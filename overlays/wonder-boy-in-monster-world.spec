# Wonder Boy in Monster World (Europe), CRC32 7D7CE80B, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with two 600 s reference I/O logs
# (random input from power on; title, NEW GAME and story text, then random play).
# The reference logs ran no I/O instruction or mapper store that the static scan had
# not found. The game shares no code with Wonder Boy III or Wonder Boy in Monster Land.
# Decisions:
# - No free RST vector ($0008, $0010, $0018, $0028 and $0038 are the game's, $0020 and
#   $0030 are inside them), so $0000 is the io vector.
# - The status bar and the title's copyright row are line interrupt splits: the frame
#   handler sets H for the top and register 10, and the line handler in $C012 writes the
#   H of the lines below. Through the runtime that write landed about 3 lines after the
#   Master System's (game line event at line 31, register 8 write done in line 34), so
#   the top lines of the copyright row showed the old H. The rastercode routine
#   wonder-boy-in-monster-world-raster.asm works out each line's H from the same RAM,
#   so the game gets no line events while a split is set.
# - priority: name table cells with the priority bit are on screen in play: the status bar
#   (rows 0-3, every cell, no pixel of colour 0), the waves of the beach (rows 20-21) and
#   the story text box. While the rastercode table is valid the runtime does not move
#   Layer 2's X (hscroll_set returns early, and its per-line copper list does not write
#   NextReg $16), so the priority cells showed at a stale X: waves over the cliffs, the text
#   box twice. The raster routine sets Layer 2's X for the playfield's H itself (as the
#   runtime's pri_x, PIC_X = 2) and clips Layer 2 to the playfield's lines; it clips the
#   sprites out of the status bar's lines instead, where on a Master System no sprite
#   shows. Its clip values are the runtime's (clip_update); without a table it writes the
#   runtime's full clips back.
# - The byte-scan I/O patterns that no path reached are the unused bank 0 routines
#   $0358, $04C4 and $04FB, the unused bank 21 routine $B318, and graphics and data
#   (data/scan-verdicts.tsv).
name Wonder Boy in Monster World
hz 50		; No-Intro regions Europe
cart 7D7CE80B
priority
rastercode wonder-boy-in-monster-world-raster.asm
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0019B   ; OUT ($BF),A
site 0019F   ; OUT ($BF),A
site 001A8   ; OUT ($BF),A
site 001AC   ; OUT ($BF),A
site 001B8   ; OUT ($BF),A
site 001BB   ; OUT ($BF),A
site 00254   ; IN A,($DD)
site 00277   ; OUT ($BF),A
site 0027B   ; OUT ($BF),A
site 00280   ; OUT ($BF),A
site 00284   ; OUT ($BF),A
site 0028E   ; OUT ($BF),A
site 00292   ; OUT ($BF),A
site 0029B   ; OUT ($BF),A
site 0029F   ; OUT ($BF),A
site 002A9   ; OUT ($BF),A
site 002AD   ; OUT ($BF),A
site 002BE   ; OUT ($BF),A
site 002C2   ; OUT ($BF),A
site 002CC   ; OUT ($BF),A
site 002D0   ; OUT ($BF),A
site 002D8   ; OUT ($BF),A
site 002DC   ; OUT ($BF),A
site 002E6   ; OUT ($BF),A
site 002EA   ; OUT ($BF),A
site 00310   ; OUT ($BE),A
site 00313   ; OUT ($BE),A
site 00324   ; OUT ($BE),A
site 00329   ; OUT ($BE),A
site 00338   ; OUT ($BE),A
site 0033D   ; OUT ($BE),A
site 0034F   ; OUTI
site 00372   ; OUT ($BF),A
site 00375   ; OUT ($BF),A
site 0037B   ; OUTI
site 00391   ; OUTI
site 00397   ; OUT (C),A
site 003AD   ; OUT ($BF),A
site 003B1   ; OUT ($BF),A
site 003BC   ; OUT ($BF),A
site 003BF   ; OUT ($BF),A
site 003C3   ; OUTI
site 003C5   ; OUTI
site 003C7   ; OUTI
site 003C9   ; OUTI
site 003CB   ; OUTI
site 003CD   ; OUTI
site 003CF   ; OUTI
site 003D1   ; OUTI
site 003D3   ; OUTI
site 003D5   ; OUTI
site 003D7   ; OUTI
site 003D9   ; OUTI
site 003DB   ; OUTI
site 003DD   ; OUTI
site 003DF   ; OUTI
site 003E1   ; OUTI
site 003E3   ; OUTI
site 003E5   ; OUTI
site 003E7   ; OUTI
site 003E9   ; OUTI
site 003EB   ; OUTI
site 003ED   ; OUTI
site 003EF   ; OUTI
site 003F1   ; OUTI
site 003F3   ; OUTI
site 003F5   ; OUTI
site 003F7   ; OUTI
site 003F9   ; OUTI
site 003FB   ; OUTI
site 003FD   ; OUTI
site 003FF   ; OUTI
site 00401   ; OUTI
site 00403   ; OUTI
site 00405   ; OUTI
site 00407   ; OUTI
site 00409   ; OUTI
site 0040B   ; OUTI
site 0040D   ; OUTI
site 0040F   ; OUTI
site 00411   ; OUTI
site 00413   ; OUTI
site 00415   ; OUTI
site 00417   ; OUTI
site 00419   ; OUTI
site 0041B   ; OUTI
site 0041D   ; OUTI
site 0041F   ; OUTI
site 00421   ; OUTI
site 00423   ; OUTI
site 00425   ; OUTI
site 00427   ; OUTI
site 00429   ; OUTI
site 0042B   ; OUTI
site 0042D   ; OUTI
site 0042F   ; OUTI
site 00431   ; OUTI
site 00433   ; OUTI
site 00435   ; OUTI
site 00437   ; OUTI
site 00439   ; OUTI
site 0043B   ; OUTI
site 0043D   ; OUTI
site 0043F   ; OUTI
site 00441   ; OUTI
site 00443   ; OUTI
site 00445   ; OUTI
site 00447   ; OUTI
site 00449   ; OUTI
site 0044B   ; OUTI
site 0044D   ; OUTI
site 0044F   ; OUTI
site 00451   ; OUTI
site 00453   ; OUTI
site 00455   ; OUTI
site 00457   ; OUTI
site 00459   ; OUTI
site 0045B   ; OUTI
site 0045D   ; OUTI
site 0045F   ; OUTI
site 00461   ; OUTI
site 00463   ; OUTI
site 00465   ; OUTI
site 00467   ; OUTI
site 00469   ; OUTI
site 0046B   ; OUTI
site 0046D   ; OUTI
site 0046F   ; OUTI
site 00471   ; OUTI
site 00473   ; OUTI
site 00475   ; OUTI
site 00477   ; OUTI
site 00479   ; OUTI
site 0047B   ; OUTI
site 0047D   ; OUTI
site 0047F   ; OUTI
site 00481   ; OUTI
site 00483   ; OUTI
site 00485   ; OUTI
site 00487   ; OUTI
site 00489   ; OUTI
site 0048B   ; OUTI
site 0048D   ; OUTI
site 0048F   ; OUTI
site 00491   ; OUTI
site 00493   ; OUTI
site 00495   ; OUTI
site 00497   ; OUTI
site 00499   ; OUTI
site 0049B   ; OUTI
site 0049D   ; OUTI
site 0049F   ; OUTI
site 004A1   ; OUTI
site 004A3   ; OUTI
site 004A5   ; OUTI
site 004A7   ; OUTI
site 004A9   ; OUTI
site 004AB   ; OUTI
site 004AD   ; OUTI
site 004AF   ; OUTI
site 004B1   ; OUTI
site 004B3   ; OUTI
site 004B5   ; OUTI
site 004B7   ; OUTI
site 004B9   ; OUTI
site 004BB   ; OUTI
site 004BD   ; OUTI
site 004BF   ; OUTI
site 004C1   ; OUTI
site 004F3   ; OUTI
site 00546   ; OUT ($BF),A
site 0054C   ; OUT ($BF),A
site 00551   ; OUTI
site 0055B   ; OUT ($BF),A
site 00561   ; OUT ($BF),A
site 00567   ; OUT ($BE),A
site 00719   ; IN A,($00)
site 007D6   ; OUTI
site 007D8   ; OUTI
site 007DA   ; OUT (C),A
site 007DC   ; OUT (C),A
site 00925   ; OUT ($BF),A
site 00929   ; OUT ($BF),A
site 01270   ; OUT ($BF),A
site 01273   ; OUT ($BF),A
site 01275   ; OUTI
site 0127B   ; OUTI
site 01296   ; OUT ($BF),A
site 01299   ; OUT ($BF),A
site 0129B   ; OUTI
site 012A1   ; OUTI
site 012BC   ; OUT ($BF),A
site 012BF   ; OUT ($BF),A
site 012C1   ; OUTI
site 012C7   ; OUTI
site 012E2   ; OUT ($BF),A
site 012E5   ; OUT ($BF),A
site 012E7   ; OUTI
site 012ED   ; OUTI
site 0147B   ; OUT ($BE),A
site 01483   ; OUT ($BE),A
site 0149C   ; OUT ($BE),A
site 014A4   ; OUT ($BE),A
site 014AC   ; OUT ($BE),A
site 014B4   ; OUT ($BE),A
site 014CD   ; OUT ($BE),A
site 014D5   ; OUT ($BE),A
site 014E3   ; OUT ($BE),A
site 014EB   ; OUT ($BE),A
site 015B3   ; OUT ($BF),A
site 015B6   ; OUT ($BF),A
site 015FA   ; OUT ($BF),A
site 015FD   ; OUT ($BF),A
site 0163E   ; OUT ($BF),A
site 01641   ; OUT ($BF),A
site 0164E   ; OUT ($BF),A
site 01651   ; OUT ($BF),A
site 01690   ; OUT ($BF),A
site 01693   ; OUT ($BF),A
site 016D7   ; OUT ($BF),A
site 016DA   ; OUT ($BF),A
site 02205   ; OUT ($BE),A
site 02211   ; OUT ($BF),A
site 02214   ; OUT ($BF),A
site 027D5   ; OUT ($BE),A
site 027DE   ; OUT ($BE),A
site 028EF   ; OUT ($BF),A
site 028F2   ; OUT ($BF),A
site 028F4   ; OUTI
site 028F8   ; OUTI
site 02913   ; OUT ($BF),A
site 02916   ; OUT ($BF),A
site 02918   ; OUTI
site 0291C   ; OUTI
site 02937   ; OUT ($BF),A
site 0293A   ; OUT ($BF),A
site 0293C   ; OUTI
site 02940   ; OUTI
site 02B78   ; OUT ($BF),A
site 02B7B   ; OUT ($BF),A
site 02B7E   ; OUT ($BE),A
site 02B84   ; OUT ($BE),A
site 039A2   ; OUT ($BF),A
site 039AA   ; OUT ($BF),A
site 04086   ; OUT ($BE),A
site 0408C   ; OUT ($BE),A
site 04590   ; OUT ($BF),A
site 04593   ; OUT ($BF),A
site 0E04C   ; OUT ($BF),A
site 0E04F   ; OUT ($BF),A
otir 0E054   ; OUTI
site 0E05D   ; IN A,($DC)
site 0E07C   ; IN A,($7E)
site 0E089   ; OTIR
site 1E561   ; OUT ($BE),A
site 1E567   ; OUT ($BE),A
site 1E6F8   ; OUT ($BE),A
site 1E704   ; OUT ($BF),A
site 1E707   ; OUT ($BF),A
site 221A7   ; OUTI
site 221AD   ; OUTI
site 221D0   ; OUTI
site 221D6   ; OUTI
site 2222C   ; OUTI
site 22232   ; OUTI
site 22264   ; OUTI
site 2226A   ; OUTI
site 2A753   ; OUT ($BF),A
site 2A757   ; OUT ($BF),A
site 2A75B   ; OUT ($BE),A
site 2A760   ; OUT ($BF),A
site 2A764   ; OUT ($BF),A
site 2A767   ; OUT ($BE),A
site 381E0   ; OUT ($7F),A
site 38306   ; OUT ($7F),A
site 38498   ; OTIR
site 385B0   ; OUT ($7F),A
site 385BA   ; OUT ($7F),A
site 385D7   ; OUT ($7F),A
site 386DB   ; OUT ($7F),A
site 38773   ; OUT ($7F),A
site 38818   ; OUT ($7F),A
site 38821   ; OUT ($7F),A
site 38831   ; OUT ($7F),A
site 38897   ; OUT ($7F),A
site 388B4   ; OUT ($7F),A
site 55938   ; OUT ($BE),A
site 55944   ; OUT ($BF),A
site 55947   ; OUT ($BF),A
site 573D7   ; OUTI
site 573DD   ; OUTI
site 573E3   ; OUTI
site 573E9   ; OUTI
site 573EF   ; OUTI
site 573F5   ; OUTI
site 573FB   ; OUTI
site 57401   ; OUTI
site 57407   ; OUTI
site 5740D   ; OUTI
site 66791   ; OUT ($BF),A
site 66794   ; OUT ($BF),A
site 66799   ; OUT ($BF),A
site 6679D   ; OUT ($BF),A
site 667A2   ; OUT ($BF),A
site 667A6   ; OUT ($BF),A
site 667AC   ; OUT ($BF),A
site 667B0   ; OUT ($BF),A
site 667B3   ; OUT ($BF),A
site 667B7   ; OUT ($BF),A
site 667C3   ; OUT ($BF),A
site 667C6   ; OUT ($BF),A
site 667CC   ; OUT ($BF),A
site 667D0   ; OUT ($BF),A
site 667D3   ; OUT ($BF),A
site 667D7   ; OUT ($BF),A
site 667EE   ; OUT ($BF),A
site 667F2   ; OUT ($BF),A
site 66806   ; OUT ($BF),A
site 66809   ; OUT ($BF),A
site 6680E   ; OUT ($BF),A
site 66812   ; OUT ($BF),A
site 66817   ; OUT ($BF),A
site 6681B   ; OUT ($BF),A
site 66834   ; OUT ($BF),A
site 66838   ; OUT ($BF),A
site 6683B   ; OUT ($BF),A
site 6683F   ; OUT ($BF),A
site 66851   ; OUT ($BF),A
site 66854   ; OUT ($BF),A
site 6686B   ; OUT ($BF),A
site 6686F   ; OUT ($BF),A
site 66881   ; OUT ($BF),A
site 66884   ; OUT ($BF),A
site 6689B   ; OUT ($BF),A
site 6689F   ; OUT ($BF),A
site 668B1   ; OUT ($BF),A
site 668B4   ; OUT ($BF),A
mapsthl 00084   ; LD ($FFFC),HL
mapsthl 0008A   ; LD ($FFFE),HL
mapst 000D6   ; LD ($FFFF),A
mapst 0017B   ; LD ($FFFF),A
mapst 001D2   ; LD ($FFFF),A
mapst 001EA   ; LD ($FFFF),A
mapst 0020D   ; LD ($FFFF),A
mapst 00242   ; LD ($FFFF),A
mapst 00269   ; LD ($FFFF),A
mapst 0056F   ; LD ($FFFF),A
mapst 006E1   ; LD ($FFFF),A
mapst 0072D   ; LD ($FFFF),A
mapst 00795   ; LD ($FFFF),A
mapst 007A8   ; LD ($FFFF),A
mapst 007F5   ; LD ($FFFF),A
mapst 00816   ; LD ($FFFF),A
mapst 008BF   ; LD ($FFFF),A
mapst 008C6   ; LD ($FFFF),A
mapst 00912   ; LD ($FFFF),A
mapst 0092D   ; LD ($FFFF),A
mapst 0096D   ; LD ($FFFF),A
mapst 0098F   ; LD ($FFFF),A
mapst 009CE   ; LD ($FFFF),A
mapst 009D5   ; LD ($FFFF),A
mapst 00F3E   ; LD ($FFFF),A
mapst 00F66   ; LD ($FFFF),A
mapst 00F7C   ; LD ($FFFF),A
mapst 00FA7   ; LD ($FFFF),A
mapst 00FD3   ; LD ($FFFF),A
mapst 01022   ; LD ($FFFF),A
mapst 01031   ; LD ($FFFF),A
mapst 01042   ; LD ($FFFF),A
mapst 0109B   ; LD ($FFFF),A
mapst 010AA   ; LD ($FFFF),A
mapst 010D3   ; LD ($FFFF),A
mapst 01120   ; LD ($FFFF),A
mapst 01131   ; LD ($FFFF),A
mapst 01142   ; LD ($FFFF),A
mapst 01152   ; LD ($FFFF),A
mapst 0115F   ; LD ($FFFF),A
mapst 0117A   ; LD ($FFFF),A
mapst 01221   ; LD ($FFFF),A
mapst 01228   ; LD ($FFFF),A
mapst 01232   ; LD ($FFFF),A
mapst 01239   ; LD ($FFFF),A
mapst 01243   ; LD ($FFFF),A
mapst 0124A   ; LD ($FFFF),A
mapst 01254   ; LD ($FFFF),A
mapst 0125B   ; LD ($FFFF),A
mapst 012FF   ; LD ($FFFF),A
mapst 0130D   ; LD ($FFFF),A
mapst 0131B   ; LD ($FFFF),A
mapst 0136B   ; LD ($FFFF),A
mapst 013B4   ; LD ($FFFF),A
mapst 015AD   ; LD ($FFFF),A
mapst 01648   ; LD ($FFFF),A
mapst 016E2   ; LD ($FFFF),A
mapst 017BC   ; LD ($FFFF),A
mapst 017C3   ; LD ($FFFF),A
mapst 017F1   ; LD ($FFFF),A
mapst 01818   ; LD ($FFFF),A
mapst 0185A   ; LD ($FFFF),A
mapst 01861   ; LD ($FFFF),A
mapst 019AD   ; LD ($FFFF),A
mapst 01A85   ; LD ($FFFF),A
mapst 01A8C   ; LD ($FFFF),A
mapst 01B1C   ; LD ($FFFF),A
mapst 01B73   ; LD ($FFFF),A
mapst 01BBA   ; LD ($FFFF),A
mapst 01BC1   ; LD ($FFFF),A
mapst 01C07   ; LD ($FFFF),A
mapst 01CBA   ; LD ($FFFF),A
mapst 01CC1   ; LD ($FFFF),A
mapst 01CC6   ; LD ($FFFF),A
mapst 01CD4   ; LD ($FFFF),A
mapst 01CDF   ; LD ($FFFF),A
mapst 01D06   ; LD ($FFFF),A
mapst 01DAE   ; LD ($FFFF),A
mapst 01DBD   ; LD ($FFFF),A
mapst 01DC6   ; LD ($FFFF),A
mapst 01F60   ; LD ($FFFF),A
mapst 02452   ; LD ($FFFF),A
mapst 02459   ; LD ($FFFF),A
mapst 02463   ; LD ($FFFF),A
mapst 0246A   ; LD ($FFFF),A
mapst 025C0   ; LD ($FFFF),A
mapst 02689   ; LD ($FFFF),A
mapst 027E9   ; LD ($FFFF),A
mapst 0281D   ; LD ($FFFF),A
mapst 02822   ; LD ($FFFF),A
mapst 028DB   ; LD ($FFFF),A
mapst 0298B   ; LD ($FFFF),A
mapst 02A00   ; LD ($FFFF),A
mapst 02A45   ; LD ($FFFF),A
mapst 02A5E   ; LD ($FFFF),A
mapst 02A83   ; LD ($FFFF),A
mapst 02A8A   ; LD ($FFFF),A
mapst 02B11   ; LD ($FFFF),A
mapst 02B69   ; LD ($FFFF),A
mapst 02B70   ; LD ($FFFF),A
mapst 02BFC   ; LD ($FFFF),A
mapst 02C01   ; LD ($FFFF),A
mapst 02C18   ; LD ($FFFF),A
mapst 02C1D   ; LD ($FFFF),A
mapst 02C65   ; LD ($FFFF),A
mapst 02C7D   ; LD ($FFFF),A
mapst 02CC9   ; LD ($FFFF),A
mapst 02DBE   ; LD ($FFFF),A
mapst 02DCE   ; LD ($FFFF),A
mapst 02DF4   ; LD ($FFFF),A
mapst 02E0E   ; LD ($FFFF),A
mapst 02E15   ; LD ($FFFF),A
mapst 02E1E   ; LD ($FFFF),A
mapst 02ECB   ; LD ($FFFF),A
mapst 02F07   ; LD ($FFFF),A
mapst 0309A   ; LD ($FFFF),A
mapst 030B2   ; LD ($FFFF),A
mapst 0314F   ; LD ($FFFF),A
mapst 03162   ; LD ($FFFF),A
mapst 031CF   ; LD ($FFFF),A
mapst 031FD   ; LD ($FFFF),A
mapst 0320B   ; LD ($FFFF),A
mapst 03469   ; LD ($FFFF),A
mapst 03470   ; LD ($FFFF),A
mapst 034CC   ; LD ($FFFF),A
mapst 03523   ; LD ($FFFF),A
mapst 0353F   ; LD ($FFFF),A
mapst 03546   ; LD ($FFFF),A
mapst 03556   ; LD ($FFFF),A
mapst 0355D   ; LD ($FFFF),A
mapst 03569   ; LD ($FFFF),A
mapst 03570   ; LD ($FFFF),A
mapst 03592   ; LD ($FFFF),A
mapst 03599   ; LD ($FFFF),A
mapst 03612   ; LD ($FFFF),A
mapst 03657   ; LD ($FFFF),A
mapst 03676   ; LD ($FFFF),A
mapst 0367D   ; LD ($FFFF),A
mapst 039D2   ; LD ($FFFF),A
mapst 03A08   ; LD ($FFFF),A
mapst 03A1C   ; LD ($FFFF),A
mapst 03A5C   ; LD ($FFFF),A
mapst 03A90   ; LD ($FFFF),A
mapst 03AB7   ; LD ($FFFF),A
mapst 03AE9   ; LD ($FFFF),A
mapst 03B2E   ; LD ($FFFF),A
mapst 03BBE   ; LD ($FFFF),A
mapst 03BEA   ; LD ($FFFF),A
mapst 03BF1   ; LD ($FFFF),A
mapst 03C61   ; LD ($FFFF),A
mapst 03C80   ; LD ($FFFF),A
mapst 03C87   ; LD ($FFFF),A
mapst 03D29   ; LD ($FFFF),A
mapst 03DA1   ; LD ($FFFF),A
mapst 03E52   ; LD ($FFFF),A
mapst 03FCA   ; LD ($FFFF),A
mapst 04010   ; LD ($FFFF),A
mapst 04017   ; LD ($FFFF),A
mapst 04022   ; LD ($FFFF),A
mapst 04039   ; LD ($FFFF),A
mapst 04068   ; LD ($FFFF),A
mapst 040A5   ; LD ($FFFF),A
mapst 040D9   ; LD ($FFFF),A
mapst 040F4   ; LD ($FFFF),A
mapst 04111   ; LD ($FFFF),A
mapst 0416E   ; LD ($FFFF),A
mapst 04346   ; LD ($FFFF),A
mapst 04378   ; LD ($FFFF),A
mapst 0437F   ; LD ($FFFF),A
mapst 043DF   ; LD ($FFFF),A
mapst 0447A   ; LD ($FFFF),A
mapst 04481   ; LD ($FFFF),A
mapst 04490   ; LD ($FFFF),A
mapst 04497   ; LD ($FFFF),A
mapst 0452E   ; LD ($FFFF),A
mapst 0455C   ; LD ($FFFF),A
mapst 04564   ; LD ($FFFF),A
mapst 04584   ; LD ($FFFF),A
mapst 045C5   ; LD ($FFFF),A
mapst 045D1   ; LD ($FFFF),A
mapst 04665   ; LD ($FFFF),A
mapst 04673   ; LD ($FFFF),A
mapst 04E01   ; LD ($FFFF),A
mapst 0520B   ; LD ($FFFF),A
mapst 05212   ; LD ($FFFF),A
mapst 05331   ; LD ($FFFF),A
mapst 062B5   ; LD ($FFFF),A
mapst 075E3   ; LD ($FFFF),A
mapst 07608   ; LD ($FFFF),A
mapst 076CD   ; LD ($FFFF),A
mapst 07711   ; LD ($FFFF),A
mapst 078CF   ; LD ($FFFF),A
mapst 078E9   ; LD ($FFFF),A
mapst 0796C   ; LD ($FFFF),A
mapst 07990   ; LD ($FFFF),A
mapst 07D97   ; LD ($FFFF),A
mapst 5A996   ; LD ($FFFF),A
# CHECK cartarea_store at 3899F ($899F bank 14): 02  LD (BC),A $0202
# CHECK cartarea_store at 38A10 ($8A10 bank 14): 02  LD (BC),A $0201
# CHECK cartarea_store at 38A28 ($8A28 bank 14): 02  LD (BC),A $0201
# CHECK cartarea_store at 38A61 ($8A61 bank 14): 02  LD (BC),A $0101
# CHECK cartarea_store at 38A62 ($8A62 bank 14): 02  LD (BC),A $0101
# CHECK cartarea_store at 38A63 ($8A63 bank 14): 02  LD (BC),A $0101
# CHECK cartarea_store at 38A64 ($8A64 bank 14): 02  LD (BC),A $0101
# CHECK cartarea_store at 38A65 ($8A65 bank 14): 02  LD (BC),A $0101
# CHECK cartarea_store at 38A86 ($8A86 bank 14): 02  LD (BC),A $0201
# CHECK indirect_unresolved at 00273 ($0273 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 5AA2A ($AA2A bank 22): C9  RET 
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00189   # LD ($FFFF),A; after LD A,$19; JP/CALL target from $4036E $58AAB; 32 bytes of valid code before it
mapst 00202   # LD ($FFFF),A; after LD A,$19; JP/CALL target from $09089 $14A53 $14B8D $1ACCC; 32 bytes of valid code before it
# CHECK high: site 00362  OUTI  (port in C; branch target from $0036B $0036E; 32 bytes of valid code before it)
# CHECK low: site 00368  OUT (C),A  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 004D8  OUT (C),D  (port in C; branch target from $004D4; 32 bytes of valid code before it)
# CHECK medium: site 00510  OUTD  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00516  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK low: site 0A763  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 0A7B1  IN A,($BD)  (vdp_status; 8 bytes of valid code before it)
# CHECK low: site 0A813  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 0A883  IN A,($BD)  (vdp_status; 13 bytes of valid code before it)
# CHECK low: site 0A88B  IN A,($BD)  (vdp_status; 21 bytes of valid code before it; no valid code after it)
# CHECK low: site 0A8DD  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 12 bytes of valid code before it)
# CHECK low: site 0A9C1  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0A9C9  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0AB66  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 24 bytes of valid code before it)
# CHECK low: site 0AB6E  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0AB92  IN A,($BD)  (vdp_status; 14 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0ABDD  IN A,($BD)  (vdp_status; 15 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0AC40  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0ACB0  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0ACB8  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0AD26  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0AE4B  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0AE53  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0AFBD  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0AFC5  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 0C542  IN A,($BD)  (vdp_status; 16 bytes of valid code before it)
# CHECK low: site 0CF1D  OUT ($7F),A  (psg; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 0DB07  IN A,(C)  (port in C; 10 bytes of valid code before it)
# CHECK low: site 1489C  IN A,($BF)  (vdp_status; no evidence)
# CHECK low: site 18DA2  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 18DAD  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 18DC0  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 19202  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 23 bytes of valid code before it)
# CHECK low: site 193ED  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 19452  IN A,($7F)  (h_counter; no evidence)
# CHECK low: site 199F3  IN A,($DC)  (joypad_a; 5 RST or NOP opcodes around it (looks like data))
# CHECK low: site 1D7DC  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1D7F4  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1D84B  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1D98D  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1D995  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1D99D  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1D9A5  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1DC61  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 1DC79  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 30 bytes of valid code before it)
# CHECK low: site 1DCCF  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 29 bytes of valid code before it)
# CHECK low: site 1DDB9  IN A,($BD)  (vdp_status; 15 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1DDC1  IN A,($BD)  (vdp_status; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1DDC9  IN A,($BD)  (vdp_status; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1DDD1  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2DAC1  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 17 bytes of valid code before it)
# CHECK low: site 2DAC9  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 25 bytes of valid code before it)
# CHECK low: site 2DD79  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2DD81  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2DF5F  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 28 bytes of valid code before it)
# CHECK low: site 2DF67  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2E1E8  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2E1F0  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 31581  OUT ($3F),A  (io_control; no valid code after it)
# CHECK low: site 3501E  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3503F  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 11 bytes of valid code before it)
# CHECK low: site 3514E  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 351D3  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3520B  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35213  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3521E  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35226  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3522E  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35236  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3523E  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3526E  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 14 bytes of valid code before it)
# CHECK low: site 35276  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 22 bytes of valid code before it)
# CHECK low: site 3527E  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 30 bytes of valid code before it)
# CHECK low: site 35286  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3528E  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35296  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3529F  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 352A7  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 352AF  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 352B7  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 352BF  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35301  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35309  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35311  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35319  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35321  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35329  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35331  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35339  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 35359  IN A,($BD)  (vdp_status; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35361  IN A,($BD)  (vdp_status; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35369  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35371  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35379  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35381  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35389  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35391  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35399  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 353A1  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 353D9  IN A,($BD)  (vdp_status; 17 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 353E1  IN A,($BD)  (vdp_status; 15 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 353E9  IN A,($BD)  (vdp_status; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 353F1  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 353F9  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35401  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35409  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35411  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35419  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35421  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35429  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35431  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35439  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35441  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3544A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35452  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3545A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35462  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3546A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35472  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3547A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35482  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3548A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35492  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3549A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 354A2  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 354AC  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 354CE  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35620  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 356A6  IN A,($BD)  (vdp_status; 13 bytes of valid code before it; no valid code after it)
# CHECK low: site 356E2  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 356EA  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35722  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3572A  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35732  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3573A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35742  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 35770  IN A,($BD)  (vdp_status; 18 bytes of valid code before it)
# CHECK high: site 35778  IN A,($BD)  (vdp_status; branch target from $357D9; 26 bytes of valid code before it)
# CHECK low: site 35780  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 31 bytes of valid code before it)
# CHECK low: site 35788  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35790  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35798  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 357A0  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 357A8  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 357B0  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 357B8  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 357C0  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 35802  IN A,($BD)  (vdp_status; 32 bytes of valid code before it)
# CHECK low: site 3580A  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35812  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3581A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35822  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3582A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35832  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3583A  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 3585B  IN A,($BD)  (vdp_status; 8 bytes of valid code before it)
# CHECK medium: site 35863  IN A,($BD)  (vdp_status; 16 bytes of valid code before it)
# CHECK low: site 3586B  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 24 bytes of valid code before it)
# CHECK low: site 35873  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3587B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35883  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3588B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35893  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3589B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 358A3  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 358DB  IN A,($BD)  (vdp_status; 15 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 358E3  IN A,($BD)  (vdp_status; branch target from $358B1; 32 bytes of valid code before it)
# CHECK low: site 358EB  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 358F3  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 358FB  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35903  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3590B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35913  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3591B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35923  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3592B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35933  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3593B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35943  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3594B  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35954  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3595C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35964  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3596C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35974  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3597C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35984  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3598C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 35994  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3599C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 359A4  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 3D54B  IN A,($F0)  (joypad_a; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3D7F1  OUT ($3F),A  (io_control; no valid code after it)
# CHECK low: site 421C0  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 4DB02  IN A,($C1)  (joypad_b_misc; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 4E363  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 50AB7  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 50ABF  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 50B0B  IN A,($BD)  (vdp_status; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 50B13  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 50B4F  IN A,($BD)  (vdp_status; 12 bytes of valid code before it; no valid code after it)
# CHECK low: site 50B68  IN A,($BD)  (vdp_status; 15 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 50B70  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 50E6F  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 50FA0  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 519AB  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 51A2C  IN A,($BF)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 51D1C  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 31 bytes of valid code before it)
# CHECK low: site 51D6B  IN A,($BD)  (vdp_status; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 51E37  IN A,($BD)  (vdp_status; 13 RST or NOP opcodes around it (looks like data); 28 bytes of valid code before it)
# CHECK low: site 521D5  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 52224  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 535E0  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 537C1  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 537C9  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 537D8  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 537E0  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 537EF  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 537F7  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 537FF  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 53807  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5381F  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 53827  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 53832  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5383A  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 53845  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5384D  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5385D  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 53865  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 53881  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 53889  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 538AD  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 538B5  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 538D1  IN A,($BD)  (vdp_status; 8 bytes of valid code before it)
# CHECK medium: site 538D9  IN A,($BD)  (vdp_status; 16 bytes of valid code before it)
# CHECK low: site 56AA5  IN A,($C0)  (joypad_a; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5731A  OUT ($BF),A  (vdp_control; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5731D  OUT ($BF),A  (vdp_control; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 5733B  OUT ($BF),A  (vdp_control; after LD A,($DD00); 32 bytes of valid code before it)
# CHECK high: site 5733F  OUT ($BF),A  (vdp_control; after LD A,$88; 32 bytes of valid code before it)
# CHECK low: site 5D4CB  IN A,($7F)  (h_counter; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 603C2  IN A,($BD)  (vdp_status; 17 bytes of valid code before it)
# CHECK low: site 603CA  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 25 bytes of valid code before it)
# CHECK low: site 603D2  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60404  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60439  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 21 bytes of valid code before it)
# CHECK low: site 60441  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 29 bytes of valid code before it)
# CHECK low: site 60476  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 60493  OUT ($DC),A  (no_effect; branch target from $60501; 32 bytes of valid code before it)
# CHECK low: site 604A8  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 604B0  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60518  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60584  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 606E3  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 19 bytes of valid code before it)
# CHECK low: site 6073E  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 60766  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 607B8  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 30 bytes of valid code before it)
# CHECK low: site 607E0  IN A,($BD)  (vdp_status; no valid code after it)
# CHECK low: site 60853  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6085B  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60863  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60893  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 22 bytes of valid code before it)
# CHECK low: site 608C7  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 608CF  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 60901  IN A,($BD)  (vdp_status; 32 bytes of valid code before it)
# CHECK low: site 6093A  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60942  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 609A6  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60A03  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60B48  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 60BA6  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60BCE  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60BDF  IN A,($C0)  (joypad_a; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 60C25  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 60C4C  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61184  OUT ($7F),A  (psg; branch target from $6116A; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 618A2  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 21 bytes of valid code before it)
# CHECK low: site 618D7  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 15 bytes of valid code before it)
# CHECK low: site 6198E  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 619F6  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 619FE  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61A5F  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 10 bytes of valid code before it)
# CHECK low: site 61AAA  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61AB2  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 61B24  IN A,($BD)  (vdp_status; 18 bytes of valid code before it)
# CHECK low: site 61B5D  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61BC8  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 14 bytes of valid code before it)
# CHECK low: site 61C3A  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61D2A  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 18 bytes of valid code before it)
# CHECK low: site 61D3A  IN A,($BD)  (vdp_status; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61D72  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 61E10  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61E76  IN A,($BD)  (vdp_status; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61E7E  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61ED4  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61F1E  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61F26  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61FA1  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 61FD1  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 21 bytes of valid code before it)
# CHECK low: site 62040  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 620AF  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 6218C  IN A,($BD)  (vdp_status; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 62467  IN A,($C1)  (joypad_b_misc; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 68A65  OUT ($BD),A  (vdp_control; no evidence)
# CHECK medium: site 697D0  IN A,($BD)  (vdp_status; 31 bytes of valid code before it)
# CHECK low: site 697D8  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 697E0  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 697E8  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 697F0  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 697F8  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69800  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69808  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69848  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 26 bytes of valid code before it)
# CHECK high: site 69850  IN A,($BD)  (vdp_status; branch target from $698B2; 32 bytes of valid code before it)
# CHECK low: site 69858  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69860  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69868  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69870  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69878  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69880  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69888  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69890  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 698CA  IN A,($BD)  (vdp_status; 24 bytes of valid code before it)
# CHECK low: site 698D2  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 698DA  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 698E2  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 698EA  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 698F2  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 698FA  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69902  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 69946  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6994E  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69956  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6995E  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69966  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6996E  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69976  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6997E  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 699C6  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 699CE  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 699D6  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 699DE  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 699E6  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 699EE  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 699F6  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 699FE  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69A4C  IN A,($BD)  (vdp_status; no evidence)
# CHECK medium: site 69A54  IN A,($BD)  (vdp_status; 15 bytes of valid code before it)
# CHECK low: site 69A5C  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 23 bytes of valid code before it)
# CHECK low: site 69A64  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 31 bytes of valid code before it)
# CHECK low: site 69A6C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69A74  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69A7C  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69ACB  IN A,($BD)  (vdp_status; no evidence)
# CHECK medium: site 69AD3  IN A,($BD)  (vdp_status; 15 bytes of valid code before it)
# CHECK low: site 69ADB  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 23 bytes of valid code before it)
# CHECK low: site 69AE3  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 31 bytes of valid code before it)
# CHECK low: site 69AEB  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69AF3  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69AFB  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69B48  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 18 bytes of valid code before it)
# CHECK low: site 69B50  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 26 bytes of valid code before it)
# CHECK low: site 69B58  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69B60  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69B68  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69B70  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69B78  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69BC2  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69BCA  IN A,($BD)  (vdp_status; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69BD2  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69BDA  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69BE2  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69BEA  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69BF2  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69C38  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69C40  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69C48  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69C50  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 69C8D  IN A,($BD)  (vdp_status; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69C95  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69C9D  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69CA5  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69CC2  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69CFB  IN A,($BD)  (vdp_status; 14 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D03  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D0B  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D13  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D1B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D23  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D2B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D33  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D71  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D79  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D81  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D89  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D91  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69D99  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69DA1  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69DA9  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69DB1  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69DB9  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69DEB  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69DF3  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69DFB  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E03  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E0B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E13  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E1B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E23  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E63  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E6B  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E73  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E7B  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E83  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E8B  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E93  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E9B  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69ED5  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 26 bytes of valid code before it)
# CHECK low: site 69EDD  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69EE5  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69EED  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69EF5  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69EFD  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F05  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F0D  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F54  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F5C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F64  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F6C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F74  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F7C  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69F84  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69FCE  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69FD6  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69FDE  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69FE6  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69FEE  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 69FF6  IN A,($BD)  (vdp_status; branch target from $69FBC; 32 bytes of valid code before it)
# CHECK low: site 69FFE  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A035  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 25 bytes of valid code before it)
# CHECK low: site 6A03D  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A045  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A04D  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A055  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A05D  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A065  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A0A5  IN A,($BD)  (vdp_status; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 6A0AD  IN A,($BD)  (vdp_status; branch target from $6A09B; 32 bytes of valid code before it)
# CHECK low: site 6A0B5  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A0BD  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A0C5  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A0CD  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A0D5  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A110  IN A,($BD)  (vdp_status; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A118  IN A,($BD)  (vdp_status; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 6A120  IN A,($BD)  (vdp_status; branch target from $6A19D; 32 bytes of valid code before it)
# CHECK low: site 6A128  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A16D  IN A,($BD)  (vdp_status; 14 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A175  IN A,($BD)  (vdp_status; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A17D  IN A,($BD)  (vdp_status; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6A185  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 6A1A5  IN A,($BD)  (vdp_status; 26 bytes of valid code before it)
# CHECK low: site 71114  OUT (C),L  (port in C; no evidence)
# CHECK low: site 71194  OUT (C),L  (port in C; no valid code after it)
# CHECK low: site 74F4B  IN A,($7F)  (h_counter; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 75137  IN A,($BE)  (vdp_data; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 7B5CB  IN A,($7F)  (h_counter; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 7EBC8  OUT ($3E),A  (memory_control; branch target from $7EBC6; 32 bytes of valid code before it)

