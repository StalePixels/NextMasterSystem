# Lord of the Sword (USA, Europe, Brazil) (En), CRC32 E8511B08, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output.
# Decisions:
# - $0008-$000A is $FF filler that no code uses, so $08 is the io vector.
# - Code in bank 0 that no path reaches is patched as sites: the region check at $01E6
#   ($01EC, $01EE, $01F7, $01F9, $0201), the VDP routines $030B and $0357 ($030C, $030F,
#   $0313, $0358, $035B, $0360, $0365) and the two-digit print routine $1835 ($1853,
#   $1859, $1860, $1866). No call, jump or table in the cart names their starts.
# - The field scenes split the picture with a line interrupt: the frame handler sets
#   register 10 to $4F and register 8 from $C147 (the mountains), and the line handler at
#   $01BC sets register 8 from $C111 (the ground) and register 10 to $FF. hsplit moves the
#   copper's map switch column with that write; without it a band on the right of the
#   ground showed the wrong map columns once the view scrolled.
# - The other byte patterns that no path reached (banks 6, 8 and 13) are data (verdict false).
name Lord of the Sword
cart E8511B08
hz any		; No-Intro regions USA, Europe, Brazil
hsplit
vector 08 io
asm 00004 2   ; IM 1 -> IM 2
    im 2
