# Choplifter (USA, Europe, Brazil), 4A21C15F, drafted by tools/mkspec.py from sitescan output.
name Choplifter
cart 4A21C15F
hz any		; No-Intro regions USA, Europe, Brazil
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00015   ; OUT ($DF),A
site 00045   ; OUT ($BE),A
site 006A0   ; OUT ($BF),A
site 006BB   ; OUT ($BF),A
site 007D6   ; OUT ($BF),A
site 007DD   ; OUT ($BF),A
site 0087A   ; OUT ($BE),A
site 00976   ; OUT ($BE),A
site 0097E   ; OUT ($BE),A
site 009D9   ; OUT ($BE),A
site 009E1   ; OUT ($BE),A
site 00A14   ; OUT ($BE),A
site 00A1C   ; OUT ($BE),A
site 00A28   ; OUT ($BE),A
site 00A30   ; OUT ($BE),A
site 00A39   ; OUT ($BE),A
site 00A41   ; OUT ($BE),A
site 00ABE   ; IN A,($7E)
site 00AC5   ; OUT ($BF),A
site 00ACC   ; OUT ($BF),A
site 00AD3   ; OUT ($BF),A
site 00ADA   ; OUT ($BF),A
site 00AE2   ; OUT ($BF),A
site 00AE9   ; OUT ($BF),A
site 00AF8   ; OUT ($BF),A
site 00AFF   ; OUT ($BF),A
site 00B1C   ; OUT ($DF),A
site 00B23   ; OUT ($DE),A
site 00B28   ; IN A,($DE)
site 00B55   ; IN A,($BF)
site 00B5E   ; OTIR
site 00B7E   ; OUT ($BE),A
site 00B84   ; OUT ($BE),A
site 00B9B   ; OUT ($BE),A
site 00BA5   ; OUT ($BF),A
site 00BAD   ; OUT ($BF),A
site 00BDA   ; OUT ($BF),A
site 00BE0   ; OUT ($BF),A
site 00BE6   ; OUT ($BE),A
site 00C0C   ; OUT ($BF),A
site 00C11   ; OUT ($BF),A
site 00C18   ; OUT ($BE),A
site 0112E   ; OUT ($BE),A
site 0157B   ; OUT ($BE),A
site 01581   ; OUT ($BE),A
site 0160A   ; OUT ($BE),A
site 01610   ; OUT ($BE),A
site 01706   ; OUT ($BE),A
site 0170C   ; OUT ($BE),A
site 01907   ; OUT ($BE),A
site 01937   ; OUT ($BE),A
site 019E9   ; OUT ($BF),A
site 019F1   ; OUT ($BF),A
site 019F8   ; OUT ($BE),A
site 019FF   ; OUT ($BE),A
otir 01B25   ; OUTI
site 01B74   ; OUT ($BE),A
site 01B7A   ; OUT ($BE),A
site 01C07   ; OUT ($BE),A
site 01C0E   ; OUT ($BE),A
site 030C4   ; OUT ($BF),A
site 030CD   ; OUT ($BF),A
site 03107   ; OUTI
site 03109   ; OUTI
site 0310B   ; OUTI
site 0310D   ; OUTI
site 0310F   ; OUTI
site 03111   ; OUTI
site 03113   ; OUTI
site 03115   ; OUTI
site 03117   ; OUTI
site 03119   ; OUTI
site 0311B   ; OUTI
site 0311D   ; OUTI
site 0311F   ; OUTI
site 03121   ; OUTI
site 03123   ; OUTI
site 03125   ; OUTI
site 03127   ; OUTI
site 03129   ; OUTI
site 0312B   ; OUTI
site 0312D   ; OUTI
site 0312F   ; OUTI
site 03131   ; OUTI
site 03133   ; OUTI
site 03135   ; OUTI
site 03137   ; OUTI
site 03139   ; OUTI
site 0313B   ; OUTI
site 0313D   ; OUTI
site 0313F   ; OUTI
site 03141   ; OUTI
site 03143   ; OUTI
site 03145   ; OUTI
site 03147   ; OUTI
site 03149   ; OUTI
site 0314B   ; OUTI
site 0314D   ; OUTI
site 0314F   ; OUTI
site 03151   ; OUTI
site 03153   ; OUTI
site 03155   ; OUTI
site 03157   ; OUTI
site 03159   ; OUTI
site 0315B   ; OUTI
site 0315D   ; OUTI
site 0315F   ; OUTI
site 03161   ; OUTI
site 03163   ; OUTI
site 03165   ; OUTI
site 03167   ; OUTI
site 03169   ; OUTI
site 0316B   ; OUTI
site 0316D   ; OUTI
site 0316F   ; OUTI
site 03171   ; OUTI
site 03173   ; OUTI
site 03175   ; OUTI
site 03177   ; OUTI
site 03179   ; OUTI
site 0317B   ; OUTI
site 0317D   ; OUTI
site 0317F   ; OUTI
site 03181   ; OUTI
site 03183   ; OUTI
site 03185   ; OUTI
site 03187   ; OUTI
site 03189   ; OUTI
site 0318B   ; OUTI
site 0318D   ; OUTI
site 0318F   ; OUTI
site 03191   ; OUTI
site 03193   ; OUTI
site 03195   ; OUTI
site 03197   ; OUTI
site 03199   ; OUTI
site 0319B   ; OUTI
site 0319D   ; OUTI
site 0319F   ; OUTI
site 031A1   ; OUTI
site 031A3   ; OUTI
site 031A5   ; OUTI
site 031A7   ; OUTI
site 031A9   ; OUTI
site 031AB   ; OUTI
site 031AD   ; OUTI
site 031AF   ; OUTI
site 031B1   ; OUTI
site 031B3   ; OUTI
site 031B5   ; OUTI
site 031B7   ; OUTI
site 031B9   ; OUTI
site 031BB   ; OUTI
site 031BD   ; OUTI
site 031BF   ; OUTI
site 031C1   ; OUTI
site 031C3   ; OUTI
site 031C5   ; OUTI
site 031C7   ; OUTI
site 031C9   ; OUTI
site 031CB   ; OUTI
site 031CD   ; OUTI
site 031CF   ; OUTI
site 031D1   ; OUTI
site 031D3   ; OUTI
site 031D5   ; OUTI
site 031D7   ; OUTI
site 031D9   ; OUTI
site 031DB   ; OUTI
site 031DD   ; OUTI
site 031DF   ; OUTI
site 031E1   ; OUTI
site 031E3   ; OUTI
site 031E5   ; OUTI
site 031E7   ; OUTI
site 031E9   ; OUTI
site 031EB   ; OUTI
site 031ED   ; OUTI
site 031EF   ; OUTI
site 031F1   ; OUTI
site 031F3   ; OUTI
site 031F5   ; OUTI
site 031F7   ; OUTI
site 031F9   ; OUTI
site 031FB   ; OUTI
site 031FD   ; OUTI
site 031FF   ; OUTI
site 03201   ; OUTI
site 03203   ; OUTI
site 03205   ; OUTI
site 03207   ; OUTI
site 03209   ; OUTI
site 0320B   ; OUTI
site 0320D   ; OUTI
site 0320F   ; OUTI
site 03211   ; OUTI
site 03213   ; OUTI
site 03215   ; OUTI
site 03217   ; OUTI
site 03219   ; OUTI
site 0321B   ; OUTI
site 0321D   ; OUTI
site 0321F   ; OUTI
site 03221   ; OUTI
site 03223   ; OUTI
site 03225   ; OUTI
site 03227   ; OUTI
site 03229   ; OUTI
site 0322B   ; OUTI
site 0322D   ; OUTI
site 0322F   ; OUTI
site 03231   ; OUTI
site 03233   ; OUTI
site 03235   ; OUTI
site 03237   ; OUTI
site 03239   ; OUTI
site 0323B   ; OUTI
site 0323D   ; OUTI
site 0323F   ; OUTI
site 03241   ; OUTI
site 03243   ; OUTI
site 03245   ; OUTI
site 03247   ; OUTI
site 03249   ; OUTI
site 0324B   ; OUTI
site 0324D   ; OUTI
site 0324F   ; OUTI
site 03251   ; OUTI
site 03253   ; OUTI
site 03255   ; OUTI
site 03257   ; OUTI
site 03259   ; OUTI
site 0325B   ; OUTI
site 0325D   ; OUTI
site 0325F   ; OUTI
site 03261   ; OUTI
site 03263   ; OUTI
site 03265   ; OUTI
site 03267   ; OUTI
site 03269   ; OUTI
site 0326B   ; OUTI
site 0326D   ; OUTI
site 0326F   ; OUTI
site 03271   ; OUTI
site 03273   ; OUTI
site 03275   ; OUTI
site 03277   ; OUTI
site 03279   ; OUTI
site 0327B   ; OUTI
site 0327D   ; OUTI
site 0327F   ; OUTI
site 03281   ; OUTI
site 03283   ; OUTI
site 03285   ; OUTI
site 03287   ; OUTI
site 03289   ; OUTI
site 0328B   ; OUTI
site 0328D   ; OUTI
site 0328F   ; OUTI
site 03291   ; OUTI
site 03293   ; OUTI
site 03295   ; OUTI
site 03297   ; OUTI
site 03299   ; OUTI
site 0329B   ; OUTI
site 0329D   ; OUTI
site 0329F   ; OUTI
site 032A1   ; OUTI
site 032A3   ; OUTI
site 032A5   ; OUTI
site 032A7   ; OUTI
site 032A9   ; OUTI
site 032AB   ; OUTI
site 032AD   ; OUTI
site 032AF   ; OUTI
site 032B1   ; OUTI
site 032B3   ; OUTI
site 032B5   ; OUTI
site 032B7   ; OUTI
site 032B9   ; OUTI
site 032BB   ; OUTI
site 032BD   ; OUTI
site 032BF   ; OUTI
site 032C1   ; OUTI
site 032C3   ; OUTI
site 032C5   ; OUTI
site 032C7   ; OUTI
site 032C9   ; OUTI
site 032CB   ; OUTI
site 032CD   ; OUTI
site 032CF   ; OUTI
site 032D1   ; OUTI
site 032D3   ; OUTI
site 032D5   ; OUTI
site 032D7   ; OUTI
site 032D9   ; OUTI
site 032DB   ; OUTI
site 032DD   ; OUTI
site 032DF   ; OUTI
site 032E1   ; OUTI
site 032E3   ; OUTI
site 032E5   ; OUTI
site 032E7   ; OUTI
site 032E9   ; OUTI
site 032EB   ; OUTI
site 032ED   ; OUTI
site 032EF   ; OUTI
site 032F1   ; OUTI
site 032F3   ; OUTI
site 032F5   ; OUTI
site 032F7   ; OUTI
site 032F9   ; OUTI
site 032FB   ; OUTI
site 032FD   ; OUTI
site 032FF   ; OUTI
site 03301   ; OUTI
site 03303   ; OUTI
site 03305   ; OUTI
site 04C27   ; OUT ($BE),A
site 04C2E   ; OUT ($BE),A
site 063FF   ; IN A,($BF)
site 064AF   ; OUT ($BF),A
site 064B6   ; OUT ($BF),A
site 064BD   ; OUT ($BF),A
site 064C4   ; OUT ($BF),A
otir 06555   ; OUTI
site 0658C   ; OUT ($BF),A
site 06594   ; OUT ($BF),A
site 065A0   ; OUT ($BE),A
site 065A7   ; OUT ($BE),A
site 065CA   ; OUT ($BF),A
site 065D2   ; OUT ($BF),A
site 065D9   ; OUT ($BE),A
site 06604   ; OUT ($BE),A
site 06645   ; OUT ($BE),A
site 06670   ; OUT ($BE),A
site 0668E   ; OUT ($BE),A
site 06692   ; OUT ($BE),A
site 06699   ; OUT ($BE),A
site 066A1   ; OUT ($BF),A
site 066A8   ; OUT ($BF),A
site 066C0   ; OUT ($BF),A
site 066C7   ; OUT ($BF),A
site 066CE   ; OUT ($BF),A
site 066D5   ; OUT ($BF),A
site 06709   ; OUT ($BF),A
site 06710   ; OUT ($BF),A
site 06717   ; OUT ($BF),A
site 0671E   ; OUT ($BF),A
site 06726   ; OUT ($BF),A
site 0672D   ; OUT ($BF),A
site 06734   ; OUT ($BF),A
site 0673B   ; OUT ($BF),A
site 06746   ; OUT ($BF),A
site 0674D   ; OUT ($BF),A
site 06754   ; OUT ($BF),A
site 0675B   ; OUT ($BF),A
site 06763   ; OUT ($BF),A
site 0676A   ; OUT ($BF),A
site 06771   ; OUT ($BF),A
site 06778   ; OUT ($BF),A
site 06780   ; OUT ($BF),A
site 06787   ; OUT ($BF),A
site 0678E   ; OUT ($BF),A
site 06795   ; OUT ($BF),A
site 0679D   ; OUT ($BF),A
site 067A4   ; OUT ($BF),A
site 067AB   ; OUT ($BF),A
site 067B2   ; OUT ($BF),A
site 067D4   ; OUT ($BF),A
site 067DB   ; OUT ($BF),A
site 067E6   ; OUT ($BF),A
site 067ED   ; OUT ($BF),A
site 067F4   ; OUT ($BF),A
site 067FB   ; OUT ($BF),A
site 06803   ; OUT ($BF),A
site 0680A   ; OUT ($BF),A
site 06811   ; OUT ($BF),A
site 06818   ; OUT ($BF),A
site 06820   ; OUT ($BF),A
site 06827   ; OUT ($BF),A
site 0682E   ; OUT ($BF),A
site 06835   ; OUT ($BF),A
site 0683D   ; OUT ($BF),A
site 06844   ; OUT ($BF),A
site 0684B   ; OUT ($BF),A
site 06852   ; OUT ($BF),A
site 0685A   ; OUT ($BF),A
site 06861   ; OUT ($BF),A
site 06868   ; OUT ($BF),A
site 0686F   ; OUT ($BF),A
site 068AD   ; OUT ($BF),A
site 068B3   ; OUT ($BF),A
site 068C0   ; OUT ($BE),A
site 0E969   ; OUT ($7F),A
site 0E998   ; OUT ($7F),A
site 0E9C2   ; OUT ($7F),A
site 0E9C6   ; OUT ($7F),A
site 0E9ED   ; OUT ($7F),A
site 0EC9C   ; OUT ($7F),A
site 0ED14   ; OUT ($7F),A
site 0ED45   ; OTIR
site 13D13   ; OUTI
site 13D18   ; OUT ($BE),A
site 13D1C   ; OUT ($BE),A
site 13D20   ; OUT ($BE),A
site 13D37   ; OUTI
site 13D40   ; OUT ($BF),A
site 13D46   ; OUT ($BF),A
site 13E4F   ; OUT ($3F),A
site 13E55   ; IN A,($DD)
site 13E5F   ; OUT ($3F),A
site 13E61   ; IN A,($DD)
site 13E6A   ; OUT ($3F),A
site 17C9D   ; IN A,($DC)
site 17CA5   ; IN A,($DC)
site 17CAA   ; IN A,($DD)
site 17CBC   ; OUT ($DE),A
site 17CBE   ; IN A,($DC)
site 17CC3   ; OUT ($DE),A
site 17CC5   ; IN A,($DC)
site 17CD0   ; OUT ($DE),A
site 17CD2   ; IN A,($DC)
site 17CDD   ; OUT ($DE),A
site 17CDF   ; IN A,($DC)
site 17CF1   ; OUT ($DE),A
site 17CF3   ; IN A,($DC)
site 17CFE   ; OUT ($DE),A
site 17D00   ; IN A,($DC)
site 17D11   ; OUT ($DE),A
site 17D13   ; IN A,($DC)
site 17D18   ; IN A,($DD)
site 17D22   ; OUT ($DE),A
site 17D24   ; IN A,($DC)
site 17D36   ; OUT ($DE),A
site 17D38   ; IN A,($DC)
site 17D43   ; OUT ($DE),A
site 17D45   ; IN A,($DC)
site 17D50   ; OUT ($DE),A
site 17D52   ; IN A,($DD)
site 17D5D   ; OUT ($DE),A
site 17D5F   ; IN A,($DD)
site 1C033   ; OUT ($BF),A
site 1C03C   ; OUT ($BF),A
site 1C04A   ; OUTI
site 1C096   ; OUTI
site 1C0B6   ; OUT (C),D
site 1C0CA   ; OUTI
site 1C0D0   ; OUT (C),A
mapst 00029   ; LD ($FFFF),A
mapst 00030   ; LD ($FFFF),A
mapst 00051   ; LD ($FFFF),A
mapst 00058   ; LD ($FFFF),A
mapst 00077   ; LD ($FFFF),A
mapst 0007E   ; LD ($FFFF),A
mapst 00089   ; LD ($FFFF),A
mapst 00090   ; LD ($FFFF),A
mapst 0009A   ; LD ($FFFF),A
mapst 000AD   ; LD ($FFFF),A
mapst 00103   ; LD ($FFFF),A
mapst 001EF   ; LD ($FFFF),A
mapst 001F6   ; LD ($FFFF),A
mapst 002A3   ; LD ($FFFF),A
mapst 002AA   ; LD ($FFFF),A
mapst 003E0   ; LD ($FFFF),A
mapst 003E7   ; LD ($FFFF),A
mapst 0044A   ; LD ($FFFF),A
mapst 004B4   ; LD ($FFFF),A
mapst 004BB   ; LD ($FFFF),A
mapst 004F7   ; LD ($FFFF),A
mapst 004FE   ; LD ($FFFF),A
mapst 00561   ; LD ($FFFF),A
mapst 00568   ; LD ($FFFF),A
mapst 0064D   ; LD ($FFFF),A
mapst 00680   ; LD ($FFFF),A
mapst 0068D   ; LD ($FFFF),A
mapst 006F3   ; LD ($FFFF),A
mapst 006FA   ; LD ($FFFF),A
mapst 00741   ; LD ($FFFF),A
mapst 00748   ; LD ($FFFF),A
mapst 0078B   ; LD ($FFFF),A
mapst 00792   ; LD ($FFFF),A
mapst 007A0   ; LD ($FFFF),A
mapst 007CD   ; LD ($FFFF),A
mapst 0085F   ; LD ($FFFF),A
mapst 0086A   ; LD ($FFFF),A
mapst 00880   ; LD ($FFFF),A
mapst 00B0C   ; LD ($FFFF),A
mapst 00B46   ; LD ($FFFF),A
mapst 00B4E   ; LD ($FFFF),A
mapst 00D7E   ; LD ($FFFF),A
mapst 00D85   ; LD ($FFFF),A
mapst 0111A   ; LD ($FFFF),A
mapst 01135   ; LD ($FFFF),A
mapst 011F6   ; LD ($FFFF),A
mapst 01216   ; LD ($FFFF),A
mapst 013B2   ; LD ($FFFF),A
mapst 013B9   ; LD ($FFFF),A
mapst 01546   ; LD ($FFFF),A
mapst 0154D   ; LD ($FFFF),A
mapst 015D8   ; LD ($FFFF),A
mapst 015EB   ; LD ($FFFF),A
mapst 017ED   ; LD ($FFFF),A
mapst 0180A   ; LD ($FFFF),A
mapst 01830   ; LD ($FFFF),A
mapst 01849   ; LD ($FFFF),A
mapst 01883   ; LD ($FFFF),A
mapst 018A0   ; LD ($FFFF),A
mapst 018C2   ; LD ($FFFF),A
mapst 018DF   ; LD ($FFFF),A
mapst 01A96   ; LD ($FFFF),A
mapst 01A9D   ; LD ($FFFF),A
mapst 02758   ; LD ($FFFF),A
mapst 0275F   ; LD ($FFFF),A
mapst 02FEC   ; LD ($FFFF),A
mapst 02FF3   ; LD ($FFFF),A
mapst 03080   ; LD ($FFFF),A
mapst 03087   ; LD ($FFFF),A
mapst 0309D   ; LD ($FFFF),A
mapst 03103   ; LD ($FFFF),A
mapst 03615   ; LD ($FFFF),A
mapst 03624   ; LD ($FFFF),A
mapst 066E6   ; LD ($FFFF),A
mapst 066EF   ; LD ($FFFF),A
mapst 067C3   ; LD ($FFFF),A
mapst 067CC   ; LD ($FFFF),A
mapst 06880   ; LD ($FFFF),A
mapst 06889   ; LD ($FFFF),A
# CHECK ram_exec at 039F6 ($39F6 bank 0): CALL M,$FE09 $FE09
# CHECK ram_exec at 03A02 ($3A02 bank 0): JP M,$FA00 $FA00
# CHECK ram_exec at 03A06 ($3A06 bank 0): JP M,$FBF4 $FBF4
# CHECK ram_exec at 03A26 ($3A26 bank 0): CALL M,$FC03 $FC03
# CHECK ram_exec at 03A2A ($3A2A bank 0): CALL M,$FCFC $FCFC
# CHECK ram_exec at 03A2E ($3A2E bank 0): CALL M,$FE0D $FE0D
# CHECK indirect_unresolved at 030F9 ($30F9 bank 0): JP (IX) 
# low-confidence byte patterns checked by hand, real code: VDP register and VRAM routines not run in the detector run
site 00AB4   ; OUT ($BF),A
site 00ABB   ; OUT ($BF),A
site 00BB4   ; OUT ($BF),A
site 00BBA   ; OUT ($BF),A
site 066AF   ; OUT ($BF),A
site 066B5   ; OUT ($BF),A
site 066BA   ; OUT ($BE),A
# the other low-confidence byte patterns are data or instruction operands
