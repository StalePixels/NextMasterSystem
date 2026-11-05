# Speedball 2 (Europe), CRC32 0C7366A0, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - The VDP control word pairs at $2A4A, $2A5C and the palette set-up at $2B9D each become
#   one far call (page 0) that sets the runtime's address, code and latch at once. The
#   game writes these pairs with interrupts on while line interrupts come every 8 lines,
#   and its interrupt entry reads the status port, which clears the latch: an interrupt
#   between the two writes turned the second byte into a first one. After a fade the code
#   was still CRAM, so the text screen's first row clear wrote 64 zeros into CRAM and the
#   screen went black; at $2B9D the 32 palette bytes went into VRAM at $xxC0.
# - The bank-call stubs at $01B4, $01C5 and $01E7 (DI; LD HL,$FFFF; LD B,(HL); PUSH BC;
#   LD (HL),$0F) get maphl lines; the scanner reached them only part way through, from the
#   reference logs. Without them the demo match jumped into data in bank 7.
# - $2A6A counts loop passes over one frame to tell 50 Hz from 60 Hz and keeps the result in
#   $D241 (not 0: the music skips every sixth frame). The count depends on the CPU speed, so
#   the test gives the 50 Hz value, which matches hz 50.
name Speedball 2
cart 0C7366A0
hz 50		; No-Intro region Europe
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0003A   ; IN A,($BF)
site 00086   ; IN A,($DD)
site 000ED   ; OUT (C),E
site 000EF   ; OUT (C),D
site 000F4   ; OUT (C),A
site 000F9   ; OUT ($BF),A
site 000FE   ; OUT (C),B
site 00101   ; OUT (C),D
site 00107   ; OUT (C),A
site 00109   ; OUT (C),B
site 0010F   ; OUT (C),A
site 00118   ; OUT (C),A
site 00150   ; OUT ($BF),A
site 00154   ; OUT ($BF),A
site 00240   ; OTIR
site 0087E   ; IN A,($7E)
site 0092C   ; IN A,($7E)
site 01552   ; OUT (C),E
site 01556   ; OUT (C),D
site 0157A   ; OUT ($BE),A
site 01581   ; OUT ($BE),A
site 02789   ; OUT (C),E
site 0278D   ; OUT (C),D
site 027B1   ; OUT (C),A
site 027BE   ; OUT (C),A
site 027CB   ; OUT (C),A
site 027D6   ; OUT (C),A
site 02845   ; OUT (C),E
site 02849   ; OUT (C),D
site 02858   ; OUT ($BE),A
site 0285F   ; OUT ($BE),A
site 028B0   ; OUT ($BF),A
site 028B5   ; OUT ($BF),A
site 028CC   ; OUT ($BE),A
site 028D3   ; OUT ($BE),A
otir 02A53   ; OUTI
otir 02A65   ; OUTI
site 02A72   ; IN B,(C)
site 02A77   ; IN B,(C)
site 02A8B   ; OUT (C),B
site 02A93   ; OUT (C),A
site 02A9A   ; OUT ($BE),A
site 02AA4   ; OUT ($BF),A
site 02AAC   ; OUT ($BF),A
site 02AB1   ; OUT ($BF),A
site 02AB9   ; OUT ($BF),A
site 02AC2   ; OUT ($BF),A
site 02ACA   ; OUT ($BF),A
site 02AE6   ; OUTI
site 02AED   ; OUT (C),A
site 02AFE   ; OUT ($BF),A
site 02B02   ; OUT ($BF),A
site 02B08   ; OUT ($BE),A
site 02B11   ; OUT ($BF),A
site 02B15   ; OUT ($BF),A
site 02B1B   ; OUT ($BE),A
site 02B23   ; IN A,($7E)
site 02B95   ; IN A,($7E)
site 02BB1   ; OUTI
site 02BB9   ; OUTI
site 02CC6   ; OUT ($BF),A
site 02CCA   ; OUT ($BF),A
site 02CCE   ; OUT ($BE),A
site 02CD0   ; OUT ($BE),A
site 02CD2   ; OUT ($BE),A
site 02CD4   ; OUT ($BE),A
site 02CD6   ; OUT ($BE),A
site 02CD8   ; OUT ($BE),A
site 02CDA   ; OUT ($BE),A
site 02CDC   ; OUT ($BE),A
site 02CDE   ; OUT ($BE),A
site 02CE0   ; OUT ($BE),A
site 02CE2   ; OUT ($BE),A
site 02CE4   ; OUT ($BE),A
site 02CE6   ; OUT ($BE),A
site 02CE8   ; OUT ($BE),A
site 02CEA   ; OUT ($BE),A
site 02CEC   ; OUT ($BE),A
site 02CEE   ; OUT ($BE),A
site 02CF0   ; OUT ($BE),A
site 02CF2   ; OUT ($BE),A
site 02CF4   ; OUT ($BE),A
site 02CF6   ; OUT ($BE),A
site 02CF8   ; OUT ($BE),A
site 02CFA   ; OUT ($BE),A
site 02CFC   ; OUT ($BE),A
site 02CFE   ; OUT ($BE),A
site 02D00   ; OUT ($BE),A
site 02D02   ; OUT ($BE),A
site 02D04   ; OUT ($BE),A
site 02D06   ; OUT ($BE),A
site 02D08   ; OUT ($BE),A
site 02D0A   ; OUT ($BE),A
site 02D0C   ; OUT ($BE),A
site 02D0E   ; OUT ($BE),A
site 02D10   ; OUT ($BE),A
site 02D12   ; OUT ($BE),A
site 02D14   ; OUT ($BE),A
site 02D16   ; OUT ($BE),A
site 02D18   ; OUT ($BE),A
site 02D1A   ; OUT ($BE),A
site 02D1C   ; OUT ($BE),A
site 02D1E   ; OUT ($BE),A
site 02D20   ; OUT ($BE),A
site 02D22   ; OUT ($BE),A
site 02D24   ; OUT ($BE),A
site 02D26   ; OUT ($BE),A
site 02D28   ; OUT ($BE),A
site 02D2A   ; OUT ($BE),A
site 02D2C   ; OUT ($BE),A
site 02D2E   ; OUT ($BE),A
site 02D30   ; OUT ($BE),A
site 02D32   ; OUT ($BE),A
site 02D34   ; OUT ($BE),A
site 02D36   ; OUT ($BE),A
site 02D38   ; OUT ($BE),A
site 02D3A   ; OUT ($BE),A
site 02D3C   ; OUT ($BE),A
site 02D3E   ; OUT ($BE),A
site 02D40   ; OUT ($BE),A
site 02D42   ; OUT ($BE),A
site 02D44   ; OUT ($BE),A
site 02D46   ; OUT ($BE),A
site 02D48   ; OUT ($BE),A
site 02D4A   ; OUT ($BE),A
site 02D4C   ; OUT ($BE),A
site 02E04   ; OUT ($BF),A
site 02E08   ; OUT ($BF),A
site 02E0C   ; OUTI
site 02E11   ; OUTI
site 02E16   ; OUTI
site 02E1B   ; OUTI
site 02E20   ; OUTI
site 02E25   ; OUTI
site 02E2A   ; OUTI
site 02E2F   ; OUTI
site 02E35   ; OUT ($BF),A
site 02E39   ; OUT ($BF),A
site 02E3D   ; OUTI
site 02E42   ; OUTI
site 02E47   ; OUTI
site 02E4C   ; OUTI
site 02E51   ; OUTI
site 02E56   ; OUTI
site 02E5B   ; OUTI
site 02E60   ; OUTI
site 02E65   ; OUTI
site 02E6A   ; OUTI
site 02E6F   ; OUTI
site 02E74   ; OUTI
site 02E79   ; OUTI
site 02E7E   ; OUTI
site 02E83   ; OUTI
site 02E88   ; OUTI
site 02EB0   ; OUT ($BF),A
site 02EB4   ; OUT ($BF),A
site 02EBA   ; OUT ($BF),A
site 02EBE   ; OUT ($BF),A
site 02F6B   ; OUT (C),L
site 02F6D   ; OUT (C),H
site 02F74   ; OUTI
site 02F76   ; OUTI
site 02F86   ; OUT (C),L
site 02F88   ; OUT (C),H
site 02F9C   ; OTIR
site 02FA4   ; OUT ($BF),A
site 02FA7   ; OUT ($BF),A
site 02FA9   ; OTIR
site 02FAE   ; OTIR
site 02FB3   ; OUT (C),L
site 02FB5   ; OUT (C),H
otir 02FC9   ; OUTI
site 02FD3   ; OUT ($BF),A
site 02FD6   ; OUT ($BF),A
otir 02FD8   ; OUTI
otir 02FDF   ; OUTI
site 03006   ; OUT (C),E
site 03008   ; OUT (C),D
otir 0300B   ; OUTI
site 03132   ; OUT (C),E
site 03134   ; OUT (C),D
site 03137   ; OTIR
site 03141   ; OUT (C),A
site 03143   ; OUT (C),D
site 03146   ; OTIR
site 0316B   ; OUT (C),E
site 0316D   ; OUT (C),D
site 03170   ; OTIR
site 03832   ; IN A,($7E)
site 038F1   ; IN A,($DC)
site 038FF   ; IN A,($DD)
site 039F7   ; OUT (C),L
site 039FB   ; OUT (C),H
site 04A60   ; OUT (C),E
site 04A62   ; OUT (C),D
otir 04A65   ; OUTI
site 07E9C   ; OUT (C),D
site 07EA2   ; OUT (C),E
site 07EA8   ; OUT (C),H
site 07EAE   ; OUT (C),L
site 3C047   ; OTIR
site 3C13E   ; OUTI
site 3C140   ; OUTI
site 3C142   ; OUTI
site 3C14D   ; OUTI
site 3C14F   ; OUTI
site 3C151   ; OUTI
site 3C15C   ; OUTI
site 3C15E   ; OUTI
site 3C160   ; OUTI
site 3C16B   ; OUTI
site 3C72E   ; OUT ($7F),A
site 3C88F   ; OUT ($7F),A
site 3C898   ; OUT ($7F),A
site 3C8E5   ; OUT ($7F),A
site 3C8EE   ; OUT ($7F),A
site 3C93B   ; OUT ($7F),A
site 3C944   ; OUT ($7F),A
site 3C98D   ; OUT ($7F),A
site 3C9B5   ; OUT ($7F),A
site 3C9E7   ; OUT ($7F),A
site 3CA22   ; OUT ($7F),A
site 3CA2A   ; OUT ($7F),A
site 3CA39   ; OUT ($7F),A
site 3CA42   ; OUT ($7F),A
site 3CA6E   ; OUT ($7F),A
site 3CA77   ; OUT ($7F),A
site 3CA99   ; OUT ($7F),A
site 3CACB   ; OUT ($7F),A
site 3CB06   ; OUT ($7F),A
site 3CB0E   ; OUT ($7F),A
site 3CB1D   ; OUT ($7F),A
site 3CB26   ; OUT ($7F),A
site 3CB52   ; OUT ($7F),A
site 3CB5B   ; OUT ($7F),A
site 3CB7D   ; OUT ($7F),A
site 3CBAF   ; OUT ($7F),A
site 3CBEA   ; OUT ($7F),A
site 3CBF2   ; OUT ($7F),A
site 3CC01   ; OUT ($7F),A
site 3CC0A   ; OUT ($7F),A
site 3CC36   ; OUT ($7F),A
site 3CC3F   ; OUT ($7F),A
site 3CC61   ; OUT ($7F),A
site 3CC93   ; OUT ($7F),A
site 3CCBF   ; OUT ($7F),A
asm 02A4A 9   ; LD C,$BF; OUT (C),E; SET 6,D; OUT (C),D; DEC C: the VDP address, two control writes
    rst $00
    db far_io, pg_ctl_w, ent_ctl_w
