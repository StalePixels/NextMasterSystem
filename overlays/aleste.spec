# Aleste (Japan) (En), CRC32 D8C4165B, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output with reference I/O logs
# of 600 s (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - Scan entries: $0042, $015A, $0165, $0170, $017B, $0298, $03D3, $03EC,
#   $055F and $1BEA, the VDP routines of bank 0 that no path reaches. Each
#   starts after a RET or a JP and is a whole routine (DI, the VDP address
#   routine, the data port, EI, RET), so their I/O sites are patched.
# - The I/O ports $F0-$F2 are the FM unit: the game looks for it at power on
#   ($00B6) and its sound driver in bank 7 writes it when it is there.
# - The byte scan rows at $0912 (a table of tile numbers), $7FFA (the
#   TMR SEGA header) and bank 4 $9FD3 (graphics) are data.
# - The jump into RAM at bank 7 $8CF0 and the RST $28 at $8CEB are music
#   data that the scanner decodes through the constant call at $803C.
# - The unrolled OUTI runs at $0D77 and $0E09 are entered part way through
#   by a RET to a pushed address; every OUTI in them is a site.
name Aleste
cart D8C4165B
hz 60		; No-Intro region Japan
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
asm 005ED 2   ; IM 1 -> IM 2
    im 2
endasm
asm 0063B 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00649 2   ; IM 1 -> IM 2
    im 2
