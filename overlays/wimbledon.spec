# Wimbledon (Europe), CRC32 912D92AF, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - No free RST vector, so $0000-$0002 (DI; IM 1) is the io vector and the game starts
#   at $0003.
# - The main loop at $016F runs the game state from a table of 3-byte entries (bank,
#   address) at $1798-$184E through CALL $0017 (JP (HL)) at $0184. The sites in those
#   handlers were taken from a scan with the table's addresses as entry points.
# - Bank 0 has a block of JP vectors at $0082-$0145 for the other banks. The routines
#   behind them are listed like the others, except $00F7 (JP $131F), which points
#   into data. So are the bank-0 VDP routines at $0897, $094C, $0971 and $0A16, which
#   have the same form as their neighbours but no caller that the scan found.
name Wimbledon
cart 912D92AF
hz 50		; No-Intro region Europe
vector 00 io
start 0003
site 0001A   ; OUT (C),L
site 0001C   ; OUT (C),H
site 0003A   ; IN A,($BF)
site 0014D   ; IN A,(C)
site 00154   ; OUT ($BF),A
site 00158   ; OUT ($BF),A
site 001CC   ; OUT ($3F),A
site 001CE   ; IN A,($DD)
site 001D8   ; OUT ($3F),A
site 001DA   ; IN A,($DD)
site 00222   ; OUT ($3E),A
site 00225   ; OUT ($F2),A
site 0022D   ; OUT ($3E),A
site 00231   ; OUT ($3F),A
site 00239   ; IN A,($BF)
site 0023B   ; IN A,($BF)
site 00247   ; IN A,($BF)
site 0025D   ; IN A,($DD)
site 0057C   ; OUT ($BF),A
site 00580   ; OUT ($BF),A
site 00583   ; IN A,($BF)
site 00594   ; OUT ($BF),A
site 00598   ; OUT ($BF),A
site 0059B   ; IN A,($DC)
site 005B8   ; IN A,($DD)
site 005DD   ; IN A,($BF)
site 005E8   ; OUT ($BF),A
site 005EB   ; OUT ($BF),A
site 005F8   ; OUT ($BE),A
site 00737   ; OUTI
site 00739   ; OUTI
site 0073B   ; OUTI
site 0073D   ; OUTI
site 0073F   ; OUTI
site 00741   ; OUTI
site 00743   ; OUTI
site 00745   ; OUTI
site 00747   ; OUTI
site 00749   ; OUTI
site 0074B   ; OUTI
site 0074D   ; OUTI
site 0074F   ; OUTI
site 00751   ; OUTI
site 00753   ; OUTI
site 00755   ; OUTI
site 00757   ; OUTI
site 00759   ; OUTI
site 0075B   ; OUTI
site 0075D   ; OUTI
site 0075F   ; OUTI
site 00761   ; OUTI
site 00763   ; OUTI
site 00765   ; OUTI
site 00767   ; OUTI
site 00769   ; OUTI
site 0076B   ; OUTI
site 0076D   ; OUTI
site 0076F   ; OUTI
site 00771   ; OUTI
site 00773   ; OUTI
site 00775   ; OUTI
site 00777   ; OUTI
site 00779   ; OUTI
site 0077B   ; OUTI
site 0077D   ; OUTI
site 0077F   ; OUTI
site 00781   ; OUTI
site 00783   ; OUTI
site 00785   ; OUTI
site 00787   ; OUTI
site 00789   ; OUTI
site 0078B   ; OUTI
site 0078D   ; OUTI
site 0078F   ; OUTI
site 00791   ; OUTI
site 00793   ; OUTI
site 00795   ; OUTI
site 00797   ; OUTI
site 00799   ; OUTI
site 0079B   ; OUTI
site 0079D   ; OUTI
site 0079F   ; OUTI
site 007A1   ; OUTI
site 007A3   ; OUTI
site 007A5   ; OUTI
site 007A7   ; OUTI
site 007A9   ; OUTI
site 007AB   ; OUTI
site 007AD   ; OUTI
site 007AF   ; OUTI
site 007B1   ; OUTI
site 007B3   ; OUTI
site 007B5   ; OUTI
site 007B7   ; OUTI
site 007B9   ; OUTI
site 007BB   ; OUTI
site 007BD   ; OUTI
site 007BF   ; OUTI
site 007C1   ; OUTI
site 007C3   ; OUTI
site 007C5   ; OUTI
site 007C7   ; OUTI
site 007C9   ; OUTI
site 007CB   ; OUTI
site 007CD   ; OUTI
site 007CF   ; OUTI
site 007D1   ; OUTI
site 007D3   ; OUTI
site 007D5   ; OUTI
site 007D7   ; OUTI
site 007D9   ; OUTI
site 007DB   ; OUTI
site 007DD   ; OUTI
site 007DF   ; OUTI
site 007E1   ; OUTI
site 007E3   ; OUTI
site 007E5   ; OUTI
site 007E7   ; OUTI
site 007E9   ; OUTI
site 007EB   ; OUTI
site 007ED   ; OUTI
site 007EF   ; OUTI
site 007F1   ; OUTI
site 007F3   ; OUTI
site 007F5   ; OUTI
site 007F7   ; OUTI
site 007F9   ; OUTI
site 007FB   ; OUTI
site 007FD   ; OUTI
site 007FF   ; OUTI
site 00801   ; OUTI
site 00803   ; OUTI
site 00805   ; OUTI
site 00807   ; OUTI
site 00809   ; OUTI
site 0080B   ; OUTI
site 0080D   ; OUTI
site 0080F   ; OUTI
site 00811   ; OUTI
site 00813   ; OUTI
site 00815   ; OUTI
site 00817   ; OUTI
site 00819   ; OUTI
site 0081B   ; OUTI
site 0081D   ; OUTI
site 0081F   ; OUTI
site 00821   ; OUTI
site 00823   ; OUTI
site 00825   ; OUTI
site 00827   ; OUTI
site 00829   ; OUTI
site 0082B   ; OUTI
site 0082D   ; OUTI
site 0082F   ; OUTI
site 00831   ; OUTI
site 00833   ; OUTI
site 00835   ; OUTI
site 0083E   ; OTIR
site 00850   ; OUT ($BE),A
site 00856   ; OUT ($BE),A
site 0086A   ; OUT ($BE),A
site 0086D   ; OUT ($BE),A
site 00882   ; OUTI
site 00887   ; OUT ($BE),A
site 0089D   ; OUT (C),A
site 008A5   ; OUT (C),A
site 008C5   ; OUT (C),E
site 008C7   ; OUT (C),D
site 008D8   ; OUT (C),E
site 008DE   ; OUT (C),D
site 00939   ; OUT (C),B
site 0095C   ; OUT (C),A
site 0099B   ; OUT ($BE),A
site 00D70   ; OUT (C),A
site 00D77   ; OUT (C),A
site 00DA8   ; OUTI
site 00E2A   ; OUTI
site 00FF8   ; OUT (C),A
site 00FFD   ; OUT (C),A
site 016AD   ; OUT (C),A
site 016B1   ; OUT (C),A
site 01FDB   ; OUT ($BF),A
site 01FDF   ; OUT ($BF),A
site 01FE4   ; OUT ($BF),A
site 01FE8   ; OUT ($BF),A
site 01FF3   ; OTIR
site 02000   ; OTIR
site 02190   ; OUT (C),E
site 02192   ; OUT (C),D
site 021A9   ; OUT (C),E
site 021AB   ; OUT (C),D
site 021AE   ; OUTI
site 021B0   ; OUTI
site 021BA   ; OUT (C),E
site 021BC   ; OUT (C),D
site 021BF   ; OUTI
site 021C1   ; OUTI
site 021CB   ; OUT (C),E
site 021CD   ; OUT (C),D
site 021D0   ; OUTI
site 021D2   ; OUTI
site 021DC   ; OUT (C),E
site 021DE   ; OUT (C),D
site 021E1   ; OUTI
site 021E3   ; OUTI
site 021ED   ; OUT (C),E
site 021EF   ; OUT (C),D
site 021F2   ; OUTI
site 021F4   ; OUTI
site 021FE   ; OUT (C),E
site 02200   ; OUT (C),D
site 02203   ; OUTI
site 02205   ; OUTI
site 0220F   ; OUT (C),E
site 02211   ; OUT (C),D
site 02214   ; OUTI
site 02216   ; OUTI
site 02220   ; OUT (C),E
site 02222   ; OUT (C),D
site 02225   ; OUTI
site 02227   ; OUTI
site 02231   ; OUT (C),E
site 02233   ; OUT (C),D
site 02236   ; OUTI
site 02238   ; OUTI
site 02242   ; OUT (C),E
site 02244   ; OUT (C),D
site 02247   ; OUTI
site 02249   ; OUTI
site 02253   ; OUT (C),E
site 02255   ; OUT (C),D
site 02258   ; OUTI
site 0225A   ; OUTI
site 02264   ; OUT (C),E
site 02266   ; OUT (C),D
site 02269   ; OUTI
site 0226B   ; OUTI
site 02275   ; OUT (C),E
site 02277   ; OUT (C),D
site 0227A   ; OUTI
site 0227C   ; OUTI
site 02286   ; OUT (C),E
site 02288   ; OUT (C),D
site 0228B   ; OUTI
site 0228D   ; OUTI
site 02297   ; OUT (C),E
site 02299   ; OUT (C),D
site 0229C   ; OUTI
site 0229E   ; OUTI
site 022A8   ; OUT (C),E
site 022AA   ; OUT (C),D
site 022AD   ; OUTI
site 022AF   ; OUTI
site 022B9   ; OUT (C),E
site 022BB   ; OUT (C),D
site 022BE   ; OUTI
site 022C0   ; OUTI
site 022CA   ; OUT (C),E
site 022CC   ; OUT (C),D
site 022CF   ; OUTI
site 022D1   ; OUTI
site 022DB   ; OUT (C),E
site 022DD   ; OUT (C),D
site 022E0   ; OUTI
site 022E2   ; OUTI
site 022EC   ; OUT (C),E
site 022EE   ; OUT (C),D
site 022F1   ; OUTI
site 022F3   ; OUTI
site 022FD   ; OUT (C),E
site 022FF   ; OUT (C),D
site 02302   ; OUTI
site 02304   ; OUTI
site 0230E   ; OUT (C),E
site 02310   ; OUT (C),D
site 02313   ; OUTI
site 02315   ; OUTI
site 0231F   ; OUT (C),E
site 02321   ; OUT (C),D
site 02324   ; OUTI
site 02326   ; OUTI
site 02330   ; OUT (C),E
site 02332   ; OUT (C),D
site 02335   ; OUTI
site 02337   ; OUTI
site 02341   ; OUT (C),E
site 02343   ; OUT (C),D
site 02346   ; OUTI
site 02348   ; OUTI
site 02352   ; OUT (C),E
site 02354   ; OUT (C),D
site 02357   ; OUTI
site 02359   ; OUTI
site 02363   ; OUT (C),E
site 02365   ; OUT (C),D
site 02368   ; OUTI
site 0236A   ; OUTI
site 02374   ; OUT (C),E
site 02376   ; OUT (C),D
site 02379   ; OUTI
site 0237B   ; OUTI
site 02388   ; OUT ($BF),A
site 0238C   ; OUT ($BF),A
site 02391   ; OUT ($BF),A
site 02395   ; OUT ($BF),A
site 02545   ; OUT (C),D
site 025C0   ; OUT (C),E
site 025C2   ; OUT (C),D
site 025D5   ; OUT (C),A
site 029EC   ; OUT (C),E
site 029EE   ; OUT (C),D
site 03542   ; OUT (C),A
site 03546   ; OUT (C),A
site 0354A   ; OUT (C),A
site 0354E   ; OUT (C),A
site 0C1C8   ; OUT (C),A
site 0C1CE   ; IN D,(C)
site 0C1D3   ; OUT (C),A
site 13047   ; OUT (C),A
site 1304D   ; OUT (C),D
site 14008   ; OUT (C),A
site 1400C   ; OUT (C),A
site 1400F   ; OUT (C),A
site 14013   ; OUT (C),A
site 1C1AF   ; OUT (C),A
site 340D8   ; OUT (C),A
site 340DD   ; OUT (C),A
site 3819B   ; OUT (C),A
site 3819F   ; OUT (C),A
site 381A2   ; OUT (C),A
site 381A6   ; OUT (C),A
site 381AA   ; OUT (C),A
site 381AE   ; OUT (C),A
site 381DE   ; OUT (C),A
site 381E2   ; OUT (C),A
site 38251   ; OUT (C),A
site 38255   ; OUT (C),A
site 38277   ; OUT (C),A
site 38279   ; OUT (C),B
site 38281   ; OUT (C),A
site 38283   ; OUT (C),B
site 382E9   ; OUT (C),A
site 382EB   ; OUT (C),B
site 382F3   ; OUT (C),A
site 382F5   ; OUT (C),B
site 3C1E2   ; OUT ($7F),A
site 3C308   ; OUT ($7F),A
site 3C49A   ; OTIR
site 3C5B2   ; OUT ($7F),A
site 3C5BC   ; OUT ($7F),A
site 3C5D9   ; OUT ($7F),A
site 3C6DD   ; OUT ($7F),A
site 3C7BA   ; OUT ($7F),A
site 3C85C   ; OUT ($7F),A
site 3C865   ; OUT ($7F),A
site 3C875   ; OUT ($7F),A
site 3C8F1   ; OUT ($7F),A
mapldk 0015A   # LD HL,$FFFC; LD (HL),$00
maphl 00160   # LD (HL),$00, HL = $FFFD
maphl 00163   # LD (HL),$01, HL = $FFFE
maphl 00166   # LD (HL),$02, HL = $FFFF
mapst 00181   ; LD ($FFFF),A
mapst 00275   ; LD ($FFFF),A
mapst 0033B   ; LD ($FFFF),A
mapst 00908   ; LD ($FFFF),A
mapst 00945   ; LD ($FFFF),A
mapst 0096A   ; LD ($FFFF),A
mapst 009A9   ; LD ($FFFF),A
mapst 009BC   ; LD ($FFFF),A
mapst 00A28   ; LD ($FFFF),A
mapst 00BC3   ; LD ($FFFF),A
mapst 00BCA   ; LD ($FFFF),A
mapst 00D81   ; LD ($FFFF),A
mapst 00DB5   ; LD ($FFFF),A
mapst 00DE4   ; LD ($FFFF),A
mapst 00E3F   ; LD ($FFFF),A
mapst 00F36   ; LD ($FFFF),A
mapst 00F3E   ; LD ($FFFF),A
mapst 00F58   ; LD ($FFFF),A
mapst 00F60   ; LD ($FFFF),A
mapst 00FC2   ; LD ($FFFF),A
mapst 00FCB   ; LD ($FFFF),A
mapst 01016   ; LD ($FFFF),A
mapst 0101D   ; LD ($FFFF),A
mapst 01032   ; LD ($FFFF),A
mapst 0103F   ; LD ($FFFF),A
mapst 01049   ; LD ($FFFF),A
mapst 01076   ; LD ($FFFF),A
mapst 013DD   ; LD ($FFFF),A
mapst 0140D   ; LD ($FFFF),A
mapst 0146B   ; LD ($FFFF),A
mapst 01487   ; LD ($FFFF),A
mapst 0168E   ; LD ($FFFF),A
mapst 01695   ; LD ($FFFF),A
mapst 01F41   ; LD ($FFFF),A
mapst 01F5A   ; LD ($FFFF),A
mapst 025CF   ; LD ($FFFF),A
mapst 025DE   ; LD ($FFFF),A
mapst 029F3   ; LD ($FFFF),A
mapst 02A40   ; LD ($FFFF),A
mapst 00A84   # LD ($FFFF),A; after LD A,(HL); 32 bytes of valid code before it

