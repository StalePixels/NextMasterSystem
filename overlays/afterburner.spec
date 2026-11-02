# After Burner (World), CRC32 1C951F8E, 512K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log.
# The game checks the region at $08AF (port $3F, then $DD) and looks for the FM unit at $08DA
# (port $F2); compare it with a reference forced to the export path and with no FM unit.
# The frame handler at $0119 runs the game's states ($C001); the main loop runs the state's
# routine once after each handler. No line interrupts, no H scroll, V scroll in the handler.
# Spec gaps (data/scan-verdicts.tsv): unused are the VDP library routines $0997-$0A47, which
# nothing names; false are byte patterns in table data in bank 1 and graphics in bank 27.
name After Burner
cart 1C951F8E
hz any		; No-Intro regions World
vector 18 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
# One-frame waits in screen changes (EI; HALT): the runtime's own interrupts end a native HALT.
# The HALTs at $0633 and $0670 wait in loops on $C001, which the frame handler sets: no patch.
eihalt 023CE
eihalt 023EF
eihalt 03612
eihalt 06119
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
site 00123   ; IN A,($BF)
site 00125   ; IN A,($DD)
site 00227   ; OUT ($BE),A
site 0022E   ; OUT ($BE),A
site 004E3   ; OUT ($BF),A
site 004E6   ; OUT ($BF),A
otir 004EB   ; OUTI
site 00501   ; OUT ($BF),A
site 00504   ; OUT ($BF),A
otir 00509   ; OUTI
site 0053E   ; OUT ($BF),A
site 00542   ; OUT ($BF),A
site 00545   ; OUT ($BF),A
site 00549   ; OUT ($BF),A
site 0074B   ; OUT ($BF),A
site 00757   ; OUT ($BF),A
site 00786   ; OUT ($BF),A
site 00792   ; OUT ($BF),A
site 007C9   ; OUT ($BF),A
site 007D5   ; OUT ($BF),A
otir 007DD   ; OUTI
site 007E4   ; OUT ($BF),A
site 007F0   ; OUT ($BF),A
otir 007F7   ; OUTI
site 0081C   ; OUT ($BF),A
site 00820   ; OUT ($BF),A
site 00823   ; OUT ($BF),A
site 00827   ; OUT ($BF),A
site 00843   ; OUT ($BF),A
site 00847   ; OUT ($BF),A
site 00872   ; OUT ($BF),A
site 00876   ; OUT ($BF),A
site 00881   ; OUT (C),A
site 008B1   ; OUT ($3F),A
site 008B3   ; IN A,($DD)
site 008BD   ; OUT ($3F),A
site 008BF   ; IN A,($DD)
site 008C8   ; OUT ($3F),A
site 008DF   ; OUT ($3E),A
site 008E7   ; OUT ($F2),A
site 008EA   ; IN A,($F2)
site 008FC   ; OUT ($F2),A
site 00904   ; OUT ($3E),A
site 00912   ; IN A,($DC)
site 00945   ; OTIR
site 0098A   ; OUT ($BE),A
site 0098F   ; OUT ($BE),A
site 009B2   ; OUT ($BE),A
site 009E2   ; OUTI
site 009E9   ; OUT (C),A
site 009FF   ; OUTI
site 00A26   ; OUT (C),D
site 00A62   ; OUT ($BE),A
site 00A91   ; OUT ($BE),A
site 00AD8   ; OUTI
site 00ADA   ; OUTI
site 00ADC   ; OUTI
site 00ADE   ; OUTI
site 00AE0   ; OUTI
site 00AE2   ; OUTI
site 00AE4   ; OUTI
site 00AE6   ; OUTI
site 00AE8   ; OUTI
site 00AEA   ; OUTI
site 00AEC   ; OUTI
site 00AEE   ; OUTI
site 00AF0   ; OUTI
site 00AF2   ; OUTI
site 00AF4   ; OUTI
site 00AF6   ; OUTI
site 00AF8   ; OUTI
site 00AFA   ; OUTI
site 00AFC   ; OUTI
site 00AFE   ; OUTI
site 00B00   ; OUTI
site 00B02   ; OUTI
site 00B04   ; OUTI
site 00B06   ; OUTI
site 00B08   ; OUTI
site 00B0A   ; OUTI
site 00B0C   ; OUTI
site 00B0E   ; OUTI
site 00B10   ; OUTI
site 00B12   ; OUTI
site 00B14   ; OUTI
site 00B16   ; OUTI
site 00B18   ; OUTI
site 00B1A   ; OUTI
site 00B1C   ; OUTI
site 00B1E   ; OUTI
site 00B20   ; OUTI
site 00B22   ; OUTI
site 00B24   ; OUTI
site 00B26   ; OUTI
site 00B28   ; OUTI
site 00B2A   ; OUTI
site 00B2C   ; OUTI
site 00B2E   ; OUTI
site 00B30   ; OUTI
site 00B32   ; OUTI
site 00B34   ; OUTI
site 00B36   ; OUTI
site 00B38   ; OUTI
site 00B3A   ; OUTI
site 00B3C   ; OUTI
site 00B3E   ; OUTI
site 00B40   ; OUTI
site 00B42   ; OUTI
site 00B44   ; OUTI
site 00B46   ; OUTI
site 00B48   ; OUTI
site 00B4A   ; OUTI
site 00B4C   ; OUTI
site 00B4E   ; OUTI
site 00B50   ; OUTI
site 00B52   ; OUTI
site 00B54   ; OUTI
site 00B56   ; OUTI
site 00B58   ; OUTI
site 00B5A   ; OUTI
site 00B5C   ; OUTI
site 00B5E   ; OUTI
site 00B60   ; OUTI
site 00B62   ; OUTI
site 00B64   ; OUTI
site 00B66   ; OUTI
site 00B68   ; OUTI
site 00B6A   ; OUTI
site 00B6C   ; OUTI
site 00B6E   ; OUTI
site 00B70   ; OUTI
site 00B72   ; OUTI
site 00B74   ; OUTI
site 00B76   ; OUTI
site 00B78   ; OUTI
site 00B7A   ; OUTI
site 00B7C   ; OUTI
site 00B7E   ; OUTI
site 00B80   ; OUTI
site 00B82   ; OUTI
site 00B84   ; OUTI
site 00B86   ; OUTI
site 00B88   ; OUTI
site 00B8A   ; OUTI
site 00B8C   ; OUTI
site 00B8E   ; OUTI
site 00B90   ; OUTI
site 00B92   ; OUTI
site 00B94   ; OUTI
site 00B96   ; OUTI
site 00B98   ; OUTI
site 00B9A   ; OUTI
site 00B9C   ; OUTI
site 00B9E   ; OUTI
site 00BA0   ; OUTI
site 00BA2   ; OUTI
site 00BA4   ; OUTI
site 00BA6   ; OUTI
site 00BA8   ; OUTI
site 00BAA   ; OUTI
site 00BAC   ; OUTI
site 00BAE   ; OUTI
site 00BB0   ; OUTI
site 00BB2   ; OUTI
site 00BB4   ; OUTI
site 00BB6   ; OUTI
site 00BB8   ; OUTI
site 00BBA   ; OUTI
site 00BBC   ; OUTI
site 00BBE   ; OUTI
site 00BC0   ; OUTI
site 00BC2   ; OUTI
site 00BC4   ; OUTI
site 00BC6   ; OUTI
site 00BC8   ; OUTI
site 00BCA   ; OUTI
site 00BCC   ; OUTI
site 00BCE   ; OUTI
site 00BD0   ; OUTI
site 00BD2   ; OUTI
site 00BD4   ; OUTI
site 00BD6   ; OUTI
site 00BD8   ; OUTI
site 00BDA   ; OUTI
site 00BDC   ; OUTI
site 00BDE   ; OUTI
site 00BE0   ; OUTI
site 00BE2   ; OUTI
site 00BE4   ; OUTI
site 00BE6   ; OUTI
site 00BE8   ; OUTI
site 00BEA   ; OUTI
site 00BEC   ; OUTI
site 00BEE   ; OUTI
site 00BF0   ; OUTI
site 00BF2   ; OUTI
site 00BF4   ; OUTI
site 00BF6   ; OUTI
site 00BF8   ; OUTI
site 00BFA   ; OUTI
site 00BFC   ; OUTI
site 00BFE   ; OUTI
site 00C00   ; OUTI
site 00C02   ; OUTI
site 00C04   ; OUTI
site 00C06   ; OUTI
site 00C08   ; OUTI
site 00C0A   ; OUTI
site 00C0C   ; OUTI
site 00C0E   ; OUTI
site 00C10   ; OUTI
site 00C12   ; OUTI
site 00C14   ; OUTI
site 00C16   ; OUTI
site 00C18   ; OUTI
site 00C1A   ; OUTI
site 00C1C   ; OUTI
site 00C1E   ; OUTI
site 00C20   ; OUTI
site 00C22   ; OUTI
site 00C24   ; OUTI
site 00C26   ; OUTI
site 00C28   ; OUTI
site 00C2A   ; OUTI
site 00C2C   ; OUTI
site 00C2E   ; OUTI
site 00C30   ; OUTI
site 00C32   ; OUTI
site 00C34   ; OUTI
site 00C36   ; OUTI
site 00C38   ; OUTI
site 00C3A   ; OUTI
site 00C3C   ; OUTI
site 00C3E   ; OUTI
site 00C40   ; OUTI
site 00C42   ; OUTI
site 00C44   ; OUTI
site 00C46   ; OUTI
site 00C48   ; OUTI
site 00C4A   ; OUTI
site 00C4C   ; OUTI
site 00C4E   ; OUTI
site 00C50   ; OUTI
site 00C52   ; OUTI
site 00C54   ; OUTI
site 00C56   ; OUTI
site 00C58   ; OUTI
site 00C5A   ; OUTI
site 00C5C   ; OUTI
site 00C5E   ; OUTI
site 00C60   ; OUTI
site 00C62   ; OUTI
site 00C64   ; OUTI
site 00C66   ; OUTI
site 00C68   ; OUTI
site 00C6A   ; OUTI
site 00C6C   ; OUTI
site 00C6E   ; OUTI
site 00C70   ; OUTI
site 00C72   ; OUTI
site 00C74   ; OUTI
site 00C76   ; OUTI
site 00C78   ; OUTI
site 00C7A   ; OUTI
site 00C7C   ; OUTI
site 00C7E   ; OUTI
site 00C80   ; OUTI
site 00C82   ; OUTI
site 00C84   ; OUTI
site 00C86   ; OUTI
site 00C88   ; OUTI
site 00C8A   ; OUTI
site 00C8C   ; OUTI
site 00C8E   ; OUTI
site 00C90   ; OUTI
site 00C92   ; OUTI
site 00C94   ; OUTI
site 00C96   ; OUTI
site 00C98   ; OUTI
site 00C9A   ; OUTI
site 00C9C   ; OUTI
site 00C9E   ; OUTI
site 00CA0   ; OUTI
site 00CA2   ; OUTI
site 00CA4   ; OUTI
site 00CA6   ; OUTI
site 00CA8   ; OUTI
site 00CAA   ; OUTI
site 00CAC   ; OUTI
site 00CAE   ; OUTI
site 00CB0   ; OUTI
site 00CB2   ; OUTI
site 00CB4   ; OUTI
site 00CB6   ; OUTI
site 00CB8   ; OUTI
site 00CBA   ; OUTI
site 00CBC   ; OUTI
site 00CBE   ; OUTI
site 00CC0   ; OUTI
site 00CC2   ; OUTI
site 00CC4   ; OUTI
site 00CC6   ; OUTI
site 00CC8   ; OUTI
site 00CCA   ; OUTI
site 00CCC   ; OUTI
site 00CCE   ; OUTI
site 00CD0   ; OUTI
site 00CD2   ; OUTI
site 00CD4   ; OUTI
site 00CD6   ; OUTI
site 00CD8   ; OUTI
site 00CDA   ; OUTI
site 00CDC   ; OUTI
site 00CDE   ; OUTI
site 00CE0   ; OUTI
site 00CE2   ; OUTI
site 00CE4   ; OUTI
site 00CE6   ; OUTI
site 00CE8   ; OUTI
site 00CEA   ; OUTI
site 00CEC   ; OUTI
site 00CEE   ; OUTI
site 00CF0   ; OUTI
site 00CF2   ; OUTI
site 00CF4   ; OUTI
site 00CF6   ; OUTI
site 00CF8   ; OUTI
site 00CFA   ; OUTI
site 00CFC   ; OUTI
site 00CFE   ; OUTI
site 00D00   ; OUTI
site 00D02   ; OUTI
site 00D04   ; OUTI
site 00D06   ; OUTI
site 00D08   ; OUTI
site 00D0A   ; OUTI
site 00D0C   ; OUTI
site 00D0E   ; OUTI
site 00D10   ; OUTI
site 00D12   ; OUTI
site 00D14   ; OUTI
site 00D16   ; OUTI
site 00D18   ; OUTI
site 00D1A   ; OUTI
site 00D1C   ; OUTI
site 00D1E   ; OUTI
site 00D20   ; OUTI
site 00D22   ; OUTI
site 00D24   ; OUTI
site 00D26   ; OUTI
site 00D28   ; OUTI
site 00D2A   ; OUTI
site 00D2C   ; OUTI
site 00D2E   ; OUTI
site 00D30   ; OUTI
site 00D32   ; OUTI
site 00D34   ; OUTI
site 00D36   ; OUTI
site 00D38   ; OUTI
site 00D3A   ; OUTI
site 00D3C   ; OUTI
site 00D3E   ; OUTI
site 00D40   ; OUTI
site 00D42   ; OUTI
site 00D44   ; OUTI
site 00D46   ; OUTI
site 00D48   ; OUTI
site 00D4A   ; OUTI
site 00D4C   ; OUTI
site 00D4E   ; OUTI
site 00D50   ; OUTI
site 00D52   ; OUTI
site 00D54   ; OUTI
site 00D56   ; OUTI
site 00D58   ; OUTI
site 00D5A   ; OUTI
site 00D5C   ; OUTI
site 00D5E   ; OUTI
site 00D60   ; OUTI
site 00D62   ; OUTI
site 00D64   ; OUTI
site 00D66   ; OUTI
site 00D68   ; OUTI
site 00D6A   ; OUTI
site 00D6C   ; OUTI
site 00D6E   ; OUTI
site 00D70   ; OUTI
site 00D72   ; OUTI
site 00D74   ; OUTI
site 00D76   ; OUTI
site 00D78   ; OUTI
site 00D7A   ; OUTI
site 00D7C   ; OUTI
site 00D7E   ; OUTI
site 00D80   ; OUTI
site 00D82   ; OUTI
site 00D84   ; OUTI
site 00D86   ; OUTI
site 00D88   ; OUTI
site 00D8A   ; OUTI
site 00D8C   ; OUTI
site 00D8E   ; OUTI
site 00D90   ; OUTI
site 00D92   ; OUTI
site 00D94   ; OUTI
site 00D96   ; OUTI
site 00D98   ; OUTI
site 00D9A   ; OUTI
site 00D9C   ; OUTI
site 00D9E   ; OUTI
site 00DA0   ; OUTI
site 00DA2   ; OUTI
site 00DA4   ; OUTI
site 00DA6   ; OUTI
site 00DA8   ; OUTI
site 00DAA   ; OUTI
site 00DAC   ; OUTI
site 00DAE   ; OUTI
site 00DB0   ; OUTI
site 00DB2   ; OUTI
site 00DB4   ; OUTI
site 00DB6   ; OUTI
site 00DB8   ; OUTI
site 00DBA   ; OUTI
site 00DBC   ; OUTI
site 00DBE   ; OUTI
site 00DC0   ; OUTI
site 00DC2   ; OUTI
site 00DC4   ; OUTI
site 00DC6   ; OUTI
site 00DC8   ; OUTI
site 00DCA   ; OUTI
site 00DCC   ; OUTI
site 00DCE   ; OUTI
site 00DD0   ; OUTI
site 00DD2   ; OUTI
site 00DD4   ; OUTI
site 00DD6   ; OUTI
site 00DD8   ; OUTI
site 00DDA   ; OUTI
site 00DDC   ; OUTI
site 00DDE   ; OUTI
site 00DE0   ; OUTI
site 00DE2   ; OUTI
site 00DE4   ; OUTI
site 00DE6   ; OUTI
site 00DE8   ; OUTI
site 00DEA   ; OUTI
site 00DEC   ; OUTI
site 00DEE   ; OUTI
site 00DF0   ; OUTI
site 00DF2   ; OUTI
site 00DF4   ; OUTI
site 00DF6   ; OUTI
site 00DF8   ; OUTI
site 00DFA   ; OUTI
site 00DFC   ; OUTI
site 00DFE   ; OUTI
site 00E00   ; OUTI
site 00E02   ; OUTI
site 00E04   ; OUTI
site 00E06   ; OUTI
site 00E08   ; OUTI
site 00E0A   ; OUTI
site 00E0C   ; OUTI
site 00E0E   ; OUTI
site 00E10   ; OUTI
site 00E12   ; OUTI
site 00E14   ; OUTI
site 00E16   ; OUTI
site 00E18   ; OUTI
site 00E1A   ; OUTI
site 00E1C   ; OUTI
site 00E1E   ; OUTI
site 00E20   ; OUTI
site 00E22   ; OUTI
site 00E24   ; OUTI
site 00E26   ; OUTI
site 00E28   ; OUTI
site 00E2A   ; OUTI
site 00E2C   ; OUTI
site 00E2E   ; OUTI
site 00E30   ; OUTI
site 00E32   ; OUTI
site 00E34   ; OUTI
site 00E36   ; OUTI
site 00E38   ; OUTI
site 00E3A   ; OUTI
site 00E3C   ; OUTI
site 00E3E   ; OUTI
site 00E40   ; OUTI
site 00E42   ; OUTI
site 00E44   ; OUTI
site 00E46   ; OUTI
site 00E48   ; OUTI
site 00E4A   ; OUTI
site 00E4C   ; OUTI
site 00E4E   ; OUTI
site 00E50   ; OUTI
site 00E52   ; OUTI
site 00E54   ; OUTI
site 00E56   ; OUTI
site 00E58   ; OUTI
site 00E5A   ; OUTI
site 00E5C   ; OUTI
site 00E5E   ; OUTI
site 00E60   ; OUTI
site 00E62   ; OUTI
site 00E64   ; OUTI
site 00E66   ; OUTI
site 00E68   ; OUTI
site 00E6A   ; OUTI
site 00E6C   ; OUTI
site 00E6E   ; OUTI
site 00E70   ; OUTI
site 00E72   ; OUTI
site 00E74   ; OUTI
site 00E76   ; OUTI
site 00E78   ; OUTI
site 00E7A   ; OUTI
site 00E7C   ; OUTI
site 00E7E   ; OUTI
site 00E80   ; OUTI
site 00E82   ; OUTI
site 00E84   ; OUTI
site 00E86   ; OUTI
site 00E88   ; OUTI
site 00E8A   ; OUTI
site 00E8C   ; OUTI
site 00E8E   ; OUTI
site 00E90   ; OUTI
site 00E92   ; OUTI
site 00E94   ; OUTI
site 00E96   ; OUTI
site 00E98   ; OUTI
site 00E9A   ; OUTI
site 00E9C   ; OUTI
site 00E9E   ; OUTI
site 00EA0   ; OUTI
site 00EA2   ; OUTI
site 00EA4   ; OUTI
site 00EA6   ; OUTI
site 00EA8   ; OUTI
site 00EAA   ; OUTI
site 00EAC   ; OUTI
site 00EAE   ; OUTI
site 00EB0   ; OUTI
site 00EB2   ; OUTI
site 00EB4   ; OUTI
site 00EB6   ; OUTI
site 00EB8   ; OUTI
site 00EBA   ; OUTI
site 00EBC   ; OUTI
site 00EBE   ; OUTI
site 00EC0   ; OUTI
site 00EC2   ; OUTI
site 00EC4   ; OUTI
site 00EC6   ; OUTI
site 00EC8   ; OUTI
site 00ECA   ; OUTI
site 00ECC   ; OUTI
site 00ECE   ; OUTI
site 00ED0   ; OUTI
site 00ED2   ; OUTI
site 00ED4   ; OUTI
site 00ED6   ; OUTI
site 00ED8   ; OUTI
site 00EDA   ; OUTI
site 00EDC   ; OUTI
site 00EDE   ; OUTI
site 00EE0   ; OUTI
site 00EE2   ; OUTI
site 00EE4   ; OUTI
site 00EE6   ; OUTI
site 00EE8   ; OUTI
site 00EEA   ; OUTI
site 00EEC   ; OUTI
site 00EEE   ; OUTI
site 00EF0   ; OUTI
site 00EF2   ; OUTI
site 00EF4   ; OUTI
site 00EF6   ; OUTI
site 00EF8   ; OUTI
site 00EFA   ; OUTI
site 00EFC   ; OUTI
site 00EFE   ; OUTI
site 00F00   ; OUTI
site 00F02   ; OUTI
site 00F04   ; OUTI
site 00F06   ; OUTI
site 00F08   ; OUTI
site 00F0A   ; OUTI
site 00F0C   ; OUTI
site 00F0E   ; OUTI
site 00F10   ; OUTI
site 00F12   ; OUTI
site 00F14   ; OUTI
site 00F16   ; OUTI
site 00F18   ; OUTI
site 00F1A   ; OUTI
site 00F1C   ; OUTI
site 00F1E   ; OUTI
site 00F20   ; OUTI
site 00F22   ; OUTI
site 00F24   ; OUTI
site 00F26   ; OUTI
site 00F28   ; OUTI
site 00F2A   ; OUTI
site 00F2C   ; OUTI
site 00F2E   ; OUTI
site 00F30   ; OUTI
site 00F32   ; OUTI
site 00F34   ; OUTI
site 00F36   ; OUTI
site 00F38   ; OUTI
site 00F3A   ; OUTI
site 00F3C   ; OUTI
site 00F3E   ; OUTI
site 00F40   ; OUTI
site 00F42   ; OUTI
site 00F44   ; OUTI
site 00F46   ; OUTI
site 00F48   ; OUTI
site 00F4A   ; OUTI
site 00F4C   ; OUTI
site 00F4E   ; OUTI
site 00F50   ; OUTI
site 00F52   ; OUTI
site 00F54   ; OUTI
site 00F56   ; OUTI
site 00F58   ; OUTI
site 00F5A   ; OUTI
site 00F5C   ; OUTI
site 00F5E   ; OUTI
site 00F60   ; OUTI
site 00F62   ; OUTI
site 00F64   ; OUTI
site 00F66   ; OUTI
site 00F68   ; OUTI
site 00F6A   ; OUTI
site 00F6C   ; OUTI
site 00F6E   ; OUTI
site 00F70   ; OUTI
site 00F72   ; OUTI
site 00F74   ; OUTI
site 00F76   ; OUTI
site 00F78   ; OUTI
site 00F7A   ; OUTI
site 00F7C   ; OUTI
site 00F7E   ; OUTI
site 00F80   ; OUTI
site 00F82   ; OUTI
site 00F84   ; OUTI
site 00F86   ; OUTI
site 00F88   ; OUTI
site 00F8A   ; OUTI
site 00F8C   ; OUTI
site 00F8E   ; OUTI
site 00F90   ; OUTI
site 00F92   ; OUTI
site 00F94   ; OUTI
site 00F96   ; OUTI
site 00F98   ; OUTI
site 00F9A   ; OUTI
site 00F9C   ; OUTI
site 00F9E   ; OUTI
site 00FA0   ; OUTI
site 00FA2   ; OUTI
site 00FA4   ; OUTI
site 00FA6   ; OUTI
site 00FA8   ; OUTI
site 00FAA   ; OUTI
site 00FAC   ; OUTI
site 00FAE   ; OUTI
site 00FB0   ; OUTI
site 00FB2   ; OUTI
site 00FB4   ; OUTI
site 00FB6   ; OUTI
site 00FB8   ; OUTI
site 00FBA   ; OUTI
site 00FBC   ; OUTI
site 00FBE   ; OUTI
site 00FC0   ; OUTI
site 00FC2   ; OUTI
site 00FC4   ; OUTI
site 00FC6   ; OUTI
site 00FC8   ; OUTI
site 00FCA   ; OUTI
site 00FCC   ; OUTI
site 00FCE   ; OUTI
site 00FD0   ; OUTI
site 00FD2   ; OUTI
site 00FD4   ; OUTI
site 00FD6   ; OUTI
site 00FD8   ; OUTI
site 00FDA   ; OUTI
site 00FDC   ; OUTI
site 00FDE   ; OUTI
site 00FE0   ; OUTI
site 00FE2   ; OUTI
site 00FE4   ; OUTI
site 00FE6   ; OUTI
site 00FE8   ; OUTI
site 00FEA   ; OUTI
site 00FEC   ; OUTI
site 00FEE   ; OUTI
site 00FF0   ; OUTI
site 00FF2   ; OUTI
site 00FF4   ; OUTI
site 00FF6   ; OUTI
site 00FF8   ; OUTI
site 00FFA   ; OUTI
site 00FFC   ; OUTI
site 00FFE   ; OUTI
site 01000   ; OUTI
site 01002   ; OUTI
site 01004   ; OUTI
site 01006   ; OUTI
site 01008   ; OUTI
site 0100A   ; OUTI
site 0100C   ; OUTI
site 0100E   ; OUTI
site 01010   ; OUTI
site 01012   ; OUTI
site 01014   ; OUTI
site 01016   ; OUTI
site 01018   ; OUTI
site 0101A   ; OUTI
site 0101C   ; OUTI
site 0101E   ; OUTI
site 01020   ; OUTI
site 01022   ; OUTI
site 01024   ; OUTI
site 01026   ; OUTI
site 01028   ; OUTI
site 0102A   ; OUTI
site 0102C   ; OUTI
site 0102E   ; OUTI
site 01030   ; OUTI
site 01032   ; OUTI
site 01034   ; OUTI
site 01036   ; OUTI
site 01038   ; OUTI
site 0103A   ; OUTI
site 0103C   ; OUTI
site 0103E   ; OUTI
site 01040   ; OUTI
site 01042   ; OUTI
site 01044   ; OUTI
site 01046   ; OUTI
site 01048   ; OUTI
site 0104A   ; OUTI
site 0104C   ; OUTI
site 0104E   ; OUTI
site 01050   ; OUTI
site 01052   ; OUTI
site 01054   ; OUTI
site 01056   ; OUTI
site 01058   ; OUTI
site 0105A   ; OUTI
site 0105C   ; OUTI
site 0105E   ; OUTI
site 01060   ; OUTI
site 01062   ; OUTI
site 01064   ; OUTI
site 01066   ; OUTI
site 01068   ; OUTI
site 0106A   ; OUTI
site 0106C   ; OUTI
site 0106E   ; OUTI
site 01070   ; OUTI
site 01072   ; OUTI
site 01074   ; OUTI
site 01076   ; OUTI
site 01078   ; OUTI
site 0107A   ; OUTI
site 0107C   ; OUTI
site 0107E   ; OUTI
site 01080   ; OUTI
site 01082   ; OUTI
site 01084   ; OUTI
site 01086   ; OUTI
site 01088   ; OUTI
site 0108A   ; OUTI
site 0108C   ; OUTI
site 0108E   ; OUTI
site 01090   ; OUTI
site 01092   ; OUTI
site 01094   ; OUTI
site 01096   ; OUTI
site 01098   ; OUTI
site 0109A   ; OUTI
site 0109C   ; OUTI
site 0109E   ; OUTI
site 010A0   ; OUTI
site 010A2   ; OUTI
site 010A4   ; OUTI
site 010A6   ; OUTI
site 010A8   ; OUTI
site 010AA   ; OUTI
site 010AC   ; OUTI
site 010AE   ; OUTI
site 010B0   ; OUTI
site 010B2   ; OUTI
site 010B4   ; OUTI
site 010B6   ; OUTI
site 010B8   ; OUTI
site 010BA   ; OUTI
site 010BC   ; OUTI
site 010BE   ; OUTI
site 010C0   ; OUTI
site 010C2   ; OUTI
site 010C4   ; OUTI
site 010C6   ; OUTI
site 010C8   ; OUTI
site 010CA   ; OUTI
site 010CC   ; OUTI
site 010CE   ; OUTI
site 010D0   ; OUTI
site 010D2   ; OUTI
site 010D4   ; OUTI
site 010D6   ; OUTI
site 010D8   ; OUTI
site 010DA   ; OUTI
site 010DC   ; OUTI
site 010DE   ; OUTI
site 010E0   ; OUTI
site 010E2   ; OUTI
site 010E4   ; OUTI
site 010E6   ; OUTI
site 010E8   ; OUTI
site 010EA   ; OUTI
site 010EC   ; OUTI
site 010EE   ; OUTI
site 010F0   ; OUTI
site 010F2   ; OUTI
site 010F4   ; OUTI
site 010F6   ; OUTI
site 010F8   ; OUTI
site 010FA   ; OUTI
site 010FC   ; OUTI
site 010FE   ; OUTI
site 01100   ; OUTI
site 01102   ; OUTI
site 01104   ; OUTI
site 01106   ; OUTI
site 01108   ; OUTI
site 0110A   ; OUTI
site 0110C   ; OUTI
site 0110E   ; OUTI
site 01110   ; OUTI
site 01112   ; OUTI
site 01114   ; OUTI
site 01116   ; OUTI
site 01118   ; OUTI
site 0111A   ; OUTI
site 0111C   ; OUTI
site 0111E   ; OUTI
site 01120   ; OUTI
site 01122   ; OUTI
site 01124   ; OUTI
site 01126   ; OUTI
site 01128   ; OUTI
site 0112A   ; OUTI
site 0112C   ; OUTI
site 0112E   ; OUTI
site 01130   ; OUTI
site 01132   ; OUTI
site 01134   ; OUTI
site 01136   ; OUTI
site 01138   ; OUTI
site 0113A   ; OUTI
site 0113C   ; OUTI
site 0113E   ; OUTI
site 01140   ; OUTI
site 01142   ; OUTI
site 01144   ; OUTI
site 01146   ; OUTI
site 01148   ; OUTI
site 0114A   ; OUTI
site 0114C   ; OUTI
site 0114E   ; OUTI
site 01150   ; OUTI
site 01152   ; OUTI
site 01154   ; OUTI
site 01156   ; OUTI
site 01158   ; OUTI
site 0115A   ; OUTI
site 0115C   ; OUTI
site 0115E   ; OUTI
site 01160   ; OUTI
site 01162   ; OUTI
site 01164   ; OUTI
site 01166   ; OUTI
site 01168   ; OUTI
site 0116A   ; OUTI
site 0116C   ; OUTI
site 0116E   ; OUTI
site 01170   ; OUTI
site 01172   ; OUTI
site 01174   ; OUTI
site 01176   ; OUTI
site 01178   ; OUTI
site 0117A   ; OUTI
site 0117C   ; OUTI
site 0117E   ; OUTI
site 01180   ; OUTI
site 01182   ; OUTI
site 01184   ; OUTI
site 01186   ; OUTI
site 01188   ; OUTI
site 0118A   ; OUTI
site 0118C   ; OUTI
site 0118E   ; OUTI
site 01190   ; OUTI
site 01192   ; OUTI
site 01194   ; OUTI
site 01196   ; OUTI
site 01198   ; OUTI
site 0119A   ; OUTI
site 0119C   ; OUTI
site 0119E   ; OUTI
site 011A0   ; OUTI
site 011A2   ; OUTI
site 011A4   ; OUTI
site 011A6   ; OUTI
site 011A8   ; OUTI
site 011AA   ; OUTI
site 011AC   ; OUTI
site 011AE   ; OUTI
site 011B0   ; OUTI
site 011B2   ; OUTI
site 011B4   ; OUTI
site 011B6   ; OUTI
site 011B8   ; OUTI
site 011BA   ; OUTI
site 011BC   ; OUTI
site 011BE   ; OUTI
site 011C0   ; OUTI
site 011C2   ; OUTI
site 011C4   ; OUTI
site 011C6   ; OUTI
site 011C8   ; OUTI
site 011CA   ; OUTI
site 011CC   ; OUTI
site 011CE   ; OUTI
site 011D0   ; OUTI
site 011D2   ; OUTI
otir 011DE   ; OUTI
otir 011E4   ; OUTI
otir 011EA   ; OUTI
otir 011F0   ; OUTI
otir 011F6   ; OUTI
site 01204   ; OUTI
site 01208   ; OUTI
site 0120D   ; OUT ($BE),A
site 01218   ; OUTI
site 0121A   ; OUTI
site 0121C   ; OUT ($BE),A
site 0121E   ; OUTI
site 01220   ; OUTI
site 01222   ; OUTI
site 01224   ; OUT ($BE),A
site 01226   ; OUTI
site 01228   ; OUTI
site 0122A   ; OUTI
site 0122C   ; OUT ($BE),A
site 0122E   ; OUTI
site 01230   ; OUTI
site 01232   ; OUTI
site 01234   ; OUT ($BE),A
site 01236   ; OUTI
site 01238   ; OUTI
site 0123A   ; OUTI
site 0123C   ; OUT ($BE),A
site 0123E   ; OUTI
site 01240   ; OUTI
site 01242   ; OUTI
site 01244   ; OUT ($BE),A
site 01246   ; OUTI
site 01248   ; OUTI
site 0124A   ; OUTI
site 0124C   ; OUT ($BE),A
site 0124E   ; OUTI
site 01250   ; OUTI
site 01252   ; OUTI
site 01254   ; OUT ($BE),A
site 01256   ; OUTI
site 01258   ; OUTI
site 0125A   ; OUTI
site 0125C   ; OUT ($BE),A
site 0125E   ; OUTI
site 01260   ; OUTI
site 01262   ; OUTI
site 01264   ; OUT ($BE),A
site 01266   ; OUTI
site 01268   ; OUTI
site 0126A   ; OUTI
site 0126C   ; OUT ($BE),A
site 0126E   ; OUTI
site 01270   ; OUTI
site 01272   ; OUTI
site 01274   ; OUT ($BE),A
site 01276   ; OUTI
site 01278   ; OUTI
site 0127A   ; OUTI
site 0127C   ; OUT ($BE),A
site 0127E   ; OUTI
site 01280   ; OUTI
site 01282   ; OUTI
site 01284   ; OUT ($BE),A
site 01286   ; OUTI
site 01288   ; OUTI
site 0128A   ; OUTI
site 0128C   ; OUT ($BE),A
site 0128E   ; OUTI
site 01290   ; OUTI
site 01292   ; OUTI
site 01294   ; OUT ($BE),A
site 01296   ; OUTI
site 01298   ; OUTI
site 0129A   ; OUTI
site 0129C   ; OUT ($BE),A
site 0129E   ; OUTI
site 012A0   ; OUTI
site 012A2   ; OUTI
site 012A4   ; OUT ($BE),A
site 012A6   ; OUTI
site 012A8   ; OUTI
site 012AA   ; OUTI
site 012AC   ; OUT ($BE),A
site 012AE   ; OUTI
site 012B0   ; OUTI
site 012B2   ; OUTI
site 012B4   ; OUT ($BE),A
site 012B6   ; OUTI
site 012B8   ; OUTI
site 012BA   ; OUTI
site 012BC   ; OUT ($BE),A
site 012BE   ; OUTI
site 012C0   ; OUTI
site 012C2   ; OUTI
site 012C4   ; OUT ($BE),A
site 012C6   ; OUTI
site 012C8   ; OUTI
site 012CA   ; OUTI
site 012CC   ; OUT ($BE),A
site 012CE   ; OUTI
site 012D0   ; OUTI
site 012D2   ; OUTI
site 012D4   ; OUT ($BE),A
site 012D6   ; OUTI
site 012D8   ; OUTI
site 012DA   ; OUTI
site 012DC   ; OUT ($BE),A
site 012DE   ; OUTI
site 012E0   ; OUTI
site 012E2   ; OUTI
site 012E4   ; OUT ($BE),A
site 012E6   ; OUTI
site 012E8   ; OUTI
site 012EA   ; OUTI
site 012EC   ; OUT ($BE),A
site 012EE   ; OUTI
site 012F0   ; OUTI
site 012F2   ; OUTI
site 012F4   ; OUT ($BE),A
site 012F6   ; OUTI
site 012F8   ; OUTI
site 012FA   ; OUTI
site 012FC   ; OUT ($BE),A
site 012FE   ; OUTI
site 01300   ; OUTI
site 01302   ; OUTI
site 01304   ; OUT ($BE),A
site 01306   ; OUTI
site 01308   ; OUTI
site 0130A   ; OUTI
site 0130C   ; OUT ($BE),A
site 0130E   ; OUTI
site 01310   ; OUTI
site 01312   ; OUTI
site 01314   ; OUT ($BE),A
site 01316   ; OUTI
site 01318   ; OUTI
site 0131A   ; OUTI
site 0131C   ; OUT ($BE),A
site 0131E   ; OUTI
site 01320   ; OUTI
site 01322   ; OUTI
site 01324   ; OUT ($BE),A
site 01326   ; OUTI
site 01328   ; OUTI
site 0132A   ; OUTI
site 0132C   ; OUT ($BE),A
site 0132E   ; OUTI
site 01330   ; OUTI
site 01332   ; OUTI
site 01334   ; OUT ($BE),A
site 01336   ; OUTI
site 01338   ; OUTI
site 0133A   ; OUTI
site 0133C   ; OUT ($BE),A
site 0133E   ; OUTI
site 01340   ; OUTI
site 01342   ; OUTI
site 01344   ; OUT ($BE),A
site 01346   ; OUTI
site 01348   ; OUTI
site 0134A   ; OUTI
site 0134C   ; OUT ($BE),A
site 0134E   ; OUTI
site 01350   ; OUTI
site 01352   ; OUTI
site 01354   ; OUT ($BE),A
site 01356   ; OUTI
site 01358   ; OUTI
site 0135A   ; OUTI
site 0135C   ; OUT ($BE),A
site 0135E   ; OUTI
site 01360   ; OUTI
site 01362   ; OUTI
site 01364   ; OUT ($BE),A
site 01366   ; OUTI
site 01368   ; OUTI
site 0136A   ; OUTI
site 0136C   ; OUT ($BE),A
site 0136E   ; OUTI
site 01370   ; OUTI
site 01372   ; OUTI
site 01374   ; OUT ($BE),A
site 01376   ; OUTI
site 01378   ; OUTI
site 0137A   ; OUTI
site 0137C   ; OUT ($BE),A
site 0137E   ; OUTI
site 01380   ; OUTI
site 01382   ; OUTI
site 01384   ; OUT ($BE),A
site 01386   ; OUTI
site 01388   ; OUTI
site 0138A   ; OUTI
site 0138C   ; OUT ($BE),A
site 0138E   ; OUTI
site 01390   ; OUTI
site 01392   ; OUTI
site 01394   ; OUT ($BE),A
site 01396   ; OUTI
site 01398   ; OUTI
site 0139A   ; OUTI
site 0139C   ; OUT ($BE),A
site 0139E   ; OUTI
site 013A0   ; OUTI
site 013A2   ; OUTI
site 013A4   ; OUT ($BE),A
site 013A6   ; OUTI
site 013A8   ; OUTI
site 013AA   ; OUTI
site 013AC   ; OUT ($BE),A
site 013AE   ; OUTI
site 013B0   ; OUTI
site 013B2   ; OUTI
site 013B4   ; OUT ($BE),A
site 013B6   ; OUTI
site 013B8   ; OUTI
site 013BA   ; OUTI
site 013BC   ; OUT ($BE),A
site 013BE   ; OUTI
site 013C0   ; OUTI
site 013C2   ; OUTI
site 013C4   ; OUT ($BE),A
site 013C6   ; OUTI
site 013C8   ; OUTI
site 013CA   ; OUTI
site 013CC   ; OUT ($BE),A
site 013CE   ; OUTI
site 013D0   ; OUTI
site 013D2   ; OUTI
site 013D4   ; OUT ($BE),A
site 013D6   ; OUTI
site 013D8   ; OUTI
site 013DA   ; OUTI
site 013DC   ; OUT ($BE),A
site 013DE   ; OUTI
site 013E0   ; OUTI
site 013E2   ; OUTI
site 013E4   ; OUT ($BE),A
site 013E6   ; OUTI
site 013E8   ; OUTI
site 013EA   ; OUTI
site 013EC   ; OUT ($BE),A
site 013EE   ; OUTI
site 013F0   ; OUTI
site 013F2   ; OUTI
site 013F4   ; OUT ($BE),A
site 013F6   ; OUTI
site 013F8   ; OUTI
site 013FA   ; OUTI
site 013FC   ; OUT ($BE),A
site 013FE   ; OUTI
site 01400   ; OUTI
site 01402   ; OUTI
site 01404   ; OUT ($BE),A
site 01406   ; OUTI
site 01408   ; OUTI
site 0140A   ; OUTI
site 0140C   ; OUT ($BE),A
site 0140E   ; OUTI
site 01410   ; OUTI
site 01412   ; OUTI
site 01414   ; OUT ($BE),A
site 01416   ; OUTI
site 01418   ; OUTI
site 0141A   ; OUTI
site 0141C   ; OUT ($BE),A
site 0141E   ; OUTI
site 01420   ; OUTI
site 01422   ; OUTI
site 01424   ; OUT ($BE),A
site 01426   ; OUTI
site 01428   ; OUTI
site 0142A   ; OUTI
site 0142C   ; OUT ($BE),A
site 0142E   ; OUTI
site 01430   ; OUTI
site 01432   ; OUTI
site 01434   ; OUT ($BE),A
site 01436   ; OUTI
site 01438   ; OUTI
site 0143A   ; OUTI
site 0143C   ; OUT ($BE),A
site 0143E   ; OUTI
site 01440   ; OUTI
site 01442   ; OUTI
site 01444   ; OUT ($BE),A
site 01446   ; OUTI
site 01448   ; OUTI
site 0144A   ; OUTI
site 0144C   ; OUT ($BE),A
site 0144E   ; OUTI
site 01450   ; OUTI
site 01452   ; OUTI
site 01454   ; OUT ($BE),A
site 01456   ; OUTI
site 01458   ; OUTI
site 0145A   ; OUTI
site 0145C   ; OUT ($BE),A
site 0145E   ; OUTI
site 01460   ; OUTI
site 01462   ; OUTI
site 01464   ; OUT ($BE),A
site 01466   ; OUTI
site 01468   ; OUTI
site 0146A   ; OUTI
site 0146C   ; OUT ($BE),A
site 0146E   ; OUTI
site 01470   ; OUTI
site 01472   ; OUTI
site 01474   ; OUT ($BE),A
site 01476   ; OUTI
site 01478   ; OUTI
site 0147A   ; OUTI
site 0147C   ; OUT ($BE),A
site 0147E   ; OUTI
site 01480   ; OUTI
site 01482   ; OUTI
site 01484   ; OUT ($BE),A
site 01486   ; OUTI
site 01488   ; OUTI
site 0148A   ; OUTI
site 0148C   ; OUT ($BE),A
site 0148E   ; OUTI
site 01490   ; OUTI
site 01492   ; OUTI
site 01494   ; OUT ($BE),A
site 01496   ; OUTI
site 01498   ; OUTI
site 0149A   ; OUTI
site 0149C   ; OUT ($BE),A
site 0149E   ; OUTI
site 014A0   ; OUTI
site 014A2   ; OUTI
site 014A4   ; OUT ($BE),A
site 014A6   ; OUTI
site 014A8   ; OUTI
site 014AA   ; OUTI
site 014AC   ; OUT ($BE),A
site 014AE   ; OUTI
site 014B0   ; OUTI
site 014B2   ; OUTI
site 014B4   ; OUT ($BE),A
site 014B6   ; OUTI
site 014B8   ; OUTI
site 014BA   ; OUTI
site 014BC   ; OUT ($BE),A
site 014BE   ; OUTI
site 014C0   ; OUTI
site 014C2   ; OUTI
site 014C4   ; OUT ($BE),A
site 014C6   ; OUTI
site 014C8   ; OUTI
site 014CA   ; OUTI
site 014CC   ; OUT ($BE),A
site 014CE   ; OUTI
site 014D0   ; OUTI
site 014D2   ; OUTI
site 014D4   ; OUT ($BE),A
site 014D6   ; OUTI
site 014D8   ; OUTI
site 014DA   ; OUTI
site 014DC   ; OUT ($BE),A
site 014DE   ; OUTI
site 014E0   ; OUTI
site 014E2   ; OUTI
site 014E4   ; OUT ($BE),A
site 014E6   ; OUTI
site 014E8   ; OUTI
site 014EA   ; OUTI
site 014EC   ; OUT ($BE),A
site 014EE   ; OUTI
site 014F0   ; OUTI
site 014F2   ; OUTI
site 014F4   ; OUT ($BE),A
site 014F6   ; OUTI
site 014F8   ; OUTI
site 014FA   ; OUTI
site 014FC   ; OUT ($BE),A
site 014FE   ; OUTI
site 01500   ; OUTI
site 01502   ; OUTI
site 01504   ; OUT ($BE),A
site 01506   ; OUTI
site 01508   ; OUTI
site 0150A   ; OUTI
site 0150C   ; OUT ($BE),A
site 0150E   ; OUTI
site 01510   ; OUTI
site 01512   ; OUTI
site 01514   ; OUT ($BE),A
site 01516   ; OUTI
site 01518   ; OUTI
site 0151A   ; OUTI
site 0151C   ; OUT ($BE),A
site 0151E   ; OUTI
site 01520   ; OUTI
site 01522   ; OUTI
site 01524   ; OUT ($BE),A
site 01526   ; OUTI
site 01528   ; OUTI
site 0152A   ; OUTI
site 0152C   ; OUT ($BE),A
site 0152E   ; OUTI
site 01530   ; OUTI
site 01532   ; OUTI
site 01534   ; OUT ($BE),A
site 01536   ; OUTI
site 01538   ; OUTI
site 0153A   ; OUTI
site 0153C   ; OUT ($BE),A
site 0153E   ; OUTI
site 01540   ; OUTI
site 01542   ; OUTI
site 01544   ; OUT ($BE),A
site 01546   ; OUTI
site 01548   ; OUTI
site 0154A   ; OUTI
site 0154C   ; OUT ($BE),A
site 0154E   ; OUTI
site 01550   ; OUTI
site 01552   ; OUTI
site 01554   ; OUT ($BE),A
site 01556   ; OUTI
site 01558   ; OUTI
site 0155A   ; OUTI
site 0155C   ; OUT ($BE),A
site 0155E   ; OUTI
site 01560   ; OUTI
site 01562   ; OUTI
site 01564   ; OUT ($BE),A
site 01566   ; OUTI
site 01568   ; OUTI
site 0156A   ; OUTI
site 0156C   ; OUT ($BE),A
site 0156E   ; OUTI
site 01570   ; OUTI
site 01572   ; OUTI
site 01574   ; OUT ($BE),A
site 01576   ; OUTI
site 01578   ; OUTI
site 0157A   ; OUTI
site 0157C   ; OUT ($BE),A
site 0157E   ; OUTI
site 01580   ; OUTI
site 01582   ; OUTI
site 01584   ; OUT ($BE),A
site 01586   ; OUTI
site 01588   ; OUTI
site 0158A   ; OUTI
site 0158C   ; OUT ($BE),A
site 0158E   ; OUTI
site 01590   ; OUTI
site 01592   ; OUTI
site 01594   ; OUT ($BE),A
site 01596   ; OUTI
site 01598   ; OUTI
site 0159A   ; OUTI
site 0159C   ; OUT ($BE),A
site 0159E   ; OUTI
site 015A0   ; OUTI
site 015A2   ; OUTI
site 015A4   ; OUT ($BE),A
site 015A6   ; OUTI
site 015A8   ; OUTI
site 015AA   ; OUTI
site 015AC   ; OUT ($BE),A
site 015AE   ; OUTI
site 015B0   ; OUTI
site 015B2   ; OUTI
site 015B4   ; OUT ($BE),A
site 015B6   ; OUTI
site 015B8   ; OUTI
site 015BA   ; OUTI
site 015BC   ; OUT ($BE),A
site 015BE   ; OUTI
site 015C0   ; OUTI
site 015C2   ; OUTI
site 015C4   ; OUT ($BE),A
site 015C6   ; OUTI
site 015C8   ; OUTI
site 015CA   ; OUTI
site 015CC   ; OUT ($BE),A
site 015CE   ; OUTI
site 015D0   ; OUTI
site 015D2   ; OUTI
site 015D4   ; OUT ($BE),A
site 015D6   ; OUTI
site 015D8   ; OUTI
site 015DA   ; OUTI
site 015DC   ; OUT ($BE),A
site 015DE   ; OUTI
site 015E0   ; OUTI
site 015E2   ; OUTI
site 015E4   ; OUT ($BE),A
site 015E6   ; OUTI
site 015E8   ; OUTI
site 015EA   ; OUTI
site 015EC   ; OUT ($BE),A
site 015EE   ; OUTI
site 015F0   ; OUTI
site 015F2   ; OUTI
site 015F4   ; OUT ($BE),A
site 015F6   ; OUTI
site 015F8   ; OUTI
site 015FA   ; OUTI
site 015FC   ; OUT ($BE),A
site 015FE   ; OUTI
site 01600   ; OUTI
site 01602   ; OUTI
site 01604   ; OUT ($BE),A
site 01606   ; OUTI
site 01608   ; OUTI
site 0160A   ; OUTI
site 0160C   ; OUT ($BE),A
site 0160E   ; OUTI
site 01610   ; OUTI
site 01612   ; OUTI
site 01614   ; OUT ($BE),A
site 01616   ; OUTI
site 01618   ; OUTI
site 0161A   ; OUTI
site 0161C   ; OUT ($BE),A
site 0161E   ; OUTI
site 01620   ; OUTI
site 01622   ; OUTI
site 01624   ; OUT ($BE),A
site 01626   ; OUTI
site 01628   ; OUTI
site 0162A   ; OUTI
site 0162C   ; OUT ($BE),A
site 0162E   ; OUTI
site 01630   ; OUTI
site 01632   ; OUTI
site 01634   ; OUT ($BE),A
site 01636   ; OUTI
site 01638   ; OUTI
site 0163A   ; OUTI
site 0163C   ; OUT ($BE),A
site 0163E   ; OUTI
site 01640   ; OUTI
site 01642   ; OUTI
site 01644   ; OUT ($BE),A
site 01646   ; OUTI
site 01648   ; OUTI
site 0164A   ; OUTI
site 0164C   ; OUT ($BE),A
site 0164E   ; OUTI
site 01650   ; OUTI
site 01652   ; OUTI
site 01654   ; OUT ($BE),A
site 01656   ; OUTI
site 01658   ; OUTI
site 0165A   ; OUTI
site 0165C   ; OUT ($BE),A
site 0165E   ; OUTI
site 01660   ; OUTI
site 01662   ; OUTI
site 01664   ; OUT ($BE),A
site 01666   ; OUTI
site 01668   ; OUTI
site 0166A   ; OUTI
site 0166C   ; OUT ($BE),A
site 0166E   ; OUTI
site 01670   ; OUTI
site 01672   ; OUTI
site 01674   ; OUT ($BE),A
site 01676   ; OUTI
site 01678   ; OUTI
site 0167A   ; OUTI
site 0167C   ; OUT ($BE),A
site 0167E   ; OUTI
site 01680   ; OUTI
site 01682   ; OUTI
site 01684   ; OUT ($BE),A
site 01686   ; OUTI
site 01688   ; OUTI
site 0168A   ; OUTI
site 0168C   ; OUT ($BE),A
site 0168E   ; OUTI
site 01690   ; OUTI
site 01692   ; OUTI
site 01694   ; OUT ($BE),A
site 01696   ; OUTI
site 01698   ; OUTI
site 0169A   ; OUTI
site 0169C   ; OUT ($BE),A
site 0169E   ; OUTI
site 016A0   ; OUTI
site 016A2   ; OUTI
site 016A4   ; OUT ($BE),A
site 016A6   ; OUTI
site 016A8   ; OUTI
site 016AA   ; OUTI
site 016AC   ; OUT ($BE),A
site 016AE   ; OUTI
site 016B0   ; OUTI
site 016B2   ; OUTI
site 016B4   ; OUT ($BE),A
site 016B6   ; OUTI
site 016B8   ; OUTI
site 016BA   ; OUTI
site 016BC   ; OUT ($BE),A
site 016BE   ; OUTI
site 016C0   ; OUTI
site 016C2   ; OUTI
site 016C4   ; OUT ($BE),A
site 016C6   ; OUTI
site 016C8   ; OUTI
site 016CA   ; OUTI
site 016CC   ; OUT ($BE),A
site 016CE   ; OUTI
site 016D0   ; OUTI
site 016D2   ; OUTI
site 016D4   ; OUT ($BE),A
site 016D6   ; OUTI
site 016D8   ; OUTI
site 016DA   ; OUTI
site 016DC   ; OUT ($BE),A
site 016DE   ; OUTI
site 016E0   ; OUTI
site 016E2   ; OUTI
site 016E4   ; OUT ($BE),A
site 016E6   ; OUTI
site 016E8   ; OUTI
site 016EA   ; OUTI
site 016EC   ; OUT ($BE),A
site 016EE   ; OUTI
site 016F0   ; OUTI
site 016F2   ; OUTI
site 016F4   ; OUT ($BE),A
site 016F6   ; OUTI
site 016F8   ; OUTI
site 016FA   ; OUTI
site 016FC   ; OUT ($BE),A
site 016FE   ; OUTI
site 01700   ; OUTI
site 01702   ; OUTI
site 01704   ; OUT ($BE),A
site 01706   ; OUTI
site 01708   ; OUTI
site 0170A   ; OUTI
site 0170C   ; OUT ($BE),A
site 0170E   ; OUTI
site 01710   ; OUTI
site 01712   ; OUTI
site 01714   ; OUT ($BE),A
site 01716   ; OUTI
site 01718   ; OUTI
site 0171A   ; OUTI
site 0171C   ; OUT ($BE),A
site 0171E   ; OUTI
site 01720   ; OUTI
site 01722   ; OUTI
site 01724   ; OUT ($BE),A
site 01726   ; OUTI
site 01728   ; OUTI
site 0172A   ; OUTI
site 0172C   ; OUT ($BE),A
site 0172E   ; OUTI
site 01730   ; OUTI
site 01732   ; OUTI
site 01734   ; OUT ($BE),A
site 01736   ; OUTI
site 01738   ; OUTI
site 0173A   ; OUTI
site 0173C   ; OUT ($BE),A
site 0173E   ; OUTI
site 01740   ; OUTI
site 01742   ; OUTI
site 01744   ; OUT ($BE),A
site 01746   ; OUTI
site 01748   ; OUTI
site 0174A   ; OUTI
site 0174C   ; OUT ($BE),A
site 0174E   ; OUTI
site 01750   ; OUTI
site 01752   ; OUTI
site 01754   ; OUT ($BE),A
site 01756   ; OUTI
site 01758   ; OUTI
site 0175A   ; OUTI
site 0175C   ; OUT ($BE),A
site 0175E   ; OUTI
site 01760   ; OUTI
site 01762   ; OUTI
site 01764   ; OUT ($BE),A
site 01766   ; OUTI
site 01768   ; OUTI
site 0176A   ; OUTI
site 0176C   ; OUT ($BE),A
site 0176E   ; OUTI
site 01770   ; OUTI
site 01772   ; OUTI
site 01774   ; OUT ($BE),A
site 01776   ; OUTI
site 01778   ; OUTI
site 0177A   ; OUTI
site 0177C   ; OUT ($BE),A
site 0177E   ; OUTI
site 01780   ; OUTI
site 01782   ; OUTI
site 01784   ; OUT ($BE),A
site 01786   ; OUTI
site 01788   ; OUTI
site 0178A   ; OUTI
site 0178C   ; OUT ($BE),A
site 0178E   ; OUTI
site 01790   ; OUTI
site 01792   ; OUTI
site 01794   ; OUT ($BE),A
site 01796   ; OUTI
site 01798   ; OUTI
site 0179A   ; OUTI
site 0179C   ; OUT ($BE),A
site 0179E   ; OUTI
site 017A0   ; OUTI
site 017A2   ; OUTI
site 017A4   ; OUT ($BE),A
site 017A6   ; OUTI
site 017A8   ; OUTI
site 017AA   ; OUTI
site 017AC   ; OUT ($BE),A
site 017AE   ; OUTI
site 017B0   ; OUTI
site 017B2   ; OUTI
site 017B4   ; OUT ($BE),A
site 017B6   ; OUTI
site 017B8   ; OUTI
site 017BA   ; OUTI
site 017BC   ; OUT ($BE),A
site 017BE   ; OUTI
site 017C0   ; OUTI
site 017C2   ; OUTI
site 017C4   ; OUT ($BE),A
site 017C6   ; OUTI
site 017C8   ; OUTI
site 017CA   ; OUTI
site 017CC   ; OUT ($BE),A
site 017CE   ; OUTI
site 017D0   ; OUTI
site 017D2   ; OUTI
site 017D4   ; OUT ($BE),A
site 017D6   ; OUTI
site 017D8   ; OUTI
site 017DA   ; OUTI
site 017DC   ; OUT ($BE),A
site 017DE   ; OUTI
site 017E0   ; OUTI
site 017E2   ; OUTI
site 017E4   ; OUT ($BE),A
site 017E6   ; OUTI
site 017E8   ; OUTI
site 017EA   ; OUTI
site 017EC   ; OUT ($BE),A
site 017EE   ; OUTI
site 017F0   ; OUTI
site 017F2   ; OUTI
site 017F4   ; OUT ($BE),A
site 017F6   ; OUTI
site 017F8   ; OUTI
site 017FA   ; OUTI
site 017FC   ; OUT ($BE),A
site 017FE   ; OUTI
site 01800   ; OUTI
site 01802   ; OUTI
site 01804   ; OUT ($BE),A
site 01806   ; OUTI
site 01808   ; OUTI
site 0180A   ; OUTI
site 0180C   ; OUT ($BE),A
site 0180E   ; OUTI
site 01810   ; OUTI
site 01812   ; OUTI
site 01814   ; OUT ($BE),A
site 01816   ; OUTI
site 01818   ; OUTI
site 0181A   ; OUTI
site 0181C   ; OUT ($BE),A
site 0181E   ; OUTI
site 01820   ; OUTI
site 01822   ; OUTI
site 01824   ; OUT ($BE),A
site 01826   ; OUTI
site 01828   ; OUTI
site 0182A   ; OUTI
site 0182C   ; OUT ($BE),A
site 0182E   ; OUTI
site 01830   ; OUTI
site 01832   ; OUTI
site 01834   ; OUT ($BE),A
site 01836   ; OUTI
site 01838   ; OUTI
site 0183A   ; OUTI
site 0183C   ; OUT ($BE),A
site 0183E   ; OUTI
site 01840   ; OUTI
site 01842   ; OUTI
site 01844   ; OUT ($BE),A
site 01846   ; OUTI
site 01848   ; OUTI
site 0184A   ; OUTI
site 0184C   ; OUT ($BE),A
site 0184E   ; OUTI
site 01850   ; OUTI
site 01852   ; OUTI
site 01854   ; OUT ($BE),A
site 01856   ; OUTI
site 01858   ; OUTI
site 0185A   ; OUTI
site 0185C   ; OUT ($BE),A
site 0185E   ; OUTI
site 01860   ; OUTI
site 01862   ; OUTI
site 01864   ; OUT ($BE),A
site 01866   ; OUTI
site 01868   ; OUTI
site 0186A   ; OUTI
site 0186C   ; OUT ($BE),A
site 0186E   ; OUTI
site 01870   ; OUTI
site 01872   ; OUTI
site 01874   ; OUT ($BE),A
site 01876   ; OUTI
site 01878   ; OUTI
site 0187A   ; OUTI
site 0187C   ; OUT ($BE),A
site 0187E   ; OUTI
site 01880   ; OUTI
site 01882   ; OUTI
site 01884   ; OUT ($BE),A
site 01886   ; OUTI
site 01888   ; OUTI
site 0188A   ; OUTI
site 0188C   ; OUT ($BE),A
site 0188E   ; OUTI
site 01890   ; OUTI
site 01892   ; OUTI
site 01894   ; OUT ($BE),A
site 0189D   ; OUTI
site 0189F   ; OUT ($BE),A
site 018A1   ; OUTI
site 018A3   ; OUT ($BE),A
site 018A5   ; OUTI
site 018A7   ; OUT ($BE),A
site 018A9   ; OUTI
site 018AB   ; OUT ($BE),A
site 018AD   ; OUTI
site 018AF   ; OUT ($BE),A
site 018B1   ; OUTI
site 018B3   ; OUT ($BE),A
site 018B5   ; OUTI
site 018B7   ; OUT ($BE),A
site 018B9   ; OUTI
site 018BB   ; OUT ($BE),A
site 018BD   ; OUTI
site 018BF   ; OUT ($BE),A
site 018C1   ; OUTI
site 018C3   ; OUT ($BE),A
site 018C5   ; OUTI
site 018C7   ; OUT ($BE),A
site 018C9   ; OUTI
site 018CB   ; OUT ($BE),A
site 018CD   ; OUTI
site 018CF   ; OUT ($BE),A
site 018D1   ; OUTI
site 018D3   ; OUT ($BE),A
site 018D5   ; OUTI
site 018D7   ; OUT ($BE),A
site 018D9   ; OUTI
site 018DB   ; OUT ($BE),A
site 018DD   ; OUTI
site 018DF   ; OUT ($BE),A
site 018E1   ; OUTI
site 018E3   ; OUT ($BE),A
site 018E5   ; OUTI
site 018E7   ; OUT ($BE),A
site 018E9   ; OUTI
site 018EB   ; OUT ($BE),A
site 018ED   ; OUTI
site 018EF   ; OUT ($BE),A
site 018F1   ; OUTI
site 018F3   ; OUT ($BE),A
site 018F5   ; OUTI
site 018F7   ; OUT ($BE),A
site 018F9   ; OUTI
site 018FB   ; OUT ($BE),A
site 018FD   ; OUTI
site 018FF   ; OUT ($BE),A
site 01901   ; OUTI
site 01903   ; OUT ($BE),A
site 01905   ; OUTI
site 01907   ; OUT ($BE),A
site 01909   ; OUTI
site 0190B   ; OUT ($BE),A
site 0190D   ; OUTI
site 0190F   ; OUT ($BE),A
site 01911   ; OUTI
site 01913   ; OUT ($BE),A
site 01915   ; OUTI
site 01917   ; OUT ($BE),A
site 01919   ; OUTI
site 0191B   ; OUT ($BE),A
site 0191D   ; OUTI
site 0191F   ; OUT ($BE),A
site 01921   ; OUTI
site 01923   ; OUT ($BE),A
site 01925   ; OUTI
site 01927   ; OUT ($BE),A
site 01929   ; OUTI
site 0192B   ; OUT ($BE),A
site 0192D   ; OUTI
site 0192F   ; OUT ($BE),A
site 01931   ; OUTI
site 01933   ; OUT ($BE),A
site 01935   ; OUTI
site 01937   ; OUT ($BE),A
site 01939   ; OUTI
site 0193B   ; OUT ($BE),A
site 0193D   ; OUTI
site 0193F   ; OUT ($BE),A
site 01941   ; OUTI
site 01943   ; OUT ($BE),A
site 01945   ; OUTI
site 01947   ; OUT ($BE),A
site 01949   ; OUTI
site 0194B   ; OUT ($BE),A
site 0194D   ; OUTI
site 0194F   ; OUT ($BE),A
site 01951   ; OUTI
site 01953   ; OUT ($BE),A
site 01955   ; OUTI
site 01957   ; OUT ($BE),A
site 01959   ; OUTI
site 0195B   ; OUT ($BE),A
site 0195D   ; OUTI
site 0195F   ; OUT ($BE),A
site 01961   ; OUTI
site 01963   ; OUT ($BE),A
site 01965   ; OUTI
site 01967   ; OUT ($BE),A
site 01969   ; OUTI
site 0196B   ; OUT ($BE),A
site 0196D   ; OUTI
site 0196F   ; OUT ($BE),A
site 01971   ; OUTI
site 01973   ; OUT ($BE),A
site 01975   ; OUTI
site 01977   ; OUT ($BE),A
site 01979   ; OUTI
site 0197B   ; OUT ($BE),A
site 0197D   ; OUTI
site 0197F   ; OUT ($BE),A
site 01981   ; OUTI
site 01983   ; OUT ($BE),A
site 01985   ; OUTI
site 01987   ; OUT ($BE),A
site 01989   ; OUTI
site 0198B   ; OUT ($BE),A
site 0198D   ; OUTI
site 0198F   ; OUT ($BE),A
site 01991   ; OUTI
site 01993   ; OUT ($BE),A
site 01995   ; OUTI
site 01997   ; OUT ($BE),A
site 01999   ; OUTI
site 0199B   ; OUT ($BE),A
site 0199D   ; OUTI
site 0199F   ; OUT ($BE),A
site 019A1   ; OUTI
site 019A3   ; OUT ($BE),A
site 019A5   ; OUTI
site 019A7   ; OUT ($BE),A
site 019A9   ; OUTI
site 019AB   ; OUT ($BE),A
site 019AD   ; OUTI
site 019AF   ; OUT ($BE),A
site 019B1   ; OUTI
site 019B3   ; OUT ($BE),A
site 019B5   ; OUTI
site 019B7   ; OUT ($BE),A
site 019B9   ; OUTI
site 019BB   ; OUT ($BE),A
site 019BD   ; OUTI
site 019BF   ; OUT ($BE),A
site 019C1   ; OUTI
site 019C3   ; OUT ($BE),A
site 019C5   ; OUTI
site 019C7   ; OUT ($BE),A
site 019C9   ; OUTI
site 019CB   ; OUT ($BE),A
site 019CD   ; OUTI
site 019CF   ; OUT ($BE),A
site 019D1   ; OUTI
site 019D3   ; OUT ($BE),A
site 019D5   ; OUTI
site 019D7   ; OUT ($BE),A
site 019D9   ; OUTI
site 019DB   ; OUT ($BE),A
site 019DD   ; OUTI
site 019DF   ; OUT ($BE),A
site 019E1   ; OUTI
site 019E3   ; OUT ($BE),A
site 019E5   ; OUTI
site 019E7   ; OUT ($BE),A
site 019E9   ; OUTI
site 019EB   ; OUT ($BE),A
site 019ED   ; OUTI
site 019EF   ; OUT ($BE),A
site 019F1   ; OUTI
site 019F3   ; OUT ($BE),A
site 019F5   ; OUTI
site 019F7   ; OUT ($BE),A
site 019F9   ; OUTI
site 019FB   ; OUT ($BE),A
site 019FD   ; OUTI
site 019FF   ; OUT ($BE),A
site 01A01   ; OUTI
site 01A03   ; OUT ($BE),A
site 01A05   ; OUTI
site 01A07   ; OUT ($BE),A
site 01A09   ; OUTI
site 01A0B   ; OUT ($BE),A
site 01A0D   ; OUTI
site 01A0F   ; OUT ($BE),A
site 01A11   ; OUTI
site 01A13   ; OUT ($BE),A
site 01A15   ; OUTI
site 01A17   ; OUT ($BE),A
site 01A19   ; OUTI
site 01A1B   ; OUT ($BE),A
site 01A1D   ; OUTI
site 01A1F   ; OUT ($BE),A
site 01A21   ; OUTI
site 01A23   ; OUT ($BE),A
site 01A25   ; OUTI
site 01A27   ; OUT ($BE),A
site 01A29   ; OUTI
site 01A2B   ; OUT ($BE),A
site 01A2D   ; OUTI
site 01A2F   ; OUT ($BE),A
site 01A31   ; OUTI
site 01A33   ; OUT ($BE),A
site 01A35   ; OUTI
site 01A37   ; OUT ($BE),A
site 01A39   ; OUTI
site 01A3B   ; OUT ($BE),A
site 01A3D   ; OUTI
site 01A3F   ; OUT ($BE),A
site 01A41   ; OUTI
site 01A43   ; OUT ($BE),A
site 01A45   ; OUTI
site 01A47   ; OUT ($BE),A
site 01A49   ; OUTI
site 01A4B   ; OUT ($BE),A
site 01A4D   ; OUTI
site 01A4F   ; OUT ($BE),A
site 01A51   ; OUTI
site 01A53   ; OUT ($BE),A
site 01A55   ; OUTI
site 01A57   ; OUT ($BE),A
site 01A59   ; OUTI
site 01A5B   ; OUT ($BE),A
site 01A5D   ; OUTI
site 01A5F   ; OUT ($BE),A
site 01A61   ; OUTI
site 01A63   ; OUT ($BE),A
site 01A65   ; OUTI
site 01A67   ; OUT ($BE),A
site 01A69   ; OUTI
site 01A6B   ; OUT ($BE),A
site 01A6D   ; OUTI
site 01A6F   ; OUT ($BE),A
site 01A71   ; OUTI
site 01A73   ; OUT ($BE),A
site 01A75   ; OUTI
site 01A77   ; OUT ($BE),A
site 01A79   ; OUTI
site 01A7B   ; OUT ($BE),A
site 01A7D   ; OUTI
site 01A7F   ; OUT ($BE),A
site 01A81   ; OUTI
site 01A83   ; OUT ($BE),A
site 01A85   ; OUTI
site 01A87   ; OUT ($BE),A
site 01A89   ; OUTI
site 01A8B   ; OUT ($BE),A
site 01A8D   ; OUTI
site 01A8F   ; OUT ($BE),A
site 01A91   ; OUTI
site 01A93   ; OUT ($BE),A
site 01A95   ; OUTI
site 01A97   ; OUT ($BE),A
site 01A99   ; OUTI
site 01A9B   ; OUT ($BE),A
site 01A9D   ; OUTI
site 01A9F   ; OUT ($BE),A
site 01AA1   ; OUTI
site 01AA3   ; OUT ($BE),A
site 01AA5   ; OUTI
site 01AA7   ; OUT ($BE),A
site 01AA9   ; OUTI
site 01AAB   ; OUT ($BE),A
site 01AAD   ; OUTI
site 01AAF   ; OUT ($BE),A
site 01AB1   ; OUTI
site 01AB3   ; OUT ($BE),A
site 01AB5   ; OUTI
site 01AB7   ; OUT ($BE),A
site 01AB9   ; OUTI
site 01ABB   ; OUT ($BE),A
site 01ABD   ; OUTI
site 01ABF   ; OUT ($BE),A
site 01AC1   ; OUTI
site 01AC3   ; OUT ($BE),A
site 01AC5   ; OUTI
site 01AC7   ; OUT ($BE),A
site 01AC9   ; OUTI
site 01ACB   ; OUT ($BE),A
site 01ACD   ; OUTI
site 01ACF   ; OUT ($BE),A
site 01AD1   ; OUTI
site 01AD3   ; OUT ($BE),A
site 01AD5   ; OUTI
site 01AD7   ; OUT ($BE),A
site 01AD9   ; OUTI
site 01ADB   ; OUT ($BE),A
site 01ADD   ; OUTI
site 01ADF   ; OUT ($BE),A
site 01AE1   ; OUTI
site 01AE3   ; OUT ($BE),A
site 01AE5   ; OUTI
site 01AE7   ; OUT ($BE),A
site 01AE9   ; OUTI
site 01AEB   ; OUT ($BE),A
site 01AED   ; OUTI
site 01AEF   ; OUT ($BE),A
site 01AF1   ; OUTI
site 01AF3   ; OUT ($BE),A
site 01AF5   ; OUTI
site 01AF7   ; OUT ($BE),A
site 01AF9   ; OUTI
site 01AFB   ; OUT ($BE),A
site 01AFD   ; OUTI
site 01AFF   ; OUT ($BE),A
site 01B01   ; OUTI
site 01B03   ; OUT ($BE),A
site 01B05   ; OUTI
site 01B07   ; OUT ($BE),A
site 01B09   ; OUTI
site 01B0B   ; OUT ($BE),A
site 01B0D   ; OUTI
site 01B0F   ; OUT ($BE),A
site 01B11   ; OUTI
site 01B13   ; OUT ($BE),A
site 01B15   ; OUTI
site 01B17   ; OUT ($BE),A
site 01B19   ; OUTI
site 01B1B   ; OUT ($BE),A
site 01B1D   ; OUTI
site 01B1F   ; OUT ($BE),A
site 01B21   ; OUTI
site 01B23   ; OUT ($BE),A
site 01B25   ; OUTI
site 01B27   ; OUT ($BE),A
site 01B29   ; OUTI
site 01B2B   ; OUT ($BE),A
site 01B2D   ; OUTI
site 01B2F   ; OUT ($BE),A
site 01B31   ; OUTI
site 01B33   ; OUT ($BE),A
site 01B35   ; OUTI
site 01B37   ; OUT ($BE),A
site 01B39   ; OUTI
site 01B3B   ; OUT ($BE),A
site 01B3D   ; OUTI
site 01B3F   ; OUT ($BE),A
site 01B41   ; OUTI
site 01B43   ; OUT ($BE),A
site 01B45   ; OUTI
site 01B47   ; OUT ($BE),A
site 01B49   ; OUTI
site 01B4B   ; OUT ($BE),A
site 01B4D   ; OUTI
site 01B4F   ; OUT ($BE),A
site 01B51   ; OUTI
site 01B53   ; OUT ($BE),A
site 01B55   ; OUTI
site 01B57   ; OUT ($BE),A
site 01B59   ; OUTI
site 01B5B   ; OUT ($BE),A
site 01B5D   ; OUTI
site 01B5F   ; OUT ($BE),A
site 01B61   ; OUTI
site 01B63   ; OUT ($BE),A
site 01B65   ; OUTI
site 01B67   ; OUT ($BE),A
site 01B69   ; OUTI
site 01B6B   ; OUT ($BE),A
site 01B6D   ; OUTI
site 01B6F   ; OUT ($BE),A
site 01B71   ; OUTI
site 01B73   ; OUT ($BE),A
site 01B75   ; OUTI
site 01B77   ; OUT ($BE),A
site 01B79   ; OUTI
site 01B7B   ; OUT ($BE),A
site 01B7D   ; OUTI
site 01B7F   ; OUT ($BE),A
site 01B81   ; OUTI
site 01B83   ; OUT ($BE),A
site 01B85   ; OUTI
site 01B87   ; OUT ($BE),A
site 01B89   ; OUTI
site 01B8B   ; OUT ($BE),A
site 01B8D   ; OUTI
site 01B8F   ; OUT ($BE),A
site 01B91   ; OUTI
site 01B93   ; OUT ($BE),A
site 01B95   ; OUTI
site 01B97   ; OUT ($BE),A
site 01B99   ; OUTI
site 01B9B   ; OUT ($BE),A
site 01B9D   ; OUTI
site 01B9F   ; OUT ($BE),A
site 01BA1   ; OUTI
site 01BA3   ; OUT ($BE),A
site 01BA5   ; OUTI
site 01BA7   ; OUT ($BE),A
site 01BA9   ; OUTI
site 01BAB   ; OUT ($BE),A
site 01BAD   ; OUTI
site 01BAF   ; OUT ($BE),A
site 01BB1   ; OUTI
site 01BB3   ; OUT ($BE),A
site 01BB5   ; OUTI
site 01BB7   ; OUT ($BE),A
site 01BB9   ; OUTI
site 01BBB   ; OUT ($BE),A
site 01BBD   ; OUTI
site 01BBF   ; OUT ($BE),A
site 01BC1   ; OUTI
site 01BC3   ; OUT ($BE),A
site 01BC5   ; OUTI
site 01BC7   ; OUT ($BE),A
site 01BC9   ; OUTI
site 01BCB   ; OUT ($BE),A
site 01BCD   ; OUTI
site 01BCF   ; OUT ($BE),A
site 01BD1   ; OUTI
site 01BD3   ; OUT ($BE),A
site 01BD5   ; OUTI
site 01BD7   ; OUT ($BE),A
site 01BD9   ; OUTI
site 01BDB   ; OUT ($BE),A
site 01BDD   ; OUTI
site 01BDF   ; OUT ($BE),A
site 01BE1   ; OUTI
site 01BE3   ; OUT ($BE),A
site 01BE5   ; OUTI
site 01BE7   ; OUT ($BE),A
site 01BE9   ; OUTI
site 01BEB   ; OUT ($BE),A
site 01BED   ; OUTI
site 01BEF   ; OUT ($BE),A
site 01BF1   ; OUTI
site 01BF3   ; OUT ($BE),A
site 01BF5   ; OUTI
site 01BF7   ; OUT ($BE),A
site 01BF9   ; OUTI
site 01BFB   ; OUT ($BE),A
site 01BFD   ; OUTI
site 01BFF   ; OUT ($BE),A
site 01C01   ; OUTI
site 01C03   ; OUT ($BE),A
site 01C05   ; OUTI
site 01C07   ; OUT ($BE),A
site 01C09   ; OUTI
site 01C0B   ; OUT ($BE),A
site 01C0D   ; OUTI
site 01C0F   ; OUT ($BE),A
site 01C11   ; OUTI
site 01C13   ; OUT ($BE),A
site 01C15   ; OUTI
site 01C17   ; OUT ($BE),A
site 01C19   ; OUTI
site 01C1B   ; OUT ($BE),A
site 01C1D   ; OUTI
site 01C1F   ; OUT ($BE),A
site 01C21   ; OUTI
site 01C23   ; OUT ($BE),A
site 01C25   ; OUTI
site 01C27   ; OUT ($BE),A
site 01C29   ; OUTI
site 01C2B   ; OUT ($BE),A
site 01C2D   ; OUTI
site 01C2F   ; OUT ($BE),A
site 01C31   ; OUTI
site 01C33   ; OUT ($BE),A
site 01C35   ; OUTI
site 01C37   ; OUT ($BE),A
site 01C39   ; OUTI
site 01C3B   ; OUT ($BE),A
site 01C3D   ; OUTI
site 01C3F   ; OUT ($BE),A
site 01C41   ; OUTI
site 01C43   ; OUT ($BE),A
site 01C45   ; OUTI
site 01C47   ; OUT ($BE),A
site 01C49   ; OUTI
site 01C4B   ; OUT ($BE),A
site 01C4D   ; OUTI
site 01C4F   ; OUT ($BE),A
site 01C51   ; OUTI
site 01C53   ; OUT ($BE),A
site 01C55   ; OUTI
site 01C57   ; OUT ($BE),A
site 01C59   ; OUTI
site 01C5B   ; OUT ($BE),A
site 01C5D   ; OUTI
site 01C5F   ; OUT ($BE),A
site 01C61   ; OUTI
site 01C63   ; OUT ($BE),A
site 01C65   ; OUTI
site 01C67   ; OUT ($BE),A
site 01C69   ; OUTI
site 01C6B   ; OUT ($BE),A
site 01C6D   ; OUTI
site 01C6F   ; OUT ($BE),A
site 01C71   ; OUTI
site 01C73   ; OUT ($BE),A
site 01C75   ; OUTI
site 01C77   ; OUT ($BE),A
site 01C79   ; OUTI
site 01C7B   ; OUT ($BE),A
site 01C7D   ; OUTI
site 01C7F   ; OUT ($BE),A
site 01C81   ; OUTI
site 01C83   ; OUT ($BE),A
site 01C85   ; OUTI
site 01C87   ; OUT ($BE),A
site 01C89   ; OUTI
site 01C8B   ; OUT ($BE),A
site 01C8D   ; OUTI
site 01C8F   ; OUT ($BE),A
site 01C91   ; OUTI
site 01C93   ; OUT ($BE),A
site 01C95   ; OUTI
site 01C97   ; OUT ($BE),A
site 01C99   ; OUTI
site 01C9B   ; OUT ($BE),A
site 01C9D   ; OUTI
site 01C9F   ; OUT ($BE),A
site 01CA1   ; OUTI
site 01CA3   ; OUT ($BE),A
site 01CA5   ; OUTI
site 01CA7   ; OUT ($BE),A
site 01CA9   ; OUTI
site 01CAB   ; OUT ($BE),A
site 01CAD   ; OUTI
site 01CAF   ; OUT ($BE),A
site 01CB1   ; OUTI
site 01CB3   ; OUT ($BE),A
site 01CB5   ; OUTI
site 01CB7   ; OUT ($BE),A
site 01CB9   ; OUTI
site 01CBB   ; OUT ($BE),A
site 01CBD   ; OUTI
site 01CBF   ; OUT ($BE),A
site 01CC1   ; OUTI
site 01CC3   ; OUT ($BE),A
site 01CC5   ; OUTI
site 01CC7   ; OUT ($BE),A
site 01CC9   ; OUTI
site 01CCB   ; OUT ($BE),A
site 01CCD   ; OUTI
site 01CCF   ; OUT ($BE),A
site 01CD1   ; OUTI
site 01CD3   ; OUT ($BE),A
site 01CD5   ; OUTI
site 01CD7   ; OUT ($BE),A
site 01CD9   ; OUTI
site 01CDB   ; OUT ($BE),A
site 01CDD   ; OUTI
site 01CDF   ; OUT ($BE),A
site 01CE1   ; OUTI
site 01CE3   ; OUT ($BE),A
site 01CE5   ; OUTI
site 01CE7   ; OUT ($BE),A
site 01CE9   ; OUTI
site 01CEB   ; OUT ($BE),A
site 01CED   ; OUTI
site 01CEF   ; OUT ($BE),A
site 01CF1   ; OUTI
site 01CF3   ; OUT ($BE),A
site 01CF5   ; OUTI
site 01CF7   ; OUT ($BE),A
site 01CF9   ; OUTI
site 01CFB   ; OUT ($BE),A
site 01CFD   ; OUTI
site 01CFF   ; OUT ($BE),A
site 01D01   ; OUTI
site 01D03   ; OUT ($BE),A
site 01D05   ; OUTI
site 01D07   ; OUT ($BE),A
site 01D09   ; OUTI
site 01D0B   ; OUT ($BE),A
site 01D0D   ; OUTI
site 01D0F   ; OUT ($BE),A
site 01D11   ; OUTI
site 01D13   ; OUT ($BE),A
site 01D15   ; OUTI
site 01D17   ; OUT ($BE),A
site 01D19   ; OUTI
site 01D1B   ; OUT ($BE),A
site 01D1D   ; OUTI
site 01D1F   ; OUT ($BE),A
site 01D21   ; OUTI
site 01D23   ; OUT ($BE),A
site 01D25   ; OUTI
site 01D27   ; OUT ($BE),A
site 01D29   ; OUTI
site 01D2B   ; OUT ($BE),A
site 01D2D   ; OUTI
site 01D2F   ; OUT ($BE),A
site 01D31   ; OUTI
site 01D33   ; OUT ($BE),A
site 01D35   ; OUTI
site 01D37   ; OUT ($BE),A
site 01D39   ; OUTI
site 01D3B   ; OUT ($BE),A
site 01D3D   ; OUTI
site 01D3F   ; OUT ($BE),A
site 01D41   ; OUTI
site 01D43   ; OUT ($BE),A
site 01D45   ; OUTI
site 01D47   ; OUT ($BE),A
site 01D49   ; OUTI
site 01D4B   ; OUT ($BE),A
site 01D4D   ; OUTI
site 01D4F   ; OUT ($BE),A
site 01D51   ; OUTI
site 01D53   ; OUT ($BE),A
site 01D55   ; OUTI
site 01D57   ; OUT ($BE),A
site 01D59   ; OUTI
site 01D5B   ; OUT ($BE),A
site 01D5D   ; OUTI
site 01D5F   ; OUT ($BE),A
site 01D61   ; OUTI
site 01D63   ; OUT ($BE),A
site 01D65   ; OUTI
site 01D67   ; OUT ($BE),A
site 01D69   ; OUTI
site 01D6B   ; OUT ($BE),A
site 01D6D   ; OUTI
site 01D6F   ; OUT ($BE),A
site 01D71   ; OUTI
site 01D73   ; OUT ($BE),A
site 01D75   ; OUTI
site 01D77   ; OUT ($BE),A
site 01D79   ; OUTI
site 01D7B   ; OUT ($BE),A
site 01D7D   ; OUTI
site 01D7F   ; OUT ($BE),A
site 01D81   ; OUTI
site 01D83   ; OUT ($BE),A
site 01D85   ; OUTI
site 01D87   ; OUT ($BE),A
site 01D89   ; OUTI
site 01D8B   ; OUT ($BE),A
site 01D8D   ; OUTI
site 01D8F   ; OUT ($BE),A
site 01D91   ; OUTI
site 01D93   ; OUT ($BE),A
site 01D95   ; OUTI
site 01D97   ; OUT ($BE),A
site 01D99   ; OUTI
site 01D9B   ; OUT ($BE),A
site 01D9D   ; OUTI
site 01D9F   ; OUT ($BE),A
site 01DA1   ; OUTI
site 01DA3   ; OUT ($BE),A
site 01DA5   ; OUTI
site 01DA7   ; OUT ($BE),A
site 01DA9   ; OUTI
site 01DAB   ; OUT ($BE),A
site 01DAD   ; OUTI
site 01DAF   ; OUT ($BE),A
site 01DB1   ; OUTI
site 01DB3   ; OUT ($BE),A
site 01DB5   ; OUTI
site 01DB7   ; OUT ($BE),A
site 01DB9   ; OUTI
site 01DBB   ; OUT ($BE),A
site 01DBD   ; OUTI
site 01DBF   ; OUT ($BE),A
site 01DC1   ; OUTI
site 01DC3   ; OUT ($BE),A
site 01DC5   ; OUTI
site 01DC7   ; OUT ($BE),A
site 01DC9   ; OUTI
site 01DCB   ; OUT ($BE),A
site 01DCD   ; OUTI
site 01DCF   ; OUT ($BE),A
site 01DD1   ; OUTI
site 01DD3   ; OUT ($BE),A
site 01DD5   ; OUTI
site 01DD7   ; OUT ($BE),A
site 01DD9   ; OUTI
site 01DDB   ; OUT ($BE),A
site 01DDD   ; OUTI
site 01DDF   ; OUT ($BE),A
site 01DE1   ; OUTI
site 01DE3   ; OUT ($BE),A
site 01DE5   ; OUTI
site 01DE7   ; OUT ($BE),A
site 01DE9   ; OUTI
site 01DEB   ; OUT ($BE),A
site 01DED   ; OUTI
site 01DEF   ; OUT ($BE),A
site 01DF1   ; OUTI
site 01DF3   ; OUT ($BE),A
site 01DF5   ; OUTI
site 01DF7   ; OUT ($BE),A
site 01DF9   ; OUTI
site 01DFB   ; OUT ($BE),A
site 01DFD   ; OUTI
site 01DFF   ; OUT ($BE),A
site 01E01   ; OUTI
site 01E03   ; OUT ($BE),A
site 01E05   ; OUTI
site 01E07   ; OUT ($BE),A
site 01E09   ; OUTI
site 01E0B   ; OUT ($BE),A
site 01E0D   ; OUTI
site 01E0F   ; OUT ($BE),A
site 01E11   ; OUTI
site 01E13   ; OUT ($BE),A
site 01E15   ; OUTI
site 01E17   ; OUT ($BE),A
site 01E19   ; OUTI
site 01E1B   ; OUT ($BE),A
site 01E1D   ; OUTI
site 01E1F   ; OUT ($BE),A
site 01E21   ; OUTI
site 01E23   ; OUT ($BE),A
site 01E25   ; OUTI
site 01E27   ; OUT ($BE),A
site 01E29   ; OUTI
site 01E2B   ; OUT ($BE),A
site 01E2D   ; OUTI
site 01E2F   ; OUT ($BE),A
site 01E31   ; OUTI
site 01E33   ; OUT ($BE),A
site 01E35   ; OUTI
site 01E37   ; OUT ($BE),A
site 01E39   ; OUTI
site 01E3B   ; OUT ($BE),A
site 01E3D   ; OUTI
site 01E3F   ; OUT ($BE),A
site 01E41   ; OUTI
site 01E43   ; OUT ($BE),A
site 01E45   ; OUTI
site 01E47   ; OUT ($BE),A
site 01E49   ; OUTI
site 01E4B   ; OUT ($BE),A
site 01E4D   ; OUTI
site 01E4F   ; OUT ($BE),A
site 01E51   ; OUTI
site 01E53   ; OUT ($BE),A
site 01E55   ; OUTI
site 01E57   ; OUT ($BE),A
site 01E59   ; OUTI
site 01E5B   ; OUT ($BE),A
site 01E5D   ; OUTI
site 01E5F   ; OUT ($BE),A
site 01E61   ; OUTI
site 01E63   ; OUT ($BE),A
site 01E65   ; OUTI
site 01E67   ; OUT ($BE),A
site 01E69   ; OUTI
site 01E6B   ; OUT ($BE),A
site 01E6D   ; OUTI
site 01E6F   ; OUT ($BE),A
site 01E71   ; OUTI
site 01E73   ; OUT ($BE),A
site 01E75   ; OUTI
site 01E77   ; OUT ($BE),A
site 01E79   ; OUTI
site 01E7B   ; OUT ($BE),A
site 01E7D   ; OUTI
site 01E7F   ; OUT ($BE),A
site 01E81   ; OUTI
site 01E83   ; OUT ($BE),A
site 01E85   ; OUTI
site 01E87   ; OUT ($BE),A
site 01E89   ; OUTI
site 01E8B   ; OUT ($BE),A
site 01E8D   ; OUTI
site 01E8F   ; OUT ($BE),A
site 01E91   ; OUTI
site 01E93   ; OUT ($BE),A
site 01E95   ; OUTI
site 01E97   ; OUT ($BE),A
site 01E99   ; OUTI
site 01E9B   ; OUT ($BE),A
site 01E9D   ; OUTI
site 01E9F   ; OUT ($BE),A
site 01EA1   ; OUTI
site 01EA3   ; OUT ($BE),A
site 01EA5   ; OUTI
site 01EA7   ; OUT ($BE),A
site 01EA9   ; OUTI
site 01EAB   ; OUT ($BE),A
site 01EAD   ; OUTI
site 01EAF   ; OUT ($BE),A
site 01EB1   ; OUTI
site 01EB3   ; OUT ($BE),A
site 01EB5   ; OUTI
site 01EB7   ; OUT ($BE),A
site 01EB9   ; OUTI
site 01EBB   ; OUT ($BE),A
site 01EBD   ; OUTI
site 01EBF   ; OUT ($BE),A
site 01EC1   ; OUTI
site 01EC3   ; OUT ($BE),A
site 01EC5   ; OUTI
site 01EC7   ; OUT ($BE),A
site 01EC9   ; OUTI
site 01ECB   ; OUT ($BE),A
site 01ECD   ; OUTI
site 01ECF   ; OUT ($BE),A
site 01ED1   ; OUTI
site 01ED3   ; OUT ($BE),A
site 01ED5   ; OUTI
site 01ED7   ; OUT ($BE),A
site 01ED9   ; OUTI
site 01EDB   ; OUT ($BE),A
site 01EDD   ; OUTI
site 01EDF   ; OUT ($BE),A
site 01EE1   ; OUTI
site 01EE3   ; OUT ($BE),A
site 01EE5   ; OUTI
site 01EE7   ; OUT ($BE),A
site 01EE9   ; OUTI
site 01EEB   ; OUT ($BE),A
site 01EED   ; OUTI
site 01EEF   ; OUT ($BE),A
site 01EF1   ; OUTI
site 01EF3   ; OUT ($BE),A
site 01EF5   ; OUTI
site 01EF7   ; OUT ($BE),A
site 01EF9   ; OUTI
site 01EFB   ; OUT ($BE),A
site 01EFD   ; OUTI
site 01EFF   ; OUT ($BE),A
site 01F01   ; OUTI
site 01F03   ; OUT ($BE),A
site 01F05   ; OUTI
site 01F07   ; OUT ($BE),A
site 01F09   ; OUTI
site 01F0B   ; OUT ($BE),A
site 01F0D   ; OUTI
site 01F0F   ; OUT ($BE),A
site 01F11   ; OUTI
site 01F13   ; OUT ($BE),A
site 01F15   ; OUTI
site 01F17   ; OUT ($BE),A
site 01F19   ; OUTI
site 01F1B   ; OUT ($BE),A
site 01F1D   ; OUTI
site 01F1F   ; OUT ($BE),A
site 01F21   ; OUTI
site 01F23   ; OUT ($BE),A
site 01F25   ; OUTI
site 01F27   ; OUT ($BE),A
site 01F29   ; OUTI
site 01F2B   ; OUT ($BE),A
site 01F2D   ; OUTI
site 01F2F   ; OUT ($BE),A
site 01F31   ; OUTI
site 01F33   ; OUT ($BE),A
site 01F35   ; OUTI
site 01F37   ; OUT ($BE),A
site 01F39   ; OUTI
site 01F3B   ; OUT ($BE),A
site 01F3D   ; OUTI
site 01F3F   ; OUT ($BE),A
site 01F41   ; OUTI
site 01F43   ; OUT ($BE),A
site 01F45   ; OUTI
site 01F47   ; OUT ($BE),A
site 01F49   ; OUTI
site 01F4B   ; OUT ($BE),A
site 01F4D   ; OUTI
site 01F4F   ; OUT ($BE),A
site 01F51   ; OUTI
site 01F53   ; OUT ($BE),A
site 01F55   ; OUTI
site 01F57   ; OUT ($BE),A
site 01F59   ; OUTI
site 01F5B   ; OUT ($BE),A
site 01F5D   ; OUTI
site 01F5F   ; OUT ($BE),A
site 01F61   ; OUTI
site 01F63   ; OUT ($BE),A
site 01F65   ; OUTI
site 01F67   ; OUT ($BE),A
site 01F69   ; OUTI
site 01F6B   ; OUT ($BE),A
site 01F6D   ; OUTI
site 01F6F   ; OUT ($BE),A
site 01F71   ; OUTI
site 01F73   ; OUT ($BE),A
site 01F75   ; OUTI
site 01F77   ; OUT ($BE),A
site 01F79   ; OUTI
site 01F7B   ; OUT ($BE),A
site 01F7D   ; OUTI
site 01F7F   ; OUT ($BE),A
site 01F81   ; OUTI
site 01F83   ; OUT ($BE),A
site 01F85   ; OUTI
site 01F87   ; OUT ($BE),A
site 01F89   ; OUTI
site 01F8B   ; OUT ($BE),A
site 01F8D   ; OUTI
site 01F8F   ; OUT ($BE),A
site 01F91   ; OUTI
site 01F93   ; OUT ($BE),A
site 01F95   ; OUTI
site 01F97   ; OUT ($BE),A
site 01F99   ; OUTI
site 01F9B   ; OUT ($BE),A
site 01F9D   ; OUTI
site 01F9F   ; OUT ($BE),A
site 01FA1   ; OUTI
site 01FA3   ; OUT ($BE),A
site 01FA5   ; OUTI
site 01FA7   ; OUT ($BE),A
site 01FA9   ; OUTI
site 01FAB   ; OUT ($BE),A
site 01FAD   ; OUTI
site 01FAF   ; OUT ($BE),A
site 01FB1   ; OUTI
site 01FB3   ; OUT ($BE),A
site 01FB5   ; OUTI
site 01FB7   ; OUT ($BE),A
site 01FB9   ; OUTI
site 01FBB   ; OUT ($BE),A
site 01FBD   ; OUTI
site 01FBF   ; OUT ($BE),A
site 01FC1   ; OUTI
site 01FC3   ; OUT ($BE),A
site 01FC5   ; OUTI
site 01FC7   ; OUT ($BE),A
site 01FC9   ; OUTI
site 01FCB   ; OUT ($BE),A
site 01FCD   ; OUTI
site 01FCF   ; OUT ($BE),A
site 01FD1   ; OUTI
site 01FD3   ; OUT ($BE),A
site 01FD5   ; OUTI
site 01FD7   ; OUT ($BE),A
site 01FD9   ; OUTI
site 01FDB   ; OUT ($BE),A
site 01FDD   ; OUTI
site 01FDF   ; OUT ($BE),A
site 01FE1   ; OUTI
site 01FE3   ; OUT ($BE),A
site 01FE5   ; OUTI
site 01FE7   ; OUT ($BE),A
site 01FE9   ; OUTI
site 01FEB   ; OUT ($BE),A
site 01FED   ; OUTI
site 01FEF   ; OUT ($BE),A
site 01FF1   ; OUTI
site 01FF3   ; OUT ($BE),A
site 01FF5   ; OUTI
site 01FF7   ; OUT ($BE),A
site 01FF9   ; OUTI
site 01FFB   ; OUT ($BE),A
site 01FFD   ; OUTI
site 01FFF   ; OUT ($BE),A
site 02001   ; OUTI
site 02003   ; OUT ($BE),A
site 02005   ; OUTI
site 02007   ; OUT ($BE),A
site 02009   ; OUTI
site 0200B   ; OUT ($BE),A
site 0200D   ; OUTI
site 0200F   ; OUT ($BE),A
site 02011   ; OUTI
site 02013   ; OUT ($BE),A
site 02015   ; OUTI
site 02017   ; OUT ($BE),A
site 02019   ; OUTI
site 0201B   ; OUT ($BE),A
site 0201D   ; OUTI
site 0201F   ; OUT ($BE),A
site 02021   ; OUTI
site 02023   ; OUT ($BE),A
site 02025   ; OUTI
site 02027   ; OUT ($BE),A
site 02029   ; OUTI
site 0202B   ; OUT ($BE),A
site 0202D   ; OUTI
site 0202F   ; OUT ($BE),A
site 02031   ; OUTI
site 02033   ; OUT ($BE),A
site 02035   ; OUTI
site 02037   ; OUT ($BE),A
site 02039   ; OUTI
site 0203B   ; OUT ($BE),A
site 0203D   ; OUTI
site 0203F   ; OUT ($BE),A
site 02041   ; OUTI
site 02043   ; OUT ($BE),A
site 02045   ; OUTI
site 02047   ; OUT ($BE),A
site 02049   ; OUTI
site 0204B   ; OUT ($BE),A
site 0204D   ; OUTI
site 0204F   ; OUT ($BE),A
site 02051   ; OUTI
site 02053   ; OUT ($BE),A
site 02055   ; OUTI
site 02057   ; OUT ($BE),A
site 02059   ; OUTI
site 0205B   ; OUT ($BE),A
site 0205D   ; OUTI
site 0205F   ; OUT ($BE),A
site 02061   ; OUTI
site 02063   ; OUT ($BE),A
site 02065   ; OUTI
site 02067   ; OUT ($BE),A
site 02069   ; OUTI
site 0206B   ; OUT ($BE),A
site 0206D   ; OUTI
site 0206F   ; OUT ($BE),A
site 02071   ; OUTI
site 02073   ; OUT ($BE),A
site 02075   ; OUTI
site 02077   ; OUT ($BE),A
site 02079   ; OUTI
site 0207B   ; OUT ($BE),A
site 0207D   ; OUTI
site 0207F   ; OUT ($BE),A
site 02081   ; OUTI
site 02083   ; OUT ($BE),A
site 02085   ; OUTI
site 02087   ; OUT ($BE),A
site 02089   ; OUTI
site 0208B   ; OUT ($BE),A
site 0208D   ; OUTI
site 0208F   ; OUT ($BE),A
site 02091   ; OUTI
site 02093   ; OUT ($BE),A
site 02095   ; OUTI
site 02097   ; OUT ($BE),A
site 020A2   ; OUT ($BE),A
site 03591   ; OUT ($BF),A
site 03595   ; OUT ($BF),A
site 03599   ; OUT ($BF),A
site 0359D   ; OUT ($BF),A
site 03623   ; OUT ($7F),A
site 03626   ; OUT ($7F),A
site 03690   ; OUT ($BF),A
site 03694   ; OUT ($BF),A
otir 0369C   ; OUTI
site 036A3   ; OUT ($BF),A
site 036A7   ; OUT ($BF),A
otir 036AE   ; OUTI
site 03706   ; OUT ($BF),A
site 0370A   ; OUT ($BF),A
site 060D0   ; OUT ($BF),A
site 060D4   ; OUT ($BF),A
site 060D8   ; OUT ($BF),A
site 060DC   ; OUT ($BF),A
site 060DF   ; OUT ($BF),A
site 060E3   ; OUT ($BF),A
site 060E7   ; OUT ($BE),A
site 061EB   ; OUT ($BF),A
site 061EF   ; OUT ($BF),A
site 0621A   ; OUT ($BF),A
site 0621E   ; OUT ($BF),A
site 70153   ; OUT ($F0),A
site 7015C   ; OUT ($F1),A
site 70174   ; OUT ($7F),A
site 70184   ; OUT (C),D
site 7018A   ; OUT ($F1),A
site 701BD   ; OTIR
site 701CB   ; OTIR
site 701D5   ; OUT ($F0),A
site 701DB   ; OUT ($F1),A
site 701E6   ; OUTI
site 701ED   ; OUTI
site 7031B   ; OUT ($7F),A
site 70343   ; OUT ($7F),A
site 70347   ; OUT ($7F),A
site 7034A   ; OUT ($7F),A
site 703B0   ; OUT ($F0),A
site 703B7   ; OUT ($F1),A
site 703BF   ; OUT ($F0),A
site 703C5   ; OUT ($F1),A
site 704BA   ; OUT ($F0),A
site 704C4   ; OUT (C),L
site 704CD   ; OUT ($F0),A
site 704E8   ; OUT (C),H
site 704F0   ; OUT ($F0),A
site 704FE   ; OUT ($F1),A
site 7050A   ; OUT ($F0),A
site 70513   ; OUT ($F1),A
site 706D4   ; OUT ($F0),A
site 706DA   ; OUTI
site 70745   ; OUT ($7F),A
site 70836   ; OUT ($7F),A
site 7083A   ; OUT ($7F),A
site 70857   ; OUT ($7F),A
site 70881   ; OUT ($7F),A
site 70894   ; OUT ($F0),A
site 7089F   ; OUT ($F1),A
site 708B0   ; OUT ($F0),A
site 708BE   ; OUT ($F1),A
site 7094A   ; OUTI
site 7094C   ; OUTI
site 7094E   ; OUTI
site 70950   ; OUTI
site 70952   ; OUTI
site 70954   ; OUTI
site 70956   ; OUTI
site 70958   ; OUTI
site 7095A   ; OUTI
site 7095C   ; OUTI
site 7095E   ; OUTI
site 70968   ; OUT (C),D
site 7096E   ; OUT ($F1),A
site 709AD   ; OUT ($7F),A
site 70A03   ; OUT ($7F),A
site 70A8D   ; OUT ($7F),A
site 70AAD   ; OUT ($7F),A
site 70AED   ; OUT ($7F),A
site 70AF7   ; OUT ($7F),A
site 70B3F   ; OUT ($7F),A
site 72DE9   ; OUT ($7F),A
site 72DEC   ; OUT ($F2),A
site 72E06   ; OUT ($7F),A
site 72E16   ; OUT ($F2),A
mapldk 00099   # LD HL,$FFFC; LD (HL),$80
maphl 0009F   # LD (HL),$00, HL = $FFFD
maphl 000A2   # LD (HL),$01, HL = $FFFE
maphl 000A5   # LD (HL),$02, HL = $FFFF
mapst 000C5   ; LD ($FFFF),A
mapst 00179   ; LD ($FFFF),A
mapst 001B0   ; LD ($FFFF),A
mapst 00353   ; LD ($FFFF),A
mapst 00368   ; LD ($FFFF),A
mapst 00423   ; LD ($FFFF),A
mapst 0043F   ; LD ($FFFF),A
mapst 00446   ; LD ($FFFF),A
mapst 0060C   ; LD ($FFFF),A
mapst 0073F   ; LD ($FFFF),A
mapst 00746   ; LD ($FFFF),A
mapst 00768   ; LD ($FFFF),A
mapst 0076F   ; LD ($FFFF),A
mapst 007A0   ; LD ($FFFF),A
mapst 007A7   ; LD ($FFFF),A
mapst 00802   ; LD ($FFFF),A
mapst 00809   ; LD ($FFFF),A
mapst 00861   ; LD ($FFFF),A
mapst 00868   ; LD ($FFFF),A
mapst 00898   ; LD ($FFFF),A
mapst 0089F   ; LD ($FFFF),A
mapst 020FC   ; LD ($FFFF),A
mapst 02162   ; LD ($FFFF),A
mapst 023DF   ; LD ($FFFF),A
mapst 02ADF   ; LD ($FFFF),A
mapst 02B0B   ; LD ($FFFF),A
mapst 02B23   ; LD ($FFFF),A
mapst 02C4C   ; LD ($FFFF),A
mapst 02DAA   ; LD ($FFFF),A
mapst 02F4F   ; LD ($FFFF),A
mapst 0300A   ; LD ($FFFF),A
mapst 0301D   ; LD ($FFFF),A
mapst 03465   ; LD ($FFFF),A
mapst 0358C   ; LD ($FFFF),A
mapst 0361E   ; LD ($FFFF),A
mapst 03640   ; LD ($FFFF),A
mapst 03647   ; LD ($FFFF),A
mapst 04024   ; LD ($FFFF),A
mapst 04127   ; LD ($FFFF),A
mapst 041E4   ; LD ($FFFF),A
mapst 04393   ; LD ($FFFF),A
mapst 043CD   ; LD ($FFFF),A
mapst 04654   ; LD ($FFFF),A
mapst 04693   ; LD ($FFFF),A
mapst 0469B   ; LD ($FFFF),A
mapst 046C1   ; LD ($FFFF),A
mapst 0610D   ; LD ($FFFF),A
mapst 06159   ; LD ($FFFF),A
mapst 061C8   ; LD ($FFFF),A
mapst 061CF   ; LD ($FFFF),A
mapst 063CB   ; LD ($FFFF),A
mapst 063E0   ; LD ($FFFF),A
mapst 0643C   ; LD ($FFFF),A
mapst 064A3   ; LD ($FFFF),A
mapst 064AA   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
# 05FA0 (22 FC FF): sprite layout table data in bank 1 (records of tile and offset bytes), not code.
# CHECK byte scan low: mapst 183FB  LD ($FFFF),A  (5 RST or NOP opcodes around it (looks like data))
# CHECK byte scan low: mapst 1C404  LD ($FFFF),A  (no valid code after it)
# CHECK byte scan low: mapst 2D031  LD ($FFFF),A  (8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK byte scan low: mapst 3C41C  LD ($FFFE),A  (5 RST or NOP opcodes around it (looks like data))
# CHECK byte scan low: mapst 47B8E  LD ($FFFD),A  (5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 0099A  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 0099F  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 009A6  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK high: site 009AD  OUT ($BE),A  (vdp_data; after LD A,($C003); 32 bytes of valid code before it)
# CHECK high: site 009BD  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $009C8; 32 bytes of valid code before it)
# CHECK high: site 009C4  OUT ($BE),A  (vdp_data; after LD A,($C003); 32 bytes of valid code before it)
# CHECK high: site 009D1  IN A,($BE)  (vdp_data; branch target from $009D8; 32 bytes of valid code before it)
# CHECK high: site 00A40  OUT ($BE),A  (vdp_data; branch target from $00A3D; 32 bytes of valid code before it)
# CHECK medium: site 05226  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 141BF  IN A,($F0)  (joypad_a; 6 RST or NOP opcodes around it (looks like data); 23 bytes of valid code before it)
# CHECK low: site 1C94B  IN A,($3F)  (unmapped_read; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 31AC3  IN A,($F0)  (joypad_a; no evidence)
# CHECK low: site 3ABFD  IN H,(C)  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 3C3FD  OUT ($7F),A  (psg; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 40213  IN D,(C)  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 40553  IN D,(C)  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 48417  OUT ($C0),A  (no_effect; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 49F1C  OUT (C),B  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 4C99C  OUT ($BF),A  (vdp_control; 7 RST or NOP opcodes around it (looks like data); 31 bytes of valid code before it)
# CHECK low: site 59071  IN A,($7E)  (v_counter; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5CA4B  IN A,($DC)  (joypad_a; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 5CBE3  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 5EE24  IN A,($C0)  (joypad_a; no evidence)
# CHECK low: site 5EF59  IN A,($7E)  (v_counter; 6 RST or NOP opcodes around it (looks like data); 26 bytes of valid code before it)
# CHECK low: site 66107  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 6821C  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 68D0B  IN A,($BF)  (vdp_status; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6C069  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 6D520  IN A,($F0)  (joypad_a; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6D569  IN A,($F1)  (joypad_b_misc; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 6DF77  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK low: site 7434B  IN A,($7E)  (v_counter; 32 bytes of valid code before it; no valid code after it)

