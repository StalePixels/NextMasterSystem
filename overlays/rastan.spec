# Rastan (USA, Europe, Brazil) (En), CRC32 C547EB1B, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - $0018-$001A are $FF filler that no code uses: $0018 is the io vector.
# - LD HL,$00FE; LD DE,$FFFC; LD BC,4; LDIR at $0085 and $00A5 copies 0,0,1,2 to the
#   mapper registers. No other code writes $FFFC or $FFFD, so they stay 0; the asm
#   blocks write $FFFE and $FFFF as one pair. HL, DE and BC are loaded again before
#   they are read.
# - FM unit: the game looks for it at $00C6-$00EC (ports $3E and $F2) and plays its PSG
#   driver ($70FC, bank 14 in slot 1) when it is not found.
# - The interrupt handler at $0102 also runs the game's main task (JP (HL) at $019F to the
#   address at $C14D, on the stack at $C14B); the task ends its frame through CALL $0251.
# - The bytes the scanner decodes at $3420-$35BA (four LD (BC),A into $0007-$0893) are
#   tile map data.
# - Unused code: the string routine $2ECC/$2ED2 in bank 0 and the PSG mute routine $7530
#   in bank 14. Data: the I/O byte patterns in banks 11, 13 and 15.
name Rastan
cart C547EB1B
hz any		; No-Intro regions USA, Europe, Brazil
vector 18 io
asm 00085 11  ; LD HL,$00FE; LD DE,$FFFC; LD BC,4; LDIR
    ld hl,$0201
    rst $18
    db $17, 0     ; LD ($FFFE),HL: bank 1 to $FFFE, bank 2 to $FFFF
    nop
    nop
    nop
    nop
    nop
endasm
asm 000A5 11  ; LD HL,$00FE; LD DE,$FFFC; LD BC,4; LDIR
    ld hl,$0201
    rst $18
    db $17, 0     ; LD ($FFFE),HL
    nop
    nop
    nop
    nop
    nop
endasm
asm 000F8 2   ; IM 1 -> IM 2
    im 2
