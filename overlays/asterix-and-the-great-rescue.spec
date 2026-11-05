# Asterix and the Great Rescue (Europe, Brazil) (En,Fr,De,Es,It), CRC32 F9B7D26B, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of the title
# (300 s, no input), random input (600 s), play (600 s, scripted) and the 60 s sweep.
# The logs ran no I/O or mapper site that the scan did not find.
# Code runs from banks 0 and 1 (slot 1 holds bank 1 whenever the foreground runs) and from the
# sound code in bank 22, which the frame handler calls at $91D6 with bank 21 in slot 1.
# The frame handler at $0038 calls the routine whose address is in $DFEE; the game sets it for
# each screen ($0705, $56DF, $5797, $5E82, $6520, $6DDB).
# Byte scan mapper stores patched (no path or recording reaches them): LD A,($C1FC) :
# LD ($FFFF),A and its EX AF,AF' : LD ($FFFF),A at $0A3A ... $2000 (the same form as $0807 and
# $087B, which the recordings ran), and three in bank 1 after LD A,n.
# Byte scan patterns judged not patched (verdicts in data/scan-verdicts.tsv): $0080-$00DF is a
# development stub that writes $FFFC and $FFFD, and $0184-$01AE (the high I/O patterns at
# $0188, $018F, $019F) and $58AB-$58EE in bank 1 (an older copy of the column writer at
# $58EF) are routines that nothing in the cart calls (unused); the I/O patterns in bank 22
# from $9B02 on are sound data after the sound code ($91D6-$965B); the rest are in banks that
# hold only graphics, maps and sound data (false).
name Asterix and the Great Rescue
cart F9B7D26B
hz 50		; No-Intro regions Europe, Brazil
# The tower walls are priority cells: at the tower door in round 1 a sprite goes behind the
# wall, and without the switch it shows over it.
priority
# No free RST vector: $0000-$0002 (IM 1; DI) becomes the vector, the game starts at $0003
# (the runtime does DI and IM 2).
vector 00 io
start 0003
site 00054   ; IN A,($BF)
site 00178   ; OUT ($BF),A
site 0017F   ; OUT ($BF),A
site 001B8   ; OUT (C),B
site 001CC   ; OUT ($BF),A
site 001D3   ; OUT ($BF),A
site 00228   ; OUT ($BE),A
site 0022D   ; OUT ($BE),A
site 00232   ; OUT ($BE),A
site 00237   ; OUT ($BE),A
site 0023C   ; OUT ($BE),A
site 00241   ; OUT ($BE),A
site 00246   ; OUT ($BE),A
site 0024B   ; OUT ($BE),A
site 00250   ; OUT ($BE),A
site 00255   ; OUT ($BE),A
site 0025A   ; OUT ($BE),A
site 0025F   ; OUT ($BE),A
site 00264   ; OUT ($BE),A
site 00269   ; OUT ($BE),A
site 0026E   ; OUT ($BE),A
site 00273   ; OUT ($BE),A
site 00278   ; OUT ($BE),A
site 0027D   ; OUT ($BE),A
site 00282   ; OUT ($BE),A
site 00287   ; OUT ($BE),A
site 0028C   ; OUT ($BE),A
site 00291   ; OUT ($BE),A
site 00296   ; OUT ($BE),A
site 0029B   ; OUT ($BE),A
site 002A0   ; OUT ($BE),A
site 002A5   ; OUT ($BE),A
site 002AA   ; OUT ($BE),A
site 002AF   ; OUT ($BE),A
site 002B4   ; OUT ($BE),A
site 002B9   ; OUT ($BE),A
site 002BE   ; OUT ($BE),A
site 002C3   ; OUT ($BE),A
site 002CD   ; OUT ($BF),A
site 002D2   ; OUT ($BF),A
site 002D5   ; OUT ($BE),A
site 002DE   ; OUT ($BF),A
site 002E5   ; OUT ($BF),A
site 002E8   ; OUTI
site 002FC   ; OUT ($BF),A
site 00302   ; OUT ($BF),A
site 00304   ; OTIR
site 003F1   ; OUT ($BF),A
site 003F7   ; OUT ($BF),A
site 0040B   ; OUT ($BF),A
site 00411   ; OUT ($BF),A
site 00416   ; OUTI
site 00418   ; OUTI
site 0041A   ; OUTI
site 0041C   ; OUTI
site 0041E   ; OUTI
site 00420   ; OUTI
site 00422   ; OUTI
site 00424   ; OUTI
site 00426   ; OUTI
site 00428   ; OUTI
site 0042A   ; OUTI
site 0042C   ; OUTI
site 0042E   ; OUTI
site 00430   ; OUTI
site 00432   ; OUTI
site 00434   ; OUTI
site 00440   ; OUT ($BF),A
site 00446   ; OUT ($BF),A
site 0044B   ; OUTI
site 0044D   ; OUTI
site 0044F   ; OUTI
site 00451   ; OUTI
site 00453   ; OUTI
site 00455   ; OUTI
site 00457   ; OUTI
site 00459   ; OUTI
site 0045B   ; OUTI
site 0045D   ; OUTI
site 0045F   ; OUTI
site 00461   ; OUTI
site 00463   ; OUTI
site 00465   ; OUTI
site 00467   ; OUTI
site 00469   ; OUTI
site 004AE   ; OUTI
site 00503   ; OUT ($BF),A
site 0050A   ; OUT ($BF),A
site 00512   ; IN A,($BE)
site 0051A   ; OUT ($BE),A
site 00590   ; OUT ($BE),A
site 0475D   ; OUT ($BF),A
site 04761   ; OUT ($BF),A
site 04780   ; OUT ($BF),A
site 04786   ; OUT ($BF),A
site 05710   ; IN A,($DC)
site 057BC   ; IN A,($DD)
site 057C1   ; IN A,($BF)
site 05DF8   ; IN A,($DC)
site 0656A   ; IN A,($DC)
site 06712   ; OUT ($BE),A
site 068D8   ; OUT ($BF),A
site 068DE   ; OUT ($BF),A
site 06DFC   ; IN A,($DC)
site 59468   ; OUT ($7F),A
site 5947F   ; OUT ($7F),A
site 59487   ; OUT ($7F),A
site 5948B   ; OUT ($7F),A
site 594D3   ; OUT ($7F),A
site 594DD   ; OUT ($7F),A
site 59529   ; OUT ($7F),A
site 5952D   ; OUT ($7F),A
site 59655   ; OUT ($7F),A
mapst 0000B   ; LD ($FFFC),A
mapst 0000E   ; LD ($FFFD),A
mapst 00012   ; LD ($FFFE),A
mapst 00016   ; LD ($FFFF),A
mapst 00051   ; LD ($FFFF),A
mapst 00103   ; LD ($FFFF),A
mapst 0013C   ; LD ($FFFF),A
mapst 0032A   ; LD ($FFFF),A
mapst 0070D   ; LD ($FFFE),A
mapst 00713   ; LD ($FFFE),A
mapst 00717   ; LD ($FFFF),A
mapst 00807   ; LD ($FFFF),A
mapst 0087B   ; LD ($FFFF),A
mapst 00CFD   ; LD ($FFFF),A
mapst 00D32   ; LD ($FFFF),A
mapst 00D98   ; LD ($FFFF),A
mapst 0112D   ; LD ($FFFF),A
mapst 01143   ; LD ($FFFF),A
mapst 018ED   ; LD ($FFFF),A
mapst 018F4   ; LD ($FFFF),A
mapst 02619   ; LD ($FFFF),A
mapst 0275C   ; LD ($FFFF),A
mapst 027EC   ; LD ($FFFF),A
mapst 02A7E   ; LD ($FFFF),A
mapst 02A85   ; LD ($FFFF),A
mapst 02C3F   ; LD ($FFFF),A
mapst 02C6A   ; LD ($FFFF),A
mapst 03138   ; LD ($FFFF),A
mapst 0474F   ; LD ($FFFF),A
mapst 04773   ; LD ($FFFF),A
mapst 050A3   ; LD ($FFFF),A
mapst 05142   ; LD ($FFFF),A
mapst 05155   ; LD ($FFFF),A
mapst 051CC   ; LD ($FFFF),A
mapst 051E7   ; LD ($FFFF),A
mapst 0520A   ; LD ($FFFF),A
mapst 05268   ; LD ($FFFF),A
mapst 052AB   ; LD ($FFFF),A
mapst 054AB   ; LD ($FFFF),A
mapst 057CB   ; LD ($FFFF),A
mapst 05A76   ; LD ($FFFF),A
mapst 05C2A   ; LD ($FFFF),A
mapst 05C42   ; LD ($FFFF),A
mapst 05D9C   ; LD ($FFFF),A
mapst 05DAA   ; LD ($FFFF),A
mapst 05F3C   ; LD ($FFFF),A
mapst 0607A   ; LD ($FFFF),A
mapst 06088   ; LD ($FFFF),A
mapst 0616C   ; LD ($FFFF),A
mapst 062DA   ; LD ($FFFF),A
mapst 062F0   ; LD ($FFFF),A
mapst 06380   ; LD ($FFFF),A
mapst 0648E   ; LD ($FFFF),A
mapst 06772   ; LD ($FFFF),A
mapst 06783   ; LD ($FFFF),A
mapst 067A9   ; LD ($FFFF),A
mapst 068CB   ; LD ($FFFF),A
mapst 06CDE   ; LD ($FFFF),A
mapst 06CF9   ; LD ($FFFF),A
mapst 06D6B   ; LD ($FFFF),A
mapst 06D79   ; LD ($FFFF),A
mapst 06D88   ; LD ($FFFF),A
mapst 00A3A   # LD ($FFFF),A; after LD A,($C1FC)
mapst 00A58   # LD ($FFFF),A; after EX AF,AF'
mapst 00AAF   # LD ($FFFF),A; after LD A,($C1FC)
mapst 00AE3   # LD ($FFFF),A; after EX AF,AF'
mapst 00E86   # LD ($FFFF),A; after LD A,($C1FC)
mapst 00E8D   # LD ($FFFF),A; after EX AF,AF'
mapst 00F30   # LD ($FFFF),A; after LD A,($C1FC)
mapst 00F5D   # LD ($FFFF),A; after EX AF,AF'
mapst 01702   # LD ($FFFF),A; after LD A,($C1FC)
mapst 01710   # LD ($FFFF),A; after EX AF,AF'
mapst 01CEA   # LD ($FFFF),A; after LD A,($C1FC)
mapst 01CF8   # LD ($FFFF),A; after EX AF,AF'
mapst 01DBD   # LD ($FFFF),A; after LD A,($C1FC)
mapst 01DEA   # LD ($FFFF),A; after EX AF,AF'
mapst 01DFD   # LD ($FFFF),A; after EX AF,AF'
mapst 01FF2   # LD ($FFFF),A; after LD A,($C1FC)
mapst 02000   # LD ($FFFF),A; after EX AF,AF'
mapst 04243   # LD ($FFFF),A; after LD A,$03
mapst 0425C   # LD ($FFFF),A; after EX AF,AF'
mapst 05FE7   # LD ($FFFF),A; after LD A,$13
mapst 0600A   # LD ($FFFF),A; after LD A,$14

