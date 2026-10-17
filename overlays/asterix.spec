# Asterix (Europe, Brazil) (En,Fr) (Rev 1), CRC32 8C9D5BE8, 512K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of
# attract mode (30 minutes, no input) and play (10 minutes, start script and random input).
# Byte scan I/O patterns judged code and patched (no recording ran them):
#   $0100-$017E: the head of the unrolled OUTI block $0100-$05FF (640 OUTI, RET at $0600),
#     entered at a computed address; the recordings ran it from $0180 on.
#   $0688-$0690: name table row writer (RST $28 sets the address, OUTI; NOP; JP NZ, DE + $40).
#   $0B8F, $0B93 (V scroll set), $209E-$20A9, $390C-$390F (JR target from $38E8),
#   $3E11-$3E36 (two VRAM block copies after waits on $C062), $73AA-$73AC (name table fill),
#   $755D-$7561 (V scroll from a table).
#   Bank 14 $84B7, $84BB: the score digit writer at $8480 (a copy of bank 0's at $2906),
#     called from bank 1 $598D, $59B1 and $59C3 after LD A,$0E; LD ($FFFF),A at $5976.
# Byte scan I/O patterns judged not code (verdicts in data/scan-verdicts.tsv for the high and
# medium ones): $6734 is a word table; bank 15 $BA8A is the word table of the RST $08 at $BA88;
# the rest are in banks with no code (font and other graphics, maps, tables), and the low ones
# in banks 0, 1, 9 and 11 are operands of other instructions.
# The byte scan mapper stores in banks 0 and 1 are all code (LD A,n or LD A,($C07B) or
# LD A,($C1B5), then LD ($FFFF),A), and are patched. The two low ones ($15C4B, $35984) are data.
# $0012 JP (HL) is the end of RST $08, a jump through a table of words its callers pass in HL.
# The jumps into slot 2 at $2338, $298F, $29C6, $2C5A, $2C63 and $6D4B all run with bank 11
# there (the recordings saw only $0B written before each), and bank 11 is scanned.
name Asterix
cart 8C9D5BE8
hz 50		; No-Intro regions Europe, Brazil
# Play frames in the runtime: median 31% of a frame without tilecache, 25% with it (95th
# percentile 47% and 41%), and the level restart load is shorter with it too.
tilecache
# No priority: the game writes priority cells only for the "ASTERIX" panel that slides over
# the round picture before a level, and with priority on that panel shows the same, only slower.
# The status bar (lines 0-31) is a line interrupt split: the frame handler sets H scroll 0, the
# event at line 31 sets H = ($C018) for the play area. A rastercode routine cannot do it: with a
# RASTER table the game gets no line interrupts, and the play loop at $2A36 waits for the flag
# ($C062) that the line interrupt handler sets. hsplit moves the copper's map switch column with
# the line 31 write; without it a band on the right of the play area shows the wrong map columns
# once the view scrolls. Play: a median of 1,766 cycles a frame more in the runtime.
hsplit
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the runtime does DI and IM 2).
vector 00 io
start 0003
site 0002A   ; OUT ($BF),A
site 0002D   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0005C   ; OUT ($BF),A
site 0005F   ; OUT ($BF),A
site 00100   ; OUTI
site 00102   ; OUTI
site 00104   ; OUTI
site 00106   ; OUTI
site 00108   ; OUTI
site 0010A   ; OUTI
site 0010C   ; OUTI
site 0010E   ; OUTI
site 00110   ; OUTI
site 00112   ; OUTI
site 00114   ; OUTI
site 00116   ; OUTI
site 00118   ; OUTI
site 0011A   ; OUTI
site 0011C   ; OUTI
site 0011E   ; OUTI
site 00120   ; OUTI
site 00122   ; OUTI
site 00124   ; OUTI
site 00126   ; OUTI
site 00128   ; OUTI
site 0012A   ; OUTI
site 0012C   ; OUTI
site 0012E   ; OUTI
site 00130   ; OUTI
site 00132   ; OUTI
site 00134   ; OUTI
site 00136   ; OUTI
site 00138   ; OUTI
site 0013A   ; OUTI
site 0013C   ; OUTI
site 0013E   ; OUTI
site 00140   ; OUTI
site 00142   ; OUTI
site 00144   ; OUTI
site 00146   ; OUTI
site 00148   ; OUTI
site 0014A   ; OUTI
site 0014C   ; OUTI
site 0014E   ; OUTI
site 00150   ; OUTI
site 00152   ; OUTI
site 00154   ; OUTI
site 00156   ; OUTI
site 00158   ; OUTI
site 0015A   ; OUTI
site 0015C   ; OUTI
site 0015E   ; OUTI
site 00160   ; OUTI
site 00162   ; OUTI
site 00164   ; OUTI
site 00166   ; OUTI
site 00168   ; OUTI
site 0016A   ; OUTI
site 0016C   ; OUTI
site 0016E   ; OUTI
site 00170   ; OUTI
site 00172   ; OUTI
site 00174   ; OUTI
site 00176   ; OUTI
site 00178   ; OUTI
site 0017A   ; OUTI
site 0017C   ; OUTI
site 0017E   ; OUTI
site 00180   ; OUTI
site 00182   ; OUTI
site 00184   ; OUTI
site 00186   ; OUTI
site 00188   ; OUTI
site 0018A   ; OUTI
site 0018C   ; OUTI
site 0018E   ; OUTI
site 00190   ; OUTI
site 00192   ; OUTI
site 00194   ; OUTI
site 00196   ; OUTI
site 00198   ; OUTI
site 0019A   ; OUTI
site 0019C   ; OUTI
site 0019E   ; OUTI
site 001A0   ; OUTI
site 001A2   ; OUTI
site 001A4   ; OUTI
site 001A6   ; OUTI
site 001A8   ; OUTI
site 001AA   ; OUTI
site 001AC   ; OUTI
site 001AE   ; OUTI
site 001B0   ; OUTI
site 001B2   ; OUTI
site 001B4   ; OUTI
site 001B6   ; OUTI
site 001B8   ; OUTI
site 001BA   ; OUTI
site 001BC   ; OUTI
site 001BE   ; OUTI
site 001C0   ; OUTI
site 001C2   ; OUTI
site 001C4   ; OUTI
site 001C6   ; OUTI
site 001C8   ; OUTI
site 001CA   ; OUTI
site 001CC   ; OUTI
site 001CE   ; OUTI
site 001D0   ; OUTI
site 001D2   ; OUTI
site 001D4   ; OUTI
site 001D6   ; OUTI
site 001D8   ; OUTI
site 001DA   ; OUTI
site 001DC   ; OUTI
site 001DE   ; OUTI
site 001E0   ; OUTI
site 001E2   ; OUTI
site 001E4   ; OUTI
site 001E6   ; OUTI
site 001E8   ; OUTI
site 001EA   ; OUTI
site 001EC   ; OUTI
site 001EE   ; OUTI
site 001F0   ; OUTI
site 001F2   ; OUTI
site 001F4   ; OUTI
site 001F6   ; OUTI
site 001F8   ; OUTI
site 001FA   ; OUTI
site 001FC   ; OUTI
site 001FE   ; OUTI
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
site 0063A   ; OUT ($BE),A
site 0066A   ; OUTI
site 0067B   ; OUT ($BE),A
site 00680   ; OUT ($BE),A
site 0068D   ; OUTI
site 006A9   ; OUT ($BF),A
site 006AC   ; OUT ($BF),A
site 006BA   ; OUT ($BE),A
site 006C8   ; IN A,($DC)
site 006D7   ; IN A,($DC)
site 006DC   ; IN A,($DD)
site 006F8   ; IN A,($DD)
site 007E1   ; IN A,($BF)
site 007E3   ; IN A,($BF)
site 007EF   ; IN A,($BF)
site 0084B   ; IN A,($BF)
site 009EA   ; OUT ($BF),A
site 009EE   ; OUT ($BF),A
site 00AA8   ; OUT ($BF),A
site 00AAC   ; OUT ($BF),A
site 00AB2   ; OUTI
site 00AC2   ; OUT ($BF),A
site 00AC6   ; OUT ($BF),A
site 00AD1   ; OUT ($BF),A
site 00AD4   ; OUT ($BF),A
site 00ADD   ; OUT ($BF),A
site 00AE4   ; OUT ($BF),A
site 00AEB   ; OUT ($BF),A
site 00AEF   ; OUT ($BF),A
site 00AF3   ; OUT ($BF),A
site 00AF7   ; OUT ($BF),A
site 00AFD   ; OUT ($BF),A
site 00B01   ; OUT ($BF),A
site 00B0B   ; OUT ($BF),A
site 00B0F   ; OUT ($BF),A
site 00B3F   ; OUT ($BF),A
site 00B43   ; OUT ($BF),A
site 00B8F   ; OUT ($BF),A
site 00B93   ; OUT ($BF),A
site 00CA1   ; OUT ($BF),A
site 00CA4   ; OUT ($BF),A
site 00CA9   ; OUTI
site 00D53   ; OUTI
site 00D55   ; OUTI
site 01F91   ; OUT (C),L
site 01F96   ; OUT ($BF),A
site 01F9B   ; OUT ($BE),A
site 01F9F   ; OUT ($BE),A
site 0209E   ; OUT ($BF),A
site 020A2   ; OUT ($BF),A
site 020A9   ; OUTI
site 027BD   ; OUT ($BF),A
site 027C0   ; OUT ($BF),A
site 038CD   ; OUT ($BF),A
site 038D1   ; OUT ($BF),A
site 0390C   ; OUT ($BF),A
site 0390F   ; OUT ($BF),A
site 03E11   ; OUT ($BF),A
site 03E15   ; OUT ($BF),A
site 03E1A   ; OUTI
site 03E2E   ; OUT ($BF),A
site 03E32   ; OUT ($BF),A
site 03E36   ; OUTI
site 073AA   ; OUT (C),E
site 073AC   ; OUT ($BE),A
site 0755D   ; OUT ($BF),A
site 07561   ; OUT ($BF),A
site 081EB   ; OUT ($7F),A
site 08201   ; OUT ($7F),A
site 08214   ; OUT ($7F),A
site 0843B   ; OTIR
site 0855A   ; OUT ($7F),A
site 08564   ; OUT ($7F),A
site 08582   ; OUT ($7F),A
site 0868E   ; OUT ($7F),A
site 0871A   ; OUT ($7F),A
site 0879F   ; OUT ($7F),A
site 087B0   ; OUT ($7F),A
site 087D9   ; OUT ($7F),A
site 087DD   ; OUT ($7F),A
site 08813   ; OUT ($7F),A
site 08825   ; OUT ($7F),A
site 0883D   ; OUT ($7F),A
site 384B7   ; OUTI
site 384BB   ; OUTI
site 3F74D   ; IN A,($B7)
site 3F8E3   ; IN A,($80)
site 3F911   ; IN A,($80)
otir 027C8   ; OUTI
mapldk 00070   # LD HL,$FFFC; LD (HL),$80
maphl 00076   # LD (HL),$00, HL = $FFFD
maphl 00079   # LD (HL),$01, HL = $FFFE
maphl 0007C   # LD (HL),$02, HL = $FFFF
mapst 0009A   ; LD ($FFFF),A
mapst 0094A   ; LD ($FFFF),A
mapst 009C8   ; LD ($FFFF),A
mapst 00B27   ; LD ($FFFF),A
mapst 00B46   ; LD ($FFFF),A
mapst 00DB7   ; LD ($FFFF),A
mapst 00E43   ; LD ($FFFF),A
mapst 00E9C   ; LD ($FFFF),A
mapst 00EAA   ; LD ($FFFF),A
mapst 00EE8   ; LD ($FFFF),A
mapst 00F5C   ; LD ($FFFF),A
mapst 01B4C   ; LD ($FFFF),A
mapst 01B69   ; LD ($FFFF),A
mapst 01BCA   ; LD ($FFFF),A
mapst 01BE5   ; LD ($FFFF),A
mapst 01BF6   ; LD ($FFFF),A
mapst 01BFF   ; LD ($FFFF),A
mapst 01F2B   ; LD ($FFFF),A
mapst 02324   ; LD ($FFFF),A
mapst 02335   ; LD ($FFFF),A
mapst 0233D   ; LD ($FFFF),A
mapst 0235B   ; LD ($FFFF),A
mapst 02388   ; LD ($FFFF),A
mapst 023DE   ; LD ($FFFF),A
mapst 02490   ; LD ($FFFF),A
mapst 025CF   ; LD ($FFFF),A
mapst 0264B   ; LD ($FFFF),A
mapst 02777   ; LD ($FFFF),A
mapst 0288C   ; LD ($FFFF),A
mapst 028A5   ; LD ($FFFF),A
mapst 028BB   ; LD ($FFFF),A
mapst 028DD   ; LD ($FFFF),A
mapst 0290E   ; LD ($FFFF),A
mapst 02943   ; LD ($FFFF),A
mapst 0295A   ; LD ($FFFF),A
mapst 02968   ; LD ($FFFF),A
mapst 02976   ; LD ($FFFF),A
mapst 0298C   ; LD ($FFFF),A
mapst 029C3   ; LD ($FFFF),A
mapst 02B20   ; LD ($FFFF),A
mapst 02C54   ; LD ($FFFF),A
mapst 038C8   ; LD ($FFFF),A
mapst 03921   ; LD ($FFFF),A
mapst 03979   ; LD ($FFFF),A
mapst 039DC   ; LD ($FFFF),A
mapst 05637   ; LD ($FFFF),A
mapst 05BE7   ; LD ($FFFF),A
mapst 05D7C   ; LD ($FFFF),A
mapst 05DA4   ; LD ($FFFF),A
mapst 05DAB   ; LD ($FFFF),A
mapst 05E55   ; LD ($FFFF),A
mapst 05EED   ; LD ($FFFF),A
mapst 06D48   ; LD ($FFFF),A
mapst 07091   ; LD ($FFFF),A
mapst 070ED   ; LD ($FFFF),A
mapst 07211   ; LD ($FFFF),A
mapst 073D1   ; LD ($FFFF),A
mapst 073EC   ; LD ($FFFF),A
mapst 07519   ; LD ($FFFF),A
mapst 075D2   ; LD ($FFFF),A
mapst 075E2   ; LD ($FFFF),A
mapst 07663   ; LD ($FFFF),A
mapst 0768E   ; LD ($FFFF),A
mapst 0769C   ; LD ($FFFF),A
mapst 076CD   ; LD ($FFFF),A
mapst 079AF   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00A69   # LD ($FFFF),A; after LD A,$11; 32 bytes of valid code before it
mapst 00B63   # LD ($FFFF),A; after LD A,$07; 32 bytes of valid code before it
mapst 00BCB   # LD ($FFFF),A; after LD A,($C07B); 32 bytes of valid code before it
mapst 00BF9   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 00C4F   # LD ($FFFF),A; after LD A,$09; JP/CALL target from $64725 $6B098; 32 bytes of valid code before it
mapst 00C7F   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 00CC4   # LD ($FFFF),A; after LD A,$0E; JP/CALL target from $551DF $55437 $72CC1; 32 bytes of valid code before it
mapst 00D11   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 00D64   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 00D77   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 013B6   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 013C4   # LD ($FFFF),A; after LD A,$18; 32 bytes of valid code before it
mapst 013DB   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 0151F   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 0152D   # LD ($FFFF),A; after LD A,$18; 32 bytes of valid code before it
mapst 01544   # LD ($FFFF),A; after LD A,$16; 32 bytes of valid code before it
mapst 015F8   # LD ($FFFF),A; after LD A,$18; 32 bytes of valid code before it
mapst 0165E   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 01715   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 01725   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 01777   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 017A9   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 017CE   # LD ($FFFF),A; after LD A,$17; 32 bytes of valid code before it
mapst 017DC   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 021CF   # LD ($FFFF),A; after LD A,($C07B); JP/CALL target from $6BD81; 32 bytes of valid code before it
mapst 038E0   # LD ($FFFF),A; after LD A,$07; 32 bytes of valid code before it
mapst 03914   # LD ($FFFF),A; after LD A,($C1B5); 32 bytes of valid code before it
mapst 03DE5   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 03E65   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 03EB4   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 03EEA   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 056D4   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 0570E   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 05815   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 0584A   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 0585A   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 05868   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 05978   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 05F33   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 05F5D   # LD ($FFFF),A; after LD A,$0B; 32 bytes of valid code before it
mapst 05F87   # LD ($FFFF),A; after LD A,$10; 32 bytes of valid code before it
mapst 061AD   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 061CE   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 06A30   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 06A9D   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 06B2D   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 06BB6   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 0724C   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 075AE   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 07633   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
# Tile unpacker at $0625: the same routine, byte for byte, as Castle of Illusion's at $0172 (the
# Sega planar RLE decoder, with JR Z where the usual copy has RET Z), apart from the addresses of
# its CALL of the VRAM address routine ($005B here, the same 7 bytes as Castle's $0564) and of its
# jump back into the loop. It uses the library page rle_tiles, as Castle of Illusion does; this
# game's interrupt code does not write $FFFD either (the recordings saw $FFFD written only at $0076).
# Its OUT ($BE),A at $063A keeps its site line but is no longer reached.
asm 00625 5          ; LD B,4 : EX AF,AF' : LD A,B : EX AF,AF': the routine is rle_tiles
    rst $00
    db far_io, pg_rle_tiles, ent_rle_tiles
    ret
endasm
libpage 0 rle_tiles  ; overlays/lib/rle_tiles.asm
