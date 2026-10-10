# The `.nms` overlay file format

An `.nms` file tells NextMasterSystem how to run one Master System game. The file holds the changes NextMasterSystem makes to the player's own cart image, the settings for the game, the game's details for the browser, a 32x32 icon, and any code pages of our own that the game needs. The file never holds bytes copied from a game.

Files live in `/nm/ovl/` on the SD card. Each file is named after the CRC32 of the cart it was made for, in upper-case hex: `/nm/ovl/0123ABCD.nms`.

## Conventions

- All numbers are little-endian.
- `u8`, `u16`, `u24` and `u32` are unsigned integers of 1, 2, 3 and 4 bytes.
- A CRC32 is the standard CRC32 used by zip and PNG. Its polynomial is `$EDB88320`, reflected. Its initial value and final XOR are `$FFFFFFFF`.
- The cart CRC32 is taken over the cart image without a copier header. A cart image whose size is 512 bytes more than a multiple of 16K has a copier header. The reader leaves out the first 512 bytes.
- A cart offset is a byte offset into the cart image, after the copier header is removed.
- Text is ASCII. Each line ends with a single `$0A`.

## File layout

An `.nms` file has a fixed header, then a sequence of chunks, then the `END ` chunk.

### Header: 16 bytes

| Offset | Size | Field |
|---|---|---|
| 0 | 4 | magic: `N`, `M`, `S`, `$1A` |
| 4 | u8 | format major version: 1 |
| 5 | u8 | format minor version: 0 |
| 6 | u8 | framework ABI the file needs; see "Versions" |
| 7 | u8 | reserved, 0 |
| 8 | u32 | primary cart CRC32: the cart the file was made for |
| 12 | u32 | size in bytes of the primary cart. The loader does not check it, because another accepted dump may have another size. |

### Chunks

Every chunk starts with an 8-byte chunk header:

| Offset | Size | Field |
|---|---|---|
| 0 | 4 | tag: four ASCII characters |
| 4 | u32 | length of the chunk data in bytes, not counting this header |

The chunk data follows the header. Chunks may appear in any order, but `END ` is always last. A reader skips any chunk whose tag it does not know, using the length. Each tag may appear only once. `PAGE` is the exception.

A file has no size limit, and neither has a chunk. NextMasterSystem never holds a whole file in memory: it reads the file in order through a small buffer, and seeks back to the chunks it needs. It refuses a file that has `CRCS`, `PTCH`, `CONF` or `META` twice.

| Tag | Required | Content |
|---|---|---|
| `CRCS` | yes | every cart CRC32 this file accepts |
| `PTCH` | yes | the operations that check and change the cart image |
| `CONF` | no | settings |
| `META` | no | the game's details for the browser |
| `ICON` | no | a 32x32 icon |
| `PAGE` | no, any number | a whole 8K bank of code of our own |
| `SIGN` | no | reserved for a signature; readers ignore it for now |
| `END ` | yes | the CRC32 of the file up to this chunk |

## `CRCS`: accepted carts

A list of `u32` CRC32 values, of any length. The first is the primary CRC32 from the header. This file also fits these other dumps of the same game. They are other regions, other revisions, or dumps that differ only in bytes the file does not touch.

Listing a CRC32 here claims that the `CHECK` operations in `PTCH` pass for that dump. The file's tools must prove the claim before they add a CRC32. The loader refuses a file whose `CRCS` does not list the cart's CRC32.

### The alias index

NextMasterSystem does not open every file to find a match. A tool builds `/nm/ovl/index` from the `CRCS` chunks of every file in the folder:

| Offset | Size | Field |
|---|---|---|
| 0 | 4 | magic: `N`, `M`, `S`, `I` |
| 4 | u16 | number of entries |
| 6 | 8 per entry | `u32` accepted CRC32, `u32` primary CRC32, which is the file name |

Entries are sorted by accepted CRC32. A reader can therefore search them with a binary search. NextMasterSystem searches the file in place: it reads only the entries it probes. A cart whose CRC32 is not in the index has no overlay. Without an index, NextMasterSystem looks only for the file named after the cart's own CRC32.

## `PTCH`: operations

The section holds a sequence of operations. Each operation starts with a `u8` opcode. The list ends with `$00`.

