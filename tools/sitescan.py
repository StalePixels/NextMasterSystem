#!/usr/bin/env python3
"""sitescan: static patch-site scanner for Sega Master System carts.

A recursive-descent Z80 disassembler that lists every site a NextMasterSystem
overlay has to patch: I/O instructions, stores to the mapper registers,
Codemasters mapper stores, RST use, code copied to RAM. docs/sitescan.md
describes the method, the output files and the limits.

usage: sitescan.py CART [options]       (run with python3 -I)
"""
import argparse
import heapq
import json
import os
import sys
import zlib

# ------------------------------------------------------------------ decoder

R8 = ['B', 'C', 'D', 'E', 'H', 'L', '(HL)', 'A']
RP = ['BC', 'DE', 'HL', 'SP']
RP2 = ['BC', 'DE', 'HL', 'AF']
CC = ['NZ', 'Z', 'NC', 'C', 'PO', 'PE', 'P', 'M']
ALU = ['ADD', 'ADC', 'SUB', 'SBC', 'AND', 'XOR', 'OR', 'CP']
ALU_TXT = ['ADD A,', 'ADC A,', 'SUB ', 'SBC A,', 'AND ', 'XOR ', 'OR ', 'CP ']
ROT = ['RLC', 'RRC', 'RL', 'RR', 'SLA', 'SRA', 'SLL', 'SRL']
ACC = ['RLCA', 'RRCA', 'RLA', 'RRA', 'DAA', 'CPL', 'SCF', 'CCF']
BLOCK = [['LDI', 'CPI', 'INI', 'OUTI'], ['LDD', 'CPD', 'IND', 'OUTD'],
         ['LDIR', 'CPIR', 'INIR', 'OTIR'], ['LDDR', 'CPDR', 'INDR', 'OTDR']]
BLOCK_IN = {'INI', 'IND', 'INIR', 'INDR'}
BLOCK_OUT = {'OUTI', 'OUTD', 'OTIR', 'OTDR'}
BLOCK_LD = {'LDI', 'LDD', 'LDIR', 'LDDR'}


def s8(v):
    return v - 256 if v & 0x80 else v


def h2(v):
    return '$%02X' % v


def h4(v):
    return '$%04X' % v


class Insn:
    __slots__ = ('addr', 'raw', 'text', 'sem')

    def __init__(self, addr, raw, text, sem):
        self.addr, self.raw, self.text, self.sem = addr, raw, text, sem

    def hexbytes(self):
        return ' '.join('%02X' % b for b in self.raw)


class _Short(Exception):
    pass


def decode(fetch, pc):
    """Decode one instruction. fetch(i) gives the byte at pc+i or None."""
    raw = []

    def nb():
        v = fetch(len(raw))
        if v is None:
            raise _Short()
        raw.append(v)
        return v
    try:
        return _decode(nb, pc, raw)
    except _Short:
        return None


def _memtxt(p, d):
    if p in ('IX', 'IY'):
        return '(%s%s$%02X)' % (p, '-' if d < 0 else '+', abs(d))
    return '(%s)' % p


def _decode(nb, pc, raw):
    def mk(text, sem):
        return Insn(pc, list(raw), text, sem)

    def bad():
        return mk('?? ' + ' '.join('%02X' % b for b in raw), ('bad',))

    op = nb()
    idx = None
    if op in (0xDD, 0xFD):
        idx = 'IX' if op == 0xDD else 'IY'
        op = nb()
        if op in (0xDD, 0xFD, 0xED):
            return bad()

    if op == 0xCB:
        if idx:
            d = s8(nb())
            op2 = nb()
            x, y, z = op2 >> 6, (op2 >> 3) & 7, op2 & 7
            o, ot = ('mem', idx, d), _memtxt(idx, d)
            copy = R8[z] if (z != 6 and x != 1) else None
        else:
            op2 = nb()
            x, y, z = op2 >> 6, (op2 >> 3) & 7, op2 & 7
            o, ot = (('mem', 'HL', 0), '(HL)') if z == 6 else (R8[z], R8[z])
            copy = None
        ctxt = (',' + copy) if copy else ''
        if x == 0:
            return mk('%s %s%s' % (ROT[y], ot, ctxt), ('cb', ROT[y], None, o, copy))
        name = ['', 'BIT', 'RES', 'SET'][x]
        return mk('%s %d,%s%s' % (name, y, ot, ctxt), ('cb', name, y, o, copy))

    if op == 0xED:
        op2 = nb()
        x, y, z = op2 >> 6, (op2 >> 3) & 7, op2 & 7
        p, q = y >> 1, y & 1
        if x == 1:
            if z == 0:
                if y == 6:
                    return mk('IN (C)', ('inC', None))
                return mk('IN %s,(C)' % R8[y], ('inC', R8[y]))
            if z == 1:
                if y == 6:
                    return mk('OUT (C),0', ('outC', ('imm', 0)))
                return mk('OUT (C),%s' % R8[y], ('outC', R8[y]))
            if z == 2:
                return mk('%s HL,%s' % ('SBC' if q == 0 else 'ADC', RP[p]), ('adc16', 'HL', RP[p]))
            if z == 3:
                nn = nb() | (nb() << 8)
                if q == 0:
                    return mk('LD (%s),%s' % (h4(nn), RP[p]), ('st16', nn, RP[p]))
                return mk('LD %s,(%s)' % (RP[p], h4(nn)), ('ld16', RP[p], ('abs', nn)))
            if z == 4:
                return mk('NEG', ('acc', 'NEG'))
            if z == 5:
                return mk('RETI' if y == 1 else 'RETN', ('reti',))
            if z == 6:
                return mk('IM %d' % [0, 0, 1, 2, 0, 0, 1, 2][y], ('nop',))
            if y == 0:
                return mk('LD I,A', ('nop',))
            if y == 1:
                return mk('LD R,A', ('nop',))
            if y in (2, 3):
                return mk('LD A,%s' % ('I' if y == 2 else 'R'), ('acc', 'LDAI'))
            if y in (4, 5):
                return mk('RRD' if y == 4 else 'RLD', ('rxd',))
            return bad()
        if x == 2 and z <= 3 and y >= 4:
            name = BLOCK[y - 4][z]
            return mk(name, ('block', name))
        return bad()

    x, y, z = op >> 6, (op >> 3) & 7, op & 7
    p, q = y >> 1, y & 1
    used = [False]

    def r(i, plain=False):
        if i == 6:
            if idx:
                used[0] = True
                d = s8(nb())
                return ('mem', idx, d), _memtxt(idx, d)
            return ('mem', 'HL', 0), '(HL)'
        if idx and not plain and i in (4, 5):
            used[0] = True
            n = idx + ('H' if i == 4 else 'L')
            return n, n
        return R8[i], R8[i]

    def rp(i, table=RP):
        if i == 2 and idx:
            used[0] = True
            return idx
        return table[i]

    def n8():
        return nb()

    def n16():
        return nb() | (nb() << 8)

    res = None
    if x == 0:
        if z == 0:
            if y == 0:
                res = mk('NOP', ('nop',))
            elif y == 1:
                res = mk("EX AF,AF'", ('exaf',))
            else:
                d = s8(nb())
                t = (pc + len(raw) + d) & 0xFFFF
                if y == 2:
                    res = mk('DJNZ %s' % h4(t), ('djnz', t))
                elif y == 3:
                    res = mk('JR %s' % h4(t), ('jr', t, None))
                else:
                    res = mk('JR %s,%s' % (CC[y - 4], h4(t)), ('jr', t, CC[y - 4]))
        elif z == 1:
            if q == 0:
                dst = rp(p)
                nn = n16()
                res = mk('LD %s,%s' % (dst, h4(nn)), ('ld16', dst, ('imm', nn)))
            else:
                dst, src = rp(2), rp(p)
                res = mk('ADD %s,%s' % (dst, src), ('add16', dst, src))
        elif z == 2:
            if q == 0:
                if p == 0:
                    res = mk('LD (BC),A', ('ld8', ('mem', 'BC', 0), 'A'))
                elif p == 1:
                    res = mk('LD (DE),A', ('ld8', ('mem', 'DE', 0), 'A'))
                elif p == 2:
                    src = rp(2)
                    nn = n16()
                    res = mk('LD (%s),%s' % (h4(nn), src), ('st16', nn, src))
                else:
                    nn = n16()
                    res = mk('LD (%s),A' % h4(nn), ('ld8', ('abs', nn), 'A'))
            else:
                if p == 0:
                    res = mk('LD A,(BC)', ('ld8', 'A', ('mem', 'BC', 0)))
                elif p == 1:
                    res = mk('LD A,(DE)', ('ld8', 'A', ('mem', 'DE', 0)))
                elif p == 2:
                    dst = rp(2)
                    nn = n16()
                    res = mk('LD %s,(%s)' % (dst, h4(nn)), ('ld16', dst, ('abs', nn)))
                else:
                    nn = n16()
                    res = mk('LD A,(%s)' % h4(nn), ('ld8', 'A', ('abs', nn)))
        elif z == 3:
            reg = rp(p)
            res = mk('%s %s' % ('INC' if q == 0 else 'DEC', reg), ('inc16' if q == 0 else 'dec16', reg))
        elif z in (4, 5):
            o, ot = r(y)
            res = mk('%s %s' % ('INC' if z == 4 else 'DEC', ot), ('inc8' if z == 4 else 'dec8', o))
        elif z == 6:
            o, ot = r(y)
            n = n8()
            res = mk('LD %s,%s' % (ot, h2(n)), ('ld8', o, ('imm', n)))
        else:
            res = mk(ACC[y], ('acc', ACC[y]))
    elif x == 1:
        if y == 6 and z == 6:
            res = mk('HALT', ('halt',))
        else:
            plain = (y == 6 or z == 6)
            d_, dt = r(y, plain)
            s_, st = r(z, plain)
            res = mk('LD %s,%s' % (dt, st), ('ld8', d_, s_))
    elif x == 2:
        o, ot = r(z)
        res = mk(ALU_TXT[y] + ot, ('alu', ALU[y], o))
    else:
        if z == 0:
            res = mk('RET %s' % CC[y], ('ret', CC[y]))
        elif z == 1:
            if q == 0:
                reg = rp(p, RP2)
                res = mk('POP %s' % reg, ('pop', reg))
            elif p == 0:
                res = mk('RET', ('ret', None))
            elif p == 1:
                res = mk('EXX', ('exx',))
            elif p == 2:
                reg = rp(2)
                res = mk('JP (%s)' % reg, ('jpind', reg))
            else:
                reg = rp(2)
                res = mk('LD SP,%s' % reg, ('ld16', 'SP', reg))
        elif z == 2:
            nn = n16()
            res = mk('JP %s,%s' % (CC[y], h4(nn)), ('jp', nn, CC[y]))
        elif z == 3:
            if y == 0:
                nn = n16()
                res = mk('JP %s' % h4(nn), ('jp', nn, None))
            elif y == 2:
                n = n8()
                res = mk('OUT (%s),A' % h2(n), ('outn', n))
            elif y == 3:
                n = n8()
                res = mk('IN A,(%s)' % h2(n), ('inn', n))
            elif y == 4:
                reg = rp(2)
                res = mk('EX (SP),%s' % reg, ('exsp', reg))
            elif y == 5:
                res = mk('EX DE,HL', ('exde',))
            elif y == 6:
                res = mk('DI', ('nop',))
            elif y == 7:
                res = mk('EI', ('nop',))
        elif z == 4:
            nn = n16()
            res = mk('CALL %s,%s' % (CC[y], h4(nn)), ('call', nn, CC[y]))
        elif z == 5:
            if q == 0:
                reg = rp(p, RP2)
                res = mk('PUSH %s' % reg, ('push', reg))
            else:
                nn = n16()
                res = mk('CALL %s' % h4(nn), ('call', nn, None))
        elif z == 6:
            n = n8()
            res = mk(ALU_TXT[y] + h2(n), ('alu', ALU[y], ('imm', n)))
        else:
            res = mk('RST %s' % h2(y * 8), ('rst', y * 8))
    if idx and not used[0]:
        return bad()
    return res


# ------------------------------------------------------------ abstract values
#
# A register holds an int, None (unknown) or a symbol:
#   ('arg', R)        the value R had when the current routine was entered
#   ('hi', X) ('lo', X)  a half of the 16-bit symbol X
#   ('tb', B)         a byte read from a table based at B
# 16-bit symbols:
#   ('off', B, k)     base B plus the constant k
#   ('idx', B)        base B plus an unknown index
#   ('idx', K, span)  int base K plus an index known to be 0..span
#   ('word', B)       a word read from a table based at B
# Bases B: an int, 'RET' (the routine's return address) or ('argpair', P).

REG8 = ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'IXH', 'IXL', 'IYH', 'IYL',
        "A'", "B'", "C'", "D'", "E'", "H'", "L'", 'F']
STATE_KEYS = REG8 + ['bank1', 'bank2']
PAIRS = {'BC': ('B', 'C'), 'DE': ('D', 'E'), 'HL': ('H', 'L'), 'IX': ('IXH', 'IXL'), 'IY': ('IYH', 'IYL')}
ARGPAIR = {v: k for k, v in PAIRS.items()}
RET0 = ('off', 'RET', 0)


def halves(v):
    if v is None:
        return (None, None)
    if isinstance(v, int):
        return (v >> 8, v & 0xFF)
    return (('hi', v), ('lo', v))