# The frame handler draws each game step over several frames (states 5-8 in $C001), with
# unrolled OUTI chains and OUTI loops from RAM into VRAM: tiles at $0000 or $2000 (the half
# the name table does not show, $C020), and the whole name table at $3800. Through the traps
# a step's uploads took more than a frame in most handler states, so the game ran late. Each
# uploader is a page 0 entry that writes the same bytes with jt_vwrite. The 3-plane tiles
# (three bytes from RAM, then A = 0) and the name table (a byte from RAM, then A) are first
# laid out in a buffer in the page, so each upload is one or two jt_vwrite calls.
asm 00AD2 6          ; LD C,$BE : 2 of the 896 OUTI to the RET at $11D4 (state 5 from $C800, state 6 from $D180)
    rst $18
    db far_io, pg_e896, ent_e896
    ret
endasm
asm 011D5 5          ; LD BC,$00BE : OUTI: 6 loops of 256 OUTI to the RET at $11FB (state 5)
    rst $18
    db far_io, pg_e1536, ent_e1536
    ret
endasm
asm 0077E 6          ; LD BC,$00BE : CALL $11EA: the last 3 loops of 256 OUTI (state 6)
    rst $18
    db far_io, pg_e768, ent_e768
endasm
asm 011FC 6          ; LD BC,$C0BE : XOR A : OUTI: 192 passes of 3 OUTI and OUT ($BE),A (state 6, from $D800)
    rst $18
    db far_io, pg_e3z192, ent_e3z192
    ret
