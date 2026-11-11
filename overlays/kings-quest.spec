# King's Quest - Quest for the Crown (USA), CRC32 F8D33BC4, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - $0018-$0037 are zero bytes that no code reaches, and the game has no RST of its own:
#   $20 is the io vector. $0000 cannot be: the game resets itself with JP $0000 and
#   JP Z,$0000 ($241D on the reset button, $3284 from the script).
# - Scan entry points (sitescan --entry): the targets of the three word tables that
#   $14CF, $14EE and $1546 call through $036A ($1F3B, $1F59, $1F65), and the routines
#   that the script command handlers at $30CF-$311A load into BC and call through $3144.
#   The RET at $3179 is the script's bad-opcode handler, which returns to the script
#   pointer the interpreter pushed; it is not a path the game takes.
# - The VRAM routines at $023B (read address), $0251 (write address and one byte),
#   $027A (fill) and $0293 (word fill), and the PSG noise write at $7EDF, are code that
#   no call, jump or table entry in the cart names; their sites are patched as code,
#   which costs nothing if they never run.
# - Bank 1 $4000-$58FC is graphics; banks 2-7 are graphics and script data. No code runs
#   in slot 2. The pointer harvest entries $75DF and $77C5 are byte tables that $7806
#   reads through ($D4BB); $77FE (LD (DE),A to $120C) is in that table.
# - priority: the scenery tiles that Graham walks behind (tree trunks, walls) and the
#   message boxes have the priority bit, and must cover the sprites.
# - Pause: the NMI handler at $24D0 toggles $D526, and the frame interrupt handler at
#   $24AC loops while it is set, with interrupts off. The runtime gives the pause NMI only
#   from its own frame interrupt, so the second Pause never came and the game stayed
#   paused. From $24B5 the handler leaves at once while $D526 is set, without counting the
#   frame ($D525): the game waits in its frame wait ($0338) with interrupts on until the
#   next Pause clears $D526. The loop's reset button test ($24BB) is gone.
name King's Quest
cart F8D33BC4
hz 60		; No-Intro region USA
vector 20 io
priority
asm 00309 2   ; IM 1 -> IM 2
    im 2
endasm
asm 024B5 15   ; the pause loop $24B5-$24C2 (IN A,($DD) at $24BB): paused, leave without counting the frame
    ld a,($D526)
    or a
    jr nz,$24CB
    jr $24C4
