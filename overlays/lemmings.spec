# Lemmings (Europe, Brazil) (En), CRC32 F369B2D8, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log.
# The game writes ROM at $0007 (LD ($0007),A) as a delay between VDP port accesses; the scanner
# reads on past it. On the Next the store writes the cart copy's byte at $0007, which nothing reads.
# Spec gaps (data/scan-verdicts.tsv): unused are the debug monitor $00B0-$02F6 (entered only from
# $1913 in code nothing names), the VRAM address routines $08DC and $08E8, the button waits $0AC7
# and $3ACC, the debug colour setters $1AA5-$1ADC, the routine $1D10 and the sound driver's own
# interrupt entry $B0CF; false are bank 6 $9401 (graphics) and bank 15 $84EF (packed data).
# No priority: the only priority cells are in name table rows 26-27, off the picture.
# Register 0 is always $36, with line interrupts on, but register 10 is only ever $FF (written
# once, at $059F), so on the SMS no line interrupt fires. The handler $069B reads the status at
# $06A4 and drops it, and nothing reads the V counter. With line interrupts on, the runtime takes
# every register 8 write as a split and leaves the copper list's X behind, which shifts the whole
# picture sideways; so the three register 0 writes leave bit 4 clear.
name Lemmings
cart F369B2D8
hz 50		; No-Intro regions Europe, Brazil
# $0008-$000A are zero bytes that no code reaches: the RST $08 vector.
vector 08 io
asm 00497 2   ; IM 1 -> IM 2
    im 2
endasm
asm 004F5 2   ; register 0 $36 -> $26: line interrupts off
    ld a,$26
endasm
asm 0469D 2   ; register 0 $36 -> $26
    ld a,$26
endasm
asm 0475B 2   ; register 0 $36 -> $26
    ld a,$26
