# Prince of Persia (Europe, Brazil) (En), CRC32 7704287D, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log.
# Priority: the health arrows in row 0 (and about 440 cells of each name table) are priority tiles
# that cover the sprites of the gate column at x 32. The game flips register 2 between $3000 and
# $3800 once a game step; ntdiff writes only the cells that differ between the two tables, so
# Layer 2 is not rebuilt whole at each flip (without it, priority made play about 3 times slower).
# prichg: the "minutes left" text reuses tiles of the password screen under priority cells; a
# rewritten tile marks its cells, so Layer 2 draws them again from the new tile.
priority
ntdiff
prichg
name Prince of Persia
cart 7704287D
hz 50		; No-Intro regions Europe, Brazil
# $0008-$0017 are NOPs that RST $08 (from $44E9) slides through into the RST $18 bank switch,
# so no RST vector is free: $0000-$0002 (DI; IM 1) becomes the vector and the game starts at
# $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
# $1240 (OUT): inside the vcp patch at $123E, which replaces the whole routine
site 01247   ; OUT ($BF),A
site 01250   ; IN A,($BE)
site 0125B   ; OUT ($BF),A
site 01262   ; OUT ($BF),A
site 0126C   ; OUT ($BE),A
site 01FBB   ; OUT ($BF),A
site 01FC0   ; OUT ($BF),A
site 01FC8   ; OUT ($BE),A
site 02465   ; OUT ($BF),A
site 0246B   ; OUT ($BF),A
site 02472   ; OUT ($BE),A
site 0288E   ; OUT ($BF),A
site 02897   ; OUT ($BF),A
site 028A0   ; OUT ($BE),A
site 0373C   ; OUT ($BF),A
site 03740   ; OUT ($BF),A
site 03749   ; IN A,($BE)
site 03EF6   ; OUT ($BF),A
site 03EFD   ; OUT ($BF),A
site 03F06   ; IN A,($BE)
site 03F0F   ; IN A,($BE)
site 042A3   ; OUT ($BF),A
site 042AE   ; OUT ($BF),A
site 04363   ; OUT ($BF),A
site 04367   ; OUT ($BF),A
site 0439C   ; OUT ($BF),A
site 043A2   ; OUT ($BF),A
site 043A8   ; IN A,($BF)
site 0447A   ; IN A,($DD)
site 04509   ; OUT ($BF),A
site 0450E   ; OUT ($BF),A
site 04516   ; OUTI
site 0451A   ; OUTI
site 0451E   ; OUTI
site 04522   ; OUTI
site 04526   ; OUTI
site 0452A   ; OUTI
site 0452E   ; OUTI
site 04532   ; OUTI
site 04536   ; OUTI
site 0453A   ; OUTI
site 0453E   ; OUTI
site 04542   ; OUTI
site 04546   ; OUTI
site 0454A   ; OUTI
site 0454E   ; OUTI
site 04552   ; OUTI
site 04556   ; OUTI
site 0455A   ; OUTI
site 0455E   ; OUTI
site 04562   ; OUTI
site 04566   ; OUTI
site 0456A   ; OUTI
site 0456E   ; OUTI
site 04572   ; OUTI
site 04576   ; OUTI
site 0457A   ; OUTI
site 0457E   ; OUTI
site 04582   ; OUTI
site 04586   ; OUTI
site 0458A   ; OUTI
site 0458E   ; OUTI
site 04592   ; OUTI
site 045DE   ; OUT ($BF),A
site 045E3   ; OUT ($BF),A
site 045F0   ; OUT ($BE),A
site 045F5   ; OUT ($BE),A
site 045FA   ; OUT ($BE),A
site 045FF   ; OUT ($BE),A
site 04604   ; OUT ($BE),A
site 04609   ; OUT ($BE),A
site 0460E   ; OUT ($BE),A
site 04613   ; OUT ($BE),A
site 04618   ; OUT ($BE),A
site 0461D   ; OUT ($BE),A
site 04622   ; OUT ($BE),A
site 04627   ; OUT ($BE),A
site 0462C   ; OUT ($BE),A
site 04631   ; OUT ($BE),A
site 04636   ; OUT ($BE),A
site 0463B   ; OUT ($BE),A
site 04640   ; OUT ($BE),A
site 04645   ; OUT ($BE),A
site 0464A   ; OUT ($BE),A
site 0464F   ; OUT ($BE),A
site 04654   ; OUT ($BE),A
site 04659   ; OUT ($BE),A
site 0465E   ; OUT ($BE),A
site 04663   ; OUT ($BE),A
site 04668   ; OUT ($BE),A
site 0466D   ; OUT ($BE),A
site 04672   ; OUT ($BE),A
site 04677   ; OUT ($BE),A
site 0467C   ; OUT ($BE),A
site 04681   ; OUT ($BE),A
site 04686   ; OUT ($BE),A
site 0468B   ; OUT ($BE),A
site 04696   ; OUT ($BE),A
site 0469B   ; OUT ($BE),A
site 046A0   ; OUT ($BE),A
site 046A5   ; OUT ($BE),A
site 046AA   ; OUT ($BE),A
site 046AF   ; OUT ($BE),A
site 046B4   ; OUT ($BE),A
site 046B9   ; OUT ($BE),A
site 046BE   ; OUT ($BE),A
site 046C3   ; OUT ($BE),A
site 046C8   ; OUT ($BE),A
site 046CD   ; OUT ($BE),A
site 046D2   ; OUT ($BE),A
site 046D7   ; OUT ($BE),A
site 046DC   ; OUT ($BE),A
site 046E1   ; OUT ($BE),A
site 046E6   ; OUT ($BE),A
site 046EB   ; OUT ($BE),A
site 046F0   ; OUT ($BE),A
site 046F5   ; OUT ($BE),A
site 046FA   ; OUT ($BE),A
site 046FF   ; OUT ($BE),A
site 04704   ; OUT ($BE),A
site 04709   ; OUT ($BE),A
site 0470E   ; OUT ($BE),A
site 04713   ; OUT ($BE),A
site 04718   ; OUT ($BE),A
site 0471D   ; OUT ($BE),A
site 04722   ; OUT ($BE),A
site 04727   ; OUT ($BE),A
site 0472C   ; OUT ($BE),A
site 04731   ; OUT ($BE),A
site 04778   ; OUT ($BF),A
site 0477D   ; OUT ($BF),A
site 0478D   ; OUT ($BE),A
site 04792   ; OUT ($BE),A
site 04797   ; OUT ($BE),A
site 0479C   ; OUT ($BE),A
site 047A1   ; OUT ($BE),A
site 047A6   ; OUT ($BE),A
site 047AB   ; OUT ($BE),A
site 047B0   ; OUT ($BE),A
site 047B5   ; OUT ($BE),A
site 047BA   ; OUT ($BE),A
site 047BF   ; OUT ($BE),A
site 047C4   ; OUT ($BE),A
site 047C9   ; OUT ($BE),A
site 047CE   ; OUT ($BE),A
site 047D3   ; OUT ($BE),A
site 047D8   ; OUT ($BE),A
site 047DD   ; OUT ($BE),A
site 047E2   ; OUT ($BE),A
site 047E7   ; OUT ($BE),A
site 047EC   ; OUT ($BE),A
site 047F1   ; OUT ($BE),A
site 047F6   ; OUT ($BE),A
site 047FB   ; OUT ($BE),A
site 04800   ; OUT ($BE),A
site 04805   ; OUT ($BE),A
site 0480A   ; OUT ($BE),A
site 0480F   ; OUT ($BE),A
site 04814   ; OUT ($BE),A
site 04819   ; OUT ($BE),A
site 0481E   ; OUT ($BE),A
site 04823   ; OUT ($BE),A
site 04828   ; OUT ($BE),A
site 04833   ; OUT ($BE),A
site 04838   ; OUT ($BE),A
site 0483D   ; OUT ($BE),A
site 04842   ; OUT ($BE),A
site 04847   ; OUT ($BE),A
site 0484C   ; OUT ($BE),A
site 04851   ; OUT ($BE),A
site 04856   ; OUT ($BE),A
site 0485B   ; OUT ($BE),A
site 04860   ; OUT ($BE),A
site 04865   ; OUT ($BE),A
site 0486A   ; OUT ($BE),A
site 0486F   ; OUT ($BE),A
site 04874   ; OUT ($BE),A
site 04879   ; OUT ($BE),A
site 0487E   ; OUT ($BE),A
site 04883   ; OUT ($BE),A
site 04888   ; OUT ($BE),A
site 0488D   ; OUT ($BE),A
site 04892   ; OUT ($BE),A
site 04897   ; OUT ($BE),A
site 0489C   ; OUT ($BE),A
site 048A1   ; OUT ($BE),A
site 048A6   ; OUT ($BE),A
site 048AB   ; OUT ($BE),A
site 048B0   ; OUT ($BE),A
site 048B5   ; OUT ($BE),A
site 048BA   ; OUT ($BE),A
site 048BF   ; OUT ($BE),A
site 048C4   ; OUT ($BE),A
site 048C9   ; OUT ($BE),A
site 048CE   ; OUT ($BE),A
site 04960   ; OUT ($BF),A
site 04963   ; OUT ($BF),A
site 04971   ; OUT ($BE),A
site 04980   ; OUT ($BE),A
site 049C6   ; OUT ($BF),A
site 049C9   ; OUT ($BF),A
site 049CF   ; IN A,($BE)
site 049D5   ; IN A,($BE)
site 049F5   ; OUT ($BF),A
site 049F8   ; OUT ($BF),A
site 049FF   ; OUT ($BE),A
site 04A07   ; OUT ($BE),A
site 04B6B   ; OUT ($BF),A
site 04B70   ; OUT ($BF),A
site 04B87   ; OUT ($BE),A
site 04B8E   ; OUT ($BE),A
site 04B97   ; OUT ($BE),A
site 04B9E   ; OUT ($BE),A
site 04BA8   ; OUT ($BF),A
site 04BAD   ; OUT ($BF),A
site 04BB7   ; OUT ($BE),A
site 04BBE   ; OUT ($BE),A
site 04BC7   ; OUT ($BE),A
site 04BCE   ; OUT ($BE),A
site 04BEF   ; OUT ($BF),A
site 04BF4   ; OUT ($BF),A
site 04C0F   ; OUT ($BE),A
site 04C16   ; OUT ($BE),A
site 04C1F   ; OUT ($BE),A
site 04C26   ; OUT ($BE),A
site 04D30   ; OUT ($BF),A
site 04D35   ; OUT ($BF),A
site 04D47   ; OUT ($BE),A
site 04D4E   ; OUT ($BE),A
site 04D55   ; OUT ($BE),A
site 04D5D   ; OUT ($BE),A
site 04D6A   ; OUT ($BF),A
site 04D6F   ; OUT ($BF),A
site 04D76   ; OUT ($BE),A
site 04D7D   ; OUT ($BE),A
site 04D84   ; OUT ($BE),A
site 04D8B   ; OUT ($BE),A
site 04E7B   ; OUT ($BF),A
site 04E80   ; OUT ($BF),A
site 04E9C   ; OUT ($BE),A
site 04EA4   ; OUT ($BE),A
site 04EB5   ; OUT ($BF),A
site 04EB9   ; OUT ($BF),A
site 04EBC   ; OUT ($BE),A
site 04EC5   ; OUT ($BF),A
site 04EC9   ; OUT ($BF),A
site 04ECC   ; OUT ($BE),A
site 04ED6   ; OUT ($BF),A
site 04EDA   ; OUT ($BF),A
site 04EDD   ; OUT ($BE),A
site 04EF0   ; OUT ($BF),A
site 04EF4   ; OUT ($BF),A
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
site 04F66   ; OUT ($BF),A
site 04F6A   ; OUT ($BF),A
site 04F6C   ; OUTI
site 04F6E   ; OUT (C),E
site 04F71   ; OUTI
site 04F73   ; OUT (C),E
site 04F76   ; OUTI
site 04F78   ; OUT (C),E
site 04F7B   ; OUTI
site 04F7D   ; OUT (C),E
site 04F80   ; OUTI
site 04F82   ; OUT (C),E
site 04F85   ; OUTI
site 04F87   ; OUT (C),E
site 04F8A   ; OUTI
site 04F8C   ; OUT (C),E
site 04F8F   ; OUTI
site 04F91   ; OUT (C),E
site 04F94   ; OUTI
site 04F96   ; OUT (C),E
site 04F99   ; OUTI
site 04F9B   ; OUT (C),E
site 04F9E   ; OUTI
site 04FA0   ; OUT (C),E
site 04FA3   ; OUTI
site 04FA5   ; OUT (C),E
site 04FA8   ; OUTI
site 04FAA   ; OUT (C),E
site 04FAD   ; OUTI
site 04FAF   ; OUT (C),E
site 04FB2   ; OUTI
site 04FB4   ; OUT (C),E
site 04FB7   ; OUTI
site 04FB9   ; OUT (C),E
site 04FBC   ; OUTI
site 04FBE   ; OUT (C),E
site 04FC1   ; OUTI
site 04FC3   ; OUT (C),E
site 04FC6   ; OUTI
site 04FC8   ; OUT (C),E
site 04FCB   ; OUTI
site 04FCD   ; OUT (C),E
site 04FD0   ; OUTI
site 04FD2   ; OUT (C),E
site 04FD5   ; OUTI
site 04FD7   ; OUT (C),E
site 04FDA   ; OUTI
site 04FDC   ; OUT (C),E
site 04FDF   ; OUTI
site 04FE1   ; OUT (C),E
site 04FE4   ; OUTI
site 04FE6   ; OUT (C),E
site 04FE9   ; OUTI
site 04FEB   ; OUT (C),E
site 04FEE   ; OUTI
site 04FF0   ; OUT (C),E
site 04FF3   ; OUTI
site 04FF5   ; OUT (C),E
site 04FF8   ; OUTI
site 04FFA   ; OUT (C),E
site 04FFD   ; OUTI
site 04FFF   ; OUT (C),E
site 05002   ; OUTI
site 05004   ; OUT (C),E
site 05007   ; OUTI
site 05009   ; OUT (C),E
site 0500C   ; OUTI
site 0500E   ; OUT (C),E
site 05011   ; OUTI
site 05013   ; OUT (C),E
site 05016   ; OUTI
site 05018   ; OUT (C),E
site 0501B   ; OUTI
site 0501D   ; OUT (C),E
site 05020   ; OUTI
site 05022   ; OUT (C),E
site 05025   ; OUTI
site 05027   ; OUT (C),E
site 0502A   ; OUTI
site 0502C   ; OUT (C),E
site 0502F   ; OUTI
site 05031   ; OUT (C),E
site 05034   ; OUTI
site 05036   ; OUT (C),E
site 05039   ; OUTI
site 0503B   ; OUT (C),E
site 0503E   ; OUTI
site 05040   ; OUT (C),E
site 05043   ; OUTI
site 05045   ; OUT (C),E
site 05048   ; OUTI
site 0504A   ; OUT (C),E
site 0504D   ; OUTI
site 0504F   ; OUT (C),E
site 05052   ; OUTI
site 05054   ; OUT (C),E
site 05057   ; OUTI
site 05059   ; OUT (C),E
site 05060   ; OUT ($BF),A
site 05064   ; OUT ($BF),A
site 05068   ; OUT ($BE),A
# $5408, $540E, $5415 (OUT): inside the u54 patch at $5403, which replaces the whole loop
site 0542B   ; OUT ($BF),A
site 05431   ; OUT ($BF),A
site 05438   ; OUT ($BE),A
site 05466   ; OUT ($BF),A
site 0546C   ; OUT ($BF),A
site 05474   ; OUTI
site 05476   ; OUTI
site 05478   ; OUTI
site 0547A   ; OUTI
site 05483   ; OUT ($BF),A
site 05486   ; OUT ($BF),A
site 05488   ; OUTI
site 0548A   ; OUTI
site 0548C   ; OUTI
site 0548E   ; OUTI
site 054A9   ; OUT ($BF),A
site 054AE   ; OUT ($BF),A
site 054B6   ; OUTI
site 054B8   ; OUTI
site 054BA   ; OUTI
site 054BC   ; OUTI
site 054BE   ; OUTI
site 054C0   ; OUTI
site 054C2   ; OUTI
site 054C4   ; OUTI
site 054C6   ; OUTI
site 054C8   ; OUTI
site 054CA   ; OUTI
site 054CC   ; OUTI
site 054CE   ; OUTI
site 054D0   ; OUTI
site 054D2   ; OUTI
site 054D4   ; OUTI
site 054D6   ; OUTI
site 054D8   ; OUTI
site 054DA   ; OUTI
site 054DC   ; OUTI
site 054DE   ; OUTI
site 054E0   ; OUTI
site 054E2   ; OUTI
site 054E4   ; OUTI
site 054E6   ; OUTI
site 054E8   ; OUTI
site 054EA   ; OUTI
site 054EC   ; OUTI
site 054EE   ; OUTI
site 054F0   ; OUTI
site 054F2   ; OUTI
site 054F4   ; OUTI
site 054F6   ; OUTI
site 054F8   ; OUTI
site 054FA   ; OUTI
site 054FC   ; OUTI
site 054FE   ; OUTI
site 05500   ; OUTI
site 05502   ; OUTI
site 05504   ; OUTI
site 05506   ; OUTI
site 05508   ; OUTI
site 0550A   ; OUTI
site 0550C   ; OUTI
site 0550E   ; OUTI
site 05510   ; OUTI
site 05512   ; OUTI
site 05514   ; OUTI
site 05516   ; OUTI
site 05518   ; OUTI
site 0551A   ; OUTI
site 0551C   ; OUTI
site 0551E   ; OUTI
site 05520   ; OUTI
site 05522   ; OUTI
site 05524   ; OUTI
site 05526   ; OUTI
site 05528   ; OUTI
site 0552A   ; OUTI
site 0552C   ; OUTI
site 0552E   ; OUTI
site 05530   ; OUTI
site 05532   ; OUTI
site 05534   ; OUTI
site 05536   ; OUTI
site 05538   ; OUTI
site 0553A   ; OUTI
site 0553C   ; OUTI
site 0553E   ; OUTI
site 05540   ; OUTI
site 05542   ; OUTI
site 05544   ; OUTI
site 05546   ; OUTI
site 05548   ; OUTI
site 0554A   ; OUTI
site 0554C   ; OUTI
site 0554E   ; OUTI
site 05550   ; OUTI
site 05552   ; OUTI
site 05554   ; OUTI
site 05556   ; OUTI
site 05558   ; OUTI
site 0555A   ; OUTI
site 0555C   ; OUTI
site 0555E   ; OUTI
site 05560   ; OUTI
site 05562   ; OUTI
site 05564   ; OUTI
site 05566   ; OUTI
site 05568   ; OUTI
site 0556A   ; OUTI
site 0556C   ; OUTI
site 0556E   ; OUTI
site 05570   ; OUTI
site 05572   ; OUTI
site 05574   ; OUTI
site 05576   ; OUTI
site 05578   ; OUTI
site 0557A   ; OUTI
site 0557C   ; OUTI
site 0557E   ; OUTI
site 05580   ; OUTI
site 05582   ; OUTI
site 05584   ; OUTI
site 05586   ; OUTI
site 05588   ; OUTI
site 0558A   ; OUTI
site 0558C   ; OUTI
site 0558E   ; OUTI
site 05590   ; OUTI
site 05592   ; OUTI
site 05594   ; OUTI
site 05596   ; OUTI
site 05598   ; OUTI
site 0559A   ; OUTI
site 0559C   ; OUTI
site 0559E   ; OUTI
site 055A0   ; OUTI
site 055A2   ; OUTI
site 055A4   ; OUTI
site 055A6   ; OUTI
site 055A8   ; OUTI
site 055AA   ; OUTI
site 055AC   ; OUTI
site 055AE   ; OUTI
site 055B0   ; OUTI
site 055B2   ; OUTI
site 055B4   ; OUTI
site 055B6   ; OUTI
site 055B8   ; OUTI
site 055BA   ; OUTI
site 055BC   ; OUTI
site 055BE   ; OUTI
site 055C0   ; OUTI
site 055C2   ; OUTI
site 055C4   ; OUTI
site 055C6   ; OUTI
site 055C8   ; OUTI
site 055CA   ; OUTI
site 055CC   ; OUTI
site 055CE   ; OUTI
site 055D0   ; OUTI
site 055D2   ; OUTI
site 055D4   ; OUTI
site 055D6   ; OUTI
site 055D8   ; OUTI
site 055DA   ; OUTI
site 055DC   ; OUTI
site 055DE   ; OUTI
site 055E0   ; OUTI
site 055E2   ; OUTI
site 055E4   ; OUTI
site 055E6   ; OUTI
site 055E8   ; OUTI
site 055EA   ; OUTI
site 055EC   ; OUTI
site 055EE   ; OUTI
site 055F0   ; OUTI
site 055F2   ; OUTI
site 055F4   ; OUTI
site 055F6   ; OUTI
site 055F8   ; OUTI
site 055FA   ; OUTI
site 055FC   ; OUTI
site 055FE   ; OUTI
site 05600   ; OUTI
site 05602   ; OUTI
site 05604   ; OUTI
site 05606   ; OUTI
site 05608   ; OUTI
site 0560A   ; OUTI
site 0560C   ; OUTI
site 0560E   ; OUTI
site 05610   ; OUTI
site 05612   ; OUTI
site 05614   ; OUTI
site 05616   ; OUTI
site 05618   ; OUTI
site 0561A   ; OUTI
site 0561C   ; OUTI
site 0561E   ; OUTI
site 05620   ; OUTI
site 05622   ; OUTI
site 05624   ; OUTI
site 05626   ; OUTI
site 05628   ; OUTI
site 0562A   ; OUTI
site 0562C   ; OUTI
site 0562E   ; OUTI
site 05630   ; OUTI
site 05632   ; OUTI
site 05634   ; OUTI
site 05693   ; OUT ($BF),A
site 05698   ; OUT ($BF),A
site 0569E   ; OUT ($BE),A
site 056A4   ; OUT ($BE),A
site 056AA   ; OUT ($BE),A
site 056B0   ; OUT ($BE),A
site 056B6   ; OUT ($BE),A
site 056BC   ; OUT ($BE),A
site 056C7   ; OUT ($BF),A
site 056CC   ; OUT ($BF),A
site 056D2   ; OUT ($BE),A
site 056D8   ; OUT ($BE),A
site 056DE   ; OUT ($BE),A
site 056E4   ; OUT ($BE),A
site 056EA   ; OUT ($BE),A
site 056F0   ; OUT ($BE),A
site 05744   ; OUT ($BF),A
site 0574C   ; OUT ($BF),A
site 05754   ; IN A,($BE)
site 05759   ; IN A,($BE)
site 05761   ; IN A,($BE)
site 05767   ; IN A,($BE)
site 05770   ; OUT ($BF),A
site 05773   ; OUT ($BF),A
site 05779   ; IN A,($BE)
site 0577F   ; IN A,($BE)
site 05787   ; IN A,($BE)
site 0578D   ; IN A,($BE)
site 05797   ; OUT (C),E
site 0579E   ; OUT (C),D
site 057B2   ; OUT (C),A
site 057B8   ; OUT (C),A
site 057BD   ; OUT (C),L
site 057C2   ; OUT (C),H
site 057CC   ; OUT (C),A
site 057D2   ; OUT (C),A
site 057D7   ; OUT (C),L
site 057DC   ; OUT (C),H
site 057E6   ; OUT (C),A
site 057EC   ; OUT (C),A
site 057F1   ; OUT (C),L
site 057F6   ; OUT (C),H
site 05800   ; OUT (C),A
site 05806   ; OUT (C),A
site 0580B   ; OUT (C),L
site 05810   ; OUT (C),H
site 0581A   ; OUT (C),A
site 05820   ; OUT (C),A
site 05825   ; OUT (C),L
site 0582A   ; OUT (C),H
site 05834   ; OUT (C),A
site 0583A   ; OUT (C),A
site 0583F   ; OUT (C),L
site 05844   ; OUT (C),H
site 0584E   ; OUT (C),E
site 05853   ; OUT (C),D
site 0586A   ; OUT (C),A
site 05870   ; OUT (C),A
site 05875   ; OUT (C),L
site 0587A   ; OUT (C),H
site 05888   ; OUT (C),A
site 0588E   ; OUT (C),A
site 05893   ; OUT (C),L
site 05898   ; OUT (C),H
site 058A6   ; OUT (C),A
site 058AC   ; OUT (C),A
site 058B1   ; OUT (C),L
site 058B6   ; OUT (C),H
site 058C4   ; OUT (C),A
site 058CA   ; OUT (C),A
site 058CF   ; OUT (C),L
site 058D4   ; OUT (C),H
site 05900   ; OUT ($BF),A
site 05903   ; OUT ($BF),A
site 0590A   ; IN A,($BE)
site 05936   ; OUT ($BF),A
site 05939   ; OUT ($BF),A
site 05940   ; IN A,($BE)
site 0598C   ; OUT ($BF),A
site 0598F   ; OUT ($BF),A
site 059AC   ; OUT ($BE),A
site 059B4   ; OUT ($BE),A
site 059BC   ; OUT ($BE),A
site 059C4   ; OUT ($BE),A
site 059CC   ; OUT ($BE),A
site 059D1   ; OUT ($BE),A
site 059D6   ; OUT ($BE),A
site 059DB   ; OUT ($BE),A
site 059E7   ; OUT ($BE),A
site 059EF   ; OUT ($BE),A
site 059F7   ; OUT ($BE),A
site 059FF   ; OUT ($BE),A
site 05A07   ; OUT ($BE),A
site 05A0C   ; OUT ($BE),A
site 05A11   ; OUT ($BE),A
site 05A16   ; OUT ($BE),A
site 05AE0   ; OUT ($BF),A
site 05AE5   ; OUT ($BF),A
site 05AE8   ; OUT (C),L
site 05AED   ; OUT (C),H
site 05AF2   ; OUT (C),L
site 05AF7   ; OUT (C),H
site 05AFC   ; OUT (C),L
site 05B01   ; OUT (C),H
site 05B06   ; OUT (C),L
site 05B0B   ; OUT (C),H
site 05B16   ; OUT (C),E
site 05B1B   ; OUT (C),D
site 05B1E   ; OUT (C),L
site 05B23   ; OUT (C),H
site 05B28   ; OUT (C),L
site 05B2D   ; OUT (C),H
site 05B32   ; OUT (C),L
site 05B37   ; OUT (C),H
site 05B3C   ; OUT (C),L
site 05B41   ; OUT (C),H
site 05B4C   ; OUT (C),E
site 05B51   ; OUT (C),D
site 05B54   ; OUT (C),L
site 05B59   ; OUT (C),H
site 05B5E   ; OUT (C),L
site 05B63   ; OUT (C),H
site 05B68   ; OUT (C),L
site 05B6D   ; OUT (C),H
site 05B72   ; OUT (C),L
site 05B77   ; OUT (C),H
site 05B82   ; OUT (C),E
site 05B87   ; OUT (C),D
site 05B8A   ; OUT (C),L
site 05B8F   ; OUT (C),H
site 05B94   ; OUT (C),L
site 05B99   ; OUT (C),H
site 05B9E   ; OUT (C),L
site 05BA3   ; OUT (C),H
site 05BA8   ; OUT (C),L
site 05BAD   ; OUT (C),H
site 05BB8   ; OUT (C),E
site 05BBD   ; OUT (C),D
site 05BC0   ; OUT (C),L
site 05BC5   ; OUT (C),H
site 05BCA   ; OUT (C),L
site 05BCF   ; OUT (C),H
site 05BD4   ; OUT (C),L
site 05BD9   ; OUT (C),H
site 05BDE   ; OUT (C),L
site 05BE3   ; OUT (C),H
site 05BEE   ; OUT (C),E
site 05BF3   ; OUT (C),D
site 05C04   ; OUT (C),L
site 05C0A   ; OUT (C),H
site 05C18   ; OUT (C),A
site 05C1F   ; OUT (C),A
site 05C26   ; OUT (C),A
site 05C2D   ; OUT (C),A
site 05C34   ; OUT (C),A
site 05C3B   ; OUT (C),A
site 05C42   ; OUT (C),A
site 05C49   ; OUT (C),A
site 05C50   ; OUT (C),A
site 05EF9   ; OUT ($BF),A
site 05EFE   ; OUT ($BF),A
site 05F13   ; OUT ($BE),A
site 05F1B   ; OUT ($BE),A
site 05F93   ; OUT ($BF),A
site 05F96   ; OUT ($BF),A
site 05F9B   ; IN A,($BE)
site 05FA3   ; OUT ($BF),A
site 05FA8   ; OUT ($BF),A
site 05FAE   ; OUT ($BE),A
site 060FB   ; OUT ($BF),A
site 060FE   ; OUT ($BF),A
site 06104   ; OUT ($BE),A
site 0610F   ; OUT ($BF),A
site 06114   ; OUT ($BF),A
site 0611A   ; OUT ($BE),A
site 0612C   ; OUT ($BF),A
site 0612F   ; OUT ($BF),A
site 06135   ; OUT ($BE),A
site 06140   ; OUT ($BF),A
site 06145   ; OUT ($BF),A
site 0614B   ; OUT ($BE),A
site 0F721   ; OUT ($BF),A
site 0F726   ; OUT ($BF),A
site 0F72D   ; OUT ($BE),A
site 0F733   ; OUT ($BF),A
site 0F73A   ; OUT ($BF),A
site 0F746   ; OUT ($BF),A
site 0F74D   ; OUT ($BF),A
site 0F764   ; OUT ($BF),A
site 0F76B   ; OUT ($BF),A
site 0F793   ; OUT ($BE),A
site 0FA3C   ; OUT ($BF),A
site 0FA40   ; OUT ($BF),A
site 0FA46   ; OUT ($BE),A
site 0FA4B   ; OUT ($BE),A
site 0FA4E   ; OUT ($BE),A
site 0FA53   ; OUT ($BE),A
site 0FA56   ; OUT ($BE),A
site 0FA5B   ; OUT ($BE),A
site 0FA5E   ; OUT ($BE),A
site 0FA63   ; OUT ($BE),A
site 0FA66   ; OUT ($BE),A
site 0FA6B   ; OUT ($BE),A
site 0FA6E   ; OUT ($BE),A
site 0FA73   ; OUT ($BE),A
site 0FA83   ; OUT ($BF),A
site 0FA87   ; OUT ($BF),A
site 0FA8C   ; OUT ($BE),A
site 0FA91   ; OUT ($BE),A
site 0FA94   ; OUT ($BE),A
site 0FA99   ; OUT ($BE),A
site 0FA9C   ; OUT ($BE),A
site 0FAA1   ; OUT ($BE),A
site 0FAA4   ; OUT ($BE),A
site 0FAA9   ; OUT ($BE),A
site 0FB8B   ; OUT ($BF),A
site 0FB97   ; OUT ($BF),A
site 0FBAD   ; OUT (C),E
site 0FBB3   ; OUT (C),D
site 0FBC4   ; OUT (C),L
site 0FBC9   ; OUT (C),H
site 0FBDA   ; OUT (C),A
site 0FBE0   ; OUT (C),A
site 0FC00   ; OUT ($BF),A
site 0FC05   ; OUT ($BF),A
site 0FC0D   ; OUT ($BE),A
site 0FC12   ; OUT ($BE),A
site 0FC2F   ; OUT ($BF),A
site 0FC34   ; OUT ($BF),A
site 0FC3C   ; OUT ($BE),A
site 0FC41   ; OUT ($BE),A
site 0FC93   ; OUT ($BF),A
site 0FC9A   ; OUT ($BF),A
site 0FCDD   ; OUT ($BE),A
# $FD4D-$FD5E (bank 3 $BD4D-$BD5E, OUT): inside the nfill patch at $BD4C
site 0FD6F   ; OUT ($BF),A
site 0FD74   ; OUT ($BF),A
site 0FD7A   ; OUT ($BE),A
site 0FD80   ; OUT ($BE),A
site 0FD92   ; IN A,($DC)
site 0FD9D   ; OUT ($DE),A
site 0FD9F   ; IN A,($DC)
site 0FDA4   ; OUT ($DE),A
site 0FDA6   ; IN A,($DC)
site 0FDB0   ; OUT ($DE),A
site 0FDB2   ; IN A,($DC)
site 0FDBC   ; OUT ($DE),A
site 0FDBE   ; IN A,($DC)
site 0FDC8   ; OUT ($DE),A
site 0FDCA   ; IN A,($DC)
site 0FDD4   ; OUT ($DE),A
site 0FDD6   ; IN A,($DC)
site 0FDF2   ; IN A,($DC)
site 0FDF5   ; IN A,($DD)
site 0FE06   ; OUT ($DE),A
site 0FE08   ; IN A,($DC)
site 0FE0B   ; IN A,($DD)
site 0FE16   ; OUT ($DE),A
site 0FE18   ; IN A,($DC)
site 0FE28   ; OUT ($DE),A
site 0FE2A   ; IN A,($DC)
site 0FE34   ; OUT ($DE),A
site 0FE36   ; IN A,($DC)
site 0FE40   ; OUT ($DE),A
site 0FE42   ; IN A,($DD)
site 0FE4C   ; OUT ($DE),A
site 0FE4E   ; IN A,($DD)
site 0FE60   ; OUT ($DF),A
site 0FE64   ; OUT ($DE),A
site 0FE66   ; IN A,($DE)
site 0FE72   ; OUT ($DE),A
site 0FE74   ; IN A,($DE)
site 0FE84   ; OUT ($DE),A
site 0FE88   ; OUT ($DF),A
site 2932D   ; OUT ($7F),A
site 29331   ; OUT ($7F),A
site 2933E   ; OUT ($7F),A
site 29342   ; OUT ($7F),A
site 29373   ; OUT ($7F),A
site 2938A   ; OUT ($7F),A
site 2939E   ; OUT ($7F),A
site 293AD   ; OUT ($7F),A
site 293C4   ; OUT ($7F),A
site 293D8   ; OUT ($7F),A
site 29405   ; OUT ($7F),A
site 29418   ; OUT ($7F),A
site 2942F   ; OUT ($7F),A
site 29435   ; OUT ($7F),A
site 29459   ; OUT ($7F),A
site 29470   ; OUT ($7F),A
site 29484   ; OUT ($7F),A
site 294E1   ; OUT ($7F),A
site 296DD   ; OUT ($7F),A
site 296E2   ; OUT ($7F),A
site 296F6   ; OUT ($7F),A
site 29709   ; OUT ($7F),A
site 29715   ; OUT ($7F),A
site 29728   ; OUT ($7F),A
# The RST $18 bank switch (PUSH AF; LD A,E; LD ($FFFF),A; POP AF; RET, about 40 calls a game step,
# also from the frame handler) runs natively in a cave: it does what the runtime's mapper store does
# (cold_mapper in fw2.asm, then map_bank in fw.asm): $FFFF and its RAM copy $DFFF get the bank,
# and slots 4 and 5 get the cart pages CART_PAGE + 2 * (bank mod 16), in cur_mmu and in NextRegs
# $54 and $55 (256K cart: 32 pages). With $FFFC bit 3 set (cart RAM in slot 2) only the registers
# change, as map_bank does. Through the trap each call cost about 1,800 cycles. $FFFF is written
# first: a frame handler that comes in the middle reads it, switches and switches back to it.
# Runtime internals used: CART_PAGE 32 (memplan.inc); cur_mmu $E02D is a public state variable.
label cv_rst18 074D0
asm 00018 7   ; PUSH AF; LD A,E; LD ($FFFF),A; POP AF; RET
    jp cv_rst18
