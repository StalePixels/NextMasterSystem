# Desert Strike (Europe) (En,Fr,De,Es), CRC32 6C1433F9, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of
# random input, 180 s with no input).
# Decisions:
# - No RST vector has $FF filler, so $0000-$0002 (DI; XOR A; the first byte of IM 1) is
#   the io vector and the game starts at $0004 (DI; LD SP,$DFF0).
# - Most VDP code runs from RAM: bank 0 copies blocks of banks 9 and 10 to $D300 with
#   LDIR and calls them. The site lines patch the ROM bytes of each copy, and the copies
#   in RAM carry the patches.
# - In play the routine $48C9 copies 17 tiles (544 bytes) from cart ROM to VRAM $3000 with
#   an unrolled loop of OUTI, which the trace splits into two runtime calls a pass, so no
#   call holds a whole tile. The cave at $48E4 far-calls page 0 (ds_tiles), which writes
#   the same bytes as OTIR blocks of whole aligned tiles; with tilecache the runtime
#   copies them from the converted cart. The OUTI after the cave no longer run; their
#   site lines stay so that the scan's rows are covered.
# - tilecache: frame loads in play (game frames 1900-6000, the same input) go from 35
#   frames over 100% to 12, at the cost of about 2.2 s more loading at game start.
# - The interrupt handler $330D does the map scroll, the sprite table, the tile upload
#   queue and the map objects' name table rows through the runtime, one trap for each
#   byte or cell. In busy play it ran past its frame and the game lost steps (1919 game
#   steps against the reference's 2000 over frames 3000-7000 of a scripted flight). Page
#   code does the same work: the map column $37A4-$3FBA and row $4027-$48C5 (dscol,
#   dsrow), the object rows $0F7C-$0FEB (dsnr) and the sprite table $3439-$36B0 (dsspr)
#   with jt_vwrite, and the tile upload loops $11B9 and $1227 (dstq) as OTIR blocks of
#   whole tiles for tilecache. The game then makes all 2000 steps, and no play frame
#   runs over 100%. The site lines of the replaced loops stay, so that the scan's rows
#   are covered.
# - $0071-$00B8 is a call gate that maps cart RAM at $8000 ($FFFC = $28) around calls
#   into it. No code that the scan or the recordings reached writes $FFFC after start;
#   its mapper stores are patched as real code.
# - $26AC and $26E0 restore the bank after the sound driver call at $26A3 and $26D7, as
#   $2678 does after $266F.
# - The I/O byte patterns that no path reached are data: bank 6 ($1B6F5, $1B705) is tile
#   graphics and bank 18 ($4A3A1-$4A6C7) is graphics data; no code runs in either bank.
name Desert Strike
cart 6C1433F9
hz 50		; No-Intro region Europe
vector 00 io
start 0004
tilecache
site 00254   ; OUT ($BF),A
site 0025B   ; OUT ($BF),A
site 00262   ; OUT ($BF),A
site 00269   ; OUT ($BF),A
site 00270   ; OUT ($BF),A
site 00277   ; OUT ($BF),A
site 0027E   ; OUT ($BF),A
site 00285   ; OUT ($BF),A
site 0028C   ; OUT ($BF),A
site 00293   ; OUT ($BF),A
site 002B7   ; OUT ($BF),A
site 002BE   ; OUT ($BF),A
site 002C5   ; OUT ($BE),A
site 002CE   ; OTIR
site 0032F   ; OUT ($BF),A
site 00336   ; OUT ($BF),A
site 0033D   ; OUT ($BF),A
site 00344   ; OUT ($BF),A
site 0034B   ; OUT ($BF),A
site 00352   ; OUT ($BF),A
site 00359   ; OUT ($BF),A
site 00360   ; OUT ($BF),A
site 00367   ; OUT ($BF),A
site 0036E   ; OUT ($BF),A
site 00375   ; OUT ($BF),A
site 0037C   ; OUT ($BF),A
site 00383   ; OUT ($BF),A
site 0038A   ; OUT ($BF),A
site 00391   ; OUT ($BF),A
site 00398   ; OUT ($BF),A
site 0039F   ; OUT ($BF),A
site 003A6   ; OUT ($BF),A
site 003BD   ; OUT ($BF),A
site 003C4   ; OUT ($BF),A
site 003CB   ; OUT ($BE),A
site 003D8   ; OTIR
site 0042F   ; OUT ($BF),A
site 00436   ; OUT ($BF),A
site 0043D   ; OUT ($BF),A
site 00444   ; OUT ($BF),A
site 0044B   ; OUT ($BF),A
site 00452   ; OUT ($BF),A
site 00459   ; OUT ($BF),A
site 00460   ; OUT ($BF),A
site 00467   ; OUT ($BF),A
site 0046E   ; OUT ($BF),A
site 00475   ; OUT ($BF),A
site 0047C   ; OUT ($BF),A
site 00483   ; OUT ($BF),A
site 0048A   ; OUT ($BF),A
site 00491   ; OUT ($BF),A
site 00498   ; OUT ($BF),A
site 0049F   ; OUT ($BF),A
site 004A6   ; OUT ($BF),A
site 004BD   ; OUT ($BF),A
site 004C4   ; OUT ($BF),A
site 004CB   ; OUT ($BE),A
site 004D4   ; OTIR
site 00F7E   ; OUT ($BF),A
site 00F84   ; OUT ($BF),A
site 00FA9   ; OUT ($BE),A
site 00FAE   ; OUTI
site 00FC0   ; OUT ($BF),A
site 00FC6   ; OUT ($BF),A
site 01197   ; OUT ($BF),A
site 0119A   ; OUT ($BF),A
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
site 01205   ; OUT ($BF),A
site 01208   ; OUT ($BF),A
site 01227   ; OUTI
site 0122C   ; OUTI
site 01231   ; OUTI
site 01236   ; OUTI
site 0123B   ; OUTI
site 01240   ; OUTI
site 01245   ; OUTI
site 0124A   ; OUTI
site 0124F   ; OUTI
site 01254   ; OUTI
site 01259   ; OUTI
site 0125E   ; OUTI
site 01263   ; OUTI
site 01268   ; OUTI
site 0126D   ; OUTI
site 01272   ; OUTI
site 01277   ; OUTI
site 0127C   ; OUTI
site 01281   ; OUTI
site 01286   ; OUTI
site 0128B   ; OUTI
site 01290   ; OUTI
site 01295   ; OUTI
site 0129A   ; OUTI
site 0129F   ; OUTI
site 012A4   ; OUTI
site 012A9   ; OUTI
site 012AE   ; OUTI
site 012B3   ; OUTI
site 012B8   ; OUTI
site 012BD   ; OUTI
site 012C2   ; OUTI
site 01D2E   ; OUT ($BF),A
site 01D34   ; OUT ($BF),A
site 01D3A   ; IN A,($BE)
site 02E79   ; OUT ($BF),A
site 02E80   ; OUT ($BF),A
site 02EBF   ; OUT ($BF),A
site 02EC5   ; OUT ($BF),A
site 02ECB   ; OUT ($BE),A
site 02ED1   ; OUT ($BE),A
site 02F70   ; OUT ($BF),A
site 02F76   ; OUT ($BF),A
site 02F7D   ; OUT ($BE),A
site 02F84   ; OUT ($BE),A
site 02F8B   ; OUT ($BE),A
site 02F92   ; OUT ($BE),A
site 02FA0   ; OUT ($BF),A
site 02FA6   ; OUT ($BF),A
site 02FAD   ; OUT ($BE),A
site 02FB4   ; OUT ($BE),A
site 02FBB   ; OUT ($BE),A
site 02FC2   ; OUT ($BE),A
site 02FDA   ; OUT ($BF),A
site 02FE0   ; OUT ($BF),A
site 02FE6   ; OUT ($BE),A
site 02FEE   ; OUT ($BE),A
site 02FF5   ; OUT ($BE),A
site 02FFD   ; OUT ($BE),A
site 0300C   ; OUT ($BF),A
site 03012   ; OUT ($BF),A
site 03018   ; OUT ($BE),A
site 03020   ; OUT ($BE),A
site 03027   ; OUT ($BE),A
site 0302F   ; OUT ($BE),A
site 03061   ; OUT ($BF),A
site 03067   ; OUT ($BF),A
site 0307B   ; OUT ($BE),A
site 03082   ; OUT ($BE),A
site 0309A   ; OUT ($BE),A
site 030A2   ; OUT ($BE),A
site 030AF   ; OUT ($BE),A
site 030B4   ; OUT ($BE),A
site 030BF   ; OUT ($BE),A
site 030C7   ; OUT ($BE),A
site 030CC   ; OUT ($BE),A
site 030D1   ; OUT ($BE),A
site 030DC   ; OUT ($BE),A
site 030E4   ; OUT ($BE),A
site 030E9   ; OUT ($BE),A
site 030EE   ; OUT ($BE),A
site 030F9   ; OUT ($BE),A
site 03101   ; OUT ($BE),A
site 03106   ; OUT ($BE),A
site 0310B   ; OUT ($BE),A
site 03116   ; OUT ($BE),A
site 0311E   ; OUT ($BE),A
site 03123   ; OUT ($BE),A
site 03128   ; OUT ($BE),A
site 03133   ; OUT ($BE),A
site 0313B   ; OUT ($BE),A
site 03140   ; OUT ($BE),A
site 03145   ; OUT ($BE),A
site 03150   ; OUT ($BE),A
site 03158   ; OUT ($BE),A
site 0315D   ; OUT ($BE),A
site 03162   ; OUT ($BE),A
site 0316D   ; OUT ($BE),A
site 03175   ; OUT ($BE),A
site 0317A   ; OUT ($BE),A
site 0317F   ; OUT ($BE),A
site 0318A   ; OUT ($BE),A
site 03192   ; OUT ($BE),A
site 031A6   ; OUT (C),A
site 031AF   ; OUT (C),A
site 031B8   ; OUT (C),A
site 031C1   ; OUT (C),A
site 031CC   ; OUT (C),A
site 031D5   ; OUT (C),A
site 031DE   ; OUT (C),A
site 031E7   ; OUT (C),A
site 031F2   ; OUT (C),A
site 031FB   ; OUT (C),A
site 03204   ; OUT (C),A
site 0320D   ; OUT (C),A
site 03218   ; OUT (C),A
site 03221   ; OUT (C),A
site 0322A   ; OUT (C),A
site 03233   ; OUT (C),A
site 0323E   ; OUT (C),A
site 03247   ; OUT (C),A
site 03250   ; OUT (C),A
site 03259   ; OUT (C),A
site 03264   ; OUT (C),A
site 0326D   ; OUT (C),A
site 03276   ; OUT (C),A
site 0327F   ; OUT (C),A
site 0328A   ; OUT (C),A
site 03293   ; OUT (C),A
site 0329C   ; OUT (C),A
site 032A5   ; OUT (C),A
site 032B0   ; OUT (C),A
site 032B9   ; OUT (C),A
site 032C2   ; OUT (C),A
site 032CB   ; OUT (C),A
site 0330E   ; IN A,($BF)
site 03335   ; OUT ($BF),A
site 0333C   ; OUT ($BF),A
site 0336C   ; IN A,($DC)
site 033B6   ; IN A,($DD)
site 03426   ; OUT ($BF),A
site 0342A   ; OUT ($BF),A
site 0342E   ; OUT ($BE),A
site 03439   ; OUT ($BF),A
site 0343D   ; OUT ($BF),A
site 03457   ; OUTI
site 03459   ; OUTI
site 0345C   ; OUTI
site 0345E   ; OUTI
site 03461   ; OUTI
site 03463   ; OUTI
site 03466   ; OUTI
site 03468   ; OUTI
site 0346B   ; OUTI
site 0346D   ; OUTI
site 03470   ; OUTI
site 03472   ; OUTI
site 03475   ; OUTI
site 03477   ; OUTI
site 0347A   ; OUTI
site 0347C   ; OUTI
site 0347F   ; OUTI
site 03481   ; OUTI
site 03484   ; OUTI
site 03486   ; OUTI
site 03489   ; OUTI
site 0348B   ; OUTI
site 0348E   ; OUTI
site 03490   ; OUTI
site 03493   ; OUTI
site 03495   ; OUTI
site 03498   ; OUTI
site 0349A   ; OUTI
site 0349D   ; OUTI
site 0349F   ; OUTI
site 034A2   ; OUTI
site 034A4   ; OUTI
site 034A7   ; OUTI
site 034A9   ; OUTI
site 034AC   ; OUTI
site 034AE   ; OUTI
site 034B1   ; OUTI
site 034B3   ; OUTI
site 034B6   ; OUTI
site 034B8   ; OUTI
site 034BB   ; OUTI
site 034BD   ; OUTI
site 034C0   ; OUTI
site 034C2   ; OUTI
site 034C5   ; OUTI
site 034C7   ; OUTI
site 034CA   ; OUTI
site 034CC   ; OUTI
site 034CF   ; OUTI
site 034D1   ; OUTI
site 034D4   ; OUTI
site 034D6   ; OUTI
site 034D9   ; OUTI
site 034DB   ; OUTI
site 034DE   ; OUTI
site 034E0   ; OUTI
site 034E3   ; OUTI
site 034E5   ; OUTI
site 034E8   ; OUTI
site 034EA   ; OUTI
site 034ED   ; OUTI
site 034EF   ; OUTI
site 034F2   ; OUTI
site 034F4   ; OUTI
site 034F7   ; OUTI
site 034F9   ; OUTI
site 034FC   ; OUTI
site 034FE   ; OUTI
site 03501   ; OUTI
site 03503   ; OUTI
site 03506   ; OUTI
site 03508   ; OUTI
site 0350B   ; OUTI
site 0350D   ; OUTI
site 03510   ; OUTI
site 03512   ; OUTI
site 03515   ; OUTI
site 03517   ; OUTI
site 0351A   ; OUTI
site 0351C   ; OUTI
site 0351F   ; OUTI
site 03521   ; OUTI
site 03524   ; OUTI
site 03526   ; OUTI
site 03529   ; OUTI
site 0352B   ; OUTI
site 0352E   ; OUTI
site 03530   ; OUTI
site 03533   ; OUTI
site 03535   ; OUTI
site 03538   ; OUTI
site 0353A   ; OUTI
site 0353D   ; OUTI
site 0353F   ; OUTI
site 03542   ; OUTI
site 03544   ; OUTI
site 03547   ; OUTI
site 03549   ; OUTI
site 0354C   ; OUTI
site 0354E   ; OUTI
site 03551   ; OUTI
site 03553   ; OUTI
site 03556   ; OUTI
site 03558   ; OUTI
site 0355B   ; OUTI
site 0355D   ; OUTI
site 03560   ; OUTI
site 03562   ; OUTI
site 03565   ; OUTI
site 03567   ; OUTI
site 0356A   ; OUTI
site 0356C   ; OUTI
site 0356F   ; OUTI
site 03571   ; OUTI
site 03574   ; OUTI
site 03576   ; OUTI
site 03579   ; OUTI
site 0357B   ; OUTI
site 0357E   ; OUTI
site 03580   ; OUTI
site 03583   ; OUTI
site 03585   ; OUTI
site 03588   ; OUTI
site 0358A   ; OUTI
site 0358D   ; OUTI
site 0358F   ; OUTI
site 03592   ; OUTI
site 03594   ; OUTI
site 03598   ; OUT ($BF),A
site 0359C   ; OUT ($BF),A
site 035AD   ; OUTI
site 035B1   ; OUTI
site 035B5   ; OUTI
site 035B9   ; OUTI
site 035BD   ; OUTI
site 035C1   ; OUTI
site 035C5   ; OUTI
site 035C9   ; OUTI
site 035CD   ; OUTI
site 035D1   ; OUTI
site 035D5   ; OUTI
site 035D9   ; OUTI
site 035DD   ; OUTI
site 035E1   ; OUTI
site 035E5   ; OUTI
site 035E9   ; OUTI
site 035ED   ; OUTI
site 035F1   ; OUTI
site 035F5   ; OUTI
site 035F9   ; OUTI
site 035FD   ; OUTI
site 03601   ; OUTI
site 03605   ; OUTI
site 03609   ; OUTI
site 0360D   ; OUTI
site 03611   ; OUTI
site 03615   ; OUTI
site 03619   ; OUTI
site 0361D   ; OUTI
site 03621   ; OUTI
site 03625   ; OUTI
site 03629   ; OUTI
site 0362D   ; OUTI
site 03631   ; OUTI
site 03635   ; OUTI
site 03639   ; OUTI
site 0363D   ; OUTI
site 03641   ; OUTI
site 03645   ; OUTI
site 03649   ; OUTI
site 0364D   ; OUTI
site 03651   ; OUTI
site 03655   ; OUTI
site 03659   ; OUTI
site 0365D   ; OUTI
site 03661   ; OUTI
site 03665   ; OUTI
site 03669   ; OUTI
site 0366D   ; OUTI
site 03671   ; OUTI
site 03675   ; OUTI
site 03679   ; OUTI
site 0367D   ; OUTI
site 03681   ; OUTI
site 03685   ; OUTI
site 03689   ; OUTI
site 0368D   ; OUTI
site 03691   ; OUTI
site 03695   ; OUTI
site 03699   ; OUTI
site 0369D   ; OUTI
site 036A1   ; OUTI
site 036A5   ; OUTI
site 036A9   ; OUTI
site 036AF   ; OUT ($BE),A
site 036C0   ; OUT ($BF),A
site 036C4   ; OUT ($BF),A
otir 036CC   ; OUTI
site 036DC   ; OUT ($BF),A
site 036E0   ; OUT ($BF),A
site 0370A   ; OUT ($BF),A
site 0370E   ; OUT ($BF),A
site 037AC   ; OUT (C),E
site 037AE   ; OUT (C),D
site 037D6   ; OUTI
site 037D8   ; OUTI
site 037F6   ; OUT (C),E
site 037F8   ; OUT (C),D
site 03820   ; OUTI
site 03822   ; OUTI
site 03840   ; OUT (C),E
site 03842   ; OUT (C),D
site 0386A   ; OUTI
site 0386C   ; OUTI
site 0388A   ; OUT (C),E
site 0388C   ; OUT (C),D
site 038B4   ; OUTI
site 038B6   ; OUTI
site 038D4   ; OUT (C),E
site 038D6   ; OUT (C),D
site 038FE   ; OUTI
site 03900   ; OUTI
site 0391E   ; OUT (C),E
site 03920   ; OUT (C),D
site 03948   ; OUTI
site 0394A   ; OUTI
site 03968   ; OUT (C),E
site 0396A   ; OUT (C),D
site 03992   ; OUTI
site 03994   ; OUTI
site 039B2   ; OUT (C),E
site 039B4   ; OUT (C),D
site 039DC   ; OUTI
site 039DE   ; OUTI
site 039FC   ; OUT (C),E
site 039FE   ; OUT (C),D
site 03A26   ; OUTI
site 03A28   ; OUTI
site 03A46   ; OUT (C),E
site 03A48   ; OUT (C),D
site 03A70   ; OUTI
site 03A72   ; OUTI
site 03A90   ; OUT (C),E
site 03A92   ; OUT (C),D
site 03ABA   ; OUTI
site 03ABC   ; OUTI
site 03ADA   ; OUT (C),E
site 03ADC   ; OUT (C),D
site 03B04   ; OUTI
site 03B06   ; OUTI
site 03B24   ; OUT (C),E
site 03B26   ; OUT (C),D
site 03B4E   ; OUTI
site 03B50   ; OUTI
site 03B6E   ; OUT (C),E
site 03B70   ; OUT (C),D
site 03B98   ; OUTI
site 03B9A   ; OUTI
site 03BB8   ; OUT (C),E
site 03BBA   ; OUT (C),D
site 03BE2   ; OUTI
site 03BE4   ; OUTI
site 03C02   ; OUT (C),E
site 03C04   ; OUT (C),D
site 03C2C   ; OUTI
site 03C2E   ; OUTI
site 03C4C   ; OUT (C),E
site 03C4E   ; OUT (C),D
site 03C76   ; OUTI
site 03C78   ; OUTI
site 03C96   ; OUT (C),E
site 03C98   ; OUT (C),D
site 03CC0   ; OUTI
site 03CC2   ; OUTI
site 03CE0   ; OUT (C),E
site 03CE2   ; OUT (C),D
site 03D0A   ; OUTI
site 03D0C   ; OUTI
site 03D2A   ; OUT (C),E
site 03D2C   ; OUT (C),D
site 03D54   ; OUTI
site 03D56   ; OUTI
site 03D74   ; OUT (C),E
site 03D76   ; OUT (C),D
site 03D9E   ; OUTI
site 03DA0   ; OUTI
site 03DBE   ; OUT (C),E
site 03DC0   ; OUT (C),D
site 03DE8   ; OUTI
site 03DEA   ; OUTI
site 03E08   ; OUT (C),E
site 03E0A   ; OUT (C),D
site 03E32   ; OUTI
site 03E34   ; OUTI
site 03E52   ; OUT (C),E
site 03E54   ; OUT (C),D
site 03E7C   ; OUTI
site 03E7E   ; OUTI
site 03E9C   ; OUT (C),E
site 03E9E   ; OUT (C),D
site 03EC6   ; OUTI
site 03EC8   ; OUTI
site 03EE6   ; OUT (C),E
site 03EE8   ; OUT (C),D
site 03F10   ; OUTI
site 03F12   ; OUTI
site 03F30   ; OUT (C),E
site 03F32   ; OUT (C),D
site 03F5A   ; OUTI
site 03F5C   ; OUTI
site 03F7A   ; OUT (C),E
site 03F7C   ; OUT (C),D
site 03FA4   ; OUTI
site 03FA6   ; OUTI
site 0402F   ; OUT (C),E
site 04031   ; OUT (C),D
site 04059   ; OUTI
site 0405B   ; OUTI
site 04074   ; OUT (C),E
site 04076   ; OUT (C),D
site 0409E   ; OUTI
site 040A0   ; OUTI
site 040B9   ; OUT (C),E
site 040BB   ; OUT (C),D
site 040E3   ; OUTI
site 040E5   ; OUTI
site 040FE   ; OUT (C),E
site 04100   ; OUT (C),D
site 04128   ; OUTI
site 0412A   ; OUTI
site 04143   ; OUT (C),E
site 04145   ; OUT (C),D
site 0416D   ; OUTI
site 0416F   ; OUTI
site 04188   ; OUT (C),E
site 0418A   ; OUT (C),D
site 041B2   ; OUTI
site 041B4   ; OUTI
site 041CD   ; OUT (C),E
site 041CF   ; OUT (C),D
site 041F7   ; OUTI
site 041F9   ; OUTI
site 04212   ; OUT (C),E
site 04214   ; OUT (C),D
site 0423C   ; OUTI
site 0423E   ; OUTI
site 04257   ; OUT (C),E
site 04259   ; OUT (C),D
site 04281   ; OUTI
site 04283   ; OUTI
site 0429C   ; OUT (C),E
site 0429E   ; OUT (C),D
site 042C6   ; OUTI
site 042C8   ; OUTI
site 042E1   ; OUT (C),E
site 042E3   ; OUT (C),D
site 0430B   ; OUTI
site 0430D   ; OUTI
site 04326   ; OUT (C),E
site 04328   ; OUT (C),D
site 04350   ; OUTI
site 04352   ; OUTI
site 0436B   ; OUT (C),E
site 0436D   ; OUT (C),D
site 04395   ; OUTI
site 04397   ; OUTI
site 043B0   ; OUT (C),E
site 043B2   ; OUT (C),D
site 043DA   ; OUTI
site 043DC   ; OUTI
site 043F5   ; OUT (C),E
site 043F7   ; OUT (C),D
site 0441F   ; OUTI
site 04421   ; OUTI
site 0443A   ; OUT (C),E
site 0443C   ; OUT (C),D
site 04464   ; OUTI
site 04466   ; OUTI
site 0447F   ; OUT (C),E
site 04481   ; OUT (C),D
site 044A9   ; OUTI
site 044AB   ; OUTI
site 044C4   ; OUT (C),E
site 044C6   ; OUT (C),D
site 044EE   ; OUTI
site 044F0   ; OUTI
site 04509   ; OUT (C),E
site 0450B   ; OUT (C),D
site 04533   ; OUTI
site 04535   ; OUTI
site 0454E   ; OUT (C),E
site 04550   ; OUT (C),D
site 04578   ; OUTI
site 0457A   ; OUTI
site 04593   ; OUT (C),E
site 04595   ; OUT (C),D
site 045BD   ; OUTI
site 045BF   ; OUTI
site 045D8   ; OUT (C),E
site 045DA   ; OUT (C),D
site 04602   ; OUTI
site 04604   ; OUTI
site 0461D   ; OUT (C),E
site 0461F   ; OUT (C),D
site 04647   ; OUTI
site 04649   ; OUTI
site 04662   ; OUT (C),E
site 04664   ; OUT (C),D
site 0468C   ; OUTI
site 0468E   ; OUTI
site 046A7   ; OUT (C),E
site 046A9   ; OUT (C),D
site 046D1   ; OUTI
site 046D3   ; OUTI
site 046EC   ; OUT (C),E
site 046EE   ; OUT (C),D
site 04716   ; OUTI
site 04718   ; OUTI
site 04731   ; OUT (C),E
site 04733   ; OUT (C),D
site 0475B   ; OUTI
site 0475D   ; OUTI
site 04776   ; OUT (C),E
site 04778   ; OUT (C),D
site 047A0   ; OUTI
site 047A2   ; OUTI
site 047BB   ; OUT (C),E
site 047BD   ; OUT (C),D
site 047E5   ; OUTI
site 047E7   ; OUTI
site 04800   ; OUT (C),E
site 04802   ; OUT (C),D
site 0482A   ; OUTI
site 0482C   ; OUTI
site 04845   ; OUT (C),E
site 04847   ; OUT (C),D
site 0486F   ; OUTI
site 04871   ; OUTI
site 0488A   ; OUT (C),E
site 0488C   ; OUT (C),D
site 048B4   ; OUTI
site 048B6   ; OUTI
site 048CF   ; OUT ($BF),A
site 048D3   ; OUT ($BF),A
asm 048E4 6          ; LD A,$11; LD C,$BE; OUTI: the 17-tile copy loop $48E8-$498C
    rst $00
    db far_io, pg_ds_tiles, ent_ds_tiles
    ret
