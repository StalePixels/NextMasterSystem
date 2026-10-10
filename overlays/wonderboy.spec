# Wonder Boy (USA, Europe, Brazil) (Rev 1), 73705C02, drafted by tools/mkspec.py from sitescan output.
name Wonder Boy
cart 73705C02
# tilecache: whole tiles copied from cart ROM are not converted again (MAME,
# game frames 300-2300: framework cycles -1.5%, vertical blank tile work halved)
tilecache
# No free RST vector: $0000-$0002 (the game's interrupt mode 1 setup and the start of its stack setup) becomes the vector,
# the game starts at $0005 with the SP its LD SP,nn set.
vector 00 io
start 0005 DFFF
site 0003E   ; OUT ($BF),A
site 00043   ; OUT ($BF),A
site 000B2   ; IN A,($BF)
site 000DE   ; IN A,($DD)
site 00183   ; OUT ($DE),A
site 00185   ; IN A,($DC)
site 00190   ; IN A,($DD)
site 001C8   ; OUT ($BF),A
site 001CF   ; OUT ($BF),A
site 001D4   ; OUT ($BF),A
site 001D9   ; OUT ($BF),A
site 001E1   ; IN A,($BE)
site 001EB   ; OUT ($BE),A
site 001F0   ; OUT ($BE),A
site 001F4   ; OUT ($BE),A
site 001F8   ; OUT ($BE),A
site 0020A   ; OUT ($BE),A
site 0021C   ; OUT ($BF),A
site 00220   ; OUT ($BF),A
site 00233   ; OUT ($BF),A
site 00237   ; OUT ($BF),A
site 00246   ; OUT ($BF),A
site 0024A   ; OUT ($BF),A
site 00257   ; OUT ($BF),A
site 0025B   ; OUT ($BF),A
site 00284   ; OUT ($BF),A
site 00287   ; OUT ($BF),A
site 002D9   ; OUTI
site 002DB   ; OUTI
site 002DD   ; OUTI
site 002DF   ; OUTI
site 002E1   ; OUTI
site 002E3   ; OUTI
site 002E5   ; OUTI
site 002E7   ; OUTI
site 002E9   ; OUTI
site 002EB   ; OUTI
site 002ED   ; OUTI
site 002EF   ; OUTI
site 002F1   ; OUTI
site 002F3   ; OUTI
site 002F5   ; OUTI
site 002F7   ; OUTI
site 002F9   ; OUTI
site 002FB   ; OUTI
site 002FD   ; OUTI
site 002FF   ; OUTI
site 00301   ; OUTI
site 00303   ; OUTI
site 00305   ; OUTI
site 00307   ; OUTI
site 00309   ; OUTI
site 0030B   ; OUTI
site 0030D   ; OUTI
site 0030F   ; OUTI
site 00311   ; OUTI
site 00313   ; OUTI
site 00315   ; OUTI
site 00317   ; OUTI
site 00319   ; OUTI
site 0031B   ; OUTI
site 0031D   ; OUTI
site 0031F   ; OUTI
site 00321   ; OUTI
site 00323   ; OUTI
site 00325   ; OUTI
site 00327   ; OUTI
site 00329   ; OUTI
site 0032B   ; OUTI
site 0032D   ; OUTI
site 0032F   ; OUTI
site 00331   ; OUTI
site 00333   ; OUTI
site 00335   ; OUTI
site 00337   ; OUTI
site 00339   ; OUTI
site 0033B   ; OUTI
site 0033D   ; OUTI
site 0033F   ; OUTI
site 00341   ; OUTI
site 00343   ; OUTI
site 00345   ; OUTI
site 00347   ; OUTI
site 00349   ; OUTI
site 0034B   ; OUTI
site 0034D   ; OUTI
site 0034F   ; OUTI
site 00351   ; OUTI
site 00353   ; OUTI
site 00355   ; OUTI
site 00357   ; OUTI
site 00359   ; OUTI
site 0035B   ; OUTI
site 0035D   ; OUTI
site 0035F   ; OUTI
site 00361   ; OUTI
site 00363   ; OUTI
site 00365   ; OUTI
site 00367   ; OUTI
site 00369   ; OUTI
site 0036B   ; OUTI
site 0036D   ; OUTI
site 0036F   ; OUTI
site 00371   ; OUTI
site 00373   ; OUTI
site 00375   ; OUTI
site 00377   ; OUTI
site 00379   ; OUTI
site 0037B   ; OUTI
site 0037D   ; OUTI
site 0037F   ; OUTI
site 00381   ; OUTI
site 00383   ; OUTI
site 00385   ; OUTI
site 00387   ; OUTI
site 00389   ; OUTI
site 0038B   ; OUTI
site 0038D   ; OUTI
site 0038F   ; OUTI
site 00391   ; OUTI
site 00393   ; OUTI
site 00395   ; OUTI
site 00397   ; OUTI
site 00399   ; OUTI
site 0039B   ; OUTI
site 0039D   ; OUTI
site 0039F   ; OUTI
site 003A1   ; OUTI
site 003A3   ; OUTI
site 003A5   ; OUTI
site 003A7   ; OUTI
site 003A9   ; OUTI
site 003AB   ; OUTI
site 003AD   ; OUTI
site 003AF   ; OUTI
site 003B1   ; OUTI
site 003B3   ; OUTI
site 003B5   ; OUTI
site 003B7   ; OUTI
site 003B9   ; OUTI
site 003BB   ; OUTI
site 003BD   ; OUTI
site 003BF   ; OUTI
site 003C1   ; OUTI
site 003C3   ; OUTI
site 003C5   ; OUTI
site 003C7   ; OUTI
site 003C9   ; OUTI
site 003CB   ; OUTI
site 003CD   ; OUTI
site 003CF   ; OUTI
site 003D1   ; OUTI
site 003D3   ; OUTI
site 003D5   ; OUTI
site 003D7   ; OUTI
site 00408   ; OUT ($BF),A
site 0040B   ; OUT ($BF),A
site 00410   ; OUT ($BE),A
site 00415   ; OUT ($BF),A
site 0041C   ; OUT ($BF),A
site 0041F   ; OUT ($BE),A
site 00473   ; OUT ($BE),A
site 00483   ; OUT ($BE),A
site 0048D   ; OUT ($BE),A
site 00492   ; OUT ($BE),A
site 0049D   ; OUT ($3F),A
site 0049F   ; IN A,($DD)
site 004A9   ; OUT ($3F),A
site 004AB   ; IN A,($DD)
site 004B4   ; OUT ($3F),A
site 01E4D   ; OUT ($BF),A
site 01E54   ; OUT ($BF),A
site 01E57   ; OUT ($BE),A
site 01E8C   ; OUT ($BF),A
site 01E93   ; OUT ($BF),A
site 01E99   ; OUTI
site 01E9B   ; OUT (C),A
site 01E9D   ; OUTI
site 01E9F   ; OUT (C),A
site 01EA1   ; OUTI
site 01EA3   ; OUT (C),A
site 01EA5   ; OUTI
site 01EA7   ; OUT (C),A
site 01EA9   ; OUTI
site 01EAB   ; OUT (C),A
site 01EAD   ; OUTI
site 01EAF   ; OUT (C),A
site 01EB1   ; OUTI
site 01EB3   ; OUT (C),A
site 01EB5   ; OUTI
site 01EB7   ; OUT (C),A
site 01EB9   ; OUTI
site 01EBB   ; OUT (C),A
site 01EBD   ; OUTI
site 01EBF   ; OUT (C),A
site 01EC1   ; OUTI
site 01EC3   ; OUT (C),A
site 01EC5   ; OUTI
site 01EC7   ; OUT (C),A
site 01EC9   ; OUTI
site 01ECB   ; OUT (C),A
site 01ECD   ; OUTI
site 01ECF   ; OUT (C),A
site 01ED1   ; OUTI
site 01ED3   ; OUT (C),A
site 01ED5   ; OUTI
site 01ED7   ; OUT (C),A
site 01ED9   ; OUTI
site 01EDB   ; OUT (C),A
site 01EDD   ; OUTI
site 01EDF   ; OUT (C),A
site 01EE1   ; OUTI
site 01EE3   ; OUT (C),A
site 01EE5   ; OUTI
site 01EE7   ; OUT (C),A
site 01EE9   ; OUTI
site 01EEB   ; OUT (C),A
site 01EED   ; OUTI
site 01EEF   ; OUT (C),A
site 01EF1   ; OUTI
site 01EF3   ; OUT (C),A
site 01EF5   ; OUTI
site 01EF7   ; OUT (C),A
site 01EF9   ; OUTI
site 01EFB   ; OUT (C),A
site 01EFD   ; OUTI
site 01EFF   ; OUT (C),A
site 01F01   ; OUTI
site 01F03   ; OUT (C),A
site 01F05   ; OUTI
site 01F07   ; OUT (C),A
site 01F09   ; OUTI
site 01F0B   ; OUT (C),A
site 01F0D   ; OUTI
site 01F0F   ; OUT (C),A
site 01F11   ; OUTI
site 01F13   ; OUT (C),A
site 01F15   ; OUTI
site 01F17   ; OUT (C),A
site 06E35   ; OUT ($7F),A
site 06E39   ; OUT ($7F),A
site 070E5   ; OUT ($7F),A
site 07156   ; OUT ($7F),A
site 07170   ; OTIR
mapst 00B13   ; LD ($FFFF),A
# the other low-confidence byte patterns are data or instruction operands
