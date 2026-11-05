# Forgotten Worlds (Europe, Brazil) (En), CRC32 38C53916, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, checked against reference I/O logs
# (600 s of random input, 180 s of the attract mode), with these scan entries:
# $0210 (the bank restore that the far call $0203 pushes as its return address),
# 2:$B256 and 2:$B85E (game states 6 and 7 of the tables $4640/$4712), 9:$B3F1 and
# 12:$8000 (object types $1F and $22 of the tables $4A12/$61D3), and 7:$8000 (the sound
# driver, FM and PSG; the reference ran it).
# Decisions:
# - No free RST vector, so $0000-$0002 (DI; IM 1) is the io vector and the game starts
#   at $0003.
# - The byte patterns that no path reached in banks 5, 6, 10, 12, 13 and 14 ($17342,
#   $19ACC, $281B4, $32AB9, $343F5, $345B5, $35D81, $3701D, $39694) are in graphics and
#   table data.
# - tilecache: the screen loads convert fewer tiles at the display-on write; measured with the
#   same input, the game start load goes from 445% to 190% of a frame, and play is the same.
name Forgotten Worlds
cart 38C53916
hz 50		; No-Intro regions Europe, Brazil
tilecache
vector 00 io
start 0003
asm 00029 2   ; IM 1 -> IM 2
    im 2
