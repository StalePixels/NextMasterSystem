# Ayrton Senna's Super Monaco GP II (Europe, Brazil) (En), CRC32 E890331D, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of attract mode
# (900 s, no input) and play (900 s, start script and random input), and these entry points
# added by hand (--entry), each proven by a static path from scanned code:
#   $6544, $6581: the routines that $653A and $656C pass in HL to $4BC2, which stores them in
#     $C07F for the JP (HL) at $4BE5.
#   $662D, $66D0, $682B, $70DE: the routines that $6619, $66C0, $681D and $70B3 pass in HL to
#     $4B77, which stores them in $C054 for the JP (HL) at $49C4.
#   $6B3E, $6B50: entries 1 and 2 of the table at $679A, which $6791 passes in HL to the
#     dispatcher $6622 (RST $10 by $C05E). They reach the digit writers $6C31 and $6C7D in
#     bank 1, whose I/O ($6C37-$6CA4) no recording ran.
# Byte scan I/O patterns judged code and patched (no recording ran them, and no call, jump or
# word naming them was found in code): the VRAM writers $04FA, $0505 and $050C and the VRAM
# write queue $0515 in bank 0.
# Byte scan I/O patterns judged not code (verdicts in data/scan-verdicts.tsv): the hits in
# banks 5-21 (graphics and tables) and bank 1 $5AA9 (the operand of LD HL,($C0D3) at $5AA8).
# The code that the scan decodes at bank 0 $2266-$2520 is data: the fifth word of the
# $C05E state table at $6627 points into graphics.
name Ayrton Senna's Super Monaco GP II
cart E890331D
hz 50		; No-Intro regions Europe, Brazil
# The race sets H scroll on every line of the road (48 lines, from a line interrupt each),
# and H = 0 for the HUD below it. A rastercode routine builds the per-line table; in those
# frames the game gets no line events. Only the line interrupt handler uses the event
# counter $C07B.
rastercode super-monaco-gp-ii-raster.asm
# No priority: the reference logs wrote no name table cell with the priority bit.
# No free RST vector: the JP at $0000 becomes the vector, the game starts at its target.
vector 00 io
start 00DE
asm 000DE 2   ; IM 1 -> IM 2
    im 2
