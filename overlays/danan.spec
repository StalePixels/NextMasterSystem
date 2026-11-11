# Danan - The Jungle Fighter (Europe, Brazil) (En), CRC32 AE4A28D7, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of
# random input, 120 s with no input).
#
# Decisions:
# - The game uses no RST and no HALT. $0018-$0037 are $FF bytes, so $18 is the io vector.
# - The sites at $0804-$0808 (intro V scroll) and $0AF0-$0AF4 come from code reached through
#   the game's state tables at $0630 and $0A66 (dispatcher $0713), which the scanner gets
#   as --entry points. Every site in the reference logs is in the spec.
# - Slot 1 always holds bank 1; slot 2 is switched only at $06B2.
name Danan - The Jungle Fighter
cart AE4A28D7
hz 50		; No-Intro regions Europe, Brazil
vector 18 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 000AC   ; OUT (C),L
site 000AE   ; OUT (C),H
site 000B3   ; OUT (C),L
site 000B5   ; OUT (C),H
site 00130   ; IN A,($BF)
site 00144   ; OUT ($BF),A
site 00148   ; OUT ($BF),A
site 0016C   ; IN A,($DD)
site 00257   ; OUT ($DE),A
site 00259   ; IN A,($DC)
site 00264   ; IN A,($DD)
site 0030C   ; OUT ($BF),A
site 00313   ; OUT ($BF),A
site 0031E   ; OUT ($BE),A
site 00323   ; OUT ($BE),A
site 00327   ; OUT ($BE),A
site 0032B   ; OUT ($BE),A
site 0033D   ; OUT ($BE),A
site 0034F   ; OUT ($BF),A
site 00353   ; OUT ($BF),A
site 00366   ; OUT ($BF),A
site 0036A   ; OUT ($BF),A
site 00377   ; OUT ($BF),A
site 0037B   ; OUT ($BF),A
site 00388   ; OUT ($BF),A
site 0038C   ; OUT ($BF),A
site 003AF   ; OUT ($BF),A
site 003B4   ; OUT ($BF),A
site 003EA   ; OUT ($BF),A
site 003EE   ; OUT ($BF),A
site 003F3   ; OUT ($BE),A
site 00466   ; OTIR
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
site 004C3   ; OUTI
site 004C5   ; OUTI
site 004C7   ; OUTI
site 004C9   ; OUTI
site 004CB   ; OUTI
site 004CD   ; OUTI
site 004CF   ; OUTI
site 004D1   ; OUTI
site 004D3   ; OUTI
site 004D5   ; OUTI
site 004D7   ; OUTI
site 004D9   ; OUTI
site 004DB   ; OUTI
site 004DD   ; OUTI
site 004DF   ; OUTI
site 004E1   ; OUTI
site 004E3   ; OUTI
site 004E5   ; OUTI
site 004E7   ; OUTI
site 004E9   ; OUTI
site 004EB   ; OUTI
site 004ED   ; OUTI
site 004EF   ; OUTI
site 004F1   ; OUTI
site 004F3   ; OUTI
site 004F5   ; OUTI
site 004F7   ; OUTI
site 004F9   ; OUTI
site 004FB   ; OUTI
site 004FD   ; OUTI
site 004FF   ; OUTI
site 00501   ; OUTI
site 00503   ; OUTI
site 00505   ; OUTI
site 00507   ; OUTI
site 00509   ; OUTI
site 0050B   ; OUTI
site 0050D   ; OUTI
site 0050F   ; OUTI
site 00511   ; OUTI
site 00513   ; OUTI
site 00515   ; OUTI
site 00517   ; OUTI
site 00519   ; OUTI
site 0051B   ; OUTI
site 0051D   ; OUTI
site 0051F   ; OUTI
site 00521   ; OUTI
site 00523   ; OUTI
site 00525   ; OUTI
site 00527   ; OUTI
site 00529   ; OUTI
site 0052B   ; OUTI
site 0052D   ; OUTI
site 0052F   ; OUTI
site 00531   ; OUTI
site 00533   ; OUTI
site 00535   ; OUTI
site 00537   ; OUTI
site 00539   ; OUTI
site 0053B   ; OUTI
site 0053D   ; OUTI
site 0053F   ; OUTI
site 00541   ; OUTI
site 00543   ; OUTI
site 00545   ; OUTI
site 00547   ; OUTI
site 00549   ; OUTI
site 0054B   ; OUTI
site 0054D   ; OUTI
site 0054F   ; OUTI
site 00551   ; OUTI
site 00553   ; OUTI
site 00555   ; OUTI
site 00557   ; OUTI
site 00559   ; OUTI
site 0055B   ; OUTI
site 0055D   ; OUTI
site 0055F   ; OUTI
site 00561   ; OUTI
site 00563   ; OUTI
site 00565   ; OUTI
site 00567   ; OUTI
site 0056D   ; OUT ($BF),A
site 00574   ; OUT ($BF),A
site 00577   ; OUT ($BE),A
site 005D2   ; OUTI
site 005E4   ; OUT ($BE),A
site 005E9   ; OUT ($3F),A
site 005EB   ; IN A,($DD)
site 005F5   ; OUT ($3F),A
site 005F7   ; IN A,($DD)
site 00600   ; OUT ($3F),A
site 00804   ; OUT ($BF),A
site 00808   ; OUT ($BF),A
site 00AF0   ; OUT ($BF),A
site 00AF4   ; OUT ($BF),A
site 01F35   ; OUT ($BF),A
site 01F39   ; OUT ($BF),A
site 026DD   ; OUTI
site 026DF   ; OUTI
site 026E1   ; OUTI
site 026E3   ; OUTI
site 026E5   ; OUTI
site 026E7   ; OUTI
site 026E9   ; OUTI
site 026EB   ; OUTI
site 026ED   ; OUTI
site 026EF   ; OUTI
site 026F1   ; OUTI
site 026F3   ; OUTI
site 026F5   ; OUTI
site 026F7   ; OUTI
site 026F9   ; OUTI
site 026FB   ; OUTI
site 026FD   ; OUTI
site 026FF   ; OUTI
site 02701   ; OUTI
site 02703   ; OUTI
site 02705   ; OUTI
site 02707   ; OUTI
site 02709   ; OUTI
site 0270B   ; OUTI
site 0270D   ; OUTI
site 0270F   ; OUTI
site 02711   ; OUTI
site 02713   ; OUTI
site 02715   ; OUTI
site 02717   ; OUTI
site 02719   ; OUTI
site 0271B   ; OUTI
otir 027D8   ; OUTI
site 027FA   ; OUT (C),A
site 027FF   ; OUT (C),A
site 02804   ; OUT (C),A
site 02809   ; OUT (C),A
site 0280E   ; OUT (C),A
site 02813   ; OUT (C),A
site 02818   ; OUT (C),A
site 0281D   ; OUT (C),A
site 02822   ; OUT (C),A
site 02827   ; OUT (C),A
site 0282C   ; OUT (C),A
site 02831   ; OUT (C),A
site 02836   ; OUT (C),A
site 0283B   ; OUT (C),A
site 02840   ; OUT (C),A
site 02845   ; OUT (C),A
site 0284A   ; OUT (C),A
site 0284F   ; OUT (C),A
site 02854   ; OUT (C),A
site 02859   ; OUT (C),A
site 0285E   ; OUT (C),A
site 02863   ; OUT (C),A
site 02868   ; OUT (C),A
site 0286D   ; OUT (C),A
site 02872   ; OUT (C),A
site 02877   ; OUT (C),A
site 0287C   ; OUT (C),A
site 02881   ; OUT (C),A
site 02886   ; OUT (C),A
site 0288B   ; OUT (C),A
site 02890   ; OUT (C),A
site 02895   ; OUT (C),A
site 09FE3   ; OUT ($7F),A
site 0A008   ; OTIR
site 0A013   ; OTIR
site 0A088   ; OUT ($7F),A
site 0A08C   ; OUT ($7F),A
site 0A0C1   ; OUT ($7F),A
site 0A0C5   ; OUT ($7F),A
site 0A0C9   ; OUT ($7F),A
site 0A0CD   ; OUT ($7F),A
site 0A0D0   ; OUT ($7F),A
site 0A2AD   ; OUTI
site 0A2AF   ; OUTI
site 0A2B1   ; OUTI
site 0A2B3   ; OUTI
site 0A2B5   ; OUTI
site 0A2B7   ; OUTI
site 0A2B9   ; OUTI
site 0A2BB   ; OUTI
site 0A2BD   ; OUTI
site 0A2BF   ; OUTI
site 0A2C1   ; OUTI
site 0A3CD   ; OUT ($7F),A
site 0A3D7   ; OUT ($7F),A
site 0A402   ; OUT ($7F),A
site 0A407   ; OUT ($7F),A
site 0A418   ; OUT ($7F),A
site 0A421   ; OUT ($7F),A
site 0A47E   ; OUT ($7F),A
site 0A4D2   ; OUT ($7F),A
site 0A503   ; OUT ($7F),A
site 0A569   ; OUT ($7F),A
site 0A5D0   ; OUT ($7F),A
site 0A5F1   ; OUT ($7F),A
site 0A5F5   ; OUT ($7F),A
site 0A5FA   ; OUT ($7F),A
mapldk 00069   # LD HL,$FFFC; LD (HL),$80
maphl 0006F   # LD (HL),$00, HL = $FFFD
maphl 00072   # LD (HL),$01, HL = $FFFE
mapst 006B2   ; LD ($FFFF),A

# Danan - The Jungle Fighter (Europe) (Action Replay).cht, "Infinite Time": RAM $C7D0 is the
# time left, counted down in hex; the HUD shows 254 and the clock never reaches 0
poke "Infinite time"
ar 00C7-D0FF
endpoke

# Danan - The Jungle Fighter (Europe) (Action Replay).cht, "Infinite/Max Health": RAM $D438 is
# the health, $1E is full (30/30). The code's value $FF is above the maximum and the HUD
# shows 252/30, so the value is $1E
poke "Infinite health"
ar 00D4-381E
endpoke

# Danan - The Jungle Fighter (Europe, Brazil).cht, "Invulnerability": RAM $D422 is the hit
# timer; holding it at $10 stops enemies hurting the player
poke "Invincibility"
ar 00D4-2210
endpoke
