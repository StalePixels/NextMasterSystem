# Land of Illusion Starring Mickey Mouse (Europe, Brazil) (En), CRC32 24E97200, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of attract mode
# (10 minutes, no input) and play (10 minutes, start script and random input).
name Land of Illusion Starring Mickey Mouse
cart 24E97200
hz 50		; No-Intro regions Europe, Brazil
# Play writes 27,315 name table cells with the priority bit (reference play log).
priority
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the runtime does DI and IM 2).
vector 00 io
start 0003
# The line interrupt handler ($0F0C) sets H scroll to 0 for the status bar (line 159 event) in
# play. Through the runtime that write lands about 2 lines late, and the top lines of the bar
# show the playfield's scroll; the routine gives the scroll of every line.
rastercode landofillusion-raster.asm
site 0002A   ; OUT ($BF),A
site 0002D   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0005C   ; OUT ($BF),A
site 0005F   ; OUT ($BF),A
site 00200   ; OUTI
site 00202   ; OUTI
site 00204   ; OUTI
site 00206   ; OUTI
site 00208   ; OUTI
site 0020A   ; OUTI
site 0020C   ; OUTI
site 0020E   ; OUTI
site 00210   ; OUTI
site 00212   ; OUTI
site 00214   ; OUTI
site 00216   ; OUTI
site 00218   ; OUTI
site 0021A   ; OUTI
site 0021C   ; OUTI
site 0021E   ; OUTI
site 00220   ; OUTI
site 00222   ; OUTI
site 00224   ; OUTI
site 00226   ; OUTI
site 00228   ; OUTI
site 0022A   ; OUTI
site 0022C   ; OUTI
site 0022E   ; OUTI
site 00230   ; OUTI
site 00232   ; OUTI
site 00234   ; OUTI
site 00236   ; OUTI
site 00238   ; OUTI
site 0023A   ; OUTI
site 0023C   ; OUTI
site 0023E   ; OUTI
site 00240   ; OUTI
site 00242   ; OUTI
site 00244   ; OUTI
site 00246   ; OUTI
site 00248   ; OUTI
site 0024A   ; OUTI
site 0024C   ; OUTI
site 0024E   ; OUTI
site 00250   ; OUTI
site 00252   ; OUTI
site 00254   ; OUTI
site 00256   ; OUTI
site 00258   ; OUTI
site 0025A   ; OUTI
site 0025C   ; OUTI
site 0025E   ; OUTI
site 00260   ; OUTI
site 00262   ; OUTI
site 00264   ; OUTI
site 00266   ; OUTI
site 00268   ; OUTI
site 0026A   ; OUTI
site 0026C   ; OUTI
site 0026E   ; OUTI
site 00270   ; OUTI
site 00272   ; OUTI
site 00274   ; OUTI
site 00276   ; OUTI
site 00278   ; OUTI
site 0027A   ; OUTI
site 0027C   ; OUTI
site 0027E   ; OUTI
site 00280   ; OUTI
site 00282   ; OUTI
site 00284   ; OUTI
site 00286   ; OUTI
site 00288   ; OUTI
site 0028A   ; OUTI
site 0028C   ; OUTI
site 0028E   ; OUTI
site 00290   ; OUTI
site 00292   ; OUTI
site 00294   ; OUTI
site 00296   ; OUTI
site 00298   ; OUTI
site 0029A   ; OUTI
site 0029C   ; OUTI
site 0029E   ; OUTI
site 002A0   ; OUTI
site 002A2   ; OUTI
site 002A4   ; OUTI
site 002A6   ; OUTI
site 002A8   ; OUTI
site 002AA   ; OUTI
site 002AC   ; OUTI
site 002AE   ; OUTI
site 002B0   ; OUTI
site 002B2   ; OUTI
site 002B4   ; OUTI
site 002B6   ; OUTI
site 002B8   ; OUTI
site 002BA   ; OUTI
site 002BC   ; OUTI
site 002BE   ; OUTI
site 002C0   ; OUTI
site 002C2   ; OUTI
site 002C4   ; OUTI
site 002C6   ; OUTI
site 002C8   ; OUTI
site 002CA   ; OUTI
site 002CC   ; OUTI
site 002CE   ; OUTI
site 002D0   ; OUTI
site 002D2   ; OUTI
site 002D4   ; OUTI
site 002D6   ; OUTI
site 002D8   ; OUTI
site 002DA   ; OUTI
site 002DC   ; OUTI
site 002DE   ; OUTI
site 002E0   ; OUTI
site 002E2   ; OUTI
site 002E4   ; OUTI
site 002E6   ; OUTI
site 002E8   ; OUTI
site 002EA   ; OUTI
site 002EC   ; OUTI
site 002EE   ; OUTI
site 002F0   ; OUTI
site 002F2   ; OUTI
site 002F4   ; OUTI
site 002F6   ; OUTI
site 002F8   ; OUTI
site 002FA   ; OUTI
site 002FC   ; OUTI
site 002FE   ; OUTI
site 00300   ; OUTI
site 00302   ; OUTI
site 00304   ; OUTI
site 00306   ; OUTI
site 00308   ; OUTI
site 0030A   ; OUTI
site 0030C   ; OUTI
site 0030E   ; OUTI
site 00310   ; OUTI
site 00312   ; OUTI
site 00314   ; OUTI
site 00316   ; OUTI
site 00318   ; OUTI
site 0031A   ; OUTI
site 0031C   ; OUTI
site 0031E   ; OUTI
site 00320   ; OUTI
site 00322   ; OUTI
site 00324   ; OUTI
site 00326   ; OUTI
site 00328   ; OUTI
site 0032A   ; OUTI
site 0032C   ; OUTI
site 0032E   ; OUTI
site 00330   ; OUTI
site 00332   ; OUTI
site 00334   ; OUTI
site 00336   ; OUTI
site 00338   ; OUTI
site 0033A   ; OUTI
site 0033C   ; OUTI
site 0033E   ; OUTI
site 00340   ; OUTI
site 00342   ; OUTI
site 00344   ; OUTI
site 00346   ; OUTI
site 00348   ; OUTI
site 0034A   ; OUTI
site 0034C   ; OUTI
site 0034E   ; OUTI
site 00350   ; OUTI
site 00352   ; OUTI
site 00354   ; OUTI
site 00356   ; OUTI
site 00358   ; OUTI
site 0035A   ; OUTI
site 0035C   ; OUTI
site 0035E   ; OUTI
site 00360   ; OUTI
site 00362   ; OUTI
site 00364   ; OUTI
site 00366   ; OUTI
site 00368   ; OUTI
site 0036A   ; OUTI
site 0036C   ; OUTI
site 0036E   ; OUTI
site 00370   ; OUTI
site 00372   ; OUTI
site 00374   ; OUTI
site 00376   ; OUTI
site 00378   ; OUTI
site 0037A   ; OUTI
site 0037C   ; OUTI
site 0037E   ; OUTI
site 00380   ; OUTI
site 00382   ; OUTI
site 00384   ; OUTI
site 00386   ; OUTI
site 00388   ; OUTI
site 0038A   ; OUTI
site 0038C   ; OUTI
site 0038E   ; OUTI
site 00390   ; OUTI
site 00392   ; OUTI
site 00394   ; OUTI
site 00396   ; OUTI
site 00398   ; OUTI
site 0039A   ; OUTI
site 0039C   ; OUTI
site 0039E   ; OUTI
site 003A0   ; OUTI
site 003A2   ; OUTI
site 003A4   ; OUTI
site 003A6   ; OUTI
site 003A8   ; OUTI
site 003AA   ; OUTI
site 003AC   ; OUTI
site 003AE   ; OUTI
site 003B0   ; OUTI
site 003B2   ; OUTI
site 003B4   ; OUTI
site 003B6   ; OUTI
site 003B8   ; OUTI
site 003BA   ; OUTI
site 003BC   ; OUTI
site 003BE   ; OUTI
site 003C0   ; OUTI
site 003C2   ; OUTI
site 003C4   ; OUTI
site 003C6   ; OUTI
site 003C8   ; OUTI
site 003CA   ; OUTI
site 003CC   ; OUTI
site 003CE   ; OUTI
site 003D0   ; OUTI
site 003D2   ; OUTI
site 003D4   ; OUTI
site 003D6   ; OUTI
site 003D8   ; OUTI
site 003DA   ; OUTI
site 003DC   ; OUTI
site 003DE   ; OUTI
site 003E0   ; OUTI
site 003E2   ; OUTI
site 003E4   ; OUTI
site 003E6   ; OUTI
site 003E8   ; OUTI
site 003EA   ; OUTI
site 003EC   ; OUTI
site 003EE   ; OUTI
site 003F0   ; OUTI
site 003F2   ; OUTI
site 003F4   ; OUTI
site 003F6   ; OUTI
site 003F8   ; OUTI
site 003FA   ; OUTI
site 003FC   ; OUTI
site 003FE   ; OUTI
site 00400   ; OUTI
site 00402   ; OUTI
site 00404   ; OUTI
site 00406   ; OUTI
site 00408   ; OUTI
site 0040A   ; OUTI
site 0040C   ; OUTI
site 0040E   ; OUTI
site 00410   ; OUTI
site 00412   ; OUTI
site 00414   ; OUTI
site 00416   ; OUTI
site 00418   ; OUTI
site 0041A   ; OUTI
site 0041C   ; OUTI
site 0041E   ; OUTI
site 00420   ; OUTI
site 00422   ; OUTI
site 00424   ; OUTI
site 00426   ; OUTI
site 00428   ; OUTI
site 0042A   ; OUTI
site 0042C   ; OUTI
site 0042E   ; OUTI
site 00430   ; OUTI
site 00432   ; OUTI
site 00434   ; OUTI
site 00436   ; OUTI
site 00438   ; OUTI
site 0043A   ; OUTI
site 0043C   ; OUTI
site 0043E   ; OUTI
site 00440   ; OUTI
site 00442   ; OUTI
site 00444   ; OUTI
site 00446   ; OUTI
site 00448   ; OUTI
site 0044A   ; OUTI
site 0044C   ; OUTI
site 0044E   ; OUTI
site 00450   ; OUTI
site 00452   ; OUTI
site 00454   ; OUTI
site 00456   ; OUTI
site 00458   ; OUTI
site 0045A   ; OUTI
site 0045C   ; OUTI
site 0045E   ; OUTI
site 00460   ; OUTI
site 00462   ; OUTI
site 00464   ; OUTI
site 00466   ; OUTI
site 00468   ; OUTI
site 0046A   ; OUTI
site 0046C   ; OUTI
site 0046E   ; OUTI
site 00470   ; OUTI
site 00472   ; OUTI
site 00474   ; OUTI
site 00476   ; OUTI
site 00478   ; OUTI
site 0047A   ; OUTI
site 0047C   ; OUTI
site 0047E   ; OUTI
site 00480   ; OUTI
site 00482   ; OUTI
site 00484   ; OUTI
site 00486   ; OUTI
site 00488   ; OUTI
site 0048A   ; OUTI
site 0048C   ; OUTI
site 0048E   ; OUTI
site 00490   ; OUTI
site 00492   ; OUTI
site 00494   ; OUTI
site 00496   ; OUTI
site 00498   ; OUTI
site 0049A   ; OUTI
site 0049C   ; OUTI
site 0049E   ; OUTI
site 004A0   ; OUTI
site 004A2   ; OUTI
site 004A4   ; OUTI
site 004A6   ; OUTI
site 004A8   ; OUTI
site 004AA   ; OUTI
site 004AC   ; OUTI
site 004AE   ; OUTI
site 004B0   ; OUTI
site 004B2   ; OUTI
site 004B4   ; OUTI
site 004B6   ; OUTI
site 004B8   ; OUTI
site 004BA   ; OUTI
site 004BC   ; OUTI
site 004BE   ; OUTI
site 004C0   ; OUTI
site 004C2   ; OUTI
site 004C4   ; OUTI
site 004C6   ; OUTI
site 004C8   ; OUTI
site 004CA   ; OUTI
site 004CC   ; OUTI
site 004CE   ; OUTI
site 004D0   ; OUTI
site 004D2   ; OUTI
site 004D4   ; OUTI
site 004D6   ; OUTI
site 004D8   ; OUTI
site 004DA   ; OUTI
site 004DC   ; OUTI
site 004DE   ; OUTI
site 004E0   ; OUTI
site 004E2   ; OUTI
site 004E4   ; OUTI
site 004E6   ; OUTI
site 004E8   ; OUTI
site 004EA   ; OUTI
site 004EC   ; OUTI
site 004EE   ; OUTI
site 004F0   ; OUTI
site 004F2   ; OUTI
site 004F4   ; OUTI
site 004F6   ; OUTI
site 004F8   ; OUTI
site 004FA   ; OUTI
site 004FC   ; OUTI
site 004FE   ; OUTI
site 00500   ; OUTI
site 00502   ; OUTI
site 00504   ; OUTI
site 00506   ; OUTI
site 00508   ; OUTI
site 0050A   ; OUTI
site 0050C   ; OUTI
site 0050E   ; OUTI
site 00510   ; OUTI
site 00512   ; OUTI
site 00514   ; OUTI
site 00516   ; OUTI
site 00518   ; OUTI
site 0051A   ; OUTI
site 0051C   ; OUTI
site 0051E   ; OUTI
site 00520   ; OUTI
site 00522   ; OUTI
site 00524   ; OUTI
site 00526   ; OUTI
site 00528   ; OUTI
site 0052A   ; OUTI
site 0052C   ; OUTI
site 0052E   ; OUTI
site 00530   ; OUTI
site 00532   ; OUTI
site 00534   ; OUTI
site 00536   ; OUTI
site 00538   ; OUTI
site 0053A   ; OUTI
site 0053C   ; OUTI
site 0053E   ; OUTI
site 00540   ; OUTI
site 00542   ; OUTI
site 00544   ; OUTI
site 00546   ; OUTI
site 00548   ; OUTI
site 0054A   ; OUTI
site 0054C   ; OUTI
site 0054E   ; OUTI
site 00550   ; OUTI
site 00552   ; OUTI
site 00554   ; OUTI
site 00556   ; OUTI
site 00558   ; OUTI
site 0055A   ; OUTI
site 0055C   ; OUTI
site 0055E   ; OUTI
site 00560   ; OUTI
site 00562   ; OUTI
site 00564   ; OUTI
site 00566   ; OUTI
site 00568   ; OUTI
site 0056A   ; OUTI
site 0056C   ; OUTI
site 0056E   ; OUTI
site 00570   ; OUTI
site 00572   ; OUTI
site 00574   ; OUTI
site 00576   ; OUTI
site 00578   ; OUTI
site 0057A   ; OUTI
site 0057C   ; OUTI
site 0057E   ; OUTI
site 00580   ; OUTI
site 00582   ; OUTI
site 00584   ; OUTI
site 00586   ; OUTI
site 00588   ; OUTI
site 0058A   ; OUTI
site 0058C   ; OUTI
site 0058E   ; OUTI
site 00590   ; OUTI
site 00592   ; OUTI
site 00594   ; OUTI
site 00596   ; OUTI
site 00598   ; OUTI
site 0059A   ; OUTI
site 0059C   ; OUTI
site 0059E   ; OUTI
site 005A0   ; OUTI
site 005A2   ; OUTI
site 005A4   ; OUTI
site 005A6   ; OUTI
site 005A8   ; OUTI
site 005AA   ; OUTI
site 005AC   ; OUTI
site 005AE   ; OUTI
site 005B0   ; OUTI
site 005B2   ; OUTI
site 005B4   ; OUTI
site 005B6   ; OUTI
site 005B8   ; OUTI
site 005BA   ; OUTI
site 005BC   ; OUTI
site 005BE   ; OUTI
site 005C0   ; OUTI
site 005C2   ; OUTI
site 005C4   ; OUTI
site 005C6   ; OUTI
site 005C8   ; OUTI
site 005CA   ; OUTI
site 005CC   ; OUTI
site 005CE   ; OUTI
site 005D0   ; OUTI
site 005D2   ; OUTI
site 005D4   ; OUTI
site 005D6   ; OUTI
site 005D8   ; OUTI
site 005DA   ; OUTI
site 005DC   ; OUTI
site 005DE   ; OUTI
site 005E0   ; OUTI
site 005E2   ; OUTI
site 005E4   ; OUTI
site 005E6   ; OUTI
site 005E8   ; OUTI
site 005EA   ; OUTI
site 005EC   ; OUTI
site 005EE   ; OUTI
site 005F0   ; OUTI
site 005F2   ; OUTI
site 005F4   ; OUTI
site 005F6   ; OUTI
site 005F8   ; OUTI
site 005FA   ; OUTI
site 005FC   ; OUTI
site 005FE   ; OUTI
site 00600   ; OUTI
site 00602   ; OUTI
site 00604   ; OUTI
site 00606   ; OUTI
site 00608   ; OUTI
site 0060A   ; OUTI
site 0060C   ; OUTI
site 0060E   ; OUTI
site 00610   ; OUTI
site 00612   ; OUTI
site 00614   ; OUTI
site 00616   ; OUTI
site 00618   ; OUTI
site 0061A   ; OUTI
site 0061C   ; OUTI
site 0061E   ; OUTI
site 00620   ; OUTI
site 00622   ; OUTI
site 00624   ; OUTI
site 00626   ; OUTI
site 00628   ; OUTI
site 0062A   ; OUTI
site 0062C   ; OUTI
site 0062E   ; OUTI
site 00630   ; OUTI
site 00632   ; OUTI
site 00634   ; OUTI
site 00636   ; OUTI
site 00638   ; OUTI
site 0063A   ; OUTI
site 0063C   ; OUTI
site 0063E   ; OUTI
site 00640   ; OUTI
site 00642   ; OUTI
site 00644   ; OUTI
site 00646   ; OUTI
site 00648   ; OUTI
site 0064A   ; OUTI
site 0064C   ; OUTI
site 0064E   ; OUTI
site 00650   ; OUTI
site 00652   ; OUTI
site 00654   ; OUTI
site 00656   ; OUTI
site 00658   ; OUTI
site 0065A   ; OUTI
site 0065C   ; OUTI
site 0065E   ; OUTI
site 00660   ; OUTI
site 00662   ; OUTI
site 00664   ; OUTI
site 00666   ; OUTI
site 00668   ; OUTI
site 0066A   ; OUTI
site 0066C   ; OUTI
site 0066E   ; OUTI
site 00670   ; OUTI
site 00672   ; OUTI
site 00674   ; OUTI
site 00676   ; OUTI
site 00678   ; OUTI
site 0067A   ; OUTI
site 0067C   ; OUTI
site 0067E   ; OUTI
site 00680   ; OUTI
site 00682   ; OUTI
site 00684   ; OUTI
site 00686   ; OUTI
site 00688   ; OUTI
site 0068A   ; OUTI
site 0068C   ; OUTI
site 0068E   ; OUTI
site 00690   ; OUTI
site 00692   ; OUTI
site 00694   ; OUTI
site 00696   ; OUTI
site 00698   ; OUTI
site 0069A   ; OUTI
site 0069C   ; OUTI
site 0069E   ; OUTI
site 006A0   ; OUTI
site 006A2   ; OUTI
site 006A4   ; OUTI
site 006A6   ; OUTI
site 006A8   ; OUTI
site 006AA   ; OUTI
site 006AC   ; OUTI
site 006AE   ; OUTI
site 006B0   ; OUTI
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
site 00736   ; OUT ($BE),A
site 00766   ; OUTI
site 00777   ; OUT ($BE),A
site 0077C   ; OUT ($BE),A
site 00789   ; OUTI
site 007A5   ; OUT ($BF),A
site 007A8   ; OUT ($BF),A
site 007B6   ; OUT ($BE),A
site 007C4   ; IN A,($DC)
site 007D3   ; IN A,($DC)
site 007D8   ; IN A,($DD)
site 007E6   ; IN A,($DD)
site 008E5   ; OUT (C),E
site 008E7   ; OUT (C),D
site 008E9   ; OUT ($BE),A
site 008F8   ; OUT (C),E
site 008FA   ; OUT (C),D
site 008FC   ; OUT ($BE),A
site 00908   ; OUT (C),E
site 0090A   ; OUT (C),D
site 00916   ; OUT ($BE),A
site 0093D   ; OUT (C),L
site 0093F   ; OUT (C),H
site 00944   ; IN A,($BE)
site 00948   ; OUT (C),E
site 0094A   ; OUT (C),D
site 0094C   ; OUT ($BE),A
site 0097D   ; IN A,($BF)
site 0097F   ; IN A,($BF)
site 0098B   ; IN A,($BF)
site 00C22   ; IN A,($BF)
site 00DBC   ; IN A,($BE)
site 00DC9   ; OUT ($BE),A
site 00E02   ; OUT ($BF),A
site 00E06   ; OUT ($BF),A
site 00EC8   ; OUT ($BF),A
site 00ECC   ; OUT ($BF),A
site 00ED3   ; OUT ($BF),A
site 00ED7   ; OUT ($BF),A
site 00EE1   ; OUT ($BF),A
site 00EE5   ; OUT ($BF),A
site 00EF2   ; OUT ($BF),A
site 00EF6   ; OUT ($BF),A
site 00F05   ; OUT ($BF),A
site 00F09   ; OUT ($BF),A
site 00F14   ; OUT ($BF),A
site 00F18   ; OUT ($BF),A
site 00F1F   ; OUT ($BF),A
site 00F23   ; OUT ($BF),A
site 00F32   ; OUT ($BF),A
site 00F36   ; OUT ($BF),A
site 00F42   ; OUT ($BF),A
site 00F46   ; OUT ($BF),A
site 00F66   ; OUT ($BF),A
site 00F6A   ; OUT ($BF),A
site 00F6F   ; OUTI
site 00F7F   ; OUT ($BF),A
site 00F83   ; OUT ($BF),A
site 00F8E   ; OUT ($BF),A
site 00F91   ; OUT ($BF),A
site 00FD7   ; OUT ($BF),A
site 00FDB   ; OUT ($BF),A
site 01042   ; OUT ($BF),A
site 01045   ; OUT ($BF),A
site 0104A   ; OUTI
site 01076   ; OUT ($BF),A
site 0107A   ; OUT ($BF),A
site 01309   ; OUTI
site 0130B   ; OUTI
site 0144D   ; OUT ($BF),A
site 01451   ; OUT ($BF),A
site 018C7   ; OUT ($BF),A
site 018CB   ; OUT ($BF),A
site 019B7   ; OUT ($BF),A
site 019BB   ; OUT ($BF),A
site 01C2F   ; OUT ($BF),A
site 01C33   ; OUT ($BF),A
site 01CD9   ; OUT ($BF),A
site 01CDD   ; OUT ($BF),A
site 01D7D   ; OUT ($BF),A
site 01D81   ; OUT ($BF),A
site 01F3F   ; OUT ($BF),A
site 01F43   ; OUT ($BF),A
site 020CF   ; OUT ($BF),A
site 020D3   ; OUT ($BF),A
site 0253A   ; OUT (C),L
site 0253F   ; OUT ($BF),A
site 02544   ; OUT ($BE),A
site 02548   ; OUT ($BE),A
site 026B2   ; OUT ($BF),A
site 026B6   ; OUT ($BF),A
site 026BD   ; OUTI
site 028D9   ; OUTI
site 05437   ; OUT ($BF),A
site 0543B   ; OUT ($BF),A
site 05592   ; OUT ($BF),A
site 05596   ; OUT ($BF),A
site 0594D   ; OUTI
site 05953   ; OUT (C),A
site 05DE5   ; OUT ($BF),A
site 05DE9   ; OUT ($BF),A
site 08204   ; OUT ($7F),A
site 0832A   ; OUT ($7F),A
site 084BC   ; OTIR
site 085D4   ; OUT ($7F),A
site 085DE   ; OUT ($7F),A
site 08609   ; OUT ($7F),A
site 0870D   ; OUT ($7F),A
site 08799   ; OUT ($7F),A
site 08834   ; OUT ($7F),A
site 0883D   ; OUT ($7F),A
site 0884D   ; OUT ($7F),A
site 088AC   ; OUT ($7F),A
site 088C9   ; OUT ($7F),A
mapldk 00070   # LD HL,$FFFC; LD (HL),$80
maphl 00076   # LD (HL),$00, HL = $FFFD
maphl 00079   # LD (HL),$01, HL = $FFFE
maphl 0007C   # LD (HL),$02, HL = $FFFF
mapst 0009A   ; LD ($FFFF),A
mapst 00D29   ; LD ($FFFF),A
mapst 00D9D   ; LD ($FFFF),A
mapst 00DE2   ; LD ($FFFF),A
mapst 00FAC   ; LD ($FFFF),A
mapst 00FBD   ; LD ($FFFF),A
mapst 00FD3   ; LD ($FFFF),A
mapst 01010   ; LD ($FFFF),A
mapst 01032   ; LD ($FFFF),A
mapst 01151   ; LD ($FFFF),A
mapst 011E5   ; LD ($FFFF),A
mapst 01210   ; LD ($FFFF),A
mapst 01287   ; LD ($FFFF),A
mapst 012D8   ; LD ($FFFF),A
mapst 01312   ; LD ($FFFF),A
mapst 013CF   ; LD ($FFFF),A
mapst 013F4   ; LD ($FFFF),A
mapst 0145A   ; LD ($FFFF),A
mapst 01540   ; LD ($FFFF),A
mapst 01550   ; LD ($FFFF),A
mapst 018D2   ; LD ($FFFF),A
mapst 019CB   ; LD ($FFFF),A
mapst 01A2A   ; LD ($FFFF),A
mapst 01AAE   ; LD ($FFFF),A
mapst 01AC9   ; LD ($FFFF),A
mapst 01B9E   ; LD ($FFFF),A
mapst 01C46   ; LD ($FFFF),A
mapst 01CE4   ; LD ($FFFF),A
mapst 01D8B   ; LD ($FFFF),A
mapst 01D9B   ; LD ($FFFF),A
mapst 01DB2   ; LD ($FFFF),A
mapst 01DCE   ; LD ($FFFF),A
mapst 01E00   ; LD ($FFFF),A
mapst 01E10   ; LD ($FFFF),A
mapst 01E72   ; LD ($FFFF),A
mapst 01E89   ; LD ($FFFF),A
mapst 0205A   ; LD ($FFFF),A
mapst 02184   ; LD ($FFFF),A
mapst 02269   ; LD ($FFFF),A
mapst 0228C   ; LD ($FFFF),A
mapst 024D8   ; LD ($FFFF),A
mapst 02791   ; LD ($FFFF),A
mapst 02B05   ; LD ($FFFF),A
mapst 02B6D   ; LD ($FFFF),A
mapst 02BC8   ; LD ($FFFF),A
mapst 02C80   ; LD ($FFFF),A
mapst 02CAD   ; LD ($FFFF),A
mapst 02D93   ; LD ($FFFF),A
mapst 02DE6   ; LD ($FFFF),A
mapst 02DEF   ; LD ($FFFF),A
mapst 03531   ; LD ($FFFF),A
mapst 044DC   ; LD ($FFFF),A
mapst 0450C   ; LD ($FFFF),A
mapst 04EFB   ; LD ($FFFF),A
mapst 05197   ; LD ($FFFF),A
mapst 051C2   ; LD ($FFFF),A
mapst 05268   ; LD ($FFFF),A
mapst 05298   ; LD ($FFFF),A
mapst 05370   ; LD ($FFFF),A
mapst 053A5   ; LD ($FFFF),A
mapst 0545B   ; LD ($FFFF),A
mapst 0559A   ; LD ($FFFF),A
mapst 05681   ; LD ($FFFF),A
mapst 056DE   ; LD ($FFFF),A
mapst 05730   ; LD ($FFFF),A
mapst 05809   ; LD ($FFFF),A
mapst 0596E   ; LD ($FFFF),A
mapst 0598A   ; LD ($FFFF),A
mapst 05A30   ; LD ($FFFF),A
mapst 05A71   ; LD ($FFFF),A
mapst 05AED   ; LD ($FFFF),A
mapst 05B1A   ; LD ($FFFF),A
mapst 05B31   ; LD ($FFFF),A
mapst 05C6F   ; LD ($FFFF),A
mapst 05C91   ; LD ($FFFF),A
mapst 05CC0   ; LD ($FFFF),A
mapst 05CE4   ; LD ($FFFF),A
mapst 05D06   ; LD ($FFFF),A
mapst 05D33   ; LD ($FFFF),A
mapst 05D68   ; LD ($FFFF),A
mapst 05DAB   ; LD ($FFFF),A
mapst 06198   ; LD ($FFFF),A
mapst 06245   ; LD ($FFFF),A
mapst 063D1   ; LD ($FFFF),A
mapst 07598   ; LD ($FFFF),A
mapst 0760B   ; LD ($FFFF),A
mapst 076E1   ; LD ($FFFF),A
mapst 07882   ; LD ($FFFF),A
mapst 07A81   ; LD ($FFFF),A
mapst 07AF1   ; LD ($FFFF),A
mapst 07B53   ; LD ($FFFF),A
mapst 07BF0   ; LD ($FFFF),A
mapst 07C0F   ; LD ($FFFF),A
mapst 07C23   ; LD ($FFFF),A
mapst 07C4B   ; LD ($FFFF),A
# $0FE7 RET jumps to the word at $C095, which $354E copies from a table: an entry into the
# unrolled OUTI runs at $0200-$02FF and $0600-$06FF (C = $BE). The play log runs them from $0280
# and in $0600-$06FF; every OUTI of both runs has a site line above.
# $0012 (JP (HL)) at $44E4, $4514 and $4EA8, $4F94 and the RST $08 at $6282 are object and
# table dispatchers; the code they reach runs no I/O in the reference logs.
# $009D CALL $84A0 runs with bank 2 in slot 2 (LD A,$02 before it): the sound driver.
# The stores into $0000-$BFFF and the calls into RAM at $89B3 and $89BB are in bytes of bank 2
# that a path reads as code; the path ends at an invalid opcode at $8AFD.
# Banks 30 and 31 hold object code run in slot 2 (the play log maps bank 30); the scanner does
# not reach it. Its byte scan I/O patterns are operands (LD HL,$B3ED at $7A2D7, LD HL,$A2ED at
# $7A2E8, JR at $7E3A2, DJNZ at $7E90A) and address tables ($7B3E3, $7D5AA).
# The other byte scan I/O patterns: $0B31 and $0B3E are in two CRAM routines nothing calls,
# $78CD is a word of the address table at $78CB, the rest are graphics and map data
# (data/scan-verdicts.tsv).
# Mapper stores found by the byte scan in bytes no path reached:
mapst 0564D   # LD ($FFFF),A; after LD A,$1C; 32 bytes of valid code before it
mapst 05BB0   # LD ($FFFF),A; after LD A,$1C; JP/CALL target from $5F25B; 32 bytes of valid code before it
mapst 065BA   # LD ($FFFF),A; after LD A,$15; 32 bytes of valid code before it
mapst 066D8   # LD ($FFFF),A; after LD A,$18; 32 bytes of valid code before it
mapst 066EB   # LD ($FFFF),A; after LD A,$15; 32 bytes of valid code before it
mapst 0686A   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 06878   # LD ($FFFF),A; after LD A,$16; 31 bytes of valid code before it
mapst 06CC0   # LD ($FFFF),A; after LD A,$15; 32 bytes of valid code before it
mapst 06F01   # LD ($FFFF),A; after LD A,$18; 32 bytes of valid code before it
mapst 06F0F   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 06F1D   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it

