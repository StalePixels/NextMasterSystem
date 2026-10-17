# R-Type, BB54B6B0, drafted by tools/mkspec.py from sitescan output (with the detector log).
name R-Type
cart BB54B6B0
hz any		; No-Intro regions World
# tilecache: whole tiles copied from cart ROM are not converted again (MAME,
# game frames 300-2300: framework cycles -0.3%, vertical blank tile work -12%)
tilecache
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
asm 00A15 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00A20 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00A2B 2   ; IM 1 -> IM 2
    im 2
endasm
site 00039   ; IN A,($BF)
site 0004B   ; OUT ($BF),A
site 00050   ; OUT ($BF),A
site 00075   ; OTIR
site 00093   ; OUT ($3F),A
site 00095   ; IN A,($DD)
site 0009F   ; OUT ($3F),A
site 000A1   ; IN A,($DD)
site 000AA   ; OUT ($3F),A
site 000B8   ; OUT ($3E),A
site 000C0   ; OUT ($F2),A
site 000C3   ; IN A,($F2)
site 000D5   ; OUT ($F2),A
site 000DD   ; OUT ($3E),A
site 000E6   ; IN A,($BF)
site 000EC   ; IN A,($BF)
site 000F3   ; IN A,($BF)
site 00105   ; IN A,($BF)
site 0011A   ; OUTI
site 0011C   ; OUT ($BF),A
site 00123   ; OUT ($BF),A
site 00127   ; OUT ($BF),A
site 0012F   ; OUT ($BE),A
site 00137   ; OUT ($BF),A
site 0013B   ; OUT ($BF),A
site 0013F   ; OUT ($BE),A
site 001C1   ; OUT ($BF),A
site 001C6   ; OUT ($BF),A
site 001CC   ; OUT ($BF),A
site 001D1   ; OUT ($BF),A
site 001DF   ; OUT ($BE),A
otir 0020E   ; OUTI
site 0022F   ; OUT (C),H
site 00234   ; OUT (C),L
site 00281   ; IN A,($BE)
site 00286   ; IN A,($BE)
site 0028B   ; OUT ($BE),A
site 00293   ; OUT ($BE),A
site 002BE   ; IN A,($BE)
site 002C3   ; IN A,($BE)
site 002C8   ; OUT ($BE),A
site 002CE   ; OUT ($BE),A
site 003D3   ; OUT ($BE),A
site 003DB   ; OUT ($BE),A
site 00435   ; OUT ($BF),A
site 00439   ; OUT ($BF),A
site 00445   ; OUT ($BF),A
site 00449   ; OUT ($BF),A
site 0044C   ; OUT ($BF),A
site 00450   ; OUT ($BF),A
site 0052A   ; IN A,($DD)
site 00559   ; OUT ($BF),A
site 0055D   ; OUT ($BF),A
site 00567   ; OUT ($BF),A
site 0056B   ; OUT ($BF),A
site 00575   ; OUT ($BF),A
site 00579   ; OUT ($BF),A
site 00587   ; OUT ($BF),A
site 0058B   ; OUT ($BF),A
otir 00595   ; OUTI
site 005DE   ; OUTI
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
site 00620   ; OUTI
site 00622   ; OUTI
site 00624   ; OUTI
site 00626   ; OUTI
site 00628   ; OUTI
site 0062A   ; OUTI
site 0062C   ; OUTI
site 0062E   ; OUTI
site 00630   ; OUTI
site 00632   ; OUTI
site 00634   ; OUTI
site 00636   ; OUTI
site 00638   ; OUTI
site 0063A   ; OUTI
site 0063C   ; OUTI
site 0063E   ; OUTI
site 00640   ; OUTI
site 00642   ; OUTI
site 00644   ; OUTI
site 00646   ; OUTI
site 00648   ; OUTI
site 0064A   ; OUTI
site 0064C   ; OUTI
site 0064E   ; OUTI
site 00650   ; OUTI
site 00652   ; OUTI
site 00654   ; OUTI
site 00656   ; OUTI
site 00658   ; OUTI
site 0065A   ; OUTI
site 0065C   ; OUTI
site 0065E   ; OUTI
site 00660   ; OUTI
site 00662   ; OUTI
site 00664   ; OUTI
site 00666   ; OUTI
site 00668   ; OUTI
site 0066A   ; OUTI
site 0066C   ; OUTI
site 0066E   ; OUTI
site 00670   ; OUTI
site 00672   ; OUTI
site 00674   ; OUTI
site 00676   ; OUTI
site 00678   ; OUTI
site 0067A   ; OUTI
site 0067C   ; OUTI
site 0067E   ; OUTI
site 00680   ; OUTI
site 00682   ; OUTI
site 00684   ; OUTI
site 00686   ; OUTI
site 00688   ; OUTI
site 0068A   ; OUTI
site 0068C   ; OUTI
site 0068E   ; OUTI
site 00690   ; OUTI
site 00692   ; OUTI
site 00694   ; OUTI
site 00696   ; OUTI
site 00698   ; OUTI
site 0069A   ; OUTI
site 0069C   ; OUTI
site 0069E   ; OUTI
site 006A0   ; OUTI
site 006A2   ; OUTI
site 006A4   ; OUTI
site 006A6   ; OUTI
site 006A8   ; OUTI
site 006AA   ; OUTI
site 006AC   ; OUTI
site 006AE   ; OUTI
site 006B0   ; OUTI
site 006B2   ; OUTI
site 006B4   ; OUTI
site 006B6   ; OUTI
site 006B8   ; OUTI
site 006BA   ; OUTI
site 006BC   ; OUTI
site 006BE   ; OUTI
site 006C0   ; OUTI
site 006C2   ; OUTI
site 006C4   ; OUTI
site 006C6   ; OUTI
site 006C8   ; OUTI
site 006CA   ; OUTI
site 006CC   ; OUTI
site 006CE   ; OUTI
site 006D0   ; OUTI
site 006D2   ; OUTI
site 006D4   ; OUTI
site 006D6   ; OUTI
site 006D8   ; OUTI
site 006DA   ; OUTI
site 006DC   ; OUTI
site 006E1   ; OUT ($DF),A
site 006E5   ; OUT ($DE),A
site 006E8   ; IN A,($DC)
site 006EE   ; IN A,($DC)
site 006F1   ; IN A,($DD)
site 0085D   ; OUTI
site 00860   ; IN A,($BE)
site 00863   ; IN A,($BE)
site 00866   ; IN A,($BE)
site 00872   ; OUT (C),A
site 00875   ; IN A,($BE)
site 00878   ; IN A,($BE)
site 0087B   ; IN A,($BE)
site 00EA5   ; OUT ($BF),A
site 00EA9   ; OUT ($BF),A
otir 00EAB   ; OUTI
site 00ECD   ; OUT ($BF),A
site 00ED1   ; OUT ($BF),A
otir 00ED3   ; OUTI
site 00EF5   ; OUT ($BF),A
site 00EF9   ; OUT ($BF),A
otir 00EFB   ; OUTI
site 00F1E   ; OUT ($BF),A
site 00F22   ; OUT ($BF),A
otir 00F24   ; OUTI
site 00F2C   ; OUT ($BF),A
site 00F30   ; OUT ($BF),A
otir 00F32   ; OUTI
site 00F55   ; OUT ($BF),A
site 00F59   ; OUT ($BF),A
otir 00F5B   ; OUTI
site 01536   ; OUT ($BF),A
site 01539   ; OUT ($BF),A
site 0153B   ; OUTI
site 0153D   ; OUTI
site 01565   ; OUT ($BF),A
site 01569   ; OUT ($BF),A
site 01570   ; OUTI
site 01572   ; OUTI
site 01574   ; OUTI
site 01576   ; OUTI
site 01578   ; OUTI
site 0157A   ; OUTI
site 0157C   ; OUTI
site 0157E   ; OUTI
site 01580   ; OUTI
site 01582   ; OUTI
site 01584   ; OUTI
site 01586   ; OUTI
site 01588   ; OUTI
site 0158A   ; OUTI
site 0158C   ; OUTI
site 0158E   ; OUTI
site 01590   ; OUTI
site 01592   ; OUTI
site 01594   ; OUTI
site 01596   ; OUTI
site 01598   ; OUTI
site 0159A   ; OUTI
site 0159C   ; OUTI
site 0159E   ; OUTI
site 015A0   ; OUTI
site 015A2   ; OUTI
site 015A4   ; OUTI
site 015A6   ; OUTI
site 015A8   ; OUTI
site 015AA   ; OUTI
site 015AC   ; OUTI
site 015AE   ; OUTI
site 0174B   ; OUT ($BF),A
site 0174E   ; OUT ($BF),A
site 01753   ; OUTI
site 01758   ; OUTI
site 01776   ; OUT ($BF),A
site 0177A   ; OUT ($BF),A
otir 01783   ; OUTI
site 025F4   ; OUT ($BF),A
site 025F8   ; OUT ($BF),A
site 02623   ; OUT ($BF),A
site 02627   ; OUT ($BF),A
site 02655   ; OUT ($BF),A
site 02659   ; OUT ($BF),A
otir 0272B   ; OUTI
site 06F26   ; OUT ($F0),A
site 06F33   ; OUT ($F1),A
site 06F43   ; OUT ($F0),A
site 06F4A   ; OUT ($F1),A
site 06F51   ; OUT ($F1),A
site 06F65   ; OUT ($F0),A
site 06F68   ; OUT ($F1),A
site 06F79   ; OUT ($F0),A
site 06F7E   ; OUT ($F1),A
site 06F8A   ; OUT ($F1),A
site 06F9D   ; OUT ($F0),A
site 06FA0   ; OUT ($F1),A
site 06FC1   ; OUT ($F0),A
site 06FC4   ; OUT ($F1),A
site 06FD9   ; OUT ($7F),A
site 06FDF   ; OUT ($7F),A
site 06FEB   ; OUT ($7F),A
site 07008   ; OUT ($7F),A
site 07011   ; OUT ($7F),A
site 077FA   ; OUT ($F0),A
site 077FD   ; OUT ($F1),A
site 0780C   ; OUT ($F0),A
site 07810   ; OUT ($F1),A
site 07825   ; OUT ($F0),A
site 07828   ; OUT ($F1),A
site 07843   ; OUT ($F2),A
site 13345   ; OUT ($BF),A
site 13349   ; OUT ($BF),A
site 13356   ; OUT ($BE),A
site 1335B   ; OUT ($BE),A
site 13364   ; OUT ($BE),A
site 13369   ; OUT ($BE),A
site 13375   ; OUT ($BF),A
site 1337A   ; OUT ($BF),A
site 13382   ; OUT ($BE),A
site 13389   ; OUT ($BE),A
site 138B2   ; OUT ($BF),A
site 138B6   ; OUT ($BF),A
site 138BC   ; OUT ($BE),A
site 138C3   ; OUT ($BE),A
# Screen I/O that the draft missed: the scan reached these only as bytes no path
# reached (bank 0) or as the bank 4 routines that the level 3 warship and the level 4
# dot-droppers draw with. The attract-mode I/O log runs every one of them.
site 02E98   ; OUT ($BE),A
site 02E9F   ; OUT ($BE),A
site 02EC2   ; OUT ($BE),A
site 02EC9   ; OUT ($BE),A
site 106D7   ; OUT ($BF),A
site 106DB   ; OUT ($BF),A
site 10894   ; OUT ($BF),A
site 10897   ; OUT ($BF),A
site 1089A   ; OUT ($BE),A
site 108A2   ; OUT ($BE),A
site 10BCC   ; OUT ($BF),A
site 10BD1   ; OUT ($BF),A
site 10BD5   ; IN A,($BE)
site 10BDB   ; IN A,($BE)
site 10BE8   ; OUT ($BF),A
site 10BEF   ; OUT ($BF),A
site 10BF5   ; IN A,($BE)
site 10BFA   ; IN A,($BE)
site 10CEA   ; OUT ($BF),A
site 10CED   ; OUT ($BF),A
site 10CF3   ; OUT ($BE),A
site 10CFA   ; OUT ($BE),A
site 10D0B   ; OUT ($BF),A
site 10D10   ; OUT ($BF),A
site 10D1B   ; OUT ($BF),A
site 10D1E   ; OUT ($BF),A
site 10D28   ; OUT ($BF),A
site 10D2D   ; OUT ($BF),A
site 10D33   ; OUT ($BE),A
site 10D3A   ; OUT ($BE),A
site 111FC   ; OUT ($BF),A
site 111FF   ; OUT ($BF),A
site 118CB   ; OUT ($BF),A
site 118CE   ; OUT ($BF),A
site 118D8   ; OUT ($BF),A
site 118DB   ; OUT ($BF),A
site 118E5   ; OUT ($BF),A
site 118E8   ; OUT ($BF),A
site 11925   ; OUT ($BE),A
site 1192B   ; OUT ($BE),A
site 11A9E   ; OUT ($BF),A
site 11AA1   ; OUT ($BF),A
site 11AA4   ; OUT ($BE),A
site 11AAB   ; OUT ($BE),A
site 122AE   ; OUT ($BF),A
site 122B4   ; OUT ($BF),A
site 122DD   ; OUTI
site 12300   ; OUT ($BE),A
site 12313   ; OUTI
site 12317   ; OUTI
site 1231B   ; OUTI
site 1231F   ; OUTI
site 1234A   ; OUT ($BE),A
# CHECK mapper at 00006 ($0006 bank 0): LD (HL),$00 $FFFC<-$00
# CHECK mapper at 00009 ($0009 bank 0): LD (HL),$00 $FFFD<-$00
# CHECK mapper at 0000C ($000C bank 0): LD (HL),$01 $FFFE<-$01
# CHECK mapper at 0000F ($000F bank 0): LD (HL),$02 $FFFF<-$02
mapldk 00003   # loads HL with $FFFC, then stores $00 through it
maphl 00009   # LD (HL),$00, HL = $FFFD
maphl 0000C   # LD (HL),$01, HL = $FFFE
maphl 0000F   # LD (HL),$02, HL = $FFFF
mapst 0048E   ; LD ($FFFF),A
mapsthl 00495   # LD ($FFFE),HL in the ISR: restores both banks
mapst 004E9   ; LD ($FFFF),A
mapst 004F6   ; LD ($FFFF),A
mapst 00500   ; LD ($FFFF),A
mapst 00507   ; LD ($FFFF),A
mapst 00514   ; LD ($FFFF),A
mapst 0051E   ; LD ($FFFF),A
mapst 007E8   ; LD ($FFFF),A
mapst 00A90   ; LD ($FFFF),A
mapst 00B16   ; LD ($FFFF),A
mapst 00B87   ; LD ($FFFF),A
mapst 00BB9   ; LD ($FFFF),A
mapst 00BCA   ; LD ($FFFF),A
mapst 00C9E   ; LD ($FFFF),A
mapst 00CA6   ; LD ($FFFF),A
mapst 00CC6   ; LD ($FFFF),A
mapst 00D0E   ; LD ($FFFF),A
mapst 00E8D   ; LD ($FFFF),A
mapst 00EB5   ; LD ($FFFF),A
mapst 00EDD   ; LD ($FFFF),A
mapst 00F06   ; LD ($FFFF),A
mapst 00F3D   ; LD ($FFFF),A
mapst 01070   ; LD ($FFFF),A
mapst 01138   ; LD ($FFFF),A
mapst 01450   ; LD ($FFFF),A
mapst 01460   ; LD ($FFFF),A
mapst 014A5   ; LD ($FFFF),A
mapst 01560   ; LD ($FFFF),A
mapst 01609   ; LD ($FFFF),A
mapst 016CD   ; LD ($FFFF),A
mapst 0176F   ; LD ($FFFF),A
mapst 01AC5   ; LD ($FFFF),A
mapst 01BB0   ; LD ($FFFF),A
mapst 01BD9   ; LD ($FFFF),A
mapst 01CE7   ; LD ($FFFF),A
mapst 01DE8   ; LD ($FFFF),A
mapst 01EBA   ; LD ($FFFF),A
mapst 02597   ; LD ($FFFF),A
mapst 025E9   ; LD ($FFFF),A
mapst 026DF   ; LD ($FFFF),A
mapst 0273D   ; LD ($FFFF),A
mapst 0648C   ; LD ($FFFF),A
mapst 064A3   ; LD ($FFFF),A
mapst 064A9   ; LD ($FFFF),A
mapst 064C2   ; LD ($FFFF),A
mapst 064C8   ; LD ($FFFF),A
mapst 06521   ; LD ($FFFF),A
mapst 065E9   ; LD ($FFFF),A
mapst 06617   ; LD ($FFFF),A
mapst 06B29   ; LD ($FFFF),A
mapst 06B72   ; LD ($FFFF),A
mapst 06BBB   ; LD ($FFFF),A
mapst 06BD6   ; LD ($FFFF),A
mapst 06C94   ; LD ($FFFF),A
mapst 06CAC   ; LD ($FFFF),A
mapst 06DC8   ; LD ($FFFF),A
mapst 06DE0   ; LD ($FFFF),A
# CHECK indirect_unresolved at 01DBE ($1DBE bank 0): CALL $1DE6 $1DE6
# CHECK indirect_unresolved at 01DBE ($1DBE bank 0): CALL $1DE6 $1DE6
# CHECK indirect_unresolved at 02644 ($2644 bank 0): RET 
# CHECK indirect_unresolved at 0266F ($266F bank 0): RET 
# CHECK bank_unresolved at 00491 ($0491 bank 0): CALL $6DEC $6DEC
# CHECK bank_unresolved at 004F2 ($04F2 bank 0): CALL $77E6 $77E6
# CHECK bank_unresolved at 00503 ($0503 bank 0): CALL $784D $784D
# CHECK bank_unresolved at 0051A ($051A bank 0): CALL $787F $787F
# CHECK bank_unresolved at 00522 ($0522 bank 0): CALL $7B39 $7B39
# CHECK bank_unresolved at 005B9 ($05B9 bank 0): CALL $7B2C $7B2C
# CHECK bank_unresolved at 005CE ($05CE bank 0): CALL $7B32 $7B32
# CHECK bank_unresolved at 00AA9 ($0AA9 bank 0): JP M,$5A6C $5A6C
# CHECK bank_unresolved at 00CA9 ($0CA9 bank 0): CALL $60DF $60DF
# CHECK bank_unresolved at 00CC9 ($0CC9 bank 0): CALL $8003 $8003
# CHECK bank_unresolved at 01464 ($1464 bank 0): CALL $575A $575A
# CHECK bank_unresolved at 03234 ($3234 bank 0): JP $5657 $5657
# CHECK bank_unresolved at 034A3 ($34A3 bank 0): CALL $56DB $56DB
# CHECK bank_unresolved at 0811E ($811E bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 08122 ($8122 bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 08125 ($8125 bank 2): CALL $7F6F $7F6F
# CHECK bank_unresolved at 08143 ($8143 bank 2): JP $7F36 $7F36
# CHECK bank_unresolved at 0840D ($840D bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 08411 ($8411 bank 2): CALL $7F60 $7F60
# CHECK bank_unresolved at 08414 ($8414 bank 2): CALL $7F66 $7F66
# CHECK bank_unresolved at 0841C ($841C bank 2): JP $7F36 $7F36
# CHECK bank_unresolved at 08484 ($8484 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 08488 ($8488 bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 0848B ($848B bank 2): CALL $7F66 $7F66
# CHECK bank_unresolved at 0848E ($848E bank 2): JP $7F78 $7F78
# CHECK bank_unresolved at 08613 ($8613 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 08617 ($8617 bank 2): CALL $7F60 $7F60
# CHECK bank_unresolved at 086D2 ($86D2 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 086D6 ($86D6 bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 086D9 ($86D9 bank 2): CALL $7F69 $7F69
# CHECK bank_unresolved at 086DC ($86DC bank 2): CALL $7F7B $7F7B
# CHECK bank_unresolved at 087CA ($87CA bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 087E0 ($87E0 bank 2): CALL $7F81 $7F81
# CHECK bank_unresolved at 087E3 ($87E3 bank 2): CALL $7F84 $7F84
# CHECK bank_unresolved at 089CB ($89CB bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 089CF ($89CF bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 08FDA ($8FDA bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 08FDE ($8FDE bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 08FE1 ($8FE1 bank 2): CALL $7F72 $7F72
# CHECK bank_unresolved at 08FE4 ($8FE4 bank 2): CALL $7F75 $7F75
# CHECK bank_unresolved at 09089 ($9089 bank 2): CALL $7FE4 $7FE4
# CHECK bank_unresolved at 093F0 ($93F0 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 093F4 ($93F4 bank 2): CALL $7F87 $7F87
# CHECK bank_unresolved at 093F7 ($93F7 bank 2): CALL $7F8A $7F8A
# CHECK bank_unresolved at 095A5 ($95A5 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 095A9 ($95A9 bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 095AC ($95AC bank 2): CALL $7F66 $7F66
# CHECK bank_unresolved at 096CF ($96CF bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 096D3 ($96D3 bank 2): CALL $7F66 $7F66
# CHECK bank_unresolved at 096D6 ($96D6 bank 2): CALL $7F8D $7F8D
# CHECK bank_unresolved at 097F5 ($97F5 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 097F9 ($97F9 bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 09B14 ($9B14 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 09B18 ($9B18 bank 2): CALL $7F6C $7F6C
# CHECK bank_unresolved at 0A3E8 ($A3E8 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 0A3EC ($A3EC bank 2): CALL $7F60 $7F60
# CHECK bank_unresolved at 0A3EF ($A3EF bank 2): CALL $7F66 $7F66
# CHECK bank_unresolved at 0A5B6 ($A5B6 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 0A5BA ($A5BA bank 2): CALL $7F66 $7F66
# CHECK bank_unresolved at 0A5BD ($A5BD bank 2): CALL $7F7E $7F7E
# CHECK bank_unresolved at 0A74A ($A74A bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 0AA02 ($AA02 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 0AA06 ($AA06 bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 0AA09 ($AA09 bank 2): CALL $7F66 $7F66
# CHECK bank_unresolved at 0AB8F ($AB8F bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 0ABA5 ($ABA5 bank 2): CALL $7F1E $7F1E
# CHECK bank_unresolved at 0AEA2 ($AEA2 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 0AEA6 ($AEA6 bank 2): CALL $7F63 $7F63
# CHECK bank_unresolved at 0B000 ($B000 bank 2): CALL $7FE4 $7FE4
# CHECK bank_unresolved at 0B4BC ($B4BC bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 0B643 ($B643 bank 2): CALL $7F00 $7F00
# CHECK bank_unresolved at 0B65D ($B65D bank 2): CALL $7F66 $7F66
# CHECK bank_unresolved at 1323E ($B23E bank 4): CALL $7FAB $7FAB
# CHECK bank_unresolved at 13267 ($B267 bank 4): CALL $7F2A $7F2A
# CHECK bank_unresolved at 1326D ($B26D bank 4): CALL $7FD5 $7FD5
# CHECK bank_unresolved at 1327F ($B27F bank 4): CALL $7FAB $7FAB
# CHECK bank_unresolved at 132CA ($B2CA bank 4): CALL $7F2A $7F2A
# CHECK bank_unresolved at 13313 ($B313 bank 4): CALL $7FAB $7FAB
# CHECK bank_unresolved at 1365E ($B65E bank 4): CALL $7FD5 $7FD5
# CHECK bank_unresolved at 1367D ($B67D bank 4): CALL $7FAB $7FAB
# CHECK bank_unresolved at 13683 ($B683 bank 4): CALL $7FD5 $7FD5
# CHECK bank_unresolved at 136FB ($B6FB bank 4): CALL $7F2A $7F2A
# CHECK bank_unresolved at 13716 ($B716 bank 4): CALL $7FD5 $7FD5
# CHECK bank_unresolved at 1914D ($914D bank 6): CALL $7FAB $7FAB
# CHECK bank_unresolved at 19152 ($9152 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 191C4 ($91C4 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 191F6 ($91F6 bank 6): CALL Z,$7FC6 $7FC6
# CHECK bank_unresolved at 19296 ($9296 bank 6): CALL $7FC6 $7FC6
# CHECK bank_unresolved at 192BF ($92BF bank 6): CALL $7FC6 $7FC6
# CHECK bank_unresolved at 1938A ($938A bank 6): CALL $7FD2 $7FD2
# CHECK bank_unresolved at 19398 ($9398 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 193B6 ($93B6 bank 6): CALL $7FD2 $7FD2
# CHECK bank_unresolved at 193C4 ($93C4 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 193D2 ($93D2 bank 6): CALL $7FD2 $7FD2
# CHECK bank_unresolved at 193D5 ($93D5 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 193EB ($93EB bank 6): CALL $7FD2 $7FD2
# CHECK bank_unresolved at 193EE ($93EE bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19416 ($9416 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19426 ($9426 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19436 ($9436 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19441 ($9441 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 194DE ($94DE bank 6): CALL $7FD2 $7FD2
# CHECK bank_unresolved at 194E1 ($94E1 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19510 ($9510 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19523 ($9523 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19543 ($9543 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 195BD ($95BD bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 195C3 ($95C3 bank 6): CALL $7FC6 $7FC6
# CHECK bank_unresolved at 195F9 ($95F9 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 195FF ($95FF bank 6): CALL $7FC6 $7FC6
# CHECK bank_unresolved at 19615 ($9615 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19622 ($9622 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 1962E ($962E bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 1963B ($963B bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 1963E ($963E bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19644 ($9644 bank 6): CALL $7FC6 $7FC6
# CHECK bank_unresolved at 1965E ($965E bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 1966B ($966B bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19677 ($9677 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19684 ($9684 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19687 ($9687 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 1968D ($968D bank 6): CALL $7FC6 $7FC6
# CHECK bank_unresolved at 196CC ($96CC bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19770 ($9770 bank 6): CALL $7FC0 $7FC0
# CHECK bank_unresolved at 19789 ($9789 bank 6): CALL $7FC3 $7FC3
# CHECK bank_unresolved at 197A0 ($97A0 bank 6): CALL $7FCC $7FCC
# CHECK bank_unresolved at 197BB ($97BB bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 197BE ($97BE bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 197F1 ($97F1 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 197F8 ($97F8 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19801 ($9801 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19804 ($9804 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 1981F ($981F bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19845 ($9845 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19851 ($9851 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 1985E ($985E bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19861 ($9861 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19883 ($9883 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 1988F ($988F bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 1989C ($989C bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 1989F ($989F bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 198C7 ($98C7 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 198D9 ($98D9 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 198E6 ($98E6 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 198E9 ($98E9 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19911 ($9911 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19923 ($9923 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19930 ($9930 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19933 ($9933 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 1995D ($995D bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19971 ($9971 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 1997E ($997E bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19981 ($9981 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 199AB ($99AB bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 199BF ($99BF bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 199CC ($99CC bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 199CF ($99CF bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 199F1 ($99F1 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 199FD ($99FD bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19A0A ($9A0A bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19A0D ($9A0D bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19A2F ($9A2F bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19A3B ($9A3B bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19A48 ($9A48 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19A4B ($9A4B bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19A6F ($9A6F bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19A7D ($9A7D bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19A8A ($9A8A bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19A8D ($9A8D bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19AB1 ($9AB1 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19ABF ($9ABF bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19ACC ($9ACC bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19ACF ($9ACF bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19B21 ($9B21 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19C6F ($9C6F bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19D65 ($9D65 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19D94 ($9D94 bank 6): JP $7FC9 $7FC9
# CHECK bank_unresolved at 19DE5 ($9DE5 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 19E01 ($9E01 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19E04 ($9E04 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19E10 ($9E10 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19E47 ($9E47 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19E4A ($9E4A bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19E59 ($9E59 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19E65 ($9E65 bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19E68 ($9E68 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19E77 ($9E77 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19E87 ($9E87 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19E9D ($9E9D bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19EB9 ($9EB9 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19ED4 ($9ED4 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19EEF ($9EEF bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19F1C ($9F1C bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19F1F ($9F1F bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19F2E ($9F2E bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19F3A ($9F3A bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 19F3D ($9F3D bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 19F4C ($9F4C bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19F5C ($9F5C bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19F72 ($9F72 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19F8E ($9F8E bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19FA9 ($9FA9 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19FC4 ($9FC4 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 19FCD ($9FCD bank 6): CALL $7FC6 $7FC6
# CHECK bank_unresolved at 19FDB ($9FDB bank 6): CALL $7FC6 $7FC6
# CHECK bank_unresolved at 1A03E ($A03E bank 6): CALL $7FCF $7FCF
# CHECK bank_unresolved at 1A041 ($A041 bank 6): CALL $7F15 $7F15
# CHECK bank_unresolved at 1A04D ($A04D bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 1A118 ($A118 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 1A254 ($A254 bank 6): JP $7FC6 $7FC6
# CHECK bank_unresolved at 1A2A4 ($A2A4 bank 6): CALL $7F2A $7F2A
# CHECK bank_unresolved at 1A34B ($A34B bank 6): CALL $7FC6 $7FC6
# CHECK low: site 00042  IN A,($BF)  (vdp_status)
# CHECK low: site 00188  IN A,($BE)  (vdp_data)
# CHECK low: site 00193  IN A,($BE)  (vdp_data)
# CHECK low: site 0019E  OUT ($BE),A  (vdp_data)
# CHECK low: site 001A9  OUT ($BE),A  (vdp_data)
# CHECK low: site 001AF  OUT ($BF),A  (vdp_control)
# CHECK low: site 001B2  OUT ($BF),A  (vdp_control)
# CHECK low: site 001B8  OUT ($BF),A  (vdp_control)
# CHECK low: site 001BB  OUT ($BF),A  (vdp_control)
# CHECK low: site 001F7  INI  (port in C)
# CHECK low: site 00319  OUT ($BE),A  (vdp_data)
# CHECK low: site 0031F  OUT ($BE),A  (vdp_data)
# CHECK low: site 0034A  OUT ($BE),A  (vdp_data)
# CHECK low: site 00350  OUT ($BE),A  (vdp_data)
# CHECK low: site 02E98  OUT ($BE),A  (vdp_data)
# CHECK low: site 02E9F  OUT ($BE),A  (vdp_data)
# CHECK low: site 02EC2  OUT ($BE),A  (vdp_data)
# CHECK low: site 02EC9  OUT ($BE),A  (vdp_data)
# CHECK low: site 04CC2  OUT ($BE),A  (vdp_data)
# CHECK low: site 04CC8  OUT ($BE),A  (vdp_data)
# CHECK low: site 05623  INI  (port in C)
# CHECK low: site 05634  INI  (port in C)
# CHECK low: site 05639  OUT ($BE),A  (vdp_data)
# CHECK low: site 0567F  OUT ($BE),A  (vdp_data)
# CHECK low: site 05687  OUT ($BE),A  (vdp_data)
# CHECK low: site 06AC0  OUTI  (port in C)
# CHECK low: site 06AC7  OUT (C),A  (port in C)
# CHECK low: site 0A72B  IN A,($7F)  (h_counter)
# CHECK low: site 0B4A3  IN A,($7F)  (h_counter)
# CHECK low: site 0B5D7  IN A,($7F)  (h_counter)
# CHECK low: site 0B6EC  IN A,($7F)  (h_counter)
# CHECK low: site 0B9DC  IN A,($7F)  (h_counter)
# CHECK low: site 0BAAC  IN A,($7F)  (h_counter)
# CHECK low: site 0BB7A  IN A,($7F)  (h_counter)
# CHECK low: site 106A2  OUT ($BF),A  (vdp_control)
# CHECK low: site 106A5  OUT ($BF),A  (vdp_control)
# CHECK low: site 106AA  OUT ($BE),A  (vdp_data)
# CHECK low: site 106B1  OUT ($BE),A  (vdp_data)
# CHECK low: site 106D7  OUT ($BF),A  (vdp_control)
# CHECK low: site 106DB  OUT ($BF),A  (vdp_control)
# CHECK low: site 1074A  OUT ($BF),A  (vdp_control)
# CHECK low: site 10750  OUT ($BF),A  (vdp_control)
# CHECK low: site 10757  IN A,($BE)  (vdp_data)
# CHECK low: site 1075D  IN A,($BE)  (vdp_data)
# CHECK low: site 10894  OUT ($BF),A  (vdp_control)
# CHECK low: site 10897  OUT ($BF),A  (vdp_control)
# CHECK low: site 1089A  OUT ($BE),A  (vdp_data)
# CHECK low: site 108A2  OUT ($BE),A  (vdp_data)
# CHECK low: site 10BCC  OUT ($BF),A  (vdp_control)
# CHECK low: site 10BD1  OUT ($BF),A  (vdp_control)
# CHECK low: site 10BD5  IN A,($BE)  (vdp_data)
# CHECK low: site 10BDB  IN A,($BE)  (vdp_data)
# CHECK low: site 10BE8  OUT ($BF),A  (vdp_control)
# CHECK low: site 10BEF  OUT ($BF),A  (vdp_control)
# CHECK low: site 10BF5  IN A,($BE)  (vdp_data)
# CHECK low: site 10BFA  IN A,($BE)  (vdp_data)
# CHECK low: site 10CEA  OUT ($BF),A  (vdp_control)
# CHECK low: site 10CED  OUT ($BF),A  (vdp_control)
# CHECK low: site 10CF3  OUT ($BE),A  (vdp_data)
# CHECK low: site 10CFA  OUT ($BE),A  (vdp_data)
# CHECK low: site 10D0B  OUT ($BF),A  (vdp_control)
# CHECK low: site 10D10  OUT ($BF),A  (vdp_control)
# CHECK low: site 10D1B  OUT ($BF),A  (vdp_control)
# CHECK low: site 10D1E  OUT ($BF),A  (vdp_control)
# CHECK low: site 10D28  OUT ($BF),A  (vdp_control)
# CHECK low: site 10D2D  OUT ($BF),A  (vdp_control)
# CHECK low: site 10D33  OUT ($BE),A  (vdp_data)
# CHECK low: site 10D3A  OUT ($BE),A  (vdp_data)
# CHECK low: site 111FC  OUT ($BF),A  (vdp_control)
# CHECK low: site 111FF  OUT ($BF),A  (vdp_control)
# CHECK low: site 118CB  OUT ($BF),A  (vdp_control)
# CHECK low: site 118CE  OUT ($BF),A  (vdp_control)
# CHECK low: site 118D8  OUT ($BF),A  (vdp_control)
# CHECK low: site 118DB  OUT ($BF),A  (vdp_control)
# CHECK low: site 118E5  OUT ($BF),A  (vdp_control)
# CHECK low: site 118E8  OUT ($BF),A  (vdp_control)
# CHECK low: site 11925  OUT ($BE),A  (vdp_data)
# CHECK low: site 1192B  OUT ($BE),A  (vdp_data)
# CHECK low: site 11A9E  OUT ($BF),A  (vdp_control)
# CHECK low: site 11AA1  OUT ($BF),A  (vdp_control)
# CHECK low: site 11AA4  OUT ($BE),A  (vdp_data)
# CHECK low: site 11AAB  OUT ($BE),A  (vdp_data)
# CHECK low: site 11F66  OUT ($BF),A  (vdp_control)
# CHECK low: site 11F69  OUT ($BF),A  (vdp_control)
# CHECK low: site 11F6D  IN A,($BE)  (vdp_data)
# CHECK low: site 11F74  OUT ($BF),A  (vdp_control)
# CHECK low: site 11F79  OUT ($BF),A  (vdp_control)
# CHECK low: site 11F7C  OUT ($BE),A  (vdp_data)
# CHECK low: site 122AE  OUT ($BF),A  (vdp_control)
# CHECK low: site 122B4  OUT ($BF),A  (vdp_control)
# CHECK low: site 122DD  OUTI  (port in C)
# CHECK low: site 12300  OUT ($BE),A  (vdp_data)
# CHECK low: site 12313  OUTI  (port in C)
# CHECK low: site 12317  OUTI  (port in C)
# CHECK low: site 1231B  OUTI  (port in C)
# CHECK low: site 1231F  OUTI  (port in C)
# CHECK low: site 1234A  OUT ($BE),A  (vdp_data)
# CHECK low: site 164FA  IN A,($BF)  (vdp_status)
# CHECK low: site 17252  OUT ($BF),A  (vdp_control)
# CHECK low: site 17258  OUT ($BF),A  (vdp_control)
# CHECK low: site 17263  OUT ($BE),A  (vdp_data)
# CHECK low: site 17269  OUT ($BE),A  (vdp_data)
# CHECK low: site 17677  OUT ($BF),A  (vdp_control)
# CHECK low: site 1767D  OUT ($BF),A  (vdp_control)
# CHECK low: site 17685  OUT ($BE),A  (vdp_data)
# CHECK low: site 1768C  OUT ($BE),A  (vdp_data)
# CHECK low: site 176A6  OUT ($BF),A  (vdp_control)
# CHECK low: site 176AC  OUT ($BF),A  (vdp_control)
# CHECK low: site 176B4  OUT ($BE),A  (vdp_data)
# CHECK low: site 176B9  OUT ($BE),A  (vdp_data)
# CHECK low: site 176C6  OUT ($BF),A  (vdp_control)
# CHECK low: site 176CA  OUT ($BF),A  (vdp_control)
# CHECK low: site 176D0  OUT ($BE),A  (vdp_data)
# CHECK low: site 176D7  OUT ($BE),A  (vdp_data)
# CHECK low: site 178B2  OUT ($BF),A  (vdp_control)
# CHECK low: site 178B6  OUT ($BF),A  (vdp_control)
# CHECK low: site 178BC  OUT ($BE),A  (vdp_data)
# CHECK low: site 178C3  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B252  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B258  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B263  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B269  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B677  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B67D  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B685  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B68C  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B6A6  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B6AC  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B6B4  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B6B9  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B6C6  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B6CA  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B6D0  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B6D7  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B8B2  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B8B6  OUT ($BF),A  (vdp_control)
# CHECK low: site 1B8BC  OUT ($BE),A  (vdp_data)
# CHECK low: site 1B8C3  OUT ($BE),A  (vdp_data)
# CHECK low: site 1C4C4  INIR  (port in C)
# CHECK low: site 1F252  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F258  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F263  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F269  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F677  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F67D  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F685  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F68C  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F6A6  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F6AC  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F6B4  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F6B9  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F6C6  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F6CA  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F6D0  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F6D7  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F8B2  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F8B6  OUT ($BF),A  (vdp_control)
# CHECK low: site 1F8BC  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F8C3  OUT ($BE),A  (vdp_data)
# CHECK low: site 23252  OUT ($BF),A  (vdp_control)
# CHECK low: site 23258  OUT ($BF),A  (vdp_control)
# CHECK low: site 23263  OUT ($BE),A  (vdp_data)
# CHECK low: site 23269  OUT ($BE),A  (vdp_data)
# CHECK low: site 23677  OUT ($BF),A  (vdp_control)
# CHECK low: site 2367D  OUT ($BF),A  (vdp_control)
# CHECK low: site 23685  OUT ($BE),A  (vdp_data)
# CHECK low: site 2368C  OUT ($BE),A  (vdp_data)
# CHECK low: site 236A6  OUT ($BF),A  (vdp_control)
# CHECK low: site 236AC  OUT ($BF),A  (vdp_control)
# CHECK low: site 236B4  OUT ($BE),A  (vdp_data)
# CHECK low: site 236B9  OUT ($BE),A  (vdp_data)
# CHECK low: site 236C6  OUT ($BF),A  (vdp_control)
# CHECK low: site 236CA  OUT ($BF),A  (vdp_control)
# CHECK low: site 236D0  OUT ($BE),A  (vdp_data)
# CHECK low: site 236D7  OUT ($BE),A  (vdp_data)
# CHECK low: site 238B2  OUT ($BF),A  (vdp_control)
# CHECK low: site 238B6  OUT ($BF),A  (vdp_control)
# CHECK low: site 238BC  OUT ($BE),A  (vdp_data)
# CHECK low: site 238C3  OUT ($BE),A  (vdp_data)
# CHECK low: site 27252  OUT ($BF),A  (vdp_control)
# CHECK low: site 27258  OUT ($BF),A  (vdp_control)
# CHECK low: site 27263  OUT ($BE),A  (vdp_data)
# CHECK low: site 27269  OUT ($BE),A  (vdp_data)
# CHECK low: site 27677  OUT ($BF),A  (vdp_control)
# CHECK low: site 2767D  OUT ($BF),A  (vdp_control)
# CHECK low: site 27685  OUT ($BE),A  (vdp_data)
# CHECK low: site 2768C  OUT ($BE),A  (vdp_data)
# CHECK low: site 276A6  OUT ($BF),A  (vdp_control)
# CHECK low: site 276AC  OUT ($BF),A  (vdp_control)
# CHECK low: site 276B4  OUT ($BE),A  (vdp_data)
# CHECK low: site 276B9  OUT ($BE),A  (vdp_data)
# CHECK low: site 276C6  OUT ($BF),A  (vdp_control)
# CHECK low: site 276CA  OUT ($BF),A  (vdp_control)
# CHECK low: site 276D0  OUT ($BE),A  (vdp_data)
# CHECK low: site 276D7  OUT ($BE),A  (vdp_data)
# CHECK low: site 278B2  OUT ($BF),A  (vdp_control)
# CHECK low: site 278B6  OUT ($BF),A  (vdp_control)
# CHECK low: site 278BC  OUT ($BE),A  (vdp_data)
# CHECK low: site 278C3  OUT ($BE),A  (vdp_data)
# CHECK low: site 34C5E  IN A,($C0)  (joypad_a)
# CHECK low: site 34C62  IN A,($C0)  (joypad_a)
# CHECK low: site 34CCA  IN A,($C0)  (joypad_a)
# CHECK low: site 3F5A0  IN A,($3F)  (unmapped_read)
# CHECK low: site 3F5A4  IN A,($3F)  (unmapped_read)
# CHECK low: site 3F860  IN C,(C)  (port in C)
# CHECK low: site 42A58  OUT ($3F),A  (io_control)
# CHECK low: site 4329B  IN A,($BD)  (vdp_status)
# CHECK low: site 48208  OUT ($3E),A  (memory_control)
# CHECK low: site 4FF50  IN A,($3F)  (unmapped_read)
# CHECK low: site 51F8E  IN A,($C0)  (joypad_a)
# CHECK low: site 52608  OUT ($3F),A  (io_control)
# CHECK low: site 53F50  IN A,($3F)  (unmapped_read)
# CHECK low: site 5907D  OUT ($C0),A  (no_effect)
# CHECK low: site 590D1  IN A,($C0)  (joypad_a)
# CHECK low: site 5C1A3  OUT ($C1),A  (no_effect)
# CHECK low: site 5C2C3  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 5CA13  OUT ($C1),A  (no_effect)
# CHECK low: site 5CB33  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 5D283  OUT ($C1),A  (no_effect)
# CHECK low: site 5D3A3  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 5DE53  OUT ($C1),A  (no_effect)
# CHECK low: site 5DF73  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 5ED83  OUT ($C1),A  (no_effect)
# CHECK low: site 5EEA3  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 62FE6  OUT ($F2),A  (fm_control)
# CHECK low: site 64786  OUT ($F2),A  (fm_control)
# LD ($FFFC-$FFFF),A stores in banks 0-1 that the draft missed (a byte scan for
# that store opcode with those addresses in $0000-$7FFF). Each follows a load of A from an immediate, an indexed or an absolute address,
# except 05657, the target of JP $5657 from $31FC, $3235, $377C and $37BF.
# 06CB2, 06D1F, 06D28 and 06D36 are the bank switches around the sine table
# at $8F4E in bank 15, which places the pods of the rotating ring in level 1.
mapst 03239   ; LD ($FFFF),A
mapst 03280   ; LD ($FFFF),A
mapst 0329E   ; LD ($FFFF),A
mapst 03306   ; LD ($FFFF),A
mapst 0333B   ; LD ($FFFF),A
mapst 0337A   ; LD ($FFFF),A
mapst 033D0   ; LD ($FFFF),A
mapst 0341E   ; LD ($FFFF),A
mapst 03469   ; LD ($FFFF),A
mapst 036BB   ; LD ($FFFF),A
mapst 03846   ; LD ($FFFF),A
mapst 0396E   ; LD ($FFFF),A
mapst 03A0E   ; LD ($FFFF),A
mapst 03A91   ; LD ($FFFF),A
mapst 04291   ; LD ($FFFF),A
mapst 042B1   ; LD ($FFFF),A
mapst 04317   ; LD ($FFFF),A
mapst 045AD   ; LD ($FFFF),A
mapst 046DA   ; LD ($FFFF),A
mapst 046FD   ; LD ($FFFF),A
mapst 04851   ; LD ($FFFF),A
mapst 048A7   ; LD ($FFFF),A
mapst 0497B   ; LD ($FFFF),A
mapst 04AD9   ; LD ($FFFF),A
mapst 04C63   ; LD ($FFFF),A
mapst 04F49   ; LD ($FFFF),A
mapst 04FB5   ; LD ($FFFF),A
mapst 04FBD   ; LD ($FFFF),A
mapst 04FCA   ; LD ($FFFF),A
mapst 04FD7   ; LD ($FFFF),A
mapst 04FE4   ; LD ($FFFF),A
mapst 054C4   ; LD ($FFFF),A
mapst 05541   ; LD ($FFFF),A
mapst 05560   ; LD ($FFFF),A
mapst 05657   ; LD ($FFFF),A
mapst 05697   ; LD ($FFFF),A
mapst 05914   ; LD ($FFFF),A
mapst 06543   ; LD ($FFFF),A
mapst 06560   ; LD ($FFFF),A
mapst 06571   ; LD ($FFFF),A
mapst 065A3   ; LD ($FFFF),A
mapst 065A9   ; LD ($FFFF),A
mapst 065D7   ; LD ($FFFF),A
mapst 0661D   ; LD ($FFFF),A
mapst 06634   ; LD ($FFFF),A
mapst 0663A   ; LD ($FFFF),A
mapst 06651   ; LD ($FFFF),A
mapst 06657   ; LD ($FFFF),A
mapst 06677   ; LD ($FFFF),A
mapst 0667D   ; LD ($FFFF),A
mapst 066C6   ; LD ($FFFF),A
mapst 066CC   ; LD ($FFFF),A
mapst 066E9   ; LD ($FFFF),A
mapst 066EF   ; LD ($FFFF),A
mapst 06708   ; LD ($FFFF),A
mapst 0670E   ; LD ($FFFF),A
mapst 06725   ; LD ($FFFF),A
mapst 0673A   ; LD ($FFFF),A
mapst 06762   ; LD ($FFFF),A
mapst 06BDC   ; LD ($FFFF),A
mapst 06C3A   ; LD ($FFFF),A
mapst 06C73   ; LD ($FFFF),A
mapst 06C8B   ; LD ($FFFF),A
mapst 06CB2   ; LD ($FFFF),A
mapst 06D1F   ; LD ($FFFF),A
mapst 06D28   ; LD ($FFFF),A
mapst 06D36   ; LD ($FFFF),A
# I/O instructions that the scanner finds in code that no recording ran, judged as code.
# Object handlers are reached through the pointer table at $202B, which the object spawn
# routine ($1E31, table read at $1E4D) indexes with the object type, and through handler
# addresses stored with LD (IX+$1E),n and LD (IX+$1F),n or passed in DE to a spawn routine.
# The dispatcher at $1DF3 jumps to the stored address.
# Stage cleared screen. $0CDA calls $1D15, which spawns object type $1E; the table entry
# for type $1E is $67F8, and its handler chain is $6826, $6924, $69D2, $6A11.
# $0197 writes one character of a number, $6AB1 writes a string (STAGE CLEARED,
# STAGE SCORE, TOTAL SCORE, SUPER STAGE CLEARED) with OUTI and OUT (C),A.
site 0019E   ; OUT ($BE),A
site 06AC0   ; OUTI
site 06AC7   ; OUT (C),A
# Object type $0E, handler $5604: reads name table rows back with INI and rewrites them.
# $01B6 sets the VRAM read address for it ($561D calls it).
site 001B8   ; OUT ($BF),A
site 001BB   ; OUT ($BF),A
site 05623   ; INI
site 05634   ; INI
site 05639   ; OUT ($BE),A
# Tile block writers. The routine at $02D8 is entered at $02F3 from $4854 and $48AA, and at
# $0307 from $592B. $4CA8 is called from $456A, $487F and $48F0, in the handler chain that
# starts at $44B2, which the type $1B handler at $432C spawns. $5657 is jumped to from $3234,
# which the type $33 handler at $31FE reaches with CALL $322C.
site 00319   ; OUT ($BE),A
site 0031F   ; OUT ($BE),A
site 04CC2   ; OUT ($BE),A
site 04CC8   ; OUT ($BE),A
site 0567F   ; OUT ($BE),A
site 05687   ; OUT ($BE),A
# Bank 4 module, update entry $8003 -> $84B3. $0CC9 runs it when $CC5C is 4 ($3843 stores 4).
# $86A0 clears a name table row, $873C reads name table rows back with IN A,($BE),
# $9F5E rewrites the name table with bit 4 cleared.
site 106A2   ; OUT ($BF),A
site 106A5   ; OUT ($BF),A
site 106AA   ; OUT ($BE),A
site 106B1   ; OUT ($BE),A
site 1074A   ; OUT ($BF),A
site 10750   ; OUT ($BF),A
site 10757   ; IN A,($BE)
site 1075D   ; IN A,($BE)
site 11F66   ; OUT ($BF),A
site 11F69   ; OUT ($BF),A
site 11F6D   ; IN A,($BE)
site 11F74   ; OUT ($BF),A
site 11F79   ; OUT ($BF),A
site 11F7C   ; OUT ($BE),A
# Bank 5 module. $CC5C is 5 after the type $1A handler ($4314); $0CC9 runs its update entry
# $8003 -> $AD43, and $431A runs its first entry $8000 -> $AD33, which calls $B6C3.
site 17252   ; OUT ($BF),A
site 17258   ; OUT ($BF),A
site 17263   ; OUT ($BE),A
site 17269   ; OUT ($BE),A
site 17677   ; OUT ($BF),A
site 1767D   ; OUT ($BF),A
site 17685   ; OUT ($BE),A
site 1768C   ; OUT ($BE),A
site 176A6   ; OUT ($BF),A
site 176AC   ; OUT ($BF),A
site 176B4   ; OUT ($BE),A
site 176B9   ; OUT ($BE),A
site 176C6   ; OUT ($BF),A
site 176CA   ; OUT ($BF),A
site 176D0   ; OUT ($BE),A
site 176D7   ; OUT ($BE),A
