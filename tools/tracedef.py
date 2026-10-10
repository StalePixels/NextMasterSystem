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
TR_NT = 8           # jump targets one copy may hold
TR_RMAX = 250       # most sites in one run: (TR_CODE >> 8) - 1


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


def port_class(p):
    """Port -> the framework's port class (port_class in src/runtime/fw.asm,
    pclass in mknms.py)."""
    return (p >> 7 & 1) << 2 | (p >> 6 & 1) << 1 | (p & 1)


VDP_DATA = port_class(0xBE)

# Unprefixed opcodes: 2-byte and 3-byte ones (the rest are 1 byte, CB 2)
_LEN2 = set(range(0x06, 0x40, 8)) | set(range(0xC6, 0x100, 8)) | \
    {0x10, 0x18, 0x20, 0x28, 0x30, 0x38, 0xD3, 0xDB, 0xCB}
_LEN3 = {0x01, 0x11, 0x21, 0x31, 0x22, 0x2A, 0x32, 0x3A, 0xC3, 0xCD} | \
    set(range(0xC2, 0x100, 8)) | set(range(0xC4, 0x100, 8))
# Opcodes that leave straight-line code: jumps, calls, returns, RST, HALT
_FLOW = {0x10, 0x18, 0x20, 0x28, 0x30, 0x38, 0xC3, 0xCD, 0xC9, 0xE9, 0x76} | \
    set(range(0xC2, 0x100, 8)) | set(range(0xC4, 0x100, 8)) | \
    set(range(0xC0, 0x100, 8)) | set(range(0xC7, 0x100, 8))
# Opcodes that write C: LD C,r / n, INC C, DEC C, INC BC, DEC BC, POP BC, EXX
_WC = set(range(0x48, 0x50)) | {0x0E, 0x0C, 0x0D, 0x01, 0x03, 0x0B, 0xC1, 0xD9}
# ED opcodes that write C: IN C,(C), LD BC,(nn), LDI, CPI, LDD, CPD and repeats
_ED_WC = {0x48, 0x4B, 0xA0, 0xA1, 0xA8, 0xA9, 0xB0, 0xB1, 0xB8, 0xB9}
_ED_FLOW = {0x45, 0x4D, 0x55, 0x5D, 0x65, 0x6D, 0x75, 0x7D}
_ED_LEN4 = {0x43, 0x4B, 0x53, 0x5B, 0x63, 0x6B, 0x73, 0x7B}


def _straight(rd, a, rst):
    """Instruction at a, as seen with the patches in place: (length, writes
    C) for straight-line code; None for a jump, call, return or anything
    not known here."""
    b = rd(a)
    if b == rst:
        op = rd(a + 1)
        if op < 0x10 or 0x18 <= op < 0x20 or 0x30 <= op < 0x40:
            return 2, False
        if 0x40 <= op < 0xC0 and op != 0x80:
            return 2, op == 0x48
        return None
    if b in _FLOW:
        return None
    if b == 0xCB:
        c = rd(a + 1)
        return 2, (c & 7) == 1 and not 0x40 <= c < 0x80
    if b == 0xED:
        c = rd(a + 1)
        if c in _ED_FLOW:
            return None
        return (4 if c in _ED_LEN4 else 2), c in _ED_WC
    if b in (0xDD, 0xFD):
        c = rd(a + 1)
        if c in (0xE9, 0xDD, 0xFD, 0xED):
            return None
        if c == 0xCB:
            return 4, (rd(a + 3) & 7) == 1 and not 0x40 <= rd(a + 3) < 0x80
        if c in (0x21, 0x22, 0x2A, 0x36):
            return 4, False
        if c in (0x34, 0x35) or (0x40 <= c < 0xC0 and ((c & 7) == 6 or (c & 0xF8) == 0x70) and c != 0x76):
            return 3, c == 0x4E
        if c in _FLOW:
            return None
        n = 3 if c in _LEN3 else 2 if c in _LEN2 else 1
        return 1 + n, c in _WC
    return (3 if b in _LEN3 else 2 if b in _LEN2 else 1), b in _WC


def port_c(rd, s, rst):
    """The port in C at site s when straight-line code before it loads C
    (LD C,n or LD BC,nn, at most 48 bytes back, with no jump or other write
    of C between), else None."""
    for a in range(s - 2, max(s - 48, 0) - 1, -1):
        if rd(a) == 0x0E:
            c, p = rd(a + 1), a + 2
        elif rd(a) == 0x01:
            c, p = rd(a + 1), a + 3
        else:
            continue
        while p < s:
            d = _straight(rd, p, rst)
            if d is None or d[1]:
                break
            p += d[0]
        if p == s:
            return c
    return None


