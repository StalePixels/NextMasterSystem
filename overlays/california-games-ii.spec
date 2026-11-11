# California Games II (Europe), CRC32 C0E25D62, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s (random
# input), 120 s (no input) and 300 s of each event menu choice (random input after it),
# then decided by hand. Every I/O and mapper site in the logs is in the static scan.
#
# Decisions:
# - $0010-$0037 are free, so $10 is the io vector. The reference logs show no RST run.
# - Not patched: the debug monitor at $00B0-$02FF (it drives development hardware at
#   $8000-$8003). Its only reference is JP $00B0 at $0069, behind the NMI vector's
#   JP $040B, so it never runs.
# - Unlike California Games (Epyx), this is Probe's code: no routine is shared with
#   californiagames.spec.
name California Games II
cart C0E25D62
hz 50		; No-Intro region Europe
vector 10 io
# At a cold start the game counts loop passes between two frame interrupts ($05E0-$05FB)
# to tell a 50 Hz Master System (high byte of the count 7) from a 60 Hz one (6) and sets
# $C817 (1 at 60 Hz: the sound driver skips every seventh step). The Next counts far more
# passes and the loop never ends. The overlay runs at 50 Hz, so $C817 is 0.
asm 005E0 4   ; EI; LD HL,$0000
    xor a
    jp $0602
endasm
asm 004C1 2   ; IM 1 -> IM 2
    im 2
endasm
# The sound step at $114F keeps the slot 2 bank in $C726 while it maps bank 15
# ($1165-$118D). Both the frame handler ($1197) and the main loop ($5405 in
# snowboarding, among others) call it, the main loop with interrupts on. A frame
# interrupt inside the main loop's call runs the step again: the inner call saves bank 15
# in $C726, the outer call then restores bank 15, and the game runs bank 15 data as code
# (it stops in snowboarding). Here the step refuses to start again while it runs: the inner
# call returns at once and that frame has no sound step. sndbusy is set from the bank save
# to after the bank restore. The caves are in the unused $FF bytes after the JP at $0038.
label sndbusy 0003B
label sndin 0003C
label sndout 0004C
asm 0003B 1   ; unused $FF byte: sndbusy
    db 0
endasm
asm 0003C 16  ; unused $FF bytes: sndin, in place of LD A,($FFFF) at $1165
    ld a,(sndbusy)
    or a
    jr nz,.skip
    inc a
    ld (sndbusy),a
    ld a,($FFFF)
    ret
.skip:
    pop af              ; the return to $1168
    ret                 ; to the caller of $114F
endasm
asm 0004C 13  ; unused $FF bytes: sndout, in place of LD A,($C726) at $1188
    ld a,($C726)
    call $118B          ; LD ($FFFF),A (mapper site); RET
    push af
    xor a
    ld (sndbusy),a
    pop af
    ret
endasm
asm 01165 3   ; LD A,($FFFF)
    call sndin
endasm
asm 01188 3   ; LD A,($C726) (the restore at $118B and the RET follow)
    jp sndout
