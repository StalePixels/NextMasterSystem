# Spy vs Spy, drafted by tools/mkspec.py from sitescan output.
name Spy vs Spy
cart 78D7FAAB
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0009   ; OUT ($BF),A
site 000C   ; OUT ($BF),A
site 0093   ; OUT ($DF),A
site 0096   ; OUT ($DE),A
site 0098   ; IN A,($DE)
site 00AB   ; OTIR
site 00E6   ; IN A,($BF)
site 00E8   ; IN A,($DD)
site 017F   ; IN A,($DC)
site 018F   ; OUT ($DE),A
site 0191   ; IN A,($DC)
site 0196   ; OUT ($DE),A
site 0198   ; IN A,($DC)
site 01A2   ; OUT ($DE),A
site 01A4   ; IN A,($DC)
site 01AE   ; OUT ($DE),A
site 01B0   ; IN A,($DC)
site 01C0   ; OUT ($DE),A
site 01C2   ; IN A,($DC)
site 01CC   ; OUT ($DE),A
site 01CE   ; IN A,($DC)
site 01DC   ; OUT ($DE),A
site 01E4   ; OUT ($DE),A
site 01E6   ; IN A,($DC)
site 01F6   ; OUT ($DE),A
site 01F8   ; IN A,($DC)
site 0202   ; OUT ($DE),A
site 0204   ; IN A,($DC)
site 020E   ; OUT ($DE),A
site 0210   ; IN A,($DD)
site 021A   ; OUT ($DE),A
site 021C   ; IN A,($DD)
site 025C   ; IN A,($DC)
site 0261   ; IN A,($DD)
site 026C   ; OUT ($BE),A
otir 028E   ; OUTI
site 029B   ; OUTI
site 02A1   ; OUT (C),A
site 02BA   ; OUT ($BE),A
site 02BF   ; OUT ($BE),A
site 02CC   ; OUTI
site 02D2   ; OUT (C),A
otir 02E5   ; OUTI
site 0308   ; OUT (C),D
site 0342   ; OUT ($BE),A
site 045C   ; OUT ($BE),A
site 06AC   ; INI
site 1454   ; OUT (C),L
site 1458   ; IN A,(C)
site 1E89   ; OUT ($BE),A
site 1EEC   ; OUT ($BE),A
site 1EF1   ; OUT ($BE),A
site 2241   ; OUT ($BE),A
site 2247   ; OUT ($BE),A
site 2411   ; OUT ($BE),A
site 7A18   ; OUT ($7F),A
site 7A39   ; OUT ($7F),A
site 7C99   ; OUT ($7F),A
site 7D3E   ; OUT ($7F),A
site 7D5E   ; OTIR
