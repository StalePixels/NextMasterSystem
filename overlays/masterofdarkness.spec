# Master of Darkness (Europe, Brazil) (En), CRC32 96FB4D4B, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of round 1.
# The play screen has three line events a frame (lines 4, 9 and 30, from the handler
# at $2F99): the lines above 30 hold the clouds' H, the lines below it the play area's.
# priority: the reference log writes name table cells with the priority bit.
# hsplit: without it the right side of the play area below line 30 shows the wrong
# map columns.
# Spec gaps (data/scan-verdicts.tsv): unused are three routines in bank 0 that only
# the $0200 jump vector names, at entries nothing calls; false are byte patterns in
# data banks 2 to 13. Open are the I/O instructions in bank 1 routines (number
# printers for the status bar, the 2x2 cell writer at $4EEA and others) that object
# handler pointers reach; no static path from scanned code and no recording yet.
name Master of Darkness
cart 96FB4D4B
hz 50		; No-Intro regions Europe, Brazil
priority
hsplit
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0001A   ; OUT (C),L
site 0001C   ; OUT (C),H
site 0003A   ; IN A,($BF)
site 0029A   ; IN A,($BF)
site 002A7   ; OUT ($BF),A
site 002AB   ; OUT ($BF),A
site 002C8   ; OUT ($BF),A
site 002CC   ; OUT ($BF),A
site 002CF   ; IN A,($DC)
site 002EC   ; IN A,($DD)
site 00312   ; IN A,($BF)
site 0031D   ; OUTI
site 0031F   ; OUT (C),A
site 0032B   ; OUT ($BE),A
site 00353   ; OUT (C),L
site 00355   ; OUT (C),H
site 0035B   ; OUTD
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
site 003E0   ; OUT (C),E
site 003E2   ; OUT (C),D
site 003E7   ; OUTI
site 003E9   ; OUTD
site 003ED   ; OUTI
site 003EF   ; OUTD
site 003F3   ; OUTI
site 003F5   ; OUTD
site 003F9   ; OUTI
site 003FB   ; OUTD
site 003FF   ; OUTI
site 00401   ; OUTD
site 00405   ; OUTI
site 00407   ; OUTD
site 0040B   ; OUTI
site 0040D   ; OUTD
site 00411   ; OUTI
site 00413   ; OUTD
site 00417   ; OUTI
site 00419   ; OUTD
site 0041D   ; OUTI
site 0041F   ; OUTD
site 00423   ; OUTI
site 00425   ; OUTD
site 00429   ; OUTI
site 0042B   ; OUTD
site 0042F   ; OUTI
site 00431   ; OUTD
site 00435   ; OUTI
site 00437   ; OUTD
site 0043B   ; OUTI
site 0043D   ; OUTD
site 00441   ; OUTI
site 00443   ; OUTD
site 00447   ; OUTI
site 00449   ; OUTD
site 0044D   ; OUTI
site 0044F   ; OUTD
site 00453   ; OUTI
site 00455   ; OUTD
site 00459   ; OUTI
site 0045B   ; OUTD
site 0045F   ; OUTI
site 00461   ; OUTD
site 00465   ; OUTI
site 00467   ; OUTD
site 0046B   ; OUTI
site 0046D   ; OUTD
site 00471   ; OUTI
site 00473   ; OUTD
site 00477   ; OUTI
site 00479   ; OUTD
site 0047D   ; OUTI
site 0047F   ; OUTD
site 00483   ; OUTI
site 00485   ; OUTD
site 00489   ; OUTI
site 0048B   ; OUTD
site 0048F   ; OUTI
site 00491   ; OUTD
site 00495   ; OUTI
site 00497   ; OUTD
site 0049B   ; OUTI
site 0049D   ; OUTD
site 004A1   ; OUTI
site 004A3   ; OUTD
site 004A7   ; OUTI
site 004A9   ; OUTD
site 004AD   ; OUTI
site 004AF   ; OUTD
site 004B3   ; OUTI
site 004B5   ; OUTD
site 004B9   ; OUTI
site 004BB   ; OUTD
site 004BF   ; OUTI
site 004C1   ; OUTD
site 004C5   ; OUTI
site 004C7   ; OUTD
site 004CB   ; OUTI
site 004CD   ; OUTD
site 004D1   ; OUTI
site 004D3   ; OUTD
site 004D7   ; OUTI
site 004D9   ; OUTD
site 004DD   ; OUTI
site 004DF   ; OUTD
site 004E3   ; OUTI
site 004E5   ; OUTD
site 004E9   ; OUTI
site 004EB   ; OUTD
site 004EF   ; OUTI
site 004F1   ; OUTD
site 004F5   ; OUTI
site 004F7   ; OUTD
site 004FB   ; OUTI
site 004FD   ; OUTD
site 00501   ; OUTI
site 00503   ; OUTD
site 00507   ; OUTI
site 00509   ; OUTD
site 0050D   ; OUTI
site 0050F   ; OUTD
site 00513   ; OUTI
site 00515   ; OUTD
site 00519   ; OUTI
site 0051B   ; OUTD
site 0051F   ; OUTI
site 00521   ; OUTD
site 00525   ; OUTI
site 00527   ; OUTD
site 0052B   ; OUTI
site 0052D   ; OUTD
site 00531   ; OUTI
site 00533   ; OUTD
site 00537   ; OUTI
site 00539   ; OUTD
site 0053D   ; OUTI
site 0053F   ; OUTD
site 00543   ; OUTI
site 00545   ; OUTD
site 00549   ; OUTI
site 0054B   ; OUTD
site 0054F   ; OUTI
site 00551   ; OUTD
site 00555   ; OUTI
site 00557   ; OUTD
site 0055B   ; OUTI
site 0055D   ; OUTD
site 00561   ; OUTI
site 00563   ; OUTD
site 00586   ; OUTI
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
site 00688   ; OUTI
site 0068A   ; OUTI
site 0068C   ; OUTI
site 0068E   ; OUTI
site 00690   ; OUTI
site 00692   ; OUTI
site 00694   ; OUTI
site 00696   ; OUTI
site 00698   ; OUTI
site 0069A   ; OUTI
site 0069C   ; OUTI
site 0069E   ; OUTI
site 006A0   ; OUTI
site 006A2   ; OUTI
site 006A4   ; OUTI
site 006A6   ; OUTI
site 006A8   ; OUTI
site 006AA   ; OUTI
site 006AC   ; OUTI
site 006AE   ; OUTI
site 006B0   ; OUTI
site 006B2   ; OUTI
site 006B4   ; OUTI
site 006B6   ; OUTI
site 006B8   ; OUTI
site 006BA   ; OUTI
site 006BC   ; OUTI
site 006BE   ; OUTI
site 006C0   ; OUTI
site 006C2   ; OUTI
site 006C4   ; OUTI
site 006C6   ; OUTI
site 006C8   ; OUTI
site 006CA   ; OUTI
site 006CC   ; OUTI
site 006CE   ; OUTI
site 006D0   ; OUTI
site 006D2   ; OUTI
site 006D4   ; OUTI
site 006D6   ; OUTI
site 006D8   ; OUTI
site 006DA   ; OUTI
site 006DC   ; OUTI
site 006DE   ; OUTI
site 006E0   ; OUTI
site 006E2   ; OUTI
site 006E4   ; OUTI
site 006E6   ; OUTI
site 006E8   ; OUTI
site 006EA   ; OUTI
site 006EC   ; OUTI
site 006EE   ; OUTI
site 006F0   ; OUTI
site 006F2   ; OUTI
site 006F4   ; OUTI
site 006F6   ; OUTI
site 006F8   ; OUTI
site 006FA   ; OUTI
site 006FC   ; OUTI
site 006FE   ; OUTI
site 00700   ; OUTI
site 00702   ; OUTI
site 00704   ; OUTI
site 00706   ; OUTI
site 00708   ; OUTI
site 0070A   ; OUTI
site 0070C   ; OUTI
site 0070E   ; OUTI
site 00710   ; OUTI
site 00712   ; OUTI
site 00714   ; OUTI
site 00716   ; OUTI
site 00718   ; OUTI
site 0071A   ; OUTI
site 0071C   ; OUTI
site 0071E   ; OUTI
site 00720   ; OUTI
site 00722   ; OUTI
site 00724   ; OUTI
site 00726   ; OUTI
site 00728   ; OUTI
site 0072A   ; OUTI
site 0072C   ; OUTI
site 0072E   ; OUTI
site 00730   ; OUTI
site 00732   ; OUTI
site 00734   ; OUTI
site 00736   ; OUTI
site 00738   ; OUTI
site 0073A   ; OUTI
site 0073C   ; OUTI
site 0073E   ; OUTI
site 00740   ; OUTI
site 00742   ; OUTI
site 00744   ; OUTI
site 00746   ; OUTI
site 00748   ; OUTI
site 0074A   ; OUTI
site 0074C   ; OUTI
site 0074E   ; OUTI
site 00750   ; OUTI
site 00752   ; OUTI
site 00754   ; OUTI
site 00756   ; OUTI
site 00758   ; OUTI
site 0075A   ; OUTI
site 0075C   ; OUTI
site 0075E   ; OUTI
site 00760   ; OUTI
site 00762   ; OUTI
site 00764   ; OUTI
site 00766   ; OUTI
site 00768   ; OUTI
site 0076A   ; OUTI
site 0076C   ; OUTI
site 0076E   ; OUTI
site 00770   ; OUTI
site 00772   ; OUTI
site 00774   ; OUTI
site 00776   ; OUTI
site 00778   ; OUTI
site 0077A   ; OUTI
site 0077C   ; OUTI
site 0077E   ; OUTI
site 00780   ; OUTI
site 00782   ; OUTI
site 00784   ; OUTI
site 00786   ; OUTI
site 00788   ; OUTI
site 0078A   ; OUTI
site 0078C   ; OUTI
site 0078E   ; OUTI
site 00790   ; OUTI
site 00792   ; OUTI
site 00794   ; OUTI
site 00796   ; OUTI
site 00798   ; OUTI
site 0079A   ; OUTI
site 0079C   ; OUTI
site 0079E   ; OUTI
site 007A0   ; OUTI
site 007A2   ; OUTI
site 007A4   ; OUTI
site 007A6   ; OUTI
site 007A8   ; OUTI
site 007AA   ; OUTI
site 007AC   ; OUTI
site 007AE   ; OUTI
site 007B0   ; OUTI
site 007B2   ; OUTI
site 007B4   ; OUTI
site 007B6   ; OUTI
site 007B8   ; OUTI
site 007BA   ; OUTI
site 007BC   ; OUTI
site 007BE   ; OUTI
site 007C0   ; OUTI
site 007C2   ; OUTI
site 007C4   ; OUTI
site 007C6   ; OUTI
site 007C8   ; OUTI
site 007CA   ; OUTI
site 007CC   ; OUTI
site 007CE   ; OUTI
site 007D0   ; OUTI
site 007D2   ; OUTI
site 007D4   ; OUTI
site 007D6   ; OUTI
site 007D8   ; OUTI
site 007DA   ; OUTI
site 007DC   ; OUTI
site 007DE   ; OUTI
site 007E0   ; OUTI
site 007E2   ; OUTI
site 007E4   ; OUTI
site 007E6   ; OUTI
site 007E8   ; OUTI
site 007EA   ; OUTI
site 007EC   ; OUTI
site 007EE   ; OUTI
site 007F0   ; OUTI
site 007F2   ; OUTI
site 007F4   ; OUTI
site 007F6   ; OUTI
site 007F8   ; OUTI
site 007FA   ; OUTI
site 007FC   ; OUTI
site 007FE   ; OUTI
site 00800   ; OUTI
site 00802   ; OUTI
site 00804   ; OUTI
site 00806   ; OUTI
site 00808   ; OUTI
site 0080A   ; OUTI
site 0080C   ; OUTI
site 0080E   ; OUTI
site 00810   ; OUTI
site 00812   ; OUTI
site 00814   ; OUTI
site 00816   ; OUTI
site 00818   ; OUTI
site 0081A   ; OUTI
site 0081C   ; OUTI
site 0081E   ; OUTI
site 00820   ; OUTI
site 00822   ; OUTI
site 00824   ; OUTI
site 00826   ; OUTI
site 00828   ; OUTI
site 0082A   ; OUTI
site 0082C   ; OUTI
site 0082E   ; OUTI
site 00830   ; OUTI
site 00832   ; OUTI
site 00834   ; OUTI
site 00836   ; OUTI
site 00838   ; OUTI
site 0083A   ; OUTI
site 0083C   ; OUTI
site 0083E   ; OUTI
site 00840   ; OUTI
site 00842   ; OUTI
site 00844   ; OUTI
site 00846   ; OUTI
site 00848   ; OUTI
site 0084A   ; OUTI
site 0084C   ; OUTI
site 0084E   ; OUTI
site 00850   ; OUTI
site 00852   ; OUTI
site 00854   ; OUTI
site 00856   ; OUTI
site 00858   ; OUTI
site 0085A   ; OUTI
site 0085C   ; OUTI
site 0085E   ; OUTI
site 00860   ; OUTI
site 00862   ; OUTI
site 00864   ; OUTI
site 00866   ; OUTI
site 00868   ; OUTI
site 0086A   ; OUTI
site 0086C   ; OUTI
site 0086E   ; OUTI
site 00870   ; OUTI
site 00872   ; OUTI
site 00874   ; OUTI
site 00876   ; OUTI
site 00878   ; OUTI
site 0087A   ; OUTI
site 0087C   ; OUTI
site 0087E   ; OUTI
site 00880   ; OUTI
site 00882   ; OUTI
site 00884   ; OUTI
site 00886   ; OUTI
site 00888   ; OUTI
site 0088A   ; OUTI
site 0088C   ; OUTI
site 0088E   ; OUTI
site 00890   ; OUTI
site 00892   ; OUTI
site 00894   ; OUTI
site 00896   ; OUTI
site 00898   ; OUTI
site 0089A   ; OUTI
site 0089C   ; OUTI
site 0089E   ; OUTI
site 008A0   ; OUTI
site 008A2   ; OUTI
site 008A4   ; OUTI
site 008A6   ; OUTI
site 008A8   ; OUTI
site 008AA   ; OUTI
site 008AC   ; OUTI
site 008AE   ; OUTI
site 008B0   ; OUTI
site 008B2   ; OUTI
site 008B4   ; OUTI
site 008B6   ; OUTI
site 008B8   ; OUTI
site 008BA   ; OUTI
site 008BC   ; OUTI
site 008BE   ; OUTI
site 008C0   ; OUTI
site 008C2   ; OUTI
site 008C4   ; OUTI
site 008DF   ; OUT ($BE),A
site 008E5   ; OUT ($BE),A
site 008F7   ; OUTI
site 008F9   ; OUT ($BE),A
site 00910   ; OUTI
site 00915   ; OUT ($BE),A
site 0093C   ; OUT (C),E
site 00942   ; OUT (C),D
site 00980   ; OUT ($BE),A
site 00985   ; OUT ($BE),A
site 0098A   ; OUT ($BE),A
site 0098F   ; OUT ($BE),A
site 00994   ; OUT ($BE),A
site 00999   ; OUT ($BE),A
site 0099E   ; OUT ($BE),A
site 009A3   ; OUT ($BE),A
site 009A8   ; OUT ($BE),A
site 009AD   ; OUT ($BE),A
site 009B2   ; OUT ($BE),A
site 009B7   ; OUT ($BE),A
site 009BC   ; OUT ($BE),A
site 009C1   ; OUT ($BE),A
site 009C6   ; OUT ($BE),A
site 009CB   ; OUT ($BE),A
site 009D0   ; OUT ($BE),A
site 009D5   ; OUT ($BE),A
site 009DA   ; OUT ($BE),A
site 009DF   ; OUT ($BE),A
site 009E4   ; OUT ($BE),A
site 009E9   ; OUT ($BE),A
site 009EE   ; OUT ($BE),A
site 009F3   ; OUT ($BE),A
site 009F8   ; OUT ($BE),A
site 009FD   ; OUT ($BE),A
site 00A02   ; OUT ($BE),A
site 00A07   ; OUT ($BE),A
site 00A0C   ; OUT ($BE),A
site 00A11   ; OUT ($BE),A
site 00A16   ; OUT ($BE),A
site 00A1B   ; OUT ($BE),A
site 00B7E   ; OUT (C),E
site 00B80   ; OUT (C),D
site 00BCA   ; OUT ($BE),A
site 00C13   ; OUT ($BE),A
site 00C34   ; OUT ($BE),A
site 00C59   ; IN A,($DD)
site 00CE4   ; OUT (C),H
site 00D06   ; OUT (C),L
site 00D08   ; OUT (C),H
site 01370   ; OUT ($BF),A
site 01374   ; OUT ($BF),A
site 02F09   ; OUT ($BF),A
site 02F0D   ; OUT ($BF),A
site 02F10   ; OUT ($BF),A
site 02F14   ; OUT ($BF),A
site 02F18   ; OUT ($BF),A
site 02F1C   ; OUT ($BF),A
site 02F36   ; OUT (C),L
site 02F38   ; OUT (C),H
site 02F40   ; OUT ($BE),A
site 02F49   ; OUT ($BE),A
site 02F5C   ; OUT ($BF),A
site 02F60   ; OUT ($BF),A
site 02F7B   ; OUT ($BF),A
site 02F7F   ; OUT ($BF),A
site 02F82   ; OUT ($BF),A
site 02F86   ; OUT ($BF),A
site 02F8A   ; OUT ($BF),A
site 02F8E   ; OUT ($BF),A
site 02FA2   ; OUT ($BF),A
site 02FA6   ; OUT ($BF),A
# The line handler $2F99 writes register 10 from the table at $C6D0 (14 FF 00, from
# $2EE4): $14 at line 4, $FF at line 9, $00 at line 30. On the Master System the $00
# write changes nothing in that picture: the counter reloads only when it runs out,
# and it was reloaded with $FF at line 30; the frame handler writes $04 in the blank.
# The runtime schedules an event on the next line for a register 10 write in the
# picture when none is scheduled (ev_recheck2), so each handler call writes $00 again
# and line events run every few lines to the bottom, each writing H = $00: a band of
# lines under the play area's split shows the wrong H. The handler skips a write of
# $00 to register 10; the two writes go to a cave in the unused bytes at $7FA0.
label r10cave 07FA0
asm 02FB0 6   ; OUT ($BF),A : LD A,$8A : OUT ($BF),A
    or a
    jp nz,r10cave
    nop
    nop