# HALTs: each waits in the runtime for the game's own frame interrupt. Caves in the zero
# bytes of bank 1 at $7C00 (slot 1 holds bank 1 whenever the foreground runs).
eihalt 053B0   ; EI : HALT
eihalt 05513   ; EI : HALT
eihalt 0643A   ; EI : HALT
asm 0030E 5    ; HALT : SET 0,(IY+$05)
    jp hc_030e
endasm
asm 00316 5    ; LD B,$04 : HALT : DJNZ $0318 (4 frames)
    jp hc_0316
endasm
asm 00335 5    ; LD B,$04 : HALT : DJNZ $0337 (4 frames)
    jp hc_0335
endasm
asm 0535B 4    ; HALT : CALL $58EF
    jp hc_535b
endasm
asm 057B4 3    ; HALT : HALT : HALT
    jp hc_57b4
endasm
asm 057F0 4    ; HALT : CALL $05D7
    jp hc_57f0
endasm
asm 05819 4    ; HALT : LD HL,$5831
    jp hc_5819
endasm
asm 0582D 4    ; HALT : JP $05D7
    jp hc_jp05d7
endasm
asm 05869 4    ; HALT : CALL $05D7
    jp hc_5869
endasm
asm 058A7 4    ; HALT : JP $05D7
    jp hc_jp05d7
