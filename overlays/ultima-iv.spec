# Ultima IV - Quest of the Avatar (Europe, Brazil) (En), CRC32 B52D60C8, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), and the entry points below, then decided by hand.
#
# Decisions:
# - No free RST vector, so $0000-$0002 (DI; IM 1) is the io vector and the game starts
#   at $0003.
# - Entry points for the scan, besides the logs: the bank 1 routines that bank 3 and
#   bank 0 call in slot 1 ($7E0C $7E5A $7E5D $7E84 $7E87 $7EED $7EF0 $7EF3 $7F0B $48E1
#   $48EB $40D9 $4205 $5627 $6C97 $6DC0), the VDP routines in bank 1 that no path or
#   recording reached ($4117 $4173 $41A9 $41D2 $4EF1 $4F8D $5247 $5290 $5659 $7CB3 $7CB8
#   $7CD3), the tasks in bank 3 ($B039 $B4FB $B55E $B709) and the VRAM read at $0209.
#   The game runs most of its code as tasks: $0B01 jumps to a task's address and slot 2
#   bank from its record in RAM ($C300 on, 10 records of $30 bytes).
# - Bank 0 has no unused bytes, and slot 1 holds bank 4 during the copy at $0F00, so the
#   code that does not fit in place goes into page 0:
#   - The cart RAM switch $0C2D (on) and $0C35 (off) does SET 3 or RES 3 on $FFFC
#     through HL. Each becomes a far call to cram_on or cram_off.
#   - The frame handler at $02D2 saves $FFFC and the slot 2 bank, then writes $80 to
#     $FFFC through HL. The far call to irq_fffc does both; the PUSH DE stays in place.
#   - The decoder at $116B reads bytes of bank $10 through $11AC, which sets slot 2 with
#     LD (HL),C and puts it back with LD (HL),B (HL = $FFFF). Its middle becomes a far
#     call to peek10.
name Ultima IV
cart B52D60C8
hz 50		; No-Intro region Europe, Brazil
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
asm 00CB5 2   ; IM 1 -> IM 2
    im 2
