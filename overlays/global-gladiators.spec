# Global Gladiators (Europe, Brazil) (En), CRC32 B67CEB76, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
#
# Drafted by tools/mkspec.py from the sitescan output with a 600 s reference I/O log, then
# decided by hand. The game is built like Cool Spot (cool-spot.spec): the same frame routine,
# sprite band multiplexer, seam at lines 152-159 and PAL test, at other addresses.
#
# Decisions:
# - No free RST vector: $0000-$0002 (DI; IM 1) becomes the io vector, and the game starts at
#   $0003 (JP $0092). The game has no RST $00 and no jump to $0000 of its own.
# - The interrupt handler at $0038 jumps through the word at $D0D1: $0040 (power-on), $3B35
#   (play), $4FC9 (the title and the other screens with sprite bands), $50CF (the intro
#   pictures and the credits) and $5240.
# - Sprites are multiplexed: the frame routine $3BA3 hides all 32 sprites ($3C2D writes $C0
#   to each Y) and writes the sprites of bands 0-2 ($3C06), and each line interrupt (every 8
#   lines) writes the next 8-line band into the next 8 of the 32 slots ($3B77: CALL $03FA).
#   The bands are lists of $40 bytes from ($D0C6) (count, 16 Y, 16 X and tile pairs). The
#   Next draws the sprites from the sprite table once a frame, after the hide, and showed
#   none: no Mick, no score numbers, no snow. Page 0 sprsat writes the sprite table once a
#   frame at $3C06 with the sprites of all 25 bands, with the same choice of sprites as $03FA
#   for a band of more than 8 (by $D0C2 bit 0); the hide and the line interrupts' band writes
#   are taken out. Slots 32-63 are the status bar's own sprites and stay as the game writes
#   them, so sprsat fills slots 0-31.
# - In play the line handler turns the display off at the line 151 event ($187F) and on at
#   the line 159 event ($1892), over the seam between the play area and the status bar; a
#   Master System shows lines 152-159 black. As in Cool Spot, the display-off write is
#   replaced with page 0 clipof (clip windows from line 160 and a black fallback colour), and
#   the 8 NOPs before the display-on write call r10off: clipon, then register 10 = $FF, so no
#   line event comes after line 159 and a late one at line 191 cannot make the frame event
#   late. The frame routine's call of the hide ($3BA7) calls r10on: clipon, then register
#   10 = 7 again when r10off set it to $FF.
# - The tile writers $0374, $039A and $1A3A wait while the V counter is $88-$9F before each
#   write, then write with interrupts off. Each wait calls vwin, in the assembler text left
#   at $0044-$0065, which waits only while interrupts are on.
# - $00C8 tells PAL from NTSC by counting a loop of V counter reads over one frame: 2100
#   passes or more is PAL ($DECB = 0), fewer NTSC ($FF). Through the runtime's traps the
#   loop counts far fewer. The DEC A at $00E1 is taken out: $DECB is 0, as on a PAL Master
#   System. A reference on sg1000m3 (NTSC) needs NM_POKEW=DECB:FF:0.
# - $0103 is a delay loop (DEC BC until 0, 26 cycles a pass); $0109 runs it E times with
#   BC = 0, and the intro pictures run it with BC = $FFFF between steps. On the Next it ran
#   about 8 times faster: the Virgin logo did not show and the intro ran at twice the pace.
#   Page 0 delay waits the same time on the Next's line counter: BC x 26 / 228 lines (BC/8 -
#   BC/128), 7475 lines for BC = 0.
# - The credits (handler $50CF) set colour 15 and register 8 at each 8-line event, one pair
#   a text row. The event's traps put the colour change about 5 lines into the row, and the
#   letters showed two colours and two H scroll values. Page 0 rowev (at $50DE) writes the
#   next row's pair at the line before it, the colour directly into the palette; rowfr (at
#   $50FD) writes the first pair in the frame path. hsplit is not needed for it, and with
#   hsplit on the play screen lost its V scroll wrap.
# - The sprite writer $0336 (Y at $3F00 + B, then X and tile at $3F80 + 2B) and the palette
#   writer $02C7 send the VDP address as two control writes. The main loop calls both with
#   interrupts on, and the frame handler reads the status port at $003A, which clears the
#   control latch. On the Next an interrupt that comes during the first write's trap is taken
#   as the trap returns, between the two writes. The second byte then starts a new address
#   with the old code: after a palette fade the Options screen's first letter wrote its Y
#   ($30) into colour 31 (code 3, address $7F), and the menu text showed blue. Page 0 sprw
#   writes the whole sprite with jt_vwrite, which sets its own address for each run, and
#   cramw does the whole palette write. Their caves turn interrupts off before the far call
#   and back on after it: the game's stack is just above the sound driver's variables
#   ($DF94-$DFA6), and the frame handler taken on the far call's frame wrote $DFA6, which
#   stopped the driver and hung the game at $54C3 after Start. $1A4C already calls $0336
#   between DI and EI.
name Global Gladiators
cart B67CEB76
hz 50		; No-Intro regions Europe, Brazil