endasm
asm 07FA0 9   ; unused $00 bytes before the header: r10cave
    rst $00
    db $05          ; OUT ($BF),A
    ld a,$8A
    rst $00
    db $05          ; OUT ($BF),A
    jp $2FB6
endasm
# The frame handler keeps interrupts off from $0038 to the EI at $0C72, and the
# runtime's once-a-frame work comes at the ULA interrupt after it. Both must end before
# the line event at line 4: when either runs late, the three events come late and a band
# at the top of the play area (lines 31 to about 60) shows the clouds' H. Through the
# traps, five VRAM writers in that part took most of the time: the name table column at
# $2F2B (20 cells, about 103,000 Next cycles, each time the map scrolls 8 pixels), the
# sprite table at $0345 (in reverse order every second frame, about 58,000), the tiles at
# $0D01 (416 bytes) and $0CDD (A x 32 bytes), and the palette at $057C. Page 0 does each
# with jt_vwrite, and the palette with CRAM writes of only the entries that changed.
asm 00345 6   ; LD HL,$DFF9 : INC (HL) : BIT 0,(HL)
    rst $00
    db far_io, pg_sat, ent_sat
    ret
endasm
asm 02F2B 6   ; LD HL,($C6AE) : LD DE,$C680
    rst $00
    db far_io, pg_col, ent_col
    ret
