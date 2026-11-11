# Buggy Run (Europe, Brazil) (En), CRC32 B0FC4577, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - The scan that drafted the sites had two sets of entry points more than the scanner finds:
#   the game state table at $0CAB (3 bytes a state: bank for slot 2, then the handler address;
#   states 0-19, called at $009F), and the JP table of service routines at $0200-$0271.
#   The table's last entry, $0272 JP $8CEB, is left out: nothing calls $0272 and the bank in
#   slot 2 is not known there. Reference logs of the title, the demo races and a free-run race
#   ran no I/O or mapper site that the spec does not have.
# - The io vector is at $00. The game's code has no RST $00, and no call or jump to $0000
#   (the reset button path at $0A83 jumps to $0077).
# - The routines at $0059 (one CRAM write), $057E (a second sprite table copy, the twin of
#   $0347) and $3BFB (clears the scroll registers) are named by no call, jump, address load
#   or table word, and no recording ran them: their I/O sites are not patched (verdict unused).
#   The jump at $1DFA enters $0059's code at $0060, and the spec patches $0060 and $0063.
# - The byte scan rows in banks 15, 26, 29, 30 and 31 are in data (verdict false).
# - $60F0 (bank 1) is LD (HL),$1D with HL = $ADDA (loaded at $60B8): a write into the cart
#   area of slot 2, a no-op on a Master System. On the Next it would change the cart image in
#   RAM, so its two bytes become NOPs.
# - The main loop sets $C610 at $00E4 and waits; the frame handler does the frame's VDP work
#   only when $C610 is set. In a race the loop sets it once a frame on the reference and on
#   the Next.
name Buggy Run
cart B0FC4577
hz 50
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0001A   ; OUT (C),L
site 0001C   ; OUT (C),H
site 00060   ; OUT ($BF),A
site 00063   ; OUT ($BE),A
site 0029A   ; IN A,($BF)
site 002A7   ; OUT ($BF),A
site 002AB   ; OUT ($BF),A
site 002C8   ; OUT ($BF),A
site 002CC   ; OUT ($BF),A
site 002CF   ; IN A,($DC)
site 002EC   ; IN A,($DD)
site 00314   ; IN A,($BF)
site 0031F   ; OUTI
site 00321   ; OUT (C),A
site 0032D   ; OUT ($BE),A
site 00355   ; OUT (C),L
site 00357   ; OUT (C),H
site 0035D   ; OUTD
site 0035F   ; OUTD
site 00361   ; OUTD
site 00363   ; OUTD
site 00365   ; OUTD
site 00367   ; OUTD
site 00369   ; OUTD
site 0036B   ; OUTD
site 0036D   ; OUTD
site 0036F   ; OUTD
site 00371   ; OUTD
site 00373   ; OUTD
site 00375   ; OUTD
site 00377   ; OUTD
site 00379   ; OUTD
site 0037B   ; OUTD
site 0037D   ; OUTD
site 0037F   ; OUTD
site 00381   ; OUTD
site 00383   ; OUTD
site 00385   ; OUTD
site 00387   ; OUTD
site 00389   ; OUTD
site 0038B   ; OUTD
site 0038D   ; OUTD
site 0038F   ; OUTD
site 00391   ; OUTD
site 00393   ; OUTD
site 00395   ; OUTD
site 00397   ; OUTD
site 00399   ; OUTD
site 0039B   ; OUTD
site 0039D   ; OUTD
site 0039F   ; OUTD
site 003A1   ; OUTD
site 003A3   ; OUTD
site 003A5   ; OUTD
site 003A7   ; OUTD
site 003A9   ; OUTD
site 003AB   ; OUTD
site 003AD   ; OUTD
site 003AF   ; OUTD
site 003B1   ; OUTD
site 003B3   ; OUTD
site 003B5   ; OUTD
site 003B7   ; OUTD
site 003B9   ; OUTD
site 003BB   ; OUTD
site 003BD   ; OUTD
site 003BF   ; OUTD
site 003C1   ; OUTD
site 003C3   ; OUTD
site 003C5   ; OUTD
site 003C7   ; OUTD
site 003C9   ; OUTD
site 003CB   ; OUTD
site 003CD   ; OUTD
site 003CF   ; OUTD
site 003D1   ; OUTD
site 003D3   ; OUTD
site 003D5   ; OUTD
site 003D7   ; OUTD
site 003D9   ; OUTD
site 003DB   ; OUTD
site 003E2   ; OUT (C),E
site 003E4   ; OUT (C),D
site 003E9   ; OUTI
site 003EB   ; OUTD
site 003EF   ; OUTI
site 003F1   ; OUTD
site 003F5   ; OUTI
site 003F7   ; OUTD
site 003FB   ; OUTI
site 003FD   ; OUTD
site 00401   ; OUTI
site 00403   ; OUTD
site 00407   ; OUTI
site 00409   ; OUTD
site 0040D   ; OUTI
site 0040F   ; OUTD
site 00413   ; OUTI
site 00415   ; OUTD
site 00419   ; OUTI
site 0041B   ; OUTD
site 0041F   ; OUTI
site 00421   ; OUTD
site 00425   ; OUTI
site 00427   ; OUTD
site 0042B   ; OUTI
site 0042D   ; OUTD
site 00431   ; OUTI
site 00433   ; OUTD
site 00437   ; OUTI
site 00439   ; OUTD
site 0043D   ; OUTI
site 0043F   ; OUTD
site 00443   ; OUTI
site 00445   ; OUTD
site 00449   ; OUTI
site 0044B   ; OUTD
site 0044F   ; OUTI
site 00451   ; OUTD
site 00455   ; OUTI
site 00457   ; OUTD
site 0045B   ; OUTI
site 0045D   ; OUTD
site 00461   ; OUTI
site 00463   ; OUTD
site 00467   ; OUTI
site 00469   ; OUTD
site 0046D   ; OUTI
site 0046F   ; OUTD
site 00473   ; OUTI
site 00475   ; OUTD
site 00479   ; OUTI
site 0047B   ; OUTD
site 0047F   ; OUTI
site 00481   ; OUTD
site 00485   ; OUTI
site 00487   ; OUTD
site 0048B   ; OUTI
site 0048D   ; OUTD
site 00491   ; OUTI
site 00493   ; OUTD
site 00497   ; OUTI
site 00499   ; OUTD
site 0049D   ; OUTI
site 0049F   ; OUTD
site 004A3   ; OUTI
site 004A5   ; OUTD
site 004A9   ; OUTI
site 004AB   ; OUTD
site 004AF   ; OUTI
site 004B1   ; OUTD
site 004B5   ; OUTI
site 004B7   ; OUTD
site 004BB   ; OUTI
site 004BD   ; OUTD
site 004C1   ; OUTI
site 004C3   ; OUTD
site 004C7   ; OUTI
site 004C9   ; OUTD
site 004CD   ; OUTI
site 004CF   ; OUTD
site 004D3   ; OUTI
site 004D5   ; OUTD
site 004D9   ; OUTI
site 004DB   ; OUTD
site 004DF   ; OUTI
site 004E1   ; OUTD
site 004E5   ; OUTI
site 004E7   ; OUTD
site 004EB   ; OUTI
site 004ED   ; OUTD
site 004F1   ; OUTI
site 004F3   ; OUTD
site 004F7   ; OUTI
site 004F9   ; OUTD
site 004FD   ; OUTI
site 004FF   ; OUTD
site 00503   ; OUTI
site 00505   ; OUTD
site 00509   ; OUTI
site 0050B   ; OUTD
site 0050F   ; OUTI
site 00511   ; OUTD
site 00515   ; OUTI
site 00517   ; OUTD
site 0051B   ; OUTI
site 0051D   ; OUTD
site 00521   ; OUTI
site 00523   ; OUTD
site 00527   ; OUTI
site 00529   ; OUTD
site 0052D   ; OUTI
site 0052F   ; OUTD
site 00533   ; OUTI
site 00535   ; OUTD
site 00539   ; OUTI
site 0053B   ; OUTD
site 0053F   ; OUTI
site 00541   ; OUTD
site 00545   ; OUTI
site 00547   ; OUTD
site 0054B   ; OUTI
site 0054D   ; OUTD
site 00551   ; OUTI
site 00553   ; OUTD
site 00557   ; OUTI
site 00559   ; OUTD
site 0055D   ; OUTI
site 0055F   ; OUTD
site 00563   ; OUTI
site 00565   ; OUTD
site 006B2   ; OUTI
site 006B4   ; OUTI
site 006B6   ; OUTI
site 006B8   ; OUTI
site 006BA   ; OUTI
site 006BC   ; OUTI
site 006BE   ; OUTI
site 006C0   ; OUTI
site 006C2   ; OUTI
site 006C4   ; OUTI
site 006C6   ; OUTI
site 006C8   ; OUTI
site 006CA   ; OUTI
site 006CC   ; OUTI
site 006CE   ; OUTI
site 006D0   ; OUTI
site 006D2   ; OUTI
site 006D4   ; OUTI
site 006D6   ; OUTI
site 006D8   ; OUTI
site 006DA   ; OUTI
site 006DC   ; OUTI
site 006DE   ; OUTI
site 006E0   ; OUTI
site 006E2   ; OUTI
site 006E4   ; OUTI
site 006E6   ; OUTI
site 006E8   ; OUTI
site 006EA   ; OUTI
site 006EC   ; OUTI
site 006EE   ; OUTI
site 006F0   ; OUTI
site 006F2   ; OUTI
site 006F4   ; OUTI
site 006F6   ; OUTI
site 006F8   ; OUTI
site 006FA   ; OUTI
site 006FC   ; OUTI
site 006FE   ; OUTI
site 00700   ; OUTI
site 00702   ; OUTI
site 00704   ; OUTI
site 00706   ; OUTI
site 00708   ; OUTI
site 0070A   ; OUTI
site 0070C   ; OUTI
site 0070E   ; OUTI
site 00710   ; OUTI
site 00712   ; OUTI
site 00714   ; OUTI
site 00716   ; OUTI
site 00718   ; OUTI
site 0071A   ; OUTI
site 0071C   ; OUTI
site 0071E   ; OUTI
site 00720   ; OUTI
site 00722   ; OUTI
site 00724   ; OUTI
site 00726   ; OUTI
site 00728   ; OUTI
site 0072A   ; OUTI
site 0072C   ; OUTI
site 0072E   ; OUTI
site 00730   ; OUTI
site 00732   ; OUTI
site 00734   ; OUTI
site 00736   ; OUTI
site 00738   ; OUTI
site 0073A   ; OUTI
site 0073C   ; OUTI
site 0073E   ; OUTI
site 00740   ; OUTI
site 00742   ; OUTI
site 00744   ; OUTI
site 00746   ; OUTI
site 00748   ; OUTI
site 0074A   ; OUTI
site 0074C   ; OUTI
site 0074E   ; OUTI
site 00750   ; OUTI
site 00752   ; OUTI
site 00754   ; OUTI
site 00756   ; OUTI
site 00758   ; OUTI
site 0075A   ; OUTI
site 0075C   ; OUTI
site 0075E   ; OUTI
site 00760   ; OUTI
site 00762   ; OUTI
site 00764   ; OUTI
site 00766   ; OUTI
site 00768   ; OUTI
site 0076A   ; OUTI
site 0076C   ; OUTI
site 0076E   ; OUTI
site 00770   ; OUTI
site 00772   ; OUTI
site 00774   ; OUTI
site 00776   ; OUTI
site 00778   ; OUTI
site 0077A   ; OUTI
site 0077C   ; OUTI
site 0077E   ; OUTI
site 00780   ; OUTI
site 00782   ; OUTI
site 00784   ; OUTI
site 00786   ; OUTI
site 00788   ; OUTI
site 0078A   ; OUTI
site 0078C   ; OUTI
site 0078E   ; OUTI
site 00790   ; OUTI
site 00792   ; OUTI
site 00794   ; OUTI
site 00796   ; OUTI
site 00798   ; OUTI
site 0079A   ; OUTI
site 0079C   ; OUTI
site 0079E   ; OUTI
site 007A0   ; OUTI
site 007A2   ; OUTI
site 007A4   ; OUTI
site 007A6   ; OUTI
site 007A8   ; OUTI
site 007AA   ; OUTI
site 007AC   ; OUTI
site 007AE   ; OUTI
site 007B0   ; OUTI
site 007B9   ; OTIR
site 007CB   ; OUT ($BE),A
site 007D1   ; OUT ($BE),A
site 007E3   ; OUTI
site 007E5   ; OUT ($BE),A
site 007FC   ; OUTI
site 00801   ; OUT ($BE),A
site 00813   ; OUT (C),E
site 00815   ; OUT (C),D
site 00828   ; OUT (C),E
site 0082E   ; OUT (C),D
site 0086C   ; OUT ($BE),A
site 00871   ; OUT ($BE),A
site 00876   ; OUT ($BE),A
site 0087B   ; OUT ($BE),A
site 00880   ; OUT ($BE),A
site 00885   ; OUT ($BE),A
site 0088A   ; OUT ($BE),A
site 0088F   ; OUT ($BE),A
site 00894   ; OUT ($BE),A
site 00899   ; OUT ($BE),A
site 0089E   ; OUT ($BE),A
site 008A3   ; OUT ($BE),A
site 008A8   ; OUT ($BE),A
site 008AD   ; OUT ($BE),A
site 008B2   ; OUT ($BE),A
site 008B7   ; OUT ($BE),A
site 008BC   ; OUT ($BE),A
site 008C1   ; OUT ($BE),A
site 008C6   ; OUT ($BE),A
site 008CB   ; OUT ($BE),A
site 008D0   ; OUT ($BE),A
site 008D5   ; OUT ($BE),A
site 008DA   ; OUT ($BE),A
site 008DF   ; OUT ($BE),A
site 008E4   ; OUT ($BE),A
site 008E9   ; OUT ($BE),A
site 008EE   ; OUT ($BE),A
site 008F3   ; OUT ($BE),A
site 008F8   ; OUT ($BE),A
site 008FD   ; OUT ($BE),A
site 00902   ; OUT ($BE),A
site 00907   ; OUT ($BE),A
site 00927   ; OUT (C),A
site 00954   ; OUT ($BE),A
site 00A8A   ; IN A,($BF)
site 00A8C   ; IN A,($DD)
site 00E54   ; OUT ($3F),A
site 00E56   ; IN A,($DD)
site 00E60   ; OUT ($3F),A
site 00E62   ; IN A,($DD)
site 00ED8   ; OUT ($3E),A
site 00EDB   ; OUT ($F2),A
site 00EE3   ; OUT ($3E),A
site 00EE7   ; OUT ($3F),A
site 00EED   ; IN A,($BF)
site 00EEF   ; IN A,($BF)
site 00EFB   ; IN A,($BF)
site 01A3A   ; OUT ($BF),A
site 01A3D   ; OUT ($BF),A
site 01A44   ; OUT ($BE),A
site 01A4B   ; OUT ($BE),A
site 01A52   ; OUT ($BE),A
site 01A59   ; OUT ($BE),A
site 01A60   ; OUT ($BE),A
site 01A67   ; OUT ($BE),A
site 01A6E   ; OUT ($BE),A
site 01A75   ; OUT ($BE),A
site 01A95   ; OUT ($BF),A
site 01A98   ; OUT ($BF),A
site 01A9D   ; OUT ($BE),A
site 01AA4   ; OUT ($BE),A
site 01AAC   ; OUT ($BE),A
site 01AB3   ; OUT ($BE),A
site 01ACA   ; OUT ($BF),A
site 01ACD   ; OUT ($BF),A
site 01ADE   ; OUT ($BE),A
site 01AE5   ; OUT ($BE),A
site 01AF2   ; OUT ($BE),A
site 01AF9   ; OUT ($BE),A
site 01B00   ; OUT ($BF),A
site 01B03   ; OUT ($BF),A
site 01B10   ; OUT ($BE),A
site 01B17   ; OUT ($BE),A
site 02953   ; OUT ($BF),A
site 02956   ; OUT ($BF),A
site 02963   ; OUT ($BE),A
site 0296A   ; OUT ($BE),A
site 02972   ; OUT ($BE),A
site 02979   ; OUT ($BE),A
site 0299B   ; OUT ($BF),A
site 0299E   ; OUT ($BF),A
site 029B0   ; OUT ($BE),A
site 029B7   ; OUT ($BE),A
site 02A44   ; OUT (C),L
site 02A46   ; OUT (C),H
site 02A5D   ; OUT (C),L
site 02A5F   ; OUT (C),H
site 02A7A   ; OUTI
site 02A7C   ; OUTI
site 02A7E   ; OUTI
site 02A81   ; OUT ($BE),A
site 03C43   ; OUT ($BF),A
site 03C47   ; OUT ($BF),A
site 03C4C   ; OUT ($BF),A
site 03C50   ; OUT ($BF),A
site 06720   ; OUT (C),A
site 06724   ; OUT (C),A
site 06727   ; OUT (C),A
site 0672B   ; OUT (C),A
site 06733   ; OUT (C),A
site 06737   ; OUT (C),A
site 0673A   ; OUT (C),A
site 0673D   ; OUT (C),A
site 0700F   ; OUT ($BE),A
site 07012   ; OUT ($BE),A
site 0701E   ; OUT ($BE),A
site 07021   ; OUT ($BE),A
site 0702D   ; OUT ($BE),A
site 07030   ; OUT ($BE),A
site 0703C   ; OUT ($BE),A
site 0703F   ; OUT ($BE),A
site 0704B   ; OUT ($BE),A
site 0704E   ; OUT ($BE),A
site 0705A   ; OUT ($BE),A
site 0705D   ; OUT ($BE),A
site 07069   ; OUT ($BE),A
site 0706C   ; OUT ($BE),A
site 07078   ; OUT ($BE),A
site 0707B   ; OUT ($BE),A
site 07087   ; OUT ($BE),A
site 0708A   ; OUT ($BE),A
site 07096   ; OUT ($BE),A
site 07099   ; OUT ($BE),A
site 070A5   ; OUT ($BE),A
site 070A8   ; OUT ($BE),A
site 070B4   ; OUT ($BE),A
site 070B7   ; OUT ($BE),A
site 070C3   ; OUT ($BE),A
site 070C6   ; OUT ($BE),A
site 070D2   ; OUT ($BE),A
site 070D5   ; OUT ($BE),A
site 070E1   ; OUT ($BE),A
site 070E4   ; OUT ($BE),A
site 070F0   ; OUT ($BE),A
site 070F3   ; OUT ($BE),A
site 070FF   ; OUT ($BE),A
site 07102   ; OUT ($BE),A
site 0710E   ; OUT ($BE),A
site 07111   ; OUT ($BE),A
site 0711D   ; OUT ($BE),A
site 07120   ; OUT ($BE),A
site 0712C   ; OUT ($BE),A
site 0712F   ; OUT ($BE),A
site 0713B   ; OUT ($BE),A
site 0713E   ; OUT ($BE),A
site 0714A   ; OUT ($BE),A
site 0714D   ; OUT ($BE),A
site 07159   ; OUT ($BE),A
site 0715C   ; OUT ($BE),A
site 07168   ; OUT ($BE),A
site 0716B   ; OUT ($BE),A
site 07177   ; OUT ($BE),A
site 0717A   ; OUT ($BE),A
site 07186   ; OUT ($BE),A
site 07189   ; OUT ($BE),A
site 07195   ; OUT ($BE),A
site 07198   ; OUT ($BE),A
site 071A4   ; OUT ($BE),A
site 071A7   ; OUT ($BE),A
site 071B3   ; OUT ($BE),A
site 071B6   ; OUT ($BE),A
site 071C2   ; OUT ($BE),A
site 071C5   ; OUT ($BE),A
site 071D1   ; OUT ($BE),A
site 071D4   ; OUT ($BE),A
site 071E0   ; OUT ($BE),A
site 071E3   ; OUT ($BE),A
site 071FA   ; OUT ($BF),A
site 071FD   ; OUT ($BF),A
site 07200   ; OUT ($BE),A
site 07203   ; OUT ($BE),A
site 07210   ; OUT ($BF),A
site 07213   ; OUT ($BF),A
site 07216   ; OUT ($BE),A
site 07219   ; OUT ($BE),A
site 07226   ; OUT ($BF),A
site 07229   ; OUT ($BF),A
site 0722C   ; OUT ($BE),A
site 0722F   ; OUT ($BE),A
site 0723C   ; OUT ($BF),A
site 0723F   ; OUT ($BF),A
site 07242   ; OUT ($BE),A
site 07245   ; OUT ($BE),A
site 07252   ; OUT ($BF),A
site 07255   ; OUT ($BF),A
site 07258   ; OUT ($BE),A
site 0725B   ; OUT ($BE),A
site 07268   ; OUT ($BF),A
site 0726B   ; OUT ($BF),A
site 0726E   ; OUT ($BE),A
site 07271   ; OUT ($BE),A
site 0727E   ; OUT ($BF),A
site 07281   ; OUT ($BF),A
site 07284   ; OUT ($BE),A
site 07287   ; OUT ($BE),A
site 07294   ; OUT ($BF),A
site 07297   ; OUT ($BF),A
site 0729A   ; OUT ($BE),A
site 0729D   ; OUT ($BE),A
site 072AA   ; OUT ($BF),A
site 072AD   ; OUT ($BF),A
site 072B0   ; OUT ($BE),A
site 072B3   ; OUT ($BE),A
site 072C0   ; OUT ($BF),A
site 072C3   ; OUT ($BF),A
site 072C6   ; OUT ($BE),A
site 072C9   ; OUT ($BE),A
site 072D6   ; OUT ($BF),A
site 072D9   ; OUT ($BF),A
site 072DC   ; OUT ($BE),A
site 072DF   ; OUT ($BE),A
site 072EC   ; OUT ($BF),A
site 072EF   ; OUT ($BF),A
site 072F2   ; OUT ($BE),A
site 072F5   ; OUT ($BE),A
site 07302   ; OUT ($BF),A
site 07305   ; OUT ($BF),A
site 07308   ; OUT ($BE),A
site 0730B   ; OUT ($BE),A
site 07318   ; OUT ($BF),A
site 0731B   ; OUT ($BF),A
site 0731E   ; OUT ($BE),A
site 07321   ; OUT ($BE),A
site 0732E   ; OUT ($BF),A
site 07331   ; OUT ($BF),A
site 07334   ; OUT ($BE),A
site 07337   ; OUT ($BE),A
site 07344   ; OUT ($BF),A
site 07347   ; OUT ($BF),A
site 0734A   ; OUT ($BE),A
site 0734D   ; OUT ($BE),A
site 0735A   ; OUT ($BF),A
site 0735D   ; OUT ($BF),A
site 07360   ; OUT ($BE),A
site 07363   ; OUT ($BE),A
site 07370   ; OUT ($BF),A
site 07373   ; OUT ($BF),A
site 07376   ; OUT ($BE),A
site 07379   ; OUT ($BE),A
site 07386   ; OUT ($BF),A
site 07389   ; OUT ($BF),A
site 0738C   ; OUT ($BE),A
site 0738F   ; OUT ($BE),A
site 0739C   ; OUT ($BF),A
site 0739F   ; OUT ($BF),A
site 073A2   ; OUT ($BE),A
site 073A5   ; OUT ($BE),A
site 073B2   ; OUT ($BF),A
site 073B5   ; OUT ($BF),A
site 073B8   ; OUT ($BE),A
site 073BB   ; OUT ($BE),A
site 073C8   ; OUT ($BF),A
site 073CB   ; OUT ($BF),A
site 073CE   ; OUT ($BE),A
site 073D1   ; OUT ($BE),A
site 073DE   ; OUT ($BF),A
site 073E1   ; OUT ($BF),A
site 073E4   ; OUT ($BE),A
site 073E7   ; OUT ($BE),A
site 073F4   ; OUT ($BF),A
site 073F7   ; OUT ($BF),A
site 073FA   ; OUT ($BE),A
site 073FD   ; OUT ($BE),A
site 0740A   ; OUT ($BF),A
site 0740D   ; OUT ($BF),A
site 07410   ; OUT ($BE),A
site 07413   ; OUT ($BE),A
site 07420   ; OUT ($BF),A
site 07423   ; OUT ($BF),A
site 07426   ; OUT ($BE),A
site 07429   ; OUT ($BE),A
site 07436   ; OUT ($BF),A
site 07439   ; OUT ($BF),A
site 0743C   ; OUT ($BE),A
site 0743F   ; OUT ($BE),A
site 0744C   ; OUT ($BF),A
site 0744F   ; OUT ($BF),A
site 07452   ; OUT ($BE),A
site 07455   ; OUT ($BE),A
site 0C7EB   ; OUT ($BF),A
site 0C7EE   ; OUT ($BF),A
site 0C7F6   ; OUT ($BE),A
site 0C7FD   ; OUT ($BE),A
site 1505C   ; OUT ($BF),A
site 1505F   ; OUT ($BF),A
site 15064   ; OUT ($BE),A
site 15068   ; OUT ($BE),A
site 1506D   ; OUT ($BE),A
site 15071   ; OUT ($BE),A
site 15095   ; OUT ($BF),A
site 15099   ; OUT ($BF),A
site 1509C   ; OUT ($BF),A
site 150A0   ; OUT ($BF),A
site 163EA   ; OUT ($BF),A
site 163ED   ; OUT ($BF),A
site 163F2   ; OUT ($BE),A
site 163F6   ; OUT ($BE),A
site 163FB   ; OUT ($BE),A
site 163FF   ; OUT ($BE),A
site 16427   ; OUT ($BF),A
site 1642A   ; OUT ($BF),A
site 16437   ; OUT ($BE),A
site 1643B   ; OUT ($BE),A
site 189C5   ; OUT ($BF),A
site 189C8   ; OUT ($BF),A
site 189D9   ; OUT ($BE),A
site 189E0   ; OUT ($BE),A
site 189ED   ; OUT ($BE),A
site 189F4   ; OUT ($BE),A
site 1C1FA   ; OUT ($7F),A
site 1C452   ; OTIR
site 1C56A   ; OUT ($7F),A
site 1C574   ; OUT ($7F),A
site 1C591   ; OUT ($7F),A
site 1C6B9   ; OUT ($7F),A
site 1C74D   ; OUT ($7F),A
site 1C7FA   ; OUT ($7F),A
site 1C803   ; OUT ($7F),A
site 1C813   ; OUT ($7F),A
site 1C893   ; OUT ($7F),A
mapldk 0007A   # LD HL,$FFFC; LD (HL),$00
maphl 00080   # LD (HL),$00, HL = $FFFD
maphl 00083   # LD (HL),$01, HL = $FFFE
maphl 00086   # LD (HL),$02, HL = $FFFF
asm 060F0 2    ; LD (HL),$1D with HL = $ADDA: a write to ROM, a no-op on the Master System
    nop
    nop
