# Kenseiden (USA, Europe, Brazil) (En), CRC32 516ED32E, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input).
# Decisions:
# - No free RST vector ($0008, $0018 and $0028 are the game's, $0010, $0020 and $0030
#   are inside them), so $0000 is the io vector.
# - The line interrupt handler is code in RAM at $C600. The game copies it there from
#   the cart ($0CCB for the intro's title wave, $5E80 for a handler that no recording ran),
#   so the site lines patch those ROM bytes, and the copies in RAM carry the patches.
# - The title wave sets H scroll on each line from line 31 to line 80, from line
#   interrupts (register 10 = 0). The rastercode routine kenseiden-raster.asm works out each
#   line's H from the game's table at $C700, so the game gets no line events while the
#   wave runs.
# - No priority: the only name table cells with the priority bit are in rows 24-27,
#   below the 192-line picture, and V scroll is always 0.
# - Site $0907 is in the text routine $07FC, which code in bank 0 ($0ECA) and bank 1
#   calls and no scanned path or recording reaches. The other byte patterns that no
#   path reached are graphics or data (verdict false).
# - The Next is an export console to the region check at $04C2 ($C001 = $FF), so the
#   game skips the power-on delay $0932 and the SEGA logo, as on an export Master System.
name Kenseiden
cart 516ED32E
hz any		; No-Intro regions USA, Europe, Brazil
rastercode kenseiden-raster.asm
vector 00 io
start 0003
site 0002A   ; OUT ($BF),A
site 0002D   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 000B3   ; OUT ($BF),A
site 000B7   ; OUT ($BF),A
site 001A3   ; OUT ($BF),A
site 001A7   ; OUT ($BF),A
site 0021E   ; OUT ($BF),A
site 00222   ; OUT ($BF),A
site 00228   ; OUTI
site 0023E   ; OUT ($BF),A
site 00242   ; OUT ($BF),A
site 00248   ; OUT ($BE),A
site 00254   ; OUTI
site 00256   ; OUTI
site 00264   ; OUTI
site 0026C   ; OUT ($BF),A
site 00270   ; OUT ($BF),A
site 0027B   ; OUT ($BF),A
site 0027E   ; OUT ($BF),A
site 00283   ; OUTI
site 00285   ; OUTI
site 00287   ; OUTI
site 00289   ; OUTI
site 0028B   ; OUTI
site 0028D   ; OUTI
site 0028F   ; OUTI
site 00291   ; OUTI
site 00293   ; OUTI
site 00295   ; OUTI
site 00297   ; OUTI
site 00299   ; OUTI
site 0029B   ; OUTI
site 0029D   ; OUTI
site 0029F   ; OUTI
site 002A1   ; OUTI
site 002A3   ; OUTI
site 002A5   ; OUTI
site 002A7   ; OUTI
site 002A9   ; OUTI
site 002AB   ; OUTI
site 002AD   ; OUTI
site 002AF   ; OUTI
site 002B1   ; OUTI
site 002B3   ; OUTI
site 002B5   ; OUTI
site 002B7   ; OUTI
site 002B9   ; OUTI
site 002BB   ; OUTI
site 002BD   ; OUTI
site 002BF   ; OUTI
site 002C1   ; OUTI
site 002C3   ; OUTI
site 002C5   ; OUTI
site 002C7   ; OUTI
site 002C9   ; OUTI
site 002CB   ; OUTI
site 002CD   ; OUTI
site 002CF   ; OUTI
site 002D1   ; OUTI
site 002D3   ; OUTI
site 002D5   ; OUTI
site 002D7   ; OUTI
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
site 00392   ; OUT ($BE),A
site 00399   ; IN A,($BE)
site 0039D   ; IN A,($BE)
site 003A1   ; IN A,($BE)
site 003BD   ; OUTI
site 003CD   ; OUT ($BE),A
site 003D2   ; OUT ($BE),A
site 003DF   ; OUTI
site 003E5   ; OUT (C),A
site 003F9   ; OUTI
site 0041E   ; OUT (C),D
site 0042E   ; OUTI
site 00434   ; OUT (C),A
site 00446   ; OUT ($BF),A
site 00449   ; OUT ($BF),A
site 00457   ; OUT ($BE),A
site 00465   ; IN A,($DC)
site 00473   ; IN A,($DD)
site 0049A   ; OUT ($3E),A
site 004A2   ; OUT ($F2),A
site 004A5   ; IN A,($F2)
site 004B7   ; OUT ($F2),A
site 004BF   ; OUT ($3E),A
site 004C7   ; OUT ($3F),A
site 004C9   ; IN A,($DD)
site 004D3   ; OUT ($3F),A
site 004D5   ; IN A,($DD)
site 004DE   ; OUT ($3F),A
site 00619   ; OUT ($BF),A
site 0061D   ; OUT ($BF),A
site 00626   ; OUTI
site 00633   ; OUT ($BF),A
site 00637   ; OUT ($BF),A
site 0063E   ; OUTI
site 00653   ; OUT ($BF),A
site 00657   ; OUT ($BF),A
site 0065E   ; OUTI
site 0067F   ; OUT (C),E
site 00681   ; OUT (C),D
site 00687   ; OUT ($BE),A
site 0068C   ; OUT ($BE),A
site 00692   ; OUT ($BE),A
site 00697   ; OUT ($BE),A
site 006A0   ; OUT ($BF),A
site 006A4   ; OUT ($BF),A
site 006AF   ; OUT ($BE),A
site 0074A   ; IN A,($BF)
site 00983   ; IN A,($BE)
site 009A3   ; OUT ($BE),A
site 00CD6   ; OUT ($BF),A
site 00CDA   ; OUT ($BF),A
site 00CDE   ; OUT ($BF),A
site 00CE2   ; OUT ($BF),A
site 01A20   ; OUT ($BF),A
site 01A24   ; OUT ($BF),A
site 01A37   ; OUT (C),L
site 01A3C   ; OUT ($BF),A
site 01A41   ; OUT ($BE),A
site 01A45   ; OUT ($BE),A
site 01C97   ; OUT ($BF),A
site 01C9B   ; OUT ($BF),A
site 01CA0   ; OUTI
site 01CA2   ; OUTI
site 01CA4   ; OUTI
site 01CA6   ; OUT ($BE),A
site 01CA8   ; OUTI
site 01CAA   ; OUTI
site 01CAC   ; OUTI
site 01CAE   ; OUT ($BE),A
site 01CB0   ; OUTI
site 01CB2   ; OUTI
site 01CB4   ; OUTI
site 01CB6   ; OUT ($BE),A
site 01CB8   ; OUTI
site 01CBA   ; OUTI
site 01CBC   ; OUTI
site 01CBE   ; OUT ($BE),A
site 01CC0   ; OUTI
site 01CC2   ; OUTI
site 01CC4   ; OUTI
site 01CC6   ; OUT ($BE),A
site 01CC8   ; OUTI
site 01CCA   ; OUTI
site 01CCC   ; OUTI
site 01CCE   ; OUT ($BE),A
site 01CD0   ; OUTI
site 01CD2   ; OUTI
site 01CD4   ; OUTI
site 01CD6   ; OUT ($BE),A
site 01CD8   ; OUTI
site 01CDA   ; OUTI
site 01CDC   ; OUTI
site 01CDE   ; OUT ($BE),A
site 01CE0   ; OUTI
site 01CE2   ; OUTI
site 01CE4   ; OUTI
site 01CE6   ; OUT ($BE),A
site 01CE8   ; OUTI
site 01CEA   ; OUTI
site 01CEC   ; OUTI
site 01CEE   ; OUT ($BE),A
site 01CF0   ; OUTI
site 01CF2   ; OUTI
site 01CF4   ; OUTI
site 01CF6   ; OUT ($BE),A
site 01CF8   ; OUTI
site 01CFA   ; OUTI
site 01CFC   ; OUTI
site 01CFE   ; OUT ($BE),A
site 01D00   ; OUTI
site 01D02   ; OUTI
site 01D04   ; OUTI
site 01D06   ; OUT ($BE),A
site 01D08   ; OUTI
site 01D0A   ; OUTI
site 01D0C   ; OUTI
site 01D0E   ; OUT ($BE),A
site 01D10   ; OUTI
site 01D12   ; OUTI
site 01D14   ; OUTI
site 01D16   ; OUT ($BE),A
site 01D18   ; OUTI
site 01D1A   ; OUTI
site 01D1C   ; OUTI
site 01D1E   ; OUT ($BE),A
site 02C02   ; OUT ($BF),A
site 02C05   ; OUT ($BF),A
site 02C0A   ; OUTI
site 02C0F   ; OUT (C),A
site 04D3E   ; OUTI
site 04D40   ; OUTI
site 04D67   ; OUTI
site 04D69   ; OUTI
site 04D6B   ; OUTI
site 04D6D   ; OUTI
site 04D6F   ; OUTI
site 04D71   ; OUTI
site 04D73   ; OUTI
site 04D75   ; OUTI
site 04D77   ; OUTI
site 04D79   ; OUTI
site 04D7B   ; OUTI
site 04D7D   ; OUTI
site 04D7F   ; OUTI
site 04D81   ; OUTI
site 04D83   ; OUTI
site 04D85   ; OUTI
site 04D87   ; OUTI
site 04D89   ; OUTI
site 04D8B   ; OUTI
site 04D8D   ; OUTI
site 04D8F   ; OUTI
site 04D91   ; OUTI
site 04D93   ; OUTI
site 04D95   ; OUTI
site 04D97   ; OUTI
site 04D99   ; OUTI
site 04D9B   ; OUTI
site 04D9D   ; OUTI
site 04D9F   ; OUTI
site 04DA1   ; OUTI
site 04DA3   ; OUTI
site 04DA5   ; OUTI
site 04DA7   ; OUTI
site 04DA9   ; OUTI
site 04DAB   ; OUTI
site 04DAD   ; OUTI
site 04DAF   ; OUTI
site 04DB1   ; OUTI
site 04DB3   ; OUTI
site 04DB5   ; OUTI
site 04DB7   ; OUTI
site 04DB9   ; OUTI
site 04DBB   ; OUTI
site 04DBD   ; OUTI
site 04DBF   ; OUTI
site 04DC1   ; OUTI
site 04DC3   ; OUTI
site 04DC5   ; OUTI
site 04DC7   ; OUTI
site 04DC9   ; OUTI
site 04DCB   ; OUTI
site 04DCD   ; OUTI
site 04DCF   ; OUTI
site 04DD1   ; OUTI
site 04DD3   ; OUTI
site 04DD5   ; OUTI
site 04DD7   ; OUTI
site 04DD9   ; OUTI
site 04DDB   ; OUTI
site 04DDD   ; OUTI
site 04DDF   ; OUTI
site 04DE1   ; OUTI
site 04DE3   ; OUTI
site 04DE5   ; OUTI
site 04DE7   ; OUTI
site 04DE9   ; OUTI
site 04DEB   ; OUTI
site 04DED   ; OUTI
site 04DEF   ; OUTI
site 04DF1   ; OUTI
site 04DF3   ; OUTI
site 04DF5   ; OUTI
site 04DF7   ; OUTI
site 04DF9   ; OUTI
site 04DFB   ; OUTI
site 04DFD   ; OUTI
site 04DFF   ; OUTI
site 04E01   ; OUTI
site 04E03   ; OUTI
site 04E05   ; OUTI
site 04E07   ; OUTI
site 04E09   ; OUTI
site 04E0B   ; OUTI
site 04E0D   ; OUTI
site 04E0F   ; OUTI
site 04E11   ; OUTI
site 04E13   ; OUTI
site 04E15   ; OUTI
site 04E17   ; OUTI
site 04E19   ; OUTI
site 04E1B   ; OUTI
site 04E1D   ; OUTI
site 04E1F   ; OUTI
site 04E21   ; OUTI
site 04E23   ; OUTI
site 04E25   ; OUTI
site 04E27   ; OUTI
site 04E29   ; OUTI
site 04E2B   ; OUTI
site 04E2D   ; OUTI
site 04E2F   ; OUTI
site 04E31   ; OUTI
site 04E33   ; OUTI
site 04E35   ; OUTI
site 04E37   ; OUTI
site 04E39   ; OUTI
site 04E3B   ; OUTI
site 04E3D   ; OUTI
site 04E3F   ; OUTI
site 04E41   ; OUTI
site 04E43   ; OUTI
site 04E45   ; OUTI
site 04E47   ; OUTI
site 04E49   ; OUTI
site 04E4B   ; OUTI
site 04E4D   ; OUTI
site 04E4F   ; OUTI
site 04E51   ; OUTI
site 04E53   ; OUTI
site 04E55   ; OUTI
site 04E57   ; OUTI
site 04E59   ; OUTI
site 04E5B   ; OUTI
site 04E5D   ; OUTI
site 04E5F   ; OUTI
site 04E61   ; OUTI
site 04E63   ; OUTI
site 04E65   ; OUTI
site 04E67   ; OUTI
site 04E69   ; OUTI
site 04E6B   ; OUTI
site 04E6D   ; OUTI
site 04E6F   ; OUTI
site 04E71   ; OUTI
site 04E73   ; OUTI
site 04E75   ; OUTI
site 04E77   ; OUTI
site 04E79   ; OUTI
site 04E7B   ; OUTI
site 04E7D   ; OUTI
site 04E7F   ; OUTI
site 04E81   ; OUTI
site 04E83   ; OUTI
site 04E85   ; OUTI
site 04E87   ; OUTI
site 04E89   ; OUTI
site 04E8B   ; OUTI
site 04E8D   ; OUTI
site 04E8F   ; OUTI
site 04E91   ; OUTI
site 04E93   ; OUTI
site 04E95   ; OUTI
site 04E97   ; OUTI
site 04E99   ; OUTI
site 04E9B   ; OUTI
site 04E9D   ; OUTI
site 04E9F   ; OUTI
site 04EA1   ; OUTI
site 04EA3   ; OUTI
site 04EA5   ; OUTI
site 04EA7   ; OUTI
site 04EA9   ; OUTI
site 04EAB   ; OUTI
site 04EAD   ; OUTI
site 04EAF   ; OUTI
site 04EB1   ; OUTI
site 04EB3   ; OUTI
site 04EB5   ; OUTI
site 04EB7   ; OUTI
site 04EB9   ; OUTI
site 04EBB   ; OUTI
site 04EBD   ; OUTI
site 04EBF   ; OUTI
site 04EC1   ; OUTI
site 04EC3   ; OUTI
site 04EC5   ; OUTI
site 04EC7   ; OUTI
site 04EC9   ; OUTI
site 04ECB   ; OUTI
site 04ECD   ; OUTI
site 04ECF   ; OUTI
site 04ED1   ; OUTI
site 04ED3   ; OUTI
site 04ED5   ; OUTI
site 04ED7   ; OUTI
site 04ED9   ; OUTI
site 04EDB   ; OUTI
site 04EDD   ; OUTI
site 04EDF   ; OUTI
site 04EE1   ; OUTI
site 04EE3   ; OUTI
site 04EE5   ; OUTI
site 04EE7   ; OUTI
site 04EE9   ; OUTI
site 04EEB   ; OUTI
site 04EED   ; OUTI
site 04EEF   ; OUTI
site 04EF1   ; OUTI
site 04EF3   ; OUTI
site 04EF5   ; OUTI
site 04EF7   ; OUTI
site 04EF9   ; OUTI
site 04EFB   ; OUTI
site 04EFD   ; OUTI
site 04EFF   ; OUTI
site 04F01   ; OUTI
site 04F03   ; OUTI
site 04F05   ; OUTI
site 04F07   ; OUTI
site 04F09   ; OUTI
site 04F0B   ; OUTI
site 04F0D   ; OUTI
site 04F0F   ; OUTI
site 04F11   ; OUTI
site 04F13   ; OUTI
site 04F15   ; OUTI
site 04F17   ; OUTI
site 04F19   ; OUTI
site 04F1B   ; OUTI
site 04F1D   ; OUTI
site 04F1F   ; OUTI
site 04F21   ; OUTI
site 04F23   ; OUTI
site 04F25   ; OUTI
site 04F27   ; OUTI
site 04F29   ; OUTI
site 04F2B   ; OUTI
site 04F2D   ; OUTI
site 04F2F   ; OUTI
site 04F31   ; OUTI
site 04F33   ; OUTI
site 04F35   ; OUTI
site 04F37   ; OUTI
site 04F39   ; OUTI
site 04F3B   ; OUTI
site 04F3D   ; OUTI
site 04F3F   ; OUTI
site 04F41   ; OUTI
site 04F43   ; OUTI
site 04F45   ; OUTI
site 04F47   ; OUTI
site 04F49   ; OUTI
site 04F4B   ; OUTI
site 04F4D   ; OUTI
site 04F4F   ; OUTI
site 04F51   ; OUTI
site 04F53   ; OUTI
site 04F55   ; OUTI
site 04F57   ; OUTI
site 04F59   ; OUTI
site 04F5B   ; OUTI
site 04F5D   ; OUTI
site 04F5F   ; OUTI
site 04F61   ; OUTI
site 04F63   ; OUTI
site 04F65   ; OUTI
site 04F67   ; OUTI
site 04F69   ; OUTI
site 04F6B   ; OUTI
site 04F6D   ; OUTI
site 04F6F   ; OUTI
site 04F71   ; OUTI
site 04F73   ; OUTI
site 04F75   ; OUTI
site 04F77   ; OUTI
site 04F79   ; OUTI
site 04F7B   ; OUTI
site 04F7D   ; OUTI
site 04F7F   ; OUTI
site 04F81   ; OUTI
site 04F83   ; OUTI
site 04F85   ; OUTI
site 04F87   ; OUTI
site 04F89   ; OUTI
site 04F8B   ; OUTI
site 04F8D   ; OUTI
site 04F8F   ; OUTI
site 04F91   ; OUTI
site 04F93   ; OUTI
site 04F95   ; OUTI
site 04F97   ; OUTI
site 04F99   ; OUTI
site 04F9B   ; OUTI
site 04F9D   ; OUTI
site 04F9F   ; OUTI
site 04FA1   ; OUTI
site 04FA3   ; OUTI
site 04FA5   ; OUTI
site 04FA7   ; OUTI
site 04FA9   ; OUTI
site 04FAB   ; OUTI
site 04FAD   ; OUTI
site 04FAF   ; OUTI
site 04FB1   ; OUTI
site 04FB3   ; OUTI
site 04FB5   ; OUTI
site 04FB7   ; OUTI
site 04FB9   ; OUTI
site 04FBB   ; OUTI
site 04FBD   ; OUTI
site 04FBF   ; OUTI
site 04FC1   ; OUTI
site 04FC3   ; OUTI
site 04FC5   ; OUTI
site 04FC7   ; OUTI
site 04FC9   ; OUTI
site 04FCB   ; OUTI
site 04FCD   ; OUTI
site 04FCF   ; OUTI
site 04FD1   ; OUTI
site 04FD3   ; OUTI
site 04FD5   ; OUTI
site 04FD7   ; OUTI
site 04FD9   ; OUTI
site 04FDB   ; OUTI
site 04FDD   ; OUTI
site 04FDF   ; OUTI
site 04FE1   ; OUTI
site 04FE3   ; OUTI
site 04FE5   ; OUTI
site 04FE7   ; OUTI
site 04FE9   ; OUTI
site 04FEB   ; OUTI
site 04FED   ; OUTI
site 04FEF   ; OUTI
site 04FF1   ; OUTI
site 04FF3   ; OUTI
site 04FF5   ; OUTI
site 04FF7   ; OUTI
site 04FF9   ; OUTI
site 04FFB   ; OUTI
site 04FFD   ; OUTI
site 04FFF   ; OUTI
site 05001   ; OUTI
site 05003   ; OUTI
site 05005   ; OUTI
site 05007   ; OUTI
site 05009   ; OUTI
site 0500B   ; OUTI
site 0500D   ; OUTI
site 0500F   ; OUTI
site 05011   ; OUTI
site 05013   ; OUTI
site 05015   ; OUTI
site 05017   ; OUTI
site 05019   ; OUTI
site 0501B   ; OUTI
site 0501D   ; OUTI
site 0501F   ; OUTI
site 05021   ; OUTI
site 05023   ; OUTI
site 05025   ; OUTI
site 05027   ; OUTI
site 05029   ; OUTI
site 0502B   ; OUTI
site 0502D   ; OUTI
site 0502F   ; OUTI
site 05031   ; OUTI
site 05033   ; OUTI
site 05035   ; OUTI
site 05037   ; OUTI
site 05039   ; OUTI
site 0503B   ; OUTI
site 0503D   ; OUTI
site 0503F   ; OUTI
site 05041   ; OUTI
site 05043   ; OUTI
site 05045   ; OUTI
site 05047   ; OUTI
site 05049   ; OUTI
site 0504B   ; OUTI
site 0504D   ; OUTI
site 0504F   ; OUTI
site 05051   ; OUTI
site 05053   ; OUTI
site 05055   ; OUTI
site 05057   ; OUTI
site 05059   ; OUTI
site 0505B   ; OUTI
site 0505D   ; OUTI
site 0505F   ; OUTI
site 05061   ; OUTI
site 05063   ; OUTI
site 05065   ; OUTI
site 05067   ; OUTI
site 05069   ; OUTI
site 0506B   ; OUTI
site 0506D   ; OUTI
site 0506F   ; OUTI
site 05071   ; OUTI
site 05073   ; OUTI
site 05075   ; OUTI
site 05077   ; OUTI
site 05079   ; OUTI
site 0507B   ; OUTI
site 0507D   ; OUTI
site 0507F   ; OUTI
site 05081   ; OUTI
site 05083   ; OUTI
site 05085   ; OUTI
site 05087   ; OUTI
site 05089   ; OUTI
site 0508B   ; OUTI
site 0508D   ; OUTI
site 0508F   ; OUTI
site 05091   ; OUTI
site 05093   ; OUTI
site 05095   ; OUTI
site 05097   ; OUTI
site 05099   ; OUTI
site 0509B   ; OUTI
site 0509D   ; OUTI
site 0509F   ; OUTI
site 050A1   ; OUTI
site 050A3   ; OUTI
site 050A5   ; OUTI
site 050A7   ; OUTI
site 050A9   ; OUTI
site 050AB   ; OUTI
site 050AD   ; OUTI
site 050AF   ; OUTI
site 050B1   ; OUTI
site 050B3   ; OUTI
site 050B5   ; OUTI
site 050B7   ; OUTI
site 050B9   ; OUTI
site 050BB   ; OUTI
site 050BD   ; OUTI
site 050BF   ; OUTI
site 050C1   ; OUTI
site 050C3   ; OUTI
site 050C5   ; OUTI
site 050C7   ; OUTI
site 050C9   ; OUTI
site 050CB   ; OUTI
site 050CD   ; OUTI
site 050CF   ; OUTI
site 050D1   ; OUTI
site 050D3   ; OUTI
site 050D5   ; OUTI
site 050D7   ; OUTI
site 050D9   ; OUTI
site 050DB   ; OUTI
site 050DD   ; OUTI
site 050DF   ; OUTI
site 050E1   ; OUTI
site 050E3   ; OUTI
site 050E5   ; OUTI
site 050E7   ; OUTI
site 050E9   ; OUTI
site 050EB   ; OUTI
site 050ED   ; OUTI
site 050EF   ; OUTI
site 050F1   ; OUTI
site 050F3   ; OUTI
site 050F5   ; OUTI
site 050F7   ; OUTI
site 050F9   ; OUTI
site 050FB   ; OUTI
site 050FD   ; OUTI
site 050FF   ; OUTI
site 05101   ; OUTI
site 05103   ; OUTI
site 05105   ; OUTI
site 05107   ; OUTI
site 05109   ; OUTI
site 0510B   ; OUTI
site 0510D   ; OUTI
site 0510F   ; OUTI
site 05111   ; OUTI
site 05113   ; OUTI
site 05115   ; OUTI
site 05117   ; OUTI
site 05119   ; OUTI
site 0511B   ; OUTI
site 0511D   ; OUTI
site 0511F   ; OUTI
site 05121   ; OUTI
site 05123   ; OUTI
site 05125   ; OUTI
site 05127   ; OUTI
site 05129   ; OUTI
site 0512B   ; OUTI
site 0512D   ; OUTI
site 0512F   ; OUTI
site 05131   ; OUTI
site 05133   ; OUTI
site 05135   ; OUTI
site 05137   ; OUTI
site 05139   ; OUTI
site 0513B   ; OUTI
site 0513D   ; OUTI
site 0513F   ; OUTI
site 05141   ; OUTI
site 05143   ; OUTI
site 05145   ; OUTI
site 05147   ; OUTI
site 05149   ; OUTI
site 0514B   ; OUTI
site 0514D   ; OUTI
site 0514F   ; OUTI
site 05151   ; OUTI
site 05153   ; OUTI
site 05155   ; OUTI
site 05157   ; OUTI
site 05159   ; OUTI
site 0515B   ; OUTI
site 0515D   ; OUTI
site 0515F   ; OUTI
site 05161   ; OUTI
site 05163   ; OUTI
site 05165   ; OUTI
site 05167   ; OUTI
site 05169   ; OUTI
site 0516B   ; OUTI
site 0516D   ; OUTI
site 0516F   ; OUTI
site 05171   ; OUTI
site 05173   ; OUTI
site 05175   ; OUTI
site 05177   ; OUTI
site 05179   ; OUTI
site 0517B   ; OUTI
site 0517D   ; OUTI
site 0517F   ; OUTI
site 05181   ; OUTI
site 05183   ; OUTI
site 05185   ; OUTI
site 05187   ; OUTI
site 05189   ; OUTI
site 0518B   ; OUTI
site 0518D   ; OUTI
site 0518F   ; OUTI
site 05191   ; OUTI
site 05193   ; OUTI
site 05195   ; OUTI
site 05197   ; OUTI
site 05199   ; OUTI
site 0519B   ; OUTI
site 0519D   ; OUTI
site 0519F   ; OUTI
site 051A1   ; OUTI
site 051A3   ; OUTI
site 051A5   ; OUTI
site 051A7   ; OUTI
site 051A9   ; OUTI
site 051AB   ; OUTI
site 051AD   ; OUTI
site 051AF   ; OUTI
site 051B1   ; OUTI
site 051B3   ; OUTI
site 051B5   ; OUTI
site 051B7   ; OUTI
site 051B9   ; OUTI
site 051BB   ; OUTI
site 051BD   ; OUTI
site 051BF   ; OUTI
site 051C1   ; OUTI
site 051C3   ; OUTI
site 051C5   ; OUTI
site 051C7   ; OUTI
site 051C9   ; OUTI
site 051CB   ; OUTI
site 051CD   ; OUTI
site 051CF   ; OUTI
site 051D1   ; OUTI
site 051D3   ; OUTI
site 051D5   ; OUTI
site 051D7   ; OUTI
site 051D9   ; OUTI
site 051DB   ; OUTI
site 051DD   ; OUTI
site 051DF   ; OUTI
site 051E1   ; OUTI
site 051E3   ; OUTI
site 051E5   ; OUTI
site 051E7   ; OUTI
site 051E9   ; OUTI
site 051EB   ; OUTI
site 051ED   ; OUTI
site 051EF   ; OUTI
site 051F1   ; OUTI
site 051F3   ; OUTI
site 051F5   ; OUTI
site 051F7   ; OUTI
site 051F9   ; OUTI
site 051FB   ; OUTI
site 051FD   ; OUTI
site 051FF   ; OUTI
site 05201   ; OUTI
site 05203   ; OUTI
site 05205   ; OUTI
site 05207   ; OUTI
site 05209   ; OUTI
site 0520B   ; OUTI
site 0520D   ; OUTI
site 0520F   ; OUTI
site 05211   ; OUTI
site 05213   ; OUTI
site 05215   ; OUTI
site 05217   ; OUTI
site 05219   ; OUTI
site 0521B   ; OUTI
site 0521D   ; OUTI
site 0521F   ; OUTI
site 05221   ; OUTI
site 05223   ; OUTI
site 05225   ; OUTI
site 05227   ; OUTI
site 05229   ; OUTI
site 0522B   ; OUTI
site 0522D   ; OUTI
site 0522F   ; OUTI
site 05231   ; OUTI
site 05233   ; OUTI
site 05235   ; OUTI
site 05237   ; OUTI
site 05239   ; OUTI
site 0523B   ; OUTI
site 0523D   ; OUTI
site 0523F   ; OUTI
site 05241   ; OUTI
site 05243   ; OUTI
site 05245   ; OUTI
site 05247   ; OUTI
site 05249   ; OUTI
site 0524B   ; OUTI
site 0524D   ; OUTI
site 0524F   ; OUTI
site 05251   ; OUTI
site 05253   ; OUTI
site 05255   ; OUTI
site 05257   ; OUTI
site 05259   ; OUTI
site 0525B   ; OUTI
site 0525D   ; OUTI
site 0525F   ; OUTI
site 05261   ; OUTI
site 05263   ; OUTI
site 05265   ; OUTI
site 0526D   ; OUTI
site 05287   ; OUT ($BF),A
site 0528B   ; OUT ($BF),A
site 05293   ; OTIR
site 05718   ; OUT ($BE),A
site 0571A   ; IN A,($BE)
site 05722   ; OUT ($BE),A
site 05724   ; IN A,($BE)
site 05E8A   ; OUT ($BF),A
site 05E8E   ; OUT ($BF),A
site 05E99   ; OUT ($BF),A
site 05E9D   ; OUT ($BF),A
site 05EA9   ; OUT ($BF),A
site 05EAD   ; OUT ($BF),A
site 08766   ; OUT ($F0),A
site 0876F   ; OUT ($F1),A
site 08797   ; OUT ($7F),A
site 087A7   ; OUT (C),D
site 087AD   ; OUT ($F1),A
site 087D7   ; OUT ($7F),A
site 087DB   ; OUT ($7F),A
site 087E0   ; OUT ($7F),A
site 0880D   ; OTIR
site 0881B   ; OTIR
site 08825   ; OUT ($F0),A
site 0882B   ; OUT ($F1),A
site 08837   ; OUTI
site 0883D   ; OUTI
site 089B1   ; OUT ($7F),A
site 089B5   ; OUT ($7F),A
site 089B9   ; OUT ($7F),A
site 08A49   ; OUT ($7F),A
site 08A4D   ; OUT ($7F),A
site 08A70   ; OUT ($7F),A
site 08A74   ; OUT ($7F),A
site 08A7D   ; OUT ($7F),A
site 08A81   ; OUT ($7F),A
site 08A84   ; OUT ($7F),A
site 08AEA   ; OUT ($F0),A
site 08AF1   ; OUT ($F1),A
site 08AF9   ; OUT ($F0),A
site 08AFF   ; OUT ($F1),A
site 08BF4   ; OUT ($F0),A
site 08BFE   ; OUT (C),L
site 08C07   ; OUT ($F0),A
site 08C22   ; OUT (C),H
site 08C2A   ; OUT ($F0),A
site 08C38   ; OUT ($F1),A
site 08C44   ; OUT ($F0),A
site 08C4D   ; OUT ($F1),A
site 08E02   ; OUT ($F0),A
site 08E0A   ; OUT (C),A
site 08E11   ; OUT ($F0),A
site 08E19   ; OUT (C),A
site 08E28   ; OUT ($F0),A
site 08E31   ; OUT (C),A
site 08E36   ; OUT ($F0),A
site 08E3C   ; OUTI
site 08EAD   ; OUT ($7F),A
site 08F78   ; OUT ($7F),A
site 08FA3   ; OUT ($7F),A
site 08FA7   ; OUT ($7F),A
site 08FB2   ; OUT ($7F),A
site 08FB7   ; OUT ($7F),A
site 08FE3   ; OUT ($F0),A
site 08FF1   ; OUT ($F1),A
site 09005   ; OUT (C),A
site 09010   ; OUT ($F0),A
site 09016   ; OUTI
site 09021   ; OUT ($F0),A
site 09035   ; OUT ($F0),A
site 090C9   ; OUTI
site 090CB   ; OUTI
site 090CD   ; OUTI
site 090CF   ; OUTI
site 090D1   ; OUTI
site 090D3   ; OUTI
site 090D5   ; OUTI
site 090D7   ; OUTI
site 090D9   ; OUTI
site 090DB   ; OUTI
site 090DD   ; OUTI
site 090E7   ; OUT (C),D
site 090ED   ; OUT ($F1),A
site 0912C   ; OUT ($7F),A
site 09182   ; OUT ($7F),A
site 091C1   ; OUT ($7F),A
site 09223   ; OUT ($7F),A
site 09243   ; OUT ($7F),A
site 09283   ; OUT ($7F),A
site 0928D   ; OUT ($7F),A
site 092D5   ; OUT ($7F),A
mapst 0009E   ; LD ($FFFF),A
mapst 000BA   ; LD ($FFFF),A
mapldk 000D0   # LD HL,$FFFC; LD (HL),$80
maphl 000D6   # LD (HL),$00, HL = $FFFD
maphl 000D9   # LD (HL),$01, HL = $FFFE
maphl 000DC   # LD (HL),$02, HL = $FFFF
mapst 00104   ; LD ($FFFF),A
mapst 0012C   ; LD ($FFFF),A
mapst 0015C   ; LD ($FFFF),A
mapst 001BD   ; LD ($FFFF),A
mapst 0025B   ; LD ($FFFF),A
mapst 007DE   ; LD ($FFFF),A
mapst 00958   ; LD ($FFFF),A
mapst 009F5   ; LD ($FFFF),A
mapst 00A16   ; LD ($FFFF),A
mapst 00A93   ; LD ($FFFF),A
mapst 00B76   ; LD ($FFFF),A
mapst 00F35   ; LD ($FFFF),A
mapst 010F3   ; LD ($FFFF),A
mapst 01AAA   ; LD ($FFFF),A
mapst 01C89   ; LD ($FFFF),A
mapst 01E0D   ; LD ($FFFF),A
mapst 01F4D   ; LD ($FFFF),A
mapst 01F8F   ; LD ($FFFF),A
mapst 02A0A   ; LD ($FFFF),A
mapst 02A3A   ; LD ($FFFF),A
mapst 02BF2   ; LD ($FFFF),A
mapst 03135   ; LD ($FFFF),A
mapst 0451F   ; LD ($FFFF),A
mapst 0453D   ; LD ($FFFF),A
mapst 04581   ; LD ($FFFF),A
mapst 045A3   ; LD ($FFFF),A
mapst 045C8   ; LD ($FFFF),A
mapst 045E1   ; LD ($FFFF),A
mapst 04782   ; LD ($FFFF),A
mapst 047BA   ; LD ($FFFF),A
mapst 047F3   ; LD ($FFFF),A
mapst 04816   ; LD ($FFFF),A
mapst 04830   ; LD ($FFFF),A
mapst 04852   ; LD ($FFFF),A
mapst 04869   ; LD ($FFFF),A
mapst 0488D   ; LD ($FFFF),A
mapst 048AF   ; LD ($FFFF),A
mapst 048BD   ; LD ($FFFF),A
mapst 048CB   ; LD ($FFFF),A
mapst 048E5   ; LD ($FFFF),A
mapst 048FF   ; LD ($FFFF),A
mapst 04919   ; LD ($FFFF),A
mapst 0493B   ; LD ($FFFF),A
mapst 04949   ; LD ($FFFF),A
mapst 0495F   ; LD ($FFFF),A
mapst 04979   ; LD ($FFFF),A
mapst 04990   ; LD ($FFFF),A
mapst 049A7   ; LD ($FFFF),A
mapst 04C10   ; LD ($FFFF),A
mapst 04D38   ; LD ($FFFF),A
mapst 05282   ; LD ($FFFF),A
mapst 05670   ; LD ($FFFF),A
mapst 0567E   ; LD ($FFFF),A
mapst 05BA3   ; LD ($FFFF),A
mapst 05BBD   ; LD ($FFFF),A
mapst 05BD1   ; LD ($FFFF),A
mapst 05C22   ; LD ($FFFF),A
mapst 05D04   ; LD ($FFFF),A
mapst 05EC9   ; LD ($FFFF),A
mapst 05ED0   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00811   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 0083D   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 07513   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 07524   # LD ($FFFF),A; after LD A,$09; 32 bytes of valid code before it
mapst 07801   # LD ($FFFF),A; after LD A,$09; 32 bytes of valid code before it
mapst 07D1B   # LD ($FFFF),A; after LD A,$08; 32 bytes of valid code before it
mapst 07E8D   # LD ($FFFF),A; after LD A,$03; 32 bytes of valid code before it
site 00907   ; OUT ($BE),A, in $0904, called by the text routine $07FC that no scanned path reaches

# Kenseiden (World) (Action Replay).cht and Kenseiden (USA, Europe, Brazil).cht, "Infinite
# Lives": RAM $C090 is the number of lives
poke "Infinite lives"
ar 00C0-9009
endpoke

# Kenseiden (World) (Action Replay).cht and Kenseiden (USA, Europe, Brazil).cht, "Infinite
# Health": RAM $C111 is the life bar, $14 when full
poke "Infinite health"
ar 00C1-1114
endpoke

# Kenseiden (USA, Europe, Brazil).cht, "Invincibility": the first of its three Game Genie
# codes ($5388, bank 1) is the whole effect; the other two have none alone
poke "Invincibility"
gg 183-88A-2AA
endpoke

# Kenseiden (USA, Europe, Brazil).cht, "Start with ?? Lives, instead of 2": the lives at the
# start of the game, set on the Pokes page
poke "Start lives"
gg ??0-34E-E62
endpoke