endasm
site 00039   ; IN A,($BF)
site 00071   ; OUT ($BF),A
site 00074   ; OUT ($BF),A
site 0007A   ; OUT ($BF),A
site 0007F   ; OUT ($BF),A
site 000A2   ; OTIR
site 000A9   ; OUT ($3F),A
site 000AB   ; IN A,($DD)
site 000B5   ; OUT ($3F),A
site 000B7   ; IN A,($DD)
site 000BF   ; OUT ($3F),A
site 000DC   ; IN A,($BF)
site 000E2   ; IN A,($BF)
site 000E9   ; IN A,($BF)
site 00118   ; OUT ($3E),A
site 00120   ; OUT ($F2),A
site 00123   ; IN A,($F2)
site 00135   ; OUT ($F2),A
site 0013D   ; OUT ($3E),A
site 0014E   ; IN A,($BF)
site 00163   ; OUTI
site 00165   ; OUT ($BF),A
site 0016C   ; OUT ($BF),A
site 00170   ; OUT ($BF),A
site 00178   ; OUT ($BE),A
site 00180   ; OUT ($BF),A
site 00184   ; OUT ($BF),A
site 00188   ; OUT ($BE),A
site 001B3   ; OUT ($BF),A
site 001B8   ; OUT ($BF),A
site 0020D   ; IN A,($BE)
site 00216   ; OUT ($BE),A
site 0021F   ; OUT (C),L
site 0022F   ; OUT ($BE),A
site 00235   ; OUT ($BE),A
site 00243   ; INI
otir 00250   ; OUTI
site 002A0   ; IN A,($BE)
site 002A5   ; IN A,($BE)
site 002AA   ; OUT ($BE),A
site 002B2   ; OUT ($BE),A
site 002E5   ; IN A,($DD)
site 0030A   ; OUT ($BF),A
site 0030E   ; OUT ($BF),A
site 00325   ; OUT ($BF),A
site 00329   ; OUT ($BF),A
site 0032C   ; OUT ($BF),A
site 00330   ; OUT ($BF),A
site 00334   ; OUT ($BF),A
site 00338   ; OUT ($BF),A
site 00342   ; OUT ($BF),A
site 00346   ; OUT ($BF),A
site 0036A   ; OUT ($BF),A
site 0036E   ; OUT ($BF),A
site 0038D   ; OUT ($BF),A
site 00390   ; OUT ($BF),A
otir 0039E   ; OUTI
site 003C5   ; OUT (C),E
site 003C7   ; OUT (C),D
otir 003CB   ; OUTI
site 0040C   ; IN A,($7E)
site 00412   ; OUT ($BF),A
site 00416   ; OUT ($BF),A
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
site 00506   ; OUTI
site 00508   ; OUTI
site 0050A   ; OUTI
site 0050C   ; OUTI
site 0050E   ; OUTI
site 00510   ; OUTI
site 00512   ; OUTI
site 00514   ; OUTI
site 00516   ; OUTI
site 00518   ; OUTI
site 0051A   ; OUTI
site 0051C   ; OUTI
site 0051E   ; OUTI
site 00520   ; OUTI
site 00522   ; OUTI
site 00524   ; OUTI
site 00526   ; OUTI
site 00528   ; OUTI
site 0052A   ; OUTI
site 0052C   ; OUTI
site 0052E   ; OUTI
site 00530   ; OUTI
site 00532   ; OUTI
site 00534   ; OUTI
site 00536   ; OUTI
site 00538   ; OUTI
site 0053A   ; OUTI
site 0053C   ; OUTI
site 0053E   ; OUTI
site 00540   ; OUTI
site 00542   ; OUTI
site 00544   ; OUTI
site 00546   ; OUTI
site 00548   ; OUTI
site 0054A   ; OUTI
site 0054C   ; OUTI
site 0054E   ; OUTI
site 00550   ; OUTI
site 00552   ; OUTI
site 00554   ; OUTI
site 00556   ; OUTI
site 00558   ; OUTI
site 0055A   ; OUTI
site 0055C   ; OUTI
site 0055E   ; OUTI
site 00560   ; OUTI
site 00562   ; OUTI
site 00564   ; OUTI
site 00566   ; OUTI
site 00568   ; OUTI
site 0056A   ; OUTI
site 0056C   ; OUTI
site 0056E   ; OUTI
site 00570   ; OUTI
site 00572   ; OUTI
site 00574   ; OUTI
site 00576   ; OUTI
site 00578   ; OUTI
site 0057A   ; OUTI
site 0057C   ; OUTI
site 0057E   ; OUTI
site 00580   ; OUTI
site 00582   ; OUTI
site 00584   ; OUTI
site 00586   ; OUTI
site 00588   ; OUTI
site 0058A   ; OUTI
site 0058C   ; OUTI
site 0058E   ; OUTI
site 00590   ; OUTI
site 00592   ; OUTI
site 00594   ; OUTI
site 00596   ; OUTI
site 00598   ; OUTI
site 0059A   ; OUTI
site 0059C   ; OUTI
site 0059E   ; OUTI
site 005A0   ; OUTI
site 005A2   ; OUTI
site 005A4   ; OUTI
site 005A6   ; OUTI
site 005A8   ; OUTI
site 005AA   ; OUTI
site 005AC   ; OUTI
site 005AE   ; OUTI
site 005B0   ; OUTI
site 005B2   ; OUTI
site 005B4   ; OUTI
site 005B6   ; OUTI
site 005B8   ; OUTI
site 005BA   ; OUTI
site 005BC   ; OUTI
site 005BE   ; OUTI
site 005C0   ; OUTI
site 005C2   ; OUTI
site 005C4   ; OUTI
site 0063F   ; OUT ($DF),A
site 00643   ; OUT ($DE),A
site 00646   ; IN A,($DC)
site 0064C   ; IN A,($DC)
site 0064F   ; IN A,($DD)
site 0076A   ; OUTI
site 0076C   ; IN A,($BE)
site 0076E   ; IN A,($BE)
site 00770   ; IN A,($BE)
site 0077A   ; OUT ($BE),A
site 0077C   ; IN A,($BE)
site 0077E   ; IN A,($BE)
site 00780   ; IN A,($BE)
site 007A9   ; OUTI
site 007B6   ; OUT ($BE),A
site 007C1   ; IN A,($BE)
site 007C6   ; IN A,($BE)
site 007CB   ; IN A,($BE)
site 01C39   ; OUTI
site 01C3B   ; OUTI
site 01C5C   ; OUT ($BE),A
site 01C63   ; OUT ($BE),A
site 01C6A   ; OUT ($BE),A
site 01C71   ; OUT ($BE),A
site 01CA6   ; OUTI
site 01CA8   ; OUTI
site 01CC7   ; OUTI
site 01CCC   ; OUTI
site 01CD1   ; OUTI
site 01CD6   ; OUTI
site 01D16   ; OUTI
site 01D18   ; OUTI
site 01D22   ; IN A,($BE)
site 01D28   ; IN A,($BE)
site 01D2E   ; IN A,($BE)
site 01D34   ; IN A,($BE)
site 01D3E   ; OUTI
site 01D40   ; OUTI
otir 01D4C   ; OUTI
site 01DA1   ; OUTI
site 01DA3   ; OUTI
site 01DC5   ; OUTI
site 01DC7   ; OUTI
site 01DD3   ; OUT ($BE),A
site 01DD9   ; OUT ($BE),A
site 01DDF   ; OUT ($BE),A
site 01DE5   ; OUT ($BE),A
site 01DED   ; OUTI
site 01DEF   ; OUTI
site 01DF7   ; OUTI
site 01DFC   ; OUTI
site 01E01   ; OUTI
site 01E06   ; OUTI
site 01E3C   ; OUTI
site 01E3E   ; OUTI
site 01E52   ; IN A,($BE)
site 01E59   ; IN A,($BE)
site 01E60   ; IN A,($BE)
site 01E67   ; IN A,($BE)
site 01E73   ; OUTI
site 01E75   ; OUTI
site 01E92   ; OUT ($BE),A
site 01E99   ; OUT ($BE),A
site 01EA0   ; OUT ($BE),A
site 01EA7   ; OUT ($BE),A
site 01EB0   ; OUTI
site 01EB2   ; OUTI
site 01EBE   ; OUT ($BE),A
site 01EC5   ; OUT ($BE),A
site 01ECC   ; OUT ($BE),A
site 01ED3   ; OUT ($BE),A
site 01EDE   ; OUTI
site 01EE0   ; OUTI
site 01F02   ; IN A,($BE)
site 01F09   ; IN A,($BE)
site 01F10   ; IN A,($BE)
site 01F17   ; IN A,($BE)
site 01F22   ; OUTI
site 01F24   ; OUTI
otir 01F2F   ; OUTI
site 01F36   ; OUTI
site 01F38   ; OUTI
site 01F40   ; OUTI
site 01F45   ; OUTI
site 01F4A   ; OUTI
site 01F4F   ; OUTI
site 01FBB   ; OUTI
site 01FBD   ; OUTI
site 01FDB   ; OUT ($BE),A
site 01FE2   ; OUT ($BE),A
site 01FE9   ; OUT ($BE),A
site 01FF0   ; OUT ($BE),A
site 01FF8   ; OUTI
site 01FFA   ; OUTI
site 0200E   ; OUT ($BE),A
site 02019   ; OUT ($BE),A
site 02024   ; OUT ($BE),A
site 0202F   ; OUT ($BE),A
site 02039   ; OUTI
site 0203B   ; OUTI
site 0205A   ; OUTI
site 0205F   ; OUTI
site 02064   ; OUTI
site 02069   ; OUTI
site 02070   ; OUTI
site 02072   ; OUTI
site 0207E   ; OUT ($BE),A
site 02084   ; OUT ($BE),A
site 0208A   ; OUT ($BE),A
site 02090   ; OUT ($BE),A
otir 02E64   ; OUTI
site 02EFD   ; INI
site 02F0B   ; INI
site 02F21   ; OUT ($BE),A
site 02F33   ; OUT ($BE),A
site 02F3F   ; OUT ($BE),A
site 02F44   ; OUT ($BE),A
otir 02F5E   ; OUTI
site 02FBA   ; OUT ($BE),A
site 02FC0   ; OUT ($BE),A
site 02FC6   ; OUT ($BE),A
site 02FCB   ; OUT ($BE),A
site 02FEB   ; OUTI
site 02FED   ; OUT ($BE),A
site 02FEF   ; OUT ($BE),A
site 02FF1   ; OUT ($BE),A
site 032DD   ; OUT ($BE),A
site 032E2   ; OUT ($BE),A
site 032E7   ; OUT ($BE),A
site 032EC   ; IN A,($BE)
otir 03320   ; OUTI
site 0349B   ; OUT ($BE),A
site 034A0   ; OUTI
site 034A5   ; OUT ($BE),A
site 034AA   ; OUT ($BE),A
site 04128   ; INI
otir 0415C   ; OUTI
site 04184   ; INI
otir 0418E   ; OUTI
site 041D9   ; IN A,($BE)
otir 041E7   ; OUTI
site 04F36   ; OUT (C),L
site 04F38   ; OUT (C),H
site 04F48   ; IN A,($BE)
site 04F53   ; IN A,($BE)
site 04F5E   ; IN A,($BE)
site 04F69   ; IN A,($BE)
site 04F77   ; OUT (C),L
site 04F79   ; OUT (C),H
otir 04F83   ; OUTI
otir 05008   ; OUTI
site 0502E   ; OUT ($BE),A
otir 050B9   ; OUTI
site 050DF   ; OUT ($BE),A
otir 05270   ; OUTI
site 052CC   ; OUT ($BE),A
site 052D1   ; OUT ($BE),A
site 052D6   ; OUT ($BE),A
site 052DB   ; OUT ($BE),A
site 05477   ; OUT ($BF),A
site 0547C   ; OUT ($BF),A
site 05483   ; OUT ($BE),A
site 0548A   ; OUT ($BE),A
site 056B9   ; INI
site 056C7   ; INI
site 056DD   ; OUT ($BE),A
site 056EF   ; OUT ($BE),A
site 056FB   ; OUT ($BE),A
site 05700   ; OUT ($BE),A
otir 05719   ; OUTI
site 07CC3   ; OUT ($BE),A
site 07CC9   ; OUT ($BE),A
site 0CB54   ; INI
site 0CB68   ; OUT ($BE),A
site 0F04F   ; OUT ($BE),A
site 0F054   ; OUT ($BE),A
site 0F059   ; OUT ($BE),A
site 0F05E   ; OUT ($BE),A
otir 0F06C   ; OUTI
site 0F516   ; IN A,($BE)
otir 0F525   ; OUTI
site 0F576   ; OUT ($BE),A
site 0F57B   ; OUT ($BE),A
site 0F580   ; OUT ($BE),A
site 0F585   ; OUT ($BE),A
otir 0F59E   ; OUTI
site 0F719   ; IN A,($BE)
otir 0F728   ; OUTI
otir 0F739   ; OUTI
site 7C16A   ; OUT ($F0),A
site 7C16D   ; OUT ($F1),A
site 7C196   ; OUT ($F0),A
site 7C19E   ; OUT ($F1),A
site 7C1AE   ; OUT ($F0),A
site 7C1B1   ; OUT ($F1),A
site 7C1CA   ; OUT ($F1),A
site 7C1DE   ; OUT ($F0),A
site 7C1E5   ; OUT ($F1),A
site 7C1EC   ; OUT ($F1),A
site 7C1FF   ; OUT ($F0),A
site 7C202   ; OUT ($F1),A
site 7C214   ; OUT ($F0),A
site 7C219   ; OUT ($F1),A
site 7C22B   ; OUT ($F1),A
site 7C23F   ; OUT ($F0),A
site 7C242   ; OUT ($F1),A
site 7C255   ; OUT ($7F),A
site 7C25B   ; OUT ($7F),A
site 7C267   ; OUT ($7F),A
site 7C284   ; OUT ($7F),A
site 7C28D   ; OUT ($7F),A
site 7CA62   ; OUT (C),A
site 7CA66   ; OUT (C),A
site 7CA76   ; OUT ($F0),A
site 7CA7A   ; OUT ($F1),A
site 7CA95   ; OUT ($F0),A
site 7CA98   ; OUT ($F1),A
site 7CAB4   ; OUT ($F2),A
mapldk 00042   # LD HL,$FFFC; LD (HL),$80
maphl 00048   # LD (HL),$00, HL = $FFFD
maphl 0004B   # LD (HL),$01, HL = $FFFE
maphl 0004E   # LD (HL),$02, HL = $FFFF
mapst 00386   ; LD ($FFFF),A
mapst 003EC   ; LD ($FFFF),A
mapst 003F4   ; LD ($FFFC),A
mapst 003F8   ; LD ($FFFF),A
mapst 005CD   ; LD ($FFFF),A
mapst 005DF   ; LD ($FFFF),A
mapst 005FA   ; LD ($FFFF),A
mapst 0060B   ; LD ($FFFF),A
mapst 0062F   ; LD ($FFFF),A
mapst 007DA   ; LD ($FFFF),A
mapst 007E4   ; LD ($FFFF),A
mapst 00B12   ; LD ($FFFF),A
mapst 00D02   ; LD ($FFFF),A
mapst 00D2E   ; LD ($FFFF),A
mapst 00D48   ; LD ($FFFF),A
mapsthl 00F00   ; LD ($FFFE),HL
mapsthl 00F31   ; LD ($FFFE),HL
mapsthl 01AE5   ; LD ($FFFE),HL
mapsthl 01BAF   ; LD ($FFFE),HL
mapst 01BBF   ; LD ($FFFF),A
mapst 01CEF   ; LD ($FFFF),A
mapst 01F62   ; LD ($FFFF),A
mapst 020A5   ; LD ($FFFF),A
mapst 020EF   ; LD ($FFFF),A
mapst 020F5   ; LD ($FFFF),A
mapst 02111   ; LD ($FFFF),A
mapst 02132   ; LD ($FFFE),A
mapst 0217C   ; LD ($FFFE),A
mapst 02182   ; LD ($FFFE),A
mapst 0219E   ; LD ($FFFE),A
mapst 021BF   ; LD ($FFFF),A
mapst 02209   ; LD ($FFFF),A
mapst 0220F   ; LD ($FFFF),A
mapst 0222B   ; LD ($FFFF),A
mapst 0224C   ; LD ($FFFE),A
mapst 02296   ; LD ($FFFE),A
mapst 0229C   ; LD ($FFFE),A
mapst 022B8   ; LD ($FFFE),A
mapst 05684   ; LD ($FFFF),A
mapst 05722   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 005E9   # LD ($FFFF),A; after LD A,$1F; 32 bytes of valid code before it
mapst 00619   # LD ($FFFF),A; after LD A,$1F; 32 bytes of valid code before it
# Cart RAM on and off ($0C2D, $0C35: PUSH HL; LD HL,$FFFC; SET or RES 3,(HL); POP HL; RET).
asm 00C2D 8
    rst $00
    db far_io, pg_cram_on, ent_cram_on
    ret
