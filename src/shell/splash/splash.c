/* splash.c: the start screen. Banked (PAGE_SPLASH).
 *
 * session_init shows it once, before the browser first opens. It is drawn
 * on Layer 2 like the information screen (l2screen.h): the white background
 * with its grey grid, then, one step a frame, a black band that grows out
 * from the middle, the name in it one character at a time, and a red line
 * under the band, drawn from the left. It lasts SPLASH_50 frames at 50 Hz,
 * SPLASH_60 at 60 Hz (NextReg $05 bit 2). Interrupts are off: a frame is
 * the video line passing line 192.
 *
 * The characters are the 48K ROM's at $3D00, at twice their size.
 */
#include <arch/zxn.h>
#include <stdint.h>
#include <z80.h>

#include "nm.h"
#include "../info/l2screen.h"

#define ROM_FONT    0x3D00u        /* character $20 */

#define SPLASH_50   150
#define SPLASH_60   180
#define SP_BAND_Y   76
#define SP_BAND_H   40
#define SP_TEXT_Y   88
#define SP_LINE_Y   116
#define SP_GROW     16                   /* the band: 8 pixels a side a frame */
#define SP_TEXT     (SP_GROW + 2 * 16)   /* a character every 2 frames */
#define SP_LINE     (SP_TEXT + 16)       /* the line: 16 pixels a frame */

static const char s_name[] = "NextMasterSystem";

/* Character c at (x, y) in colour c, each pixel 2x2; the other pixels are
 * left as they are. */
static void big_char(uint8_t x, uint8_t y, uint8_t ch, uint8_t c)
{
    const uint8_t *g = (const uint8_t *)(ROM_FONT + (uint16_t)(ch - 0x20) * 8);
    uint8_t *d;
    uint8_t i, j, s, bits;

    for (i = 0; i < 8; i++) {
        for (s = 0; s < 2; s++) {
            d = l2_row(y++) + x;
            bits = g[i];
            for (j = 0; j < 8; j++) {
                if (bits & 0x80) d[0] = d[1] = c;
                d += 2;
                bits <<= 1;
            }
        }
    }
}

/* What frame f adds to the picture. */
static void step(uint8_t f)
{
    uint8_t x;

    if (f < SP_GROW) {
        x = (uint8_t)(f * 8);
        fill(120 - x, SP_BAND_Y, 8, SP_BAND_H, C_BLACK);
        fill(128 + x, SP_BAND_Y, 8, SP_BAND_H, C_BLACK);
    } else if (f < SP_TEXT) {
        if (f & 1) return;
        x = (uint8_t)((f - SP_GROW) / 2);
        big_char(x * 16, SP_TEXT_Y, (uint8_t)s_name[x], x < 4 ? C_RED : C_WHITE);
    } else if (f < SP_LINE) {
        fill((uint8_t)((f - SP_TEXT) * 16), SP_LINE_Y, 16, 3, C_RED);
    }
}

/* ---- frames and keys ------------------------------------------------------ */

/* The video line now (NextRegs $1E and $1F, read again when $1E changed). */
static uint16_t video_line(void)
{
    uint8_t h, l;

    do {
        h = ZXN_READ_REG(0x1E);
        l = ZXN_READ_REG(0x1F);
    } while (h != ZXN_READ_REG(0x1E));
    return ((uint16_t)(h & 1) << 8) | l;
}

/* Until the next time the video line reaches 192, the first line under
 * the picture. */
static void wait_frame(void)
{
    while (video_line() >= 192)
        ;
    while (video_line() < 192)
        ;
}

/* 1 when port $1F reads bits 3, 4 and 5 set (and is not $FF), or port
 * $FBFE bit 0 and port $7FFE bits 0 and 2 all read 0. */
static uint8_t boot_keys(void)
{
    uint8_t k = z80_inp(0x001F);

    if (k != 0xFF && (k & 0x38) == 0x38) return 1;
    return !(z80_inp(0xFBFE) & 0x01) && !(z80_inp(0x7FFE) & 0x05);
}

/* 1 when any key or joystick input is down. Port $1F reads $FF when there
 * is no joystick port. */
static uint8_t any_key(void)
{
    uint8_t k = z80_inp(0x001F);

    if (k != 0xFF && k) return 1;
    return (z80_inp(0x00FE) & 0x1F) != 0x1F;
}

/* The keyboard's half rows: the high byte of the port, then the bits that
 * other_key reads. */
static const uint8_t other_rows[] = {
    0xFE, 0x1F, 0xFD, 0x1F, 0xFB, 0x1E, 0xF7, 0x1F,
    0xEF, 0x1F, 0xDF, 0x1F, 0xBF, 0x1F, 0x7F, 0x1A
};

/* 1 when a key or joystick input is down that boot_keys does not read. */
static uint8_t other_key(void)
{
    uint8_t i, m, k = z80_inp(0x001F);

    if (k != 0xFF && (k & 0xC7)) return 1;
    for (i = 0; i < sizeof other_rows; i += 2) {
        m = other_rows[i + 1];
        if ((z80_inp(((uint16_t)other_rows[i] << 8) | 0xFE) & m) != m) return 1;
    }
    return 0;
}

/* ---- the screen ----------------------------------------------------------- */

/* The keys are read once a frame. The screen ends at the end of its time,
 * or when other_key reads 1 in a frame after a frame in which any_key read
 * 0, so the keys held as nms.nex starts do not end it. After a key ends it,
 * the screen stays until any_key reads 0, for at most 100 frames. Returns 1,
 * at once, from the first frame in which boot_keys reads 1, else 0. Layer 2
 * and the NextRegs are put back as on the information screen. */
void *splash_show(void *unused)
{
    struct l2_keep keep;
    uint8_t f, n, armed = 0, boot = 0;

    (void)unused;
    n = (ZXN_READ_REG(0x05) & 4) ? SPLASH_60 : SPLASH_50;
    screen_on(&keep);
    grid();
    z80_outp(0x123B, 0x02);                         /* Layer 2 on */
    for (f = 0; f < n; f++) {
        step(f);
        if (boot_keys()) {
            boot = 1;
            break;
        }
        if (!any_key()) armed = 1;
        else if (armed && other_key()) break;
        wait_frame();
    }
    if (!boot)
        for (f = 0; f < 100 && any_key(); f++) wait_frame();
    screen_off(&keep);
    return (void *)(uintptr_t)boot;
}
