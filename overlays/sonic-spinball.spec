# Sonic Spinball (Europe, Brazil) (En), CRC32 11C1BC8A, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, scanned with the entry 1:4362 and
# reference I/O logs.
# Decisions:
# - The reset code at $02C4 pushes $4362 (bank 1) and the RET at $03BA after the VDP
#   set-up goes there: the main code starts in bank 1.
# - No free RST vector ($0020, $0030 and $0038 are the game's), so $0000 is the io vector.
#   The game runs no RST $00. Its resets are JP $0000 ($1955, $1969, $19B1, $1A0E, $1A63,
#   $1AE5, $1D80, $1D90, $3A3F); the io vector at $00 turns each into the start.
# - The unrolled run of 384 OUTI at $1FD1-$22D0 (C = $BE) is entered at $22D1 minus 64
#   bytes per tile, through the RET at $1FD0: every OUTI is a site.
# - Banks 1, 2, 4, 5, 7 and 30 each end with the same name table clear at $7FC3; the sites
#   of every copy are patched. Bank 30 also holds a line interrupt set-up (cart offsets
#   $7B8C0-$7B915) and a 32-byte palette write ($7BDA0-$7BDB6), both code that no scanned
#   path reaches: patched.
# - The VRAM word read at $145C (OUT (C),L; OUT (C),A; IN A,(C) twice) and the joypad
#   read at cart offset $17EC6 (bank 5) are code that no scanned path reaches: patched.
# - $3BB3 is the twin of $3BA7 (LD A,($C825); DI; LD ($FFFE),A ... with carry set): its
#   mapper store is patched.
# - The other byte patterns that no path reached are tables, graphics or operand bytes
#   (verdict false in data/scan-verdicts.tsv).
# - $1E02 is not a site. The scan reads the jump table of $2CFD at $4028 in bank 1, but
#   bank 1 holds code there; its fifth word, $1E02, falls inside LD A,($D38D) / LD C,A
#   ($1E00-$1E03) of the sprite list build, and a patch there breaks the build.
name Sonic Spinball
cart 11C1BC8A
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
start 0003
site 0008C   ; IN A,($BF)
site 000BB   ; OUT ($BF),A
site 000BF   ; OUT ($BF),A
site 000E4   ; OUT ($BF),A
site 000E8   ; OUT ($BF),A
site 000FC   ; OUT ($BF),A
site 00100   ; OUT ($BF),A
site 0010A   ; OUT ($BF),A
site 0010E   ; OUT ($BF),A
site 0011C   ; OUT ($BF),A
site 00120   ; OUT ($BF),A
site 00128   ; OUT ($BF),A
site 0012C   ; OUT ($BF),A
site 00141   ; IN A,($DD)
site 00150   ; OUT ($BF),A
site 00154   ; OUT ($BF),A
site 00192   ; OUT ($BF),A
site 00196   ; OUT ($BF),A
site 001CB   ; OUT ($BF),A
site 001CF   ; OUT ($BF),A
site 001E3   ; OUT ($BF),A
site 001E7   ; OUT ($BF),A
site 001EE   ; OUT ($BF),A
site 001F2   ; OUT ($BF),A
site 00201   ; IN A,($7E)
site 00235   ; OUT ($BF),A
site 00239   ; OUT ($BF),A
site 0023E   ; OUT ($BE),A
site 0025B   ; OUT ($BF),A
site 0025F   ; OUT ($BF),A
site 002D3   ; IN A,($7E)
site 002FD   ; IN A,($BE)
site 00300   ; OUT ($BF),A
site 00304   ; OUT ($BF),A
site 0030A   ; OUT ($BE),A
site 0031E   ; OUT ($BF),A
site 00324   ; OUT ($BF),A
site 00333   ; OUT ($BF),A
site 00337   ; OUT ($BF),A
site 00344   ; OUT ($BF),A
site 00348   ; OUT ($BF),A
site 0038D   ; OUT ($BF),A
site 00391   ; OUT ($BF),A
site 00398   ; OUT ($BF),A
site 0039C   ; OUT ($BF),A
site 003A3   ; OUT ($BF),A
site 003A7   ; OUT ($BF),A
site 003B3   ; OUT ($BF),A
site 003B7   ; OUT ($BF),A
site 003D8   ; OUT ($BF),A
site 003DC   ; OUT ($BF),A
site 0047A   ; OUT ($BF),A
site 0047E   ; OUT ($BF),A
site 004ED   ; OUT ($BF),A
site 004F1   ; OUT ($BF),A
site 004FB   ; OUT ($BF),A
site 004FF   ; OUT ($BF),A
site 0050F   ; OUT ($BF),A
site 00513   ; OUT ($BF),A
site 00744   ; OUT ($BF),A
site 00748   ; OUT ($BF),A
site 00754   ; OUT ($BF),A
site 00758   ; OUT ($BF),A
site 007E6   ; OUT ($BF),A
site 007EA   ; OUT ($BF),A
site 00870   ; OUT ($BF),A
site 00873   ; OUT ($BF),A
site 0087E   ; OUTI
site 00883   ; OUTI
site 0088E   ; OUT ($BF),A
site 008A0   ; OUT ($BF),A
site 008A7   ; OUT ($BF),A
site 00CF2   ; OUT (C),L
site 00CF4   ; OUT (C),H
site 00CF9   ; OUT ($BE),A
site 00D00   ; OUT ($BE),A
site 00D7C   ; OUT (C),E
site 00D7E   ; OUT (C),D
site 00D9D   ; OUTI
site 00DA1   ; OUTI
site 0107A   ; OUT ($BF),A
site 0107E   ; OUT ($BF),A
site 01081   ; OUT ($BE),A
site 0115C   ; OUT ($BF),A
site 01161   ; OUT ($BF),A
site 01164   ; OUT ($BE),A
site 01183   ; OUT ($BF),A
site 01187   ; OUT ($BF),A
site 01193   ; OUT ($BF),A
site 01197   ; OUT ($BF),A
site 0119F   ; OUT ($BF),A
site 011A3   ; OUT ($BF),A
site 011DB   ; OUT ($BF),A
site 011DF   ; OUT ($BF),A
site 011F4   ; OUT ($BF),A
site 011F8   ; OUT ($BF),A
site 01304   ; OUT ($BF),A
site 01308   ; OUT ($BF),A
site 01328   ; OUT ($BF),A
site 0132C   ; OUT ($BF),A
site 01336   ; OUT ($BF),A
site 0133A   ; OUT ($BF),A
site 01442   ; OUT (C),L
site 01444   ; OUT (C),A
site 01447   ; OUT (C),D
site 0144D   ; OUT (C),E
site 0149D   ; OUT ($BF),A
site 014A2   ; OUT ($BF),A
site 014A7   ; IN A,($BE)
site 014D4   ; OUT ($BF),A
site 014D9   ; OUT ($BF),A
site 014DF   ; OUT ($BE),A
site 01510   ; OUT ($BF),A
site 01514   ; OUT ($BF),A
site 01528   ; OUT ($BF),A
site 0152C   ; OUT ($BF),A
site 01541   ; OUT ($BF),A
site 01545   ; OUT ($BF),A
site 01559   ; OUT ($BF),A
site 0155D   ; OUT ($BF),A
site 01AB6   ; OUT (C),L
site 01AB8   ; OUT (C),H
site 01ABD   ; OUT ($BE),A
site 01F9F   ; OUT ($BF),A
site 01FA3   ; OUT ($BF),A
site 01FC4   ; OUT (C),L
site 01FC6   ; OUT (C),H
site 01FD1   ; OUTI
site 01FD3   ; OUTI
site 01FD5   ; OUTI
site 01FD7   ; OUTI
site 01FD9   ; OUTI
site 01FDB   ; OUTI
site 01FDD   ; OUTI
site 01FDF   ; OUTI
site 01FE1   ; OUTI
site 01FE3   ; OUTI
site 01FE5   ; OUTI
site 01FE7   ; OUTI
site 01FE9   ; OUTI
site 01FEB   ; OUTI
site 01FED   ; OUTI
site 01FEF   ; OUTI
site 01FF1   ; OUTI
site 01FF3   ; OUTI
site 01FF5   ; OUTI
site 01FF7   ; OUTI
site 01FF9   ; OUTI
site 01FFB   ; OUTI
site 01FFD   ; OUTI
site 01FFF   ; OUTI
site 02001   ; OUTI
site 02003   ; OUTI
site 02005   ; OUTI
site 02007   ; OUTI
site 02009   ; OUTI
site 0200B   ; OUTI
site 0200D   ; OUTI
site 0200F   ; OUTI
site 02011   ; OUTI
site 02013   ; OUTI
site 02015   ; OUTI
site 02017   ; OUTI
site 02019   ; OUTI
site 0201B   ; OUTI
site 0201D   ; OUTI
site 0201F   ; OUTI
site 02021   ; OUTI
site 02023   ; OUTI
site 02025   ; OUTI
site 02027   ; OUTI
site 02029   ; OUTI
site 0202B   ; OUTI
site 0202D   ; OUTI
site 0202F   ; OUTI
site 02031   ; OUTI
site 02033   ; OUTI
site 02035   ; OUTI
site 02037   ; OUTI
site 02039   ; OUTI
site 0203B   ; OUTI
site 0203D   ; OUTI
site 0203F   ; OUTI
site 02041   ; OUTI
site 02043   ; OUTI
site 02045   ; OUTI
site 02047   ; OUTI
site 02049   ; OUTI
site 0204B   ; OUTI
site 0204D   ; OUTI
site 0204F   ; OUTI
site 02051   ; OUTI
site 02053   ; OUTI
site 02055   ; OUTI
site 02057   ; OUTI
site 02059   ; OUTI
site 0205B   ; OUTI
site 0205D   ; OUTI
site 0205F   ; OUTI
site 02061   ; OUTI
site 02063   ; OUTI
site 02065   ; OUTI
site 02067   ; OUTI
site 02069   ; OUTI
site 0206B   ; OUTI
site 0206D   ; OUTI
site 0206F   ; OUTI
site 02071   ; OUTI
site 02073   ; OUTI
site 02075   ; OUTI
site 02077   ; OUTI
site 02079   ; OUTI
site 0207B   ; OUTI
site 0207D   ; OUTI
site 0207F   ; OUTI
site 02081   ; OUTI
site 02083   ; OUTI
site 02085   ; OUTI
site 02087   ; OUTI
site 02089   ; OUTI
site 0208B   ; OUTI
site 0208D   ; OUTI
site 0208F   ; OUTI
site 02091   ; OUTI
site 02093   ; OUTI
site 02095   ; OUTI
site 02097   ; OUTI
site 02099   ; OUTI
site 0209B   ; OUTI
site 0209D   ; OUTI
site 0209F   ; OUTI
site 020A1   ; OUTI
site 020A3   ; OUTI
site 020A5   ; OUTI
site 020A7   ; OUTI
site 020A9   ; OUTI
site 020AB   ; OUTI
site 020AD   ; OUTI
site 020AF   ; OUTI
site 020B1   ; OUTI
site 020B3   ; OUTI
site 020B5   ; OUTI
site 020B7   ; OUTI
site 020B9   ; OUTI
site 020BB   ; OUTI
site 020BD   ; OUTI
site 020BF   ; OUTI
site 020C1   ; OUTI
site 020C3   ; OUTI
site 020C5   ; OUTI
site 020C7   ; OUTI
site 020C9   ; OUTI
site 020CB   ; OUTI
site 020CD   ; OUTI
site 020CF   ; OUTI
site 020D1   ; OUTI
site 020D3   ; OUTI
site 020D5   ; OUTI
site 020D7   ; OUTI
site 020D9   ; OUTI
site 020DB   ; OUTI
site 020DD   ; OUTI
site 020DF   ; OUTI
site 020E1   ; OUTI
site 020E3   ; OUTI
site 020E5   ; OUTI
site 020E7   ; OUTI
site 020E9   ; OUTI
site 020EB   ; OUTI
site 020ED   ; OUTI
site 020EF   ; OUTI
site 020F1   ; OUTI
site 020F3   ; OUTI
site 020F5   ; OUTI
site 020F7   ; OUTI
site 020F9   ; OUTI
site 020FB   ; OUTI
site 020FD   ; OUTI
site 020FF   ; OUTI
site 02101   ; OUTI
site 02103   ; OUTI
site 02105   ; OUTI
site 02107   ; OUTI
site 02109   ; OUTI
site 0210B   ; OUTI
site 0210D   ; OUTI
site 0210F   ; OUTI
site 02111   ; OUTI
site 02113   ; OUTI
site 02115   ; OUTI
site 02117   ; OUTI
site 02119   ; OUTI
site 0211B   ; OUTI
site 0211D   ; OUTI
site 0211F   ; OUTI
site 02121   ; OUTI
site 02123   ; OUTI
site 02125   ; OUTI
site 02127   ; OUTI
site 02129   ; OUTI
site 0212B   ; OUTI
site 0212D   ; OUTI
site 0212F   ; OUTI
site 02131   ; OUTI
site 02133   ; OUTI
site 02135   ; OUTI
site 02137   ; OUTI
site 02139   ; OUTI
site 0213B   ; OUTI
site 0213D   ; OUTI
site 0213F   ; OUTI
site 02141   ; OUTI
site 02143   ; OUTI
site 02145   ; OUTI
site 02147   ; OUTI
site 02149   ; OUTI
site 0214B   ; OUTI
site 0214D   ; OUTI
site 0214F   ; OUTI
site 02151   ; OUTI
site 02153   ; OUTI
site 02155   ; OUTI
site 02157   ; OUTI
site 02159   ; OUTI
site 0215B   ; OUTI
site 0215D   ; OUTI
site 0215F   ; OUTI
site 02161   ; OUTI
site 02163   ; OUTI
site 02165   ; OUTI
site 02167   ; OUTI
site 02169   ; OUTI
site 0216B   ; OUTI
site 0216D   ; OUTI
site 0216F   ; OUTI
site 02171   ; OUTI
site 02173   ; OUTI
site 02175   ; OUTI
site 02177   ; OUTI
site 02179   ; OUTI
site 0217B   ; OUTI
site 0217D   ; OUTI
site 0217F   ; OUTI
site 02181   ; OUTI
site 02183   ; OUTI
site 02185   ; OUTI
site 02187   ; OUTI
site 02189   ; OUTI
site 0218B   ; OUTI
site 0218D   ; OUTI
site 0218F   ; OUTI
site 02191   ; OUTI
site 02193   ; OUTI
site 02195   ; OUTI
site 02197   ; OUTI
site 02199   ; OUTI
site 0219B   ; OUTI
site 0219D   ; OUTI
site 0219F   ; OUTI
site 021A1   ; OUTI
site 021A3   ; OUTI
site 021A5   ; OUTI
site 021A7   ; OUTI
site 021A9   ; OUTI
site 021AB   ; OUTI
site 021AD   ; OUTI
site 021AF   ; OUTI
site 021B1   ; OUTI
site 021B3   ; OUTI
site 021B5   ; OUTI
site 021B7   ; OUTI
site 021B9   ; OUTI
site 021BB   ; OUTI
site 021BD   ; OUTI
site 021BF   ; OUTI
site 021C1   ; OUTI
site 021C3   ; OUTI
site 021C5   ; OUTI
site 021C7   ; OUTI
site 021C9   ; OUTI
site 021CB   ; OUTI
site 021CD   ; OUTI
site 021CF   ; OUTI
site 021D1   ; OUTI
site 021D3   ; OUTI
site 021D5   ; OUTI
site 021D7   ; OUTI
site 021D9   ; OUTI
site 021DB   ; OUTI
site 021DD   ; OUTI
site 021DF   ; OUTI
site 021E1   ; OUTI
site 021E3   ; OUTI
site 021E5   ; OUTI
site 021E7   ; OUTI
site 021E9   ; OUTI
site 021EB   ; OUTI
site 021ED   ; OUTI
site 021EF   ; OUTI
site 021F1   ; OUTI
site 021F3   ; OUTI
site 021F5   ; OUTI
site 021F7   ; OUTI
site 021F9   ; OUTI
site 021FB   ; OUTI
site 021FD   ; OUTI
site 021FF   ; OUTI
site 02201   ; OUTI
site 02203   ; OUTI
site 02205   ; OUTI
site 02207   ; OUTI
site 02209   ; OUTI
site 0220B   ; OUTI
site 0220D   ; OUTI
site 0220F   ; OUTI
site 02211   ; OUTI
site 02213   ; OUTI
site 02215   ; OUTI
site 02217   ; OUTI
site 02219   ; OUTI
site 0221B   ; OUTI
site 0221D   ; OUTI
site 0221F   ; OUTI
site 02221   ; OUTI
site 02223   ; OUTI
site 02225   ; OUTI
site 02227   ; OUTI
site 02229   ; OUTI
site 0222B   ; OUTI
site 0222D   ; OUTI
site 0222F   ; OUTI
site 02231   ; OUTI
site 02233   ; OUTI
site 02235   ; OUTI
site 02237   ; OUTI
site 02239   ; OUTI
site 0223B   ; OUTI
site 0223D   ; OUTI
site 0223F   ; OUTI
site 02241   ; OUTI
site 02243   ; OUTI
site 02245   ; OUTI
site 02247   ; OUTI
site 02249   ; OUTI
site 0224B   ; OUTI
site 0224D   ; OUTI
site 0224F   ; OUTI
site 02251   ; OUTI
site 02253   ; OUTI
site 02255   ; OUTI
site 02257   ; OUTI
site 02259   ; OUTI
site 0225B   ; OUTI
site 0225D   ; OUTI
site 0225F   ; OUTI
site 02261   ; OUTI
site 02263   ; OUTI
site 02265   ; OUTI
site 02267   ; OUTI
site 02269   ; OUTI
site 0226B   ; OUTI
site 0226D   ; OUTI
site 0226F   ; OUTI
site 02271   ; OUTI
site 02273   ; OUTI
site 02275   ; OUTI
site 02277   ; OUTI
site 02279   ; OUTI
site 0227B   ; OUTI
site 0227D   ; OUTI
site 0227F   ; OUTI
site 02281   ; OUTI
site 02283   ; OUTI
site 02285   ; OUTI
site 02287   ; OUTI
site 02289   ; OUTI
site 0228B   ; OUTI
site 0228D   ; OUTI
site 0228F   ; OUTI
site 02291   ; OUTI
site 02293   ; OUTI
site 02295   ; OUTI
site 02297   ; OUTI
site 02299   ; OUTI
site 0229B   ; OUTI
site 0229D   ; OUTI
site 0229F   ; OUTI
site 022A1   ; OUTI
site 022A3   ; OUTI
site 022A5   ; OUTI
site 022A7   ; OUTI
site 022A9   ; OUTI
site 022AB   ; OUTI
site 022AD   ; OUTI
site 022AF   ; OUTI
site 022B1   ; OUTI
site 022B3   ; OUTI
site 022B5   ; OUTI
site 022B7   ; OUTI
site 022B9   ; OUTI
site 022BB   ; OUTI
site 022BD   ; OUTI
site 022BF   ; OUTI
site 022C1   ; OUTI
site 022C3   ; OUTI
site 022C5   ; OUTI
site 022C7   ; OUTI
site 022C9   ; OUTI
site 022CB   ; OUTI
site 022CD   ; OUTI
site 022CF   ; OUTI
site 02307   ; OUT (C),L
site 02309   ; OUT (C),H
site 0231C   ; OTIR
site 02323   ; OUT (C),L
site 02325   ; OUT (C),H
site 02332   ; OTIR
site 03C7E   ; OUT ($BF),A
site 03C82   ; OUT ($BF),A
site 03C91   ; OUT ($BE),A
site 03C9F   ; OUT ($BF),A
site 03CA3   ; OUT ($BF),A
site 03CAB   ; OUT ($BE),A
site 03CB9   ; OUT ($BE),A
site 03FBA   ; OTIR
site 0437C   ; IN A,($DC)
site 043B3   ; OUT ($BF),A
site 043B7   ; OUT ($BF),A
site 043D1   ; IN A,($DC)
site 04451   ; OUT ($BF),A
site 04455   ; OUT ($BF),A
site 04822   ; OUT (C),E
site 04824   ; OUT (C),D
site 04828   ; INI
site 0482C   ; INI
site 0484C   ; OUT (C),E
site 0484E   ; OUT (C),D
site 04852   ; OUTI
site 04856   ; OUTI
site 04884   ; OTIR
site 048A6   ; OUT ($BF),A
site 048AA   ; OUT ($BF),A
site 048AE   ; OUT ($BE),A
site 048B6   ; OUT ($BF),A
site 048BA   ; OUT ($BF),A
site 048BE   ; OUT ($BE),A
site 04BB9   ; OUT ($BF),A
site 04BBD   ; OUT ($BF),A
site 04BC1   ; OUT ($BE),A
site 04BC9   ; OUT ($BF),A
site 04BCD   ; OUT ($BF),A
site 04BD1   ; OUT ($BE),A
site 050C7   ; OUT ($BF),A
site 050CC   ; OUT ($BF),A
site 050D2   ; OUT ($BE),A
site 0541A   ; IN A,($DC)
site 05B89   ; OUT ($BF),A
site 05B8D   ; OUT ($BF),A
site 0691F   ; OUT ($BF),A
site 06923   ; OUT ($BF),A
site 077C1   ; OUT ($BF),A
site 077C5   ; OUT ($BF),A
site 0780A   ; IN A,($7E)
site 07863   ; IN A,($DC)
site 07FC4   ; IN A,($BE)
site 07FC9   ; OUT ($BF),A
site 07FD0   ; OUT ($BF),A
site 07FD6   ; OUT ($BE),A
site 0925C   ; OUT ($BF),A
site 09261   ; OUT ($BF),A
site 09349   ; OUT ($BE),A
site 09355   ; OUT ($BE),A
site 0936C   ; OUT ($BE),A
site 09374   ; OUT ($BE),A
site 09390   ; OUT ($BE),A
site 09398   ; OUT ($BE),A
site 093A0   ; OUT ($BE),A
site 093C1   ; OUT ($BE),A
site 093C9   ; OUT ($BE),A
site 093D1   ; OUT ($BE),A
site 093D9   ; OUT ($BE),A
site 093E7   ; OUT ($BE),A
site 09406   ; OUT ($BF),A
site 09409   ; OUT ($BF),A
site 09411   ; IN A,($BE)
site 0941B   ; OUT ($BF),A
site 09420   ; OUT ($BF),A
site 09429   ; OUT ($BE),A
site 0C4A4   ; OUT ($7F),A
site 0C4B9   ; OUT ($7F),A
site 0C4C2   ; OUT ($7F),A
site 0C4CD   ; OUT ($7F),A
site 0C4F8   ; OUT ($7F),A
site 0C6AA   ; OUT ($7F),A
site 0C6E1   ; OUT ($7F),A
site 0C6EA   ; OUT ($7F),A
site 0C705   ; OUT ($7F),A
site 0C709   ; OUT ($7F),A
site 0C7BF   ; OUT ($7F),A
site 0C7D5   ; OUT ($7F),A
site 0C7ED   ; OUT ($7F),A
site 0C7F1   ; OUT ($7F),A
site 0C7FF   ; OUT ($7F),A
site 0C83D   ; OUT ($7F),A
site 0C853   ; OUT ($7F),A
site 0C857   ; OUT ($7F),A
site 1CE41   ; OUT (C),L
site 1CE43   ; OUT (C),A
site 1CE46   ; OUT (C),D
site 1CE4C   ; OUT (C),E
mapst 00085   ; LD ($FFFE),A
mapst 00158   ; LD ($FFFD),A
mapst 00164   ; LD ($FFFE),A
mapst 00220   ; LD ($FFFE),A
mapst 00248   ; LD ($FFFE),A
mapst 00271   ; LD ($FFFF),A
mapst 00284   ; LD ($FFFF),A
mapst 002A2   ; LD ($FFFE),A
mapst 002B3   ; LD ($FFFE),A
mapldk 002D9   # LD HL,$FFFC; LD (HL),$80
mapst 002E0   ; LD ($FFFD),A
mapst 002E8   ; LD ($FFFE),A
mapst 002F0   ; LD ($FFFF),A
mapst 0036D   ; LD ($FFFD),A
mapst 00375   ; LD ($FFFE),A
mapst 0037D   ; LD ($FFFF),A
mapst 003CD   ; LD ($FFFE),A
mapst 00422   ; LD ($FFFE),A
mapst 0042F   ; LD ($FFFE),A
mapst 00457   ; LD ($FFFE),A
mapst 004BD   ; LD ($FFFE),A
mapst 004C8   ; LD ($FFFE),A
mapst 007FD   ; LD ($FFFF),A
mapst 00C7D   ; LD ($FFFF),A
mapst 00D33   ; LD ($FFFF),A
mapst 00FEE   ; LD ($FFFF),A
mapst 01010   ; LD ($FFFF),A
mapst 010A2   ; LD ($FFFF),A
mapst 01173   ; LD ($FFFF),A
mapst 0121A   ; LD ($FFFF),A
mapst 018FC   ; LD ($FFFE),A
mapst 01925   ; LD ($FFFE),A
mapst 019DF   ; LD ($FFFE),A
mapst 01A19   ; LD ($FFFE),A
mapst 01A2F   ; LD ($FFFE),A
mapst 01A3E   ; LD ($FFFF),A
mapst 01AC6   ; LD ($FFFE),A
mapst 01CEC   ; LD ($FFFE),A
mapst 01CF6   ; LD ($FFFE),A
mapst 01DCA   ; LD ($FFFF),A
mapst 01F0A   ; LD ($FFFF),A
mapst 01F75   ; LD ($FFFF),A
mapst 022D2   ; LD ($FFFF),A
mapst 02384   ; LD ($FFFF),A
mapst 023A9   ; LD ($FFFE),A
mapst 023B5   ; LD ($FFFE),A
mapst 023BC   ; LD ($FFFF),A
mapst 02B97   ; LD ($FFFE),A
mapst 02BA0   ; LD ($FFFF),A
mapst 02BCF   ; LD ($FFFE),A
mapst 02C30   ; LD ($FFFE),A
mapst 02DAB   ; LD ($FFFE),A
mapst 02E03   ; LD ($FFFE),A
mapst 02F2F   ; LD ($FFFE),A
mapst 03459   ; LD ($FFFE),A
mapst 03528   ; LD ($FFFE),A
mapst 0353D   ; LD ($FFFE),A
mapst 03608   ; LD ($FFFE),A
mapst 036D8   ; LD ($FFFE),A
mapst 0375D   ; LD ($FFFE),A
mapst 03925   ; LD ($FFFE),A
mapst 0392E   ; LD ($FFFE),A
mapst 03A0A   ; LD ($FFFE),A
mapst 03A28   ; LD ($FFFE),A
mapst 03BAA   ; LD ($FFFE),A
mapst 03C40   ; LD ($FFFF),A
mapst 03DDA   ; LD ($FFFE),A
mapst 03DE2   ; LD ($FFFF),A
mapst 03E22   ; LD ($FFFE),A
mapst 03E2A   ; LD ($FFFF),A
mapst 03E5D   ; LD ($FFFF),A
mapst 03E66   ; LD ($FFFE),A
mapst 03E75   ; LD ($FFFF),A
mapst 03E7E   ; LD ($FFFE),A
mapst 03EB8   ; LD ($FFFF),A
mapst 03ED2   ; LD ($FFFF),A
mapst 03F18   ; LD ($FFFF),A
mapst 04600   ; LD ($FFFE),A
mapst 0461B   ; LD ($FFFE),A
mapst 04646   ; LD ($FFFE),A
mapst 04696   ; LD ($FFFE),A
mapst 046E7   ; LD ($FFFE),A
mapst 04707   ; LD ($FFFE),A
mapst 0495F   ; LD ($FFFF),A
mapst 04A64   ; LD ($FFFF),A
mapst 04C26   ; LD ($FFFF),A
mapst 05110   ; LD ($FFFF),A
mapst 064D7   ; LD ($FFFF),A
mapst 0776D   ; LD ($FFFF),A
mapst 07782   ; LD ($FFFF),A
mapldk 07810   # LD HL,$FFFC; LD (HL),$80
mapst 07817   ; LD ($FFFD),A
mapst 0781F   ; LD ($FFFE),A
mapst 07827   ; LD ($FFFF),A
mapst 07F82   ; LD ($FFFF),A
mapst 18250   ; LD ($FFFF),A
mapst 182A2   ; LD ($FFFF),A
mapst 182EF   ; LD ($FFFF),A
mapst 18343   ; LD ($FFFF),A
mapst 183D1   ; LD ($FFFF),A
mapst 18423   ; LD ($FFFF),A
mapst 18470   ; LD ($FFFF),A
mapst 184C4   ; LD ($FFFF),A
mapst 00DC6   # LD ($FFFF),A; after LD A,($C844); 32 bytes of valid code before it
mapst 0BF82   # LD ($FFFF),A; after LD A,$1A; 32 bytes of valid code before it
mapst 13F82   # LD ($FFFF),A; after LD A,$1A; 32 bytes of valid code before it
mapst 17F82   # LD ($FFFF),A; after LD A,$1A; 32 bytes of valid code before it
mapst 1FF82   # LD ($FFFF),A; after LD A,$1A; 32 bytes of valid code before it
mapst 7BF82   # LD ($FFFF),A; after LD A,$1A; 32 bytes of valid code before it
mapst 03BB7   ; LD ($FFFE),A, the twin of $3BA7 that returns with carry set
site 0145F   ; OUT (C),L
site 01461   ; OUT (C),A
site 01468   ; IN A,(C)
site 0146F   ; IN A,(C)
site 0BFC4   ; IN A,($BE)
site 0BFC9   ; OUT ($BF),A
site 0BFD0   ; OUT ($BF),A
site 0BFD6   ; OUT ($BE),A
site 13FC4   ; IN A,($BE)
site 13FC9   ; OUT ($BF),A
site 13FD0   ; OUT ($BF),A
site 13FD6   ; OUT ($BE),A
site 17EC6   ; IN A,($DC)
site 17FC4   ; IN A,($BE)
site 17FC9   ; OUT ($BF),A
site 17FD0   ; OUT ($BF),A
site 17FD6   ; OUT ($BE),A
site 1FFC4   ; IN A,($BE)
site 1FFC9   ; OUT ($BF),A
site 1FFD0   ; OUT ($BF),A
site 1FFD6   ; OUT ($BE),A
site 7B8D6   ; OUT ($BF),A
site 7B8DA   ; OUT ($BF),A
site 7B8E4   ; OUT ($BF),A
site 7B8E8   ; OUT ($BF),A
site 7B910   ; OUT ($BF),A
site 7B914   ; OUT ($BF),A
site 7BDA3   ; OUT ($BF),A
site 7BDA7   ; OUT ($BF),A
site 7BDAC   ; OUT ($BE),A
site 7BFC4   ; IN A,($BE)
site 7BFC9   ; OUT ($BF),A
site 7BFD0   ; OUT ($BF),A
site 7BFD6   ; OUT ($BE),A