endasm
asm 074D0 40
    push af
    ld a,e
    ld ($FFFF),a
    ld ($DFFF),a
    ld a,($FFFC)
    and 8
    jr nz,cv_rst18_x
    ld a,e
    and $0F
    add a,a
    add a,32
    ld (cur_mmu+4),a
    db $ED,$92,$54            ; nextreg $54,a
    inc a
    ld (cur_mmu+5),a
    db $ED,$92,$55            ; nextreg $55,a
cv_rst18_x:
    pop af
    ret
endasm
mapst 00096   ; LD ($FFFC),A
mapst 00119   ; LD ($FFFC),A
mapst 0011C   ; LD ($FFFD),A
mapst 00120   ; LD ($FFFE),A
mapst 00124   ; LD ($FFFF),A
mapst 03658   ; LD ($FFFF),A
mapst 00071   # LD ($FFFC),A; after LD A,$28; 32 bytes of valid code before it
mapst 00083   # LD ($FFFC),A; after LD A,($FFFB); JP/CALL target from $087CE $23B23; 32 bytes of valid code before it
mapst 00089   # LD ($FFFC),A; after LD A,$28; 32 bytes of valid code before it
mapst 00090   # LD ($FFFC),A; after LD A,($FFFB); 31 bytes of valid code before it
mapst 0009A   # LD ($FFFD),A; after another mapper store, LD ($FFFC),A at $00096; 32 bytes of valid code before it
mapst 000A0   # LD ($FFFC),A; after LD A,($FFFB); JP/CALL target from $0E6D4; 32 bytes of valid code before it
mapst 000B5   # LD ($FFFC),A; after LD A,$28; 32 bytes of valid code before it
# HALTs. Every HALT the game runs waits for one frame (or counts frames in a fade), so each is
# patched: EI; HALT pairs with eihalt, the others through code caves. The caves sit in the zero
# padding at the end of bank 1 ($6D1F-$7507, slot 1 is always bank 1), 16 bytes apart. Where the
# byte after a HALT is a branch target (1EB4 from $1ED5, 1F81 from $2073) the cave takes the
# instructions before the HALT instead; $5F8D is a HALT between a RET and a branch target
# ($5F8E from $5FB2), so its two callers call the cave.
eihalt 020DF
eihalt 020E1
eihalt 02103
eihalt 02172
eihalt 0217A
eihalt 021DE
eihalt 048D6
label cv_1eb0 07400
label cv_1f7d 07410
label cv_224b 07420
label cv_22fd 07430
label cv_243d 07440
label cv_4ee2 07450
label cv_5425 07460
label cv_5f8d 07470
label cv_bc8b 07480
label cv_bce4 07490
label cv_bd49 074A0
label cv_bd6a 074B0
label cv_b75d 074C0
asm 01EB0 4   ; CALL $53C3; HALT
    jp cv_1eb0
