# Fantasy Zone II, B8B141F9, drafted by tools/mkspec.py from sitescan output (with the detector log).
name Fantasy Zone II
cart B8B141F9
hz any		; No-Intro regions USA, Europe, Brazil
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0000A   ; OUT ($BF),A
site 0000D   ; OUT ($BF),A
site 00029   ; OUT ($BF),A
site 0002C   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0007D   ; IN A,($BF)
site 0008C   ; OTIR
site 0008F   ; OUT ($BF),A
site 00093   ; OUT ($BF),A
site 00098   ; OUT ($BE),A
site 00212   ; OUT ($BE),A
site 00253   ; IN A,($DD)
site 0027D   ; OUT ($BF),A
site 00281   ; OUT ($BF),A
site 00286   ; OUT ($BF),A
site 0028A   ; OUT ($BF),A
site 0028F   ; OUT ($BF),A
site 00293   ; OUT ($BF),A
site 002E3   ; OUT ($3F),A
site 002E5   ; IN A,($DD)
site 002EF   ; OUT ($3F),A
site 002F1   ; IN A,($DD)
site 002FA   ; OUT ($3F),A
site 0032B   ; OUT ($BE),A
site 0032E   ; OUT ($BE),A
site 00440   ; OUT ($BE),A
site 004A1   ; OUT ($BF),A
site 004A5   ; OUT ($BF),A
site 004B4   ; OUT ($3E),A
site 004BC   ; OUT ($F2),A
site 004BF   ; IN A,($F2)
site 004D1   ; OUT ($F2),A
site 004D9   ; OUT ($3E),A
site 00507   ; OUT ($BF),A
site 0050B   ; OUT ($BF),A
site 0050F   ; OUT ($BF),A
site 00513   ; OUT ($BF),A
site 0051A   ; OUT ($BF),A
site 0051E   ; OUT ($BF),A
site 0052D   ; OUT ($BE),A
site 00532   ; OUT ($BE),A
site 00543   ; OUT ($BE),A
site 00564   ; OUT ($BE),A
site 0056F   ; OUT ($BE),A
site 0057A   ; OUT ($BE),A
site 0057F   ; IN A,($BE)
site 0058E   ; OUT ($BE),A
site 00594   ; OUT ($BE),A
site 005B5   ; IN A,($DC)
site 005E6   ; OUT ($BF),A
site 005EA   ; OUT ($BF),A
site 005EF   ; OUT ($BF),A
site 005F3   ; OUT ($BF),A
site 00791   ; OUT ($BE),A
site 007D2   ; OUT ($BE),A
site 00852   ; OUT ($BE),A
site 0085B   ; OUT ($BE),A
site 01010   ; IN A,($C1)
site 01BB0   ; IN A,($BE)
site 021EE   ; IN A,($BE)
site 021FA   ; OUT ($BE),A
site 022B0   ; OUT ($BE),A
site 022BB   ; OUT ($BE),A
site 024F1   ; OUT ($BE),A
site 024F5   ; IN A,($BE)
site 02508   ; OUT ($BE),A
site 025A4   ; OUT ($BE),A
site 025A8   ; IN A,($BE)
site 025BA   ; OUT ($BE),A
site 025C1   ; IN A,($BE)
site 025CB   ; OUT ($BE),A
site 025CF   ; IN A,($BE)
site 025D9   ; OUT ($BE),A
site 025DD   ; IN A,($BE)
site 025E3   ; OUT ($BE),A
site 025E9   ; OUT ($BE),A
site 02603   ; OUT ($BE),A
site 0262A   ; OUT ($BE),A
site 02645   ; OUT ($BE),A
site 0264C   ; IN A,($BE)
site 0448E   ; OUT ($BE),A
site 04494   ; OUT ($BE),A
site 046F7   ; IN A,($BE)
site 04700   ; OUT ($BE),A
site 04D09   ; OUT ($BE),A
site 04D17   ; OUT ($BE),A
site 04D1C   ; OUT ($BE),A
site 04DDD   ; IN A,($BE)
site 055C4   ; OUT ($BF),A
site 055C8   ; OUT ($BF),A
site 06546   ; OUT ($BE),A
site 06636   ; OUT ($BE),A
site 0663C   ; OUT ($BE),A
site 06642   ; OUT ($BE),A
site 06648   ; OUT ($BE),A
site 07204   ; OUT ($BF),A
site 07208   ; OUT ($BF),A
site 07E0C   ; OUT ($BE),A
site 07E12   ; OUT ($BE),A
site 07F8F   ; OUT ($BE),A
site 07F99   ; OUT ($BE),A
site 1C292   ; OUT ($F0),A
site 1C298   ; OUT ($F1),A
site 1C2DB   ; OUT ($7F),A
site 1C5A4   ; OUTI
site 1C5AB   ; OUTI
site 1C77E   ; OUT ($F0),A
site 1C784   ; OUT ($F1),A
site 1C865   ; OUT ($7F),A
site 1C873   ; OUT ($7F),A
site 1C87D   ; OUT ($7F),A
site 1CAE6   ; OUT ($7F),A
site 1CB96   ; OUT ($7F),A
site 1CC4C   ; OTIR
site 1CC5A   ; OUT (C),D
site 1CC60   ; OUT ($F1),A
site 1CC6C   ; OUT ($7F),A
site 1CC70   ; OUT ($7F),A
# not patched (data, read as code through a table): site 1F3BE
mapst 00030   ; LD ($FFFF),A
mapst 002C7   ; LD ($FFFF),A
# CHECK mapper at 00400 ($0400 bank 0): LDIR $8D02-$1248D $8D02-$1248D $8D02-$1248D $8D02-$1248D $FA9B-$19226 $FA9B-$19226 $FA9B-$19226 $FA9B-$19226 $FA9B-$19226 $FA9B-$19226 $FA9B-$19226 $FA9B-$19226 $8302-$12A83 $7002-$11570
# CHECK mapper at 00413 ($0413 bank 0): LD (HL),$80 $FFFC<-$80
# CHECK mapper at 00416 ($0416 bank 0): LD (HL),$00 $FFFD<-$00
# CHECK mapper at 00419 ($0419 bank 0): LD (HL),$01 $FFFE<-$01
# CHECK mapper at 0041C ($041C bank 0): LD (HL),$02 $FFFF<-$02
mapldk 00410   # loads HL with $FFFC, then stores $80 through it
maphl 00416   # LD (HL),$00, HL = $FFFD
maphl 00419   # LD (HL),$01, HL = $FFFE
maphl 0041C   # LD (HL),$02, HL = $FFFF
# CHECK cartarea_store at 00081 ($0081 bank 0): LD (BC),A $0202
# CHECK cartarea_store at 00677 ($0677 bank 0): LD (HL),A $46B4
# CHECK cartarea_store at 006BB ($06BB bank 0): INC (HL) $46B4
# CHECK cartarea_store at 006C0 ($06C0 bank 0): LD (HL),A $46B5
# CHECK cartarea_store at 006C7 ($06C7 bank 0): DEC (HL) $46B5
# CHECK cartarea_store at 006CC ($06CC bank 0): LD (HL),A $46B5
# CHECK cartarea_store at 006CE ($06CE bank 0): INC (HL) $46B4
# CHECK cartarea_store at 006D4 ($06D4 bank 0): LD (HL),$00 $46B4
# CHECK cartarea_store at 006D7 ($06D7 bank 0): LD (HL),$00 $46B3
# CHECK cartarea_store at 02084 ($2084 bank 0): LD (BC),A $0002,$0100
# CHECK cartarea_store at 02088 ($2088 bank 0): LD (BC),A $0002,$0100
# CHECK cartarea_store at 0208C ($208C bank 0): LD (BC),A $0002,$0100
# CHECK cartarea_store at 02106 ($2106 bank 0): LD (BC),A $0001
# CHECK cartarea_store at 02129 ($2129 bank 0): LD (HL),H $0202
# CHECK cartarea_store at 0240B ($240B bank 0): LD (DE),A $1102
# CHECK cartarea_store at 0248C ($248C bank 0): LD ($092D),A $092D
# CHECK cartarea_store at 1C038 ($8038 bank 7): LD (BC),A $8201
# CHECK cartarea_store at 1C03E ($803E bank 7): LD (BC),A $0101
# CHECK cartarea_store at 1C03F ($803F bank 7): LD (BC),A $0101
# CHECK cartarea_store at 1C059 ($8059 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C06F ($806F bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C070 ($8070 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C074 ($8074 bank 7): LD (BC),A $0201
# CHECK cartarea_store at 1C084 ($8084 bank 7): LD (BC),A $0800,$0801,$0803
# CHECK cartarea_store at 1C08C ($808C bank 7): LD (BC),A $0201
# CHECK cartarea_store at 1C090 ($8090 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C098 ($8098 bank 7): LD (BC),A $0101
# CHECK cartarea_store at 1C099 ($8099 bank 7): LD (BC),A $0101
# CHECK cartarea_store at 1C09A ($809A bank 7): LD (BC),A $0101
# CHECK cartarea_store at 1C0A7 ($80A7 bank 7): LD (BC),A $0603
# CHECK cartarea_store at 1C0C0 ($80C0 bank 7): DEC (HL) $2F81
# CHECK cartarea_store at 1C0CC ($80CC bank 7): LD (HL),H $0281
# CHECK cartarea_store at 1C0DD ($80DD bank 7): LD (BC),A $0201
# CHECK cartarea_store at 1C0EB ($80EB bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C0F3 ($80F3 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C0F4 ($80F4 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C0FE ($80FE bank 7): LD (BC),A $0403
# CHECK cartarea_store at 1C102 ($8102 bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C107 ($8107 bank 7): LD (BC),A $0201
# CHECK cartarea_store at 1C10B ($810B bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C111 ($8111 bank 7): LD (BC),A $0202
# CHECK cartarea_store at 1C128 ($8128 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C130 ($8130 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C138 ($8138 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C140 ($8140 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C148 ($8148 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C150 ($8150 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C158 ($8158 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C160 ($8160 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C168 ($8168 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C170 ($8170 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1CE1D ($8E1D bank 7): LD (DE),A $0073,$0202,$9002
# CHECK cartarea_store at 1CE1E ($8E1E bank 7): LD (BC),A $8003
# CHECK cartarea_store at 1CE27 ($8E27 bank 7): LD (BC),A $2004,$200B
# CHECK cartarea_store at 1CE30 ($8E30 bank 7): LD (BC),A $2104,$210B
# CHECK cartarea_store at 1CE43 ($8E43 bank 7): LD (BC),A $1F04,$1F0B
# CHECK cartarea_store at 1CE4C ($8E4C bank 7): LD (BC),A $0309
# CHECK cartarea_store at 1CE55 ($8E55 bank 7): LD (BC),A $0509
# CHECK cartarea_store at 1CE5E ($8E5E bank 7): LD (BC),A $0609
# CHECK cartarea_store at 1CE66 ($8E66 bank 7): LD (BC),A $0609
# CHECK cartarea_store at 1CE68 ($8E68 bank 7): LD (BC),A $0609
# CHECK cartarea_store at 1CE83 ($8E83 bank 7): LD (DE),A $91AE,$92AE,$93AE,$94AE...
# CHECK cartarea_store at 1CEA1 ($8EA1 bank 7): LD (DE),A $91AE
# CHECK cartarea_store at 1D16C ($916C bank 7): LD (BC),A $7F00,$7F03
# CHECK cartarea_store at 1D177 ($9177 bank 7): LD (DE),A $5A02
# CHECK cartarea_store at 1D178 ($9178 bank 7): LD (BC),A $7F01,$7F04
# CHECK cartarea_store at 1D17E ($917E bank 7): LD (BC),A $7F01,$7F04
# CHECK cartarea_store at 1D181 ($9181 bank 7): LD (BC),A $7F01,$7F04
# CHECK cartarea_store at 1D187 ($9187 bank 7): LD (BC),A $7F01,$7F04
# CHECK cartarea_store at 1D18A ($918A bank 7): LD (BC),A $7F01,$7F04
# CHECK cartarea_store at 1D199 ($9199 bank 7): LD (BC),A $7E03,$7E06
# CHECK cartarea_store at 1D19D ($919D bank 7): LD (BC),A $7F03,$7F06
# CHECK cartarea_store at 1D1A6 ($91A6 bank 7): LD (BC),A $0001
# CHECK cartarea_store at 1D1AF ($91AF bank 7): LD (BC),A $0100,$0101
# CHECK cartarea_store at 1D1B8 ($91B8 bank 7): LD (BC),A $0200,$0201
# CHECK cartarea_store at 1D3C0 ($93C0 bank 7): LD (BC),A $0104,$0204
# CHECK cartarea_store at 1D3CB ($93CB bank 7): LD (BC),A $0104
# CHECK cartarea_store at 1D3DB ($93DB bank 7): LD (BC),A $0104,$0204,$0304
# CHECK cartarea_store at 1D3ED ($93ED bank 7): LD (BC),A $0404
# CHECK cartarea_store at 1D403 ($9403 bank 7): LD (BC),A $A604
# CHECK cartarea_store at 1D41A ($941A bank 7): LD (BC),A $A305,$A306,$A307,$A308...
# CHECK cartarea_store at 1D446 ($9446 bank 7): LD (BC),A $A205,$A206,$A207,$A208...
# CHECK cartarea_store at 1D452 ($9452 bank 7): LD (BC),A $A405,$A406,$A407,$A408...
# CHECK cartarea_store at 1D458 ($9458 bank 7): LD (BC),A $A505,$A506,$A507,$A508...
# CHECK cartarea_store at 1D460 ($9460 bank 7): LD (BC),A $A605,$A606,$A607,$A608...
# CHECK cartarea_store at 1D467 ($9467 bank 7): LD (BC),A $A205,$A206,$A207,$A208...
# CHECK cartarea_store at 1D6B0 ($96B0 bank 7): LD (DE),A $8C01
# CHECK cartarea_store at 1D6F1 ($96F1 bank 7): LD (BC),A $995C
# CHECK cartarea_store at 1D6F7 ($96F7 bank 7): LD (BC),A $995C
# CHECK cartarea_store at 1D991 ($9991 bank 7): LD (DE),A $2F06
# CHECK cartarea_store at 1D9B3 ($99B3 bank 7): LD (BC),A $0D01,$0D04
# CHECK cartarea_store at 1D9D8 ($99D8 bank 7): LD (BC),A $0D0A
# CHECK cartarea_store at 1D9E4 ($99E4 bank 7): LD (BC),A $06FA
# CHECK cartarea_store at 1D9EF ($99EF bank 7): LD (BC),A $06FA
# CHECK cartarea_store at 1D9F6 ($99F6 bank 7): LD (BC),A $06FA
# CHECK cartarea_store at 1D9FA ($99FA bank 7): LD (BC),A $07FA
# CHECK cartarea_store at 1DA03 ($9A03 bank 7): LD (BC),A $07FA
# CHECK cartarea_store at 1DA07 ($9A07 bank 7): LD (BC),A $08FA
# CHECK cartarea_store at 1DA1D ($9A1D bank 7): LD (BC),A $80F5
# CHECK cartarea_store at 1DA26 ($9A26 bank 7): LD (BC),A $81F5
# CHECK cartarea_store at 1DA2A ($9A2A bank 7): LD (BC),A $82F5
# CHECK cartarea_store at 1DA2C ($9A2C bank 7): LD (BC),A $83F5
# CHECK cartarea_store at 1DA30 ($9A30 bank 7): LD (BC),A $84F5
# CHECK cartarea_store at 1DA3D ($9A3D bank 7): LD (BC),A $ABF5
# CHECK cartarea_store at 1DA5F ($9A5F bank 7): LD (BC),A $B0F1
# CHECK cartarea_store at 1DA65 ($9A65 bank 7): LD (BC),A $B1F1
# CHECK cartarea_store at 1DA69 ($9A69 bank 7): LD (BC),A $B2F1
# CHECK cartarea_store at 1DA6E ($9A6E bank 7): LD (BC),A $B3F1
# CHECK cartarea_store at 1DA73 ($9A73 bank 7): LD (BC),A $B4F1
# CHECK cartarea_store at 1DA7E ($9A7E bank 7): LD (BC),A $17B0
# CHECK cartarea_store at 1DA88 ($9A88 bank 7): LD (BC),A $17B0
# CHECK cartarea_store at 1DA8C ($9A8C bank 7): LD (BC),A $18B0
# CHECK cartarea_store at 1DA90 ($9A90 bank 7): LD (BC),A $19B0
# CHECK cartarea_store at 1DA9F ($9A9F bank 7): LD (BC),A $1AB0
# CHECK cartarea_store at 1DAAD ($9AAD bank 7): LD (BC),A $03AC
# CHECK cartarea_store at 1DABB ($9ABB bank 7): LD (BC),A $ACF0
# CHECK cartarea_store at 1DAC2 ($9AC2 bank 7): LD (BC),A $ADF0
# CHECK cartarea_store at 1DACF ($9ACF bank 7): LD (BC),A $17AB
# CHECK cartarea_store at 1DADF ($9ADF bank 7): LD (BC),A $9194
# CHECK cartarea_store at 1DAE4 ($9AE4 bank 7): LD (BC),A $9294
# CHECK cartarea_store at 1DAF3 ($9AF3 bank 7): LD (BC),A $17AC
# CHECK cartarea_store at 1DB00 ($9B00 bank 7): LD (BC),A $18AC,$9297
# CHECK cartarea_store at 1DB09 ($9B09 bank 7): LD (BC),A $ACAB
# CHECK cartarea_store at 1DB15 ($9B15 bank 7): LD (BC),A $ADAB
# CHECK cartarea_store at 1DB1A ($9B1A bank 7): LD (BC),A $AEAB
# CHECK cartarea_store at 1DB20 ($9B20 bank 7): LD (BC),A $AFAB
# CHECK cartarea_store at 1DB27 ($9B27 bank 7): LD (BC),A $B0AB
# CHECK cartarea_store at 1DB4A ($9B4A bank 7): LD (BC),A $0280,$9094
# CHECK cartarea_store at 1DB4D ($9B4D bank 7): LD (BC),A $0280,$9094
# CHECK cartarea_store at 1DB50 ($9B50 bank 7): LD (BC),A $0280,$9094
# CHECK cartarea_store at 1DB53 ($9B53 bank 7): LD (BC),A $0280,$9094
# CHECK cartarea_store at 1DB5F ($9B5F bank 7): LD (BC),A $0480,$0494
# CHECK cartarea_store at 1DB74 ($9B74 bank 7): LD (BC),A $9297
# CHECK cartarea_store at 1DB77 ($9B77 bank 7): LD (BC),A $9297
# CHECK cartarea_store at 1DB7A ($9B7A bank 7): LD (BC),A $9297
# CHECK cartarea_store at 1DB81 ($9B81 bank 7): LD (BC),A $9297
# CHECK cartarea_store at 1DB91 ($9B91 bank 7): LD (BC),A $9397
# CHECK cartarea_store at 1DB95 ($9B95 bank 7): LD (BC),A $9397
# CHECK cartarea_store at 1DBA6 ($9BA6 bank 7): LD (BC),A $9597
# CHECK cartarea_store at 1DBAC ($9BAC bank 7): LD (BC),A $9797
# CHECK cartarea_store at 1DBBC ($9BBC bank 7): LD (BC),A $9094
# CHECK cartarea_store at 1DBBF ($9BBF bank 7): LD (BC),A $9094
# CHECK cartarea_store at 1DBCD ($9BCD bank 7): LD (BC),A $8004
# CHECK cartarea_store at 1DC01 ($9C01 bank 7): LD (BC),A $0380
# CHECK cartarea_store at 1DC12 ($9C12 bank 7): LD (BC),A $0396
# CHECK cartarea_store at 1DC1D ($9C1D bank 7): LD (BC),A $0396
# CHECK cartarea_store at 1DC25 ($9C25 bank 7): LD (BC),A $A596
# CHECK cartarea_store at 1DD3E ($9D3E bank 7): LD (DE),A $2302
# CHECK cartarea_store at 1DD3F ($9D3F bank 7): LD (BC),A $7E01,$7E04
# CHECK cartarea_store at 1DD48 ($9D48 bank 7): LD (BC),A $7E02,$7E05
# CHECK cartarea_store at 1DD51 ($9D51 bank 7): LD (BC),A $5102,$5105
# CHECK cartarea_store at 1DD60 ($9D60 bank 7): LD (BC),A $5002,$5005
# CHECK cartarea_store at 1DD64 ($9D64 bank 7): LD (BC),A $5102,$5105
# CHECK cartarea_store at 1DD6D ($9D6D bank 7): LD (BC),A $0305
# CHECK cartarea_store at 1DD76 ($9D76 bank 7): LD (BC),A $0505
# CHECK cartarea_store at 1DD7F ($9D7F bank 7): LD (BC),A $0605
# CHECK cartarea_store at 1DD80 ($9D80 bank 7): LD ($009F),HL $009F,$00A0
# CHECK cartarea_store at 1DF41 ($9F41 bank 7): LD (DE),A $2301
# CHECK cartarea_store at 1DF63 ($9F63 bank 7): LD (BC),A $408B
# CHECK cartarea_store at 1DF9B ($9F9B bank 7): LD (DE),A $2401,$2402
# CHECK cartarea_store at 1E092 ($A092 bank 7): LD (BC),A $011E,$0120,$0122,$0124
# CHECK cartarea_store at 1E134 ($A134 bank 7): LD (BC),A $AC0A,$AC0F,$AC14,$AC1C
# CHECK cartarea_store at 1E137 ($A137 bank 7): LD (BC),A $AC0A,$AC0F,$AC14,$AC1C
# CHECK cartarea_store at 1E140 ($A140 bank 7): LD (BC),A $AE0A,$AE0F,$AE14,$AE1C
# CHECK cartarea_store at 1E143 ($A143 bank 7): LD (BC),A $AE0A,$AE0F,$AE14,$AE1C
# CHECK cartarea_store at 1E17A ($A17A bank 7): LD (DE),A $2004
# CHECK cartarea_store at 1E19C ($A19C bank 7): LD (BC),A $7F05,$7F0A,$7F0F
# CHECK cartarea_store at 1E1C1 ($A1C1 bank 7): LD (BC),A $0AB2
# CHECK cartarea_store at 1E1C3 ($A1C3 bank 7): LD (BC),A $0AB2
# CHECK cartarea_store at 1E1C5 ($A1C5 bank 7): LD (BC),A $0AB2
# CHECK cartarea_store at 1E1DB ($A1DB bank 7): LD (BC),A $A9A8
# CHECK cartarea_store at 1E1F0 ($A1F0 bank 7): LD (BC),A $06AE
# CHECK cartarea_store at 1E1F7 ($A1F7 bank 7): LD (BC),A $ABAE
# CHECK cartarea_store at 1E1FC ($A1FC bank 7): LD (BC),A $ABAE
# CHECK cartarea_store at 1E202 ($A202 bank 7): LD (BC),A $0A0B,$ADAE
# CHECK cartarea_store at 1E20F ($A20F bank 7): LD (BC),A $06B2
# CHECK cartarea_store at 1E231 ($A231 bank 7): LD (BC),A $08B2
# CHECK cartarea_store at 1E2EF ($A2EF bank 7): LD (BC),A $8E01
# CHECK cartarea_store at 1E2F5 ($A2F5 bank 7): LD (BC),A $8E01
# CHECK cartarea_store at 1E31B ($A31B bank 7): LD (DE),A $0202,$0204
# CHECK cartarea_store at 1E322 ($A322 bank 7): LD (BC),A $A424
# CHECK cartarea_store at 1E33D ($A33D bank 7): LD (BC),A $00B0
# CHECK cartarea_store at 1E488 ($A488 bank 7): LD (DE),A $0073,$0202,$6F01
# CHECK cartarea_store at 1E48F ($A48F bank 7): LD (BC),A $A5E3
# CHECK cartarea_store at 1E4AA ($A4AA bank 7): LD (BC),A $A3D2,$A4D2
# CHECK cartarea_store at 1E4E2 ($A4E2 bank 7): LD (HL),B $49B5,$4AB5
# CHECK cartarea_store at 1E612 ($A612 bank 7): LD (BC),A $B5FB
# CHECK cartarea_store at 1E627 ($A627 bank 7): LD (DE),A $0202,$0303,$2F06,$2F07...
# CHECK cartarea_store at 1E661 ($A661 bank 7): LD (DE),A $8201
# CHECK cartarea_store at 1E683 ($A683 bank 7): LD (BC),A $BFC4
# CHECK cartarea_store at 1E9C7 ($A9C7 bank 7): LD (DE),A $0202
# CHECK cartarea_store at 1E9C8 ($A9C8 bank 7): LD (BC),A $7F00,$7F03
# CHECK cartarea_store at 1E9D1 ($A9D1 bank 7): LD (BC),A $8003
# CHECK cartarea_store at 1E9D7 ($A9D7 bank 7): LD (BC),A $1000,$1003
# CHECK cartarea_store at 1E9DA ($A9DA bank 7): LD (BC),A $1000,$1003
# CHECK cartarea_store at 1E9E0 ($A9E0 bank 7): LD (BC),A $1000,$1003
# CHECK cartarea_store at 1E9E9 ($A9E9 bank 7): LD (BC),A $0F00,$0F03
# CHECK cartarea_store at 1E9ED ($A9ED bank 7): LD (BC),A $1000,$1003
# CHECK cartarea_store at 1E9F6 ($A9F6 bank 7): LD (BC),A $0308
# CHECK cartarea_store at 1E9FF ($A9FF bank 7): LD (BC),A $0100,$0408
# CHECK cartarea_store at 1EA08 ($AA08 bank 7): LD (BC),A $0200,$0508,$AEF0
# CHECK cartarea_store at 1EA10 ($AA10 bank 7): LD (BC),A $0200,$0508,$AEF0
# CHECK cartarea_store at 1EA12 ($AA12 bank 7): LD (BC),A $0200,$0508,$AEF0
# CHECK cartarea_store at 1EA5B ($AA5B bank 7): LD (HL),E $0F03
# CHECK cartarea_store at 1EA66 ($AA66 bank 7): LD (HL),E $0F03
# CHECK cartarea_store at 1EAC0 ($AAC0 bank 7): LD (DE),A $2602
# CHECK cartarea_store at 1EAC1 ($AAC1 bank 7): LD (BC),A $7F04
# CHECK cartarea_store at 1EAC7 ($AAC7 bank 7): LD (BC),A $7E05
# CHECK cartarea_store at 1EACA ($AACA bank 7): LD (BC),A $7E05
# CHECK cartarea_store at 1EAD3 ($AAD3 bank 7): LD (BC),A $7E05
# CHECK cartarea_store at 1EAE2 ($AAE2 bank 7): LD (BC),A $7D05,$7E05
# CHECK cartarea_store at 1EAE6 ($AAE6 bank 7): LD (BC),A $7E05,$7F05
# CHECK cartarea_store at 1EAEF ($AAEF bank 7): LD (BC),A $0104
# CHECK cartarea_store at 1EAF8 ($AAF8 bank 7): LD (BC),A $0205
# CHECK cartarea_store at 1EAFE ($AAFE bank 7): LD (BC),A $0106
# CHECK cartarea_store at 1EB01 ($AB01 bank 7): LD (BC),A $0106,$03AC
# CHECK cartarea_store at 1EB09 ($AB09 bank 7): LD (BC),A $0106,$03AC
# CHECK cartarea_store at 1EB0B ($AB0B bank 7): LD (BC),A $0106,$03AC
# CHECK cartarea_store at 1EB76 ($AB76 bank 7): LD (HL),B $AE0B
# CHECK cartarea_store at 1EB77 ($AB77 bank 7): LD (BC),A $8004,$8908
# CHECK cartarea_store at 1EB92 ($AB92 bank 7): LD (BC),A $8908,$8A08,$8B08
# CHECK cartarea_store at 1EBBB ($ABBB bank 7): LD (BC),A $030B
# CHECK cartarea_store at 1EBC1 ($ABC1 bank 7): LD (BC),A $040B
# CHECK cartarea_store at 1EBC4 ($ABC4 bank 7): LD (BC),A $050B
# CHECK cartarea_store at 1EBCA ($ABCA bank 7): LD (BC),A $060B
# CHECK cartarea_store at 1EBCE ($ABCE bank 7): LD (BC),A $070B
# CHECK cartarea_store at 1EBCF ($ABCF bank 7): LD (BC),A $070B
# CHECK cartarea_store at 1EBD3 ($ABD3 bank 7): LD (BC),A $090B
# CHECK cartarea_store at 1EBD9 ($ABD9 bank 7): LD (BC),A $090B
# CHECK cartarea_store at 1EBDA ($ABDA bank 7): LD (BC),A $090B
# CHECK cartarea_store at 1EBEA ($ABEA bank 7): LD (BC),A $090B
# CHECK cartarea_store at 1EBEB ($ABEB bank 7): LD (BC),A $090B
# CHECK cartarea_store at 1EBEF ($ABEF bank 7): LD (BC),A $0A0B
# CHECK cartarea_store at 1EBF0 ($ABF0 bank 7): LD (BC),A $0A0B
# CHECK cartarea_store at 1EBF7 ($ABF7 bank 7): LD (BC),A $0A0B
# CHECK cartarea_store at 1EBFD ($ABFD bank 7): LD (BC),A $0B0B
# CHECK cartarea_store at 1EC01 ($AC01 bank 7): LD (BC),A $0C0B
# CHECK cartarea_store at 1EC07 ($AC07 bank 7): LD (BC),A $0D0B
# CHECK cartarea_store at 1EC0B ($AC0B bank 7): LD (BC),A $0E0B
# CHECK cartarea_store at 1EC0C ($AC0C bank 7): LD (BC),A $0E0B
# CHECK cartarea_store at 1EC10 ($AC10 bank 7): LD (BC),A $100B
# CHECK cartarea_store at 1EC18 ($AC18 bank 7): LD (BC),A $110B
# CHECK cartarea_store at 1EC21 ($AC21 bank 7): LD (BC),A $110B
# CHECK cartarea_store at 1EC85 ($AC85 bank 7): LD (BC),A $0704
# CHECK cartarea_store at 1EC8D ($AC8D bank 7): LD (BC),A $0704
# CHECK cartarea_store at 1EC99 ($AC99 bank 7): LD (BC),A $8589
# CHECK cartarea_store at 1EC9E ($AC9E bank 7): LD (BC),A $8589
# CHECK cartarea_store at 1ECB2 ($ACB2 bank 7): LD (BC),A $028D
# CHECK cartarea_store at 1ECBA ($ACBA bank 7): LD (BC),A $02B1
# CHECK cartarea_store at 1ECBF ($ACBF bank 7): LD (BC),A $8581
# CHECK cartarea_store at 1ECC2 ($ACC2 bank 7): LD (BC),A $8581
# CHECK cartarea_store at 1ECCF ($ACCF bank 7): LD (BC),A $8585
# CHECK cartarea_store at 1ECE1 ($ACE1 bank 7): LD (BC),A $B102
# CHECK cartarea_store at 1ECE9 ($ACE9 bank 7): LD (BC),A $B102
# CHECK cartarea_store at 1ECEF ($ACEF bank 7): LD (BC),A $8D89
# CHECK cartarea_store at 1ECF4 ($ACF4 bank 7): LD (BC),A $8D89
# CHECK cartarea_store at 1ED0D ($AD0D bank 7): LD (BC),A $0289
# CHECK cartarea_store at 1ED12 ($AD12 bank 7): LD (BC),A $0289
# CHECK cartarea_store at 1ED19 ($AD19 bank 7): LD (BC),A $8589
# CHECK cartarea_store at 1ED73 ($AD73 bank 7): LD (BC),A $828B
# CHECK cartarea_store at 1ED7F ($AD7F bank 7): LD (BC),A $868B
# CHECK cartarea_store at 1ED8A ($AD8A bank 7): LD (BC),A $868C
# CHECK cartarea_store at 1EF0D ($AF0D bank 7): LD (BC),A $89B2,$89F3,$89F7
# CHECK cartarea_store at 1F0FD ($B0FD bank 7): LD (BC),A $1580
# CHECK cartarea_store at 1F235 ($B235 bank 7): LD (BC),A $010C
# CHECK cartarea_store at 1F2AB ($B2AB bank 7): LD (BC),A $80A5
# CHECK cartarea_store at 1F2AE ($B2AE bank 7): LD (BC),A $80A5
# CHECK cartarea_store at 1F322 ($B322 bank 7): LD (BC),A $0003,$02F2
# CHECK cartarea_store at 1F335 ($B335 bank 7): LD (BC),A $B37F
# CHECK cartarea_store at 1F34C ($B34C bank 7): LD (BC),A $B380
# CHECK cartarea_store at 1F352 ($B352 bank 7): LD (BC),A $B380
# CHECK cartarea_store at 1F358 ($B358 bank 7): LD (BC),A $B380
# CHECK cartarea_store at 1F383 ($B383 bank 7): LD (BC),A $96E1
# CHECK cartarea_store at 1F389 ($B389 bank 7): LD (BC),A $96E1
# CHECK cartarea_store at 1F38F ($B38F bank 7): LD (BC),A $96E1
# CHECK cartarea_store at 1F3CA ($B3CA bank 7): LD (DE),A $0001
# CHECK cartarea_store at 1F4E9 ($B4E9 bank 7): LD (BC),A $1580
# CHECK cartarea_store at 1F502 ($B502 bank 7): LD (BC),A $1580
# CHECK cartarea_store at 1F5C9 ($B5C9 bank 7): LD (BC),A $1580
# CHECK cartarea_store at 1F5EE ($B5EE bank 7): LD (BC),A $B5F2
# CHECK cartarea_store at 1F5F8 ($B5F8 bank 7): LD (BC),A $019B
# CHECK cartarea_store at 1F675 ($B675 bank 7): LD (DE),A $B601
# CHECK cartarea_store at 1F69A ($B69A bank 7): LD (BC),A $0002
# CHECK cartarea_store at 1F69F ($B69F bank 7): LD ($B699),HL $B699,$B69A
# CHECK cartarea_store at 1F6A3 ($B6A3 bank 7): LD ($04B1),HL $04B1,$04B2
# CHECK cartarea_store at 1F773 ($B773 bank 7): LD (BC),A $0003
# CHECK cartarea_store at 1F779 ($B779 bank 7): LD (BC),A $B799
# CHECK cartarea_store at 1F77A ($B77A bank 7): LD (BC),A $B799
# CHECK cartarea_store at 1F782 ($B782 bank 7): LD (BC),A $B799
# CHECK cartarea_store at 1F795 ($B795 bank 7): LD (BC),A $B7A1
# CHECK cartarea_store at 1F7A8 ($B7A8 bank 7): LD (BC),A $B7A2
# CHECK cartarea_store at 1F7AC ($B7AC bank 7): LD (BC),A $1580,$B7A3
# CHECK cartarea_store at 1F7BE ($B7BE bank 7): LD (BC),A $0005
# CHECK cartarea_store at 1F7E5 ($B7E5 bank 7): LD (BC),A $0180,$1580
# CHECK cartarea_store at 1F81B ($B81B bank 7): LD (BC),A $A512
# CHECK cartarea_store at 1F87C ($B87C bank 7): LD (BC),A $3000
# CHECK cartarea_store at 1F8D3 ($B8D3 bank 7): DEC (HL) $2300
# CHECK cartarea_store at 1F8D4 ($B8D4 bank 7): LD ($2721),A $2721
# CHECK ram_exec at 00295 ($0295 bank 0): CALL $CC00 $CC00
# CHECK ram_exec at 00364 ($0364 bank 0): CALL $CEFB $CEFB
# CHECK ram_exec at 0036C ($036C bank 0): CALL $CEFB $CEFB
# CHECK ram_exec at 00374 ($0374 bank 0): JP $CEFB $CEFB
# CHECK ram_exec at 003B7 ($03B7 bank 0): CALL $CEBB $CEBB
# CHECK ram_exec at 003BC ($03BC bank 0): CALL $CEBB $CEBB
# CHECK ram_exec at 003C1 ($03C1 bank 0): JP $CEBB $CEBB
# CHECK ram_exec at 003DB ($03DB bank 0): JP $CF59 $CF59
# CHECK ram_exec at 021D3 ($21D3 bank 0): CALL $CC00 $CC00
# CHECK ram_exec at 06054 ($6054 bank 1): JP NZ,$FECD $FECD
# CHECK ram_exec at 1D172 ($9172 bank 7): CALL P,$E000 $E000
# CHECK ram_exec at 1D6FD ($96FD bank 7): JP NZ,$C224 $C224
# CHECK ram_exec at 1D8C8 ($98C8 bank 7): CALL M,$F501 $F501
# CHECK ram_exec at 1D8DF ($98DF bank 7): CALL M,$F500 $F500
# CHECK ram_exec at 1D9EB ($99EB bank 7): JP M,$F106 $F106
# CHECK ram_exec at 1DA1E ($9A1E bank 7): JP M,$F106 $F106
# CHECK ram_exec at 1DA7A ($9A7A bank 7): JP M,$F106 $F106
# CHECK ram_exec at 1DAB7 ($9AB7 bank 7): JP M,$F106 $F106
# CHECK ram_exec at 1DACB ($9ACB bank 7): JP M,$F106 $F106
# CHECK ram_exec at 1DAEF ($9AEF bank 7): JP M,$F106 $F106
# CHECK ram_exec at 1DB57 ($9B57 bank 7): CALL M,$F800 $F800
# CHECK ram_exec at 1DBC3 ($9BC3 bank 7): CALL M,$F600 $F600
# CHECK ram_exec at 1DF3C ($9F3C bank 7): CALL P,$F000 $F000
# CHECK ram_exec at 1E0D1 ($A0D1 bank 7): CALL M,$E101 $E101
# CHECK ram_exec at 1E0F8 ($A0F8 bank 7): CALL M,$E400 $E400
# CHECK ram_exec at 1E11A ($A11A bank 7): CALL M,$F501 $F501
# CHECK ram_exec at 1E14A ($A14A bank 7): CALL M,$F500 $F500
# CHECK ram_exec at 1E316 ($A316 bank 7): CALL P,$E000 $E000
# CHECK ram_exec at 1E369 ($A369 bank 7): CALL M,$F501 $F501
# CHECK ram_exec at 1E62D ($A62D bank 7): CALL M,$F501 $F501
# CHECK ram_exec at 1E9C2 ($A9C2 bank 7): CALL P,$E000 $E000
# CHECK ram_exec at 1EB3D ($AB3D bank 7): JP P,$F380 $F380
# CHECK ram_exec at 1EC13 ($AC13 bank 7): JP P,$F302 $F302
# CHECK ram_exec at 1EC31 ($AC31 bank 7): JP P,$F303 $F303
# CHECK ram_exec at 1F2B7 ($B2B7 bank 7): JP M,$C303 $C303
# CHECK ram_exec at 1F5D4 ($B5D4 bank 7): JP C,$F5B5 $F5B5
# CHECK ram_exec at 1F7F8 ($B7F8 bank 7): JP P,$F202 $F202
# CHECK ram_exec at 1F818 ($B818 bank 7): JP P,$F203 $F203
# CHECK indirect_unresolved at 00043 ($0043 bank 0): JP (HL) 
# CHECK indirect_unresolved at 00103 ($0103 bank 0): RET NZ 
# CHECK indirect_unresolved at 00304 ($0304 bank 0): RET 
# CHECK indirect_unresolved at 00304 ($0304 bank 0): RET 
# CHECK indirect_unresolved at 0040F ($040F bank 0): JP (HL) 
# CHECK indirect_unresolved at 00516 ($0516 bank 0): RET 
# CHECK indirect_unresolved at 0062C ($062C bank 0): RET 
# CHECK indirect_unresolved at 009C6 ($09C6 bank 0): RET 
# CHECK indirect_unresolved at 00AD2 ($0AD2 bank 0): JP (HL) 
# CHECK indirect_unresolved at 00BFA ($0BFA bank 0): JP (HL) 
# CHECK indirect_unresolved at 01D5F ($1D5F bank 0): RET 
# CHECK indirect_unresolved at 1D3F2 ($93F2 bank 7): RET M 
# CHECK indirect_unresolved at 1D409 ($9409 bank 7): RET M 
# CHECK indirect_unresolved at 1D425 ($9425 bank 7): RET M 
# CHECK indirect_unresolved at 1D437 ($9437 bank 7): RET M 
# CHECK indirect_unresolved at 1D8B4 ($98B4 bank 7): RET M 
# CHECK indirect_unresolved at 1D9E6 ($99E6 bank 7): RET NZ 
# CHECK indirect_unresolved at 1DA0A ($9A0A bank 7): RET NC 
# CHECK indirect_unresolved at 1DA10 ($9A10 bank 7): RET NC 
# CHECK indirect_unresolved at 1DA12 ($9A12 bank 7): RET M 
# CHECK indirect_unresolved at 1DA32 ($9A32 bank 7): RET NC 
# CHECK indirect_unresolved at 1DA34 ($9A34 bank 7): RET M 
# CHECK indirect_unresolved at 1DA51 ($9A51 bank 7): RET PO 
# CHECK indirect_unresolved at 1E321 ($A321 bank 7): RET NC 
# CHECK indirect_unresolved at 1E352 ($A352 bank 7): RET NZ 
# CHECK indirect_unresolved at 1E35B ($A35B bank 7): RET PO 
# CHECK indirect_unresolved at 1E4D7 ($A4D7 bank 7): RET M 
# CHECK indirect_unresolved at 1E4DC ($A4DC bank 7): RET M 
# CHECK indirect_unresolved at 1E4E4 ($A4E4 bank 7): RET M 
# CHECK indirect_unresolved at 1E4E7 ($A4E7 bank 7): RET M 
# CHECK indirect_unresolved at 1E4EA ($A4EA bank 7): RET M 
# CHECK indirect_unresolved at 1E4ED ($A4ED bank 7): RET M 
# CHECK indirect_unresolved at 1E4F3 ($A4F3 bank 7): RET M 
# CHECK indirect_unresolved at 1E615 ($A615 bank 7): RET M 
# CHECK indirect_unresolved at 1E618 ($A618 bank 7): RET M 
# CHECK indirect_unresolved at 1E61B ($A61B bank 7): RET M 
# CHECK indirect_unresolved at 1EC81 ($AC81 bank 7): RET M 
# CHECK indirect_unresolved at 1EC89 ($AC89 bank 7): RET M 
# CHECK indirect_unresolved at 1EC95 ($AC95 bank 7): RET M 
# CHECK indirect_unresolved at 1F367 ($B367 bank 7): RET PO 
# CHECK indirect_unresolved at 1F367 ($B367 bank 7): RET PO 
# CHECK indirect_unresolved at 1F39E ($B39E bank 7): RET PO 
# CHECK indirect_unresolved at 1F39E ($B39E bank 7): RET PO 
# CHECK indirect_unresolved at 1F791 ($B791 bank 7): RET NZ 
# CHECK indirect_unresolved at 1F86E ($B86E bank 7): RET NZ 
# CHECK bank_unresolved at 04915 ($4915 bank 1): CALL NZ,$A13A $A13A
# CHECK low: site 00483  OUT ($BE),A  (vdp_data)
# CHECK low: site 0049A  OUT ($BE),A  (vdp_data)
# CHECK low: site 01026  IN A,($C1)  (joypad_b_misc)
site 04466   ; OUT ($BE),A
site 0446B   ; OUT ($BE),A
# CHECK low: site 0545D  OUT ($BE),A  (vdp_data)
# CHECK low: site 05463  OUT ($BE),A  (vdp_data)
# CHECK low: site 05875  OUT ($BE),A  (vdp_data)
# CHECK low: site 0587A  OUT ($BE),A  (vdp_data)
# CHECK low: site 0587F  OUT ($BE),A  (vdp_data)
# CHECK low: site 05884  OUT ($BE),A  (vdp_data)
# CHECK low: site 05960  OUT ($BE),A  (vdp_data)
# CHECK low: site 05965  OUT ($BE),A  (vdp_data)
# CHECK low: site 06913  OUT ($BE),A  (vdp_data)
# CHECK low: site 0691A  OUT ($BE),A  (vdp_data)
# CHECK low: site 06A43  OUT ($BE),A  (vdp_data)
# CHECK low: site 07C3C  OUT ($BE),A  (vdp_data)
# CHECK low: site 07CEF  OUT ($BE),A  (vdp_data)
# CHECK low: site 07CFE  OUT ($BE),A  (vdp_data)
# CHECK low: site 07E46  IN A,($7E)  (v_counter)
# CHECK low: site 07E52  OUT ($BF),A  (vdp_control)
# CHECK low: site 07E56  OUT ($BF),A  (vdp_control)
# CHECK low: site 0B8A9  IN A,($DC)  (joypad_a)
# CHECK low: site 0BCF9  IN A,($DC)  (joypad_a)
# CHECK low: site 10139  IN A,($DC)  (joypad_a)
# CHECK low: site 10C99  OUT ($DC),A  (no_effect)
# CHECK low: site 141A0  IN A,($DC)  (joypad_a)
# CHECK low: site 14F07  OUT ($C0),A  (no_effect)
# CHECK low: site 1671D  IN A,($DC)  (joypad_a)
# CHECK low: site 1B894  OUT ($3E),A  (memory_control)
# CHECK low: site 1B898  IN A,($BE)  (vdp_data)
# CHECK low: site 1B8AD  OUT ($3E),A  (memory_control)
# CHECK low: site 1B8B1  IN A,($BE)  (vdp_data)
# CHECK low: site 1B8B7  OUT ($3E),A  (memory_control)
# CHECK low: site 1C627  OUT ($F0),A  (fm_address)
# CHECK low: site 1C62D  OUT ($F1),A  (fm_data)
# CHECK low: site 1C6F6  OUT ($F0),A  (fm_address)
# CHECK low: site 1C6FD  OUT ($F1),A  (fm_data)
# CHECK low: site 1C8AB  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 1C8E9  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 1CA96  OUTI  (port in C)
# CHECK low: site 1CA9D  OUTI  (port in C)
# CHECK low: site 1CB89  OUT ($7F),A  (psg)
# CHECK low: site 1CB8D  OUT ($7F),A  (psg)
# CHECK low: site 1CD32  OUT ($F0),A  (fm_address)
# CHECK low: site 1CD39  OUT ($F1),A  (fm_data)
# CHECK low: site 1CD45  OUT ($F0),A  (fm_address)
# CHECK low: site 1CD5C  OUT ($F1),A  (fm_data)
# CHECK low: site 1CD66  OUT ($F0),A  (fm_address)
# CHECK low: site 1CD70  OUT ($F1),A  (fm_data)
# CHECK low: site 1FBDE  IN A,($DC)  (joypad_a)
# CHECK low: site 1FD8D  IN A,($BD)  (vdp_status)
# CHECK low: site 23C8E  IN A,($DC)  (joypad_a)
# CHECK low: site 27325  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 27334  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 27562  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 27574  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 27E63  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 30D73  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 30E66  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 37B83  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 37C77  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 387C1  IN A,($DC)  (joypad_a)
# CHECK low: site 387F1  IN A,($DC)  (joypad_a)
# CHECK low: site 3894A  IN A,($DC)  (joypad_a)
# CHECK low: site 38953  IN A,($DC)  (joypad_a)
# CHECK low: site 3C50D  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 3CA9E  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 3CAC9  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 3CC85  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 3CCB0  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 3EAE4  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 3FB1F  IN A,($DC)  (joypad_a)
# Fantasy Zone II unpacks its VRAM routines into RAM $CC00-$CF7A from the
# packed stream at ROM $1B7D5 (routine $07A9). These pokes change the stream
# so the unpacked code has RST io + op at its 368 I/O instructions
# (all trace ops; 301 start a run or loop). Made by fantasyzone2-ramcode.py, next to this file.
poke 1B7DB BF 1D
poke 1B7DD BF 1D
poke 1B7E2 AB CB
poke 1B7E5 BF 1D
poke 1B7E7 BF 1D
poke 1B7EA ED C7
poke 1B7EB ED C7
poke 1B7ED ED C7
poke 1B7EE ED C7
poke 1B7F0 ED C7
poke 1B7F1 ED C7
poke 1B7F3 ED C7
poke 1B7F4 ED C7
poke 1B7F6 ED C7
poke 1B7F7 ED C7
poke 1B7F9 ED C7
poke 1B7FA ED C7
poke 1B7FC ED C7
poke 1B7FD ED C7
poke 1B7FF ED C7
poke 1B800 ED C7
poke 1B802 ED C7
poke 1B803 ED C7
poke 1B805 ED C7
poke 1B806 ED C7
poke 1B808 ED C7
poke 1B809 ED C7
poke 1B80B ED C7
poke 1B80C ED C7
poke 1B80E ED C7
poke 1B80F ED C7
poke 1B811 ED C7
poke 1B812 ED C7
poke 1B814 ED C7
poke 1B815 ED C7
poke 1B817 ED C7
poke 1B818 ED C7
poke 1B81A ED C7
poke 1B81B ED C7
poke 1B81D ED C7
poke 1B81E ED C7
poke 1B820 ED C7
poke 1B821 ED C7
poke 1B823 ED C7
poke 1B824 ED C7
poke 1B826 ED C7
poke 1B827 ED C7
poke 1B829 ED C7
poke 1B82A ED C7
poke 1B82C ED C7
poke 1B82D ED C7
poke 1B82F ED C7
poke 1B830 ED C7
poke 1B832 ED C7
poke 1B833 ED C7
poke 1B835 ED C7
poke 1B836 ED C7
poke 1B838 ED C7
poke 1B839 ED C7
poke 1B83B ED C7
poke 1B83C ED C7
poke 1B83E ED C7
poke 1B83F ED C7
poke 1B841 ED C7
poke 1B842 ED C7
poke 1B844 ED C7
poke 1B845 ED C7
poke 1B848 ED C7
poke 1B84B ED C7
poke 1B84C ED C7
poke 1B84E ED C7
poke 1B84F ED C7
poke 1B851 ED C7
poke 1B852 ED C7
poke 1B854 ED C7
poke 1B855 ED C7
poke 1B857 ED C7
poke 1B858 ED C7
poke 1B85A ED C7
poke 1B85B ED C7
poke 1B85D ED C7
poke 1B85E ED C7
poke 1B860 ED C7
poke 1B861 ED C7
poke 1B863 ED C7
poke 1B864 ED C7
poke 1B866 ED C7
poke 1B867 ED C7
poke 1B869 ED C7
poke 1B86A ED C7
poke 1B86C ED C7
poke 1B86D ED C7
poke 1B86F ED C7
poke 1B870 ED C7
poke 1B872 ED C7
poke 1B873 ED C7
poke 1B875 ED C7
poke 1B876 ED C7
poke 1B878 ED C7
poke 1B879 ED C7
poke 1B87B ED C7
poke 1B87C ED C7
poke 1B87E ED C7
poke 1B87F ED C7
poke 1B881 ED C7
poke 1B882 ED C7
poke 1B884 ED C7
poke 1B885 ED C7
poke 1B887 ED C7
poke 1B888 ED C7
poke 1B88A ED C7
poke 1B88B ED C7
poke 1B88D ED C7
poke 1B88E ED C7
poke 1B890 ED C7
poke 1B891 ED C7
poke 1B894 D3 C7
poke 1B896 D3 C7
poke 1B89B ED C7
poke 1B89F BF 1D
poke 1B8A0 D3 C7
poke 1B8A4 A3 C3
poke 1B8A6 A3 C3
poke 1B8AD D3 C7
poke 1B8AF D3 C7
poke 1B8B4 ED C7
poke 1B8B7 D3 C7
poke 1B8B9 D3 C7
poke 1B8BD A3 C3
poke 1B8BE AB CB
poke 1B8C0 A3 C3
poke 1B8C1 AB CB
poke 1B8C3 A3 C3
poke 1B8C4 AB CB
poke 1B8C6 A3 C3
poke 1B8C7 AB CB
poke 1B8C9 A3 C3
poke 1B8CA AB CB
poke 1B8CC A3 C3
poke 1B8CD AB CB
poke 1B8CF A3 C3
poke 1B8D0 AB CB
poke 1B8D2 A3 C3
poke 1B8D3 AB CB
poke 1B8D5 A3 C3
poke 1B8D6 AB CB
poke 1B8D8 A3 C3
poke 1B8D9 AB CB
poke 1B8DB A3 C3
poke 1B8DC AB CB
poke 1B8DE A3 C3
poke 1B8DF AB CB
poke 1B8E1 A3 C3
poke 1B8E2 AB CB
poke 1B8E4 A3 C3
poke 1B8E5 AB CB
poke 1B8E7 A3 C3
poke 1B8E8 AB CB
poke 1B8EA A3 C3
poke 1B8EB AB CB
poke 1B8ED A3 C3
poke 1B8EE AB CB
poke 1B8F0 A3 C3
poke 1B8F1 AB CB
poke 1B8F3 A3 C3
poke 1B8F4 AB CB
poke 1B8F6 A3 C3
poke 1B8F7 AB CB
poke 1B8F9 A3 C3
poke 1B8FA AB CB
poke 1B8FC A3 C3
poke 1B8FD AB CB
poke 1B8FF A3 C3
poke 1B900 AB CB
poke 1B902 A3 C3
poke 1B903 AB CB
poke 1B905 A3 C3
poke 1B906 AB CB
poke 1B908 A3 C3
poke 1B909 AB CB
poke 1B90B A3 C3
poke 1B90C AB CB
poke 1B90E A3 C3
poke 1B90F AB CB
poke 1B911 A3 C3
poke 1B912 AB CB
poke 1B914 A3 C3
poke 1B915 AB CB
poke 1B917 A3 C3
poke 1B918 AB CB
poke 1B91A A3 C3
poke 1B91B AB CB
poke 1B91D A3 C3
poke 1B91E AB CB
poke 1B920 A3 C3
poke 1B921 AB CB
poke 1B923 A3 C3
poke 1B924 AB CB
poke 1B926 A3 C3
poke 1B927 AB CB
poke 1B929 A3 C3
poke 1B92A AB CB
poke 1B92C A3 C3
poke 1B92D AB CB
poke 1B92F A3 C3
poke 1B930 AB CB
poke 1B932 A3 C3
poke 1B933 AB CB
poke 1B936 A3 C3
poke 1B937 AB CB
poke 1B939 A3 C3
poke 1B93A AB CB
poke 1B93C A3 C3
poke 1B93D AB CB
poke 1B93F A3 C3
poke 1B940 AB CB
poke 1B942 A3 C3
poke 1B943 AB CB
poke 1B945 A3 C3
poke 1B946 AB CB
poke 1B948 A3 C3
poke 1B949 AB CB
poke 1B94B A3 C3
poke 1B94C AB CB
poke 1B94E A3 C3
poke 1B94F AB CB
poke 1B951 A3 C3
poke 1B952 AB CB
poke 1B954 A3 C3
poke 1B955 AB CB
poke 1B957 A3 C3
poke 1B958 AB CB
poke 1B95A A3 C3
poke 1B95B AB CB
poke 1B95D A3 C3
poke 1B95E AB CB
poke 1B960 A3 C3
poke 1B961 AB CB
poke 1B963 A3 C3
poke 1B964 AB CB
poke 1B967 BF 1D
poke 1B969 BF 1D
poke 1B96E A3 C3
poke 1B971 D3 C7
poke 1B973 BF 1D
poke 1B976 ED C7
poke 1B978 ED C7
# Sprite table upload, every frame from the frame handler ($0295) and once at $21D3,
# as native code in page 0. The game's routine is the RAM code at $CC00 (unpacked
# from the stream above): 360 OUTI and OUTD to the sprite table, 65-80% of a frame
# through the traps. Both CALL $CC00 go to a far call at $0011-$0015 (filler
# bytes between RST $08's routine and RST $18).
label sat_far 00011
asm 00011 5          ; filler bytes
    rst $00
    db far_io, pg_sat, ent_sat
    ret