endasm
asm 007B6 7          ; LD BC,$68BE : XOR A : CALL $1200: 104 passes of the same loop (state 7)
    rst $18
    db far_io, pg_e3z104, ent_e3z104
endasm
asm 01213 5          ; LD C,$BE : XOR A : OUTI: 208 groups of 3 OUTI and OUT ($BE),A to the RET at $1896 (state 7, from $DA40)
    rst $18
    db far_io, pg_eq3, ent_eq3
    ret
endasm
asm 01897 6          ; LD C,$BE : OUTI : OUT ($BE),A: 512 name table cells to the RET at $2099 (state 8, rows 0-15)
    rst $18
    db far_io, pg_ent512, ent_ent512
    ret
endasm
asm 0209A 6          ; LD BC,$00BE : OUTI : DEC DE: 256 passes of OUTI and OUT ($BE),A (state 8, rows 16-23)
    rst $18
    db far_io, pg_ent256, ent_ent256
    ret
endasm
# Game speed. A game step is the main loop's $05D3: it builds the next picture in RAM while
# the frame handler uploads the last one (states 5 to 8), and it ends at $0669, when the
# handler has reached state 9. On the Master System the main loop's work takes longer than
# the four handler frames, so a step takes 4 to 7 frames by its load (reference: mostly 5 or
# 6 at 60 Hz). At 28 MHz the work ends in time and every step took 4 frames. The entries
# st_s to st_d time the main loop's work with the Next's raster line, with interrupts off
# while it runs (W1: $05D3 to the wait at $062C; W2: $0636 to $0669), turn it into
# Master System T-states, and work out the frame in which a Master System running at the
# Next's video rate ends the step: each frame gives the main loop the frame's T-states less
# the frame handler's for that state. The wait at $0669 then sees state 9 only from that
# frame on.
label cave_s 00020
asm 005D3 6          ; CALL $26CA : LD HL,$C022: the step starts
    call cave_s