endasm
asm 07400 16
    call $53C3
    rst $00
    db halt_io
    jp $1EB4
endasm
asm 01F7D 4   ; LD E,$02; RST $18; HALT
    jp cv_1f7d
endasm
asm 07410 16
    ld e,$02
    rst $18
    rst $00
    db halt_io
    jp $1F81
endasm
asm 0224B 3   ; HALT; LD E,$02
    jp cv_224b
endasm
asm 07420 16
    rst $00
    db halt_io
    ld e,$02
    jp $224E
endasm
asm 022FD 5   ; HALT; XOR A; LD ($C265),A
    jp cv_22fd
endasm
asm 07430 16
    rst $00
    db halt_io
    xor a
    ld ($C265),a
    jp $2302
endasm
asm 0243D 4   ; HALT; CALL $5EC7
    jp cv_243d
endasm
asm 07440 16
    rst $00
    db halt_io
    call $5EC7
    jp $2441
endasm
asm 04EE2 5   ; HALT; DI; LD A,($C24F)  (entry $4EE2)
    jp cv_4ee2
endasm
asm 07450 16
    rst $00
    db halt_io
    di
    ld a,($C24F)
    jp $4EE7
endasm
asm 05425 4   ; HALT; LD HL,($CF07)  (entry $5425)
    jp cv_5425
endasm
asm 07460 16
    rst $00
    db halt_io
    ld hl,($CF07)
    jp $5429
endasm
asm 05F62 3   ; CALL $5F8D
    call cv_5f8d
endasm
asm 05F6A 3   ; CALL $5F8D
    call cv_5f8d
endasm
asm 07470 16
    rst $00
    db halt_io
    jp $5F8E
endasm
asm 0FC8B 3   ; HALT; HALT; PUSH HL
    jp cv_bc8b
endasm
asm 07480 16
    rst $00
    db halt_io
    rst $00
    db halt_io
    push hl
    jp $BC8E
endasm
asm 0FCE4 5   ; LD B,$05; HALT; DJNZ $BCE6
    jp cv_bce4
endasm
asm 07490 16
    ld b,$05
cv_bce4_l:
    rst $00
    db halt_io
    djnz cv_bce4_l
    jp $BCE9
endasm
asm 0FD49 3   ; LD E,$80; HALT  (entry $BD49)
    jp cv_bd49
endasm
asm 074A0 16
    ld e,$80
    rst $00
    db halt_io
    jp $BD4C
endasm
asm 0FD6A 3   ; HALT; LD E,$80  (entry $BD6A)
    jp cv_bd6a
endasm
asm 074B0 16
    rst $00
    db halt_io
    ld e,$80
    jp $BD6D
endasm
asm 0F75D 6   ; six HALTs: one fade step every 6 frames (entry $B75D)
    jp cv_b75d
endasm
asm 074C0 16
    rept 6
    rst $00
    db halt_io
    endr
    jp $B763
endasm
# Name table segment copy, bank 3 $BA28-$BAB6 (called from $235C once a game step). The list at
# $C3xx holds 6-byte entries; each gives two VRAM control words, (IX+0,1) for a run of 12 bytes and
# (IX+2,3) for a run of 8, copied from the name table shadow at ((D OR 8)+$4F)*256+E, the source
# low byte stepping with INC C only (it wraps inside its 256-byte page). Page 0 writes each run with
# one jt_vwrite call.
# The game's caller restores its slot 2 bank from A' after the call, and the loop leaves A' = the
# last byte written, so the page leaves the same A' (and the other registers as the loop leaves them).
asm 045D2 5   ; DI; LD E,C; LD C,$BE; EXX
    rst $00
    db far_io, pg_tw_plain, ent_tw_plain
    ret
endasm
asm 0476F 5   ; DI; EXX; LD H,$79; LD L,A
    rst $00
    db far_io, pg_tw_mirror, ent_tw_mirror
    ret
endasm
# Screen name table writer, bank 1 $4D20-$4DA3 (from $4D03, for the title, password, options and
# "minutes left" screens): 192 blocks of 2 x 2 cells, one map byte each (HL), each block 8 bytes
# from the metatile table at ($C25A) + 8 * byte, rows of 16 blocks from $3800. Through the traps
# it cost about 3.5 million cycles a screen (8 frames at 60 Hz) against about one frame on the
# Master System. Page 0 ntb builds the 24 rows in its own buffer and writes only the cells that
# differ from the VRAM copy, then the last cell, so the VDP ends as the game's writes leave it.
asm 04D20 7   ; LD IX,($C244); LD BC,$0000
    rst $00
    db far_io, pg_ntb, ent_ntb
    jp $4DA4                ; LD E,$02; RST $18; LD A,$0F; LD ($C2DB),A; RET
