# Aztec Adventure (World), CRC32 FF614EB3, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output.
# Decisions:
# - The unrolled OUTI run $03D0-$040F (32 OUTI, then RET) has no entry: no call, jump,
#   address load or table entry names an address in it, and a 10-minute recording did
#   not run it (verdict unused). The scanner reached $0400 only through a pointer
#   harvest of the timer value $0400 stored at $0D18, so those rows are not patched.
# - The other byte patterns that no path reached are data in banks 3, 6 and 7, which
#   no code runs, or the operand of JR NC at $1BD2 (verdict false).
name Aztec Adventure
cart FF614EB3
hz any		; No-Intro region World
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
otir 00033   ; OUTI
site 00039   ; IN A,($BF)
site 00181   ; IN A,($DD)
site 001A6   ; OUT ($BE),A
otir 001B8   ; OUTI
site 001D1   ; OUTI
site 001D5   ; OUT (C),A
site 001E6   ; INI
site 00205   ; OUT ($BE),A
otir 00212   ; OUTI
otir 00242   ; OUTI
site 0024F   ; OUTI
site 00255   ; OUT (C),A
site 00279   ; OUT (C),D
site 00296   ; OUT ($BF),A
site 0029A   ; OUT ($BF),A
site 002A2   ; OUTD
site 002A8   ; OUT ($BE),A
site 002AC   ; OUT ($BF),A
site 002B0   ; OUT ($BF),A
site 002BF   ; OUTI
site 002C1   ; OUTD
site 002CF   ; OUT ($BF),A
site 002D3   ; OUT ($BF),A
otir 002D5   ; OUTI
site 002DE   ; OUT ($BF),A
site 002E2   ; OUT ($BF),A
otir 002E6   ; OUTI
site 002F0   ; OUT ($BE),A
site 002F8   ; OTIR
site 00333   ; OUT (C),D
site 00335   ; IN A,($BE)
site 00337   ; IN A,($BE)
site 00339   ; IN A,($BE)
site 00343   ; OUTI
site 00345   ; IN A,($BE)
site 00347   ; IN A,($BE)
site 00349   ; IN A,($BE)
site 00368   ; OUT ($BF),A
site 0036B   ; OUT ($BF),A
site 0036F   ; OUT ($BE),A
site 00413   ; OUT ($BE),A
site 00418   ; OUT ($BE),A
site 0041D   ; OUT ($BE),A
site 00422   ; OUT ($BE),A
site 00427   ; OUT ($BE),A
site 0042C   ; OUT ($BE),A
site 00431   ; OUT ($BE),A
site 00436   ; OUT ($BE),A
site 0043B   ; OUT ($BE),A
site 00440   ; OUT ($BE),A
site 00445   ; OUT ($BE),A
site 0044A   ; OUT ($BE),A
site 0044F   ; OUT ($BE),A
site 00454   ; OUT ($BE),A
site 00459   ; OUT ($BE),A
site 0045E   ; OUT ($BE),A
site 00463   ; OUT ($BE),A
site 00468   ; OUT ($BE),A
site 0046D   ; OUT ($BE),A
site 00472   ; OUT ($BE),A
site 00477   ; OUT ($BE),A
site 0047C   ; OUT ($BE),A
site 00481   ; OUT ($BE),A
site 00486   ; OUT ($BE),A
site 0048B   ; OUT ($BE),A
site 00490   ; OUT ($BE),A
site 00495   ; OUT ($BE),A
site 0049A   ; OUT ($BE),A
site 0049F   ; OUT ($BE),A
site 004A4   ; OUT ($BE),A
site 004A9   ; OUT ($BE),A
site 004AE   ; OUT ($BE),A
site 004B3   ; OUTI
site 004B5   ; OUTI
site 004B7   ; OUT ($BE),A
site 004B9   ; OUT ($BE),A
site 004BB   ; OUTI
site 004BD   ; OUTI
site 004BF   ; OUT ($BE),A
site 004C1   ; OUT ($BE),A
site 004C3   ; OUTI
site 004C5   ; OUTI
site 004C7   ; OUT ($BE),A
site 004C9   ; OUT ($BE),A
site 004CB   ; OUTI
site 004CD   ; OUTI
site 004CF   ; OUT ($BE),A
site 004D1   ; OUT ($BE),A
site 004D3   ; OUTI
site 004D5   ; OUTI
site 004D7   ; OUT ($BE),A
site 004D9   ; OUT ($BE),A
site 004DB   ; OUTI
site 004DD   ; OUTI
site 004DF   ; OUT ($BE),A
site 004E1   ; OUT ($BE),A
site 004E3   ; OUTI
site 004E5   ; OUTI
site 004E7   ; OUT ($BE),A
site 004E9   ; OUT ($BE),A
site 004EB   ; OUTI
site 004ED   ; OUTI
site 004EF   ; OUT ($BE),A
site 004F1   ; OUT ($BE),A
site 004FE   ; OUT ($BE),A
site 00503   ; OUT ($BE),A
site 00594   ; OUT ($3F),A
site 00596   ; IN A,($DD)
site 005A0   ; OUT ($3F),A
site 005A2   ; IN A,($DD)
site 005AB   ; OUT ($3F),A
site 005B7   ; IN A,($DC)
site 005BD   ; IN A,($DD)
site 005D7   ; OUT ($3E),A
site 005DF   ; OUT ($F2),A
site 005E2   ; IN A,($F2)
site 005F4   ; OUT ($F2),A
site 005FC   ; OUT ($3E),A
site 0068A   ; IN A,($BE)
site 0068E   ; IN A,($BE)
site 00697   ; OUT ($BE),A
site 0069E   ; OUT ($BE),A
site 0073C   ; OUT ($BE),A
site 0073F   ; OUT ($BE),A
site 00742   ; OUT ($BE),A
site 00744   ; OUT ($BE),A
site 00787   ; OUT ($BF),A
site 0078B   ; OUT ($BF),A
site 00792   ; OTIR
site 0079A   ; OUT ($BF),A
site 0079E   ; OUT ($BF),A
site 007A3   ; OTIR
site 007E1   ; OUT ($BE),A
site 00B5A   ; OUT ($BE),A
site 00B61   ; OUT ($BE),A
site 00B63   ; OUT ($BE),A
site 00D52   ; OUT ($BF),A
site 00D56   ; OUT ($BF),A
site 00D5A   ; OUT ($BF),A
site 00D5E   ; OUT ($BF),A
site 00DAA   ; OUT ($BF),A
site 00DAE   ; OUT ($BF),A
site 00DB2   ; OUT ($BF),A
site 00DB6   ; OUT ($BF),A
site 00DD5   ; OUT ($BF),A
site 00DD9   ; OUT ($BF),A
site 00DE1   ; OUT ($BF),A
site 00DE5   ; OUT ($BF),A
site 00DEC   ; OUT ($BF),A
site 00DF0   ; OUT ($BF),A
site 00E7B   ; OUT ($BF),A
site 00E7F   ; OUT ($BF),A
site 01168   ; OUT ($BE),A
site 0116D   ; OUT ($BE),A
site 0245C   ; OUT ($BF),A
site 02460   ; OUT ($BF),A
site 02477   ; OUTI
site 02479   ; OUTI
site 0247B   ; OUTI
site 0247D   ; OUT ($BE),A
site 0247F   ; OUTI
site 02481   ; OUTI
site 02483   ; OUTI
site 02485   ; OUT ($BE),A
site 02487   ; OUTI
site 02489   ; OUTI
site 0248B   ; OUTI
site 0248D   ; OUT ($BE),A
site 0248F   ; OUTI
site 02491   ; OUTI
site 02493   ; OUTI
site 02495   ; OUT ($BE),A
site 02497   ; OUTI
site 02499   ; OUTI
site 0249B   ; OUTI
site 0249D   ; OUT ($BE),A
site 0249F   ; OUTI
site 024A1   ; OUTI
site 024A3   ; OUTI
site 024A5   ; OUT ($BE),A
site 024A7   ; OUTI
site 024A9   ; OUTI
site 024AB   ; OUTI
site 024AD   ; OUT ($BE),A
site 024AF   ; OUTI
site 024B1   ; OUTI
site 024B3   ; OUTI
site 024B5   ; OUT ($BE),A
site 024B7   ; OUTI
site 024B9   ; OUTI
site 024BB   ; OUTI
site 024BD   ; OUT ($BE),A
site 024BF   ; OUTI
site 024C1   ; OUTI
site 024C3   ; OUTI
site 024C5   ; OUT ($BE),A
site 024C7   ; OUTI
site 024C9   ; OUTI
site 024CB   ; OUTI
site 024CD   ; OUT ($BE),A
site 024CF   ; OUTI
site 024D1   ; OUTI
site 024D3   ; OUTI
site 024D5   ; OUT ($BE),A
site 024D7   ; OUTI
site 024D9   ; OUTI
site 024DB   ; OUTI
site 024DD   ; OUT ($BE),A
site 024DF   ; OUTI
site 024E1   ; OUTI
site 024E3   ; OUTI
site 024E5   ; OUT ($BE),A
site 024E7   ; OUTI
site 024E9   ; OUTI
site 024EB   ; OUTI
site 024ED   ; OUT ($BE),A
site 024EF   ; OUTI
site 024F1   ; OUTI
site 024F3   ; OUTI
site 024F5   ; OUT ($BE),A
site 02ABF   ; OUT ($BF),A
site 02AC3   ; OUT ($BF),A
site 02AC8   ; OUT ($BF),A
site 02ACC   ; OUT ($BF),A
site 02AD4   ; OUT ($BF),A
site 02AD7   ; OUT ($BF),A
site 02ADD   ; OUT ($BE),A
site 02AE2   ; OUT ($BE),A
site 031AF   ; OUT ($BF),A
site 031B2   ; OUT ($BF),A
site 031C5   ; OUTI
site 031C7   ; OUTI
site 031C9   ; OUTI
site 031CB   ; OUTI
site 031CD   ; OUTI
site 031CF   ; OUTI
site 031D1   ; OUTI
site 031D3   ; OUTI
site 031D5   ; OUTI
site 031D7   ; OUTI
site 031D9   ; OUTI
site 031DB   ; OUTI
site 031DD   ; OUTI
site 031DF   ; OUTI
site 031E1   ; OUTI
site 031E3   ; OUTI
site 031E5   ; OUTI
site 031E7   ; OUTI
site 031E9   ; OUTI
site 031EB   ; OUTI
site 031ED   ; OUTI
site 031EF   ; OUTI
site 031F1   ; OUTI
site 031F3   ; OUTI
site 031F5   ; OUTI
site 031F7   ; OUTI
site 031F9   ; OUTI
site 031FB   ; OUTI
site 031FD   ; OUTI
site 031FF   ; OUTI
site 03201   ; OUTI
site 03203   ; OUTI
site 03205   ; OUTI
site 03207   ; OUTI
site 03209   ; OUTI
site 0320B   ; OUTI
site 0320D   ; OUTI
site 0320F   ; OUTI
site 03211   ; OUTI
site 03213   ; OUTI
site 03215   ; OUTI
site 03217   ; OUTI
site 03219   ; OUTI
site 0321B   ; OUTI
site 0321D   ; OUTI
site 0321F   ; OUTI
site 03221   ; OUTI
site 03223   ; OUTI
site 03225   ; OUTI
site 03227   ; OUTI
site 03229   ; OUTI
site 0322B   ; OUTI
site 0322D   ; OUTI
site 0322F   ; OUTI
site 03231   ; OUTI
site 03233   ; OUTI
site 03235   ; OUTI
site 03237   ; OUTI
site 03239   ; OUTI
site 0323B   ; OUTI
site 0323D   ; OUTI
site 0323F   ; OUTI
site 03241   ; OUTI
site 03243   ; OUTI
site 0400B   ; OUT ($BE),A
site 04167   ; OTIR
site 04291   ; OUT ($BE),A
site 04299   ; OUT ($BE),A
site 042A3   ; OUT ($BE),A
site 042AB   ; OUT ($BE),A
site 04539   ; OUT ($BE),A
site 0453D   ; OUT ($BE),A
site 06490   ; OUT ($BE),A
site 064C6   ; OUT ($BE),A
site 07F3C   ; OUT ($BE),A
site 07F57   ; OUT ($BF),A
site 07F5A   ; OUT ($BF),A
site 07F5D   ; OUT ($BE),A
site 140FF   ; OUT (C),B
site 14104   ; OUT ($F1),A
site 14148   ; OUT ($7F),A
site 14157   ; OUT ($F0),A
site 1415E   ; OUT ($F1),A
site 14166   ; OUT ($F0),A
site 1416D   ; OUT ($F1),A
site 142C3   ; OUT ($F0),A
site 142C9   ; OUT ($F1),A
site 142D4   ; OUTI
site 142DB   ; OUTI
site 142FC   ; OUT ($7F),A
site 14300   ; OUT ($7F),A
site 14350   ; OUT ($F0),A
site 14357   ; OUT ($F1),A
site 1435F   ; OUT ($F0),A
site 14365   ; OUT ($F1),A
site 1445F   ; OUT ($F0),A
site 14466   ; OUT (C),L
site 14472   ; OUT ($F0),A
site 1448D   ; OUT (C),H
site 14495   ; OUT ($F0),A
site 144A1   ; OUT ($F1),A
site 144A9   ; OUT ($F0),A
site 144B3   ; OUT ($F1),A
site 14635   ; OUT ($F0),A
site 1463B   ; OUTI
site 14658   ; OUT ($7F),A
site 146F5   ; OUT ($7F),A
site 146F9   ; OUT ($7F),A
site 1470F   ; OUT ($7F),A
site 1473C   ; OUT ($F0),A
site 14744   ; OUT ($F1),A
site 14750   ; OUT ($F0),A
site 1475E   ; OUT ($F1),A
site 147C5   ; OTIR
site 147D3   ; OUT (C),D
site 147D9   ; OUT ($F1),A
site 14814   ; OUT ($7F),A
site 14865   ; OUT ($7F),A
site 148F0   ; OUT ($7F),A
site 1490E   ; OUT ($7F),A
site 1494E   ; OUT ($7F),A
site 14958   ; OUT ($7F),A
site 149A0   ; OUT ($7F),A
mapst 0007A   ; LD ($FFFF),A
mapst 00086   ; LD ($FFFF),A
mapst 000DB   ; LD ($FFFF),A
mapst 000E6   ; LD ($FFFF),A
mapst 000F2   ; LD ($FFFF),A
mapst 00173   ; LD ($FFFF),A
mapst 0017E   ; LD ($FFFF),A
mapst 006FE   ; LD ($FFFF),A
mapst 00AFA   ; LD ($FFFF),A
mapst 00B38   ; LD ($FFFF),A
mapst 00C19   ; LD ($FFFF),A
mapst 00C98   ; LD ($FFFF),A
mapst 00CB5   ; LD ($FFFF),A
mapst 00CC3   ; LD ($FFFF),A
mapst 00D8A   ; LD ($FFFF),A
mapst 00F36   ; LD ($FFFF),A
mapst 00F9C   ; LD ($FFFF),A
mapst 00FDC   ; LD ($FFFF),A
mapst 01023   ; LD ($FFFF),A
mapst 0102D   ; LD ($FFFF),A
mapst 01056   ; LD ($FFFF),A
mapst 0106F   ; LD ($FFFF),A
mapst 0107C   ; LD ($FFFF),A
mapst 0109B   ; LD ($FFFF),A
mapst 010C4   ; LD ($FFFF),A
mapst 01127   ; LD ($FFFF),A
mapst 01423   ; LD ($FFFF),A
mapst 01499   ; LD ($FFFF),A
mapst 014BF   ; LD ($FFFF),A
mapst 0187C   ; LD ($FFFF),A
mapst 02431   ; LD ($FFFF),A
mapst 02500   ; LD ($FFFF),A
mapst 02518   ; LD ($FFFF),A
mapst 02960   ; LD ($FFFF),A
mapst 02999   ; LD ($FFFF),A
mapld 02C42   # LD HL,$FFFF; LD (HL),$02
mapst 02C50   ; LD ($FFFF),A
mapst 032A5   ; LD ($FFFF),A
mapst 03771   ; LD ($FFFF),A
mapst 03786   ; LD ($FFFF),A
mapst 037B4   ; LD ($FFFF),A
mapst 037C8   ; LD ($FFFF),A
mapst 038E9   ; LD ($FFFF),A
mapst 03907   ; LD ($FFFF),A
mapst 03919   ; LD ($FFFF),A
mapst 03928   ; LD ($FFFF),A
mapst 039A8   ; LD ($FFFF),A
mapst 039B6   ; LD ($FFFF),A
mapst 039C4   ; LD ($FFFF),A
mapst 03C97   ; LD ($FFFF),A
mapst 03CC4   ; LD ($FFFF),A
mapst 03DAE   ; LD ($FFFF),A
mapst 04250   ; LD ($FFFF),A
mapst 04269   ; LD ($FFFF),A
mapst 044EA   ; LD ($FFFF),A
mapst 0463F   ; LD ($FFFF),A
mapst 061F3   ; LD ($FFFF),A
mapst 062C5   ; LD ($FFFF),A
mapst 06334   ; LD ($FFFF),A
mapst 0642C   ; LD ($FFFF),A
mapst 0643E   ; LD ($FFFF),A
mapst 064A1   ; LD ($FFFF),A
mapst 06581   ; LD ($FFFF),A
mapst 065C8   ; LD ($FFFF),A
mapst 065D6   ; LD ($FFFF),A
mapst 065F0   ; LD ($FFFF),A
mapst 06673   ; LD ($FFFF),A
mapst 07164   ; LD ($FFFF),A
mapst 0716F   ; LD ($FFFF),A

