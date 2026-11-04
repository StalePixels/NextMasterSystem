# Sonic The Hedgehog 2, drafted by tools/mkspec.py from sitescan output.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
name Sonic The Hedgehog 2
cart 5B3B922C
hz 50		; No-Intro regions Europe, Brazil
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
# HALTs. The game counts frames with EI; HALT (most in DJNZ loops: title, act card, act end,
# fades); the runtime's own interrupts end a native HALT, so each becomes the HALT code.
# The routines at $13D2, $179B, $259C and $2849 also wait with EI; HALT, but nothing in the
# cart calls them and no reference run reached them: left as they are.
eihalt 00090
eihalt 0048D
eihalt 006DA
eihalt 00733
eihalt 00752
eihalt 00770
eihalt 007D6
eihalt 00828
eihalt 0083A
eihalt 00857
eihalt 00860
eihalt 008BE
eihalt 008D6
eihalt 008DF
eihalt 0094F
eihalt 00960
eihalt 00990
eihalt 017AC
eihalt 01C19
eihalt 01C58
eihalt 01C63
eihalt 021DA
eihalt 021DD
eihalt 02449
eihalt 02461
eihalt 024D1
eihalt 0255E
eihalt 02597
eihalt 02640
eihalt 026E2
eihalt 02723
eihalt 0286B
# The bare HALT at $09E0 (then JP $0690) is left native: $0690 calls $0593 at once, which
# waits for the frame handler's count at $D135.
site 00018   ; IN A,($7E)
site 0003A   ; IN A,($BF)
site 0049B   ; IN A,($DD)
site 004E1   ; OUT ($BF),A
site 004E5   ; OUT ($BF),A
site 004EB   ; OUT ($BF),A
site 004EF   ; OUT ($BF),A
site 005B4   ; OUT ($BF),A
site 005B8   ; OUT ($BF),A
site 005CA   ; OUT ($BF),A
site 005CE   ; OUT ($BF),A
site 01246   ; OUT ($BF),A
site 0124C   ; OUT ($BF),A
site 012A6   ; IN A,($BF)
site 012A8   ; IN A,($BF)
site 012B4   ; IN A,($BF)
site 012EC   ; IN A,($BF)
site 012F9   ; OUT ($BF),A
site 012FD   ; OUT ($BF),A
site 0132A   ; OUT ($BF),A
site 0132F   ; OUT ($BF),A
site 01395   ; OUT ($BF),A
site 01399   ; OUT ($BF),A
site 013A3   ; OUT ($BF),A
site 013A7   ; OUT ($BF),A
site 013BF   ; OUT ($BE),A
site 013C7   ; OUT ($BE),A
site 01A70   ; IN A,($DD)
site 01A7A   ; IN A,($DC)
site 01DD8   ; OUT ($BE),A
site 01DDE   ; OUT ($BE),A
site 01DF5   ; OUT ($BE),A
site 01DFB   ; OUT ($BE),A
site 07878   ; OUT ($BE),A
site 078BE   ; OUT ($BE),A
site 081FD   ; OUT ($7F),A
site 08416   ; OTIR
site 0852E   ; OUT ($7F),A
site 08538   ; OUT ($7F),A
site 08555   ; OUT ($7F),A
site 08659   ; OUT ($7F),A
site 086E5   ; OUT ($7F),A
site 08787   ; OUT ($7F),A
site 08790   ; OUT ($7F),A
site 087A0   ; OUT ($7F),A
site 08806   ; OUT ($7F),A
site 08823   ; OUT ($7F),A
mapst 00008   ; LD ($FFFC),A
mapst 0000D   ; LD ($FFFD),A
mapst 00011   ; LD ($FFFE),A
mapst 00015   ; LD ($FFFF),A
mapst 00447   ; LD ($FFFC),A
mapst 0044C   ; LD ($FFFD),A
mapst 00450   ; LD ($FFFE),A
mapst 00454   ; LD ($FFFF),A
mapst 00536   ; LD ($FFFF),A
mapst 0054C   ; LD ($FFFF),A
mapst 00557   ; LD ($FFFF),A
mapst 0055F   ; LD ($FFFF),A
mapst 00576   ; LD ($FFFF),A
mapst 010E3   ; LD ($FFFF),A
mapst 010ED   ; LD ($FFFF),A
mapst 0129F   ; LD ($FFFF),A
mapst 01A8F   ; LD ($FFFF),A
mapst 07F42   ; LD ($FFFF),A
mapst 07FD8   ; LD ($FFFF),A
# CHECK cartarea_store at 088FF ($88FF bank 2): 02  LD (BC),A $080D
# CHECK cartarea_store at 08907 ($8907 bank 2): 12  LD (DE),A $080F
# CHECK ram_exec at 088DE ($88DE bank 2): F2 88 FE  JP P,$FE88 $FE88
# CHECK indirect_unresolved at 02FC5 ($2FC5 bank 0): CD 39 61  CALL $6139 $6139
# CHECK indirect_unresolved at 05F1E ($5F1E bank 1): CD 39 61  CALL $6139 $6139
# CHECK indirect_unresolved at 05F36 ($5F36 bank 1): CD 39 61  CALL $6139 $6139
# CHECK indirect_unresolved at 05F4A ($5F4A bank 1): CD 39 61  CALL $6139 $6139
# CHECK indirect_unresolved at 066C9 ($66C9 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 067B0 ($67B0 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 0700F ($700F bank 1): C9  RET 
# CHECK indirect_unresolved at 088F9 ($88F9 bank 2): F0  RET P 
# CHECK indirect_unresolved at 088FA ($88FA bank 2): D0  RET NC 
# CHECK indirect_unresolved at 780BD ($80BD bank 30): E9  JP (HL) 
# Bank 3 $8000: a 4-bit sample player on the PSG (three volume writes per nibble, timed with
# DJNZ). No path the scanner follows maps bank 3 and no reference run played it; patched as
# the code it is.
site 0C00D   ; OUT ($7F),A
site 0C011   ; OUT ($7F),A
site 0C015   ; OUT ($7F),A
site 0C019   ; OUT ($7F),A
site 0C01D   ; OUT ($7F),A
site 0C021   ; OUT ($7F),A
site 0C031   ; OUT ($7F),A
site 0C035   ; OUT ($7F),A
site 0C039   ; OUT ($7F),A
site 0C044   ; OUT ($7F),A
site 0C048   ; OUT ($7F),A
site 0C04C   ; OUT ($7F),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 06671   # LD ($FFFF),A; after LD ($D12B),A; 32 bytes of valid code before it
mapst 0701A   # LD ($FFFF),A; after LD ($D12B),A; 32 bytes of valid code before it
mapst 0706A   # LD ($FFFF),A; after LD ($D12B),A; 32 bytes of valid code before it
mapst 0748A   # LD ($FFFF),A; after LD ($D12B),A; 32 bytes of valid code before it
mapst 0752A   # LD ($FFFF),A; after LD ($D12B),A; 32 bytes of valid code before it
mapst 07537   # LD ($FFFF),A; after LD ($D12B),A; 32 bytes of valid code before it
mapst 075A3   # LD ($FFFF),A; after LD ($D12B),A; 32 bytes of valid code before it
# CHECK byte scan low: mapsthl 5008A  LD ($FFFC),HL  (no valid code after it)
# CHECK byte scan low: mapsthl 510B4  LD ($FFFC),HL  (no valid code after it)
# CHECK byte scan low: mapsthl 5EDF7  LD ($FFFE),HL  (8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK byte scan low: mapsthl 65809  LD ($FFFC),HL  (no valid code after it)
# CHECK byte scan low: mapsthl 6F162  LD ($FFFE),HL  (no valid code after it)
# CHECK high: site 0066C  OUT ($BF),A  (vdp_control; after LD A,$00; branch target from $0065A; 32 bytes of valid code before it)
# CHECK high: site 00670  OUT ($BF),A  (vdp_control; after LD A,$88; 32 bytes of valid code before it)
# CHECK high: site 01313  OUT ($BF),A  (vdp_control; branch target from $1EB4B $64317 $6431B $6431F; 32 bytes of valid code before it)
# CHECK low: site 01318  OUT ($BF),A  (vdp_control; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 01325  IN A,($BF)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 01334  OUT ($BF),A  (vdp_control; branch target from $01346 $55CBE; 32 bytes of valid code before it)
# CHECK medium: site 01339  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 01343  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK medium: site 01349  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 01354  OUT ($BE),A  (vdp_data; branch target from $0135D; 32 bytes of valid code before it)
# CHECK medium: site 01358  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 013B1  OUT ($BF),A  (vdp_control; branch target from $7F14D; 32 bytes of valid code before it)
# CHECK high: site 013B5  OUT ($BF),A  (vdp_control; after LD A,$81; branch target from $05F95; 32 bytes of valid code before it)
# CHECK high: site 013E0  OUT ($BE),A  (vdp_data; after LD A,(DE); 32 bytes of valid code before it)
# CHECK medium: site 013E8  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 03125  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 03144  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 03628  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 03755  OUT ($F1),A  (fm_data; no evidence)
# CHECK low: site 0378E  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 038A2  OUT ($DD),A  (no_effect; no evidence)
# CHECK medium: site 038C6  OUT ($C1),A  (no_effect; branch target from $20230)
# CHECK low: site 03A9F  OUT ($DD),A  (no_effect; no evidence)
# CHECK medium: site 03CBE  OUT ($DD),A  (no_effect; branch target from $1EDFD $68399 $683A5 $68549)
# CHECK low: site 0429B  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 04401  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 0479F  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 06121  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 0612B  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 06EB6  OUT ($DD),A  (no_effect; no evidence)
# CHECK medium: site 074DD  OUT ($7E),A  (psg; branch target from $73B79)
# CHECK low: site 07525  OUT ($F1),A  (fm_data; no evidence)
# CHECK low: site 0758A  OUT ($7E),A  (psg; no evidence)
# CHECK low: site 0759E  OUT ($F1),A  (fm_data; no evidence)
# CHECK low: site 075AF  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 075B4  OUT ($3E),A  (memory_control; no evidence)
# CHECK medium: site 075B9  OUT ($3E),A  (memory_control; branch target from $0F624)
# CHECK low: site 0C4FD  IN A,($BD)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 0C6B3  OTDR  (port in C; no evidence)
# CHECK medium: site 0CB00  OTDR  (port in C; 28 bytes of valid code before it)
# CHECK low: site 0D801  INDR  (port in C; no evidence)
# CHECK medium: site 0D89D  INDR  (port in C; 32 bytes of valid code before it)
# CHECK high: site 0E8ED  OTDR  (port in C; branch target from $0FD5D; 31 bytes of valid code before it)
# CHECK low: site 0F095  IND  (port in C; no evidence)
# CHECK low: site 0F931  OTDR  (port in C; no evidence)
# CHECK medium: site 0FADF  INDR  (port in C; 31 bytes of valid code before it)
# CHECK medium: site 0FC16  INDR  (port in C; 21 bytes of valid code before it)
# CHECK low: site 1C7F4  OUT ($3E),A  (memory_control; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1CD22  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 1E4FF  IN A,($7E)  (v_counter; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E503  IN A,($7E)  (v_counter; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E507  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E50B  IN A,($7E)  (v_counter; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E50F  IN A,($7E)  (v_counter; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E513  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E517  IN A,($7E)  (v_counter; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E51B  IN A,($7E)  (v_counter; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E51F  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E523  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E527  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E52B  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E52F  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E533  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E537  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E53B  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E53F  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E543  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E547  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E54B  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E54F  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E553  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E557  IN A,($7E)  (v_counter; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 1E55B  IN A,($7E)  (v_counter; branch target from $1E4EA; 32 bytes of valid code before it)
# CHECK low: site 21375  IN A,($7F)  (h_counter; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 26C9D  OUT ($C0),A  (no_effect; no evidence)
# CHECK medium: site 274A7  OUTD  (port in C; 32 bytes of valid code before it)
# CHECK low: site 32FEA  OUT ($C1),A  (no_effect; no valid code after it)
# CHECK low: site 33002  OUT ($C1),A  (no_effect; no valid code after it)
# CHECK medium: site 3647A  OUT ($C1),A  (no_effect; 15 bytes of valid code before it)
# CHECK medium: site 365BD  OUT ($C1),A  (no_effect; 10 bytes of valid code before it)
# CHECK medium: site 365BF  OUT ($C0),A  (no_effect; 12 bytes of valid code before it)
# CHECK low: site 371A4  OUT ($C0),A  (no_effect; 8 bytes of valid code before it; no valid code after it)
# CHECK low: site 372B2  OUT ($C0),A  (no_effect; no valid code after it)
# CHECK low: site 37350  OUT ($C0),A  (no_effect; no valid code after it)
# CHECK medium: site 37543  OUT ($C1),A  (no_effect; 12 bytes of valid code before it)
# CHECK low: site 39061  IN A,($BF)  (vdp_status; no evidence)
# CHECK medium: site 390F0  OUT ($BD),A  (vdp_control; 17 bytes of valid code before it)
# CHECK low: site 390F7  OUT ($BD),A  (vdp_control; 24 bytes of valid code before it; no valid code after it)
# CHECK low: site 39CAE  OUT ($BF),A  (vdp_control; no evidence)
# CHECK low: site 434FC  OUT ($C0),A  (no_effect; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 4BC3A  OUT ($C0),A  (no_effect; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 52095  OUT ($BF),A  (vdp_control; no valid code after it)
# CHECK low: site 61AA5  IN A,($7F)  (h_counter; 5 RST or NOP opcodes around it (looks like data); 18 bytes of valid code before it)
# CHECK low: site 625C8  OUT ($F0),A  (fm_address; no evidence)
# CHECK low: site 62B2A  IN A,(C)  (port in C; no valid code after it)
# CHECK low: site 65054  IN A,($3F)  (unmapped_read; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 65EC8  IN A,($BF)  (vdp_status; 8 bytes of valid code before it)
# CHECK low: site 6683E  OUT ($7F),A  (psg; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 66B32  OUT ($7F),A  (psg; 16 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 69E8B  OUT ($7E),A  (psg; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 70757  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 7083E  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 70A83  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 70BE9  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 70C10  OUT ($3E),A  (memory_control; branch target from $70C0C; no valid code after it)
# CHECK low: site 70C20  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 70E95  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 71B0F  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 72C40  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 73BF8  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 73C1E  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 73F67  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 7EDD7  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 7EF68  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 7F3F9  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 7F7AA  OUT ($DD),A  (no_effect; no evidence)
# The frame handler's name table streams, as native code in page 1. The handler turns the
# display off at its start ($04C0) and on again after its VRAM work ($0521); through the I/O
# traps the column and row streams took most of the Next's vertical blank, so the display
# went on inside the picture and its top lines showed the backdrop, HUD sprites included.
# Column ($5904-$591A, from $58BA): 27 cells, one control write and two OUTI each, from
# source HL to VRAM HL' (with bit 14) and 64 bytes on, wrapping from row 28 to row 0.
asm 05904 23
    rst $00
    db far_io, pg_colw, ent_colw
    jp $591B
