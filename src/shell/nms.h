/* nms.h: what the loader (loader/loader.c), the overlay module
 * (overlay/overlay.c) and the file reader (rd.c) share about an overlay
 * file. The format is docs/nms-format.md.
 */
#ifndef NMS_H
#define NMS_H

#include <stdint.h>

#define WINDOW      ((uint8_t *)0xC000)   /* MMU 6 */
#define PAGE_SIZE   0x2000u

/* The chunks read after the walk, in the order of chunk_tags in loader.c. */
#define C_CRCS      0
#define C_PTCH      1
#define C_CONF      2
#define C_META      3
#define C_N         4

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

/* ---- reading a file through OVL_BUF (rd.c, resident) ----------------------
 * A run of bytes of a file, read in order through OVL_BUF. The bytes from
 * OVL_BUF + at to OVL_BUF + fill are read but not handed out yet. left is
 * the number of bytes of the run still in the file. */
struct rd {
    uint8_t  h;
    uint16_t at;
    uint16_t fill;
    uint32_t left;
};

uint32_t rd24(const uint8_t *p);
uint16_t rd16(const uint8_t *p);
uint32_t rd32(const uint8_t *p);
/* Start a run of len bytes of the file from offset pos. Returns 0, or 1
 * when the seek fails. */
uint8_t rd_open(struct rd *r, uint8_t h, uint32_t pos, uint32_t len);
/* The bytes of the run not handed out yet. */
uint32_t rd_left(const struct rd *r);
/* The next n bytes of the run, n at most OVL_BUFSIZE, in one piece. Returns
 * 0 when the run has fewer. The pointer is good until the next call. */
const uint8_t *rd_take(struct rd *r, uint16_t n);
/* The next bytes of the run: at least 1 and at most n, the number in *got.
 * Returns 0 when the run is over. */
const uint8_t *rd_piece(struct rd *r, uint16_t n, uint16_t *got);
/* Skip n bytes of the run. Returns 0, or 1 when the run has fewer. */
uint8_t rd_skip(struct rd *r, uint16_t n);
/* Copy the next len bytes of the run to dst. Returns 0, or 1 when the run
 * has fewer. */
uint8_t rd_copy(struct rd *r, uint8_t *dst, uint16_t len);

/* ---- CRC32 checks that the overlay module far-calls in the loader --------- */
struct crc_range {        /* loader_check_range: 1 when the CRC32 of len */
    uint32_t off;         /* bytes of the cart from off equals crc */
    uint16_t len;
    uint32_t crc;
};
struct ramsite {          /* loader_ramsite_old: the original instruction of */
    const uint8_t *new;   /* a RAMSITES entry into out; 0 when none matches */
    uint16_t crc16;
    uint8_t *out;
};

#endif
