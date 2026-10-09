#!/usr/bin/env python3
"""Build a NextMasterSystem overlay file (.nms) from a spec and the cart.

usage: mknms.py SPEC CART OUTDIR [--compat CSV] [--titles CSV] [--sjasmplus PATH]

The output is OUTDIR/XXXXXXXX.nms, named after the cart's CRC32 in upper-case
hex. docs/nms-format.md describes the file. The cart is read to work out
its CRC32 and size, to find the instructions that each spec line names, and
to compute the CRC32 values of the CHECK operations. The file holds no bytes
copied from the cart: a CHECK holds a CRC32 of the original bytes, and a
PATCH holds only the bytes that differ from the cart.

--compat and --titles are the compatibility list and the title list (CSV,
see the meta repo's docs/compatibility.md). With them, the META chunk gets
the game's title, release details and status, found by the cart's CRC32.
Without a row for the cart, META holds the spec's name only.

--sjasmplus is the assembler for rastercode files and asm blocks (default: sjasmplus on
the PATH).

SPEC lines. # or ; starts a comment. ADDR is a cart offset in hex; in the
first 32K it is also the Z80 address.

  name TEXT          the game's name, used for META when the CSVs have none
  cart CRC32         the CRC32 of the cart the spec is for; the builder stops
                     if CART has another CRC32
  vector ADDR KIND   write JP <framework entry> at RST vector ADDR (hex)
                     KIND is one of out_n, in_n, ed, ld_de_a, outi_run, io.
                     Each site kind needs its vector. An io vector at $00
                     jumps to fw_io0, which also turns a game's JP $0000 (a
                     reset) into a jump to its start address.
  site ADDR          the I/O instruction at ADDR becomes RST + inline code
  mapper ADDR        the one-byte LD (DE),A at ADDR becomes the mapper RST
  mapst ADDR         LD ($FFFC-$FFFF),A (32 nn FF) -> RST io, $10 + register,
                     the third byte skipped by the framework
  mapld ADDR         LD HL,$FFFF; LD (HL),n (21 FF FF 36 n) -> RST io, $14,
                     n, two bytes skipped
  mapsthl ADDR       LD ($FFFC-$FFFE),HL (22 nn FF) -> RST io, $15 + nn-$FC,
                     the third byte skipped
  mapstbc ADDR       LD ($FFFC-$FFFE),BC (ED 43 nn FF) -> RST io, $20 + nn-$FC,
                     two bytes skipped
  mapstde ADDR       LD ($FFFC-$FFFE),DE (ED 53 nn FF) -> RST io, $24 + nn-$FC
  mapldk ADDR        LD HL,$FFFC+k; LD (HL),n (21 nn FF 36 n) -> RST io,
                     $28 + k, n, two bytes skipped
  codem ADDR         Codemasters mapper LD ($0000/$4000/$8000),A (32 00 nn)
                     -> RST io, $2C + slot, one byte skipped
  maphl ADDR         LD (HL),n with n < 16 where HL holds $FFFC-$FFFF
                     (36 n) -> RST io, $30 + n
  outi START END     unrolled OUTI block START..END-1 (END holds its RET):
                     each ED A3 becomes RST + the count of OUTIs left
  otir ADDR          OUTI followed by JR NZ,-2 or JP NZ,ADDR (a loop that
                     is OTIR): the OUTI becomes an OTIR site, the jump stays
  poke ADDR OLD NEW  replace hex bytes OLD with NEW at ADDR
  asm ADDR LEN       Z80 assembly instead of hex. The lines up to a line
  ...                "endasm" are assembled with sjasmplus, as if at the Z80
  endasm             address that cart offset ADDR runs at (the offset itself
                     in the first 32K, slot 2 at $8000 for other banks). The
                     code replaces the LEN cart bytes at ADDR: it must not be
                     longer, and the bytes it leaves are filled with NOP. The
                     cart supplies the CHECK. The LEN bytes stay inside one 8K
                     page of the cart. Example:
                         asm 00089 2        ; IM 1 -> IM 2
                             im 2
                         endasm
  label NAME ADDR    NAME is the game address that cart offset ADDR runs at,
                     for use in asm blocks (any asm block in the spec, before
                     or after this line)
  start ADDR [SP]    the game starts at ADDR instead of $0000, with SP
                     (default $DFF0)
  ramsite ADDR BB    an I/O instruction (bytes BB) that the game builds in
                     RAM at ADDR: the framework patches it when the ramhook
                     runs, if the RAM still holds those bytes
  ramhook ADDR       JP nn at ADDR, which the game runs after it builds its
                     RAM code: it becomes RST io, $2F, and the framework goes
                     on to nn
  rastercode FILE    the per-line horizontal scroll routine: sjasmplus
                     source, path relative to the spec, assembled at $3C00
                     for the framework's second page, at most 1024 bytes
  notrace            no trace forms (below) in this overlay
  plain ADDR         this output site keeps its plain inline code
  priority           CONF priority=1: priority tiles are drawn again in
                     Layer 2, above the sprites
  toppal             CONF toppal=1: the palette the frame handler leaves is
                     shown from line 0

Names that every asm block knows (the framework's jump table and the fixed
state at $E000-$E071, from src/runtime/fw.asm). Jump table entries:
jt_out_n $E000, jt_in_n $E003, jt_ed $E006, jt_ld_de_a $E009, jt_start $E00C,
jt_fatal $E00F, jt_outi_run $E012, jt_io $E015, jt_io0 $E018, fw_resume $E01B.
State: fw_status $E020, fw_crc $E021, fw_size $E025, fw_npages $E029,
fw_lastop $E02A, fw_frames $E02B, cur_mmu $E02D, vdp_latch $E035, vdp_code
$E036, vdp_addr $E037, vdp_rbuf $E039, vdp_status $E03A, vdp_regs $E03B,
nt_base $E04B, cram $E04D, fw_start_addr $E06D, fw_start_sp $E06F, isr_n $E071.
A label line may not reuse one of these names.

Site lines may also name LD I,A and LD A,I (ED 47, ED 57): the framework
keeps the game's I register, because it needs I for IM 2.

Trace forms (tools/tracedef.py): an output site (OUT (n),A, OUTI, OUTD,
OUT (C),r) that another patched output follows at once, or that a loop
jumps back over, gets the trace form of its inline code ($18 + class, $C3,
$CB, $81 + 8r), and the framework runs the whole run or loop in one call.

The framework ABI the file needs is worked out from what it uses: 1 without
an io vector, 2 with one, 3 with trace forms, fw_io0 or mapsthl, 4 with
RAMSITES, RASTER or the ABI 4 mapper lines, 5 with LD I,A, LD A,I or a CONF
switch.
"""
import argparse
import csv
import os
import re
import struct
import subprocess
import sys
import tempfile
import unicodedata
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracedef  # noqa: E402