endasm
# Row ($59B0-$59D5, from $5966): B cells from DE to VRAM HL (with bit 14), wrapping to
# the row's start at column 32.
asm 059B0 38
    rst $00
    db far_io, pg_roww, ent_roww
    jp $59D6
endasm
# Sprite table upload ($1409, called at $051B), as native code in one write: even frames send
# $DB00-$DB3F to $3F00 and $DB40-$DBBF to $3F80 ($1418-$15B6); odd frames ($15B7-$179A) keep the first
# 8 sprites and send the rest in reverse order (the game's sprite flicker): Y from $DB00-$DB07
# then $DB3F down to $DB08, X and tile from $DB40-$DB4F then the pairs at $DBBE down to $DB50.
asm 01418 5
    rst $00
    db far_io, pg_spre, ent_spre
    ret
endasm
asm 015B7 5
    rst $00
    db far_io, pg_spro, ent_spro
    ret
endasm
# Loads. Byte-by-byte VRAM writes through the traps made the power-on path to the SEGA logo
# about 120 frames longer than on the Master System.
# Tile writer of the graphics decompressor ($1AA6): each 32-byte tile from $D300 ($1BBE-$1BCB),
# or through the byte table at $0100 ($1BCC-$1BDC), to the VDP's current address.
asm 01BBE 5
    rst $00
    db far_io, pg_tilew, ent_tilew
    ret
endasm
asm 01BCC 5
    rst $00
    db far_io, pg_tilet, ent_tilet
    ret
endasm
# VRAM clear ($77F3): 16K bytes of E from the VDP's current address ($7803-$782C).
asm 07803 9
    rst $00
    db far_io, pg_vclr, ent_vclr
    call $1380              ; as $7829-$782C
    ret
endasm
# Word fill ($1361): BC words of DE from the VDP's current address ($1364-$1371).
asm 01364 5
    rst $00
    db far_io, pg_fillw, ent_fillw
    ret
endasm
# Sonic's sprite art ($10BF, in the frame handler when $D34E bit 7 is set): B blocks of 64
# bytes from DE, in the bank the table at $BCC7/$BE53 names, to VRAM $0000 ($10F0-$1243,
# unrolled OUT ($BE),A; about 180,000 cycles a frame through the traps when Sonic's frame
# changes). With frame 0 ($1244) it clears the 512 bytes ($124E-$1273).
asm 010F0 10
    rst $00
    db far_io, pg_artw, ent_artw
    ld hl,$D34E             ; as $123E-$1243
    res 7,(hl)
    ret
endasm
asm 0124E 5
    rst $00
    db far_io, pg_artz, ent_artz
    ret
endasm
# Rectangle of name table cells ($197F, after its CALL $19D7; objects such as monitors and
# blocks): B rows of C cells from DE to VRAM HL, each row wrapping to its start at column 32,
# rows wrapping from row 28 to row 0 ($1982-$19B8, ends with EI). Page 1 writes the cells and
# draws their Layer 2 pixels.
asm 01982 7
    rst $00
    db far_io, pg_rect, ent_rect
    ei
    ret
endasm
# Animated level tiles ($7FAE, every 8th frame from the frame handler): 128 bytes from HL (bank
# $1D) to VRAM DE ($7FDB-$7FE9, two control writes and an OTIR). animw (page 1) writes them
# into the VRAM copy and has the priority cells that show them drawn again.
asm 07FDB 15
    rst $00
    db far_io, pg_animw, ent_animw
    ret
endasm
page 0 spre spro tilew tilet vclr fillw artw artz
    OPT --zxnext        ; NEXTREG, SWAPNIB, ADD HL,A
; Every entry runs its body on this page's own stack (own, below): the game's stack holds
; only what the game's own code puts there. Interrupts are off while the page stack is in
; use; the entry turns them on again just before its RET when they were on at the site.
spre:   ld (osp_hl),hl
        ld hl,spre_b
        jp own
spro:   ld (osp_hl),hl
        ld hl,spro_b
        jp own
tilew:  ld (osp_hl),hl
        ld hl,tilew_b
        jp own
tilet:  ld (osp_hl),hl
        ld hl,tilet_b
        jp own
vclr:   ld (osp_hl),hl
        ld hl,vclr_b
        jp own
fillw:  ld (osp_hl),hl
        ld hl,fillw_b
        jp own
artw:   ld (osp_hl),hl
        ld hl,artw_b
        jp own
artz:   ld (osp_hl),hl
        ld hl,artz_b
        jp own
; own: HL = the body. Moves to the page stack, runs the body with the site's registers, and
; returns to the runtime with the body's registers and flags.
own:    ld (osp_body),hl
        pop hl                  ; the return into the runtime
        ld (osp_ret),hl
        ld (osp_sp),sp
        ld sp,pstack
        push af
        ld a,i                  ; P/V = the interrupt state at the site
        di
        ld a,0
        jp po,.off
        inc a
.off:   ld (osp_ei),a
        pop af
        ld hl,.back
        push hl
        ld hl,(osp_body)
        push hl
        ld hl,(osp_hl)
        ret                     ; into the body, which returns to .back
.back:  ld (osp_hl),hl
        ld sp,(osp_sp)
        ld hl,(osp_ret)
        push hl
        ld hl,(osp_hl)
        push af
        ld a,(osp_ei)
        or a
        jr z,.di
        pop af
        ei
        ret
.di:    pop af
        ret
osp_hl:   dw 0
osp_body: dw 0
osp_ret:  dw 0
osp_sp:   dw 0
osp_ei:   db 0
        ds 128
pstack:
; spre: as $1418-$15B6: $DB00-$DB3F to $3F00 and $DB40-$DBBF to $3F80. Leaves HL = $DBC0, B = 0,
; C = $BE.
spre_b: nextreg $52,29          ; slot 2: VRAM $2000-$3FFF, $3F00 at $5F00
        ld hl,$DB00
        ld de,$5F00
        ld bc,64
        ldir
        ld hl,$DB40
        ld de,$5F80
        ld bc,128
        ldir
        call sat_end
        ld hl,$DBC0
        ld c,$BE
        ret
; spro: as $15B7-$179A: the same, the first 8 sprites as they are and the rest in reverse.
; Leaves HL = $DB4E, DE = $FFFC, B = 0, C = $BE.
spro_b: nextreg $52,29
        ld hl,$DB00
        ld de,$5F00
        ld bc,8
        ldir
        ld hl,$DB3F             ; Y of sprites 63 down to 8
        ld b,56
.y:     ld a,(hl)
        ld (de),a
        inc e
        dec l
        djnz .y
        ld hl,$DB40
        ld de,$5F80
        ld bc,16
        ldir
        ld hl,$DBBE             ; X and tile of sprites 63 down to 8
        ld b,56
.x:     ld a,(hl)
        ld (de),a
        inc e
        inc l
        ld a,(hl)
        ld (de),a
        inc e
        dec l
        dec l
        dec l
        djnz .x
        call sat_end
        ld hl,$DB4E
        ld de,$FFFC
        ld c,$BE
        ret
; sat_end: after the sprite table was written straight into the VRAM copy (slot 2, as the data
; port writes would write it through vram_put, fw.asm): slot 2 back, sat_dirty $E085 (the mark
; that the sprite table changed), and the VDP state the writes leave: address $0000 (past
; $3FFF), code 1, latch clear, the read buffer the last byte. Interrupts are off, so the
; runtime's sprite update never sees half a table. Runtime internals: SHADOW_PAGE 29, sat_dirty,
; vdp_addr, vdp_code, vdp_latch, vdp_rbuf, cur_mmu.
sat_end:
        ld a,($5FFF)
        ld (vdp_rbuf),a
        ld a,(cur_mmu+2)
        nextreg $52,a
        ld a,1
        ld ($E085),a            ; sat_dirty
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld h,a
        ld l,a
        ld (vdp_addr),hl
        ret
; tilew: as $1BBE-$1BCB. Leaves HL = $D320, B = 0, A = the last byte.
tilew_b:  push ix
        push iy
        ld hl,$D300
        ld de,(vdp_addr)
        ld bc,32
        call ntw
        xor a                   ; the source as the game sees it
        call vw1
        pop iy
        pop ix
        ld hl,$D320
        ld b,0
        ld a,($D31F)
        ret
; tilet: as $1BCC-$1BDC: each byte e of $D300-$D31F written as the byte at $0100 + e.
; Leaves HL = $D320, B = 0, DE = $0100 + the last e, A = the byte written last.
tilet_b:  push ix
        push iy
        ld hl,$D300
        ld bc,tbuf
        ld d,$01
.t:     ld e,(hl)
        ld a,(de)               ; bank 0, mapped at $0000 as the game sees it
        ld (bc),a
        inc hl
        inc c
        ld a,c
        cp low (tbuf+32)
        jr nz,.t
        push de
        ld hl,tbuf
        ld de,(vdp_addr)
        ld bc,32
        call ntw
        ld a,1                  ; the source as mapped now: this page
        call vw1
        pop de
        pop iy
        pop ix
        ld hl,$D320
        ld b,0
        ld a,(tbuf+31)
        ret
; vclr: as $7803-$7828, BC = $0400 passes of 16 bytes of E. Leaves A = 0, BC = 0.
vclr_b:   push ix
        push iy
        push hl
        push de
        ld hl,fbuf
        ld b,0
.f:     ld (hl),e
        inc hl
        djnz .f
        ld hl,fbuf
        ld de,(vdp_addr)
        ld bc,$4000
        call ntw
        ld bc,$0040             ; 64 runs of 256 bytes
        ld ix,0
        ld iy,256
        ld a,1
        call jt_vwrite
        pop de
        pop hl
        pop iy
        pop ix
        ld bc,0
        xor a
        ret
; fillw: as $1364-$1371, BC words of E then D. Leaves A = 0, BC = 0.
fillw_b:  push ix
        push iy
        push hl
        push de
        ld hl,fbuf
        push bc
        ld b,128
.p:     ld (hl),e
        inc hl
        ld (hl),d
        inc hl
        djnz .p
        pop bc
        ld de,(vdp_addr)
        push bc
        sla c
        rl b
        call ntw
        pop bc
.w:     ld a,b                  ; runs of 256 bytes (128 words) while they last
        or a
        jr nz,.big
        ld a,c
        cp 128
        jr c,.last
.big:   push bc
        ld hl,fbuf
        ld bc,$0001             ; 1 run of 256 bytes
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        inc d                   ; DE += 256
        pop bc
        ld a,c
        sub 128
        ld c,a
        jr nc,.w
        dec b
        jr .w
.last:  or a
        jr z,.done
        add a,a                 ; C words, 2 to 254 bytes
        ld b,a
        ld c,1
        ld hl,fbuf
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
.done:  pop de
        pop hl
        pop iy
        pop ix
        ld bc,0
        xor a
        ret
