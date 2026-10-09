/* loader.c: load the picked cart, find and check its overlay, apply it and
 * start the game. Banked (PAGE_LOADER).
 *
 * The cart is read into RAM pages CART_PAGE and up, one 8K page at a time
 * through MMU 6 ($C000). This code runs from $E000, so MMU 7 is never
 * touched here. Overlay patches are applied to the cart pages in place.
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

/* overlay file header */
#define OV_FORMAT   4
#define OV_ABI      5
#define OV_HDRSIZE  6
#define OV_CRC      8
#define OV_FLAGS    17

#define WINDOW      ((uint8_t *)0xC000)   /* MMU 6 */
#define PAGE_SIZE   0x2000u

static const char hex_digits[] = "0123456789ABCDEF";

static void put_hex32(char *out, uint32_t v)
{
    uint8_t i;

    for (i = 0; i < 8; i++) {
        out[i] = hex_digits[(v >> 28) & 15];
        v <<= 4;
    }
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

/* Read /nm/ovl/<CRC32>.nmo into OVL_BUF. Returns 0 or a failure code. */
static uint8_t read_overlay(void)
{
    int16_t h;
    uint8_t code = 0;

    put_hex32(nm.ovl_name + 8, nm.launch.crc);
    h = nm_open(nm.ovl_name);
    if (h < 0) return NM_E_NOOVL;
    if (nm_read((uint8_t)h, OVL_BUF, OVL_MAX) < 0) code = NM_E_NOOVL;
    nm_close((uint8_t)h);
    return code;
}

/* Check the header, then run the operations. Returns 0 or a failure code. */
static uint8_t apply_overlay(void)
{
    const uint8_t *o = OVL_BUF;
    const uint8_t *op;
    const uint8_t *end = OVL_BUF + OVL_MAX;
    uint8_t *dst;
    uint16_t len, off;
    uint8_t pg;

    if (o[0] != 'N' || o[1] != 'M' || o[2] != 'O' || o[3] != 'V') return NM_E_BADOVL;
    if ((uint8_t)(o[OV_FORMAT] - 1) >= 3) return NM_E_BADOVL;   /* formats 1 to 3 */
    if (o[OV_ABI] > FW_ABI) return NM_E_BADOVL;                 /* needs a newer runtime */
    nm.launch.flags = o[OV_FLAGS];
    if (memcmp(o + OV_CRC, &nm.launch.crc, 8) != 0) return NM_E_OTHER;

    nm.launch.start = 0;
    nm.launch.sp = 0xDFF0;
    nm.launch.hook = 0;
    nm.launch.hook2 = 0;

    op = o + (o[OV_HDRSIZE] | (o[OV_HDRSIZE + 1] << 8));
    for (;;) {
        if (op + 5 > end) return NM_E_BADOP;
        switch (op[0]) {
        case 0:
            return 0;
        case 1:     /* PATCH: u24 offset, u8 length, original bytes, new bytes */
            len = op[4];
            pg = (uint8_t)((op[3] << 3) | (op[2] >> 5));
            if (pg >= nm.launch.npages) return NM_E_BADOP;
            off = ((op[2] & 0x1F) << 8) | op[1];
            if (off + len > PAGE_SIZE || op + 5 + 2 * len > end) return NM_E_BADOP;
            ZXN_WRITE_MMU6(CART_PAGE + pg);
            dst = WINDOW + off;
            if (memcmp(dst, op + 5, len) != 0) return NM_E_DIFFER;
            memcpy(dst, op + 5 + len, len);
            op += 5 + 2 * len;
            break;
        case 2:     /* START: u16 address, u16 stack (0 is $DFF0) */
            nm.launch.start = op[1] | (op[2] << 8);
            nm.launch.sp = op[3] | (op[4] << 8);
            if (nm.launch.sp == 0) nm.launch.sp = 0xDFF0;
            op += 5;
            break;
        case 3:     /* CODE: u16 address in the runtime's second page, u16 length, bytes */
            len = op[3] | (op[4] << 8);
            off = (op[1] | (op[2] << 8)) & 0x1FFF;
            if (off + len > PAGE_SIZE || op + 5 + len > end) return NM_E_BADOP;
            ZXN_WRITE_MMU6(FW2_PAGE);
            memcpy(WINDOW + off, op + 5, len);
            op += 5 + len;
            break;
        case 4:     /* HOOK: u8 kind (1 per-line scroll table, 2 RAM patch table), u16 address */
            if (op[1] == 2) nm.launch.hook2 = op[2] | (op[3] << 8);
            else nm.launch.hook = op[2] | (op[3] << 8);
            op += 4;
            break;
        default:
            return NM_E_BADOP;
        }
    }
}

void *loader_load(void *unused)
{
    uint8_t code;

    (void)unused;
    code = read_cart();
    if (!code) code = read_overlay();
    if (!code) code = apply_overlay();
    ZXN_WRITE_MMU6(0);
    if (code) return (void *)(uintptr_t)code;
    NM_FAR(PAGE_INFO, info_show, 0);
    nm_launch(&nm.launch);
    return 0;
}
