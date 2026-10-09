"""Instruction table for the framework's trace handler (src/trace.asm).

A trace starts at a patched output site. The framework copies the game's
code around the site (the site, the straight-line code after it and, when
a jump goes back over the site, the loop) into a buffer, with every
patched output turned into a call that appends the byte to a buffer, and
runs it there; the bytes go to the port in one block at the end. The
table says which instructions a trace may contain. gentables.py writes it
into tables.inc; mkovl.py uses the same rules to choose trace sites.

Table byte: bits 0-1 length, bits 2-4 kind, bit 7 the instruction writes
register C. Kinds:
  0 not allowed (the trace ends before it)
  1 copied as it is
  2 CB prefix: copied when the second byte works on a register
  3 JR e   4 JR cc,e   5 DJNZ e   6 JP nn   7 JP cc,nn
Allowed: register loads and arithmetic, reads through (HL), (BC), (DE),
INC/DEC of B, C, D, E, H, L, A and of BC, DE, HL, ADD HL, rotates of A,
CPL, SCF, CCF, DAA, EX DE,HL, NOP, CB operations on registers, and jumps.
Not allowed: memory writes, stack and SP, calls, returns, RST, I/O other
than patched outputs, IX/IY, ED-prefixed instructions, HALT, EX AF, EXX,
DI, EI.
"""
K_BAD, K_COPY, K_CB, K_JR, K_JRC, K_DJNZ, K_JP, K_JPC = range(8)
WC = 0x80

# Patched output ops (the byte after the io RST). Plain and trace forms.
TRACE_OUTN = range(0x18, 0x20)          # OUT (n),A to port class op & 7
TRACE_OUTI, TRACE_OUTD = 0xC3, 0xCB


def trace_op(op):
    """Plain output op -> trace op, or None if it is not an output op."""
    if op < 8:
        return 0x18 + op
    if op == 0xA3:
        return TRACE_OUTI
    if op == 0xAB:
        return TRACE_OUTD
    if op & 0xC7 == 0x41:
        return op + 0x40
    return None


def out_kind(op):
    """Patched op -> ('n', class) | ('outi',) | ('outd',) | ('c', r) | None."""
    if op < 8 or op in TRACE_OUTN:
        return ('n', op & 7)
    if op in (0xA3, TRACE_OUTI):
        return ('outi',)
    if op in (0xAB, TRACE_OUTD):
        return ('outd',)
    if op & 0xC7 in (0x41, 0x81):
        return ('c', (op >> 3) & 7)
    return None


def table():
    t = [0] * 256

    def s(op, kind, ln, wc=False):
        t[op] = kind << 2 | ln | (WC if wc else 0)
    s(0x00, K_COPY, 1)
    for d in range(8):
        for r in range(8):
            op = 0x40 + d * 8 + r
            if d == 6:          # LD (HL),r and HALT
                continue
            s(op, K_COPY, 1, d == 1)
    for op in range(0x80, 0xC0):
        s(op, K_COPY, 1)
    for r in (0, 1, 2, 3, 4, 5, 7):
        s(0x04 + 8 * r, K_COPY, 1, r == 1)
        s(0x05 + 8 * r, K_COPY, 1, r == 1)
        s(0x06 + 8 * r, K_COPY, 2, r == 1)
    for op in (0x03, 0x0B, 0x13, 0x1B, 0x23, 0x2B):
        s(op, K_COPY, 1, op in (0x03, 0x0B))
    for op in (0x09, 0x19, 0x29, 0x0A, 0x1A, 0x07, 0x0F, 0x17, 0x1F, 0x27, 0x2F, 0x37, 0x3F, 0xEB):
        s(op, K_COPY, 1)
    for op in range(0xC6, 0x100, 8):
        s(op, K_COPY, 2)
    s(0x01, K_COPY, 3, True)
    s(0x11, K_COPY, 3)
    s(0x21, K_COPY, 3)
    s(0xCB, K_CB, 2)
    s(0x18, K_JR, 2)
    for op in (0x20, 0x28, 0x30, 0x38):
        s(op, K_JRC, 2)
    s(0x10, K_DJNZ, 2)
    s(0xC3, K_JP, 3)
    for op in range(0xC2, 0x100, 8):
        s(op, K_JPC, 3)
    return t


def cb_ok(b):
    """CB second byte: (allowed, writes C)."""
    return (b & 7) != 6, (b & 7) == 1 and not 0x40 <= b < 0x80


# Bytes the trace code takes per instruction (worst case for jumps), and
# the room it has: TR_BUDGET in trace.asm, the end stub included.
SIZE_BUDGET = 120
END_STUB = 5


def emit_size(kind, ln, op=None):
    if kind in (K_COPY, K_CB):
        return ln
    if kind == 'site':
        k = out_kind(op)
        return 6 if k[0] == 'c' and k[1] != 7 else 3
    if kind == K_JR or kind == K_JP:
        return 5
    if kind in (K_JRC, K_JPC):
        return 8
    if kind == K_DJNZ:
        return 9
    raise ValueError(kind)


