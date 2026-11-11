# Chuck Rock (Europe, Brazil) (En), CRC32 DD0E2927, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of the title
# (300 s, no input), random input (600 s) and play (600 s, scripted).
# The logs ran no I/O or mapper site that the scan with them did not find.
# Code runs from banks 0 and 1 (slot 1 always holds bank 1) and from the sound driver in bank
# 31, which the frame handlers call at $AC66 after RST $18 with E = $1F (RST $18 writes
# ($0016) OR E, that is E, to $FFFF). The frame handler at $0038 calls the routine whose
# address is in $DFEE ($04FD for the logos, title and screens, $054C for play).
# $C7D7 (a note offset in the sound driver) comes from a count of loop passes in one frame at
# boot ($045A); it is 1 on the 60 Hz reference and 0 on the Next.
# Byte scan patterns judged not patched (verdicts in data/scan-verdicts.tsv): the development
# monitor $0071-$0378, entered only through RST $20 and RST $28, which no code uses, the VDP
# routines $0658-$06A9 and the sound driver's own interrupt wrapper $AC4E in bank 31, which
# nothing names (unused); an operand at $1CE2, a table in bank 1 and bytes in the data banks
# 3, 4, 5 and 30 (false).
name Chuck Rock
cart DD0E2927
hz 50		; No-Intro regions Europe, Brazil
# Most cells are priority cells: sprites go behind the palms, the grass and the rock walls.
# Page 0 writes the priority bit only in the cells under a sprite (ntd, mkmask).
priority
# No free RST vector: $0000-$0002 (DI; LD SP part) becomes the vector,
# the game starts at $0004 with the SP its LD SP,nn set.
vector 00 io
start 0004 DFEC
asm 00396 2   ; IM 1 -> IM 2
    im 2
endasm
site 00047   ; IN A,($BF)
site 00049   ; IN A,($C1)
site 003A6   ; IN A,($BF)
site 0042C   ; OUT (C),B
site 00436   ; OUT (C),B
site 0043E   ; OUT ($BE),A
site 00528   ; IN A,($BF)
site 00577   ; IN A,($BF)
site 005AB   ; OUT ($BF),A
site 005AF   ; OUT ($BF),A
site 005B8   ; OUT ($BF),A
site 005BC   ; OUT ($BF),A
site 005C5   ; OUT ($BF),A
site 005C9   ; OUT ($BF),A
site 005D6   ; OUT ($BF),A
site 005DA   ; OUT ($BF),A
site 00628   ; OUT ($BF),A
site 0062E   ; OUT ($BF),A
site 00641   ; OUT ($BF),A
site 00648   ; OUT ($BF),A
site 0064E   ; OUT ($BF),A
site 00655   ; OUT ($BF),A
site 00747   ; IN A,($DC)
site 00755   ; IN A,($DD)
site 00BD4   ; OUT ($BF),A
site 00BD8   ; OUT ($BF),A
site 00BE0   ; OUT ($BF),A
site 00BE4   ; OUT ($BF),A
site 00C1A   ; OUT ($BF),A
site 00C1E   ; OUT ($BF),A
site 00C24   ; OUT ($BF),A
site 00C28   ; OUT ($BF),A
site 00C51   ; OUT ($BF),A
site 00C55   ; OUT ($BF),A
site 00C5D   ; OUT ($BF),A
site 00C61   ; OUT ($BF),A
site 00C85   ; OUT ($BF),A
site 00C8A   ; OUT ($BF),A
site 00CE8   ; OUT ($BF),A
site 00CEF   ; OUT ($BF),A
site 041D5   ; OUT ($BF),A
site 041D9   ; OUT ($BF),A
site 7E913   ; OUT ($7F),A
site 7E917   ; OUT ($7F),A
site 7E924   ; OUT ($7F),A
site 7E928   ; OUT ($7F),A
site 7E959   ; OUT ($7F),A
site 7E970   ; OUT ($7F),A
site 7E984   ; OUT ($7F),A
site 7E993   ; OUT ($7F),A
site 7E9AA   ; OUT ($7F),A
site 7E9BE   ; OUT ($7F),A
site 7E9EB   ; OUT ($7F),A
site 7E9FE   ; OUT ($7F),A
site 7EA15   ; OUT ($7F),A
site 7EA1B   ; OUT ($7F),A
site 7EA3F   ; OUT ($7F),A
site 7EA56   ; OUT ($7F),A
site 7EA6A   ; OUT ($7F),A
site 7EAC7   ; OUT ($7F),A
# The RST $08 routine ($0008, $008B); no code the scan or the recordings reached uses RST $08.
site 0000A   ; OUT ($BF),A
site 0008D   ; OUT ($BF),A
site 7ECC3   ; OUT ($7F),A
site 7ECC8   ; OUT ($7F),A
site 7ECDC   ; OUT ($7F),A
site 7ECEF   ; OUT ($7F),A
site 7ECFB   ; OUT ($7F),A
site 7ED0E   ; OUT ($7F),A
mapst 00056   ; LD ($FFFF),A
mapst 00398   ; LD ($FFFC),A
mapst 0039B   ; LD ($FFFD),A
mapst 0039F   ; LD ($FFFE),A
mapst 003A3   ; LD ($FFFF),A

