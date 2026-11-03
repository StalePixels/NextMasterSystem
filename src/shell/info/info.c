/* info.c: the cart information screen. Banked (PAGE_INFO).
 *
 * Shown after the loader has read the cart and applied its overlay, and
 * before the game starts. It is drawn on Layer 2 at 256x192, in RAM pages
 * L2_PAGE to L2_PAGE + 5, one 8K page (32 lines) at a time through MMU 6:
 * a white background with a grey grid, a black title band with a red line
 * under it, and white panels with black frames. It has three pages:
 *
 *   - the main page: the overlay's icon (the ICON chunk, or a drawn NMS
 *     icon), the game's title and status, and a menu: start the game, the
 *     Pokes page (when the overlay has pokes), the details page. Any key
 *     that is not a menu key starts the game;
 *   - the details page: the file, its CRC32 and size, and what the overlay
 *     file says (title, status, rate, format, ABI, switches);
 *   - the Pokes page: each poke with its on or off mark, then "Start game"
 *     and "Back".
 *
 * Every poke is off when the screen opens. info_show returns when the
 * player starts the game, with nm.pokes_on holding the pokes turned on.
 * Before it returns it turns Layer 2 off and puts back the NextRegs it
 * changed.
 *
 * Text uses the character shapes in the 48K ROM at $3D00 (character $20
 * first, 8 bytes each), which is mapped at $0000 while the shell runs. The
 * icon and the poke names are in INFO_PAGE, where overlay_apply copied
 * them. This module keeps no data of its own: everything is on the stack.
 */
#include <arch/zxn.h>
#include <string.h>
#include <z80.h>

#include "nm.h"
#include "nms.h"

#define ULA_PIXELS  ((uint8_t *)0x4000)
#define ULA_ATTRS   ((uint8_t *)0x5800)
#define ROM_FONT    0x3D00u        /* character $20 */

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

/* Inputs */
#define IN_UP       0x01
#define IN_DOWN     0x02
#define IN_FIRE     0x04
#define IN_DETAILS  0x08
#define IN_HELD     0x40      /* the press is a key still held: a repeat */
#define IN_ANY      0x80

/* The main page's menu */
#define M_START     0
#define M_POKES     1
#define M_DETAILS   2
#define MENU_Y      118
#define MENU_DY     14

/* The Pokes page's rows */
#define PK_Y        32
#define PK_DY       8

static const char hex_digits[] = "0123456789ABCDEF";

static const char s_nms[]     = "NextMasterSystem";
static const char s_details[] = "Details";
static const char s_pokes[]   = "Pokes";
static const char s_start[]   = "Start game";
static const char s_back[]    = "Back";
static const char s_on[]      = " on";
static const char s_main_keys[] = "UP/DOWN  ENTER/FIRE  D: DETAILS";
static const char s_pk_keys[] = "ENTER/FIRE: ON/OFF OR CHOOSE";
static const char s_any_key[] = "ANY KEY OR FIRE: BACK";
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
static const char s_working[] = "working";
static const char s_imperfect[] = "imperfect";
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
static const char s_cl[]      = "collision line";
static const char s_rs[]      = "scroll segments";
static const char s_wl[]      = "work line ";
static const char s_nd[]      = "name table diff";
static const char s_pc[]      = "priority tile changes";
static const char s_sep[]     = ", ";

/* ---- Layer 2 drawing ------------------------------------------------------ */

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

static void frame(uint8_t x, uint8_t y, uint16_t w, uint8_t h, uint8_t c)
{
    fill(x, y, w, 1, c);
    fill(x, y + h - 1, w, 1, c);
    fill(x, y, 1, h, c);
    fill(x + w - 1, y, 1, h, c);
}

/* l2draw.asm: one 8x8 character on Layer 2 */
struct l2g {
    uint8_t y, x;
    const uint8_t *glyph;
    uint8_t fg, bg;
};
void l2_glyph(struct l2g *p) __z88dk_fastcall;

/* Character c at (x, y), its pixels in fg and the others in bg (NO_BG:
 * left as they are). With big, each pixel is 2x2. */
