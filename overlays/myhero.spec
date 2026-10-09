# My Hero, drafted by tools/mkspec.py from sitescan output.
name My Hero
cart 62F0C23D
# No free RST vector: the JP at $0000 becomes the vector, the game
# starts at its target.
vector 00 io
start 0085
asm 0089 2   ; IM 1 -> IM 2
    im 2
endasm
site 009A   ; OUT ($DF),A
site 009E   ; OUT ($DE),A
site 00A0   ; IN A,($DE)
site 00AC   ; OUT ($DE),A
site 00AE   ; IN A,($DE)
site 00BE   ; OUT ($DE),A
site 00F0   ; IN A,($BF)
site 00F9   ; OTIR
site 014E   ; IN A,($BF)
site 0150   ; IN A,($DD)
site 01D3   ; OUT ($BE),A
site 01F7   ; OUT ($BE),A
site 02A2   ; OUT ($BE),A
site 2291   ; OUT ($BF),A
site 2295   ; OUT ($BF),A
site 22B1   ; OUT ($BE),A
site 22B9   ; OUT ($BE),A
site 2326   ; OUT ($BF),A
site 232D   ; OUT ($BF),A
site 2472   ; OUT ($BE),A
site 2478   ; OUT ($BE),A
site 24E5   ; OUT ($BE),A
site 24EB   ; OUT ($BE),A
site 24F4   ; OUT ($BE),A
site 24FA   ; OUT ($BE),A
site 257D   ; IN A,($DC)
site 2580   ; IN A,($DD)
site 258E   ; OUT ($DE),A
site 2590   ; IN A,($DC)
site 2593   ; IN A,($DD)
site 259E   ; OUT ($DE),A
site 25A0   ; IN A,($DC)
site 25B0   ; OUT ($DE),A
site 25B2   ; IN A,($DC)
site 25BC   ; OUT ($DE),A
site 25BE   ; IN A,($DC)
site 25C8   ; OUT ($DE),A
site 25CA   ; IN A,($DD)
site 25D4   ; OUT ($DE),A
site 25D6   ; IN A,($DD)
site 25E9   ; IN A,($DC)
site 25F1   ; OUT ($DE),A
site 25F3   ; IN A,($DC)
site 25F8   ; OUT ($DE),A
site 25FA   ; IN A,($DC)
site 2604   ; OUT ($DE),A
site 2606   ; IN A,($DC)
site 2610   ; OUT ($DE),A
site 2612   ; IN A,($DC)
site 261C   ; OUT ($DE),A
site 261E   ; IN A,($DC)
site 2628   ; OUT ($DE),A
site 262A   ; IN A,($DC)
site 28DE   ; OUT ($BF),A
site 28E2   ; OUT ($BF),A
site 2974   ; OUT ($BE),A
site 2978   ; OUT ($BE),A
site 29D9   ; OUT ($BF),A
site 29DD   ; OUT ($BF),A
site 29EF   ; OUT ($BE),A
site 29FE   ; OUT ($BF),A
site 2A03   ; OUT ($BF),A
site 2A0C   ; OUT ($BE),A
site 2A1D   ; OUT ($BE),A
site 2A2D   ; OUT ($BE),A
site 2A32   ; OUT ($BE),A
site 2A42   ; OUT ($BE),A
site 2A48   ; OUT ($BE),A
site 2A59   ; OUT ($BF),A
site 2A5E   ; OUT ($BF),A
site 2A63   ; OUT ($BE),A
site 2A8E   ; OUT ($BF),A
site 2A91   ; OUT ($BF),A
site 2A96   ; IN A,($BE)
site 2ABE   ; OUT ($BE),A
site 2AE6   ; OUT ($BF),A
site 2AEB   ; OUT ($BF),A
site 2AF0   ; OUT ($BE),A
site 2C00   ; OUT ($DE),A
site 2C02   ; IN A,($DD)
site 3340   ; OUT ($7F),A
site 335E   ; OTIR
# CHECK cartarea_store at 4850: LD (BC),A $0278
# CHECK cartarea_store at 4854: LD ($2E02),A $2E02
# CHECK indirect_unresolved at 14C7: CALL $1A52 $1A52
# CHECK indirect_unresolved at 1531: CALL $1A52 $1A52
# CHECK indirect_unresolved at 1A5D: JP (HL) 
# CHECK bank_unresolved at 1553: JP NZ,$8B15 $8B15
# CHECK bank_unresolved at 480C: CALL M,$8088 $8088
site 2A80   # low confidence in the scan; the 1bpp tile loop, real code
