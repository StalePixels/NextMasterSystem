# Cool Spot (Europe), CRC32 13AC9023, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
#
# Drafted by tools/mkspec.py from the sitescan output with a 600 s reference I/O log, then
# decided by hand.
#
# Decisions:
# - No free RST vector: $0000-$0002 (DI; IM 1) becomes the io vector, and the game starts at
#   $0003 (JP $00E9). The game has no RST $00 of its own: the scanner's one at $69BF is in
#   the script data at $692B.
# - $692B-$6A4B is script data (a pointer stored at $CFFA by $6603), not code: the I/O
#   patterns at $693A, $6941 and $695A are not patched.
# - Sprites are multiplexed: the frame handler $41EF in play, the bonus stage included (and
#   $7210 in the title and the other screens that $70C5 sets up, handler $71B2) hides all 32 sprites ($4273 writes $C0 to each Y), writes the sprites of bands 0-2
#   ($4247), and each line interrupt (every 8 lines) writes the next 8-line band into the next
#   8 of the 32 slots ($41C3, $71E4: CALL $0577). The bands are lists of $40 bytes from ($D078)
#   (count, 16 Y, 16 X and tile pairs), double-buffered at $C000 and $C800. The Next draws
#   the sprites from the sprite table once a frame, after the hide, and showed none. Page 0
#   writes the sprite table once a frame at $4247 (sprsat) and $7267 (sprsat64) with the
#   sprites of all 25 bands, with the same choice of sprites as $0577 for a band of more than
#   8 (by $D074 bit 0); the hide and the line interrupts' band writes are taken out. In play
#   slots 32-63 are the status bar's own sprites and stay as the game writes them, so sprsat
#   fills slots 0-31; the title leaves slots 32-63 empty and its menu needs more than 32, so
#   sprsat64 fills all 64. Sprites past the limit in one frame are not shown.
# - The time display ($183E, from the frame handler's $4D61) and the tile writers at $0412,
#   $045B and $049B wait while the V counter is $80-$9F (lines 128-159) before each write, so
#   that their writes with interrupts off do not delay the line interrupts at lines 151
#   (display off) and 159 (display on). On a Master System the frame handler is done before
#   line 128. On the Next it can reach line 128 and then waited there with interrupts off,
#   past the line interrupts of lines 151 and 159. Each wait now calls vwin, in the zero
#   bytes at $0044, which waits only while interrupts are on.
# - The line interrupt comes every 8 lines (register 10 = 7), so in play the last one of a
#   picture is at line 191. When the game takes that one a line or two late (interrupts off),
#   the runtime schedules the frame event at line 192, which has passed: the frame event then
#   came a frame late and every line event of the next picture was lost (about one frame in
#   three in play). In play nothing below line 159
#   needs a line interrupt: the line handler of line 159 ($1630, the display on) now sets
#   register 10 to $FF through r10off, so no event comes after it, and the frame handler
#   sets it back to 7 through r10on (at $41F7 and $7218), in the vertical blank, where it
#   sets the next picture's first event.
# - In play the line handler turns the display off at line 151 ($1625) and on at line 159
#   ($1638), over the seam between the play area and the status bar. On the Next the
#   display-on write first converts the tiles written since the display went off, and in
#   about one frame in five that took 20-51 lines, so the top of the status bar was black.
#   The display-off write is replaced with page 0 clipof: from line 152 the tilemap, sprite
#   and Layer 2 clip windows start at line 160 and the fallback colour is black, so lines
#   152-159 are black, as on a Master System, and line 160 shows the status bar with no
#   display-on write. The display-on write at $1638 then changes nothing. clipon (from
#   r10off at line 159 and r10on in the frame handler) puts the windows and the colour back.
# - $013F tells PAL from NTSC by counting a loop of V counter reads over one frame: 2100
#   passes or more is PAL ($DEAB = 0), fewer NTSC ($FF). Through the runtime's traps the
#   loop counts far fewer, so the game took its NTSC path at 50 Hz: the level clock counted
#   60 frames a second ($4D94) and the sound driver ran its NTSC setting ($8045). The
#   DEC A at $0158 is taken out: $DEAB is 0, as on a PAL Master System. A reference on
#   sg1000m3 (NTSC) needs $DEAB forced to 0 (NM_POKEW=DEAB:FF:0).
name Cool Spot
cart 13AC9023
hz 50		; No-Intro region Europe
# The title writes the H scroll from the line interrupts (one value a
# band, from $D544 at $71B6); without hsplit the right of the lines below a split showed the
# wrong map columns.
hsplit
vector 00 io
start 0003
site 0003A   ; IN A,($BF)
asm 07FC0 24  ; zero bytes before the cart header (slot 1 always holds bank 1)
; r10off ($7FC0) / r10on ($7FC4): the clip windows back to the whole picture (page 0 clipon),
; then register 10 = $FF / 7 through OUT (C),A to port $BF. Keep every register but A and F.
c_off:
    ld a,$FF
    jr c_w
