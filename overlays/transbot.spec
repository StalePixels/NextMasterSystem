# TransBot, drafted by tools/mkspec.py from sitescan output.
name TransBot
cart 4BC42857
vector 28 io
asm 008E 2   ; IM 1 -> IM 2
    im 2
endasm
site 00C2   ; IN A,($BF)
site 00CB   ; OTIR
site 04FD   ; IN A,($BF)
site 0506   ; OTIR
site 0FE1   ; IN A,($BF)
site 0FF1   ; OUT ($BF),A
site 0FF5   ; OUT ($BF),A
site 0FF9   ; OUT ($BF),A
site 0FFD   ; OUT ($BF),A
site 1005   ; OUT ($BF),A
site 1009   ; OUT ($BF),A
site 100D   ; OUT ($BF),A
site 1011   ; OUT ($BF),A
site 1021   ; IN A,($DD)
site 2493   ; IN A,($DC)
site 2496   ; IN A,($DD)
site 24A4   ; OUT ($DE),A
site 24A6   ; IN A,($DC)
site 24A9   ; IN A,($DD)
site 24B4   ; OUT ($DE),A
site 24B6   ; IN A,($DC)
site 24C6   ; OUT ($DE),A
site 24C8   ; IN A,($DC)
site 24D2   ; OUT ($DE),A
site 24D4   ; IN A,($DC)
site 24DE   ; OUT ($DE),A
site 24E0   ; IN A,($DD)
site 24EA   ; OUT ($DE),A
site 24EC   ; IN A,($DD)
site 24FF   ; IN A,($DC)
site 2507   ; OUT ($DE),A
site 2509   ; IN A,($DC)
site 250E   ; OUT ($DE),A
site 2510   ; IN A,($DC)
site 251A   ; OUT ($DE),A
site 251C   ; IN A,($DC)
site 2526   ; OUT ($DE),A
site 2528   ; IN A,($DC)
site 2532   ; OUT ($DE),A
site 2534   ; IN A,($DC)
site 253E   ; OUT ($DE),A
site 2540   ; IN A,($DC)
site 2787   ; OUT ($BE),A
site 278C   ; OUT ($BE),A
site 27C4   ; OUT ($BE),A
site 27F5   ; OUT ($7F),A
site 27F9   ; OUT ($7F),A
site 27FD   ; OUT ($7F),A
site 2801   ; OUT ($7F),A
site 283E   ; OUT ($BF),A
site 2842   ; OUT ($BF),A
site 2847   ; OUT ($DF),A
site 284B   ; OUT ($DE),A
site 284D   ; IN A,($DE)
site 2859   ; OUT ($DE),A
site 285B   ; IN A,($DE)
site 286B   ; OUT ($DE),A
site 2896   ; OUT ($BF),A
site 289B   ; OUT ($BF),A
site 28A4   ; OUT ($BE),A
site 28B5   ; OUT ($BE),A
site 28C5   ; OUT ($BE),A
site 28CA   ; OUT ($BE),A
site 28DA   ; OUT ($BE),A
site 28E0   ; OUT ($BE),A
site 28F1   ; OUT ($BF),A
site 28F6   ; OUT ($BF),A
site 28FB   ; OUT ($BE),A
site 2918   ; OUT (C),D
site 2E6F   ; OUT ($BE),A
site 2E75   ; OUT ($BE),A
site 2EA7   ; OUT ($BE),A
site 2EAD   ; OUT ($BE),A
site 348D   ; OUT ($7F),A
site 34A6   ; OTIR
site 34B0   ; OUT ($7F),A
# CHECK indirect_unresolved at 1B29: JP (HL) 
site 34B5   # low confidence in the scan; PSG mute routines, real code
site 34BA   ; OUT ($7F),A
site 34BF   ; OUT ($7F),A
