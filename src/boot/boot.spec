# boot, drafted by tools/mkspec.py from sitescan output.
name boot
cart 45DFC266
hz any
vector 08 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 00039   ; IN A,($BF)
site 00072   ; OTIR
site 0007B   ; OTIR
site 0008A   ; OTIR
site 000B6   ; IN A,($DC)
site 000CD   ; OUT ($BF),A
site 000D0   ; OUT ($BF),A
site 000DB   ; OTIR
site 000E4   ; OTIR
site 000FF   ; OUT ($BF),A
site 00103   ; OUT ($BF),A
site 0011D   ; IN A,($BF)
site 00121   ; OUT ($BF),A
site 00125   ; OUT ($BF),A
site 002F5   ; OUT ($BE),A
site 002F9   ; OUT ($BE),A
site 00302   ; OUT ($BE),A
site 00305   ; OUT ($BE),A
site 003BF   ; OUT ($7F),A
site 003D0   ; OUT ($7F),A
site 003DD   ; OUT ($7F),A
site 003E2   ; OUT ($7F),A