endasm
site 0001C   ; OTIR
site 00039   ; IN A,($BF)
site 00042   ; IN A,($BF)
site 0004B   ; OUT ($BF),A
site 00050   ; OUT ($BF),A
site 00071   ; OUT ($3F),A
site 00073   ; IN A,($DD)
site 0007D   ; OUT ($3F),A
site 0007F   ; IN A,($DD)
site 00088   ; OUT ($3F),A
site 00098   ; IN A,($BF)
site 0009E   ; IN A,($BF)
site 000A5   ; IN A,($BF)
site 000BB   ; OUT ($3E),A
site 000C3   ; OUT ($F2),A
site 000C6   ; IN A,($F2)
site 000D8   ; OUT ($F2),A
site 000E0   ; OUT ($3E),A
site 000E4   ; IN A,($BF)
site 000F9   ; OUTI
site 000FB   ; OUT ($BF),A
site 00102   ; OUT ($BF),A
site 00106   ; OUT ($BF),A
site 0010E   ; OUT ($BE),A
site 00116   ; OUT ($BF),A
site 0011A   ; OUT ($BF),A
site 0011E   ; OUT ($BE),A
site 00161   ; IN A,($BE)
site 0016C   ; IN A,($BE)
site 00177   ; OUT ($BE),A
site 00182   ; OUT ($BE),A
site 00188   ; OUT ($BF),A
site 0018D   ; OUT ($BF),A
site 00193   ; OUT ($BF),A
site 00198   ; OUT ($BF),A
site 0019E   ; OUT ($BF),A
site 001A3   ; OUT ($BF),A
site 001A9   ; OUT ($BF),A
site 001AE   ; OUT ($BF),A
site 001BC   ; OUT ($BE),A
site 001CE   ; IN A,($BE)
site 001E2   ; OUT ($BE),A
site 00204   ; OUT (C),H
site 00209   ; OUT (C),L
site 0023D   ; OUTI
site 00245   ; OUT (C),A
site 0027D   ; IN A,($BE)
site 00282   ; IN A,($BE)
site 00287   ; OUT ($BE),A
site 0028F   ; OUT ($BE),A
site 002BA   ; IN A,($BE)
site 002BF   ; IN A,($BE)
site 002C4   ; OUT ($BE),A
site 002CA   ; OUT ($BE),A
site 002F9   ; OUT ($BE),A
site 002FF   ; OUT ($BE),A
site 00389   ; OUT ($BE),A
site 00391   ; OUT ($BE),A
site 003C3   ; OUT ($BE),A
site 003C8   ; IN A,($BE)
site 003DC   ; OUT ($BE),A
site 003E2   ; IN A,($BE)
site 003EC   ; OUT ($BE),A
site 003F1   ; OUT ($DF),A
site 003F9   ; OUT (C),D
site 003FB   ; IN A,(C)
site 00400   ; OUT (C),E
site 00402   ; IN A,(C)
site 00407   ; OUT (C),B
site 00441   ; OUT ($DE),A
site 00443   ; IN A,($DC)
site 0047C   ; OUT ($DE),A
site 0047E   ; IN A,($DC)
site 00486   ; IN A,($DD)
site 00493   ; OUT ($DE),A
site 00495   ; IN A,($DC)
site 0049F   ; OUT ($DE),A
site 004A1   ; IN A,($DD)
site 0056E   ; OTIR
site 00578   ; OUT ($BE),A
site 00592   ; OUTI
site 00595   ; IN A,($BE)
site 005A1   ; OUT (C),A
site 005A4   ; IN A,($BE)
site 005C6   ; OUTI
site 005C9   ; IN A,($BE)
site 005CC   ; IN A,($BE)
site 005CF   ; IN A,($BE)
site 005DB   ; OUT (C),A
site 005DE   ; IN A,($BE)
site 005E1   ; IN A,($BE)
site 005E4   ; IN A,($BE)
site 00CFF   ; IN A,($DD)
site 00D34   ; OUT ($BF),A
site 00D38   ; OUT ($BF),A
site 00D41   ; OUT ($BF),A
site 00D45   ; OUT ($BF),A
site 00D68   ; OUT ($BF),A
site 00D6C   ; OUT ($BF),A
site 00D77   ; OUTI
site 00D79   ; OUTI
site 00D7B   ; OUTI
site 00D7D   ; OUTI
site 00D7F   ; OUTI
site 00D81   ; OUTI
site 00D83   ; OUTI
site 00D85   ; OUTI
site 00D87   ; OUTI
site 00D89   ; OUTI
site 00D8B   ; OUTI
site 00D8D   ; OUTI
site 00D8F   ; OUTI
site 00D91   ; OUTI
site 00D93   ; OUTI
site 00D95   ; OUTI
site 00D97   ; OUTI
site 00D99   ; OUTI
site 00D9B   ; OUTI
site 00D9D   ; OUTI
site 00D9F   ; OUTI
site 00DA1   ; OUTI
site 00DA3   ; OUTI
site 00DA5   ; OUTI
site 00DA7   ; OUTI
site 00DA9   ; OUTI
site 00DAB   ; OUTI
site 00DAD   ; OUTI
site 00DAF   ; OUTI
site 00DB1   ; OUTI
site 00DB3   ; OUTI
site 00DB5   ; OUTI
site 00DB7   ; OUTI
site 00DB9   ; OUTI
site 00DBB   ; OUTI
site 00DBD   ; OUTI
site 00DBF   ; OUTI
site 00DC1   ; OUTI
site 00DC3   ; OUTI
site 00DC5   ; OUTI
site 00DC7   ; OUTI
site 00DC9   ; OUTI
site 00DCB   ; OUTI
site 00DCD   ; OUTI
site 00DCF   ; OUTI
site 00DD1   ; OUTI
site 00DD3   ; OUTI
site 00DD5   ; OUTI
site 00DD7   ; OUTI
site 00DD9   ; OUTI
site 00DDB   ; OUTI
site 00DDD   ; OUTI
site 00DDF   ; OUTI
site 00DE1   ; OUTI
site 00DE3   ; OUTI
site 00DE5   ; OUTI
site 00DE7   ; OUTI
site 00DE9   ; OUTI
site 00DEB   ; OUTI
site 00DED   ; OUTI
site 00DEF   ; OUTI
site 00DF1   ; OUTI
site 00DF3   ; OUTI
site 00DF5   ; OUTI
site 00DF9   ; OUT ($BF),A
site 00DFD   ; OUT ($BF),A
site 00E09   ; OUTI
site 00E0B   ; OUTI
site 00E0D   ; OUTI
site 00E0F   ; OUTI
site 00E11   ; OUTI
site 00E13   ; OUTI
site 00E15   ; OUTI
site 00E17   ; OUTI
site 00E19   ; OUTI
site 00E1B   ; OUTI
site 00E1D   ; OUTI
site 00E1F   ; OUTI
site 00E21   ; OUTI
site 00E23   ; OUTI
site 00E25   ; OUTI
site 00E27   ; OUTI
site 00E29   ; OUTI
site 00E2B   ; OUTI
site 00E2D   ; OUTI
site 00E2F   ; OUTI
site 00E31   ; OUTI
site 00E33   ; OUTI
site 00E35   ; OUTI
site 00E37   ; OUTI
site 00E39   ; OUTI
site 00E3B   ; OUTI
site 00E3D   ; OUTI
site 00E3F   ; OUTI
site 00E41   ; OUTI
site 00E43   ; OUTI
site 00E45   ; OUTI
site 00E47   ; OUTI
site 00E49   ; OUTI
site 00E4B   ; OUTI
site 00E4D   ; OUTI
site 00E4F   ; OUTI
site 00E51   ; OUTI
site 00E53   ; OUTI
site 00E55   ; OUTI
site 00E57   ; OUTI
site 00E59   ; OUTI
site 00E5B   ; OUTI
site 00E5D   ; OUTI
site 00E5F   ; OUTI
site 00E61   ; OUTI
site 00E63   ; OUTI
site 00E65   ; OUTI
site 00E67   ; OUTI
site 00E69   ; OUTI
site 00E6B   ; OUTI
site 00E6D   ; OUTI
site 00E6F   ; OUTI
site 00E71   ; OUTI
site 00E73   ; OUTI
site 00E75   ; OUTI
site 00E77   ; OUTI
site 00E79   ; OUTI
site 00E7B   ; OUTI
site 00E7D   ; OUTI
site 00E7F   ; OUTI
site 00E81   ; OUTI
site 00E83   ; OUTI
site 00E85   ; OUTI
site 00E87   ; OUTI
site 00E89   ; OUTI
site 00E8B   ; OUTI
site 00E8D   ; OUTI
site 00E8F   ; OUTI
site 00E91   ; OUTI
site 00E93   ; OUTI
site 00E95   ; OUTI
site 00E97   ; OUTI
site 00E99   ; OUTI
site 00E9B   ; OUTI
site 00E9D   ; OUTI
site 00E9F   ; OUTI
site 00EA1   ; OUTI
site 00EA3   ; OUTI
site 00EA5   ; OUTI
site 00EA7   ; OUTI
site 00EA9   ; OUTI
site 00EAB   ; OUTI
site 00EAD   ; OUTI
site 00EAF   ; OUTI
site 00EB1   ; OUTI
site 00EB3   ; OUTI
site 00EB5   ; OUTI
site 00EB7   ; OUTI
site 00EB9   ; OUTI
site 00EBB   ; OUTI
site 00EBD   ; OUTI
site 00EBF   ; OUTI
site 00EC1   ; OUTI
site 00EC3   ; OUTI
site 00EC5   ; OUTI
site 00EC7   ; OUTI
site 00EC9   ; OUTI
site 00ECB   ; OUTI
site 00ECD   ; OUTI
site 00ECF   ; OUTI
site 00ED1   ; OUTI
site 00ED3   ; OUTI
site 00ED5   ; OUTI
site 00ED7   ; OUTI
site 00ED9   ; OUTI
site 00EDB   ; OUTI
site 00EDD   ; OUTI
site 00EDF   ; OUTI
site 00EE1   ; OUTI
site 00EE3   ; OUTI
site 00EE5   ; OUTI
site 00EE7   ; OUTI
site 00EE9   ; OUTI
site 00EEB   ; OUTI
site 00EED   ; OUTI
site 00EEF   ; OUTI
site 00EF1   ; OUTI
site 00EF3   ; OUTI
site 00EF5   ; OUTI
site 00EF7   ; OUTI
site 00EF9   ; OUTI
site 00EFB   ; OUTI
site 00EFD   ; OUTI
site 00EFF   ; OUTI
site 00F01   ; OUTI
site 00F03   ; OUTI
site 00F05   ; OUTI
site 00F07   ; OUTI
site 00F40   ; OUTI
site 00F42   ; OUTI
site 00F44   ; OUTI
site 00F46   ; OUTI
site 00F48   ; OUTI
site 00F4A   ; OUTI
site 00F4C   ; OUTI
site 00F4E   ; OUTI
site 00F50   ; OUTI
site 00F52   ; OUTI
site 00F54   ; OUTI
site 00F56   ; OUTI
site 00F58   ; OUTI
site 00F5A   ; OUTI
site 00F5C   ; OUTI
site 00F5E   ; OUTI
site 00F60   ; OUTI
site 00F62   ; OUTI
site 00F64   ; OUTI
site 00F66   ; OUTI
site 00F68   ; OUTI
site 00F6A   ; OUTI
site 00F6C   ; OUTI
site 00F6E   ; OUTI
site 00F70   ; OUTI
site 00F72   ; OUTI
site 00F74   ; OUTI
site 00F76   ; OUTI
site 00F78   ; OUTI
site 00F7A   ; OUTI
site 00F7C   ; OUTI
site 00F7E   ; OUTI
site 00F80   ; OUTI
site 00F82   ; OUTI
site 00F84   ; OUTI
site 00F86   ; OUTI
site 00F88   ; OUTI
site 00F8A   ; OUTI
site 00F8C   ; OUTI
site 00F8E   ; OUTI
site 00F90   ; OUTI
site 00F92   ; OUTI
site 00F94   ; OUTI
site 00F96   ; OUTI
site 00F98   ; OUTI
site 00F9A   ; OUTI
site 00F9C   ; OUTI
site 00F9E   ; OUTI
site 00FA0   ; OUTI
site 00FA2   ; OUTI
site 00FA4   ; OUTI
site 00FA6   ; OUTI
site 00FA8   ; OUTI
site 00FAA   ; OUTI
site 00FAC   ; OUTI
site 00FAE   ; OUTI
site 00FB0   ; OUTI
site 00FB2   ; OUTI
site 00FB4   ; OUTI
site 00FB6   ; OUTI
site 00FB8   ; OUTI
site 00FBA   ; OUTI
site 00FBC   ; OUTI
site 00FBE   ; OUTI
site 00FF9   ; OUT (C),E
site 00FFB   ; OUT (C),D
site 00FFF   ; OUTI
site 01001   ; OUTI
site 01003   ; OUTI
site 01005   ; OUTI
site 01007   ; OUTI
site 01009   ; OUTI
site 0100B   ; OUTI
site 0100D   ; OUTI
site 0100F   ; OUTI
site 01011   ; OUTI
site 01013   ; OUTI
site 01015   ; OUTI
site 01017   ; OUTI
site 01019   ; OUTI
site 0101B   ; OUTI
site 0101D   ; OUTI
site 01BEC   ; OUT ($BF),A
site 01BF0   ; OUT ($BF),A
site 01BFA   ; INI
site 01C06   ; OUT ($BF),A
site 01C0A   ; OUT ($BF),A
otir 01C14   ; OUTI
site 01E06   ; OUT ($FF),A
site 03C5B   ; OUT ($BE),A
site 03C62   ; OUT ($BE),A
site 03C6A   ; IN A,($BE)
site 03C71   ; IN A,($BE)
site 06308   ; OUT ($BE),A
site 1C132   ; OUT ($F0),A
site 1C13F   ; OUT ($F1),A
site 1C151   ; OUT ($F0),A
site 1C158   ; OUT ($F1),A
site 1C161   ; OUT ($F1),A
site 1C176   ; OUT ($F0),A
site 1C17A   ; OUT ($F1),A
site 1C189   ; OUT ($F0),A
site 1C18E   ; OUT ($F1),A
site 1C19A   ; OUT ($F1),A
site 1C1AD   ; OUT ($F0),A
site 1C1B1   ; OUT ($F1),A
site 1C1D1   ; OUT ($F0),A
site 1C1D6   ; OUT ($F1),A
site 1C1EB   ; OUT ($7F),A
site 1C1F1   ; OUT ($7F),A
site 1C1FD   ; OUT ($7F),A
site 1C21A   ; OUT ($7F),A
site 1C223   ; OUT ($7F),A
site 1C828   ; OUT ($F0),A
site 1C82C   ; OUT ($F1),A
site 1C83D   ; OUT ($F2),A
mapst 00817   ; LD ($FFFF),A
mapst 00826   ; LD ($FFFF),A
mapst 00830   ; LD ($FFFF),A
mapst 00837   ; LD ($FFFF),A
mapst 0085D   ; LD ($FFFF),A
mapst 00867   ; LD ($FFFF),A
mapst 00871   ; LD ($FFFF),A
mapst 00878   ; LD ($FFFF),A
mapst 00882   ; LD ($FFFF),A
mapst 0088C   ; LD ($FFFF),A
mapst 0089A   ; LD ($FFFF),A
mapst 008A1   ; LD ($FFFF),A
mapst 01055   ; LD ($FFFF),A
mapst 0106F   ; LD ($FFFF),A
mapst 01083   ; LD ($FFFF),A
mapst 0108A   ; LD ($FFFF),A
mapst 0145B   ; LD ($FFFF),A
mapst 014CF   ; LD ($FFFF),A
mapst 01773   ; LD ($FFFF),A
mapst 01C28   ; LD ($FFFF),A
mapst 01CD1   ; LD ($FFFF),A
mapst 01CE5   ; LD ($FFFF),A
mapst 01D4F   ; LD ($FFFF),A
mapst 02B7F   ; LD ($FFFF),A
mapst 02C3D   ; LD ($FFFF),A

