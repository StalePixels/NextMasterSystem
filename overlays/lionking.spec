# The Lion King (Europe, Brazil) (En), CRC32 C352C7EB, 512K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the 60 s and the bank-aware 600 s reference
# I/O logs and these extra entry points (the scanner does not follow them): the object handler table
# in bank 31 that $6B89 jumps through (JP (IX), bank 31 set at $6AF3): $6E39 and 1F:8570 8571 857E
# 8587 8594 85CF 85E7 85EF 860D 8620 862F 863E 8655 8668 8673 8684 8699 86CF 86E4 86E8 86F1 86FE
# 8719 8730 8741.
# Spec gaps (data/scan-verdicts.tsv): unused are the bank 0 routines $0589, $0B0B and $1000 and the
# sound driver's own interrupt entry in bank 6 ($A1BB); false are the byte patterns in graphics banks.
# Register 0 has line interrupts on; register 10 is $FF, so no line interrupt fires, except in
# level index 3 (the stampede, $C640 = 3; $C644 set at $3B3B), where $3DA8 writes register 10 =
# $0F and the handler's $04AD sets H for 16-line bands. Checked by setting $C640 to 3 at the level
# start $3471 on both machines. Each band's H still applies 2-3 lines later than on the Master
# System (the line event's delivery and the handler's traps); a rastercode routine would place the
# lines exactly, but this level has V scroll $DE and the runtime's per-line copper list has no
# V scroll wrap.
name The Lion King
cart C352C7EB
hz 50		; No-Intro regions Europe, Brazil
# The game uses no RST. Its sprite list writers run once with a null list pointer ($C6F6 = 0
# after the RAM clear) and write $0000-$0024 of the cart copy, so the vector is $30.
vector 30 io
# Level index 3 (the stampede): register 10 is $0F, so a line event comes every 16 lines, and the
# frame and line handler ($045B) sets H from the table at $D803, chosen by the V counter it reads
# at $04B0. On the Master System the k-th event of a picture reads $0F + 16 (k - 1), takes entry
# min(k, 10) of the table, and its register 8 write in line 16k applies from line 16k + 1. On the
# Next the handler is entered at the end of line 16k, reads the V counter about 2 lines later
# ($11, $21, ...), took the next band's entry, and its write applied 2-3 lines late.
# lvirq, a native cave at the handler's entry ($045B, DI : PUSH AF : PUSH BC : PUSH DE become
# JP lvirq), counts the events of a picture in lv_n ($DE02; the frame event clears it). In the
# stampede (register 10 $0F, ($C644) set, line interrupts on, no locked rows, display on, 192
# lines, no rastercode table) it then, for event k, at once (the end of line 16k):
# - writes band k's X into NextReg $2F/$30 and $16, as hscroll_set computes them (K = -H,
#   X = K - 34 mod 320, Layer 2 X = K - 2), so the band starts on line 16k + 1;
# - writes band k's map switch column into copper lines 16k+1 to 16k+16, and band k+1's column
#   into its first line (the copper reads a line's WAIT during the line before), while the
#   runtime's normal list has its switch pairs (cop_mode 0, cop_sw neither 0 nor $FF); the frame
#   event writes band 1's column into line 17.
# The game's own register 8 write then goes through the runtime and sets the same X. lv_line, at
# $04B0 in place of IN A,($7E) : ADD A,$10, returns the V counter the Master System gives the
# k-th event (16k - 1, plus $10), so the game takes the same entry. No hsplit: lines 0-16 keep the
# runtime's column from the frame's H, and the cave owns the column of lines 18-191.
# Runtime internals lvirq uses (runtime map of public/ at the time of writing): vdp_regs $E03B,
# vdp_status $E03A, cur_mmu $E02D, m224 $E08F, hl_on $E096; in part 2 (page 25, mapped at MMU4
# for the read with interrupts off) cop_sw $27B3 and cop_mode $27B5; the normal list's line y
# WAIT first byte at copper address 6 + 10y, $80 + 2 x column (cop_switches); the column 39 for
# K <= 64, else (291 - K) / 8 (hscroll_set).
# $DE00-$DE7F (the cave's state and its own stack) is RAM the game clears at power-on and never
# writes again in the reference logs or in the stampede runs. The cave code is in $7A00-$7BFF,
# $FF fill before the bit-reverse table at $7C00 in bank 1 (slot 1 always holds bank 1).
label lvirq 07A00
asm 0045B 4          ; DI : PUSH AF : PUSH BC : PUSH DE
    jp lvirq
    nop
endasm
asm 07A00 400        ; lvirq, in free bytes of bank 1
        OPT --zxnext
VREGS   equ $E03B
VSTAT   equ $E03A
CURMMU  equ $E02D
M224    equ $E08F
HLON    equ $E096
COPSW   equ $87B3               ; cop_sw ($27B3) with page 25 at MMU4
COPMODE equ $87B5               ; cop_mode ($27B5)
LVSP    equ $DE00
LVN     equ $DE02
LVSTK   equ $DE80
        di                      ; lvirq
        ld (LVSP),sp
        ld sp,LVSTK
        push af
        push bc
        push de
        push hl
        ld a,(VSTAT)            ; frame event: clear the count
        rla
        jr nc,.line
        xor a
        ld (LVN),a
        call lvok
        jr nz,.out
        ld a,1                  ; band 1's column into line 18
        call lvh
        call lvcol
        ld b,18
        ld e,1
        call lvwl
        jr .out
.line:  ld a,(LVN)
        inc a
        ld (LVN),a
        ld c,a                  ; C = k
        call lvok
        jr nz,.out
        ld a,c
        call lvh                ; A = K of band k
        push af
        ld e,a
        ld d,0
        ld hl,-34
        add hl,de
        bit 7,h
        jr z,.pos
        ld de,320
        add hl,de
.pos:   ld a,c                  ; wait for line 16k + 2, and write the X as it starts
        add a,a
        add a,a
        add a,a
        add a,a
        add a,2
        ld b,a
.wt:    call lvline
        cp b
        jr c,.wt
        ld a,h
        nextreg $2F,a
        ld a,l
        nextreg $30,a
        pop af
        sub 2
        nextreg $16,a           ; Layer 2 X
        ld a,c
        call lvh
        call lvcol              ; D = band k's column
        ld a,b                  ; B = 16k + 2
        cp 192
        jr nc,.out
        ld a,191+1
        sub b
        cp 16
        jr c,.n
        ld a,16
.n:     ld e,a
        call lvwl
        ld a,b                  ; band k+1's first line
        add a,16
        cp 192
        jr nc,.out
        ld b,a
        ld a,c
        inc a
        call lvh
        call lvcol
        ld e,1
        call lvwl
.out:   pop hl
        pop de
        pop bc
        pop af
        ld sp,(LVSP)
        push af
        push bc
        push de
        jp $045F
