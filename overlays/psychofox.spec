# Psycho Fox (USA, Europe, Brazil) (En), CRC32 97993479, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the reference I/O log
# (reflogs/sweep/97993479, 60 s).
name Psycho Fox
cart 97993479
hz any		; No-Intro regions USA, Europe, Brazil
# No free RST vector: $0000-$0002 (IM 1; DI) becomes the vector,
# the game starts at $0003 (LD SP,$D800; the runtime does DI and IM 2).
vector 00 io
start 0003
# The wave effect (bank 11 $8000) sets H every 2 lines from line interrupts;
# psychofox-raster.asm gives the per-line table, page 0 `wave` replaces the loop.
rastercode psychofox-raster.asm
# HALTs: the main loop's frame wait ($00B7), state 2's frame wait ($01AF) and the
# line 96 split of bank 11 ($A646). The wave effect's and the pause screen band's
# HALT loops are replaced by page 0 entries below.
eihalt 001AF   ; EI : HALT
eihalt 2E646   ; EI : HALT
site 00009   ; OUT ($BF),A
site 0000E   ; OUT ($BF),A
site 00021   ; OUT ($BF),A
site 00028   ; OUT ($BF),A
site 00031   ; OUT ($BF),A
site 00034   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 00212   ; OTIR
site 005FD   ; OUT ($BE),A
site 0071A   ; OUT ($BE),A
site 00729   ; OUT ($BE),A
site 03F2D   ; OUT ($BF),A
site 03F30   ; OUT ($BF),A
site 03F34   ; OUT ($BE),A
site 03F38   ; OUT ($BE),A
site 03F3C   ; OUT ($BF),A
site 03F3F   ; OUT ($BF),A
site 03F43   ; OUT ($BE),A
site 03F47   ; OUT ($BE),A
site 03F60   ; OUT ($BF),A
site 03F65   ; OUT ($BF),A
site 03F68   ; OUT ($BE),A
site 041B6   ; OUT ($BF),A
site 041BA   ; OUT ($BF),A
site 041C2   ; OUT ($BE),A
site 041C6   ; OUT ($BE),A
site 041CE   ; OUT ($BE),A
site 04555   ; OUT ($BE),A
site 04562   ; OUT ($BE),A
site 0459B   ; OUT ($BF),A
site 045A0   ; OUT ($BF),A
site 045A5   ; OUT ($BE),A
site 045AC   ; OUT ($BE),A
site 045B3   ; OUT ($BE),A
site 04C42   ; OTIR
site 04EF7   ; OUT (C),A
site 04F03   ; OUT (C),A
site 04F1D   ; OUT ($BF),A
site 04F21   ; OUT ($BF),A
site 04F29   ; OUT ($BE),A
site 04F2C   ; OUT ($BE),A
site 04F35   ; OUT ($BF),A
site 04F39   ; OUT ($BF),A
site 04F45   ; OUT ($BF),A
site 04F49   ; OUT ($BF),A
site 04F5B   ; OUT ($BE),A
site 04F5F   ; OUT ($BE),A
site 04F94   ; OUT ($BF),A
site 04F99   ; OUT ($BF),A
site 04F9C   ; OUT ($BE),A
site 04F9F   ; OUT ($BE),A
site 04FA2   ; OUT ($BE),A
site 04FA5   ; OUT ($BE),A
site 04FBA   ; OUT ($BE),A
site 07C1C   ; OTIR
site 07C24   ; OTIR
site 07E52   ; IN A,($DD)
site 07E5F   ; OUT ($3F),A
site 07E61   ; IN A,($DD)
site 07E6B   ; OUT ($3F),A
site 07E6D   ; IN A,($DD)
site 07E75   ; OUT ($3F),A
site 07E7B   ; OUT ($BF),A
site 07E7F   ; OUT ($BF),A
site 07E87   ; OTIR
site 07E8B   ; OUT ($BF),A
site 07E8F   ; OUT ($BF),A
site 07E94   ; OTIR
site 07EA6   ; OUT ($BF),A
site 07EAA   ; OUT ($BF),A
site 07EAD   ; OUT ($BF),A
site 07EB1   ; OUT ($BF),A
site 07EBC   ; OUT ($BF),A
site 07EC0   ; OUT ($BF),A
site 07EC8   ; OUT ($BF),A
site 07ECC   ; OUT ($BF),A
site 07ED7   ; OUT ($BE),A
site 07EDA   ; OUT ($BE),A
site 07EF2   ; OUT ($BE),A
site 07F88   ; IN A,($DC)
site 07F93   ; IN A,($DC)
site 2812D   ; OUT ($F0),A
site 28136   ; OUT ($F1),A
site 2814E   ; OUT ($7F),A
site 2815E   ; OUT (C),D
site 28164   ; OUT ($F1),A
site 28186   ; OUT ($7F),A
site 2818A   ; OUT ($7F),A
site 281B7   ; OTIR
site 281C5   ; OTIR
site 281CF   ; OUT ($F0),A
site 281D5   ; OUT ($F1),A
site 281E1   ; OUTI
site 281E7   ; OUTI
site 28241   ; OUT ($7F),A
site 28245   ; OUT ($7F),A
site 282DD   ; OUT ($7F),A
site 282E1   ; OUT ($7F),A
site 28311   ; OUT ($7F),A
site 28315   ; OUT ($7F),A
site 28319   ; OUT ($7F),A
site 2831C   ; OUT ($7F),A
site 28382   ; OUT ($F0),A
site 28389   ; OUT ($F1),A
site 28391   ; OUT ($F0),A
site 28397   ; OUT ($F1),A
site 28498   ; OUT ($F0),A
site 284A2   ; OUT (C),L
site 284AB   ; OUT ($F0),A
site 284C6   ; OUT (C),H
site 284CE   ; OUT ($F0),A
site 284DC   ; OUT ($F1),A
site 284E8   ; OUT ($F0),A
site 284F1   ; OUT ($F1),A
site 286BD   ; OUT ($F0),A
site 286C6   ; OUT (C),A
site 286CB   ; OUT ($F0),A
site 286D1   ; OUTI
site 28742   ; OUT ($7F),A
site 2880F   ; OUT ($7F),A
site 28836   ; OUT ($7F),A
site 2883B   ; OUT ($7F),A
site 28867   ; OUT ($F0),A
site 28875   ; OUT ($F1),A
site 28883   ; OUT ($F0),A
site 2891A   ; OUTI
site 2891C   ; OUTI
site 2891E   ; OUTI
site 28920   ; OUTI
site 28922   ; OUTI
site 28924   ; OUTI
site 28926   ; OUTI
site 28928   ; OUTI
site 2892A   ; OUTI
site 2892C   ; OUTI
site 2892E   ; OUTI
site 28938   ; OUT (C),D
site 2893E   ; OUT ($F1),A
site 2897D   ; OUT ($7F),A
site 289D3   ; OUT ($7F),A
site 28A12   ; OUT ($7F),A
site 28A74   ; OUT ($7F),A
site 28A94   ; OUT ($7F),A
site 28AE0   ; OUT ($7F),A
site 28AEA   ; OUT ($7F),A
site 28B32   ; OUT ($7F),A
site 2C2D3   ; OTIR
site 2C4EA   ; OUT ($BE),A
site 2C663   ; OUT ($BE),A
site 2C7C0   ; OUT ($BE),A
site 2C7C4   ; OUT ($BE),A
site 2C7DB   ; OUT ($BE),A
site 2C7DF   ; OUT ($BE),A
site 2C9FC   ; OUT ($BE),A
site 2CA00   ; OUT ($BE),A
site 2CA17   ; OUT ($BE),A
site 2CA1B   ; OUT ($BE),A
site 2CB61   ; OTIR
site 2CD6F   ; OUT ($BE),A
site 2CD73   ; OUT ($BE),A
site 2CE27   ; OTIR
site 2D1BE   ; OUT ($BE),A
site 2D536   ; OUT ($BE),A
site 2D53A   ; OUT ($BE),A
site 2DA24   ; OTIR
site 2DFD7   ; OTIR
site 2E197   ; OUT ($BE),A
site 2E1D6   ; OUT ($BE),A
site 2E238   ; OUT ($BE),A
site 2E23F   ; OUT ($BE),A
site 2E629   ; OUT ($BE),A
site 2E675   ; OUT ($BF),A
site 2E679   ; OUT ($BF),A
site 2E720   ; OTIR
site 2E8C0   ; OUT ($BE),A
site 2E8C3   ; OUT ($BE),A
site 2E8DB   ; OTIR
mapst 0004C   ; LD ($FFFF),A
mapsthl 00081   ; LD ($FFFC),HL
mapsthl 00087   ; LD ($FFFE),HL
# The main loop's EI; HALT at $00B7, where every load ends. The load at the
# start of state $0E runs with frame interrupts off; the reference takes the
# interrupt that the VDP's frame flag then holds at this EI ($C011 steps by
# 2 at f608), and the game runs one more frame step. A cave asks page entry
# irqp; when the flag is held it enters the game's handler through RST $38
# with interrupts off, as the CPU takes an interrupt, and goes on after the
# HALT, which that interrupt ends. Else it is the patched EI; HALT. The cave
# also stops the CTC timer (irqp).
label mlc 05E8A
asm 000B7 5   ; EI : HALT : CALL $7E7A
    jp mlc
