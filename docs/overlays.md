# Making an overlay

An overlay file (`.nms`) tells NextMasterSystem how to patch one Master System cart. This guide takes a cart from scan to SD card. The file format is in [nms-format.md](nms-format.md).

You need Python 3. You need `sjasmplus` only for a spec with a `rastercode` line or an `asm` block. All commands run from the repository root, and the tools are in `tools/`.

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
- Go through every `CHECK` comment. A low-confidence site is a byte pattern that looks like an I/O instruction in bytes that the scanner did not reach. It can be data. Make it a `site` line only if it is code.
- Check the mapper stores from the byte scan. `sitescan.py` also looks for mapper store byte patterns in code that no path reached, because an unpatched mapper store does not switch the bank and the game then reads the wrong bank. `mkspec.py` writes a spec line for each one with high confidence; the comment after it gives the evidence. Read the code around each one. A `CHECK byte scan` comment is a medium or low confidence hit: make it a spec line only if it is code. [sitescan.md](sitescan.md) describes the ratings.
- Read `game.unproven.tsv`. It lists stores that the scanner could not prove to stay off the mapper registers.

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

Copy every `.nms` file and the `index` file to `/nm/ovl/` on the SD card. When there is no `index`, NextMasterSystem looks only for the file named after the cart's own CRC32.
