# rasterparallax, drafted by tools/mkspec.py from sitescan output.
name rasterparallax
cart 05DDDD90
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
site 01BC   ; OUT ($BF),A
site 01C0   ; OUT ($BF),A
otir 01C6   ; OUTI
site 02A0   ; OUT ($BE),A
site 02BA   ; OUT ($BF),A
site 02BE   ; OUT ($BF),A
otir 02C4   ; OUTI
site 0439   ; OUT ($BE),A
site 0442   ; OUT ($BE),A
site 0493   ; OUT ($BF),A
site 0497   ; OUT ($BF),A
site 049D   ; OUT ($BF),A
site 04A1   ; OUT ($BF),A
site 04EE   ; OUT ($BF),A
site 04F3   ; OUT ($BF),A
site 0504   ; OUT ($BF),A
site 0509   ; OUT ($BF),A
site 054E   ; OUTI
site 0550   ; OUTI
site 0552   ; OUTI
site 0554   ; OUTI
site 0556   ; OUTI
site 0558   ; OUTI
site 055A   ; OUTI
site 055C   ; OUTI
site 055E   ; OUTI
site 0560   ; OUTI
site 0562   ; OUTI
site 0564   ; OUTI
site 0566   ; OUTI
site 0568   ; OUTI
site 056A   ; OUTI
site 056C   ; OUTI
site 056E   ; OUTI
site 0570   ; OUTI
site 0572   ; OUTI
site 0574   ; OUTI
site 0576   ; OUTI
site 0578   ; OUTI
site 057A   ; OUTI
site 057C   ; OUTI
site 057E   ; OUTI
site 0580   ; OUTI
site 0582   ; OUTI
site 0584   ; OUTI
site 0586   ; OUTI
site 0588   ; OUTI
site 058A   ; OUTI
site 058C   ; OUTI
site 058E   ; OUTI
site 0590   ; OUTI
site 0592   ; OUTI
site 0594   ; OUTI
site 0596   ; OUTI
site 0598   ; OUTI
site 059A   ; OUTI
site 059C   ; OUTI
site 059E   ; OUTI
site 05A0   ; OUTI
site 05A2   ; OUTI
site 05A4   ; OUTI
site 05A6   ; OUTI
site 05A8   ; OUTI
site 05AA   ; OUTI
site 05AC   ; OUTI
site 05AE   ; OUTI
site 05B0   ; OUTI
site 05B2   ; OUTI
site 05B4   ; OUTI
site 05B6   ; OUTI
site 05B8   ; OUTI
site 05BA   ; OUTI
site 05BC   ; OUTI
site 05BE   ; OUTI
site 05C0   ; OUTI
site 05C2   ; OUTI
site 05C4   ; OUTI
site 05C6   ; OUTI
site 05C8   ; OUTI
site 05CA   ; OUTI
site 05CC   ; OUTI
site 05CE   ; OUTI
site 05D0   ; OUTI
site 05D2   ; OUTI
site 05D4   ; OUTI
site 05D6   ; OUTI
site 05D8   ; OUTI
site 05DA   ; OUTI
site 05DC   ; OUTI
site 05DE   ; OUTI
site 05E0   ; OUTI
site 05E2   ; OUTI
site 05E4   ; OUTI
site 05E6   ; OUTI
site 05E8   ; OUTI
site 05EA   ; OUTI
site 05EC   ; OUTI
site 05EE   ; OUTI
site 05F0   ; OUTI
site 05F2   ; OUTI
site 05F4   ; OUTI
site 05F6   ; OUTI
site 05F8   ; OUTI
site 05FA   ; OUTI
site 05FC   ; OUTI
site 05FE   ; OUTI
site 0600   ; OUTI
site 0602   ; OUTI
site 0604   ; OUTI
site 0606   ; OUTI
site 0608   ; OUTI
site 060A   ; OUTI
site 060C   ; OUTI
site 060E   ; OUTI
site 0610   ; OUTI
site 0612   ; OUTI
site 0614   ; OUTI
site 0616   ; OUTI
site 0618   ; OUTI
site 061A   ; OUTI
site 061C   ; OUTI
site 061E   ; OUTI
site 0620   ; OUTI
site 0622   ; OUTI
site 0624   ; OUTI
site 0626   ; OUTI
site 0628   ; OUTI
site 062A   ; OUTI
site 062C   ; OUTI
site 062E   ; OUTI
site 0630   ; OUTI
site 0632   ; OUTI
site 0634   ; OUTI
site 0636   ; OUTI
site 0638   ; OUTI
site 063A   ; OUTI
site 063C   ; OUTI
site 063E   ; OUTI
site 0640   ; OUTI
site 0642   ; OUTI
site 0644   ; OUTI
site 0646   ; OUTI
site 0648   ; OUTI
site 064A   ; OUTI
site 064C   ; OUTI
# CHECK mapper at 006F: LD ($FFFC),DE $FFFC,$FFFD
# CHECK mapper at 0076: LD ($FFFE),DE $FFFE,$FFFF
# CHECK indirect_unresolved at 00F5: CALL $0032 
# CHECK low: site 850B  IN B,(C)  (port in C)
# CHECK low: site 877E  IN A,($BF)  (vdp_status)
# CHECK low: site 87B8  OUT ($DD),A  (no_effect)
# CHECK low: site 8A01  OUT ($3E),A  (memory_control)
# CHECK low: site 8A5D  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 9333  OTDR  (port in C)
# CHECK low: site 949C  IN A,($BD)  (vdp_status)
# CHECK low: site 96D0  OUT ($7F),A  (psg)
# CHECK low: site 99B9  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 9CD7  IN A,($DC)  (joypad_a)
# CHECK low: site 9E7A  IN A,($7F)  (h_counter)
# CHECK low: site A1EA  OUT ($BF),A  (vdp_control)
# CHECK low: site A57B  OTIR  (port in C)
