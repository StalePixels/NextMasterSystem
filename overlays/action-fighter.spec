# Action Fighter (USA, Europe, Brazil) (En) (Rev 1), CRC32 3658F3E0, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - $0018-$001A are $FF filler and no code uses RST $18: it is the io vector. The game
#   has no RST of its own.
# - The writes to ports $DE and $DF are the SC-3000 keyboard ports, which the game probes
#   at power on ($02E8-$0402); on a Master System they do nothing.
# - The VDP routines at $014D (read one VRAM byte), $01A0 (read a VRAM block) and $0223
#   (write a column of cells), the bank routine at $1EBA (sets slot 2 from A, reads a
#   header at $8000, returns through JP (IX)) and the PSG routines at $7538 and $753D
#   are code that no scanned path or recording reaches; their sites are patched as code,
#   which costs nothing if they never run.
# - $323D (LD (BC),A) is in the byte table at $3236 that the pointer harvest took for
#   code, and $1D75 (IN A,($C1)) is the operand of LD A,($C1DB) at $1D74: not code.
name Action Fighter
cart 3658F3E0
hz any		; No-Intro regions USA, Europe, Brazil
vector 18 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 000F6   ; OTIR
site 00127   ; OUT ($BF),A
site 0012C   ; OUT ($BF),A
site 00130   ; OUT ($BF),A
site 00133   ; OUT ($BF),A
site 00145   ; OUT ($BE),A
site 0014E   ; OUT ($BF),A
site 00151   ; OUT ($BF),A
site 00155   ; IN A,($BE)
site 0015D   ; OUT ($BE),A
site 00161   ; OUT ($BF),A
site 00164   ; OUT ($BF),A
site 00173   ; OUTI
site 00193   ; OUTI
site 00199   ; OUT (C),A
site 001A2   ; OUT ($BF),A
site 001A5   ; OUT ($BF),A
site 001A8   ; IN A,($BE)
site 001B8   ; IN A,($BE)
site 001DF   ; OUT ($BE),A
site 001E4   ; OUT ($BE),A
site 001F3   ; OUTI
site 001FA   ; OUT (C),A
site 00212   ; OUTI
site 00228   ; OUT (C),H
site 00231   ; OUT (C),L
site 0024C   ; OUT (C),D
site 00275   ; OUT ($BE),A
site 002A5   ; OTIR
site 002AF   ; OTIR
site 002B4   ; OUT ($3F),A
site 002B6   ; IN A,($DD)
site 002C0   ; OUT ($3F),A
site 002C2   ; IN A,($DD)
site 002CB   ; OUT ($3F),A
site 002E8   ; OUT ($DF),A
site 002F0   ; OUT ($DE),A
site 002F2   ; IN A,($DE)
site 002FB   ; OUT ($7F),A
site 002FF   ; OUT ($7F),A
site 00303   ; OUT ($7F),A
site 00307   ; OUT ($7F),A
site 00310   ; IN A,($DD)
site 00332   ; IN A,($DC)
site 00337   ; IN A,($DC)
site 0033C   ; IN A,($DD)
site 0034C   ; OUT ($DE),A
site 0034E   ; IN A,($DC)
site 00353   ; OUT ($DE),A
site 00355   ; IN A,($DC)
site 00360   ; OUT ($DE),A
site 00362   ; IN A,($DC)
site 0036D   ; OUT ($DE),A
site 0036F   ; IN A,($DC)
site 00381   ; OUT ($DE),A
site 00383   ; IN A,($DC)
site 0038E   ; OUT ($DE),A
site 00390   ; IN A,($DC)
site 003B6   ; OUT ($DE),A
site 003B8   ; IN A,($DC)
site 003BD   ; IN A,($DD)
site 003C7   ; OUT ($DE),A
site 003C9   ; IN A,($DC)
site 003DB   ; OUT ($DE),A
site 003DD   ; IN A,($DC)
site 003E8   ; OUT ($DE),A
site 003EA   ; IN A,($DC)
site 003F5   ; OUT ($DE),A
site 003F7   ; IN A,($DD)
site 00402   ; OUT ($DE),A
site 00404   ; IN A,($DD)
site 0041F   ; IN A,($BF)
site 004AB   ; OUT (C),H
site 006B2   ; OUT ($BF),A
site 006B6   ; OUT ($BF),A
site 006F0   ; OUT ($BF),A
site 006F4   ; OUT ($BF),A
site 0074A   ; OUT ($BE),A
site 00C1D   ; OUT ($BE),A
site 00C24   ; OUT ($BE),A
site 00C2B   ; OUT ($BE),A
site 00C32   ; OUT ($BE),A
site 00C73   ; OUT ($BE),A
site 00C78   ; OUT ($BE),A
site 00C94   ; OUT ($BE),A
site 00C99   ; OUT ($BE),A
site 00E84   ; OUT ($BE),A
site 01071   ; OUT (C),A
site 01075   ; OUT (C),A
site 01079   ; OUT (C),B
site 0107B   ; OUT (C),A
site 01F68   ; OUT ($BE),A
site 01F6E   ; OUT ($BE),A
site 01F74   ; OUT ($BE),A
site 01F7B   ; OUT ($BE),A
site 023EC   ; OUT ($BE),A
site 023F0   ; OUT ($BE),A
site 02405   ; OUT ($BE),A
site 03C6E   ; OUT ($BE),A
site 03C75   ; OUT ($BE),A
site 0620C   ; OUT ($BF),A
site 06210   ; OUT ($BF),A
site 0708A   ; OUT ($7F),A
site 07170   ; OUT ($7F),A
site 07194   ; OUT ($7F),A
site 07198   ; OUT ($7F),A
site 074B4   ; OUT ($7F),A
site 07516   ; OUT ($7F),A
site 07530   ; OTIR
site 0753A   ; OUT ($7F),A
site 0753F   ; OUT ($7F),A
mapst 00679   ; LD ($FFFF),A
mapst 007ED   ; LD ($FFFF),A
mapst 0093D   ; LD ($FFFF),A
mapst 01118   ; LD ($FFFF),A
mapst 01319   ; LD ($FFFF),A
mapst 01D9E   ; LD ($FFFF),A
mapst 01DD5   ; LD ($FFFF),A
mapst 01DF8   ; LD ($FFFF),A
mapst 01E0C   ; LD ($FFFF),A
mapst 01E37   ; LD ($FFFF),A
mapst 01E82   ; LD ($FFFF),A
mapst 01EBF   ; LD ($FFFF),A
mapst 023B9   ; LD ($FFFF),A
mapst 02D1E   ; LD ($FFFF),A
mapst 03DEB   ; LD ($FFFF),A
mapst 06017   ; LD ($FFFF),A
mapst 06098   ; LD ($FFFF),A
mapst 0621E   ; LD ($FFFF),A
mapst 062B4   ; LD ($FFFF),A
mapst 062E5   ; LD ($FFFF),A

# Action Fighter (USA, Europe, Brazil) (Rev 1).cht, "Infinite Time": RAM $C118/$C119 is the
# timer (999 at the start); the cheat holds the low byte at $E8, this block at $E7 so that the
# timer is 999 on the mission card as well
poke "Infinite time"
ar 00C1-18E7
endpoke

# Action Fighter (USA, Europe, Brazil) (Rev 1).cht, "Letters A, B, C, D, E & F": RAM $C11E
# held at 6 shows the letters A to F and turns the bike into the red car
poke "All letters A-F"
ar 00C1-1E06
endpoke

# Action Fighter (USA, Europe, Brazil) (Rev 1).cht, "Mission Select [Replace ? With 0-4]": RAM
# $C115 is the mission number, read when a mission starts; the game clears it at a new game,
# so the chosen mission starts after a death (0 first mission, 4 last mission)
poke "Mission on restart"
ar 00C1-15??
endpoke
