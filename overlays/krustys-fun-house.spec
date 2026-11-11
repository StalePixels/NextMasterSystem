# Krusty's Fun House (Europe, Brazil) (En), CRC32 64A585EB, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from a sitescan output with three reference I/O logs (the 60 s
# sweep, 600 s of random input, 180 s with no input) and hand-made entries, then decided by hand.
#
# Decisions:
# - The game's code is in bank 0 and in slot 1, which holds bank 1 whenever code runs there
#   (the game puts bank 2 in slot 1 only for short data reads at $34BE-$356A, with interrupts
#   off). The scan entries are the slot 1 targets in bank 1; the object handler tables at
#   $1984 (3-byte records) and $1B00 (words; banks 0, 1 and 8); the far-call routine $6B5A
#   (CALL $6B5A, then the bank and address): bank 5 $8000, bank 8 $B6A6-$B7BB, bank 12 $8A27,
#   bank 1 $69FE and $6A1A; the bank 12, 13 and 8 routines called after constant bank writes;
#   and the bank 1 VDP helpers that no scanned path reaches ($5809, $581C, $5B0D, $5B13,
#   $5CDA, $617E, $6256, $64E9, $6505, $650C, $69E2, $4ED8, $662C).
# - io vector at $10, not $00: the game writes $FF to $0000 every frame through a null
#   pointer ($70C7 and $70CC, LD (HL),$FF with HL from $C4CA and $C4C8), which would break
#   an io vector there. The bytes at $0007-$0037 are filler that no code reads.
# - The game never sets an interrupt mode; the runtime's IM 2 stays.
# - Many VDP writes go through an unrolled run of 128 OUTI at $1700-$17FF (RET at $1800) that
#   the game enters at any OUTI, through a JP it builds in RAM ($C315, $C31A).
# - Five mapper stores go through a register, which no spec line form takes; each is a far
#   call to a page 0 entry that does the same through the runtime's mapper store:
#   $2A77 (LD ($C4ED),A; LD (HL),A, HL = $FFFF), $34B0 (EX DE,HL; LD (HL),C; DEC L;
#   LD (HL),$01, HL = $FFFF), $4BC3 and $4BC9 (LD (DE),A, DE = $FFFF), $6265 (LD (HL),$0F;
#   EX AF,AF'; LD (HL),A, HL = $FFFF).
# - The byte scan rows in banks 2, 4, 5, 6, 8, 9, 10 and 11 are graphics, maps and sound data
#   (verdict false); bank 13 $9971 (OUTD; RET between two routines) has no path to it.
name Krusty's Fun House
cart 64A585EB
hz 50		; No-Intro regions Europe, Brazil
vector 10 io
site 01700   ; OUTI
site 01702   ; OUTI
site 01704   ; OUTI
site 01706   ; OUTI
site 01708   ; OUTI
site 0170A   ; OUTI
site 0170C   ; OUTI
site 0170E   ; OUTI
site 01710   ; OUTI
site 01712   ; OUTI
site 01714   ; OUTI
site 01716   ; OUTI
site 01718   ; OUTI
site 0171A   ; OUTI
site 0171C   ; OUTI
site 0171E   ; OUTI
site 01720   ; OUTI
site 01722   ; OUTI
site 01724   ; OUTI
site 01726   ; OUTI
site 01728   ; OUTI
site 0172A   ; OUTI
site 0172C   ; OUTI
site 0172E   ; OUTI
site 01730   ; OUTI
site 01732   ; OUTI
site 01734   ; OUTI
site 01736   ; OUTI
site 01738   ; OUTI
site 0173A   ; OUTI
site 0173C   ; OUTI
site 0173E   ; OUTI
site 01740   ; OUTI
site 01742   ; OUTI
site 01744   ; OUTI
site 01746   ; OUTI
site 01748   ; OUTI
site 0174A   ; OUTI
site 0174C   ; OUTI
site 0174E   ; OUTI
site 01750   ; OUTI
site 01752   ; OUTI
site 01754   ; OUTI
site 01756   ; OUTI
site 01758   ; OUTI
site 0175A   ; OUTI
site 0175C   ; OUTI
site 0175E   ; OUTI
site 01760   ; OUTI
site 01762   ; OUTI
site 01764   ; OUTI
site 01766   ; OUTI
site 01768   ; OUTI
site 0176A   ; OUTI
site 0176C   ; OUTI
site 0176E   ; OUTI
site 01770   ; OUTI
site 01772   ; OUTI
site 01774   ; OUTI
site 01776   ; OUTI
site 01778   ; OUTI
site 0177A   ; OUTI
site 0177C   ; OUTI
site 0177E   ; OUTI
site 01780   ; OUTI
site 01782   ; OUTI
site 01784   ; OUTI
site 01786   ; OUTI
site 01788   ; OUTI
site 0178A   ; OUTI
site 0178C   ; OUTI
site 0178E   ; OUTI
site 01790   ; OUTI
site 01792   ; OUTI
site 01794   ; OUTI
site 01796   ; OUTI
site 01798   ; OUTI
site 0179A   ; OUTI
site 0179C   ; OUTI
site 0179E   ; OUTI
site 017A0   ; OUTI
site 017A2   ; OUTI
site 017A4   ; OUTI
site 017A6   ; OUTI
site 017A8   ; OUTI
site 017AA   ; OUTI
site 017AC   ; OUTI
site 017AE   ; OUTI
site 017B0   ; OUTI
site 017B2   ; OUTI
site 017B4   ; OUTI
site 017B6   ; OUTI
site 017B8   ; OUTI
site 017BA   ; OUTI
site 017BC   ; OUTI
site 017BE   ; OUTI
site 017C0   ; OUTI
site 017C2   ; OUTI
site 017C4   ; OUTI
site 017C6   ; OUTI
site 017C8   ; OUTI
site 017CA   ; OUTI
site 017CC   ; OUTI
site 017CE   ; OUTI
site 017D0   ; OUTI
site 017D2   ; OUTI
site 017D4   ; OUTI
site 017D6   ; OUTI
site 017D8   ; OUTI
site 017DA   ; OUTI
site 017DC   ; OUTI
site 017DE   ; OUTI
site 017E0   ; OUTI
site 017E2   ; OUTI
site 017E4   ; OUTI
site 017E6   ; OUTI
site 017E8   ; OUTI
site 017EA   ; OUTI
site 017EC   ; OUTI
site 017EE   ; OUTI
site 017F0   ; OUTI
site 017F2   ; OUTI
site 017F4   ; OUTI
site 017F6   ; OUTI
site 017F8   ; OUTI
site 017FA   ; OUTI
site 017FC   ; OUTI
site 017FE   ; OUTI
mapst 01DEB   ; LD ($FFFF),A
maphl 01EED   # LD (HL),$04, HL = $FFFF
mapst 01F13   ; LD ($FFFF),A
maphl 01FAD   # LD (HL),$0D, HL = $FFFF
mapst 01FC3   ; LD ($FFFF),A
site 01FCD   ; OUT ($BE),A
site 01FD4   ; OUT ($BE),A
mapst 021BF   ; LD ($FFFE),A
site 021C4   ; OUT ($BF),A
site 021C8   ; OUT ($BF),A
site 021CC   ; OUT ($BF),A
site 021D0   ; OUT ($BF),A
site 021D4   ; OUT ($BF),A
site 021D8   ; OUT ($BF),A
site 021E3   ; OUT ($BF),A
site 021E7   ; OUT ($BF),A
site 021EB   ; OUT ($BF),A
site 021EF   ; OUT ($BF),A
mapst 02205   ; LD ($FFFF),A
site 0220D   ; OUTI
site 02213   ; OUT ($BE),A
site 0222B   ; OUT ($BE),A
site 02233   ; OUT ($BE),A
site 0223C   ; OUT ($BE),A
site 02246   ; OUT ($BE),A
mapst 02249   ; LD ($FFFE),A
site 0225A   ; OUT ($BE),A
site 02265   ; OUT ($BE),A
site 0226A   ; OUT ($BE),A
site 02274   ; OUT ($BE),A
site 027A9   ; OUT ($BF),A
site 027AD   ; OUT ($BF),A
site 027B1   ; OUT ($BF),A
site 027B5   ; OUT ($BF),A
site 02802   ; OUT ($BF),A
site 02806   ; OUT ($BF),A
site 0280A   ; OUT ($BF),A
site 0280E   ; OUT ($BF),A
mapst 0281F   ; LD ($FFFF),A
mapst 028A6   ; LD ($FFFF),A
mapst 0292C   ; LD ($FFFF),A
mapst 0293A   ; LD ($FFFF),A
otir 02963   ; OUTI
mapst 0299F   ; LD ($FFFF),A
mapst 029DD   ; LD ($FFFF),A
site 029E6   ; OUTI
mapst 029F8   ; LD ($FFFF),A
site 02A06   ; OUTI
site 02A1C   ; OUT ($BE),A
mapst 02A98   ; LD ($FFFF),A
mapst 02A9F   ; LD ($FFFF),A
site 02AB4   ; OUT ($BF),A
site 02AB8   ; OUT ($BF),A
site 02ABC   ; OUT ($BF),A
site 02AC0   ; OUT ($BF),A
mapst 02AC4   ; LD ($FFFF),A
mapst 02B03   ; LD ($FFFF),A
mapst 02B18   ; LD ($FFFF),A
site 02BCC   ; OUT ($BF),A
site 02BD0   ; OUT ($BF),A
site 02C2E   ; IN A,($BF)
site 02C30   ; IN A,($7E)
site 02C88   ; OUT ($BF),A
site 02C8C   ; OUT ($BF),A
site 02CC0   ; IN A,($7E)
mapst 02CCF   ; LD ($FFFF),A
mapst 02CD4   ; LD ($FFFF),A
mapst 02D0A   ; LD ($FFFF),A
site 02D23   ; IN A,($7E)
maphl 02D36   # LD (HL),$0D, HL = $FFFF
mapst 02D4F   ; LD ($FFFF),A
mapst 02D54   ; LD ($FFFF),A
maphl 02D61   # LD (HL),$0D, HL = $FFFF
maphl 02D73   # LD (HL),$0D, HL = $FFFF
maphl 02D88   # LD (HL),$0D, HL = $FFFF
mapst 02EB7   ; LD ($FFFF),A
mapst 02EC2   ; LD ($FFFF),A
mapst 02EDD   ; LD ($FFFF),A
mapst 02F3D   ; LD ($FFFF),A
site 032A3   ; OUT ($BF),A
site 032A7   ; OUT ($BF),A
site 032AB   ; OUT ($BF),A
site 032AF   ; OUT ($BF),A
mapldk 03450   # LD HL,$FFFE; LD (HL),$02
maphl 03457   # LD (HL),$0B, HL = $FFFF
mapldk 034BF   # LD HL,$FFFE; LD (HL),$02
maphl 034C5   # LD (HL),$0B, HL = $FFFF
site 034EE   ; OUT ($BF),A
site 034F4   ; OUT ($BF),A
mapldk 03509   # LD HL,$FFFE; LD (HL),$01
mapldk 03535   # LD HL,$FFFE; LD (HL),$02
maphl 0353B   # LD (HL),$0B, HL = $FFFF
mapldk 03567   # LD HL,$FFFE; LD (HL),$01
maphl 0356D   # LD (HL),$02, HL = $FFFF
site 04A3E   ; OUT ($BE),A
site 04A44   ; OUT ($BE),A
site 04A5C   ; OUT ($BF),A
site 04A5F   ; OUT ($BF),A
site 04A69   ; INI
site 04A7C   ; OUTI
site 04A86   ; OUTI
mapst 04A99   ; LD ($FFFF),A
mapst 04AF7   ; LD ($FFFF),A
site 04AFF   ; OUT ($BF),A
site 04B03   ; OUT ($BF),A
site 04B07   ; OUT ($BF),A
site 04B0B   ; OUT ($BF),A
mapst 04B4B   ; LD ($FFFF),A
site 04BFD   ; OUT ($BF),A
site 04C02   ; OUT ($BF),A
mapst 04C05   ; LD ($FFFF),A
mapst 04C13   ; LD ($FFFF),A
mapst 04CB9   ; LD ($FFFF),A
mapst 04CEE   ; LD ($FFFF),A
site 04D12   ; OUT ($BE),A
site 04D19   ; OUT ($BE),A
site 04D1F   ; OUT ($BE),A
site 04D25   ; OUT ($BE),A
mapst 04ED9   ; LD ($FFFF),A
site 04EEE   ; OUT ($BF),A
site 04EF1   ; OUT ($BF),A
otir 04F08   ; OUTI
site 04F0E   ; OUT ($BE),A
site 04F15   ; OUT ($BF),A
site 04F18   ; OUT ($BF),A
otir 04F21   ; OUTI
site 04F3A   ; OUTI
site 04F46   ; OUTD
site 04F4C   ; OUT ($BE),A
site 04F53   ; OUT ($BF),A
site 04F56   ; OUT ($BF),A
site 04F68   ; OUTI
site 04F75   ; OUTI
site 04F7B   ; OUTD
mapst 04FE4   ; LD ($FFFF),A
site 05014   ; OUT ($BF),A
site 05018   ; OUT ($BF),A
site 0501C   ; OUT ($BF),A
site 05020   ; OUT ($BF),A
site 05024   ; OUT ($BF),A
site 05028   ; OUT ($BF),A
site 0502C   ; OUT ($BF),A
site 05030   ; OUT ($BF),A
site 05034   ; OUT ($BF),A
site 05038   ; OUT ($BF),A
site 0503C   ; OUT ($BF),A
site 05040   ; OUT ($BF),A
site 05044   ; OUT ($BF),A
site 05048   ; OUT ($BF),A
site 0504C   ; OUT ($BF),A
site 05050   ; OUT ($BF),A
site 05054   ; OUT ($BF),A
site 05058   ; OUT ($BF),A
site 0505C   ; OUT ($BF),A
site 05060   ; OUT ($BF),A
site 05069   ; OUT ($BF),A
site 0506D   ; OUT ($BF),A
site 05077   ; OUT ($BE),A
mapst 05099   ; LD ($FFFF),A
site 057CE   ; OUT ($BE),A
site 057DA   ; OUT ($BF),A
site 057E0   ; OUT ($BF),A
site 057EC   ; OUT ($BE),A
site 057F2   ; OUT ($BE),A
site 05804   ; OUT ($BE),A
site 0580F   ; IN A,($BE)
site 05818   ; IN A,($BE)
site 05823   ; OUT ($BE),A
site 0582C   ; OUT ($BE),A
site 05A80   ; OUT ($BF),A
site 05A85   ; OUT ($BF),A
site 05AAB   ; OUT ($BE),A
site 05B17   ; OUT ($BF),A
site 05B1B   ; OUT ($BF),A
site 05B28   ; OUT ($BE),A
site 05B59   ; OUT ($BF),A
site 05B5D   ; OUT ($BF),A
site 05BD0   ; OUT ($BF),A
site 05BD4   ; OUT ($BF),A
site 05BD7   ; OUT ($BE),A
site 05BDC   ; OUT ($BF),A
site 05BE0   ; OUT ($BF),A
site 05BED   ; IN A,($DC)
maphl 05C40   # LD (HL),$0C, HL = $FFFF
maphl 05C54   # LD (HL),$0C, HL = $FFFF
site 05C59   ; OUT ($BF),A
site 05C5D   ; OUT ($BF),A
site 05C70   ; OUT ($BF),A
site 05C74   ; OUT ($BF),A
site 05C78   ; OUT ($BF),A
site 05C7C   ; OUT ($BF),A
mapst 05C96   ; LD ($FFFF),A
mapst 05CB9   ; LD ($FFFF),A
site 05CEC   ; OUT ($BE),A
site 05CF2   ; OUT ($BE),A
mapst 05DB8   ; LD ($FFFF),A
site 05DFA   ; OUT ($BF),A
site 05DFF   ; OUT ($BF),A
site 05E47   ; OUT ($BE),A
site 05E4C   ; OUT ($BE),A
site 05E51   ; OUT ($BE),A
site 05E56   ; OUT ($BE),A
site 05E5B   ; OUT ($BE),A
site 05E60   ; OUT ($BE),A
site 05E65   ; OUT ($BE),A
site 05E6A   ; OUT ($BE),A
site 05E6F   ; OUT ($BE),A
site 05E74   ; OUT ($BE),A
site 05E79   ; OUT ($BE),A
site 05E7E   ; OUT ($BE),A
site 05E83   ; OUT ($BE),A
site 05E88   ; OUT ($BE),A
site 05E8D   ; OUT ($BE),A
site 05E92   ; OUT ($BE),A
site 05E97   ; OUT ($BE),A
site 05E9C   ; OUT ($BE),A
site 05EA1   ; OUT ($BE),A
site 05EA6   ; OUT ($BE),A
site 05EAB   ; OUT ($BE),A
site 05EB0   ; OUT ($BE),A
site 05EB5   ; OUT ($BE),A
site 05EBA   ; OUT ($BE),A
site 05EBF   ; OUT ($BE),A
site 05EC4   ; OUT ($BE),A
site 05EC9   ; OUT ($BE),A
site 05ECE   ; OUT ($BE),A
site 05ED3   ; OUT ($BE),A
site 05ED8   ; OUT ($BE),A
site 05EDD   ; OUT ($BE),A
site 05EE2   ; OUT ($BE),A
mapst 06186   ; LD ($FFFF),A
mapst 06196   ; LD ($FFFF),A
mapst 061A0   ; LD ($FFFF),A
otir 061C4   ; OUTI
mapst 061CC   ; LD ($FFFF),A
site 061D3   ; IN A,($BF)
site 061F5   ; IN A,($DD)
site 0620E   ; OUT ($BF),A
site 06214   ; OUT ($BF),A
site 06246   ; OUT ($BF),A
site 0624A   ; OUT ($BF),A
site 0624F   ; OUT ($BF),A
site 06253   ; OUT ($BF),A
otir 0625A   ; OUTI
mapst 062F3   ; LD ($FFFF),A
site 0635C   ; OUT ($BF),A
site 06361   ; OUT ($BF),A
site 0636C   ; OUTI
site 06374   ; OUT ($BF),A
site 06379   ; OUT ($BF),A
site 06384   ; OUTI
site 064E1   ; OUT ($BF),A
site 064E6   ; OUT ($BF),A
site 064EA   ; OUT ($BF),A
site 064F1   ; OUT ($BF),A
site 06519   ; OUT ($BE),A
site 0651F   ; OUT ($BE),A
mapst 0652A   ; LD ($FFFF),A
mapst 06551   ; LD ($FFFF),A
site 065BB   ; OUT ($BF),A
site 065C0   ; OUT ($BF),A
site 065FD   ; OUTI
site 06602   ; OUTI
site 06618   ; OUT ($BF),A
site 0661E   ; OUT ($BF),A
site 06637   ; OUTI
site 0663C   ; OUTI
site 06658   ; OUTI
site 0665B   ; OUTI
site 0665E   ; OUTI
site 06661   ; OUTI
site 06669   ; OUTI
site 0666C   ; OUTI
site 0666F   ; OUTI
site 06672   ; OUTI
site 0667A   ; OUTI
site 0667D   ; OUTI
site 06680   ; OUTI
site 06683   ; OUTI
site 0668B   ; OUTI
site 0668E   ; OUTI
site 06691   ; OUTI
site 06694   ; OUTI
site 0669C   ; OUTI
site 0669F   ; OUTI
site 066A2   ; OUTI
site 066A5   ; OUTI
site 066AD   ; OUTI
site 066B0   ; OUTI
site 066B3   ; OUTI
site 066B6   ; OUTI
site 066BE   ; OUTI
site 066C1   ; OUTI
site 066C4   ; OUTI
site 066C7   ; OUTI
site 066CF   ; OUTI
site 066D2   ; OUTI
site 066D5   ; OUTI
site 066D8   ; OUTI
site 066E0   ; OUTI
site 066E3   ; OUTI
site 066E6   ; OUTI
site 066E9   ; OUTI
site 066F1   ; OUTI
site 066F4   ; OUTI
site 066F7   ; OUTI
site 066FA   ; OUTI
site 06702   ; OUTI
site 06705   ; OUTI
site 06708   ; OUTI
site 0670B   ; OUTI
site 06713   ; OUTI
site 06716   ; OUTI
site 06719   ; OUTI
site 0671C   ; OUTI
site 06724   ; OUTI
site 06727   ; OUTI
site 0672A   ; OUTI
site 0672D   ; OUTI
site 06735   ; OUTI
site 06738   ; OUTI
site 0673B   ; OUTI
site 0673E   ; OUTI
site 06746   ; OUTI
site 06749   ; OUTI
site 0674C   ; OUTI
site 0674F   ; OUTI
site 06757   ; OUTI
site 0675A   ; OUTI
site 0675D   ; OUTI
site 06760   ; OUTI
site 0676B   ; OUTI
site 0676E   ; OUTI
site 067D2   ; OUT ($BF),A
site 067D8   ; OUT ($BF),A
site 067EB   ; OUT ($BE),A
site 067F4   ; OUT ($BE),A
site 067FB   ; OUT ($BF),A
site 06801   ; OUT ($BF),A
site 0680A   ; OUT ($BE),A
site 06811   ; OUT ($BE),A
otir 068C1   ; OUTI
site 068CD   ; OUT ($BF),A
site 068D1   ; OUT ($BF),A
mapst 068DE   ; LD ($FFFF),A
site 0696B   ; OUTI
site 06971   ; OUTI
mapst 069E7   ; LD ($FFFF),A
mapst 069FA   ; LD ($FFFF),A
site 06AD6   ; IN A,($7E)
site 06AE8   ; OUT ($BF),A
site 06AED   ; OUT ($BF),A
site 06AF4   ; OUT ($BE),A
site 06AF9   ; OUT ($BE),A
site 06B25   ; IN A,($7E)
site 06B34   ; OUT ($BF),A
site 06B3B   ; OUT ($BF),A
otir 06B43   ; OUTI
mapst 06B72   ; LD ($FFFF),A
mapst 06B7F   ; LD ($FFFF),A
mapst 06BB2   ; LD ($FFFF),A
mapst 06C4C   ; LD ($FFFF),A
site 06C7D   ; OUT ($BF),A
site 06C81   ; OUT ($BF),A
site 06CB1   ; OUT ($BF),A
site 06CB5   ; OUT ($BF),A
site 06CDE   ; OUT ($BF),A
site 06CE2   ; OUT ($BF),A
site 06D0A   ; OUT ($BE),A
site 06D10   ; OUT ($BE),A
site 06D46   ; OUT ($BE),A
site 06D4A   ; OUT ($BF),A
site 06D4E   ; OUT ($BF),A
site 06E0D   ; OUTI
site 06E13   ; OUTI
site 06E18   ; OUT ($BE),A
site 06E1E   ; OUT ($BE),A
maphl 06E44   # LD (HL),$0F, HL = $FFFF
mapst 06E93   ; LD ($FFFF),A
mapst 06F1C   ; LD ($FFFF),A
mapst 06F55   ; LD ($FFFF),A
site 06F8E   ; OUTI
mapst 06FB6   ; LD ($FFFF),A
mapst 07016   ; LD ($FFFF),A
mapst 0703D   ; LD ($FFFF),A
site 07071   ; IN A,($BF)
eihalt 07078   ; EI; HALT in the frame wait $706C
maphl 0708E   # LD (HL),$0C, HL = $FFFF
mapst 070CF   ; LD ($FFFF),A
mapst 071AC   ; LD ($FFFF),A
site 14008   ; OTIR
site 1400C   ; IN A,($DC)
site 1402A   ; OUT ($7F),A
site 14030   ; OUT ($7F),A
site 14036   ; OUT ($7F),A
site 14049   ; OUT ($7F),A
site 1404F   ; OUT ($7F),A
site 14055   ; OUT ($7F),A
site 14059   ; IN A,($DC)
site 2384C   ; OUTI
site 2384F   ; OUT ($BE),A
site 23852   ; OUTI
site 23855   ; OUT ($BE),A
site 2DF74   ; OUT ($BF),A
site 2DF79   ; OUT ($BF),A
site 30A7A   ; OUTI
site 30A83   ; OUT ($BE),A
site 30A8F   ; OUTI
site 30C0E   ; IN A,($BF)
site 30C10   ; IN A,($BF)
site 30C1C   ; IN A,($BF)
site 3C100   ; OTIR
site 3C13E   ; OUTI
site 3C140   ; OUTI
site 3C142   ; OUTI
site 3C14D   ; OUTI
site 3C14F   ; OUTI
site 3C151   ; OUTI
site 3C15C   ; OUTI
site 3C15E   ; OUTI
site 3C160   ; OUTI
site 3C16B   ; OUTI
site 3C72E   ; OUT ($7F),A
site 3C895   ; OUT ($7F),A
site 3C89E   ; OUT ($7F),A
site 3C8F1   ; OUT ($7F),A
site 3C8FA   ; OUT ($7F),A
site 3C94D   ; OUT ($7F),A
site 3C956   ; OUT ($7F),A
site 3C9A5   ; OUT ($7F),A
site 3C9CD   ; OUT ($7F),A
site 3C9FF   ; OUT ($7F),A
site 3CA3A   ; OUT ($7F),A
site 3CA42   ; OUT ($7F),A
site 3CA51   ; OUT ($7F),A
site 3CA5A   ; OUT ($7F),A
site 3CA86   ; OUT ($7F),A
site 3CA8F   ; OUT ($7F),A
site 3CAB1   ; OUT ($7F),A
site 3CAE3   ; OUT ($7F),A
site 3CB1E   ; OUT ($7F),A
site 3CB26   ; OUT ($7F),A
site 3CB35   ; OUT ($7F),A
site 3CB3E   ; OUT ($7F),A
site 3CB6A   ; OUT ($7F),A
site 3CB73   ; OUT ($7F),A
site 3CB95   ; OUT ($7F),A
site 3CBC7   ; OUT ($7F),A
site 3CC02   ; OUT ($7F),A
site 3CC0A   ; OUT ($7F),A
site 3CC19   ; OUT ($7F),A
site 3CC22   ; OUT ($7F),A
site 3CC4E   ; OUT ($7F),A
site 3CC57   ; OUT ($7F),A
site 3CC79   ; OUT ($7F),A
site 3CCAB   ; OUT ($7F),A
site 3CCD7   ; OUT ($7F),A
site 3EF37   ; OUTI
site 3EF3B   ; OUT ($BE),A
site 3EF40   ; OUT ($BE),A
site 3EF45   ; OUT ($BE),A
site 3EFC9   ; OUT ($BE),A
site 3EFCF   ; OUT ($BE),A
site 3EFD2   ; OUT ($BE),A
site 3EFD5   ; OUT ($BE),A
site 3EFD9   ; OUT ($BE),A
site 3EFDF   ; OUT ($BE),A
site 3EFE2   ; OUT ($BE),A
site 3EFE5   ; OUT ($BE),A
site 3EFE9   ; OUT ($BE),A
site 3EFEF   ; OUT ($BE),A
site 3EFF2   ; OUT ($BE),A
site 3EFF5   ; OUT ($BE),A
site 3EFF9   ; OUT ($BE),A
site 3EFFF   ; OUT ($BE),A
site 3F002   ; OUT ($BE),A
site 3F005   ; OUT ($BE),A
site 3F009   ; OUT ($BE),A
site 3F00F   ; OUT ($BE),A
site 3F012   ; OUT ($BE),A
site 3F015   ; OUT ($BE),A
site 3F019   ; OUT ($BE),A
site 3F01F   ; OUT ($BE),A
site 3F022   ; OUT ($BE),A
site 3F025   ; OUT ($BE),A
site 3F029   ; OUT ($BE),A
site 3F02F   ; OUT ($BE),A
site 3F032   ; OUT ($BE),A
site 3F035   ; OUT ($BE),A
site 3F039   ; OUT ($BE),A
site 3F03F   ; OUT ($BE),A
site 3F042   ; OUT ($BE),A
site 3F045   ; OUT ($BE),A
# Delay $719A (bank 1): LD HL,$0000, then DEC HL : LD A,L : OR H : JR NZ,$719D : RET, 65536
# passes of 26 T-states; $7185 runs it B times. It holds the copyright, Flying Edge and Audiogenic
# screens (reference: 245 and 365 frames with no frame wait). A busy loop, so at 28 MHz the holds
# were about 8 times too short. Page entry delay waits the same real time on the Next's raster
# line, as in mortal-kombat-ii.spec, whose $3BFF is the same loop.
asm 0719D 6          ; DEC HL : LD A,L : OR H : JR NZ,$719D : RET
    rst $10
    db far_io, pg_delay, ent_delay
    ret