endasm
site 0044C   ; OUT ($3F),A
site 00496   ; OUT ($3F),A
site 004A9   ; OTIR
site 00574   ; OUT ($BF),A
site 0057B   ; OUT ($BF),A
site 0057F   ; OUT ($BF),A
site 00586   ; OUT ($BF),A
site 0058E   ; OUT ($BF),A
site 00595   ; OUT ($BF),A
site 0059B   ; OUTI
site 005B6   ; OUT (C),B
site 005C0   ; OUT ($3F),A
site 005C3   ; IN A,($DC)
site 00EC5   ; OUT ($BE),A
site 00ECB   ; OUT ($BE),A
site 00ED1   ; OUT ($BE),A
site 00ED6   ; OUT ($BE),A
site 00EE5   ; OUT ($BE),A
site 00EEA   ; OUT ($BE),A
site 00EEF   ; OUT ($BE),A
site 00EF4   ; OUT ($BE),A
site 00F00   ; OUT ($BE),A
site 00F06   ; OUT ($BE),A
site 00F0C   ; OUT ($BE),A
site 00F12   ; OUT ($BE),A
site 00F3B   ; OUT ($BE),A
site 00F4B   ; OUT ($BE),A
site 00F52   ; OUT ($BF),A
site 00F58   ; OUT ($BF),A
site 0102F   ; OUT ($BE),A
site 01034   ; OUT ($BE),A
site 01039   ; OUT ($BE),A
site 0103E   ; OUT ($BE),A
site 01055   ; OUT ($BE),A
site 0105A   ; OUT ($BE),A
site 0105F   ; OUT ($BE),A
site 01064   ; OUT ($BE),A
site 01070   ; OUT ($BE),A
site 01076   ; OUT ($BE),A
site 0107C   ; OUT ($BE),A
site 01082   ; OUT ($BE),A
site 010D1   ; OUT ($3F),A
site 010D5   ; IN A,($DD)
site 010ED   ; IN A,($BF)
site 01112   ; OUT ($3F),A
site 01116   ; IN A,($DD)
site 011DA   ; OUT ($BE),A
site 011DF   ; OUT ($BE),A
site 011FD   ; OUT ($BE),A
site 01202   ; OUT ($BE),A
site 01233   ; OUT ($BE),A
site 01239   ; OUT ($BE),A
site 01252   ; OUT ($BE),A
site 01258   ; OUT ($BE),A
site 01718   ; OUT (C),D
site 0171E   ; OUT (C),E
site 01724   ; OUT (C),H
site 0172A   ; OUT (C),L
site 01747   ; OUT ($BE),A
site 01750   ; OUT ($BE),A
site 01760   ; OUT ($BE),A
site 01765   ; OUT ($BE),A
site 0176A   ; OUT ($BE),A
site 0176E   ; OUT ($BE),A
site 01775   ; OUT ($BE),A
site 0177A   ; OUT ($BE),A
site 0177F   ; OUT ($BE),A
site 01784   ; OUT ($BE),A
site 02E04   ; OUT ($BF),A
site 02E0A   ; OUT ($BF),A
site 030EA   ; OUT ($BE),A
site 030EF   ; OUT ($BE),A
site 031A8   ; OUT ($BE),A
site 031AD   ; OUT ($BE),A
site 031B8   ; OUT ($BE),A
site 031BD   ; OUT ($BE),A
site 03845   ; OUT ($BE),A
site 0384B   ; OUT ($BE),A
site 03851   ; OUT ($BE),A
site 03857   ; OUT ($BE),A
site 03BC0   ; OUT ($BE),A
site 03BC6   ; OUT ($BE),A
site 03BE3   ; OUT ($BE),A
site 03BF1   ; OUT ($BE),A
site 03C93   ; OUT ($BE),A
site 03C99   ; OUT ($BE),A
site 03CCD   ; OUT ($BE),A
site 03CD3   ; OUT ($BE),A
site 04591   ; OUT ($BE),A
site 04599   ; OUT ($BE),A
site 045B7   ; OUT ($BE),A
site 045BF   ; OUT ($BE),A
site 04ADD   ; OUT ($BE),A
site 04AE7   ; OUT ($BE),A
site 04B2D   ; OUT ($BE),A
site 04B33   ; OUT ($BE),A
site 04B45   ; OUT ($BE),A
site 04B4C   ; OUT ($BE),A
site 04B9F   ; OUT ($BE),A
site 04BA5   ; OUT ($BE),A
site 04BC5   ; OUT ($BE),A
site 04BCB   ; OUT ($BE),A
site 04DFE   ; OUT ($BE),A
site 04E05   ; OUT ($BE),A
site 1121C   ; OUT ($BE),A
site 11222   ; OUT ($BE),A
site 1122B   ; OUT ($BE),A
site 11231   ; OUT ($BE),A
site 11253   ; OUT ($BE),A
site 11259   ; OUT ($BE),A
site 1127E   ; OUT ($BE),A
site 11283   ; OUT ($BE),A
site 11289   ; OUT ($BE),A
site 1128E   ; OUT ($BE),A
site 11294   ; OUT ($BE),A
site 11299   ; OUT ($BE),A
site 1129F   ; OUT ($BE),A
site 112A4   ; OUT ($BE),A
site 112CA   ; OUT ($BE),A
site 112D0   ; OUT ($BE),A
site 112D4   ; OUT ($BE),A
site 112DA   ; OUT ($BE),A
site 112DE   ; OUT ($BE),A
site 112E4   ; OUT ($BE),A
site 112E8   ; OUT ($BE),A
site 112EE   ; OUT ($BE),A
site 1130F   ; OUT ($BE),A
site 11315   ; OUT ($BE),A
site 139A1   ; OUT ($BE),A
site 139A9   ; OUT ($BE),A
site 1FBFC   ; OUT ($BE),A
site 1FD88   ; OUT ($BE),A
site 1FDB7   ; OUT ($BE),A
site 301E9   ; OUT ($BE),A
site 301EF   ; OUT ($BE),A
site 3022E   ; OUT ($BE),A
site 30234   ; OUT ($BE),A
site 3023F   ; OUT ($BE),A
site 30245   ; OUT ($BE),A
site 32D2C   ; OUT ($BE),A
site 32D32   ; OUT ($BE),A
site 32D39   ; OUT ($BE),A
site 32D40   ; OUT ($BE),A
site 3C067   ; OUT ($7F),A
site 3C07D   ; OUT ($7F),A
site 3C094   ; OUT ($7F),A
site 3C0A7   ; OUT ($7F),A
mapldk 004C4   # LD HL,$FFFC; LD (HL),$00
maphl 004CA   # LD (HL),$00, HL = $FFFD
maphl 004CD   # LD (HL),$01, HL = $FFFE
maphl 004D0   # LD (HL),$02, HL = $FFFF
mapst 00628   ; LD ($FFFF),A
mapst 00659   ; LD ($FFFF),A
mapst 0066E   ; LD ($FFFF),A
mapst 007CB   ; LD ($FFFF),A
mapst 007D3   ; LD ($FFFF),A
mapst 007DB   ; LD ($FFFF),A
mapst 00D00   ; LD ($FFFF),A
mapst 00D1B   ; LD ($FFFF),A
mapst 0116D   ; LD ($FFFF),A
mapst 0118B   ; LD ($FFFF),A
mapst 012B4   ; LD ($FFFF),A
mapst 012C4   ; LD ($FFFF),A
mapst 01332   ; LD ($FFFF),A
mapst 01345   ; LD ($FFFF),A
mapst 01359   ; LD ($FFFF),A
mapst 01393   ; LD ($FFFF),A
mapst 013A2   ; LD ($FFFF),A
mapst 01796   ; LD ($FFFF),A
mapst 017B0   ; LD ($FFFF),A
mapst 017CC   ; LD ($FFFF),A
mapst 023B2   ; LD ($FFFF),A
mapst 02567   ; LD ($FFFF),A
mapst 0257F   ; LD ($FFFF),A
mapst 02742   ; LD ($FFFF),A
mapst 0275B   ; LD ($FFFF),A
mapst 02800   ; LD ($FFFF),A
mapst 02951   ; LD ($FFFF),A
mapst 02959   ; LD ($FFFF),A
mapst 0297E   ; LD ($FFFF),A
mapst 02B66   ; LD ($FFFF),A
mapst 02B7F   ; LD ($FFFF),A
mapst 02BD1   ; LD ($FFFF),A
mapst 02E34   ; LD ($FFFF),A
mapst 02E4B   ; LD ($FFFF),A
mapst 033C1   ; LD ($FFFF),A
mapst 033C9   ; LD ($FFFF),A
mapst 034E4   ; LD ($FFFF),A
mapst 034FD   ; LD ($FFFF),A
mapst 03726   ; LD ($FFFF),A
mapst 0373E   ; LD ($FFFF),A
mapst 03E42   ; LD ($FFFF),A
mapst 03FBE   ; LD ($FFFF),A
mapst 03FC6   ; LD ($FFFF),A
mapst 04422   ; LD ($FFFF),A
mapst 0443A   ; LD ($FFFF),A
mapst 0478B   ; LD ($FFFF),A
mapst 04793   ; LD ($FFFF),A
mapst 04797   ; LD ($FFFF),A
mapst 0479F   ; LD ($FFFF),A
mapst 047A3   ; LD ($FFFF),A
mapst 047AD   ; LD ($FFFF),A
mapst 04C09   ; LD ($FFFF),A
mapst 04D83   ; LD ($FFFF),A
mapst 04D8C   ; LD ($FFFF),A
mapst 04DBE   ; LD ($FFFF),A
mapst 04DD6   ; LD ($FFFF),A
mapst 04E6A   ; LD ($FFFF),A
mapst 04EB2   ; LD ($FFFF),A
mapst 04EDD   ; LD ($FFFF),A
mapst 04EEE   ; LD ($FFFF),A
mapst 04F08   ; LD ($FFFF),A
mapst 04F20   ; LD ($FFFF),A
mapst 04F28   ; LD ($FFFF),A
mapst 04F46   ; LD ($FFFF),A
mapst 05022   ; LD ($FFFF),A
mapst 0503C   ; LD ($FFFF),A
mapst 05078   ; LD ($FFFF),A
mapst 050E9   ; LD ($FFFF),A
mapst 0510D   ; LD ($FFFF),A
mapst 052F0   ; LD ($FFFF),A
mapst 0531D   ; LD ($FFFF),A

