# R.C. Grand Prix (USA, Europe, Brazil) (En), CRC32 54316FEA, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - The line interrupt goes through the word at $C372; the game stores only $15DD there
#   (at $1585), which sets register 8 from ($C380). It runs on the title screen, where
#   register 10 is $B7: the credits row (lines 184-191) scrolls under a still picture.
#   Through the runtime's line event the new H came some lines late and tore the row.
#   The rastercode routine gives H = 0 to lines 0-183 and ($C380) to lines 184-191.
# - The io vector is at $00. The game's code has no RST $00, and no call or jump to $0000.
# - The jump tables at $1A5E-$1A7C, read at $1AF4, $1B16, $1B34, $1B51 and $1B6C, lead
#   only to $1B78, $1B8A, $1B9C and $1BAE, which move race order bytes in RAM: no I/O.
# - The byte scan rows at $2662 and $3144 are in code that no call, jump, relative jump,
#   address load or table word names (from $2645 and from $3134; verdict unused).
# - Slot 2 code is bank 9 (the sound driver) and bank 10 (called at $8003 from $4D09).
#   The other banks mapped there are data; the low-rated byte scan rows in banks 7 and 11
#   are in that data.
# - The VRAM copy $24C5 calls an unrolled OUTI loop at $24D7 that ends when B is 0, and the
#   CRAM copy $255F loops OUTI at $256A until B is 0. Through the runtime each OUTI costs
#   about 2000 cycles and the race does about 100 a step, so the Next fell behind the
#   Master System's one step a frame. Each loop becomes one OTIR through the runtime: the
#   same bytes to the same port, ending with the same HL, B = 0 and Z set. The OUTI sites
#   of the loop at $24D7 stay patched; nothing reaches them now.
name R.C. Grand Prix
cart 54316FEA
hz any
rastercode rc-grand-prix-raster.asm
# No free RST vector: the JP at $0000 becomes the vector, the game
# starts at its target.
vector 00 io
start 0100
asm 00101 2   ; IM 1 -> IM 2
    im 2
endasm
site 0003A   ; IN A,($BF)
site 00113   ; IN A,($DC)
site 00116   ; IN A,($DD)
site 015E0   ; OUT ($BF),A
site 015E7   ; OUT ($BF),A
site 024A1   ; OUT ($BF),A
site 024A8   ; OUT ($BF),A
site 024AD   ; OUT ($BE),A
site 024B2   ; OUT ($BE),A
site 024C7   ; OUT ($BF),A
site 024CE   ; OUT ($BF),A
asm 024D2 3   ; CALL $24D7, the OUTI loop (B bytes from HL, 0 = 256) -> one OTIR
    rst $00
    db $B3
    nop
endasm
site 024D7   ; OUTI
site 024DC   ; OUTI
site 024E1   ; OUTI
site 024E6   ; OUTI
site 024EB   ; OUTI
site 024F0   ; OUTI
site 024F5   ; OUTI
site 024FA   ; OUTI
site 024FF   ; OUTI
site 02504   ; OUTI
site 0250C   ; OUT (C),E
site 02511   ; OUT ($BF),A
site 02515   ; OTIR
site 02538   ; OUT ($BF),A
site 0253F   ; OUT ($BF),A
site 02545   ; OUT ($BE),A
site 0254B   ; OUT ($BE),A
site 02554   ; OUT ($BF),A
site 0255B   ; OUT ($BF),A
site 02562   ; OUT (C),E
site 02566   ; OUT (C),A
asm 0256A 5   ; OUTI : NOP : JR NZ,$256A (CRAM, B bytes from HL) -> one OTIR
    rst $00
    db $B3
    nop
    nop
    nop
