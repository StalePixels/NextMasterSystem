# Taz in Escape from Mars (Brazil) (En), CRC32 11CE074C, 512K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - The game's code is in banks 0, 1, 28 (sound) and 31 (the interrupt handler calls
#   $8000 there). Slot 1 is always bank 1: the only store to $FFFE with another value is
#   the interrupt handler putting back what it read. The sites in bank 1 and in the VDP
#   routines at $14BE and $2B74-$2C45, which no scanned path reaches, are listed like the
#   others.
# - The unpacker at $2A5E-$2B59 steps slot 2 to the next bank with
#   PUSH HL; LD HL,$FFFF; INC (HL); POP HL, and once with LD HL,$FFFF; INC (HL); XOR A.
#   Each is a CALL to a code cave in the $00 bytes at $2B5A-$2B73, which writes the
#   next bank through the runtime's mapper code.
# - The bank call stubs at $2F87-$3004 (bank 28) are reached only from banked code; their
#   mapper stores are listed like the others.
# - The tile routines at $0747 and $08A7 write each byte the unpacker gives (CALL $2A5C)
#   with its own OUT ($BE),A, 32 a tile, and the game runs them for about three tiles a
#   frame. Both loops are written again in place: the bytes go into $DFF0-$DFFB, which
#   the game never writes, and each 12 bytes go out with one OTIR through the runtime.
#   $0747 keeps its lookup through the table at $7E00.
# - priority: nearly every cell of a stage has the priority bit (the cage bars, the walls,
#   the capsule glass), and the bars hide Taz and the aliens in almost every frame of play.
#   With the bit in every cell, the runtime's Layer 2 redraw of the lines that a vertical
#   scroll brings into view takes more than the frame. Page 0 keeps the bit only in the
#   cells under a sprite: the game's four map writers give each cell's high byte to pw, and
#   fx, after the sprite table upload in the frame interrupt, sets and clears the bit as the
#   sprites move.
# - The other byte patterns that no path reached are in banks the code only reads data
#   from (verdict false).
name Taz in Escape from Mars
cart 11CE074C
hz 60		; No-Intro region Brazil
vector 20 io
priority
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 02C73 2   ; IM 1 -> IM 2
    im 2
endasm
asm 02CB0 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00750 227  ; LD DE,$7E00, then 32 times CALL $2A5C; LD E,A; LD A,(DE); OUT ($BE),A
    push hl
    ld de,$7E00
    ld b,32
ta_chunk:
    ld hl,$DFF0     ; 12 bytes of RAM the game never writes
    ld c,12
ta_byte:
    call $2A5C      ; the unpacker: next byte in A, the main registers kept
    ld e,a
    ld a,(de)
    ld (hl),a
    inc hl
    dec b
    jr z,ta_flush
    dec c
    jr nz,ta_byte
ta_flush:
    push bc
    ld a,l
    sub $F0
    ld b,a
    ld hl,$DFF0
    ld c,$BE
    rst $20
    db $B3          ; OTIR
    pop bc
    ld a,b
    or a
    jr nz,ta_chunk
    pop hl
    jp $0833
    ds 227 - ($ - $0750), 0
endasm
asm 008B0 160  ; 32 times CALL $2A5C; OUT ($BE),A
    push hl
    ld b,32
tb_chunk:
    ld hl,$DFF0     ; 12 bytes of RAM the game never writes
    ld c,12
tb_byte:
    call $2A5C      ; the unpacker: next byte in A, the main registers kept
    ld (hl),a
    inc hl
    dec b
    jr z,tb_flush
    dec c
    jr nz,tb_byte
tb_flush:
    push bc
    ld a,l
    sub $F0
    ld b,a
    ld hl,$DFF0
    ld c,$BE
    rst $20
    db $B3          ; OTIR
    pop bc
    ld a,b
    or a
    jr nz,tb_chunk
    pop hl
    ld bc,$0020     ; BC as the game's code leaves it
    jp $0950
    ds 160 - ($ - $08B0), 0
endasm
asm 02191 7    ; LD A,(HL) : AND $17 : NOP : XOR D : OUT ($BE),A, column writer's high byte
    ld a,(hl)
    rst $20
    db far_io, pg_pm, ent_pm
    rst $20
    db $04          ; OUT ($BE),A