endasm
asm 0057C 7   ; LD HL,$C000 : RST $18 : LD HL,$C3E0
    rst $00
    db far_io, pg_pal, ent_pal
    ret
endasm
asm 00D01 5   ; LD HL,$4020 : LD C,$BF
    rst $00
    db far_io, pg_tl416, ent_tl416
    ret
endasm
asm 00CDD 7   ; LD HL,($C726) : LD C,$BF : OUT (C),L (the copy runs to $0CF1)
    rst $00
    db far_io, pg_tlcopy, ent_tlcopy
    jp $0CF2
endasm
page 0 sat col pal tl416 tlcopy
; Each entry does what the game's routine does: the same VRAM and CRAM contents and VDP
; state after it, and the registers the game's routine leaves (noted for each). The game
; calls all five with interrupts off (the frame handler, and its other callers, turn them
; off first). sat, col, tl416 and tlcopy run on the page's own stack; they turn interrupts
; off themselves if they find them on, and on again just before RET, on the game's stack.
; Runtime entries used: jt_vwrite, cram, vdp_addr, vdp_code, vdp_latch, vdp_rbuf.

; ENTER: interrupts off, then the page's own stack. Keeps every register but F.
    macro ENTER
        ld (sv_a),a
        ld a,i                  ; P/V = IFF2
        di
        ld a,0
        jp po,$+4
        inc a
        ld (sv_ie),a
        ld (sv_sp),sp
        ld sp,pstk
        ld a,(sv_a)
    endm
