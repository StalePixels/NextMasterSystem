# Making an overlay

An overlay file (`.nms`) tells NextMasterSystem how to patch one Master System cart. This guide takes a cart from scan to SD card. The file format is in [nms-format.md](nms-format.md).

You need Python 3. You need `sjasmplus` only for a spec with a `rastercode` line, an `asm` block or a `page` block. All commands run from the repository root, and the tools are in `tools/`.

The steps:

1. Scan the cart with `sitescan.py`.
2. Draft a spec with `mkspec.py`.
3. Check and edit the spec by hand.
4. Build the `.nms` file and the index.
5. Copy them to the SD card.

## 1. Scan the cart

```sh
python3 -I tools/sitescan.py game.sms --out scan --name game
```

`sitescan.py` disassembles the cart from its reset and interrupt vectors. It lists every I/O instruction, every store to the mapper registers, mapper store byte patterns in bytes that it did not reach, and the other places a patch may be needed. It writes four files to `scan/`: `game.sites.tsv`, `game.unproven.tsv`, `game.summary.txt` and `game.dis.txt`. Read `game.summary.txt` first. It lists the indirect jumps that the scanner could not follow. If you know where they go, add the targets with `--entry` and scan again. [sitescan.md](sitescan.md) describes the options and the output.

## 2. Draft a spec

```sh
python3 tools/mkspec.py game.sms scan game "Game title" > game.spec
```

A spec is a text file with one change per line. `mkspec.py` reads the scan and writes a first draft: the RST vector the patches use, a `site` line for each I/O instruction it is sure of, a line for each mapper store, including the high-confidence ones from the byte scan, and `IM 1` changed to `IM 2` in an `asm` block. Each `site` and mapper line ends with a comment that shows the instruction it replaces, for example `site 01B6E   ; OUT ($BF),A`. The draft also holds comments that start with `CHECK`. These are the cases that `mkspec.py` could not decide.

## 3. Edit the spec

The draft is not finished. Before you build it:

- Keep the `cart` line. `mkspec.py` writes it with the cart's CRC32 in hex, for example `cart 0123ABCD`. `build-overlays.py` uses this line to find the cart, and `mknms.py` stops if the cart has another CRC32.
- Go through every `CHECK` comment. A `CHECK high`, `CHECK medium` or `CHECK low` site is a byte pattern that looks like an I/O instruction in bytes that the scanner did not reach, rated by how much the bytes around it look like code; the comment gives the evidence. It can be data. Make it a `site` line only if it is code.
- Check the mapper stores from the byte scan. `sitescan.py` also looks for mapper store byte patterns in code that no path reached, because an unpatched mapper store does not switch the bank and the game then reads the wrong bank. `mkspec.py` writes a spec line for each one with high confidence; the comment after it gives the evidence. Read the code around each one. A `CHECK byte scan` comment is a medium or low confidence hit: make it a spec line only if it is code. [sitescan.md](sitescan.md) describes the ratings.
- Read `game.unproven.tsv`. It lists stores that the scanner could not prove to stay off the mapper registers.
- Give the spec an `io` vector (`vector 10 io`, or any free vector, `vector 00 io` when no other is free). `mknms.py` gives a site a trace form (a run of outputs, a loop or straight code with several outputs run in one framework call) only when the spec has an `io` vector. Without it every site is a single trap of about 1,000 to 2,100 Next cycles, and a long copy, such as a 192-byte sprite table, can run past the next frame's work. In DataStorm this made the sprites jump. When a spec patches I/O sites and has no `io` vector, `mknms.py` prints a warning to stderr. The warning is not an error: Canyon Racer (`racer.spec`) has no `io` vector, and a test with one showed little gain. Add the vector, rebuild and measure before you ignore the warning.

`python3 tools/mknms.py --help` lists every spec line and what it does.

## Writing code in a spec

A `poke` line writes raw bytes. When the bytes are Z80 instructions, write them as assembly in an `asm` block instead. The block is assembled with `sjasmplus` when the overlay is built.

```
asm 00089 2        ; IM 1 -> IM 2
    im 2
endasm
```

`asm ADDR LEN` starts the block. `ADDR` is a cart offset in hex, as on the other spec lines. `LEN` is the number of cart bytes that the block replaces, in decimal. The lines after it are `sjasmplus` source, up to a line that holds only `endasm`.