endasm
asm 00295 3          ; CALL $CC00 in the frame handler
    call sat_far
endasm
asm 021D3 3          ; CALL $CC00
    call sat_far
endasm
# Run-length unpacker ($07A4/$07A9/$07AE set the step, then $07B1), as native code
# in page 0. With A = 0 it writes VRAM through RST $08 (two control writes and one
# data write for every byte: about 2,300 Next cycles a byte through the traps, 55%
# of every frame for half a second at a stage start). $07B1-$07C1 becomes the far
# call; the page leaves interrupts off and returns A' = 1 where the game's code
# leaves them on (RST $08 does EI). $07C2 stays the RET it was.
asm 007B1 17         ; LD ($C10D),BC, LD B,C, the phase loop and EX AF,AF'
    rst $00
    db far_io, pg_unpk, ent_unpk
    ex af,af'
    or a
    jr z,$+3
    ei
    xor a
    ex af,af'
    ret
endasm
# Name table column writer ($0318-$034D, called from the frame handler through
# $0312 and at a stage start): 22 rows, each a control write and two data writes
# (the cell's bytes from two buffers 64 bytes a row apart), about 4,000 Next
# cycles a row through the traps. $031B-$034C becomes the far call; the patch
# turns interrupts off around it and restores them (the game's code leaves them
# alone), then sets A = 0 and the Z flag as the game's loop end does.
asm 0031B 50         ; the column loop, up to the RET at $034D
    ld a,i
    di
    push af
    rst $00
    db far_io, pg_ntcol, ent_ntcol
    pop af
    jp po,$+4
    ei
    ld a,1
    dec a