# The name table decoder at $3C71 (bank 0): HL = a stream of cells (a tile byte, then an
# attribute byte; with bit 7 of the second byte set, its low 7 bits count a run of the cell,
# with the attribute in a third byte; tile $12 leaves the cell as it is; $FF $FF ends it),
# written from HL' in rows of 16 cells with the step DE' after each row, IXH rows. The
# event menu runs it for rows 0-14 of the whole width each time the man on it changes pose
# ($BB28-$BB94, bank 4), then draws the man's halves ($9267, $92B5) and the icons over it.
# Through the runtime each cell is two traps; the menu then showed the plain background,
# without the icons and half of the man, in almost every frame. Page 0 entry bg writes
# each run of cells with jt_vwrite.
asm 03C71 5   ; LD IXL,$10; LD A,(HL); CP $FF (the loop at $3C74 is inside the routine)
    rst $10
    db far_io, pg_bg, ent_bg
    ret
endasm

# The rows of sea and sand behind the man on the event menu: $9267 (bank 4) writes rows 4-14
# of the left half from $3900, $92B5 the right half from $3920 as its mirror (the cells in
# the other order with the H flip bit). Each row is one 4-cell pattern of 8 source bytes
# (high byte first) written 4 times; the menu runs one of them in the frame after each
# decode at $3C71. Through the runtime they ran into the picture with the decode, and the
# icons showed half drawn. Page 0 entries sea_l and sea_r write the 11 rows with one
# jt_vwrite call.
asm 11267 5   ; EXX; LD HL,$3900; LD DE,$0040 (CALL $0F50 follows)
    rst $10
    db far_io, pg_sea_l, ent_sea_l
    ret
endasm
asm 112B5 5   ; EXX; LD HL,$3920; LD DE,$0040 (CALL $0F50 follows)
    rst $10
    db far_io, pg_sea_r, ent_sea_r
    ret
endasm

# The event icons on the menu: $91E9 (bank 4) draws an icon's frame and $924B its picture,
# 4x4 cells. The menu draws two icons each frame, before the half of the background at
# $3C71. Through the runtime they were about 190 traps a frame. In the frame where the man
# changes pose, the work then ran past the frame event: the game missed a frame and showed
# a whole picture with the new background over the icons, before it drew them again. Page
# 0 entries box and pic write the cells with jt_vwrite.
asm 111E9 5   ; CALL $9216; EXX; ADD HL,DE (the loop at $91F4 is inside the routine)
    rst $10
    db far_io, pg_box, ent_box
    ret
endasm
asm 1124B 5   ; LD C,$04; LD B,$04; LD A,(HL) (the loops at $924D and $924F are inside the routine)
    rst $10
    db far_io, pg_pic, ent_pic
    ret
endasm

# Hang gliding redraws the whole name table from a map in RAM 98 cells wide: $30D3 (bank 0,
# from bank 7 $BA5C and $BCD5) writes 24 rows of 32 cells from ($C222); $318E (from bank 7
# $BCD0) writes the same rows turned by one cell (each row's cell 31 first, then cells
# 0-30). Through the runtime each call cost about 880,000 cycles, more than a frame, and
# play ran at 100-130% of the frame. Page 0 entries full and rot write the rows with
# jt_vwrite.
asm 030D3 5   ; EXX; LD HL,$3800; LD DE,... (the loop at $30E6 is inside the routine)
    rst $10
    db far_io, pg_full, ent_full
    ret