endasm
site 0042E   ; OTIR
site 00441   ; OUT ($3E),A
site 00445   ; OUT ($3F),A
site 004B5   ; OUT ($BF),A
site 004BD   ; OUT ($BF),A
site 004C8   ; OUT ($BF),A
site 004D0   ; OUT ($BF),A
site 004E1   ; OUT (C),E
site 004E8   ; OUT (C),D
site 004F0   ; OUT (C),A
site 004F7   ; OUT ($BF),A
site 004FF   ; OUT ($BF),A
site 00509   ; OUT ($BF),A
site 00511   ; OUT ($BF),A
site 0051B   ; OUT ($BF),A
site 00523   ; OUT ($BF),A
site 0052D   ; OUT ($BF),A
site 00535   ; OUT ($BF),A
site 0053F   ; OUT ($BF),A
site 00547   ; OUT ($BF),A
site 00551   ; OUT ($BF),A
site 00559   ; OUT ($BF),A
site 00563   ; OUT ($BF),A
site 0056B   ; OUT ($BF),A
site 00575   ; OUT ($BF),A
site 0057D   ; OUT ($BF),A
site 00587   ; OUT ($BF),A
site 0058F   ; OUT ($BF),A
site 00599   ; OUT ($BF),A
site 005A1   ; OUT ($BF),A
site 005C1   ; OUT ($BF),A
site 005C9   ; OUT ($BF),A
site 005D1   ; OUT ($BE),A
site 005D9   ; OUT ($BF),A
site 005E1   ; OUT ($BF),A
site 005EA   ; OUT ($BE),A
site 00604   ; OUT ($BF),A
site 0060C   ; OUT ($BF),A
site 00615   ; OUT (C),A
site 00621   ; OUT ($BF),A
site 00629   ; OUT ($BF),A
site 00638   ; OUT (C),A
site 0063F   ; OUT (C),A
site 00648   ; OUT ($BF),A
site 00650   ; OUT ($BF),A
site 00660   ; OUT ($BE),A
site 00670   ; OUT ($BE),A
site 0067A   ; OUT ($BF),A
site 00682   ; OUT ($BF),A
site 0068A   ; OUT ($BE),A
site 00691   ; OUT ($BE),A
site 006A4   ; IN A,($BF)
site 006AD   ; IN A,($DD)
site 006F8   ; OUT (C),L
site 006FF   ; OUT (C),H
site 00707   ; OUT (C),A
site 00715   ; OUT (C),L
site 0071C   ; OUT (C),H
site 00725   ; OUT (C),E
site 0072C   ; OUT (C),D
site 00739   ; OUT ($BF),A
site 00741   ; OUT ($BF),A
site 007D8   ; OUT (C),L
site 007DF   ; OUT (C),H
site 007E7   ; OUT (C),E
site 007EE   ; OUT (C),D
site 007F7   ; OUT (C),L
site 007FE   ; OUT (C),H
site 00804   ; OUT (C),E
site 0080B   ; OUT (C),D
site 00846   ; IN A,($DC)
site 0084E   ; IN A,($DC)
site 00856   ; IN A,($DC)
site 0085E   ; IN A,($DC)
site 00866   ; IN A,($DC)
site 0086E   ; IN A,($DC)
site 008B7   ; OUT (C),E
site 008BE   ; OUT (C),D
site 008C5   ; OUTI
site 009F8   ; OUT (C),A
site 009FF   ; OUT (C),A
site 00A0D   ; OUTI
site 00A13   ; OUT (C),A
site 00A1A   ; OUT (C),A
site 00A21   ; OUT (C),A
site 00A3C   ; OUT ($BF),A
site 00A45   ; OUT ($BF),A
site 00A58   ; OUT ($BE),A
site 00B10   ; OUT (C),L
site 00B17   ; OUT (C),H
site 00B64   ; OUT (C),E
site 00B9E   ; OUT (C),L
site 00BA5   ; OUT (C),H
site 00BAD   ; OUT (C),A
site 0141A   ; OUT (C),E
site 01421   ; OUT (C),D
site 01428   ; OUT (C),A
site 0142F   ; OUT (C),A
site 01436   ; OUT (C),L
site 0143D   ; OUT (C),H
site 01444   ; OUT (C),A
site 0144C   ; OUT (C),A
site 01453   ; OUT (C),E
site 0145A   ; OUT (C),D
site 01462   ; OUT (C),A
site 0146A   ; OUT (C),A
site 01471   ; OUT (C),L
site 01478   ; OUT (C),H
site 0147F   ; OUT (C),B
site 01487   ; OUT (C),A
site 014AB   ; OUT (C),E
site 014B2   ; OUT (C),D
site 014BA   ; INI
site 014CB   ; OUT (C),E
site 014D2   ; OUT (C),D
site 01514   ; OUT (C),A
site 0151A   ; OUT (C),A
site 01520   ; OUT (C),A
site 01526   ; OUT (C),A
site 015E6   ; OUT (C),E
site 015ED   ; OUT (C),D
site 015F5   ; INI
site 01606   ; OUT (C),E
site 0160D   ; OUT (C),D
site 01615   ; OUTI
site 01633   ; OUT (C),L
site 0163A   ; OUT (C),H
site 01643   ; INI
site 0164A   ; OUT (C),L
site 01651   ; OUT (C),H
site 01658   ; OUT (C),A
site 0165F   ; OUT (C),A
site 01666   ; OUT (C),A
site 0166D   ; OUT (C),A
site 0198F   ; OUT (C),E
site 01996   ; OUT (C),D
site 0199C   ; OUT ($BE),A
site 019A3   ; OUT ($BE),A
site 019D5   ; OUT (C),E
site 019DC   ; OUT (C),D
site 019E4   ; OUTI
site 019E9   ; OUTI
site 019EF   ; OUTI
site 019F5   ; OUTI
site 01A02   ; OUT (C),E
site 01A09   ; OUT (C),D
site 01A11   ; OUT (C),E
site 01A18   ; OUT (C),D
site 01A75   ; OUT (C),E
site 01A7C   ; OUT (C),D
site 01A84   ; OUT (C),A
site 01BBE   ; OUT (C),E
site 01BC5   ; OUT (C),D
site 01BD0   ; OUT (C),A
site 01BD7   ; OUT (C),A
site 01BDE   ; OUT (C),A
site 01BE6   ; OUT (C),A
site 01BEE   ; OUT (C),E
site 01BF5   ; OUT (C),D
site 01BFC   ; OUT (C),L
site 01C03   ; OUT (C),H
site 01C0A   ; OUT (C),L
site 01C10   ; OUT (C),H
site 01C16   ; OUT (C),E
site 01C1D   ; OUT (C),D
site 01C25   ; OUTI
site 01C2D   ; OUT (C),E
site 01C34   ; OUT (C),D
site 01C3B   ; OUT (C),L
site 01C42   ; OUT (C),H
site 01C49   ; OUT (C),L
site 01C50   ; OUT (C),H
site 01C57   ; OUT (C),L
site 01C5E   ; OUT (C),H
site 01CB0   ; OUT (C),E
site 01CB7   ; OUT (C),D
site 01CBC   ; OUT (C),L
site 01CC3   ; OUT (C),H
site 01CF9   ; OUT (C),E
site 01D00   ; OUT (C),D
site 01D4F   ; OUT (C),E
site 01D56   ; OUT (C),D
site 01D6B   ; OUT (C),E
site 01D73   ; OUT (C),A
site 01D7A   ; OUT (C),A
site 01D82   ; OUT (C),A
site 026F1   ; OUT ($BF),A
site 026F9   ; OUT ($BF),A
site 0270E   ; IN A,(C)
site 02713   ; IN A,(C)
site 02718   ; IN A,(C)
site 0271D   ; IN A,(C)
site 03581   ; OUT (C),E
site 03588   ; OUT (C),D
site 03590   ; OUT (C),A
site 03597   ; OUT (C),E
site 0359E   ; OUT (C),D
site 035A6   ; OUT (C),A
site 035AD   ; OUT (C),B
site 03879   ; OUT ($BF),A
site 03881   ; OUT ($BF),A
site 038AC   ; OUTI
site 038B9   ; OUTI
site 038C4   ; OUTI
site 038D3   ; OUTI
site 03A8B   ; OUT (C),E
site 03A92   ; OUT (C),D
site 03A9A   ; OUTI
site 03AB4   ; OUT (C),E
site 03ABB   ; OUT (C),D
site 03AC4   ; INI
site 03D33   ; OUT (C),L
site 03D3A   ; OUT (C),H
site 03D45   ; OUTI
site 03D4F   ; OUTI
site 0411F   ; IN A,($DC)
site 04128   ; IN A,($DC)
site 04222   ; IN A,($DC)
site 0422E   ; IN A,($DC)
site 04237   ; IN A,($DC)
site 04240   ; IN A,($DC)
site 04389   ; IN A,($DC)
site 0438F   ; IN A,($DC)
site 044CE   ; IN A,($DC)
site 044F3   ; IN A,($DC)
site 045FB   ; OUT (C),E
site 04602   ; OUT (C),D
site 04609   ; OUT (C),A
site 04610   ; OUT (C),A
site 0464F   ; OUT (C),E
site 04656   ; OUT (C),D
site 0465D   ; OUT (C),A
site 04687   ; OUT ($BF),A
site 0468F   ; OUT ($BF),A
site 0469F   ; OUT ($BF),A
site 046A7   ; OUT ($BF),A
site 0475D   ; OUT ($BF),A
site 04765   ; OUT ($BF),A
site 0476F   ; OUT ($BF),A
site 04777   ; OUT ($BF),A
site 047A0   ; OUT (C),E
site 047A7   ; OUT (C),D
site 047AE   ; OUT (C),A
site 0488A   ; IN A,($DC)
site 04891   ; IN A,($DC)
site 048A2   ; IN A,($DC)
site 048A9   ; IN A,($DC)
site 04908   ; OUT (C),L
site 0490F   ; OUT (C),H
site 04917   ; OUT (C),A
site 0491E   ; OUT (C),E
site 04925   ; OUT (C),A
site 0492C   ; OUT (C),E
site 04933   ; OUT (C),A
site 0493B   ; OUT (C),E
site 04943   ; OUT (C),A
site 0494A   ; OUT (C),E
site 04951   ; OUT (C),A
site 04959   ; OUT (C),E
site 0496B   ; OUT (C),E
site 04972   ; OUT (C),D
site 04977   ; OUT (C),A
site 0497E   ; OUT (C),A
site 0498F   ; OUT (C),E
site 04996   ; OUT (C),D
site 049A0   ; OUT (C),A
site 049A8   ; OUT (C),A
site 049B9   ; OUT (C),E
site 049C0   ; OUT (C),D
site 049C8   ; OUT (C),A
site 04A43   ; OUT (C),E
site 04A49   ; OUT (C),D
site 04A53   ; OUT (C),L
site 04A59   ; OUT (C),H
site 04A60   ; OUT (C),L
site 04A66   ; OUT (C),H
site 0760E   ; OUT ($7F),A
site 07612   ; OUT ($7F),A
site 07616   ; OUT ($7F),A
site 07619   ; OUT ($7F),A
site 0761D   ; OUT ($7F),A
site 07620   ; OUT ($7F),A
site 07624   ; OUT ($7F),A
site 07626   ; OUT ($7F),A
site 0762A   ; OUT ($7F),A
site 0762E   ; OUT ($7F),A
site 07632   ; OUT ($7F),A
site 0764D   ; OUT ($7F),A
site 07651   ; OUT ($7F),A
site 07657   ; OUT ($7F),A
site 07660   ; OUT ($7F),A
site 0AE43   ; OUT ($7F),A
site 0AE47   ; OUT ($7F),A
site 0AE54   ; OUT ($7F),A
site 0AE58   ; OUT ($7F),A
site 0AE89   ; OUT ($7F),A
site 0AEA0   ; OUT ($7F),A
site 0AEAD   ; OUT ($7F),A
site 0AEBC   ; OUT ($7F),A
site 0AED3   ; OUT ($7F),A
site 0AEE0   ; OUT ($7F),A
site 0AF06   ; OUT ($7F),A
site 0AF19   ; OUT ($7F),A
site 0AF30   ; OUT ($7F),A
site 0AF36   ; OUT ($7F),A
site 0AF5A   ; OUT ($7F),A
site 0AF71   ; OUT ($7F),A
site 0AF7E   ; OUT ($7F),A
site 0AFDB   ; OUT ($7F),A
site 0B144   ; OUT ($7F),A
site 0B149   ; OUT ($7F),A
site 0B15D   ; OUT ($7F),A
site 0B170   ; OUT ($7F),A
site 0B17C   ; OUT ($7F),A
site 0B18F   ; OUT ($7F),A
mapst 00449   ; LD ($FFFC),A
mapst 0044D   ; LD ($FFFD),A
mapst 00452   ; LD ($FFFE),A
mapst 00457   ; LD ($FFFF),A
mapst 006DE   ; LD ($FFFF),A
mapst 006E5   ; LD ($FFFF),A
mapst 007B6   ; LD ($FFFF),A
mapst 00953   ; LD ($FFFF),A
mapst 0095A   ; LD ($FFFF),A
mapst 00968   ; LD ($FFFF),A
mapst 00974   ; LD ($FFFF),A
mapst 00982   ; LD ($FFFF),A
mapst 0098E   ; LD ($FFFF),A
mapst 00A38   ; LD ($FFFF),A
mapst 00A50   ; LD ($FFFF),A
mapst 00B6C   ; LD ($FFFF),A
mapst 010B0   ; LD ($FFFF),A
mapst 010DC   ; LD ($FFFF),A
mapst 01936   ; LD ($FFFF),A
mapst 01A35   ; LD ($FFFF),A
mapst 01B09   ; LD ($FFFF),A
mapst 01B3A   ; LD ($FFFF),A
mapst 01E43   ; LD ($FFFF),A
mapst 01FD0   ; LD ($FFFF),A
mapst 021E4   ; LD ($FFFF),A
mapst 0223D   ; LD ($FFFF),A
mapst 02530   ; LD ($FFFF),A
mapst 02662   ; LD ($FFFF),A
mapst 0277A   ; LD ($FFFF),A
mapst 02902   ; LD ($FFFF),A
mapst 035EB   ; LD ($FFFF),A
mapst 037CD   ; LD ($FFFF),A
mapst 038F6   ; LD ($FFFF),A
mapst 03C09   ; LD ($FFFF),A
mapst 03C49   ; LD ($FFFF),A
mapst 03C71   ; LD ($FFFF),A
mapst 03C99   ; LD ($FFFF),A
mapst 03F52   ; LD ($FFFF),A
mapst 03FA6   ; LD ($FFFF),A
mapst 04045   ; LD ($FFFF),A
mapst 040D2   ; LD ($FFFF),A
mapst 04174   ; LD ($FFFF),A
mapst 043C3   ; LD ($FFFF),A
mapst 04437   ; LD ($FFFF),A
mapst 04475   ; LD ($FFFF),A
mapst 04699   ; LD ($FFFF),A
mapst 046C9   ; LD ($FFFF),A
mapst 046F4   ; LD ($FFFF),A
mapst 047E0   ; LD ($FFFF),A
mapst 0481E   ; LD ($FFFF),A
mapst 04826   ; LD ($FFFF),A
mapst 0484D   ; LD ($FFFF),A
mapst 04A19   ; LD ($FFFF),A
mapst 04A76   ; LD ($FFFF),A
mapst 07604   ; LD ($FFFF),A
# CHECK cartarea_store at 004E5 ($04E5 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 005BE ($05BE bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 005C3 ($05C3 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 005CD ($05CD bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 005D3 ($05D3 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 005DB ($05DB bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 005E6 ($05E6 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 006FC ($06FC bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00719 ($0719 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 007DC ($07DC bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 007E3 ($07E3 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 007EB ($07EB bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 007FB ($07FB bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00808 ($0808 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 008BB ($08BB bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 009FC ($09FC bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00B14 ($0B14 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00BA2 ($0BA2 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0141C ($141C bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01423 ($1423 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0142C ($142C bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01438 ($1438 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0143F ($143F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01448 ($1448 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01455 ($1455 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01467 ($1467 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01473 ($1473 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0147A ($147A bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01483 ($1483 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 014AD ($14AD bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 014CD ($14CD bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 015EA ($15EA bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0160A ($160A bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01635 ($1635 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0164E ($164E bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01991 ($1991 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 019D9 ($19D9 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 019EB ($19EB bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 019F1 ($19F1 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01A06 ($1A06 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01A15 ($1A15 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01A79 ($1A79 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01BC0 ($1BC0 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01BD2 ($1BD2 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01BF2 ($1BF2 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01BF8 ($1BF8 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C00 ($1C00 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C06 ($1C06 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C0D ($1C0D bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C1A ($1C1A bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C20 ($1C20 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C31 ($1C31 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C38 ($1C38 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C3F ($1C3F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C45 ($1C45 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C4D ($1C4D bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C54 ($1C54 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01C5B ($1C5B bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01CB2 ($1CB2 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01CC0 ($1CC0 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01CFD ($1CFD bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01D53 ($1D53 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01D6F ($1D6F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01D7E ($1D7E bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 026FB ($26FB bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 02BE8 ($2BE8 bank 0): FD 36 0A 01  LD (IY+$0A),$01 $000A
# CHECK cartarea_store at 02BFE ($2BFE bank 0): FD 77 01  LD (IY+$01),A $0001
# CHECK cartarea_store at 03585 ($3585 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0359B ($359B bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 035AA ($35AA bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03A8D ($3A8D bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03A95 ($3A95 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03AB6 ($3AB6 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03D35 ($3D35 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03D3D ($3D3D bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 03D4A ($3D4A bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 045FD ($45FD bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04604 ($4604 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0460B ($460B bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04651 ($4651 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0465A ($465A bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 047A4 ($47A4 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 047AA ($47AA bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0490C ($490C bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04912 ($4912 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0491A ($491A bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04922 ($4922 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04928 ($4928 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04930 ($4930 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04937 ($4937 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04946 ($4946 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0494E ($494E bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04955 ($4955 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0496F ($496F bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04979 ($4979 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04993 ($4993 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 049BD ($49BD bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 049C2 ($49C2 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04A4C ($4A4C bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 04A5D ($4A5D bank 1): 32 07 00  LD ($0007),A $0007
# Mapper stores found by the byte scan in bytes no path reached:
mapst 000E7   # LD ($FFFC),A; JP/CALL target from $20533 $21773 $219B3 $21C53; 32 bytes of valid code before it
# CHECK byte scan medium: mapst 0010C  LD ($FFFC),A  (32 bytes of valid code before it)
# CHECK byte scan medium: mapst 00246  LD ($FFFC),A  (32 bytes of valid code before it)
# CHECK byte scan medium: mapst 00289  LD ($FFFC),A  (32 bytes of valid code before it)
# CHECK byte scan medium: mapst 00296  LD ($FFFC),A  (32 bytes of valid code before it)
# CHECK byte scan medium: mapst 002D4  LD ($FFFC),A  (32 bytes of valid code before it)
# CHECK byte scan low: mapst 199EF  LD ($FFFF),A  (no valid code after it)
# CHECK byte scan low: mapst 20281  LD ($FFFF),A  (32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 00199  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 001FD  IN A,($BE)  (vdp_data; branch target from $3D7B2 $3D7C6 $00205; 32 bytes of valid code before it)
# CHECK high: site 002EC  OUT ($BF),A  (vdp_control; branch target from $2EC6A; 32 bytes of valid code before it)
# CHECK low: site 002F4  OUT ($BF),A  (vdp_control; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 002F8  OUT ($BF),A  (vdp_control; branch target from $3D611 $3D668 $00192; 32 bytes of valid code before it)
# CHECK medium: site 008DD  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 008E5  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 008E9  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 008EF  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 00AC7  IN A,($DC)  (joypad_a; branch target from $00ACB; 32 bytes of valid code before it)
# CHECK high: site 00ACE  IN A,($DC)  (joypad_a; branch target from $00AD2; 32 bytes of valid code before it)
# CHECK high: site 00AD5  IN A,($DC)  (joypad_a; branch target from $00AD9; 32 bytes of valid code before it)
# CHECK low: site 01843  INDR  (port in C; 12 RST or NOP opcodes around it (looks like data); 21 bytes of valid code before it)
# CHECK low: site 01895  IN A,($BD)  (vdp_status; 17 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 01ABA  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 01AC4  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 01ACD  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 01AD6  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 01D16  OUT (C),E  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 01D1D  OUT (C),D  (port in C; 32 bytes of valid code before it)
# CHECK low: site 01D87  OUT (C),E  (port in C; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 01D8E  OUT (C),D  (port in C; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 01D95  OUT (C),L  (port in C; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 01D9C  OUT (C),H  (port in C; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 01DA4  OUT (C),L  (port in C; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 01DAB  OUT (C),H  (port in C; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 03ACC  IN A,($DC)  (joypad_a; branch target from $03AF5 $03B14; 32 bytes of valid code before it)
# CHECK low: site 0AFEC  OUT ($C0),A  (no_effect; no evidence)
# CHECK medium: site 0B0D0  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK medium: site 0B0D2  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK medium: site 19401  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK low: site 19713  OUT ($7F),A  (psg; 19 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2CFF0  IN A,($C0)  (joypad_a; no evidence)
# CHECK low: site 2E870  IND  (port in C; no evidence)
# CHECK low: site 333E9  OUT (C),B  (port in C; 12 bytes of valid code before it; no valid code after it)
# CHECK low: site 359FE  IN A,($BF)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 36290  IN A,($F0)  (joypad_a; no evidence)
# CHECK low: site 36AD6  IN A,($DD)  (joypad_b_misc; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 36F3F  IN A,($F1)  (joypad_b_misc; no valid code after it)
# CHECK low: site 38B7A  OUT ($F1),A  (fm_data; no evidence)
# CHECK low: site 3A5F5  IN A,($7F)  (h_counter; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 3C4EF  OUT ($DD),A  (no_effect; 8 bytes of valid code before it)
# CHECK low: site 3D170  OUT ($F2),A  (fm_control; no evidence)
# CHECK low: site 3DB5B  IN A,($F1)  (joypad_b_misc; no evidence)
# CHECK low: site 3EAF8  IN A,($BF)  (vdp_status; 24 bytes of valid code before it; no valid code after it)
# Menu text ticker ($1A6A, called every frame from the frame handler through $1A2F): it rotates
# one 8-pixel column of 42 tiles and writes byte 3 of each of their 168 rows, $3563-$3800 in
# steps of 4, with a VRAM address write before each byte: 504 traps, about 450,000 cycles a
# frame, so the frame handler missed frames and the menu took no input. Page entry tick writes
# the same bytes with one jt_vwrite call (168 runs of 1 byte, source step 1, VRAM step 4).
asm 01A6A 6          ; LD DE,$7563 : LD HL,$CE00
    rst $08
    db far_io, pg_tick, ent_tick
    ei
    ret