static void put_char(uint8_t x, uint8_t y, uint8_t c, uint8_t fg, uint8_t bg, uint8_t big)
{
    struct l2g a;
    const uint8_t *g;
    uint8_t *d;
    uint8_t i, j, bits, s, v;

    if (c < 0x20 || c > 0x7E) c = '?';
    g = (const uint8_t *)(ROM_FONT + (uint16_t)(c - 0x20) * 8);
    if (!big) {
        a.y = y;
        a.x = x;
        a.glyph = g;
        a.fg = fg;
        a.bg = bg;
        l2_glyph(&a);
        return;
    }
    for (i = 0; i < 8; i++) {
        for (s = 0; s <= big; s++) {
            d = l2_row(y++) + x;
            bits = g[i];
            for (j = 0; j < 8; j++) {
                v = (bits & 0x80) ? fg : bg;
                if (v != NO_BG) {
                    *d = v;
                    if (big) d[1] = v;
                }
                d += 1 + big;
                bits <<= 1;
            }
        }
    }
}

/* n characters of s from (x, y); returns the x after them. */
static uint8_t put_text(uint8_t x, uint8_t y, const char *s, uint8_t n, uint8_t fg, uint8_t bg)
{
    while (n-- && *s && x <= 248) {
        put_char(x, y, (uint8_t)*s++, fg, bg, 0);
        x += 8;
    }
    return x;
}

static uint8_t put_str0(uint8_t x, uint8_t y, const char *s, uint8_t fg, uint8_t bg)
{
    return put_text(x, y, s, 255, fg, bg);
}

/* s from (x, y), cols characters to a line, broken at spaces, on lines dy
 * apart up to line ymax. Returns the y of the next line. */
static uint8_t put_wrap(uint8_t x, uint8_t y, const char *s, uint8_t cols, uint8_t dy,
                        uint8_t ymax, uint8_t fg)
{
    uint8_t len = (uint8_t)strlen(s);
    uint8_t n, i;

    for (;;) {
        if (y > ymax) return y;
        n = len;
        if (n > cols) {
            n = cols;
            for (i = cols; i > 0; i--)
                if (s[i] == ' ') { n = i; break; }
        }
        put_text(x, y, s, n, fg, NO_BG);
        y += dy;
        s += n;
        len -= n;
        while (len && *s == ' ') { s++; len--; }
        if (!len) return y;
    }
}

/* The background, the title band with its text, and the key line. */
static void page(const char *title, const char *keys)
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
    fill(0, 0, 256, 20, C_BLACK);
    fill(0, 20, 256, 3, C_RED);
    put_str0((uint8_t)(128 - 4 * strlen(title)), 6, title, C_WHITE, NO_BG);
    fill(0, 180, 256, 12, C_BLACK);
    put_str0((uint8_t)(128 - 4 * strlen(keys)), 182, keys, C_WHITE, NO_BG);
}

static void panel(uint8_t x, uint8_t y, uint16_t w, uint8_t h)
{
    fill(x, y, w, h, C_WHITE);
    frame(x, y, w, h, C_BLACK);
}

/* The icon, 64x64 at (x, y): the ICON chunk at 2x2 pixels a pixel, or
 * without one the NMS icon drawn here. */
static void put_icon(uint8_t x, uint8_t y)
{
    uint8_t row[32];
    uint8_t *d;
    uint8_t i, j, s, v;

    if (!nm.icon) {
        fill(x, y, 64, 64, C_BLACK);
        fill(x, y + 26, 64, 12, C_RED);
        put_char(x + 8, y + 24, 'N', C_WHITE, NO_BG, 1);
        put_char(x + 24, y + 24, 'M', C_WHITE, NO_BG, 1);
        put_char(x + 40, y + 24, 'S', C_WHITE, NO_BG, 1);
        frame(x + 4, y + 4, 56, 56, C_GREY);
        return;
    }
    for (i = 0; i < 32; i++) {
        ZXN_WRITE_MMU6(INFO_PAGE);
        memcpy(row, WINDOW + INFO_ICON + (uint16_t)i * 32, 32);
        for (s = 0; s < 2; s++) {
            d = l2_row(y++) + x;
            for (j = 0; j < 32; j++) {
                v = row[j];
                if (v == NO_BG) v = C_WHITE;    /* transparent: the panel */
                *d++ = v;
                *d++ = v;
            }
        }
    }
}

/* ---- the pokes ------------------------------------------------------------ */

/* The name of poke i into name, with its end byte. Returns 1 when a code
 * of the poke takes the player's byte (PK_VALUE). */