endasm
asm 0227C 7    ; LD A,(HL) : AND $17 : NOP : XOR D : OUT ($BE),A, row writer's high byte
    ld a,(hl)
    rst $20
    db far_io, pg_pm, ent_pm
    rst $20
    db $04          ; OUT ($BE),A
endasm
asm 06CE4 6    ; LD A,(HL) : AND $17 : XOR D : OUT ($BE),A, stage writer's high byte
    ld a,(hl)
    rst $20
    db far_io, pg_pw, ent_pw
    nop
endasm
asm 071EA 6    ; LD A,(HL) : AND $17 : XOR D : OUT ($BE),A, object writer's high byte
    ld a,(hl)
    rst $20
    db far_io, pg_pw, ent_pw
    nop
endasm
asm 02826 5    ; OTIR : LD HL,$D57A, the sprite X and tile table in the frame interrupt
    rst $20
    db far_io, pg_fx, ent_fx
    nop
endasm
label cv_inc 02B5A
label cv_inc0 02B64
asm 02B5A 10   ; unused $00 bytes: cave for PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    push af
    ld a,($FFFF)
    inc a
    rst $20
    db $13, 0     ; LD ($FFFF),A
    pop af
    ret
endasm
asm 02B64 10   ; unused $00 bytes: cave for LD HL,$FFFF; INC (HL); XOR A
    ld hl,$FFFF
    ld a,(hl)
    inc a
    rst $20
    db $13, 0     ; LD ($FFFF),A
    xor a
    ret
endasm
asm 02A81 6    ; PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    call cv_inc
    nop
    nop
    nop
endasm
asm 02A98 6    ; PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    call cv_inc
    nop
    nop
    nop
endasm
asm 02AAB 6    ; PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    call cv_inc
    nop
    nop
    nop
endasm
asm 02ABA 6    ; PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    call cv_inc
    nop
    nop
    nop
endasm
asm 02AE1 6    ; PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    call cv_inc
    nop
    nop
    nop
endasm
asm 02AF1 6    ; PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    call cv_inc
    nop
    nop
    nop
endasm
asm 02B01 6    ; PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    call cv_inc
    nop
    nop
    nop
endasm
asm 02B28 6    ; PUSH HL; LD HL,$FFFF; INC (HL); POP HL
    call cv_inc
    nop
    nop
    nop
endasm
asm 02B50 5    ; LD HL,$FFFF; INC (HL); XOR A
    call cv_inc0
    nop
    nop
