# Deep Duck Trouble Starring Donald Duck (Europe, Brazil) (En), CRC32 42FC3A6E, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of random
# input, 180 s of the attract mode) and the scan entries below.
# Decisions:
# - No RST vector has $FF filler, so $0000-$0002 (DI; IM 1) is the io vector and the
#   game starts at $0003.
# - Slot 1 holds bank 1, except while the sound start-up at $031C runs bank 2 there. The
#   calls from bank 0 into slot 1 ($401D-$79F1) are scan entries in bank 1, and so are the
#   bank 1 routines $65AE, $67FA and $74E3 that map slot 2 through ($D12B).
# - The frame handler's JP (HL) at $05B9 reads the 4-entry table at $0050 ($05BA, $05C6,
#   $05DA, $05F6); each entry is a scan entry.
# - The library routines $2FD0 (VDP register write), $2FE5 (status read), $2FF3 (VRAM read
#   address), $2FFE, $3006, $300C (VRAM byte helpers), $306A (frame interrupt off), $3626,
#   $3799 (text drawing) and $3A96 in bank 0 are code that no path or recording reached;
#   they are scan entries and their I/O is patched.
# - The sound driver's command table at $4138 (bank 2) has a fourth entry, $7000, that
#   points into data; the I/O byte patterns the scanner decodes there ($703B, $70A4, $70BB)
#   are data and are not patched, nor is the store at $67372 (bank 25, tile data).
# - The other I/O byte patterns that no path reached are tile graphics, tables or other
#   data (verdict false).
name Deep Duck Trouble Starring Donald Duck
cart 42FC3A6E
hz 50		; No-Intro region Europe, Brazil
# Play writes name table cells with the priority bit: the rock faces in front of pits and
# slopes (12,439 cells in 180 s of the attract mode, reference log).
priority
vector 00 io
start 0003

# Donald's tile upload ($08BF, called from the frame handler at $041E and $0514) writes
# ($D352)'s entry of the table at $0BE9 (bank, source, count) to VRAM $0000: count runs
# of 64 bytes from the bank it maps at slot 2, plain ($08E9, unrolled LD A,(DE); OUT
# ($BE),A; INC DE) or, with ($D351) bit 6 set, mirrored through the bit-reversal table at
# $0100 ($0A3B). With ($D352) = 0 it writes 512 zero bytes ($0B90). Through the runtime
# these took 37,000 cycles a run of 64 bytes and 220,000 cycles for the zero bytes. Each
# path is a far call to page 0 and a RET; the plain and mirrored entries end as the game's
# paths do ($0A35, $0B8A: RES 7,($D351)). The callers use no register the routine returns.
asm 008E9 8		; LD A,$00; OUT ($BF),A; LD A,$40; OUT ($BF),A
    rst $00
    db far_io, pg_tiles, ent_tiles
    ret
endasm
asm 00A3B 8		; LD A,$00; OUT ($BF),A; LD A,$40; OUT ($BF),A
    rst $00
    db far_io, pg_tilesflip, ent_tilesflip
    ret
endasm
asm 00B90 10		; LD A,$00; OUT ($BF),A; LD A,$00; OR $40; OUT ($BF),A
    rst $00
    db far_io, pg_tilesclr, ent_tilesclr
    ret
endasm
# The VRAM clear at $4173 (bank 1, with the display off) writes 16,384 zero bytes from VRAM
# $0000 as 1,024 runs of 16 OUT ($BE),A, about 3.9 million cycles through the runtime. It
# is a far call to page 0 and a jump to the routine's end ($41AD, display on). The loop
# it skips keeps its site lines: the cut scan does not cut a block that jumps on.
asm 04184 6		; CALL $2FE8; LD A,E; OUT ($BE),A
    rst $00
    db far_io, pg_vclear, ent_vclear
    jr $41AD
endasm
page 0 tiles tilesflip tilesclr vclear
; tiles: B runs of 64 bytes from DE (slot 2, the bank the game mapped) to VRAM $0000, in
; one jt_vwrite call.
tiles:	ex de,hl
	xor a			; the source as the game sees it