static uint8_t poke_name(uint8_t i, char *name)
{
    const uint8_t *p;
    uint8_t n, ask = 0;

    ZXN_WRITE_MMU6(INFO_PAGE);
    p = WINDOW + INFO_POKE + 1;
    while (i--) {
        p += 1 + *p;                 /* the name */
        p += 1 + *p * PK_CODE;       /* the codes */
    }
    n = *p++;
    memcpy(name, p, n);
    name[n] = 0;
    p += n;
    n = *p++;
    while (n--) {
        ask |= *p & PK_VALUE;
        p += PK_CODE;
    }
    return ask != 0;
}

static uint8_t pokes_on(void)
{
    uint16_t m = nm.pokes_on;
    uint8_t n = 0;

    while (m) {
        n += (uint8_t)(m & 1);
        m >>= 1;
    }
    return n;
}

/* ---- input ---------------------------------------------------------------- */

/* The keys and the joystick now: cursor keys (6 and 7) or Q and A, ENTER or
 * SPACE, D, and the Kempston joystick's directions and fire buttons. */
static uint8_t input(void)
{
    uint8_t m = 0, k;

    k = z80_inp(0x001F);
    if (k != 0xFF) {                 /* no joystick port: the bus floats */
        if (k & 0x08) m |= IN_UP;
        if (k & 0x04) m |= IN_DOWN;
        if (k & 0x30) m |= IN_FIRE;
    }
    k = z80_inp(0xEFFE);             /* 0 9 8 7 6 */
    if (!(k & 0x08)) m |= IN_UP;
    if (!(k & 0x10)) m |= IN_DOWN;
    if (!(z80_inp(0xFBFE) & 0x01)) m |= IN_UP;        /* Q */
    k = z80_inp(0xFDFE);             /* A S D F G */
    if (!(k & 0x01)) m |= IN_DOWN;
    if (!(k & 0x04)) m |= IN_DETAILS;
    if (!(z80_inp(0xBFFE) & 0x01)) m |= IN_FIRE;      /* ENTER */
    if (!(z80_inp(0x7FFE) & 0x01)) m |= IN_FIRE;      /* SPACE */
    if (m || (z80_inp(0x00FE) & 0x1F) != 0x1F) m |= IN_ANY;
    return m;
}

/* The next press. It first waits, for at most hold polls, until nothing
 * is held, so a key held down repeats and the key that picked the cart in
 * the browser does not count. A press that comes from a key still held has
 * IN_HELD set. Interrupts are off: a polling loop. */
#define HOLD_FIRST  30000u
#define HOLD_REPEAT 1500u

static uint8_t wait_input_for(uint16_t hold)
{
    uint16_t n;
    uint8_t m;

    for (n = 0; n < hold; n++)
        if (!input()) break;
    if (n == hold) return input() | IN_HELD;
    for (n = 0; n < 3000u; n++)      /* key bounce */
        input();
    for (;;) {
        /* read again a little after the first sign of a press: a key that
           goes down during one input() shows in some of its reads only */
        while (!input())
            ;
        for (n = 0; n < 300u; n++)
            input();
        if ((m = input()) != 0) return m;
    }
}

static uint8_t wait_input(void)
{
    return wait_input_for(HOLD_FIRST);
}

/* ---- the details page ----------------------------------------------------- */

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

#define DT_X     8
#define DT_VX    64
#define DT_COLS  23
#define DT_YMAX  168

/* A label and its value. Returns the y of the next line. */
static uint8_t field(uint8_t y, const char *label, const char *value)
{
    if (y > DT_YMAX) return y;
    put_str0(DT_X, y, label, C_GREY, NO_BG);
    return put_wrap(DT_VX, y, value, DT_COLS, 8, DT_YMAX, C_BLACK);
}

