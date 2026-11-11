# Miracle Warriors - Seal of The Dark Lord (USA, Europe, Brazil) (En), CRC32 0E333B6E, 256K,
# Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - The scan runs with --no-harvest: the harvested addresses $0100, $01B6, $0558 and
#   $05A0 are tables, and decoding them gives the RET C rows at $0589-$05DB and $01D6.
# - Entry points for the scan, besides the logs: the VRAM read routines at $3D7E (INI
#   loop) and $4002 (a rectangle read), which nothing in the scan or the logs calls.
# - Code runs only in banks 0 and 1 and, in slot 2, in the sound driver in bank 15. Banks
#   2-14 are data that slot 2 maps through the stubs at $2B98-$2BEB (LD A,n; LD ($FFFF),A;
#   RET). The stubs for banks 11-14 ($2BCE-$2BE5) are not called directly, but are the
#   same code, so they are patched as well.
# - The start-up sets the mapper through IX = $FFFC with LD (IX+d),n, which has no inline
#   code. $007B-$008E becomes LD A,n and a mapper write for each register.
# - The game saves to cart RAM: LD ($FFFC),A with $08 and $80 around the writes to $8020-
#   $8029 ($31BF-$328F, $6F7A-$7014).
# - priority: the hero's name under the health bar is tiles with the priority bit (name
#   table rows 16-17, columns 1-4), drawn over the bar's sprites. Without it the bar hides
#   the name.
name Miracle Warriors
cart 0E333B6E
hz any		; No-Intro regions USA, Europe, Brazil
priority	; the hero's name below the health bar is tiles with the priority bit over the bar's sprites
vector 30 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 0007B 20  ; LD IX,$FFFC; LD (IX+0..3),$80/$00/$01/$02 -> mapper writes
    ld a,$80
    rst $30
    db $10, 0
    xor a
    rst $30
    db $11, 0
    ld a,$01
    rst $30
    db $12, 0
    ld a,$02
    rst $30
    db $13, 0
endasm
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
otir 00027   ; OUTI
site 00070   ; OUT ($DF),A
site 000DC   ; IN A,($BF)
site 001C7   ; OTIR
site 001D4   ; OTIR
site 01825   ; OUT ($BE),A
site 03CDC   ; OUT ($3F),A
site 03CDE   ; IN A,($DD)
site 03CE8   ; OUT ($3F),A
site 03CEA   ; IN A,($DD)
site 03CF3   ; OUT ($3F),A
site 03D05   ; OUT ($3E),A
site 03D0D   ; OUT ($F2),A
site 03D10   ; IN A,($F2)
site 03D22   ; OUT ($F2),A
site 03D2A   ; OUT ($3E),A
site 03D66   ; OUT ($BE),A
site 03D74   ; IN A,($BE)
site 03D85   ; INI
site 03D93   ; OUT ($BE),A
site 03DC5   ; OUT ($BE),A
site 03F2D   ; OUT ($7F),A
site 03F31   ; OUT ($7F),A
site 03F35   ; OUT ($7F),A
site 03F39   ; OUT ($7F),A
site 03F54   ; OUT (C),D
site 03F7F   ; OUT ($BE),A
site 03F94   ; IN A,($DC)
site 03FA3   ; IN A,($DD)
site 03FBE   ; OUTI
site 03FC5   ; OUT ($BE),A
site 03FDD   ; OUTI
site 04007   ; IN A,($BE)
site 0400D   ; IN A,($BE)
site 04022   ; IN A,($BE)
site 04028   ; IN A,($BE)
site 04045   ; OUT ($BE),A
site 0404C   ; OUT ($BE),A
site 04071   ; OUT ($BE),A
site 04076   ; OUT ($BE),A
site 04099   ; OUT ($BE),A
site 0409F   ; OUT ($BE),A
site 04233   ; OUT ($BE),A
site 0437A   ; OUT ($BE),A
site 04933   ; OUT ($BE),A
site 0493A   ; OUT ($BE),A
site 05FEF   ; OUT ($BE),A
site 06D66   ; OUT ($BE),A
site 06D6F   ; OUT ($BE),A
site 06DA6   ; OUT ($BE),A
site 06F52   ; OUT ($BE),A
site 06F57   ; OUT ($BE),A
site 3CAA8   ; OUT (C),B
site 3CABC   ; OUT ($F1),A
site 3CB03   ; OUT ($7F),A
site 3CB13   ; OUT (C),D
site 3CB19   ; OUT ($F1),A
site 3CD15   ; OUT ($F0),A
site 3CD1B   ; OUT ($F1),A
site 3CD26   ; OUTI
site 3CD2D   ; OUTI
site 3CD4E   ; OUT ($7F),A
site 3CD52   ; OUT ($7F),A
site 3CDAD   ; OUT ($F0),A
site 3CDB4   ; OUT ($F1),A
site 3CDBC   ; OUT ($F0),A
site 3CDC2   ; OUT ($F1),A
site 3CEBC   ; OUT ($F0),A
site 3CEC3   ; OUT (C),L
site 3CECC   ; OUT ($F0),A
site 3CEE7   ; OUT (C),H
site 3CEEF   ; OUT ($F0),A
site 3CEFD   ; OUT ($F1),A
site 3CF05   ; OUT ($F0),A
site 3CF0F   ; OUT ($F1),A
site 3D091   ; OUT ($F0),A
site 3D097   ; OUTI
site 3D0F8   ; OUT ($7F),A
site 3D1AD   ; OUT ($7F),A
site 3D1B1   ; OUT ($7F),A
site 3D1C7   ; OUT ($7F),A
site 3D1E9   ; OUT ($7F),A
site 3D1F8   ; OUT ($F0),A
site 3D203   ; OUT ($F1),A
site 3D20D   ; OUT ($F0),A
site 3D21B   ; OUT ($F1),A
site 3D227   ; OUT ($F0),A
site 3D235   ; OUT ($F1),A
site 3D2B0   ; OTIR
site 3D2BE   ; OUT (C),D
site 3D2C4   ; OUT ($F1),A
site 3D301   ; OUT ($7F),A
site 3D352   ; OUT ($7F),A
site 3D3D7   ; OUT ($7F),A
site 3D3F5   ; OUT ($7F),A
site 3D435   ; OUT ($7F),A
site 3D43F   ; OUT ($7F),A
site 3D487   ; OUT ($7F),A
site 3F61F   ; OUT ($7F),A
site 3F622   ; OUT ($F2),A
site 3F63C   ; OUT ($7F),A
site 3F64C   ; OUT ($F2),A
mapst 0013F   ; LD ($FFFF),A
mapst 009CD   ; LD ($FFFF),A
mapst 02B9A   ; LD ($FFFF),A
mapst 02BA0   ; LD ($FFFF),A
mapst 02BA6   ; LD ($FFFF),A
mapst 02BAC   ; LD ($FFFF),A
mapst 02BB2   ; LD ($FFFF),A
mapst 02BB8   ; LD ($FFFF),A
mapst 02BBE   ; LD ($FFFF),A
mapst 02BC4   ; LD ($FFFF),A
mapst 02BCA   ; LD ($FFFF),A
mapst 02BE8   ; LD ($FFFF),A
mapst 031BF   ; LD ($FFFC),A
mapst 031DB   ; LD ($FFFC),A
mapst 031EC   ; LD ($FFFC),A
mapst 03208   ; LD ($FFFC),A
mapst 03219   ; LD ($FFFC),A
mapst 03235   ; LD ($FFFC),A
mapst 03246   ; LD ($FFFC),A
mapst 03262   ; LD ($FFFC),A
mapst 03273   ; LD ($FFFC),A
mapst 0328F   ; LD ($FFFC),A
mapst 06F7A   ; LD ($FFFC),A
mapst 06F96   ; LD ($FFFC),A
mapst 06FB5   ; LD ($FFFC),A
mapst 06FCD   ; LD ($FFFC),A
mapst 06FE5   ; LD ($FFFC),A
mapst 06FFD   ; LD ($FFFC),A
mapst 07014   ; LD ($FFFC),A
mapst 02BD0   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 02BD6   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 02BDC   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 02BE2   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it

