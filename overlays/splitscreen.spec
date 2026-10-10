# splitscreen, drafted by tools/mkspec.py from sitescan output.
name splitscreen
cart 1FB17CAA
hz any		; no No-Intro name
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 000B   ; OUT (C),L
site 000D   ; OUT (C),H
site 0019   ; OUT ($BE),A
site 001F   ; OUT ($BE),A
site 00A8   ; OUT ($BF),A
site 00AD   ; OUT ($BF),A
site 00B9   ; OTIR
site 00CB   ; IN A,($BF)
site 00DE   ; IN A,($DC)
site 00E4   ; IN A,($DD)
otir 0122   ; OUTI
otir 0134   ; OUTI
site 013A   ; IN A,($7E)
site 0140   ; IN A,($7E)
site 0146   ; IN A,($7E)
site 0149   ; IN A,($7E)
site 0187   ; OUT ($BE),A
site 018D   ; OUT ($BF),A
site 0191   ; OUT ($BF),A
otir 0197   ; OUTI
site 0271   ; OUT ($BE),A
otir 02AD   ; OUTI
site 02BE   ; OUT ($BF),A
site 02C2   ; OUT ($BF),A
site 02C8   ; OUT ($BF),A
site 02CC   ; OUT ($BF),A
site 02E2   ; OUT ($BF),A
site 02E7   ; OUT ($BF),A
site 02F8   ; OUT ($BF),A
site 02FD   ; OUT ($BF),A
# CHECK mapper at 006F: LD ($FFFC),DE $FFFC,$FFFD
# CHECK mapper at 0076: LD ($FFFE),DE $FFFE,$FFFF
# CHECK cartarea_store at 06A5: LD ($AACC),HL $AACC,$AACD
# CHECK cartarea_store at 8819: LD ($AAAA),HL $AAAA,$AAAB
# CHECK cartarea_store at 8826: LD ($2AAA),HL $2AAA,$2AAB
# CHECK indirect_unresolved at 00F5: CALL $0032 
# CHECK indirect_unresolved at 0693: RET P 
# CHECK indirect_unresolved at 06A9: RET P 
# CHECK bank_unresolved at 063C: JP P,$8800 $8800
# CHECK bank_unresolved at 066B: JP P,$8800 $8800
# CHECK bank_unresolved at 0683: JP P,$8800 $8800
# CHECK low: site 2130  IN D,(C)  (port in C)
