/* session.c: the browser loop. Banked (PAGE_SESSION).
 *
 * One pass shows the NextZXOS file browser filtered to .sms files and, for
 * the file the player picks, asks the loader to load it. A failed load
 * leaves a code in nm.err, which the next pass shows in the browser's help
 * line. A started game does not return here; BREAK in the game comes back
 * through nm_resume to nm_run, which calls the next pass. BREAK in the
 * browser leaves NextMasterSystem for NextZXOS (leave, nm_basic).
 *
 * The browser's filter and flags are NextZXOS's own settings and outlive
 * this program, so they are saved before the browser opens and put back as
 * soon as it returns.
 */
#include <arch/zxn.h>
#include <intrinsic.h>
#include <string.h>
#include <z80.h>

#include "nm.h"

#define IDE_BROWSER   0x01BA
#define HELP_WIDTH    51

/* NextRegs the runtime puts back when a game ends. */
static const uint8_t save_regs[] = {
    0x05, 0x08, 0x09, 0x0A, 0x15, 0x43, 0x4A, 0x4B, 0x4C, 0x68, 0x6B,
    0x6E, 0x6F, 0x2F, 0x30, 0x31, 0x12, 0x14, 0x16, 0x17, 0x70
};

/* The help line is 51 characters wide. */
static const char msg_pick[]  = "NextMasterSystem: pick a Master System .sms file";
static const char msg_e1[]    = "That file could not be opened.";
static const char msg_e2[]    = "That file could not be read.";
static const char msg_e3[]    = "That file is empty or larger than 512K.";
static const char msg_e4a[]   = "Unknown game: no /nm/ovl/";
static const char msg_e4b[]   = ".nms for it.";
static const char msg_e5[]    = "Its overlay file is damaged or too new.";
static const char msg_e6[]    = "Its overlay is for another cart (CRC32 or size).";
static const char msg_e7[]    = "Its overlay has a bad operation.";
static const char msg_e8[]    = "This dump differs from the one the overlay is for.";
static const char msg_line2[] = "ENTER loads. Break to exit game, or menu.";

static const char *const msg_tab[] = {
    msg_pick, msg_e1, msg_e2, msg_e3, 0, msg_e5, msg_e6, msg_e7, msg_e8
};

/* Fill nm.help: the message padded to 51 characters, the second line, $FF. */
static void make_help(uint8_t code)
{
    uint8_t *d = nm.help;
    uint8_t n;

    if (code == NM_E_NOOVL) {
        /* the overlay name is the part of nm.ovl_name after "/nm/ovl/" */
        memcpy(d, msg_e4a, sizeof msg_e4a - 1);
        memcpy(d + sizeof msg_e4a - 1, nm.ovl_name + 8, 8);
        n = sizeof msg_e4a - 1 + 8;
        memcpy(d + n, msg_e4b, sizeof msg_e4b - 1);
        n += sizeof msg_e4b - 1;
    } else {
        const char *m = msg_tab[code];
        n = (uint8_t)strlen(m);
        memcpy(d, m, n);
    }
    memset(d + n, ' ', HELP_WIDTH - n);
    memcpy(d + HELP_WIDTH, msg_line2, sizeof msg_line2 - 1);
    d[HELP_WIDTH + sizeof msg_line2 - 1] = 0xFF;
}

/* Once, at start: full speed, and the NextRegs to restore on exit. */
void *session_init(void *unused)
{
    uint8_t i, *o = nm.launch.nr;

    (void)unused;
    intrinsic_di();
    nm.speed = ZXN_READ_REG(REG_TURBO_MODE) & 3;
    ZXN_NEXTREG(REG_TURBO_MODE, 3);
    for (i = 0; i < sizeof save_regs; i++) {
        *o++ = save_regs[i];
        *o++ = ZXN_READ_REG(save_regs[i]);
    }
    *o = 0xFF;
    memcpy(nm.ovl_name, "/nm/ovl/00000000.nms", 21);
    nm.err = 0;
    return 0;
}

static void browser_settings(uint8_t change, const void *filter, uint16_t flags)
{
    struct nm_p3 p;

    p.a = change;
    p.hl = (uint16_t)filter;
    p.de = 0;
    p.bc = flags;
    p.routine = IDE_BROWSER;
    p.opt = 0;
    nm_p3dos(&p);
    nm.bflags = p.bc;
}

/* Put back what session_init changed, then start NextZXOS's BASIC. */
static void leave(void)
{
    const uint8_t *r = nm.launch.nr;

    while (*r != 0xFF) {
        ZXN_WRITE_REG(r[0], r[1]);
        r += 2;
    }
    ZXN_WRITE_REG(REG_TURBO_MODE, nm.speed);
    nm_basic();
}

void *session_pass(void *unused)
{
    struct nm_p3 p;
    uint16_t user_flags;
    uint8_t code;

    (void)unused;
    intrinsic_di();
    z80_outp(0xFE, 1);

    /* The user's filter and flags: read them, then show .sms files with
       directories first. */
    browser_settings(0, nm.filter, 0);
    user_flags = nm.bflags;
    browser_settings(1, nm_filter_sms, user_flags | 0x0040);

    code = nm.err;
    nm.err = 0;
    make_help(code);

    p.a = 0;
    p.hl = (uint16_t)nm_filetypes;
    p.de = (uint16_t)nm.help;
    p.bc = 0;
    p.routine = IDE_BROWSER;
    p.opt = NM_P3_NAME;
    nm_p3dos(&p);
    intrinsic_di();

    browser_settings(1, nm.filter, user_flags);

    /* BREAK or SPACE (carry set, zero clear) leaves for NextZXOS. */
    if ((p.f & (NM_F_CARRY | NM_F_ZERO)) == NM_F_CARRY)
        leave();

    /* An error (carry clear) opens the browser again. */
    if (!(p.f & NM_F_CARRY))
        return 0;

    nm.err = (uint8_t)(uintptr_t)NM_FAR(PAGE_LOADER, loader_load, 0);
    return 0;
}
