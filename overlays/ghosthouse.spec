# Ghost House, drafted by tools/mkspec.py from sitescan output.
name Ghost House
cart F1F8FF2D
# No free RST vector: $0000-$0002 (the game's interrupt-disable and the start of its stack setup) becomes the vector,
# the game starts at $0004 with the SP its LD SP,nn set.
vector 00 io
start 0004 C18E
asm 0004 2   ; IM 1 -> IM 2
    im 2
endasm
site 000B   ; IN A,($BE)
site 0010   ; IN A,($BE)
site 001D   ; OUT ($BE),A
otir 002C   ; OUTI
site 0131   ; OUT ($DF),A
site 0139   ; OUT ($DE),A
site 013B   ; IN A,($DE)
site 01E7   ; IN A,($BF)
site 01FA   ; IN A,($DD)
site 04C5   ; OUT ($BE),A
site 08B8   ; OUT ($BE),A
site 08BD   ; OUT ($BE),A
site 08C2   ; OUT ($BE),A
site 08C7   ; OUT ($BE),A
site 0CB8   ; OUTI
site 0CBE   ; OUT (C),A
site 0CD7   ; OUT ($BE),A
site 0CDC   ; OUT ($BE),A
site 0CEB   ; OUTI
site 0CF1   ; OUT (C),A
site 0D0A   ; OUTI
site 0D1F   ; OTIR
site 0D5C   ; OUT ($BE),A
site 0D63   ; OUT ($BF),A
site 0D68   ; OUT ($BF),A
site 0D6C   ; OUT ($BF),A
site 0D6F   ; OUT ($BF),A
site 0E56   ; OUT ($BF),A
site 0E59   ; OUT ($BF),A
site 0E5C   ; OUT ($BE),A
site 0EAA   ; IN A,($DC)
site 0EAF   ; IN A,($DD)
site 0EBC   ; IN A,($DC)
site 0EC8   ; OUT ($DE),A
site 0ECA   ; IN A,($DC)
site 0ECF   ; OUT ($DE),A
site 0ED1   ; IN A,($DC)
site 0EDC   ; OUT ($DE),A
site 0EDE   ; IN A,($DC)
site 0EE9   ; OUT ($DE),A
site 0EEB   ; IN A,($DC)
site 0EFD   ; OUT ($DE),A
site 0EFF   ; IN A,($DC)
site 0F0A   ; OUT ($DE),A
site 0F0C   ; IN A,($DC)
site 0F3B   ; OUT ($DE),A
site 0F3D   ; IN A,($DC)
site 0F42   ; IN A,($DD)
site 0F4C   ; OUT ($DE),A
site 0F4E   ; IN A,($DC)
site 0F60   ; OUT ($DE),A
site 0F62   ; IN A,($DC)
site 0F6D   ; OUT ($DE),A
site 0F6F   ; IN A,($DC)
site 0F7A   ; OUT ($DE),A
site 0F7C   ; IN A,($DD)
site 0F87   ; OUT ($DE),A
site 0F89   ; IN A,($DD)
site 3B17   ; OUT ($BE),A
site 4CF5   ; OUT ($7F),A
site 4D5B   ; OUT ($7F),A
site 4D78   ; OTIR
# CHECK indirect_unresolved at 357C: JP (HL) 
