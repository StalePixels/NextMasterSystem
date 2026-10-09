# OutRun, drafted by tools/mkspec.py from sitescan output.
name OutRun
cart 5589D8D2
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 00101   ; IN A,($DC)
site 0011C   ; OUT ($3F),A
site 00122   ; IN A,($DC)
site 00129   ; OUT ($3F),A
site 0012F   ; IN A,($DC)
site 0017A   ; IN A,($DD)
site 0020B   ; OUT ($BF),A
site 0020F   ; OUT ($BF),A
site 00214   ; OUT ($BF),A
site 00218   ; OUT ($BF),A
site 00226   ; IN A,($7E)
site 0022E   ; OUT ($BF),A
site 00232   ; OUT ($BF),A
site 0024B   ; OUT ($BF),A
site 0024F   ; OUT ($BF),A
site 00270   ; OUT ($BF),A
site 00274   ; OUT ($BF),A
site 00279   ; OUT ($BF),A
site 0027D   ; OUT ($BF),A
site 0028B   ; IN A,($7E)
site 00293   ; OUT ($BF),A
site 00297   ; OUT ($BF),A
site 002EC   ; OUT ($BF),A
site 002F0   ; OUT ($BF),A
site 00346   ; OUT ($BF),A
site 0034A   ; OUT ($BF),A
site 0034F   ; OUT ($BF),A
site 00353   ; OUT ($BF),A
site 0035B   ; IN A,($7E)
site 00363   ; OUT ($BF),A
site 00367   ; OUT ($BF),A
site 0036F   ; OUT ($BF),A
site 00373   ; OUT ($BF),A
site 00378   ; OUT ($BF),A
site 0037C   ; OUT ($BF),A
site 0039A   ; IN A,($7E)
site 003A2   ; OUT ($BF),A
site 003A6   ; OUT ($BF),A
site 003B5   ; OUT ($BF),A
site 003B9   ; OUT ($BF),A
site 003BE   ; OUT ($BF),A
site 003C2   ; OUT ($BF),A
site 003D2   ; IN A,($7E)
site 003DA   ; OUT ($BF),A
site 003DE   ; OUT ($BF),A
site 003F0   ; OUT ($BF),A
site 003F4   ; OUT ($BF),A
site 003F9   ; OUT ($BF),A
site 003FD   ; OUT ($BF),A
site 0041C   ; IN A,($7E)
site 00424   ; OUT ($BF),A
site 00428   ; OUT ($BF),A
site 0043C   ; OUT ($BF),A
site 00440   ; OUT ($BF),A
site 00450   ; OUT ($BF),A
site 00454   ; OUT ($BF),A
site 00465   ; OUT ($BF),A
site 00469   ; OUT ($BF),A
site 00475   ; OUT ($BF),A
site 00479   ; OUT ($BF),A
otir 00494   ; OUTI
otir 00499   ; OUTI
site 007B0   ; OUT ($BF),A
site 007B4   ; OUT ($BF),A
site 007CD   ; OUT ($BF),A
site 007D1   ; OUT ($BF),A
site 007D6   ; OUT ($BF),A
site 007DA   ; OUT ($BF),A
site 007DF   ; IN A,($7E)
site 007E7   ; OUT ($BF),A
site 007EB   ; OUT ($BF),A
site 007F0   ; IN A,($7E)
site 007F9   ; OUT ($BF),A
site 007FD   ; OUT ($BF),A
site 0082C   ; OUT ($3F),A
site 0082E   ; IN A,($DD)
site 00838   ; OUT ($3F),A
site 0083A   ; IN A,($DD)
site 00843   ; OUT ($3F),A
site 00851   ; IN A,($BF)
site 00857   ; IN A,($BF)
site 0085E   ; IN A,($BF)
site 00871   ; OUT ($3E),A
site 00875   ; OUT ($F2),A
site 00877   ; IN A,($F2)
site 00880   ; OUT ($F2),A
site 00887   ; OUT ($3E),A
site 00891   ; IN A,($DC)
site 008A3   ; IN A,($DC)
site 008C3   ; IN A,($DC)
site 008CC   ; IN A,($DC)
site 008F2   ; OUT ($3F),A
site 008F8   ; IN A,($DC)
site 00900   ; OUT ($3F),A
site 00906   ; IN A,($DC)
otir 00925   ; OUTI
site 0093F   ; OUT ($BE),A
site 00944   ; OUT ($BE),A
site 00951   ; OUTI
site 00957   ; OUT (C),A
otir 0096A   ; OUTI
site 00987   ; OUT ($BE),A
site 0098C   ; OUT ($BE),A
site 009C0   ; OUT (C),D
site 009D3   ; OTIR
site 00A10   ; OUT ($BE),A
site 00A98   ; OUT ($BE),A
site 00F0A   ; OUT ($BE),A
site 01108   ; OUT ($BF),A
site 0110B   ; OUT ($BF),A
site 01111   ; IN A,($BE)
site 01118   ; IN A,($BE)
site 01127   ; OUT ($BF),A
site 0112A   ; OUT ($BF),A
site 01135   ; IN A,($BE)
site 0113F   ; OUT ($BF),A
site 01142   ; OUT ($BF),A
site 0114D   ; IN A,($BE)
site 01160   ; OUT ($BF),A
site 01163   ; OUT ($BF),A
site 0116B   ; OUT ($BE),A
site 011A3   ; IN A,($7E)
site 011B1   ; OUT ($BF),A
site 011B6   ; OUT ($BF),A
site 011BC   ; IN A,($BE)
site 011C4   ; OUT ($BF),A
site 011C9   ; OUT ($BF),A
site 011DD   ; OUT ($BE),A
site 013BC   ; OUT ($F2),A
site 0147C   ; OUT ($F2),A
site 017E8   ; OUT (C),E
site 017EA   ; OUT (C),E
site 017EC   ; OUT (C),E
site 017EE   ; OUT (C),D
site 017F0   ; OUT (C),D
site 017F2   ; OUT (C),D
site 017F4   ; OUT (C),L
site 017F6   ; OUT (C),L
site 017F8   ; OUT (C),L
site 017FA   ; OUT (C),H
site 017FC   ; OUT (C),H
site 017FE   ; OUT (C),H
site 01804   ; OUT (C),E
site 01806   ; OUT (C),E
site 01808   ; OUT (C),D
site 0180A   ; OUT (C),D
site 0180C   ; OUT (C),D
site 0180E   ; OUT (C),E
site 01810   ; OUT (C),L
site 01812   ; OUT (C),L
site 01814   ; OUT (C),H
site 01816   ; OUT (C),H
site 01818   ; OUT (C),H
site 0181A   ; OUT (C),L
site 01820   ; OUT (C),E
site 01822   ; OUT (C),D
site 01824   ; OUT (C),D
site 01826   ; OUT (C),D
site 01828   ; OUT (C),E
site 0182A   ; OUT (C),E
site 0182C   ; OUT (C),L
site 0182E   ; OUT (C),H
site 01830   ; OUT (C),H
site 01832   ; OUT (C),H
site 01834   ; OUT (C),L
site 01836   ; OUT (C),L
site 0183C   ; OUT (C),D
site 0183E   ; OUT (C),D
site 01840   ; OUT (C),D
site 01842   ; OUT (C),E
site 01844   ; OUT (C),E
site 01846   ; OUT (C),E
site 01848   ; OUT (C),H
site 0184A   ; OUT (C),H
site 0184C   ; OUT (C),H
site 0184E   ; OUT (C),L
site 01850   ; OUT (C),L
site 01852   ; OUT (C),L
site 01858   ; OUT (C),D
site 0185A   ; OUT (C),D
site 0185C   ; OUT (C),E
site 0185E   ; OUT (C),E
site 01860   ; OUT (C),E
site 01862   ; OUT (C),D
site 01864   ; OUT (C),H
site 01866   ; OUT (C),H
site 01868   ; OUT (C),L
site 0186A   ; OUT (C),L
site 0186C   ; OUT (C),L
site 0186E   ; OUT (C),H
site 01874   ; OUT (C),D
site 01876   ; OUT (C),E
site 01878   ; OUT (C),E
site 0187A   ; OUT (C),E
site 0187C   ; OUT (C),D
site 0187E   ; OUT (C),D
site 01880   ; OUT (C),H
site 01882   ; OUT (C),L
site 01884   ; OUT (C),L
site 01886   ; OUT (C),L
site 01888   ; OUT (C),H
site 0188A   ; OUT (C),H
site 018A8   ; OUT (C),B
site 018AF   ; OUT (C),B
site 018B6   ; OUT (C),B
site 018BD   ; OUT (C),B
site 0204E   ; OUT ($BE),A
site 02054   ; OUT ($BE),A
site 0205E   ; OUT ($BE),A
site 02064   ; OUT ($BE),A
site 03DB6   ; OUTI
site 03DB8   ; OUTI
site 03DBA   ; OUTI
site 03DBC   ; OUTI
site 03DBE   ; OUTI
site 03DC0   ; OUTI
site 03DC2   ; OUTI
site 03DC4   ; OUTI
site 03DC6   ; OUTI
site 03DC8   ; OUTI
site 03DCA   ; OUTI
site 03DCC   ; OUTI
site 03DCE   ; OUTI
site 03DD0   ; OUTI
site 03DD2   ; OUTI
site 03DD4   ; OUTI
site 03DD6   ; OUTI
site 03DD8   ; OUTI
site 03DDA   ; OUTI
site 03DDC   ; OUTI
site 03DDE   ; OUTI
site 03DE0   ; OUTI
site 03DE2   ; OUTI
site 03DE4   ; OUTI
site 03DE6   ; OUTI
site 03DE8   ; OUTI
site 03DEA   ; OUTI
site 03DEC   ; OUTI
site 03DEE   ; OUTI
site 03DF0   ; OUTI
site 03DF2   ; OUTI
site 03DF4   ; OUTI
site 03DF6   ; OUTI
site 03DF8   ; OUTI
site 03DFA   ; OUTI
site 03DFC   ; OUTI
site 03DFE   ; OUTI
site 03E00   ; OUTI
site 03E02   ; OUTI
site 03E04   ; OUTI
site 03E06   ; OUTI
site 03E08   ; OUTI
site 03E0A   ; OUTI
site 03E0C   ; OUTI
site 03E0E   ; OUTI
site 03E10   ; OUTI
site 03E12   ; OUTI
site 03E14   ; OUTI
site 03E16   ; OUTI
site 03E18   ; OUTI
site 03E1A   ; OUTI
site 03E1C   ; OUTI
site 03E1E   ; OUTI
site 03E20   ; OUTI
site 03E22   ; OUTI
site 03E24   ; OUTI
site 03E26   ; OUTI
site 03E28   ; OUTI
site 03E2A   ; OUTI
site 03E2C   ; OUTI
site 03E2E   ; OUTI
site 03E30   ; OUTI
site 03E32   ; OUTI
site 03E34   ; OUTI
site 03E36   ; OUTI
site 03E38   ; OUTI
site 03E3A   ; OUTI
site 03E3C   ; OUTI
site 03E3E   ; OUTI
site 03E40   ; OUTI
site 03E42   ; OUTI
site 03E44   ; OUTI
site 03E46   ; OUTI
site 03E48   ; OUTI
site 03E4A   ; OUTI
site 03E4C   ; OUTI
site 03E4E   ; OUTI
site 03E50   ; OUTI
site 03E52   ; OUTI
site 03E54   ; OUTI
site 03E56   ; OUTI
site 03E58   ; OUTI
site 03E5A   ; OUTI
site 03E5C   ; OUTI
site 03E5E   ; OUTI
site 03E60   ; OUTI
site 03E62   ; OUTI
site 03E64   ; OUTI
site 03E66   ; OUTI
site 03E68   ; OUTI
site 03E6A   ; OUTI
site 03E6C   ; OUTI
site 03E6E   ; OUTI
site 03E70   ; OUTI
site 03E72   ; OUTI
site 03E74   ; OUTI
site 03E76   ; OUTI
site 03E78   ; OUTI
site 03E7A   ; OUTI
site 03E7C   ; OUTI
site 03E7E   ; OUTI
site 03E80   ; OUTI
site 03E82   ; OUTI
site 03E84   ; OUTI
site 03E86   ; OUTI
site 03E88   ; OUTI
site 03E8A   ; OUTI
site 03E8C   ; OUTI
site 03E8E   ; OUTI
site 03E90   ; OUTI
site 03E92   ; OUTI
site 03E94   ; OUTI
site 03E96   ; OUTI
site 03E98   ; OUTI
site 03E9A   ; OUTI
site 03E9C   ; OUTI
site 03E9E   ; OUTI
site 03EA0   ; OUTI
site 03EA2   ; OUTI
site 03EA4   ; OUTI
site 03EA6   ; OUTI
site 03EA8   ; OUTI
site 03EAA   ; OUTI
site 03EAC   ; OUTI
site 03EAE   ; OUTI
site 03EB0   ; OUTI
site 03EB2   ; OUTI
site 03EB4   ; OUTI
site 0402D   ; OUT ($BE),A
site 04037   ; OUT ($BE),A
site 04071   ; OUTI
site 04075   ; OUT ($BE),A
site 040B8   ; OUT ($BE),A
site 040BD   ; OUT ($BE),A
site 040C2   ; OUT ($BE),A
site 040C7   ; OUT ($BE),A
site 040CD   ; OUT ($BE),A
site 040D2   ; OUT ($BE),A
site 040FA   ; OUT ($BE),A
site 040FF   ; OUT ($BE),A
site 04105   ; OUT ($BE),A
site 0410A   ; OUT ($BE),A
site 04155   ; OUT ($BE),A
site 0415A   ; OUT ($BE),A
otir 041C6   ; OUTI
otir 0426D   ; OUTI
otir 04302   ; OUTI
otir 04348   ; OUTI
site 056BE   ; OUTI
site 056C5   ; OUTI
site 05713   ; OUT ($7F),A
site 0577D   ; OUT ($F0),A
site 05783   ; OUT ($F1),A
site 0583D   ; OUT ($F0),A
site 05844   ; OUT ($F1),A
site 058A0   ; OUT ($F0),A
site 058A6   ; OUT ($F1),A
site 05BFA   ; OUT ($7F),A
site 05BFE   ; OUT ($7F),A
site 05C07   ; OUT ($7F),A
site 05C7D   ; OUT ($7F),A
site 05CA2   ; OTIR
site 05CB0   ; OUT (C),D
site 05CB6   ; OUT ($F1),A
site 05CC1   ; OUT ($7F),A
site 05CC5   ; OUT ($7F),A
site 05D86   ; OUT ($F0),A
site 05D8D   ; OUT ($F1),A
site 05D95   ; OUT ($F0),A
site 05D9D   ; OUT ($F1),A
site 05DA7   ; OUT ($F0),A
site 05DB2   ; OUT ($F1),A
# not a site: 07DD6 (overlapping decode in bank 1 data)
# not a site: 07DF2 (overlapping decode in bank 1 data)
mapldk 00084   # loads HL with $FFFC, then stores $80 through it
maphl 0008A   # LD (HL),$00, HL = $FFFD
maphl 0008D   # LD (HL),$01, HL = $FFFE
maphl 00090   # LD (HL),$02, HL = $FFFF
mapst 001BA   ; LD ($FFFF),A
mapld 0099B   # loads HL with $FFFF, then stores $0A through it
mapst 00A5A   ; LD ($FFFF),A
mapld 01195   # loads HL with $FFFF, then stores $0A through it
mapld 01282   # loads HL with $FFFF, then stores $0A through it
mapst 012C1   ; LD ($FFFF),A
mapld 012D7   # loads HL with $FFFF, then stores $07 through it
mapld 01431   # loads HL with $FFFF, then stores $0A through it
mapld 01493   # loads HL with $FFFF, then stores $0A through it
mapld 0157D   # loads HL with $FFFF, then stores $02 through it
mapld 0158E   # loads HL with $FFFF, then stores $0B through it
mapld 0159C   # loads HL with $FFFF, then stores $08 through it
mapld 015BC   # loads HL with $FFFF, then stores $09 through it
mapld 0188D   # loads HL with $FFFF, then stores $05 through it
mapld 01F52   # loads HL with $FFFF, then stores $0F through it
mapld 01FA0   # loads HL with $FFFF, then stores $0F through it
mapld 01FF8   # loads HL with $FFFF, then stores $0F through it
mapld 02270   # loads HL with $FFFF, then stores $0F through it
mapld 023A1   # loads HL with $FFFF, then stores $0F through it
mapld 02AA2   # loads HL with $FFFF, then stores $03 through it
mapld 02F6B   # loads HL with $FFFF, then stores $09 through it
mapld 03909   # loads HL with $FFFF, then stores $02 through it
mapld 03A2C   # loads HL with $FFFF, then stores $03 through it
mapld 03ACA   # loads HL with $FFFF, then stores $03 through it
mapld 03CCA   # loads HL with $FFFF, then stores $02 through it
mapld 03CE3   # loads HL with $FFFF, then stores $02 through it
mapld 03D34   # loads HL with $FFFF, then stores $02 through it
mapld 03D6A   # loads HL with $FFFF, then stores $02 through it
mapld 03EBE   # loads HL with $FFFF, then stores $02 through it
mapld 04039   # loads HL with $FFFF, then stores $09 through it
mapld 0416D   # loads HL with $FFFF, then stores $02 through it
mapld 0419D   # loads HL with $FFFF, then stores $0E through it
mapld 04240   # loads HL with $FFFF, then stores $09 through it
mapld 04287   # loads HL with $FFFF, then stores $08 through it
mapld 042DD   # loads HL with $FFFF, then stores $0C through it
mapld 04323   # loads HL with $FFFF, then stores $0C through it
mapld 04574   # loads HL with $FFFF, then stores $06 through it
mapld 047C7   # loads HL with $FFFF, then stores $03 through it
mapld 04BD4   # loads HL with $FFFF, then stores $04 through it
mapld 04E0E   # loads HL with $FFFF, then stores $0B through it
mapld 04E53   # loads HL with $FFFF, then stores $0B through it
mapld 04E98   # loads HL with $FFFF, then stores $0B through it
mapld 04EFD   # loads HL with $FFFF, then stores $0B through it
mapld 04F3F   # loads HL with $FFFF, then stores $03 through it
mapld 04FB6   # loads HL with $FFFF, then stores $05 through it
mapld 04FE6   # loads HL with $FFFF, then stores $05 through it
mapld 05104   # loads HL with $FFFF, then stores $05 through it
# CHECK cartarea_store at 014F8 ($14F8 bank 0): LD (BC),A $0502
# CHECK cartarea_store at 01507 ($1507 bank 0): LD (BC),A $52FF
# CHECK cartarea_store at 0150B ($150B bank 0): LD (BC),A $52FF
# CHECK cartarea_store at 05E4C ($5E4C bank 1): LD (BC),A $0209,$07F3,$5F54,$5F5D...
# CHECK cartarea_store at 05E73 ($5E73 bank 1): LD (BC),A $5F7D
# CHECK cartarea_store at 05E7C ($5E7C bank 1): LD (BC),A $5F7D
# CHECK cartarea_store at 05EBC ($5EBC bank 1): LD (BC),A $5FBE
# CHECK cartarea_store at 05F05 ($5F05 bank 1): LD (BC),A $000B
# CHECK cartarea_store at 05F0A ($5F0A bank 1): LD (BC),A $000B
# CHECK cartarea_store at 05F0F ($5F0F bank 1): LD (BC),A $000B
# CHECK cartarea_store at 05F14 ($5F14 bank 1): LD (BC),A $000B
# CHECK cartarea_store at 05F34 ($5F34 bank 1): LD (BC),A $5F30
# CHECK cartarea_store at 05F37 ($5F37 bank 1): LD (BC),A $5F31
# CHECK cartarea_store at 05F40 ($5F40 bank 1): LD (BC),A $0209,$07F3,$5F54,$5F5D...
# CHECK cartarea_store at 05F56 ($5F56 bank 1): LD (BC),A $5F5E
# CHECK cartarea_store at 05F58 ($5F58 bank 1): LD (BC),A $5F5E
# CHECK cartarea_store at 05F76 ($5F76 bank 1): LD (BC),A $5F85
# CHECK cartarea_store at 05FCE ($5FCE bank 1): LD (BC),A $5FE2
# CHECK cartarea_store at 05FD7 ($5FD7 bank 1): LD (BC),A $5FF8
# CHECK cartarea_store at 05FE1 ($5FE1 bank 1): LD (BC),A $600E
# CHECK cartarea_store at 05FEB ($5FEB bank 1): LD (BC),A $0A70
# CHECK cartarea_store at 06028 ($6028 bank 1): LD (BC),A $0640
# CHECK cartarea_store at 0605E ($605E bank 1): LD (BC),A $0208,$0209,$5F54,$5F5D...
# CHECK cartarea_store at 06071 ($6071 bank 1): LD (BC),A $0230
# CHECK cartarea_store at 06083 ($6083 bank 1): LD (BC),A $6085
# CHECK cartarea_store at 06671 ($6671 bank 1): LD (BC),A $1180
# CHECK cartarea_store at 06679 ($6679 bank 1): LD (DE),A $0120,$9C02
# CHECK cartarea_store at 0667A ($667A bank 1): LD (BC),A $1181
# CHECK cartarea_store at 06683 ($6683 bank 1): LD (BC),A $2082
# CHECK cartarea_store at 0668D ($668D bank 1): LD (BC),A $2183
# CHECK cartarea_store at 06693 ($6693 bank 1): LD (BC),A $2183
# CHECK cartarea_store at 06696 ($6696 bank 1): LD (BC),A $2083,$2183
# CHECK cartarea_store at 0669F ($669F bank 1): LD (BC),A $2183,$2283
# CHECK cartarea_store at 066A8 ($66A8 bank 1): LD (BC),A $2083
# CHECK cartarea_store at 066D0 ($66D0 bank 1): LD (BC),A $0985
# CHECK cartarea_store at 06F7E ($6F7E bank 1): LD ($30A0),A $30A0
# CHECK cartarea_store at 07045 ($7045 bank 1): LD (BC),A $030A,$08F4,$6055,$605E...
# CHECK cartarea_store at 0704E ($704E bank 1): LD (BC),A $030A,$08F4,$605E,$6087
# CHECK cartarea_store at 07050 ($7050 bank 1): LD (DE),A $9F02
# CHECK cartarea_store at 07051 ($7051 bank 1): LD (BC),A $030A,$08F4,$605E,$6087
# CHECK cartarea_store at 0705A ($705A bank 1): LD (BC),A $030B,$08F5,$605F,$6088
# CHECK cartarea_store at 07064 ($7064 bank 1): LD (BC),A $0488,$04F5
# CHECK cartarea_store at 0706D ($706D bank 1): LD (BC),A $0105
# CHECK cartarea_store at 07076 ($7076 bank 1): LD (BC),A $0206
# CHECK cartarea_store at 0707F ($707F bank 1): LD (BC),A $0006
# CHECK cartarea_store at 07B4F ($7B4F bank 1): LD (BC),A $0260
# CHECK cartarea_store at 07B51 ($7B51 bank 1): LD (DE),A $B802
# CHECK cartarea_store at 07B52 ($7B52 bank 1): LD (BC),A $0260
# CHECK cartarea_store at 07B5B ($7B5B bank 1): LD (BC),A $0261
# CHECK cartarea_store at 07B65 ($7B65 bank 1): LD (BC),A $0362
# CHECK cartarea_store at 07B6E ($7B6E bank 1): LD (BC),A $0205
# CHECK cartarea_store at 07B77 ($7B77 bank 1): LD (BC),A $0305
# CHECK cartarea_store at 07B80 ($7B80 bank 1): LD (BC),A $0105
# CHECK cartarea_store at 07DDB ($7DDB bank 1): LD (BC),A $0231,$06F5,$07F5,$5E88...
# CHECK cartarea_store at 07DDD ($7DDD bank 1): LD (DE),A $0120
# CHECK cartarea_store at 07DE4 ($7DE4 bank 1): LD (BC),A $0331,$07F5,$08F5,$5F88...
# CHECK cartarea_store at 07E0D ($7E0D bank 1): LD (DE),A $0120
# CHECK cartarea_store at 07E45 ($7E45 bank 1): LD (DE),A $0120
# CHECK ram_exec at 00029 ($0029 bank 0): JR $FFFB $FFFB
# CHECK ram_exec at 05E26 ($5E26 bank 1): JP Z,$E509 $E509
# CHECK ram_exec at 05E3E ($5E3E bank 1): JP Z,$E50B $E50B
# CHECK ram_exec at 05EBE ($5EBE bank 1): CALL NZ,$FE5E $FE5E
# CHECK ram_exec at 05EC2 ($5EC2 bank 1): JP P,$F580 $F580
# CHECK ram_exec at 0600B ($600B bank 1): JP P,$F301 $F301
# CHECK ram_exec at 06094 ($6094 bank 1): CALL Z,$DD60 $DD60
# CHECK ram_exec at 0609A ($609A bank 1): CALL PE,$F160 $F160
# CHECK ram_exec at 0704B ($704B bank 1): CALL P,$E000 $E000
# CHECK indirect_unresolved at 001B4 ($01B4 bank 0): JP (HL) 
# CHECK indirect_unresolved at 017D4 ($17D4 bank 0): JP (HL) 
# CHECK indirect_unresolved at 05E75 ($5E75 bank 1): RET NZ 
# CHECK indirect_unresolved at 05ECF ($5ECF bank 1): RET Z 
# CHECK indirect_unresolved at 05ED3 ($5ED3 bank 1): RET PO 
# CHECK indirect_unresolved at 05F48 ($5F48 bank 1): RET P 
# CHECK indirect_unresolved at 05F51 ($5F51 bank 1): RET P 
# CHECK indirect_unresolved at 05F70 ($5F70 bank 1): RET PO 
# CHECK indirect_unresolved at 05F79 ($5F79 bank 1): RET NZ 
# CHECK indirect_unresolved at 05F80 ($5F80 bank 1): RET P 
# CHECK indirect_unresolved at 05F89 ($5F89 bank 1): RET PO 
# CHECK indirect_unresolved at 05F9A ($5F9A bank 1): RET NC 
# CHECK indirect_unresolved at 05FA3 ($5FA3 bank 1): RET P 
# CHECK indirect_unresolved at 05FD9 ($5FD9 bank 1): RET PO 
# CHECK indirect_unresolved at 06027 ($6027 bank 1): RET PO 
# CHECK indirect_unresolved at 0607C ($607C bank 1): RET NZ 
# CHECK indirect_unresolved at 07067 ($7067 bank 1): RET M 
# CHECK indirect_unresolved at 07070 ($7070 bank 1): RET M 
# CHECK indirect_unresolved at 07075 ($7075 bank 1): RET NZ 
# CHECK indirect_unresolved at 07079 ($7079 bank 1): RET M 
# CHECK indirect_unresolved at 0707E ($707E bank 1): RET PO 
# CHECK indirect_unresolved at 0708D ($708D bank 1): RET M 
# CHECK indirect_unresolved at 07090 ($7090 bank 1): RET M 
# CHECK bank_unresolved at 05F64 ($5F64 bank 1): JP P,$A802 $A802
# CHECK bank_unresolved at 05FC4 ($5FC4 bank 1): JP P,$A803 $A803
# CHECK bank_unresolved at 06086 ($6086 bank 1): JP P,$A280 $A280
# CHECK low: site 002C6  OUT ($BF),A  (vdp_control)
# CHECK low: site 002CA  OUT ($BF),A  (vdp_control)
# CHECK low: site 00A3E  OUT ($BE),A  (vdp_data)
# CHECK low: site 01E51  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B080  IN L,(C)  (port in C)
# CHECK low: site 1B25C  IN A,($BF)  (vdp_status)
# CHECK low: site 1B4EF  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 1B819  IN A,($3F)  (unmapped_read)
# CHECK low: site 1E6B0  IN A,($DC)  (joypad_a)
# CHECK low: site 1FCDB  OUTD  (port in C)
# CHECK low: site 21648  IN A,($BF)  (vdp_status)
# CHECK low: site 2187C  IN A,($7F)  (h_counter)
# CHECK low: site 2193D  IN C,(C)  (port in C)
# CHECK low: site 21B94  IN C,(C)  (port in C)
# CHECK low: site 2297D  IN A,($7F)  (h_counter)
# CHECK low: site 25E44  OUT ($C0),A  (no_effect)
# CHECK low: site 2E3C7  IN A,($7E)  (v_counter)
# CHECK low: site 2E42F  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 2E53C  IN A,($7E)  (v_counter)
# CHECK low: site 2E584  IN A,($3F)  (unmapped_read)
# CHECK low: site 2E5A2  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 32567  IN A,($BF)  (vdp_status)
# CHECK low: site 36997  IN A,($BD)  (vdp_status)
# CHECK low: site 3699F  IN A,($BD)  (vdp_status)
# CHECK low: site 38947  OUT ($F0),A  (fm_address)
# CHECK low: site 39AD1  OUT ($BF),A  (vdp_control)
# CHECK low: site 3A3E1  IN A,($BF)  (vdp_status)
# CHECK low: site 3A798  IN A,($7F)  (h_counter)
# CHECK low: site 3BD25  IN H,(C)  (port in C)
# CHECK low: site 3C7AC  IN D,(C)  (port in C)
# The line interrupt handler at $DE80 is copied from ROM $07F0-$0801; its
# I/O (sites 007F0, 007F9, 007FD above) is patched in the ROM source. With
# the raster hook its interrupts are not delivered.
plain 007F0
plain 007F9
plain 007FD
rastercode outrun-raster.asm
# Mapper stores the draft missed: LD (HL),n with HL set to $FFFF, in banks 0-1, found
# by sitescan's byte scan, in routines that load graphics.
# "ran in the reference run": the SMS reference MAME saw it write the mapper.
# Byte scan hits left out: they decode as data (RST and NOP runs, no valid
# code after them, or no code leading to them).
mapld 01940   # ran in the reference run
mapld 01951   # ran in the reference run
mapld 01B92   # ran in the reference run
mapld 01E54   ; loads HL with $FFFF, then stores $09 through it
mapld 01E62   ; loads HL with $FFFF, then stores $0F through it
mapld 01E8A   ; loads HL with $FFFF, then stores $0D through it
mapld 04393   ; loads HL with $FFFF, then stores $0C through it
# not patched (data): mapst 302AF  LD ($FFFE),A  (no evidence)
