# Marble Madness (Europe), CRC32 BF6F3E5F, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - No free RST vector: $0008, $0018, $0020 and $0028 are the game's, and the game reads
#   $0013-$0016 as data, so $0000 is the io vector.
# - The game's stack starts at $DFFC, not $DFEA. The game keeps variables up to $DFD4
#   (the option screen's values, the interrupt counter $DFCB) and its own stack goes no
#   lower than $DFD8; the runtime's traps push a few bytes more and overwrote $DFD4, so
#   the option screen showed START LEVEL A and the game crashed at the first race.
#   $DFEC-$DFFB is free: the only other use is one write of $DFEE that nothing reads.
# - The routine $14EB counts loop passes over 63 interrupts and sets $D707 from the
#   count. On the Next the line interrupt at line 191 and the frame event come back to
#   back (the handler's two traps take longer than a Next line), the counter at $DFCB
#   steps past $3F and the loop never ended. The loop now ends at $3F or more, and
#   $D707 (a note offset in the sound driver) is always 0, the value of a PAL Master
#   System; the count means nothing at the Next's speed.
# - $0008-$0394 holds the cart's development monitor (RST $18, $20 and $28, the reset
#   button routine at $0072). No recording ran it; its I/O and mapper stores are patched
#   anyway. Its LD (HL),A at $009A writes $CE to $FFFF: the asm block writes it in the
#   maphl form.
# - The bytes $03B5-$03FF after JP NZ,$0400 at $03B2 are a table: the jump is always
#   taken (the byte at $0007 is $01).
# - The jump table at $4B0E has 8 code entries; the 4 words after them point at data in
#   bank 1 ($4B26-$4B3B), which the scanner decodes as code.
# - No priority: name table cells with the priority bit show only under the "TIME TO
#   FINISH" box at the start of a race, and no sprite is under them in any reference
#   dump.
# - Unused code: the bank 1 tile routine $48AF and the bank 1 interrupt handler $7BEB.
#   Data: the I/O byte patterns in banks 5, 7 and 13.
name Marble Madness
cart BF6F3E5F
hz 50		; No-Intro region Europe
vector 00 io
start 0004 DFFC
asm 00396 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00401 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00403 3   ; LD SP,$DFEA: the stack starts below the mapper copies at $DFFC
    ld sp,$DFFC
endasm
asm 0043B 3   ; LD SP,$DFEA
    ld sp,$DFFC
endasm
asm 00096 5   ; LD A,(HL); PUSH AF; LD A,$CE; LD (HL),A with HL = $FFFF
    ld a,(hl)
    push af
    rst $00
    db $3E        ; maphl form: bank 14 ($CE on a 256K cart) to $FFFF; A is loaded again at $009C
endasm
asm 01505 2   ; JR NZ,$1509: the speed loop ends at 63 interrupts or more
    jr c,$1509
endasm
asm 004EA 2   ; JR C,$04EE: $D707 = 0, the PAL value
    jr $04EE
endasm
asm 00C47 2   ; JR C,$0C4E: $D707 keeps the PAL value
    jr $0C4E