def combine(h, lo):
    if isinstance(h, int) and isinstance(lo, int):
        return (h << 8) | lo
    if isinstance(h, tuple) and isinstance(lo, tuple):
        if h[0] == 'hi' and lo[0] == 'lo' and h[1] == lo[1]:
            return h[1]
        if h[0] == 'tb' and lo[0] == 'tb' and (h[1] == lo[1] if not isinstance(lo[1], int)
                                               else h[1] == (lo[1] + 1) & 0xFFFF):
            return ('word', lo[1])
        if h[0] == 'sarg' and lo[0] == 'sarg' and h[1] == lo[1] + 1:
            return ('sargw', lo[1])
        if h[0] == 'mb' and lo[0] == 'mb' and h[1] == lo[1] and h[2] == lo[2] + 1:
            return ('mword', lo[1], lo[2])
        if h[0] == 'arg' and lo[0] == 'arg':
            pr = ARGPAIR.get((h[1], lo[1]))
            if pr:
                return ('off', ('argpair', pr), 0)
    return None


# The stack is a tuple of bytes, bottom (highest address) first. At routine entry it holds the
# return address: (high byte at SP0+1, low byte at SP0), where SP0 is SP on entry. 'sbase' counts
# bytes popped above that bottom, which are the caller's stack arguments ('sarg', j) at SP0+2+j.

def sp_off(s):
    return s['sbase'] + 2 - len(s['stack'])


def pop_byte(s):
    st = s['stack']
    if st is None:
        return None
    if st:
        s['stack'] = st[:-1]
        return st[-1]
    v = ('sarg', s['sbase'])
    s['sbase'] += 1
    return v


def push_byte(s, v):
    st = s['stack']
    if st is not None:
        st = st + (v,)
        s['stack'] = st if len(st) <= 96 else None


def pop_word(s):
    lo = pop_byte(s)
    hi = pop_byte(s)
    return hi, lo


def pget(s, p):
    if p == 'SP':
        return None if s['stack'] is None else ('sp', sp_off(s))
    if p == 'AF':
        return None
    hi, lo = PAIRS[p]
    return combine(s[hi], s[lo])


def pset(s, p, v):
    if p == 'SP':
        # LD SP,IX after IX = SP + k (an SDCC epilogue): the stack position is known again.
        # Slots between the return address and the new SP are unknown; the return address is kept.
        st = s['stack']
        if isinstance(v, tuple) and v[0] == 'sp':
            off = v[1]
            if st is not None:
                n = s['sbase'] + 2 - off
                if n >= 0:
                    s['stack'] = st[:n] + (None,) * max(0, n - len(st))
                else:
                    s['stack'] = ()
                    s['sbase'] = off - 2
                return
            if off <= 0:
                s['stack'] = halves(RET0) + (None,) * (-off)
                s['sbase'] = 0
                return
        s['stack'] = None
        return
    hi, lo = PAIRS[p]
    s[hi], s[lo] = halves(v)


def is_addr_sym(v):
    return isinstance(v, tuple) and v[0] in ('off', 'idx')


def add_const(v, d):
    if d == 0:
        return v
    if isinstance(v, int):
        return (v + d) & 0xFFFF
    if isinstance(v, tuple):
        if v[0] == 'off':
            return ('off', v[1], v[2] + d)
        if v[0] == 'sp':
            return ('sp', ((v[1] + d + 0x8000) & 0xFFFF) - 0x8000)
        if v[0] == 'idx':
            return ('idx', (v[1] + d) & 0xFFFF) + v[2:] if isinstance(v[1], int) else v
    return None


def add_bounded(a, off, span):
    """a + off + (0..span): the high byte of the index is known, the low byte is not."""
    if isinstance(a, int):
        return ('idx', (a + off) & 0xFFFF, span)
    if isinstance(a, tuple) and a[0] == 'idx' and isinstance(a[1], int):
        if len(a) == 3:
            return ('idx', (a[1] + off) & 0xFFFF, a[2] + span)
        return ('idx', (a[1] + off) & 0xFFFF)
    return add16(a, None)


def add16(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a + b) & 0xFFFF
    for x, y in ((a, b), (b, a)):
        if isinstance(x, tuple) and x[0] == 'sp':
            return add_const(x, y) if isinstance(y, int) else None
    if isinstance(b, int):
        a, b = b, a
    if isinstance(a, int):
        if is_addr_sym(b):
            return add_const(b, a)
        return ('idx', a)
    if is_addr_sym(a):
        return ('idx', a[1])
    if is_addr_sym(b):
        return ('idx', b[1])
    return None


HALF_OF = {}
for _p, (_h, _l) in PAIRS.items():
    HALF_OF[_h] = ('hi', _p)
    HALF_OF[_l] = ('lo', _p)


def as_half(v):
    """The caller's L as ('lo', caller's HL), and so on; other values unchanged."""
    if isinstance(v, tuple) and v[0] == 'arg' and v[1] in HALF_OF:
        side, p = HALF_OF[v[1]]
        return (side, ('off', ('argpair', p), 0))
    return v


def alu8(op, a, b, same):
    if same and op in ('SUB', 'XOR'):
        return 0
    if op == 'CP' or (same and op in ('AND', 'OR')):
        return a
    if op == 'AND' and b == 0:
        return 0
    if op == 'OR' and b == 0xFF:
        return 0xFF
    if isinstance(a, int) and isinstance(b, int):
        if op == 'ADD':
            return (a + b) & 0xFF
        if op == 'SUB':
            return (a - b) & 0xFF
        if op == 'AND':
            return a & b
        if op == 'OR':
            return a | b
        if op == 'XOR':
            return a ^ b
        return None
    # the 8-bit form of "HL = table + index": ADD A,L / LD L,A / ADC A,H / SUB L / LD H,A
    a, b = as_half(a), as_half(b)
    if op == 'ADD':
        for v in (a, b):
            if isinstance(v, tuple) and v[0] == 'lo' and is_addr_sym(v[1]):
                return ('lo', ('idx', v[1][1]))
    if op == 'ADC':
        for v in (a, b):
            if isinstance(v, tuple) and v[0] == 'hi' and is_addr_sym(v[1]):
                return ('hi', ('idx', v[1][1]))
    if op == 'SUB' and isinstance(a, tuple) and a[0] == 'hi' and isinstance(b, tuple) and b[0] == 'lo':
        return a
    return None


def stack_byte(s, o):
    """Byte at SP0 + o in state s (SP0 = SP at routine entry). ('sarg', j) above the return address."""
    st = s['stack']
    if st is not None:
        i = 1 + s['sbase'] - o
        if 0 <= i < len(st):
            return st[i]
    if o >= 2:
        return ('sarg', o - 2)
    return None


def caller_arg(cs, j, word=False):
    """The caller's view of the callee's stack argument byte j (or word at j), at the CALL."""
    if cs['stack'] is None:
        return None
    top = sp_off(cs)
    if word:
        return combine(stack_byte(cs, top + j + 1), stack_byte(cs, top + j))
    return stack_byte(cs, top + j)


def mentions_args(v):
    if not isinstance(v, tuple):
        return False
    if v[0] in ('arg', 'argpair', 'sarg', 'sargw'):
        return True
    return any(mentions_args(x) for x in v[1:])


def subst(v, cs):
    """Rewrite a callee's symbolic value in terms of the caller's state cs."""
    if v is None or isinstance(v, int):
        return v
    t = v[0]
    if t == 'arg':
        return cs[v[1]]
    if t == 'sarg':
        return caller_arg(cs, v[1])
    if t == 'sargw':
        return caller_arg(cs, v[1], True)
    if t in ('hi', 'lo'):
        x = subst(v[1], cs)
        if x is None:
            return None
        if isinstance(x, int):
            return (x >> 8) if t == 'hi' else (x & 0xFF)
        return (t, x)
    base = v[1]
    if not (isinstance(base, tuple) and base[0] == 'argpair'):
        return None
    b = pget(cs, base[1])
    if t == 'off':
        return add_const(b, v[2])
    if t == 'idx':
        if isinstance(b, int):
            return ('idx', b)
        return ('idx', b[1]) if is_addr_sym(b) else None
    if t == 'word':
        return ('word', b) if isinstance(b, int) else None
    if t == 'tb':
        return ('tb', ('fromint', b)) if isinstance(b, int) else None
    return None


def join_states(a, b):
    out = {}
    for k in STATE_KEYS:
        out[k] = a[k] if a[k] == b[k] else None
    sa, sb = a['stack'], b['stack']
    out['sbase'] = a['sbase']
    if sa is None or sb is None or len(sa) != len(sb) or a['sbase'] != b['sbase']:
        out['stack'] = None
        out['sbase'] = 0
    else:
        out['stack'] = tuple(x if x == y else None for x, y in zip(sa, sb))
    return out


def initial_state(bank1, bank2):
    s = {r: ('arg', r) for r in REG8}
    s['bank1'] = bank1
    s['bank2'] = bank2
    s['F'] = None           # F is only tracked when POP AF took half of a return address
    s['stack'] = halves(RET0)
    s['sbase'] = 0
    return s


