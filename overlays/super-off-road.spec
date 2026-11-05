# Super Off Road (Europe), CRC32 54F68C2A, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output with a reference I/O log
# of 600 s, then decided by hand.
#
# Decisions:
# - RST $10 is never executed and $0010-$0015 hold zero bytes, so $10 is the
#   io vector. $0016 stays as it is: the bank switch at $0050 (RST $18) ORs
#   it into the bank number.
# - Every high and medium confidence I/O site is kept. The reference log runs
#   $276F, $2774 and $27E6-$27FC, which static flow does not reach: $2581 ends
#   in a JP $D407 whose target the game writes at $2645, so the CALL $2753 at
#   $2572 is never followed.
# - The byte scan rows are not patched. $0008-$000E with $0091 (a VDP address
#   routine for RST $08) and $00E2-$0258 (a loader that polls $8002 and jumps
#   to $C000) are code that nothing runs: the start code at $0292 always
#   jumps to $0400, because $0007 holds $01, and the game has no RST $08
#   (verdict unused). $1453-$146E is a second ending of the text routine that
#   the JR $146F at $1451 jumps over, and $2801-$282A is a second form of the
#   name table writer $2732 that nothing calls (verdict unused). $0536 is in a
#   table of squares at $0520, $4EBC-$4EF3 in map bytes at $4EA0, and the
#   rows in banks 3, 5, 6 and 7 are in graphics data: these banks hold no
#   code (verdict false).
# - The race HUD box (8 by 3 cells) and the text of the shop screen have the
#   priority bit (name table writes at $144F and $20E7), so cars pass behind
#   the HUD as on a Master System: priority is on.
# - The race loop at $0FE1 waits one tick ($2501, on the frame counter $C295
#   that the interrupt handler counts) before each pass. A Master System
#   needs 2 to 4 ticks for a pass, the Next mostly 2, so without a hold
#   races run faster than on a Master System; the cave at $0295 holds the
#   pass to the Master System's rate.
name Super Off Road
cart 54F68C2A
hz 50		; No-Intro region Europe
vector 10 io
priority
asm 00276 2   ; IM 1 -> IM 2
    im 2
endasm

# The race loop's tick wait. A pass of the race loop (the wait, then the
# CALL $282B that swaps the words at $C4E0 and $C4E2 and writes the VDP, then
# the game's work) takes 2 to 4 ticks of 1/60 s on the reference, 2.9 on
# average: about 20.5 passes a second, and the race clock counts passes.
# Without the cave the Next runs a pass in 2.2 ticks at 50 Hz, 22.9 passes a
# second. The cave makes a pass last at least 2 and 3
# ticks in turn, 2.5 on average, 20 passes a second: a pass that ends up to
# 2 ticks late is made up by the next. $D7F0 (the tick the last pass was due
# to end) and $D7F1 (the turn) are in $D55A-$D8FF, RAM that the game did not
# write in a 600 s reference run. A target more than 3 ticks ahead is stale (the RAM held
# anything at power-on) and is dropped.
label wait_tick 02501
label race_wait 00295
asm 00FE4 3   ; CALL $2501 in the race loop
    call race_wait
endasm
asm 00295 56  ; NOP bytes after the JP NZ,$0400 at $0292, never run
    push bc
    ld a,($D7F1)
    inc a
    ld ($D7F1),a
    and 1
    add a,2
    ld b,a
    ld a,($D7F0)
    add a,b
    ld b,a              ; the tick this pass may end at
    call wait_tick      ; the game's own wait: the next tick
.next:
    ld a,($C295)
    sub b
    jp p,.done          ; at or past the target
    cp $FD
    jr c,.done          ; more than 3 ticks ahead: stale
    call wait_tick
    jr .next
.done:
    ld a,($C295)
    sub b
    cp 3
    ld a,b
    jr c,.keep          ; up to 2 ticks late: the next pass makes it up
    ld a,($C295)        ; later or stale: start again from now
.keep:
    ld ($D7F0),a
    pop bc
    ret