endasm
asm 0318E 5   ; EXX; LD DE,$3800; CALL ... (the loop at $31A5 is inside the routine)
    rst $10
    db far_io, pg_rot, ent_rot
    ret
endasm

# The sprite pattern streamer at $0DCB (bank 0) writes each sprite's patterns into VRAM
# every frame: a run of 4-byte rows from the sprite's data, forward ($0EDF) or turned
# upside down ($0EAC), then H' rows of zeros ($0EFF), and at the end the sprite table from
# $C000 ($0F2A). In hang gliding it ran to about 270,000 cycles a frame through the
# runtime, and play frames reached 148%. $1011 and $104B are the same for a sprite turned
# left to right: each byte goes through the table at $0300 (bank 0) first. Page 0 entries
# sprf, sprv, shf and shv write a sprite's rows and zero rows, sat the sprite table, each
# with jt_vwrite.
asm 00EAC 7   ; LD A,B; ADD A; ADD A; PUSH HL; LD L,A; LD H,$00 (the flipped rows, to $0EDD)
    rst $10
    db far_io, pg_sprv, ent_sprv
    jp $0F18
endasm
asm 00EDF 6   ; CALL $0F50; INC DE; LD A,(DE); INC DE (the forward rows, to $0EF7)
    rst $10
    db far_io, pg_sprf, ent_sprf
    jr $0F18
endasm
asm 0104B 6   ; CALL $0F50; INC DE; LD H,$03 (the forward rows through the table, to $1066)
    rst $10
    db far_io, pg_shf, ent_shf
    jr $1088
endasm
asm 01011 7   ; LD A,B; ADD A; ADD A; PUSH HL; LD L,A; LD H,$00 (the rows last first through
              ; the table, to $1049)
    rst $10
    db far_io, pg_shv, ent_shv
    jp $1088
endasm
asm 00F2E 5   ; LD HL,$3F00; CALL ... (the sprite table, to the RET at $0F4F)
    rst $10
    db far_io, pg_sat, ent_sat
    ret
endasm

# The frame handler redraws the skateboarding view each frame from $119D (bank 0): the
# same cell stream as $3C71, in rows of 20 cells from $38C2 to the $FF $FF end mark, the
# first IXH rows (11, or 6 at 60 Hz) with 2 NOPs between a cell's two writes and the rest
# with 3. Through the runtime each cell is two traps, about 90 cells a frame, and play
# frames ran past the frame. Page 0 entry pipe writes the cells with jt_vwrite.
asm 011BE 5   ; LD A,(HL); CP $FF (JP NZ,$11CA follows; the loop at $11BE is inside the routine)
    rst $10
    db far_io, pg_pipe, ent_pipe
    ret
endasm

# Page 0 uses these runtime internals: jt_vwrite, jt_peek, vdp_addr $E037, vdp_code $E036,
# vdp_latch $E035, vdp_rbuf $E039.
page 0 bg sea_l sea_r pipe box pic full rot sprf sprv shf shv sat
; bg: the decoder at $3C71. In: HL = the stream, HL' = the VRAM address of the first
; cell, DE' = the step after each row of 16 cells, IXH = the rows. Out, as the routine
; leaves them: HL past the stream (on the second $FF of the end mark), HL' the next cell's
; address, IXH and IXL the rows and cells left, Z set, the VDP address where the game's
; writes leave it. The game's $0F50 (DI, the VDP address, EI unless $C739 is set) runs
; at each skipped cell, each row end and each run end; so interrupts end as $0F50 leaves
; them, or as they were if it never ran. The page runs with interrupts off on its own stack.
bg:     ld ixl,16               ; as LD IXL,$10 at $3C71
        ld a,16
        ld (width),a
        ld a,1
        ld (doskip),a
        ld (rstop),a
        jr dec
; pipe: the decoder at $11BE. The same stream with rows of 20 cells (IXL), no skipped
; tile, and no stop on the rows: IXH counts the rows written with the faster code (2 NOPs
; between the two writes of a cell, for the blank) and stays at 0 after them; the stream
; ends only at $FF $FF. Out as bg, with A = $FF.
pipe:   ld a,20
        ld (width),a
        xor a                   ; no tile is skipped
        ld (doskip),a
        ld (rstop),a
dec:    ld a,i                  ; P/V = the interrupt state at the entry
        di
        ld a,0
        jp po,.iff0
        inc a
.iff0:  ld (iff),a
        ld (sv_sp),sp
        ld sp,stk_top
        push bc
        push de
        exx
        ld (vaddr),hl
        ld (rstep),de
        exx
        ld (sptr),hl
        ld a,ixh
        ld (rows),a
        ld a,ixl
        ld (col),a
        ld hl,(vdp_addr)
        ld (vcur),hl
        xor a
        ld (did),a
        ld (seglen),a
        ld a,(vdp_rbuf)
        ld (rbuf),a
.loop:  ld hl,(sptr)
        call getb
        cp $FF
        jr nz,.cell
        inc hl
        call getb
        cp $FF
        jp z,.term
        dec hl
.cell:  call getb
        ld (tile),a
        inc hl
        call getb
        inc hl
        bit 7,a
        jr z,.single
        and $7F
        ld b,a                  ; 0 runs 256 times, as DJNZ does
        call getb
        inc hl
        ld (attr),a
        ld (sptr),hl
.run:   push bc
        call skipq
        call nz,put             ; a skipped cell in a run leaves the VDP address
        call step2
        ld hl,col
        dec (hl)
        jr nz,.rnext
        call rowend
        jr z,.rret
        ld a,(width)
        ld (col),a
.rnext: pop bc
        djnz .run
        ld a,(doskip)           ; bg sets the VDP address at a run's end; pipe does not
        or a
        jp z,.loop
        ld hl,(vaddr)
        call f50
        jp .loop