endasm
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0004F   ; OUT ($BF),A
site 00053   ; OUT ($BF),A
site 00098   ; OUT ($BF),A
site 0009C   ; OUT ($BF),A
site 000A5   ; OUT ($BF),A
site 000A9   ; OUT ($BF),A
site 000B3   ; OUT ($BF),A
site 000B7   ; OUT ($BF),A
site 000C1   ; OUT ($BF),A
site 000C5   ; OUT ($BF),A
site 000CC   ; OUT ($BF),A
site 000D0   ; OUT ($BF),A
site 000D4   ; OUT ($BF),A
site 000D8   ; OUT ($BF),A
site 001EF   ; OUT ($BE),A
site 00234   ; OTIR
site 00252   ; OUT ($3F),A
site 00254   ; IN A,($DD)
site 0025E   ; OUT ($3F),A
site 00260   ; IN A,($DD)
site 00269   ; OUT ($3F),A
site 00293   ; OUT ($BF),A
site 00297   ; OUT ($BF),A
site 0029C   ; OUT ($BF),A
site 002A0   ; OUT ($BF),A
site 002A5   ; OUT ($BF),A
site 002A9   ; OUT ($BF),A
site 002DC   ; IN A,($DD)
site 0030A   ; IN A,($BF)
site 0030C   ; IN A,($BF)
site 00318   ; IN A,($BF)
site 00439   ; OUT ($BE),A
site 00448   ; OUT ($BF),A
site 0044C   ; OUT ($BF),A
site 00453   ; OUTI
site 00455   ; OUTI
site 00457   ; OUTI
site 00459   ; OUTI
site 0045B   ; OUTI
site 0045D   ; OUTI
site 0045F   ; OUTI
site 00461   ; OUTI
site 00463   ; OUTI
site 00465   ; OUTI
site 00467   ; OUTI
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
site 004D2   ; OUTI
site 004E4   ; OUTI
site 004E6   ; OUTI
site 004EF   ; OUT ($DE),A
site 004F1   ; IN A,($DC)
site 0054D   ; OUT ($BE),A
site 00551   ; OUT ($BE),A
site 005BE   ; OUT (C),A
site 00639   ; OUT ($BF),A
site 0063C   ; OUT ($BF),A
site 00641   ; OUT ($BE),A
site 00647   ; OUT ($BE),A
site 006B3   ; OUTI
site 00702   ; OUT ($BF),A
site 00705   ; OUT ($BF),A
site 00722   ; OUT ($BE),A
site 00727   ; OUT ($BE),A
site 0077F   ; OUT ($BF),A
site 00784   ; OUT ($BF),A
site 00789   ; OUT ($BE),A
site 0078D   ; OUT ($BE),A
site 0085E   ; OUTI
site 00865   ; OUT (C),A
site 008B4   ; INI
site 008B8   ; INI
site 0091C   ; OUT (C),L
site 00920   ; OUT (C),H
site 00972   ; OUTI
site 00974   ; OUTI
site 00976   ; OUTI
site 00978   ; OUTI
site 0097A   ; OUTI
site 0097C   ; OUTI
site 0097E   ; OUTI
site 00980   ; OUTI
site 00982   ; OUTI
site 00984   ; OUTI
site 00986   ; OUTI
site 00988   ; OUTI
site 0098A   ; OUTI
site 0098C   ; OUTI
site 0098E   ; OUTI
site 00990   ; OUTI
site 00992   ; OUTI
site 00994   ; OUTI
site 00996   ; OUTI
site 00998   ; OUTI
site 0099A   ; OUTI
site 0099C   ; OUTI
site 0099E   ; OUTI
site 009A0   ; OUTI
site 009A2   ; OUTI
site 009A4   ; OUTI
site 009A6   ; OUTI
site 009A8   ; OUTI
site 009AA   ; OUTI
site 009AC   ; OUTI
site 009AE   ; OUTI
site 009B0   ; OUTI
site 009B2   ; OUTI
site 009B4   ; OUTI
site 009B6   ; OUTI
site 009B8   ; OUTI
site 009BA   ; OUTI
site 009BC   ; OUTI
site 009BE   ; OUTI
site 009C0   ; OUTI
site 009C2   ; OUTI
site 009C4   ; OUTI
site 009C6   ; OUTI
site 009C8   ; OUTI
site 009CA   ; OUTI
site 009CC   ; OUTI
site 009CE   ; OUTI
site 009D0   ; OUTI
site 009D2   ; OUTI
site 009D4   ; OUTI
site 009D6   ; OUTI
site 009D8   ; OUTI
site 009DA   ; OUTI
site 009DC   ; OUTI
site 009DE   ; OUTI
site 009E0   ; OUTI
site 009E2   ; OUTI
site 009E4   ; OUTI
site 009E6   ; OUTI
site 009E8   ; OUTI
site 009EA   ; OUTI
site 009EC   ; OUTI
site 009EE   ; OUTI
site 009F0   ; OUTI
site 009F2   ; OUTI
site 009F4   ; OUTI
site 009F6   ; OUTI
site 009F8   ; OUTI
site 009FA   ; OUTI
site 009FC   ; OUTI
site 009FE   ; OUTI
site 00A00   ; OUTI
site 00A02   ; OUTI
site 00A04   ; OUTI
site 00A06   ; OUTI
site 00A08   ; OUTI
site 00A0A   ; OUTI
site 00A0C   ; OUTI
site 00A0E   ; OUTI
site 00A10   ; OUTI
site 00A12   ; OUTI
site 00A14   ; OUTI
site 00A16   ; OUTI
site 00A18   ; OUTI
site 00A1A   ; OUTI
site 00A1C   ; OUTI
site 00A1E   ; OUTI
site 00A20   ; OUTI
site 00A22   ; OUTI
site 00A24   ; OUTI
site 00A26   ; OUTI
site 00A28   ; OUTI
site 00A2A   ; OUTI
site 00A2C   ; OUTI
site 00A2E   ; OUTI
site 00A30   ; OUTI
site 00A32   ; OUTI
site 00A34   ; OUTI
site 00A36   ; OUTI
site 00A38   ; OUTI
site 00A3A   ; OUTI
site 00A3C   ; OUTI
site 00A3E   ; OUTI
site 00A40   ; OUTI
site 00A42   ; OUTI
site 00A44   ; OUTI
site 00A46   ; OUTI
site 00A48   ; OUTI
site 00A4A   ; OUTI
site 00A4C   ; OUTI
site 00A4E   ; OUTI
site 00A50   ; OUTI
site 00A52   ; OUTI
site 00A54   ; OUTI
site 00A56   ; OUTI
site 00A58   ; OUTI
site 00A5A   ; OUTI
site 00A5C   ; OUTI
site 00A5E   ; OUTI
site 00A60   ; OUTI
site 00A62   ; OUTI
site 00A64   ; OUTI
site 00A66   ; OUTI
site 00A68   ; OUTI
site 00A6A   ; OUTI
site 00A6C   ; OUTI
site 00A6E   ; OUTI
site 00A70   ; OUTI
site 02E10   ; OUT ($BE),A
site 02E13   ; OUT ($BE),A
site 06C37   ; OUT (C),E
site 06C39   ; OUT (C),D
site 06C5C   ; OUT ($BE),A
site 06C62   ; OUT ($BE),A
site 06C6A   ; IN A,($BE)
site 06C6E   ; IN A,($BE)
site 06C81   ; OUT (C),E
site 06C83   ; OUT (C),D
site 06C90   ; OUTI
site 06C92   ; OUTI
site 06C9B   ; OUT (C),L
site 06C9D   ; OUT (C),H
site 06CA2   ; OUTI
site 06CA4   ; OUTI
site 07CB4   ; OUT ($BE),A
site 07CB8   ; OUT ($BE),A
site 7C1C4   ; OUT ($7F),A
site 7C3B0   ; OTIR
site 7C4EA   ; OUT ($7F),A
site 7C4F4   ; OUT ($7F),A
site 7C511   ; OUT ($7F),A
site 7C615   ; OUT ($7F),A
site 7C6A3   ; OUT ($7F),A
site 7C71E   ; OUT ($7F),A
site 7C72E   ; OUT ($7F),A
site 7C794   ; OUT ($7F),A
site 7C7B1   ; OUT ($7F),A
site 7C907   ; OUT ($7F),A
site 7C90B   ; OUT ($7F),A
site 7C931   ; OUT ($7F),A
mapst 00033   ; LD ($FFFF),A
mapst 000E5   ; LD ($FFFC),A
mapst 000E9   ; LD ($FFFD),A
mapst 000EE   ; LD ($FFFE),A
mapst 002D2   ; LD ($FFFF),A
mapst 002E6   ; LD ($FFFF),A
mapst 0094C   ; LD ($FFFF),A
# Byte scan I/O patterns judged code (see the head of the file).
site 004FF   ; OUT ($BE),A
site 00506   ; OUT ($BE),A
site 0050F   ; OUT ($BE),A
site 00537   ; OUT ($BE),A
site 0053D   ; OUT ($BE),A