static void details(void)
{
    char buf[164];       /* the longest value is the list of every switch */
    char *p, *q;
    uint32_t size;
    uint8_t y, fl, i;

    page(s_details, s_any_key);
    panel(4, 28, 248, 148);
    y = 32;

    /* the cart: the long name if the browser gave one */
    y = field(y, s_file, nm_lname[0] ? nm_lname : nm_name);

    p = buf;
    for (i = 0; i < 8; i++)
        *p++ = hex_digits[(nm.launch.crc >> (28 - 4 * i)) & 15];
    *p = 0;
    y = field(y, s_crc, buf);

    size = nm.launch.size;
    p = put_dec(buf, (uint16_t)((size + 1023) >> 10));
    p = put_str(p, s_kb);
    *p = 0;
    y = field(y, s_size, buf);
    y += 4;

    /* the overlay file: its META title and status and its CONF rate, as
       the loader read them, and its header */
    y = field(y, s_game, nm.title);
    y = field(y, s_status, nm.status[0] ? (const char *)nm.status : s_untested);

    /* NextReg $05 bit 2 is the rate the Next shows now: the boot rate,
       which the browser and this screen keep */
    fl = nm.launch.flags;
    q = buf;
    if (!(fl & NM_FL_HZ)) q = put_str(q, s_boot);
    q = put_str(q, ((fl & NM_FL_HZ) ? (fl & NM_FL_HZ60) : (ZXN_READ_REG(0x05) & 4)) ? s_hz60 : s_hz50);
    if (!(fl & NM_FL_HZ)) q = put_str(q, s_close);
    *q = 0;
    y = field(y, s_rate, buf);

    p = put_dec(buf, nm.nms_ver[0]);
    *p++ = '.';
    p = put_dec(p, nm.nms_ver[1]);
    *p = 0;
    y = field(y, s_format, buf);

    p = put_dec(buf, nm.nms_ver[2]);
    *p = 0;
    y = field(y, s_abi, buf);

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
    if (fl & NM_FL_COLLLINE) {
        if (q != buf) q = put_str(q, s_sep);
        q = put_str(q, s_cl);
    }
    if (fl & NM_FL_RASTSEG) {
        if (q != buf) q = put_str(q, s_sep);
        q = put_str(q, s_rs);
    }
    if (nm.launch.flags2 & NM_FL2_NTDIFF) {
        if (q != buf) q = put_str(q, s_sep);
        q = put_str(q, s_nd);
    }
    if (nm.launch.flags2 & NM_FL2_PRICHG) {
        if (q != buf) q = put_str(q, s_sep);
        q = put_str(q, s_pc);
    }
    if (nm.launch.wline) {
        if (q != buf) q = put_str(q, s_sep);
        q = put_str(q, s_wl);
        q = put_dec(q, nm.launch.wline);
    }
    if (q == buf) q = put_str(q, s_none);
    *q = 0;
    field(y, s_flags, buf);

    wait_input();
}

/* ---- the Pokes page ------------------------------------------------------- */

/* Row r of the Pokes page: poke r with its mark, then "Start game", then
 * "Back". The chosen row is white on black. A poke that takes the player's
 * byte shows it on the right in hex and decimal, white on green while up
 * and down change it (edit). */
static void poke_row(uint8_t r, uint8_t sel, uint8_t edit)
{
    char name[NM_POKE_NAME + 1];
    char num[10];
    char *p;
    uint8_t y = PK_Y + r * PK_DY;
    uint8_t fg = sel ? C_WHITE : C_BLACK;
    uint8_t bg = sel ? C_BLACK : C_WHITE;
    uint8_t v;

    fill(10, y, 236, PK_DY, bg);
    if (r < nm.npokes) {
        frame(14, y + 1, 6, 6, fg);
        if (nm.pokes_on & (1u << r)) fill(15, y + 2, 4, 4, sel ? C_WHITE : C_GREEN);
        if (poke_name(r, name)) {
            v = nm.poke_val[r];
            num[0] = hex_digits[v >> 4];
            num[1] = hex_digits[v & 15];
            p = put_str(num + 2, " / ");
            *put_dec(p, v) = 0;
            if (edit) fill(170, y, 74, PK_DY, C_GREEN);
            put_str0(172, y, num, edit ? C_WHITE : fg, NO_BG);
            name[18] = 0;            /* the name stops before the byte */
        }
        put_str0(26, y, name, fg, NO_BG);
    } else {
        put_str0(26, y, r == nm.npokes ? s_start : s_back, fg, NO_BG);
    }
}

/* Returns 1 when the player chose "Start game". ENTER or fire on a poke
 * turns it on or off. On a poke that takes the player's byte it goes from
 * off to on with the byte in edit, where up and down change it (held, they
 * repeat fast), then to on, then to off. */