# HALTs: each waits in the runtime for the game's own frame interrupt. Caves in the
# development monitor at $0091-$0378, which the reset skips ($0007 is 1).
eihalt 00453   ; EI : HALT
eihalt 00495   ; EI : HALT
eihalt 004CB   ; EI : HALT
haltret 010F7  ; HALT : RET
asm 00455 5    ; HALT : LD (IY+$08),$00
    jp hc_0455
endasm
asm 00E2A 5    ; HALT : BIT 4,(IY+$04)
    jp hc_0e2a
endasm
asm 010D8 4    ; HALT : LD A,($C7D8)
    jp hc_10d8
endasm
asm 010E1 3    ; HALT : ADD A,$0A
    jp hc_10e1
endasm
asm 010E7 3    ; HALT : ADD A,$0A
    jp hc_10e7
endasm
asm 010FC 5    ; HALT : LD (IY+$12),$80
    jp hc_10fc
endasm
eihalt 010AD   ; EI : HALT
asm 010B5 4    ; HALT : CALL $104B
    jp hc_10b5
endasm
asm 01104 3    ; HALT : HALT : HALT
    jp hc_1104
endasm
label hc_0455 00091
label hc_0e2a 000A0
label hc_10d8 000B0
label hc_10e1 000C0
label hc_10e7 000D0
label hc_10fc 000E0
label hc_1104 000F0
label hc_10b5 00110
asm 00091 15   ; development monitor: HALT : LD (IY+$08),$00
    rst $00
    db halt_io
    ld (iy+$08),$00
    jp $045A
endasm
asm 000A0 16   ; development monitor: HALT : BIT 4,(IY+$04)
    rst $00
    db halt_io
    bit 4,(iy+$04)
    jp $0E2F
endasm
asm 000B0 16   ; development monitor: HALT : LD A,($C7D8)
    rst $00
    db halt_io
    ld a,($C7D8)
    jp $10DC
endasm
asm 000C0 16   ; development monitor: HALT : ADD A,$0A
    rst $00
    db halt_io
    add a,$0A
    jp $10E4
endasm
asm 000D0 16   ; development monitor: HALT : ADD A,$0A
    rst $00
    db halt_io
    add a,$0A
    jp $10EA
endasm
asm 000E0 16   ; development monitor: HALT : LD (IY+$12),$80
    rst $00
    db halt_io
    ld (iy+$12),$80
    jp $1101
endasm
asm 000F0 16   ; development monitor: HALT : HALT : HALT
    rst $00
    db halt_io
    rst $00
    db halt_io
    rst $00
    db halt_io
    jp $1107
endasm

# The play loop waits at $118C for the frame handler's stage counter (IY+$01) to be 0: the one
# frame after stage 0 (sprite table and name table) and before stage 1. On the Next, stage 0
# and the runtime's once-a-frame work after it can fill that frame when the view moves (the
# Layer 2 lines of the priority cells that come into view), so the next interrupt comes before
# the loop reads the counter, the loop never sees 0, and the game stops. The wait
# goes on at 0 or 1, as stage 0 has run at both. The game's buffers for the sprite table and
# name table are double ($C09E), so the step may start in stage 1.
asm 0118C 7    ; EI : LD A,(IY+$01) : OR A : JR NZ,$118C
    jp wt_118c
