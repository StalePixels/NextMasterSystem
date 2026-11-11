# Pac-Mania (Europe), CRC32 BE57A9A5, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - No free RST vector: $0008-$000F is the start-up code and $0011-$0034 is sprite table
#   data that $4186 copies to VRAM. So $0000-$0002 (DI; the first byte of LD SP,$C7FC)
#   is the io vector, and the game starts at $0004 with SP $C7FC.
# - No code runs from slot 2: banks 2-7 are data, and the spec patches nothing there.
#   The byte patterns at $00034 and $1AFE2 are data (verdict false).
name Pac-Mania
cart BE57A9A5
hz 50		; No-Intro region Europe
vector 00 io
start 0004 C7FC
asm 00004 2   ; IM 1 -> IM 2
    im 2
endasm
site 0003A   ; IN A,($DD)
site 00041   ; IN A,($BF)
site 0058A   ; OUT (C),A
site 00590   ; OUT (C),A
site 00597   ; IN A,(C)
site 0059D   ; IN A,(C)
site 005A7   ; OUT ($BF),A
site 005AB   ; OUT ($BF),A
site 005B1   ; OUT ($BE),A
site 005BA   ; IN A,($7E)
site 005C7   ; OUT ($BF),A
site 005CD   ; OUT ($BF),A
site 005D4   ; OUT ($BF),A
site 005DA   ; OUT ($BF),A
site 005E0   ; OUT ($BE),A
site 008F8   ; OUT ($7F),A
site 0092D   ; OUT ($7F),A
site 00931   ; OUT ($7F),A
site 00935   ; OUT ($7F),A
site 00946   ; OUT ($7F),A
site 00981   ; OUT ($7F),A
site 00985   ; OUT ($7F),A
site 00989   ; OUT ($7F),A
site 009C2   ; OUT ($7F),A
site 009D3   ; OUT ($7F),A
site 00A29   ; OUT ($7F),A
site 00A32   ; OUT ($7F),A
site 00A36   ; OUT ($7F),A
site 00A3B   ; OUT ($7F),A
site 013FD   ; OUT ($7F),A
site 01401   ; OUT ($7F),A
site 01405   ; OUT ($7F),A
site 01409   ; OUT ($7F),A
site 01A95   ; OUT ($BE),A
site 01A9C   ; OUT ($BE),A
site 01AA3   ; OUT ($BE),A
site 01AAA   ; OUT ($BE),A
site 01AB8   ; OUT ($BE),A
site 01ABD   ; OUT ($BE),A
site 01AC7   ; OUT ($BE),A
site 01ACC   ; OUT ($BE),A
site 01AD1   ; OUT ($BE),A
site 01AD6   ; OUT ($BE),A
site 01AE0   ; OUT ($BE),A
site 01AE5   ; OUT ($BE),A
site 0401E   ; OUT ($BF),A
site 04022   ; OUT ($BF),A
site 04027   ; OUT ($BE),A
site 0403C   ; OUT ($BF),A
site 04043   ; OUT ($BF),A
site 04048   ; OUT ($BF),A
site 0404F   ; OUT ($BF),A
site 04052   ; OUT ($BE),A
site 04056   ; OUT ($BF),A
site 0405E   ; OUT ($BF),A
site 04062   ; OUT ($BF),A
site 04069   ; OUT ($BF),A
site 0406E   ; OUT ($BE),A
site 04078   ; IN A,($DC)
site 04214   ; OUT ($BF),A
site 04218   ; OUT ($BF),A
site 04550   ; OUT ($7F),A
site 04554   ; OUT ($7F),A
site 04558   ; OUT ($7F),A
site 0455C   ; OUT ($7F),A
site 04879   ; OUT ($BE),A
site 0487F   ; OUT ($BE),A
mapst 000F9   ; LD ($FFFF),A
mapst 0010B   ; LD ($FFFF),A
mapst 0024E   ; LD ($FFFF),A
mapst 003DB   ; LD ($FFFF),A
mapst 003E6   ; LD ($FFFF),A
mapst 004DB   ; LD ($FFFF),A
mapst 02872   ; LD ($FFFF),A
mapst 02883   ; LD ($FFFF),A
mapst 02A3D   ; LD ($FFFF),A
mapst 02C58   ; LD ($FFFF),A
mapst 043E8   ; LD ($FFFF),A

# Pac-Mania (Europe) (Action Replay).cht, "Infinite Lives": RAM $C040 is the lives counter,
# held at 9; the game never reaches the game-over screen
poke "Infinite lives"
ar 00C0-4009
endpoke

# Pac-Mania (Europe).cht, "Eat One Pellet To Complete Level": RAM $C020 is the count of pellets
# left in the round, held at 1; the next pellet eaten clears the round
poke "One pellet clears round"
ar 00C0-2001
endpoke
