# OutRun, drafted by tools/mkspec.py from sitescan output.
name OutRun
cart 5589D8D2
hz any		; No-Intro regions World
# tilecache: whole tiles copied from cart ROM are not converted again (MAME,
# game frames 300-2300: framework cycles -1.4%, vertical blank tile work -8%)
tilecache
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
# Frame-interrupt handler, entry 14 of the table at $01D0 (the interrupt code at $01B4 reads it
# with the byte offset $1C that $1E15 passes to $0056, the game mode $13 routine). It sets the
# horizontal scroll (VDP register 8) to 0.
site 002C6   ; OUT ($BF),A
site 002CA   ; OUT ($BF),A
site 002EC   ; OUT ($BF),A
site 002F0   ; OUT ($BF),A
site 00346   ; OUT ($BF),A
site 0034A   ; OUT ($BF),A
site 0034F   ; OUT ($BF),A
site 00353   ; OUT ($BF),A
site 00363   ; OUT ($BF),A
site 00367   ; OUT ($BF),A
site 0036F   ; OUT ($BF),A
site 00373   ; OUT ($BF),A
site 00378   ; OUT ($BF),A
site 0037C   ; OUT ($BF),A
site 003A2   ; OUT ($BF),A
site 003A6   ; OUT ($BF),A
site 003B5   ; OUT ($BF),A
site 003B9   ; OUT ($BF),A
site 003BE   ; OUT ($BF),A
site 003C2   ; OUT ($BF),A
site 003DA   ; OUT ($BF),A
site 003DE   ; OUT ($BF),A
site 003F0   ; OUT ($BF),A
site 003F4   ; OUT ($BF),A
site 003F9   ; OUT ($BF),A
site 003FD   ; OUT ($BF),A
site 00424   ; OUT ($BF),A
site 00428   ; OUT ($BF),A
site 00440   ; OUT ($BF),A
site 00450   ; OUT ($BF),A
site 00454   ; OUT ($BF),A
site 00465   ; OUT ($BF),A
site 00469   ; OUT ($BF),A
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
site 00A3E   ; OUT ($BE),A
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
# Code page 0. In the race the frame handler works through a cycle of five
# tasks. Task 9 ($044A) writes name table rows 8-27, $3A00-$3EFF, from the
# buffer at $D500: seven calls into the unrolled OUTI block at $3DB6 (896
# bytes), then two OUTI loops, the first of 128 bytes and the second, which
# starts with B = 0, of 256: 1,280 bytes. Through the I/O trap that takes
# most of a frame, so the handler runs past the next frame event. nt_up9
# writes the same 1,280 bytes with two jt_vwrite calls, columns 0-7 and then
# columns 8-31 of each row, with interrupts off across both, so the game's
# interrupt handler never sees a half-written region. The other way into the
# same writes, $0434 (when ($C24E) is not 0), writes rows 15-27 from $D6C0
# at $3BC0: nt_up9b.
# sat_up replaces the sprite table writer at $3DA3 (64 Y bytes from $C600 to
# $3F00, then 128 X and tile bytes from $C680 to $3F80, through the OUTI
# block) with two OTIR calls.
# The entries leave the registers, the VDP address and code as the game's
# code does (HL, B, C and A as after the last OUTI, F only with Z from B),
# and keep interrupts as they were.
asm 00471 7   ; task 9: name table rows from $D500 -> page 0, then the code after the writes
    rst $00
    db far_io, pg_nt_up9, ent_nt_up9
    jp $049E
endasm
asm 00437 7   ; task 9 with ($C24E) not 0: rows from $D6C0 at $3BC0 -> page 0
    rst $00
    db far_io, pg_nt_up9b, ent_nt_up9b
    jp $049E
endasm
asm 03DA3 5   ; sprite table writer -> page 0, then return
    rst $00
    db far_io, pg_sat_up, ent_sat_up
    ret
