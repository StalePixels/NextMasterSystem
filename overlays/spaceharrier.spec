# Space Harrier, CA1D3752, drafted by tools/mkspec.py from sitescan output (with the detector log).
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
name Space Harrier
cart CA1D3752
hz 50		; No-Intro regions Europe
vector 10 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 000FE   ; OUT ($DF),A
site 00101   ; OUT ($DE),A
site 00103   ; IN A,($DE)
site 00161   ; OUT ($BF),A
site 00165   ; OUT ($BF),A
site 00170   ; IN A,($DD)
# 00451-0046C: the line handler's CRAM writes, replaced by the asm block at 0044A (page 1, sh_gnd)
site 004F4   ; OUT ($3F),A
site 004F6   ; IN A,($DD)
site 00500   ; OUT ($3F),A
site 00502   ; IN A,($DD)
site 0050B   ; OUT ($3F),A
site 00516   ; IN A,($DC)
site 00526   ; OUT ($DE),A
site 00528   ; IN A,($DC)
site 0052D   ; OUT ($DE),A
site 0052F   ; IN A,($DC)
site 00539   ; OUT ($DE),A
site 0053B   ; IN A,($DC)
site 00545   ; OUT ($DE),A
site 00547   ; IN A,($DC)
site 00557   ; OUT ($DE),A
site 00559   ; IN A,($DC)
site 00563   ; OUT ($DE),A
site 00565   ; IN A,($DC)
site 00573   ; OUT ($DE),A
site 0057B   ; OUT ($DE),A
site 0057D   ; IN A,($DC)
site 0058D   ; OUT ($DE),A
site 0058F   ; IN A,($DC)
site 00599   ; OUT ($DE),A
site 0059B   ; IN A,($DC)
site 005A5   ; OUT ($DE),A
site 005A7   ; IN A,($DD)
site 005B1   ; OUT ($DE),A
site 005B3   ; IN A,($DD)
site 005D6   ; IN A,($DC)
site 005DB   ; IN A,($DD)
otir 005ED   ; OUTI
site 005FA   ; OUTI
site 00600   ; OUT (C),A
site 00615   ; OUT ($BE),A
site 0061A   ; OUT ($BE),A
site 00627   ; OUTI
site 0062D   ; OUT (C),A
otir 00640   ; OUTI
site 00663   ; OUT (C),D
site 00676   ; OTIR
site 006B3   ; OUT ($BE),A
site 0070C   ; OUT ($BE),A
site 00A7E   ; OUT ($BE),A
# 00FA8 OUTI loop: replaced by the asm block at 00F99 (page 0, sh_nt)
otir 012A4   ; OUTI
otir 012CD   ; OUTI
otir 016BB   ; OUTI
site 017E3   ; OUT ($BE),A
site 02033   ; OUT (C),A
site 02039   ; OUT (C),A
site 023B2   ; OUTI
site 023B7   ; OUT (C),A
site 04AE6   ; OUTI
site 04AE8   ; OUTI
site 04AEA   ; OUTI
site 04AEC   ; OUTI
site 04AEE   ; OUTI
site 04AF0   ; OUTI
site 04AF2   ; OUTI
site 04AF4   ; OUTI
site 04AF6   ; OUTI
site 04AF8   ; OUTI
site 04AFA   ; OUTI
site 04AFC   ; OUTI
site 04AFE   ; OUTI
site 04B00   ; OUTI
site 04B02   ; OUTI
site 04B04   ; OUTI
site 04B06   ; OUTI
site 04B08   ; OUTI
site 04B0A   ; OUTI
site 04B0C   ; OUTI
site 04B0E   ; OUTI
site 04B10   ; OUTI
site 04B12   ; OUTI
site 04B14   ; OUTI
site 04B16   ; OUTI
site 04B18   ; OUTI
site 04B1A   ; OUTI
site 04B1C   ; OUTI
site 04B1E   ; OUTI
site 04B20   ; OUTI
site 04B22   ; OUTI
site 04B24   ; OUTI
site 04B26   ; OUTI
site 04B28   ; OUTI
site 04B2A   ; OUTI
site 04B2C   ; OUTI
site 04B2E   ; OUTI
site 04B30   ; OUTI
site 04B32   ; OUTI
site 04B34   ; OUTI
site 04B36   ; OUTI
site 04B38   ; OUTI
site 04B3A   ; OUTI
site 04B3C   ; OUTI
site 04B3E   ; OUTI
site 04B40   ; OUTI
site 04B42   ; OUTI
site 04B44   ; OUTI
site 04B46   ; OUTI
site 04B48   ; OUTI
site 04B4A   ; OUTI
site 04B4C   ; OUTI
site 04B4E   ; OUTI
site 04B50   ; OUTI
site 04B52   ; OUTI
site 04B54   ; OUTI
site 04B56   ; OUTI
site 04B58   ; OUTI
site 04B5A   ; OUTI
site 04B5C   ; OUTI
site 04B5E   ; OUTI
site 04B60   ; OUTI
site 04B62   ; OUTI
site 04B64   ; OUTI
site 04B66   ; OUTI
site 04B68   ; OUTI
site 04B6A   ; OUTI
site 04B6C   ; OUTI
site 04B6E   ; OUTI
site 04B70   ; OUTI
site 04B72   ; OUTI
site 04B74   ; OUTI
site 04B76   ; OUTI
site 04B78   ; OUTI
site 04B7A   ; OUTI
site 04B7C   ; OUTI
site 04B7E   ; OUTI
site 04B80   ; OUTI
site 04B82   ; OUTI
site 04B84   ; OUTI
site 04B86   ; OUTI
site 04B88   ; OUTI
site 04B8A   ; OUTI
site 04B8C   ; OUTI
site 04B8E   ; OUTI
site 04B90   ; OUTI
site 04B92   ; OUTI
site 04B94   ; OUTI
site 04B96   ; OUTI
site 04B98   ; OUTI
site 04B9A   ; OUTI
site 04B9C   ; OUTI
site 04B9E   ; OUTI
site 04BA0   ; OUTI
site 04BA2   ; OUTI
site 04BA4   ; OUTI
site 04BA6   ; OUTI
site 04BA8   ; OUTI
site 04BAA   ; OUTI
site 04BAC   ; OUTI
site 04BAE   ; OUTI
site 04BB0   ; OUTI
site 04BB2   ; OUTI
site 04BB4   ; OUTI
site 04BB6   ; OUTI
site 04BB8   ; OUTI
site 04BBA   ; OUTI
site 04BBC   ; OUTI
site 04BBE   ; OUTI
site 04BC0   ; OUTI
site 04BC2   ; OUTI
site 04BC4   ; OUTI
site 04BC6   ; OUTI
site 04BC8   ; OUTI
site 04BCA   ; OUTI
site 04BCC   ; OUTI
site 04BCE   ; OUTI
site 04BD0   ; OUTI
site 04BD2   ; OUTI
site 04BD4   ; OUTI
site 04BD6   ; OUTI
site 04BD8   ; OUTI
site 04BDA   ; OUTI
site 04BDC   ; OUTI
site 04BDE   ; OUTI
site 04BE0   ; OUTI
site 04BE2   ; OUTI
site 04BE4   ; OUTI
site 04E5E   ; OUTI
site 04E60   ; OUTI
site 04E62   ; OUTI
site 04E64   ; OUT ($BE),A
site 04E66   ; OUTI
site 04E68   ; OUTI
site 04E6A   ; OUTI
site 04E6C   ; OUT ($BE),A
site 04E6E   ; OUTI
site 04E70   ; OUTI
site 04E72   ; OUTI
site 04E74   ; OUT ($BE),A
site 04E76   ; OUTI
site 04E78   ; OUTI
site 04E7A   ; OUTI
site 04E7C   ; OUT ($BE),A
site 04E7E   ; OUTI
site 04E80   ; OUTI
site 04E82   ; OUTI
site 04E84   ; OUT ($BE),A
site 04E86   ; OUTI
site 04E88   ; OUTI
site 04E8A   ; OUTI
site 04E8C   ; OUT ($BE),A
site 04E8E   ; OUTI
site 04E90   ; OUTI
site 04E92   ; OUTI
site 04E94   ; OUT ($BE),A
site 04E96   ; OUTI
site 04E98   ; OUTI
site 04E9A   ; OUTI
site 04E9C   ; OUT ($BE),A
site 050AC   ; OUT ($BE),A
site 050B1   ; OUT ($BE),A
site 055D3   ; OUT ($7F),A
site 056B6   ; OUT ($7F),A
site 056F8   ; OUT ($7F),A
site 0573C   ; OUT ($7F),A
site 059DD   ; OUT ($7F),A
site 05A3A   ; OUT ($7F),A
site 05A3E   ; OUT ($7F),A
site 05A64   ; OUT ($7F),A
site 05AD2   ; OUT ($7F),A
site 05AF2   ; OTIR
site 07ECE   ; OUT ($7F),A
site 07EDE   ; OUT ($7F),A
site 07EE2   ; OUT ($7F),A
site 07EE6   ; OUT ($7F),A
# CHECK mapper at 00083 ($0083 bank 0): LD (HL),$80 $FFFC<-$80
# CHECK mapper at 00086 ($0086 bank 0): LD (HL),$00 $FFFD<-$00
# CHECK mapper at 00089 ($0089 bank 0): LD (HL),$01 $FFFE<-$01
# CHECK mapper at 0008C ($008C bank 0): LD (HL),$02 $FFFF<-$02
mapldk 00080   # loads HL with $FFFC, then stores $80 through it
maphl 00086   # LD (HL),$00, HL = $FFFD
maphl 00089   # LD (HL),$01, HL = $FFFE
maphl 0008C   # LD (HL),$02, HL = $FFFF
mapst 001B1   ; LD ($FFFF),A
mapld 003D4   # loads HL with $FFFF, then stores $03 through it
mapst 00444   ; LD ($FFFF),A
mapst 006CE   ; LD ($FFFF),A
mapld 00BF9   # loads HL with $FFFF, then stores $03 through it
mapld 00C68   # loads HL with $FFFF, then stores $03 through it
mapld 00E17   # loads HL with $FFFF, then stores $02 through it
mapld 01002   # loads HL with $FFFF, then stores $08 through it
mapld 01010   # loads HL with $FFFF, then stores $0F through it
mapld 0121D   # loads HL with $FFFF, then stores $02 through it
mapld 01385   # loads HL with $FFFF, then stores $02 through it
mapld 013EA   # loads HL with $FFFF, then stores $02 through it
mapld 01498   # loads HL with $FFFF, then stores $02 through it
mapld 01697   # loads HL with $FFFF, then stores $02 through it
mapld 01765   # loads HL with $FFFF, then stores $0F through it
mapld 01801   # loads HL with $FFFF, then stores $02 through it
mapld 019FC   # loads HL with $FFFF, then stores $07 through it
mapld 01E3B   # loads HL with $FFFF, then stores $06 through it
mapld 01E8D   # loads HL with $FFFF, then stores $06 through it
mapld 01EA8   # loads HL with $FFFF, then stores $06 through it
mapld 01EB6   # loads HL with $FFFF, then stores $07 through it
mapld 0228C   # loads HL with $FFFF, then stores $07 through it
mapld 022A5   # loads HL with $FFFF, then stores $06 through it
mapld 0236B   # loads HL with $FFFF, then stores $0D through it
mapld 023D6   # loads HL with $FFFF, then stores $07 through it
mapst 023FC   ; LD ($FFFF),A
mapld 02487   # loads HL with $FFFF, then stores $06 through it
mapld 02495   # loads HL with $FFFF, then stores $07 through it
mapld 024BD   # loads HL with $FFFF, then stores $0F through it
mapld 024DC   # loads HL with $FFFF, then stores $03 through it
mapld 02CB0   # loads HL with $FFFF, then stores $05 through it
mapld 02D92   # loads HL with $FFFF, then stores $02 through it
mapld 0471A   # loads HL with $FFFF, then stores $04 through it
mapld 0477E   # loads HL with $FFFF, then stores $05 through it
mapld 047D4   # loads HL with $FFFF, then stores $04 through it
mapld 04857   # loads HL with $FFFF, then stores $05 through it
mapst 048FA   ; LD ($FFFF),A
mapld 04E2B   # loads HL with $FFFF, then stores $02 through it
mapld 053C0   # loads HL with $FFFF, then stores $04 through it
mapld 053FB   # loads HL with $FFFF, then stores $04 through it
mapld 0542D   # loads HL with $FFFF, then stores $04 through it
mapld 05470   # loads HL with $FFFF, then stores $04 through it
mapld 054F0   # loads HL with $FFFF, then stores $04 through it
mapld 07E6E   # loads HL with $FFFF, then stores $06 through it
mapld 07E93   # loads HL with $FFFF, then stores $06 through it
# CHECK cartarea_store at 01787 ($1787 bank 0): LD (BC),A $0801
# CHECK cartarea_store at 01788 ($1788 bank 0): LD (BC),A $0801
# CHECK cartarea_store at 0178F ($178F bank 0): LD (BC),A $0C01
# CHECK cartarea_store at 01790 ($1790 bank 0): LD (BC),A $0C01
# CHECK cartarea_store at 01798 ($1798 bank 0): LD (BC),A $0101
# CHECK indirect_unresolved at 00154 ($0154 bank 0): JP (HL) 
# CHECK low: site 04FB2  IN A,($DC)  (joypad_a)
# CHECK low: site 05AFE  OUT ($7F),A  (psg)
# CHECK low: site 05B03  OUT ($7F),A  (psg)
# CHECK low: site 0C4E8  OUT ($7E),A  (psg)
# CHECK low: site 0C964  IN A,($3F)  (unmapped_read)
# CHECK low: site 0D8D6  OUT (C),C  (port in C)
# CHECK low: site 1331D  OTIR  (port in C)
# CHECK low: site 193C9  IN A,($7E)  (v_counter)
# CHECK low: site 29590  OUT ($3F),A  (io_control)
# CHECK low: site 2A3AB  OUT ($C0),A  (no_effect)
# CHECK low: site 2B291  OUT ($DD),A  (no_effect)
# CHECK low: site 2B368  OUT ($3F),A  (io_control)
# CHECK low: site 2B745  IN A,($7F)  (h_counter)
# CHECK low: site 2D89A  OTDR  (port in C)
# CHECK low: site 2DFD3  IN A,($DC)  (joypad_a)
# CHECK low: site 2E3FD  IN A,($DC)  (joypad_a)
# CHECK low: site 2EA25  OUT ($F0),A  (fm_address)
# CHECK low: site 2FC78  OUT ($7F),A  (psg)
# CHECK low: site 314CF  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 3198C  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 31C2B  OTDR  (port in C)
# CHECK low: site 320E2  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 329FF  IN A,($7E)  (v_counter)
# CHECK low: site 38E47  IN A,($BD)  (vdp_status)
# CHECK low: site 3ABFC  OUT ($DD),A  (no_effect)
# CHECK low: site 3AD4D  OUT ($BD),A  (vdp_control)
# CHECK low: site 3C049  IN A,($7E)  (v_counter)
# CHECK low: site 3C05B  IN A,($BD)  (vdp_status)
# CHECK low: site 3C1A3  IN A,($BD)  (vdp_status)
# CHECK low: site 3C366  IN A,($BD)  (vdp_status)
# CHECK low: site 3C4E5  IN A,($BD)  (vdp_status)
# CHECK low: site 3EB09  IN A,($BF)  (vdp_status)
# CHECK low: site 3F504  OUTD  (port in C)
# Name table rewrite at $0F98: rows 1-23 (VRAM $3840-$3FBF) from the RAM copy at $CD20,
# 128 bytes a row in the copy, with an OUTI loop: about 19,000 Next cycles a row through
# the traps, 436,000 for the screen. The page writes it with two jt_vwrite calls.
asm 00F99 25         ; LD DE,$7840 up to the JP NZ at $0FAF; the game's DI before, EI : RET after
    rst $10
    db far_io, pg_sh_nt, ent_sh_nt
    jr $0FB2
