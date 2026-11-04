# Rainbow Islands (Europe), CRC32 C172A22C, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, checked against reference I/O logs
# (600 s of random input, 180 s of the attract mode).
# Decisions:
# - No RST vector has $FF filler, so $0000-$0002 (DI; IM 1) is the io vector and the
#   game starts at $0003.
# - The sprite table clear at $04CC (after the RET at $04CB) and the routines $12F5,
#   $12FE and $1306 (called from $12E1) are code that no path or recording reached;
#   they are scan entries, and their VDP writes $04D7, $04E6, $1315 and $131D are sites.
# - Every bank change is LD ($C012),A; LD ($FFFF),A. The byte scan's high-confidence
#   stores of that form in banks 0 and 1 are patched; the low-confidence one at $0AE8C
#   (bank 2) is data.
# - The OUT ($3F),A patterns in bank 4 ($10CD2, $10D52) and IN A,($7F) in bank 8
#   ($23163) are in graphics data.
name Rainbow Islands
cart C172A22C
hz 50		; No-Intro region Europe
vector 00 io
start 0003
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 000DB   ; IN A,($BF)
site 000DD   ; IN A,($BF)
site 000EE   ; IN A,($BF)
site 000F0   ; IN A,($BF)
site 000FC   ; IN A,($BF)
site 0010E   ; OUT ($3F),A
site 00110   ; IN A,($DD)
site 0011A   ; OUT ($3F),A
site 0011C   ; IN A,($DD)
site 00124   ; OUT ($3F),A
site 0012C   ; OUT ($BF),A
site 001D6   ; OUT (C),A
site 001E6   ; IN A,(C)
site 00203   ; OUT ($BF),A
site 00207   ; OUT ($BF),A
site 00221   ; OUT ($BE),A
site 00223   ; OUT ($BE),A
site 00238   ; OUT ($BE),A
site 0023C   ; OUT ($BE),A
site 00250   ; OUT ($BE),A
site 0025B   ; OUT ($BE),A
site 00272   ; OTIR
site 0027F   ; OUT ($BE),A
site 00283   ; OUT ($BE),A
site 00290   ; OTDR
site 002A0   ; OUT ($BE),A
site 002A4   ; OUT ($BE),A
site 002E8   ; OUT ($BE),A
site 00304   ; OUT ($BE),A
site 0030C   ; OUT ($BE),A
site 004A6   ; OUT ($BE),A
site 004AE   ; OUT ($BE),A
site 004D7   ; OUT ($BE),A
site 004E6   ; OUT ($BE),A
site 005E4   ; OUT ($BE),A
site 005EC   ; OUT ($BE),A
site 00608   ; OUT ($BE),A
site 01315   ; OUT ($BE),A
site 0131D   ; OUT ($BE),A
site 06262   ; OUT (C),A
site 0626A   ; OUT (C),A
site 06A2E   ; OUT ($BE),A
site 06A36   ; OUT ($BE),A
site 06C92   ; OUT ($BE),A
site 06C9A   ; OUT ($BE),A
site 0702F   ; OUT (C),L
site 07035   ; OUT (C),H
site 072F9   ; OUT ($BE),A
site 07301   ; OUT ($BE),A
site 0732F   ; OUT ($BE),A
site 07337   ; OUT ($BE),A
site 07558   ; OUT ($BE),A
site 07560   ; OUT ($BE),A
site 3C1E7   ; OUT ($7F),A
site 3C30D   ; OUT ($7F),A
site 3C49F   ; OTIR
site 3C5B7   ; OUT ($7F),A
site 3C5C1   ; OUT ($7F),A
site 3C5DE   ; OUT ($7F),A
site 3C6E2   ; OUT ($7F),A
site 3C76E   ; OUT ($7F),A
site 3C810   ; OUT ($7F),A
site 3C819   ; OUT ($7F),A
site 3C829   ; OUT ($7F),A
site 3C8A5   ; OUT ($7F),A
mapst 0009C   ; LD ($FFFC),A
mapst 000A1   ; LD ($FFFF),A
mapsthl 000AA   ; LD ($FFFC),HL
mapsthl 000B0   ; LD ($FFFE),HL
mapst 00183   ; LD ($FFFF),A
mapst 0018D   ; LD ($FFFF),A
mapst 001B7   ; LD ($FFFF),A
mapst 002CE   ; LD ($FFFF),A
mapst 002F8   ; LD ($FFFF),A
mapst 0035B   ; LD ($FFFF),A
mapst 0037C   ; LD ($FFFF),A
mapst 0038E   ; LD ($FFFF),A
mapst 003AA   ; LD ($FFFF),A
mapst 005A4   ; LD ($FFFF),A
mapst 005FE   ; LD ($FFFF),A
mapst 00D85   ; LD ($FFFF),A
mapst 00E03   ; LD ($FFFF),A
mapst 00E10   ; LD ($FFFF),A
mapst 00E2D   ; LD ($FFFF),A
mapst 01173   ; LD ($FFFF),A
mapst 01190   ; LD ($FFFF),A
mapst 013B1   ; LD ($FFFF),A
mapst 013D0   ; LD ($FFFF),A
mapst 0146C   ; LD ($FFFF),A
mapst 01477   ; LD ($FFFF),A
mapst 015E9   ; LD ($FFFF),A
mapst 0160B   ; LD ($FFFF),A
mapst 016B9   ; LD ($FFFF),A
mapst 016CF   ; LD ($FFFF),A
mapst 01E61   ; LD ($FFFF),A
mapst 01E77   ; LD ($FFFF),A
mapst 025C8   ; LD ($FFFF),A
mapst 02603   ; LD ($FFFF),A
mapst 026D5   ; LD ($FFFF),A
mapst 02744   ; LD ($FFFF),A
mapst 031E6   ; LD ($FFFF),A
mapst 031FA   ; LD ($FFFF),A
mapst 03213   ; LD ($FFFF),A
mapst 03227   ; LD ($FFFF),A
mapst 0366C   ; LD ($FFFF),A
mapst 03676   ; LD ($FFFF),A
mapst 03696   ; LD ($FFFF),A
mapst 036F8   ; LD ($FFFF),A
mapst 037E4   ; LD ($FFFF),A
mapst 03834   ; LD ($FFFF),A
mapst 03901   ; LD ($FFFF),A
mapst 03927   ; LD ($FFFF),A
mapst 03934   ; LD ($FFFF),A
mapst 0395B   ; LD ($FFFF),A
mapst 04290   ; LD ($FFFF),A
mapst 042CB   ; LD ($FFFF),A
mapst 042DB   ; LD ($FFFF),A
mapst 04339   ; LD ($FFFF),A
mapst 04346   ; LD ($FFFF),A
mapst 04376   ; LD ($FFFF),A
mapst 043AA   ; LD ($FFFF),A
mapst 043C6   ; LD ($FFFF),A
mapst 043DB   ; LD ($FFFF),A
mapst 04D42   ; LD ($FFFF),A
mapst 04D4C   ; LD ($FFFF),A
mapst 04DCE   ; LD ($FFFF),A
mapst 04DF1   ; LD ($FFFF),A
mapst 04E22   ; LD ($FFFF),A
mapst 04E2F   ; LD ($FFFF),A
mapst 04F77   ; LD ($FFFF),A
mapst 04F8A   ; LD ($FFFF),A
mapst 04FDE   ; LD ($FFFF),A
mapst 05021   ; LD ($FFFF),A
mapst 0507D   ; LD ($FFFF),A
mapst 050BF   ; LD ($FFFF),A
mapst 05127   ; LD ($FFFF),A
mapst 0515E   ; LD ($FFFF),A
mapst 051C9   ; LD ($FFFF),A
mapst 051DC   ; LD ($FFFF),A
mapst 0523B   ; LD ($FFFF),A
mapst 05288   ; LD ($FFFF),A
mapst 052F3   ; LD ($FFFF),A
mapst 05306   ; LD ($FFFF),A
mapst 05362   ; LD ($FFFF),A
mapst 053B8   ; LD ($FFFF),A
mapst 0590F   ; LD ($FFFF),A
mapst 05928   ; LD ($FFFF),A
mapst 05A94   ; LD ($FFFF),A
mapst 05ACE   ; LD ($FFFF),A
mapst 05B18   ; LD ($FFFF),A
mapst 05B52   ; LD ($FFFF),A
mapst 05C4E   ; LD ($FFFF),A
mapst 05C61   ; LD ($FFFF),A
mapst 0618F   ; LD ($FFFF),A
mapst 061A2   ; LD ($FFFF),A
mapst 061DF   ; LD ($FFFF),A
mapst 061F2   ; LD ($FFFF),A
mapst 061FF   ; LD ($FFFF),A
mapst 06211   ; LD ($FFFF),A
mapst 0621E   ; LD ($FFFF),A
mapst 06236   ; LD ($FFFF),A
mapst 06AF2   ; LD ($FFFF),A
mapst 06B05   ; LD ($FFFF),A
mapst 06B11   ; LD ($FFFF),A
mapst 06B70   ; LD ($FFFF),A
mapst 06BEE   ; LD ($FFFF),A
mapst 06C00   ; LD ($FFFF),A
mapst 0721D   ; LD ($FFFF),A
mapst 07380   ; LD ($FFFF),A
mapst 0738B   ; LD ($FFFF),A
mapst 01289   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 01293   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 017E0   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 017F6   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 018B9   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 018CF   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 03077   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 03081   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 0327E   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 03292   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 032A7   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 032BB   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 03498   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 034AE   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 03589   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 0359B   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 035D9   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it
mapst 03605   # LD ($FFFF),A; after LD ($C012),A; 32 bytes of valid code before it

