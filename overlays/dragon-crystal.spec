# Dragon Crystal (Europe, Brazil) (En), CRC32 9549FCE4, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input), then decided by hand.
#
# Decisions:
# - No free RST vector: the JP $0081 at $0000 becomes the io vector, and the game starts at
#   $0081, its own DI. The game runs no RST $00 and has no jump or call to $0000.
# - The scan needs entry points that no path names. The object dispatcher at $03F4 jumps
#   with JP (HL) to the word at IX+0 of each object at $C100; the handlers store the next
#   handler there (LD (IX+$00),n; LD (IX+$01),n, or LD HL,n then JP $4786). The main state
#   table at $017F has 24 entries (state in $C019; entry 5 is $0000); the scan reads only
#   the first 5. The monster handler table at $2012 has 33 entries, and $2054 follows it.
# - The pointer harvest takes $160F (stored by $154E to $C0B8) for code; it is a text list.
#   The sound driver's command table at $86BB (bank 7) has entries ($888C) that point at
#   data; the bank 7 stores through BC and the RET at $1C8E come from that data.
# - The VRAM fill at $0618 ends its inner loop with DJNZ $0624, the operand byte of the
#   OUT ($BE),A at $0623. Both calls ($05C9, $05F3) pass BC = 1, so the inner loop never
#   runs again and the patched byte at $0624 is never run as an opcode.
# - Unused code (no call, jump, address load or table entry names it): the VDP routines at
#   $0018 (RST $18), $062C, $06CB, $06E6 and $0706.
# - priority: the message windows ($C700 buffer) are drawn with the priority bit, and on a
#   Master System they hide the sprites under them; without it the sprites under the bottom
#   window cover its top border. The map's wall metatiles carry the priority bit as well,
#   and the walls cover most of the screen: with them marked, each wall cell is drawn
#   again in Layer 2, and the window draws run over a frame three times as often. The map
#   is a grid of 16x16 cells and the sprites stay in theirs, except for a few pixels at a
#   cell's edge, such as the tip of the hero's weapon in an attack, which a Master System
#   hides behind the wall and the Next shows. $2A22 loads the floor's metatile words into
#   $C800-$C8AF; its tail (LD HL,$86C5; LD DE,$C860; JP $0A9D, the second half of the copy)
#   goes to a cave in the unused $FF bytes of bank 1 (slot 1 always holds bank 1) that makes
#   the same copy and then clears bit 4 of the attribute byte of each word. Only the
#   windows keep the priority bit.
name Dragon Crystal
cart 9549FCE4
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
priority
start 0081
asm 00085 2   ; IM 1 -> IM 2
    im 2
endasm
asm 02A53 3   ; LD HL,$86C5 -> JP mtcave: the metatile copy goes on in the cave
    jp $7E00
endasm
asm 07E00 23  ; unused $FF bytes: mtcave, the rest of the copy, then the priority bit off
    ld hl,$86C5
    ld de,$C860
    ld bc,80
    ldir
    ld hl,$C801
    ld b,88
.strip:
    res 4,(hl)
    inc hl
    inc hl
    djnz .strip
    ret