; leave: back to the game's stack and its interrupt state, then RET. Keeps every register.
leave:  push af
        ld a,(sv_ie)
        or a
        jr z,.di
        pop af
        ld sp,(sv_sp)
        ei
        ret
.di:    pop af
        ld sp,(sv_sp)
        ret

; sat: the game's $0345-$0567 and $0568-$08C6. ($DFF9) + 1; with bit 0 set, the 64 Y
; values from $C33F down to $C300 go to VRAM $3F00 and the 64 X and tile pairs from
; ($C3BE, $C3BF) down to ($C340, $C341) to $3F80; with bit 0 clear, $C300-$C33F go to
; $3F00 and $C340-$C3BF to $3F80. Leaves B + 64 and C = $BE; HL = $C33E and DE = $7F80
; with bit 0 set, HL = $C3C0 and DE as it was with bit 0 clear; A as it was.
sat:    ENTER
        push bc
        push de
        push ix
        push iy
        ld hl,$DFF9
        inc (hl)
        bit 0,(hl)
        jr z,.fwd
        ld hl,$C33F
        ld de,ybuf
        ld b,64
.y:     ld a,(hl)
        ld (de),a
        dec l
        inc e
        djnz .y
        ld hl,$C3BE
        ld de,xbuf
        ld b,64