- The block is assembled at the Z80 address that offset `ADDR` runs at. In the first 32K that is the offset itself. For a bank above that, it is `$8000` plus the offset within the 16K bank, because the tools treat every other bank as if it were in slot 2. The address matters for `jp`, `call` and `jr`, and for any label you use.
- The code must not be longer than `LEN`. If it is, the build stops and prints the spec line and the sizes. If it is shorter, the builder fills the rest with `NOP` (`$00`).
- `LEN` must cover whole instructions of the game. The builder does not check that. It takes the CHECK for those bytes from the cart, so you never type the original bytes.
- The `LEN` bytes must stay inside one 8K page of the cart, because a PATCH operation cannot cross a page. The build stops if they do not.
- A comment in the block starts with `;`. In the spec outside a block, both `#` and `;` start a comment.
- Assembler errors are shown with the spec line number.

`poke ADDR OLD NEW` still works. Use it for bytes that are not code, such as a data table.

### Labels

`label NAME ADDR` gives a game address a name for the `asm` blocks. `ADDR` is a cart offset in hex. The builder converts it to the Z80 address in the same way as for an `asm` line. A label is visible in every block of the spec, whether the `label` line comes before the block or after it.

### Names that every block knows

These are the framework's entry points and fixed addresses. They are the same in every overlay. `src/runtime/fw.asm` defines them, and [design.md](design.md) describes the jump table.

The jump table entries. A patch calls or jumps to one of these addresses:

| Name | Address | Purpose |
|---|---|---|
| `jt_out_n` | `$E000` | `OUT (n),A`, with the port number as the inline byte after the RST |
| `jt_in_n` | `$E003` | `IN A,(n)`, with the port number as the inline byte |
| `jt_ed` | `$E006` | the `ED xx` group, with `xx` as the inline byte |
| `jt_ld_de_a` | `$E009` | `LD (DE),A`, aware of the mapper |
| `jt_start` | `$E00C` | start the game (used by the loader) |
| `jt_fatal` | `$E00F` | stop with a red border |
| `jt_outi_run` | `$E012` | a run of `OUTI` to the end of an unrolled block |
| `jt_io` | `$E015` | any I/O instruction, with an operation code as the inline byte |
| `jt_io0` | `$E018` | the same, entered from RST `$00` |
| `fw_resume` | `$E01B` | jump to the outer shell's resume entry |
| `jt_far` | `$E072` | far call into a code page, with the page and entry numbers as the two inline bytes |
| `jt_peek` | `$E075` | for page code: A = the byte the game sees at HL |
| `jt_vwrite` | `$E078` | for page code: write a block of bytes into VRAM, in runs with a step between them |

The fixed state variables:

| Name | Address | Size | Holds |
|---|---|---|---|
| `fw_status` | `$E020` | 1 | loader progress or error code |
| `fw_crc` | `$E021` | 4 | cart CRC32 |
| `fw_size` | `$E025` | 4 | cart size |
| `fw_npages` | `$E029` | 1 | cart size in 8K pages |
| `fw_lastop` | `$E02A` | 1 | the last `ED` operation |
| `fw_frames` | `$E02B` | 2 | frames of vblank work done |
| `cur_mmu` | `$E02D` | 8 | the game's MMU0 to MMU7 pages |
| `vdp_latch` | `$E035` | 1 | VDP control latch |
| `vdp_code` | `$E036` | 1 | VDP code register |
| `vdp_addr` | `$E037` | 2 | VDP address |
| `vdp_rbuf` | `$E039` | 1 | VDP read buffer |
| `vdp_status` | `$E03A` | 1 | VDP status |
| `vdp_regs` | `$E03B` | 16 | VDP registers |
| `nt_base` | `$E04B` | 2 | name table base |
| `cram` | `$E04D` | 32 | colour RAM |
| `fw_start_addr` | `$E06D` | 2 | game start address |
| `fw_start_sp` | `$E06F` | 2 | game stack pointer at the start |
| `isr_n` | `$E071` | 1 | frame handler entries, modulo 256 |

A `label` line may not reuse one of these names.

### Example

A game calls a slow routine at offset `02F10`. The call takes 6 bytes with the instructions that follow it, and the Next does not need any of them. The patch calls the game's own frame wait instead, at offset `01B40`, and leaves the rest as `NOP`:

