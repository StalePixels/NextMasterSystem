# Super Kick Off (Europe, Brazil) (En,Fr,De,Es,It,Nl,Pt,Sv), CRC32 406AA0C2, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output with the reference logs, then decided by hand.
#
# Decisions:
# - No free RST vector ($0008-$0029 are the power-on code, $002A-$0037 hold bytes that are not
#   code): $0000-$0002 (DI; IM 1) becomes the io vector, and the game starts at $0003. The
#   game has no RST $00 of its own.
# - The game switches slot 1 between banks 1, 4 and 8, so the scan cannot name the bank of
#   its calls into slot 1. The bank 1 and bank 4 sites come from a reference I/O log of a
#   practice match, with banks, and the bank 4 sites $49F7, $4A4A, $4ED2-$4EDB from the 60 s
#   sweep log, scanned as entry points.
# - $018F counts loop passes in one frame to tell a 50 Hz machine from a 60 Hz one and keeps
#   the result in $D516 (0: 50 Hz). It repeats the test until the count is in a Master
#   System's range, so on the faster CPU it never ends. The test's end at $01A6 sets the
#   50 Hz value.
# - The map column writer $11F6-$1227 points SP at its table of name table row addresses
#   ($1228) with interrupts off and reads it with POP HL. A patched OUT there pushes its
#   return address into the table, and the cart is in RAM on the Next, so the table is
#   overwritten and later columns go to wrong VRAM addresses. Page 0 (mapcol) does the
#   column's writes with jt_vwrite and no stack in the table.
# - The copy loop of $0BBE (BC bytes from DE to VRAM, the address already set) goes to page 0
#   (vcopy), which writes 256 bytes at a time through jt_vwrite. Through the runtime's trace
#   form it took about 3,400,000 cycles for the 8K of match tiles ($101F) and 510,000 for
#   tiles loaded in play, which put play frames at 160%.
# - $001E, $0021 and $0026 (LD (HL),A to $FFFC, $FFFD and $FFFF at power-on) are not patched:
#   they write $80, $00 and $02, the mapping the runtime starts the game with, and the RAM
#   bytes there get the values, as on a Master System.
# - priority: the column and row writers give map tiles $C7 and up (the goal and its net) the
#   priority bit, and the net covers the players and the score sprites, as on a Master System.
# - Bank 3 is the sound driver, called from the line interrupt ($01C4).
# - Unreached code that the byte scan finds is patched as code: the silence routine $805A
#   (bank 3), the RAM form of the graphics unpacker $42A9 and the cell copier $633F (bank 4).
# - The NMI handler at $0066 reads port $0E; a value of 4 there would jump to $DF20 in RAM, a
#   development hook that a Master System never takes.
name Super Kick Off
cart 406AA0C2
vector 00 io
start 0003
hz 50		; No-Intro regions Europe, Brazil
priority	; the goal net (map tiles $C7 and up) covers the players and the score
asm 001A6 7   ; DI; LD A,B; CP $0D; JP NC,$018F: the end of the speed test at $018F
    di
    xor a         ; $D516 = 0, the 50 Hz value
    jp $01C0
endasm
asm 00BC2 10   ; LD A,(DE); OUT ($BE),A; INC DE; DEC BC; LD A,B; OR C; JR NZ; RET: the copy loop of $0BBE
    rst $00     ; BC bytes from DE to VRAM, through jt_vwrite (page 0)
    db far_io, pg_vcopy, ent_vcopy
    ret
endasm
asm 011F6 7   ; DI; LD ($C5B5),SP; LD SP,HL; LD C,A: the map column writer, which reads its
    rst $00     ; table of row addresses with POP HL; on the Next the cart is in RAM, so the
    db far_io, pg_mapcol, ent_mapcol   ; I/O RST pushes over the table (page 0)
    jp $1221    ; EI; slot 1 back to bank 1; RET
