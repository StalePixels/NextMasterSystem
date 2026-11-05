# Ghouls'n Ghosts (USA, Europe, Brazil) (En), CRC32 7A92EBA6, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input), plus routine starts given with --entry, because the game reaches most of
# its code through tables that hold a bank and an address, which the scanner does not
# follow:
# - the game mode table at $024E (9 entries of bank, address; JP (HL) at $024D);
# - the object handler table at $10B5 (entries 1-84 of bank, address; the call at $10AF
#   switches slot 2 to the entry's bank first);
# - the stage table at $173A (words, index $C06B; JP (HL) at $1769);
# - the state tables of the object handlers (LD HL,table; JP $091A), in banks 0, 1, 3, 4,
#   7, 9, 10 and 14, each read up to the start of the first code it names.
# Decisions:
# - No free RST vector ($0008-$0038 are all the game's), so $0000-$0002 (DI; JP $0200)
#   is the io vector, and the game starts at $0200.
# - The VDP block fill $02A2 and the FM detection $02F9 (after the RET at $02F8, which
#   the start-up code calls) are code that nothing in the cart calls or jumps to: no site
#   lines (verdict unused).
# - The LD (BC),A stores that the scanner proves into $0000-$7FFF are in the sound
#   driver's pointer and note tables in bank 2 ($8969 on), which the 32-entry table at
#   $8717 reaches when read too far: data.
# - The other byte patterns that no path reached are a word table at $1010, a pointer
#   table in bank 4 ($BE80) and graphics in banks 8, 10, 11, 12 and 13 (verdict false).
# - hsplit: in the round 2-3 boss fight the line interrupt at line 159 sets H scroll 0 for
#   the floor, and the vertical blank sets $88-$8C for the rest. Without the switch the
#   floor shows a column of wrong map cells at the copper's map switch column.
# - priority: the stone face statue of round 3-2 is priority cells, and sprites pass
#   behind it. The switch costs most in the name table strip writer at $0926-$09AC, so a
#   few frames of round 3-2 play go just over a Next frame.
name Ghouls'n Ghosts
cart 7A92EBA6
hz any		; No-Intro regions USA, Europe, Brazil
vector 00 io
start 0200
hsplit		; round 2-3 boss: H $88-$8C in the vertical blank, H 0 for the floor from line 159
priority	; round 3-2: the stone face statue is 60 priority cells that sprites pass behind
asm 00201 2   ; IM 1 -> IM 2
    im 2
