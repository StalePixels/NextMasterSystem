/* info.c: the cart information screen. Banked (PAGE_INFO).
 *
 * Shown after the loader has read the cart and checked its overlay, and
 * before the game starts. It clears the standard ULA screen, prints what
 * the player picked and what the overlay file says about it, and waits for a
 * key or a joystick fire button.
 *
 * Text is drawn straight into the ULA screen ($4000 pixels, $5800
 * attributes), 32 columns by 24 rows, using the character shapes in the
 * 48K ROM at $3D00 (character $20 first, 8 bytes each). The ROM is always
 * mapped at $0000 while the shell runs. This module keeps no data of its
 * own: everything is on the stack.
 */
#include <arch/zxn.h>
#include <string.h>
#include <z80.h>

#include "nm.h"

#define COLS        32
#define ROWS        24
#define VALUE_COL   8
#define VALUE_WIDTH (COLS - VALUE_COL)

#define ULA_PIXELS  ((uint8_t *)0x4000)
#define ULA_ATTRS   ((uint8_t *)0x5800)
#define ROM_FONT    0x3D00u        /* character $20 */
#define ATTR_TEXT   0x07           /* white on black */

#define PORT_KEYS   0x00FE         /* all keyboard rows at once */
#define PORT_KEMP   0x001F         /* Kempston joystick 1 */
#define KEMP_FIRE   0x10

static const char hex_digits[] = "0123456789ABCDEF";

static const char s_title[]   = "NextMasterSystem: cart info";
static const char s_file[]    = "File";
static const char s_crc[]     = "CRC32";
static const char s_size[]    = "Size";
static const char s_game[]    = "Game";
static const char s_format[]  = "Format";
static const char s_abi[]     = "ABI";
static const char s_flags[]   = "Flags";
static const char s_status[]  = "Status";
static const char s_rate[]    = "Rate";
static const char s_untested[] = "untested";
static const char s_hz50[]    = "50 Hz";
static const char s_hz60[]    = "60 Hz";
static const char s_boot[]    = "boot rate (";
static const char s_close[]   = ")";
static const char s_kb[]      = " KB";
static const char s_none[]    = "none";
static const char s_prio[]    = "priority tiles";
static const char s_top[]     = "line-0 palette";
static const char s_tc[]      = "tile cache";
static const char s_hs[]      = "scroll split";
static const char s_sep[]     = ", ";
static const char s_prompt[]  = "Press any key or fire to start.";

static void put_char(uint8_t col, uint8_t row, uint8_t c)
{
    const uint8_t *g;
    uint8_t *d;
    uint8_t i;

    if (c < 0x20 || c > 0x7E) c = '?';
    g = (const uint8_t *)(ROM_FONT + (uint16_t)(c - 0x20) * 8);
    d = ULA_PIXELS + ((uint16_t)(row & 0x18) << 8) + ((uint16_t)(row & 7) << 5) + col;
    for (i = 0; i < 8; i++) {
        *d = g[i];
        d += 256;
    }
}

static void put_text(uint8_t col, uint8_t row, const char *s, uint8_t n)
{
    while (n-- && col < COLS) put_char(col++, row, (uint8_t)*s++);
}

/* The text at VALUE_COL, broken at spaces to fit the screen. Returns the
 * next free row. */
static uint8_t put_value(uint8_t row, const char *s)
{
    uint8_t len = (uint8_t)strlen(s);
    uint8_t n, i;

    for (;;) {
        if (row >= ROWS) return row;
        n = len;
        if (n > VALUE_WIDTH) {
            n = VALUE_WIDTH;
            for (i = VALUE_WIDTH; i > 0; i--)
                if (s[i] == ' ') { n = i; break; }
        }
        put_text(VALUE_COL, row++, s, n);
        s += n;
        len -= n;
        while (len && *s == ' ') { s++; len--; }
        if (!len) return row;
    }
}

/* A label at column 0 and its value beside it. Returns the next free row. */
static uint8_t put_field(uint8_t row, const char *label, const char *value)
{
    put_text(0, row, label, (uint8_t)strlen(label));
    return put_value(row, value);
}

/* Append the decimal digits of v to p and return the new end. */
static char *put_dec(char *p, uint16_t v)
{
    char t[5];
    uint8_t n = 0;

    do {
        t[n++] = (char)('0' + v % 10);
        v /= 10;
    } while (v);
    while (n) *p++ = t[--n];
    return p;
}

static char *put_str(char *p, const char *s)
{
    while (*s) *p++ = *s++;
    return p;
}