endasm
label wt_118c 00100
asm 00110 16   ; development monitor: HALT : CALL $104B
    rst $00
    db halt_io
    call $104B
    jp $10B9
endasm
asm 00100 16   ; development monitor: the wait at $118C
    ei
.w: ld a,(iy+$01)
    and $FE
    jr nz,.w
    jp $1193
endasm

# The VRAM writers. $06AA copies BC bytes from DE to the VRAM address in HL (OUTI : DJNZ, both
# take one from B). $06DB writes A runs of 32 bytes from HL to port C with 32 unrolled OUTI,
# after the caller has set the VDP address. Once a screen is up the frame handler calls $06AA
# for the whole name table every frame ($061B: 1536 bytes from $D000 to $3800), and the play
# frame handler calls $06DB for the sprite table ($05CF, $05E0), the tiles of the animated
# objects ($0BFA, $0C0F, $0C3D, $0C80) and the palette ($0635, a CRAM write). Through the
# runtime's traps the name table copy alone takes more than a frame, and the game does not
# leave its first HALT after the title. Each becomes a far call to page 0, which writes VRAM with
# jt_vwrite and anything else (CRAM) with OTIR through the runtime. No game code enters
# either routine past its first instruction.
asm 006AA 5    ; LD A,L : OUT ($BF),A : LD A,H : AND $3F
    rst $00
    db far_io, pg_cpy, ent_cpy
    ret
endasm
asm 006DB 64   ; OUTI x 32
    rst $00
    db far_io, pg_blk, ent_blk
    ret
endasm
# The sprite tile streamers $0C83, $0CE6 and $0D4D, which the play frame handler calls in
# its second stage: each walks a list ($CC00, $CC40, $CC80) of entries (32-byte tiles, bank,
# source) and writes each entry's tiles after the last, with 32 unrolled OUTI ($0C9E, $0D05)
# or OUTI : NOP : NOP : DJNZ ($0D5F). Each entry's write becomes a far call to blk, with the
# VDP address the routine set; no game code enters the loops past their first instruction.
asm 00C9E 64   ; OUTI x 32
    rst $00
    db far_io, pg_blk, ent_blk
    jp $0CE2
endasm
asm 00D05 64   ; OUTI x 32
    rst $00
    db far_io, pg_blk, ent_blk
    jp $0D49
endasm
asm 00D5D 11   ; LD B,$40 : OUTI : NOP : NOP : DJNZ $0D5F : DEC A : JR NZ,$0D5D
    rst $00
    db far_io, pg_blk, ent_blk
    jp $0D68
endasm
# The VRAM fill $06CA: E written BC times from the VRAM address in HL (OUT (C),B in a loop);
# the boot clears all 16K with it. It becomes a far call to page 0, fil, which writes the
# bytes with jt_vwrite from a buffer of 256 copies of E. No game code enters it past its first
# instruction.
asm 006CA 17   ; CALL $064D : ... : OUT (C),B : DEC DE : LD A,D : OR E : JR NZ,$06D3 : RET
    rst $00
    db far_io, pg_fil, ent_fil
    ret
endasm
page 0 cpy blk fil
; cpy: in HL = VRAM address, DE = source, BC = bytes (1 to 65535). Out as the game's routine
; leaves them: A = 0, B = 0, C = $BE, DE = the VRAM address given, HL = source + bytes, Z set;
; IX, IY and the interrupt state kept.
; blk: in A = runs of 32 bytes (0 = 256), HL = source, C = port. Out as the game's routine
; leaves them: A = 0, HL past the bytes, B less the bytes written, Z and N set, carry kept;
; C, DE, IX, IY and the interrupt state kept. Before DI it holds AF on the game's stack, where
; the game's own frame interrupt would push more.
; Both write no variable before DI (the frame handler calls the same routines), then run on
; a stack of their own in the page.
; Runtime internals used: jt_vwrite, vdp_latch, vdp_code, vdp_addr, vdp_rbuf, vdp_regs, nt_base,
; cur_mmu, and SHADOW_PAGE 28-29 (the VRAM copy, in slot 0 while tdf, ntd and mkmask read it;
; interrupts are off).
cpy:    ld a,i                  ; P/V = IFF2, kept by LD and DI
        di
        ld a,0
        jp po,.ioff
        inc a
