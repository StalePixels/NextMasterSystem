# Road Rash (Europe, Brazil) (En), CRC32 B876FC74, 512K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output, with reference I/O logs (600 s of random
# input, 180 s of the attract mode) and these scan entries: the two 8-entry jump tables
# after JP (HL) at $31C7 ($31C8: $3497 $3439 $33DF $3389 $3337 $32E9 $329F $3259) and
# $3508 ($3509: $3805 $37A6 $374A $36F1 $369B $3648 $35F8 $35AB), into unrolled VDP writes.
# Decisions:
# - $0038 jumps to a stub that the game copies from $04BD to $DFEA; site 004BE patches its
#   IN A,($BF) in the copy's source.
# - The line interrupt handlers are copied from $7E00 to $C100 (LDIR at $0448); the sites
#   07E02-07EE8 patch their VDP writes in the copy's source. The game rewrites only
#   operand bytes and $DFEE in that code, never an I/O instruction.
# - The stores to $8000-$8003 and the $FFFC bit 5 writes at $00B0-$02DB are a development
#   link that polls $8001; nothing in the game reaches it, and they are not patched.
name Road Rash
cart B876FC74
hz 50		; No-Intro regions Europe, Brazil
vector 10 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 00197   ; OUT ($BE),A
site 0024B   ; IN A,($BE)
site 002E0   ; OUT ($BF),A
site 002E8   ; OUT ($BF),A
site 002EC   ; OUT ($BF),A
site 002F4   ; OUT ($BF),A
site 002F8   ; OUT ($BF),A
site 002FE   ; OUT ($BF),A
site 00310   ; IN A,($BF)
site 0044D   ; IN A,($BF)
site 004BE   ; IN A,($BF)
site 0050E   ; IN A,($DC)
site 00514   ; IN A,($DD)
site 00555   ; OUT ($BF),A
site 00559   ; OUT ($BF),A
site 0055E   ; OUT ($BE),A
site 00570   ; OUT ($BF),A
site 00574   ; OUT ($BF),A
site 0058D   ; OUT ($BE),A
site 0059C   ; OUT ($BF),A
site 005A1   ; OUT ($BF),A
site 005A5   ; OUT ($BF),A
site 005AC   ; OUT ($BF),A
site 005B0   ; OUT ($BF),A
site 005B7   ; OUT ($BF),A
site 005C7   ; OUTI
site 005D8   ; OUT (C),B
site 005E0   ; OUTI
site 005E2   ; OUTI
site 005E4   ; OUTI
site 005E6   ; OUTI
site 005E8   ; OUTI
site 005EA   ; OUTI
site 005EC   ; OUTI
site 005EE   ; OUTI
site 005F0   ; OUTI
site 005F2   ; OUTI
site 005F4   ; OUTI
site 005F6   ; OUTI
site 005F8   ; OUTI
site 005FA   ; OUTI
site 005FC   ; OUTI
site 005FE   ; OUTI
site 00600   ; OUTI
site 00602   ; OUTI
site 00604   ; OUTI
site 00606   ; OUTI
site 00608   ; OUTI
site 0060A   ; OUTI
site 0060C   ; OUTI
site 0060E   ; OUTI
site 00610   ; OUTI
site 00612   ; OUTI
site 00614   ; OUTI
site 00616   ; OUTI
site 00618   ; OUTI
site 0061A   ; OUTI
site 0061C   ; OUTI
site 0061E   ; OUTI
site 00671   ; OUT ($BF),A
site 00677   ; OUT ($BF),A
site 0067E   ; OUTI
site 00756   ; OUT ($BE),A
site 0075C   ; OUT ($BE),A
site 00A57   ; IN A,($BF)
site 00A74   ; IN A,($DD)
site 00A7A   ; IN A,($BF)
site 00A82   ; OUT ($7F),A
site 00A86   ; OUT ($7F),A
site 00A8A   ; OUT ($7F),A
site 00A8E   ; OUT ($7F),A
site 00A92   ; OUT ($7F),A
site 00A96   ; OUT ($7F),A
site 00A9A   ; OUT ($7F),A
site 00A9E   ; OUT ($7F),A
site 00AA2   ; OUT ($7F),A
site 00AA6   ; OUT ($7F),A
site 00AAA   ; OUT ($7F),A
site 00D46   ; OUT ($BF),A
site 00D4D   ; OUT ($BF),A
site 00DF8   ; OUT (C),D
site 00DFE   ; OUT (C),E
site 00E04   ; OUT (C),H
site 00E0A   ; OUT (C),L
site 01005   ; OUT ($BF),A
site 0100A   ; OUT ($BF),A
site 01016   ; OUT ($BE),A
site 0101D   ; OUT ($BE),A
site 01074   ; OUT ($BE),A
site 0107B   ; OUT ($BE),A
site 010D9   ; OUT ($BE),A
site 010E0   ; OUT ($BE),A
site 010E7   ; OUT ($BE),A
site 010EC   ; OUT ($BE),A
site 01180   ; OUT ($BF),A
site 01184   ; OUT ($BF),A
site 011EC   ; OUT ($BF),A
site 011F0   ; OUT ($BF),A
site 011F5   ; OUT ($BE),A
site 011FC   ; OUT ($BE),A
site 01269   ; OUT ($BF),A
site 0126D   ; OUT ($BF),A
site 01271   ; OUT ($BF),A
site 01275   ; OUT ($BF),A
site 012C2   ; OUT ($BF),A
site 012C6   ; OUT ($BF),A
site 01C4A   ; IN A,($BF)
site 01D10   ; IN A,($BF)
site 01D5D   ; IN A,($DD)
site 01F08   ; OUT ($BF),A
site 01F0B   ; OUT ($BF),A
site 01F0D   ; OUTI
site 01F12   ; OUTI
site 01F18   ; OUT ($BF),A
site 01F1B   ; OUT ($BF),A
site 01F1D   ; OUTI
site 01F22   ; OUTI
site 01F28   ; OUT ($BF),A
site 01F2B   ; OUT ($BF),A
site 01F2D   ; OUTI
site 01F32   ; OUTI
site 01F38   ; OUT ($BF),A
site 01F3B   ; OUT ($BF),A
site 01F3D   ; OUTI
site 01F42   ; OUTI
site 01F48   ; OUT ($BF),A
site 01F4B   ; OUT ($BF),A
site 01F4D   ; OUTI
site 01F52   ; OUTI
site 01F58   ; OUT ($BF),A
site 01F5B   ; OUT ($BF),A
site 01F5D   ; OUTI
site 01F62   ; OUTI
site 01F68   ; OUT ($BF),A
site 01F6B   ; OUT ($BF),A
site 01F6D   ; OUTI
site 01F72   ; OUTI
site 01F78   ; OUT ($BF),A
site 01F7B   ; OUT ($BF),A
site 01F7D   ; OUTI
site 01F82   ; OUTI
site 01FB9   ; OUT ($BF),A
site 01FBC   ; OUT ($BF),A
site 01FBE   ; OUTI
site 01FC4   ; OUT ($BF),A
site 01FC7   ; OUT ($BF),A
site 01FC9   ; OUTI
site 01FCF   ; OUT ($BF),A
site 01FD2   ; OUT ($BF),A
site 01FD4   ; OUTI
site 01FDA   ; OUT ($BF),A
site 01FDD   ; OUT ($BF),A
site 01FDF   ; OUTI
site 01FE5   ; OUT ($BF),A
site 01FE8   ; OUT ($BF),A
site 01FEA   ; OUTI
site 01FF0   ; OUT ($BF),A
site 01FF3   ; OUT ($BF),A
site 01FF5   ; OUTI
site 01FFB   ; OUT ($BF),A
site 01FFE   ; OUT ($BF),A
site 02000   ; OUTI
site 02006   ; OUT ($BF),A
site 02009   ; OUT ($BF),A
site 0200B   ; OUTI
site 022B4   ; OUT ($BF),A
site 022B8   ; OUT ($BF),A
site 022C2   ; OUT (C),A
site 022C7   ; IN D,(C)
site 022D6   ; OUT ($BF),A
site 022DA   ; OUT ($BF),A
site 02309   ; OUT ($BF),A
site 0230D   ; OUT ($BF),A
site 02320   ; OUT (C),E
site 02327   ; OUT (C),D
site 0232C   ; OUT (C),D
site 02332   ; OUT (C),E
site 02337   ; OUT (C),D
site 0233D   ; OUT (C),E
site 02342   ; OUT (C),D
site 0234A   ; OUT ($BF),A
site 0234F   ; OUT ($BF),A
site 02365   ; OUT ($BE),A
site 0236B   ; OUT ($BE),A
site 02371   ; OUT ($BE),A
site 02377   ; OUT ($BE),A
site 0237E   ; OUT ($BF),A
site 02382   ; OUT ($BF),A
site 02388   ; OUT (C),D
site 0238E   ; OUT (C),H
site 02394   ; OUT (C),L
site 0239A   ; OUT (C),A
site 023E0   ; OUT ($BF),A
site 023E4   ; OUT ($BF),A
site 02403   ; OUT ($BF),A
site 02407   ; OUT ($BF),A
site 02450   ; OUT ($BF),A
site 02454   ; OUT ($BF),A
site 0249B   ; OUT ($BF),A
site 0249E   ; OUT ($BF),A
site 024A0   ; OUTI
site 024A6   ; OUT ($BF),A
site 024A9   ; OUT ($BF),A
site 024AB   ; OUTI
site 024B1   ; OUT ($BF),A
site 024B4   ; OUT ($BF),A
site 024B6   ; OUTI
site 024BC   ; OUT ($BF),A
site 024BF   ; OUT ($BF),A
site 024C1   ; OUTI
site 024C7   ; OUT ($BF),A
site 024CA   ; OUT ($BF),A
site 024CC   ; OUTI
site 024D2   ; OUT ($BF),A
site 024D5   ; OUT ($BF),A
site 024D7   ; OUTI
site 024DD   ; OUT ($BF),A
site 024E0   ; OUT ($BF),A
site 024E2   ; OUTI
site 024E8   ; OUT ($BF),A
site 024EB   ; OUT ($BF),A
site 024ED   ; OUTI
site 02501   ; OUT ($BF),A
site 02504   ; OUT ($BF),A
site 02506   ; OUTI
site 0250B   ; OUTI
site 02511   ; OUT ($BF),A
site 02514   ; OUT ($BF),A
site 02516   ; OUTI
site 0251B   ; OUTI
site 02521   ; OUT ($BF),A
site 02524   ; OUT ($BF),A
site 02526   ; OUTI
site 0252B   ; OUTI
site 02531   ; OUT ($BF),A
site 02534   ; OUT ($BF),A
site 02536   ; OUTI
site 0253B   ; OUTI
site 02541   ; OUT ($BF),A
site 02544   ; OUT ($BF),A
site 02546   ; OUTI
site 0254B   ; OUTI
site 02551   ; OUT ($BF),A
site 02554   ; OUT ($BF),A
site 02556   ; OUTI
site 0255B   ; OUTI
site 02561   ; OUT ($BF),A
site 02564   ; OUT ($BF),A
site 02566   ; OUTI
site 0256B   ; OUTI
site 02571   ; OUT ($BF),A
site 02574   ; OUT ($BF),A
site 02576   ; OUTI
site 0257B   ; OUTI
site 02594   ; OUT ($BF),A
site 02598   ; OUT ($BF),A
site 025A4   ; OUT ($BF),A
site 025A8   ; OUT ($BF),A
site 025B2   ; OUT ($BF),A
site 025B6   ; OUT ($BF),A
site 025C6   ; OUT ($BE),A
site 025CC   ; IN A,($BE)
site 025D3   ; OUT ($BE),A
site 02676   ; OUT ($BF),A
site 0267A   ; OUT ($BF),A
site 0267E   ; OUTI
site 02686   ; OUT ($BF),A
site 0268A   ; OUT ($BF),A
site 0268E   ; OUTI
site 02697   ; OUT ($BF),A
site 0269B   ; OUT ($BF),A
site 0269F   ; OUTI
site 026A7   ; OUT ($BF),A
site 026AB   ; OUT ($BF),A
site 026AF   ; OUTI
site 026E2   ; OUT ($BF),A
site 026E6   ; OUT ($BF),A
site 026EF   ; OUT ($BE),A
site 026F4   ; IN E,(C)
site 026FA   ; OUT (C),A
site 02701   ; OUT ($BF),A
site 02705   ; OUT ($BF),A
site 0270A   ; OUT ($BE),A
site 02711   ; OUT ($BE),A
site 02F25   ; OUT ($BF),A
site 02F28   ; OUT ($BF),A
site 0304B   ; OUT ($BF),A
site 0304E   ; OUT ($BF),A
site 031D8   ; OUTI
site 031DA   ; OUTI
site 031DC   ; OUTI
site 031DE   ; OUTI
site 031E0   ; OUTI
site 031E2   ; OUTI
site 031E4   ; OUTI
site 031E6   ; OUTI
site 031E8   ; OUTI
site 031EA   ; OUTI
site 031EC   ; OUTI
site 031EE   ; OUTI
site 031F0   ; OUTI
site 031F2   ; OUTI
site 031F4   ; OUTI
site 031F6   ; OUTI
site 031F8   ; OUTI
site 031FA   ; OUTI
site 031FC   ; OUTI
site 031FE   ; OUTI
site 03200   ; OUTI
site 03202   ; OUTI
site 03204   ; OUTI
site 03206   ; OUTI
site 03208   ; OUTI
site 0320A   ; OUTI
site 0320C   ; OUTI
site 0320E   ; OUTI
site 03210   ; OUTI
site 03212   ; OUTI
site 03214   ; OUTI
site 03216   ; OUTI
site 03218   ; OUTI
site 0321A   ; OUTI
site 0321C   ; OUTI
site 0321E   ; OUTI
site 03220   ; OUTI
site 03222   ; OUTI
site 03224   ; OUTI
site 03226   ; OUTI
site 03228   ; OUTI
site 0322A   ; OUTI
site 0322C   ; OUTI
site 0322E   ; OUTI
site 03230   ; OUTI
site 03232   ; OUTI
site 03234   ; OUTI
site 03236   ; OUTI
site 03238   ; OUTI
site 0323A   ; OUTI
site 0323C   ; OUTI
site 0323E   ; OUTI
site 03240   ; OUTI
site 03242   ; OUTI
site 03244   ; OUTI
site 03246   ; OUTI
site 03248   ; OUTI
site 0324A   ; OUTI
site 0324C   ; OUTI
site 0324E   ; OUTI
site 03250   ; OUTI
site 03252   ; OUTI
site 03254   ; OUTI
site 03256   ; OUTI
site 0325A   ; OUTI
site 0325C   ; OUTI
site 0325E   ; OUTI
site 03260   ; OUTI
site 03262   ; OUTI
site 03264   ; OUTI
site 03266   ; OUTI
site 03268   ; OUTI
site 0326A   ; OUTI
site 0326C   ; OUTI
site 0326E   ; OUTI
site 03270   ; OUTI
site 03272   ; OUTI
site 03274   ; OUTI
site 03276   ; OUTI
site 03278   ; OUTI
site 0327A   ; OUTI
site 0327C   ; OUTI
site 0327E   ; OUTI
site 03280   ; OUTI
site 03282   ; OUTI
site 03284   ; OUTI
site 03286   ; OUTI
site 03288   ; OUTI
site 0328A   ; OUTI
site 0328C   ; OUTI
site 0328E   ; OUTI
site 03290   ; OUTI
site 03293   ; OUT (C),A
site 03296   ; OUT (C),A
site 03299   ; OUT (C),A
site 0329C   ; OUT (C),A
site 032A0   ; OUTI
site 032A2   ; OUTI
site 032A4   ; OUTI
site 032A6   ; OUTI
site 032A8   ; OUTI
site 032AA   ; OUTI
site 032AC   ; OUTI
site 032AE   ; OUTI
site 032B0   ; OUTI
site 032B2   ; OUTI
site 032B4   ; OUTI
site 032B6   ; OUTI
site 032B8   ; OUTI
site 032BA   ; OUTI
site 032BC   ; OUTI
site 032BE   ; OUTI
site 032C0   ; OUTI
site 032C2   ; OUTI
site 032C4   ; OUTI
site 032C6   ; OUTI
site 032C8   ; OUTI
site 032CA   ; OUTI
site 032CC   ; OUTI
site 032CE   ; OUTI
site 032D1   ; OUT (C),A
site 032D4   ; OUT (C),A
site 032D7   ; OUT (C),A
site 032DA   ; OUT (C),A
site 032DD   ; OUT (C),A
site 032E0   ; OUT (C),A
site 032E3   ; OUT (C),A
site 032E6   ; OUT (C),A
site 032EA   ; OUTI
site 032EC   ; OUTI
site 032EE   ; OUTI
site 032F0   ; OUTI
site 032F2   ; OUTI
site 032F4   ; OUTI
site 032F6   ; OUTI
site 032F8   ; OUTI
site 032FA   ; OUTI
site 032FC   ; OUTI
site 032FE   ; OUTI
site 03300   ; OUTI
site 03302   ; OUTI
site 03304   ; OUTI
site 03306   ; OUTI
site 03308   ; OUTI
site 0330A   ; OUTI
site 0330C   ; OUTI
site 0330E   ; OUTI
site 03310   ; OUTI
site 03313   ; OUT (C),A
site 03316   ; OUT (C),A
site 03319   ; OUT (C),A
site 0331C   ; OUT (C),A
site 0331F   ; OUT (C),A
site 03322   ; OUT (C),A
site 03325   ; OUT (C),A
site 03328   ; OUT (C),A
site 0332B   ; OUT (C),A
site 0332E   ; OUT (C),A
site 03331   ; OUT (C),A
site 03334   ; OUT (C),A
site 03338   ; OUTI
site 0333A   ; OUTI
site 0333C   ; OUTI
site 0333E   ; OUTI
site 03340   ; OUTI
site 03342   ; OUTI
site 03344   ; OUTI
site 03346   ; OUTI
site 03348   ; OUTI
site 0334A   ; OUTI
site 0334C   ; OUTI
site 0334E   ; OUTI
site 03350   ; OUTI
site 03352   ; OUTI
site 03354   ; OUTI
site 03356   ; OUTI
site 03359   ; OUT (C),A
site 0335C   ; OUT (C),A
site 0335F   ; OUT (C),A
site 03362   ; OUT (C),A
site 03365   ; OUT (C),A
site 03368   ; OUT (C),A
site 0336B   ; OUT (C),A
site 0336E   ; OUT (C),A
site 03371   ; OUT (C),A
site 03374   ; OUT (C),A
site 03377   ; OUT (C),A
site 0337A   ; OUT (C),A
site 0337D   ; OUT (C),A
site 03380   ; OUT (C),A
site 03383   ; OUT (C),A
site 03386   ; OUT (C),A
site 0338A   ; OUTI
site 0338C   ; OUTI
site 0338E   ; OUTI
site 03390   ; OUTI
site 03392   ; OUTI
site 03394   ; OUTI
site 03396   ; OUTI
site 03398   ; OUTI
site 0339A   ; OUTI
site 0339C   ; OUTI
site 0339E   ; OUTI
site 033A0   ; OUTI
site 033A3   ; OUT (C),A
site 033A6   ; OUT (C),A
site 033A9   ; OUT (C),A
site 033AC   ; OUT (C),A
site 033AF   ; OUT (C),A
site 033B2   ; OUT (C),A
site 033B5   ; OUT (C),A
site 033B8   ; OUT (C),A
site 033BB   ; OUT (C),A
site 033BE   ; OUT (C),A
site 033C1   ; OUT (C),A
site 033C4   ; OUT (C),A
site 033C7   ; OUT (C),A
site 033CA   ; OUT (C),A
site 033CD   ; OUT (C),A
site 033D0   ; OUT (C),A
site 033D3   ; OUT (C),A
site 033D6   ; OUT (C),A
site 033D9   ; OUT (C),A
site 033DC   ; OUT (C),A
site 033E0   ; OUTI
site 033E2   ; OUTI
site 033E4   ; OUTI
site 033E6   ; OUTI
site 033E8   ; OUTI
site 033EA   ; OUTI
site 033EC   ; OUTI
site 033EE   ; OUTI
site 033F1   ; OUT (C),A
site 033F4   ; OUT (C),A
site 033F7   ; OUT (C),A
site 033FA   ; OUT (C),A
site 033FD   ; OUT (C),A
site 03400   ; OUT (C),A
site 03403   ; OUT (C),A
site 03406   ; OUT (C),A
site 03409   ; OUT (C),A
site 0340C   ; OUT (C),A
site 0340F   ; OUT (C),A
site 03412   ; OUT (C),A
site 03415   ; OUT (C),A
site 03418   ; OUT (C),A
site 0341B   ; OUT (C),A
site 0341E   ; OUT (C),A
site 03421   ; OUT (C),A
site 03424   ; OUT (C),A
site 03427   ; OUT (C),A
site 0342A   ; OUT (C),A
site 0342D   ; OUT (C),A
site 03430   ; OUT (C),A
site 03433   ; OUT (C),A
site 03436   ; OUT (C),A
site 0343A   ; OUTI
site 0343C   ; OUTI
site 0343E   ; OUTI
site 03440   ; OUTI
site 03443   ; OUT (C),A
site 03446   ; OUT (C),A
site 03449   ; OUT (C),A
site 0344C   ; OUT (C),A
site 0344F   ; OUT (C),A
site 03452   ; OUT (C),A
site 03455   ; OUT (C),A
site 03458   ; OUT (C),A
site 0345B   ; OUT (C),A
site 0345E   ; OUT (C),A
site 03461   ; OUT (C),A
site 03464   ; OUT (C),A
site 03467   ; OUT (C),A
site 0346A   ; OUT (C),A
site 0346D   ; OUT (C),A
site 03470   ; OUT (C),A
site 03473   ; OUT (C),A
site 03476   ; OUT (C),A
site 03479   ; OUT (C),A
site 0347C   ; OUT (C),A
site 0347F   ; OUT (C),A
site 03482   ; OUT (C),A
site 03485   ; OUT (C),A
site 03488   ; OUT (C),A
site 0348B   ; OUT (C),A
site 0348E   ; OUT (C),A
site 03491   ; OUT (C),A
site 03494   ; OUT (C),A
site 03499   ; OUT (C),A
site 0349C   ; OUT (C),A
site 0349F   ; OUT (C),A
site 034A2   ; OUT (C),A
site 034A5   ; OUT (C),A
site 034A8   ; OUT (C),A
site 034AB   ; OUT (C),A
site 034AE   ; OUT (C),A
site 034B1   ; OUT (C),A
site 034B4   ; OUT (C),A
site 034B7   ; OUT (C),A
site 034BA   ; OUT (C),A
site 034BD   ; OUT (C),A
site 034C0   ; OUT (C),A
site 034C3   ; OUT (C),A
site 034C6   ; OUT (C),A
site 034C9   ; OUT (C),A
site 034CC   ; OUT (C),A
site 034CF   ; OUT (C),A
site 034D2   ; OUT (C),A
site 034D5   ; OUT (C),A
site 034D8   ; OUT (C),A
site 034DB   ; OUT (C),A
site 034DE   ; OUT (C),A
site 034E1   ; OUT (C),A
site 034E4   ; OUT (C),A
site 034E7   ; OUT (C),A
site 034EA   ; OUT (C),A
site 034ED   ; OUT (C),A
site 034F0   ; OUT (C),A
site 034F3   ; OUT (C),A
site 034F6   ; OUT (C),A
site 03519   ; OUTI
site 0351B   ; OUTI
site 0351E   ; OUT (C),A
site 03521   ; OUTI
site 03523   ; OUTI
site 03525   ; OUTI
site 03527   ; OUT (C),A
site 0352A   ; OUTI
site 0352C   ; OUTI
site 0352E   ; OUTI
site 03530   ; OUT (C),A
site 03533   ; OUTI
site 03535   ; OUTI
site 03537   ; OUTI
site 03539   ; OUT (C),A
site 0353C   ; OUTI
site 0353E   ; OUTI
site 03540   ; OUTI
site 03542   ; OUT (C),A
site 03545   ; OUTI
site 03547   ; OUTI
site 03549   ; OUTI
site 0354B   ; OUT (C),A
site 0354E   ; OUTI
site 03550   ; OUTI
site 03552   ; OUTI
site 03554   ; OUT (C),A
site 03557   ; OUTI
site 03559   ; OUTI
site 0355B   ; OUTI
site 0355D   ; OUT (C),A
site 03560   ; OUTI
site 03562   ; OUTI
site 03564   ; OUTI
site 03566   ; OUT (C),A
site 03569   ; OUTI
site 0356B   ; OUTI
site 0356D   ; OUTI
site 0356F   ; OUT (C),A
site 03572   ; OUTI
site 03574   ; OUTI
site 03576   ; OUTI
site 03578   ; OUT (C),A
site 0357B   ; OUTI
site 0357D   ; OUTI
site 0357F   ; OUTI
site 03581   ; OUT (C),A
site 03584   ; OUTI
site 03586   ; OUTI
site 03588   ; OUTI
site 0358A   ; OUT (C),A
site 0358D   ; OUTI
site 0358F   ; OUTI
site 03591   ; OUTI
site 03593   ; OUT (C),A
site 03596   ; OUTI
site 03598   ; OUTI
site 0359A   ; OUTI
site 0359C   ; OUT (C),A
site 0359F   ; OUTI
site 035A1   ; OUTI
site 035A3   ; OUTI
site 035A5   ; OUT (C),A
site 035A8   ; OUTI
site 035AC   ; OUTI
site 035AE   ; OUTI
site 035B0   ; OUT (C),A
site 035B3   ; OUTI
site 035B5   ; OUTI
site 035B7   ; OUTI
site 035B9   ; OUT (C),A
site 035BC   ; OUTI
site 035BE   ; OUTI
site 035C0   ; OUTI
site 035C2   ; OUT (C),A
site 035C5   ; OUTI
site 035C7   ; OUTI
site 035C9   ; OUTI
site 035CB   ; OUT (C),A
site 035CE   ; OUTI
site 035D0   ; OUTI
site 035D2   ; OUTI
site 035D4   ; OUT (C),A
site 035D7   ; OUTI
site 035D9   ; OUTI
site 035DB   ; OUTI
site 035DD   ; OUT (C),A
site 035E0   ; OUTI
site 035E2   ; OUTI
site 035E4   ; OUTI
site 035E6   ; OUT (C),A
site 035E9   ; OUTI
site 035EC   ; OUT (C),A
site 035EF   ; OUT (C),A
site 035F2   ; OUT (C),A
site 035F5   ; OUT (C),A
site 035F9   ; OUTI
site 035FB   ; OUTI
site 035FD   ; OUT (C),A
site 03600   ; OUTI
site 03602   ; OUTI
site 03604   ; OUTI
site 03606   ; OUT (C),A
site 03609   ; OUTI
site 0360B   ; OUTI
site 0360D   ; OUTI
site 0360F   ; OUT (C),A
site 03612   ; OUTI
site 03614   ; OUTI
site 03616   ; OUTI
site 03618   ; OUT (C),A
site 0361B   ; OUTI
site 0361D   ; OUTI
site 0361F   ; OUTI
site 03621   ; OUT (C),A
site 03624   ; OUTI
site 03626   ; OUTI
site 03628   ; OUTI
site 0362A   ; OUT (C),A
site 0362D   ; OUTI
site 03630   ; OUT (C),A
site 03633   ; OUT (C),A
site 03636   ; OUT (C),A
site 03639   ; OUT (C),A
site 0363C   ; OUT (C),A
site 0363F   ; OUT (C),A
site 03642   ; OUT (C),A
site 03645   ; OUT (C),A
site 03649   ; OUTI
site 0364B   ; OUTI
site 0364D   ; OUT (C),A
site 03650   ; OUTI
site 03652   ; OUTI
site 03654   ; OUTI
site 03656   ; OUT (C),A
site 03659   ; OUTI
site 0365B   ; OUTI
site 0365D   ; OUTI
site 0365F   ; OUT (C),A
site 03662   ; OUTI
site 03664   ; OUTI
site 03666   ; OUTI
site 03668   ; OUT (C),A
site 0366B   ; OUTI
site 0366D   ; OUTI
site 0366F   ; OUTI
site 03671   ; OUT (C),A
site 03674   ; OUTI
site 03677   ; OUT (C),A
site 0367A   ; OUT (C),A
site 0367D   ; OUT (C),A
site 03680   ; OUT (C),A
site 03683   ; OUT (C),A
site 03686   ; OUT (C),A
site 03689   ; OUT (C),A
site 0368C   ; OUT (C),A
site 0368F   ; OUT (C),A
site 03692   ; OUT (C),A
site 03695   ; OUT (C),A
site 03698   ; OUT (C),A
site 0369C   ; OUTI
site 0369E   ; OUTI
site 036A0   ; OUT (C),A
site 036A3   ; OUTI
site 036A5   ; OUTI
site 036A7   ; OUTI
site 036A9   ; OUT (C),A
site 036AC   ; OUTI
site 036AE   ; OUTI
site 036B0   ; OUTI
site 036B2   ; OUT (C),A
site 036B5   ; OUTI
site 036B7   ; OUTI
site 036B9   ; OUTI
site 036BB   ; OUT (C),A
site 036BE   ; OUTI
site 036C1   ; OUT (C),A
site 036C4   ; OUT (C),A
site 036C7   ; OUT (C),A
site 036CA   ; OUT (C),A
site 036CD   ; OUT (C),A
site 036D0   ; OUT (C),A
site 036D3   ; OUT (C),A
site 036D6   ; OUT (C),A
site 036D9   ; OUT (C),A
site 036DC   ; OUT (C),A
site 036DF   ; OUT (C),A
site 036E2   ; OUT (C),A
site 036E5   ; OUT (C),A
site 036E8   ; OUT (C),A
site 036EB   ; OUT (C),A
site 036EE   ; OUT (C),A
site 036F2   ; OUTI
site 036F4   ; OUTI
site 036F6   ; OUT (C),A
site 036F9   ; OUTI
site 036FB   ; OUTI
site 036FD   ; OUTI
site 036FF   ; OUT (C),A
site 03702   ; OUTI
site 03704   ; OUTI
site 03706   ; OUTI
site 03708   ; OUT (C),A
site 0370B   ; OUTI
site 0370E   ; OUT (C),A
site 03711   ; OUT (C),A
site 03714   ; OUT (C),A
site 03717   ; OUT (C),A
site 0371A   ; OUT (C),A
site 0371D   ; OUT (C),A
site 03720   ; OUT (C),A
site 03723   ; OUT (C),A
site 03726   ; OUT (C),A
site 03729   ; OUT (C),A
site 0372C   ; OUT (C),A
site 0372F   ; OUT (C),A
site 03732   ; OUT (C),A
site 03735   ; OUT (C),A
site 03738   ; OUT (C),A
site 0373B   ; OUT (C),A
site 0373E   ; OUT (C),A
site 03741   ; OUT (C),A
site 03744   ; OUT (C),A
site 03747   ; OUT (C),A
site 0374B   ; OUTI
site 0374D   ; OUTI
site 0374F   ; OUT (C),A
site 03752   ; OUTI
site 03754   ; OUTI
site 03756   ; OUTI
site 03758   ; OUT (C),A
site 0375B   ; OUTI
site 0375E   ; OUT (C),A
site 03761   ; OUT (C),A
site 03764   ; OUT (C),A
site 03767   ; OUT (C),A
site 0376A   ; OUT (C),A
site 0376D   ; OUT (C),A
site 03770   ; OUT (C),A
site 03773   ; OUT (C),A
site 03776   ; OUT (C),A
site 03779   ; OUT (C),A
site 0377C   ; OUT (C),A
site 0377F   ; OUT (C),A
site 03782   ; OUT (C),A
site 03785   ; OUT (C),A
site 03788   ; OUT (C),A
site 0378B   ; OUT (C),A
site 0378E   ; OUT (C),A
site 03791   ; OUT (C),A
site 03794   ; OUT (C),A
site 03797   ; OUT (C),A
site 0379A   ; OUT (C),A
site 0379D   ; OUT (C),A
site 037A0   ; OUT (C),A
site 037A3   ; OUT (C),A
site 037A7   ; OUTI
site 037A9   ; OUTI
site 037AB   ; OUT (C),A
site 037AE   ; OUTI
site 037B1   ; OUT (C),A
site 037B4   ; OUT (C),A
site 037B7   ; OUT (C),A
site 037BA   ; OUT (C),A
site 037BD   ; OUT (C),A
site 037C0   ; OUT (C),A
site 037C3   ; OUT (C),A
site 037C6   ; OUT (C),A
site 037C9   ; OUT (C),A
site 037CC   ; OUT (C),A
site 037CF   ; OUT (C),A
site 037D2   ; OUT (C),A
site 037D5   ; OUT (C),A
site 037D8   ; OUT (C),A
site 037DB   ; OUT (C),A
site 037DE   ; OUT (C),A
site 037E1   ; OUT (C),A
site 037E4   ; OUT (C),A
site 037E7   ; OUT (C),A
site 037EA   ; OUT (C),A
site 037ED   ; OUT (C),A
site 037F0   ; OUT (C),A
site 037F3   ; OUT (C),A
site 037F6   ; OUT (C),A
site 037F9   ; OUT (C),A
site 037FC   ; OUT (C),A
site 037FF   ; OUT (C),A
site 03802   ; OUT (C),A
site 03807   ; OUT (C),A
site 0380A   ; OUT (C),A
site 0380D   ; OUT (C),A
site 03810   ; OUT (C),A
site 03813   ; OUT (C),A
site 03816   ; OUT (C),A
site 03819   ; OUT (C),A
site 0381C   ; OUT (C),A
site 0381F   ; OUT (C),A
site 03822   ; OUT (C),A
site 03825   ; OUT (C),A
site 03828   ; OUT (C),A
site 0382B   ; OUT (C),A
site 0382E   ; OUT (C),A
site 03831   ; OUT (C),A
site 03834   ; OUT (C),A
site 03837   ; OUT (C),A
site 0383A   ; OUT (C),A
site 0383D   ; OUT (C),A
site 03840   ; OUT (C),A
site 03843   ; OUT (C),A
site 03846   ; OUT (C),A
site 03849   ; OUT (C),A
site 0384C   ; OUT (C),A
site 0384F   ; OUT (C),A
site 03852   ; OUT (C),A
site 03855   ; OUT (C),A
site 03858   ; OUT (C),A
site 0385B   ; OUT (C),A
site 0385E   ; OUT (C),A
site 03861   ; OUT (C),A
site 03864   ; OUT (C),A
site 05BB9   ; IN A,($BF)
site 05CCA   ; OUT ($BF),A
site 05CCE   ; OUT ($BF),A
site 05CD1   ; OUT ($BF),A
site 05CD5   ; OUT ($BF),A
site 05CFA   ; OUT ($BF),A
site 05CFE   ; OUT ($BF),A
site 05D17   ; OUT ($BF),A
site 05D1B   ; OUT ($BF),A
site 05D24   ; OUT ($BF),A
site 05D28   ; OUT ($BF),A
site 05EA4   ; IN A,($BF)
site 05F13   ; OUT ($BE),A
site 05F1A   ; OUT ($BE),A
site 05F21   ; OUT ($BE),A
site 05F27   ; OUT ($BE),A
site 06152   ; IN A,($BF)
site 062DF   ; OUT ($BE),A
site 06572   ; IN A,($BF)
site 066FC   ; IN A,($BF)
site 069EA   ; IN A,($BF)
site 06B73   ; OUT ($BE),A
site 06B7A   ; OUT ($BE),A
site 06B81   ; OUT ($BE),A
site 06B87   ; OUT ($BE),A
site 06C50   ; IN A,($BF)
site 06EA0   ; OUT ($BE),A
site 06EA7   ; OUT ($BE),A
site 06F33   ; OUT ($BF),A
site 06F37   ; OUT ($BF),A
site 06F42   ; OUT ($BE),A
site 06F51   ; OUT ($BE),A
site 073AC   ; IN A,($BF)
site 0751B   ; OUT ($BE),A
site 0758A   ; OUT ($BE),A
site 07594   ; OUT ($BE),A
site 0759B   ; OUT ($BE),A
site 075A5   ; OUT ($BE),A
site 075AC   ; OUT ($BE),A
site 07905   ; IN A,($BF)
site 07A10   ; OUT ($BE),A
site 07A2B   ; OUTI
site 07A68   ; OUT ($BE),A
site 07A6E   ; OUT ($BE),A
site 07AA8   ; OUT ($BE),A
site 07AAF   ; OUT ($BE),A
site 07AB4   ; OUT ($BE),A
site 07ABB   ; OUT ($BE),A
site 07B46   ; IN A,($BF)
site 07BCE   ; IN A,($BF)
site 07C26   ; IN A,($BF)
site 47F85   ; OUT ($BE),A
site 47F8C   ; OUT ($BE),A
site 47F93   ; OUT ($BE),A
site 47F9A   ; OUT ($BE),A
site 7DBED   ; OUT ($7F),A
site 7DBF1   ; OUT ($7F),A
site 7DBFE   ; OUT ($7F),A
site 7DC02   ; OUT ($7F),A
site 7DC33   ; OUT ($7F),A
site 7DC4A   ; OUT ($7F),A
site 7DC5E   ; OUT ($7F),A
site 7DC6D   ; OUT ($7F),A
site 7DC84   ; OUT ($7F),A
site 7DC98   ; OUT ($7F),A
site 7DCC5   ; OUT ($7F),A
site 7DCD8   ; OUT ($7F),A
site 7DCEF   ; OUT ($7F),A
site 7DCF5   ; OUT ($7F),A
site 7DD19   ; OUT ($7F),A
site 7DD30   ; OUT ($7F),A
site 7DD51   ; OUT ($7F),A
site 7DDA3   ; OUT ($7F),A
site 7DF91   ; OUT ($7F),A
site 7DF96   ; OUT ($7F),A
site 7DFAA   ; OUT ($7F),A
site 7DFBD   ; OUT ($7F),A
site 7DFC9   ; OUT ($7F),A
site 7DFDC   ; OUT ($7F),A
site 7E351   ; OUT ($BF),A
site 7E354   ; OUT ($BF),A
site 7E356   ; OUTI
site 7E358   ; IN A,(C)
site 7E35B   ; OUTI
site 7E35D   ; IN A,(C)
site 7E360   ; OUTI
site 7E362   ; IN A,(C)
site 7E365   ; OUTI
site 7E367   ; IN A,(C)
site 7E36A   ; OUTI
site 7E36C   ; IN A,(C)
site 7E36F   ; OUTI
site 7E371   ; IN A,(C)
site 7E374   ; OUTI
site 7E376   ; IN A,(C)
site 7E379   ; OUTI
site 7E37B   ; IN A,(C)
site 7E37E   ; OUTI
site 7E380   ; IN A,(C)
site 7E383   ; OUTI
site 7E385   ; IN A,(C)
site 7E388   ; OUTI
site 7E38A   ; IN A,(C)
site 7E38D   ; OUTI
site 7E38F   ; IN A,(C)
site 7E392   ; OUTI
site 7E394   ; IN A,(C)
site 7E397   ; OUTI
site 7E399   ; IN A,(C)
site 7E39C   ; OUTI
site 7E39E   ; IN A,(C)
site 7E3A1   ; OUTI
site 7E3A3   ; IN A,(C)
site 7E3A6   ; OUTI
site 7E3A8   ; IN A,(C)
site 7E3AB   ; OUTI
site 7E3AD   ; IN A,(C)
site 7E3B0   ; OUTI
site 7E3B2   ; IN A,(C)
site 7E3B5   ; OUTI
site 7E3B7   ; IN A,(C)
site 7E3BA   ; OUTI
site 7E3BC   ; IN A,(C)
site 7E3BF   ; OUTI
site 7E3C1   ; IN A,(C)
site 7E3C4   ; OUTI
site 7E3C6   ; IN A,(C)
site 7E3EC   ; OUT ($BF),A
site 7E3F0   ; OUT ($BF),A
site 7E40D   ; OUT (C),A
site 7E412   ; OUT ($BF),A
site 7E416   ; OUT ($BF),A
site 7E46B   ; OUTI
site 7E46E   ; OUTI
site 7E471   ; OUTI
site 7E474   ; OUTI
site 7E477   ; OUTI
site 7E47A   ; OUTI
site 7E47D   ; OUTI
site 7E480   ; OUTI
site 7E483   ; OUTI
site 7E486   ; OUTI
site 7E489   ; OUTI
site 7E48C   ; OUTI
site 7E48F   ; OUTI
site 7E492   ; OUTI
site 7E495   ; OUTI
site 7E498   ; OUTI
site 7E4CD   ; OUT (C),A
site 7E4D0   ; OUT (C),A
site 7E4D4   ; OUT (C),A
site 7E4D7   ; OUT (C),A
site 7E4DB   ; OUT (C),A
site 7E4DE   ; OUT (C),A
site 7E4E2   ; OUT (C),A
site 7E4E5   ; OUT (C),A
site 7E4E9   ; OUT (C),A
site 7E4EC   ; OUT (C),A
site 7E4F0   ; OUT (C),A
site 7E4F3   ; OUT (C),A
site 7E4F7   ; OUT (C),A
site 7E4FA   ; OUT (C),A
site 7E4FE   ; OUT (C),A
site 7E501   ; OUT (C),A
site 7E509   ; OUTI
site 7E50B   ; OUT (C),L
site 7E50E   ; OUTI
site 7E510   ; OUT (C),L
site 7E513   ; OUTI
site 7E515   ; OUT (C),L
site 7E518   ; OUTI
site 7E51A   ; OUT (C),L
site 7E51D   ; OUTI
site 7E51F   ; OUT (C),L
site 7E522   ; OUTI
site 7E524   ; OUT (C),L
site 7E527   ; OUTI
site 7E529   ; OUT (C),L
site 7E52C   ; OUTI
site 7E52E   ; OUT (C),L
site 7E531   ; OUTI
site 7E533   ; OUT (C),L
site 7E536   ; OUTI
site 7E538   ; OUT (C),L
site 7E53B   ; OUTI
site 7E53D   ; OUT (C),L
site 7E540   ; OUTI
site 7E542   ; OUT (C),L
site 7E545   ; OUTI
site 7E547   ; OUT (C),L
site 7E54A   ; OUTI
site 7E54C   ; OUT (C),L
site 7E54F   ; OUTI
site 7E551   ; OUT (C),L
site 7E554   ; OUTI
site 7E556   ; OUT (C),L
site 7E591   ; OUT (C),A
site 7E594   ; OUT (C),L
site 7E597   ; OUT (C),A
site 7E59A   ; OUT (C),L
site 7E59E   ; OUT (C),A
site 7E5A1   ; OUT (C),L
site 7E5A4   ; OUT (C),A
site 7E5A7   ; OUT (C),L
site 7E5AB   ; OUT (C),A
site 7E5AE   ; OUT (C),L
site 7E5B1   ; OUT (C),A
site 7E5B4   ; OUT (C),L
site 7E5B8   ; OUT (C),A
site 7E5BB   ; OUT (C),L
site 7E5BE   ; OUT (C),A
site 7E5C1   ; OUT (C),L
site 7E5C5   ; OUT (C),A
site 7E5C8   ; OUT (C),L
site 7E5CB   ; OUT (C),A
site 7E5CE   ; OUT (C),L
site 7E5D2   ; OUT (C),A
site 7E5D5   ; OUT (C),L
site 7E5D8   ; OUT (C),A
site 7E5DB   ; OUT (C),L
site 7E5DF   ; OUT (C),A
site 7E5E2   ; OUT (C),L
site 7E5E5   ; OUT (C),A
site 7E5E8   ; OUT (C),L
site 7E5EC   ; OUT (C),A
site 7E5EF   ; OUT (C),L
site 7E5F2   ; OUT (C),A
site 7E5F5   ; OUT (C),L
site 7F9A5   ; OUT ($BF),A
site 7F9A8   ; OUT ($BF),A
site 7F9AA   ; OUTI
site 7F9B0   ; OUT ($BF),A
site 7F9B3   ; OUT ($BF),A
site 7F9B5   ; OUTI
site 7F9BB   ; OUT ($BF),A
site 7F9BE   ; OUT ($BF),A
site 7F9C0   ; OUTI
site 7F9C6   ; OUT ($BF),A
site 7F9C9   ; OUT ($BF),A
site 7F9CB   ; OUTI
site 7F9D1   ; OUT ($BF),A
site 7F9D4   ; OUT ($BF),A
site 7F9D6   ; OUTI
site 7F9DC   ; OUT ($BF),A
site 7F9DF   ; OUT ($BF),A
site 7F9E1   ; OUTI
site 7F9E7   ; OUT ($BF),A
site 7F9EA   ; OUT ($BF),A
site 7F9EC   ; OUTI
site 7F9F2   ; OUT ($BF),A
site 7F9F5   ; OUT ($BF),A
site 7F9F7   ; OUTI
site 7FA37   ; OUT ($BF),A
site 7FA3A   ; OUT ($BF),A
site 7FA3C   ; OUTI
site 7FA42   ; OUTI
site 7FA56   ; OUT ($BF),A
site 7FA59   ; OUT ($BF),A
site 7FA5B   ; OUTI
site 7FA61   ; OUTI
site 7FA72   ; OUT ($BF),A
site 7FA75   ; OUT ($BF),A
site 7FA77   ; OUTI
site 7FA7D   ; OUTI
site 7FA96   ; OUT ($BF),A
site 7FA99   ; OUT ($BF),A
site 7FA9B   ; OUTI
site 7FAA1   ; OUTI
site 7FAA8   ; OUT ($BF),A
site 7FAAB   ; OUT ($BF),A
site 7FAAE   ; OUT ($BE),A
site 7FAB6   ; OUT ($BE),A
site 7FAC7   ; OUT ($BF),A
site 7FACA   ; OUT ($BF),A
site 7FACC   ; OUTI
site 7FAD2   ; OUTI
site 7FAD9   ; OUT ($BF),A
site 7FADC   ; OUT ($BF),A
site 7FADF   ; OUT ($BE),A
site 7FAE7   ; OUT ($BE),A
mapst 000E7   ; LD ($FFFC),A
mapst 00106   ; LD ($FFFC),A
# CHECK mapper at 001B2 ($01B2 bank 0): 77  LD (HL),A $FFFF<-unknown
mapst 001FD   ; LD ($FFFC),A
mapst 00219   ; LD ($FFFC),A
mapst 00222   ; LD ($FFFC),A
mapst 0023B   ; LD ($FFFC),A
mapst 0029A   ; LD ($FFFC),A
mapst 002B4   ; LD ($FFFC),A
mapst 002BE   ; LD ($FFFC),A
mapst 002D8   ; LD ($FFFC),A
mapst 00302   ; LD ($FFFC),A
mapst 00305   ; LD ($FFFD),A
mapst 00309   ; LD ($FFFE),A
mapst 0030D   ; LD ($FFFF),A
mapst 00473   ; LD ($FFFF),A
mapst 00483   ; LD ($FFFF),A
mapst 0065F   ; LD ($FFFF),A
mapst 0098B   ; LD ($FFFF),A
mapst 00AAF   ; LD ($FFFF),A
mapst 00AC8   ; LD ($FFFF),A
mapst 00ADB   ; LD ($FFFF),A
mapst 00AF4   ; LD ($FFFF),A
mapst 00B07   ; LD ($FFFF),A
mapst 00B50   ; LD ($FFFF),A
mapst 00B6A   ; LD ($FFFF),A
mapst 00C14   ; LD ($FFFF),A
mapst 00EF2   ; LD ($FFFF),A
mapst 00F43   ; LD ($FFFF),A
mapst 00FEF   ; LD ($FFFF),A
mapst 01029   ; LD ($FFFF),A
mapst 01099   ; LD ($FFFF),A
mapst 0115F   ; LD ($FFFF),A
mapst 01190   ; LD ($FFFF),A
mapst 012A2   ; LD ($FFFF),A
mapst 012D4   ; LD ($FFFF),A
mapst 01650   ; LD ($FFFF),A
mapst 01B0C   ; LD ($FFFF),A
mapst 01B44   ; LD ($FFFF),A
mapst 01BC2   ; LD ($FFFF),A
mapst 01BDC   ; LD ($FFFF),A
mapst 01C58   ; LD ($FFFF),A
mapst 01CAA   ; LD ($FFFF),A
mapst 01CEB   ; LD ($FFFF),A
mapst 01E05   ; LD ($FFFF),A
mapst 01E19   ; LD ($FFFF),A
mapst 01EA4   ; LD ($FFFF),A
mapst 01EAD   ; LD ($FFFF),A
mapst 01EC8   ; LD ($FFFF),A
mapst 01ED1   ; LD ($FFFF),A
mapst 0209F   ; LD ($FFFF),A
mapst 02189   ; LD ($FFFF),A
mapst 02197   ; LD ($FFFF),A
mapst 021A5   ; LD ($FFFF),A
mapst 021B3   ; LD ($FFFF),A
mapst 022A0   ; LD ($FFFF),A
mapst 022CE   ; LD ($FFFF),A
mapst 0240B   ; LD ($FFFF),A
mapst 0246F   ; LD ($FFFF),A
mapst 02619   ; LD ($FFFF),A
mapst 02641   ; LD ($FFFF),A
mapst 02661   ; LD ($FFFF),A
mapst 026BF   ; LD ($FFFF),A
mapst 02715   ; LD ($FFFF),A
mapst 0273B   ; LD ($FFFF),A
mapst 02767   ; LD ($FFFF),A
mapst 02795   ; LD ($FFFF),A
mapst 0282E   ; LD ($FFFF),A
mapst 028DE   ; LD ($FFFF),A
mapst 02913   ; LD ($FFFF),A
mapst 0292F   ; LD ($FFFF),A
mapst 02949   ; LD ($FFFF),A
mapst 02965   ; LD ($FFFF),A
mapst 02A6F   ; LD ($FFFF),A
mapst 02AC1   ; LD ($FFFF),A
mapst 02B08   ; LD ($FFFF),A
mapst 02F40   ; LD ($FFFF),A
mapst 02FA8   ; LD ($FFFF),A
mapst 03060   ; LD ($FFFF),A
mapst 030A2   ; LD ($FFFF),A
mapst 03137   ; LD ($FFFF),A
mapst 03151   ; LD ($FFFF),A
mapst 0386D   ; LD ($FFFF),A
mapst 038D6   ; LD ($FFFF),A
mapst 038F6   ; LD ($FFFF),A
mapst 040F6   ; LD ($FFFF),A
mapst 042BC   ; LD ($FFFF),A
mapst 0451F   ; LD ($FFFF),A
mapst 04533   ; LD ($FFFF),A
mapst 04559   ; LD ($FFFF),A
mapst 0460D   ; LD ($FFFF),A
mapst 04F87   ; LD ($FFFF),A
mapst 0525B   ; LD ($FFFF),A
mapst 05568   ; LD ($FFFF),A
mapst 05B7C   ; LD ($FFFF),A
mapst 05B8A   ; LD ($FFFF),A
mapst 05CE3   ; LD ($FFFF),A
mapst 05D4C   ; LD ($FFFF),A
mapst 05D5A   ; LD ($FFFF),A
mapst 05D68   ; LD ($FFFF),A
mapst 05D76   ; LD ($FFFF),A
mapst 05D84   ; LD ($FFFF),A
mapst 05D92   ; LD ($FFFF),A
mapst 05DB2   ; LD ($FFFF),A
mapst 05DC0   ; LD ($FFFF),A
mapst 05E0B   ; LD ($FFFF),A
mapst 05E1E   ; LD ($FFFF),A
mapst 05E3C   ; LD ($FFFF),A
mapst 05F6D   ; LD ($FFFF),A
mapst 0603C   ; LD ($FFFF),A
mapst 06064   ; LD ($FFFF),A
mapst 06078   ; LD ($FFFF),A
mapst 06086   ; LD ($FFFF),A
mapst 06094   ; LD ($FFFF),A
mapst 06265   ; LD ($FFFF),A
mapst 06292   ; LD ($FFFF),A
mapst 06335   ; LD ($FFFF),A
mapst 06346   ; LD ($FFFF),A
mapst 0635A   ; LD ($FFFF),A
mapst 06377   ; LD ($FFFF),A
mapst 063AB   ; LD ($FFFF),A
mapst 063BF   ; LD ($FFFF),A
mapst 063E7   ; LD ($FFFF),A
mapst 064A2   ; LD ($FFFF),A
mapst 06518   ; LD ($FFFF),A
mapst 065B9   ; LD ($FFFF),A
mapst 06642   ; LD ($FFFF),A
mapst 06650   ; LD ($FFFF),A
mapst 06664   ; LD ($FFFF),A
mapst 06672   ; LD ($FFFF),A
mapst 06683   ; LD ($FFFF),A
mapst 066AF   ; LD ($FFFF),A
mapst 06722   ; LD ($FFFF),A
mapst 06880   ; LD ($FFFF),A
mapst 0693E   ; LD ($FFFF),A
mapst 0694C   ; LD ($FFFF),A
mapst 0695A   ; LD ($FFFF),A
mapst 0696B   ; LD ($FFFF),A
mapst 069F8   ; LD ($FFFF),A
mapst 06AD2   ; LD ($FFFF),A
mapst 06AE6   ; LD ($FFFF),A
mapst 06B30   ; LD ($FFFF),A
mapst 06BD2   ; LD ($FFFF),A
mapst 06BE0   ; LD ($FFFF),A
mapst 06BFA   ; LD ($FFFF),A
mapst 06D09   ; LD ($FFFF),A
mapst 06ECC   ; LD ($FFFF),A
mapst 06EFA   ; LD ($FFFF),A
mapst 06F0A   ; LD ($FFFF),A
mapst 07294   ; LD ($FFFF),A
mapst 072A2   ; LD ($FFFF),A
mapst 072B0   ; LD ($FFFF),A
mapst 072BE   ; LD ($FFFF),A
mapst 072CC   ; LD ($FFFF),A
mapst 072DD   ; LD ($FFFF),A
mapst 072EB   ; LD ($FFFF),A
mapst 0733F   ; LD ($FFFF),A
mapst 073EF   ; LD ($FFFF),A
mapst 0752E   ; LD ($FFFF),A
mapst 07537   ; LD ($FFFF),A
mapst 07573   ; LD ($FFFF),A
mapst 075B1   ; LD ($FFFF),A
mapst 07677   ; LD ($FFFF),A
mapst 0770E   ; LD ($FFFF),A
mapst 07732   ; LD ($FFFF),A
mapst 0776A   ; LD ($FFFF),A
mapst 07811   ; LD ($FFFF),A
mapst 07843   ; LD ($FFFF),A
mapst 07851   ; LD ($FFFF),A
mapst 0785F   ; LD ($FFFF),A
mapst 0786D   ; LD ($FFFF),A
mapst 0787B   ; LD ($FFFF),A
mapst 07889   ; LD ($FFFF),A
mapst 078D1   ; LD ($FFFF),A
mapst 079AF   ; LD ($FFFF),A
mapst 07A3B   ; LD ($FFFF),A
mapst 07AD1   ; LD ($FFFF),A
mapst 07ADF   ; LD ($FFFF),A
mapst 07AED   ; LD ($FFFF),A
mapst 07B1D   ; LD ($FFFF),A
mapst 07BA7   ; LD ($FFFF),A
mapst 07BE1   ; LD ($FFFF),A
mapst 07BEF   ; LD ($FFFF),A
mapst 07F49   ; LD ($FFFF),A
mapst 07F83   ; LD ($FFFF),A
# CHECK cartarea_store at 000EC ($00EC bank 0): 32 02 80  LD ($8002),A $8002
# CHECK cartarea_store at 000EF ($00EF bank 0): 32 02 80  LD ($8002),A $8002
# CHECK cartarea_store at 000F2 ($00F2 bank 0): 32 03 80  LD ($8003),A $8003
# CHECK cartarea_store at 000F5 ($00F5 bank 0): 32 01 80  LD ($8001),A $8001
# CHECK cartarea_store at 000FA ($00FA bank 0): 32 03 80  LD ($8003),A $8003
# CHECK cartarea_store at 00209 ($0209 bank 0): 32 02 80  LD ($8002),A $8002
# CHECK cartarea_store at 0020D ($020D bank 0): 32 02 80  LD ($8002),A $8002
# CHECK cartarea_store at 00227 ($0227 bank 0): 32 02 80  LD ($8002),A $8002
# CHECK cartarea_store at 0022A ($022A bank 0): 32 02 80  LD ($8002),A $8002
# CHECK cartarea_store at 00230 ($0230 bank 0): 32 01 80  LD ($8001),A $8001
# CHECK cartarea_store at 002A9 ($02A9 bank 0): 32 01 80  LD ($8001),A $8001
# CHECK cartarea_store at 002C6 ($02C6 bank 0): 32 01 80  LD ($8001),A $8001
# CHECK indirect_unresolved at 01568 ($1568 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 02C28 ($2C28 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 031C7 ($31C7 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 03508 ($3508 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 7E439 ($A439 bank 31): DD E9  JP (IX) 
# CHECK indirect_unresolved at 7E462 ($A462 bank 31): DD E9  JP (IX) 
# CHECK indirect_unresolved at 7E4C3 ($A4C3 bank 31): DD E9  JP (IX) 
# CHECK indirect_unresolved at 7E585 ($A585 bank 31): DD E9  JP (IX) 
# CHECK indirect_unresolved at 7F91D ($B91D bank 31): C9  RET 
# CHECK indirect_unresolved at 7F91D ($B91D bank 31): C9  RET 
# CHECK indirect_unresolved at 7F946 ($B946 bank 31): C9  RET 
# CHECK bank_unresolved at 00AD0 ($0AD0 bank 0): CD 29 9F  CALL $9F29 $9F29
# CHECK bank_unresolved at 01E1C ($1E1C bank 0): CD 28 A3  CALL $A328 $A328
# CHECK bank_unresolved at 01E1F ($1E1F bank 0): CD DC A3  CALL $A3DC $A3DC
# CHECK bank_unresolved at 01EA7 ($1EA7 bank 0): CD 70 B8  CALL $B870 $B870
# CHECK bank_unresolved at 01ECB ($1ECB bank 0): CD 51 B8  CALL $B851 $B851
# CHECK bank_unresolved at 02CA9 ($2CA9 bank 0): CD BC BC  CALL $BCBC $BCBC
# CHECK bank_unresolved at 02CCE ($2CCE bank 0): CD 68 BC  CALL $BC68 $BC68
# CHECK bank_unresolved at 02CD5 ($2CD5 bank 0): CD 00 BC  CALL $BC00 $BC00
# CHECK bank_unresolved at 02CE6 ($2CE6 bank 0): CD 7E BC  CALL $BC7E $BC7E
# CHECK bank_unresolved at 02CF2 ($2CF2 bank 0): CD BC BC  CALL $BCBC $BCBC
# CHECK bank_unresolved at 02D18 ($2D18 bank 0): CD 68 BC  CALL $BC68 $BC68
# CHECK bank_unresolved at 02D1F ($2D1F bank 0): CD 00 BC  CALL $BC00 $BC00
# CHECK bank_unresolved at 02D2F ($2D2F bank 0): CD 7E BC  CALL $BC7E $BC7E
# Mapper stores found by the byte scan in bytes no path reached:
# CHECK byte scan low: mapst 18D58  LD ($FFFF),A  (no evidence)
# CHECK byte scan medium: mapst 4EA17  LD ($FFFF),A  (32 bytes of valid code before it)
# CHECK byte scan low: mapsthl 54F17  LD ($FFFC),HL  (8 RST or NOP opcodes around it (looks like data); 25 bytes of valid code before it)
# CHECK byte scan low: mapsthl 54F23  LD ($FFFC),HL  (7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK byte scan low: mapst 59D67  LD ($FFFD),A  (4 RST or NOP opcodes around it (looks like data))
mapst 66713   # LD ($FFFF),A; after LD A,($FFEF); 19 bytes of valid code before it
# CHECK byte scan low: mapst 6E1AB  LD ($FFFF),A  (32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 00565  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 00569  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK high: site 0056C  OUT ($BE),A  (vdp_data; after POP AF; 32 bytes of valid code before it)
# CHECK medium: site 01D2B  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK high: site 01D30  IN A,($DD)  (joypad_b_misc; branch target from $01D35; 32 bytes of valid code before it)
site 07E02   ; OUT ($BF),A (RAM line handler at $C102)
site 07E06   ; OUT ($BF),A (RAM line handler at $C106)
site 07E11   ; OUT ($BF),A (RAM line handler at $C111)
site 07E15   ; OUT ($BF),A (RAM line handler at $C115)
site 07E19   ; OUT ($BF),A (RAM line handler at $C119)
site 07E1D   ; OUT ($BF),A (RAM line handler at $C11D)
site 07E33   ; OUT ($BF),A (RAM line handler at $C133)
site 07E37   ; OUT ($BF),A (RAM line handler at $C137)
site 07E44   ; OUT ($BF),A (RAM line handler at $C144)
site 07E48   ; OUT ($BF),A (RAM line handler at $C148)
site 07E50   ; OUT ($BF),A (RAM line handler at $C150)
site 07E54   ; OUT ($BF),A (RAM line handler at $C154)
site 07E69   ; OUT ($BF),A (RAM line handler at $C169)
site 07E6D   ; OUT ($BF),A (RAM line handler at $C16D)
site 07E79   ; OUT ($BF),A (RAM line handler at $C179)
site 07E7D   ; OUT ($BF),A (RAM line handler at $C17D)
site 07E82   ; OUT ($BF),A (RAM line handler at $C182)
site 07E86   ; OUT ($BF),A (RAM line handler at $C186)
site 07EA0   ; OUT ($BF),A (RAM line handler at $C1A0)
site 07EA4   ; OUT ($BF),A (RAM line handler at $C1A4)
site 07EB0   ; OUT ($BF),A (RAM line handler at $C1B0)
site 07EB4   ; OUT ($BF),A (RAM line handler at $C1B4)
site 07EC1   ; OUT ($BF),A (RAM line handler at $C1C1)
site 07EC5   ; OUT ($BF),A (RAM line handler at $C1C5)
site 07EDD   ; OUT ($BF),A (RAM line handler at $C1DD)
site 07EE1   ; OUT ($BF),A (RAM line handler at $C1E1)
site 07EE4   ; OUT ($BF),A (RAM line handler at $C1E4)
site 07EE8   ; OUT ($BF),A (RAM line handler at $C1E8)
# CHECK medium: site 0F246  IN A,($DD)  (joypad_b_misc; 19 bytes of valid code before it)
# CHECK medium: site 0F681  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK low: site 12B7D  OUTD  (port in C; no evidence)
# CHECK low: site 1337C  OUT ($7E),A  (psg; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 133A1  OUT ($7F),A  (psg; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 13558  OUT ($7F),A  (psg; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1355E  OUT ($7F),A  (psg; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 1495D  IN A,($BD)  (vdp_status; no evidence)
# CHECK medium: site 14996  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK medium: site 14A6D  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 14D39  OUTD  (port in C; 18 bytes of valid code before it)
# CHECK medium: site 14E42  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK low: site 14F92  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 14FB0  IN A,($DC)  (joypad_a; no evidence)
# CHECK medium: site 1536E  IN A,($3F)  (unmapped_read; 26 bytes of valid code before it)
# CHECK medium: site 15376  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 15492  OUT ($3F),A  (io_control; 32 bytes of valid code before it)
# CHECK low: site 1555B  OUT ($3F),A  (io_control; no evidence)
# CHECK low: site 1575A  OUT ($BD),A  (vdp_control; no evidence)
# CHECK medium: site 15787  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK medium: site 15AA7  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK high: site 16FC5  OUT (C),H  (port in C; branch target from $161F2; 32 bytes of valid code before it)
# CHECK low: site 17376  OTIR  (port in C; 17 bytes of valid code before it; no valid code after it)
# CHECK low: site 18A68  IN A,($DD)  (joypad_b_misc; no valid code after it)
# CHECK medium: site 197ED  OTDR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 197EF  IN A,($BD)  (vdp_status; 32 bytes of valid code before it)
# CHECK high: site 19955  OUT (C),E  (port in C; branch target from $185CE; 32 bytes of valid code before it)
# CHECK low: site 19AA8  OTIR  (port in C; branch target from $190C0; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 19BA5  IN A,($F0)  (joypad_a; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1A0D8  OUT ($3F),A  (io_control; no valid code after it)
# CHECK low: site 1A211  IN C,(C)  (port in C; no evidence)
# CHECK low: site 1A3C3  OTIR  (port in C; no evidence)
# CHECK medium: site 1A3C5  OTIR  (port in C; 21 bytes of valid code before it)
# CHECK medium: site 1A3C7  OTIR  (port in C; 23 bytes of valid code before it)
# CHECK medium: site 1A3C9  OTIR  (port in C; 25 bytes of valid code before it)
# CHECK medium: site 1A3CB  OTIR  (port in C; 27 bytes of valid code before it)
# CHECK low: site 1A3CD  OTIR  (port in C; 4 RST or NOP opcodes around it (looks like data); 29 bytes of valid code before it)
# CHECK low: site 1A658  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 1B2DF  IN A,($C1)  (joypad_b_misc; no evidence)
# CHECK medium: site 1B424  OUT ($3E),A  (memory_control; 32 bytes of valid code before it)
# CHECK medium: site 1B659  IN A,($F1)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK medium: site 1BAD4  IN A,($BD)  (vdp_status; 15 bytes of valid code before it)
# CHECK high: site 1BB0A  OUT ($F0),A  (fm_address; after LD A,$16)
# CHECK low: site 1BC94  OUT (C),A  (port in C; no evidence)
# CHECK low: site 1BCED  IN A,($F0)  (joypad_a; 24 bytes of valid code before it; no valid code after it)
# CHECK high: site 1C7EE  IND  (port in C; branch target from $1EDE0; 32 bytes of valid code before it)
# CHECK medium: site 1CA56  IN A,($3E)  (unmapped_read; branch target from $1E2DC)
# CHECK low: site 1CA58  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 1CA5A  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 1D935  OUT ($7F),A  (psg; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 1DA1E  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK low: site 1E081  IN C,(C)  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 1E19C  IN H,(C)  (port in C; branch target from $1D6A9)
# CHECK medium: site 1E2E9  IN A,($F0)  (joypad_a; 32 bytes of valid code before it)
# CHECK low: site 1E758  OUT (C),B  (port in C; no evidence)
# CHECK low: site 1EC60  OUT (C),B  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 1EF22  IN A,($3E)  (unmapped_read; branch target from $1EFA0)
# CHECK low: site 1F13E  IN A,($3E)  (unmapped_read; no evidence)
# CHECK medium: site 1F5C0  IN H,(C)  (port in C; 32 bytes of valid code before it)
# CHECK low: site 21596  IN A,(C)  (port in C; no valid code after it)
# CHECK low: site 21CA6  OUT ($C1),A  (no_effect; no valid code after it)
# CHECK low: site 21E2D  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 21F4F  IN A,($C1)  (joypad_b_misc; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 22625  INI  (port in C; no evidence)
# CHECK low: site 22916  IN A,($F2)  (fm_detect; no evidence)
# CHECK low: site 22C1F  IN A,($F2)  (fm_detect; no evidence)
# CHECK low: site 22E66  IN C,(C)  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 24687  IN A,($F0)  (joypad_a; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 24D63  IN A,($BF)  (vdp_status; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 25C42  IN A,($F0)  (joypad_a; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 27628  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 2782E  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 2F41F  IN A,($DC)  (joypad_a; 32 bytes of valid code before it)
# CHECK medium: site 2F87B  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK medium: site 2FADD  IN A,($DC)  (joypad_a; 19 bytes of valid code before it)
# CHECK low: site 2FED7  IN A,($3F)  (unmapped_read; no evidence)
# CHECK low: site 33A63  OUT ($7F),A  (psg; 4 RST or NOP opcodes around it (looks like data))
# CHECK low: site 345EB  OUT ($7F),A  (psg; 4 RST or NOP opcodes around it (looks like data))
# CHECK low: site 360A7  OUT ($7F),A  (psg; 9 RST or NOP opcodes around it (looks like data))
# CHECK low: site 3D8BB  IN A,($DC)  (joypad_a; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 3DE55  IN A,($DC)  (joypad_a; 4 RST or NOP opcodes around it (looks like data); 14 bytes of valid code before it)
# CHECK low: site 3F305  IN A,($DD)  (joypad_b_misc; 17 bytes of valid code before it; no valid code after it)
# CHECK low: site 3F61D  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK high: site 3F8E9  OUT (C),B  (port in C; branch target from $3F8DD; 26 bytes of valid code before it)
# CHECK low: site 3FBCC  IN A,($DC)  (joypad_a; 23 bytes of valid code before it; no valid code after it)
# CHECK low: site 42A60  IN A,($BF)  (vdp_status; no evidence)
# CHECK low: site 4A365  OUTD  (port in C; 20 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 4B0F7  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 4B789  IN B,(C)  (port in C; 5 RST or NOP opcodes around it (looks like data); 11 bytes of valid code before it)
# CHECK low: site 4B795  IN H,(C)  (port in C; 9 RST or NOP opcodes around it (looks like data); 23 bytes of valid code before it)
# CHECK low: site 50BA5  OUT (C),C  (port in C; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 512AD  OUT (C),B  (port in C; no evidence)
# CHECK low: site 6C583  IN H,(C)  (port in C; no valid code after it)
# CHECK low: site 6C587  INIR  (port in C; no valid code after it)
# CHECK medium: site 6F0FB  IN A,($7E)  (v_counter; 32 bytes of valid code before it)
# CHECK low: site 76583  IN B,(C)  (port in C; 5 RST or NOP opcodes around it (looks like data); 11 bytes of valid code before it)
# Re-entry guard for the bank 31 drawing task. The line handler at $C1DB runs
# EI; JP $1E73 once a frame, and $1E73 calls the task ($B851, $B870, or $225E in
# bank 0) with interrupts on. Bit 6 of $C2E9 is set for the whole call. On a
# Master System the call ends within the frame (at most 12,185 cycles; the reference
# never enters $1E73 with the bit set). On the Next it can still run when the chain
# comes round again, and the second entry corrupts the task's saved stack ($C200).
# The guard leaves the interrupt as $1E83 does while the bit is set.
label rr_guard 00020
label rr_1e78 01E78
label rr_1e83 01E83
asm 00020 16
    ld a,($C2E9)
    bit 6,a
    jp nz,rr_1e83
    ld a,($C2B2)
    bit 5,a
    jp rr_1e78
endasm
asm 01E73 5
    jp rr_guard
endasm
# HALTs that count frames (fades, waits). $1244 and $5BF0 wait for a flag and are safe.
eihalt 0044F
asm 00451 2
    rst $10
    db halt_io
endasm
eihalt 008CC
asm 009EE 4
    rst $10
    db halt_io
    rst $10
    db halt_io
endasm
asm 00A09 4
    rst $10
    db halt_io
    rst $10
    db halt_io
endasm
label rr_h0927 00041
label rr_h0918 00046
label rr_h7b71 0004B
label rr_h7b93 00050
label rr_hdjnz 00055
asm 00041 26
    rst $10
    db halt_io
    jp $0927
    rst $10
    db halt_io
    jp $0918
    rst $10
    db halt_io
    jp $7B71
    rst $10
    db halt_io
    jp $7B93
.l: rst $10
    db halt_io
    djnz .l
    ret
endasm
asm 00A1F 4
    call rr_h0927
endasm
asm 00A45 4
    call rr_h0918
endasm
asm 07B65 4
    call rr_h7b71
endasm
asm 07B87 4
    call rr_h7b93
endasm
asm 07BD6 3
    call rr_hdjnz
endasm