# Land of Illusion Starring Mickey Mouse (Europe) (Action Replay).cht, "Infinite Lives"
poke "Infinite lives"
ar 00C0-9F09
endpoke

# Land of Illusion Starring Mickey Mouse (Europe) (Action Replay).cht, "Infinite Circles (Hits)"
poke "Infinite power"
ar 00C0-9902
endpoke

# Land of Illusion Starring Mickey Mouse (Europe) (Action Replay).cht, "Infinite Time"
poke "Infinite time"
ar 00C0-A299
endpoke

# Land of Illusion Starring Mickey Mouse (Europe) (Action Replay).cht, "Infinite Air"
poke "Infinite air"
ar 00C0-AD07
endpoke

# Land of Illusion Starring Mickey Mouse (Europe, Brazil).cht, "Invincibility (blinking)"
poke "Invincibility"
ar 00C2-2601
endpoke

# Land of Illusion Starring Mickey Mouse (Europe, Brazil).cht, "High Jump"
poke "High jump"
ar 00C2-2AFF
endpoke

# Land of Illusion Starring Mickey Mouse (Europe, Brazil).cht, "Level Select [Replace ? With 0-C]"
poke "Start stage"
ar 00C0-B0??
endpoke

# Land of Illusion Starring Mickey Mouse (Europe, Brazil).cht, "Start with ?? Lives, instead of 03"
poke "Start lives"
gg ??E-0ED-E66
endpoke

# Land of Illusion Starring Mickey Mouse (Europe, Brazil).cht, "Start a new game with ?? health stars"
poke "Start power"
gg ??D-FFD-E62
endpoke