endasm
site 0000E   ; OUT ($3E),A
site 00039   ; IN A,($BF)
site 00067   ; IN A,($0E)
site 00BAF   ; OUT ($BE),A
site 00BB7   ; OUT ($BE),A
site 00BCF   ; IN A,($BE)
site 00BDD   ; OUT ($BF),A
site 00BE3   ; OUT ($BF),A
site 00BF7   ; OUT ($BF),A
site 00BFF   ; OUT ($BF),A
site 00C08   ; OUT ($BE),A
site 00C11   ; OUT ($BF),A
site 00C15   ; OUT ($BF),A
site 00C1B   ; OUT ($BE),A
site 00C72   ; OUT ($3F),A
site 00C74   ; IN A,($DC)
site 00CE6   ; OUT ($3F),A
site 00CE8   ; IN A,($DC)
site 00CF3   ; OUT ($3F),A
site 00CF5   ; IN A,($DD)
site 00D40   ; IN A,($DD)
site 00D63   ; IN A,($DD)
site 00D88   ; OTIR
site 00D9E   ; OUT ($BF),A
site 00DA8   ; OUT ($BF),A
site 00DB5   ; OUT ($BE),A
site 0107C   ; OUT ($BE),A
site 01082   ; OUT ($BE),A
site 01202   ; OUT ($BF),A
site 01207   ; OUT ($BF),A
site 0120B   ; OUT ($BE),A
site 01219   ; OUT ($BE),A
site 012E0   ; OUT ($BF),A
site 012E5   ; OUT ($BF),A
site 012FB   ; OUT ($BE),A
site 01308   ; OUT ($BE),A
site 01311   ; OUT ($BF),A
site 01316   ; OUT ($BF),A
site 0131A   ; OUT ($BE),A
site 01327   ; OUT ($BE),A
site 029BA   ; OUT ($BF),A
site 029C1   ; OUT ($BF),A
site 029C7   ; OUT ($BE),A
site 029E1   ; OUT ($BF),A
site 029E8   ; OUT ($BF),A
site 029EE   ; OUT ($BE),A
site 05D4B   ; OUT ($BF),A
site 05D4F   ; OUT ($BF),A
site 05D59   ; OUTI
site 05D5B   ; OUTI
site 05D5D   ; OUTI
site 05D5F   ; OUTI
site 05D61   ; OUTI
site 05D63   ; OUTI
site 05D65   ; OUTI
site 05D67   ; OUTI
site 05D69   ; OUTI
site 05D6B   ; OUTI
site 05D6D   ; OUTI
site 05D6F   ; OUTI
site 05D71   ; OUTI
site 05D73   ; OUTI
site 05D75   ; OUTI
site 05D77   ; OUTI
site 05D79   ; OUTI
site 05D7B   ; OUTI
site 05D7D   ; OUTI
site 05D7F   ; OUTI
site 05D81   ; OUTI
site 05D83   ; OUTI
site 05D85   ; OUTI
site 05D87   ; OUTI
site 05D89   ; OUTI
site 05D8B   ; OUTI
site 05D8D   ; OUTI
site 05D8F   ; OUTI
site 05D91   ; OUTI
site 05D93   ; OUTI
site 05D95   ; OUTI
site 05D97   ; OUTI
site 05D99   ; OUTI
site 05D9B   ; OUTI
site 05D9D   ; OUTI
site 05D9F   ; OUTI
site 05DA1   ; OUTI
site 05DA3   ; OUTI
site 05DA5   ; OUTI
site 05DA7   ; OUTI
site 05DA9   ; OUTI
site 05DAB   ; OUTI
site 05DAD   ; OUTI
site 05DAF   ; OUTI
site 05DB1   ; OUTI
site 05DB3   ; OUTI
site 05DB5   ; OUTI
site 05DB7   ; OUTI
site 05DB9   ; OUTI
site 05DBB   ; OUTI
site 05DBD   ; OUTI
site 05DBF   ; OUTI
site 05DC3   ; OUT ($BF),A
site 05DC6   ; OUT ($BF),A
site 05DCC   ; OUTI
site 05DCE   ; OUTI
site 05DD0   ; OUTI
site 05DD2   ; OUTI
site 05DD4   ; OUTI
site 05DD6   ; OUTI
site 05DD8   ; OUTI
site 05DDA   ; OUTI
site 05DDC   ; OUTI
site 05DDE   ; OUTI
site 05DE0   ; OUTI
site 05DE2   ; OUTI
site 05DE4   ; OUTI
site 05DE6   ; OUTI
site 05DE8   ; OUTI
site 05DEA   ; OUTI
site 05DEC   ; OUTI
site 05DEE   ; OUTI
site 05DF0   ; OUTI
site 05DF2   ; OUTI
site 05DF4   ; OUTI
site 05DF6   ; OUTI
site 05DF8   ; OUTI
site 05DFA   ; OUTI
site 05DFC   ; OUTI
site 05DFE   ; OUTI
site 05E00   ; OUTI
site 05E02   ; OUTI
site 05E04   ; OUTI
site 05E06   ; OUTI
site 05E08   ; OUTI
site 05E0A   ; OUTI
site 05E0C   ; OUTI
site 05E0E   ; OUTI
site 05E10   ; OUTI
site 05E12   ; OUTI
site 05E14   ; OUTI
site 05E16   ; OUTI
site 05E18   ; OUTI
site 05E1A   ; OUTI
site 05E1C   ; OUTI
site 05E1E   ; OUTI
site 05E20   ; OUTI
site 05E22   ; OUTI
site 05E24   ; OUTI
site 05E26   ; OUTI
site 05E28   ; OUTI
site 05E2A   ; OUTI
site 05E2C   ; OUTI
site 05E2E   ; OUTI
site 05E30   ; OUTI
site 05E32   ; OUTI
site 05E34   ; OUTI
site 05E36   ; OUTI
site 05E38   ; OUTI
site 05E3A   ; OUTI
site 05E3C   ; OUTI
site 05E3E   ; OUTI
site 05E40   ; OUTI
site 05E42   ; OUTI
site 05E44   ; OUTI
site 05E46   ; OUTI
site 05E48   ; OUTI
site 05E4A   ; OUTI
site 05E4C   ; OUTI
site 05E4E   ; OUTI
site 05E50   ; OUTI
site 05E52   ; OUTI
site 05E54   ; OUTI
site 05E56   ; OUTI
site 05E58   ; OUTI
site 05E5A   ; OUTI
site 05E5C   ; OUTI
site 05E5E   ; OUTI
site 05E60   ; OUTI
site 05E62   ; OUTI
site 05E64   ; OUTI
site 05E66   ; OUTI
site 05E68   ; OUTI
site 05E6A   ; OUTI
site 05E6C   ; OUTI
site 05E6E   ; OUTI
site 05E70   ; OUTI
site 05E72   ; OUTI
site 05E74   ; OUTI
site 05E76   ; OUTI
site 05E78   ; OUTI
site 05E7A   ; OUTI
site 05E7C   ; OUTI
site 05E7E   ; OUTI
site 05E80   ; OUTI
site 05E82   ; OUTI
site 05E84   ; OUTI
site 05E86   ; OUTI
site 05E88   ; OUTI
site 05E8A   ; OUTI
site 05E8C   ; OUTI
site 05E8E   ; OUTI
site 05E90   ; OUTI
site 05E92   ; OUTI
site 05E94   ; OUTI
site 05E96   ; OUTI
site 05FCE   ; OUT ($BF),A
site 05FD1   ; OUT ($BF),A
site 05FD4   ; OUTI
site 05FD6   ; OUTI
site 05FD8   ; OUTI
site 05FDA   ; OUTI
site 05FDC   ; OUTI
site 05FDE   ; OUTI
site 05FE0   ; OUTI
site 05FE2   ; OUTI
site 05FE4   ; OUTI
site 05FE6   ; OUTI
site 05FE8   ; OUTI
site 05FEA   ; OUTI
site 05FEC   ; OUTI
site 05FEE   ; OUTI
site 05FF0   ; OUTI
site 05FF2   ; OUTI
site 05FF4   ; OUTI
site 05FF6   ; OUTI
site 05FF8   ; OUTI
site 05FFA   ; OUTI
site 05FFC   ; OUTI
site 05FFE   ; OUTI
site 06000   ; OUTI
site 06002   ; OUTI
site 06004   ; OUTI
site 06006   ; OUTI
site 06008   ; OUTI
site 0600A   ; OUTI
site 0600C   ; OUTI
site 0600E   ; OUTI
site 06010   ; OUTI
site 06012   ; OUTI
site 06014   ; OUTI
site 06016   ; OUTI
site 06018   ; OUTI
site 0601A   ; OUTI
site 0601C   ; OUTI
site 0601E   ; OUTI
site 06020   ; OUTI
site 06022   ; OUTI
site 06024   ; OUTI
site 06026   ; OUTI
site 06028   ; OUTI
site 0602A   ; OUTI
site 0602C   ; OUTI
site 0602E   ; OUTI
site 06030   ; OUTI
site 06032   ; OUTI
site 06034   ; OUTI
site 06036   ; OUTI
site 06038   ; OUTI
site 0603A   ; OUTI
site 0603C   ; OUTI
site 0603E   ; OUTI
site 06040   ; OUTI
site 06042   ; OUTI
site 06044   ; OUTI
site 06046   ; OUTI
site 06048   ; OUTI
site 0604A   ; OUTI
site 0604C   ; OUTI
site 0604E   ; OUTI
site 06050   ; OUTI
site 06052   ; OUTI
site 06054   ; OUTI
site 06056   ; OUTI
site 06058   ; OUTI
site 0605A   ; OUTI
site 0605C   ; OUTI
site 0605E   ; OUTI
site 06060   ; OUTI
site 06062   ; OUTI
site 06064   ; OUTI
site 06066   ; OUTI
site 06068   ; OUTI
site 0606A   ; OUTI
site 0606C   ; OUTI
site 0606E   ; OUTI
site 06070   ; OUTI
site 06072   ; OUTI
site 06074   ; OUTI
site 06076   ; OUTI
site 06078   ; OUTI
site 0607A   ; OUTI
site 0607C   ; OUTI
site 0607E   ; OUTI
site 06080   ; OUTI
site 06082   ; OUTI
site 06084   ; OUTI
site 06086   ; OUTI
site 06088   ; OUTI
site 0608A   ; OUTI
site 0608C   ; OUTI
site 0608E   ; OUTI
site 06090   ; OUTI
site 06092   ; OUTI
site 06094   ; OUTI
site 06096   ; OUTI
site 06098   ; OUTI
site 0609A   ; OUTI
site 0609C   ; OUTI
site 0609E   ; OUTI
site 060A0   ; OUTI
site 060A2   ; OUTI
site 060A4   ; OUTI
site 060A6   ; OUTI
site 060A8   ; OUTI
site 060AA   ; OUTI
site 060AC   ; OUTI
site 060AE   ; OUTI
site 060B0   ; OUTI
site 060B2   ; OUTI
site 060B4   ; OUTI
site 060B6   ; OUTI
site 060B8   ; OUTI
site 060BA   ; OUTI
site 060BC   ; OUTI
site 060BE   ; OUTI
site 060C0   ; OUTI
site 060C2   ; OUTI
site 060C4   ; OUTI
site 060C6   ; OUTI
site 060C8   ; OUTI
site 060CA   ; OUTI
site 060CC   ; OUTI
site 060CE   ; OUTI
site 060D0   ; OUTI
site 060D2   ; OUTI
site 06104   ; OUT ($BF),A
site 06107   ; OUT ($BF),A
site 0610A   ; OUTI
site 0610C   ; OUTI
site 0610E   ; OUTI
site 06110   ; OUTI
site 06112   ; OUTI
site 06114   ; OUTI
site 06116   ; OUTI
site 06118   ; OUTI
site 0611A   ; OUTI
site 0611C   ; OUTI
site 0611E   ; OUTI
site 06120   ; OUTI
site 06122   ; OUTI
site 06124   ; OUTI
site 06126   ; OUTI
site 06128   ; OUTI
site 0612A   ; OUTI
site 0612C   ; OUTI
site 0612E   ; OUTI
site 06130   ; OUTI
site 06132   ; OUTI
site 06134   ; OUTI
site 06136   ; OUTI
site 06138   ; OUTI
site 0613A   ; OUTI
site 0613C   ; OUTI
site 0613E   ; OUTI
site 06140   ; OUTI
site 06142   ; OUTI
site 06144   ; OUTI
site 06146   ; OUTI
site 06148   ; OUTI
site 061B3   ; OUT ($BF),A
site 061B6   ; OUT ($BF),A
site 061B9   ; OUTI
site 061BB   ; OUTI
site 061BD   ; OUTI
site 061BF   ; OUTI
site 061C1   ; OUTI
site 061C3   ; OUTI
site 061C5   ; OUTI
site 061C7   ; OUTI
site 061C9   ; OUTI
site 061CB   ; OUTI
site 061CD   ; OUTI
site 061CF   ; OUTI
site 061D1   ; OUTI
site 061D3   ; OUTI
site 061D5   ; OUTI
site 061D7   ; OUTI
site 061D9   ; OUTI
site 061DB   ; OUTI
site 061DD   ; OUTI
site 061DF   ; OUTI
site 061E1   ; OUTI
site 061E3   ; OUTI
site 061E5   ; OUTI
site 061E7   ; OUTI
site 061E9   ; OUTI
site 061EB   ; OUTI
site 061ED   ; OUTI
site 061EF   ; OUTI
site 061F1   ; OUTI
site 061F3   ; OUTI
site 061F5   ; OUTI
site 061F7   ; OUTI
site 06C9E   ; IN A,($BE)
site 06CA5   ; IN A,($BE)
site 06CD9   ; OUT ($BE),A
site 06CDF   ; OUT ($BE),A
site 06D52   ; IN A,($BE)
site 06D59   ; IN A,($BE)
site 06D88   ; OUT ($BE),A
site 06D90   ; OUT ($BE),A
site 06E23   ; OUT ($BE),A
site 06E2A   ; OUT ($BE),A
site 0C057   ; OTIR
site 0C3E6   ; OUT ($7F),A
site 0C3EC   ; OUT ($7F),A
site 0C3F7   ; OUT ($7F),A
site 0C3FE   ; OUT ($7F),A
site 0C406   ; OUT ($7F),A
site 0C5E6   ; OUT ($7F),A
site 0C5EA   ; OUT ($7F),A
site 101A6   ; OUT ($BE),A
site 101AB   ; OUT ($BE),A
site 101B0   ; OUT ($BE),A
site 101B5   ; OUT ($BE),A
site 1021C   ; OUT ($BE),A
site 10223   ; OUT ($BE),A
site 10228   ; OUT ($BE),A
site 10235   ; OUT ($BE),A
site 10248   ; OUT ($BE),A
site 1027C   ; OUT ($BE),A
site 10283   ; OUT ($BE),A
site 104A5   ; OUT ($BF),A
site 104A9   ; OUT ($BF),A
site 104AD   ; OUT ($BF),A
site 104B1   ; OUT ($BF),A
site 109F7   ; OUT ($BE),A
site 10A4A   ; OUT ($BE),A
site 10EAF   ; OUT ($BE),A
site 10ED2   ; OUT ($BF),A
site 10ED6   ; OUT ($BF),A
site 10EDB   ; OUT ($BE),A
site 11E16   ; OUT ($BE),A
site 11E1D   ; OUT ($BE),A
site 11E48   ; OUT ($BE),A
site 11E4F   ; OUT ($BE),A
site 122F9   ; IN A,($BE)
site 12300   ; IN A,($BE)
site 12315   ; OUT ($BE),A
site 1231C   ; OUT ($BE),A
site 124C6   ; IN A,($BE)
site 124CC   ; IN A,($BE)
site 127D2   ; OUT ($BE),A
site 127D8   ; OUT ($BE),A
site 127EC   ; IN A,($BE)
site 127F2   ; IN A,($BE)
site 128B7   ; OUT ($BE),A
site 128BD   ; OUT ($BE),A
site 128D3   ; IN A,($BE)
site 128D9   ; IN A,($BE)
site 129A4   ; OUT ($BE),A
site 129AA   ; OUT ($BE),A
site 129C0   ; IN A,($BE)
site 129C6   ; IN A,($BE)
site 12A91   ; OUT ($BE),A
site 12A97   ; OUT ($BE),A
site 12B61   ; IN A,($BE)
site 12B69   ; IN A,($BE)
site 12B76   ; OUT ($BE),A
site 12B7E   ; OUT ($BE),A
site 12BB7   ; IN A,($BE)
mapst 0012C   ; LD ($FFFE),A
mapst 00131   ; LD ($FFFE),A
mapst 001CB   ; LD ($FFFF),A
mapst 001D2   ; LD ($FFFF),A
mapst 001DE   ; LD ($FFFF),A
mapst 001E6   ; LD ($FFFF),A
mapst 001F1   ; LD ($FFFF),A
mapst 001F9   ; LD ($FFFF),A
mapst 00204   ; LD ($FFFF),A
mapst 0020B   ; LD ($FFFF),A
mapst 00217   ; LD ($FFFF),A
mapst 0021E   ; LD ($FFFF),A
mapst 002F6   ; LD ($FFFE),A
mapst 00504   ; LD ($FFFF),A
mapst 00586   ; LD ($FFFF),A
mapst 005AF   ; LD ($FFFF),A
mapst 005E4   ; LD ($FFFF),A
mapst 005EF   ; LD ($FFFF),A
mapst 00622   ; LD ($FFFF),A
mapst 006AC   ; LD ($FFFF),A
mapst 00743   ; LD ($FFFF),A
mapst 00CB4   ; LD ($FFFF),A
mapst 00CC9   ; LD ($FFFF),A
mapst 01030   ; LD ($FFFF),A
mapst 01041   ; LD ($FFFE),A
mapst 01045   ; LD ($FFFF),A
mapst 010AB   ; LD ($FFFE),A
mapst 0119B   ; LD ($FFFE),A
mapst 0119F   ; LD ($FFFF),A
mapst 01224   ; LD ($FFFE),A
mapst 0129A   ; LD ($FFFE),A
mapst 0129E   ; LD ($FFFF),A
mapst 0132D   ; LD ($FFFE),A
mapst 018B2   ; LD ($FFFE),A
mapst 018BE   ; LD ($FFFF),A
mapst 018C6   ; LD ($FFFF),A
mapst 018CE   ; LD ($FFFF),A
mapst 018DF   ; LD ($FFFF),A
mapst 018F9   ; LD ($FFFF),A
mapst 01904   ; LD ($FFFF),A
mapst 01918   ; LD ($FFFF),A
mapst 01933   ; LD ($FFFF),A
mapst 0193E   ; LD ($FFFF),A
mapst 01946   ; LD ($FFFF),A
mapst 01A16   ; LD ($FFFE),A
mapst 01A23   ; LD ($FFFE),A
mapst 01BC3   ; LD ($FFFF),A
mapst 01E60   ; LD ($FFFF),A
mapst 02370   ; LD ($FFFF),A
mapst 02551   ; LD ($FFFF),A
mapst 030F1   ; LD ($FFFF),A
mapst 03164   ; LD ($FFFF),A
mapst 03611   ; LD ($FFFF),A
mapst 037F2   ; LD ($FFFF),A
mapst 045C4   ; LD ($FFFF),A
mapst 045CD   ; LD ($FFFF),A
mapst 04635   ; LD ($FFFF),A
mapst 0530C   ; LD ($FFFF),A
mapst 05902   ; LD ($FFFF),A
mapst 05936   ; LD ($FFFF),A
mapst 05EA9   ; LD ($FFFF),A
mapst 05EC0   ; LD ($FFFF),A
mapst 05ED7   ; LD ($FFFF),A
mapst 05EF2   ; LD ($FFFF),A
mapst 05F09   ; LD ($FFFF),A
mapst 05F20   ; LD ($FFFF),A
mapst 05F3B   ; LD ($FFFF),A
mapst 05F52   ; LD ($FFFF),A
mapst 05F69   ; LD ($FFFF),A
mapst 05F84   ; LD ($FFFF),A
mapst 05F9B   ; LD ($FFFF),A
mapst 05FB2   ; LD ($FFFF),A
mapst 06173   ; LD ($FFFF),A
mapst 061AC   ; LD ($FFFF),A
mapst 06B2B   ; LD ($FFFF),A
mapst 06C43   ; LD ($FFFF),A
mapst 06C54   ; LD ($FFFF),A
mapst 100FA   ; LD ($FFFF),A
mapst 1012A   ; LD ($FFFF),A
mapst 10172   ; LD ($FFFF),A
mapst 101EB   ; LD ($FFFF),A
mapst 1025D   ; LD ($FFFF),A
mapst 10298   ; LD ($FFFF),A
mapst 10A9E   ; LD ($FFFF),A
mapst 11DB2   ; LD ($FFFF),A
mapst 11E71   ; LD ($FFFF),A
mapst 1216D   ; LD ($FFFF),A
mapst 123D3   ; LD ($FFFF),A
mapst 124A7   ; LD ($FFFF),A
mapst 124F6   ; LD ($FFFF),A
mapst 15EAB   ; LD ($FFFE),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 01A3D   # LD ($FFFE),A; after LD A,$01; 32 bytes of valid code before it
mapst 05D1B   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 05D44   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 102AD   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 17DA1   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it