c_on:
    ld a,7
c_w:
    rst $00
    db far_io, pg_sprsat, ent_clipon
    push bc
    ld c,$BF
    rst $00
    db $79              ; OUT (C),A
    ld a,$8A
    rst $00
    db $79              ; OUT (C),A: register 10
    pop bc
    ret
endasm
label r10off 07FC0
label r10on 07FC4
label vwin 00044
asm 00044 19  ; zero bytes after the frame handler entry: vwin
; vwin: A = the V counter. Z: write now; NZ: wait. The game's window ($80-$9F) applies only
; while interrupts are on (IFF2 from LD A,I). Changes A and F; the callers' POP AF follow.
    cp $80
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
site 00147   ; IN B,(C)
site 0014C   ; IN B,(C)
asm 00158 1   ; DEC A: the NTSC result of the frame count (see the header)
endasm
site 00169   ; OTIR
site 00170   ; IN A,($DD)
site 0018E   ; IN A,($7E)
site 0019F   ; IN A,($DC)
site 001AD   ; IN A,($DD)
site 0030B   ; OUT ($BF),A
site 0030F   ; OUT ($BF),A
site 00315   ; OUT ($BE),A
site 00331   ; OUT ($BF),A
site 00335   ; OUT ($BF),A
site 0033B   ; OUT ($BE),A
site 00344   ; OUT ($BE),A
site 00350   ; OUT (C),A
site 00354   ; OUT (C),A
site 00359   ; OUT (C),A
site 0037C   ; OUT ($BF),A
site 00381   ; OUT ($BF),A
site 00386   ; OUTI
site 00394   ; OUT (C),L
site 00396   ; OUT (C),H
site 003AA   ; OUTI
site 003B8   ; OUT ($BF),A
site 003BB   ; OUT ($BF),A
site 003BD   ; OUTI
site 003C8   ; OUTI
site 003D3   ; OUT ($BF),A
site 003D8   ; OUT (C),B
site 003E1   ; OUT (C),D
site 003E7   ; OUT (C),A
site 003E9   ; OUT (C),B
site 003F2   ; OUT (C),E
site 003FB   ; OUT (C),A
site 00403   ; OUT (C),E
site 00405   ; OUT (C),D
site 0040A   ; OUT (C),A
site 00413   ; IN A,($7E)
asm 00415 8   ; CP $80; JR C; CP $A0; JR C,$0413: the wait through vwin
    call vwin
    jr nz,$0413
endasm
site 0041F   ; OUT (C),E
site 00421   ; OUT (C),D
otir 00424   ; OUTI
site 0045C   ; IN A,($7E)
asm 0045E 8   ; CP $80; JR C; CP $A0; JR C,$045C: the wait through vwin
    call vwin
    jr nz,$045C
