/* nm.h: what every part of the outer shell shares.
 *
 * The shell is C. Its resident part lives in bank 2 ($8000-$BFFF) and is
 * always mapped. Everything else lives in 8K pages that are mapped at
 * $E000 for the length of a far call. Read docs/design.md first.
 */
#ifndef NM_H
#define NM_H

#include <stdint.h>

#include "memplan.h"   /* generated from src/runtime/memplan.inc */
#include "fwsyms.h"    /* generated from the runtime's map file: FW_ABI */

/* ---- banked modules ----------------------------------------------------
 * PAGE_x is the 8K page number that the module's code is linked for. The
 * module's linker section is the high half of a 16K bank: bank 54 is pages
 * 108 and 109, and its high half, page 109, is linked at $E000.
 * Keep these in step with the MODULES list in the Makefile. */
#define PAGE_SESSION   109   /* BANK_54_H: the browse loop and its messages */
#define PAGE_LOADER    111   /* BANK_55_H: cart, CRC32 and the overlay file's walk */
#define PAGE_INFO      113   /* BANK_56_H: the cart information screen */
#define PAGE_OVERLAY   115   /* BANK_57_H: the overlay file's index and chunks */

/* ---- resident memory ---------------------------------------------------- */
#define NM_STACK_TOP   0xBFE0u   /* must equal REGISTER_SP in zpragma.inc */
#define OVL_BUF        ((uint8_t *)0xA000)   /* the loader's file buffer */
#define OVL_BUFSIZE    0x100u

/* ---- far calls ----------------------------------------------------------
 * A banked entry point has the type  void *fn(void *arg).
 * nm_far maps `page` at $E000, calls fn(arg), puts the caller's page back
 * and returns fn's result. Calls nest. */
void *nm_far(uint8_t page, void *(*fn)(void *), void *arg);
#define NM_FAR(page, fn, arg) nm_far((page), (fn), (void *)(arg))

/* ---- operating system calls (glue.asm, os.c) -------------------------------
 * Everything the operating system reads or writes through a pointer must be
 * in resident memory: a buffer on the stack or a global in the resident
 * part. A string in a banked module is not reachable while the OS runs. */

/* esxDOS call: fn is the esxDOS function number. The call returns 1 when
 * the OS reports an error. */
struct nm_esx {
    uint8_t  fn;
    uint8_t  a;     /* in: A, out: A */
    uint16_t bc;    /* in: BC, out: BC */
    uint16_t ix;    /* in: IX */
    uint16_t de;    /* in: DE */
};
uint8_t nm_esx(struct nm_esx *p) __z88dk_fastcall;

/* NextZXOS call through M_P3DOS. `routine` is the DE of the M_P3DOS call and
 * the other registers are its parameters. MMU 6 and 7 are set to the NextZXOS
 * defaults for the call and put back afterwards. With NM_P3_NAME set and a
 * successful result (carry and zero set), the $FF terminated string at HL is
 * copied to nm_name. */
struct nm_p3 {
    uint8_t  a;
    uint16_t hl;
    uint16_t de;
    uint16_t bc;
    uint8_t  f;        /* out: F */
    uint16_t routine;
    uint8_t  opt;
};
#define NM_P3_NAME  1
#define NM_F_CARRY  0x01
#define NM_F_ZERO   0x40
uint8_t nm_p3dos(struct nm_p3 *p) __z88dk_fastcall;

/* Hand over to the runtime and start the game. Never returns. */
struct nm_launch {
    uint32_t crc;        /* the first 9 bytes are copied to the runtime as they are */
    uint32_t size;
    uint8_t  npages;
    uint16_t start;
    uint16_t sp;
    uint16_t hook;
    uint16_t hook2;
    uint8_t  flags;
    uint8_t  nr[43];     /* NextReg number and value pairs, then $FF */
};
void nm_launch(struct nm_launch *p) __z88dk_fastcall;

/* esxDOS file calls, in os.c. Each returns a negative number on failure. */
int16_t nm_open(const char *path);
int8_t  nm_fstat(uint8_t handle, uint8_t *stat16);
int16_t nm_read(uint8_t handle, void *dst, uint16_t n);
int8_t  nm_seek(uint8_t handle, uint32_t pos);   /* from the start of the file */
void    nm_close(uint8_t handle);

#define NM_TITLE_MAX  48

/* ---- shared state --------------------------------------------------------
 * Mutable state that more than one module reads lives here, in the resident
 * part, which is cleared at start. A banked module keeps no mutable data of
 * its own. */
struct nm_state {
    uint8_t  err;             /* 0, or the code of the last failure */
    char     ovl_name[21];    /* "/nm/ovl/XXXXXXXX.nms" */
    uint16_t bflags;          /* the user's Browser view (C) and sort (B) flags */
    uint8_t  filter[16];      /* the user's Browser filter, saved */
    uint8_t  help[120];       /* the browser's two help lines */
    uint8_t  nms_ver[3];      /* the .nms header: format major, minor, framework ABI */
    char     title[NM_TITLE_MAX + 1];   /* the META title, cut to fit; empty if none */
    struct nm_launch launch;
};
extern struct nm_state nm;
extern char nm_name[13];      /* the short file name the browser returned */
#define NM_LNAME_SIZE 128     /* NM_LNAME_MAX in glue.asm is one less */
extern char nm_lname[NM_LNAME_SIZE];   /* its long file name, cut to fit; empty if none */
extern const char nm_filter_sms[];   /* "*.SMS", $FF */
extern const char nm_filetypes[];

/* ---- failure codes (nm.err) ---------------------------------------------- */
#define NM_E_OPEN     1   /* the file could not be opened */
#define NM_E_READ     2   /* the file could not be read */
#define NM_E_SIZE     3   /* the file is empty or too large */
#define NM_E_NOOVL    4   /* no overlay for this CRC32 */
#define NM_E_BADOVL   5   /* the overlay is damaged or too new */
#define NM_E_OTHER    6   /* the overlay is for another cart */
#define NM_E_BADOP    7   /* the overlay has a bad operation */
#define NM_E_DIFFER   8   /* the dump differs from the one the overlay is for */

/* ---- entry points of the banked modules ----------------------------------- */
void *session_init(void *unused);   /* once, at start */
void *session_pass(void *unused);   /* one browser pass */
void *loader_load(void *unused);    /* load nm_name; returns a failure code */
void *info_show(void *unused);      /* show the cart information, wait for a key */
void *loader_check_range(void *a);  /* struct crc_range *: 1 when the CRC32 matches */
void *loader_ramsite_old(void *a);  /* struct ramsite *: a RAMSITES entry's original */
void *overlay_find(void *unused);   /* nm.ovl_name from the index; returns a failure code */
void *overlay_apply(void *f);       /* struct nms *: CRCS, META, CONF, PTCH; failure code */

/* ---- resident entry points ------------------------------------------------- */
void nm_run(void);                  /* the main loop; also where a game's BREAK returns */

#endif