/* Nothing but the ULA screen shows: every hardware sprite hidden and the
 * sprite layer, Layer 2, the tilemap and the copper off. A game that ended
 * with BREAK leaves its sprites in the attribute table, and NextZXOS's own
 * NextReg $15, which the runtime puts back, may show the sprite layer. The
 * runtime sets every layer again when the game starts. */
static void layers_off(void)
{
    uint8_t i;

    ZXN_NEXTREGA(0x15, ZXN_READ_REG(0x15) & 0xFE);  /* sprites off */
    ZXN_NEXTREGA(0x6B, ZXN_READ_REG(0x6B) & 0x7F);  /* tilemap off */
    ZXN_NEXTREG(0x62, 0);                           /* copper stopped */
    z80_outp(0x123B, 0);                            /* Layer 2 off */
    z80_outp(0x303B, 0);                            /* sprite attribute slot 0 */
    for (i = 0; i < 128; i++) {
        z80_outp(0x57, 0);                          /* 4-byte attributes, */
        z80_outp(0x57, 0);                          /* the visible bit clear */
        z80_outp(0x57, 0);
        z80_outp(0x57, 0);
    }
}

static void wait_key(void)
{
    uint16_t n;

    /* let go of the key that picked the cart (ENTER in the browser) */
    for (n = 0; n < 30000u; n++)
        if ((z80_inp(PORT_KEYS) & 0x1F) == 0x1F && !(z80_inp(PORT_KEMP) & KEMP_FIRE))
            break;
    for (;;)
        if ((z80_inp(PORT_KEYS) & 0x1F) != 0x1F || (z80_inp(PORT_KEMP) & KEMP_FIRE))
            return;
}

void *info_show(void *unused)
{
    char buf[64];        /* the longest value is the list of every switch */
    char *p, *q;
    const char *name;
    uint32_t size;
    uint8_t row, fl, i;

    (void)unused;

    /* a plain ULA screen, whatever mode the browser or the last game left */
    layers_off();
    z80_outp(0xFF, 0);
    memset(ULA_PIXELS, 0, 0x1800);
    memset(ULA_ATTRS, ATTR_TEXT, 0x300);

    row = 0;
    put_text(0, row, s_title, (uint8_t)strlen(s_title));
    row += 2;

    /* the cart: the long name if the browser gave one */
    name = nm_lname[0] ? nm_lname : nm_name;
    row = put_field(row, s_file, name);

    p = buf;
    for (i = 0; i < 8; i++)
        *p++ = hex_digits[(nm.launch.crc >> (28 - 4 * i)) & 15];
    *p = 0;
    row = put_field(row, s_crc, buf);

    size = nm.launch.size;
    p = put_dec(buf, (uint16_t)((size + 1023) >> 10));
    p = put_str(p, s_kb);
    *p = 0;
    row = put_field(row, s_size, buf);
    row++;

    /* the overlay file: its META title and status and its CONF rate, as
       the loader read them, and its header */
    row = put_field(row, s_game, nm.title);
    row = put_field(row, s_status, nm.status[0] ? (const char *)nm.status : s_untested);

    /* NextReg $05 bit 2 is the rate the Next shows now: the boot rate,
       which the browser and this screen keep */
    fl = nm.launch.flags;
    q = buf;
    if (!(fl & NM_FL_HZ)) q = put_str(q, s_boot);
    q = put_str(q, ((fl & NM_FL_HZ) ? (fl & NM_FL_HZ60) : (ZXN_READ_REG(0x05) & 4)) ? s_hz60 : s_hz50);
    if (!(fl & NM_FL_HZ)) q = put_str(q, s_close);
    *q = 0;
    row = put_field(row, s_rate, buf);

    p = put_dec(buf, nm.nms_ver[0]);
    *p++ = '.';
    p = put_dec(p, nm.nms_ver[1]);
    *p = 0;
    row = put_field(row, s_format, buf);

    p = put_dec(buf, nm.nms_ver[2]);
    *p = 0;
    row = put_field(row, s_abi, buf);

    /* the CONF switches, as the loader read them */
    q = buf;
    if (fl & NM_FL_PRIORITY) q = put_str(q, s_prio);
    if (fl & NM_FL_TOPPAL) {
        if (q != buf) q = put_str(q, s_sep);
        q = put_str(q, s_top);
    }
    if (fl & NM_FL_TILECACHE) {
        if (q != buf) q = put_str(q, s_sep);
        q = put_str(q, s_tc);
    }
    if (fl & NM_FL_HSPLIT) {
        if (q != buf) q = put_str(q, s_sep);
        q = put_str(q, s_hs);
    }
    if (q == buf) q = put_str(q, s_none);
    *q = 0;
    put_field(row, s_flags, buf);

    put_text(0, ROWS - 1, s_prompt, (uint8_t)strlen(s_prompt));

    wait_key();
    return 0;
}