; artw: as $10F0-$123D: B blocks of 64 bytes from DE (slot 2 as the game maps it) to VRAM
; $0000. Leaves B = 0, DE = source + 64 x B, A = the last byte.
artw_b:   push ix
        push iy
        push hl
        ex de,hl                ; HL = the source
        ld a,b                  ; BC = 64 x B bytes
        rrca
        rrca
        ld c,a
        and $3F
        ld b,a
        ld a,c
        and $C0
        ld c,a
        ld de,0
        xor a                   ; the source as the game sees it
        call vw1
        ld a,d
        or e
        jr z,.none
        ld a,2                  ; the last byte again with tw_cnt at TW_MAX * 256: its tw_check
        ld ($E084),a            ; converts the tiles now, after the display-on write, and not in
        dec hl                  ; the next vertical blank (tw_cnt high byte $E084)
        dec de
        ld bc,$0101
        ld ix,0
        ld iy,0
        xor a
        call jt_vwrite
        inc hl
.none:  dec hl
        call jt_peek            ; A = the last byte written
        inc hl
        ex de,hl
        pop hl
        pop iy
        pop ix
        ld b,0
        ret
; vw1: BC bytes from HL to VRAM DE through jt_vwrite's one-byte form (runs of one byte, steps
; of 1), in pieces of at most 256 bytes that stay inside one 8K page of the source.
; A = jt_vwrite's source mode. Leaves HL and DE past the bytes, BC = 0; sets IX = IY = 1.
vw1:    ld (.mode),a
        ld ix,1
        ld iy,1
.l:     ld a,b
        or c
        ret z
        ld (.left),bc
        ld a,h                  ; room = $2000 - (HL & $1FFF)
        and $1F
        ld b,a
        ld c,l
        push hl
        ld hl,$2000
        or a
        sbc hl,bc
        ld bc,(.left)
        or a
        sbc hl,bc
        jr c,.r1                ; room < left: n = room
        ld h,b                  ; else n = left
        ld l,c
        jr .cap
.r1:    add hl,bc
.cap:   ld a,h                  ; at most 256
        or a
        jr z,.c1
        ld hl,256
.c1:    ld (.n),hl
        pop hl
        ld a,(.n)
        ld c,a                  ; runs (256 = 0)
        ld b,1                  ; one byte each
        ld a,(.mode)
        call jt_vwrite
        ld bc,(.n)
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        push hl
        ld hl,(.left)
        or a
        sbc hl,bc
        ld b,h
        ld c,l
        pop hl
        jr .l
.mode:  db 0
.left:  dw 0
.n:     dw 0
; artz: as $124E-$1273: 512 bytes of 0 to the VDP's current address. Leaves A = 0, B = 0.
artz_b:   push ix
        push iy
        push hl
        push de
        ld hl,fbuf
        ld b,0
.z:     ld (hl),0
        inc hl
        djnz .z
        ld hl,fbuf
        ld de,(vdp_addr)
        ld bc,$0002             ; 2 runs of 256 bytes
        ld ix,0
        ld iy,256
        ld a,1
        call jt_vwrite
        pop de
        pop hl
        pop iy
        pop ix
        xor a
        ld b,a
        ret
; ntw: VRAM DE (14 bits) to DE + BC - 1 reaches into the name table (nt_base to + $6FF): page
; 1's Layer 2 wants a whole rebuild (D_FULL, $84A0 with this overlay's page 2, RAM page 118, in
; slot 4). Keeps BC, DE, HL.
ntw:    push hl
        push de
        ld a,d
        and $3F
        ld d,a
        ld hl,(nt_base)
        ld a,h
        add a,7
        ld h,a                  ; the table's end
        or a
        sbc hl,de
        jr c,.no                ; DE at or past the end
        jr z,.no
        ex de,hl
        add hl,bc               ; the range's end
        ld de,(nt_base)
        or a
        sbc hl,de
        jr c,.no                ; ends before the table
        jr z,.no
        nextreg $54,118
        ld a,1
        ld ($84A0),a
        ld a,(cur_mmu+4)
        nextreg $54,a
.no:    pop de
        pop hl
        ret
        align 256
fbuf:   ds 256
tbuf:   ds 32
endpage
# Priority tiles, done by the overlay. Cells with the priority bit (the high byte's bit 4) show
# in front of the sprites: the intro's ring, the levels' foreground and Aqua Lake's water. The
# runtime's priority switch did this with generic passes (its once-a-frame work, pic_ready at
# the display-on write, the marks of every name table write) that cost more than this game's
# vertical blank holds: in Aqua Lake's water the display went on inside the picture in about one
# frame in six. Here the switch is off and pages 1 and 2 do all of it for this game: Layer 2 set
# up as the runtime sets it up for priority, its palette, shown with the display, its Y scroll,
# and its pixels drawn where the game writes the name table, where tiles change and where lines
# come into view. See page 1 for how.
# Display on ($1380-$138D, called from $046F, the frame handler at $0521 and vclr's block): page
# 1 does the register 1 write itself, so it can show Layer 2 after it and draw the lines that
# came into view.
asm 01380 14
    rst $00
    db far_io, pg_dson, ent_dson
    ret
endasm
# Just after the frame handler's V write ($04ED): Layer 2's ring moves with V.
asm 004F1 5   ; LD A,($D15E); BIT 6,A
    rst $00
    db far_io, pg_vscr, ent_vscr
endasm
# CRAM writes, so that Layer 2's palette follows each one. The line interrupt's water palette
# ($05D0-$0652: 16 entries from $065A) and the block writer's loop ($1376-$137F, from $1372: the
# frame handler's palette upload at $12D6).
asm 005D0 131
    rst $00
    db far_io, pg_wpal, ent_wpal
    jp $0653
endasm
asm 01376 10
    rst $00
    db far_io, pg_blkw, ent_blkw
    ret
endasm
page 1 dson vscr colw roww rect animw wpal blkw
    OPT --zxnext        ; NEXTREG, SWAPNIB, ADD HL,A, ADD DE,A, MUL D,E