endasm
# Four of the race tasks end with a wait for the next picture: IN A,($7E),
# CP $B7, JP NC back, with interrupts off. Through the framework that loop
# runs the vblank work once in the vertical blank, then again when it reads
# a picture line: the framework's frame interrupt, held since line 248 by
# the game's DI, comes at the EI after the loop and finds the work not done.
# vwait waits for the same line by reading the Next's line number itself. It
# reads the V counter through the framework once, when the line is in the
# vertical blank, so that the vblank work is done there, and never sees a
# picture line through the framework. It changes only A and F, as the loop
# does, and the game sets A after it.
asm 0035B 7   ; task 0: wait for the picture -> page 0
    rst $00
    db far_io, pg_vwait, ent_vwait
    nop
    nop
    nop
endasm
asm 0039A 7   ; task 6: wait for the picture -> page 0
    rst $00
    db far_io, pg_vwait, ent_vwait
    nop
    nop
    nop
endasm
asm 003D2 7   ; task 7: wait for the picture -> page 0
    rst $00
    db far_io, pg_vwait, ent_vwait
    nop
    nop
    nop
endasm
asm 0041C 7   ; task 8: wait for the picture -> page 0
    rst $00
    db far_io, pg_vwait, ent_vwait
    nop
    nop
    nop
endasm
# $0A52 (which tasks 0, 7 and 8 call) unpacks up to 128 bytes of run-length
# coded tile data a call, from ($C144) to VRAM 4 bytes apart from ($C146)
# (one bit plane): runs of literal or repeated bytes, each byte through
# RST $08 (the address from DE) and OUT ($BE),A. Most runs are 2 to 4
# bytes, so a far call for each run costs more than its writes. rle runs
# the routine from $0A64 to its RET as the game's code, but collects the
# bytes, which go to consecutive addresses 4 apart, and writes them with one
# jt_vwrite call (runs of one byte, VRAM step 4) before the routine leaves
# the unpacking loop. With a DE that is not a VRAM write command, or whose
# command would change on the way, it writes them through the ports as the
# game does. It runs with interrupts off and reads the source as the game
# sees it.
asm 00A64 5   ; $0A52 from LD C,0 to its RET -> page 0
    rst $00
    db far_io, pg_rle, ent_rle
    ret
endasm
site 00A98   ; OUT ($BE),A (no longer reached: rle replaces its loop)
page 0 nt_up9 nt_up9b sat_up vwait rle
; Both ways in end at name table address $3F00 and source $DA00.
nt_up9: ld (n_gde),de            ; the game's DE, kept
        ld hl,$D500
        ld de,$3A00
        ld c,20                 ; rows
        ld a,$7A                ; A as the game's code leaves it
        jr ntw
nt_up9b:
        ld (n_gde),de
        ld hl,$D6C0
        ld de,$3BC0
        ld c,13
        ld a,$7B
; HL = source, DE = name table address of column 0, C = rows, A = A on return
ntw:    ld (n_a),a
        ld a,i                  ; P/V = IFF
        di
        push af
        push ix
        push iy
        ld ix,64
        ld iy,64
        ld b,16                 ; columns 0-7 of each row
        xor a
        call jt_vwrite
        ld a,l                  ; HL += 16 (no carry: a row starts at $xx00, $xx40, $xx80 or $xxC0)
        add a,16
        ld l,a
        ld a,e
        add a,16
        ld e,a
        ld b,48                 ; columns 8-31: the VDP address ends at $3F00
        xor a
        call jt_vwrite
        pop iy
        pop ix
        pop af
        jp po,.di
        ei
.di:    ld de,(n_gde)
        ld hl,$DA00
        ld bc,$00BE
        xor a                   ; Z, as after the last OUTI
        ld a,(n_a)
        ret
sat_up: ld a,b                  ; B as after 192 OUTIs
        add a,64
        ld (s_b),a
        ld a,i
        di
        push af
        ld hl,$3F00
        ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld hl,$C600
        ld bc,$40BE
        rst $00
        db $B3
        ld hl,$3F80
        ld (vdp_addr),hl
        ld hl,$C680
        ld bc,$80BE
        rst $00
        db $B3
        pop af
        jp po,.d
        ei