# Mick _ Mack as the Global Gladiators (Europe) (Action Replay).cht, "Infinite Lives"
# (Global Gladiators (Europe, Brazil).cht has 00D0-B903, which holds 3): RAM $D0B9 is the
# lives left. The game starts with 5; held at 9 the HUD shows 9
poke "Infinite lives"
ar 00D0-B909
endpoke

# Global Gladiators (Europe, Brazil).cht, "Infinite Energy": RAM $D0BA is the energy bar,
# $3F is full; each hit takes 8
poke "Infinite energy"
ar 00D0-BA3F
endpoke

# Global Gladiators (Europe, Brazil).cht, "Invulnerability": RAM $D506 is the hit timer;
# held at $2C a hit takes no energy
poke "Invincibility"
ar 00D5-062C
endpoke

# Global Gladiators (Europe, Brazil).cht, "Freeze Timer": RAM $D4EA is the clock's tick
# counter; held at $3C the clock stops, and with it the time-out that costs a life
poke "Infinite time"
ar 00D4-EA3C
endpoke

# Global Gladiators (Europe, Brazil).cht, "Infinite "M"'s": RAM $D503 is the M token count
# (BCD) that the HUD shows; held at 99 the HUD shows 99
poke "Max M tokens"
ar 00D5-0399
endpoke

# Global Gladiators (Europe, Brazil).cht, "Each M icon counts as ??": the Game Genie patch
# writes $02 at cart offset $3033, where the game has $01. Each M icon adds 2 to the token
# count
poke "Double M tokens"
gg 020-33C-E6E
endpoke

# Global Gladiators (Europe, Brazil).cht, "Enable Cheats Menu": the Game Genie patch writes $1A
# at cart offset $543E, where the game has $01. The Options screen gets a Cheats! entry
# with Lives, Shield and Level rows, which the player sets in the game
poke "Cheats menu"
gg 1A4-3EA-E6E
endpoke

vector 00 io
start 0003
asm 000E1 1   ; DEC A: the NTSC result of the frame count (see the header)
endasm
asm 00103 6   ; DEC BC; LD A,B; OR C; JR NZ,$0103; RET: the delay loop
    rst $00
    db far_io, pg_sprsat, ent_delay
    ret
endasm
label vwin 00044
asm 00044 19  ; assembler text after the frame handler's RET: vwin
; vwin: A = the V counter. Z: write now; NZ: wait. The game's window ($88-$9F) applies only
; while interrupts are on (IFF2 from LD A,I). Changes A and F; the callers' POP AF follow.
    cp $88
    jr c,vgo
    cp $A0
    jr nc,vgo
    ld a,i
    jp pe,vwait
vgo:
    cp a
    ret
vwait:
    ld a,1
    or a
    ret
endasm
asm 0037A 8   ; CP $88; JR C; CP $A0; JR C,$0378: the wait through vwin
    call vwin
    jr nz,$0378
endasm
asm 003BF 8   ; CP $88; JR C; CP $A0; JR C,$03BD: the wait through vwin
    call vwin
    jr nz,$03BD
endasm
asm 01A42 8   ; CP $88; JR C; CP $A0; JR C,$1A40: the wait through vwin
    call vwin
    jr nz,$1A40
endasm
label r10off 07FD3
label r10on 07FD8
asm 07FD3 10  ; zero bytes before the cart header (slot 1 always holds bank 1)
    rst $00
    db far_io, pg_sprsat, ent_p10off
    ret
    rst $00
    db far_io, pg_sprsat, ent_p10on
    ret
endasm
asm 0187F 8   ; LD A,$A0; OUT ($BF),A; LD A,$81; OUT ($BF),A: the display off at line 151
    rst $00
    db far_io, pg_sprsat, ent_clipof
endasm
asm 0188A 8   ; the 8 NOPs before the display-on write of line 159
    call r10off
endasm
asm 050DE 27  ; 4 NOPs, then the line event's writes of colour 15 and register 8 (see rowev)
    rst $00
    db far_io, pg_sprsat, ent_rowev
endasm
asm 050FD 9   ; LD HL,($D4FF); LD ($D501),HL; JP $50E2: the frame's first pair (see rowfr)
    rst $00
    db far_io, pg_sprsat, ent_rowfr
    jp $50F9
endasm
asm 03BA7 3   ; CALL $3C2D: the hide of all 32 sprites; sprsat writes the whole table
    call r10on
endasm
asm 03B77 3   ; CALL $03FA: a line interrupt's band; sprsat has written every band
endasm
asm 002C7 14  ; XOR A ... POP HL: the palette write, 16 bytes to colours 0-15 and 16-31 (see cramw)
    ld a,i
    di
    rst $00
    db far_io, pg_sprsat, ent_cramw
    ret nc
    ei
    ret
endasm
asm 00336 45  ; LD H,C ... RET: the sprite writer (see sprw)
    ld a,i
    di
    rst $00
    db far_io, pg_sprsat, ent_sprw
    ret nc
    ei
    ret
