# NextMasterSystem

A fixed recompiler that runs Sega Master System games on the ZX Spectrum Next.

## What it is

NextMasterSystem runs the game's own Z80 code on the Next's Z80N processor. NextMasterSystem patches each Master System I/O instruction in the game into a call to a small runtime. The runtime draws with the Next's tilemap, sprites and copper. It plays sound on the AY chips.

An overlay (`.nms` file) holds the patches for one game. NextMasterSystem used the CRC32 of the cart. image to match it to the required overlay.  This means that arbitary cart. images, and patched files most likely won't work unless they have a matching overlay, or alias.

- Z88DK c for the UX/loader/overlay/infoscreen/etc, direct assembly for the hot loops and tight code-caves.

The design notes are in [docs/design.md](docs/design.md).

### Controls

| Master System | Next |
|---|---|
| Direction pad | Master System or Mega Drive pad, or Q A O P |
| Button 1 | Fire 1, or pad B, or SPACE |
| Button 2 | Fire 2, or pad C, or M |
| Pause | Pad Start, or ENTER |
| Quit | BREAK, returns to the browser |

## Licence notes

`src/shell/loader/crc32.asm` contains code from gunzip by Laurens Holst under the BSD 2-clause licence. The licence text is in that file.
