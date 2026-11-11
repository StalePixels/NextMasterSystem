# Gauntlet (Europe, Brazil) (En), CRC32 D9190956, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, scanned with reference I/O logs.
# Decisions:
# - $0028 holds bytes of the game (RES 2,H; LD A,(HL); AND A; EX AF,AF'; RET) and RST $08,
#   $10, $18, $20, $30 and $38 are the game's, so $0000 is the io vector. No scanned path
#   runs RST $00 or JP $0000.
# - $0401 (LD (HL),$80, HL = $FFFC) is not patched: it writes the runtime's copy of $FFFC,
#   and bit 3 (cart RAM) stays clear.
# - Mapper stores that no spec line form takes go to code caves in the $FF filler of bank 1
#   ($6B80 on): $1062 and $106D (LD (HL),A, HL = $FFFF), $117A and $1197 (INC (IX+0),
#   IX = $FFFF: the next bank).
# - The start-up's speed test at $086F (EI; HALT; HALT; count until the frame handler
#   changes $C8A0) picks the PAL timing table ($52AB to $D080) when the count is $0A41 or
#   more. Its HALTs wait for the game's interrupt.
# - The scan's jump table at $4C57 has 16 code entries; the 7 words after them ($2A15,
#   $0F3F, $063F, $030B, $392B, $3730, $0C3E) are data, so $2A15 is not a HALT (it is the
#   last byte of BIT 6,(IY+$05) at $2A12).
# - Four of the frame handler's VDP routines run in page 0: the sprite loop at $1A9C
#   (spr: it POPs masks from $D430 with SP pointed there, and an RST in place of its OUTs
#   would overwrite them), the sprite pattern writer at $09E3 (sat), the name table copy
#   at $0EAA (nts) and the 8 name table cells at $0A6B (nmr). Through the runtime's traps
#   they took most of each frame. spr and nts compare with the VRAM copy and write only
#   what differs: the runtime converts every tile it is given again.
# - The game's random numbers use LD A,R ($00E3): compare runs of changed page code with
#   run.py --pinr.
name Gauntlet
cart D9190956
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
start 03FA
asm 00411 2   ; IM 1 -> IM 2
    im 2