# The hero's tiles: in a frame with new hero art (every swing, and other moves), the frame
# handler's $4514 writes 18 tiles (576 bytes, VRAM $2000) and then $03A5 writes the sprite
# table. Through the OUTI sites the handler ran about 100 lines: the 576 bytes pass the
# runtime's 512-byte early tile conversion (tw_check), and the once-a-frame work ran between
# the tiles and the sprite table, so for one frame the Next showed the old pose's sprites
# with the new pose's tiles. The page writes the sprite table first and then the tiles, both
# with jt_vwrite; the early conversion runs at the end of the tile write, when the VRAM copy
# holds both, so the work never sees one without the other. On the Master System both land
# in the same vertical blank, so the order does not show.
asm 04567 27   ; LD DE,$6000 ... CALL $0443 : RET (VRAM $2000, 4 x 128 + 64 bytes from HL)
    rst $00
    db far_io, pg_hero_art, ent_hero_art
    ld de,$6000            ; DE and A as the game's control write leaves them
    ld a,$60
    ret
endasm
page 0 hero_art
; hero_art: HL = the hero's art in the game's slot 2 (bank $19 or $1F, mapped by $452E).
; First $03A5's work: when $C27B is set, clear it and write the sprite table, 64 bytes from
; $C200 to VRAM $3F00 and 128 from $C280 to $3F80; the game's own CALL $03A5 after this
; then finds $C27B clear and returns. Then the 576 bytes from HL to VRAM $2000, as 18 runs of
; 32. Leaves HL = source + 576, B = B - 64 and C = $BE, as the 576 OUTIs leave them; the VDP
; address is $2240. Runs with interrupts off (the frame handler). Keeps DE, IX, IY.
hero_art:
        push ix
        push iy
        push de
        push bc
        push hl
        ld a,($C27B)
        or a
        jr z,.tiles
        xor a
        ld ($C27B),a
        ld ix,0
        ld iy,0
        ld hl,$C200
        ld de,$3F00
        ld bc,$4001             ; 64 bytes, 1 run
        call jt_vwrite
        ld hl,$C280
        ld de,$3F80
        ld b,128
        xor a
        call jt_vwrite
