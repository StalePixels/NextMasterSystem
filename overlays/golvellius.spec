# Golvellius - Valley of Doom (USA, Europe, Brazil) (En), CRC32 A51376FE, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (start presses, then
# random input; start presses, then walking in the first screen), plus these routine starts
# given with --entry, because no scanned path or recording reached them: bank 0 $0042, $0177,
# $0182, $0198, $01E4, $0321, $0333, $0342, $0356 (the VDP and joypad helpers), $16E0, $2EDF,
# $2F06, $0918 and $0A19 (the unrolled OUTD and OUTI/OUTD runs of the sprite table upload);
# bank 7 $8049, $82A2, $8312, $83B6, $956A.
# The frame handler $05F6 does the VDP work of a game frame when the main loop has set $C00B.
# Spec gaps (data/scan-verdicts.tsv): false are a byte table in bank 0, an address table in
# bank 2 and graphics in banks 5, 10, 11, 13 and 15.
name Golvellius
cart A51376FE
hz any		; No-Intro regions USA, Europe, Brazil
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
asm 00406 2   ; IM 1 -> IM 2
    im 2
endasm
site 00039   ; IN A,($BF)
site 00042   ; IN A,($BF)
site 0004B   ; OUT ($BF),A
site 00050   ; OUT ($BF),A
site 00085   ; OTIR
site 000A3   ; OUT ($3F),A
site 000A5   ; IN A,($DD)
site 000AF   ; OUT ($3F),A
site 000B1   ; IN A,($DD)
site 000BA   ; OUT ($3F),A
site 000C8   ; OUT ($3E),A
site 000D0   ; OUT ($F2),A
site 000D3   ; IN A,($F2)
site 000E5   ; OUT ($F2),A
site 000ED   ; OUT ($3E),A
site 000F6   ; IN A,($BF)
site 000FC   ; IN A,($BF)
site 00103   ; IN A,($BF)
site 00115   ; IN A,($BF)
site 0012A   ; OUTI
site 0012C   ; OUT ($BF),A
site 00133   ; OUT ($BF),A
site 00137   ; OUT ($BF),A
site 0013F   ; OUT ($BE),A
site 00147   ; OUT ($BF),A
site 0014B   ; OUT ($BF),A
site 0014F   ; OUT ($BE),A
site 0017E   ; IN A,($BE)
site 00189   ; IN A,($BE)
site 00194   ; OUT ($BE),A
site 0019F   ; OUT ($BE),A
site 001A5   ; OUT ($BF),A
site 001AA   ; OUT ($BF),A
site 001B0   ; OUT ($BF),A
site 001B5   ; OUT ($BF),A
site 001BB   ; OUT ($BF),A
site 001C0   ; OUT ($BF),A
site 001C6   ; OUT ($BF),A
site 001CB   ; OUT ($BF),A
site 001D9   ; OUT ($BE),A
site 001EB   ; IN A,($BE)
site 001FE   ; OUT ($BE),A
site 0021F   ; OUT (C),H
site 00224   ; OUT (C),L
site 00271   ; IN A,($BE)
site 00276   ; IN A,($BE)
site 0027B   ; OUT ($BE),A
site 00283   ; OUT ($BE),A
site 0029A   ; OUT ($BE),A
site 002A0   ; OUT ($BE),A
site 002EF   ; OUT ($BE),A
site 002F7   ; OUT ($BE),A
site 00321   ; OUT ($BE),A
site 00326   ; OUT ($DF),A
site 0032A   ; OUT ($DE),A
site 0032D   ; IN A,($DC)
site 00333   ; IN A,($DC)
site 00336   ; IN A,($DD)
site 00351   ; OTIR
site 0035B   ; OUT ($BE),A
site 00375   ; OUTI
site 00378   ; IN A,($BE)
site 00384   ; OUT (C),A
site 00387   ; IN A,($BE)
site 003A9   ; OUTI
site 003AE   ; IN A,($BE)
site 003B3   ; IN A,($BE)
site 003B8   ; IN A,($BE)
site 003C7   ; OUT (C),A
site 003CC   ; IN A,($BE)
site 003D1   ; IN A,($BE)
site 003D6   ; IN A,($BE)
site 0060F   ; IN A,($DD)
site 0064A   ; OUT ($BF),A
site 0064E   ; OUT ($BF),A
site 00769   ; OUT (C),E
site 0076B   ; OUT (C),D
site 0076F   ; OUTI
site 00771   ; OUTI
site 00773   ; OUTI
site 00775   ; OUTI
site 00777   ; OUTI
site 00779   ; OUTI
site 0077B   ; OUTI
site 0077D   ; OUTI
site 0077F   ; OUTI
site 00781   ; OUTI
site 00783   ; OUTI
site 00785   ; OUTI
site 00787   ; OUTI
site 00789   ; OUTI
site 0078B   ; OUTI
site 0078D   ; OUTI
site 00817   ; OUTI
site 00819   ; OUTI
site 0081B   ; OUTI
site 0081D   ; OUTI
site 0081F   ; OUTI
site 00821   ; OUTI
site 00823   ; OUTI
site 00825   ; OUTI
site 00827   ; OUTI
site 00829   ; OUTI
site 0082B   ; OUTI
site 0082D   ; OUTI
site 0082F   ; OUTI
site 00831   ; OUTI
site 00833   ; OUTI
site 00835   ; OUTI
site 00837   ; OUTI
site 00839   ; OUTI
site 0083B   ; OUTI
site 0083D   ; OUTI
site 0083F   ; OUTI
site 00841   ; OUTI
site 00843   ; OUTI
site 00845   ; OUTI
site 00847   ; OUTI
site 00849   ; OUTI
site 0084B   ; OUTI
site 0084D   ; OUTI
site 0084F   ; OUTI
site 00851   ; OUTI
site 00853   ; OUTI
site 00855   ; OUTI
site 00857   ; OUTI
site 00859   ; OUTI
site 0085B   ; OUTI
site 0085D   ; OUTI
site 0085F   ; OUTI
site 00861   ; OUTI
site 00863   ; OUTI
site 00865   ; OUTI
site 00867   ; OUTI
site 00869   ; OUTI
site 0086B   ; OUTI
site 0086D   ; OUTI
site 0086F   ; OUTI
site 00871   ; OUTI
site 00873   ; OUTI
site 00875   ; OUTI
site 00877   ; OUTI
site 00879   ; OUTI
site 0087B   ; OUTI
site 0087D   ; OUTI
site 0087F   ; OUTI
site 00881   ; OUTI
site 00883   ; OUTI
site 00885   ; OUTI
site 00887   ; OUTI
site 00889   ; OUTI
site 0088B   ; OUTI
site 0088D   ; OUTI
site 0088F   ; OUTI
site 00891   ; OUTI
site 00893   ; OUTI
site 00895   ; OUTI
site 00897   ; OUTI
site 00899   ; OUTI
site 0089B   ; OUTI
site 0089D   ; OUTI
site 0089F   ; OUTI
site 008A1   ; OUTI
site 008A3   ; OUTI
site 008A5   ; OUTI
site 008A7   ; OUTI
site 008A9   ; OUTI
site 008AB   ; OUTI
site 008AD   ; OUTI
site 008AF   ; OUTI
site 008B1   ; OUTI
site 008B3   ; OUTI
site 008B5   ; OUTI
site 008B7   ; OUTI
site 008B9   ; OUTI
site 008BB   ; OUTI
site 008BD   ; OUTI
site 008BF   ; OUTI
site 008C1   ; OUTI
site 008C3   ; OUTI
site 008C5   ; OUTI
site 008C7   ; OUTI
site 008C9   ; OUTI
site 008CB   ; OUTI
site 008CD   ; OUTI
site 008CF   ; OUTI
site 008D1   ; OUTI
site 008D3   ; OUTI
site 008D5   ; OUTI
site 008D7   ; OUTI
site 008D9   ; OUTI
site 008DB   ; OUTI
site 008DD   ; OUTI
site 008DF   ; OUTI
site 008E1   ; OUTI
site 008E3   ; OUTI
site 008E5   ; OUTI
site 008E7   ; OUTI
site 008E9   ; OUTI
site 008EB   ; OUTI
site 008ED   ; OUTI
site 008EF   ; OUTI
site 008F1   ; OUTI
site 008F3   ; OUTI
site 008F5   ; OUTI
site 008F7   ; OUTI
site 008F9   ; OUTI
site 008FB   ; OUTI
site 008FD   ; OUTI
site 008FF   ; OUTI
site 00901   ; OUTI
site 00903   ; OUTI
site 00905   ; OUTI
site 00907   ; OUTI
site 00909   ; OUTI
site 0090B   ; OUTI
site 0090D   ; OUTI
site 0090F   ; OUTI
site 00911   ; OUTI
site 00913   ; OUTI
site 00915   ; OUTI
site 00918   ; OUTD
site 0091A   ; OUTD
site 0091C   ; OUTD
site 0091E   ; OUTD
site 00920   ; OUTD
site 00922   ; OUTD
site 00924   ; OUTD
site 00926   ; OUTD
site 00928   ; OUTD
site 0092A   ; OUTD
site 0092C   ; OUTD
site 0092E   ; OUTD
site 00930   ; OUTD
site 00932   ; OUTD
site 00934   ; OUTD
site 00936   ; OUTD
site 00938   ; OUTD
site 0093A   ; OUTD
site 0093C   ; OUTD
site 0093E   ; OUTD
site 00940   ; OUTD
site 00942   ; OUTD
site 00944   ; OUTD
site 00946   ; OUTD
site 00948   ; OUTD
site 0094A   ; OUTD
site 0094C   ; OUTD
site 0094E   ; OUTD
site 00950   ; OUTD
site 00952   ; OUTD
site 00954   ; OUTD
site 00956   ; OUTD
site 00958   ; OUTD
site 0095A   ; OUTD
site 0095C   ; OUTD
site 0095E   ; OUTD
site 00960   ; OUTD
site 00962   ; OUTD
site 00964   ; OUTD
site 00966   ; OUTD
site 00968   ; OUTD
site 0096A   ; OUTD
site 0096C   ; OUTD
site 0096E   ; OUTD
site 00970   ; OUTD
site 00972   ; OUTD
site 00974   ; OUTD
site 00976   ; OUTD
site 00978   ; OUTD
site 0097A   ; OUTD
site 0097C   ; OUTD
site 0097E   ; OUTD
site 00980   ; OUTD
site 00982   ; OUTD
site 00984   ; OUTD
site 00986   ; OUTD
site 00988   ; OUTD
site 0098A   ; OUTD
site 0098C   ; OUTD
site 0098E   ; OUTD
site 00990   ; OUTD
site 00992   ; OUTD
site 00994   ; OUTD
site 00996   ; OUTD
site 00998   ; OUTD
site 0099A   ; OUTD
site 0099C   ; OUTD
site 0099E   ; OUTD
site 009A0   ; OUTD
site 009A2   ; OUTD
site 009A4   ; OUTD
site 009A6   ; OUTD
site 009A8   ; OUTD
site 009AA   ; OUTD
site 009AC   ; OUTD
site 009AE   ; OUTD
site 009B0   ; OUTD
site 009B2   ; OUTD
site 009B4   ; OUTD
site 009B6   ; OUTD
site 009B8   ; OUTD
site 009BA   ; OUTD
site 009BC   ; OUTD
site 009BE   ; OUTD
site 009C0   ; OUTD
site 009C2   ; OUTD
site 009C4   ; OUTD
site 009C6   ; OUTD
site 009C8   ; OUTD
site 009CA   ; OUTD
site 009CC   ; OUTD
site 009CE   ; OUTD
site 009D0   ; OUTD
site 009D2   ; OUTD
site 009D4   ; OUTD
site 009D6   ; OUTD
site 009D8   ; OUTD
site 009DA   ; OUTD
site 009DC   ; OUTD
site 009DE   ; OUTD
site 009E0   ; OUTD
site 009E2   ; OUTD
site 009E4   ; OUTD
site 009E6   ; OUTD
site 009E8   ; OUTD
site 009EA   ; OUTD
site 009EC   ; OUTD
site 009EE   ; OUTD
site 009F0   ; OUTD
site 009F2   ; OUTD
site 009F4   ; OUTD
site 009F6   ; OUTD
site 009F8   ; OUTD
site 009FA   ; OUTD
site 009FC   ; OUTD
site 009FE   ; OUTD
site 00A00   ; OUTD
site 00A02   ; OUTD
site 00A04   ; OUTD
site 00A06   ; OUTD
site 00A08   ; OUTD
site 00A0A   ; OUTD
site 00A0C   ; OUTD
site 00A0E   ; OUTD
site 00A10   ; OUTD
site 00A12   ; OUTD
site 00A14   ; OUTD
site 00A16   ; OUTD
site 00A19   ; OUTI
site 00A1B   ; OUTD
site 00A1F   ; OUTI
site 00A21   ; OUTD
site 00A25   ; OUTI
site 00A27   ; OUTD
site 00A2B   ; OUTI
site 00A2D   ; OUTD
site 00A31   ; OUTI
site 00A33   ; OUTD
site 00A37   ; OUTI
site 00A39   ; OUTD
site 00A3D   ; OUTI
site 00A3F   ; OUTD
site 00A43   ; OUTI
site 00A45   ; OUTD
site 00A49   ; OUTI
site 00A4B   ; OUTD
site 00A4F   ; OUTI
site 00A51   ; OUTD
site 00A55   ; OUTI
site 00A57   ; OUTD
site 00A5B   ; OUTI
site 00A5D   ; OUTD
site 00A61   ; OUTI
site 00A63   ; OUTD
site 00A67   ; OUTI
site 00A69   ; OUTD
site 00A6D   ; OUTI
site 00A6F   ; OUTD
site 00A73   ; OUTI
site 00A75   ; OUTD
site 00A79   ; OUTI
site 00A7B   ; OUTD
site 00A7F   ; OUTI
site 00A81   ; OUTD
site 00A85   ; OUTI
site 00A87   ; OUTD
site 00A8B   ; OUTI
site 00A8D   ; OUTD
site 00A91   ; OUTI
site 00A93   ; OUTD
site 00A97   ; OUTI
site 00A99   ; OUTD
site 00A9D   ; OUTI
site 00A9F   ; OUTD
site 00AA3   ; OUTI
site 00AA5   ; OUTD
site 00AA9   ; OUTI
site 00AAB   ; OUTD
site 00AAF   ; OUTI
site 00AB1   ; OUTD
site 00AB5   ; OUTI
site 00AB7   ; OUTD
site 00ABB   ; OUTI
site 00ABD   ; OUTD
site 00AC1   ; OUTI
site 00AC3   ; OUTD
site 00AC7   ; OUTI
site 00AC9   ; OUTD
site 00ACD   ; OUTI
site 00ACF   ; OUTD
site 00AD3   ; OUTI
site 00AD5   ; OUTD
site 00AD9   ; OUTI
site 00ADB   ; OUTD
site 00ADF   ; OUTI
site 00AE1   ; OUTD
site 00AE5   ; OUTI
site 00AE7   ; OUTD
site 00AEB   ; OUTI
site 00AED   ; OUTD
site 00AF1   ; OUTI
site 00AF3   ; OUTD
site 00AF7   ; OUTI
site 00AF9   ; OUTD
site 00AFD   ; OUTI
site 00AFF   ; OUTD
site 00B03   ; OUTI
site 00B05   ; OUTD
site 00B09   ; OUTI
site 00B0B   ; OUTD
site 00B0F   ; OUTI
site 00B11   ; OUTD
site 00B15   ; OUTI
site 00B17   ; OUTD
site 00B1B   ; OUTI
site 00B1D   ; OUTD
site 00B21   ; OUTI
site 00B23   ; OUTD
site 00B27   ; OUTI
site 00B29   ; OUTD
site 00B2D   ; OUTI
site 00B2F   ; OUTD
site 00B33   ; OUTI
site 00B35   ; OUTD
site 00B39   ; OUTI
site 00B3B   ; OUTD
site 00B3F   ; OUTI
site 00B41   ; OUTD
site 00B45   ; OUTI
site 00B47   ; OUTD
site 00B4B   ; OUTI
site 00B4D   ; OUTD
site 00B51   ; OUTI
site 00B53   ; OUTD
site 00B57   ; OUTI
site 00B59   ; OUTD
site 00B5D   ; OUTI
site 00B5F   ; OUTD
site 00B63   ; OUTI
site 00B65   ; OUTD
site 00B69   ; OUTI
site 00B6B   ; OUTD
site 00B6F   ; OUTI
site 00B71   ; OUTD
site 00B75   ; OUTI
site 00B77   ; OUTD
site 00B7B   ; OUTI
site 00B7D   ; OUTD
site 00B81   ; OUTI
site 00B83   ; OUTD
site 00B87   ; OUTI
site 00B89   ; OUTD
site 00B8D   ; OUTI
site 00B8F   ; OUTD
site 00B93   ; OUTI
site 00B95   ; OUTD
site 00B99   ; OUTI
site 00B9B   ; OUTD
site 00B9F   ; OUTI
site 00BA1   ; OUTD
site 00BA5   ; OUTI
site 00BA7   ; OUTD
site 00BAB   ; OUTI
site 00BAD   ; OUTD
site 00BB1   ; OUTI
site 00BB3   ; OUTD
site 00BB7   ; OUTI
site 00BB9   ; OUTD
site 00BBD   ; OUTI
site 00BBF   ; OUTD
site 00BC3   ; OUTI
site 00BC5   ; OUTD
site 00BC9   ; OUTI
site 00BCB   ; OUTD
site 00BCF   ; OUTI
site 00BD1   ; OUTD
site 00BD5   ; OUTI
site 00BD7   ; OUTD
site 00BDB   ; OUTI
site 00BDD   ; OUTD
site 00BE1   ; OUTI
site 00BE3   ; OUTD
site 00BE7   ; OUTI
site 00BE9   ; OUTD
site 00BED   ; OUTI
site 00BEF   ; OUTD
site 00BF3   ; OUTI
site 00BF5   ; OUTD
site 00BF9   ; OUTI
site 00BFB   ; OUTD
site 00BFF   ; OUTI
site 00C01   ; OUTD
site 00C05   ; OUTI
site 00C07   ; OUTD
site 00C0B   ; OUTI
site 00C0D   ; OUTD
site 00C11   ; OUTI
site 00C13   ; OUTD
site 00C17   ; OUTI
site 00C19   ; OUTD
site 00C1D   ; OUTI
site 00C1F   ; OUTD
site 00C23   ; OUTI
site 00C25   ; OUTD
site 00C29   ; OUTI
site 00C2B   ; OUTD
site 00C2F   ; OUTI
site 00C31   ; OUTD
site 00C35   ; OUTI
site 00C37   ; OUTD
site 00C3B   ; OUTI
site 00C3D   ; OUTD
site 00C41   ; OUTI
site 00C43   ; OUTD
site 00C47   ; OUTI
site 00C49   ; OUTD
site 00C4D   ; OUTI
site 00C4F   ; OUTD
site 00C53   ; OUTI
site 00C55   ; OUTD
site 00C59   ; OUTI
site 00C5B   ; OUTD
site 00C5F   ; OUTI
site 00C61   ; OUTD
site 00C65   ; OUTI
site 00C67   ; OUTD
site 00C6B   ; OUTI
site 00C6D   ; OUTD
site 00C71   ; OUTI
site 00C73   ; OUTD
site 00C77   ; OUTI
site 00C79   ; OUTD
site 00C7D   ; OUTI
site 00C7F   ; OUTD
site 00C83   ; OUTI
site 00C85   ; OUTD
site 00C89   ; OUTI
site 00C8B   ; OUTD
site 00C8F   ; OUTI
site 00C91   ; OUTD
site 00C95   ; OUTI
site 00C97   ; OUTD
site 00C9B   ; OUTI
site 00C9D   ; OUTD
site 00CA1   ; OUTI
site 00CA3   ; OUTD
site 00CA7   ; OUTI
site 00CA9   ; OUTD
site 00CAD   ; OUTI
site 00CAF   ; OUTD
site 00CB3   ; OUTI
site 00CB5   ; OUTD
site 00CB9   ; OUTI
site 00CBB   ; OUTD
site 00CBF   ; OUTI
site 00CC1   ; OUTD
site 00CC5   ; OUTI
site 00CC7   ; OUTD
site 00CCB   ; OUTI
site 00CCD   ; OUTD
site 00CD1   ; OUTI
site 00CD3   ; OUTD
site 00CD7   ; OUTI
site 00CD9   ; OUTD
site 00CDD   ; OUTI
site 00CDF   ; OUTD
site 00CE3   ; OUTI
site 00CE5   ; OUTD
site 00CE9   ; OUTI
site 00CEB   ; OUTD
site 00CEF   ; OUTI
site 00CF1   ; OUTD
site 00CF5   ; OUTI
site 00CF7   ; OUTD
site 00CFB   ; OUTI
site 00CFD   ; OUTD
site 00D01   ; OUTI
site 00D03   ; OUTD
site 00D07   ; OUTI
site 00D09   ; OUTD
site 00D0D   ; OUTI
site 00D0F   ; OUTD
site 00D13   ; OUTI
site 00D15   ; OUTD
site 01026   ; OUT ($BF),A
site 01029   ; OUT ($BF),A
site 0102C   ; OUT (C),A
site 01032   ; OUT (C),A
site 016F9   ; OUT ($BF),A
site 016FC   ; OUT ($BF),A
site 016FF   ; OUT ($BE),A
site 01704   ; OUT ($BE),A
site 0247B   ; OUT ($BE),A
site 02481   ; OUT ($BE),A
site 02508   ; OUT ($BF),A
site 0250D   ; OUT ($BF),A
site 025D3   ; OUT ($BE),A
site 02EEA   ; OUT ($BE),A
site 02EF3   ; OUT ($BE),A
site 02F22   ; OUT ($BE),A
site 02F29   ; OUT ($BE),A
site 038C6   ; OUT ($BE),A
site 038CC   ; OUT ($BE),A
site 0393E   ; OUT ($BE),A
site 03942   ; OUT ($BE),A
site 03978   ; OUT ($BE),A
site 0397C   ; OUT ($BE),A
site 06F31   ; OUT ($F0),A
site 06F39   ; OUT ($F1),A
site 06F4B   ; OUT ($F1),A
site 06F5F   ; OUT ($F0),A
site 06F66   ; OUT ($F1),A
site 06F6D   ; OUT ($F1),A
site 06F80   ; OUT ($F0),A
site 06F83   ; OUT ($F1),A
site 06F95   ; OUT ($F0),A
site 06F9A   ; OUT ($F1),A
site 06FAC   ; OUT ($F1),A
site 06FC0   ; OUT ($F0),A
site 06FC3   ; OUT ($F1),A
site 06FE5   ; OUT ($F0),A
site 06FE8   ; OUT ($F1),A
site 06FFD   ; OUT ($7F),A
site 07003   ; OUT ($7F),A
site 0700F   ; OUT ($7F),A
site 0702C   ; OUT ($7F),A
site 07035   ; OUT ($7F),A
site 07721   ; OUT ($F0),A
site 07724   ; OUT ($F1),A
site 07733   ; OUT ($F0),A
site 07737   ; OUT ($F1),A
site 0774C   ; OUT ($F0),A
site 0774F   ; OUT ($F1),A
site 0776A   ; OUT ($F2),A
site 1C05E   ; OUT ($BE),A
site 1C091   ; OUT ($BE),A
site 1C095   ; OUT ($BE),A
site 1C273   ; OUT ($BE),A
site 1C27C   ; OUT ($BE),A
site 1C2A6   ; IN A,($BE)
site 1C2AC   ; IN A,($BE)
site 1C2B3   ; OUT ($BE),A
site 1C2B9   ; OUT ($BE),A
site 1C319   ; OUT ($BE),A
site 1C354   ; OUT ($BE),A
site 1C35A   ; OUT ($BE),A
site 1C36F   ; OUT ($BE),A
site 1C374   ; OUT ($BE),A
site 1C3BE   ; OUT ($BE),A
site 1C3C3   ; OUT ($BE),A
site 1C5EB   ; OUT ($BE),A
site 1C5EF   ; OUT ($BE),A
site 1C765   ; OUT ($BE),A
site 1C770   ; OUT ($BE),A
site 1C7C2   ; OUT ($BE),A
site 1CED8   ; OUT ($BE),A
site 1CEDE   ; OUT ($BE),A
site 1CEF5   ; OUT ($BE),A
site 1CEFC   ; OUT ($BE),A
site 1CFB2   ; OUT ($BE),A
site 1CFB7   ; OUT ($BE),A
site 1CFE1   ; OUT ($BE),A
site 1CFE5   ; OUT ($BE),A
site 1D316   ; OUT ($BE),A
site 1D31C   ; OUT ($BE),A
site 1D4FC   ; OUT ($BE),A
site 1D501   ; OUT ($BE),A
site 1D542   ; OUT ($BE),A
site 1D547   ; OUT ($BE),A
site 1D576   ; OUT ($BE),A
site 1D57B   ; OUT ($BE),A
# Sprite table upload $0651-$0717 in the frame handler, as native code in page 0 (entry sat).
# The game rotates its 64 sprites by one place every second frame, counted at $C83A, and
# reverses their order on odd counts, so that sprites past 8 on a line take turns. It
# writes the Y table ($C980, 64 bytes) to VRAM $3F00 and the X and tile pairs ($C900,
# 128 bytes) to $3F80 with computed entries into unrolled OUTI and OUTD runs ($0817-$0D18).
# Through the traps that took about 200,000 Next cycles a frame and could run past the
# once-a-frame sprite work, which then took new Y values with old X and tile values, and
# Kelesis was not shown in about half of the frames.
asm 00651 199  ; LD A,$00; OUT ($BF),A ... up to $0718
    rst $00
    db far_io, pg_sat, ent_sat
    jp $0718