; A = the beam's line (NextReg $1E, $1F; the picture's line in 192-line mode), 255 from line 256
; on. Uses A; keeps the others.
lvline: push bc
        push de
.rd:    ld bc,$243B
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        ld e,a
        dec b
        ld a,$1F
        out (c),a
        inc b
        in a,(c)
        ld d,a
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        cp e
        jr nz,.rd
        rra
        ld a,d
        jr nc,.ok
        ld a,255
.ok:    pop de
        pop bc
        ret
; Z when the stampede's bands are on and the list can take columns. Uses A; with page 25 at
; MMU4 for the read, MMU4 back from cur_mmu.
lvok:   ld a,(VREGS+10)
        cp $0F
        ret nz
        ld a,($C644)
        or a
        jr z,.no
        ld a,(VREGS+0)
        and $50
        cp $10
        ret nz
        ld a,(VREGS+1)
        and $40
        jr z,.no
        ld a,(M224)
        or a
        ret nz
        ld a,(HLON)
        or a
        ret nz
        nextreg $54,25
        ld a,(COPMODE)
        or a
        jr nz,.back
        ld a,(COPSW)
        inc a                   ; $FF: no switch pairs yet
        jr z,.nz
        dec a                   ; 0: no switch pairs
        jr z,.nz
        xor a
        jr .back
.nz:    or 1
.back:  push af
        ld a,(CURMMU+4)
        nextreg $54,a
        pop af
        ret
.no:    or 1
        ret
; A = band (1-11) -> A = K = -H of the table entry min(band, 10). Uses A, HL, D (keeps E).
lvh:    cp 11
        jr c,.k
        ld a,10
.k:     cp 10
        jr c,.k2
        ld a,10
.k2:    ld l,a
        add a,a
        add a,a
        add a,a
        sub l                   ; 7 x band
        add a,3
        ld l,a
        ld h,$D8
        ld a,(hl)
        neg
        ret
; A = K -> D = map switch column (39 for K <= 64, else (291 - K) / 8). Uses A.
lvcol:  cp 65
        ld d,39
        ret c
        ld d,a
        ld a,255&(291-256)
        sub d
        rrca
        rrca
        rrca
        and $1F
        ld d,a
        ret
; D = column, B = first line, E = lines: the first byte of each line's WAIT. Uses A, HL; keeps
; BC, DE.
lvwl:   push bc
        push de
        ld a,d
        add a,a
        or $80
        ld c,a                  ; C = the WAIT byte
        ld a,e
        push af                 ; lines
        ld d,10
        ld e,b
        mul d,e
        ld hl,6
        add hl,de
        pop af
        ld b,a
.one:   ld a,h
        or %11000000
        nextreg $62,a
.l:     ld a,l
        nextreg $61,a
        ld a,c
        nextreg $60,a
        ld a,l
        add a,10
        ld l,a
        jr c,.c
        djnz .l
        jr .end
.c:     inc h
        djnz .one
.end:   pop de
        pop bc
        ret
endasm
asm 004B0 4          ; IN A,($7E) : ADD A,$10
    rst $30
    db far_io, pg_lv_line, ent_lv_line
endasm
asm 0029A 2   ; IM 1 -> IM 2
    im 2
endasm
# Delay $0F78 (B units, 0 means 256, of a 16 x 256-pass NOP; DJNZ loop): a busy loop of 69,960
# T-states a unit, about 75,000 with the frame handler that cuts into it (measured on the reference:
# 73,117-76,994 T a unit). Every timed screen uses it: the Disney and Virgin screens, the sunrise and
# title fades, and the pauses in play. At 28 MHz the loop ran about 8 times too fast and the intro
# screens showed for about a tenth of their time. Page entry delay waits the Master System's real
# time on the Next's raster line: 21.1 ms a unit with interrupts on (329 lines at 50 Hz, 335 at
# 60 Hz), 19.7 ms with them off (307 and 313 lines), from a PAL Master System's 3.547 MHz.
asm 00F78 5          ; PUSH BC : PUSH HL : LD H,B : LD C,$10
    rst $30
    db far_io, pg_delay, ent_delay
    ret
endasm
# Power-on delay $0280-$028C (LD B,4 : LD HL,$FFFF : DEC HL ... DJNZ): 4 x 65,535 passes of 24
# T-states, about 1.77 s on a PAL Master System, with interrupts off. It runs as 90 units of the
# delay entry (19.7 ms each with interrupts off) and leaves B, HL and A at 0, as the loop does.
asm 00280 13         ; LD B,4 : LD HL,$FFFF : DEC HL : LD A,L : OR H : JP NZ : DJNZ
    ld b,90
    rst $30
    db far_io, pg_delay, ent_delay
    ld b,0
    ld hl,0
    xor a
endasm
# Sprite tile uploads. The uploader ($0B15, and $0B79 for a mirrored object) writes A tiles of an
# object's animation frame from the cart into a sprite tile buffer, in one of four forms: 4 planes
# as stored (OUTI loop at $0B34), 3 planes with a fourth plane of 0 ($0B4C, when the object's
# (IX+$2B) bit 0 is set), and both mirrored through the bit-reverse table at $7C00 ($0B98 and
# $0C4D, unrolled LD E,(HL) : LD A,(DE) : OUT ($BE),A). The 3-plane form ran each row as 4 single
# traps (the trace builder makes no copy of a loop with the LD ($0007),A delays in it), and the
# mirrored forms ran as copied traces of 32 table lookups; an upload of 9 tiles took up to 360,000
# cycles, and play fell behind the Master System's one game step a frame. Page entries spr3, spr3f
# and spr4f build the tile bytes in their page and write them with one jt_vwrite call for up to 64
# tiles. The 4-plane OUTI loop runs as a copied trace at about the speed of a block and is left.
asm 00B4C 5          ; DI : LD C,$BF : OUT (C),E
    rst $30
    db far_io, pg_spr3, ent_spr3
    ret
endasm
asm 00B98 5          ; DI : LD C,$BF : OUT (C),E
    rst $30
    db far_io, pg_spr4f, ent_spr4f
    ret
endasm
asm 00C4D 5          ; DI : LD C,$BF : OUT (C),E
    rst $30
    db far_io, pg_spr3f, ent_spr3f
    ret
endasm
# Name table fill $055E-$0588 (in $0533, the screen reset that every screen change calls): 896
# entries of tile 0 with the sprite palette ($00, $08) from $3800, with interrupts off, as
# OUT (C),E / OUT (C),D traps: about 2,900,000 cycles, so a screen change held the runtime for
# several frames (one measured frame 107%). Page entry ntfill writes the same 1,792 bytes with
# jt_vwrite, and only the runs of entries that differ from it in the runtime's VRAM copy
# (page 29, SHADOW_PAGE + 1, read at MMU4 with interrupts off): the game calls $0533 again and
# again at some screen changes, with the table already filled. It then waits, with interrupts
# off, for the loop's time on a PAL Master System (about 69,900 T: 307 Next lines at 50 Hz), so
# the screen changes keep their length.
asm 0055E 7          ; DI : LD HL,$7800 : LD BC,$00BF
    rst $30
    db far_io, pg_ntfill, ent_ntfill
    ret
