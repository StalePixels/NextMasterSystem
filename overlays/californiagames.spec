# California Games (USA, Europe, Brazil) (En), CRC32 AC6009A7, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log and the
# reference logs of each of the six events in practice mode (reflogs/events-AC6009A7).
# The game runs each event's step in the foreground, then the frame handler ($13F4) does the
# step's VRAM work when $C100 is set; line interrupt handlers (through $C105) change H scroll
# and CRAM 0 per band. On the Master System every event makes one step a frame.
# hsplit: skating, BMX and flying disc set H scroll in line interrupts for bands; without it
# the lower bands showed the wrong map columns and the skating obstacles sat off place.
# Priority cells (the BMX ramp and fence, the surfing wave lip, the half pipe) cover the rider.
# The priority switch is off: its once-a-frame work cost more than a BMX or surfing step can
# hold. Page 0 keeps Layer 2 itself, as the switch would show it (see l2svc): set up at the
# first palette upload, redrawn whole from the name table after each screen set-up ($0950,
# scr), and where the game writes cells (bmx, scol, cq: the cells' marks, then l2go). The
# game's V scroll is always 0, so Layer 2 line y is SMS line y; the runtime sets Layer 2's X
# (pri_x into NextReg $16) and clip window with or without the switch.
# The game takes random numbers from R at start and from a generator stepped by the frame
# handler, so the waves, obstacles and messages differ from the reference after a load.
# The game checks the region ($0695): the Next takes the export path (no SEGA logo), the
# reference (sg1000m3) the Japanese one, so the title sequence runs about 300 frames ahead.
# Page 0 uses these runtime internals (addresses in build/rt/runtime.map of public/ at
# 9753a1e): jt_vwrite, jt_peek, vdp_addr $E037, vdp_code $E036, vdp_latch $E035, vdp_rbuf
# $E039, vdp_status $E03A, vdp_regs $E03B, nt_base $E04B, cram $E04D, cur_mmu $E02D, m224
# $E08F, pal43 $E09F, tiles_dirty $E082, region_tab $E400, dirty_pages $E440, mapattr_table
# $E200, pal_hi_table $E300, pal_lo_table $E340; MAP_PAGE 14 (M0 $0000, A8 $0A00, and the
# priority marks, unused by the runtime without the switch: $1BC0/$1BE0 + row, $1C00 + cell),
# SHADOW_PAGE 28-29, TILE_PAGE 10-11, L2_PAGE 102-107, FW2_PAGE 25 (lay15 $27BA), L2_TRANS $24.
name California Games
cart AC6009A7
hz any		; No-Intro regions USA, Europe, Brazil
hsplit
# No free RST vector: $0000-$0002 (DI; LD HL,$FFFC) becomes the vector. The reset code
# sets the mapper and jumps to $029C, which sets it again at $02D6; the game starts there.
vector 00 io
start 029C
asm 002D4 2   ; IM 1 -> IM 2
    im 2
endasm
site 002E6   ; OUT ($3F),A
site 0030A   ; OUT ($3F),A
site 00697   ; OUT ($3F),A
site 00699   ; IN A,($DD)
site 006A3   ; OUT ($3F),A
site 006A5   ; IN A,($DD)
site 006BD   ; IN A,($BF)
site 006C3   ; IN A,($BF)
site 006CA   ; IN A,($BF)
site 006F9   ; OUT ($3E),A
site 00701   ; OUT ($F2),A
site 00704   ; IN A,($F2)
site 00716   ; OUT ($F2),A
site 0071E   ; OUT ($3E),A
site 0072E   ; OUT ($F2),A
site 00730   ; IN A,($F2)
site 008A0   ; OUT ($BF),A
site 008A3   ; OUT ($BF),A
site 008A7   ; OUT ($BF),A
site 008AA   ; OUT ($BF),A
site 008AD   ; OUT ($BE),A
site 008B2   ; OUT ($BE),A
site 008D6   ; OUT ($BE),A
site 008ED   ; OUT ($BE),A
site 008F2   ; OUT ($BE),A
site 00900   ; OUTI
site 00912   ; INI
site 00928   ; OUT ($BE),A
site 0092D   ; OUT ($BE),A
site 00932   ; OUT ($BE),A
site 00937   ; OUT ($BE),A
site 0093C   ; OUT ($BE),A
site 00941   ; OUT ($BE),A
site 00946   ; OUT ($BE),A
site 0094B   ; OUT ($BE),A
site 00957   ; OUT ($BF),A
site 0095E   ; OUT ($BF),A
site 00966   ; OUT ($BF),A
site 0096A   ; OUT ($BF),A
site 0096E   ; OUT ($BE),A
site 00977   ; OUT ($BF),A
site 0097B   ; OUT ($BF),A
site 0097F   ; OUT ($BE),A
site 009EC   ; OUT ($BE),A
site 00A00   ; OUT ($BE),A
site 00A05   ; OUT ($BE),A
site 00A0C   ; OUT ($BE),A
site 00A13   ; OUT ($BE),A
site 00A22   ; OUT ($BE),A
site 00A27   ; OUT ($BE),A
site 00A3F   ; OUT ($BE),A
site 00A45   ; OUT ($BE),A
site 00ADA   ; OUT ($BE),A
site 00AE0   ; OUT ($BE),A
site 00E22   ; OUT ($BF),A
site 00E25   ; OUT ($BF),A
site 00EF8   ; OUT ($BE),A
site 00EFD   ; OUT ($BE),A
site 00F02   ; OUT ($BE),A
site 00F07   ; OUT ($BE),A
site 01293   ; OUT ($BF),A
site 01297   ; OUT ($BF),A
site 013FB   ; IN A,($DD)
site 01416   ; OUT ($BF),A
site 0141A   ; OUT ($BF),A
site 01441   ; OUT ($BF),A
site 01445   ; OUT ($BF),A
site 01448   ; OUT ($BF),A
site 0144C   ; OUT ($BF),A
site 01451   ; OUT ($BF),A
site 01455   ; OUT ($BF),A
site 0152E   ; OUT ($BF),A
site 01532   ; OUT ($BF),A
site 01540   ; OUT ($BF),A
site 01544   ; OUT ($BF),A
site 01548   ; OUT ($BE),A
site 01562   ; OUT ($BF),A
site 01566   ; OUT ($BF),A
site 0157F   ; OUT ($BF),A
site 01583   ; OUT ($BF),A
site 0159B   ; OUT ($BF),A
site 0159F   ; OUT ($BF),A
site 015B7   ; OUT ($BF),A
site 015BB   ; OUT ($BF),A
site 015D5   ; OUT ($BF),A
site 015D9   ; OUT ($BF),A
site 015E5   ; OUT ($BF),A
site 015E9   ; OUT ($BF),A
site 015FB   ; OUT ($BF),A
site 015FF   ; OUT ($BF),A
site 01603   ; OUT ($BE),A
site 01618   ; OUT ($BF),A
site 0161C   ; OUT ($BF),A
site 01636   ; OUT ($BF),A
site 0163A   ; OUT ($BF),A
site 0164C   ; OUT ($BF),A
site 01650   ; OUT ($BF),A
site 01654   ; OUT ($BE),A
site 01660   ; OUT ($BF),A
site 01664   ; OUT ($BF),A
site 01668   ; OUT ($BE),A
site 01672   ; OUT ($BF),A
site 01676   ; OUT ($BF),A
site 01685   ; OUT ($BF),A
site 01689   ; OUT ($BF),A
site 01691   ; OUT ($BF),A
site 01695   ; OUT ($BF),A
site 01699   ; OUT ($BE),A
site 016BB   ; OUT ($BF),A
site 016BF   ; OUT ($BF),A
site 016C3   ; OUT ($BE),A
site 016D6   ; OUT ($BF),A
site 016DA   ; OUT ($BF),A
site 016DE   ; OUT ($BE),A
site 016EC   ; OUT ($BF),A
site 016F0   ; OUT ($BF),A
site 016F4   ; OUT ($BE),A
site 0176C   ; OUT ($BF),A
site 01770   ; OUT ($BF),A
site 01793   ; OUT (C),A
site 01795   ; OUT (C),A
site 01797   ; OUT (C),A
site 01799   ; OUT (C),A
site 0179B   ; OUT (C),A
site 0179D   ; OUT (C),A
site 0179F   ; OUT (C),A
site 017A1   ; OUT (C),A
site 017A3   ; OUT (C),A
site 017A5   ; OUT (C),A
site 017A7   ; OUT (C),A
site 017A9   ; OUT (C),A
site 017AB   ; OUT (C),A
site 017AD   ; OUT (C),A
site 017AF   ; OUT (C),A
site 017B1   ; OUT (C),A
site 017B3   ; OUT (C),A
site 017B5   ; OUT (C),A
site 017B7   ; OUT (C),A
site 017B9   ; OUT (C),A
site 017BB   ; OUT (C),A
site 017BE   ; IN A,($DC)
site 017C6   ; IN A,($DC)
site 017C9   ; IN A,($DD)
site 01802   ; OUTI
site 01804   ; OUTI
site 0181B   ; OUTI
site 0181D   ; OUTI
site 01832   ; OUTI
site 01834   ; OUTI
site 01836   ; OUTI
site 01838   ; OUTI
site 0183A   ; OUTI
site 0183C   ; OUTI
site 0183E   ; OUTI
site 01840   ; OUTI
site 01842   ; OUTI
site 01844   ; OUTI
site 01846   ; OUTI
site 01848   ; OUTI
site 0184A   ; OUTI
site 0184C   ; OUTI
site 0184E   ; OUTI
site 01850   ; OUTI
site 01852   ; OUTI
site 01854   ; OUTI
site 01856   ; OUTI
site 01858   ; OUTI
site 0185A   ; OUTI
site 0185C   ; OUTI
site 0185E   ; OUTI
site 01860   ; OUTI
site 01862   ; OUTI
site 01864   ; OUTI
site 01866   ; OUTI
site 01868   ; OUTI
site 0186A   ; OUTI
site 0186C   ; OUTI
site 0186E   ; OUTI
site 01870   ; OUTI
site 01875   ; OUTI
site 01881   ; OUT ($BE),A
site 01886   ; OUT ($BE),A
site 0188B   ; OUT ($BE),A
site 01890   ; OUT ($BE),A
site 01895   ; OUT ($BE),A
site 0189A   ; OUT ($BE),A
site 0189F   ; OUT ($BE),A
site 018A4   ; OUT ($BE),A
site 018B1   ; OUTI
site 018BC   ; OUTI
site 018C3   ; OUTI
site 018CB   ; OUTI
site 01982   ; OUTI
site 01DB2   ; OUT ($BF),A
site 01DB6   ; OUT ($BF),A
site 01DBA   ; OUT ($BE),A
site 01DC2   ; OUT ($BF),A
site 01DC6   ; OUT ($BF),A
site 01DD2   ; OTIR
site 01DDA   ; OUT ($BF),A
site 01DDD   ; OUT ($BF),A
site 01DE2   ; OTIR
site 01DF4   ; OUT ($BF),A
site 01DF8   ; OUT ($BF),A
site 01E08   ; OTDR
site 01E11   ; OUT (C),L
site 01E1C   ; OUT ($BF),A
site 01E1F   ; OUT ($BF),A
site 01E23   ; OUTI
site 01E25   ; OUTD
site 01E2D   ; OUT ($BE),A
site 0203A   ; OUT ($BE),A
site 02040   ; OUT ($BE),A
site 02064   ; OUT ($BE),A
site 0206A   ; OUT ($BE),A
site 029C0   ; OUT ($BE),A
site 029C4   ; OUT ($BE),A
site 029C9   ; OUT ($BE),A
site 029CD   ; OUT ($BE),A
site 02B54   ; OUT ($BE),A
site 02B5B   ; OUT ($BE),A
site 02B62   ; OUT ($BE),A
site 02B69   ; OUT ($BE),A
site 02B71   ; OUT ($BE),A
site 02B78   ; OUT ($BE),A
site 02B7F   ; OUT ($BE),A
site 02B86   ; OUT ($BE),A
site 03E8D   ; OUT ($BE),A
site 03E95   ; OUT ($BE),A
site 03E9B   ; OUT ($BE),A
site 040F4   ; OUT ($BF),A
site 040F8   ; OUT ($BF),A
site 04169   ; OUT (C),D
site 04172   ; OUT ($BE),A
site 0417A   ; OUT (C),D
site 04182   ; OUT ($BE),A
site 04189   ; OUT ($BE),A
site 04197   ; OUT ($BE),A
site 0419D   ; OUT ($BE),A
site 041A3   ; OUT ($BE),A
site 041D8   ; OUT (C),D
site 041DD   ; OUT ($BE),A
site 041E4   ; OUT (C),D
site 053F2   ; OUT ($BF),A
site 053F5   ; OUT ($BF),A
site 053FE   ; OUTI
site 05462   ; OUT ($BF),A
site 05465   ; OUT ($BF),A
site 05479   ; OUT ($BE),A
site 05480   ; OUT ($BE),A
site 054AE   ; OUT ($BE),A
site 054B5   ; OUT ($BE),A
site 054C1   ; OUT ($BE),A
site 054C9   ; OUT ($BE),A
site 054DA   ; OUT ($BE),A
site 0796C   ; OUT ($BF),A
site 0796F   ; OUT ($BF),A
site 07972   ; OUTI
site 0797A   ; OUTI
site 07992   ; OUT ($BF),A
site 07995   ; OUT ($BF),A
site 07998   ; OUTI
site 079A0   ; OUTI
site 079AE   ; OUT ($BF),A
site 079B1   ; OUT ($BF),A
site 079B4   ; OUTI
site 079BC   ; OUTI
site 079C8   ; OUT ($BF),A
site 079CB   ; OUT ($BF),A
site 079CE   ; OUTI
site 079D9   ; OUT ($BE),A
site 079F3   ; OUT ($BF),A
site 079F6   ; OUT ($BF),A
site 079F9   ; OUTI
site 07A04   ; OUT ($BE),A
site 07A37   ; OUT ($BF),A
site 07A3C   ; OUT ($BF),A
site 07A7E   ; OUTI
site 07A80   ; OUTI
site 07A82   ; OUTI
site 07A84   ; OUT (C),D
site 07A86   ; OUTI
site 07A88   ; OUTI
site 07A8A   ; OUTI
site 07A8C   ; OUT (C),D
site 07A8E   ; OUTI
site 07A90   ; OUTI
site 07A92   ; OUTI
site 07A94   ; OUT (C),D
site 07A96   ; OUTI
site 07A98   ; OUTI
site 07A9A   ; OUTI
site 07A9C   ; OUT (C),D
site 07AA3   ; OUTI
site 07AA9   ; OUTI
site 07AAF   ; OUTI
site 07AB6   ; OUT ($BE),A
site 07C98   ; OUT ($BE),A
site 07C9F   ; OUT ($BE),A
site 07E2D   ; OUT ($BE),A
site 07E33   ; OUT ($BE),A
site 1479E   ; OUT ($F0),A
site 147A7   ; OUT ($F1),A
site 147C9   ; OUT ($7F),A
site 147CD   ; OUT ($F0),A
site 147D3   ; OUT ($F1),A
site 147EF   ; OUT ($7F),A
site 147FF   ; OUT (C),D
site 14805   ; OUT ($F1),A
site 14829   ; OUT ($7F),A
site 1482D   ; OUT ($7F),A
site 1485B   ; OTIR
site 1486E   ; OUT ($F0),A
site 1487C   ; OUT ($F1),A
site 14885   ; OTIR
site 1488F   ; OUT ($F0),A
site 14895   ; OUT ($F1),A
site 148A1   ; OUTI
site 148A7   ; OUTI
site 14904   ; OUT ($7F),A
site 14908   ; OUT ($7F),A
site 1490C   ; OUT ($7F),A
site 1499D   ; OUT ($7F),A
site 149A1   ; OUT ($7F),A
site 149B8   ; OUT ($7F),A
site 149E0   ; OUT ($7F),A
site 149E4   ; OUT ($7F),A
site 149E8   ; OUT ($7F),A
site 149EC   ; OUT ($7F),A
site 149EF   ; OUT ($7F),A
site 14A55   ; OUT ($F0),A
site 14A5C   ; OUT ($F1),A
site 14A64   ; OUT ($F0),A
site 14A6A   ; OUT ($F1),A
site 14B6B   ; OUT ($F0),A
site 14B78   ; OUT (C),L
site 14B84   ; OUT ($F0),A
site 14B9F   ; OUT (C),H
site 14BA7   ; OUT ($F0),A
site 14BB5   ; OUT ($F1),A
site 14BC1   ; OUT ($F0),A
site 14BCA   ; OUT ($F1),A
site 14D81   ; OUT ($F0),A
site 14D8A   ; OUT (C),A
site 14D8F   ; OUT ($F0),A
site 14D95   ; OUTI
site 14DBC   ; OUT ($F0),A
site 14DC4   ; OUT (C),A
site 14DCB   ; OUT ($F0),A
site 14DD3   ; OUT (C),A
site 14E1B   ; OUT ($7F),A
site 14EF9   ; OUT ($7F),A
site 14F27   ; OUT ($7F),A
site 14F32   ; OUT ($7F),A
site 14F39   ; OUT ($7F),A
site 14F45   ; OUT ($7F),A
site 14F4A   ; OUT ($7F),A
site 14F76   ; OUT ($F0),A
site 14F84   ; OUT ($F1),A
site 14F98   ; OUT (C),A
site 14FA3   ; OUT ($F0),A
site 14FA9   ; OUTI
site 14FB4   ; OUT ($F0),A
site 1504B   ; OUTI
site 1504D   ; OUTI
site 1504F   ; OUTI
site 15051   ; OUTI
site 15053   ; OUTI
site 15055   ; OUTI
site 15057   ; OUTI
site 15059   ; OUTI
site 1505B   ; OUTI
site 1505D   ; OUTI
site 1505F   ; OUTI
site 15069   ; OUT (C),D
site 1506F   ; OUT ($F1),A
site 150AE   ; OUT ($7F),A
site 15104   ; OUT ($7F),A
site 15143   ; OUT ($7F),A
site 151A5   ; OUT ($7F),A
site 151C5   ; OUT ($7F),A
site 15211   ; OUT ($7F),A
site 1521B   ; OUT ($7F),A
site 15263   ; OUT ($7F),A
mapst 00008   ; LD ($FFFF),A
mapst 00021   ; LD ($FFFE),A
mapst 00028   ; LD ($FFFE),A
mapst 0002C   ; LD ($FFFF),A
mapst 00078   ; LD ($FFFF),A
mapst 0007C   ; LD ($FFFE),A
maphl 00083   # LD (HL),$00, HL = $FFFD
maphl 00086   # LD (HL),$01, HL = $FFFE
maphl 00089   # LD (HL),$02, HL = $FFFF
mapldk 002D6   # LD HL,$FFFC; LD (HL),$80
maphl 002DC   # LD (HL),$00, HL = $FFFD
maphl 002DF   # LD (HL),$01, HL = $FFFE
maphl 002E2   # LD (HL),$02, HL = $FFFF
mapst 0034A   ; LD ($FFFE),A
mapst 00436   ; LD ($FFFF),A
mapst 00451   ; LD ($FFFF),A
mapst 0084E   ; LD ($FFFF),A
mapst 00855   ; LD ($FFFF),A
mapst 012F2   ; LD ($FFFF),A
mapst 012FD   ; LD ($FFFF),A
mapsthl 0147F   ; LD ($FFFE),HL
mapst 014CE   ; LD ($FFFE),A
mapsthl 014DC   ; LD ($FFFE),HL
mapsthl 01501   ; LD ($FFFE),HL
mapst 0199A   ; LD ($FFFF),A
mapst 019DC   ; LD ($FFFF),A
mapst 01E63   ; LD ($FFFF),A
mapst 02008   ; LD ($FFFF),A
mapst 02016   ; LD ($FFFF),A
# CHECK mapper at 020E1 ($20E1 bank 0): ED B0  LDIR $C240-$1C23F $C240-$1C23F
mapst 0284F   ; LD ($FFFF),A
mapst 042A4   ; LD ($FFFF),A
mapst 077F8   ; LD ($FFFF),A
mapst 07A2A   ; LD ($FFFF),A
mapst 082BC   ; LD ($FFFF),A
mapst 082D6   ; LD ($FFFF),A
mapst 08336   ; LD ($FFFF),A
mapst 08C11   ; LD ($FFFF),A
mapst 08DE7   ; LD ($FFFF),A
mapst 36D01   ; LD ($FFFF),A
mapst 36D7A   ; LD ($FFFF),A
mapst 36E0C   ; LD ($FFFF),A
mapst 36EA6   ; LD ($FFFF),A
mapst 36F45   ; LD ($FFFF),A
mapst 37276   ; LD ($FFFF),A
# $047B LD ($0000),A is a write to ROM, a no-op on the Master System (the sprite list end
# check at $0465 calls it). On the Next it would write the cart's RAM copy.
asm 0047B 3
    nop
