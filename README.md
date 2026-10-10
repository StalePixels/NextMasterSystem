# NextMasterSystem

A fixed recompiler that runs Sega Master System games on the ZX Spectrum Next.

## What it is

NextMasterSystem runs the game's own Z80 code on the Next's Z80N processor. NextMasterSystem patches each Master System I/O instruction in the game into a call to a small runtime. The runtime draws with the Next's tilemap, sprites and copper. It plays sound on the AY chips.

An overlay (`.nms` file) holds the patches for one game. NextMasterSystem uses the CRC32 of the cart image to match it to the required overlay. This means that arbitrary cart images, and patched files, most likely won't work unless they have a matching overlay, or alias.

- z88dk C for the UX/loader/overlay/info screen/etc, direct assembly for the hot loops and tight code caves.
- Overlays can carry their own native code pages, for the game routines that are too slow through the runtime.
- Engine features with a cost are switches, turned on per overlay. [docs/overlays.md](docs/overlays.md) lists them.

The design notes are in [docs/design.md](docs/design.md).

### What you need

- A ZX Spectrum Next with 2 MB of RAM. It won't work on a 1 MB machine.
- Your own `.sms` cart dumps. No games come with NextMasterSystem, and each dump must match an overlay.

### Playing

Start `nms.nex` (for example `/nm/nms.nex`), pick a `.sms` file in the browser, and press a key on the info screen. The info screen shows the game, its state (working, imperfect, not working, untested) and the video rate it will use.

Games made for one rate only (50 Hz PAL or 60 Hz NTSC) switch the Next to that rate when the game starts. Games sold for both run at the rate the Next started with. The browser and the info screen always use the rate the Next started with, so BREAK always gets you back to a screen your monitor can show.

### Overlay files

Overlay files go in an `ovl` folder next to `nms.nex`, each named after the CRC32 of its cart: `ovl/0123ABCD.nms`. NextMasterSystem finds `ovl` in the folder it was started from, so the folder holding `nms.nex` can be anywhere on the SD card. `ovl/index` lists every cart CRC32 that the files accept, so one file can serve other dumps of the same game. The file format is in [docs/nms-format.md](docs/nms-format.md).

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