endasm
asm 03C06 39  ; XOR A ... JP $03ED: bands 0-2 into slots $18, $10 and $08
    rst $00
    db far_io, pg_sprsat, ent_sprsat
    ret
endasm
site 0003A   ; IN A,($BF)
site 000D0   ; IN B,(C)
site 000D5   ; IN B,(C)
site 000EC   ; OTIR
site 000F5   ; IN A,($DD)
site 00113   ; IN A,($7E)
site 00124   ; IN A,($DC)
site 00132   ; IN A,($DD)
site 0028C   ; OUT ($BF),A
site 00290   ; OUT ($BF),A
site 00296   ; OUT ($BE),A
site 0029F   ; OUT ($BF),A
site 002A3   ; OUT ($BF),A
site 002A9   ; OUT ($BE),A
site 002B5   ; OUT (C),A
site 002B9   ; OUT (C),A
site 002BE   ; OUT (C),A
site 002D7   ; OUTI
site 002E1   ; OUT ($BF),A
site 002E6   ; OUT ($BF),A
site 002EB   ; OUTI
site 002F9   ; OUT (C),L
site 002FB   ; OUT (C),H
site 0030F   ; OUTI
site 0031D   ; OUT ($BF),A
site 00320   ; OUT ($BF),A
site 00322   ; OUTI
site 0032D   ; OUTI
site 00368   ; OUT (C),E
site 0036A   ; OUT (C),D
site 0036F   ; OUT (C),A
site 00378   ; IN A,($7E)
site 00384   ; OUT (C),E
site 00386   ; OUT (C),D
otir 00389   ; OUTI
site 0043A   ; OUT (C),A
site 0043E   ; OUT (C),A
site 00441   ; OUTI
site 00446   ; OUTI
site 0044B   ; OUTI
site 00450   ; OUTI
site 00455   ; OUTI
site 0045A   ; OUTI
site 0045F   ; OUTI
site 00464   ; OUTI
site 0046C   ; OUT (C),A
site 00470   ; OUT (C),A
site 00473   ; OUTI
site 00478   ; OUTI
site 0047D   ; OUTI
site 00482   ; OUTI
site 00487   ; OUTI
site 0048C   ; OUTI
site 00491   ; OUTI
site 00496   ; OUTI
site 0049B   ; OUTI
site 004A0   ; OUTI
site 004A5   ; OUTI
site 004AA   ; OUTI
site 004AF   ; OUTI
site 004B4   ; OUTI
site 004B9   ; OUTI
site 004BE   ; OUTI
site 004C9   ; OUTI
site 004CC   ; OUT (C),A
site 004DE   ; OUT ($BF),A
site 004E2   ; OUT ($BF),A
site 004E8   ; OUT ($BF),A
site 004EC   ; OUT ($BF),A
site 004F2   ; OUT ($BF),A
site 004F6   ; OUT ($BF),A
site 0050B   ; OUT ($BF),A
site 0050F   ; OUT ($BF),A
site 005A5   ; OUT ($BF),A
site 005A9   ; OUT ($BF),A
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
site 005C6   ; OUTI
site 005C8   ; OUTI
site 005CA   ; OUTI
site 005CC   ; OUTI
site 005CE   ; OUTI
site 005D0   ; OUTI
site 005D2   ; OUTI
site 005D4   ; OUTI
site 005D6   ; OUTI
site 005D8   ; OUTI
site 005DA   ; OUTI
site 005DC   ; OUTI
site 005DE   ; OUTI
site 005E0   ; OUTI
site 005E2   ; OUTI
site 005E4   ; OUTI
site 005E6   ; OUTI
site 005E8   ; OUTI
site 005EA   ; OUTI
site 005EC   ; OUTI
site 005EE   ; OUTI
site 00688   ; OUT ($BF),A
site 0068D   ; OUT ($BF),A
site 0069D   ; OUT (C),A
site 006A6   ; OUT (C),A
site 006E6   ; OUT (C),L
site 006E8   ; OUT (C),H
site 006EF   ; OUTI
site 006F5   ; OUTI
site 00709   ; OUT (C),L
site 0070B   ; OUT (C),H
site 0071F   ; OUTI
site 0072D   ; OUT ($BF),A
site 00730   ; OUT ($BF),A
site 00732   ; OUTI
site 0073D   ; OUTI
site 0077A   ; OUT (C),E
site 0077C   ; OUT (C),D
site 0077F   ; OUTI
site 0078F   ; OUT (C),A
site 00791   ; OUT (C),D
site 00794   ; OUTI
site 007BF   ; OUT (C),E
site 007C1   ; OUT (C),D
site 007C4   ; OUTI
site 010A4   ; OUT ($BF),A
site 010A8   ; OUT ($BF),A
site 01894   ; OUT ($BF),A
site 01898   ; OUT ($BF),A
site 01A40   ; IN A,($7E)
site 03B39   ; IN A,($7E)
site 03C2E   ; OUT ($BF),A
site 03C32   ; OUT ($BF),A
site 03C36   ; OUT ($BE),A
site 03C38   ; OUT ($BE),A
site 03C3A   ; OUT ($BE),A
site 03C3C   ; OUT ($BE),A
site 03C3E   ; OUT ($BE),A
site 03C40   ; OUT ($BE),A
site 03C42   ; OUT ($BE),A
site 03C44   ; OUT ($BE),A
site 03C46   ; OUT ($BE),A
site 03C48   ; OUT ($BE),A
site 03C4A   ; OUT ($BE),A
site 03C4C   ; OUT ($BE),A
site 03C4E   ; OUT ($BE),A
site 03C50   ; OUT ($BE),A
site 03C52   ; OUT ($BE),A
site 03C54   ; OUT ($BE),A
site 03C56   ; OUT ($BE),A
site 03C58   ; OUT ($BE),A
site 03C5A   ; OUT ($BE),A
site 03C5C   ; OUT ($BE),A
site 03C5E   ; OUT ($BE),A
site 03C60   ; OUT ($BE),A
site 03C62   ; OUT ($BE),A
site 03C64   ; OUT ($BE),A
site 03C66   ; OUT ($BE),A
site 03C68   ; OUT ($BE),A
site 03C6A   ; OUT ($BE),A
site 03C6C   ; OUT ($BE),A
site 03C6E   ; OUT ($BE),A
site 03C70   ; OUT ($BE),A
site 03C72   ; OUT ($BE),A
site 03C74   ; OUT ($BE),A
site 0473A   ; OUT ($BF),A
site 0473E   ; OUT ($BF),A
site 04741   ; OUT ($BE),A
site 04744   ; OUT ($BE),A
site 047D8   ; OUT (C),E
site 047DA   ; OUT (C),D
site 047DD   ; OUTI
site 047DF   ; OUTI
site 047E1   ; OUTI
site 047E3   ; OUTI
site 047E5   ; OUTI
site 047E7   ; OUTI
site 047E9   ; OUTI
site 047EB   ; OUTI
site 047ED   ; OUTI
site 047EF   ; OUTI
site 047F1   ; OUTI
site 047F3   ; OUTI
site 047F5   ; OUTI
site 047F7   ; OUTI
site 047F9   ; OUTI
site 047FB   ; OUTI
site 047FD   ; OUTI
site 047FF   ; OUTI
site 04801   ; OUTI
site 04803   ; OUTI
site 04805   ; OUTI
site 04807   ; OUTI
site 04809   ; OUTI
site 0480B   ; OUTI
site 0480D   ; OUTI
site 0480F   ; OUTI
site 04811   ; OUTI
site 04813   ; OUTI
site 04815   ; OUTI
site 04817   ; OUTI
site 04819   ; OUTI
site 0481B   ; OUTI
site 04FCD   ; IN A,($7E)
site 04FFB   ; OUT ($BF),A
site 05000   ; OUT ($BF),A
site 05015   ; OUT ($BE),A
site 05020   ; OUT ($BE),A
site 0502E   ; OUT ($BF),A
site 05033   ; OUT ($BF),A
site 05036   ; OUT ($BE),A
site 05040   ; OUT ($BE),A
site 050D3   ; IN A,($7E)
site 05138   ; OUT (C),E
site 0513A   ; OUT (C),D
site 0513F   ; OUTI
site 05154   ; OUT (C),E
site 05158   ; OUT (C),D
site 07FB9   ; OUT (C),D
site 07FBF   ; OUT (C),E
site 07FC5   ; OUT (C),H
site 07FCB   ; OUT (C),L
site 38013   ; OUT ($7F),A
site 38017   ; OUT ($7F),A
site 38024   ; OUT ($7F),A
site 38028   ; OUT ($7F),A
site 38064   ; OUT ($7F),A
site 3807B   ; OUT ($7F),A
site 3808F   ; OUT ($7F),A
site 3809E   ; OUT ($7F),A
site 380B5   ; OUT ($7F),A
site 380C9   ; OUT ($7F),A
site 380F6   ; OUT ($7F),A
site 38109   ; OUT ($7F),A
site 38120   ; OUT ($7F),A
site 38126   ; OUT ($7F),A
site 3814A   ; OUT ($7F),A
site 38161   ; OUT ($7F),A
site 38175   ; OUT ($7F),A
site 381D2   ; OUT ($7F),A
site 383BB   ; OUT ($7F),A
site 383C0   ; OUT ($7F),A
site 383D4   ; OUT ($7F),A
site 383E7   ; OUT ($7F),A
site 383F3   ; OUT ($7F),A
site 38406   ; OUT ($7F),A
mapst 00A96   ; LD ($FFFF),A
mapst 01088   ; LD ($FFFF),A
mapst 01297   ; LD ($FFFF),A
mapst 01565   ; LD ($FFFF),A
mapst 01589   ; LD ($FFFF),A
mapst 0189F   ; LD ($FFFF),A
mapst 01AEB   ; LD ($FFFF),A
mapst 02749   ; LD ($FFFF),A
mapst 029FE   ; LD ($FFFF),A
mapst 02B37   ; LD ($FFFF),A
mapst 03AB7   ; LD ($FFFF),A
mapst 03BFB   ; LD ($FFFF),A
mapst 03C02   ; LD ($FFFF),A
mapst 03F4A   ; LD ($FFFF),A
mapst 04061   ; LD ($FFFF),A
mapst 041DC   ; LD ($FFFF),A
mapst 04216   ; LD ($FFFF),A
mapst 042BA   ; LD ($FFFF),A
mapst 043A4   ; LD ($FFFF),A
mapst 045CD   ; LD ($FFFF),A
mapst 04642   ; LD ($FFFF),A
mapst 04669   ; LD ($FFFF),A
mapst 046F8   ; LD ($FFFF),A
mapst 04717   ; LD ($FFFF),A
mapst 0474C   ; LD ($FFFF),A
mapst 04786   ; LD ($FFFF),A
mapst 047B3   ; LD ($FFFF),A
mapst 047D2   ; LD ($FFFF),A
mapst 048F9   ; LD ($FFFF),A
mapst 04A67   ; LD ($FFFF),A
mapst 04C30   ; LD ($FFFF),A
mapst 04E26   ; LD ($FFFF),A
mapst 04E2E   ; LD ($FFFF),A
mapst 04E3E   ; LD ($FFFF),A
mapst 04E46   ; LD ($FFFF),A
mapst 04E50   ; LD ($FFFF),A
mapst 04E57   ; LD ($FFFF),A
mapst 04E61   ; LD ($FFFF),A
mapst 04E68   ; LD ($FFFF),A
mapst 04E72   ; LD ($FFFF),A
mapst 04E79   ; LD ($FFFF),A
mapst 04FDA   ; LD ($FFFF),A
mapst 05073   ; LD ($FFFF),A
mapst 05115   ; LD ($FFFF),A
mapst 0514F   ; LD ($FFFF),A
mapst 0581B   ; LD ($FFFF),A
mapst 0039D   # LD ($FFFF),A; after LD A,(IX+$06); 32 bytes of valid code before it
site 003BD   ; IN A,($7E)
site 003C9   ; OUT (C),E
site 003CB   ; OUT (C),D
otir 003CE   ; OUTI
mapst 0039D   ; LD ($FFFF),A

