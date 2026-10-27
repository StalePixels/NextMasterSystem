# Ninja Gaiden (Europe, Brazil) (En), CRC32 1B1D8CC2, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log and these
# extra entry points (the scanner does not follow them):
#   the main state table at $0E92 (bank, address triples, called from $0099 through $0007):
#     F:BAC0 3:8000 4:B89B 1AB1 F:BB70 5:BB5F 3:8003 1507 3:8006 4:B89E 3:8009;
#   the jump tables dispatched with LD HL,table then CALL $0006 or RST $28; JP (HL):
#     $0A64 (the frame handler's mailbox $C6E0), $0AE2, $2E2E, $3009, $31B1, $34D3, $4A1C,
#     $4CEA, $4DB7, $53F2, bank 3 $8230, bank 15 $BC71 and $BC7D;
#   calls from banks 0 and 1 into bank 2 at $9246 $910F $922C $9131 $9276 $925B $9F31
#   $9F11 $9F17 $9FE6 $A0E4 $A28A $A2AE $B4DF $B571 $B5B7.
# Bank 0 $0059 (one CRAM write), $0689 (OTIR rectangle, jump vector $0212) and $081D (banked
# tile copy, jump vector $0230) are code that no path or log reached, and are patched.
# Spec gaps (data/scan-verdicts.tsv): $03497 is the operand of JR Z at $3496; banks 4, 8, 12 and
# 13 ($11F2C, $2273A, $338FA, $36A22) are graphics and table bytes.
# Register 0 has line interrupts on and register 10 is always $FF, so no line interrupt fires.
# Play scrolls H with register 0 bit 6 (status bar rows not scrolled).
name Ninja Gaiden
cart 1B1D8CC2
hz 50		; No-Intro regions Europe, Brazil
# Play has priority cells in the status bar (rows 0-1) and the ground and spikes (rows 20-23):
# Ryu in a pit is hidden behind them on the Master System.
priority
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0001A   ; OUT (C),L
site 0001C   ; OUT (C),H
site 002A7   ; OUT ($BF),A
site 002AB   ; OUT ($BF),A
site 002C8   ; OUT ($BF),A
site 002CC   ; OUT ($BF),A
site 002CF   ; IN A,($DC)
site 002EC   ; IN A,($DD)
site 00314   ; IN A,($BF)
site 0031F   ; OUTI
site 00321   ; OUT (C),A
site 00358   ; OUT (C),E
site 0035A   ; OUT (C),D
site 0035D   ; OUTD
site 0035F   ; OUTD
site 00361   ; OUTD
site 00363   ; OUTD
site 00365   ; OUTD
site 00367   ; OUTD
site 00369   ; OUTD
site 0036B   ; OUTD
site 0036D   ; OUTD
site 0036F   ; OUTD
site 00371   ; OUTD
site 00373   ; OUTD
site 00375   ; OUTD
site 00377   ; OUTD
site 00379   ; OUTD
site 0037B   ; OUTD
site 0037D   ; OUTD
site 0037F   ; OUTD
site 00381   ; OUTD
site 00383   ; OUTD
site 00385   ; OUTD
site 00387   ; OUTD
site 00389   ; OUTD
site 0038B   ; OUTD
site 0038D   ; OUTD
site 0038F   ; OUTD
site 00391   ; OUTD
site 00393   ; OUTD
site 00395   ; OUTD
site 00397   ; OUTD
site 00399   ; OUTD
site 0039B   ; OUTD
site 0039D   ; OUTD
site 0039F   ; OUTD
site 003A1   ; OUTD
site 003A3   ; OUTD
site 003A5   ; OUTD
site 003A7   ; OUTD
site 003A9   ; OUTD
site 003AB   ; OUTD
site 003AD   ; OUTD
site 003AF   ; OUTD
site 003B1   ; OUTD
site 003B3   ; OUTD
site 003B5   ; OUTD
site 003B7   ; OUTD
site 003B9   ; OUTD
site 003BB   ; OUTD
site 003BD   ; OUTD
site 003BF   ; OUTD
site 003C1   ; OUTD
site 003C3   ; OUTD
site 003C5   ; OUTD
site 003C7   ; OUTD
site 003C9   ; OUTD
site 003CB   ; OUTD
site 003CD   ; OUTD
site 003CF   ; OUTD
site 003D1   ; OUTD
site 003D3   ; OUTD
site 003D5   ; OUTD
site 003D7   ; OUTD
site 003D9   ; OUTD
site 003DB   ; OUTD
site 003E4   ; OUT (C),E
site 003E6   ; OUT (C),D
site 003E9   ; OUTI
site 003EB   ; OUTD
site 003EF   ; OUTI
site 003F1   ; OUTD
site 003F5   ; OUTI
site 003F7   ; OUTD
site 003FB   ; OUTI
site 003FD   ; OUTD
site 00401   ; OUTI
site 00403   ; OUTD
site 00407   ; OUTI
site 00409   ; OUTD
site 0040D   ; OUTI
site 0040F   ; OUTD
site 00413   ; OUTI
site 00415   ; OUTD
site 00419   ; OUTI
site 0041B   ; OUTD
site 0041F   ; OUTI
site 00421   ; OUTD
site 00425   ; OUTI
site 00427   ; OUTD
site 0042B   ; OUTI
site 0042D   ; OUTD
site 00431   ; OUTI
site 00433   ; OUTD
site 00437   ; OUTI
site 00439   ; OUTD
site 0043D   ; OUTI
site 0043F   ; OUTD
site 00443   ; OUTI
site 00445   ; OUTD
site 00449   ; OUTI
site 0044B   ; OUTD
site 0044F   ; OUTI
site 00451   ; OUTD
site 00455   ; OUTI
site 00457   ; OUTD
site 0045B   ; OUTI
site 0045D   ; OUTD
site 00461   ; OUTI
site 00463   ; OUTD
site 00467   ; OUTI
site 00469   ; OUTD
site 0046D   ; OUTI
site 0046F   ; OUTD
site 00473   ; OUTI
site 00475   ; OUTD
site 00479   ; OUTI
site 0047B   ; OUTD
site 0047F   ; OUTI
site 00481   ; OUTD
site 00485   ; OUTI
site 00487   ; OUTD
site 0048B   ; OUTI
site 0048D   ; OUTD
site 00491   ; OUTI
site 00493   ; OUTD
site 00497   ; OUTI
site 00499   ; OUTD
site 0049D   ; OUTI
site 0049F   ; OUTD
site 004A3   ; OUTI
site 004A5   ; OUTD
site 004A9   ; OUTI
site 004AB   ; OUTD
site 004AF   ; OUTI
site 004B1   ; OUTD
site 004B5   ; OUTI
site 004B7   ; OUTD
site 004BB   ; OUTI
site 004BD   ; OUTD
site 004C1   ; OUTI
site 004C3   ; OUTD
site 004C7   ; OUTI
site 004C9   ; OUTD
site 004CD   ; OUTI
site 004CF   ; OUTD
site 004D3   ; OUTI
site 004D5   ; OUTD
site 004D9   ; OUTI
site 004DB   ; OUTD
site 004DF   ; OUTI
site 004E1   ; OUTD
site 004E5   ; OUTI
site 004E7   ; OUTD
site 004EB   ; OUTI
site 004ED   ; OUTD
site 004F1   ; OUTI
site 004F3   ; OUTD
site 004F7   ; OUTI
site 004F9   ; OUTD
site 004FD   ; OUTI
site 004FF   ; OUTD
site 00503   ; OUTI
site 00505   ; OUTD
site 00509   ; OUTI
site 0050B   ; OUTD
site 0050F   ; OUTI
site 00511   ; OUTD
site 00515   ; OUTI
site 00517   ; OUTD
site 0051B   ; OUTI
site 0051D   ; OUTD
site 00521   ; OUTI
site 00523   ; OUTD
site 00527   ; OUTI
site 00529   ; OUTD
site 0052D   ; OUTI
site 0052F   ; OUTD
site 00533   ; OUTI
site 00535   ; OUTD
site 00539   ; OUTI
site 0053B   ; OUTD
site 0053F   ; OUTI
site 00541   ; OUTD
site 00545   ; OUTI
site 00547   ; OUTD
site 0054B   ; OUTI
site 0054D   ; OUTD
site 00551   ; OUTI
site 00553   ; OUTD
site 00557   ; OUTI
site 00559   ; OUTD
site 0055D   ; OUTI
site 0055F   ; OUTD
site 00563   ; OUTI
site 00565   ; OUTD
site 00588   ; OUTI
site 0058A   ; OUTI
site 0058C   ; OUTI
site 0058E   ; OUTI
site 00590   ; OUTI
site 00592   ; OUTI
site 00594   ; OUTI
site 00596   ; OUTI
site 00598   ; OUTI
site 0059A   ; OUTI
site 0059C   ; OUTI
site 0059E   ; OUTI
site 005A0   ; OUTI
site 005A2   ; OUTI
site 005A4   ; OUTI
site 005A6   ; OUTI
site 005A8   ; OUTI
site 005AA   ; OUTI
site 005AC   ; OUTI
site 005AE   ; OUTI
site 005B0   ; OUTI
site 005B2   ; OUTI
site 005B4   ; OUTI
site 005B6   ; OUTI
site 005B8   ; OUTI
site 005BA   ; OUTI
site 005BC   ; OUTI
site 005BE   ; OUTI
site 005C0   ; OUTI
site 005C2   ; OUTI
site 005C4   ; OUTI
site 005C6   ; OUTI
site 005C8   ; OUTI
site 005CA   ; OUTI
site 005CC   ; OUTI
site 005CE   ; OUTI
site 005D0   ; OUTI
site 005D2   ; OUTI
site 005D4   ; OUTI
site 005D6   ; OUTI
site 005D8   ; OUTI
site 005DA   ; OUTI
site 005DC   ; OUTI
site 005DE   ; OUTI
site 005E0   ; OUTI
site 005E2   ; OUTI
site 005E4   ; OUTI
site 005E6   ; OUTI
site 005E8   ; OUTI
site 005EA   ; OUTI
site 005EC   ; OUTI
site 005EE   ; OUTI
site 005F0   ; OUTI
site 005F2   ; OUTI
site 005F4   ; OUTI
site 005F6   ; OUTI
site 005F8   ; OUTI
site 005FA   ; OUTI
site 005FC   ; OUTI
site 005FE   ; OUTI
site 00600   ; OUTI
site 00602   ; OUTI
site 00604   ; OUTI
site 00606   ; OUTI
site 00608   ; OUTI
site 0060A   ; OUTI
site 0060C   ; OUTI
site 0060E   ; OUTI
site 00610   ; OUTI
site 00612   ; OUTI
site 00614   ; OUTI
site 00616   ; OUTI
site 00618   ; OUTI
site 0061A   ; OUTI
site 0061C   ; OUTI
site 0061E   ; OUTI
site 00620   ; OUTI
site 00622   ; OUTI
site 00624   ; OUTI
site 00626   ; OUTI
site 00628   ; OUTI
site 0062A   ; OUTI
site 0062C   ; OUTI
site 0062E   ; OUTI
site 00630   ; OUTI
site 00632   ; OUTI
site 00634   ; OUTI
site 00636   ; OUTI
site 00638   ; OUTI
site 0063A   ; OUTI
site 0063C   ; OUTI
site 0063E   ; OUTI
site 00640   ; OUTI
site 00642   ; OUTI
site 00644   ; OUTI
site 00646   ; OUTI
site 00648   ; OUTI
site 0064A   ; OUTI
site 0064C   ; OUTI
site 0064E   ; OUTI
site 00650   ; OUTI
site 00652   ; OUTI
site 00654   ; OUTI
site 00656   ; OUTI
site 00658   ; OUTI
site 0065A   ; OUTI
site 0065C   ; OUTI
site 0065E   ; OUTI
site 00660   ; OUTI
site 00662   ; OUTI
site 00664   ; OUTI
site 00666   ; OUTI
site 00668   ; OUTI
site 0066A   ; OUTI
site 0066C   ; OUTI
site 0066E   ; OUTI
site 00670   ; OUTI
site 00672   ; OUTI
site 00674   ; OUTI
site 00676   ; OUTI
site 00678   ; OUTI
site 0067A   ; OUTI
site 0067C   ; OUTI
site 0067E   ; OUTI
site 00680   ; OUTI
site 00682   ; OUTI
site 00684   ; OUTI
site 00686   ; OUTI
site 006A1   ; OUT ($BE),A
site 006A7   ; OUT ($BE),A
site 006BB   ; OUT ($BE),A
site 006D2   ; OUTI
site 006D7   ; OUT ($BE),A
site 006E9   ; OUT (C),E
site 006EB   ; OUT (C),D
site 006FE   ; OUT (C),E
site 00704   ; OUT (C),D
site 00742   ; OUT ($BE),A
site 00747   ; OUT ($BE),A
site 0074C   ; OUT ($BE),A
site 00751   ; OUT ($BE),A
site 00756   ; OUT ($BE),A
site 0075B   ; OUT ($BE),A
site 00760   ; OUT ($BE),A
site 00765   ; OUT ($BE),A
site 0076A   ; OUT ($BE),A
site 0076F   ; OUT ($BE),A
site 00774   ; OUT ($BE),A
site 00779   ; OUT ($BE),A
site 0077E   ; OUT ($BE),A
site 00783   ; OUT ($BE),A
site 00788   ; OUT ($BE),A
site 0078D   ; OUT ($BE),A
site 00792   ; OUT ($BE),A
site 00797   ; OUT ($BE),A
site 0079C   ; OUT ($BE),A
site 007A1   ; OUT ($BE),A
site 007A6   ; OUT ($BE),A
site 007AB   ; OUT ($BE),A
site 007B0   ; OUT ($BE),A
site 007B5   ; OUT ($BE),A
site 007BA   ; OUT ($BE),A
site 007BF   ; OUT ($BE),A
site 007C4   ; OUT ($BE),A
site 007C9   ; OUT ($BE),A
site 007CE   ; OUT ($BE),A
site 007D3   ; OUT ($BE),A
site 007D8   ; OUT ($BE),A
site 007DD   ; OUT ($BE),A
site 00963   ; OUT (C),E
site 00965   ; OUT (C),D
site 009AF   ; OUT ($BE),A
site 009F8   ; OUT ($BE),A
site 00A19   ; OUT ($BE),A
site 00A3B   ; IN A,($BF)
site 00A40   ; IN A,($DD)
site 00A82   ; OUT ($BF),A
site 00A86   ; OUT ($BF),A
site 00ABD   ; OUT (C),L
site 00ABF   ; OUT (C),H
site 00ACA   ; OUTI
site 00ACC   ; OUTI
site 00ADB   ; OUT ($BF),A
site 00ADF   ; OUT ($BF),A
site 00AF5   ; OUT ($BF),A
site 00AF9   ; OUT ($BF),A
site 00B28   ; OUT ($BF),A
site 00B2C   ; OUT ($BF),A
site 014F5   ; OUT ($BE),A
site 014FE   ; OUT ($BE),A
site 0184A   ; OUT (C),A
site 01850   ; OUT (C),A
site 01882   ; OUT ($BF),A
site 01885   ; OUT ($BF),A
site 0188A   ; OUT ($BE),A
site 018CF   ; OUT (C),A
site 0191A   ; OUT ($BF),A
site 0191D   ; OUT ($BF),A
site 01922   ; OUT ($BE),A
site 01AE3   ; IN A,($DC)
site 038C2   ; OUT ($BF),A
site 038C5   ; OUT ($BF),A
site 038CB   ; IN A,($BE)
site 038D0   ; OUT ($BF),A
site 038D3   ; OUT ($BF),A
site 038D9   ; IN A,($BE)
site 038DE   ; OUT ($BF),A
site 038E1   ; OUT ($BF),A
site 038E7   ; IN A,($BE)
site 038EC   ; OUT ($BF),A
site 038EF   ; OUT ($BF),A
site 038F5   ; IN A,($BE)
site 038FA   ; OUT ($BF),A
site 038FD   ; OUT ($BF),A
site 03903   ; IN A,($BE)
site 053A6   ; IN L,(C)
site 09F20   ; OUT (C),L
site 09F25   ; OUT ($BF),A
site 09F2C   ; IN C,(C)
site 0C177   ; OUT (C),A
site 0C17D   ; OUT (C),A
site 0C1CC   ; IN A,(C)
site 0C1D5   ; IN A,(C)
site 1394C   ; OUT (C),B
site 13953   ; OUT (C),A
site 13999   ; OUT (C),A
site 139A0   ; OUT (C),A
site 13BB4   ; OUT ($BF),A
site 13BB9   ; OUT ($BF),A
site 13BC1   ; OUT ($BF),A
site 13BC5   ; OUT ($BF),A
site 17C04   ; OUT (C),A
site 17C0A   ; OUT (C),A
site 17C52   ; OUT (C),A
site 17C58   ; OUT (C),A
site 1C1E2   ; OUT ($7F),A
site 1C308   ; OUT ($7F),A
site 1C49A   ; OTIR
site 1C5B2   ; OUT ($7F),A
site 1C5BC   ; OUT ($7F),A
site 1C5D9   ; OUT ($7F),A
site 1C6DD   ; OUT ($7F),A
site 1C7BA   ; OUT ($7F),A
site 1C85C   ; OUT ($7F),A
site 1C865   ; OUT ($7F),A
site 1C875   ; OUT ($7F),A
site 1C8F1   ; OUT ($7F),A
site 3FADE   ; OUT ($3F),A
site 3FAE0   ; IN A,($DD)
site 3FAEA   ; OUT ($3F),A
site 3FAEC   ; IN A,($DD)
site 3FB3C   ; OUT ($3E),A
site 3FB3F   ; OUT ($F2),A
site 3FB47   ; OUT ($3E),A
site 3FB4B   ; OUT ($3F),A
site 3FB51   ; IN A,($BF)
site 3FB53   ; IN A,($BF)
site 3FB5F   ; IN A,($BF)
site 3FC68   ; OUT (C),A
site 3FC6E   ; OUT (C),A
site 3FD06   ; OUT (C),D
site 3FD0D   ; OUT (C),A
mapldk 00074   # LD HL,$FFFC; LD (HL),$00
maphl 0007A   # LD (HL),$00, HL = $FFFD
maphl 0007D   # LD (HL),$01, HL = $FFFE
maphl 00080   # LD (HL),$02, HL = $FFFF
mapst 00092   ; LD ($FFFF),A
mapst 0028F   ; LD ($FFFF),A
mapst 00296   ; LD ($FFFF),A
mapst 0072A   ; LD ($FFFF),A
mapst 007E4   ; LD ($FFFF),A
mapst 007F7   ; LD ($FFFF),A
mapst 00940   ; LD ($FFFF),A
mapst 00950   ; LD ($FFFF),A
mapst 00A59   ; LD ($FFFF),A
mapst 00A60   ; LD ($FFFF),A
mapst 00A8B   ; LD ($FFFF),A
mapst 00AF1   ; LD ($FFFF),A
mapst 00B20   ; LD ($FFFF),A
mapst 012ED   ; LD ($FFFF),A
mapst 01300   ; LD ($FFFF),A
mapst 01344   ; LD ($FFFF),A
mapst 013A4   ; LD ($FFFF),A
mapst 013C6   ; LD ($FFFF),A
mapst 01426   ; LD ($FFFF),A
mapst 01477   ; LD ($FFFF),A
mapst 01482   ; LD ($FFFF),A
mapst 01495   ; LD ($FFFF),A
mapst 014DC   ; LD ($FFFF),A
mapst 01866   ; LD ($FFFF),A
mapst 0189D   ; LD ($FFFF),A
mapst 018C5   ; LD ($FFFF),A
mapst 018DA   ; LD ($FFFF),A
mapst 019A3   ; LD ($FFFF),A
mapst 019ED   ; LD ($FFFF),A
mapst 019F2   ; LD ($FFFF),A
mapst 02DC5   ; LD ($FFFF),A
mapst 0083C   # LD ($FFFF),A; after POP AF; JP/CALL target from $320FB; 32 bytes of valid code before it
site 0005C   ; OUT ($BF),A  ($0059, CRAM entry 16)
site 00060   ; OUT ($BF),A
site 00063   ; OUT ($BE),A
site 0068F   ; OTIR  ($0689, jump vector $0212)
mapst 00822   ; LD ($FFFF),A  ($081D, jump vector $0230)
site 0082D   ; OUT (C),A
# The play screen blit at $14E2 (called at level start and after each death) writes the
# name table's rows 2-23 from the cell list at $C400 (tile from the list, high byte $01, or
# $11 with the priority bit when the tile is at least ($C6C3)). Through the runtime each of
# its 1,408 writes marks its cell, and the priority switch then draws every priority cell
# of the play area again in Layer 2: about 1.4M cycles in one vertical blank, and the play
# screen came back about 2 frames later than on the Master System after a death. Page 0
# `ntblit` writes only the cells whose value changes, straight into the VRAM copy, the Next
# tilemaps and the priority marks (the runtime internals are named at the page code), and
# leaves the VDP state as the game's writes leave it. VRAM ends the same as with the game's
# writes.
# The rectangle routine at $06B6 rewrites the status bar's two rows (64 priority cells) with
# the same cells at every restart ($4FE2), and the priority switch then drew all of them
# again in Layer 2 (about 650,000 cycles in one vertical blank). Page 0 `rect` replaces it
# in the same way as `ntblit`: only the cells that change are written.
asm 006B6 5   ; PUSH BC; RST $18; EX DE,HL; OUTI -> far call to page 0 rect
    rst $00
    db far_io, pg_rect, ent_rect
    ret