.x:     ld a,(hl)
        ld (de),a
        inc l
        inc e
        ld a,(hl)
        ld (de),a
        inc e
        dec l
        dec l
        dec l
        djnz .x
        ld hl,ybuf
        ld de,xbuf
        ld a,1                  ; the source as mapped now: the buffers are in this page
        call send
        pop iy
        pop ix
        pop de
        ld hl,$C33E
        ld de,$7F80
        jr .out
.fwd:   ld hl,$C300
        ld de,$C340
        ld a,1
        call send
        pop iy
        pop ix
        pop de
        ld hl,$C3C0
.out:   pop bc
        ld a,b
        add a,64
        ld b,a
        ld c,$BE
        ld a,(sv_a)
        jp leave
; send: 64 bytes from HL to VRAM $3F00, then 128 bytes from DE to $3F80; A as for jt_vwrite.
send:   push de
        push af
        ld de,$3F00
        ld bc,$4001             ; one run of 64 bytes
        ld ix,64
        ld iy,64
        call jt_vwrite
        pop af
        pop hl
        ld de,$3F80
        ld bc,$8001             ; one run of 128 bytes
        ld ix,128
        ld iy,128
        jp jt_vwrite

; col: the game's $2F2B-$2F56. The 20 tiles at $C680 go to the name table column at
; ($C6AE), one cell each 64 bytes, with the high byte $01 for a tile below ($C6A6) and $11
; (priority) for the others; then ($C6B0) = 0. Leaves A = 0 and F as XOR A, B = 0, C as it
; was, DE = $C694, HL = ($C6AE) + $500.
col:    ENTER
        push bc
        push ix
        push iy
        ld a,($C6A6)
        ld c,a
        ld hl,$C680
        ld de,cbuf
        ld b,20
.c:     ld a,(hl)
        inc hl
        ld (de),a
        inc e
        cp c
        ld a,$01
        jr c,.lo
        or $10
.lo:    ld (de),a
        inc e
        djnz .c
        ld hl,($C6AE)
        ld d,h
        ld e,l
        push hl
        ld hl,cbuf
        ld bc,$0214             ; 20 runs of 2 bytes
        ld ix,2
        ld iy,64
        ld a,1
        call jt_vwrite
        pop hl
        ld de,$0500
        add hl,de
        ld de,$C694
        pop iy
        pop ix
        pop bc
        ld b,0
        xor a
        ld ($C6B0),a
        jp leave

; pal: the game's $057C-$0583 and the 32 OUTI at $0886: the 32 bytes at $C3E0 to CRAM
; 0-31. Writes only the entries whose colour differs from cram; the VDP state is then as
; the 32 writes leave it: address 32, code 3, latch clear, read buffer the last byte.
; Leaves HL = $C400, B - 32, C = $BE. Uses the game's stack as the game's code does.
pal:    push de
        ld a,b
        sub 32
        push af
        ld hl,$C3E0
        ld c,0
        ld b,32
        ld de,cram
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
        pop af
        ld b,a
        ld c,$BE
        pop de
        ret

; tl416: the game's $0D01-$0D15: the 416 bytes at $DA00 to VRAM $0020, then ($C901) = 0.
; Leaves A = 0 and F as XOR A, HL = $DBA0, B + 96, C = $BE.
tl416:  ENTER
        push bc
        push de
        push ix
        push iy
        ld hl,$DA00
        ld de,$0020
        ld bc,$D002             ; 2 runs of 208 bytes
        ld ix,208
        ld iy,208
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        pop de
        pop bc
        ld a,b
        add a,96
        ld b,a
        ld c,$BE
        ld hl,$DBA0
        xor a
        ld ($C901),a
        jp leave

; tlcopy: the game's $0CDD-$0CF1, entered with A' = n (1 to 255), the count of 32-byte
; blocks: the 32 x n bytes at ($C728), as the game sees them with its banks, to VRAM
; ($C726). Leaves A' as A was at the entry, A = 0, HL = ($C728) + 32 x n, B - 32 x n,
; C = $BE.
tlcopy: ENTER
        ex af,af'
        push de
        push ix
        push iy
        ld (sv_n),a
        ld c,a                  ; n runs
        ld a,b
        ld (sv_b),a
        ld de,($C726)
        ld hl,($C728)
        ld b,32                 ; of 32 bytes
        ld ix,32
        ld iy,32
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,(sv_n)
        ld e,a
        ld d,0
        ex de,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl               ; 32 x n
        ld a,(sv_b)
        sub l
        ld b,a
        add hl,de
        ld c,$BE
        pop iy
        pop ix
        pop de
        xor a
        jp leave

sv_a:   db 0
sv_ie:  db 0
sv_sp:  dw 0
sv_n:   db 0
sv_b:   db 0
        ds 64
pstk:
        align 256
ybuf:   ds 64
cbuf:   ds 40
        align 256