endasm
asm 00C35 8
    rst $00
    db far_io, pg_cram_off, ent_cram_off
    ret
endasm
# Frame handler: LD HL,$FFFC; LD E,(HL); LD A,($DFFF); LD D,A; PUSH DE; LD (HL),$80.
asm 002D2 11
    rst $00
    db far_io, pg_irq_fffc, ent_irq_fffc
    push de
endasm
# Decoder byte read: LD (HL),C; LD E,A; LD A,(DE); LD (HL),B; EXX; RET.
asm 011AE 6
    rst $00
    db far_io, pg_peek10, ent_peek10
    exx
    ret
endasm
page 0 cram_on cram_off irq_fffc peek10
; cram_on, cram_off: set or clear bit 3 of $FFFC (cart RAM in slot 2) through the
; runtime's mapper code. A, F and every other register kept, as SET and RES leave them.
cram_on:
    ld (sv_a),a
    ld a,($FFFC)
    set 3,a
    rst $00
    db $10, 0           ; LD ($FFFC),A
    ld a,(sv_a)
    ret
cram_off:
    ld (sv_a),a
    ld a,($FFFC)
    res 3,a
    rst $00
    db $10, 0           ; LD ($FFFC),A
    ld a,(sv_a)
    ret
; irq_fffc: E = $FFFC, D = the slot 2 bank ($DFFF), then $FFFC = $80.
; HL = $FFFC and A = D, as the game's code leaves them.
irq_fffc:
    ld a,($FFFC)
    ld e,a
    ld a,$80
    rst $00
    db $10, 0           ; LD ($FFFC),A
    ld a,($DFFF)
    ld d,a
    ld hl,$FFFC
    ret