endasm
site 02F80   ; IN A,($DC)
site 02F83   ; IN A,($DD)
site 03679   ; OUT ($BF),A
site 0367E   ; OUT ($BF),A
site 03684   ; OUTI
site 036F4   ; OUT ($BF),A
site 036F9   ; OUT ($BF),A
site 03704   ; OUTI
site 03733   ; OUT ($BF),A
site 03738   ; OUT ($BF),A
site 0373E   ; OUTI
site 24026   ; OTIR
site 24042   ; OUT (C),A
site 24054   ; OUT (C),L
site 2405A   ; OUT (C),A
site 24062   ; OUT (C),A
site 24067   ; OUT (C),A
mapst 0008A   ; LD ($FFFF),A
mapst 00091   ; LD ($FFFF),A
mapst 00108   ; LD ($FFFF),A
mapst 00288   ; LD ($FFFF),A
mapst 00294   ; LD ($FFFF),A
mapst 0038A   ; LD ($FFFF),A
mapst 00442   ; LD ($FFFF),A
mapst 00468   ; LD ($FFFF),A
mapst 0051F   ; LD ($FFFF),A
mapst 0052B   ; LD ($FFFF),A
mapst 00537   ; LD ($FFFF),A
mapst 00543   ; LD ($FFFF),A
mapst 0054F   ; LD ($FFFF),A
mapst 00560   ; LD ($FFFF),A
mapst 00571   ; LD ($FFFF),A
mapst 00582   ; LD ($FFFF),A
mapst 0058F   ; LD ($FFFF),A
mapst 0059B   ; LD ($FFFF),A
mapst 005A7   ; LD ($FFFF),A
mapst 005B3   ; LD ($FFFF),A
mapst 0063B   ; LD ($FFFF),A
mapst 00661   ; LD ($FFFF),A
mapst 0086A   ; LD ($FFFF),A
mapst 0088D   ; LD ($FFFF),A
mapst 00BBB   ; LD ($FFFF),A
mapst 00BDE   ; LD ($FFFF),A
mapst 00CA1   ; LD ($FFFF),A
mapst 00DCB   ; LD ($FFFF),A
mapst 00DE5   ; LD ($FFFF),A
mapst 00E04   ; LD ($FFFF),A
mapst 00EF5   ; LD ($FFFF),A
mapst 00F83   ; LD ($FFFF),A
mapst 00F9D   ; LD ($FFFF),A
mapst 00FAF   ; LD ($FFFF),A
mapst 0110E   ; LD ($FFFF),A
mapst 01175   ; LD ($FFFF),A
mapst 0117A   ; LD ($FFFF),A
mapst 01214   ; LD ($FFFF),A
mapst 01292   ; LD ($FFFF),A
mapst 012AA   ; LD ($FFFF),A
mapst 012BB   ; LD ($FFFF),A
mapst 01306   ; LD ($FFFF),A
mapst 01315   ; LD ($FFFF),A
mapst 0144A   ; LD ($FFFF),A
mapst 014BC   ; LD ($FFFF),A
mapst 0151D   ; LD ($FFFF),A
mapst 01579   ; LD ($FFFF),A
mapst 01634   ; LD ($FFFF),A
mapst 017FD   ; LD ($FFFF),A
mapst 0186A   ; LD ($FFFF),A
mapst 0204B   ; LD ($FFFF),A
mapst 0209E   ; LD ($FFFF),A
mapst 020AC   ; LD ($FFFF),A
mapst 020C9   ; LD ($FFFF),A
mapst 020D6   ; LD ($FFFF),A
mapst 02174   ; LD ($FFFF),A
mapst 0218B   ; LD ($FFFF),A
mapst 021CC   ; LD ($FFFF),A
mapst 021DA   ; LD ($FFFF),A
mapst 021F7   ; LD ($FFFF),A
mapst 02204   ; LD ($FFFF),A
mapst 022D5   ; LD ($FFFF),A
mapst 02343   ; LD ($FFFF),A
mapst 023E8   ; LD ($FFFF),A
mapst 02452   ; LD ($FFFF),A
mapst 02487   ; LD ($FFFF),A
mapst 02573   ; LD ($FFFF),A
mapst 02F38   ; LD ($FFFF),A
mapst 02FEB   ; LD ($FFFF),A
mapst 02FFF   ; LD ($FFFF),A
mapst 030CE   ; LD ($FFFF),A
mapst 0312F   ; LD ($FFFF),A
mapst 0315D   ; LD ($FFFF),A
mapst 03221   ; LD ($FFFF),A
mapst 032B8   ; LD ($FFFF),A
mapst 03774   ; LD ($FFFF),A
mapst 0384A   ; LD ($FFFF),A
mapst 03AE7   ; LD ($FFFF),A
mapst 03B40   ; LD ($FFFF),A
mapst 04456   ; LD ($FFFF),A
mapst 0446A   ; LD ($FFFF),A
mapst 04486   ; LD ($FFFF),A
mapst 0450E   ; LD ($FFFF),A
mapst 04755   ; LD ($FFFF),A
mapst 047A9   ; LD ($FFFF),A
mapst 0487A   ; LD ($FFFF),A
mapst 04A7D   ; LD ($FFFF),A
mapst 04A9A   ; LD ($FFFF),A
mapst 04C07   ; LD ($FFFF),A
mapst 04CFC   ; LD ($FFFF),A
mapst 04D60   ; LD ($FFFF),A
mapst 04D72   ; LD ($FFFF),A
mapst 04D7E   ; LD ($FFFF),A