site 0C071   # OTIR; the sound driver's silence routine $805A (bank 3), which nothing calls
mapst 102DD   # LD ($FFFF),A; in $42A9 (bank 4), the RAM form of the graphics unpacker $40F2, which nothing calls
mapst 10313   # LD ($FFFF),A; in $42A9
mapst 1035C   # LD ($FFFF),A; in $42A9
site 12391   # IN A,($BE); in $633F (bank 4), the name table cell copier of the menu screens ($4B3D, $4E05)
site 12397   # IN A,($BE); in $633F
site 123A2   # OUT ($BE),A; in $633F
site 123A8   # OUT ($BE),A; in $633F

# Super Kick Off (Europe) (Action Replay).cht, "Timer Modifier" (00CF-94XX): the seconds digit
# of the clock is held, so the clock never counts down and the match does not end
poke "Infinite time"
ar 00CF-945E
endpoke

; Page 0: mapcol replaces the map column writer at $11F6-$121C. At $11F6 HL points into the
; table of name table row addresses at $1228 (bank 0), A is the column's byte offset, HL' the
; map byte of the column's top cell and DE' the map's row step ($92). For 28 rows it writes
; the cell (map byte, then $10 when the byte is $C7 or more, else $00) at the row's address
; OR A. Each cell goes through jt_vwrite. Returns with interrupts off, B = 0, C = the column
; offset, HL = the last row address, HL' past the last row, as the game's loop leaves them.
page 0 mapcol vcopy
mapcol:
    di
    ld (.sp),sp
    ld sp,.stk
    push ix
    push iy
    ld c,a
    ld b,$1C