endasm
asm 00020 11         ; free bytes ($FF) between the RST vectors
    rst $18
    db far_io, pg_st_s, ent_st_s
    call $26CA
    ld hl,$C022
    ret
endasm
asm 0062C 5          ; LD A,($C001) : CP $07: the wait for state 7 (W1 ends)
    rst $18
    db far_io, pg_st_a, ent_st_a
    nop
endasm
asm 00636 6          ; LD A,(HL) : INC HL : OR A : JP NZ,$068F (W2 starts)
    rst $18
    db far_io, pg_st_b, ent_st_b
    jr nz,$068F
endasm
asm 00669 5          ; LD A,($C001) : CP $09: the wait for state 9 (W2 ends; the step's pacing)
    rst $18
    db far_io, pg_st_d, ent_st_d
    nop
endasm
page 0 e896 e1536 e768 e3z192 e3z104 eq3 ent512 ent256 st_s st_a st_b st_d
; Every entry runs in the frame handler, with interrupts off; each keeps the interrupt state
; it finds all the same. Each runs on a stack in this page and returns the registers the
; game's own code leaves (flags are not kept: no caller tests them). Runtime internals used:
; vdp_addr (the VDP address, $E037), read as the start of each write; cur_mmu ($E02D);
; the VRAM copy in pages 28-29 (SHADOW_PAGE).
BUF     equ $3000               ; layout buffer, up to 1536 bytes
PSTACK  equ $3FF0

; Prologue: A and the interrupt state saved, interrupts off, the page's stack, IX and IY kept.
        macro ENTER
        ld (sv_a),a
        ld a,i                  ; P/V = IFF2
        di
        ld a,0
        jp po,1F
        inc a
1:      ld (sv_ie),a
        ld (sv_sp),sp
        ld sp,PSTACK
        push ix
        push iy
        ld a,(sv_a)
        endm
; Epilogue: IX, IY, the game's stack and the interrupt state back; A = (sv_a).
        macro LEAVE
        pop iy
        pop ix
        ld sp,(sv_sp)
        ld a,(sv_ie)
        or a
        ld a,(sv_a)
        jr z,1F
        ei
1:      ret
        endm

; e896: $0AD2, 896 bytes from HL. Out: HL + 896, B - 128, C = $BE; A, DE kept.
e896:   ENTER
        ld (sv_b),bc
        push de
        ld bc,896
        call cpbuf
        pop de
        ld a,(sv_b+1)
        sub 128
        ld b,a
        ld c,$BE
        LEAVE

; e1536: $11D5, 1536 bytes from HL. Out: HL + 1536, B = 0, C = $BE; A, DE kept.
e1536:  ld bc,1536
        jr elin
; e768: $077E (LD BC,$00BE : CALL $11EA), 768 bytes from HL. Out as e1536.
e768:   ld bc,768
elin:   ENTER
        push de
        call cpbuf
        pop de
        ld bc,$00BE
        LEAVE

; e3z192: $11FC, 192 passes of three bytes from HL and a 0. e3z104: $07B6, 104 passes.
; Out: HL + 3 * passes, A = 0, B = 0, C = $BE; DE kept.
e3z192: ld bc,192
        jr e3z
e3z104: ld bc,104
e3z:    ENTER
        xor a
        ld (sv_a),a
        push de
        call lay3
        pop de
        ld bc,$00BE
        LEAVE

; eq3: $1213, 208 groups of three bytes from HL and a 0. Out: HL + 624, A = 0, B - 112,
; C = $BE; DE kept.
eq3:    ENTER
        xor a
        ld (sv_a),a
        ld a,b
        sub 112
        ld (sv_b),a
        push de
        ld bc,208
        call lay3
        pop de
        ld a,(sv_b)
        ld b,a
        ld c,$BE
        LEAVE

; ent512: $1897, 512 name table cells: a byte from HL, then A. Out: HL + 512, B kept,
; C = $BE; A, DE kept.
ent512: ENTER
        ld (sv_b),bc
        push de
        ld bc,512
        call lay1
        pop de
        ld bc,(sv_b)
        ld c,$BE
        LEAVE

; ent256: $209A, 256 cells. Out: HL + 256, B = 0, C = $BE; A, DE kept.
ent256: ENTER
        push de
        ld bc,256
        call lay1
        pop de
        ld bc,$00BE
        LEAVE

; cpbuf: BC bytes from HL (game RAM) into BUF, then to VRAM in tiles. Out: HL past the source.
cpbuf:  push bc
        ld de,BUF
        ldir
        pop bc
        ld a,32
        push hl
        call vput
        pop hl
        ret

; lay3: BC groups of 3 bytes from HL, each followed by a 0, into BUF, then to VRAM in tiles.
; Out: HL past the source.
lay3:   ld de,BUF
        push bc
1:      ldi
        ldi
        ldi
        inc bc
        inc bc
        xor a
        ld (de),a
        inc de
        ld a,b
        or c
        jr nz,1B
        pop bc                  ; groups -> bytes: 4 * groups
        push hl
        ld h,b
        ld l,c
        add hl,hl
        add hl,hl
        ld b,h
        ld c,l
        ld a,32
        call vput
        pop hl
        ret

; lay1: BC cells, the low byte from HL and the high byte (sv_a), into BUF, then to VRAM in
; cells. Out: HL past the source.
lay1:   ld de,BUF
        push bc
        ld a,(sv_a)
1:      ldi
        ld (de),a
        inc de
        jp pe,1B                ; P/V clear when BC reaches 0
        pop bc
        push hl
        ld h,b
        ld l,c
        add hl,hl
        ld b,h
        ld c,l
        ld a,2
        call vput
        pop hl
        ret

; vput: BC bytes at BUF to VRAM from the VDP address, as the game's writes leave it, but
; writing only the units of A bytes (32: tiles, 2: name table cells) that differ from the
; VRAM copy, in runs with jt_vwrite; when the last unit is unchanged its last byte is written
; again, so the VDP address and read buffer end as after the game's writes. An address or a
; length that is not a whole number of units is written whole. Interrupts must be off: slot 0
; holds the VRAM copy (pages 28-29, SHADOW_PAGE in the runtime) while a unit is compared.
; Changes AF, BC, DE, HL, IX, IY.
vput:   ld (vu),a
        ld (vlen),bc
        ld de,(vdp_addr)
        ld a,d
        and $3F
        ld d,a
        ld (vstart),de
        ld a,(vu)
        dec a
        ld l,a
        and e
        jp nz,8F
        ld a,l
        and c
        jp nz,8F
        ld a,(vu)               ; units = BC / vu
        ld h,b
        ld l,c
1:      rra
        jr c,2F
        srl h
        rr l
        jr 1B
2:      ld (vcnt),hl
        xor a
        ld (vrun),a
        ld hl,BUF
3:      ld a,d                  ; the VRAM copy's page of DE in slot 0
        rlca
        rlca
        rlca
        and 1
        add a,28
        db $ED,$92,$50          ; nextreg $50,a
        push de
        push hl
        ld a,d
        and $1F
        ld d,a
        ld a,(vu)
        ld b,a
4:      ld a,(de)
        cp (hl)
        jr nz,5F
        inc de
        inc hl
        djnz 4B
        pop hl                  ; unchanged: end the run
        pop de
        xor a
        ld (vlast),a
        call vflush
        jr 6F
5:      pop hl                  ; differs: into the run
        pop de
        ld a,1
        ld (vlast),a
        ld a,(vrun)
        or a
        jr nz,7F
        ld (vrs),hl
        ld (vrd),de
        ld bc,0
        ld (vrn),bc
7:      ld a,1
        ld (vrun),a
        ld bc,(vrn)
        ld a,(vu)
        add a,c
        ld c,a
        ld a,0
        adc a,b
        ld b,a
        ld (vrn),bc
6:      ld a,(vu)               ; the next unit
        ld c,a
        ld b,0
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        ld bc,(vcnt)
        dec bc
        ld (vcnt),bc
        ld a,b
        or c
        jr nz,3B
        call vflush
        ld a,(vlast)
        or a
        ret nz
        ld hl,(vlen)            ; the last byte once more
        dec hl
        push hl
        ld de,(vstart)
        add hl,de
        ex de,hl                ; DE = its VRAM address
        pop hl
        ld bc,BUF
        add hl,bc               ; HL = BUF + length - 1
        ld bc,1
        ld a,1
        jp vlin
8:      ld a,(cur_mmu+0)        ; written whole
        db $ED,$92,$50          ; nextreg $50,a
        ld hl,BUF
        ld a,1
        jp vlin
; vflush: write the open run, if any. Keeps DE, HL.
vflush: ld a,(cur_mmu+0)        ; the game's page back in slot 0
        db $ED,$92,$50          ; nextreg $50,a
        ld a,(vrun)
        or a
        ret z
        xor a
        ld (vrun),a
        push de
        push hl
        ld hl,(vrs)
        ld de,(vrd)
        ld bc,(vrn)
        ld a,1
        call vlin
        pop hl
        pop de
        ret

; vlin: BC bytes (1 to 65535) from HL to VRAM from DE, with jt_vwrite; A = jt_vwrite's
; source mode. Changes AF, BC, DE, HL, IX, IY.
vlin:   ld (vl_m),a
        ld a,c
        ld (vl_c),a             ; the bytes after the whole runs of 256
        ld a,b
        or a
        jr z,2F
        ld c,b                  ; B runs of 256 bytes
        ld b,0
        ld ix,256
        ld iy,256
        ld a,(vl_m)
        call jt_vwrite          ; keeps BC, DE, HL
        ld a,h                  ; HL and DE past them
        add a,c
        ld h,a
        ld a,d
        add a,c
        ld d,a
2:      ld a,(vl_c)
        or a
        ret z
        ld b,a                  ; one run of the rest
        ld c,1
        ld ix,0
        ld iy,0
        ld a,(vl_m)
        jp jt_vwrite
vu:     db 0
vrun:   db 0
vlast:  db 0
vlen:   dw 0
vstart: dw 0
vcnt:   dw 0
vrs:    dw 0
vrd:    dw 0
vrn:    dw 0

; ---- Game speed: the step model (see the spec comment before cave_s).
; Runtime internals used: isr_n ($E071, the game's frame handler entries).
; Units: T-states / 16. A Next line is 1,824 cycles. The work took 1.48 (W1) and 1.36 (W2)
; Next cycles per Master System T-state, its traps and these entries included (means over
; about 200 steps of stage 1, against the reference's), so a line is 77 (W1) and 84 (W2) units.
K1      equ 77
K2      equ 84
H5      equ 3562                ; the frame handler's T-states / 16 in each state, measured in
H6      equ 3487                ; the reference (medians over 248 steps of stage 1)
H7      equ 1937
H8      equ 1806
H9      equ 175

; st_s: $05D3 (from cave_s). The step starts: note the line and the handler count, and turn
; interrupts off for W1. Keeps every register.
st_s:   di
        push af
        push bc
        push hl
        call rdline
        ld (sl0),hl
        ld a,(isr_n)
        ld (sc0),a
        ld a,1
        ld (sflag),a
        pop hl
        pop bc
        pop af
        ret                     ; interrupts stay off (W1)

; st_a: $062C, the wait loop's head. A = ($C001), flags of CP 7. The first time in a step it
; ends W1 and turns interrupts on.
st_a:   ld a,(sflag)
        cp 1
        jr nz,1F
        push bc
        push de
        push hl
        ld a,K1
        ld (sk),a
        call elapsed
        ld (sw1),hl
        ld a,2
        ld (sflag),a
        pop hl
        pop de
        pop bc
        ld a,($C001)
        cp 7
        ei
        ret
1:      ld a,($C001)
        cp 7
        ret

; st_b: $0636. W2 starts with interrupts off. Does LD A,(HL) : INC HL : OR A.
st_b:   di
        push bc
        push hl
        call rdline
        ld (sl0),hl
        ld a,3
        ld (sflag),a
        pop hl
        pop bc
        call jt_peek
        inc hl
        or a
        ret                     ; interrupts stay off (W2)

; st_d: $0669, the wait loop's head. The first time in a step it ends W2, turns interrupts
; on and works out the step's frames. Returns A = ($C001), or 8 while the step has not yet
; reached the Master System's frame, and the flags of CP 9.
st_d:   ld a,(sflag)
        cp 3
        jr nz,2F
        push bc
        push de
        push hl
        ld a,K2
        ld (sk),a
        call elapsed
        ld (sw2),hl
        call model
        ld (sn),a
        xor a
        ld (sflag),a
        pop hl
        pop de
        pop bc
        ei
2:      ld a,($C001)
        cp 9
        ret nz
        push bc
        ld a,(sn)
        dec a
        ld b,a                  ; frames after the step's first: N - 1
        ld a,(isr_n)
        ld c,a
        ld a,(sc0)
        neg
        add a,c                 ; handler entries since the step started
        cp b
        pop bc
        ld a,9
        jr nc,3F
        ld a,8
3:      cp 9
        ret

; rdline: HL = the Next's raster line. Changes A, BC.
rdline: ld a,i                  ; keep the interrupt state
        push af
        di
1:      ld bc,$243B
        ld a,$1E
        out (c),a
        inc b
        in h,(c)
        dec b
        ld a,$1F
        out (c),a
        inc b
        in l,(c)
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        cp h
        jr nz,1B
        ld a,h
        and 1
        ld h,a
        pop af
        ret po
        ei
        ret

; elapsed: HL = units since the line in (sl0), at (sk) units a line; sets (sf), the frame in
; units. Changes A, BC, DE.
elapsed: call rdline
        ld de,(sl0)
        or a
        sbc hl,de
        push hl
        ld bc,$243B
        ld a,5
        out (c),a
        inc b
        in a,(c)
        ld hl,4460              ; 50 Hz: 71,364 T-states a frame, 311 lines
        ld de,311
        bit 2,a
        jr z,1F
        ld hl,3733              ; 60 Hz: 59,736 T-states a frame, 264 lines
        ld de,264
1:      ld (sf),hl
        pop hl
        bit 7,h
        jr z,2F
        add hl,de               ; the line count went round
2:      ld a,(sk)               ; HL * (sk): lines to units
        ex de,hl
        ld hl,0
        ld b,8
3:      add hl,hl
        rla
        jr nc,4F
        add hl,de
4:      djnz 3B
        ret

; model: A = the step's frames (from its start to the next step's start) on a Master System
; at the Next's rate, from (sw1), (sw2) and (sf).
model:  ld hl,H5
        ld (mt),hl
        xor a
        ld (mk),a
        ld hl,(sw1)
        ld (mrem),hl
1:      call avail              ; W1
        ld de,(mrem)
        or a
        sbc hl,de
        jr c,2F
        ld hl,(mt)
        add hl,de
        ld (mt),hl
        jr 3F
2:      call negrem
        call nextf
        jr c,9F
        jr 1B
3:      ld hl,(sw2)             ; W2, from the frame after the state 6 handler
        ld (mrem),hl
        ld a,(mk)
        or a
        call z,nextf
4:      call avail
        ld de,(mrem)
        or a
        sbc hl,de
        jr nc,9F
        call negrem
        call nextf
        jr nc,4B
9:      ld a,(mk)
        inc a
        cp 4
        ret nc
        ld a,4
        ret
avail:  ld hl,(sf)              ; HL = the frame less the time used in it
        ld de,(mt)
        or a
        sbc hl,de
        ret
negrem: xor a                   ; (mrem) = -HL
        sub l
        ld l,a
        sbc a,a
        sub h
        ld h,a
        ld (mrem),hl
        ret
nextf:  ld a,(mk)               ; the next frame: its handler's time; carry set past 30 frames
        inc a
        ld (mk),a
        ld hl,H6
        cp 1
        jr z,1F
        ld hl,H7
        cp 2
        jr z,1F
        ld hl,H8
        cp 3
        jr z,1F
        ld hl,H9
1:      ld (mt),hl
        cp 30
        ccf
        ret
sflag:  db 0
sc0:    db 0
sn:     db 4
sl0:    dw 0
sw1:    dw 0
sw2:    dw 0
sf:     dw 4460
mt:     dw 0
mrem:   dw 0
mk:     db 0
sk:     db 0
sv_a:   db 0
sv_ie:  db 0
sv_sp:  dw 0
sv_b:   dw 0
vl_m:   db 0
vl_c:   db 0
endpage
