# Astro Warrior (Japan, USA, Brazil), 299CBB74, drafted by tools/mkspec.py from sitescan output.
name Astro Warrior
cart 299CBB74
hz 60		; No-Intro regions Japan, USA, Brazil
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00019   ; OUT ($BF),A
site 0001C   ; OUT ($BF),A
otir 00027   ; OUTI
site 00039   ; IN A,($BF)
site 00044   ; OUT ($7F),A
site 00048   ; OUT ($7F),A
site 0004C   ; OUT ($7F),A
site 00050   ; OUT ($7F),A
site 0008D   ; OUT ($DF),A
site 00090   ; OUT ($DE),A
site 00092   ; IN A,($DE)
site 0031C   ; IN A,($DD)
site 0039E   ; OTIR
site 003A9   ; OTIR
site 003D1   ; OTIR
site 00592   ; OUT ($BE),A
site 00597   ; OUT ($BE),A
site 0059C   ; OUT ($BF),A
site 0059F   ; OUT ($BF),A
site 005B5   ; OUT ($BE),A
site 005CA   ; OUT ($BE),A
site 005D0   ; OUT ($BE),A
site 005EB   ; OUT ($BE),A
site 005F7   ; OUT ($BF),A
site 005FB   ; OUT ($BF),A
site 00602   ; OUT ($BF),A
site 00606   ; OUT ($BF),A
site 0064E   ; OUT ($BE),A
site 00686   ; IN A,($DC)
site 0068B   ; IN A,($DC)
site 00690   ; IN A,($DD)
site 006B0   ; OUT ($DE),A
site 006B2   ; IN A,($DC)
site 006B7   ; OUT ($DE),A
site 006B9   ; IN A,($DC)
site 006C4   ; OUT ($DE),A
site 006C6   ; IN A,($DC)
site 006D1   ; OUT ($DE),A
site 006D3   ; IN A,($DC)
site 006E5   ; OUT ($DE),A
site 006E7   ; IN A,($DC)
site 006F2   ; OUT ($DE),A
site 006F4   ; IN A,($DC)
site 00738   ; OUT ($DE),A
site 0073A   ; IN A,($DC)
site 0073F   ; IN A,($DD)
site 00749   ; OUT ($DE),A
site 0074B   ; IN A,($DC)
site 0075D   ; OUT ($DE),A
site 0075F   ; IN A,($DC)
site 0076A   ; OUT ($DE),A
site 0076C   ; IN A,($DC)
site 00777   ; OUT ($DE),A
site 00779   ; IN A,($DD)
site 00784   ; OUT ($DE),A
site 00786   ; IN A,($DD)
site 007CE   ; OUT ($BE),A
site 00F06   ; OUTI
site 01E68   ; OUT ($BE),A
site 01E6D   ; OUT ($BE),A
site 01F0D   ; OUT ($BE),A
site 01F13   ; OUT ($BE),A
site 01F5D   ; OUT ($BE),A
site 01F71   ; OUT ($BE),A
site 02586   ; IN A,($BE)
site 02844   ; OUT ($BE),A
site 0284A   ; OUT ($BE),A
site 02850   ; OUT ($BE),A
site 02856   ; OUT ($BE),A
site 02861   ; OUT ($BE),A
site 02867   ; OUT ($BE),A
site 0286D   ; OUT ($BE),A
site 02873   ; OUT ($BE),A
site 034F7   ; OUT ($7F),A
site 035D8   ; OUT ($7F),A
site 035E8   ; OUT ($7F),A
site 038D0   ; OUT ($7F),A
site 03932   ; OUT ($7F),A
site 0394C   ; OTIR
mapst 000BB   ; LD ($FFFF),A
mapst 00656   ; LD ($FFFF),A
mapst 00714   ; LD ($FFFF),A
mapst 007E5   ; LD ($FFFF),A
mapst 00E49   ; LD ($FFFF),A
mapst 00EDA   ; LD ($FFFF),A
mapst 01D67   ; LD ($FFFF),A
mapst 03A2D   ; LD ($FFFF),A
# CHECK cartarea_store at 01847 ($1847 bank 0): LD ($0818),HL $0818,$0819
# CHECK cartarea_store at 04107 ($4107 bank 1): LD ($B547),HL $B547,$B548
# CHECK cartarea_store at 04130 ($4130 bank 1): LD (BC),A $1808
# CHECK cartarea_store at 0436E ($436E bank 1): LD ($3001),HL $3001,$3002
# CHECK cartarea_store at 04472 ($4472 bank 1): LD ($6040),HL $6040,$6041
# CHECK cartarea_store at 04476 ($4476 bank 1): LD ($8060),HL $8060,$8061
# CHECK cartarea_store at 04483 ($4483 bank 1): LD ($A040),HL $A040,$A041
# CHECK cartarea_store at 04487 ($4487 bank 1): LD ($8060),HL $8060,$8061
# CHECK cartarea_store at 0448C ($448C bank 1): LD ($A001),HL $A001,$A002
# CHECK cartarea_store at 04490 ($4490 bank 1): LD ($A021),HL $A021,$A022
# CHECK cartarea_store at 04494 ($4494 bank 1): LD ($A041),HL $A041,$A042
# CHECK cartarea_store at 04498 ($4498 bank 1): LD ($A061),HL $A061,$A062
# CHECK cartarea_store at 0449D ($449D bank 1): LD ($6001),HL $6001,$6002
# CHECK cartarea_store at 04824 ($4824 bank 1): LD (HL),H $2500
# CHECK cartarea_store at 0482A ($482A bank 1): LD (BC),A $9C64
# CHECK cartarea_store at 04830 ($4830 bank 1): LD (HL),H $2503
# CHECK cartarea_store at 0483A ($483A bank 1): LD (BC),A $7C84
# CHECK cartarea_store at 069FC ($69FC bank 1): LD (BC),A $B000
# CHECK cartarea_store at 06A08 ($6A08 bank 1): LD (BC),A $B000
# CHECK cartarea_store at 06A16 ($6A16 bank 1): LD (BC),A $B000
# CHECK cartarea_store at 06A1A ($6A1A bank 1): LD (BC),A $B000
# CHECK cartarea_store at 06A2C ($6A2C bank 1): LD (HL),C $0040,$08BE,$09BE,$0ABE...
# CHECK cartarea_store at 074FC ($74FC bank 1): LD (BC),A $B000
# CHECK cartarea_store at 07508 ($7508 bank 1): LD (BC),A $B000
# CHECK cartarea_store at 07516 ($7516 bank 1): LD (BC),A $B000
# CHECK cartarea_store at 0751A ($751A bank 1): LD (BC),A $B000
# CHECK cartarea_store at 0752C ($752C bank 1): LD (HL),C $0040,$08BE,$09BE,$0ABE...
# CHECK ram_exec at 00380 ($0380 bank 0): CALL C,$CACD $CACD
# CHECK ram_exec at 02820 ($2820 bank 0): CALL C,$DDC9 $DDC9
# CHECK ram_exec at 0410B ($410B bank 1): JP Z,$DF47 $DF47
# CHECK ram_exec at 04113 ($4113 bank 1): JP Z,$DF47 $DF47
# CHECK indirect_unresolved at 00052 ($0052 bank 0): RET 
# CHECK indirect_unresolved at 065B2 ($65B2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 066B2 ($66B2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 069B2 ($69B2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 069B2 ($69B2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 069B2 ($69B2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 069D5 ($69D5 bank 1): RET Z 
# CHECK indirect_unresolved at 069E3 ($69E3 bank 1): RET Z 
# CHECK indirect_unresolved at 06AB2 ($6AB2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 06EB2 ($6EB2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 06EB2 ($6EB2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 06EB2 ($6EB2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 074B2 ($74B2 bank 1): JP (HL) 
# CHECK indirect_unresolved at 074D5 ($74D5 bank 1): RET Z 
# CHECK indirect_unresolved at 074E3 ($74E3 bank 1): RET Z 
# CHECK indirect_unresolved at 075B2 ($75B2 bank 1): JP (HL) 
# CHECK bank_unresolved at 00601 ($0601 bank 0): JP PO,$BFD3 $BFD3
# CHECK bank_unresolved at 06559 ($6559 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06567 ($6567 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06575 ($6575 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06587 ($6587 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06595 ($6595 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 065A3 ($65A3 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06687 ($6687 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06695 ($6695 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 066A3 ($66A3 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06959 ($6959 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06967 ($6967 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06975 ($6975 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06987 ($6987 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06995 ($6995 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 069A3 ($69A3 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 069B6 ($69B6 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 069C7 ($69C7 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 069D6 ($69D6 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 069E4 ($69E4 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 069F6 ($69F6 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 06A30 ($6A30 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 06A3D ($6A3D bank 1): CALL PE,$9FD2 $9FD2
# CHECK bank_unresolved at 06A4C ($6A4C bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 06A59 ($6A59 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06A67 ($6A67 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06A75 ($6A75 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06A87 ($6A87 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06A95 ($6A95 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06AA3 ($6AA3 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06E59 ($6E59 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06E67 ($6E67 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06E75 ($6E75 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06E87 ($6E87 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06E95 ($6E95 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 06EA3 ($6EA3 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 074C7 ($74C7 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 074D6 ($74D6 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 074E4 ($74E4 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 074F6 ($74F6 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 07530 ($7530 bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 0753D ($753D bank 1): CALL PE,$9FD2 $9FD2
# CHECK bank_unresolved at 0754C ($754C bank 1): JP NC,$979F $979F
# CHECK bank_unresolved at 07559 ($7559 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 07567 ($7567 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 07575 ($7575 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 07587 ($7587 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 07595 ($7595 bank 1): CALL NC,$9FD2 $9FD2
# CHECK bank_unresolved at 075A3 ($75A3 bank 1): CALL NC,$9FD2 $9FD2
# 59 sites in bank 1 ($655D-$75A7, writes to ports $B1 and $9F) dropped: the scanner
# reached graphics data through a table it read too long; none ran in the detector run.
# low-confidence byte patterns checked by hand, real code: VDP, PSG and region-check routines (a write to port $3F, a read of port $DD) not run in the detector run
site 005A7   ; OUT ($BE),A
site 005AD   ; IN A,($BE)
site 00619   ; OUT ($BF),A
site 0061D   ; OUT ($BF),A
site 01E84   ; OUT ($BE),A
site 01E89   ; OUT ($BE),A
site 01E9D   ; OUT ($BE),A
site 01EA3   ; OUT ($BE),A
site 01EDA   ; OUT ($BE),A
site 01EDF   ; OUT ($BE),A
site 02027   ; OUT (C),D
site 02036   ; OUT ($3F),A
site 02038   ; IN A,($DD)
site 02042   ; OUT ($3F),A
site 02044   ; IN A,($DD)
site 0204D   ; OUT ($3F),A
site 03952   ; OUT ($7F),A
site 03957   ; OUT ($7F),A
# the other low-confidence byte patterns are data or instruction operands