endasm
# Sprite table upload at $4AD3: $C500-$C53F to VRAM $3F00 and $C580-$C5FF to $3F80,
# through 192 OUTI.
asm 04AD3 6          ; LD HL,$C500 : LD DE,$7F00, then the RET of the block's end
    rst $10
    db far_io, pg_sh_sat, ent_sh_sat
    ret
endasm
# Tile upload at $4E53: E tiles of 3 bitplanes (24 bytes each, in bank 2) to VRAM from
# $2000, the fourth plane 0, through 3 OUTI and an OUT ($BE),A per row: about 21,000
# Next cycles a tile through the traps.
asm 04E53 10         ; LD C,$BE : XOR A : the CALL $4E5E loop, up to its RET at $4E5D
    rst $10
    db far_io, pg_sh_tiles, ent_sh_tiles
endasm
# Tile loader in the frame handler at $06C6: decodes run-length data into one bitplane
# of the tiles, every fourth VRAM byte, up to 128 bytes a frame, with a control write
# and an OUT ($BE),A for each byte: about 2,300 Next cycles a byte through the traps.
# State: $C131 planes left, $C132 run kind, $C133 run bytes left, $C134 bank (the code
# before $06D1 maps it), $C135 plane address, $C153 source, $C155 VRAM address, and a
# queue of jobs from $C139.
asm 006D1 7          ; LD DE,($C155) : LD HL,($C153): the rest of the routine is sh_rle
    rst $10
    db far_io, pg_sh_rle, ent_sh_rle
    ret