.vw:	ld de,$0000
	ld c,b
	ld b,64
	push ix
	push iy
	ld ix,64
	ld iy,64
	call jt_vwrite
	pop iy
	pop ix
	ld hl,$D351
	res 7,(hl)
	ret
; tilesflip: the same bytes, each through the game's bit-reversal table at $0100 (bank 0,
; readable here), into buf (at most 8 runs, 512 bytes), then to VRAM in the same way. A
; source in $2000-$3FFF is read with jt_peek.
tilesflip:
	push bc
	ex de,hl
	ld de,buf
	ld c,b
	ld b,64
.l:	ld a,h
	and $E0
	cp $20
	jr z,.pk
	ld a,(hl)
.rv:	push hl
	ld l,a
	ld h,$01
	ld a,(hl)
	pop hl
	ld (de),a
	inc hl
	inc de
	djnz .l
	ld b,64
	dec c
	jr nz,.l
	pop bc
	ld hl,buf
	ld a,1			; the source as mapped now: buf in this page
	jr tiles.vw
.pk:	call jt_peek
	jr .rv
; tilesclr: 512 zero bytes to VRAM $0000, as 8 runs of 64 from zero.
tilesclr:
	ld hl,zero
	ld de,$0000
	ld bc,$4008
	push ix
	push iy
	ld ix,0
	ld iy,64
	ld a,1
	call jt_vwrite
	pop iy
	pop ix
	ret
; vclear: 16,384 zero bytes to VRAM $0000, as 256 runs of 64 from zero.
vclear:
	ld hl,zero
	ld de,$0000
	ld bc,$4000
	push ix
	push iy
	ld ix,0
	ld iy,64
	ld a,1
	call jt_vwrite
	pop iy
	pop ix
	ret