endasm
mapldk 02C78   ; LD HL,$FFFC; LD (HL),$00
maphl 02C7E   ; LD (HL),$00, HL = $FFFD
maphl 02C81   ; LD (HL),$01, HL = $FFFE
maphl 02C84   ; LD (HL),$02, HL = $FFFF
site 0000A   ; OUT ($BF),A
site 0000F   ; OUT ($BF),A
site 0001A   ; OUT ($BF),A
site 0001D   ; OUT ($BF),A
site 00040   ; OUT ($BF),A
site 00044   ; OUT ($BF),A
mapst 0006E   ; LD ($FFFC),A
mapst 00071   ; LD ($FFFD),A
mapst 00076   ; LD ($FFFE),A
mapst 0007B   ; LD ($FFFF),A
site 0008A   ; OTIR
mapst 000B2   ; LD ($FFFF),A
mapst 000DB   ; LD ($FFFF),A
mapst 00106   ; LD ($FFFF),A
mapst 00212   ; LD ($FFFF),A
site 00245   ; OUT ($BF),A
site 00252   ; OUT ($BF),A
mapst 002F6   ; LD ($FFFF),A
mapst 0031C   ; LD ($FFFF),A
mapst 00439   ; LD ($FFFF),A
mapst 0054B   ; LD ($FFFF),A
mapst 00744   ; LD ($FFFF),A
site 00749   ; OUT ($BF),A
site 0074E   ; OUT ($BF),A
mapst 00844   ; LD ($FFFF),A
mapst 008A1   ; LD ($FFFF),A
site 008A9   ; OUT ($BF),A
site 008AE   ; OUT ($BF),A
mapst 00961   ; LD ($FFFF),A
mapst 00B02   ; LD ($FFFF),A
mapst 00D86   ; LD ($FFFF),A
mapst 00E03   ; LD ($FFFF),A
mapst 010AA   ; LD ($FFFF),A
mapst 010BA   ; LD ($FFFF),A
mapst 01340   ; LD ($FFFF),A
mapst 013A1   ; LD ($FFFF),A
mapst 013DE   ; LD ($FFFF),A
mapst 0145C   ; LD ($FFFF),A
site 014BE   ; IN A,($BF)
site 014C2   ; OUT ($BF),A
site 014C8   ; OUT ($BF),A
site 014D3   ; OUT ($BE),A
mapst 015E7   ; LD ($FFFF),A
mapst 01680   ; LD ($FFFF),A
mapst 01717   ; LD ($FFFF),A
mapst 01909   ; LD ($FFFF),A
mapst 01918   ; LD ($FFFF),A
mapst 01A94   ; LD ($FFFF),A
mapst 01A9C   ; LD ($FFFF),A
mapst 01E4A   ; LD ($FFFF),A
mapst 01E65   ; LD ($FFFF),A
site 02184   ; OUT ($BF),A
site 0218B   ; OUT ($BF),A
site 0218E   ; OUT ($BE),A
site 02265   ; OUT ($BF),A
site 0226C   ; OUT ($BF),A
site 02279   ; OUT ($BE),A
site 022D4   ; OUT ($BF),A
site 022D9   ; OUT ($BF),A
mapst 022FE   ; LD ($FFFF),A
mapst 02344   ; LD ($FFFF),A
mapst 0234C   ; LD ($FFFF),A
site 027B2   ; IN A,($BF)
mapst 027C4   ; LD ($FFFC),A
mapst 027C8   ; LD ($FFFD),A
mapst 027CC   ; LD ($FFFE),A
mapst 027D0   ; LD ($FFFF),A
site 027EC   ; OUT ($BF),A
site 027F0   ; OUT ($BF),A
site 027F8   ; OUT ($BF),A
site 027FC   ; OUT ($BF),A
site 02801   ; OUT ($BF),A
site 02805   ; OUT ($BF),A
site 02810   ; OTIR
site 0281E   ; OUT ($BF),A
site 02822   ; OUT ($BF),A
site 0284E   ; OUT ($BF),A
site 02852   ; OUT ($BF),A
mapst 02880   ; LD ($FFFF),A
mapst 02887   ; LD ($FFFF),A
site 0288C   ; OUT ($BF),A
site 02890   ; OUT ($BF),A
site 02897   ; OUT ($BE),A
site 028A4   ; OUT ($BF),A
site 028A9   ; OUT ($BF),A
site 028B7   ; OUT (C),A
site 028BC   ; OUT (C),A
site 028CE   ; OUT ($BF),A
site 028D3   ; OUT ($BF),A
site 028E1   ; OUT (C),A
site 028E6   ; OUT (C),A
mapst 0290F   ; LD ($FFFF),A
mapst 02931   ; LD ($FFFF),A
mapst 0296A   ; LD ($FFFF),A
mapst 0299D   ; LD ($FFFF),A
site 029CB   ; OUT ($BF),A
site 029D0   ; OUT ($BF),A
site 029D8   ; OUT ($BE),A
mapst 02A18   ; LD ($FFFF),A
mapst 02A2D   ; LD ($FFFF),A
site 02A38   ; OUT ($BF),A
site 02A3D   ; OUT ($BF),A
site 02A4E   ; OUT ($BE),A
mapst 02A69   ; LD ($FFFF),A
mapst 02B1E   ; LD ($FFFF),A
mapst 02B3E   ; LD ($FFFF),A
site 02B81   ; OUT ($BE),A
site 02B86   ; OUT ($BE),A
mapst 02B9D   ; LD ($FFFF),A
site 02BA8   ; OUT ($BF),A
site 02BAF   ; OUT ($BF),A
site 02BB7   ; OUTI
site 02BBD   ; OUTI
mapst 02BCC   ; LD ($FFFF),A
mapst 02BD6   ; LD ($FFFF),A
site 02BDF   ; OUT ($BF),A
site 02BE4   ; OUT ($BF),A
site 02BEB   ; OTIR
mapst 02BF4   ; LD ($FFFF),A
mapst 02BFE   ; LD ($FFFF),A
site 02C07   ; OUT ($BF),A
site 02C0C   ; OUT ($BF),A
otir 02C13   ; OUTI
mapst 02C1E   ; LD ($FFFF),A
mapst 02C28   ; LD ($FFFF),A
site 02C2D   ; OUT ($BF),A
site 02C32   ; OUT ($BF),A
site 02C39   ; OTIR
mapst 02C42   ; LD ($FFFF),A
site 02C9B   ; IN A,($7E)
site 02CB5   ; IN A,($BF)
site 02CBE   ; OTIR
site 02CD6   ; OUT ($BF),A
site 02CDA   ; OUT ($BF),A
site 02CE5   ; OTIR
site 02CF3   ; OUT ($BF),A
site 02CF7   ; OUT ($BF),A
site 02CFB   ; OTIR
mapst 02D29   ; LD ($FFFF),A
mapst 02D3C   ; LD ($FFFF),A
site 02D48   ; OUT ($BF),A
mapst 02E88   ; LD ($FFFF),A
mapst 02EAB   ; LD ($FFFF),A
mapst 02EE5   ; LD ($FFFF),A
mapst 02F5A   ; LD ($FFFF),A
mapst 02F8D   ; LD ($FFFF),A
mapst 02F95   ; LD ($FFFF),A
mapst 02F9F   ; LD ($FFFF),A
mapst 02FA6   ; LD ($FFFF),A
mapst 02FB3   ; LD ($FFFF),A
mapst 02FBB   ; LD ($FFFF),A
mapst 02FC5   ; LD ($FFFF),A
mapst 02FCD   ; LD ($FFFF),A
mapst 02FD7   ; LD ($FFFF),A
mapst 02FDF   ; LD ($FFFF),A
mapst 02FE9   ; LD ($FFFF),A
mapst 02FF0   ; LD ($FFFF),A
mapst 02FFA   ; LD ($FFFF),A
mapst 03001   ; LD ($FFFF),A
site 0307B   ; OUT ($BF),A
site 0307E   ; OUT ($BF),A
site 03082   ; OUT ($BE),A
site 0308B   ; OUT ($BE),A
site 0321F   ; OUT ($BF),A
site 03222   ; OUT ($BF),A
site 03229   ; IN A,($BE)
site 03231   ; IN A,($BE)
site 03282   ; OUT ($BF),A
site 03285   ; OUT ($BF),A
site 03289   ; OUT ($BE),A
site 03291   ; OUT ($BE),A
mapst 04B7F   ; LD ($FFFF),A
mapst 04C31   ; LD ($FFFF),A
site 06C86   ; IN A,($BF)
site 06CCD   ; OUT ($BF),A
site 06CD4   ; OUT ($BF),A
site 06CDD   ; OUT ($BE),A
site 06D28   ; OUT ($BF),A
site 06D2C   ; OUT ($BF),A
site 06D31   ; OUT ($BE),A
site 06E26   ; OUT ($BE),A
site 06E49   ; IN A,($DC)
site 0716D   ; OUT ($BF),A
site 07172   ; OUT ($BF),A
site 071CA   ; OUT ($BF),A
site 071CF   ; OUT ($BF),A
site 071E3   ; OUT ($BE),A
site 7C4F1   ; OUT ($7F),A
site 7C506   ; OUT ($7F),A
site 7C50F   ; OUT ($7F),A
site 7C51A   ; OUT ($7F),A
site 7C545   ; OUT ($7F),A
site 7C681   ; OUT ($7F),A
site 7C6BA   ; OUT ($7F),A
site 7C6C3   ; OUT ($7F),A
site 7C6DE   ; OUT ($7F),A
site 7C6E2   ; OUT ($7F),A
site 7C798   ; OUT ($7F),A
site 7C7AE   ; OUT ($7F),A
site 7C7C6   ; OUT ($7F),A
site 7C7CA   ; OUT ($7F),A
site 7C7D8   ; OUT ($7F),A
site 7C816   ; OUT ($7F),A
page 0 pw pm fx
; The priority bit only in the cells under a sprite. On the Master System the bit acts only
; where a sprite overlaps the cell, and nearly every cell of a stage (the cage bars, the walls,
; the capsule glass) has it; the runtime draws every priority cell that the game writes or that
; a vertical scroll brings into view in Layer 2, more than the frame holds. So the VRAM copy
; holds the bit only in the cells that a sprite of the frame may cover, and Layer 2 draws only
; those.
; pw: the high byte of a name table cell from the game's map writers (column $2114, row $21E0,
; stage $6CC0, object $71C0). In A = the map byte, D = the flip and palette bits to XOR, HL = the
; map byte's address (the low byte at HL-1, already written). The cell's high byte is
; (A AND $17) XOR D, as the game's own code makes it. The page keeps it and the low byte (gw,
; glo) and writes it at vdp_addr with the priority bit only when the cell was under a sprite at
; the last frame interrupt (stamp in stp). Out: A and F changed; the rest and the interrupt
; state kept.
; pm: as pw, but it writes nothing: out A = the byte to write, for the game's own OUT ($BE),A
; after the far call (the column and row writers, where the patch has room for it). A write
; through jt_vwrite costs about 3,000 cycles more a cell than that trap.
; fx: in the frame interrupt, at $2826: the game's OTIR of the sprite X and tile table (B = $80
; bytes from HL = $C228 to port C), then the cells under each sprite of the game's table in
; RAM ($C1E8 Y, $C228 X and tile; 8x8 sprites) with the scroll in vdp_regs are stamped: the
; one to four cells that each sprite overlaps. A covered cell whose kept byte has the priority bit gets it written
; back. A cell keeps the bit until no sprite has covered it for 32 frames, and at most 3 cells
; a frame lose it: each change is a Layer 2 draw of the cell, about 10,000 cycles, and a bit
; with no sprite over it changes nothing on the screen. Only cells
; whose VRAM copy still holds what the page wrote are changed (another writer has the cell
; otherwise). Out: HL = $D57A, B = 0, C = $BE, as the game's code leaves them.
; Runtime internals used: jt_vwrite, jt_peek, vdp_addr, vdp_regs, cur_mmu, and SHADOW_PAGE 29
; (the VRAM copy at $2000-$3FFF, in slot 0 while fx reads it; interrupts are off).
NL      equ 300                 ; cells a list holds
pw:     ld (p_a),a
        ld a,1
        jr pw0
