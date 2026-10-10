# Sonic The Hedgehog, drafted by tools/mkspec.py from sitescan output.
name Sonic The Hedgehog
cart B519E833
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
# priority tiles (palm leaves in front of item monitors and the HUD) and the
# line-0 palette (Labyrinth: the frame handler's palette upload lands in the
# first picture lines on the Next) (batch 5)
priority
toppal
start 0003
site 00003   ; IN A,($7E)
site 00078   ; IN A,($BF)
site 00096   ; OUT ($BF),A
site 0009A   ; OUT ($BF),A
site 000A1   ; OUT ($BF),A
site 000A5   ; OUT ($BF),A
site 000DB   ; IN A,($DD)
site 000FC   ; OUT ($BF),A
site 00100   ; OUT ($BF),A
site 00107   ; OUT ($BF),A
site 0010B   ; OUT ($BF),A
site 00110   ; OUT ($BF),A
site 00114   ; OUT ($BF),A
site 00127   ; OUT ($BF),A
site 0012B   ; OUT ($BF),A
site 001FE   ; IN A,($7E)
site 00205   ; OUT ($BF),A
site 00209   ; OUT ($BF),A
site 0021B   ; OUT ($BF),A
site 0021F   ; OUT ($BF),A
site 00230   ; OUT ($BE),A
site 00235   ; OUT ($BE),A
site 0023F   ; OUT ($BF),A
site 00243   ; OUT ($BF),A
site 002BA   ; OUT ($BF),A
site 002BE   ; OUT ($BF),A
site 00340   ; OUT ($BF),A
site 00346   ; OUT ($BF),A
site 00356   ; OUT ($BE),A
site 0036B   ; OUT ($BE),A
site 0037A   ; OUT ($BF),A
site 00380   ; OUT ($BF),A
site 00383   ; OUT ($BE),A
site 00388   ; OUT ($BE),A
site 00415   ; OUT ($BF),A
site 0041A   ; OUT ($BF),A
site 0048F   ; OUT ($BE),A
site 00495   ; OUT ($BE),A
site 0049B   ; OUT ($BE),A
site 004A1   ; OUT ($BE),A
site 004C8   ; OUT ($BE),A
site 004CE   ; OUT ($BE),A
site 004D4   ; OUT ($BE),A
site 004DA   ; OUT ($BE),A
site 00503   ; OUT ($BF),A
site 00508   ; OUT ($BF),A
site 00516   ; OUT ($BE),A
site 0051C   ; OUT ($BE),A
site 00534   ; OUT ($BE),A
site 0053A   ; OUT ($BE),A
site 0054A   ; IN A,($BE)
site 0054F   ; IN A,($BE)
site 00558   ; IN A,($BE)
site 0055C   ; IN A,($BE)
site 0058A   ; OUT ($BF),A
site 0058E   ; OUT ($BF),A
site 00592   ; OTIR
site 00597   ; OUT ($BF),A
site 0059C   ; OUT ($BF),A
site 0059F   ; OUT ($BE),A
site 005A7   ; IN A,($DC)
site 005C9   ; OUT ($BF),A
site 005CE   ; OUT ($BF),A
site 005D5   ; OUT ($BE),A
site 005DC   ; OUT ($BE),A
site 009B7   ; OUT ($BF),A
site 009BC   ; OUT ($BF),A
site 009BF   ; OUT ($BE),A
site 009C5   ; OUT ($BE),A
site 009CA   ; OUT ($BE),A
site 009D0   ; OUT ($BE),A
site 009D5   ; OUT ($BE),A
site 009DB   ; OUT ($BE),A
site 009E0   ; OUT ($BE),A
site 009E6   ; OUT ($BE),A
site 00C35   ; OUT ($BF),A
site 00C3A   ; OUT ($BF),A
site 00C3F   ; OUT ($BE),A
site 00C45   ; OUT ($BE),A
site 01F34   ; OUT ($BF),A
site 01F38   ; OUT ($BF),A
site 01F45   ; OUT ($BE),A
site 027EA   ; OUT ($BF),A
site 027ED   ; OUT ($BF),A
site 027F3   ; IN A,($BE)
site 027FB   ; OUT ($BF),A
site 02800   ; OUT ($BF),A
site 02807   ; OUT ($BE),A
site 0388A   ; OUT ($BF),A
site 0388F   ; OUT ($BF),A
site 03894   ; OUT ($BE),A
site 03899   ; OUT ($BE),A
site 0389E   ; OUT ($BE),A
site 038A3   ; OUT ($BE),A
site 03930   ; OUT ($BF),A
site 03935   ; OUT ($BF),A
site 03938   ; OUT ($BE),A
site 0393E   ; OUT ($BE),A
site 03944   ; OUT ($BE),A
site 0394A   ; OUT ($BE),A
site 0C163   ; OTIR
site 0C18A   ; OUT ($7F),A
site 0C40D   ; OUT ($7F),A
site 0C47B   ; OUT ($7F),A
site 0C48D   ; OUT ($7F),A
site 0C4AF   ; OUT ($7F),A
site 0C526   ; OUT ($7F),A
mapst 000C5   ; LD ($FFFE),A
mapsthl 000E3   ; LD ($FFFE),HL
mapst 0012F   ; LD ($FFFE),A
mapst 00137   ; LD ($FFFF),A
mapst 00146   ; LD ($FFFE),A
mapst 0014E   ; LD ($FFFF),A
mapst 00176   ; LD ($FFFE),A
mapst 0017E   ; LD ($FFFF),A
mapst 001A7   ; LD ($FFFE),A
mapst 001AF   ; LD ($FFFF),A
mapst 0028D   ; LD ($FFFC),A
mapst 00292   ; LD ($FFFD),A
mapst 00297   ; LD ($FFFE),A
mapst 0029C   ; LD ($FFFF),A
mapst 002DB   ; LD ($FFFE),A
mapst 002E8   ; LD ($FFFE),A
mapst 002F0   ; LD ($FFFE),A
mapst 002F9   ; LD ($FFFE),A
mapst 00302   ; LD ($FFFE),A
mapst 0030C   ; LD ($FFFE),A
mapst 00426   ; LD ($FFFE),A
mapst 0042D   ; LD ($FFFF),A
mapstde 004EF   ; LD ($FFFE),DE
mapst 006C5   ; LD ($FFFE),A
mapst 006CD   ; LD ($FFFF),A
mapst 00969   ; LD ($FFFE),A
mapst 00971   ; LD ($FFFF),A
mapst 00A42   ; LD ($FFFE),A
mapst 00A4A   ; LD ($FFFF),A
mapst 00ABE   ; LD ($FFFE),A
mapst 00AC6   ; LD ($FFFF),A
mapst 00B70   ; LD ($FFFE),A
mapst 00B78   ; LD ($FFFF),A
mapst 00C20   ; LD ($FFFE),A
mapst 00C4D   ; LD ($FFFE),A
mapst 00CAC   ; LD ($FFFE),A
mapst 00D0E   ; LD ($FFFE),A
mapst 012AE   ; LD ($FFFE),A
mapst 0141E   ; LD ($FFFE),A
mapst 0158D   ; LD ($FFFE),A
mapst 01CEF   ; LD ($FFFE),A
mapst 01D57   ; LD ($FFFE),A
mapst 01D81   ; LD ($FFFE),A
mapst 01D89   ; LD ($FFFF),A
mapst 01DB7   ; LD ($FFFE),A
mapst 01E52   ; LD ($FFFE),A
mapst 01E5A   ; LD ($FFFF),A
mapst 01EB3   ; LD ($FFFE),A
mapst 01ECE   ; LD ($FFFE),A
mapst 01F0E   ; LD ($FFFE),A
mapst 01F16   ; LD ($FFFF),A
mapst 020BA   ; LD ($FFFE),A
mapst 0221E   ; LD ($FFFE),A
mapst 02226   ; LD ($FFFF),A
mapst 02230   ; LD ($FFFE),A
mapst 02238   ; LD ($FFFF),A
mapst 0227F   ; LD ($FFFE),A
mapst 02287   ; LD ($FFFF),A
mapst 022BF   ; LD ($FFFE),A
mapst 022C7   ; LD ($FFFF),A
mapst 022E2   ; LD ($FFFE),A
mapst 025B6   ; LD ($FFFE),A
mapst 025DD   ; LD ($FFFE),A
mapst 02677   ; LD ($FFFE),A
mapst 026C3   ; LD ($FFFE),A
mapst 049E9   ; LD ($FFFF),A
mapst 04A20   ; LD ($FFFF),A
# CHECK ram_exec at 0128E ($128E bank 0): JP NC,$CBFD $CBFD
# CHECK indirect_unresolved at 032E1 ($32E1 bank 0): JP (HL) 
# CHECK bank_unresolved at 03643 ($3643 bank 0): RET $4A28
# CHECK bank_unresolved at 036BD ($36BD bank 0): RET $4A28
# CHECK bank_unresolved at 0522D ($522D bank 1): CALL Z,$91EB $91EB
# CHECK bank_unresolved at 0B7E5 ($B7E5 bank 2): RET $4A28
# (batch 5: real code, the tile copy and RLE routines at $0397-$0404)
site 00399   ; OUT ($BF),A
# was: CHECK low: site 00399  OUT ($BF),A  (vdp_control)
# (batch 5: real code, the tile copy and RLE routines at $0397-$0404)
site 0039E   ; OUT ($BF),A
# was: CHECK low: site 0039E  OUT ($BF),A  (vdp_control)
# (batch 5: real code, the tile copy and RLE routines at $0397-$0404)
site 003A2   ; OUT ($BE),A
# was: CHECK low: site 003A2  OUT ($BE),A  (vdp_data)
# (batch 5: real code, the tile copy and RLE routines at $0397-$0404)
site 003AF   ; OUT ($BF),A
# was: CHECK low: site 003AF  OUT ($BF),A  (vdp_control)
# (batch 5: real code, the tile copy and RLE routines at $0397-$0404)
site 003B4   ; OUT ($BF),A
# was: CHECK low: site 003B4  OUT ($BF),A  (vdp_control)
# (batch 5: real code, the tile copy and RLE routines at $0397-$0404)
site 003D1   ; OUT ($BE),A
# was: CHECK low: site 003D1  OUT ($BE),A  (vdp_data)
# (batch 5: real code, the tile copy and RLE routines at $0397-$0404)
site 003E6   ; OUT ($BE),A
# was: CHECK low: site 003E6  OUT ($BE),A  (vdp_data)
# CHECK low: site 01919  IN A,($DC)  (joypad_a)
# CHECK low: site 01950  IN A,($DC)  (joypad_a)
# CHECK low: site 05DFB  OUT ($DD),A  (no_effect)
# CHECK low: site 08553  OUT ($DD),A  (no_effect)
# CHECK low: site 0A959  OUT ($DD),A  (no_effect)
# CHECK low: site 0B328  OUT ($DD),A  (no_effect)
# CHECK low: site 0BC67  OUT ($DD),A  (no_effect)
# CHECK low: site 0BE43  OUT ($DD),A  (no_effect)
# CHECK low: site 10C5B  OUT ($F2),A  (fm_control)
# CHECK low: site 10D71  OUT ($C1),A  (no_effect)
# CHECK low: site 1274F  IN B,(C)  (port in C)
# CHECK low: site 15299  IN A,($C0)  (joypad_a)
# CHECK low: site 161B8  IN A,($DC)  (joypad_a)
# CHECK low: site 161D4  IN A,($DC)  (joypad_a)
# CHECK low: site 16251  IN A,($DC)  (joypad_a)
# CHECK low: site 27BBD  OUT ($F1),A  (fm_data)
# CHECK low: site 281B0  IN A,($C0)  (joypad_a)
# CHECK low: site 2B286  IN A,($BD)  (vdp_status)
# CHECK low: site 2C225  OUT ($7F),A  (psg)
# CHECK low: site 2C573  OUT ($F1),A  (fm_data)
# CHECK low: site 2C5ED  IN A,($F1)  (joypad_b_misc)
# CHECK low: site 2D154  IN A,($DC)  (joypad_a)
# CHECK low: site 2D338  IN A,($BD)  (vdp_status)
# CHECK low: site 2E57A  IN A,($BF)  (vdp_status)
# CHECK low: site 2E772  IN A,($F1)  (joypad_b_misc)
# CHECK low: site 2FC09  IN A,($C0)  (joypad_a)
# CHECK low: site 3022F  OUT ($F1),A  (fm_data)
# CHECK low: site 30905  IN A,($C0)  (joypad_a)
# CHECK low: site 31386  OUT ($C0),A  (no_effect)
# CHECK low: site 332F7  IN A,($F1)  (joypad_b_misc)
# CHECK low: site 342CF  IN A,($7F)  (h_counter)
# CHECK low: site 348F3  IN A,($F1)  (joypad_b_misc)
# CHECK low: site 34907  IN A,($F1)  (joypad_b_misc)
# CHECK low: site 34AA9  OUT ($F2),A  (fm_control)
# CHECK low: site 34AB9  IN A,($F2)  (fm_detect)
# CHECK low: site 34C00  IN A,($F2)  (fm_detect)
# CHECK low: site 34C02  IN A,($F2)  (fm_detect)
# CHECK low: site 34C04  IN A,($F1)  (joypad_b_misc)
# CHECK low: site 34DFC  OUT ($BD),A  (vdp_control)
# CHECK low: site 35918  IN A,($C0)  (joypad_a)
# CHECK low: site 35BBC  IN A,($C0)  (joypad_a)
# CHECK low: site 37157  IN A,($BD)  (vdp_status)
# CHECK low: site 373DC  IN A,($DC)  (joypad_a)
# CHECK low: site 376A4  OUT ($F2),A  (fm_control)
# CHECK low: site 379DF  OTIR  (port in C)
# CHECK low: site 38E66  OUT ($F1),A  (fm_data)
# CHECK low: site 39E73  IN A,($DC)  (joypad_a)
# CHECK low: site 3A04D  IN A,($F1)  (joypad_b_misc)
# CHECK low: site 3ADB2  IN A,($BE)  (vdp_data)
# CHECK low: site 3B43B  OUT ($F1),A  (fm_data)
# CHECK low: site 3C2C8  OUT ($C0),A  (no_effect)
# CHECK low: site 3CAD1  IN A,($DC)  (joypad_a)
# CHECK low: site 3D5A0  IN A,($7F)  (h_counter)
# CHECK low: site 3DD05  OUT ($F1),A  (fm_data)
# CHECK low: site 3DD0C  OUT ($F1),A  (fm_data)
# CHECK low: site 3DD0E  OUT ($F1),A  (fm_data)
# CHECK low: site 3EDEE  IN A,($BE)  (vdp_data)
# CHECK low: site 3F15C  IN A,($DC)  (joypad_a)
# batch 5: the mapper stores of the routines at $0397-$0404 (missed by the
# scanner; unpatched they wrote the framework's register copies only)
mapst 003BC   ; LD ($FFFE),A
mapst 003C3   ; LD ($FFFF),A
mapst 003FC   ; LD ($FFFE),A
mapst 00400   ; LD ($FFFF),A
# Byte scan hits left out: they decode as data (RST and NOP runs, no valid
# code after them, or no code leading to them).
# not patched (data): mapst 07681  LD ($FFFF),A  (no valid code after it)
# not patched (data): mapst 2C9EE  LD ($FFFE),A  (6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# The frame handler's VRAM uploads, as native code in page 0. The game runs them with
# interrupts off between its frame event and its EI at $00C2. Through the I/O traps they
# took about 210 lines of the Next's 311 while Sonic ran fast, so the framework's vertical
# blank work waited for that EI and ran inside the next picture, where its copper update
# and direct X scroll write tore the picture across (palm trunks broken sideways).
# Name table column ($082F-$0843): 25 cells, one control write and two OUTI each, from
# $D180 to VRAM HL' (alternate HL, with bit 14) and 64 bytes on, wrapping from row 28 to
# row 0.
asm 0082F 21
    rst $00
    db far_io, pg_colw, ent_colw
    jp $0844