.ioff:  ld (v_iff),a
        ld (v_ssp),sp
        ld sp,stk
        push ix
        push iy
        ld (v_vram),hl
        ex de,hl                ; HL = source, DE = VRAM address
        call wrv
        pop iy
        pop ix
        ld de,(v_vram)
        ld bc,$00BE
        ld sp,(v_ssp)
        ld a,(v_iff)
        or a
        jr z,.di
        xor a
        ei
        ret
.di:    xor a
        ret

blk:    push af
        ld a,i
        di
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
        push de
        push ix
        push iy
        ld (v_sbc),bc
        ld a,c
        cp $BE
        jr nz,.slow
        ld a,(vdp_latch)
        or a
        jr nz,.slow
        ld a,(vdp_code)
        cp 1
        jr nz,.slow
        ld a,(v_cnt)            ; BC = runs x 32
        ld c,a
        ld b,0
        or a
        jr nz,.n
        inc b
.n:     sla c
        rl b
        sla c
        rl b
        sla c
        rl b
        sla c
        rl b
        sla c
        rl b
        ld de,(vdp_addr)
        call wrv
        jr .out
.slow:  ld a,(v_cnt)
        ld e,a
.sl:    ld b,32                 ; one run with OTIR through the runtime
        rst $00
        db $B3
        dec e
        jr nz,.sl
.out:   ld bc,(v_sbc)
        ld a,(v_cnt)            ; B less the bytes, modulo 256
        add a,a
        add a,a
        add a,a
        add a,a
        add a,a
        neg
        add a,b
        ld b,a
        pop iy
        pop ix
        pop de
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

; fil: in HL = VRAM address, E = the value, BC = bytes (1 to 65535). Out as the game's
; routine leaves them: A = 0, B = the value, C = $BE, DE = 0, HL kept, Z set; IX, IY and the
; interrupt state kept. Writes nothing before DI, then runs on a stack of its own in the page.
fil:    ld a,i
        di
        ld a,0
        jp po,.ioff
        inc a
.ioff:  ld (v_iff),a
        ld (v_ssp),sp
        ld sp,stk
        push hl
        push ix
        push iy
        ld (v_n),bc
        ld a,e
        ld (v_fv),a
        ld hl,v_buf             ; 256 copies of the value
        ld (hl),a
        ld de,v_buf+1
        ld bc,255
        ldir
        pop iy
        pop ix
        pop hl
        push hl
        push ix
        push iy
        ex de,hl                ; DE = VRAM address
        ld a,d
        and $3F
        ld d,a
        ld hl,v_buf
        ld ix,0                 ; every run from the same 256 bytes
        ld iy,256
        ld a,(v_n+1)            ; whole runs of 256
        or a
        jr z,.rest
        ld c,a
        ld b,0
        ld a,1                  ; the source as mapped now: v_buf
        call jt_vwrite
        ld a,(v_n+1)
        add a,d
        and $3F
        ld d,a
.rest:  ld a,(v_n)
        or a
        jr z,.done
        ld b,a
        ld c,1
        ld a,1
        call jt_vwrite
.done:  pop iy
        pop ix
        pop hl
        ld de,0
        ld a,(v_fv)
        ld b,a
        ld c,$BE
        ld sp,(v_ssp)
        ld a,(v_iff)
        or a
        jr z,.di
        xor a
        ei
        ret
.di:    xor a
        ret