endasm
# Frame wait $706C (bank 1): EI : HALT until the frame interrupt sets bit 5 of $C44F, then
# IN A,($7E) : DI : RET at $7080, as in Mortal Kombat II ($58A2). That read, just after the frame
# event, would run the runtime's frame work before the game's frame; vread makes it with vbl_done
# set, so the work runs at the ULA interrupt, after the game has written the frame. The 4 bytes
# of the far call cover the RET; vread returns to the game's caller itself.
asm 07080 4          ; IN A,($7E) : DI : RET
    rst $10
    db far_io, pg_vread, ent_vread
endasm
asm 02A77 4   ; LD ($C4ED),A; LD (HL),A with HL = $FFFF
    rst $10
    db far_io, pg_m2a77, ent_m2a77
endasm
asm 034B0 5   ; EX DE,HL; LD (HL),C; DEC L; LD (HL),$01 with HL = $FFFF
    rst $10
    db far_io, pg_m34b0, ent_m34b0
    nop
endasm
asm 04BC3 6   ; LD A,$0F; LD (DE),A; JP $AED4 with DE = $FFFF
    rst $10
    db far_io, pg_m4bc3, ent_m4bc3
    nop
    nop
endasm
asm 04BC9 6   ; LD A,$0B; LD DE,$FFFF; LD (DE),A
    rst $10
    db far_io, pg_m4bc9, ent_m4bc9
    nop
    nop
