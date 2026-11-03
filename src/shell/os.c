/* os.c: esxDOS file calls over nm_esx, and a file held in RAM pages that
 * the same calls read (handle NM_MEM_H). Resident. */
#include <arch/zxn.h>
#include <string.h>

#include "nm.h"

#define F_OPEN   0x9A
#define F_CLOSE  0x9B
#define F_READ   0x9D
#define F_SEEK   0x9F
#define F_FSTAT  0xA1
#define F_GETCWD 0xA8
#define MODE_READ 1
#define SEEK_SET  0

/* The file in RAM pages: its first page, its size and the read position.
 * It is read through MMU 7 ($E000), which the calls put back, so the
 * destination may be anywhere below $E000. */
static uint8_t  mem_page;
static uint32_t mem_size;
static uint32_t mem_pos;

int16_t nm_mopen(uint8_t page, uint32_t size)
{
    mem_page = page;
    mem_size = size;
    mem_pos = 0;
    return NM_MEM_H;
}

static int16_t mem_read(uint8_t *dst, uint16_t n)
{
    uint8_t old = ZXN_READ_REG(REG_MMU0 + 7);
    uint16_t in, k, got;

    if ((uint32_t)n > mem_size - mem_pos) n = (uint16_t)(mem_size - mem_pos);
    got = n;
    while (n) {
        in = (uint16_t)mem_pos & 0x1FFF;
        k = 0x2000 - in;
        if (k > n) k = n;
        ZXN_WRITE_MMU7(mem_page + (uint8_t)(mem_pos >> 13));
        memcpy(dst, (const uint8_t *)0xE000 + in, k);
        dst += k;
        mem_pos += k;
        n -= k;
    }
    ZXN_WRITE_MMU7(old);
    return (int16_t)got;
}

int16_t nm_open(const char *path)
{
    struct nm_esx e;

    e.fn = F_OPEN;
    e.a = '*';
    e.bc = (uint16_t)MODE_READ << 8;
    e.ix = (uint16_t)path;
    e.de = 0;
    if (nm_esx(&e)) return -1;
    return e.a;
}

int8_t nm_fstat(uint8_t handle, uint8_t *stat16)
{
    struct nm_esx e;

    if (handle == NM_MEM_H) {
        memcpy(stat16 + 7, &mem_size, 4);
        return 0;
    }
    e.fn = F_FSTAT;
    e.a = handle;
    e.bc = 0;
    e.ix = (uint16_t)stat16;
    e.de = 0;
    return nm_esx(&e) ? -1 : 0;
}

int16_t nm_read(uint8_t handle, void *dst, uint16_t n)
{
    struct nm_esx e;

    if (handle == NM_MEM_H) return mem_read((uint8_t *)dst, n);
    e.fn = F_READ;
    e.a = handle;
    e.bc = n;
    e.ix = (uint16_t)dst;
    e.de = 0;
    if (nm_esx(&e)) return -1;
    return (int16_t)e.bc;
}

void nm_close(uint8_t handle)
{
    struct nm_esx e;

    if (handle == NM_MEM_H) return;
    e.fn = F_CLOSE;
    e.a = handle;
    e.bc = 0;
    e.ix = 0;
    e.de = 0;
    nm_esx(&e);
}

/* BCDE is the position, IX the seek mode. */
int8_t nm_seek(uint8_t handle, uint32_t pos)
{
    struct nm_esx e;

    if (handle == NM_MEM_H) {
        if (pos > mem_size) return -1;
        mem_pos = pos;
        return 0;
    }
    e.fn = F_SEEK;
    e.a = handle;
    e.bc = (uint16_t)(pos >> 16);
    e.de = (uint16_t)pos;
    e.ix = SEEK_SET;
    return nm_esx(&e) ? -1 : 0;
}

/* The current directory of the default drive, into dst (NM_CWD_MAX bytes). */
int8_t nm_getcwd(char *dst)
{
    struct nm_esx e;

    e.fn = F_GETCWD;
    e.a = '*';
    e.bc = 0;
    e.ix = (uint16_t)dst;
    e.de = 0;
    return nm_esx(&e) ? -1 : 0;
}