endasm
# CHECK indirect_unresolved at 00043 ($0043 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 00074 ($0074 bank 0): CD 80 00  CALL $0080 
# CHECK indirect_unresolved at 0180C ($180C bank 0): CD 30 18  CALL $1830 
# CHECK indirect_unresolved at 02B27 ($2B27 bank 0): CD 4D 2B  CALL $2B4D 
# CHECK indirect_unresolved at 0411C ($411C bank 1): CD 2B 41  CALL $412B 
# CHECK indirect_unresolved at 04125 ($4125 bank 1): CD 2B 41  CALL $412B 
# CHECK indirect_unresolved at 36D51 ($6D51 bank 13): CD 57 6D  CALL $6D57 
# CHECK bank_unresolved at 016A4 ($16A4 bank 0): CD 71 40  CALL $4071 $4071
# CHECK bank_unresolved at 01FF2 ($1FF2 bank 0): CC A6 5D  CALL Z,$5DA6 $5DA6
# CHECK bank_unresolved at 03EB7 ($3EB7 bank 0): C3 8D 42  JP $428D $428D
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00055   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 00059   # LD ($FFFE),A; after POP AF; JP/CALL target from $130C5; 32 bytes of valid code before it
mapst 0005E   # LD ($FFFF),A; after another mapper store, LD ($FFFE),A at $00059; 32 bytes of valid code before it
mapst 1401E   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 1403E   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 143F6   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 377DF   # LD ($FFFF),A; after LD A,(HL); 32 bytes of valid code before it
# CHECK high: site 008B9  OUT ($BF),A  (vdp_control; branch target from $00897 $00896; 32 bytes of valid code before it)
# CHECK high: site 008BC  OUT ($BF),A  (vdp_control; branch target from $1130C; 32 bytes of valid code before it)
# CHECK medium: site 008BF  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 008C6  OUT ($BE),A  (vdp_data; branch target from $005AA $338AB; 32 bytes of valid code before it)
# CHECK high: site 00AA2  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 00AA6  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 00AAA  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 00AAE  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 00AB8  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $00AC6; 32 bytes of valid code before it)
# CHECK medium: site 00ABC  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 00AC0  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 00AC4  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 01716  OUT ($BF),A  (vdp_control; after LD A,($C112); branch target from $392B3; 32 bytes of valid code before it)
# CHECK high: site 0171A  OUT ($BF),A  (vdp_control; after LD A,$88; 32 bytes of valid code before it)
# CHECK medium: site 01726  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 0172A  OUT ($BF),A  (vdp_control; after LD A,$88; 32 bytes of valid code before it)
# CHECK low: site 02B8E  OUT ($BE),A  (vdp_data; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 02B95  OUT ($BE),A  (vdp_data; branch target from $27101; 32 bytes of valid code before it)
# CHECK low: site 02B9C  OUT ($BE),A  (vdp_data; 16 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 02BA3  OUT ($BE),A  (vdp_data; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 02BAB  OUT ($BE),A  (vdp_data; branch target from $02BDE; 32 bytes of valid code before it)
# CHECK high: site 02BB2  OUT ($BE),A  (vdp_data; branch target from $38CCB; 32 bytes of valid code before it)
# CHECK low: site 02BB9  OUT ($BE),A  (vdp_data; 19 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 02BC0  OUT ($BE),A  (vdp_data; 15 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 02BC4  OUT ($BE),A  (vdp_data; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 02BCC  OUT ($BE),A  (vdp_data; 15 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 02BD3  OUT ($BE),A  (vdp_data; 14 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 02BDA  OUT ($BE),A  (vdp_data; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 02F74  OUT (C),B  (port in C; no evidence)
# CHECK low: site 04B37  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK high: site 04BFA  IN A,($DC)  (joypad_a; branch target from $1C819; 32 bytes of valid code before it)
# CHECK low: site 05CE7  IN A,($3E)  (unmapped_read; no evidence)
# CHECK medium: site 10575  IN A,($DC)  (joypad_a; 20 bytes of valid code before it)
# CHECK low: site 106F2  IN A,($7E)  (v_counter; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 10B2F  IN A,($7E)  (v_counter; 32 bytes of valid code before it)
# CHECK medium: site 10C5C  IN A,($F1)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK low: site 115A9  IN L,(C)  (port in C; no evidence)
# CHECK medium: site 11AF6  OUT ($F1),A  (fm_data; 32 bytes of valid code before it)
# CHECK low: site 11DD3  OUTD  (port in C; no valid code after it)
# CHECK medium: site 12842  IN A,($7E)  (v_counter; 32 bytes of valid code before it)
# CHECK low: site 1356A  OUT ($7F),A  (psg; no evidence)
# CHECK medium: site 13726  IN L,(C)  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 14461  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 14466  OUT ($BF),A  (vdp_control; branch target from $1442B; 32 bytes of valid code before it)
# CHECK medium: site 1446D  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 14474  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 14501  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 14505  OUT ($BF),A  (vdp_control; after LD A,$7A; 32 bytes of valid code before it)
# CHECK high: site 14517  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 1451D  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK low: site 197FF  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK medium: site 19B9A  IN A,($DC)  (joypad_a; 32 bytes of valid code before it)
# CHECK low: site 1A6A2  OUT ($C1),A  (no_effect; no evidence)
# CHECK medium: site 1A755  IN E,(C)  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 1A9CB  IN A,($3F)  (unmapped_read; 32 bytes of valid code before it)
# CHECK medium: site 1AED3  OUT ($3E),A  (memory_control; 32 bytes of valid code before it)
# CHECK medium: site 1AEE4  OUT ($3E),A  (memory_control; 32 bytes of valid code before it)
# CHECK medium: site 1B0AF  IN H,(C)  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 1C2AE  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 1D497  OUT (C),B  (port in C; 11 bytes of valid code before it)
# CHECK low: site 1D67C  IN A,($F1)  (joypad_b_misc; no evidence)
# CHECK medium: site 1D8D2  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK low: site 1D9E8  OUT (C),E  (port in C; no evidence)
# CHECK low: site 1DC44  OUT (C),D  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 1E165  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 1E203  OUT (C),A  (port in C; 15 bytes of valid code before it; no valid code after it)
# CHECK medium: site 1E6B2  IN B,(C)  (port in C; 19 bytes of valid code before it)
# CHECK low: site 21D74  IN L,(C)  (port in C; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2547A  OUT ($C0),A  (no_effect; no evidence)
# CHECK medium: site 25538  OUT ($7E),A  (psg; 32 bytes of valid code before it)
# CHECK medium: site 255DC  OUT ($F1),A  (fm_data; 12 bytes of valid code before it)
# CHECK medium: site 25617  OUT ($F1),A  (fm_data; 29 bytes of valid code before it)
# CHECK medium: site 25D46  IN H,(C)  (port in C; 19 bytes of valid code before it)
# CHECK low: site 25DE8  IN A,($F2)  (fm_detect; 26 bytes of valid code before it; no valid code after it)
# CHECK medium: site 269C0  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 274C4  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK low: site 274D6  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 274EC  IN A,($C1)  (joypad_b_misc; 17 bytes of valid code before it)
# CHECK low: site 28C57  OUT ($7F),A  (psg; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 2E918  OUT ($F2),A  (fm_control; 32 bytes of valid code before it)
# CHECK low: site 2EBC6  IN A,($BF)  (vdp_status; no evidence)
# CHECK medium: site 3322F  OUT ($3F),A  (io_control; 32 bytes of valid code before it)
# CHECK low: site 3337A  IN A,($7F)  (h_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 33894  OTDR  (port in C; 18 bytes of valid code before it)
# CHECK high: site 34CD5  OUT ($F1),A  (fm_data; after POP AF; 32 bytes of valid code before it)
# CHECK low: site 369D8  IN A,($BF)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 37146  OUT ($3E),A  (memory_control; no evidence)
# CHECK high: site 377F2  OUT ($7F),A  (psg; after LD A,$81; 32 bytes of valid code before it)
# CHECK medium: site 377F5  OUT ($F2),A  (fm_control; 32 bytes of valid code before it)
# CHECK high: site 37822  OUT ($7F),A  (psg; branch target from $3781B; 32 bytes of valid code before it)
# CHECK medium: site 3782B  IN A,(C)  (port in C; 31 bytes of valid code before it)
# CHECK high: site 3783C  OUT ($7F),A  (psg; after LD A,$9F; branch target from $3759D $37A67; 32 bytes of valid code before it)
# CHECK high: site 37847  OUT ($F2),A  (fm_control; after LD A,($DE00); 32 bytes of valid code before it)
# CHECK medium: site 382DD  OUT ($C0),A  (no_effect; 23 bytes of valid code before it)
# CHECK low: site 38CB9  IN A,($3F)  (unmapped_read; no evidence)
# CHECK medium: site 395A3  OUT ($BD),A  (vdp_control; 13 bytes of valid code before it)
# CHECK low: site 39B8E  OUT ($C0),A  (no_effect; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 39C64  IN A,($7F)  (h_counter; 10 bytes of valid code before it)
# CHECK medium: site 39C67  IN A,($BF)  (vdp_status; 13 bytes of valid code before it)
# CHECK medium: site 3A1B0  IN A,(C)  (port in C; 32 bytes of valid code before it)
# CHECK low: site 3A2C5  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 3A31C  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 3A567  IN A,($7E)  (v_counter; 11 bytes of valid code before it; no valid code after it)
# CHECK medium: site 3AFBA  IN A,($3F)  (unmapped_read; 32 bytes of valid code before it)
# CHECK low: site 3B2F4  IND  (port in C; no evidence)
# CHECK medium: site 3B374  IN H,(C)  (port in C; 24 bytes of valid code before it)
# CHECK medium: site 3B377  IN A,($DD)  (joypad_b_misc; 27 bytes of valid code before it)
# CHECK low: site 3B39D  IN A,($F2)  (fm_detect; no evidence)
# CHECK low: site 3C4B3  IN A,($BE)  (vdp_data; no evidence)
# CHECK medium: site 3CFD7  OUT ($3F),A  (io_control; 32 bytes of valid code before it)
# CHECK medium: site 3CFE9  OUT ($3F),A  (io_control; 32 bytes of valid code before it)
# CHECK low: site 3D0B3  OUT ($7E),A  (psg; no evidence)
# CHECK medium: site 3D0C3  OUT ($7E),A  (psg; 32 bytes of valid code before it)
# CHECK low: site 3E105  OUT (C),H  (port in C; no evidence)
# CHECK low: site 3E55C  OUT ($DD),A  (no_effect; 32 bytes of valid code before it; no valid code after it)