page 0 sprsat clipof clipon p10off p10on delay rowfr rowev sprw cramw
    OPT --zxnext        ; NEXTREG
; sprsat: the sprite table of a frame in one write. Does what $3C06-$3C2C leaves in RAM
; ($D0C3 = $08, $D0C8 = ($D0C6) + $80), then takes the bands of the list at ($D0C6): 25
; bands of $40 bytes, each a count n (0 to 16), 16 Y bytes and 16 X and tile pairs. A band of
; n <= 8 gives sprites 0 to n-1; for n > 8, $03FA gives sprites 0-7 when $D0C2 bit 0 is
; clear, else sprites 0 to 15-n and 8 to n-1. The sprites go in band order into slots 0-31;
; the slots left over get Y $E0 (below the picture). A Y of $D0 from a band is written as $E0,
; so that it does not end the table before the status bar's slots 32-63. jt_vwrite writes the
; Y bytes to $3F00 and the X and tile bytes to $3F80. Runs inside the frame handler, with
; interrupts off, on its own stack. Changes A, F, BC, DE and HL, as the code it replaces does.
sprsat: ld (sv_sp),sp
        ld sp,stk_top
        ld a,8
        ld ($D0C3),a
        ld hl,($D0C6)
        ld de,$0080
        add hl,de
        ld ($D0C8),hl
        ld a,($D0C2)
        and 1
        ld (par),a
        xor a
        ld (cnt),a
        ld hl,($D0C6)
        ld b,25