endasm
site 00047   ; IN A,($BF)
site 00049   ; IN A,($C1)
site 00286   ; IN A,($BF)
site 01348   ; OUT ($BF),A
site 0134D   ; OUT ($BF),A
site 01354   ; IN A,($BE)
site 0135B   ; IN A,($BE)
site 01367   ; OUT ($BF),A
site 0136C   ; OUT ($BF),A
site 01370   ; OUT ($BE),A
site 01377   ; OUT ($BE),A
site 0143C   ; OUT ($BF),A
site 01441   ; OUT ($BF),A
site 01445   ; OUT ($BE),A
site 0144F   ; OUT ($BE),A
site 014F1   ; IN A,($DC)
site 014FB   ; IN A,($DD)
site 017EE   ; OUT ($BF),A
site 017F2   ; OUT ($BF),A
site 017F6   ; OUT ($BF),A
site 017FA   ; OUT ($BF),A
site 01F93   ; OUT ($BF),A
site 01F98   ; OUT ($BF),A
site 01FAC   ; OUT ($BE),A
site 01FBA   ; OUT ($BF),A
site 01FBF   ; OUT ($BF),A
site 01FC3   ; OUT ($BE),A
site 01FCD   ; OUT ($BE),A
site 01FEC   ; OUT ($BF),A
site 01FF1   ; OUT ($BF),A
site 02000   ; OUT ($BE),A
site 02007   ; OUT ($BE),A
site 0209A   ; OUT ($BF),A
site 0209F   ; OUT ($BF),A
site 020A3   ; OUT ($BE),A
site 020B9   ; OUT ($BF),A
site 020BE   ; OUT ($BF),A
site 020C2   ; OUT ($BE),A
site 020C7   ; OUT ($BE),A
site 020D9   ; OUT ($BF),A
site 020DE   ; OUT ($BF),A
site 020E7   ; OUT ($BE),A
site 020F3   ; OUT ($BF),A
site 020F6   ; OUT ($BF),A
site 020FC   ; IN A,($BE)
site 02109   ; OUT ($BF),A
site 0210D   ; OUT ($BF),A
site 02113   ; OUT ($BE),A
site 02122   ; OUT ($BF),A
site 02126   ; OUT ($BF),A
site 0212B   ; OUT ($BE),A
site 0225D   ; OUT ($BF),A
site 02261   ; OUT ($BF),A
site 022BD   ; OUT ($BF),A
site 022C0   ; OUT ($BF),A
site 022DD   ; OUT ($BE),A
site 022E8   ; OUT ($BE),A
site 02300   ; OUT ($BF),A
site 02303   ; OUT ($BF),A
site 0245D   ; OUT ($BF),A
site 02461   ; OUT ($BF),A
site 02470   ; OUT ($BE),A
site 02477   ; OUT ($BE),A
site 02483   ; OUT ($BF),A
site 02487   ; OUT ($BF),A
site 0248D   ; OUT ($BE),A
site 02492   ; OUT ($BE),A
site 0250F   ; IN A,($BF)
site 0251D   ; IN A,($DD)
site 026B0   ; OUT ($BF),A
site 026B5   ; OUT ($BF),A
site 026C6   ; OUT ($BE),A
site 026CC   ; OUT ($BE),A
site 026D1   ; OUT ($BE),A
site 026D8   ; OUT ($BE),A
site 026DF   ; OUT ($BE),A
site 026E6   ; OUT ($BE),A
site 026ED   ; OUT ($BE),A
site 026F4   ; OUT ($BE),A
site 026FB   ; OUT ($BE),A
site 02702   ; OUT ($BE),A
site 0270A   ; OUT ($BE),A
site 02711   ; OUT ($BE),A
site 02717   ; OUT ($BE),A
site 0271E   ; OUT ($BE),A
site 02725   ; OUT ($BE),A
site 0272D   ; OUT ($BE),A
site 0273C   ; OUT ($BE),A
site 02744   ; OUT ($BE),A
site 02749   ; OUT ($BE),A
site 0274E   ; OUT ($BE),A
site 0276F   ; OUT ($BF),A
site 02774   ; OUT ($BF),A
site 0278C   ; OUT ($BE),A
site 02793   ; OUT ($BE),A
site 0279B   ; OUT ($BE),A
site 027A2   ; OUT ($BE),A
site 027AA   ; OUT ($BE),A
site 027B1   ; OUT ($BE),A
site 027B8   ; OUT ($BE),A
site 027BF   ; OUT ($BE),A
site 027C8   ; OUT ($BE),A
site 027CF   ; OUT ($BE),A
site 027D7   ; OUT ($BE),A
site 027DE   ; OUT ($BE),A
site 027E6   ; OUT ($BE),A
site 027ED   ; OUT ($BE),A
site 027F4   ; OUT ($BE),A
site 027FC   ; OUT ($BE),A
site 0284D   ; OUT ($BF),A
site 02851   ; OUT ($BF),A
site 0286D   ; OUT ($BE),A
site 02878   ; OUT ($BE),A
site 02891   ; OUT ($BE),A
site 02896   ; OUT ($BE),A
site 0289D   ; OUT ($BE),A
site 028A2   ; OUT ($BF),A
site 028A6   ; OUT ($BF),A
site 028C4   ; OUT ($BE),A
site 028CC   ; OUT ($BE),A
site 028D6   ; OUT ($BE),A
site 028DD   ; OUT ($BE),A
site 028FA   ; OUT ($BE),A
site 02903   ; OUT ($BE),A
site 0290A   ; OUT ($BE),A
site 02911   ; OUT ($BE),A
site 02CC7   ; OUT ($BF),A
site 02CCA   ; OUT ($BF),A
site 02CED   ; IN A,($BE)
site 02CF8   ; IN A,($BE)
site 02D02   ; IN A,($BE)
site 02D0E   ; IN A,($BE)
site 038D1   ; OUT ($BF),A
site 038D6   ; OUT ($BF),A
site 0390C   ; OUT ($BE),A
site 03914   ; OUT ($BE),A
site 03A4E   ; OUT ($BF),A
site 03A52   ; OUT ($BF),A
site 03A57   ; OUT ($BE),A
site 03F67   ; OUT ($BE),A
site 03F73   ; OUT ($BE),A
site 03F92   ; OUT ($BE),A
site 03F9F   ; OUT ($BE),A
site 03FC0   ; OUT ($BF),A
site 03FC5   ; OUT ($BF),A
site 04334   ; OUT ($BF),A
site 04338   ; OUT ($BF),A
site 04396   ; OUT ($BF),A
site 04399   ; OUT ($BF),A
site 043A3   ; OUT ($BE),A
site 047CB   ; OUT ($7F),A
site 04834   ; OUT ($7F),A
site 0484A   ; OUT ($7F),A
site 0485A   ; OUT ($7F),A
site 04861   ; OUT ($7F),A
site 0492D   ; OUT ($7F),A
site 0493F   ; OUT ($7F),A
mapst 00055   ; LD ($FFFF),A
mapst 00255   ; LD ($FFFF),A
mapst 00278   ; LD ($FFFC),A
mapst 0027B   ; LD ($FFFD),A
mapst 0027F   ; LD ($FFFE),A
mapst 00283   ; LD ($FFFF),A