```
label wait_frame 01B40   ; the game's frame wait
asm 02F10 6              ; was a call to the slow routine
    call wait_frame
endasm
```

The builder assembles `call wait_frame` at `$2F10` as `CD 40 1B`, adds three `NOP` bytes, and writes the six bytes as a PATCH. The CHECK for offsets `02F10` to `02F15` comes from the cart.

## Code pages

A routine that is too slow through the framework's I/O traps can be replaced with code of our own in a code page. A page is an 8K bank that runs at `$2000-$3FFF` while one of its entries runs. [nms-format.md](nms-format.md) describes the far call and the rules that page code follows.

```
page 0 fill_rows clear_map
    ; sjasmplus source, assembled at $2000
fill_rows:
    ...
    ret
clear_map:
    ...
    ret
endpage
```

`page N NAME...` starts the block. `N` is the page number, from 0 to 7. Each `NAME` is a label in the page's source. It becomes the page's entry 0, 1 and so on, in the order of the line. The lines after it are `sjasmplus` source, up to a line that holds only `endpage`. The page knows the same names as an `asm` block. The build stops if the code is longer than 8192 bytes or an entry is not a label in it.

For each entry, every `asm` block of the spec knows `pg_NAME`, its page number, and `ent_NAME`, its entry number. `far_io` is the far call's inline code, `$80`. A patch reaches an entry in one of two ways:

```
asm 01234 4          ; 4 bytes, with the io vector at $00
    rst $00
    db far_io, pg_fill_rows, ent_fill_rows
endasm
asm 01234 5          ; 5 bytes, with no io vector
    call jt_far
    db pg_fill_rows, ent_fill_rows
endasm
```

The entry runs with the game's registers and interrupt state, and the patch goes on after the two bytes with the registers the entry returns. A spec with a page needs framework ABI 6, and ABI 7 when a block calls `jt_vwrite`. `mknms.py` sets it.

In page code:

- Read the game's memory with `call jt_peek` for any address that can be in `$2000-$3FFF`. A plain read there reads the page itself.
- Use the game's I/O `RST` and inline codes for I/O, as a patch does. `rst <io vector>` then `db $B3` is an `OTIR` through the framework: it writes B bytes from HL to the port in C.
- Write VRAM with `call jt_vwrite`. It writes the bytes as the game's writes to the VDP data port would: the framework's copy of VRAM, the Next tilemaps, the priority marks, the tiles to convert again and the sprite table. Each run of bytes needs only one call, and many runs with the same step need only one call too. The arguments and results are in [nms-format.md](nms-format.md).
- The state variables in the table above (`vdp_addr`, `vdp_code`, `vdp_latch` and the others) can be read and written directly.

`overlays/ecco.spec` has a page that writes a name table column with one `jt_vwrite` call. `overlays/aliensyndrome.spec` has a page that writes rows of name table cells.

## Switches

A switch is a spec line of one word, or for `hz` a word and a value. It turns on an engine feature that helps some games and costs others, so each overlay turns on only the ones that measurements show it gains from. `mknms.py` writes the switches into the file's `CONF` chunk as `key=0` or `key=1`, and `hz` as `hz=50`, `hz=60` or `hz=any` ([nms-format.md](nms-format.md)). The information screen lists the switches that are on and shows the video rate the game will use.