endasm
label hc_030e 07C00
label hc_0316 07C10
label hc_0335 07C20
label hc_535b 07C30
label hc_57b4 07C40
label hc_57f0 07C50
label hc_5819 07C60
label hc_jp05d7 07C70
label hc_5869 07C80
asm 07C00 16   ; zero bytes in bank 1: HALT : SET 0,(IY+$05)
    rst $00
    db halt_io
    set 0,(iy+$05)
    jp $0313
endasm
asm 07C10 16   ; zero bytes in bank 1: LD B,$04 : HALT : DJNZ
    ld b,$04
.w: rst $00
    db halt_io
    djnz .w
    jp $031B
endasm
asm 07C20 16   ; zero bytes in bank 1: LD B,$04 : HALT : DJNZ
    ld b,$04
.w: rst $00
    db halt_io
    djnz .w
    jp $033A
endasm
asm 07C30 16   ; zero bytes in bank 1: HALT : CALL $58EF
    rst $00
    db halt_io
    call $58EF
    jp $535F
endasm
asm 07C40 16   ; zero bytes in bank 1: HALT : HALT : HALT
    rst $00
    db halt_io
    rst $00
    db halt_io
    rst $00
    db halt_io
    jp $57B7
endasm
asm 07C50 16   ; zero bytes in bank 1: HALT : CALL $05D7
    rst $00
    db halt_io
    call $05D7
    jp $57F4