pm:     ld (p_a),a
        xor a
pw0:    ld (p_wm),a
        ld a,i                  ; P/V = IFF2
        di
        ld a,0
        jp po,.ioff
        inc a
.ioff:  ld (p_iff),a
        ld (p_hl),hl
        ld (p_ssp),sp
        ld sp,stk
        push bc
        push de
        push ix
        push iy
        ld a,(p_a)
        and $17
        xor d
        ld (p_v),a
        ld hl,(vdp_addr)
        ld a,l
        rra
        jr nc,.raw              ; not a high byte
        ld a,h
        sub $38
        jr c,.raw
        cp 7
        jr nc,.raw              ; not in the name table at $3800
        ld h,a
        srl h
        rr l                    ; HL = the cell, 0-895
        ld b,h
        ld c,l
        ld hl,(p_hl)
        dec hl
        call jt_peek            ; the low byte
        ld hl,glo
        add hl,bc
        ld (hl),a
        ld hl,gw
        add hl,bc
        ld a,(p_v)
        ld (hl),a
        ld hl,sts
        add hl,bc
        ld (hl),0
        bit 4,a
        jr z,.wr
        ld hl,stp
        add hl,bc
        ld a,(p_cur)
        cp (hl)
        jr nz,.clr
        call app                ; covered: the bit stays
        jr nc,.clr
        ld hl,sts
        add hl,bc
        ld (hl),1