endasm
asm 05E8A 18  ; $FF filler
    rst $00
    db far_io, pg_irqp, ent_irqp
    jr z,.n
    rst $38
    ei
    jr .c
.n: rst $00
    db eihalt_io
.c: call $7E7A
    jp $00BC
endasm
# Bank 1 $5EB0-$5FE4: a routine (CRAM load, name table writes) that no call,
# jump or pointer in the cart names; patched as it is real code.
eihalt 05EB9   ; EI : HALT
site 05F4E   ; OUT ($BF),A
site 05F52   ; OUT ($BF),A
site 05F57   ; OUT ($BE),A
site 05F5B   ; OUT ($BE),A
site 05F60   ; OUT ($BE),A
site 05F64   ; OUT ($BE),A
site 05FB1   ; OTIR
site 05FC3   ; OUT ($BF),A
site 05FC7   ; OUT ($BF),A
site 05FCE   ; OUT ($BE),A
site 05FD2   ; OUT ($BE),A
# Opening and closing band of the pause screen (bank 11 $8528, called from $8511
# while the screen opens and from $8887 while it closes). The game turns
# the display off, turns line interrupts on (one every 2 lines, register 10 = 1),
# counts them in a HALT loop, turns the display on at count L ($C1DA) and off at
# count H ($C1DB), then turns line interrupts off. On the Master System the band
# shows SMS rows 2L to 2H-1 (reference snapshots, f874-f898 of a pause at
# frame 860). The Next cannot take a line event every 2 lines in time: the band
# flickered and most frames showed no band at all. Page 0 `band` waits on the
# beam's line for the two writes instead, with line interrupts left off.
asm 2C528 7   ; LD BC,$1600 : RST $08 : LD BC,$8001
    rst $00
    db far_io, pg_band, ent_band
    ret
endasm
# The wave effect (bank 11 $8000-$80AA, 256 frames from $C24F): after the
# table rotation the game turns line interrupts on (register 0 = $36, register
# 10 = 1) and writes H after each of 96 of them in a HALT loop ($8085). The
# Next cannot take a line event every 2 lines: each call took about 3 frames
# and the picture broke into misplaced bands. Page 0 `wave` waits for line 191
# instead, and psychofox-raster.asm gives the lines their H.
asm 2C07A 31  ; LD BC,$3600 : RST $08 : LD C,3 ... DEC C : JR NZ,$8080
    rst $00
    db far_io, pg_wave, ent_wave
endasm
# The round build's own code. Traced on the reference with MAME's cycle
# count, the build takes 1,172,245 cycles: the copies and `cols` 836,000, the
# clear of $C021-$D3FF ($3AA5, an LDIR of 5,086 bytes) 106,851, the map
# unpackers $3B6C, $3C2A (also entered from the end of $3B6C) and $3B10
# about 216,000, the rest about 13,000. The Next ran that code about 8 times
# as fast. Their calls go to wrappers in unused cart bytes (bank 1
# $5E60-$5E89, $FF filler). A wrapper far-calls a page entry that works out
# the Master System cycles of the path the code is about to take (from the
# same RAM it reads; per call on the reference: $3B10 356 or 365, $3C2A 4,886
# or 4,893, $3B6C 6,242 or 6,249), runs the game's code, and far-calls `post`,
# which waits the rest of that time (`smswait`). $3B10 is counted with the
# routine called after it, so that one pair of far calls covers both. The
# lone call of $3B10 at $3D36 is left as it is.
label u3AA5 03AA5
label u3B6C 03B6C
label u3C2A 03C2A
label u3B10 03B10
asm 05E60 42  ; $FF filler: the wrappers
    rst $00
    db far_io, pg_p3AA5, ent_p3AA5
    call u3AA5
    rst $00
    db far_io, pg_post, ent_post
    ret
    rst $00
    db far_io, pg_p3B6C, ent_p3B6C
    call u3B10
    call u3B6C
    rst $00
    db far_io, pg_post, ent_post
    ret
    rst $00
    db far_io, pg_p3C2A, ent_p3C2A
    call u3B10
    call u3C2A
    rst $00
    db far_io, pg_post, ent_post
    ret
endasm
label w3AA5 05E60
label w3B6C 05E6C
label w3C2A 05E7B
asm 03A32 3   ; CALL $3AA5
    call w3AA5
endasm
asm 03FBD 6   ; CALL $3B10 : CALL $3B6C
    call w3B6C
endasm
asm 0402D 6   ; CALL $3B10 : CALL $3B6C
    call w3B6C
endasm
asm 0403E 6   ; CALL $3B10 : CALL $3C2A
    call w3C2A
endasm
asm 04063 6   ; CALL $3B10 : CALL $3B6C
    call w3B6C