endasm
mapst 00098   ; LD ($FFFF),A
mapst 0028F   ; LD ($FFFF),A
mapst 00296   ; LD ($FFFF),A
mapst 00854   ; LD ($FFFF),A
mapst 0090E   ; LD ($FFFF),A
mapst 00936   ; LD ($FFFF),A
mapst 00964   ; LD ($FFFF),A
mapst 00977   ; LD ($FFFF),A
mapst 00AA5   ; LD ($FFFF),A
mapst 00AAC   ; LD ($FFFF),A
mapst 00F15   ; LD ($FFFF),A
mapst 00F74   ; LD ($FFFF),A
mapst 01945   ; LD ($FFFF),A
mapst 01958   ; LD ($FFFF),A
mapst 01962   ; LD ($FFFF),A
mapst 01998   ; LD ($FFFF),A
mapst 019A2   ; LD ($FFFF),A
mapst 019B5   ; LD ($FFFF),A
mapst 0249E   ; LD ($FFFF),A
mapst 024AE   ; LD ($FFFF),A
mapst 024D4   ; LD ($FFFF),A
mapst 02889   ; LD ($FFFF),A
mapst 028AA   ; LD ($FFFF),A
mapst 028B7   ; LD ($FFFF),A
mapst 028E7   ; LD ($FFFF),A
mapst 028F7   ; LD ($FFFF),A
mapst 02905   ; LD ($FFFF),A
mapst 02A36   ; LD ($FFFF),A
mapst 02A55   ; LD ($FFFF),A
mapst 02A71   ; LD ($FFFF),A
mapst 02A88   ; LD ($FFFF),A
mapst 030BD   ; LD ($FFFF),A
mapst 030C5   ; LD ($FFFF),A
mapst 03136   ; LD ($FFFF),A
mapst 03189   ; LD ($FFFF),A
mapst 031A3   ; LD ($FFFF),A
mapst 031FB   ; LD ($FFFF),A
mapst 03208   ; LD ($FFFF),A
mapst 0321F   ; LD ($FFFF),A
mapst 03227   ; LD ($FFFF),A
mapst 03257   ; LD ($FFFF),A
mapst 0325F   ; LD ($FFFF),A
mapst 03288   ; LD ($FFFF),A
mapst 03290   ; LD ($FFFF),A
mapst 03298   ; LD ($FFFF),A
mapst 0330B   ; LD ($FFFF),A
mapst 03331   ; LD ($FFFF),A
mapst 034BC   ; LD ($FFFF),A
mapst 03525   ; LD ($FFFF),A
mapst 035BF   ; LD ($FFFF),A
mapst 035F0   ; LD ($FFFF),A
mapst 0360A   ; LD ($FFFF),A
mapst 03666   ; LD ($FFFF),A
mapst 0366E   ; LD ($FFFF),A
mapst 03685   ; LD ($FFFF),A
mapst 0368D   ; LD ($FFFF),A
mapst 036A8   ; LD ($FFFF),A
mapst 036B0   ; LD ($FFFF),A
mapst 036DC   ; LD ($FFFF),A
mapst 036E4   ; LD ($FFFF),A
mapst 037A3   ; LD ($FFFF),A
mapst 037AB   ; LD ($FFFF),A
mapst 03914   ; LD ($FFFF),A
mapst 0399E   ; LD ($FFFF),A
mapst 039A7   ; LD ($FFFF),A
mapst 03A4B   ; LD ($FFFF),A
mapst 03A7D   ; LD ($FFFF),A
mapst 03A85   ; LD ($FFFF),A
mapst 03ACB   ; LD ($FFFF),A
mapst 03AD1   ; LD ($FFFF),A
mapst 03D6E   ; LD ($FFFF),A
mapst 03D92   ; LD ($FFFF),A
mapst 03DAC   ; LD ($FFFF),A
mapst 03DFF   ; LD ($FFFF),A
mapst 03E0C   ; LD ($FFFF),A
mapst 03E1E   ; LD ($FFFF),A
mapst 03E26   ; LD ($FFFF),A
mapst 03E5B   ; LD ($FFFF),A
mapst 03E63   ; LD ($FFFF),A
mapst 03E75   ; LD ($FFFF),A
mapst 03E7D   ; LD ($FFFF),A
mapst 03E9D   ; LD ($FFFF),A
mapst 03EB3   ; LD ($FFFF),A
mapst 03EBB   ; LD ($FFFF),A
mapst 043EF   ; LD ($FFFF),A
mapst 043F8   ; LD ($FFFF),A
mapst 04504   ; LD ($FFFF),A
mapst 04517   ; LD ($FFFF),A
mapst 045D5   ; LD ($FFFF),A
mapst 045DE   ; LD ($FFFF),A
mapst 04A36   ; LD ($FFFF),A
mapst 04A3F   ; LD ($FFFF),A
mapst 05586   ; LD ($FFFF),A
mapst 055CE   ; LD ($FFFF),A
mapst 066E8   ; LD ($FFFF),A
mapst 066F4   ; LD ($FFFF),A
mapst 0675D   ; LD ($FFFF),A
mapst 06775   ; LD ($FFFF),A
mapst 0678E   ; LD ($FFFF),A
mapst 07554   ; LD ($FFFF),A
mapst 07588   ; LD ($FFFF),A
mapst 07610   ; LD ($FFFF),A
mapst 07624   ; LD ($FFFF),A
mapst 0763A   ; LD ($FFFF),A
mapst 0767D   ; LD ($FFFF),A
mapst 07695   ; LD ($FFFF),A
mapst 07703   ; LD ($FFFF),A
mapst 07715   ; LD ($FFFF),A
mapst 077B4   ; LD ($FFFF),A
mapst 077CB   ; LD ($FFFF),A