endasm
site 00468   ; OUT (C),E
site 0046A   ; OUT (C),D
otir 0046D   ; OUTI
site 0049C   ; IN A,($7E)
asm 0049E 8   ; CP $80; JR C; CP $A0; JR C,$049C: the wait through vwin
    call vwin
    jr nz,$049C
endasm
site 004A8   ; OUT (C),E
site 004AA   ; OUT (C),D
site 004B2   ; OUT (C),A
site 004B7   ; OUT (C),A
site 004BC   ; OUT (C),A
site 004C1   ; OUT (C),A
site 004C6   ; OUT (C),A
site 004CB   ; OUT (C),A
site 004D0   ; OUT (C),A
site 004D5   ; OUT (C),A
site 004DA   ; OUT (C),A
site 004DF   ; OUT (C),A
site 004E4   ; OUT (C),A
site 004E9   ; OUT (C),A
site 004EE   ; OUT (C),A
site 004F3   ; OUT (C),A
site 004F8   ; OUT (C),A
site 004FD   ; OUT (C),A
site 00502   ; OUT (C),A
site 00507   ; OUT (C),A
site 0050C   ; OUT (C),A
site 00511   ; OUT (C),A
site 00516   ; OUT (C),A
site 0051B   ; OUT (C),A
site 00520   ; OUT (C),A
site 00525   ; OUT (C),A
site 0052A   ; OUT (C),A
site 0052F   ; OUT (C),A
site 00534   ; OUT (C),A
site 00539   ; OUT (C),A
site 0053E   ; OUT (C),A
site 00543   ; OUT (C),A
site 00548   ; OUT (C),A
site 0054C   ; OUT (C),A
site 005B7   ; OUT (C),A
site 005BB   ; OUT (C),A
site 005BE   ; OUTI
site 005C3   ; OUTI
site 005C8   ; OUTI
site 005CD   ; OUTI
site 005D2   ; OUTI
site 005D7   ; OUTI
site 005DC   ; OUTI
site 005E1   ; OUTI
site 005E9   ; OUT (C),A
site 005ED   ; OUT (C),A
site 005F0   ; OUTI
site 005F5   ; OUTI
site 005FA   ; OUTI
site 005FF   ; OUTI
site 00604   ; OUTI
site 00609   ; OUTI
site 0060E   ; OUTI
site 00613   ; OUTI
site 00618   ; OUTI
site 0061D   ; OUTI
site 00622   ; OUTI
site 00627   ; OUTI
site 0062C   ; OUTI
site 00631   ; OUTI
site 00636   ; OUTI
site 0063B   ; OUTI
site 00646   ; OUTI
site 00649   ; OUT (C),A
site 0065B   ; OUT ($BF),A
site 0065F   ; OUT ($BF),A
site 00665   ; OUT ($BF),A
site 00669   ; OUT ($BF),A
site 0066F   ; OUT ($BF),A
site 00673   ; OUT ($BF),A
site 00677   ; OUT ($BF),A
site 0067B   ; OUT ($BF),A
site 00737   ; OUT ($BF),A
site 0073B   ; OUT ($BF),A
site 00742   ; OUTI
site 00744   ; OUTI
site 00746   ; OUTI
site 00748   ; OUTI
site 0074A   ; OUTI
site 0074C   ; OUTI
site 0074E   ; OUTI
site 00750   ; OUTI
site 00752   ; OUTI
site 00754   ; OUTI
site 00756   ; OUTI
site 00758   ; OUTI
site 0075A   ; OUTI
site 0075C   ; OUTI
site 0075E   ; OUTI
site 00760   ; OUTI
site 00762   ; OUTI
site 00764   ; OUTI
site 00766   ; OUTI
site 00768   ; OUTI
site 0076A   ; OUTI
site 0076C   ; OUTI
site 0076E   ; OUTI
site 00770   ; OUTI
site 00772   ; OUTI
site 00774   ; OUTI
site 00776   ; OUTI
site 00778   ; OUTI
site 0077A   ; OUTI
site 0077C   ; OUTI
site 0077E   ; OUTI
site 00780   ; OUTI
site 0081D   ; OUT ($BF),A
site 00822   ; OUT ($BF),A
site 00832   ; OUT (C),A
site 0083B   ; OUT (C),A
site 0087B   ; OUT (C),L
site 0087D   ; OUT (C),H
site 00884   ; OUTI
site 0088A   ; OUTI
site 0089E   ; OUT (C),L
site 008A0   ; OUT (C),H
site 008B4   ; OUTI
site 008C2   ; OUT ($BF),A
site 008C5   ; OUT ($BF),A
site 008C7   ; OUTI
site 008D2   ; OUTI
site 00911   ; OUT (C),E
site 00913   ; OUT (C),D
site 00916   ; OUTI
site 0091E   ; OUT (C),A
site 00930   ; OUT (C),A
site 00932   ; OUT (C),D
site 00935   ; OUTI
site 0093D   ; OUT (C),A
site 00969   ; OUT (C),E
site 0096B   ; OUT (C),D
site 0096E   ; OUTI
site 00976   ; OUT (C),A
site 0126E   ; OUT ($BF),A
site 01272   ; OUT ($BF),A
asm 01625 8   ; LD A,$A0; OUT ($BF),A; LD A,$81; OUT ($BF),A: the display off at line 151 (see the header)
    rst $00
    db far_io, pg_sprsat, ent_clipof
