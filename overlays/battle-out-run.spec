# Battle Out Run (Europe, Brazil) (En), CRC32 C19430CE, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - The road needs a scroll value on every line. The line interrupt handler ($02A8,
#   per-line part copied to $D200) gets an event at line 47, line 95 and then on every
#   line from 127, and sets register 8 from ($C171) and the table at $D002. The
#   rastercode routine works out the same 192 values from RAM once a frame.
# - The byte scan rows at $0136 and $1E1D are in the VRAM copy routines $0132 and
#   $1E1A: no call, jump, address load or table word in the cart names their starts
#   (verdict unused).
# - Banks 2-14 hold data only: every call or jump into slot 2 is with bank 15 (the
#   sound driver); the other banks come from the VRAM upload lists at $C200, $C207 and
#   $C238 and are copy sources. The byte scan rows there are data (verdict false).
# - The jump table at $3443 (base $3550) has entries for ($C316) = 1 to 3 only; the
#   scanner reads data past them as entries, which gives the bogus stores into
#   $3F48-$4737 in the scan. No I/O site comes from those paths.
# - The game steps every two frame events ($00AD and $00C4) and does not need a hold:
#   on the Next it steps every 2 frames, which a PAL Master System also does on most of
#   a race; it only slows down less in busy stretches.
name Battle Out Run
cart C19430CE
hz 50
# No free RST vector: the JP at $0000 becomes the vector, the game
# starts at its target.
vector 00 io
start 0069
asm 0006A 2   ; IM 1 -> IM 2
    im 2