endasm
# Tile loader $067B (B tiles from HL to the VRAM address in DE, OUTI : NOP : DJNZ, 32 bytes a
# tile, with interrupts off): a level start loads about 190 tiles in one call. The copied trace
# of the OUTI run took about 640,000 cycles in the runtime before the next once-a-frame work (a
# measured frame of 113%); on the Master System the loop takes about 1,092 T a tile, about three
# frames with interrupts off. Page entry tload writes the tiles with jt_vwrite in one-byte runs
# (the runtime's fast form for tile data), then waits with interrupts off for the loop's time
# on a PAL Master System (4.75 Next lines a tile at 50 Hz, 4.875 at 60 Hz).
asm 0067B 5          ; DI : LD C,$BF : OUT (C),E
    rst $30
    db far_io, pg_tload, ent_tload
    ret
endasm
page 0 delay spr3 spr3f spr4f lv_line ntfill tload
        OPT --zxnext
; delay: as the game's $0F78-$0F8C, in real time. Returns as the game's routine does: A, BC, DE, HL
; kept, F as after its last DEC H (Z and N set, carry kept). The interrupt state stays as it was;
; each line read runs with interrupts off, so a handler cannot change the NextReg select port
; between the select and the read. The stack holds no more than the game's routine puts there.
delay:  push af
        ld (sv_hl),hl
        ld (sv_de),de
        ld (sv_bc),bc
        ld a,i                  ; P/V: interrupts on at entry
        ld a,0
        jp po,.di
        inc a
.di:    ld (dirq),a
        ld l,b                  ; units: B, 0 means 256
        ld h,0
        ld a,b
        or a
        jr nz,.nz
        inc h
.nz:    ld (dunits),hl
        di
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld hl,311               ; lines in a 50 Hz frame
        ld de,329               ; a unit with the frame handler running
        bit 2,a
        jr z,.hz
        ld hl,264               ; 60 Hz
        ld de,335
.hz:    ld (dlen),hl
        ld a,(dirq)
        or a
        jr nz,.on
        ld hl,-22               ; interrupts off: no handler time, 307 or 313 lines
        add hl,de
        ex de,hl
.on:    ld (dunit),de
        call dline
        ld (dprev),hl
        ld hl,(dunit)
        ld (dleft),hl
.poll:  call dline              ; HL = this line
        ld de,(dprev)
        ld (dprev),hl
        or a
        sbc hl,de               ; lines since the last read
        jr nc,.pos
        ld de,(dlen)
        add hl,de               ; the frame wrapped
.pos:   ex de,hl
        ld hl,(dleft)
        or a
        sbc hl,de
.chk:   ld (dleft),hl
        bit 7,h
        jr nz,.unit
        ld a,h
        or l
        jr nz,.poll
.unit:  ld de,(dunits)          ; a unit is over
        dec de
        ld (dunits),de
        ld a,d
        or e
        jr z,.end
        ld de,(dunit)
        add hl,de
        jr .chk
.end:   ld hl,(sv_hl)
        ld de,(sv_de)
        ld bc,(sv_bc)
        pop af
        push hl
        ld h,1
        dec h                   ; the game's last DEC H: Z, N, carry kept
        pop hl
        ret
; HL = the Next's raster line (0-310). Interrupts off for the read, then as at the entry. The high
; bit is read again after the low byte, and the read repeats when it changed (line 255 to 256).
dline:  di
        ld bc,$243B
.again: ld a,$1E
        out (c),a
        inc b
        in h,(c)
        dec b
        ld a,$1F
        out (c),a
        inc b
        in l,(c)
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        dec b
        xor h
        and 1
        jr nz,.again
        ld a,h
        and 1
        ld h,a
        ld a,(dirq)
        or a
        ret z
        ei
        ret
dirq:   db 0
dunits: dw 0
dunit:  dw 0
dlen:   dw 0
dprev:  dw 0
dleft:  dw 0
sv_hl:  dw 0
sv_de:  dw 0
sv_bc:  dw 0
;
;
; Sprite tile uploads, as the game's $0B4C-$0B78 (spr3), $0C4D-$0D11 (spr3f) and $0B98-$0C4C
; (spr4f). In: DE = VRAM address (bit 6 of D may be clear), HL = the source, A = tiles (0 means
; 256); 24 source bytes a tile for the 3-plane forms (3 a row, the fourth byte 0), 32 for spr4f.
; The mirrored forms take each source byte through the game's bit-reverse table at $7C00 (slot 1).
; Each returns as the game's code does: HL past the source, B = 0, C = $BE, Z and N set and carry
; kept, IX and IY kept, VDP address after the last byte, latch clear; spr3: D with bit 6 set,
; E = 0, A = 0; spr3f: D = $7C, E = the last source byte, A = 0; spr4f: D = $7C, E = the last
; source byte, A = its mirrored value. Interrupts off, then on, as the game's DI ... EI. The tile
; bytes are built in s3_buf, up to 64 tiles at a time, and written with one jt_vwrite call.
; Runs on a stack of its own in the page.
spr3:   ld (s3_n),a
        sbc a,a                 ; carry -> A, carry kept
        ld (s3_cy),a
        xor a                   ; mode: bit 0 mirrored, bit 1 four planes
        jr sp_go
spr3f:  ld (s3_n),a
        sbc a,a
        ld (s3_cy),a
        ld a,1
        jr sp_go
spr4f:  ld (s3_n),a
        sbc a,a
        ld (s3_cy),a
        ld a,3
sp_go:  di
        ld (s3_sp),sp           ; a stack of its own while interrupts are off
        ld sp,s3_stk
        ld (s3_m),a
        ld (s3_ix),ix
        ld (s3_iy),iy
        ld a,d
        or $40
        ld (s3_d),a
        and $3F
        ld d,a
.chunk: ld a,(s3_n)             ; tiles left (0 means 256)
        dec a
        cp 64
        jr c,.last
        ld a,63
.last:  inc a                   ; tiles in this chunk, 1-64
        ld (s3_k),a
        ld ix,s3_buf
        ld c,a
.tile:  ld b,8
.row:   call sp_byte
        ld (ix+0),a
        call sp_byte
        ld (ix+1),a
        call sp_byte
        ld (ix+2),a
        ld a,(s3_m)
        bit 1,a
        ld a,0
        jr z,.p3
        call sp_byte