# --- fixes ---
# BMX and flying disc: the line handlers $1555, $1572, $158E, $15AA and $15C8 set H scroll for
# the bands below them from ($C112 + k), or ($C11A + k) when $C107 is not 0. Through the
# runtime (its line interrupt, the status read at $0039, two control writes) the X write
# landed about 2 lines late. The interrupt entry $0038 jumps to a native cave in the zero
# bytes $008E-$00EF (the 32 bytes the code at $7E45 names are a fill value, not a source):
# for a line interrupt with one of those handlers in $C105 it writes the band's X into
# NextReg $2F, $30 and $16 at once, as hscroll_set (fw2) does (X = K - 34 mod 320, Layer 2
# K - 2, K = -H), then makes the status read through the runtime and goes on at $003B. The
# game's own register writes still go through the runtime and set the same values.
# The line interrupt itself comes about a line after the Master System's, so even the cave's
# X is late for the band's first line; in the flying disc the sign's top line then showed at
# the band above's X (the white strip beside the TRAIL sign). For the chain's first handler
# ($154D, no register write) the cave far-calls page 0 entry bdset, which puts each band's X
# and map switch column into the copper list for its first line. The cave pushes AF, HL and
# BC, as the game's own line interrupt path does; the far call's words are within what the
# game's frame interrupt path pushes. Runtime internals: vdp_status $E03A (bit 7: the frame
# flag, for a frame interrupt).
asm 00038 3   ; PUSH AF; IN A,($BF)
    jp $008E
endasm
asm 0008E 98  ; zero bytes
    OPT --zxnext        ; NEXTREG
lc:     push af
        ld a,($E03A)
        rla
        jr c,.st
        push hl
        push bc
        ld hl,($C105)
        ld a,h
        cp $15
        jr nz,.x
        ld a,l
        cp $4D                  ; the flying disc chain's first handler: its bands (bdset)
        jr z,.bd
        ld hl,.tb
        ld bc,$0512
.f:     cp (hl)
        jr z,.k
        inc hl
        inc c
        djnz .f
        jr .x
.k:     ld a,($C107)
        or a
        ld a,c
        jr z,.k2
        add a,8
.k2:    ld l,a
        ld h,$C1
        ld a,(hl)
        neg
        ld b,a
        sub 2
        nextreg $16,a
        ld a,b
        sub 34
        ld b,0
        jr nc,.w
        add a,64
        inc b
.w:     ld c,a
        ld a,b
        nextreg $2F,a
        ld a,c
        nextreg $30,a
.x:     pop bc
        pop hl
.st:    rst $00
        db $0D
        jp $003B
.bd:    rst $00
        db far_io, pg_bdset, ent_bdset
        jr .x
.tb:    db $55,$72,$8E,$AA,$C8
endasm
# Byte-scan I/O that is code the reference logs did not run, patched: the VRAM word writer
# $08B5, the plane-to-VRAM pass of the RLE decoder $0A52 ($0A86-$0AD1, IN A,($BE) steps the
# VRAM address), two line interrupt handlers ($1713, $1725, set through $C105 at $1708),
# the tile pattern writers of the $2B4D family (JP (IX) at $2B4D; the title logo's colour planes:
# all five 4-OUT routines from $2B4F, the scanner found only some), bank 5 name table writers ($8461, $8501) and the
# bank 13 sample player ($77C3, slot 1).
site 008B9   ; OUT ($BF),A
site 008BC   ; OUT ($BF),A
site 008BF   ; OUT ($BE),A
site 008C6   ; OUT ($BE),A
site 00AA2   ; OUT ($BE),A
site 00AA6   ; IN A,($BE)
site 00AAA   ; IN A,($BE)
site 00AAE   ; IN A,($BE)
site 00AB8   ; OUT ($BE),A
site 00ABC   ; IN A,($BE)
site 00AC0   ; IN A,($BE)
site 00AC4   ; IN A,($BE)
site 01716   ; OUT ($BF),A
site 0171A   ; OUT ($BF),A
site 01726   ; OUT ($BF),A
site 0172A   ; OUT ($BF),A
site 02B8E   ; OUT ($BE),A
site 02B95   ; OUT ($BE),A
site 02B9C   ; OUT ($BE),A
site 02BA3   ; OUT ($BE),A
site 02BAB   ; OUT ($BE),A
site 02BB2   ; OUT ($BE),A
site 02BB9   ; OUT ($BE),A
site 02BC0   ; OUT ($BE),A
site 02BC4   ; OUT ($BE),A
site 02BCC   ; OUT ($BE),A
site 02BD3   ; OUT ($BE),A
site 02BDA   ; OUT ($BE),A
site 14461   ; OUT ($BF),A
site 14466   ; OUT ($BF),A
site 1446D   ; OUT ($BE),A
site 14474   ; OUT ($BE),A
site 14501   ; OUT ($BF),A
site 14505   ; OUT ($BF),A
site 14517   ; OUT ($BE),A
site 1451D   ; OUT ($BE),A
site 377F2   ; OUT ($7F),A
site 377F5   ; OUT ($F2),A
site 37822   ; OUT ($7F),A
site 3782B   ; IN A,(C)
site 3783C   ; OUT ($7F),A
site 37847   ; OUT ($F2),A
# BMX: the track renderer at bank 1 $4071 writes 512 name table bytes one OUT at a time from
# the last line interrupt handler (called at $16A4); through the runtime's traps a game step
# took 2 to 3 frames against 1 on the Master System. Page 0 entry bmx does the same work
# natively, writes the rows straight into the VRAM copy and the Next maps (bmx_nt), marks
# only the cells that change, and draws their Layer 2 cells at once (l2go).
asm 04071 5   ; LD A,($C075); DEC A; RET NZ
    rst $00
    db far_io, pg_bmx, ent_bmx
    ret
endasm
# Surfing: the frame handler writes the wave's name table columns (bank 1 $7961, two
# control writes and two data writes a cell) and one tile of the wave animation for each of
# 4 positions (the unrolled chain $7A7C). Page 0 entry scol writes the cells straight into
# the VRAM copy and the Next maps (cput) and draws their Layer 2 cells (l2go); stile writes
# the tile with jt_vwrite.
asm 07961 6   ; LD A,($C0AA); OR A; JR NZ,$79C3
    rst $00
    db far_io, pg_scol, ent_scol
    ret
endasm
asm 07A4B 9   ; PUSH HL; EXX; POP HL; LD B,$18; LD C,$BE; JP (IX)
    rst $00
    db far_io, pg_stile, ent_stile
    jr $7A54
endasm
# All events: the frame handler's palette upload ($176B, 32 CRAM writes every frame). Page 0
# entry pal writes only the entries whose colour changes.
asm 0176B 7   ; XOR A; OUT ($BF),A; LD A,$C0; OUT ($BF),A
    rst $00
    db far_io, pg_pal, ent_pal
    ret
endasm
# BMX: the step's band records ($4055 and the 4 calls of $3F29 at its start, before the step
# sets $C075 for the line 112 renderer) each map bank 6 into slot 2 with LD A,$06; LD
# ($FFFF),A, almost always with bank 6 there already. Through the runtime each store is a
# trap of about 1,800 cycles; the 5 of them delayed $C075 by about 5 lines. On the Master
# System a store of the bank slot 2 holds changes nothing. Caves mk1 and mk2, in the rest of
# the palette upload routine ($1772-$17BD), which page 0 entry pal replaces and nothing else
# reaches, make the store (through the runtime, as mapst does) only when the bank changes:
# ($DFFF) holds the last value stored to $FFFF (the runtime writes the RAM copy with every
# mapper store, as the Master System's RAM does; the game writes $DFFF no other way). Flags
# change; the code after each store sets them again before it reads them.
label mk1 01772
label mk2 01782
asm 01772 33  ; LD C,$BE; LD HL,($C022); ...; OUT (C),A x11
        ld a,($DFFF)
        cp 6
        ld a,6
        jp z,$3F32
        rst $00
        db $13,$FF              ; LD ($FFFF),A through the runtime
        jp $3F32
        ASSERT $ == mk2
        ld a,($DFFF)
        cp 6
        ld a,6
        jp z,$405A
        rst $00
        db $13,$FF
        jp $405A
endasm
asm 03F2D 5   ; LD A,$06; LD ($FFFF),A
        jp mk1
        nop
        nop
endasm
asm 04055 5   ; LD A,$06; LD ($FFFF),A
        jp mk2
        nop
        nop
endasm
# The frame handler's colour queue ($18A9): page 0 entry cq, the same way.
asm 018A9 8   ; LD C,$BE; LD HL,$C120; JP $18B3
    rst $00
    db far_io, pg_cq, ent_cq
    ret
endasm
# The frame handler's VRAM queue ($17F2, tiles of 32 bytes): page 0 entry vq writes each
# entry with jt_vwrite.
asm 017F2 7   ; LD C,$BF; LD H,$C1; LD A,($C109)
    rst $00
    db far_io, pg_vq, ent_vq
    ret
endasm
# The tile builder $0ED8 (BMX and other screens) writes each tile row with four OUT ($BE),A.
# Page 0 entry trow puts the row straight into the VRAM copy.
asm 00EF7 18  ; LD A,B; OUT ($BE),A; LD A,C; PUSH AF; POP AF; OUT ($BE),A; ... LD A,E; ...; OUT ($BE),A
    rst $00
    db far_io, pg_trow, ent_trow
    jp $0F09
endasm
# Surfing: CRAM 0 = $20 at line 71 (the handler $16B4). Page 0 entry c0.
asm 016C1 4   ; LD A,$20; OUT ($BE),A
    rst $00
    db far_io, pg_c0, ent_c0
endasm
# The tile loader at $197D (C tiles of 32 OUTI, half pipe and others). Page 0 entry hpt.
asm 0197D 15  ; LD D,C; LD C,$BE; LD B,$20; OUTI; NOP; JP NZ,$1982; DEC D; JP NZ,$1980
    rst $00
    db far_io, pg_hpt, ent_hpt
    jp $198C
endasm
# The register table write at $0950 (the 11 VDP registers from $C024), at the start of every
# screen set-up. Page 0 entry scr notes the new screen for Layer 2 (l2svc).
asm 00950 5   ; LD HL,$C024; LD B,$0B
    rst $00
    db far_io, pg_scr, ent_scr
    nop
endasm
page 0 bmx scol stile pal cq vq trow c0 hpt scr bdset
    OPT --zxnext        ; NEXTREG, SWAPNIB, ADD HL,A