endasm
# Name table row ($08A5-$08CE; the RET at $08CF stays, $0855 jumps to it): 31 cells from
# HL to VRAM DE (with bit 14), wrapping to the row's start ($D20E) at column 32.
asm 008A5 42
    rst $00
    db far_io, pg_roww, ent_roww
    ret
endasm
# Sonic's sprite tiles ($37EF-$3878): 96 lines of 3 bytes from HL with a fourth byte 0,
# to VRAM $3680; bit 0 of (IY+6) reads the lines bottom up.
asm 037EF 138
    rst $00
    db far_io, pg_artw, ent_artw
    ret
endasm
page 0 colw roww artw
; colw: as the game's loop at $082F-$0843. Leaves HL = $D180 source + 50, B = 0,
; C = $BE, DE and the alternate registers as they were.
colw:   push de
        push ix
        push iy
        exx
        push hl                 ; HL' = the first cell's VRAM address
        exx
        pop de
        ld a,d                  ; row = (address - $3800) / 64
        and $07
        add a,a
        add a,a
        ld b,a
        ld a,e
        rlca
        rlca
        and $03
        add a,b
        ld b,a
        ld a,28                 ; cells before the wrap at row 28
        sub b
        cp 25
        jr c,.n1
        ld a,25
.n1:    ld c,a
        ld b,2
        ld ix,2
        ld iy,64
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,25
        sub c
        jr z,.done
        push hl                 ; the rest from row 0
        ld b,0
        add hl,bc
        add hl,bc
        ld c,a
        ld a,e
        and $3F
        ld e,a
        ld d,$38
        ld b,2
        xor a
        call jt_vwrite
        pop hl