RASTER_ORG, RASTER_MAX = 0x3C00, 0x400   # rast_code in src/runtime/fw2.asm
ENTRY = {'out_n': 0xE000, 'in_n': 0xE003, 'ed': 0xE006, 'ld_de_a': 0xE009, 'outi_run': 0xE012, 'io': 0xE015}
# Names every asm block can use. The addresses are fixed by src/runtime/fw.asm
# (the jump table, then "state that tools read from outside"). The jt_ names
# are the table entries; fw.asm's own fw_out_n and the like are the handlers.
ASM_NAMES = {
    'jt_out_n': 0xE000, 'jt_in_n': 0xE003, 'jt_ed': 0xE006, 'jt_ld_de_a': 0xE009,
    'jt_start': 0xE00C, 'jt_fatal': 0xE00F, 'jt_outi_run': 0xE012, 'jt_io': 0xE015,
    'jt_io0': 0xE018, 'fw_resume': 0xE01B,
    'fw_status': 0xE020, 'fw_crc': 0xE021, 'fw_size': 0xE025, 'fw_npages': 0xE029,
    'fw_lastop': 0xE02A, 'fw_frames': 0xE02B, 'cur_mmu': 0xE02D,
    'vdp_latch': 0xE035, 'vdp_code': 0xE036, 'vdp_addr': 0xE037, 'vdp_rbuf': 0xE039,
    'vdp_status': 0xE03A, 'vdp_regs': 0xE03B, 'nt_base': 0xE04B, 'cram': 0xE04D,
    'fw_start_addr': 0xE06D, 'fw_start_sp': 0xE06F, 'isr_n': 0xE071,
}
CHECK_GAP = 32       # patched ranges closer than this share one CHECK
CHECK_MAX = 0x1000   # longest CHECK range