# Step rate. The play loop in bank 1 runs one step of the game's logic, then waits for
# the next frame event (CALL $0555 with B = ($DA5F), at $450D). A Master System
# cannot finish a step in one frame: in the attract demo a step takes 2 to 7 frames on
# the reference (sg1000m3, NTSC), 3 or 4 most of the time, and the game, the ball
# included, plays at that rate. The Next finishes most steps in one or two frames and
# would play about twice as fast. Page 0 times the logic of each step on the Next in Next
# lines, without the game's frame handler (marks at $00B5 and $0167), turns the lines
# into PAL Master System frames and holds the step until that many frame events have
# passed since it started. The model: a step's Master System logic is 200.6 cycles per
# Next line of logic plus 77399 (a least-squares fit over 122 demo steps paired with the
# reference, median error 6%); a PAL Master System frame is 71364 cycles, of which the
# frame handler takes about 5580, so a step takes 2 + (lines + 58) / 328 frames (whole
# frames). The same model with the NTSC frame gives the reference's own step lengths for
# 267 of its 276 demo steps. A step whose logic takes the Next longer than that ends
# later, as without the hold.
asm 000B5 6    ; LD A,($C925); LD ($C819),A: the frame path of the interrupt handler starts
    rst $00
    db far_io, pg_ss_in, ent_ss_in