.raw:   ld a,(p_v)
        jr .wr
.clr:   ld a,(p_v)
        and $EF
.wr:    ld (p_b),a
        ld a,(p_wm)
        or a
        jr z,.nw
        ld hl,p_b
        ld de,(vdp_addr)
        call wr1
.nw:    pop iy
        pop ix
        pop de
        pop bc
        ld hl,(p_hl)
        ld sp,(p_ssp)
        ld a,(p_iff)
        or a
        ld a,(p_b)
        ret z
        ei
        ret
; app: cell BC onto the current list. Carry set if it went on, clear if the list is full.
app:    ld hl,(p_ln)
        ld de,NL
        or a
        sbc hl,de
        ret nc
        ld hl,(p_ln)
        inc hl
        ld (p_ln),hl
        dec hl
        add hl,hl
        ld de,(p_lp)
        add hl,de
        ld (hl),c
        inc hl
        ld (hl),b
        scf
        ret
; wr1: one byte from HL (in the page) to VRAM address DE.
wr1:    ld bc,$0101
        ld ix,1
        ld iy,1
        ld a,1
        jp jt_vwrite

fx:     rst $20
        db $B3                  ; OTIR
        ld (p_ssp),sp
        ld sp,stk
        push de
        push ix
        push iy
        call cover
        pop iy
        pop ix
        pop de
        ld sp,(p_ssp)
        ld hl,$D57A
        ld bc,$00BE
        ret