# Aleste (Japan).cht, "Infinite Lives": RAM $C812 holds the lives count
poke "Infinite lives"
ar 00C8-1203
endpoke

# Aleste (Japan).cht, "Start with ?? Lives, instead of 3": the patched byte is the lives count
# a new game starts with (3 in the cartridge)
poke "Start lives ??"
gg ??A-CBF-E66
endpoke

# Aleste (Japan).cht, "Simi-Invulnerability": RAM $C405 held at $80 makes the ship take no hits
poke "Invincibility"
ar 00C4-0580
endpoke

# Aleste (Japan).cht, "Round Modifier": RAM $C881 is the round; 01 is the first round, and 02
# to 05 start the second to the fifth
poke "Start round ??"
ar 00C8-81??
endpoke

# Aleste (Japan).cht, "Max Regular Weapon Power": RAM $C813, $C815 and $C816 hold the regular
# weapon's power; at these values the ship fires more shots
poke "Max weapon power"
ar 00C8-1308
ar 00C8-1503
ar 00C8-1604
endpoke

# Aleste (Japan).cht, "Regular Weapon Powers-up ?? faster": the patched byte is 5 in the
# cartridge; lower values make the weapon power up from fewer pickups
poke "Faster power-up ??"
gg ??8-48B-F7E
endpoke

