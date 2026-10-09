# NextMasterSystem design notes

NextMasterSystem runs Sega Master System games on the ZX Spectrum Next. The program is one NEX file, `nms.nex`. It has two parts.

- The **outer shell** is C. It shows the NextZXOS file browser, reads the game file, finds the game's patch file, which is an overlay, applies it, shows an information screen about the game, and starts the game. When the player presses BREAK in a game, control returns to the shell, and the browser opens again. A future graphical interface will be added to the shell.
- The **runtime** is Z80 assembly. It runs while a game runs. It receives every I/O instruction the game makes. It drives the Next's tilemap, sprites, copper and sound chips. The build assembles the runtime separately, and puts it into the NEX as three ready-made 8K pages.

This file describes the layout of both parts. It also covers how the shell is split over banked memory, and how to extend it.

## Memory map

The Next has 8K pages. The CPU sees eight of them at a time, one in each 8K slot of the 64K address space. NextRegs `$50` to `$57` choose the page for each slot. These are MMU0 to MMU7.

### While the shell runs

| Address | Slot | Content |
|---|---|---|
| `$0000` to `$3FFF` | 0, 1 | NextZXOS ROM. The shell never changes it. |
| `$4000` to `$7FFF` | 2, 3 | NextZXOS bank 5: screen and system variables. The shell writes here only on the information screen, and only to the ULA screen from `$4000` to `$5AFF`. |
| `$8000` to `$9FFF` | 4 | Resident part: C start-up code, `main`, far-call code, operating system glue, shared state, library routines. |
| `$A000` to `$A0FF` | 5 | `OVL_BUF`: the loader reads the overlay index and the overlay file through these 256 bytes (`OVL_BUFSIZE`). |
| `$A100` to `$BDFF` | 5 | Free. |
| `$BE00` to `$BFDF` | 5 | Stack. It grows down from `$BFE0`. |
| `$C000` to `$DFFF` | 6 | A data window. The loader maps the cart's RAM pages here one at a time. |
| `$E000` to `$FFFF` | 7 | The **banked code window**. A far call maps a module's page here. |

Slots 4 and 5 are NEX bank 2. They are always mapped. Everything the shell hands to the operating system lives there. See "Pointers given to the operating system" below.

The Makefile passes `--main-fence 0xA000` to the linker. The build fails if code, data or BSS of the resident part grows past `$A000`. `OVL_BUF` starts at `$A000`.

### Pages

Page numbers are 8K pages. A NEX bank is two pages. So bank `n` is pages `2n` and `2n+1`. `src/runtime/memplan.inc` is the authoritative list of the runtime's pages. The Makefile turns it into `build/memplan.h` for the C code. In short:

| Pages | Use |
|---|---|
| 10, 11, 14 | NextZXOS's tile definitions and tilemaps, in banks 5 and 7. The runtime borrows them while a game runs and keeps copies in pages 27, 30 and 31. |
| 24, 25 | Runtime, parts 1 and 2, in bank 12. Part 1 runs at `$E000`, part 2 at `$2000`. |
| 26, 28, 29 | SMS RAM and the 16K video RAM copy. |
| 32 and up | The cart, up to 512K. |
| 96 to 99 | Cart RAM. |
| 100 | Runtime part 3, in bank 50, mapped at `$0000` during the vertical blank work only. |
| 102 to 107 | Layer 2, used for priority tiles. |
| 108 to 113 | The shell's banked C modules, in banks 54, 55 and 56. |

The NEX file asks for the 2 MB memory flag, because pages above 95 are used.

### While a game runs

The runtime owns the machine. `jp` to `$E00C` starts it. The jump table at `$E000` is the overlay ABI. Its entries never move. `FW_ABI` in `src/runtime/fw.asm` is its version. The state variables at `$E020` to `$E071` are at fixed addresses too. Existing overlays depend on both.

One entry is new. It sits in the free bytes after the table's last jump: `fw_resume` at `$E01B`, a `jp` whose two target bytes are at `$E01C`. The shell points it at its resume entry before it starts a game. The runtime's quit routine jumps to it. The runtime then restores NextZXOS's pages and registers, so the shell finds the machine as it left it.

## Banked code

### Why 8K pages at `$E000`