endasm
# Line handler at $044A (the line interrupt at line 127, register 10 = $7F): CRAM 0 and
# CRAM 16 = ($C17B), the ground colour, which the SMS writes at line 128. Pixel value 0 is
# the tilemap's transparent value here (CRAM 0 = CRAM 16), so the cells that use it show
# the fallback colour (NextReg $4A). On the Next the handler starts at line 130 (the line
# event and the status read at $0039 through the runtime), so the cells of row 16 with
# pixel value 0, round objects and explosions at the horizon, showed the sky colour in
# lines 128-130, and the border the ground colour from line 134. The frame handler writes
# register 10 = $7B (line 123) in place of $7F, and page 1 entry sh_gnd waits for line 128,
# then writes the fallback colour, the border and CRAM 0 and 16 at once.
asm 0015F 2          ; LD A,$7F: register 10, written at $0161-$0165
    ld a,$7B
endasm
asm 0044A 36         ; LD A,$07 : DEC A : JR NZ ... OUT ($BE),A: up to $046D
    rst $10
    db far_io, pg_sh_gnd, ent_sh_gnd
    jr $046E
endasm
# The frame handler's palette upload, LD HL,$C15A : LD DE,$C000 : RST $08 : LD C,$BE :
# CALL $4BA6 (32 OUTI): CRAM 0-31 from $C15A, CRAM 0 and 16 the sky colour. The counted
# delay loops before it (two or three LD B,$E0 : DJNZ, with the sprite table upload in
# the two-loop forms) put CRAM 0's write at SMS line 233-235, past the picture; at 28 MHz
# they take about 5 lines, and the backdrop (the bottom border) turned to the sky colour
# from line 218. Page 1 entry sh_pal waits for the line in A, the line of the SMS's
# CRAM 0 write on each path (MAME sg1000m3, cycles from the handler's entry), then writes
# the 32 entries.
asm 001DE 12         ; after two loops, the display on and the sprite table: line 235
    ld a,235
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 0024F 12         ; after three loops: line 233
    ld a,233
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 002B1 12         ; after three loops and $10E5: line 233
    ld a,233
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 002DA 12         ; after two loops, the sprite table and $10E5: line 235
    ld a,235
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 0030D 12         ; after three loops and $10E5: line 234
    ld a,234
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 0033C 12         ; after three loops and $10E5: line 233
    ld a,233
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 00366 12         ; after three loops and $10E5: line 233
    ld a,233
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 0038D 12         ; after three loops and $10E5: line 233
    ld a,233
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 003BC 12         ; after two loops and the sprite table: line 235
    ld a,235
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 00410 12         ; after three loops: line 233
    ld a,233
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
asm 00434 12         ; after three loops (the pause): line 233
    ld a,233
    rst $10
    db far_io, pg_sh_pal, ent_sh_pal