.rret:  pop bc
        jr .out
.single:
        ld (attr),a
        ld (sptr),hl
        call skipq
        jr z,.skip
        call put
        call step2
        jr .cnext
.skip:  call step2
        ld hl,(vaddr)
        call f50
.cnext: ld hl,col
        dec (hl)
        jp nz,.loop
        call rowend
        jr z,.out
        ld a,(width)
        ld (col),a
        jp .loop
.term:  ld (sptr),hl
.out:   call flush
        ld hl,(vcur)
        res 6,h
        res 7,h
        ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld a,(rbuf)
        ld (vdp_rbuf),a
        ld a,(rows)
        ld ixh,a
        ld a,(col)
        ld ixl,a
        exx
        ld hl,(vaddr)
        exx
        ld hl,(sptr)
        pop de
        pop bc
        ld sp,(sv_sp)
        ld a,(did)
        or a
        jr z,.asin
        ld a,($C739)            ; $0F50 leaves interrupts off when $C739 is set
        or a
        jr nz,.off
.on:    xor a                   ; Z set, as the routine's RET Z
        ei
        ret
.asin:  ld a,(iff)              ; $0F50 never ran: interrupts as at the entry
        or a
        jr nz,.on
.off:   xor a
        ret
; (pipe's callers do not read A; bg and pipe both return A = 0 and Z set)
; sea_l, sea_r: the routines at $9267 and $92B5. In: HL = the source, 11 rows of 8 bytes
; (sea_l: from HL; sea_r: from HL, read backwards from HL + 8). Out, as the routines leave
; them: HL past the 11 rows (sea_r: plus 8), HL' = the start + 11 rows of $40, DE' = $40,
; DE = 8, BC = 0, A = ($C739), Z set, the VDP address at HL' as the last $0F50 leaves
; it, and interrupts as $0F50 leaves them (off when $C739 is set).
sea_l:  xor a
        jr sea
sea_r:  ld a,1
sea:    di
        ld (sv_sp),sp
        ld sp,stk_top
        push iy
        ld (mirror),a
        ld de,buf
        ld c,11
.row:   ld b,4
.rep:   push hl
        ld a,(mirror)
        or a
        jr nz,.mir
        ld a,4
.fw:    ex af,af'
        inc hl
        call getb
        ld (de),a               ; the low byte: the second source byte
        inc de
        dec hl
        call getb
        ld (de),a
        inc de
        inc hl
        inc hl
        ex af,af'
        dec a
        jr nz,.fw
        jr .next
.mir:   ld a,4
.bk:    ex af,af'
        dec hl
        call getb
        ld (de),a
        inc de
        dec hl
        call getb
        or 2
        ld (de),a
        inc de
        ex af,af'
        dec a
        jr nz,.bk
.next:  pop hl
        djnz .rep
        push de
        ld de,8
        add hl,de
        pop de
        dec c
        jr nz,.row
        push hl
        ld a,(mirror)
        or a
        ld de,$3900
        jr z,.ad
        ld de,$3920
.ad:    push de
        ld hl,buf
        ld b,32
        ld c,11
        ld ix,32
        ld iy,$40
        ld a,1
        call jt_vwrite
        pop hl
        ld de,11*$40
        add hl,de               ; the start + 11 rows: HL' and the VDP address
        ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld a,h
        add a,$40
        ld (vdp_rbuf),a
        push hl
        exx
        pop hl
        ld de,$40
        exx
        pop hl                  ; the source past the rows
        pop iy
        ld de,8
        ld bc,0
        ld sp,(sv_sp)
        ld a,($C739)            ; A as $0F50 leaves it; interrupts off when $C739 is set
        or a
        jr nz,.off
        ei
.off:   cp a                    ; Z set, as after the last DEC C
        ret
; box: the routine at $91E9, an icon's frame: a row of 6 cells, then 4 rows of a left cell
; and a right cell 10 bytes after it (the same 2 cells in each row), then a row of 6 cells.
; In: HL = the 14 cells (attribute byte first), HL' = the address of the top row (the VDP
; address is there), DE' = the step to the second row. Out, as the routine leaves them: HL
; past the cells, HL' = the bottom row's address, DE' as it was, BC' = $36, B = 0, A = the
; last cell's attribute, A' its tile, the VDP address past the bottom row.
; pic: the routine at $924B, an icon's picture: 4 rows of 4 cells. In: HL = the 16 cells,
; HL' = the first row's address (the VDP address is there), DE' = the row step. Out: HL
; past the cells, HL' = the start + 4 row steps, BC = 0, A = ($C739), Z set, A' the last
; cell's tile, the VDP address at HL'.
; Both: interrupts as the game's last $0F50 leaves them (off when $C739 is set).
box:    ld a,1
        jr icon
pic:    xor a
icon:   di
        ld (sv_sp),sp
        ld sp,stk_top
        push ix
        push iy
        push bc
        push de
        ld (kind),a
        ld (sptr),hl
        exx
        ld (vaddr),hl
        ld (rstep),de
        ld (bcs),bc
        exx
        ld hl,(vdp_addr)
        ld (vcur),hl
        xor a
        ld (seglen),a
        ld a,(vdp_rbuf)
        ld (rbuf),a
        ld a,(kind)
        or a
        jr z,.pic
        ld b,6
        call cells
        call nrow
        ld b,4