endasm
# VRAM tile copy, bank 1 $5403-$541F (bank 11 $AF94, $760 bytes = 59 tiles to $2D00, interrupts
# on): page 0 u54 writes the tiles that differ from the VRAM copy (vcw). Through the traps it cost
# about 800,000 cycles.
asm 05403 29  ; LD HL,$AF94; ... the OUT ($BE) loop to $541F
    rst $00
    db far_io, pg_u54, ent_u54
    jp $5420
endasm
# Level name table writer, bank 1 $4B62-$4BE1 (from $499D with BC = $0100): as $4D20, rows 1-24,
# and $4DAD for each block. Page 0 ntl, as ntb; $4DAD runs natively from the page.
asm 04B62 7   ; LD A,$C0; DI; EX AF,AF'; PUSH BC; CALL $4334 (first byte)
    rst $00
    db far_io, pg_ntl, ent_ntl
    jp $4BE2                ; LD E,$02; RST $18; RET
endasm
# Name table clear, bank 3 $BD4C-$BD69 (after the HALT at $BD4B, cave cv_bd49): $380 cells of
# ($80, 0) from $3800, interrupts on. Through the traps it cost about 2.1 million cycles at the
# level start. Page 1 nfill writes only the cells that differ from the VRAM copy, then the last.
asm 0FD4C 6   ; XOR A; OUT ($BF),A; LD A,$78 (first byte)
    rst $00
    db far_io, pg_nfill, ent_nfill
    ret
endasm
# Tile upload, bank 1 $4500 (entry $44F4 falls into it): A = the slot, whose VRAM address is at
# $7900 + A (low) and $7A00 + A (high), C = tiles (0 = 256), HL = source; 32 OUTIs a tile with
# interrupts off. Each screen load sends 174 tiles this way; through the traps that took about
# 130 ms against 48 ms on the Master System. Page 0 upl writes them with one jt_vwrite.
asm 04500 5   ; DI; EXX; LD H,$79; LD L,A
    rst $00
    db far_io, pg_upl, ent_upl
    ret
endasm
# Text printer, bank 1 $4E67 (IX = record: column, row, then characters; $0D starts the next row at
# the same column, 0 ends). Each character is a name table cell, tile $148 + character, priority on.
# The game prints its screens' texts again on every pass of their loops (the "minutes left" screen:
# about 60 cells every 3 frames), and through the traps each cell write cost about 5,500 cycles and
# marked its cell for Layer 2: the loop took 5 frames a pass against 3 on the Master System, so the
# screen's fade-in and its countdown ran late. Page 0 txt writes only the cells whose value differs
# from the VRAM copy, with jt_vwrite, and always the last cell of the last row, so the VDP is left as
# the game's writes leave it. When the record ends just after a $0D, the game's last access is the
# control word of the new row: txt returns with carry set and DE = that address, and the cave writes
# it through the traps, as the game would. The cave keeps the game's bank switches (RST $18).
label cv_txt 07300
label cv_txt_t 07304
label cv_txt2 07320
asm 04E67 7   ; DI; LD E,$0B; RST $18; LD A,(IX+0)
    di
    ld e,$0B
    rst $18
    jp cv_txt
endasm
asm 07300 20
    rst $00
    db far_io, pg_txt, ent_txt
    jr nc,cv_txt_x          ; (cv_txt_t)
    ld a,e
    rst $00
    db $05                  ; OUT ($BF),A
    ld a,d
    or $40
    rst $00
    db $05                  ; OUT ($BF),A
cv_txt_x:
    xor a                   ; A = 0 with the flags of the game's OR A on the last 0
    jp $4EAB                ; LD E,$02; RST $18; EI; RET
endasm
asm 0218A 14  ; LD IX,$6B94; CALL $4E67; LD IX,$C29B; CALL $4E67
    ld ix,$6B94
    call cv_txt2
    jp $2198
    nop
    nop
    nop
    nop
endasm
asm 07320 14
    di
    ld e,$0B
    rst $18
    ld de,$C29B             ; the second record (after the bank switch, which uses E)
    rst $00
    db far_io, pg_txt2, ent_txt2
    jp cv_txt_t
endasm
asm 04EEB 5   ; LD HL,$C100; LD A,$00  (the sprite table upload, through $505D)
    rst $00
    db far_io, pg_satup, ent_satup
    ret
endasm
asm 0572F 6   ; INC L; LD C,$BF; PUSH HL; POP IX  (the compositor, through $5A25)
    rst $00
    db far_io, pg_comp, ent_comp
    ret
endasm
asm 0FA28 5   ; DI; INC L; PUSH HL; POP IX
    rst $00
    db far_io, pg_ntcopy, ent_ntcopy
    ret
endasm
# Name table copy, bank 0 $123E-$1275 (from $22FA and $2E5C): page 1 vcp.
asm 0123E 5   ; DI; XOR A; OUT ($BF),A (first byte)
    rst $00
    db far_io, pg_vcp, ent_vcp
    ret
endasm
# The compositor's path for a count with bit 7 set, bank 1 $5AC7-$5C5A: page 1 big.
asm 05AC7 5   ; LD C,$BE; LD A,($C250)
    rst $00
    db far_io, pg_big, ent_big
    ret
endasm
# The list writer, bank 1 $5453-$563E (after $544A's RET Z): page 1 lw.
asm 05453 5   ; DI; LD B,A; ADD A,A; ADD A,A; ADD A,A
    rst $00
    db far_io, pg_lw, ent_lw
    ret
endasm
page 0 ntcopy tw_plain tw_mirror satup comp txt txt2
; ntcopy: A = number of entries (1-127), HL = address of the count byte. Runs with interrupts
; off, returns with EI as the game's routine does.
ntcopy:
    di
    inc l
    ld (nc_hl),hl
    ld (nc_iy),iy
    ld (nc_p),hl
    ld (nc_n),a
    ld ix,64
    ld iy,64
nc_loop:
    ld hl,(nc_p)
    ld e,(hl)
    inc hl
    ld d,(hl)
    ld b,12
    call nc_run
    ld hl,(nc_p)
    inc hl
    inc hl
    ld e,(hl)
    inc hl
    ld d,(hl)
    ld b,8
    call nc_run
    ld hl,(nc_p)
    ld bc,6
    add hl,bc
    ld (nc_p),hl
    ld a,(nc_n)
    dec a
    ld (nc_n),a
    jr nz,nc_loop
    ld ix,(nc_p)
    ld iy,(nc_iy)
    ld hl,(nc_hl)
    ld de,(nc_de)
    ld a,(nc_last)
    ex af,af'
    ld bc,6
    ld a,1
    or a
    dec a
    ei
    ret
; nc_run: DE = the game's VRAM control word, B = bytes, IX = IY = 64 (the steps of one run).
nc_run:
    ld (nc_de),de
    ld a,d
    or $08
    add a,$4F
    ld h,a
    ld a,e
    add a,b
    dec a
    ld l,a
    ld a,(hl)
    ld (nc_last),a
    ld l,e
    ld a,e
    neg
    jr z,nc_one
    cp b
    jr nc,nc_one
    ld c,a
    ld a,b
    sub c
    push af
    ld b,c
    ld c,1
    xor a
    call jt_vwrite
    ld a,e
    add a,b
    ld e,a
    jr nc,nc_run__d
    inc d
nc_run__d:
    ld l,0
    pop af
    ld b,a
nc_one:
    ld c,1
    xor a
    jp jt_vwrite
nc_n:    db 0
nc_last: db 0
nc_hl:   dw 0
nc_iy:   dw 0
nc_de:   dw 0
nc_p:    dw 0
; Sprite tile writers, bank 1. tw_plain replaces $45D2-$4738, tw_mirror $476F-$48D5.
; In: A = index into the VRAM address table ($7900 low bytes, $7A00 high bytes), C = tiles (0 = 256),
; HL = source, IX = the object: bit 0 of (IX+$17) set means 4 bytes a tile row, clear means 3 bytes
; and a zero byte. tw_mirror maps each source byte through the table at $7800 (D = $78, E = byte).
; Each tile is 32 bytes at the next VRAM address. The page builds up to TW_MAX tiles in tw_buf and
; writes them with one jt_vwrite call. Registers on return are those the game's loop leaves.
TW_MAX equ 64
tw_plain:
    di
    exx
    ld h,$79
    ld l,a
    ld e,(hl)
    inc h
    ld d,(hl)
    ld (tw_vad),de
    exx
    xor a
    ld (tw_mir),a
    call tw_common
    ld e,0
    ld c,$BE
    ld a,(tw_lasta)
    inc e
    dec e
    ei
    ret
tw_mirror:
    di
    exx
    ld h,$79
    ld l,a
    ld e,(hl)
    inc h
    ld d,(hl)
    ld (tw_vad),de
    exx
    ld a,1
    ld (tw_mir),a
    ld d,$78
    call tw_common
    ld b,0
    ld d,$78
    ld a,(tw_laste)
    ld e,a
    ld a,(tw_lasta)
    inc b
    dec b
    ei
    ret
; tw_common: C = tiles, HL = source, IX = object. Returns HL advanced as the game's loop leaves it.
; Keeps IX, IY, B, D.
tw_common:
    ld (tw_ix),ix
    ld (tw_iy),iy
    push bc
    push de
    ld a,0
    bit 0,(ix+$17)
    jr z,tw_c__m
    inc a
tw_c__m:
    ld (tw_four),a
    ld a,c
    ld (tw_left),a
tw_c__chunk:
    ld a,(tw_left)
    or a
    jr z,tw_c__big
    cp TW_MAX+1
    jr c,tw_c__n
tw_c__big:
    ld a,TW_MAX
tw_c__n:
    ld (tw_cnt),a
    ld b,a
    ld de,tw_buf
tw_c__tile:
    push bc
    call tw_tile
    pop bc
    djnz tw_c__tile
    push hl
    ld hl,tw_buf
    ld de,(tw_vad)
    ld a,(tw_cnt)
    ld c,a
    ld b,32
    ld ix,32
    ld iy,32
    ld a,1
    call jt_vwrite
    ld a,(tw_cnt)
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,de
    ld (tw_vad),hl
    pop hl
    ld a,(tw_cnt)
    ld b,a
    ld a,(tw_left)
    sub b
    ld (tw_left),a
    jr nz,tw_c__chunk
    ld ix,(tw_ix)
    ld iy,(tw_iy)
    pop de
    pop bc
    ret
; tw_tile: one tile from HL into DE (the buffer).
tw_tile:
    ld a,(tw_four)
    or a
    jr nz,tw_t__four
    ld b,8
tw_t__row:
    call tw_rd
    inc hl
    ld (de),a
    inc de
    call tw_rd
    inc hl
    ld (de),a
    inc de
    call tw_rd
    inc hl
    ld (de),a
    inc de
    xor a
    ld (de),a
    inc de
    ld (tw_lasta),a
    djnz tw_t__row
    ret
tw_t__four:
    ld b,8
tw_t__frow:
    ld a,(tw_mir)
    or a
    jr nz,tw_t__fm
    call tw_rd
    inc hl
    ld (de),a
    inc de
    call tw_rd
    inc hl
    ld (de),a
    inc de
    call tw_rd
    inc hl
    ld (de),a
    inc de
    call tw_rd
    inc hl
    ld (de),a
    inc de
    ld (tw_lasta),a
    djnz tw_t__frow
    ret
tw_t__fm:
    call tw_rd
    inc l
    ld (de),a
    inc de
    call tw_rd
    inc l
    ld (de),a
    inc de
    call tw_rd
    inc l
    ld (de),a
    inc de
    call tw_rd
    inc hl
    ld (de),a
    inc de
    ld (tw_lasta),a
    djnz tw_t__frow
    ret
; tw_rd: A = the source byte at HL as the game sees it, mapped through $7800 for tw_mirror.
tw_rd:
    ld a,h
    and $E0
    cp $20
    jr z,tw_rd__p
    ld a,(hl)
    jr tw_rd__m
tw_rd__p:
    call jt_peek
tw_rd__m:
    push hl
    ld (tw_laste),a
    ld l,a
    ld a,(tw_mir)
    or a
    ld a,l
    jr z,tw_rd__x
    ld h,$78
    ld a,(hl)
tw_rd__x:
    pop hl
    ret
tw_mir:   db 0
tw_four:  db 0
tw_left:  db 0
tw_cnt:   db 0
tw_lasta: db 0
tw_laste: db 0
tw_vad:   dw 0
tw_ix:    dw 0
tw_iy:    dw 0
tw_buf:   ds TW_MAX*32
; Sprite table upload, bank 1 $4EEB-$505D (after the frame wait at $4EE2). The game writes the
; 48 Y bytes at $C100 to $3F00, then 48 pairs at $3F80: the X byte from $C200 and a tile number
; that counts up from ($C260); ($C260) flips by $30 each time (two sets of sprite tiles). Through
; the traps this cost about 470,000 cycles a game step. satup writes the two tables with two
; jt_vwrite calls and leaves the registers as the game's code does.
satup:
    ld a,($C260)
    ld (su_e),a
    xor $30
    ld ($C260),a
    ld a,b
    ld (su_b),a
    push de
    ld (su_ix),ix
    ld (su_iy),iy
    ld hl,$C100
    ld de,$3F00
    ld b,48
    ld c,1
    ld ix,64
    ld iy,64
    xor a
    call jt_vwrite
    ld hl,$C200
    ld de,su_buf
    ld a,(su_e)
    ld c,a
    ld b,48
su_l:
    ld a,(hl)
    ld (de),a
    inc hl
    inc de
    ld a,c
    ld (de),a
    inc de
    inc c
    djnz su_l
    ld hl,su_buf
    ld de,$3F80
    ld b,96
    ld c,1
    ld a,1
    call jt_vwrite
    ld ix,(su_ix)
    ld iy,(su_iy)
    pop de
    ld a,(su_b)
    sub 96
    ld b,a
    ld a,(su_e)
    add a,47
    ld e,a
    inc e
    ld c,$BE
    ld hl,$C230
    ld a,$7F
    ei
    ret