endasm
site 0163A   ; OUT ($BF),A
site 0163E   ; OUT ($BF),A
asm 01630 8   ; the 8 NOPs before the display-on write of line 159
    call r10off
endasm
site 01844   ; IN A,($7E)
asm 01846 8   ; CP $80; JR C; CP $A0; JR C,$1844: the wait through vwin
    call vwin
    jr nz,$1844
endasm
site 04185   ; IN A,($7E)
site 04274   ; OUT ($BF),A
site 04278   ; OUT ($BF),A
site 0427C   ; OUT ($BE),A
site 0427E   ; OUT ($BE),A
site 04280   ; OUT ($BE),A
site 04282   ; OUT ($BE),A
site 04284   ; OUT ($BE),A
site 04286   ; OUT ($BE),A
site 04288   ; OUT ($BE),A
site 0428A   ; OUT ($BE),A
site 0428C   ; OUT ($BE),A
site 0428E   ; OUT ($BE),A
site 04290   ; OUT ($BE),A
site 04292   ; OUT ($BE),A
site 04294   ; OUT ($BE),A
site 04296   ; OUT ($BE),A
site 04298   ; OUT ($BE),A
site 0429A   ; OUT ($BE),A
site 0429C   ; OUT ($BE),A
site 0429E   ; OUT ($BE),A
site 042A0   ; OUT ($BE),A
site 042A2   ; OUT ($BE),A
site 042A4   ; OUT ($BE),A
site 042A6   ; OUT ($BE),A
site 042A8   ; OUT ($BE),A
site 042AA   ; OUT ($BE),A
site 042AC   ; OUT ($BE),A
site 042AE   ; OUT ($BE),A
site 042B0   ; OUT ($BE),A
site 042B2   ; OUT ($BE),A
site 042B4   ; OUT ($BE),A
site 042B6   ; OUT ($BE),A
site 042B8   ; OUT ($BE),A
site 042BA   ; OUT ($BE),A
site 04B48   ; OUT (C),E
site 04B4A   ; OUT (C),D
site 04B4D   ; OUTI
site 04B4F   ; OUTI
site 04B51   ; OUTI
site 04B53   ; OUTI
site 04B55   ; OUTI
site 04B57   ; OUTI
site 04B59   ; OUTI
site 04B5B   ; OUTI
site 04B5D   ; OUTI
site 04B5F   ; OUTI
site 04B61   ; OUTI
site 04B63   ; OUTI
site 04B65   ; OUTI
site 04B67   ; OUTI
site 04B69   ; OUTI
site 04B6B   ; OUTI
site 04B6D   ; OUTI
site 04B6F   ; OUTI
site 04B71   ; OUTI
site 04B73   ; OUTI
site 04B75   ; OUTI
site 04B77   ; OUTI
site 04B79   ; OUTI
site 04B7B   ; OUTI
site 04B7D   ; OUTI
site 04B7F   ; OUTI
site 04B81   ; OUTI
site 04B83   ; OUTI
site 04B85   ; OUTI
site 04B87   ; OUTI
site 04B89   ; OUTI
site 04B8B   ; OUTI
site 050D5   ; OUT (C),E
site 050D7   ; OUT (C),D
site 050DC   ; OUTI
site 050E4   ; OUT (C),A
site 050F9   ; OUT (C),E
site 050FD   ; OUT (C),D
site 05622   ; OUT (C),D
site 05628   ; OUT (C),E
site 0562E   ; OUT (C),H
site 05634   ; OUT (C),L
site 06A87   ; OUT (C),E
site 06A89   ; OUT (C),D
site 06A8C   ; OUTI
site 06A8E   ; OUTI
site 06A90   ; OUTI
site 06A92   ; OUTI
site 06A94   ; OUTI
site 06A96   ; OUTI
site 06A98   ; OUTI
site 06A9A   ; OUTI
site 06A9C   ; OUTI
site 06A9E   ; OUTI
site 06AA0   ; OUTI
site 06AA2   ; OUTI
site 06AA4   ; OUTI
site 06AA6   ; OUTI
site 06AA8   ; OUTI
site 06AAA   ; OUTI
site 06AAC   ; OUTI
site 06AAE   ; OUTI
site 06AB0   ; OUTI
site 06AB2   ; OUTI
site 06AB4   ; OUTI
site 06AB6   ; OUTI
site 06AB8   ; OUTI
site 06ABA   ; OUTI
site 06ABC   ; OUTI
site 06ABE   ; OUTI
site 06AC0   ; OUTI
site 06AC2   ; OUTI
site 06AC4   ; OUTI
site 06AC6   ; OUTI
site 06AC8   ; OUTI
site 06ACA   ; OUTI
site 08013   ; OUT ($7F),A
site 08017   ; OUT ($7F),A
site 08024   ; OUT ($7F),A
site 08028   ; OUT ($7F),A
site 08064   ; OUT ($7F),A
site 0807B   ; OUT ($7F),A
site 0808F   ; OUT ($7F),A
site 0809E   ; OUT ($7F),A
site 080B5   ; OUT ($7F),A
site 080C9   ; OUT ($7F),A
site 080F6   ; OUT ($7F),A
site 08109   ; OUT ($7F),A
site 08120   ; OUT ($7F),A
site 08126   ; OUT ($7F),A
site 0814A   ; OUT ($7F),A
site 08161   ; OUT ($7F),A
site 08175   ; OUT ($7F),A
site 081D2   ; OUT ($7F),A
site 083BB   ; OUT ($7F),A
site 083C0   ; OUT ($7F),A
site 083D4   ; OUT ($7F),A
site 083E7   ; OUT ($7F),A
site 083F3   ; OUT ($7F),A
site 08406   ; OUT ($7F),A
mapst 00090   ; LD ($FFFC),A
mapst 00096   ; LD ($FFFC),A
mapst 000EA   ; LD ($FFFC),A
mapst 000ED   ; LD ($FFFD),A
mapst 000F1   ; LD ($FFFE),A
mapst 000F5   ; LD ($FFFF),A
mapst 00438   ; LD ($FFFF),A
mapst 00C33   ; LD ($FFFF),A
mapst 01252   ; LD ($FFFF),A
mapst 01645   ; LD ($FFFF),A
mapst 01B14   ; LD ($FFFF),A
mapst 01CAC   ; LD ($FFFF),A
mapst 02A23   ; LD ($FFFF),A
mapst 02A65   ; LD ($FFFF),A
mapst 031F8   ; LD ($FFFF),A
mapst 04126   ; LD ($FFFF),A
mapst 04241   ; LD ($FFFF),A
mapst 0426F   ; LD ($FFFF),A
mapst 04428   ; LD ($FFFF),A
mapst 04852   ; LD ($FFFF),A
mapst 048DD   ; LD ($FFFF),A
mapst 0499B   ; LD ($FFFF),A
mapst 049C2   ; LD ($FFFF),A
mapst 049D3   ; LD ($FFFF),A
mapst 049EE   ; LD ($FFFF),A
mapst 04A8F   ; LD ($FFFF),A
mapst 04C3D   ; LD ($FFFF),A
mapst 04E01   ; LD ($FFFF),A
mapst 0503A   ; LD ($FFFF),A
mapst 05042   ; LD ($FFFF),A
mapst 05052   ; LD ($FFFF),A
mapst 0505A   ; LD ($FFFF),A
mapst 05064   ; LD ($FFFF),A
mapst 0506B   ; LD ($FFFF),A
mapst 0508F   ; LD ($FFFF),A
mapst 05096   ; LD ($FFFF),A
mapst 050A0   ; LD ($FFFF),A
mapst 050A7   ; LD ($FFFF),A
mapst 050B2   ; LD ($FFFF),A
mapst 050F4   ; LD ($FFFF),A
mapst 05682   ; LD ($FFFF),A
mapst 059EE   ; LD ($FFFF),A
mapst 05AF4   ; LD ($FFFF),A
mapst 05C63   ; LD ($FFFF),A
mapst 05E07   ; LD ($FFFF),A
mapst 05E74   ; LD ($FFFF),A
mapst 05FEA   ; LD ($FFFF),A
mapst 06084   ; LD ($FFFF),A
mapst 06133   ; LD ($FFFF),A
mapst 061A3   ; LD ($FFFF),A
mapst 06229   ; LD ($FFFF),A
mapst 0646B   ; LD ($FFFF),A
mapst 06A5F   ; LD ($FFFF),A
mapst 06ADD   ; LD ($FFFF),A
mapst 07062   ; LD ($FFFF),A
mapst 0724A   ; LD ($FFFF),A
mapst 07292   ; LD ($FFFF),A
mapst 00071   # LD ($FFFC),A; after LD A,$28; 32 bytes of valid code before it
mapst 00083   # LD ($FFFC),A; after LD A,($FFFB); JP/CALL target from $1CD6D; 32 bytes of valid code before it
mapst 00089   # LD ($FFFC),A; after LD A,$28; JP/CALL target from $0957E; 32 bytes of valid code before it
mapst 0009A   # LD ($FFFD),A; after another mapper store, LD ($FFFC),A at $00096; 32 bytes of valid code before it
mapst 000A0   # LD ($FFFC),A; after LD A,($FFFB); JP/CALL target from $30DA9; 32 bytes of valid code before it
mapst 000AB   # LD ($FFFD),A; JP/CALL target from $3BCCC; 32 bytes of valid code before it
mapst 000B6   # LD ($FFFC),A; after LD A,$28; 32 bytes of valid code before it
asm 041F7 3   ; CALL $4273: the hide of all 32 sprites; sprsat writes the whole table
    call r10on