endasm
asm 03798 12         ; LD A,($CEF0) up to EX AF,AF' at $37A3: the map column loop $37A4-$3FBA
    rst $00
    db far_io, pg_dscol, ent_dscol
    jp $3700
endasm
asm 0401E 9          ; LD A,($CEF0) up to EX AF,AF' at $4026: the map row loop $4027-$48C5
    rst $00
    db far_io, pg_dsrow, ent_dsrow
    jp $3731
endasm
asm 00F76 8          ; ADD A,$78 up to LD A,L at $0F7D: the name table row loop $0F7C-$0FEB
    rst $00
    db far_io, pg_dsnr, ent_dsnr
    jp $0FEC
endasm
asm 011B1 8          ; RES 7,L up to LD C,$BE at $11B7: the tile upload loop $11B9-$11FC
    rst $00
    db far_io, pg_dstq, ent_dstq
    jp $11FD
endasm
asm 0121F 8          ; RES 7,L up to LD C,$BE at $1225: the tile upload loop $1227-$12CA
    rst $00
    db far_io, pg_dstq, ent_dstq
    ret
endasm
asm 03431 8          ; LD C,A up to LD A,$80 at $3437: the sprite table writes $3439-$36B0
    rst $00
    db far_io, pg_dsspr, ent_dsspr
    jp $36B1