Only one page is mapped at `$E000` at a time. The shell uses MMU7 for code and keeps MMU6 free. So a module can map cart data at `$C000` and work on it without unmapping itself. The linker sections are the high halves of 16K banks, `BANK_54_H` and `BANK_55_H`. z88dk links them at `$E000`. The low half of each bank is free for read-only data that code maps through MMU6. `BANK_54_L` and `BANK_55_L` are linked at `$C000`.

### Far calls

The trampoline is `nm_far` in `src/shell/far.c`:

```c
void *nm_far(uint8_t page, void *(*fn)(void *), void *arg);
```

It reads the current MMU7 page, maps `page` at `$E000`, calls `fn(arg)`, puts the old page back, and returns the result.

The calling convention:

- Every banked entry point has the type `void *fn(void *arg)`. To pass more than one value, pass a pointer to a structure in resident memory. To return a small number, cast it to `void *`.
- `page` is the page number the module is linked for. `src/shell/nm.h` has one `PAGE_` constant per module.
- Call a banked entry point only through `nm_far`, using the `NM_FAR` macro. A direct call works only if the caller is in the same page.
- Calls nest. Banked code may far-call another module, and `nm_far` restores each caller's page on the way out. The stack is resident, so it survives page changes.
- Code in a module calls the resident part directly. That covers the library, `nm_esx` and so on. Resident code never calls into a module except through `nm_far`.
- A pointer into a module's code or constants is valid only while its page is mapped. Do not keep one across a far call that may map another page.
- Interrupts are off for the whole run of the shell, so no interrupt handler sees a changed MMU7.

### Data in banked modules

- Modules keep no mutable data of their own. Shared state is in `struct nm_state`. The variable is `nm`, in `src/shell/state.c`. It is resident and cleared at start. Only the resident part is cleared, so do not rely on a module's uninitialised data being zero.
- `const` data in a module is fine. Messages and tables are examples. The data is read while the module's page is mapped.

### Pointers given to the operating system

NextZXOS and esxDOS read and write through pointers while their own pages are mapped at `$C000` and above. Anything passed to them has to be below `$C000`:

- Buffers and strings handed to `nm_esx` and `nm_p3dos` live in the resident part. This means a global variable, or a local variable on the stack.
- `nm_filter_sms` and `nm_filetypes` in `state.c` are examples. Putting them in a module would pass NextZXOS a pointer into a page it cannot see.

`nm_p3dos` also sets MMU6 and MMU7 to pages 0 and 1, which NextZXOS expects. It puts the old values back.

### The information screen

After `loader_load` has read the cart, found the overlay and applied it without error, and before it starts the game, it far-calls `info_show`. `info_show` is in `src/shell/info/info.c`, in the page `PAGE_INFO`. A failure returns to the browser with its message, and the screen is not shown.

`info_show` first writes 0 to port `$FF`, because the browser leaves a Timex mode on. It then clears the standard ULA screen and prints 32 columns of text. It takes the character shapes from the 48K ROM at `$3D00`, which is mapped while the shell runs. So the module has no font of its own. It prints:

- the file name. It is `nm_lname`, the long name that the browser gives in DE. `glue.asm` copies it next to the short name, cut to 127 characters. If the browser gave no long name, it is `nm_name`.
- the CRC32 and size, from `nm.launch`.
- from the overlay file, as the loader read it into `nm`: the `title` from its `META` chunk (`nm.title`), cut to 48 characters and broken over lines at spaces; the format version from the header, as major.minor; and the framework ABI the file needs (both in `nm.nms_ver`).
- the flags, in words: `priority tiles`, `line-0 palette`, or `none`. They are the `CONF` switches as the loader read them, from `nm.launch.flags`.

It then waits. First it waits, for at most a short time, until no key and no joystick fire is held. This stops the key that picked the cart in the browser from counting. Then it polls every keyboard row, from port `$00FE`, and the Kempston joystick 1 fire bit, from port `$1F`, bit 4. It returns when one is pressed. Interrupts are off, so this is a polling loop. The game then starts as before.

### Loading an overlay file

`loader_load` in `src/shell/loader/loader.c` does this, in order. The file format is [nms-format.md](nms-format.md).