endasm
site 000A9   ; IN A,($BF)
site 000AD   ; OUT ($BF),A
site 000B1   ; OUT ($BF),A
site 00102   ; OUT ($3E),A
site 0010A   ; OUT ($F2),A
site 0010D   ; IN A,($F2)
site 0011F   ; OUT ($F2),A
site 00127   ; OUT ($3E),A
site 0012B   ; OUT ($3F),A
site 0012E   ; IN A,($BF)
site 00135   ; OUT ($BF),A
site 00139   ; OUT ($BF),A
site 0013E   ; OUT ($BF),A
site 00142   ; OUT ($BF),A
site 00149   ; OUT ($BF),A
site 0014D   ; OUT ($BF),A
site 0015E   ; OUT ($BF),A
site 00162   ; OUT ($BF),A
site 00171   ; OUT ($BF),A
site 00175   ; OUT ($BF),A
site 00194   ; OUT ($BF),A
site 00198   ; OUT ($BF),A
site 0019E   ; IN A,($DD)
site 001AC   ; OUT ($BF),A
site 001B0   ; OUT ($BF),A
site 001C1   ; IN A,($BF)
site 001C3   ; IN A,($BF)
site 001CF   ; IN A,($BF)
site 0025E   ; OUT ($BF),A
site 00262   ; OUT ($BF),A
site 0027F   ; OUT ($BF),A
site 00283   ; OUT ($BF),A
site 0028A   ; IN A,($DC)
site 002A7   ; IN A,($DD)
site 003EA   ; OUT ($BF),A
site 003ED   ; OUT ($BF),A
site 003F0   ; IN A,($BF)
site 003FB   ; OUT ($BF),A
site 003FE   ; OUT ($BF),A
site 00404   ; OUT ($BE),A
site 00411   ; OUT ($BE),A
site 0046F   ; OUTI
site 00471   ; OUTD
site 00486   ; OUTI
site 00488   ; OUTI
site 0048A   ; OUTI
site 0048C   ; OUTI
site 0048E   ; OUTI
site 00490   ; OUTI
site 00492   ; OUTI
site 00494   ; OUTI
site 00496   ; OUTI
site 00498   ; OUTI
site 0049A   ; OUTI
site 0049C   ; OUTI
site 0049E   ; OUTI
site 004A0   ; OUTI
site 004A2   ; OUTI
site 004A4   ; OUTI
site 004A6   ; OUTI
site 004A8   ; OUTI
site 004AA   ; OUTI
site 004AC   ; OUTI
site 004AE   ; OUTI
site 004B0   ; OUTI
site 004B2   ; OUTI
site 004B4   ; OUTI
site 004B6   ; OUTI
site 004B8   ; OUTI
site 004BA   ; OUTI
site 004BC   ; OUTI
site 004BE   ; OUTI
site 004C0   ; OUTI
site 004C2   ; OUTI
site 004C4   ; OUTI
site 004C6   ; OUTI
site 004C8   ; OUTI
site 004CA   ; OUTI
site 004CC   ; OUTI
site 004CE   ; OUTI
site 004D0   ; OUTI
site 004D2   ; OUTI
site 004D4   ; OUTI
site 004D6   ; OUTI
site 004D8   ; OUTI
site 004DA   ; OUTI
site 004DC   ; OUTI
site 004DE   ; OUTI
site 004E0   ; OUTI
site 004E2   ; OUTI
site 004E4   ; OUTI
site 004E6   ; OUTI
site 004E8   ; OUTI
site 004EA   ; OUTI
site 004EC   ; OUTI
site 004EE   ; OUTI
site 004F0   ; OUTI
site 004F2   ; OUTI
site 004F4   ; OUTI
site 004F6   ; OUTI
site 004F8   ; OUTI
site 004FA   ; OUTI
site 004FC   ; OUTI
site 004FE   ; OUTI
site 00500   ; OUTI
site 00502   ; OUTI
site 00504   ; OUTI
site 00507   ; OUTD
site 00509   ; OUTD
site 0050B   ; OUTD
site 0050D   ; OUTD
site 0050F   ; OUTD
site 00511   ; OUTD
site 00513   ; OUTD
site 00515   ; OUTD
site 00517   ; OUTD
site 00519   ; OUTD
site 0051B   ; OUTD
site 0051D   ; OUTD
site 0051F   ; OUTD
site 00521   ; OUTD
site 00523   ; OUTD
site 00525   ; OUTD
site 00527   ; OUTD
site 00529   ; OUTD
site 0052B   ; OUTD
site 0052D   ; OUTD
site 0052F   ; OUTD
site 00531   ; OUTD
site 00533   ; OUTD
site 00535   ; OUTD
site 00537   ; OUTD
site 00539   ; OUTD
site 0053B   ; OUTD
site 0053D   ; OUTD
site 0053F   ; OUTD
site 00541   ; OUTD
site 00543   ; OUTD
site 00545   ; OUTD
site 00547   ; OUTD
site 00549   ; OUTD
site 0054B   ; OUTD
site 0054D   ; OUTD
site 0054F   ; OUTD
site 00551   ; OUTD
site 00553   ; OUTD
site 00555   ; OUTD
site 00557   ; OUTD
site 00559   ; OUTD
site 0055B   ; OUTD
site 0055D   ; OUTD
site 0055F   ; OUTD
site 00561   ; OUTD
site 00563   ; OUTD
site 00565   ; OUTD
site 00567   ; OUTD
site 00569   ; OUTD
site 0056B   ; OUTD
site 0056D   ; OUTD
site 0056F   ; OUTD
site 00571   ; OUTD
site 00573   ; OUTD
site 00575   ; OUTD
site 00577   ; OUTD
site 00579   ; OUTD
site 0057B   ; OUTD
site 0057D   ; OUTD
site 0057F   ; OUTD
site 00581   ; OUTD
site 00583   ; OUTD
site 00585   ; OUTD
site 00594   ; OUT ($BE),A
site 00597   ; OUT ($BE),A
site 005B2   ; OUT ($BE),A
site 005B5   ; OUT ($BE),A
site 006AC   ; OUT ($BF),A
site 006B2   ; OUT ($BF),A
site 006C3   ; OTIR
site 006EE   ; OUT ($BF),A
site 006F1   ; OUT ($BF),A
site 006FB   ; OUTI
site 006FD   ; OUTI
site 00728   ; OUT ($BF),A
site 0072D   ; OUT ($BF),A
site 00733   ; IN A,($BE)
site 00739   ; OUT ($BF),A
site 0073C   ; OUT ($BF),A
site 00743   ; OUT ($BE),A
site 009BD   ; OUT ($3E),A
site 009C0   ; OUT ($F2),A
site 009C8   ; OUT ($3E),A
site 009D1   ; OUT ($3F),A
site 00A14   ; OUT ($BF),A
site 00A17   ; OUT ($BF),A
site 00A1D   ; OUTI
site 00A1F   ; OUTI
site 010FD   ; OUT ($BE),A
site 01102   ; OUT ($BE),A
site 0111F   ; OUT ($BE),A
site 01124   ; OUT ($BE),A
site 01542   ; OUT ($BF),A
site 01546   ; OUT ($BF),A
site 0154F   ; OUTI
site 01555   ; OUTI
site 015A8   ; OUT ($BF),A
site 015AB   ; OUT ($BF),A
site 015B4   ; OUTI
site 015BA   ; OUTI
site 02D4C   ; OUT ($BF),A
site 02D52   ; OUT ($BF),A
site 02D58   ; IN A,($BE)
site 05E99   ; OUT ($BF),A
site 05E9E   ; OUT ($BF),A
site 05EA4   ; IN A,($BE)
site 05EAA   ; IN A,($BE)
site 06D0F   ; OUT ($BF),A
site 06D14   ; OUT ($BF),A
site 06D1A   ; IN A,($BE)
site 06DEE   ; OUT ($BF),A
site 06DF3   ; OUT ($BF),A
site 06DF6   ; IN A,($BE)
site 06DFA   ; IN A,($BE)
site 06FD6   ; OUT ($BF),A
site 06FD9   ; OUT ($BF),A
site 06FDD   ; OUT ($BE),A
site 06FE1   ; OUT ($BE),A
site 1C100   ; OUT ($F0),A
site 1C109   ; OUT ($F1),A
site 1C121   ; OUT ($7F),A
site 1C131   ; OUT (C),D
site 1C137   ; OUT ($F1),A
site 1C16A   ; OTIR
site 1C178   ; OTIR
site 1C182   ; OUT ($F0),A
site 1C188   ; OUT ($F1),A
site 1C194   ; OUTI
site 1C19A   ; OUTI
site 1C25F   ; OUT ($7F),A
site 1C263   ; OUT ($7F),A
site 1C28B   ; OUT ($7F),A
site 1C28F   ; OUT ($7F),A
site 1C292   ; OUT ($7F),A
site 1C2F8   ; OUT ($F0),A
site 1C2FF   ; OUT ($F1),A
site 1C307   ; OUT ($F0),A
site 1C30D   ; OUT ($F1),A
site 1C3F4   ; OUT ($F0),A
site 1C3FE   ; OUT (C),L
site 1C407   ; OUT ($F0),A
site 1C422   ; OUT (C),H
site 1C42A   ; OUT ($F0),A
site 1C438   ; OUT ($F1),A
site 1C444   ; OUT ($F0),A
site 1C44D   ; OUT ($F1),A
site 1C621   ; OUT ($7F),A
site 1C66C   ; OUT ($7F),A
site 1C693   ; OUT ($7F),A
site 1C698   ; OUT ($7F),A
site 1C6C4   ; OUT ($F0),A
site 1C6D2   ; OUT ($F1),A
site 1C6E3   ; OUT ($F0),A
site 1C777   ; OUTI
site 1C779   ; OUTI
site 1C77B   ; OUTI
site 1C77D   ; OUTI
site 1C77F   ; OUTI
site 1C781   ; OUTI
site 1C783   ; OUTI
site 1C785   ; OUTI
site 1C787   ; OUTI
site 1C789   ; OUTI
site 1C78B   ; OUTI
site 1C795   ; OUT (C),D
site 1C79B   ; OUT ($F1),A
site 1C7DA   ; OUT ($7F),A
site 1C830   ; OUT ($7F),A
site 1C86F   ; OUT ($7F),A
site 1C8C2   ; OUT ($7F),A
site 1C8E2   ; OUT ($7F),A
site 1C92E   ; OUT ($7F),A
site 1C938   ; OUT ($7F),A
site 1C980   ; OUT ($7F),A
site 27D2A   ; OUT ($BF),A
site 27D2D   ; OUT ($BF),A
site 27D31   ; OUT ($BE),A
site 27D37   ; OUT ($BE),A
mapst 0004F   ; LD ($FFFF),A
mapldk 000B3   # LD HL,$FFFC; LD (HL),$00
maphl 000B9   # LD (HL),$00, HL = $FFFD
maphl 000BC   # LD (HL),$01, HL = $FFFE
maphl 000BF   # LD (HL),$02, HL = $FFFF
mapst 000FA   ; LD ($FFFF),A
mapst 001B9   ; LD ($FFFF),A
mapst 00208   ; LD ($FFFF),A
mapst 00211   ; LD ($FFFF),A
mapst 0062A   ; LD ($FFFF),A
mapst 0068D   ; LD ($FFFF),A
mapst 00A3C   ; LD ($FFFF),A
mapst 00A4D   ; LD ($FFFF),A
mapst 01705   ; LD ($FFFF),A
mapst 0170D   ; LD ($FFFF),A
mapst 0174F   ; LD ($FFFF),A
mapst 01948   ; LD ($FFFF),A
mapst 01972   ; LD ($FFFF),A
mapst 01983   ; LD ($FFFF),A
mapst 01C1E   ; LD ($FFFF),A
mapst 02077   ; LD ($FFFF),A
mapst 0211C   ; LD ($FFFF),A
mapst 02241   ; LD ($FFFF),A
mapst 024B3   ; LD ($FFFF),A
mapst 02EE0   ; LD ($FFFF),A
mapst 04628   ; LD ($FFFF),A
mapst 048F8   ; LD ($FFFF),A
mapst 04909   ; LD ($FFFF),A
mapst 04918   ; LD ($FFFF),A
mapst 049B1   ; LD ($FFFF),A
mapst 059AD   ; LD ($FFFF),A
mapst 06E18   ; LD ($FFFF),A
mapst 06E3F   ; LD ($FFFF),A
mapst 06EF0   ; LD ($FFFF),A
mapst 06F57   ; LD ($FFFF),A
mapst 06F6A   ; LD ($FFFF),A
mapst 07007   ; LD ($FFFF),A
mapst 07065   ; LD ($FFFF),A
mapst 0730D   ; LD ($FFFF),A
mapst 07342   ; LD ($FFFF),A
mapst 07356   ; LD ($FFFF),A
mapst 0742F   ; LD ($FFFF),A
mapst 07460   ; LD ($FFFF),A
mapst 07488   ; LD ($FFFF),A
mapst 074A0   ; LD ($FFFF),A
mapst 074DB   ; LD ($FFFF),A
mapst 074F9   ; LD ($FFFF),A

