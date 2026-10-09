/* loader.c: load the picked cart, find and check its overlay file (.nms),
 * apply it and start the game. Banked (PAGE_LOADER).
 *
 * The cart is read into RAM pages CART_PAGE and up, one 8K page at a time
 * through MMU 6 ($C000). This code runs from $E000, so MMU 7 is never
 * touched here. Patches are applied to the cart pages in place.
 *
 * The overlay file format is docs/nms-format.md. The loader finds the file
 * through /nm/ovl/index, or by the cart's own CRC32 when there is no index.
 * Neither file is ever held whole in memory. Both are read through OVL_BUF,
 * which holds OVL_BUFSIZE bytes, so a file or a chunk may be of any size.
 *
 * The overlay file is read in these steps:
 *   1. The walk reads every byte from the start of the file to END, in
 *      order, into the running CRC32. It checks the header and every chunk
 *      header and notes where CRCS, PTCH, CONF and META start. Other chunks
 *      are read only for the CRC32. END must be last and must match.
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

/* PTCH opcodes */
#define OP_END      0
#define OP_CHECK    1
#define OP_PATCH    2
#define OP_START    3
#define OP_RAMSITES 4
#define OP_RASTER   5

/* The framework's second page holds the RASTER routine or the RAMSITES
 * table from $3C00 to $3FFF (rast_code in src/runtime/fw2.asm). */
#define FW2_HOOK    0x3C00u
#define FW2_HOOKOFF 0x1C00u
#define FW2_HOOKMAX 0x400u

#define WINDOW      ((uint8_t *)0xC000)   /* MMU 6 */
#define PAGE_SIZE   0x2000u

/* The chunks the loader reads after the walk, in the order of chunk_tags. */
#define C_CRCS      0
#define C_PTCH      1
#define C_CONF      2
#define C_META      3
#define C_N         4

/* A META or CONF line is cut to this length: "title=" and the title. */
#define LINE_MAX    (6 + NM_TITLE_MAX)

/* An open overlay file and where its chunks are. at[] is the file offset
 * of a chunk's data, len[] its length, seen has bit 1 << C_x set for each
 * chunk the file has. */
struct nms {
    uint8_t  h;
    uint8_t  seen;
    uint32_t size;
    uint32_t at[C_N];
    uint32_t len[C_N];
};

/* A run of bytes of a file, read in order through OVL_BUF. The bytes from
 * OVL_BUF + at to OVL_BUF + fill are read but not handed out yet. left is
 * the number of bytes of the run still in the file. */
struct rd {
    uint8_t  h;
    uint16_t at;
    uint16_t fill;
    uint32_t left;
};

static const char hex_digits[] = "0123456789ABCDEF";
static const char index_name[] = "/nm/ovl/index";
static const char chunk_tags[] = "CRCSPTCHCONFMETA";

static void put_hex32(char *out, uint32_t v)
{
    uint8_t i;

    for (i = 0; i < 8; i++) {
        out[i] = hex_digits[(v >> 28) & 15];
        v <<= 4;
    }
}

static uint32_t rd24(const uint8_t *p)
{
    return (uint32_t)p[0] | ((uint32_t)p[1] << 8) | ((uint32_t)p[2] << 16);
}

static uint16_t rd16(const uint8_t *p)
{
    return p[0] | (p[1] << 8);
}

static uint32_t rd32(const uint8_t *p)
{
    return *(const uint32_t *)p;
}

static uint32_t crc_of(const uint8_t *data, uint16_t len)
{
    struct crc_job job;

    crc32_init();
    job.data = data;
    job.len = len;
    crc32_update(&job);
    return crc32_final();
}