endasm
site 048ED   ; OUTI
site 048F2   ; OUTI
site 048F7   ; OUTI
site 048FC   ; OUTI
site 04901   ; OUTI
site 04906   ; OUTI
site 0490B   ; OUTI
site 04910   ; OUTI
site 04915   ; OUTI
site 0491A   ; OUTI
site 0491F   ; OUTI
site 04924   ; OUTI
site 04929   ; OUTI
site 0492E   ; OUTI
site 04933   ; OUTI
site 04938   ; OUTI
site 0493D   ; OUTI
site 04942   ; OUTI
site 04947   ; OUTI
site 0494C   ; OUTI
site 04951   ; OUTI
site 04956   ; OUTI
site 0495B   ; OUTI
site 04960   ; OUTI
site 04965   ; OUTI
site 0496A   ; OUTI
site 0496F   ; OUTI
site 04974   ; OUTI
site 04979   ; OUTI
site 0497E   ; OUTI
site 04983   ; OUTI
site 04A14   ; OUT ($BF),A
site 04A1B   ; OUT ($BF),A
site 04A25   ; OUT ($BE),A
site 04A35   ; OUT ($BF),A
site 04A3B   ; OUT ($BF),A
site 04A43   ; IN A,($7E)
site 04A50   ; OUT ($BF),A
site 04A56   ; OUT ($BF),A
site 04A5D   ; OUT ($BE),A
site 04DC8   ; OUT ($BF),A
site 04DCC   ; OUT ($BF),A
site 04DD6   ; OUTI
site 04DDD   ; OUT ($BF),A
site 04DE3   ; OUT ($BF),A
site 04DE9   ; OUT ($BE),A
site 04DF8   ; OUT ($BF),A
site 04DFE   ; OUT ($BF),A
site 04E03   ; IN A,($7E)
site 04E10   ; OUT ($BF),A
site 04E16   ; OUT ($BF),A
site 04E1C   ; OUT ($BE),A
site 04E6C   ; OUT ($BF),A
site 04E73   ; OUT ($BF),A
site 04EA5   ; OUT ($BE),A
site 04EAB   ; OUT ($BE),A
site 04FD9   ; OUT ($BF),A
site 04FE0   ; OUT ($BF),A
site 04FE6   ; OUT ($BE),A
site 04FE9   ; IN A,($7E)
site 05001   ; OUT ($BF),A
site 05008   ; OUT ($BF),A
site 0500D   ; OUT ($BE),A
site 05010   ; IN A,($7E)
site 05CD4   ; OUT ($BF),A
site 05CDB   ; OUT ($BF),A
site 05CE6   ; IN A,($BE)
site 05D1C   ; OUT ($BF),A
site 05D23   ; OUT ($BF),A
site 05D2A   ; OUT ($BF),A
site 05D31   ; OUT ($BF),A
site 05D38   ; OUT ($BF),A
site 05D3F   ; OUT ($BF),A
site 05D46   ; OUT ($BF),A
site 05D4D   ; OUT ($BF),A
site 05D54   ; OUT ($BF),A
site 05D5B   ; OUT ($BF),A
site 05D62   ; OUT ($BF),A
site 05D69   ; OUT ($BF),A
site 05D8D   ; OUT ($BF),A
site 05D94   ; OUT ($BF),A
site 05D9B   ; OUT ($BE),A
site 05DA4   ; OTIR
site 05DC6   ; OUT ($BF),A
site 05DCD   ; OUT ($BF),A
site 05DEF   ; OUT ($BF),A
site 05DF6   ; OUT ($BF),A
site 05E04   ; OUT ($BE),A
site 05E0B   ; OUT ($BE),A
site 05F19   ; OUT ($BF),A
site 05F20   ; OUT ($BF),A
site 05F27   ; OUT ($BF),A
site 05F2E   ; OUT ($BF),A
site 05F35   ; OUT ($BF),A
site 05F3C   ; OUT ($BF),A
site 05F43   ; OUT ($BF),A
site 05F4A   ; OUT ($BF),A
site 05F52   ; OUT ($BF),A
site 05F59   ; OUT ($BF),A
site 05F61   ; OUT ($BF),A
site 05F68   ; OUT ($BF),A
site 05F6F   ; OUT ($BF),A
site 05F76   ; OUT ($BF),A
site 05F80   ; OUT ($BF),A
site 05F87   ; OUT ($BF),A
site 05F93   ; OUT ($BE),A
site 06062   ; OUT ($BF),A
site 06068   ; OUT ($BF),A
site 0606F   ; OUT ($BE),A
site 06076   ; OUT ($BE),A
site 0607D   ; OUT ($BE),A
site 06084   ; OUT ($BE),A
site 0608B   ; OUT ($BE),A
site 06092   ; OUT ($BE),A
site 06099   ; OUT ($BE),A
site 060A0   ; OUT ($BE),A
site 060A7   ; OUT ($BE),A
site 060AE   ; OUT ($BE),A
site 060B8   ; OUT ($BF),A
site 060BE   ; OUT ($BF),A
site 060C5   ; OUT ($BE),A
site 060CC   ; OUT ($BE),A
site 060D6   ; OUT ($BF),A
site 060DC   ; OUT ($BF),A
site 060E3   ; OUT ($BE),A
site 060EA   ; OUT ($BE),A
site 060F4   ; OUT ($BF),A
site 060FA   ; OUT ($BF),A
site 06101   ; OUT ($BE),A
site 06108   ; OUT ($BE),A
site 06112   ; OUT ($BF),A
site 06118   ; OUT ($BF),A
site 0611F   ; OUT ($BE),A
site 06126   ; OUT ($BE),A
site 06130   ; OUT ($BF),A
site 06136   ; OUT ($BF),A
site 0613D   ; OUT ($BE),A
site 06144   ; OUT ($BE),A
site 0614B   ; OUT ($BE),A
site 06152   ; OUT ($BE),A
site 06159   ; OUT ($BE),A
site 06160   ; OUT ($BE),A
site 06167   ; OUT ($BE),A
site 0616E   ; OUT ($BE),A
site 06175   ; OUT ($BE),A
site 0617C   ; OUT ($BE),A
site 06183   ; OUT ($BF),A
site 06189   ; OUT ($BF),A
site 06190   ; OUT ($BE),A
site 06197   ; OUT ($BE),A
site 0619E   ; OUT ($BE),A
site 061A5   ; OUT ($BE),A
site 061AC   ; OUT ($BE),A
site 061B3   ; OUT ($BE),A
site 061BA   ; OUT ($BE),A
site 061C1   ; OUT ($BE),A
site 061C8   ; OUT ($BE),A
site 061CF   ; OUT ($BE),A
site 061D9   ; OUT ($BF),A
site 061DF   ; OUT ($BF),A
site 061E6   ; OUT ($BE),A
site 061ED   ; OUT ($BE),A
site 061F7   ; OUT ($BF),A
site 061FD   ; OUT ($BF),A
site 06204   ; OUT ($BE),A
site 0620B   ; OUT ($BE),A
site 06215   ; OUT ($BF),A
site 0621B   ; OUT ($BF),A
site 06222   ; OUT ($BE),A
site 06229   ; OUT ($BE),A
site 06233   ; OUT ($BF),A
site 06239   ; OUT ($BF),A
site 06240   ; OUT ($BE),A
site 06247   ; OUT ($BE),A
site 06251   ; OUT ($BF),A
site 06257   ; OUT ($BF),A
site 0625E   ; OUT ($BE),A
site 06265   ; OUT ($BE),A
site 0626C   ; OUT ($BE),A
site 06273   ; OUT ($BE),A
site 0627A   ; OUT ($BE),A
site 06281   ; OUT ($BE),A
site 06288   ; OUT ($BE),A
site 0628F   ; OUT ($BE),A
site 06296   ; OUT ($BE),A
site 0629D   ; OUT ($BE),A
site 06312   ; OUT ($BF),A
site 06319   ; OUT ($BF),A
site 0633B   ; OUT ($BE),A
site 06342   ; OUT ($BE),A
site 0638A   ; OUT ($BF),A
site 06390   ; OUT ($BF),A
site 06399   ; OUT ($BE),A
site 063A0   ; OUT ($BE),A
site 063EC   ; OUT ($BF),A
site 063F2   ; OUT ($BF),A
site 063FC   ; OUT ($BE),A
site 06402   ; OUT ($BE),A
site 06411   ; OUT ($BF),A
site 06418   ; OUT ($BF),A
site 0641F   ; OUT ($BE),A
site 0643D   ; OUT ($BF),A
site 06443   ; OUT ($BF),A
site 0644C   ; OUT ($BE),A
site 06453   ; OUT ($BE),A
site 064CE   ; OUT ($BF),A
site 064D4   ; OUT ($BF),A
site 064E6   ; OUT ($BE),A
site 0651C   ; OUT ($BF),A
site 06522   ; OUT ($BF),A
site 0652D   ; OUT ($BE),A
site 06535   ; OUT ($BE),A
site 06556   ; OUT ($BF),A
site 0655D   ; OUT ($BF),A
site 06564   ; OUT ($BE),A
site 0657D   ; OUT ($BF),A
site 06583   ; OUT ($BF),A
site 0658C   ; OUT ($BE),A
site 06593   ; OUT ($BE),A
site 06632   ; OUT ($BF),A
site 06639   ; OUT ($BF),A
site 06640   ; OUT ($BE),A
site 06659   ; OUT ($BF),A
site 0665F   ; OUT ($BF),A
site 06668   ; OUT ($BE),A
site 0666F   ; OUT ($BE),A
site 27342   ; OUT ($BF),A
site 27349   ; OUT ($BF),A
site 27350   ; OUT ($BF),A
site 27357   ; OUT ($BF),A
site 2735E   ; OUT ($BF),A
site 27365   ; OUT ($BF),A
site 2736C   ; OUT ($BF),A
site 27373   ; OUT ($BF),A
site 2737A   ; OUT ($BF),A
site 27381   ; OUT ($BF),A
site 27388   ; OUT ($BF),A
site 2738F   ; OUT ($BF),A
site 27396   ; OUT ($BF),A
site 2739D   ; OUT ($BF),A
site 273A4   ; OUT ($BF),A
site 273AB   ; OUT ($BF),A
site 273B2   ; OUT ($BF),A
site 273B9   ; OUT ($BF),A
site 273D0   ; OUT ($BF),A
site 273D7   ; OUT ($BF),A
site 273DE   ; OUT ($BE),A
site 273E7   ; OTIR
site 27442   ; OUT ($BF),A
site 27449   ; OUT ($BF),A
site 27494   ; OUT ($BF),A
site 2749A   ; OUT ($BF),A
site 274AA   ; OUT ($BE),A
site 274B1   ; OUT ($BE),A
site 274BA   ; OUT ($BF),A
site 274C0   ; OUT ($BF),A
site 274CE   ; OUT ($BE),A
site 274D5   ; OUT ($BE),A
site 274DC   ; OUT ($BE),A
site 274E3   ; OUT ($BE),A
site 274ED   ; OUT ($BF),A
site 274F3   ; OUT ($BF),A
site 274F9   ; OUT ($BE),A
site 27500   ; OUT ($BE),A
site 27507   ; OUT ($BE),A
site 2750E   ; OUT ($BE),A
site 2757A   ; OUT ($BF),A
site 27580   ; OUT ($BF),A
site 2758D   ; OUT ($BE),A
site 27594   ; OUT ($BE),A
site 275A6   ; OUT ($BE),A
site 275AD   ; OUT ($BE),A
site 275C7   ; OUT ($BF),A
site 275CD   ; OUT ($BF),A
site 275D6   ; OUT ($BE),A
site 275DD   ; OUT ($BE),A
site 28002   ; OUT ($BF),A
site 28009   ; OUT ($BF),A
site 28010   ; OUT ($BF),A
site 28017   ; OUT ($BF),A
site 2801E   ; OUT ($BF),A
site 28025   ; OUT ($BF),A
site 2802C   ; OUT ($BF),A
site 28033   ; OUT ($BF),A
site 2803A   ; OUT ($BF),A
site 28041   ; OUT ($BF),A
site 28048   ; OUT ($BF),A
site 2804F   ; OUT ($BF),A
site 28056   ; OUT ($BF),A
site 2805D   ; OUT ($BF),A
site 28064   ; OUT ($BF),A
site 2806B   ; OUT ($BF),A
site 28072   ; OUT ($BF),A
site 28079   ; OUT ($BF),A
site 280A2   ; OUT ($BF),A
site 280A9   ; OUT ($BF),A
site 280B0   ; OUT ($BE),A
site 280B9   ; OTIR
site 280D9   ; OUT ($BF),A
site 280E0   ; OUT ($BF),A
site 280E7   ; OUT ($BF),A
site 280EE   ; OUT ($BF),A
site 280F5   ; OUT ($BF),A
site 280FC   ; OUT ($BF),A
site 28103   ; OUT ($BF),A
site 2810A   ; OUT ($BF),A
site 28111   ; OUT ($BF),A
site 28118   ; OUT ($BF),A
site 2811F   ; OUT ($BF),A
site 28126   ; OUT ($BF),A
site 2812D   ; OUT ($BF),A
site 28134   ; OUT ($BF),A
site 2813B   ; OUT ($BF),A
site 28142   ; OUT ($BF),A
site 28149   ; OUT ($BF),A
site 28150   ; OUT ($BF),A
site 28170   ; OUT ($BF),A
site 28177   ; OUT ($BF),A
site 2817E   ; OUT ($BE),A
site 28187   ; OTIR
site 281C0   ; OUT ($BF),A
site 281C7   ; OUT ($BF),A
site 28207   ; OUT ($BF),A
site 2820E   ; OUT ($BF),A
site 2821A   ; OUT ($BE),A
site 28223   ; OUT ($BE),A
site 2822E   ; OUT ($BF),A
site 28235   ; OUT ($BF),A
site 28242   ; OUT ($BE),A
site 28249   ; OUT ($BE),A
site 28250   ; OUT ($BE),A
site 28257   ; OUT ($BE),A
site 282A8   ; OUT ($BF),A
site 282AF   ; OUT ($BF),A
site 282E8   ; OUT ($BF),A
site 282EF   ; OUT ($BF),A
site 282FE   ; OUT ($BF),A
site 28305   ; OUT ($BF),A
site 2830C   ; OUT ($BF),A
site 28313   ; OUT ($BF),A
site 28322   ; OUT ($BF),A
site 28329   ; OUT ($BF),A
site 28359   ; OUT ($BF),A
site 28360   ; OUT ($BF),A
site 283AB   ; OUT ($BF),A
site 283B2   ; OUT ($BF),A
site 28415   ; OUT ($BF),A
site 2841C   ; OUT ($BF),A
site 2842C   ; OUT ($BF),A
site 28433   ; OUT ($BF),A
site 2843A   ; OUT ($BF),A
site 28441   ; OUT ($BF),A
site 2848C   ; OUT ($BF),A
site 28493   ; OUT ($BF),A
site 284B3   ; OUT ($BF),A
site 284BA   ; OUT ($BF),A
site 284E8   ; OUT ($BF),A
site 284EF   ; OUT ($BF),A
site 284F9   ; OUT ($BF),A
site 28500   ; OUT ($BF),A
site 28507   ; OUT ($BF),A
site 2850E   ; OUT ($BF),A
site 2851D   ; OUT ($BF),A
site 28524   ; OUT ($BF),A
site 2859F   ; OUT ($BF),A
site 285A6   ; OUT ($BF),A
site 285BC   ; OUT ($BF),A
site 285C3   ; OUT ($BF),A
site 285D3   ; OUT ($BE),A
site 285D9   ; OUT ($BE),A
site 28635   ; OUT ($BF),A
site 2863B   ; OUT ($BF),A
site 2864C   ; OUT ($BE),A
site 28653   ; OUT ($BE),A
site 286A2   ; OUT ($BF),A
site 286A9   ; OUT ($BF),A
site 286BF   ; OUT ($BF),A
site 286C6   ; OUT ($BF),A
site 286D6   ; OUT ($BE),A
site 286DC   ; OUT ($BE),A
site 287CB   ; OUT ($BF),A
site 287D2   ; OUT ($BF),A
site 287DF   ; OUT ($BF),A
site 287E6   ; OUT ($BF),A
site 287ED   ; OUT ($BF),A
site 287F4   ; OUT ($BF),A
site 287FB   ; OUT ($BF),A
site 28802   ; OUT ($BF),A
site 28809   ; OUT ($BF),A
site 28810   ; OUT ($BF),A
site 28817   ; OUT ($BF),A
site 2881E   ; OUT ($BF),A
site 28825   ; OUT ($BF),A
site 2882C   ; OUT ($BF),A
site 28833   ; OUT ($BF),A
site 2883A   ; OUT ($BF),A
site 28841   ; OUT ($BF),A
site 28848   ; OUT ($BF),A
site 2884F   ; OUT ($BF),A
site 28856   ; OUT ($BF),A
site 2886D   ; OUT ($BF),A
site 28874   ; OUT ($BF),A
site 2887B   ; OUT ($BE),A
site 28884   ; OTIR
site 288F9   ; OUT ($BF),A
site 288FF   ; OUT ($BF),A
site 2890C   ; OUT ($BE),A
site 28913   ; OUT ($BE),A
site 28925   ; OUT ($BE),A
site 2892C   ; OUT ($BE),A
site 289E2   ; OUT ($BE),A
site 289E8   ; OUT ($BE),A
site 28A00   ; OUT ($BF),A
site 28A06   ; OUT ($BF),A
site 28A0F   ; OUT ($BE),A
site 28A15   ; OUT ($BE),A
site 28A3C   ; OUT ($BF),A
site 28A43   ; OUT ($BF),A
site 28A4A   ; OUT ($BF),A
site 28A51   ; OUT ($BF),A
site 28A58   ; OUT ($BF),A
site 28A5F   ; OUT ($BF),A
site 28A66   ; OUT ($BF),A
site 28A6D   ; OUT ($BF),A
site 28A74   ; OUT ($BF),A
site 28A7B   ; OUT ($BF),A
site 28A82   ; OUT ($BF),A
site 28A89   ; OUT ($BF),A
site 28AA7   ; OUT ($BF),A
site 28AAE   ; OUT ($BF),A
site 28AB5   ; OUT ($BE),A
site 28ABE   ; OTIR
site 28AF2   ; OUT ($BF),A
site 28AF9   ; OUT ($BF),A
site 28B05   ; OUT ($BE),A
site 28B0E   ; OUT ($BE),A
site 28B1E   ; OUT ($BF),A
site 28B25   ; OUT ($BF),A
site 28B30   ; OUT ($BE),A
site 28B37   ; OUT ($BE),A
site 28B3E   ; OUT ($BE),A
site 28B45   ; OUT ($BE),A
site 28B5F   ; OUT ($BF),A
site 28B66   ; OUT ($BF),A
site 28B6E   ; OUT ($BE),A
site 28B75   ; OUT ($BE),A
site 28BB6   ; OUT ($BF),A
site 28BBC   ; OUT ($BF),A
site 28BC1   ; OUT ($BE),A
site 28BC8   ; OUT ($BF),A
site 28BCE   ; OUT ($BF),A
site 28BD3   ; OUT ($BE),A
site 28C58   ; OUT ($BF),A
site 28C5F   ; OUT ($BF),A
site 28C67   ; OUT ($BE),A
site 28C6E   ; OUT ($BE),A
site 28C88   ; OUT ($BF),A
site 28C8F   ; OUT ($BF),A
site 28C96   ; OUT ($BF),A
site 28C9D   ; OUT ($BF),A
site 28CBA   ; OUT ($BF),A
site 28CC1   ; OUT ($BF),A
site 28CD6   ; OUT ($BF),A
site 28CDD   ; OUT ($BF),A
site 28D5D   ; OUT ($BF),A
site 28D64   ; OUT ($BF),A
site 2902C   ; OUT ($BF),A
site 29033   ; OUT ($BF),A
site 2907C   ; OUT ($BF),A
site 29083   ; OUT ($BF),A
site 29091   ; OUT ($BE),A
site 29097   ; OUT ($BE),A
site 290AA   ; OUT ($BE),A
site 290B0   ; OUT ($BE),A
site 290C9   ; OUT ($BF),A
site 290CF   ; OUT ($BF),A
site 290D5   ; OUT ($BE),A
site 290DA   ; OUT ($BE),A
site 2911F   ; OUT ($BF),A
site 29126   ; OUT ($BF),A
site 291DA   ; OUT ($BF),A
site 291E0   ; OUT ($BF),A
site 291E9   ; OUT ($BE),A
site 291F0   ; OUT ($BE),A
site 2929C   ; OUT ($BF),A
site 292A3   ; OUT ($BF),A
site 293AF   ; OUT ($BF),A
site 293B6   ; OUT ($BF),A
site 293E2   ; OUT ($BF),A
site 293E9   ; OUT ($BF),A
site 29418   ; OUT ($BF),A
site 2941E   ; OUT ($BF),A
site 29424   ; OUT ($BE),A
site 2942B   ; OUT ($BE),A
site 29441   ; OUT ($BF),A
site 29447   ; OUT ($BF),A
site 2944E   ; OUT ($BE),A
site 29455   ; OUT ($BE),A
site 2945E   ; OUT ($BF),A
site 29464   ; OUT ($BF),A
site 2946B   ; OUT ($BE),A
site 29472   ; OUT ($BE),A
site 294E6   ; OUT ($BF),A
site 294EC   ; OUT ($BF),A
site 294F3   ; OUT ($BE),A
site 294FA   ; OUT ($BE),A
site 29503   ; OUT ($BF),A
site 29509   ; OUT ($BF),A
site 29510   ; OUT ($BE),A
site 29517   ; OUT ($BE),A
site 29523   ; OUT ($BF),A
site 29529   ; OUT ($BF),A
site 29530   ; OUT ($BE),A
site 29537   ; OUT ($BE),A
site 29540   ; OUT ($BF),A
site 29546   ; OUT ($BF),A
site 2954D   ; OUT ($BE),A
site 29554   ; OUT ($BE),A
site 2959B   ; OUT ($BF),A
site 295A1   ; OUT ($BF),A
site 295A7   ; OUT ($BE),A
site 295AF   ; OUT ($BE),A
site 2964B   ; OUT ($BF),A
site 29652   ; OUT ($BF),A
site 29675   ; OUT ($BF),A
site 2967B   ; OUT ($BF),A
site 29681   ; OUT ($BE),A
site 29687   ; OUT ($BE),A
site 296A2   ; OUT ($BF),A
site 296A8   ; OUT ($BF),A
site 296AE   ; OUT ($BE),A
site 296B5   ; OUT ($BE),A
site 296BC   ; OUT ($BE),A
site 296C3   ; OUT ($BE),A
site 29832   ; OUT ($BF),A
site 29838   ; OUT ($BF),A
site 2983E   ; OUT ($BE),A
site 29845   ; OUT ($BE),A
site 2984C   ; OUT ($BE),A
site 29853   ; OUT ($BE),A
site 2A0E0   ; OUT ($BF),A
site 2A0E7   ; OUT ($BF),A
site 2A0EE   ; OUT ($BF),A
site 2A0F5   ; OUT ($BF),A
site 2A104   ; OUT ($BF),A
site 2A10B   ; OUT ($BF),A
site 2A190   ; OUT ($BF),A
site 2A197   ; OUT ($BF),A
site 2A1AD   ; OUT ($BF),A
site 2A1B4   ; OUT ($BF),A
site 2A1C4   ; OUT ($BE),A
site 2A1CA   ; OUT ($BE),A
site 2A232   ; OUT ($BF),A
site 2A238   ; OUT ($BF),A
site 2A249   ; OUT ($BE),A
site 2A250   ; OUT ($BE),A
site 2A294   ; OUT ($BF),A
site 2A29B   ; OUT ($BF),A
site 2A2A2   ; OUT ($BF),A
site 2A2A9   ; OUT ($BF),A
site 2A2B0   ; OUT ($BF),A
site 2A2B7   ; OUT ($BF),A
site 2A2BE   ; OUT ($BF),A
site 2A2C5   ; OUT ($BF),A
site 2A2CC   ; OUT ($BF),A
site 2A2D3   ; OUT ($BF),A
site 2A2DA   ; OUT ($BF),A
site 2A2E1   ; OUT ($BF),A
site 2A2E8   ; OUT ($BF),A
site 2A2EF   ; OUT ($BF),A
site 2A2F6   ; OUT ($BF),A
site 2A2FD   ; OUT ($BF),A
site 2A304   ; OUT ($BF),A
site 2A30B   ; OUT ($BF),A
site 2A312   ; OUT ($BF),A
site 2A319   ; OUT ($BF),A
site 2A330   ; OUT ($BF),A
site 2A337   ; OUT ($BF),A
site 2A33E   ; OUT ($BE),A
site 2A347   ; OTIR
site 2A3FD   ; OUT ($BF),A
site 2A404   ; OUT ($BF),A
site 2A40B   ; OUT ($BF),A
site 2A412   ; OUT ($BF),A
site 2A419   ; OUT ($BF),A
site 2A420   ; OUT ($BF),A
site 2A427   ; OUT ($BF),A
site 2A42E   ; OUT ($BF),A
site 2A435   ; OUT ($BF),A
site 2A43C   ; OUT ($BF),A
site 2A443   ; OUT ($BF),A
site 2A44A   ; OUT ($BF),A
site 2A451   ; OUT ($BF),A
site 2A458   ; OUT ($BF),A
site 2A45F   ; OUT ($BF),A
site 2A466   ; OUT ($BF),A
site 2A46D   ; OUT ($BF),A
site 2A474   ; OUT ($BF),A
site 2A48D   ; OUT ($BF),A
site 2A494   ; OUT ($BF),A
site 2A49B   ; OUT ($BE),A
site 2A4A4   ; OTIR
site 2A744   ; OUT ($BF),A
site 2A74B   ; OUT ($BF),A
site 2A752   ; OUT ($BF),A
site 2A759   ; OUT ($BF),A
site 2A760   ; OUT ($BF),A
site 2A767   ; OUT ($BF),A
site 2A76E   ; OUT ($BF),A
site 2A775   ; OUT ($BF),A
site 2A77C   ; OUT ($BF),A
site 2A783   ; OUT ($BF),A
site 2A7A7   ; OUT ($BF),A
site 2A7AE   ; OUT ($BF),A
site 2A7B5   ; OUT ($BE),A
site 2A7BE   ; OTIR
site 2A7D5   ; OUT ($BF),A
site 2A7DC   ; OUT ($BF),A
site 2A7F7   ; OUT ($BF),A
site 2A7FE   ; OUT ($BF),A
site 2A82D   ; OUT ($BF),A
site 2A833   ; OUT ($BF),A
site 2A839   ; OUT ($BE),A
site 2A840   ; OUT ($BE),A
site 2A856   ; OUT ($BF),A
site 2A85C   ; OUT ($BF),A
site 2A863   ; OUT ($BE),A
site 2A86A   ; OUT ($BE),A
site 2A873   ; OUT ($BF),A
site 2A879   ; OUT ($BF),A
site 2A880   ; OUT ($BE),A
site 2A887   ; OUT ($BE),A
site 2A8E8   ; OUT ($BF),A
site 2A8EE   ; OUT ($BF),A
site 2A8F5   ; OUT ($BE),A
site 2A8FC   ; OUT ($BE),A
site 2A905   ; OUT ($BF),A
site 2A90B   ; OUT ($BF),A
site 2A912   ; OUT ($BE),A
site 2A919   ; OUT ($BE),A
site 2A925   ; OUT ($BF),A
site 2A92B   ; OUT ($BF),A
site 2A932   ; OUT ($BE),A
site 2A939   ; OUT ($BE),A
site 2A942   ; OUT ($BF),A
site 2A948   ; OUT ($BF),A
site 2A94F   ; OUT ($BE),A
site 2A956   ; OUT ($BE),A
site 2A99D   ; OUT ($BF),A
site 2A9A3   ; OUT ($BF),A
site 2A9A9   ; OUT ($BE),A
site 2A9B1   ; OUT ($BE),A
site 2AA0A   ; OUT ($BF),A
site 2AA11   ; OUT ($BF),A
site 2AA18   ; OUT ($BF),A
site 2AA1F   ; OUT ($BF),A
site 2AA26   ; OUT ($BF),A
site 2AA2D   ; OUT ($BF),A
site 2AA34   ; OUT ($BF),A
site 2AA3B   ; OUT ($BF),A
site 2AA42   ; OUT ($BF),A
site 2AA49   ; OUT ($BF),A
site 2AA50   ; OUT ($BF),A
site 2AA57   ; OUT ($BF),A
site 2AA5E   ; OUT ($BF),A
site 2AA65   ; OUT ($BF),A
site 2AA6C   ; OUT ($BF),A
site 2AA73   ; OUT ($BF),A
site 2AA7A   ; OUT ($BF),A
site 2AA81   ; OUT ($BF),A
site 2AA98   ; OUT ($BF),A
site 2AA9F   ; OUT ($BF),A
site 2AAA6   ; OUT ($BE),A
site 2AAAF   ; OTIR
site 2AAD0   ; OUT ($BF),A
site 2AAD7   ; OUT ($BF),A
site 2AADE   ; OUT ($BF),A
site 2AAE5   ; OUT ($BF),A
site 2AAEC   ; OUT ($BF),A
site 2AAF3   ; OUT ($BF),A
site 2AAFA   ; OUT ($BF),A
site 2AB01   ; OUT ($BF),A
site 2AB08   ; OUT ($BF),A
site 2AB0F   ; OUT ($BF),A
site 2AB36   ; OUT ($BF),A
site 2AB3D   ; OUT ($BF),A
site 2AB44   ; OUT ($BE),A
site 2AB4D   ; OTIR
site 2AB54   ; OUT ($BF),A
site 2AB5B   ; OUT ($BF),A
site 2AB65   ; OUT ($BE),A
site 2AB6C   ; OUT ($BE),A
site 2AB7C   ; OUT ($BF),A
site 2AB83   ; OUT ($BF),A
site 2AB8D   ; OUT ($BE),A
site 2AB94   ; OUT ($BE),A
site 2ABB1   ; OUT ($BF),A
site 2ABB7   ; OUT ($BF),A
site 2ABBF   ; OUT ($BE),A
site 2ABE2   ; OUT ($BF),A
site 2ABE9   ; OUT ($BF),A
site 2ABF0   ; OUT ($BE),A
site 2ABF4   ; OUT ($BF),A
site 2ABFB   ; OUT ($BF),A
site 2AC02   ; OUT ($BF),A
site 2AC09   ; OUT ($BF),A
site 2AC10   ; OUT ($BF),A
site 2AC17   ; OUT ($BF),A
site 2AC35   ; OUT ($BF),A
site 2AC3C   ; OUT ($BF),A
site 2AC43   ; OUT ($BE),A
site 2C18B   ; OUT ($7F),A
site 2C18F   ; OUT ($7F),A
site 2C193   ; OUT ($7F),A
site 2C197   ; OUT ($7F),A
site 2C3D3   ; OUT ($7E),A
site 2C403   ; OUT ($7F),A
site 2C417   ; OUT ($7F),A
site 2C429   ; OUT ($7F),A
site 2C875   ; OUT ($7F),A
site 2C879   ; OUT ($7F),A
site 2C884   ; OUT ($7F),A
site 2C88F   ; OUT ($7F),A
site 2C89A   ; OUT ($7F),A
mapst 00009   ; LD ($FFFC),A
mapst 0000C   ; LD ($FFFD),A
mapst 00011   ; LD ($FFFE),A
mapst 00016   ; LD ($FFFF),A
mapst 0001E   ; LD ($FFFF),A
mapst 0010B   ; LD ($FFFF),A
mapst 0011E   ; LD ($FFFF),A
mapst 00138   ; LD ($FFFF),A
mapst 0014B   ; LD ($FFFF),A
mapst 0015E   ; LD ($FFFF),A
mapst 001C3   ; LD ($FFFF),A
mapst 0020E   ; LD ($FFFF),A
mapst 0022A   ; LD ($FFFF),A
mapst 002D5   ; LD ($FFFF),A
mapst 002F8   ; LD ($FFFF),A
mapst 003F8   ; LD ($FFFF),A
mapst 0040B   ; LD ($FFFF),A
mapst 004E7   ; LD ($FFFF),A
mapst 00BF0   ; LD ($FFFF),A
mapst 00CDD   ; LD ($FFFF),A
mapst 00D1C   ; LD ($FFFF),A
mapst 00D5E   ; LD ($FFFF),A
mapst 00D67   ; LD ($FFFF),A
mapst 00D82   ; LD ($FFFF),A
mapst 00E1C   ; LD ($FFFF),A
mapst 0101B   ; LD ($FFFF),A
mapst 011A6   ; LD ($FFFF),A
mapst 01214   ; LD ($FFFF),A
mapst 01389   ; LD ($FFFF),A
mapst 013A1   ; LD ($FFFF),A
mapst 0157F   ; LD ($FFFF),A
mapst 015F7   ; LD ($FFFF),A
mapst 0163C   ; LD ($FFFF),A
mapst 01724   ; LD ($FFFF),A
mapst 01744   ; LD ($FFFF),A
mapst 01847   ; LD ($FFFF),A
mapst 0185C   ; LD ($FFFF),A
mapst 01865   ; LD ($FFFF),A
mapst 01911   ; LD ($FFFF),A
mapst 01926   ; LD ($FFFF),A
mapst 0192F   ; LD ($FFFF),A
mapst 019DF   ; LD ($FFFF),A
mapst 019F0   ; LD ($FFFF),A
mapst 01B58   ; LD ($FFFF),A
mapst 01C21   ; LD ($FFFF),A
mapst 01C72   ; LD ($FFFF),A
mapst 01D4A   ; LD ($FFFF),A
mapst 020FA   ; LD ($FFFF),A
mapst 02112   ; LD ($FFFF),A
mapst 0266F   ; LD ($FFFF),A
mapst 02678   ; LD ($FFFF),A
mapst 0288B   ; LD ($FFFF),A
mapst 02894   ; LD ($FFFF),A
mapst 028BB   ; LD ($FFFF),A
mapst 028C4   ; LD ($FFFF),A
mapst 028E1   ; LD ($FFFF),A
mapst 02999   ; LD ($FFFF),A
mapst 029A2   ; LD ($FFFF),A
mapst 029C7   ; LD ($FFFF),A
mapst 02AC0   ; LD ($FFFF),A
mapst 02E65   ; LD ($FFFF),A
mapst 02E94   ; LD ($FFFF),A
mapst 02EE3   ; LD ($FFFF),A
mapst 03396   ; LD ($FFFF),A
mapst 033C0   ; LD ($FFFF),A
mapst 033E0   ; LD ($FFFF),A
mapst 033F6   ; LD ($FFFF),A
mapst 03418   ; LD ($FFFF),A
mapst 037A4   ; LD ($FFFF),A
mapst 037D1   ; LD ($FFFF),A
mapst 037EE   ; LD ($FFFF),A
mapst 0381B   ; LD ($FFFF),A
mapst 03838   ; LD ($FFFF),A
mapst 03865   ; LD ($FFFF),A
mapst 03882   ; LD ($FFFF),A
mapst 038AF   ; LD ($FFFF),A
mapst 038CC   ; LD ($FFFF),A
mapst 038F9   ; LD ($FFFF),A
mapst 03916   ; LD ($FFFF),A
mapst 03943   ; LD ($FFFF),A
mapst 03960   ; LD ($FFFF),A
mapst 0398D   ; LD ($FFFF),A
mapst 039AA   ; LD ($FFFF),A
mapst 039D7   ; LD ($FFFF),A
mapst 039F4   ; LD ($FFFF),A
mapst 03A21   ; LD ($FFFF),A
mapst 03A3E   ; LD ($FFFF),A
mapst 03A6B   ; LD ($FFFF),A
mapst 03A88   ; LD ($FFFF),A
mapst 03AB5   ; LD ($FFFF),A
mapst 03AD2   ; LD ($FFFF),A
mapst 03AFF   ; LD ($FFFF),A
mapst 03B1C   ; LD ($FFFF),A
mapst 03B49   ; LD ($FFFF),A
mapst 03B66   ; LD ($FFFF),A
mapst 03B93   ; LD ($FFFF),A
mapst 03BB0   ; LD ($FFFF),A
mapst 03BDD   ; LD ($FFFF),A
mapst 03BFA   ; LD ($FFFF),A
mapst 03C27   ; LD ($FFFF),A
mapst 03C44   ; LD ($FFFF),A
mapst 03C71   ; LD ($FFFF),A
mapst 03C8E   ; LD ($FFFF),A
mapst 03CBB   ; LD ($FFFF),A
mapst 03CD8   ; LD ($FFFF),A
mapst 03D05   ; LD ($FFFF),A
mapst 03D22   ; LD ($FFFF),A
mapst 03D4F   ; LD ($FFFF),A
mapst 03D6C   ; LD ($FFFF),A
mapst 03D99   ; LD ($FFFF),A
mapst 03DB6   ; LD ($FFFF),A
mapst 03DE3   ; LD ($FFFF),A
mapst 03E00   ; LD ($FFFF),A
mapst 03E2D   ; LD ($FFFF),A
mapst 03E4A   ; LD ($FFFF),A
mapst 03E77   ; LD ($FFFF),A
mapst 03E94   ; LD ($FFFF),A
mapst 03EC1   ; LD ($FFFF),A
mapst 03EDE   ; LD ($FFFF),A
mapst 03F0B   ; LD ($FFFF),A
mapst 03F28   ; LD ($FFFF),A
mapst 03F55   ; LD ($FFFF),A
mapst 03F72   ; LD ($FFFF),A
mapst 03F9F   ; LD ($FFFF),A
mapst 04027   ; LD ($FFFF),A
mapst 04054   ; LD ($FFFF),A
mapst 0406C   ; LD ($FFFF),A
mapst 04099   ; LD ($FFFF),A
mapst 040B1   ; LD ($FFFF),A
mapst 040DE   ; LD ($FFFF),A
mapst 040F6   ; LD ($FFFF),A
mapst 04123   ; LD ($FFFF),A
mapst 0413B   ; LD ($FFFF),A
mapst 04168   ; LD ($FFFF),A
mapst 04180   ; LD ($FFFF),A
mapst 041AD   ; LD ($FFFF),A
mapst 041C5   ; LD ($FFFF),A
mapst 041F2   ; LD ($FFFF),A
mapst 0420A   ; LD ($FFFF),A
mapst 04237   ; LD ($FFFF),A
mapst 0424F   ; LD ($FFFF),A
mapst 0427C   ; LD ($FFFF),A
mapst 04294   ; LD ($FFFF),A
mapst 042C1   ; LD ($FFFF),A
mapst 042D9   ; LD ($FFFF),A
mapst 04306   ; LD ($FFFF),A
mapst 0431E   ; LD ($FFFF),A
mapst 0434B   ; LD ($FFFF),A
mapst 04363   ; LD ($FFFF),A
mapst 04390   ; LD ($FFFF),A
mapst 043A8   ; LD ($FFFF),A
mapst 043D5   ; LD ($FFFF),A
mapst 043ED   ; LD ($FFFF),A
mapst 0441A   ; LD ($FFFF),A
mapst 04432   ; LD ($FFFF),A
mapst 0445F   ; LD ($FFFF),A
mapst 04477   ; LD ($FFFF),A
mapst 044A4   ; LD ($FFFF),A
mapst 044BC   ; LD ($FFFF),A
mapst 044E9   ; LD ($FFFF),A
mapst 04501   ; LD ($FFFF),A
mapst 0452E   ; LD ($FFFF),A
mapst 04546   ; LD ($FFFF),A
mapst 04573   ; LD ($FFFF),A
mapst 0458B   ; LD ($FFFF),A
mapst 045B8   ; LD ($FFFF),A
mapst 045D0   ; LD ($FFFF),A
mapst 045FD   ; LD ($FFFF),A
mapst 04615   ; LD ($FFFF),A
mapst 04642   ; LD ($FFFF),A
mapst 0465A   ; LD ($FFFF),A
mapst 04687   ; LD ($FFFF),A
mapst 0469F   ; LD ($FFFF),A
mapst 046CC   ; LD ($FFFF),A
mapst 046E4   ; LD ($FFFF),A
mapst 04711   ; LD ($FFFF),A
mapst 04729   ; LD ($FFFF),A
mapst 04756   ; LD ($FFFF),A
mapst 0476E   ; LD ($FFFF),A
mapst 0479B   ; LD ($FFFF),A
mapst 047B3   ; LD ($FFFF),A
mapst 047E0   ; LD ($FFFF),A
mapst 047F8   ; LD ($FFFF),A
mapst 04825   ; LD ($FFFF),A
mapst 0483D   ; LD ($FFFF),A
mapst 0486A   ; LD ($FFFF),A
mapst 04882   ; LD ($FFFF),A
mapst 048AF   ; LD ($FFFF),A
mapst 048CB   ; LD ($FFFF),A
mapst 048E1   ; LD ($FFFF),A
mapst 04996   ; LD ($FFFF),A
mapst 049C0   ; LD ($FFFF),A
mapst 049D0   ; LD ($FFFF),A
mapst 04E82   ; LD ($FFFF),A
mapst 04E95   ; LD ($FFFF),A
mapst 05DB2   ; LD ($FFFF),A
mapst 05DDE   ; LD ($FFFF),A
mapst 05E40   ; LD ($FFFF),A
mapst 05E5F   ; LD ($FFFF),A
mapst 05E83   ; LD ($FFFF),A
mapst 05FCD   ; LD ($FFFF),A
mapst 062A5   ; LD ($FFFF),A
mapst 06375   ; LD ($FFFF),A
mapst 063B0   ; LD ($FFFF),A
mapst 06423   ; LD ($FFFF),A
mapst 06466   ; LD ($FFFF),A
mapst 06481   ; LD ($FFFF),A
mapst 06489   ; LD ($FFFF),A
mapst 064BC   ; LD ($FFFF),A
mapst 064E0   ; LD ($FFFF),A
mapst 064F4   ; LD ($FFFF),A
mapst 0650A   ; LD ($FFFF),A
mapst 06516   ; LD ($FFFF),A
mapst 06568   ; LD ($FFFF),A
mapst 065A3   ; LD ($FFFF),A
mapst 06644   ; LD ($FFFF),A
mapst 0667F   ; LD ($FFFF),A
mapst 0678F   ; LD ($FFFF),A
mapst 067A5   ; LD ($FFFF),A
mapst 27404   ; LD ($FFFF),A
mapst 27415   ; LD ($FFFF),A
mapst 27420   ; LD ($FFFF),A
mapst 2743D   ; LD ($FFFF),A
mapst 2745A   ; LD ($FFFF),A
mapst 2751C   ; LD ($FFFF),A
mapst 27536   ; LD ($FFFF),A
mapst 2819E   ; LD ($FFFF),A
mapst 281AF   ; LD ($FFFF),A
mapst 281D8   ; LD ($FFFF),A
mapst 282A3   ; LD ($FFFF),A
mapst 282DD   ; LD ($FFFF),A
mapst 2831D   ; LD ($FFFF),A
mapst 2833B   ; LD ($FFFF),A
mapst 28367   ; LD ($FFFF),A
mapst 283A6   ; LD ($FFFF),A
mapst 283C3   ; LD ($FFFF),A
mapst 28407   ; LD ($FFFF),A
mapst 28518   ; LD ($FFFF),A
mapst 28536   ; LD ($FFFF),A
mapst 2857A   ; LD ($FFFF),A
mapst 2859A   ; LD ($FFFF),A
mapst 285B7   ; LD ($FFFF),A
mapst 285F4   ; LD ($FFFF),A
mapst 2867E   ; LD ($FFFF),A
mapst 2868C   ; LD ($FFFF),A
mapst 2869D   ; LD ($FFFF),A
mapst 286BA   ; LD ($FFFF),A
mapst 286ED   ; LD ($FFFF),A
mapst 28700   ; LD ($FFFF),A
mapst 2870B   ; LD ($FFFF),A
mapst 28734   ; LD ($FFFF),A
mapst 287C3   ; LD ($FFFF),A
mapst 28AC2   ; LD ($FFFF),A
mapst 28AD0   ; LD ($FFFF),A
mapst 28AED   ; LD ($FFFF),A
mapst 28B19   ; LD ($FFFF),A
mapst 28CA4   ; LD ($FFFF),A
mapst 28CB5   ; LD ($FFFF),A
mapst 28CEF   ; LD ($FFFF),A
mapst 28D03   ; LD ($FFFF),A
mapst 28D1A   ; LD ($FFFF),A
mapst 28E21   ; LD ($FFFF),A
mapst 28EA1   ; LD ($FFFF),A
mapst 29027   ; LD ($FFFF),A
mapst 2904D   ; LD ($FFFF),A
mapst 290EB   ; LD ($FFFF),A
mapst 29197   ; LD ($FFFF),A
mapst 291D0   ; LD ($FFFF),A
mapst 2924D   ; LD ($FFFF),A
mapst 293C3   ; LD ($FFFF),A
mapst 293D1   ; LD ($FFFF),A
mapst 293FD   ; LD ($FFFF),A
mapst 29482   ; LD ($FFFF),A
mapst 295EA   ; LD ($FFFF),A
mapst 2961A   ; LD ($FFFF),A
mapst 29646   ; LD ($FFFF),A
mapst 29666   ; LD ($FFFF),A
mapst 29781   ; LD ($FFFF),A
mapst 297B8   ; LD ($FFFF),A
mapst 297C3   ; LD ($FFFF),A
mapst 297D1   ; LD ($FFFF),A
mapst 2980C   ; LD ($FFFF),A
mapst 2A0FF   ; LD ($FFFF),A
mapst 2A11D   ; LD ($FFFF),A
mapst 2A15A   ; LD ($FFFF),A
mapst 2A16B   ; LD ($FFFF),A
mapst 2A18B   ; LD ($FFFF),A
mapst 2A1A8   ; LD ($FFFF),A
mapst 2A1E5   ; LD ($FFFF),A
mapst 2A27F   ; LD ($FFFF),A
mapst 2A364   ; LD ($FFFF),A
mapst 2A3A8   ; LD ($FFFF),A
mapst 2A4C1   ; LD ($FFFF),A
mapst 2A4D2   ; LD ($FFFF),A
mapst 2A602   ; LD ($FFFF),A
mapst 2A66E   ; LD ($FFFF),A
mapst 2A67F   ; LD ($FFFF),A
mapst 2A690   ; LD ($FFFF),A
mapst 2A6A1   ; LD ($FFFF),A
mapst 2A7C5   ; LD ($FFFF),A
mapst 2A7E6   ; LD ($FFFF),A
mapst 2A812   ; LD ($FFFF),A
mapst 2A897   ; LD ($FFFF),A
mapst 2A9E6   ; LD ($FFFF),A
mapst 2ABA4   ; LD ($FFFF),A
mapst 2AC21   ; LD ($FFFF),A
mapst 2AC61   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00071   ; LD ($FFFC),A; after LD A,$28; 32 bytes of valid code before it
mapst 00083   ; LD ($FFFC),A; after LD A,($FFFB); JP/CALL target from $467F4 $46B0C $46B12 $46C04; 32 bytes of valid code before it
mapst 00089   ; LD ($FFFC),A; after LD A,$28; 32 bytes of valid code before it
mapst 00090   ; LD ($FFFC),A; after LD A,($FFFB); JP/CALL target from $362F8; 31 bytes of valid code before it
mapst 00096   ; LD ($FFFC),A; after LD A,$28; JP/CALL target from $4B72B; 32 bytes of valid code before it
mapst 0009A   ; LD ($FFFD),A; after another mapper store, LD ($FFFC),A at $00096; 32 bytes of valid code before it
mapst 000A0   ; LD ($FFFC),A; after LD A,($FFFB); JP/CALL target from $5A3F9; 32 bytes of valid code before it
mapst 000AA   ; LD ($FFFD),A
mapst 000B5   ; LD ($FFFC),A; after LD A,$28; 32 bytes of valid code before it
mapst 026A3   ; LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 026AC   ; LD ($FFFF),A
mapst 026D7   ; LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 026E0   ; LD ($FFFF),A
mapst 05987   ; LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 0598D   ; LD ($FFFF),A; after another mapper store, LD ($FFFF),A at $05987; 32 bytes of valid code before it
page 0 ds_tiles dscol dsrow dstq dsnr dsspr
; ds_tiles: at $48E4, HL = the source in ROM (slot 2, 32-byte aligned), the VDP address
; set to $3000 for a VRAM write. Does what the game's loop $48E8-$498B does, 17 passes of
; 32 OUTI to the VDP data port (544 bytes from HL to VRAM $3000-$321F), as OTIR through
; the runtime in blocks of at most 256 bytes that stay inside one 8K page of the cart,
; so that each block holds whole aligned tiles and tilecache copies them from the
; converted cart. Returns with the registers the loop leaves: HL + 544, B - 32 (544
; OUTIs), C = $BE, A = 0 with Z set, DE kept.
ds_tiles:
        ld a,b
        sub 32
        ld (sv_b),a
        ld (sv_de),de
        ld de,544           ; bytes left
