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
        self.edges = {}          # node -> [(successor, tag)] inside the routine


class Summary:
    def __init__(self, returns=True, skip=0, out=None, dispatch=None):
        self.returns, self.skip, self.out, self.dispatch = returns, skip, out or {}, dispatch

    def key(self):
        return (self.returns, self.skip, tuple(sorted((k, repr(v)) for k, v in self.out.items())), repr(self.dispatch))


DEFAULT_SUMMARY = Summary()
UNKNOWN_ENTRY_KINDS = {'vector', 'cmdline', 'table', 'log', 'cdl', 'ram', 'harvest', 'bankcall', 'bankhead',
                       'htable', 'hstore', 'hspawn'}
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
        self.bank_calls = set()
        self.bank_headers = set()
        self.task_entries = set()
        self.handler_kind = {}       # handler entry node -> 'htable', 'hstore' or 'hspawn'
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
        if not isinstance(bank1, int) and R.kinds & set(HANDLER_HOW) and len(self.bank_values[1]) == 1:
            # an object handler runs from its dispatcher: slot 1 holds the one bank the code writes there
            bank1 = next(iter(self.bank_values[1]))
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
        R.edges = edges
        self.stack_switches(seen, states)
        for n in sorted(seen, key=lambda x: (repr(x[0]), x[1])):
            if self.decode_node(n) is not None:
                lst = self.ctx.setdefault(n, [])
                for st in states[n]:
                    lst.append((entry, st, n not in direct))

    def stack_switches(self, nodes, states):
        """Report a RET that runs on a stack loaded from a register or from RAM.

        LD SP,HL / LD SP,(nn) with an unknown value, then RET, is a task or
        coroutine switch: the RET goes to an address kept on another stack, and
        the code it starts is not followed. Without this report the RET looks
        like a plain return.
        """
        nodes = sorted(nodes, key=nkey)
        loads = []
        for m in nodes:
            ins = self.decode_node(m)
            if ins is None or ins.sem[0] != 'ld16' or ins.sem[1] != 'SP':
                continue
            src = ins.sem[2]
            if isinstance(src, tuple) and src[0] == 'imm':
                continue
            if any(self.step(st, ins)['stack'] is None for st in states[m]):
                loads.append(m)
        if not loads:
            return
        what = ', '.join('%s %s' % (h4(m[1]), self.decode_node(m).text) for m in sorted(loads, key=nkey)[:3])
        for m in nodes:
            ins = self.decode_node(m)
            if ins is not None and ins.sem[0] in ('ret', 'reti') and any(st['stack'] is None for st in states[m]):
                self.stack_switch.add(m)
                self.unresolved.append((m, 'RET', None, 'an address on a stack the routine switched to (%s): '
                                        'a task or coroutine switch; the tasks it starts are not followed' % what))

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
        self.stack_switch = set()

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
        hl, bc = vals[1], vals[2]
        if isinstance(hl, int) and isinstance(bc, int):
            lo, hi = (hl - (bc or 0x10000) + 1, hl) if name == 'LDDR' else (hl, hl + (bc or 0x10000) - 1)
            # a source wholly in slot 0 (always bank 0) or slots 0-1 needs no slot 2 bank,
            # and one wholly in slot 0 no slot 1 bank
            if 0 <= lo and hi < 0x8000:
                vals[3] = 0
            if 0 <= lo and hi < 0x4000:
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
            pcs = set()     # (pc, cart offset in hex or '')
            lists = {'example_pcs': 'example_offsets', 'ram_code_writer_pcs': 'ram_code_writer_offsets'}

            def walk(o):
                if isinstance(o, dict):
                    for k, v in o.items():
                        if k in lists and isinstance(v, list):
                            offs = o.get(lists[k])
                            offs = offs if isinstance(offs, list) and len(offs) == len(v) else [''] * len(v)
                            for pc, off in zip(v, offs):
                                if isinstance(pc, str):
                                    pcs.add((int(pc, 16), off if isinstance(off, str) else ''))
                        else:
                            walk(v)
                elif isinstance(o, list):
                    for v in o:
                        walk(v)
            walk(d)
            for pc, off in sorted(pcs):
                out.append((pc, None, base, 'features', {'cart_offset': off} if off else None))
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
    ap.add_argument('--no-tracedef', action='store_true',
                    help='run without tools/tracedef.py: the trace and run forms are not costed and the costs differ from the overlay builder\'s (printed in the summary)')
    ap.add_argument('--handler', action='append', default=[],
                    help='frame cost model: the game\'s own interrupt handler entry, hex ADDR or BANK:ADDR (repeatable)')
    args = ap.parse_args()
    TRACEDEF_OFF[0] = args.no_tracedef
    load_tracedef()         # fail now, not after the scan

    args.entry = args.entry + args.handler
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
    TRACEDEF_OFF[0] = args.no_tracedef
    result['cost'] = frame_cost(result['sc'], [parse_addr(h, result['sc']) for h in args.handler])
    result['rules'] = pattern_rules(result, rom, mapper, args)
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
    # a task started from a table of task entries may call code the game put in RAM
    stops = ('bank',) if k in sc.task_entries else ('ram', 'bank')
    for (n, via, target, why) in sc.unresolved:
        if n in nodes and why in stops:
            return True
    for n in nodes:
        ins = sc.decode_node(n)
        if ins is not None and ins.sem[0] in ('outn', 'inn') and ins.sem[1] not in HARVEST_PORTS:
            return True
    return False


def task_table_words(sc):
    """Words of a ROM table that the code stores into RAM, in a cart that switches stacks.

    A task scheduler starts a task by writing its start address, read from a
    table of task entry points, onto the task's own stack, byte by byte through
    a register pointer; a RET after LD SP later jumps there. Only used when a
    stack switch was found, because outside that pattern a table word stored to
    RAM is usually a data pointer. A store to a fixed address is not used.
    Returns {word: storing node}.
    """
    out = {}
    done = set()
    for n, ctxs in sc.ctx.items():
        ins = sc.decode_node(n)
        sem = ins.sem
        for (rt, s, _h) in ctxs:
            v = None
            # a byte store through a register pointer: a task's stack is not at a fixed address
            if sem[0] == 'ld8' and not isinstance(sem[1], str) and sem[1][0] == 'mem' and isinstance(sem[2], str):
                a = sc.addr_of(s, sem[1])
                if isinstance(a, int) and a < 0xC000:
                    continue
                for p in ('BC', 'DE', 'HL'):
                    if sem[2] in PAIRS[p]:
                        v = pget(s, p)
            if not (isinstance(v, tuple) and v[0] == 'word' and isinstance(v[1], int) and v[1] < 0xC000):
                continue
            base = v[1]
            if (base, s['bank1'], s['bank2']) in done:
                continue
            done.add((base, s['bank1'], s['bank2']))
            slot = base >> 14
            if slot < 2 and not (slot == 1 and s['bank1'] != 1 % sc.nb):
                region = sc.region_for(slot, slot)
            elif isinstance(s['bank2'] if slot == 2 else s['bank1'], int):
                region = sc.region_for(slot, s['bank2'] if slot == 2 else s['bank1'])
            else:
                continue
            ents, _nbytes = sc.table_targets(rt, n, region, base, s)
            for (w, _nodes) in ents:
                out.setdefault(w, n)
    return out


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
    task_ws = set()
    if sc.stack_switch:
        for w, n in task_table_words(sc).items():
            words.setdefault(w, n)
            task_ws.add(w)
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
        if code_like(sc, node, covered):
            out.append(node)
            sc.harvest_src[node] = words[w]
            if w in task_ws:
                sc.task_entries.add(node)
    for node, src, kind in handler_entries(sc, covered):
        if node not in out:
            out.append(node)
            sc.harvest_src[node] = src
            sc.handler_kind[node] = kind
    for node, src in bank_calls(sc, covered):
        if node not in out:
            out.append(node)
            sc.harvest_src[node] = src
            sc.bank_calls.add(node)
    for node in bank_headers(sc, covered):
        if node not in out:
            out.append(node)
            sc.bank_headers.add(node)
    return out


def bank_headers(sc, covered):
    """Module headers: a bank that starts with two or more JP nn, every nn in $8000-$BFFF.

    Games keep a module (an init entry, a per-frame entry) in a bank of its own
    and call the header entries with that bank in slot 2. Each JP of the
    header is an entry in that bank, however the caller picks the bank.
    """
    out = []
    rom = sc.rom
    for b in range(2, sc.nb):
        o, jps = b * 0x4000, 0
        while o + 3 * jps + 2 < len(rom) and rom[o + 3 * jps] == 0xC3 \
                and 0x8000 <= (rom[o + 3 * jps + 1] | (rom[o + 3 * jps + 2] << 8)) < 0xC000:
            jps += 1
        if jps < 2:
            continue
        for i in range(jps):
            node = (sc.region_for(2, b), 0x8000 + 3 * i)
            if code_like(sc, node, covered, follow_jp=True):
                out.append(node)
    return out


def seed_kind(sc, k):
    """The seed kind of an entry that harvest() returned."""
    if k in sc.handler_kind:
        return sc.handler_kind[k]
    return 'bankcall' if k in sc.bank_calls else 'bankhead' if k in sc.bank_headers else 'harvest'


def code_like(sc, node, covered, follow_jp=False):
    """True when the bytes at node are not reached yet and decode as a plausible run of code.

    With follow_jp, a JP nn continues the run at nn, so a jump table entry counts.
    """
    o = sc.off_of(node[0], node[1])
    if o is None or o in covered or o in sc.table_bytes or sc.rom[o] == 0xFF:
        return False
    a, count = node[1], 0
    while count < 12:
        ins = sc.decode_node((node[0], a))
        if ins is None or ins.sem[0] == 'bad':
            return False
        count += 1
        if ins.sem[0] in ('ret', 'reti', 'jpind') and (ins.sem[0] != 'ret' or ins.sem[1] is None):
            break
        if ins.sem[0] == 'jp' and ins.sem[2] is None and follow_jp and isinstance(ins.sem[1], int):
            a = ins.sem[1]
            continue
        if ins.sem[0] in ('jp', 'jr') and ins.sem[2] is None:
            break
        a = (a + len(ins.raw)) & 0xFFFF
    return count >= 2


HANDLER_HOW = {'htable': 'handler-table', 'hstore': 'handler-store', 'hspawn': 'handler-spawn'}
FLOW_STOP = {'jp', 'jr', 'djnz', 'call', 'rst', 'ret', 'reti', 'retn', 'jpind', 'bad', 'halt'}


def _field_load(ins):
    """(dst register, index register, d) for LD r,(IX+d) or LD r,(IY+d), else None."""
    sem = ins.sem
    if sem[0] == 'ld8' and isinstance(sem[1], str) and not isinstance(sem[2], str) \
            and sem[2][0] == 'mem' and sem[2][1] in ('IX', 'IY'):
        return sem[1], sem[2][1], sem[2][2]
    return None


def _field_store(ins):
    """(index register, d, source) for LD (IX+d),r or LD (IX+d),n (IX or IY), else None."""
    sem = ins.sem
    if sem[0] == 'ld8' and not isinstance(sem[1], str) and sem[1][0] == 'mem' and sem[1][1] in ('IX', 'IY'):
        return sem[1][1], sem[1][2], sem[2]
    return None


def handler_fields(sc):
    """Offsets d of the record fields that hold an object's handler address.

    A field is a handler field when code a path reached jumps through it:
    LD L,(IX+d) and LD H,(IX+d+1), in either order (IX or IY), right before
    JP (HL); or the same loads into E and D right before EX DE,HL; JP (HL).
    Games run each object this way: the record's handler field holds the
    address of the routine that updates it.
    """
    out = set()
    for n in sc.ctx:
        if sc.decode_node(n).sem != ('jpind', 'HL'):
            continue
        a, regs = n[1], ('L', 'H')
        if (n[0], (a - 1) & 0xFFFF) in sc.ctx and sc.decode_node((n[0], (a - 1) & 0xFFFF)).sem == ('exde',):
            a, regs = a - 1, ('E', 'D')
        loads = {}
        for b in ((a - 6) & 0xFFFF, (a - 3) & 0xFFFF):
            m = (n[0], b)
            if m not in sc.ctx:
                break
            f = _field_load(sc.decode_node(m))
            if f is None or len(sc.decode_node(m).raw) != 3:
                break
            loads[f[0]] = f[1:]
        lo, hi = loads.get(regs[0]), loads.get(regs[1])
        if lo and hi and lo[0] == hi[0] and hi[1] == lo[1] + 1:
            out.add(lo[1])
    return out


def _table_region(sc, base, s):
    """The region to read a table at cpu address base in state s, or None when its bank is unknown."""
    slot = base >> 14
    if slot == 0:
        return sc.region_for(0, 0)
    if slot == 1:
        b = s['bank1']
        if isinstance(b, int):
            return sc.region_for(1, b)
        return None if sc.slot1_banked_prev else sc.region_for(1, 1)
    if slot == 2 and isinstance(s['bank2'], int):
        return sc.region_for(2, s['bank2'])
    return None


def handler_entries(sc, covered):
    """Object handlers stored into a handler field (handler_fields()) by code a path reached.

    The low and high byte stores, LD (X+d),r and LD (X+d+1),r with X IX or IY and d a
    handler field, in either order and at most four straight-line instructions apart,
    store a word:
    - a constant (LD (IX+d),n twice, or the halves of LD HL,nn): the handler ('hstore');
    - a word read from a table in ROM at a constant base with an index added
      (LD HL,table; ADD HL,BC; ADD HL,BC; LD A,(HL); INC HL; LD A,(HL)): every entry of
      the table is a handler ('htable'). The table is read as a jump table is
      (Scanner.table_targets()), so it ends at the first entry that is not code;
    - a register pair the routine was called with (a spawn routine that stores the DE
      its caller loaded): the constant each caller passes ('hspawn').
    A call of a routine that jumps to its caller's HL (a call through HL), with HL a word
    read from such a table, also makes every entry of the table a handler ('htable').
    A handler runs later, from the dispatcher, so the slot 1 bank at the store does not
    name its bank. When the slot 1 bank is unknown there and the code writes one constant
    bank to $FFFE and no other, a target in slot 1 is in that bank.
    Returns [(node, store node, kind)] for targets no path reached that decode as code.
    """
    fields = handler_fields(sc)
    found = []
    seen = set()
    one_bank1 = next(iter(sc.bank_values[1])) if len(sc.bank_values[1]) == 1 else None

    def add(w, rt, n, s, kind):
        if not isinstance(w, int) or w >= 0xC000 or (w >> 8) == (w & 0xFF):
            return
        nodes, _why = sc.resolve_target(rt, n, w, s)
        for (m, _h) in nodes:
            if m not in seen and code_like(sc, m, covered):
                seen.add(m)
                found.append((m, n, kind))

    def table(base, rt, n, s):
        if not isinstance(base, int) or base >= 0xC000:
            return
        region = _table_region(sc, base, s)
        if region is None:
            return
        ents, _nbytes = sc.table_targets(rt, n, region, base, s)
        for (w, _nodes) in ents:
            add(w, rt, n, s, 'htable')

    def known1(s):
        return s if isinstance(s['bank1'], int) or one_bank1 is None else dict(s, bank1=one_bank1)

    for n in sorted(sc.ctx, key=repr):
        ins = sc.decode_node(n)
        f = _field_store(ins)
        if f is None or f[1] not in fields:
            continue
        # n stores the low byte; find the high byte store after it, or before it
        pair = None
        for direction in (1, -1):
            path, a = [n], n[1]
            for _ in range(4):
                if direction == 1:
                    a = (a + len(sc.decode_node((n[0], a)).raw)) & 0xFFFF
                    m = (n[0], a)
                else:
                    m = next(((n[0], (a - k) & 0xFFFF) for k in (4, 3, 2, 1)
                              if (n[0], (a - k) & 0xFFFF) in sc.ctx
                              and (a - k + len(sc.decode_node((n[0], (a - k) & 0xFFFF)).raw)) & 0xFFFF == a), None)
                    if m is None:
                        break
                    a = m[1]
                if m not in sc.ctx:
                    break
                mi = sc.decode_node(m)
                if mi.sem[0] in FLOW_STOP:
                    break
                path.append(m)
                g = _field_store(mi)
                if g is not None and g[0] == f[0] and g[1] == f[1] + 1:
                    pair = path if direction == 1 else path[::-1]
                    break
            if pair:
                break
        if not pair:
            continue
        first, last = pair[0], pair[-1]
        lo_node, hi_node = n, (last if direction == 1 else first)
        for (rt, s, _h) in sc.ctx[first]:
            st, vals = s, {}
            for k in pair:
                ki = sc.decode_node(k)
                if k in (lo_node, hi_node):
                    vals[k] = sc.g8(st, _field_store(ki)[2])
                if k != last:
                    st = sc.step(st, ki)
            lo, hi = vals[lo_node], vals[hi_node]
            w = combine(hi, lo)
            s = known1(s)
            if isinstance(w, int):
                add(w, rt, n, s, 'hstore')
            elif isinstance(w, tuple) and w[0] == 'word':
                table(w[1], rt, n, s)
            elif sc._argform(w):
                for res in sc.resolve_multi(rt, [w], sc.callers_prev):
                    if res is not None:
                        add(res[0], rt, n, s, 'hspawn')
    # a call through HL with HL a word read from a table
    for n in sorted(sc.ctx, key=repr):
        ins = sc.decode_node(n)
        if ins.sem[0] != 'call' or not isinstance(ins.sem[1], int):
            continue
        for (rt, s, _h) in sc.ctx[n]:
            nodes, _why = sc.resolve_target(rt, n, ins.sem[1], s)
            for (callee, _hh) in nodes:
                d = sc.summary(callee).dispatch
                if not (isinstance(d, tuple) and d[0] == 'jparg' and d[2] == 0):
                    continue
                v = pget(s, d[1])
                if isinstance(v, tuple) and v[0] == 'word':
                    table(v[1], rt, n, known1(s))
    return found