endasm
# The VRAM clear at $032D (every screen set-up, $0311, display off) writes 16,128 bytes
# of zero one trap run of 256 at a time: about 4.2M cycles, 7.4 frames, against about
# 5.4 frames on a PAL Master System. Page 0 `vclr` writes each 256 bytes with one
# jt_vwrite from a buffer of the fill value, at the address the game set (vdp_addr), and
# lets the game's interrupts in between, as the game's loop does.
# Screen set-ups unpack their tiles with the decompressor at $093B (LZ with a 2K ring at $D000,
# one OUT ($BE),A a byte, interrupts off). The runtime marks each tile and converted all of
# them (about 448, 2.27M cycles) in one piece at the next vertical blank, 4 frames over. Page
# 0 converts them itself, a VRAM page at a time (`tstep`, as the runtime's tile_flush and
# conv_page in fw3 do), in time the Master System spends: while the decompressor is ahead of
# its time, and in the waits of the paced routines. The ring clear at $0954, called before and
# after each chunk, becomes page 0 `tconv`: the same clear, and its time.
asm 00954 13  ; the ring clear (EX AF,AF'; EXX; XOR A; ...; RET) -> far call to page 0 tconv
    rst $00
    db far_io, pg_tconv, ent_tconv
    ret
endasm
# The tile loaders $0715 and $0731 (jump vectors $0224, $0227) copy whole tiles from cart
# ROM; their list loops call them at $0805 and $0816. Page 0 `ld15` and `ld31` do their work,
# and their tiles are converted in the same way (`tstep`), so no vertical blank has to.
asm 00805 4   ; CALL $0715; EX DE,HL -> far call to page 0 ld15
    rst $00
    db far_io, pg_ld15, ent_ld15
endasm
asm 00816 4   ; CALL $0731; EX DE,HL -> far call to page 0 ld31
    rst $00
    db far_io, pg_ld31, ent_ld31
endasm
asm 0032D 8   ; OUT ($BE),A; DJNZ; DEC C; JP NZ -> far call to page 0 vclr
    rst $00
    db far_io, pg_vclr, ent_vclr
    nop
    nop
    nop
    nop
endasm
# The display-on routine at $029A first does the work that waits (tile conversion, Layer 2
# cells) in the time the Master System spends in its frame wait (page 0 `don`), and the rest
# after the wait (page 0 `don2` at $02A2, before the display-on write).
asm 0029A 5   ; IN A,($BF); EI; LD A,1 -> far call to page 0 don
    rst $00
    db far_io, pg_don, ent_don
    nop
endasm
asm 002A2 5   ; LD A,($DFE1); OR $40 -> far call to page 0 don2
    rst $00
    db far_io, pg_don2, ent_don2
    nop
endasm
# The fill at $0008 (RST $08, the game's memory fill) is page 0 `fill8`: the same fill, then
# its time on a Master System (the level set-up clears $C100-$DFAF, 2.8 NTSC frames).
asm 00008 7   ; DEC BC; LD (HL),A; LD D,H; LD E,L; INC DE; LDIR -> far call to fill8, RET
    rst $00
    db far_io, pg_fill8, ent_fill8
    ret
    nop
    nop
endasm
# The decompressor's loop at $0973 (the token handler $0982 with it) is page 0 `lz`: the same
# ring and VRAM writes, with the time of each path on a Master System (see the page).
asm 00973 5   ; LD BC,($D802); OR A -> far call to page 0 lz, then RET
    rst $00
    db far_io, pg_lz, ent_lz
    ret
endasm
# The cell list builder at $148C (before each blit) runs about 8 times faster on the Next
# than on a Master System; page 0 `p148c` (cave at $14A2) waits for its time there.
asm 014A2 7   ; LD IY,$C400; LD BC,$100B -> far call to page 0 p148c
    rst $00
    db far_io, pg_p148c, ent_p148c
    nop
    nop
    nop
endasm
asm 014E2 8   ; LD HL,$7880; DI; RST $18; LD HL,$02C0 -> far call to page 0 ntblit
    rst $00
    db far_io, pg_ntblit, ent_ntblit
    ei
    ret
endasm
# The status bar's digits ($507E, $506F) and its bar ($516B) write one cell at a time through
# the traps, about 2,000 cycles a write with the priority marks; page 0 `dig7E`, `dig6F` and
# `bar76` write each run with one jt_vwrite.
asm 05080 15  ; the digit loop (LD A,(DE); ADD $9D; OUT (C),A; ...; DJNZ) -> page 0 dig7E
    rst $00
    db far_io, pg_dig7E, ent_dig7E
    jp $508F
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
endasm
asm 0506F 13  ; the one digit (LD A,(DE); ADD $9C; OUT (C),A; ...; OUT (C),A) -> page 0 dig6F
    rst $00
    db far_io, pg_dig6F, ent_dig6F
    jp $507C
    nop
    nop
    nop
    nop
    nop
    nop
endasm
asm 05176 15  ; the bar loop (XOR 0; XOR 0; OUTI; ...; JR NZ) -> page 0 bar76
    rst $00
    db far_io, pg_bar76, ent_bar76
    jp $5185
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
endasm
page 0 ntblit rect vclr tconv ld15 ld31 lz fill8 don don2 p148c dig7E dig6F bar76
    OPT --zxnext        ; NEXTREG
T_CONV   equ $0000      ; the runtime's conv_tables: FW2_PAGE in slot 0 while tiles convert
SHADOW_HI equ 29        ; runtime SHADOW_PAGE+1: VRAM $2000-$3FFF
; ntblit: the play area blit at $14E2 (rows 2-23 from the cell list at $C400, high byte $01, or
; $11 when the tile is at least ($C6C3)). Each cell whose value changes is written into the
; VRAM copy, with the priority switch with its marks as the runtime's pri_markc (fw.asm) sets
; them; each row with a changed cell is then written again into the two Next tilemaps from
; the copy, as nt_put would write each entry (the maps always hold what the copy holds, so the
; other cells get the values they have). Runtime internals:
;   SHADOW_PAGE+1 29 in slot 2: VRAM $2000-$3FFF at $4000;
;   MAP_PAGE 14 in slot 0: M0 at $0000 and A8 at $0A00, 40 columns of 2 bytes, 80 bytes a row.
;     M0 holds SMS columns 0-31 in Next columns 0-31 and SMS columns 0-7 again in 32-39; A8
;     holds SMS columns 8-31, 0-7, 0-7 (A8 entry = M0 entry + $0A00 - 16 for columns 8-31;
;     columns 0-7 also at M0 + 64, A8 + 64 and A8 + 80). The copper's M0 to A8 switch reads
;     the maps as they are, so it needs nothing more. The marks: $1BC0 + row (the row has
;     priority cells), $1BE0 + row (the row has marked cells), $1C00 + cell (bit 0 marked,
;     bit 1 Layer 2 holds the cell);
;   mapattr_table $E200 (the Next attribute of an entry's high byte), nt_base $E04B,
;   fw_flags $E09E bit 0 (priority).
; Then the last cell again with the VDP state the game's writes leave (nlast: address $3E00,
; code 1, latch clear, read buffer the last byte), and pdraw for Layer 2.
; It stops with jt_fatal if the name table is not at $3800 (register 2 is always $FF here).
MAPATTR  equ $E200
NT_SHAD  equ $4000+$1880        ; VRAM $3880 (row 2) in the copy, mapped in slot 2
CELLS    equ 704
ntblit:
    call pbegin
    xor a
    ld (p_ei),a                 ; the game's loop runs with interrupts off
    push ix
    push iy
    exx                         ; the game's BC', DE', HL'
    push bc
    push de
    push hl
    ld hl,0                     ; HL' = cells with the priority bit
    exx
    ld hl,(nt_base)
    ld de,$3800
    or a
    sbc hl,de
    call nz,jt_fatal
    ld a,(P_FLAGS)
    and 1
    ld (n_pri),a
    ld a,($C6C3)
    ld ixl,a
    ld ixh,2                    ; row
    nextreg $50,P_MAP
    nextreg $52,SHADOW_HI
    ld hl,$C400
    ld de,NT_SHAD
    ld iy,$1C00+2*32            ; the cell's mark
.row:
    call ptick
    xor a
    ld (n_rc),a
    ld (n_rm),a
    ld (n_rp),a
; the row's cells: the copy compared and written, the marks
.cell:
    ld c,(hl)                   ; C = tile
    inc hl
    ld a,c
    cp ixl
    ld b,$01                    ; B = high byte
    jr c,.lo
    ld b,$11
    exx
    inc hl
    exx
.lo:
    ex de,hl
    ld a,c
    cp (hl)
    jr nz,.wt
    inc hl
    ld a,b
    cp (hl)
    jr nz,.wh
    inc hl
    ex de,hl
    jr .nx
.wt:
    ld (hl),c
    inc hl
.wh:
    ld (hl),b
    inc hl
    ex de,hl
    ld a,1
    ld (n_rc),a
    ld a,(n_pri)
    or a
    jr z,.nx
    bit 4,b
    jr z,.np
    set 0,(iy+0)                ; the priority bit: marked, the row has priority cells
    ld (n_rp),a
    ld (n_rm),a
    jr .nx
.np:
    bit 1,(iy+0)                ; else only a cell Layer 2 holds
    jr z,.nx
    set 0,(iy+0)
    ld (n_rm),a
.nx:
    inc iy
    ld a,e
    and $3F
    jp nz,.cell
; the row's flags
    push hl
    ld h,$1B
    ld a,(n_rp)
    or a
    jr z,.f1
    ld a,ixh
    add a,$C0
    ld l,a
    ld (hl),1
.f1:
    ld a,(n_rm)
    or a
    jr z,.f2
    ld a,ixh
    add a,$E0
    ld l,a
    ld (hl),1
.f2:
; a changed row: M0 and A8 written again from the copy
    ld a,(n_rc)
    or a
    jr z,.rx
    push de
    ld d,ixh
    ld e,80
    mul d,e
    ld (n_s),de                 ; S = the row in M0
    pop de
    push de
    ex de,hl
    ld de,-64
    add hl,de
    ex de,hl                    ; DE = the row in the copy
    ld hl,(n_s)
    ld b,MAPATTR>>8
.m: ld a,(de)                   ; the tile, then the attribute of the high byte
    ld (hl),a
    inc e
    inc hl
    ld a,(de)
    ld c,a
    ld a,(bc)
    ld (hl),a
    inc e
    inc hl
    ld a,e
    and $3F
    jr nz,.m
    ld de,(n_s)                 ; M0 columns 32-39 = SMS columns 0-7
    ld hl,64
    add hl,de
    ex de,hl
    ld bc,16
    ldir
    ld hl,(n_s)                 ; A8 columns 0-31 = M0 columns 8-39
    ld de,$0A00
    add hl,de
    ex de,hl
    ld hl,(n_s)
    ld bc,16
    add hl,bc
    ld bc,64
    ldir
    ld hl,(n_s)                 ; A8 columns 32-39 = SMS columns 0-7
    ld bc,16
    ldir
    pop de
.rx:
    pop hl
    inc ixh
    ld a,ixh
    cp 24
    jp nz,.row
; the last cell again: the VDP state as after the game's last write
    ex de,hl
    dec hl
    ld a,(hl)
    ld (n_last+1),a
    dec hl
    ld a,(hl)
    ld (n_last),a
    ld a,(cur_mmu+0)
    nextreg $50,a
    ld a,(cur_mmu+2)
    nextreg $52,a
    ld hl,n_last
    ld de,$3880+2*(CELLS-1)
    call nlast
    call pdraw
    exx
    ld (n_hi),hl
    pop hl
    pop de
    pop bc
    exx
    ld hl,(n_hi)                 ; the loop's time on a Master System: 128 + 79 a cell,
    add hl,hl                    ; 81 for a cell with the priority bit
    ld de,128+79*CELLS
    add hl,de
    ex de,hl
    call padd
    call pend
; the registers as the game's loop leaves them (before its EI)
    pop iy
    pop ix
    ld hl,$C400+CELLS
    ex de,hl
    ld a,($C6C3)
    ld c,a
    ld b,$01
    ld hl,0
    xor a
    ret
n_pri:  db 0
n_rc:   db 0
n_rm:   db 0
n_rp:   db 0
n_s:    dw 0
n_last: dw 0
; p148c: at $14A2 in the cell list builder $148C (LD IY,$C400; LD BC,$100B): the builder's
; time on a Master System, waited before it runs. Its code has no branch that depends on data
; but RST $28: 174 to the cave with RST $28 (70 at most), the 11 x 16 blocks 43,549, the end 47:
; 43,840 T-states, less the eighth that its own code then takes on the Next at 28 MHz. The
; wait does the waiting work (pwork). Then IY and BC as the replaced code sets them.
p148c:
    call pbegin
    push de
    ld de,43840-43840/8
    call padd
    call pend
    pop de
    ld iy,$C400
    ld bc,$100B
    ret
; rect: the game's rectangle routine at $06B6 (jump vector $0218; also the frame
; handler's mailbox case 2 at $0A77): B cells across, C rows $40 apart, at the VRAM
; address in HL (bits 14-15 the VDP code), tiles from DE, every high byte A. Interrupts
; stay as they were. Out as the game's loop leaves them: HL + C*$40, DE past the
; source, B, C = 0, A, Z and N set, carry clear. Row by row, the row's cells from the
; source as the game sees it, then each run of cells that differ from the VRAM copy
; written as nwrite writes them (all cells when the rectangle does not lie in $3800-$3FFF),
; and at the end the last cell again with the VDP state it leaves (nlast).
; With the display off, the tiles still marked are then converted (tall), so the
; once-a-frame work does not do it when the game turns interrupts on.
rect:
    ld (r_attr),a
    ld (r_hl),hl
    ld (r_de),de
    ld (r_bc),bc
    ld a,i
    ld a,0
    jp po,.i0
    inc a
.i0:
    ld (r_ei),a
    di
    call pbegin                  ; (interrupts are off now: the wait keeps them off)
    push ix
    push iy
    ld a,b
    dec a
    cp 32
    call nc,jt_fatal        ; width 1-32
    ld a,c
    dec a
    cp 28
    call nc,jt_fatal        ; rows 1-28
; compare with VRAM only when the whole rectangle lies in $3800-$3FFF
    ld hl,(r_hl)
    ld a,h
    and $3F
    ld h,a
    ld (r_v),hl
    ld (r_row),hl
    xor a
    ld (r_all),a
    ld a,h
    cp $38
    jr c,.all
    ld a,(r_bc)
    ld e,a
    ld d,$40
    mul d,e                  ; rows * $40
    add hl,de
    ld a,h
    cp $40
    jr c,.cmp
    jr nz,.all
    ld a,l
    or a
    jr z,.cmp
.all:
    ld a,1
    ld (r_all),a
.cmp:
    ld hl,(r_de)
    ld (r_src),hl
    ld a,(r_bc)
    ld (r_rows),a
.row:
    call ptick
    ld hl,(r_src)                ; the row's cells as the game writes them
    ld de,img
    ld a,(r_bc+1)
    ld b,a
.bc:
    call jt_peek
    inc hl
    ld (de),a
    inc de
    ld a,(r_attr)
    ld (de),a
    inc de
    djnz .bc
    ld (r_src),hl
    ld hl,img
    ld de,(r_row)
    ld a,(r_bc+1)
    ld c,a                       ; C = cells left in the row
.cc:
    call rdiff
    jr nz,.st
    call rnext
    dec c
    jr nz,.cc
    jr .rend
.st:
    push hl                      ; a run of differing cells
    push de
    ld b,0
.ct:
    inc b
    call rnext
    dec c
    jr z,.wr
    call rdiff
    jr nz,.ct
.wr:
    ld (r_hp),hl
    ld (r_dp),de
    pop de
    pop hl
    push bc
    call nwrc
    pop bc
    ld hl,(r_hp)
    ld de,(r_dp)
    ld a,c
    or a
    jr nz,.cc
.rend:
    ld hl,(r_row)
    ld de,$40
    add hl,de
    ld (r_row),hl
    ld a,(r_rows)
    dec a
    ld (r_rows),a
    jp nz,.row
; the last cell again: the VDP state as after the game's last write
    ld a,(r_bc+1)
    dec a
    add a,a
    ld hl,(r_row)
    ld de,-$40
    add hl,de
    add hl,a
    ex de,hl                     ; DE = its VRAM address
    ld hl,img
    add hl,a
    call nlast
    call pdraw
    ld a,(vdp_regs+1)            ; the display off: no tile left for the once-a-frame work
    and $40
    call z,tall
    ld a,(r_bc+1)               ; the loop's time on a Master System: 10 + C (120 + 37 B)
    ld e,a
    ld d,37
    mul d,e
    ld hl,120
    add hl,de
    ex de,hl
    ld a,(r_bc)
    ld b,a
.pt:
    call padd
    djnz .pt
    ld de,10
    call padd
    call pend
; registers and interrupts as the game's routine leaves them
    pop iy
    pop ix
    ld a,(r_bc)
    ld e,a
    ld d,$40
    mul d,e
    ld hl,(r_hl)
    add hl,de
    ld de,(r_src)
    ld a,(r_bc+1)
    ld b,a
    ld c,0
    ld a,(r_ei)
    or a
    jr z,.f
    ei
.f:
    or a                    ; carry clear
    ld a,1
    dec a                   ; Z and N set
    ld a,(r_attr)
    ret
; rdiff: HL = a cell in img, DE = its VRAM address: NZ when it differs from the VRAM copy
; (always with r_all). The copy's page is mapped in slot 2 for the compare.
rdiff:
    ld a,(r_all)
    or a
    ret nz
    nextreg $52,SHADOW_HI
    push de
    ld a,d
    add a,$20               ; VRAM $2000-$3FFF is at $4000-$5FFF in slot 2
    ld d,a
    ld a,(de)
    cp (hl)
    jr nz,.x
    inc de
    inc hl
    ld a,(de)
    cp (hl)
    dec hl
.x: pop de
    ld a,(cur_mmu+2)
    nextreg $52,a
    ret
rnext:
    inc hl
    inc hl
    inc de
    inc de
    ret
; HL = source in this page, DE = VRAM address, B = bytes: one jt_vwrite run
vrun:
    ld c,1
    ld ix,0
    ld iy,0
    ld a,1
    jp jt_vwrite
; nwrite: B cells (tile, high byte) from HL in this page to the VRAM address DE (even): each
; cell of name table rows 0-23 at $3800 straight into the VRAM copy, M0, A8 and the marks
; (nput), any other cell through jt_vwrite; then the VDP state as the game's last write
; leaves it (nlast). Changes AF, BC, DE, HL, IX, IY.
nwrite:
    push bc
    push de
    push hl
.c: push bc
    call nputx
    inc hl
    inc hl
    inc de
    inc de
    pop bc
    djnz .c
    pop hl
    pop de
    pop bc
    dec b                        ; the last cell
    ld a,b
    add a,a
    add hl,a
    ex de,hl
    add hl,a
    ex de,hl
    jp nlast
; nlast: the cell at HL to VRAM DE again as the game's last write (nputx), then the VDP state
; that write leaves: address DE + 2, code 1 (a VRAM write), latch clear, read buffer the
; cell's high byte (as vclr sets it).
nlast:
    call nputx
    inc hl
    ld a,(hl)
    ld (vdp_rbuf),a
    ex de,hl
    inc hl
    inc hl
    ld a,h
    and $3F
    ld h,a
    ld (vdp_addr),hl
    ld a,1
    ld (vdp_code),a
    xor a
    ld (vdp_latch),a
    ret
; nputx: the cell at HL to VRAM DE: nput, or jt_vwrite outside rows 0-23 of the table at $3800.
; Keeps HL, DE.
nputx:
    ld a,d
    and $3F
    cp $38
    jr c,.v
    cp $3E
    jr nc,.v
    ld a,(nt_base)
    or a
    jr nz,.v
    ld a,(nt_base+1)
    cp $38
    jr nz,.v
    nextreg $50,P_MAP
    nextreg $52,SHADOW_HI
    call nput
    ld a,(cur_mmu+0)
    nextreg $50,a
    ld a,(cur_mmu+2)
    nextreg $52,a
    ret
.v: push hl
    push de
    ld b,2
    call vrun
    pop de
    pop hl
    ret
; nput: one cell of name table rows 0-23 (the table at $3800): tile (HL), high byte (HL+1) at
; VRAM DE, as nt_put and pri_markc write it (see ntblit): the copy, the M0 entry (and for SMS
; columns 0-7 M0 + 64, A8 + 64, A8 + 80; else the A8 entry), with the priority switch the
; marks. MAP_PAGE in slot 0, SHADOW_PAGE+1 in slot 2. Keeps HL, DE.
nput:
    push hl
    push de
    ld b,(hl)
    inc hl
    ld c,(hl)                    ; B = tile, C = high byte
    ld a,d
    and $3F
    ld d,a
    add a,$20
    ld h,a
    ld l,e
    ld (hl),b                    ; the copy
    inc hl
    ld (hl),c
    ld a,e
    and $3F
    rrca
    ld (n_col),a
    ld a,d
    sub $38
    ld h,a
    ld l,e                       ; HL = o, the offset in the table
    push hl
    add hl,hl
    add hl,hl                    ; H = row
    ld a,h
    ld (n_r),a
    ld e,a
    ld d,16
    mul d,e
    pop hl
    add hl,de                    ; HL = the M0 entry
    ld e,c
    ld d,MAPATTR>>8
    ld a,(de)
    ld (n_at),a
    ld (hl),b
    inc hl
    ld (hl),a
    dec hl
    ld a,(n_col)
    cp 8
    jr nc,.hi
    push hl
    ld de,64                     ; M0 columns 32-39
    add hl,de
    call .two
    ld de,$0A00-16               ; A8 columns 24-31
    add hl,de
    call .two
    ld de,16                     ; A8 columns 32-39
    add hl,de
    call .two
    pop hl
    jr .mk
.hi:
    ld de,$0A00-16               ; the A8 entry
    add hl,de
    call .two
.mk:
    ld a,(P_FLAGS)
    rra
    jr nc,.x
    ld a,(n_r)                   ; the mark: $1C00 + 32 row + column
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,(n_col)
    add hl,a
    ld a,h
    add a,$1C
    ld h,a
    bit 4,c
    jr z,.np
    set 0,(hl)
    ld a,(n_r)
    add a,$C0
    ld l,a
    ld h,$1B
    ld (hl),1
    jr .rm
.np:
    bit 1,(hl)
    jr z,.x
    set 0,(hl)
.rm:
    ld a,(n_r)
    add a,$E0
    ld l,a
    ld h,$1B
    ld (hl),1
.x: pop de
    pop hl
    ret
.two:
    ld (hl),b
    inc hl
    ld a,(n_at)
    ld (hl),a
    dec hl
    ret
n_col:  db 0
n_at:   db 0
n_r:    db 0
; nwrc: B cells from HL to DE as nwrite writes them, without the last cell again
nwrc:
.c: push bc
    call nputx
    inc hl
    inc hl
    inc de
    inc de
    pop bc
    djnz .c
    ret
; tall: every tile still marked converted (tstep until none is left)
tall:
    call tstep
    jr nz,tall
    ret
; ---- the status bar: digits and the bar, written by the game one cell at a time ----
; dig7E: the loop at $5080 in $507E (after DI; RST $18 set the VDP address from HL): B
; digits from (DE) down, each cell tile (DE) + $9D, high byte $19. dig6F: the one digit
; at $506F, tile (DE) + $9C. The cells go out at vdp_addr through nwrite; pdraw then
; queues or draws their Layer 2 (they are priority cells); with the display off the tiles
; still marked are converted (tall). Then the loop's Master System time: 78 a digit, 73
; the last ($507E); 65 ($506F). Out as the game's code leaves them: A = $19, the flags of
; NEG of the last tile, DE down by the digits, HL up by them, B = 0 ($507E) or as it was
; ($506F), C as it was. The game's EI; RET follows the cave.
dig7E:
    call gstack
    ld a,$9D
    ld (g_add),a
    xor a
    ld (g_one),a
    jr digit
dig6F:
    call gstack
    ld a,$9C
    ld (g_add),a
    ld a,1
    ld (g_one),a
    ld (g_bc),bc
    ld b,1
digit:
    ld a,b
    ld (g_n),a
    ld a,(g_one)
    or a
    jr nz,.s
    ld (g_bc),bc
.s:
    call pbegin
    push ix
    push iy
    ld (g_hl),hl
    ld hl,img
    ld a,(g_add)
    ld c,a
.b: ld a,(de)
    add a,c
    ld (hl),a
    ld (g_last),a
    inc hl
    ld (hl),$19
    inc hl
    dec de
    djnz .b
    ld (g_de),de
    ld a,(g_n)
    ld b,a
    ld hl,img
    ld de,(vdp_addr)
    call nwrite
    call pdraw
    ld a,(vdp_regs+1)
    and $40
    call z,tall
    ld a,(g_one)
    or a
    ld de,65
    jr nz,.t
    ld a,(g_n)                   ; 78 n - 5
    ld e,a
    ld d,78
    mul d,e
    dec de
    dec de
    dec de
    dec de
    dec de
.t: call padd
    call pend
    pop iy
    pop ix
    ld hl,(g_hl)
    ld a,(g_n)
    add hl,a
    ld de,(g_de)
    ld bc,(g_bc)
    ld a,(g_one)
    or a
    jr nz,.o
    ld b,0
.o: ld a,(g_last)
    neg
    ld a,$19
    ld sp,(g_sp)                 ; the game's stack again
    ret
; bar76: the loop at $5176 in $516B (after DI; RST $18; RST $10): B cells from (HL) up,
; each with OUTI, high byte $19, as dig7E; its Master System time 80 a cell, 75 the last.
; Out: HL up by the cells, B = 0, Z set, A = $19, C and DE as they were.
bar76:
    call gstack
    ld (g_bc),bc
    ld a,b
    ld (g_n),a
    call pbegin
    push ix
    push iy
    push de
    ld de,img
.b: call jt_peek
    inc hl
    ld (de),a
    inc de
    ld a,$19
    ld (de),a
    inc de
    djnz .b
    ld (g_hl),hl
    ld a,(g_n)
    ld b,a
    ld hl,img
    ld de,(vdp_addr)
    call nwrite
    call pdraw
    ld a,(vdp_regs+1)
    and $40
    call z,tall
    ld a,(g_n)                   ; 80 n - 5
    ld e,a
    ld d,80
    mul d,e
    dec de
    dec de
    dec de
    dec de
    dec de
    call padd
    call pend
    pop de
    pop iy
    pop ix
    ld hl,(g_hl)
    ld bc,(g_bc)
    ld b,1
    dec b                        ; B = 0, Z set
    ld a,$19
    ld sp,(g_sp)                 ; the game's stack again
    ret
; gstack: these entries run on a stack of their own in this page (g_stk), from the game's
; DI to its EI after the cave, so their calls write nothing below the game's stack. p1get's
; far call (which maps page 1 over this page) is made first, on the game's stack; nothing
; under them maps slot 1 with the stack in use (jt_peek keeps none there, jt_vwrite has its
; own). Interrupts stay off throughout. Changes AF.
gstack:
    call p1get
    pop af                       ; the return into the entry
    ld (g_sp),sp                 ; the game's SP, the far call's frame on top
    ld sp,g_stk
    push af
    ret
g_sp:   dw 0
g_stkb: ds 96
g_stk:
g_add:  db 0
g_one:  db 0
g_n:    db 0
g_last: db 0
g_bc:   dw 0
g_de:   dw 0
g_hl:   dw 0
; pmask: one name table row (pm_row) of pal_scan's work done ahead (fw3.asm): each entry with
; the sprite palette (high byte bit 3) whose tile has no set of pixel values in tm_mask gets
; it, as tile_mask makes it from the Next tile definition with nibm (page 1 holds the same
; table). So the once-a-frame pal_scan finds every set made. NZ: a row was done; Z: none
; left (pm_row 28). pdraw starts the rows again (pm_row 0). Runtime internals: FW3_PAGE 100
; (tm_mask at $0000, here in slot 3), TILE_PAGE 10, 11, SHADOW_PAGE+1 29, nt_base. Interrupts
; are off. Changes AF, BC, DE, HL.
pmask:
    ld a,(pm_row)
    cp 28
    jr c,.go
    xor a
    ret
.go:
    inc a
    ld (pm_row),a
    ld a,(nt_base+1)
    cp $20
    jr nc,.nt
    ld a,28                      ; the name table below $2000: left to pal_scan
    ld (pm_row),a
    xor a
    ret
.nt:
    call pq_close
    call p1get
    nextreg $50,a
    nextreg $52,SHADOW_HI
    nextreg $53,T_FW3
    nextreg $54,T_TILES
    nextreg $55,T_TILES+1
    ld a,(pm_row)
    dec a
    ld e,a
    ld d,64
    mul d,e
    ld hl,(nt_base)
    add hl,de
    ld a,h
    add a,$20
    ld h,a
    inc hl                       ; the row's first high byte in slot 2
    ld b,32
.e: bit 3,(hl)
    jr z,.n
    push bc
    push hl
    ld a,(hl)
    and 1
    ld b,a
    dec l
    ld c,(hl)                    ; BC = tile
    ld h,b
    ld l,c
    add hl,hl
    ld de,$6000
    add hl,de                    ; its tm_mask entry
    ld a,(hl)
    inc hl
    or (hl)
    jr nz,.k
    push hl
    ld h,b
    ld l,c
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld de,$8000
    add hl,de                    ; its definition: 32 bytes, 32-byte aligned
    ld de,0
    ld b,P1_NIBM>>8
.c: ld c,(hl)
    ld a,(bc)
    or e
    ld e,a
    inc b
    ld a,(bc)
    or d
    ld d,a
    dec b
    inc l
    ld a,l
    and $1F
    jr nz,.c
    pop hl
    ld (hl),d
    dec hl
    ld (hl),e
.k: pop hl
    pop bc
.n: inc l
    inc l
    djnz .e
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
    or 1
    ret
pm_row: db 28
; p1get: A = the RAM page of code page 1 (its tables), found once with a far call to its
; entry p1no.
p1get:
    ld a,(p1pg)
    or a
    ret nz
    rst $00
    db far_io, pg_p1no, ent_p1no
    ld (p1pg),a
    ret
p1pg:   db 0
; vclr: the game's loop at $032D: A to the data port, 256 times C (B = 0, the only use, $0329).
; With the VRAM address on a 256-byte boundary and A = 0, each tile page (region_tab 0) is
; zeroed straight in the VRAM copy and the Next tile definitions, its dirty_pages bits are
; cleared and its tiles get conv_page's bookkeeping (tbook); the other pages (name table,
; sprite table) go through jt_vwrite. Otherwise every page goes through jt_vwrite. Then it
; takes the loop's time on a Master System (pace): 6,153 T-states a page. Out: A, B = 0,
; C = 0, Z and N set, carry clear; the VDP state as after the game's last write.
; Runtime internals as tconv, and region_tab $E400.
V_REGION equ $E400
vclr:
    ld (v_a),a
    ld a,b
    or a
    call nz,jt_fatal
    ld a,c
    ld (v_c),a
    push de
    push hl
    push ix
    push iy
    call pbegin
    ld de,(vdp_addr)
    ld (v_d),de
    ld a,(v_a)
    or e
    ld (v_slow),a             ; non-zero: every page through jt_vwrite
    ld hl,tlist
    ld (t_lp),hl