endasm
site 000C8   ; OUT ($3E),A
site 000D0   ; OUT ($F2),A
site 000D3   ; IN A,($F2)
site 000E5   ; OUT ($F2),A
site 000EC   ; OUT ($3E),A
site 00103   ; IN A,($BF)
site 0014F   ; OUT ($BE),A
site 00159   ; OUT ($BE),A
site 0017E   ; IN A,($DD)
site 0018D   ; IN A,($DD)
site 002D6   ; OUT ($BE),A
site 002E9   ; OUT ($BE),A
site 00306   ; OUT ($BE),A
site 00318   ; OUT ($BE),A
site 00320   ; OUT ($BF),A
site 00325   ; OUT ($BF),A
site 0033A   ; OUT ($DE),A
site 0033C   ; IN A,($DC)
site 00343   ; IN A,($DD)
site 00352   ; OUT ($DE),A
site 00354   ; IN A,($DC)
site 00362   ; IN A,($DD)
site 00387   ; OUT ($BE),A
site 00395   ; OUT ($BE),A
site 003A4   ; OUT ($BE),A
site 003B3   ; OUT ($BE),A
site 00458   ; OUT ($3F),A
site 0045A   ; IN A,($DD)
site 00464   ; OUT ($3F),A
site 00466   ; IN A,($DD)
site 0046E   ; OUT ($3F),A
site 005CA   ; OUT ($BF),A
site 005D1   ; OUT ($BF),A
site 005ED   ; OUT ($BE),A
site 005F3   ; OUT ($BE),A
site 00602   ; OUT ($BF),A
site 00609   ; OUT ($BF),A
site 00619   ; OUT ($BE),A
site 00622   ; OUT ($BE),A
site 00630   ; OUT ($BF),A
site 00637   ; OUT ($BF),A
site 0063B   ; OUT ($BE),A
site 00641   ; OUT ($BE),A
site 0064F   ; OUT ($BF),A
site 00656   ; OUT ($BF),A
site 0066C   ; OUT ($BE),A
site 00672   ; OUT ($BE),A
site 00677   ; OUT ($BF),A
site 0067E   ; OUT ($BF),A
site 0069E   ; OUT ($BF),A
site 006A5   ; OUT ($BF),A
site 006B3   ; OUT ($BE),A
site 00ED1   ; OUT ($BF),A
site 00ED8   ; OUT ($BF),A
site 00EF4   ; OUT ($BE),A
site 00EFA   ; OUT ($BE),A
site 00F09   ; OUT ($BF),A
site 00F10   ; OUT ($BF),A
site 00F20   ; OUT ($BE),A
site 00F29   ; OUT ($BE),A
site 00F37   ; OUT ($BF),A
site 00F3E   ; OUT ($BF),A
site 00F42   ; OUT ($BE),A
site 00F48   ; OUT ($BE),A
site 00F56   ; OUT ($BF),A
site 00F5D   ; OUT ($BF),A
site 00F73   ; OUT ($BE),A
site 00F79   ; OUT ($BE),A
site 01084   ; OUT ($BF),A
site 0108B   ; OUT ($BF),A
site 010A2   ; OUT ($BE),A
site 010A9   ; OUT ($BE),A
site 010AF   ; OUT ($BF),A
site 010B6   ; OUT ($BF),A
site 010C2   ; OUT ($BE),A
site 010C9   ; OUT ($BE),A
site 01185   ; OUT ($BF),A
site 0118C   ; OUT ($BF),A
site 011A3   ; OUT ($BE),A
site 011AA   ; OUT ($BE),A
site 011B0   ; OUT ($BF),A
site 011B7   ; OUT ($BF),A
site 011C3   ; OUT ($BE),A
site 011CA   ; OUT ($BE),A
site 02DB0   ; OUT ($BE),A
site 02DB7   ; OUT ($BE),A
site 02DD3   ; OUT ($BE),A
site 02DD9   ; OUT ($BE),A
site 02DF8   ; OUT ($BE),A
site 02DFC   ; OUT ($BE),A
site 02E00   ; OUT ($BE),A
site 02E04   ; OUT ($BE),A
site 02E36   ; OUT ($BE),A
site 02E3A   ; OUT ($BE),A
site 02E3E   ; OUT ($BE),A
site 02E42   ; OUT ($BE),A
site 02E72   ; OUT ($BE),A
site 02E76   ; OUT ($BE),A
site 02E7A   ; OUT ($BE),A
site 02E7E   ; OUT ($BE),A
site 02EAE   ; OUT ($BE),A
site 02EB2   ; OUT ($BE),A
site 02EB6   ; OUT ($BE),A
site 02EBA   ; OUT ($BE),A
site 02F1F   ; OUT ($BE),A
site 02F26   ; OUT ($BE),A
site 02F4C   ; OUT ($BE),A
site 02F53   ; OUT ($BE),A
site 17D85   ; OUT ($BE),A
site 17D8D   ; OUT ($BE),A
site 17D95   ; OUT ($BE),A
site 17D9D   ; OUT ($BE),A
site 17DC6   ; OUT ($BE),A
site 17DCE   ; OUT ($BE),A
site 17DD6   ; OUT ($BE),A
site 17DDE   ; OUT ($BE),A
site 17E0D   ; OUT ($BE),A
site 17E15   ; OUT ($BE),A
site 17E1D   ; OUT ($BE),A
site 17E25   ; OUT ($BE),A
site 17E30   ; OUT ($BE),A
site 17E38   ; OUT ($BE),A
site 17E40   ; OUT ($BE),A
site 17E48   ; OUT ($BE),A
site 17E5A   ; OUT ($BE),A
site 17E62   ; OUT ($BE),A
site 17E6A   ; OUT ($BE),A
site 17E72   ; OUT ($BE),A
site 17E7E   ; OUT ($BE),A
site 17E86   ; OUT ($BE),A
site 17E8E   ; OUT ($BE),A
site 17E96   ; OUT ($BE),A
site 17EA5   ; OUT ($BE),A
site 17EAD   ; OUT ($BE),A
site 17EB5   ; OUT ($BE),A
site 17EBD   ; OUT ($BE),A
site 17F2E   ; OUT ($BF),A
site 17F35   ; OUT ($BF),A
site 2FDE7   ; OUT ($BE),A
site 2FDEF   ; OUT ($BE),A
site 2FDF7   ; OUT ($BE),A
site 2FDFF   ; OUT ($BE),A
site 2FE0B   ; OUT ($BE),A
site 2FE13   ; OUT ($BE),A
site 2FE1B   ; OUT ($BE),A
site 2FE23   ; OUT ($BE),A
site 2FE5C   ; OUT ($BE),A
site 2FE64   ; OUT ($BE),A
site 2FE6C   ; OUT ($BE),A
site 2FE74   ; OUT ($BE),A
site 2FE9C   ; OUT ($BE),A
site 2FEA4   ; OUT ($BE),A
site 2FEAC   ; OUT ($BE),A
site 2FEB4   ; OUT ($BE),A
site 2FEE3   ; OUT ($BE),A
site 2FEEB   ; OUT ($BE),A
site 2FEF3   ; OUT ($BE),A
site 2FEFB   ; OUT ($BE),A
site 2FF0A   ; OUT ($BE),A
site 2FF12   ; OUT ($BE),A
site 2FF1A   ; OUT ($BE),A
site 2FF22   ; OUT ($BE),A
site 2FF34   ; OUT ($BE),A
site 2FF3C   ; OUT ($BE),A
site 2FF44   ; OUT ($BE),A
site 2FF4C   ; OUT ($BE),A
site 2FF58   ; OUT ($BE),A
site 2FF60   ; OUT ($BE),A
site 2FF68   ; OUT ($BE),A
site 2FF70   ; OUT ($BE),A
site 2FF7F   ; OUT ($BE),A
site 2FF87   ; OUT ($BE),A
site 2FF8F   ; OUT ($BE),A
site 2FF97   ; OUT ($BE),A
site 2FFED   ; OUT ($BF),A
site 2FFF4   ; OUT ($BF),A
site 3AF9C   ; OUT ($F0),A
site 3AFA2   ; OUT ($F1),A
site 3B11A   ; OUT ($7F),A
site 3B132   ; OUT ($7F),A
site 3B13B   ; OUT ($7F),A
site 3B15D   ; OUT ($7F),A
site 3B166   ; OUT ($7F),A
site 3B174   ; OUT ($7F),A
site 3B178   ; OUT ($7F),A
mapst 00169   ; LD ($FFFF),A
mapst 001D6   ; LD ($FFFE),A
mapst 001DA   ; LD ($FFFF),A
mapst 001ED   ; LD ($FFFF),A
mapst 001F1   ; LD ($FFFE),A
mapst 00222   ; LD ($FFFE),A
mapst 00226   ; LD ($FFFF),A
mapst 00239   ; LD ($FFFF),A
mapst 0023D   ; LD ($FFFE),A
mapst 003F1   ; LD ($FFFE),A
mapst 003F5   ; LD ($FFFF),A
mapst 0048F   ; LD ($FFFE),A
mapst 00494   ; LD ($FFFF),A
mapst 004A6   ; LD ($FFFE),A
mapst 004AB   ; LD ($FFFF),A
mapst 004CC   ; LD ($FFFF),A
mapst 004D1   ; LD ($FFFF),A
mapst 006CA   ; LD ($FFFF),A
mapst 008B2   ; LD ($FFFE),A
mapst 008B6   ; LD ($FFFF),A
mapst 00952   ; LD ($FFFE),A
mapst 00956   ; LD ($FFFF),A
mapst 00981   ; LD ($FFFF),A
mapst 00AD2   ; LD ($FFFE),A
mapst 00AD8   ; LD ($FFFF),A
mapst 01489   ; LD ($FFFE),A
mapst 0148E   ; LD ($FFFF),A
mapst 01603   ; LD ($FFFE),A
mapst 01608   ; LD ($FFFF),A
mapst 016DD   ; LD ($FFFE),A
mapst 016E2   ; LD ($FFFF),A
mapst 01815   ; LD ($FFFE),A
mapst 0183F   ; LD ($FFFE),A
mapst 0187E   ; LD ($FFFE),A
mapst 01894   ; LD ($FFFE),A
mapst 01899   ; LD ($FFFF),A
mapst 018A4   ; LD ($FFFF),A
mapst 018B0   ; LD ($FFFE),A
mapst 018B5   ; LD ($FFFF),A
mapst 018BD   ; LD ($FFFE),A
mapst 018C2   ; LD ($FFFF),A
mapst 0190A   ; LD ($FFFE),A
mapst 0190F   ; LD ($FFFF),A
mapst 01923   ; LD ($FFFE),A
mapst 01928   ; LD ($FFFF),A
mapst 01930   ; LD ($FFFF),A
mapst 01984   ; LD ($FFFE),A
mapst 01989   ; LD ($FFFF),A
mapst 01A3B   ; LD ($FFFE),A
mapst 01A64   ; LD ($FFFF),A
mapst 01AA2   ; LD ($FFFE),A
mapst 01AA7   ; LD ($FFFF),A
mapst 01AB0   ; LD ($FFFE),A
mapst 01AB5   ; LD ($FFFF),A
mapst 01ABD   ; LD ($FFFE),A
mapst 01AC2   ; LD ($FFFF),A
mapst 01AEF   ; LD ($FFFE),A
mapst 01AF4   ; LD ($FFFF),A
mapst 01AFC   ; LD ($FFFE),A
mapst 01B01   ; LD ($FFFF),A
mapst 01B1B   ; LD ($FFFE),A
mapst 01B20   ; LD ($FFFF),A
mapst 01B32   ; LD ($FFFE),A
mapst 01B37   ; LD ($FFFF),A
mapst 01B49   ; LD ($FFFE),A
mapst 01B4E   ; LD ($FFFF),A
mapst 01B60   ; LD ($FFFE),A
mapst 01B65   ; LD ($FFFF),A
mapst 01B77   ; LD ($FFFE),A
mapst 01B7C   ; LD ($FFFF),A
mapst 01B8E   ; LD ($FFFE),A
mapst 01B93   ; LD ($FFFF),A
mapst 01BA5   ; LD ($FFFE),A
mapst 01C2C   ; LD ($FFFE),A
mapst 01C61   ; LD ($FFFE),A
mapst 01D82   ; LD ($FFFF),A
mapst 01E2A   ; LD ($FFFE),A
mapst 01E2E   ; LD ($FFFF),A
mapst 01E56   ; LD ($FFFF),A
mapst 01E70   ; LD ($FFFF),A
mapst 01E84   ; LD ($FFFF),A
mapst 01E98   ; LD ($FFFF),A
mapst 01EA9   ; LD ($FFFF),A
mapst 01EEB   ; LD ($FFFE),A
mapst 01EEF   ; LD ($FFFF),A
mapst 01FCA   ; LD ($FFFF),A
mapst 02012   ; LD ($FFFF),A
mapst 021D8   ; LD ($FFFE),A
mapst 021DD   ; LD ($FFFF),A
mapst 022BC   ; LD ($FFFF),A
mapst 022C5   ; LD ($FFFF),A
mapst 0237A   ; LD ($FFFF),A
mapst 024ED   ; LD ($FFFF),A
mapst 02DE2   ; LD ($FFFF),A
mapst 02E0F   ; LD ($FFFF),A
mapst 02F7B   ; LD ($FFFF),A
mapst 02F7F   ; LD ($FFFE),A
mapst 02F91   ; LD ($FFFF),A
mapst 02F95   ; LD ($FFFE),A
mapst 03C3D   ; LD ($FFFF),A
mapst 03C5B   ; LD ($FFFF),A
mapst 03C68   ; LD ($FFFE),A
mapst 03C7D   ; LD ($FFFF),A
mapst 03CCE   ; LD ($FFFF),A
mapst 03D2F   ; LD ($FFFF),A
mapst 03DF9   ; LD ($FFFF),A
mapst 04017   ; LD ($FFFF),A
mapst 04022   ; LD ($FFFF),A
mapst 04036   ; LD ($FFFF),A
mapst 06393   ; LD ($FFFF),A
mapst 065B9   ; LD ($FFFF),A
mapst 0661A   ; LD ($FFFF),A
mapst 07555   ; LD ($FFFF),A
mapst 07585   ; LD ($FFFF),A
mapst 07598   ; LD ($FFFF),A
mapst 075BB   ; LD ($FFFF),A
mapst 07613   ; LD ($FFFF),A
mapst 0761E   ; LD ($FFFF),A
mapst 0762E   ; LD ($FFFF),A
mapst 0765A   ; LD ($FFFF),A
mapst 0766B   ; LD ($FFFF),A
mapst 0767B   ; LD ($FFFF),A
mapst 07699   ; LD ($FFFF),A
mapst 076C2   ; LD ($FFFF),A
mapst 0789E   ; LD ($FFFF),A
mapst 078AF   ; LD ($FFFF),A
mapst 078BF   ; LD ($FFFF),A
mapst 07999   ; LD ($FFFF),A
mapst 079AC   ; LD ($FFFF),A
mapst 079CC   ; LD ($FFFF),A
mapst 07A03   ; LD ($FFFF),A
mapst 07A0E   ; LD ($FFFF),A
mapst 07A1B   ; LD ($FFFE),A
mapst 07A5D   ; LD ($FFFF),A
mapst 07AB5   ; LD ($FFFF),A
mapst 07B1D   ; LD ($FFFF),A
mapst 07B7D   ; LD ($FFFF),A
mapst 07BC8   ; LD ($FFFF),A
mapst 07C09   ; LD ($FFFF),A
mapst 07C4A   ; LD ($FFFF),A

