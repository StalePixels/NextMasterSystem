# Joe Montana Football (USA, Europe, Brazil) (En), CRC32 0A9089E5, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - No free RST vector, so the JP at $0000 is the io vector; the game starts at its target
#   $0069. The game's code has no RST; the frame handler jumps to $0069 when the reset
#   button is pressed ($0196).
# - $122C, $21C6 and $5C08 are LD ($0006),A: stores into cart ROM, no-ops on a Master
#   System. No code reads $0006, so they stay as they are.
# - Line interrupts stay off. Every register 0 value the game writes has bit 4 set (line
#   interrupt on, register 10 = $58), but the frame handler returns at $00A9 on a line
#   interrupt and does nothing else, so a Master System plays the same without them. With
#   them on, the runtime writes register 8 straight to the Next, and the copper list's head
#   keeps an older X, which it sets again at line 0 of every frame: after a kickoff return
#   the play select screen and the field showed shifted by the H of an earlier frame. The
#   spec clears bit 4 in the nine LD A,$36 or LD A,$16 before a register 0 write and in the
#   register table at $0F28 (power-on, loaded by $02E0).
# - Step rate. In field play the main loop runs one step a pass: CALL $025D, then it sets
#   bit 6 of $C7FA at $01E9 and waits until the frame handler clears it ($0169). A Master
#   System needs about 3.4 NTSC frames for a step's work, so on the reference (sg1000m3) 312
#   of 330 field steps take 4 frames, the rest 5; a PAL Master System takes about 3. The
#   Next does the work in under a frame and stepped every frame, three to four times too
#   fast. The cave at $000F holds each field step to at least 3 frames at 50 Hz and 4 at
#   60 Hz (NextReg $05 bit 2), counted on the game's frame counter $C7DE; it keeps the
#   counter value of the last release in $0008 (unused zero filler, like the cave). The
#   menus use other waits and are not held.
# - No priority: the cells with the priority bit (row 0 of the field, tile 361) have only
#   colour 0 pixels, which never cover sprites.
# - The routines at $02F3 (one CRAM write), $0444 (one VRAM read) and $044E (a block VRAM
#   read, called only from $16BB, which nothing names) are named by no call, jump, address
#   load or table word, and no recording ran them: their I/O sites are not patched (verdict
#   unused). The I/O byte patterns in banks 9 and 10 are graphics (verdict false).
name Joe Montana Football
cart 0A9089E5
hz any		; No-Intro regions USA, Europe, Brazil
vector 00 io
start 0069
asm 00069 2   ; IM 1 -> IM 2
    im 2