# Aztec Adventure (World).cht and Aztec Adventure - The Golden Road to Paradise (World)
# (Action Replay).cht, "Infinite Lives": RAM $C144 is the life counter, held at 10
poke "Infinite lives"
ar 00C1-440A
endpoke

# Aztec Adventure (World).cht, "Infinite Health": RAM $C147 is the energy bar, $40 is full
poke "Infinite health"
ar 00C1-4740
endpoke

# Aztec Adventure (World).cht, "Invincibility": the byte at cart offset $1B48 is changed
# to $C9; enemy hits no longer take energy
poke "Invincibility"
gg C9B-48E-A22
endpoke

# Aztec Adventure (World).cht, "Final Level [Change "A" For Other Levels]": RAM $C146 is
# the level, 0 at the start; the game starts on the level that is held there (03 is the
# water level, 06 the cave, 0A the last level)
poke "Start level"
ar 00C1-46??
endpoke

# Aztec Adventure (World).cht, "Level Select": RAM $C1E5 = 1 turns on the game's own level
# selector on the title screen; Up and Down change the number beside the player's face and
# Button 1 starts on that level
poke "Level select"
ar 00C1-E501
endpoke

# Aztec Adventure (World).cht, "Infinite Money": RAM $C14C is the first counter of the status
# bar (the money bag), held at 9
poke "Infinite money"
ar 00C1-4C09
endpoke

# Aztec Adventure (World).cht, "Infinite Iron Balls": RAM $C14D is the second counter, held at 9
poke "Infinite iron balls"
ar 00C1-4D09
endpoke

# Aztec Adventure (World).cht, "Infinite Spears": RAM $C14E is the third counter, held at 9
poke "Infinite spears"
ar 00C1-4E09
endpoke

# Aztec Adventure (World).cht, "Infinite 4-Directional Iron Balls": RAM $C14F is the fourth
# counter, held at 9
poke "Infinite 4-way balls"
ar 00C1-4F09
endpoke

# Aztec Adventure (World).cht, "Infinite Special Items": RAM $C150 is the fifth counter, held at 9
poke "Infinite special items"
ar 00C1-5009
endpoke
