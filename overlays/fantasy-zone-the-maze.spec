# Fantasy Zone - The Maze (USA, Europe, Brazil) (En), CRC32 D29889AD, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of random
# input, 120 s with no input).
# Decisions:
# - $0018 is free (erased fill), so it is the io vector.
# - Scan entries, not reached by any path or recording: the VDP fill routines $0218, $0236
#   and $05A1 in bank 0 (each starts after a RET and is a whole routine, so its I/O sites
#   are patched); the targets of the routine tables at $2DE2 and $2E22 ($2FEF, $33B7,
#   $32B1, $31CC, $2FD8, $33C6, $329E, $31D3), whose entries $2E43 and $2E53 store in
#   $CD80 and $CD82 for the jumps at $2F17 and $2F10; and the targets of the 27 7-byte
#   records at $4610 ($4EED, $4FDC, $51A0) for the jump at $460F. These targets hold no
#   I/O or mapper stores.
# - The dark maze in rounds 4 and 8 is the game's bonus stage, the same on a Master System.
name Fantasy Zone - The Maze
cart D29889AD
hz any		; No-Intro regions USA, Europe, Brazil
vector 18 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 0003E   ; OUT ($BF),A
site 00043   ; OUT ($BF),A
site 000B6   ; IN A,($BF)
site 000F8   ; IN A,($DD)
site 0019B   ; OUT ($DE),A
site 0019D   ; IN A,($DC)
site 001A8   ; IN A,($DD)
site 001DE   ; OUT ($BF),A
site 001E5   ; OUT ($BF),A
site 001EA   ; OUT ($BF),A
site 001EF   ; OUT ($BF),A
site 001F7   ; IN A,($BE)
site 00201   ; OUT ($BE),A
site 00206   ; OUT ($BE),A
site 0020A   ; OUT ($BE),A
site 0020E   ; OUT ($BE),A
site 0021F   ; OUT ($BE),A
site 00224   ; OUT ($BE),A
site 00228   ; OUT ($BE),A
site 0022C   ; OUT ($BE),A
site 0023E   ; OUT ($BE),A
site 00243   ; OUT ($BE),A
site 00247   ; OUT ($BE),A
site 0024D   ; OUT ($BE),A
site 0025F   ; OUT ($BE),A
site 00272   ; OUT ($BE),A
site 00284   ; OUT ($BF),A
site 00288   ; OUT ($BF),A
site 0029B   ; OUT ($BF),A
site 0029F   ; OUT ($BF),A
site 002AC   ; OUT ($BF),A
site 002B0   ; OUT ($BF),A
site 002BD   ; OUT ($BF),A
site 002C1   ; OUT ($BF),A
site 00309   ; OUT ($BF),A
site 0030D   ; OUT ($BF),A
site 00312   ; OUT ($BE),A
site 0038A   ; OTIR
site 0038D   ; OUTI
site 0038F   ; OUTI
site 00391   ; OUTI
site 00393   ; OUTI
site 00395   ; OUTI
site 00397   ; OUTI
site 00399   ; OUTI
site 0039B   ; OUTI
site 0039D   ; OUTI
site 0039F   ; OUTI
site 003A1   ; OUTI
site 003A3   ; OUTI
site 003A5   ; OUTI
site 003A7   ; OUTI
site 003A9   ; OUTI
site 003AB   ; OUTI
site 003AD   ; OUTI
site 003AF   ; OUTI
site 003B1   ; OUTI
site 003B3   ; OUTI
site 003B5   ; OUTI
site 003B7   ; OUTI
site 003B9   ; OUTI
site 003BB   ; OUTI
site 003BD   ; OUTI
site 003BF   ; OUTI
site 003C1   ; OUTI
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
site 004E6   ; OUT ($BF),A
site 004ED   ; OUT ($BF),A
site 004F0   ; OUT ($BE),A
site 0054B   ; OUTI
site 0055D   ; OUT ($BE),A
site 00567   ; OUT ($BE),A
site 0056C   ; OUT ($BE),A
site 0057C   ; OUT ($BE),A
site 00582   ; OUT ($BE),A
site 00592   ; OUT ($BE),A
site 00598   ; OUT ($BE),A
site 005A8   ; OUT ($BE),A
site 005AE   ; OUT ($BE),A
site 005B9   ; OUT ($3F),A
site 005BB   ; IN A,($DD)
site 005C5   ; OUT ($3F),A
site 005C7   ; IN A,($DD)
site 005D0   ; OUT ($3F),A
site 00883   ; OUT ($BF),A
site 0088A   ; OUT ($BF),A
site 008A7   ; OUT ($BE),A
site 008B2   ; OUT ($BE),A
site 008BD   ; OUT ($BE),A
site 008C7   ; OUT ($BE),A
site 00909   ; OUT ($3E),A
site 00911   ; OUT ($F2),A
site 00914   ; IN A,($F2)
site 00926   ; OUT ($F2),A
site 0092E   ; OUT ($3E),A
site 00942   ; OUT ($BF),A
site 00946   ; OUT ($BF),A
site 00958   ; OUT ($BF),A
site 0095C   ; OUT ($BF),A
site 02DAE   ; OUT ($BF),A
site 02DB3   ; OUT ($BF),A
site 02DB7   ; IN A,($BE)
site 07579   ; OUT ($BF),A
site 0757E   ; OUT ($BF),A
site 0764B   ; OUT ($BE),A
site 0764F   ; OUT ($BE),A
site 07654   ; OUT ($BE),A
site 07658   ; OUT ($BE),A
site 1C0F5   ; OUT ($F0),A
site 1C0FE   ; OUT ($F1),A
site 1C142   ; OUT ($7F),A
site 1C152   ; OUT (C),D
site 1C158   ; OUT ($F1),A
site 1C375   ; OUT ($F0),A
site 1C37B   ; OUT ($F1),A
site 1C387   ; OUTI
site 1C38D   ; OUTI
site 1C3AE   ; OUT ($7F),A
site 1C3B2   ; OUT ($7F),A
site 1C404   ; OUT ($F0),A
site 1C40B   ; OUT ($F1),A
site 1C413   ; OUT ($F0),A
site 1C419   ; OUT ($F1),A
site 1C513   ; OUT ($F0),A
site 1C51A   ; OUT (C),L
site 1C523   ; OUT ($F0),A
site 1C53E   ; OUT (C),H
site 1C546   ; OUT ($F0),A
site 1C554   ; OUT ($F1),A
site 1C55C   ; OUT ($F0),A
site 1C566   ; OUT ($F1),A
site 1C6F7   ; OUT ($F0),A
site 1C6FD   ; OUTI
site 1C762   ; OUT ($7F),A
site 1C859   ; OUT ($7F),A
site 1C85D   ; OUT ($7F),A
site 1C87A   ; OUT ($7F),A
site 1C89C   ; OUT ($7F),A
site 1C8AB   ; OUT ($F0),A
site 1C8BB   ; OUT ($F1),A
site 1C8D9   ; OUT ($F0),A
site 1C8E4   ; OUT ($F1),A
site 1C949   ; OTIR
site 1C957   ; OUT (C),D
site 1C95D   ; OUT ($F1),A
site 1C998   ; OUT ($7F),A
site 1C9E9   ; OUT ($7F),A
site 1CA73   ; OUT ($7F),A
site 1CA91   ; OUT ($7F),A
site 1CAD1   ; OUT ($7F),A
site 1CADB   ; OUT ($7F),A
site 1CB23   ; OUT ($7F),A
mapst 0081A   ; LD ($FFFF),A

# Fantasy Zone - The Maze (USA, Europe, Brazil).cht, "Infinite Lives - Player 1" and
# "Infinite Lives - Player 2": RAM $C067 and $C068 are the lives of players 1 and 2, held at 5
poke "Infinite lives"
ar 00C0-6705
ar 00C0-6805
endpoke

# Fantasy Zone - The Maze (USA, Europe, Brazil).cht, "Final Round [51]": RAM $C04C is the
# round index, the round shown is that value plus 1 ($32 is round 51)
poke "Start round ??"
ar 00C0-4C??
endpoke