endasm
page 0 sh_nt sh_sat sh_tiles sh_rle
; sh_nt: does what $0F99-$0FB1 does with interrupts off: name table rows 1-23,
; 32 cells each, from $CD20 + 128 * row to VRAM $3840 + 64 * row. Columns 0-7
; and columns 8-31 are two calls, so that each takes jt_vwrite's fast form for
; name table runs. Returns with the registers the game's loop leaves: A = 0,
; B = 0, C = $BE, DE = $0040, HL = $CD20 + 23 * 128, Z set.
sh_nt:  push ix
        push iy
        ld hl,$CD20
        ld de,$3840
        ld bc,$1017             ; 23 runs of 16 bytes: columns 0-7
        ld ix,128               ; the source step
        ld iy,64                ; the VRAM step
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld l,$30                ; HL = $CD30, DE = $3850: columns 8-31
        ld e,$50
        ld b,48
        xor a
        call jt_vwrite
        pop iy
        pop ix
        ld hl,$CD20+23*128
        ld de,$0040
        ld bc,$00BE
        xor a
        ret

; sh_sat: does what $4AD3-$4BE6 does: $C500-$C53F to VRAM $3F00, then
; $C580-$C5FF to VRAM $3F80. Returns as that code does: A = $7F, B = B - 192,
; C = $BE, DE = $7F80, HL = $C600.
sh_sat: ld a,i                  ; P/V = the interrupt state
        di
        push af
        push ix
        push iy
        ld a,b
        add a,64                ; B - 192, as the 192 OUTI leave it
        ld (sat_b),a
        ld hl,$C500
        ld de,$3F00
        ld bc,$4001             ; 1 run of 64 bytes
        ld ix,0
        ld iy,0
        xor a
        call jt_vwrite
        ld l,$80                ; HL = $C580, DE = $3F80
        ld e,l
        ld b,l                  ; 1 run of 128 bytes
        xor a
        call jt_vwrite
        pop iy
        pop ix
        ld hl,$C600
        ld de,$7F80
        ld a,(sat_b)
        ld b,a
        ld c,$BE
        pop af
        ld a,$7F
        jp po,.di
        ei