; bmx: the BMX track renderer at bank 1 $4071, called from the last line interrupt handler
; ($16A4) with the game's interrupts off. When $C075 is 1 it builds the track's row list at
; $DAB0 from the four band records at $DA80, then writes eight name table rows from $3980,
; each cell from the source rows at $C300 or from the lookup pages $CE00-$D5FF. The game
; writes the 512 bytes one OUT at a time; this does the same work natively into a buffer
; and writes the rows with bmx_nt (jt_vwrite when the table is not at $3800). The rows are 6-13, which the beam has passed at the
; handler's line, so on the Master System as here they show from the next picture.
; Registers: the caller saves every register it uses.
bmx:    ld a,($C075)
        dec a
        ret nz
        ld ($C075),a
        ld (bmx_sp),sp
        ld sp,bmx_stk
        push iy
        ld a,($C107)
        xor 1
        ld ($C107),a
        ld b,0
        ld a,($C0AE)
        ld c,a
        ld hl,$DAB0
        ld ix,$DA80
        exx
        ld hl,$DAA8
        exx
.band:  ld d,(ix+0)
        ld a,c
        sub d
        ld e,a
        and 7
        add a,$CE
        ld (hl),a
        inc l
        ld a,e
        rra
        rra
        rra
        neg
        and $1F
        ld e,a
        add a,b
        ld (hl),a
        inc l
        ld a,$20
        sub e
        ld (hl),a
        inc l
        ld a,d
        rra
        rra
        rra
        inc a
        and $1F
        add a,b
        ld e,a
        ld a,d
        and 7
        ld d,a
        ld a,c
        and 7
        sub d
        ld d,$DB
        jr c,.lo
        ld a,(ix+6)
        ld (de),a
        ld a,e
        add a,$20
        ld e,a
        ld a,(ix+8)
        jr .st
.lo:    ld a,(ix+7)
        ld (de),a
        ld a,e
        add a,$20
        ld e,a
        ld a,(ix+9)
.st:    ld (de),a
        call bmx_ptr
        call bmx_ptr
        ld a,b
        add a,$40
        ld b,a
        ld de,10
        add ix,de
        jr nz,.band
        ld (hl),0
        ld iy,bmx_buf
        exx
        ld de,$C300
        ld h,$DB
        exx
        ld c,$BE
        ld hl,$DAB0
.ent:   ld a,(hl)
        or a
        jr z,.flush
        inc l
        ex af,af'
        ld a,(hl)
        inc l
        exx
        ld l,a
        ex af,af'
        ld b,a
        dec e
        inc de
        exx
        ld a,(hl)
        inc l
        push af
        ld e,(hl)
        inc l
        ld d,(hl)
        inc l
        ex de,hl
        call bmx_run
        pop af
        ld e,(hl)
        inc l
        ld d,(hl)
        inc l
        ex de,hl
        call bmx_run
        jr .ent
.flush: push iy
        pop bc
        ld hl,-bmx_buf
        add hl,bc               ; HL = bytes written, 64 a row
        ld a,h
        or l
        jp z,.none
        ld (bmx_len),hl
        add hl,hl
        add hl,hl               ; H = rows
        ld a,h
        ld (bmx_rows),a
        ld hl,(nt_base)         ; the table at $3800 (register 2 is always $FF): cells straight
        ld de,$3800             ; into the VRAM copy, the Next maps and the marks (bmx_nt)
        or a
        sbc hl,de
        jr nz,.vw
        call bmx_nt
        jr .wr
.vw:    ld a,(bmx_rows)         ; any other table: jt_vwrite
        ld c,a
        ld b,64
        ld ix,64
        ld iy,64
        ld hl,bmx_buf
        ld de,$3980
        ld a,1                  ; the source as mapped: the buffer in this page
        call jt_vwrite
.wr:    ld hl,(bmx_len)         ; the VDP as the game's writes leave it
        ld de,bmx_buf-1
        add hl,de
        ld a,(hl)
        ld (vdp_rbuf),a
        ld hl,(bmx_len)
        ld de,$3980
        add hl,de
        res 6,h
        ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld a,(bmx_any)
        or a
        call nz,l2go            ; the Layer 2 cells the writes marked, drawn now
        jr .done
.none:  ld hl,$3980             ; no rows: only the address write
        ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
.done:  pop iy
        ld sp,(bmx_sp)
        ret

; bmx_nt: the rows in bmx_buf to name table rows 6 on (the table at $3800), as nt_put and
; pri_markc (fw.asm) write each cell, a whole row at a time: the row into the VRAM copy; the
; M0 row (tile, then the attribute from mapattr_table) and M0 columns 32-39 = columns 0-7;
; the A8 row = M0 columns 8-31, 0-7, 0-7; in a row that has or gets priority cells, each
; cell's mark for l2go. Runtime internals: SHADOW_PAGE+1 29 (slot 2: VRAM $2000-$3FFF at
; $4000); MAP_PAGE 14 (slot 0: M0 $0000, A8 $0A00, 80 bytes a row; marks $1BC0 + row (the row
; has priority cells), $1BE0 + row (the row has marked cells), $1C00 + cell, bit 0 marked,
; bit 1 Layer 2 holds the cell); mapattr_table $E200; nt_base $E04B.
bmx_nt: push iy
        xor a
        ld (bmx_any),a
        nextreg $50,14
        nextreg $52,29
        ld a,6
        ld (bmx_r),a
        ld hl,bmx_buf
        ld (bmx_src),hl
.row:
        ld a,(bmx_r)            ; the marks, in a row with priority cells
        add a,$C0
        ld l,a
        ld h,$1B
        ld a,(hl)
        or a
        jr nz,.mk
        ld hl,(bmx_src)         ; or one that gets one
        inc hl
        ld b,32
.pq:    bit 4,(hl)
        jr nz,.mk
        inc hl
        inc hl
        djnz .pq
        jp .cpy
.mk:    ld a,(bmx_r)
        ld e,a
        ld d,32
        mul d,e
        ld a,d
        add a,$1C
        ld d,a                  ; DE = the row's marks
        push de
        ld a,(bmx_r)            ; IX = the row in the VRAM copy
        ld e,a
        ld d,64
        mul d,e
        ld a,d
        add a,$58
        ld d,a
        push de
        pop ix
        pop de
        ld hl,(bmx_src)
        inc hl
        ld b,32
        ld c,0                  ; C: bit 0 a priority cell, bit 1 a cell marked
.mc:    dec hl                  ; a cell that keeps its value is not marked
        ld a,(ix+0)
        cp (hl)
        inc hl
        jr nz,.mch
        ld a,(ix+1)
        cp (hl)
        jr z,.mn
.mch:   bit 4,(hl)
        jr z,.np
        ld a,(de)
        or 1
        ld (de),a
        ld a,c
        or 3
        ld c,a
        jr .mn
.np:    ld a,(de)
        bit 1,a
        jr z,.mn
        or 1
        ld (de),a
        set 1,c
.mn:    inc hl
        inc hl
        inc de
        inc ix
        inc ix
        djnz .mc
        ld a,(bmx_r)
        ld h,$1B
        bit 0,c
        jr z,.m1
        add a,$C0
        ld l,a
        ld (hl),1
        ld a,(bmx_r)
.m1:    bit 1,c
        jp z,.cpy
        add a,$E0
        ld l,a
        ld (hl),1
        ld a,1
        ld (bmx_any),a
.cpy:
        ld hl,(bmx_src)         ; the copy
        ld a,(bmx_r)
        ld e,a
        ld d,64
        mul d,e
        ld a,d
        add a,$58               ; $4000 + ($3800 - $2000) + 64 row
        ld d,a
        ld bc,64
        ldir
        ld a,(bmx_r)            ; DE = the M0 row: 80 row
        ld e,a
        ld d,80
        mul d,e
        ld (bmx_m0),de
        ld hl,(bmx_src)
        ld iyl,32
        ld b,$E2                ; mapattr_table
.m0:    ld a,(hl)
        inc hl
        ld (de),a
        inc de
        ld c,(hl)
        inc hl
        ld a,(bc)
        ld (de),a
        inc de
        dec iyl
        jr nz,.m0
        ld hl,(bmx_m0)          ; M0 columns 32-39 = columns 0-7
        push hl
        ld bc,16
        ldir
        pop hl
        push hl
        ld de,$0A00             ; A8 columns 0-23 = M0 columns 8-31
        add hl,de
        ex de,hl
        pop hl
        push hl
        ld bc,16
        add hl,bc
        ld bc,48
        ldir
        pop hl                  ; A8 columns 24-31 and 32-39 = M0 columns 0-7
        push hl
        ld bc,16
        ldir
        pop hl
        ld bc,16
        ldir
.next:  ld hl,(bmx_src)
        ld bc,64
        add hl,bc
        ld (bmx_src),hl
        ld a,(bmx_r)
        inc a
        ld (bmx_r),a
        sub 6
        ld b,a
        ld a,(bmx_rows)
        cp b
        jp nz,.row
        ld a,(cur_mmu+0)
        nextreg $50,a
        ld a,(cur_mmu+2)
        nextreg $52,a
        pop iy
        ret

; the game's $412C: the routine for one row, from the next byte of the shadow HL list
bmx_ptr: exx
        ld a,(hl)
        inc l
        exx
        ld de,$4145
        or a
        jr nz,.a
        ld de,$41AC
.a:     cp $20
        jr nz,.b
        ld de,$418E
.b:     ld (hl),e
        inc l
        ld (hl),d
        inc l
        ret

; the game's JP (HL) at $412B: HL = the row routine's game address, DE = the list
bmx_run: ld (bmx_n),a
        ld a,h
        cp $41
        jp nz,jt_fatal
        ld a,l
        cp $45
        jr z,r4145
        cp $AC
        jr z,r41AC
        cp $8E
        jp nz,jt_fatal
        ; $418E: 32 cells copied from the source
        ex de,hl
        ld d,1
        exx
        push bc
        ld b,$20
        jr .c2
.c1:    ld (iy+0),a
        inc iy
        inc e
.c2:    ld a,(de)
        inc e
        nop
        ld (iy+0),a
        inc iy
        ld a,(de)
        djnz .c1
        inc e
        ld (iy+0),a
        inc iy
        pop bc
        ld a,l
        add a,$20
        ld l,a
        exx
        ret
        ; A = cells before the wrap of the 32-cell row (from the list); the restored A
r4145:  ld a,(bmx_n)
        ex de,hl
        ld d,1
        ld b,a
        cp $20
        jr z,.all
        ld a,$20
        sub b
        ld e,a
        exx
        call c416C
        ld b,e
        exx
        ld a,l
        sub $20
        ld l,a
        call c416C
        exx
        ld a,l
        add a,$20
        ld l,a
        exx
        ret
.all:   exx
        jp c416C
r41AC:  ld a,(bmx_n)
        ex de,hl
        ld d,1
        ld b,a
        cp $20
        jr z,.all
        ld a,$20
        sub b
        ld e,a
        exx
        call c41DB
        ld b,e
        exx
        ld a,l
        sub $20
        ld l,a
        call c41DB
        exx
        ld a,l
        add a,$20
        ld l,a
        jr .end
.all:   exx
        call c41DB
        exx
.end:   ld a,e
        add a,$40
        ld e,a
        exx
        ret

; the game's $416C loop, entered in the shadow set: cells from the source when its first
; byte is not 0, else the lookup (B:C) and the high byte in D of the main set
c4169:  ld (iy+0),d
        inc iy
        exx
c416C:  ld a,(de)
        or a
        jr nz,.src
.look:  ld c,(hl)
        ld a,(bc)
        ld (iy+0),a
        inc iy
        inc e
        inc e
        inc l
        exx
        djnz c4169
        ld (iy+0),d
        inc iy
        ret
.nxt:   exx
        ld a,(de)
        or a
        jr z,.look
.src:   ld (iy+0),a
        inc iy
        inc e
        ld a,(de)
        inc e
        inc l
        exx
        ld (iy+0),a
        inc iy
        djnz .nxt
        ret

; the game's $41DB loop: cells from the lookup only
c41D8:  ld (iy+0),d
        inc iy
        exx
c41DB:  ld c,(hl)
        ld a,(bc)
        ld (iy+0),a
        inc iy
        inc l
        exx
        djnz c41D8
        ld (iy+0),d
        inc iy
        ret

bmx_n:  db 0
bmx_any: db 0
bmx_len: dw 0
bmx_rows: db 0
bmx_r:  db 0
bmx_t:  db 0
bmx_h:  db 0
bmx_at: db 0
bmx_src: dw 0
bmx_m0: dw 0
bmx_sp: dw 0
        ds 64
bmx_stk:
bmx_buf: ds 512

; scol: the surfing wave's column writer, bank 1 $7961 to the end of $7873, called from the
; frame handler ($77EC) with the game's interrupts off. It writes up to three segments of a
; name table column, each cell's address set with two control writes and the two bytes with
; OUTI (or, when $C0AA is not 0, the second byte masked to bit 0). Entered with the
; registers as at $7961: B = the first segment's bytes, DE = its control word, HL = its
; source; the shadow B, HL = the second segment's; A' = the third segment's bytes. Each
; segment goes to VRAM with one jt_vwrite, in the game's order; the registers are left as
; the game's code leaves them.
scol:   ld (sc_sp),sp
        ld sp,sc_stk
        push iy
        call sc_t0              ; is tile 0 blank
        ld iy,sc_buf
        xor a
        ld (sc_n),a
        ld (sc_mk),a
        ld (sc_ln),a
        ld a,($C0AA)
        or a
        jr nz,.v
        ld a,b
        or a
        jr z,.a2
        call sc_l1
        call sc_fl
.a2:    push de
        exx
        pop de
        ld a,b
        exx
        add a,$20
        add a,l
        ld l,a
        jr nc,.a3
        inc h
.a3:    exx
        ld a,b
        or a
        jr z,.seg3
        call sc_l1
        call sc_fl
        jr .seg3
.v:     ld a,b
        or a
        jr z,.v2
        call sc_l2
        call sc_fl
.v2:    push de
        exx
        pop de
        ld a,b
        exx
        add a,$20
        add a,l
        ld l,a
        jr nc,.v3
        inc h
.v3:    exx
        ld a,b
        or a
        jr z,.seg3
        call sc_l2
        call sc_fl
.seg3:  push de
        exx
        pop de
        ex af,af'
        or a
        jr z,.end
        ld b,a
        call sc_l1
        call sc_fl
