# The `.nms` overlay file format

An `.nms` file tells NextMasterSystem how to run one Master System game. The file holds the changes NextMasterSystem makes to the player's own cart image, the settings for the game, the game's details for the browser, a 32x32 icon, and any code pages of our own that the game needs. The file never holds bytes copied from a game.

Files live in `/nm/ovl/` on the SD card. Each file is named after the CRC32 of the cart it was made for, in upper-case hex: `/nm/ovl/2728FAA3.nms`.

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
| 12 | u32 | cart size in bytes |

### Chunks

Every chunk starts with an 8-byte chunk header:

| Offset | Size | Field |
|---|---|---|
| 0 | 4 | tag: four ASCII characters |
| 4 | u32 | length of the chunk data in bytes, not counting this header |

The chunk data follows the header. Chunks may appear in any order, but `END ` is always last. A reader skips any chunk whose tag it does not know, using the length. Each tag may appear only once. `PAGE` is the exception.

| Tag | Required | Content |
|---|---|---|
| `CRCS` | yes | every cart CRC32 this file accepts |
| `PTCH` | yes | the operations that check and change the cart image |
| `CONF` | no | settings |
| `META` | no | the game's details for the browser |
| `ICON` | no | a 32x32 icon |
| `PAGE` | no, any number | an 8K page of code of our own |
| `SIGN` | no | reserved for a signature; readers ignore it for now |
| `END ` | yes | the CRC32 of the file up to this chunk |

## `CRCS`: accepted carts

A list of `u32` CRC32 values. The first is the primary CRC32 from the header. This file also fits these other dumps of the same game. They are other regions, other revisions, or dumps that differ only in bytes the file does not touch.

Listing a CRC32 here claims that the `CHECK` operations in `PTCH` pass for that dump. The file's tools must prove the claim before they add a CRC32.

### The alias index

NextMasterSystem does not open every file to find a match. A tool builds `/nm/ovl/index` from the `CRCS` chunks of every file in the folder:

| Offset | Size | Field |
|---|---|---|
| 0 | 4 | magic: `N`, `M`, `S`, `I` |
| 4 | u16 | number of entries |
| 6 | 8 per entry | `u32` accepted CRC32, `u32` primary CRC32, which is the file name |

Entries are sorted by accepted CRC32. A reader can therefore search them with a binary search. A cart whose CRC32 is not in the index has no overlay. Without an index, NextMasterSystem looks only for the file named after the cart's own CRC32.

## `PTCH`: operations

The section holds a sequence of operations. Each operation starts with a `u8` opcode. The list ends with `$00`.

| Opcode | Name | Operands | Meaning |
|---|---|---|---|
| `$00` | `END` | | end of the operations |
| `$01` | `CHECK` | `u24` cart offset, `u16` length, `u32` CRC32 | the CRC32 of that range of the cart image must equal the value |
| `$02` | `PATCH` | `u24` cart offset, `u8` n, n bytes | write the bytes into the cart image |
| `$03` | `START` | `u16` address, `u16` stack pointer | the game starts at this address instead of `$0000`, with this SP. An SP of 0 means `$DFF0`. |
| `$04` | `RAMSITES` | `u16` continuation, `u8` n, n entries | patches for code the game builds in RAM; see `RAMSITES` below |
| `$05` | `RASTER` | `u8` page, `u8` entry | the per-line horizontal scroll routine is entry `entry` of code page `page` |

The loader runs every `CHECK` before it applies any `PATCH`. If one fails, the loader applies none of them and reports the cart as a different dump. Every byte a `PATCH` writes must lie inside a range that a `CHECK` covers.

A `PATCH` holds only the new bytes. A `CHECK` holds only a CRC32 of the original bytes, so the file never carries code or data from the game.

### `RAMSITES`

Some games build code in RAM, so its I/O instructions are not in the cart image. The continuation is the address the game jumps to once its RAM code is built; the cart image is patched to call the framework there first. Each entry is:

| Size | Field |
|---|---|
| u16 | RAM address |
| u8 | length n, from 1 to 4 |
| u16 | low 16 bits of the CRC32 of the original n bytes |
| n | the new bytes |

The framework checks each entry and patches the RAM code, then jumps to the continuation.

## `CONF`: settings

The section is text, with one `key=value` per line. The reader ignores unknown keys.

| Key | Values | Meaning |
|---|---|---|
| `hz` | `50`, `60`, `any` | the frame rate the game was made for. NextMasterSystem can only warn, because the Next sets its rate at boot. |
| `cpu` | `28`, `3.5` | the CPU speed for the game's own code |
| `priority` | `0`, `1` | draw priority tiles again in Layer 2, above the sprites |
| `toppal` | `0`, `1` | show the palette the frame handler leaves from line 0 of the picture |
| `button1`, `button2`, `pause` | key or pad button names | the control map |

## `META`: the game's details

The section is text, with one `key=value` per line. The browser shows these values. Unknown keys are ignored.

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

## `PAGE`: code pages

A page is 8K of Z80N code of our own for this game. It can replace a slow routine of the game, hold a per-line raster routine, or act as a library of helpers. A file may hold any number of pages.

| Offset | Size | Field |
|---|---|---|
| 0 | u8 | page number in this file, from 0 |
| 1 | u8 | number of entries, e |
| 2 | 2 x e | entry addresses, `u16` each |
| 2 + 2e | rest | the page's code and data, at most 8192 bytes |

The loader puts each page into a free 8K RAM page before the game starts. The code is assembled to run at `$2000-$3FFF`. When the game reaches it, the framework maps the page into that window, calls the entry, and maps the window back when the entry returns. Patched sites reach a page entry through the far-call inline code, described below.

Page code may do what it needs. It can turn interrupts off, switch to a stack of its own inside its page, map other pages, and use any Z80N instruction. One rule applies to it. Before an entry returns, the entry restores everything it changed: the stack pointer, the interrupt state, the MMU slots, and any registers that the replaced game code did not change. The game then carries on as if its own code had run.

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
| to be assigned | far call into a code page | `u8` page, `u8` entry |

## Versions

- The **format version** in the header says how the file is laid out. A reader accepts a file with the same major version and any minor version. A minor version only adds chunks or keys that older readers can skip.
- The **framework ABI** in the header says which inline codes and framework features the file uses. A framework accepts a file whose ABI is not higher than its own.
