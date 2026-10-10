/* loader.c: load the picked cart, find and check its overlay file (.nms),
 * apply it and start the game. Banked (PAGE_LOADER). The index lookup and
 * steps 2 to 4 below are in the overlay module (overlay/overlay.c,
 * PAGE_OVERLAY); the file reader is resident (rd.c). nms.h has what they
 * share.
 *
 * The cart is read into RAM pages CART_PAGE and up, one 8K page at a time
 * through MMU 6 ($C000). This code runs from $E000, so MMU 7 is never
 * touched here. Patches are applied to the cart pages in place.
 *
 * The overlay file format is docs/nms-format.md. The loader finds the file
 * through ovl/index in the start folder, or by the cart's own CRC32 when there is no index.
 * Neither file is ever held whole in memory. Both are read through OVL_BUF,
 * which holds OVL_BUFSIZE bytes, so a file or a chunk may be of any size.
 *
 * The overlay file is read in these steps:
 *   1. The walk reads every byte from the start of the file to END, in
 *      order, into the running CRC32. It checks the header and every chunk
 *      header and notes where CRCS, PTCH, CONF and META start. It puts the
 *      code of each PAGE chunk into its RAM page and its entries into the
 *      framework's table. Other chunks are read only for the CRC32. END
 *      must be last and must match.
 *   2. CRCS, META and CONF are read again from their start (F_SEEK).
 *   3. PTCH, first pass: every CHECK runs against the cart, and every
 *      operation is checked. Nothing is written.
 *   4. PTCH, second pass: the operations are applied.
 * A file that fails at any step before the last changes nothing.
 *
 * loader_load returns a failure code (NM_E_*). On success it does not
 * return: it calls nm_launch.
 */
#include <arch/zxn.h>
#include <string.h>

#include "nm.h"
#include "nms.h"

/* crc32.asm */
struct crc_job {
    const uint8_t *data;
    uint16_t       len;
};
void     crc32_init(void);
void     crc32_update(struct crc_job *job) __z88dk_fastcall;
uint32_t crc32_final(void);

/* .nms header */
#define NMS_MAJOR   4
#define NMS_MINOR   5
#define NMS_ABI     6
#define NMS_HDR     16

/* The framework's table of code pages in its second page (pg_tab in
 * src/runtime/fw2.asm): the RAM page, the number of entries and the first
 * entry of each page number, then the entry addresses. Page code runs at
 * $2000-$3FFF. */
#define PG_TABOFF   (PG_TAB - 0x2000u)
#define PG_RAM      0
#define PG_N        CODE_MAX
#define PG_FIRST    (2 * CODE_MAX)
#define PG_ENT      (3 * CODE_MAX)
#define PG_ORG      0x2000u

static const char chunk_tags[] = "CRCSPTCHCONFMETA";

/* The running CRC32 over len bytes at data. */
static void crc_job_at(const uint8_t *data, uint16_t len)
{
    struct crc_job job;

    job.data = data;
    job.len = len;
    crc32_update(&job);
}

static uint32_t crc_of(const uint8_t *data, uint16_t len)
{
    crc32_init();
    crc_job_at(data, len);
    return crc32_final();
}

/* Read the cart into pages, compute its CRC32. Returns 0 or a failure code. */
static uint8_t read_cart(void)
{
    uint8_t stat[16];
    uint32_t size;
    int16_t h, got;
    uint8_t np, page, code = 0;

    h = nm_open(nm_name);
    if (h < 0) return NM_E_OPEN;
    if (nm_fstat((uint8_t)h, stat)) { code = NM_E_READ; goto out; }
    size = *(uint32_t *)(stat + 7);

    /* a 512-byte copier header: size mod 16384 is 512 */
    if ((size & 0x3FFF) == 0x200) {
        if (nm_seek((uint8_t)h, 512)) { code = NM_E_READ; goto out; }
        size -= 512;
    }
    if ((size >> 24) != 0 || (size >> 8) >= (uint32_t)MAX_PAGES * 32 + 1) {
        code = NM_E_SIZE;
        goto out;
    }
    np = (uint8_t)((size + (PAGE_SIZE - 1)) >> 13);
    if (np == 0) { code = NM_E_SIZE; goto out; }

    crc32_init();
    for (page = 0; page < np; page++) {
        ZXN_WRITE_MMU6(CART_PAGE + page);
        got = nm_read((uint8_t)h, WINDOW, PAGE_SIZE);
        if (got < 0) { code = NM_E_READ; goto out; }
        crc_job_at(WINDOW, (uint16_t)got);
        if ((uint16_t)got < PAGE_SIZE)
            memset(WINDOW + got, 0xFF, PAGE_SIZE - got);
    }
    nm.launch.crc = crc32_final();
    nm.launch.size = size;
    nm.launch.npages = np;
out:
    ZXN_WRITE_MMU6(0);
    nm_close((uint8_t)h);
    return code;
}