.end:   ld a,(sc_mk)            ; the Layer 2 cells the columns marked, drawn at once
        or a
        call nz,l2go
        ld a,(sc_ln)
        or a
        jr z,.end2
        nextreg $50,14
        ld b,a
        ld hl,sc_l
.cl:    ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ex de,hl
        res 1,(hl)
        ex de,hl
        djnz .cl
        ld a,(cur_mmu+0)
        nextreg $50,a
.end2:
        pop iy
        ld sp,(sc_sp)
        ret

; one cell more: note the segment's first control word
sc_cs:  push af
        ld a,(sc_n)
        or a
        jr nz,.n
        ld (sc_de),de
.n:     inc a
        ld (sc_n),a
        pop af
        ret

; the loop at $796B: two bytes a cell, B counts down by 2
sc_l1:  call sc_cs
        ld a,(hl)
        ld (iy+0),a
        inc iy
        inc hl
        ld a,e
        add a,$40
        ld e,a
        jr nc,.c
        inc d
.c:     ld a,(hl)
        ld (iy+0),a
        inc iy
        inc hl
        dec b
        dec b
        jp nz,sc_l1
        ret

; the loop at $79C7: the second byte masked to bit 0
sc_l2:  call sc_cs
        ld a,(hl)
        ld (iy+0),a
        inc iy
        inc hl
        dec b
        ld a,e
        add a,$40
        ld e,a
        jr nc,.c
        inc d
.c:     ld a,(hl)
        and 1
        ld (iy+0),a
        inc iy
        inc hl
        djnz sc_l2
        ret

; write the cells collected since the last call: runs of 2 bytes, $40 apart in VRAM
sc_fl:  ld a,(sc_n)
        or a
        ret z
        push bc
        push de
        push hl
        push ix
        ld c,a                  ; C cells
        ld hl,(sc_de)
        ld a,h
        and $3F
        ld h,a                  ; HL = the first cell's VRAM address
        ld de,(nt_base)
        ld a,d
        cp $38
        jr nz,.vw
        ld a,e
        or a
        jr nz,.vw
        ld a,h                  ; the column inside rows 0-27 of the table at $3800
        cp $38
        jr c,.vw
        ld a,c                  ; and its last cell too
        dec a
        rrca
        rrca
        and $3F
        ld e,a
        ld a,l
        rlca
        rlca
        and 3
        add a,e
        ld e,a
        ld a,h
        sub $38
        add a,a
        add a,a
        add a,e
        cp 28
        jr nc,.vw
        ld ix,sc_buf
        nextreg $50,14
        nextreg $52,28
        nextreg $53,29
.c:     push bc
        push hl
        call cput2
        pop hl
        ld de,$40
        add hl,de
        inc ix
        inc ix
        pop bc
        dec c
        jr nz,.c
        ld a,(cur_mmu+0)
        nextreg $50,a
        ld a,(cur_mmu+2)
        nextreg $52,a
        ld a,(cur_mmu+3)
        nextreg $53,a
        ld de,-$40+2            ; the VDP as the last write leaves it
        add hl,de
        ld (vdp_addr),hl
        ld a,(ix-1)
        ld (vdp_rbuf),a
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        jr .x
.vw:    ld b,2                  ; anywhere else: jt_vwrite
        ld ix,2
        ld iy,$40
        ld hl,(sc_de)
        ex de,hl
        ld hl,sc_buf
        ld a,1                  ; the source as mapped: the buffer in this page
        call jt_vwrite
.x:     pop ix
        pop hl
        pop de
        pop bc
        ld iy,sc_buf
        xor a
        ld (sc_n),a
        ret

; cput: one name table cell, IX = its two bytes, HL = its VRAM address in rows 0-27 of the
; table at $3800: cput2 with its slots mapped, then the game's pages back.
cput:   nextreg $50,14
        nextreg $52,28
        nextreg $53,29
        call cput2
        ld a,(cur_mmu+0)
        nextreg $50,a
        ld a,(cur_mmu+2)
        nextreg $52,a
        ld a,(cur_mmu+3)
        nextreg $53,a
        ret

; cput2: the cell as nt_put and pri_markc (fw.asm) write it: the VRAM copy, the M0 entry (and
; for SMS columns 0-7 M0 + 64 and A8 + 48, A8 + 64; else A8 entry = M0 + $0A00 - 16) and the
; cell's mark for l2go, except for a priority cell that shows tile 0 when tile 0 is blank and
; Layer 2 holds nothing of the cell: it puts no pixel in Layer 2. A cell that keeps its value
; changes nothing, unless it has the priority bit and Layer 2 does not hold it as its tile is
; now: it is marked again when its l2_cv differs from its tile's l2_tv (stile counts each
; write of a wave tile in l2_tv; l2go notes the count it drew in l2_cv). Slots mapped:
; SHADOW_PAGE 28, 29 (slots 2, 3: VRAM at $4000); MAP_PAGE 14 (slot 0: M0 $0000, A8 $0A00, 80
; bytes a row; l2_cv $1400 + cell and l2_tv $1800 + tile, unused by the runtime without the
; priority switch; marks $1BC0 + row, $1BE0 + row, $1C00 + cell, bit 0 marked, bit 1 Layer 2
; holds the cell). Runtime internals: mapattr_table $E200. Uses A, BC, DE, HL.
cput2:  push hl
        ld de,$4000
        add hl,de               ; HL = the cell in the copy
        ld a,(ix+0)
        cp (hl)
        jr nz,.new
        inc hl
        ld a,(ix+1)
        cp (hl)
        dec hl
        jr nz,.new
        pop hl                  ; the cell keeps its value
        bit 4,a
        ret z                   ; no priority bit: nothing to do
        call cp_rc
        call cp_mark
        bit 1,(hl)
        jr z,.mk                ; Layer 2 holds nothing of it: as a new value
        push hl
        ld a,h
        sub $08
        ld h,a                  ; HL = its l2_cv
        ld e,(ix+0)
        ld a,(ix+1)
        and 1
        add a,$18
        ld d,a                  ; DE = its tile's l2_tv
        ld a,(de)
        cp (hl)
        pop hl
        ret z                   ; Layer 2 holds the tile as it is
        jr .mk
.new:   ld a,(ix+0)
        ld (hl),a               ; the copy
        inc hl
        ld a,(ix+1)
        ld (hl),a
        pop hl
        call cp_rc
        ld e,b
        ld d,80
        mul d,e
        ld a,c
        add a,a
        add de,a                ; DE = the M0 entry
        ex de,hl
        ld a,(ix+0)
        ld (hl),a
        inc hl
        ld e,(ix+1)
        ld d,$E2                ; mapattr_table
        ld a,(de)
        ld (hl),a
        ld d,a                  ; D = the attribute
        ld e,(ix+0)             ; E = the tile
        dec hl
        ld a,c
        cp 8
        jr nc,.hi
        push bc
        ld bc,64
        add hl,bc
        ld (hl),e
        inc hl
        ld (hl),d
        ld bc,$0A00-16-1
        add hl,bc
        ld (hl),e
        inc hl
        ld (hl),d
        ld bc,16-1
        add hl,bc
        ld (hl),e
        inc hl
        ld (hl),d
        pop bc
        jr .m
.hi:    ld de,$0A00-16
        add hl,de
        ld a,(ix+0)
        ld (hl),a
        inc hl
        ld a,(ix+1)
        ld e,a
        ld d,$E2
        ld a,(de)
        ld (hl),a
.m:     call cp_mark
.mk:    bit 4,(ix+1)
        jr z,.np
        ld a,(ix+0)             ; tile 0, blank, and nothing of the cell in Layer 2: no mark
        or a
        jr nz,.p
        bit 0,(ix+1)
        jr nz,.p
        ld a,(sc_b0)
        or a
        jr z,.p
        bit 1,(hl)
        ret z
        ld a,(sc_ln)            ; Layer 2 holds it: drawn (cleared) once, then bit 1 goes
        cp 32
        jr nc,.p
        push hl
        push de
        ex de,hl
        ld hl,sc_l
        add a,a
        add hl,a
        ld (hl),e
        inc hl
        ld (hl),d
        pop de
        pop hl
        ld a,(sc_ln)
        inc a
        ld (sc_ln),a
.p:     set 0,(hl)
        ld a,b
        add a,$C0
        ld l,a
        ld h,$1B
        ld (hl),1
        jr .rm
.np:    bit 1,(hl)
        ret z
        set 0,(hl)
.rm:    ld a,b
        add a,$E0
        ld l,a
        ld h,$1B
        ld (hl),1
        ld a,1
        ld (sc_mk),a
        ret
; HL = a VRAM address in the table at $3800 -> B = row, C = column
cp_rc:  ld de,-$3800
        add hl,de
        ld a,l
        and $3F
        rrca
        ld c,a
        add hl,hl
        add hl,hl
        ld b,h
        ret
; B = row, C = column -> HL = the cell's mark, $1C00 + 32 row + column
cp_mark: ld l,b
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld a,c
        add hl,a
        ld a,h
        add a,$1C
        ld h,a
        ret

; stile: one tile of the surfing wave's animation, written by the unrolled chain $7A7C
; (JP (IX) at $7A52): 8 rows of 3 bytes from HL and a 0 byte, to the address the game just
; set ($0F20 + BC), and one more count in the tile's l2_tv (cput2). Entered at $7A4B with the main set active; leaves the shadow set active
; as the chain does (HL past the 24 source bytes, B = 0, C = $BE, D = 0) for the EXX at $7A54.
stile:  ld (sc_sp),sp
        ld sp,sc_stk
        push iy
        push ix
        push bc
        push de
        push hl
        ld de,sc_buf
        ld b,8
.row:   ld a,(hl)
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
        djnz .row
        pop hl                  ; the source
        pop de                  ; the main DE, kept
        pop bc
        ld (sc_src),hl
        push de
        push bc
        ld hl,$0F20
        add hl,bc
        ex de,hl                ; DE = the VRAM address
        ld hl,sc_buf
        ld bc,$2001             ; 32 bytes, one run
        ld ix,32
        ld iy,32
        ld a,1                  ; the source as mapped: the buffer in this page
        call jt_vwrite
        ld a,e                  ; the tile's l2_tv ($1800 + tile, MAP_PAGE 14 in slot 0)
        rlca                    ; counts one more write (cput2)
        rlca
        rlca
        and 7
        ld l,a
        ld a,d
        add a,a
        add a,a
        add a,a
        or l
        ld l,a
        ld a,d
        rrca
        rrca
        rrca
        rrca
        rrca
        and 1
        add a,$18
        ld h,a
        nextreg $50,14
        inc (hl)
        ld a,(cur_mmu+0)
        nextreg $50,a
        pop bc
        pop de
        ld hl,(sc_src)          ; the main HL, kept
        pop ix
        pop iy
        exx                     ; the shadow set, as the chain leaves it
        ld hl,(sc_src)
        ld bc,24
        add hl,bc
        ld b,0
        ld c,$BE
        ld d,0
        ld sp,(sc_sp)
        ret

sc_n:   db 0
sc_mk:  db 0
sc_ln:  db 0
sc_l:   ds 64
sc_b0:  db 0
; sc_t0: sc_b0 = 1 when tile 0 is 32 zero bytes in the VRAM copy (SHADOW_PAGE 28 in slot 2)
sc_t0:  push bc
        push hl
        nextreg $52,28
        ld hl,$4000
        ld b,32
        xor a
.z:     or (hl)
        inc hl
        djnz .z
        cp 1
        ld a,0
        adc a,a                 ; 1 when the OR was 0
        ld (sc_b0),a
        ld a,(cur_mmu+2)
        nextreg $52,a
        pop hl
        pop bc
        ret
sc_de:  dw 0
sc_src: dw 0
sc_sp:  dw 0
        ds 64
sc_stk:
sc_buf: ds 512

; From Prince of Persia's page 1 l2go (overlays/princeofpersia.spec), for the Layer 2 this
; page keeps (l2svc).
; l2go: the Layer 2 cells that name table writes have marked, drawn at once, as the runtime's
; pri_frame marked-cells pass (pri_rowcells, pri_cell, pri_tile, pri_put; fw2.asm) draws them
; with the priority switch: a priority cell gets its tile's pixels on its lines on screen, bit 1
; of its mark and its lines' l2_lf flags; any other marked cell that Layer 2 holds (mark bit 1)
; gets zeros where l2_lf says a line may hold pixels. Each mark is cleared. The pixels come from
; the Next tile definitions, or from the VRAM copy (the planar tile) for a tile that waits for
; conversion (its bit in dirty_pages). V scroll is 0 (l2_v, l2_ys): Layer 2 line y is SMS line
; y. Nothing is drawn before l2init, or in 224-line mode (the game never sets it); the marks
; wait. Interrupts must be off. Keeps IX and IY. Runtime internals:
;   MAP_PAGE 14 (slot 0): row "marked" $1BE0 + row, cell marks $1C00 + cell (bit 0 marked, bit 1
;     Layer 2 holds the cell);
;   SHADOW_PAGE 28, 29 (slots 2, 3: VRAM at $4000); TILE_PAGE 10, 11 (slots 4, 5: tile * 32 + $8000);
;   L2_PAGE 102-107 (slot 6): Layer 2, 32 lines of 256 bytes a page;
;   part 1: dirty_pages $E440, nt_base $E04B, m224 $E08F, cur_mmu.
l2go:
    ld a,($E08F)
    or a
    ret nz
    ld a,(l2_ok)
    or a
    ret z
    push ix
    nextreg $50,14
    nextreg $52,28
    nextreg $53,29
    nextreg $54,10
    nextreg $55,11
    ld a,$FF
    ld (l2_pg),a
    ld b,0
l2_r:
    ld a,b
    add a,$E0
    ld l,a
    ld h,$1B
    ld a,(hl)
    or a
    jr z,l2_rn
    ld (hl),0
    push bc
    call l2_row
    pop bc
l2_rn:
    inc b
    ld a,b
    cp 28
    jr nz,l2_r
    pop ix