zero:	ds 64
buf:	ds 512
endpage
site 00018   ; IN A,($7E)
site 00039   ; IN A,($BF)
site 003E1   ; OUT ($BF),A
site 003E5   ; OUT ($BF),A
site 003EB   ; OUT ($BF),A
site 003EF   ; OUT ($BF),A
site 00494   ; OUT ($BF),A
site 00498   ; OUT ($BF),A
site 0049D   ; OUT ($BF),A
site 004A1   ; OUT ($BF),A
site 004E5   ; OUT ($BF),A
site 004E9   ; OUT ($BF),A
site 004EE   ; OUT ($BF),A
site 004F2   ; OUT ($BF),A
site 005BD   ; OUT ($BF),A
site 005C1   ; OUT ($BF),A
site 005C9   ; OUT ($BF),A
site 005CD   ; OUT ($BF),A
site 005D1   ; OUT ($BF),A
site 005D5   ; OUT ($BF),A
site 005DD   ; OUT ($BF),A
site 005E1   ; OUT ($BF),A
site 005E5   ; OUT ($BF),A
site 005E9   ; OUT ($BF),A
site 005ED   ; OUT ($BF),A
site 005F1   ; OUT ($BF),A
site 01494   ; IN A,($DD)
site 02F4E   ; IN A,($BF)
site 02F50   ; IN A,($BF)
site 02F5C   ; IN A,($BF)
site 02FAC   ; IN A,($BF)
site 02FB9   ; OUT ($BF),A
site 02FBD   ; OUT ($BF),A
site 02FD3   ; OUT ($BF),A
site 02FD8   ; OUT ($BF),A
site 02FE5   ; IN A,($BF)
site 02FEA   ; OUT ($BF),A
site 02FEF   ; OUT ($BF),A
site 02FF4   ; OUT ($BF),A
site 02FF9   ; OUT ($BF),A
site 03003   ; OUT ($BE),A
site 03009   ; IN A,($BE)
site 03014   ; OUT ($BE),A
site 03018   ; IN A,($BE)
site 03025   ; OUT ($BE),A
site 0302A   ; OUT ($BE),A
site 03037   ; OUT ($BE),A
site 03047   ; OUT ($BF),A
site 0304B   ; OUT ($BF),A
site 03055   ; OUT ($BF),A
site 03059   ; OUT ($BF),A
site 03063   ; OUT ($BF),A
site 03067   ; OUT ($BF),A
site 03071   ; OUT ($BF),A
site 03075   ; OUT ($BF),A
site 0307F   ; OUT ($BE),A
site 03087   ; OUT ($BE),A
site 0309B   ; OUT ($BE),A
site 030A3   ; OUT ($BE),A
site 030BC   ; OUT ($BE),A
site 030C4   ; OUT ($BE),A
site 0311B   ; OUT ($BE),A
site 03123   ; OUT ($BE),A
site 0318D   ; OUT ($BE),A
site 03195   ; OUT ($BE),A
site 031A1   ; OUT ($BE),A
site 031A9   ; OUT ($BE),A
site 031C0   ; OUT ($BE),A
site 031C8   ; OUT ($BE),A
site 031D6   ; OUT ($BE),A
site 031DE   ; OUT ($BE),A
site 03201   ; OUT ($BF),A
site 03207   ; OUT ($BF),A
site 0320E   ; OUTI
site 03210   ; OUTI
site 03212   ; OUTI
site 03214   ; OUTI
site 03216   ; OUTI
site 03218   ; OUTI
site 0321A   ; OUTI
site 0321C   ; OUTI
site 0321E   ; OUTI
site 03220   ; OUTI
site 03222   ; OUTI
site 03224   ; OUTI
site 03226   ; OUTI
site 03228   ; OUTI
site 0322A   ; OUTI
site 0322C   ; OUTI
site 0322E   ; OUTI
site 03230   ; OUTI
site 03232   ; OUTI
site 03234   ; OUTI
site 03236   ; OUTI
site 03238   ; OUTI
site 0323A   ; OUTI
site 0323C   ; OUTI
site 0323E   ; OUTI
site 03240   ; OUTI
site 03242   ; OUTI
site 03244   ; OUTI
site 03246   ; OUTI
site 03248   ; OUTI
site 0324A   ; OUTI
site 0324C   ; OUTI
site 0324E   ; OUTI
site 03250   ; OUTI
site 03252   ; OUTI
site 03254   ; OUTI
site 03256   ; OUTI
site 03258   ; OUTI
site 0325A   ; OUTI
site 0325C   ; OUTI
site 0325E   ; OUTI
site 03260   ; OUTI
site 03262   ; OUTI
site 03264   ; OUTI
site 03266   ; OUTI
site 03268   ; OUTI
site 0326A   ; OUTI
site 0326C   ; OUTI
site 0326E   ; OUTI
site 03270   ; OUTI
site 03272   ; OUTI
site 03274   ; OUTI
site 03276   ; OUTI
site 03278   ; OUTI
site 0327A   ; OUTI
site 0327C   ; OUTI
site 0327E   ; OUTI
site 03280   ; OUTI
site 03282   ; OUTI
site 03284   ; OUTI
site 03286   ; OUTI
site 03288   ; OUTI
site 0328A   ; OUTI
site 0328C   ; OUTI
site 03290   ; OUT ($BF),A
site 03296   ; OUT ($BF),A
site 0329D   ; OUTI
site 0329F   ; OUTI
site 032A1   ; OUTI
site 032A3   ; OUTI
site 032A5   ; OUTI
site 032A7   ; OUTI
site 032A9   ; OUTI
site 032AB   ; OUTI
site 032AD   ; OUTI
site 032AF   ; OUTI
site 032B1   ; OUTI
site 032B3   ; OUTI
site 032B5   ; OUTI
site 032B7   ; OUTI
site 032B9   ; OUTI
site 032BB   ; OUTI
site 032BD   ; OUTI
site 032BF   ; OUTI
site 032C1   ; OUTI
site 032C3   ; OUTI
site 032C5   ; OUTI
site 032C7   ; OUTI
site 032C9   ; OUTI
site 032CB   ; OUTI
site 032CD   ; OUTI
site 032CF   ; OUTI
site 032D1   ; OUTI
site 032D3   ; OUTI
site 032D5   ; OUTI
site 032D7   ; OUTI
site 032D9   ; OUTI
site 032DB   ; OUTI
site 032DD   ; OUTI
site 032DF   ; OUTI
site 032E1   ; OUTI
site 032E3   ; OUTI
site 032E5   ; OUTI
site 032E7   ; OUTI
site 032E9   ; OUTI
site 032EB   ; OUTI
site 032ED   ; OUTI
site 032EF   ; OUTI
site 032F1   ; OUTI
site 032F3   ; OUTI
site 032F5   ; OUTI
site 032F7   ; OUTI
site 032F9   ; OUTI
site 032FB   ; OUTI
site 032FD   ; OUTI
site 032FF   ; OUTI
site 03301   ; OUTI
site 03303   ; OUTI
site 03305   ; OUTI
site 03307   ; OUTI
site 03309   ; OUTI
site 0330B   ; OUTI
site 0330D   ; OUTI
site 0330F   ; OUTI
site 03311   ; OUTI
site 03313   ; OUTI
site 03315   ; OUTI
site 03317   ; OUTI
site 03319   ; OUTI
site 0331B   ; OUTI
site 0331D   ; OUTI
site 0331F   ; OUTI
site 03321   ; OUTI
site 03323   ; OUTI
site 03325   ; OUTI
site 03327   ; OUTI
site 03329   ; OUTI
site 0332B   ; OUTI
site 0332D   ; OUTI
site 0332F   ; OUTI
site 03331   ; OUTI
site 03333   ; OUTI
site 03335   ; OUTI
site 03337   ; OUTI
site 03339   ; OUTI
site 0333B   ; OUTI
site 0333D   ; OUTI
site 0333F   ; OUTI
site 03341   ; OUTI
site 03343   ; OUTI
site 03345   ; OUTI
site 03347   ; OUTI
site 03349   ; OUTI
site 0334B   ; OUTI
site 0334D   ; OUTI
site 0334F   ; OUTI
site 03351   ; OUTI
site 03353   ; OUTI
site 03355   ; OUTI
site 03357   ; OUTI
site 03359   ; OUTI
site 0335B   ; OUTI
site 0335D   ; OUTI
site 0335F   ; OUTI
site 03361   ; OUTI
site 03363   ; OUTI
site 03365   ; OUTI
site 03367   ; OUTI
site 03369   ; OUTI
site 0336B   ; OUTI
site 0336D   ; OUTI
site 0336F   ; OUTI
site 03371   ; OUTI
site 03373   ; OUTI
site 03375   ; OUTI
site 03377   ; OUTI
site 03379   ; OUTI
site 0337B   ; OUTI
site 0337D   ; OUTI
site 0337F   ; OUTI
site 03381   ; OUTI
site 03383   ; OUTI
site 03385   ; OUTI
site 03387   ; OUTI
site 03389   ; OUTI
site 0338B   ; OUTI
site 0338D   ; OUTI
site 0338F   ; OUTI
site 03391   ; OUTI
site 03393   ; OUTI
site 03395   ; OUTI
site 03397   ; OUTI
site 03399   ; OUTI
site 0339B   ; OUTI
site 033A0   ; OUT ($BF),A
site 033A6   ; OUT ($BF),A
site 033AD   ; OUTD
site 033AF   ; OUTD
site 033B1   ; OUTD
site 033B3   ; OUTD
site 033B5   ; OUTD
site 033B7   ; OUTD
site 033B9   ; OUTD
site 033BB   ; OUTD
site 033BD   ; OUTD
site 033BF   ; OUTD
site 033C1   ; OUTD
site 033C3   ; OUTD
site 033C5   ; OUTD
site 033C7   ; OUTD
site 033C9   ; OUTD
site 033CB   ; OUTD
site 033CD   ; OUTD
site 033CF   ; OUTD
site 033D1   ; OUTD
site 033D3   ; OUTD
site 033D5   ; OUTD
site 033D7   ; OUTD
site 033D9   ; OUTD
site 033DB   ; OUTD
site 033DD   ; OUTD
site 033DF   ; OUTD
site 033E1   ; OUTD
site 033E3   ; OUTD
site 033E5   ; OUTD
site 033E7   ; OUTD
site 033E9   ; OUTD
site 033EB   ; OUTD
site 033ED   ; OUTD
site 033EF   ; OUTD
site 033F1   ; OUTD
site 033F3   ; OUTD
site 033F5   ; OUTD
site 033F7   ; OUTD
site 033F9   ; OUTD
site 033FB   ; OUTD
site 033FD   ; OUTD
site 033FF   ; OUTD
site 03401   ; OUTD
site 03403   ; OUTD
site 03405   ; OUTD
site 03407   ; OUTD
site 03409   ; OUTD
site 0340B   ; OUTD
site 0340D   ; OUTD
site 0340F   ; OUTD
site 03411   ; OUTD
site 03413   ; OUTD
site 03415   ; OUTD
site 03417   ; OUTD
site 03419   ; OUTD
site 0341B   ; OUTD
site 0341D   ; OUTD
site 0341F   ; OUTD
site 03421   ; OUTD
site 03423   ; OUTD
site 03425   ; OUTD
site 03427   ; OUTD
site 03429   ; OUTD
site 0342B   ; OUTD
site 0342F   ; OUT ($BF),A
site 03435   ; OUT ($BF),A
site 0343F   ; OUTI
site 03441   ; OUTI
site 03444   ; OUTI
site 03446   ; OUTI
site 03449   ; OUTI
site 0344B   ; OUTI
site 0344E   ; OUTI
site 03450   ; OUTI
site 03453   ; OUTI
site 03455   ; OUTI
site 03458   ; OUTI
site 0345A   ; OUTI
site 0345D   ; OUTI
site 0345F   ; OUTI
site 03462   ; OUTI
site 03464   ; OUTI
site 03467   ; OUTI
site 03469   ; OUTI
site 0346C   ; OUTI
site 0346E   ; OUTI
site 03471   ; OUTI
site 03473   ; OUTI
site 03476   ; OUTI
site 03478   ; OUTI
site 0347B   ; OUTI
site 0347D   ; OUTI
site 03480   ; OUTI
site 03482   ; OUTI
site 03485   ; OUTI
site 03487   ; OUTI
site 0348A   ; OUTI
site 0348C   ; OUTI
site 0348F   ; OUTI
site 03491   ; OUTI
site 03494   ; OUTI
site 03496   ; OUTI
site 03499   ; OUTI
site 0349B   ; OUTI
site 0349E   ; OUTI
site 034A0   ; OUTI
site 034A3   ; OUTI
site 034A5   ; OUTI
site 034A8   ; OUTI
site 034AA   ; OUTI
site 034AD   ; OUTI
site 034AF   ; OUTI
site 034B2   ; OUTI
site 034B4   ; OUTI
site 034B7   ; OUTI
site 034B9   ; OUTI
site 034BC   ; OUTI
site 034BE   ; OUTI
site 034C1   ; OUTI
site 034C3   ; OUTI
site 034C6   ; OUTI
site 034C8   ; OUTI
site 034CB   ; OUTI
site 034CD   ; OUTI
site 034D0   ; OUTI
site 034D2   ; OUTI
site 034D5   ; OUTI
site 034D7   ; OUTI
site 034DA   ; OUTI
site 034DC   ; OUTI
site 034DF   ; OUTI
site 034E1   ; OUTI
site 034E4   ; OUTI
site 034E6   ; OUTI
site 034E9   ; OUTI
site 034EB   ; OUTI
site 034EE   ; OUTI
site 034F0   ; OUTI
site 034F3   ; OUTI
site 034F5   ; OUTI
site 034F8   ; OUTI
site 034FA   ; OUTI
site 034FD   ; OUTI
site 034FF   ; OUTI
site 03502   ; OUTI
site 03504   ; OUTI
site 03507   ; OUTI
site 03509   ; OUTI
site 0350C   ; OUTI
site 0350E   ; OUTI
site 03511   ; OUTI
site 03513   ; OUTI
site 03516   ; OUTI
site 03518   ; OUTI
site 0351B   ; OUTI
site 0351D   ; OUTI
site 03520   ; OUTI
site 03522   ; OUTI
site 03525   ; OUTI
site 03527   ; OUTI
site 0352A   ; OUTI
site 0352C   ; OUTI
site 0352F   ; OUTI
site 03531   ; OUTI
site 03534   ; OUTI
site 03536   ; OUTI
site 03539   ; OUTI
site 0353B   ; OUTI
site 0353E   ; OUTI
site 03540   ; OUTI
site 03543   ; OUTI
site 03545   ; OUTI
site 03548   ; OUTI
site 0354A   ; OUTI
site 0354D   ; OUTI
site 0354F   ; OUTI
site 03552   ; OUTI
site 03554   ; OUTI
site 03557   ; OUTI
site 03559   ; OUTI
site 0355C   ; OUTI
site 0355E   ; OUTI
site 03561   ; OUTI
site 03563   ; OUTI
site 03566   ; OUTI
site 03568   ; OUTI
site 0356B   ; OUTI
site 0356D   ; OUTI
site 03570   ; OUTI
site 03572   ; OUTI
site 03575   ; OUTI
site 03577   ; OUTI
site 0357A   ; OUTI
site 0357C   ; OUTI
site 0366D   ; OUT ($BE),A
site 03675   ; OUT ($BE),A
site 03695   ; OUT ($BE),A
site 0369D   ; OUT ($BE),A
site 037DF   ; OUT ($BE),A
site 037E7   ; OUT ($BE),A
site 03811   ; OUT ($BE),A
site 03819   ; OUT ($BE),A
site 039BC   ; OUT ($BE),A
site 039C3   ; OUT ($BE),A
site 039D7   ; OUT ($BE),A
site 039DE   ; OUT ($BE),A
site 039F1   ; OUT ($BE),A
site 039F8   ; OUT ($BE),A
site 03A0C   ; OUT ($BE),A
site 03A13   ; OUT ($BE),A
site 03A30   ; OUT ($BE),A
site 03A37   ; OUT ($BE),A
site 03A68   ; OUT ($BE),A
site 03A6E   ; OUT ($BE),A
site 03AA0   ; OUT ($BE),A
site 03AA7   ; OUT ($BE),A
site 03AC7   ; OUT ($BE),A
site 03ACE   ; OUT ($BE),A
site 03F07   ; IN A,($DD)
site 03F17   ; IN A,($DC)
site 04061   ; OUT ($BE),A
site 04072   ; OUT ($BE),A
site 0418A   ; OUT ($BE),A
site 0418C   ; OUT ($BE),A
site 0418E   ; OUT ($BE),A
site 04190   ; OUT ($BE),A
site 04192   ; OUT ($BE),A
site 04194   ; OUT ($BE),A
site 04196   ; OUT ($BE),A
site 04198   ; OUT ($BE),A
site 0419A   ; OUT ($BE),A
site 0419C   ; OUT ($BE),A
site 0419E   ; OUT ($BE),A
site 041A0   ; OUT ($BE),A
site 041A2   ; OUT ($BE),A
site 041A4   ; OUT ($BE),A
site 041A6   ; OUT ($BE),A
site 04C95   ; OUT ($BF),A
site 04C98   ; OUT ($BF),A
site 04CA3   ; OUTI
site 04CA5   ; OUTI
site 04D94   ; OUT ($BF),A
site 04D97   ; OUT ($BF),A
site 04D9A   ; OUT ($BE),A
site 04D9F   ; OUT ($BE),A
site 04DB1   ; OUT ($BF),A
site 04DB4   ; OUT ($BF),A
site 081DD   ; OUT ($7F),A
site 08404   ; OTIR
site 0851C   ; OUT ($7F),A
site 08526   ; OUT ($7F),A
site 08543   ; OUT ($7F),A
site 08647   ; OUT ($7F),A
site 086D2   ; OUT ($7F),A
site 08774   ; OUT ($7F),A
site 0877D   ; OUT ($7F),A
site 0878D   ; OUT ($7F),A
site 087F3   ; OUT ($7F),A
site 08810   ; OUT ($7F),A
mapst 00008   ; LD ($FFFC),A
mapst 0000D   ; LD ($FFFD),A
mapst 00011   ; LD ($FFFE),A
mapst 00015   ; LD ($FFFF),A
mapst 00309   ; LD ($FFFC),A
mapst 0030E   ; LD ($FFFD),A
mapst 00312   ; LD ($FFFE),A
mapst 00316   ; LD ($FFFF),A
mapst 00322   ; LD ($FFFE),A
mapst 0032A   ; LD ($FFFF),A
mapst 00335   ; LD ($FFFE),A
mapst 00437   ; LD ($FFFF),A
mapst 00445   ; LD ($FFFF),A
mapst 0044E   ; LD ($FFFE),A
mapst 00453   ; LD ($FFFF),A
mapst 0045B   ; LD ($FFFE),A
mapst 0046D   ; LD ($FFFE),A
mapst 00473   ; LD ($FFFF),A
mapst 004CE   ; LD ($FFFE),A
mapst 0052F   ; LD ($FFFF),A
mapst 00540   ; LD ($FFFE),A
mapst 00545   ; LD ($FFFF),A
mapst 0054D   ; LD ($FFFE),A
mapst 0055E   ; LD ($FFFE),A
mapst 00564   ; LD ($FFFF),A
mapst 00735   ; LD ($FFFF),A
mapst 007D0   ; LD ($FFFF),A
mapst 008DE   ; LD ($FFFF),A
mapst 02F47   ; LD ($FFFF),A
mapst 0387F   ; LD ($FFFF),A
mapst 0389C   ; LD ($FFFF),A
mapst 038DD   ; LD ($FFFF),A
mapst 0392F   ; LD ($FFFF),A
mapst 0394B   ; LD ($FFFF),A
mapst 03F2C   ; LD ($FFFF),A
mapst 05DA2   ; LD ($FFFF),A
mapst 065CC   ; LD ($FFFF),A
mapst 065E5   ; LD ($FFFF),A
mapst 065FA   ; LD ($FFFF),A
mapst 067AE   ; LD ($FFFF),A
mapst 067F6   ; LD ($FFFF),A
mapst 06804   ; LD ($FFFF),A
mapst 06841   ; LD ($FFFF),A
mapst 06DCC   ; LD ($FFFF),A
mapst 06E16   ; LD ($FFFF),A
mapst 06E5A   ; LD ($FFFF),A
mapst 06E68   ; LD ($FFFF),A
mapst 06ED5   ; LD ($FFFF),A
mapst 06F34   ; LD ($FFFF),A
mapst 07410   ; LD ($FFFF),A
mapst 07433   ; LD ($FFFF),A
mapst 074BD   ; LD ($FFFF),A
mapst 074CD   ; LD ($FFFF),A
mapst 074ED   ; LD ($FFFF),A
mapst 074FD   ; LD ($FFFF),A

