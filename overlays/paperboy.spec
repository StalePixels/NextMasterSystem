# Paperboy (Europe), CRC32 294E0759, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - The reset code clears $C000-$FEFF with one LDIR ($0014-$0017). $E000-$FEFF is the RAM
#   mirror on a Master System and the runtime's page on the Next, so the clear stops at $DFFF.
#   The reference logs show no other store into the mirror.
# - The mapper set-up at $0019-$0026 (LD (HL),A to $FFFC-$FFFF) goes through the runtime:
#   $FFFC = $80, which the game reads back at $263E (not 0: play the recorded demo at bank 1
#   $B400; 0: record a demo there), and banks 1 and 2 to $FFFE and $FFFF.
# - $589A counts loop passes in one frame to tell a 50 Hz machine from a 60 Hz one and keeps
#   the result in $D47B (0: 50 Hz; 1: 60 Hz, the sound driver skips every sixth frame). The
#   count depends on the CPU speed, so the test at $58B1 sets the 50 Hz value.
# - No tilecache: measured with and without, the play loads are the same.
# - No priority: the reference logs show no frame with priority cells on screen.
# - Unused code: the sample player at $33AC and the CRAM write at $5665.
name Paperboy
cart 294E0759
hz 50		; No-Intro region Europe
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0000E   ; OUT ($3E),A
site 00039   ; IN A,($BF)
site 003CD   ; OUT ($BF),A
site 003D1   ; OUT ($BF),A
site 0053D   ; OUT ($BE),A
site 005DE   ; OUT ($BF),A
site 005E2   ; OUT ($BF),A
site 005E5   ; OUT ($BE),A
site 00738   ; OUT ($BF),A
site 0073D   ; OUT ($BF),A
site 00759   ; OUT ($BE),A
site 0075F   ; OUT ($BE),A
site 00828   ; OUT ($BE),A
site 00D1F   ; OUT ($BE),A
site 00D4B   ; OUT ($BE),A
site 00D54   ; OUT ($BE),A
site 00F7D   ; OUT ($BF),A
site 00F80   ; OUT ($BF),A
site 00F87   ; IN A,($BE)
site 00F92   ; OUT ($BF),A
site 00F95   ; OUT ($BF),A
site 00FA2   ; INI
site 00FB3   ; OUT ($BF),A
site 00FB8   ; OUT ($BF),A
site 00FD8   ; OUT ($BE),A
site 00FE1   ; OUT ($BE),A
site 00FEA   ; OUT ($BE),A
site 00FF3   ; OUT ($BE),A
site 00FFE   ; OUT ($BF),A
site 01003   ; OUT ($BF),A
site 0100A   ; OUT ($BE),A
site 01010   ; OUT ($BE),A
site 0106D   ; OUT ($BE),A
site 01076   ; OUT ($BE),A
site 01576   ; OUT ($BF),A
site 0157A   ; OUT ($BF),A
site 01583   ; OUTI
site 01585   ; OUTI
site 01587   ; OUTI
site 01589   ; OUTI
site 0158B   ; OUTI
site 0158D   ; OUTI
site 0158F   ; OUTI
site 01591   ; OUTI
site 01593   ; OUTI
site 01595   ; OUTI
site 01597   ; OUTI
site 01599   ; OUTI
site 0159B   ; OUTI
site 0159D   ; OUTI
site 0159F   ; OUTI
site 015A1   ; OUTI
site 015A3   ; OUTI
site 015A5   ; OUTI
site 015A7   ; OUTI
site 015A9   ; OUTI
site 015AB   ; OUTI
site 015AD   ; OUTI
site 015AF   ; OUTI
site 015B1   ; OUTI
site 015B3   ; OUTI
site 015B5   ; OUTI
site 015B7   ; OUTI
site 015B9   ; OUTI
site 015BB   ; OUTI
site 015BD   ; OUTI
site 015BF   ; OUTI
site 015C1   ; OUTI
site 015C3   ; OUTI
site 015C5   ; OUTI
site 015C7   ; OUTI
site 015C9   ; OUTI
site 015CB   ; OUTI
site 015CD   ; OUTI
site 015CF   ; OUTI
site 015D1   ; OUTI
site 015D3   ; OUTI
site 015D5   ; OUTI
site 015D7   ; OUTI
site 015D9   ; OUTI
site 015DB   ; OUTI
site 015DD   ; OUTI
site 015DF   ; OUTI
site 015E1   ; OUTI
site 015E3   ; OUTI
site 015E5   ; OUTI
site 015E7   ; OUTI
site 015E9   ; OUTI
site 015EB   ; OUTI
site 015ED   ; OUTI
site 015EF   ; OUTI
site 015F1   ; OUTI
site 015F3   ; OUTI
site 015F5   ; OUTI
site 015F7   ; OUTI
site 015F9   ; OUTI
site 015FB   ; OUTI
site 015FD   ; OUTI
site 015FF   ; OUTI
site 01601   ; OUTI
site 01604   ; OUT ($BF),A
site 01607   ; OUT ($BF),A
site 0160A   ; OUTI
site 0160C   ; OUTI
site 0160E   ; OUTI
site 01610   ; OUTI
site 01612   ; OUTI
site 01614   ; OUTI
site 01616   ; OUTI
site 01618   ; OUTI
site 0161A   ; OUTI
site 0161C   ; OUTI
site 0161E   ; OUTI
site 01620   ; OUTI
site 01622   ; OUTI
site 01624   ; OUTI
site 01626   ; OUTI
site 01628   ; OUTI
site 0162A   ; OUTI
site 0162C   ; OUTI
site 0162E   ; OUTI
site 01630   ; OUTI
site 01632   ; OUTI
site 01634   ; OUTI
site 01636   ; OUTI
site 01638   ; OUTI
site 0163A   ; OUTI
site 0163C   ; OUTI
site 0163E   ; OUTI
site 01640   ; OUTI
site 01642   ; OUTI
site 01644   ; OUTI
site 01646   ; OUTI
site 01648   ; OUTI
site 0164A   ; OUTI
site 0164C   ; OUTI
site 0164E   ; OUTI
site 01650   ; OUTI
site 01652   ; OUTI
site 01654   ; OUTI
site 01656   ; OUTI
site 01658   ; OUTI
site 0165A   ; OUTI
site 0165C   ; OUTI
site 0165E   ; OUTI
site 01660   ; OUTI
site 01662   ; OUTI
site 01664   ; OUTI
site 01666   ; OUTI
site 01668   ; OUTI
site 0166A   ; OUTI
site 0166C   ; OUTI
site 0166E   ; OUTI
site 01670   ; OUTI
site 01672   ; OUTI
site 01674   ; OUTI
site 01676   ; OUTI
site 01678   ; OUTI
site 0167A   ; OUTI
site 0167C   ; OUTI
site 0167E   ; OUTI
site 01680   ; OUTI
site 01682   ; OUTI
site 01684   ; OUTI
site 01686   ; OUTI
site 01688   ; OUTI
site 0168A   ; OUTI
site 0168C   ; OUTI
site 0168E   ; OUTI
site 01690   ; OUTI
site 01692   ; OUTI
site 01694   ; OUTI
site 01696   ; OUTI
site 01698   ; OUTI
site 0169A   ; OUTI
site 0169C   ; OUTI
site 0169E   ; OUTI
site 016A0   ; OUTI
site 016A2   ; OUTI
site 016A4   ; OUTI
site 016A6   ; OUTI
site 016A8   ; OUTI
site 016AA   ; OUTI
site 016AC   ; OUTI
site 016AE   ; OUTI
site 016B0   ; OUTI
site 016B2   ; OUTI
site 016B4   ; OUTI
site 016B6   ; OUTI
site 016B8   ; OUTI
site 016BA   ; OUTI
site 016BC   ; OUTI
site 016BE   ; OUTI
site 016C0   ; OUTI
site 016C2   ; OUTI
site 016C4   ; OUTI
site 016C6   ; OUTI
site 016C8   ; OUTI
site 016CA   ; OUTI
site 016CC   ; OUTI
site 016CE   ; OUTI
site 016D0   ; OUTI
site 016D2   ; OUTI
site 016D4   ; OUTI
site 016D6   ; OUTI
site 016D8   ; OUTI
site 016DA   ; OUTI
site 016DC   ; OUTI
site 016DE   ; OUTI
site 016E0   ; OUTI
site 016E2   ; OUTI
site 016E4   ; OUTI
site 016E6   ; OUTI
site 016E8   ; OUTI
site 016EA   ; OUTI
site 016EC   ; OUTI
site 016EE   ; OUTI
site 016F0   ; OUTI
site 016F2   ; OUTI
site 016F4   ; OUTI
site 016F6   ; OUTI
site 016F8   ; OUTI
site 016FA   ; OUTI
site 016FC   ; OUTI
site 016FE   ; OUTI
site 01700   ; OUTI
site 01702   ; OUTI
site 01704   ; OUTI
site 01706   ; OUTI
site 01708   ; OUTI
site 0172A   ; OUT ($BF),A
site 0172F   ; OUT ($BF),A
site 01737   ; OUTI
site 01739   ; OUTI
site 0173B   ; OUTI
site 0173D   ; OUTI
site 0173F   ; OUTI
site 01741   ; OUTI
site 01743   ; OUTI
site 01745   ; OUTI
site 01747   ; OUTI
site 01749   ; OUTI
site 0174B   ; OUTI
site 0174D   ; OUTI
site 0174F   ; OUTI
site 01751   ; OUTI
site 01753   ; OUTI
site 01755   ; OUTI
site 01757   ; OUTI
site 01759   ; OUTI
site 0175B   ; OUTI
site 0175D   ; OUTI
site 0175F   ; OUTI
site 01761   ; OUTI
site 01763   ; OUTI
site 01765   ; OUTI
site 01767   ; OUTI
site 01769   ; OUTI
site 0176B   ; OUTI
site 0176D   ; OUTI
site 0176F   ; OUTI
site 01771   ; OUTI
site 01773   ; OUTI
site 01775   ; OUTI
site 02571   ; OUT ($BE),A
site 0273D   ; IN A,($BE)
site 02746   ; OUT ($BE),A
site 027BD   ; OUT ($BE),A
site 027C4   ; OUT ($BE),A
site 027F5   ; OUT ($BE),A
site 027FC   ; OUT ($BE),A
site 02B68   ; OUT ($BE),A
site 02B72   ; OUT ($BE),A
site 0484A   ; OUT ($7F),A
site 04866   ; OUT ($7F),A
site 04885   ; OUT ($7F),A
site 0489D   ; OUT ($7F),A
site 048AA   ; OUT ($7F),A
site 048BE   ; OUT ($7F),A
site 048CD   ; OUT ($7F),A
site 04A21   ; IN A,($BE)
site 04A28   ; IN A,($BE)
site 04A39   ; OUT ($BE),A
site 04A40   ; OUT ($BE),A
site 04A51   ; OUT ($BE),A
site 04A66   ; OUT ($BF),A
site 04A69   ; OUT ($BF),A
site 04A6F   ; OUTI
site 04A75   ; OUTI
site 04A7B   ; OUTI
site 04A81   ; OUTI
site 04AC7   ; OUT ($BF),A
site 04ACA   ; OUT ($BF),A
site 04AD0   ; OUTI
site 04AD6   ; OUTI
site 04ADC   ; OUTI
site 04AE2   ; OUTI
site 0535C   ; IN A,($DD)
site 05391   ; IN A,($DD)
site 053B6   ; OTIR
site 0549A   ; OUT ($BF),A
site 054A3   ; OUT ($BF),A
site 054B0   ; OUT ($BE),A
site 054B5   ; OUT ($BE),A
site 05573   ; OUT ($BF),A
site 05577   ; OUT ($BF),A
site 05581   ; OUTI
site 055E6   ; OUT ($BF),A
site 055F0   ; OUT ($BF),A
site 055FD   ; OUT ($BE),A
site 05603   ; OUT ($BE),A
site 05614   ; OUT ($BF),A
site 05619   ; OUT ($BF),A
site 0561D   ; OUT ($BE),A
site 05623   ; OUT ($BE),A
site 0562D   ; OUT ($BE),A
site 0563A   ; OUT ($BF),A
site 0563D   ; OUT ($BF),A
site 0564D   ; OUT ($BF),A
site 05654   ; OUT ($BF),A
site 0565D   ; OUT ($BE),A
site 056D0   ; OUT ($3F),A
site 056D2   ; IN A,($DC)
site 05778   ; OUT ($BE),A
site 06FA6   ; OUT ($BF),A
site 06FA9   ; OUT ($BF),A
site 06FB0   ; OUT ($BE),A
site 06FB7   ; OUT ($BE),A
site 07094   ; OUT ($BE),A
site 07099   ; OUT ($BE),A
site 0709E   ; OUT ($BE),A
site 070A3   ; OUT ($BE),A
site 07106   ; OUT ($BE),A
site 0710D   ; OUT ($BE),A
site 07112   ; OUT ($BE),A
site 0711F   ; OUT ($BE),A
site 0712F   ; OUT ($BE),A
site 07161   ; OUT ($BE),A
site 07168   ; OUT ($BE),A
asm 00014 3   ; LD BC,$3F00: the reset clear of $C000-$FEFF, whose $E000-$FEFF is the RAM mirror
    ld bc,$1FFF   ; $C000-$DFFF only: $E000-$FFFF is the runtime's page on the Next
