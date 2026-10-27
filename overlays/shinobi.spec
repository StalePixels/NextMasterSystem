# Shinobi (USA, Europe, Brazil) (En) (Rev 1), CRC32 0C6FAC4E, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log.
# The game checks the region at $0003 (port $3F, then $DD); compare it with a reference forced
# to the export path. Register 8 is written at $1ADB, in the frame handler's column streamer
# $1AD4; the reference log's few mid-frame register 8 writes come from frames where the SMS
# frame handler starts late, not from a line interrupt (line interrupts are never on).
# No priority cells in the reference log.
# Spec gaps (data/scan-verdicts.tsv): unused are the 1bpp tile loader $1088 and the VRAM copy
# $117F, which nothing names; false are byte patterns in data banks 8, 10 and 11.
name Shinobi
cart 0C6FAC4E
hz any		; No-Intro regions USA, Europe, Brazil
vector 28 io
asm 00089 2   ; IM 1 -> IM 2
    im 2
endasm
site 00005   ; OUT ($3F),A
site 00007   ; IN A,($DD)
site 00011   ; OUT ($3F),A
site 00013   ; IN A,($DD)
site 0001C   ; OUT ($3F),A
site 000A2   ; OUT ($DF),A
site 000BE   ; IN A,($BF)
site 000C7   ; OTIR
site 00100   ; OUT ($BF),A
site 00104   ; OUT ($BF),A
site 0017F   ; OUT ($3E),A
site 00187   ; OUT ($F2),A
site 0018A   ; IN A,($F2)
site 0019C   ; OUT ($F2),A
site 001A4   ; OUT ($3E),A
site 00232   ; OUT ($BF),A
site 00235   ; OUT ($BF),A
site 00242   ; OUTI
site 00248   ; OUT (C),A
site 00269   ; OUTI
site 0026D   ; OUTI
site 00271   ; OUT ($BE),A
site 00275   ; OUT ($BE),A
site 002BB   ; OUT ($BF),A
site 002BF   ; OUT ($BF),A
site 00729   ; OUT ($BF),A
site 0072D   ; OUT ($BF),A
site 00A2B   ; OUT ($BF),A
site 00A2F   ; OUT ($BF),A
site 00C96   ; IN A,($DC)
site 00C9C   ; IN A,($DC)
site 00C9F   ; IN A,($DD)
site 00D17   ; IN A,($BF)
site 00D32   ; IN A,($DD)
site 00D5C   ; OUT ($BF),A
site 00D62   ; OUT ($BF),A
site 00D6A   ; OUTI
site 00D6C   ; OUTI
site 00D6E   ; OUTI
site 00D70   ; OUTI
site 00D72   ; OUTI
site 00D74   ; OUTI
site 00D76   ; OUTI
site 00D78   ; OUTI
site 00D7A   ; OUTI
site 00D7C   ; OUTI
site 00D7E   ; OUTI
site 00D80   ; OUTI
site 00D82   ; OUTI
site 00D84   ; OUTI
site 00D86   ; OUTI
site 00D88   ; OUTI
site 00D8A   ; OUTI
site 00D8C   ; OUTI
site 00D8E   ; OUTI
site 00D90   ; OUTI
site 00D92   ; OUTI
site 00D94   ; OUTI
site 00D96   ; OUTI
site 00D98   ; OUTI
site 00D9A   ; OUTI
site 00D9C   ; OUTI
site 00D9E   ; OUTI
site 00DA0   ; OUTI
site 00DA2   ; OUTI
site 00DA4   ; OUTI
site 00DA6   ; OUTI
site 00DA8   ; OUTI
site 00DAA   ; OUTI
site 00DAC   ; OUTI
site 00DAE   ; OUTI
site 00DB0   ; OUTI
site 00DB2   ; OUTI
site 00DB4   ; OUTI
site 00DB6   ; OUTI
site 00DB8   ; OUTI
site 00DBA   ; OUTI
site 00DBC   ; OUTI
site 00DBE   ; OUTI
site 00DC0   ; OUTI
site 00DC2   ; OUTI
site 00DC4   ; OUTI
site 00DC6   ; OUTI
site 00DC8   ; OUTI
site 00DCA   ; OUTI
site 00DCC   ; OUTI
site 00DCE   ; OUTI
site 00DD0   ; OUTI
site 00DD2   ; OUTI
site 00DD4   ; OUTI
site 00DD6   ; OUTI
site 00DD8   ; OUTI
site 00DDA   ; OUTI
site 00DDC   ; OUTI
site 00DDE   ; OUTI
site 00DE0   ; OUTI
site 00DE2   ; OUTI
site 00DE4   ; OUTI
site 00DE6   ; OUTI
site 00DE8   ; OUTI
site 00DF0   ; OUT ($BF),A
site 00DF4   ; OUT ($BF),A
site 00DF9   ; OUTI
site 00DFB   ; OUTI
site 00DFD   ; OUTI
site 00DFF   ; OUTI
site 00E01   ; OUTI
site 00E03   ; OUTI
site 00E05   ; OUTI
site 00E07   ; OUTI
site 00E09   ; OUTI
site 00E0B   ; OUTI
site 00E0D   ; OUTI
site 00E0F   ; OUTI
site 00E11   ; OUTI
site 00E13   ; OUTI
site 00E15   ; OUTI
site 00E17   ; OUTI
site 00E19   ; OUTI
site 00E1B   ; OUTI
site 00E1D   ; OUTI
site 00E1F   ; OUTI
site 00E21   ; OUTI
site 00E23   ; OUTI
site 00E25   ; OUTI
site 00E27   ; OUTI
site 00E29   ; OUTI
site 00E2B   ; OUTI
site 00E2D   ; OUTI
site 00E2F   ; OUTI
site 00E31   ; OUTI
site 00E33   ; OUTI
site 00E35   ; OUTI
site 00E37   ; OUTI
site 00E39   ; OUTI
site 00E3B   ; OUTI
site 00E3D   ; OUTI
site 00E3F   ; OUTI
site 00E41   ; OUTI
site 00E43   ; OUTI
site 00E45   ; OUTI
site 00E47   ; OUTI
site 00E49   ; OUTI
site 00E4B   ; OUTI
site 00E4D   ; OUTI
site 00E4F   ; OUTI
site 00E51   ; OUTI
site 00E53   ; OUTI
site 00E55   ; OUTI
site 00E57   ; OUTI
site 00E59   ; OUTI
site 00E5B   ; OUTI
site 00E5D   ; OUTI
site 00E5F   ; OUTI
site 00E61   ; OUTI
site 00E63   ; OUTI
site 00E65   ; OUTI
site 00E67   ; OUTI
site 00E69   ; OUTI
site 00E6B   ; OUTI
site 00E6D   ; OUTI
site 00E6F   ; OUTI
site 00E71   ; OUTI
site 00E73   ; OUTI
site 00E75   ; OUTI
site 00E77   ; OUTI
site 00E7B   ; OUT ($BF),A
site 00E7F   ; OUT ($BF),A
site 00E84   ; OUTI
site 00E86   ; OUTI
site 00E88   ; OUTI
site 00E8A   ; OUTI
site 00E8C   ; OUTI
site 00E8E   ; OUTI
site 00E90   ; OUTI
site 00E92   ; OUTI
site 00E94   ; OUTI
site 00E96   ; OUTI
site 00E98   ; OUTI
site 00E9A   ; OUTI
site 00E9C   ; OUTI
site 00E9E   ; OUTI
site 00EA0   ; OUTI
site 00EA2   ; OUTI
site 00EA4   ; OUTI
site 00EA6   ; OUTI
site 00EA8   ; OUTI
site 00EAA   ; OUTI
site 00EAC   ; OUTI
site 00EAE   ; OUTI
site 00EB0   ; OUTI
site 00EB2   ; OUTI
site 00EB4   ; OUTI
site 00EB6   ; OUTI
site 00EB8   ; OUTI
site 00EBA   ; OUTI
site 00EBC   ; OUTI
site 00EBE   ; OUTI
site 00EC0   ; OUTI
site 00EC2   ; OUTI
site 00EC4   ; OUTI
site 00EC6   ; OUTI
site 00EC8   ; OUTI
site 00ECA   ; OUTI
site 00ECC   ; OUTI
site 00ECE   ; OUTI
site 00ED0   ; OUTI
site 00ED2   ; OUTI
site 00ED4   ; OUTI
site 00ED6   ; OUTI
site 00ED8   ; OUTI
site 00EDA   ; OUTI
site 00EDC   ; OUTI
site 00EDE   ; OUTI
site 00EE0   ; OUTI
site 00EE2   ; OUTI
site 00EE4   ; OUTI
site 00EE6   ; OUTI
site 00EE8   ; OUTI
site 00EEA   ; OUTI
site 00EEC   ; OUTI
site 00EEE   ; OUTI
site 00EF0   ; OUTI
site 00EF2   ; OUTI
site 00EF4   ; OUTI
site 00EF6   ; OUTI
site 00EF8   ; OUTI
site 00EFA   ; OUTI
site 00EFC   ; OUTI
site 00EFE   ; OUTI
site 00F00   ; OUTI
site 00F02   ; OUTI
site 00F04   ; OUTI
site 00F06   ; OUTI
site 00F08   ; OUTI
site 00F0A   ; OUTI
site 00F0C   ; OUTI
site 00F0E   ; OUTI
site 00F10   ; OUTI
site 00F12   ; OUTI
site 00F14   ; OUTI
site 00F16   ; OUTI
site 00F18   ; OUTI
site 00F1A   ; OUTI
site 00F1C   ; OUTI
site 00F1E   ; OUTI
site 00F20   ; OUTI
site 00F22   ; OUTI
site 00F24   ; OUTI
site 00F26   ; OUTI
site 00F28   ; OUTI
site 00F2A   ; OUTI
site 00F2C   ; OUTI
site 00F2E   ; OUTI
site 00F30   ; OUTI
site 00F32   ; OUTI
site 00F34   ; OUTI
site 00F36   ; OUTI
site 00F38   ; OUTI
site 00F3A   ; OUTI
site 00F3C   ; OUTI
site 00F3E   ; OUTI
site 00F40   ; OUTI
site 00F42   ; OUTI
site 00F44   ; OUTI
site 00F46   ; OUTI
site 00F48   ; OUTI
site 00F4A   ; OUTI
site 00F4C   ; OUTI
site 00F4E   ; OUTI
site 00F50   ; OUTI
site 00F52   ; OUTI
site 00F54   ; OUTI
site 00F56   ; OUTI
site 00F58   ; OUTI
site 00F5A   ; OUTI
site 00F5C   ; OUTI
site 00F5E   ; OUTI
site 00F60   ; OUTI
site 00F62   ; OUTI
site 00F64   ; OUTI
site 00F66   ; OUTI
site 00F68   ; OUTI
site 00F6A   ; OUTI
site 00F6C   ; OUTI
site 00F6E   ; OUTI
site 00F70   ; OUTI
site 00F72   ; OUTI
site 00F74   ; OUTI
site 00F76   ; OUTI
site 00F78   ; OUTI
site 00F7A   ; OUTI
site 00F7C   ; OUTI
site 00F7E   ; OUTI
site 00F80   ; OUTI
site 00F82   ; OUTI
site 01000   ; OUT ($BF),A
site 01004   ; OUT ($BF),A
site 01008   ; OUT ($BF),A
site 0100C   ; OUT ($BF),A
site 01014   ; OUT ($BF),A
site 01018   ; OUT ($BF),A
site 0101D   ; OUT ($BF),A
site 01022   ; OUT ($BF),A
site 0102B   ; OUT ($BE),A
site 0103C   ; OUT ($BE),A
site 0104C   ; OUT ($BE),A
site 01051   ; OUT ($BE),A
site 01061   ; OUT ($BE),A
site 01067   ; OUT ($BE),A
site 01078   ; OUT ($BF),A
site 0107D   ; OUT ($BF),A
site 01082   ; OUT ($BE),A
site 010C5   ; OUT ($BF),A
site 010CA   ; OUT ($BF),A
site 010CF   ; OUT ($BE),A
site 010FE   ; OUT ($BF),A
site 01103   ; OUT ($BF),A
site 01108   ; OUT ($BE),A
site 01149   ; OUT ($BF),A
site 0114C   ; OUT ($BF),A
site 01150   ; IN A,($BE)
site 01176   ; OUT ($BE),A
site 01AD7   ; OUT ($BF),A
site 01ADB   ; OUT ($BF),A
site 01AFE   ; OUT ($BF),A
site 01B03   ; OUT ($BF),A
site 01B08   ; OUT ($BE),A
site 01B10   ; OUT ($BE),A
site 01B2D   ; OUT ($BE),A
site 01B32   ; OUT ($BE),A
site 05378   ; OUT ($BE),A
site 0537E   ; OUT ($BE),A
site 05397   ; OUT ($BE),A
site 0539D   ; OUT ($BE),A
site 053C1   ; OUT ($BE),A
site 053C7   ; OUT ($BE),A
site 053D4   ; OUT ($BE),A
site 053DA   ; OUT ($BE),A
site 053FA   ; OUT ($BE),A
site 053FF   ; OUT ($BE),A
site 05410   ; OUT ($BE),A
site 05415   ; OUT ($BE),A
site 05436   ; IN A,($BE)
site 0543B   ; OUT ($BE),A
site 05449   ; IN A,($BE)
site 0544E   ; OUT ($BE),A
site 058EE   ; OUT ($BF),A
site 058F2   ; OUT ($BF),A
site 059F4   ; OUT ($BE),A
site 059F8   ; OUT ($BE),A
site 05A15   ; OUT ($BE),A
site 05A19   ; OUT ($BE),A
site 05A36   ; OUT ($BE),A
site 05A3A   ; OUT ($BE),A
site 05A57   ; OUT ($BE),A
site 05A5B   ; OUT ($BE),A
site 05A9F   ; OUT ($BE),A
site 05AA5   ; OUT ($BE),A
site 060CB   ; OUT ($BF),A
site 060CF   ; OUT ($BF),A
site 060D3   ; OUT ($BF),A
site 060D7   ; OUT ($BF),A
site 0628D   ; OUT ($BF),A
site 06291   ; OUT ($BF),A
site 07727   ; OUTI
site 18132   ; OUT ($F0),A
site 1813B   ; OUT ($F1),A
site 1815A   ; OUT ($7F),A
site 1815E   ; OUT ($F0),A
site 18164   ; OUT ($F1),A
site 1817B   ; OUT ($7F),A
site 1818B   ; OUT (C),D
site 18191   ; OUT ($F1),A
site 181BD   ; OUT ($F0),A
site 181CB   ; OUT ($F1),A
site 181ED   ; OTIR
site 181FB   ; OTIR
site 18217   ; OUT ($7F),A
site 1821B   ; OUT ($7F),A
site 18221   ; OUT ($F0),A
site 1822F   ; OUT ($F1),A
site 18234   ; OUT ($F0),A
site 1823A   ; OUT ($F1),A
site 18246   ; OUTI
site 1824C   ; OUTI
site 183BE   ; OUT ($7F),A
site 183C2   ; OUT ($7F),A
site 183C6   ; OUT ($7F),A
site 1845B   ; OUT ($7F),A
site 1845F   ; OUT ($7F),A
site 18487   ; OUT ($7F),A
site 1848B   ; OUT ($7F),A
site 1848F   ; OUT ($7F),A
site 18493   ; OUT ($7F),A
site 18496   ; OUT ($7F),A
site 184FC   ; OUT ($F0),A
site 18503   ; OUT ($F1),A
site 1850B   ; OUT ($F0),A
site 18511   ; OUT ($F1),A
site 18606   ; OUT ($F0),A
site 18610   ; OUT (C),L
site 18619   ; OUT ($F0),A
site 18634   ; OUT (C),H
site 1863C   ; OUT ($F0),A
site 1864A   ; OUT ($F1),A
site 18656   ; OUT ($F0),A
site 1865F   ; OUT ($F1),A
site 18820   ; OUT ($F0),A
site 18829   ; OUT (C),A
site 1882E   ; OUT ($F0),A
site 18834   ; OUTI
site 188A5   ; OUT ($7F),A
site 1897E   ; OUT ($7F),A
site 189A9   ; OUT ($7F),A
site 189AD   ; OUT ($7F),A
site 189B9   ; OUT ($7F),A
site 189BE   ; OUT ($7F),A
site 189EA   ; OUT ($F0),A
site 189F8   ; OUT ($F1),A
site 18A06   ; OUT ($F0),A
site 18A1A   ; OUT ($F0),A
site 18AAE   ; OUTI
site 18AB0   ; OUTI
site 18AB2   ; OUTI
site 18AB4   ; OUTI
site 18AB6   ; OUTI
site 18AB8   ; OUTI
site 18ABA   ; OUTI
site 18ABC   ; OUTI
site 18ABE   ; OUTI
site 18AC0   ; OUTI
site 18AC2   ; OUTI
site 18ACC   ; OUT (C),D
site 18AD2   ; OUT ($F1),A
site 18B11   ; OUT ($7F),A
site 18B67   ; OUT ($7F),A
site 18BA6   ; OUT ($7F),A
site 18C08   ; OUT ($7F),A
site 18C28   ; OUT ($7F),A
site 18C68   ; OUT ($7F),A
site 18C72   ; OUT ($7F),A
site 18CBA   ; OUT ($7F),A
site 1AC5B   ; OUT ($7F),A
site 1AC5E   ; OUT ($F2),A
site 1AC78   ; OUT ($7F),A
site 1AC88   ; OUT ($F2),A
site 1AC99   ; OUT ($7F),A
site 1AC9D   ; OUT ($7F),A
mapst 0008D   ; LD ($FFFF),A
mapst 000EA   ; LD ($FFFF),A
mapst 001EF   ; LD ($FFFF),A
mapst 002D3   ; LD ($FFFF),A
mapst 002E1   ; LD ($FFFF),A
mapst 00377   ; LD ($FFFF),A
mapst 003B1   ; LD ($FFFF),A
mapst 00471   ; LD ($FFFF),A
mapst 0048C   ; LD ($FFFF),A
mapst 004D4   ; LD ($FFFF),A
mapst 004E0   ; LD ($FFFF),A
mapst 00558   ; LD ($FFFF),A
mapst 005B6   ; LD ($FFFF),A
mapst 005C4   ; LD ($FFFF),A
mapst 00611   ; LD ($FFFF),A
mapst 006CE   ; LD ($FFFF),A
mapst 00741   ; LD ($FFFF),A
mapst 00758   ; LD ($FFFF),A
mapst 00769   ; LD ($FFFF),A
mapst 0077F   ; LD ($FFFF),A
mapst 0079C   ; LD ($FFFF),A
mapst 007BC   ; LD ($FFFF),A
mapst 007D3   ; LD ($FFFF),A
mapst 0082E   ; LD ($FFFF),A
mapst 00870   ; LD ($FFFF),A
mapst 0088A   ; LD ($FFFF),A
mapst 00934   ; LD ($FFFF),A
mapst 00965   ; LD ($FFFF),A
mapst 00992   ; LD ($FFFF),A
mapst 009B2   ; LD ($FFFF),A
mapst 009F8   ; LD ($FFFF),A
mapst 00A46   ; LD ($FFFF),A
mapst 00AEC   ; LD ($FFFF),A
mapst 00AF7   ; LD ($FFFF),A
mapst 00B16   ; LD ($FFFF),A
mapst 00BE9   ; LD ($FFFF),A
mapst 00CAD   ; LD ($FFFF),A
mapst 00D3E   ; LD ($FFFF),A
mapst 00D57   ; LD ($FFFF),A
mapst 00FD4   ; LD ($FFFF),A
mapst 00FE9   ; LD ($FFFF),A
mapst 01276   ; LD ($FFFF),A
mapst 01286   ; LD ($FFFF),A
mapst 012FF   ; LD ($FFFF),A
mapst 0130E   ; LD ($FFFF),A
mapst 01403   ; LD ($FFFF),A
mapst 01649   ; LD ($FFFF),A
mapst 01664   ; LD ($FFFF),A
mapst 01791   ; LD ($FFFF),A
mapst 017A3   ; LD ($FFFF),A
mapst 02158   ; LD ($FFFF),A
mapst 0505C   ; LD ($FFFF),A
mapst 050CD   ; LD ($FFFF),A
mapst 0557D   ; LD ($FFFF),A
mapst 056C9   ; LD ($FFFF),A
mapst 058F6   ; LD ($FFFF),A
mapst 05904   ; LD ($FFFF),A
mapst 05A86   ; LD ($FFFF),A
mapst 05B62   ; LD ($FFFF),A
mapst 05B8D   ; LD ($FFFF),A
mapst 05BD8   ; LD ($FFFF),A
mapst 05BED   ; LD ($FFFF),A
mapst 05C74   ; LD ($FFFF),A
mapst 05CA2   ; LD ($FFFF),A
mapst 05CB6   ; LD ($FFFF),A
mapst 05CD6   ; LD ($FFFF),A
mapst 05CFD   ; LD ($FFFF),A
mapst 05D24   ; LD ($FFFF),A
mapst 05F9D   ; LD ($FFFF),A
mapst 06046   ; LD ($FFFF),A
mapst 0604E   ; LD ($FFFF),A
mapst 0607E   ; LD ($FFFF),A
mapst 06086   ; LD ($FFFF),A
mapst 060E8   ; LD ($FFFF),A
mapst 0617C   ; LD ($FFFF),A
mapst 061FC   ; LD ($FFFF),A
mapst 0620E   ; LD ($FFFF),A
mapst 064AF   ; LD ($FFFF),A
mapst 067E6   ; LD ($FFFF),A
mapst 06991   ; LD ($FFFF),A
mapst 06B60   ; LD ($FFFF),A
mapst 06DA5   ; LD ($FFFF),A
mapst 06E8A   ; LD ($FFFF),A
mapst 07070   ; LD ($FFFF),A
mapst 070DF   ; LD ($FFFF),A
mapst 07156   ; LD ($FFFF),A
mapst 07BDB   ; LD ($FFFF),A