.p3:    ld (ix+3),a
        inc ix
        inc ix
        inc ix
        inc ix
        djnz .row
        dec c
        jr nz,.tile
        ld (s3_hl),hl
        ld hl,s3_buf
        ld a,(s3_k)
        ld c,a                  ; runs of 32 bytes, one a tile
        ld b,32
        ld ix,32
        ld iy,32
        ld a,1                  ; the source is this page
        call jt_vwrite
        ld a,(s3_k)             ; DE += 32 a tile
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,de
        ex de,hl
        ld hl,(s3_hl)
        ld a,(s3_k)
        ld b,a
        ld a,(s3_n)
        sub b
        ld (s3_n),a
        jp nz,.chunk
        ld ix,(s3_ix)
        ld iy,(s3_iy)
        ld bc,$00BE
        ld hl,(s3_hl)
        ld a,(s3_m)
        or a
        jr nz,.mir
        ld a,(s3_d)
        ld d,a
        ld e,0
        xor a
        jr .fl
.mir:   ld de,(s3_last)         ; E = the last source byte, D = $7C
        bit 1,a
        ld a,0
        jr z,.fl
        ld a,(s3_lastr)
.fl:    ld (s3_ra),a
        ld a,(s3_cy)
        rla                     ; carry back
        ld a,1
        dec a                   ; Z and N set, carry kept
        ld a,(s3_ra)
        ld sp,(s3_sp)           ; LD keeps the flags
        ei
        ret
; A = the next source byte, mirrored in the mirrored modes; HL steps on. Keeps BC, DE, IX.
sp_byte: ld a,h
        cp $40
        jr nc,.ram
        call jt_peek
        jr .got
.ram:   ld a,(hl)
.got:   inc hl
        push de
        ld e,a
        ld d,$7C
        ld (s3_last),de
        ld a,(s3_m)
        rra
        ld a,e
        jr nc,.done
        ld a,(de)               ; the game's bit-reverse table (bank 1 in slot 1)
        ld (s3_lastr),a
.done:  pop de
        ret
;
;
;
; ntfill: as the game's $055E-$0588. Writes 896 name table entries ($00, $08) from VRAM $3800.
; Returns as the game's loop does: HL = 0, A = 0 with Z set, B = 0, C = $BE, D = $08, E = 0, VDP
; address $3F00, latch clear; interrupts off, then on, as the game's DI ... EI, after the loop's
; Master System time.
ntfill: di
        ld (nt_sp),sp           ; a stack of its own while interrupts are off
        ld sp,nt_stk
        ld (nt_ix),ix
        ld (nt_iy),iy
        xor a                   ; the line at the start, for the Master System's time
        ld (dirq),a
        call dline
        ld (nt_l0),hl
        ld a,29                 ; the VRAM copy's page of $2000-$3FFF (SHADOW_PAGE + 1) at MMU4
        nextreg $54,a
        ld hl,$8000+$1800       ; name table entries in the copy
        ld ix,nt_runs           ; runs of differing entries: first entry, count
        ld bc,896               ; entries left
        ld e,0                  ; runs found
        ld d,0                  ; 1 while in a run
.scan:  ld a,(hl)
        or a
        jr nz,.diff
        inc hl
        ld a,(hl)
        dec hl
        cp $08
        jr nz,.diff
        ld d,0                  ; equal: a run ends
        jr .next
.diff:  ld a,d
        or a
        jr nz,.more
        ld a,e                  ; a new run
        cp 64
        jp nc,.all              ; too many runs: write the whole table
        inc e
        ld d,1
        push hl
        ld a,l                  ; entry number = (HL - $9800) / 2
        sub $00
        ld l,a
        ld a,h
        sub $98
        ld h,a
        srl h
        rr l
        ld (ix+0),l
        ld (ix+1),h
        ld (ix+2),0
        ld (ix+3),0
        pop hl
        inc ix
        inc ix
        inc ix
        inc ix
.more:  ld a,(ix-2)             ; count + 1
        add a,1
        ld (ix-2),a
        jr nc,.next
        inc (ix-1)
.next:  inc hl
        inc hl
        dec bc
        ld a,b
        or c
        jr nz,.scan
        call nt_mmu
        ld a,e
        or a
        jr z,.state
        ld ix,nt_runs
.run:   push de                 ; write one run: entries (IX+0..1), count (IX+2..3)
        ld l,(ix+0)
        ld h,(ix+1)
        add hl,hl
        ld de,$3800
        add hl,de
        ex de,hl                ; DE = VRAM address
        ld l,(ix+2)
        ld h,(ix+3)
        add hl,hl               ; bytes
.part:  ld a,h
        or a
        jr nz,.big
        ld a,l
        or a
        jr z,.done
        ld b,l                  ; under 256 bytes
        ld hl,0
        jr .w
.big:   dec h                   ; 256 bytes
        ld b,0
.w:     push hl
        push ix
        push iy
        ld hl,nt_pat
        ld c,1
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        ld a,b                  ; DE += bytes written (0 means 256)
        or a
        jr nz,.w2
        inc d
        jr .w3
.w2:    add a,e
        ld e,a
        jr nc,.w3
        inc d
.w3:    pop hl
        jr .part
.done:  pop de
        inc ix
        inc ix
        inc ix
        inc ix
        dec e
        jr nz,.run
.state: ld bc,$243B             ; wait for the loop's time on a PAL Master System: 69,900 T,
        ld a,$05                ; 307 lines at 50 Hz, 313 at 60 Hz, with interrupts off
        out (c),a
        inc b
        in a,(c)
        ld hl,311
        ld de,307
        bit 2,a
        jr z,.hz
        ld hl,264
        ld de,313
.hz:    ld (dlen),hl
.wt:    call dline              ; HL = lines since the start
        ld bc,(nt_l0)
        or a
        sbc hl,bc
        jr nc,.pos
        ld bc,(dlen)
        add hl,bc
.pos:   or a
        sbc hl,de
        jr c,.wt
        ld hl,$3F00             ; VDP state as the game's loop leaves it
        ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld a,$08
        ld (vdp_rbuf),a
        ld ix,(nt_ix)
        ld iy,(nt_iy)
        ld hl,0
        ld bc,$00BE
        ld de,$0800
        xor a
        ld sp,(nt_sp)
        ei
        ret
.all:   call nt_mmu
        ld hl,nt_pat
        ld de,$3800
        ld bc,$0007             ; 7 runs of 256 bytes
        ld ix,0
        ld iy,256
        ld a,1
        call jt_vwrite
        jr .state
; MMU4 back to the game's page.
nt_mmu: ld a,(cur_mmu+4)
        nextreg $54,a
        ret
nt_ix:  dw 0
nt_iy:  dw 0
nt_sp:  dw 0
nt_l0:  dw 0
        ds 32
nt_stk:
nt_runs: ds 4*64
nt_pat:                         ; 128 entries of tile 0, sprite palette
        dup 128
        db $00,$08
        edup