; peek10: in the alternate set, B = the old slot 2 bank, C = the bank to read,
; D = the high byte and A = the low byte of the address, HL = $FFFF. Sets slot 2 to C,
; reads the byte into A, sets slot 2 back to B. E = the low byte, HL = $FFFF, as the
; game's code leaves them; F kept.
peek10:
    ld e,a
    ld a,c
    rst $00
    db $13, 0           ; LD ($FFFF),A
    ld a,(de)
    ld l,a
    ld a,b
    rst $00
    db $13, 0           ; LD ($FFFF),A
    ld a,l
    ld l,$FF
    ret
sv_a:
    db 0
endpage

# Ultima IV - Quest of the Avatar (Europe, Brazil).cht, "Infinite Food": RAM $C907-$C908 is the party's food, held at 9999
poke "Infinite food"
ar 00C9-070F
ar 00C9-0827
endpoke

# Ultima IV - Quest of the Avatar (Europe, Brazil).cht, "Infinite Gold": RAM $C909-$C90A is the party's gold, held at 9999
poke "Infinite gold"
ar 00C9-090F
ar 00C9-0A27
endpoke

# Ultima IV - Quest of the Avatar (Europe, Brazil).cht, "Character Slot 1 Has 800 HP/HP Is Infinite": RAM $C751-$C752 is the Avatar's hit points, held at 800
poke "Infinite health"
ar 00C7-5120
ar 00C7-5203
endpoke

