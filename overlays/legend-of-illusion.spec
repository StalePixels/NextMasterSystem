# Legend of Illusion Starring Mickey Mouse (Brazil) (En), CRC32 6350E649, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of random
# input, 180 s of the attract mode) and the scan entries below.
# Decisions:
# - No RST vector has $FF filler, so $0000-$0002 (DI; IM 1) is the io vector and the
#   game starts at $0003.
# - The game maps code into slot 1 as well as slot 2. Object handlers: the type at
#   (IX+0) picks a bank from the table at $2327 (banks 1, 15, 16, 24) and an address from
#   the table at $2146 ($0E53); each handler is a scan entry in its bank. The level start
#   table at $1461 runs with bank 16 in slot 1 ($1441); the state tables at $52DA, $5629,
#   $5C8C (bank 15) and $6E13 (bank 16), the table at $400D (bank 24) and the table at
#   $4009 (bank 30, called from $04CA) are read by hand into scan entries.
# - The library routines $0929 (VRAM upload), $0B77 (VDP register write), $0BB6 (display
#   off), $0C0E, $0C19, $0C21 (VRAM address and byte helpers) and $0DF4 (tile map decoder)
#   in bank 0, $6AC9 in bank 16 and $4A15, $5121, $55A5 in bank 30 are code that no path or
#   recording reached; they are scan entries and their I/O and mapper stores are patched.
# - The table at $6394 (bank 15, object type $6F) is not a jump table the scanner can
#   read: it holds data, and the bytes it leads to in bank 15 ($4200-$46CC) are data.
#   The OUT ($FF),A at $3C5C4 there is not patched.
# - The byte scan's high-confidence mapper stores (LD A,n; LD ($FFFF),A; LD ($C13B),A, in
#   code of banks 1, 15, 16 and 30 that no path reached) are patched; the medium one at
#   $51F34 (bank 20) and the low ones are data.
# - The other I/O byte patterns that no path reached are tile graphics, tables or other
#   data (verdict false).
name Legend of Illusion Starring Mickey Mouse
cart 6350E649
hz 60		; No-Intro region Brazil
# Play writes 14,386 name table cells with the priority bit (reference log).
priority
# The line interrupt handler ($079E) sets H for the parallax bands and H = 0 for the status
# bar, up to 12 times a frame. Through the runtime those writes land late and the bar shows
# the playfield's scroll; the routine gives the scroll of every line. While its table is
# valid, the runtime does not move Layer 2 (the priority tiles) with the scroll, and the
# barrels of stage 1 showed at the left edge; the routine sets Layer 2's X and clip itself.
rastercode legend-of-illusion-raster.asm
vector 00 io
start 0003

# The frame code's tile upload ($5408, bank 1) writes 576 bytes (18 tiles) to VRAM $0040
# from HL = ($CB01) in the bank it maps at slot 2: as 12 runs of 48 OUTI ($5428), or, with
# ($D403) set, mirrored through the bit-reversal table at $0100 ($5492, 576 unrolled
# LD E,(HL); LD A,(DE); OUT ($BE),A; INC HL). Through the runtime each upload took a whole
# Next frame, and play dropped a game step in about one frame in five. Each path is a far
# call to page 0 and a RET; the callers ($05FC, $0628, $1398) use no register it returns.
asm 05425 5		; LD HL,($CB01); OUTI
    rst $00
    db far_io, pg_tiles, ent_tiles
    ret
endasm
asm 0548D 5		; LD HL,($CB01); LD D,$01
    rst $00
    db far_io, pg_tilesflip, ent_tilesflip
    ret
endasm
page 0 tiles tilesflip
; tiles: 576 bytes from HL = ($CB01), as the game sees it, to VRAM from the address the
; game set ($0040), in one jt_vwrite call (3 runs of 192 bytes). Three calls of 192
; one-byte runs measured slower in play (1.07 frames a game step against 1.02).
tiles:	ld hl,($CB01)
	xor a			; the source as the game sees it
.vw:	ld de,(vdp_addr)
	push ix
	push iy
	ld ix,192
	ld iy,192
	ld bc,$C003
	call jt_vwrite
	pop iy
	pop ix
	ret