.di:    ret

; sh_tiles: does what $4E53-$4E5D does: E tiles (0 = 256) from HL, 3 bytes a
; row, 8 rows a tile, to VRAM from $2000, 4 bytes a row, the fourth byte 0. The
; game reads HL in bank 2 in slot 2, so the page reads it directly. The tiles
; go through buf, 32 at a time, with one jt_vwrite call for each 32. Returns as
; that code does: A = 0, E = 0, B = B - 24 * E, C = $BE, HL past the last
; tile, Z set.
sh_tiles:
        ld a,i
        di
        push af
        push ix
        push iy
        push de
        ld a,e
        add a,a
        add a,a
        add a,a
        ld c,a
        add a,a
        add a,c                 ; 24 * E, modulo 256
        neg
        add a,b
        ld (tl_b),a             ; B as the OUTI leave it
        ld d,0
        dec e
        inc de                  ; DE = tiles, 1-256
        ld (tl_n),de
        ld de,$2000
        ld (tl_v),de
        ld ix,32
        ld iy,32
.chunk: ld de,(tl_n)
        ld a,d
        or a
        jr nz,.full
        ld a,e
        cp 33
        jr c,.some
.full:  ld a,32
.some:  ld (tl_c),a             ; tiles in this call, 1-32
        ld b,a
        ld de,buf