endasm
site 000B3   ; OUT ($DF),A
site 00127   ; IN A,($BF)
site 0014E   ; OUT ($BF),A
site 00152   ; OUT ($BF),A
site 00154   ; IN A,($DD)
site 00172   ; OUT ($BF),A
site 00176   ; OUT ($BF),A
site 001D4   ; OUT ($BF),A
site 001D8   ; OUT ($BF),A
site 001DC   ; OUT ($BF),A
site 001E0   ; OUT ($BF),A
site 00228   ; OUT ($3E),A
site 00230   ; OUT ($F2),A
site 00233   ; IN A,($F2)
site 00245   ; OUT ($F2),A
site 0024D   ; OUT ($3E),A
site 002B4   ; IN A,($DC)
site 00303   ; OUT ($BF),A
site 00308   ; OUT ($BF),A
site 00318   ; OUT ($BF),A
site 0031B   ; OUT ($BF),A
site 0031E   ; OUT ($BE),A
site 00322   ; OUT ($BF),A
site 00325   ; OUT ($BF),A
site 00328   ; OUT ($BE),A
site 00332   ; OUT ($BF),A
site 00335   ; OUT ($BF),A
site 00338   ; OUT ($BE),A
site 0033D   ; OUT ($BE),A
site 00347   ; OUT ($BF),A
site 0034A   ; OUT ($BF),A
site 0034D   ; OUT ($BE),A
site 00370   ; OUT ($BF),A
site 00373   ; OUT ($BF),A
site 00378   ; OUTI
site 00388   ; OUT ($BF),A
site 0038B   ; OUT ($BF),A
site 00422   ; OUT ($BF),A
site 00425   ; OUT ($BF),A
site 00427   ; OTIR
site 00A47   ; OUT ($BF),A
site 00A4B   ; OUT ($BF),A
site 00A54   ; OUTI
site 00A56   ; OUTI
site 00A58   ; OUTI
site 00A5A   ; OUT ($BE),A
site 00A5C   ; OUTI
site 00A5E   ; OUTI
site 00A60   ; OUTI
site 00A62   ; OUT ($BE),A
site 00A64   ; OUTI
site 00A66   ; OUTI
site 00A68   ; OUTI
site 00A6A   ; OUT ($BE),A
site 00A6C   ; OUTI
site 00A6E   ; OUTI
site 00A70   ; OUTI
site 00A72   ; OUT ($BE),A
site 00A74   ; OUTI
site 00A76   ; OUTI
site 00A78   ; OUTI
site 00A7A   ; OUT ($BE),A
site 00A7C   ; OUTI
site 00A7E   ; OUTI
site 00A80   ; OUTI
site 00A82   ; OUT ($BE),A
site 00A84   ; OUTI
site 00A86   ; OUTI
site 00A88   ; OUTI
site 00A8A   ; OUT ($BE),A
site 00A8C   ; OUTI
site 00A8E   ; OUTI
site 00A90   ; OUTI
site 00A92   ; OUT ($BE),A
site 00A94   ; OUTI
site 00A96   ; OUTI
site 00A98   ; OUTI
site 00A9A   ; OUT ($BE),A
site 00A9C   ; OUTI
site 00A9E   ; OUTI
site 00AA0   ; OUTI
site 00AA2   ; OUT ($BE),A
site 00AA4   ; OUTI
site 00AA6   ; OUTI
site 00AA8   ; OUTI
site 00AAA   ; OUT ($BE),A
site 00AAC   ; OUTI
site 00AAE   ; OUTI
site 00AB0   ; OUTI
site 00AB2   ; OUT ($BE),A
site 00AB4   ; OUTI
site 00AB6   ; OUTI
site 00AB8   ; OUTI
site 00ABA   ; OUT ($BE),A
site 00ABC   ; OUTI
site 00ABE   ; OUTI
site 00AC0   ; OUTI
site 00AC2   ; OUT ($BE),A
site 00AC4   ; OUTI
site 00AC6   ; OUTI
site 00AC8   ; OUTI
site 00ACA   ; OUT ($BE),A
site 00ACC   ; OUTI
site 00ACE   ; OUTI
site 00AD0   ; OUTI
site 00AD2   ; OUT ($BE),A
site 00AD4   ; OUTI
site 00AD6   ; OUTI
site 00AD8   ; OUTI
site 00ADA   ; OUT ($BE),A
site 00ADC   ; OUTI
site 00ADE   ; OUTI
site 00AE0   ; OUTI
site 00AE2   ; OUT ($BE),A
site 00AE4   ; OUTI
site 00AE6   ; OUTI
site 00AE8   ; OUTI
site 00AEA   ; OUT ($BE),A
site 00AEC   ; OUTI
site 00AEE   ; OUTI
site 00AF0   ; OUTI
site 00AF2   ; OUT ($BE),A
site 00AF4   ; OUTI
site 00AF6   ; OUTI
site 00AF8   ; OUTI
site 00AFA   ; OUT ($BE),A
site 00AFC   ; OUTI
site 00AFE   ; OUTI
site 00B00   ; OUTI
site 00B02   ; OUT ($BE),A
site 00B04   ; OUTI
site 00B06   ; OUTI
site 00B08   ; OUTI
site 00B0A   ; OUT ($BE),A
site 00B0C   ; OUTI
site 00B0E   ; OUTI
site 00B10   ; OUTI
site 00B12   ; OUT ($BE),A
site 00B14   ; OUTI
site 00B16   ; OUTI
site 00B18   ; OUTI
site 00B1A   ; OUT ($BE),A
site 00B1C   ; OUTI
site 00B1E   ; OUTI
site 00B20   ; OUTI
site 00B22   ; OUT ($BE),A
site 00B24   ; OUTI
site 00B26   ; OUTI
site 00B28   ; OUTI
site 00B2A   ; OUT ($BE),A
site 00B2C   ; OUTI
site 00B2E   ; OUTI
site 00B30   ; OUTI
site 00B32   ; OUT ($BE),A
site 00B34   ; OUTI
site 00B36   ; OUTI
site 00B38   ; OUTI
site 00B3A   ; OUT ($BE),A
site 00B3C   ; OUTI
site 00B3E   ; OUTI
site 00B40   ; OUTI
site 00B42   ; OUT ($BE),A
site 00B44   ; OUTI
site 00B46   ; OUTI
site 00B48   ; OUTI
site 00B4A   ; OUT ($BE),A
site 00B4C   ; OUTI
site 00B4E   ; OUTI
site 00B50   ; OUTI
site 00B52   ; OUT ($BE),A
site 00B54   ; OUTI
site 00B56   ; OUTI
site 00B58   ; OUTI
site 00B5A   ; OUT ($BE),A
site 00B5C   ; OUTI
site 00B5E   ; OUTI
site 00B60   ; OUTI
site 00B62   ; OUT ($BE),A
site 00B64   ; OUTI
site 00B66   ; OUTI
site 00B68   ; OUTI
site 00B6A   ; OUT ($BE),A
site 00B6C   ; OUTI
site 00B6E   ; OUTI
site 00B70   ; OUTI
site 00B72   ; OUT ($BE),A
site 00B74   ; OUTI
site 00B76   ; OUTI
site 00B78   ; OUTI
site 00B7A   ; OUT ($BE),A
site 00B7C   ; OUTI
site 00B7E   ; OUTI
site 00B80   ; OUTI
site 00B82   ; OUT ($BE),A
site 00B84   ; OUTI
site 00B86   ; OUTI
site 00B88   ; OUTI
site 00B8A   ; OUT ($BE),A
site 00B8C   ; OUTI
site 00B8E   ; OUTI
site 00B90   ; OUTI
site 00B92   ; OUT ($BE),A
site 00B94   ; OUTI
site 00B96   ; OUTI
site 00B98   ; OUTI
site 00B9A   ; OUT ($BE),A
site 00B9C   ; OUTI
site 00B9E   ; OUTI
site 00BA0   ; OUTI
site 00BA2   ; OUT ($BE),A
site 00BA4   ; OUTI
site 00BA6   ; OUTI
site 00BA8   ; OUTI
site 00BAA   ; OUT ($BE),A
site 00BAC   ; OUTI
site 00BAE   ; OUTI
site 00BB0   ; OUTI
site 00BB2   ; OUT ($BE),A
site 00BB4   ; OUTI
site 00BB6   ; OUTI
site 00BB8   ; OUTI
site 00BBA   ; OUT ($BE),A
site 00BBC   ; OUTI
site 00BBE   ; OUTI
site 00BC0   ; OUTI
site 00BC2   ; OUT ($BE),A
site 00BC4   ; OUTI
site 00BC6   ; OUTI
site 00BC8   ; OUTI
site 00BCA   ; OUT ($BE),A
site 00BCC   ; OUTI
site 00BCE   ; OUTI
site 00BD0   ; OUTI
site 00BD2   ; OUT ($BE),A
site 00BD4   ; OUTI
site 00BD6   ; OUTI
site 00BD8   ; OUTI
site 00BDA   ; OUT ($BE),A
site 00BDC   ; OUTI
site 00BDE   ; OUTI
site 00BE0   ; OUTI
site 00BE2   ; OUT ($BE),A
site 00BE4   ; OUTI
site 00BE6   ; OUTI
site 00BE8   ; OUTI
site 00BEA   ; OUT ($BE),A
site 00BEC   ; OUTI
site 00BEE   ; OUTI
site 00BF0   ; OUTI
site 00BF2   ; OUT ($BE),A
site 00BF4   ; OUTI
site 00BF6   ; OUTI
site 00BF8   ; OUTI
site 00BFA   ; OUT ($BE),A
site 00BFC   ; OUTI
site 00BFE   ; OUTI
site 00C00   ; OUTI
site 00C02   ; OUT ($BE),A
site 00C04   ; OUTI
site 00C06   ; OUTI
site 00C08   ; OUTI
site 00C0A   ; OUT ($BE),A
site 00C0C   ; OUTI
site 00C0E   ; OUTI
site 00C10   ; OUTI
site 00C12   ; OUT ($BE),A
site 00C14   ; OUTI
site 00C16   ; OUTI
site 00C18   ; OUTI
site 00C1A   ; OUT ($BE),A
site 00C1C   ; OUTI
site 00C1E   ; OUTI
site 00C20   ; OUTI
site 00C22   ; OUT ($BE),A
site 00C24   ; OUTI
site 00C26   ; OUTI
site 00C28   ; OUTI
site 00C2A   ; OUT ($BE),A
site 00C2C   ; OUTI
site 00C2E   ; OUTI
site 00C30   ; OUTI
site 00C32   ; OUT ($BE),A
site 00C34   ; OUTI
site 00C36   ; OUTI
site 00C38   ; OUTI
site 00C3A   ; OUT ($BE),A
site 00C3C   ; OUTI
site 00C3E   ; OUTI
site 00C40   ; OUTI
site 00C42   ; OUT ($BE),A
site 00C44   ; OUTI
site 00C46   ; OUTI
site 00C48   ; OUTI
site 00C4A   ; OUT ($BE),A
site 00C4C   ; OUTI
site 00C4E   ; OUTI
site 00C50   ; OUTI
site 00C52   ; OUT ($BE),A
site 00C54   ; OUTI
site 00C56   ; OUTI
site 00C58   ; OUTI
site 00C5A   ; OUT ($BE),A
site 00C5C   ; OUTI
site 00C5E   ; OUTI
site 00C60   ; OUTI
site 00C62   ; OUT ($BE),A
site 00C64   ; OUTI
site 00C66   ; OUTI
site 00C68   ; OUTI
site 00C6A   ; OUT ($BE),A
site 00C6C   ; OUTI
site 00C6E   ; OUTI
site 00C70   ; OUTI
site 00C72   ; OUT ($BE),A
site 00C74   ; OUTI
site 00C76   ; OUTI
site 00C78   ; OUTI
site 00C7A   ; OUT ($BE),A
site 00C7C   ; OUTI
site 00C7E   ; OUTI
site 00C80   ; OUTI
site 00C82   ; OUT ($BE),A
site 00C84   ; OUTI
site 00C86   ; OUTI
site 00C88   ; OUTI
site 00C8A   ; OUT ($BE),A
site 00C8C   ; OUTI
site 00C8E   ; OUTI
site 00C90   ; OUTI
site 00C92   ; OUT ($BE),A
site 00C94   ; OUTI
site 00C96   ; OUTI
site 00C98   ; OUTI
site 00C9A   ; OUT ($BE),A
site 00C9C   ; OUTI
site 00C9E   ; OUTI
site 00CA0   ; OUTI
site 00CA2   ; OUT ($BE),A
site 00CA4   ; OUTI
site 00CA6   ; OUTI
site 00CA8   ; OUTI
site 00CAA   ; OUT ($BE),A
site 00CAC   ; OUTI
site 00CAE   ; OUTI
site 00CB0   ; OUTI
site 00CB2   ; OUT ($BE),A
site 00CB4   ; OUTI
site 00CB6   ; OUTI
site 00CB8   ; OUTI
site 00CBA   ; OUT ($BE),A
site 00CBC   ; OUTI
site 00CBE   ; OUTI
site 00CC0   ; OUTI
site 00CC2   ; OUT ($BE),A
site 00CC4   ; OUTI
site 00CC6   ; OUTI
site 00CC8   ; OUTI
site 00CCA   ; OUT ($BE),A
site 00CCC   ; OUTI
site 00CCE   ; OUTI
site 00CD0   ; OUTI
site 00CD2   ; OUT ($BE),A
site 00CD4   ; OUTI
site 00CD6   ; OUTI
site 00CD8   ; OUTI
site 00CDA   ; OUT ($BE),A
site 00CDC   ; OUTI
site 00CDE   ; OUTI
site 00CE0   ; OUTI
site 00CE2   ; OUT ($BE),A
site 00CE4   ; OUTI
site 00CE6   ; OUTI
site 00CE8   ; OUTI
site 00CEA   ; OUT ($BE),A
site 00CEC   ; OUTI
site 00CEE   ; OUTI
site 00CF0   ; OUTI
site 00CF2   ; OUT ($BE),A
site 00CF4   ; OUTI
site 00CF6   ; OUTI
site 00CF8   ; OUTI
site 00CFA   ; OUT ($BE),A
site 00CFC   ; OUTI
site 00CFE   ; OUTI
site 00D00   ; OUTI
site 00D02   ; OUT ($BE),A
site 00D04   ; OUTI
site 00D06   ; OUTI
site 00D08   ; OUTI
site 00D0A   ; OUT ($BE),A
site 00D0C   ; OUTI
site 00D0E   ; OUTI
site 00D10   ; OUTI
site 00D12   ; OUT ($BE),A
site 00D14   ; OUTI
site 00D16   ; OUTI
site 00D18   ; OUTI
site 00D1A   ; OUT ($BE),A
site 00D1C   ; OUTI
site 00D1E   ; OUTI
site 00D20   ; OUTI
site 00D22   ; OUT ($BE),A
site 00D24   ; OUTI
site 00D26   ; OUTI
site 00D28   ; OUTI
site 00D2A   ; OUT ($BE),A
site 00D2C   ; OUTI
site 00D2E   ; OUTI
site 00D30   ; OUTI
site 00D32   ; OUT ($BE),A
site 00D34   ; OUTI
site 00D36   ; OUTI
site 00D38   ; OUTI
site 00D3A   ; OUT ($BE),A
site 00D3C   ; OUTI
site 00D3E   ; OUTI
site 00D40   ; OUTI
site 00D42   ; OUT ($BE),A
site 00D44   ; OUTI
site 00D46   ; OUTI
site 00D48   ; OUTI
site 00D4A   ; OUT ($BE),A
site 00D4C   ; OUTI
site 00D4E   ; OUTI
site 00D50   ; OUTI
site 00D52   ; OUT ($BE),A
site 00D54   ; OUTI
site 00D56   ; OUTI
site 00D58   ; OUTI
site 00D5A   ; OUT ($BE),A
site 00D5C   ; OUTI
site 00D5E   ; OUTI
site 00D60   ; OUTI
site 00D62   ; OUT ($BE),A
site 00D64   ; OUTI
site 00D66   ; OUTI
site 00D68   ; OUTI
site 00D6A   ; OUT ($BE),A
site 00D6C   ; OUTI
site 00D6E   ; OUTI
site 00D70   ; OUTI
site 00D72   ; OUT ($BE),A
site 00D74   ; OUTI
site 00D76   ; OUTI
site 00D78   ; OUTI
site 00D7A   ; OUT ($BE),A
site 00D7C   ; OUTI
site 00D7E   ; OUTI
site 00D80   ; OUTI
site 00D82   ; OUT ($BE),A
site 00D84   ; OUTI
site 00D86   ; OUTI
site 00D88   ; OUTI
site 00D8A   ; OUT ($BE),A
site 00D8C   ; OUTI
site 00D8E   ; OUTI
site 00D90   ; OUTI
site 00D92   ; OUT ($BE),A
site 00D94   ; OUTI
site 00D96   ; OUTI
site 00D98   ; OUTI
site 00D9A   ; OUT ($BE),A
site 00D9C   ; OUTI
site 00D9E   ; OUTI
site 00DA0   ; OUTI
site 00DA2   ; OUT ($BE),A
site 00DA4   ; OUTI
site 00DA6   ; OUTI
site 00DA8   ; OUTI
site 00DAA   ; OUT ($BE),A
site 00DAC   ; OUTI
site 00DAE   ; OUTI
site 00DB0   ; OUTI
site 00DB2   ; OUT ($BE),A
site 00DB4   ; OUTI
site 00DB6   ; OUTI
site 00DB8   ; OUTI
site 00DBA   ; OUT ($BE),A
site 00DBC   ; OUTI
site 00DBE   ; OUTI
site 00DC0   ; OUTI
site 00DC2   ; OUT ($BE),A
site 00DC4   ; OUTI
site 00DC6   ; OUTI
site 00DC8   ; OUTI
site 00DCA   ; OUT ($BE),A
site 00DCC   ; OUTI
site 00DCE   ; OUTI
site 00DD0   ; OUTI
site 00DD2   ; OUT ($BE),A
site 00DD4   ; OUTI
site 00DD6   ; OUTI
site 00DD8   ; OUTI
site 00DDA   ; OUT ($BE),A
site 00DDC   ; OUTI
site 00DDE   ; OUTI
site 00DE0   ; OUTI
site 00DE2   ; OUT ($BE),A
site 00DE4   ; OUTI
site 00DE6   ; OUTI
site 00DE8   ; OUTI
site 00DEA   ; OUT ($BE),A
site 00DEC   ; OUTI
site 00DEE   ; OUTI
site 00DF0   ; OUTI
site 00DF2   ; OUT ($BE),A
site 00DF4   ; OUTI
site 00DF6   ; OUTI
site 00DF8   ; OUTI
site 00DFA   ; OUT ($BE),A
site 00DFC   ; OUTI
site 00DFE   ; OUTI
site 00E00   ; OUTI
site 00E02   ; OUT ($BE),A
site 00E04   ; OUTI
site 00E06   ; OUTI
site 00E08   ; OUTI
site 00E0A   ; OUT ($BE),A
site 00E0C   ; OUTI
site 00E0E   ; OUTI
site 00E10   ; OUTI
site 00E12   ; OUT ($BE),A
site 00E14   ; OUTI
site 00E16   ; OUTI
site 00E18   ; OUTI
site 00E1A   ; OUT ($BE),A
site 00E1C   ; OUTI
site 00E1E   ; OUTI
site 00E20   ; OUTI
site 00E22   ; OUT ($BE),A
site 00E24   ; OUTI
site 00E26   ; OUTI
site 00E28   ; OUTI
site 00E2A   ; OUT ($BE),A
site 00E2C   ; OUTI
site 00E2E   ; OUTI
site 00E30   ; OUTI
site 00E32   ; OUT ($BE),A
site 00E34   ; OUTI
site 00E36   ; OUTI
site 00E38   ; OUTI
site 00E3A   ; OUT ($BE),A
site 00E3C   ; OUTI
site 00E3E   ; OUTI
site 00E40   ; OUTI
site 00E42   ; OUT ($BE),A
site 00E44   ; OUTI
site 00E46   ; OUTI
site 00E48   ; OUTI
site 00E4A   ; OUT ($BE),A
site 00E4C   ; OUTI
site 00E4E   ; OUTI
site 00E50   ; OUTI
site 00E52   ; OUT ($BE),A
site 00E54   ; OUTI
site 00E56   ; OUTI
site 00E58   ; OUTI
site 00E5A   ; OUT ($BE),A
site 00E5C   ; OUTI
site 00E5E   ; OUTI
site 00E60   ; OUTI
site 00E62   ; OUT ($BE),A
site 00E64   ; OUTI
site 00E66   ; OUTI
site 00E68   ; OUTI
site 00E6A   ; OUT ($BE),A
site 00E6C   ; OUTI
site 00E6E   ; OUTI
site 00E70   ; OUTI
site 00E72   ; OUT ($BE),A
site 00E74   ; OUTI
site 00E76   ; OUTI
site 00E78   ; OUTI
site 00E7A   ; OUT ($BE),A
site 00E7C   ; OUTI
site 00E7E   ; OUTI
site 00E80   ; OUTI
site 00E82   ; OUT ($BE),A
site 00E84   ; OUTI
site 00E86   ; OUTI
site 00E88   ; OUTI
site 00E8A   ; OUT ($BE),A
site 00E8C   ; OUTI
site 00E8E   ; OUTI
site 00E90   ; OUTI
site 00E92   ; OUT ($BE),A
site 00E94   ; OUTI
site 00E96   ; OUTI
site 00E98   ; OUTI
site 00E9A   ; OUT ($BE),A
site 00E9C   ; OUTI
site 00E9E   ; OUTI
site 00EA0   ; OUTI
site 00EA2   ; OUT ($BE),A
site 00EA4   ; OUTI
site 00EA6   ; OUTI
site 00EA8   ; OUTI
site 00EAA   ; OUT ($BE),A
site 00EAC   ; OUTI
site 00EAE   ; OUTI
site 00EB0   ; OUTI
site 00EB2   ; OUT ($BE),A
site 00EB4   ; OUTI
site 00EB6   ; OUTI
site 00EB8   ; OUTI
site 00EBA   ; OUT ($BE),A
site 00EBC   ; OUTI
site 00EBE   ; OUTI
site 00EC0   ; OUTI
site 00EC2   ; OUT ($BE),A
site 00EC4   ; OUTI
site 00EC6   ; OUTI
site 00EC8   ; OUTI
site 00ECA   ; OUT ($BE),A
site 00ECC   ; OUTI
site 00ECE   ; OUTI
site 00ED0   ; OUTI
site 00ED2   ; OUT ($BE),A
site 00ED4   ; OUTI
site 00ED6   ; OUTI
site 00ED8   ; OUTI
site 00EDA   ; OUT ($BE),A
site 00EDC   ; OUTI
site 00EDE   ; OUTI
site 00EE0   ; OUTI
site 00EE2   ; OUT ($BE),A
site 00EE4   ; OUTI
site 00EE6   ; OUTI
site 00EE8   ; OUTI
site 00EEA   ; OUT ($BE),A
site 00EEC   ; OUTI
site 00EEE   ; OUTI
site 00EF0   ; OUTI
site 00EF2   ; OUT ($BE),A
site 00EF4   ; OUTI
site 00EF6   ; OUTI
site 00EF8   ; OUTI
site 00EFA   ; OUT ($BE),A
site 00EFC   ; OUTI
site 00EFE   ; OUTI
site 00F00   ; OUTI
site 00F02   ; OUT ($BE),A
site 00F04   ; OUTI
site 00F06   ; OUTI
site 00F08   ; OUTI
site 00F0A   ; OUT ($BE),A
site 00F0C   ; OUTI
site 00F0E   ; OUTI
site 00F10   ; OUTI
site 00F12   ; OUT ($BE),A
site 00F14   ; OUTI
site 00F16   ; OUTI
site 00F18   ; OUTI
site 00F1A   ; OUT ($BE),A
site 00F1C   ; OUTI
site 00F1E   ; OUTI
site 00F20   ; OUTI
site 00F22   ; OUT ($BE),A
site 00F24   ; OUTI
site 00F26   ; OUTI
site 00F28   ; OUTI
site 00F2A   ; OUT ($BE),A
site 00F2C   ; OUTI
site 00F2E   ; OUTI
site 00F30   ; OUTI
site 00F32   ; OUT ($BE),A
site 00F34   ; OUTI
site 00F36   ; OUTI
site 00F38   ; OUTI
site 00F3A   ; OUT ($BE),A
site 00F3C   ; OUTI
site 00F3E   ; OUTI
site 00F40   ; OUTI
site 00F42   ; OUT ($BE),A
site 00F44   ; OUTI
site 00F46   ; OUTI
site 00F48   ; OUTI
site 00F4A   ; OUT ($BE),A
site 00F4C   ; OUTI
site 00F4E   ; OUTI
site 00F50   ; OUTI
site 00F52   ; OUT ($BE),A
site 0160C   ; OUT ($BF),A
site 0160F   ; OUT ($BF),A
site 01613   ; IN A,($BE)
site 01618   ; IN A,($BE)
site 01807   ; OUT ($BE),A
site 0181D   ; OUT ($BE),A
site 0182E   ; OUT ($BE),A
site 018CE   ; OUT ($BF),A
site 018D1   ; OUT ($BF),A
site 018DD   ; OUT ($BE),A
site 01A47   ; OUT ($BF),A
site 01A4A   ; OUT ($BF),A
site 01A4D   ; OUT ($BE),A
site 01A51   ; OUT ($BE),A
site 01B8C   ; OUT ($BF),A
site 01B8F   ; OUT ($BF),A
site 01B92   ; OUT ($BE),A
site 01B96   ; OUT ($BE),A
site 01BA1   ; OUT ($BF),A
site 01BA4   ; OUT ($BF),A
site 01BAA   ; OUT ($BE),A
site 01BAE   ; OUT ($BE),A
site 01C28   ; OUT ($BF),A
site 01C2B   ; OUT ($BF),A
site 01C2E   ; OUT ($BE),A
site 01C32   ; OUT ($BE),A
site 01C3D   ; OUT ($BF),A
site 01C40   ; OUT ($BF),A
site 01C46   ; OUT ($BE),A
site 01C4A   ; OUT ($BE),A
site 01E15   ; OUT ($BF),A
site 01E1A   ; OUT ($BF),A
site 01E1E   ; OUT ($BE),A
site 01E45   ; OUT ($BF),A
site 01E48   ; OUT ($BF),A
site 01E4C   ; OUT ($BE),A
site 01ED8   ; OUT ($BF),A
site 01EDB   ; OUT ($BF),A
site 01EE0   ; OUT ($BE),A
site 01F0F   ; IN A,($BE)
site 01F30   ; OUT ($BE),A
site 06C7B   ; IN A,($DC)
site 0C14D   ; OUT ($F0),A
site 0C156   ; OUT ($F1),A
site 0C16E   ; OUT ($7F),A
site 0C17E   ; OUT (C),D
site 0C184   ; OUT ($F1),A
site 0C1B7   ; OTIR
site 0C1C5   ; OTIR
site 0C1CF   ; OUT ($F0),A
site 0C1D5   ; OUT ($F1),A
site 0C1E1   ; OUTI
site 0C1E7   ; OUTI
site 0C3B5   ; OUT ($7F),A
site 0C3B9   ; OUT ($7F),A
site 0C3E1   ; OUT ($7F),A
site 0C3E5   ; OUT ($7F),A
site 0C3E8   ; OUT ($7F),A
site 0C44E   ; OUT ($F0),A
site 0C455   ; OUT ($F1),A
site 0C45D   ; OUT ($F0),A
site 0C463   ; OUT ($F1),A
site 0C558   ; OUT ($F0),A
site 0C562   ; OUT (C),L
site 0C56B   ; OUT ($F0),A
site 0C586   ; OUT (C),H
site 0C58E   ; OUT ($F0),A
site 0C59C   ; OUT ($F1),A
site 0C5A8   ; OUT ($F0),A
site 0C5B1   ; OUT ($F1),A
site 0C777   ; OUT ($F0),A
site 0C780   ; OUT (C),A
site 0C785   ; OUT ($F0),A
site 0C78B   ; OUTI
site 0C7FC   ; OUT ($7F),A
site 0C8C4   ; OUT ($7F),A
site 0C8EB   ; OUT ($7F),A
site 0C8F0   ; OUT ($7F),A
site 0C91C   ; OUT ($F0),A
site 0C92A   ; OUT ($F1),A
site 0C93B   ; OUT ($F0),A
site 0C9CF   ; OUTI
site 0C9D1   ; OUTI
site 0C9D3   ; OUTI
site 0C9D5   ; OUTI
site 0C9D7   ; OUTI
site 0C9D9   ; OUTI
site 0C9DB   ; OUTI
site 0C9DD   ; OUTI
site 0C9DF   ; OUTI
site 0C9E1   ; OUTI
site 0C9E3   ; OUTI
site 0C9ED   ; OUT (C),D
site 0C9F6   ; OUT ($F1),A
site 0CA38   ; OUT ($7F),A
site 0CA8E   ; OUT ($7F),A
site 0CACD   ; OUT ($7F),A
site 0CB2F   ; OUT ($7F),A
site 0CB4F   ; OUT ($7F),A
site 0CB8F   ; OUT ($7F),A
site 0CB99   ; OUT ($7F),A
site 0CBE1   ; OUT ($7F),A
mapst 0008F   ; LD ($FFFC),A
mapst 00094   ; LD ($FFFD),A
mapst 00099   ; LD ($FFFE),A
mapst 0009E   ; LD ($FFFF),A
mapst 000CD   ; LD ($FFFF),A
mapst 001AC   ; LD ($FFFF),A
mapst 00469   ; LD ($FFFF),A
mapst 00522   ; LD ($FFFF),A
mapst 005CE   ; LD ($FFFF),A
mapst 00648   ; LD ($FFFF),A
mapst 009DE   ; LD ($FFFF),A
mapst 009F5   ; LD ($FFFF),A
mapst 00A0B   ; LD ($FFFF),A
mapst 00A4E   ; LD ($FFFF),A
mapst 019BD   ; LD ($FFFF),A
mapst 01B53   ; LD ($FFFF),A
mapst 01BEF   ; LD ($FFFF),A
mapst 01F5A   ; LD ($FFFF),A
mapst 01F72   ; LD ($FFFF),A
mapst 020A9   ; LD ($FFFF),A
mapst 02197   ; LD ($FFFF),A
mapst 05117   ; LD ($FFFF),A
mapst 05191   ; LD ($FFFF),A
mapst 0519B   ; LD ($FFFF),A
mapst 051C5   ; LD ($FFFF),A
mapst 052D1   ; LD ($FFFF),A
mapst 05368   ; LD ($FFFF),A
mapst 053E5   ; LD ($FFFF),A
mapst 05451   ; LD ($FFFF),A
mapst 0549F   ; LD ($FFFF),A
mapst 05511   ; LD ($FFFF),A
mapst 05893   ; LD ($FFFF),A
mapst 058AB   ; LD ($FFFF),A
mapst 058D8   ; LD ($FFFF),A
mapst 0590D   ; LD ($FFFF),A
mapst 059F4   ; LD ($FFFF),A
mapst 05A7D   ; LD ($FFFF),A
mapst 05A90   ; LD ($FFFF),A
mapst 05BC4   ; LD ($FFFF),A
mapst 05BF6   ; LD ($FFFF),A
mapst 05DAE   ; LD ($FFFF),A
mapst 069FC   ; LD ($FFFF),A
mapst 06B70   ; LD ($FFFF),A
mapst 06B7E   ; LD ($FFFF),A
mapst 06BA0   ; LD ($FFFF),A
mapst 06BE1   ; LD ($FFFF),A
mapst 06EAE   ; LD ($FFFF),A
mapst 06EBC   ; LD ($FFFF),A
mapst 06ECC   ; LD ($FFFF),A
mapst 06EDA   ; LD ($FFFF),A
mapst 06F23   ; LD ($FFFF),A
mapst 06F9F   ; LD ($FFFF),A
mapst 06FB2   ; LD ($FFFF),A
mapst 06FD3   ; LD ($FFFF),A
mapst 06FF9   ; LD ($FFFF),A
site 001EC   ; OUT ($3F),A
site 001EE   ; IN A,($DD)
site 001F7   ; OUT ($3F),A
site 001F9   ; IN A,($DD)
site 00201   ; OUT ($DE),A
site 0030C   ; OUT ($BF),A
site 0030F   ; OUT ($BF),A
site 00313   ; IN A,($BE)
site 00358   ; OUT ($BF),A
site 0035B   ; OUT ($BF),A
site 00360   ; OUT ($BE),A
site 00365   ; OUT ($BE),A
site 01853   ; OUT ($BE),A
site 01859   ; OUT ($BE),A
site 01860   ; OUT ($BE),A
site 01866   ; OUT ($BE),A

# Lord of the Sword (USA, Europe, Brazil).cht, "Infinite Health": RAM $C129 is the health
# bar (a hit takes 3), held at $2F, so hits no longer lower it and the player does not die
poke "Infinite health"
ar 00C1-292F
endpoke

# Lord of the Sword (USA, Europe, Brazil).cht, "Invulnerability": RAM $C12C is the low byte of
# the timer that runs after a hit (the flag is $C12B). Held at $76, the timer never reaches
# zero, so after the first hit the player takes no more hits
poke "Invulnerability"
ar 00C1-2C76
endpoke
