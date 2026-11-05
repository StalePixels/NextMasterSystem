# Xenon 2 - Megablast (Europe) (Rev 1), CRC32 EC726C0D, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - The reset code clears $C000-$FFFB with one LDIR; $E000-$FFFB is the RAM mirror on a
#   Master System and the runtime's page on the Next, so the clear stops at $DFFF.
# - The mapper set-up at $0104-$010E (LDIR of 00 00 01 02 to $FFFC-$FFFF) goes through the runtime.
# - LD I,A is the game's delay between VDP port accesses; the framework needs I for IM 2.
# - $1542 counts loop passes in one frame to tell 50 Hz from 60 Hz; the count depends on the
#   CPU speed, so the test sets the 50 Hz value.
# - The call at $71C3 into slot 2 ($8673) is the font lookup in bank 2.
# - Unused code (no reference names it): $06BE-$06EA, $0817, $0C98, $0CF2, $0F48, $1A80,
#   $1CFD, $2020-$208E, $236B, $2519, $25DE, $285D, $620C-$6222, $7FD5, bank 2 $8680.
name Xenon 2 - Megablast
cart EC726C0D
hz 50		; No-Intro region Europe
# No free RST vector: $0000-$0002 (DI; JP $0005) becomes the vector,
# the game starts at $0005 (the framework does DI and IM 2).
vector 00 io
start 0005
asm 0000B 3   ; LD BC,$3FFB: the reset clear of $C000-$FFFB, whose $E000-$FFFB is the RAM mirror
    ld bc,$1FFF   ; $C000-$DFFF only: $E000-$FFFF is the runtime's page on the Next
endasm
asm 00104 11  ; LD HL,$296C; LD DE,$FFFC; LD BC,4; LDIR: 00 00 01 02 to $FFFC-$FFFF
    ld hl,$0201
    rst $00
    db $17, 0     ; LD ($FFFE),HL: bank 1 to $FFFE, bank 2 to $FFFF
endasm
asm 01542 5   ; DI; LD C,$7E; LD HL,$0000: the speed test of $1542, which counts loop passes in a frame
    xor a         ; $DE27 = 0, the PAL value (not 0: the music at bank 11 $AA92 skips every sixth frame)
    ld ($DE27),a
    ret
endasm
# LD I,A (ED 47) is the game's delay between VDP port accesses; the game never reads I.
# The framework needs I for IM 2, so each one becomes NOPs (the cart has no other ED 47 bytes).
asm 00678 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 0067F 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 006A5 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 006F5 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 006FC 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 0081C 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 00828 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 011BD 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 018A7 2   ; LD I,A
    nop
    nop
endasm
asm 018AC 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01A84 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01A8B 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01D04 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01D0A 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01D12 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01D1A 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01D20 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01F6D 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01F73 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01F83 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01F89 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01F99 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 01F9F 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 0203D 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 02075 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 0207C 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 02084 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 02577 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 0257D 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 02585 4   ; LD I,A; LD I,A
    nop
    nop
    nop
    nop
endasm
asm 026BF 2   ; LD I,A
    nop
    nop
endasm
asm 026C5 2   ; LD I,A
    nop
    nop
endasm
asm 026CB 2   ; LD I,A
    nop
    nop
endasm
asm 04617 2   ; LD I,A
    nop
    nop