/* Read the cart into pages, compute its CRC32. Returns 0 or a failure code. */
static uint8_t read_cart(void)
{
    uint8_t stat[16];
    struct crc_job job;
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
        job.data = WINDOW;
        job.len = (uint16_t)got;
        crc32_update(&job);
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

/* ---- reading a file through OVL_BUF ------------------------------------- */

/* Start a run of len bytes of the file from offset pos. Returns 0, or 1
 * when the seek fails. */
static uint8_t rd_open(struct rd *r, uint8_t h, uint32_t pos, uint32_t len)
{
    r->h = h;
    r->at = 0;
    r->fill = 0;
    r->left = len;
    return nm_seek(h, pos) != 0;
}

/* The bytes of the run not handed out yet. */
static uint32_t rd_left(const struct rd *r)
{
    return r->left + (r->fill - r->at);
}

/* Move the bytes not handed out yet to the start of OVL_BUF and read more
 * of the run after them. A failed read ends the run. */
static void rd_more(struct rd *r)
{
    uint16_t keep = r->fill - r->at;
    uint16_t k;

    if (keep && r->at) memmove(OVL_BUF, OVL_BUF + r->at, keep);
    r->at = 0;
    r->fill = keep;
    k = OVL_BUFSIZE - keep;
    if (k > r->left) k = (uint16_t)r->left;
    if (!k) return;
    if (nm_read(r->h, OVL_BUF + keep, k) != (int16_t)k) {
        r->left = 0;
        return;
    }
    r->fill += k;
    r->left -= k;
}

/* The next n bytes of the run, n at most OVL_BUFSIZE, in one piece. Returns
 * 0 when the run has fewer. The pointer is good until the next call. */
static const uint8_t *rd_take(struct rd *r, uint16_t n)
{
    const uint8_t *p;

    if (r->fill - r->at < n) {
        rd_more(r);
        if (r->fill - r->at < n) return 0;
    }
    p = OVL_BUF + r->at;
    r->at += n;
    return p;
}

/* The next bytes of the run: at least 1 and at most n, the number in *got.
 * Returns 0 when the run is over. */
static const uint8_t *rd_piece(struct rd *r, uint16_t n, uint16_t *got)
{
    const uint8_t *p;
    uint16_t k;

    if (r->fill == r->at) {
        rd_more(r);
        if (r->fill == r->at) return 0;
    }
    k = r->fill - r->at;
    if (k > n) k = n;
    p = OVL_BUF + r->at;
    r->at += k;
    *got = k;
    return p;
}

/* Skip n bytes of the run. Returns 0, or 1 when the run has fewer. */
static uint8_t rd_skip(struct rd *r, uint16_t n)
{
    uint16_t k;

    while (n) {
        if (!rd_piece(r, n, &k)) return 1;
        n -= k;
    }
    return 0;
}

/* The next line of the run, without its $0A, into line, cut to LINE_MAX
 * bytes. Returns the line's whole length, or -1 when the run is over. */
static int16_t rd_line(struct rd *r, char *line)
{
    const uint8_t *p;
    int16_t n = 0;

    if (!rd_left(r)) return -1;
    while ((p = rd_take(r, 1)) != 0 && *p != '\n') {
        if (n < LINE_MAX) line[n] = (char)*p;
        if (n < 0x7FFF) n++;
    }
    return n;
}

/* ---- the alias index ------------------------------------------------------ */

/* The primary CRC32 of the overlay file for this cart: from the index, or
 * the cart's own CRC32 without one. Sets the name in nm.ovl_name. Returns
 * 0 or a failure code.
 *
 * The index is searched in place: a binary search that seeks to each probed
 * entry and reads its 8 bytes. */
static uint8_t find_overlay(void)
{
    char path[sizeof index_name];
    uint8_t stat[16];
    uint16_t n, lo, hi, mid;
    uint32_t c;
    int16_t h;
    uint8_t code = NM_E_NOOVL;

    put_hex32(nm.ovl_name + 8, nm.launch.crc);
    memcpy(path, index_name, sizeof index_name);
    h = nm_open(path);
    if (h < 0) return 0;          /* no index: the file named after the cart */
    if (nm_fstat((uint8_t)h, stat) || nm_read((uint8_t)h, OVL_BUF, 6) != 6 ||
        memcmp(OVL_BUF, "NMSI", 4) != 0) {
        code = NM_E_BADOVL;
        goto out;
    }
    n = rd16(OVL_BUF + 4);
    if ((uint32_t)n * 8 + 6 > *(uint32_t *)(stat + 7)) { code = NM_E_BADOVL; goto out; }
    lo = 0;
    hi = n;
    while (lo < hi) {
        mid = lo + ((hi - lo) >> 1);
        if (nm_seek((uint8_t)h, 6 + (uint32_t)mid * 8) ||
            nm_read((uint8_t)h, OVL_BUF, 8) != 8) {
            code = NM_E_BADOVL;
            break;
        }
        c = rd32(OVL_BUF);
        if (c == nm.launch.crc) {
            put_hex32(nm.ovl_name + 8, rd32(OVL_BUF + 4));
            code = 0;
            break;
        }
        if (c < nm.launch.crc) lo = mid + 1;
        else hi = mid;
    }
out:
    nm_close((uint8_t)h);
    return code;
}

/* ---- the overlay file ------------------------------------------------------- */

/* Step 1, the walk: the header, every chunk and END, through the running
 * CRC32. Fills f. Returns 0 or a failure code. */
static uint8_t walk(struct nms *f)
{
    struct rd r;
    struct crc_job job;
    const uint8_t *p;
    uint32_t n;
    uint16_t k;
    uint8_t i;

    if (rd_open(&r, f->h, 0, f->size)) return NM_E_BADOVL;
    p = rd_take(&r, NMS_HDR);
    if (!p || p[0] != 'N' || p[1] != 'M' || p[2] != 'S' || p[3] != 0x1A) return NM_E_BADOVL;
    if (p[NMS_MAJOR] != 1) return NM_E_BADOVL;
    if (p[NMS_ABI] > FW_ABI) return NM_E_BADOVL;     /* needs a newer runtime */
    nm.nms_ver[0] = p[NMS_MAJOR];
    nm.nms_ver[1] = p[NMS_MINOR];
    nm.nms_ver[2] = p[NMS_ABI];
    crc32_init();
    job.data = p;
    job.len = NMS_HDR;
    crc32_update(&job);

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
        job.data = p;
        job.len = 8;
        crc32_update(&job);
        /* The chunk's data. Loading PAGE chunks slots in here: see
         * docs/design.md, "Loading an overlay file". */
        while (n) {
            job.data = rd_piece(&r, n > OVL_BUFSIZE ? OVL_BUFSIZE : (uint16_t)n, &k);
            if (!job.data) return NM_E_BADOVL;
            job.len = k;
            crc32_update(&job);
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

/* Start a run over chunk c of f. Returns 0 or 1 when the seek fails. */
static uint8_t open_chunk(struct rd *r, const struct nms *f, uint8_t c)
{
    return rd_open(r, f->h, f->at[c], f->len[c]);
}

/* Does CRCS list the cart? Returns 0 or a failure code. */
static uint8_t accepts(const struct nms *f)
{
    struct rd r;
    const uint8_t *p;
    uint32_t n = f->len[C_CRCS] >> 2;

    if (open_chunk(&r, f, C_CRCS)) return NM_E_BADOVL;
    while (n--) {
        p = rd_take(&r, 4);
        if (!p) return NM_E_BADOVL;
        if (rd32(p) == nm.launch.crc) return 0;
    }
    return NM_E_OTHER;
}

/* The META title into nm.title, cut to NM_TITLE_MAX characters; empty if
 * the file has none. Returns 0 or a failure code. */
static uint8_t read_title(const struct nms *f)
{
    struct rd r;
    char line[LINE_MAX];
    int16_t n;

    nm.title[0] = 0;
    if (!(f->seen & (1 << C_META))) return 0;
    if (open_chunk(&r, f, C_META)) return NM_E_BADOVL;
    while ((n = rd_line(&r, line)) >= 0) {
        if (n < 6 || memcmp(line, "title=", 6)) continue;
        n -= 6;
        if (n > NM_TITLE_MAX) n = NM_TITLE_MAX;
        memcpy(nm.title, line + 6, n);
        nm.title[n] = 0;
        break;
    }
    return 0;
}

/* Is the CONF line in line, of length n, equal to s? */
static uint8_t conf_is(const char *line, int16_t n, const char *s)
{
    int16_t l = (int16_t)strlen(s);

    return n == l && !memcmp(line, s, l);
}

/* CONF switches: priority=1 and toppal=1. Unknown keys are skipped.
 * Returns 0 or a failure code. */
static uint8_t read_conf(const struct nms *f)
{
    struct rd r;
    char line[LINE_MAX];
    int16_t n;

    nm.launch.flags = 0;
    if (!(f->seen & (1 << C_CONF))) return 0;
    if (open_chunk(&r, f, C_CONF)) return NM_E_BADOVL;
    while ((n = rd_line(&r, line)) >= 0) {
        if (conf_is(line, n, "priority=1")) nm.launch.flags |= 1;
        if (conf_is(line, n, "toppal=1")) nm.launch.flags |= 2;
    }
    return 0;
}

/* CRC32 of len bytes of the cart from offset off. Returns 1 when it equals
 * crc. Bytes past the end of the cart make the check fail. */
static uint8_t check_range(uint32_t off, uint16_t len, uint32_t crc)
{
    struct crc_job job;
    uint16_t in, k;

    if (off + len > nm.launch.size) return 0;
    crc32_init();
    while (len) {
        in = (uint16_t)off & (PAGE_SIZE - 1);
        k = PAGE_SIZE - in;
        if (k > len) k = len;
        ZXN_WRITE_MMU6(CART_PAGE + (uint8_t)(off >> 13));
        job.data = WINDOW + in;
        job.len = k;
        crc32_update(&job);
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

/* Step 3, PTCH first pass: every CHECK, the bounds of every operation and
 * the original of every RAMSITES entry. Writes nothing. Returns 0 or a
 * failure code. */
static uint8_t check_ops(const struct nms *f)
{
    struct rd r;
    const uint8_t *p;
    uint32_t off;
    uint16_t len;
    uint8_t k, hook = 0, old[2];

    if (open_chunk(&r, f, C_PTCH)) return NM_E_BADOVL;
    for (;;) {
        p = rd_take(&r, 1);
        if (!p) return NM_E_BADOP;
        switch (*p) {
        case OP_END:
            return 0;
        case OP_CHECK:      /* u24 offset, u16 length, u32 CRC32 */
            p = rd_take(&r, 9);
            if (!p) return NM_E_BADOP;
            if (!check_range(rd24(p), rd16(p + 3), rd32(p + 5))) return NM_E_DIFFER;
            break;
        case OP_PATCH:      /* u24 offset, u8 n, n bytes */
            p = rd_take(&r, 4);
            if (!p) return NM_E_BADOP;
            off = rd24(p);
            len = p[3];
            if ((off >> 13) >= nm.launch.npages) return NM_E_BADOP;
            if (((uint16_t)off & (PAGE_SIZE - 1)) + len > PAGE_SIZE) return NM_E_BADOP;
            if (rd_skip(&r, len)) return NM_E_BADOP;
            break;
        case OP_START:      /* u16 address, u16 SP */
            if (!rd_take(&r, 4)) return NM_E_BADOP;
            break;
        case OP_RAMSITES:   /* u16 continuation, u8 n, n entries */
            p = rd_take(&r, 3);
            if (!p || hook) return NM_E_BADOP;
            hook = 1;
            k = p[2];
            if (3 + 6 * (uint16_t)k > FW2_HOOKMAX) return NM_E_BADOP;
            while (k--) {
                /* u16 address, u8 length (2), u16 CRC, 2 new bytes */
                p = rd_take(&r, 7);
                if (!p || p[2] != 2) return NM_E_BADOP;
                if (!ramsite_old(p + 5, rd16(p + 3), old)) return NM_E_BADOP;
            }
            break;
        case OP_RASTER:     /* u16 length, the routine */
            p = rd_take(&r, 2);
            if (!p || hook) return NM_E_BADOP;
            hook = 1;
            len = rd16(p);
            if (len > FW2_HOOKMAX || rd_skip(&r, len)) return NM_E_BADOP;
            break;
        default:
            return NM_E_BADOP;
        }
    }
}

/* Copy the next len bytes of the run to dst. Returns 0, or 1 when the run
 * has fewer. */
static uint8_t rd_copy(struct rd *r, uint8_t *dst, uint16_t len)
{
    const uint8_t *p;
    uint16_t k;

    while (len) {
        p = rd_piece(r, len, &k);
        if (!p) return 1;
        memcpy(dst, p, k);
        dst += k;
        len -= k;
    }
    return 0;
}

/* Step 4, PTCH second pass: apply the operations. check_ops has passed, so
 * only a failed read can stop it. Returns 0 or a failure code. */
static uint8_t apply_ops(const struct nms *f)
{
    struct rd r;
    const uint8_t *p;
    uint8_t *dst;
    uint32_t off;
    uint16_t len;
    uint8_t k, old[2];

    nm.launch.start = 0;
    nm.launch.sp = 0xDFF0;
    nm.launch.hook = 0;
    nm.launch.hook2 = 0;

    if (open_chunk(&r, f, C_PTCH)) return NM_E_BADOVL;
    for (;;) {
        p = rd_take(&r, 1);
        if (!p) return NM_E_BADOVL;
        switch (*p) {
        case OP_END:
            return 0;
        case OP_CHECK:
            if (!rd_take(&r, 9)) return NM_E_BADOVL;
            break;
        case OP_PATCH:
            p = rd_take(&r, 4);
            if (!p) return NM_E_BADOVL;
            off = rd24(p);
            len = p[3];
            ZXN_WRITE_MMU6(CART_PAGE + (uint8_t)(off >> 13));
            if (rd_copy(&r, WINDOW + ((uint16_t)off & (PAGE_SIZE - 1)), len)) return NM_E_BADOVL;
            break;
        case OP_START:
            p = rd_take(&r, 4);
            if (!p) return NM_E_BADOVL;
            nm.launch.start = rd16(p);
            nm.launch.sp = rd16(p + 2);
            if (nm.launch.sp == 0) nm.launch.sp = 0xDFF0;
            break;
        case OP_RAMSITES:
            /* the framework's table: u16 continuation, u8 n, then n x
             * (u16 address, 2 original bytes, 2 new bytes) */
            p = rd_take(&r, 3);
            if (!p) return NM_E_BADOVL;
            ZXN_WRITE_MMU6(FW2_PAGE);
            dst = WINDOW + FW2_HOOKOFF;
            *dst++ = p[0];
            *dst++ = p[1];
            *dst++ = k = p[2];
            while (k--) {
                p = rd_take(&r, 7);
                if (!p) return NM_E_BADOVL;
                ramsite_old(p + 5, rd16(p + 3), old);
                *dst++ = p[0];
                *dst++ = p[1];
                *dst++ = old[0];
                *dst++ = old[1];
                *dst++ = p[5];
                *dst++ = p[6];
            }
            nm.launch.hook2 = FW2_HOOK;
            break;
        case OP_RASTER:
            p = rd_take(&r, 2);
            if (!p) return NM_E_BADOVL;
            len = rd16(p);
            ZXN_WRITE_MMU6(FW2_PAGE);
            if (rd_copy(&r, WINDOW + FW2_HOOKOFF, len)) return NM_E_BADOVL;
            nm.launch.hook = FW2_HOOK;
            break;
        default:
            return NM_E_BADOP;
        }
    }
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
    if (!code) code = accepts(&f);
    if (!code) code = read_title(&f);
    if (!code) code = read_conf(&f);
    if (!code) code = check_ops(&f);
    if (!code) code = apply_ops(&f);
    nm_close(f.h);
    return code;
}

void *loader_load(void *unused)
{
    uint8_t code;

    (void)unused;
    code = read_cart();
    if (!code) code = find_overlay();
    if (!code) code = use_overlay();
    ZXN_WRITE_MMU6(0);
    if (code) return (void *)(uintptr_t)code;
    NM_FAR(PAGE_INFO, info_show, 0);
    nm_launch(&nm.launch);
    return 0;
}