.side:  push bc
        ld b,1
        call cells
        ld de,$0A
        call vstep
        ld hl,(vaddr)
        ld de,$36
        add hl,de
        ld (vaddr),hl
        ld b,1
        call cells
        ld hl,(vaddr)
        call f50
        ld hl,(sptr)
        ld de,-4
        add hl,de
        ld (sptr),hl
        pop bc
        djnz .side
        ld hl,(sptr)
        ld de,4
        add hl,de
        ld (sptr),hl
        ld b,6
        call cells
        ld hl,$36
        ld (bcs),hl
        jr .out
.pic:   ld c,4
.prow:  push bc
        ld b,4
        call cells
        call nrow
        pop bc
        dec c
        jr nz,.prow
.out:   call flush
        ld hl,(vcur)
        res 6,h
        res 7,h
        ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld a,(rbuf)
        ld (vdp_rbuf),a
        exx
        ld hl,(vaddr)
        ld de,(rstep)
        ld bc,(bcs)
        exx
        ld a,(tile)
        ex af,af'
        ld hl,(sptr)
        pop de
        pop bc
        pop iy
        pop ix
        ld a,(kind)
        or a
        jr z,.pend
        ld b,0
        ld a,($C739)
        or a
        ld a,(attr)             ; A as the routine leaves it; the flags tell $C739
        ld sp,(sv_sp)
        ret nz                  ; $0F50 leaves interrupts off when $C739 is set
        ei
        ret
.pend:  ld bc,0
        ld a,($C739)
        or a
        ld sp,(sv_sp)
        jr nz,.poff
        ei
.poff:  cp a                    ; Z set, as after the last DEC C
        ret
; B cells from sptr (attribute byte first) to the VDP address vcur
cells:  ld hl,(sptr)
        call getb
        ld (attr),a
        inc hl
        call getb
        ld (tile),a
        inc hl
        ld (sptr),hl
        push bc
        call put
        pop bc
        djnz cells
        ret
; HL' += DE' (nrow) or DE (vstep), then $0F50 with it
nrow:   ld de,(rstep)
vstep:  ld hl,(vaddr)
        add hl,de
        ld (vaddr),hl
        jp f50
; full: the routine at $30D3, the name table from the map at ($C222): 24 rows of 64 bytes,
; $C4 bytes apart in the map. Out, as the routine leaves them: HL = the map + 24 * $C4,
; DE = $84, BC = 0, HL' = $3E00, DE' = $40, A = ($C739), Z set, the VDP address at $3E00,
; interrupts as $0F50 leaves them (off when $C739 is set).
; rot: the routine at $318E, the same rows turned by one cell: VRAM cell 0 of each row from
; map cell 31, cells 1-31 from map cells 0-30. Out: HL = the map + 24 * $C4, DE = $86,
; BC = 0, HL' = the map + $3E + 24 * $C4, DE' = $3E00, BC' = $40, A = $7E, Z set, the VDP
; address at $3E00, interrupts as at the entry ($2E03 does not change them).
full:   xor a
        jr nmap
rot:    ld a,1
nmap:   ld (kind),a
        ld a,i                  ; P/V = the interrupt state at the entry
        di
        ld a,0
        jp po,.i0
        inc a
.i0:    ld (iff),a
        ld (sv_sp),sp
        ld sp,stk_top
        push ix
        push iy
        ex af,af'
        push af
        ld hl,($C222)
        ld (sptr),hl
        ld ix,$C4
        ld iy,$40
        ld a,(kind)
        or a
        jr nz,.rot
        ld de,$3800
        ld bc,$4018             ; 24 runs of 64 bytes
        call jt_vwrite          ; A = 0: the map as the game sees it
        jr .done
.rot:   ld de,$3E
        add hl,de
        ld de,$3800
        ld bc,$0218             ; cell 31 of each row into cell 0
        xor a
        call jt_vwrite
        ld hl,(sptr)
        ld de,$3802
        ld bc,$3E18             ; cells 0-30 into cells 1-31
        ld ix,$C4
        ld iy,$40
        xor a
        call jt_vwrite
.done:  ld a,$7E                ; the last control byte: $3E00 + $4000, high byte
        ld (vdp_rbuf),a
        pop af
        ex af,af'
        pop iy
        pop ix
        ld hl,(sptr)
        ld de,24*$C4
        add hl,de
        ld bc,0
        ld a,(kind)
        or a
        jr nz,.rout
        exx
        ld hl,$3E00
        ld de,$40
        exx
        ld de,$84
        ld a,($C739)
        or a
        ld sp,(sv_sp)
        jr nz,.off
        ei
.off:   cp a                    ; Z set, as after the last DEC C
        ret
.rout:  push hl
        exx
        pop hl
        ld de,$3E
        add hl,de
        ld de,$3E00
        ld bc,$40
        exx
        ld de,$86
        ld a,(iff)
        or a
        ld a,$7E
        ld sp,(sv_sp)
        jr z,.off
        ei
        cp a
        ret
; sprf, sprv, shf, shv: a sprite's rows, then its zero rows ($0EF9-$0F16, $1069-$1086).
; sprf: forward ($0EDF); sprv: last row first ($0EAC); shf: forward, each byte through the
; table at $0300 (left-right flip, $104B); shv: last row first through the table ($1011).
; In: HL = the VRAM address, DE = the sprite's data (the rows start at DE + 1, 4 bytes
; each), B = the rows (0 is 256), H' = the zero rows. They return to the EXX at $0F18
; (sprf, sprv) or $1088 (shf, shv) with the registers as the game has them there: the
; current set is the game's second set, with B' = 0, A = 0 and Z set; in the first set
; DE = the data + 4 * rows + 1; HL = the VRAM address (sprf), the data - 3 (sprv, shv) or
; $0300 + the last row's last byte (shf); B = 0 and C as it was, or BC = $FFF9 (shv). The
; VDP address is after the last row, and interrupts are as $0F50 leaves them.
sprf:   xor a
        jr spr
