# Renegade (Europe, Brazil) (En), CRC32 3BE7F641, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of
# random input, 120 s with no input).
#
# Decisions:
# - No free RST vector: $0000-$0002 (DI; LD B,$00) becomes the io vector. B = 0 at $009B
#   is a cold start (all RAM cleared); RST $08 at $0008 is the game's warm start (B = $FF).
#   The game starts at a cave in the $FF bytes at $0029 that sets B = 0 and jumps to $009B.
# - The frame handler ($016C) turns interrupts on at $0186 and runs the whole game
#   logic there. The next frame event can come while it runs: with $C001 set that entry
#   takes the short path at $01DA (sound only), and at the handler's start or end ($C001
#   clear) it runs the logic again. The runtime holds frame and line events while a
#   frame handler runs. At $0186 a cave (nestcave, in the $FF bytes at $3F93) moves the
#   handler's return address to a stack of 8 words at $DFE2 (count at $DFE0; RAM that no
#   code names and the reference logs never wrote, cleared by both starts at $009B) and
#   puts nesttramp ($3FCB) in the return slot. The runtime then takes the handler as
#   returned and gives the events at once, as the Master System does. nesttramp takes
#   the address back off the stack and jumps to it. Past 8 nested entries the slot is
#   left as it is.
# - Scroll bands: with $C004 bit 4 set the game sets H from line interrupts, from the
#   table at $D181 (the HUD rows and the play area in play, the sky, wall and road on the
#   title). Each line event costs the Next about 5 lines and the first one can come late,
#   after the once-a-frame work, so the bands came late. The rastercode routine
#   renegade-raster.asm works out each line's H from the table, so the game gets no line
#   events while bands are on. The last band's event ($037F) also builds the next
#   picture's table ($3BBA) and runs the sound driver ($0211); with no line events,
#   nestcave makes those two calls at each frame entry with bands on.
# - With a V scroll the runtime's per-line copper list does not wrap the map at line 224,
#   so the title menu (V $30, every band H 0) showed other map rows at the bottom. The
#   routine and nestcave both take bands as on only when the V scroll ($C201) is 0; the
#   menu then gets its line events as without the routine.
name Renegade
cart 3BE7F641
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
start 0029
rastercode renegade-raster.asm
asm 00029 5   ; $FF filler -> cold start
    ld b,0
    jp $009B
endasm
label nestcave 03F93
label nesttramp 03FCB
asm 00186 4   ; EI : LD A,($C002)
    call nestcave
endasm
asm 03F93 56  ; unused $FF bytes: nestcave
    ld a,($C004)
    bit 4,a
    jr z,.nobands
    ld a,($C201)
    or a
    jr nz,.nobands
    call $3BBA
    call $0211
.nobands:
    ld hl,22
    add hl,sp
    ld a,($DFE0)
    cp 8
    jr nc,.full
    inc a
    ld ($DFE0),a
    add a,a
    add a,$E0
    ld e,a
    ld d,$DF
    ld a,(hl)
    ld (de),a
    ld (hl),nesttramp & $FF
    inc hl
    inc de
    ld a,(hl)
    ld (de),a
    ld (hl),nesttramp >> 8
.full:
    ld a,($C002)
    ei
    ret
endasm
asm 03FCB 20  ; unused $FF bytes: nesttramp
    di
    push hl
    push af
    ld hl,$DFE0
    ld a,(hl)
    dec (hl)
    add a,a
    add a,$E0
    ld l,a
    ld a,(hl)
    inc hl
    ld h,(hl)
    ld l,a
    pop af
    ex (sp),hl
    ei
    ret
endasm
asm 0009E 2   ; IM 1 -> IM 2
    im 2