endasm
asm 00167 6    ; LD A,($C833); LD ($C824),A: the interrupt handler ends
    rst $00
    db far_io, pg_ss_out, ent_ss_out
endasm
asm 04503 19   ; LD A,($DB90); LD ($CA0C),A; LD A,($DA5F); LD B,A; CALL $0555; CALL $78A6; CALL $03CA
1:  ei
    rst $00
    db far_io, pg_ss_wait, ent_ss_wait
    jr c,2f
    rst $00
    db halt_io
    jr 1b
2:  nop
    nop
    call $78A6
    call $03CA
endasm
page 0 ss_in ss_out ss_wait
; Times the logic of each play loop step and holds the step at a PAL Master System's
; rate. Uses no runtime internals but isr_n (frame events, modulo 256); reads the Next's
; line through NextRegs $1E and $1F (ports $243B/$253B). Works on a stack of its own in
; this page with interrupts off, and returns with the interrupt state it found.
LPF     equ 311             ; Next lines in a 50 Hz frame (the spec sets hz 50)
LSTEP   equ 328             ; Next lines of logic per Master System frame
LOFF    equ 58              ; and the offset: frames = 2 + (lines + LOFF) / LSTEP
CMAX    equ 4000            ; the most logic lines counted
; rd_line: HL = the Next's current line. Uses A, BC.
rd_line:
        ld bc,$243B
        ld a,$1E
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
        cp h
        jr nz,rd_line
        ld a,h
        and 1
        ld h,a
        ret