endasm
site 0000A   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0003B   ; IN A,($C1)
site 0008D   ; OUT ($BF),A
site 003A6   ; IN A,($BF)
site 0067B   ; OUTI
site 0068A   ; OUT ($BF),A
site 0068F   ; OUT ($BF),A
site 006A1   ; OUT ($BE),A
site 006A9   ; OUT ($BE),A
site 01410   ; OUT ($BE),A
site 01417   ; OUT ($BE),A
site 0141E   ; OUT ($BE),A
site 01426   ; OUT ($BE),A
site 01432   ; OUT ($BE),A
site 01462   ; OUT (C),A
site 01497   ; OUT (C),A
site 014A1   ; OUT (C),A
site 014AA   ; OUT (C),A
site 014B3   ; OUT ($BE),A
site 014C0   ; OUT (C),A
site 014C9   ; OUT ($BE),A
site 014D1   ; OUT (C),A
site 014D9   ; OUT ($BE),A
site 014E0   ; OUT (C),E
site 014E8   ; OUT ($BE),A
site 01E82   ; OUT ($BE),A
site 01E89   ; OUT ($BE),A
site 02094   ; OUT ($BF),A
site 02098   ; OUT ($BF),A
site 020C0   ; OUT ($BE),A
site 020C5   ; OUT ($BE),A
site 020CA   ; OUT ($BE),A
site 020D1   ; OUT (C),B
site 020D5   ; OUT ($BE),A
site 020DA   ; OUT ($BE),A
site 020DF   ; OUT ($BE),A
site 020E6   ; OUT (C),B
site 020EA   ; OUT ($BE),A
site 020EF   ; OUT ($BE),A
site 020F4   ; OUT ($BE),A
site 020FB   ; OUT (C),B
site 020FF   ; OUT ($BE),A
site 02104   ; OUT ($BE),A
site 02109   ; OUT ($BE),A
site 02110   ; OUT (C),B
site 02114   ; OUT ($BE),A
site 02119   ; OUT ($BE),A
site 0211E   ; OUT ($BE),A
site 02125   ; OUT (C),B
site 02129   ; OUT ($BE),A
site 0212E   ; OUT ($BE),A
site 02133   ; OUT ($BE),A
site 0213A   ; OUT (C),B
site 0213E   ; OUT ($BE),A
site 02143   ; OUT ($BE),A
site 02148   ; OUT ($BE),A
site 0214F   ; OUT (C),B
site 02153   ; OUT ($BE),A
site 02158   ; OUT ($BE),A
site 0215D   ; OUT ($BE),A
site 02164   ; OUT (C),B
site 02215   ; OUT ($BF),A
site 0221B   ; OUT ($BF),A
site 02246   ; OUT ($BE),A
site 0224D   ; OUT (C),D
site 0225D   ; OUT ($BF),A
site 02263   ; OUT ($BF),A
site 02291   ; OUT (C),A
site 022AB   ; OUT ($BE),A
site 02A51   ; OUT ($BF),A
site 02A56   ; OUT ($BF),A
site 02A5D   ; OUT ($BE),A
site 02A64   ; OUT ($BE),A
site 02A70   ; OUT ($BE),A
site 02A77   ; OUT ($BE),A
site 02B90   ; OUT ($BF),A
site 02B94   ; OUT ($BF),A
site 02BC0   ; OUTI
site 02BC3   ; OUTI
site 02BC6   ; OUTI
site 02BCA   ; OUT (C),A
site 02E2F   ; OUT ($BF),A
site 02E36   ; OUT ($BF),A
site 02E90   ; OUT (C),E
site 02E96   ; OUT (C),E
site 02E9C   ; OUT ($BE),A
site 02EA2   ; OUT ($BE),A
site 02EBD   ; OUT (C),E
site 02EC2   ; OUT (C),E
site 02EC8   ; OUT (C),E
site 02ECE   ; OUT (C),A
site 02EE9   ; OUT (C),E
site 02EEE   ; OUT (C),E
site 02EF2   ; OUT ($BE),A
site 02EF8   ; OUT ($BE),A
site 02F16   ; OUT (C),E
site 02F1B   ; OUT (C),E
site 02F20   ; OUT (C),E
site 02F27   ; OUT ($BE),A
site 02F44   ; OUT (C),A
site 02F49   ; OUT (C),A
site 02F4E   ; OUT (C),A
site 02F56   ; OUT (C),A
site 03197   ; OUT ($BF),A
site 0319B   ; OUT ($BF),A
site 031C3   ; OUTI
site 031C5   ; OUTI
site 031C7   ; OUTI
site 031C9   ; OUT ($BE),A
site 031CB   ; OUTI
site 031CD   ; OUTI
site 031CF   ; OUTI
site 031D1   ; OUT ($BE),A
site 031D3   ; OUTI
site 031D5   ; OUTI
site 031D7   ; OUTI
site 031D9   ; OUT ($BE),A
site 031DB   ; OUTI
site 031DD   ; OUTI
site 031DF   ; OUTI
site 031E1   ; OUT ($BE),A
site 031E3   ; OUTI
site 031E5   ; OUTI
site 031E7   ; OUTI
site 031E9   ; OUT ($BE),A
site 031EB   ; OUTI
site 031ED   ; OUTI
site 031EF   ; OUTI
site 031F1   ; OUT ($BE),A
site 031F3   ; OUTI
site 031F5   ; OUTI
site 031F7   ; OUTI
site 031F9   ; OUT ($BE),A
site 031FB   ; OUTI
site 031FD   ; OUTI
site 031FF   ; OUTI
site 03201   ; OUT ($BE),A
site 03323   ; OUT ($BF),A
site 0332A   ; OUT ($BF),A
site 03339   ; OUT ($BE),A
site 0333F   ; OUT (C),A
site 03345   ; OUT ($BE),A
site 0334B   ; OUT (C),A
site 0337F   ; OUT ($BF),A
site 03383   ; OUT ($BF),A
site 0339F   ; OUT ($BF),A
site 033A3   ; OUT ($BF),A
site 033A8   ; OUTI
site 033AC   ; OUTI
site 033B0   ; OUTI
site 033B4   ; OUTI
site 033B8   ; OUTI
site 033BC   ; OUTI
site 033C0   ; OUTI
site 033C4   ; OUTI
site 03593   ; OUT ($BF),A
site 03597   ; OUT ($BF),A
site 035BE   ; OUTI
site 035C3   ; OUTI
site 035C8   ; OUTI
site 035CE   ; OUT ($BE),A
site 035D3   ; OUTI
site 035D8   ; OUTI
site 035DD   ; OUTI
site 035E3   ; OUT ($BE),A
site 035E8   ; OUTI
site 035ED   ; OUTI
site 035F2   ; OUTI
site 035F8   ; OUT ($BE),A
site 035FD   ; OUTI
site 03602   ; OUTI
site 03607   ; OUTI
site 0360D   ; OUT ($BE),A
site 03612   ; OUTI
site 03617   ; OUTI
site 0361C   ; OUTI
site 03622   ; OUT ($BE),A
site 03627   ; OUTI
site 0362C   ; OUTI
site 03631   ; OUTI
site 03637   ; OUT ($BE),A
site 0363C   ; OUTI
site 03641   ; OUTI
site 03646   ; OUTI
site 0364C   ; OUT ($BE),A
site 03651   ; OUTI
site 03656   ; OUTI
site 0365B   ; OUTI
site 03661   ; OUT ($BE),A
site 038F7   ; OUT ($BE),A
site 03901   ; OUT ($BF),A
site 03905   ; OUT ($BF),A
site 0390D   ; OUT ($BE),A
site 03927   ; OUT ($BF),A
site 0392E   ; OUT ($BF),A
site 03937   ; OUT ($BE),A
site 0393B   ; OUT ($BF),A
site 03942   ; OUT ($BF),A
site 03945   ; OUT ($BE),A
site 0394E   ; IN A,($DD)
site 03955   ; IN A,($DC)
site 03A54   ; OUT (C),E
site 03A5A   ; OUT (C),E
site 03A60   ; OUT (C),A
site 03A66   ; OUT (C),A
site 03A7F   ; OUT (C),E
site 03A85   ; OUT (C),A
site 03A8C   ; OUT ($BF),A
site 03A92   ; OUT ($BF),A
site 03A97   ; OUT ($BE),A
site 03B07   ; OUT ($BE),A
site 03B0E   ; OUT ($BE),A
site 03BA2   ; OUT ($BE),A
site 03BA9   ; OUT ($BE),A
site 03BBA   ; OUT ($BE),A
site 03D36   ; OUT ($BF),A
site 03D3B   ; OUT ($BF),A
site 03D53   ; OUT (C),A
site 03D59   ; OUT (C),E
site 03D60   ; OUT (C),A
site 03D67   ; OUT (C),A
site 03D92   ; OUT (C),L
site 03D98   ; OUT (C),A
site 03D9F   ; OUT (C),A
site 03DA5   ; OUT (C),A
site 03DC1   ; OUT (C),A
site 03DC8   ; OUT (C),A
site 03DCC   ; OUT ($BF),A
site 03DD3   ; OUT ($BF),A
site 03DD7   ; OUT (C),L
site 03DDE   ; OUT (C),H
site 03E25   ; OUT ($BE),A
site 03E97   ; OUT ($BE),A
site 03E9F   ; OUT ($BE),A
site 03EA7   ; OUT ($BE),A
site 03EAE   ; OUT ($BE),A
site 03EC2   ; OUT ($BE),A
site 03ECB   ; OUT ($BE),A
site 03F3A   ; OUT ($BE),A
site 03F42   ; OUT ($BE),A
site 03F6D   ; OUT ($BE),A
site 03F75   ; OUT ($BE),A
site 03F7C   ; OUT ($BE),A
site 03F84   ; OUT ($BE),A
site 03F8E   ; OUT ($BE),A
site 03F96   ; OUT ($BE),A
site 03F9E   ; OUT ($BE),A
site 03FA6   ; OUT ($BE),A
site 03FB0   ; OUT ($BE),A
site 03FB8   ; OUT ($BE),A
site 03FC0   ; OUT ($BE),A
site 03FC7   ; OUT ($BE),A
site 03FCF   ; OUT ($BF),A
site 03FD4   ; OUT ($BF),A
site 04031   ; OUT ($BE),A
site 04038   ; OUT ($BE),A
site 04056   ; OUT ($BE),A
site 0405F   ; OUT ($BE),A
site 04067   ; OUT ($BE),A
site 04071   ; OUT ($BE),A
site 0415C   ; OUT ($BE),A
site 04165   ; OUT ($BE),A
site 04171   ; OUT ($BE),A
site 0417A   ; OUT ($BE),A
site 04739   ; OUT (C),A
site 0473F   ; OUT (C),A
site 04745   ; OUT (C),A
site 0474B   ; OUT (C),A
site 0476B   ; OUT (C),A
site 0476F   ; OUT (C),A
site 04773   ; OUT (C),A
site 04777   ; OUT (C),A
site 078CF   ; OUT ($7F),A
site 078D3   ; OUT ($7F),A
site 078E0   ; OUT ($7F),A
site 078E4   ; OUT ($7F),A
site 07915   ; OUT ($7F),A
site 0792C   ; OUT ($7F),A
site 07939   ; OUT ($7F),A
site 07948   ; OUT ($7F),A
site 0795F   ; OUT ($7F),A
site 0796C   ; OUT ($7F),A
site 07992   ; OUT ($7F),A
site 079A5   ; OUT ($7F),A
site 079BC   ; OUT ($7F),A
site 079C2   ; OUT ($7F),A
site 079E6   ; OUT ($7F),A
site 079FD   ; OUT ($7F),A
site 07A0A   ; OUT ($7F),A
site 07A67   ; OUT ($7F),A
site 07C60   ; OUT ($7F),A
site 07C65   ; OUT ($7F),A
site 07C79   ; OUT ($7F),A
site 07C8C   ; OUT ($7F),A
site 07C98   ; OUT ($7F),A
site 07CAB   ; OUT ($7F),A
mapst 00056   ; LD ($FFFF),A
mapst 000B9   ; LD ($FFFF),A
mapst 000C3   ; LD ($FFFF),A
mapst 000D1   ; LD ($FFFF),A
mapst 0020D   ; LD ($FFFF),A
mapst 00398   ; LD ($FFFC),A
mapst 0039B   ; LD ($FFFD),A
mapst 0039F   ; LD ($FFFE),A
mapst 003A3   ; LD ($FFFF),A
mapst 0050A   ; LD ($FFFF),A
mapst 0066C   ; LD ($FFFF),A
mapst 006C6   ; LD ($FFFF),A
mapst 007A9   ; LD ($FFFF),A
mapst 00CBC   ; LD ($FFFF),A
mapst 01001   ; LD ($FFFF),A
mapst 01194   ; LD ($FFFF),A
mapst 012D7   ; LD ($FFFF),A
mapst 01E4C   ; LD ($FFFF),A
mapst 01F70   ; LD ($FFFF),A
mapst 02BAA   ; LD ($FFFF),A
mapst 02E16   ; LD ($FFFF),A
mapst 02FBF   ; LD ($FFFF),A
mapst 031B2   ; LD ($FFFF),A
mapst 0320E   ; LD ($FFFF),A
mapst 032E5   ; LD ($FFFF),A
mapst 0346D   ; LD ($FFFF),A
mapst 03491   ; LD ($FFFF),A
mapst 034F2   ; LD ($FFFF),A
mapst 03535   ; LD ($FFFF),A
mapst 035AD   ; LD ($FFFF),A
mapst 03979   ; LD ($FFFF),A
mapst 03A3C   ; LD ($FFFF),A
mapst 03BCA   ; LD ($FFFF),A
mapst 03D06   ; LD ($FFFF),A
mapst 03E4B   ; LD ($FFFF),A
mapst 03FDB   ; LD ($FFFF),A
mapst 041DC   ; LD ($FFFF),A
mapst 0426D   ; LD ($FFFF),A
mapst 043E0   ; LD ($FFFF),A
mapst 044C9   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 000DF   # LD ($FFFF),A; after LD A,$CE
mapst 0018B   # LD ($FFFF),A; in the monitor's command code
mapst 0019E   # LD ($FFFF),A; in the monitor's command code
mapst 0021F   # LD ($FFFF),A; after LD A,$CE; 32 bytes of valid code before it
mapst 00230   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 00255   # LD ($FFFF),A; after LD A,$CE
mapst 00261   # LD ($FFFF),A; after LD A,$89; 16 bytes of valid code before it
mapst 0027A   # LD ($FFFF),A; after LD A,$CE
mapst 0028D   # LD ($FFFF),A; after LD A,$89; 23 bytes of valid code before it
mapst 002D9   # LD ($FFFF),A; after LD A,$CE
mapst 002F0   # LD ($FFFF),A; after LD A,$89; 27 bytes of valid code before it
mapst 002FC   # LD ($FFFF),A; after LD A,$CE; JP/CALL target from $073DB $09BB4
mapst 0031B   # LD ($FFFF),A; after LD A,$89; 32 bytes of valid code before it
mapst 0032A   # LD ($FFFF),A; after LD A,$CE
mapst 00343   # LD ($FFFF),A; after LD A,$89; 29 bytes of valid code before it

# Marble Madness (Europe).cht, "Infinite Time" (3AD-16F-2A2): the store of the new time
# at $0D16 (LD ($DFC4),A) becomes a load, so the race clock stays at its starting value
poke "Infinite time"
gg 3AD-16F-2A2
endpoke

# Marble Madness (Europe).cht, "Enable Stage Select" (00DF-D002+00DF-D205): RAM $DFD0 = $02
# and $DFD2 = $05 are the title menu's TEST FX and TEST TUNE values that unlock the START
# LEVEL line; the cursor then reaches it and the level can be chosen
# The poke adds a START LEVEL line to the title menu; the player picks the level there.
poke "Level select"
ar 00DF-D002
ar 00DF-D205
endpoke
