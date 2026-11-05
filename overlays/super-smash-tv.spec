# Super Smash T.V. (Europe), CRC32 E0B1AFF8, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - RST $08 ($0008-$000F) is $FF filler: it is the io vector.
# - Five JP (HL) dispatchers read a word table at an index doubled and added to the
#   table's address (SLA A; ADD A,lo; LD L,A; LD A,0; ADC A,hi): $2B7D (table $2B85, 11
#   entries), $3812 ($381E, 21), $5817 ($581A, 98), $6A61 ($6AAA, 16) and $A156 in bank 2
#   ($A164, 19). A scan with every table entry as an entry point finds no I/O or mapper
#   site that the spec does not patch.
# - Every call into slot 2 is to bank 2: a breakpoint run showed bank 2 in slot 2 at
#   each call to $8ACF, $8FFC, $9069, $90D4, $9BD6 and $9BFF and at each of the five
#   JP (HL). The game maps banks 3-14 into slot 2 only to read data. A scan with the
#   slot 2 call targets as bank 2 entry points finds no I/O or mapper site that the
#   spec does not patch.
# - $00B0-$02A8 is a development monitor that reads commands through the joypad port.
#   Nothing in the cart names its start: it is unused, and its I/O is not patched. The
#   scanner reaches $021C inside it from a byte pair that $1BB2 stores ($1C, $02), which
#   is object data, not a code address.
# - Data: the IN B,(C) patterns at $17AA3 and $17E63 (bank 5) and the mapper store
#   pattern at $367C7 (bank 13) are in tile graphics.
# - The game takes its interrupts as line interrupts: register 0 is $36 (line interrupts
#   on), register 10 is $C0 and register 1 is $80 or $C0 (frame interrupt off) after
#   the start. On the Master System the line counter of 192 runs out at line 192, once a
#   frame. The runtime schedules no line event for a counter of 192 or more, so the game
#   waited for ever at $19CE. The two register 1 writes ($192E display off, $193F display
#   on) also set the frame interrupt bit: the runtime's frame event is at the end of line
#   192, the line where the game's line interrupt comes.
name Super Smash T.V.
cart E0B1AFF8
hz 50		; No-Intro region Europe
vector 08 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 0192E 3   ; LD HL,$8180 -> register 1 $A0: display off, frame interrupt on
    ld hl,$81A0
endasm
asm 0193F 3   ; LD HL,$81C0 -> register 1 $E0: display on, frame interrupt on
    ld hl,$81E0
endasm
site 00217   ; IN A,($DC)
site 00228   ; IN A,($DC)
site 00243   ; IN A,($DC)
site 0024E   ; IN A,($DC)
site 0025C   ; IN A,($DC)
site 0026C   ; IN A,($DC)
site 00281   ; OUT ($3F),A
site 015DB   ; OUT ($3F),A
site 0160D   ; IN A,($BF)
site 01613   ; IN A,($DD)
site 01653   ; OTIR
site 01665   ; OUTI
site 016BE   ; OUT ($BF),A
site 016C5   ; OUT ($BF),A
site 016CF   ; OUT ($BF),A
site 016D8   ; OUT ($BF),A
site 016E2   ; OUT ($BF),A
site 016EB   ; OUT ($BF),A
site 016F5   ; OUT ($BF),A
site 016FD   ; OUT ($BF),A
site 01704   ; OUT ($BE),A
site 01774   ; OUT ($BE),A
site 017DF   ; OUTI
site 01830   ; OUT ($BF),A
site 0183C   ; OUT ($BF),A
site 01842   ; OUTI
site 0195A   ; OUT ($BE),A
site 019A7   ; OUT ($BE),A
site 019B0   ; OUT ($BE),A
site 01C45   ; OUT ($BE),A
site 01C4D   ; OUT ($BE),A
site 01C55   ; OUT ($BE),A
site 01C5D   ; OUT ($BE),A
site 01F87   ; OUT ($BE),A
site 023F1   ; OUTI
site 0243D   ; OUTI
site 0249E   ; OUTI
site 0254D   ; OUT ($BE),A
site 026D9   ; OUT ($BE),A
site 0271D   ; OUTI
site 0272C   ; OUTI
site 02A26   ; OUTI
site 02B10   ; OUTI
site 02D51   ; OUT ($BE),A
site 02D59   ; OUT ($BE),A
site 03335   ; IN A,($DC)
site 0443A   ; OUT ($BF),A
site 0443F   ; OUT ($BF),A
site 04446   ; OUT ($BE),A
site 0444B   ; OUT ($BE),A
site 05FCE   ; OUT ($BE),A
site 05FD8   ; OUT ($BE),A
site 06025   ; OUT ($BE),A
site 0675E   ; IN A,($BF)
site 06760   ; IN A,($BF)
site 0676C   ; IN A,($BF)
site 069DA   ; IN A,($BE)
site 069E3   ; OUT ($BE),A
site 07222   ; OUT ($BE),A
site 07A2A   ; IN A,($DC)
site 07A34   ; IN A,($DD)
site 07A7D   ; IN A,($DC)
site 093A7   ; OUT ($BE),A
site 0B6E7   ; OUT ($7F),A
site 0B6EB   ; OUT ($7F),A
site 0B6F8   ; OUT ($7F),A
site 0B6FC   ; OUT ($7F),A
site 0B72D   ; OUT ($7F),A
site 0B744   ; OUT ($7F),A
site 0B758   ; OUT ($7F),A
site 0B767   ; OUT ($7F),A
site 0B77E   ; OUT ($7F),A
site 0B792   ; OUT ($7F),A
site 0B7BF   ; OUT ($7F),A
site 0B7D2   ; OUT ($7F),A
site 0B7E9   ; OUT ($7F),A
site 0B7EF   ; OUT ($7F),A
site 0B813   ; OUT ($7F),A
site 0B82A   ; OUT ($7F),A
site 0B83E   ; OUT ($7F),A
site 0B89B   ; OUT ($7F),A
site 0BA0A   ; IN A,($BF)
site 0BA0C   ; IN A,($C1)
site 0BA83   ; OUT ($7F),A
site 0BA88   ; OUT ($7F),A
site 0BA9C   ; OUT ($7F),A
site 0BAAF   ; OUT ($7F),A
site 0BABB   ; OUT ($7F),A
site 0BACE   ; OUT ($7F),A
mapldk 015DD   # LD HL,$FFFC; LD (HL),$80
maphl 015E3   # LD (HL),$00, HL = $FFFD
maphl 015E6   # LD (HL),$01, HL = $FFFE
maphl 015E9   # LD (HL),$02, HL = $FFFF
mapst 01632   ; LD ($FFFF),A
mapst 01639   ; LD ($FFFF),A
mapst 0170C   ; LD ($FFFF),A

# Super Smash T.V. (Europe).cht, "Infinite Lives P1": holds the player 1 life count at 7
poke "Infinite lives"
ar 00C5-1007
endpoke