endasm
# Name table clear ($0525-$0537): 1,792 zero bytes to VRAM $3800, two OUT ($BE),A
# a pass, about 2,400 Next cycles a byte through the traps, at every stage start.
# $0528-$0537 becomes the far call; EI as the game's RST $08 leaves interrupts.
asm 00528 16         ; RST $08 and the clear loop
    di
    rst $00
    db far_io, pg_clr, ent_clr
    ei
endasm
# Tile animation uploads in the frame handler: $035A-$0376 writes 3 x 64 bytes to
# VRAM $2B40, $03B0-$03C3 writes 288 bytes to VRAM $0800, both through calls into
# the OUTI chain of the RAM code at $CC00. Each becomes a far call and a RET.
asm 0035A 29         ; LD DE,$6B40 to JP $CEFB
    rst $00
    db far_io, pg_anim1, ent_anim1
    ret
endasm
asm 003B0 20         ; LD DE,$4800 to JP $CEBB
    rst $00
    db far_io, pg_anim2, ent_anim2
    ret
endasm
page 0 sat unpk ntcol clr anim1 anim2
    OPT --zxnext
; ---------------------------------------------------------------------------
; sat: does what the RAM code at $CC00 does. ($C011) bit 0 = 0: sprite Y
; bytes 8-63 from $DB3F down to $DB08 into VRAM $3F08-$3F3F, then X and tile
; pairs 8-63 from $DC7E,$DC7F / $DC7C,$DC7D / ... / $DC10,$DC11 into VRAM
; $3F90-$3FFF. Bit 0 = 1: $DB00-$DB3F into $3F00-$3F3F and $DC00-$DC7F into
; $3F80-$3FFF. Returns the registers that code leaves: A = $7F, BC = $00BE,
; HL = $DC0E or $DC80, DE kept.
; ---------------------------------------------------------------------------
sat:    ld a,i                  ; P/V = IFF2
        push af
        di
        push ix
        push iy
        push de
        ld ix,0
        ld iy,0
        ld a,($C011)
        rrca
        jr c,sat_b
        ld hl,$DB3F             ; Y bytes, last entry first
        ld de,satbuf
        ld b,56
