# Sensible Soccer (Europe), CRC32 F8176918, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs.
# Decisions:
# - $1BA38 (D3 A5, bank 6 $BA38) is not patched. It is inside the compressed pitch
#   tiles that the decoder at $78EF reads from $BA30 at every match start ($0154).
#   A patch there changes the data and every pitch tile after it comes out wrong.
#   One recording ran it as code once, through a stray jump.
# - $0211 (VDP register 0, then on into $021A) and $0DD0 (VDP register 9) are whole
#   routines that no scanned path or recording reaches; their sites are patched.
name Sensible Soccer
cart F8176918
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
asm 00091 2   ; IM 1 -> IM 2
    im 2
endasm
site 0000E   ; OUT ($3E),A
site 0003C   ; IN A,($BF)
site 0009A   ; OTIR
site 000FB   ; OUT ($BF),A
site 000FF   ; OUT ($BF),A
site 00104   ; OUT ($BE),A
site 00114   ; OUT ($BF),A
site 0011A   ; OUT ($BF),A
site 0011D   ; OUT ($BE),A
site 00120   ; OUT ($BE),A
site 00143   ; OUT ($BF),A
site 00148   ; OUT ($BF),A
site 0014E   ; OUT ($BE),A
site 001CB   ; OUT ($BF),A
site 001D0   ; OUT ($BF),A
site 001D6   ; OTIR
site 001DB   ; OUT ($BE),A
site 001E3   ; OTIR
site 001E8   ; OUT ($BE),A
site 001F7   ; OUT ($BF),A
site 001FD   ; OUT ($BF),A
site 00201   ; OUT ($BE),A
site 00213   ; OUT ($BF),A
site 00218   ; OUT ($BF),A
site 0021C   ; OUT ($BF),A
site 00221   ; OUT ($BF),A
site 00226   ; OUT ($BF),A
site 0022B   ; OUT ($BF),A
site 00232   ; OUT ($BF),A
site 00237   ; OUT ($BF),A
site 0023D   ; OUT ($BE),A
site 00255   ; IN A,($DC)
site 00267   ; IN A,($DD)
site 0033A   ; OUT ($BF),A
site 0033E   ; OUT ($BF),A
site 00342   ; OUT ($BE),A
site 0034D   ; OUT ($BF),A
site 00352   ; OUT ($BF),A
site 00356   ; OUT ($BE),A
site 004B9   ; OUT ($BF),A
site 004BE   ; OUT ($BF),A
site 004C2   ; OUT ($BF),A
site 004C7   ; OUT ($BF),A
site 00517   ; OUT ($BF),A
site 0051C   ; OUT ($BF),A
site 00520   ; OUT ($BF),A
site 00525   ; OUT ($BF),A
site 009ED   ; OUT ($BF),A
site 009F3   ; OUT ($BF),A
site 00A03   ; OUTI
site 00A05   ; OUTI
site 00A0C   ; OUT ($BF),A
site 00A12   ; OUT ($BF),A
site 00A22   ; OUTI
site 00A24   ; OUTI
site 00A2B   ; OUT ($BF),A
site 00A31   ; OUT ($BF),A
site 00A41   ; OUTI
site 00A43   ; OUTI
site 00A4A   ; OUT ($BF),A
site 00A50   ; OUT ($BF),A
site 00A60   ; OUTI
site 00A62   ; OUTI
site 00A69   ; OUT ($BF),A
site 00A6F   ; OUT ($BF),A
site 00A7F   ; OUTI
site 00A81   ; OUTI
site 00A88   ; OUT ($BF),A
site 00A8E   ; OUT ($BF),A
site 00A9E   ; OUTI
site 00AA0   ; OUTI
site 00AA7   ; OUT ($BF),A
site 00AAD   ; OUT ($BF),A
site 00ABD   ; OUTI
site 00ABF   ; OUTI
site 00AC6   ; OUT ($BF),A
site 00ACC   ; OUT ($BF),A
site 00ADC   ; OUTI
site 00ADE   ; OUTI
site 00AE5   ; OUT ($BF),A
site 00AEB   ; OUT ($BF),A
site 00AFB   ; OUTI
site 00AFD   ; OUTI
site 00B04   ; OUT ($BF),A
site 00B0A   ; OUT ($BF),A
site 00B1A   ; OUTI
site 00B1C   ; OUTI
site 00B23   ; OUT ($BF),A
site 00B29   ; OUT ($BF),A
site 00B39   ; OUTI
site 00B3B   ; OUTI
site 00B42   ; OUT ($BF),A
site 00B48   ; OUT ($BF),A
site 00B58   ; OUTI
site 00B5A   ; OUTI
site 00B61   ; OUT ($BF),A
site 00B67   ; OUT ($BF),A
site 00B77   ; OUTI
site 00B79   ; OUTI
site 00B80   ; OUT ($BF),A
site 00B86   ; OUT ($BF),A
site 00B96   ; OUTI
site 00B98   ; OUTI
site 00B9F   ; OUT ($BF),A
site 00BA5   ; OUT ($BF),A
site 00BB5   ; OUTI
site 00BB7   ; OUTI
site 00BBE   ; OUT ($BF),A
site 00BC4   ; OUT ($BF),A
site 00BD4   ; OUTI
site 00BD6   ; OUTI
site 00BDD   ; OUT ($BF),A
site 00BE3   ; OUT ($BF),A
site 00BF3   ; OUTI
site 00BF5   ; OUTI
site 00BFC   ; OUT ($BF),A
site 00C02   ; OUT ($BF),A
site 00C12   ; OUTI
site 00C14   ; OUTI
site 00C1B   ; OUT ($BF),A
site 00C21   ; OUT ($BF),A
site 00C31   ; OUTI
site 00C33   ; OUTI
site 00C3A   ; OUT ($BF),A
site 00C40   ; OUT ($BF),A
site 00C50   ; OUTI
site 00C52   ; OUTI
site 00C59   ; OUT ($BF),A
site 00C5F   ; OUT ($BF),A
site 00C6F   ; OUTI
site 00C71   ; OUTI
site 00C78   ; OUT ($BF),A
site 00C7E   ; OUT ($BF),A
site 00C8E   ; OUTI
site 00C90   ; OUTI
site 00C97   ; OUT ($BF),A
site 00C9D   ; OUT ($BF),A
site 00CAD   ; OUTI
site 00CAF   ; OUTI
site 00CB6   ; OUT ($BF),A
site 00CBC   ; OUT ($BF),A
site 00CCC   ; OUTI
site 00CCE   ; OUTI
site 00CD5   ; OUT ($BF),A
site 00CDB   ; OUT ($BF),A
site 00CEB   ; OUTI
site 00CED   ; OUTI
site 00CF4   ; OUT ($BF),A
site 00CFA   ; OUT ($BF),A
site 00D0A   ; OUTI
site 00D0C   ; OUTI
site 00D13   ; OUT ($BF),A
site 00D19   ; OUT ($BF),A
site 00D29   ; OUTI
site 00D2B   ; OUTI
site 00D32   ; OUT ($BF),A
site 00D38   ; OUT ($BF),A
site 00D48   ; OUTI
site 00D4A   ; OUTI
site 00D69   ; OUT ($BF),A
site 00D6C   ; OUT ($BF),A
site 00D78   ; OTIR
site 00D7D   ; OUT ($BF),A
site 00D80   ; OUT ($BF),A
site 00D86   ; OTIR
site 00D8C   ; OUT ($BF),A
site 00D90   ; OUT ($BF),A
site 00D9F   ; OUT ($BF),A
site 00DA3   ; OUT ($BF),A
site 00DD3   ; OUT ($BF),A
site 00DD7   ; OUT ($BF),A
site 01059   ; OUT ($BF),A
site 0105D   ; OUT ($BF),A
site 01071   ; OUT ($BE),A
site 01078   ; OUT ($BE),A
site 0107C   ; OUT ($BF),A
site 01080   ; OUT ($BF),A
site 0108F   ; OUT ($BE),A
site 01094   ; OUT ($BE),A
site 0109C   ; OUT ($BE),A
site 010D4   ; OUT ($BF),A
site 010D9   ; OUT ($BF),A
site 010DE   ; OTIR
site 05377   ; OUT ($BF),A
site 0537B   ; OUT ($BF),A
site 05387   ; OUT ($BE),A
site 068DA   ; OUT ($BF),A
site 068DE   ; OUT ($BF),A
site 068F3   ; OTIR
site 068F7   ; OUT ($BF),A
site 068FB   ; OUT ($BF),A
site 06914   ; OTIR
site 06923   ; OUT ($BF),A
site 06927   ; OUT ($BF),A
site 0693F   ; OTIR
site 06943   ; OUT ($BF),A
site 06947   ; OUT ($BF),A
site 06956   ; OTIR
site 0695A   ; OUT ($BF),A
site 0695E   ; OUT ($BF),A
site 06973   ; OTIR
site 06977   ; OUT ($BF),A
site 0697B   ; OUT ($BF),A
site 0698A   ; OTIR
site 071E1   ; OUT ($BF),A
site 071E4   ; OUT ($BF),A
site 071F0   ; OTIR
site 071F5   ; OUT ($BF),A
site 071F8   ; OUT ($BF),A
site 071FE   ; OTIR
site 07317   ; OUT ($BF),A
site 0731C   ; OUT ($BF),A
site 07321   ; OUT ($BF),A
site 07326   ; OUT ($BF),A
site 07848   ; OUT ($BF),A
site 0784E   ; OUT ($BF),A
site 07866   ; OUT ($BF),A
site 0786C   ; OUT ($BF),A
site 07909   ; OUT ($BE),A
site 11AE1   ; OUT ($BF),A
site 11AE5   ; OUT ($BF),A
site 11AE8   ; OUT ($BF),A
site 11AEC   ; OUT ($BF),A
site 1276F   ; OUT ($BF),A
site 12773   ; OUT ($BF),A
site 1277E   ; OUT ($BE),A
site 12785   ; OUT ($BE),A
site 1278C   ; OUT ($BF),A
site 12790   ; OUT ($BF),A
site 12794   ; OUT ($BE),A
site 12798   ; OUT ($BE),A
site 1279E   ; OUT ($BE),A
site 127A2   ; OUT ($BE),A
site 127A9   ; OUT ($BE),A
site 127AD   ; OUT ($BE),A
site 127B2   ; OUT ($BF),A
site 127B6   ; OUT ($BF),A
site 127BA   ; OUT ($BE),A
site 127BD   ; OUT ($BE),A
site 127C1   ; OUT ($BE),A
site 127C5   ; OUT ($BF),A
site 127C9   ; OUT ($BF),A
site 127CD   ; OUT ($BE),A
site 127D1   ; OUT ($BE),A
site 127D4   ; OUT ($BE),A
site 127D8   ; OUT ($BE),A
site 137D5   ; OUT ($BF),A
site 137D9   ; OUT ($BF),A
site 137EA   ; OUT ($BE),A
site 14079   ; OUT ($7F),A
site 14080   ; OUT ($7F),A
site 14087   ; OUT ($7F),A
site 1408E   ; OUT ($7F),A
site 14260   ; OTIR
site 1426C   ; OUT ($7F),A
site 1F878   ; OUT ($BF),A
site 1F87C   ; OUT ($BF),A
site 1F87F   ; OUT ($BF),A
site 1F883   ; OUT ($BF),A
site 1F887   ; OUT ($BF),A
site 1F88B   ; OUT ($BF),A
site 1F8D3   ; OUT ($BF),A
site 1F8D7   ; OUT ($BF),A
site 1F8DA   ; OUT ($BF),A
site 1F8DE   ; OUT ($BF),A
site 1F8E2   ; OUT ($BF),A
site 1F8E6   ; OUT ($BF),A
site 1F921   ; OUT ($BF),A
site 1F927   ; OUT ($BF),A
site 1F92F   ; OUT ($BE),A
site 1F933   ; OUT ($BE),A
site 1F942   ; OUT ($BF),A
site 1F946   ; OUT ($BF),A
site 1F949   ; OUT ($BF),A
site 1F94D   ; OUT ($BF),A
site 1F951   ; OUT ($BF),A
site 1F955   ; OUT ($BF),A
site 1F990   ; OUT ($BF),A
site 1F994   ; OUT ($BF),A
site 1F997   ; OUT ($BF),A
site 1F99B   ; OUT ($BF),A
mapst 0009E   ; LD ($FFFF),A
mapst 000B9   ; LD ($FFFF),A
mapst 000C6   ; LD ($FFFF),A
mapst 000DC   ; LD ($FFFF),A
mapst 000EA   ; LD ($FFFF),A
mapst 001A9   ; LD ($FFFF),A
mapst 001AF   ; LD ($FFFF),A
mapst 001ED   ; LD ($FFFF),A
mapst 0020D   ; LD ($FFFF),A
mapst 002DE   ; LD ($FFFF),A
mapst 003CB   ; LD ($FFFF),A
mapst 003DD   ; LD ($FFFF),A
mapst 003F6   ; LD ($FFFF),A
mapst 003FE   ; LD ($FFFF),A
mapst 0040C   ; LD ($FFFF),A
mapst 00419   ; LD ($FFFF),A
mapst 00461   ; LD ($FFFF),A
mapst 00469   ; LD ($FFFF),A
mapst 00472   ; LD ($FFFF),A
mapst 004D1   ; LD ($FFFF),A
mapst 004E7   ; LD ($FFFF),A
mapst 004F1   ; LD ($FFFF),A
mapst 004FA   ; LD ($FFFF),A
mapst 0052F   ; LD ($FFFF),A
mapst 0053A   ; LD ($FFFF),A
mapst 00552   ; LD ($FFFF),A
mapst 005B7   ; LD ($FFFF),A
mapst 00639   ; LD ($FFFF),A
mapst 00698   ; LD ($FFFF),A
mapst 00715   ; LD ($FFFF),A
mapst 00762   ; LD ($FFFF),A
mapst 009D3   ; LD ($FFFF),A
mapst 00D94   ; LD ($FFFF),A
mapst 00DA8   ; LD ($FFFF),A
mapst 010C7   ; LD ($FFFF),A
mapst 010E9   ; LD ($FFFF),A
mapst 056C1   ; LD ($FFFF),A
mapst 056C9   ; LD ($FFFF),A
mapst 068CC   ; LD ($FFFF),A
mapst 06993   ; LD ($FFFF),A
mapst 06B0E   ; LD ($FFFF),A
mapst 06B17   ; LD ($FFFF),A
mapst 06B3E   ; LD ($FFFF),A
mapst 06B47   ; LD ($FFFF),A
mapst 06F61   ; LD ($FFFF),A
mapst 06F88   ; LD ($FFFF),A
mapst 06F92   ; LD ($FFFF),A
mapst 06FA4   ; LD ($FFFF),A
mapst 06FEF   ; LD ($FFFF),A
mapst 07006   ; LD ($FFFF),A
mapst 0783E   ; LD ($FFFF),A
mapst 07857   ; LD ($FFFF),A
mapst 0785C   ; LD ($FFFF),A
mapst 0787A   ; LD ($FFFF),A
mapst 07886   ; LD ($FFFF),A
mapst 078AD   ; LD ($FFFF),A
mapst 078BC   ; LD ($FFFF),A
mapst 078CE   ; LD ($FFFF),A
mapst 078F7   ; LD ($FFFF),A
mapst 07923   ; LD ($FFFF),A
mapst 0792A   ; LD ($FFFF),A
mapst 0795D   ; LD ($FFFF),A
mapst 07964   ; LD ($FFFF),A
mapst 0797B   ; LD ($FFFF),A
mapst 07982   ; LD ($FFFF),A
mapst 07AC6   ; LD ($FFFF),A
mapst 07AFC   ; LD ($FFFF),A
mapst 07B31   ; LD ($FFFF),A
mapst 07B90   ; LD ($FFFF),A
mapst 07C20   ; LD ($FFFF),A
mapst 07CCB   ; LD ($FFFF),A
mapst 07CD5   ; LD ($FFFF),A
mapst 07CF5   ; LD ($FFFF),A
mapst 07CFD   ; LD ($FFFF),A
mapst 07D06   ; LD ($FFFF),A
mapst 07D25   ; LD ($FFFF),A
mapst 07D41   ; LD ($FFFF),A
# CHECK cartarea_store at 1A614 ($A614 bank 6): 02  LD (BC),A $0101
# CHECK cartarea_store at 1A744 ($A744 bank 6): 02  LD (BC),A $0101
# CHECK cartarea_store at 1A874 ($A874 bank 6): 02  LD (BC),A $0101
# CHECK cartarea_store at 1A9A4 ($A9A4 bank 6): 02  LD (BC),A $0101
# CHECK cartarea_store at 1AAD4 ($AAD4 bank 6): 02  LD (BC),A $0101
# CHECK cartarea_store at 1AC04 ($AC04 bank 6): 02  LD (BC),A $0101
# CHECK cartarea_store at 1AD74 ($AD74 bank 6): 02  LD (BC),A $0101
# CHECK cartarea_store at 1AE92 ($AE92 bank 6): 36 05  LD (HL),$05 $917B
# CHECK cartarea_store at 1AE94 ($AE94 bank 6): 02  LD (BC),A $0535
# CHECK cartarea_store at 1AEA6 ($AEA6 bank 6): 35  DEC (HL) $917B
# CHECK cartarea_store at 1AF1A ($AF1A bank 6): 32 05 32  LD ($3205),A $3205
# CHECK ram_exec at 121FC ($A1FC bank 4): C9  RET $C500
# CHECK ram_exec at 121FC ($A1FC bank 4): C9  RET $C555
# CHECK ram_exec at 12205 ($A205 bank 4): C9  RET $C500
# CHECK ram_exec at 12205 ($A205 bank 4): C9  RET $C555
# CHECK indirect_unresolved at 0004C ($004C bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 0005A ($005A bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 06B1A ($6B1A bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 06B4A ($6B4A bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 06C32 ($6C32 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 06C55 ($6C55 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 0726A ($726A bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 12503 ($A503 bank 4): E9  JP (HL) 
# CHECK indirect_unresolved at 14009 ($8009 bank 5): E9  JP (HL) 
# CHECK indirect_unresolved at 1FA19 ($BA19 bank 7): E9  JP (HL) 
# CHECK bank_unresolved at 000F6 ($00F6 bank 0): C3 F6 9A  JP $9AF6 $9AF6
# CHECK bank_unresolved at 00534 ($0534 bank 0): CD 00 80  CALL $8000 $8000
# CHECK bank_unresolved at 06F6F ($6F6F bank 1): CD 7C BE  CALL $BE7C $BE7C
# CHECK bank_unresolved at 07A69 ($7A69 bank 1): CD FB B7  CALL $B7FB $B7FB
# CHECK bank_unresolved at 07AAF ($7AAF bank 1): C3 E4 B4  JP $B4E4 $B4E4
# CHECK bank_unresolved at 07B07 ($7B07 bank 1): CD 8B 9E  CALL $9E8B $9E8B
# CHECK bank_unresolved at 07B3C ($7B3C bank 1): CD 8B 9E  CALL $9E8B $9E8B
# CHECK bank_unresolved at 07B40 ($7B40 bank 1): CD 3A AF  CALL $AF3A $AF3A
# CHECK bank_unresolved at 07B9E ($7B9E bank 1): CD 8B 9E  CALL $9E8B $9E8B
# CHECK bank_unresolved at 07BC8 ($7BC8 bank 1): CD 5D AF  CALL $AF5D $AF5D
# CHECK bank_unresolved at 07BE9 ($7BE9 bank 1): CD 5D AF  CALL $AF5D $AF5D
# CHECK bank_unresolved at 07F1F ($7F1F bank 1): CD C1 A0  CALL $A0C1 $A0C1
# CHECK bank_unresolved at 07F3B ($7F3B bank 1): CD C1 A0  CALL $A0C1 $A0C1
# CHECK high: site 00213  OUT ($BF),A  (vdp_control; after LD A,$B6; 32 bytes of valid code before it)
# CHECK high: site 00218  OUT ($BF),A  (vdp_control; after LD A,$80; 32 bytes of valid code before it)
# CHECK medium: site 00DD3  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 00DD7  OUT ($BF),A  (vdp_control; after LD A,$89; 32 bytes of valid code before it)
# CHECK low: site 0729A  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 072A5  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 072AA  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 072AF  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 072BA  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 072BF  OUT ($3E),A  (memory_control; no evidence)
# CHECK medium: site 072C4  OUT ($3E),A  (memory_control; branch target from $0B29D)
# CHECK low: site 072CF  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 072D4  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 072D9  OUT ($3E),A  (memory_control; no evidence)
# CHECK medium: site 072E4  OUT ($3E),A  (memory_control; branch target from $0AB5C)
# CHECK low: site 072E9  OUT ($3E),A  (memory_control; no evidence)
# CHECK medium: site 0A160  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 0A40B  IN A,($BF)  (vdp_status; no evidence)
# CHECK medium: site 0A70A  OUT (C),B  (port in C; 8 bytes of valid code before it)
# CHECK medium: site 0AD75  IN A,($7E)  (v_counter; 32 bytes of valid code before it)
# CHECK low: site 0BBE4  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 0BCC4  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 0BDA4  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 0FBB3  IN H,(C)  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 0FE7A  IN H,(C)  (port in C; 21 bytes of valid code before it; no valid code after it)
# CHECK medium: site 110ED  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK low: site 11275  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK medium: site 11913  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK low: site 1240B  OTDR  (port in C; no evidence)
# CHECK low: site 13B7A  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK medium: site 13F9C  OUT ($DC),A  (no_effect; 15 bytes of valid code before it)
# CHECK medium: site 13FC6  OUT ($DC),A  (no_effect; 8 bytes of valid code before it)
# CHECK medium: site 13FDA  OUT ($DC),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 13FF6  OUT ($DC),A  (no_effect; 32 bytes of valid code before it)
# CHECK low: site 140C9  IN A,($C0)  (joypad_a; no evidence)
# CHECK low: site 14147  IN A,($C0)  (joypad_a; no evidence)
# CHECK medium: site 1618E  OUT ($C1),A  (no_effect; 10 bytes of valid code before it)
# CHECK medium: site 16500  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 16645  OUT ($DC),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 1702B  INDR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 170A3  OUT ($DD),A  (no_effect; 26 bytes of valid code before it)
# CHECK low: site 17529  OUT (C),C  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 1785D  OUT ($7E),A  (psg; branch target from $1742C; 32 bytes of valid code before it)
# CHECK low: site 1BAFB  OTIR  (port in C; no evidence)
# CHECK low: site 1BB05  OTIR  (port in C; no evidence)
# CHECK medium: site 1BD9F  INIR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 1BDB8  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK low: site 1C828  OUT ($BF),A  (vdp_control; no evidence)
# CHECK medium: site 1C8C6  OUT ($F1),A  (fm_data; 19 bytes of valid code before it)
# CHECK low: site 1CD2D  OUT ($BD),A  (vdp_control; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 1E388  IN A,($7F)  (h_counter; 8 bytes of valid code before it)
# CHECK medium: site 1E5A7  OUT ($BD),A  (vdp_control; 32 bytes of valid code before it)
# CHECK low: site 1E5CA  OUT ($BD),A  (vdp_control; no evidence)
# CHECK low: site 1E6F0  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 1E9DB  INIR  (port in C; no evidence)
# CHECK high: site 1ECA6  OUT ($DD),A  (no_effect; after LD A,($CA3B); 32 bytes of valid code before it)
# CHECK medium: site 1EFF8  INDR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 1F265  IN A,($3E)  (unmapped_read; 32 bytes of valid code before it)
# CHECK low: site 1F34B  IN A,($3E)  (unmapped_read; no evidence)

# Sensible Soccer (Europe).cht and Sensible Soccer (Europe) (Action Replay).cht,
# "Team 1/P1 Always Scores 99 (Left On Scoreboard)": RAM $C532 is the left score on the
# scoreboard, the home team (player 1)
poke "P1 scores 99"
ar 00C5-3263
endpoke

# Sensible Soccer (Europe).cht and Sensible Soccer (Europe) (Action Replay).cht,
# "Team 2/CPU Never Scores (Right On Scoreboard)": RAM $C587 is the right score on the
# scoreboard, the away team (CPU)
poke "CPU never scores"
ar 00C5-8700
endpoke
