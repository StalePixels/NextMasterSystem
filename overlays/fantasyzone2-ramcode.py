#!/usr/bin/env python3
"""Fantasy Zone II builds its VRAM routines in RAM ($CC00-$CF7A) by
unpacking a stream from bank 6 ($B7D5, ROM $1B7D5) with its routine at
$07A9 (run-length bytes, written every other byte: the even bytes, then
the odd ones). This finds the I/O instructions in the unpacked code (the
detector log's RAM PCs) and prints spec poke lines that change the packed
stream so the unpacked code holds RST io + op at each, as the overlay
does for code in ROM.

usage: fantasyzone2-ramcode.py CART IO.TSV RST_OPCODE
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))
import tracedef  # noqa: E402

cart = open(sys.argv[1], 'rb').read()
rst = int(sys.argv[3], 16)
SRC, DST = 6 * 0x4000 + 0x37D5, 0xCC00


def unpack(data):
    """-> (out bytes by address, stream offset that made each byte)"""
    out, src = {}, {}
    p = SRC
    for phase in range(2):
        d = DST + phase
        while True:
            c = data[p]
            p += 1
            if c == 0:
                break
            n = c & 0x7F
            for _ in range(n):
                out[d], src[d] = data[p], p
                if c & 0x80:
                    p += 1
                d += 2
            if not c & 0x80:
                p += 1
    return out, src


def pclass(port):
    return (port >> 7 & 1) << 2 | (port >> 6 & 1) << 1 | (port & 1)


out, src = unpack(cart)
want = {}
for line in list(open(sys.argv[2]))[1:]:
    f = line.split('\t')
    pc = int(f[0], 16)
    if pc < 0xC000:
        continue
    b0, b1 = out[pc], out[pc + 1]
    if b0 == 0xD3:
        op = pclass(b1)
    elif b0 == 0xED and b1 in (0xA3, 0xAB):
        op = b1
    else:
        raise SystemExit(f'{pc:04X}: {b0:02X} {b1:02X} not handled')
    want[pc] = op
img = dict(out)
for pc, op in want.items():
    img[pc], img[pc + 1] = rst, op
rd = lambda a: img.get(a & 0xFFFF, 0xFF)  # noqa: E731
# Every site gets its trace op: runs of op bytes share one stream byte,
# and a trace op where no trace pays runs as a plain output.
ntr = 0
for pc, op in want.items():
    img[pc + 1] = tracedef.trace_op(op)
    ntr += tracedef.choose(rd, pc, rst)
# stream changes
chg = {}
for a in sorted(img):
    if img[a] != out[a]:
        s = src[a]
        if chg.get(s, img[a]) != img[a]:
            raise SystemExit(f'stream byte {s:05X}: two values wanted')
        chg[s] = img[a]
# every output byte made by a changed stream byte must want the new value
for a, s in src.items():
    if s in chg and img[a] != chg[s]:
        raise SystemExit(f'stream byte {s:05X} also makes {a:04X}, which must stay {out[a]:02X}')
print(f'# Fantasy Zone II unpacks its VRAM routines into RAM $CC00-$CF7A from the')
print(f'# packed stream at ROM $1B7D5 (routine $07A9). These pokes change the stream')
print(f'# so the unpacked code has RST io + op at its {len(want)} I/O instructions')
print(f'# (all trace ops; {ntr} start a run or loop). Made by fantasyzone2-ramcode.py, next to this file.')
for s in sorted(chg):
    print(f'poke {s:05X} {cart[s]:02X} {chg[s]:02X}')