band:   push bc
        push hl
        ld a,(hl)
        or a
        jr z,bnext
        inc hl                  ; HL = Y of sprite 0
        cp 9
        jr nc,big
        ld b,a                  ; n <= 8: sprites 0 to n-1
        ld e,0
        call copy
        jr bnext
big:    ld c,a
        ld a,(par)
        or a
        jr nz,odd
        ld b,8                  ; sprites 0-7
        ld e,0
        call copy
        jr bnext
odd:    ld a,16
        sub c
        ld b,a                  ; sprites 0 to 15-n
        ld e,0
        call copy
        ld a,c
        sub 8
        ld b,a                  ; sprites 8 to n-1
        ld e,8
        call copy
bnext:  pop hl
        ld de,$0040
        add hl,de
        pop bc
        djnz band
        ld a,(cnt)
        ld e,a
        ld d,0
        ld hl,ybuf
        add hl,de
hide:   cp 32
        jr nc,full
        ld (hl),$E0             ; an unused slot: below the picture
        inc hl
        inc a
        jr hide
full:   push ix
        push iy
        ld ix,0
        ld iy,0
        ld hl,ybuf
        ld de,$3F00
        ld bc,32*256+1          ; 1 run of 32 bytes
        ld a,1                  ; the source in this page
        call jt_vwrite
        ld hl,xbuf
        ld de,$3F80
        ld bc,64*256+1          ; 1 run of 64 bytes
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        ld sp,(sv_sp)
        ret