# Rastan (USA, Europe, Brazil).cht, "Infinite Continues": RAM $C2C4 is the number of lives
# left, held at 4 (the game takes one from it at each death)
poke "Infinite lives"
ar 00C2-C404
endpoke

# Rastan (USA, Europe) (Action Replay).cht, "Infinite Life": RAM $C020 is the energy, held
# at its starting value $64 (a full bar)
poke "Infinite energy"
ar 00C0-2064
endpoke

# Rastan (USA, Europe, Brazil).cht, "Invincibility" (C9E-7E7-E69): the routine that tests the
# hero against the enemies returns at once, so no enemy hurts or knocks back the hero
poke "Invincibility"
gg C9E-7E7-E69
endpoke

# Rastan (USA, Europe, Brazil).cht, "Start a new game with ?? Health": the energy and its
# maximum, $C020 and $C021, start at the value chosen instead of $64
poke "Start energy ??"
gg ??8-2BE-7FB
gg ??8-2FE-7FB
endpoke

# Rastan (USA, Europe, Brazil).cht, "Start On Final Level": RAM $C14A is the stage number,
# held at the value chosen ($01 is the first stage; $15 is the red dragon's cave)
poke "Stage ??"
ar 00C1-4A??
endpoke

# Rastan (USA, Europe, Brazil).cht, "Have All Items": RAM $C001 holds the hero's weapon
# and armour flags, held with every flag set (the sword turns into the red one)
poke "Have all items"
ar 00C0-01FF
endpoke