sat_a1: ld a,(hl)
        ld (de),a
        dec hl
        inc de
        djnz sat_a1
        ld hl,$DC7E             ; X and tile pairs, last entry first
        ld b,56
sat_a2: ld a,(hl)
        ld (de),a
        inc de
        inc l
        ld a,(hl)
        ld (de),a
        inc de
        dec l
        dec l
        dec l
        djnz sat_a2
        ld hl,satbuf
        ld de,$3F08
        ld bc,$3801             ; one run of 56 bytes
        ld a,1                  ; the source as mapped: this page
        call jt_vwrite
        ld hl,satbuf+56
        ld de,$3F90
        ld bc,$7001             ; one run of 112 bytes
        ld a,1
        call jt_vwrite
        ld hl,$DC0E
        jr sat_end
sat_b:  ld hl,$DB00
        ld de,$3F00
        ld bc,$4001             ; one run of 64 bytes
        xor a
        call jt_vwrite
        ld hl,$DC00
        ld de,$3F80
        ld bc,$8001             ; one run of 128 bytes
        xor a
        call jt_vwrite
        ld hl,$DC80
sat_end:
        pop de
        pop iy
        pop ix
        ld bc,$00BE
        pop af
        jp po,sat_di
        ei
sat_di: ld a,$7F
        ret