su_e:   db 0
su_b:   db 0
su_ix:  dw 0
su_iy:  dw 0
su_buf: ds 96
; comp: the software sprite compositor, bank 1 $572F-$5A25 (from $570D, once a game step; the
; path for a count with bit 7 set, $5AC7, stays native). In: A = entries (1-127), HL = $C3xx with
; L = ($C250) (the list's count byte). For each 6-byte entry (IX):
;  A  reads 4 bytes of VRAM at (IX+0,1) and 4 at 8 bytes on, the odd ones AND $0F, to $C340-$C347;
;  B  writes 6 cells at (IX+0,1) and 4 at (IX+2,3): the shadow cell where its high byte has the
;     priority bit (row 2: and not bit 7), else the next sprite tile (high byte $41, row 2 $51);
;  C  with bank ($C2FB): two tiles named by $C340-$C343 to $C348/$C368, from ROM at ($CF78) for
;     hflip or a tile below $29, else read from VRAM; the tiles named by $C344-$C347 from ROM to
;     $C388/$C3A8;
;  D  with bank 9: 10 tiles at the entry's first sprite tile from the source (IX+4,5): 2 tiles of
;     (background AND mask) OR data, 2 plain, 2 masked, 4 plain.
; Through the traps this cost about 250,000 cycles a step (the cell writes at $57BE-$58D6, the
; VRAM reads at $5754-$578D, $590A and $5940, and the tile writes at $59A6-$5A18). comp reads
; VRAM from the VRAM copy (a control word that is not a plain read goes through the traps, as the
; game's code would), writes with jt_vwrite, and switches banks through cv_rst18.
; Runtime internals used: SHADOW_PAGE 28 (the VRAM copy, pages 28-29); cur_mmu $E02D is public.
CP_RST18 equ $74D0
comp:
    di
    ld (cp_n),a
    ld a,l              ; ($C250): 0 -> first sprite tile $143, else $161 (DEC L; JR Z at $5735)
    or a
    ld a,$43
    jr z,cp__b0
    ld a,$61
cp__b0:
    ld (cp_tile),a
    ld a,$01
    ld (cp_tile+1),a
    inc l
    ld (cp_ix),hl
    ld (cp_iy0),iy
    exx
    ld (cp_b1),bc            ; the main set's B (the game leaves it)
    exx
cp_loop:
    ld hl,(cp_tile)
    ld (cp_tbase),hl
; A: the name table bytes
    ld ix,(cp_ix)
    ld l,(ix+0)
    ld a,(ix+1)
    res 6,a
    ld h,a
    ld (cp_ra),hl
    ld de,$C340
    ld b,4
    call cp_rd
    ld hl,(cp_ra)
    ld a,l
    add a,8
    ld l,a
    ld b,4
    call cp_rd
    ld hl,$C341
    ld b,4
cp_a__m:
    ld a,(hl)
    and $0F
    ld (hl),a
    inc l
    inc l
    djnz cp_a__m
; B: the two rows of cells
    ld ix,(cp_ix)
    ld e,(ix+0)
    ld d,(ix+1)
    ld a,$40
    ld (cp_hmask),a
    xor a
    ld (cp_row2),a
    ld b,6
    call cp_row
    ld ix,(cp_ix)
    ld e,(ix+2)
    ld d,(ix+3)
    ld a,$50
    ld (cp_hmask),a
    ld a,1
    ld (cp_row2),a
    ld b,4
    call cp_row
; C: the background tiles
    ld a,($C2FB)
    ld e,a
    call CP_RST18
    ld hl,($C340)
    ld de,$C348
    call cp_bg
    ld hl,($C342)
    ld de,$C368
    call cp_bg
    ld hl,($C344)
    ld de,$C388
    call cp_rom
    ld hl,($C346)
    ld de,$C3A8
    call cp_rom
; D: 10 tiles
    ld e,9
    call CP_RST18
    ld ix,(cp_ix)
    ld l,(ix+4)
    ld h,(ix+5)
    ld a,h
    and $E0
    cp $20
    jp z,jt_fatal       ; a sprite source in $2000-$3FFF is not handled (never seen)
    ld de,$C348
    ld ix,cp_tbuf
    call cp_mask
    ld b,64
    call cp_plain
    call cp_mask
    ld b,128
    call cp_plain
    ld (cp_src),hl
    ld (cp_de2),de
    ld hl,(cp_tbase)
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ex de,hl
    ld hl,cp_tbuf
    ld b,32
    ld c,10
    ld ix,32
    ld iy,32
    ld a,1
    call jt_vwrite
    call cp_ptclr
; the next entry
    ld hl,(cp_ix)
    ld bc,6
    add hl,bc
    ld (cp_ix),hl
    ld a,(cp_n)
    dec a
    ld (cp_n),a
    jp nz,cp_loop
; the registers as the game's loop leaves them, then bank 2
    ld ix,(cp_ix)
    ld iy,$C340
    ld hl,(cp_src)
    ld de,(cp_de2)
    ld bc,$00BF
    ld a,(cp_last)
    or a
    ex af,af'
    exx
    ld hl,(cp_tile)
    ld bc,(cp_b1)
    ld c,$BF
    ld a,(cp_d1)
    ld d,a
    ld e,2
    call CP_RST18
    ld a,1
    dec a
    ei
    ret
; cp_rd: B bytes of VRAM from the control word HL (L then H, as the game writes it) to DE.
cp_rd:
    ld a,h
    and $C0
    jr nz,cp_rd__t
    push de
    call cp_map
    pop de
cp_rd__l:
    ld a,(hl)
    ld (de),a
    inc hl
    inc de
    djnz cp_rd__l
    jp cp_unmap
cp_rd__t:
    ld a,l
    rst $00
    db $05              ; OUT ($BF),A
    ld a,h
    rst $00
    db $05
cp_rd__tl:
    rst $00
    db $0C              ; IN A,($BE)
    ld (de),a
    inc de
    djnz cp_rd__tl
    ret
; cp_map: HL = VRAM address (bits 14-15 ignored): its VRAM copy page in slot 0, HL = there
cp_map:
    ld a,h
    and $3F
    ld h,a
    rlca
    rlca
    rlca
    and 1
    add a,28
    db $ED,$92,$50            ; nextreg $50,a
    ld a,h
    and $1F
    ld h,a
    ret
cp_unmap:
    ld a,(cur_mmu+0)
    db $ED,$92,$50
    ret
; cp_row: DE = the control word of the row, B = cells (row 1: 6, row 2: 4); the cells into
; cp_rbuf, then one jt_vwrite.
cp_row:
    ld a,b
    add a,a
    ld (cp_rlen),a
    ld (cp_rad),de
    ld a,d
    or $08
    add a,$4F
    ld d,a
    ld (cp_d1),a
    inc e
    ld hl,cp_rbuf
cp_r__c:
    ld a,(de)
    bit 4,a
    jr z,cp_r__s
    ld c,a
    ld a,(cp_row2)
    or a
    jr z,cp_r__sh
    bit 7,c
    jr nz,cp_r__s
cp_r__sh:
    dec e
    ld a,(de)
    ld (hl),a
    inc hl
    inc e
    ld a,(de)
    ld (hl),a
    inc hl
    jr cp_r__n
cp_r__s:
    push de
    ld de,(cp_tile)
    ld (hl),e
    inc hl
    ld a,(cp_hmask)
    or d
    ld (hl),a
    inc hl
    pop de
cp_r__n:
    push hl
    ld hl,(cp_tile)          ; INC HL after every cell, both branches
    inc hl
    ld (cp_tile),hl
    pop hl
    inc e
    inc e
    djnz cp_r__c
    ld hl,cp_rbuf
    ld de,(cp_rad)
    ld a,(cp_rlen)
    ld b,a
    ld c,1
    ld ix,64
    ld iy,64
    ld a,1
    jp jt_vwrite
; cp_bg: HL = the tile's two name table bytes (low, high AND $0F), DE = destination
cp_bg:
    bit 1,h
    jr nz,cp_rom
    ld a,l
    cp $29
    jr c,cp_rom
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld b,32
    jp cp_rd
; cp_rom: the tile from ROM at ($CF78) + 32 * HL (16 bits)
cp_rom:
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld bc,($CF78)
    add hl,bc
    ld a,h
    and $E0
    cp $20
    jr z,cp_rom__p
    ld bc,32
    ldir
    ret
cp_rom__p:              ; $2000-$3FFF holds this page: read as the game sees it
    ld b,32
cp_rom__pl:
    call jt_peek
    ld (de),a
    inc hl
    inc de
    djnz cp_rom__pl
    ret
; cp_mask: 64 bytes (bg at DE) AND mask OR data, from HL as the game steps it (INC L, the 8th INC HL)
cp_mask:
    ld b,16
cp_m__l:
    call cp_m1
    inc l
    call cp_m1
    inc l
    call cp_m1
    inc l
    call cp_m1
    inc hl
    djnz cp_m__l
    ret
cp_m1:
    ld a,(de)
    inc e
    and (hl)
    inc l
    or (hl)
    ld (ix+0),a
    inc ix
    ld (cp_last),a
    ret
cp_plain:
    ld a,(hl)
    inc hl
    ld (ix+0),a
    inc ix
    ld (cp_last),a
    djnz cp_plain
    ret
; cp_ptclr: the 10 tiles just written leave the runtime's pri_tiles. Row 2's cells show them with
; the priority bit, so pri_tile puts them there when Layer 2 draws those cells, and then each step's
; new tiles would start pri_redraw, a scan of all 896 cells (the largest cost left in play). The
; tiles from $143 are shown only by the table at $3000 and those from $161 only by the one at
; $3800, and each set is written while its table is hidden. At the flip ntdiff writes every cell that
; differs between the tables (the two sets never share a tile number), and nt_put marks those
; cells, so Layer 2 draws them from the new tiles. It also clears the bits of the 64 tiles that
; are the hidden name table's VRAM ($3000-$37FF while $3800 shows, and the other way round): ntcopy
; writes there every step, and the runtime converts those bytes as tiles; a bit left from an earlier
; screen (tile 387) made each step start pri_redraw. While the game double-buffers, no cell shows
; those tiles. Runtime internals: pri_tiles $3538 in FW2_PAGE 25; nt_base $E04B is public.
PT_TILES equ $3538-$2000
cp_ptclr:
    db $ED,$91,$50,25         ; nextreg $50,25
    ld hl,PT_TILES+48         ; the hidden name table's tiles: 384-447 ($3000) or 448-511 ($3800)
    ld a,(nt_base+1)
    cp $38
    jr z,cp_pc__h0
    ld hl,PT_TILES+56
cp_pc__h0:
    ld b,8
cp_pc__h1:
    ld (hl),0
    inc hl
    djnz cp_pc__h1
    ld de,(cp_tbase)
    ld b,10
cp_pc__l:
    push bc
    ld a,e
    and 7
    ld b,a
    ld a,1
    jr z,cp_pc__s
cp_pc__b:
    add a,a
    djnz cp_pc__b
cp_pc__s:
    cpl
    ld c,a
    ld a,e
    srl d
    rra
    srl a
    srl a               ; (tile >> 3), tile < 512
    ld hl,PT_TILES
    add a,l
    ld l,a
    jr nc,cp_pc__h
    inc h
cp_pc__h:
    ld a,(hl)
    and c
    ld (hl),a
    ld de,(cp_tbase)    ; next tile: cp_tbase + count
    pop bc
    ld a,10
    sub b
    inc a
    add a,e
    ld e,a
    jr nc,cp_pc__n
    inc d
cp_pc__n:
    djnz cp_pc__l
    jp cp_unmap
cp_n:     db 0
cp_row2:  db 0
cp_hmask: db 0
cp_last:  db 0
cp_d1:    db 0
cp_tile:  dw 0
cp_tbase: dw 0
cp_ix:    dw 0
cp_iy0:   dw 0
cp_b1:    dw 0
cp_ra:    dw 0
cp_rad:   dw 0
cp_src:   dw 0
cp_de2:   dw 0
cp_rbuf:  ds 12
cp_rlen:  db 0
cp_tbuf:  ds 320
; txt: the text printer $4E67 from its first character on (the cave has done DI and the bank 11
; switch); txt2 prints the record at IX and then the one at DE, as the game's two calls at $218A.
; Each record's cells go into a list (address, value) without writing them; in txt2 a cell of the
; second record replaces the first record's cell at the same address. The list is then compared
; with the VRAM copy (pages 28-29) and each run of differing cells is written with one jt_vwrite;
; the last character's cell is written in any case, last, so the VDP is left as the game's writes
; leave it. The minutes screen clears its row 10 and prints its text there again on every pass;
; written through, those cells changed twice a pass and Layer 2 drew them again each time.
; Returns as the game's loop leaves its registers: B = the last row, C = the column, D = the high
; byte of the last row's address, HL = the last character's tile + $148 (unchanged when no record
; has a character), IX after the last record's 0. Carry set when the last record ends just after a
; $0D, or has no character, with DE = that row's address: the cave writes that control word.
; Runs on a stack of its own (tx_stk), with interrupts off as the cave leaves them: the game's
; $4E67 goes 6 bytes deep, and txt with jt_vwrite deeper.
; Runtime internals used: SHADOW_PAGE 28 (the VRAM copy, pages 28-29); cur_mmu $E02D is public.
TX_MAX equ 250
txt:
    ld (tx_sp),sp
    ld sp,tx_stk_top
    call tx_init
    call tx_parse
    jp tx_commit
txt2:
    ld (tx_sp),sp
    ld sp,tx_stk_top
    ld (tx_rec2),de
    call tx_init
    call tx_parse
    ld a,(tx_np)
    ld (tx_srch),a          ; cells of the first record that the second can replace
    ld ix,(tx_rec2)
    call tx_parse
    jp tx_commit
tx_init:
    ld (tx_hl),hl
    xor a
    ld (tx_np),a
    ld (tx_any),a
    ld (tx_srch),a
    ret
; tx_parse: the record at IX into the list
tx_parse:
    call tx_rd
    ld c,a
    call tx_rd
    ld b,a
tx_line:
    ld h,b                  ; DE = $3800 + 64 B + 2 C, as $4334
    ld l,0
    srl h
    rr l
    srl h
    rr l
    push bc
    ld b,$38
    sla c
    add hl,bc
    pop bc
    ld (tx_row),hl
    ld (tx_de),hl
    xor a
    ld (tx_rowc),a
tx_char:
    call tx_rd
    or a
    ret z
    cp $0D
    jr z,tx_nl
    push bc
    ld l,a
    ld h,0
    ld bc,$0148
    add hl,bc
    pop bc
    ld (tx_hl),hl
    ld a,h
    or $10
    ld h,a
    ld de,(tx_de)
    call tx_add
    ld hl,(tx_de)
    inc hl
    inc hl
    ld (tx_de),hl
    ld a,1
    ld (tx_rowc),a
    ld (tx_any),a
    jr tx_char
tx_nl:
    inc b
    jr tx_line
; tx_add: DE = address, HL = value; replaces a cell of the first record or appends. tx_fi = its index.
tx_add:
    ld a,d
    and $3F
    ld d,a
    push bc
    ld a,(tx_srch)
    or a
    jr z,tx_ad__new
    ld b,a
    push hl
    ld hl,tx_list
    ld c,0
tx_ad__s:
    ld a,(hl)
    cp e
    jr nz,tx_ad__n
    inc hl
    ld a,(hl)
    dec hl
    cp d
    jr z,tx_ad__f
tx_ad__n:
    inc hl
    inc hl
    inc hl
    inc hl
    inc c
    djnz tx_ad__s
    pop hl
tx_ad__new:
    ld a,(tx_np)
    cp TX_MAX
    jr c,tx_ad__ok
    push de                 ; the list is full: write it out and start a new one
    push hl
    ld a,$FF
    ld (tx_fi),a            ; no forced cell in this part
    call tx_wlist
    xor a
    ld (tx_np),a
    ld (tx_srch),a
    pop hl
    pop de
tx_ad__ok:
    ld a,(tx_np)
    ld c,a
    inc a
    ld (tx_np),a
    push hl
    call tx_ptr
    jr tx_ad__w
tx_ad__f:                   ; HL = the entry, C = its index; the value on the stack
tx_ad__w:
    ld (hl),e
    inc hl
    ld (hl),d
    inc hl
    pop de                  ; the value
    ld (hl),e
    inc hl
    ld (hl),d
    ld a,c
    ld (tx_fi),a
    pop bc
    ret
; tx_ptr: HL = the entry of index C
tx_ptr:
    ld l,c
    ld h,0
    add hl,hl
    add hl,hl
    push de
    ld de,tx_list
    add hl,de
    pop de
    ret
tx_commit:
    ld a,(tx_any)
    or a
    jr nz,tx_cm__f
    ld a,$FF
    ld (tx_fi),a            ; no character: nothing is forced
tx_cm__f:
    call tx_wlist
    ld a,(tx_any)
    or a
    call nz,tx_wforced
    ld de,(tx_row)
    ld hl,(tx_hl)
    ld a,(tx_rowc)
    cp 1                    ; carry = the last row had no characters
    ld sp,(tx_sp)
    ret
; tx_wlist: the tx_np cells of the list that differ from the VRAM copy, in runs, but not the
; cell tx_fi
tx_wlist:
    push bc
    push ix
    push iy
    xor a
    ld (tx_run),a
    ld c,0
tx_wl__c:
    ld a,(tx_np)
    cp c
    jp z,tx_wl__e
    ld a,(tx_fi)
    cp c
    jr z,tx_wl__same        ; the forced cell: written at the end
    call tx_ptr
    ld e,(hl)
    inc hl
    ld d,(hl)
    inc hl
    push de
    ld a,d                  ; the VRAM copy of the cell at DE in slot 0
    rlca
    rlca
    rlca
    and 1
    add a,28
    db $ED,$92,$50          ; nextreg $50,a
    ld a,d
    and $1F
    ld d,a
    ld a,(de)
    cp (hl)
    jr nz,tx_wl__dm
    inc de
    inc hl
    ld a,(de)
    cp (hl)
    dec hl
tx_wl__dm:
    push af
    call tx_unmap
    pop af
    pop de
    jr z,tx_wl__same0
    ld a,(tx_run)           ; differs: into the open run, or a new one
    or a
    jr z,tx_wl__new
    push hl
    ld hl,(tx_rend)
    or a
    sbc hl,de
    pop hl
    jr z,tx_wl__add
    call tx_wrun
tx_wl__new:
    ld (tx_rva),de
    ld (tx_rend),de
tx_wl__add:
    push de
    ld de,(tx_rp)
    ld a,(tx_run)
    or a
    jr nz,tx_wl__a2
    ld de,tx_rbuf
tx_wl__a2:
    ld a,(hl)
    ld (de),a
    inc hl
    inc de
    ld a,(hl)
    ld (de),a
    inc de
    ld (tx_rp),de
    pop de
    inc de
    inc de
    ld (tx_rend),de
    ld a,(tx_run)
    inc a
    ld (tx_run),a
    cp 120
    call nc,tx_wrun
    jp tx_wl__n
tx_wl__same0:
tx_wl__same:
    call tx_wrun
tx_wl__n:
    inc c
    jp tx_wl__c
tx_wl__e:
    call tx_wrun
    pop iy
    pop ix
    pop bc
    ret
tx_unmap:
    ld a,(cur_mmu+0)
    db $ED,$92,$50          ; nextreg $50,a
    ret
; tx_wrun: the open run of tx_run cells from tx_rbuf to tx_rva, in one jt_vwrite
tx_wrun:
    ld a,(tx_run)
    or a
    ret z
    push bc
    push de
    push hl
    add a,a
    ld b,a
    ld c,1
    ld hl,tx_rbuf
    ld de,(tx_rva)
    ld ix,64
    ld iy,64
    ld a,1                  ; the source is in this page
    call jt_vwrite
    xor a
    ld (tx_run),a
    pop hl
    pop de
    pop bc
    ret
; tx_wforced: the cell tx_fi, the game's last data write
tx_wforced:
    ld a,(tx_fi)
    ld c,a
    call tx_ptr
    ld e,(hl)
    inc hl
    ld d,(hl)
    inc hl
    push ix
    push iy
    ld bc,$0201
    ld ix,64
    ld iy,64
    ld a,1
    call jt_vwrite
    pop iy
    pop ix
    ret
; tx_rd: A = the byte the game sees at IX, IX + 1
tx_rd:
    push hl
    push ix
    pop hl
    inc ix
    ld a,h
    and $E0
    cp $20
    jr z,tx_rd__p
    ld a,(hl)
    pop hl
    ret
tx_rd__p:
    call jt_peek
    pop hl
    ret
tx_np:    db 0
tx_srch:  db 0
tx_fi:    db 0
tx_run:   db 0
tx_any:   db 0
tx_rowc:  db 0
tx_row:   dw 0
tx_de:    dw 0
tx_hl:    dw 0
tx_rva:   dw 0
tx_rend:  dw 0
tx_rp:    dw 0
tx_rec2:  dw 0
tx_sp:    dw 0
tx_rbuf:  ds 240
tx_list:  ds 4*TX_MAX
tx_stk:   ds 64
tx_stk_top:
endpage
page 1 upl ntb u54 ntl nfill vcp big lw
    OPT --zxnext        ; NEXTREG, SWAPNIB, ADD HL,A
; Page 1: the screen set-up routines (tile uploads and name table writers).
; upl: the tile upload $4500-$459B: vcw writes the tiles that differ from the VRAM copy. Returns as the game's
; loop leaves its registers: HL after the source, B = 1, C = $BE, E = 0, D kept, A = the byte the
; game sees at D * 256 + 1 (the loop's last LD A,(DE)), Z and N set as by its last DEC E (carry is
; not the loop's); in the alternate set H = $7A, L = the slot, DE = the VRAM address. Interrupts
; on at the return, as the game's EI; RET. Runs on a stack of its own (the game's routine pushes
; nothing), with interrupts off.
upl:
    di
    ld (up_sp),sp
    ld sp,up_stk_top
    exx
    ld h,$79
    ld l,a
    ld e,(hl)
    inc h
    ld d,(hl)
    ld (up_va),de
    exx
    ld (up_ix),ix
    ld (up_iy),iy
    ld (up_hl),hl
    push de
    ld de,(up_va)
    push bc
    call vcw                ; C tiles (0 = 256): only those that differ
    pop bc
    ld hl,(up_hl)
    ld l,c                  ; HL = source + 32 C
    ld h,0
    ld a,c
    or a
    jr nz,upl__n
    inc h
upl__n:
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld de,(up_hl)
    add hl,de
    pop de
    ld ix,(up_ix)
    ld iy,(up_iy)
    push hl
    ld h,d
    ld l,1
    call jt_peek
    pop hl
    ld bc,$01BE
    ld e,1
    dec e
    ld sp,(up_sp)
    ei
    ret
up_sp:    dw 0
up_va:    dw 0
up_ix:    dw 0
up_iy:    dw 0
up_hl:    dw 0
up_stk:   ds 32
up_stk_top:
; ntb: the name table writer $4D20-$4DA3. HL = the map (192 bytes as the game sees memory).
; Builds the cells in nb_img (the name table's layout, 64 bytes a row), compares them with the VRAM
; copy (page 29: $3800 is at $1800 in slot 0) and writes each run of differing cells of a row with
; one jt_vwrite; cell (23, 31), the game's last write, is written in any case, last. Returns as the
; loop leaves its registers: IX = ($C244), B = 24, C = 0, DE = $3DFC, HL after the map, A = 0 with
; Z set; in the alternate set BC = ($C25A) and HL after the last block's 8 bytes. Interrupts on at
; the return, as after the loop's last EI. Runs on its own stack with interrupts off (the game's
; loop takes interrupts between blocks; this runs in about a tenth of its Master System time).
ntb:
    di
    ld (nb_sp),sp
    ld sp,nb_stk_top
    xor a                   ; rows 0-23, no hook
    ld (nb_r0),a
    ld (nb_hk),a
    jr nb_go
; ntl: the level's writer $4B62-$4BE1, the same with B = the first row (1 from $499D) and C = 0,
; and $4DAD called natively for each block with A = the map byte and DE = the block's address
; (it records torches and the like in RAM; no I/O). Returns B = first row + 24, C = 0, DE = the
; last block's second row, HL after the map, A = 0 with Z set, the alternate set as ntb.
ntl:
    di
    ld (nb_sp),sp
    ld sp,nb_stk_top
    ld a,b
    ld (nb_r0),a
    ld a,1
    ld (nb_hk),a
    ld (nb_gix),ix
nb_go:
    push iy
    ld (nb_src),hl
    ld ix,nb_img
    ld a,(nb_r0)            ; B, C: the block's row and column, as the game's loop
    ld b,a
    ld a,0
    ld (nb_c),a
    ld c,192
nb_blk:
    call nb_rd              ; A = map byte, HL + 1
    push af
    ld a,(nb_hk)
    or a
    jr z,nb_nohk
    pop af
    push af
    push bc
    push de
    push hl
    push ix
    ld (nb_b),bc
    ld (nb_byte),a                  ; DE = $3800 + 64 row + 2 column, as $4334
    ld a,b
    ld h,a
    ld l,0
    srl h
    rr l
    srl h
    rr l
    ld a,(nb_c)
    add a,a
    add a,l
    ld l,a
    ld a,h
    adc a,$38
    ld h,a
    ex de,hl
    ld bc,(nb_b)
    ld a,(nb_c)
    ld c,a                  ; BC = row, column, as the game's loop has them here
    ld a,(nb_byte)
    ld ix,(nb_gix)
    call $4DAD
    ld (nb_gix),ix
    pop ix
    pop hl
    pop de
    pop bc
nb_nohk:
    pop af
    push hl
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    ld de,($C25A)
    add hl,de               ; the block's 8 bytes
    call nb_rd
    ld (ix+0),a
    call nb_rd
    ld (ix+1),a
    call nb_rd
    ld (ix+2),a
    call nb_rd
    ld (ix+3),a
    call nb_rd
    ld (ix+64),a
    call nb_rd
    ld (ix+65),a
    call nb_rd
    ld (ix+66),a
    call nb_rd
    ld (ix+67),a
    ld (nb_alt),hl
    pop hl
    ld de,4                 ; next block: 4 bytes on, and a row of blocks is 2 rows
    add ix,de
    ld a,(nb_c)             ; column + 2; a new row of blocks every 16
    add a,2
    and $1F
    ld (nb_c),a
    jr nz,nb_nx
    inc b
    inc b
    ld de,64
    add ix,de
nb_nx:
    dec c
    jp nz,nb_blk
    ld (nb_src),hl
; compare and write, row by row
    ld a,(nb_r0)            ; DE = $3800 + 64 first row
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld de,$3800
    add hl,de
    ex de,hl
    ld (nb_vr0),de
    ld hl,nb_img
    ld b,24
nb_row:
    push bc
    ld c,32
    xor a
    ld (nb_run),a
nb_cell:
    push hl
    push de
    ld a,d
    sub $20
    db $ED,$91,$50,29       ; nextreg $50,29: VRAM $2000-$3FFF in slot 0
    ld d,a
    ld a,(de)
    cp (hl)
    jr nz,nb_df
    inc de
    inc hl
    ld a,(de)
    cp (hl)
nb_df:
    push af
    ld a,(cur_mmu+0)
    db $ED,$92,$50          ; nextreg $50,a
    pop af
    pop de
    pop hl
    jr z,nb_same
    ld a,b                  ; the last cell is written at the end
    dec a
    jr nz,nb_wr
    ld a,c
    dec a
    jr z,nb_same
nb_wr:
    ld a,(nb_run)
    or a
    jr nz,nb_ext
    ld (nb_rs),hl
    ld (nb_rd2),de
nb_ext:
    inc a
    ld (nb_run),a
    jr nb_nc
nb_same:
    call nb_flush
nb_nc:
    inc hl
    inc hl
    inc de
    inc de
    dec c
    jr nz,nb_cell
    call nb_flush
    pop bc
    djnz nb_row
    ld hl,(nb_vr0)          ; the last cell
    ld de,23*64+62
    add hl,de
    ex de,hl
    ld hl,nb_img+23*64+62
    ld bc,$0201
    ld ix,64
    ld iy,64
    ld a,1
    call jt_vwrite
    call l2go
    pop iy
    exx                     ; the alternate set as the loop leaves it
    ld bc,($C25A)
    ld hl,(nb_alt)
    exx
    ld a,(nb_hk)
    or a
    ld ix,($C244)           ; ntb: the loop's LD IX,($C244)
    jr z,nb_ix
    ld ix,(nb_gix)          ; ntl: as $4DAD left it
nb_ix:
    ld hl,(nb_vr0)          ; DE = the last block's second row: first row + 23, column 30
    ld de,23*64+60
    add hl,de
    ex de,hl
    ld a,(nb_r0)
    add a,24
    ld b,a
    ld c,0
    ld hl,(nb_src)
    ld a,1
    dec a
    ld sp,(nb_sp)
    ei
    ret
; nb_rd: A = the byte the game sees at HL, HL + 1
nb_rd:
    ld a,h
    and $E0
    cp $20
    jr z,nb_rd__p
    ld a,(hl)
    inc hl
    ret
nb_rd__p:
    call jt_peek
    inc hl
    ret
; nb_flush: the open run of nb_run cells, from nb_rs to nb_rd2
nb_flush:
    ld a,(nb_run)
    or a
    ret z
    push bc
    push de
    push hl
    push ix
    push iy
    add a,a
    ld b,a
    ld c,1
    ld hl,(nb_rs)
    ld de,(nb_rd2)
    ld ix,64
    ld iy,64
    ld a,1
    call jt_vwrite
    call l2go               ; the run's Layer 2 cells
    xor a
    ld (nb_run),a
    pop iy
    pop ix
    pop hl
    pop de
    pop bc
    ret
nb_sp:   dw 0
nb_src:  dw 0
nb_alt:  dw 0
nb_rs:   dw 0
nb_rd2:  dw 0
nb_run:  db 0
nb_r0:   db 0
nb_hk:   db 0
nb_byte: db 0
nb_c:    db 0
nb_b:    dw 0
nb_gix:  dw 0
nb_vr0:  dw 0
nb_img:  ds 24*64
nb_stk:  ds 48
nb_stk_top:
; u54: $5403-$541F. Returns HL = $AF94 + $760, BC = 0, A = 0 with Z set, as the loop leaves them;
; the interrupt state kept. Own stack.
u54:
    ld (u5_sp),sp
    ld sp,u5_stk_top
    push ix
    push iy
    ld a,i
    di
    ld a,0
    jp po,u54__s
    inc a
u54__s:
    ld (u5_ei),a
    ld hl,$AF94
    ld de,$2D00
    ld c,59
    call vcw
    pop iy
    pop ix
    ld hl,$AF94+$760
    ld bc,0
    ld sp,(u5_sp)           ; back on the game's stack before interrupts go on again
    ld a,(u5_ei)
    or a
    jr z,u54__d
    ei
u54__d:
    xor a
    ret
u5_sp:   dw 0
u5_ei:   db 0
u5_stk:  ds 48
u5_stk_top:
; vcw: C tiles (0 = 256) from HL (as the game sees memory) to VRAM DE (a multiple of 32), only those
; that differ from the VRAM copy, in runs of whole tiles with jt_vwrite; then the last byte once
; more, so that the VDP address and read buffer end as after the game's writes. Interrupts must be
; off (slot 0 holds the VRAM copy while a tile is compared). Uses AF, BC, DE, HL, IX, IY.
vcw:
    ld a,e
    and 31
    jr z,vcw__a
    ld b,32                 ; not tile-aligned: everything, as the game writes it
    ld ix,32
    ld iy,32
    xor a
    jp jt_vwrite
vcw__a:
    xor a
    ld (vc_run),a
vcw__t:
    push bc
    push de
    ld de,vc_buf            ; the source tile into vc_buf
    ld b,32
vcw__c:
    ld a,h
    and $E0
    cp $20
    jr nz,vcw__m
    call jt_peek
    jr vcw__s
vcw__m:
    ld a,(hl)
vcw__s:
    ld (de),a
    inc hl
    inc de
    djnz vcw__c
    pop de
    push hl
    push de
    ld a,d                  ; the VRAM copy's page in slot 0
    and $3F
    rlca
    rlca
    rlca
    and 1
    add a,28
    db $ED,$92,$50          ; nextreg $50,a
    ld a,d
    and $1F
    ld d,a
    ld hl,vc_buf
    ld b,32
vcw__k:
    ld a,(de)
    cp (hl)
    jr nz,vcw__d
    inc de
    inc hl
    djnz vcw__k
vcw__d:
    ld a,(cur_mmu+0)
    db $ED,$92,$50          ; nextreg $50,a
    pop de
    pop hl
    ld a,b
    or a
    jr z,vcw__same
    ld a,(vc_run)           ; differs: into the run
    or a
    jr nz,vcw__x
    push hl
    ld bc,-32
    add hl,bc
    ld (vc_rs),hl
    pop hl
    ld (vc_rd),de
vcw__x:
    inc a
    ld (vc_run),a
    cp 128
    call nc,vc_flush
    jr vcw__n
vcw__same:
    call vc_flush
vcw__n:
    ld (vc_lsrc),hl         ; after this tile
    ld (vc_ld),de
    ex de,hl
    ld bc,32
    add hl,bc
    ex de,hl
    pop bc
    dec c
    jr nz,vcw__t
    call vc_flush
    ld hl,(vc_lsrc)         ; the last byte once more
    dec hl
    ld de,(vc_ld)
    ld a,e
    add a,31
    ld e,a
    ld bc,$0101
    ld ix,1
    ld iy,1
    xor a
    jp jt_vwrite
vc_flush:
    ld a,(vc_run)
    or a
    ret z
    push bc
    push de
    push hl
    ld c,a
    ld b,32
    ld hl,(vc_rs)
    ld de,(vc_rd)
    ld ix,32
    ld iy,32
    xor a
    call jt_vwrite
    xor a
    ld (vc_run),a
    pop hl
    pop de
    pop bc
    ret
vc_run:  db 0
vc_rs:   dw 0
vc_rd:   dw 0
vc_lsrc: dw 0
vc_ld:   dw 0
vc_buf:  ds 32
; nfill: $BD4C-$BD69, E = the cells' low byte ($80), high byte 0, $380 cells from $3800. Runs of
; differing cells go out with jt_vwrite from the 2-byte pattern (source step 0), the last cell in
; any case, last. Returns A = 0 with Z set, BC = 0, DE and HL kept; the interrupt state kept.
; After the clear no cell has the priority bit, so the tiles in the runtime's pri_tiles (those that
; earlier screens' priority cells showed, such as the "minutes left" text, tiles $168-$1A7) are
; cleared, with pri_chg and pri_redo: the level's tiles at the same numbers are rewritten in the
; wait loop after the build and in play (torches, the prince), and each rewrite of a tile with its
; bit set made the runtime scan all 896 cells (pri_redraw, about 280,000 cycles). Layer 2 draws the
; level's priority cells from ntl's marks and sets their bits again. Runtime internals: pri_tiles
; $3538, pri_chg $3578 and pri_redo $346A in FW2_PAGE 25.
nfill:
    ld (nf_sp),sp
    ld sp,nf_stk_top
    push de
    push hl
    push ix
    push iy
    ld a,i
    di
    ld a,0
    jp po,nf_s
    inc a
nf_s:
    ld (nf_ei),a
    ld a,e
    ld (nf_pat),a
    xor a
    ld (nf_pat+1),a
    ld (nf_run),a
    ld hl,$3800
    ld bc,$0380
nf_c:
    push bc
    ld a,b                  ; the last cell is written at the end
    or a
    jr nz,nf_k
    ld a,c
    dec a
    jr z,nf_same
nf_k:
    push hl
    ld a,h
    sub $20
    ld h,a
    db $ED,$91,$50,29       ; nextreg $50,29
    ld a,(nf_pat)
    cp (hl)
    jr nz,nf_d
    inc hl
    ld a,(hl)
    or a
nf_d:
    push af
    ld a,(cur_mmu+0)
    db $ED,$92,$50          ; nextreg $50,a
    pop af
    pop hl
    jr z,nf_same
    ld a,(nf_run)
    or a
    jr nz,nf_x
    ld (nf_rd),hl
nf_x:
    inc a
    ld (nf_run),a
    cp 255
    call nc,nf_flush
    jr nf_n
nf_same:
    call nf_flush
nf_n:
    inc hl
    inc hl
    pop bc
    dec bc
    ld a,b
    or c
    jr nz,nf_c
    call nf_flush
    ld de,$3800+2*$37F       ; the last cell
    ld hl,nf_pat
    ld bc,$0201
    ld ix,2
    ld iy,2
    ld a,1
    call jt_vwrite
    call l2go
    db $ED,$91,$50,25       ; nextreg $50,25: FW2_PAGE in slot 0
    ld hl,$3538-$2000       ; pri_tiles and pri_chg after it: 128 bytes
    ld b,128
nf_pt:
    ld (hl),0
    inc hl
    djnz nf_pt
    xor a
    ld ($346A-$2000),a      ; pri_redo
    ld a,(cur_mmu+0)
    db $ED,$92,$50          ; nextreg $50,a
    pop iy
    pop ix
    pop hl
    pop de
    ld bc,0
    ld sp,(nf_sp)           ; back on the game's stack before interrupts go on again
    ld a,(nf_ei)
    or a
    jr z,nf_di
    ei
nf_di:
    xor a
    ret
nf_flush:
    ld a,(nf_run)
    or a
    ret z
    push bc
    push de
    push hl
    ld c,a
    ld b,2
    ld hl,nf_pat
    ld de,(nf_rd)
    ld ix,0
    ld iy,2
    ld a,1
    call jt_vwrite
    call l2go
    xor a
    ld (nf_run),a
    pop hl
    pop de
    pop bc
    ret
nf_sp:   dw 0
nf_ei:   db 0
nf_rd:   dw 0
nf_run:  db 0
nf_pat:  ds 2
nf_stk:  ds 48
nf_stk_top:
; vcp: $123E-$1275 (from $22FA before the level's first frame, and $2E5C): the 1,600 bytes of VRAM
; from $3800 (the name table just built) read into $C700, then written to $3000 (the other name
; table). Through the traps the reads cost about 1.3 million cycles and the writes 0.6 million. vcp
; copies them from the VRAM copy and writes them with one jt_vwrite, which leaves the VDP as the
; game's last write does. Returns as the loops leave the registers: BC = 0, HL = $CD40, A = 0 with
; Z set, DE kept; interrupts on, as after the routine's EI. Own stack, interrupts off.
vcp:
    di
    ld (vp_sp),sp
    ld sp,vp_stk_top
    push de
    push ix
    push iy
    db $ED,$91,$50,29       ; nextreg $50,29: VRAM $2000-$3FFF in slot 0
    ld hl,$1800
    ld de,$C700
    ld bc,$0640
    ldir
    ld a,(cur_mmu+0)
    db $ED,$92,$50          ; nextreg $50,a
    ld hl,$C700
    ld de,$3000
    ld bc,$4019             ; 25 runs of 64 bytes
    ld ix,64
    ld iy,64
    xor a
    call jt_vwrite
    pop iy
    pop ix
    pop de
    ld hl,$C700+$0640
    ld bc,0
    xor a
    ld sp,(vp_sp)           ; back on the game's stack before interrupts go on again
    ei
    ret
vp_sp:   dw 0
vp_stk:  ds 24
vp_stk_top:
; big: the compositor's path for a count with bit 7 set, $5AC7-$5C5A (from $572C, interrupts off):
; with T = $143 (($C250) = 0) or $161, it writes 5 rows of 4 cells, tiles T to T + 19 (high byte
; 1), from the VRAM address in the list at ($C250) + 1, then 20 tiles from bank 13 at the source
; in the list at + 3 to tile T. Through the traps it cost about 330,000 cycles a call, and the
; level's first steps call it once a step. big writes the cells with one jt_vwrite and the tiles
; that differ from the VRAM copy with vcw, and switches banks through cv_rst18. Returns as the
; game's code leaves the registers: A = the last tile byte, Z and N set, carry clear, B kept,
; C = $BE, D = $40 + (T >> 3), E = 2, HL = the source + 640; in the alternate set C = $BF,
; HL = $C3xx + 4, DE = the source, B kept; IX and IY kept. Interrupts on at the return, as after
; the game's EI. Own stack.
; Runtime internals used: cur_mmu $E02D is public (vcw).
BG_RST18 equ $74D0
big:
    di
    ld (bg_sp),sp
    ld sp,bg_stk_top
    push bc
    push ix
    push iy
    ld a,($C250)
    ld hl,$0143
    or a
    jr z,bg_b0
    ld hl,$0161
bg_b0:
    ld (bg_t),hl
    ld l,a
    ld h,$C3
    inc l
    ld e,(hl)
    inc l
    ld d,(hl)
    inc l
    ld (bg_lp),hl           ; list + 3: the source
    push de                 ; the cells' VRAM address
    ld hl,(bg_t)
    ld ix,bg_buf
    ld b,20
bg_c:
    ld (ix+0),l
    ld (ix+1),h
    inc ix
    inc ix
    inc hl
    djnz bg_c
    pop de
    ld hl,bg_buf
    ld bc,$0805             ; 5 rows of 8 bytes
    ld ix,8
    ld iy,64
    ld a,1
    call jt_vwrite
    ld hl,(bg_lp)
    ld e,(hl)
    inc l
    ld d,(hl)
    ld (bg_src),de
    ld hl,(bg_t)
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld (bg_vt),hl
    ld e,$0D
    call BG_RST18
    ld hl,(bg_src)
    ld de,(bg_vt)
    ld c,20
    call vcw
    ld hl,(bg_src)
    ld de,640
    add hl,de
    ld (bg_end),hl
    dec hl
    ld a,(hl)
    ld (bg_a),a
    ld e,2
    call BG_RST18
    exx
    ld hl,(bg_lp)
    inc l
    ld de,(bg_src)
    ld c,$BF
    exx
    pop iy
    pop ix
    pop bc
    ld c,$BE
    ld a,(bg_vt+1)
    or $40
    ld d,a
    ld hl,(bg_end)
    ld e,1
    dec e                   ; Z and N set
    ld e,2
    ld a,(bg_a)
    scf
    ccf                     ; carry clear
    ld sp,(bg_sp)           ; back on the game's stack before interrupts go on again
    ei
    ret
bg_sp:   dw 0
bg_t:    dw 0
bg_lp:   dw 0
bg_src:  dw 0
bg_vt:   dw 0
bg_end:  dw 0
bg_a:    db 0
bg_buf:  ds 40
bg_stk:  ds 32
bg_stk_top:
; lw: the list writer $5453-$563E (after $544A's LD IX,$C000; LD A,($C253); OR A; RET Z; from
; $2371 once a game step). A = entries at IX, 4 bytes each: (IX+0,1) and (IX+2,3). With bit 5 of
; (IX+1) set, two rows of 4 bytes from the source (IX+2,3) to the VRAM address (IX+0,1) and $40
; on; else 6 tiles from bank 14 at the source to tile (IX+0,1). Through the traps it cost about
; 150,000 cycles a step in the level's first steps. lw writes the rows with one jt_vwrite and the
; tiles that differ from the VRAM copy with vcw. Returns B = 0, C = $BE, DE = 4, HL after the last
; source, IX after the list, IY kept; A and F are not the loop's (the caller's next routine, $5641,
; loads both). Interrupts on at the return, as after the routine's EI. Own stack.
lw:
    di
    ld (lw_sp),sp
    ld sp,lw_stk_top
    push iy
    ld b,a
lw_l:
    push bc
    ld e,(ix+0)
    ld d,(ix+1)
    ld l,(ix+2)
    ld h,(ix+3)
    push ix
    bit 5,d
    jr z,lw_t
    ld bc,$0402
    ld ix,4
    ld iy,64
    xor a                   ; the source as the game sees it
    call jt_vwrite
    ld bc,8
    jr lw_n
lw_t:
    push hl
    ld e,$0E
    call BG_RST18
    pop hl
    ex de,hl                ; DE = the source, HL = the tile
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ex de,hl
    push hl
    ld c,6
    call vcw
    ld e,2
    call BG_RST18
    pop hl
    ld bc,192
lw_n:
    add hl,bc
    ld (lw_hl),hl
    pop ix
    ld de,4
    add ix,de
    pop bc
    djnz lw_l
    pop iy
    ld hl,(lw_hl)
    ld bc,$00BE
    ld sp,(lw_sp)           ; back on the game's stack before interrupts go on again
    ei
    ret
lw_sp:   dw 0
lw_hl:   dw 0
lw_stk:  ds 32
lw_stk_top:
; l2go: the Layer 2 cells that name table writes have marked, drawn at once, as the runtime's
; pri_frame marked-cells pass (pri_rowcells, pri_cell, pri_tile, pri_put; fw2.asm) would draw
; them at its next once-a-frame work: a priority cell gets its tile's pixels on its lines on
; screen, bit 1 of its mark, its tile's bit in pri_tiles and its lines' pri_lf flags; any other
; marked cell that Layer 2 holds (mark bit 1) gets zeros where pri_lf says a line may hold pixels.
; Each mark is cleared, so the runtime draws the cell no more. The runtime's pass cost about 10,600
; cycles a cell; the level's build marks about 400 cells. The pixels come from the Next tile
; definitions, or from the VRAM copy (the planar tile) for a tile that waits for conversion
; (its bit in dirty_pages). Left to the runtime: everything with the priority switch off, in
; 224-line mode, and with a whole rebuild pending (pri_full). Interrupts must be off. Keeps IX and
; IY. Runtime internals:
;   MAP_PAGE 14 (slot 0): row "marked" $1BE0 + row, cell marks $1C00 + cell (bit 0 marked, bit 1
;     Layer 2 holds the cell);
;   SHADOW_PAGE 28, 29 (slots 2, 3: VRAM at $4000); TILE_PAGE 10, 11 (slots 4, 5: tile * 32 + $8000);
;   L2_PAGE 102-107 (slot 6): Layer 2, 32 lines of 256 bytes a page;
;   FW2_PAGE 25 (slot 4 while copied): pri_full $3469, pri_v $346B, pri_ys $346D, pri_lf $3478
;     (192 bytes) and pri_tiles $3538 (64 bytes), copied in and back;
;   part 1: dirty_pages $E440, nt_base $E04B, m224 $E08F, fw_flags $E09E (bit 0: priority), cur_mmu.
l2go:
    ld a,($E09E)
    rra
    ret nc
    ld a,($E08F)
    or a
    ret nz
    nextreg $54,25
    ld a,($8000+$1469)          ; pri_full
    or a
    jp nz,l2_back
    push ix
    ld a,($8000+$146B)
    ld (l2_v),a
    ld a,($8000+$146D)
    ld (l2_ys),a
    ld hl,$8000+$1478
    ld de,l2_lf
    ld bc,256
    ldir
    nextreg $50,14
    nextreg $52,28
    nextreg $53,29
    nextreg $54,10
    nextreg $55,11
    ld a,$FF
    ld (l2_pg),a
    ld b,0
l2_r:
    ld a,b
    add a,$E0
    ld l,a
    ld h,$1B
    ld a,(hl)
    or a
    jr z,l2_rn
    ld (hl),0
    push bc
    call l2_row
    pop bc
l2_rn:
    inc b
    ld a,b
    cp 28
    jr nz,l2_r
    nextreg $54,25
    ld hl,l2_lf
    ld de,$8000+$1478
    ld bc,256
    ldir
    pop ix
l2_back:
    ld a,(cur_mmu+0)
    nextreg $50,a
    ld a,(cur_mmu+2)
    nextreg $52,a
    ld a,(cur_mmu+3)
    nextreg $53,a
    ld a,(cur_mmu+4)
    nextreg $54,a
    ld a,(cur_mmu+5)
    nextreg $55,a
    ld a,(cur_mmu+6)
    nextreg $56,a
    ret
; l2_row: B = row: each marked cell (pri_rowcells)
l2_row:
    ld a,b
    ld (l2_rw),a
    ld l,b
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld de,$1C00
    add hl,de
    ld c,0
l2_c:
    bit 0,(hl)
    jr z,l2_cn
    res 0,(hl)
    push hl
    push bc
    ld a,c
    ld (l2_col),a
    call l2_cell
    pop bc
    pop hl
l2_cn:
    inc hl
    inc c
    ld a,c
    cp 32
    jr nz,l2_c
    ret
; l2_cell: cell (l2_rw, l2_col), HL = its mark (pri_cell)
l2_cell:
    push hl
    ld a,(l2_rw)                ; its entry: nt_base + 64 r + 2 c, at $4000 + that
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,(l2_col)
    add a,a
    add hl,a
    ld de,($E04B)
    add hl,de
    ld a,h
    and $3F
    or $40
    ld h,a
    ld a,(hl)
    ld (l2_tl),a
    inc hl
    ld a,(hl)
    ld (l2_th),a
    pop hl
    and $10
    jr nz,l2_p
    bit 1,(hl)
    ret z                       ; Layer 2 holds nothing of it
    res 1,(hl)
    xor a
    ld (l2_on),a
    jr l2_lines
l2_p:
    set 1,(hl)
    ld a,(l2_tl)                ; pri_tiles: byte (tile >> 3), bit (tile & 7)
    rrca
    rrca
    rrca
    and $1F
    ld e,a
    ld a,(l2_th)
    and 1
    rrca
    rrca
    rrca
    or e
    ld e,a
    ld hl,l2_lf+192
    add hl,a
    ld a,(l2_tl)
    and 7
    ld b,a
    ld a,1
    jr z,l2_b0
l2_bs:
    add a,a
    djnz l2_bs
l2_b0:
    ld c,a
    or (hl)
    ld (hl),a
    ld hl,$E440                 ; dirty_pages: the tile waits for conversion
    ld a,e
    add hl,a
    ld a,c
    and (hl)
    ld (l2_dty),a
    ld a,(l2_th)
    and 1
    ld h,a
    ld a,(l2_tl)
    ld l,a
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld (l2_t32),hl
    ld a,(l2_th)
    and 8
    add a,a
    ld ixl,a                    ; $10: the sprite palette
    ld a,1
    ld (l2_on),a
; the cell's lines on screen
l2_lines:
    ld a,(l2_rw)
    add a,a
    add a,a
    add a,a
    ld (l2_y0),a                ; map line of the cell's top
    ld hl,l2_v                  ; the fast form: all 8 lines on screen, in one Layer 2 page,
    sub (hl)                    ; no wrap of the 192-line ring
    jr nc,l2_f0
    add a,224
l2_f0:
    cp 192-7
    jr nc,l2_sl
    ld hl,l2_ys
    add a,(hl)
    jr c,l2_f1
    cp 192
    jr c,l2_f2
l2_f1:
    sub 192
l2_f2:
    cp 192-7
    jr nc,l2_sl
    ld e,a
    and $1F
    cp 32-7
    jp c,l2_fast
l2_sl:
    ld d,0
l2_k:
    ld a,(l2_y0)
    add a,d
    ld hl,l2_v
    sub (hl)
    jr nc,l2_y
    add a,224
l2_y:
    cp 192
    jp nc,l2_nx
    ld hl,l2_ys
    add a,(hl)
    jr c,l2_w
    cp 192
    jr c,l2_l
l2_w:
    sub 192
l2_l:
    ld e,a                      ; the Layer 2 line
    ld hl,l2_lf
    add hl,a
    ld a,(l2_on)
    or a
    jr nz,l2_lp
    ld a,(hl)
    or a
    jp z,l2_nx                  ; no pixels on that line
    jr l2_pg0
l2_lp:
    ld (hl),1
l2_pg0:
    ld a,e                      ; slot 6 = its Layer 2 page
    rlca
    rlca
    rlca
    and 7
    add a,102
    ld hl,l2_pg
    cp (hl)
    jr z,l2_pg1
    ld (hl),a
    nextreg $56,a
l2_pg1:
    ld a,e
    and $1F
    or $C0
    ld h,a
    ld a,(l2_col)
    add a,a
    add a,a
    add a,a
    ld l,a                      ; HL = the 8 bytes
    ld a,(l2_on)
    or a
    jp nz,l2_px
    xor a
    rept 8
    ld (hl),a
    inc l
    endr
    jp l2_nx
l2_px:
    push de
    ld a,(l2_th)
    ld b,a
    ld a,d                      ; the tile row: D, or 7 - D with V flip
    bit 2,b
    jr z,l2_nv
    xor 7
l2_nv:
    add a,a
    add a,a
    ex de,hl                    ; DE = the destination
    ld hl,(l2_t32)
    add hl,a
    ld a,(l2_dty)
    or a
    jp nz,l2_pl
    ld a,h                      ; the Next definition: 4 bytes, the left pixel in the high nibble
    add a,$80
    ld h,a
    ld c,ixl
    bit 1,b
    jp nz,l2_nf
    rept 4
    ld a,(hl)
    swapnib
    and $0F
    or c
    ld (de),a
    inc e
    ld a,(hl)
    and $0F
    or c
    ld (de),a
    inc e
    inc hl
    endr
    jp l2_pd
l2_nf:
    inc hl
    inc hl
    inc hl
    rept 4
    ld a,(hl)
    and $0F
    or c
    ld (de),a
    inc e
    ld a,(hl)
    swapnib
    and $0F
    or c
    ld (de),a
    inc e
    dec hl
    endr
    jp l2_pd
l2_pl:
    ld a,h                      ; the planar tile in the VRAM copy: 4 bytes, plane 0 first
    add a,$40
    ld h,a
    push bc
    ld a,(hl)
    inc hl
    ld c,(hl)
    inc hl
    ld b,(hl)
    inc hl
    ld l,(hl)
    ld h,b
    ld b,a                      ; B, C, H, L = planes 0-3
    pop af                      ; A = l2_th (from B)
    bit 1,a
    ex de,hl                    ; HL = the destination, D, E = planes 2, 3
    jp nz,l2_pf
    rept 8
    xor a
    sla e
    rla
    sla d
    rla
    sla c
    rla
    sla b
    rla
    or ixl
    ld (hl),a
    inc l
    endr
    jp l2_pd
l2_pf:
    rept 8
    xor a
    srl e
    rla
    srl d
    rla
    srl c
    rla
    srl b
    rla
    or ixl
    ld (hl),a
    inc l
    endr
l2_pd:
    pop de
l2_nx:
    inc d
    ld a,d
    cp 8
    jp nz,l2_k
    ret
; l2_fast: E = the first Layer 2 line; lines E to E + 7 lie in one page and on screen
l2_fast:
    ld a,e                      ; slot 6 = the page
    rlca
    rlca
    rlca
    and 7
    add a,102
    ld hl,l2_pg
    cp (hl)
    jr z,l2_fa0
    ld (hl),a
    nextreg $56,a
l2_fa0:
    ld hl,l2_lf
    ld a,e
    add hl,a
    ld a,e
    and $1F
    or $C0
    ld d,a
    ld a,(l2_col)
    add a,a
    add a,a
    add a,a
    ld e,a                      ; DE = the cell's first line in Layer 2, HL = its pri_lf flag
    ld a,(l2_on)
    or a
    jr nz,l2_fp
    ld b,8                      ; zeros on the lines that may hold pixels
l2_fz:
    ld a,(hl)
    or a
    jr z,l2_fz1
    xor a
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    inc e
    ld (de),a
    ld a,e
    sub 7
    ld e,a
l2_fz1:
    inc hl
    inc d
    djnz l2_fz
    ret
l2_fp:
    ld b,8
l2_fl:
    ld (hl),1
    inc hl
    djnz l2_fl
    ld a,(l2_dty)
    or a
    jr z,l2_fn
    ld a,e                      ; a tile that waits for conversion: line by line from the VRAM copy
    sub e
    ld d,a
    jp l2_k
l2_fn:
    ld a,(l2_th)
    ld b,a
    ld hl,(l2_t32)
    ld a,h
    add a,$80
    ld h,a
    ld c,ixl
    bit 2,b
    jr z,l2_fn0
    ld a,28                     ; V flip: from the last row up
    add hl,a
l2_fn0:
    bit 1,b
    jr nz,l2_fh
    ld a,0                      ; the step after a row: 0, or -8 with V flip
    bit 2,b
    jr z,l2_fn1
    ld a,-8
l2_fn1:
    ld (l2_fa+1),a
    rlca
    sbc a,a
    ld (l2_fa+5),a              ; its high byte
    ld b,8
l2_fr:
    rept 4
    ld a,(hl)
    swapnib
    and $0F
    or c
    ld (de),a
    inc e
    ld a,(hl)
    and $0F
    or c
    ld (de),a
    inc e
    inc hl
    endr
l2_fa:
    ld a,0
    add a,l
    ld l,a
    ld a,0                      ; (the step's high byte)
    adc a,h
    ld h,a
    ld a,e
    sub 8
    ld e,a
    inc d
    djnz l2_fr
    ret
l2_fh:
    inc hl
    inc hl
    inc hl
    ld a,8                      ; the step after a row: 8, or 0 with V flip
    bit 2,b
    jr z,l2_fh1
    xor a
l2_fh1:
    ld (l2_fb+1),a
    ld b,8
l2_fq:
    rept 4
    ld a,(hl)
    and $0F
    or c
    ld (de),a
    inc e
    ld a,(hl)
    swapnib
    and $0F
    or c
    ld (de),a
    inc e
    dec hl
    endr
l2_fb:
    ld a,0
    add a,l
    ld l,a
    ld a,0
    adc a,h
    ld h,a
    ld a,e
    sub 8
    ld e,a
    inc d
    djnz l2_fq
    ret
l2_v:    db 0
l2_ys:   db 0
l2_pg:   db 0
l2_rw:   db 0
l2_col:  db 0
l2_tl:   db 0
l2_th:   db 0
l2_on:   db 0
l2_dty:  db 0
l2_y0:   db 0
l2_t32:  dw 0
l2_lf:   ds 256                 ; pri_lf and pri_tiles while cells are drawn
endpage

# Prince of Persia (Europe, Brazil).cht, "Infinite Life"
poke "Infinite health"
ar 00C2-9208
endpoke