xbuf:   ds 128
endpage
site 04820   ; OUT ($BE),A
site 04824   ; OUT ($BE),A
site 0482D   ; OUT ($BE),A
site 04831   ; OUT ($BE),A
site 04842   ; OUT ($BE),A
site 04846   ; OUT ($BE),A
site 0484B   ; OUT ($BE),A
site 0484F   ; OUT ($BE),A
site 0485B   ; OUT (C),E
site 0485D   ; OUT (C),D
site 04860   ; OUT (C),E
site 04862   ; OUT (C),D
site 04876   ; OUT (C),E
site 04878   ; OUT (C),D
site 0487B   ; OUT (C),E
site 0487D   ; OUT (C),D
site 04891   ; OUT (C),E
site 04893   ; OUT (C),D
site 04896   ; OUT (C),E
site 04898   ; OUT (C),D
site 048B9   ; OUT ($BE),A
site 048BD   ; OUT ($BE),A
site 04A44   ; OUT ($BE),A
site 04A4A   ; OUT ($BE),A
site 04AD4   ; OUT (C),E
site 04ADA   ; OUT (C),D
site 04AE2   ; OUT (C),E
site 04AE8   ; OUT (C),D
site 04BBB   ; OUT ($BE),A
site 04BC1   ; OUT ($BE),A
site 04E8B   ; OUT ($BE),A
site 04E94   ; OUT ($BE),A
site 04FF3   ; OUT (C),A
site 0C036   ; OUT ($3F),A
site 0C038   ; IN A,($DD)
site 0C042   ; OUT ($3F),A
site 0C044   ; IN A,($DD)
site 0C094   ; OUT ($3E),A
site 0C097   ; OUT ($F2),A
site 0C09F   ; OUT ($3E),A
site 0C0A3   ; OUT ($3F),A
site 0C0A9   ; IN A,($BF)
site 0C0AB   ; IN A,($BF)
site 0C0B7   ; IN A,($BF)
site 0C1BC   ; OUT (C),A
site 0C1C3   ; OUT (C),A
site 0C277   ; OUT (C),D
site 0C27F   ; OUT (C),A
site 0C488   ; OUT ($BE),A
site 0C48D   ; OUT ($BE),A
site 0C5D1   ; OUT ($BF),A
site 0C5D7   ; OUT ($BF),A
site 0C6F1   ; OUT ($BE),A
site 0C6F7   ; OUT ($BE),A
site 0C7C7   ; OUT (C),A
site 0C7CC   ; OUT (C),A
site 0C973   ; OUT (C),A
site 0C979   ; OUT (C),A
site 0CE21   ; OUT (C),A
site 0CE27   ; OUT (C),A
site 0EAED   ; OUT ($BF),A
site 0EAF1   ; OUT ($BF),A
site 0EC95   ; OUT ($BF),A
site 0EC9B   ; OUT ($BF),A
site 0ECB1   ; OUT ($BF),A
site 0ECB7   ; OUT ($BF),A
site 0FA00   ; OUT (C),A
site 0FA04   ; OUT (C),A
site 0FA0F   ; OUT (C),A
site 0FA13   ; OUT (C),A
site 0FD35   ; OUT ($BE),A
site 0FD3B   ; OUT ($BE),A
site 0FD42   ; OUT ($BE),A
site 0FD48   ; OUT ($BE),A
site 0FD51   ; OUT ($BE),A
site 0FD57   ; OUT ($BE),A
site 241E2   ; OUT ($7F),A
site 24308   ; OUT ($7F),A
site 2449A   ; OTIR
site 245B2   ; OUT ($7F),A
site 245BC   ; OUT ($7F),A
site 245D9   ; OUT ($7F),A
site 246DD   ; OUT ($7F),A
site 247BA   ; OUT ($7F),A
site 2485C   ; OUT ($7F),A
site 24865   ; OUT ($7F),A
site 24875   ; OUT ($7F),A
site 248F1   ; OUT ($7F),A
mapldk 0007A   # LD HL,$FFFC; LD (HL),$00
maphl 00080   # LD (HL),$00, HL = $FFFD
maphl 00083   # LD (HL),$01, HL = $FFFE
maphl 00086   # LD (HL),$02, HL = $FFFF
mapst 00098   ; LD ($FFFF),A
mapst 0028F   ; LD ($FFFF),A
mapst 00296   ; LD ($FFFF),A
mapst 00968   ; LD ($FFFF),A
mapst 00A22   ; LD ($FFFF),A
mapst 00A35   ; LD ($FFFF),A
mapst 00B5B   ; LD ($FFFF),A
mapst 00B6B   ; LD ($FFFF),A
mapst 00C75   ; LD ($FFFF),A
mapst 00C94   ; LD ($FFFF),A
mapst 00CDA   ; LD ($FFFF),A
mapst 00CF3   ; LD ($FFFF),A
mapst 0127D   ; LD ($FFFF),A
mapst 012AE   ; LD ($FFFF),A
mapst 013CC   ; LD ($FFFF),A
mapst 025A5   ; LD ($FFFF),A
mapst 02656   ; LD ($FFFF),A
mapst 02669   ; LD ($FFFF),A
mapst 029B0   ; LD ($FFFF),A
mapst 02B5B   ; LD ($FFFF),A
mapst 02B6A   ; LD ($FFFF),A
mapst 02B7F   ; LD ($FFFF),A
mapst 02BA1   ; LD ($FFFF),A
mapst 02CEE   ; LD ($FFFF),A
mapst 02D3B   ; LD ($FFFF),A
mapst 02D46   ; LD ($FFFF),A
mapst 02D94   ; LD ($FFFF),A
mapst 03CA3   ; LD ($FFFF),A
mapst 03CBF   ; LD ($FFFF),A
mapst 04035   ; LD ($FFFF),A
mapst 04055   ; LD ($FFFF),A
mapst 04757   ; LD ($FFFF),A
mapst 04769   ; LD ($FFFF),A
mapst 04E34   ; LD ($FFFF),A
mapst 04EA3   ; LD ($FFFF),A
mapst 05002   ; LD ($FFFF),A
mapst 0509F   ; LD ($FFFF),A
mapst 050AD   ; LD ($FFFF),A
mapst 052BA   ; LD ($FFFF),A
mapst 052D6   ; LD ($FFFF),A
# CHECK cartarea_store at 24A99 ($8A99 bank 9): 02  LD (BC),A $8103
# CHECK cartarea_store at 24A9B ($8A9B bank 9): 02  LD (BC),A $8203
# CHECK cartarea_store at 24B1C ($8B1C bank 9): 02  LD (BC),A $0403
# CHECK cartarea_store at 24B25 ($8B25 bank 9): 02  LD (BC),A $0402
# CHECK cartarea_store at 24B29 ($8B29 bank 9): 02  LD (BC),A $0100
# CHECK cartarea_store at 24B2A ($8B2A bank 9): 02  LD (BC),A $0100
# CHECK cartarea_store at 24B31 ($8B31 bank 9): 02  LD (BC),A $0202
# CHECK cartarea_store at 24B37 ($8B37 bank 9): 02  LD (BC),A $0201
# CHECK cartarea_store at 24B38 ($8B38 bank 9): 02  LD (BC),A $0201
# CHECK cartarea_store at 24B39 ($8B39 bank 9): 02  LD (BC),A $0201
# CHECK cartarea_store at 24B5F ($8B5F bank 9): 02  LD (BC),A $0201
# CHECK cartarea_store at 24B60 ($8B60 bank 9): 02  LD (BC),A $0201
# CHECK cartarea_store at 24B6E ($8B6E bank 9): 02  LD (BC),A $0101
# CHECK cartarea_store at 24B71 ($8B71 bank 9): 02  LD (BC),A $0202
# CHECK cartarea_store at 24B72 ($8B72 bank 9): 02  LD (BC),A $0202
# CHECK cartarea_store at 24B75 ($8B75 bank 9): 02  LD (BC),A $0302
# CHECK cartarea_store at 24B76 ($8B76 bank 9): 02  LD (BC),A $0302
# CHECK cartarea_store at 24B7B ($8B7B bank 9): 02  LD (BC),A $0304
# CHECK cartarea_store at 24B90 ($8B90 bank 9): 02  LD (BC),A $0604
# CHECK cartarea_store at 24B91 ($8B91 bank 9): 02  LD (BC),A $0604
# CHECK cartarea_store at 24B92 ($8B92 bank 9): 02  LD (BC),A $0604
# CHECK cartarea_store at 24B9E ($8B9E bank 9): 02  LD (BC),A $0403
# CHECK cartarea_store at 24BEA ($8BEA bank 9): 02  LD (BC),A $0C00
# CHECK cartarea_store at 24C04 ($8C04 bank 9): 22 9B 01  LD ($019B),HL $019B,$019C
# CHECK cartarea_store at 24D09 ($8D09 bank 9): 02  LD (BC),A $8104
# CHECK cartarea_store at 24D12 ($8D12 bank 9): 02  LD (BC),A $8105
# CHECK cartarea_store at 24D1B ($8D1B bank 9): 02  LD (BC),A $0602
# CHECK ram_exec at 24CFD ($8CFD bank 9): E4 01 F7  CALL PO,$F701 $F701
# CHECK indirect_unresolved at 0009F ($009F bank 0): CD 07 00  CALL $0007 
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00A60   # LD ($FFFF),A; JP/CALL target from $28E6F; 32 bytes of valid code before it
mapst 00A7A   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 04EF3   # LD ($FFFF),A; after LD A,($C6A2); 32 bytes of valid code before it
mapst 04F5A   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 05030   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 0556D   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 0559D   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 055F6   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 05610   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 0565B   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 0584C   # LD ($FFFF),A; after LD A,($C6A2); 32 bytes of valid code before it
mapst 058C1   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 05DC3   # LD ($FFFF),A; after LD A,($C6A2); 32 bytes of valid code before it
mapst 05E08   # LD ($FFFF),A; after POP AF; JP/CALL target from $1F1AB; 32 bytes of valid code before it
mapst 07473   # LD ($FFFF),A; after LD A,$0F; 32 bytes of valid code before it
mapst 074AC   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
# CHECK byte scan low: mapst 2ABB1  LD ($FFFF),A  (no valid code after it)
# CHECK byte scan low: mapst 349AC  LD ($FFFF),A  (32 bytes of valid code before it; no valid code after it)
# CHECK high: site 008CD  OTIR  (port in C; branch target from $297D6 $2997A; 32 bytes of valid code before it)
# CHECK high: site 00927  OUT (C),E  (port in C; branch target from $0092B; 32 bytes of valid code before it)
# CHECK medium: site 00929  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00A6B  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK low: site 03EC7  OUT ($3E),A  (memory_control; no evidence)
# CHECK medium: site 04A6B  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 04A71  OUT ($BE),A  (vdp_data; after LD A,$09; 32 bytes of valid code before it)
# CHECK medium: site 04A78  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 04A7E  OUT ($BE),A  (vdp_data; after LD A,$09; 32 bytes of valid code before it)
# CHECK medium: site 04AA5  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 04AAB  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 04AB2  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 04AB8  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 04ABF  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 04AC5  OUT ($BE),A  (vdp_data; branch target from $3558A; 32 bytes of valid code before it)
# CHECK medium: site 04B00  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 04B06  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 04B0E  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 04B14  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 04B2C  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 04B32  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 04B3A  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 04B40  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK high: site 04F0D  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK high: site 04F18  OUT ($BE),A  (vdp_data; branch target from $04F14; 32 bytes of valid code before it)
# CHECK high: site 04F1E  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK high: site 04F29  OUT ($BE),A  (vdp_data; branch target from $04F25; 32 bytes of valid code before it)
# CHECK high: site 04F3A  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK high: site 04F45  OUT ($BE),A  (vdp_data; branch target from $04F41; 32 bytes of valid code before it)
# CHECK high: site 04F4B  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK high: site 04F56  OUT ($BE),A  (vdp_data; branch target from $04F52; 32 bytes of valid code before it)
# CHECK high: site 05020  OUT ($BE),A  (vdp_data; after LD A,(DE); 32 bytes of valid code before it)
# CHECK medium: site 05776  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 0577C  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 0581E  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 05825  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 058A1  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 058AA  OUT ($BE),A  (vdp_data; branch target from $058A6; 32 bytes of valid code before it)
# CHECK medium: site 05F0D  IN A,($3E)  (unmapped_read; branch target from $23A8E)
# CHECK low: site 06041  OUT ($DD),A  (no_effect; no evidence)
# CHECK medium: site 067C2  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 067C8  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 07277  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 0727D  OUT ($BF),A  (vdp_control; after POP AF; 32 bytes of valid code before it)
# CHECK medium: site 07325  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 0747C  OUT (C),L  (port in C; 32 bytes of valid code before it)
# CHECK high: site 07482  OUT (C),H  (port in C; branch target from $0740B; 32 bytes of valid code before it)
# CHECK medium: site 07486  OUTI  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 0748C  OUTI  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 07492  OUTI  (port in C; 32 bytes of valid code before it)
# CHECK high: site 07498  OUTI  (port in C; branch target from $2932F; 32 bytes of valid code before it)
# CHECK medium: site 075CF  OUT (C),L  (port in C; 32 bytes of valid code before it)
# CHECK high: site 075D5  OUT (C),H  (port in C; branch target from $07613 $07605; 32 bytes of valid code before it)
# CHECK medium: site 075D8  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 075DE  OUT ($BE),A  (vdp_data; branch target from $0429C; 32 bytes of valid code before it)
# CHECK medium: site 075E4  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 075EA  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 0BD86  OUT ($C0),A  (no_effect; no evidence)
# CHECK medium: site 0BEAF  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 12D02  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 12D07  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 12D0B  IN A,($DC)  (joypad_a; branch target from $12C8B; no valid code after it)
# CHECK low: site 12D94  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 12E34  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 12E36  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 12ED3  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 12ED5  IN A,($DD)  (joypad_b_misc; no valid code after it)
# CHECK low: site 12F71  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 12F73  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 13002  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 1301D  IN A,($DC)  (joypad_a; 6 RST or NOP opcodes around it (looks like data); 28 bytes of valid code before it)
# CHECK low: site 130E0  IN A,($DC)  (joypad_a; 16 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 130EC  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 153D9  IN A,($DC)  (joypad_a; no evidence)
# CHECK medium: site 1540D  IN A,($F2)  (fm_detect; 32 bytes of valid code before it)
# CHECK low: site 16E76  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 17021  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 17180  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 171FC  OUTI  (port in C; no evidence)
# CHECK low: site 17226  OUTI  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 17A67  INDR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 17BE3  OTDR  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 1C5F2  OUT ($C1),A  (no_effect; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1C865  IN A,($C1)  (joypad_b_misc; 4 RST or NOP opcodes around it (looks like data); 21 bytes of valid code before it)
# CHECK low: site 1D887  IN A,($3F)  (unmapped_read; no valid code after it)
# CHECK low: site 1DE64  IN H,(C)  (port in C; no evidence)
# CHECK low: site 1DE68  OUT (C),H  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 20D21  IN C,(C)  (port in C; 14 bytes of valid code before it; no valid code after it)
# CHECK low: site 21094  IN A,($C1)  (joypad_b_misc; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 214E2  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK low: site 2218A  IN E,(C)  (port in C; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 23AF5  IN B,(C)  (port in C; 10 bytes of valid code before it)
# CHECK medium: site 23C03  IN C,(C)  (port in C; 32 bytes of valid code before it)
# CHECK low: site 29EFB  IN A,($C0)  (joypad_a; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 2AA57  IN A,($3E)  (unmapped_read; 32 bytes of valid code before it)
# CHECK low: site 30BB1  IN B,(C)  (port in C; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 30BF9  INIR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 321E4  IN B,(C)  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 3249C  IN H,(C)  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 337CC  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK medium: site 355CB  OUT (C),L  (port in C; branch target from $3561F)
# CHECK low: site 356C7  INI  (port in C; no evidence)
# CHECK low: site 35A84  IN A,($3E)  (unmapped_read; branch target from $35AB5; 25 bytes of valid code before it; no valid code after it)
# CHECK medium: site 3600C  IN A,($7F)  (h_counter; branch target from $342AE $35FFB)
# CHECK low: site 3F3BC  OUT ($7E),A  (psg; no valid code after it)

# Master of Darkness (Europe, Brazil).cht: "Infinite Lives"
poke "Infinite lives"
ar 00DF-BA03
endpoke

# Master of Darkness (Europe, Brazil).cht: "Infinite Energy"
poke "Infinite energy"
ar 00CA-3A20
endpoke

# Master of Darkness (Europe, Brazil).cht: "Invincible"
poke "Invincibility"
ar 00DF-B463
endpoke

# Master of Darkness (Europe, Brazil).cht: "Freeze Timer"
poke "Infinite time"
ar 00DF-C21E
endpoke

# Master of Darkness (Europe, Brazil).cht: "Infinite Ammo"
poke "Infinite ammo"
ar 00DF-B963
endpoke

# Master of Darkness (Europe, Brazil).cht: "Start with ?? Lives, instead of 3"
poke "Start lives"
gg ??2-857-E66
endpoke

# Master of Darkness (Europe, Brazil).cht: "Press 1 or 2 on Title Screen for Debug Menu"
poke "Debug menu"
gg 000-EB7-2AE
endpoke
