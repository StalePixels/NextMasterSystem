/* overlay.c: the overlay file's index and chunks. Banked (PAGE_OVERLAY).
 *
 * The loader (loader.c) far-calls this module twice for a picked cart:
 * overlay_find looks the cart up in the alias index, and, after the walk
 * has checked the whole file, overlay_apply reads CRCS, META and CONF and
 * runs the two passes over PTCH. The format is docs/nms-format.md; the
 * steps are listed in loader.c.
 *
 * The CRC32 code is in the loader's page, so the PTCH checks that need it
 * (a CHECK operation's range, a RAMSITES entry's original instruction)
 * far-call the loader for them.
 */
#include <arch/zxn.h>
#include <string.h>

#include "nm.h"
#include "nms.h"

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

/* A META or CONF line is cut to this length: "title=" and the title. */
#define LINE_MAX    (6 + NM_TITLE_MAX)

static const char hex_digits[] = "0123456789ABCDEF";

/* CRC32 checks, in the loader's page. */
static uint8_t check_range(uint32_t off, uint16_t len, uint32_t crc)
{
    struct crc_range a;

    a.off = off;
    a.len = len;
    a.crc = crc;
    return (uint8_t)(uintptr_t)NM_FAR(PAGE_LOADER, loader_check_range, &a);
}

static uint8_t ramsite_old(const uint8_t *new, uint16_t crc16, uint8_t *out)
{
    struct ramsite a;

    a.new = new;
    a.crc16 = crc16;
    a.out = out;
    return (uint8_t)(uintptr_t)NM_FAR(PAGE_LOADER, loader_ramsite_old, &a);
}

static void put_hex32(char *out, uint32_t v)
{
    uint8_t i;

    for (i = 0; i < 8; i++) {
        out[i] = hex_digits[(v >> 28) & 15];
        v <<= 4;
    }
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

/* nm.ovl_name after the folder: the CRC32 in hex and ".nms". */
static void set_ovl_name(uint32_t crc)
{
    put_hex32(nm.ovl_name + nm.ovl_len, crc);
    memcpy(nm.ovl_name + nm.ovl_len + 8, ".nms", 5);
}

/* The primary CRC32 of the overlay file for this cart: from the index, or
 * the cart's own CRC32 without one. Sets the name in nm.ovl_name. Returns
 * 0 or a failure code.
 *
 * The index is searched in place: a binary search that seeks to each probed
 * entry and reads its 8 bytes. */
static uint8_t find_overlay(void)
{
    uint8_t stat[16];
    uint16_t n, lo, hi, mid;
    uint32_t c;
    int16_t h;
    uint8_t code = NM_E_NOOVL;

    /* the index shares the folder: its name overwrites the file name, which
     * is set again once the index has been read */
    memcpy(nm.ovl_name + nm.ovl_len, "index", 6);
    h = nm_open(nm.ovl_name);
    set_ovl_name(nm.launch.crc);
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
            set_ovl_name(rd32(OVL_BUF + 4));
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

/* The value of the META line in line, of length n, when its key is key
 * (with its "="), into out, cut to max characters. */
static void meta_take(const char *line, int16_t n, const char *key, char *out, uint8_t max)
{
    int16_t k = (int16_t)strlen(key);

    if (n < k || memcmp(line, key, k)) return;
    n -= k;
    if (n > LINE_MAX - k) n = LINE_MAX - k;
    if (n > max) n = max;
    memcpy(out, line + k, n);
    out[n] = 0;
}

/* The META title into nm.title and status into nm.status, cut to fit; each
 * empty if the file has none. Returns 0 or a failure code. */
static uint8_t read_meta(const struct nms *f)
{
    struct rd r;
    char line[LINE_MAX];
    int16_t n;

    nm.title[0] = 0;
    nm.status[0] = 0;
    if (!(f->seen & (1 << C_META))) return 0;
    if (open_chunk(&r, f, C_META)) return NM_E_BADOVL;
    while ((n = rd_line(&r, line)) >= 0) {
        meta_take(line, n, "title=", nm.title, NM_TITLE_MAX);
        meta_take(line, n, "status=", nm.status, NM_STATUS_MAX);
    }
    return 0;
}

/* Is the CONF line in line, of length n, equal to s? */
static uint8_t conf_is(const char *line, int16_t n, const char *s)
{
    int16_t l = (int16_t)strlen(s);

    return n == l && !memcmp(line, s, l);
}

/* CONF workline=N: SMS line N, 1 to 191, else 0 (off). */
static uint8_t conf_line(const char *line, int16_t n)
{
    uint16_t v = 0;
    int16_t i;

    if (n < 10 || memcmp(line, "workline=", 9)) return 0;
    for (i = 9; i < n; i++) {
        if (line[i] < '0' || line[i] > '9' || v > 191) return 0;
        v = v * 10 + (line[i] - '0');
    }
    return v < 192 ? (uint8_t)v : 0;
}

/* CONF switches: priority=1, toppal=1, tilecache=1, hsplit=1, collline=1,
 * rastseg=1, workline=N, and hz=50 or hz=60.
 * Unknown keys, and hz=any, are skipped.
 * Returns 0 or a failure code. */
static uint8_t read_conf(const struct nms *f)
{
    struct rd r;
    char line[LINE_MAX];
    int16_t n;
    uint8_t w;

    nm.launch.flags = 0;
    nm.launch.wline = 0;
    if (!(f->seen & (1 << C_CONF))) return 0;
    if (open_chunk(&r, f, C_CONF)) return NM_E_BADOVL;
    while ((n = rd_line(&r, line)) >= 0) {
        if (conf_is(line, n, "priority=1")) nm.launch.flags |= NM_FL_PRIORITY;
        if (conf_is(line, n, "toppal=1")) nm.launch.flags |= NM_FL_TOPPAL;
        if (conf_is(line, n, "tilecache=1")) nm.launch.flags |= NM_FL_TILECACHE;
        if (conf_is(line, n, "hsplit=1")) nm.launch.flags |= NM_FL_HSPLIT;
        if (conf_is(line, n, "collline=1")) nm.launch.flags |= NM_FL_COLLLINE;
        if (conf_is(line, n, "rastseg=1")) nm.launch.flags |= NM_FL_RASTSEG;
        if ((w = conf_line(line, n)) != 0) nm.launch.wline = w;
        if (conf_is(line, n, "hz=50")) nm.launch.flags |= NM_FL_HZ;
        if (conf_is(line, n, "hz=60")) nm.launch.flags |= NM_FL_HZ | NM_FL_HZ60;
    }
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

/* The cart's overlay file name in nm.ovl_name, from the index. Returns a
 * failure code. */
void *overlay_find(void *unused)
{
    (void)unused;
    return (void *)(uintptr_t)find_overlay();
}

/* f has passed the walk: CRCS, META, CONF, then PTCH, checked and applied.
 * Returns 0 or a failure code. */
void *overlay_apply(void *arg)
{
    const struct nms *f = (const struct nms *)arg;
    uint8_t code;

    code = accepts(f);
    if (!code) code = read_meta(f);
    if (!code) code = read_conf(f);
    if (!code) code = check_ops(f);
    if (!code) code = apply_ops(f);
    return (void *)(uintptr_t)code;
}