The loader never holds a whole file in memory. It reads the index and the overlay file through `OVL_BUF`, 256 bytes, so a file or a chunk can be of any size. A small reader in `loader.c` (`struct rd`) hands out the bytes of one run of the file in order: `rd_take` gives the next few bytes in one piece, and `rd_piece` gives the next bytes in pieces for long data such as a `PATCH` or a `RASTER` routine. An operation may cross the end of the buffer: the reader moves the bytes not yet used to the start and reads more after them. `nm_seek` (esxDOS `F_SEEK`) starts a run anywhere in the file.

1. It reads the cart into pages 32 and up and computes its CRC32.
2. It finds the overlay file in `/nm/ovl/index`, if the file is there. It searches the index in place with a binary search: for each entry it probes, it seeks to the entry and reads its 8 bytes. The entry gives the primary CRC32, which names the overlay file. A cart that is not in the index has no overlay. Without an index, the overlay file is the one named after the cart's own CRC32.
3. The walk. It reads `/nm/ovl/<CRC32>.nms` once from the start to the end, and every byte up to the `END ` chunk goes through the running CRC32. It checks the header: the magic, format major version 1, and a framework ABI not higher than `FW_ABI`. It reads each chunk header, checks that the chunk fits in the file, and notes where `CRCS`, `PTCH`, `CONF` and `META` start. It reads every other chunk only for the CRC32. `END ` must be last, with the right CRC32, and nothing may follow it. `CRCS` and `PTCH` must be there, and each of the four chunks may appear only once.
4. It seeks back to `CRCS` and checks that it lists the cart's CRC32. A list of any length works.
5. It seeks to `META` and keeps the `title` in `nm.title`, and seeks to `CONF` and keeps the switches `priority=1` and `toppal=1` in the runtime's flags.
6. `PTCH`, first pass. It runs every `CHECK` operation against the cart pages, checks the bounds of every other operation, and works out the original instruction of every `RAMSITES` entry. Nothing is written yet, so a dump that fails a `CHECK` is left as it was read.
7. `PTCH`, second pass. It seeks back to the start of `PTCH` and applies the operations: `PATCH` into the cart pages, `START` into the start address and stack pointer, and `RAMSITES` or `RASTER` into the framework's second page from `$3C00`, through MMU6. For `RAMSITES` it writes the table the framework reads: the continuation, the count, and for each entry the address, the two original bytes and the two new bytes. It sets the hook addresses that the runtime reads, `rast_hook` and `ramp_hook`.

Only a failed read can stop the second pass. The cart is then part patched, and the loader reports the file as damaged. Picking the cart again reads it again from the card.

The failure codes and their messages are in `src/shell/nm.h` and `src/shell/session/session.c`. "Unknown game" names the file that the loader looked for.

#### Loading `PAGE` chunks

The loader does not load `PAGE` chunks yet. The walk reads them for the CRC32 like any other chunk it does not use. Loading one is an addition to the walk, at the place in `walk()` marked for it:

1. Read the chunk's own header, the page number and the entry addresses, through `OVL_BUF` and the running CRC32, like any other chunk data.
2. Pick a free 8K RAM page for the chunk and map it at `$C000` with MMU6.
3. Copy the part of the page's code that is already in `OVL_BUF` to the start of the page, then read the rest of the chunk with `nm_read` straight into the page.
4. Run the CRC32 over the page's bytes where they are, in place of reading them through `OVL_BUF`.

The code goes into its page once, during the walk, and is never read twice. If the walk then fails, the file is refused and the page is not used.

### Starting a game

`nm_launch` is in `src/shell/glue.asm`. It copies the start-up values into the runtime's state variables. It saves the NextZXOS pages that the runtime overwrites: the tile definitions and one tilemap page. It maps the runtime at `$E000`. Then it jumps to the jump table's start entry. It never returns. Only the resident part can do this, because the runtime replaces whatever is in slot 7.

### Coming back

BREAK in a game makes the runtime restore NextZXOS. It then jumps to `fw_resume`, which jumps to `nm_resume` in `glue.asm`. `nm_resume` sets the stack to `$BFE0`, maps pages 0 and 1 at `$C000` and `$E000`, and jumps to `nm_run`. The stack frames of the first pass are abandoned. The state in `nm` is kept, so a failure message from a rejected game is still shown.

## Source layout