; wrv: writes BC bytes (1 to 65535) from HL to VRAM at DE with jt_vwrite. Whole name table
; rows inside the name table go as two calls, columns 0-7 and 8-31, with a step of one row:
; the form jt_vwrite writes fastest. Anything else goes in runs of 256 and one shorter run,
; split where the address wraps from $3FFF to $0000. Out: HL past the bytes; AF, BC, DE, IX
; and IY changed.
wrv:    ld (v_n),bc
        ld a,d
        and $3F
        ld d,a
        ld a,e
        and $3F
        jr nz,.gen
        ld a,c
        and $3F
        jr nz,.gen
        push hl
        ld hl,(nt_base)
        ex de,hl                ; HL = VRAM address, DE = name table base
        or a
        sbc hl,de
        jr c,.gen0              ; below the name table
        push hl
        ld bc,(v_n)
        add hl,bc
        ld bc,$0701
        or a
        sbc hl,bc
        pop hl
        jr nc,.gen0             ; past its end
        add hl,de
        ex de,hl                ; DE = VRAM address
        pop hl                  ; HL = source
        ld a,(v_n+1)            ; C = rows
        add a,a
        add a,a
        ld c,a
        ld a,(v_n)
        rlca
        rlca
        and 3
        or c
        ld c,a
        ld a,h
        cp $40
        jr c,.rows              ; a source below $4000: written whole
        ld a,d
        and $18
        cp $18
        jr nz,.rows             ; ntd's mask covers a table at $1800 or $3800 only
        ld a,c
        ld (v_rows),a
        jp ntd
.rows:  ld ix,64
        ld iy,64
        ld b,16
        xor a
        call jt_vwrite          ; columns 0-7
        push hl
        push de
        ld a,16
        add a,l
        ld l,a
        jr nc,.r1
        inc h
.r1:    ld a,16
        add a,e
        ld e,a
        ld b,48
        xor a
        call jt_vwrite          ; columns 8-31
        pop de
        pop hl
        ld bc,(v_n)
        add hl,bc
        ret
.gen0:  add hl,de
        ex de,hl
        pop hl
.gen:   ld a,h                  ; whole tiles from $4000 or above: only those that differ
        cp $40
        jr c,.gen1
        ld a,e
        and $1F
        jr nz,.gen1
        ld a,(v_n)
        and $1F
        jp z,tdf
.gen1:  ld ix,256
        ld iy,256
.ch:    push hl
        ld hl,$4000
        or a
        sbc hl,de               ; the room before the wrap
        ld bc,(v_n)
        or a
        sbc hl,bc
        jr nc,.fit
        add hl,bc
        ld b,h
        ld c,l
.fit:   ld (v_k),bc             ; the bytes of this piece
        pop hl
        ld a,b
        or a
        jr z,.rest
        push bc
        ld c,a
        ld b,0
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop bc
        ld a,h
        add a,b
        ld h,a
        ld a,d
        add a,b
        ld d,a
.rest:  ld a,c
        or a
        jr z,.adv
        ld b,a
        ld c,1
        xor a
        call jt_vwrite
        ld a,l
        add a,b
        ld l,a
        jr nc,.adv
        inc h
.adv:   push hl
        ld hl,(v_n)
        ld bc,(v_k)
        or a
        sbc hl,bc
        ld (v_n),hl
        ld a,h
        or l
        pop hl
        ret z
        ld de,0                 ; the rest from VRAM $0000
        jr .ch

; tdf: (v_n) bytes, a multiple of 32, from HL (at $4000 or above) to the VRAM address DE (a
; multiple of 32), outside the name table rows. The runtime marks each tile written for
; conversion, changed or not, and the game writes the same animation and sprite tiles again
; every game step. So each 32 bytes are compared with the VRAM copy and only the runs that
; differ are written; the VDP address, code, latch and read buffer are then set as the game's
; writes leave them. Out: HL past the source; AF, BC, DE, IX and IY changed.
tdf:    ld (v_dst),de
        ld bc,(v_n)
        add hl,bc
        ld (v_send),hl
        sbc hl,bc               ; carry clear from the add
        srl b
        rr c
        srl b
        rr c
        srl b
        rr c
        srl b
        rr c
        srl b
        rr c                    ; BC = 32-byte pieces
        ld (v_np),bc
        ld ix,0                 ; the run: pieces (0 = none open)
.pc:    ld a,d                  ; this piece's copy in slot 0
        and $3F
        ld d,a
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a
        push hl
        push de
        ld a,d
        and $1F
        ld d,a
        ld b,32
.cm:    ld a,(de)
        cp (hl)
        jr nz,.df
        inc hl
        inc de
        djnz .cm
        pop de                  ; the same: end the open run
        pop hl
        call tflush
        jr .nx