1:      ld a,h              ; BC = bytes to the end of the source's 8K page
        and $1F
        ld b,a
        xor a
        sub l
        ld c,a
        ld a,$20
        sbc a,b
        ld b,a
        ld a,c              ; at most the bytes left
        sub e
        ld a,b
        sbc a,d
        jr c,2f
        ld b,d
        ld c,e
2:      ld a,b              ; at most 256
        or a
        jr z,3f
        ld bc,$0100
3:      ld a,e              ; DE = bytes left after this block
        sub c
        ld e,a
        ld a,d
        sbc a,b
        ld d,a
        ld b,c              ; B = the block's length (0 = 256)
        ld c,$BE
        rst $00
        db $B3              ; OTIR
        ld a,d
        or e
        jr nz,1b
        ld de,(sv_de)
        ld a,(sv_b)
        ld b,a
        xor a
        ret
sv_de:  dw 0
sv_b:   db 0
; The entries that call jt_vwrite (dscol, dsrow, dsnr, dsspr) run on the page's own
; stack with interrupts off (PG_IN), and put the game's interrupt state back with the
; byte that PG_IN writes before their RET. The game calls all of these routines from
; its interrupt handler $330D, with interrupts off.
; Runtime internal used: the cart's place in Next memory, bank n in pages
; CART_PAGE + 2n with CART_PAGE = 32 (src/runtime/memplan.inc), in ms_map.

        macro PG_IN eib
        ex af,af'               ; AF' = the game's AF
        ld a,i                  ; P/V = IFF2
        di
        ld a,$FB                ; EI
        jp pe,$+4
        xor a                   ; NOP
        ld (eib),a
        ld (gsp),sp
        ld sp,stk
        ex af,af'
        push af
        push bc
        push de
        push ix
        push iy
        endm

        macro MS_IN
        PG_IN ms_ei
        exx
        ld (ms_vd),de
        exx
        endm