.done:  pop iy
        pop ix
        pop de
        ld bc,50
        add hl,bc
        ld bc,$00BE
        ret
; roww: as the game's code at $08A5-$08CE. Leaves HL = source + 62, B = 0, C = $BE.
roww:   push de
        push ix
        push iy
        ld a,e
        and $3F
        ld b,a
        ld a,64                 ; bytes up to the row's end
        sub b
        cp 62
        jr c,.n1
        ld a,62
.n1:    ld b,a
        ld c,1
        ld ix,0
        ld iy,0
        xor a
        call jt_vwrite
        ld a,62
        sub b
        jr z,.done
        push hl                 ; the rest from the row's start
        ld c,b
        ld b,0
        add hl,bc
        ld b,a
        ld c,1
        ld a,($D20E)
        ld e,a
        xor a
        call jt_vwrite
        pop hl
.done:  pop iy
        pop ix
        pop de
        ld bc,62
        add hl,bc
        ld bc,$00BE
        ret
; artw: as the game's code at $37EF-$3878, HL = the tiles' source. Builds the 384
; bytes in artbuf and writes them with one call. Leaves A = 0, HL = ($D28F).
artw:   push ix
        push iy
        ld de,artbuf
        ld b,96
        bit 0,(iy+6)
        jr nz,.flip
.n:     ldi
        ldi
        ldi
        inc bc                  ; LDI counts BC down; B is the line count
        inc bc
        inc bc
        xor a
        ld (de),a
        inc de
        djnz .n
        jr .up
.flip:  push bc
        ld bc,$011D
        add hl,bc
        pop bc
.f:     ldi
        ldi
        ldi
        inc bc
        inc bc
        inc bc
        xor a
        ld (de),a
        inc de
        push bc
        ld bc,-6
        add hl,bc
        pop bc
        djnz .f
.up:    ld hl,artbuf
        ld de,$3680
        ld bc,$C002             ; 2 runs of 192 bytes
        ld ix,192
        ld iy,192
        ld a,1                  ; the source as mapped now: this page
        call jt_vwrite
        pop iy
        pop ix
        ld hl,($D28F)
        ld ($D291),hl
        xor a
        ret
artbuf: ds 384
endpage