endasm
site 00074   ; OUT ($BF),A
site 00078   ; OUT ($BF),A
site 0007C   ; OUT ($BF),A
site 00080   ; OUT ($BF),A
site 00084   ; OUT ($BF),A
site 00088   ; OUT ($BF),A
site 000A3   ; IN A,($BF)
site 00192   ; IN A,($DD)
site 00297   ; OUT ($BF),A
site 0029B   ; OUT ($BF),A
site 002E8   ; OUT (C),A
site 002ED   ; OUT (C),A
site 00308   ; OUT (C),A
site 0030C   ; OUT (C),A
site 00312   ; OUT (C),A
site 00319   ; OUT (C),E
site 0031E   ; OUT (C),A
site 00322   ; OUTI
site 00324   ; OUTI
site 00326   ; OUTI
site 00328   ; OUTI
site 0032A   ; OUTI
site 0032C   ; OUTI
site 0032E   ; OUTI
site 00330   ; OUTI
site 00332   ; OUTI
site 00334   ; OUTI
site 00336   ; OUTI
site 00338   ; OUTI
site 0033A   ; OUTI
site 0033C   ; OUTI
site 0033E   ; OUTI
site 00340   ; OUTI
site 00342   ; OUTI
site 00344   ; OUTI
site 00346   ; OUTI
site 00348   ; OUTI
site 0034A   ; OUTI
site 0034C   ; OUTI
site 0034E   ; OUTI
site 00350   ; OUTI
site 00352   ; OUTI
site 00354   ; OUTI
site 00356   ; OUTI
site 00358   ; OUTI
site 0035A   ; OUTI
site 0035C   ; OUTI
site 0035E   ; OUTI
site 00360   ; OUTI
site 00362   ; OUTI
site 00364   ; OUTI
site 00366   ; OUTI
site 00368   ; OUTI
site 0036A   ; OUTI
site 0036C   ; OUTI
site 0036E   ; OUTI
site 00370   ; OUTI
site 00372   ; OUTI
site 00374   ; OUTI
site 00376   ; OUTI
site 00378   ; OUTI
site 0037A   ; OUTI
site 0037C   ; OUTI
site 0037E   ; OUTI
site 00380   ; OUTI
site 00382   ; OUTI
site 00384   ; OUTI
site 00386   ; OUTI
site 00388   ; OUTI
site 0038A   ; OUTI
site 0038C   ; OUTI
site 0038E   ; OUTI
site 00390   ; OUTI
site 00392   ; OUTI
site 00394   ; OUTI
site 00396   ; OUTI
site 00398   ; OUTI
site 0039A   ; OUTI
site 0039C   ; OUTI
site 0039E   ; OUTI
site 003A0   ; OUTI
site 003A2   ; OUTI
site 003A4   ; OUTI
site 003A6   ; OUTI
site 003A8   ; OUTI
site 003AA   ; OUTI
site 003AC   ; OUTI
site 003AE   ; OUTI
site 003B0   ; OUTI
site 003B2   ; OUTI
site 003B4   ; OUTI
site 003B6   ; OUTI
site 003B8   ; OUTI
site 003BA   ; OUTI
site 003BC   ; OUTI
site 003BE   ; OUTI
site 003C0   ; OUTI
site 003C2   ; OUTI
site 003C4   ; OUTI
site 003C6   ; OUTI
site 003C8   ; OUTI
site 003CA   ; OUTI
site 003CC   ; OUTI
site 003CE   ; OUTI
site 003D0   ; OUTI
site 003D2   ; OUTI
site 003D4   ; OUTI
site 003D6   ; OUTI
site 003D8   ; OUTI
site 003DA   ; OUTI
site 003DC   ; OUTI
site 003DE   ; OUTI
site 003E0   ; OUTI
site 003E2   ; OUTI
site 003E4   ; OUTI
site 003E6   ; OUTI
site 003E8   ; OUTI
site 003EA   ; OUTI
site 003EC   ; OUTI
site 003EE   ; OUTI
site 003F0   ; OUTI
site 003F2   ; OUTI
site 003F4   ; OUTI
site 003F6   ; OUTI
site 003F8   ; OUTI
site 003FA   ; OUTI
site 003FC   ; OUTI
site 003FE   ; OUTI
site 00400   ; OUTI
site 00402   ; OUTI
site 00404   ; OUTI
site 00406   ; OUTI
site 00408   ; OUTI
site 0040A   ; OUTI
site 0040C   ; OUTI
site 0040E   ; OUTI
site 00410   ; OUTI
site 00412   ; OUTI
site 00414   ; OUTI
site 00416   ; OUTI
site 00418   ; OUTI
site 0041A   ; OUTI
site 0041C   ; OUTI
site 0041E   ; OUTI
site 00420   ; OUTI
site 00425   ; OUT (C),E
site 0042A   ; OUT (C),A
label jmf_hold 0000F
asm 0000F 40   ; unused zero filler $000F-$0036: jmf_hold, the field step hold
    push bc
    ld bc,$243B
    ld a,$05
    out (c),a
    inc b
    in a,(c)            ; NextReg $05: bit 2 set at 60 Hz
    and 4
    rrca
    rrca
    add a,3
    ld b,a              ; frames a step: 3 at 50 Hz, 4 at 60 Hz
    ld hl,$0008         ; $C7DE when the last step was released
jmf_wait:
    ld a,($C7DE)
    sub (hl)
    cp b
    jr c,jmf_wait
    ld a,($C7DE)
    ld (hl),a
    pop bc
    ld hl,$C7FA         ; as the game's code: LD HL,$C7FA; SET 6,(HL)
    set 6,(hl)
    ret
endasm
asm 001E6 5    ; LD HL,$C7FA; SET 6,(HL): the end of a field step
    call jmf_hold
    nop
    nop