endasm
site 00086   ; IN A,($BF)
site 0008B   ; OUT ($BF),A
site 0008F   ; OUT ($BF),A
site 00094   ; OUT ($BF),A
site 00098   ; OUT ($BF),A
site 000A2   ; OUT ($3E),A
site 000A6   ; OUT ($3F),A
site 000EE   ; IN A,($BF)
site 000F0   ; IN A,($BF)
site 000FB   ; IN A,($BF)
site 0011A   ; OUT ($BF),A
site 0011E   ; OUT ($BF),A
site 0012A   ; OUT ($7F),A
site 0012F   ; OUT ($BF),A
site 00133   ; OUT ($BF),A
site 00139   ; OUT ($BE),A
site 0016E   ; IN A,($BF)
site 002A6   ; IN A,(C)
site 002EF   ; IN A,($BF)
site 002F3   ; OUT (C),E
site 002F7   ; OUT (C),B
site 002F9   ; OUT (C),D
site 002FC   ; OUT (C),B
site 002FF   ; IN A,($BF)
site 00305   ; OUT ($BF),A
site 00309   ; OUT ($BF),A
site 0030F   ; OTIR
site 00313   ; OUT ($BF),A
site 00318   ; OUT ($BF),A
site 0031A   ; OTIR
site 0032C   ; IN A,($7E)
site 0033A   ; OUT (C),A
site 0033E   ; OUT (C),A
site 00343   ; OTIR
site 0034E   ; OUT (C),A
site 00352   ; OUT (C),A
site 0035B   ; OUT (C),A
site 0035F   ; OUT (C),A
site 00366   ; OUT ($BF),A
site 0036A   ; OUT ($BF),A
site 00372   ; OUT ($BF),A
site 00376   ; OUT ($BF),A
site 00384   ; OUT ($BF),A
site 00388   ; OUT ($BF),A
site 00481   ; OTIR
site 00487   ; IN A,($7E)
site 00E56   ; OUT ($BF),A
site 00E5A   ; OUT ($BF),A
site 00E60   ; OUT ($BE),A
site 00E65   ; OUT ($BE),A
site 035A1   ; OUT (C),L
site 035A3   ; OUT (C),H
site 035AB   ; OTIR
site 035AD   ; OTIR
site 03895   ; OUT (C),L
site 03897   ; OUT (C),H
site 0389F   ; OTIR
site 038A1   ; OTIR
site 038A3   ; OTIR
site 038A5   ; OTIR
site 038A7   ; OTIR
site 038A9   ; OTIR
site 03E5B   ; IN A,($BF)
site 03E9E   ; OUT ($BF),A
site 03EA2   ; OUT ($BF),A
site 03EA5   ; OTIR
site 03EBF   ; OUT (C),L
site 03EC1   ; OUT (C),H
site 03ECB   ; OTIR
site 03ED5   ; OUT (C),L
site 03ED7   ; OUT (C),H
site 03EDF   ; OTIR
site 03EE3   ; OTIR
site 03EED   ; OUT (C),L
site 03EEF   ; OUT (C),H
site 03EFC   ; OTIR
site 03F0C   ; OUT (C),L
site 03F0E   ; OUT (C),H
site 03F16   ; OTIR
site 03F18   ; OTIR
site 03F27   ; OUT (C),L
site 03F29   ; OUT (C),H
site 03F37   ; OUT (C),A
site 03F39   ; OUT (C),A
site 03F3B   ; OUT (C),A
site 03F3D   ; OUT (C),A
site 03F5F   ; OUT ($BF),A
site 03F63   ; OUT ($BF),A
site 03F65   ; OUTI
site 03F67   ; OUTI
site 03F7B   ; OUT (C),E
site 03F7D   ; OUT (C),D
site 03F86   ; OUT (C),D
site 03F88   ; OUT (C),E
site 1C0B5   ; OUT ($7F),A
site 1C0B9   ; OUT ($7F),A
site 1C0BD   ; OUT ($7F),A
site 1C0C1   ; OUT ($7F),A
site 1C3E6   ; OUT ($7F),A
site 1C42D   ; OUT ($7F),A
site 1C44F   ; OUT ($7F),A
site 1C453   ; OUT ($7F),A
site 1C457   ; OUT ($7F),A
site 1C45B   ; OUT ($7F),A
site 1C45F   ; OUT ($7F),A
site 1C463   ; OUT ($7F),A
site 1C477   ; OUT ($7F),A
site 1C47C   ; OUT ($7F),A
site 1C481   ; OUT ($7F),A
site 1C491   ; OUT ($7F),A
site 1C498   ; OUT ($7F),A
site 1C49F   ; OUT ($7F),A
site 1C4B2   ; OUT ($7F),A
site 1C4B6   ; OUT ($7F),A
site 1C4BA   ; OUT ($7F),A
site 1DB7C   ; OUT ($7F),A
site 1DB80   ; OUT ($7F),A
site 1DB84   ; OUT ($7F),A
site 1DB88   ; OUT ($7F),A
site 1DC29   ; OUT ($7F),A
site 1DC2F   ; OUT ($7F),A
site 1DC34   ; OUT ($7F),A
site 1DC72   ; OUT ($7F),A
site 1DC77   ; OUT ($7F),A
site 1DE68   ; OUT ($7F),A
site 1DE9B   ; OUT ($7F),A
site 1DFEB   ; OUT ($7F),A
site 1DFF6   ; OUT ($7F),A
site 1E004   ; OUT ($7F),A
mapst 000A9   ; LD ($FFFC),A
mapst 000AC   ; LD ($FFFD),A
mapst 000B1   ; LD ($FFFE),A
mapst 000B6   ; LD ($FFFF),A
mapst 001B8   ; LD ($FFFE),A
mapst 001E7   ; LD ($FFFE),A
mapst 001FE   ; LD ($FFFE),A
mapst 00220   ; LD ($FFFE),A
mapstde 00227   ; LD ($FFFE),DE
mapst 0024E   ; LD ($FFFE),A
mapst 003F3   ; LD ($FFFE),A
mapst 003FB   ; LD ($FFFE),A
mapst 00521   ; LD ($FFFE),A
mapst 00526   ; LD ($FFFF),A
mapst 0054B   ; LD ($FFFE),A
mapst 00557   ; LD ($FFFE),A
mapst 00563   ; LD ($FFFE),A
mapst 0059B   ; LD ($FFFE),A
mapst 005A0   ; LD ($FFFF),A
mapst 005C0   ; LD ($FFFE),A
mapst 005C5   ; LD ($FFFF),A
mapst 005F0   ; LD ($FFFE),A
mapst 005F5   ; LD ($FFFF),A
mapst 0062B   ; LD ($FFFE),A
mapst 00630   ; LD ($FFFF),A
mapst 0065F   ; LD ($FFFE),A
mapst 00664   ; LD ($FFFF),A
mapst 00675   ; LD ($FFFE),A
mapst 0067A   ; LD ($FFFF),A
mapst 006A4   ; LD ($FFFE),A
mapst 006A9   ; LD ($FFFF),A
mapst 006D1   ; LD ($FFFE),A
mapst 006EB   ; LD ($FFFE),A
mapst 006F0   ; LD ($FFFF),A
mapst 00711   ; LD ($FFFE),A
mapst 00716   ; LD ($FFFF),A
mapst 0075B   ; LD ($FFFE),A
mapst 00760   ; LD ($FFFF),A
mapst 0078F   ; LD ($FFFE),A
mapst 007A9   ; LD ($FFFE),A
mapst 007AE   ; LD ($FFFF),A
mapst 00865   ; LD ($FFFE),A
mapst 0086A   ; LD ($FFFF),A
mapst 00915   ; LD ($FFFE),A
mapst 0091A   ; LD ($FFFF),A
mapst 00941   ; LD ($FFFE),A
mapst 00946   ; LD ($FFFF),A
mapst 009DD   ; LD ($FFFE),A
mapst 009E2   ; LD ($FFFF),A
mapst 00A62   ; LD ($FFFE),A
mapst 00A67   ; LD ($FFFF),A
mapst 00B29   ; LD ($FFFE),A
mapst 00B2E   ; LD ($FFFF),A
mapst 00B9E   ; LD ($FFFE),A
mapst 00CC1   ; LD ($FFFE),A
mapst 00CCF   ; LD ($FFFE),A
mapst 00CD4   ; LD ($FFFF),A
mapst 00CFC   ; LD ($FFFE),A
mapst 00D0A   ; LD ($FFFE),A
mapst 00D0F   ; LD ($FFFF),A
mapst 00D34   ; LD ($FFFE),A
mapst 00D40   ; LD ($FFFE),A
mapst 00D80   ; LD ($FFFE),A
mapst 00F2F   ; LD ($FFFE),A
mapst 00FFB   ; LD ($FFFE),A
mapst 01000   ; LD ($FFFF),A
mapst 01199   ; LD ($FFFE),A
mapst 0119E   ; LD ($FFFF),A
mapst 011D6   ; LD ($FFFE),A
mapst 01270   ; LD ($FFFE),A
mapst 012EA   ; LD ($FFFE),A
mapst 012FD   ; LD ($FFFE),A
mapst 01358   ; LD ($FFFE),A
mapst 01415   ; LD ($FFFE),A
mapst 01428   ; LD ($FFFE),A
mapst 014BB   ; LD ($FFFE),A
mapst 01545   ; LD ($FFFF),A
mapst 0159B   ; LD ($FFFF),A
mapst 015DA   ; LD ($FFFE),A
mapst 0164C   ; LD ($FFFF),A
mapst 016D4   ; LD ($FFFE),A
mapst 017FC   ; LD ($FFFE),A
mapst 018DA   ; LD ($FFFE),A
mapst 018E2   ; LD ($FFFE),A
mapst 0198B   ; LD ($FFFE),A
mapst 01A3D   ; LD ($FFFE),A
mapst 01A64   ; LD ($FFFE),A
mapst 01AC2   ; LD ($FFFE),A
mapst 01B2B   ; LD ($FFFE),A
mapst 01BD4   ; LD ($FFFE),A
mapst 01C72   ; LD ($FFFE),A
mapst 01C97   ; LD ($FFFE),A
mapst 01D3A   ; LD ($FFFE),A
mapst 01DC1   ; LD ($FFFE),A
mapst 01EB4   ; LD ($FFFE),A
mapst 01ED8   ; LD ($FFFE),A
mapst 01EDD   ; LD ($FFFF),A
mapst 01EED   ; LD ($FFFE),A
mapst 01F6B   ; LD ($FFFE),A
mapst 01FEA   ; LD ($FFFE),A
mapst 02067   ; LD ($FFFE),A
mapst 020EB   ; LD ($FFFE),A
mapst 0217B   ; LD ($FFFE),A
mapst 0223F   ; LD ($FFFE),A
mapst 02276   ; LD ($FFFE),A
mapst 0227B   ; LD ($FFFF),A
mapst 022D5   ; LD ($FFFE),A
mapst 022DA   ; LD ($FFFF),A
mapst 0235E   ; LD ($FFFE),A
mapst 02388   ; LD ($FFFE),A
mapst 023B5   ; LD ($FFFE),A
mapst 024B3   ; LD ($FFFE),A
mapst 02525   ; LD ($FFFE),A
mapst 0259A   ; LD ($FFFE),A
mapst 0260F   ; LD ($FFFE),A
mapst 0284B   ; LD ($FFFE),A
mapst 028ED   ; LD ($FFFE),A
mapst 0291C   ; LD ($FFFE),A
mapst 02938   ; LD ($FFFE),A
mapst 02964   ; LD ($FFFE),A
mapst 02996   ; LD ($FFFE),A
mapst 029D2   ; LD ($FFFE),A
mapst 02A07   ; LD ($FFFE),A
mapst 02AF0   ; LD ($FFFE),A
mapst 02AF5   ; LD ($FFFF),A
mapst 02C22   ; LD ($FFFE),A
mapst 02C47   ; LD ($FFFE),A
mapst 02D7C   ; LD ($FFFE),A
mapst 02E05   ; LD ($FFFE),A
mapst 02F4F   ; LD ($FFFE),A
mapst 03001   ; LD ($FFFF),A
mapst 03023   ; LD ($FFFE),A
mapst 030A3   ; LD ($FFFE),A
mapst 030FC   ; LD ($FFFE),A
mapst 031CC   ; LD ($FFFE),A
mapst 031D1   ; LD ($FFFF),A
mapst 034B3   ; LD ($FFFF),A
mapst 034EB   ; LD ($FFFF),A
mapst 03523   ; LD ($FFFF),A
mapst 03599   ; LD ($FFFF),A
mapst 035B8   ; LD ($FFFE),A
mapst 035BD   ; LD ($FFFF),A
mapst 035F4   ; LD ($FFFE),A
mapst 035F9   ; LD ($FFFF),A
mapst 0361E   ; LD ($FFFE),A
mapst 03623   ; LD ($FFFF),A
mapst 0365A   ; LD ($FFFE),A
mapst 0365F   ; LD ($FFFF),A
mapst 0369C   ; LD ($FFFE),A
mapst 036A1   ; LD ($FFFF),A
mapst 036D6   ; LD ($FFFE),A
mapst 036DB   ; LD ($FFFF),A
mapst 03704   ; LD ($FFFE),A
mapst 03709   ; LD ($FFFF),A
mapst 0373B   ; LD ($FFFE),A
mapst 03740   ; LD ($FFFF),A
mapst 0381A   ; LD ($FFFE),A
mapst 0385A   ; LD ($FFFE),A
mapst 03873   ; LD ($FFFE),A
mapst 03878   ; LD ($FFFF),A
mapst 0387F   ; LD ($FFFE),A
mapst 03884   ; LD ($FFFF),A
mapst 03D9C   ; LD ($FFFE),A
mapst 03EB7   ; LD ($FFFF),A
mapst 03F1F   ; LD ($FFFF),A
mapst 04142   ; LD ($FFFF),A
mapst 0C01A   ; LD ($FFFF),A
mapst 0C024   ; LD ($FFFF),A
mapst 0C04C   ; LD ($FFFF),A
mapst 0C056   ; LD ($FFFF),A
mapst 0C10B   ; LD ($FFFF),A
mapst 0C129   ; LD ($FFFF),A
mapst 0C135   ; LD ($FFFF),A
mapst 0C16B   ; LD ($FFFF),A
mapst 0F185   ; LD ($FFFF),A
mapst 0F18F   ; LD ($FFFF),A
mapst 0F1AD   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it