.df:    pop de                  ; differs: into the run
        pop hl
        ld a,ixl
        or ixh
        jr nz,.in
        ld (v_rs),hl
        ld (v_rd),de
.in:    inc ix
.nx:    ld bc,32
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        ld bc,(v_np)
        dec bc
        ld (v_np),bc
        ld a,b
        or c
        jr nz,.pc
        call tflush
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 back
        ld hl,(v_dst)           ; the VDP state after the game's writes
        ld bc,(v_n)
        add hl,bc
        ld a,h
        and $3F
        ld h,a
        ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld hl,(v_send)
        dec hl
        ld a,(hl)
        ld (vdp_rbuf),a
        inc hl
        ret
; tflush: writes the open run of IX pieces from (v_rs) to (v_rd), if any, and closes it.
; Keeps HL and DE.
tflush: ld a,ixl
        or ixh
        ret z
        push hl
        push de
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 for the source
        push ix
        pop bc                  ; pieces: whole runs of 256 bytes = BC / 8, then the rest
        ld hl,(v_rs)
        ld de,(v_rd)
.t1:    ld a,b
        or a
        jr nz,.t8
        ld a,c
        cp 8
        jr c,.t2
.t8:    push bc                 ; 8 pieces: 256 bytes
        ld bc,$0001
        ld ix,256
        ld iy,256
        xor a
        call jt_vwrite
        inc h
        inc d
        res 6,d
        pop bc
        ld a,c
        sub 8
        ld c,a
        jr nc,.t1
        dec b
        jr .t1
.t2:    or a
        jr z,.t3
        add a,a                 ; the rest: C x 32 bytes
        add a,a
        add a,a
        add a,a
        add a,a
        ld b,a
        ld c,1
        ld ix,256
        ld iy,256
        xor a
        call jt_vwrite
.t3:    ld ix,0
        pop de
        pop hl
        ret

; ntd: whole name table rows, (v_rows) of them, from HL (at $4000 or above) to the VRAM address
; DE (a row start in a table at $1800 or $3800). The runtime marks every priority cell written,
; changed or not, for a Layer 2 redraw, and this game writes its whole name table each game
; step, nearly all of it priority cells: a scroll step changes most of them and, written whole,
; takes about 8 frames. On the Master System the priority bit acts only where a sprite overlaps
; the cell. So the bytes written are the game's with the priority bit cleared in every cell that
; no sprite of the sprite table covers (the AND mask at msk, from mkmask), and of those only the
; cells that differ from the VRAM copy. One pass with the copy in slot 0 notes, for each row,
; the span from the first to the last differing cell in columns 0-7 and in columns 8-31; then
; each span is built in v_buf and written with one jt_vwrite, and the last byte once more, so
; that the VDP address and read buffer end as after the game's copy. The game never reads VRAM.
; Out: HL past the source; AF, BC, DE, IX and IY changed.
ntd:    ld (v_dst),de
        push hl
        ld hl,(nt_base)         ; the mask again only for a write from row 0: the game's
        or a                    ; other rows ($41E9) follow its row 0 write in the same
        sbc hl,de               ; frame handler
        call z,mkmask
        pop hl
        ld de,(v_dst)
        ld a,d
        and $20
        ld (v_vh),a             ; the VRAM address's 8K half
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a: the VRAM copy in slot 0
        ld a,d
        and $1F
        ld d,a                  ; DE = the cell in the copy; its mask byte is at DE + $2000
        ld ix,v_list
        xor a
        ld (v_ne),a
        ld a,(v_rows)
.row:   push af
        ld b,8
        call grp                ; columns 0-7
        ld b,24
        call grp                ; columns 8-31
        pop af
        dec a
        jr nz,.row
        ld (v_send),hl
        ld (v_dend),de
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 back
        ld ix,v_list
        ld a,(v_ne)
        or a
        jr z,.last
.wr:    push af
        ld l,(ix+0)             ; the span's source
        ld h,(ix+1)
        ld e,(ix+2)             ; its mask
        ld a,(ix+3)
        or $20
        ld d,a
        ld a,(ix+4)
        srl a
        ld iyl,a                ; cells
        ld bc,v_buf
