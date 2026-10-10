# NextMasterSystem

A fixed recompiler that runs Sega Master System games on the ZX Spectrum Next.

## What it is

NextMasterSystem runs the game's own Z80 code on the Next's Z80N processor. NextMasterSystem patches each Master System I/O instruction in the game into a call to a small runtime. The runtime draws with the Next's tilemap, sprites and copper. It plays sound on the AY chips.

An overlay (`.nms` file) holds the patches for one game. NextMasterSystem used the CRC32 of the cart. image to match it to the required overlay.  This means that arbitary cart. images, and patched files most likely won't work unless they have a matching overlay, or alias.

- Z88DK c for the UX/loader/overlay/infoscreen/etc, direct assembly for the hot loops and tight code-caves.

The design notes are in [docs/design.md](docs/design.md).

### Overlay files

Overlay files go in `/nm/ovl/` on the SD card, each named after the CRC32 of its cart: `/nm/ovl/0123ABCD.nms`. `/nm/ovl/index` lists every cart CRC32 that the files accept, so one file can serve other dumps of the same game. The file format is in [docs/nms-format.md](docs/nms-format.md).

[docs/overlays.md](docs/overlays.md) shows how to make an overlay for a cart. The tools, all Python 3:

- `tools/sitescan.py` scans a cart for the instructions an overlay has to patch. [docs/sitescan.md](docs/sitescan.md) describes it.
- `tools/mkspec.py` drafts a spec, which is a text list of the changes, from the scan.
- `tools/mknms.py` builds an overlay file from a spec and the player's cart. Its help text describes the spec lines.
- `tools/mknmsindex.py` builds the index from a folder of overlay files.
- `tools/build-overlays.py` builds a folder of specs and the index in one run.

### Controls

| Master System | Next |
|---|---|
| Direction pad | Master System or Mega Drive pad, or Q A O P |
| Button 1 | Fire 1, or pad B, or SPACE |
| Button 2 | Fire 2, or pad C, or M |
| Pause | Pad Start, or ENTER |
| Quit | BREAK: leaves the game for the browser, and leaves the browser for NextZXOS |

## Licence notes

`src/shell/loader/crc32.asm` contains code from gunzip by Laurens Holst under the BSD 2-clause licence. The licence text is in that file.