; tilesflip: the same 576 bytes, each through the game's bit-reversal table at $0100
; (bank 0, readable here), into buf, then to VRAM in the same way. A source in
; $2000-$3FFF is read with jt_peek.
tilesflip:
	ld hl,($CB01)
	ld de,buf
	ld bc,576
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
	dec bc
	ld a,b
	or c
	jr nz,.l
	ld hl,buf
	ld a,1			; the source as mapped now: buf in this page
	jr tiles.vw
.pk:	call jt_peek
	jr .rv
buf:	ds 576
endpage
site 00019   ; IN A,($7E)
site 0003A   ; IN A,($BF)
site 00083   ; IN A,($DC)
site 000A5   ; OUT ($BE),A
site 005A9   ; OUT ($BF),A
site 005AD   ; OUT ($BF),A
site 005B2   ; OUT ($BF),A
site 005B6   ; OUT ($BF),A
site 005C9   ; OUT ($BF),A
site 005CD   ; OUT ($BF),A
site 005D2   ; OUT ($BF),A
site 005D6   ; OUT ($BF),A
site 0069F   ; OUT ($BF),A
site 006A3   ; OUT ($BF),A
site 006A8   ; OUT ($BF),A
site 006AC   ; OUT ($BF),A
site 00701   ; OUT ($BF),A
site 00705   ; OUT ($BF),A
site 00735   ; OUT ($BF),A
site 0073C   ; OUT ($BF),A
site 00741   ; OUT ($BF),A
site 00745   ; OUT ($BF),A
site 0074A   ; OUT ($BF),A
site 0074E   ; OUT ($BF),A
site 0075A   ; OUT ($BF),A
site 0075E   ; OUT ($BF),A
site 00764   ; OUT ($BF),A
site 00768   ; OUT ($BF),A
site 0076B   ; IN A,($BF)
site 00774   ; OUT ($BF),A
site 00778   ; OUT ($BF),A
site 0077F   ; OUT ($BF),A
site 00786   ; OUT ($BF),A
site 00795   ; OUT ($BF),A
site 00799   ; OUT ($BF),A
site 007B2   ; OUT ($BF),A
site 007B6   ; OUT ($BF),A
site 007BD   ; OUT ($BF),A
site 007C1   ; OUT ($BF),A
site 007EA   ; OUT ($BF),A
site 007F0   ; OUT ($BF),A
site 007F8   ; OUT ($BE),A
site 00806   ; OUT ($BF),A
site 0080C   ; OUT ($BF),A
site 00813   ; OUT ($BE),A
site 00817   ; OUT ($BE),A
site 0081B   ; OUT ($BF),A
site 00821   ; OUT ($BF),A
site 00828   ; OUT ($BE),A
site 0082C   ; OUT ($BE),A
site 00850   ; OUT ($BE),A
site 00854   ; OUT ($BE),A
site 0088D   ; OUT ($BF),A
site 00892   ; OUT ($BF),A
site 00896   ; OUT ($BE),A
site 0089A   ; OUT ($BE),A
site 008BA   ; OUT ($BF),A
site 008C1   ; OUT ($BF),A
site 008CA   ; OUT ($BE),A
site 00906   ; OUT ($BF),A
site 0090B   ; OUT ($BF),A
site 0090E   ; OUT ($BE),A
site 00936   ; OUT ($BF),A
site 0093D   ; OUT ($BF),A
site 00946   ; OUT ($BE),A
site 00955   ; IN A,($BF)
site 00957   ; IN A,($BF)
site 00963   ; IN A,($BF)
site 00994   ; OUT ($BF),A
site 00998   ; OUT ($BF),A
site 0099F   ; OUTI
site 009A1   ; OUTI
site 009A3   ; OUTI
site 009A5   ; OUTI
site 009A7   ; OUTI
site 009A9   ; OUTI
site 009AB   ; OUTI
site 009AD   ; OUTI
site 009AF   ; OUTI
site 009B1   ; OUTI
site 009B3   ; OUTI
site 009B5   ; OUTI
site 009B7   ; OUTI
site 009B9   ; OUTI
site 009BB   ; OUTI
site 009BD   ; OUTI
site 009BF   ; OUTI
site 009C1   ; OUTI
site 009C3   ; OUTI
site 009C5   ; OUTI
site 009C7   ; OUTI
site 009C9   ; OUTI
site 009CB   ; OUTI
site 009CD   ; OUTI
site 009CF   ; OUTI
site 009D1   ; OUTI
site 009D3   ; OUTI
site 009D5   ; OUTI
site 009D7   ; OUTI
site 009D9   ; OUTI
site 009DB   ; OUTI
site 009DD   ; OUTI
site 009DF   ; OUTI
site 009E1   ; OUTI
site 009E3   ; OUTI
site 009E5   ; OUTI
site 009E7   ; OUTI
site 009E9   ; OUTI
site 009EB   ; OUTI
site 009ED   ; OUTI
site 009EF   ; OUTI
site 009F1   ; OUTI
site 009F3   ; OUTI
site 009F5   ; OUTI
site 009F7   ; OUTI
site 009F9   ; OUTI
site 009FB   ; OUTI
site 009FD   ; OUTI
site 009FF   ; OUTI
site 00A01   ; OUTI
site 00A03   ; OUTI
site 00A05   ; OUTI
site 00A07   ; OUTI
site 00A09   ; OUTI
site 00A0B   ; OUTI
site 00A0D   ; OUTI
site 00A0F   ; OUTI
site 00A11   ; OUTI
site 00A13   ; OUTI
site 00A15   ; OUTI
site 00A17   ; OUTI
site 00A19   ; OUTI
site 00A1B   ; OUTI
site 00A1D   ; OUTI
site 00A21   ; OUT ($BF),A
site 00A25   ; OUT ($BF),A
site 00A2A   ; OUTI
site 00A2C   ; OUTI
site 00A2E   ; OUTI
site 00A30   ; OUTI
site 00A32   ; OUTI
site 00A34   ; OUTI
site 00A36   ; OUTI
site 00A38   ; OUTI
site 00A3A   ; OUTI
site 00A3C   ; OUTI
site 00A3E   ; OUTI
site 00A40   ; OUTI
site 00A42   ; OUTI
site 00A44   ; OUTI
site 00A46   ; OUTI
site 00A48   ; OUTI
site 00A4A   ; OUTI
site 00A4C   ; OUTI
site 00A4E   ; OUTI
site 00A50   ; OUTI
site 00A52   ; OUTI
site 00A54   ; OUTI
site 00A56   ; OUTI
site 00A58   ; OUTI
site 00A5A   ; OUTI
site 00A5C   ; OUTI
site 00A5E   ; OUTI
site 00A60   ; OUTI
site 00A62   ; OUTI
site 00A64   ; OUTI
site 00A66   ; OUTI
site 00A68   ; OUTI
site 00A6A   ; OUTI
site 00A6C   ; OUTI
site 00A6E   ; OUTI
site 00A70   ; OUTI
site 00A72   ; OUTI
site 00A74   ; OUTI
site 00A76   ; OUTI
site 00A78   ; OUTI
site 00A7A   ; OUTI
site 00A7C   ; OUTI
site 00A7E   ; OUTI
site 00A80   ; OUTI
site 00A82   ; OUTI
site 00A84   ; OUTI
site 00A86   ; OUTI
site 00A88   ; OUTI
site 00A8A   ; OUTI
site 00A8C   ; OUTI
site 00A8E   ; OUTI
site 00A90   ; OUTI
site 00A92   ; OUTI
site 00A94   ; OUTI
site 00A96   ; OUTI
site 00A98   ; OUTI
site 00A9A   ; OUTI
site 00A9C   ; OUTI
site 00A9E   ; OUTI
site 00AA0   ; OUTI
site 00AA2   ; OUTI
site 00AA4   ; OUTI
site 00AA6   ; OUTI
site 00AA8   ; OUTI
site 00AAA   ; OUTI
site 00AAC   ; OUTI
site 00AAE   ; OUTI
site 00AB0   ; OUTI
site 00AB2   ; OUTI
site 00AB4   ; OUTI
site 00AB6   ; OUTI
site 00AB8   ; OUTI
site 00ABA   ; OUTI
site 00ABC   ; OUTI
site 00ABE   ; OUTI
site 00AC0   ; OUTI
site 00AC2   ; OUTI
site 00AC4   ; OUTI
site 00AC6   ; OUTI
site 00AC8   ; OUTI
site 00ACA   ; OUTI
site 00ACC   ; OUTI
site 00ACE   ; OUTI
site 00AD0   ; OUTI
site 00AD2   ; OUTI
site 00AD4   ; OUTI
site 00AD6   ; OUTI
site 00AD8   ; OUTI
site 00ADA   ; OUTI
site 00ADC   ; OUTI
site 00ADE   ; OUTI
site 00AE0   ; OUTI
site 00AE2   ; OUTI
site 00AE4   ; OUTI
site 00AE6   ; OUTI
site 00AE8   ; OUTI
site 00AEA   ; OUTI
site 00AEC   ; OUTI
site 00AEE   ; OUTI
site 00AF0   ; OUTI
site 00AF2   ; OUTI
site 00AF4   ; OUTI
site 00AF6   ; OUTI
site 00AF8   ; OUTI
site 00AFA   ; OUTI
site 00AFC   ; OUTI
site 00AFE   ; OUTI
site 00B00   ; OUTI
site 00B02   ; OUTI
site 00B04   ; OUTI
site 00B06   ; OUTI
site 00B08   ; OUTI
site 00B0A   ; OUTI
site 00B0C   ; OUTI
site 00B0E   ; OUTI
site 00B10   ; OUTI
site 00B12   ; OUTI
site 00B14   ; OUTI
site 00B16   ; OUTI
site 00B18   ; OUTI
site 00B1A   ; OUTI
site 00B1C   ; OUTI
site 00B1E   ; OUTI
site 00B20   ; OUTI
site 00B22   ; OUTI
site 00B24   ; OUTI
site 00B26   ; OUTI
site 00B28   ; OUTI
site 00B53   ; IN A,($BF)
site 00B60   ; OUT ($BF),A
site 00B64   ; OUT ($BF),A
site 00B7A   ; OUT ($BF),A
site 00B7F   ; OUT ($BF),A
site 00B93   ; OUT ($BF),A
site 00B97   ; OUT ($BF),A
site 00BA1   ; OUT ($BF),A
site 00BA5   ; OUT ($BF),A
site 00BAF   ; OUT ($BF),A
site 00BB3   ; OUT ($BF),A
site 00BBD   ; OUT ($BF),A
site 00BC1   ; OUT ($BF),A
site 00BD1   ; OUT ($BE),A
site 00BD3   ; OUT ($BE),A
site 00BD5   ; OUT ($BE),A
site 00BD7   ; OUT ($BE),A
site 00BD9   ; OUT ($BE),A
site 00BDB   ; OUT ($BE),A
site 00BDD   ; OUT ($BE),A
site 00BDF   ; OUT ($BE),A
site 00BE1   ; OUT ($BE),A
site 00BE3   ; OUT ($BE),A
site 00BE5   ; OUT ($BE),A
site 00BE7   ; OUT ($BE),A
site 00BE9   ; OUT ($BE),A
site 00BEB   ; OUT ($BE),A
site 00BED   ; OUT ($BE),A
site 00BEF   ; OUT ($BE),A
site 00C05   ; OUT ($BF),A
site 00C0A   ; OUT ($BF),A
site 00C0F   ; OUT ($BF),A
site 00C14   ; OUT ($BF),A
site 00C1E   ; OUT ($BE),A
site 00C29   ; OUT ($BE),A
site 00C2D   ; IN A,($BE)
site 00C3B   ; OUT ($BE),A
site 00C40   ; OUT ($BE),A
site 00C4E   ; OUT ($BE),A
site 00DF6   ; OUT ($BF),A
site 00DFB   ; OUT ($BF),A
site 00E07   ; OTIR
site 00E11   ; OUT ($BE),A
site 01274   ; OUT ($BF),A
site 0127A   ; OUT ($BF),A
site 0127F   ; OUT ($BE),A
site 01347   ; OUT ($BF),A
site 0134B   ; OUT ($BF),A
site 0134F   ; OUT ($BF),A
site 01353   ; OUT ($BF),A
site 013FF   ; OUT ($BF),A
site 01404   ; OUT ($BF),A
site 0140A   ; OUT ($BE),A
site 014EC   ; OUT ($BF),A
site 014F2   ; OUT ($BF),A
site 023CE   ; OUT ($BF),A
site 023D5   ; OUT ($BF),A
site 023DC   ; OUTI
site 023DE   ; OUTI
site 023E0   ; OUTI
site 023E2   ; OUTI
site 023E4   ; OUTI
site 023E6   ; OUTI
site 023E8   ; OUTI
site 023EA   ; OUTI
site 023EC   ; OUTI
site 023EE   ; OUTI
site 023F0   ; OUTI
site 023F2   ; OUTI
site 023F4   ; OUTI
site 023F6   ; OUTI
site 023F8   ; OUTI
site 023FA   ; OUTI
site 023FC   ; OUTI
site 023FE   ; OUTI
site 02400   ; OUTI
site 02402   ; OUTI
site 02404   ; OUTI
site 02406   ; OUTI
site 02408   ; OUTI
site 0240A   ; OUTI
site 0240C   ; OUTI
site 0240E   ; OUTI
site 02410   ; OUTI
site 02412   ; OUTI
site 02414   ; OUTI
site 02416   ; OUTI
site 02418   ; OUTI
site 0241A   ; OUTI
site 02501   ; OUT ($BF),A
site 02506   ; OUT ($BF),A
site 02509   ; OUT ($BE),A
site 0250D   ; OUT ($BE),A
site 02691   ; OUT ($BF),A
site 02697   ; OUT ($BF),A
site 027CA   ; OUT ($BF),A
site 027CF   ; OUT ($BF),A
site 027D2   ; OUT ($BE),A
site 027D6   ; OUT ($BE),A
site 02CF9   ; OUT ($BE),A
site 02D0A   ; OUT ($BE),A
site 03B7C   ; OUT ($BF),A
site 03B80   ; OUT ($BF),A
site 03B83   ; OUT ($BF),A
site 03B87   ; OUT ($BF),A
site 03BB8   ; OUT ($BF),A
site 03BBC   ; OUT ($BF),A
site 03BC1   ; OUT ($BE),A
site 03BC7   ; OUT ($BF),A
site 03BCB   ; OUT ($BF),A
site 03BD1   ; OUT ($BE),A
site 03D2A   ; OUT ($BF),A
site 03D2F   ; OUT ($BF),A
site 03E19   ; OUT ($BF),A
site 03E1E   ; OUT ($BF),A
site 03E23   ; OUT ($BE),A
site 03E27   ; OUT ($BE),A
site 05414   ; OUT ($BF),A
site 05418   ; OUT ($BF),A
site 0665B   ; OUT ($BF),A
site 06662   ; OUT ($BF),A
site 06669   ; OUTI
site 0666B   ; OUTI
site 0666D   ; OUTI
site 0666F   ; OUTI
site 06671   ; OUTI
site 06673   ; OUTI
site 06675   ; OUTI
site 06677   ; OUTI
site 06679   ; OUTI
site 0667B   ; OUTI
site 0667D   ; OUTI
site 0667F   ; OUTI
site 06681   ; OUTI
site 06683   ; OUTI
site 06685   ; OUTI
site 06687   ; OUTI
site 06689   ; OUTI
site 0668B   ; OUTI
site 0668D   ; OUTI
site 0668F   ; OUTI
site 06691   ; OUTI
site 06693   ; OUTI
site 06695   ; OUTI
site 06697   ; OUTI
site 06699   ; OUTI
site 0669B   ; OUTI
site 0669D   ; OUTI
site 0669F   ; OUTI
site 066A1   ; OUTI
site 066A3   ; OUTI
site 066A5   ; OUTI
site 066A7   ; OUTI
site 066A9   ; OUTI
site 066AB   ; OUTI
site 066AD   ; OUTI
site 066AF   ; OUTI
site 066B1   ; OUTI
site 066B3   ; OUTI
site 066B5   ; OUTI
site 066B7   ; OUTI
site 066B9   ; OUTI
site 066BB   ; OUTI
site 066BD   ; OUTI
site 066BF   ; OUTI
site 066C1   ; OUTI
site 066C3   ; OUTI
site 066C5   ; OUTI
site 066C7   ; OUTI
site 066C9   ; OUTI
site 066CB   ; OUTI
site 066CD   ; OUTI
site 066CF   ; OUTI
site 066D1   ; OUTI
site 066D3   ; OUTI
site 066D5   ; OUTI
site 066D7   ; OUTI
site 066D9   ; OUTI
site 066DB   ; OUTI
site 066DD   ; OUTI
site 066DF   ; OUTI
site 066E1   ; OUTI
site 066E3   ; OUTI
site 066E5   ; OUTI
site 066E7   ; OUTI
site 06DE0   ; OUT ($BF),A
site 06DE7   ; OUT ($BF),A
site 06DEC   ; OUTI
site 06DEE   ; OUTI
site 06DF0   ; OUTI
site 06DF2   ; OUTI
site 06E03   ; OUT ($BF),A
site 06E08   ; OUT ($BF),A
site 06E0D   ; OUTI
site 06E0F   ; OUTI
site 06E11   ; OUTI
site 06E13   ; OUTI
site 07EAA   ; OUT ($BF),A
site 07EAE   ; OUT ($BF),A
site 07F03   ; OUT ($BF),A
site 07F0A   ; OUT ($BF),A
site 07F13   ; OTIR
site 07F18   ; OUT ($BF),A
site 07F1F   ; OUT ($BF),A
site 07F23   ; OTIR
site 07F49   ; OUT ($BF),A
site 07F4C   ; OUT ($BF),A
site 07F52   ; OUT (C),D
site 07F57   ; OUT (C),E
site 07FD8   ; OUT ($BE),A
site 07FDD   ; OUT ($BE),A
site 07FE5   ; OUT ($BF),A
site 07FEA   ; OUT ($BF),A
site 081F1   ; OUT ($7F),A
site 08419   ; OTIR
site 085A4   ; OUT ($7F),A
site 085AE   ; OUT ($7F),A
site 085FB   ; OUT ($7F),A
site 08652   ; OUT ($7F),A
site 086FB   ; OUT ($7F),A
site 087E7   ; OUT ($7F),A
site 087ED   ; OUT ($7F),A
site 087FD   ; OUT ($7F),A
site 08889   ; OUT ($7F),A
site 088A6   ; OUT ($7F),A
site 4134A   ; OUT ($BF),A
site 4134D   ; OUT ($BF),A
site 4134F   ; IN A,($BE)
site 41DDE   ; OUT ($BF),A
site 41DE5   ; OUT ($BF),A
site 41DEA   ; OUT ($BE),A
site 42880   ; OUT ($BF),A
site 42884   ; OUT ($BF),A
site 428A1   ; OUT ($BF),A
site 428A7   ; OUT ($BF),A
site 42B0D   ; OUT ($BF),A
site 42B13   ; OUT ($BF),A
site 42B19   ; OUT ($BE),A
site 42CA8   ; OUT ($BF),A
site 42CAE   ; OUT ($BF),A
site 43ABE   ; OUT ($BF),A
site 43AC4   ; OUT ($BF),A
site 43AD6   ; OUT ($BF),A
site 43ADB   ; OUT ($BF),A
site 43AE0   ; OUT ($BE),A
site 43AE4   ; OUT ($BE),A
site 43C3B   ; OUT ($BF),A
site 43C3E   ; OUT ($BF),A
site 43C44   ; OUT (C),E
site 43C48   ; OUT (C),D
site 60048   ; OUT ($BF),A
site 6004E   ; OUT ($BF),A
site 600D0   ; OUT ($BF),A
site 600D6   ; OUT ($BF),A
site 600F9   ; OUT ($BF),A
site 600FF   ; OUT ($BF),A
site 6019E   ; OUT ($BF),A
site 601A3   ; OUT ($BF),A
site 601AC   ; OUT ($BE),A
site 60354   ; OUT ($BF),A
site 60359   ; OUT ($BF),A
site 60362   ; OTIR
site 60372   ; OUT ($BF),A
site 60377   ; OUT ($BF),A
site 60380   ; OTIR
site 63E58   ; OUT ($BE),A
site 63E5C   ; OUT ($BE),A
site 7802D   ; OUT ($BF),A
site 78033   ; OUT ($BF),A
site 7803C   ; OUT ($BE),A
site 78214   ; OUT ($BF),A
site 7821A   ; OUT ($BF),A
site 78220   ; OUT ($BE),A
site 78224   ; OUT ($BE),A
site 78227   ; OUT ($BE),A
site 78229   ; OUT ($BE),A
site 78234   ; OUT ($BF),A
site 7823A   ; OUT ($BF),A
site 78240   ; OUT ($BE),A
site 78242   ; OUT ($BE),A
site 784D8   ; OUT ($BF),A
site 784DD   ; OUT ($BF),A
site 7852C   ; OUT ($BF),A
site 78532   ; OUT ($BF),A
site 78538   ; OUT ($BE),A
site 7853C   ; OUT ($BE),A
site 7854A   ; OUT ($BF),A
site 78550   ; OUT ($BF),A
site 78556   ; OUT ($BE),A
site 7855A   ; OUT ($BE),A
site 785A7   ; OUT ($BF),A
site 785AC   ; OUT ($BF),A
site 787FE   ; OUT ($BF),A
site 78802   ; OUT ($BF),A
site 78808   ; OUT ($BE),A
site 7880B   ; OUT ($BE),A
site 78839   ; OUT ($BF),A
site 7883F   ; OUT ($BF),A
site 78845   ; OUT ($BE),A
site 78849   ; OUT ($BE),A
site 7884C   ; OUT ($BE),A
site 7884E   ; OUT ($BE),A
site 788FF   ; OUT ($BF),A
site 78905   ; OUT ($BF),A
site 78EDA   ; OUT ($BF),A
site 78EE0   ; OUT ($BF),A
site 78EE6   ; OUT ($BE),A
site 78EEA   ; OUT ($BE),A
site 78EED   ; OUT ($BE),A
site 78EEF   ; OUT ($BE),A
site 78F0B   ; OUT ($BF),A
site 78F11   ; OUT ($BF),A
site 78F17   ; OUT ($BE),A
site 78F1A   ; OUT ($BE),A
site 7913D   ; OUT ($BF),A
site 79142   ; OUT ($BF),A
site 79562   ; OUT ($BF),A
site 79567   ; OUT ($BF),A
site 7956A   ; OUT ($BE),A
site 79589   ; OUT ($BF),A
site 7958E   ; OUT ($BF),A
site 79591   ; OUT ($BE),A
site 795AF   ; OUT ($BF),A
site 795B4   ; OUT ($BF),A
site 795B7   ; OUT ($BE),A
mapst 00008   ; LD ($FFFC),A
mapst 0000D   ; LD ($FFFD),A
mapst 00011   ; LD ($FFFE),A
mapst 00016   ; LD ($FFFF),A
mapst 00416   ; LD ($FFFC),A
mapst 0041B   ; LD ($FFFD),A
mapst 00422   ; LD ($FFFE),A
mapst 0042A   ; LD ($FFFF),A
mapst 00483   ; LD ($FFFE),A
mapst 004CC   ; LD ($FFFE),A
mapst 004D7   ; LD ($FFFE),A
mapst 004E2   ; LD ($FFFE),A
mapst 004ED   ; LD ($FFFE),A
mapst 004FB   ; LD ($FFFE),A
mapst 00506   ; LD ($FFFE),A
mapst 005DA   ; LD ($FFFE),A
mapst 0060C   ; LD ($FFFE),A
mapst 00642   ; LD ($FFFE),A
mapst 0064D   ; LD ($FFFE),A
mapst 0067D   ; LD ($FFFE),A
mapst 00689   ; LD ($FFFE),A
mapst 006B3   ; LD ($FFFE),A
mapst 006B8   ; LD ($FFFF),A
mapst 006C7   ; LD ($FFFE),A
mapst 006D3   ; LD ($FFFF),A
mapst 007D5   ; LD ($FFFE),A
mapst 00839   ; LD ($FFFF),A
mapst 008DE   ; LD ($FFFE),A
mapst 008E7   ; LD ($FFFF),A
mapst 00CF1   ; LD ($FFFE),A
mapst 00CFD   ; LD ($FFFE),A
mapst 00D82   ; LD ($FFFF),A
mapst 00DA7   ; LD ($FFFF),A
mapst 00E21   ; LD ($FFFF),A
mapst 00E3F   ; LD ($FFFE),A
mapst 00E4A   ; LD ($FFFF),A
mapst 00E60   ; LD ($FFFE),A
mapst 00F72   ; LD ($FFFF),A
mapst 01040   ; LD ($FFFF),A
mapst 0104C   ; LD ($FFFF),A
mapst 01357   ; LD ($FFFF),A
mapst 013B6   ; LD ($FFFF),A
mapst 01443   ; LD ($FFFE),A
mapst 0145A   ; LD ($FFFE),A
mapst 014E4   ; LD ($FFFF),A
mapst 01549   ; LD ($FFFE),A
mapst 0156E   ; LD ($FFFE),A
mapst 015D6   ; LD ($FFFE),A
mapst 019BD   ; LD ($FFFF),A
mapst 019CA   ; LD ($FFFF),A
mapst 023BD   ; LD ($FFFF),A
mapst 0243D   ; LD ($FFFF),A
mapst 0246D   ; LD ($FFFF),A
mapst 0264F   ; LD ($FFFF),A
mapst 0267F   ; LD ($FFFF),A
mapst 02684   ; LD ($FFFF),A
mapst 02740   ; LD ($FFFF),A
mapst 02916   ; LD ($FFFF),A
mapst 03746   ; LD ($FFFE),A
mapst 03A72   ; LD ($FFFF),A
mapst 03BF1   ; LD ($FFFF),A
mapst 03E41   ; LD ($FFFF),A
mapst 04025   ; LD ($FFFF),A
mapst 0540F   ; LD ($FFFF),A
mapst 06003   ; LD ($FFFF),A
mapst 0664E   ; LD ($FFFF),A
mapst 069C5   ; LD ($FFFF),A
mapst 06AB9   ; LD ($FFFF),A
mapst 06AF4   ; LD ($FFFF),A
mapst 06B51   ; LD ($FFFF),A
mapst 06B97   ; LD ($FFFF),A
mapst 06CE9   ; LD ($FFFF),A
mapst 06EBB   ; LD ($FFFF),A
mapst 07605   ; LD ($FFFF),A
mapst 07653   ; LD ($FFFF),A
mapst 07664   ; LD ($FFFF),A
mapst 07A06   ; LD ($FFFF),A
mapst 3FEA8   ; LD ($FFFF),A
mapst 41481   ; LD ($FFFF),A
mapst 41CC3   ; LD ($FFFF),A
mapst 41D50   ; LD ($FFFF),A
mapst 41DD0   ; LD ($FFFF),A
mapst 42899   ; LD ($FFFF),A
mapst 42ACB   ; LD ($FFFF),A
mapst 42ADF   ; LD ($FFFF),A
mapst 42AF3   ; LD ($FFFF),A
mapst 42CA0   ; LD ($FFFF),A
mapst 4387D   ; LD ($FFFF),A
mapst 43891   ; LD ($FFFF),A
mapst 43A9E   ; LD ($FFFF),A
mapst 43AB2   ; LD ($FFFF),A
mapst 600ED   ; LD ($FFFF),A
mapst 60113   ; LD ($FFFF),A
mapst 60278   ; LD ($FFFF),A
mapst 78089   ; LD ($FFFF),A
mapst 781F8   ; LD ($FFFF),A
mapst 782D7   ; LD ($FFFF),A
mapst 78322   ; LD ($FFFF),A
mapst 783DB   ; LD ($FFFF),A
mapst 78413   ; LD ($FFFF),A
mapst 784BF   ; LD ($FFFF),A
mapst 786CD   ; LD ($FFFF),A
mapst 786FB   ; LD ($FFFF),A
mapst 78814   ; LD ($FFFF),A
mapst 788F3   ; LD ($FFFF),A
mapst 78A21   ; LD ($FFFF),A
mapst 78EBE   ; LD ($FFFF),A
mapst 79124   ; LD ($FFFF),A
mapst 792FA   ; LD ($FFFF),A
mapst 799D1   ; LD ($FFFF),A
mapst 06E1B   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 3FB14   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 3FB44   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 3FE6A   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 429E0   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 78B13   # LD ($FFFF),A; after LD A,$16; 32 bytes of valid code before it
mapst 78B2A   # LD ($FFFF),A; after LD A,$16; 32 bytes of valid code before it
mapst 78F93   # LD ($FFFF),A; after LD A,$16; 32 bytes of valid code before it
mapst 78FE0   # LD ($FFFF),A; after LD A,$16; 32 bytes of valid code before it
mapst 79070   # LD ($FFFF),A; after LD A,$1C; 32 bytes of valid code before it
mapst 7934C   # LD ($FFFF),A; after LD A,$1E; 32 bytes of valid code before it

# Legend of Illusion Starring Mickey Mouse (Brazil) (Action Replay).cht, "Infinite Lives": RAM
# $C304 is the number of lives; held at 9, a lost life does not use one up
poke "Infinite lives"
ar 00C3-0409
endpoke

# Legend of Illusion Starring Mickey Mouse (Brazil) (Action Replay).cht, "Infinite Hearts
# (Hits)": RAM $C305 is the number of hearts; held at 9, hits do not use them up
poke "Infinite hearts"
ar 00C3-0509
endpoke