| Opcode | Name | Operands | Meaning |
|---|---|---|---|
| `$00` | `END` | | end of the operations |
| `$01` | `CHECK` | `u24` cart offset, `u16` length, `u32` CRC32 | the CRC32 of that range of the cart image must equal the value |
| `$02` | `PATCH` | `u24` cart offset, `u8` n, n bytes | write the bytes into the cart image. The n bytes stay inside one 8K page of the cart: offset mod 8192, plus n, is at most 8192. |
| `$03` | `START` | `u16` address, `u16` stack pointer | the game starts at this address instead of `$0000`, with this SP. An SP of 0 means `$DFF0`. |
| `$04` | `RAMSITES` | `u16` continuation, `u8` n, n entries | patches for code the game builds in RAM; see `RAMSITES` below |
| `$05` | `RASTER` | `u16` length, the routine | the per-line horizontal scroll routine; see `RASTER` below |

The loader reads `PTCH` twice. The first pass runs every `CHECK` and checks every other operation. The second pass applies the operations. If a `CHECK` fails, the loader applies none of them and reports the cart as a different dump. Every byte a `PATCH` writes must lie inside a range that a `CHECK` covers.

A `PATCH` holds only the new bytes, and only the bytes that differ from the cart. A `CHECK` holds only a CRC32 of the original bytes, so the file never carries code or data from the game. A `CHECK` range must lie inside the cart image; a range past its end fails.

A file has at most one `RAMSITES` and at most one `RASTER`, and not both: the framework keeps the `RAMSITES` table and the `RASTER` routine in the same place.

### `RAMSITES`

Some games build code in RAM, so its I/O instructions are not in the cart image. The continuation is the address the game jumps to once its RAM code is built; the cart image is patched to call the framework there first. Each entry is:

| Size | Field |
|---|---|
| u16 | RAM address |
| u8 | length n, from 1 to 4 |
| u16 | low 16 bits of the CRC32 of the original n bytes |
| n | the new bytes |

The framework compares the RAM with the original bytes, writes the new bytes where they match, then jumps to the continuation.

The current framework takes entries of 2 bytes only: an `RST` to the I/O entry and an inline code. The loader refuses other lengths. It works out the original instruction from the inline code and the CRC32:

- codes `$00-$07`: `OUT (n),A`, `D3 n`, with n in that port class;
- codes `$08-$0F`: `IN A,(n)`, `DB n`, with n in that port class;
- any other code: the `ED`-prefixed instruction `ED` code.

Of these candidates, the original is the one whose CRC32 has the entry's low 16 bits. The file's tools make sure exactly one candidate matches. The loader refuses an entry that no candidate matches.

### `RASTER`

Some games set the horizontal scroll on nearly every line from a line interrupt. The Next cannot deliver an interrupt on every line in time, so the file brings a routine that works out each line's scroll value from the game's RAM. The routine is code of our own, assembled to run at `$3C00` in the framework's second page, at most 1024 bytes long. The loader copies it there. Its entry is its first byte.

The framework calls the routine once a frame with HL pointing to a table of 192 bytes, one per line, IX pointing to the framework's copy of VDP registers 0 to 10, and the game's RAM at `$C000`. The routine fills the table with the value of VDP register 8 for each line, and returns with carry set when the table is valid for this frame. With carry clear, the framework uses its normal scroll handling.

## `CONF`: settings

The section is text, with one `key=value` per line. The reader ignores unknown keys.

| Key | Values | Meaning |
|---|---|---|
| `hz` | `50`, `60`, `any` | the frame rate the game was made for. NextMasterSystem can only warn, because the Next sets its rate at boot. |
| `cpu` | `28`, `3.5` | the CPU speed for the game's own code |
| `priority` | `0`, `1` | draw priority tiles again in Layer 2, above the sprites |
| `toppal` | `0`, `1` | show the palette the frame handler leaves from line 0 of the picture |
| `tilecache` | `0`, `1` | copy the tiles that block writes take whole from cart ROM from a converted copy of the cart, made at game start, and do not convert them again |
| `button1`, `button2`, `pause` | key or pad button names | the control map |

NextMasterSystem acts on `priority`, `toppal` and `tilecache`. It does not act on the other keys yet. An engine that does not know `tilecache` ignores it, and the game runs as with `tilecache=0`.

## `META`: the game's details

The section is text, with one `key=value` per line. The browser shows these values. Unknown keys are ignored. For now, the information screen before a game starts shows the `title`.