endasm
site 0041A   ; OUT ($3E),A
site 0041E   ; OUT ($3F),A
site 00809   ; OUT ($BE),A
site 0080F   ; OUT ($BE),A
site 00937   ; OUT ($BE),A
site 0093C   ; OUT ($BE),A
site 00941   ; OUT ($BE),A
site 00946   ; OUT ($BE),A
site 009E6   ; OUT ($BF),A
site 009E9   ; OUT (C),H
site 009EC   ; OUTI
site 009EF   ; OUT ($BF),A
site 009F2   ; OUT (C),H
site 009F5   ; OUTI
site 009F8   ; OUT ($BF),A
site 009FB   ; OUT (C),H
site 009FE   ; OUTI
site 00A01   ; OUT ($BF),A
site 00A04   ; OUT (C),H
site 00A07   ; OUTI
site 00A09   ; OUT ($BF),A
site 00A0C   ; OUT (C),H
site 00A10   ; OUTI
site 00A50   ; OUT ($BF),A
site 00A53   ; OUT ($BF),A
site 00A70   ; OUTI
site 00A73   ; OUT (C),A
site 00A75   ; OUTI
site 00A78   ; OUT (C),A
site 00A7A   ; OUTI
site 00A7D   ; OUT (C),A
site 00A7F   ; OUTI
site 00A82   ; OUT (C),A
site 00A84   ; OUTI
site 00A87   ; OUT (C),A
site 00A89   ; OUTI
site 00A8C   ; OUT (C),A
site 00A8E   ; OUTI
site 00A91   ; OUT (C),A
site 00D3E   ; IN A,($BF)
site 00D59   ; OUT ($BF),A
site 00D60   ; OUT ($BF),A
site 00D73   ; OUT ($BF),A
site 00D77   ; OUT ($BF),A
site 00DCA   ; IN A,($DD)
site 00DD7   ; IN A,($DC)
site 00EC4   ; OUT ($BF),A
site 00EC7   ; OUT ($BF),A
site 00ECA   ; OUTI
site 00ECC   ; OUTI
site 00ECE   ; OUTI
site 00ED0   ; OUTI
site 00ED2   ; OUTI
site 00ED4   ; OUTI
site 00ED6   ; OUTI
site 00ED8   ; OUTI
site 00EDA   ; OUTI
site 00EDC   ; OUTI
site 00EDE   ; OUTI
site 00EE0   ; OUTI
site 00EE2   ; OUTI
site 00EE4   ; OUTI
site 00EE6   ; OUTI
site 00EE8   ; OUTI
site 00EEA   ; OUTI
site 00EEC   ; OUTI
site 00EEE   ; OUTI
site 00EF0   ; OUTI
site 00EF2   ; OUTI
site 00EF4   ; OUTI
site 00EF6   ; OUTI
site 00EF8   ; OUTI
site 00EFA   ; OUTI
site 00EFC   ; OUTI
site 00EFE   ; OUTI
site 00F00   ; OUTI
site 00F02   ; OUTI
site 00F04   ; OUTI
site 00F06   ; OUTI
site 00F08   ; OUTI
site 00F0A   ; OUTI
site 00F0C   ; OUTI
site 00F0E   ; OUTI
site 00F10   ; OUTI
site 00F12   ; OUTI
site 00F14   ; OUTI
site 00F16   ; OUTI
site 00F18   ; OUTI
site 00F1A   ; OUTI
site 00F1C   ; OUTI
site 00F1E   ; OUTI
site 00F20   ; OUTI
site 00F22   ; OUTI
site 00F24   ; OUTI
site 00F26   ; OUTI
site 00F28   ; OUTI
site 00F3F   ; OUTI
site 00F4E   ; OUT (C),L
site 00F50   ; OUT (C),H
site 00F60   ; OUT (C),L
site 00F62   ; OUT (C),H
site 00F72   ; OUTI
site 00F74   ; OUTI
site 00F76   ; OUTI
site 00F78   ; OUTI
site 00F7A   ; OUTI
site 00F7C   ; OUTI
site 00F7E   ; OUTI
site 00F80   ; OUTI
site 00F82   ; OUTI
site 00F84   ; OUTI
site 00F86   ; OUTI
site 00F88   ; OUTI
site 00F8A   ; OUTI
site 00F8C   ; OUTI
site 00F8E   ; OUTI
site 00F90   ; OUTI
site 00F92   ; OUTI
site 00F94   ; OUTI
site 00F96   ; OUTI
site 00F98   ; OUTI
site 00F9A   ; OUTI
site 00F9C   ; OUTI
site 00F9E   ; OUTI
site 00FA0   ; OUTI
site 00FE1   ; OUT ($BF),A
site 00FE5   ; OUT ($BF),A
site 00FE8   ; OUT ($BE),A
site 01719   ; OUTI
site 0171F   ; OUTI
site 01725   ; OUT (C),E
site 0172B   ; OUT (C),E
site 01792   ; OUT ($BE),A
site 0179A   ; OUT ($BE),A
site 017A0   ; OUT ($BE),A
site 017A5   ; OUT ($BE),A
site 01927   ; OUT ($BF),A
site 0192A   ; OUT ($BF),A
site 01940   ; OUT ($BF),A
site 01943   ; OUT ($BF),A
site 01966   ; OUT ($BF),A
site 01969   ; OUT ($BF),A
site 01A1F   ; OUT ($BF),A
site 01A22   ; OUT ($BF),A
site 01A4C   ; OUT ($BF),A
site 01A52   ; OUT ($BF),A
site 01A7F   ; OUT ($BF),A
site 01A85   ; OUT ($BF),A
site 01AA4   ; OUT ($BE),A
site 01AAA   ; OUT ($BE),A
site 01AB0   ; OUT ($BE),A
site 01AB5   ; OUT ($BE),A
site 01ABA   ; OUT ($BE),A
site 01AC0   ; OUT ($BE),A
site 01AC6   ; OUT ($BE),A
site 01ACB   ; OUT ($BE),A
site 01AD0   ; OUT ($BE),A
site 01AD6   ; OUT ($BE),A
site 01ADC   ; OUT ($BE),A
site 01AE1   ; OUT ($BE),A
site 01AE6   ; OUT ($BE),A
site 01AEC   ; OUT ($BE),A
site 01AF2   ; OUT ($BE),A
site 01AF7   ; OUT ($BE),A
site 01AFC   ; OUT ($BE),A
site 01B02   ; OUT ($BE),A
site 01B08   ; OUT ($BE),A
site 01B0D   ; OUT ($BE),A
site 01B12   ; OUT ($BE),A
site 01B18   ; OUT ($BE),A
site 01B1E   ; OUT ($BE),A
site 01B23   ; OUT ($BE),A
site 01B28   ; OUT ($BE),A
site 01B2E   ; OUT ($BE),A
site 01B34   ; OUT ($BE),A
site 01B39   ; OUT ($BE),A
site 01B3E   ; OUT ($BE),A
site 01B44   ; OUT ($BE),A
site 01B4A   ; OUT ($BE),A
site 01B4F   ; OUT ($BE),A
site 03E91   ; OUT ($BE),A
site 03E96   ; OUT ($BE),A
site 03ED6   ; OUT ($BE),A
site 03EDB   ; OUT ($BE),A
site 03EF7   ; IN A,($DC)
site 03F00   ; IN A,($DD)
site 03F12   ; IN A,($DC)
site 05442   ; IN A,($DC)
site 05447   ; IN A,($DD)
site 05B3F   ; OUT ($BE),A
site 05B47   ; OUT ($BE),A
site 05BC4   ; OUT ($BE),A
site 06619   ; OUT ($7F),A
site 0663D   ; OUT ($7F),A
site 06661   ; OUT ($7F),A
site 0667C   ; OUT ($7F),A
site 06689   ; OUT ($7F),A
site 06695   ; OUT ($7F),A
site 066A4   ; OUT ($7F),A
site 067FC   ; OUT ($BF),A
site 06803   ; OUT ($BF),A
site 06808   ; OUT ($BF),A
site 0680F   ; OUT ($BF),A
site 06823   ; OUT ($BF),A
site 0682A   ; OUT ($BF),A
site 06830   ; OUTI
site 06839   ; OUT (C),B
site 0683D   ; OUT (C),B
site 06840   ; OUT ($BE),A
site 06854   ; OUTI
site 06865   ; OUT (C),B
site 0686F   ; OUTI
site 06871   ; OUTI
site 06873   ; OUTI
site 06875   ; OUTI
site 06877   ; OUTI
site 06879   ; OUTI
site 0687B   ; OUTI
site 0687D   ; OUTI
site 0687F   ; OUTI
site 06881   ; OUTI
site 06883   ; OUTI
site 06885   ; OUTI
site 06887   ; OUTI
site 06889   ; OUTI
site 0688B   ; OUTI
site 0688D   ; OUTI
site 0688F   ; OUTI
site 06891   ; OUTI
site 06893   ; OUTI
site 06895   ; OUTI
site 06897   ; OUTI
site 06899   ; OUTI
site 0689B   ; OUTI
site 0689D   ; OUTI
site 0689F   ; OUTI
site 068A1   ; OUTI
site 068A3   ; OUTI
site 068A5   ; OUTI
site 068A7   ; OUTI
site 068A9   ; OUTI
site 068AB   ; OUTI
site 068AD   ; OUTI
site 14413   ; OUT ($7F),A
site 14416   ; OUT ($7F),A
site 1441A   ; OUT ($7F),A
site 1441D   ; OUT ($7F),A
site 14421   ; OUT ($7F),A
site 14424   ; OUT ($7F),A
site 14427   ; OUT ($7F),A
site 1443A   ; OUTI
site 1443C   ; OUTI
site 1443E   ; OUTI
site 14455   ; OUTI
site 14457   ; OUTI
site 14459   ; OUTI
site 14467   ; OUT ($7F),A
site 1446B   ; OUT ($7F),A
site 1446F   ; OUT ($7F),A
site 15D80   ; OTIR
site 15DD6   ; OUT ($7F),A
site 15DE5   ; OUT ($7F),A
site 15E00   ; OUT ($7F),A
site 15E10   ; OUT ($7F),A
site 15E17   ; OUT ($7F),A
site 15E1E   ; OUT ($7F),A
site 06813   ; OUT ($BF),A (VRAM write address routine at $6812, no caller found)
site 06818   ; OUT ($BF),A
mapldk 003FB   # LD HL,$FFFD; LD (HL),$00
maphl 00405   # LD (HL),$01, HL = $FFFE
maphl 00408   # LD (HL),$02, HL = $FFFF
mapst 006CE   ; LD ($FFFF),A
mapst 006F8   ; LD ($FFFF),A
mapst 007A9   ; LD ($FFFF),A
mapst 007D0   ; LD ($FFFF),A
mapst 007E1   ; LD ($FFFF),A
mapst 008B9   ; LD ($FFFF),A
mapst 0094C   ; LD ($FFFF),A
mapst 00AA4   ; LD ($FFFF),A
mapst 00E96   ; LD ($FFFF),A
mapst 00E9D   ; LD ($FFFF),A
mapst 01003   ; LD ($FFFF),A
maphl 0104C   # LD (HL),$05, HL = $FFFF
mapst 01053   ; LD ($FFFF),A
maphl 0105B   # LD (HL),$05, HL = $FFFF
maphl 01068   # LD (HL),$05, HL = $FFFF
mapst 01156   ; LD ($FFFF),A
mapst 016FC   ; LD ($FFFF),A
mapst 01736   ; LD ($FFFF),A
mapst 01774   ; LD ($FFFF),A
mapst 01923   ; LD ($FFFF),A
mapst 01933   ; LD ($FFFF),A
mapst 01999   ; LD ($FFFF),A
mapst 01A32   ; LD ($FFFF),A
mapst 02C21   ; LD ($FFFF),A
mapst 02C3F   ; LD ($FFFF),A
mapst 03F4A   ; LD ($FFFF),A
mapst 03FAC   ; LD ($FFFF),A
mapst 03FB0   ; LD ($FFFC),A
mapst 03FD1   ; LD ($FFFC),A
mapst 055CB   ; LD ($FFFF),A
mapst 056C3   ; LD ($FFFF),A
mapst 058FB   ; LD ($FFFF),A
mapst 05AAC   ; LD ($FFFF),A
mapst 05AEA   ; LD ($FFFF),A
mapld 068B3   # LD HL,$FFFF; LD (HL),$05
label cv_m1062 06B80
label cv_m106d 06B88
label cv_m117a 06B90
label cv_m1197 06BA0
label cv_halt  06BB0
asm 0105D 7   ; PUSH AF; CALL $9D0E; POP AF; LD (HL),A; RET with HL = $FFFF
    push af
    call $9D0E
    jp cv_m1062