endasm
asm 07218 3   ; CALL $4273, as at $41F7
    call r10on
endasm
asm 041C3 3   ; CALL $0577: a line interrupt's band; sprsat has written every band
endasm
asm 071E4 3   ; CALL $0577, as at $41C3
endasm
asm 04247 39  ; XOR A ... CALL $056A x3: bands 0-2 into slots $18, $10 and $08
    rst $00
    db far_io, pg_sprsat, ent_sprsat
endasm
asm 07267 39  ; the same bands in the title's handler ($71B2), into all 64 slots
    rst $00
    db far_io, pg_sprsat, ent_sprsat64
endasm

# Cool Spot (Europe).cht, "Infinite Lives": RAM $D18E is the lives counter (the HUD shows it
# minus 1); held at 3 a death leaves it at 3
poke "Infinite lives"
ar 00D1-8E03
endpoke

# Cool Spot (Europe).cht, "Invinicibility": RAM $D1BD is the hit timer; held at 2 a hit
# no longer costs a life
poke "Invincibility"
ar 00D1-BD02
endpoke

# Cool Spot (Europe).cht, "Infinite Time": RAM $D090 and $D091 are the seconds and minutes
# of the level clock, in BCD; held at 9:59 the clock never runs out
poke "Infinite time"
ar 00D0-9059
ar 00D0-9109
endpoke