endasm
page 0 sat
; sat: does what the game's code at $0651-$0717 does. With n = ($C83A), then ($C83A) = n + 1
; and r = (n AND $7E) / 2, sprite i of the table written is sprite (r + i) AND 63 of the
; game's lists for an even n, and sprite (r - 1 - i) AND 63 for an odd n. The Y values go to
; VRAM $3F00 (64 bytes), the X and tile pairs to $3F80 (128 bytes). The VDP is left as the
; game's writes leave it: address $0000 after the last byte, a VRAM write. The registers that
; the game's code changes are not used after $0718: the frame handler sets each one before use.
; Runs on its own stack, with interrupts as the game has them (off, in the frame handler).
; Runtime entries used: jt_vwrite.
sat:    ld (sv_sp),sp
        ld sp,pstk
        push ix
        push iy
        ld hl,$C83A
        ld a,(hl)
        inc (hl)
        ld c,a                  ; C = n
        and $7E
        rrca
        ld e,a                  ; E = r
        ld ix,ybuf
        ld iy,xbuf
        ld b,64
        bit 0,c
        jr nz,.odd
.even:  ld a,e                  ; sprite r + i
        call put
        inc e
        djnz .even
        jr .send
.odd:   dec e                   ; sprite r - 1 - i
        ld a,e
        call put
        djnz .odd