```
Makefile                 one-command build: make
src/runtime/             the assembly runtime (z80asm)
    runtime.asm          three sections: fw, fw2, fw3, one per page
    fw.asm fw2.asm fw3.asm trace.asm trvars.inc
    tables.inc tables2.inc tables3.inc    generated by tools/gentables.py
    memplan.inc          page numbers of the memory plan
src/shell/               the C shell
    nm.h                 shared declarations, PAGE_ numbers, failure codes
    main.c               main and the main loop (resident)
    far.c                the far-call trampoline (resident)
    state.c              shared state and strings handed to the OS (resident)
    os.c                 esxDOS file calls (resident)
    glue.asm             nm_esx, nm_p3dos, nm_launch, nm_resume (resident)
    fwpages.asm          puts the runtime's pages into their banks
    zpragma.inc          linker settings (stack, start address)
    session/session.c    browser loop and messages (BANK_54_H)
    loader/loader.c      cart reading, overlay checks and patching (BANK_55_H)
    loader/crc32.asm     CRC32 (BANK_55_H)
    info/info.c          the information screen (BANK_56_H)
tools/check-layout       build-time layout checks
tools/mknms.py           builds an overlay file from a spec and the cart
tools/mknmsindex.py      builds /nm/ovl/index from a folder of overlay files
tools/build-overlays.py  builds a folder of specs and the index
tools/sitescan.py        scans a cart for the sites an overlay patches
tools/mkspec.py          drafts a spec from a scan
tools/gentables.py       regenerates the runtime's tables
build/                   all build output; build/nms.nex is the result
```

### How the build fits together

1. `z88dk-z80asm -split-bin` assembles `runtime.asm`. Its three sections have their own origins: `$E000`, `$2000` and `$0000`. The output is one file per section, each padded to 8192 bytes, plus a map file.
2. The Makefile reads the map for the few runtime addresses the shell needs. It writes them to `build/fwsyms.inc` and `build/fwsyms.h`. It also turns `memplan.inc` into `build/memplan.h`.
3. `zcc` compiles each C file. Resident files use the default sections. Module files get `--codeseg`, `--constseg`, `--dataseg` and `--bssseg` set to the module's bank section.
4. `fwpages.asm` puts the three runtime files into banks 12 and 50 as plain bytes with `binary`.
5. `zcc -create-app -subtype=nex` links everything and writes the NEX.
6. `tools/check-layout` runs. It checks size and alignment rules that the assembler cannot check. The rules are listed in that file.

The runtime is assembled at addresses that have nothing to do with where its bytes sit in the NEX. The NEX loader puts bank 12 and bank 50 into physical pages 24, 25 and 100. The runtime maps them where it wants.

## Adding a C module

1. Make a directory `src/shell/<name>/`. Put the C and assembly files in it.
2. Choose a free bank. Banks 54, 55 and 56 are taken. Bank 57 would be pages 114 and 115. Keep the pages below page 224, and clear of the pages in the memory map.
3. In the `Makefile`, add the name to `MODULES`. Set `<name>_SEG` to the bank's high half, for example `BANK_57_H`.
4. In `src/shell/nm.h`, add `PAGE_<NAME>`. Its value is the high half's page number, 115 for bank 57. Declare the entry points, each as `void *fn(void *arg)`.
5. Call it with `NM_FAR(PAGE_<NAME>, fn, arg)`.
6. Assembly files in a module start with `section BANK_57_H`.

A module has 8K for code and constants. When a module gets full, split it. The linker stops with a message when a section does not fit.

If a module needs data larger than a few hundred bytes, such as icons or a font, put it in the low half of its bank. That half is `BANK_57_L`, linked at `$C000`. Map the page with `ZXN_WRITE_MMU6`.

## Known limits

- The memory plan limits a cart to 512K. A cart between 512K and 512K plus 255 bytes passes the size check. It then uses one page too many. This is the prototype's check, kept as it was.
- A `PATCH` must stay inside one 8K cart page. A `RASTER` routine or a `RAMSITES` table must fit in the 1024 bytes from `$3C00` in the runtime's second page. The shell refuses an overlay file that breaks these rules, and reports failure 7. It does not write past the page.
- `$E01B` to `$E01D` was unused in the runtime's page. It now holds `fw_resume`. Overlays do not touch it.