; copy: B sprites from index E of the band whose Y bytes start at HL, into the table, while
; it holds fewer than 32. Keeps HL.
copy:   ld a,b
        or a
        ret z
        push hl
        ld d,0
        add hl,de               ; HL = Y of sprite E
        push hl
        ld a,e
        add a,16
        ld e,a
        add hl,de               ; X of sprite E: Y0 + 16 + 2E
        ld (xsrc),hl
        pop hl
cloop:  ld a,(cnt)
        cp 32
        jr nc,cdone
        ld e,a
        ld d,0
        push hl
        ld hl,ybuf
        add hl,de
        ex de,hl
        pop hl
        ld a,(hl)
        cp $D0
        jr nz,yok
        ld a,$E0                ; not the end of the table
yok:    ld (de),a               ; Y
        inc hl
        push hl
        ld a,(cnt)
        add a,a
        ld e,a
        ld d,0
        ld hl,xbuf
        add hl,de
        ex de,hl
        ld hl,(xsrc)
        ld a,(hl)
        ld (de),a               ; X
        inc hl
        inc de
        ld a,(hl)
        ld (de),a               ; tile
        inc hl
        ld (xsrc),hl
        ld hl,cnt
        inc (hl)
        pop hl
        djnz cloop
cdone:  pop hl
        ret

; p10off: from the line 159 event, after clipon: register 10 = $FF, so no line event comes
; in the rest of the picture. p10on: from the frame routine, after clipon: register 10 = 7
; again when p10off set it. Both write register 10 through OUT (C),A to port $BF. Keep every
; register but A and F.
p10off: call clipon
        ld a,1
        ld (r10f),a
        ld a,$FF
        jr r10w
p10on:  call clipon
        ld a,(r10f)
        or a
        ret z
        xor a
        ld (r10f),a
        ld a,7
r10w:   push bc
        ld c,$BF
        rst $00
        db $79                  ; OUT (C),A
        ld a,$8A
        rst $00
        db $79                  ; OUT (C),A: register 10
        pop bc
        ret

; delay: in place of the loop at $0103 (DEC BC until 0, 26 cycles a pass at 3.55 MHz, 228
; cycles a line). Waits BC x 26 / 228 lines (BC/8 - BC/128) on the Next's line counter, 7475
; lines for BC = 0, then returns BC = 0, A = 0 and Z, as the loop does. Lines are counted from
; the 9-bit line number (NextRegs $1E and $1F) modulo 311 (the 50 Hz frame), so interrupts
; taken during the wait still count. Keeps DE, HL and the interrupt state.
delay:  push hl
        push de
        ld h,b
        ld l,c
        ld a,h
        or l
        jr nz,d_n
        ld hl,7475
        jr d_go
d_n:    srl h
        rr l
        srl h
        rr l
        srl h
        rr l                    ; HL = BC/8
        ld d,h
        ld e,l
        srl d
        rr e
        srl d
        rr e
        srl d
        rr e
        srl d
        rr e                    ; DE = BC/128
        or a
        sbc hl,de
d_go:   ld a,h
        or l
        jr z,d_x
        ld (left),hl
        call rdln
        ld (lprev),hl
d_lp:   call rdln
        ld de,(lprev)
        ld (lprev),hl
        or a
        sbc hl,de               ; the lines since the last read
        jr nc,d_pos
        ld de,311
        add hl,de
d_pos:  ex de,hl
        ld hl,(left)
        or a
        sbc hl,de
        jr c,d_x
        jr z,d_x
        ld (left),hl
        jr d_lp
d_x:    pop de
        pop hl
        ld bc,0
        xor a
        ret

; rowfr, rowev: the credits screen (handler $50CF) sets colour 15 and register 8 for each
; 8-line text row from a list of pairs at ($D4FF): the frame path writes pair 0 and line
; event j (at line 8j - 1 on a Master System) writes pair j, so the colour changes at line 8j.
; On the Next the event's status read, V counter read and three CRAM traps put the colour
; change about 5 lines into the row, in the middle of the letters. So each event j writes
; pair j + 1 instead, directly into the first tilemap palette and cram when the Next reaches
; line 8j + 7, and register 8 through the runtime after it. Event 1 also writes pair 1 at
; once (nothing comes before it). ($D501) is kept as the game keeps it, the next pair. Runtime
; internal used: cram. Both keep every register; interrupts are off in the handler.
rowfr:  push af
        push bc
        push de
        push hl
        xor a
        ld (evn),a
        ld hl,($D4FF)
        call rpair
        ld a,1
        ld (nxt),a
        jr row_x
rowev:  push af
        push bc
        push de
        push hl
        ld hl,evn
        inc (hl)
        ld a,(nxt)
        cp (hl)
        jr nz,re_ahead
        call rpairn             ; pair j not written yet: now
