#!/usr/bin/env python3
"""Draft an overlay spec for a cart from sitescan.py output.

usage: mkspec.py CART.sms SCANDIR NAME "Game name" > NAME.spec

SCANDIR holds NAME.sites.tsv and NAME.dis.txt from sitescan.py. mknms.py
describes the spec lines; docs/overlays.md describes the workflow. The draft:
- writes every address as a ROM file offset (the cart copy is patched
  bank by bank, so code in any bank gets its patch);
- picks the io vector: the first of $08-$30 that no RST site uses, whose
  three bytes no scanned code covers and are $FF filler (games keep
  data there too); otherwise $00, when the cart starts with DI; IM 1 (the
  game then starts at $0003), DI; LD SP,nn (starts at $0004 with that SP),
  IM 1; LD SP,nn (starts at $0005 with that SP) or JP nn (starts at nn);
- changes every IM 1 in scanned code to IM 2 (not the one at $0001 when
  the vector is $00);
- lists every high and medium confidence I/O site; OUTI followed by
  JR NZ,-2 becomes an otir line;
- turns mapper stores LD ($FFFC-$FFFF),A into mapst lines,
  LD HL,$FFFF; LD (HL),n into mapld lines, LD ($FFFC-$FFFE),HL into
  mapsthl lines, LD ($FFFC-$FFFE),BC or DE into mapstbc or mapstde lines,
  LD HL,$FFFC-$FFFE; LD (HL),n into mapldk lines and other LD (HL),n
  stores with n < 16 into maphl lines, Codemasters LD ($0000/$4000/
  $8000),A into codem lines;
- turns high confidence mapper stores from the byte scan (kind
  mapper_unreached) into spec lines of the form sitescan names, and lists
  the medium and low ones as CHECK comments;
- lists low confidence I/O byte patterns as comments, to be checked by hand.
- writes the cart line: the CRC32 of the cart, without a copier header;
Everything it could not decide is a comment starting with "CHECK".
"""
import sys
import zlib

cart_path, scandir, name, title = sys.argv[1:5]
cart = open(cart_path, 'rb').read()
if len(cart) % 16384 == 512:
    cart = cart[512:]
rows = [l.rstrip('\n').split('\t') for l in open(f'{scandir}/{name}.sites.tsv')][1:]
code = set()
im1 = []
for l in open(f'{scandir}/{name}.dis.txt'):
    f = l.split()
    if len(f) < 4 or not f[0].startswith('$'):
        continue
    try:
        addr = int(f[0][1:], 16)
    except ValueError:
        continue
    nb = 0
    for t in f[3:]:
        if len(t) == 2 and all(c in '0123456789ABCDEF' for c in t):
            nb += 1
        else:
            break
    for k in range(nb):
        code.add(addr + k)
    if f[3:5] == ['ED', '56']:
        im1.append(addr)

def cpu(off):
    """CPU address of a ROM offset: banks 0-1 as they are, others in slot 2."""
    return off if off < 0x8000 else 0x8000 | (off & 0x3FFF)


used = set()
for r in rows:
    if r[5] == 'rst_vector':
        used.add(int(r[0][1:], 16))
vec = None
for v in range(8, 0x38, 8):
    if v not in used and not any(a in code for a in range(v, v + 3)) \
            and cart[v:v + 3] == b'\xff\xff\xff':
        vec = v
        break
out = [f'# {title}, drafted by tools/mkspec.py from sitescan output.', f'name {title}',
       f'cart {zlib.crc32(cart) & 0xFFFFFFFF:08X}']
start = None
if vec is None:
    if cart[0:3] == b'\xf3\xed\x56':
        vec, start = 0, '0003'
        out.append('# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,')
        out.append('# the game starts at $0003 (the framework does DI and IM 2).')
    elif cart[0:2] == b'\xf3\x31':
        vec, start = 0, f'0004 {cart[2] | cart[3] << 8:04X}'
        out.append('# No free RST vector: $0000-$0002 (DI; LD SP part) becomes the vector,')
        out.append('# the game starts at $0004 with the SP its LD SP,nn set.')
    elif cart[0:3] == b'\xed\x56\x31':
        vec, start = 0, f'0005 {cart[3] | cart[4] << 8:04X}'
        out.append('# No free RST vector: $0000-$0002 (IM 1; LD SP part) becomes the vector,')
        out.append('# the game starts at $0005 with the SP its LD SP,nn set.')
    elif cart[0] == 0xC3:
        vec, start = 0, f'{cart[1] | cart[2] << 8:04X}'
        out.append('# No free RST vector: the JP at $0000 becomes the vector, the game')
        out.append('# starts at its target.')
    else:
        out.append('# CHECK: no free RST vector and the cart does not start with DI; IM 1')
        vec = 0