/* The next n bytes of the run in one piece, as rd_take, and through the
 * running CRC32. */
static const uint8_t *rd_crc(struct rd *r, uint16_t n)
{
    const uint8_t *p = rd_take(r, n);

    if (p) crc_job_at(p, n);
    return p;
}

/* A PAGE chunk of n bytes, during the walk: its entries into the
 * framework's table, its code into RAM page CODE_PAGE + its page number,
 * and every byte through the running CRC32. *used counts the entries of
 * the pages so far. Returns 0 or a failure code. */
static uint8_t load_page(struct rd *r, uint32_t n, uint8_t *used)
{
    const uint8_t *p;
    uint8_t *tab = WINDOW + PG_TABOFF;
    uint16_t len;
    uint8_t num, e, k;

    if (n > 2 + 2 * 255 + PAGE_SIZE || !(p = rd_crc(r, 2))) return NM_E_BADOVL;
    num = p[0];
    e = p[1];
    len = (uint16_t)n - 2 - 2 * e;      /* the code; wraps when n is too short */
    if (num >= CODE_MAX || !e || len > PAGE_SIZE || *used + e > CODE_ENTS) return NM_E_BADOVL;
    ZXN_WRITE_MMU6(FW2_PAGE);
    if (tab[PG_RAM + num]) return NM_E_BADOVL;      /* each page number once */
    tab[PG_N + num] = e;
    tab[PG_FIRST + num] = *used;
    k = PG_ENT + 2 * *used;
    *used += e;
    while (e--) {
        /* an entry address inside the code */
        if (!(p = rd_crc(r, 2)) || (uint16_t)(rd16(p) - PG_ORG) >= len) return NM_E_BADOVL;
        tab[k++] = p[0];
        tab[k++] = p[1];
    }
    tab[PG_RAM + num] = CODE_PAGE + num;
    ZXN_WRITE_MMU6(CODE_PAGE + num);
    if (rd_copy(r, WINDOW, len)) return NM_E_BADOVL;
    crc_job_at(WINDOW, len);
    memset(WINDOW + len, 0, PAGE_SIZE - len);
    return 0;
}

/* Step 1, the walk: the header, every chunk and END, through the running
 * CRC32. Fills f, and loads the PAGE chunks. Returns 0 or a failure code. */
static uint8_t walk(struct nms *f)
{
    struct rd r;
    const uint8_t *p;
    uint32_t n;
    uint16_t k;
    uint8_t i, used = 0;

    ZXN_WRITE_MMU6(FW2_PAGE);       /* no code pages until a PAGE chunk */
    memset(WINDOW + PG_TABOFF + PG_RAM, 0, CODE_MAX);

    if (rd_open(&r, f->h, 0, f->size)) return NM_E_BADOVL;
    p = rd_take(&r, NMS_HDR);
    if (!p || p[0] != 'N' || p[1] != 'M' || p[2] != 'S' || p[3] != 0x1A) return NM_E_BADOVL;
    if (p[NMS_MAJOR] != 1) return NM_E_BADOVL;
    if (p[NMS_ABI] > FW_ABI) return NM_E_BADOVL;     /* needs a newer runtime */
    nm.nms_ver[0] = p[NMS_MAJOR];
    nm.nms_ver[1] = p[NMS_MINOR];
    nm.nms_ver[2] = p[NMS_ABI];
    crc32_init();
    crc_job_at(p, NMS_HDR);

    f->seen = 0;
    for (;;) {
        p = rd_take(&r, 8);
        if (!p) return NM_E_BADOVL;
        n = rd32(p + 4);
        if (n > rd_left(&r)) return NM_E_BADOVL;
        if (!memcmp(p, "END ", 4)) break;
        for (i = 0; i < C_N; i++) {
            if (memcmp(p, chunk_tags + 4 * i, 4)) continue;
            if (f->seen & (1 << i)) return NM_E_BADOVL;   /* each only once */
            f->seen |= 1 << i;
            f->at[i] = f->size - rd_left(&r);
            f->len[i] = n;
        }
        crc_job_at(p, 8);
        if (!memcmp(p, "PAGE", 4)) {
            i = load_page(&r, n, &used);
            if (i) return i;
            continue;
        }
        /* any other chunk's data: only for the CRC32 here */
        while (n) {
            p = rd_piece(&r, n > OVL_BUFSIZE ? OVL_BUFSIZE : (uint16_t)n, &k);
            if (!p) return NM_E_BADOVL;
            crc_job_at(p, k);
            n -= k;
        }
    }

    /* END: the CRC32 of every byte before its header, and nothing after it */
    if (n != 4) return NM_E_BADOVL;
    p = rd_take(&r, 4);
    if (!p || rd_left(&r) != 0) return NM_E_BADOVL;
    if (crc32_final() != rd32(p)) return NM_E_BADOVL;
    if ((f->seen & ((1 << C_CRCS) | (1 << C_PTCH))) != ((1 << C_CRCS) | (1 << C_PTCH)))
        return NM_E_BADOVL;
    if (f->len[C_PTCH] == 0) return NM_E_BADOVL;
    return 0;
}