# Forgotten Worlds (Europe, Brazil).cht, "Infinite Health": RAM $CC8C is the health, 8 at the
# top. The catalogue writes $0F, which draws the bar taller than its frame; $08 is the full bar
poke "Infinite health"
ar 00CC-8C08
endpoke

# Forgotten Worlds (Europe, Brazil).cht, "Invulnerability": RAM $CC8D is the hit timer, held
# at $21 so that no hit lands
poke "Invincibility"
ar 00CC-8D21
endpoke

# Forgotten Worlds (Europe, Brazil).cht, "Always Have Life Potion": the potion revives the
# player at zero health instead of ending the game
poke "Life potion"
ar 00CC-E001
endpoke

# Forgotten Worlds (Europe, Brazil).cht, "Always Have Armor": RAM $CCD1 and $CCD2 are the armor
poke "Armor"
ar 00CC-D101
ar 00CC-D205
endpoke

# Forgotten Worlds (Europe, Brazil).cht, "Infinite Zenny": RAM $CD50 and $CD51 are the money,
# one unit is 100 zenny; the shop shows 999900
poke "Infinite zenny"
ar 00CD-50FF
ar 00CD-51FF
endpoke

# Forgotten Worlds (Europe, Brazil).cht, "Faster Rate of Fire": RAM $CC92 and $CC93 held at 0
poke "Faster fire"
ar 00CC-9200
ar 00CC-9300
endpoke

# Forgotten Worlds (Europe) (Action Replay).cht, "Always Have Satellite type": RAM $CC96 is the
# satellite type; 00 and 02 to 07 each show another satellite, 01 blanks the screen
poke "Satellite type"
ar 00CC-96??
endpoke