; ---------------------------------------------------------------------------
; unpk: does what $07B1-$07C2 and $07C3 do. In: HL = the stream, DE = the
; destination, BC = the step (1, 2 or 4), A = 0 for VRAM, else RAM. The stream
; holds one part per step; part p goes to DE + p, DE + p + step, and so on.
; A part is records up to a 0 byte: n (1-127, 0 = 256) and one byte to repeat
; n times, or $80 + n and n bytes. Sets ($C10D) = BC. Returns HL after the
; stream, DE + step, B = 0, C = the step, A as it came with the flags of OR A,
; and AF' = 0 with the flags of OR A (as the game's last OR A on a 0 byte)
; once the far call's patch has used it: here A' = 1 if interrupts are to be
; on after the call. Interrupts stay off while it runs.
; VRAM: the parts are unpacked into ubuf, interleaved as they lie in VRAM,
; then written with jt_vwrite: as one block for the bytes every part has, then
; the rest of each part in runs of 1 byte with the step between them. A stream
; that does not fit in ubuf is written a byte at a time.
; ---------------------------------------------------------------------------
UB_LIMH equ $3C                 ; ubuf ends at $3C00; one record adds at most 1024
unpk:   ld ($C10D),bc
        ld (u_flag),a
        ld (u_dst),de
        ld (u_src0),hl
        ld b,a
        ld a,i                  ; P/V = IFF2
        ld a,0
        jp po,unpk_1
        inc a