endasm
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 000FA   ; OUT ($BE),A
site 00100   ; OUT ($BE),A
site 00112   ; OTIR
site 0012C   ; OUT ($BF),A
site 0012F   ; OUT ($BF),A
site 00147   ; OUT ($BE),A
site 00159   ; OUT ($BE),A
site 00187   ; OUT ($3E),A
site 0018F   ; OUT ($F2),A
site 00192   ; IN A,($F2)
site 001A5   ; OUT ($F2),A
site 001AD   ; OUT ($3E),A
site 001EC   ; OUT ($3F),A
site 001EE   ; IN A,($DD)
site 001F8   ; OUT ($3F),A
site 001FA   ; IN A,($DD)
site 00203   ; OUT ($3F),A
site 00239   ; OUT ($BF),A
site 0023D   ; OUT ($BF),A
site 00244   ; OUT ($BF),A
site 00248   ; OUT ($BF),A
site 0028B   ; IN A,($DD)
site 002A9   ; IN A,($BF)
site 002C4   ; OUT ($BF),A
site 002C8   ; OUT ($BF),A
site 002D2   ; OUT ($BF),A
site 002D6   ; OUT ($BF),A
site 002DA   ; OUT ($BF),A
site 002DE   ; OUT ($BF),A
site 002EC   ; OUT ($BF),A
site 002F0   ; OUT ($BF),A
site 002F7   ; OUT ($BF),A
site 002FB   ; OUT ($BF),A
site 00968   ; OUT ($BE),A
site 00970   ; OUT ($BE),A
site 00CB2   ; OUT ($BE),A
site 00CBA   ; OUT ($BE),A
site 01A8C   ; OUT ($BE),A
site 01A94   ; OUT ($BE),A
site 01D23   ; OUT ($BE),A
site 01D35   ; OUTI
site 01D37   ; OUTI
site 01DA3   ; OUT ($BE),A
site 01DA8   ; OUT ($BE),A
site 01DE7   ; OUT ($DE),A
site 01DE9   ; IN A,($DC)
site 01DFC   ; IN A,($DD)
site 01E0D   ; OUT ($BE),A
site 01E14   ; OUT ($BE),A
site 020C8   ; OUT ($BE),A
site 020CE   ; OUT ($BE),A
site 02617   ; OUT ($BE),A
site 0263B   ; OUT ($BE),A
site 06C51   ; OUT ($BE),A
site 06C59   ; OUT ($BE),A
site 075F6   ; OUT ($BF),A
site 075F9   ; OUT ($BF),A
site 076CC   ; OUT ($BE),A
site 076D1   ; OUT ($BE),A
site 076D6   ; OUT ($BE),A
site 076DB   ; OUT ($BE),A
site 3C04C   ; OUT ($7F),A
site 3C057   ; OUT ($7F),A
site 3C062   ; OUT ($7F),A
site 3C18D   ; OUT ($F0),A
site 3C196   ; OUT ($F1),A
site 3C1AE   ; OUT ($7F),A
site 3C1BE   ; OUT (C),D
site 3C1C4   ; OUT ($F1),A
site 3C1E2   ; OUT ($F0),A
site 3C1F0   ; OUT ($F1),A
site 3C21A   ; OTIR
site 3C228   ; OTIR
site 3C232   ; OUT ($F0),A
site 3C238   ; OUT ($F1),A
site 3C244   ; OUTI
site 3C24A   ; OUTI
site 3C2A4   ; OUT ($7F),A
site 3C2A8   ; OUT ($7F),A
site 3C33D   ; OUT ($7F),A
site 3C341   ; OUT ($7F),A
site 3C369   ; OUT ($7F),A
site 3C36D   ; OUT ($7F),A
site 3C370   ; OUT ($7F),A
site 3C3D6   ; OUT ($F0),A
site 3C3DD   ; OUT ($F1),A
site 3C3E5   ; OUT ($F0),A
site 3C3EB   ; OUT ($F1),A
site 3C4D2   ; OUT ($F0),A
site 3C4DC   ; OUT (C),L
site 3C4E5   ; OUT ($F0),A
site 3C500   ; OUT (C),H
site 3C508   ; OUT ($F0),A
site 3C516   ; OUT ($F1),A
site 3C522   ; OUT ($F0),A
site 3C52B   ; OUT ($F1),A
site 3C700   ; OUT ($7F),A
site 3C75F   ; OUT ($7F),A
site 3C786   ; OUT ($7F),A
site 3C78B   ; OUT ($7F),A
site 3C7B7   ; OUT ($F0),A
site 3C7C5   ; OUT ($F1),A
site 3C7D3   ; OUT ($F0),A
site 3C7E7   ; OUT ($F0),A
site 3C87B   ; OUTI
site 3C87D   ; OUTI
site 3C87F   ; OUTI
site 3C881   ; OUTI
site 3C883   ; OUTI
site 3C885   ; OUTI
site 3C887   ; OUTI
site 3C889   ; OUTI
site 3C88B   ; OUTI
site 3C88D   ; OUTI
site 3C88F   ; OUTI
site 3C899   ; OUT (C),D
site 3C89F   ; OUT ($F1),A
site 3C8DE   ; OUT ($7F),A
site 3C934   ; OUT ($7F),A
site 3C973   ; OUT ($7F),A
site 3C9C6   ; OUT ($7F),A
site 3C9E6   ; OUT ($7F),A
site 3CA32   ; OUT ($7F),A
site 3CA3C   ; OUT ($7F),A
site 3CA84   ; OUT ($7F),A
mapst 00070   ; LD ($FFFD),A
mapst 00075   ; LD ($FFFE),A
mapst 00164   ; LD ($FFFF),A
mapst 00277   ; LD ($FFFF),A
mapst 00295   ; LD ($FFFF),A
mapst 01D4D   ; LD ($FFFF),A
mapst 01DC4   ; LD ($FFFF),A
# The line interrupt handler's per-line part at $D200 is copied from ROM
# $02E3-$02F4; its I/O (sites 002EC and 002F0 above) is patched in the ROM
# source. With the raster hook its interrupts are not delivered.
plain 002EC
plain 002F0
rastercode battle-out-run-raster.asm

# Battle Out Run (Europe, Brazil).cht, "Infinite Time": the time counter, held at $FF
poke "Infinite time"
ar 00C1-9FFF
endpoke

# Battle Out Run (Europe, Brazil).cht, "Infinite Nitro": the nitro counter, held at $20 (a full bar)
poke "Infinite nitro"
ar 00C2-E820
endpoke

# Battle Out Run (Europe, Brazil).cht, "Infinite Money": the savings word at $C2E5/$C2E6, held at $FFFF; spent in the tune-up shop
poke "Infinite money"
ar 00C2-E5FF
ar 00C2-E6FF
endpoke