endasm
asm 0106A 5   ; CALL $9D11; LD (HL),A; RET with HL = $FFFF
    jp cv_m106d
endasm
asm 0117A 5   ; INC (IX+$00) with IX = $FFFF; JR $1163
    jp cv_m117a
endasm
asm 01197 4   ; INC (IX+$00) with IX = $FFFF; RET
    jp cv_m1197
endasm
asm 06B80 8   ; filler: cave for $1062
    pop af
    rst $00
    db $13, $FF       ; LD ($FFFF),A
    ret
endasm
asm 06B88 8   ; filler: cave for $106D
    call $9D11
    rst $00
    db $13, $FF       ; LD ($FFFF),A
    ret
endasm
asm 06B90 16  ; filler: cave for $117A
    push af
    ld a,($FFFF)
    inc a
    rst $00
    db $13, $FF       ; LD ($FFFF),A
    pop af
    jp $1163
endasm
asm 06BA0 16  ; filler: cave for $1197
    push af
    ld a,($FFFF)
    inc a
    rst $00
    db $13, $FF       ; LD ($FFFF),A
    pop af
    ret
endasm
eihalt 00873   ; EI; HALT of the speed test
asm 00875 9   ; HALT; SUB A; LD D,A; LD E,A; LD HL,$C8A0; HALT; LD (HL),A
    jp cv_halt