endasm
site 0000A   ; OUT ($BF),A
site 0000F   ; OUT ($BF),A
site 0003B   ; OUT ($BF),A
site 0003F   ; OUT ($BF),A
site 000A2   ; IN A,($7E)
site 000A9   ; OUT ($BF),A
site 000AD   ; OUT ($BF),A
site 000B4   ; OUT ($BE),A
site 000C4   ; IN A,($BF)
site 000CD   ; OTIR
site 000FE   ; IN A,($DC)
site 001B0   ; IN A,($BF)
site 00277   ; OUT ($BF),A
site 0027B   ; OUT ($BF),A
site 0029F   ; OUT ($BF),A
site 002A3   ; OUT ($BF),A
site 002AF   ; OUT ($BF),A
site 002B3   ; OUT ($BF),A
site 002D4   ; OUT ($BF),A
site 002D8   ; OUT ($BF),A
site 002ED   ; OUT ($BF),A
site 002F1   ; OUT ($BF),A
site 002FB   ; OUT ($BF),A
site 002FF   ; OUT ($BF),A
site 00308   ; IN A,($DD)
site 00326   ; IN A,($DC)
otir 0060E   ; OUTI
site 00623   ; OUT ($BE),A
site 0063F   ; OUT (C),A
site 00644   ; OUT (C),A
site 00651   ; OUTI
site 00653   ; OUTI
site 00666   ; OUTI
site 0066B   ; OUTI
site 0069D   ; OUTI
site 006A2   ; OUTI
site 006AF   ; OUTI
site 006B4   ; OUTI
site 00785   ; OUT ($BF),A
site 00789   ; OUT ($BF),A
site 007BC   ; OUT ($BE),A
site 0082F   ; OUT (C),D
site 0083C   ; OUTI
site 0083E   ; OUTI
site 00840   ; OUTI
site 00842   ; OUTI
site 00844   ; OUTI
site 00846   ; OUTI
site 00848   ; OUTI
site 0084A   ; OUTI
site 0084C   ; OUTI
site 0084E   ; OUTI
site 00850   ; OUTI
site 00852   ; OUTI
site 00854   ; OUTI
site 00856   ; OUTI
site 00858   ; OUTI
site 0085A   ; OUTI
site 0085C   ; OUTI
site 0085E   ; OUTI
site 00860   ; OUTI
site 00862   ; OUTI
site 00864   ; OUTI
site 00866   ; OUTI
site 00868   ; OUTI
site 0086A   ; OUTI
site 0086C   ; OUTI
site 0086E   ; OUTI
site 00870   ; OUTI
site 00872   ; OUTI
site 00874   ; OUTI
site 00876   ; OUTI
site 00878   ; OUTI
site 0087A   ; OUTI
site 0087C   ; OUTI
site 0087E   ; OUTI
site 00880   ; OUTI
site 00882   ; OUTI
site 00884   ; OUTI
site 00886   ; OUTI
site 00888   ; OUTI
site 0088A   ; OUTI
site 0088C   ; OUTI
site 0088E   ; OUTI
site 00890   ; OUTI
site 00892   ; OUTI
site 00894   ; OUTI
site 00896   ; OUTI
site 00898   ; OUTI
site 0089A   ; OUTI
site 0089C   ; OUTI
site 0089E   ; OUTI
site 008A0   ; OUTI
site 008A2   ; OUTI
site 008A4   ; OUTI
site 008A6   ; OUTI
site 008A8   ; OUTI
site 008AA   ; OUTI
site 008AC   ; OUTI
site 008AE   ; OUTI
site 008B0   ; OUTI
site 008B2   ; OUTI
site 008B4   ; OUTI
site 008B6   ; OUTI
site 008B8   ; OUTI
site 008BA   ; OUTI
site 008BC   ; OUTI
site 008BE   ; OUTI
site 008C0   ; OUTI
site 008C2   ; OUTI
site 008C4   ; OUTI
site 008C6   ; OUTI
site 008C8   ; OUTI
site 008CA   ; OUTI
site 008CC   ; OUTI
site 008CE   ; OUTI
site 008D0   ; OUTI
site 008D2   ; OUTI
site 008D4   ; OUTI
site 008D6   ; OUTI
site 008D8   ; OUTI
site 008DA   ; OUTI
site 008DC   ; OUTI
site 008DE   ; OUTI
site 008E0   ; OUTI
site 008E2   ; OUTI
site 008E4   ; OUTI
site 008E6   ; OUTI
site 008E8   ; OUTI
site 008EA   ; OUTI
site 008EC   ; OUTI
site 008EE   ; OUTI
site 008F0   ; OUTI
site 008F2   ; OUTI
site 008F4   ; OUTI
site 008F6   ; OUTI
site 008F8   ; OUTI
site 008FA   ; OUTI
site 008FC   ; OUTI
site 008FE   ; OUTI
site 00900   ; OUTI
site 00902   ; OUTI
site 00904   ; OUTI
site 00906   ; OUTI
site 00908   ; OUTI
site 0090A   ; OUTI
site 0090C   ; OUTI
site 0090E   ; OUTI
site 00910   ; OUTI
site 00912   ; OUTI
site 00914   ; OUTI
site 00916   ; OUTI
site 00918   ; OUTI
site 0091A   ; OUTI
site 0091C   ; OUTI
site 0091E   ; OUTI
site 00920   ; OUTI
site 00922   ; OUTI
site 00924   ; OUTI
site 00926   ; OUTI
site 00928   ; OUTI
site 0092A   ; OUTI
site 0092C   ; OUTI
site 0092E   ; OUTI
site 00930   ; OUTI
site 00932   ; OUTI
site 00934   ; OUTI
site 00936   ; OUTI
site 00938   ; OUTI
site 0093A   ; OUTI
site 0093C   ; OUTI
site 0093E   ; OUTI
site 00940   ; OUTI
site 00942   ; OUTI
site 00944   ; OUTI
site 00946   ; OUTI
site 00948   ; OUTI
site 0094A   ; OUTI
site 0094C   ; OUTI
site 0094E   ; OUTI
site 00950   ; OUTI
site 00952   ; OUTI
site 00954   ; OUTI
site 00956   ; OUTI
site 00958   ; OUTI
site 0095A   ; OUTI
site 0095C   ; OUTI
site 0095E   ; OUTI
site 00960   ; OUTI
site 00962   ; OUTI
site 00964   ; OUTI
site 00966   ; OUTI
site 00968   ; OUTI
site 0096A   ; OUTI
site 0096C   ; OUTI
site 0096E   ; OUTI
site 00970   ; OUTI
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
site 00BC9   ; OUT ($BF),A
site 00BCD   ; OUT ($BF),A
site 00BD0   ; OUT ($BF),A
site 00BD4   ; OUT ($BF),A
site 00BDC   ; OUT ($BF),A
site 00BE0   ; OUT ($BF),A
site 00F5C   ; OUT ($BF),A
site 00F60   ; OUT ($BF),A
site 0127F   ; OUT ($BE),A
site 01283   ; OUT ($BE),A
site 012AC   ; OUT ($BE),A
site 012B0   ; OUT ($BE),A
site 012D1   ; OUTI
site 012D6   ; OUT (C),A
site 012EB   ; IN A,($BE)
site 012F0   ; IN A,($BE)
site 012F5   ; IN A,($BE)
site 012FA   ; IN A,($BE)
site 01303   ; OUTI
site 01308   ; OUT (C),A
site 01315   ; OUTI
site 0131A   ; OUT (C),A
site 0153D   ; OUT ($BF),A
site 01541   ; OUT ($BF),A
site 01545   ; OUT ($BF),A
site 01549   ; OUT ($BF),A
site 0157D   ; OUT ($BF),A
site 01581   ; OUT ($BF),A
site 015FB   ; OUTI
site 015FF   ; OUTI
site 01606   ; OUT ($BE),A
site 0160C   ; OUT ($BE),A
site 017E1   ; OUT ($BE),A
site 017E5   ; OUT ($BE),A
site 0181F   ; OUT ($BE),A
site 01823   ; OUT ($BE),A
site 01827   ; OUT ($BE),A
site 0182B   ; OUT ($BE),A
site 01847   ; OUT ($BE),A
site 0184B   ; OUT ($BE),A
site 01871   ; OUT ($BE),A
site 01875   ; OUT ($BE),A
site 0189B   ; OUT ($BE),A
site 0189F   ; OUT ($BE),A
site 018C6   ; OUT ($BE),A
site 018CA   ; OUT ($BE),A
site 018E9   ; OUT ($BE),A
site 018ED   ; OUT ($BE),A
site 0194D   ; OUT ($BE),A
site 01951   ; OUT ($BE),A
otir 0290C   ; OUTI
site 030CF   ; OUT ($BF),A
site 030D3   ; OUT ($BF),A
site 030D8   ; OUT ($BF),A
site 030DC   ; OUT ($BF),A
otir 03781   ; OUTI
site 04DFC   ; IN A,($BE)
site 04E03   ; OUT ($BE),A
site 04E0D   ; IN A,($BE)
site 04E14   ; OUT ($BE),A
site 04E49   ; OUT ($BE),A
site 04E5A   ; OUT ($BE),A
site 04E6B   ; OUT ($BE),A
site 04E7F   ; OUT ($BE),A
site 04E93   ; OUT ($BE),A
site 04EAF   ; OUT ($BE),A
site 04EE8   ; OUTI
site 04EED   ; OUT (C),A
site 04F3A   ; OUTI
site 04F3F   ; OUT (C),A
site 04F82   ; OUT ($BE),A
site 04F88   ; OUT ($BE),A
site 04F8F   ; OUT ($BE),A
site 04F95   ; OUT ($BE),A
site 1C198   ; OUT ($7F),A
site 1C27A   ; OUT ($7F),A
site 1C3CD   ; OTIR
site 1C4E9   ; OUT ($7F),A
site 1C4F3   ; OUT ($7F),A
site 1C510   ; OUT ($7F),A
site 1C614   ; OUT ($7F),A
site 1C6A0   ; OUT ($7F),A
site 1C738   ; OUT ($06),A
site 1C782   ; OUT ($7F),A
site 1C78B   ; OUT ($7F),A
site 1C79B   ; OUT ($7F),A
site 1C7FD   ; OUT ($7F),A
mapldk 00087   # LD HL,$FFFC; LD (HL),$00
maphl 0008D   # LD (HL),$00, HL = $FFFD
maphl 00090   # LD (HL),$01, HL = $FFFE
maphl 00093   # LD (HL),$02, HL = $FFFF
mapst 001ED   ; LD ($FFFF),A
mapst 00208   ; LD ($FFFF),A
mapst 00BEF   ; LD ($FFFF),A
mapst 00BF7   ; LD ($FFFF),A
mapst 00C05   ; LD ($FFFF),A
mapst 00CE4   ; LD ($FFFF),A
mapst 00D77   ; LD ($FFFF),A
mapst 00D83   ; LD ($FFFF),A
mapst 00D94   ; LD ($FFFF),A
mapst 00E73   ; LD ($FFFF),A
mapst 00E97   ; LD ($FFFF),A
mapst 00EB0   ; LD ($FFFF),A
mapst 00F51   ; LD ($FFFF),A
mapst 0105D   ; LD ($FFFF),A
mapst 010D6   ; LD ($FFFF),A
mapst 0112F   ; LD ($FFFF),A
mapst 0116E   ; LD ($FFFF),A
mapst 011A5   ; LD ($FFFF),A
mapst 011E0   ; LD ($FFFF),A
mapst 01211   ; LD ($FFFF),A
mapst 0121F   ; LD ($FFFF),A
mapst 01245   ; LD ($FFFF),A
mapst 013A9   ; LD ($FFFF),A
mapst 013C7   ; LD ($FFFF),A
mapst 013D2   ; LD ($FFFF),A
mapst 013ED   ; LD ($FFFF),A
mapst 0144C   ; LD ($FFFF),A
mapst 01467   ; LD ($FFFF),A
mapst 014A7   ; LD ($FFFF),A
mapst 014C5   ; LD ($FFFF),A
mapst 016F9   ; LD ($FFFF),A
mapst 01B25   ; LD ($FFFF),A
mapst 01B72   ; LD ($FFFF),A
mapst 01BAB   ; LD ($FFFF),A
mapst 01BDF   ; LD ($FFFF),A
mapst 01BF3   ; LD ($FFFF),A
mapst 01C27   ; LD ($FFFF),A
mapst 01C38   ; LD ($FFFF),A
mapst 01CAD   ; LD ($FFFF),A
mapst 01D1C   ; LD ($FFFF),A
mapst 01D62   ; LD ($FFFF),A
mapst 01D9E   ; LD ($FFFF),A
mapst 02056   ; LD ($FFFF),A
mapst 024B4   ; LD ($FFFF),A
mapst 02672   ; LD ($FFFF),A
mapst 026F5   ; LD ($FFFF),A
mapst 027E5   ; LD ($FFFF),A
mapst 02808   ; LD ($FFFF),A
mapst 02823   ; LD ($FFFF),A
mapst 028B4   ; LD ($FFFF),A
mapst 028FF   ; LD ($FFFF),A
mapst 0295A   ; LD ($FFFF),A
mapst 02A24   ; LD ($FFFF),A
mapst 02B2D   ; LD ($FFFF),A
mapst 035A6   ; LD ($FFFF),A
mapst 0374C   ; LD ($FFFF),A
mapst 04E2F   ; LD ($FFFF),A
mapst 04EBF   ; LD ($FFFF),A
mapst 04F00   ; LD ($FFFF),A