ED_OK = {0xB3, 0xA3, 0xA2, 0xB2, 0xAB, 0xBB} | {0x41 + 8 * r for r in range(8) if r != 6} | {0x40 + 8 * r for r in range(8)}
ED_OK |= {0x47, 0x57}


def crc32(b):
    return zlib.crc32(bytes(b)) & 0xFFFFFFFF


def cpu(off):
    """CPU address of a cart offset: banks 0-1 as they are, others in slot 2."""
    return off if off < 0x8000 else 0x8000 | (off & 0x3FFF)


def strip_comment(line):
    return re.split('[#;]', line, 1)[0].strip()


def read_asm_block(it, spec, n):
    """The lines of an asm block that starts on spec line N, up to endasm."""
    body = []
    for _, raw in it:
        if strip_comment(raw) == 'endasm':
            return body
        body.append(raw.rstrip('\n'))
    raise SystemExit(f'{spec}:{n}: asm block has no endasm')


def spec_labels(spec):
    """The label lines of a spec: name -> Z80 address."""
    labels = {}
    it = enumerate(open(spec), 1)
    for n, raw in it:
        line = strip_comment(raw)
        w = line.split()
        if w[:1] == ['asm']:
            read_asm_block(it, spec, n)
        elif w[:1] == ['label']:
            if len(w) != 3 or not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', w[1]):
                raise SystemExit(f'{spec}:{n}: label NAME ADDR')
            if w[1] in ASM_NAMES or w[1] in labels:
                raise SystemExit(f'{spec}:{n}: label {w[1]} is already defined')
            labels[w[1]] = cpu(int(w[2], 16))
    return labels


def assemble_block(sjasmplus, spec, n, body, org, labels):
    """Assemble the asm block that starts on spec line N at Z80 address ORG."""
    names = dict(ASM_NAMES, **labels)
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, 'names.i'), 'w') as f:
            f.write(''.join(f'{k} equ 0x{v:04X}\n' for k, v in names.items()))
        with open(os.path.join(td, 'blk.asm'), 'w') as f:
            f.write(f' INCLUDE "names.i" : ORG 0x{org:04X}\n' + '\n'.join(body) + '\n')
        p = subprocess.run([sjasmplus, '--nologo', '--msg=war', '--raw=blk.bin', 'blk.asm'],
                           capture_output=True, text=True, cwd=td)
        if p.returncode or not os.path.exists(os.path.join(td, 'blk.bin')):
            text = re.sub(r'blk\.asm\((\d+)\)', lambda m: f'{spec}:{n + int(m.group(1)) - 1}', p.stdout + p.stderr)
            raise SystemExit(f'{spec}:{n}: asm block failed\n{text.strip()}')
        return open(os.path.join(td, 'blk.bin'), 'rb').read()


def pclass(p):
    return (p >> 7 & 1) << 2 | (p >> 6 & 1) << 1 | (p & 1)


def ramsite_candidates(code):
    """The instructions a RAMSITES entry with inline code CODE can replace."""
    if code < 8:
        return [bytes([0xD3, p]) for p in range(256) if pclass(p) == code]
    if code < 16:
        return [bytes([0xDB, p]) for p in range(256) if pclass(p) == code - 8]
    return [bytes([0xED, code])]


QUOTES = str.maketrans({'\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"', '\u2013': '-', '\u2014': '-'})


def ascii_text(s):
    s = unicodedata.normalize('NFKC', s).translate(QUOTES)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    return ' '.join(s.split())


def chunk(tag, data):
    return tag.encode('ascii') + struct.pack('<I', len(data)) + data


