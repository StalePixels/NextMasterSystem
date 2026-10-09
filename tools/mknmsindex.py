#!/usr/bin/env python3
"""Build the alias index of a folder of .nms overlay files.

usage: mknmsindex.py FOLDER [OUT]

Reads the CRCS chunk of every FOLDER/*.nms and writes the index (default
FOLDER/index): magic NMSI, u16 entry count, then one entry per accepted
CRC32, sorted by it: u32 accepted CRC32, u32 primary CRC32. The primary
CRC32 is the file name. docs/nms-format.md describes the index.

The tool checks each file's header and END chunk, and that the file is
named after its primary CRC32. It stops if two files accept the same CRC32.
"""
import glob
import os
import struct
import sys
import zlib


def read_crcs(path):
    d = open(path, 'rb').read()
    if d[:4] != b'NMS\x1a' or d[4] != 1:
        raise SystemExit(f'{path}: not an .nms file of format 1')
    primary = struct.unpack_from('<I', d, 8)[0]
    if os.path.basename(path).upper() != f'{primary:08X}.NMS':
        raise SystemExit(f'{path}: the file name is not its primary CRC32 {primary:08X}')
    p, crcs, end = 16, None, False
    while p + 8 <= len(d):
        tag, n = d[p:p + 4], struct.unpack_from('<I', d, p + 4)[0]
        if p + 8 + n > len(d):
            raise SystemExit(f'{path}: chunk {tag!r} runs past the end of the file')
        if tag == b'CRCS':
            crcs = list(struct.unpack_from(f'<{n // 4}I', d, p + 8))
        elif tag == b'END ':
            if p + 8 + n != len(d) or struct.unpack_from('<I', d, p + 8)[0] != zlib.crc32(d[:p]) & 0xFFFFFFFF:
                raise SystemExit(f'{path}: bad END chunk')
            end = True
        p += 8 + n
    if not end or not crcs or crcs[0] != primary:
        raise SystemExit(f'{path}: no END chunk, or CRCS does not start with the primary CRC32')
    return primary, crcs


def build_index(folder, out=None):
    """Write the index of folder's .nms files to out (default folder/index)."""
    out = out or os.path.join(folder, 'index')
    seen = {}
    for path in sorted(glob.glob(os.path.join(folder, '*.nms'))):
        primary, crcs = read_crcs(path)
        for c in crcs:
            if c in seen and seen[c] != primary:
                raise SystemExit(f'{c:08X} is accepted by both {seen[c]:08X}.nms and {primary:08X}.nms')
            seen[c] = primary
    if len(seen) > 0xFFFF:
        raise SystemExit('too many entries')
    data = b'NMSI' + struct.pack('<H', len(seen))
    data += b''.join(struct.pack('<II', c, seen[c]) for c in sorted(seen))
    open(out, 'wb').write(data)
    print(f'{out}: {len(seen)} entries')


def main():
    if len(sys.argv) not in (2, 3):
        raise SystemExit(__doc__)
    build_index(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else None)


if __name__ == '__main__':
    main()