endasm
asm 06BB0 16  ; filler: cave for $0875
    rst $00
    db halt_io
    sub a
    ld d,a
    ld e,a
    ld hl,$C8A0
    rst $00
    db halt_io
    ld (hl),a
    jp $087E
endasm
asm 03E57 4   ; EI; HALT; DJNZ $3E58: B frames
h3e57:
    rst $00
    db eihalt_io
    djnz h3e57
endasm
asm 03E66 4   ; EI; HALT; DJNZ $3E67: B frames
h3e66:
    rst $00
    db eihalt_io
    djnz h3e66
endasm
eihalt 055A7
eihalt 056F0
asm 01A94 8   ; LD ($C889),SP; SET 1,(IY+$05): the sprite loop at $1A9C-$1B5E runs in page 0
    rst $00
    db far_io, pg_spr, ent_spr
    ret
endasm
asm 009E3 5   ; ADD HL,DE; EXX; LD A,L; OUT ($BF),A: the loop at $09E3-$0A15 runs in page 0
    rst $00           ; entered at $09E3 (CALL NZ,$09E3 at $0986 and $0996) and after the EXX at $09E2
    db far_io, pg_sat, ent_sat
    nop
endasm
asm 00A6B 5   ; OUTI; NOP; OUT (C),A; ...: the 8 cells at $0A6B-$0A92 run in page 0
    rst $00
    db far_io, pg_nmr, ent_nmr
    ret
