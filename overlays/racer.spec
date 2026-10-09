# Canyon Racer 0.01alpha (haroldoop, Unlicense). 7626 bytes.
# Sites: the 27 from research/4-work/out/canyonracer.io.tsv, plus $1BD6,
# which a linear disassembly of the code ($0100-$1DC9) finds in load_tiles
# (the padding branch for tiles with fewer than 4 bitplanes; never runs).
# The game's code uses no RST; $0010-$0012 is z88dk header text.
name Canyon Racer 0.01alpha
cart EEAD16C7
vector 10 out_n
vector 18 in_n
vector 20 ed
site 0135   ; OTIR
site 1B6E   ; OUT ($BF),A
site 1B72   ; OUT ($BF),A
site 1B76   ; OTIR
site 1BAD   ; OUT ($BF),A
site 1BB2   ; OUT ($BF),A
site 1BC4   ; OUT ($BE),A
site 1BD6   ; OUT ($BE),A
site 1D07   ; IN A,($DC)
site 1D15   ; OUT ($BF),A
site 1D19   ; OUT ($BF),A
site 1D1C   ; OUT ($BF),A
site 1D20   ; OUT ($BF),A
site 1D66   ; OUT ($BE),A
site 1D6A   ; OUT ($BE),A
site 1D75   ; OUT ($BF),A
site 1D7A   ; OUT ($BF),A
site 1D8D   ; OUT ($BF),A
site 1D91   ; OUT ($BF),A
site 1D94   ; OUT ($BE),A
site 1D9A   ; OUT ($BF),A
site 1D9E   ; OUT ($BF),A
site 1DA1   ; OUT ($BE),A
site 1DA4   ; OUT ($BE),A
site 1DAE   ; OUT ($BF),A
site 1DB1   ; OUT ($BF),A
site 1DBE   ; IN A,($7E)
site 1DC1   ; IN A,($7E)
# the framework's interrupts need IM 2 (vector table at $FD00)
asm 0122 2   ; IM 1 -> IM 2
    im 2
endasm