; Map scroll. When the map moves 8 pixels, the scroll routine $36D2 draws a new column
; of 28 cells (the unrolled loop $37A4-$3FBA) and a new row of 32 cells ($4027-$48C5).
; Each cell takes the map byte m at the map pointer (bank ($CEF0) in slot 2) and writes
; the tile word at $A000 + 32 m + row x 8 + column x 2 (bank ($CEF5)) to the name table,
; with two mapper stores, two control writes and two OUTI through the runtime. dscol
; and dsrow read all the map bytes, then all the tile words, into a buffer, and write it
; with jt_vwrite. They map the two banks into MMU4-5 themselves (ms_map), and end with
; the game's last mapper store through the runtime, so that slot 2 holds bank ($CEF5)
; as after the game's loop.

; dscol: at $3798. Main HL = the map pointer, B = the row in the metatile x 8,
; C = the column in the metatile x 2; alt DE = the VDP control word of the first cell.
; Per cell the row steps by 8, and at 32 goes to 0 with the map pointer + $80; the VDP
; word steps by $40, from $7F00 back to $7800. Returns as the loop leaves its
; registers at $3FBB: main HL moved on, DE = $0080, BC kept; alt B = the row x 8,
; C = $BE, HL = the last tile word + 2, DE = the VDP word after the last cell;
; AF' = (($CEF0), the F at the entry); A and F differ (the code at $3700 sets both).
dscol:  MS_IN
        ld a,b
        ld (ms_ra),a
        ld a,c
        ld (ms_rc),a
        ld a,($CEF0)
        call ms_map
        ld a,28
        ld (ms_wrap),a
        ld de,(ms_vd)
        ld ix,ms_ptr
        ld b,0