/* CRC32 of len bytes of the cart from offset off. Returns 1 when it equals
 * crc. Bytes past the end of the cart make the check fail. */
static uint8_t check_range(uint32_t off, uint16_t len, uint32_t crc)
{
    uint16_t in, k;

    if (off + len > nm.launch.size) return 0;
    crc32_init();
    while (len) {
        in = (uint16_t)off & (PAGE_SIZE - 1);
        k = PAGE_SIZE - in;
        if (k > len) k = len;
        ZXN_WRITE_MMU6(CART_PAGE + (uint8_t)(off >> 13));
        crc_job_at(WINDOW + in, k);
        off += k;
        len -= k;
    }
    return crc32_final() == crc;
}

/* The original instruction of a RAMSITES entry. new holds the RST and the
 * inline code; the original is OUT (n),A or IN A,(n) with n in the code's
 * port class, or ED and the code. The one whose CRC32 has the entry's low
 * 16 bits is written to out. Returns 0 when none has. */
static uint8_t ramsite_old(const uint8_t *new, uint16_t crc16, uint8_t *out)
{
    uint8_t code = new[1];
    uint8_t cls, p;

    if (code >= 16) {
        out[0] = 0xED;
        out[1] = code;
        return (uint16_t)crc_of(out, 2) == crc16;
    }
    out[0] = code < 8 ? 0xD3 : 0xDB;
    cls = code & 7;
    p = 0;
    do {
        /* port class: bits A7, A6 and A0 of the port */
        if ((uint8_t)(((p >> 5) & 6) | (p & 1)) == cls) {
            out[1] = p;
            if ((uint16_t)crc_of(out, 2) == crc16) return 1;
        }
    } while (++p);
    return 0;
}

/* check_range and ramsite_old for the overlay module, which has no CRC32
 * code of its own. */
void *loader_check_range(void *arg)
{
    const struct crc_range *a = (const struct crc_range *)arg;

    return (void *)(uintptr_t)check_range(a->off, a->len, a->crc);
}

void *loader_ramsite_old(void *arg)
{
    const struct ramsite *a = (const struct ramsite *)arg;

    return (void *)(uintptr_t)ramsite_old(a->new, a->crc16, a->out);
}

/* Open the overlay file named in nm.ovl_name, check it and apply it.
 * Returns 0 or a failure code. */
static uint8_t use_overlay(void)
{
    struct nms f;
    uint8_t stat[16];
    int16_t h;
    uint8_t code;

    h = nm_open(nm.ovl_name);
    if (h < 0) return NM_E_NOOVL;
    f.h = (uint8_t)h;
    code = nm_fstat(f.h, stat) ? NM_E_BADOVL : 0;
    f.size = *(uint32_t *)(stat + 7);
    if (!code) code = walk(&f);
    if (!code) code = (uint8_t)(uintptr_t)NM_FAR(PAGE_OVERLAY, overlay_apply, &f);
    nm_close(f.h);
    return code;
}

void *loader_load(void *unused)
{
    uint8_t code;

    (void)unused;
    code = read_cart();
    if (!code) code = (uint8_t)(uintptr_t)NM_FAR(PAGE_OVERLAY, overlay_find, 0);
    if (!code) code = use_overlay();
    ZXN_WRITE_MMU6(0);
    if (code) return (void *)(uintptr_t)code;
    NM_FAR(PAGE_INFO, info_show, 0);
    nm_launch(&nm.launch);
    return 0;
}