# Cool Spot (Europe).cht, "Cool % Modifier": RAM $C769 is the cool percentage on the HUD, in
# BCD; from $63 the game sets its cage flag ($C768) itself
poke "Cool percent"
ar 00C7-69??
endpoke

# Cool Spot (Europe).cht, "Cheat Menu Enabled": RAM $CE47 held at 4 adds a Cheats! row to the
# Options screen (Lives, Shield, Level)
poke "Cheat menu"
ar 00CE-4704
endpoke

page 0 sprsat sprsat64 clipof clipon
    OPT --zxnext        ; NEXTREG
; sprsat: the sprite table of a frame in one write. Does what $4247-$426D leaves in RAM
; ($D075 = $08, $D07A = ($D078) + $80), then takes the bands of the list at ($D078): 25
; bands of $40 bytes, each a count n (0 to 16), 16 Y bytes and 16 X and tile pairs. A band of
; n <= 8 gives sprites 0 to n-1; for n > 8, $0577 gives sprites 0-7 when $D074 bit 0 is
; clear, else sprites 0 to 15-n and 8 to n-1. The sprites go in band order into slots 0-31
; (sprsat) or 0-63 (sprsat64); the slots left over get Y $E0 (below the picture). A Y of $D0
; from a band is written as $E0, so that it does not end the table before the status bar's
; slots 32-63. jt_vwrite writes the Y bytes to $3F00 and the X and tile bytes to $3F80. Runs inside the frame handler, with interrupts off, on its own stack.
; Changes A, F, BC, DE and HL, as the code it replaces does.
sprsat64:
        ld (sv_sp),sp
        ld sp,stk_top
        ld a,64
        jr sstart