;
; tload: as the game's $067B-$0694. In: B = tiles (0 means 256), HL = the source, DE = the VRAM
; address (bit 6 of D may be clear). Returns as the game's code does: HL past the source, B = 0,
; C = $BE, D with bit 6 set, E kept, A kept, Z clear; VDP address after the last byte, latch
; clear. Interrupts off, then on, as the game's DI ... EI, after the loop's Master System time.
; Runs on a stack of its own.
tload:  di
        ld (tl_sp),sp
        ld sp,tl_stk
        ld (tl_a),a
        ld (tl_ix),ix
        ld (tl_iy),iy
        ld a,e
        ld (tl_e),a
        ld a,d
        or $40
        ld (tl_d),a
        and $3F
        ld d,a
        ld a,b
        ld (tl_n),a
        ld (tl_t),a
        xor a
        ld (dirq),a
        push hl
        push de
        call dline
        ld (tl_l0),hl
        pop de
        pop hl
.lp:    ld a,(tl_n)             ; tiles left (0 means 256)
        dec a
        cp 8
        jr c,.k
        ld a,7
.k:     inc a                   ; tiles in this call, 1-8
        ld (tl_k),a
        add a,a
        add a,a
        add a,a
        add a,a
        add a,a                 ; bytes (0 means 256)
        ld c,a
        ld b,1                  ; runs of one byte
        ld ix,1
        ld iy,1
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,(tl_k)             ; HL, DE += 32 a tile
        push de
        ld e,a
        ld d,32
        mul d,e                 ; DE = bytes
        add hl,de               ; the source
        ex de,hl
        ex (sp),hl              ; HL = the VRAM address, (SP) = bytes
        pop bc
        add hl,bc
        ex de,hl
        ld a,(tl_k)
        ld b,a
        ld a,(tl_n)
        sub b
        ld (tl_n),a
        jr nz,.lp
        push hl
        ld bc,$243B             ; the loop's time: 4.75 lines a tile at 50 Hz, 4.875 at 60 Hz
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        and 4
        ld (tl_hz),a
        ld a,(tl_t)
        ld l,a
        ld h,0
        or a
        jr nz,.t
        inc h                   ; 256 tiles
.t:     ld d,h
        ld e,l
        add hl,hl
        add hl,hl               ; 4 n
        push hl
        ld h,d
        ld l,e
        add hl,hl
        add hl,de               ; 3 n
        ld a,(tl_hz)
        or a
        jr z,.q
        add hl,hl               ; 6 n
        add hl,de               ; 7 n
        srl h
        rr l                    ; 7 n / 2
        srl h
        rr l
        srl h
        rr l                    ; 7 n / 8
        jr .s
.q:     srl h
        rr l
        srl h
        rr l                    ; 3 n / 4
.s:     pop de
        add hl,de               ; lines to wait
        ld (tl_w),hl
        ld hl,311
        ld a,(tl_hz)
        or a
        jr z,.f
        ld hl,264
.f:     ld (dlen),hl
.wt:    call dline              ; lines since the start
        ld bc,(tl_l0)
        or a
        sbc hl,bc
        jr nc,.pos
        ld bc,(dlen)
        add hl,bc
.pos:   ld de,(tl_w)
        or a
        sbc hl,de
        jr c,.wt
        pop hl
        ld ix,(tl_ix)
        ld iy,(tl_iy)
        ld a,(tl_d)
        ld d,a
        ld a,(tl_e)
        ld e,a
        ld b,2
        dec b                   ; Z clear, as after the game's last OUTI
        ld b,0
        ld c,$BE
        ld a,(tl_a)
        ld sp,(tl_sp)
        ei
        ret
tl_n:   db 0
tl_t:   db 0
tl_k:   db 0
tl_a:   db 0
tl_d:   db 0
tl_e:   db 0
tl_hz:  db 0
tl_w:   dw 0
tl_l0:  dw 0
tl_ix:  dw 0
tl_iy:  dw 0
tl_sp:  dw 0
        ds 32
tl_stk:
; lv_line: in place of the game's $04B0-$04B3 (IN A,($7E) : ADD A,$10) in the line path. Returns,
; with the flags of the ADD, the V counter the Master System gives the k-th line event of a
; picture, 16k - 1, plus $10; lvirq counts k in ($DE02).
lv_line: ld a,($DE02)
        add a,a
        add a,a
        add a,a
        add a,a
        dec a                   ; 16k - 1
        add a,$10
        ret
s3_n:   db 0
s3_k:   db 0
s3_m:   db 0
s3_cy:  db 0
s3_d:   db 0
s3_hl:  dw 0
s3_ix:  dw 0
s3_iy:  dw 0
s3_last: dw 0
s3_lastr: db 0
s3_ra:  db 0
s3_sp:  dw 0
        ds 64