def describe(v):
    if v is None:
        return 'unknown'
    if isinstance(v, int):
        return h4(v)
    t = v[0]
    if t == 'arg':
        return "caller's %s" % v[1]
    if t == 'sargw':
        return "caller's stack argument word %d" % (v[1] // 2)
    if t == 'sp':
        return 'stack frame (entry SP%+d)' % v[1]
    if t in ('off', 'idx', 'word'):
        b = v[1]
        if isinstance(b, int):
            bs = h4(b)
        elif b == 'RET':
            bs = 'return address'
        else:
            bs = "caller's %s" % b[1]
        if t == 'off':
            return '%s+%d' % (bs, v[2])
        if t == 'idx':
            return '%s+index' % bs
        return 'word from table at %s' % bs
    return str(v)


def port_class(port, d):
    if port is None:
        return 'unresolved'
    if d == 'in' and port in (0xF2,):
        return 'fm_detect'
    if d == 'out' and port in (0xF0, 0xF1, 0xF2):
        return ['fm_address', 'fm_data', 'fm_control'][port - 0xF0]
    hi, odd = port & 0xC0, port & 1
    if hi == 0x00:
        if d == 'out':
            return 'io_control' if odd else 'memory_control'
        return 'unmapped_read'
    if hi == 0x40:
        if d == 'out':
            return 'psg'
        return 'h_counter' if odd else 'v_counter'
    if hi == 0x80:
        if d == 'out':
            return 'vdp_control' if odd else 'vdp_data'
        return 'vdp_status' if odd else 'vdp_data'
    if d == 'out':
        return 'no_effect'
    return 'joypad_b_misc' if odd else 'joypad_a'


COMMON_PORTS = {0xBE, 0xBF, 0xBD, 0x7E, 0x7F, 0xDC, 0xDD, 0xC0, 0xC1, 0x3E, 0x3F, 0xF0, 0xF1, 0xF2}
MAPPER_LO, MAPPER_HI = 0xFFFC, 0xFFFF
CODEM_ADDRS = (0x0000, 0x4000, 0x8000)


# ------------------------------------------------------------------ routines

class Routine:
    def __init__(self, entry):
        self.entry = entry
        self.kinds = set()
        self.exits = []          # (kind, state)
        self.dispatch = None     # 'inline' or ('arg', pair)
        self.nodes = set()


class Summary:
    def __init__(self, returns=True, skip=0, out=None, dispatch=None):
        self.returns, self.skip, self.out, self.dispatch = returns, skip, out or {}, dispatch

    def key(self):
        return (self.returns, self.skip, tuple(sorted((k, repr(v)) for k, v in self.out.items())), repr(self.dispatch))


DEFAULT_SUMMARY = Summary()
UNKNOWN_ENTRY_KINDS = {'vector', 'cmdline', 'table', 'log', 'cdl', 'ram', 'harvest'}
STRONG_SEEDS = {'vector', 'cmdline'}
MAX_ROUNDS = 15


class Scanner:
    def __init__(self, rom, mapper='sega', unroll=8):
        self.unroll = unroll
        self.rom = rom
        self.size = len(rom)
        self.nb = max(1, (self.size + 0x3FFF) // 0x4000)
        self.mapper = mapper
        self.decode_cache = {}
        self.summ_prev = {}
        self.callers_prev = {}
        self.copies_prev = []
        self.code_starts_prev = set()
        self.harvest_src = {}
        self.struct_dispatch = set()
        self.slot1_banked_prev = False
        self.slot1_banked_cur = False
        self.bank_values = {1: set(), 2: set()}
        self.resolve_cache = {}

    # ---- memory

    def region_for(self, slot, bank):
        return ('rom', slot, bank % self.nb)

    def off_of(self, region, addr):
        """ROM file offset of the byte at cpu addr, seen from region."""
        if region[0] == 'ram':
            _, dest, length, src = region
            if dest <= addr < dest + length:
                off = src + addr - dest
                return off if 0 <= off < self.size else None
            return None
        slot = addr >> 14
        if slot == region[1]:
            bank = region[2]
        elif slot == 0:
            bank = 0
        elif slot == 1:
            bank = 1 % self.nb
        else:
            return None
        off = bank * 0x4000 + (addr & 0x3FFF)
        return off if off < self.size else None

    def cpu_off(self, addr, bank2, bank1=1):
        if addr >= 0xC000:
            return None
        slot = addr >> 14
        if slot == 0:
            off = addr
        elif slot == 1:
            if not isinstance(bank1, int):
                if self.slot1_banked_prev:
                    return None
                bank1 = 1
            off = (bank1 % self.nb) * 0x4000 + (addr & 0x3FFF)
        else:
            if not isinstance(bank2, int):
                return None
            off = (bank2 % self.nb) * 0x4000 + (addr & 0x3FFF)
        return off if off < self.size else None

    def decode_node(self, n):
        ins = self.decode_cache.get(n)
        if ins is None and n not in self.decode_cache:
            region, addr = n

            def fetch(i):
                o = self.off_of(region, (addr + i) & 0xFFFF)
                return None if o is None else self.rom[o]
            ins = decode(fetch, addr)
            self.decode_cache[n] = ins
        return ins

    def read8(self, a, s):
        if isinstance(a, int):
            off = self.cpu_off(a, s['bank2'], s['bank1'])
            return self.rom[off] if off is not None else None
        if is_addr_sym(a):
            return ('tb', a[1])
        if isinstance(a, tuple) and a[0] == 'sp':
            return stack_byte(s, a[1])
        return None

    def read16(self, a, s):
        lo, hi = self.read8(a, s), self.read8((a + 1) & 0xFFFF, s)
        return combine(hi, lo) if isinstance(lo, int) and isinstance(hi, int) else None

    def addr_of(self, s, o):
        if o[0] == 'abs':
            return o[1]
        return add_const(pget(s, o[1]), o[2])

    def g8(self, s, o):
        if isinstance(o, str):
            return s[o]
        if o[0] == 'imm':
            return o[1]
        a = self.addr_of(s, o)
        if a is None and o[0] == 'mem' and o[1] in ('IX', 'IY'):
            return ('mb', o[1], o[2])       # a byte of a structure field, base unknown
        return self.read8(a, s)

    def store8(self, s, addr, v):
        if isinstance(addr, tuple) and addr[0] == 'sp':
            st = s['stack']
            if st is not None:
                i = 1 + s['sbase'] - addr[1]
                if 0 <= i < len(st):
                    s['stack'] = st[:i] + (v,) + st[i + 1:]
            return
        if not isinstance(addr, int):
            return
        if self.mapper == 'codemasters':
            if addr == 0x8000:
                s['bank2'] = v
            elif addr == 0x4000:
                s['bank1'] = v
                self.slot1_banked_cur |= v != 1
        elif addr == 0xFFFF:
            s['bank2'] = v
            if isinstance(v, int):
                self.bank_values[2].add(v % self.nb)
        elif addr == 0xFFFE:
            s['bank1'] = v
            self.slot1_banked_cur |= v != 1
            if isinstance(v, int):
                self.bank_values[1].add(v % self.nb)

    # ---- transfer function (everything except control flow)

    def step(self, s, ins):
        sem = ins.sem
        t = sem[0]
        s = dict(s)
        if t == 'ld8':
            dst, src = sem[1], sem[2]
            v = self.g8(s, src)
            if isinstance(dst, str):
                s[dst] = v
            else:
                self.store8(s, self.addr_of(s, dst), v)
        elif t == 'ld16':
            dst, src = sem[1], sem[2]
            if isinstance(src, str):
                v = pget(s, src)
            elif src[0] == 'imm':
                v = src[1]
            else:
                v = self.read16(src[1], s)
            pset(s, dst, v)
        elif t == 'st16':
            nn, src = sem[1], sem[2]
            h, lo = halves(pget(s, src)) if src != 'SP' else (None, None)
            if src in PAIRS:
                h, lo = s[PAIRS[src][0]], s[PAIRS[src][1]]
            self.store8(s, nn, lo)
            self.store8(s, (nn + 1) & 0xFFFF, h)
        elif t in ('inc8', 'dec8'):
            o = sem[1]
            d = 1 if t == 'inc8' else -1
            if isinstance(o, str):
                v = s[o]
                s[o] = (v + d) & 0xFF if isinstance(v, int) else None
            else:
                self.store8(s, self.addr_of(s, o), None)
        elif t in ('inc16', 'dec16'):
            p = sem[1]
            if p == 'SP':
                if t == 'inc16':
                    pop_byte(s)
                else:
                    push_byte(s, None)
            else:
                pset(s, p, add_const(pget(s, p), 1 if t == 'inc16' else -1))
        elif t == 'add16':
            dst, src = sem[1], sem[2]
            a = pget(s, dst)
            if src == dst:
                r = (2 * a) & 0xFFFF if isinstance(a, int) else None
            else:
                b = pget(s, src)
                r = None
                if b is None and src in PAIRS and isinstance(s[PAIRS[src][0]], int):
                    r = add_bounded(a, s[PAIRS[src][0]] << 8, 255)
                elif a is None and isinstance(s[PAIRS[dst][0]], int) and isinstance(b, int):
                    r = add_bounded(b, s[PAIRS[dst][0]] << 8, 255)
                if r is None:
                    r = add16(a, b)
            pset(s, dst, r)
        elif t == 'adc16':
            pset(s, sem[1], None)
        elif t == 'alu':
            op, src = sem[1], sem[2]
            s['A'] = alu8(op, s['A'], self.g8(s, src), src == 'A')
        elif t == 'acc':
            name, a = sem[1], s['A']
            ia = isinstance(a, int)
            if name == 'CPL':
                s['A'] = (~a) & 0xFF if ia else None
            elif name == 'NEG':
                s['A'] = (-a) & 0xFF if ia else None
            elif name == 'RLCA':
                s['A'] = ((a << 1) | (a >> 7)) & 0xFF if ia else None
            elif name == 'RRCA':
                s['A'] = ((a >> 1) | (a << 7)) & 0xFF if ia else None
            elif name in ('SCF', 'CCF'):
                pass
            else:
                s['A'] = None
        elif t == 'cb':
            opn, bit, o, copy = sem[1], sem[2], sem[3], sem[4]
            if opn != 'BIT':
                v = self.g8(s, o)
                r = None
                if isinstance(v, int):
                    if opn == 'SET':
                        r = v | (1 << bit)
                    elif opn == 'RES':
                        r = v & ~(1 << bit) & 0xFF
                    elif opn == 'RLC':
                        r = ((v << 1) | (v >> 7)) & 0xFF
                    elif opn == 'RRC':
                        r = ((v >> 1) | (v << 7)) & 0xFF
                    elif opn == 'SLA':
                        r = (v << 1) & 0xFF
                    elif opn == 'SRL':
                        r = v >> 1
                    elif opn == 'SRA':
                        r = (v >> 1) | (v & 0x80)
                    elif opn == 'SLL':
                        r = ((v << 1) | 1) & 0xFF
                if isinstance(o, str):
                    s[o] = r
                else:
                    self.store8(s, self.addr_of(s, o), r)
                if copy:
                    s[copy] = r
        elif t == 'exaf':
            s['A'], s["A'"] = s["A'"], s['A']
        elif t == 'exx':
            for rg in 'BCDEHL':
                s[rg], s[rg + "'"] = s[rg + "'"], s[rg]
        elif t == 'exde':
            s['D'], s['H'] = s['H'], s['D']
            s['E'], s['L'] = s['L'], s['E']
        elif t == 'exsp':
            p = sem[1]
            hi, lo = PAIRS[p]
            st = s['stack']
            if st is None:
                s[hi], s[lo] = None, None
            else:
                while len(st) < 2:
                    # the bytes at SP are the caller's next argument bytes
                    st = (('sarg', s['sbase']),) + st
                    s['sbase'] += 1
                new_top = (s[hi], s[lo])
                s[hi], s[lo] = st[-2], st[-1]
                s['stack'] = st[:-2] + new_top
        elif t == 'push':
            p = sem[1]
            hv = (s['A'], s['F']) if p == 'AF' else (s[PAIRS[p][0]], s[PAIRS[p][1]])
            push_byte(s, hv[0])
            push_byte(s, hv[1])
        elif t == 'pop':
            p = sem[1]
            top = pop_word(s)
            if p == 'AF':
                s['A'] = top[0]
                s['F'] = top[1] if isinstance(top[1], tuple) and top[1][0] == 'lo' else None
            else:
                s[PAIRS[p][0]], s[PAIRS[p][1]] = top
        elif t == 'inn':
            s['A'] = None
        elif t == 'inC':
            if sem[1]:
                s[sem[1]] = None
        elif t == 'rxd':
            s['A'] = None
        elif t == 'block':
            self.block_effect(s, sem[1])
        return s

    def block_effect(self, s, name):
        down = name in ('LDD', 'LDDR', 'CPD', 'CPDR', 'IND', 'INDR', 'OUTD', 'OTDR')
        d = -1 if down else 1
        rep = name in ('LDIR', 'LDDR', 'CPIR', 'CPDR', 'INIR', 'INDR', 'OTIR', 'OTDR')
        if name in BLOCK_LD:
            bc = pget(s, 'BC')
            n = (bc or 0x10000) if isinstance(bc, int) else None
            if not rep:
                n = 1
            de = pget(s, 'DE')
            if isinstance(de, int) and n is not None:
                lo = de - n + 1 if down else de
                if lo <= 0xFFFF <= lo + n - 1 and self.mapper != 'codemasters':
                    s['bank2'] = None
                if lo <= 0xFFFE <= lo + n - 1 and self.mapper != 'codemasters':
                    s['bank1'] = None
            for p in ('HL', 'DE'):
                v = pget(s, p)
                pset(s, p, add_const(v, d * n) if n is not None else None)
            pset(s, 'BC', 0 if rep else add_const(bc, -1))
        elif name.startswith('CP'):
            pset(s, 'HL', None if rep else add_const(pget(s, 'HL'), d))
            pset(s, 'BC', None if rep else add_const(pget(s, 'BC'), -1))
        else:
            b = s['B']
            n = ((b or 256) if isinstance(b, int) else None) if rep else 1
            pset(s, 'HL', add_const(pget(s, 'HL'), d * n) if n is not None else None)
            s['B'] = 0 if rep else ((b - 1) & 0xFF if isinstance(b, int) else None)

    # ---- argument resolution through callers

    def _argform(self, v):
        return isinstance(v, tuple) and (v[0] in ('arg', 'sarg', 'sargw') or
                                         (v[0] == 'off' and isinstance(v[1], tuple) and v[1][0] == 'argpair'))

    def _in_caller(self, v, cs):
        if isinstance(v, int) or v is None:
            return v
        if v[0] == 'arg':
            return cs[v[1]]
        if v[0] == 'sarg':
            return caller_arg(cs, v[1])
        if v[0] == 'sargw':
            return caller_arg(cs, v[1], True)
        return add_const(pget(cs, v[1][1]), v[2])

    def resolve_multi(self, rt, vals, callers, depth=0, budget=None):
        """Values of vals at entry to rt, one tuple per caller path; None = a path that cannot be resolved."""
        if depth == 0 and callers is self.callers_prev:
            key = (rt, tuple(vals))
            hit = self.resolve_cache.get(key)
            if hit is None:
                hit = self.resolve_cache[key] = self._resolve_multi(rt, vals, callers, 0, None)
            return hit
        return self._resolve_multi(rt, vals, callers, depth, budget)

    def _resolve_multi(self, rt, vals, callers, depth=0, budget=None):
        if budget is None:
            budget = [256]
        if all(isinstance(v, int) for v in vals):
            return [tuple(vals)]
        budget[0] -= 1
        if depth > 8 or budget[0] < 0 or any(not isinstance(v, int) and not self._argform(v) for v in vals):
            return [None]
        R = self.routines.get(rt)
        out = []
        cl = callers.get(rt, [])
        if R is None or (R.kinds & UNKNOWN_ENTRY_KINDS) or not cl:
            out.append(None)
        for (crt, cnode, cs) in cl:
            cvals = [self._in_caller(v, cs) for v in vals]
            for x in self._resolve_multi(crt, cvals, callers, depth + 1, budget):
                if x not in out:
                    out.append(x)
        return out

    # ---- control-flow targets

    def resolve_target(self, rt, n, target, s):
        """List of (node, heuristic) for a transfer to cpu address target, or ([], reason)."""
        region = n[0]
        target &= 0xFFFF
        if target >= 0xC000:
            if region[0] == 'ram' and region[1] <= target < region[1] + region[2]:
                return [((region, target), False)], None
            hits = [c for c in self.copies_prev if c[2] is not None and c[0] <= target < c[0] + c[2]]
            if not hits:
                return [], 'ram'
            return [((('ram', c[0], c[2], c[1]), target), False) for c in hits], None
        slot = target >> 14
        if region[0] == 'rom' and region[1] == slot and slot != 2:
            return [((region, target), False)], None
        if slot == 0:
            return [((self.region_for(0, 0), target), False)], None
        if slot == 1:
            b = s['bank1']
            if isinstance(b, int):
                return [((self.region_for(1, b), target), False)], None
            if region[0] == 'rom' and region[1] == 1:
                return [((region, target), False)], None
            if self._argform(b):
                res = self.resolve_multi(rt, [b], self.callers_prev)
                if res and None not in res:
                    return [((self.region_for(1, x[0]), target), True) for x in res], None
            if not self.slot1_banked_prev:
                return [((self.region_for(1, 1), target), False)], None
            return [], 'bank1'
        b = s['bank2']
        if isinstance(b, int):
            return [((self.region_for(2, b), target), False)], None
        if region[0] == 'rom' and region[1] == 2:
            return [((region, target), False)], None
        if self._argform(b):
            res = self.resolve_multi(rt, [b], self.callers_prev)
            if res and None not in res:
                return [((self.region_for(2, x[0]), target), True) for x in res], None
        return [], 'bank'

    # ---- table readers

    def raw_words(self, a, s, count=16):
        """Words at cpu address a, for a person to read when the scanner could not follow a table."""
        words = []
        for i in range(count):
            lo, hi = self.read8(a + 2 * i, s), self.read8(a + 2 * i + 1, s)
            if not (isinstance(lo, int) and isinstance(hi, int)):
                break
            words.append('%04X' % (lo | hi << 8))
        return ' '.join(words) if words else 'not readable (bank unknown)'

    def plausible_code(self, node, want=4):
        """True when a linear decode from node gives want valid instructions, or a valid run that ends in a jump or return."""
        region, a = node
        for _ in range(want):
            ins = self.decode_node((region, a))
            if ins is None or ins.sem[0] == 'bad':
                return False
            t = ins.sem[0]
            if t in ('jpind', 'reti') or (t in ('ret', 'jp', 'jr') and ins.sem[-1] is None):
                return True
            a = (a + len(ins.raw)) & 0xFFFF
        return True

    def table_targets(self, rt, n, region, start, s):
        """Read a jump table at cpu address start. Returns (entries, byte count)."""
        entries, pos, limit = [], start, None
        size = 2
        skipped = False
        for _ in range(256):
            if limit is not None and pos >= limit:
                break
            if pos != start and self.off_of(region, pos) in self.code_starts_prev:
                break
            offs = [self.off_of(region, pos + i) for i in range(size)]
            if None in offs:
                break
            bs = [self.rom[o] for o in offs]
            w = bs[0] | (bs[1] << 8)
            nodes = []
            if not (w == 0 or w >= 0xC000 or start <= w < pos + size):
                nodes, why = self.resolve_target(rt, n, w, s)
            if not nodes or not self.plausible_code(nodes[0][0]):
                if pos == start and not skipped:
                    # tables indexed from 1 have no entry 0
                    skipped = True
                    pos += size
                    continue
                break
            entries.append((w, nodes))
            if w > start:
                limit = w if limit is None else min(limit, w)
            pos += size
        return entries, pos - start

    # ---- one routine

    def analyze(self, entry):
        R = self.routines[entry]
        region = entry[0]
        bank2 = region[2] if region[0] == 'rom' and region[1] == 2 else ('arg', 'bank2')
        if region[0] == 'rom' and region[1] == 1:
            bank1 = region[2]
        else:
            bank1 = ('arg', 'bank1') if self.slot1_banked_prev else 1 % self.nb
        K = self.unroll
        states = {entry: [initial_state(bank1, bank2)]}
        work = [(entry, 0)]
        while work:
            n, i = work.pop()
            s = states[n][i]
            ins = self.decode_node(n)
            if ins is None:
                continue
            for (m, s2, _tag) in self.flow(R, n, ins, s, False):
                lst = states.get(m)
                if lst is None:
                    states[m] = [s2]
                    work.append((m, 0))
                elif s2 in lst:
                    continue
                elif len(lst) < K:
                    lst.append(s2)
                    work.append((m, len(lst) - 1))
                else:
                    j = join_states(lst[-1], s2)
                    if j != lst[-1]:
                        lst[-1] = j
                        work.append((m, K - 1))
        # final pass from the fixed-point states
        edges = {}
        seen = {entry}
        queue = [entry]
        while queue:
            n = queue.pop()
            ins = self.decode_node(n)
            if ins is None:
                continue
            es = []
            for st in states[n]:
                for (m, _s, tag) in self.flow(R, n, ins, st, True):
                    es.append((m, tag))
            edges[n] = es
            for (m, _t) in es:
                if m not in seen:
                    seen.add(m)
                    queue.append(m)
        direct = {entry}
        queue = [entry]
        while queue:
            n = queue.pop()
            for (m, tag) in edges.get(n, []):
                if tag == 'd' and m not in direct:
                    direct.add(m)
                    queue.append(m)
        R.nodes = seen
        for n in sorted(seen, key=lambda x: (repr(x[0]), x[1])):
            if self.decode_node(n) is not None:
                lst = self.ctx.setdefault(n, [])
                for st in states[n]:
                    lst.append((entry, st, n not in direct))

    def add_routine(self, node, kind, caller=None, edge_heur=False):
        R = self.routines.get(node)
        if R is None:
            R = self.routines[node] = Routine(node)
            self.queue.append(node)
        R.kinds.add(kind)
        if caller is not None:
            crt, cnode, cs = caller
            self.callers_cur.setdefault(node, []).append((crt, cnode, cs))
            self.rt_edges.append((crt, node, edge_heur))
        return R

    def summary(self, node):
        return self.summ_prev.get(node, DEFAULT_SUMMARY)

    def apply_summary(self, summ, s):
        new = dict(s)
        for k in STATE_KEYS:
            o = summ.out.get(k)
            if o is None:
                new[k] = None
            elif o[0] == 'keep':
                pass
            elif o[0] == 'const':
                new[k] = o[1]
            elif o[0] == 'sym':
                new[k] = subst(o[1], s)
            else:
                new[k] = s[o[1]]
        return new

    def flow(self, R, n, ins, s, final):
        region, addr = n
        sem = ins.sem
        t = sem[0]
        out = []
        if t == 'bad':
            if final:
                self.bad_nodes.add(n)
            return out
        nxt = (addr + len(ins.raw)) & 0xFFFF
        why = self.implausible(ins)
        if why:
            if final:
                self.bad_nodes.add(n)
                self.bad_why[n] = why
            return out
        if t == 'rst' and sem[1] == 0x38:
            # RST $38 followed by $FF is erased-ROM fill, not code
            o = self.off_of(region, nxt)
            if o is not None and self.rom[o] == 0xFF:
                if final:
                    self.bad_nodes.add(n)
                return out
        s1 = self.step(s, ins)

        def go(target, st, tag='d', why_ctx='jump'):
            nodes, why = self.resolve_target(R.entry, n, target, st)
            for (m, heur) in nodes:
                out.append((m, st, 'h' if (heur or tag == 'h') else 'd'))
            if not nodes and final:
                self.unresolved.append((n, why_ctx, target, why))

        if t in ('jp', 'jr'):
            go(sem[1], s1)
            if sem[2]:
                go(nxt, s1)
        elif t == 'djnz':
            b = s1['B']
            st_t = dict(s1)
            st_t['B'] = (b - 1) & 0xFF if isinstance(b, int) else None
            st_f = dict(s1)
            st_f['B'] = 0
            if not isinstance(b, int) or st_t['B'] != 0:
                go(sem[1], st_t)
            if not isinstance(b, int) or st_t['B'] == 0:
                go(nxt, st_f)
        elif t in ('call', 'rst'):
            target = sem[1]
            cond = sem[2] if t == 'call' else None
            nodes, why = self.resolve_target(R.entry, n, target, s1)
            if not nodes:
                if final:
                    self.unresolved.append((n, 'call', target, why))
                go(nxt, self.apply_summary(DEFAULT_SUMMARY, s1))
            for (callee, heur) in nodes:
                if final:
                    self.add_routine(callee, t, (R.entry, n, s1), heur)
                summ = self.summary(callee)
                cs = self.apply_summary(summ, s1)
                tag = 'h' if heur else 'd'
                if summ.dispatch == 'inline':
                    ents, nbytes = self.table_targets(R.entry, n, region, nxt, s1)
                    if final:
                        self.tables.append((n, 'inline', nxt, [e[0] for e in ents], nbytes, region))
                    for (w, wnodes) in ents:
                        for (m, _h) in wnodes:
                            out.append((m, cs, 'h'))
                elif isinstance(summ.dispatch, tuple) and summ.dispatch[0] == 'jparg':
                    v = add_const(pget(s1, summ.dispatch[1]), summ.dispatch[2])
                    if isinstance(v, int):
                        vals, partial = [v], False
                    elif self._argform(v):
                        res = self.resolve_multi(R.entry, [v], self.callers_prev)
                        vals = [x[0] for x in res if x is not None]
                        partial = None in res
                    else:
                        vals, partial = [], True
                    for w in vals:
                        wnodes, why = self.resolve_target(R.entry, n, w, s1)
                        for (m, h2_) in wnodes:
                            if final:
                                self.add_routine(m, 'call', (R.entry, n, s1), heur or h2_ or len(vals) > 1)
                        if final:
                            self.indirect_resolved.append((n, 'call through %s' % summ.dispatch[1], w))
                    if partial and final:
                        self.unresolved.append((n, 'call through %s' % summ.dispatch[1], None, describe(v)))
                    go(nxt, self.apply_summary(DEFAULT_SUMMARY, s1), tag)
                elif isinstance(summ.dispatch, tuple):
                    base = pget(s1, summ.dispatch[1])
                    if isinstance(base, int):
                        ents, nbytes = self.table_targets(R.entry, n, region, base, s1)
                        if final:
                            self.tables.append((n, 'arg-' + summ.dispatch[1], base, [e[0] for e in ents], nbytes,
                                                ents[0][1][0][0][0] if ents else region))
                            for (w, wnodes) in ents:
                                for (m, _h) in wnodes:
                                    self.add_routine(m, 'table', (R.entry, n, cs), True)
                    elif final:
                        self.unresolved.append((n, 'dispatch-table', target, describe(base)))
                    go(nxt, cs, tag)
                elif summ.returns:
                    if summ.skip == 'var':
                        if final:
                            self.unresolved.append((n, 'inline-data', target, 'routine skips a variable number of bytes after the call'))
                    else:
                        if final and summ.skip:
                            for i in range(summ.skip):
                                o = self.off_of(region, nxt + i)
                                if o is not None:
                                    self.table_bytes.add(o)
                        go(nxt + summ.skip, cs, tag)
            if cond:
                go(nxt, s1)
        elif t in ('ret', 'reti'):
            cond = sem[1] if t == 'ret' else None
            self.do_return(R, n, s1, final, out, go)
            if cond:
                go(nxt, s1)
        elif t == 'jpind':
            self.do_indirect(R, n, pget(s1, sem[1]), s1, final, out, go, 'JP (%s)' % sem[1])
        else:
            go(nxt, s1)
        return out

    def implausible(self, ins):
        """Reason why a valid opcode is still unlikely to be code, or None."""
        sem = ins.sem
        t = sem[0]
        nn = None
        if t == 'ld8' and not isinstance(sem[1], str) and sem[1][0] == 'abs':
            nn, width = sem[1][1], 1
        elif t == 'st16':
            nn, width = sem[1], 2
        if nn is not None and nn + width - 1 < 0x8000:
            if nn not in CODEM_ADDRS:
                return 'store to ROM address %s' % h4(nn)
        if t == 'ld16' and sem[1] == 'SP' and not isinstance(sem[2], str) and sem[2][0] == 'imm' \
                and 0 < sem[2][1] < 0xC000:
            return 'stack pointer set into ROM (%s)' % h4(sem[2][1])
        return None

    def exit(self, R, kind, s, final):
        if final:
            R.exits.append((kind, s))

    def do_return(self, R, n, s, final, out, go):
        st = s['stack']
        if st is None:
            self.exit(R, 'normal', s, final)
            return
        if len(st) == 0:
            self.exit(R, 'normal', s, final)
            return
        s2 = dict(s)
        hi, lo = pop_word(s2)
        self.do_indirect(R, n, combine(hi, lo), s2, final, out, go, 'RET')

    def do_indirect(self, R, n, v, s, final, out, go, via):
        region, addr = n
        if isinstance(v, int):
            go(v, s)
            if final and via != 'RET':
                self.indirect_resolved.append((n, via, v))
            return
        if isinstance(v, tuple) and v[1] == 'RET':
            if v[0] == 'off':
                self.exit(R, ('skip', v[2]) if v[2] else 'normal', s, final)
                return
            if v[0] == 'idx':
                self.exit(R, 'skipvar', s, final)
                return
            if v[0] == 'word':
                if final:
                    R.dispatch = 'inline'
                return
        if isinstance(v, tuple) and v[0] == 'word':
            b = v[1]
            if isinstance(b, tuple) and b[0] == 'fromint':
                b = b[1]
            if isinstance(b, int):
                ents, nbytes = self.table_targets(R.entry, n, region, b, s)
                if final:
                    self.tables.append((n, 'word', b, [e[0] for e in ents], nbytes, region))
                for (w, wnodes) in ents:
                    for (m, _h) in wnodes:
                        out.append((m, s, 'h'))
                if ents:
                    return
                if final:
                    self.unresolved.append((n, via, None, 'word from table at %s; first words: %s' %
                                            (h4(b), self.raw_words(b, s))))
                s2 = {k: None for k in STATE_KEYS}
                s2['stack'] = s['stack']
                s2['sbase'] = s['sbase']
                self.exit(R, 'normal', s2, final)
                return
            elif isinstance(b, tuple) and b[0] == 'argpair':
                if final:
                    R.dispatch = ('arg', b[1])
                return
        if isinstance(v, tuple) and v[0] == 'mword':
            # jump through a pointer field of a structure: the harvest uses the field offset
            self.struct_dispatch.add((v[1], v[2]))
            if final:
                self.unresolved.append((n, via, None, 'word from (%s%+d), a pointer in a structure' % (v[1], v[2])))
            s2 = {k: None for k in STATE_KEYS}
            s2['stack'] = s['stack']
            s2['sbase'] = s['sbase']
            self.exit(R, 'normal', s2, final)
            return
        if self._argform(v) and v[0] == 'off':
            # JP (HL) to an address the caller passed in: a call through a pointer
            if final:
                R.dispatch = ('jparg', v[1][1], v[2])
            return
        if isinstance(v, tuple) and v[0] == 'idx' and isinstance(v[1], int) and v[1] < 0xC000:
            # base + index into a list of JP nn (3 bytes) or JR d (2 bytes) instructions
            o = self.cpu_off(v[1], s['bank2'], s['bank1'])
            op = self.rom[o] if o is not None else None
            if op in (0xC3, 0x18):
                stride = 3 if op == 0xC3 else 2
                tregion = region if (region[0] == 'rom' and region[1] == (v[1] >> 14)) else \
                    self.resolve_target(R.entry, n, v[1], s)[0][0][0][0]
                count = 0
                limit = None
                for i in range(64):
                    a = v[1] + stride * i
                    if limit is not None and a >= limit:
                        break
                    ins = self.decode_node((tregion, a))
                    if ins is None or ins.raw[0] != op or ins.sem[2] is not None:
                        break
                    t = ins.sem[1]
                    if t > v[1]:
                        limit = t if limit is None else min(limit, t)
                    out.append(((tregion, a), s, 'h'))
                    count += 1
                if final:
                    self.tables.append((n, 'jp-list' if op == 0xC3 else 'jr-list', v[1], [v[1] + stride * i for i in range(count)], 0, tregion))
                if count:
                    return
        if isinstance(v, tuple) and v[0] == 'idx' and isinstance(v[1], int) and v[1] < 0xC000:
            # base + unknown offset that is not a jump list: an entry into unrolled code
            # (a chain of LDI or OUTI, say). Follow the base; the rest of the chain is reached from it.
            nodes, why = self.resolve_target(R.entry, n, v[1], s)
            ins = self.decode_node(nodes[0][0]) if nodes else None
            if ins is not None and ins.sem[0] != 'bad':
                for (m, _h) in nodes:
                    out.append((m, s, 'h'))
                if final:
                    self.unresolved.append((n, via, None, describe(v) + '; followed at the base address only'))
                return
        if final:
            self.unresolved.append((n, via, None, describe(v)))
        # assume the unknown target returns to this routine's caller
        s2 = {k: None for k in STATE_KEYS}
        s2['stack'] = s['stack']
        s2['sbase'] = s['sbase']
        self.exit(R, 'normal', s2, final)

    # ---- rounds

    def begin_round(self):
        self.resolve_cache = {}
        self.slot1_banked_cur = False
        self.routines = {}
        self.queue = []
        self.ctx = {}
        self.callers_cur = {}
        self.rt_edges = []
        self.tables = []
        self.table_bytes = set()
        self.unresolved = []
        self.indirect_resolved = []
        self.bad_nodes = set()
        self.bad_why = {}

    def end_round(self):
        summ = {}
        for e, R in self.routines.items():
            exits = R.exits
            out = {}
            skip = 0
            if exits:
                j = exits[0][1]
                for _k, s in exits[1:]:
                    j = join_states(j, s)
                for k in STATE_KEYS:
                    v = j[k]
                    if v == ('arg', k):
                        out[k] = ('keep',)
                    elif isinstance(v, int):
                        out[k] = ('const', v)
                    elif isinstance(v, tuple) and v[0] == 'arg':
                        out[k] = ('from', v[1])
                    elif mentions_args(v):
                        out[k] = ('sym', v)
                    else:
                        out[k] = None
                kinds = set(k for k, _s in exits)
                if 'skipvar' in kinds:
                    skip = 'var'
                else:
                    ks = set(k[1] if isinstance(k, tuple) else 0 for k in kinds)
                    skip = ks.pop() if len(ks) == 1 else 'var'
            summ[e] = Summary(bool(exits) or isinstance(R.dispatch, tuple), skip, out, R.dispatch)
        self.summ_new = summ
        copies = []
        starts = set()
        for n, ctxs in self.ctx.items():
            ins = self.decode_node(n)
            o = self.off_of(n[0], n[1])
            if o is not None:
                starts.add(o)
            if ins.sem[0] == 'block' and ins.sem[1] in ('LDIR', 'LDDR'):
                for (rt, s, _h) in ctxs:
                    for c in self.copy_of(rt, n, s, ins.sem[1]):
                        if c not in copies:
                            copies.append(c)
        sig = (tuple(sorted((repr(k), v.key()) for k, v in summ.items())), tuple(sorted(map(repr, copies))),
               tuple(sorted(repr(t[:4]) for t in self.tables)), len(self.ctx))
        self.summ_prev = summ
        self.callers_prev = self.callers_cur
        self.resolve_cache = {}
        self.slot1_banked_prev = self.slot1_banked_cur
        sig = sig + (self.slot1_banked_cur,)
        self.copies_prev = copies
        self.code_starts_prev = starts
        return sig

    def copy_of(self, rt, n, s, name):
        """Copies ROM -> RAM made by an LDIR/LDDR: (dest, src_off, length, node)."""
        out = []
        vals = [pget(s, 'DE'), pget(s, 'HL'), pget(s, 'BC'), s['bank2'], s['bank1']]
        if not isinstance(vals[3], int) and not self._argform(vals[3]):
            vals[3] = 0
        if not isinstance(vals[4], int) and not self._argform(vals[4]):
            vals[4] = 1
        for res in self.resolve_multi(rt, vals, self.callers_cur):
            if res is None:
                continue
            de, hl, bc, b2, b1 = res
            length = bc or 0x10000
            if name == 'LDDR':
                de, hl = de - length + 1, hl - length + 1
            if de >= 0xC000 and hl < 0xC000:
                so = self.cpu_off(hl, b2, b1)
                if so is not None:
                    out.append((de, so, length, n))
        return out

    def run(self, seeds):
        seen = []
        self.rounds = 0
        self.cycled = False
        for rnd in range(MAX_ROUNDS):
            self.begin_round()
            for node, kind in seeds:
                self.add_routine(node, kind)
            while self.queue:
                e = self.queue.pop(0)
                self.analyze(e)
            sig = self.end_round()
            self.rounds = rnd + 1
            if seen and sig == seen[-1]:
                self.converged = True
                return
            if sig in seen:
                # a table read longer in one round decodes code that cuts it shorter in the next:
                # the rounds repeat, so stop here
                self.converged = True
                self.cycled = True
                return
            seen.append(sig)
        self.converged = False


# ------------------------------------------------------------------ inputs

def parse_addr(text, scanner):
    """ADDR or BANK:ADDR (hex) -> node."""
    if ':' in text:
        b, a = text.split(':')
        b, a = int(b, 16), int(a, 16)
        return ((scanner.region_for(a >> 14, b)), a)
    a = int(text, 16)
    slot = a >> 14
    return (scanner.region_for(slot, slot), a)


def read_logs(paths):
    """PCs from dynamic logs (docs/sitescan.md): list of (pc, bytes or None, source, kind, extra)."""
    out = []
    for p in paths:
        base = os.path.basename(p)
        if base.endswith('.io.tsv') or base.endswith('.mapper.tsv'):
            kind = 'io' if base.endswith('.io.tsv') else 'mapper'
            with open(p) as f:
                hdr = f.readline().rstrip('\n').split('\t')
                for line in f:
                    cols = line.rstrip('\n').split('\t')
                    if len(cols) < 4:
                        continue
                    row = dict(zip(hdr, cols))
                    bs = bytes.fromhex(row.get('insn_bytes', '').replace(' ', '')) if row.get('insn_bytes') else None
                    out.append((int(row['pc'], 16), bs, base, kind, row))
        elif base.endswith('.json'):
            with open(p) as f:
                d = json.load(f)
            pcs = set()

            def walk(o, key=''):
                if isinstance(o, dict):
                    for k, v in o.items():
                        walk(v, k)
                elif isinstance(o, list):
                    if key in ('example_pcs', 'ram_code_writer_pcs'):
                        for v in o:
                            if isinstance(v, str):
                                pcs.add(int(v, 16))
                    else:
                        for v in o:
                            walk(v, key)
            walk(d)
            for pc in sorted(pcs):
                out.append((pc, None, base, 'features', None))
        else:
            sys.exit('unknown log file type: %s' % p)
    return out


def logs_in_dir(d):
    out = []
    for name in sorted(os.listdir(d)):
        if name.endswith(('.io.tsv', '.mapper.tsv', '.features.json')):
            out.append(os.path.join(d, name))
    return out


def read_cdl(path, rom):
    data = open(path, 'rb').read()
    if data[:5] != b'CDLv2':
        sys.exit('%s: not a Mesen2 CDLv2 file' % path)
    crc = int.from_bytes(data[5:9], 'little')
    flags = data[9:]
    warn = None
    if crc != zlib.crc32(rom) & 0xFFFFFFFF:
        warn = 'CDL CRC32 %08X does not match the cart' % crc
    if len(flags) != len(rom):
        warn = (warn + '; ' if warn else '') + 'CDL has %d flag bytes, cart has %d bytes' % (len(flags), len(rom))
    offs = []
    prev_code = False
    for o, f in enumerate(flags[:len(rom)]):
        code = bool(f & 0x01)
        if code and (not prev_code or (f & 0x0C)):
            offs.append(o)
        prev_code = code
    return offs, warn


# ------------------------------------------------------------------ report

def main():
    ap = argparse.ArgumentParser(description='Static patch-site scanner for SMS carts (NextMasterSystem).')
    ap.add_argument('cart')
    ap.add_argument('--entry', action='append', default=[], help='extra entry point, hex ADDR or BANK:ADDR (repeatable)')
    ap.add_argument('--log', action='append', default=[], help='dynamic log: *.io.tsv, *.mapper.tsv or *.features.json (repeatable)')
    ap.add_argument('--logdir', action='append', default=[], help='directory holding dynamic log files (repeatable)')
    ap.add_argument('--cdl', help='Mesen2 CDLv2 file')
    ap.add_argument('--mapper', choices=['auto', 'sega', 'codemasters'], default='auto')
    ap.add_argument('--out', default='.', help='output directory')
    ap.add_argument('--name', help='output file prefix (default: cart file name)')
    ap.add_argument('--no-harvest', action='store_true', help='do not follow code addresses that the code stores into RAM')
    ap.add_argument('--unroll', type=int, default=8, help='distinct states kept per instruction before joining (default 8)')
    args = ap.parse_args()

    rom = open(args.cart, 'rb').read()
    header = 0
    if len(rom) % 16384 == 512:
        rom, header = rom[512:], 512
    crc = zlib.crc32(rom) & 0xFFFFFFFF
    name = args.name or os.path.splitext(os.path.basename(args.cart))[0]
    os.makedirs(args.out, exist_ok=True)

    mapper = 'sega' if args.mapper == 'auto' else args.mapper
    result = scan(rom, mapper, args)
    if args.mapper == 'auto':
        mp = [r for r in result['sites'] if r['kind'] == 'mapper']
        cm = [r for r in result['sites'] if r['kind'] == 'codem_store']
        if cm and not mp:
            mapper = 'codemasters'
            result = scan(rom, mapper, args)
    result['mapper'] = mapper
    write_outputs(result, rom, crc, header, name, args)


def byte_stores(sc, n, ins, s):
    """Byte stores of known values: list of (base key, offset, value)."""
    sem = ins.sem
    out = []
    if sem[0] == 'ld8' and not isinstance(sem[1], str):
        v = sc.g8(s, sem[2])
        if not isinstance(v, int):
            return out
        o = sem[1]
        a = sc.addr_of(s, o)
        if isinstance(a, int):
            out.append((('abs',), a, v))
        elif o[0] == 'mem':
            out.append((('reg', o[1]), o[2], v))
    return out


HARVEST_PORTS = COMMON_PORTS | {0xDE, 0xDF}


def harvest_dirty(sc, k):
    """True when code reached from a harvested entry shows signs of being data."""
    R = sc.routines.get(k)
    if R is None:
        return False
    nodes = R.nodes
    if nodes & sc.bad_nodes:
        return True
    for (n, via, target, why) in sc.unresolved:
        if n in nodes and why in ('ram', 'bank'):
            return True
    for n in nodes:
        ins = sc.decode_node(n)
        if ins is not None and ins.sem[0] in ('outn', 'inn') and ins.sem[1] not in HARVEST_PORTS:
            return True
    return False


def harvest(sc):
    """Code-like 16-bit constants written to RAM ($C000-$FFFF): candidate entry points."""
    per_node = {}
    for n, ctxs in sc.ctx.items():
        ins = sc.decode_node(n)
        sem = ins.sem
        for (_rt, s, _h) in ctxs:
            if sem[0] == 'st16' and sem[1] >= 0xC000 and sem[2] in PAIRS:
                v = pget(s, sem[2])
                if isinstance(v, int):
                    per_node.setdefault(n, set()).add(v)
            b1 = byte_stores(sc, n, ins, s)
            if not b1:
                continue
            m = (n[0], (n[1] + len(ins.raw)) & 0xFFFF)
            if m not in sc.ctx:
                continue
            mins = sc.decode_node(m)
            for (_rt2, s2, _h2) in sc.ctx[m]:
                for (k1, o1, v1) in b1:
                    for (k2, o2, v2) in byte_stores(sc, m, mins, s2):
                        if k1 != k2 or abs(o1 - o2) != 1:
                            continue
                        if k1 == ('abs',) and min(o1, o2) < 0xC000:
                            continue
                        if k1[0] == 'reg' and (k1[1], min(o1, o2)) not in sc.struct_dispatch:
                            continue
                        lo, hi = (v1, v2) if o1 < o2 else (v2, v1)
                        per_node.setdefault(n, set()).add(lo | (hi << 8))
    # a store that writes several different values (a pointer stepping through data) is not harvested
    words = {}
    for n, vals in per_node.items():
        if len(vals) == 1:
            words.setdefault(next(iter(vals)), n)
    out = []
    covered = set()
    for nn, ctxs in sc.ctx.items():
        for i in range(len(sc.decode_node(nn).raw)):
            o = sc.off_of(nn[0], nn[1] + i)
            if o is not None:
                covered.add(o)
    for w in sorted(words):
        if w >= 0x8000 and not (w < 0xC000 and sc.nb <= 2):
            continue
        if (w >> 8) == (w & 0xFF):
            continue        # $0909, $2020 and the like are fill or BCD values, not pointers
        node = (sc.region_for(w >> 14, w >> 14), w)
        o = sc.off_of(node[0], w)
        if o is None or o in covered or o in sc.table_bytes or sc.rom[o] == 0xFF:
            continue
        # the bytes must decode as a plausible run of code
        a, ok, count = w, True, 0
        while count < 12:
            ins = sc.decode_node((node[0], a))
            if ins is None or ins.sem[0] == 'bad':
                ok = False
                break
            count += 1
            if ins.sem[0] in ('ret', 'reti', 'jpind') and (ins.sem[0] != 'ret' or ins.sem[1] is None):
                break
            if ins.sem[0] in ('jp', 'jr') and ins.sem[2] is None:
                break
            a = (a + len(ins.raw)) & 0xFFFF
        if ok and count >= 2:
            out.append(node)
            sc.harvest_src[node] = words[w]
    return out


def scan(rom, mapper, args):
    sc = Scanner(rom, mapper, args.unroll)
    seeds = [((sc.region_for(0, 0), a), 'vector') for a in (0x0000, 0x0038, 0x0066) if a < len(rom)]
    for e in args.entry:
        seeds.append((parse_addr(e, sc), 'cmdline'))
    sc.run(seeds)
    static_rounds = sc.rounds
    static_starts = set(sc.off_of(x[0], x[1]) for x in sc.ctx)

    # pointer harvest: constant code-like addresses that the code writes to RAM
    harvested = []
    rejected = []
    if not args.no_harvest:
        for _ in range(8):
            new = [k for k in harvest(sc) if k not in harvested and k not in rejected]
            dirty = [k for k in harvested if harvest_dirty(sc, k)]
            if not new and not dirty:
                break
            for k in dirty:
                harvested.remove(k)
                rejected.append(k)
            harvested += new
            sc.run(seeds + [(k, 'harvest') for k in harvested])
        seeds = seeds + [(k, 'harvest') for k in harvested]
        static_starts = set(sc.off_of(x[0], x[1]) for x in sc.ctx)
    sc.harvest_rejected = rejected

    # dynamic seeds: only the PCs that static analysis did not reach
    log_files = list(args.log)
    for d in args.logdir:
        log_files += logs_in_dir(d)
    logs = read_logs(log_files)
    dyn = []
    log_notes = []
    ram_pcs = set()
    mismatched = []
    for pc, bs, src, kind, row in logs:
        if pc >= 0xC000:
            ram_pcs.add(pc)
            continue
        slot = pc >> 14
        if slot < 2:
            cands = [(sc.region_for(slot, slot), pc)]
            if bs:
                o = sc.off_of(cands[0][0], pc)
                if o is None or rom[o:o + len(bs)] != bs[:len(rom[o:o + len(bs)])]:
                    mismatched.append((src, pc))
                    continue
        else:
            cands = [(sc.region_for(2, b), pc) for b in range(sc.nb)]
            if bs:
                cands = [c for c in cands if all(sc.off_of(c[0], pc + i) is not None and rom[sc.off_of(c[0], pc + i)] == bs[i]
                                                 for i in range(min(len(bs), 2)))]
            elif sc.nb > 3:
                log_notes.append('%s: PC %s is in slot 2 and the log has no bytes to pick its bank; skipped' % (src, h4(pc)))
                continue
        for c in cands:
            dyn.append((c, kind, src))
    if mismatched:
        srcs = sorted(set(m[0] for m in mismatched))
        log_notes.append('%d log rows ignored because the cart bytes at their PC differ from the logged bytes (from %s); '
                         'the log is probably from another cart' % (len(mismatched), ', '.join(srcs)))
        bad = set(mismatched)
        logs = [l for l in logs if (l[2], l[0]) not in bad]
    cdl_warn = None
    if args.cdl:
        offs, cdl_warn = read_cdl(args.cdl, rom)
        for o in offs:
            if o < 0x8000:
                n = (sc.region_for(o >> 14, o >> 14), o)
            else:
                n = (sc.region_for(2, o >> 14), 0x8000 + (o & 0x3FFF))
            dyn.append((n, 'cdl', os.path.basename(args.cdl)))
    extra = []
    for n, kind, src in dyn:
        o = sc.off_of(n[0], n[1])
        if o is None or o in static_starts:
            continue
        k = 'cdl' if kind == 'cdl' else 'log'
        if (n, k) not in extra:
            extra.append((n, k))
    if extra:
        sc.run(seeds + extra)
    sc.harvested = harvested

    return collect(sc, rom, logs, log_notes, ram_pcs, cdl_warn, static_rounds, len(extra), args)


def collect(sc, rom, logs, log_notes, ram_pcs, cdl_warn, static_rounds, n_extra, args):
    # provenance of routines: best seed kind reachable
    rank = {}
    adj = {}
    for (a, b, heur) in sc.rt_edges:
        adj.setdefault(a, []).append((b, heur))
    heap = []
    for e, R in sc.routines.items():
        if R.kinds & STRONG_SEEDS:
            heap.append((0, repr(e), e, 'static'))
        elif 'log' in R.kinds or 'cdl' in R.kinds:
            heap.append((1, repr(e), e, 'log-seed' if 'log' in R.kinds else 'cdl-seed'))
        elif 'harvest' in R.kinds:
            heap.append((2, repr(e), e, 'pointer-harvest'))
    heapq.heapify(heap)
    while heap:
        r, _k, e, how = heapq.heappop(heap)
        if e in rank:
            continue
        rank[e] = (r, how)
        for (m, heur) in adj.get(e, []):
            if m not in rank:
                nr = max(r, 2) if heur else r
                nhow = how + '+table' if heur and not how.endswith('+table') else how
                heapq.heappush(heap, (nr, repr(m), m, nhow))

    log_io = {}
    log_map = {}
    for pc, bs, src, kind, row in logs:
        if kind == 'io':
            log_io[pc] = row
        elif kind == 'mapper':
            log_map.setdefault(pc, []).append(row)

    def provenance(n):
        best = None
        for (rt, s, heur) in sc.ctx[n]:
            r, how = rank.get(rt, (3, 'unknown'))
            if heur:
                r, how = max(r, 2), (how if how.endswith('+table') else how + '+table')
            if best is None or r < best[0]:
                best = (r, how)
        return best

    def conf(r):
        return 'high' if r <= 1 else 'medium'

    def node_off(n):
        return sc.off_of(n[0], n[1])

    def node_bank(n):
        return n[0][2] if n[0][0] == 'rom' else 'ram'

    sites, unproven = [], []

    def add_site(n, ins, kind, target, pclass, note=''):
        r, how = provenance(n)
        if n[1] in log_io or n[1] in log_map:
            how += '+seen-in-log'
        o = node_off(n)
        sites.append({'addr': n[1], 'bank': node_bank(n), 'offset': o, 'bytes': ins.hexbytes(), 'insn': ins.text,
                      'kind': kind, 'target': target, 'class': pclass, 'confidence': conf(r), 'how': how, 'note': note})

    def values_at(n, v_of_state):
        """Resolve a value at node n in every context. Returns (set of results, how) where how is local/callers/partial/unresolved."""
        res, local = [], True
        for (rt, s, _h) in sc.ctx[n]:
            v = v_of_state(s)
            if isinstance(v, int):
                res.append(v)
                continue
            local = False
            for x in sc.resolve_multi(rt, [v], sc.callers_prev):
                res.append(None if x is None else x[0])
        ints = sorted(set(x for x in res if x is not None))
        if not ints:
            return [], 'unresolved'
        if None in res:
            return ints, 'partial'
        return ints, ('local' if local else 'callers')

    def fmt_vals(vals, how, width=2):
        f = h2 if width == 2 else h4
        if how == 'unresolved':
            return 'unresolved'
        txt = ','.join(f(v) for v in vals)
        return txt if how == 'local' else '%s (%s)' % (txt, how)

    rst_used = {}
    for n in sorted(sc.ctx, key=lambda n: (node_off(n) if node_off(n) is not None else 1 << 30, n[1])):
        ins = sc.decode_node(n)
        sem = ins.sem
        t = sem[0]
        if t in ('outn', 'inn'):
            d = 'out' if t == 'outn' else 'in'
            add_site(n, ins, d, h2(sem[1]), port_class(sem[1], d))
        elif t in ('outC', 'inC') or (t == 'block' and (sem[1] in BLOCK_IN or sem[1] in BLOCK_OUT)):
            if t == 'block':
                d = 'in' if sem[1] in BLOCK_IN else 'out'
                kind = 'block_' + d
            else:
                d = 'out' if t == 'outC' else 'in'
                kind = d + '_c'
            vals, how = values_at(n, lambda s: s['C'])
            classes = sorted(set(port_class(v, d) for v in vals)) if vals else ['unresolved']
            if how == 'partial':
                classes.append('unresolved')
            add_site(n, ins, kind, fmt_vals(vals, how), '/'.join(classes))
        elif t == 'rst':
            add_site(n, ins, 'rst', h2(sem[1]), 'rst')
            rst_used.setdefault(sem[1], []).append(n[1])
        # stores
        forms = []
        if t == 'ld8' and not isinstance(sem[1], str):
            forms.append((sem[1], 1, sem[2]))
        elif t == 'st16':
            forms.append((('abs', sem[1]), 2, sem[2]))
        elif t in ('inc8', 'dec8') and not isinstance(sem[1], str):
            forms.append((sem[1], 1, None))
        elif t == 'cb' and sem[1] != 'BIT' and not isinstance(sem[3], str):
            forms.append((sem[3], 1, None))
        elif t == 'rxd':
            forms.append((('mem', 'HL', 0), 1, None))
        elif t == 'block' and sem[1] in BLOCK_LD:
            forms.append((('ldblock', sem[1]), 0, None))
        elif t == 'block' and sem[1] in BLOCK_IN:
            forms.append((('mem', 'HL', 0), 1, None))
        for (o, width, src) in forms:
            classify_store(sc, n, ins, o, width, src, add_site, unproven, provenance, conf, node_off, node_bank, values_at)
        # ROM -> RAM copies
        if t == 'block' and sem[1] in ('LDIR', 'LDDR'):
            for (rt, s, _h) in sc.ctx[n]:
                for c in sc.copy_of(rt, n, s, sem[1]):
                    note = '%d bytes from ROM offset %s to %s' % (c[2], '$%05X' % c[1], h4(c[0]))
                    if not any(x['kind'] == 'ram_copy' and x['addr'] == n[1] and x['target'] == note for x in sites):
                        executed = any(nn[0][0] == 'ram' and nn[0][1] == c[0] for nn in sc.ctx)
                        add_site(n, ins, 'ram_copy', note, 'code' if executed else 'data?',
                                 'code in this copy is executed (scanned at its RAM address)' if executed else
                                 'no call or jump into this range was found')

    # unresolved transfers
    seen_u = set()
    for (n, via, target, why) in sc.unresolved:
        key = (n, via, target, why)
        if key in seen_u or n not in sc.ctx:
            continue
        seen_u.add(key)
        ins = sc.decode_node(n)
        if why == 'ram':
            add_site(n, ins, 'ram_exec', h4(target), 'unresolved', 'jump or call into RAM; no ROM->RAM copy covering it was found')
        elif why in ('bank', 'bank1'):
            slot = 2 if why == 'bank' else 1
            vals = sorted(sc.bank_values[slot])
            add_site(n, ins, 'bank_unresolved', h4(target), 'unresolved',
                     'transfer into slot %d with an unknown bank; banks the code writes to $%s: %s' %
                     (slot, 'FFFF' if slot == 2 else 'FFFE', ','.join(str(v) for v in vals) or 'none proven'))
        elif via == 'inline-data':
            add_site(n, ins, 'inline_unresolved', h4(target), 'unresolved', why)
        elif via == 'dispatch-table':
            add_site(n, ins, 'indirect_unresolved', h4(target), 'unresolved', 'table dispatcher called with table address ' + why)
        elif via in ('call', 'jump'):
            add_site(n, ins, 'target_unresolved', h4(target) if target is not None else '', 'unresolved', str(why))
        else:
            add_site(n, ins, 'indirect_unresolved', '', 'unresolved', '%s with target %s' % (via, why))
    for (n, via, v) in sc.indirect_resolved:
        if n in sc.ctx and not any(x['kind'] == 'indirect_resolved' and x['addr'] == n[1] and x['target'] == h4(v) for x in sites):
            add_site(n, sc.decode_node(n), 'indirect_resolved', h4(v), 'flow', via + ' with a constant target')
    seen_t = set()
    for (n, kind, base, ents, nbytes, region) in sc.tables:
        key = (n, kind, base, tuple(ents))
        if key in seen_t or n not in sc.ctx:
            continue
        seen_t.add(key)
        add_site(n, sc.decode_node(n), 'jump_table', h4(base),
                 kind, '%d entries: %s' % (len(ents), ' '.join(h4(w) for w in ents)))
        if kind not in ('jp-list', 'jr-list'):
            for i in range(len(ents) * 2):
                o = sc.off_of(region, base + i)
                if o is not None:
                    sc.table_bytes.add(o)

    # RST vectors
    vectors = []
    for v in sorted(rst_used):
        n = (sc.region_for(0, 0), v)
        ins = sc.decode_node(n)
        tgt = h4(ins.sem[1]) if ins and ins.sem[0] == 'jp' and ins.sem[2] is None else 'code at the vector'
        vectors.append((v, tgt, ins.text if ins else '?', sorted(set(rst_used[v]))))
        sites.append({'addr': v, 'bank': 0, 'offset': v, 'bytes': ins.hexbytes() if ins else '', 'insn': ins.text if ins else '',
                      'kind': 'rst_vector', 'target': tgt, 'class': 'rst', 'confidence': 'high', 'how': 'static',
                      'note': 'used by %d RST sites' % len(set(rst_used[v]))})

    # coverage
    code = {}
    conflicts = set()
    for n in sc.ctx:
        ins = sc.decode_node(n)
        for i in range(len(ins.raw)):
            o = sc.off_of(n[0], (n[1] + i) & 0xFFFF)
            if o is None:
                continue
            kind = 'op' if i == 0 else 'arg'
            if o in code and code[o] != kind:
                conflicts.add(o)
                if kind == 'op':
                    code[o] = 'op'
            else:
                code.setdefault(o, kind)
    table_only = sc.table_bytes - set(code)

    # I/O byte patterns in bytes never reached
    unreached = []
    ED_IO = {0x40 + 8 * r: 'IN %s,(C)' % R8[r] for r in range(8) if r != 6}
    ED_IO.update({0x41 + 8 * r: 'OUT (C),%s' % R8[r] for r in range(8) if r != 6})
    ED_IO.update({0xA2: 'INI', 0xA3: 'OUTI', 0xAA: 'IND', 0xAB: 'OUTD', 0xB2: 'INIR', 0xB3: 'OTIR', 0xBA: 'INDR', 0xBB: 'OTDR'})
    for o in range(len(rom) - 1):
        if o in code or o in sc.table_bytes or (o + 1) in code:
            continue
        b0, b1 = rom[o], rom[o + 1]
        if b0 in (0xD3, 0xDB):
            d = 'out' if b0 == 0xD3 else 'in'
            txt = ('OUT (%s),A' if d == 'out' else 'IN A,(%s)') % h2(b1)
            cl = port_class(b1, d)
            c = 'low' if b1 in COMMON_PORTS else 'very-low'
        elif b0 == 0xED and b1 in ED_IO:
            txt, cl, c = ED_IO[b1], 'port in C', 'low'
        else:
            continue
        bank = o >> 14
        addr = o if o < 0x8000 else 0x8000 + (o & 0x3FFF)
        unreached.append({'addr': addr, 'bank': bank, 'offset': o, 'bytes': '%02X %02X' % (b0, b1), 'insn': txt,
                          'kind': 'io_unreached', 'target': h2(b1) if b0 != 0xED else '', 'class': cl,
                          'confidence': c, 'how': 'byte pattern in bytes no path reached', 'note': ''})

    unreached += mapper_byte_scan(sc, rom, code)

    # log comparison
    static_io = set(x['addr'] for x in sites if x['kind'] in ('in', 'out', 'in_c', 'out_c', 'block_in', 'block_out'))
    static_map = set(x['addr'] for x in sites if x['kind'] in ('mapper',))
    log_cmp = {
        'io_logged': sorted(log_io), 'io_logged_missed': sorted(set(log_io) - static_io),
        'map_logged': sorted(log_map), 'map_logged_missed': sorted(set(log_map) - static_map),
        'io_static_not_logged': sorted(static_io - set(log_io)) if log_io else None,
    }
    return {'sc': sc, 'sites': sites, 'unproven': unproven, 'unreached': unreached, 'code': code,
            'table_only': table_only, 'conflicts': conflicts, 'vectors': vectors, 'log_cmp': log_cmp,
            'log_notes': log_notes, 'ram_pcs': ram_pcs, 'cdl_warn': cdl_warn, 'static_rounds': static_rounds,
            'n_extra': n_extra, 'logs': logs}


def mapper_setter(ins, src):
    """True when ins loads the register a mapper store writes, in a way games do before one."""
    t = ins.text
    if src == 'A':
        if t.startswith('LD A,'):
            arg = t[5:]
            if arg.startswith('$') or arg in ('(HL)', '(DE)', '(BC)') or arg.startswith('(IX') or arg.startswith('(IY'):
                return True
            if arg.startswith('($') and int(arg[2:6], 16) >= 0xC000:
                return True
            return False
        if t == 'POP AF':
            return True     # restores a bank saved with PUSH AF
        # LD (nn),A to RAM: the game keeps a copy of the bank number
        return t.startswith('LD ($') and t.endswith('),A') and int(t[5:9], 16) >= 0xC000
    return t.startswith(('LD %s,$' % src, 'LD %s,($' % src, 'POP %s' % src))


def mapper_byte_patterns(rom, o, mapper):
    """The mapper store byte pattern at offset o: (length, text, source register, spec form) or None."""
    b = rom[o:o + 5]
    if len(b) >= 3 and b[0] == 0x32 and b[2] == 0xFF and b[1] >= 0xFC and mapper != 'codemasters':
        return 3, 'LD ($FF%02X),A' % b[1], 'A', 'mapst'
    if len(b) >= 3 and b[0] == 0x22 and b[2] == 0xFF and 0xFC <= b[1] <= 0xFE and mapper != 'codemasters':
        return 3, 'LD ($FF%02X),HL' % b[1], 'HL', 'mapsthl'
    if len(b) >= 4 and b[0] == 0xED and b[1] in (0x43, 0x53) and b[3] == 0xFF and 0xFC <= b[2] <= 0xFE \
            and mapper != 'codemasters':
        r = 'BC' if b[1] == 0x43 else 'DE'
        return 4, 'LD ($FF%02X),%s' % (b[2], r), r, 'mapst' + r.lower()
    if len(b) >= 5 and b[0] == 0x21 and b[2] == 0xFF and b[1] >= 0xFC and b[3] == 0x36 and mapper != 'codemasters':
        return 5, 'LD HL,$FF%02X; LD (HL),$%02X' % (b[1], b[4]), None, 'mapld' if b[1] == 0xFF else 'mapldk'
    if len(b) >= 3 and b[0] == 0x32 and b[1] == 0x00 and b[2] in (0x00, 0x40, 0x80) and mapper == 'codemasters':
        return 3, 'LD ($%02X00),A' % b[2], 'A', 'codem'
    return None


def mapper_byte_scan(sc, rom, code):
    """Mapper store byte patterns anywhere in the cart that no path reached as an instruction.

    Each hit is rated by evidence that it is code: the instruction just before it
    sets the stored register (a setter), a JP or CALL somewhere in the cart
    targets it, the bytes before it decode as a run of valid instructions that
    ends exactly on it, and the instructions after it decode cleanly. A hit that
    overlaps reached code at another instruction boundary, or lies in a jump
    table that was read, is data.
    """
    def cpu(o):
        return o if o < 0x8000 else 0x8000 | (o & 0x3FFF)

    def dec(o):
        if o < 0 or o >= len(rom):
            return None
        ins = decode(lambda i: rom[o + i] if o + i < len(rom) else None, cpu(o))
        if ins is None or ins.sem[0] == 'bad' or sc.implausible(ins):
            return None
        return ins

    # JP nn and CALL nn (plain and conditional) anywhere in the cart, by target
    refs = {}
    for o in range(len(rom) - 2):
        b0 = rom[o]
        if b0 in (0xC3, 0xCD) or (b0 & 0xC7) in (0xC2, 0xC4):
            refs.setdefault(rom[o + 1] | rom[o + 2] << 8, []).append(o)

    def referenced(o):
        a = cpu(o)
        rs = [r for r in refs.get(a, []) if code.get(r) != 'arg']
        return rs if o < 0x8000 else [r for r in rs if r >> 14 == o >> 14]

    def back_chain(o):
        """The longest chain (at most 32 bytes) of valid instructions that ends exactly at o."""
        for s in range(max(0, o - 32), o):
            p, chain = s, []
            while p < o:
                ins = dec(p)
                if ins is None:
                    break
                chain.append(ins)
                p += len(ins.raw)
            if p == o:
                return chain
        return []

    def fwd_chain(o, n):
        """Up to n valid instructions from o, stopping after an unconditional jump or return; None if one is invalid."""
        p, chain = o, []
        for _ in range(n):
            ins = dec(p)
            if ins is None or (ins.raw == [0xFF] and p + 1 < len(rom) and rom[p + 1] == 0xFF):
                return None
            chain.append(ins)
            t = ins.sem[0]
            if t in ('jpind', 'reti') or (t == 'ret' and ins.sem[1] is None) or (t in ('jp', 'jr') and ins.sem[2] is None):
                break
            p += len(ins.raw)
        return chain

    rows = []
    for o in range(len(rom) - 2):
        m = mapper_byte_patterns(rom, o, sc.mapper)
        if m is None:
            continue
        length, text, src, form = m
        if code.get(o) == 'op':
            continue            # reached as an instruction: the flow scan classified it
        ev, data = [], None
        if any(code.get(o + i) for i in range(length)):
            data = 'overlaps code that was reached at another instruction boundary'
        elif any((o + i) in sc.table_bytes for i in range(length)):
            data = 'inside a jump table that was read'
        setter = None
        if src is None:
            setter = 'LD HL,$FF%02X' % rom[o + 1]
        else:
            end = o
            for _ in range(3):
                for k in (4, 3, 2, 1):
                    ins = dec(end - k)
                    if ins is not None and len(ins.raw) == k and mapper_setter(ins, src):
                        setter = ins.text
                        break
                if setter or end < 1 or rom[end - 1] not in (0x00, 0x7F):
                    break
                end -= 1        # step back over NOP or LD A,A
        if not setter:
            for q in range(o - 6, o - 2):
                m2 = mapper_byte_patterns(rom, q, sc.mapper) if q >= 0 else None
                if m2 and m2[0] in (3, 4) and q + m2[0] <= o:
                    setter = 'another mapper store, %s at $%05X' % (m2[1], q)
                    break
        if setter:
            ev.append('after ' + setter)
        refs_o = referenced(o)
        if refs_o:
            ev.append('JP/CALL target from %s' % ' '.join('$%05X' % r for r in refs_o[:4]))
        back = back_chain(o)
        run = sum(len(x.raw) for x in back)
        if run >= 8:
            ev.append('%d bytes of valid code before it' % run)
        fwd = fwd_chain(o, 6)
        filler = []
        if fwd is None:
            ev.append('no valid code after it')
        else:
            # tile data and zero padding decode as runs of RST and NOP
            filler = [x for x in back + fwd[1:] if x.sem[0] == 'rst' or x.raw == [0]]
        if data or fwd is None:
            conf = 'low'
        elif setter or refs_o:
            conf = 'high'
        elif len(filler) >= 4:
            conf = 'low'
            ev.insert(0, '%d RST or NOP opcodes around it (looks like data)' % len(filler))
        elif run >= 8:
            conf = 'medium'
        else:
            conf = 'low'
        if data:
            ev.insert(0, data)
        rows.append({'addr': cpu(o), 'bank': o >> 14, 'offset': o, 'bytes': ' '.join('%02X' % x for x in rom[o:o + length]),
                     'insn': text, 'kind': 'mapper_unreached', 'target': form, 'class': 'byte scan',
                     'confidence': conf, 'how': 'byte scan, no path reached it', 'note': '; '.join(ev) or 'no evidence'})
    return rows


def classify_store(sc, n, ins, o, width, src, add_site, unproven, provenance, conf, node_off, node_bank, values_at):
    """Sort one store into mapper / codemasters / cart-area / proven harmless / unproven."""
    mapper_mode = sc.mapper
    if o[0] == 'ldblock':
        name = o[1]
        results = []
        partial = False
        for (rt, s, _h) in sc.ctx[n]:
            for x in sc.resolve_multi(rt, [pget(s, 'DE'), pget(s, 'BC')], sc.callers_prev):
                if x is None:
                    partial = True
                    continue
                de, bc = x
                ln = (bc or 0x10000) if name in ('LDIR', 'LDDR') else 1
                lo = de - ln + 1 if name in ('LDD', 'LDDR') else de
                results.append((lo, lo + ln - 1))
        hits = [r for r in results if r[0] <= MAPPER_HI and r[1] >= MAPPER_LO]
        if hits:
            add_site(n, ins, 'mapper', ' '.join('%s-%s' % (h4(a), h4(b)) for a, b in hits), 'block copy over $FFFC-$FFFF',
                     'partly unresolved' if partial else '')
        if partial or not results:
            de_txt = '; '.join(sorted(set(describe(pget(s, 'DE')) for (_r, s, _h) in sc.ctx[n])))
            unproven.append(unproven_row(sc, n, ins, 'DE=' + de_txt, 'block copy, destination or length not proven',
                                         provenance, node_off, node_bank))
        return
    if o[0] == 'abs':
        addrs, how = [o[1]], 'local'
    else:
        addrs, how = values_at(n, lambda s, o=o: sc.addr_of(s, o))
    span = [(a + i) & 0xFFFF for a in addrs for i in range(width)]
    val_txt = ''
    if src is not None and src not in PAIRS and src != 'SP':
        if isinstance(src, str):
            vals, vhow = values_at(n, lambda s, src=src: s[src])
        elif src[0] == 'imm':
            vals, vhow = [src[1]], 'local'
        else:
            vals, vhow = [], 'unresolved'
        if vhow != 'unresolved':
            val_txt = ','.join(h2(v) for v in vals) + ('' if vhow == 'local' else ' (%s)' % vhow)
        else:
            val_txt = 'unknown'
    mp = sorted(set(a for a in span if MAPPER_LO <= a <= MAPPER_HI))
    if mp:
        tgt = ','.join(h4(a) for a in mp) + ('<-' + val_txt if val_txt else '')
        add_site(n, ins, 'mapper', tgt, 'sega mapper' if mapper_mode != 'codemasters' else 'RAM ($FFFC-$FFFF)',
                 '' if how == 'local' else 'address %s' % how)
    cm = sorted(set(a for a in span if a in CODEM_ADDRS))
    if cm:
        add_site(n, ins, 'codem_store', ','.join(h4(a) for a in cm) + ('<-' + val_txt if val_txt else ''),
                 'codemasters mapper', '' if how == 'local' else 'address %s' % how)
    other = sorted(set(a for a in span if a < 0xC000 and a not in CODEM_ADDRS))
    if other:
        add_site(n, ins, 'cartarea_store', ','.join(h4(a) for a in other[:4]) + ('...' if len(other) > 4 else ''),
                 'store into $0000-$BFFF (cart RAM or ignored)', '' if how == 'local' else 'address %s' % how)
    if how in ('local', 'callers'):
        return
    # not proven: is the page known?
    if o[0] == 'mem':
        pages_ok = True
        descs = set()
        for (rt, s, _h) in sc.ctx[n]:
            v = sc.addr_of(s, o)
            descs.add(describe(v) + ('' if o[2] == 0 else ' (with displacement)'))
            if isinstance(v, int):
                continue
            if isinstance(v, tuple) and v[0] == 'sp':
                continue        # a slot in the routine's stack frame
            if isinstance(v, tuple) and v[0] == 'idx' and isinstance(v[1], int) and len(v) == 3:
                if not (v[1] <= MAPPER_HI and v[1] + v[2] >= MAPPER_LO):
                    continue
            hi = s[PAIRS[o[1]][0]]
            his = [hi] if isinstance(hi, int) else []
            if not his and sc._argform(hi):
                # the page comes from the caller: every known caller must pass a page other than $FF
                res = sc.resolve_multi(rt, [hi], sc.callers_prev)
                if res and None not in res:
                    his = [x[0] for x in res]
            if his and all(not ((h << 8) + o[2] <= MAPPER_HI and (h << 8) + o[2] + 255 >= MAPPER_LO) for h in his):
                continue
            pages_ok = False
        if pages_ok:
            return
        unproven.append(unproven_row(sc, n, ins, '; '.join(sorted(descs)),
                                     'address partly resolved' if how == 'partial' else 'address not proven',
                                     provenance, node_off, node_bank))


def unproven_row(sc, n, ins, addr_desc, reason, provenance, node_off, node_bank):
    r, how = provenance(n)
    return {'addr': n[1], 'bank': node_bank(n), 'offset': node_off(n), 'bytes': ins.hexbytes(), 'insn': ins.text,
            'address': addr_desc, 'reason': reason, 'how': how}


def node_bank_s(n):
    return str(n[0][2]) if n[0][0] == 'rom' else 'ram'


def fmt_off(o):
    return '' if o is None else '$%05X' % o


def write_outputs(res, rom, crc, header, name, args):
    sc = res['sc']
    out = args.out
    cols = ['addr', 'bank', 'offset', 'bytes', 'insn', 'kind', 'target', 'class', 'confidence', 'how', 'note']
    order = {'out': 0, 'in': 0, 'out_c': 0, 'in_c': 0, 'block_out': 0, 'block_in': 0, 'mapper': 1, 'codem_store': 2,
             'cartarea_store': 3, 'rst': 4, 'rst_vector': 5, 'ram_copy': 6, 'ram_exec': 7, 'jump_table': 8,
             'indirect_resolved': 9, 'indirect_unresolved': 10, 'bank_unresolved': 11, 'target_unresolved': 12,
             'inline_unresolved': 13, 'mapper_unreached': 19, 'io_unreached': 20}
    rows = res['sites'] + res['unreached']
    rows.sort(key=lambda r: (order.get(r['kind'], 15), r['offset'] if r['offset'] is not None else 1 << 30, r['addr']))
    with open(os.path.join(out, name + '.sites.tsv'), 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join([h4(r['addr']), str(r['bank']), fmt_off(r['offset'])] +
                              [str(r[c]) for c in cols[3:]]) + '\n')
    ucols = ['addr', 'bank', 'offset', 'bytes', 'insn', 'address', 'reason', 'how']
    with open(os.path.join(out, name + '.unproven.tsv'), 'w') as f:
        f.write('\t'.join(ucols) + '\n')
        for r in sorted(res['unproven'], key=lambda r: (r['offset'] if r['offset'] is not None else 1 << 30)):
            f.write('\t'.join([h4(r['addr']), str(r['bank']), fmt_off(r['offset'])] + [str(r[c]) for c in ucols[3:]]) + '\n')

    # listing
    with open(os.path.join(out, name + '.dis.txt'), 'w') as f:
        f.write('; sitescan listing of %s, CRC32 %08X. Columns: ROM offset, bank, address, bytes, instruction.\n' % (os.path.basename(args.cart), crc))
        site_at = {}
        for r in res['sites']:
            site_at.setdefault((r['offset'], r['addr']), []).append(r['kind'])
        nodes = sorted(sc.ctx, key=lambda n: (sc.off_of(n[0], n[1]) if sc.off_of(n[0], n[1]) is not None else 1 << 30, n[1]))
        prev_end = None
        for n in nodes:
            ins = sc.decode_node(n)
            o = sc.off_of(n[0], n[1])
            if prev_end is not None and o is not None and o != prev_end:
                f.write('\n')
            bank = n[0][2] if n[0][0] == 'rom' else 'ram'
            k = site_at.get((o, n[1]))
            f.write('%s  %-3s %04X  %-12s %-22s%s\n' % (fmt_off(o), bank, n[1], ins.hexbytes(), ins.text,
                                                       ('; ' + ','.join(sorted(set(k)))) if k else ''))
            prev_end = None if o is None else o + len(ins.raw)

    # summary
    code = res['code']
    L = []
    w = L.append
    w('sitescan summary: %s' % os.path.basename(args.cart))
    w('CRC32 %08X, %d bytes%s, %d banks of 16 KB, mapper model: %s' % (crc, len(rom), ' (512-byte copier header skipped)' if header else '', sc.nb, res['mapper']))
    w('Slot 1 ($4000-$7FFF) bank switching: %s' % ('seen (a store to $FFFE with a value other than 1, or an unknown value)'
                                                    if sc.slot1_banked_prev else 'not seen, slot 1 is taken as bank 1'))
    if sc.nb > 2:
        w('Constant banks written: $FFFE (slot 1): %s; $FFFF (slot 2): %s' % (
            ','.join(str(v) for v in sorted(sc.bank_values[1])) or 'none',
            ','.join(str(v) for v in sorted(sc.bank_values[2])) or 'none'))
    w('Analysis rounds: %d%s; dynamic or CDL entry points added after the static pass: %d' %
      (sc.rounds, ' (stopped when the rounds started to repeat; a table length alternates)' if sc.cycled else
       '' if sc.converged else ' (did not converge, results are from the last round)', res['n_extra']))
    w('')
    io = [r for r in res['sites'] if r['kind'] in ('out', 'in', 'out_c', 'in_c', 'block_out', 'block_in')]
    w('I/O instructions found on code paths: %d' % len(io))
    by = {}
    for r in io:
        by.setdefault(r['class'], 0)
        by[r['class']] += 1
    for k in sorted(by):
        w('  %-28s %d' % (k, by[k]))
    unres = [r for r in io if 'unresolved' in r['class']]
    if unres:
        w('  port not resolved for: ' + ' '.join(h4(r['addr']) for r in unres))
    conf_c = {}
    for r in io:
        conf_c[r['confidence']] = conf_c.get(r['confidence'], 0) + 1
    w('  by confidence: ' + ', '.join('%s %d' % kv for kv in sorted(conf_c.items())))
    w('')
    w('Address  Bank Bytes        Instruction           Kind       Port/target            Class                Confidence How found')
    for r in sorted(io, key=lambda r: (r['offset'] if r['offset'] is not None else 1 << 30)):
        w('%s %-4s %-12s %-21s %-10s %-22s %-20s %-10s %s' % (h4(r['addr']), r['bank'], r['bytes'], r['insn'], r['kind'],
                                                             r['target'], r['class'], r['confidence'], r['how']))
    w('')
    for kind, title in (('mapper', 'Stores that reach $FFFC-$FFFF (proven)'), ('codem_store', 'Codemasters-style stores ($0000/$4000/$8000, proven)'),
                        ('cartarea_store', 'Other proven stores into $0000-$BFFF')):
        rs = [r for r in res['sites'] if r['kind'] == kind]
        w('%s: %d' % (title, len(rs)))
        for r in rs:
            w('  %s bank %s  %-12s %-20s %s %s' % (h4(r['addr']), r['bank'], r['bytes'], r['insn'], r['target'], r['note']))
        w('')
    up = res['unproven']
    w('Stores through a register whose address is not proven to stay off $FFFC-$FFFF: %d (full list in %s.unproven.tsv)' % (len(up), name))
    reasons = {}
    for r in up:
        insn = r['insn']
        if '(IX' in insn or '(IY' in insn:
            form = 'through IX or IY'
        elif '(HL)' in insn:
            form = 'through HL'
        elif '(DE)' in insn or '(BC)' in insn:
            form = 'through DE or BC'
        else:
            form = 'block copy (LDI, LDIR and the like)'
        key = '%s, %s' % (r['reason'], form)
        reasons[key] = reasons.get(key, 0) + 1
    for k, v in sorted(reasons.items()):
        w('  %-60s %d' % (k, v))
    w('')
    w('RST vectors used:')
    for v, tgt, txt, callers in res['vectors']:
        w('  RST %s: vector holds "%s" -> %s; called from %s' % (h2(v), txt, tgt, ' '.join(h4(c) for c in callers)))
    if not res['vectors']:
        w('  none on the code paths found')
    w('')
    for kind, title in (('ram_copy', 'ROM to RAM copies (LDIR/LDDR, destination $C000-$FFFF)'),
                        ('ram_exec', 'Jumps or calls into RAM with no known copy'),
                        ('jump_table', 'Jump tables read'),
                        ('indirect_resolved', 'Indirect jumps resolved to a constant'),
                        ('indirect_unresolved', 'Indirect jumps not resolved (add entry points by hand)'),
                        ('bank_unresolved', 'Transfers into a banked slot with an unknown bank'),
                        ('target_unresolved', 'Other unresolved transfers'),
                        ('inline_unresolved', 'Calls to routines that skip a variable amount of inline data')):
        rs = [r for r in res['sites'] if r['kind'] == kind]
        w('%s: %d' % (title, len(rs)))
        for r in rs:
            w('  %s bank %s  %-20s %s %s %s' % (h4(r['addr']), r['bank'], r['insn'], r['target'], r['class'], r['note']))
        w('')
    if getattr(sc, 'harvested', None):
        w('Entry points taken from code addresses stored into RAM (pointer harvest, medium confidence):')
        for k in sc.harvested:
            src = sc.harvest_src.get(k)
            sins = sc.decode_node(src) if src else None
            w('  %s bank %s, stored by %s %s' % (h4(k[1]), k[0][2], h4(src[1]) if src else '?', sins.text if sins else ''))
        w('')
    if getattr(sc, 'harvest_rejected', None):
        w('Harvested addresses rejected because the code reached from them looks like data: ' +
          ' '.join(h4(k[1]) for k in sc.harvest_rejected))
        w('')
    if sc.bad_nodes:
        w('Paths that stopped because the bytes do not look like code (likely data reached as code):')
        for n in sorted(sc.bad_nodes, key=lambda n: (sc.off_of(n[0], n[1]) or 0, n[1])):
            ins = sc.decode_node(n)
            w('  %s bank %s  %-20s %s' % (h4(n[1]), node_bank_s(n), ins.text if ins else '',
                                          sc.bad_why.get(n, 'invalid opcode or $FF fill')))
        w('')
    if res['conflicts']:
        cs = sorted(res['conflicts'])
        w('Bytes decoded both as an opcode and as an operand (overlapping code paths): %d, first at %s' %
          (len(cs), ' '.join(fmt_off(o) for o in cs[:20])))
        w('')
    lo = [r for r in res['unreached'] if r['confidence'] == 'low']
    vl = [r for r in res['unreached'] if r['confidence'] == 'very-low']
    w('I/O byte patterns in bytes no path reached: %d with a common SMS port or an ED I/O opcode, %d others (all in %s.sites.tsv as io_unreached)' % (len(lo), len(vl), name))
    for r in lo:
        w('  offset %s (bank %d, %s)  %-6s %s' % (fmt_off(r['offset']), r['bank'], h4(r['addr']), r['bytes'], r['insn']))
    w('')
    mb = [r for r in res['unreached'] if r['kind'] == 'mapper_unreached']
    w('Mapper store byte patterns in bytes no path reached (byte scan): %s (all in %s.sites.tsv as mapper_unreached)' % (
        ', '.join('%s %d' % (c, sum(1 for r in mb if r['confidence'] == c)) for c in ('high', 'medium', 'low')), name))
    for r in mb:
        w('  offset %s (bank %d, %s)  %-6s %-14s %-24s %s' % (fmt_off(r['offset']), r['bank'], h4(r['addr']), r['confidence'],
                                                            r['bytes'], r['insn'], r['note']))
    w('')
    # coverage
    w('Coverage (bytes):')
    w('  bank  code   table/inline  unknown')
    tot = [0, 0, 0]
    for b in range(sc.nb):
        lo_o, hi_o = b * 0x4000, min(len(rom), (b + 1) * 0x4000)
        c = sum(1 for o in range(lo_o, hi_o) if o in code)
        t = sum(1 for o in range(lo_o, hi_o) if o in res['table_only'])
        u = (hi_o - lo_o) - c - t
        tot[0] += c
        tot[1] += t
        tot[2] += u
        w('  %-4d  %-6d %-13d %d' % (b, c, t, u))
    w('  all   %-6d %-13d %d   (code %.1f%% of the cart)' % (tot[0], tot[1], tot[2], 100.0 * tot[0] / len(rom)))
    w('')
    lc = res['log_cmp']
    if res['logs']:
        w('Dynamic logs: %d PCs read' % len(res['logs']))
        w('  logged I/O sites: %d, not found by the static scan: %s' % (len(lc['io_logged']), ' '.join(h4(a) for a in lc['io_logged_missed']) or 'none'))
        w('  logged mapper-write sites: %d, not found as proven mapper stores: %s' % (len(lc['map_logged']), ' '.join(h4(a) for a in lc['map_logged_missed']) or 'none'))
        if lc['io_static_not_logged'] is not None:
            w('  static I/O sites the log never saw: %d: %s' % (len(lc['io_static_not_logged']), ' '.join(h4(a) for a in lc['io_static_not_logged'])))
        if res['ram_pcs']:
            w('  PCs in RAM in the logs (not scanned): ' + ' '.join(h4(a) for a in sorted(res['ram_pcs'])))
        for x in res['log_notes']:
            w('  ' + x)
        w('')
    if res['cdl_warn']:
        w('CDL: ' + res['cdl_warn'])
    with open(os.path.join(out, name + '.summary.txt'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('%s: %d I/O sites, %d mapper stores, %d unproven stores, code %d of %d bytes; output in %s' %
          (name, len(io), len([r for r in res['sites'] if r['kind'] == 'mapper']), len(up), tot[0], len(rom), out))


if __name__ == '__main__':
    main()