endasm
# The load of state $0E (bank 11 $A700, the "fox x 3" screen): page 0 `p0E`
# (cave at $A70A) counts the handler's own code, and the name table copy
# $7EE7 is page 0 `nt7EE7`, with the Master System time of each.
label c22 05A4A
asm 03A22 3   ; LD BC,$8001 (the round build's start)
    jp c22
endasm
asm 05A4A 10  ; $FF filler
    rst $00
    db far_io, pg_pbs, ent_pbs
    ld bc,$8001
    jp $3A25
endasm
label c0E 05A40
asm 2E70A 3   ; LD BC,$2600
    jp c0E
endasm
asm 05A40 10  ; $FF filler
    rst $00
    db far_io, pg_p0E, ent_p0E
    ld bc,$2600
    jp $A70D
endasm
asm 07EE7 5   ; LD HL,$3800 : LD DE,$D8.. (the name table copy)
    rst $00
    db far_io, pg_nt7EE7, ent_nt7EE7
    ret
endasm
# The rest of the round build, counted as the routines above: $3AD8 (CALL
# at $4019) and $3ED0 (CALL at $4059) through wrappers at $5A00 and $5A0C,
# and the calls not wrapped ($7E97, $7E7A, $4422) at $3A97, the end of the
# build, before the display goes on (wrapper at $5A18).
label u3AD8 03AD8
label u3ED0 03ED0
asm 05A00 54  ; $FF filler: the wrappers
    rst $00
    db far_io, pg_pAD8, ent_pAD8
    call u3AD8
    rst $00
    db far_io, pg_post, ent_post
    ret
    rst $00
    db far_io, pg_pED0, ent_pED0
    call u3ED0
    rst $00
    db far_io, pg_post, ent_post
    ret
    rst $00
    db far_io, pg_pend, ent_pend
    rst $00
    db far_io, pg_pearly, ent_pearly
    ld a,$01
    ld ($C00E),a
    ld bc,$2600
    rst $08
    ld bc,$E001
    rst $08
    rst $00
    db far_io, pg_hold, ent_hold
    ret
endasm
label wAD8 05A00
label wED0 05A0C
label wEND 05A18
asm 04019 3   ; CALL $3AD8
    call wAD8
endasm
asm 04059 3   ; CALL $3ED0
    call wED0
endasm
asm 03A97 13  ; LD A,$01 : LD ($C00E),A ... RST $08 : RET
    jp wEND
endasm
# The VRAM copy at $7E41 (bank 1; called only from $0050, which maps a bank
# first) and the name table column writer at $408F (bank 1) cost about 8
# million Next cycles in a round build through the traps. Page 0 `vcopy`
# and `cols` write the bytes with jt_vwrite and add the Master System time of
# the replaced code, from its Z80 cycles, to the load's clock (`smswait`).
# Measured at 60 Hz against the reference with its 300-frame offset: the
# round build (state $0C) takes 20 frames, as on the reference (through the
# traps: 26), and $C011 has gone up by 3 one frame after it on both.
asm 07E41 11  ; RST $20 : LD A,(DE) : OUT ($BE),A ... JR NZ,$7E42 : RET
    rst $00
    db far_io, pg_vcopy, ent_vcopy
    ret
endasm
asm 0408F 40  ; LD HL,($C410) ... JP NZ,$409B : LD ($C429),A : RET
    rst $00
    db far_io, pg_cols, ent_cols
    ret
endasm
page 0 band wave vcopy cols p3AA5 p3B6C p3C2A post irqp pAD8 pED0 pend pearly hold p0E nt7EE7 pbs
; band: as the game's $8528-$8553. Register 1 = $80 (display off, frame
; interrupt off); register 1 = $C0 for SMS rows 2L on, when 0 < L < H;
; register 1 = $A0 from row 2H (row 191 at most, so the write comes before
; the frame event that the game's next HALT waits for). Each write goes
; through the game's RST $08 routine and the runtime, started early for
; the time the two traps take: ON_LEAD lines for the display-on write (the
; runtime makes the picture whole first), OFF_LEAD for the others. Measured
; in MAME with the status reads below: with 3 and 1 both edges came a row late.
; The game's handler would have counted H line interrupts in $C011: the
; entry adds H. The handler
; also reads the VDP status at each of them; the entry reads it before each
; write. Without that read a frame flag left from below the picture raised
; the frame interrupt as soon as the last write enabled it, and the game's
; next frame started in the picture, 20 to 30 lines after the band. Register 0
; stays $06 (the game writes $16 at the start and $06 at the end). The
; waits run with interrupts on, as the game's HALT loop does: no game
; event comes (frame and line interrupts are off), and the runtime's
; once-a-frame work at the ULA interrupt converts the tiles the game wrote
; this frame, so the display-on write stays short. With interrupts off
; through the waits, that write converted them itself and the band started
; 8 rows late, up to 60 in frames where the portraits changed. Returns
; with interrupts off, A = $06, BC = 0, HL = $C002, as the game's code.
; In 192-line mode SMS line N is Next line N (NextReg $1E, $1F).
        OPT --zxnext
ON_LEAD equ 4
OFF_LEAD equ 2
band:   di
        ld bc,$8001
        rst $08                 ; display off, frame interrupt off
        ld hl,($C1DA)           ; L, H
        ld a,($C011)
        add a,h
        ld ($C011),a
        ld a,l
        or a
        jr z,.off
        cp h
        jr nc,.off
        add a,a                 ; row 2L
        ld d,ON_LEAD
        ei
        call bwait
        rst $00
        db $0D                  ; IN A,($BF), as the game's handler
        ld bc,$C001
        rst $08                 ; display on
.off:   ld a,($C1DB)
        add a,a                 ; row 2H, at most 191
        jr c,.cl
        cp 192
        jr c,.ok
.cl:    ld a,191
.ok:    ld d,OFF_LEAD
        ei
        call bwait
        rst $00
        db $0D                  ; IN A,($BF)
        ld bc,$A001
        rst $08                 ; display off, frame interrupt on
        ld bc,$0600
        rst $08                 ; line interrupts off
        di
        ret
; wave: as the game's $807A-$8098. Stamps $DFF8 with isr_n for the
; rastercode routine (psychofox-raster.asm), so its table is valid for the
; picture after this frame handler entry. Register 0 stays $26: the game
; writes $36 at the start and $26 after. Waits, with interrupts on, for
; line 191, where the game's 96th line interrupt comes (called in the
; vertical blank: of the next picture). The handler would have counted 96
; interrupts in $C011 and read the status at each: the entry adds 96 and
; reads it once. Returns with interrupts off, B = C = 0, HL = $C1A0, A = $88,
; as the loop leaves them (its last H write is overwritten by $7EB4 before
; any line shows it).
wave:   di
        ld a,(isr_n)
        ld ($DFF8),a
        ld a,($C011)
        add a,96
        ld ($C011),a
        ld a,191
        ld d,0
        ei
        call bwait
        rst $00
        db $0D                  ; IN A,($BF), as the game's handler
        di
        ld bc,0
        ld hl,$C1A0
        ld a,$88
        ret