.tile:
        dup 8
        ld a,(hl)
        ld (de),a
        inc hl
        inc de
        ld a,(hl)
        ld (de),a
        inc hl
        inc de
        ld a,(hl)
        ld (de),a
        inc hl
        inc de
        xor a
        ld (de),a
        inc de
        edup
        dec b
        jp nz,.tile
        push hl
        ld a,(tl_c)
        ld c,a                  ; runs: one tile each
        ld b,32
        ld hl,buf
        ld de,(tl_v)
        ld a,1                  ; the source as mapped: buf in this page
        call jt_vwrite
        ld h,0
        ld l,c
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,de
        ld (tl_v),hl            ; VRAM after these tiles
        ld hl,(tl_n)
        ld b,0
        or a
        sbc hl,bc
        ld (tl_n),hl
        ld a,h
        or l
        pop hl
        jp nz,.chunk
        pop de
        ld e,0
        pop iy
        pop ix
        ld a,(tl_b)
        ld b,a
        ld c,$BE
        pop af
        jp po,.di
        ei
.di:    xor a
        ret

; sh_rle: does what $06D1-$078A does, with the bytes collected in buf and
; written with one jt_vwrite call (one byte a run, 4 bytes apart in VRAM).
; The callers go on to the frame handler's exit, which uses no register.
sh_rle: ld a,i
        di
        push af
        push ix
        push iy
        ld hl,($C155)
        ld (rl_v),hl            ; the VRAM address of the first byte
        ld hl,($C153)
        ld ix,buf
        ld c,0                  ; bytes this call, up to $80
        ld a,($C133)
        or a
        jr nz,.cont
.next:  ld a,c                  ; $06E1
        cp $80
        jr nc,.save
        call rl_rd
        or a
        jr z,.eop
        and $7F
        ld b,a
        add a,c
        cp $81
        jr c,.fits
        ld a,$80                ; past this call's 128 bytes: the rest next time
        sub c
        ld b,a
        call rl_rd
        and $7F
        sub b
        ld ($C133),a
        ld a,$80
.fits:  ld c,a
        call rl_rd
        inc hl
        and $80
        ld ($C132),a
.run:   jr z,.rep               ; $070A: bit 7 clear, B copies of one byte
.lit:   call rl_rd              ; bit 7 set, B bytes
        ld (ix+0),a
        inc ix
        inc hl
        djnz .lit
        jr .next
.rep:   call rl_rd
.rp:    ld (ix+0),a
        inc ix
        djnz .rp
        ld a,($C133)
        or a
        jr nz,.next             ; the run goes on next time: HL stays on its byte
        inc hl
        jr .next
.cont:  cp $80                  ; $0726: the rest of a run from the last call
        jr c,.c1
        sub $80
        ld ($C133),a
        ld b,$80
        ld c,b
        jr .c2
.c1:    ld b,a
        ld c,a
        xor a
        ld ($C133),a
.c2:    ld a,($C132)
        or a
        jr .run
.save:  ld ($C153),hl           ; $0759
        call rl_flush
        ld ($C155),de
        jr .ret
.eop:   inc hl                  ; $0761: the plane ends
        ld ($C153),hl
        call rl_flush
        ld hl,($C135)
        inc hl
        ld ($C135),hl
        ld ($C155),hl
        ld hl,$C131
        dec (hl)
        jr nz,.ret
        ld hl,$C139             ; the tile set ends: the next job
        ld de,$C134
        ld bc,$001A
        ldir
        ld a,($C134)
        inc a
        jr z,.ret
        ld hl,($C137)           ; $0743
        ld ($C153),hl
        ld hl,($C135)
        ld ($C155),hl
        ld a,4
        ld ($C131),a
        xor a
        ld ($C133),a
.ret:   pop iy
        pop ix
        pop af
        jp po,.di
        ei
.di:    ret

; rl_rd: A = the byte the game sees at HL.
rl_rd:  ld a,h
        and $E0
        cp $20
        jp z,jt_peek
        ld a,(hl)
        ret

; rl_flush: writes the bytes from buf to IX - 1 to VRAM from (rl_v), 4 bytes
; apart. Returns DE = (rl_v) + 4 * bytes, the game's DE after them.
rl_flush:
        push hl
        push ix
        pop hl
        ld bc,buf
        or a
        sbc hl,bc               ; L = bytes, 0-128
        ld c,l
        ld de,(rl_v)
        ld a,c
        or a
        jr z,.none
        push de
        ld hl,buf
        ld b,1
        ld ix,1
        ld iy,4
        ld a,1                  ; the source as mapped: buf in this page
        call jt_vwrite
        pop de
.none:  ld h,0
        ld l,c
        add hl,hl
        add hl,hl
        add hl,de
        ex de,hl
        pop hl
        ret