.d:     ld hl,$C700
        ld de,$7F80
        ld a,(s_b)
        ld b,a
        or a                    ; Z from B
        ld a,$7F
        ld c,$BE
        ret
; vwait: until the Next line is a picture line below 183 (V below $B7)
vwait:  push bc
        push de
        ld e,0                  ; 1: the framework has read V this time
.l:     ld bc,$243B
        ld a,$1E
        out (c),a
        inc b
        in d,(c)                ; line, bit 8
        dec b
        ld a,$1F
        out (c),a
        inc b
        in a,(c)                ; line, bits 0-7
        bit 0,d
        jr nz,.vb
        cp 183
        jr c,.done
        cp 194                  ; the framework's vertical blank starts at 194
        jr c,.l
.vb:    ld a,e
        or a
        jr nz,.l
        inc e
        rst $00
        db $0A                  ; IN A,($7E) through the framework
        jr .l
.done:  pop de
        pop bc
        ret
;
;
; rle: $0A64-$0B16 as the game's code, with the VRAM writes collected in
; r_buf and written by flush. While it unpacks, DE points into r_buf; the
; game's DE is r_de + 4 * the bytes collected, worked out (vde) where the
; code leaves the loop. Z through the loop at $0A96 says whether the run
; repeats one byte, so the loop is in two copies, one for each; F is not
; read after either copy before code that sets it. rd reads (HL) as the
; game sees it; the count byte that $0A73, $0A85 and $0A8F read is read once.
rle:    ld a,i                  ; P/V = IFF (B and C are not live here)
        push af
        pop bc
        ld a,c
        ld (r_iff),a
        di
        ld (r_de),de            ; the VRAM address of the first byte
        ld de,r_buf
        ld c,0                  ; $0A64
        ld a,($C124)
        or a
        jp nz,.ab2
.a6d:   ld a,c
        cp $80
        jp nc,.ae5
        call rd
        ld (r_cb),a
        or a
        jp z,.aed
        and $7F
        ld b,a
        add a,c
        cp $81
        jp c,.a8e
        ld a,$80
        sub c
        ld b,a
        ld a,(r_cb)
        and $7F
        sub b
        ld ($C124),a
        ld a,$80
.a8e:   ld c,a
        ld a,(r_cb)
        inc hl
        and $80
        ld ($C123),a            ; Z: one byte repeated
.a96:   jr z,.rep
        inc b                   ; literal: RST $08, LD A,(HL), OUT ($BE),A, INC HL
        dec b
        jr z,.b0l               ; B = 0: 256 bytes
        ld a,h
        cp $40
        jr nc,.lf               ; the source is above $3FFF
        and $E0
        cp $20
        jr z,.lsl               ; the source starts in $2000-$3FFF
        ld a,b
        dec a
        add a,l
        ld a,h
        adc a,0
        and $E0
        cp $20
        jr z,.lsl               ; or ends there
.lf:    ld a,c
        ld c,b
        ld b,0
        ldir
        ld c,a
        jp .a6d                 ; Z clear: back to $0A6D
.lsl:   call rd
        ld (de),a
        inc e
        inc hl
        djnz .lsl
        jp .a6d
.rep:   inc b                   ; the same byte B times
        dec b
        jr z,.b0r
        call rd
.rl:    ld (de),a
        inc e
        djnz .rl
.aa7:   ld a,($C124)            ; $0AA7: Z set
        or a
        jp nz,.a6d
        inc hl
        jp .a6d
; a run of 256 bytes (count byte $80: B = 0, and C does not grow) goes
; through the ports as the game's code does, after the bytes before it
.b0l:   call vde
        call flush
.sl:    call sbyte
        inc hl
        inc de
        inc de
        inc de
        inc de
        djnz .sl
        ld (r_de),de
        ld de,r_buf
        jp .a6d
.b0r:   call vde
        call flush
.sr:    call sbyte
        inc de
        inc de
        inc de
        inc de
        djnz .sr
        ld (r_de),de
        ld de,r_buf
        jp .aa7
