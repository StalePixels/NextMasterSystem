/* loader.c: load the picked cart, find and check its overlay file (.nms),
 * apply it and start the game. Banked (PAGE_LOADER).
 *
 * The cart is read into RAM pages CART_PAGE and up, one 8K page at a time
 * through MMU 6 ($C000). This code runs from $E000, so MMU 7 is never
 * touched here. Patches are applied to the cart pages in place.
 *
 * The overlay file format is docs/nms-format.md. The loader finds the file
 * through /nm/ovl/index, or by the cart's own CRC32 when there is no index.
 * It checks the whole file (header, chunks, END) and runs every CHECK
 * before it writes anything, so a file that fails changes nothing.
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

/* where the chunks are in OVL_BUF */
struct nms {
    uint16_t len;
    const uint8_t *crcs;
    uint16_t crcs_len;
    const uint8_t *ptch;
    uint16_t ptch_len;
    const uint8_t *conf;
    uint16_t conf_len;
};

static const char hex_digits[] = "0123456789ABCDEF";
static const char index_name[] = "/nm/ovl/index";

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
        if (nm_read((uint8_t)h, OVL_BUF, 512) < 0) { code = NM_E_READ; goto out; }
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

/* Read a whole file into OVL_BUF. Returns its length, 0 if the file is
 * missing or unreadable, or 0xFFFF if it is larger than OVL_MAX. The path
 * must be in resident memory. */
static uint16_t read_file(const char *path)
{
    uint8_t extra;
    int16_t h, got;

    h = nm_open(path);
    if (h < 0) return 0;
    got = nm_read((uint8_t)h, OVL_BUF, OVL_MAX);
    if (got == (int16_t)OVL_MAX && nm_read((uint8_t)h, &extra, 1) == 1) got = -2;
    nm_close((uint8_t)h);
    if (got == -2) return 0xFFFF;
    return got < 0 ? 0 : (uint16_t)got;
}

/* The primary CRC32 of the overlay file for this cart: from the index, or
 * the cart's own CRC32 without one. Sets the name in nm.ovl_name. Returns
 * 0 or a failure code. */
static uint8_t find_overlay(void)
{
    char path[sizeof index_name];
    uint32_t primary = nm.launch.crc;
    uint16_t len, n, lo, hi, mid;
    const uint8_t *e;
    uint32_t c;

    put_hex32(nm.ovl_name + 8, nm.launch.crc);
    memcpy(path, index_name, sizeof index_name);
    len = read_file(path);
    if (len == 0) return 0;       /* no index: the file named after the cart */
    if (len < 6 || memcmp(OVL_BUF, "NMSI", 4) != 0) return NM_E_BADOVL;
    n = rd16(OVL_BUF + 4);
    if (len == 0xFFFF || (uint32_t)n * 8 + 6 > len) return NM_E_BADOVL;
    lo = 0;
    hi = n;
    while (lo < hi) {
        mid = (lo + hi) >> 1;
        e = OVL_BUF + 6 + mid * 8;
        c = rd32(e);
        if (c == nm.launch.crc) {
            primary = rd32(e + 4);
            put_hex32(nm.ovl_name + 8, primary);
            return 0;
        }
        if (c < nm.launch.crc) lo = mid + 1;
        else hi = mid;
    }
    return NM_E_NOOVL;
}

/* Read the overlay file and check its header, chunks and END. Fills f.
 * Returns 0 or a failure code. */