re_ahead:
        ld a,(evn)
        cp 23
        jr nc,row_x             ; the last event: no row below it
        add a,a
        add a,a
        add a,a
        add a,7
        ld e,a                  ; E = 8j + 7
re_w:   call rdln
        ld a,h
        or a
        jr nz,re_go
        ld a,l
        cp e
        jr nc,re_go             ; at the line or past it
        ld a,e
        sub l
        cp 9
        jr c,re_w               ; up to 8 lines early: wait
re_go:  call rpairn
row_x:  pop hl
        pop de
        pop bc
        pop af
        ret

; rpairn: write pair nxt of the list. rpair: write the pair at HL. Both leave nxt + 1 and
; ($D501) at the pair after it.
rpairn: ld a,(nxt)
        ld l,a
        ld h,0
        add hl,hl
        ld de,($D4FF)
        add hl,de
rpair:  ld a,(hl)
        inc hl
        push hl
        call setc15
        pop hl
        ld a,(hl)
        inc hl
        ld ($D501),hl
        ld c,$BF
        rst $00
        db $79                  ; OUT (C),A
        ld a,$88
        rst $00
        db $79                  ; OUT (C),A: register 8
        ld hl,nxt
        inc (hl)
        ret

; setc15: SMS colour A into cram entry 15 and the first tilemap palette's entry 15, as the
; runtime's cram_set does (levels 0, 3, 5, 7 for each channel).
setc15: and $3F
        ld (cram+15),a
        ld c,a
        and 3
        call lv
        rlca
        rlca
        rlca
        ld d,a                  ; R << 3
        ld a,c
        rrca
        rrca
        and 3
        call lv
        or d
        rlca
        rlca
        ld d,a                  ; R << 5 | G << 2
        ld a,c
        rrca
        rrca
        rrca
        rrca
        and 3
        call lv
        ld e,a                  ; B
        srl a
        or d
        ld d,a                  ; first $44 byte
        ld a,e
        and 1
        ld e,a                  ; second $44 byte
        ld bc,$243B
        ld a,$43
        out (c),a
        inc b
        in a,(c)
        ld (s43),a
        and %10001111
        or %00110000            ; write the first tilemap palette
        nextreg $43,a
        nextreg $40,15
        ld a,d
        nextreg $44,a
        ld a,e
        nextreg $44,a
        ld a,(s43)
        nextreg $43,a
        ret
lv:     push hl
        ld hl,lvt
        add a,l
        ld l,a
        jr nc,lv1
        inc h
lv1:    ld a,(hl)
        pop hl
        ret
lvt:    db 0,3,5,7

; rdln: HL = the line the Next draws (0-310), read twice until both reads agree. Changes A,
; F, BC; keeps the interrupt state (interrupts off between the register select and the read).
rdln:   ld a,i
        di
        push af
        ld bc,$243B
r_a:    ld a,$1F
        out (c),a
        inc b
        in l,(c)
        dec b
        ld a,$1E
        out (c),a
        inc b
        in h,(c)
        dec b
        ld a,$1F
        out (c),a
        inc b
        in a,(c)
        dec b
        cp l
        jr nz,r_a
        ld a,h
        and 1
        ld h,a
        pop af
        ret po
        ei
        ret

; clipof: at the line 151 event, in place of the display off. The event comes up to 5 lines
; early on the Next, so when the beam is at lines 140-151 it first waits for line 152, the first
; line the display off blanks on a Master System. Then the tilemap, sprite and Layer 2 clip
; windows start at line 160 of the picture, and the fallback colour (NextReg $4A) is black, so
; lines 152-159 are black, and line 160 shows the status bar with no display-on write. clipon: from
; the line 159 event and from the frame handler. When the beam is at lines 150-159 it first
; waits for line 160. It puts the clip windows back to the picture's (as the runtime's
; clip_update in 192-line mode: X from 17, or 21 when register 0 bit 5 hides column 0;
; tilemap and sprites lines 32-223, Layer 2 lines 0-191), and the fallback colour back to the
; value clipof found, unless the runtime has set another one since. Runtime internal used:
; vdp_regs. Keep every register.
clipof: push af
        push de
        push bc
        ld bc,$243B
cof_w:  ld a,$1E
        out (c),a
        inc b
        in a,(c)
        dec b
        rrca
        jr c,cof_g              ; line 256 or later
        ld a,$1F
        out (c),a
        inc b
        in a,(c)
        dec b
        cp 140
        jr c,cof_g
        cp 152
        jr c,cof_w              ; lines 140-151: wait for line 152
cof_g:  ld a,(fb_on)
        or a
        jr nz,cof_h             ; already hidden: keep the saved colour
        ld a,$4A
        out (c),a
        inc b
        in a,(c)
        ld (fb_sv),a
        ld a,1
        ld (fb_on),a
cof_h:  nextreg $4A,0
        ld de,160*256+192       ; D = Layer 2 Y1, E = tilemap and sprite Y1
        jr clipw