| Key | Meaning |
|---|---|
| `title` | game title |
| `id` | the game's id in the compatibility list |
| `dump` | the dump's name in the No-Intro list |
| `year`, `publisher`, `regions` | release details |
| `status` | `working`, `imperfect`, `not working` or `untested` |
| `flags` | what is wrong, separated by `\|`: `graphics`, `colors`, `sound`, `controls`, `timing`, `frame overrun`, `crash`, `no saving`, `peripheral` |
| `issues` | what a player sees, in plain words |
| `tested` | where and when it was last tested |
| `version` | the overlay's own version |
| `author` | who made the overlay |

## `ICON`: the icon

The icon is 1024 bytes: 32 rows of 32 pixels. The top row comes first. In each row, the left pixel comes first. Each byte is an index into the Next's default 256-colour palette. In that palette, index n is the 8-bit colour n, in the format `RRRGGGBB`. The ninth blue bit is the OR of the two blue bits. Index `$E3` is transparent, because the Next's default transparency colour is `$E3`.

All icons share this one palette, so the browser can show any number of icons at once.

NextMasterSystem does not read the `ICON` chunk yet.

## `PAGE`: code pages

A page is a whole 8K bank of Z80N code of our own for this game. It can replace a slow routine of the game or act as a library of helpers. A file may hold any number of `PAGE` chunks, one for each page number.

| Offset | Size | Field |
|---|---|---|
| 0 | u8 | page number in this file, from 0 |
| 1 | u8 | number of entries, e, at least 1 |
| 2 | 2 x e | entry addresses, `u16` each |
| 2 + 2e | rest | the page's code and data, at most 8192 bytes |

The code is assembled to run at `$2000-$3FFF`. Each entry address lies inside the code. Entry n of the page is the n-th address in the list.

The loader puts each page into its own 8K RAM page before the game starts, and fills the rest of that RAM page with zeros. The current framework takes page numbers 0 to 7 and at most 64 entries over all the pages of a file. The loader refuses a file with a page number over 7, a page number twice, more entries, no entries, or an entry outside its page's code.

### The far call

A patched site reaches a page entry through a far call. It has one of two forms:

- an `RST` to the framework's I/O entry, the inline code `$80`, then `u8` page and `u8` entry: 4 bytes;
- `CALL $E072` (`jt_far` in the jump table), then `u8` page and `u8` entry: 5 bytes.

The framework then:

1. maps the page into `$2000-$3FFF` (MMU1), in place of the page the window held;
2. jumps to the entry, with the game's registers and the game's interrupt state as they were at the site;
3. when the entry returns, maps the old page back into the window and returns to the byte after the page and entry bytes, with the registers and flags the entry returned.

At the entry, the stack holds the return into the framework, then a word whose low byte is the page the window held, then the return address after the site. An entry can make a far call itself. A page number that the file has no page for, or an entry number that the page does not list, stops the game with a red border.

### Rules for page code

Page code may do what it needs. It can turn interrupts off, switch to a stack of its own inside its page, map other pages, and use any Z80N instruction. It follows these rules:

- Before an entry returns, it restores everything it changed that the game code it replaces does not change: the stack pointer, the interrupt state, the MMU slots, and the registers. The game then carries on as if its own code had run.
- While an entry runs, `$2000-$3FFF` holds the page, not the game's code and data there. `jt_peek` (`$E075` in the jump table) gives in A the byte that the game sees at the address in HL. For an address in `$2000-$3FFF` it reads the game's own page. It keeps every other register except F, and leaves interrupts as they are.
- Page code can use the overlay's I/O `RST` with the inline codes in this file, in the same way as a patched site. For example, one `OTIR` through the framework writes a whole buffer to the VDP.
- `jt_vwrite` (`$E078`, ABI 7) writes bytes into VRAM in runs: the same bytes, in the same places, as a control write of each run's address and then its data writes to the VDP data port. It is much faster than the I/O `RST`, because it maps the pages it uses once for the call. See "Writing VRAM from page code" below.
- The game's interrupt handler can run while an entry runs with interrupts on. The framework then maps the game's own page into `$2000-$3FFF` for the handler, and maps the code page back when the handler returns. An entry can leave interrupts on only for a game whose interrupt code does not write the mapper register `$FFFD`. For any other game, the entry turns interrupts off while it runs.

