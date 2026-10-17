# Castle of Illusion Starring Mickey Mouse (USA, Europe, Brazil) (Rev 1), CRC32 953F42E1, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of
# attract mode (30 minutes, no input) and play (10 minutes, start script and random input).
# The byte scan's I/O patterns in bank 0 at $01DA-$022F (name table row and tile writers),
# $062C-$0647, $07A5-$07A9 and $0851-$0854 are code that neither log ran, and are patched.
# The other byte scan I/O patterns are data: operands of other instructions
# ($0F18, $19B1, $1E3A, $397F) and graphics or map bytes in banks 3-15.
# The byte scan mapper stores in banks 0 and 1 are all code (LD A,n or LD A,($C0AA)
# then LD ($FFFF),A in level and object set-up routines), and are patched.
name Castle of Illusion Starring Mickey Mouse
cart 953F42E1
hz any		; No-Intro regions USA, Europe, Brazil
# The status bar (name table rows 20-23, H scroll 0) is all priority cells: Mickey goes behind
# it when he falls into a pit.
priority
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the runtime does DI and IM 2).
vector 00 io
# The line interrupt handler sets H scroll every 8 lines in the intro's castle scenes, and to 0
# for the status bar in play.
rastercode castleofillusion-raster.asm
start 0003
site 0002A   ; OUT ($BF),A
site 0002D   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 00187   ; OUT ($BE),A
site 001B7   ; OUTI
site 001C8   ; OUT ($BE),A
site 001CD   ; OUT ($BE),A
site 001F4   ; OUTI
site 00241   ; OUT ($BF),A
site 00244   ; OUT ($BF),A
site 00252   ; OUT ($BE),A
site 00260   ; IN A,($DC)
site 0026F   ; IN A,($DC)
site 00274   ; IN A,($DD)
site 00282   ; IN A,($DD)
site 003BA   ; IN A,($BF)
site 00486   ; IN A,($BF)
site 00488   ; IN A,($BF)
site 00494   ; IN A,($BF)
site 004C0   ; IN A,($BE)
site 004E2   ; OUT ($BE),A
site 00565   ; OUT ($BF),A
site 00568   ; OUT ($BF),A
site 0065A   ; OUT ($BF),A
site 0065E   ; OUT ($BF),A
site 00662   ; OUT ($BF),A
site 00666   ; OUT ($BF),A
site 00686   ; IN A,($DD)
site 006A6   ; OUT ($BF),A
site 006AA   ; OUT ($BF),A
site 006AE   ; OUT ($BF),A
site 006B2   ; OUT ($BF),A
site 006D8   ; OUT ($BF),A
site 006DC   ; OUT ($BF),A
site 006E4   ; OUT ($BF),A
site 006E8   ; OUT ($BF),A
site 006F3   ; OUT ($BF),A
site 006F6   ; OUT ($BF),A
site 00706   ; OUT ($BF),A
site 0070A   ; OUT ($BF),A
site 0070E   ; OUT ($BF),A
site 00712   ; OUT ($BF),A
site 0072B   ; OUT ($BF),A
site 0072F   ; OUT ($BF),A
site 00749   ; OUT ($BF),A
site 0074C   ; OUT ($BF),A
site 00751   ; OUTI
site 0184D   ; OUT ($BF),A
site 01851   ; OUT ($BF),A
site 01864   ; OUT (C),L
site 01869   ; OUT ($BF),A
site 0186E   ; OUT ($BE),A
site 01872   ; OUT ($BE),A
site 049FF   ; OUT ($BF),A
site 04A03   ; OUT ($BF),A
site 04A0A   ; OUTI
site 04A0C   ; OUTI
site 04A0E   ; OUTI
site 04A10   ; OUTI
site 04A12   ; OUTI
site 04A14   ; OUTI
site 04A16   ; OUTI
site 04A18   ; OUTI
site 04A1A   ; OUTI
site 04A1C   ; OUTI
site 04A1E   ; OUTI
site 04A20   ; OUTI
site 04A22   ; OUTI
site 04A24   ; OUTI
site 04A26   ; OUTI
site 04A28   ; OUTI
site 04A2A   ; OUTI
site 04A2C   ; OUTI
site 04A2E   ; OUTI
site 04A30   ; OUTI
site 04A32   ; OUTI
site 04A34   ; OUTI
site 04A36   ; OUTI
site 04A38   ; OUTI
site 04A3A   ; OUTI
site 04A3C   ; OUTI
site 04A3E   ; OUTI
site 04A40   ; OUTI
site 04A42   ; OUTI
site 04A44   ; OUTI
site 04A46   ; OUTI
site 04A48   ; OUTI
site 04A4A   ; OUTI
site 04A4C   ; OUTI
site 04A4E   ; OUTI
site 04A50   ; OUTI
site 04A52   ; OUTI
site 04A54   ; OUTI
site 04A56   ; OUTI
site 04A58   ; OUTI
site 04A5A   ; OUTI
site 04A5C   ; OUTI
site 04A5E   ; OUTI
site 04A60   ; OUTI
site 04A62   ; OUTI
site 04A64   ; OUTI
site 04A66   ; OUTI
site 04A68   ; OUTI
site 04A6A   ; OUTI
site 04A6C   ; OUTI
site 04A6E   ; OUTI
site 04A70   ; OUTI
site 04A72   ; OUTI
site 04A74   ; OUTI
site 04A76   ; OUTI
site 04A78   ; OUTI
site 04A7A   ; OUTI
site 04A7C   ; OUTI
site 04A7E   ; OUTI
site 04A80   ; OUTI
site 04A82   ; OUTI
site 04A84   ; OUTI
site 04A86   ; OUTI
site 04A88   ; OUTI
site 04A8A   ; OUTI
site 04A8C   ; OUTI
site 04A8E   ; OUTI
site 04A90   ; OUTI
site 04A92   ; OUTI
site 04A94   ; OUTI
site 04A96   ; OUTI
site 04A98   ; OUTI
site 04A9A   ; OUTI
site 04A9C   ; OUTI
site 04A9E   ; OUTI
site 04AA0   ; OUTI
site 04AA2   ; OUTI
site 04AA4   ; OUTI
site 04AA6   ; OUTI
site 04AA8   ; OUTI
site 04AAA   ; OUTI
site 04AAC   ; OUTI
site 04AAE   ; OUTI
site 04AB0   ; OUTI
site 04AB2   ; OUTI
site 04AB4   ; OUTI
site 04AB6   ; OUTI
site 04AB8   ; OUTI
site 04ABA   ; OUTI
site 04ABC   ; OUTI
site 04ABE   ; OUTI
site 04AC0   ; OUTI
site 04AC2   ; OUTI
site 04AC4   ; OUTI
site 04AC6   ; OUTI
site 04AC8   ; OUTI
site 04ACA   ; OUTI
site 04ACC   ; OUTI
site 04ACE   ; OUTI
site 04AD0   ; OUTI
site 04AD2   ; OUTI
site 04AD4   ; OUTI
site 04AD6   ; OUTI
site 04AD8   ; OUTI
site 04ADA   ; OUTI
site 04ADC   ; OUTI
site 04ADE   ; OUTI
site 04AE0   ; OUTI
site 04AE2   ; OUTI
site 04AE4   ; OUTI
site 04AE6   ; OUTI
site 04AE8   ; OUTI
site 04AEA   ; OUTI
site 04AEC   ; OUTI
site 04AEE   ; OUTI
site 04AF0   ; OUTI
site 04AF2   ; OUTI
site 04AF4   ; OUTI
site 04AF6   ; OUTI
site 04AF8   ; OUTI
site 04AFA   ; OUTI
site 04AFC   ; OUTI
site 04AFE   ; OUTI
site 04B00   ; OUTI
site 04B02   ; OUTI
site 04B04   ; OUTI
site 04B06   ; OUTI
site 04B08   ; OUTI
site 04B0A   ; OUTI
site 04B0C   ; OUTI
site 04B0E   ; OUTI
site 04B10   ; OUTI
site 04B12   ; OUTI
site 04B14   ; OUTI
site 04B16   ; OUTI
site 04B18   ; OUTI
site 04B1A   ; OUTI
site 04B1C   ; OUTI
site 04B1E   ; OUTI
site 04B20   ; OUTI
site 04B22   ; OUTI
site 04B24   ; OUTI
site 04B26   ; OUTI
site 04B28   ; OUTI
site 04B2A   ; OUTI
site 04B2C   ; OUTI
site 04B2E   ; OUTI
site 04B30   ; OUTI
site 04B32   ; OUTI
site 04B34   ; OUTI
site 04B36   ; OUTI
site 04B38   ; OUTI
site 04B3A   ; OUTI
site 04B3C   ; OUTI
site 04B3E   ; OUTI
site 04B40   ; OUTI
site 04B42   ; OUTI
site 04B44   ; OUTI
site 04B46   ; OUTI
site 04B48   ; OUTI
site 04B4A   ; OUTI
site 04B4C   ; OUTI
site 04B4E   ; OUTI
site 04B50   ; OUTI
site 04B52   ; OUTI
site 04B54   ; OUTI
site 04B56   ; OUTI
site 04B58   ; OUTI
site 04B5A   ; OUTI
site 04B5C   ; OUTI
site 04B5E   ; OUTI
site 04B60   ; OUTI
site 04B62   ; OUTI
site 04B64   ; OUTI
site 04B66   ; OUTI
site 04B68   ; OUTI
site 04B6A   ; OUTI
site 04B6C   ; OUTI
site 04B6E   ; OUTI
site 04B70   ; OUTI
site 04B72   ; OUTI
site 04B74   ; OUTI
site 04B76   ; OUTI
site 04B78   ; OUTI
site 04B7A   ; OUTI
site 04B7C   ; OUTI
site 04B7E   ; OUTI
site 04B80   ; OUTI
site 04B82   ; OUTI
site 04B84   ; OUTI
site 04B86   ; OUTI
site 04B88   ; OUTI
site 04B8A   ; OUTI
site 04B8C   ; OUTI
site 04B8E   ; OUTI
site 04B90   ; OUTI
site 04B92   ; OUTI
site 04B94   ; OUTI
site 04B96   ; OUTI
site 04B98   ; OUTI
site 04B9A   ; OUTI
site 04B9C   ; OUTI
site 04B9E   ; OUTI
site 04BA0   ; OUTI
site 04BA2   ; OUTI
site 04BA4   ; OUTI
site 04BA6   ; OUTI
site 04BA8   ; OUTI
site 04BAA   ; OUTI
site 04BAC   ; OUTI
site 04BAE   ; OUTI
site 04BB0   ; OUTI
site 04BB2   ; OUTI
site 04BB4   ; OUTI
site 04BB6   ; OUTI
site 04BB8   ; OUTI
site 04BBA   ; OUTI
site 04BBC   ; OUTI
site 04BBE   ; OUTI
site 04BC0   ; OUTI
site 04BC2   ; OUTI
site 04BC4   ; OUTI
site 04BC6   ; OUTI
site 04BC8   ; OUTI
site 04BCA   ; OUTI
site 04BCC   ; OUTI
site 04BCE   ; OUTI
site 04BD0   ; OUTI
site 04BD2   ; OUTI
site 04BD4   ; OUTI
site 04BD6   ; OUTI
site 04BD8   ; OUTI
site 04BDA   ; OUTI
site 04BDC   ; OUTI
site 04BDE   ; OUTI
site 04BE0   ; OUTI
site 04BE2   ; OUTI
site 04BE4   ; OUTI
site 04BE6   ; OUTI
site 04BE8   ; OUTI
site 04BEA   ; OUTI
site 04BEC   ; OUTI
site 04BEE   ; OUTI
site 04BF0   ; OUTI
site 04BF2   ; OUTI
site 04BF4   ; OUTI
site 04BF6   ; OUTI
site 04BF8   ; OUTI
site 04BFA   ; OUTI
site 04BFC   ; OUTI
site 04BFE   ; OUTI
site 04C00   ; OUTI
site 04C02   ; OUTI
site 04C04   ; OUTI
site 04C06   ; OUTI
site 04C08   ; OUTI
site 04C0A   ; OUTI
site 04C0C   ; OUTI
site 04C0E   ; OUTI
site 04C10   ; OUTI
site 04C12   ; OUTI
site 04C14   ; OUTI
site 04C16   ; OUTI
site 04C18   ; OUTI
site 04C1A   ; OUTI
site 04C1C   ; OUTI
site 04C1E   ; OUTI
site 04C20   ; OUTI
site 04C22   ; OUTI
site 04C24   ; OUTI
site 04C26   ; OUTI
site 04C28   ; OUTI
site 04C2A   ; OUTI
site 04C2C   ; OUTI
site 04C2E   ; OUTI
site 04C30   ; OUTI
site 04C32   ; OUTI
site 04C34   ; OUTI
site 04C36   ; OUTI
site 04C38   ; OUTI
site 04C3A   ; OUTI
site 04C3C   ; OUTI
site 04C3E   ; OUTI
site 04C40   ; OUTI
site 04C42   ; OUTI
site 04C44   ; OUTI
site 04C46   ; OUTI
site 04C48   ; OUTI
site 04C4A   ; OUTI
site 04C4C   ; OUTI
site 04C4E   ; OUTI
site 04C50   ; OUTI
site 04C52   ; OUTI
site 04C54   ; OUTI
site 04C56   ; OUTI
site 04C58   ; OUTI
site 04C5A   ; OUTI
site 04C5C   ; OUTI
site 04C5E   ; OUTI
site 04C60   ; OUTI
site 04C62   ; OUTI
site 04C64   ; OUTI
site 04C66   ; OUTI
site 04C68   ; OUTI
site 04C6A   ; OUTI
site 04C6C   ; OUTI
site 04C6E   ; OUTI
site 04C70   ; OUTI
site 04C72   ; OUTI
site 04C74   ; OUTI
site 04C76   ; OUTI
site 04C78   ; OUTI
site 04C7A   ; OUTI
site 04C7C   ; OUTI
site 04C7E   ; OUTI
site 04C80   ; OUTI
site 04C82   ; OUTI
site 04C84   ; OUTI
site 04C86   ; OUTI
site 04C88   ; OUTI
site 04C8A   ; OUTI
site 04C8C   ; OUTI
site 04C8E   ; OUTI
site 04C90   ; OUTI
site 04C92   ; OUTI
site 04C94   ; OUTI
site 04C96   ; OUTI
site 04C98   ; OUTI
site 04C9A   ; OUTI
site 04C9C   ; OUTI
site 04C9E   ; OUTI
site 04CA0   ; OUTI
site 04CA2   ; OUTI
site 04CA4   ; OUTI
site 04CA6   ; OUTI
site 04CA8   ; OUTI
site 04CAA   ; OUTI
site 04CAC   ; OUTI
site 04CAE   ; OUTI
site 04CB0   ; OUTI
site 04CB2   ; OUTI
site 04CB4   ; OUTI
site 04CB6   ; OUTI
site 04CB8   ; OUTI
site 04CBA   ; OUTI
site 04CBC   ; OUTI
site 04CBE   ; OUTI
site 04CC0   ; OUTI
site 04CC2   ; OUTI
site 04CC4   ; OUTI
site 04CC6   ; OUTI
site 04CC8   ; OUTI
site 04CCA   ; OUTI
site 04CCC   ; OUTI
site 04CCE   ; OUTI
site 04CD0   ; OUTI
site 04CD2   ; OUTI
site 04CD4   ; OUTI
site 04CD6   ; OUTI
site 04CD8   ; OUTI
site 04CDA   ; OUTI
site 04CDC   ; OUTI
site 04CDE   ; OUTI
site 04CE0   ; OUTI
site 04CE2   ; OUTI
site 04CE4   ; OUTI
site 04CE6   ; OUTI
site 04CE8   ; OUTI
site 04CEA   ; OUTI
site 04CEC   ; OUTI
site 04CEE   ; OUTI
site 04CF0   ; OUTI
site 04CF2   ; OUTI
site 04CF4   ; OUTI
site 04CF6   ; OUTI
site 04CF8   ; OUTI
site 04CFA   ; OUTI
site 04CFC   ; OUTI
site 04CFE   ; OUTI
site 04D00   ; OUTI
site 04D02   ; OUTI
site 04D04   ; OUTI
site 04D06   ; OUTI
site 04D08   ; OUTI
site 04D0A   ; OUTI
site 04D0C   ; OUTI
site 04D0E   ; OUTI
site 04D10   ; OUTI
site 04D12   ; OUTI
site 04D14   ; OUTI
site 04D16   ; OUTI
site 04D18   ; OUTI
site 04D1A   ; OUTI
site 04D1C   ; OUTI
site 04D1E   ; OUTI
site 04D20   ; OUTI
site 04D22   ; OUTI
site 04D24   ; OUTI
site 04D26   ; OUTI
site 04D28   ; OUTI
site 04D2A   ; OUTI
site 04D2C   ; OUTI
site 04D2E   ; OUTI
site 04D30   ; OUTI
site 04D32   ; OUTI
site 04D34   ; OUTI
site 04D36   ; OUTI
site 04D38   ; OUTI
site 04D3A   ; OUTI
site 04D3C   ; OUTI
site 04D3E   ; OUTI
site 04D40   ; OUTI
site 04D42   ; OUTI
site 04D44   ; OUTI
site 04D46   ; OUTI
site 04D48   ; OUTI
site 04D4A   ; OUTI
site 04D4C   ; OUTI
site 04D4E   ; OUTI
site 04D50   ; OUTI
site 04D52   ; OUTI
site 04D54   ; OUTI
site 04D56   ; OUTI
site 04D58   ; OUTI
site 04D5A   ; OUTI
site 04D5C   ; OUTI
site 04D5E   ; OUTI
site 04D60   ; OUTI
site 04D62   ; OUTI
site 04D64   ; OUTI
site 04D66   ; OUTI
site 04D68   ; OUTI
site 04D6A   ; OUTI
site 04D6C   ; OUTI
site 04D6E   ; OUTI
site 04D70   ; OUTI
site 04D72   ; OUTI
site 04D74   ; OUTI
site 04D76   ; OUTI
site 04D78   ; OUTI
site 04D7A   ; OUTI
site 04D7C   ; OUTI
site 04D7E   ; OUTI
site 04D80   ; OUTI
site 04D82   ; OUTI
site 04D84   ; OUTI
site 04D86   ; OUTI
site 04D88   ; OUTI
site 04D8A   ; OUTI
site 04D8C   ; OUTI
site 04D8E   ; OUTI
site 04D90   ; OUTI
site 04D92   ; OUTI
site 04D94   ; OUTI
site 04D96   ; OUTI
site 04D98   ; OUTI
site 04D9A   ; OUTI
site 04D9C   ; OUTI
site 04D9E   ; OUTI
site 04DA0   ; OUTI
site 04DA2   ; OUTI
site 04DA4   ; OUTI
site 04DA6   ; OUTI
site 04DA8   ; OUTI
site 04DAA   ; OUTI
site 04DAC   ; OUTI
site 04DAE   ; OUTI
site 04DB0   ; OUTI
site 04DB2   ; OUTI
site 04DB4   ; OUTI
site 04DB6   ; OUTI
site 04DB8   ; OUTI
site 04DBA   ; OUTI
site 04DBC   ; OUTI
site 04DBE   ; OUTI
site 04DC0   ; OUTI
site 04DC2   ; OUTI
site 04DC4   ; OUTI
site 04DC6   ; OUTI
site 04DC8   ; OUTI
site 04DCA   ; OUTI
site 04DCC   ; OUTI
site 04DCE   ; OUTI
site 04DD0   ; OUTI
site 04DD2   ; OUTI
site 04DD4   ; OUTI
site 04DD6   ; OUTI
site 04DD8   ; OUTI
site 04DDA   ; OUTI
site 04DDC   ; OUTI
site 04DDE   ; OUTI
site 04DE0   ; OUTI
site 04DE2   ; OUTI
site 04DE4   ; OUTI
site 04DE6   ; OUTI
site 04DE8   ; OUTI
site 04DEA   ; OUTI
site 04DEC   ; OUTI
site 04DEE   ; OUTI
site 04DF0   ; OUTI
site 04DF2   ; OUTI
site 04DF4   ; OUTI
site 04DF6   ; OUTI
site 04DF8   ; OUTI
site 04DFA   ; OUTI
site 04DFC   ; OUTI
site 04DFE   ; OUTI
site 04E00   ; OUTI
site 04E02   ; OUTI
site 04E04   ; OUTI
site 04E06   ; OUTI
site 04E08   ; OUTI
site 04E0A   ; OUTI
site 04E0C   ; OUTI
site 04E0E   ; OUTI
site 04E10   ; OUTI
site 04E12   ; OUTI
site 04E14   ; OUTI
site 04E16   ; OUTI
site 04E18   ; OUTI
site 04E1A   ; OUTI
site 04E1C   ; OUTI
site 04E1E   ; OUTI
site 04E20   ; OUTI
site 04E22   ; OUTI
site 04E24   ; OUTI
site 04E26   ; OUTI
site 04E28   ; OUTI
site 04E2A   ; OUTI
site 04E2C   ; OUTI
site 04E2E   ; OUTI
site 04E30   ; OUTI
site 04E32   ; OUTI
site 04E34   ; OUTI
site 04E36   ; OUTI
site 04E38   ; OUTI
site 04E3A   ; OUTI
site 04E3C   ; OUTI
site 04E3E   ; OUTI
site 04E40   ; OUTI
site 04E42   ; OUTI
site 04E44   ; OUTI
site 04E46   ; OUTI
site 04E48   ; OUTI
site 04E4A   ; OUTI
site 04E4C   ; OUTI
site 04E4E   ; OUTI
site 04E50   ; OUTI
site 04E52   ; OUTI
site 04E54   ; OUTI
site 04E56   ; OUTI
site 04E58   ; OUTI
site 04E5A   ; OUTI
site 04E5C   ; OUTI
site 04E5E   ; OUTI
site 04E60   ; OUTI
site 04E62   ; OUTI
site 04E64   ; OUTI
site 04E66   ; OUTI
site 04E68   ; OUTI
site 04E6A   ; OUTI
site 04E6C   ; OUTI
site 04E6E   ; OUTI
site 04E70   ; OUTI
site 04E72   ; OUTI
site 04E74   ; OUTI
site 04E76   ; OUTI
site 04E78   ; OUTI
site 04E7A   ; OUTI
site 04E7C   ; OUTI
site 04E7E   ; OUTI
site 04E80   ; OUTI
site 04E82   ; OUTI
site 04E84   ; OUTI
site 04E86   ; OUTI
site 04E88   ; OUTI
site 04E8A   ; OUTI
site 04E8C   ; OUTI
site 04E8E   ; OUTI
site 04E90   ; OUTI
site 04E92   ; OUTI
site 04E94   ; OUTI
site 04E96   ; OUTI
site 04E98   ; OUTI
site 04E9A   ; OUTI
site 04E9C   ; OUTI
site 04E9E   ; OUTI
site 04EA0   ; OUTI
site 04EA2   ; OUTI
site 04EA4   ; OUTI
site 04EA6   ; OUTI
site 04EA8   ; OUTI
site 04EAA   ; OUTI
site 04EAC   ; OUTI
site 04EAE   ; OUTI
site 04EB0   ; OUTI
site 04EB2   ; OUTI
site 04EB4   ; OUTI
site 04EB6   ; OUTI
site 04EB8   ; OUTI
site 04EBA   ; OUTI
site 04EBC   ; OUTI
site 04EBE   ; OUTI
site 04EC0   ; OUTI
site 04EC2   ; OUTI
site 04EC4   ; OUTI
site 04EC6   ; OUTI
site 04EC8   ; OUTI
site 04ECA   ; OUTI
site 04ECC   ; OUTI
site 04ECE   ; OUTI
site 04ED0   ; OUTI
site 04ED2   ; OUTI
site 04ED4   ; OUTI
site 04ED6   ; OUTI
site 04ED8   ; OUTI
site 04EDA   ; OUTI
site 04EDC   ; OUTI
site 04EDE   ; OUTI
site 04EE0   ; OUTI
site 04EE2   ; OUTI
site 04EE4   ; OUTI
site 04EE6   ; OUTI
site 04EE8   ; OUTI
site 04EEA   ; OUTI
site 04EEC   ; OUTI
site 04EEE   ; OUTI
site 04EF0   ; OUTI
site 04EF2   ; OUTI
site 04EF4   ; OUTI
site 04EF6   ; OUTI
site 04EF8   ; OUTI
site 04EFA   ; OUTI
site 04EFC   ; OUTI
site 04EFE   ; OUTI
site 04F00   ; OUTI
site 04F02   ; OUTI
site 04F04   ; OUTI
site 04F06   ; OUTI
site 04F08   ; OUTI
site 06DFC   ; OUT ($BF),A
site 06E00   ; OUT ($BF),A
site 06E14   ; OUT ($BE),A
site 06E17   ; OUT ($BE),A
site 06E23   ; OUT ($BE),A
site 06E26   ; OUT ($BE),A
site 06E2D   ; OUT ($BE),A
site 06E30   ; OUT ($BE),A
site 08199   ; OUT ($7F),A
site 081B1   ; OUT ($7F),A
site 0838F   ; OTIR
site 084A5   ; OUT ($7F),A
site 084AF   ; OUT ($7F),A
site 084CC   ; OUT ($7F),A
site 085D0   ; OUT ($7F),A
site 0865E   ; OUT ($7F),A
site 086E2   ; OUT ($7F),A
site 086F2   ; OUT ($7F),A
site 08766   ; OUT ($7F),A
mapst 000CC   ; LD ($FFFF),A
mapst 000E5   ; LD ($FFFF),A
mapldk 000FB   # LD HL,$FFFC; LD (HL),$80
maphl 00101   # LD (HL),$00, HL = $FFFD
maphl 00104   # LD (HL),$01, HL = $FFFE
maphl 00107   # LD (HL),$02, HL = $FFFF
mapst 00125   ; LD ($FFFF),A
mapst 00470   ; LD ($FFFF),A
mapst 00571   ; LD ($FFFF),A
mapst 008C4   ; LD ($FFFF),A
mapst 008DF   ; LD ($FFFF),A
mapst 00965   ; LD ($FFFF),A
mapst 00B6E   ; LD ($FFFF),A
mapst 00B76   ; LD ($FFFF),A
mapst 00BA2   ; LD ($FFFF),A
mapst 00BB0   ; LD ($FFFF),A
mapst 00BDE   ; LD ($FFFF),A
mapst 00C1D   ; LD ($FFFF),A
mapst 00C9B   ; LD ($FFFF),A
mapst 00D44   ; LD ($FFFF),A
mapst 00DA4   ; LD ($FFFF),A
mapst 00DF5   ; LD ($FFFF),A
mapst 011EF   ; LD ($FFFF),A
mapst 01229   ; LD ($FFFF),A
mapst 012D6   ; LD ($FFFF),A
mapst 01529   ; LD ($FFFF),A
mapst 01596   ; LD ($FFFF),A
mapst 01924   ; LD ($FFFF),A
mapst 022A9   ; LD ($FFFF),A
mapst 04001   ; LD ($FFFF),A
mapst 0414A   ; LD ($FFFF),A
mapst 04F0D   ; LD ($FFFF),A
mapst 0638D   ; LD ($FFFF),A
mapst 063B0   ; LD ($FFFF),A
mapst 06475   ; LD ($FFFF),A
mapst 065DC   ; LD ($FFFF),A
mapst 069DE   ; LD ($FFFF),A
mapst 06A14   ; LD ($FFFF),A
mapst 06B84   ; LD ($FFFF),A
mapst 06BE3   ; LD ($FFFF),A
mapst 06C76   ; LD ($FFFF),A
mapst 06CD0   ; LD ($FFFF),A
mapst 06D08   ; LD ($FFFF),A
mapst 06DF7   ; LD ($FFFF),A
mapst 06E35   ; LD ($FFFF),A
mapst 06E8B   ; LD ($FFFF),A
mapst 06EAA   ; LD ($FFFF),A
mapst 06EFE   ; LD ($FFFF),A
mapst 06F0F   ; LD ($FFFF),A
mapst 06F2E   ; LD ($FFFF),A
mapst 06F61   ; LD ($FFFF),A
mapst 06FB7   ; LD ($FFFF),A
# $0012 JP (HL) is the end of RST $08, a jump through a table of words that its callers pass in HL.
# $0B71 CALL $8386 runs with bank 2 in slot 2 (LD A,$02 before it); $8386 is the sound driver's
# PSG reset, reached through the JP $8386 at the start of bank 2 and patched below.
# Mapper stores found by the byte scan in bytes no path reached:
mapst 007EF   # LD ($FFFF),A; after LD A,$0F; 32 bytes of valid code before it
mapst 0082E   # LD ($FFFF),A; after LD A,$0F; 32 bytes of valid code before it
mapst 00868   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 0087C   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 008AF   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 0098F   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 009A8   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 009CC   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 009F1   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 00AA3   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 00AB4   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 00F14   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 00F5E   # LD ($FFFF),A; after LD A,$05; JP/CALL target from $33809; 32 bytes of valid code before it
mapst 01005   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 01015   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
mapst 01023   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 01031   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 0103F   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
mapst 010B8   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
mapst 011C1   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 0194E   # LD ($FFFF),A; after LD A,($C0AA); 32 bytes of valid code before it
mapst 0195F   # LD ($FFFF),A; after LD A,($C0AA); 32 bytes of valid code before it
mapst 01970   # LD ($FFFF),A; after LD A,($C0AA); 32 bytes of valid code before it
mapst 01D92   # LD ($FFFF),A; after LD A,($C0AA); 32 bytes of valid code before it
mapst 01DA3   # LD ($FFFF),A; after LD A,($C0AA); 32 bytes of valid code before it
mapst 01DB4   # LD ($FFFF),A; after LD A,($C0AA); 32 bytes of valid code before it
mapst 01F07   # LD ($FFFF),A; after LD A,$0F; 32 bytes of valid code before it
mapst 01F89   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 06233   # LD ($FFFF),A; after LD A,$07; 32 bytes of valid code before it
mapst 06243   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 0624E   # LD ($FFFF),A; after LD A,$07; 32 bytes of valid code before it
mapst 06289   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 064B0   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 064E3   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 06656   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 06788   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 067B0   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 06892   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 068D6   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 0702B   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 0704D   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
site 001DA   ; OUTI
site 001E0   ; OUT
site 00219   ; OUT
site 00229   ; OUTI
site 0022F   ; OUT
site 0062C   ; OUT
site 00630   ; OUT
site 00639   ; OUTI
site 0063F   ; OUTI
site 00647   ; OUTI
site 007A5   ; OUT
site 007A9   ; OUT
site 00851   ; OUT
site 00854   ; OUT
# Tile unpacker at $0172 (the Sega planar RLE decoder, with JR Z where the usual copy has RET Z),
# called with HL = the data and DE = a VRAM write address: four bit planes, each a list of runs
# (a count byte n, then n AND $7F bytes when n has bit 7, or one byte repeated n times; 0 ends
# the plane), every fourth VRAM byte, the next plane one byte later. It sets the VRAM address and
# writes each byte with interrupts off: about 2,450 Next cycles a byte through the traps, about
# 60 frames for the screens of one level load. rle_tiles unpacks each plane into a buffer and
# writes it with jt_vwrite. Its OUT ($BE),A at $0187 keeps its site line but is no longer reached.
asm 00172 5          ; LD B,4 : EX AF,AF' : LD A,B : EX AF,AF': the routine is rle_tiles
    rst $00
    db far_io, pg_rle_tiles, ent_rle_tiles
    ret
endasm
libpage 0 rle_tiles  ; overlays/lib/rle_tiles.asm