.ab2:   cp $80
        jp c,.ac2
        sub $80
        ld ($C124),a
        ld b,$80
        ld c,b
        jp .ac8
.ac2:   ld b,a
        ld c,a
        xor a
        ld ($C124),a
.ac8:   ld a,($C123)
        or a
        jp .a96
.acf:   ld hl,($C128)
        ld ($C144),hl
        ld hl,($C126)
        ld ($C146),hl
        ld a,$04
        ld ($C122),a
        xor a
        ld ($C124),a
        jp .ret
.ae5:   call vde
        call flush
        ld ($C144),hl
        ld ($C146),de
        jp .ret
.aed:   call vde
        call flush
        inc hl
        ld ($C144),hl
        ld hl,($C126)
        inc hl
        ld ($C126),hl
        ld ($C146),hl
        ld a,($C122)
        dec a
        ld ($C122),a
        jp nz,.ret
        ld hl,$C12A
        ld de,$C125
        ld bc,$001A
        ldir
        ld a,($C125)
        cp $FF
        jp nz,.acf
.ret:   push af                 ; interrupts as they were; A and F kept
        ld a,(r_iff)
        bit 2,a
        jr z,.di
        pop af
        ei
        ret
.di:    pop af
        ret
; E = the bytes in r_buf: r_ptr = E, DE = r_de + 4 * E (the game's DE); F kept
vde:    push hl
        push af
        ld a,e
        ld (r_ptr),a
        ld l,e
        ld h,0
        add hl,hl
        add hl,hl
        ld de,(r_de)
        add hl,de
        ex de,hl
        pop af
        pop hl
        ret
; A = (HL) as the game sees it; F changes
rd:     ld a,h
        and $E0
        cp $20
        jp z,jt_peek            ; the game's page under this one
        ld a,(hl)
        ret
; RST $08, LD A,(HL), OUT ($BE),A through the framework; F kept
sbyte:  push af
        ld a,e
        rst $00
        db $05                  ; OUT ($BF),A
        ld a,d
        rst $00
        db $05
        call rd
        rst $00
        db $04                  ; OUT ($BE),A
        pop af
        ret
; the r_ptr bytes in r_buf to VRAM at r_de, r_de + 4, ...; keeps every
; register and F
flush:  push af
        ld a,(r_ptr)            ; bytes, 0-128
        or a
        jr z,.f0
        push bc
        push de
        push hl
        push ix
        push iy
        ld b,a
        ld de,(r_de)
        ld l,b                  ; the last control word + 3 = DE + 4 * bytes - 1
        ld h,0
        add hl,hl
        add hl,hl
        dec hl
        add hl,de
        ld a,h
        xor d
        and $C0
        jr nz,.port             ; the command changes on the way
        ld a,d
        and $C0
        cp $40
        jr nz,.port             ; not a VRAM write command
        ld c,b                  ; runs = bytes
        ld b,1
        ld hl,r_buf
        ld ix,1
        ld iy,4
        ld a,1                  ; the source as mapped: r_buf in this page
        call jt_vwrite
        jr .fd
.port:  ld hl,r_buf
.pl:    ld a,e
        rst $00
        db $05                  ; OUT ($BF),A
        ld a,d
        rst $00
        db $05
        ld a,(hl)
        rst $00
        db $04                  ; OUT ($BE),A
        inc hl
        inc de
        inc de
        inc de
        inc de
        djnz .pl
.fd:    pop iy
        pop ix
        pop hl
        pop de
        pop bc
.f0:    pop af
        ret
r_iff:  db 0
r_ptr:  db 0
r_cb:   db 0
r_de:   dw 0
n_a:    db 0
s_b:    db 0
n_gde:  dw 0
        align 256
r_buf:  ds 256
endpage
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
# Game mode routine $1E29 (entry 19 of the 20-word mode table that the RST $10 call at $0154 reads; the
# mapper loads at $1E54, $1E62 and $1E8A in the same routine are patched above). It sets the VRAM address
# to $3F00 with RST $08 and writes $D0 there: the Y of the first sprite, which ends the sprite list.
site 01E51   ; OUT ($BE),A