; Page 1: Layer 2 priority tiles for this game, without the runtime's priority switch.
;
; Set-up (l2_init, at the first display-on): what the runtime's fw2_switches does for the
; switch: NextReg $14 (global transparency) = $24, the colour of Layer 2 entries 0 and 16, which
; fw4_start sets for both Layer 2 palettes whatever the switch; and lay15 = 4 (layer order L S
; U), which r1_hw ORs into NextReg $15 at every register 1 write. The runtime itself still keeps
; Layer 2's mode and bank ($70, $12 = L2_BANK 51, $71: l2_mode), its clip window ($18:
; clip_update), and its X scroll ($16 = pri_x, H scroll - 2: hscroll_set and the copper list's
; head) with the switch off.
; Shown (dson, after the display-on write): port $123B = 2 while register 1 bit 6 is set. The
; runtime's l2_vis writes 0 to the port at every register 1 write when the switch is off, so the
; display-off write ($138E) hides it.
; Palette: the first Layer 2 palette (NextReg $43 = pal43 | $10, $40, $44 twice) gets each CRAM
; entry but 0 and 16 after each CRAM write (wpal, blkw), from cram, as cram_x does.
; Y: Layer 2 is a ring of the 192 lines on screen: screen line y is Layer 2 line (ys + y) mod
; 192 (NextReg $17 = ys) and shows map line (pv + y) mod 224. When V moves by d (vscr, dson), ys
; moves by d and the d lines that come into view are drawn (vm_lines). vscr runs in the vertical
; blank with the display off, so its lines wait (pend_y0, pend_n) and are drawn by dson from the
; name table as the frame handler's writes leave it, after the display-on write, so that the
; display goes on in the vertical blank.
; Pixels: a priority cell's 8 pixels on a line are its tile's (pixel value + 16 for the sprite
; palette, flips done), zeros elsewhere where the line may hold pixels (D_LF). The column, row
; and rectangle writers draw the cells they change (ql_draw); animw draws again the cells that
; show the animated tiles. A whole rebuild (l2_full) draws all 192 lines: at the first
; display-on, and after a write that reached the name table by another way (vclr, fillw, the
; decompressor's tile writers and blkw set D_FULL).
; Lines (seg_draw) are drawn run by run: cells in a row with the same tile and flags (Aqua
; Lake's water) push the same 8 bytes, 4 PUSHes a cell.
;
; Every entry runs on this page's stack with interrupts off, and turns them on again just
; before its RET when they were on at the site. dson, wpal and blkw write the VDP through the
; I/O RST (OUT ($BF),A: inline code 5, OUT ($BE),A: 4), which can run the once-a-frame work and
; map the game's pages back: they map their own pages again after it.
; Runtime internals: part 1: vdp_regs+1, +9, nt_base, cram, vdp_latch, vdp_code, vdp_addr,
; vdp_rbuf, cur_mmu (fixed addresses), pal43 $E09F, mapattr_table $E200, dirty_pages $E440 (a
; bit per tile); part 2 (FW2_PAGE 25): lay15 $27BA (in slot 4 at $87BA). Pages: MAP_PAGE 14
; (slot 0: M0 at $0000 and A8 at $0A00, 40 columns of 2 bytes; M0 holds SMS columns 0-31 and
; 0-7 again, A8 columns 8-31, 0-7, 0-7); SHADOW_PAGE 28, 29 (the VRAM copy: slot 2 for the name
; table, slot 3 for planar tiles); TILE_PAGE 10, 11 (slot 5: the Next tile definitions, tile *
; 32); L2_PAGE 102-107 (slot 6: Layer 2, 32 lines of 256 bytes a page); CODE_PAGE 116 + 2 =
; 118, this overlay's page 2 (slot 4: D_ state).
MAPATTR equ $E200
DIRTY   equ $E440
PAL43   equ $E09F
LAY15   equ $87BA           ; lay15 with FW2_PAGE in slot 4
DPAGE   equ 118             ; page 2 of this overlay: CODE_PAGE 116 + 2
D_MK    equ $8000           ; cell marks, 32 row + column: bit 1, Layer 2 may hold its pixels
D_LF    equ $8380           ; per Layer 2 line: it may hold pixels
D_RF    equ $8440           ; per row: it may have priority cells
D_PT    equ $8460           ; a bit per tile: a priority cell showing it was drawn
D_FULL  equ $84A0           ; a whole rebuild waits
D_INIT  equ $84A1           ; Layer 2 is set up
D_BUF   equ $8500           ; gather's buffer, 1792 bytes
D_RUN   equ $8C00           ; seg_draw's runs, 4 bytes each (256-byte aligned)
D_QL    equ $8E00           ; cells to draw (row, column), at most QL_MAX
QL_MAX  equ 255
dson:   ld (o_hl),hl
        ld hl,dson_b
        jr own
vscr:   ld (o_hl),hl
        ld hl,vscr_b
        jr own
colw:   ld (o_hl),hl
        ld hl,colw_b
        jr own
roww:   ld (o_hl),hl
        ld hl,roww_b
        jr own
rect:   ld (o_hl),hl
        ld hl,rect_b
        jr own
animw:  ld (o_hl),hl
        ld hl,animw_b
        jr own
wpal:   ld (o_hl),hl
        ld hl,wpal_b
        jr own
blkw:   ld (o_hl),hl
        ld hl,blkw_b
; own: HL = the body. Moves to the page stack, runs the body with the site's registers, and
; returns to the runtime with the body's registers and flags.
own:    ld (o_body),hl
        pop hl                  ; the return into the runtime
        ld (o_ret),hl
        ld (o_sp),sp
        ld sp,o_stk
        push af
        ld a,i                  ; P/V = the interrupt state at the site
        di
        ld a,0
        jp po,.off
        inc a
.off:   ld (o_ei),a
        pop af
        ld hl,.back
        push hl
        ld hl,(o_body)
        push hl
        ld hl,(o_hl)
        ret                     ; into the body, which returns to .back
.back:  ld (o_hl),hl
        ld sp,(o_sp)
        ld hl,(o_ret)
        push hl
        ld hl,(o_hl)
        push af
        ld a,(o_ei)
        or a
        jr z,.di
        pop af
        ei
        ret
.di:    pop af
        ret
o_hl:   dw 0
o_body: dw 0
o_ret:  dw 0
o_sp:   dw 0
o_ei:   db 0
        ds 128
o_stk:
; save_r, rest_r: BC, DE, IX, IY and the other set kept around a body's work.
save_r: pop hl
        push bc
        push de
        push ix
        push iy
        exx
        push bc
        push de
        push hl
        exx
        jp (hl)
rest_r: pop hl
        exx
        pop hl
        pop de
        pop bc
        exx
        pop iy
        pop ix
        pop de
        pop bc
        jp (hl)
; dson_b: as $1380-$138D: register 1 = ($D11F) OR $40, kept there. Before the write: the
; set-up and a whole rebuild that waits. After it: Layer 2 shown with the display, then the
; lines that came into view drawn. Leaves HL = $D11F, A = $81.
dson_b: call save_r
        nextreg $54,DPAGE
        ld a,(D_INIT)
        or a
        call z,l2_init
        ld a,(D_FULL)
        or a
        call nz,l2_full
        call vm_rest
        ld hl,$D11F
        ld a,(hl)
        or $40
        ld (hl),a
        rst $00
        db 5                    ; OUT ($BF),A
        ld a,$81
        rst $00
        db 5                    ; OUT ($BF),A: register 1
        call nb_map
        ld a,(vdp_regs+1)       ; Layer 2 shown with the display
        and $40
        jr z,.v
        ld a,(l2on)
        add a,a
.v:     ld bc,$123B
        out (c),a
        ld a,(l2on)
        or a
        jr z,.x
        call c_clr
        call cr_all             ; the cells the frame handler's writers changed
        call ql_all
        ld a,(an_pend)          ; the cells that show the animated tiles
        or a
        call nz,an_cells
        xor a                   ; the lines that came into view
        call vmove
.x:     xor a
        ld (hseen),a
        ld (an_pend),a
        call vm_rest
        call rest_r
        ld hl,$D11F
        ld a,$81
        ret
hseen:  db 0                    ; vscr ran: the frame handler's writes wait for dson
; vscr_b: the ring moves with V; its lines wait for dson. Then as $04F1-$04F5: A = ($D15E),
; flags as BIT 6,A.
vscr_b: push hl
        call save_r
        call nb_map
        ld a,1
        ld (hseen),a
        ld a,(l2on)
        or a
        jr z,.x
        call c_clr
        call vmove
.x:     call vm_rest
        call rest_r
        pop hl
        ld a,($D15E)
        bit 6,a
        ret
; l2_init: Layer 2 set up for priority tiles (slot 4 holds page 2).
l2_init:
        nextreg $14,$24         ; global transparency: L2_TRANS
        nextreg $54,25
        ld a,4
        ld (LAY15),a            ; layer order L S U at the next register 1 write
        nextreg $54,DPAGE
        ld hl,D_LF              ; every line may hold pixels: the rebuild clears them
        ld de,D_LF+1
        ld bc,191
        ld (hl),1
        ldir
        ld a,1
        ld (D_INIT),a
        ld (D_FULL),a
; pal_all: the first Layer 2 palette from cram, entries 1-15 and 17-31.
pal_all:
        ld e,1
.l:     ld a,e
        and $0F
        call nz,pal_e
        inc e
        ld a,e
        cp 32
        jr nz,.l
        ret
; pal_e: Layer 2 palette entry E (not 0 or 16) from cram. Keeps E.
pal_e:  ld a,(PAL43)
        or $10                  ; the first Layer 2 palette
        nextreg $43,a
        ld a,e
        nextreg $40,a
        ld hl,cram
        add hl,a
        ld a,(hl)
        and $3F
        ld hl,p_hi
        add hl,a
        ld a,(hl)
        nextreg $44,a
        ld a,l
        add a,64                ; p_lo (p_hi is 128-aligned)
        ld l,a
        ld a,(hl)
        nextreg $44,a
        ret
; wpal_b: as $05D0-$0652: the 16 bytes at $065A to CRAM, one data port write each. Leaves
; HL = $066A, A = the last byte.
wpal_b: push bc
        push de
        ld hl,$065A             ; bank 0, at $0000
        ld b,16
.l:     ld a,(vdp_addr)
        and $1F
        ld e,a
        ld a,(hl)
        rst $00
        db 4                    ; OUT ($BE),A
        push hl
        ld a,e
        and $0F
        call nz,pal_e
        pop hl
        inc hl
        djnz .l
        pop de
        pop bc
        dec hl
        ld a,(hl)
        inc hl
        ret
; blkw_b: as $1376-$137F: BC bytes from DE to the data port. Leaves DE past them, BC = 0, A = 0,
; Z set. CRAM (code 3): byte by byte through the I/O RST, each with its Layer 2 palette entry.
; VRAM (code 1): through jt_vwrite's one-byte form (vw1), much faster than a trap a byte (the
; main loop writes 128-byte tile blocks this way, with interrupts off); a write that reaches
; the name table asks for a whole rebuild. Any other code: byte by byte, as written.
blkw_b: push hl
        ld a,(vdp_code)
        cp 1
        jr nz,.l
        push ix
        push iy
        ld hl,(vdp_addr)
        call nt_rng
        ex de,hl                ; HL = the source
        ld de,(vdp_addr)
        xor a                   ; the source as the game sees it
        call vw1                ; HL past the source
        ex de,hl
        pop iy
        pop ix
        pop hl
        xor a
        ret
.l:     ld a,(vdp_code)
        ld (bk_c),a
        ld hl,(vdp_addr)
        ld a,l
        and $1F
        ld (bk_e),a
        ld a,(bk_c)
        cp 3
        call nz,nt_hit
        ex de,hl
        call jt_peek            ; the byte as the game sees it
        ex de,hl
        rst $00
        db 4                    ; OUT ($BE),A
        ld a,(bk_c)
        cp 3
        jr nz,.n
        ld a,(bk_e)
        and $0F
        jr z,.n
        push de
        ld a,(bk_e)
        ld e,a
        call pal_e
        pop de
.n:     inc de
        dec bc
        ld a,b
        or c
        jr nz,.l
        pop hl
        ret
bk_c:   db 0
bk_e:   db 0
; nt_rng: VRAM HL to HL + BC - 1 reaching into the name table (nt_base to + $6FF): D_FULL.
; Keeps BC, DE, HL.
nt_rng: push hl
        push de
        ld a,h
        and $3F
        ld h,a
        ex de,hl                ; DE = the start
        ld hl,(nt_base)
        ld a,h
        add a,7
        ld h,a                  ; the table's end
        or a
        sbc hl,de
        jr c,.no
        jr z,.no
        ex de,hl
        add hl,bc               ; the range's end
        ld de,(nt_base)
        or a
        sbc hl,de
        jr c,.no
        jr z,.no
        call nt_full
.no:    pop de
        pop hl
        ret
; nt_hit: VRAM address HL in the name table (nt_base to + $6FF): D_FULL. Keeps BC, DE.
nt_hit: ld a,h
        and $3F
        ld h,a
        push de
        ld de,(nt_base)
        or a
        sbc hl,de
        pop de
        ret c
        ld a,h
        cp 7
        ret nc
nt_full:
        nextreg $54,DPAGE
        ld a,1
        ld (D_FULL),a
        ld a,(cur_mmu+4)
        nextreg $54,a
        ret
; l2_full: the whole of Layer 2 from the name table: marks, row flags and tile bits cleared,
; the rows with priority cells found, ys = 0, pv = V, the 192 lines drawn.
l2_full:
        call nb_map0
        call c_clr
        ld hl,D_MK
        ld de,D_MK+1
        ld bc,895
        ld (hl),0
        ldir
        ld hl,D_RF
        ld de,D_RF+1
        ld bc,95                ; D_RF and D_PT
        ld (hl),0
        ldir
        ld hl,(vm_nt)           ; D_RF: rows with a priority cell
        inc hl
        ld de,D_RF
        ld c,28
.r:     ld b,32
        xor a
.c:     or (hl)
        inc hl
        inc hl
        djnz .c
        and $10
        ld (de),a
        inc de
        dec c
        jr nz,.r
        ld a,(vdp_regs+9)
        cp 224
        jr c,.v
        sub 224
.v:     ld (pv),a
        xor a
        ld (ys),a
        ld (pend_n),a
        ld (D_FULL),a
        ld (dq_n),a
        ld (cr_n),a
        ld (an_pend),a
        nextreg $17,0
        ld bc,192               ; lines 0-191
        call vm_lines
        jp vm_rest
; colw_b: as the game's loop at $5904-$591A, entered at its EXX: the registers in use hold the
; source in HL; the other set holds the first cell's VRAM address in HL (with bit 14). 27 cells
; of 2 bytes, 64 bytes apart in VRAM, from row 28 back to row 0. Leaves the source set in use
; with HL = source + 54, B = 0, C = $BE, Z set; in the other set HL = the address after the
; last cell as the loop leaves it, BC = $0040, DE = $7F07.
colw_b: push ix
        push iy
        ld bc,54
        call gather             ; buf = the 54 bytes; HL = source + 54
        push hl
        exx
        ld a,h
        and $3F
        ld h,a
        ld (c_va),hl            ; the first cell
        exx
        call nb_map
        ld de,(c_va)
        call qset
        call cr_new             ; the record for this column's changed cells
        ld hl,D_BUF
        ld b,27
        call qcol
        call cr_end
        ld hl,(c_va)            ; the last cell: 26 rows on, from row 28 back to row 0
        ld de,26*64
        add hl,de
        ld a,h
        cp $3F
        jr c,.l
        sub 7
        ld h,a
.l:     ld (c_last),hl
        ld de,64
        add hl,de
        ld a,h
        cp $3F
        jr c,.n
        sub 7
        ld h,a
.n:     ld (c_va),hl            ; the next cell
        ld hl,(c_last)          ; the VDP state after the last cell
        inc hl
        inc hl
        call nb_end
        exx
        ld hl,(c_va)
        set 6,h                 ; HL' = the next cell, with bit 14, as the loop leaves it
        ld bc,$0040
        ld de,$7F07
        exx
        pop hl
        ld bc,$00BE
        xor a                   ; Z: B = 0
        pop iy
        pop ix
        ret
c_va:   dw 0
c_last: dw 0
; roww_b: as the game's loop at $59B0-$59D5: B cells from DE to VRAM HL (with bit 14), from the
; row's end back to its start. Leaves DE = source + 2 x cells, B = 0, HL = the address after
; the last cell as the loop leaves it (with bit 14).
roww_b: push ix
        push iy
        push hl
        ex de,hl
        ld a,b
        ld (r_n),a
        ld c,b
        ld b,0
        sla c
        rl b                    ; BC = 2 x cells
        call gather
        ex (sp),hl              ; HL = the VRAM address, the source + 2 x cells kept
        ld a,h
        and $3F
        ld d,a
        ld e,l
        call nb_map
        ld a,(r_n)
        ld b,a
        ld hl,D_BUF
        call ntrow              ; DE = the address after the last cell
        ex de,hl
        call nb_end
        set 6,h
        pop de
        ld b,0
        pop iy
        pop ix
        ret
r_n:    db 0
; rect_b: as $1982-$19B6: B rows of C cells from DE to VRAM HL (without bit 14), each row from
; its end back to its start, rows from $3F00 back to $3800. Leaves B = 0, C, DE = source + 2 x
; B x C, HL = the row after the last, and A and the flags as the loop's last CP $3F.
rect_b: push ix
        push iy
        push hl
        push bc
        ex de,hl                ; HL = the source
        ld e,c
        ld d,b
        mul d,e
        ex de,hl
        add hl,hl
        ld b,h
        ld c,l                  ; BC = 2 x B x C bytes
        ex de,hl
        call gather             ; HL = the source after
        ld (t_src),hl
        call nb_map
        pop bc
        ld a,c
        ld (t_c),a
        ld a,b
        ld (t_rows),a
        pop de                  ; DE = the first row's VRAM address
        ld hl,D_BUF
.r:     push de
        ld a,(t_c)
        ld b,a
        call ntrow              ; HL = the buffer after the row
        ld (t_end),de
        pop de
        ex de,hl
        ld bc,$40               ; the next row: + 64, from $3F00 back to $3800
        add hl,bc
        ld a,h
        ld (t_a),a
        cp $3F
        jr nz,.n
        ld h,$38
.n:     ex de,hl
        ld a,(t_rows)
        dec a
        ld (t_rows),a
        jr nz,.r
        push de
        ld hl,(t_end)
        call nb_end
        pop hl                  ; HL = the row after the last
        ld de,(t_src)
        ld a,(t_c)
        ld c,a
        ld b,0
        pop iy
        pop ix
        ld a,(t_a)              ; A and the flags of the loop's last CP $3F
        cp $3F
        ret
t_a:    db 0
t_src:  dw 0
t_end:  dw 0
t_c:    db 0
t_rows: db 0
; ntrow: B cells from HL (the buffer) to VRAM DE (14 bits), wrapping to the row's start at
; column 32. Leaves HL past the bytes, DE = the address after the last cell (wrapped as the
; game's loop wraps it).
ntrow:  push hl
        push bc
        push de
        call qset
        call q_leanr
        pop de
        pop bc
        pop hl
        push bc
        push de
        call qrow               ; HL past the bytes
        pop de
        pop bc
        ld a,e                  ; DE: the address after the last cell, as the game's loop
        add a,b                 ; leaves it: the row's start + ((column + B) mod 32) x 2
        add a,b
        and $3F
        ld c,a
        ld a,e
        and $C0
        or c
        ld e,a
        ret
; animw_b: as $7FDB-$7FE9: 128 bytes from HL to VRAM DE (4 tiles, T = DE / 32). Leaves
; HL = source + 128, B = 0, C = $BE, A = D OR $40, Z set. When a priority cell showing one of
; the 4 tiles was drawn (D_PT), the cells that show them are drawn again after the write.
animw_b:
        push ix
        push iy
        push de
        ld a,d
        and $3F
        ld d,a
        ld (an_va),de
        ex de,hl                ; T = address / 32
        add hl,hl
        add hl,hl
        add hl,hl               ; carry = T bit 8
        ld a,0
        adc a,a
        ld (an_t+1),a
        ld a,h
        ld (an_t),a
        ex de,hl
        push hl
        call nb_map
        xor a
        ld (an_need),a
        ld a,(l2on)
        or a
        call nz,an_bits         ; some priority cell shows one of the 4 tiles?
        ld (an_need),a
        call vm_rest
        pop hl
        call an_put             ; HL = source + 128
        push hl
        ld a,(an_need)
        or a
        jr z,.done
        ld a,(hseen)            ; in the frame handler: dson draws them
        or a
        jr z,.now
        ld (an_pend),a
        jr .done
.now:   call nb_map
        ld a,(l2on)
        or a
        jr z,.n0
        call c_clr
        call an_cells
.n0:
        call vm_rest
.done:  pop hl
        pop de
        ld a,d
        or $40
        ld bc,$00BE
        pop iy
        pop ix
        cp a                    ; Z, as after the OTIR
        ret
an_va:  dw 0
an_t:   dw 0
; an_put: the 128 bytes from HL to VRAM an_va (4 whole tiles), as the data port writes would
; write them (vram_put, fw.asm): the VRAM copy, the tiles' dirty_pages bits, tiles_dirty and
; tw_cnt; and the VDP state they leave (address after the last byte, code 1, latch clear, the
; read buffer the last byte). Through jt_vwrite's one-byte form this took about 20,000 cycles.
; The 4 tiles need not start on a 128-byte boundary (the rings of the zone that the scripted
; input reaches are at $2DE0, tiles 7 of VRAM page $2D and 0-2 of page $2E), so each tile gets
; the dirty_pages bit of its own address. A source in $4000-$5FFF (slot 2, which takes the
; copy), or a destination that crosses an 8 KB page of the copy, goes through jt_vwrite.
; Leaves HL past the bytes. Runtime internals: SHADOW_PAGE 28, 29, dirty_pages $E440,
; tiles_dirty $E082, tw_cnt $E083.
an_put: ld de,(an_va)
        ld a,h
        and $E0
        cp $40
        jr z,.j
        ld a,d                  ; DE AND $1FFF over $1F80: the bytes cross into the next page
        and $1F
        cp $1F
        jr nz,.d
        ld a,e
        cp $81
        jr c,.d
.j:     ld bc,128
        xor a                   ; the source as the game sees it
        jp vw1
.d:     ld a,d                  ; slot 2: the copy's page of VRAM DE
        rlca
        rlca
        rlca
        and 1
        add a,28
        nextreg $52,a
        ld a,d
        and $1F
        or $40
        ld d,a
        ld bc,128
        ldir
        dec de
        ld a,(de)
        ld (vdp_rbuf),a
        ld a,(cur_mmu+2)
        nextreg $52,a
        push hl
        ld de,(an_va)           ; each tile: bit (address bits 5-7) of dirty_pages + VRAM page
        ld b,4
.t:     ld a,e
        rlca
        rlca
        rlca
        and 7
        ld c,a
        ld a,1
        inc c
.s:     dec c
        jr z,.m
        add a,a
        jr .s
.m:     ld l,d
        ld h,DIRTY>>8
        set 6,l                 ; dirty_pages = $E440 + page
        or (hl)
        ld (hl),a
        ld ($E082),a            ; tiles_dirty
        ld a,e
        add a,32
        ld e,a
        jr nc,.n
        inc d
.n:     djnz .t
        ld hl,($E083)           ; tw_cnt
        ld bc,128
        add hl,bc
        ld ($E083),hl
        ld hl,(an_va)
        add hl,bc
        res 6,h
        ld (vdp_addr),hl
        xor a
        ld (vdp_latch),a
        inc a
        ld (vdp_code),a
        pop hl
        ret
an_need: db 0
an_pend: db 0                   ; dson draws the cells of an_t's tiles
; an_bits: A = the D_PT bits of tiles T to T + 3, ORed
an_bits:
        ld de,(an_t)
        ld b,4
        ld c,0
.t:     push bc
        ld c,e
        ld b,d
        call t_bit
        and (hl)
        pop bc
        or c
        ld c,a
        inc de
        djnz .t
        ld a,c
        ret
; t_bit: tile C + 256 (B bit 0): HL = its D_PT byte, A = its bit. Uses A, HL.
t_bit:  ld a,b
        and 1
        rrca
        rrca
        rrca
        ld l,a
        ld a,c
        rrca
        rrca
        rrca
        and $1F
        or l
        ld hl,D_PT
        add hl,a
        ld a,c
        and 7
        push hl
        ld hl,c_bit
        add hl,a
        ld a,(hl)
        pop hl
        ret
; an_cells: each name table cell with the priority bit whose tile is T to T + 3, in a row that
; may have priority cells, is drawn again (its tile changed). nb_map has run.
an_cells:
        xor a
        ld (an_r),a
.r:     ld a,(an_r)
        ld hl,D_RF
        add hl,a
        ld a,(hl)
        or a
        jr z,.rn
        ld a,(an_r)             ; HL = the row's first entry in the VRAM copy
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,(vm_nt)
        add hl,de
        ld de,(an_t)
        ld b,32
.c:     ld a,(hl)               ; tile low
        inc hl
        bit 4,(hl)
        jr z,.n
        sub e
        cp 4
        jr nc,.n                ; low byte not T to T + 3 (T is a multiple of 4)
        ld a,(hl)               ; tile bit 8 = T's
        xor d
        rra
        jr c,.n
        push hl
        push bc
        push de
        ld a,32
        sub b
        ld (w_col),a
        ld a,(an_r)
        ld (w_row),a
        dec hl
        ld b,(hl)
        inc hl
        ld a,(hl)
        ld (w_lhi),a
        call cell_d
        pop de
        pop bc
        pop hl
.n:     inc hl
        djnz .c
.rn:    ld a,(an_r)
        inc a
        ld (an_r),a
        cp 28
        jr nz,.r
        ret
an_r:   db 0
; vw1: BC bytes from HL to VRAM DE through jt_vwrite's one-byte form (runs of one byte, steps
; of 1), in pieces of at most 256 bytes that stay inside one 8K page of the source.
; A = jt_vwrite's source mode. Leaves HL and DE past the bytes, BC = 0; sets IX = IY = 1.
vw1:    ld (.mode),a
        ld ix,1
        ld iy,1
.l:     ld a,b
        or c
        ret z
        ld (.left),bc
        ld a,h                  ; room = $2000 - (HL & $1FFF)
        and $1F
        ld b,a
        ld c,l
        push hl
        ld hl,$2000
        or a
        sbc hl,bc
        ld bc,(.left)
        or a
        sbc hl,bc
        jr c,.r1                ; room < left: n = room
        ld h,b                  ; else n = left
        ld l,c
        jr .cap
.r1:    add hl,bc
.cap:   ld a,h                  ; at most 256
        or a
        jr z,.c1
        ld hl,256
.c1:    ld (.n),hl
        pop hl
        ld a,(.n)
        ld c,a                  ; runs (256 = 0)
        ld b,1                  ; one byte each
        ld a,(.mode)
        call jt_vwrite
        ld bc,(.n)
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        push hl
        ld hl,(.left)
        or a
        sbc hl,bc
        ld b,h
        ld c,l
        pop hl
        jr .l
.mode:  db 0
.left:  dw 0
.n:     dw 0
; gather: BC bytes (at most 1792) from HL, as the game sees them, into D_BUF (page 2, slot 4,
; mapped here). Leaves HL past them.
gather: nextreg $54,DPAGE
        push de
        ld de,D_BUF
        ld a,h                  ; from $4000 on (RAM, the banked slots): one LDIR
        cp $40
        jr c,.l
        ldir
        pop de
        ret
.l:     ld a,h                  ; $2000-$3FFF holds this page: those bytes through jt_peek
        and $E0
        cp $20
        jr z,.pk
        ldi
        jp pe,.l
        pop de
        ret
.pk:    call jt_peek
        ld (de),a
        inc de
        inc hl
        dec bc
        ld a,b
        or c
        jr nz,.l
        pop de
        ret
; nb_map: slots 0 MAP_PAGE, 2 the VRAM copy page of the name table (vm_nt: the table there),
; 4 page 2; l2on (Layer 2 is drawn: set up, no whole rebuild waiting) and the tile cache
; emptied. Keeps DE.
nb_map: call nb_map0
        xor a
        ld (l2on),a
        ld a,(D_INIT)
        or a
        ret z
        ld a,(D_FULL)
        or a
        ret nz
        inc a
        ld (l2on),a
        ret
c_clr:  ld a,$FF
        ld (lk_b),a
        ld hl,c_key             ; empty the tile cache: no key is $FF $FF
        ld (hl),$FF
        push de
        ld de,c_key+1
        ld bc,63
        ldir
        pop de
        ret
nb_map0:
        nextreg $50,14
        nextreg $54,DPAGE
        ld hl,(nt_base)
        ld a,h
        rlca
        rlca
        rlca
        and 1
        add a,28
        nextreg $52,a
        ld a,h
        and $1F
        or $40
        ld h,a
        ld (vm_nt),hl
        ret
l2on:   db 0
vm_nt:  dw 0
; nb_end: the VDP state after the writes, HL = the address after the last byte (bits 14 and 15
; cleared); the slots back.
nb_end: ld a,h
        and $3F
        ld h,a
        ld (vdp_addr),hl
        xor a
        ld (vdp_latch),a
        inc a
        ld (vdp_code),a
        ld a,(w_lhi)
        ld (vdp_rbuf),a
vm_rest:
        ld a,(cur_mmu+0)
        nextreg $50,a
        ld a,(cur_mmu+2)
        nextreg $52,a
        ld a,(cur_mmu+3)
        nextreg $53,a
        ld a,(cur_mmu+4)
        nextreg $54,a
        ld a,(cur_mmu+5)
        nextreg $55,a
        ld a,(cur_mmu+6)
        nextreg $56,a
        ret
; qset: the cell pointers for VRAM DE (even, 14 bits, in the name table): q_sh its entry in the
; VRAM copy (slot 2), q_m0 its M0 entry (slot 0), q_mk its mark, q_row, q_col. Uses A, DE, HL.
qset:   ld a,d
        and $1F
        or $40
        ld h,a
        ld l,e
        ld (q_sh),hl
        ld hl,(nt_base)
        ex de,hl
        or a
        sbc hl,de               ; HL = o, the offset in the table
        ld a,l
        rrca
        and 31
        ld (q_col),a
        ld a,l
        rlca
        rlca
        and 3
        ld e,a
        ld a,h
        add a,a
        add a,a
        or e
        ld (q_row),a            ; row 0-27
        ld e,a
        ld d,16
        mul d,e
        add hl,de               ; o + 16 row: the M0 entry
        ld (q_m0),hl
        ld a,(q_row)
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld a,(q_col)
        add hl,a
        ld de,D_MK
        add hl,de
        ld (q_mk),hl
        ret
q_sh:   dw 0
q_m0:   dw 0
q_mk:   dw 0
q_row:  db 0
q_col:  db 0
; qcol, qrow: B cells from HL (the buffer: tile, high byte) from the cell at the q_ pointers,
; down a column (from row 27 back to row 0) or along a row (from column 31 back to column 0),
; as data port writes would write them: the VRAM copy and the Next tilemaps (nt_put: M0 and,
; through mapattr_table, the attribute byte; A8 and M0 columns 32-39 as copies). With Layer 2
; on (l2on), each cell whose entry changes goes into D_QL (q_note): dson draws them after the
; frame handler's writes, other callers at once (q_end). Name table rows 24-27, which the
; runtime also counts as tile data (region_tab 3), get no dirty_pages marks: their tiles
; (496-503) are never shown in Sonic 2 (name table at $3800, sprite table at $3F00, sprite
; tiles from $0000), and their conversion cost about 20,000 cycles in the display-on write of
; each frame with a column write. Leave HL past the bytes. Use A, BC, DE, IX, IY.
qcol:   ld de,(q_sh)
        ld ix,(q_m0)
        call q_iy
        ld a,(q_col)
        cp 8
        jp c,qcol_lo
.c:     ld a,(de)               ; the low byte: the copy, M0, A8
        xor (hl)
        ld c,a
        ld a,(hl)
        ld (de),a
        ld (ix+0),a
        ld (iy+0),a
        inc hl
        inc e
        ld a,(de)               ; the high byte: the copy, the attribute in M0, A8
        xor (hl)
        or c
        ld c,a
        ld a,(hl)
        ld (de),a
        inc hl
        push hl
        ld h,MAPATTR>>8
        ld l,a
        ld a,(hl)
        pop hl
        ld (ix+1),a
        ld (iy+1),a
        ld a,c                  ; changed: into the record (HL' walks it)
        exx
        ld (hl),a
        inc hl
        exx
        ld a,63                 ; down: + 64, M0 and A8 + 80
        add de,a
        push bc
        ld bc,80
        add ix,bc
        add iy,bc
        pop bc
        ld a,(q_row)
        inc a
        ld (q_row),a
        cp 28
        call z,q_cwrap
        djnz .c
        ret
; qcol_lo: qcol for SMS columns 0-7, which M0 also holds in columns 32-39 and A8 in columns
; 24-31 and 32-39 (IY and IY + 16)
qcol_lo:
.c:     ld a,(de)
        xor (hl)
        ld c,a
        ld a,(hl)
        ld (de),a
        ld (ix+0),a
        ld (ix+64),a
        ld (iy+0),a
        ld (iy+16),a
        inc hl
        inc e
        ld a,(de)
        xor (hl)
        or c
        ld c,a
        ld a,(hl)
        ld (de),a
        inc hl
        push hl
        ld h,MAPATTR>>8
        ld l,a
        ld a,(hl)
        pop hl
        ld (ix+1),a
        ld (ix+65),a
        ld (iy+1),a
        ld (iy+17),a
        ld a,c
        exx
        ld (hl),a
        inc hl
        exx
        ld a,63
        add de,a
        push bc
        ld bc,80
        add ix,bc
        add iy,bc
        pop bc
        ld a,(q_row)
        inc a
        ld (q_row),a
        cp 28
        call z,q_cwrap
        djnz .c
        ret
; cr_new: a column record at cr_tab (column, first row, then a byte per cell: not 0 when the
; cell's entry changed), HL' on its first cell byte. CR_MAX records wait for dson; past that
; the record goes into the spare slot after them, and cr_end draws it at once.
CR_MAX  equ 4
cr_new: ld a,(cr_n)
        add a,a
        add a,a
        add a,a
        add a,a
        add a,a
        ld hl,cr_tab
        add hl,a
        ld a,(q_col)
        ld (hl),a
        inc hl
        ld a,(q_row)
        ld (hl),a
        inc hl
        push hl
        exx
        pop hl
        exx
        ret
; cr_end: with Layer 2 on, the record waits for dson (in the frame handler, CR_MAX at most),
; or is drawn now.
cr_end: ld a,(l2on)
        or a
        ret z
        ld a,(cr_n)
        cp CR_MAX
        jr nc,cr_draw
        ld b,a
        ld a,(hseen)
        or a
        ld a,b
        jr z,cr_draw
        inc a
        ld (cr_n),a
        ret
; cr_draw: record A drawn
cr_draw:
        add a,a
        add a,a
        add a,a
        add a,a
        add a,a
        ld hl,cr_tab
        add hl,a
        push hl
        call c_clr
        pop hl
; col_draw: the changed cells of the column record at HL, as cell_c draws them, row by row
; with the row's entry, mark and top screen line carried from one row to the next.
col_draw:
        ld a,(hl)
        ld (w_col),a
        inc hl
        ld a,(hl)
        ld (cd_row),a
        inc hl
        ld (cd_p),hl
        ld a,(cd_row)
        call row_p              ; HL = the row's first entry, DE = its first mark
        ld a,(w_col)
        add a,a
        add hl,a
        ld (cd_e),hl
        ex de,hl
        ld a,(w_col)
        add hl,a
        ld (cd_m),hl
        ld a,(cd_row)
        add a,a
        add a,a
        add a,a
        ld hl,pv
        sub (hl)
        jr nc,.y
        add a,224
.y:     ld (cd_y0),a
        ld a,27
        ld (cd_n),a
.c:     ld hl,(cd_p)
        ld a,(hl)
        inc hl
        ld (cd_p),hl
        or a
        jr z,.nx
        ld a,(cd_row)
        ld (w_row),a
        ld hl,(cd_e)
        ld b,(hl)               ; B = tile low, w_lhi = high byte
        inc hl
        ld a,(hl)
        ld (w_lhi),a
        ld ix,(cd_m)
        ld a,(cd_y0)
        ld (w_y0),a
        call cell_y
.nx:    ld a,(cd_row)
        inc a
        ld de,64
        ld bc,32
        cp 28
        jr c,.r
        xor a                   ; row 28: row 0
        ld de,-27*64
        ld bc,-27*32
.r:     ld (cd_row),a
        ld hl,(cd_e)
        add hl,de
        ld (cd_e),hl
        ld hl,(cd_m)
        add hl,bc
        ld (cd_m),hl
        ld a,(cd_y0)
        add a,8
        cp 224
        jr c,.yy
        sub 224
.yy:    ld (cd_y0),a
        ld hl,cd_n
        dec (hl)
        jr nz,.c
        ret
cd_e:   dw 0
cd_m:   dw 0
cd_row: db 0
cd_y0:  db 0
cd_n:   db 0
cd_p:   dw 0
cr_n:   db 0
cr_tab: ds 32*(CR_MAX+1)
; q_cwrap: row 28 is row 0 again; q_cwrap: row 28 is row 0 again: the copy - 28 x 64, M0 and A8 - 28 x 80
q_cwrap:
        xor a
        ld (q_row),a
        push hl
        push bc
        ld hl,-28*64
        add hl,de
        ex de,hl
        ld bc,-28*80
        add ix,bc
        add iy,bc
        pop bc
        pop hl
        ret
; qrow: the copy and M0 cell by cell (IY on M0), from column 32 back to column 0 (the row
; lies in one 256-byte page of the copy); then A8 and M0 columns 32-39 for the whole row from
; M0 columns 0-31 (q_rowfix).
qrow:   ld de,(q_sh)
        ld iy,(q_m0)
.c:     ld a,(de)
        xor (hl)
        ld c,a
        ld a,(hl)
        ld (de),a
        ld (iy+0),a
        inc hl
        inc e
        ld a,(de)
        xor (hl)
        or c
        ld c,a
        ld a,(hl)
        ld (de),a
        inc hl
        inc e
        push hl
        ld h,MAPATTR>>8
        ld l,a
        ld a,(hl)
        pop hl
        ld (iy+1),a
        ld a,c
        or a
        call nz,q_noter
        inc iy
        inc iy
        ld a,e
        and $3F
        jr z,.w
.n:     djnz .c
        jr q_rowfix
.w:     ld a,e                  ; column 32: back to column 0
        sub 64
        ld e,a
        push bc
        ld bc,-64
        add iy,bc
        pop bc
        jr .n
; q_rowfix: row q_row's A8 columns 0-23 = M0 columns 8-31, A8 columns 24-31 and 32-39 and M0
; columns 32-39 = M0 columns 0-7 (as nt_put writes them). Keeps HL.
q_rowfix:
        push hl
        ld a,(q_row)
        ld e,a
        ld d,80
        mul d,e
        push de                 ; M0 row
        ld hl,16
        add hl,de
        push hl
        ld hl,$0A00
        add hl,de
        ex de,hl                ; DE = A8 row
        pop hl                  ; HL = M0 column 8
        ld bc,48
        ldir
        pop hl
        push hl
        ld bc,16
        ldir                    ; A8 columns 24-31
        pop hl
        push hl
        ld bc,16
        ldir                    ; A8 columns 32-39
        pop hl
        ld de,64
        ex de,hl
        add hl,de
        ex de,hl
        ld bc,16
        ldir                    ; M0 columns 32-39
        pop hl
; q_end: in the frame handler the noted cells wait for dson; else they are drawn now. Keeps HL.
q_end:  ld a,(hseen)
        or a
        ret nz
        ld a,(dq_n)
        or a
        ret z
        push hl
        call c_clr
        pop hl
        jp ql_all
; q_leanr: q_lean = row q_row has no line on screen, or all of them wait for dson: then its
; changed cells are not noted (the lines are drawn whole when they come into view), only the
; row's D_RF flag for a priority cell. Uses A, C, D, E, HL.
q_leanr:
        ld a,(q_row)
        add a,a
        add a,a
        add a,a
        ld hl,pv
        sub (hl)
        jr nc,.y0
        add a,224
.y0:    ld (w_y0),a
        ld c,1
        cp 192
        jr c,.v
        cp 217
        jr c,.s
.v:     dec c
        ld a,(pend_n)
        or a
        jr z,.s
        call pw_all
        ld a,0
        adc a,a
        ld c,a
.s:     ld a,c
        ld (q_lean),a
        ret
q_lean: db 0
; q_noter: q_note for the cell before DE (qrow); in a lean row, only D_RF for a priority cell
; (HL is past the cell)
q_noter:
        ld a,(q_lean)
        or a
        jr z,.n
        ld a,(l2on)
        or a
        ret z
        dec hl
        ld a,(hl)
        inc hl
        and $10
        ret z
        push hl
        ld a,(q_row)
        ld hl,D_RF
        add hl,a
        ld (hl),1
        pop hl
        ret
.n:     ld a,e
        sub 2
        and $3F
        rrca
        ld (q_col),a
; q_note: with Layer 2 on, cell (q_row, q_col) into D_QL. Past QL_MAX cells, a whole rebuild.
; Uses A.
q_note: ld a,(l2on)
        or a
        ret z
        push hl
        ld a,(dq_n)
        cp QL_MAX
        jr nc,.full
        inc a
        ld (dq_n),a
        dec a
        ld l,a
        ld h,0
        add hl,hl
        ld a,D_QL>>8
        add a,h
        ld h,a
        ld a,(q_row)
        ld (hl),a
        inc hl
        ld a,(q_col)
        ld (hl),a
        pop hl
        ret
.full:  ld a,1
        ld (D_FULL),a
        pop hl
        ret
dq_n:   db 0
; cr_all: the column records that wait, drawn
cr_all: ld a,(cr_n)
        or a
        ret z
        ld b,a
        xor a
        ld (cr_n),a
        ld hl,cr_tab
.r:     push bc
        push hl
        call col_draw
        pop hl
        ld a,32
        add hl,a
        pop bc
        djnz .r
        ret
; ql_all: the cells in D_QL drawn, the list emptied. Keeps HL.
ql_all: ld a,(dq_n)
        or a
        ret z
        push hl
        ld b,a
        xor a
        ld (dq_n),a
        ld hl,D_QL
        call ql_draw
        pop hl
        ret
; q_iy: IY = the A8 entry for the M0 entry IX: M0 + $0A00 - 16 for columns 8-31; M0 + 64 + $0A00
; - 16 (A8 columns 24-31) for columns 0-7, whose A8 columns 32-39 are 16 bytes on.
q_iy:   push ix
        pop iy
        push bc
        ld bc,$0A00-16
        ld a,(q_col)
        cp 8
        jr nc,.h
        ld bc,64+$0A00-16
.h:     add iy,bc
        pop bc
        ret
; ql_draw: Layer 2 for the B cells (row, column) at HL, as cell_c draws them. What depends only on the
; row (its first entry and mark, its top line on screen, and whether any of its lines on screen
; is drawn now rather than by dson) is worked out once a row, and a tile whose D_PT bit was
; just set is not looked up again. A row with no line to draw now only gets its marks and
; flags: the row writes come at the edge of the picture, where V has just moved. Keeps HL.
ql_draw:
        ld a,$FF
        ld (qm_row),a
        ld (qm_th),a
.l:     push bc
        ld a,(hl)
        ld (w_row),a
        inc hl
        ld a,(hl)
        ld (w_col),a
        inc hl
        push hl
        ld a,(w_row)
        ld hl,qm_row
        cp (hl)
        call nz,qm_new
        ld hl,(qm_nt)           ; the entry: B = tile low, w_lhi = high byte
        ld a,(w_col)
        add a,a
        add hl,a
        ld b,(hl)
        inc hl
        ld a,(hl)
        ld (w_lhi),a
        ld hl,(qm_mk)           ; IX = its mark
        ld a,(w_col)
        add hl,a
        push hl
        pop ix
        ld a,(w_lhi)
        bit 4,a
        jr z,.np
        set 1,(ix+0)            ; the priority bit: Layer 2 holds it
        ld a,(qm_rf)
        or a
        call z,qm_flag
        ld c,b                  ; its D_PT bit, unless it was the last tile's
        ld a,(w_lhi)
        and 1
        ld b,a
        ld a,(qm_tl)
        cp c
        jr nz,.tb
        ld a,(qm_th)
        cp b
        jr z,.tk
.tb:    ld a,c
        ld (qm_tl),a
        ld a,b
        ld (qm_th),a
        call t_bit
        or (hl)
        ld (hl),a
.tk:    ld a,(qm_lean)
        or a
        jr nz,.nx
        ld a,(w_lhi)            ; C = tile low, B = the high byte's low nibble
        and $0F
        ld b,a
        call c_get
        ld (w_px),hl
        ld a,1
        ld (w_on),a
        call cell_l
        jr .nx
.np:    bit 1,(ix+0)            ; no priority bit: zeros, if Layer 2 holds the cell
        jr z,.nx
        res 1,(ix+0)
        ld a,(qm_lean)
        or a
        jr nz,.nx
        xor a
        ld (w_on),a
        call cell_l
.nx:    pop hl
        pop bc
        dec b
        jp nz,.l
        ret
; qm_new: row A's pointers, top line and lean flag (HL = qm_row)
qm_new: ld (hl),a
        xor a
        ld (qm_rf),a
        ld a,(w_row)
        call row_p
        ld (qm_nt),hl
        ld (qm_mk),de
        ld a,(w_row)            ; y0: the screen line of the row's top (mod 224)
        add a,a
        add a,a
        add a,a
        ld hl,pv
        sub (hl)
        jr nc,.y0
        add a,224
.y0:    ld (w_y0),a
        ld c,1                  ; lean: no line on screen, or all of them wait
        cp 192
        jr c,.v
        cp 217
        jr c,.s
.v:     dec c
        ld a,(pend_n)
        or a
        jr z,.s
        call pw_all
        ld a,0
        adc a,a
        ld c,a
.s:     ld a,c
        ld (qm_lean),a
        ret
qm_flag:
        ld a,(w_row)            ; the row has priority cells
        ld hl,D_RF
        add hl,a
        ld (hl),1
        ld a,1
        ld (qm_rf),a
        ret
qm_row: db 0
qm_rf:  db 0
qm_tl:  db 0
qm_th:  db 0
qm_lean: db 0
qm_nt:  dw 0
qm_mk:  dw 0

; w_mark: IX = the mark of cell (w_row, w_col), D_MK + 32 row + column. Uses A, HL.
w_mark: ld a,(w_row)
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld a,(w_col)
        add hl,a
        ld a,h
        add a,D_MK>>8
        ld h,a
        push hl
        pop ix
        ret
; cell_d: cell (w_row, w_col) with tile B, high byte w_lhi is drawn again.
cell_d: call w_mark
; cell_c: Layer 2 for cell (w_row, w_col), mark IX, tile B, high byte w_lhi.
cell_c: ld a,(w_row)            ; y0: the screen line of its top (mod 224)
        add a,a
        add a,a
        add a,a
        ld hl,pv
        sub (hl)
        jr nc,.y0
        add a,224
.y0:    ld (w_y0),a
; cell_y: the same with w_y0 set.
cell_y: ld a,(w_lhi)
        bit 4,a
        jr nz,.p
        bit 1,(ix+0)            ; no priority bit: zeros, if Layer 2 holds the cell
        ret z
        res 1,(ix+0)
        xor a
        ld (w_on),a
        jr cell_l
.p:     set 1,(ix+0)            ; the priority bit: Layer 2 holds it
        ld a,(w_row)            ; the row has priority cells
        ld hl,D_RF
        add hl,a
        ld (hl),1
        ld c,b                  ; C = tile low, B = the high byte's low nibble
        ld a,(w_lhi)
        and $0F
        ld b,a
        ld a,(lk_c)             ; the last c_get's tile: its D_PT bit is set
        cp c
        jr nz,.tb
        ld a,(lk_b)
        cp b
        jr z,.tk
.tb:    call t_bit              ; its D_PT bit
        or (hl)
        ld (hl),a
.tk:    ld a,(w_y0)             ; no line on screen: nothing to draw
        cp 192
        jr c,.v
        cp 217
        ret c
.v:     ld a,(pend_n)           ; every line on screen waits for dson: nothing to draw now
        or a
        jr z,.g
        push bc
        call pw_all
        pop bc
        ret c
        jr .g
; pw_all: carry when every line of cell row w_y0 that is on screen waits for dson (pend_n not 0).
; Uses A, C, D, E.
pw_all: ld a,(w_y0)             ; lines D (the first on screen) to E (the last)
        ld d,a
        add a,7
        ld e,a
        cp 191
        jr c,.v1
        ld e,191
.v1:    ld a,d
        cp 192
        jr c,.v2
        ld d,0                  ; y0 217-223: lines 0 to y0 + 7 - 224
        ld a,(w_y0)
        add a,7-224
        ld e,a
.v2:    ld a,(pend_y0)
        ld c,a
        ld a,d
        cp c
        ccf
        ret nc                  ; a line above the first waiting one
        ld a,(pend_n)
        add a,c
        ld c,a                  ; C = past the last waiting line
        ld a,e
        cp c
        ret
cell_y.g:
        call c_get
        ld (w_px),hl
        ld a,1
        ld (w_on),a
; cell_l: the cell's lines on screen: y = y0 + k (mod 224) below 192 is Layer 2 line
; (ys + y) mod 192: its 8 bytes from w_px + 8k (w_on 1) or zeros where D_LF is set.
cell_l: ld a,(pend_n)            ; a waiting line among the 8: line by line
        or a
        jr z,.np
        ld a,(w_y0)
        ld hl,pend_y0
        add a,7
        jp c,.slow              ; y0 near 224: the slow form looks
        cp (hl)
        jr c,.np                ; y0 + 7 below the first waiting line
        ld a,(pend_n)
        add a,(hl)
        ld c,a                  ; C = past the last waiting line
        ld a,(w_y0)
        cp c
        jp c,.slow
.np:    ld a,(w_y0)
        cp 192-7
        jr nc,.slow
        ld hl,ys
        add a,(hl)
        jr c,.w0
        cp 192
        jr c,.f0
.w0:    sub 192
.f0:    cp 192-7                ; all 8 lines on screen, no wrap of the 192-line ring,
        jr nc,.slow             ; one Layer 2 page
        ld e,a
        and $1F
        cp 32-7
        jr nc,.slow
        ld a,e                  ; the fast form
        ld (vl_l),a
        call vl_page            ; DE = the first line's byte 0
        ld a,(w_col)
        add a,a
        add a,a
        add a,a
        ld e,a
        ld hl,D_LF
        ld a,(vl_l)
        add hl,a                ; HL = its D_LF flag
        ld a,(w_on)
        or a
        jr z,.fz
        ld b,8
.fl:    ld (hl),1
        inc hl
        djnz .fl
        ld hl,(w_px)
        ld iyh,8
.fr:    ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        ld a,248                ; the next line: + 256 in all (LDI carries into D at column 31)
        add de,a
        dec iyh
        jr nz,.fr
        ret
.fz:    ld b,8                  ; zeros on the lines that may hold pixels
.fzl:   ld a,(hl)
        or a
        jr z,.fzn
        xor a
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld (de),a
        ld a,e
        sub 7
        ld e,a
.fzn:   inc hl
        inc d
        djnz .fzl
        ret
.slow:  ld b,0                  ; line by line: B = k
.k:     ld a,(w_y0)
        add a,b
        cp 224
        jr c,.k1
        sub 224
.k1:    cp 192
        jr nc,.kn               ; off screen
        ld c,a
        ld a,(pend_n)           ; a waiting line: dson draws it
        or a
        jr z,.kv
        ld a,c
        ld hl,pend_y0
        sub (hl)
        jr c,.kv
        ld hl,pend_n
        cp (hl)
        jr c,.kn
.kv:    ld a,c
        ld hl,ys
        add a,(hl)
        jr c,.kw
        cp 192
        jr c,.kl
.kw:    sub 192
.kl:    ld (vl_l),a
        ld hl,D_LF
        add hl,a
        ld a,(w_on)
        or a
        jr nz,.kp
        ld a,(hl)
        or a
        jr z,.kn                ; no pixels on that line
        push bc
        call vl_page
        ld a,(w_col)
        add a,a
        add a,a
        add a,a
        ld e,a
        xor a
        ld b,8
.kz:    ld (de),a
        inc e
        djnz .kz
        pop bc
        jr .kn
.kp:    ld (hl),1
        push bc
        call vl_page
        ld a,(w_col)
        add a,a
        add a,a
        add a,a
        ld e,a
        ld a,b
        add a,a
        add a,a
        add a,a
        ld hl,(w_px)
        add hl,a
        ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        pop bc
.kn:    inc b
        ld a,b
        cp 8
        jp nz,.k
        ret
w_lhi:  db 0
w_row:  db 0
w_col:  db 0
w_on:   db 0
w_y0:   db 0
w_px:   dw 0
; vmove: Layer 2's ring follows V (vdp_regs+9, mod 224). A = 0: the lines that come into view are
; drawn now; A = 1 (vscr): they wait (pend_y0, pend_n) for the next dson; a writer draws none
; of their pixels meanwhile. Waiting lines are drawn first at every call. nb_map has run, l2on.
vmove:  ld (vm_md),a
        ld a,(pend_n)
        or a
        call nz,vm_flush
        ld a,(vdp_regs+9)
        cp 224
        jr c,.v0
        sub 224
.v0:    ld b,a                  ; B = V
        ld hl,pv
        sub (hl)
        ret z                   ; V did not move
        jr nc,.d0
        add a,224
.d0:    ld (hl),b               ; pv = V
        ld c,a                  ; C = d, 1-223
        cp 113
        jr nc,.up
        ld a,(ys)               ; d = 1-112: ys + d; lines 192 - d to 191 come into view
        add a,c
        jr c,.y1s
        cp 192
        jr c,.y1
.y1s:   sub 192
.y1:    ld (ys),a
        ld a,192
        sub c
        ld b,a                  ; B = the first line, C = lines
        jr .mv
.up:    ld a,224                ; d = -(224 - d): ys - that; lines 0 to 223 - d come into view
        sub c
        ld c,a
        ld a,(ys)
        sub c
        jr nc,.y2
        add a,192
.y2:    ld (ys),a
        ld b,0
.mv:    ld a,(ys)
        nextreg $17,a
        ld a,(vm_md)
        or a
        jr z,vm_lines
        ld a,b
        ld (pend_y0),a
        ld a,c
        ld (pend_n),a
        ret
; vm_flush: the waiting lines drawn
vm_flush:
        ld a,(pend_y0)
        ld b,a
        ld a,(pend_n)
        ld c,a
        xor a
        ld (pend_n),a
; vm_lines: C lines from screen line B drawn (B + C at most 192), in segments of lines that lie
; in one map row and one Layer 2 page (seg_draw). Screen line y is Layer 2 line (ys + y) mod
; 192 and map line (pv + y) mod 224.
vm_lines:
.l:     push bc
        ld a,(pv)
        add a,b
        jr c,.w1
        cp 224
        jr c,.m
.w1:    sub 224
.m:     ld (vs_m),a
        and 7
        ld (vs_k),a
        ld a,(ys)
        add a,b
        jr c,.w2
        cp 192
        jr c,.y
.w2:    sub 192
.y:     ld (vs_l),a
        and $1F
        ld e,a
        ld a,32
        sub e
        ld d,a                  ; D = lines to the Layer 2 page's end
        ld a,(vs_k)
        ld e,a
        ld a,8
        sub e                   ; lines to the cell's end
        cp d
        jr c,.n1
        ld a,d
.n1:    cp c
        jr c,.n2
        ld a,c
.n2:    ld (vs_n),a
        call seg_draw
        pop bc
        ld a,(vs_n)
        ld e,a
        add a,b
        ld b,a
        ld a,c
        sub e
        ld c,a
        jr nz,.l
        ret
; seg_draw: vs_n lines of map row r = vs_m / 8 from line vs_k of its cells into Layer 2 lines
; vs_l onward (one page). A row without priority cells clears the lines that held pixels;
; otherwise the row's cells become runs (run_build) and each run is drawn (run_draw).
seg_draw:
        ld hl,D_LF              ; did any of the lines hold pixels
        ld a,(vs_l)
        add hl,a
        ld (vs_lf),hl
        ld a,(vs_n)
        ld b,a
        xor a
.o:     or (hl)
        inc hl
        djnz .o
        ld (vs_old),a
        ld a,(vs_k)
        add a,a
        add a,a
        add a,a
        ld (vs_k8),a
        ld a,(vs_m)
        rrca
        rrca
        rrca
        and $1F
        ld (vs_r),a
        ld hl,D_RF
        add hl,a
        ld a,(hl)
        or a
        jr nz,.cells
        ld (vs_any),a
        ld a,(vs_old)           ; no priority cells: the lines that held pixels cleared
        or a
        ret z
        ld ix,D_RUN             ; one run of 32 zero cells
        ld (ix+0),0
        ld (ix+1),32
        ld (ix+3),$80
        ld a,4
        ld (rn_end),a
        call run_draw
        jr .f
.cells: call run_build
        call run_draw
.f:     ld hl,(vs_lf)           ; D_LF of the lines
        ld a,(vs_n)
        ld b,a
        ld a,(vs_any)
.fl:    ld (hl),a
        inc hl
        djnz .fl
        ret
; run_build: row vs_r's cells from column 31 back to 0 as runs at D_RUN: x_end (8 x the column
; after the run's last, 0 for 256), cells, key low, key high. A priority cell's key is its tile
; low byte and the high byte's low nibble (tile bit 8, flips, palette); its mark gets bit 1 and
; its tile its D_PT bit. A cell without the priority bit is a zero cell (key high $80) when a
; line held pixels, else it ends the run. Equal neighbours share a run. vs_any: a priority cell.
run_build:
        ld a,(vs_r)
        call row_p              ; HL = the row's first entry, DE = its first mark
        ld bc,63
        add hl,bc               ; the high byte of column 31
        ex de,hl
        ld bc,31
        add hl,bc
        ex de,hl                ; DE = the mark of column 31
        ld ix,D_RUN
        xor a
        ld (vs_any),a
        ld iy,$FFFF             ; no run open
        ld b,32                 ; B = column + 1
.c:     ld a,(hl)
        dec hl
        bit 4,a
        jr z,.np
        and $0F
        ld c,a                  ; C = key high
        ld a,(de)
        or 2
        ld (de),a
        ld a,(hl)               ; key low
        cp iyl
        jr nz,.newp
        ld a,c
        cp iyh
        jr nz,.newp
        inc (ix-3)              ; the open run grows
        jr .nx
.newp:  ld a,(hl)
        ld iyl,a
        ld iyh,c
        ld (ix+2),a
        ld (ix+3),c
        ld (ix+1),1
        ld a,b
        add a,a
        add a,a
        add a,a
        ld (ix+0),a
        ld a,1
        ld (vs_any),a
        push hl
        push bc
        ld a,c
        ld b,a
        ld c,(hl)
        call t_bit
        or (hl)
        ld (hl),a
        pop bc
        pop hl
        ld a,ixl
        add a,4
        ld ixl,a
        jr .nx
.np:    ld a,(vs_old)
        or a
        jr z,.sk
        ld a,iyh                ; a zero cell
        cp $80
        jr nz,.newz
        inc (ix-3)
        jr .nx
.newz:  ld iyh,$80
        ld (ix+3),$80
        ld (ix+1),1
        ld a,b
        add a,a
        add a,a
        add a,a
        ld (ix+0),a
        ld a,ixl
        add a,4
        ld ixl,a
        jr .nx
.sk:    ld iyh,$FF              ; a cell left as it is: the open run ends
.nx:    dec hl
        dec de
        djnz .c
        ld a,ixl
        ld (rn_end),a
        ret
; run_draw: each run at D_RUN (to rn_end) on lines vs_l to vs_l + vs_n - 1: SP at the run's end
; on the line, the line's 8 bytes from the cache entry (or zeros) in BC, DE, IY, HL, and 4
; PUSHes a cell. Interrupts are off; SP comes back from rd_sp.
run_draw:
        ld a,(vs_l)             ; slot 6: the lines' Layer 2 page
        rlca
        rlca
        rlca
        and 7
        add a,102
        nextreg $56,a
        ld (rd_sp),sp
        ld a,low D_RUN
        ld (rd_p),a
.r:     ld a,(rd_p)
        ld hl,rn_end
        cp (hl)
        jr z,.done
        ld l,a
        ld h,D_RUN>>8
        add a,4
        ld (rd_p),a
        ld a,(hl)
        ld (rd_x),a
        inc l
        ld a,(hl)
        ld (rd_n),a
        inc l
        ld c,(hl)               ; key low
        inc l
        ld b,(hl)               ; key high
        ld a,b
        cp $80
        jr z,.z
        ld a,(rd_n)
        dec a
        jr nz,.cg
        call c_part             ; one cell: HL = its line vs_k
        jr .go
.cg:    call c_get              ; HL = the tile's cache entry
        ld a,(vs_k8)
        add a,l                 ; + 8 k (the entry is 64-byte aligned)
        ld l,a
        jr .go
.z:     ld hl,c_zero
.go:    ld a,(vs_l)             ; IX = the run's end on the first line
        and $1F
        or $C0
        ld d,a
        ld a,(rd_x)
        ld e,a
        or a
        jr nz,.e
        inc d                   ; x_end 256: the next line's start
.e:     push de
        pop ix
        ld a,(vs_n)
        ld b,a
        ld a,(rd_n)
        ld c,a
.ln:    ld sp,hl                ; the line's 8 bytes
        ld a,l
        add a,8
        ld l,a
        ld a,c
        exx
        pop bc
        pop de
        pop iy
        pop hl
        ld sp,ix
.p:     push hl
        push iy
        push de
        push bc
        dec a
        jr nz,.p
        inc ixh                 ; the next line
        exx
        djnz .ln
        ld sp,(rd_sp)
        jr .r
.done:  ld sp,(rd_sp)
        ret
rd_sp:  dw 0
rd_p:   db 0
rd_x:   db 0
rd_n:   db 0
rn_end: db 0
vs_m:   db 0
vs_k:   db 0
vs_k8:  db 0
vs_l:   db 0
vs_n:   db 0
vs_r:   db 0
vs_old: db 0
vs_any: db 0
vs_lf:  dw 0
vm_md:  db 0
pend_y0: db 0
pend_n: db 0
ys:     db 0
pv:     db 0
; row_p: A = row: HL = its first entry in the VRAM copy, DE = its first mark (D_MK + 32 row).
row_p:  ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,D_MK
        add hl,de
        ex de,hl                ; DE = the mark
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        push de
        ld de,(vm_nt)
        add hl,de
        pop de
        ret
; vl_page: slot 6 = the Layer 2 page of line vl_l; DE = the line's first byte
vl_page:
        ld a,(vl_l)
        rlca
        rlca
        rlca
        and 7
        add a,102
        nextreg $56,a
        ld a,(vl_l)
        and $1F
        or $C0
        ld d,a
        ld e,0
        ret
vl_l:   db 0
; c_get: HL = the cache entry of tile C + 256 (B bit 0), flips B bits 1-2, palette B bit 3,
; built on a miss (and the tile's D_PT bit set then). Uses A, DE, IYL.
c_get:  ld a,(lk_c)              ; the key of the last c_get: its entry
        cp c
        jr nz,.s
        ld a,(lk_b)
        cp b
        jr nz,.s
        ld hl,(lk_p)
        ret
.s:     ld a,c
        ld (lk_c),a
        ld a,b
        ld (lk_b),a
        xor c
        and 31
        ld e,a                  ; the slot
        add a,a
        ld hl,c_key
        add hl,a
        ld a,(hl)
        cp c
        jr nz,.miss
        inc hl
        ld a,(hl)
        cp b
        jr nz,.miss1
        call c_ent
        ld (lk_p),hl
        ret
.miss:  ld (hl),c
        inc hl
.miss1: ld (hl),b
        call c_ent
        ld (lk_p),hl
        push hl
        xor a
        ld (cb_k),a
        ld a,8
        ld (cb_n),a
        call c_build
        pop hl
        ret
lk_c:   db 0
lk_b:   db $FF
lk_p:   dw 0
; c_part: HL = line vs_k of tile C + 256 (B bit 0), flags B: in its cache entry when the cache
; holds it, else lines vs_k to vs_k + vs_n - 1 only, built into c_tmp (a run of one cell does
; not pay for the 8 lines of a cache entry).
c_part: ld a,c
        xor b
        and 31
        ld e,a
        add a,a
        ld hl,c_key
        add hl,a
        ld a,(hl)
        cp c
        jr nz,.m
        inc hl
        ld a,(hl)
        cp b
        jr nz,.m
        call c_ent
        jr .k
.m:     ld a,(vs_k)
        ld (cb_k),a
        ld a,(vs_n)
        ld (cb_n),a
        ld hl,c_tmp
        push hl
        call c_build
        pop hl
.k:     ld a,(vs_k8)
        add a,l
        ld l,a
        ret
; c_ent: HL = c_dat + 64 E (c_dat is 256-byte aligned)
c_ent:  ld a,e
        rrca
        rrca
        ld l,a
        and $07
        add a,c_dat>>8
        ld h,a
        ld a,l
        and $C0
        ld l,a
        ret
; c_build: entry HL for tile C + 256 (B bit 0), flags B. Its D_PT bit is set. A tile that waits
; for conversion (its dirty_pages bit) comes from the planar tile in the VRAM copy.
c_build:
        ex de,hl                ; DE = the entry
        push bc
        ld a,b                  ; D_PT: byte (tile >> 3), bit (tile & 7)
        and 1
        rrca
        rrca
        rrca
        ld l,a
        ld a,c
        rrca
        rrca
        rrca
        and $1F
        or l
        ld l,a
        ld h,0
        push hl
        ld a,c
        and 7
        ld hl,c_bit
        add hl,a
        ld a,(hl)
        ld (cb_bit),a
        pop hl
        push hl
        ld bc,D_PT
        add hl,bc
        or (hl)
        ld (hl),a
        pop hl
        ld bc,DIRTY             ; waits for conversion?
        add hl,bc
        ld a,(cb_bit)
        and (hl)
        ld (cb_dty),a
        pop bc
        ld a,b
        and 8
        add a,a
        ld (cb_pal),a           ; $10: the sprite palette
        ld iyl,a
        ld a,b
        ld (cb_fl),a
        ld h,0
        ld l,c
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl               ; HL = (tile & 255) * 32
        ld a,(cb_dty)
        or a
        jp nz,cb_planar
        ld a,b                  ; the Next definition, slot 5
        and 1
        add a,10
        nextreg $55,a
        ld a,h
        add a,$A0
        ld h,a
        call cb_rows
.r:     push bc
        ld a,(cb_pal)
        ld c,a
        ld a,(cb_fl)
        bit 1,a
        jp nz,.h
        rept 4
        ld a,(hl)
        swapnib
        and $0F
        or c
        ld (de),a
        inc de
        ld a,(hl)
        and $0F
        or c
        ld (de),a
        inc de
        inc hl
        endr
        jp .rn
.h:     inc hl
        inc hl
        inc hl
        rept 4
        ld a,(hl)
        and $0F
        or c
        ld (de),a
        inc de
        ld a,(hl)
        swapnib
        and $0F
        or c
        ld (de),a
        inc de
        dec hl
        endr
        inc hl
        inc hl
        inc hl
        inc hl
        inc hl                  ; past the row (HL was row - 1)
.rn:    ld a,(cb_fl)
        bit 2,a
        jr z,.rd
        ld bc,-8                ; V flip: the row above
        add hl,bc
.rd:    pop bc
        dec b
        jp nz,.r
        ret
; cb_planar: the planar tile in the VRAM copy (4 bytes a row, plane 0 first), slot 3
cb_planar:
        ld a,b
        and 1
        add a,28
        nextreg $53,a
        ld a,h
        add a,$60
        ld h,a
        call cb_rows
.r:     push bc
        push hl
        ld a,(hl)
        inc hl
        ld c,(hl)
        inc hl
        ld b,(hl)
        inc hl
        ld l,(hl)
        ld h,b
        ld b,a                  ; B, C, H, L = planes 0-3
        ld a,(cb_fl)
        bit 1,a
        jp nz,.h
        rept 8
        xor a
        sla l
        rla
        sla h
        rla
        sla c
        rla
        sla b
        rla
        or iyl
        ld (de),a
        inc de
        endr
        jp .rn
.h:     rept 8
        xor a
        srl l
        rla
        srl h
        rla
        srl c
        rla
        srl b
        rla
        or iyl
        ld (de),a
        inc de
        endr
.rn:    pop hl
        ld bc,4
        ld a,(cb_fl)
        bit 2,a
        jr z,.rd
        ld bc,-4
.rd:    add hl,bc
        pop bc
        dec b
        jp nz,.r
        ret
; cb_rows: rows cb_k to cb_k + cb_n - 1: HL (row 0 of the tile, 4 bytes a row) to row cb_k's (the
; last row up with V flip), DE (the entry) to its line cb_k, B = cb_n.
cb_rows:
        ld a,(cb_k)
        add a,a
        add a,a
        ld c,a                  ; 4 k
        ld a,(cb_fl)
        bit 2,a
        ld a,c
        jr z,.n
        ld a,28
        sub c
.n:     add hl,a
        ld a,c
        add a,a
        add de,a                ; 8 k
        ld a,(cb_n)
        ld b,a
        ret
cb_k:   db 0
cb_n:   db 8
cb_bit: db 0
cb_dty: db 0
cb_pal: db 0
cb_fl:  db 0
c_bit:  db 1,2,4,8,16,32,64,128
c_key:  ds 64
        align 64
c_zero: ds 64
c_tmp:  ds 64
; p_hi, p_lo: SMS colour (--BBGGRR) -> the two NextReg $44 bytes (the runtime's pal_hi_table
; and pal_lo_table)
        align 128
p_hi:   db $00,$60,$A0,$E0,$0C,$6C,$AC,$EC,$14,$74,$B4,$F4,$1C,$7C,$BC,$FC
        db $01,$61,$A1,$E1,$0D,$6D,$AD,$ED,$15,$75,$B5,$F5,$1D,$7D,$BD,$FD
        db $02,$62,$A2,$E2,$0E,$6E,$AE,$EE,$16,$76,$B6,$F6,$1E,$7E,$BE,$FE
        db $03,$63,$A3,$E3,$0F,$6F,$AF,$EF,$17,$77,$B7,$F7,$1F,$7F,$BF,$FF
p_lo:   db $00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00,$00
        db $01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01
        db $01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01
        db $01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01
        align 256
c_dat:  ds 2048
endpage
# Page 2: the state of page 1's Layer 2 (D_ names there), mapped at $8000 while page 1 runs. The
# loader fills it with zeros.
page 2 d_none
d_none: ret
endpage

# Sonic The Hedgehog 2 (Europe, Brazil).cht, "Infinite Lives"
poke "Infinite lives"
ar 00D2-9809
endpoke

# Sonic The Hedgehog 2 (Europe, Brazil).cht, "Score 999000 For Every Act And Unlimited Timer"
poke "Infinite time"
ar 00D2-B9FF
endpoke

# Sonic The Hedgehog 2 (Europe, Brazil).cht, "Level Select Zone"
poke "Zone"
ar 00D2-95??
endpoke

# Sonic The Hedgehog 2 (Europe, Brazil).cht, "Invulnerability"
poke "Invulnerability"
ar 00D3-A972
endpoke

# Sonic The Hedgehog 2 (Europe, Brazil).cht, "Always Have Invincibility"
poke "Invincibility"
ar 00D5-3202
endpoke

# Sonic The Hedgehog 2 (Europe, Brazil).cht, "Start with ?? Lives, instead of 3"
poke "Start lives"
gg ??2-5CD-E66
endpoke

# Sonic The Hedgehog 2 (Europe, Brazil).cht, "Start with some Rings most of the Time"
poke "Start with rings"
gg 222-92D-2A2
endpoke

# Sonic The Hedgehog 2 (Europe, Brazil).cht, "Don't Lose Rings when Hit"
poke "Keep rings when hit"
gg 3A7-DFC-2A2
endpoke