rl_v:   dw 0
sat_b:  db 0
tl_b:   db 0
tl_c:   db 0
tl_n:   dw 0
tl_v:   dw 0
buf:    ds 32*32
endpage
page 1 sh_gnd sh_pal
; Mid-frame colours. The entries write CRAM as the runtime's data port writes with VDP
; code 3 do (cram_set, cram_block and pal_out in fw.asm), straight into the Next
; palettes at the line where the SMS writes them: for each entry e, the colour (low
; 6 bits) into cram, into the first tilemap palette (index e) and, for e 16-31, into
; the first sprite palette (e - 16), from pal_hi_table and pal_lo_table, with NextReg
; $43 holding pal43's display bits. Then the VDP state as the game's writes leave it
; (address, code 3, latch clear, read buffer), and fallback_update, which sets the
; transparent value, the fallback colour and the backdrop (the border). With priority
; or toppal (fw_flags bits 0 and 1) the writes go through the I/O RST instead, which
; also does the Layer 2 and second palettes.
; Both entries run in the game's interrupt handler with interrupts off. They keep the
; game's stack as the game's code does: fallback_update maps part 2 of the runtime in
; slot 1, so the entries' own stack cannot be in this page at $2000. They map this page
; at $4000 as well (slot 2) and use a stack there, and put slot 2 back from cur_mmu + 2;
; the I/O RST path runs on the game's stack, as the game's own writes.
; Runtime internals (build/rt/runtime.map): pal43 $E09F, pal_hi_table $E300,
; pal_lo_table $E340, fw_flags $E09E, fallback_update $F582 (calls fallback2 in fw2
; through fw2_call, which puts back the page in slot 1 from cur_mmu + 1: this code
; page while an entry runs).
        OPT --zxnext
S_PAL43 equ $E09F
S_PHI   equ $E300
S_PLO   equ $E340
S_FLAGS equ $E09E
S_FBUP  equ $F582

; sh_gnd: does what $044A-$046D does: CRAM 0 and CRAM 16 = ($C17B), at line 128, where
; the SMS writes them (the line interrupt comes 5 lines early: register 10 = $7B). It
; waits for that line when the handler starts up to 16 lines before it. The fallback
; colour goes first, when the transparent value (NextReg $4C) is 0: the cells with pixel
; value 0 show it; then the border, when it shows CRAM 16 (register 7 = 0). Keeps BC,
; DE, HL; returns A = ($C17B), as the game's code.
GND_LINE equ 128
sh_gnd: call enter
        ld de,GND_LINE*256+GND_LINE-16
        call wline
        ld a,(S_FLAGS)
        and 3
        jr nz,.rst
        ld bc,$243B
        ld a,$4C
        out (c),a
        inc b
        in b,(c)                ; the transparent value
        ld a,($C17B)
        and $3F
        ld c,a
        ld a,b
        or a
        jr nz,.nt
        ld a,c
        add a,S_PHI&255
        ld l,a
        ld h,S_PHI>>8
        ld a,(hl)
        nextreg $4A,a           ; the fallback colour
.nt:    ld a,(vdp_regs+7)
        and $0F
        call z,ulab             ; the border shows CRAM 16
        ld e,0
        call c1
        ld e,16
        call c1
        ld a,(S_PAL43)
        nextreg $43,a
        ld hl,$0011             ; after CRAM 16
        ld (vdp_addr),hl
        ld a,3
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld a,($C17B)
        ld (vdp_rbuf),a
        call S_FBUP
        call leave
        jr .ret
.rst:   call leave
        xor a
        rst $10
        db $05                  ; OUT ($BF),A
        ld a,$C0
        rst $10
        db $05
        ld a,($C17B)
        rst $10
        db $04                  ; OUT ($BE),A
        ld a,$10
        rst $10
        db $05
        ld a,$C0
        rst $10
        db $05
        ld a,($C17B)
        rst $10
        db $04
.ret:   ld bc,(e_bc)
        ld de,(e_de)
        ld hl,(e_hl)
        ld a,(e_ie)
        or a
        ld a,($C17B)
        jr z,.di
        ei
.di:    ret

; sh_pal: does what LD HL,$C15A : LD DE,$C000 : RST $08 : LD C,$BE : CALL $4BA6 does:
; CRAM 0-31 from $C15A. A = the SMS line of the CRAM 0 write. It waits from line 192 for
; line A, writes the border (the backdrop, CRAM 16 + register 7, which the SMS writes
; about a line after CRAM 0), then entries 0-16, runs fallback_update, writes entries
; 17-31 and runs it again.
; Returns as that code does: HL = $C17A, DE = $C000, C = $BE, B = B - 32, A = $C0. The
; flags are not those of the last OUTI: the code after each site does not read them.
sh_pal: call enter
        ld a,(e_a)
        ld d,a                  ; the line to wait for
        ld e,192
        call wline
        ld a,(S_FLAGS)
        and 3
        jr nz,.rst
        ld a,(vdp_regs+7)
        and $0F
        add a,$6A
        ld l,a
        ld h,$C1                ; $C16A + register 7: the backdrop's entry
        ld a,(hl)
        and $3F
        ld c,a
        call ulab
        ld hl,$C15A
        ld e,0
        ld b,17
        call cn
        push hl
        push de
        call S_FBUP
        pop de
        pop hl
        ld b,15
        call cn
        ld a,(S_PAL43)
        nextreg $43,a
        ld hl,$0020             ; after CRAM 31
        ld (vdp_addr),hl
        ld a,3
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld a,($C179)
        ld (vdp_rbuf),a
        call S_FBUP
        call leave
        jr .ret
