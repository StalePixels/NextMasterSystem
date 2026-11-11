# KLAX (Europe), CRC32 2B435FD6, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log of 600 s
# (random input), then decided by hand.
#
# Decisions:
# - $6B93 counts loop passes in one frame to tell a 50 Hz machine from a 60 Hz one and keeps
#   the result in $C001 (0: 50 Hz; 1: 60 Hz, the sound driver at $7A15 skips every sixth
#   frame). It repeats the test until the count is in a Master System's range, so on the
#   faster CPU it never ends. The test at $6BA3 sets the 50 Hz value.
# - $2E34 (D3 0A, OUT ($0A),A to the scanner) is not patched: it is the operand of
#   LD HL,$0AD3 at $2E33. The scanner reaches it through CALL $2E31 in the demo recorder
#   code at $0454, which jumps into the middle of that instruction.
# - No code runs from slot 2: banks 2-7 are data, and the spec patches nothing there.
# - Unused code (no call, jump or table names it): the VDP routines at $026F, $0291, $02FB,
#   $0409, $1230, $283E, $294A, $4DF8, $5948, $596A, $598B, $59A4 and $59DF.
name KLAX
cart 2B435FD6
hz 50		; No-Intro region Europe
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0000A   ; OUT ($3E),A
site 00039   ; IN A,($BF)
site 00067   ; IN A,($0E)
site 00212   ; OUT ($BF),A
site 00216   ; OUT ($BF),A
site 0021A   ; OUT ($BF),A
site 0021E   ; OUT ($BF),A
site 00222   ; OUT ($BF),A
site 00226   ; OUT ($BF),A
site 002D0   ; OUT ($BF),A
site 002D3   ; OUT ($BF),A
site 002E3   ; OUT ($BF),A
site 002EA   ; OUT ($BF),A
site 002F3   ; OUT ($BE),A
site 0030F   ; OUT ($3F),A
site 00311   ; IN A,($DC)
site 0037E   ; IN A,($DD)
site 00397   ; IN A,($DD)
site 003A9   ; IN A,($DD)
site 003CF   ; OTIR
site 003E5   ; OUT ($BF),A
site 003EF   ; OUT ($BF),A
site 00406   ; OUT ($BE),A
site 0058C   ; OUT ($BE),A
site 00600   ; IN A,($DD)
site 0084A   ; OUT ($BE),A
site 0084F   ; OUT ($BE),A
site 00854   ; OUT ($BE),A
site 00859   ; OUT ($BE),A
site 008C0   ; OUT ($BE),A
site 008C7   ; OUT ($BE),A
site 008CC   ; OUT ($BE),A
site 008D9   ; OUT ($BE),A
site 008EC   ; OUT ($BE),A
site 00920   ; OUT ($BE),A
site 00927   ; OUT ($BE),A
site 00B2F   ; OUT ($BF),A
site 00B33   ; OUT ($BF),A
site 00B3A   ; OUT ($BE),A
site 00B71   ; OUT ($BF),A
site 00B75   ; OUT ($BF),A
site 00B7C   ; OUT ($BE),A
site 00BBE   ; OUT ($BF),A
site 00BC2   ; OUT ($BF),A
site 00BC9   ; OUT ($BE),A
site 00C49   ; OUT ($BF),A
site 00C4D   ; OUT ($BF),A
site 00C54   ; OUT ($BE),A
site 00C60   ; OUT ($BF),A
site 00C64   ; OUT ($BF),A
site 00C6B   ; OUT ($BE),A
site 00D1E   ; OUT ($BF),A
site 00D22   ; OUT ($BF),A
site 00D29   ; OUT ($BE),A
site 010A7   ; OUT ($BF),A
site 010AB   ; OUT ($BF),A
site 010AF   ; OUTI
site 010B1   ; OUTI
site 010B3   ; OUTI
site 010B5   ; OUTI
site 010B7   ; OUTI
site 010B9   ; OUTI
site 010BB   ; OUTI
site 010BD   ; OUTI
site 010BF   ; OUTI
site 010C1   ; OUTI
site 010C3   ; OUTI
site 010C5   ; OUTI
site 010C7   ; OUTI
site 010C9   ; OUTI
site 010CB   ; OUTI
site 010CD   ; OUTI
site 010CF   ; OUTI
site 010D1   ; OUTI
site 010D3   ; OUTI
site 010D5   ; OUTI
site 010D7   ; OUTI
site 010D9   ; OUTI
site 010DB   ; OUTI
site 010DD   ; OUTI
site 010DF   ; OUTI
site 010E1   ; OUTI
site 010E3   ; OUTI
site 010E5   ; OUTI
site 010E7   ; OUTI
site 010E9   ; OUTI
site 010EB   ; OUTI
site 010ED   ; OUTI
site 010EF   ; OUTI
site 010F1   ; OUTI
site 010F3   ; OUTI
site 010F5   ; OUTI
site 010F7   ; OUTI
site 010F9   ; OUTI
site 010FB   ; OUTI
site 010FD   ; OUTI
site 010FF   ; OUTI
site 01101   ; OUTI
site 01103   ; OUTI
site 01105   ; OUTI
site 01107   ; OUTI
site 01109   ; OUTI
site 0110B   ; OUTI
site 0110D   ; OUTI
site 0110F   ; OUTI
site 01111   ; OUTI
site 01113   ; OUTI
site 01115   ; OUTI
site 01117   ; OUTI
site 01119   ; OUTI
site 0111B   ; OUTI
site 0111D   ; OUTI
site 0111F   ; OUTI
site 01121   ; OUTI
site 01123   ; OUTI
site 01125   ; OUTI
site 01127   ; OUTI
site 01129   ; OUTI
site 01130   ; OUT ($BF),A
site 01133   ; OUT ($BF),A
site 01137   ; OUTI
site 01139   ; OUTI
site 0113B   ; OUTI
site 0113D   ; OUTI
site 0113F   ; OUTI
site 01141   ; OUTI
site 01143   ; OUTI
site 01145   ; OUTI
site 01147   ; OUTI
site 01149   ; OUTI
site 0114B   ; OUTI
site 0114D   ; OUTI
site 0114F   ; OUTI
site 01151   ; OUTI
site 01153   ; OUTI
site 01155   ; OUTI
site 01157   ; OUTI
site 01159   ; OUTI
site 0115B   ; OUTI
site 0115D   ; OUTI
site 0115F   ; OUTI
site 01161   ; OUTI
site 01163   ; OUTI
site 01165   ; OUTI
site 01167   ; OUTI
site 01169   ; OUTI
site 0116B   ; OUTI
site 0116D   ; OUTI
site 0116F   ; OUTI
site 01171   ; OUTI
site 01173   ; OUTI
site 01175   ; OUTI
site 01177   ; OUTI
site 01179   ; OUTI
site 0117B   ; OUTI
site 0117D   ; OUTI
site 0117F   ; OUTI
site 01181   ; OUTI
site 01183   ; OUTI
site 01185   ; OUTI
site 01187   ; OUTI
site 01189   ; OUTI
site 0118B   ; OUTI
site 0118D   ; OUTI
site 0118F   ; OUTI
site 01191   ; OUTI
site 01193   ; OUTI
site 01195   ; OUTI
site 01197   ; OUTI
site 01199   ; OUTI
site 0119B   ; OUTI
site 0119D   ; OUTI
site 0119F   ; OUTI
site 011A1   ; OUTI
site 011A3   ; OUTI
site 011A5   ; OUTI
site 011A7   ; OUTI
site 011A9   ; OUTI
site 011AB   ; OUTI
site 011AD   ; OUTI
site 011AF   ; OUTI
site 011B1   ; OUTI
site 011B3   ; OUTI
site 011B5   ; OUTI
site 011B7   ; OUTI
site 011B9   ; OUTI
site 011BB   ; OUTI
site 011BD   ; OUTI
site 011BF   ; OUTI
site 011C1   ; OUTI
site 011C3   ; OUTI
site 011C5   ; OUTI
site 011C7   ; OUTI
site 011C9   ; OUTI
site 011CB   ; OUTI
site 011CD   ; OUTI
site 011CF   ; OUTI
site 011D1   ; OUTI
site 011D3   ; OUTI
site 011D5   ; OUTI
site 011D7   ; OUTI
site 011D9   ; OUTI
site 011DB   ; OUTI
site 011DD   ; OUTI
site 011DF   ; OUTI
site 011E1   ; OUTI
site 011E3   ; OUTI
site 011E5   ; OUTI
site 011E7   ; OUTI
site 011E9   ; OUTI
site 011EB   ; OUTI
site 011ED   ; OUTI
site 011EF   ; OUTI
site 011F1   ; OUTI
site 011F3   ; OUTI
site 011F5   ; OUTI
site 011F7   ; OUTI
site 011F9   ; OUTI
site 011FB   ; OUTI
site 011FD   ; OUTI
site 011FF   ; OUTI
site 01201   ; OUTI
site 01203   ; OUTI
site 01205   ; OUTI
site 01207   ; OUTI
site 01209   ; OUTI
site 0120B   ; OUTI
site 0120D   ; OUTI
site 0120F   ; OUTI
site 01211   ; OUTI
site 01213   ; OUTI
site 01215   ; OUTI
site 01217   ; OUTI
site 01219   ; OUTI
site 0121B   ; OUTI
site 0121D   ; OUTI
site 0121F   ; OUTI
site 01221   ; OUTI
site 01223   ; OUTI
site 01225   ; OUTI
site 01227   ; OUTI
site 01229   ; OUTI
site 0122B   ; OUTI
site 0122D   ; OUTI
site 0127E   ; OUTI
site 01280   ; OUTI
site 01282   ; OUTI
site 01284   ; OUTI
site 01286   ; OUTI
site 01288   ; OUTI
site 0128A   ; OUTI
site 0128C   ; OUTI
site 0128E   ; OUTI
site 01290   ; OUTI
site 01292   ; OUTI
site 01294   ; OUTI
site 01296   ; OUTI
site 01298   ; OUTI
site 0129A   ; OUTI
site 0129C   ; OUTI
site 012A3   ; OUT ($BF),A
site 012A7   ; OUT ($BF),A
site 012AE   ; OUT ($BE),A
site 012B3   ; OUT ($BE),A
site 012BB   ; OUT ($BF),A
site 012BF   ; OUT ($BF),A
site 012C6   ; OUT ($BE),A
site 012CB   ; OUT ($BE),A
site 012D4   ; OUT ($BF),A
site 012D8   ; OUT ($BF),A
site 012DF   ; OUT ($BE),A
site 012E4   ; OUT ($BE),A
site 012EE   ; OUT ($BF),A
site 012F2   ; OUT ($BF),A
site 012F9   ; OUT ($BE),A
site 012FE   ; OUT ($BE),A
site 01307   ; OUT ($BF),A
site 0130B   ; OUT ($BF),A
site 01312   ; OUT ($BE),A
site 01317   ; OUT ($BE),A
site 0154E   ; OUT ($BF),A
site 01552   ; OUT ($BF),A
site 01561   ; OUT ($BE),A
site 01567   ; OUT ($BE),A
site 0157D   ; OUT ($BF),A
site 01580   ; OUT ($BF),A
site 01591   ; OUT ($BE),A
site 01598   ; OUT ($BE),A
site 0159E   ; OUT ($BE),A
site 015A5   ; OUT ($BE),A
site 02858   ; OUT ($BF),A
site 0285C   ; OUT ($BF),A
site 02863   ; OUT ($BE),A
site 02A85   ; OUT ($BF),A
site 02A89   ; OUT ($BF),A
site 02A99   ; OUT ($BE),A
site 02AA0   ; OUT ($BE),A
site 02AA9   ; OUT ($BF),A
site 02AAE   ; OUT ($BF),A
site 02AB4   ; OUT ($BE),A
site 02ABB   ; OUT ($BE),A
site 02AED   ; OUT ($BF),A
site 02AF1   ; OUT ($BF),A
site 02AF8   ; OUT ($BE),A
site 02C04   ; OUT ($BF),A
site 02C08   ; OUT ($BF),A
site 02C0F   ; OUT ($BE),A
site 02D4B   ; OUT ($3F),A
site 02D4D   ; IN A,($DC)
site 03798   ; OUT ($BF),A
site 0379D   ; OUT ($BF),A
site 037B3   ; OUT ($BE),A
site 037BB   ; OUT ($BE),A
site 037C1   ; OUT ($BE),A
site 037C8   ; OUT ($BE),A
site 037EA   ; OUT ($BF),A
site 037EF   ; OUT ($BF),A
site 037F7   ; OUT ($BE),A
site 037FF   ; OUT ($BE),A
site 03806   ; OUT ($BE),A
site 0380D   ; OUT ($BE),A
site 0381E   ; OUT ($BE),A
site 03842   ; OUT ($BF),A
site 03847   ; OUT ($BF),A
site 03858   ; OUT ($BE),A
site 03C44   ; OUT ($BF),A
site 03C47   ; OUT ($BF),A
site 03C4E   ; OUT ($BE),A
site 03C55   ; OUT ($BE),A
site 03C5D   ; OUT ($BF),A
site 03C60   ; OUT ($BF),A
site 03C67   ; OUT ($BE),A
site 03C6E   ; OUT ($BE),A
site 03CD2   ; OUT ($BF),A
site 03CD7   ; OUT ($BF),A
site 03CDE   ; OUT ($BE),A
site 03CE9   ; OUT ($BE),A
site 03CF0   ; OUT ($BE),A
site 03CF6   ; OUT ($BE),A
site 03D42   ; OUT ($BF),A
site 03D47   ; OUT ($BF),A
site 03D4F   ; OUT ($BE),A
site 03D56   ; OUT ($BE),A
site 03D5C   ; OUT ($BE),A
site 03D62   ; OUT ($BE),A
site 03D67   ; OUT ($BF),A
site 03D6A   ; OUT ($BF),A
site 03D6F   ; IN A,($BE)
site 03D75   ; IN A,($BE)
site 03D88   ; OUT ($BF),A
site 03D8B   ; OUT ($BF),A
site 03DAA   ; OUT ($BF),A
site 03DAD   ; OUT ($BF),A
site 03DCC   ; IN A,($BE)
site 03E22   ; IN A,($BE)
site 03E28   ; IN A,($BE)
site 03E2E   ; IN A,($BE)
site 03E34   ; IN A,($BE)
site 03E5D   ; OUT ($BF),A
site 03E62   ; OUT ($BF),A
site 03E68   ; OUT ($BE),A
site 03E7C   ; OUT ($BF),A
site 03E7F   ; OUT ($BF),A
site 03ED5   ; OUT ($BF),A
site 03ED8   ; OUT ($BF),A
site 03EE3   ; OUT ($BE),A
site 03EE8   ; OUT ($BE),A
site 03EED   ; OUT ($BE),A
site 03EF3   ; OUT ($BE),A
site 041B2   ; OUT ($BF),A
site 041B5   ; OUT ($BF),A
site 041BB   ; OUT ($BE),A
site 041C1   ; OUT ($BE),A
site 041F6   ; OUT ($BF),A
site 041F9   ; OUT ($BF),A
site 04200   ; OUT ($BE),A
site 04209   ; OUT ($BE),A
site 0420E   ; OUT ($BF),A
site 04211   ; OUT ($BF),A
site 04217   ; OUT ($BE),A
site 04224   ; OUT ($BE),A
site 042C1   ; OUT ($BF),A
site 042C4   ; OUT ($BF),A
site 042D6   ; OUT ($BE),A
site 042DC   ; OUT ($BE),A
site 04388   ; OUT ($BF),A
site 0438B   ; OUT ($BF),A
site 04399   ; OUT ($BE),A
site 043A0   ; OUT ($BE),A
site 043A6   ; OUT ($BF),A
site 043AB   ; OUT ($BF),A
site 043B5   ; OUT ($BE),A
site 043BC   ; OUT ($BE),A
site 0484A   ; OUT ($BF),A
site 0484D   ; OUT ($BF),A
site 04854   ; IN A,($BE)
site 0485E   ; OUT ($BF),A
site 04861   ; OUT ($BF),A
site 04866   ; IN A,($BE)
site 0486E   ; IN A,($BE)
site 048F7   ; OUT ($BF),A
site 048FC   ; OUT ($BF),A
site 0490D   ; OUT ($BE),A
site 04913   ; OUT ($BE),A
site 0492A   ; OUT ($BF),A
site 0492F   ; OUT ($BF),A
site 04940   ; OUT ($BE),A
site 04946   ; OUT ($BE),A
site 049CB   ; OUT ($BF),A
site 049CE   ; OUT ($BF),A
site 049D5   ; OUT ($BE),A
site 049DB   ; OUT ($BE),A
site 049E0   ; OUT ($BE),A
site 049E6   ; OUT ($BE),A
site 04A2C   ; OUT ($BF),A
site 04A30   ; OUT ($BF),A
site 04A37   ; OUT ($BE),A
site 04A91   ; OUT ($BF),A
site 04A96   ; OUT ($BF),A
site 04A9D   ; OUT ($BE),A
site 04AA2   ; OUT ($BE),A
site 04B72   ; OUT ($BF),A
site 04B77   ; OUT ($BF),A
site 04B85   ; OUT ($BE),A
site 04B8B   ; OUT ($BE),A
site 04BE7   ; OUT ($BF),A
site 04BEC   ; OUT ($BF),A
site 04BF3   ; OUT ($BE),A
site 04BFA   ; OUT ($BE),A
site 04C1D   ; OUT ($BF),A
site 04C20   ; OUT ($BF),A
site 04C25   ; OUT ($BE),A
site 04C2C   ; OUT ($BE),A
site 04CA6   ; OUT ($BF),A
site 04CA9   ; OUT ($BF),A
site 04CB0   ; OUT ($BE),A
site 04CB7   ; OUT ($BE),A
site 04CCB   ; OUT ($BF),A
site 04CCE   ; OUT ($BF),A
site 04CD5   ; OUT ($BE),A
site 04CDC   ; OUT ($BE),A
site 04CE5   ; OUT ($BF),A
site 04CE8   ; OUT ($BF),A
site 04CEF   ; OUT ($BE),A
site 04CF6   ; OUT ($BE),A
site 04D2E   ; OUT ($BF),A
site 04D31   ; OUT ($BF),A
site 04D38   ; OUT ($BE),A
site 04D3F   ; OUT ($BE),A
site 04DA7   ; OUT ($BF),A
site 04DAA   ; OUT ($BF),A
site 04DB8   ; OUT ($BE),A
site 04DBF   ; OUT ($BE),A
site 04DC5   ; OUT ($BF),A
site 04DCA   ; OUT ($BF),A
site 04DE7   ; OUT ($BE),A
site 04DEE   ; OUT ($BE),A
site 04E6D   ; OUT ($BF),A
site 04E70   ; OUT ($BF),A
site 04E77   ; OUT ($BE),A
site 04E7E   ; OUT ($BE),A
site 04E85   ; OUT ($BE),A
site 04E8C   ; OUT ($BE),A
site 04E93   ; OUT ($BF),A
site 04E96   ; OUT ($BF),A
site 04E9D   ; OUT ($BE),A
site 04EA4   ; OUT ($BE),A
site 04EAB   ; OUT ($BE),A
site 04EB2   ; OUT ($BE),A
site 04EB7   ; OUT ($BF),A
site 04EBB   ; OUT ($BF),A
site 04EC2   ; OUT ($BE),A
site 04F0D   ; OUT ($BF),A
site 04F11   ; OUT ($BF),A
site 04F18   ; OUT ($BE),A
site 04F55   ; OUT ($BF),A
site 04F59   ; OUT ($BF),A
site 04F60   ; OUT ($BE),A
site 04FF8   ; OUT ($BF),A
site 04FFB   ; OUT ($BF),A
site 05000   ; IN A,($BE)
site 05005   ; OUT ($BF),A
site 0500A   ; OUT ($BF),A
site 05010   ; OUT ($BE),A
site 05013   ; OUT ($BF),A
site 05017   ; OUT ($BF),A
site 0501D   ; OUT ($BE),A
site 05027   ; OUT ($BF),A
site 0502B   ; OUT ($BF),A
site 05032   ; OUT ($BE),A
site 0517F   ; OUT ($BF),A
site 05183   ; OUT ($BF),A
site 0518A   ; OUT ($BE),A
site 051D6   ; OUT ($BF),A
site 051DA   ; OUT ($BF),A
site 051E1   ; OUT ($BE),A
site 0533D   ; OUT ($BF),A
site 05341   ; OUT ($BF),A
site 05348   ; OUT ($BE),A
site 0534C   ; OUT ($BE),A
site 05350   ; OUT ($BE),A
site 05354   ; OUT ($BF),A
site 05358   ; OUT ($BF),A
site 0535F   ; OUT ($BE),A
site 05363   ; OUT ($BE),A
site 05374   ; OUT ($BE),A
site 05378   ; OUT ($BE),A
site 053A7   ; OUT ($BF),A
site 053AE   ; OUT ($BF),A
site 053B9   ; OUTI
site 053BB   ; OUTI
site 053BD   ; OUTI
site 053BF   ; OUTI
site 053C1   ; OUTI
site 053C3   ; OUTI
site 053C5   ; OUTI
site 053C7   ; OUTI
site 053C9   ; OUTI
site 053CB   ; OUTI
site 053CD   ; OUTI
site 053CF   ; OUTI
site 053D1   ; OUTI
site 053D3   ; OUTI
site 053D5   ; OUTI
site 053D7   ; OUTI
site 053D9   ; OUTI
site 053DB   ; OUTI
site 053DD   ; OUTI
site 053DF   ; OUTI
site 053E1   ; OUTI
site 053E3   ; OUTI
site 053E5   ; OUTI
site 053E7   ; OUTI
site 053E9   ; OUTI
site 053EB   ; OUTI
site 053ED   ; OUTI
site 053EF   ; OUTI
site 053F1   ; OUTI
site 053F3   ; OUTI
site 053F5   ; OUTI
site 053F7   ; OUTI
site 05438   ; OUT ($BF),A
site 0543F   ; OUT ($BF),A
site 0544A   ; OUTI
site 0544F   ; OUTI
site 05454   ; OUTI
site 05459   ; OUTI
site 0545E   ; OUTI
site 05463   ; OUTI
site 05468   ; OUTI
site 0546D   ; OUTI
site 05472   ; OUTI
site 05477   ; OUTI
site 0547C   ; OUTI
site 05481   ; OUTI
site 05486   ; OUTI
site 0548B   ; OUTI
site 05490   ; OUTI
site 05495   ; OUTI
site 0549A   ; OUTI
site 0549F   ; OUTI
site 054A4   ; OUTI
site 054A9   ; OUTI
site 054AE   ; OUTI
site 054B3   ; OUTI
site 054B8   ; OUTI
site 054BD   ; OUTI
site 054C2   ; OUTI
site 054C7   ; OUTI
site 054CC   ; OUTI
site 054D1   ; OUTI
site 054D6   ; OUTI
site 054DB   ; OUTI
site 054E0   ; OUTI
site 054E5   ; OUTI
site 055DB   ; OUT ($BF),A
site 055DF   ; OUT ($BF),A
site 055F4   ; OUT ($BE),A
site 05622   ; OUT ($BF),A
site 05628   ; OUT ($BF),A
site 05634   ; OUT ($BE),A
site 05639   ; OUT ($BE),A
site 05644   ; OUT ($BF),A
site 05648   ; OUT ($BF),A
site 0564E   ; OUT ($BE),A
site 05655   ; OUT ($BE),A
site 0565C   ; OUT ($BE),A
site 05663   ; OUT ($BE),A
site 05672   ; OUT ($BF),A
site 05677   ; OUT ($BF),A
site 05680   ; OUT ($BE),A
site 0568F   ; OUT ($BF),A
site 05692   ; OUT ($BF),A
site 056A1   ; OUT ($BE),A
site 056A6   ; OUT ($BE),A
site 056BC   ; OUT ($BE),A
site 056C1   ; OUT ($BE),A
site 056E2   ; OUT ($BF),A
site 056E5   ; OUT ($BF),A
site 056EF   ; OUT ($BE),A
site 056F4   ; OUT ($BE),A
site 057C2   ; OUT ($BF),A
site 057C6   ; OUT ($BF),A
site 057CC   ; OUT ($BE),A
site 05824   ; OUT ($BF),A
site 05828   ; OUT ($BF),A
site 0582E   ; OUT ($BE),A
site 05961   ; OUT ($BE),A
site 0597A   ; OUT ($BF),A
site 0597D   ; OUT ($BF),A
site 059BC   ; OTIR
site 059D2   ; OUT ($BF),A
site 059DC   ; OUT ($BF),A
site 07A9F   ; OUT ($7F),A
site 07AA8   ; OUT ($7F),A
site 07AB6   ; OUT ($7F),A
site 07ABB   ; OUT ($7F),A
site 07AC3   ; OUT ($7F),A
asm 06BA3 5   ; DI; LD A,B; CP $0D: the speed test of $6B93, which counts loop passes in a frame
    di
    xor a         ; $C001 = 0, the 50 Hz value
    jp $6BBD