; seg: HL = (HL - DE) modulo the frame's lines. Uses DE.
seg:
        or a
        sbc hl,de
        ret nc
        ld de,LPF
        add hl,de
        ret
; ss_in: at $00B5, the start of the interrupt handler's frame path, interrupts off, every
; register but A saved by the game. The step's logic ran from the last mark to now. Does
; LD A,($C925) and LD ($C819),A. The mark is not at the handler's entry: its line path
; reads the V counter ($0201) and branches on it, and a far call there changes the
; game's title timing.
ss_in:
        ld a,1
        ld (inirq),a
        ld a,(active)
        or a
        jr z,1f
        ld (sv_sp),sp
        ld sp,stk_top
        call rd_line
        ld de,(last)
        call seg
        ld de,(cacc)
        add hl,de
        ld (cacc),hl
        ld sp,(sv_sp)
1:      ld a,($C925)
        ld ($C819),a
        ret
; ss_out: at $0167, the end of the interrupt handler, interrupts off, every register but
; A saved by the game. After the frame path, the logic goes on from now; after the line
; path it does nothing. A step that waits for its frame event
; starts here once that event has come (waiting 1 -> 2). Does LD A,($C833) and
; LD ($C824),A.
ss_out:
        ld a,(inirq)
        or a
        jr z,3f
        xor a
        ld (inirq),a
        ld a,(active)
        or a
        jr nz,2f
        ld a,(waiting)
        cp 1
        jr nz,3f
        ld a,(isr_n)
        ld hl,target
        sub (hl)
        jp m,3f
        ld a,2
        ld (waiting),a
        ld hl,0
        ld (cacc),hl
        ld a,(isr_n)
        ld (s0),a
        ld a,1
        ld (active),a