.rst:   call leave
        xor a
        rst $10
        db $05                  ; OUT ($BF),A
        ld a,$C0
        rst $10
        db $05
        ld hl,$C15A
        ld bc,$20BE
        rst $10
        db $B3                  ; OTIR
.ret:   ld a,(e_bc+1)
        sub 32
        ld b,a                  ; B as the 32 OUTI leave it
        ld c,$BE
        ld hl,$C17A
        ld de,$C000
        ld a,(e_ie)
        or a
        ld a,$C0
        jr z,.di
        ei
.di:    ret

; enter: called first by each entry. Keeps the game's A, BC, DE, HL and SP in e_a to e_sp
; and the interrupt state in e_ie, turns interrupts off, maps this page at $4000 too and
; puts SP on e_stk there, with the return to the entry on it.
enter:  ld (e_a),a
        ld (e_bc),bc
        ld (e_de),de
        ld (e_hl),hl
        ld a,i                  ; P/V = the interrupt state
        di
        ld a,0
        jp po,.di
        inc a
.di:    ld (e_ie),a
        pop hl                  ; the return to the entry, from the game's stack
        ld (e_sp),sp
        ld bc,$243B
        ld a,$51
        out (c),a
        inc b
        in a,(c)                ; this page
        nextreg $52,a           ; and at $4000-$5FFF
        ld sp,e_stk+$2000
        jp (hl)

; leave: back to the game's stack and slot 2 page (cur_mmu + 2). Uses A, HL.
leave:  pop hl
        ld a,(cur_mmu+2)
        nextreg $52,a
        ld sp,(e_sp)
        jp (hl)

; ulab: the border: the second ULA palette's 32 entries = colour C, as bd_update in
; fw2.asm writes them (every entry holds the backdrop colour). bd_update writes them
; again with its own note of the colour (bd_cur) when fallback_update runs. Uses A, B, HL.
ulab:   ld a,(S_PAL43)
        or %01000000            ; the second ULA palette
        nextreg $43,a
        nextreg $40,0
        ld a,c
        add a,S_PHI&255
        ld l,a
        ld h,S_PHI>>8
        ld b,(hl)
        ld a,c
        add a,S_PLO&255
        ld l,a
        ld l,(hl)
        ld h,32
.w:     ld a,b
        nextreg $44,a
        ld a,l
        nextreg $44,a
        dec h
        jr nz,.w
        ld a,(S_PAL43)
        nextreg $43,a
        ret

; cn: B entries from HL, from entry E, through c1. Returns HL and E past them.
cn:     ld a,(hl)
        and $3F
        ld c,a
        push bc
        push hl
        call c1
        pop hl
        pop bc
        inc hl
        inc e
        djnz cn
        ld a,(S_PAL43)
        nextreg $43,a
        ret

; c1: CRAM entry E (0-31) = colour C (0-63): cram, the first tilemap palette, and for
; E 16-31 the first sprite palette. Uses A, B, HL.
c1:     ld hl,cram
        ld a,e
        add hl,a
        ld (hl),c
        ld a,c
        add a,S_PHI&255
        ld l,a
        ld h,S_PHI>>8
        ld b,(hl)
        ld a,c
        add a,S_PLO&255
        ld l,a
        ld l,(hl)               ; S_PLO has the same high byte
        ld a,(S_PAL43)
        or %00110000            ; the first tilemap palette
        nextreg $43,a
        ld a,e
        nextreg $40,a
        ld a,b
        nextreg $44,a
        ld a,l
        nextreg $44,a
        ld a,e
        cp 16
        ret c
        ld a,(S_PAL43)
        or %00100000            ; the first sprite palette
        nextreg $43,a
        ld a,e
        sub 16
        nextreg $40,a
        ld a,b
        nextreg $44,a
        ld a,l
        nextreg $44,a
        ret

; wline: waits while the Next's line is from E to D - 1 (lines 0-255; the Next's line
; is the SMS line in 192-line mode). Uses A, BC, HL.
wline:  call rline
        ld a,h
        or a
        ret nz
        ld a,l
        cp e
        ret c
        cp d
        ret nc
        jr wline

; rline: HL = the Next's line (NextReg $1E, $1F), read again when the high byte changed
; between the reads. Uses A, BC.
rline:  ld bc,$243B
.a:     ld a,$1E
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
        jr nz,.a
        ld a,h
        and 1
        ld h,a
        ret

e_a:    db 0
e_ie:   db 0
e_bc:   dw 0
e_de:   dw 0
e_hl:   dw 0
e_sp:   dw 0
        ds 64
e_stk:
endpage

# Space Harrier (Europe).cht, "Infinite Lives"
poke "Infinite lives"
ar 00C1-2309
endpoke

# Space Harrier (Europe).cht, "Invincibility (after dying)"
poke "Invincibility"
gg 3A5-EDD-2A2
endpoke