unpk_1: ld (u_ei),a             ; 1: interrupts were on
        di
        ld a,c
        ld (u_step),a
        push ix
        push iy
        ld ixl,a                ; IXL = the step, IXH = parts left
        ld ixh,a
        ld a,b
        or a
        jp nz,unpk_ram
; VRAM: unpack every part into ubuf, interleaved as in VRAM
        ld de,ubuf
        ld iy,u_cnt
        ld a,h
        cp $40
        jr c,uv_ph              ; a stream below $4000 can be in $2000-$3FFF
; the fast form: the stream is not in $2000-$3FFF, so plain reads
uf_ph:  push de                 ; the part's first byte in ubuf
uf_rec: ld a,(hl)
        inc hl
        or a
        jr z,uf_phend
        ld c,a
        and $7F
        ld b,a                  ; n (0 = 256)
        bit 7,c
        jr nz,uf_lit
        ld c,(hl)               ; n times the next byte
        inc hl
        ld a,ixl
        ex de,hl
uf_rep: ld (hl),c
        add hl,a
        djnz uf_rep
        ex de,hl
        jr uf_chk
uf_lit: ld c,b                  ; n bytes: BC = n for LDI
        ld b,0
        ld a,c
        or a
        jr nz,uf_l0
        inc b                   ; 256