# Renegade (Europe, Brazil).cht, "Invincibility": the patch at $5201 (bank 3) turns the
# SUB B that takes the hit off the energy byte into a NOP, so the energy never drops
poke "Infinite energy"
gg 002-01A-A28
endpoke

# Renegade (Europe, Brazil).cht, "Infinite Lives - Both Players": the patch at $541C
# (bank 3) removes the store that writes the lives back after a death
poke "Infinite lives"
gg 3A4-1CA-2A2
endpoke

# Renegade (Europe, Brazil).cht, "Infinite Time": the patch at $03E8 (bank 0) removes the
# store to the countdown counter at $C3A2, so the clock stops
poke "Infinite time"
gg 3A3-E8F-2A2
endpoke

# Renegade (Europe) (Action Replay).cht, "Mission Select (Replace ? With 0-3)": RAM $C21E is
# the mission, 00 to 03; 04 gives a black screen
poke "Start mission"
ar 00C2-1E??
endpoke

# Renegade (Europe) (Action Replay).cht, "Enemies Have No Life": RAM $C26F, $C28F and $C2AF
# are the energy of the enemies, held at $00, so each one falls at the first hit
poke "One-hit enemies"
ar 00C2-6F00
ar 00C2-8F00
ar 00C2-AF00
endpoke