endasm
asm 06265 4   ; LD (HL),$0F; EX AF,AF'; LD (HL),A with HL = $FFFF
    rst $10
    db far_io, pg_m6265, ent_m6265
endasm
page 0 m2a77 m34b0 m4bc3 m4bc9 m6265 delay vread
; Mapper stores through a register, done through the runtime's mapper store: rst $10 with
; inline code $10 + register (LD ($FFFC-$FFFF),A, third byte skipped) or $30 + n (LD (HL),n,
; HL on a mapper register). Each entry leaves the registers and flags as the game's code does.
; m2a77: as $2A77-$2A7A. A is the bank; HL = $FFFF.
m2a77:  ld ($C4ED),a
        rst $10
        db $13, $FF
        ret
; m34b0: as $34B0-$34B4. DE = $FFFF on entry; C to $FFFF, then 1 to $FFFE; HL = $FFFE and
; the flags of DEC L on return.
m34b0:  ex de,hl
        push af
        ld a,c
        rst $10
        db $13, $FF
        ld a,1
        rst $10
        db $12, $FF
        pop af
        dec l
        ret
; m4bc3: as $4BC3-$4BC8: A = $0F to $FFFF, then on to $AED4 (bank 15). The entry puts $AED4
; in place of the return address after the site, which the far call returns to.
m4bc3:  ld a,$0F
        rst $10
        db $13, $FF
        push hl
        push af
        ld hl,8
        add hl,sp
        ld (hl),$D4
        inc hl
        ld (hl),$AE
        pop af
        pop hl
        ret