def c_class(rd, s, rst, block):
    """Port C's class at site s (the runtime's game_class there): from
    port_c, else, when the outputs met include OUTI or OUTD (block), the
    VDP data port, the usual target of a block output. None when it cannot
    be told."""
    c = port_c(rd, s, rst)
    if c is not None:
        return port_class(c)
    return VDP_DATA if block else None


class _Copy:
    """The runtime's running totals while it decides what a copy takes
    (tr_take in src/runtime/trbuild.asm): worst-case code size, the port C
    flags and the jump targets. nport: an OUT (n),A trace; cls: its class,
    or for a port C trace port C's class (c_class, None if not known)."""

    def __init__(self, nport, cls):
        self.nport, self.cls = nport, cls
        self.size, self.flags, self.tg = 0, 0, []

    def keep(self):
        return self.size, self.flags, list(self.tg)

    def put_back(self, k):
        self.size, self.flags, self.tg = k[0], k[1], list(k[2])

    def take(self, d):
        """May instruction d join the copy? Updates the totals when it may."""
        kind, ln, sz, tgt, wc, co = d
        if kind == K_BAD:
            return False
        if self.size + sz > SIZE_BUDGET - END_STUB:
            return False
        if kind == 'site':
            k = out_kind(tgt)
            if not co:
                # OUT (n),A: its class must be the trace's, in a port C
                # trace port C's class; one not known is taken as
                # different, so the copy ends here at the latest
                if self.cls is None or k[1] != self.cls:
                    return False
            else:
                if self.nport or self.flags & 2:
                    return False
                self.flags |= 1
        else:
            if kind not in (K_COPY, K_CB) and len(self.tg) >= TR_NT:
                return False
            if wc:
                if self.flags & 1:
                    return False
                self.flags |= 2
            if kind not in (K_COPY, K_CB):
                self.tg.append(tgt)
        self.size += sz
        return True


def region(rd, s, rst):
    """The copy the runtime makes for a trace at site s (tr_build in
    src/runtime/trbuild.asm), or None when it cannot make one and runs
    the site as a single output.

    Forward from the site it takes instructions while tr_take allows,
    and stops after a jump back to the site or before it (a loop over the
    site), or after a JR or JP. A jump before the site gives a loop head:
    the code from it to the site is copied too when all of it may be. No
    copy is made when nothing fits, when there is no loop over the site
    and fewer than three outputs, or when a jump inside the copy lands
    inside an instruction. A loop inside the copy that does not go back
    over the site (a delay loop after an output) does not count.

    Returns (H, E, outputs, loop): the copied range [H, E), the output
    sites in it, and whether the copy holds the loop over the site (False
    also when the loop's head could not be copied: the copy then runs once
    per pass, like straight code)."""
    k0 = out_kind(rd(s + 1))
    if k0[0] == 'n':
        cp = _Copy(True, k0[1])
    else:
        cp = _Copy(False, c_class(rd, s, rst, k0[0] in ('outi', 'outd')))
    a, back, loop_rt, nout = s, None, False, 0
    starts = []
    while True:
        d = decode(rd, a, rst)
        if not cp.take(d):
            break
        starts.append(a)
        kind, ln = d[0], d[1]
        if kind == 'site':
            nout += 1
        elif kind not in (K_COPY, K_CB):
            t = d[3]
            if t <= s:
                loop_rt = True
                if t < s:
                    back = t
                a += ln
                break
            if kind in (K_JR, K_JP):
                a += ln
                break
        a += ln
    e = a
    if e == s or not (loop_rt or nout >= 3):
        return None
    h = s
    if back is not None:
        keep = cp.keep()
        a, hstarts = back, []
        while a < s:
            d = decode(rd, a, rst)
            if not cp.take(d) or d[0] in (K_JR, K_JP):
                break
            hstarts.append(a)
            a += d[1]
        if a == s:
            h = back
            starts = hstarts + starts
        else:
            cp.put_back(keep)
    # pass 2: a jump inside [H, E] must land on an instruction (tr_find)
    marks = set(starts) | {e}
    for a in starts:
        d = decode(rd, a, rst)
        if d[0] not in (K_COPY, K_CB, 'site') and h <= d[3] <= e and d[3] not in marks:
            return None
    return h, e, nout, loop_rt and (back is None or h == back)


def run_scan(rd, s, rst):
    """Sites in a row from s as the runtime counts them (tr_rscan): every
    2-byte step that starts with the io RST, at most TR_RMAX."""
    n, a = 0, s
    while True:
        a += 2
        n += 1
        if n == TR_RMAX or rd(a) != rst:
            return n


