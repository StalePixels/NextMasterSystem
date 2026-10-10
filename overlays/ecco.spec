# Ecco the Dolphin, drafted by tools/mkspec.py from sitescan output.
name Ecco the Dolphin
cart 6687FAB9
hz 50		; No-Intro regions Europe, Brazil
# tilecache: whole tiles copied from cart ROM are not converted again (MAME,
# game frames 300-2300: framework cycles -1.7%, frames over 100% 4 -> 1)
tilecache
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00008   ; OUT ($BF),A
site 0000D   ; OUT ($BF),A
site 0008A   ; OUT ($7F),A
site 0008E   ; OUT ($7F),A
site 00092   ; OUT ($7F),A
site 00096   ; OUT ($7F),A
site 000A3   ; IN A,($BF)
site 000C4   ; IN A,($7E)
site 000D1   ; OUT ($BF),A
site 000D8   ; OUT ($BF),A
site 000E1   ; OUT ($BF),A
site 000E5   ; OUT ($BF),A
site 000EB   ; OUT ($BE),A
site 000F3   ; OUT ($BF),A
site 000F7   ; OUT ($BF),A
site 000FC   ; OUT ($BE),A
site 00126   ; IN A,($BF)
site 0012D   ; OUT ($7F),A
site 00131   ; OUT ($7F),A
site 00135   ; OUT ($7F),A
site 00139   ; OUT ($7F),A
site 00167   ; IN A,($BF)
site 00199   ; OUT ($BF),A
site 0019D   ; OUT ($BF),A
site 001B3   ; OUT ($BE),A
site 001BB   ; OUTI
site 001C7   ; OTIR
site 001D4   ; OTIR
site 001D9   ; OUT ($BF),A
site 001DD   ; OUT ($BF),A
site 001DF   ; OTIR
site 00220   ; OUT ($BF),A
site 00227   ; OUT ($BF),A
site 0022C   ; OTIR
site 0023A   ; OUT ($BF),A
site 0023E   ; OUT ($BF),A
site 00246   ; OTIR
site 00248   ; OTIR
site 0024A   ; OTIR
site 00259   ; OUT ($BF),A
site 0025D   ; OUT ($BF),A
site 00265   ; OTIR
site 00267   ; OTIR
site 00269   ; OTIR
site 00275   ; OUT ($BF),A
site 00279   ; OUT ($BF),A
site 00281   ; OTIR
site 00283   ; OTIR
site 00292   ; OUT ($BF),A
site 00299   ; OUT ($BF),A
site 0029E   ; OTIR
site 002A8   ; OUT ($BF),A
site 002B6   ; OUT ($BF),A
site 002BB   ; OTIR
site 002CA   ; OUT ($BF),A
site 002D1   ; OUT ($BF),A
site 002D6   ; OTIR
site 002E0   ; OUT ($BF),A
site 002EE   ; OUT ($BF),A
site 002F3   ; OTIR
site 00360   ; OUT ($BF),A
site 00367   ; OUT ($BF),A
site 00371   ; OTIR
site 0037D   ; OTIR
site 00407   ; OUT ($BF),A
site 0040B   ; OUT ($BF),A
site 00413   ; OTIR
site 00428   ; OUT ($BF),A
site 0042D   ; OUT ($BF),A
site 00434   ; OTIR
site 0043F   ; OTIR
site 00446   ; OUT ($BF),A
site 0044A   ; OUT ($BF),A
site 0048B   ; OUT ($BE),A
site 00591   ; OUT ($BF),A
site 00597   ; OUT ($BF),A
site 0059F   ; OUT ($BF),A
site 005A4   ; OUT ($BF),A
site 005AB   ; OTIR
site 005B4   ; OTIR
site 005C4   ; IN A,($DC)
site 005FB   ; OUT ($BF),A
site 00600   ; OUT ($BF),A
site 00619   ; OUT ($BE),A
site 00626   ; OUT ($BE),A
site 00633   ; OUT ($BE),A
site 00640   ; OUT ($BE),A
# not a site: 00D06 is the operand of LD A,($CBDB) at $0D05 (overlapping decode through a table)
site 01E16   ; IN A,($7E)
site 01E20   ; OUT ($7F),A
site 01E23   ; OUT ($7F),A
site 01E27   ; OUT ($7F),A
site 01E2A   ; OUT ($7F),A
site 01E2E   ; OUT ($7F),A
site 01E31   ; OUT ($7F),A
site 01E34   ; OUT ($7F),A
site 01E4D   ; OUTI
site 01E4F   ; OUTI
site 01E51   ; OUTI
site 01E66   ; OUT ($7F),A
site 01E6B   ; OUT ($7F),A
site 01E70   ; OUT ($7F),A
# not a site: 020D8 is in a data table at $20CD
# not a site: 020DC is in a data table at $20CD
site 0CF9E   ; OUT ($BF),A
site 0CFA3   ; OUT ($BF),A
site 0CFB9   ; OUT ($BE),A
site 0CFC1   ; OUT ($BE),A
site 0CFC9   ; OUT ($BE),A
site 0CFD0   ; OUT ($BE),A
site 584F1   ; OUT ($7F),A
site 58506   ; OUT ($7F),A
site 5850F   ; OUT ($7F),A
site 5851A   ; OUT ($7F),A
site 58545   ; OUT ($7F),A
site 58699   ; OUT ($7F),A
site 586D0   ; OUT ($7F),A
site 586D9   ; OUT ($7F),A
site 586F4   ; OUT ($7F),A
site 586F8   ; OUT ($7F),A
site 587AE   ; OUT ($7F),A
site 587C4   ; OUT ($7F),A
site 587DC   ; OUT ($7F),A
site 587E0   ; OUT ($7F),A
site 587EE   ; OUT ($7F),A
site 5882C   ; OUT ($7F),A
mapst 000B6   ; LD ($FFFC),A
mapst 000B9   ; LD ($FFFD),A
mapst 000BD   ; LD ($FFFE),A
mapst 000C1   ; LD ($FFFF),A
mapldk 0010E   # loads HL with $FFFE, then stores $16 through it
maphl 00116   # LD (HL),$01, HL = $FFFE
mapst 00356   ; LD ($FFFE),A
mapst 0035A   ; LD ($FFFF),A
mapsthl 00396   ; LD ($FFFE),HL
mapst 00420   ; LD ($FFFE),A
mapst 00424   ; LD ($FFFF),A
mapst 00685   ; LD ($FFFE),A
mapst 00689   ; LD ($FFFF),A
mapsthl 006D2   ; LD ($FFFE),HL
mapst 00814   ; LD ($FFFE),A
mapst 00818   ; LD ($FFFF),A
mapst 00844   ; LD ($FFFE),A
mapst 00848   ; LD ($FFFF),A
mapstbc 008B5   ; LD ($FFFE),BC
mapst 00959   ; LD ($FFFE),A
mapst 0095D   ; LD ($FFFF),A
mapstbc 0096E   ; LD ($FFFE),BC
mapstbc 009B4   ; LD ($FFFE),BC
mapstbc 009E0   ; LD ($FFFE),BC
mapstbc 00A2D   ; LD ($FFFE),BC
mapstde 00B31   ; LD ($FFFE),DE
mapsthl 00BB0   ; LD ($FFFE),HL
mapst 00CE4   ; LD ($FFFE),A
mapst 00CE8   ; LD ($FFFF),A
mapst 00DA8   ; LD ($FFFE),A
mapst 00DAC   ; LD ($FFFF),A
mapst 00DDA   ; LD ($FFFE),A
mapst 00DDE   ; LD ($FFFF),A
mapst 00E46   ; LD ($FFFE),A
mapst 00E4A   ; LD ($FFFF),A
mapst 00E54   ; LD ($FFFE),A
mapst 00E58   ; LD ($FFFF),A
mapst 00E7A   ; LD ($FFFE),A
mapsthl 00E8D   ; LD ($FFFE),HL
mapsthl 00EB1   ; LD ($FFFE),HL
mapst 00FD3   ; LD ($FFFE),A
mapst 00FD7   ; LD ($FFFF),A
mapst 0101F   ; LD ($FFFE),A
mapst 01023   ; LD ($FFFF),A
mapsthl 0102C   ; LD ($FFFE),HL
mapsthl 01038   ; LD ($FFFE),HL
mapst 0125C   ; LD ($FFFE),A
mapst 01281   ; LD ($FFFE),A
mapst 012DB   ; LD ($FFFE),A
mapst 012DF   ; LD ($FFFF),A
mapsthl 012F9   ; LD ($FFFE),HL
mapst 012FF   ; LD ($FFFE),A
mapst 01303   ; LD ($FFFF),A
mapsthl 01316   ; LD ($FFFE),HL
mapstbc 0140F   ; LD ($FFFE),BC
mapstde 01418   ; LD ($FFFE),DE
mapstde 01425   ; LD ($FFFE),DE
mapstde 01432   ; LD ($FFFE),DE
mapst 01DF4   ; LD ($FFFE),A
mapst 01DF8   ; LD ($FFFF),A
mapsthl 01E11   ; LD ($FFFE),HL
# CHECK cartarea_store at 079BD ($79BD bank 1): LD (BC),A $7A94
# CHECK cartarea_store at 0A25C ($A25C bank 2): LD (DE),A $0100,$0101,$0102,$0103...
# CHECK cartarea_store at 12AF3 ($AAF3 bank 4): LD (DE),A $0200,$0201,$0202,$0203...
# CHECK ram_exec at 00508 ($0508 bank 0): JP Z,$E67D $E67D
# CHECK ram_exec at 00C04 ($0C04 bank 0): CALL C,$FE2A $FE2A
# CHECK ram_exec at 0DBF9 ($5BF9 bank 3): CALL M,$C0CF $C0CF
# CHECK ram_exec at 0DBFE ($5BFE bank 3): JP $FC03 $FC03
# CHECK ram_exec at 11186 ($9186 bank 4): JP $D191 $D191
# CHECK indirect_unresolved at 000AC ($00AC bank 0): RETN 
# CHECK indirect_unresolved at 0104D ($104D bank 0): RET 
# CHECK indirect_unresolved at 01312 ($1312 bank 0): JP (HL) 
# CHECK bank_unresolved at 00331 ($0331 bank 0): JP Z,$A0ED $A0ED
# CHECK bank_unresolved at 060BB ($60BB bank 1): CALL $8AAD $8AAD
# CHECK bank_unresolved at 0614D ($614D bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 061FF ($61FF bank 1): CALL $8E11 $8E11
# CHECK bank_unresolved at 06226 ($6226 bank 1): CALL $A027 $A027
# CHECK bank_unresolved at 06286 ($6286 bank 1): CALL $99B3 $99B3
# CHECK bank_unresolved at 06294 ($6294 bank 1): CALL $8AAD $8AAD
# CHECK bank_unresolved at 062DD ($62DD bank 1): CALL $8EEE $8EEE
# CHECK bank_unresolved at 062E2 ($62E2 bank 1): CALL $94FB $94FB
# CHECK bank_unresolved at 066FA ($66FA bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 0699B ($699B bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 069B0 ($69B0 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 069EB ($69EB bank 1): CALL $A1D8 $A1D8
# CHECK bank_unresolved at 06A17 ($6A17 bank 1): CALL $A1D8 $A1D8
# CHECK bank_unresolved at 06A6E ($6A6E bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 06A99 ($6A99 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 06ADF ($6ADF bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 06B0D ($6B0D bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 06B60 ($6B60 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 06BCD ($6BCD bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 06BD9 ($6BD9 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 06BE5 ($6BE5 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 06F33 ($6F33 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 070AD ($70AD bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 070CE ($70CE bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 070E7 ($70E7 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 07122 ($7122 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 0715B ($715B bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 07179 ($7179 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 07192 ($7192 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 071C8 ($71C8 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 0721F ($721F bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 07240 ($7240 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 07259 ($7259 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 07294 ($7294 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 072CD ($72CD bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 072EB ($72EB bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 07304 ($7304 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 0733A ($733A bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 07373 ($7373 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 073AD ($73AD bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 073EC ($73EC bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 07426 ($7426 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 0743A ($743A bank 1): CALL $86FD $86FD
# CHECK bank_unresolved at 074C0 ($74C0 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 07855 ($7855 bank 1): CALL $A278 $A278
# CHECK bank_unresolved at 07861 ($7861 bank 1): CALL $A268 $A268
# CHECK bank_unresolved at 0789C ($789C bank 1): CALL $836B $836B
# CHECK bank_unresolved at 078B4 ($78B4 bank 1): CALL $8038 $8038
# CHECK bank_unresolved at 079B5 ($79B5 bank 1): CALL $A1ED $A1ED
# CHECK bank_unresolved at 0CB3D ($4B3D bank 3): CALL $AB0F $AB0F
# CHECK bank_unresolved at 0CB62 ($4B62 bank 3): CALL $AA1F $AA1F
# CHECK bank_unresolved at 0CBB8 ($4BB8 bank 3): CALL $AA1F $AA1F
# CHECK bank_unresolved at 0CBCB ($4BCB bank 3): CALL $AA1F $AA1F
# CHECK bank_unresolved at 0CBEB ($4BEB bank 3): CALL $AA6F $AA6F
# CHECK bank_unresolved at 0CC08 ($4C08 bank 3): CALL $AA6F $AA6F
# CHECK bank_unresolved at 0CC6B ($4C6B bank 3): CALL $AB0F $AB0F
# CHECK bank_unresolved at 0CCAA ($4CAA bank 3): CALL $AA6F $AA6F
# CHECK bank_unresolved at 0CCD4 ($4CD4 bank 3): CALL $AA6F $AA6F
# CHECK bank_unresolved at 0CCEE ($4CEE bank 3): CALL $AA41 $AA41
# CHECK bank_unresolved at 0CCF6 ($4CF6 bank 3): CALL $AA1F $AA1F
# CHECK bank_unresolved at 0CD01 ($4D01 bank 3): CALL $AA3E $AA3E
# CHECK bank_unresolved at 0CD7F ($4D7F bank 3): CALL $AA6F $AA6F
# CHECK bank_unresolved at 0CDA5 ($4DA5 bank 3): CALL $AA6F $AA6F
# CHECK low: site 004B1  OUT ($BE),A  (vdp_data)
# CHECK low: site 004BB  OUT ($BE),A  (vdp_data)
# CHECK low: site 004E1  OUT ($BE),A  (vdp_data)
# CHECK low: site 004EB  OUT ($BE),A  (vdp_data)
# CHECK low: site 0131A  IN A,($7E)  (v_counter)
# CHECK low: site 0131E  IN A,($7F)  (h_counter)
# CHECK low: site 02550  IN E,(C)  (port in C)
# CHECK low: site 02554  IN E,(C)  (port in C)
# CHECK low: site 02558  IN E,(C)  (port in C)
# CHECK low: site 02560  IN E,(C)  (port in C)
# CHECK low: site 0D2D1  IN D,(C)  (port in C)
# CHECK low: site 0E8F1  IN D,(C)  (port in C)
# CHECK low: site 125CE  IN A,($BD)  (vdp_status)
# CHECK low: site 19026  OUT ($7F),A  (psg)
# CHECK low: site 1EA9E  OUT (C),L  (port in C)
# CHECK low: site 2A402  IN C,(C)  (port in C)
# CHECK low: site 324DF  OUT ($F0),A  (fm_address)
# CHECK low: site 3AC16  OUT ($BF),A  (vdp_control)
# CHECK low: site 3AF71  OUT ($C0),A  (no_effect)
# CHECK low: site 54DAA  IN A,($3F)  (unmapped_read)
# CHECK low: site 54DAE  IN A,($3F)  (unmapped_read)
# CHECK low: site 588A2  IN C,(C)  (port in C)
# CHECK low: site 588B4  OUT (C),C  (port in C)
# CHECK low: site 588BE  OUT (C),C  (port in C)
# CHECK low: site 622AD  OUT ($C0),A  (no_effect)
# CHECK low: site 62C24  OUT ($C0),A  (no_effect)
# CHECK low: site 62D3D  IN A,($C0)  (joypad_a)
# CHECK low: site 630FE  IN A,($C0)  (joypad_a)
# CHECK low: site 68161  IN A,($C0)  (joypad_a)
# CHECK low: site 69FAC  IN A,($F2)  (fm_detect)
# CHECK low: site 6ADEA  IN A,($C0)  (joypad_a)
# CHECK low: site 71267  IN B,(C)  (port in C)
# CHECK low: site 76821  IN A,($C0)  (joypad_a)
# Sound driver PSG writes, bank 30: a byte-for-byte copy of bank 22 (patched above as 58xxx).
site 784F1   ; OUT ($7F),A
site 78506   ; OUT ($7F),A
site 7850F   ; OUT ($7F),A
site 7851A   ; OUT ($7F),A
site 78545   ; OUT ($7F),A
site 78699   ; OUT ($7F),A
site 786D0   ; OUT ($7F),A
site 786D9   ; OUT ($7F),A
site 786F4   ; OUT ($7F),A
site 786F8   ; OUT ($7F),A
site 787AE   ; OUT ($7F),A
site 787C4   ; OUT ($7F),A
site 787DC   ; OUT ($7F),A
site 787E0   ; OUT ($7F),A
site 787EE   ; OUT ($7F),A
site 7882C   ; OUT ($7F),A
# CHECK low: site 788A2  IN C,(C)  (port in C)
# CHECK low: site 788B4  OUT (C),C  (port in C)
# CHECK low: site 788BE  OUT (C),C  (port in C)
# Mapper stores the draft missed, in bank 0, found by sitescan's byte scan:
# LD ($FFFE),A after LD A,n, the store to $FFFF that follows it (A one higher), and
# LD ($FFFE),HL after POP HL, which restores both banks.
# Byte scan hits left out: they decode as data (RST and NOP runs, no valid
# code after them, or no code leading to them).
mapst 00EBB   ; LD ($FFFE),A
mapst 00EBF   ; LD ($FFFF),A
mapsthl 00EE0   ; LD ($FFFE),HL
mapst 011DB   ; LD ($FFFE),A
mapst 01209   ; LD ($FFFE),A
# not patched (data): mapst 32461  LD ($FFFF),A  (13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# not patched (data): mapsthl 4511C  LD ($FFFD),HL  (21 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# not patched (data): mapsthl 45480  LD ($FFFD),HL  (32 bytes of valid code before it; no valid code after it)
# Name table column upload in the frame handler ($01E8-$020F), as native code in page 0.
# The game writes one column of 28 name table cells (2 bytes each) from its RAM copy at
# $C000 (64 bytes a row) to VRAM $3800 + E + 64 * row, E = ($CBE3) AND $3F, with two
# control writes and two OUTI per row: about 230,000 Next cycles through the traps,
# in the frames where the screen scrolls by a column.
asm 001E8 40         ; RES 4,(HL) and the column loop, up to the DJNZ at $020E
    rst $00
    db far_io, pg_ntcol, ent_ntcol
    jp $0210
endasm
page 0 ntcol
; ntcol: HL = $CA9A. Does what the game's code at $01E8-$020F does: RES 4,(HL),
; then the 28 cells of name table column E = ($CBE3) AND $3F, from $C000 + E
; + 64 * row to VRAM $3800 + E + 64 * row, in one call to the framework's
; jt_vwrite (28 runs of 2 bytes, 64 bytes apart in the source and in VRAM).
; Returns with the registers that code leaves: A = 1, B = 0, C = $3E,
; HL = $C000 + E + 28 * 64, DE = $7F00 + E.
ntcol:  res 4,(hl)
        ld a,($CBE3)
        and $3F
        ld e,a
        ld d,0
        ld hl,$C000
        add hl,de               ; the source: row 0 of the column
        ld d,$38                ; DE = VRAM $3800 + E
        push ix
        push iy
        ld ix,64                ; the source step
        ld iy,64                ; the VRAM step
        ld bc,$021C             ; 28 runs of 2 bytes
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop iy
        pop ix
        ld bc,28*64
        add hl,bc
        ld d,$7F                ; registers as the game's loop leaves them
        ld a,1
        ld bc,$003E
        ret
endpage