l2_back:
    ld a,(cur_mmu+0)
    nextreg $50,a
    ld a,(cur_mmu+2)
    nextreg $52,a
    ld a,(cur_mmu+3)
    nextreg $53,a
    ld a,(cur_mmu+4)
    nextreg $54,a
    ld a,(cur_mmu+5)
    nextreg $55,a
    ld a,(cur_mmu+6)
    nextreg $56,a
    ret
; l2_row: B = row: each marked cell (pri_rowcells)
l2_row:
    ld a,b
    ld (l2_rw),a
    ld l,b
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld de,$1C00
    add hl,de
    ld c,0
l2_c:
    bit 0,(hl)
    jr z,l2_cn
    res 0,(hl)
    push hl
    push bc
    ld a,c
    ld (l2_col),a
    call l2_cell
    pop bc
    pop hl
l2_cn:
    inc hl
    inc c
    ld a,c
    cp 32
    jr nz,l2_c
    ret
; l2_cell: cell (l2_rw, l2_col), HL = its mark (pri_cell)
l2_cell:
    push hl
    ld a,(l2_rw)                ; its entry: nt_base + 64 r + 2 c, at $4000 + that
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,(l2_col)
    add a,a
    add hl,a
    ld de,($E04B)
    add hl,de
    ld a,h
    and $3F
    or $40
    ld h,a
    ld a,(hl)
    ld (l2_tl),a
    inc hl
    ld a,(hl)
    ld (l2_th),a
    pop hl
    and $10
    jr nz,l2_p
    bit 1,(hl)
    ret z                       ; Layer 2 holds nothing of it
    res 1,(hl)
    xor a
    ld (l2_on),a
    jr l2_lines
l2_p:
    set 1,(hl)
    push hl                     ; l2_cv ($1400 + cell) = the tile's l2_tv ($1800 + tile)
    ld a,h
    sub $08
    ld h,a
    ld a,(l2_th)
    and 1
    add a,$18
    ld d,a
    ld a,(l2_tl)
    ld e,a
    ld a,(de)
    ld (hl),a
    pop hl
    ld a,(l2_tl)                ; the tile's dirty_pages byte (tile >> 3) and bit (tile & 7)
    rrca
    rrca
    rrca
    and $1F
    ld e,a
    ld a,(l2_th)
    and 1
    rrca
    rrca
    rrca
    or e
    ld e,a
    ld a,(l2_tl)
    and 7
    ld b,a
    ld a,1
    jr z,l2_b0
l2_bs:
    add a,a
    djnz l2_bs
l2_b0:
    ld c,a
    ld hl,$E440                 ; dirty_pages: the tile waits for conversion
    ld a,e
    add hl,a
    ld a,c
    and (hl)
    ld (l2_dty),a
    ld a,(l2_th)
    and 1
    ld h,a
    ld a,(l2_tl)
    ld l,a
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld (l2_t32),hl
    ld a,(l2_th)
    and 8
    add a,a
    ld ixl,a                    ; $10: the sprite palette
    ld a,1
    ld (l2_on),a
; the cell's lines on screen
l2_lines:
    ld a,(l2_rw)
    add a,a
    add a,a
    add a,a
    ld (l2_y0),a                ; map line of the cell's top
    ld hl,l2_v                  ; the fast form: all 8 lines on screen, in one Layer 2 page,
    sub (hl)                    ; no wrap of the 192-line ring
    jr nc,l2_f0
    add a,224
l2_f0:
    cp 192-7
    jr nc,l2_sl
    ld hl,l2_ys
    add a,(hl)
    jr c,l2_f1
    cp 192
    jr c,l2_f2
l2_f1:
    sub 192
l2_f2:
    cp 192-7
    jr nc,l2_sl
    ld e,a
    and $1F
    cp 32-7
    jp c,l2_fast
l2_sl:
    ld d,0
l2_k:
    ld a,(l2_y0)
    add a,d
    ld hl,l2_v
    sub (hl)
    jr nc,l2_y
    add a,224
l2_y:
    cp 192
    jp nc,l2_nx
    ld hl,l2_ys
    add a,(hl)
    jr c,l2_w
    cp 192
    jr c,l2_l
l2_w:
    sub 192
l2_l:
    ld e,a                      ; the Layer 2 line
    ld hl,l2_lf
    add hl,a
    ld a,(l2_on)
    or a
    jr nz,l2_lp
    ld a,(hl)
    or a
    jp z,l2_nx                  ; no pixels on that line
    jr l2_pg0
l2_lp:
    ld (hl),1
l2_pg0:
    ld a,e                      ; slot 6 = its Layer 2 page
    rlca
    rlca
    rlca
    and 7
    add a,102
    ld hl,l2_pg
    cp (hl)
    jr z,l2_pg1
    ld (hl),a
    nextreg $56,a
l2_pg1:
    ld a,e
    and $1F
    or $C0
    ld h,a
    ld a,(l2_col)
    add a,a
    add a,a
    add a,a
    ld l,a                      ; HL = the 8 bytes
    ld a,(l2_on)
    or a
    jp nz,l2_px
    xor a
    rept 8
    ld (hl),a
    inc l
    endr
    jp l2_nx
l2_px:
    push de
    ld a,(l2_th)
    ld b,a
    ld a,d                      ; the tile row: D, or 7 - D with V flip
    bit 2,b
    jr z,l2_nv
    xor 7
l2_nv:
    add a,a
    add a,a
    ex de,hl                    ; DE = the destination
    ld hl,(l2_t32)
    add hl,a
    ld a,(l2_dty)
    or a
    jp nz,l2_pl
    ld a,h                      ; the Next definition: 4 bytes, the left pixel in the high nibble
    add a,$80
    ld h,a
    ld c,ixl
    bit 1,b
    jp nz,l2_nf
    rept 4
    ld a,(hl)
    swapnib
    and $0F
    or c
    ld (de),a
    inc e
    ld a,(hl)
    and $0F
    or c
    ld (de),a
    inc e
    inc hl
    endr
    jp l2_pd
l2_nf:
    inc hl
    inc hl
    inc hl
    rept 4
    ld a,(hl)
    and $0F
    or c
    ld (de),a
    inc e
    ld a,(hl)
    swapnib
    and $0F
    or c
    ld (de),a
    inc e
    dec hl
    endr
    jp l2_pd
l2_pl:
    ld a,h                      ; the planar tile in the VRAM copy: 4 bytes, plane 0 first
    add a,$40
    ld h,a
    push bc
    ld a,(hl)
    inc hl
    ld c,(hl)
    inc hl
    ld b,(hl)
    inc hl
    ld l,(hl)
    ld h,b
    ld b,a                      ; B, C, H, L = planes 0-3
    pop af                      ; A = l2_th (from B)
    bit 1,a
    ex de,hl                    ; HL = the destination, D, E = planes 2, 3
    jp nz,l2_pf
    rept 8
    xor a
    sla e
    rla
    sla d
    rla
    sla c
    rla
    sla b
    rla
    or ixl
    ld (hl),a
    inc l
    endr
    jp l2_pd
l2_pf:
    rept 8
    xor a
    srl e
    rla
    srl d
    rla
    srl c
    rla
    srl b
    rla
    or ixl
    ld (hl),a
    inc l
    endr
l2_pd:
    pop de
l2_nx:
    inc d
    ld a,d
    cp 8
    jp nz,l2_k
    ret
; l2_fast: E = the first Layer 2 line; lines E to E + 7 lie in one page and on screen
l2_fast:
    ld a,e                      ; slot 6 = the page
    rlca
    rlca
    rlca
    and 7
    add a,102
    ld hl,l2_pg
    cp (hl)
    jr z,l2_fa0
    ld (hl),a
    nextreg $56,a
l2_fa0:
    ld hl,l2_lf
    ld a,e
    add hl,a
    ld a,e
    and $1F
    or $C0
    ld d,a
    ld a,(l2_col)
    add a,a
    add a,a
    add a,a
    ld e,a                      ; DE = the cell's first line in Layer 2, HL = its l2_lf flag
    ld a,(l2_on)
    or a
    jr nz,l2_fp
    ld b,8                      ; zeros on the lines that may hold pixels
l2_fz:
    ld a,(hl)
    or a
    jr z,l2_fz1
    xor a
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    ld a,e
    sub 7
    ld e,a
l2_fz1:
    inc hl
    inc d
    djnz l2_fz
    ret
l2_fp:
    ld b,8
l2_fl:
    ld (hl),1
    inc hl
    djnz l2_fl
    ld a,(l2_dty)
    or a
    jr z,l2_fn
    ld a,e                      ; a tile that waits for conversion: line by line from the VRAM copy
    sub e
    ld d,a
    jp l2_k
l2_fn:
    ld a,(l2_th)
    ld b,a
    ld hl,(l2_t32)
    ld a,h
    add a,$80
    ld h,a
    ld c,ixl
    bit 2,b
    jr z,l2_fn0
    ld a,28                     ; V flip: from the last row up
    add hl,a
l2_fn0:
    bit 1,b
    jr nz,l2_fh
    ld a,0                      ; the step after a row: 0, or -8 with V flip
    bit 2,b
    jr z,l2_fn1
    ld a,-8
l2_fn1:
    ld (l2_fa+1),a
    rlca
    sbc a,a
    ld (l2_fa+5),a              ; its high byte
    ld b,8
l2_fr:
    rept 4
    ld a,(hl)
    swapnib
    and $0F
    or c
    ld (de),a
    inc e
    ld a,(hl)
    and $0F
    or c
    ld (de),a
    inc e
    inc hl
    endr