# Dragon Crystal (Europe) (Action Replay).cht, "Infinite Food": RAM $C620 is the food, in
# BCD; $30 is the full ration and it no longer runs down
poke "Infinite food"
ar 00C6-2030
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Infinite Energy": RAM $C621 is the current
# hit points; $99 holds them above the maximum of 100 and starvation or monsters no longer
# kill the hero
poke "Infinite energy"
ar 00C6-2199
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Rapidly Gain Levels": RAM $C626 is the
# experience count; held at $FF the hero gains levels quickly in fights (rank, maximum hit points and
# power grow)
poke "Rapid level gain"
ar 00C6-26FF
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Have 90,000 Gold": RAM $C62D is the gold in
# units of 10,000; $09 shows GOLD 90000
poke "90,000 gold"
ar 00C6-2D09
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "PW (Attack Power) Modifier": RAM $C618 is
# the base attack power shown as PW; any byte is the value
poke "Attack power"
ar 00C6-18??
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "AC (Armor Class) Modifier": RAM $C61A is the
# armor class shown as AC; any byte is the value
poke "Armor class"
ar 00C6-1A??
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Have Weapon Slot 1": RAM $C900 is the first
# weapon slot; $01 is DAGGER, $02 SHORT SWORD, $03 LONG SWORD, $05 GLADIUS, $08 LASER BLADE, $0F
# DEATH BLADE
poke "Weapon slot 1"
ar 00C9-00??
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Have Armor Slot 1": RAM $C908 is the first
# armor slot; the byte is $10 plus the armor number
poke "Armor slot 1"
ar 00C9-08??
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Have Scroll Slot 1": RAM $C910 is the first
# scroll slot; the byte is $20 plus the scroll number
poke "Scroll slot 1"
ar 00C9-10??
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Have Rod Slot 1": RAM $C918 is the first rod
# slot; the byte is $30 plus the rod number
poke "Rod slot 1"
ar 00C9-18??
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Have Potion Slot 1": RAM $C920 is the first
# potion slot; the byte is $40 plus the potion number
poke "Potion slot 1"
ar 00C9-20??
endpoke

# Dragon Crystal (Europe) (Action Replay).cht, "Have Ring Slot 1": RAM $C928 is the first
# ring slot; the byte is $50 plus the ring number
poke "Ring slot 1"
ar 00C9-28??
endpoke