out.append(f'vector {vec:02X} io')
if start is not None:
    out.append(f'start {start}')
for a in im1:
    if (start == '0003' and a == 1) or (start is not None and start.startswith('0005') and a == 0):
        continue
    out.append(f'poke {a:05X} ED56 ED5E')
seen = set()
bytescan_head = False
for r in rows:
    addr, kind, conf = r[0], r[5], r[8]
    if not addr.startswith('$') or len(addr) != 5:
        continue
    a = int(r[2][1:], 16)
    if kind == 'mapper' and r[3].startswith('32 ') and r[3].endswith(' FF') and int(r[3][3:5], 16) >= 0xFC:
        if a not in seen:
            seen.add(a)
            out.append(f'mapst {a:05X}')
        continue
    if kind == 'mapper' and r[3].startswith('22 ') and r[3].endswith(' FF') and 0xFC <= int(r[3][3:5], 16) <= 0xFE:
        if a not in seen:
            seen.add(a)
            out.append(f'mapsthl {a:05X}')
        continue
    if kind == 'mapper' and r[3].startswith('ED ') and r[3][3:5] in ('43', '53') and r[3].endswith(' FF'):
        if a not in seen:
            seen.add(a)
            out.append(f"{'mapstbc' if r[3][3:5] == '43' else 'mapstde'} {a:05X}")
        continue
    if kind == 'mapper' and r[3].startswith('36 ') and cart[a - 3] == 0x21 and cart[a - 1] == 0xFF and cart[a - 2] >= 0xFC and cart[a - 2] != 0xFF:
        if a not in seen:
            seen.add(a)
            out.append(f'mapldk {a - 3:05X}   # LD HL,$FF{cart[a - 2]:02X}; {r[4]}')
        continue
    if kind == 'mapper' and r[3].startswith('36 ') and cart[a - 3:a] == b'\x21\xff\xff':
        if a not in seen:
            seen.add(a)
            out.append(f'mapld {a - 3:05X}   # LD HL,$FFFF; {r[4]}')
        continue
    if kind == 'mapper' and r[3].startswith('36 ') and cart[a + 1] < 16:
        if a not in seen:
            seen.add(a)
            out.append(f'maphl {a:05X}   # {r[4]}, HL = {r[6].split("<-")[0]}')
        continue
    if kind == 'codem_store' and r[3].startswith('32 00 ') and r[3][6:8] in ('00', '40', '80'):
        if a not in seen:
            seen.add(a)
            out.append(f'codem {a:05X}')
        continue
    if kind in ('out', 'in', 'out_c', 'in_c', 'block_out', 'block_in') and conf in ('high', 'medium'):
        if a in seen:
            continue
        seen.add(a)
        if cart[a:a + 4] == b'\xed\xa3\x20\xfc' or cart[a:a + 5] == bytes([0xED, 0xA3, 0xC2, cpu(a) & 0xFF, cpu(a) >> 8]):
            out.append(f'otir {a:05X}')
        else:
            out.append(f'site {a:05X}')
    elif kind == 'mapper_unreached':
        if a in seen:
            continue
        seen.add(a)
        if not bytescan_head:
            bytescan_head = True
            out.append('# Mapper stores found by the byte scan in bytes no path reached:')
        line = f'{r[6]} {a:05X}'
        if conf == 'high':
            out.append(f'{line}   # {r[4]}; {r[10]}')
        else:
            out.append(f'# CHECK byte scan {conf}: {line}  {r[4]}  ({r[10]})')
    elif kind == 'io_unreached' and conf == 'low':
        out.append(f'# CHECK low: site {a:05X}  {r[4]}  ({r[7]})')
    elif kind in ('mapper', 'ram_exec', 'indirect_unresolved', 'bank_unresolved', 'cartarea_store'):
        out.append(f'# CHECK {kind} at {a:05X} ({r[0]} bank {r[1]}): {r[3]}  {r[4]} {r[6]}')
print('\n'.join(out))