# Miracle Warriors - Seal of the Dark Lord (USA, Europe, Brazil).cht, "Infinite Health Main
# Char.": the patch at $4603 (bank 1) is a RET, so the hero's hit points are never reduced
poke "Infinite health"
gg C96-03B-6E2
endpoke

# Miracle Warriors - Seal of the Dark Lord (USA, Europe) (Action Replay) (diff).cht, "Maximum
# Gold": RAM $C430-$C431 is the gold, held at $EA60
poke "Maximum gold"
ar 00C4-3060
ar 00C4-31EA
endpoke

# Miracle Warriors - Seal of the Dark Lord (USA, Europe) (Action Replay) (diff).cht, "Infinite
# Fangs": RAM $C434 is the number of fangs, held at $FF
poke "Infinite fangs"
ar 00C4-34FF
endpoke

# Miracle Warriors - Seal of the Dark Lord (USA, Europe, Brazil).cht, "Character 1 Quick Level
# Up": RAM $C509 is the high byte of the experience the hero needs for the next level, held
# at 0
poke "Quick level up"
ar 00C5-0900
endpoke

# Miracle Warriors - Seal of the Dark Lord (USA, Europe, Brazil).cht, "Character 1 Quickly
# Kills Enemies": RAM $C510, held at $FF
poke "Quick kills"
ar 00C5-10FF
endpoke

# Miracle Warriors - Seal of the Dark Lord (USA, Europe, Brazil).cht, "No Random Battles":
# the patches at $090F and $092A (bank 0) are RETs
poke "No random battles"
gg C99-0FF-A29
gg C99-2AF-A29
endpoke

# Miracle Warriors - Seal of the Dark Lord (USA, Europe, Brazil).cht, "Walk Anywhere": the
# patch at $2F7A (bank 0) is a NOP
poke "Walk anywhere"
gg 00F-7AD-E69
endpoke

# Miracle Warriors - Seal of the Dark Lord (USA, Europe) (Action Replay) (diff).cht, "Infinite
# Feathers": RAM $C403 is the number of feathers, held at 5; FEATHER is in the field menu
poke "Feathers"
ar 00C4-0305
endpoke

# Miracle Warriors - Seal of the Dark Lord (USA, Europe) (Action Replay) (diff).cht, "Scroll":
# RAM $C40A, held at 1; SCROLL is in the field menu
poke "Scroll"
ar 00C4-0A01
endpoke
