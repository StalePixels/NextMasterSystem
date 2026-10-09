# Making an overlay

An overlay file (`.nms`) tells NextMasterSystem how to patch one Master System cart. This guide takes a cart from scan to SD card. The file format is in [nms-format.md](nms-format.md).

You need Python 3. You need `sjasmplus` only for a spec with a `rastercode` line. All commands run from the repository root, and the tools are in `tools/`.

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

A spec is a text file with one change per line. `mkspec.py` reads the scan and writes a first draft: the RST vector the patches use, a `site` line for each I/O instruction it is sure of, a line for each mapper store, including the high-confidence ones from the byte scan, and `IM 1` changed to `IM 2`. The draft also holds comments that start with `CHECK`. These are the cases that `mkspec.py` could not decide.

## 3. Edit the spec

The draft is not finished. Before you build it:

- Keep the `cart` line. `mkspec.py` writes it with the cart's CRC32 in hex, for example `cart 0123ABCD`. `build-overlays.py` uses this line to find the cart, and `mknms.py` stops if the cart has another CRC32.
- Go through every `CHECK` comment. A low-confidence site is a byte pattern that looks like an I/O instruction in bytes that the scanner did not reach. It can be data. Make it a `site` line only if it is code.
- Check the mapper stores from the byte scan. `sitescan.py` also looks for mapper store byte patterns in code that no path reached, because an unpatched mapper store does not switch the bank and the game then reads the wrong bank. `mkspec.py` writes a spec line for each one with high confidence; the comment after it gives the evidence. Read the code around each one. A `CHECK byte scan` comment is a medium or low confidence hit: make it a spec line only if it is code. [sitescan.md](sitescan.md) describes the ratings.
- Read `game.unproven.tsv`. It lists stores that the scanner could not prove to stay off the mapper registers.

`python3 tools/mknms.py --help` lists every spec line and what it does.

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