endasm
asm 07C60 16   ; zero bytes in bank 1: HALT : LD HL,$5831
    rst $00
    db halt_io
    ld hl,$5831
    jp $581D
endasm
asm 07C70 16   ; zero bytes in bank 1: HALT : JP $05D7
    rst $00
    db halt_io
    jp $05D7
endasm
asm 07C80 16   ; zero bytes in bank 1: HALT : CALL $05D7
    rst $00
    db halt_io
    call $05D7
    jp $586D
endasm

# The VRAM block writers: $021A writes A runs of 32 bytes from HL with OUTI : DJNZ (both take
# one from B, so LD B,$40 makes 32 bytes a run); $01D6 writes A runs of 32 bytes with an
# unrolled block of 32 OUTI. The sprite tables ($05B2, $05D7), the play frame handler's map
# rows ($5924-$592E) and the level loader's tiles ($4791, $514A, $68E9) use them. Each becomes a far call to page 0, which writes the bytes with one
# jt_vwrite call when the VDP is set for a VRAM write and C is $BE, and otherwise with OTIR
# through the runtime. No caller enters either routine past its first instruction.
asm 0021A 10   ; LD B,$40 : OUTI : DJNZ : DEC A : JR NZ : RET
    rst $00
    db far_io, pg_blk64, ent_blk64
    ret
endasm
asm 001D6 68   ; 32 OUTI : DEC A : JR NZ,$01D6 : RET
    rst $00
    db far_io, pg_blk32, ent_blk32
    ret
endasm
# The play frame handler's name table column ($58EF): 28 rows of 2 bytes from $C082, the
# address low byte in A (+$40 a row), the high byte from the table at HL' (alternate set,
# C' = $BF). The loop $5910-$591D becomes a far call to page 0, col, which writes the column
# with one jt_vwrite call for each run of rows $40 apart (two runs where the column wraps).
asm 05910 14   ; EXX : OUT ($BF),A : ADD A,$40 : OUTI : EXX : OUTI : OUTI : JR NZ,$5910
    rst $00
    db far_io, pg_col, ent_col
    jp $591E
endasm
page 0 blk64 blk32 col
; blk64, blk32: in A = runs of 32 bytes (0 = 256), HL = source, C = port. Out as the game's
; routines leave them: A = 0, HL past the bytes, B = 0 (blk64) or B - bytes (blk32), Z and N
; set, carry kept; C, DE, IX, IY and the interrupt state kept. Runs with interrupts off, on a stack of its own
; in the page; before DI it holds AF on the game's stack, where the game's own frame
; interrupt would push more.
blk64:  push af                 ; no variable is written before DI: the frame handler
        ld a,i                  ; calls these routines too. P/V = IFF2, kept by LD and DI.
        di
        ld a,$80                ; bit 7: B leaves as 0
        jr blk
blk32:  push af
        ld a,i
        di
        ld a,0                  ; B leaves less the bytes written (LD keeps P/V)
blk:    ld (v_mode),a
        ld a,0
        jp po,.ioff
        inc a