def bank_calls(sc, covered):
    """Calls into slot 2 right after a constant bank switch that no path reached.

    The bytes are LD A,n, then optionally LD (nn),A to RAM (a copy of the bank
    number), then LD ($FFFF),A and CALL nn or JP nn with nn in $8000-$BFFF, all
    in slot 0 or slot 1. Games start objects this way from a handler that is
    reached only through RAM. The target in bank n is the entry: (node, store node).
    """
    out = []
    if sc.mapper == 'codemasters':
        return out
    rom = sc.rom
    for o in range(min(len(rom), 0x8000) - 10):
        if rom[o] != 0x3E or rom[o + 1] >= sc.nb:
            continue
        p = o + 2
        if rom[p] == 0x32 and rom[p + 2] >= 0xC0 and not (rom[p + 2] == 0xFF and rom[p + 1] >= 0xFC):
            p += 3
        if rom[p:p + 3] != b'\x32\xFF\xFF' or p in covered or rom[p + 3] not in (0xCD, 0xC3):
            continue
        w = rom[p + 4] | (rom[p + 5] << 8)
        if not 0x8000 <= w < 0xC000:
            continue
        node = (sc.region_for(2, rom[o + 1]), w)
        if code_like(sc, node, covered, follow_jp=True):
            out.append((node, (sc.region_for(p >> 14, p >> 14), p)))
    return out


def starts_without_handlers(sc):
    """Cart offsets of the instructions that routines reach from every seed but the object
    handler entries. Code that only a handler entry reaches stays open to the dynamic logs,
    so a logged PC there is still a log seed (high confidence)."""
    seeds = {'vector', 'cmdline', 'harvest', 'bankcall', 'bankhead'}
    adj = {}
    for (a, b, _h) in sc.rt_edges:
        adj.setdefault(a, []).append(b)
    todo = [e for e, R in sc.routines.items() if R.kinds & seeds]
    done = set(todo)
    while todo:
        for m in adj.get(todo.pop(), []):
            if m not in done:
                done.add(m)
                todo.append(m)
    out = set()
    for e in done:
        for n in sc.routines[e].nodes:
            out.add(sc.off_of(n[0], n[1]))
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
            # an entry whose store is in code no longer reached (code of a rejected entry) has lost its evidence
            stale = [k for k in harvested if k not in dirty and k not in sc.bank_calls
                     and sc.harvest_src.get(k) is not None and sc.harvest_src[k] not in sc.ctx]
            if not new and not dirty and not stale:
                break
            for k in dirty:
                harvested.remove(k)
                rejected.append(k)
            for k in stale:
                harvested.remove(k)
            harvested += new
            sc.run(seeds + [(k, seed_kind(sc, k)) for k in harvested])
        seeds = seeds + [(k, seed_kind(sc, k)) for k in harvested]
        static_starts = starts_without_handlers(sc)
    sc.harvest_rejected = rejected

    # dynamic seeds: only the PCs that static analysis did not reach
    ref = rom
    log_files = list(args.log)
    for d in args.logdir:
        log_files += logs_in_dir(d)
    logs = read_logs(log_files)
    dyn = []
    log_notes = []
    ram_pcs = set()
    mismatched = []
    no_bank = {}
    for pc, bs, src, kind, row in logs:
        if pc >= 0xC000:
            ram_pcs.add(pc)
            continue
        slot = pc >> 14
        co = row.get('cart_offset') if isinstance(row, dict) else None
        if co:
            # the log names the cart offset the PC ran from, so the bank is known
            o = int(co, 16)
            c = (sc.region_for(slot, o >> 14), pc)
            if sc.off_of(c[0], pc) != o or (bs and ref[o:o + len(bs)] != bs[:len(ref[o:o + len(bs)])]):
                mismatched.append((src, pc))
                continue
            cands = [c]
        elif slot == 0 and sc.mapper != 'codemasters' or slot == 1 and sc.mapper != 'codemasters' and not sc.slot1_banked_prev:
            # a slot the cart never banks: the address names the bank
            cands = [(sc.region_for(slot, slot), pc)]
            if bs:
                o = sc.off_of(cands[0][0], pc)
                if o is None or ref[o:o + len(bs)] != bs[:len(ref[o:o + len(bs)])]:
                    mismatched.append((src, pc))
                    continue
        else:
            # a PC in a slot the cart banks, with no cart offset, does not say which bank ran: not evidence
            no_bank.setdefault(src, set()).add(pc)
            continue
        for c in cands:
            dyn.append((c, kind, src))
    for src in sorted(no_bank):
        log_notes.append('%s: %d PCs in banked slots skipped because the log has no cart_offset column to name their bank'
                         % (src, len(no_bank[src])))
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
    sc.final_seeds = seeds + extra

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
        elif 'bankcall' in R.kinds:
            heap.append((2, repr(e), e, 'bank-call'))
        elif 'bankhead' in R.kinds:
            heap.append((2, repr(e), e, 'bank-header'))
        elif R.kinds & set(HANDLER_HOW):
            heap.append((2, repr(e), e, HANDLER_HOW[min(R.kinds & set(HANDLER_HOW))]))
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
    seen_offs, seen_pcs = set(), set()     # logged cart offsets; logged PCs outside slot 2 (ROM or RAM) with no offset
    for pc, bs, src, kind, row in logs:
        if kind == 'io':
            log_io[pc] = row
        elif kind == 'mapper':
            log_map.setdefault(pc, []).append(row)
        if kind in ('io', 'mapper'):
            co = row.get('cart_offset') if isinstance(row, dict) else None
            if co:
                seen_offs.add(int(co, 16))
            elif not 0x8000 <= pc < 0xC000:
                seen_pcs.add(pc)

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
        if node_off(n) in seen_offs or (n[1] in seen_pcs and not 0x8000 <= n[1] < 0xC000):
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
    for n in sorted(sc.ctx, key=lambda n: (node_off(n) if node_off(n) is not None else 1 << 30, nkey(n))):
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

    # I/O and mapper store byte patterns in bytes never reached
    bev = ByteEvidence(sc, rom, code)
    unreached = io_byte_scan(sc, rom, code, bev)
    unreached += mapper_byte_scan(sc, rom, code, bev)

    # Evidence only adds up: a site that only medium paths reach keeps the high
    # rating the byte scans give it when the code those paths reach is left out.
    strong = {}
    for n in sc.ctx:
        if provenance(n)[0] > 1:
            continue
        ins = sc.decode_node(n)
        for i in range(len(ins.raw)):
            o = sc.off_of(n[0], (n[1] + i) & 0xFFFF)
            if o is not None:
                strong.setdefault(o, 'op' if i == 0 else 'arg')
    weak = [x for x in sites if x['confidence'] == 'medium' and isinstance(x['offset'], int)]
    if weak:
        sbev = ByteEvidence(sc, rom, strong)
        rated = {(r['offset'], r['insn']): r for r in io_byte_scan(sc, rom, strong, sbev) + mapper_byte_scan(sc, rom, strong, sbev)
                 if r['confidence'] == 'high'}
        for x in weak:
            r = rated.get((x['offset'], x['insn']))
            if r is not None:
                x['confidence'] = 'high'
                x['how'] += ' + byte pattern'
                x['note'] = '; '.join(v for v in (x['note'], r['note']) if v)

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


class ByteEvidence:
    """Evidence that a byte pattern no path reached is code, for the byte scans.

    The tests: a JP or CALL somewhere in the cart targets it (and, when asked,
    a JR or DJNZ, or a branch to the one-byte instruction just before it), the
    bytes before it decode as a run of valid instructions that ends exactly on
    it, and the instructions after it decode cleanly. Tile data and zero
    padding decode as runs of RST and NOP.
    """

    def __init__(self, sc, rom, code):
        self.sc, self.rom, self.code = sc, rom, code
        self.refs = {}          # JP nn / CALL nn (plain and conditional), by target
        self.rel = {}           # JR, JR cc and DJNZ, by target
        for o in range(len(rom) - 2):
            b0 = rom[o]
            if b0 in (0xC3, 0xCD) or (b0 & 0xC7) in (0xC2, 0xC4):
                self.refs.setdefault(rom[o + 1] | rom[o + 2] << 8, []).append(o)
        for o in range(len(rom) - 1):
            if rom[o] in (0x10, 0x18, 0x20, 0x28, 0x30, 0x38):
                self.rel.setdefault(o + 2 + s8(rom[o + 1]), []).append(o)

    def cpu(self, o):
        return o if o < 0x8000 else 0x8000 | (o & 0x3FFF)

    def dec(self, o):
        rom = self.rom
        if o < 0 or o >= len(rom):
            return None
        ins = decode(lambda i: rom[o + i] if o + i < len(rom) else None, self.cpu(o))
        if ins is None or ins.sem[0] == 'bad' or self.sc.implausible(ins):
            return None
        return ins

    def referenced(self, o, relative=False):
        """Offsets of branches that target o. relative: also JR and DJNZ, and branches to a
        one-byte instruction just before o that runs on into it."""
        code = self.code
        rs = [r for r in self.refs.get(self.cpu(o), []) if code.get(r) != 'arg']
        if o >= 0x8000:
            rs = [r for r in rs if r >> 14 == o >> 14]
        if not relative:
            return rs
        rs = rs + [r for r in self.rel.get(o, []) if code.get(r) != 'arg' and r >> 14 == o >> 14]
        p = self.dec(o - 1)
        if p is not None and len(p.raw) == 1 and p.sem[0] not in ('ret', 'reti', 'jpind', 'rst'):
            before = [r for r in self.refs.get(self.cpu(o - 1), []) + self.rel.get(o - 1, [])
                      if code.get(r) != 'arg' and (o - 1 < 0x8000 or r >> 14 == o >> 14)]
            rs = rs + [r for r in before if r not in rs]
        return rs

    def back_chain(self, o):
        """The longest chain (at most 32 bytes) of valid instructions that ends exactly at o."""
        for s in range(max(0, o - 32), o):
            p, chain = s, []
            while p < o:
                ins = self.dec(p)
                if ins is None:
                    break
                chain.append(ins)
                p += len(ins.raw)
            if p == o:
                return chain
        return []

    def fwd_chain(self, o, n):
        """Up to n valid instructions from o, stopping after an unconditional jump or return; None if one is invalid."""
        rom = self.rom
        p, chain = o, []
        for _ in range(n):
            ins = self.dec(p)
            if ins is None or (ins.raw == [0xFF] and p + 1 < len(rom) and rom[p + 1] == 0xFF):
                return None
            chain.append(ins)
            t = ins.sem[0]
            if t in ('jpind', 'reti') or (t == 'ret' and ins.sem[1] is None) or (t in ('jp', 'jr') and ins.sem[2] is None):
                break
            p += len(ins.raw)
        return chain

    def setter_before(self, o, src):
        """Text of the instruction just before o that loads src for a store or OUT.

        It steps back over up to two NOP, LD A,A or (when src is not HL) EX (SP),HL,
        which games put before an OUT to the VDP as a delay.
        """
        rom = self.rom
        skip = (0x00, 0x7F) if src == 'HL' else (0x00, 0x7F, 0xE3)
        end = o
        for _ in range(3):
            for k in (4, 3, 2, 1):
                ins = self.dec(end - k)
                if ins is not None and len(ins.raw) == k and mapper_setter(ins, src):
                    return ins.text
            if end < 1 or rom[end - 1] not in skip:
                return None
            end -= 1
        return None

    def rate(self, o, data, setter, relative=False):
        """Confidence and evidence list for a pattern at o.

        data: a reason the bytes are data, or None. setter: text of a setter, or None.
        """
        ev = []
        if setter:
            ev.append('after ' + setter)
        refs_o = self.referenced(o, relative)
        if refs_o:
            ev.append('branch target from %s' % ' '.join('$%05X' % r for r in refs_o[:4]) if relative else
                      'JP/CALL target from %s' % ' '.join('$%05X' % r for r in refs_o[:4]))
        back = self.back_chain(o)
        run = sum(len(x.raw) for x in back)
        if run >= 8:
            ev.append('%d bytes of valid code before it' % run)
        fwd = self.fwd_chain(o, 6)
        filler = []
        if fwd is None:
            ev.append('no valid code after it')
        else:
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
        return conf, ev


ED_IO = {0x40 + 8 * r: 'IN %s,(C)' % R8[r] for r in range(8) if r != 6}
ED_IO.update({0x41 + 8 * r: 'OUT (C),%s' % R8[r] for r in range(8) if r != 6})
ED_IO.update({0xA2: 'INI', 0xA3: 'OUTI', 0xAA: 'IND', 0xAB: 'OUTD', 0xB2: 'INIR', 0xB3: 'OTIR', 0xBA: 'INDR', 0xBB: 'OTDR'})


def io_byte_scan(sc, rom, code, bev):
    """IN, OUT and ED I/O byte patterns that no path reached, rated by the same evidence as the mapper byte scan.

    A port SMS games do not use is always very-low. For an OUT the setter is the
    instruction just before it loading A. A branch target with no setter and no
    valid code before it is medium, not high.
    """
    rows = []
    for o in range(len(rom) - 1):
        if o in code or o in sc.table_bytes or (o + 1) in code:
            continue
        b0, b1 = rom[o], rom[o + 1]
        if b0 in (0xD3, 0xDB):
            d = 'out' if b0 == 0xD3 else 'in'
            txt = ('OUT (%s),A' if d == 'out' else 'IN A,(%s)') % h2(b1)
            cl = port_class(b1, d)
            port_c = 'low' if b1 in COMMON_PORTS else 'very-low'
            setter = bev.setter_before(o, 'A') if d == 'out' else None
        elif b0 == 0xED and b1 in ED_IO:
            txt, cl, port_c, setter = ED_IO[b1], 'port in C', 'low', None
        else:
            continue
        conf, ev = bev.rate(o, None, setter, relative=True)
        if conf == 'high' and not setter and not any(e.endswith('bytes of valid code before it') for e in ev):
            conf = 'medium'     # only a branch points at it, and data can supply one
        if b0 == 0xED and b1 == 0xA3 and conf != 'high':
            # An unrolled OUTI block is entered at a computed address: the OUTIs before the
            # first one a path reached are code when an unbroken run of OUTI leads to it.
            p = o + 2
            while p + 1 < len(rom) and p >> 14 == o >> 14 and p not in code and rom[p] == 0xED and rom[p + 1] == 0xA3:
                p += 2
            if code.get(p) == 'op' and p + 1 < len(rom) and rom[p] == 0xED and rom[p + 1] == 0xA3:
                conf = 'high'
                ev = ['in an unrolled OUTI run that reaches code at $%05X' % p] + [e for e in ev if 'looks like data' not in e]
        if port_c == 'very-low':
            conf = 'very-low'   # a port SMS games do not use: data, whatever the bytes around it look like
            ev.insert(0, 'port not used by SMS games')
        rows.append({'addr': bev.cpu(o), 'bank': o >> 14, 'offset': o, 'bytes': '%02X %02X' % (b0, b1), 'insn': txt,
                     'kind': 'io_unreached', 'target': h2(b1) if b0 != 0xED else '', 'class': cl,
                     'confidence': conf, 'how': 'byte pattern in bytes no path reached', 'note': '; '.join(ev) or 'no evidence'})
    return rows


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


