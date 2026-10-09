# hangon, drafted by tools/mkspec.py from sitescan output.
name Hang On
cart 071B045E
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00017   ; OUT ($BF),A
site 0001A   ; OUT ($BF),A
otir 00027   ; OUTI
site 00039   ; IN A,($BF)
site 00044   ; OUT ($7F),A
site 00048   ; OUT ($7F),A
site 0004C   ; OUT ($7F),A
site 00050   ; OUT ($7F),A
site 001D5   ; IN A,($DD)
site 00274   ; OUT ($BE),A
site 002B2   ; OUTI
site 002C4   ; OUTI
site 002C8   ; OUTI
site 0034F   ; OUTI
site 00361   ; OUTI
site 00365   ; OUTI
site 00606   ; OUT ($BE),A
site 0060B   ; OUT ($BE),A
site 00610   ; OUT ($BF),A
site 00613   ; OUT ($BF),A
site 0061D   ; OUT ($BE),A
site 00625   ; IN A,($BE)
site 0062F   ; OUT ($BE),A
site 0063D   ; IN A,($BE)
site 00665   ; OUT ($BE),A
site 0066B   ; OUT ($BE),A
site 00682   ; OUT ($BE),A
site 00688   ; OUT ($BE),A
site 006A1   ; OUT ($BE),A
site 006AD   ; OUT ($BF),A
site 006B1   ; OUT ($BF),A
site 006B8   ; OUT ($BF),A
site 006BC   ; OUT ($BF),A
site 006D2   ; IN A,($BF)
site 0076A   ; IN A,($DC)
site 00967   ; OUT ($BE),A
site 0096D   ; OUT ($BE),A
site 0098C   ; OUT ($BE),A
site 00992   ; OUT ($BE),A
site 02480   ; OUT ($BE),A
site 02486   ; OUT ($BE),A
site 0248B   ; OUT ($BF),A
site 02490   ; OUT ($BF),A
site 02493   ; OUT ($BE),A
site 030C7   ; OUT ($BF),A
site 030CB   ; OUT ($BF),A
site 030D1   ; OUT ($BE),A
site 030EA   ; OUT ($BF),A
site 030EE   ; OUT ($BF),A
site 030F4   ; OUT ($BE),A
site 035C7   ; OUT ($BE),A
site 035CD   ; OUT ($BE),A
site 03699   ; OUT ($BE),A
site 0369F   ; OUT ($BE),A
site 036B6   ; OUT ($BE),A
site 036BB   ; OUT ($BE),A
site 036E6   ; OUT ($BE),A
site 036EC   ; OUT ($BE),A
site 036F6   ; OUT ($BE),A
site 036FC   ; OUT ($BE),A
site 03717   ; OUT ($BE),A
site 0371D   ; OUT ($BE),A
site 03723   ; OUT ($BE),A
site 03729   ; OUT ($BE),A
site 03920   ; OUT ($BE),A
site 0392B   ; OUT ($BE),A
site 03936   ; OUT ($BE),A
site 03A68   ; OUT ($BE),A
site 03A71   ; OUT ($BE),A
site 071E1   ; OUT ($7F),A
site 072EF   ; OUT ($7F),A
site 072F9   ; OUT ($7F),A
site 07301   ; OUT ($7F),A
site 07646   ; OUT ($7F),A
site 076E4   ; OUT ($7F),A
site 076FB   ; OTIR
site 07704   ; OUT ($7F),A
site 07708   ; OUT ($7F),A
# CHECK cartarea_store at 007AE ($07AE bank 0): LD (HL),A $4004,$4005,$4006,$4007...
# CHECK ram_exec at 0003C ($003C bank 0): JP P,$C4D0 $C4D0
# CHECK indirect_unresolved at 07152 ($7152 bank 1): JP (HL) 
# CHECK indirect_unresolved at 078C0 ($78C0 bank 1): JP (HL) 
# CHECK low: site 003B3  IN A,($7E)  (v_counter)
# CHECK low: site 003BF  OUT ($BF),A  (vdp_control)
# CHECK low: site 003C3  OUT ($BF),A  (vdp_control)
# CHECK low: site 003CD  OUT ($BF),A  (vdp_control)
# CHECK low: site 003D1  OUT ($BF),A  (vdp_control)
# CHECK low: site 003D4  OUT ($BF),A  (vdp_control)
# CHECK low: site 003D8  OUT ($BF),A  (vdp_control)
# CHECK low: site 02665  IN C,(C)  (port in C)
# The line interrupt handler is copied from ROM $03B3-$03DC to $C4D0. With
# the raster hook below its interrupts are not delivered, but its I/O is
# patched in the ROM source all the same, so the copy holds RST io + op.
site 003B3   ; IN A,($7E)
site 003BF   ; OUT ($BF),A
site 003C3   ; OUT ($BF),A
site 003CD   ; OUT ($BF),A
site 003D1   ; OUT ($BF),A
site 003D4   ; OUT ($BF),A
site 003D8   ; OUT ($BF),A
plain 003BF
plain 003C3
plain 003CD
plain 003D1
plain 003D4
plain 003D8
rastercode hangon-raster.asm