endasm
mapldk 0000C   # LD HL,$FFFC; LD (HL),$00
maphl 00012   # LD (HL),$00, HL = $FFFD
maphl 00015   # LD (HL),$01, HL = $FFFE
maphl 00018   # LD (HL),$02, HL = $FFFF
mapst 0034B   ; LD ($FFFF),A
mapst 00363   ; LD ($FFFF),A
mapst 0079E   ; LD ($FFFF),A
mapst 007CE   ; LD ($FFFF),A
mapst 00816   ; LD ($FFFF),A
mapst 0088F   ; LD ($FFFF),A
mapst 00901   ; LD ($FFFF),A
mapst 0093C   ; LD ($FFFF),A
mapst 00981   ; LD ($FFFF),A
mapst 009B7   ; LD ($FFFF),A
mapst 00A00   ; LD ($FFFF),A
mapst 03EDC   ; LD ($FFFF),A
mapst 04384   ; LD ($FFFF),A
mapst 04561   ; LD ($FFFF),A
mapst 0460D   ; LD ($FFFF),A
mapst 04615   ; LD ($FFFF),A
mapst 0471F   ; LD ($FFFF),A
mapst 04727   ; LD ($FFFF),A
mapst 04767   ; LD ($FFFF),A
mapst 04788   ; LD ($FFFF),A
mapst 04B59   ; LD ($FFFF),A
mapst 04C38   ; LD ($FFFF),A
mapst 04C68   ; LD ($FFFF),A
mapst 04C87   ; LD ($FFFF),A
mapst 04CFF   ; LD ($FFFF),A
mapst 04D10   ; LD ($FFFF),A
mapst 04D64   ; LD ($FFFF),A
mapst 04DA3   ; LD ($FFFF),A
mapst 053A3   ; LD ($FFFF),A
mapst 05434   ; LD ($FFFF),A
mapst 05519   ; LD ($FFFF),A
mapst 0556E   ; LD ($FFFF),A
mapst 05592   ; LD ($FFFF),A
mapst 055B1   ; LD ($FFFF),A
mapst 055ED   ; LD ($FFFF),A
mapst 0562C   ; LD ($FFFF),A
mapst 0566A   ; LD ($FFFF),A
mapst 05688   ; LD ($FFFF),A
mapst 056E9   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00089   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 00951   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it

# Klax (Europe) (Action Replay).cht, "Infinite Drop Meter": RAM $C09F counts the drops lost
# in a game; held at 0, no drop is ever lost
poke "Infinite drops"
ar 00C0-9F00
endpoke

# Klax (Europe).cht, "Infinite Credits (Continues)": RAM $C0E6 is the number of credits left,
# held at 9, so every continue is free
poke "Infinite credits"
ar 00C0-E609
endpoke

# Klax (Europe) (Action Replay).cht, "Klaxes Remaining Modifier": RAM $C1FE is the number of
# klaxes left in the wave. At 01 the next klax ends the wave; at 00 or above 01 the wave never ends
poke "Klaxes to go ??"
ar 00C1-FE??
endpoke