cover:  ld a,(p_cur)            ; a new stamp
        inc a
        jr nz,.c1
        ld hl,stp
        ld de,stp+1
        ld bc,895
        ld (hl),0
        ldir
        ld a,1
.c1:    ld (p_cur),a
        ld hl,(p_lp)            ; the last list becomes the old one
        ld (p_op),hl
        ld hl,(p_ln)
        ld (p_on),hl
        ld de,ls0
        ld hl,(p_lp)
        or a
        sbc hl,de
        jr nz,.c2
        ld de,ls1
.c2:    ld (p_lp),de
        ld hl,0
        ld (p_ln),hl
        ld hl,wq
        ld (p_wq),hl
        ld a,(vdp_regs+2)
        and $0E
        cp $0E
        jp nz,.wq               ; name table not at $3800
        ld a,(vdp_regs+9)
        cp 224
        jr c,.v
        sub 224
.v:     ld (p_vs),a
        ld a,(vdp_regs+8)
        ld (p_hs),a
        ld a,29                 ; SHADOW_PAGE + 1: VRAM $2000-$3FFF in slot 0
        db $ED,$92,$50          ; nextreg $50,a
        ld ix,$C1E8
        ld iy,$C228
        ld a,64
        ld (p_n),a
.sp:    ld a,(ix+0)
        cp $D0
        jr z,.old
        inc a                   ; the first line
        cp 192
        jr c,.on
        cp 256-7
        jr c,.nx                ; below the screen
        xor a                   ; partly above: from line 0
.on:    ld e,a
        ld a,(p_vs)             ; name table line = (line + V) mod 224
        add a,e
        jr c,.ov
        cp 224
        jr c,.ok
        sub 224
        jr .ok
.ov:    add a,32
.ok:    ld (p_r),a              ; the name table line of the first line
        ld a,(p_hs)
        ld e,a
        ld a,(iy+0)
        sub e
        ld (p_x),a              ; the name table pixel of the first pixel
        rrca
        rrca
        rrca
        and $1F
        ld (p_c),a
        ld a,(p_r)
        and $F8
        call mk2
        ld a,(p_r)
        and 7
        jr z,.nx                ; on a row's first line: one row
        ld a,(p_r)
        and $F8
        add a,8
        cp 224
        jr c,.r2
        xor a
.r2:    call mk2
.nx:    inc ix
        inc iy
        inc iy
        ld hl,p_n
        dec (hl)
        jr nz,.sp
.old:   xor a                   ; cells of the last list that no sprite covers now
        ld (p_ncl),a
        ld hl,(p_on)
        ld a,h
        or l
        jr z,.done
        ld ix,(p_op)
.ol:    push hl
        ld c,(ix+0)
        ld b,(ix+1)
        ld hl,sts
        add hl,bc
        ld a,(hl)
        or a
        jr z,.on2               ; the bit is off already
        ld hl,stp
        add hl,bc
        ld a,(p_cur)
        cp (hl)
        jr z,.on2               ; covered: on the new list already
        sub (hl)
        cp 32
        jr c,.keep              ; covered in the last 32 frames: the bit stays
        ld a,(p_ncl)
        cp 3
        jr nc,.keep             ; 3 cells cleared in this frame already
        inc a
        ld (p_ncl),a
        ld hl,sts
        add hl,bc
        ld (hl),0
        call vchk               ; the copy as written, with the bit?
        jr nz,.on2
        cp (hl)
        jr nz,.on2
        and $EF
        call queue
        jr .on2