endasm
# Play area blit ($09ED, every game step, 4 frames on the Master System): 19 rows of 32 name
# table cells from the level map ($DAEC, rows 112 bytes apart) and the lemming layer at $D800,
# 1,216 data writes through single traps and copied traces: about 1.2 Next frames, so a step took
# 5 frames against 4. Page entry blit builds the 1,216 bytes in its page and writes them with one
# jt_vwrite call (19 runs of 64 bytes).
asm 009ED 7          ; DI : LD HL,($DAEC) : LD DE,$D800
    rst $08
    db far_io, pg_blit, ent_blit
    ei
    ret
endasm
# Delay $0ADD (B units of a 3,000-pass DEC BC loop, about 20.5 ms each on the Master System, measured
# 80 units in 98.3 frames of the 60 Hz reference): a busy loop, so at 28 MHz it ran about 8 times too
# fast, and the title, the logo after the SEGA scroll and the waits on the level screens were cut short
# (the title showed for under a second). Page entry delay waits the same real time by counting the
# Next's raster lines, 315 lines (65 us each) a unit, with the game's interrupts as they were.
asm 00ADD 5          ; PUSH BC : LD BC,$0BB8 : DEC BC
    rst $08
    db far_io, pg_delay, ent_delay
    ret
endasm
page 0 tick blit delay
; tick: as the game's $1A6A-$1A8B. Writes the 168 bytes from $CE00 to VRAM $3563, $3567, ...
; Returns as the game's loop does: B = 0, C = $BF, DE = $7803, HL = $CEA8, A = the last byte.
; Interrupts stay off; the cave turns them on, as the game's EI does.
tick:   di
        push ix
        push iy
        ld hl,$CE00
        ld de,$3563
        ld bc,$01A8             ; 168 runs of 1 byte
        ld ix,1
        ld iy,4
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop iy
        pop ix
        ld bc,$00BF
        ld de,$7803
        ld hl,$CEA8
        ld a,($CEA7)
        ret