.ioff:  ld (v_iff),a
        pop af
        ld (v_cnt),a
        ld a,0
        rla                     ; the carry the game's routine keeps
        ld (v_cy),a
        ld (v_ssp),sp
        ld sp,stk
        ld (v_shl),hl
        ld (v_sde),de
        ld (v_sbc),bc
        ld (v_six),ix
        ld (v_siy),iy
        ; n = runs x run length
        ld a,(v_cnt)
        ld l,a
        ld h,0
        or a
        jr nz,.n1
        inc h                   ; 0 runs = 256
.n1:    add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld (v_nby),hl           ; 32 bytes a run
        ld a,c
        cp $BE
        jp nz,.slow
        ld a,(vdp_latch)
        or a
        jp nz,.slow
        ld a,(vdp_code)
        cp 1
        jp nz,.slow
        ; the bytes in chunks that end at the VRAM wrap ($4000 -> $0000), each chunk as
        ; runs of 256 bytes and one shorter run
        ld de,(vdp_addr)
        ld a,d
        and $3F
        ld d,a
        ld (v_dst),de
        ld hl,(v_shl)
        ld (v_cur),hl
        ld hl,(v_nby)
        ld (v_rem),hl
        ld ix,256
        ld iy,256
.ch:    ld de,(v_dst)
        ld hl,$4000
        or a
        sbc hl,de               ; room before the wrap
        ld de,(v_rem)
        or a
        sbc hl,de
        jr c,.part
        ld hl,(v_rem)             ; all that is left fits
        jr .c1
.part:  add hl,de               ; the room
.c1:    ld (v_chk),hl
        ld a,h
        or a
        jr z,.r
        ld c,a
        ld b,0
        ld hl,(v_cur)
        ld de,(v_dst)
        xor a
        call jt_vwrite
.r:     ld a,(v_chk)
        or a
        jr z,.adv
        ld b,a
        ld c,1
        ld a,(v_chk+1)
        ld hl,(v_cur)
        add a,h
        ld h,a
        ld a,(v_chk+1)
        ld de,(v_dst)
        add a,d
        ld d,a
        xor a
        call jt_vwrite
.adv:   ld de,(v_chk)
        ld hl,(v_cur)
        add hl,de
        ld (v_cur),hl
        ld hl,(v_dst)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (v_dst),hl
        ld hl,(v_rem)
        or a
        sbc hl,de
        ld (v_rem),hl
        ld a,h
        or l
        jr nz,.ch
        ld hl,(v_dst)
        ld (vdp_addr),hl
        jr .out
.slow:  ld hl,(v_nby)             ; one OUTI through the runtime a byte
        ld (v_rem),hl
        ld hl,(v_shl)
        ld sp,(v_ssp)             ; the runtime's I/O call runs on the game's stack
.sl:    rst $00
        db $A3                  ; OUTI
        ld de,(v_rem)
        dec de
        ld (v_rem),de
        ld a,d
        or e
        jr nz,.sl
        ld sp,stk
.out:   ld hl,(v_shl)
        ld de,(v_nby)
        add hl,de
        ld bc,(v_sbc)
        ld a,(v_mode)
        rlca
        ld a,0
        jr c,.b0
        ld a,b
        sub e                   ; B - bytes, as the OUTIs leave it
.b0:    ld b,a
        ld de,(v_sde)
        ld ix,(v_six)
        ld iy,(v_siy)
        ld sp,(v_ssp)
        ld a,(v_iff)
        or a
        jr z,.di
        ld a,(v_cy)
        rra
        ld a,1
        dec a                   ; A = 0, Z and N set, carry kept
        ei
        ret
.di:    ld a,(v_cy)
        rra
        ld a,1
        dec a
        ret

; col: in A = address low byte of the first row, HL = source (2 bytes a row), B = 2 x rows,
; HL' = table of address high bytes (one a row). Out as the game's loop leaves it: A + $40 a
; row, HL past the bytes, B = 0, Z set, HL' past the table bytes used, B' less one a row; C, C',
; DE, DE', IX, IY and the interrupt state kept.
col:    push af
        ld a,i
        di
        ld a,0
        jp po,.ioff
        inc a
.ioff:  ld (v_iff),a
        pop af
        ld (v_clo),a
        ld (v_ssp),sp
        ld sp,stk
        ld (v_shl),hl
        ld (v_sde),de
        ld (v_sbc),bc
        ld (v_six),ix
        ld (v_siy),iy
        exx
        ld (v_thl),hl
        ld (v_tbc),bc
        ld (v_tde),de
        exx
        ld a,b
        srl a
        ld (v_rows),a
        ld (v_lp),a
        ld ix,2
        ld iy,$40
        ld hl,(v_thl)
        ld (v_tp),hl
        ld hl,(v_shl)
        ld (v_src),hl
        call .addr              ; DE = first row's address
        ld (v_radr),de
        ld (v_prev),de
        ld hl,(v_src)
        ld (v_rsrc),hl
        ld a,1
        ld (v_rn),a