# Deep Duck Trouble Starring Donald Duck (Europe) (Action Replay).cht, "Infinite Lives": RAM
# $D2B1 is the number of lives, held at 3
poke "Infinite lives"
ar 00D2-B103
endpoke

# Deep Duck Trouble Starring Donald Duck (Europe) (Action Replay).cht, "Infinite Energy": RAM
# $D2B2 is the energy, held at 3, the full meter
poke "Infinite energy"
ar 00D2-B203
endpoke

# Deep Duck Trouble Starring Donald Duck (Europe) (Action Replay).cht, "Invincible": RAM $D369
# is held at 3; the game sets it to other values when Donald is hit, and with the code he
# takes no damage
poke "Invincibility"
ar 00D3-6903
endpoke

# Deep Duck Trouble Starring Donald Duck (Europe, Brazil).cht, "Start with ?? Lives, instead of
# 3": the load of the starting lives count; the game starts with the chosen number
poke "Start lives ??"
gg ??7-06F-E66
endpoke

# Deep Duck Trouble Starring Donald Duck (Europe, Brazil).cht, "Start with ?? Health Units,
# instead of 3": the two loads of the energy count, at the start and after a life is lost. The
# meter shows only the first diamonds of a count above 3
poke "Start health ??"
gg ??7-0BF-E66
gg ??4-4EE-E66
endpoke

# Deep Duck Trouble Starring Donald Duck (Europe, Brazil).cht, "Jump Height Modifier": the
# load of $FB80 into HL at $8201 (bank 31) becomes $FA80; the jump rises 78 pixels, not 52
poke "High jump"
gg FA2-027-085
endpoke