.send:  ld hl,ybuf
        ld de,$3F00
        ld bc,$4001             ; 64 bytes, one run
        ld ix,64
        ld iy,64
        ld a,1                  ; the source as mapped now: the buffers are in this page
        call jt_vwrite
        ld hl,xbuf
        ld de,$3F80
        ld bc,$8001             ; 128 bytes, one run
        ld ix,128
        ld iy,128
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        ld sp,(sv_sp)
        ret

; put: copy sprite A AND 63 of the game's lists to (IX) (Y) and (IY) (X, tile), then step
; IX by 1 and IY by 2. Keeps BC, DE.
put:    and 63
        ld l,a
        ld h,$C9
        set 7,l                 ; $C980 + s
        ld a,(hl)
        ld (ix+0),a
        inc ix
        res 7,l
        sla l                   ; $C900 + 2s
        ld a,(hl)
        ld (iy+0),a
        inc l
        ld a,(hl)
        ld (iy+1),a
        inc iy
        inc iy
        ret

sv_sp:  dw 0
ybuf:   ds 64
xbuf:   ds 128
        ds 64
pstk:
endpage
mapldk 00003   # LD HL,$FFFC; LD (HL),$00
maphl 00009   # LD (HL),$00, HL = $FFFD
maphl 0000C   # LD (HL),$01, HL = $FFFE
maphl 0000F   # LD (HL),$02, HL = $FFFF
mapst 0041C   ; LD ($FFFF),A
mapst 00798   ; LD ($FFFF),A
mapst 0079F   ; LD ($FFFF),A
mapst 00E12   ; LD ($FFFF),A
mapst 00E28   ; LD ($FFFF),A
mapst 00E30   ; LD ($FFFF),A
mapst 00F4E   ; LD ($FFFF),A
mapst 019EB   ; LD ($FFFF),A
mapst 01CAD   ; LD ($FFFF),A
mapst 01CB5   ; LD ($FFFF),A
mapst 01DB4   ; LD ($FFFF),A
mapst 01DFB   ; LD ($FFFF),A
mapst 01EA5   ; LD ($FFFF),A
mapst 01FDE   ; LD ($FFFF),A
mapst 020CA   ; LD ($FFFF),A
mapst 025E5   ; LD ($FFFF),A
mapst 027A6   ; LD ($FFFF),A
mapst 027E0   ; LD ($FFFF),A
mapst 02904   ; LD ($FFFF),A
mapst 02952   ; LD ($FFFF),A
mapst 033FA   ; LD ($FFFF),A
mapst 041BA   ; LD ($FFFF),A
mapst 04213   ; LD ($FFFF),A
mapst 04356   ; LD ($FFFF),A
mapst 0457C   ; LD ($FFFF),A
mapst 0476A   ; LD ($FFFF),A
mapst 047BB   ; LD ($FFFF),A
mapst 0489A   ; LD ($FFFF),A
mapst 04967   ; LD ($FFFF),A
mapst 04A93   ; LD ($FFFF),A
mapst 04B0F   ; LD ($FFFF),A
mapst 04C45   ; LD ($FFFF),A
mapst 04CAB   ; LD ($FFFF),A
mapst 04DCF   ; LD ($FFFF),A
mapst 04DDE   ; LD ($FFFF),A
mapst 0654D   ; LD ($FFFF),A
mapst 066B1   ; LD ($FFFF),A
mapst 06A86   ; LD ($FFFF),A
mapst 06C53   ; LD ($FFFF),A
mapst 06D53   ; LD ($FFFF),A
mapst 07ABA   ; LD ($FFFF),A
mapst 07B3B   ; LD ($FFFF),A
mapst 07B4F   ; LD ($FFFF),A
mapst 07C72   ; LD ($FFFF),A
mapst 07CA1   ; LD ($FFFF),A
mapst 07CD7   ; LD ($FFFF),A
mapst 07D19   ; LD ($FFFF),A
mapst 07D56   ; LD ($FFFF),A
mapst 07D67   ; LD ($FFFF),A
mapst 07DB1   ; LD ($FFFF),A
# CHECK cartarea_store at 03D0C ($3D0C bank 0): 77  LD (HL),A $3D0C
# CHECK indirect_unresolved at 00428 ($0428 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 00679 ($0679 bank 0): C9  RET 
# CHECK indirect_unresolved at 0068B ($068B bank 0): C9  RET 
# CHECK indirect_unresolved at 006A7 ($06A7 bank 0): C9  RET 
# CHECK indirect_unresolved at 006BB ($06BB bank 0): C9  RET 
# CHECK indirect_unresolved at 006D3 ($06D3 bank 0): C9  RET 
# CHECK indirect_unresolved at 00705 ($0705 bank 0): C9  RET 
# CHECK indirect_unresolved at 0133E ($133E bank 0): C9  RET 
# CHECK indirect_unresolved at 0136C ($136C bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 01508 ($1508 bank 0): D8  RET C 
# CHECK indirect_unresolved at 01F14 ($1F14 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 01F8D ($1F8D bank 0): C8  RET Z 
# CHECK indirect_unresolved at 01FBA ($1FBA bank 0): C9  RET 
# CHECK indirect_unresolved at 02148 ($2148 bank 0): C9  RET 
# CHECK indirect_unresolved at 027F7 ($27F7 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 02999 ($2999 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 03D6A ($3D6A bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 0526D ($526D bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 05273 ($5273 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 0527D ($527D bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 05286 ($5286 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 05C27 ($5C27 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 077C8 ($77C8 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 07810 ($7810 bank 1): E9  JP (HL) 
# Mapper stores found by the byte scan in bytes no path reached:
# CHECK byte scan low: mapst 342D3  LD ($FFFF),A  (12 bytes of valid code before it; no valid code after it)
# CHECK byte scan low: mapst 36B02  LD ($FFFF),A  (no evidence)
# CHECK medium: site 01A7E  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK medium: site 08365  OTDR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 16DF7  OTDR  (port in C; branch target from $16E12)
# CHECK low: site 16DF9  IN A,($7E)  (v_counter; no evidence)
# CHECK low: site 19236  IN A,($7E)  (v_counter; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 19FB4  IN A,($BD)  (vdp_status; no valid code after it)
# CHECK low: site 1A49A  IN A,($BF)  (vdp_status; no evidence)
# CHECK low: site 1A964  IN A,($3F)  (unmapped_read; no valid code after it)
# CHECK low: site 1AD96  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 2451B  IN A,($7E)  (v_counter; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2451F  IN A,($7E)  (v_counter; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 263DA  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 2A439  IN A,($DD)  (joypad_b_misc; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 2A982  IN A,($DC)  (joypad_a; 32 bytes of valid code before it)
# CHECK high: site 2AE46  IN A,($DC)  (joypad_a; branch target from $2AE2C; 16 bytes of valid code before it)
# CHECK medium: site 2F029  OUT ($BF),A  (vdp_control; branch target from $2F017)
# CHECK low: site 31E49  IN A,($BD)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 29 bytes of valid code before it)
# CHECK low: site 342E2  IN A,($7F)  (h_counter; 27 bytes of valid code before it; no valid code after it)
# CHECK low: site 342F2  IN A,($7F)  (h_counter; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 35093  IN A,($DD)  (joypad_b_misc; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 359E1  OUT ($F0),A  (fm_address; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 35B24  IN A,($3F)  (unmapped_read; 32 bytes of valid code before it)
# CHECK high: site 35FFD  IN A,($BF)  (vdp_status; branch target from $34174; 16 bytes of valid code before it)
# CHECK low: site 36261  IN A,($BF)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 16 bytes of valid code before it)
# CHECK medium: site 36299  IN A,($3F)  (unmapped_read; 32 bytes of valid code before it)
# CHECK low: site 372D8  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 38E03  IN B,(C)  (port in C; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3B8CE  IN A,($BF)  (vdp_status; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 3C956  OUT ($DC),A  (no_effect; 32 bytes of valid code before it)
# CHECK low: site 3D311  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 3DFE8  OUT ($C0),A  (no_effect; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3E767  IN A,($DC)  (joypad_a; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)

# Golvellius - Valley of Doom (USA, Europe, Brazil).cht, "Always Have "Red Squid" (Infinite
# Health)": RAM $C836 is the Red Squid count; the game uses it to revive the player at 0 power
poke "Infinite lives"
ar 00C8-3601
endpoke

# Golvellius - Valley of Doom (USA, Europe, Brazil).cht, "Invincibility": RAM $C81A is the
# power, 6 when full. Hits still land, but the power is refilled each frame
poke "Infinite energy"
ar 00C8-1A06
endpoke

# Golvellius - Valley of Doom (USA, Europe, Brazil).cht, "Infinite Money": RAM $C840 is the
# gold
poke "Infinite money"
ar 00C8-4099
endpoke