l2_fa:
    ld a,0
    add a,l
    ld l,a
    ld a,0                      ; (the step's high byte)
    adc a,h
    ld h,a
    ld a,e
    sub 8
    ld e,a
    inc d
    djnz l2_fr
    ret
l2_fh:
    inc hl
    inc hl
    inc hl
    ld a,8                      ; the step after a row: 8, or 0 with V flip
    bit 2,b
    jr z,l2_fh1
    xor a
l2_fh1:
    ld (l2_fb+1),a
    ld b,8
l2_fq:
    rept 4
    ld a,(hl)
    and $0F
    or c
    ld (de),a
    inc e
    ld a,(hl)
    swapnib
    and $0F
    or c
    ld (de),a
    inc e
    dec hl
    endr
l2_fb:
    ld a,0
    add a,l
    ld l,a
    ld a,0
    adc a,h
    ld h,a
    ld a,e
    sub 8
    ld e,a
    inc d
    djnz l2_fq
    ret
l2_v:    db 0
l2_ys:   db 0
l2_pg:   db 0
l2_rw:   db 0
l2_col:  db 0
l2_tl:   db 0
l2_th:   db 0
l2_on:   db 0
l2_dty:  db 0
l2_y0:   db 0
l2_t32:  dw 0
l2_lf:   ds 192                 ; per Layer 2 line: 1 when it may hold pixels

; scr: the register table write at $0950 (LD HL,$C024; LD B,$0B, then the 11 writes), at the
; start of every screen set-up. Notes a new screen for l2svc. Returns HL = $C024, B = 11.
scr:    ld a,1
        ld (l2_all),a
        ld hl,$C024
        ld b,$0B
        ret

; l2svc: Layer 2 kept by this page, as the priority switch shows it (l2_vis, l2_mode,
; fw2_switches, cram_x in fw2.asm), from pal once a frame (the frame handler's palette upload,
; interrupts off), on a stack of its own:
; - l2init the first time;
; - after a screen set-up (scr), at the first upload that is not all black (the screen is
;   built and shows): every cell of rows 0-23 that has the priority bit or that Layer 2 holds
;   is marked (l2sw) and drawn (l2go);
; - the Layer 2 palette from cram (l2pal);
; - Layer 2 shown (port $123B = 2) while the display is on (register 1 bit 6) and no new
;   screen waits; the runtime hides it at each register 1 write.
; It also runs bdrest. Keeps DE, IX, IY.
l2svc:  ld (l2_sp),sp
        ld sp,l2_stk
        push de
        push ix
        push iy
        ld a,(l2_ok)
        or a
        call z,l2init
        ld a,(l2_all)
        or a
        jr z,.pal
        ld hl,pal_buf
        ld b,32
        xor a
.o:     or (hl)
        inc hl
        djnz .o
        and $3F
        jr z,.pal               ; all black
        xor a
        ld (l2_all),a
        call l2sw
        call l2go
.pal:   call l2pal
        call bdrest
        ld a,(l2_all)
        or a
        ld a,0
        jr nz,.v
        ld a,($E03C)            ; vdp_regs+1: the display
        and $40
        jr z,.v
        ld a,2
.v:     ld bc,$123B
        out (c),a
        pop iy
        pop ix
        pop de
        ld sp,(l2_sp)
        ret

; l2init: what the runtime's start does for the priority switch (fw4_start, fw2_switches):
; NextReg $14 = L2_TRANS ($24; the Layer 2 palettes' entries 0 and 16 already hold it), the
; layer order L S U (lay15 = 4, which r1_hw puts into NextReg $15 at each register 1 write,
; and into $15 now), Layer 2 pages 102-107 cleared (SP as the pointer, interrupts off), no
; line with pixels, no Layer 2 colour known.
l2init: ld a,1
        ld (l2_ok),a
        nextreg $14,$24
        nextreg $54,25
        ld a,4
        ld ($8000+$07BA),a      ; lay15
        ld a,(cur_mmu+4)
        nextreg $54,a
        ld bc,$243B
        ld a,$15
        out (c),a
        inc b
        in a,(c)
        and %11100011
        or %00000100
        out (c),a
        ld (l2_isp),sp
        ld a,102
.pg:    nextreg $56,a
        ld sp,$E000
        ld hl,0
        ld b,0
.lp:    rept 16
        push hl
        endr
        djnz .lp
        inc a
        cp 108
        jr nz,.pg
        ld sp,(l2_isp)
        ld a,(cur_mmu+6)
        nextreg $56,a
        ld hl,l2_lf
        ld b,192
.z:     ld (hl),0
        inc hl
        djnz .z
        ld hl,l2_pc
        ld b,32
.u:     ld (hl),$FF
        inc hl
        djnz .u
        ret

; l2sw: marks every cell of rows 0-23 that has the priority bit in the VRAM copy, or that
; Layer 2 holds (mark bit 1), with its row's flag. SHADOW_PAGE 28, 29 in slots 2, 3; MAP_PAGE
; 14 in slot 0. Uses A, BC, DE, HL.
l2sw:   nextreg $50,14
        nextreg $52,28
        nextreg $53,29
        ld hl,(nt_base)
        ld a,h
        and $3F
        or $40
        ld h,a
        inc hl                  ; HL = the first cell's high byte in the copy
        ld de,$1C00             ; DE = its mark
        ld c,0                  ; C = the row
.r:     ld b,32
        xor a
        ld (l2_any),a
.c:     bit 4,(hl)
        jr nz,.m
        ld a,(de)
        bit 1,a
        jr z,.n
.m:     ld a,(de)
        or 1
        ld (de),a
        ld a,1
        ld (l2_any),a
.n:     inc hl
        inc hl
        inc de
        djnz .c
        ld a,(l2_any)
        or a
        jr z,.nr
        push hl
        ld a,c
        add a,$E0
        ld l,a
        ld h,$1B
        ld (hl),1
        pop hl
.nr:    inc c
        ld a,c
        cp 24
        jr nz,.r
        ld a,(cur_mmu+0)
        nextreg $50,a
        ld a,(cur_mmu+2)
        nextreg $52,a
        ld a,(cur_mmu+3)
        nextreg $53,a
        ret

; l2pal: the first Layer 2 palette's entries 1-15 and 17-31 = the colours in cram, as cram_x
; writes them, for each entry whose colour changed since the last call (l2_pc). Entries 0
; and 16 stay transparent. Runtime internals: cram $E04D, pal43 $E09F, pal_hi_table $E300,
; pal_lo_table $E340. Uses A, BC, DE, HL.
l2pal:  ld hl,cram+1
        ld de,l2_pc+1
        ld c,1
.lp:    ld a,c
        cp 16
        jr z,.n
        ld a,(de)
        cp (hl)
        jr z,.n
        ld a,(hl)
        ld (de),a
        push hl
        ld l,a
        ld a,(C0_P43)
        or %00010000            ; the first Layer 2 palette
        nextreg $43,a
        ld a,c
        nextreg $40,a
        ld h,$E3                ; pal_hi_table
        ld a,(hl)
        nextreg $44,a
        set 6,l                 ; pal_lo_table
        ld a,(hl)
        nextreg $44,a
        ld a,(C0_P43)
        nextreg $43,a
        pop hl
.n:     inc hl
        inc de
        inc c
        ld a,c
        cp 32
        jr nz,.lp
        ret

; bdset: the flying disc's band splits. The frame handler sets $C105 = $154D from $C103 and
; register 10 = ($C102); the handlers $1555, $1572, $158E, $15AA and $15C8 write register 8
; at lines ($C102) + 24, + 48, + 64, + 80 and + 96, so each band starts on the next line s,
; with K = -($C112 + k), or -($C11A + k) when $C107 is not 0 (the game writes those tables
; in the vertical blank, after the frame handler's palette upload). The line interrupt comes
; too late for line s (see the $0038 cave), so the cave calls this entry from the first
; handler of the chain ($154D, line ($C102)), which writes each band into the copper list,
; as the runtime writes its list (cop_update, cop_wlines; fw3): its X low byte as MOVE $30
; in the free fifth slot of line s - 1 (run after the line's MOVE $6E,M0, so the X changes
; for line s); when the X high byte changes too and line s - 1 has no map switch to make
; (the band above has K up to 64, column 39), MOVE $2F in line s - 1's switch pair, as WAIT
; s - 1,40; and the band's map switch column in the first byte of the WAIT of lines s to
; s + 2, where the runtime's own column change starts only where the game's register 8
; write lands. The first band's band above is the frame's H (vdp_regs+8). bdrest first
; puts back what the last call wrote (bd_n, bd_s, bd_h): NOOP fifth slots, and the runtime's
; switch pairs and columns (rtcol); l2svc runs it once a frame in the vertical blank too, so
; the list is the runtime's again when the splits stop. Only with the normal list with its
; switch pairs (cop_sw not 0, cop_mode 0), V scroll 0 and the 192-line mode. Interrupts are
; off (a line handler); on a stack of its own; keeps every register. Runtime internals:
; FW2_PAGE 25 (cop_sw $27B3, cop_mode $27B5) at $A000 and FW3_PAGE 100 (sg_n $08A6, sg_tab
; $08A7: per hsplit segment its first line, column and a flag) at $8000 for the reads;
; vdp_regs $E03B; m224 $E08F; NR6E_A8 $8A.
bdset:  ld (bd_sp),sp
        ld sp,bd_stk
        push af
        push bc
        push de
        push hl
        push ix
        push iy
        call bdrest
        nextreg $54,100
        nextreg $55,25
        ld a,($A000+$07B3)      ; cop_sw
        or a
        jp z,.x
        ld a,($A000+$07B5)      ; cop_mode
        or a
        jp nz,.x
        ld a,($E08F)            ; m224
        ld hl,$E03B+9           ; V scroll
        or (hl)
        jp nz,.x
        ld a,($C107)
        or a
        ld de,$C112
        jr z,.t
        ld de,$C11A
.t:     ld (bd_tp),de
        ld a,($E03B+8)          ; the frame's H
        neg
        ld (bd_k),a             ; K of the band above
        ld a,($C102)
        add a,25
        ld (bd_cs),a            ; the first band's line
        ld ix,bd_s
        ld iy,bd_dl
        ld b,5
.wb:    push bc
        ld a,(bd_cs)
        ld c,a                  ; C = s
        cp 190
        jp nc,.wn
        ld (ix+0),c
        ld (ix+5),0
        ld hl,(bd_tp)
        ld a,(hl)
        inc hl
        ld (bd_tp),hl
        neg
        ld (bd_kn),a            ; K
        ld a,c                  ; line s - 1: MOVE $30,X low in its fifth slot
        dec a
        ld e,8
        call cpa
        ld a,$30
        call cpw
        ld a,(bd_kn)
        sub 34
        jr nc,.lo
        add a,64
.lo:    call cpw
        ld a,(bd_k)             ; X high byte changes, and line s - 1 has no switch to make
        cp 34
        sbc a,a
        ld d,a
        ld a,(bd_kn)
        cp 34
        sbc a,a
        cp d
        jr z,.nh
        ld d,a
        ld a,(bd_k)
        call kcol
        cp $80+2*39
        jr nz,.nh
        ld a,c
        dec a
        ld e,0
        call cpa
        ld a,$80+2*40           ; WAIT s - 1,40; MOVE $2F,X high
        call cpw
        ld a,c
        dec a
        call cpw
        ld a,$2F
        call cpw
        ld a,d
        and 1
        call cpw
        ld (ix+5),1
.nh:    ld a,(bd_kn)            ; lines s to s + 2: the band's column
        call kcol
        ld d,a
        ld b,3
        ld a,c
.wl:    push af
        ld e,0
        call cpa
        ld a,d
        call cpw
        pop af
        inc a
        djnz .wl
        ld a,(bd_kn)
        ld (bd_k),a
        inc ix
        ld hl,bd_n
        inc (hl)
.wn:    ld a,(bd_cs)
        add a,(iy+0)
        ld (bd_cs),a
        inc iy
        pop bc
        dec b
        jp nz,.wb
.x:     ld a,(cur_mmu+4)
        nextreg $54,a
        ld a,(cur_mmu+5)
        nextreg $55,a
        pop iy
        pop ix
        pop hl
        pop de
        pop bc
        pop af
        ld sp,(bd_sp)
        ret
; bdrest: what bdset wrote the last time, back as the runtime keeps it (see bdset). Uses A,
; BC, DE, HL, IX.
bdrest: ld a,(bd_n)
        or a
        ret z
        nextreg $54,100
        nextreg $55,25
        ld b,a
        ld ix,bd_s
.rb:    push bc
        ld a,(ix+0)             ; s
        dec a
        ld c,a                  ; C = s - 1
        ld e,8
        call cpa                ; its fifth slot: NOOP
        xor a
        call cpw
        xor a
        call cpw
        ld a,(ix+5)
        or a
        jr z,.r2
        ld a,c                  ; its switch pair, as the runtime's
        ld e,0
        call cpa
        ld a,c
        call rtcol
        call cpw
        ld a,c
        call cpw
        ld a,$6E
        call cpw
        ld a,$8A
        call cpw
.r2:    ld b,3                  ; lines s to s + 2: the runtime's columns
.r3:    inc c
        ld a,c
        ld e,0
        call cpa
        ld a,c
        call rtcol
        call cpw
        djnz .r3
        inc ix
        pop bc
        djnz .rb
        xor a
        ld (bd_n),a
        ld a,(cur_mmu+4)
        nextreg $54,a
        ld a,(cur_mmu+5)
        nextreg $55,a
        ret
; A = K -> A = the first byte of WAIT for its map switch column (hscroll_set, fw2)
kcol:   cp 65
        ld e,39
        jr c,.c
        ld e,a
        ld a,35                 ; 291 - 256
        sub e
        rrca
        rrca
        rrca
        and $1F
        ld e,a
.c:     ld a,e
        add a,a
        or $80
        ret
; A = line, E = byte in its entry: the copper write index at 6 + 10 x line + E (NextReg $62
; with the copper's run mode kept, $61). Keeps BC, D.
cpa:    ld h,0
        ld l,a
        add hl,hl
        add hl,hl
        add hl,a
        add hl,hl
        ld a,e
        add a,6
        add hl,a
        ld a,h
        or $C0
        nextreg $62,a
        ld a,l
        nextreg $61,a
        ret
; A to the copper list at the write index, which steps on
cpw:    nextreg $60,a
        ret
; A = line -> A = the first byte of WAIT for the column the runtime keeps for it: cop_sw for
; segment 0, else the column of the hsplit segment that holds it (sg_n, sg_tab). Keeps BC,
; DE, IX.
rtcol:  push bc
        ld c,a
        ld a,($A000+$07B3)      ; cop_sw
        ld b,a
        ld a,($8000+$08A6)      ; sg_n
        dec a
        jr z,.d
        ld hl,$8000+$08A7+3     ; segment 1
.s:     ld e,a
        ld a,c
        cp (hl)
        jr c,.d                 ; before this segment's first line
        inc hl
        ld b,(hl)
        inc hl
        inc hl
        ld a,e
        dec a
        jr nz,.s
.d:     ld a,b
        add a,a
        or $80
        pop bc
        ret
bd_dl:  db 24,16,16,16,0        ; lines from one band to the next
bd_n:   db 0                    ; bands written the frame before
bd_s:   ds 5                    ; their first lines
bd_h:   ds 5                    ; 1: MOVE $2F in the switch pair of the line before
bd_k:   db 0
bd_kn:  db 0
bd_cs:  db 0
bd_tp:  dw 0
bd_sp:  dw 0
        ds 40
bd_stk:

l2_ok:  db 0                    ; l2init done
l2_all: db 0                    ; a screen set-up waits for its first colours
l2_any: db 0
l2_pc:  ds 32                   ; the first Layer 2 palette's colours, $FF: not known
l2_isp: dw 0
l2_sp:  dw 0
        ds 64
l2_stk:

; pal: the frame handler's palette upload at $176B (called at $14B9 and $1515): CRAM 0-31
; from ($C022), or all 32 entries = L when H is 0. On the Master System 32 OUTs; through the
; runtime about 38,000 cycles every frame. Each entry whose colour differs from the runtime's
; copy (cram, $E04D) gets the VDP address and a write through the I/O RST; the VDP is then
; left as the 32 writes leave it (cram_upd, as Fantastic Dizzy's page 0). Then Layer 2's
; service (l2svc). Interrupts are off (the frame handler). Returns as the game's code: C = $BE;
; A, B, HL change.
pal:    push de
        ld hl,($C022)
        ld a,h
        or a
        ld de,pal_buf
        ld b,32
        jr z,.fill
        ld a,h                  ; a source that does not touch $2000-$3FFF or $DF00 up
        cp $1F                  ; is read as it is mapped
        jr c,.ld
        cp $40
        jr c,.cp
        cp $DF
        jr c,.ld
.cp:    call jt_peek
        ld (de),a
        inc hl
        inc de
        djnz .cp
        jr .go
.ld:    ld bc,32
        ldir
        jr .go
.fill:  ld a,l
.f:     ld (de),a
        inc de
        djnz .f
.go:    ld hl,pal_buf
        ld bc,$2000             ; 32 entries from index 0
        call cram_upd
        call l2svc
        ld c,$BE
        pop de
        ret
; HL = the source, C = the first CRAM index, B = the entries. Each entry
; whose colour (low 6 bits) differs from cram gets the VDP address and a
; write through the I/O RST; then the VDP state is as B writes from index C
; leave it: address C + B, code 3, latch clear, read buffer the last byte.
cram_upd:
        ld de,cram
        ld a,e
        add a,c
        ld e,a                  ; cram is inside one 256-byte page
.lp:    ld a,(hl)
        and $3F
        ex de,hl
        cp (hl)
        ex de,hl
        jr z,.same
        ld a,c
        ld (vdp_addr),a
        xor a
        ld (vdp_addr+1),a
        ld (vdp_latch),a
        ld a,3
        ld (vdp_code),a
        ld a,(hl)
        rst $00
        db $04                  ; OUT ($BE),A
.same:  inc hl
        inc de
        inc c
        djnz .lp
        dec hl
        ld a,(hl)
        inc hl
        ld (vdp_rbuf),a
        ld a,c
        ld (vdp_addr),a
        xor a
        ld (vdp_addr+1),a
        ld (vdp_latch),a
        ld a,3
        ld (vdp_code),a
        ret
pal_buf: ds 32

; cq: the frame handler's colour queue at $18A9 (called at $14E8): entries at $C120 of a
; control word (low byte first) and two data bytes, up to a byte with bit 0 set. The game
; writes each through OUTI (about 13,000 cycles an entry through the runtime). An entry for
; CRAM writes only the entries whose colour changes (cram_upd). A name table cell of rows 0-23
; (the HUD's timer and messages, rows 0-1, every frame) goes straight into the VRAM copy, the
; Next maps and its Layer 2 mark (cput; the table is at $3800, register 2 is always $FF), drawn
; with l2go at the end. Any other entry goes through the I/O RST byte by byte. On a stack of
; its own; interrupts are off (the frame handler). Returns as the game's code: HL at the end
; byte, C = $BE.
cq:     ld (cq_sp),sp
        ld sp,cq_stk
        push de
        push ix
        xor a
        ld (sc_b0),a            ; cput: no tile 0 case
        ld (sc_mk),a
        ld hl,$C120
.lp:    bit 0,(hl)
        jr nz,.end
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,d
        and $C0
        cp $C0
        jr nz,.vram
        push hl
        ld a,e
        and $1F
        ld c,a
        ld b,2
        call cram_upd
        pop hl
        inc hl
        inc hl
        jr .lp
.vram:  cp $40
        jr nz,.io               ; not a VRAM write
        ld a,d
        and $3F
        ld d,a
        bit 0,e
        jr nz,.io               ; not a whole cell
        sub $38
        cp 6
        jr nc,.io               ; not rows 0-23 of the table
        ld a,(nt_base+1)
        cp $38
        jr nz,.io
        ld a,(nt_base)
        or a
        jr nz,.io
        push hl
        push de
        push hl
        pop ix                  ; IX = the two bytes
        ex de,hl                ; HL = the cell's VRAM address
        call cput
        pop de
        pop hl
        inc de                  ; the VDP as the two writes leave it
        inc de
        ld (vdp_addr),de
        inc hl
        ld a,(hl)
        ld (vdp_rbuf),a
        inc hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        jr .lp
.io:    ld a,d                  ; through the RST, as the game's writes
        rlca
        rlca
        and 3
        ld (vdp_code),a
        ld a,d
        and $3F
        ld d,a
        ld (vdp_addr),de
        xor a
        ld (vdp_latch),a
        ld a,(hl)
        rst $00
        db $04                  ; OUT ($BE),A
        inc hl
        ld a,(hl)
        rst $00
        db $04                  ; OUT ($BE),A
        inc hl
        jr .lp
.end:   ld a,(sc_mk)
        or a
        call nz,l2go
        pop ix
        pop de
        ld c,$BE
        ld sp,(cq_sp)
        ret
cq_sp:  dw 0
        ds 48
cq_stk:

; vq: the frame handler's VRAM queue, $17F2 (called at $148D and $14C2 with IX = $1832, the
; unrolled run of 32 OUTI, and at $14E5 with IX = $1873, a loop of 32 OUTI). E = the budget.
; The queue at $C100 + ($C109) holds entries of a flag byte, the two control bytes and a data
; pointer: flag bit 0 clear, the data goes as it is (budget 1); bit 0 set and bit 1 clear,
; 32 bytes looked up in the table at $0100 from 32 index bytes ($187A, budget 2);; bits 0
; and 1 set, the end. Each entry goes to VRAM with one jt_vwrite; an entry whose control
; word is not a VRAM write goes through the I/O RST as the game's OUTIs. Returns as the game
; does: A = the budget left, L = the queue position, H = $C1.
vq:     ld (vq_sp),sp
        ld sp,vq_stk
        push ix
        push iy
        ld a,32                 ; both forms write 32 bytes ($1873: LD B,$40; OUTI; DJNZ)
        ld (vq_cnt),a
        ld h,$C1
        ld a,($C109)
        ld l,a
        ld a,e
.lp:    bit 0,(hl)
        jr nz,.k2
        dec a
        jp m,.ret
        inc l
        ld (vq_a),a
        call vq_hdr             ; control word and data pointer; HL = the data
        ld a,(vq_cnt)
        call vq_out
        ld a,(vq_a)
        ex de,hl
        jr .lp
.k2:    bit 1,(hl)
        jr nz,.ret
        sub 2
        jp m,.ret
        inc l
        ld (vq_a),a
        call vq_hdr
        push de
        ld de,vq_buf
        ld b,32
.lk:    call jt_peek            ; the index, as the game sees it
        inc hl
        push hl
        ld l,a
        ld h,$01
        ld a,(hl)               ; the table at $0100, in the game's bank 0
        ld (de),a
        inc de
        pop hl
        djnz .lk
        pop de
        ld hl,vq_buf
        ld a,$80+32             ; 32 bytes from this page
        call vq_out
        ld a,(vq_a)
        ex de,hl
        jr .lp
.ret:   pop iy
        pop ix
        ld sp,(vq_sp)
        ret

; reads the control word into vq_ctl and the data pointer; returns HL = the data pointer,
; DE = the queue position after the entry
vq_hdr: ld e,(hl)
        inc l
        ld d,(hl)
        inc l
        ld (vq_ctl),de
        ld e,(hl)
        inc l
        ld d,(hl)
        inc l
        ex de,hl
        ret

; writes A bytes (bit 7 set: from this page, count in bits 0-6) from HL to the address in
; vq_ctl. Keeps DE.
vq_out: push de
        ld (vq_n),a
        ld a,(vq_ctl+1)
        and $C0
        cp $40
        jr nz,.io
        ld a,(vq_n)
        and $7F
        ld b,a
        ld e,a
        ld d,0
        push de
        pop ix
        push de
        pop iy
        ld de,(vq_ctl)
        ld a,(vq_n)
        and $80                 ; 0: the source as the game sees it
        ld c,1
        call jt_vwrite
        pop de
        ret
.io:    ld a,(vq_n)             ; not a VRAM write: the game's OUTIs through the runtime
        or a
        jp m,.inbuf
        and $7F
        ld b,a
        ld de,vq_buf
.cp:    call jt_peek
        ld (de),a
        inc hl
        inc de
        djnz .cp
.inbuf: ld hl,vq_ctl
        ld bc,$02BF
        rst $00
        db $B3                  ; OTIR: the two control bytes
        ld a,(vq_n)
        and $7F
        ld b,a
        ld c,$BE
        ld hl,vq_buf
        rst $00
        db $B3                  ; OTIR: the data
        pop de
        ret

vq_cnt: db 0
vq_n:   db 0
vq_a:   db 0
vq_ctl: dw 0
vq_sp:  dw 0
        ds 64
vq_stk:
vq_buf: ds 64

; trow: the four OUT ($BE),A of one tile row at $0EF7 in the tile builder $0ED8 (B, C, D, E,
; the row's four planes). A row of tile data goes straight into the VRAM copy, with the
; tile's dirty_pages bit and tiles_dirty set, as vram_put (fw.asm) does for each byte, so the
; once-a-frame work converts it; tw_cnt is left alone, so the early conversion of 512 bytes
; does not run for these rows. Any other target (code not 1, or a VRAM page region_tab
; does not mark as tile data) goes through the I/O RST. The VDP is left as the four writes
; leave it. Runtime internals: SHADOW_PAGE 28-29 (slot 0 while written), region_tab $E400,
; dirty_pages $E440, tiles_dirty $E082. Keeps BC, DE, HL.
trow:   push hl
        ld a,(vdp_code)
        cp 1
        jr nz,.io
        ld hl,(vdp_addr)
        ld a,l
        and $FC
        cp l
        jr nz,.io               ; a row that could cross a 256-byte page
        push hl
        ld l,h
        ld h,$E4                ; region_tab
        ld a,(hl)
        pop hl
        or a
        jr nz,.io
        ld a,h
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        nextreg $50,a
        push hl
        ld a,h
        and $1F
        ld h,a
        ld (hl),b
        inc l
        ld (hl),c
        inc l
        ld (hl),d
        inc l
        ld (hl),e
        pop hl
        ld a,(cur_mmu+0)
        nextreg $50,a
        push hl
        ld a,l                  ; the tile's bit: 1 << (l >> 5)
        rlca
        rlca
        rlca
        and 7
        ld l,a
        ld a,1
        jr z,.b0
.bs:    add a,a
        dec l
        jr nz,.bs
.b0:    pop hl
        push hl
        ld l,h
        ld h,$E4
        set 6,l                 ; dirty_pages $E440 + VRAM page
        or (hl)
        ld (hl),a
        ld ($E082),a            ; tiles_dirty
        pop hl
        inc hl
        inc hl
        inc hl
        inc hl
        res 6,h
        ld (vdp_addr),hl
        ld a,e
        ld (vdp_rbuf),a
        xor a
        ld (vdp_latch),a
        pop hl
        ret
.io:    ld a,b
        rst $00
        db $04                  ; OUT ($BE),A
        ld a,c
        rst $00
        db $04
        ld a,d
        rst $00
        db $04
        ld a,e
        rst $00
        db $04
        pop hl
        ret

; c0: surfing's line handler at $16B4 writes CRAM 0 = $20 at line 71 (the water's backdrop).
; The write goes through the I/O RST as the game's OUT ($BE),A; then, because the runtime
; leaves pixel value 0 of the tiles below that line with the colour from before the write
; (see the tracker), the colour goes straight into the shown Next registers too: entry 0 of
; the first tilemap palette, and the fallback colour (NextReg $4A) when the tilemap's
; transparent value (NextReg $4C) is 0, as value 0 then shows the fallback colour. The runtime
; writes both again from the palette at the next frame's upload. Runtime internals: pal43 $E09F (the
; NextReg $43 display bits), pal_hi_table $E300, pal_lo_table $E340 (SMS colour -> NextReg
; $44 bytes). Interrupts are off (a line handler). Returns as the game's code: A = $20.
C0_P43  equ $E09F                ; pal43
C0_PHI  equ $E300                ; pal_hi_table
C0_PLO  equ $E340                ; pal_lo_table
c0:     ld a,$20
        rst $00
        db $04                  ; OUT ($BE),A: CRAM 0 through the runtime
        push hl
        ld a,(C0_P43)
        or %00110000            ; the first tilemap palette
        nextreg $43,a
        nextreg $40,0
        ld hl,C0_PHI+$20
        ld a,(hl)
        nextreg $44,a
        ld hl,C0_PLO+$20
        ld a,(hl)
        nextreg $44,a
        ld a,(C0_P43)
        nextreg $43,a
        push bc
        ld bc,$243B
        ld a,$4C
        out (c),a
        inc b
        in a,(c)
        pop bc
        or a
        jr nz,.t
        ld a,(C0_PHI+$20)
        nextreg $4A,a
.t:     pop hl
        ld a,$20
        ret

; hpt: the tile loader at $197D (half pipe and other screens; after DI and the address write
; at $1979-$197A): C tiles (0 = 256) of 32 bytes from HL, each through 32 OUTI, about 9,000
; cycles a tile through the runtime. Here the tiles go straight into the VRAM copy with their
; dirty_pages bits and tiles_dirty set, as vram_put (fw.asm) marks them, so the once-a-frame
; work converts them. Any tile that is not wholly tile data (region_tab not 0), or a source
; that touches $2000-$3FFF, goes through jt_vwrite. The VDP is left as the game's writes leave
; it. Returns as the game's loop: HL past the tiles, B = 0, C = $BE, D = 0, Z set.
; Runtime internals: SHADOW_PAGE 28-29 (slots 2-3, or 4-5 when the source is below $8000),
; region_tab $E400, dirty_pages $E440, tiles_dirty $E082.
hpt:    ld (hp_sp),sp
        ld sp,hp_stk
        push ix
        push iy
        ld b,c                  ; B = tiles
.t:     push bc
        ld de,(vdp_addr)
        ld a,(vdp_code)
        cp 1
        jp nz,.vw
        ld a,e
        and $1F
        jp nz,.vw               ; not a whole tile
        push hl
        ld l,d
        ld h,$E4                ; region_tab: the tile's VRAM page holds tile data
        ld a,(hl)
        pop hl
        or a
        jp nz,.vw
        ld a,h                  ; the source must avoid $2000-$3FFF and the window used
        cp $20
        jr c,.lo
        cp $40
        jp c,.vw
.lo:    ld a,h
        cp $80
        ld a,$40                ; VRAM at $4000 (slots 2, 3) for a source at $8000 up
        ld bc,$5253
        jr nc,.m
        ld a,h
        cp $40
        ld a,$40
        jr c,.m
        ld a,$80                ; else VRAM at $8000 (slots 4, 5)
        ld bc,$5455
.m:     ld (hp_win),a
        ld a,b
        ld (.r1+2),a
        ld (.b1+2),a
        ld a,c
        ld (.r2+2),a
        ld (.b2+2),a
.r1:    nextreg $52,28
.r2:    nextreg $53,29
        push hl
        ld a,(hp_win)
        add a,d
        ld d,a                  ; DE = the copy
        ld bc,32
        ldir
        pop bc                  ; the old source
        push hl
        ld hl,32-1
        add hl,bc
        ld a,(hl)
        ld (vdp_rbuf),a         ; the last byte
        ld b,0                  ; (window back below)
        ld a,(hp_win)
        cp $40
        jr nz,.b0
        ld a,(cur_mmu+2)
        jr .b
.b0:    ld a,(cur_mmu+4)
.b:
.b1:    nextreg $52,a
        ld a,(hp_win)
        cp $40
        ld a,(cur_mmu+3)
        jr z,.b2
        ld a,(cur_mmu+5)
.b2:    nextreg $53,a
        ld de,(vdp_addr)        ; dirty_pages $E440 + VRAM page: the tile's bit
        ld a,e
        rlca
        rlca
        rlca
        and 7
        ld b,a
        ld a,1
        jr z,.k
.s:     add a,a
        djnz .s
.k:     ld l,d
        ld h,$E4
        set 6,l
        or (hl)
        ld (hl),a
        ld ($E082),a            ; tiles_dirty
        ld hl,32
        add hl,de
        res 6,h
        ld (vdp_addr),hl
        xor a
        ld (vdp_latch),a
        pop hl
        jr .n
.vw:    ld b,32                 ; through jt_vwrite
        ld c,1
        ld ix,32
        ld iy,32
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld de,32
        add hl,de
.n:     pop bc
        dec b
        jp nz,.t
        pop iy
        pop ix
        ld sp,(hp_sp)
        ld b,0
        ld c,$BE
        ld d,0
        xor a                   ; Z set, as the loop's last JP NZ falls through
        ret
hp_win: db 0
hp_sp:  dw 0
        ds 48
hp_stk:
endpage