static uint8_t pokes(void)
{
    char name[NM_POKE_NAME + 1];
    uint8_t rows = nm.npokes + 2;
    uint8_t sel = 0, edit = 0, r, m = 0;
    uint16_t bit;

    page(s_pokes, s_pk_keys);
    panel(8, 30, 240, PK_Y - 30 + rows * PK_DY + 2);
    for (r = 0; r < rows; r++) poke_row(r, r == sel, 0);
    for (;;) {
        m = wait_input_for(edit && (m & IN_HELD) ? HOLD_REPEAT : HOLD_FIRST);
        r = sel;
        bit = 1u << sel;
        if (edit) {
            if (m & IN_FIRE) edit = 0;
            else if (m & IN_UP) nm.poke_val[sel]++;
            else if (m & IN_DOWN) nm.poke_val[sel]--;
        } else if (m & IN_FIRE) {
            if (sel == nm.npokes) return 1;
            if (sel > nm.npokes) return 0;
            if (!(nm.pokes_on & bit) && poke_name(sel, name)) edit = 1;
            nm.pokes_on ^= bit;
        } else if (m & IN_UP) {
            sel = sel ? sel - 1 : rows - 1;
        } else if (m & IN_DOWN) {
            sel = sel + 1 < rows ? sel + 1 : 0;
        }
        if (r != sel) poke_row(r, 0, 0);
        poke_row(sel, 1, edit);
    }
}

/* ---- the main page -------------------------------------------------------- */

/* Menu entry i (M_x) at row r. */
static void menu_row(uint8_t r, uint8_t item, uint8_t sel)
{
    char buf[12];
    char *p;
    uint8_t y = MENU_Y + r * MENU_DY;
    uint8_t fg = sel ? C_WHITE : C_BLACK;
    uint8_t x;

    fill(22, y, 212, 12, sel ? C_BLACK : C_WHITE);
    if (item == M_START) {
        put_str0(30, y + 2, s_start, fg, NO_BG);
    } else if (item == M_DETAILS) {
        put_str0(30, y + 2, s_details, fg, NO_BG);
    } else {
        x = put_str0(30, y + 2, s_pokes, fg, NO_BG);
        if (nm.pokes_on) {
            p = put_str(buf, ": ");
            p = put_dec(p, pokes_on());
            p = put_str(p, s_on);
            *p = 0;
            put_str0(x, y + 2, buf, sel ? C_WHITE : C_GREEN, NO_BG);
        }
    }
}

static void main_page(const uint8_t *items, uint8_t n, uint8_t sel)
{
    const char *st;
    uint8_t c, r, x;

    page(s_nms, s_main_keys);
    panel(12, 30, 232, 146);
    frame(23, 39, 66, 66, C_BLACK);
    put_icon(24, 40);
    put_wrap(100, 42, nm.title, 17, 10, 72, C_BLACK);

    st = nm.status[0] ? (const char *)nm.status : s_untested;
    c = C_GREY;
    if (!strcmp(st, s_working)) c = C_GREEN;
    else if (!strcmp(st, s_imperfect)) c = C_ORANGE;
    else if (strcmp(st, s_untested)) c = C_DRED;
    x = put_str0(100, 92, s_status, C_GREY, NO_BG);
    put_str0(x + 8, 92, st, c, NO_BG);

    for (r = 0; r < n; r++) menu_row(r, items[r], r == sel);
}

/* ---- the screen ----------------------------------------------------------- */

/* The NextRegs this screen changes, saved when it opens and put back when
 * the game starts. */
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

void *info_show(void *unused)
{
    struct l2_keep keep;
    uint8_t items[3];
    uint8_t n = 0, sel = 0, r, m;

    (void)unused;
    nm.pokes_on = 0;
    memset(nm.poke_val, 0, sizeof(nm.poke_val));
    items[n++] = M_START;
    if (nm.npokes) items[n++] = M_POKES;
    items[n++] = M_DETAILS;

    screen_on(&keep);
    main_page(items, n, sel);
    z80_outp(0x123B, 0x02);                         /* Layer 2 on */
    for (;;) {
        m = wait_input();
        if (!(m & IN_ANY)) continue;     /* a key let go as the wait ended */
        r = sel;
        if (m & IN_DETAILS) {
            details();
            main_page(items, n, sel);
            continue;
        }
        if (m & IN_FIRE) {
            if (items[sel] == M_START) break;
            if (items[sel] == M_DETAILS) details();
            else if (pokes()) break;
            main_page(items, n, sel);
            continue;
        }
        if (m & IN_UP) sel = sel ? sel - 1 : n - 1;
        else if (m & IN_DOWN) sel = sel + 1 < n ? sel + 1 : 0;
        else break;                  /* any other key starts the game */
        menu_row(r, items[r], 0);
        menu_row(sel, items[sel], 1);
    }
    screen_off(&keep);
    return 0;
}