.cell:  call ms_tile
        ld a,(ms_ra)            ; the next row of the metatile
        add a,8
        cp $20
        jr nz,.rw
        push de
        ld de,$0080             ; the next map row
        add hl,de
        pop de
        xor a
.rw:    ld (ms_ra),a
        ld a,e                  ; the next name table row
        add a,$40
        ld e,a
        jr nc,.nw
        inc d
        ld a,d
        cp $7F
        jr nz,.nw
        ld d,$78
        ld a,b
        inc a
        ld (ms_wrap),a          ; the cells above the wrap
.nw:    inc b
        ld a,b
        cp 28
        jr nz,.cell
        ld (ms_mp),hl
        ld (ms_ve),de
        ld b,28
        call ms_copy
        ld hl,ms_buf            ; the cells down to the table's last row
        ld de,(ms_vd)
        ld a,(ms_wrap)
        ld c,a
        ld b,2
        ld ix,2
        ld iy,$40
        ld a,1                  ; the source as mapped now (this page)
        call jt_vwrite
        ld a,(ms_wrap)
        cp 28
        jr z,.done
        add a,a
        db $ED,$31              ; add hl,a: the rest from the table's first row
        ld a,(ms_vd)
        and $3F
        ld e,a
        ld d,$78
        ld a,(ms_wrap)
        neg
        add a,28
        ld c,a
        ld a,1
        call jt_vwrite
