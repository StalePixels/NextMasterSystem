/* rd.c: reading a run of a file through OVL_BUF, for the loader and the
 * overlay module. Resident, so both banked modules share one copy. See
 * nms.h. */
#include <string.h>

#include "nm.h"
#include "nms.h"

uint32_t rd24(const uint8_t *p)
{
    return (uint32_t)p[0] | ((uint32_t)p[1] << 8) | ((uint32_t)p[2] << 16);
}

uint16_t rd16(const uint8_t *p)
{
    return p[0] | (p[1] << 8);
}

uint32_t rd32(const uint8_t *p)
{
    return *(const uint32_t *)p;
}

/* Start a run of len bytes of the file from offset pos. Returns 0, or 1
 * when the seek fails. */
uint8_t rd_open(struct rd *r, uint8_t h, uint32_t pos, uint32_t len)
{
    r->h = h;
    r->at = 0;
    r->fill = 0;
    r->left = len;
    return nm_seek(h, pos) != 0;
}

/* The bytes of the run not handed out yet. */
uint32_t rd_left(const struct rd *r)
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
const uint8_t *rd_take(struct rd *r, uint16_t n)
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
const uint8_t *rd_piece(struct rd *r, uint16_t n, uint16_t *got)
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
uint8_t rd_skip(struct rd *r, uint16_t n)
{
    uint16_t k;

    while (n) {
        if (!rd_piece(r, n, &k)) return 1;
        n -= k;
    }
    return 0;
}

/* Copy the next len bytes of the run to dst. Returns 0, or 1 when the run
 * has fewer. */
uint8_t rd_copy(struct rd *r, uint8_t *dst, uint16_t len)
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