.keep:  call app                ; a full list leaves the bit on, untracked
.on2:   inc ix
        inc ix
        pop hl
        dec hl
        ld a,h
        or l
        jr nz,.ol
.done:  ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 back
.wq:    ld hl,(p_wq)            ; the writes
        ld de,wq
        or a
        sbc hl,de
        ret z
        ld hl,wq
.w:     ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        push hl
        call wr1
        pop hl
        inc hl
        ld de,(p_wq)
        ld a,l
        cp e
        jr nz,.w
        ld a,h
        cp d
        jr nz,.w
        ret
; mk2: the cells (row A/8, column p_c) and, unless the sprite starts on a cell's first pixel
; (p_x), (row A/8, column p_c + 1, mod 32).
mk2:    ld l,a
        ld h,0
        add hl,hl
        add hl,hl               ; row x 32
        ld a,(p_c)
        ld c,a
        ld b,0
        push hl
        add hl,bc
        ld b,h
        ld c,l
        call mkc
        pop hl
        ld a,(p_x)
        and 7
        ret z
        ld a,(p_c)
        inc a
        and $1F
        ld c,a
        ld b,0
        add hl,bc
        ld b,h
        ld c,l
; mkc: cell BC is under a sprite this frame.
mkc:    ld hl,stp
        add hl,bc
        ld a,(p_cur)
        cp (hl)
        ret z                   ; done this frame
        ld (hl),a
        ld hl,gw
        add hl,bc
        bit 4,(hl)
        ret z                   ; the game has no priority bit here
        ld hl,sts
        add hl,bc
        ld a,(hl)
        or a
        jr nz,.app              ; the bit is on already
        call vchk               ; the copy as written, without the bit?
        ret nz
        and $EF
        cp (hl)
        ret nz
        call app
        ret nc                  ; list full: left without the bit
        ld hl,sts
        add hl,bc
        ld (hl),1
        ld hl,gw
        add hl,bc
        ld a,(hl)
        jp queue
.app:   jp app
; vchk: cell BC. Z set if the copy's low byte is glo's and its high byte is gw's; then A = gw.
; HL = the copy's high byte (slot 0 holds VRAM $2000-$3FFF).
vchk:   ld hl,glo
        add hl,bc
        ld a,(hl)
        ld h,b
        ld l,c
        add hl,hl
        ld de,$1800
        add hl,de
        cp (hl)
        inc hl
        ret nz
        push hl
        ld hl,gw
        add hl,bc
        ld a,(hl)
        pop hl
        ret                     ; Z from the low byte; the caller compares the high byte
; queue: the write of A to the high byte of cell BC.
queue:  ld hl,(p_wq)
        push af
        push hl
        ld h,b
        ld l,c
        add hl,hl
        ld de,$3801
        add hl,de
        ex de,hl
        pop hl
        ld (hl),e
        inc hl
        ld (hl),d
        inc hl
        pop af
        ld (hl),a
        inc hl
        ld (p_wq),hl
        ret

p_a:    db 0
p_iff:  db 0
p_v:    db 0
p_b:    db 0
p_cur:  db 1                    ; the stamp of the last frame; stp starts at 0
p_vs:   db 0
p_hs:   db 0
p_r:    db 0
p_c:    db 0
p_n:    db 0
p_wm:   db 0
p_x:    db 0
p_ncl:  db 0
p_hl:   dw 0
p_ssp:  dw 0
p_lp:   dw ls0
p_ln:   dw 0
p_op:   dw 0
p_on:   dw 0
p_wq:   dw 0
        ds 96
stk:
ls0:    ds 2*NL
ls1:    ds 2*NL
wq:     ds 3*2*NL
        ds $3000-$
gw:     ds 896
glo:    ds 896
sts:    ds 896
stp:    ds 896
endpage