# The end of a race ($7067: $C03C = 0, register 0 = $16, line interrupts stay on). On the
# SMS the race's last line event (K = $30) leaves register 10 = $FF, so the screens after it
# (the World Championship result list, the password screen) get no line events. In the race
# the rastercode table takes the place of the line events, so that write never comes, and
# register 10 is left at $1F or 0: the line handler then sets H on every line from the old
# road table, and the result list shows in shifted rows. The cave in the unused $FF bytes
# at $7F80 (bank 1, as $7067) writes register 10 = $FF there, the state the SMS reaches.
label raceend 07F80
asm 07074 6    ; LD ($C03C),A : LD ($C085),A
    ld ($C03C),a
    call raceend
endasm
asm 07F80 8    ; unused $FF bytes: raceend
    ld ($C085),a
    ld de,$8AFF	; register 10 = $FF
    rst $08
    ret
endasm

# Ayrton Senna's Super Monaco GP II (Europe, Brazil).cht, "Always End In 1st Place": RAM
# $C517 held at $A3. The player's car runs at about 325 km/h and the race ends in first place
poke "Win the race"
ar 00C5-17A3
endpoke

# Ayrton Senna's Super Monaco GP II (Europe, Brazil).cht, "You Never Crash": RAM $C529 held at
# $81. The car stays on the road and at full speed instead of leaving it
poke "Stay on track"
ar 00C5-2981
endpoke

# Ayrton Senna's Super Monaco GP II (Europe, Brazil).cht, "Low Timer - One's Seconds",
# "Low Timer - Ten's Seconds Digits" and "Low Timer - Minute's Digits": RAM $C34A, $C34B and
# $C34C, the digits of the race time, held at 0. The race time on screen and in the result
# list stays near 0'00"
poke "Low race time"
ar 00C3-4A00
ar 00C3-4B00
ar 00C3-4C00
endpoke

# Ayrton Senna's Super Monaco GP II (Europe, Brazil).cht, "Freeze Lap Timer" (Action Replay):
# RAM $C33D held at 0. The lap time stays at 0'00"0x
poke "Freeze lap time"
ar 00C3-3D00
endpoke

# Ayrton Senna's Super Monaco GP II (Europe, Brazil).cht, "Freeze Lap Timer" (Game Genie):
# ROM $0AA0 becomes $7E. The race time and the lap time both stay at 0'00"00
poke "Freeze all timers"
gg 7EA-A0F-3B7
endpoke