; bwait: wait until the beam is on SMS line A - D of a picture (A is 1 to
; 191). Called in the vertical blank it waits for the next picture. Called
; in the picture past the line it returns at once: waiting for the next
; picture would keep interrupts off over the frame event, the game's next
; frame would then start late in the picture, and so would every band call
; after it. That happens once, on the first frame of the opening band,
; where the display-on write takes the runtime most of a frame (pic_ready
; converts the pause screen's tiles); that frame shows the band from the
; line where the write ends.
bwait:  sub d
        jr nc,.t
        xor a
.t:     ld e,a
        call bline
        cp 192
        jr nc,.w                ; below the picture
        cp e
        ret nc                  ; past the line in this picture
.w:     call bline
        cp 192
        jr nc,.w
        cp e
        jr c,.w
        ret
; bline: A = the beam's Next line, or 255 from line 256 on. Reads with
; interrupts off (the runtime's handlers select other NextRegs) and
; returns with them on. Keeps BC, DE, HL.
bline:  push bc
.rd:    di
        ld a,$1E
        call nrd
        ld b,a
        ld a,$1F
        call nrd
        ld c,a
        ld a,$1E
        call nrd
        cp b
        jr nz,.rd
        or a
        ld a,c
        jr z,.lo
        ld a,255
.lo:    pop bc
        ei
        ret
nrd:    push bc
        ld bc,$243B
        out (c),a
        inc b
        in a,(c)
        pop bc
        ret
; vcopy: as the game's $7E41-$7E4B: HL = VDP address, DE = source, BC = n
; bytes (0: 65536), copied to VRAM at HL AND $3FFF. One jt_vwrite of runs
; of 256 and one for the rest. Returns as the loop leaves the registers: A =
; 0, BC = 0, DE = source + n, HL kept, Z set, carry clear; IX, IY kept.
; Master System time: RST $20 and its routine 65 cycles, 50 a byte (45 for
; the last), RET 10: 50n + 70; and $0050 around it (its only caller: CALL
; $0050, CALL $0044 and $0044, CALL $7E41, LD A,($C013), JP $0044 and
; $0044): 188.
vcopy:  call tstart
        push ix
        push iy
        push hl
        push de
        push bc
        ex de,hl                ; HL = source, DE = VRAM
        ld a,b
        or c
        jr nz,.nz
        jr .run                 ; n = 0: B = 0, 256 runs of 256
.nz:    ld a,b                  ; whole runs of 256, one jt_vwrite each, so
        or a                    ; that the time is read at least once a
        jr z,.rest              ; frame (tick)
.run:   push bc
        ld bc,$0001
        xor a
        call jt_vwrite
        inc h
        inc d
        call tick
        pop bc
        djnz .run
.rest:  ld a,c
        or a
        jr z,.done
        ld b,a
        ld c,1
        xor a
        call jt_vwrite
.done:  pop bc                  ; BC = n; cycles = 50n + 70 in A:HL
        push bc
        ld h,b
        ld l,c
        xor a
        ld e,a                  ; E:HL = n (n = 0: 65536)
        ld a,h
        or l
        jr nz,.n
        inc e
.n:     ld a,e                  ; x 50 = x 32 + x 16 + x 2
        add hl,hl
        rla                     ; x2
        push hl
        push af
        add hl,hl
        rla
        add hl,hl
        rla
        add hl,hl
        rla                     ; x16
        push hl
        push af
        add hl,hl
        rla                     ; x32
        pop bc                  ; B = x16 high
        pop de                  ; DE = x16 low
        add hl,de
        adc a,b
        pop bc                  ; B = x2 high
        pop de
        add hl,de
        adc a,b
        ld de,70+188
        add hl,de
        adc a,0
        call smswait
        pop bc                  ; n
        pop de                  ; source
        pop hl                  ; VDP address
        pop iy
        pop ix
        ex de,hl                ; DE = source + n
        add hl,bc
        ex de,hl
        ld bc,0
        xor a                   ; A = 0, Z, no carry
        ret
; cols: as the game's $408F-$40B6: 28 rows of 2 bytes from ($C414) to the
; VDP address ($C410), both stepping $40. Returns as the game's loop: HL =
; ($C410) + $700, DE = ($C414) + $700, BC = $40, A = 0 (also into $C429),
; A' = the last byte written; IX, IY kept. Master System time: the CALL
; $408A and its test of $C429 (39), 53 cycles before the loop, 126 a row,
; 23 after: 3,643.
cols:   call tstart
        push ix
        push iy
        ld hl,($C414)
        ld de,($C410)
        ld bc,$021C
        ld ix,$40
        ld iy,$40
        xor a
        call jt_vwrite
        ld bc,27*$40+1          ; A' = the second byte of the last row
        add hl,bc
        ex af,af'
        ld a,(hl)
        ex af,af'
        pop iy
        pop ix
        xor a
        ld hl,3643
        call smswait
        ld hl,($C410)
        ld bc,$700
        add hl,bc
        ex de,hl
        ld hl,($C414)
        add hl,bc
        ex de,hl
        ld bc,$40
        ld a,1
        dec a
        ld ($C429),a
        ret
; p3AA5, p3B6C, p3C2A: start the clock (tstart) and work out in t_cyc the
; Master System cycles of the calls the wrapper is about to make, each with
; its CALL (17). Keep every register. post: wait until that time has passed
; (smswait). Keeps every register and the flags.
P3AA5_C equ 17+106851          ; CALL; $3AA5: 4 loads, LDIR of 5,086, RET
p3AA5:  call pall
        ld a,($C01C)            ; for pend: the handler's branch at $3A35
        ld (b_01c),a
        ld hl,P3AA5_C & $FFFF
        ld a,P3AA5_C >> 16
        ld (t_cyc),hl
        ld (t_cyc+2),a
        jp pallx
p3B6C:  call pall
        call c3B10
        ld hl,17
        call cadd
        call c3B6C
        jp pallx
p3C2A:  call pall
        ld hl,106               ; $4036-$4056: the rest of $3FF8's loop
        call cadd
        call c3B10
        ld hl,17
        call cadd
        ld a,(s418)
        call c3C2A
        jp pallx
post:   push af
        push bc
        push de
        push hl
        ld hl,(t_cyc)
        ld a,(t_cyc+2)
        call smswait
        pop hl
        pop de
        pop bc
        pop af
        ret
; pearly: adds pend's cycles (t_cyc) to t_bud, but waits only until HOLD_M
; lines before it, so that
; the display-on write that follows has time for the runtime's pic_ready
; (the tiles and maps written since the last once-a-frame work: 26 lines in
; round 1-1, traced). hold: right after that write, turns the Next's
; tilemap and sprites off again and shows the backdrop colour (NextReg $6B,
; $15 and $4A as r1_hw and fallback2 set them for the display off), waits
; until t_bud, and puts the three registers back: the picture comes on at
; the Master System's line. Uses runtime internals cram ($E04D), vdp_regs
; and pal_hi_table ($E300) of the 16:44 build of nms.nex. Keep every
; register.
HOLD_M  equ 132
pearly: push af
        push bc
        push de
        push hl
        ld hl,(t_cyc)           ; pend's cycles
        ld a,(t_cyc+2)
        call sadd
        ld hl,(t_bud)
        ld (t_tgt),hl
        ld de,HOLD_M
        or a
        sbc hl,de
        jr nc,.ok
        ld hl,0
.ok:    ld (t_bud),hl
        call swait
        ld hl,(t_tgt)
        ld (t_bud),hl
        pop hl
        pop de
        pop bc
        pop af
        ret
hold:   push af
        push bc
        push de
        push hl
        ld a,$6B
        call nrd
        ld (h_6b),a
        and $10
        or $02
        nextreg $6B,a
        ld a,$15
        call nrd
        ld (h_15),a
        and $FE
        nextreg $15,a
        ld a,$4A
        call nrd
        ld (h_4a),a
        ld a,(vdp_regs+7)       ; the backdrop: CRAM 16 + register 7
        and $0F
        add a,255&(cram+16)
        ld l,a
        ld h,(cram+16)>>8
        ld a,(hl)
        ld l,a
        ld h,0
        ld de,$E300
        add hl,de
        ld a,(hl)
        nextreg $4A,a
        call swait              ; until t_bud
        ld a,(h_6b)
        nextreg $6B,a
        ld a,(h_15)
        nextreg $15,a
        ld a,(h_4a)
        nextreg $4A,a
        pop hl
        pop de
        pop bc
        pop af
        ret
; p0E: at $A70A, the start of the load of state $0E (bank 11 $A700, the
; "fox x 3" screen). Starts the clock and adds the handler's own Master
; System cycles, counted from the code: 27 to the JP Z, three RST $08
; writes (96 each), the CRAM load (61 + 687), the loads and CALLs of the two
; $0050 copies (37 + 86), CALL $7E97 and $7E97 (17 + 1,368), CALL $7EA5 and
; $7EA5 (93), 38, the fill of $D800-$DEFF (20 + 896 x 58 - 5), 33 + 27, the
; lives digits from ($C016): hundreds and tens loops (42 x k - 5 each, k
; the digit + 1) with 7 + 7 + 13, 47, the leading zero loop (40 a zero,
; 26 at the first other digit) and the digit loop (52 a digit, 47 the
; last), then RST $08 (96), RET and JP $0154 (20). The copies and $7EE7
; add their own time. Keeps every register.
p0E:    call pall
        ld hl,54745+74+96+20
        call cadd
        ld a,($C016)
        ld c,0                  ; hundreds
.h:     cp 100
        jr c,.hd
        sub 100
        inc c
        jr .h
.hd:    ld b,0                  ; tens
.t:     cp 10
        jr c,.td
        sub 10
        inc b
        jr .t
.td:    ld (d_u),a
        ld a,c
        ld (d_h),a
        ld a,b
        ld (d_t),a
        inc c                   ; k = hundreds + 1
        call .k42
        ld c,b
        inc c
        call .k42
        ld hl,d_h               ; leading zeros, then the digits
        ld b,3
.z:     ld a,(hl)
        or a
        jr nz,.nz
        push hl
        ld hl,40
        dec b
        jr nz,.z2
        ld hl,35                ; three zeros: the last DJNZ falls through,
.z2:    inc b                   ; then 256 digits
        call cadd
        pop hl
        inc hl
        djnz .z
        ld b,0
        jr .pr
.nz:    push hl
        ld hl,26
        call cadd
        pop hl
.pr:    ld hl,47                ; the last digit: 47, the others 52
        call cadd
        dec b
        jr z,.pd
.p2:    ld hl,52
        call cadd
        djnz .p2
.pd:    jp pallx
.k42:   ld hl,37                ; 42 x k - 5
        call cadd
        dec c
        ret z
.k1:    ld hl,42
        call cadd
        dec c
        jr nz,.k1
        ret
; nt7EE7: as the game's $7EE7-$7EFA: the name table, $700 bytes from $D800,
; to VRAM $3800, written with jt_vwrite in runs of 256 (the clock is read
; after each, tick). Returns as the game's loop: A = 0, BC = 0, DE = $DF00,
; HL = $3800, Z set, carry clear; IX, IY kept. Master System time: CALL 17,
; three loads 30, RST $20 and its routine 65, 50 a byte (45 the last), RET
; 10: 89,717.
nt7EE7: call tstart
        push ix
        push iy
        ld hl,$D800
        ld de,$3800
        ld b,7
.r:     push bc
        ld bc,$0001
        xor a
        call jt_vwrite
        inc h
        inc d
        call tick
        pop bc
        djnz .r
        ld a,(89717>>16)&255
        ld hl,89717&$FFFF
        call smswait
        pop iy
        pop ix
        ld hl,$3800
        ld de,$DF00
        ld bc,0
        xor a
        ret
; pbs: at $3A22, the first instruction of the round build: starts the
; clock there, so that the build's first writes (counted in pend) are on it.
; Keeps every register.
pbs:    jp tstart
; pAD8: CALL $3AD8 and the routine: 17 + 11,297 (no branch on data: two
; $3CC2 of 3, a $3CE0 of 12, $421A's 24 rows; equal to the reference's trace).
; pED0: CALL $3ED0 and the routine: 17 + 2,561 + $4251 (153, 157 when
; ($C436) >= 2, +26 when it is 0) + $42B8 (1,361, +7 for each of the 32
; bytes at $C600 + 8k that ($C023) is not below).
pAD8:   call pall
        ld hl,17+11297
        call cadd
        jp pallx
pED0:   call pall
        ld hl,17+2561+153+1361
        call cadd
        ld a,($C436)
        or a
        jr nz,.n0
        ld hl,26
        call cadd
.n0:    cp 2
        jr c,.n2
        ld hl,4
        call cadd
.n2:    ld a,($C023)
        ld c,a
        ld hl,$C600
        ld de,8
        ld b,32
.lp:    ld a,c
        cp (hl)
        jr c,.nw
        push hl
        ld hl,7
        call cadd
        pop hl
.nw:    add hl,de
        djnz .lp
        jp pallx
; pend: at $3A97, the end of the round build: the build's code not counted
; on the way, each routine with its CALL, counted path by path from the
; code and the values it reads (taken here, at the end of the build: the
; build clears $C021-$D3FF first, and the routines below leave these
; values as they found them; ($C01C) is taken at the start, by p3AA5):
;   the handler's own code: the three RST $08 writes (288), 17, the branch
;     at $3A35 (29, or 159 when ($C01C) was not 0), the CALLs (16 x 17),
;     $3A70 with CALL $0044 and $0044 (81), $3A87 (17, CALL NZ 10), and the
;     end up to the display-on OUT (174);
;   $7E97 (1,368), $7E7A (4,131), $4422 (535, 542 when ($C020) >= $15);
;   $41FF (40 when ($C020) >= $15, else 99 + 34 x ($C020) / 3);
;   $7B00 and its five $7B8D, each $7B8D from its table byte;
;   $7DE9 (96, less 17 for the JP $0050 that vcopy counts as a CALL);
;   $7C00 (868), $43EA (125), $43AF (135), $4FD7 (131), $43CA (151, 152
;     when ($C020) >= $15), $39FB (32, or 192 when ($C01D) is not 0);
;   $3FF8 outside its loop (378, with SUB when ($C024) - $10 >= $E0: +11),
;     and $41AE when ($C023) is 0 (17 + 191, or 17 + 31 when ($C020) >= $15);
;   $109B, run through on its values (c109B);
;   $7DAD with $7D70 (by ($CAB4), ($C24B) and ($C020)).
; Not counted: bank 4 $8000 (the object handler; 140 in round 1-1's
; trace, added as that) and $1EB7 (called when ($C0A0) is not 0; not in
; the round 1-1 build). All keep every register.
pend:   call pall
        ld hl,288+17+221+51+81+17+174+1368+4131+535+868+125+135+131+151+140+378
        call cadd
        ld a,(b_01c)
        or a
        ld hl,29
        jr z,.c1
        ld hl,159
.c1:    call cadd
        ld a,($C0A0)
        or a
        ld hl,10                ; CALL NZ not taken
        jr z,.c2
        ld hl,17                ; taken ($1EB7 itself not counted)
.c2:    call cadd
.c3:    ld a,($C020)
        cp $15
        jr c,.r1
        ld hl,7+1               ; $4422 +7, $43CA +1
        call cadd
        ld hl,40                ; $41FF
        call cadd
        jr .r2
.r1:    ld hl,99                ; $41FF: 99 + 34 per subtraction of 3
        call cadd
        ld b,a
.r1l:   ld a,b
        cp 3
        jr c,.r2
        sub 3
        ld b,a
        ld hl,34
        call cadd
        jr .r1l
.r2:    ld a,($C01D)            ; $39FB
        or a
        ld hl,32
        jr z,.c4
        ld hl,192
.c4:    call cadd
        call c7B00
        ld hl,96-17             ; $7DE9
        call cadd
        call c3FF8
        call c109B
        call c7DAD
        jp pallx
; c7B00: $7B00 and its five $7B8D (each ending in JP $0050, which vcopy
; counts as a CALL: -7).
c7B00:  ld a,($C020)
        ld hl,13+7+12+13
        cp $15
        ld a,($C021)
        jr c,.a
        ld hl,13+7+7+7+10
        ld a,6
.a:     call cadd
        ld b,a                  ; A x 5
        add a,a
        add a,a
        add a,b
        ld e,a
        ld d,0
        ld hl,4+4+4+4+4+7+13+4+11+16+5*(10+17)+10
        call cadd
        ld a,($CAB4)
        or a
        ld hl,$7B47
        ld bc,12+10
        jr z,.b
        ld hl,$7B6A
        ld bc,7+10+12
.b:     add hl,de
        push hl
        ld h,b
        ld l,c
        call cadd
        pop de                  ; DE = the table pointer
        ld b,5
.c:     ld a,(de)
        inc de
        ld hl,20+7+6+20+7+12+7
        cp $20
        jr c,.d
        sub $20
        ld hl,20+7+6+20+7+7+7+7+10
.d:     call cadd
.e:     cp 8
        jr c,.f
        sub 8
        push af
        ld hl,37
        call cadd
        pop af
        jr .e
.f:     ld hl,19+12+7+4+7+4+10+10-17
        call cadd
        djnz .c
        ret
; c3FF8: $3FF8's code outside its loop, and $41AE.
c3FF8:  ld hl,($C024)
        ld de,$0110
        or a
        sbc hl,de
        ld a,l
        cp $E0
        jr c,.a
        ld hl,11
        call cadd
.a:     ld a,($C023)
        or a
        ret nz
        ld a,($C020)
        cp $15
        ld hl,17+191
        jr c,.b
        ld hl,17+13+7+11
.b:     jp cadd
; c7DAD: $7DAD and $7D70 (17 + 105) and its RET.
c7DAD:  ld hl,13+4+10+17+105+10
        call cadd
        ld a,($CAB4)
        or a
        ld hl,7+10
        jr nz,.x
        ld hl,13+7+10
        call cadd
        ld a,($C24B)
        cp 1
        ld hl,7+10
        jr z,.x
        ld hl,13+7+10
        call cadd
        ld a,($C020)
        cp $15
        ld hl,7+10
        jr nc,.x
        ld hl,13+7+4+10+11+7
.x:     jp cadd
; c109B: $109B run through on its values: the fox's sprite positions.
; Follows every branch of $109B, $11C1 and $11D8 with the same arithmetic
; and flags, adding each instruction's cycles. Uses AF, BC, DE, HL, IX.
c109B:  ld hl,13+7
        call cadd
        ld a,($C24B)
        cp 2
        jr nz,.n1
        ld hl,7+13+4
        call cadd
        ld a,($C24C)
        rra
        jr nc,.n2
        ld hl,7+10+10+10+10+205+10
        jp cadd
.n2:    ld hl,12
        call cadd
        jr .b6
.n1:    ld hl,12
        call cadd
.b6:    ld hl,13+7
        call cadd
        ld a,($C203)
        ld c,0                  ; C = the +2 to ($C034) at $10C1
        cp 8
        jr c,.s1
        ld hl,7+7
        call cadd
        cp $0A
        jr nc,.s1
        ld hl,7+10+7+7+7
        call cadd
        ld c,2
        jr .c8
.s1:    ld hl,12
        call cadd
.c8:    ld hl,4+17+17+10+7+7+7  ; XOR, CALL $11C1, CALL $11D8, LD HL, ADD, JR C, CP
        call cadd
        ld a,($C034)
        add a,c
        cp $E0
        jr c,.l1
        sub $E0
        ld e,a
        ld hl,7+7+4
        call cadd
        ld a,($C035)
        inc a
        jr .l2
.l1:    ld e,a
        ld hl,12
        call cadd
        ld a,($C035)
.l2:    ld d,a                  ; DE = the HL that $11D8 returns
        ld hl,4+4+13+7+4+10+20+4+13+4
        call cadd
        ld hl,($C024)           ; L = H of it ... as $11C4-$11D7
        ld a,e
        sub l
        jr nc,.l3
        sub $20
        ld e,a
        ld a,d
        scf
        sbc a,h
        ld d,a
        ld hl,7+7+4
        jr .l4
.l3:    ld e,a
        ld a,d
        sub h
        ld d,a
        ld hl,12
.l4:    call cadd
        ld hl,13+4+4+10+4+13+4+13+10+7+13+7
        call cadd               ; to the C229 tests
        ld h,d                  ; H, L as at $10CC
        ld l,e
        ld a,($C229)
        ld ix,$11EE
        ld b,0                  ; B: entry at $112C (C229 = 7)
        cp 2
        jr z,.t2
        push hl
        ld hl,7+7
        call cadd
        pop hl
        cp 4
        jr z,.t2
        push hl
        ld hl,7+7
        call cadd
        pop hl
        cp 7
        jr z,.t7
        push hl
        ld hl,7+14+12
        call cadd
        pop hl
        jr .lp
.t2:    push hl
        ld hl,12+14
        call cadd
        pop hl
        ld ix,$11F2
        jr .lp
.t7:    push hl
        ld hl,12+14+7+12
        call cadd
        pop hl
        ld ix,$11F6
        ld b,1
.lp:    ld c,4                  ; four sprites
.it:    ld a,b
        or a
        jp nz,.st               ; the C229 = 7 entry goes to the store
        ld a,(ix+0)
        push hl
        ld hl,19+4
        call cadd
        pop hl
        add a,l
        jr c,.cy
        cp $E0
        jr c,.lt
        push hl
        ld hl,7+7+7+7+4
        call cadd
        pop hl
        sub $E0
        jr .sb
.cy:    push hl
        ld hl,12+7+4
        call cadd
        pop hl
        sub $E0
.sb:    ld e,a                  ; ($C1D3); CCF gives carry 1
        ld a,h
        inc a
        jr .ad
.lt:    push hl
        ld hl,7+7+12
        call cadd
        pop hl
        ld e,a
        ld a,h
.ad:    push hl
        ld hl,13+4+4+7
        call cadd
        pop hl
        or a
        jr nz,.nz
        ld a,e                  ; zero: ($C1D3) = $D0?
        push hl
        ld hl,7+13+7
        call cadd
        pop hl
        cp $D0
        jr nz,.st7
        push hl
        ld hl,12+7+12
        call cadd
        pop hl
        jr .e0
.st7:   push hl
        ld hl,7
        call cadd
        pop hl
        jr .st
.nz:    push hl
        ld hl,12+7
        call cadd
        pop hl
        cp $FF
        jr nz,.e0c
        ld a,e
        push hl
        ld hl,7+13+7
        call cadd
        pop hl
        cp $D8
        jr c,.e0j
        push hl
        ld hl,7+7+12
        call cadd
        pop hl
        jr .st
.e0j:   push hl
        ld hl,12
        call cadd
        pop hl
        jr .e0
.e0c:   push hl
        ld hl,12
        call cadd
        pop hl
.e0:    push hl
        ld hl,7+12
        call cadd
        pop hl
.st:    ld b,0
        push hl
        ld hl,7+6+7+6+10+13     ; the stores, INC IX, DJNZ
        call cadd
        pop hl
        inc ix
        dec c
        jp nz,.it
        ld hl,12-5              ; JR $1130; the last DJNZ is 8, not 13
        call cadd
        ld hl,7+13+7            ; $1130: LD C, LD A, CP 2
        call cadd
        ld bc,0
        ld a,($C229)
        cp 2
        jr z,.d3
        ld hl,7+7
        call cadd
        cp 4
        jr z,.d3b
        ld hl,12
        call cadd
        jr .d8
.d3b:   ld hl,7
        call cadd
        jr .d3c
.d3:    ld hl,12
        call cadd
.d3c:   ld hl,13+7
        call cadd
        ld a,($C03B)
        cp 1
        jr z,.d4
        ld hl,7+6+12
        call cadd
        dec bc
        jr .d8
.d4:    ld hl,12+6
        call cadd
        inc bc
.d8:    push bc
        ld hl,13+20+4+4+13+13+4+4
        call cadd
        ld a,($C031)
        ld de,($C022)
        sub e
        ld l,a
        ld a,($C032)
        sbc a,d
        ld h,a
        call .zz                ; $1159
        ld a,l
        add a,8
        ld l,a
        ld a,h
        adc a,0
        ld h,a
        push hl
        ld hl,4+7+4+4+7+4
        call cadd
        pop hl
        call .zz                ; $1174
        pop bc
        ld a,l
        add a,c
        ld l,a
        ld a,h
        adc a,b                 ; H is not stored here, as in the game
        push hl
        ld hl,4+4+4+4+4
        call cadd
        pop hl
        call .zz                ; $118C
        ld a,l
        sub 8
        ld l,a
        ld a,h
        sbc a,0                 ; $11A6: JR Z, then RET either way
        ld hl,4+7+4+4+7+12+4+13+13+10
        jr z,.zl
        ld hl,4+7+4+4+7+7+7+13+13+10
.zl:    jp cadd
.zz:    or a                    ; JR Z: zero 12 + 4 + 13 + 13, else 7 + 7 + 13 + 13 + 12
        push hl
        ld hl,12+4+13+13
        jr z,.zy
        ld hl,7+7+13+13+12
.zy:    call cadd
        pop hl
        ret
; pall: save AF, BC, DE, HL, IX, IY above the caller's return, start the
; clock, t_cyc = 0. pallx: put them back and return from the entry.
pall:   ex (sp),hl              ; HL = return into the entry
        ld (pl_ret),hl
        pop hl
        push af
        push bc
        push de
        push hl
        push ix
        push iy
        call tstart
        xor a
        ld h,a
        ld l,a
        ld (t_cyc),hl
        ld (t_cyc+2),a
        ld hl,(pl_ret)
        jp (hl)
pallx:  pop iy
        pop ix
        pop hl
        pop de
        pop bc
        pop af
        ret
; cadd: t_cyc += HL. Keeps AF, BC, DE.
cadd:   push af
        push de
        ld de,(t_cyc)
        add hl,de
        ld (t_cyc),hl
        ld a,(t_cyc+2)
        adc a,0
        ld (t_cyc+2),a
        pop de
        pop af
        ret
; c3B10: the cycles of $3B10 (356 with its three JR C taken; +6, +3, +9
; when not) and the values it leaves for $3B6C and $3C2A, in s408, s40A,
; s418, s404, s41F, worked out from $C407, $C406 and $C400 as it does.
c3B10:  ld hl,17+356
        call cadd
        ld a,($C407)
        add a,a
        ld b,a
        ld a,($C406)
        and $F0
        rrca
        rrca
        rrca
        rrca
        ld (s408),a
        cp 7
        jr c,.s1
        sub 7
        inc b
        ld hl,6
        call cadd
.s1:     ld (s40A),a
        ld c,b                  ; ($C41A)
        ld b,0
        ld a,($C406)
        and $0F
        cp 8
        jr c,.s2
        inc b
        ld hl,3
        call cadd
.s2:     ld a,b
        ld (s418),a
        ld d,0
        ld a,($C400)
        and $F0
        rrca
        rrca
        rrca
        rrca
        cp 8
        jr c,.s3
        sub 8
        ld d,6
        ld hl,9
        call cadd
.s3:     ld (s404),a
        ld a,c
        add a,d
        ld (s41F),a
        ret
; c3C2A: the cycles of $3C2A from its first instruction to its RET, with
; A = ($C418) when it runs: 4,886 when ($C400) AND $0F < 8, its column
; counter (from ($C408)) never reaches 13 in the first 13 rows and
; ($C418) = 0; +7, +18 for each reset of the counter, +143 for the last
; cell.
c3C2A:  push af
        ld hl,4886
        call cadd
        ld a,($C400)
        and $0F
        cp 8
        jr c,.n
        ld hl,7
        call cadd
.n:     ld a,(s408)
        ld c,a
        ld b,13
.r:     ld a,c
        cp 13
        jr nz,.i
        ld hl,18
        call cadd
        ld c,0
        jr .rn
.i:     inc c
.rn:    djnz .r
        pop af
        or a
        ret z
        ld hl,143
        jp cadd
; c3B6C: the cycles of $3B6C, run through its loop on the values it reads
; ($C436, the map bytes at $C800/$C860/$C8C0 + 8 x ($C41F) + ($C404), and
; s40A, s418, s41F, s404 from c3B10), ending in $3C2A (c3C2A).
c3B6C:  ld hl,167+16
        call cadd
        ld a,($C436)
        ld de,$C800
        ld hl,20
        cp 2
        jr z,.tb
        ld de,$C8C0
        ld hl,37
        cp 1
        jr z,.tb
        ld de,$C860
        ld hl,27
.tb:    call cadd
        ld (b_tab),de
        ld a,(s41F)
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        ld (b_422),hl
        ld a,14
        ld (b_428),a
        ld a,(s40A)
        ld (b_41b),a
        ld a,(s418)
        ld (b_418),a
.bac:   ld hl,16
        call cadd
.baf:   ld hl,94+96
        call cadd
        ld hl,(b_422)           ; the map byte: $FF takes the other path
        ld de,(b_tab)
        add hl,de
        ld a,(s404)
        ld e,a
        ld d,0
        add hl,de
        ld a,(hl)
        cp $FF
        ld hl,83
        jr nz,.nf
        ld hl,121
.nf:    call cadd
        ld a,(b_41b)
        ld c,a
        ld a,7
        sub c
        ld c,a                  ; n = 7 - ($C41B)
        ld a,(b_428)
        cp c
        jr nc,.ge
        ld c,a                  ; len = ($C428), which becomes 0
        xor a
        ld hl,20
        jr .ln
.ge:    sub c
        ld hl,21
.ln:    ld (b_428),a
        call cadd
        ld d,0                  ; 13 + LDIR (21 x len - 5) + 72
        ld e,c
        ld hl,0
        ld b,21
.mul:   add hl,de
        djnz .mul
        ld de,13-5+72
        add hl,de
        call cadd
        xor a
        ld (b_41b),a
        ld a,(b_428)
        or a
        jr z,.end
.c1d:   ld hl,63
        call cadd
        ld hl,(b_422)
        ld de,8
        add hl,de
        ld (b_422),hl
        jp .baf
.end:   ld a,(b_418)
        cp 1
        jr z,.again
        ld hl,32
        call cadd
        jp c3C2A
.again: ld hl,100
        call cadd
        ld a,1
        ld (b_428),a
        inc a
        ld (b_418),a
        ld a,(s40A)
        ld (b_41b),a
        or a
        jp nz,.bac
        jr .c1d
; irqp: at the main loop's EI; HALT ($00B7), where every load ends. NZ
; when the VDP's frame flag is set (vdp_status bit 7) and register 1 has
; frame interrupts on. The runtime sets the flag at each frame event that
; comes while frame interrupts are off and enters no handler, and it raises
; no interrupt when the game turns them on again. On the Master System the
; flag asserts the interrupt line, and the handler runs at the first EI with
; frame interrupts on. Also stops CTC channel 0 (the docs of NextZXOS do not
; say whether it uses the CTC), so the next timed routine starts a new clock
; (tstart). Keeps A and every other register.
irqp:   push bc
        ld b,a
        ld a,(t_ctc)
        or a
        jr z,.nc
        xor a
        ld (t_ctc),a
        push bc
        ld bc,$183B
        ld a,$03                ; control word, reset: the channel stops
        out (c),a
        pop bc
.nc:    ld a,(vdp_regs+1)
        and $20
        jr z,.x
        ld a,(vdp_status)
        and $80                 ; NZ: the flag is set
.x:     ld a,b
        pop bc
        ret
; tstart: start or go on with the clock of the replaced routines. The clock
; runs over a whole load: t_el counts the lines since its start, t_bud the
; Master System time owed so far, in lines. Each replaced routine adds its
; time to t_bud and waits until t_el reaches it, so the far calls and the
; game's own code between the routines take part of that time instead of
; adding to it. A gap of more than T_GAP lines since the last wait ended
; (a new frame of the game, not a load) starts the clock again. Starts the
; CTC timer at the first call. Keeps every register.
T_GAP   equ 200
tstart: push af
        push bc
        push de
        push hl
        ld a,i
        push af
        di
        ld a,(t_ctc)            ; the CTC timer, once
        or a
        jr nz,.on
        inc a
        ld (t_ctc),a
        ld bc,$183B
        ld a,$27                ; timer, prescaler 256, time constant next, reset
        out (c),a
        xor a                   ; time constant 256
        out (c),a
        jr .new
.on:    call tick               ; the gap since the last wait
        ld hl,(t_el)
        ld de,(t_end)
        or a
        sbc hl,de
        ld de,T_GAP+1
        or a
        sbc hl,de
        jr c,.go                ; a short gap: the same load
.new:   call rd16
        ld (t_s),de
        ld bc,$183B
        in a,(c)
        ld (t_c),a
        ld hl,0
        ld (t_el),hl
        ld (t_bud),hl
        ld (t_end),hl           ; a new clock: the gap test counts from here
.go:    pop af
        jp po,.di
        ei
.di:    pop hl
        pop de
        pop bc
        pop af
        ret
; tick: add the time since the last read to t_el, in lines. The line
; count gives the gap modulo the Next's frame, and gaps of a frame or more
; come: the runtime's once-a-frame work, run inside jt_vwrite (vbl_chkv)
; with the game's interrupts off, converts a level's new tiles and took up
; to about 1.2 frames in a round build. So the entry also runs CTC channel
; 0 as a free timer (28 MHz clock, prescaler 256, time constant 256, no
; interrupt: one count every 256 cycles, a turn every 65,536 cycles, about
; 36 lines), which gives the gap modulo 65,536 cycles. Of the gaps d, d +
; one frame and d + two frames (1,824 cycles a line), the one whose cycle
; count agrees best with the CTC is taken. The read and the count run with
; interrupts off: with the game's interrupts on, the once-a-frame work came
; between them and the read was stale. Keeps BC, DE, HL; changes AF.
tick:   push bc
        push de
        push hl
        push ix
        ld a,i                  ; P/V = the game's interrupt state
        push af
        di
        ld a,$05
        call nrd
        and 4                   ; NextReg $05 bit 2: 60 Hz
        ld bc,311
        jr z,.fl
        ld bc,264
.fl:    ld (t_fl),bc
        call rd16
        ld bc,$183B             ; CTC channel 0 count, down
        in a,(c)
        ld c,a
        ld a,(t_c)
        sub c                   ; CTC counts since the last read, mod 256
        ld (t_g),a
        ld a,c
        ld (t_c),a
        ld hl,(t_s)
        ex de,hl                ; HL = now, DE = last
        ld (t_s),hl
        or a
        sbc hl,de               ; d = now - last, mod the frame
        jr nc,.d
        ld de,(t_fl)
        add hl,de
.d:     ld ix,$FFFF             ; best distance so far (IXL), best gap in t_bg
        ld b,3                  ; k = 0, 1, 2
.k:     push hl
        push bc
        ld d,h                  ; HL * 57 / 8 = the gap in CTC counts
        ld e,l
        add hl,hl               ; x2
        add hl,hl               ; x4
        add hl,hl               ; x8
        push hl
        add hl,hl               ; x16
        add hl,hl               ; x32
        add hl,hl               ; x64
        pop bc
        or a
        sbc hl,bc               ; x56
        add hl,de               ; x57
        srl h
        rr l
        srl h
        rr l
        srl h
        rr l
        ld a,(t_g)
        sub l                   ; circular distance to the CTC's count
        jp p,.ab
        neg
.ab:    cp ixl
        jr nc,.nb
        ld ixl,a
        ld (t_bg),de
.nb:    pop bc
        pop hl
        ld de,(t_fl)
        add hl,de
        djnz .k
        ld hl,(t_bg)
        ld de,(t_el)
        add hl,de
        ld (t_el),hl
        pop af
        jp po,.di
        ei
.di:    pop ix
        pop hl
        pop de
        pop bc
        ret
; smswait: A:HL = Master System cycles of the replaced code. Adds them to
; t_bud and waits until t_el reaches it. The unit is the Next's line,
; scaled so that a Master System frame is a Next frame: at 60 Hz 59,736
; cycles (an NTSC frame) to 264 lines, at 50 Hz 71,364 (a PAL frame, 313
; lines) to 311, so a load takes as many frames as on the Master System.
; The divisor is in 1/256 cycles (57,926 or 58,744); the part of a line left
; over carries to the next call (t_rem). While it waits it reads port $DD
; through the runtime now and then, so that the once-a-frame work (tile
; conversion, map rebuild) runs on time inside the wait and not at the
; display-on write after the load. The wait keeps the game's interrupt
; state. Changes AF, BC, DE, HL.
smswait:
        call sadd
        jp swait
; sadd: A:HL = Master System cycles: adds them to t_bud (as smswait) and
; returns without waiting. Changes AF, BC, DE, HL.
sadd:   push ix
        ld ix,t_dv
        ld (ix+0),0             ; dividend = cycles x 256
        ld (ix+1),l
        ld (ix+2),h
        ld (ix+3),a
        ld hl,(t_rem)           ; + the remainder of the last call
        ld a,(ix+0)
        add a,l
        ld (ix+0),a
        ld a,(ix+1)
        adc a,h
        ld (ix+1),a
        ld a,(ix+2)
        adc a,0
        ld (ix+2),a
        ld a,(ix+3)
        adc a,0
        ld (ix+3),a
        ld a,$05
        call nrd
        and 4
        ld de,58744
        jr z,.dz
        ld de,57926
.dz:    ld hl,0
        ld b,32
.dv:    sla (ix+0)
        rl (ix+1)
        rl (ix+2)
        rl (ix+3)
        adc hl,hl
        jr c,.sb
        or a
        sbc hl,de
        jr nc,.q
        add hl,de
        jr .nx
.sb:    or a
        sbc hl,de
.q:     inc (ix+0)
.nx:    djnz .dv
        ld (t_rem),hl
        ld l,(ix+0)
        ld h,(ix+1)
        pop ix
        ld de,(t_bud)
        add hl,de
        ld (t_bud),hl
        ret
; swait: waits until t_el reaches t_bud. Changes AF, BC, DE, HL.
swait:  ld hl,(t_bud)
.w:     rst $00
        db $0F                  ; IN A,($DD): lets the once-a-frame work run
        call tick               ; HL = t_bud
        ld de,(t_el)
        push hl
        or a
        sbc hl,de
        pop hl
        jr z,.done
        jr nc,.w
.done:  ld hl,(t_el)
        ld (t_end),hl
        ret
; rd16: DE = the beam's Next line (0 to 310 at 50 Hz). Keeps the game's
; interrupt state. Changes AF.
rd16:   ld a,i
        push af
        di
.rd:    ld a,$1E
        call nrd
        ld d,a
        ld a,$1F
        call nrd
        ld e,a
        ld a,$1E
        call nrd
        cp d
        jr nz,.rd
        pop af
        ret po
        ei
        ret
t_cyc:  ds 3
pl_ret: dw 0
s408:   db 0
s40A:   db 0
s418:   db 0
s404:   db 0
s41F:   db 0
b_tab:  dw 0
b_422:  dw 0
b_428:  db 0
b_41b:  db 0
b_418:  db 0
t_s:    dw 0
t_el:   dw 0
b_01c:  db 0
d_h:    db 0
d_t:    db 0
d_u:    db 0
t_tgt:  dw 0
h_6b:   db 0
h_15:   db 0
h_4a:   db 0
t_dv:   ds 4
t_bud:  dw 0
t_end:  dw 0
t_fl:   dw 264
t_bg:   dw 0
t_c:    db 0
t_g:    db 0
t_ctc:  db 0
t_rem:  dw 0
endpage

# Psycho Fox (USA, Europe, Brazil).cht, "Infinite Lives": $0F33 DEC (HL) becomes DEC H
poke "Infinite lives"
gg 25F-33F-3BE
endpoke

# Psycho Fox (USA, Europe, Brazil).cht, "Start with ?? lives"
poke "Start lives"
gg ??E-F66-E66
endpoke

# Psycho Fox (USA, Europe) (Action Replay).cht, "Start As Hippo"
poke "Start as Hippo"
ar 00C0-1701
endpoke

# Psycho Fox (USA, Europe, Brazil).cht, "Level Select (Replace ?? With 00-14)"
poke "Start level"
ar 00C0-20??
endpoke

# Psycho Fox (USA, Europe, Brazil).cht, "Invulnerability"
poke "Invulnerability"
gg 019-9EE-A2E
endpoke