endasm
site 00383   ; OUT ($BF),A
site 00386   ; OUT ($BF),A
site 00389   ; OUT ($BE),A
site 0038E   ; OUT ($BE),A
site 0065C   ; OUT ($BF),A
site 00660   ; OUT ($BF),A
site 00664   ; IN A,($DC)
site 0066A   ; IN A,($DC)
site 00674   ; OUT (C),B
site 0067C   ; OUT (C),A
site 00683   ; OUT ($BE),A
site 006A1   ; OUT ($BF),A
site 006A9   ; OUT ($BF),A
otir 006AF   ; OUTI
otir 006B7   ; OUTI
site 006F9   ; OUTI
site 00700   ; OUT (C),A
site 0075A   ; OUT ($7F),A
site 0075E   ; OUT ($7F),A
site 00762   ; OUT ($7F),A
site 00766   ; OUT ($7F),A
site 0076A   ; OUT ($BF),A
site 0076E   ; OUT ($BF),A
site 00774   ; OUT ($BE),A
site 007E9   ; OUT ($BF),A
site 007ED   ; OUT ($BF),A
site 007F3   ; OUT ($BE),A
site 007F8   ; OUT ($BF),A
site 007FC   ; OUT ($BF),A
site 00802   ; OUT ($BE),A
site 009B5   ; IN A,($DC)
site 009CF   ; IN A,($DC)
site 009FE   ; IN A,($DC)
site 00A39   ; IN A,($DC)
site 00BEB   ; OUT (C),E
site 00BED   ; OUT (C),D
otir 00BF2   ; OUTI
site 00BFE   ; OUT (C),L
site 00C00   ; OUT (C),H
otir 00C06   ; OUTI
site 00C15   ; OUT (C),E
site 00C19   ; OUT (C),D
otir 00C1C   ; OUTI
site 00C2B   ; OUT (C),E
site 00C2F   ; OUT (C),D
otir 00C32   ; OUTI
site 00C6B   ; OUT (C),E
site 00C6D   ; OUT (C),D
otir 00C6F   ; OUTI
site 00C76   ; OUT (C),L
site 00C78   ; OUT (C),H
site 00CAD   ; OUTI
site 00CAF   ; OUTI
site 00CB1   ; OUTI
site 00CB3   ; OUTI
site 00CB5   ; OUTI
site 00CB7   ; OUTI
site 00CB9   ; OUTI
site 00CBB   ; OUTI
site 00CBD   ; OUTI
site 00CBF   ; OUTI
site 00CC1   ; OUTI
site 00CC3   ; OUTI
site 00CC5   ; OUTI
site 00CC7   ; OUTI
site 00CC9   ; OUTI
site 00CCB   ; OUTI
site 00CCD   ; OUTI
site 00CCF   ; OUTI
site 00CD1   ; OUTI
site 00CD3   ; OUTI
site 00CD5   ; OUTI
site 00CD7   ; OUTI
site 00CD9   ; OUTI
site 00CDB   ; OUTI
site 00CDD   ; OUTI
site 00CDF   ; OUTI
site 00CE1   ; OUTI
site 00CE3   ; OUTI
site 00CE5   ; OUTI
site 00CE7   ; OUTI
site 00CE9   ; OUTI
site 00CEB   ; OUTI
site 00D33   ; OUT ($BF),A
site 00D37   ; OUT ($BF),A
site 00D3B   ; OUT ($BF),A
site 00D3F   ; OUT ($BF),A
site 00D56   ; IN A,($DD)
site 00E2A   ; IN A,($BF)
site 00E30   ; IN A,($7E)
site 00E7D   ; OUT ($BF),A
site 00E81   ; OUT ($BF),A
site 00E85   ; OUTI
site 00E8A   ; OUTI
site 00E8F   ; OUTI
site 00E94   ; OUTI
site 00E99   ; OUTI
site 00E9E   ; OUTI
site 00EA3   ; OUTI
site 00EA8   ; OUTI
site 00EAD   ; OUTI
site 00EB2   ; OUTI
site 00EB7   ; OUTI
site 00EBC   ; OUTI
site 00EC1   ; OUTI
site 00EC6   ; OUTI
site 00ECB   ; OUTI
site 00ED0   ; OUTI
site 00ED6   ; OUT ($BF),A
site 00EDA   ; OUT ($BF),A
site 00EDE   ; OUTI
site 00EE3   ; OUTI
site 00EE8   ; OUTI
site 00EED   ; OUTI
site 00EF2   ; OUTI
site 00EF7   ; OUTI
site 00EFC   ; OUTI
site 00F01   ; OUTI
site 00F1E   ; IN A,($7E)
site 00F28   ; IN A,(C)
site 00F32   ; OUT (C),B
site 00F37   ; OUT (C),B
site 00F3F   ; OUT (C),B
site 00F44   ; OUT (C),B
site 011B9   ; OUT ($BF),A
site 011C1   ; OUT ($BF),A
otir 011C7   ; OUTI
site 011D0   ; OUT ($BF),A
site 011D4   ; OUT ($BF),A
site 011DA   ; OUT ($BE),A
site 011E5   ; OUT ($BF),A
site 011E9   ; OUT ($BF),A
site 011EF   ; OUT ($BE),A
site 011FB   ; OUT (C),E
site 011FF   ; OUT (C),D
otir 01202   ; OUTI
site 0120B   ; OUT (C),E
site 0120F   ; OUT (C),D
site 01213   ; OUT (C),A
site 01219   ; OUT (C),A
site 0122A   ; OUT ($BF),A
site 0122E   ; OUT ($BF),A
site 0123E   ; OUT ($BF),A
site 01242   ; OUT ($BF),A
site 014EE   ; OUTI
site 014F2   ; OUTI
site 014F6   ; OUTI
site 014FA   ; OUTI
site 01508   ; OUTI
site 0150C   ; OUTI
site 01510   ; OUTI
site 01514   ; OUTI
site 01539   ; OUT ($BF),A
site 0153F   ; OUT ($BF),A
site 0154A   ; IN B,(C)
site 0154F   ; IN B,(C)
site 0189A   ; OUT ($BF),A
site 0189F   ; OUT (C),B
site 018A2   ; OUT (C),D
site 018A9   ; OUT ($BF),A
site 018B0   ; OUT (C),B
site 018B6   ; OUT (C),E
site 018BC   ; OUT ($BE),A
site 01940   ; OUT ($BF),A
site 01944   ; OUT ($BF),A
site 0194A   ; OUT ($BE),A
site 0194C   ; OUT ($BE),A
site 0194E   ; OUT ($BE),A
site 01950   ; OUT ($BE),A
site 01952   ; OUT ($BE),A
site 01954   ; OUT ($BE),A
site 01956   ; OUT ($BE),A
site 01958   ; OUT ($BE),A
site 01D64   ; OUT (C),L
site 01D66   ; OUT (C),H
site 01D68   ; IN A,($BE)
site 01D6A   ; OUT (C),E
site 01D6C   ; OUT (C),D
site 01D70   ; OUT ($BE),A
site 01D98   ; OUT (C),L
site 01D9A   ; OUT (C),H
site 01D9C   ; IN A,($BE)
site 01D9E   ; OUT (C),E
site 01DA0   ; OUT (C),D
site 01DA4   ; OUT ($BE),A
site 01F62   ; OUT (C),E
site 01F64   ; OUT (C),D
site 01F6B   ; OUT ($BE),A
site 01F71   ; OUT ($BE),A
site 01F77   ; OUT ($BE),A
site 01F7D   ; OUT (C),L
site 01F7F   ; OUT (C),H
site 01F81   ; OUT ($BE),A
site 01F87   ; OUT ($BE),A
site 01F8D   ; OUT ($BE),A
site 01F93   ; OUT (C),L
site 01F95   ; OUT (C),H
site 01F97   ; OUT ($BE),A
site 01F9D   ; OUT ($BE),A
site 01FA3   ; OUT ($BE),A
site 020C1   ; OUT (C),B
site 020C6   ; OUT (C),B
site 020CE   ; OUT (C),B
site 020D3   ; OUT (C),B
site 020D7   ; OUT ($BF),A
site 020DB   ; OUT ($BF),A
site 020DF   ; OUT ($BF),A
site 020E3   ; OUT ($BF),A
site 020ED   ; OUT ($BF),A
site 020F1   ; OUT ($BF),A
site 02346   ; OUT ($BF),A
site 0234A   ; OUT ($BF),A
site 02358   ; OTIR
site 0235B   ; OUT ($BF),A
site 0235E   ; OUT ($BF),A
site 02364   ; OTIR
site 02366   ; OUTI
site 02368   ; OUTI
site 02392   ; OUT (C),L
site 02394   ; OUT (C),H
site 0239B   ; OUTI
site 0239D   ; OUTI
site 02600   ; OUT (C),E
site 02604   ; OUT (C),D
site 026BD   ; OUT (C),D
site 026C3   ; OUT (C),E
site 026C9   ; OUT (C),H
site 026CF   ; OUT (C),L
site 04611   ; OUT (C),E
site 04614   ; OUT (C),A
site 04619   ; INI
site 04D27   ; OUT ($BF),A
site 04D2B   ; OUT ($BF),A
site 060F2   ; OUT ($BF),A
site 060F6   ; OUT ($BF),A
site 060FC   ; OUT ($BE),A
site 06108   ; OUT (C),E
site 0610C   ; OUT (C),D
otir 0610F   ; OUTI
site 06145   ; OUT (C),E
site 06147   ; OUT (C),D
otir 0614C   ; OUTI
site 06158   ; OUT (C),L
site 0615A   ; OUT (C),H
otir 06160   ; OUTI
site 061E7   ; OUT ($BF),A
site 061ED   ; OUT ($BF),A
site 061F5   ; OUTI
site 0622F   ; OUTI
site 06234   ; OUT (C),A
site 06253   ; IN A,($7E)
site 0669A   ; OUT (C),E
site 0669C   ; OUT (C),D
site 066A2   ; OUT (C),E
site 066A4   ; OUT (C),D
site 066A8   ; IN A,($7E)
site 06DFE   ; OUT (C),E
site 06E02   ; OUT (C),D
site 06E0D   ; OUT (C),A
site 06E80   ; OUT (C),E
site 06E84   ; OUT (C),D
site 06E95   ; OUT (C),A
site 06E9C   ; OUT (C),E
site 06EA0   ; OUT (C),D
site 06EA7   ; OUT (C),A
site 06EB0   ; OUT (C),A
site 06EB7   ; OUT (C),E
site 06EBB   ; OUT (C),D
site 06EC2   ; OUT (C),A
site 06ECB   ; OUT (C),A
site 06FA3   ; IN A,($DC)
site 06FB7   ; IN A,($DC)
site 0747D   ; OUT (C),E
site 07481   ; OUT (C),D
site 07484   ; OUT (C),L
site 07488   ; OUT (C),H
site 07A8D   ; OUT (C),L
site 07A91   ; OUT (C),H
site 07A95   ; OUT (C),L
site 07A99   ; OUT (C),H
site 07AAE   ; OUT (C),E
site 07AB2   ; OUT (C),D
site 07ABE   ; OUT (C),L
site 07AC4   ; OUT (C),H
site 07AC9   ; OUT (C),L
site 07ACF   ; OUT (C),H
site 2EA85   ; OTIR
site 2EAB4   ; OUT ($7F),A
site 2EAB9   ; OUT ($7F),A
site 2EABE   ; OUT ($7F),A
site 2EAC9   ; OUT ($7F),A
site 2EACE   ; OUT ($7F),A
site 2EAD3   ; OUT ($7F),A
site 2EADE   ; OUT ($7F),A
site 2EAE3   ; OUT ($7F),A
site 2EAE8   ; OUT ($7F),A
site 2EAF3   ; OUT ($7F),A
site 2F025   ; OUT ($7F),A
site 2F239   ; OUT ($7F),A
site 2F262   ; OUT ($7F),A
site 2F298   ; OUT ($7F),A
site 2F2CF   ; OUT ($7F),A
site 2F2DA   ; OUT ($7F),A
site 2F2E8   ; OUT ($7F),A
site 2F2F2   ; OUT ($7F),A
site 2F31E   ; OUT ($7F),A
site 2F32B   ; OUT ($7F),A
site 2F33D   ; OUT ($7F),A
site 2F34A   ; OUT ($7F),A
site 2F360   ; OUT ($7F),A
site 2F396   ; OUT ($7F),A
site 2F3CD   ; OUT ($7F),A
site 2F3D8   ; OUT ($7F),A
site 2F3E6   ; OUT ($7F),A
site 2F3F0   ; OUT ($7F),A
site 2F41C   ; OUT ($7F),A
site 2F429   ; OUT ($7F),A
site 2F43B   ; OUT ($7F),A
site 2F448   ; OUT ($7F),A
site 2F45E   ; OUT ($7F),A
site 2F494   ; OUT ($7F),A
site 2F4CB   ; OUT ($7F),A
site 2F4D6   ; OUT ($7F),A
site 2F4E4   ; OUT ($7F),A
site 2F4EE   ; OUT ($7F),A
site 2F51A   ; OUT ($7F),A
site 2F527   ; OUT ($7F),A
site 2F539   ; OUT ($7F),A
site 2F546   ; OUT ($7F),A
site 2F55C   ; OUT ($7F),A
site 2F592   ; OUT ($7F),A
mapst 0049D   ; LD ($FFFF),A
mapst 004A8   ; LD ($FFFF),A
mapst 00787   ; LD ($FFFF),A
mapst 007D4   ; LD ($FFFF),A
mapst 0080E   ; LD ($FFFF),A
mapst 009CC   ; LD ($FFFF),A
mapst 00E1B   ; LD ($FFFF),A
mapst 0115C   ; LD ($FFFF),A
mapst 0116D   ; LD ($FFFF),A
mapst 01676   ; LD ($FFFF),A
mapst 017AC   ; LD ($FFFF),A
mapst 018DA   ; LD ($FFFF),A
mapst 0196A   ; LD ($FFFF),A
mapst 019C7   ; LD ($FFFF),A
mapst 01DE4   ; LD ($FFFF),A
mapst 01FB2   ; LD ($FFFF),A
mapst 020A0   ; LD ($FFFF),A
mapst 02232   ; LD ($FFFF),A
mapst 02245   ; LD ($FFFF),A
mapst 023B3   ; LD ($FFFF),A
mapst 03609   ; LD ($FFFF),A
mapst 03613   ; LD ($FFFF),A
mapst 0364D   ; LD ($FFFF),A
mapst 03657   ; LD ($FFFF),A
mapst 03664   ; LD ($FFFF),A
mapst 0366E   ; LD ($FFFF),A
mapst 0367B   ; LD ($FFFF),A
mapst 03685   ; LD ($FFFF),A
mapst 03692   ; LD ($FFFF),A
mapst 0369C   ; LD ($FFFF),A
mapst 036A9   ; LD ($FFFF),A
mapst 036B3   ; LD ($FFFF),A
mapst 0391E   ; LD ($FFFF),A
mapst 039DA   ; LD ($FFFF),A
mapst 03A51   ; LD ($FFFF),A
mapst 03BA0   ; LD ($FFFF),A
mapst 03BC8   ; LD ($FFFF),A
mapst 03CC6   ; LD ($FFFF),A
mapst 03EF5   ; LD ($FFFF),A
mapst 04335   ; LD ($FFFF),A
mapst 048C4   ; LD ($FFFF),A
mapst 048DF   ; LD ($FFFF),A
mapst 04DD4   ; LD ($FFFF),A
mapst 04DEF   ; LD ($FFFF),A
mapst 04E09   ; LD ($FFFF),A
mapst 04F23   ; LD ($FFFF),A
mapst 04F42   ; LD ($FFFF),A
mapst 04F49   ; LD ($FFFF),A
mapst 06014   ; LD ($FFFF),A
mapst 0617B   ; LD ($FFFF),A
mapst 0618C   ; LD ($FFFF),A
mapst 061A6   ; LD ($FFFF),A
mapst 061B7   ; LD ($FFFF),A
mapst 061BF   ; LD ($FFFF),A
mapst 061CE   ; LD ($FFFF),A
mapst 061D6   ; LD ($FFFF),A
mapst 06282   ; LD ($FFFF),A
mapst 0628A   ; LD ($FFFF),A
mapst 06296   ; LD ($FFFF),A
mapst 0629E   ; LD ($FFFF),A
mapst 062BE   ; LD ($FFFF),A
mapst 062C6   ; LD ($FFFF),A
mapst 066C6   ; LD ($FFFF),A
mapst 06764   ; LD ($FFFF),A
mapst 06942   ; LD ($FFFF),A
mapst 0694A   ; LD ($FFFF),A
mapst 06E52   ; LD ($FFFF),A
mapst 06E59   ; LD ($FFFF),A
mapst 072BA   ; LD ($FFFF),A
mapst 072C2   ; LD ($FFFF),A
mapst 073F8   ; LD ($FFFF),A
mapst 07402   ; LD ($FFFF),A
mapst 074CB   ; LD ($FFFF),A
mapst 074D3   ; LD ($FFFF),A
mapst 077D2   ; LD ($FFFF),A
mapst 077D9   ; LD ($FFFF),A
mapst 077E4   ; LD ($FFFF),A
mapst 077EC   ; LD ($FFFF),A
mapst 0785D   ; LD ($FFFF),A
mapst 07B71   ; LD ($FFFF),A
# CHECK indirect_unresolved at 02362 ($2362 bank 0): C8  RET Z 
# CHECK indirect_unresolved at 0236A ($236A bank 0): C9  RET 
# CHECK indirect_unresolved at 04709 ($4709 bank 1): C9  RET 
# CHECK indirect_unresolved at 04D73 ($4D73 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 052F8 ($52F8 bank 1): C0  RET NZ 
# CHECK bank_unresolved at 071C3 ($71C3 bank 1): CD 73 86  CALL $8673 $8673
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00F72   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 0149B   # LD ($FFFF),A; after LD A,($DB0D)
mapst 0251C   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 025E0   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 0287B   # LD ($FFFF),A; after LD A,$0F; 32 bytes of valid code before it
mapst 03620   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 0362A   # LD ($FFFF),A; after LD A,($DCC2); 32 bytes of valid code before it
mapst 03636   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 03640   # LD ($FFFF),A; after LD A,($DCC2); 32 bytes of valid code before it
mapst 0600B   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 062AA   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 062B2   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 074EC   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
# CHECK low: site 0058E  IN A,($F2)  (fm_detect; no evidence)
# CHECK medium: site 006BF  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 006C3  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK high: site 006C9  OUTI  (port in C; branch target from $006CB; 32 bytes of valid code before it)
# CHECK medium: site 006D8  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 006DC  OUT ($BF),A  (vdp_control; after LD A,$87; 32 bytes of valid code before it)
# CHECK medium: site 006E1  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 006E5  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK high: site 006E8  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK medium: site 00818  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 00820  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 00826  OUT ($BE),A  (vdp_data; branch target from $00832; 32 bytes of valid code before it)
# CHECK medium: site 0082D  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 0085D  OUT ($BF),A  (vdp_control; branch target from $00879 $0087C; 32 bytes of valid code before it)
# CHECK medium: site 00862  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 00865  OUT ($BE),A  (vdp_data; branch target from $0086E; 32 bytes of valid code before it)
# CHECK medium: site 0086A  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 00CA6  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00CA8  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00CAB  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00CF7  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00CF9  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK high: site 00CFC  INI  (port in C; branch target from $00D01 $00CFE; 32 bytes of valid code before it)
# CHECK medium: site 00F4C  OUT (C),B  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00F51  OUT (C),B  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00F59  OUT (C),B  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 00F5E  OUT (C),B  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 01A82  OUT ($BF),A  (vdp_control; 30 bytes of valid code before it)
# CHECK medium: site 01A89  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 01A90  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 01D02  OUT (C),L  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 01D08  OUT (C),H  (port in C; 32 bytes of valid code before it)
# CHECK high: site 01D0E  IN A,($BE)  (vdp_data; branch target from $166D8; 32 bytes of valid code before it)
# CHECK medium: site 01D16  OUT (C),L  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 01D1E  OUT (C),H  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 01D24  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 0202D  OUT ($BF),A  (vdp_control; branch target from $02069 $0205D; 32 bytes of valid code before it)
# CHECK high: site 02031  OUT ($BF),A  (vdp_control; after LD A,$78; 32 bytes of valid code before it)
# CHECK high: site 0203B  OUT (C),L  (port in C; branch target from $02047; 32 bytes of valid code before it)
# CHECK medium: site 02041  OUT (C),H  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 02066  IN A,($DC)  (joypad_a; 32 bytes of valid code before it)
# CHECK high: site 02071  OUT (C),B  (port in C; branch target from $1C5EB; 32 bytes of valid code before it)
# CHECK medium: site 02079  OUT (C),B  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 02080  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 02088  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 0208C  OUT (C),B  (port in C; 32 bytes of valid code before it)
# CHECK high: site 0236C  OUTI  (port in C; branch target from $0236E; 32 bytes of valid code before it)
# CHECK medium: site 02575  OUT (C),L  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 0257B  OUT (C),H  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 02583  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 02589  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 025E5  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 025E9  OUT ($BF),A  (vdp_control; after LD A,$59; 32 bytes of valid code before it)
# CHECK high: site 028A7  OUT ($BF),A  (vdp_control; after LD A,$E0; 32 bytes of valid code before it)
# CHECK high: site 028AB  OUT ($BF),A  (vdp_control; after LD A,$BF; 32 bytes of valid code before it)
# CHECK high: site 028AF  OUT ($BF),A  (vdp_control; after LD A,$81; 32 bytes of valid code before it)
# CHECK high: site 028B3  OUT ($BF),A  (vdp_control; after LD A,$BF; 32 bytes of valid code before it)
# CHECK low: site 02AE7  IN A,($DC)  (joypad_a; no evidence)
# CHECK medium: site 03348  IN A,($DC)  (joypad_a; 32 bytes of valid code before it)
# CHECK low: site 04AE1  IN A,($DC)  (joypad_a; no evidence)
# CHECK medium: site 04C5A  IN A,($DC)  (joypad_a; 32 bytes of valid code before it)
# CHECK medium: site 0620D  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 06211  OUT ($BF),A  (vdp_control; after LD A,$87; 32 bytes of valid code before it)
# CHECK medium: site 06218  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 0621C  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK high: site 0621F  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK high: site 07FD5  IN A,($DC)  (joypad_a; branch target from $07FDB; 32 bytes of valid code before it)
# CHECK low: site 08686  OUT (C),E  (port in C; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 0868A  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK high: site 0868D  OUT (C),L  (port in C; branch target from $08697; 32 bytes of valid code before it)
# CHECK medium: site 08691  OUT (C),H  (port in C; 31 bytes of valid code before it)
# CHECK low: site 0E9E8  IN A,($7F)  (h_counter; 10 RST or NOP opcodes around it (looks like data); 18 bytes of valid code before it)
# CHECK low: site 14D1C  IN A,($7F)  (h_counter; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 16AA4  IN A,($F2)  (fm_detect; 32 bytes of valid code before it)
# CHECK low: site 16AD8  IN A,($7F)  (h_counter; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 16CD8  IN A,($7F)  (h_counter; no evidence)
# CHECK medium: site 16EA4  IN A,($F2)  (fm_detect; 32 bytes of valid code before it)
# CHECK low: site 16ED8  IN A,($7F)  (h_counter; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 195E7  IN A,($3F)  (unmapped_read; no evidence)
# CHECK low: site 1A14D  OUT ($3F),A  (io_control; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1FF39  IN A,($BD)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1FF49  IN A,($BD)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2CC3C  IN A,($7E)  (v_counter; no evidence)
# CHECK medium: site 2D499  INIR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 2DC7C  IN A,($7E)  (v_counter; no evidence)
# CHECK medium: site 32C74  OUT (C),H  (port in C; 12 bytes of valid code before it)
# CHECK low: site 34270  IN A,($BE)  (vdp_data; no evidence)
# CHECK low: site 356F0  IN A,($BE)  (vdp_data; no evidence)
# CHECK low: site 372AF  IN A,($BE)  (vdp_data; no evidence)
# CHECK low: site 37367  OUT (C),B  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 3AD35  IN A,($7F)  (h_counter; 10 bytes of valid code before it)
# CHECK low: site 3B10A  IN A,($7F)  (h_counter; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3B14A  IN A,($7F)  (h_counter; no evidence)
# CHECK medium: site 3C389  OUT ($BD),A  (vdp_control; 15 bytes of valid code before it)
# CHECK low: site 3C45D  OUT ($BE),A  (vdp_data; no valid code after it)
