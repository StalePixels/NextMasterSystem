# Fantasy Zone (World) (Rev 1), 65D7E4E0, drafted by tools/mkspec.py from sitescan output.
name Fantasy Zone
cart 65D7E4E0
hz any		; No-Intro regions World
vector 08 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 0010B   ; IN A,($BF)
site 0010D   ; IN A,($DD)
site 00182   ; OUT ($BF),A
site 00187   ; OUT ($BF),A
site 0018F   ; OUT ($BE),A
site 00193   ; OUT ($BF),A
site 00196   ; OUT ($BF),A
otir 001A5   ; OUTI
site 001B4   ; OUTI
site 001BA   ; OUT (C),A
site 001C2   ; OUT ($BF),A
site 001C5   ; OUT ($BF),A
site 001C9   ; IN A,($BE)
site 001EC   ; OUT ($BE),A
site 0020C   ; OUT ($BE),A
site 0023B   ; OUT ($BE),A
site 00240   ; OUT ($BE),A
site 0024F   ; OUTI
site 00268   ; OUTI
site 0026E   ; OUT (C),A
site 00286   ; OUT ($BE),A
site 002A7   ; OUT (C),D
site 002D4   ; OUTI
site 002E4   ; OUTI
site 002E6   ; OUTI
site 00300   ; OUTI
site 0030D   ; OUTD
site 00315   ; OUT ($BE),A
site 00322   ; OUTI
site 00324   ; OUTI
site 00330   ; OUTI
site 00332   ; OUTD
site 0033F   ; OUTD
site 0034A   ; OTIR
site 0034D   ; OUT ($BE),A
site 00386   ; OUT ($BF),A
site 00389   ; OUT ($BF),A
site 0038C   ; OUT ($BE),A
site 00507   ; OUT ($BE),A
site 0050B   ; OUT ($BE),A
site 005D7   ; OUT ($BE),A
site 005DE   ; OUT ($BE),A
site 006DE   ; OUT ($3F),A
site 006E2   ; IN A,($DD)
site 006EC   ; OUT ($3F),A
site 006F0   ; IN A,($DD)
site 006F9   ; OUT ($3F),A
site 007C2   ; OUT ($BE),A
site 007D3   ; OTIR
site 007E7   ; OTIR
site 007FB   ; OTIR
site 0080F   ; OTIR
site 0083A   ; OUT ($BE),A
site 008AF   ; OUT ($DF),A
site 008BB   ; OUT ($DE),A
site 008BD   ; IN A,($DE)
site 008D0   ; IN A,($DC)
site 008D5   ; IN A,($DC)
site 008DA   ; IN A,($DD)
site 008EA   ; OUT ($DE),A
site 008EC   ; IN A,($DC)
site 008F1   ; OUT ($DE),A
site 008F3   ; IN A,($DC)
site 008FE   ; OUT ($DE),A
site 00900   ; IN A,($DC)
site 0090B   ; OUT ($DE),A
site 0090D   ; IN A,($DC)
site 0091F   ; OUT ($DE),A
site 00921   ; IN A,($DC)
site 0092C   ; OUT ($DE),A
site 0092E   ; IN A,($DC)
site 00945   ; OUT ($DE),A
site 00947   ; IN A,($DC)
site 0094C   ; IN A,($DD)
site 00956   ; OUT ($DE),A
site 00958   ; IN A,($DC)
site 0096A   ; OUT ($DE),A
site 0096C   ; IN A,($DC)
site 00977   ; OUT ($DE),A
site 00979   ; IN A,($DC)
site 00984   ; OUT ($DE),A
site 00986   ; IN A,($DD)
site 00991   ; OUT ($DE),A
site 00993   ; IN A,($DD)
site 009BF   ; OTIR
site 00C2D   ; OUT (C),H
site 00C2F   ; OUT (C),L
site 01515   ; OUT ($BF),A
site 0151A   ; OUT ($BF),A
site 0151D   ; OUT ($BE),A
site 01522   ; OUT ($BE),A
site 05972   ; OTIR
site 0662C   ; OUT ($BE),A
site 0666E   ; OUT ($BE),A
site 06D1B   ; OUT ($BE),A
site 0788A   ; OUT (C),L
site 0788C   ; OUT (C),H
site 078A1   ; OUT ($BE),A
site 078A3   ; OUT ($BE),A
site 1DF77   ; OUT ($7F),A
site 1E3BD   ; OUT ($7F),A
site 1E3E6   ; OTIR
mapst 0007D   ; LD ($FFFF),A
mapst 0014C   ; LD ($FFFF),A
mapst 00153   ; LD ($FFFF),A
mapst 0040F   ; LD ($FFFF),A
mapst 00424   ; LD ($FFFF),A
mapst 00653   ; LD ($FFFF),A
mapst 009F2   ; LD ($FFFF),A
mapst 00A04   ; LD ($FFFF),A
mapst 00D13   ; LD ($FFFF),A
mapst 00D32   ; LD ($FFFF),A
mapst 00D42   ; LD ($FFFF),A
mapst 00D82   ; LD ($FFFF),A
mapst 00E73   ; LD ($FFFF),A
mapst 00E99   ; LD ($FFFF),A
mapst 00EBA   ; LD ($FFFF),A
mapst 010C0   ; LD ($FFFF),A
mapst 04DDF   ; LD ($FFFF),A
mapst 04DEE   ; LD ($FFFF),A
mapst 04EDA   ; LD ($FFFF),A
mapst 04EFE   ; LD ($FFFF),A
mapst 053E2   ; LD ($FFFF),A
mapst 0550F   ; LD ($FFFF),A
mapst 05536   ; LD ($FFFF),A
mapst 05D28   ; LD ($FFFF),A
mapst 05D46   ; LD ($FFFF),A
mapst 07BF4   ; LD ($FFFF),A
mapst 07D55   ; LD ($FFFF),A
mapst 07E70   ; LD ($FFFF),A
# CHECK cartarea_store at 00B34 ($0B34 bank 0): LD ($5531),A $5531
# CHECK indirect_unresolved at 00198 ($0198 bank 0): RET 
# CHECK indirect_unresolved at 00B7C ($0B7C bank 0): RET 
# CHECK indirect_unresolved at 017C8 ($17C8 bank 0): JP (HL) 
# CHECK indirect_unresolved at 017C8 ($17C8 bank 0): JP (HL) 
# low-confidence byte patterns checked by hand, real code: PSG mute routines in bank 7 (each loads A, writes it to port $7F and returns)
site 1E3EC   ; OUT ($7F),A
site 1E3F1   ; OUT ($7F),A
# the other low-confidence byte patterns are data or instruction operands
# Each EI : HALT waits in the runtime for the game's own frame interrupt, as
# on the Master System, not for the runtime's interrupts too.
eihalt 00A17   ; EI : HALT
eihalt 013CC   ; EI : HALT