s3_stk:
s3_buf: ds 2048
endpage
site 00253   ; OTIR
site 00266   ; OUT ($3E),A
site 0026A   ; OUT ($3F),A
site 002A6   ; OUT ($BF),A
site 002AE   ; OUT ($BF),A
site 002B9   ; OUT ($BF),A
site 002C1   ; OUT ($BF),A
site 002CF   ; OUT (C),E
site 002D5   ; OUT (C),D
site 002DC   ; OUT (C),A
site 0030E   ; OUT ($BF),A
site 00316   ; OUT ($BF),A
site 00320   ; OUT ($BF),A
site 00328   ; OUT ($BF),A
site 00332   ; OUT ($BF),A
site 0033A   ; OUT ($BF),A
site 00344   ; OUT ($BF),A
site 0034C   ; OUT ($BF),A
site 00356   ; OUT ($BF),A
site 0035E   ; OUT ($BF),A
site 00368   ; OUT ($BF),A
site 00370   ; OUT ($BF),A
site 0037A   ; OUT ($BF),A
site 00382   ; OUT ($BF),A
site 0038C   ; OUT ($BF),A
site 00394   ; OUT ($BF),A
site 0039E   ; OUT ($BF),A
site 003A6   ; OUT ($BF),A
site 003B0   ; OUT ($BF),A
site 003B8   ; OUT ($BF),A
site 003C2   ; OUT ($BF),A
site 003CA   ; OUT ($BF),A
site 003DA   ; OUT ($BF),A
site 003E1   ; OUT ($BF),A
site 003E8   ; OUT ($BE),A
site 003EB   ; OUT ($BF),A
site 003F2   ; OUT ($BF),A
site 003FB   ; OUT ($BE),A
site 0041B   ; OUT ($BF),A
site 00422   ; OUT ($BF),A
site 0042E   ; OUT (C),A
site 0043A   ; OUT ($BF),A
site 00441   ; OUT ($BF),A
site 0044F   ; OUT (C),A
site 00455   ; OUT (C),A
site 0046A   ; IN A,($BF)
site 00478   ; IN A,($DD)
site 004FD   ; OUT (C),A
site 00507   ; OUT (C),B
site 0051F   ; OUT (C),L
site 00525   ; OUT (C),H
site 0052C   ; OUT (C),A
site 00536   ; OUT ($BF),A
site 0053E   ; OUT ($BF),A
site 00548   ; OUT ($BF),A
site 00550   ; OUT ($BF),A
site 005A1   ; IN A,($DC)
site 005A9   ; IN A,($DC)
site 005B1   ; IN A,($DC)
site 005B9   ; IN A,($DC)
site 005C1   ; IN A,($DC)
site 005C9   ; IN A,($DC)
site 00699   ; OUT (C),E
site 006A0   ; OUT (C),D
site 006A9   ; OUT (C),A
site 00702   ; OUT (C),A
site 0070A   ; OUT (C),B
site 00713   ; OUT (C),A
site 0071B   ; OUT (C),B
site 008D2   ; OUT ($BF),A
site 008DA   ; OUT ($BF),A
site 008E0   ; OUT ($BE),A
site 008E5   ; OUT ($BE),A
site 00953   ; OUT (C),A
site 00958   ; OUT (C),A
site 00964   ; OUT (C),L
site 0096B   ; OUT (C),A
site 00971   ; OUT (C),A
site 00976   ; OUT (C),A
site 00B00   ; OUT ($BF),A
site 00B08   ; OUT ($BF),A
site 00B37   ; OUT (C),E
site 00B3D   ; OUT (C),D
site 00B42   ; OUTI
# The mirrored 3-plane loop $0C5A-$0D0F no longer runs (spr3f); its sites stay patched, because
# the scan reaches the loop through a data word ($0D00, stored at $6D0E) taken as a code address.
site 00C5E   ; OUT ($BE),A
site 00C63   ; OUT ($BE),A
site 00C68   ; OUT ($BE),A
site 00C6F   ; OUT ($BE),A
site 00C74   ; OUT ($BE),A
site 00C79   ; OUT ($BE),A
site 00C7E   ; OUT ($BE),A
site 00C85   ; OUT ($BE),A
site 00C8A   ; OUT ($BE),A
site 00C8F   ; OUT ($BE),A
site 00C94   ; OUT ($BE),A
site 00C9B   ; OUT ($BE),A
site 00CA0   ; OUT ($BE),A
site 00CA5   ; OUT ($BE),A
site 00CAA   ; OUT ($BE),A
site 00CB1   ; OUT ($BE),A
site 00CB6   ; OUT ($BE),A
site 00CBB   ; OUT ($BE),A
site 00CC0   ; OUT ($BE),A
site 00CC7   ; OUT ($BE),A
site 00CCC   ; OUT ($BE),A
site 00CD1   ; OUT ($BE),A
site 00CD6   ; OUT ($BE),A
site 00CDD   ; OUT ($BE),A
site 00CE2   ; OUT ($BE),A
site 00CE7   ; OUT ($BE),A
site 00CEC   ; OUT ($BE),A
site 00CF3   ; OUT ($BE),A
site 00CF8   ; OUT ($BE),A
site 00CFD   ; OUT ($BE),A
site 00D02   ; OUT ($BE),A
site 00D09   ; OUT ($BE),A
site 00F9B   ; OUT ($BF),A
site 00FA3   ; OUT ($BF),A
site 00FB0   ; OUT (C),A
site 00FB9   ; OUT (C),A
site 00FCF   ; OUT ($BF),A
site 00FD7   ; OUT ($BF),A
site 00FE7   ; OUT (C),A
site 00FEE   ; OUT (C),A
site 01024   ; IN A,($DC)
site 0102B   ; IN A,($DC)
site 01032   ; IN A,($DC)
site 01168   ; IN A,($7E)
site 014AC   ; OUT (C),L
site 014B3   ; OUT (C),H
site 01500   ; OUT (C),E
site 01596   ; OUT ($BF),A
site 0159F   ; OUT ($BF),A
site 015CE   ; OUT ($BF),A
site 015D7   ; OUT ($BF),A
site 015F1   ; OUT ($BE),A
site 01772   ; OUT ($BF),A
site 0177A   ; OUT ($BF),A
site 01780   ; OUT ($BE),A
site 01785   ; OUT ($BE),A
site 01797   ; OUT ($BF),A
site 0179F   ; OUT ($BF),A
site 017A5   ; OUT ($BE),A
site 017AA   ; OUT ($BE),A
site 01821   ; OUT ($BF),A
site 0182A   ; OUT ($BF),A
site 01834   ; OUT ($BE),A
site 0184D   ; OUT ($BF),A
site 01857   ; OUT ($BF),A
site 01860   ; OUT ($BE),A
site 01936   ; OUT (C),L
site 0193C   ; OUT (C),H
site 01943   ; IN A,(C)
site 01948   ; IN A,(C)
site 01957   ; OUT (C),L
site 0195D   ; OUT (C),H
site 01996   ; OUT (C),L
site 0199C   ; OUT (C),H
site 019A7   ; OUT (C),A
site 019AC   ; OUT (C),A
site 019B9   ; OUT (C),L
site 019BF   ; OUT (C),H
site 019FA   ; OUT (C),L
site 01A00   ; OUT (C),H
site 01A0B   ; OUT (C),A
site 01A11   ; OUT (C),A
site 01A1F   ; OUT (C),L
site 01A25   ; OUT (C),H
site 03554   ; IN A,($7E)
site 0355D   ; IN A,($7E)
site 03627   ; OUT ($BF),A
site 0362F   ; OUT ($BF),A
site 03639   ; OUT ($BF),A
site 03641   ; OUT ($BF),A
site 0364B   ; OUT ($BF),A
site 03653   ; OUT ($BF),A
site 036A3   ; OUT ($BF),A
site 036AB   ; OUT ($BF),A
site 036B5   ; OUT ($BF),A
site 036BD   ; OUT ($BF),A
site 03CD5   ; IN A,($DC)
site 03CE5   ; IN A,($DC)
site 03CEF   ; IN A,($DC)
site 03CFF   ; IN A,($DC)
site 03D09   ; IN A,($DC)
site 03D19   ; IN A,($DC)
site 03D23   ; IN A,($DC)
site 03D33   ; IN A,($DC)
site 03DA2   ; OUT ($BF),A
site 03DAA   ; OUT ($BF),A
site 03DB4   ; OUT ($BF),A
site 03DBC   ; OUT ($BF),A
site 03DCA   ; OUT (C),L
site 03DD0   ; OUT (C),H
site 03DDB   ; OUT (C),E
site 03DE1   ; OUT (C),D
site 04054   ; OUT (C),E
site 0405A   ; OUT (C),D
site 04067   ; OUT (C),E
site 0406D   ; OUT (C),D
site 042F2   ; IN A,($DC)
site 043A0   ; OUT ($BF),A
site 043A8   ; OUT ($BF),A
site 0470C   ; OUT ($BF),A
site 04714   ; OUT ($BF),A
site 05D68   ; OUT ($BF),A
site 05D70   ; OUT ($BF),A
site 05EA7   ; OUT (C),L
site 05EAD   ; OUT (C),H
site 05EB4   ; OUT (C),E
site 05EBA   ; OUT (C),D
site 0724C   ; OUT ($BF),A
site 07251   ; OUT ($BF),A
site 072C0   ; OUT ($BE),A
site 072E0   ; OUT ($BE),A
site 19F2F   ; OUT ($7F),A
site 19F33   ; OUT ($7F),A
site 19F40   ; OUT ($7F),A
site 19F44   ; OUT ($7F),A
site 19F75   ; OUT ($7F),A
site 19F8C   ; OUT ($7F),A
site 19F99   ; OUT ($7F),A
site 19FA8   ; OUT ($7F),A
site 19FBF   ; OUT ($7F),A
site 19FCC   ; OUT ($7F),A
site 19FF2   ; OUT ($7F),A
site 1A005   ; OUT ($7F),A
site 1A01C   ; OUT ($7F),A
site 1A022   ; OUT ($7F),A
site 1A046   ; OUT ($7F),A
site 1A05D   ; OUT ($7F),A
site 1A06A   ; OUT ($7F),A
site 1A0C7   ; OUT ($7F),A
site 1A230   ; OUT ($7F),A
site 1A235   ; OUT ($7F),A
site 1A249   ; OUT ($7F),A
site 1A25C   ; OUT ($7F),A
site 1A268   ; OUT ($7F),A
site 1A27B   ; OUT ($7F),A
mapst 0026D   ; LD ($FFFC),A
mapst 00270   ; LD ($FFFD),A
mapst 00275   ; LD ($FFFE),A
mapst 0027A   ; LD ($FFFF),A
mapst 00496   ; LD ($FFFF),A
mapst 0049D   ; LD ($FFFF),A
mapst 005F5   ; LD ($FFFF),A
mapst 006D5   ; LD ($FFFF),A
mapst 006DF   ; LD ($FFFF),A
mapst 00980   ; LD ($FFFF),A
mapst 00B17   ; LD ($FFFF),A
mapst 00B21   ; LD ($FFFF),A
mapst 00B7B   ; LD ($FFFF),A
mapst 00B85   ; LD ($FFFF),A
mapst 010DE   ; LD ($FFFF),A
mapst 0111E   ; LD ($FFFF),A
mapst 01128   ; LD ($FFFF),A
mapst 01391   ; LD ($FFFF),A
mapst 0150C   ; LD ($FFFF),A
mapst 01524   ; LD ($FFFF),A
mapst 01566   ; LD ($FFFF),A
mapst 015A7   ; LD ($FFFF),A
mapst 015BC   ; LD ($FFFF),A
mapst 015DF   ; LD ($FFFF),A
mapst 015EB   ; LD ($FFFF),A
mapst 01745   ; LD ($FFFF),A
mapst 017F1   ; LD ($FFFF),A
mapst 01C96   ; LD ($FFFF),A
mapst 01CB3   ; LD ($FFFF),A
mapst 0359C   ; LD ($FFFF),A
mapst 037D4   ; LD ($FFFF),A
mapst 03885   ; LD ($FFFF),A
mapst 038A3   ; LD ($FFFF),A
mapst 038B3   ; LD ($FFFF),A
mapst 03B5A   ; LD ($FFFF),A
mapst 03BCC   ; LD ($FFFF),A
mapst 03BE2   ; LD ($FFFF),A
mapst 03C72   ; LD ($FFFF),A
mapst 03D3C   ; LD ($FFFF),A
mapst 03E2C   ; LD ($FFFF),A
mapst 03E71   ; LD ($FFFF),A
mapst 03EF7   ; LD ($FFFF),A
mapst 03F5E   ; LD ($FFFF),A
mapst 04042   ; LD ($FFFF),A
mapst 040B0   ; LD ($FFFF),A
mapst 0411C   ; LD ($FFFF),A
mapst 04130   ; LD ($FFFF),A
mapst 0414E   ; LD ($FFFF),A
mapst 04263   ; LD ($FFFF),A
mapst 04352   ; LD ($FFFF),A
mapst 04403   ; LD ($FFFF),A
mapst 045D5   ; LD ($FFFF),A
mapst 0468C   ; LD ($FFFF),A
mapst 046B4   ; LD ($FFFF),A
mapst 05666   ; LD ($FFFF),A
mapst 0566A   ; LD ($FFFF),A
mapst 0580A   ; LD ($FFFF),A
mapst 05B3B   ; LD ($FFFF),A
mapst 05BA6   ; LD ($FFFF),A
mapst 05BE1   ; LD ($FFFF),A
mapst 05BF7   ; LD ($FFFF),A
mapst 05C8B   ; LD ($FFFF),A
mapst 05CB5   ; LD ($FFFF),A
mapst 05CED   ; LD ($FFFF),A
mapst 05D33   ; LD ($FFFF),A
mapst 06AF3   ; LD ($FFFF),A
mapst 06B31   ; LD ($FFFF),A
mapst 06BC9   ; LD ($FFFF),A
mapst 06BFE   ; LD ($FFFF),A
mapst 06CA8   ; LD ($FFFF),A
mapst 06CB0   ; LD ($FFFF),A
mapst 06E4E   ; LD ($FFFF),A
mapst 06E66   ; LD ($FFFF),A
mapst 06E9F   ; LD ($FFFF),A
mapst 06EAB   ; LD ($FFFF),A
mapst 06EBB   ; LD ($FFFF),A
mapst 06EC7   ; LD ($FFFF),A
mapst 06ECD   ; LD ($FFFF),A
# CHECK cartarea_store at 002D2 ($02D2 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 003DC ($03DC bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 003E5 ($03E5 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 003ED ($03ED bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 003F7 ($03F7 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00522 ($0522 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00568 ($0568 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00579 ($0579 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0057E ($057E bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00704 ($0704 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00707 ($0707 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0070C ($070C bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00715 ($0715 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00718 ($0718 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00B02 ($0B02 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00B5F ($0B5F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00B65 ($0B65 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00B6B ($0B6B bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00F9F ($0F9F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00FA7 ($0FA7 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00FB6 ($0FB6 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00FD3 ($0FD3 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00FDB ($0FDB bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 014B0 ($14B0 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0184F ($184F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01852 ($1852 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01859 ($1859 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0185C ($185C bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01862 ($1862 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01865 ($1865 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01939 ($1939 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0195A ($195A bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0195F ($195F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01999 ($1999 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0199E ($199E bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 019BC ($19BC bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 019C1 ($19C1 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 019FD ($19FD bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01A02 ($1A02 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01A22 ($1A22 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01A27 ($1A27 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03DCD ($3DCD bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03DDE ($3DDE bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03DE3 ($3DE3 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04057 ($4057 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0405D ($405D bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0406A ($406A bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05EAA ($5EAA bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05EB0 ($5EB0 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05EB7 ($5EB7 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK indirect_unresolved at 01A9E ($1A9E bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 06943 ($6943 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 06B89 ($6B89 bank 1): DD E9  JP (IX) 
# CHECK indirect_unresolved at 06B89 ($6B89 bank 1): DD E9  JP (IX) 
# CHECK indirect_unresolved at 075B1 ($75B1 bank 1): C9  RET 
# CHECK indirect_unresolved at 07F03 ($7F03 bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F04 ($7F04 bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F0D ($7F0D bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F0E ($7F0E bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F12 ($7F12 bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F13 ($7F13 bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F17 ($7F17 bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F18 ($7F18 bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F1C ($7F1C bank 1): F8  RET M 
# CHECK indirect_unresolved at 07F1D ($7F1D bank 1): F8  RET M 
# CHECK bank_unresolved at 07F08 ($7F08 bank 1): F4 F8 90  CALL P,$90F8 $90F8
# Mapper stores found by the byte scan in bytes no path reached:
mapst 013F0   # LD ($FFFF),A; after LD A,($C653); 32 bytes of valid code before it
# CHECK byte scan low: mapst 4F659  LD ($FFFE),A  (7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0058C  OUT ($BF),A  (vdp_control; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 00593  OUT ($BF),A  (vdp_control; after LD A,$87; 32 bytes of valid code before it)
# CHECK high: site 00B0C  OUT ($BF),A  (vdp_control; branch target from $21524 $25C9C $4B16E $70DAB; 32 bytes of valid code before it)
# CHECK high: site 00B12  OUT ($BF),A  (vdp_control; branch target from $12AE5 $60C5D $0AE37 $3D634; 31 bytes of valid code before it)
# CHECK high: site 01006  OUT (C),E  (port in C; branch target from $29190 $35E03; 32 bytes of valid code before it)
# CHECK high: site 0100D  OUT (C),D  (port in C; branch target from $601AB; 32 bytes of valid code before it)
# CHECK high: site 01012  OUT (C),A  (port in C; branch target from $0101F; 32 bytes of valid code before it)
# CHECK high: site 01019  OUT (C),A  (port in C; branch target from $750C5; 32 bytes of valid code before it)
# CHECK medium: site 0901C  OUT (C),B  (port in C; 32 bytes of valid code before it)
# CHECK low: site 09078  OUT ($C0),A  (no_effect; no evidence)
# CHECK medium: site 0A41E  OUT ($3F),A  (io_control; 28 bytes of valid code before it)
# CHECK medium: site 0A487  IN A,($DC)  (joypad_a; 18 bytes of valid code before it)
# CHECK low: site 0DA46  IN A,($F0)  (joypad_a; no valid code after it)
# CHECK medium: site 1A1BC  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK medium: site 1A1BE  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK medium: site 1D099  IN A,($BF)  (vdp_status; 12 bytes of valid code before it)
# CHECK low: site 1D09D  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 2018F  IN A,($3F)  (unmapped_read; no evidence)
# CHECK medium: site 28BD3  OUT ($BD),A  (vdp_control; 32 bytes of valid code before it)
# CHECK low: site 2EA41  OUT ($C0),A  (no_effect; no evidence)
# CHECK low: site 31DC3  OUT ($3E),A  (memory_control; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 31F9B  IN A,($BE)  (vdp_data; no evidence)
# CHECK low: site 3314D  OUT ($3F),A  (io_control; no evidence)
# CHECK low: site 3423D  IN C,(C)  (port in C; no evidence)
# CHECK medium: site 346F0  IN B,(C)  (port in C; 32 bytes of valid code before it)
# CHECK low: site 35218  IN A,($F0)  (joypad_a; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3C8E8  IN D,(C)  (port in C; no evidence)
# CHECK medium: site 3CFE0  INI  (port in C; 26 bytes of valid code before it)
# CHECK low: site 3D512  IN A,($7F)  (h_counter; no valid code after it)
# CHECK medium: site 3D726  IN A,($7E)  (v_counter; 29 bytes of valid code before it)
# CHECK low: site 3E65C  IN A,($7E)  (v_counter; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 434D9  OUT ($3F),A  (io_control; 16 bytes of valid code before it)
# CHECK medium: site 4590A  OUT ($3F),A  (io_control; 32 bytes of valid code before it)
# CHECK low: site 45A7D  OUT ($7F),A  (psg; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 45CDC  IN A,($BF)  (vdp_status; no evidence)
# CHECK low: site 45D35  OUT ($3F),A  (io_control; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 49E77  OUT ($7F),A  (psg; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 4A189  IN A,($7F)  (h_counter; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 4EC25  IN A,($C0)  (joypad_a; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 4ED5E  OUT ($BD),A  (vdp_control; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 4F029  IN B,(C)  (port in C; 13 bytes of valid code before it)
# CHECK medium: site 4F277  OUT ($DC),A  (no_effect; 28 bytes of valid code before it)
# CHECK medium: site 4F4C1  IN A,($3F)  (unmapped_read; 24 bytes of valid code before it)
# CHECK medium: site 4FCFE  OUT ($C1),A  (no_effect; 32 bytes of valid code before it)
# CHECK low: site 51219  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 51241  IN A,($DC)  (joypad_a; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 512AD  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 512B2  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 512B7  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 512BC  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 512C1  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 5262F  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 52647  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 5265F  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 52664  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 52669  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 5266E  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 526AF  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 5AECC  OUT (C),E  (port in C; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5CEA7  IN A,($7F)  (h_counter; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5D8A6  OUTD  (port in C; no evidence)
# CHECK medium: site 5E120  IN A,($3F)  (unmapped_read; 15 bytes of valid code before it)
# CHECK low: site 5E1B7  IN B,(C)  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 5E685  OUT ($F1),A  (fm_data; no evidence)
# CHECK low: site 6199F  OUT ($F2),A  (fm_control; no evidence)
# CHECK low: site 61C45  OUT ($F2),A  (fm_control; no evidence)
# CHECK low: site 646F7  IN A,($F0)  (joypad_a; no evidence)
# CHECK medium: site 66994  IN A,($BF)  (vdp_status; branch target from $669B2)
# CHECK medium: site 6864C  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK medium: site 68E26  OUT ($3F),A  (io_control; 9 bytes of valid code before it)
# CHECK low: site 69180  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 6CDFD  IN A,($F0)  (joypad_a; no evidence)
# CHECK medium: site 6D348  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK medium: site 7B112  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK low: site 7E2CC  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 7E956  IN A,($F0)  (joypad_a; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 7EE76  IN A,($C1)  (joypad_b_misc; 18 bytes of valid code before it)
# CHECK medium: site 7F400  OUT ($7E),A  (psg; 32 bytes of valid code before it)
