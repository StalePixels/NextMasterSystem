# Pro Wrestling, drafted by tools/mkspec.py from sitescan output.
name Pro Wrestling
cart FBDE42D3
hz any		; No-Intro regions USA, Europe, Brazil
vector 30 io
# priority tiles: the ring posts, ropes and move captions cover the wrestlers (batch 5)
priority
asm 00089 2   ; IM 1 -> IM 2
    im 2
endasm
site 0009A   ; OUT ($7F),A
site 0009E   ; OUT ($7F),A
site 000A2   ; OUT ($7F),A
site 000A6   ; OUT ($7F),A
site 000AA   ; OUT ($DF),A
site 000AE   ; OUT ($DE),A
site 000B0   ; IN A,($DE)
site 000BC   ; OUT ($DE),A
site 000BE   ; IN A,($DE)
site 000CE   ; OUT ($DE),A
site 000E1   ; IN A,($BF)
site 000EA   ; OTIR
site 00141   ; IN A,($BF)
site 00146   ; IN A,($DD)
site 0018F   ; OTIR
site 001A4   ; OTIR
site 001B1   ; OTIR
site 001C5   ; OTIR
site 001D2   ; OTIR
site 0022F   ; OUT ($7F),A
site 00233   ; OUT ($7F),A
site 00237   ; OUT ($7F),A
site 0023B   ; OUT ($7F),A
site 0078E   ; OUT ($BE),A
site 00794   ; OUT ($BE),A
site 02E13   ; OUT ($BE),A
site 02E19   ; OUT ($BE),A
site 03706   ; IN A,($DC)
site 03709   ; IN A,($DD)
site 03717   ; OUT ($DE),A
site 03719   ; IN A,($DC)
site 0371C   ; IN A,($DD)
site 03727   ; OUT ($DE),A
site 03729   ; IN A,($DC)
site 03739   ; OUT ($DE),A
site 0373B   ; IN A,($DC)
site 03745   ; OUT ($DE),A
site 03747   ; IN A,($DC)
site 03751   ; OUT ($DE),A
site 03753   ; IN A,($DD)
site 0375D   ; OUT ($DE),A
site 0375F   ; IN A,($DD)
site 03772   ; IN A,($DC)
site 0377A   ; OUT ($DE),A
site 0377C   ; IN A,($DC)
site 03781   ; OUT ($DE),A
site 03783   ; IN A,($DC)
site 0378D   ; OUT ($DE),A
site 0378F   ; IN A,($DC)
site 03799   ; OUT ($DE),A
site 0379B   ; IN A,($DC)
site 037A5   ; OUT ($DE),A
site 037A7   ; IN A,($DC)
site 037B1   ; OUT ($DE),A
site 037B3   ; IN A,($DC)
site 037DA   ; OUT ($7F),A
site 037DE   ; OUT ($7F),A
site 037E2   ; OUT ($7F),A
site 037E6   ; OUT ($7F),A
site 03810   ; OUT ($BF),A
site 03814   ; OUT ($BF),A
site 03867   ; OUT ($BF),A
site 0386C   ; OUT ($BF),A
site 03875   ; OUT ($BE),A
site 03886   ; OUT ($BE),A
site 03896   ; OUT ($BE),A
site 0389B   ; OUT ($BE),A
site 038AB   ; OUT ($BE),A
site 038B1   ; OUT ($BE),A
site 038C2   ; OUT ($BF),A
site 038C7   ; OUT ($BF),A
site 038CC   ; OUT ($BE),A
site 038F6   ; OUT ($BF),A
site 038F9   ; OUT ($BF),A
site 038FD   ; IN A,($BE)
site 03923   ; OUT ($BE),A
site 0394A   ; OUT ($BF),A
site 0394F   ; OUT ($BF),A
site 03954   ; OUT ($BE),A
site 03996   ; OUT ($BF),A
site 0399B   ; OUT ($BF),A
site 039A0   ; OUT ($BE),A
site 039EF   ; OUT ($BE),A
site 039F5   ; OUT ($BE),A
site 03A0A   ; OUT ($BE),A
site 03A0E   ; IN A,($BE)
site 04053   ; OUT ($BE),A
site 040E4   ; OUT ($BE),A
site 04472   ; OUT ($BF),A
site 04477   ; OUT ($BF),A
site 0448A   ; OUT ($BE),A
site 0448E   ; OUT ($BE),A
site 080B6   ; OUT ($7F),A
site 081D4   ; OUT ($7F),A
site 081F9   ; OUT ($7F),A
site 084DE   ; OUT ($7F),A
site 08540   ; OUT ($7F),A
site 08581   ; OTIR
site 08658   ; OUT ($7F),A
site 08669   ; OUT ($7F),A
site 0866D   ; OUT ($7F),A
site 08671   ; OUT ($7F),A
mapst 00104   ; LD ($FFFF),A
mapst 00112   ; LD ($FFFF),A
mapst 0017B   ; LD ($FFFF),A
mapst 00196   ; LD ($FFFF),A
mapst 001FF   ; LD ($FFFF),A
mapst 004BA   ; LD ($FFFF),A
mapst 00508   ; LD ($FFFF),A
mapst 00525   ; LD ($FFFF),A
mapst 00583   ; LD ($FFFF),A
mapst 0071C   ; LD ($FFFF),A
mapst 0079B   ; LD ($FFFF),A
mapst 031C3   ; LD ($FFFF),A
mapst 031D5   ; LD ($FFFF),A
mapst 031E3   ; LD ($FFFF),A
mapst 0397E   ; LD ($FFFF),A
mapst 03992   ; LD ($FFFF),A
mapst 039AC   ; LD ($FFFF),A
mapst 039BE   ; LD ($FFFF),A
mapst 047D2   ; LD ($FFFF),A
mapst 04838   ; LD ($FFFF),A
mapst 04976   ; LD ($FFFF),A
mapst 0498D   ; LD ($FFFF),A
mapst 05B18   ; LD ($FFFF),A
mapst 05B29   ; LD ($FFFF),A
mapst 05C2D   ; LD ($FFFF),A
mapst 05C3E   ; LD ($FFFF),A
mapst 05C44   ; LD ($FFFF),A
mapst 05C58   ; LD ($FFFF),A
mapst 05C61   ; LD ($FFFF),A
mapst 05C78   ; LD ($FFFF),A
mapst 05F4B   ; LD ($FFFF),A
mapst 05F5C   ; LD ($FFFF),A
mapst 05F7C   ; LD ($FFFF),A
mapst 05FB5   ; LD ($FFFF),A
mapst 063A1   ; LD ($FFFF),A
mapst 0640F   ; LD ($FFFF),A
mapst 064C9   ; LD ($FFFF),A
mapst 064D7   ; LD ($FFFF),A
mapst 06A09   ; LD ($FFFF),A
mapst 06A74   ; LD ($FFFF),A
mapst 06A8D   ; LD ($FFFF),A
mapst 06F09   ; LD ($FFFF),A
mapst 06F3D   ; LD ($FFFF),A
mapst 06FC2   ; LD ($FFFF),A
mapst 06FDF   ; LD ($FFFF),A
# CHECK cartarea_store at 0001B ($001B bank 0): LD ($0F03),A $0F03
# CHECK cartarea_store at 04D08 ($4D08 bank 1): LD (DE),A $11AB
# CHECK cartarea_store at 04D0A ($4D0A bank 1): LD (DE),A $11AB
# CHECK cartarea_store at 04D4C ($4D4C bank 1): LD ($22D6),HL $22D6,$22D7
# CHECK ram_exec at 04CF9 ($4CF9 bank 1): CALL $FB0D $FB0D
# CHECK indirect_unresolved at 0045D ($045D bank 0): JP (HL) 
# CHECK low: site 038E9  OUT (C),D  (port in C)
# CHECK low: site 09169  IN A,($7F)  (h_counter)
# CHECK low: site 1828C  IN A,($BF)  (vdp_status)
# CHECK low: site 1A7BB  IN A,($BD)  (vdp_status)
# CHECK low: site 1A95A  IN A,($BD)  (vdp_status)
# CHECK low: site 1B40E  IN A,($BD)  (vdp_status)
# CHECK low: site 1E2A0  IN A,($BD)  (vdp_status)
# CHECK low: site 1E4F9  IN A,($BD)  (vdp_status)
# Mapper stores the draft missed: LD ($FFFF),A in bank 1, found by sitescan's
# byte scan, after A is loaded with $02 or from $C094.
# "ran in the reference run": the SMS reference MAME saw it write the mapper.
mapst 05BE5   # ran in the reference run
mapst 05C0D   # ran in the reference run
mapst 05C23   # ran in the reference run
