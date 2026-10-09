# Teddy Boy (USA, Europe, Brazil), CRC32 2728FAA3, 32K, no mapper.
# The game uses RST $08, $10, $18, $20 and $30, and its RST $20 routine
# runs through $0028, so no RST vector is free except $00: $0000-$0002
# (the game's interrupt-disable and interrupt mode 1 setup) becomes JP to the io entry and the game starts at $0003
# (the framework has already done DI and IM 2).
# Sites: tools/sitescan.py (static, with the detector's dynamic log),
# all high and medium confidence I/O rows, plus the low-confidence rows
# at $01AB, $01B0, $01B5, $51DF, $51E4, which a linear disassembly shows
# are real code. $003F is an OUTI loop that jumps back to itself, patched as OTIR.
name Teddy Boy
cart 2728FAA3
vector 00 io
start 0003
otir 003F   ; OUTI
site 0009   ; OUT ($BF),A
site 0013   ; OUT ($BE),A
site 0023   ; OUTI
site 0029   ; OUT (C),A
site 0031   ; OUT ($BF),A
site 0034   ; OUT ($BF),A
site 005A   ; OUT (C),D
site 010C   ; IN A,($BF)
site 010E   ; IN A,($C1)
site 019C   ; OUT ($BE),A
site 01A1   ; OUT ($BE),A
site 027C   ; OTIR
site 02B5   ; OUT ($BE),A
site 02C0   ; OUTI
site 02C2   ; OUTI
site 02C5   ; OUT (C),A
site 02C8   ; OUT (C),A
site 02E0   ; OUT ($DF),A
site 02E8   ; OUT ($DE),A
site 02EA   ; IN A,($DE)
site 02F3   ; OUT ($7F),A
site 02F7   ; OUT ($7F),A
site 02FB   ; OUT ($7F),A
site 02FF   ; OUT ($7F),A
site 030E   ; IN A,($C0)
site 0313   ; IN A,($C0)
site 0318   ; IN A,($C1)
site 0328   ; OUT ($DE),A
site 032A   ; IN A,($C0)
site 032F   ; OUT ($DE),A
site 0331   ; IN A,($C0)
site 033C   ; OUT ($DE),A
site 033E   ; IN A,($C0)
site 0349   ; OUT ($DE),A
site 034B   ; IN A,($C0)
site 035D   ; OUT ($DE),A
site 035F   ; IN A,($C0)
site 036A   ; OUT ($DE),A
site 036C   ; IN A,($C0)
site 0383   ; OUT ($DE),A
site 0385   ; IN A,($C0)
site 038A   ; IN A,($C1)
site 0394   ; OUT ($DE),A
site 0396   ; IN A,($C0)
site 03A8   ; OUT ($DE),A
site 03AA   ; IN A,($C0)
site 03B5   ; OUT ($DE),A
site 03B7   ; IN A,($C0)
site 03C2   ; OUT ($DE),A
site 03C4   ; IN A,($C1)
site 03CF   ; OUT ($DE),A
site 03D1   ; IN A,($C1)
site 35E0   ; OUT ($BE),A
site 35E6   ; OUT ($BE),A
site 5148   ; OUT ($7F),A
site 51BB   ; OUT ($7F),A
site 51D5   ; OTIR
site 01AB   ; OUT ($BF),A
site 01B0   ; OUT ($BF),A
site 01B5   ; OUTI
site 51DF   ; OUT ($7F),A
site 51E4   ; OUT ($7F),A
