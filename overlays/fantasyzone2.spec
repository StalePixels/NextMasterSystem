# Fantasy Zone II, B8B141F9, drafted by tools/mkspec.py from sitescan output (with the detector log).
name Fantasy Zone II
cart B8B141F9
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
# CHECK low: site 04466  OUT ($BE),A  (vdp_data)
# CHECK low: site 0446B  OUT ($BE),A  (vdp_data)
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