endasm
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 00269   ; IN A,($BF)
site 00271   ; OTIR
site 0028F   ; OUT ($BF),A
site 00292   ; OUT ($BF),A
site 00299   ; OUT ($BE),A
site 002BB   ; OUT ($BE),A
site 002C1   ; OUT ($BE),A
site 002D6   ; OUT ($BE),A
site 002F0   ; OUT ($BE),A
site 00346   ; OUT ($3F),A
site 00348   ; IN A,($DD)
site 00352   ; OUT ($3F),A
site 00354   ; IN A,($DD)
site 0035D   ; OUT ($3F),A
site 0037F   ; OUT ($BF),A
site 00383   ; OUT ($BF),A
site 0038A   ; OUT ($BF),A
site 0038E   ; OUT ($BF),A
site 00393   ; OUT ($BF),A
site 00397   ; OUT ($BF),A
site 003A9   ; IN A,($DD)
site 003DA   ; OUT ($BF),A
site 003DE   ; OUT ($BF),A
site 003E5   ; OUT ($BF),A
site 003E9   ; OUT ($BF),A
site 00422   ; OUT ($BF),A
site 00426   ; OUT ($BF),A
site 0042B   ; OUT ($BF),A
site 0042F   ; OUT ($BF),A
site 00434   ; OUT ($BF),A
site 00438   ; OUT ($BF),A
site 00456   ; INI
site 0046D   ; OUTI
site 00614   ; OUT ($BF),A
site 00617   ; OUT ($BF),A
site 00624   ; OUT ($BF),A
site 00629   ; OUT ($BF),A
site 00631   ; OUT ($BE),A
site 00636   ; OUT ($BE),A
site 0065A   ; OUT ($BE),A
site 0065F   ; OUT ($BE),A
otir 006BA   ; OUTI
site 006C4   ; OUTI
site 006C8   ; OUTI
site 00705   ; OUT ($BE),A
site 00717   ; OUT ($BE),A
site 00725   ; IN A,($BE)
site 007A1   ; OUT ($BF),A
site 007A4   ; OUT ($BF),A
site 007A7   ; OUT ($BE),A
site 007AB   ; OUT ($BE),A
site 00901   ; OUT ($BE),A
site 00926   ; OUT ($BF),A
site 0092A   ; OUT ($BF),A
site 00930   ; OUT ($BE),A
site 00934   ; OUT ($BE),A
site 00938   ; OUT ($BE),A
site 0093C   ; OUT ($BE),A
site 00940   ; OUT ($BE),A
site 00944   ; OUT ($BE),A
site 00948   ; OUT ($BE),A
site 0094C   ; OUT ($BE),A
site 00950   ; OUT ($BE),A
site 00954   ; OUT ($BE),A
site 00958   ; OUT ($BE),A
site 0095C   ; OUT ($BE),A
site 00960   ; OUT ($BE),A
site 00964   ; OUT ($BE),A
site 00968   ; OUT ($BE),A
site 0096C   ; OUT ($BE),A
site 00970   ; OUT ($BE),A
site 00974   ; OUT ($BE),A
site 00978   ; OUT ($BE),A
site 0097C   ; OUT ($BE),A
site 00980   ; OUT ($BE),A
site 00984   ; OUT ($BE),A
site 00988   ; OUT ($BE),A
site 0098C   ; OUT ($BE),A
site 00990   ; OUT ($BE),A
site 00994   ; OUT ($BE),A
site 00998   ; OUT ($BE),A
site 0099C   ; OUT ($BE),A
site 009A0   ; OUT ($BE),A
site 009A4   ; OUT ($BE),A
site 009A8   ; OUT ($BE),A
site 009AC   ; OUT ($BE),A
site 009CB   ; OUT ($BE),A
site 009DD   ; OUTI
site 009DF   ; OUTI
site 009E8   ; OUT ($DE),A
site 009EA   ; IN A,($DC)
site 00A05   ; IN A,($DD)
site 00A11   ; IN A,($DC)
site 03ED5   ; OUT ($BF),A
site 03ED8   ; OUT ($BF),A
site 03EDF   ; OUT ($BE),A
site 03EE7   ; OUT ($BE),A
site 03F02   ; OUT ($BF),A
site 03F05   ; OUT ($BF),A
site 03F0C   ; OUT ($BE),A
site 03F14   ; OUT ($BE),A
site 065AD   ; IN A,($BF)
site 066BA   ; IN A,($BF)
site 067D3   ; IN A,($BF)
site 069B1   ; IN A,($BF)
site 06C4E   ; OUT ($BE),A
site 06E88   ; OUT ($BE),A
site 06FD8   ; IN A,($BF)
site 0703F   ; IN A,($BF)
site 071C2   ; OUT ($BE),A
site 071C5   ; OUT ($BE),A
site 07245   ; OUT ($BE),A
site 0762C   ; OUT ($BE),A
site 07634   ; OUT ($BE),A
site 081CA   ; OUT ($7F),A
site 0829B   ; OUT ($7F),A
site 0842D   ; OTIR
site 08543   ; OUT ($7F),A
site 0854D   ; OUT ($7F),A
site 0856A   ; OUT ($7F),A
site 0866E   ; OUT ($7F),A
site 086FC   ; OUT ($7F),A
site 0879E   ; OUT ($7F),A
site 087A7   ; OUT ($7F),A
site 087B7   ; OUT ($7F),A
site 0882B   ; OUT ($7F),A
site 1F512   ; OUT ($BE),A
site 1F527   ; OUT ($BE),A
site 27A03   ; OUT ($BE),A
site 27A09   ; OUT ($BE),A
site 3B70E   ; OUT ($BE),A
site 3B714   ; OUT ($BE),A
mapst 0001B   ; LD ($FFFF),A
mapst 00207   ; LD ($FFFD),A
mapst 0020C   ; LD ($FFFE),A
mapst 003C2   ; LD ($FFFF),A
mapst 003CB   ; LD ($FFFF),A
mapst 00643   ; LD ($FFFF),A
mapst 006E4   ; LD ($FFFF),A
mapst 0078A   ; LD ($FFFF),A
mapst 007B9   ; LD ($FFFF),A

# Ghouls'n Ghosts (USA, Europe).cht, "Infinite Lives": RAM $C033 is the lives count, held at 9
poke "Infinite lives"
ar 00C0-3309
endpoke

# Ghouls'n Ghosts (USA, Europe).cht, "Invincibility" (Game Genie C95-F2E-3BE): the cart byte
# $15F2, the DEC (HL) that takes one hit off $C04C, becomes $C9 (RET), so a hit
# from an enemy takes nothing off Arthur
poke "Invincibility"
gg C95-F2E-3BE
endpoke

# Ghouls'n Ghosts (USA, Europe) (Action Replay).cht, "Infinite Hits": RAM $C04C is Arthur's hits
# left, held at 1. A hit does not kill him, but he stays without armor
poke "Never die"
ar 00C0-4C01
endpoke

# Ghouls'n Ghosts (USA, Europe).cht, "Enable Cheat Mode" (Game Genie 007-E14-D5E): the title
# screen leads to the game's own OPTION menu, with the round, the starting helmet, armor, shoes
# and weapon, and the number of players
poke "Options menu"
gg 007-E14-D5E
endpoke

# Ghouls'n Ghosts (USA, Europe) (Action Replay).cht, "Arthur Starts With X Weapon": RAM $C041 is
# the weapon, held. Values 00 to 05 give six weapons; 06 breaks the game
poke "Weapon"
ar 00C0-41??
endpoke

# Ghouls'n Ghosts (USA, Europe) (Action Replay).cht, "Arthur Starts With X Armor": RAM $C043 is
# the armor, held. Values 00 to 07 give eight armors, each with its own colour
poke "Armor"
ar 00C0-43??
endpoke