sprv:   ld a,1
        jr spr
shf:    ld a,2
        jr spr
shv:    ld a,3
spr:    ld (kind),a
        di
        ld (sv_sp),sp
        ld sp,stk_top
        push ix
        push iy
        ex af,af'
        push af
        ex af,af'
        push bc
        exx
        push bc
        push de
        push hl
        ld a,h
        exx
        ld (col),a              ; the zero rows
        ld (vaddr),hl
        ld (sptr),de
        ld a,b
        ld (rows),a
        ld de,(vaddr)
        ld a,(kind)
        or a
        jr nz,.cpy
        call r4                 ; forward, no table: straight from the data
        ld hl,(sptr)
        inc hl
        xor a                   ; the data as the game sees it
        ld (vrmod),a
        inc a
        ld (vrstp),a
        call vrun
        jp .zr
.cpy:   ld hl,(sptr)            ; the first row to write
        inc hl
        ld a,(kind)
        rrca
        call c,last
        ld (rptr),hl
        ld a,(rows)
        ld (rleft),a
.chunk: ld a,(rleft)            ; up to 64 rows into buf
        or a
        jr z,.c64
        cp 65
        jr c,.cn
.c64:   ld a,64
.cn:    ld (rn),a
        ld b,a
        ld hl,(rptr)
        ld de,buf
.crow:  push bc
        ld b,4
.cb:    call getb
        push af
        ld a,(kind)
        and 2
        jr z,.nt
        pop af
        push hl
        ld l,a
        ld h,$03                ; the table at $0300
        call getb
        pop hl
        push af
.nt:    pop af
        ld (de),a
        inc hl
        inc de
        djnz .cb
        ld a,(kind)
        rrca
        jr nc,.nx
        ld bc,-8                ; last row first: back to the row before
        add hl,bc
.nx:    pop bc
        djnz .crow
        ld (rptr),hl
        ld a,(rn)
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        ld b,h
        ld c,l
        ld hl,buf
        ld de,(vdp_addr)
        ld a,(rleft)            ; the first piece starts at the sprite's address
        ld e,a
        ld a,(rows)
        cp e
        ld de,(vdp_addr)
        jr nz,.nf
        ld de,(vaddr)
.nf:    ld a,1                  ; buf is in this page
        ld (vrmod),a
        ld (vrstp),a
        call vrun
        ld a,(rn)
        ld e,a
        ld a,(rleft)
        sub e
        ld (rleft),a
        jr nz,.chunk
.zr:    ld a,(col)
        or a
        jr z,.nz
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        ld b,h
        ld c,l
        ld hl,zero4
        ld de,(vdp_addr)
        ld a,1                  ; zero4 is in this page
        ld (vrmod),a
        xor a
        ld (vrstp),a
        call vrun
.nz:    exx
        pop hl
        pop de
        pop bc
        ld b,0
        exx
        pop bc
        ld b,0
        pop af
        ex af,af'
        pop iy
        pop ix
        call r4
        ld hl,(sptr)
        add hl,bc
        inc hl
        ex de,hl                ; DE = the data + 4 * rows + 1
        ld a,(kind)
        or a
        ld hl,(vaddr)
        jr z,.hl
        cp 2
        jr nz,.h3
        dec de                  ; shf: $0300 + the last byte read
        ld a,(de)
        ld l,a
        ld h,$03
        inc de
        jr .hl
.h3:    ld hl,(sptr)
        dec hl
        dec hl
        dec hl
        cp 3
        jr nz,.hl
        ld bc,$FFF9
.hl:    ld a,(kind)             ; keep C (B is 0) unless shv
        cp 3
        jr z,.hl2
        ld b,0
.hl2:   exx                     ; the game's second set is current at the EXX
        ld a,($C739)
        or a
        ld sp,(sv_sp)
        jr nz,.off
        ei
.off:   xor a
        ret
; BC = 4 * rows (rows 0 is 256)
r4:     ld a,(rows)
        ld c,a
        ld b,0
        or a
        jr nz,.n
        inc b
.n:     sla c
        rl b
        sla c
        rl b
        ret
; HL = the last row of the sprite at sptr: sptr + 1 + 4 * (rows - 1)
last:   ld a,(rows)
        dec a
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        ld de,(sptr)
        add hl,de
        inc hl
        ret
; vrun: BC bytes (BC > 0) from HL into VRAM at DE, 256 at most in each jt_vwrite call, in
; its one-byte form (runs of one byte; the runtime takes its general path for bytes outside
; the tiles). vrstp = the source step (0 or 1), vrmod = jt_vwrite's A.
vrun:   ld a,b
        or a
        ld a,c
        jr z,.go
        xor a                   ; 256 bytes
.go:    push bc
        push af
        ld c,a
        ld b,1
        ld a,(vrstp)
        ld ixl,a
        ld ixh,0
        ld iy,1
        ld a,(vrmod)
        call jt_vwrite
        pop af                  ; the bytes written (0 is 256)
        pop bc
        ld de,(vdp_addr)
        push af
        ld a,(vrstp)
        or a
        jr z,.ns
        pop af
        push af
        or a
        jr nz,.a8
        inc h
        jr .ns
.a8:    add a,l
        ld l,a
        jr nc,.ns
        inc h
.ns:    pop af
        push hl
        ld l,a
        ld h,0
        or a
        jr nz,.sb
        inc h
.sb:    ld a,c
        sub l
        ld c,a
        ld a,b
        sbc a,h
        ld b,a
        pop hl
        or c
        jr nz,vrun
        ret
