# Alex Kidd in Miracle World (USA, Europe, Brazil) (Rev 1), AED9AAC4, drafted by tools/mkspec.py from sitescan output.
name Alex Kidd in Miracle World
cart AED9AAC4
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
otir 00033   ; OUTI
site 000CE   ; IN A,($BF)
site 000D0   ; IN A,($DD)
site 00142   ; OUT ($BE),A
otir 0014F   ; OUTI
site 0015F   ; OUTI
site 00163   ; OUT (C),A
site 0018B   ; OUT ($BE),A
site 00198   ; OUTI
site 001CB   ; OUT ($BE),A
site 001EA   ; OUT (C),D
otir 00212   ; OUTI
otir 0021F   ; OUTI
otir 00235   ; OUTI
site 00241   ; OUTD
site 00247   ; OUT ($BE),A
otir 00252   ; OUTI
site 00263   ; OUTI
site 00265   ; OUTD
site 00271   ; OTIR
site 00274   ; OUT ($BE),A
site 002A9   ; OUT ($BF),A
site 002AC   ; OUT ($BF),A
site 002AF   ; OUT ($BE),A
site 002CE   ; OUT ($BE),A
site 00352   ; OUT ($DF),A
site 0035E   ; OUT ($DE),A
site 00360   ; IN A,($DE)
site 0036F   ; IN A,($DC)
site 00376   ; OUT ($DE),A
site 00378   ; IN A,($DC)
site 0037D   ; OUT ($DE),A
site 0037F   ; IN A,($DC)
site 0038A   ; OUT ($DE),A
site 0038C   ; IN A,($DC)
site 00397   ; OUT ($DE),A
site 00399   ; IN A,($DC)
site 003AB   ; OUT ($DE),A
site 003AD   ; IN A,($DC)
site 003B8   ; OUT ($DE),A
site 003BA   ; IN A,($DC)
site 00470   ; OUT ($BE),A
site 00477   ; OUT ($BE),A
site 041E2   ; OUTI
site 041E4   ; OUTI
site 041E6   ; OUTI
site 041E8   ; OUT ($BE),A
site 041EA   ; OUTI
site 041EC   ; OUTI
site 041EE   ; OUTI
site 041F0   ; OUT ($BE),A
site 041F2   ; OUTI
site 041F4   ; OUTI
site 041F6   ; OUTI
site 041F8   ; OUT ($BE),A
site 041FA   ; OUTI
site 041FC   ; OUTI
site 041FE   ; OUTI
site 04200   ; OUT ($BE),A
site 04202   ; OUTI
site 04204   ; OUTI
site 04206   ; OUTI
site 04208   ; OUT ($BE),A
site 0420A   ; OUTI
site 0420C   ; OUTI
site 0420E   ; OUTI
site 04210   ; OUT ($BE),A
site 04212   ; OUTI
site 04214   ; OUTI
site 04216   ; OUTI
site 04218   ; OUT ($BE),A
site 0421A   ; OUTI
site 0421C   ; OUTI
site 0421E   ; OUTI
site 04220   ; OUT ($BE),A
site 04366   ; OUT ($BE),A
site 0436B   ; IN A,($BE)
site 04BE7   ; OUT ($BE),A
site 06952   ; OUT ($BE),A
site 06957   ; OUT ($BE),A
site 07F3F   ; OUT ($BE),A
site 07F43   ; OUT ($BE),A
site 099CE   ; OUT ($7F),A
site 099E1   ; OUT ($7F),A
site 09D96   ; OUT ($7F),A
site 09DF0   ; OUT ($7F),A
site 09E0A   ; OTIR
site 09E11   ; OUT ($7F),A
site 09E15   ; OUT ($7F),A
mapst 00087   ; LD ($FFFF),A
mapst 000A1   ; LD ($FFFF),A
mapst 00109   ; LD ($FFFF),A
mapst 00114   ; LD ($FFFF),A
mapst 00789   ; LD ($FFFF),A
mapst 007AD   ; LD ($FFFF),A
mapld 00867   # loads HL with $FFFF, then stores $84 through it
mapst 00926   ; LD ($FFFF),A
mapst 00A14   ; LD ($FFFF),A
mapst 00A37   ; LD ($FFFF),A
mapst 00AC5   ; LD ($FFFF),A
mapst 00B3C   ; LD ($FFFF),A
mapst 00B4A   ; LD ($FFFF),A
mapst 00B7A   ; LD ($FFFF),A
mapst 00CB0   ; LD ($FFFF),A
mapst 00CCA   ; LD ($FFFF),A
mapst 00CF0   ; LD ($FFFF),A
mapst 01101   ; LD ($FFFF),A
mapst 01136   ; LD ($FFFF),A
mapst 01520   ; LD ($FFFF),A
mapst 01546   ; LD ($FFFF),A
mapst 0154C   ; LD ($FFFF),A
mapst 0155D   ; LD ($FFFF),A
mapst 015A8   ; LD ($FFFF),A
mapst 016E2   ; LD ($FFFF),A
mapst 0195F   ; LD ($FFFF),A
mapst 01975   ; LD ($FFFF),A
mapst 019CD   ; LD ($FFFF),A
mapst 01A03   ; LD ($FFFF),A
mapst 01A53   ; LD ($FFFF),A
mapst 01A67   ; LD ($FFFF),A
mapst 01ADF   ; LD ($FFFF),A
mapst 01B12   ; LD ($FFFF),A
mapst 01B28   ; LD ($FFFF),A
mapst 01B30   ; LD ($FFFF),A
mapst 01C06   ; LD ($FFFF),A
mapst 01FEE   ; LD ($FFFF),A
mapst 02037   ; LD ($FFFF),A
mapst 0204F   ; LD ($FFFF),A
mapst 0205D   ; LD ($FFFF),A
mapst 0207E   ; LD ($FFFF),A
mapst 020A1   ; LD ($FFFF),A
mapst 020DB   ; LD ($FFFF),A
mapst 020E7   ; LD ($FFFF),A
mapst 021D9   ; LD ($FFFF),A
mapst 02238   ; LD ($FFFF),A
mapst 02260   ; LD ($FFFF),A
mapst 022AF   ; LD ($FFFF),A
mapst 022C2   ; LD ($FFFF),A
mapst 022E8   ; LD ($FFFF),A
mapst 023A6   ; LD ($FFFF),A
mapst 02503   ; LD ($FFFF),A
mapst 025F4   ; LD ($FFFF),A
mapst 0260E   ; LD ($FFFF),A
mapst 041CA   ; LD ($FFFF),A
mapst 0424D   ; LD ($FFFF),A
mapst 042FA   ; LD ($FFFF),A
mapst 0437F   ; LD ($FFFF),A
mapst 043CC   ; LD ($FFFF),A
mapst 04BA0   ; LD ($FFFF),A
mapst 0606E   ; LD ($FFFF),A
mapst 06079   ; LD ($FFFF),A
mapst 06260   ; LD ($FFFF),A
mapst 06271   ; LD ($FFFF),A
mapst 065B9   ; LD ($FFFF),A
mapst 066CA   ; LD ($FFFF),A
mapst 0684F   ; LD ($FFFF),A
mapst 06879   ; LD ($FFFF),A
mapst 06A92   ; LD ($FFFF),A
mapst 06B33   ; LD ($FFFF),A
mapst 06B4B   ; LD ($FFFF),A
mapst 07201   ; LD ($FFFF),A
mapst 07934   ; LD ($FFFF),A
# CHECK indirect_unresolved at 00029 ($0029 bank 0): JP (HL) 
# CHECK indirect_unresolved at 01088 ($1088 bank 0): JP (HL) 
# CHECK indirect_unresolved at 015AE ($15AE bank 0): JP (HL) 
# CHECK indirect_unresolved at 06461 ($6461 bank 1): JP (HL) 
# CHECK indirect_unresolved at 06F47 ($6F47 bank 1): JP (HL) 
# CHECK bank_unresolved at 01A56 ($1A56 bank 0): CALL $9DF3 $9DF3
# CHECK bank_unresolved at 01FE9 ($1FE9 bank 0): CALL $9DF3 $9DF3
# CHECK bank_unresolved at 025D3 ($25D3 bank 0): CALL $9DF3 $9DF3
# CHECK bank_unresolved at 048B4 ($48B4 bank 1): CALL $99D3 $99D3
# CHECK bank_unresolved at 04B74 ($4B74 bank 1): CALL $99D3 $99D3
# CHECK bank_unresolved at 07447 ($7447 bank 1): CALL $99D3 $99D3
# CHECK bank_unresolved at 074F7 ($74F7 bank 1): CALL $99D3 $99D3
# CHECK bank_unresolved at 0792F ($792F bank 1): CALL $9DF3 $9DF3
# low-confidence byte patterns checked by hand: real code (VRAM read and write routines, not run in the detector run)
site 00172   ; INI
site 001AF   ; OUTI
site 001B5   ; OUT (C),A
# the other low-confidence patterns are data or instruction operands
# Mapper stores the draft missed: LD ($FFFF),A in banks 0-1 that no
# scanned path reached, found by sitescan's byte scan. Each follows LD A,n
# (banks $82-$87) inside a routine that loads graphics or sets up a scene.
# "ran in the reference run": the SMS reference MAME saw it write the mapper.
mapst 004BE   ; LD ($FFFF),A
mapst 01689   ; LD ($FFFF),A
mapst 01760   ; LD ($FFFF),A
mapst 01773   ; LD ($FFFF),A
mapst 017A3   ; LD ($FFFF),A
mapst 01806   ; LD ($FFFF),A
mapst 018B0   ; LD ($FFFF),A
mapst 018D6   ; LD ($FFFF),A
mapst 018E4   ; LD ($FFFF),A
mapst 01C3B   ; LD ($FFFF),A
mapst 01C95   ; LD ($FFFF),A
mapst 01C9D   ; LD ($FFFF),A
mapst 01CAB   ; LD ($FFFF),A
mapst 01CBB   ; LD ($FFFF),A
mapst 01CEE   ; LD ($FFFF),A
mapst 01D37   ; LD ($FFFF),A
mapst 01D57   ; LD ($FFFF),A
mapst 01D8D   ; LD ($FFFF),A
mapst 01DA0   ; LD ($FFFF),A
mapst 01E33   ; LD ($FFFF),A
mapst 01E99   ; LD ($FFFF),A
mapst 06C32   # ran in the reference run
mapst 06DAF   # ran in the reference run
mapst 07E46   ; LD ($FFFF),A
mapst 07ED5   ; LD ($FFFF),A
mapst 07EF3   ; LD ($FFFF),A