.pg:
    ld de,(v_d)
    ld a,(v_slow)
    or a
    jr nz,.vw
    ld a,d
    and $3F
    ld d,a
    ld l,a
    ld h,V_REGION>>8
    ld a,(hl)
    or a
    jr nz,.vw
    ; a tile page: zeros in the copy and the definitions, its tiles booked
    ld a,l
    add a,$40                 ; dirty_pages
    ld l,a
    ld (hl),0
    nextreg $52,T_SHADOW
    nextreg $53,T_SHADOW+1
    nextreg $54,T_TILES
    nextreg $55,T_TILES+1
    ld a,d
    add a,$40
    ld h,a
    ld l,0
    call z256
    ld a,d
    add a,$80
    ld h,a
    ld l,0
    call z256
    ld hl,(t_lp)
    ld (hl),d
    inc hl
    ld (hl),$FF
    inc hl
    ld (t_lp),hl
    ld a,(cur_mmu+2)
    nextreg $52,a
    ld a,(cur_mmu+3)
    nextreg $53,a
    ld a,(cur_mmu+4)
    nextreg $54,a
    ld a,(cur_mmu+5)
    nextreg $55,a
    ld a,(v_d+1)              ; the VDP address moves past the page
    inc a
    and $3F
    ld (v_d+1),a
    xor a
    ld (v_d),a
    jr .nx