endasm
asm 00019 14  ; LD L,$FC; LD A,$80; LD (HL),A; INC HL; XOR A; LD (HL),A; INC HL; INC A; LD (HL),A; INC HL; INC A; LD (HL),A
    ld a,$80
    rst $00
    db $10, 0     ; LD ($FFFC),A: $80, read back at $263E
    ld hl,$0201
    rst $00
    db $17, 0     ; LD ($FFFE),HL: bank 1 to $FFFE, bank 2 to $FFFF
    ld a,2
    nop
endasm
asm 058B1 5   ; DI; LD A,B; CP $0D: the speed test of $589A, which counts loop passes in a frame
    di
    xor a         ; $D47B = 0, the PAL value
    jp $58CB
endasm
mapst 00693   ; LD ($FFFF),A
mapst 0071D   ; LD ($FFFF),A
mapst 00D37   ; LD ($FFFF),A
mapst 00F79   ; LD ($FFFF),A
mapst 0105F   ; LD ($FFFF),A
mapst 01724   ; LD ($FFFF),A
mapst 0264B   ; LD ($FFFF),A
mapst 02666   ; LD ($FFFF),A
mapst 027CB   ; LD ($FFFF),A
mapst 04AAE   ; LD ($FFFF),A
mapst 04D84   ; LD ($FFFF),A
mapst 04E0E   ; LD ($FFFF),A
mapst 04F31   ; LD ($FFFF),A
mapst 05490   ; LD ($FFFF),A
mapst 055BC   ; LD ($FFFF),A
mapst 0570D   ; LD ($FFFF),A
mapst 05722   ; LD ($FFFF),A
mapst 06FF1   ; LD ($FFFF),A
mapst 07022   ; LD ($FFFF),A
mapst 07060   ; LD ($FFFF),A
mapst 070D5   ; LD ($FFFF),A
mapst 07142   ; LD ($FFFF),A
mapst 0717B   ; LD ($FFFF),A
# CHECK cartarea_store at 02651 ($2651 bank 0): 22 00 B4  LD ($B400),HL $B400,$B401
# CHECK indirect_unresolved at 02CAF ($2CAF bank 0): E9  JP (HL) 
# Mapper stores found by the byte scan in bytes no path reached:
# CHECK byte scan medium: mapst 033AC  LD ($FFFF),A  (32 bytes of valid code before it)
# CHECK byte scan low: mapst 1C9AC  LD ($FFFF),A  (10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 033B1  OUT ($7F),A  (psg; after LD A,$80; 32 bytes of valid code before it)
# CHECK medium: site 033B4  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK high: site 033B8  OUT ($7F),A  (psg; after LD A,$A0; 32 bytes of valid code before it)
# CHECK medium: site 033BB  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK high: site 033BF  OUT ($7F),A  (psg; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 033C2  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK medium: site 033C5  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK medium: site 033D5  OUTI  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 033D7  OUTI  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 033D9  OUTI  (port in C; 32 bytes of valid code before it)
# CHECK high: site 033E7  OUT ($7F),A  (psg; after LD A,$90; 32 bytes of valid code before it)
# CHECK high: site 033EB  OUT ($7F),A  (psg; after LD A,$B0; 32 bytes of valid code before it)
# CHECK high: site 033EF  OUT ($7F),A  (psg; after LD A,$D0; 32 bytes of valid code before it)
# CHECK medium: site 05666  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 0566D  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 05673  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 14342  OTDR  (port in C; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 19A8A  IN A,($7F)  (h_counter; no valid code after it)
# CHECK low: site 19BA2  OTDR  (port in C; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1C44A  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 1E2CF  IN A,($DC)  (joypad_a; no valid code after it)

# Paperboy (Europe).cht, "Infinite Lives": RAM $D50E is the number of lives (hats), held at 9
poke "Infinite lives"
ar 00D5-0E09
endpoke

# Paperboy (Europe).cht, "Infinite Papers": RAM $D50F is the papers in the bag, held at 10
poke "Infinite papers"
ar 00D5-0F0A
endpoke