def parse(spec, cart, sjasmplus):
    """Run the spec over the cart. Returns a dict of what the file needs."""
    r = dict(name='', crc=None, ops=[], start=None, rcode=None, ramsites=[], ramcont=None,
             priority=False, toppal=False, abi=1)
    rst = {}
    outs = {}
    notrace, plain, io0, abi4, abi5 = False, set(), False, False, False
    ops = r['ops']

    def patch(addr, new):
        ops.append((addr, bytes(new)))

    labels = spec_labels(spec)
    it = enumerate(open(spec), 1)
    for lineno, raw in it:
        line = strip_comment(raw)
        if not line:
            continue
        word, rest = (line.split(None, 1) + [''])[:2]
        if word == 'label':
            pass
        elif word == 'asm':
            w = rest.split()
            body = read_asm_block(it, spec, lineno)
            if len(w) != 2:
                raise SystemExit(f'{spec}:{lineno}: asm ADDR LEN')
            a, n = int(w[0], 16), int(w[1])
            if n < 1 or a + n > len(cart):
                raise SystemExit(f'{spec}:{lineno}: asm {a:05X} {n}: outside the cart')
            if a % 8192 + n > 8192:
                raise SystemExit(f'{spec}:{lineno}: asm {a:05X} {n}: crosses an 8K page of the cart')
            code = assemble_block(sjasmplus, spec, lineno, body, cpu(a), labels)
            if len(code) > n:
                raise SystemExit(f'{spec}:{lineno}: asm {a:05X}: the code is {len(code)} bytes, '
                                 f'more than the {n} it replaces')
            patch(a, code + b'\0' * (n - len(code)))
        elif word == 'name':
            r['name'] = rest
        elif word == 'cart':
            r['crc'] = int(rest, 16)
        elif word == 'vector':
            a, kind = rest.split()
            a = int(a, 16)
            if a % 8 or a > 0x30:
                raise SystemExit(f'bad RST vector {a:04X}')
            rst[kind] = 0xC7 + a
            e = ENTRY[kind]
            if kind == 'io' and a == 0:
                e = 0xE018
                io0 = True
            patch(a, [0xC3, e & 0xFF, e >> 8])
        elif word == 'rastercode':
            src = os.path.join(os.path.dirname(os.path.abspath(spec)), rest)
            with tempfile.TemporaryDirectory() as td:
                binf = os.path.join(td, 'raster.bin')
                p = subprocess.run([sjasmplus, '--nologo', '--msg=war', f'--raw={binf}', src],
                                   capture_output=True, text=True)
                if p.returncode or not os.path.exists(binf):
                    raise SystemExit(f'rastercode {rest}: {p.stdout}{p.stderr}')
                r['rcode'] = open(binf, 'rb').read()
            if len(r['rcode']) > RASTER_MAX:
                raise SystemExit(f'rastercode {rest}: {len(r["rcode"])} bytes, more than {RASTER_MAX}')
        elif word == 'ramsite':
            w = rest.split()
            a, old = int(w[0], 16), bytes.fromhex(w[1])
            if len(old) != 2:
                raise SystemExit(f'ramsite {w[0]}: give the two instruction bytes')
            b0, b1 = old
            if b0 == 0xD3:
                op = pclass(b1)
            elif b0 == 0xDB:
                op = 8 + pclass(b1)
            elif b0 == 0xED and b1 in ED_OK:
                op = b1
            else:
                raise SystemExit(f'ramsite {w[0]}: {old.hex()} is not a supported I/O instruction')
            r['ramsites'].append((a, old, bytes([rst['io'], op])))
        elif word == 'ramhook':
            a = int(rest, 16)
            if cart[a] != 0xC3:
                raise SystemExit(f'ramhook {a:05X}: {cart[a]:02X} is not JP nn')
            r['ramcont'] = cart[a + 1] | cart[a + 2] << 8
            patch(a, [rst['io'], 0x2F, 0])
            abi4 = True
        elif word == 'notrace':
            notrace = True
        elif word == 'priority':
            r['priority'] = True
        elif word == 'toppal':
            r['toppal'] = True
        elif word == 'plain':
            plain.add(int(rest, 16))
        elif word == 'start':
            w = rest.split()
            r['start'] = (int(w[0], 16), int(w[1], 16) if len(w) > 1 else 0)
        elif word in ('site', 'otir'):
            a = int(rest, 16)
            b0, b1 = cart[a], cart[a + 1]
            if word == 'otir':
                if cart[a:a + 4] != b'\xed\xa3\x20\xfc' and cart[a:a + 5] != bytes([0xED, 0xA3, 0xC2, cpu(a) & 0xFF, cpu(a) >> 8]):
                    raise SystemExit(f'{a:04X}: not OUTI; JR NZ,-2 or OUTI; JP NZ,self')
                b1 = 0xB3
            if 'io' in rst:
                if b0 == 0xD3:
                    op = pclass(b1)
                elif b0 == 0xDB:
                    op = 8 + pclass(b1)
                elif b0 == 0xED and b1 in ED_OK:
                    op = b1
                    if b1 in (0x47, 0x57):
                        abi5 = True
                else:
                    raise SystemExit(f'{a:04X}: {b0:02X} {b1:02X} is not a supported I/O instruction')
                if tracedef.trace_op(op) is not None:
                    outs[a] = len(ops)
                patch(a, [rst['io'], op])
            elif b0 == 0xD3:
                patch(a, [rst['out_n'], b1])
            elif b0 == 0xDB:
                patch(a, [rst['in_n'], b1])
            elif b0 == 0xED and b1 in ED_OK:
                patch(a, [rst['ed'], b1])
            else:
                raise SystemExit(f'{a:04X}: {b0:02X} {b1:02X} is not a supported I/O instruction')
        elif word == 'mapper':
            a = int(rest, 16)
            if cart[a] != 0x12:
                raise SystemExit(f'{a:04X}: {cart[a]:02X} is not LD (DE),A')
            patch(a, [rst['ld_de_a']])
        elif word == 'mapst':
            a = int(rest, 16)
            if cart[a] != 0x32 or cart[a + 2] != 0xFF or cart[a + 1] < 0xFC:
                raise SystemExit(f'{a:05X}: {cart[a:a + 3].hex()} is not LD ($FFFC-$FFFF),A')
            patch(a, [rst['io'], 0x10 + cart[a + 1] - 0xFC, 0xFF])
        elif word == 'mapsthl':
            a = int(rest, 16)
            if cart[a] != 0x22 or cart[a + 2] != 0xFF or not 0xFC <= cart[a + 1] <= 0xFE:
                raise SystemExit(f'{a:05X}: {cart[a:a + 3].hex()} is not LD ($FFFC-$FFFE),HL')
            patch(a, [rst['io'], 0x15 + cart[a + 1] - 0xFC, 0xFF])
            io0 = True
        elif word in ('mapstbc', 'mapstde'):
            a = int(rest, 16)
            b1 = 0x43 if word == 'mapstbc' else 0x53
            if cart[a] != 0xED or cart[a + 1] != b1 or cart[a + 3] != 0xFF or not 0xFC <= cart[a + 2] <= 0xFE:
                raise SystemExit(f'{a:05X}: {cart[a:a + 4].hex()} is not LD ($FFFC-$FFFE),{word[-2:].upper()}')
            patch(a, [rst['io'], (0x20 if b1 == 0x43 else 0x24) + cart[a + 2] - 0xFC, 0, 0])
            abi4 = True
        elif word == 'mapldk':
            a = int(rest, 16)
            if cart[a] != 0x21 or cart[a + 2] != 0xFF or cart[a + 1] < 0xFC or cart[a + 3] != 0x36:
                raise SystemExit(f'{a:05X}: {cart[a:a + 5].hex()} is not LD HL,$FFFC-$FFFF; LD (HL),n')
            patch(a, [rst['io'], 0x28 + cart[a + 1] - 0xFC, cart[a + 4], 0, 0])
            abi4 = True
        elif word == 'codem':
            a = int(rest, 16)
            if cart[a] != 0x32 or cart[a + 1] != 0 or cart[a + 2] not in (0x00, 0x40, 0x80):
                raise SystemExit(f'{a:05X}: {cart[a:a + 3].hex()} is not LD ($0000/$4000/$8000),A')
            patch(a, [rst['io'], 0x2C + (cart[a + 2] >> 6), 0])
            abi4 = True
        elif word == 'maphl':
            a = int(rest, 16)
            if cart[a] != 0x36 or cart[a + 1] > 15:
                raise SystemExit(f'{a:05X}: {cart[a:a + 2].hex()} is not LD (HL),n with n < 16')
            patch(a, [rst['io'], 0x30 + cart[a + 1]])
            abi4 = True
        elif word == 'mapld':
            a = int(rest, 16)
            if cart[a:a + 4] != b'\x21\xff\xff\x36':
                raise SystemExit(f'{a:05X}: {cart[a:a + 5].hex()} is not LD HL,$FFFF; LD (HL),n')
            patch(a, [rst['io'], 0x14, cart[a + 4], 0, 0])
        elif word == 'outi':
            a, end = (int(x, 16) for x in rest.split())
            if cart[end] != 0xC9 or (end - a) % 2:
                raise SystemExit(f'outi {a:04X} {end:04X}: no RET at the end, or odd length')
            for p in range(a, end, 2):
                if cart[p:p + 2] != b'\xed\xa3':
                    raise SystemExit(f'{p:04X}: not OUTI')
                patch(p, [rst['outi_run'], (end - p) // 2])
        elif word == 'poke':
            a, old, new = rest.split()
            a, old, new = int(a, 16), bytes.fromhex(old), bytes.fromhex(new)
            if cart[a:a + len(old)] != old or len(old) != len(new):
                raise SystemExit(f'poke {a:04X}: cart has {cart[a:a + len(old)].hex()}')
            patch(a, new)
        else:
            raise SystemExit(f'unknown spec line: {line}')

    # trace forms: decided on the image with every patch in place
    ntrace = 0
    if 'io' in rst and not notrace:
        img = bytearray(cart)
        for addr, new in ops:
            img[addr:addr + len(new)] = new
        for off, i in sorted(outs.items()):
            if off in plain:
                continue
            base = cpu(off)

            def rd(x, off=off, base=base):
                x &= 0xFFFF
                if x >> 14 == base >> 14:
                    y = off - base + x
                elif x < 0x8000:
                    y = x
                else:
                    return 0xFF
                return img[y] if 0 <= y < len(img) else 0xFF
            if tracedef.choose(rd, base, rst['io']):
                addr, new = ops[i]
                ops[i] = (addr, bytes([new[0], tracedef.trace_op(new[1])]))
                ntrace += 1
    if r['ramsites']:
        if r['rcode'] is not None or r['ramcont'] is None or len(r['ramsites']) > 255:
            raise SystemExit('ramsite needs one ramhook, at most 255 sites, and no rastercode')
        if 3 + 6 * len(r['ramsites']) > RASTER_MAX:
            raise SystemExit('ramsite table too big for the framework')
    if 'io' in rst:
        r['abi'] = 4 if abi4 or r['rcode'] is not None else 3 if ntrace or io0 else 2
    if abi5 or r['priority'] or r['toppal']:
        r['abi'] = max(r['abi'], 5)
    r['ntrace'] = ntrace
    return r


def patch_runs(cart, ops):
    """PATCH operations: only the bytes that differ from the cart, each run
    inside one 8K page. Later operations win where two touch one byte."""
    want = {}
    for addr, new in ops:
        for k, b in enumerate(new):
            want[addr + k] = b
    runs = []
    for a in sorted(want):
        if want[a] == cart[a]:
            continue
        if runs and runs[-1][0] + len(runs[-1][1]) == a and a % 8192 and len(runs[-1][1]) < 255:
            runs[-1][1].append(want[a])
        else:
            runs.append((a, bytearray([want[a]])))
    return runs


def check_ranges(ops):
    """CHECK ranges: every byte an operation covers, near ranges merged."""
    spans = sorted((a, a + len(n)) for a, n in ops)
    out = []
    for s, e in spans:
        if out and s - out[-1][1] < CHECK_GAP and e - out[-1][0] <= CHECK_MAX:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


def load_meta(crc, name, compat, titles):
    meta = {}
    row = None
    if compat:
        for x in csv.DictReader(open(compat, newline='', encoding='utf-8')):
            if x['crc32'].upper() == f'{crc:08X}':
                row = x
                break
    trow = None
    if row and titles and row.get('id'):
        for x in csv.DictReader(open(titles, newline='', encoding='utf-8')):
            if x['id'] == row['id']:
                trow = x
                break
    meta['title'] = (trow or {}).get('title') or name
    if row:
        meta['id'] = row.get('id', '')
        meta['dump'] = row.get('nointro_name') or row.get('dump_name', '')
    if trow:
        for k in ('year', 'publisher', 'regions'):
            meta[k] = trow.get(k, '')
    if row:
        meta['status'] = row.get('status', '')
        meta['flags'] = row.get('flags', '')
        meta['issues'] = row.get('issues', '')
        meta['tested'] = ' '.join(x for x in (row.get('tested_on', ''), row.get('tested_date', '')) if x)
    return {k: ascii_text(v) for k, v in meta.items() if v and ascii_text(v)}


def build(spec, cart_path, outdir, compat=None, titles=None, sjasmplus='sjasmplus'):
    cart = open(cart_path, 'rb').read()
    if len(cart) % 16384 == 512:
        cart = cart[512:]
    crc = crc32(cart)
    r = parse(spec, cart, sjasmplus)
    if r['crc'] is not None and r['crc'] != crc:
        raise SystemExit(f'{spec}: made for cart {r["crc"]:08X}, this cart is {crc:08X}')

    ptch = b''
    checks = check_ranges(r['ops'])
    for s, e in checks:
        ptch += bytes([1]) + s.to_bytes(3, 'little') + struct.pack('<HI', e - s, crc32(cart[s:e]))
    runs = patch_runs(cart, r['ops'])
    for a, b in runs:
        if not any(s <= a and a + len(b) <= e for s, e in checks):
            raise SystemExit(f'PATCH at {a:05X} is outside every CHECK')
        ptch += bytes([2]) + a.to_bytes(3, 'little') + bytes([len(b)]) + bytes(b)
    if r['start'] is not None:
        ptch += bytes([3]) + struct.pack('<HH', *r['start'])
    if r['ramsites']:
        ptch += bytes([4]) + struct.pack('<HB', r['ramcont'], len(r['ramsites']))
        for a, old, new in r['ramsites']:
            c16 = crc32(old) & 0xFFFF
            hits = [o for o in ramsite_candidates(new[1]) if crc32(o) & 0xFFFF == c16]
            if hits != [old]:
                raise SystemExit(f'ramsite {a:04X}: the CRC does not pick out {old.hex()} alone')
            ptch += struct.pack('<HBH', a, len(old), c16) + new
    if r['rcode'] is not None:
        ptch += bytes([5]) + struct.pack('<H', len(r['rcode'])) + r['rcode']
    ptch += b'\0'

    conf = f'priority={int(r["priority"])}\ntoppal={int(r["toppal"])}\n'.encode('ascii')
    meta = load_meta(crc, r['name'], compat, titles)
    metab = ''.join(f'{k}={v}\n' for k, v in meta.items()).encode('ascii')

    body = b'NMS\x1a' + bytes([1, 0, r['abi'], 0]) + struct.pack('<II', crc, len(cart))
    body += chunk('CRCS', struct.pack('<I', crc))
    body += chunk('PTCH', ptch)
    body += chunk('CONF', conf)
    body += chunk('META', metab)
    body += chunk('END ', struct.pack('<I', crc32(body)))
    out = os.path.join(outdir, f'{crc:08X}.nms')
    open(out, 'wb').write(body)
    print(f'{out}: {meta.get("title", "")}, CRC32 {crc:08X}, {len(cart)} bytes, ABI {r["abi"]}, '
          f'{len(checks)} checks, {len(runs)} patches ({r["ntrace"]} trace sites), {len(body)} bytes')
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('spec')
    ap.add_argument('cart')
    ap.add_argument('outdir')
    ap.add_argument('--compat', help='compatibility list CSV')
    ap.add_argument('--titles', help='title list CSV')
    ap.add_argument('--sjasmplus', default='sjasmplus', help='assembler for rastercode files and asm blocks')
    a = ap.parse_args()
    build(a.spec, a.cart, a.outdir, a.compat, a.titles, a.sjasmplus)


if __name__ == '__main__':
    main()