.vw:
    ld a,(v_a)
    ld hl,img
    ld b,0
.f: ld (hl),a
    inc hl
    djnz .f
    ld hl,img
    ld b,0
    ld c,1
    ld ix,0
    ld iy,0
    ld a,1
    call jt_vwrite
    ld de,(vdp_addr)
    ld (v_d),de
.nx:
    ld de,6153
    call padd
    call ptick
    ld a,(p_ei)
    or a
    jr z,.nw
    ei                        ; the game's interrupts between pages, as in its loop
    nop
    di
.nw:
    ld hl,v_c
    dec (hl)
    jp nz,.pg
    ld hl,(t_lp)
    ld de,tlist
    or a
    sbc hl,de
    call nz,tbook
    ; the VDP state the game's last write leaves (vdp_addr, vdp_code, vdp_latch, vdp_rbuf)
    ld hl,(v_d)
    ld (vdp_addr),hl
    ld a,1
    ld (vdp_code),a
    xor a
    ld (vdp_latch),a
    ld a,(v_a)
    ld (vdp_rbuf),a
    call pend
    pop iy
    pop ix
    pop hl
    pop de
    ld bc,0
    or a
    ld a,1
    dec a                     ; Z and N set, carry clear
    ld a,(v_a)
    ret
z256:
    xor a
    ld b,0