# Rainbow Islands (Europe).cht, "Infinite Lives" (also in Rainbow Islands - Story of the
# Bubble Bobble 2 (Europe, Brazil) (Action Replay).cht): RAM $C02E is the lives count
poke "Infinite lives"
ar 00C0-2E09
endpoke

# Rainbow Islands (Europe).cht, "Invincibility": RAM $C5AA is the player's state flags;
# bit 2 makes the player take no hits
poke "Invincibility"
ar 00C5-AA04
endpoke

# Rainbow Islands (Europe).cht, "Enable World Select on Title Screen": RAM $D1CF is the
# flag that the title screen tests; with it set, button 2 on the title screen steps the
# world (shown in place of the B of BUTTON), and button 1 starts in that world
poke "World select"
ar 00D1-CF01
endpoke

# Rainbow Islands (Europe).cht, "Start with ?? Lives, instead of 3": the cart byte at
# $139A is the lives count of a new game
poke "Start lives ??"
gg ??3-9AE-E66
endpoke

# Rainbow Islands (Europe).cht, "Continue with ?? Lives": the cart byte at $71B3 is the
# lives count after a continue
poke "Continue lives ??"
gg ??1-B38-E66
endpoke

# Rainbow Islands (Europe).cht, "Infinite Time (Water doesn't rise)": RAM $C59B is the low
# byte of the round's time counter; the player loses a life when it runs out
poke "Infinite time"
ar 00C5-9BA4
endpoke

# Rainbow Islands (Europe).cht, "Have all Items (invincible) (after dying or in the menu)":
# RAM $C5BA and $C5BB hold the item flags; the player shoots with the rainbow power-ups
# and takes no hits
poke "All items"
ar 00C5-BA6F
ar 00C5-BB6F
endpoke

# Rainbow Islands (Europe).cht, "Have all Big Diamonds": RAM $C158 holds the big diamonds
# collected; the READY screen shows all seven
poke "All big diamonds"
ar 00C1-587F
endpoke