; m4bc9: as $4BC9-$4BCE: A = $0B, DE = $FFFF, A to $FFFF.
m4bc9:  ld a,$0B
        ld de,$FFFF
        rst $10
        db $13, $FF
        ret
; m6265: as $6265-$6268: $0F to $FFFF, EX AF,AF', then A to $FFFF.
m6265:  rst $10
        db $3F
        ex af,af'
        rst $10
        db $13, $FF
        ret
; delay: as the game's $719D-$71A2, in real time. HL passes of 26 T-states (0 means 65536).
; Returns as the game's loop does: HL = 0, A = 0, flags as OR H with A = 0 (Z, P/V set; S, H, N, C
; clear); BC and DE kept. The interrupt state stays as it was, so the game's frame interrupt runs
; during the wait as during the game's loop; each line read runs with interrupts off, so a handler
; cannot change the NextReg select port between the select and the read. The entry uses no stack of
; its own (the game's interrupts can come while it runs, and they need the game's stack).
    macro RDLINE        ; HL = the Next's raster line, below (dlen); A, F, BC changed
        di
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
        xor h
        and 1
        jr nz,.again
        ld a,h
        and 1
        ld h,a
        jr z,.inrange           ; a read of line 511 comes at some line changes: a line of
        ld a,(dlen)             ; (dlen) or more is read again
        cp l
        jr c,.again
        jr z,.again