2:      ld (sv_sp),sp
        ld sp,stk_top
        call rd_line
        ld (last),hl
        ld sp,(sv_sp)
3:      ld a,($C833)
        ld ($C824),a
        ret
; ss_wait: at $4504, in the loop that replaces the frame wait. The first call ends the
; step's logic, does the game's LD A,($DB90), LD ($CA0C),A and B = ($DA5F), and works out
; the frame event at which the step may end: the later of the Master System's frames
; from the step's start and the game's own B frame events from now. Returns carry set
; once ss_out has started the next step at that frame event, with A = B = ($DA5F).
; Keeps DE and HL.
ss_wait:
        ld a,i              ; P/V = the interrupt state
        di
        ld (sv_sp),sp
        ld sp,stk_top
        push af
        push de
        push hl
        ld a,(waiting)      ; 0: the step's logic ran, 1: waiting, 2: the next step began
        cp 1
        jr z,5f
        jr c,9f
        xor a
        ld (waiting),a
        inc a
        jr 7f
9:      ld a,($DB90)
        ld ($CA0C),a
        ld a,(active)
        or a
        ld c,0              ; C = Master System frames after s0; 0 when not timed
        jr z,4f
        xor a
        ld (active),a
        call rd_line
        ld de,(last)
        call seg
        ld de,(cacc)
        add hl,de
        ld de,CMAX
        or a
        sbc hl,de
        add hl,de
        jr c,1f
        ex de,hl