clipon: push af
        push de
        push bc
        ld a,(fb_on)
        or a
        jr z,con_x              ; nothing hidden
        ld bc,$243B
con_w:  ld a,$1E
        out (c),a
        inc b
        in a,(c)
        dec b
        rrca
        jr c,con_f              ; line 256 or later
        ld a,$1F
        out (c),a
        inc b
        in a,(c)
        dec b
        cp 150
        jr c,con_f
        cp 160
        jr c,con_w              ; lines 150-159: wait for line 160
con_f:  xor a
        ld (fb_on),a
        ld a,$4A
        out (c),a
        inc b
        in a,(c)
        or a
        jr nz,con_x             ; the runtime has set the colour since
        ld a,(fb_sv)
        nextreg $4A,a
con_x:  ld de,0*256+32
clipw:  ld a,(vdp_regs+0)
        and $20
        jr z,cw_x
        ld a,4
cw_x:   ld c,a
        nextreg $1C,%00001011   ; reset the tilemap, sprite and Layer 2 clip indexes
        add a,a
        add a,2
        nextreg $18,a           ; Layer 2: X from PIC_X (+ 8)
        nextreg $18,255
        ld a,d
        nextreg $18,a
        nextreg $18,191
        ld a,17
        add a,c
        ld b,a
        nextreg $1B,a           ; tilemap
        nextreg $1B,144
        ld a,e
        nextreg $1B,a
        nextreg $1B,223
        ld a,b
        nextreg $19,a           ; sprites
        nextreg $19,144
        ld a,e
        nextreg $19,a
        nextreg $19,223
        pop bc
        pop de
        pop af
        ret

; sprw: the sprite writer $0336. B = the slot, D = Y, E = X, C = the tile. Y goes to
; $3F00 + B, X and the tile to $3F80 + 2B, each run through jt_vwrite, which sets its own
; address. Entered with interrupts off and P/V = the game's IFF2 (the cave's LD A,I; DI).
; Returns what $0336 leaves: A = H = the tile, B = $7F, C = $BE, DE and L kept, and carry
; set when interrupts were on, for the cave's RET NC; EI. Runs on its own stack.
sprw:   ld (sw_bc),bc
        ld (sw_de),de
        ld a,0
        jp po,sw_s
        inc a
sw_s:   ld (sw_ei),a
        ld (sw_sp),sp
        ld sp,stk_top
        push hl
        push ix
        push iy
        ld a,d
        ld (sw_y),a
        ld a,e
        ld (sw_xt),a
        ld a,c
        ld (sw_xt+1),a
        ld ix,0
        ld iy,0
        ld e,b
        ld d,$3F
        ld hl,sw_y
        ld bc,1*256+1           ; 1 run of 1 byte
        ld a,1                  ; the source in this page
        call jt_vwrite
        ld a,(sw_bc+1)
        add a,a
        or $80
        ld e,a
        ld d,$3F
        ld hl,sw_xt
        ld bc,2*256+1           ; 1 run of 2 bytes
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        pop hl
        ld sp,(sw_sp)
        ld a,(sw_bc)
        ld h,a
        ld de,(sw_de)
        ld bc,$7FBE
        ld a,(sw_ei)
        rra                     ; carry: interrupts were on
        ld a,h
        ret

; cramw: the palette write $02C7-$02DF. Sends the address of colour 0 for a CRAM write,
; then the 16 bytes at HL twice (colours 0-15 and 16-31), each through the runtime's OTIR.
; Entered with interrupts off and P/V = the game's IFF2 (the cave's LD A,I; DI). Returns
; what $02DF leaves: HL + 16, B = 0, C = $BE, A = $C0, and carry set when interrupts were
; on, for the cave's RET NC; EI. Uses no stack of its own beyond the traps.
cramw:  ld a,0
        jp po,cw_s
        inc a
cw_s:   ld (sw_ei),a
        ld (sw_hl),hl
        xor a
        ld c,$BF
        rst $00
        db $79                  ; OUT (C),A
        ld a,$C0
        rst $00
        db $79                  ; OUT (C),A: code 3, address 0
        ld c,$BE
        ld b,16
        rst $00
        db $B3                  ; OTIR: colours 0-15
        ld hl,(sw_hl)
        ld b,16
        rst $00
        db $B3                  ; OTIR: colours 16-31
        ld a,(sw_ei)
        rra                     ; carry: interrupts were on
        ld a,$C0
        ret

fb_on:  db 0
fb_sv:  db 0
r10f:   db 0
evn:    db 0
nxt:    db 0
s43:    db 0
sv_sp:  dw 0
sw_sp:  dw 0
sw_bc:  dw 0
sw_de:  dw 0
sw_ei:  db 0
sw_hl:  dw 0
sw_y:   db 0
sw_xt:  dw 0
xsrc:   dw 0
left:   dw 0
lprev:  dw 0
par:    db 0
cnt:    db 0
ybuf:   ds 32
xbuf:   ds 64
        ds 64
stk_top:
endpage