.inrange:
        ld a,(dirq)
        or a
        jr z,.noei
        ei
.noei:
    endm
delay:  ld (sv_bc),bc
        ld (sv_de),de
        ld a,h
        or l
        jr nz,.cnt
        ld hl,7424              ; 65536 passes
        jr .set
.cnt:   ex de,hl                ; DE = passes
        ld hl,0
        ld a,0                  ; A:HL = passes * 29, 24 bits
        ld b,29
.mul:   add hl,de
        adc a,0
        djnz .mul
        ld l,h
        ld h,a                  ; HL = passes * 29 / 256 lines
.set:   ld (dleft),hl
        ld a,i                  ; P/V: interrupts on at entry
        ld a,0
        jp po,.di
        inc a
.di:    ld (dirq),a
        di
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld hl,311               ; lines in a 50 Hz frame
        bit 2,a
        jr z,.hz
        ld hl,264               ; 60 Hz
.hz:    ld (dlen),hl
        RDLINE
        ld (dprev),hl
.poll:  RDLINE
        ld (dcur),hl
        ld de,(dprev)
        or a
        sbc hl,de               ; lines since the last read
        jr nc,.pos
        ld a,d                  ; a lower line: the frame wrapped only from line 256 or later.
        or a                    ; At line 256 the low byte can read 0 before the high byte
        jp z,.poll              ; reads 1: such a read is dropped
        ld de,(dlen)
        add hl,de               ; the frame wrapped