# Ultima IV - Quest of the Avatar (Europe, Brazil).cht, "Character Slot 1 Has 99 MP/MP Is Infinite": RAM $C75A is the Avatar's magic points, held at 99
poke "Infinite magic"
ar 00C7-5A63
endpoke

# Ultima IV - Quest of the Avatar (Europe, Brazil).cht, "Start With/Have All Quest Items": RAM $C951-$C952 are the quest item flags (Bell, Book, Candle, Keys, Horn, Wheel, Skull)
poke "All quest items"
ar 00C9-51FF
ar 00C9-52FF
endpoke

# Ultima IV - Quest of the Avatar (Europe, Brazil).cht, "Start With/Have All Stones": RAM $C955 is the stone flags
poke "All stones"
ar 00C9-55FF
endpoke

# Ultima IV - Quest of the Avatar (Europe, Brazil).cht, "Start With/Have Cloth armor" to "Start With/Have Mystic Robe": RAM $C918-$C91E are the armour counts, held at 99
poke "All armour"
ar 00C9-1863
ar 00C9-1963
ar 00C9-1A63
ar 00C9-1B63
ar 00C9-1C63
ar 00C9-1D63
ar 00C9-1E63
endpoke

# Ultima IV - Quest of the Avatar (Europe, Brazil).cht, "Start With/Have Staff" to "Start With/Have Mystic Sword": RAM $C920-$C92E are the weapon counts, held at 99
poke "All weapons"
ar 00C9-2063
ar 00C9-2163
ar 00C9-2263
ar 00C9-2363
ar 00C9-2463
ar 00C9-2563
ar 00C9-2663
ar 00C9-2763
ar 00C9-2863
ar 00C9-2963
ar 00C9-2A63
ar 00C9-2B63
ar 00C9-2C63
ar 00C9-2D63
ar 00C9-2E63
endpoke