# Super Off Road (Europe).cht, "Infinite Nitros - Both Players": the patch at $340E stops the
# nitro count from going down (a Game Genie code, bank 0)
poke "Infinite nitros"
gg 004-0EC-3BE
endpoke

# Super Off Road (Europe) (Action Replay).cht, "Infinite Credits": RAM $D065 is the credit count,
# held at 99. The Game Genie form (00D-34E-3BE, $1D34) stops only the decrement at the end of a
# race, not the one when the shop continue spends a credit ($41B9).
poke "Infinite credits"
ar 00D0-6563
endpoke

# Super Off Road (Europe).cht, "Infinite Money - Both Players": the patch at $41F4 stops a
# purchase from taking cash (bank 1)
poke "Infinite money"
gg 7E1-F4B-3B7
endpoke

# Super Off Road (Europe).cht, "P1 Max Accel Upgrade", "P1 Max Tires Upgrade",
# "P1 Max Top Spd Upgrade" and "P1 Max Shocks Upgrade": RAM $C110, $C10F, $C112 and $C111 are
# player 1's upgrade levels, 8 at the top
poke "Max upgrades P1"
ar 00C1-1008
ar 00C1-0F08
ar 00C1-1208
ar 00C1-1108
endpoke

# Super Off Road (Europe).cht, "Start with ?? Credits, instead of 2 - Both Players": the byte
# at $3F2B is the credit count at the start of a game
poke "Start credits"
gg ??F-2BC-E62
endpoke

# Super Off Road (Europe).cht, "Start with ?? Nitros, instead of 25 - Both Players": the byte
# at $062F is the nitro count at the start of a game
poke "Start nitros"
gg ??6-2FF-80E
endpoke