; blit: as the game's $09ED-$0A30. A cell is the map byte and high byte 0 when the $D800 byte is
; 0, else the $D800 byte and high byte 1. Returns as the game's code does: HL = map + 19 * 112,
; DE = $D800 + 608, BC = $00BE, B' = 0, A = the last byte written. Interrupts stay off.
blit:   di
        push ix
        push iy
        ld hl,($DAEC)
        ld de,$D800
        ld ix,bbuf
        ld c,19
.row:   ld b,32
.cell:  ld a,(de)
        and a
        jr nz,.lem
        ld a,h                  ; the map is in RAM; a map address under $4000 reads through jt_peek
        cp $40
        jr c,.peek
        ld a,(hl)
.put:   ld (ix+0),a
        ld (ix+1),0
        jr .next
.peek:  call jt_peek
        jr .put
.lem:   ld (ix+0),a
        ld (ix+1),1
.next:  inc hl
        inc de
        inc ix
        inc ix
        djnz .cell
        push bc
        ld bc,$0050
        add hl,bc
        pop bc
        dec c
        jr nz,.row
        push hl
        push de
        ld hl,bbuf
        ld de,$3800
        ld bc,$4013             ; 19 runs of 64 bytes
        ld ix,64
        ld iy,64
        ld a,1                  ; the source is this page
        call jt_vwrite
        pop de
        pop hl
        pop iy
        pop ix
        exx
        ld b,0
        exx
        ld bc,$00BE
        ld a,(bbuf+1215)
        ret