### Writing VRAM from page code

`call jt_vwrite` takes:

| Register | Value |
|---|---|
| HL | the source of the first run |
| DE | the VRAM address of the first run. Bits 14 and 15 are ignored. |
| B | the bytes in each run, 1 to 256 (0 means 256) |
| C | the number of runs, 1 to 256 (0 means 256) |
| IX | the source step: from the start of one run to the start of the next |
| IY | the VRAM step: from the start of one run to the start of the next. The address wraps at `$4000`. |
| A | 0: the source as the game sees it, so an address in `$2000-$3FFF` reads the game's page there, as `jt_peek` does. Any other value: the source as it is mapped now, so `$2000-$3FFF` is the code page. |

The source lies in `$0000-$DFFF`. For example, a name table column of 28 cells, 2 bytes each, from a copy in RAM with 64 bytes to a row: HL = the copy's first cell, DE = the VRAM address of the column's first cell, B = 2, C = 28, IX = IY = 64.

For each byte, `jt_vwrite` does what the framework does for a write to the data port: it writes the framework's copy of VRAM, the Next tilemaps for a name table entry, the priority marks with the `priority` switch, the mark that a tile must be converted again, and the mark that the sprite table changed. It leaves the VDP state as the writes would: the address after the last byte of the last run, code 1 (a VRAM write), the control latch clear, and the read buffer holding the last byte written.

It keeps BC, DE, HL, IX, IY, the alternate registers and the interrupt state; A and F change. It runs with interrupts off and on a stack of its own, so the game's interrupt handler cannot run in the middle of it. It writes VRAM only: CRAM writes go through the I/O `RST`.

## `END `: integrity

The chunk is one `u32`: the CRC32 of every byte of the file before this chunk's header. A reader that finds a wrong value rejects the file.

## Inline codes

Most changes in `PTCH` replace an instruction in the game with an `RST` to the framework's I/O entry. The `RST` is followed by an inline code byte. That byte tells the framework which instruction it replaced. The inline codes and their operand bytes are part of the framework ABI. A code never changes meaning. New codes need a new ABI version.

| Code | Instruction replaced | Operands after the code |
|---|---|---|
| `$00-$07` | `OUT (n),A` to port class 0-7. The class comes from port bits A7, A6 and A0. | none |
| `$08-$0F` | `IN A,(n)` from port class 0-7 | none |
| `$10-$13` | `LD ($FFFC-$FFFF),A`, a mapper write | one byte, skipped |
| `$14` | `LD HL,$FFFF : LD (HL),n` | n, then two bytes skipped |
| `$15-$17` | `LD ($FFFC-$FFFE),HL` | one byte, skipped |
| `$18-$1F` | `OUT (n),A` to class 0-7, as the first of a run handled in one call | none |
| `$20-$23` | `LD ($FFFC-$FFFE),BC` | two bytes, skipped |
| `$24-$27` | `LD ($FFFC-$FFFE),DE` | two bytes, skipped |
| `$28-$2B` | `LD HL,$FFFC+k : LD (HL),n` | n, then two bytes skipped |
| `$2C-$2E` | Codemasters mapper `LD ($0000/$4000/$8000),A` | one byte, skipped |
| `$2F` | the `RAMSITES` continuation | none |
| `$30-$3F` | `LD (HL),n` with n below 16, HL on a mapper register | none |
| ED second byte | the `ED`-prefixed I/O instruction with that second byte: `IN r,(C)`, `OUT (C),r`, `INI`, `OUTI`, `INIR`, `OTIR`, `IND`, `OUTD`, `INDR`, `OTDR`, and `LD I,A` / `LD A,I` | none |
| `$81 + 8r` | `OUT (C),r`, as the first of a run | none |
| `$C3`, `$CB` | `OUTI`, `OUTD`, as the first of a run | none |
| `$80` | far call into a code page; see `PAGE` | `u8` page, `u8` entry |

## Versions

- The **format version** in the header says how the file is laid out. A reader accepts a file with the same major version and any minor version. A minor version only adds chunks or keys that older readers can skip.
- The **framework ABI** in the header says which inline codes and framework features the file uses. A framework accepts a file whose ABI is not higher than its own. A file with a `PAGE` chunk needs ABI 6, and a file whose page code calls `jt_vwrite` needs ABI 7.
