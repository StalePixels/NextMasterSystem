# DataStorm 1.00 (haroldoop, Unlicense). 32768 bytes, SDCC + devkitSMS.
# Sites: the logged ones in research/4-work/out/datastorm.io.tsv, plus
# unexecuted SMSlib/PSGlib sites found by a linear disassembly of the code
# below $2000 (the D3/DB bytes above $2000, and at $024D-$0265, are data).
# The game itself uses RST $08 (at $0202/$0206); $10-$30 are free (zeros).
name DataStorm 1.00
cart 37B775D6
# One io vector for every I/O site: only with it can the builder give a loop its trace form,
# so the loops that copy the sprite table go to the VDP as one block each.
vector 10 io
vector 18 ld_de_a
vector 20 outi_run
# crt0: IM 1 -> IM 2, so the Next line interrupt enters through the framework
asm 0001 2   ; IM 1 -> IM 2
    im 2
endasm
# crt0 mapper init: LD (DE),A with DE = $FFFC..$FFFF
mapper 0077   ; LD (DE),A
mapper 007B   ; LD (DE),A
# 128 unrolled OUTIs, $0099-$0198, RET at $0199
outi 0099 0199
# logged sites
site 12B7   ; OUT ($BF),A
site 12BC   ; OUT ($BF),A
site 1316   ; OUT ($BF),A
site 131C   ; OUT ($BF),A
site 1347   ; OUT ($BF),A
site 134D   ; OUT ($BF),A
site 13A4   ; OUT ($BF),A
site 13A8   ; OUT ($BF),A
site 13E3   ; OUT ($BF),A
site 13E7   ; OUT ($BF),A
site 13F1   ; OUT ($BE),A
site 13FA   ; OUT ($BF),A
site 13FE   ; OUT ($BF),A
site 1408   ; OUT ($BE),A
site 141F   ; OUT ($BF),A
site 1432   ; OUT ($BF),A
site 1442   ; OUT ($BE),A
site 1606   ; OUT ($BF),A
site 1624   ; OUT ($BF),A
site 1634   ; OUT ($BE),A
site 168E   ; OUT ($BF),A
site 16AE   ; OUT ($BF),A
site 16C7   ; OUT ($BE),A
site 1A55   ; OUT ($BF),A
site 1A63   ; OUT ($BF),A
site 1A6C   ; OUT ($BE),A
site 1A7C   ; OUT ($BF),A
site 1A92   ; OUT ($BF),A
site 1A9B   ; OUT ($BE),A
site 1C57   ; OUT ($BF),A
site 1C65   ; OUT ($BF),A
site 1C76   ; OUT ($BF),A
site 1C8C   ; OUT ($BF),A
site 1C9E   ; IN A,($BF)
site 1CB7   ; OUT ($3F),A
site 1CB9   ; IN A,($DE)
site 1CBE   ; IN A,($DC)
site 1CDD   ; OUT ($3F),A
site 1CDF   ; IN A,($DC)
site 1D19   ; OUT ($3F),A
site 1D1D   ; OUT ($3F),A
site 1D1F   ; IN A,($DC)
site 1D27   ; OUT ($3F),A
site 1D29   ; IN A,($DC)
site 1D52   ; OUT ($3F),A
site 1D87   ; OUT ($7F),A
site 1D8B   ; OUT ($7F),A
site 1D95   ; OUT ($7F),A
site 1D9F   ; OUT ($7F),A
site 1E09   ; OUT ($7F),A
site 1E10   ; OUT ($7F),A
site 1E19   ; OUT ($7F),A
site 1E1F   ; OUT ($7F),A
site 1E39   ; OUT ($7F),A
site 1E42   ; OUT ($7F),A
site 1F5B   ; OUT ($7F),A
site 1FF5   ; OUT ($7F),A
# unexecuted library sites (linear disassembly)
site 1362   ; OUT ($BF),A
site 1366   ; OUT ($BF),A
site 1377   ; OUT ($BF),A
site 137B   ; OUT ($BF),A
site 1389   ; OUT ($BF),A
site 138D   ; OUT ($BF),A
site 13B6   ; OUT ($BF),A
site 13BA   ; OUT ($BF),A
site 13C2   ; OUT ($BE),A
site 13D1   ; OUT ($BF),A
site 13D5   ; OUT ($BF),A
site 13DD   ; OUT ($BE),A
site 1460   ; OUT ($BF),A
site 1473   ; OUT ($BF),A
site 1532   ; OUT ($BE),A
site 1561   ; OUT ($BF),A
site 157F   ; OUT ($BF),A
site 158C   ; OUT ($BE),A
site 1592   ; OUT ($BE),A
site 15B4   ; OUT ($BF),A
site 15D2   ; OUT ($BF),A
site 15E0   ; OUT ($BE),A
site 15E6   ; OUT ($BE),A
site 1735   ; OUT ($BF),A
site 1795   ; OUT ($BF),A
site 180B   ; OUT ($BE),A
site 1811   ; OUT ($BE),A
site 1840   ; OUT ($BE),A
site 1848   ; OUT ($BE),A
site 189C   ; OUT ($BE),A
site 18AC   ; OUT ($BE),A
site 1B71   ; OUT ($BF),A
site 1B75   ; OUT ($BF),A
site 1B79   ; IN A,($7E)
site 1B7D   ; IN A,($7F)
site 1B8D   ; OUT ($BF),A
site 1B97   ; OUT ($BF),A
site 1BA7   ; OUT ($BE),A
site 1BC0   ; OUT ($BF),A
site 1BCA   ; OUT ($BF),A
site 1BDA   ; OUT ($BE),A
site 1BEA   ; OUT ($BF),A
site 1BF4   ; OUT ($BF),A
site 1C07   ; OUT ($BE),A
site 1C19   ; OUT ($BF),A
site 1C23   ; OUT ($BF),A
site 1C42   ; OUT ($BE),A
site 1C48   ; OUT ($BE),A
site 1E48   ; OUT ($7F),A
