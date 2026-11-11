# Rampage (USA, Europe, Brazil) (En), CRC32 42FC47EE, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - No free RST vector ($0008, $0010 and $0020 are the game's; $0018, $0028 and $0030
#   are inside the routines there): $0000-$0002 (IM 1; part of LD SP,$DFF0) becomes
#   the io vector, and the game starts at $0005 with SP $DFF0. The game has no RST $00.
# - The I/O ports $F0-$F2 are the FM unit: the game looks for it at power on ($0576)
#   and its sound driver in bank 2 writes it when it is there.
# - The Next is an export console to the region check at $0468 ($C001 = $FF), so the
#   game skips the power-on delay $048B and the SEGA logo ($0728), as on an export
#   Master System.
# - The byte scan rows in banks 2, 4 and 10 are graphics or sound data (verdict false):
#   the only code in slot 2 is the sound driver in bank 2 ($8000-$8C57).
# - $065B (LD ($FFFF),A in the unreached sound driver entry $0659) is patched as code.
# - $710E writes 192 bytes of a monster's tiles each time its frame changes, one OUTI
#   at a time with two EX (SP),HL between them for the VDP's speed. The loop at $7122
#   becomes one OTIR through the runtime: 192 single traps cost up to 390,000 cycles,
#   and put play frames over 100%.
name Rampage
cart 42FC47EE
hz any		; No-Intro regions USA, Europe, Brazil
vector 00 io
start 0005 DFF0
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 002FF   ; IN A,($BF)
site 00353   ; IN A,($DD)
site 0039F   ; OUTI
site 003C2   ; OUT ($BE),A
site 003CF   ; OUTI
site 00411   ; OUT ($BE),A
site 00416   ; OUT ($BE),A
site 00423   ; OUTI
site 00429   ; OUT (C),A
site 0043E   ; OUTI
site 00458   ; OTIR
site 0046D   ; OUT ($3F),A
site 0046F   ; IN A,($DD)
site 00479   ; OUT ($3F),A
site 0047B   ; IN A,($DD)
site 00484   ; OUT ($3F),A
site 004B4   ; IN A,($DC)
site 004B8   ; IN A,($DD)
site 004DF   ; IN A,($DD)
site 004E3   ; IN A,($DC)
site 0056D   ; OUT ($BE),A
site 00572   ; OUT ($BE),A
site 0057B   ; OUT ($3E),A
site 00583   ; OUT ($F2),A
site 00586   ; IN A,($F2)
site 00598   ; OUT ($F2),A
site 005A0   ; OUT ($3E),A
site 006DF   ; OUT ($BE),A
site 0070D   ; OUT ($BE),A
otir 0453A   ; OUTI
otir 04565   ; OUTI
site 04D51   ; OUT ($BE),A
site 04D5A   ; OUT ($BE),A
site 04FD8   ; OUT ($BE),A
site 04FE5   ; OUT ($BE),A
site 05097   ; OUT ($BE),A
site 051D9   ; OUT ($BE),A
site 051E5   ; OUT ($BE),A
site 0524C   ; OUT ($BE),A
site 05258   ; OUT ($BE),A
site 0529B   ; OUT ($BE),A
site 052A7   ; OUT ($BE),A
site 05377   ; OUT ($BE),A
site 05384   ; OUT ($BE),A
site 053CE   ; OUT ($BE),A
site 053D9   ; OUT ($BE),A
site 053EA   ; OUT ($BE),A
site 053F7   ; OUT ($BE),A
site 0543F   ; OUT ($BE),A
site 0544A   ; OUT ($BE),A
site 0545A   ; OUT ($BE),A
site 05467   ; OUT ($BE),A
site 05511   ; OUT ($BE),A
site 055CD   ; OUT ($BE),A
site 0581F   ; OUT ($BE),A
site 05825   ; OUT ($BE),A
asm 07122 6    ; OUTI; EX (SP),HL; EX (SP),HL; JR NZ,$7122: 192 bytes of monster tiles
    rst $00     ; one OTIR through the runtime: B bytes from HL to port C ($BE)
    db $B3
    nop
    nop
    nop
    nop