endasm
asm 02A5C 9   ; LD C,$BF; OUT (C),E; SET 6,D; OUT (C),D; DEC C: the VDP address, two control writes
    rst $00
    db far_io, pg_ctl_w, ent_ctl_w
endasm
asm 02A7C 8   ; XOR A; LD DE,$F7CC; ADD HL,DE; JR C,$2A84; DEC A: the 50/60 Hz answer of the speed test
    xor a         ; $D241 = 0, the 50 Hz value
endasm
asm 02B9D 17  ; LD ($DECD),A; NOP; XOR A; OUT ($BF),A; LD ($DECD),A; NOP; LD A,$C0; OUT ($BF),A; LD C,$BE
    rst $00
    db far_io, pg_pal_w, ent_pal_w
endasm
page 0 ctl_w pal_w
; ctl_w: what LD C,$BF; OUT (C),E; SET 6,D; OUT (C),D; DEC C does, in one step: the VDP
; address and code from E and D OR $40, with the control latch cleared. The game's
; interrupt handler reads the status port, which clears the latch; an interrupt between
; the game's two writes turned the second byte into a first one and left the code of the
; write before (CRAM, after a fade). Keeps A, B, HL; returns D OR $40 and C = $BE.
; Runtime internals used: vdp_latch, vdp_addr, vdp_code.
ctl_w:
    ld (sv_a),a
    xor a
    ld (vdp_latch),a
    ld a,e
    ld (vdp_addr),a
    set 6,d
    ld a,d
    and $3F
    ld (vdp_addr+1),a
    ld a,d
    rlca
    rlca
    and 3
    ld (vdp_code),a
    ld a,(sv_a)
    ld c,$BE
    ret