uf_l0:  ld a,ixl
        dec a                   ; the step - 1
uf_l1:  ldi
        add de,a
        jp pe,uf_l1
uf_chk: ld a,d
        cp UB_LIMH
        jr c,uf_rec
        pop de
        jp uv_over              ; too big for ubuf
uf_phend:
        pop bc
        call ph_count
        dec ixh
        jr nz,uf_ph
        jr uv_dec_end
; the general form: every stream byte through rdb
uv_ph:  push de
uv_rec: call rdb
        or a
        jr z,uv_phend
        ld c,a
        and $7F
        ld b,a
        bit 7,c
        jr nz,uv_lit
        call rdb
        ld c,a
uv_rep: ld a,c
        ld (de),a
        ld a,ixl
        add de,a
        djnz uv_rep
        jr uv_chk
uv_lit: call rdb
        ld (de),a
        ld a,ixl
        add de,a
        djnz uv_lit
uv_chk: ld a,d
        cp UB_LIMH
        jr c,uv_rec
        pop de
        jp uv_over
uv_phend:
        pop bc
        call ph_count
        dec ixh
        jr nz,uv_ph
uv_dec_end:
        ld (u_src),hl
; m = the fewest bytes in a part
        ld a,(u_step)
        ld b,a
        ld iy,u_cnt
        ld hl,$FFFF
uv_min: ld e,(iy+0)
        ld d,(iy+1)
        push hl
        or a
        sbc hl,de
        pop hl
        jr c,uv_min1            ; HL < DE
        ex de,hl
uv_min1:
        inc iy
        inc iy
        djnz uv_min
        ld (u_min),hl
        ld a,(u_step)
uv_mul: rra
        jr c,uv_muld
        add hl,hl
        jr uv_mul
uv_muld:
        ld (u_tot),hl           ; m * step: the bytes every part has, as one block
        ld a,h
        or a
        jr z,uv_c2
        ld c,a                  ; runs of 256 bytes
        ld b,0
        ld hl,ubuf
        ld de,(u_dst)
        ld ix,256
        ld iy,256
        ld a,1
        call jt_vwrite
uv_c2:  ld a,(u_tot)
        or a
        jr z,uv_tails
        ld b,a                  ; the last run, under 256 bytes
        ld a,(u_tot+1)
        ld d,a
        ld e,0
        ld hl,ubuf
        add hl,de
        push hl
        ld hl,(u_dst)
        add hl,de
        ex de,hl
        pop hl
        ld c,1
        ld a,1
        call jt_vwrite
; the bytes past m in each part
uv_tails:
        ld iy,u_cnt
        xor a
        ld (u_p),a