1:      ld de,LOFF
        add hl,de
        ld de,LSTEP
        ld c,2
2:      or a
        sbc hl,de
        jr c,3f
        inc c
        jr 2b
3:      ld a,(s0)
        add a,c
        ld c,a              ; C = s0 + Master System frames
4:      ld a,($DA5F)
        ld b,a
        ld a,(isr_n)
        add a,b             ; A = now + the game's frames
        ld b,a
        ld a,c
        or a
        jr z,6f
        sub b
        jp m,6f
        ld b,c              ; the Master System's frames end later
6:      ld a,b
        ld (target),a
        ld a,1
        ld (waiting),a
5:      xor a
7:      ld (rdy),a
        pop hl
        pop de
        pop af
        ld sp,(sv_sp)
        ld a,($DA5F)
        ld b,a
        jp po,8f
        ld a,(rdy)
        rrca
        ld a,b
        ei
        ret
8:      ld a,(rdy)
        rrca
        ld a,b
        ret
active: db 0
inirq:  db 0
waiting: db 0
rdy:    db 0
s0:     db 0
target: db 0
last:   dw 0
cacc:   dw 0
sv_sp:  dw 0
stk:    ds 64
stk_top:
endpage

# Sonic Spinball (Europe, Brazil).cht, "Infinite Lives": RAM $DA2F is the lives count
poke "Infinite lives"
ar 00DA-2F09
endpoke

# Sonic Spinball (Europe, Brazil).cht, "Infinite Continues": RAM $DA34 is the continues count
poke "Infinite continues"
ar 00DA-3409
endpoke
