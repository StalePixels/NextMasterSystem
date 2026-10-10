# Zillion, 5718762C, drafted by tools/mkspec.py from sitescan output (with the detector log).
name Zillion
cart 5718762C
hz any		; No-Intro regions USA, Europe
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
# priority tiles: the text boxes after the yes/no prompt set the priority bit
# on every name table entry; they hide the cursor ship's sprites, which the
# game leaves in the sprite table.
priority
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
otir 00033   ; OUTI
site 00120   ; IN A,($BF)
site 0016F   ; IN A,($DD)
site 00190   ; OUT ($BE),A
otir 001A2   ; OUTI
site 001B6   ; OUTI
site 001BA   ; OUT (C),A
site 001D0   ; INI
site 001EC   ; OUT ($BE),A
site 001F9   ; OUTI
site 0020F   ; OUTI
site 00226   ; OUTI
site 0022C   ; OUT (C),A
site 00245   ; OUTI
site 0024B   ; OUT (C),A
site 0026E   ; OUT (C),D
site 00296   ; OUT ($BF),A
site 0029A   ; OUT ($BF),A
otir 0029C   ; OUTI
site 002A9   ; OUTD
site 002B0   ; OUT ($BE),A
site 002B9   ; OUT ($BF),A
site 002BD   ; OUT ($BF),A
site 002BF   ; OUTI
site 002D2   ; OUTI
site 002D4   ; OUTD
site 002EB   ; OUT ($BF),A
site 002EF   ; OUT ($BF),A
site 002F3   ; OUT ($BE),A
site 002FB   ; OUTI
site 00308   ; OUT ($BF),A
site 0030C   ; OUT ($BF),A
site 0030E   ; OUTI
site 00316   ; OUT ($BF),A
site 0031A   ; OUT ($BF),A
site 0031F   ; OUT ($BE),A
site 00324   ; OUT ($BF),A
site 00328   ; OUT ($BF),A
site 00330   ; OUTI
site 0033D   ; OUT ($BF),A
site 00341   ; OUT ($BF),A
site 00343   ; OUTI
site 00350   ; OTIR
site 00353   ; OUT ($BE),A
site 00390   ; OUT (C),D
site 00392   ; IN A,($BE)
site 00394   ; IN A,($BE)
site 00396   ; IN A,($BE)
site 003A0   ; OUTI
site 003A2   ; IN A,($BE)
site 003A4   ; IN A,($BE)
site 003A6   ; IN A,($BE)
site 003C5   ; OUT ($BF),A
site 003C8   ; OUT ($BF),A
site 003CC   ; OUT ($BE),A
site 00436   ; OUTI
site 00438   ; OUTI
site 0043A   ; OUTI
site 0043C   ; OUTI
site 0043E   ; OUTI
site 00440   ; OUTI
site 00442   ; OUTI
site 00444   ; OUTI
site 00446   ; OUTI
site 00448   ; OUTI
site 0044A   ; OUTI
site 0044C   ; OUTI
site 0044E   ; OUTI
site 00450   ; OUTI
site 00452   ; OUTI
site 00454   ; OUTI
site 00456   ; OUTI
site 00458   ; OUTI
site 0045A   ; OUTI
site 0045C   ; OUTI
site 0045E   ; OUTI
site 00460   ; OUTI
site 00462   ; OUTI
site 00464   ; OUTI
site 00466   ; OUTI
site 00468   ; OUTI
site 0046A   ; OUTI
site 0046C   ; OUTI
site 0046E   ; OUTI
site 00470   ; OUTI
site 00472   ; OUTI
site 00474   ; OUTI
site 00479   ; OUT ($BE),A
site 0047E   ; OUT ($BE),A
site 00483   ; OUT ($BE),A
site 00488   ; OUT ($BE),A
site 0048D   ; OUT ($BE),A
site 00492   ; OUT ($BE),A
site 00497   ; OUT ($BE),A
site 0049C   ; OUT ($BE),A
site 004A1   ; OUT ($BE),A
site 004A6   ; OUT ($BE),A
site 004AB   ; OUT ($BE),A
site 004B0   ; OUT ($BE),A
site 004B5   ; OUT ($BE),A
site 004BA   ; OUT ($BE),A
site 004BF   ; OUT ($BE),A
site 004C4   ; OUT ($BE),A
site 004C9   ; OUT ($BE),A
site 004CE   ; OUT ($BE),A
site 004D3   ; OUT ($BE),A
site 004D8   ; OUT ($BE),A
site 004DD   ; OUT ($BE),A
site 004E2   ; OUT ($BE),A
site 004E7   ; OUT ($BE),A
site 004EC   ; OUT ($BE),A
site 004F1   ; OUT ($BE),A
site 004F6   ; OUT ($BE),A
site 004FB   ; OUT ($BE),A
site 00500   ; OUT ($BE),A
site 00505   ; OUT ($BE),A
site 0050A   ; OUT ($BE),A
site 0050F   ; OUT ($BE),A
site 00514   ; OUT ($BE),A
site 0059D   ; OUT ($3F),A
site 0059F   ; IN A,($DD)
site 005A9   ; OUT ($3F),A
site 005AB   ; IN A,($DD)
site 005B4   ; OUT ($3F),A
site 005C0   ; IN A,($DC)
site 005C6   ; IN A,($DD)
site 005EC   ; OUT ($BF),A
site 005F0   ; OUT ($BF),A
site 00600   ; OUT ($BF),A
site 00604   ; OUT ($BF),A
site 00657   ; OUT ($BF),A
site 0065A   ; OUT ($BF),A
site 0073E   ; OUT ($BE),A
site 00741   ; OUT ($BE),A
site 00744   ; OUT ($BE),A
site 00746   ; OUT ($BE),A
site 0079F   ; OUT ($BF),A
site 007A3   ; OUT ($BF),A
site 007AA   ; OTIR
site 007B2   ; OUT ($BF),A
site 007B6   ; OUT ($BF),A
site 007BB   ; OTIR
site 007F9   ; OUT ($BE),A
site 00EF0   ; OUT ($BE),A
site 00F29   ; OUT ($BF),A
site 00F2D   ; OUT ($BF),A
site 00F31   ; OUTI
site 00F33   ; OUTI
site 00F35   ; OUTI
site 00F37   ; OUTI
site 00F4F   ; OUT ($BF),A
site 00F53   ; OUT ($BF),A
site 00F5C   ; OUT ($BE),A
site 00F61   ; OUT ($BE),A
site 0199C   ; IN A,($BE)
site 0199E   ; IN A,($BE)
site 019AA   ; OUT ($BE),A
site 019AE   ; OUT ($BE),A
site 019D0   ; OUT ($BE),A
site 019D4   ; OUT ($BE),A
site 019E2   ; OUT ($BE),A
site 019E6   ; OUT ($BE),A
site 01A04   ; OUT ($BF),A
site 01A07   ; OUT ($BF),A
site 01A2A   ; OUT ($BE),A
site 01A2C   ; OUT ($BE),A
site 01A2E   ; OUT ($BE),A
site 01A31   ; OUTI
site 01A33   ; OUT ($BE),A
site 01A35   ; OUT ($BE),A
site 01A37   ; OUT ($BE),A
site 01A3A   ; OUTI
site 01A3C   ; OUT ($BE),A
site 01A3E   ; OUT ($BE),A
site 01A40   ; OUT ($BE),A
site 01A43   ; OUTI
site 01A45   ; OUT ($BE),A
site 01A47   ; OUT ($BE),A
site 01A49   ; OUT ($BE),A
site 01A4C   ; OUTI
site 01A4E   ; OUT ($BE),A
site 01A50   ; OUT ($BE),A
site 01A52   ; OUT ($BE),A
site 01A55   ; OUTI
site 01A57   ; OUT ($BE),A
site 01A59   ; OUT ($BE),A
site 01A5B   ; OUT ($BE),A
site 01A5E   ; OUTI
site 01A60   ; OUT ($BE),A
site 01A62   ; OUT ($BE),A
site 01A64   ; OUT ($BE),A
site 01A67   ; OUTI
site 01A69   ; OUT ($BE),A
site 01A6B   ; OUT ($BE),A
site 01A6D   ; OUT ($BE),A
site 01A70   ; OUTI
site 01A79   ; OUTI
site 01A7B   ; OUTI
site 01A7D   ; OUT ($BE),A
site 01A7F   ; OUT ($BE),A
site 01A81   ; OUTI
site 01A83   ; OUTI
site 01A85   ; OUT ($BE),A
site 01A87   ; OUT ($BE),A
site 01A89   ; OUTI
site 01A8B   ; OUTI
site 01A8D   ; OUT ($BE),A
site 01A8F   ; OUT ($BE),A
site 01A91   ; OUTI
site 01A93   ; OUTI
site 01A95   ; OUT ($BE),A
site 01A97   ; OUT ($BE),A
site 01A99   ; OUTI
site 01A9B   ; OUTI
site 01A9D   ; OUT ($BE),A
site 01A9F   ; OUT ($BE),A
site 01AA1   ; OUTI
site 01AA3   ; OUTI
site 01AA5   ; OUT ($BE),A
site 01AA7   ; OUT ($BE),A
site 01AA9   ; OUTI
site 01AAB   ; OUTI
site 01AAD   ; OUT ($BE),A
site 01AAF   ; OUT ($BE),A
site 01AB1   ; OUTI
site 01AB3   ; OUTI
site 01AB5   ; OUT ($BE),A
site 01AB7   ; OUT ($BE),A
site 01B01   ; OUT ($BE),A
site 01B05   ; OUT ($BE),A
site 01B09   ; OUT ($BE),A
site 01B0D   ; OUT ($BE),A
site 01F07   ; OTIR
site 021D1   ; OUT ($BE),A
site 021EC   ; OUT ($BF),A
site 021F0   ; OUT ($BF),A
site 022C7   ; OUT ($BE),A
site 040BA   ; OUT ($BF),A
site 040BE   ; OUT ($BF),A
site 040C3   ; OUT ($BF),A
site 040C7   ; OUT ($BF),A
site 040CF   ; OUT ($BF),A
site 040D2   ; OUT ($BF),A
site 040D8   ; OUT ($BE),A
site 040DD   ; OUT ($BE),A
site 072B4   ; OUT ($BF),A
site 072B8   ; OUT ($BF),A
site 072BF   ; OUT ($BE),A
site 072C3   ; OUT ($BE),A
site 072CD   ; OUT ($BE),A
site 072CF   ; OUT ($BE),A
site 07360   ; OUTI
site 073B6   ; OUT ($BF),A
site 073BA   ; OUT ($BF),A
site 073E2   ; OUT ($BF),A
site 073E6   ; OUT ($BF),A
site 07456   ; OUT (C),L
site 07458   ; OUT (C),H
site 0745B   ; OUT (C),E
site 0745D   ; OUT (C),D
site 074ED   ; OUT ($BE),A
site 074F6   ; OUT ($BE),A
site 07506   ; OUT ($BE),A
site 07509   ; OUT ($BE),A
site 07549   ; OUT ($BE),A
site 0754C   ; OUT ($BE),A
site 07576   ; OUT ($BF),A
site 0757A   ; OUT ($BF),A
site 07582   ; OTIR
site 1600B   ; OUT ($7F),A
site 160B8   ; OUT ($7F),A
site 160C8   ; OUT ($7F),A
site 165D6   ; OUT ($7F),A
site 16630   ; OUT ($7F),A
site 1664A   ; OTIR
site 16651   ; OUT ($7F),A
site 16655   ; OUT ($7F),A
mapst 00084   ; LD ($FFFF),A
mapst 00090   ; LD ($FFFF),A
mapst 000DC   ; LD ($FFFF),A
mapst 000E8   ; LD ($FFFF),A
mapst 00161   ; LD ($FFFF),A
mapst 0016C   ; LD ($FFFF),A
mapst 005E7   ; LD ($FFFF),A
mapst 0062C   ; LD ($FFFF),A
mapst 006DC   ; LD ($FFFF),A
mapst 0070F   ; LD ($FFFF),A
mapst 0074E   ; LD ($FFFF),A
mapst 00871   ; LD ($FFFF),A
mapst 008AF   ; LD ($FFFF),A
mapst 00958   ; LD ($FFFF),A
mapst 0099F   ; LD ($FFFF),A
mapst 00A9E   ; LD ($FFFF),A
mapst 00C13   ; LD ($FFFF),A
mapst 00CD0   ; LD ($FFFF),A
mapst 00CF0   ; LD ($FFFF),A
mapst 00D25   ; LD ($FFFF),A
mapst 00D42   ; LD ($FFFF),A
mapst 00D56   ; LD ($FFFF),A
mapst 00DDA   ; LD ($FFFF),A
mapst 00E0D   ; LD ($FFFF),A
mapst 00E1C   ; LD ($FFFF),A
mapst 00F78   ; LD ($FFFF),A
mapst 00FEC   ; LD ($FFFF),A
mapst 0105B   ; LD ($FFFF),A
mapst 01069   ; LD ($FFFF),A
mapst 010CA   ; LD ($FFFF),A
mapst 010F4   ; LD ($FFFF),A
mapst 0111B   ; LD ($FFFF),A
mapst 01129   ; LD ($FFFF),A
mapst 011C8   ; LD ($FFFF),A
mapst 011D9   ; LD ($FFFF),A
mapst 0128F   ; LD ($FFFF),A
mapst 01423   ; LD ($FFFF),A
mapst 0151C   ; LD ($FFFF),A
mapst 0154E   ; LD ($FFFF),A
mapst 01556   ; LD ($FFFF),A
mapst 01836   ; LD ($FFFF),A
mapst 01859   ; LD ($FFFF),A
mapst 019ED   ; LD ($FFFF),A
mapst 01C68   ; LD ($FFFF),A
mapst 01C84   ; LD ($FFFF),A
mapst 01DAD   ; LD ($FFFF),A
mapst 02014   ; LD ($FFFF),A
mapst 02023   ; LD ($FFFF),A
mapst 02057   ; LD ($FFFF),A
mapst 02252   ; LD ($FFFF),A
mapst 02273   ; LD ($FFFF),A
mapst 0235A   ; LD ($FFFF),A
mapst 023D9   ; LD ($FFFF),A
mapst 02535   ; LD ($FFFF),A
mapst 025C1   ; LD ($FFFF),A
mapst 025E3   ; LD ($FFFF),A
mapst 0263A   ; LD ($FFFF),A
mapst 026E9   ; LD ($FFFF),A
mapst 0279A   ; LD ($FFFF),A
mapst 02ADF   ; LD ($FFFF),A
mapst 02AF3   ; LD ($FFFF),A
mapst 02B26   ; LD ($FFFF),A
mapst 02B4C   ; LD ($FFFF),A
mapst 02E61   ; LD ($FFFF),A
mapst 039A3   ; LD ($FFFF),A
mapst 039AB   ; LD ($FFFF),A
mapst 03BD3   ; LD ($FFFF),A
mapst 03CEB   ; LD ($FFFF),A
mapst 03CFD   ; LD ($FFFF),A
mapst 042DE   ; LD ($FFFF),A
mapst 042ED   ; LD ($FFFF),A
mapst 04306   ; LD ($FFFF),A
mapst 04327   ; LD ($FFFF),A
mapst 04370   ; LD ($FFFF),A
mapld 043B9   # loads HL with $FFFF, then stores $07 through it
mapst 043C7   ; LD ($FFFF),A
mapst 043CE   ; LD ($FFFF),A
mapst 0486D   ; LD ($FFFF),A
mapst 048D6   ; LD ($FFFF),A
mapst 048E7   ; LD ($FFFF),A
mapst 04985   ; LD ($FFFF),A
mapst 049A0   ; LD ($FFFF),A
mapst 04B3A   ; LD ($FFFF),A
mapst 04B55   ; LD ($FFFF),A
mapst 04BBE   ; LD ($FFFF),A
mapst 04BCA   ; LD ($FFFF),A
mapst 06FFD   ; LD ($FFFF),A
mapst 07012   ; LD ($FFFF),A
mapst 07043   ; LD ($FFFF),A
mapst 0734E   ; LD ($FFFF),A
mapst 07379   ; LD ($FFFF),A
mapst 073B1   ; LD ($FFFF),A
mapst 073DD   ; LD ($FFFF),A
mapst 07514   ; LD ($FFFF),A
mapst 07939   ; LD ($FFFF),A
mapst 07981   ; LD ($FFFF),A
mapst 079B9   ; LD ($FFFF),A
mapst 07AFB   ; LD ($FFFF),A
mapld 07B5F   # loads HL with $FFFF, then stores $07 through it
# CHECK cartarea_store at 00BA0 ($0BA0 bank 0): LD (BC),A $98E6
# CHECK indirect_unresolved at 02DB6 ($2DB6 bank 0): RET 
# CHECK indirect_unresolved at 072F6 ($72F6 bank 1): RET NZ 
# CHECK indirect_unresolved at 072FB ($72FB bank 1): RET 
# CHECK indirect_unresolved at 07316 ($7316 bank 1): RET 
# CHECK low: site 050C5  OUT ($C1),A  (no_effect)
# CHECK low: site 052AD  OUT ($C1),A  (no_effect)
# CHECK low: site 0F102  OUT ($BF),A  (vdp_control)
# CHECK low: site 0F106  OUT ($7F),A  (psg)
# CHECK low: site 0F185  IN A,($DC)  (joypad_a)
# CHECK low: site 15430  IN A,($DC)  (joypad_a)
# CHECK low: site 15432  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 19CAA  OUTI  (port in C)
# CHECK low: site 1F278  OUT ($DC),A  (no_effect)
# Mapper stores the draft missed: LD ($FFFF),A in banks 0-1 that no
# scanned path reached, found by sitescan's byte scan. Each follows LD A,n.
mapst 01FCA   ; LD ($FFFF),A
mapst 02061   ; LD ($FFFF),A
mapst 04E30   ; LD ($FFFF),A
mapst 04E3C   ; LD ($FFFF),A
mapst 04F5B   ; LD ($FFFF),A
mapst 04F67   ; LD ($FFFF),A
mapst 0522A   ; LD ($FFFF),A
# Player sprite tile upload in the frame handler ($3BCD, called from $0139 when the
# player's animation frame changes), as native code in page 0. The game writes
# 8-14 tiles to VRAM $0000 through the traps: plain frames as 3 OUTI and an
# OUT of 0 per tile row, mirrored frames as 3 bytes through its table at $7E00
# and an IN A,($BE) per row, which skips the 4th byte. The mirrored form took
# about 50,000 Next cycles a tile, a third of a frame in the attract-mode
# corridor, so the game got about 0.68 game frames a Next frame there.
# The sites $3BE9-$3CE0 are in the code this replaces.
asm 03BE3 6          ; ADD A / LD C,A / LD B,0 / LD A,0 -> far call to page 0, then return
    rst $00
    db far_io, pg_plup, ent_plup
    ret