# Buggy Run (Europe) (Action Replay).cht and Buggy Run (Europe, Brazil).cht, "Infinite Money P1"
# and "P1 Infinite Money": RAM $CE4C-$CE4D is the money in units of $100; the high byte at $27
# makes the shop show the largest amount ($999,900) and a purchase takes none of it
poke "Infinite money"
ar 00CE-4D27
endpoke

# Buggy Run (Europe) (Action Replay).cht and Buggy Run (Europe, Brazil).cht, "Infinite Mines (At
# Setup Screen)": RAM $C839 is the mine stock of the SET UP screen, shown as 99
poke "99 mines"
ar 00C8-3963
endpoke

# Buggy Run (Europe) (Action Replay).cht and Buggy Run (Europe, Brazil).cht, "Infinite Nitoro (At
# Setup Screen)": RAM $C83A is the nitro stock of the SET UP screen, shown as 99
poke "99 nitros"
ar 00C8-3A63
endpoke

# Buggy Run (Europe, Brazil).cht, "P1 Max Item Slots": RAM $C838 is the number of CAPACITY
# slots on the SET UP screen, 6 slots instead of 2
poke "Six item slots"
ar 00C8-3806
endpoke

# Buggy Run (Europe, Brazil).cht, "Infinite Nitros/Mines - Both Players": the Game Genie patch
# stops the race from taking a nitro or a mine out of its slot when it is used
poke "Infinite items"
gg 004-AEE-3B2
endpoke

# Buggy Run (Europe, Brazil).cht, "P1 Tire Upgrades", "P1 Engine Uprgrades", "P1 Suspension
# Upgrades", "P1 Steering Upgrades" and "P1 Transmission Upgrades": RAM $CE41-$CE45 are the
# levels of the five parts, shown as LV.1 to LV.4 on the SET UP screen; the files hold 01, and
# the placeholder lets the player choose
poke "Parts level"
ar 00CE-41??
ar 00CE-42??
ar 00CE-43??
ar 00CE-44??
ar 00CE-45??
endpoke

# Buggy Run (Europe) (Action Replay).cht and Buggy Run (Europe, Brazil).cht, "Infinite Points P1"
# and "P1 Infinite Points": RAM $CE24 held at $64 makes the RESULT screen show the player's total as 99
poke "Maximum points"
ar 00CE-2464
endpoke