bbuf:   ds 1216
; delay: as the game's $0ADD-$0AEA, in real time. B units (0 means 256) of 315 raster lines. Returns
; as the game's loop does: A = 0 with Z set, B = 0; C, DE and HL kept. The interrupt state stays as it
; was; each line read runs with interrupts off, so a handler cannot change the NextReg select port
; between the select and the read.
delay:  push hl
        push de
        ld a,b
        ld (dunits),a
        ld a,i                  ; P/V: interrupts on at entry
        ld a,0
        jp po,.di
        inc a
.di:    ld (dirq),a
        di
        push bc
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        pop bc
        ld hl,311               ; lines in a 50 Hz frame
        bit 2,a
        jr z,.hz
        ld hl,264               ; 60 Hz
.hz:    ld (dlen),hl
        call dline
        ld (dprev),hl
        ld hl,315
        ld (dleft),hl
.poll:  call dline              ; HL = this line
        ld de,(dprev)
        ld (dprev),hl
        or a
        sbc hl,de               ; lines since the last read
        jr nc,.pos
        ld de,(dlen)
        add hl,de               ; the frame wrapped
.pos:   ex de,hl
        ld hl,(dleft)
        or a
        sbc hl,de
.chk:   ld (dleft),hl
        bit 7,h
        jr nz,.unit
        ld a,h
        or l
        jr nz,.poll
