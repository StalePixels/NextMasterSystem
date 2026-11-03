/* l2screen.h: the Layer 2 screen of the information screen (info.c) and the
 * start screen (splash.c). The functions are static: each module that
 * includes this file has its own copy in its own page.
 *
 * Layer 2 is 256x192 in RAM pages L2_PAGE to L2_PAGE + 5, drawn one 8K page
 * (32 lines) at a time through MMU 6.
 */
#ifndef L2SCREEN_H
#define L2SCREEN_H

#include <arch/zxn.h>
#include <string.h>
#include <z80.h>

#include "nm.h"
#include "nms.h"      /* WINDOW */

#define ULA_PIXELS  ((uint8_t *)0x4000)
#define ULA_ATTRS   ((uint8_t *)0x5800)

/* Layer 2 colours: the Next's default palette, RRRGGGBB. $E3 is the
 * transparent colour, so NO_BG means "leave the pixel as it is". */
#define C_WHITE     0xFF
#define C_BLACK     0x00
#define C_GRID      0xB6
#define C_RED       0xE0
#define C_GREEN     0x14
#define C_ORANGE    0xEC
#define C_DRED      0xC0
#define C_GREY      0x92
#define NO_BG       0xE3

/* Line y of Layer 2, with its page mapped at $C000. */
static uint8_t *l2_row(uint8_t y)
{
    ZXN_WRITE_MMU6(L2_PAGE + (y >> 5));
    return WINDOW + ((uint16_t)(y & 31) << 8);
}

static void fill(uint8_t x, uint8_t y, uint16_t w, uint8_t h, uint8_t c)
{
    while (h--) memset(l2_row(y++) + x, c, w);
}

/* The white background with its grey grid. */
static void grid(void)
{
    uint8_t *d;
    uint8_t i, y = 0;

    do {
        d = l2_row(y);
        if (y & 15) {
            memset(d, C_WHITE, 256);
            for (i = 0; i < 16; i++) d[i << 4] = C_GRID;
            d[255] = C_GRID;
        } else {
            memset(d, C_GRID, 256);
        }
    } while (++y < 192);
}

/* The NextRegs this screen changes, saved when it opens and put back when
 * the screen closes. */
struct l2_keep {
    uint8_t r12, r15, r16, r17, r43, r70, r71;
};

/* Nothing but Layer 2 shows: every hardware sprite hidden and the sprite
 * layer, the tilemap and the copper off, the ULA screen black. A game that
 * ended with BREAK leaves its sprites in the attribute table, and NextZXOS's
 * own NextReg $15, which the runtime puts back, may show the sprite layer.
 * Layer 2 is 256x192 in L2_PAGE, with no scroll, the whole clip window,
 * the first palette set to the default colours (the runtime's priority
 * tiles write it) and the layer order sprites, Layer 2, ULA. */
static void screen_on(struct l2_keep *k)
{
    uint16_t i;

    k->r12 = ZXN_READ_REG(0x12);
    k->r15 = ZXN_READ_REG(0x15);
    k->r16 = ZXN_READ_REG(0x16);
    k->r17 = ZXN_READ_REG(0x17);
    k->r43 = ZXN_READ_REG(0x43);
    k->r70 = ZXN_READ_REG(0x70);
    k->r71 = ZXN_READ_REG(0x71);

    ZXN_NEXTREGA(0x15, k->r15 & 0xE2);              /* sprites off, order SLU */
    ZXN_NEXTREGA(0x6B, ZXN_READ_REG(0x6B) & 0x7F);  /* tilemap off */
    ZXN_NEXTREG(0x62, 0);                           /* copper stopped */
    z80_outp(0x123B, 0);                            /* Layer 2 hidden */
    z80_outp(0x303B, 0);                            /* sprite attribute slot 0 */
    for (i = 0; i < 128; i++) {
        z80_outp(0x57, 0);                          /* 4-byte attributes, */
        z80_outp(0x57, 0);                          /* the visible bit clear */
        z80_outp(0x57, 0);
        z80_outp(0x57, 0);
    }
    z80_outp(0xFF, 0);                              /* no Timex mode */
    memset(ULA_PIXELS, 0, 0x1800);
    memset(ULA_ATTRS, 0, 0x300);

    ZXN_NEXTREGA(0x12, L2_BANK);
    ZXN_NEXTREG(0x70, 0);                           /* 256x192, palette offset 0 */
    ZXN_NEXTREG(0x16, 0);
    ZXN_NEXTREG(0x17, 0);
    ZXN_NEXTREG(0x71, 0);
    ZXN_NEXTREG(0x1C, 1);                           /* the Layer 2 clip window */
    ZXN_NEXTREG(0x18, 0);
    ZXN_NEXTREG(0x18, 255);
    ZXN_NEXTREG(0x18, 0);
    ZXN_NEXTREG(0x18, 191);
    ZXN_NEXTREG(0x43, 0x10);                        /* write Layer 2's first palette */
    ZXN_NEXTREG(0x40, 0);
    for (i = 0; i < 256; i++) ZXN_NEXTREGA(0x41, (uint8_t)i);
}

static void screen_off(const struct l2_keep *k)
{
    z80_outp(0x123B, 0);                            /* Layer 2 off */
    ZXN_NEXTREGA(0x12, k->r12);
    ZXN_NEXTREGA(0x15, k->r15 & 0xFE);              /* the order; sprites stay off */
    ZXN_NEXTREGA(0x16, k->r16);
    ZXN_NEXTREGA(0x17, k->r17);
    ZXN_NEXTREGA(0x43, k->r43);
    ZXN_NEXTREGA(0x70, k->r70);
    ZXN_NEXTREGA(0x71, k->r71);
    ZXN_WRITE_MMU6(0);
}

#endif