.done:  pop iy
        pop ix
        pop de
        pop bc
        pop af
        ld a,($CEF0)
        ex af,af'
        ld a,(ms_ra)
        exx
        ld b,a
        ld c,$BE
        ld de,(ms_ve)
        ld hl,(ms_tl)
        exx
        ld hl,(ms_mp)
        ld de,$0080
        jp ms_out

; dsrow: at $401E. Main HL = the map pointer, B = the column in the metatile x 2,
; C = the row in the metatile x 8; alt DE = the VDP control word of the first cell.
; Per cell the column steps by 2, and at 8 goes to 0 with L + 1; the VDP word steps by
; 2 inside its name table row (32 cells, so it ends where it started). Returns as the
; loop leaves its registers at $48C6: main HL moved on, BC and DE kept; alt B = the
; column x 2, C = $BE, H = the high byte of the last tile word + 2, L = E and $C0,
; DE kept; A = E with the flags of OR A; AF' = (($CEF0), the F at the entry).
dsrow:  MS_IN
        ld a,b
        ld (ms_rc),a
        ld a,c
        ld (ms_ra),a
        ld a,($CEF0)
        call ms_map
        ld ix,ms_ptr
        ld b,32
.cell:  call ms_tile
        ld a,(ms_rc)            ; the next column of the metatile
        add a,2
        cp 8
        jr nz,.cw
        inc l                   ; the next map byte
        xor a
.cw:    ld (ms_rc),a
        djnz .cell
        ld (ms_mp),hl
        ld b,32
        call ms_copy
        ld a,(ms_vd)            ; the cells up to the end of the name table row
        and $3F
        ld c,a
        ld a,64
        sub c
        ld b,a
        ld c,1
        ld hl,ms_buf
        ld de,(ms_vd)
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        ld a,b                  ; the rest from the start of the row
        db $ED,$31              ; add hl,a
        ld a,(ms_vd)
        and $3F
        jr z,.done
        ld b,a
        ld a,e
        and $C0
        ld e,a
        ld a,1
        call jt_vwrite
.done:  pop iy
        pop ix
        pop de
        pop bc
        pop af
        ld a,($CEF0)
        ex af,af'
        ld a,(ms_rc)
        exx
        ld b,a
        ld c,$BE
        ld de,(ms_vd)
        ld hl,(ms_tl)
        ld a,e
        and $C0
        ld l,a
        exx
        ld hl,(ms_mp)
        ld a,(ms_vd)
        ld (ms_fa),a

; ms_out: back on the game's stack, the game's last mapper store, then A = (ms_fa)
; with the flags of OR A, and the game's interrupt state.
ms_out: ld sp,(gsp)
        ld a,($CEF5)
        rst $00
        db $13,$00              ; LD ($FFFF),A through the runtime
        ld a,(ms_fa)
        or a
ms_ei:  nop
        ret

; ms_tile: the tile word's address for the map byte at HL: $A000 + 32 m + (ms_ra) +
; (ms_rc), stored at IX, IX + 2. Keeps HL, B, DE; changes A, C.
ms_tile:
        ld a,(hl)
        push hl
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld a,(ms_ra)
        ld c,a
        ld a,(ms_rc)
        or c
        or l
        ld (ix+0),a
        ld a,h
        add a,$A0
        ld (ix+1),a
        inc ix
        inc ix
        pop hl
        ret

; ms_copy: B tile words from the addresses at ms_ptr (bank ($CEF5)) to ms_buf;
; ms_tl = the last address + 2.
ms_copy:
        ld a,($CEF5)
        call ms_map
        ld ix,ms_ptr
        ld de,ms_buf
.w:     ld l,(ix+0)
        ld h,(ix+1)
        inc ix
        inc ix
        ld a,(hl)
        ld (de),a
        inc hl
        inc de
        ld a,(hl)
        ld (de),a
        inc hl
        inc de
        djnz .w
        ld (ms_tl),hl
        ret