.unit:  ld a,(dunits)           ; a unit is over
        dec a
        ld (dunits),a
        jr z,.end
        ld de,315
        add hl,de
        jr .chk
.end:   pop de
        pop hl
        ld b,0
        xor a
        ret
; HL = the Next's raster line (0-310). Interrupts off for the read, then as at the entry. The high
; bit is read again after the low byte, and the read repeats when it changed (line 255 to 256).
dline:  di
        push bc
        ld bc,$243B
.again: ld a,$1E
        out (c),a
        inc b
        in h,(c)
        dec b
        ld a,$1F
        out (c),a
        inc b
        in l,(c)
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        dec b
        xor h
        and 1
        jr nz,.again
        pop bc
        ld a,h
        and 1
        ld h,a
        ld a,(dirq)
        or a
        ret z
        ei
        ret
dunits: db 0
dirq:   db 0
dlen:   dw 0
dprev:  dw 0
dleft:  dw 0
endpage

# Lemmings (Europe, Brazil).cht, "Infinite Climber"
# Lemmings (Europe, Brazil).cht, "Infinite Floater"
# Lemmings (Europe, Brazil).cht, "Infinite Bomber"
# Lemmings (Europe, Brazil).cht, "Infinite Blocker"
# Lemmings (Europe, Brazil).cht, "Infinite Builder"
# Lemmings (Europe, Brazil).cht, "Infinite Basher"
# Lemmings (Europe, Brazil).cht, "Infinite Miner"
# Lemmings (Europe, Brazil).cht, "Infinite Digger"
poke "Infinite skills"
ar 00DB-720A
ar 00DB-730A
ar 00DB-740A
ar 00DB-750A
ar 00DB-760A
ar 00DB-770A
ar 00DB-780A
ar 00DB-790A
endpoke

# Lemmings (Europe, Brazil).cht, "Infinite Time - One's Digit"
# Lemmings (Europe, Brazil).cht, "Infinite Time - Ten's Digit"
# Lemmings (Europe, Brazil).cht, "Infinite Time - Minutes' Digit"
poke "Infinite time"
ar 00DA-D309
ar 00DA-D209
ar 00DA-D109
endpoke

# Lemmings (Europe) (Action Replay).cht, "Level Select"
poke "Level select"
ar 00DB-9D??
endpoke