; pal_w: what $2B9D-$2BAD does, in one step: CRAM address 0 for the palette writes that
; follow, $DECD = 0, A = $C0, C = $BE. An interrupt between the game's two control writes
; sent the 32 palette bytes into VRAM at $xxC0 with the code of the write before.
; Runtime internals used: vdp_latch, vdp_addr, vdp_code.
pal_w:
    xor a
    ld ($DECD),a
    ld (vdp_latch),a
    ld (vdp_addr),a
    ld (vdp_addr+1),a
    ld a,3
    ld (vdp_code),a
    ld a,$C0
    ld c,$BE
    ret
sv_a:
    db 0
endpage
mapst 000BE   ; LD ($FFFF),A
mapst 000C6   ; LD ($FFFF),A
mapst 000CD   ; LD ($FFFF),A
mapst 000D4   ; LD ($FFFF),A
maphl 00197   # LD (HL),$0F, HL = $FFFF
mapst 0019F   ; LD ($FFFF),A
maphl 001A9   # LD (HL),$0F, HL = $FFFF
mapst 001AF   ; LD ($FFFF),A
maphl 001BA   # LD (HL),$0F, HL = $FFFF (the stub at $01B4)
mapst 001C0   ; LD ($FFFF),A
maphl 001CB   # LD (HL),$0F, HL = $FFFF (the stub at $01C5)
mapst 001D1   ; LD ($FFFF),A
maphl 001DC   # LD (HL),$0F, HL = $FFFF
mapst 001E2   ; LD ($FFFF),A
maphl 001ED   # LD (HL),$0F, HL = $FFFF (the stub at $01E7)
mapst 001F3   ; LD ($FFFF),A
maphl 001FD   # LD (HL),$0F, HL = $FFFF
mapst 00203   ; LD ($FFFF),A
maphl 0020C   # LD (HL),$0F, HL = $FFFF
mapst 00212   ; LD ($FFFF),A
# CHECK cartarea_store at 02A28 ($2A28 bank 0): 71  LD (HL),C $0210
# CHECK cartarea_store at 02A2A ($2A2A bank 0): 70  LD (HL),B $0211
# CHECK ram_exec at 0248B ($248B bank 0): CD DC DB  CALL $DBDC $DBDC
# CHECK ram_exec at 035A4 ($35A4 bank 0): CD DC DB  CALL $DBDC $DBDC
# CHECK ram_exec at 035BD ($35BD bank 0): CD DC DB  CALL $DBDC $DBDC
# CHECK indirect_unresolved at 0003F ($003F bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 02591 ($2591 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 0277E ($277E bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 05561 ($5561 bank 1): E9  JP (HL) 
# CHECK bank_unresolved at 0019B ($019B bank 0): CD 09 81  CALL $8109 $8109
# CHECK bank_unresolved at 001BC ($01BC bank 0): CD 49 88  CALL $8849 $8849
# CHECK bank_unresolved at 001CD ($01CD bank 0): CD 9F 88  CALL $889F $889F
# CHECK bank_unresolved at 001DE ($01DE bank 0): CD F5 88  CALL $88F5 $88F5
# CHECK bank_unresolved at 001EF ($01EF bank 0): CD 4B 89  CALL $894B $894B
# CHECK bank_unresolved at 046B4 ($46B4 bank 1): C3 C9 A8  JP $A8C9 $A8C9
# CHECK medium: site 0232C  IN A,($BE)  (vdp_data; branch target from $02318)
# CHECK low: site 0236C  IN A,($7E)  (v_counter; no evidence)
# CHECK high: site 02B2D  IN A,(C)  (port in C; branch target from $02B30; 32 bytes of valid code before it)
# CHECK low: site 0302E  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 03336  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 03352  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 0369B  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 0374E  OUT ($3E),A  (memory_control; no evidence)
# CHECK medium: site 03DC3  IN A,($DD)  (joypad_b_misc; branch target from $0D8CA $0DA66 $0DAA6 $0DD86)
# CHECK low: site 03F0C  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 041A3  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 042D7  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0496D  OUT (C),C  (port in C; no evidence)
# CHECK low: site 04FBF  IN A,($C1)  (joypad_b_misc; no evidence)
# CHECK low: site 05059  OUT ($DD),A  (no_effect; no valid code after it)
# CHECK low: site 05290  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 052A4  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0535F  IN A,($3E)  (unmapped_read; no evidence)
# CHECK medium: site 053C1  IN A,($3E)  (unmapped_read; branch target from $05355)
# CHECK low: site 053EF  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 05417  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0543E  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0546A  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 054CE  OUT (C),L  (port in C; no evidence)
# CHECK medium: site 055E9  IN A,($3E)  (unmapped_read; branch target from $05619)
# CHECK medium: site 05626  IN A,($7E)  (v_counter; 13 bytes of valid code before it)
# CHECK low: site 0571B  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 08E33  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 08F59  IN A,($DD)  (joypad_b_misc; no valid code after it)
# CHECK low: site 08F8C  IN A,($DD)  (joypad_b_misc; no valid code after it)
# CHECK low: site 09315  IN A,($DD)  (joypad_b_misc; no valid code after it)
# CHECK low: site 09971  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09F0A  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09FCD  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK medium: site 09FDE  IN A,($DD)  (joypad_b_misc; 9 bytes of valid code before it)
# CHECK low: site 0A52D  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 0A906  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 0A912  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 0B1E1  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 10030  IN B,(C)  (port in C; no evidence)
# CHECK low: site 10034  IN B,(C)  (port in C; no evidence)
# CHECK low: site 11B13  OUT ($7F),A  (psg; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 1226D  IN A,($3F)  (unmapped_read; 22 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1857F  OTDR  (port in C; no evidence)
# CHECK low: site 19EF5  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 1A40F  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 1A6AE  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 1A791  IN A,($7E)  (v_counter; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1AC63  IN A,($7E)  (v_counter; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1AE1B  IN A,($7E)  (v_counter; 14 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1B719  IN A,($7E)  (v_counter; no valid code after it)
# CHECK low: site 1B74E  IN A,($7E)  (v_counter; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 1B86E  IN A,($7E)  (v_counter; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1B963  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 1B9EA  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2226B  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 223D8  IN A,($F1)  (joypad_b_misc; 17 bytes of valid code before it)
# CHECK low: site 24B2A  IN A,($C0)  (joypad_a; 24 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 24F2A  IN A,($C0)  (joypad_a; 22 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2A7E7  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 2B0DB  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 2B2D3  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 2C09D  IN H,(C)  (port in C; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 2CCE6  IN A,($DC)  (joypad_a; 32 bytes of valid code before it)
# CHECK high: site 2D820  OUT ($3F),A  (io_control; branch target from $2D84D; 32 bytes of valid code before it)
# CHECK low: site 2DDCF  IN A,($BD)  (vdp_status; 19 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 2DE1D  IN H,(C)  (port in C; branch target from $2D8E9; 32 bytes of valid code before it)
# CHECK low: site 2E910  OTIR  (port in C; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 2F0B0  OTIR  (port in C; branch target from $2CEE0; 32 bytes of valid code before it)
# CHECK medium: site 30B1D  IN E,(C)  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 30BA0  OUT (C),L  (port in C; 32 bytes of valid code before it)
# CHECK low: site 3131B  OTDR  (port in C; no evidence)
# CHECK medium: site 34771  OTDR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 347E0  OUT ($F0),A  (fm_address; no evidence)
# CHECK medium: site 34BB8  IN E,(C)  (port in C; 28 bytes of valid code before it)
# CHECK low: site 34C92  OUT (C),E  (port in C; no evidence)
# CHECK medium: site 351D6  OTDR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 35399  OUTD  (port in C; 32 bytes of valid code before it)
# CHECK low: site 35647  OTDR  (port in C; no evidence)
# CHECK low: site 356DB  OUT ($BF),A  (vdp_control; no evidence)
# CHECK low: site 35854  OTDR  (port in C; no evidence)
# CHECK medium: site 36D79  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK low: site 39155  IN H,(C)  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 392D7  IN B,(C)  (port in C; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 3ADE4  IN C,(C)  (port in C; 11 bytes of valid code before it)
# CHECK medium: site 3AE3B  OUT ($F2),A  (fm_control; 32 bytes of valid code before it)
# CHECK low: site 3AF68  OUT (C),B  (port in C; no evidence)