def mapper_byte_scan(sc, rom, code, bev):
    """Mapper store byte patterns anywhere in the cart that no path reached as an instruction.

    Each hit is rated by ByteEvidence, plus a setter: the instruction just before
    it sets the stored register. A hit that overlaps reached code at another
    instruction boundary, or lies in a jump table that was read, is data.
    """
    rows = []
    for o in range(len(rom) - 2):
        m = mapper_byte_patterns(rom, o, sc.mapper)
        if m is None:
            continue
        length, text, src, form = m
        if code.get(o) == 'op':
            continue            # reached as an instruction: the flow scan classified it
        data = None
        if any(code.get(o + i) for i in range(length)):
            data = 'overlaps code that was reached at another instruction boundary'
        elif any((o + i) in sc.table_bytes for i in range(length)):
            data = 'inside a jump table that was read'
        if src is None:
            setter = 'LD HL,$FF%02X' % rom[o + 1]
        else:
            setter = bev.setter_before(o, src)
        if not setter:
            for q in range(o - 6, o - 2):
                m2 = mapper_byte_patterns(rom, q, sc.mapper) if q >= 0 else None
                if m2 and m2[0] in (3, 4) and q + m2[0] <= o:
                    setter = 'another mapper store, %s at $%05X' % (m2[1], q)
                    break
        conf, ev = bev.rate(o, data, setter)
        rows.append({'addr': bev.cpu(o), 'bank': o >> 14, 'offset': o, 'bytes': ' '.join('%02X' % x for x in rom[o:o + length]),
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


# ------------------------------------------------------------ frame cost model
#
# On the Next every SMS I/O instruction runs through the engine's io trap, which
# costs far more than the instruction does on an SMS. The model adds up, per
# routine, the Next cycles of the native instructions and of the traps, and
# compares them with the Next frame. docs/sitescan.md describes the method and
# the output.
#
# All costs are Next CPU cycles (28 MHz). They were measured in MAME tbblue with
# the engine built from public/ at commit 03a88f6: a test cart runs each form
# between two breakpoints that print totalcycles (median over passes, with the
# trace cache warm), and the same forms were timed at Alien Syndrome's own
# sites. The 'otir' and 'run' rows and OUT (C),r to the control port were
# measured again, the same way, on the ABI 7 engine.
# Values marked "est." are derived from the measured ones, not measured.
# Re-measure them when the runtime's I/O paths change.

NEXT_FRAME = 567264          # 311 lines of 1,824 cycles

# A data port write costs more or less by the VRAM region it lands in (the
# runtime keeps a converted copy of tiles, name table and sprite table).
# The region is not known statically, so a VRAM cost is a range over tile
# data, sprite table and name table. CRAM writes cost more and are not in the
# range. Each entry: (fixed cycles per instruction, cycles per byte).
VRAM_REGIONS = ('tile', 'sat', 'nt')
COST_VDATA = {
    'outn':  {'tile': (0, 1138), 'sat': (0, 956), 'nt': (0, 1328), 'cram': (0, 2885)},   # OUT (n),A
    'outc':  {'tile': (0, 1571), 'sat': (0, 1389), 'nt': (0, 1761), 'cram': (0, 3318)},   # OUT (C),r
    'outi':  {'tile': (0, 1871), 'sat': (0, 1689), 'nt': (0, 2061), 'cram': (0, 3618)},   # OUTI, OUTD
    # OTIR, and OUTI; JR NZ,-2 (the overlay makes it an OTIR)
    'otir':  {'tile': (3163, 24), 'sat': (3075, 25), 'nt': (4399, 235), 'cram': (1162, 651)},
    # a run of OUTI or OUTD in a row, done in one trap (tracedef.RUN_BREAK_EVEN).
    # A run of other outputs, or of OUTI mixed with them, costs more: 16
    # OUT ($BE),A 13,765 in tile data, 32 OUTI and OUT ($BE),A mixed 21,286.
    'run':   {'tile': (5998, 180), 'sat': (5919, 180), 'nt': (6352, 446), 'cram': (5917, 687)},
    # a trace (tools/tracedef.py): fixed per trap, per output on top of the
    # native code of the copy, which runs at native speed
    'trace': {'tile': (4240, 223), 'sat': (4910, 223), 'nt': (5800, 437), 'cram': (1890, 940)},
    'in':    {'tile': (0, 859), 'sat': (0, 859), 'nt': (0, 859), 'cram': (0, 859)},       # IN A,(n)
    'inc':   {'tile': (0, 1637), 'sat': (0, 1637), 'nt': (0, 1637), 'cram': (0, 1637)},   # IN r,(C), est.
    'ini':   {'tile': (0, 1833), 'sat': (0, 1833), 'nt': (0, 1833), 'cram': (0, 1833)},   # INI, IND
    'inir':  {'tile': (485, 1348), 'sat': (485, 1348), 'nt': (485, 1348), 'cram': (485, 1348)},  # est.
}
# The other port classes. 'other' is every class not named (no-effect writes,
# memory and I/O control, FM, unmapped reads). VDP control: the address byte
# pair; a register write costs more (up to 3,546 for register 2, which
# rebuilds the tilemaps).
COST_PORT = {
    'outn':  {'vdp_control': (0, 760), 'psg': (0, 1089), 'other': (0, 485)},
    'outc':  {'vdp_control': (0, 1120), 'psg': (0, 1522), 'other': (0, 1033)},    # psg est.
    'outi':  {'vdp_control': (0, 1493), 'psg': (0, 1822), 'other': (0, 1218)},    # est.
    'otir':  {'vdp_control': (1200, 1057), 'psg': (1587, 600), 'other': (1200, 300)},  # psg 4 bytes 3,987; rest est.
    'run':   {'vdp_control': (1200, 1057), 'psg': (1587, 600), 'other': (1200, 300)},  # est.
    'trace': {'vdp_control': (4240, 700), 'psg': (4240, 700), 'other': (4240, 300)},   # est.
    'in':    {'vdp_status': (0, 888), 'v_counter': (0, 832), 'h_counter': (0, 577),
              'joypad_a': (0, 639), 'joypad_b_misc': (0, 563), 'other': (0, 577)},
    'inc':   {'vdp_status': (0, 1666), 'v_counter': (0, 1610), 'h_counter': (0, 1355),
              'joypad_a': (0, 1417), 'joypad_b_misc': (0, 1341), 'other': (0, 1355)},  # status measured, rest est.
    'ini':   {'other': (0, 1355)},     # est.
    'inir':  {'other': (485, 870)},    # est.
}


class Cost:
    """Next cycles as a range lo..hi (the range comes from unknown VRAM regions);
    unk: a loop count on some path is unknown, and that loop is counted as one pass."""
    __slots__ = ('lo', 'hi', 'unk')

    def __init__(self, lo=0, hi=None, unk=False):
        self.lo, self.hi, self.unk = lo, (lo if hi is None else hi), unk

    def __add__(self, o):
        return Cost(self.lo + o.lo, self.hi + o.hi, self.unk or o.unk)

    def times(self, n):
        return Cost(self.lo * n, self.hi * n, self.unk)

    def most(self, o):
        return Cost(max(self.lo, o.lo), max(self.hi, o.hi), self.unk or o.unk)

    def txt(self):
        if self.lo == self.hi:
            return '%d' % self.lo
        return '%d-%d' % (self.lo, self.hi)


ZERO = Cost()

# Z80 T-states of the unprefixed opcodes $00-$3F and $C0-$FF; conditional
# branches as not taken. _TAKEN: the extra T-states when the branch is taken.
_T0 = [4, 10, 7, 6, 4, 4, 7, 4, 4, 11, 7, 6, 4, 4, 7, 4,
       8, 10, 7, 6, 4, 4, 7, 4, 12, 11, 7, 6, 4, 4, 7, 4,
       7, 10, 16, 6, 4, 4, 7, 4, 7, 11, 16, 6, 4, 4, 7, 4,
       7, 10, 13, 6, 11, 11, 10, 4, 7, 11, 13, 6, 4, 4, 7, 4]
_T3 = [5, 10, 10, 10, 10, 11, 7, 11, 5, 10, 10, 0, 10, 17, 7, 11,
       5, 10, 10, 11, 10, 11, 7, 11, 5, 4, 10, 11, 10, 0, 7, 11,
       5, 10, 10, 19, 10, 11, 7, 11, 5, 4, 10, 4, 10, 0, 7, 11,
       5, 10, 10, 4, 10, 11, 7, 11, 5, 6, 10, 4, 10, 0, 7, 11]


def _t_unprefixed(op):
    if op < 0x40:
        return _T0[op]
    if op < 0xC0:
        if op == 0x76:
            return 4
        return 7 if (op & 7) == 6 or 0x70 <= op < 0x78 else 4
    return _T3[op - 0xC0]


def tstates(raw):
    """Z80 T-states of an instruction, conditional branches not taken, block
    instructions for one pass."""
    op = raw[0]
    if op == 0xCB:
        b = raw[1]
        if b & 7 == 6:
            return 12 if 0x40 <= b < 0x80 else 15
        return 8
    if op == 0xED:
        b = raw[1]
        if 0xA0 <= b < 0xC0:
            return 21 if b >= 0xB0 else 16
        x = b & 0xC7
        if x in (0x40, 0x41):
            return 12
        if x == 0x42:
            return 15
        if x == 0x43:
            return 20
        if x == 0x45:
            return 14
        if b in (0x67, 0x6F):
            return 18
        if b in (0x47, 0x4F, 0x57, 0x5F):
            return 9
        return 8
    if op in (0xDD, 0xFD):
        b = raw[1]
        if b == 0xCB:
            return 20 if 0x40 <= raw[3] < 0x80 else 23
        if b in (0x34, 0x35):
            return 23
        if b == 0x36 or (0x40 <= b < 0xC0 and b != 0x76 and ((b & 7) == 6 or 0x70 <= b < 0x78)):
            return 19
        return _t_unprefixed(b) + 4
    return _t_unprefixed(op)


def taken_extra(ins):
    """Extra Next cycles when a conditional branch is taken."""
    t = ins.sem[0]
    if t in ('jr', 'djnz') and (t == 'djnz' or ins.sem[2]):
        return 5
    return 0


def mem_reads(ins):
    """Memory reads of an instruction: its own bytes plus the data it reads."""
    sem = ins.sem
    t = sem[0]
    n = len(ins.raw)

    def is_mem(o):
        return isinstance(o, tuple) and o[0] in ('mem', 'abs')
    if t == 'ld8' and is_mem(sem[2]):
        n += 1
    elif t == 'ld16' and isinstance(sem[2], tuple) and sem[2][0] == 'abs':
        n += 2
    elif t in ('pop', 'exsp', 'ret', 'reti'):
        n += 2
    elif t in ('alu', 'inc8', 'dec8') and is_mem(sem[-1] if t == 'alu' else sem[1]):
        n += 1
    elif t == 'cb' and is_mem(sem[3]):
        n += 1
    elif t == 'rxd':
        n += 1
    elif t == 'block' and sem[1][:2] in ('LD', 'CP', 'OU', 'OT'):
        n += 1
    return n


def native_cycles(ins):
    """Next cycles of a native instruction: its T-states plus one cycle per
    memory read (measured: writes and I/O add nothing, every read one)."""
    return tstates(ins.raw) + mem_reads(ins)


def port_index(p):
    """The runtime's port class number: A7 A6 A0."""
    return ((p >> 6) & 3) << 1 | (p & 1)


def trap_cost(form, pclass, count=1):
    """Cost of `count` outputs or inputs of one trap form to a port class
    (None: unknown), with the trap's fixed part once."""
    if pclass == 'vdp_data' or pclass is None:
        tab = COST_VDATA[form]
        vals = [tab[r][0] + tab[r][1] * count for r in VRAM_REGIONS]
        lo, hi = min(vals), max(vals)
        if pclass is None:
            other = COST_PORT[form]
            ov = [f + p * count for (f, p) in other.values()]
            lo, hi = min(lo, min(ov)), max(hi, max(ov))
        return Cost(lo, hi)
    tab = COST_PORT[form]
    f, p = tab.get(pclass, tab['other'])
    return Cost(f + p * count)


def nkey(n):
    """Sort key of a node (region, address): the region tag is a string, whose
    hash changes from run to run, so set order must never decide a result."""
    return (repr(n[0]), n[1])


TRACEDEF_OFF = [False]      # set by --no-tracedef


def load_tracedef():
    """tools/tracedef.py, from this script's own folder. Without it the trace
    costs differ from the overlay builder's, so a missing module is an error
    unless --no-tracedef was given (then None)."""
    if TRACEDEF_OFF[0]:
        return None
    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)
    try:
        import tracedef
    except ImportError as e:
        sys.exit('sitescan: cannot import tracedef.py from %s (%s); copy it next to sitescan.py, '
                 'or pass --no-tracedef to scan without it (the costs then differ)' % (here, e))
    return tracedef


class Loop:
    def __init__(self, header):
        self.header = header
        self.body = {header}
        self.latches = set()
        self.parent = None

    def body_sorted(self):
        return sorted(self.body, key=nkey)

    def latches_sorted(self):
        return sorted(self.latches, key=nkey)


class FrameCost:
    """Per-routine Next cost, interrupt context and interrupt state."""

    def __init__(self, sc, handlers=()):
        self.sc = sc
        self.calls_at = {}
        self._dedges = {}
        # calls from code reached by proven flow only
        self.callers = {}
        for callee, lst in sc.callers_prev.items():
            for (crt, cnode, cs) in lst:
                R = sc.routines.get(crt)
                if R is None or cnode not in self.dedges(R):
                    continue
                self.callers.setdefault(callee, []).append((crt, cnode, cs))
                self.calls_at.setdefault((crt, cnode), []).append(callee)
        for k, lst in self.calls_at.items():
            self.calls_at[k] = sorted(set(lst), key=nkey)
        self.io = {}            # node -> (form, classes or None)
        self.vdp_write = {}     # node -> 'data' / 'control'
        self._find_io()
        self.trace_info = self._traces()
        self.loops = {}
        self.memo = {}
        self.noret = set()      # routines with no path that returns
        self.evals = 0
        self.stop_ei = False    # paths end at the first EI (handler_to_ei)
        z = sc.region_for(0, 0)
        self.vec_irq = [(z, 0x0038), (z, 0x0066)] + list(handlers)
        # a jump from another routine into the reset code restarts the game: no
        # path through it returns
        R0 = sc.routines.get((z, 0x0000))
        self.reset_nodes = set(R0.nodes) if R0 is not None else set()
        self.irq_set = self._reach_live([e for e in self.vec_irq if e in sc.routines])
        # foreground: not reached from the handler, or called from code outside it
        self.fg_set = set(e for e in sc.routines if e not in self.vec_irq and
                          (e not in self.irq_set or
                           any(c not in self.irq_set for (c, _n, _s) in self.callers.get(e, ()))))
        self.iff_entry, self.iff_node = self._iff()

    def dedges(self, R):
        """R's edges of proven flow: not through a jump table whose length the
        scanner guessed (its entries past the real end are often data)."""
        d = self._dedges.get(R.entry)
        if d is None:
            d = {}
            work = [R.entry]
            while work:
                n = work.pop()
                if n in d:
                    continue
                d[n] = [x for x in R.edges.get(n, ()) if x[1] == 'd']
                work.extend(m for (m, _t) in d[n] if m not in d)
            self._dedges[R.entry] = d
        return d

    # ---- I/O sites

    def _c_values(self, n):
        vals = set()
        unknown = False
        for (rt, s, _h) in self.sc.ctx[n]:
            v = s['C']
            if isinstance(v, int):
                vals.add(v)
                continue
            for x in self.sc.resolve_multi(rt, [v], self.callers):
                if x is None:
                    unknown = True
                else:
                    vals.add(x[0])
        return vals, unknown

    def _find_io(self):
        sc = self.sc
        for n in sc.ctx:
            ins = sc.decode_node(n)
            sem = ins.sem
            t = sem[0]
            if t in ('outn', 'inn'):
                d = 'out' if t == 'outn' else 'in'
                ports, unk = {sem[1]}, False
                form = 'outn' if t == 'outn' else 'in'
            elif t in ('outC', 'inC') or (t == 'block' and (sem[1] in BLOCK_IN or sem[1] in BLOCK_OUT)):
                d = 'in' if (t == 'inC' or sem[1] in BLOCK_IN) else 'out'
                if t == 'outC':
                    form = 'outc'
                elif t == 'inC':
                    form = 'inc'
                elif sem[1] in ('OUTI', 'OUTD'):
                    form = 'outi'
                elif sem[1] in ('OTIR', 'OTDR'):
                    form = 'otir'
                elif sem[1] in ('INI', 'IND'):
                    form = 'ini'
                else:
                    form = 'inir'
                ports, unk = self._c_values(n)
            else:
                continue
            classes = set(port_class(p, d) for p in ports)
            if unk or not classes:
                classes.add(None)
            self.io[n] = (form, classes)
            if d == 'out':
                if 'vdp_data' in classes or None in classes:
                    self.vdp_write[n] = 'data'
                elif 'vdp_control' in classes:
                    self.vdp_write[n] = 'control'

    def _patched_reader(self, region):
        sc = self.sc
        sent = 0x1FF

        def rd(a):
            a &= 0xFFFF
            n = (region, a)
            if n in self.io:
                return sent
            p = (region, (a - 1) & 0xFFFF)
            if p in self.io:
                ins = sc.decode_node(p)
                if ins.sem[0] == 'outn':
                    return port_index(ins.sem[1])
                if ins.sem[0] == 'inn':
                    return 8 + port_index(ins.sem[1])
                return ins.raw[1]
            o = sc.off_of(region, a)
            return 0xFF if o is None else sc.rom[o]
        return rd, sent

    def _traces(self):
        """Output sites as the overlay patches them: 'otir' for OUTI; JR NZ,-2
        (or JP NZ to itself), 'run' or 'trace' for the trace forms tracedef
        chooses, else 'single'. Returns node -> (kind, region start, region end, loop)."""
        sc = self.sc
        out = {}
        tracedef = load_tracedef()
        readers = {}
        for n, (form, _cl) in sorted(self.io.items(), key=lambda x: (repr(x[0][0]), x[0][1])):
            region, a = n
            ins = sc.decode_node(n)
            if ins.sem[0] == 'block' and ins.sem[1] == 'OUTI':
                nx = sc.decode_node((region, (a + 2) & 0xFFFF))
                if nx is not None and nx.sem[0] in ('jr', 'jp') and nx.sem[1] == a and nx.sem[2] == 'NZ':
                    out[n] = ('otir', a, a + 2 + len(nx.raw), True)
                    continue
            if tracedef is None or form not in ('outn', 'outc', 'outi') or n in out:
                continue
            if region not in readers:
                readers[region] = self._patched_reader(region)
            rd, sent = readers[region]
            try:
                if not tracedef.choose(rd, a, sent):
                    continue
                v = tracedef.verdict(rd, a, sent)
            except (IndexError, TypeError):
                continue
            if v[0] == 'run':
                # the call does the whole run: every site in it is part of the run
                for i in range(v[1]):
                    out[(region, (a + 2 * i) & 0xFFFF)] = ('run', a + 2 * i, a + 2 * i + 2, False)
            elif v[0] == 'copy':
                out[n] = ('trace', v[1], v[2], v[4])
        return out

    # ---- call graph

    def _reach(self, roots, stop=()):
        seen = set()
        work = list(roots)
        adj = {}
        for (a, n), bs in self.calls_at.items():
            adj.setdefault(a, set()).update(bs)
        while work:
            e = work.pop()
            if e in seen:
                continue
            seen.add(e)
            for m in adj.get(e, ()):
                if m not in seen and m not in stop:
                    work.append(m)
        return seen

    def live_nodes(self, R):
        """Nodes of R from which a return to the caller can be reached."""
        preds = {}
        exits = []
        for n, es in self.dedges(R).items():
            for (m, _t) in es:
                preds.setdefault(m, set()).add(n)
        for n in self.dedges(R):
            ins = self.sc.decode_node(n)
            if ins is not None and self.is_exit(R, n, ins):
                exits.append(n)
        live = set()
        exits = [n for n in exits if n not in self.reset_nodes or R.entry[1] == 0x0000]
        while exits:
            n = exits.pop()
            if n in live:
                continue
            live.add(n)
            exits.extend(preds.get(n, ()))
        return live

    def _reach_live(self, roots):
        """Routines called on paths that return, from the roots on: the code an
        interrupt handler runs before it returns."""
        seen = set()
        work = list(roots)
        while work:
            e = work.pop()
            if e in seen:
                continue
            seen.add(e)
            R = self.sc.routines[e]
            for n in self.live_nodes(R):
                for m in self.calls_at.get((e, n), ()):
                    if m not in seen:
                        work.append(m)
        return seen

    # ---- interrupt enable state

    def _iff(self):
        """IFF1 at each routine entry and node: a set of 'on', 'off', 'unknown'."""
        sc = self.sc
        z = sc.region_for(0, 0)
        entry = {}
        for e, R in sc.routines.items():
            if e in self.vec_irq or e == (z, 0x0000):
                entry[e] = {'off'}
            elif not self.callers.get(e):
                entry[e] = {'unknown'}
            else:
                entry[e] = set()
        effect = {e: {'in'} for e in sc.routines}      # exit state in terms of 'in' (= entry state)
        node_rel = {}
        for _ in range(12):
            changed = False
            for e, R in sc.routines.items():
                rel = self._iff_routine(R, effect)
                node_rel[e] = rel
                ex = set()
                for n, v in rel.items():
                    ins = sc.decode_node(n)
                    if ins is not None and ins.sem[0] in ('ret', 'reti'):
                        ex |= v
                if not ex:
                    ex = {'in'}
                if ex != effect[e]:
                    effect[e] = ex
                    changed = True
            if not changed:
                break
        for _ in range(64):
            changed = False
            for callee, lst in self.callers.items():
                if callee not in entry or callee in self.vec_irq:
                    continue
                for (crt, cnode, _cs) in lst:
                    rel = node_rel.get(crt, {}).get(cnode, {'in'})
                    v = set()
                    for x in rel:
                        v |= entry.get(crt, {'unknown'}) if x == 'in' else {x}
                    if not v <= entry[callee]:
                        entry[callee] |= v
                        changed = True
            if not changed:
                break
        node = {}
        for e, rel in node_rel.items():
            for n, v in rel.items():
                r = set()
                for x in v:
                    r |= (entry[e] or {'unknown'}) if x == 'in' else {x}
                node[(e, n)] = r
        return entry, node

    def _iff_routine(self, R, effect):
        sc = self.sc
        st = {R.entry: {'in'}}
        work = [R.entry]
        while work:
            n = work.pop()
            ins = sc.decode_node(n)
            if ins is None:
                continue
            v = st[n]
            if ins.text == 'DI':
                v = {'off'}
            elif ins.text == 'EI':
                v = {'on'}
            elif ins.sem[0] in ('call', 'rst'):
                callees = self.calls_at.get((R.entry, n), ())
                if callees:
                    nv = set()
                    for c in callees:
                        for x in effect.get(c, {'in'}):
                            nv |= v if x == 'in' else {x}
                    v = nv
            for (m, _tag) in self.dedges(R).get(n, ()):
                old = st.get(m)
                if old is None or not v <= old:
                    st[m] = (old or set()) | v
                    work.append(m)
        return st

    # ---- loops

    def _loops(self, R):
        got = self.loops.get(R.entry)
        if got is not None:
            return got
        edges = self.dedges(R)
        preds = {}
        for n, es in edges.items():
            for (m, _t) in es:
                preds.setdefault(m, set()).add(n)
        back = set()
        state = {}
        stack = [(R.entry, iter(edges.get(R.entry, ())))]
        state[R.entry] = 1
        while stack:
            n, it = stack[-1]
            for (m, _t) in it:
                s = state.get(m)
                if s is None:
                    state[m] = 1
                    stack.append((m, iter(edges.get(m, ()))))
                    break
                if s == 1:
                    back.add((n, m))
            else:
                state[n] = 2
                stack.pop()
        loops = {}
        for (u, h) in sorted(back, key=lambda b: (nkey(b[0]), nkey(b[1]))):
            L = loops.get(h)
            if L is None:
                L = loops[h] = Loop(h)
            L.latches.add(u)
            work = [u]
            while work:
                x = work.pop()
                if x in L.body:
                    continue
                L.body.add(x)
                work.extend(preds.get(x, ()))
        order = sorted(loops.values(), key=lambda L: (len(L.body), nkey(L.header)))
        for i, L in enumerate(order):
            for P in order[i + 1:]:
                if L.header in P.body and P is not L and L.body <= P.body | {L.header}:
                    L.parent = P
                    break
        inner = {}
        for L in order:            # smallest first: the innermost loop of a node
            for x in L.body_sorted():
                inner.setdefault(x, L)
        res = (loops, inner, preds, back)
        self.loops[R.entry] = res
        return res

    def _counter(self, R, L, preds):
        """The register (or pair) a loop counts down to zero in, or None."""
        sc = self.sc
        for u in L.latches_sorted():
            ins = sc.decode_node(u)
            t = ins.sem[0]
            if t == 'djnz':
                return 'B'
            if t not in ('jr', 'jp') or ins.sem[2] != 'NZ':
                continue
            x = u
            seen = 0
            pend_pop = False
            nexx = 0        # EXX between the latch and the counter: the count is in a shadow register
            while seen < 24:
                seen += 1
                ps = [p for p in preds.get(x, ()) if p in L.body]
                if len(ps) != 1:
                    break
                x = ps[0]
                pi = sc.decode_node(x)
                s = pi.sem
                k = s[0]
                if k == 'pop' and s[1] == 'AF':
                    pend_pop = True
                    continue
                if k == 'push' and s[1] == 'AF' and pend_pop:
                    pend_pop = False
                    continue
                if pend_pop:
                    break
                if k == 'exx':
                    nexx += 1
                if k in ('ld8', 'ld16', 'push', 'pop', 'inc16', 'dec16', 'exde', 'exx', 'outn', 'outC', 'nop', 'st16') \
                        and pi.text not in ('LD A,I', 'LD A,R'):
                    continue            # these leave the flags alone
                if k == 'block' and s[1] in ('OUTI', 'OUTD', 'INI', 'IND'):
                    return None if nexx % 2 else 'B'
                if k == 'dec8' and isinstance(s[1], str) and s[1] in R8 and s[1] != '(HL)':
                    return None if nexx % 2 else s[1]
                if k == 'alu' and s[1] == 'OR' and isinstance(s[2], str):
                    # DEC rr; LD A,hi; OR lo: a 16-bit count
                    q = [p for p in preds.get(x, ()) if p in L.body]
                    if len(q) == 1:
                        li = sc.decode_node(q[0])
                        if li.sem[0] == 'ld8' and li.sem[1] == 'A' and isinstance(li.sem[2], str):
                            for name, hl in PAIRS.items():
                                if set(hl) == {li.sem[2], s[2]}:
                                    return name
                break
        return None

    def _value(self, R, n, reg, env, need, counter=False):
        """Largest value of reg (8-bit register or pair) at node n over the
        routine's states; None if unknown. counter: n is the head of a loop that
        counts reg down, and its states hold the passes the scanner unrolled
        (v, v-1, ...); only a value whose successor is not there is an entry value."""
        sc = self.sc
        if counter:
            vals = []
            for (rt, s, _h) in sc.ctx.get(n, ()):
                if rt == R.entry:
                    vals.append(self._value_in(s, reg, env, need))
            ints = set(v for v in vals if isinstance(v, int))
            mask = 0xFFFF if reg in PAIRS else 0xFF
            ents = [v for v in ints if ((v + 1) & mask) not in ints]
            return max(ents) if ents else None
        best = None
        for (rt, s, _h) in sc.ctx.get(n, ()):
            if rt != R.entry:
                continue
            if reg in PAIRS:
                h, lo = PAIRS[reg]
                hv, lv = self._resolve(s[h], env, need), self._resolve(s[lo], env, need)
                v = (hv << 8 | lv) if isinstance(hv, int) and isinstance(lv, int) else None
            else:
                v = self._resolve(s[reg], env, need)
            if v is None:
                continue
            best = v if best is None else max(best, v)
        return best

    def _value_in(self, s, reg, env, need):
        if reg in PAIRS:
            h, lo = PAIRS[reg]
            hv, lv = self._resolve(s[h], env, need), self._resolve(s[lo], env, need)
            return (hv << 8 | lv) if isinstance(hv, int) and isinstance(lv, int) else None
        return self._resolve(s[reg], env, need)

    @staticmethod
    def _resolve(v, env, need):
        if isinstance(v, int):
            return v
        if isinstance(v, tuple) and v[0] == 'arg':
            x = env.get(v[1])
            if x is None:
                need.add(v[1])
            return x
        return None

    # ---- cost

    def node_cost(self, R, n, env, need, stack):
        sc = self.sc
        ins = sc.decode_node(n)
        if ins is None:
            return ZERO
        c = Cost(native_cycles(ins))
        io = self.io.get(n)
        tr = self.trace_info.get(n)
        if io is not None:
            form, classes = io
            if tr is not None and tr[0] == 'otir':
                c = ZERO            # the loop around it carries the cost (see loop_total)
            elif form in ('otir', 'inir'):
                cnt = self._value(R, n, 'B', env, need)
                k = None
                for cl in classes:
                    tc = trap_cost(form, cl, 1 if cnt is None else (cnt or 256))
                    k = tc if k is None else k.most(tc)
                c = Cost(k.lo, k.hi, cnt is None)
            else:
                f = form
                if tr is not None:
                    f = tr[0]
                k = None
                for cl in classes:
                    if tr is not None:
                        tc = trap_cost(f, cl, 1)
                        fx = trap_cost(f, cl, 0)
                        tc = Cost(tc.lo - fx.lo, tc.hi - fx.hi)
                        if not self._trace_covered(n, tr):
                            tc = tc + fx
                    else:
                        tc = trap_cost(f, cl, 1)
                    k = tc if k is None else k.most(tc)
                c = c + k
        elif ins.sem[0] == 'block' and ins.sem[1] in ('LDIR', 'LDDR', 'CPIR', 'CPDR'):
            cnt = self._value(R, n, 'BC', env, need)
            per = 21 + 3
            if cnt is None:
                c = Cost(per, per, True)
            else:
                c = Cost(per * (cnt or 0x10000) - 5)
        callees = self.calls_at.get((R.entry, n))
        if callees:
            best = None
            for e in callees:
                ce = self.callee_env(R, n, env, need)
                k = self.routine_cost(e, ce, stack, need, (R.entry, n))
                best = k if best is None else best.most(k)
            c = c + best
        return c

    def _trace_covered(self, n, tr):
        """A trace site inside the region of another trace that starts earlier
        (or a later OUTI of a run): it runs inside that trap."""
        region, a = n
        if tr[0] == 'run':
            p = self.trace_info.get((region, (a - 2) & 0xFFFF))
            return p is not None and p[0] == 'run'
        if tr[0] == 'trace' and tr[3]:
            return True         # a loop trace: the loop carries the fixed part
        for d in range(2, 120):
            p = self.trace_info.get((region, (a - d) & 0xFFFF))
            if p is not None and p[0] == 'trace' and p[1] <= a < p[2]:
                return True
        return False

    def callee_env(self, R, n, env, need):
        sc = self.sc
        out = {}
        for r in ('A', 'B', 'C', 'D', 'E', 'H', 'L'):
            vals = set()
            ok = True
            for (rt, s, _h) in sc.ctx.get(n, ()):
                if rt != R.entry:
                    continue
                v = s[r]
                if isinstance(v, int):
                    vals.add(v)
                elif isinstance(v, tuple) and v[0] == 'arg' and env.get(v[1]) is not None:
                    vals.add(env[v[1]])
                else:
                    ok = False
            if ok and vals:
                out[r] = max(vals)
        return out

    def routine_cost(self, e, env, stack, need_up=None, at=None):
        """Worst-case cost of one call of routine e with the given entry values.
        Entry values the routine's loop counts need and env lacks are added to
        need_up when the caller (at = (caller entry, call node)) passes them on."""
        R = self.sc.routines.get(e)
        if R is None or e in stack or len(stack) > 40:
            return ZERO
        key = (e, tuple(sorted(env.items())))
        hit = self.memo.get(key)
        if hit is None:
            self.evals += 1
            need = set()
            stack = stack | {e}
            c = self._path(R, None, R.entry, env, need, stack, {}, set(), False)
            if c is None:
                self.noret.add(e)
                c = self._path(R, None, R.entry, env, need, stack, {}, set(), True)
            hit = self.memo[key] = (c, frozenset(need))
        c, need = hit
        if need and need_up is not None and at is not None:
            crt, cnode = at
            for (rt, s, _h) in self.sc.ctx.get(cnode, ()):
                if rt != crt:
                    continue
                for r in need:
                    v = s[r]
                    if isinstance(v, tuple) and v[0] == 'arg':
                        need_up.add(v[1])
        return c

    def is_exit(self, R, n, ins):
        """A return to the routine's caller, or a RET on a stack the routine
        switched to (the end of an interrupt handler that restores SP, or a task
        switch); not a jump through a pushed address."""
        if ins.sem[0] not in ('ret', 'reti'):
            return False
        nxt = (n[0], (n[1] + len(ins.raw)) & 0xFFFF)
        return all(m == nxt for (m, _t) in self.dedges(R).get(n, ()))

    def _path(self, R, ctx, n, env, need, stack, memo, active, anyend):
        """Longest cost from node n to a return of the routine (ctx None) or to
        the end of one pass of loop ctx; None when no such path exists. With
        anyend, a path may also end where the scanner lost the flow."""
        if n in memo:
            return memo[n]
        if n in active:
            return ZERO if anyend else None
        loops, inner, preds, back = self._loops(R)
        # the outermost loop inside ctx that holds n
        L, x = None, inner.get(n)
        while x is not None and x is not ctx:
            L, x = x, x.parent
        if x is not ctx:
            L = None
        if L is not None and self.stop_ei and any(
                (d := self.sc.decode_node(b)) is not None and d.text == 'EI' for b in L.body):
            L = None            # one pass is counted, up to the EI
        active.add(n)
        opts = []
        if L is not None:
            c = self.loop_total(R, L, env, need, stack)
            for x in L.body_sorted():
                for (m, _t) in self.dedges(R).get(x, ()):
                    if m in L.body:
                        continue
                    if ctx is not None and (m == ctx.header or m not in ctx.body):
                        opts.append(ZERO)
                        continue
                    r = self._path(R, ctx, m, env, need, stack, memo, active, anyend)
                    if r is not None:
                        opts.append(r)
                ins = self.sc.decode_node(x)
                if ins is not None and self.is_exit(R, x, ins):
                    opts.append(ZERO)
        else:
            c = self.node_cost(R, n, env, need, stack)
            ins = self.sc.decode_node(n)
            es = self.dedges(R).get(n, ()) if ins is not None else ()
            if ins is not None and self.is_exit(R, n, ins):
                opts.append(ZERO)
            if self.stop_ei and ins is not None and ins.text == 'EI':
                es = ()
                opts.append(ZERO)
            for (m, _t) in es:
                if m in self.reset_nodes and R.entry[1] != 0x0000 and n not in self.reset_nodes:
                    continue
                extra = Cost(taken_extra(ins)) if ins.sem[0] in ('jr', 'djnz') and m[1] == ins.sem[1] else ZERO
                if ctx is not None and (m == ctx.header or m not in ctx.body):
                    opts.append(extra)
                    continue
                r = self._path(R, ctx, m, env, need, stack, memo, active, anyend)
                if r is not None:
                    opts.append(extra + r)
            if not es and anyend:
                opts.append(ZERO)
        if not opts and anyend:
            opts.append(ZERO)
        res = None
        if opts:
            best = opts[0]
            for o in opts[1:]:
                best = best.most(o)
            res = c + best
        active.discard(n)
        memo[n] = res
        return res

    def loop_count(self, R, L, env, need):
        loops, inner, preds, back = self._loops(R)
        reg = self._counter(R, L, preds)
        if reg is None:
            return None, None
        # a loop inside L that counts down the same register uses up the count:
        # L's passes and the inner passes share it, so L counts as one pass
        regs = set(PAIRS.get(reg, (reg,)))
        for M in loops.values():
            if M is L or M.header not in L.body:
                continue
            P = M.parent
            while P is not None and P is not L:
                P = P.parent
            if P is None:
                continue
            r2 = self._counter(R, M, preds)
            if r2 is not None and regs & set(PAIRS.get(r2, (r2,))):
                return reg, 1
        v = self._value(R, L.header, reg, env, need, counter=True)
        if v is None:
            return reg, None
        return reg, (v or (0x10000 if reg in PAIRS else 0x100))

    def loop_total(self, R, L, env, need, stack):
        reg, cnt = self.loop_count(R, L, env, need)
        tr = self.trace_info.get(L.header)
        if tr is not None and tr[0] == 'otir':
            # OUTI; JR NZ,-2: one OTIR trap for the whole loop
            k = None
            for cl in self.io[L.header][1]:
                tc = trap_cost('otir', cl, 1 if cnt is None else cnt)
                k = tc if k is None else k.most(tc)
            return Cost(k.lo, k.hi, cnt is None)
        loops, inner, preds, back = self._loops(R)
        p = self._path(R, L, L.header, env, need, stack, {}, set(), True)
        fixed = ZERO
        for x in L.body_sorted():
            t = self.trace_info.get(x)
            if t is not None and t[0] == 'trace' and t[3] and inner.get(x) is L:
                for cl in self.io[x][1]:
                    fixed = fixed.most(trap_cost('trace', cl, 0))
        if cnt is None:
            return fixed + Cost(p.lo, p.hi, True)
        return fixed + p.times(cnt)

    def loop_report(self, R, env):
        """(header, count register, count, cost of one pass) for the routine's outer loops."""
        loops, inner, preds, back = self._loops(R)
        out = []
        need = set()
        for L in sorted(loops.values(), key=lambda L: nkey(L.header)):
            if L.parent is not None:
                continue
            reg, cnt = self.loop_count(R, L, env, need)
            p = self._path(R, L, L.header, env, need, frozenset({R.entry}), {}, set(), True)
            out.append((L.header, reg, cnt, p))
        return out

    def evaluate(self, e):
        """Worst cost of routine e over the entry values its callers pass:
        (cost, env used, partial) where partial means some callers pass values
        the scanner does not know."""
        c = self.routine_cost(e, {}, frozenset(), None, None)
        hit = self.memo.get((e, ()))
        need = set(hit[1]) if hit else set()
        if not need:
            return c, {}, False
        regs = sorted(need)
        combos = self.sc.resolve_multi(e, [('arg', r) for r in regs], self.callers)
        best, benv, partial = None, {}, not combos
        for x in combos[:64]:
            if x is None:
                partial = True
                continue
            env = dict(zip(regs, x))
            k = self.routine_cost(e, env, frozenset(), None, None)
            if best is None or (k.unk, -k.hi) < (best.unk, -best.hi):
                best, benv = k, env
        if best is None:
            return c, {}, True
        return best, benv, partial

    def own_vdp_iff_on(self, e):
        """Whether routine e's own instructions write the VDP with interrupts on."""
        R = self.sc.routines[e]
        return any(n in self.vdp_write and 'on' in self.iff_node.get((e, n), ()) for n in self.dedges(R))

    def writes_ctrl(self, roots):
        for e in roots:
            R = self.sc.routines.get(e)
            if R is None:
                continue
            for n in self.dedges(R):
                if self.vdp_write.get(n) == 'control' or (n in self.io and 'vdp_control' in self.io[n][1]):
                    return True
        return False


def frame_cost(sc, handlers):
    """Run the frame cost model. Returns a dict for write_outputs."""
    sys.setrecursionlimit(max(sys.getrecursionlimit(), 20000))
    fc = FrameCost(sc, handlers)
    z = sc.region_for(0, 0)
    rows = {}
    for e in sorted(sc.routines, key=lambda x: (repr(x[0]), x[1])):
        c, env, partial = fc.evaluate(e)
        rows[e] = (c, env, partial)
    irq_roots = [e for e in fc.vec_irq if e in sc.routines]
    handler = ZERO
    for e in irq_roots:
        if e[1] == 0x0038 or e in handlers:
            handler = handler.most(rows[e][0])
    ctrl = fc.writes_ctrl(fc.irq_set)
    # a write sequence longer than the time between the handler's end and the
    # next frame interrupt is cut by the handler. When the handler's own worst
    # case is a frame or more, the frame alone is the limit.
    limit = NEXT_FRAME - handler.lo if handler.lo < NEXT_FRAME else NEXT_FRAME

    def callees(e):
        R = sc.routines[e]
        out = set()
        for n in fc.dedges(R):
            out.update(fc.calls_at.get((e, n), ()))
        return out
    race, overrun = [], []
    for e, (c, env, partial) in rows.items():
        if e in fc.fg_set and e not in fc.irq_set and ctrl and c.hi > limit and fc.own_vdp_iff_on(e):
            if all(rows[x][0].hi <= limit or x == e for x in callees(e) if x in rows):
                race.append(e)
        if e in fc.irq_set and c.hi > NEXT_FRAME:
            if all(rows[x][0].hi <= NEXT_FRAME or x == e for x in callees(e) if x in rows):
                overrun.append(e)
    to_ei = handler_to_ei(fc, [e for e in irq_roots if e[1] == 0x0038 or e in handlers])
    return {'fc': fc, 'rows': rows, 'handler': handler, 'handler_ctrl': ctrl, 'limit': limit,
            'race': race, 'overrun': overrun, 'irq_roots': irq_roots, 'to_ei': to_ei}


LINE_CYCLES = 1824      # one Next line: 28 MHz, 448 x 311 at 50 Hz
FRAME_EVENT_LINE = 192  # the SMS frame interrupt: the end of line 192
ULA_IRQ_LINE = 248      # the Next ULA interrupt


def handler_to_ei(fc, roots):
    """Worst-case Next cycles from the entry of the game's interrupt handler (the
    maskable interrupt enters with interrupts off) to its first EI, or to its
    return when no EI comes first. A called routine counts in full, up to its
    own first EI. Returns the Cost, or None when there is no handler."""
    if not roots:
        return None
    saved = fc.memo, fc.noret
    fc.memo, fc.noret, fc.stop_ei = {}, set(), True
    try:
        best = None
        for e in roots:
            c = fc.routine_cost(e, {}, frozenset(), None, None)
            best = c if best is None else best.most(c)
    finally:
        fc.memo, fc.noret, fc.stop_ei = saved[0], saved[1], False
    return best


def write_cost(res, name, out, w):
    """NAME.cost.tsv and the frame cost section of the summary."""
    cm = res.get('cost')
    if cm is None:
        return
    sc, fc, rows = res['sc'], cm['fc'], cm['rows']

    def where(e):
        return '%s bank %s' % (h4(e[1]), node_bank_s(e))

    def ctx_of(e):
        i, f = e in fc.irq_set, e in fc.fg_set
        return 'both' if i and f else 'irq' if i else 'fg' if f else '-'

    def iff_of(e):
        v = fc.iff_entry.get(e) or {'unknown'}
        return 'mixed' if {'on', 'off'} <= v else '/'.join(sorted(v))

    def vdp_of(e):
        k = set(fc.vdp_write.get(n) for n in fc.dedges(sc.routines[e])) - {None}
        return '+'.join(sorted(k)) or '-'

    def count_of(c, partial):
        return 'unknown' if c.unk else 'partial' if partial else 'known'

    def args_of(env):
        return ' '.join('%s=%s' % (r, h2(v)) for r, v in sorted(env.items()))

    def loops_of(e, env):
        txt = []
        for (hd, reg, cnt, p) in fc.loop_report(sc.routines[e], env):
            txt.append('%s x%s %s' % (h4(hd[1]), cnt if cnt is not None else '?', p.txt()))
        return ', '.join(txt)

    cols = ['entry', 'bank', 'offset', 'context', 'iff', 'vdp', 'returns', 'cost_lo', 'cost_hi', 'frames', 'count', 'args', 'loops']
    with open(os.path.join(out, name + '.cost.tsv'), 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for e, (c, env, partial) in sorted(rows.items(), key=lambda x: (-x[1][0].hi, nkey(x[0]))):
            f.write('\t'.join([h4(e[1]), node_bank_s(e), fmt_off(sc.off_of(e[0], e[1])), ctx_of(e), iff_of(e),
                                vdp_of(e), 'no' if e in fc.noret else 'yes', str(c.lo), str(c.hi), '%.3f' % (c.hi / NEXT_FRAME),
                                count_of(c, partial), args_of(env), loops_of(e, env)]) + '\n')

    def line(e):
        c, env, partial = rows[e]
        x = '    %s: %s cycles (%.2f frames), counts %s' % (where(e), c.txt(), c.hi / NEXT_FRAME, count_of(c, partial))
        if env:
            x += ', with ' + args_of(env)
        lp = loops_of(e, env)
        if lp:
            x += '; loops ' + lp
        return x

    w('Frame cost (Next cycles; a Next frame is %d):' % NEXT_FRAME)
    h = cm['handler']
    w('  interrupt handler: %s cycles (%.2f frames) from %s; it %s the VDP control port' %
      (h.txt(), h.hi / NEXT_FRAME, ', '.join(h4(e[1]) for e in cm['irq_roots']) or 'no vector',
       'writes' if cm['handler_ctrl'] else 'does not write'))
    te = cm.get('to_ei')
    if te is not None:
        def lines(c):
            return '%.1f' % (c / LINE_CYCLES)
        end_lo = FRAME_EVENT_LINE + te.lo / LINE_CYCLES
        end_hi = FRAME_EVENT_LINE + te.hi / LINE_CYCLES
        cost = lines(te.lo) if te.lo == te.hi else '%s to %s' % (lines(te.lo), lines(te.hi))
        until = '%.1f' % end_hi if te.lo == te.hi else '%.1f to %.1f' % (end_lo, end_hi)
        flag = ''
        if end_lo > ULA_IRQ_LINE:
            flag = ': TEAR RISK, even the cheapest path runs past line %d' % ULA_IRQ_LINE
        elif end_hi > ULA_IRQ_LINE:
            flag = ': the costliest path runs past line %d, the cheapest does not' % ULA_IRQ_LINE
        w('  interrupt handler to its EI: %s cycles (%s Next lines at %d cycles a line); the frame event is the end of line %d, '
          'so interrupts stay off until line %s; the ULA interrupt is at line %d%s' %
          (te.txt(), cost, LINE_CYCLES, FRAME_EVENT_LINE, until, ULA_IRQ_LINE, flag))
    w('  race: foreground routines that write the VDP with interrupts on and cost more than %d (%s): %d' %
      (cm['limit'], 'the frame minus the handler' if cm['limit'] < NEXT_FRAME else
       'the frame; the handler\'s worst case is a frame or more', len(cm['race'])))
    for e in sorted(cm['race'], key=lambda e: -rows[e][0].hi):
        w(line(e))
    w('  overrun: interrupt routines that cost more than a frame: %d' % len(cm['overrun']))
    for e in sorted(cm['overrun'], key=lambda e: -rows[e][0].hi):
        w(line(e))
    top = [e for e in rows if e in fc.fg_set and e not in fc.irq_set and e not in fc.noret and fc.own_vdp_iff_on(e)]
    top.sort(key=lambda e: -rows[e][0].hi)
    if top:
        w('  costliest foreground routines that write the VDP with interrupts on:')
        for e in top[:8]:
            w(line(e))
    w('')


# ------------------------------------------------------------------ pattern rules
#
# Code shapes found in particular games that cost time or break on the Next.
# Each rule adds its own rows to NAME.sites.tsv and a section to the summary;
# no rule changes the rows of the main scan. docs/sitescan.md describes them.

RULE_CAP = 2 * NEXT_FRAME       # time searches stop here


def _ram_addr(a):
    return isinstance(a, int) and 0xC000 <= a < 0x10000


def _vals(sc, rt, v):
    """Ints a value can have at a node of routine rt (its own constant, or
    through the callers); empty when unknown."""
    if isinstance(v, int):
        return {v}
    if isinstance(v, tuple) and sc._argform(v):
        return set(x[0] for x in sc.resolve_multi(rt, [v], sc.callers_prev) if x is not None)
    return set()


def _mem_addrs(sc, rt, s, o):
    """Addresses of a memory operand ('abs', nn) or ('mem', reg, d) in state s."""
    if o[0] == 'abs':
        return {o[1]}
    if o[0] == 'mem':
        return set((v + o[2]) & 0xFFFF for v in _vals(sc, rt, pget(s, o[1])))
    return set()


# ---- rule 1: A-indexed inline jump tables after an RST or CALL

def _linear(sc, node, depth, limit=40):
    """The instructions from node on in run order, following unconditional
    JP nn and expanding calls into short helpers that end in RET; None when
    the code branches or does not decode."""
    seq = []
    n = node
    for _ in range(limit):
        ins = sc.decode_node(n)
        if ins is None or ins.sem[0] == 'bad':
            return None
        t = ins.sem[0]
        nxt = (n[0], (n[1] + len(ins.raw)) & 0xFFFF)
        if t in ('call', 'rst') and (t == 'rst' or ins.sem[2] is None):
            if depth >= 2:
                return None
            tgt = ins.sem[1]
            same = n[0][0] == 'rom' and n[0][1] == tgt >> 14
            sub = _linear(sc, (sc.region_for(tgt >> 14, n[0][2] if same else tgt >> 14), tgt), depth + 1, 16)
            if sub is None or not sub or sub[-1].sem[0] != 'ret':
                return None
            seq += sub[:-1]
            n = nxt
            continue
        if t == 'jp' and ins.sem[2] is None:
            n = (n[0], ins.sem[1])
            continue
        if t in ('jp', 'jr', 'djnz', 'call') or (t == 'ret' and ins.sem[1] is not None):
            return None
        seq.append(ins)
        if t in ('ret', 'reti', 'jpind'):
            return seq
        n = nxt
    return None


def inline_dispatcher(sc, node):
    """True when the routine at node takes its return address, adds twice A
    to it, reads the word there and jumps to it: a table of words follows each
    call, indexed by A."""
    seq = _linear(sc, node, 0)
    if not seq or seq[-1].sem[0] not in ('ret', 'jpind'):
        return False
    i = 0
    while i < len(seq) and seq[i].sem[0] == 'push' and seq[i].sem[1] != 'HL':
        i += 1
    if i >= len(seq) or seq[i].text not in ('EX (SP),HL', 'POP HL'):
        return False
    rest = seq[i + 1:]
    twice = sum(1 for x in rest if x.text in ('ADD A,A', 'SLA A', 'RLCA', 'ADD HL,HL'))
    adds = sum(1 for x in rest if x.text in ('ADD HL,DE', 'ADD HL,BC'))
    loads = sum(1 for x in rest if x.sem[0] == 'ld8' and x.sem[2] == ('mem', 'HL', 0))
    if not (twice or adds >= 2) or loads < 2:
        return False
    if seq[-1].sem[0] == 'jpind':
        return True
    return any(x.text in ('EX (SP),HL', 'PUSH HL', 'PUSH DE') for x in rest)


def _block_starts(sc):
    """ROM offsets where the listing starts a new run of code."""
    spans = sorted(set((sc.off_of(n[0], n[1]), len(sc.decode_node(n).raw)) for n in sc.ctx
                       if sc.off_of(n[0], n[1]) is not None))
    out = set()
    prev = None
    for o, ln in spans:
        if prev is None or o > prev:
            out.add(o)
        prev = max(prev or 0, o + ln)
    return out


def _prev_insn(sc, ends, n):
    m = ends.get((n[0], n[1]))
    return (m, sc.decode_node(m)) if m is not None else (None, None)


def inline_tables(sc, disp, bound):
    """Read the table after every call of the dispatchers in disp.
    Returns a list of (site node, dispatcher, table start, mask, words, end reason)."""
    ends = {}
    for n in sc.ctx:
        ins = sc.decode_node(n)
        ends[(n[0], (n[1] + len(ins.raw)) & 0xFFFF)] = n
    out = []
    for d in disp:
        sites = set(cn for (_crt, cn, _cs) in sc.callers_prev.get(d, ()))
        for cn in sorted(sites, key=lambda x: (repr(x[0]), x[1])):
            ins = sc.decode_node(cn)
            region, a = cn
            t0 = (a + len(ins.raw)) & 0xFFFF
            o0 = sc.off_of(region, t0)
            if o0 is None:
                continue
            mask = None
            p, pi = _prev_insn(sc, ends, cn)
            if pi is not None and pi.text == 'DEC A':
                p, pi = _prev_insn(sc, ends, p)
            if pi is not None and pi.sem[0] == 'alu' and pi.sem[1] == 'AND' and pi.sem[2][0] == 'imm':
                m = pi.sem[2][1]
                if (m + 1) & m == 0:
                    mask = m + 1
            hi = 0x7FFF if a < 0x8000 else 0xBFFF
            bank = region[2] if region[0] == 'rom' else None
            words = []
            limit = 0x10000
            why = '128 entries'
            for k in range(mask or 128):
                if t0 + 2 * k >= limit:
                    why = 'reached the lowest target after the table'
                    break
                o = o0 + 2 * k
                if o + 1 >= sc.size:
                    why = 'end of the cart'
                    break
                if k and (o in bound or o + 1 in bound):
                    why = 'reached known code'
                    break
                w = sc.rom[o] | sc.rom[o + 1] << 8
                if not (0x100 <= w <= hi):
                    why = 'word %s is not a code address' % h4(w)
                    break
                if words and (w > max(words) + 0x800 or w < min(words) - 0x800):
                    why = 'word %s is far from the others' % h4(w)
                    break
                words.append(w)
                if t0 < w < limit:
                    limit = w
            else:
                if mask:
                    why = 'AND %s before the call' % h2(mask - 1)
            out.append((cn, d, t0, mask, words, why, bank))
    return out


def _word_node(sc, w, site):
    region = site[0]
    slot = w >> 14
    if slot == 2:
        if region[0] != 'rom' or region[1] != 2:
            return None
        return (sc.region_for(2, region[2]), w)
    return (sc.region_for(slot, slot), w)


def _word_off(sc, w, site):
    n = _word_node(sc, w, site)
    return None if n is None else sc.off_of(n[0], n[1])


SITE_KINDS_NEW = ('out', 'in', 'out_c', 'in_c', 'block_out', 'block_in', 'mapper', 'codem_store',
                  'cartarea_store', 'ram_copy')


def rule_inline(res, rom, mapper, args):
    """Rule 1. Returns (rows, text lines)."""
    sc = res['sc']
    z = sc.region_for(0, 0)
    cands = set()
    for e, R in sc.routines.items():
        if e[0] == z and e[1] in range(8, 0x40, 8) and 'rst' in R.kinds:
            cands.add(e)
        elif len(sc.callers_prev.get(e, ())) >= 2:
            cands.add(e)
    disp = sorted((e for e in cands if inline_dispatcher(sc, e)
                   and sc.summ_prev.get(e, DEFAULT_SUMMARY).dispatch != 'inline'), key=lambda e: e[1])
    rows, text = [], []
    if not disp:
        return rows, text
    seeds = list(getattr(sc, 'final_seeds', []))
    cur = sc
    extra = []
    tables = []
    rescans = 0
    for _round in range(8):
        bound = _block_starts(cur)
        first = inline_tables(cur, [d for d in disp if d in cur.routines], bound)
        tg = set()
        for (cn, d, t0, mask, words, why, bank) in first:
            tg.update(o for o in (_word_off(cur, w, cn) for w in words) if o is not None)
        tables = inline_tables(cur, [d for d in disp if d in cur.routines], bound | tg)
        new = []
        for (cn, d, t0, mask, words, why, bank) in tables:
            for w in words:
                m = _word_node(cur, w, cn)
                if m is not None and m not in extra and m not in cur.routines:
                    new.append(m)
        new = sorted(set(new), key=lambda x: (repr(x[0]), x[1]))
        if not new:
            break
        extra += new
        sc2 = Scanner(rom, mapper, args.unroll)
        sc2.run(seeds + [(m, 'table') for m in extra])
        cur = sc2
        rescans += 1
    for (cn, d, t0, mask, words, why, bank) in tables:
        rows.append({'addr': cn[1], 'bank': node_bank_s(cn), 'offset': cur.off_of(cn[0], cn[1]), 'bytes': cur.decode_node(cn).hexbytes(), 'insn': cur.decode_node(cn).text,
                     'kind': 'inline_table', 'target': h4(t0), 'class': 'dispatcher %s' % h4(d[1]),
                     'confidence': 'medium', 'how': 'inline-table',
                     'note': '%d entries (%s): %s' % (len(words), why, ' '.join(h4(w) for w in words))})
    text.append('  dispatchers: ' + ', '.join('%s bank %s' % (h4(d[1]), node_bank_s(d)) for d in disp))
    text.append('  tables read: %d; entry points added: %d; rescans: %d' % (len(tables), len(extra), rescans))
    if cur is sc:
        return rows, text
    r2 = collect(cur, rom, [], [], set(), None, cur.rounds, 0, args)
    old = set((r['kind'], r['offset'], r['addr']) for r in res['sites'])
    added = []
    for r in r2['sites']:
        if r['kind'] in SITE_KINDS_NEW and (r['kind'], r['offset'], r['addr']) not in old:
            r = dict(r)
            r['confidence'] = 'medium'
            r['how'] = 'inline-table'
            r['note'] = ('reached only through an inline table; ' + r['note']).rstrip('; ')
            rows.append(r)
            added.append(r)
    text.append('  sites reached only through the tables: %d' % len(added))
    for r in added:
        text.append('    %s bank %s offset %s  %-20s %-12s %s %s' % (h4(r['addr']), r['bank'], fmt_off(r['offset']), r['insn'],
                                                                  r['kind'], r['target'], r['class']))
    return rows, text


# ---- rule 2: a mailbox byte that a second plain store can overwrite

def _accesses(sc, rt, s, ins):
    """Memory accesses at known RAM addresses: list of (addr, what, value),
    what = 'read', 'store' (a plain store) or 'rmw' (INC, DEC, SET, RES...)."""
    sem = ins.sem
    t = sem[0]
    out = []

    def mem(o):
        return isinstance(o, tuple) and o[0] in ('abs', 'mem')
    if t == 'ld8':
        if mem(sem[1]):
            v = sc.g8(s, sem[2])
            for a in _mem_addrs(sc, rt, s, sem[1]):
                out.append((a, 'store', v if isinstance(v, int) else None))
        if mem(sem[2]):
            for a in _mem_addrs(sc, rt, s, sem[2]):
                out.append((a, 'read', None))
    elif t == 'st16':
        for a in (sem[1], (sem[1] + 1) & 0xFFFF):
            out.append((a, 'store', None))
    elif t == 'ld16' and isinstance(sem[2], tuple) and sem[2][0] == 'abs':
        out += [(sem[2][1], 'read', None), ((sem[2][1] + 1) & 0xFFFF, 'read', None)]
    elif t == 'alu' and mem(sem[2]):
        out += [(a, 'read', None) for a in _mem_addrs(sc, rt, s, sem[2])]
    elif t in ('inc8', 'dec8') and mem(sem[1]):
        out += [(a, 'rmw', None) for a in _mem_addrs(sc, rt, s, sem[1])]
    elif t == 'cb' and mem(sem[3]):
        out += [(a, 'read' if sem[1] == 'BIT' else 'rmw', None) for a in _mem_addrs(sc, rt, s, sem[3])]
    return [x for x in out if _ram_addr(x[0])]


class PathMin(FrameCost):
    """The frame cost model with the cheapest path instead of the costliest:
    the shortest run time of a routine, loops with a known count counted in
    full and other loops once. mode 'next': Next cycles, each I/O instruction
    at its cheapest trap; mode 'sms': Z80 T-states."""

    def __init__(self, fc, mode):
        self.__dict__.update(fc.__dict__)
        self.memo = {}
        self.noret = set()
        self.mode = mode

    def node_cost(self, R, n, env, need, stack):
        if self.mode == 'next':
            c = FrameCost.node_cost(self, R, n, env, need, stack)
            return Cost(c.lo, c.lo, c.unk)
        ins = self.sc.decode_node(n)
        if ins is None:
            return ZERO
        c = Cost(tstates(ins.raw))
        if ins.sem[0] == 'block' and ins.sem[1] in ('LDIR', 'LDDR', 'CPIR', 'CPDR'):
            cnt = self._value(R, n, 'BC', env, need)
            c = Cost(21 * (cnt or 0x10000) - 5) if cnt is not None else Cost(16, 16, True)
        elif ins.sem[0] == 'block' and ins.sem[1] in ('OTIR', 'OTDR', 'INIR', 'INDR'):
            cnt = self._value(R, n, 'B', env, need)
            c = Cost(21 * (cnt or 256) - 5) if cnt is not None else Cost(16, 16, True)
        callees = self.calls_at.get((R.entry, n))
        if callees:
            best = None
            for e in callees:
                k = self.routine_cost(e, self.callee_env(R, n, env, need), stack, need, (R.entry, n))
                best = k if best is None or k.lo < best.lo else best
            c = c + best
        return c

    def _path(self, R, ctx, n, env, need, stack, memo, active, anyend):
        if n in memo:
            return memo[n]
        if n in active:
            return ZERO if anyend else None
        loops, inner, preds, back = self._loops(R)
        L, x = None, inner.get(n)
        while x is not None and x is not ctx:
            L, x = x, x.parent
        if x is not ctx:
            L = None
        active.add(n)
        opts = []
        if L is not None:
            c = self.loop_total(R, L, env, need, stack)
            for x in L.body_sorted():
                for (m, _t) in self.dedges(R).get(x, ()):
                    if m in L.body:
                        continue
                    if ctx is not None and (m == ctx.header or m not in ctx.body):
                        opts.append(ZERO)
                        continue
                    r = self._path(R, ctx, m, env, need, stack, memo, active, anyend)
                    if r is not None:
                        opts.append(r)
                ins = self.sc.decode_node(x)
                if ins is not None and self.is_exit(R, x, ins):
                    opts.append(ZERO)
        else:
            c = self.node_cost(R, n, env, need, stack)
            ins = self.sc.decode_node(n)
            es = self.dedges(R).get(n, ()) if ins is not None else ()
            if ins is not None and self.is_exit(R, n, ins):
                opts.append(ZERO)
            for (m, _t) in es:
                if m in self.reset_nodes and R.entry[1] != 0x0000 and n not in self.reset_nodes:
                    continue
                if ctx is not None and (m == ctx.header or m not in ctx.body):
                    opts.append(ZERO)
                    continue
                r = self._path(R, ctx, m, env, need, stack, memo, active, anyend)
                if r is not None:
                    opts.append(r)
            if not es and anyend:
                opts.append(ZERO)
        if not opts and anyend:
            opts.append(ZERO)
        res = None
        if opts:
            res = c + min(opts, key=lambda k: k.lo)
        active.discard(n)
        memo[n] = res
        return res

    def shortest(self, e):
        """Shortest time of one call of e, or None when no path returns."""
        if e not in self.sc.routines:
            return None
        c = self.routine_cost(e, {}, frozenset(), None, None)
        return None if e in self.noret else c.lo


class MinTime:
    """Shortest run time from one instruction to another, over every edge the
    scanner found (table entries too), through calls and returns: called
    routines that the path does not enter cost their shortest time
    (PathMin), and loops on the path itself count once. A HALT or a loop
    that waits for the frame interrupt (no stores, no calls, and a read of the
    VDP status, the V counter, or one fixed RAM byte) ends a path: the handler
    runs there. So does a call of a routine that always waits (every path to
    its return meets a HALT, a wait loop, or a call of such a routine)."""

    def __init__(self, fc, irq_stores):
        self.fc, self.sc = fc, fc.sc
        self.pm = (PathMin(fc, 'next'), PathMin(fc, 'sms'))
        self.skip = {}
        self.cost = {}
        self.calls = {}
        for callee, lst in self.sc.callers_prev.items():
            for (crt, cnode, _cs) in lst:
                self.calls.setdefault((crt, cnode), set()).add(callee)
        for k, cs in self.calls.items():
            self.calls[k] = sorted(cs, key=nkey)
        self.wait = set()
        for e, R in self.sc.routines.items():
            for L in fc._loops(R)[0].values():
                if self._waits(e, L, irq_stores):
                    self.wait |= L.body

    def _waits(self, e, L, irq_stores):
        sc = self.sc
        polls = False
        for n in L.body_sorted():
            ins = sc.decode_node(n)
            t = ins.sem[0]
            if t in ('call', 'rst', 'st16', 'outn', 'outC', 'block', 'halt'):
                return False
            if t == 'ld8' and not isinstance(ins.sem[1], str):
                return False
            if t == 'inn' and port_class(ins.sem[1], 'in') in ('vdp_status', 'v_counter'):
                polls = True
            for (rt, s, _h) in sc.ctx.get(n, ())[:4]:
                if rt != e:
                    continue
                for (a, what, _v) in _accesses(sc, rt, s, ins):
                    if what == 'read' and a in irq_stores:
                        polls = True
                    # a fixed RAM byte polled by a loop with no stores and no
                    # calls: only another context can end the loop
                    if what == 'read' and isinstance(a, int) and 0xC000 <= a <= 0xFFFB:
                        polls = True
        return polls

    def node(self, e, n):
        """(Next cycles, SMS T-states) of one run of node n in routine e, without
        its callees; False for a HALT or a wait loop."""
        key = (e, n)
        c = self.cost.get(key)
        if c is None:
            ins = self.sc.decode_node(n)
            sem = ins.sem
            if sem[0] == 'halt' or n in self.wait:
                c = False
            else:
                nx, ts = native_cycles(ins), tstates(ins.raw)
                cnt = 1
                if sem[0] == 'block' and sem[1] in ('LDIR', 'LDDR', 'CPIR', 'CPDR', 'OTIR', 'OTDR', 'INIR', 'INDR'):
                    reg = 'BC' if sem[1][:2] in ('LD', 'CP') else 'B'
                    vals = set()
                    for (rt, s, _h) in self.sc.ctx.get(n, ()):
                        if rt == e:
                            v = pget(s, reg) if reg == 'BC' else s['B']
                            vals.add(v if isinstance(v, int) else None)
                    if vals and None not in vals:
                        cnt = min(vals) or (0x10000 if reg == 'BC' else 0x100)
                    ts = 21 * cnt - 5
                    nx = 24 * cnt - 5
                io = self.fc.io.get(n)
                if io is not None:
                    form, classes = io
                    nx = min(trap_cost(form, cl, cnt).lo for cl in classes)
                c = (nx, ts)
            self.cost[key] = c
        return c

    def passable(self, c):
        """False when every path through routine c to its return meets a HALT,
        a wait loop, or a call of a routine that always waits."""
        memo = self.__dict__.setdefault('_pass', {})
        if c in memo:
            return memo[c]
        memo[c] = True          # recursion: assume passable
        R = self.sc.routines.get(c)
        if R is None:
            return True
        ok = False
        work, seen = [c], set()
        while work and not ok:
            n = work.pop()
            if n in seen:
                continue
            seen.add(n)
            ins = self.sc.decode_node(n)
            if ins.sem[0] == 'halt' or n in self.wait:
                continue
            callees = self.calls.get((c, n), ())
            if callees and not any(self.passable(x) for x in callees):
                continue
            if not callees and (self._is_exit(c, n, ins) or (ins.sem[0] == 'ret' and ins.sem[1] is not None)):
                ok = True
                break
            work.extend(self._succ(c, n))
        memo[c] = ok
        return ok

    def skip_cost(self, c):
        if not self.passable(c):
            return None
        if c not in self.skip:
            a, b = self.pm[0].shortest(c), self.pm[1].shortest(c)
            self.skip[c] = None if a is None or b is None else (a, b)
        return self.skip[c]

    def _succ(self, e, n):
        R = self.sc.routines.get(e)
        return [m for (m, _t) in R.edges.get(n, ())] if R is not None else []

    def _is_exit(self, e, n, ins):
        if ins.sem[0] not in ('ret', 'reti'):
            return False
        nxt = (n[0], (n[1] + len(ins.raw)) & 0xFFFF)
        return all(m == nxt for m in self._succ(e, n))

    def between(self, starts, goal):
        """(Next cycles, SMS T-states, anon) from the end of a start node to
        the start of goal on the shortest path, or None. The search first
        keeps to paths whose returns all match a call on the path; only when
        there is none does it allow a return with no known stack (to any
        caller of the routine), and then anon is True."""
        for anon_ok in (False, True):
            r = self._between(starts, goal, anon_ok)
            if r is not None:
                return r + (anon_ok,)
        return None

    def _between(self, starts, goal, anon_ok):
        sc = self.sc
        # routines whose calls can lead to goal: only those are entered
        rev = {}
        for (crt, _cn), cs in self.calls.items():
            for c in cs:
                rev.setdefault(c, set()).add(crt)
        work = [rt for (rt, _s, _h) in sc.ctx.get(goal, ())]
        self.enter = set()
        while work:
            x = work.pop()
            if x in self.enter:
                continue
            self.enter.add(x)
            work.extend(rev.get(x, ()))
        heap = []
        k = 0
        for (n, e) in starts:
            c = self.node(e, n)
            if c is False:
                continue
            for m in self._next(e, n, (), anon_ok):
                k += 1
                heapq.heappush(heap, (c[0] + m[3], c[1] + m[4], k, m[0], m[1], m[2]))
        seen = set()
        while heap:
            nx, ts, _k, n, e, stack = heapq.heappop(heap)
            if nx > RULE_CAP:
                return None
            if n == goal:
                return (nx, ts)
            key = (n, e, stack)
            if key in seen:
                continue
            seen.add(key)
            if len(seen) > 200000:
                return None
            c = self.node(e, n)
            if c is False:
                continue
            for m in self._next(e, n, stack, anon_ok):
                k += 1
                heapq.heappush(heap, (nx + c[0] + m[3], ts + c[1] + m[4], k, m[0], m[1], m[2]))
        return None

    def _next(self, e, n, stack, anon_ok=True):
        """Successors (node, routine, stack, extra Next, extra SMS)."""
        sc = self.sc
        ins = sc.decode_node(n)
        out = []
        callees = self.calls.get((e, n), ())
        succ = self._succ(e, n)
        if callees:
            for c in callees:
                if len(stack) < 8 and c in self.enter:
                    out.append((c, c, stack + ((e, n),), 0, 0))
                k = self.skip_cost(c)
                if k is not None:
                    out += [(m, e, stack, k[0], k[1]) for m in succ]
            if ins.sem[0] == 'call' and ins.sem[2] is not None:
                nxt = (n[0], (n[1] + len(ins.raw)) & 0xFFFF)
                out += [(m, e, stack, 0, 0) for m in succ if m == nxt]
            return out
        cond_ret = ins.sem[0] == 'ret' and ins.sem[1] is not None
        if self._is_exit(e, n, ins) or cond_ret:
            if stack:
                pe, pn = stack[-1]
                out += [(m, pe, stack[:-1], 0, 0) for m in self._succ(pe, pn)]
            elif anon_ok:
                for (crt, cnode, _cs) in sc.callers_prev.get(e, ()):
                    if crt in sc.routines:
                        out += [(m, crt, (), 0, 0) for m in self._succ(crt, cnode)]
            if cond_ret:
                nxt = (n[0], (n[1] + len(ins.raw)) & 0xFFFF)
                out += [(m, e, stack, 0, 0) for m in succ if m == nxt]
            return out
        return [(m, e, stack, 0, 0) for m in succ]


def _ramclear_seed(sc, n, ins):
    """True for LD (HL),x at the head of the RAM-clear idiom LD (HL),x; ...;
    LDIR: it writes one byte of a range, not a mailbox clear."""
    sem = ins.sem
    if sem[0] != 'ld8' or sem[1] != ('mem', 'HL', 0):
        return False
    m = (n[0], (n[1] + len(ins.raw)) & 0xFFFF)
    for _ in range(4):
        nx = sc.decode_node(m)
        if nx is None:
            return False
        if nx.sem[0] == 'block':
            return nx.sem[1] == 'LDIR'
        m = (m[0], (m[1] + len(nx.raw)) & 0xFFFF)
    return False


MAILBOX_WINDOW = 0.1            # SMS frames between the stores below which a race is unlikely


def _mailbox_conf(p):
    """medium for a pair that has a window of at least MAILBOX_WINDOW SMS
    frames and under a frame on the SMS too; low otherwise (an interrupt is
    unlikely to land between the stores, or on the SMS it always does)."""
    sms = p[0][1]
    return 'medium' if MAILBOX_WINDOW * SMS_FRAME_T <= sms < SMS_FRAME_T else 'low'


def rule_mailbox(res):
    sc, cm = res['sc'], res['cost']
    fc = cm['fc']
    irq_r, irq_w0, irq_st = {}, {}, set()
    irq_inc = set()
    fg_st = {}
    fg_reads = {}
    fg_read_nodes = {}
    fg_writers = {}
    for e, R in sc.routines.items():
        irq = e in fc.irq_set
        fg = e in fc.fg_set and not irq
        if not irq and not fg:
            continue
        for n in fc.dedges(R):
            ins = sc.decode_node(n)
            for (rt, s, _h) in sc.ctx.get(n, ()):
                if rt != e:
                    continue
                for (a, what, v) in _accesses(sc, rt, s, ins):
                    if irq:
                        if what == 'read':
                            irq_r.setdefault(a, set()).add(n)
                        elif what == 'store':
                            irq_st.add(a)
                            if v == 0 and not _ramclear_seed(sc, n, ins):
                                irq_w0.setdefault(a, set()).add(n)
                        else:
                            irq_st.add(a)
                            if ins.sem[0] in ('inc8', 'dec8'):
                                irq_inc.add(a)
                    else:
                        if what == 'read' or what == 'rmw':
                            fg_reads.setdefault(a, set()).add(e)
                        if what == 'read':
                            fg_read_nodes.setdefault(a, set()).add((n, e))
                        else:
                            fg_writers.setdefault(a, set()).add(e)
                        if what == 'store' and v != 0:
                            fg_st.setdefault(a, {}).setdefault(n, set()).add((e, v))
    mt = MinTime(fc, irq_st)
    # a byte the interrupt increments is a counter, and one that a foreground
    # routine reads outside a wait loop, without writing it, is a state the
    # foreground dispatches on: neither is a request that a second store can
    # lose
    boxes = sorted(a for a in irq_r if a in irq_w0 and a in fg_st and a not in irq_inc and
                   all(n in mt.wait or e in fg_writers.get(a, ()) for (n, e) in fg_read_nodes.get(a, ())))
    rows, text = [], []
    for a in boxes:
        stores = {}
        for n, evs in fg_st[a].items():
            plain = [(e, v) for (e, v) in evs if e not in fg_reads.get(a, ())]
            if plain:
                stores[n] = plain
        nodes = sorted(stores, key=lambda n: (sc.off_of(n[0], n[1]) or 0, nkey(n)))[:12]
        if len(nodes) < 2:
            continue
        rd = sorted(irq_r[a], key=nkey)
        cl = sorted(irq_w0[a], key=nkey)
        found = []
        for s1 in nodes:
            starts = [(s1, e) for (e, _v) in sorted(set(stores[s1]), key=repr)]
            for s2 in nodes:
                if s2 == s1:
                    continue
                t = mt.between(starts, s2)
                if t is not None:
                    found.append((t[:2], s1, s2, t[2]))
        if not found:
            text.append('  %s: read and cleared by the interrupt context at %s; foreground plain stores at %s; '
                        'no path from one store to another within %d cycles' %
                        (h4(a), ' '.join(h4(n[1]) for n in rd + cl), ' '.join(h4(n[1]) for n in nodes), RULE_CAP))
            continue
        pairs = []
        for (t, s1, s2, anon) in found:
            vs1 = set(v for (_e, v) in stores[s1])
            vs2 = set(v for (_e, v) in stores[s2])
            if None not in vs1 and vs1 == vs2 and len(vs1) == 1:
                continue            # the same value twice loses nothing
            if t[0] < NEXT_FRAME:
                pairs.append((t, s1, s2, anon))

        def vals_of(n):
            return ','.join(sorted(set(h2(v) if v is not None else '?' for (_e, v) in stores[n])))

        def pair_txt(p):
            t, s1, s2, anon = p
            return '%s stores %s, then %s stores %s: %d Next cycles (%.2f frames), %d SMS T-states (%.2f SMS frames)' % (
                h4(s1[1]), vals_of(s1), h4(s2[1]), vals_of(s2), t[0], t[0] / NEXT_FRAME, t[1], t[1] / SMS_FRAME_T) + (
                ' (needs a return with no known stack)' if anon else '')
        head = 'interrupt context reads %s at %s and clears it at %s' % (
            h4(a), ' '.join(h4(n[1]) for n in rd), ' '.join(h4(n[1]) for n in cl))
        if not pairs:
            text.append('  %s: %s; no two foreground stores with different values within a frame of each other' %
                        (h4(a), head))
            continue
        # the row: the pair of highest confidence; among equals one whose path
        # has a known stack, then the longest SMS time
        pairs.sort(key=lambda p: (_mailbox_conf(p) != 'medium', p[3], -p[0][1], p[0][0]))
        t, s1, s2, anon = pairs[0]
        over = t[1] >= SMS_FRAME_T
        note = ('%s; %d store pairs under a frame on the Next (shortest paths); longest on the SMS: %s%s' %
                (head, len(pairs), pair_txt(pairs[0]),
                 '; over a frame on the SMS: only the Next can lose the first store' if over else
                 '; the SMS time is a lower bound'))
        cls = ('under a frame, SMS over' if over else
               'under a frame, caller unknown' if anon else 'under a frame')
        conf = _mailbox_conf(pairs[0])
        ins = sc.decode_node(s2)
        rows.append({'addr': s2[1], 'bank': node_bank_s(s2), 'offset': sc.off_of(s2[0], s2[1]),
                     'bytes': ins.hexbytes(), 'insn': ins.text, 'kind': 'mailbox_race', 'target': h4(a),
                     'class': cls, 'confidence': conf,
                     'how': 'static', 'note': note})
        text.append('  %s: %s; %d store pairs under a frame on the Next:' % (h4(a), head, len(pairs)))
        for p in pairs[:6]:
            text.append('    ' + pair_txt(p))
        if len(pairs) > 6:
            text.append('    ... %d more' % (len(pairs) - 6))
    return rows, text


SMS_FRAME_T = 59736             # 262 lines of 228 T-states


# ---- rule 3: column and rectangle streamers

def _writes_in(fc, e, n, env=None, depth=0, active=frozenset(), sink=None):
    """(control writes, data writes, unknown) of one run of node n of routine
    e, with its callees; loops in the callees count with the values the call
    passes; unknown: some such loop count is not known (counted once)."""
    sc = fc.sc
    env = env or {}
    R = sc.routines[e]
    ctrl = data = 0
    unk = False
    w = fc.vdp_write.get(n)
    if w is not None:
        if sink is not None:
            sink.add(n)
        ins = sc.decode_node(n)
        k = 1
        if ins.sem[0] == 'block' and ins.sem[1] in ('OTIR', 'OTDR'):
            b = fc._value(R, n, 'B', env, set())
            if b is None:
                unk = True
            k = (b or 256) if b is not None else 1
        if w == 'control':
            ctrl += k
        else:
            data += k
            io = fc.io.get(n)
            if io is not None and 'vdp_control' in io[1]:
                ctrl += k
    if depth < 3:
        for c in fc.calls_at.get((e, n), ()):
            Rc = sc.routines.get(c)
            if Rc is None or c in active:
                continue
            cenv = fc.callee_env(R, n, env, set())
            loops, inner, preds, back = fc._loops(Rc)
            for m in fc.dedges(Rc):
                a, b, u = _writes_in(fc, c, m, cenv, depth + 1, active | {c}, sink)
                if not a and not b:
                    unk |= u
                    continue
                mult = 1
                L = inner.get(m)
                while L is not None:
                    _r, cnt = fc.loop_count(Rc, L, cenv, set())
                    if cnt is None:
                        unk = True
                    else:
                        mult *= cnt
                    L = L.parent
                ctrl += a * mult
                data += b * mult
                unk |= u
    return ctrl, data, unk


def _adds_40(sc, e, n):
    """'+$40' or '-$40' when node n adds $40 to an address, else None."""
    ins = sc.decode_node(n)
    sem = ins.sem
    if sem[0] == 'add16':
        for (rt, s, _h) in sc.ctx.get(n, ()):
            if rt != e:
                continue
            for v in _vals(sc, rt, pget(s, sem[2])):
                if v == 0x40:
                    return '+$40'
                if v == 0xFFC0:
                    return '-$40'
    elif sem[0] == 'alu' and sem[1] in ('ADD', 'SUB') and sem[2] == ('imm', 0x40):
        return '+$40' if sem[1] == 'ADD' else '-$40'
    elif sem[0] == 'alu' and sem[1] == 'ADD' and sem[2] == ('imm', 0xC0):
        return '-$40'
    return None


def rule_streamers(res):
    sc, cm = res['sc'], res['cost']
    fc, crow = cm['fc'], cm['rows']
    found = {}
    for e in sorted(sc.routines, key=lambda x: (repr(x[0]), x[1])):
        R = sc.routines[e]
        loops, inner, preds, back = fc._loops(R)
        good = {}
        for L in loops.values():
            ctrl = data = 0
            step = None
            env = crow[e][1] if e in crow else {}
            for n in L.body_sorted():
                a, b, _u = _writes_in(fc, e, n, env, sink=set())
                ctrl += a
                data += b
                step = step or _adds_40(sc, e, n)
            if ctrl >= 2 and data >= 1 and not step:
                step = _pass_step(sc, fc, e, L)
            if ctrl >= 2 and data >= 1 and step:
                good[L.header] = L
        for h, L in good.items():
            if any(M.parent is L for M in good.values()):
                continue            # report the innermost loop that streams
            if h in found:
                continue
            env = crow[e][1] if e in crow else {}
            need = set()
            reg, cnt = fc.loop_count(R, L, env, need)
            per = fc._path(R, L, L.header, env, need, frozenset({e}), {}, set(), True)
            # data writes per pass, inner loops counted
            cells = 0
            unknown_inner = False
            wnodes = set()
            for n in L.body_sorted():
                il = inner.get(n)
                k = 1
                M = il
                while M is not None and M is not L:
                    _r, c = fc.loop_count(R, M, env, need)
                    if c is None:
                        unknown_inner = True
                    else:
                        k *= c
                    M = M.parent
                _a, b, u = _writes_in(fc, e, n, env, sink=wnodes)
                cells += k * b
                unknown_inner |= u
            total = fc.loop_total(R, L, env, need, frozenset({e}))
            ctx = 'irq' if e in fc.irq_set and e not in fc.fg_set else 'both' if e in fc.irq_set else 'fg'
            outer = L.parent
            ocnt = fc.loop_count(R, outer, env, need)[1] if outer is not None else None
            ps = _pass_step(sc, fc, e, L)
            found[h] = (e, L, cnt, cells, unknown_inner, per, total, ctx, outer, ocnt,
                        ('%s a pass' % ps) if ps else _adds_40_any(sc, e, L), wnodes)
    rows, text = [], []
    for h, (e, L, cnt, cells, unk, per, total, ctx, outer, ocnt, step, wn) in sorted(found.items(), key=lambda x: -x[1][6].hi):
        ins = sc.decode_node(h)
        note = ('routine %s (%s); passes %s, address step %s, %s%s VDP data writes a pass; one pass %s cycles, '
                'loop %s cycles (%.2f frames)%s' %
                (h4(e[1]), ctx, cnt if cnt is not None else '?', step, cells, '+' if unk else '', per.txt(),
                 total.txt(), total.hi / NEXT_FRAME,
                 '; inside loop %s x%s' % (h4(outer.header[1]), ocnt if ocnt is not None else '?') if outer else ''))
        note += '; VDP writes at ' + ' '.join('%s(%s)' % (h4(m[1]), fmt_off(sc.off_of(m[0], m[1])))
                                             for m in sorted(wn, key=lambda m: (sc.off_of(m[0], m[1]) or 0, nkey(m))))
        rows.append({'addr': h[1], 'bank': node_bank_s(h), 'offset': sc.off_of(h[0], h[1]), 'bytes': ins.hexbytes(),
                     'insn': ins.text, 'kind': 'streamer', 'target': h4(e[1]), 'class': ctx,
                     'confidence': 'high' if cnt is not None else 'medium', 'how': 'static', 'note': note})
        text.append('  %s bank %s: %s' % (h4(h[1]), node_bank_s(h), note))
    return rows, text


def _adds_40_any(sc, e, L):
    for n in L.body_sorted():
        s = _adds_40(sc, e, n)
        if s:
            return '%s at %s' % (s, h4(n[1]))
    return '?'


_STEP_PAIRS = ('BC', 'DE', 'HL', 'IX', 'IY')


def _pass_step(sc, fc, e, L):
    """A register pair that one pass of loop L moves by $40 or -$40 (net, on
    some path through the body): 'HL +$40' and the like, or None. Follows INC,
    DEC, ADD rr with a known value, the block instructions and EX DE,HL; a
    call keeps only the pairs its summary keeps."""
    R = sc.routines[e]
    edges = fc.dedges(R)
    paths = 0

    def apply(st, n):
        ins = sc.decode_node(n)
        sem = ins.sem
        t = sem[0]
        st = dict(st)
        if t == 'exde':
            st['HL'], st['DE'] = st['DE'], st['HL']
        elif t in ('inc16', 'dec16') and sem[1] in st:
            o = st[sem[1]]
            if o is not None:
                st[sem[1]] = (o[0], o[1] + (1 if t == 'inc16' else -1))
        elif t == 'add16' and sem[1] in st:
            o = st[sem[1]]
            k = set()
            for (rt, s, _h) in sc.ctx.get(n, ()):
                if rt == e:
                    k |= _vals(sc, rt, pget(s, sem[2])) or {None}
            if o is not None and len(k) == 1 and None not in k:
                v = k.pop()
                st[sem[1]] = (o[0], o[1] + (v if v < 0x8000 else v - 0x10000))
            else:
                st[sem[1]] = None
        elif t == 'block':
            d = 1 if sem[1] in ('LDI', 'LDIR', 'OUTI', 'OTIR', 'INI', 'INIR', 'CPI', 'CPIR') else -1
            if sem[1][-1] == 'R':
                st['HL'] = None
                if sem[1][:2] == 'LD':
                    st['DE'] = None
            else:
                if st['HL'] is not None:
                    st['HL'] = (st['HL'][0], st['HL'][1] + d)
                if sem[1] in ('LDI', 'LDD') and st['DE'] is not None:
                    st['DE'] = (st['DE'][0], st['DE'][1] + d)
        elif t in ('call', 'rst'):
            for c in fc.calls_at.get((e, n), ()):
                out = sc.summ_prev.get(c, DEFAULT_SUMMARY).out
                for p in _STEP_PAIRS:
                    if not all(out.get(h) == ('keep',) for h in PAIRS[p]):
                        st[p] = None
        elif t == 'pop' and sem[1] in st:
            st[sem[1]] = None
        elif t == 'ld16' and sem[1] in st:
            st[sem[1]] = None
        elif t in ('ld8', 'alu', 'inc8', 'dec8', 'cb', 'acc', 'inC', 'exx'):
            dst = sem[1] if t in ('ld8', 'inc8', 'dec8') else sem[4] if t == 'cb' else sem[1] if t == 'inC' else None
            if t == 'exx':
                st = {p: (None if p in ('BC', 'DE', 'HL') else st[p]) for p in st}
            for p in _STEP_PAIRS:
                if isinstance(dst, str) and dst in PAIRS[p]:
                    st[p] = None
            if t == 'cb' and isinstance(sem[3], str):
                for p in _STEP_PAIRS:
                    if sem[3] in PAIRS[p] and sem[1] != 'BIT':
                        st[p] = None
        return st

    start = {p: (p, 0) for p in _STEP_PAIRS}
    work = [(L.header, start, frozenset())]
    steps = 0
    while work and paths < 64 and steps < 4000:
        steps += 1
        n, st, seen = work.pop()
        st = apply(st, n)
        for (m, _t) in edges.get(n, ()):
            if m == L.header:
                paths += 1
                for p in _STEP_PAIRS:
                    o = st[p]
                    if o is not None and o[0] == p and o[1] in (0x40, -0x40):
                        return '%s %s$40' % (p, '+' if o[1] > 0 else '-')
            elif m in L.body and m not in seen:
                work.append((m, st, seen | {n}))
    return None


# ---- rule 4: Sega planar RLE decoder

RLE_CORE = bytes.fromhex('7E23B7C84FE67F47')
RLE_CORE_DE = bytes.fromhex('1A13B7C8')      # the same core reading the stream through DE (Hang On)
RLE_JRZ_HEAD = bytes.fromhex('7E23B728')     # the core with JR Z,exit for RET Z (Castle of Illusion) ...
RLE_JRZ_TAIL = bytes.fromhex('4FE67F47')     # ... then LD C,A; AND $7F; LD B,A


def _rle_jrz_loop(rom, j):
    """True when the JR Z core at offset j is the head of a decoder loop: the
    code from the core to the JR Z target decodes in a run, holds a jump back
    to the head, BIT 7,C (the literal or run choice), a count down of B
    (DJNZ or DEC B) and an OUT to the VDP data port."""
    d = rom[j + 4]
    end = j + 5 + (d - 256 if d >= 128 else d)
    if end <= j + 9:
        return False
    bank = j >> 14
    head = (j & 0x3FFF) | (0x8000 if bank >= 2 else bank * 0x4000)
    back = bits7 = count = data = False
    o = j + 9
    while o < end:
        ins = decode(lambda i, o=o: rom[o + i] if o + i < len(rom) else None, head + o - j)
        if ins is None or not ins.raw:
            return False
        sem = ins.sem
        if sem[0] in ('jp', 'jr', 'djnz') and isinstance(sem[1], int) and (sem[1] & 0x3FFF) == (head & 0x3FFF):
            back = True
        if sem[0] == 'djnz' or ins.text == 'DEC B':
            count = True
        if ins.text == 'BIT 7,C':
            bits7 = True
        if sem[0] == 'outn' and port_class(sem[1], 'out') == 'vdp_data':
            data = True
        o += len(ins.raw)
    return back and bits7 and count and data


def rule_rle(res):
    sc, cm = res['sc'], res['cost']
    fc, crow = cm['fc'], cm['rows']
    rom = sc.rom
    byoff = {}
    for n in sc.ctx:
        o = sc.off_of(n[0], n[1])
        if o is not None:
            byoff.setdefault(o, []).append(n)
    hits = []
    i = rom.find(RLE_CORE)
    while i >= 0:
        hits.append((i, 'core'))
        i = rom.find(RLE_CORE, i + 1)
    for head, form in ((RLE_CORE[:4], 'variant'), (RLE_CORE_DE, 'variant-de')):
        j = rom.find(head)
        while j >= 0:
            if not any(o == j for o, _k in hits) and 0xE6 in rom[j + 4:j + 8] and rom[rom.index(0xE6, j + 4) + 1] == 0x7F:
                hits.append((j, form))
            j = rom.find(head, j + 1)
    j = rom.find(RLE_JRZ_HEAD)
    while j >= 0:
        if rom[j + 5:j + 9] == RLE_JRZ_TAIL and _rle_jrz_loop(rom, j):
            hits.append((j, 'jr-z'))
        j = rom.find(RLE_JRZ_HEAD, j + 1)
    rows, text = [], []
    vec_ctrl = set(v for v in range(0, 0x40, 8) if rom[v:v + 2] == b'\xD3\xBF')
    for o, form in sorted(hits):
        window = rom[o:o + 64]
        out_be = window.count(b'\xD3\xBE')
        ctrl_bytes = window.count(b'\xD3\xBF') + sum(1 for b in window if b in (0xC7 + v for v in vec_ctrl))
        nodes = byoff.get(o, [])
        bank = o >> 14
        if nodes:
            n = nodes[0]
            ents = sorted(set(rt for m in nodes for (rt, _s, _h) in sc.ctx[m]), key=nkey)
            irq = [e for e in ents if e in fc.irq_set]
            ctrl = data = 0
            wn = set()
            for e in ents:
                R = sc.routines[e]
                L = fc._loops(R)[1].get(n)
                body = L.body if L is not None else {n}
                for m in body:
                    a, b, _u = _writes_in(fc, e, m, crow[e][1] if e in crow else {}, sink=wn)
                    ctrl, data = max(ctrl, a), max(data, b)
            cost = None
            for e in ents:
                if e in crow:
                    c = crow[e][0]
                    cost = c if cost is None else cost.most(c)
            note = ('%s; routine %s; %s; loop: %d control and %d data writes a pass; routine cost %s cycles%s' %
                    ('frame work: reached from the interrupt handler (%s)' % ' '.join(h4(e[1]) for e in irq) if irq else
                     'not frame work: foreground only',
                     ' '.join(h4(e[1]) for e in ents), form, ctrl, data, cost.txt() if cost else '?',
                     ' (%.2f frames, loop count from the data)' % (cost.hi / NEXT_FRAME) if cost else ''))
            note += '; VDP writes at ' + ' '.join('%s(%s)' % (h4(m[1]), fmt_off(sc.off_of(m[0], m[1])))
                                                 for m in sorted(wn, key=lambda m: (sc.off_of(m[0], m[1]) or 0, nkey(m))))
            calls = sorted(set(cn for e in ents for (_crt, cn, _cs) in sc.callers_prev.get(e, ())),
                           key=lambda m: (sc.off_of(m[0], m[1]) or 0, nkey(m)))
            note += '; called from ' + (' '.join('%s(%s)' % (h4(m[1]), fmt_off(sc.off_of(m[0], m[1]))) for m in calls)
                                        or 'nowhere (a jump or table entry)')
            addr, cls, conf = n[1], 'irq' if irq else 'fg', 'high'
            ins = sc.decode_node(n)
            bts, txt = ins.hexbytes(), ins.text
        else:
            addr = (o & 0x3FFF) | (0x8000 if bank >= 2 else bank * 0x4000)
            cls, conf = 'unreached', 'low'
            bts, txt = '7E', 'LD A,(HL)'
            note = '%s; no path reached it; in the 64 bytes from the core: %d OUT ($BE),A, %d control writes' % (
                form, out_be, ctrl_bytes)
        rows.append({'addr': addr, 'bank': bank if not nodes else node_bank_s(nodes[0]), 'offset': o, 'bytes': bts,
                     'insn': txt, 'kind': 'rle_decoder', 'target': form, 'class': cls, 'confidence': conf,
                     'how': 'byte scan', 'note': note})
        text.append('  offset %s (%s): %s' % (fmt_off(o), h4(addr), note))
    return rows, text



# ---- rule 5: H scroll from a table in the interrupt handler

def _vdp_ctrl_out(sc, n):
    ins = sc.decode_node(n)
    return ins is not None and ins.sem[0] == 'outn' and port_class(ins.sem[1], 'out') == 'vdp_control'


def _code_stores(sc):
    """Proven store addresses anywhere in the code: address -> store nodes."""
    out = {}
    for n in sc.ctx:
        sem = sc.decode_node(n).sem
        if sem[0] == 'ld8' and not isinstance(sem[1], str):
            for (rt, st, _h) in sc.ctx[n]:
                for a in _mem_addrs(sc, rt, st, sem[1]):
                    out.setdefault(a, set()).add(n)
        elif sem[0] == 'st16':
            for a in (sem[1], (sem[1] + 1) & 0xFFFF):
                out.setdefault(a, set()).add(n)
    return out


def rule_raster(res):
    """Interrupt code that writes VDP register 8 (H scroll) with a byte read
    from an address that changes from one interrupt to the next."""
    sc, fc = res['sc'], res['cost']['fc']
    stores = None
    found = {}
    for e in sorted(fc.irq_set, key=nkey):
        R = sc.routines[e]
        d = fc.dedges(R)
        preds = {}
        for n, es in d.items():
            for (m, _t) in es:
                preds.setdefault(m, set()).add(n)
        for n in d:
            if not _vdp_ctrl_out(sc, n):
                continue
            a = set(st['A'] for (rt, st, _h) in sc.ctx.get(n, ()) if rt == e)
            if a != {0x88}:
                continue
            # LD A,src; OUT ($BF),A; LD A,$88; OUT ($BF),A
            for p1 in preds.get(n, ()):
                if sc.decode_node(p1).sem != ('ld8', 'A', ('imm', 0x88)):
                    continue
                for p2 in preds.get(p1, ()):
                    if not _vdp_ctrl_out(sc, p2):
                        continue
                    for m in preds.get(p2, ()):
                        ins = sc.decode_node(m)
                        sem = ins.sem
                        if sem[0] != 'ld8' or sem[1] != 'A' or isinstance(sem[2], str) or sem[2][0] not in ('mem', 'abs'):
                            continue
                        o = sem[2]
                        how = None
                        if o[0] == 'mem':
                            addrs, unknown = set(), False
                            for (rt, st, _h) in sc.ctx.get(m, ()):
                                if rt != e:
                                    continue
                                v = _mem_addrs(sc, rt, st, o)
                                addrs |= v
                                unknown |= not v
                            if unknown or len(addrs) > 1:
                                how = 'pointer'
                                what = '%s from %s' % (ins.text, 'a pointer the scanner cannot prove' if unknown else
                                                      ' '.join(h4(x) for x in sorted(addrs)))
                        elif m[0][0] == 'ram':
                            if stores is None:
                                stores = _code_stores(sc)
                            ops = sorted(set(x for b in (m[1] + 1, m[1] + 2) for x in stores.get(b & 0xFFFF, ())),
                                         key=lambda x: (sc.off_of(x[0], x[1]) or 0, nkey(x)))
                            if ops:
                                how = 'patched address'
                                what = '%s, its address written by %s' % (
                                    ins.text, ' '.join('%s(%s) %s' % (h4(x[1]), fmt_off(sc.off_of(x[0], x[1])),
                                                                      sc.decode_node(x).text) for x in ops))
                        if how is None or m in found:
                            continue
                        vc = sorted((x for x in d if sc.decode_node(x).sem[0] == 'inn' and
                                     port_class(sc.decode_node(x).sem[1], 'in') == 'v_counter'), key=nkey)
                        found[m] = (e, n, how, what, vc)
    rows, text = [], []
    for m, (e, n, how, what, vc) in sorted(found.items(), key=lambda x: (sc.off_of(x[0][0], x[0][1]) or 0, nkey(x[0]))):
        ins = sc.decode_node(m)
        note = ('H scroll (VDP register 8) from a table: %s; register write at %s(%s); interrupt routine %s; %s; '
                'the spec may need a rastercode routine' %
                (what, h4(n[1]), fmt_off(sc.off_of(n[0], n[1])), h4(e[1]),
                 ('reads the V counter at ' + ' '.join(h4(x[1]) for x in vc)) if vc else 'no V counter read'))
        rows.append({'addr': m[1], 'bank': node_bank_s(m), 'offset': sc.off_of(m[0], m[1]), 'bytes': ins.hexbytes(),
                     'insn': ins.text, 'kind': 'raster_hscroll', 'target': h4(e[1]), 'class': how,
                     'confidence': 'high', 'how': 'static', 'note': note})
        text.append('  %s bank %s: %s' % (h4(m[1]), node_bank_s(m), note))
    return rows, text

def pattern_rules(res, rom, mapper, args):
    out = {'rows': [], 'sections': []}
    for title, fn in (('Inline jump tables (an RST or CALL that adds 2*A to its return address and jumps '
                       'through the word there)', lambda: rule_inline(res, rom, mapper, args)),
                      ('Mailbox races (a RAM byte the interrupt context reads and clears, written by two '
                       'foreground plain stores)', lambda: rule_mailbox(res)),
                      ('Column and rectangle streamers (a loop with a VDP control write pair, data writes '
                       'and an address step of $40)', lambda: rule_streamers(res)),
                      ('Sega planar RLE decoders (core 7E 23 B7 C8 4F E6 7F 47, or JR Z,exit for RET Z)',
                       lambda: rule_rle(res)),
                      ('Raster H scroll (interrupt code that writes VDP register 8 from a table)',
                       lambda: rule_raster(res))):
        rows, text = fn()
        out['rows'] += rows
        out['sections'].append((title, rows, text))
    return out


def write_rules(res, w):
    pr = res.get('rules')
    if not pr:
        return
    w('Pattern rules (rows in the sites file with kinds inline_table, mailbox_race, streamer, rle_decoder, '
      'raster_hscroll, and new sites with how inline-table):')
    for title, rows, text in pr['sections']:
        w('  %s: %d rows' % (title, len(rows)))
        for x in text:
            w('  ' + x)
    w('')


def write_outputs(res, rom, crc, header, name, args):
    sc = res['sc']
    out = args.out
    cols = ['addr', 'bank', 'offset', 'bytes', 'insn', 'kind', 'target', 'class', 'confidence', 'how', 'note']
    order = {'out': 0, 'in': 0, 'out_c': 0, 'in_c': 0, 'block_out': 0, 'block_in': 0, 'mapper': 1, 'codem_store': 2,
             'cartarea_store': 3, 'rst': 4, 'rst_vector': 5, 'ram_copy': 6, 'ram_exec': 7, 'jump_table': 8,
             'indirect_resolved': 9, 'indirect_unresolved': 10, 'bank_unresolved': 11, 'target_unresolved': 12,
             'inline_unresolved': 13, 'inline_table': 14, 'mailbox_race': 16, 'streamer': 17, 'rle_decoder': 18,
             'raster_hscroll': 19, 'mapper_unreached': 20, 'io_unreached': 21}
    rows = res['sites'] + res['unreached'] + res.get('rules', {}).get('rows', [])
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
        nodes = sorted(sc.ctx, key=lambda n: (sc.off_of(n[0], n[1]) if sc.off_of(n[0], n[1]) is not None else 1 << 30, nkey(n)))
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
    if TRACEDEF_OFF[0]:
        w('WARNING: run with --no-tracedef; trace and run forms are not costed, so the costs differ from the overlay builder\'s')
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
            if k in sc.bank_calls or k in sc.bank_headers or k in sc.handler_kind:
                continue
            src = sc.harvest_src.get(k)
            sins = sc.decode_node(src) if src else None
            w('  %s bank %s, stored by %s %s' % (h4(k[1]), k[0][2], h4(src[1]) if src else '?', sins.text if sins else ''))
        w('')
    if getattr(sc, 'harvested', None) and set(sc.handler_kind) & set(sc.harvested):
        w('Entry points taken from object handler fields (handler-table, handler-store, handler-spawn; medium confidence):')
        for k in sc.harvested:
            if k in sc.handler_kind:
                src = sc.harvest_src[k]
                w('  %s bank %s, %s, from %s %s' % (h4(k[1]), k[0][2], HANDLER_HOW[sc.handler_kind[k]],
                                                       h4(src[1]), sc.decode_node(src).text))
        w('')
    if getattr(sc, 'harvested', None) and sc.bank_calls & set(sc.harvested):
        w('Entry points called right after a constant bank switch that no path reached (bank call, medium confidence):')
        for k in sc.harvested:
            if k in sc.bank_calls:
                src = sc.harvest_src[k]
                w('  %s bank %s, after %s %s' % (h4(k[1]), k[0][2], h4(src[1]), sc.decode_node(src).text))
        w('')
    if getattr(sc, 'harvested', None) and sc.bank_headers & set(sc.harvested):
        w('Entry points in module headers, a run of JP at the start of a bank (bank header, medium confidence):')
        w('  ' + ' '.join('%s bank %s' % (h4(k[1]), k[0][2]) for k in sc.harvested if k in sc.bank_headers))
        w('')
    if getattr(sc, 'harvest_rejected', None):
        w('Harvested addresses rejected because the code reached from them looks like data: ' +
          ' '.join(h4(k[1]) for k in sc.harvest_rejected))
        w('')
    if sc.bad_nodes:
        w('Paths that stopped because the bytes do not look like code (likely data reached as code):')
        for n in sorted(sc.bad_nodes, key=lambda n: (sc.off_of(n[0], n[1]) or 0, nkey(n))):
            ins = sc.decode_node(n)
            w('  %s bank %s  %-20s %s' % (h4(n[1]), node_bank_s(n), ins.text if ins else '',
                                          sc.bad_why.get(n, 'invalid opcode or $FF fill')))
        w('')
    if res['conflicts']:
        cs = sorted(res['conflicts'])
        w('Bytes decoded both as an opcode and as an operand (overlapping code paths): %d, first at %s' %
          (len(cs), ' '.join(fmt_off(o) for o in cs[:20])))
        w('')
    ib = [r for r in res['unreached'] if r['kind'] == 'io_unreached']
    w('I/O byte patterns in bytes no path reached: %s (all in %s.sites.tsv as io_unreached; very-low rows are not listed here)' % (
        ', '.join('%s %d' % (c, sum(1 for r in ib if r['confidence'] == c)) for c in ('high', 'medium', 'low', 'very-low')), name))
    for r in ib:
        if r['confidence'] != 'very-low':
            w('  offset %s (bank %d, %s)  %-6s %-6s %-14s %s' % (fmt_off(r['offset']), r['bank'], h4(r['addr']), r['confidence'],
                                                               r['bytes'], r['insn'], r['note']))
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
    write_cost(res, name, out, w)
    write_rules(res, w)
    with open(os.path.join(out, name + '.summary.txt'), 'w') as f:
        f.write('\n'.join(L) + '\n')
    print('%s: %d I/O sites, %d mapper stores, %d unproven stores, code %d of %d bytes; output in %s' %
          (name, len(io), len([r for r in res['sites'] if r['kind'] == 'mapper']), len(up), tot[0], len(rom), out))


if __name__ == '__main__':
    main()