endasm
site 07468   ; OUT ($BE),A
site 0746E   ; OUT ($BE),A
site 07505   ; OUTI
site 07517   ; OUT ($BE),A
site 0751D   ; OUT ($BE),A
site 0762E   ; OUT ($BE),A
site 07634   ; OUT ($BE),A
site 07C31   ; OUTI
site 07C40   ; OUTI
site 07C42   ; OUTI
site 07C57   ; OUTI
site 07C67   ; OUTI
site 07C69   ; OUTI
site 07C84   ; OUTI
site 07C93   ; OUTI
site 07C95   ; OUTI
site 07CAD   ; OUTD
site 07CB5   ; OUT ($BE),A
site 07CCB   ; OUTI
site 07CCD   ; OUTD
site 0812D   ; OUT ($F0),A
site 08136   ; OUT ($F1),A
site 0814E   ; OUT ($7F),A
site 0815E   ; OUT (C),D
site 08164   ; OUT ($F1),A
site 08189   ; OUT ($7F),A
site 0818D   ; OUT ($7F),A
site 081BB   ; OTIR
site 081C9   ; OTIR
site 081D3   ; OUT ($F0),A
site 081D9   ; OUT ($F1),A
site 081E5   ; OUTI
site 081EB   ; OUTI
site 0837C   ; OUT ($7F),A
site 08380   ; OUT ($7F),A
site 08429   ; OUT ($7F),A
site 0842D   ; OUT ($7F),A
site 08455   ; OUT ($7F),A
site 08459   ; OUT ($7F),A
site 0845D   ; OUT ($7F),A
site 08461   ; OUT ($7F),A
site 08464   ; OUT ($7F),A
site 084CA   ; OUT ($F0),A
site 084D1   ; OUT ($F1),A
site 084D9   ; OUT ($F0),A
site 084DF   ; OUT ($F1),A
site 085D0   ; OUT ($F0),A
site 085DA   ; OUT (C),L
site 085E3   ; OUT ($F0),A
site 085FE   ; OUT (C),H
site 08606   ; OUT ($F0),A
site 08614   ; OUT ($F1),A
site 08620   ; OUT ($F0),A
site 08629   ; OUT ($F1),A
site 087EA   ; OUT ($F0),A
site 087F3   ; OUT (C),A
site 087F8   ; OUT ($F0),A
site 087FE   ; OUTI
site 0886F   ; OUT ($7F),A
site 0893E   ; OUT ($7F),A
site 08965   ; OUT ($7F),A
site 0896A   ; OUT ($7F),A
site 08996   ; OUT ($F0),A
site 089A4   ; OUT ($F1),A
site 089B2   ; OUT ($F0),A
site 08A49   ; OUTI
site 08A4B   ; OUTI
site 08A4D   ; OUTI
site 08A4F   ; OUTI
site 08A51   ; OUTI
site 08A53   ; OUTI
site 08A55   ; OUTI
site 08A57   ; OUTI
site 08A59   ; OUTI
site 08A5B   ; OUTI
site 08A5D   ; OUTI
site 08A67   ; OUT (C),D
site 08A6D   ; OUT ($F1),A
site 08AAC   ; OUT ($7F),A
site 08B02   ; OUT ($7F),A
site 08B41   ; OUT ($7F),A
site 08BA3   ; OUT ($7F),A
site 08BC3   ; OUT ($7F),A
site 08C03   ; OUT ($7F),A
site 08C0D   ; OUT ($7F),A
site 08C55   ; OUT ($7F),A
mapsthl 0006C   ; LD ($FFFC),HL
mapsthl 00072   ; LD ($FFFE),HL
mapst 00349   ; LD ($FFFF),A
mapst 00364   ; LD ($FFFF),A
mapst 00653   ; LD ($FFFF),A
mapst 00663   ; LD ($FFFF),A
mapst 006C0   ; LD ($FFFF),A
mapst 0412D   ; LD ($FFFF),A
mapst 0452C   ; LD ($FFFF),A
mapst 04557   ; LD ($FFFF),A
mapst 0458A   ; LD ($FFFF),A
mapst 045A7   ; LD ($FFFF),A
mapst 045BC   ; LD ($FFFF),A
mapst 0493F   ; LD ($FFFF),A
mapst 07B14   ; LD ($FFFF),A
mapst 0065B   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it

# Rampage (USA, Europe, Brazil).cht, "Infinite Health P1": RAM $C096 is the player 1
# energy, $60 when full
poke "Infinite energy"
ar 00C0-9660
endpoke

# Rampage (USA, Europe, Brazil).cht, "Infinite Lives P1": RAM $C0A0 is the player 1 lives
poke "Infinite lives"
ar 00C0-A003
endpoke

# Rampage (USA, Europe, Brazil).cht, "City/Day Select - City 02 - Los Angeles - Day 1":
# RAM $C0E0-$C0E2 hold the city and day; the game starts in Los Angeles
poke "Start Los Angeles"
ar 00C0-E005
ar 00C0-E100
ar 00C0-E201
endpoke

# Rampage (USA, Europe, Brazil).cht, "City/Day Select - City 10 - New York - Day 5 (Final
# Day of Final City)": RAM $C0E0-$C0E2 hold the city and day; the game starts in New York
poke "Start New York"
ar 00C0-E031
ar 00C0-E104
ar 00C0-E209
endpoke