# Wimbledon (Europe) (Action Replay).cht, "P2/CPU Never Scores": RAM $CB02 is the CPU player's
# point count in the current game; held at 0, the CPU never gets a point
poke "CPU never scores"
ar 00CB-0200
endpoke

# Wimbledon (Europe) (Action Replay).cht, "P1 Score Modifier": RAM $CB03 is player 1's point
# count in the current game (0 = 0, 1 = 15, 2 = 30, 3 = 40), held at the value chosen
poke "P1 score ??"
ar 00CB-03??
endpoke

# Wimbledon (Europe).cht, "P2 Games Won Modifier": RAM $CB04 is the CPU player's game count in the
# set, held at the value chosen; 00 means the CPU never wins a game
poke "CPU games ??"
ar 00CB-04??
endpoke

# Wimbledon (Europe).cht, "P1 Games Won Modifier": RAM $CB07 is player 1's game count in the set,
# held at the value chosen
poke "P1 games ??"
ar 00CB-07??
endpoke

# Wimbledon (Europe).cht, "Most Games are given to you": the game the CPU player wins is
# counted for player 1
poke "CPU games go to you"
gg 07C-98E-F7A
endpoke

# Wimbledon (Europe).cht, "Infinite Attribute Points": RAM $CB22 is the points left to spend
# in Tour Mode, held at 60
poke "Infinite points"
ar 00CB-223C
endpoke

# Wimbledon (Europe).cht, "Start with ?? Attribute Points, instead of 15": a Tour Mode player
# starts with 20 points to spend
poke "Start with 20 points"
gg 141-804-D56
endpoke

# Wimbledon (Europe).cht, "Max Speed": RAM $C430 is the Tour Mode player's speed, held at 20
poke "Max speed"
ar 00C4-3014
endpoke

# Wimbledon (Europe).cht, "Max Power": RAM $C431 is the Tour Mode player's power, held at 20
poke "Max power"
ar 00C4-3114
endpoke

# Wimbledon (Europe).cht, "Max Skill": RAM $C432 is the Tour Mode player's skill, held at 20
poke "Max skill"
ar 00C4-3214
endpoke