vrstp:  db 0
vrmod:  db 0
rptr:   dw 0
rleft:  db 0
rn:     db 0
; sat: the sprite table at $0F2E: $3F00-$3F3F from $C000 (through ybuf, where sbhide moves
; the sprites the snowboarding slope covers), $3F80-$3FFF from $C040. Out, as the
; routine leaves them: HL = $C0C0, DE = $3F80, B = 0, A = ($C0BF), the flags of
; AND ($C739), the VDP address at $0000 (after $3FFF), interrupts as $0F50 leaves them.
sat:    di
        ld (sv_sp),sp
        ld sp,stk_top
        push ix
        push iy
        push bc
        ex af,af'
        push af
        ld hl,$C000
        ld de,ybuf
        ld bc,$40
        ldir
        ld a,($DFFF)            ; the slot 2 bank: 9 in snowboarding
        cp 9
        call z,sbhide
        ld hl,ybuf
        ld de,$3F00
        ld bc,$4001
        ld ix,$40
        ld iy,$40
        ld a,1                  ; the source is this page
        call jt_vwrite
        ld hl,$C040
        ld de,$3F80
        ld bc,$8001
        ld ix,$80
        ld iy,$80
        xor a
        call jt_vwrite
        pop af
        ex af,af'
        pop bc
        pop iy
        pop ix
        ld hl,$C0C0
        ld de,$3F80
        ld b,0
        ld a,($C739)
        or a
        ld a,($C0BF)
        ld sp,(sv_sp)
        ret nz                  ; $0F50 leaves interrupts off when $C739 is set
        ei
        ret
zero4:  db 0,0,0,0
; sbhide: snowboarding draws the bridge at the bottom left with sprites from X 240 (X -16
; meant). sat calls it when the slot 2 bank is 9 ($DFFF, the RAM copy of the last mapper
; write), the snowboarding graphics bank. On the Master System the sprites at X 240-255 fall on slope cells with the
; priority bit at the right edge (columns 28-31 from about line 144) and do not show. The
; overlay runs without `priority`, so a sprite at X 240 or more with its top at line 145 or
; below gets Y $E0 (below the picture) in the copy in ybuf. Stops at the $D0 end mark.
sbhide: ld hl,ybuf
        ld de,$C040
        ld b,64
.next:  ld a,(hl)
        cp $D0
        ret z
        cp $90
        jr c,.skip
        ld a,(de)
        cp $F0
        jr c,.skip
        ld (hl),$E0
.skip:  inc hl
        inc de
        inc de
        djnz .next
        ret
ybuf:   ds 64
; HL' += 2 (bg: the game's INC HL; INC HL on the shadow address; pipe keeps HL' at the
; row start)
step2:  ld a,(doskip)
        or a
        ret z
        ld hl,(vaddr)
        inc hl
        inc hl
        ld (vaddr),hl
        ret
; the row end: HL' += DE', $0F50, IXH - 1 (not below 0). Z set when bg has no rows left;
; pipe never stops here.
rowend: ld hl,(vaddr)
        ld de,(rstep)
        add hl,de
        ld (vaddr),hl
        call f50
        ld hl,rows
        ld a,(hl)
        or a
        jr z,.zero
        dec (hl)
.zero:  ld a,(rstop)
        or a
        jr nz,.bg
        inc a                   ; NZ: pipe goes on past the rows
        ret
.bg:    ld a,(hl)
        or a                    ; Z: bg stops when no rows are left
        ret
; Z when the cell in tile is skipped: bg's tile $12
skipq:  ld a,(doskip)
        or a
        jr z,.no
        ld a,(tile)
        cp $12
        ret
.no:    inc a                   ; NZ
        ret
; $0F50 with HL: the VDP address becomes HL. The cells gathered so far are written first
; when HL does not follow them.
f50:    ld a,1
        ld (did),a
        ld a,h
        add a,$40
        ld (rbuf),a
        ld de,(vcur)
        or a
        sbc hl,de
        add hl,de
        ret z
        push hl
        call flush
        pop hl
        ld (vcur),hl
        ret
; put: the cell (tile, attr) goes to the VDP address vcur, gathered in buf.
put:    ld a,(seglen)
        or a
        jr nz,.add
        ld hl,(vcur)
        ld (segad),hl
.add:   ld e,a
        ld d,0
        ld hl,buf
        add hl,de
        ld a,(tile)
        ld (hl),a
        inc hl
        ld a,(attr)
        ld (hl),a
        ld (rbuf),a
        ld a,e
        add a,2
        ld (seglen),a
        ld hl,(vcur)
        inc hl
        inc hl
        ld (vcur),hl
        cp 254
        ret c
; flush: the gathered cells into VRAM with one jt_vwrite call.
flush:  ld a,(seglen)
        or a
        ret z
        push iy
        ld b,a
        ld c,1
        ld e,a
        ld d,0
        ld ix,de                ; one run: the steps only pick the write path
        ld iy,de
        ld hl,buf
        ld de,(segad)
        ld a,1                  ; the source is this page
        call jt_vwrite
        pop iy
        xor a
        ld (seglen),a
        ret
; A = the byte the game sees at HL
getb:   ld a,h
        and $E0
        cp $20
        jr z,.pk
        ld a,(hl)
        ret
.pk:    jp jt_peek
sv_sp:  dw 0
vaddr:  dw 0
rstep:  dw 0
sptr:   dw 0
vcur:   dw 0
segad:  dw 0
rows:   db 0
col:    db 0
tile:   db 0
attr:   db 0
did:    db 0
seglen: db 0
rbuf:   db 0
iff:    db 0
width:  db 0
doskip: db 0
rstop:  db 0
mirror: db 0
kind:   db 0
bcs:    dw 0
buf:    ds 11*32
        ds 64
stk_top:
endpage