.pos:   ex de,hl
        ld hl,(dcur)
        ld (dprev),hl
        ld hl,(dleft)
        or a
        sbc hl,de
        ld (dleft),hl
        jr c,.end
        ld a,h
        or l
        jr nz,.poll
.end:   ld bc,(sv_bc)
        ld de,(sv_de)
        ld hl,0
        xor a
        ret
dirq:   db 0
dlen:   dw 0
dprev:  dw 0
dcur:   dw 0
dleft:  dw 0
sv_bc:  dw 0
sv_de:  dw 0
; vread: as the game's $7080-$7083 (IN A,($7E) : DI : RET): the V counter read through the
; runtime's I/O RST with vbl_done ($E086) set first, so the read does not run the frame work,
; which the ULA interrupt then runs. A = the V counter, interrupts off, the other registers and F
; as the read leaves them. The far call returns after the 4 bytes, to $7084, which is not the
; game's: the entry takes that return address off and puts the game's own RET target, the word
; under it, in its place, so the far call returns where the game's RET would.
VR_DONE equ $E086
vread:  ld a,1
        ld (VR_DONE),a
        rst $10
        db $0A                  ; IN A,(n), port class 2 ($7E: the V counter)
        di
        ld (vr_hl),hl           ; stack: far_ret, old page, $7084, the game's return
        pop hl
        ld (vr_fr),hl
        pop hl                  ; the old page word
        ex (sp),hl              ; it replaces $7084
        ld hl,(vr_fr)
        push hl                 ; stack: far_ret, old page, the game's return
        ld hl,(vr_hl)
        ret
vr_hl:  dw 0
vr_fr:  dw 0
endpage

# Krusty's Fun House (Europe, Brazil).cht, "Infinite Lives": $C429 is the life count (3 at the start of a game)
poke "Infinite lives"
ar 00C4-2903
endpoke

# Krusty's Fun House (Europe, Brazil).cht, "Invincibility": $C42A is the energy ($64 at the start of a game)
poke "Invincibility"
ar 00C4-2A64
endpoke