sprsat: ld (sv_sp),sp
        ld sp,stk_top
        ld a,32
sstart: ld (lim),a
        ld a,8
        ld ($D075),a
        ld hl,($D078)
        ld de,$0080
        add hl,de
        ld ($D07A),hl
        ld a,($D074)
        and 1
        ld (par),a
        xor a
        ld (cnt),a
        ld hl,($D078)
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
        ld b,a
        ld a,(lim)
        ld c,a
        ld a,b
hide:   cp c
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
        ld a,(lim)
        ld b,a                  ; 1 run of 32 or 64 bytes
        ld c,1
        ld a,1                  ; the source in this page
        call jt_vwrite
        ld hl,xbuf
        ld de,$3F80
        ld a,(lim)
        add a,a
        ld b,a                  ; 1 run of 64 or 128 bytes (0: 256 would be wrong)
        ld c,1
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        ld sp,(sv_sp)
        ret

; copy: B sprites from index E of the band whose Y bytes start at HL, into the table, while
; it holds fewer than lim. Keeps HL.
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
cloop:  ld a,(lim)
        ld d,a
        ld a,(cnt)
        cp d
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

fb_on:  db 0
fb_sv:  db 0
sv_sp:  dw 0
xsrc:   dw 0
par:    db 0
cnt:    db 0
lim:    db 32
ybuf:   ds 64
xbuf:   ds 128
        ds 64
stk_top:
endpage