endasm
asm 00EAA 6   ; LD HL,$D884; LD DE,$0010: the name table copy at $0EAA-$0F48 runs in page 0
    rst $00
    db far_io, pg_nts, ent_nts
    ret
    nop
endasm
# Gauntlet (Europe, Brazil).cht, "Infinite Health P1": RAM $C80F is the low two digits of
# player 1's health (BCD, high digits in $C810); held at 99 the health never falls below
# the hundred it is in
poke "Infinite health"
ar 00C8-0F99
endpoke

# Gauntlet (Europe, Brazil).cht, "Infinite Potion": RAM $C80E is player 1's potion count;
# held at 1 a use of a potion does not lower it
poke "Infinite potions"
ar 00C8-0E01
endpoke

# Gauntlet (Europe, Brazil).cht, "P1 Infinite Credits": RAM $C868 is player 1's credit
# count, lowered by each death
poke "Infinite credits P1"
ar 00C8-6803
endpoke
page 0 spr sat nts nmr
; spr: as $1A94-$1B5E. The game's loop points SP at the 8 mask words at $D430 and POPs them
; for each tile it writes; on the Next each OUT ($BE),A there is an RST, whose return address
; lands on the mask word just popped, so from the second tile on the masks are wrong. This
; entry builds the same bytes without the stack and writes them with jt_vwrite.
; In: B = tiles; after EXX, DE = shape bytes, HL = pattern bytes (4 per row, the low byte
; of HL steps with INC L, as the game's code does); the VDP address is set.
; Out: as the game's code: B = 0, the other set's DE and HL past the last tile, BC = the
; last mask word, A = the last byte written, Z set, carry clear, ($C889) = the SP at the site.
spr:    ld (sp_m),hl
        ld (sp_m+2),de
        ld (sp_m+4),bc
        ld a,b
        ld (sp_n),a
        ld (sp_cnt),a
        ld hl,6
        add hl,sp
        ld ($C889),hl
        push ix
        push iy
        exx
        ld ix,sp_buf
sp_pass: ld iy,$D430
        ld a,7
        ld (sp_r),a
sp_row: ld c,(iy+0)
        ld b,(iy+1)
        inc iy
        inc iy
        ld a,(de)
        and c
        or (hl)
        ld (ix+0),a
        inc l
        ld a,(de)
        and b
        or (hl)
        ld (ix+1),a
        ld a,(sp_r)
        or a
        jr z,sp_last
        inc e
        inc l
        ld a,(hl)
        inc l
        ld (ix+2),a
        ld a,(hl)
        inc l
        ld (ix+3),a
        ld bc,4
        add ix,bc
        ld a,(sp_r)
        dec a
        ld (sp_r),a
        jr sp_row
sp_last: inc de
        inc l
        ld a,(hl)
        inc l
        ld (ix+2),a
        ld a,(hl)
        inc hl
        ld (ix+3),a
        ld (sp_lb),a
        ld bc,4
        add ix,bc
        ld a,(sp_n)
        dec a
        ld (sp_n),a
        jr nz,sp_pass
        ld bc,($D43E)
        push de
        push hl
        push bc
        call sp_put
        pop bc
        pop hl
        pop de
        exx
        ld hl,(sp_m)
        ld de,(sp_m+2)
        ld bc,(sp_m+4)
        ld b,0
        pop iy
        pop ix
        xor a
        ld a,(sp_lb)
        ret
; sp_put: writes the sp_cnt tiles of sp_buf to VRAM from vdp_addr. A tile that equals its
; bytes in the VRAM copy is not written again (the runtime converts every tile it is given, about
; 10,000 cycles each); the tiles that differ go in runs of tiles one after the other. With
; interrupts on, or an address not at a tile's start, it writes them all.
; Runtime internals used: jt_vwrite, cur_mmu, vdp_addr, vdp_rbuf, vdp_code, vdp_latch and
; SHADOW_PAGE 28-29 (the VRAM copy, mapped into slot 0 while a tile is compared).
sp_put: ld de,(vdp_addr)
        ld a,i
        jp pe,sp_all            ; interrupts on
        ld a,e
        and $1F
        jr nz,sp_all
        xor a
        ld (sp_rn),a
        ld hl,sp_buf
        ld a,(sp_cnt)
        ld b,a
sp_t:   push bc
        call sp_cmp
        pop bc
        jr z,sp_same
        ld a,(sp_rn)
        or a
        jr nz,sp_add
        ld (sp_rh),hl
        ld (sp_rv),de
sp_add: inc a
        ld (sp_rn),a
        jr sp_nx
sp_same: call sp_flush
sp_nx:  push bc
        ld bc,32
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        pop bc
        djnz sp_t
        call sp_flush
        ld a,d                  ; the VDP state after the game's writes
        and $3F
        ld d,a
        ld (vdp_addr),de
        dec hl
        ld a,(hl)
        ld (vdp_rbuf),a
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ret
sp_all: ld hl,sp_buf
        ld a,(sp_cnt)
        ld c,a
        ld b,32
        ld ix,32
        ld iy,32
        ld a,1
        jp jt_vwrite
; the run of differing tiles so far, if any
sp_flush: ld a,(sp_rn)
        or a
        ret z
        push hl
        push de
        push bc
        ld c,a
        ld b,32
        ld hl,(sp_rh)
        ld de,(sp_rv)
        ld ix,32
        ld iy,32
        ld a,1
        call jt_vwrite
        xor a
        ld (sp_rn),a
        pop bc
        pop de
        pop hl
        ret
; HL = 32 bytes, DE = their VRAM address (bits 14-15 ignored): Z when the VRAM copy holds them.
; Keeps HL and DE.
sp_cmp: push hl
        push de
        ld a,d
        and $3F
        ld d,a
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a
        ld a,d
        and $1F
        ld d,a
        ld b,32
sp_c1:  ld a,(de)
        cp (hl)
        jr nz,sp_c2
        inc hl
        inc de
        djnz sp_c1
sp_c2:  ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 (flags kept)
        pop de
        pop hl
        ret
sp_rn:  db 0
sp_rh:  dw 0
sp_rv:  dw 0
;
; sat: as $09E3-$0A15. The game writes 6 groups of 5 bytes, each byte with its own address
; written to the control port: 30 bytes cost about two thirds of a frame through the runtime.
; In: this set's HL + DE = the first source byte, B = the bytes (30); the other set's HL = VRAM
; address of the first group (H with the write code), B = the address step inside a group
; (added to the low byte only), DE = the step from group to group.
; Out: as the game's code: this set's HL past the last byte and B = 0, the other
; set's HL past the last group, A = the low byte of the last address, Z set. The entry returns
; to the RET at $0A15 (the return address after the site is replaced).
sat:    add hl,de
        ld (st_x),hl
        ld (st_x+2),de
        ld (st_x+4),bc
        exx
        ld (st_y),hl
        ld (st_y+2),de
        ld (st_y+4),bc
        exx
        ld hl,4
        add hl,sp
        ld (hl),$15
        inc hl
        ld (hl),$0A
        push ix
        push iy
st_grp: ld de,(st_y)
        ld a,(st_y+5)
        ld c,a
        add a,a
        add a,a
        add a,e
        ld (st_a),a
        ld a,c
        cp $40
        jr nc,st_one
        add a,a
        add a,a
        add a,e
        jr c,st_one
        ld hl,(st_x)            ; no wrap of the low byte: one call, 5 runs of one byte
        ld b,1
        ld c,5
        ld ix,1
        ld iyh,0
        ld a,(st_y+5)
        ld iyl,a
        xor a
        call jt_vwrite
        jr st_next
st_one: ld a,5                  ; the low byte wraps: one call for each byte
        ld (st_k),a
        ld hl,(st_x)
        ld de,(st_y)
st_1:   push hl
        push de
        ld b,1
        ld c,1
        ld ix,1
        ld iy,1
        xor a
        call jt_vwrite
        pop de
        pop hl
        inc hl
        ld a,(st_y+5)
        add a,e
        ld e,a
        ld a,(st_k)
        dec a
        ld (st_k),a
        jr nz,st_1
st_next: ld hl,(st_x)
        ld bc,5
        add hl,bc
        ld (st_x),hl
        ld hl,(st_y)
        ld de,(st_y+2)
        add hl,de
        ld (st_y),hl
        ld a,(st_x+5)
        sub 5
        ld (st_x+5),a
        jr nz,st_grp
        pop iy
        pop ix
        exx
        ld hl,(st_y)
        ld de,(st_y+2)
        ld bc,(st_y+4)
        exx
        ld hl,(st_x)
        ld de,(st_x+2)
        ld bc,(st_x+4)
        xor a
        ld a,(st_a)
        ret
st_x:   ds 6
st_y:   ds 6
st_a:   db 0
st_k:   db 0
;
; nts: as $0EAA-$0F48, called only from $0E18 in the frame handler. The game copies 25 rows of
; 48 bytes (24 cells) from $D884 (64 bytes a row) to the name table at $3800, with an address
; write for each row. The entry compares each row with the VRAM copy and writes only the rows
; that differ, from the first to the last cell that differs: one jt_vwrite for each row, or for
; rows one after the other with the same span (a scroll changes them all). It leaves the VDP
; state as the game's writes would.
; Runtime internals used: jt_vwrite, cur_mmu, vdp_addr, vdp_rbuf, vdp_code, vdp_latch and
; SHADOW_PAGE+1 = 29 (VRAM $2000-$3FFF of the VRAM copy, mapped into slot 0 while it compares).
; Out: as the game's code: the sets swapped; this set HL = $7E40, DE = $0040, B = 0; the other
; set HL = $DEC4, DE = $0010, BC = $00BE; A = $7E; interrupts off (the game's $6806 runs DI).
nts:    di
        exx
        ld a,c
        ld (nt_c),a
        exx
        push ix
        push iy
        ld a,29                 ; SHADOW_PAGE+1: VRAM $2000-$3FFF in slot 0
        db $ED,$92,$50          ; nextreg $50,a
        ld hl,$D884             ; each row: the first and the last byte that differs
        ld de,$1800             ; from the VRAM copy, widened to whole cells
        ld ix,nt_s
        ld a,25
nt_row: ld (nt_n),a
        push hl
        push de
        ld b,48
nt_f:   ld a,(de)
        cp (hl)
        jr nz,nt_fd
        inc hl
        inc de
        djnz nt_f
        ld (ix+1),0             ; the same row: no write
        jr nt_rn
nt_fd:  ld a,48
        sub b
        and $FE
        ld (ix+0),a             ; the first byte
        pop de
        pop hl
        push hl
        push de
        ld a,47                 ; no carry: rows start at $x04, $x44, $x84, $xC4 in RAM and
        add a,l                 ; $x00, $x40, $x80, $xC0 in the copy
        ld l,a
        ld a,47
        add a,e
        ld e,a
        ld b,48
nt_b:   ld a,(de)
        cp (hl)
        jr nz,nt_bd
        dec hl
        dec de
        djnz nt_b
nt_bd:  ld a,b                  ; B - 1 = the last byte that differs
        dec a
        or 1
        inc a                   ; the end of its cell
        sub (ix+0)
        ld (ix+1),a             ; the length
nt_rn:  pop de
        pop hl
        ld bc,64
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        inc ix
        inc ix
        ld a,(nt_n)
        dec a
        jr nz,nt_row
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0
        ld ix,nt_s              ; each row that differs: one call for its span
        ld c,0                  ; C = row
nt_w:   ld a,(ix+1)
        or a
        jr z,nt_wn
        ld b,a                  ; B = the length
        ld d,(ix+0)             ; D = the first byte
        ld e,1                  ; E = rows with this same span, one after the other
        push ix
        push bc
nt_m:   ld a,c
        add a,e
        cp 25
        jr nc,nt_mw
        ld a,(ix+3)
        cp b
        jr nz,nt_mw
        ld a,(ix+2)
        cp d
        jr nz,nt_mw
        inc ix
        inc ix
        inc e
        jr nt_m
nt_mw:  ld a,e
        ld (nt_n),a
        ld l,c                  ; HL = row * 64 + first byte
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld e,d
        ld d,0
        add hl,de
        ex de,hl
        ld hl,$3800
        add hl,de
        push hl
        ld hl,$D884
        add hl,de
        pop de                  ; HL = source, DE = VRAM
        ld a,(nt_n)
        ld c,a
        ld ix,64
        ld iy,64
        xor a
        call jt_vwrite
        pop bc
        pop ix
        ld a,(nt_n)             ; past the rows written
        dec a
        jr z,nt_wn
        ld e,a
nt_ws:  inc ix
        inc ix
        inc c
        dec e
        jr nz,nt_ws
nt_wn:  inc ix
        inc ix
        inc c
        ld a,c
        cp 25
        jr c,nt_w
        ld hl,$3E30             ; the VDP state after the game's 1200 writes
        ld (vdp_addr),hl
        ld a,($DE83)            ; the last byte written: row 24, byte 47
        ld (vdp_rbuf),a
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        pop iy
        pop ix
        ld hl,$DEC4
        ld de,$0010
        ld bc,$00BE
        exx
        ld hl,$7E40
        ld de,$0040
        ld a,(nt_c)
        ld c,a
        ld b,0
        ld a,$7E
        ret
nt_c:   db 0
;
; nmr: as $0A6B-$0A92, called 3 or 4 times a frame from $0A16: 8 name table cells, each the
; tile number from HL and the attribute byte $19 in A, written with OUTI and OUT (C),A after
; the address writes at $0A50 and $0A53. One jt_vwrite writes the same 16 bytes. HL is at
; $9C64 or $9FE4 plus a small offset (bank 4 in slot 2), never in $2000-$3FFF.
; Out: as the game's code: HL + 8, B - 8, A = $19, C = $BE, Z as the last OUTI leaves it.
; Runtime internals used: jt_vwrite and vdp_addr (the address the game wrote).
nmr:    push de
        push ix
        push iy
        ld de,nm_buf
        ld c,8
nm_1:   ld a,(hl)
        inc hl
        ld (de),a
        inc de
        ld a,$19
        ld (de),a
        inc de
        dec c
        jr nz,nm_1
        push hl
        push bc
        ld hl,nm_buf
        ld de,(vdp_addr)
        ld bc,$1001             ; one run of 16 bytes
        ld ix,64
        ld iy,64
        ld a,1
        call jt_vwrite
        pop bc
        pop hl
        pop iy
        pop ix
        pop de
        ld a,b
        sub 8
        ld b,a                  ; Z when B is 0, as after the last OUTI
        ld c,$BE
        ld a,$19
        ret
nm_buf: ds 16
nt_n:   db 0
nt_s:   ds 50
sp_n:   db 0
sp_cnt: db 0
sp_r:   db 0
sp_lb:  db 0
sp_m:   ds 6
sp_buf: ds 32*48            ; the game draws at most $29 tiles in one call
endpage