uv_t1:  ld l,(iy+0)
        ld h,(iy+1)
        ld de,(u_min)
        or a
        sbc hl,de
        jr z,uv_t2
        push iy
        ld (u_t),hl
        ld hl,(u_tot)
        ld a,(u_p)
        add hl,a
        ex de,hl                ; m * step + p
        ld hl,ubuf
        add hl,de
        push hl
        ld hl,(u_dst)
        add hl,de
        ex de,hl
        pop hl
        ld a,(u_step)
        ld ixl,a
        ld ixh,0
        push ix
        pop iy                  ; IX = IY = the step
uv_t3:  ld bc,(u_t)
        ld a,b
        or a
        ld b,1
        jr z,uv_t4
        ld c,0                  ; 256 runs
uv_t4:  ld a,1
        call jt_vwrite
        ld bc,(u_t)
        ld a,b
        or a
        jr z,uv_t5
        dec b
        ld (u_t),bc
        ld a,b
        or c
        jr z,uv_t5
        ld a,(u_step)           ; 256 runs on
        add a,h
        ld h,a
        ld a,(u_step)
        add a,d
        ld d,a
        jr uv_t3
uv_t5:  pop iy
uv_t2:  inc iy
        inc iy
        ld a,(u_p)
        inc a
        ld (u_p),a
        ld hl,u_step
        cp (hl)
        jr c,uv_t1
; the VDP state after the game's last write: the last part with bytes
        ld a,(u_step)
        ld b,a                  ; B = p + 1
uv_f1:  dec iy
        dec iy
        ld l,(iy+0)
        ld h,(iy+1)
        ld a,h
        or l
        jr nz,uv_f2
        djnz uv_f1
        jr unpk_exit            ; no bytes: nothing written
uv_f2:  dec hl
        ld a,(u_step)
uv_f3:  rra
        jr c,uv_f4
        add hl,hl
        jr uv_f3
uv_f4:  ld a,b
        dec a
        add hl,a                ; the last byte: (n - 1) * step + p
        ld de,ubuf
        add hl,de
        ld a,(hl)
        ld (vdp_rbuf),a
        or a
        sbc hl,de
        inc hl
        ld de,(u_dst)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (vdp_addr),hl
        ld a,1
        ld (u_ei),a             ; RST $08 leaves interrupts on
unpk_exit:
        ld hl,(u_dst)
        ld a,(u_step)
        ld c,a
        ld b,0
        add hl,bc
        ex de,hl
        ld hl,(u_src)
        pop iy
        pop ix
        ld a,(u_ei)
        ex af,af'
        ld a,(u_flag)
        or a
        ret
; too big for ubuf: from the start again, a byte at a time
uv_over:
        ld hl,(u_src0)
        ld de,(u_dst)
        ld a,(u_step)
        ld ixl,a
        ld ixh,a
uo_ph:  push de
uo_rec: call rdb
        or a
        jr z,uo_phend
        ld c,a
        and $7F
        ld b,a
        bit 7,c
        jr nz,uo_lit
        call rdb
        ld c,a
uo_rep: ld a,c
        call uo_put
        djnz uo_rep
        jr uo_rec
uo_lit: call rdb
        call uo_put
        djnz uo_lit
        jr uo_rec
uo_phend:
        pop de
        inc de
        dec ixh
        jr nz,uo_ph
        ld (u_src),hl
        ld a,1
        ld (u_ei),a
        jp unpk_exit
; uo_put: A into VRAM at DE, DE += the step. Keeps BC, HL, IX, IY.
uo_put: push hl
        push bc
        ld (u_byte),a
        ld hl,u_byte
        ld bc,$0101
        ld a,1
        call jt_vwrite
        ld a,ixl
        add de,a
        pop bc
        pop hl
        ret
; RAM: the game's loop, natively
unpk_ram:
ur_ph:  push de
ur_rec: call rdb
        or a
        jr z,ur_phend
        ld c,a
        and $7F
        ld b,a
        bit 7,c
        jr nz,ur_lit
        call rdb
        ld c,a
ur_rep: ld a,c
        ld (de),a
        ld a,ixl
        add de,a
        djnz ur_rep
        jr ur_rec
ur_lit: call rdb
        ld (de),a
        ld a,ixl
        add de,a
        djnz ur_lit
        jr ur_rec
ur_phend:
        pop de
        inc de
        dec ixh
        jr nz,ur_ph
        ld (u_src),hl
        jp unpk_exit
; ---------------------------------------------------------------------------
; ntcol: does what $031B-$034C does. Name table column: 22 rows from VRAM
; ($C1D2), 64 bytes a row; each row's two bytes are (($C1D4) + 64 * row) and
; (($C1D6) + 64 * row). Copies the 44 bytes into ncbuf, then one jt_vwrite
; (22 runs of 2 bytes, 2 apart in ncbuf and 64 apart in VRAM). Returns HL, BC
; and DE past the last row (+ 22 * 64) and AF' as the game's last row leaves
; it (A' = D); the patch sets A and F.
; ---------------------------------------------------------------------------
ntcol:  push ix
        push iy
        ld de,($C1D2)
        push de
        ld hl,($C1D4)
        ld bc,($C1D6)
        ld de,ncbuf
        ld ixl,22
nc_row: call rdb
        dec hl
        ld (de),a
        inc de
        push hl
        ld h,b
        ld l,c
        call rdb
        pop hl
        ld (de),a
        inc de
        add hl,64
        add bc,64
        dec ixl
        jr nz,nc_row
        pop de
        push hl
        push bc
        ld hl,ncbuf
        ld bc,$0216             ; 22 runs of 2 bytes
        ld ix,2
        ld iy,64
        ld a,1                  ; the source as mapped: this page
        call jt_vwrite
        ex de,hl
        add hl,22*64
        ex de,hl
        ld a,e                  ; AF' as after the game's last row:
        sub $40                 ; A' = D, F' from ADC A,0 with the carry
        ld l,a                  ; of E + $40
        add a,$40
        ld a,d
        sbc a,0
        ld h,a
        ld a,l
        add a,$40
        ld a,h
        adc a,0
        ex af,af'
        pop bc
        pop hl
        pop iy
        pop ix
        ret

; ---------------------------------------------------------------------------
; clr: does what $0528-$0537 does: 1,792 zero bytes to VRAM DE ($7800 from
; $0525), with one jt_vwrite (7 runs of 256 bytes, all from zero256). Returns
; A = 0, HL = 0, the flags of OR on 0, DE kept.
; ---------------------------------------------------------------------------
clr:    push ix
        push iy
        push de
        ld hl,zero256
        ld bc,$0007             ; 7 runs of 256 bytes
        ld ix,0
        ld iy,256
        ld a,1
        call jt_vwrite
        pop de
        pop iy
        pop ix
        ld hl,0
        xor a
        ret

; ---------------------------------------------------------------------------
; anim1: does what $035A-$0376 does: 64 bytes from each of ($C1CB), ($C1CD)
; and ($C1CF), in that order, to VRAM $2B40-$2BFF. Returns A = $6B, BC = $00BE,
; DE = $6B40, HL = ($C1CF) + 64, Z set (as the last OUTI leaves B = 0).
; anim2: does what $03B0-$03C3 does: 288 bytes from HL to VRAM $0800-$091F.
; Returns A = $48, BC = $00BE, DE = $4800, HL + 288, Z set.
; ---------------------------------------------------------------------------
anim1:  push ix
        push iy
        ld de,$2B40
        ld hl,($C1CB)
        call an_64
        ld de,$2B80
        ld hl,($C1CD)
        call an_64
        ld de,$2BC0
        ld hl,($C1CF)
        call an_64
        ld bc,64
        add hl,bc
        ld de,$6B40
        ld a,$6B
        jr an_end
an_64:  ld bc,$4001             ; one run of 64 bytes
        xor a                   ; the source as the game sees it
        jp jt_vwrite
anim2:  push ix
        push iy
        ld de,$0800
        ld bc,$9002             ; 2 runs of 144 bytes
        ld ix,144
        ld iy,144
        xor a
        call jt_vwrite
        ld bc,288
        add hl,bc
        ld de,$4800
        ld a,$48
an_end: ld bc,$00BE
        pop iy
        pop ix
        cp a                    ; Z
        ret
; ph_count: the end of a part. BC = its first byte in ubuf, DE = past its
; last. Stores its bytes at (IY), IY + 2, DE = the next part's first byte.
; Keeps HL.
ph_count:
        push hl
        ex de,hl
        or a
        sbc hl,bc               ; bytes in the part * step
        ld a,ixl
pc_div: rra
        jr c,pc_divd
        srl h
        rr l
        jr pc_div
pc_divd:
        ld (iy+0),l
        ld (iy+1),h
        inc iy
        inc iy
        ld d,b
        ld e,c
        inc de
        pop hl
        ret
; rdb: A = the stream byte the game sees at HL, HL + 1. Keeps BC, DE.
rdb:    ld a,h
        sub $20
        cp $20
        jr c,rdb_pk             ; $2000-$3FFF: the game's page, not this one
        ld a,(hl)
        inc hl
        ret
rdb_pk: call jt_peek
        inc hl
        ret

u_flag: db 0
u_ei:   db 0
u_step: db 0
u_p:    db 0
u_byte: db 0
u_dst:  dw 0
u_src0: dw 0
u_src:  dw 0
u_min:  dw 0
u_tot:  dw 0
u_t:    dw 0
u_cnt:  ds 16                   ; bytes in each part
satbuf: ds 168
ncbuf:  ds 44
zero256: ds 256                 ; never written
ubuf:
endpage