.next:  ld a,(v_lp)
        dec a
        ld (v_lp),a
        jr z,.last
        ld a,(v_clo)
        add a,$40
        ld (v_clo),a
        ld hl,(v_tp)
        inc hl
        ld (v_tp),hl
        ld hl,(v_src)
        inc hl
        inc hl
        ld (v_src),hl
        call .addr
        ld hl,(v_prev)
        ld bc,$40
        add hl,bc
        ld a,h
        and $3F
        ld h,a
        ld (v_prev),de
        or a
        sbc hl,de
        jr nz,.flush
        ld a,(v_rn)
        inc a
        ld (v_rn),a
        jr .next
.flush: ld (v_nadr),de
        call .write
        ld de,(v_nadr)
        ld (v_radr),de
        ld hl,(v_src)
        ld (v_rsrc),hl
        ld a,1
        ld (v_rn),a
        jr .next
.last:  call .write
        ; outputs
        ld a,(v_clo)
        add a,$40
        ld (v_clo),a
        ld hl,(v_tp)
        inc hl
        ld bc,(v_tbc)
        ld a,(v_rows)
        ld e,a
        ld a,b
        sub e
        ld b,a
        ld de,(v_tde)
        exx
        ld hl,(v_src)
        inc hl
        inc hl
        ld bc,(v_sbc)
        ld b,0
        ld de,(v_sde)
        ld ix,(v_six)
        ld iy,(v_siy)
        ld sp,(v_ssp)
        ld a,(v_iff)
        or a
        jr z,.di
        xor a                   ; Z set
        ld a,(v_clo)
        ei
        ret
.di:    xor a
        ld a,(v_clo)
        ret
; DE = (high byte from the table at (v_tp)) x 256 + (v_clo), bits 14 and 15 clear
.addr:  ld hl,(v_tp)
        call jt_peek
        and $3F
        ld d,a
        ld a,(v_clo)
        ld e,a
        ret
; one jt_vwrite for the run: (v_rn) rows from (v_rsrc) to (v_radr)
.write: ld hl,(v_rsrc)
        ld de,(v_radr)
        ld a,(v_rn)
        ld c,a
        ld b,2
        xor a
        jp jt_vwrite

v_cnt:    db 0
v_mode:   db 0
v_cy:     db 0
v_iff:    db 0
v_lp:     db 0
v_nby:    dw 0
v_shl:    dw 0
v_sde:    dw 0
v_sbc:    dw 0
v_six:    dw 0
v_siy:    dw 0
v_clo:    db 0
v_rows:   db 0
v_rn:     db 0
v_thl:    dw 0
v_tbc:    dw 0
v_tp:     dw 0
v_src:    dw 0
v_prev:   dw 0
v_radr:   dw 0
v_rsrc:   dw 0
v_dst:    dw 0
v_cur:    dw 0
v_rem:    dw 0
v_chk:    dw 0
v_nadr:   dw 0
v_tde:    dw 0
v_ssp:    dw 0
        ds 32
stk:
endpage

# Asterix and the Great Rescue (Europe, Brazil) (En,Fr,De,Es,It).cht, "Infinite Lives": RAM
# $C197 is the lives count
poke "Infinite lives"
ar 00C1-9709
endpoke

# Asterix and the Great Rescue (Europe, Brazil) (En,Fr,De,Es,It).cht, "Infinite Health": RAM
# $C196 is the health, 5 when full
poke "Infinite health"
ar 00C1-9605
endpoke

# Asterix and the Great Rescue (Europe, Brazil) (En,Fr,De,Es,It).cht, "Infinite Continues":
# RAM $C195 is the number on the game over screen's CONTINUE sign
poke "Max continues"
ar 00C1-9509
endpoke

# Asterix and the Great Rescue (Europe, Brazil) (En,Fr,De,Es,It).cht, "Invincible": RAM $C19E
# is the hit timer, held at 1
poke "Invincibility"
ar 00C1-9E01
endpoke