.row:
    ld e,(hl)
    inc hl
    ld d,(hl)
    inc hl
    ld (.last),de
    ld a,e
    or c
    ld e,a
    exx
    ld a,(hl)
    add hl,de
    exx
    ld (.buf),a
    cp $C7
    ld a,$00
    jr c,.lo
    ld a,$10
.lo:
    ld (.buf+1),a
    push bc
    push hl
    ld hl,.buf
    ld bc,$0201
    ld ix,2
    ld iy,$40
    ld a,1
    call jt_vwrite
    pop hl
    pop bc
    djnz .row
    pop iy
    pop ix
    ld hl,(.last)
    ld sp,(.sp)
    ret
.sp:    dw 0
.last:  dw 0
.buf:   db 0, 0
        ds 32
.stk:

; vcopy replaces the copy loop at $0BC2-$0BCB: BC bytes (BC = 0 is not used by the game) from
; DE, as the game sees it, to VRAM at the address the game has set (vdp_addr). Each call of
; jt_vwrite writes up to 256 bytes; interrupts stay as the game has them (on), so the frame
; interrupt is taken between the calls on the game's stack (five words of it). Returns as
; the game's loop leaves it: DE past the last byte, BC = 0, A the last byte, Z set; HL kept.
vcopy:
    push hl
    push ix
    push iy
    ex de,hl
    ld ix,256
    ld iy,256
.next:
    ld a,b
    or a
    jr z,.part
    push bc
    ld b,0
    jr .go
.part:
    push bc
    ld b,c
.go:
    ld c,1
    ld de,(vdp_addr)
    xor a
    call jt_vwrite
    ld e,b
    ld d,0
    dec e
    inc de          ; DE = bytes written (B = 0 is 256)
    add hl,de
    pop bc
    ld a,b
    or a
    jr z,.last
    dec b
    jr nz,.next
    ld a,c
    or a
    jr nz,.next
    jr .done
.last:
    ld c,0
.done:
    dec hl
    call jt_peek
    inc hl
    ex de,hl
    ld bc,0
    pop iy
    pop ix
    pop hl
    cp a            ; Z set; A kept
    ret
endpage