# Aleste (Japan).cht, "Keep Regular Weapon Power after Dying"
poke "Keep weapon power"
gg 3AF-A9A-2A2
endpoke

# Aleste (Japan).cht, "Infinite Special Weapon": RAM $C83E holds the special weapon's ammunition
poke "Infinite special"
ar 00C8-3E64
endpoke

# Aleste (Japan).cht, "Special Weapon Modifier": RAM $C83C holds the special weapon; 01 to 04
# give four different shots
poke "Special weapon ??"
ar 00C8-3C??
endpoke

# Aleste (Japan).cht, "Max Special Weapon Power": RAM $C840 holds the special weapon's power
poke "Max special power"
ar 00C8-4003
endpoke

# Aleste (Japan).cht, "Keep Special Weapon Power after Dying and Special Weapon Pickups that are
# Different than your Current Special Weapon don't Decrease Special Weapon Power": the two
# patches work together
poke "Keep special power"
gg 3A6-3BB-2A2
gg 3A6-69B-2A2
endpoke

# Aleste (Japan).cht, "Always Fight Power-Up Pods": with RAM $C826 held at 1, power-up pickups
# appear far more often
poke "Power-up pods"
ar 00C8-2601
endpoke

# Aleste (Japan).cht, "Temporary Invincibility after Dying and at Start of Level Lasts ?? Longer":
# the patched byte is loaded into the timer at RAM $C416 after a death and at the start of a
# level (3C in the cartridge)
poke "Respawn shield ??"
gg ??F-18C-19A
endpoke
