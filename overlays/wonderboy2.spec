# Wonder Boy in Monster Land (USA, Europe), 8CBEF0C1, drafted by tools/mkspec.py from sitescan output (with the detector log).
name Wonder Boy in Monster Land
cart 8CBEF0C1
hz any		; No-Intro regions USA, Europe
# tilecache: whole tiles copied from cart ROM are not converted again (MAME,
# game frames 300-2300: framework cycles -0.7%, vertical blank tile work -11%)
tilecache
vector 08 io
asm 00004 2   ; IM 1 -> IM 2
    im 2
endasm
site 0009A   ; OUT ($DF),A
site 00102   ; IN A,($BF)
site 0015C   ; IN A,($DD)
site 0018A   ; OUT ($3F),A
site 0018C   ; IN A,($DD)
site 00195   ; OUT ($3F),A
site 00197   ; IN A,($DD)
site 0019F   ; OUT ($DE),A
site 001AC   ; OUT ($3E),A
site 001B4   ; OUT ($F2),A
site 001B7   ; IN A,($F2)
site 001C9   ; OUT ($F2),A
site 001D1   ; OUT ($3E),A
site 002C3   ; IN A,($DC)
site 002F5   ; OUT ($BF),A
site 002FA   ; OUT ($BF),A
site 00301   ; OUT ($BF),A
site 00305   ; IN A,($BE)
site 0030A   ; OUT ($BF),A
site 0030D   ; OUT ($BF),A
site 00310   ; OUT ($BE),A
site 00314   ; OUT ($BF),A
site 00317   ; OUT ($BF),A
site 0031A   ; OUT ($BE),A
site 00324   ; OUT ($BF),A
site 00327   ; OUT ($BF),A
site 0032A   ; OUT ($BE),A
site 0032F   ; OUT ($BE),A
site 00339   ; OUT ($BF),A
site 0033C   ; OUT ($BF),A
site 0033F   ; OUT ($BE),A
site 0034A   ; OUT ($BF),A
site 0034D   ; OUT ($BF),A
site 00352   ; OUT ($BE),A
site 00357   ; OUT ($BE),A
site 00362   ; OUT ($BF),A
site 00365   ; OUT ($BF),A
site 0036A   ; OUTI
site 0037A   ; OUT ($BF),A
site 0037D   ; OUT ($BF),A
site 00414   ; OUT ($BF),A
site 00417   ; OUT ($BF),A
site 00419   ; OTIR
site 006AD   ; OUT ($BF),A
site 006B2   ; OUT ($BF),A
site 006B6   ; OUT ($BE),A
site 006E7   ; OUT ($BF),A
site 006EA   ; OUT ($BF),A
site 006EE   ; OUT ($BE),A
site 00753   ; OUT ($BF),A
site 00756   ; OUT ($BF),A
site 0075B   ; OUT ($BE),A
site 00794   ; IN A,($BE)
site 007BF   ; OUT ($BE),A
site 009FD   ; OUT ($BE),A
site 00A13   ; OUT ($BE),A
site 00A24   ; OUT ($BE),A
site 00A49   ; OUT ($BE),A
site 00A4F   ; OUT ($BE),A
site 00A56   ; OUT ($BE),A
site 00A5C   ; OUT ($BE),A
site 00E24   ; OUT ($BF),A
site 00E27   ; OUT ($BF),A
site 00E2B   ; IN A,($BE)
site 00E30   ; IN A,($BE)
site 019F8   ; OUT ($BF),A
site 019FC   ; OUT ($BF),A
site 01A57   ; OUT ($BF),A
site 01A5A   ; OUT ($BF),A
site 01A5E   ; OUT ($BE),A
site 01A63   ; OUT ($BE),A
site 01A6E   ; OUT ($BF),A
site 01A71   ; OUT ($BF),A
site 01A78   ; OUT ($BE),A
site 01A7D   ; OUT ($BE),A
site 01B8D   ; OUT ($BF),A
site 01B91   ; OUT ($BF),A
site 01BBD   ; OUT ($BF),A
site 01BC1   ; OUT ($BF),A
site 01C13   ; OUT ($BF),A
site 01C16   ; OUT ($BF),A
site 01C1B   ; OUT ($BE),A
site 01C21   ; OUT ($BE),A
site 01C27   ; OUT ($BE),A
site 01C2D   ; OUT ($BE),A
site 01D1A   ; OUT ($BF),A
site 01D1E   ; OUT ($BF),A
site 01D22   ; OUTI
site 01D24   ; OUTI
site 01D26   ; OUTI
site 01D28   ; OUTI
site 01D2A   ; OUTI
site 01D2C   ; OUTI
site 01D2E   ; OUTI
site 01D30   ; OUTI
site 01D32   ; OUTI
site 01D34   ; OUTI
site 01D36   ; OUTI
site 01D38   ; OUTI
site 01D3A   ; OUTI
site 01D3C   ; OUTI
site 01D3E   ; OUTI
site 01D40   ; OUTI
site 01D42   ; OUTI
site 01D44   ; OUTI
site 01D46   ; OUTI
site 01D48   ; OUTI
site 01D4A   ; OUTI
site 01D4C   ; OUTI
site 01D4E   ; OUTI
site 01D50   ; OUTI
site 01D52   ; OUTI
site 01D54   ; OUTI
site 01D56   ; OUTI
site 01D58   ; OUTI
site 01D5A   ; OUTI
site 01D5C   ; OUTI
site 01D5E   ; OUTI
site 01D60   ; OUTI
site 01D62   ; OUTI
site 01D64   ; OUTI
site 01D66   ; OUTI
site 01D68   ; OUTI
site 01D6A   ; OUTI
site 01D6C   ; OUTI
site 01D6E   ; OUTI
site 01D70   ; OUTI
site 01D72   ; OUTI
site 01D74   ; OUTI
site 01D76   ; OUTI
site 01D78   ; OUTI
site 01D7A   ; OUTI
site 01D7C   ; OUTI
site 01D7E   ; OUTI
site 01D80   ; OUTI
site 01D82   ; OUTI
site 01D84   ; OUTI
site 01D86   ; OUTI
site 01D88   ; OUTI
site 01D8A   ; OUTI
site 01D8C   ; OUTI
site 01D8E   ; OUTI
site 01D90   ; OUTI
site 01D92   ; OUTI
site 01D94   ; OUTI
site 01D96   ; OUTI
site 01D98   ; OUTI
site 01D9A   ; OUTI
site 01D9C   ; OUTI
site 01D9E   ; OUTI
site 01DA0   ; OUTI
site 01DA2   ; OUTI
site 01DA4   ; OUTI
site 01DA6   ; OUTI
site 01DA8   ; OUTI
site 01DAA   ; OUTI
site 01DAC   ; OUTI
site 01DAE   ; OUTI
site 01DB0   ; OUTI
site 01DB2   ; OUTI
site 01DB4   ; OUTI
site 01DB6   ; OUTI
site 01DB8   ; OUTI
site 01DBA   ; OUTI
site 01DBC   ; OUTI
site 01DBE   ; OUTI
site 01DC0   ; OUTI
site 01DC2   ; OUTI
site 01DC4   ; OUTI
site 01DC6   ; OUTI
site 01DC8   ; OUTI
site 01DCA   ; OUTI
site 01DCC   ; OUTI
site 01DCE   ; OUTI
site 01DD0   ; OUTI
site 01DD2   ; OUTI
site 01DD4   ; OUTI
site 01DD6   ; OUTI
site 01DD8   ; OUTI
site 01DDA   ; OUTI
site 01DDC   ; OUTI
site 01DDE   ; OUTI
site 01DE0   ; OUTI
site 01DE2   ; OUTI
site 01DE4   ; OUTI
site 01DE6   ; OUTI
site 01DE8   ; OUTI
site 01DEA   ; OUTI
site 01DEC   ; OUTI
site 01DEE   ; OUTI
site 01DF0   ; OUTI
site 01DF2   ; OUTI
site 01DF4   ; OUTI
site 01DF6   ; OUTI
site 01DF8   ; OUTI
site 01DFA   ; OUTI
site 01DFC   ; OUTI
site 01DFE   ; OUTI
site 01E00   ; OUTI
site 01E02   ; OUTI
site 01E04   ; OUTI
site 01E06   ; OUTI
site 01E08   ; OUTI
site 01E0A   ; OUTI
site 01E0C   ; OUTI
site 01E0E   ; OUTI
site 01E10   ; OUTI
site 01E12   ; OUTI
site 01E14   ; OUTI
site 01E16   ; OUTI
site 01E18   ; OUTI
site 01E1A   ; OUTI
site 01E1C   ; OUTI
site 01E1E   ; OUTI
site 01E20   ; OUTI
site 01E22   ; OUTI
site 01E24   ; OUTI
site 01E26   ; OUTI
site 01E28   ; OUTI
site 01E2A   ; OUTI
site 01E2C   ; OUTI
site 01E2E   ; OUTI
site 01E30   ; OUTI
site 01E32   ; OUTI
site 01E34   ; OUTI
site 01E36   ; OUTI
site 01E38   ; OUTI
site 01E3A   ; OUTI
site 01E3C   ; OUTI
site 01E3E   ; OUTI
site 01E40   ; OUTI
site 01E42   ; OUTI
site 01E44   ; OUTI
site 01E46   ; OUTI
site 01E48   ; OUTI
site 01E4A   ; OUTI
site 01E4C   ; OUTI
site 01E4E   ; OUTI
site 01E50   ; OUTI
site 01E52   ; OUTI
site 01E54   ; OUTI
site 01E56   ; OUTI
site 01E58   ; OUTI
site 01E5A   ; OUTI
site 01E5C   ; OUTI
site 01E5E   ; OUTI
site 01E60   ; OUTI
site 01E62   ; OUTI
site 01E64   ; OUTI
site 01E66   ; OUTI
site 01E68   ; OUTI
site 01E6A   ; OUTI
site 01E6C   ; OUTI
site 01E6E   ; OUTI
site 01E70   ; OUTI
site 01E72   ; OUTI
site 01E74   ; OUTI
site 01E76   ; OUTI
site 01E78   ; OUTI
site 01E7A   ; OUTI
site 01E7C   ; OUTI
site 01E7E   ; OUTI
site 01E80   ; OUTI
site 01E82   ; OUTI
site 01E84   ; OUTI
site 01E86   ; OUTI
site 01E88   ; OUTI
site 01E8A   ; OUTI
site 01E8C   ; OUTI
site 01E8E   ; OUTI
site 01E90   ; OUTI
site 01E92   ; OUTI
site 01E94   ; OUTI
site 01E96   ; OUTI
site 01E98   ; OUTI
site 01E9A   ; OUTI
site 01E9C   ; OUTI
site 01E9E   ; OUTI
site 01EA0   ; OUTI
site 01EA2   ; OUTI
site 01EA4   ; OUTI
site 01EA6   ; OUTI
site 01EA8   ; OUTI
site 01EAA   ; OUTI
site 01EAC   ; OUTI
site 01EAE   ; OUTI
site 01EB0   ; OUTI
site 01EB2   ; OUTI
site 01EB4   ; OUTI
site 01EB6   ; OUTI
site 01EB8   ; OUTI
site 01EBA   ; OUTI
site 01EBC   ; OUTI
site 01EBE   ; OUTI
site 01EC0   ; OUTI
site 01EC2   ; OUTI
site 01EC4   ; OUTI
site 01EC6   ; OUTI
site 01EC8   ; OUTI
site 01ECA   ; OUTI
site 01ECC   ; OUTI
site 01ECE   ; OUTI
site 01ED0   ; OUTI
site 01ED2   ; OUTI
site 01ED4   ; OUTI
site 01ED6   ; OUTI
site 01ED8   ; OUTI
site 01EDA   ; OUTI
site 01EDC   ; OUTI
site 01EDE   ; OUTI
site 01EE0   ; OUTI
site 01EE2   ; OUTI
site 01EE4   ; OUTI
site 01EE6   ; OUTI
site 01EE8   ; OUTI
site 01EEA   ; OUTI
site 01EEC   ; OUTI
site 01EEE   ; OUTI
site 01EF0   ; OUTI
site 01EF2   ; OUTI
site 01EF4   ; OUTI
site 01EF6   ; OUTI
site 01EF8   ; OUTI
site 01EFA   ; OUTI
site 01EFC   ; OUTI
site 01EFE   ; OUTI
site 01F00   ; OUTI
site 01F02   ; OUTI
site 01F04   ; OUTI
site 01F06   ; OUTI
site 01F08   ; OUTI
site 01F0A   ; OUTI
site 01F0C   ; OUTI
site 01F0E   ; OUTI
site 01F10   ; OUTI
site 01F12   ; OUTI
site 01F14   ; OUTI
site 01F16   ; OUTI
site 01F18   ; OUTI
site 01F1A   ; OUTI
site 01F1C   ; OUTI
site 01F1E   ; OUTI
site 01F20   ; OUTI
site 01F22   ; OUTI
site 01F24   ; OUTI
site 01F26   ; OUTI
site 01F28   ; OUTI
site 01F2A   ; OUTI
site 01F2C   ; OUTI
site 01F2E   ; OUTI
site 01F30   ; OUTI
site 01F32   ; OUTI
site 01F34   ; OUTI
site 01F36   ; OUTI
site 01F38   ; OUTI
site 01F3A   ; OUTI
site 01F3C   ; OUTI
site 01F3E   ; OUTI
site 01F40   ; OUTI
site 01F42   ; OUTI
site 01F44   ; OUTI
site 01F46   ; OUTI
site 01F48   ; OUTI
site 01F4A   ; OUTI
site 01F4C   ; OUTI
site 01F4E   ; OUTI
site 01F50   ; OUTI
site 01F52   ; OUTI
site 01F54   ; OUTI
site 01F56   ; OUTI
site 01F58   ; OUTI
site 01F5A   ; OUTI
site 01F5C   ; OUTI
site 01F5E   ; OUTI
site 01F60   ; OUTI
site 01F62   ; OUTI
site 01F64   ; OUTI
site 01F66   ; OUTI
site 01F68   ; OUTI
site 01F6A   ; OUTI
site 01F6C   ; OUTI
site 01F6E   ; OUTI
site 01F70   ; OUTI
site 01F72   ; OUTI
site 01F74   ; OUTI
site 01F76   ; OUTI
site 01F78   ; OUTI
site 01F7A   ; OUTI
site 01F7C   ; OUTI
site 01F7E   ; OUTI
site 01F80   ; OUTI
site 01F82   ; OUTI
site 01F84   ; OUTI
site 01F86   ; OUTI
site 01F88   ; OUTI
site 01F8A   ; OUTI
site 01F8C   ; OUTI
site 01F8E   ; OUTI
site 01F90   ; OUTI
site 01F92   ; OUTI
site 01F94   ; OUTI
site 01F96   ; OUTI
site 01F98   ; OUTI
site 01F9A   ; OUTI
site 01F9C   ; OUTI
site 01F9E   ; OUTI
site 01FA0   ; OUTI
site 02997   ; OUT ($BF),A
site 0299B   ; OUT ($BF),A
site 029A3   ; IN A,($BE)
site 039BA   ; OUT ($BF),A
site 039BD   ; OUT ($BF),A
site 039DA   ; OUT ($BF),A
site 039DD   ; OUT ($BF),A
site 039EF   ; OUT ($BE),A
site 039F5   ; OUT ($BE),A
site 04C72   ; OUT ($BF),A
site 04C76   ; OUT ($BF),A
site 04C79   ; OUT ($BE),A
site 04C7D   ; OUT ($BE),A
site 04C81   ; OUT ($BF),A
site 04C84   ; OUT ($BF),A
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
site 05004   ; OUT ($BF),A
site 05007   ; OUT ($BF),A
site 0500B   ; OUT ($BE),A
site 0500F   ; OUT ($BE),A
site 0506F   ; IN A,($DD)
site 05741   ; OUT ($BF),A
site 05744   ; OUT ($BF),A
site 0574B   ; OUT ($BE),A
site 05751   ; OUT ($BE),A
site 057A3   ; OUT ($BF),A
site 057A8   ; OUT ($BF),A
site 057AB   ; OUT ($BE),A
site 057AF   ; OUT ($BE),A
site 05899   ; OUT ($BF),A
site 0589C   ; OUT ($BF),A
site 058A1   ; OUT ($BE),A
site 058A7   ; OUT ($BE),A
site 07BA2   ; OUT ($BF),A
site 07BA6   ; OUT ($BF),A
site 07DFF   ; OUT ($BE),A
site 07EC8   ; OUT ($BF),A
site 07ECC   ; OUT ($BF),A
site 07ED4   ; OUT ($BE),A
site 07ED9   ; OUT ($BE),A
site 07EDE   ; OUT ($BE),A
site 07EE3   ; OUT ($BE),A
site 07FB5   ; IN A,($DC)
site 28E28   ; OUT ($F0),A
site 28E31   ; OUT ($F1),A
site 28E49   ; OUT ($7F),A
site 28E59   ; OUT (C),D
site 28E5F   ; OUT ($F1),A
site 28E72   ; OUT ($F0),A
site 28E78   ; OUT ($F1),A
site 28E83   ; OUTI
site 28E8A   ; OUTI
site 28E99   ; OUT ($7F),A
site 28E9D   ; OUT ($F0),A
site 28EA3   ; OUT ($F1),A
site 2905C   ; OUT ($7F),A
site 29060   ; OUT ($7F),A
site 290EB   ; OUT ($7F),A
site 29113   ; OUT ($7F),A
site 2916C   ; OUT ($F0),A
site 29173   ; OUT ($F1),A
site 2917B   ; OUT ($F0),A
site 29181   ; OUT ($F1),A
site 29276   ; OUT ($F0),A
site 2927D   ; OUT (C),L
site 29286   ; OUT ($F0),A
site 292A1   ; OUT (C),H
site 292A9   ; OUT ($F0),A
site 292B7   ; OUT ($F1),A
site 292BF   ; OUT ($F0),A
site 292C9   ; OUT ($F1),A
site 29485   ; OUT ($F0),A
site 2948B   ; OUTI
site 294F6   ; OUT ($7F),A
site 295ED   ; OUT ($7F),A
site 295F1   ; OUT ($7F),A
site 2960E   ; OUT ($7F),A
site 29630   ; OUT ($7F),A
site 2963F   ; OUT ($F0),A
site 2964A   ; OUT ($F1),A
site 2965B   ; OUT ($F0),A
site 2966F   ; OUT ($F0),A
site 29683   ; OUT ($F1),A
site 296E8   ; OTIR
site 296F5   ; OUT (C),D
site 296FB   ; OUT ($F1),A
site 29736   ; OUT ($7F),A
site 29787   ; OUT ($7F),A
site 29811   ; OUT ($7F),A
site 29831   ; OUT ($7F),A
site 29871   ; OUT ($7F),A
site 2987B   ; OUT ($7F),A
site 298C3   ; OUT ($7F),A
mapst 00076   ; LD ($FFFC),A
mapst 0007B   ; LD ($FFFD),A
mapst 00080   ; LD ($FFFE),A
mapst 00085   ; LD ($FFFF),A
mapst 000A7   ; LD ($FFFF),A
mapst 0014C   ; LD ($FFFF),A
mapst 00467   ; LD ($FFFF),A
mapst 004B1   ; LD ($FFFF),A
mapst 00565   ; LD ($FFFF),A
mapst 005DF   ; LD ($FFFF),A
mapst 00A69   ; LD ($FFFF),A
mapst 00E48   ; LD ($FFFF),A
mapst 00EDD   ; LD ($FFFF),A
mapst 00F1A   ; LD ($FFFF),A
mapst 00FA8   ; LD ($FFFF),A
mapst 01A1E   ; LD ($FFFF),A
mapst 01BE1   ; LD ($FFFF),A
mapst 01CEA   ; LD ($FFFF),A
mapst 02398   ; LD ($FFFF),A
mapst 023A6   ; LD ($FFFF),A
mapst 0244B   ; LD ($FFFF),A
mapst 0249A   ; LD ($FFFF),A
mapst 024C8   ; LD ($FFFF),A
mapst 02559   ; LD ($FFFF),A
mapst 02574   ; LD ($FFFF),A
mapst 0264F   ; LD ($FFFF),A
mapst 0265C   ; LD ($FFFF),A
mapst 0275D   ; LD ($FFFF),A
mapst 027DA   ; LD ($FFFF),A
mapst 027E2   ; LD ($FFFF),A
mapst 0285F   ; LD ($FFFF),A
mapst 0291E   ; LD ($FFFF),A
mapst 02942   ; LD ($FFFF),A
mapst 02953   ; LD ($FFFF),A
mapst 02976   ; LD ($FFFF),A
mapst 029CA   ; LD ($FFFF),A
mapst 031E5   ; LD ($FFFF),A
mapst 033C7   ; LD ($FFFF),A
mapst 033EF   ; LD ($FFFF),A
mapst 033F7   ; LD ($FFFF),A
mapst 03525   ; LD ($FFFF),A
mapst 035D3   ; LD ($FFFF),A
mapst 035DB   ; LD ($FFFF),A
mapst 03646   ; LD ($FFFF),A
mapst 036AB   ; LD ($FFFF),A
mapst 036B3   ; LD ($FFFF),A
mapst 03A30   ; LD ($FFFF),A
mapst 03A55   ; LD ($FFFF),A
mapst 03B03   ; LD ($FFFF),A
mapst 03B47   ; LD ($FFFF),A
mapst 03C7C   ; LD ($FFFF),A
mapst 03F34   ; LD ($FFFF),A
mapst 03F4A   ; LD ($FFFF),A
mapst 03FE3   ; LD ($FFFF),A
mapst 0412C   ; LD ($FFFF),A
mapst 04149   ; LD ($FFFF),A
mapst 04159   ; LD ($FFFF),A
mapst 04168   ; LD ($FFFF),A
mapst 0434F   ; LD ($FFFF),A
mapst 0435E   ; LD ($FFFF),A
mapst 04381   ; LD ($FFFF),A
mapst 04C53   ; LD ($FFFF),A
mapst 04DDD   ; LD ($FFFF),A
mapst 04DE9   ; LD ($FFFF),A
mapst 04E5C   ; LD ($FFFF),A
mapst 051BE   ; LD ($FFFF),A
mapst 05237   ; LD ($FFFF),A
mapst 054B1   ; LD ($FFFF),A
mapst 05608   ; LD ($FFFF),A
mapst 05689   ; LD ($FFFF),A
mapst 056B9   ; LD ($FFFF),A
mapst 057C4   ; LD ($FFFF),A
mapst 05A5D   ; LD ($FFFF),A
mapst 05A6B   ; LD ($FFFF),A
mapst 05BC9   ; LD ($FFFF),A
mapst 06385   ; LD ($FFFF),A
mapst 07178   ; LD ($FFFF),A
mapst 0756B   ; LD ($FFFF),A
mapst 0778F   ; LD ($FFFF),A
mapst 07B9D   ; LD ($FFFF),A
mapst 07C8E   ; LD ($FFFF),A
mapst 07D5A   ; LD ($FFFF),A
mapst 07E64   ; LD ($FFFF),A
mapst 07F0C   ; LD ($FFFF),A
mapst 07F22   ; LD ($FFFF),A
mapst 07F95   ; LD ($FFFF),A
# CHECK cartarea_store at 179B7 ($B9B7 bank 5): LD ($2525),A $2525
# CHECK cartarea_store at 17AB8 ($BAB8 bank 5): LD (BC),A $0001
# CHECK cartarea_store at 17AD7 ($BAD7 bank 5): LD (BC),A $8104,$8108,$810C,$8110
# CHECK cartarea_store at 17B83 ($BB83 bank 5): LD (BC),A $0100
# CHECK cartarea_store at 17B89 ($BB89 bank 5): LD (BC),A $0101
# CHECK cartarea_store at 17B8B ($BB8B bank 5): LD (BC),A $0201
# CHECK cartarea_store at 17B8E ($BB8E bank 5): LD (BC),A $0301
# CHECK cartarea_store at 17B92 ($BB92 bank 5): LD (BC),A $0402
# CHECK cartarea_store at 17BC1 ($BBC1 bank 5): LD ($2621),HL $2621,$2622
# CHECK ram_exec at 17AF7 ($BAF7 bank 5): CALL M,$F804 $F804
# CHECK indirect_unresolved at 000F0 ($00F0 bank 0): JP (HL) 
# CHECK indirect_unresolved at 17AE0 ($BAE0 bank 5): RET NZ 
# CHECK indirect_unresolved at 17AE6 ($BAE6 bank 5): RET C 
# CHECK bank_unresolved at 028C9 ($28C9 bank 0): CALL $96DF $96DF
# CHECK low: site 002FE  OUT ($BF),A  (vdp_control)
# CHECK low: site 09047  OUT (C),B  (port in C)
# CHECK low: site 0A3C7  OUT (C),B  (port in C)
# CHECK low: site 0C596  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 117B7  OUT ($C1),A  (no_effect)
# CHECK low: site 1369B  OUT ($BF),A  (vdp_control)
# CHECK low: site 16F20  IN A,($7F)  (h_counter)
# CHECK low: site 1A2B1  IN A,($F0)  (joypad_a)
# CHECK low: site 1A59C  OUT ($F0),A  (fm_address)
# CHECK low: site 1A758  IND  (port in C)
# CHECK low: site 1A848  IND  (port in C)
# CHECK low: site 1EFE6  IN A,($BD)  (vdp_status)
# CHECK low: site 1F01D  OTDR  (port in C)
# CHECK low: site 1F14D  IN A,(C)  (port in C)
# CHECK low: site 1F2C6  IN A,($BD)  (vdp_status)
# CHECK low: site 209F4  OUT ($F2),A  (fm_control)
# CHECK low: site 20C38  OUT ($C1),A  (no_effect)
# CHECK low: site 2AA29  IN A,($F0)  (joypad_a)
# CHECK low: site 2B664  OUT ($BF),A  (vdp_control)
# CHECK low: site 37056  OUT ($7F),A  (psg)
# CHECK low: site 38654  OUTI  (port in C)
# CHECK low: site 3A4B8  OUT ($7F),A  (psg)
# CHECK low: site 3A4C8  OUT ($7F),A  (psg)
# CHECK low: site 3E382  IN A,($BF)  (vdp_status)
# CHECK low: site 3E38A  IN A,($7F)  (h_counter)
# CHECK low: site 3EAA5  OUT ($BD),A  (vdp_control)