def decode(rd, a, rst):
    """Instruction at CPU address a: (kind, length, size, target_or_op, wc, co).
    rd(addr) gives the byte the framework will see (patches applied)."""
    b0 = rd(a)
    if b0 == rst:
        op = rd(a + 1)
        k = out_kind(op)
        if k is None:
            return (K_BAD, 0, 0, None, False, False)
        co = k[0] != 'n'
        return ('site', 2, emit_size('site', 2, op), op, False, co)
    t = TABLE[b0]
    if not t:
        return (K_BAD, 0, 0, None, False, False)
    ln, kind, wc = t & 3, (t >> 2) & 7, bool(t & WC)
    if kind == K_CB:
        ok, wc = cb_ok(rd(a + 1))
        if not ok:
            return (K_BAD, 0, 0, None, False, False)
        return (K_CB, 2, 2, None, wc, False)
    if kind == K_COPY:
        return (K_COPY, ln, ln, None, wc, False)
    if kind in (K_JR, K_JRC, K_DJNZ):
        e = rd(a + 1)
        tgt = (a + 2 + (e - 256 if e > 127 else e)) & 0xFFFF
    else:
        tgt = rd(a + 1) | rd(a + 2) << 8
    return (kind, ln, emit_size(kind, ln), tgt, False, False)


def region(rd, s, rst):
    """The framework's choice of copied range for a trace at site s.
    Returns (H, E, outputs, loop): outputs = output sites in [H, E),
    loop = a jump inside the range goes back. None if the site cannot
    start a trace."""
    st = {'size': 0, 'flags': 0, 'tg': []}
    k0 = out_kind(rd(s + 1))
    nport = k0[0] == 'n'
    cls = k0[1] if nport else None

    def take(d):
        kind, ln, sz, tgt, wc, co = d
        if kind == K_BAD:
            return False
        if st['size'] + sz > SIZE_BUDGET - END_STUB:
            return False
        if kind == 'site':
            # An OUT (n),A trace takes OUT (n),A of its class; a port C
            # trace takes port C outputs and OUT (n),A of C's class (not
            # known here, taken as matching).
            k = out_kind(tgt)
            if not co:
                if nport and k[1] != cls:
                    return False
            else:
                if nport or st['flags'] & 2:
                    return False
                st['flags'] |= 1
        else:
            if kind not in (K_COPY, K_CB) and len(st['tg']) >= 8:
                return False
            if wc:
                if st['flags'] & 1:
                    return False
                st['flags'] |= 2
            if kind not in (K_COPY, K_CB):
                st['tg'].append(tgt)
        st['size'] += sz
        return True
    a, back = s, None
    while True:
        d = decode(rd, a, rst)
        if not take(d):
            break
        kind, ln = d[0], d[1]
        if kind not in (K_COPY, K_CB, 'site'):
            if d[3] <= s or kind in (K_JR, K_JP):
                if d[3] < s:
                    back = d[3]
                a += ln
                break
        a += ln
    e = a
    if e == s:
        return None
    h = s
    if back is not None:
        keep = dict(st, tg=list(st['tg']))
        a, ok = back, False
        while a < s:
            d = decode(rd, a, rst)
            if not take(d) or d[0] in (K_JR, K_JP):
                break
            a += d[1]
        ok = a == s
        if ok:
            h = back
        else:
            st.update(keep)
    outs, loop, a = 0, False, h
    while a < e:
        d = decode(rd, a, rst)
        if d[0] == 'site':
            outs += 1
        elif d[0] not in (K_COPY, K_CB) and h <= d[3] <= a:
            loop = True
        a += d[1]
    return h, e, outs, loop


TABLE = table()


def choose(rd, s, rst):
    """Does a trace op at site s pay? A run of two or more patched outputs
    in a row (done in one call, no copy), a loop over the site, or straight
    code with three or more outputs (copied once and kept)."""
    k0, k1 = out_kind(rd(s + 1)), out_kind(rd(s + 3)) if rd(s + 2) == rst else None
    if k1 is not None and (k0[0] != 'n' or (k1[0] == 'n' and k1[1] == k0[1])):
        return True               # a run: an OUT (n),A run takes OUT (n),A of its class
    r = region(rd, s, rst)
    if not r:
        return False
    if not r[3]:
        return r[2] >= 3          # straight code with 3 or more outputs
    return not short_djnz(rd, r[0], r[1], rst)


def short_djnz(rd, h, e, rst):
    """A DJNZ loop that LD B,n with n < 8 sets up just before its head:
    a few passes per call, so the copy costs more than it saves."""
    a, last = h, None
    while a < e:
        d = decode(rd, a, rst)
        last = d
        a += d[1]
    if not last or last[0] != K_DJNZ:
        return False
    for k in range(2, 9):
        a, n, ok = h - k, 0, False
        while a < h and n < 4:
            d = decode(rd, a, rst)
            if d[0] != K_COPY:
                break
            if rd(a) == 0x06 and rd(a + 1) < 8:
                ok = True
            a += d[1]
            n += 1
        if a == h and ok:
            return True
    return False