.cp:    ld a,(hl)
        ld (bc),a
        inc hl
        inc bc
        inc de
        ld a,(de)
        and (hl)
        ld (bc),a
        inc hl
        inc bc
        inc de
        dec iyl
        jr nz,.cp
        ld hl,v_buf
        ld e,(ix+2)
        ld a,(v_vh)
        or (ix+3)
        ld d,a
        ld b,(ix+4)
        ld c,1
        push ix
        ld ix,64
        ld iy,64
        ld a,1                  ; the source as mapped now: v_buf
        call jt_vwrite
        pop ix
        ld de,5
        add ix,de
        pop af
        dec a
        jr nz,.wr
.last:  ld hl,(v_send)          ; the last byte once more
        dec hl
        ld de,(v_dend)
        dec de
        set 5,d
        ld a,(de)
        and (hl)
        ld (v_lb),a
        res 5,d
        ld a,(v_vh)
        or d
        ld d,a
        ld hl,v_lb
        ld bc,$0101
        ld ix,64
        ld iy,64
        ld a,1
        call jt_vwrite
        ld hl,(v_send)
        ret
; grp: compares B cells from HL, high byte ANDed with its mask byte (copy address + $2000),
; with the copy at DE, and notes the span of the differing ones at IX (source, copy address,
; bytes; 5 bytes) with (v_ne) counted. HL and DE move past the cells.
grp:    ld (v_gs),hl
        ld (v_gd),de
        ld a,$FF
        ld (v_fst),a            ; the first differing cell: none
        ld iyl,0
.lp:    ld a,(de)
        cp (hl)
        inc hl
        inc de
        jr nz,.d1
        set 5,d
        ld a,(de)
        and (hl)
        res 5,d
        ld c,a
        ld a,(de)
        cp c
        inc hl
        inc de
        jr nz,.rec
.nx:    inc iyl
        djnz .lp
        ld a,(v_fst)
        cp $FF
        ret z
        push hl
        push de
        ld c,a
        add a,a
        ld e,a
        ld d,0
        ld hl,(v_gs)
        add hl,de
        ld (ix+0),l
        ld (ix+1),h
        ld hl,(v_gd)
        add hl,de
        ld (ix+2),l
        ld (ix+3),h
        ld a,iyh
        sub c
        inc a
        add a,a
        ld (ix+4),a
        ld de,5
        add ix,de
        ld hl,v_ne
        inc (hl)
        pop de
        pop hl
        ret
.d1:    inc hl
        inc de
.rec:   ld a,iyl
        ld iyh,a                ; the last differing cell
        ld a,(v_fst)
        cp $FF
        jr nz,.nx
        ld a,iyl
        ld (v_fst),a
        jr .nx
; mkmask: the AND mask for the high bytes at msk ($3800-$3EFF, one row of 64 bytes for each
; name table row): $FF in each cell a sprite of the sprite table may cover, else $EF (priority
; bit off). For each sprite up to the $D0 end mark that has a line on the screen, the 3 rows
; from the one under its line Y+1 and the 2 columns from the one under its column X, with the
; scroll in vdp_regs and the wrap of the 28 rows and 32 columns (an 8x16 sprite covers at most
; 3 rows and 2 columns of cells). The marks of the call before are undone from the list at v_mkl.
mkmask: ld a,(v_init)
        or a
        jr nz,.undo
        ld hl,msk
        ld de,msk+1
        ld bc,$06FF
        ld (hl),$EF
        ldir
        ld a,1
        ld (v_init),a
        jr .new
.undo:  ld hl,v_mkl
        ld de,(v_mke)
        ld a,e
        sub l
        ld c,a
        ld a,d
        sbc a,h
        ld b,a
        srl b
        rr c                    ; BC = the marks listed
        ld a,b
        or c
        jr z,.new
.u1:    ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,$EF
        ld (de),a
        dec bc
        ld a,b
        or c
        jr nz,.u1