static uint8_t read_overlay(struct nms *f)
{
    const uint8_t *o = OVL_BUF;
    uint16_t p, n;
    uint8_t i;

    f->len = read_file(nm.ovl_name);
    if (f->len == 0) return NM_E_NOOVL;
    if (f->len == 0xFFFF || f->len < NMS_HDR + 12) return NM_E_BADOVL;
    if (o[0] != 'N' || o[1] != 'M' || o[2] != 'S' || o[3] != 0x1A) return NM_E_BADOVL;
    if (o[NMS_MAJOR] != 1) return NM_E_BADOVL;
    if (o[NMS_ABI] > FW_ABI) return NM_E_BADOVL;     /* needs a newer runtime */

    f->crcs = f->ptch = f->conf = 0;
    f->crcs_len = f->ptch_len = f->conf_len = 0;
    p = NMS_HDR;
    for (;;) {
        if (p + 8 > f->len) return NM_E_BADOVL;
        if (o[p + 6] || o[p + 7]) return NM_E_BADOVL;
        n = rd16(o + p + 4);
        if (n > f->len - p - 8) return NM_E_BADOVL;
        if (!memcmp(o + p, "END ", 4)) {
            if (n != 4 || p + 12 != f->len) return NM_E_BADOVL;
            if (crc_of(o, p) != rd32(o + p + 8)) return NM_E_BADOVL;
            break;
        }
        if (!memcmp(o + p, "CRCS", 4)) { f->crcs = o + p + 8; f->crcs_len = n; }
        else if (!memcmp(o + p, "PTCH", 4)) { f->ptch = o + p + 8; f->ptch_len = n; }
        else if (!memcmp(o + p, "CONF", 4)) { f->conf = o + p + 8; f->conf_len = n; }
        p += 8 + n;
    }
    if (!f->crcs || !f->ptch || f->ptch_len == 0) return NM_E_BADOVL;

    /* the cart must be one the file accepts */
    for (i = 0; (uint16_t)(i + 1) * 4 <= f->crcs_len; i++)
        if (rd32(f->crcs + i * 4) == nm.launch.crc) return 0;
    return NM_E_OTHER;
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

/* First pass: every CHECK, and the bounds of every operation. Writes
 * nothing. Returns 0 or a failure code. */
static uint8_t check_ops(const struct nms *f)
{
    const uint8_t *op = f->ptch;
    const uint8_t *end = f->ptch + f->ptch_len;
    uint32_t off;
    uint16_t len, k;
    uint8_t hook = 0;

    for (;;) {
        if (op >= end) return NM_E_BADOP;
        switch (op[0]) {
        case OP_END:
            return 0;
        case OP_CHECK:      /* u24 offset, u16 length, u32 CRC32 */
            if (op + 10 > end) return NM_E_BADOP;
            if (!check_range(rd24(op + 1), rd16(op + 4), rd32(op + 6))) return NM_E_DIFFER;
            op += 10;
            break;
        case OP_PATCH:      /* u24 offset, u8 n, n bytes */
            if (op + 5 > end) return NM_E_BADOP;
            off = rd24(op + 1);
            len = op[4];
            if (op + 5 + len > end) return NM_E_BADOP;
            if ((off >> 13) >= nm.launch.npages) return NM_E_BADOP;
            if (((uint16_t)off & (PAGE_SIZE - 1)) + len > PAGE_SIZE) return NM_E_BADOP;
            op += 5 + len;
            break;
        case OP_START:      /* u16 address, u16 SP */
            if (op + 5 > end) return NM_E_BADOP;
            op += 5;
            break;
        case OP_RAMSITES:   /* u16 continuation, u8 n, n entries */
            if (op + 4 > end || hook) return NM_E_BADOP;
            hook = 1;
            k = op[3];
            if (3 + 6 * k > FW2_HOOKMAX) return NM_E_BADOP;
            op += 4;
            while (k--) {
                /* u16 address, u8 length (2), u16 CRC, 2 new bytes */
                if (op + 7 > end || op[2] != 2) return NM_E_BADOP;
                op += 7;
            }
            break;
        case OP_RASTER:     /* u16 length, the routine */
            if (op + 3 > end || hook) return NM_E_BADOP;
            hook = 1;
            len = rd16(op + 1);
            if (len > FW2_HOOKMAX || op + 3 + len > end) return NM_E_BADOP;
            op += 3 + len;
            break;
        default:
            return NM_E_BADOP;
        }
    }
}

/* Second pass: apply the operations. check_ops has passed. Returns 0 or a
 * failure code. */
static uint8_t apply_ops(const struct nms *f)
{
    const uint8_t *op = f->ptch;
    uint8_t *dst;
    uint32_t off;
    uint16_t len;
    uint8_t k, old[2];

    nm.launch.start = 0;
    nm.launch.sp = 0xDFF0;
    nm.launch.hook = 0;
    nm.launch.hook2 = 0;

    for (;;) {
        switch (op[0]) {
        case OP_END:
            return 0;
        case OP_CHECK:
            op += 10;
            break;
        case OP_PATCH:
            off = rd24(op + 1);
            len = op[4];
            ZXN_WRITE_MMU6(CART_PAGE + (uint8_t)(off >> 13));
            memcpy(WINDOW + ((uint16_t)off & (PAGE_SIZE - 1)), op + 5, len);
            op += 5 + len;
            break;
        case OP_START:
            nm.launch.start = rd16(op + 1);
            nm.launch.sp = rd16(op + 3);
            if (nm.launch.sp == 0) nm.launch.sp = 0xDFF0;
            op += 5;
            break;
        case OP_RAMSITES:
            /* the framework's table: u16 continuation, u8 n, then n x
             * (u16 address, 2 original bytes, 2 new bytes) */
            ZXN_WRITE_MMU6(FW2_PAGE);
            dst = WINDOW + FW2_HOOKOFF;
            *dst++ = op[1];
            *dst++ = op[2];
            *dst++ = k = op[3];
            op += 4;
            while (k--) {
                if (!ramsite_old(op + 5, rd16(op + 3), old)) return NM_E_BADOP;
                ZXN_WRITE_MMU6(FW2_PAGE);
                *dst++ = op[0];
                *dst++ = op[1];
                *dst++ = old[0];
                *dst++ = old[1];
                *dst++ = op[5];
                *dst++ = op[6];
                op += 7;
            }
            nm.launch.hook2 = FW2_HOOK;
            break;
        case OP_RASTER:
            len = rd16(op + 1);
            ZXN_WRITE_MMU6(FW2_PAGE);
            memcpy(WINDOW + FW2_HOOKOFF, op + 3, len);
            nm.launch.hook = FW2_HOOK;
            op += 3 + len;
            break;
        }
    }
}

/* Does the CONF line at p, of n bytes, equal s? */
static uint8_t conf_is(const uint8_t *p, uint16_t n, const char *s)
{
    uint16_t l = strlen(s);

    return n == l && !memcmp(p, s, l);
}

/* CONF switches: priority=1 and toppal=1. Unknown keys are skipped. */
static void apply_conf(const struct nms *f)
{
    const uint8_t *p = f->conf;
    const uint8_t *end = f->conf + f->conf_len;
    const uint8_t *e;

    nm.launch.flags = 0;
    if (!p) return;
    while (p < end) {
        for (e = p; e < end && *e != '\n'; e++)
            ;
        if (conf_is(p, e - p, "priority=1")) nm.launch.flags |= 1;
        if (conf_is(p, e - p, "toppal=1")) nm.launch.flags |= 2;
        p = e + 1;
    }
}

void *loader_load(void *unused)
{
    struct nms f;
    uint8_t code;

    (void)unused;
    code = read_cart();
    if (!code) code = find_overlay();
    if (!code) code = read_overlay(&f);
    if (!code) code = check_ops(&f);
    if (!code) code = apply_ops(&f);
    ZXN_WRITE_MMU6(0);
    if (code) return (void *)(uintptr_t)code;
    apply_conf(&f);
    NM_FAR(PAGE_INFO, info_show, 0);
    nm_launch(&nm.launch);
    return 0;
}