; ms_map: cart bank A into MMU4-5 (slot 2): pages CART_PAGE + 2A and + 1, as the
; runtime's map_bank does for this 512K cart (32 banks).
ms_map: and $1F
        add a,a
        add a,32
        db $ED,$92,$54          ; nextreg $54,a
        inc a
        db $ED,$92,$55          ; nextreg $55,a
        ret

; dstq: at $11B1 and $121F, the two tile uploads of the queue routine $118F (called from
; the game's interrupt handler): a queue entry of up to 8 tiles from cart ROM in slot 2
; (the bank already mapped) to VRAM at the address already set, with a run of 32 OUTI a
; tile ($11B9-$11FC; $1227-$12CA has NOPs between them). HL = the queue pointer past the
; entry, DE = the source, A = the tiles - 1. Does what the game does: RES 7,L, HL into
; ($CF36), EX DE,HL, C = $BE; then writes the tiles as OTIR blocks through the runtime,
; at most 256 bytes each and inside one 8K page of the cart, so that each block holds
; whole aligned tiles and tilecache copies them from the converted cart. Runs on the
; game's stack with its interrupt state, as ds_tiles. Returns as the loop leaves it:
; HL = the source + 32 x tiles, DE = the queue pointer, B - 32 x tiles, C = $BE,
; A = $FF with the flags of DEC A (carry clear).
dstq:   res 7,l
        ld ($CF36),hl
        ex de,hl
        ld (tq_de),de
        ld c,a
        ld a,b
        ld (tq_b),a
        ld a,c
        inc a
        add a,a
        add a,a
        add a,a
        add a,a
        add a,a                 ; 32 x tiles (0 = 256)
        ld (tq_len),a
        ld a,h                  ; DE = the bytes to the end of the source's 8K page
        and $1F
        ld d,a
        xor a
        sub l
        ld e,a
        ld a,$20
        sbc a,d
        ld d,a
        ld a,d
        or a
        jr nz,.one              ; 256 or more
        ld a,(tq_len)
        or a
        jr z,.two               ; 256 bytes, fewer to the page's end
        cp e
        jr c,.one
        jr z,.one
.two:   ld b,e                  ; up to the page's end
        ld c,$BE
        rst $00
        db $B3                  ; OTIR
        ld a,(tq_len)
        sub e
        ld b,a                  ; the rest
        rst $00
        db $B3
        jr .end
.one:   ld a,(tq_len)
        ld b,a
        ld c,$BE
        rst $00
        db $B3
.end:   ld de,(tq_de)
        ld a,(tq_len)
        ld c,a
        ld a,(tq_b)
        sub c
        ld b,a
        ld c,$BE
        xor a
        dec a
        ret

; dsnr: at $0F76, the rows that the object drawing at $0E4C (called from the game's
; interrupt handler through $0E1A) writes into the name table: E' rows of D' cells from
; the source HL' (rows ($CE34) bytes apart, bank 2 in slot 2 in every recorded run), at
; the VDP word (A + $78, L or C). A cell whose high byte has bit 0 set gets the low byte
; (low and 7) or ($CE23 + low / 8). A row that runs past the end of its name table row
; goes on at the row's start; each next row is $40 on, from $7F00 back to $7800. The game
; sets the VDP address for every cell; jt_vwrite writes each row as runs, and when the
; game's last address wrapped to its row's start, two control writes set it.
; Returns as the loop leaves its registers at $0FEC: main HL = the VDP word of the next
; row, BC = $0040, DE kept; alt HL = the source + rows x ($CE34), B = 0, C = ($CE34),
; D kept, E = 0; AF' = ($7F, the flags of CP H for the last row's H + 1 before the wrap);
; A and F differ (the code at $0FEC sets both).
dsnr:   add a,$78
        ld h,a
        ld a,l
        or c
        ld l,a
        PG_IN nr_ei
        ld (nr_vd),hl
        exx
        ld (nr_src),hl
        ld (nr_de),de
        exx
        ld a,(nr_de)            ; E' = the rows
        ld (nr_rows),a
        xor a
        ld (nr_fix),a
.row:   ld hl,(nr_src)
        ld de,nr_buf
        ld a,(nr_de+1)          ; D' = the cells (0 = 256)
        ld b,a
.cell:  inc hl
        ld c,(hl)               ; the high byte
        dec hl
        ld a,(hl)               ; the low byte
        bit 0,c
        jr z,.raw
        push hl
        ld l,a
        and 7
        ld h,a
        ld a,l
        rrca
        rrca
        rrca
        and $1F
        add a,$23
        ld l,a
        ld a,h
        ld h,$CE
        or (hl)
        pop hl
.raw:   ld (de),a
        inc de
        ld a,c
        ld (de),a
        inc de
        inc hl
        inc hl
        djnz .cell
        ld a,(nr_de+1)          ; the bytes to write
        ld l,a
        ld h,0
        or a
        jr nz,.n
        inc h
.n:     add hl,hl
        ld (nr_bl),hl
        ld hl,nr_buf
        ld de,(nr_vd)
.run:   ld a,e                  ; the room to the end of the name table row
        and $3F
        neg
        add a,64
        ld c,a
        ld a,(nr_bl+1)
        or a
        jr nz,.full
        ld a,(nr_bl)
        cp c
        jr nc,.full
        ld c,a
.full:  ld b,c
        ld a,e
        and $3F
        add a,b
        ld (nr_end),a           ; the run's end in the row (64 = the row's end)
        ld c,1
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        ld a,b
        db $ED,$31              ; add hl,a
        ld a,e
        and $C0
        ld e,a                  ; the next run from the row's start
        ld a,(nr_bl)
        sub b
        ld (nr_bl),a
        ld a,(nr_bl+1)
        sbc a,0
        ld (nr_bl+1),a
        ld c,a
        ld a,(nr_bl)
        or c
        jr nz,.run
        ld a,(nr_end)           ; the game's last address wrapped to the row's start
        cp 64
        ld a,0
        jr nz,.nf
        inc a
.nf:    ld (nr_fix),a
        ld hl,(nr_vd)
        ld a,l
        and $C0
        ld (nr_fw),a
        ld a,h
        ld (nr_fw+1),a
        ld de,$0040             ; the next row
        add hl,de
        ld a,h
        ld (nr_hpre),a
        cp $7F
        jr nz,.nw
        ld h,$78
.nw:    ld (nr_vd),hl
        ld hl,(nr_src)
        ld a,($CE34)
        db $ED,$31              ; add hl,a
        ld (nr_src),hl
        ld a,(nr_rows)
        dec a
        ld (nr_rows),a
        jp nz,.row
        pop iy
        pop ix
        pop de
        pop bc
        pop af
        ld hl,nr_hpre
        ld a,$7F
        cp (hl)
        ex af,af'               ; AF' = ($7F, the flags of CP H)
        exx
        ld hl,(nr_src)
        ld a,($CE34)
        ld c,a
        ld b,0
        ld a,(nr_de+1)
        ld d,a
        ld e,0
        exx
        ld hl,(nr_vd)
        ld bc,$0040
        ld sp,(gsp)
        ld a,(nr_fix)
        or a
        jr z,nr_ei
        ld a,(nr_fw)            ; the game's last control word: the last row's start
        rst $00
        db $05                  ; OUT ($BF),A
        ld a,(nr_fw+1)
        rst $00
        db $05
nr_ei:  nop
        ret

; dsspr: at $3431, the sprite table writes of $341E (called from the game's interrupt
; handler) for A = n sprites (1 to 64) from the buffer at $C000 (3 bytes a sprite: Y, X,
; tile): X and tile to $3F80 (the unrolled run $3457-$3596, entered at sprite 64 - n),
; Y to $3F00 ($35AD-$36AC), then $D0 after them. Returns as the game reaches $36B1:
; A = $D0, B = -3n, C = $BE, D = 0, E = 4 x (64 - n), HL = $C002 + 3n,
; IX = $35AD + E, AF' = ($7F, the flags of XOR A); F differs (the code at $36B1 sets it).
dsspr:  PG_IN sp_ei
        ld (sp_n),a
        ld c,a
        ld hl,$C000             ; X and tile
        ld de,$7F80
        ld b,2
        ld ix,3
        ld iy,2
        ld a,1
        call jt_vwrite
        ld hl,$C002             ; Y
        ld de,$7F00
        ld b,1
        ld iy,1
        ld a,1
        call jt_vwrite
        ld hl,sp_d0             ; the end mark
        ld a,(sp_n)
        ld e,a
        ld c,1
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        pop de
        pop bc
        pop af
        ld a,(sp_n)
        ld c,a
        add a,a
        add a,c
        ld hl,$C002
        db $ED,$31              ; add hl,a: HL = $C002 + 3n
        neg
        ld b,a                  ; B = -3n
        ld a,c
        neg
        add a,$40
        add a,a
        add a,a
        ld e,a                  ; E = 4 x (64 - n)
        ld d,0
        ld ix,$35AD
        add ix,de
        ld c,$BE
        xor a
        ld a,$7F
        ex af,af'
        ld a,$D0
        ld sp,(gsp)
sp_ei:  nop
        ret

ms_vd:  dw 0                    ; the VDP word of the first cell
ms_ve:  dw 0                    ; the VDP word after the column's last cell
ms_mp:  dw 0                    ; the map pointer at the end
ms_tl:  dw 0                    ; the last tile word's address + 2
ms_ra:  db 0                    ; the row in the metatile x 8
ms_rc:  db 0                    ; the column in the metatile x 2
ms_wrap: db 0                   ; the column's cells above the name table's end
ms_fa:  db 0                    ; A at the return
gsp:    dw 0
tq_de:  dw 0
tq_b:   db 0
tq_len: db 0
nr_vd:  dw 0                    ; the VDP word of the row
nr_src: dw 0                    ; the row's source
nr_de:  dw 0                    ; DE' at the entry: D = the cells, E = the rows
nr_bl:  dw 0                    ; the row's bytes left to write
nr_fw:  dw 0                    ; the last row's start, as a VDP word
nr_rows: db 0
nr_end: db 0
nr_fix: db 0
nr_hpre: db 0
sp_n:   db 0
sp_d0:  db $D0
ms_ptr: ds 64
ms_buf: ds 64
nr_buf: ds 512
        ds 32
stk:
endpage

# Desert Strike (Europe) (En,Fr,De,Es).cht, "Infinite Lives": RAM $CED5 is the lives count
poke "Infinite lives"
ar 00CE-D509
endpoke

# Desert Strike (Europe) (En,Fr,De,Es).cht, "Infinite Armor": RAM $CED7-$CED8 is the armor,
# a 16-bit count; the two codes work only together (999 when full)
poke "Infinite armor"
ar 00CE-D7E7
ar 00CE-D803
endpoke

# Desert Strike (Europe) (En,Fr,De,Es).cht, "Infinite Fuel": RAM $CED9 is the fuel
poke "Infinite fuel"
ar 00CE-D98F
endpoke

# Desert Strike (Europe) (En,Fr,De,Es).cht, "Infinite Bullets": RAM $CEDB-$CEDC is the gun
# ammunition, a 16-bit count; the two codes work only together (9999)
poke "Infinite bullets"
ar 00CE-DB0F
ar 00CE-DC27
endpoke

# Desert Strike (Europe) (En,Fr,De,Es).cht, "Infinite Hydras": RAM $CEDD is the Hydra
# rocket count
poke "Infinite hydras"
ar 00CE-DD37
endpoke

# Desert Strike (Europe) (En,Fr,De,Es).cht, "Infinite Hellfires": RAM $CEDE is the Hellfire
# missile count
poke "Infinite hellfires"
ar 00CE-DE09
endpoke

# Desert Strike (Europe) (En,Fr,De,Es).cht, "Campaign Select" and the four "Campaign N"
# codes: RAM $CEEF is the campaign chosen on the main menu. 0 Air Supremacy, 1 Scud Buster,
# 2 Embassy City, 3 Nuclear Storm
poke "Start campaign"
ar 00CE-EF??
endpoke

# Desert Strike (Europe) (En,Fr,De,Es).cht, "Copilot Select": RAM $CEEA is the copilot
# chosen on the main menu. 0 Xavier Thomas, 1 Kris Tinmarie, 2 Carlos Valdez, 3 Dave Arrick
poke "Copilot"
ar 00CE-EA??
endpoke