.tiles: pop hl
        ld ix,32
        ld iy,32
        ld de,$2000
        ld bc,$2012             ; B = 32 bytes a run, C = 18 runs
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld bc,576
        add hl,bc
        pop bc
        ld a,b
        sub 64
        ld b,a
        ld c,$BE
        pop de
        pop iy
        pop ix
        ret
endpage

# Wonder Boy in Monster World (Europe).cht, "Infinite Health": RAM $C58D is the health in
# quarter hearts, $0C when full. Hits still land, but the health is refilled each frame
poke "Infinite health"
ar 00C5-8D0C
endpoke

# Wonder Boy in Monster World (Europe).cht, "Invulnerability": RAM $C312 is the timer that
# runs after a hit; held at $3E, no hit lands
poke "Invulnerability"
ar 00C3-123E
endpoke

# Wonder Boy in Monster World (Europe).cht, "Infinite Gold": RAM $C67D and $C67E are the
# gold, held at 65535
poke "Infinite gold"
ar 00C6-7DFF
ar 00C6-7EFF
endpoke

# Wonder Boy in Monster World (Europe).cht, "Shion Starts With Maximum Hearts": RAM $C58B is
# the number of heart containers. The health is not raised; use Infinite health with it
poke "Eight hearts"
ar 00C5-8B08
endpoke

# Wonder Boy in Monster World (Europe).cht, "Shion Can Multi-Jump": RAM $C670 allows a jump
# in mid-air each time Button 2 is pressed
poke "Jump in mid-air"
ar 00C6-7001
endpoke

# Wonder Boy in Monster World (Europe).cht, "Walk Through Walls": the wall check in cart
# bank 1 at $48D7 is changed so that walls no longer block
poke "Walk through walls"
gg C98-D7B-C49
endpoke

# Wonder Boy in Monster World (Europe) (Action Replay).cht, "Shion Has ?? Armor Equipped":
# RAM $C59E is the armor worn. $00 is none, $06 takes the least damage (proved: 01, 03, 05, 06)
poke "Armor ??"
ar 00C5-9E??
endpoke

# Wonder Boy in Monster World (Europe) (Action Replay).cht, "Shion Has ?? Boots Equipped":
# RAM $C5AA is the boots worn. A higher value walks faster (proved: 01, 03, 06)
poke "Boots ??"
ar 00C5-AA??
endpoke