| Spec line | `CONF` key | What it does | What it costs | When to turn it on |
|---|---|---|---|---|
| `priority` | `priority` | Draws the tiles that have the priority bit again in Layer 2, above the sprites, in 192-line and 224-line mode. | Layer 2 pages are cleared at game start (RAM pages 102-107, and 192-201 for 224-line mode). Each name table write marks its cell when the cell gets the priority bit or Layer 2 holds it, and the vertical blank work draws the marked cells again. A game that shows many priority cells pays for them every frame. In 224-line mode each H scroll change that moves the first map column shown into another 8-pixel cell draws the priority cells of the cell columns that move (Micro Machines' bath race: about 6,000 cycles a frame on average). A new tile under many priority cells has them all drawn again in one vertical blank, about 6,500 cycles a cell in 224-line mode: Micro Machines' intro screen of about 700 priority cells takes 8 frames once; Layer 2 is hidden until such a whole redraw ends. When the display goes on after the game had it off, the marked cells are drawn before it goes on, and the display-on write waits for them ([design.md](design.md), "Display off and on"). | Tiles with the priority bit must cover sprites, as in the game on the Master System. |
| `toppal` | `toppal` | Shows the palette the frame handler leaves from line 0 of the picture. CRAM writes also go to the second tilemap, sprite and Layer 2 palettes, which are shown from the frame event to the first line event. A display-off write in that time is held until the picture would show it ([design.md](design.md), "Display off and on"). | Each CRAM write does more work, and the frame and line events switch the palettes. | The frame handler writes the palette late, and the top lines of the picture show the wrong colours. |
| `hz 50`, `hz 60`, `hz any` | `hz` | The video rate of the game. With `50` or `60` the engine sets the Next to that rate when the game starts, after the information screen. BREAK out of the game sets the rate the Next booted at again before the browser shows. With `any`, or no `hz` line, the game runs at the rate the Next booted at. The V counter counts like a PAL Master System at 50 Hz and like an NTSC one at 60 Hz ([design.md](design.md), "The video rate"). | At 60 Hz the Next's frame is 264 lines, 481,536 cycles at 28 MHz, against 311 lines and 567,264 cycles at 50 Hz. Its vertical blank is 72 lines against 119. A game whose frame work nearly fills a 50 Hz frame can overrun at 60 Hz. A monitor that cannot show the rate shows no picture until the player presses BREAK. | Set it from the dump's No-Intro regions. Europe only, or Europe and Brazil: `50`. Any of USA, Japan and Brazil without Europe: `60`. USA or Japan with Europe, or World: `any`. Before you set `60`, measure the frame loads at 60 Hz (`tools/mame/run.py --measure` with the overlay built with `hz 60`). |
| `tilecache` | `tilecache` | Tiles that a block write (`OTIR`, `OUTI` runs) copies whole from cart ROM, with the source and the VRAM address aligned alike, are copied from a converted copy of the cart and are not converted again. | The engine converts the whole cart at game start: about 1.1 seconds more of loading for each 256K of cart, and RAM pages 125 and 128-191. Each block write costs more: about 45 cycles for a block read from RAM, and about 250 for a block from ROM that holds no whole aligned tile. | The game copies many tiles from ROM while it plays. Measure the frame loads with and without it (`tools/mame/run.py --measure`), and turn it on only where the loads go down. |

## 4. Build the overlay file and the index

To build one file:

```sh
python3 tools/mknms.py game.spec game.sms ovl
python3 tools/mknmsindex.py ovl
```

`mknms.py` writes `ovl/<CRC32>.nms`. The file holds no bytes from the cart. It holds a CRC32 for each range of the cart it changes and only the new bytes, so it works only with the same dump of the cart. `mknmsindex.py` writes `ovl/index`, which lists every cart CRC32 that the files in `ovl/` accept.

To build a folder of specs:

```sh
python3 tools/build-overlays.py specs carts ovl
```

`build-overlays.py` finds the cart for each spec in `carts/` by the CRC32 on the spec's `cart` line, so the cart files may have any names. It builds every spec, then writes the index. It exits with status 1 if a spec has no `cart` line, if its cart is missing or if the build fails, and builds the rest.

### Game details

With `--compat` and `--titles`, `mknms.py` and `build-overlays.py` put the game's details in the file's `META` chunk. The information screen shows the title. Both files are CSV with a header line:

- the compatibility list: one row per cart dump. The tools read the columns `crc32`, `id`, `nointro_name` (or `dump_name`), `status`, `flags`, `issues`, `tested_on` and `tested_date`.
- the title list: one row per game. The tools read the columns `id`, `title`, `year`, `publisher` and `regions`. A row matches a compatibility row by `id`.

Without them, or for a cart with no row, the title is the spec's `name` line.

## 5. Copy to the SD card

Copy every `.nms` file and the `index` file to an `ovl` folder next to `nms.nex` on the SD card. The folder with `nms.nex` can be anywhere; for example `/nm/nms.nex` with `/nm/ovl/`, or `/games/sms/nms.nex` with `/games/sms/ovl/`. When there is no `index`, NextMasterSystem looks only for the file named after the cart's own CRC32.