def run_loop(rd, s, n, rst):
    """Does a conditional jump back to the site or before it come within
    six instructions after a run of n sites? The runtime then copies the
    run and its loop instead of doing it as a run (tr_build)."""
    a = s + 2 * n
    for _ in range(6):
        d = decode(rd, a, rst)
        if d[0] in (K_COPY, K_CB):
            a += d[1]
            continue
        return d[0] in (K_JRC, K_DJNZ, K_JPC) and d[3] <= s
    return False


def run_effective(rd, s, n, rst):
    """The outputs a run of n sites at s does in one call (tr_runs), and
    their kinds. It stops at an output to another port class than the
    first site's: an OUT (n),A of another class than port C's in a port C
    run, a port C output in an OUT (n),A run unless port C has the run's
    class (port C's class from c_class; one not known ends the run)."""
    ks = []
    for i in range(n):
        k = out_kind(rd(s + 2 * i + 1))
        if k is None:
            break
        ks.append(k)
    if not ks:
        return 0, set()
    ccls = c_class(rd, s, rst, any(k[0] in ('outi', 'outd') for k in ks))
    nport = ks[0][0] == 'n'
    kinds, i = set(), 0
    for k in ks:
        if k[0] == 'n':
            if k[1] != (ks[0][1] if nport else ccls):
                break
        elif nport and ccls != ks[0][1]:
            break
        kinds.add(k[0])
        i += 1
    return i, kinds


def verdict(rd, s, rst):
    """What the runtime does with a trace op at site s:
    ('run', outputs, kinds) for a run of sites in a row done in one call,
    ('copy', H, E, outputs, loop) for a copy of the code (region), or
    ('single',) when it can make neither and runs the site alone."""
    n = run_scan(rd, s, rst)
    if n >= 2:
        if run_loop(rd, s, n, rst):
            r = region(rd, s, rst)
            if r:
                return ('copy',) + r
        return ('run',) + run_effective(rd, s, n, rst)
    r = region(rd, s, rst)
    if r:
        return ('copy',) + r
    return ('single',)


TABLE = table()


# RUN_BREAK_EVEN: the shortest run of patched outputs in a row, by the kinds
# of output in it, that one call does more cheaply than the same outputs as
# single traps. Measured in Next cycles with a test cart on the ABI 7
# engine; a run's cost is set by the runtime's run handlers in
# src/runtime/trace.asm, so re-measure and update this table when they
# change.
#   'outi', 'outd': only OUTI or only OUTD, sent as one block. A run costs
#     about 4,600 + 24 per byte in tile data and the sprite table and + 290
#     in the name table, against 1,871, 1,689 and 2,061 per single OUTI: a
#     run of 3 is cheaper in every region.
#   'mixed': OUTI or OUTD together with other outputs, done site by site and
#     sent as one block. With three OUTI to one OUT (n),A, 4 is cheaper in
#     every VRAM region.
#   'other': only OUT (n),A and OUT (C),r, sent as one block from 3 bytes.
#     A run of OUT (n),A is cheaper from 7 in the name table and the sprite
#     table (6 in tile data), a run of OUT (C),A from 5 or 6. The VDP
#     address as a run of OUT (C),L; OUT (C),H costs 4,244 against 2,163 as
#     two single writes.
# CRAM runs pay sooner (from 2 or 3), but the builder does not know the
# region, and VRAM writes are far more common.
RUN_BREAK_EVEN = {'outi': 3, 'outd': 3, 'mixed': 4, 'other': 7}


def run_break_even(kinds):
    """Break-even length of a run whose outputs are of these out_kind kinds."""
    if kinds in ({'outi'}, {'outd'}):
        return RUN_BREAK_EVEN[next(iter(kinds))]
    if kinds & {'outi', 'outd'}:
        return RUN_BREAK_EVEN['mixed']
    return RUN_BREAK_EVEN['other']


def choose(rd, s, rst):
    """Does a trace op at site s pay? Only where the runtime can do more
    than the single output (verdict): a run done in one call from its
    RUN_BREAK_EVEN length on; a copy with a loop, unless short_djnz; a copy
    with no loop (three or more outputs, copied once and kept)."""
    v = verdict(rd, s, rst)
    if v[0] == 'run':
        return v[1] >= 2 and v[1] >= run_break_even(v[2])
    if v[0] == 'copy':
        if v[4]:
            return not short_djnz(rd, v[1], v[2], rst)
        return v[3] >= 3
    return False


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
