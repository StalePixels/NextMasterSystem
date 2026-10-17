#!/usr/bin/env python3
"""Build the overlay files for a folder of specs, and their index.

usage: build-overlays.py SPECDIR CARTDIR OUTDIR [--compat CSV] [--titles CSV]
                         [--sjasmplus PATH]

For each SPECDIR/*.spec, the cart is the file in CARTDIR whose CRC32 is the
one on the spec's "cart" line. The CRC32 is computed from each *.sms file
in CARTDIR (not its subfolders), without a copier header, so the cart files
may have any names. Each spec is built with mknms.py into OUTDIR, then
mknmsindex.py writes OUTDIR/index. Any .nms files and index already in
OUTDIR are removed first.

--compat, --titles and --sjasmplus are passed to mknms.py; see its help.

A spec with no "cart" line, or whose cart is not in CARTDIR, is reported
and skipped. The tool then exits with status 1, after building the rest.

Every overlay that uses a library page (a libpage line) must carry the same
bytes for it. When one does not, the tool names the two specs and exits
with status 1.
"""
import argparse
import glob
import os
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mknms  # noqa: E402
import mknmsindex  # noqa: E402


def cart_crcs(cartdir):
    """CRC32 -> path for every *.sms file in cartdir."""
    out = {}
    for name in sorted(os.listdir(cartdir)):
        path = os.path.join(cartdir, name)
        if not name.lower().endswith('.sms') or not os.path.isfile(path):
            continue
        data = open(path, 'rb').read()
        if len(data) % 16384 == 512:
            data = data[512:]
        out.setdefault(zlib.crc32(data) & 0xFFFFFFFF, path)
    return out


def spec_cart(spec):
    """The CRC32 on the spec's cart line, or None."""
    for line in open(spec):
        w = line.split('#')[0].split()
        if len(w) == 2 and w[0] == 'cart':
            return int(w[1], 16)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('specdir')
    ap.add_argument('cartdir')
    ap.add_argument('outdir')
    ap.add_argument('--compat', help='compatibility list CSV')
    ap.add_argument('--titles', help='title list CSV')
    ap.add_argument('--sjasmplus', default='sjasmplus', help='assembler for rastercode files')
    a = ap.parse_args()

    os.makedirs(a.outdir, exist_ok=True)
    for old in glob.glob(os.path.join(a.outdir, '*.nms')) + glob.glob(os.path.join(a.outdir, 'index')):
        os.remove(old)
    carts = cart_crcs(a.cartdir)
    fail = 0
    lib_first = {}   # library page name -> (spec, PAGE data) of the first spec that uses it
    for spec in sorted(glob.glob(os.path.join(a.specdir, '*.spec'))):
        crc = spec_cart(spec)
        if crc is None:
            print(f'{os.path.basename(spec)}: no cart line', file=sys.stderr)
            fail = 1
            continue
        if crc not in carts:
            print(f'{os.path.basename(spec)}: cart {crc:08X} not found', file=sys.stderr)
            fail = 1
            continue
        libs = {}
        try:
            mknms.build(spec, carts[crc], a.outdir, a.compat, a.titles, a.sjasmplus, libs)
        except SystemExit as e:
            print(f'{os.path.basename(spec)}: {e}', file=sys.stderr)
            fail = 1
        for name, data in sorted(libs.items()):
            first, fdata = lib_first.setdefault(name, (spec, data))
            if data != fdata:
                print(f'{os.path.basename(spec)}: library page {name} does not have the bytes it has in '
                      f'{os.path.basename(first)}; a library page must not use a name that a spec '
                      f'defines differently', file=sys.stderr)
                fail = 1
    try:
        mknmsindex.build_index(a.outdir)
    except SystemExit as e:
        print(f'index: {e}', file=sys.stderr)
        fail = 1
    return fail


if __name__ == '__main__':
    sys.exit(main())