endasm
asm 00F28 1    ; register table: register 0 = $16, line interrupts off
    db $06
endasm
asm 00072 2    ; LD A,$36 for register 0: line interrupts off
    ld a,$26
endasm
asm 009E0 2    ; LD A,$36 for register 0: line interrupts off
    ld a,$26
endasm
asm 05EA1 2    ; LD A,$16 for register 0: line interrupts off
    ld a,$06
endasm
asm 067F4 2    ; LD A,$16 for register 0: line interrupts off
    ld a,$06
endasm
asm 06A2E 2    ; LD A,$16 for register 0: line interrupts off
    ld a,$06
endasm
asm 06E03 2    ; LD A,$16 for register 0: line interrupts off
    ld a,$06
endasm
asm 06E98 2    ; LD A,$16 for register 0: line interrupts off
    ld a,$06
endasm
asm 06F3E 2    ; LD A,$16 for register 0: line interrupts off
    ld a,$06
endasm
asm 1B076 2    ; LD A,$16 for register 0: line interrupts off
    ld a,$06
endasm
otir 0042E   ; OUTI
site 00434   ; OUT ($BF),A
site 00439   ; OUT ($BF),A
site 0043C   ; OUT ($BE),A
site 00466   ; OUT (C),E
site 0046B   ; OUT (C),A
otir 00479   ; OUTI
site 00487   ; OUT ($BF),A
site 0048C   ; OUT ($BF),A
site 00491   ; OUT ($BE),A
site 00496   ; OUT ($BE),A
site 0049A   ; OUT ($BF),A
site 0049F   ; OUT ($BF),A
site 004A4   ; OUT ($BE),A
site 004A9   ; OUT ($BE),A
site 004AD   ; OUT ($BF),A
site 004B2   ; OUT ($BF),A
site 004B7   ; OUT ($BE),A
site 004BC   ; OUT ($BE),A
site 004C0   ; OUT ($BF),A
site 004C5   ; OUT ($BF),A
site 004CA   ; OUT ($BE),A
site 004CF   ; OUT ($BE),A
site 004D3   ; OUT ($BF),A
site 004D8   ; OUT ($BF),A
site 004DD   ; OUT ($BE),A
site 004E2   ; OUT ($BE),A
site 004E6   ; OUT ($BF),A
site 004EB   ; OUT ($BF),A
site 004F0   ; OUT ($BE),A
site 004F5   ; OUT ($BE),A
site 004F9   ; OUT ($BF),A
site 004FE   ; OUT ($BF),A
site 00503   ; OUT ($BE),A
site 00508   ; OUT ($BE),A
site 0050C   ; OUT ($BF),A
site 00511   ; OUT ($BF),A
site 00516   ; OUT ($BE),A
site 0051B   ; OUT ($BE),A
site 0051F   ; OUT ($BF),A
site 00524   ; OUT ($BF),A
site 00529   ; OUT ($BE),A
site 0052E   ; OUT ($BE),A
site 00532   ; OUT ($BF),A
site 00537   ; OUT ($BF),A
site 0053C   ; OUT ($BE),A
site 00541   ; OUT ($BE),A
site 00545   ; OUT ($BF),A
site 0054A   ; OUT ($BF),A
site 0054F   ; OUT ($BE),A
site 00554   ; OUT ($BE),A
site 00558   ; OUT ($BF),A
site 0055D   ; OUT ($BF),A
site 00562   ; OUT ($BE),A
site 00567   ; OUT ($BE),A
site 0056B   ; OUT ($BF),A
site 00570   ; OUT ($BF),A
site 00575   ; OUT ($BE),A
site 0057A   ; OUT ($BE),A
site 0057E   ; OUT ($BF),A
site 00583   ; OUT ($BF),A
site 00588   ; OUT ($BE),A
site 0058D   ; OUT ($BE),A
site 00591   ; OUT ($BF),A
site 00596   ; OUT ($BF),A
site 0059B   ; OUT ($BE),A
site 005A0   ; OUT ($BE),A
site 005A4   ; OUT ($BF),A
site 005A9   ; OUT ($BF),A
site 005AE   ; OUT ($BE),A
site 005B3   ; OUT ($BE),A
site 005B7   ; OUT ($BF),A
site 005BC   ; OUT ($BF),A
site 005C1   ; OUT ($BE),A
site 005C6   ; OUT ($BE),A
site 005CA   ; OUT ($BF),A
site 005CF   ; OUT ($BF),A
site 005D4   ; OUT ($BE),A
site 005D9   ; OUT ($BE),A
site 005DD   ; OUT ($BF),A
site 005E2   ; OUT ($BF),A
site 005E7   ; OUT ($BE),A
site 005EC   ; OUT ($BE),A
site 005F0   ; OUT ($BF),A
site 005F5   ; OUT ($BF),A
site 005FA   ; OUT ($BE),A
site 005FF   ; OUT ($BE),A
site 00603   ; OUT ($BF),A
site 00608   ; OUT ($BF),A
site 0060D   ; OUT ($BE),A
site 00612   ; OUT ($BE),A
site 00616   ; OUT ($BF),A
site 0061B   ; OUT ($BF),A
site 00620   ; OUT ($BE),A
site 00625   ; OUT ($BE),A
site 00629   ; OUT ($BF),A
site 0062E   ; OUT ($BF),A
site 00633   ; OUT ($BE),A
site 00638   ; OUT ($BE),A
site 00640   ; OUT (C),E
site 00645   ; OUT (C),A
site 0064E   ; OUT ($BE),A
site 00656   ; OUT ($BE),A
site 00675   ; OUT ($BF),A
site 0067A   ; OUT ($BF),A
site 0067D   ; OUT ($BE),A
site 00681   ; OUT ($BE),A
site 0068A   ; OUT ($BF),A
site 0068F   ; OUT ($BF),A
site 00692   ; OUT ($BE),A
site 00696   ; OUT ($BE),A
site 0095C   ; OUT ($3F),A
site 009E2   ; OUT ($BF),A
site 009E6   ; OUT ($BF),A
site 012BB   ; OUT ($BF),A
site 012BF   ; OUT ($BF),A
site 012C4   ; OUT ($BF),A
site 012C8   ; OUT ($BF),A
site 015A3   ; IN A,($DC)
site 015E1   ; IN A,($DD)
site 05BEF   ; OUT (C),E
site 05BF2   ; OUT (C),A
site 05BF6   ; IN A,(C)
site 05BFB   ; IN A,(C)
site 05BFF   ; IN A,(C)
site 05C03   ; IN A,(C)
site 05CE6   ; OUT (C),E
site 05CEB   ; OUT (C),A
site 05CF1   ; OUT (C),A
site 05CF5   ; OUT (C),A
site 05CFA   ; OUT (C),A
site 05CFE   ; OUT (C),A
site 05D03   ; OUT (C),A
site 05D07   ; OUT (C),A
site 05D0C   ; OUT (C),A
site 05D10   ; OUT (C),A
site 05D15   ; OUT (C),A
site 05D19   ; OUT (C),A
site 05D1E   ; OUT (C),A
site 05D22   ; OUT (C),A
site 05D27   ; OUT (C),A
site 05D2B   ; OUT (C),A
site 05D30   ; OUT (C),A
site 05D34   ; OUT (C),A
site 05D39   ; OUT (C),A
site 05D3D   ; OUT (C),A
site 05D67   ; OUT (C),E
site 05D6C   ; OUT (C),A
site 05D71   ; OUT (C),A
site 05D74   ; OUT (C),A
site 05D78   ; OUT (C),A
site 05D7B   ; OUT (C),A
site 05D7F   ; OUT (C),A
site 05D82   ; OUT (C),A
site 05D86   ; OUT (C),A
site 05D89   ; OUT (C),A
site 05D8D   ; OUT (C),A
site 05D90   ; OUT (C),A
site 05D94   ; OUT (C),A
site 05D97   ; OUT (C),A
site 05D9B   ; OUT (C),A
site 05D9E   ; OUT (C),A
site 05DA2   ; OUT (C),A
site 05DA5   ; OUT (C),A
site 05DA9   ; OUT (C),A
site 05DAC   ; OUT (C),A
site 05E6D   ; OUT (C),E
site 05E72   ; OUT (C),A
site 05E7B   ; OUT ($BE),A
site 05E81   ; OUT ($BE),A
site 05EA3   ; OUT ($BF),A
site 05EA7   ; OUT ($BF),A
site 06256   ; OUT (C),E
site 0625B   ; OUT (C),A
site 06266   ; OUT ($BE),A
site 0626C   ; OUT ($BE),A
site 0629C   ; OUT ($BF),A
site 062A0   ; OUT ($BF),A
site 062A4   ; OUT ($BE),A
site 067B4   ; OUT (C),E
site 067B9   ; OUT (C),A
site 067C2   ; OUT ($BE),A
site 067CA   ; OUT ($BE),A
site 067F6   ; OUT ($BF),A
site 067FA   ; OUT ($BF),A
site 06877   ; OUT ($BF),A
site 0687B   ; OUT ($BF),A
site 0687F   ; OUT ($BE),A
site 069EE   ; OUT (C),E
site 069F3   ; OUT (C),A
site 069FC   ; OUT ($BE),A
site 06A04   ; OUT ($BE),A
site 06A30   ; OUT ($BF),A
site 06A34   ; OUT ($BF),A
site 06E05   ; OUT ($BF),A
site 06E09   ; OUT ($BF),A
site 06E9A   ; OUT ($BF),A
site 06E9E   ; OUT ($BF),A
site 06F40   ; OUT ($BF),A
site 06F44   ; OUT ($BF),A
site 0721F   ; OUT (C),E
site 07224   ; OUT (C),A
site 0722D   ; OUT ($BE),A
site 0723E   ; OUT ($BE),A
site 1B078   ; OUT ($BF),A
site 1B07C   ; OUT ($BF),A
site 1B406   ; OUT (C),E
site 1B40B   ; OUT (C),A
site 1B414   ; OUT ($BE),A
site 1B427   ; OUT ($BE),A
site 2019D   ; OUT ($7F),A
site 2028F   ; OUT ($7F),A
site 20421   ; OTIR
site 20537   ; OUT ($7F),A
site 20541   ; OUT ($7F),A
site 2055E   ; OUT ($7F),A
site 20662   ; OUT ($7F),A
site 206F0   ; OUT ($7F),A
site 20775   ; OUT ($06),A
site 207BF   ; OUT ($7F),A
site 207C8   ; OUT ($7F),A
site 207D8   ; OUT ($7F),A
site 2084C   ; OUT ($7F),A
mapst 00188   ; LD ($FFFF),A
mapst 0018F   ; LD ($FFFF),A
mapst 00970   ; LD ($FFFF),A
mapst 00978   ; LD ($FFFF),A
mapst 0099F   ; LD ($FFFF),A
mapst 009EA   ; LD ($FFFF),A
mapst 05C2C   ; LD ($FFFF),A
mapst 05C43   ; LD ($FFFF),A
mapst 05C67   ; LD ($FFFF),A
mapst 05C7E   ; LD ($FFFF),A
mapst 05E99   ; LD ($FFFF),A
mapst 067E2   ; LD ($FFFF),A
mapst 06851   ; LD ($FFFF),A
mapst 06888   ; LD ($FFFF),A
mapst 0689B   ; LD ($FFFF),A
mapst 06A1C   ; LD ($FFFF),A
mapst 06AEF   ; LD ($FFFF),A
mapst 06BDE   ; LD ($FFFF),A
mapst 06BF4   ; LD ($FFFF),A
mapst 06DF1   ; LD ($FFFF),A
mapst 06E63   ; LD ($FFFF),A
mapst 06E86   ; LD ($FFFF),A
mapst 06EF8   ; LD ($FFFF),A
mapst 06F2C   ; LD ($FFFF),A
mapst 06FEE   ; LD ($FFFF),A
mapst 06FF7   ; LD ($FFFF),A
mapst 070FB   ; LD ($FFFF),A

# Joe Montana Football (USA, Europe, Brazil).cht, "Team 1 Has A High Scores": RAM $C866 is team 1's score (BCD)
poke "Team 1 score 99"
ar 00C8-6699
endpoke

# Joe Montana Football (USA, Europe, Brazil).cht, "Team 2/CPU Never Scores": RAM $C868 is team 2's score
poke "CPU never scores"
ar 00C8-6800
endpoke