endasm
site 0018E   ; OUT ($BF),A
site 00195   ; OUT ($BF),A
site 0019C   ; OUT ($BE),A
site 001A2   ; OUT ($BF),A
site 001A9   ; OUT ($BF),A
site 001B3   ; OUT ($BF),A
site 001BA   ; OUT ($BF),A
site 001E0   ; OUT (C),A
site 001F2   ; OUT ($BF),A
site 001F9   ; OUT ($BF),A
site 00201   ; OUT ($BE),A
site 00229   ; OUT ($BF),A
site 0022D   ; OUT ($BF),A
site 00233   ; OUT (C),A
site 00247   ; OUT ($BF),A
site 0024E   ; OUT ($BF),A
site 00264   ; OUT ($BF),A
site 0026B   ; OUT ($BF),A
site 00272   ; OUT ($BE),A
site 00277   ; OUT ($BE),A
site 002AF   ; OUTI
site 002BA   ; OUT ($BF),A
site 002C1   ; OUT ($BF),A
site 002C8   ; INI
site 002D3   ; OUT ($BF),A
site 002DA   ; OUT ($BF),A
site 002E1   ; IN A,($BE)
site 002E7   ; OUT ($BF),A
site 002EF   ; OUT ($BF),A
site 002F4   ; OUT ($BE),A
site 01770   ; OUT ($BF),A
site 01777   ; OUT ($BF),A
site 01785   ; OUT ($BE),A
site 0178C   ; OUT ($BE),A
site 017A4   ; OUT ($BF),A
site 017AB   ; OUT ($BF),A
site 017C4   ; OUT ($BE),A
site 017CB   ; OUT ($BE),A
site 01813   ; OTIR
site 02419   ; IN A,($DD)
site 02420   ; IN A,($DC)
site 024AE   ; IN A,($BF)
site 0251C   ; OUT ($BF),A
site 02521   ; OUT ($BF),A
site 02526   ; OUT ($BE),A
site 028E6   ; OUT (C),L
site 028EB   ; OUT (C),H
site 028F2   ; IN E,(C)
site 028F7   ; IN D,(C)
site 07CB8   ; OUT ($7F),A
site 07CBF   ; OUT ($7F),A
site 07CC3   ; OUT ($7F),A
site 07CD9   ; OUT ($7F),A
site 07CFA   ; OUT ($7F),A
site 07D01   ; OUT ($7F),A
site 07D08   ; OUT ($7F),A
site 07D2B   ; OUT ($7F),A
site 07D3C   ; OUT ($7F),A
site 07D4C   ; OUT ($7F),A
site 07D8B   ; OUT ($7F),A
site 07D92   ; OUT ($7F),A
site 07D96   ; OUT ($7F),A
site 07D9F   ; OUT ($7F),A
site 07EB4   ; OUT ($7F),A
site 07EC5   ; OUT ($7F),A
site 07EDB   ; OUT ($7F),A
mapldk 0030B   # LD HL,$FFFC; LD (HL),$00
maphl 00311   # LD (HL),$00, HL = $FFFD
maphl 00314   # LD (HL),$01, HL = $FFFE
maphl 00317   # LD (HL),$02, HL = $FFFF
mapst 003D1   ; LD ($FFFF),A
mapst 0046B   ; LD ($FFFF),A
mapst 0104E   ; LD ($FFFF),A
mapst 01107   ; LD ($FFFF),A
mapst 01120   ; LD ($FFFF),A
mapst 01127   ; LD ($FFFF),A
mapst 025BB   ; LD ($FFFF),A
mapst 027F5   ; LD ($FFFF),A
mapst 02D58   ; LD ($FFFF),A
mapst 03129   ; LD ($FFFF),A
mapst 032AD   ; LD ($FFFF),A
mapst 033A9   ; LD ($FFFF),A
mapst 0590C   ; LD ($FFFF),A
mapst 05925   ; LD ($FFFF),A
mapst 05A3A   ; LD ($FFFF),A
mapst 05A71   ; LD ($FFFF),A
mapst 05A7D   ; LD ($FFFF),A
mapst 05A96   ; LD ($FFFF),A
mapst 05A9E   ; LD ($FFFF),A
mapst 05AAB   ; LD ($FFFF),A
mapst 05AB4   ; LD ($FFFF),A
mapst 05AC2   ; LD ($FFFF),A
mapst 05ACA   ; LD ($FFFF),A
mapst 05AD8   ; LD ($FFFF),A
mapst 05AE0   ; LD ($FFFF),A
mapst 05B05   ; LD ($FFFF),A
mapst 05B25   ; LD ($FFFF),A
mapst 05B3F   ; LD ($FFFF),A
mapst 05B5D   ; LD ($FFFF),A
mapst 05BA0   ; LD ($FFFF),A
mapst 0669B   ; LD ($FFFF),A
mapst 066A6   ; LD ($FFFF),A
mapst 0684A   ; LD ($FFFF),A
mapst 06A25   ; LD ($FFFF),A
mapst 06A41   ; LD ($FFFF),A
mapst 06B22   ; LD ($FFFF),A
mapst 06B5D   ; LD ($FFFF),A
mapst 06B8C   ; LD ($FFFF),A
mapst 06D6E   ; LD ($FFFF),A
mapst 073B6   ; LD ($FFFF),A
mapst 07AA6   ; LD ($FFFF),A
mapst 07B5C   ; LD ($FFFF),A
mapst 07B75   ; LD ($FFFF),A
mapst 07BE9   ; LD ($FFFF),A
mapst 07C03   ; LD ($FFFF),A
site 0023C   ; OUT ($BF),A
site 00243   ; OUT ($BF),A
site 00252   ; OUT ($BF),A
site 00259   ; OUT ($BF),A
site 00260   ; OUT ($BE),A
site 00285   ; OUT ($BE),A
site 0029C   ; OUT ($BE),A
site 002A1   ; OUT ($BE),A
site 07EE3   ; OUT ($7F),A

# King's Quest - Quest for the Crown (USA).cht, "Invisibility": RAM $D282 is the Invisibility line of the status screen; held at 1
# the line reads YES
poke "Invisibility"
ar 00D2-8201
endpoke

# King's Quest - Quest for the Crown (USA).cht, "Spell [Protection From Monsters]": RAM $D24A = 1 puts SPELL
# in the inventory
poke "Protection spell"
ar 00D2-4A01
endpoke

# King's Quest - Quest for the Crown (USA).cht, "4-Leafer [Protection From Leprechauns]": RAM $D261 = 1 puts
# 4 LEAFER in the inventory
poke "Four-leaf clover"
ar 00D2-6101
endpoke

# King's Quest - Quest for the Crown (USA).cht, the item codes Dagger to Slingshot ($D24B to $D260, one byte each, 1 = held): all 22
# items are in the inventory
poke "All items"
ar 00D2-4B01
ar 00D2-4C01
ar 00D2-4D01
ar 00D2-4E01
ar 00D2-4F01
ar 00D2-5001
ar 00D2-5101
ar 00D2-5201
ar 00D2-5301
ar 00D2-5401
ar 00D2-5501
ar 00D2-5601
ar 00D2-5701
ar 00D2-5801
ar 00D2-5901
ar 00D2-5A01
ar 00D2-5B01
ar 00D2-5C01
ar 00D2-5D01
ar 00D2-5E01
ar 00D2-5F01
ar 00D2-6001
endpoke