endasm
page 0 plup
; plup: A = the new animation frame. Does what the game's code at
; $3BE3-$3CE8 does, with bank 3 in slot 2. The frame's header is at
; ($8000 + 2A): a byte n (bit 7: mirrored), then n pointers, each to a
; tile's 8 rows of 3 bytes. A plain tile is written as rows of the 3 bytes
; and a 0; a mirrored tile's bytes go through the table at $7E00, and the
; 4th byte of each row is not written. The tiles go to VRAM $0000 on, one
; jt_vwrite call each. The game's frame data is all in bank 3 ($8000 on),
; and the table in slot 1, so plain reads see what the game sees.
; Leaves the VDP address after the last tile, as the game's code does;
; changes AF, BC, DE and HL (the game's code also changes AF').
plup:   push ix
        push iy
        add a,a
        ld l,a
        ld h,$80
        ld e,(hl)
        inc hl
        ld d,(hl)
        ex de,hl                ; HL = the frame's header
        ld a,(hl)
        inc hl
        ld (.mir),a             ; bit 7: mirrored
        and $7F
        ld de,0                 ; the VRAM address
.tile:  push af                 ; tiles left
        push hl                 ; the pointer list
        ld a,(hl)
        inc hl
        ld h,(hl)
        ld l,a                  ; HL = the tile's 24 bytes
        push de
        ld de,.buf
        ld ixl,8
        ld a,(.mir)
        rlca
        jr c,.mrow
.prow:  ld a,(hl)
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
        dec ixl
        jr nz,.prow
        pop de
        ld bc,$2001             ; one run of 32 bytes
        jr .write
.mrow:  ld b,$7E
        ld c,(hl)
        ld a,(bc)
        ld (de),a
        inc hl
        inc de
        ld c,(hl)
        ld a,(bc)
        ld (de),a
        inc hl
        inc de
        ld c,(hl)
        ld a,(bc)
        ld (de),a
        inc hl
        inc de
        inc de                  ; the 4th byte: not written
        dec ixl
        jr nz,.mrow
        pop de
        ld bc,$0308             ; 8 runs of 3 bytes, 4 apart
.write: ld hl,.buf
        ld ix,4                 ; the source step
        ld iy,4                 ; the VRAM step
        ld a,1                  ; the source as mapped now (this page)
        call jt_vwrite
        ld hl,32
        add hl,de
        ex de,hl                ; DE = the next tile
        pop hl
        inc hl
        inc hl
        pop af
        dec a
        jr nz,.tile
        ld (vdp_addr),de        ; the game's last IN A,($BE) moves past the 4th byte too
        pop iy
        pop ix
        ret
.mir:   db 0
.buf:   ds 32
endpage