.new:   ld hl,v_mkl
        ld (v_mke),hl
        ld a,(vdp_regs+5)       ; the sprite table in the VRAM copy, in slot 0
        and $7E
        srl a
        ld h,a                  ; (reg 5 AND $7E) << 7: a multiple of $100
        ld l,0
        ld a,h
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a
        ld a,h
        and $1F
        ld h,a
        ld (v_sat),hl
        ld a,(vdp_regs+9)
        ld (v_vs),a
        ld a,(vdp_regs+8)
        ld (v_hs),a
        ld c,0                  ; the sprite
.sp:    ld hl,(v_sat)
        ld l,c
        ld a,(hl)
        cp $D0
        jr z,.end
        inc a                   ; the first line
        cp 192
        jr c,.on
        cp 256-15               ; above the screen: lines from line 0 on, or none
        jr c,.nx
        xor a
.on:    ld e,a
        ld a,(v_vs)             ; name table line = (line + V) mod 224, from 0-255 + 0-255
        add a,e
        jr c,.ov
        cp 224
        jr c,.ok
        sub 224
        jr .ok
.ov:    add a,32
.ok:    rrca
        rrca
        rrca
        and $1F
        ld (v_r),a              ; the row (0-27)
        ld a,c
        add a,a
        add a,$80
        ld l,a
        ld a,(v_hs)             ; name table column = (x - H) / 8
        ld e,a
        ld a,(hl)
        sub e
        rrca
        rrca
        rrca
        and $1F
        ld (v_c),a              ; the column (0-31)
        ld b,3
        ld a,(v_r)
.r:     push af
        call mk2
        pop af
        inc a
        cp 28
        jr c,.r1
        xor a
.r1:    djnz .r
.nx:    inc c
        ld a,c
        cp 64
        jr c,.sp
.end:   ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 back
        ret
; mk2: marks the cells (row A, column v_c) and (row A, column v_c + 1, mod 32), and lists them.
mk2:    ld l,a                  ; HL = msk + 1 + row x 64
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,msk+1
        add hl,de
        ld a,(v_c)
        call mk1
        ld a,(v_c)
        inc a
        and $1F
mk1:    add a,a                 ; the cell's high byte: HL + column x 2
        add a,l
        ld e,a
        ld a,h
        adc a,0
        ld d,a
        ld a,$FF
        ld (de),a
        push hl
        ld hl,(v_mke)
        ld (hl),e
        inc hl
        ld (hl),d
        inc hl
        ld (v_mke),hl
        pop hl
        ret

v_iff:  db 0
v_cnt:  db 0
v_cy:   db 0
v_ssp:  dw 0
v_vram: dw 0
v_sbc:  dw 0
v_n:    dw 0
v_k:    dw 0
v_rows: db 0
v_vh:   db 0
v_ne:   db 0
v_fst:  db 0
v_lb:   db 0
v_init: db 0
v_gs:   dw 0
v_gd:   dw 0
v_dst:  dw 0
v_send: dw 0
v_dend: dw 0
v_sat:  dw 0
v_sy:   db 0
v_sx:   db 0
v_mke:  dw 0
v_fv:   db 0
v_np:   dw 0
v_rs:   dw 0
v_rd:   dw 0
v_vs:   db 0
v_hs:   db 0
v_r:    db 0
v_c:    db 0
        ds 64
stk:
v_list: ds 5*56
v_mkl:  ds 2*64*6
v_buf:  ds 28*64
        ds $3800-$
msk:    ds $700                 ; at $3800: the mask, at the copy's address + $2000
endpage

# Chuck Rock (Europe, Brazil).cht and Chuck Rock (Europe) (Action Replay).cht, "Infinite Lives"
poke "Infinite lives"
ar 00C0-8E03
endpoke

# Chuck Rock (Europe, Brazil).cht and Chuck Rock (Europe) (Action Replay).cht, "Infinite Health"
poke "Infinite health"
ar 00C0-8F05
endpoke

# Chuck Rock (Europe, Brazil).cht, "Invulnerability"
poke "Invincibility"
ar 00C1-1102
endpoke

# Chuck Rock (Europe, Brazil).cht, "Level Select", and Chuck Rock (Europe) (Action Replay).cht,
# "Level Select (2-4)": values 1 to 4 start levels 2 to 5; 5 and above draw a garbled screen
poke "Start level"
ar 00C0-8C??
endpoke
