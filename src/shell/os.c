/* os.c: esxDOS file calls over nm_esx. Resident. */
#include "nm.h"

#define F_OPEN   0x9A
#define F_CLOSE  0x9B
#define F_READ   0x9D
#define F_SEEK   0x9F
#define F_FSTAT  0xA1
#define MODE_READ 1
#define SEEK_SET  0

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

    e.fn = F_SEEK;
    e.a = handle;
    e.bc = (uint16_t)(pos >> 16);
    e.de = (uint16_t)pos;
    e.ix = SEEK_SET;
    return nm_esx(&e) ? -1 : 0;
}