.z: ld (hl),a
    inc hl
    djnz .z
    ret
v_c:    db 0
v_d:    dw 0
v_slow: db 0
; ---- pacing: the Master System's T-states of a routine, waited on the Next's raster ----
; pbegin: notes the game's interrupt state, turns interrupts off, and starts the count.
; padd: DE = T-states more (at most 65,000). ptick: the lines passed since the last call; it
; sees the gap modulo a frame, so every loop that can run long calls it. pend: waits until
; the lines passed reach the T-states in lines, with the game's interrupts on while it waits
; when they were on; then leaves interrupts as the game had them. The unit makes a Master
; System frame a Next frame (as Psycho Fox's smswait): at 50 Hz 71,364 T-states (a PAL frame)
; to 311 lines, at 60 Hz 59,736 (an NTSC frame) to 264 lines; p_div is the T-states a line
; in 1/256 (58,744 or 57,926), and the part of a line left over carries (p_rem, 1/256).
; While pend waits it does the work that waits for time (pwork: tile conversion, Layer 2
; cells). Video timing from NextReg $05 bit 2; the raster line from NextRegs $1E/$1F.
pbegin:
    push af
    push bc
    push de
    push hl
    ld a,i
    ld a,0
    jp po,.i
    inc a
.i: ld (p_ei),a
    di
    ld bc,$243B
    ld a,$05
    out (c),a
    inc b
    in a,(c)
    ld hl,311
    ld de,58744
    bit 2,a
    jr z,.hz
    ld hl,264
    ld de,57926
.hz:
    ld (p_wlen),hl
    ld (p_div),de
    ld hl,0
    ld (p_ln),hl
    ld (p_rem),hl
    ld hl,($E02B)               ; fw_frames: no frame since the last paced routine? Then its
    ld de,(p_fr)                ; overrun (p_debt, lines) counts against this one
    or a
    sbc hl,de
    ld hl,0
    jr nz,.nd
    ld hl,(p_debt)
.nd:
    ld (p_el),hl
    call pline
    ld (p_last),hl
    pop hl
    pop de
    pop bc
    pop af
    ret
padd:
    push af
    push bc
    push hl
    ld hl,(p_rem)               ; A:HL = DE * 256 + p_rem
    ld a,e
    add a,h
    ld h,a
    ld a,d
    adc a,0
    ld bc,(p_div)
.d: or a
    jr nz,.s                    ; 65,536 or more: a line
    push hl
    sbc hl,bc
    pop hl
    jr c,.dd
.s: or a
    sbc hl,bc
    sbc a,0
    push hl
    ld hl,(p_ln)
    inc hl
    ld (p_ln),hl
    pop hl
    jr .d
.dd:
    ld (p_rem),hl
    pop hl
    pop bc
    pop af
    ret
ptick:
    push af
    push de
    push hl
    call pline
    ld de,(p_last)
    ld (p_last),hl
    or a
    sbc hl,de
    jr nc,.p
    ld de,(p_wlen)
    add hl,de
.p: ld de,(p_el)
    add hl,de
    ld (p_el),hl
    pop hl
    pop de
    pop af
    ret
pend:
    push af
    push hl
    push de
.w: call ptick
    ld hl,(p_el)
    ld de,(p_ln)
    or a
    sbc hl,de
    jr nc,.x
    call pwork                   ; tiles to convert, Layer 2 cells: done in the time left
    jr nz,.w
    call pq_close
    ld a,(p_ei)
    or a
    jr z,.w
    ei                         ; wait with the game's interrupts on, as it had them
    halt
    di
    jr .w
.x: push hl
    call pq_close
    pop hl
    ld (p_debt),hl              ; lines past the budget
    ld hl,($E02B)
    ld (p_fr),hl
    pop de
    pop hl
    ld a,(p_ei)
    or a
    jr z,.di
    pop af
    ei
    ret
.di:
    pop af
    ret
; pline: HL = the Next's raster line (interrupts are off)
pline:
    push bc
    ld bc,$243B
.a: ld a,$1E
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
    pop bc
    ret
p_ei:   db 0
p_wlen: dw 311
p_div:  dw 58744
p_el:   dw 0
p_ln:   dw 0
p_rem:  dw 0
p_last: dw 0
p_debt: dw 0
p_fr:   dw $FFFF
; ---- lz: the game's decompressor loop at $0973 and the token handler at $0982 ----
; HL = the stream (in slot 2 or 1; read with jt_peek in $2000-$3FFF), ($D802) = its end.
; Does what the game's code does: each token's output bytes to the VDP data port (here
; buffered, written with jt_vwrite at vdp_addr), into the 2K ring at $D000 with the index
; at $D800, and the LZ copy through $D804 and the buffer at $D80E. Then it takes the
; Master System's time of every path (pace):
;   loop and token head 113; then an LZ copy (2 bytes) 324 + 265 a byte (n = 2-17);
;   a literal 38 + 177 a byte; a run 116 (131 with bit 5) + R (67 + 177 E) + 18;
;   the loop's exit 50.
; Out as the game's loop leaves: HL = stream - end, BC = end, carry clear.
lz:
    call pbegin
    push ix
    push iy
    xor a
    ld (ob_n),a
.tok:
    ld bc,($D802)
    or a
    sbc hl,bc
    jp nc,.end
    add hl,bc
    call ptick
    call lzstep
    ld a,(p_ei)
    or a
    jr z,.nw
    ei                         ; the game's interrupts between tokens, when it had them on
    nop
    di
.nw:
    ld de,113
    call padd
    call rd
    inc hl
    bit 7,a
    jp z,.lzc
    bit 6,a
    jr z,.lit
; a run: E bytes R times
    ld (lz_a),a
    bit 5,a
    ld de,116
    jr z,.r0
    ld de,131
    and 7
    ld b,a
    call rd
    inc hl
    ld c,a
    jr .r1
.r0:
    and 7
    ld c,a
    ld b,0
.r1:
    inc bc
    inc bc                     ; R
    call padd
    ld a,(lz_a)
    rra
    rra
    rra
    and 3
    inc a
    ld (lz_e),a                ; E
    ld de,18
    call padd
.rr:
    push bc
    push hl
    ld a,(lz_e)
    ld d,a
.rb:
    call rd
    call obyte
    call put
    inc hl
    dec d
    jr nz,.rb
    pop hl
    ld a,(lz_e)                ; 67 + 177 E
    ld e,a
    ld d,177
    mul d,e
    ld a,67
    add de,a
    call padd
    pop bc
    dec bc
    ld a,b
    or c
    jr nz,.rr
    ld a,(lz_e)
    add hl,a
    jp .tok
; a literal: (A & $3F) + 1 bytes
.lit:
    and $3F
    inc a
    ld b,a
    ld e,a
    ld d,177
    mul d,e
    ld a,38
    add de,a
    call padd
.lb:
    call rd
    call obyte
    call put
    inc hl
    djnz .lb
    jp .tok
; an LZ copy: 12-bit offset back from the ring index, (second & 15) + 2 bytes
.lzc:
    ld e,a
    ld d,0
    ex de,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ex de,hl                   ; DE = A << 4
    call rd
    rra
    rra
    rra
    rra
    and $0F
    or e
    ld e,a
    push hl
    ld hl,($D800)
    or a
    sbc hl,de
    ld a,h
    and 7
    ld h,a
    ld (lz_src),hl
    pop hl
    call rd
    inc hl
    and $0F
    add a,2
    ld (lz_n),a
    push hl
    ld b,a
    ld e,a
    ld d,9
    mul d,e                    ; 9 n
    ld h,b
    ld l,0                     ; 256 n
    add hl,de
    ld de,324
    add hl,de
    ex de,hl                   ; 324 + 265 n
    call padd
    ld de,$D80E
    ld hl,(lz_src)
.cp:
    push hl
    ld a,h
    or $D0
    ld h,a
    ld a,(hl)
    ld (de),a
    inc de
    call obyte
    pop hl
    inc hl
    ld a,h
    and 7
    ld h,a
    djnz .cp
    xor a
    ld ($D804),a
    ld hl,$D80E
    ld a,(lz_n)
    ld b,a
.pu:
    ld a,(hl)
    call put
    inc hl
    djnz .pu
    pop hl
    jp .tok
.end:
    call oflush
    pop iy
    pop ix
    push hl
    push bc
    ld de,50
    call padd
    call pend
    pop bc
    pop hl
    or a
    ret
; lzstep: while lz is ahead of its time, one page of marked tiles converted (tstep). The
; output bytes still in obuf mark their page again when written. Keeps all but AF.
lzstep:
    ld a,(T_DIRTY)
    or a
    ret z
    push bc
    push de
    push hl
    ld hl,(p_el)
    ld de,(p_ln)
    or a
    sbc hl,de
    call c,tstep
    pop hl
    pop de
    pop bc
    ret
; rd: A = the byte the game sees at HL
rd: ld a,h
    and $E0
    cp $20
    jr z,.p
    ld a,(hl)
    ret
.p: jp jt_peek
; put: A into the ring at ($D800), the index then + 1 (mod 2K). Keeps all but F.
put:
    push hl
    push de
    ld e,a
    ld hl,($D800)
    push hl
    ld a,h
    or $D0
    ld h,a
    ld (hl),e
    pop hl
    inc hl
    ld a,h
    and 7
    ld h,a
    ld ($D800),hl
    ld a,e
    pop de
    pop hl
    ret
; obyte: A to the output buffer; full (256): written. Keeps all but F.
obyte:
    push hl
    push af
    ld hl,ob_n
    ld l,(hl)
    ld h,obuf>>8
    pop af
    ld (hl),a
    push af
    ld hl,ob_n
    inc (hl)
    jr nz,.x
    xor a                        ; 256 bytes
    call oflush0
.x: pop af
    pop hl
    ret
oflush:
    ld a,(ob_n)
    or a
    ret z
oflush0:
    push af
    push bc
    push de
    push hl
    push ix
    push iy
    ld b,a                     ; bytes (0 = 256)
    ld c,1
    ld de,(vdp_addr)
    ld hl,obuf
    ld ix,0
    ld iy,0
    ld a,1
    call jt_vwrite
    xor a
    ld (ob_n),a
    pop iy
    pop ix
    pop hl
    pop de
    pop bc
    pop af
    ret
lz_a:   db 0
lz_e:   db 0
lz_n:   db 0
lz_src: dw 0
ob_n:   db 0
; tconv: the game's ring clear at $0954 (EX AF,AF'; EXX; XOR A; HL=$D000, BC=$0820, the RST
; $08 fill; EXX; EX AF,AF') and its time; the wait converts the tiles that dirty_pages marks
; (pwork, tstep), from the VRAM copy into the Next tile definitions, with the bookkeeping of
; the runtime's conv_page (fw3.asm). Interrupts stay as they were. Runtime internals
; (build/rt/runtime.map):
;   SHADOW_PAGE 28, 29 (slots 2-3: $4000 + VRAM address), TILE_PAGE 10, 11 (slots 4-5:
;   $8000 + VRAM address), FW3_PAGE 100 (tm_mask at $0000, in slot 0 here),
;   FW2_PAGE 25 (runs at $2000): conv_tables $2000 (here in slot 0 at $0000 while tiles
;   convert), and in slot 5 at $A000 tile_slot $2400, pri_redo $346A, pri_tiles $3538;
;   part 1: tiles_dirty $E082, tw_cnt $E083, sat_dirty $E085, dirty_pages $E440, cur_mmu.
T_SHADOW  equ 28
T_TILES   equ 10
T_FW3     equ 100
T_FW2     equ 25
T_DIRTY   equ $E082
T_TWCNT   equ $E083
T_SATD    equ $E085
T_DPAGES  equ $E440
T_TSLOT   equ $A000+$0400
T_PREDO   equ $A000+$146A
T_PTILES  equ $A000+$1538
tconv:
    call pbegin
    ex af,af'                    ; the game's ring clear, as at $0954
    exx
    xor a
    ld hl,$D000
    ld bc,$0820
    dec bc
    ld (hl),a
    ld d,h
    ld e,l
    inc de
    ldir
    exx
    ex af,af'
    push de
    ld de,43752                  ; the ring clear's T-states on a Master System
    call padd
    pop de
    jp pend
; ld15, ld31: the tile loaders $0715 and $0731 (jump vectors $0224, $0227), as the list loops
; at $07FB and $080C call them: HL = the record (bank, tiles, source, VRAM address, as $07EB
; reads it). They switch the bank in slot 2 through the runtime (the I/O RST, mapper code $13),
; copy the tiles ($0731 through the table at $0100) into the VRAM copy (tile pages: the bytes
; and the dirty_pages bits; the waits convert them, pwork) or through jt_vwrite (other pages),
; put the bank back, leave the VDP state as the game's writes would, and take the loop's time
; on a Master System: $0715 300 + 553 a tile, $0731 303 + 1,006 a tile. Then the EX DE,HL the
; cave replaced. Runtime internals: as tconv, and region_tab $E400.
ld15:
    xor a
    jr ldt
ld31:
    ld a,1
ldt:
    ld (l_tr),a
    push bc
    push hl
    push de
    push ix
    push iy
    call pbegin
    call rd
    ld (l_bank),a
    inc hl
    call rd
    ld (l_n),a
    inc hl
    call rd
    ld e,a
    inc hl
    call rd
    ld d,a
    ld (l_src),de
    inc hl
    call rd
    ld e,a
    inc hl
    call rd
    and $3F
    ld d,a
    ld (l_v),de
    ld a,($DFFF)
    ld (l_old),a
    ld a,(l_bank)
    rst $00                     ; LD ($FFFF),A through the runtime
    db $13, 0
    ld a,(l_n)
    ld (l_left),a
    call tbulk
.tile:
    ld a,(l_left)
    or a
    jr z,.done
    dec a
    ld (l_left),a
    call ptick
    call tfast
    jr nc,.tile
    ld hl,(l_src)               ; any other tile: its bytes as the game sees them, then vtile
    ld de,img
    ld b,32
.by:
    call rd
    inc hl
    ld c,a
    ld a,(l_tr)
    or a
    ld a,c
    jr z,.st
    push hl
    ld h,$01                    ; $0731: the byte through the table at $0100
    ld l,c
    call rd
    pop hl
.st:
    ld (de),a
    inc de
    djnz .by
    ld (l_src),hl
    ld hl,img
    call vtile
    jr .tile
.done:
    ld a,(l_old)
    rst $00                     ; the bank back
    db $13, 0
    ld hl,(l_v)                 ; the VDP state the game's last write leaves
    ld (vdp_addr),hl
    ld a,1
    ld (vdp_code),a
    xor a
    ld (vdp_latch),a
    ld a,(l_last)
    ld (vdp_rbuf),a
    ld a,(l_n)                  ; the loop's time on a Master System
    ld b,a
    ld de,300
    ld hl,553
    ld a,(l_tr)
    or a
    jr z,.t
    ld de,303
    ld hl,1006
.t: call padd
    ex de,hl
.tn:
    call padd
    djnz .tn
    call pend
    pop iy
    pop ix
    pop de
    pop hl
    pop bc
    ex de,hl
    ret
; tbulk: every tile left (l_left) at once, straight into the VRAM copy, when l_v starts a
; tile, every VRAM page of the run is a tile page (no wrap at $4000), and the source run lies
; in $0000-$1FFF or in $8000-$BFFF: the dirty_pages bits, one LDIR ($0715) or the table at
; $0100 ($0731). Then l_src, l_v, l_last as after the tiles, l_left 0. Otherwise nothing.
tbulk:
    ld a,(l_left)
    or a
    ret z
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld (l_by),hl                ; bytes
    ld de,(l_v)
    ld a,e
    and $1F
    ret nz
    add hl,de
    dec hl                      ; the run's last VRAM byte
    ld a,h
    cp $40
    ret nc
    ld b,h
    ld c,d
.rg:
    ld l,c
    ld h,V_REGION>>8
    ld a,(hl)
    or a
    ret nz                      ; not a tile page
    ld a,c
    inc c
    cp b
    jr nz,.rg
    ld hl,(l_src)               ; the source run
    ld de,(l_by)
    add hl,de
    dec hl
    ld a,(l_src+1)
    cp $20
    jr nc,.s8
    ld a,h
    cp $20
    ret nc
    jr .ok
.s8:
    sub $80
    cp $40
    ret nc
    ld a,h
    sub $80
    cp $40
    ret nc
.ok:
    ld de,(l_v)                 ; dirty_pages: each tile's bit
    ld a,(l_left)
    ld b,a
.db:
    push bc
    ld a,d
    add a,$40
    ld l,a
    ld h,V_REGION>>8
    ld a,e
    rlca
    rlca
    rlca
    and 7
    ld b,a
    ld a,1
    jr z,.b0
.bs:
    add a,a
    djnz .bs
.b0:
    or (hl)
    ld (hl),a
    ld hl,32
    add hl,de
    ex de,hl
    pop bc
    djnz .db
    ld a,1
    ld (T_DIRTY),a
    nextreg $52,T_SHADOW
    nextreg $53,T_SHADOW+1
    ld hl,(l_v)
    ld a,h
    add a,$40
    ld d,a
    ld e,l
    ld hl,(l_src)
    ld a,(l_tr)
    or a
    jr nz,.tr
    ld bc,(l_by)
    ldir
    jr .e
.tr:
    ld ixh,$01                  ; $0731: each byte through the table at $0100 (slot 0)
    ld a,(l_left)
    ld c,a
.tt:
    call ptick
    ld b,32
.tb:
    ld a,(hl)
    inc hl
    ld ixl,a
    ld a,(ix+0)
    ld (de),a
    inc de
    djnz .tb
    dec c
    jr nz,.tt
.e:
    ld (l_src),hl
    dec de
    ld a,(de)
    ld (l_last),a
    ld a,(cur_mmu+2)
    nextreg $52,a
    ld a,(cur_mmu+3)
    nextreg $53,a
    ld hl,(l_v)
    ld de,(l_by)
    add hl,de
    ld a,h
    and $3F
    ld h,a
    ld (l_v),hl
    xor a
    ld (l_left),a
    ret
l_by:   dw 0
; tfast: one tile from l_src straight into the VRAM copy at l_v, when l_v starts a tile in a
; tile page and the source lies in $0000-$1EFF or $8000-$BEFF (not the code page, not the
; copy's slots). Then l_src and l_v move on, l_last is its last byte. Carry: not done.
tfast:
    ld de,(l_v)
    ld a,e
    and $1F
    scf
    ret nz
    ld l,d
    ld h,V_REGION>>8
    ld a,(hl)
    or a
    scf
    ret nz
    ld hl,(l_src)
    ld a,h
    cp $1F
    jr c,.ok
    sub $80
    cp $3F
    ccf
    ret c
.ok:
    push hl
    ld l,d                      ; dirty_pages: the tile's bit
    ld h,V_REGION>>8
    ld a,l
    add a,$40
    ld l,a
    ld a,e
    rlca
    rlca
    rlca
    and 7
    ld b,a
    ld a,1
    jr z,.b0
.bs:
    add a,a
    djnz .bs
.b0:
    or (hl)
    ld (hl),a
    ld a,1
    ld (T_DIRTY),a
    pop hl
    nextreg $52,T_SHADOW
    nextreg $53,T_SHADOW+1
    ld a,d
    add a,$40
    ld d,a
    ld a,(l_tr)
    or a
    jr nz,.tr
    ld bc,32
    ldir
    jr .e
.tr:
    ld b,32
.tb:
    ld a,(hl)
    inc hl
    push hl
    ld h,$01                    ; $0731: the byte through the table at $0100 (slot 0)
    ld l,a
    ld a,(hl)
    pop hl
    ld (de),a
    inc de
    djnz .tb
.e: ld (l_src),hl
    dec de
    ld a,(de)
    ld (l_last),a
    ld a,(cur_mmu+2)
    nextreg $52,a
    ld a,(cur_mmu+3)
    nextreg $53,a
    ld hl,(l_v)
    ld de,32
    add hl,de
    ld a,h
    and $3F
    ld h,a
    ld (l_v),hl
    or a
    ret
; vtile: HL = 32 bytes in this page: one tile at l_v (then l_v + 32)
vtile:
    push hl
    ld de,(l_v)
    ld a,e
    and $1F
    jr nz,.vw                   ; not on a tile boundary: jt_vwrite
    ld l,d
    ld h,V_REGION>>8
    ld a,(hl)
    or a
    jr nz,.vw
    ld a,l                      ; dirty_pages: the tile's bit
    add a,$40
    ld l,a
    ld a,e
    rlca
    rlca
    rlca
    and 7
    ld b,a
    ld a,1
    jr z,.b0
.bs:
    add a,a
    djnz .bs
.b0:
    or (hl)
    ld (hl),a
    ld a,1
    ld (T_DIRTY),a
    nextreg $52,T_SHADOW
    nextreg $53,T_SHADOW+1
    pop hl
    push hl
    ld a,d
    add a,$40
    ld d,a
    ld bc,32
    ldir
    ld a,(cur_mmu+2)
    nextreg $52,a
    ld a,(cur_mmu+3)
    nextreg $53,a
    jr .x
.vw:
    pop hl
    push hl
    ld b,32
    ld c,1
    ld ix,0
    ld iy,0
    ld a,1
    call jt_vwrite
.x: pop hl
    push hl
    ld de,31
    add hl,de
    ld a,(hl)
    ld (l_last),a
    ld hl,(l_v)
    ld de,32
    add hl,de
    ld a,h
    and $3F
    ld h,a
    ld (l_v),hl
    pop hl
    ret
l_tr:   db 0
l_bank: db 0
l_n:    db 0
l_left: db 0
l_old:  db 0
l_last: db 0
l_src:  dw 0
l_v:    dw 0
; fill8: the game's fill at $0008 (RST $08: DEC BC; LD (HL),A; LD D,H; LD E,L; INC DE; LDIR;
; RET), done the same way here, then its time on a Master System: 43 + 21 (BC - 1) T-states
; (BC - 1 = 0 is 65,536, as LDIR counts).
fill8:
    call pbegin
    push bc
    dec bc
    ld (hl),a
    ld d,h
    ld e,l
    inc de
    ldir
    ex (sp),hl                  ; HL = the count, the fill's HL kept on the stack
    push de
    push af
    dec hl                      ; LDIR's count
    ld de,43
    call padd
.k: ld a,h
    or a
    jr z,.r
    ld de,21*256                ; 256 bytes at a time
    call padd
    dec h
    jr .k
.r: ld e,l
    ld d,21
    mul d,e
    call padd
    pop af
    pop de
    pop hl
    ld bc,0
    jp pend
; tstep: converts the tiles of one VRAM page that dirty_pages marks, as the runtime's
; tile_flush and conv_page do for all of them. NZ: a page was converted. Z: none is marked,
; and tiles_dirty and tw_cnt are cleared as tile_flush leaves them. Interrupts are off.
; Keeps IX, IY; changes AF, BC, DE, HL.
tstep:
    ld a,(T_DIRTY)
    or a
    ret z
    call pq_close
    ld hl,T_DPAGES
    ld b,64
.f: ld a,(hl)
    or a
    jr nz,.g
    inc l
    djnz .f
    xor a
    ld (T_DIRTY),a
    ld (T_TWCNT),a
    ld (T_TWCNT+1),a
    ret
.g: ld (hl),0
    ld c,a
    ld a,l
    sub T_DPAGES&255
    ld hl,tlist                  ; the page and its mask, for the bookkeeping
    ld (hl),a
    inc hl
    ld (hl),c
    inc hl
    ld (t_lp),hl
    push ix
    push iy
    nextreg $50,T_FW2            ; conv_tables at $0000
    nextreg $52,T_SHADOW
    nextreg $53,T_SHADOW+1
    nextreg $54,T_TILES
    nextreg $55,T_TILES+1
    call tpage
    call tbook
    pop iy
    pop ix
    or 1
    ret
; pwork: one piece of the work that waits for time: a page of marked tiles (first, as
; Layer 2 cells read the converted tiles), else one waiting Layer 2 cell, else a row of
; pixel value sets (pmask). NZ: done; Z: none.
pwork:
    call tstep
    ret nz
    ld a,(pq_any)
    or a
    jr z,.m
    call pqone
    ld a,1
    or a
    ret
.m: jp pmask
; tbook: conv_page's bookkeeping (tm_mask, pri_tiles -> pri_redo, tile_slot, sat_dirty) for
; the (page, mask) pairs in tlist up to t_lp, then the game's pages back in slots 0 and 2-5.
tbook:
    nextreg $50,T_FW3
    nextreg $55,T_FW2
    ld ix,tlist
tb_bk:
    ld hl,(t_lp)
    push ix
    pop de
    or a
    sbc hl,de
    jr z,tb_bkd
    ld e,(ix+0)                  ; page
    ld c,(ix+1)                  ; mask
    ld l,e
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl                    ; tm_mask: the page's 8 entries of 2 bytes
    ld a,c
    ld b,8
tb_v: rra
    jr nc,tb_vn
    ld (hl),0
    inc hl
    ld (hl),0
    dec hl
tb_vn:
    inc hl
    inc hl
    djnz tb_v
; (conv_page also sets pri_redo when a converted tile is one Layer 2 holds. Without the
; prichg switch nothing fills pri_chg, so that redraw draws no cell: it is left out here.)
    ld l,e
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    ld de,T_TSLOT
    add hl,de
    ld a,c
    srl a
    and $55
    or c
    ld b,8
tb_d: rra
    jr nc,tb_dn
    ld (hl),0
tb_dn:
    inc hl
    djnz tb_d
    inc ix
    inc ix
    jr tb_bk
tb_bkd:
    ld a,1
    ld (T_SATD),a
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
    ret
; tpage: A = VRAM page (256 bytes, 8 tiles), C = the tile mask: conv_page's conversion.
; Each tile row is read with two POPs (interrupts are off): C, B, E, D = planes 0 to 3.
    MACRO CONVP k       ; the runtime's CONVBYTE (fw.asm), with the planes in C, B, E, D
    ld l,d
    ld a,(hl)
    add a,a
    ld l,e
    or (hl)
    add a,a
    ld l,b
    or (hl)
    add a,a
    ld l,c
    or (hl)
    ld (ix+k),a
    ENDM
tpage:
    ld b,a
    add a,$40
    ld iyh,a
    ld iyl,0
    ld a,b
    add a,$80
    ld ixh,a
    ld ixl,0
    ld a,c
.tile:
    ld (t_m),a
    rra
    jr c,.conv
    ld bc,32
    add ix,bc
    add iy,bc
    jr .next
.conv:
    ld (t_sp),sp
    ld sp,iy
    ld a,8
.row:
    ld (t_n),a
    pop bc
    pop de
    ld h,T_CONV>>8
    CONVP 0
    inc h
    CONVP 1
    inc h
    CONVP 2
    inc h
    CONVP 3
    ld bc,4
    add ix,bc
    ld a,(t_n)
    dec a
    jr nz,.row
    ld iy,0
    add iy,sp
    ld sp,(t_sp)
.next:
    ld a,(t_m)
    srl a
    jr nz,.tile
    ret
t_tab: db 0
t_m:   db 0
t_n:   db 0
t_sp:  dw 0
t_lp:  dw 0
tlist: ds 128
; pdraw: Layer 2 for the cells that name table writes have marked, as the runtime's
; pri_frame marked-cells pass (pri_rowcells, pri_cell, pri_put, pri_tile; fw2.asm) would draw
; them in the next vertical blank, here in the page with interrupts off. Each cell drawn has
; its mark cleared, so the runtime draws it no more. Left to the runtime: everything when the
; priority switch is off, in 224-line mode, with a whole Layer 2 rebuild pending (pri_full),
; or with the name table below VRAM $2000. Runtime internals (build/rt/runtime.map):
;   MAP_PAGE 14 (slot 0 here): row "has priority cells" $1BC0 + row, row "marked" $1BE0 + row,
;     cell marks $1C00 + cell (bit 0 marked, bit 1 Layer 2 holds the cell);
;   L2_PAGE 102-107: Layer 2, 32 lines of 256 bytes a page (slot 3 here);
;   SHADOW_PAGE+1 29 (slot 2), TILE_PAGE 10, 11 (slots 4-5, $8000 + tile * 32);
;   FW2_PAGE 25 (slot 5 at $A000 to copy): pri_full $3469, pri_v $346B, pri_ys $346D,
;     pri_lf $3478 (192 bytes) and pri_tiles $3538 (64 bytes), copied in and back;
;   part 1: nt_base $E04B, m224 $E08F, fw_flags $E09E (bit 0: priority), cur_mmu.
P_MAP     equ 14
P_L2      equ 102
P_FULL    equ $A000+$1469
P_V       equ $A000+$146B
P_YS      equ $A000+$146D
P_LF      equ $A000+$1478       ; pri_lf, then pri_tiles 192 bytes on
P_M224    equ $E08F
P_FLAGS   equ $E09E
P1_NIBM   equ $0400             ; page 1's copy of nibm, in slot 0
pdraw:
    xor a
    ld (pm_row),a                ; the name table changed: pmask's rows again
    ld a,(P_FLAGS)
    rra
    ret nc
    ld a,(P_M224)
    or a
    ret nz
    ld a,(nt_base+1)
    cp $20
    ret c
    ld a,(vdp_regs+1)            ; the display off: the cells wait in pq for the time the
    and $40                      ; Master System spends after the write (pend), or for the
    jr nz,.now                   ; display-on write (don)
    ld a,1
    ld (p_defer),a
    nextreg $50,P_MAP
    call prows
    ld a,(cur_mmu+0)
    nextreg $50,a
    ret
.now:
    xor a
    ld (p_defer),a
    call pq_open
    call z,prows
    jp pq_close
; prows: each marked row (MAP_PAGE in slot 0)
prows:
    ld b,0
.r: ld a,b
    add a,$E0
    ld l,a
    ld h,$1B
    ld a,(hl)
    or a
    jr z,.rn
    ld (hl),0
    push bc
    call prow
    pop bc
.rn:
    inc b
    ld a,b
    cp 28
    jr nz,.r
    ret
; pq_open: the Layer 2 state in, the pages mapped; NZ (and nothing mapped but FW2) when a
; whole rebuild is pending. pq_close: the state back, the game's pages back.
pq_open:
    ld a,1
    ld (pq_op),a
    nextreg $55,T_FW2
    ld a,(P_FULL)
    or a
    ret nz
    ld a,(P_V)
    ld (p_v),a
    ld a,(P_YS)
    ld (p_ys),a
    ld hl,P_LF
    ld de,p_lf
    ld bc,256
    ldir
    nextreg $50,P_MAP
    nextreg $52,T_SHADOW+1
    nextreg $54,T_TILES
    nextreg $55,T_TILES+1
    ld a,$FF
    ld (p_pg),a
    xor a
    ret
pq_close:
    ld a,(pq_op)
    or a
    ret z
    xor a
    ld (pq_op),a
    nextreg $55,T_FW2
    ld a,(P_FULL)
    or a
    jr nz,.back
    ld hl,p_lf
    ld de,P_LF
    ld bc,256
    ldir
.back:
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
    ret
; pqone: the waiting cells of one byte of pq (up to 8; one with pq_one set) drawn (pq_open
; first). A whole rebuild pending: the list dropped.
pqone:
    push af
    push bc
    push de
    push hl
    ld a,(pq_op)
    or a
    jr nz,.o
    call pq_open
    jr z,.o
    ld hl,pq                     ; the rebuild draws them all
    ld b,112
.c: ld (hl),0
    inc hl
    djnz .c
    xor a
    ld (pq_any),a
    jr .x
.o: ld a,(pq_pos)                ; from the byte of the last cell found
    ld c,a
    ld hl,pq
    add hl,a
.f: ld a,(hl)
    or a
    jr nz,.g
    inc hl
    inc c
    ld a,c
    cp 112
    jr nz,.f
    xor a
    ld (pq_pos),a
    ld (pq_any),a
    jr .x
.g: ld b,0                       ; B = the lowest bit set, E = its mask
    ld e,1
.h: rrca
    jr c,.k
    inc b
    sla e
    jr .h
.k: ld a,c
    ld (pq_pos),a
    ld a,e
    cpl
    and (hl)
    ld (hl),a
    ld l,c                       ; cell = 8 C + B
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,b
    add hl,a
    ld a,l
    and 31
    ld (p_c),a
    push hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,h                       ; row = cell >> 5
    ld (p_r),a
    pop hl
    ld de,$1C00
    add hl,de
    call pcell
    ld a,(pq_one)                ; don: one cell a step
    or a
    jr nz,.x
    ld a,(pq_pos)                ; the byte's other cells in the same step
    ld c,a
    ld hl,pq
    add hl,a
    ld a,(hl)
    or a
    jr nz,.g
.x: pop hl
    pop de
    pop bc
    pop af
    ret
; don: the display-on routine at $029A (IN A,($BF); EI; LD A,1; CALL $00B9, the wait for the
; next frame interrupt). The Master System waits there; the waiting work (pwork) is done in
; that time, up to D_STOP lines before the frame event (the line interrupt at Next line 193,
; the end of picture line 192: the runtime's ev_program and pic_end), so that no step runs
; into it. Then the routine's own work. What is left is done by don2 after the wait. Keeps
; BC, DE, HL.
D_STOP   equ 193-28              ; a step takes at most about 20 lines (a page of tiles)
don:
    di                           ; slot 0 holds MAP_PAGE while cells are drawn
    push bc
    push de
    push hl
    ld a,1
    ld (pq_one),a
.d: call pline
    ld de,D_STOP
    or a
    sbc hl,de
    jr c,.go                     ; before D_STOP
    ld de,193+2-D_STOP
    sbc hl,de                    ; (carry clear)
    jr c,.e                      ; D_STOP to 194: the frame event is near or now
.go:
    call pwork
    jr nz,.d
.e: call pq_close
    xor a
    ld (pq_one),a
    pop hl
    pop de
    pop bc
    rst $00
    db $0D                       ; IN A,($BF)
    ei
    ld a,1
    ret
; don2: at $02A2 in the display-on routine, after its frame wait: the tiles and Layer 2 cells
; still waiting, then the replaced LD A,($DFE1); OR $40. Keeps the interrupt state and BC,
; DE, HL.
don2:
    push bc
    push de
    push hl
    ld a,i
    push af
    di
.d: call tstep                   ; tiles, then cells: what the picture needs (no pmask here,
    jr nz,.d                     ; that waits for the time pal_scan leaves)
    ld a,(pq_any)
    or a
    jr z,.e
    call pqone
    jr .d
.e: call pq_close
    pop af
    jp po,.n
    ei
.n: pop hl
    pop de
    pop bc
    ld a,($DFE1)
    or $40
    ret
p_defer: db 0
pq_op:   db 0
pq_any:  db 0
pq_one:  db 0
pq_pos:  db 0
pq:      ds 112
; prow: B = row: each marked cell (pri_rowcells)
prow:
    ld a,b
    ld (p_r),a
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
.c: bit 0,(hl)
    jr z,.n
    res 0,(hl)
    push hl
    push bc
    ld a,c
    ld (p_c),a
    ld a,(p_defer)
    or a
    jr nz,.q
    call pcell
    jr .qn
.q: ld a,(p_r)                   ; into pq: bit (cell & 7) of byte cell >> 3
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,c
    add hl,a
    ld a,l
    and 7
    ld b,a
    srl h
    rr l
    srl h
    rr l
    srl h
    rr l
    ld de,pq
    add hl,de
    ld a,1
    inc b
    dec b
    jr z,.qb
.qs:
    add a,a
    djnz .qs
.qb:
    or (hl)
    ld (hl),a
    ld a,1
    ld (pq_any),a
    xor a
    ld (pq_pos),a
.qn:
    pop bc
    pop hl
.n: inc hl
    inc c
    ld a,c
    cp 32
    jr nz,.c
    ret
; pcell: cell (p_r, p_c), HL = its mark (pri_cell)
pcell:
    push hl
    ld a,(p_r)                   ; the entry in the copy: nt_base + 64 r + 2 c, at + $2000
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,(p_c)
    add a,a
    add hl,a
    ld de,(nt_base)
    add hl,de
    ld a,h
    add a,$20
    ld h,a
    ld a,(hl)
    ld (p_tl),a
    inc hl
    ld a,(hl)
    ld (p_th),a
    pop hl
    and $10
    jr nz,.p
    bit 1,(hl)
    ret z                        ; Layer 2 holds nothing of it
    res 1,(hl)
    jp .lines
.p: set 1,(hl)
    ld a,(p_tl)                  ; pri_tiles: byte (tile >> 3), bit (tile & 7)
    rrca
    rrca
    rrca
    and $1F
    ld e,a
    ld a,(p_th)
    and 1
    rrca
    rrca
    rrca
    or e
    ld hl,p_lf+192
    add hl,a
    ld a,(p_tl)
    and 7
    ld b,a
    ld a,1
    jr z,.b0
.bs:
    add a,a
    djnz .bs
.b0:
    or (hl)
    ld (hl),a
; the cell's pixels: per line the Layer 2 line, then 8 bytes from the tile row
    ld a,(p_th)
    and 1
    ld h,a
    ld a,(p_tl)
    ld l,a
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,h
    add a,$80
    ld h,a                       ; the tile in the definitions
    ld a,(p_th)
    ld b,a
    ld de,4
    bit 2,b                      ; V flip: from the last row up
    jr z,.nv
    ld de,28
    add hl,de
    ld de,-4
.nv:
    ld (p_src),hl
    ld (p_step),de
    ld a,b
    and 8
    add a,a
    ld (p_pal),a                 ; $10: the sprite palette
    ld a,b
    and 2
    ld (p_hf),a
    ld a,(p_c)
    add a,a
    add a,a
    add a,a
    ld (p_x),a
    ld a,(p_r)
    add a,a
    add a,a
    add a,a
    ld hl,p_v
    sub (hl)
    jr nc,.y0
    add a,224
.y0:
    cp 192-7                     ; the fast form: all 8 lines in the picture, in one Layer 2
    jr nc,.sl                    ; page, no wrap of the 192-line ring
    ld e,a
    ld hl,p_ys
    add a,(hl)
    jr c,.w0
    cp 192
    jr c,.n0
.w0:
    sub 192
.n0:
    cp 192-7
    jr nc,.sl0
    ld d,a                       ; D = the first Layer 2 line
    and $1F
    cp 32-7
    jp c,fcell
.sl0:
    ld a,e
.sl:
    ld b,8
.ln:
    push bc
    ld (p_y),a
    cp 192
    jp nc,.sk
    ld hl,p_ys
    add a,(hl)
    jr c,.wr
    cp 192
    jr c,.ok
.wr:
    sub 192
.ok:
    ld e,a                       ; the Layer 2 line
    ld hl,p_lf
    add hl,a
    ld (hl),1
    ld a,e
    rlca
    rlca
    rlca
    and 7
    add a,P_L2
    ld hl,p_pg
    cp (hl)
    jr z,.sp
    ld (hl),a
    nextreg $53,a
.sp:
    ld a,e
    and $1F
    or $60
    ld d,a
    ld a,(p_x)
    ld e,a
    ld hl,(p_src)
    ld a,(p_pal)
    ld c,a
    ld a,(p_hf)
    or a
    jr nz,.hf
    REPT 4
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
    ENDR
    jr .sk
.hf:
    inc hl
    inc hl
    inc hl
    REPT 4
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
    ENDR
.sk:
    ld hl,(p_src)
    ld de,(p_step)
    add hl,de
    ld (p_src),hl
    ld a,(p_y)
    inc a
    cp 224
    jr c,.yy
    xor a
.yy:
    pop bc
    dec b
    jp nz,.ln
    ret
.lines:
    ld a,(p_r)                   ; the fast form, as fcell: 8 lines of zeros in one page
    add a,a
    add a,a
    add a,a
    ld hl,p_v
    sub (hl)
    jr nc,.ly
    add a,224
.ly:
    cp 192-7
    jr nc,.ls
    ld hl,p_ys
    add a,(hl)
    jr c,.lw
    cp 192
    jr c,.l0
.lw:
    sub 192
.l0:
    cp 192-7
    jr nc,.ls
    ld d,a
    and $1F
    cp 32-7
    jr nc,.ls
    ld a,d
    rlca
    rlca
    rlca
    and 7
    add a,P_L2
    ld (p_pg),a
    nextreg $53,a
    ld a,d
    and $1F
    or $60
    ld d,a
    ld a,(p_c)
    add a,a
    add a,a
    add a,a
    ld e,a
    ld c,a
    xor a
    ld b,8
.lz:
    REPT 8
    ld (de),a
    inc e
    ENDR
    ld e,c
    inc d
    djnz .lz
    ret
.ls:
    ld a,(p_r)
    add a,a
    add a,a
    add a,a
    ld e,a                       ; map line of the cell's top
    ld d,0                       ; line in the cell
.k: ld a,e
    add a,d
    ld hl,p_v
    sub (hl)
    jr nc,.y
    add a,224
.y: cp 192
    jr nc,.nx
    ld hl,p_ys
    add a,(hl)
    jr c,.w
    cp 192
    jr c,.l
.w: sub 192
.l: ld (p_l),a                   ; Layer 2 line
    push de
    ld hl,p_lf
    add hl,a
.clr:
    ld a,(hl)
    or a
    call nz,pzero
.nd:
    pop de
.nx:
    inc d
    ld a,d
    cp 8
    jr nz,.k
    ret
; fcell: pcell's 8 lines at once, D = the first Layer 2 line (the lines D to D + 7 lie in
; one Layer 2 page and in the picture): the lines' pri_lf flags, the page mapped once, then
; each line's 8 pixels from the tile row (p_src, p_th flips, p_pal palette) through the
; tables of page 1, mapped in slot 0 meanwhile: per byte, the high then the low pixel with
; the palette bit. Keeps IX.
fcell:
    push ix
    ld h,p_lf>>8                 ; p_lf is 256-aligned
    ld l,d
    ld b,8
.lf:
    ld (hl),1
    inc l
    djnz .lf
    ld a,d
    rlca
    rlca
    rlca
    and 7
    add a,P_L2
    ld (p_pg),a
    nextreg $53,a
    ld a,d
    and $1F
    or $60
    ld d,a
    ld a,(p_x)
    ld e,a
    call p1get
    nextreg $50,a                ; the tables at $0000
    ld a,(p_pal)                 ; $00 or $10 -> table pair $00 or $02
    rrca
    rrca
    rrca
    ld b,a
    ld ixl,8
    ld hl,(p_src)                ; the tile row (the definitions are 32-byte aligned: INC L)
    ld a,(p_th)
    bit 1,a
    jr nz,.hf
    and 4                        ; V flip: from the row after to the row before
    ld a,0
    jr z,.v0
    ld a,-8
.v0:
    ld ixh,a
.fl:
    REPT 4
    ld c,(hl)
    ld a,(bc)
    ld (de),a
    inc e
    inc b
    ld a,(bc)
    ld (de),a
    inc e
    dec b
    inc l
    ENDR
    ld a,l
    add a,ixh
    ld l,a
    inc d
    ld a,e
    sub 8
    ld e,a
    dec ixl
    jr nz,.fl
    jr .x
.hf:
    and 4
    ld a,5
    jr z,.v1
    ld a,5-8
.v1:
    ld ixh,a
    inc l
    inc l
    inc l
.fh:
    REPT 4
    ld c,(hl)
    inc b
    ld a,(bc)
    ld (de),a
    inc e
    dec b
    ld a,(bc)
    ld (de),a
    inc e
    dec l
    ENDR
    ld a,l
    add a,ixh
    ld l,a
    inc d
    ld a,e
    sub 8
    ld e,a
    dec ixl
    jr nz,.fh
.x: nextreg $50,P_MAP
    pop ix
    ret
; pdest: DE = the cell's 8 bytes on Layer 2 line p_l (its page in slot 3)
pdest:
    ld a,(p_l)
    rlca
    rlca
    rlca
    and 7
    add a,P_L2
    ld hl,p_pg
    cp (hl)
    jr z,.s
    ld (hl),a
    nextreg $53,a
.s: ld a,(p_l)
    and $1F
    or $60
    ld d,a
    ld a,(p_c)
    add a,a
    add a,a
    add a,a
    ld e,a
    ret
pzero:
    call pdest
    xor a
    ld b,8
.z: ld (de),a
    inc e
    djnz .z
    ret
p_v:  db 0
p_y:  db 0
p_pal: db 0
p_hf: db 0
p_x:  db 0
p_src: dw 0
p_step: dw 0
p_ys: db 0
p_pg: db 0
p_r:  db 0
p_c:  db 0
p_l:  db 0
p_k:  db 0
p_tl: db 0
p_th: db 0
v_a:    db 0
v_ei:   db 0
r_attr: db 0
r_ei:   db 0
r_rows: db 0
r_all:  db 0
r_hl:   dw 0
r_de:   dw 0
r_bc:   dw 0
r_v:    dw 0
r_row:  dw 0
r_src:  dw 0
r_hp:   dw 0
r_dp:   dw 0
n_hi:  dw 0
    ALIGN 256
img:   ds 256                 ; a rectangle row, a status bar run, a tile, vclr's 256 bytes
obuf   equ img                ; lz's output buffer (lz never runs with rect, vclr, ldt)
p_lf:  ds 256                 ; pri_lf and pri_tiles while Layer 2 cells are drawn
    ASSERT $ <= $4000
endpage
# Code page 1: tables for page 0, mapped by it into slot 0 ($0000): $0000 the high pixel of a
# tile byte, $0100 the low pixel, $0200 and $0300 the same with the sprite palette bit ($10);
# $0400 and $0500 the runtime's nibm (the set of a byte's two pixel values, low then high
# bytes). Entry p1no gives page 0 this page's RAM page.
page 1 p1no
P1T:
    DUP 256, x
    db x >> 4
    EDUP
    DUP 256, x
    db x & 15
    EDUP
    DUP 256, x
    db (x >> 4) | $10
    EDUP
    DUP 256, x
    db (x & 15) | $10
    EDUP
    DUP 256, x
    db low((1 << (x >> 4)) | (1 << (x & 15)))
    EDUP
    DUP 256, x
    db high((1 << (x >> 4)) | (1 << (x & 15)))
    EDUP
; p1no: A = this page's RAM page (the far call put it in cur_mmu+1)
p1no:
    ld a,(cur_mmu+1)
    ret
endpage
