# Alex Kidd in Shinobi World (USA, Europe, Brazil) (En), CRC32 D2417ED7, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, checked against reference I/O logs
# (600 s of random input, 180 s of the attract mode): the scan found every I/O and mapper
# site that the logs ran.
# Decisions:
# - RST $08, $18 and $28 are the game's own table and VDP address routines, and they fill
#   $08-$30, so $0000-$0002 (DI; IM 1) is the io vector and the game starts at $0003.
# - $0387, $03B7 and $03D8 (VRAM loaders) and $043C (FM sound detection) are code that
#   nothing calls; their I/O is patched, at no cost.
# - The byte-scan I/O patterns in banks 5 to 14 lie where no path or recording reaches; the
#   high and medium ones, in banks 8 and 11, are graphics data (data/scan-verdicts.tsv).
# - The tile unpacker $0328 is the jr-z form of the Sega planar RLE decoder (sitescan rule 4):
#   it sets the VRAM address with RST $28 and writes each byte through a trap, which made the
#   loads before each round slow. The library page rle_tiles does the whole routine; the
#   routine's OUT ($BE),A at $033A keeps its site line but is no longer reached.
# - The frame handler's tile animation $6177 (called from $01B6 and $01E7) writes up to 160
#   rows of 3 tile bytes and a 0 to VRAM $0000, from the word at $C083, through unrolled OUTI
#   and OUT (C),A at $61C3-$66C9; $C085 picks how many rows. Through the traps it took about
#   half a frame, and play frames that ran it took 2 frames where the Master System took one.
#   Page 1, entry anim, builds the rows in a buffer and writes them with one jt_vwrite call;
#   the cave at $619C replaces the load of $C083 and $C085 and the jump to the rows.
# - workline 1: the frame handler writes the sprite table ($0277), then the sprite tiles
#   ($6177), then the scroll, with interrupts off to its end, and on the Next it ends a median
#   of 73 lines after it starts (p95 135). With the once-a-frame work at the ULA interrupt the
#   Next sprites were made from a half-written table or old tiles: ninjas drawn with their
#   heads apart from their bodies, or Alex with another pose's tiles. The work's line event
#   waits for the handler's EI, so the sprites are made from a whole frame.
name Alex Kidd in Shinobi World
cart D2417ED7
hz any		; No-Intro regions USA, Europe, Brazil
vector 00 io
workline 1
start 0003
site 0002A   ; OUT ($BF),A
site 0002D   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 00268   ; OUT ($BF),A
site 0026C   ; OUT ($BF),A
site 00272   ; OUTI
site 00278   ; OUT ($BF),A
site 0027C   ; OUT ($BF),A
site 00285   ; OUTI
site 0028B   ; OUT ($BF),A
site 0028E   ; OUT ($BF),A
site 00295   ; OUTI
site 002A8   ; OUT ($BF),A
site 002AC   ; OUT ($BF),A
site 002B0   ; OUT ($BF),A
site 002B4   ; OUT ($BF),A
site 0033A   ; OUT ($BE),A
site 00369   ; OUTI
site 0037A   ; OUT ($BE),A
site 0037F   ; OUT ($BE),A
site 0038C   ; OUTI
site 00392   ; OUT (C),A
site 003A6   ; OUTI
site 003CB   ; OUT (C),D
site 003DB   ; OUTI
site 003E1   ; OUT (C),A
site 003F3   ; OUT ($BF),A
site 003F6   ; OUT ($BF),A
site 00404   ; OUT ($BE),A
site 00412   ; IN A,($DC)
site 00421   ; IN A,($DC)
site 00426   ; IN A,($DD)
site 00434   ; IN A,($DD)
site 0045B   ; OUT ($3E),A
site 00463   ; OUT ($F2),A
site 00466   ; IN A,($F2)
site 00478   ; OUT ($F2),A
site 00480   ; OUT ($3E),A
site 00488   ; OUT ($3F),A
site 0048A   ; IN A,($DD)
site 00494   ; OUT ($3F),A
site 00496   ; IN A,($DD)
site 0049F   ; OUT ($3F),A
site 004A9   ; IN A,($BF)
site 004AF   ; IN A,($BF)
site 004B6   ; IN A,($BF)
site 00659   ; IN A,($BF)
site 0076F   ; IN A,($BE)
site 0078F   ; OUT ($BE),A
site 00AF6   ; OUT ($BF),A
site 00AFA   ; OUT ($BF),A
site 00B0E   ; OUT (C),L
site 00B19   ; OUT ($BF),A
site 00B1E   ; OUT ($BE),A
site 00B22   ; OUT ($BE),A
site 00C44   ; OUT ($BF),A
site 00C48   ; OUT ($BF),A
site 00C5D   ; OUT (C),L
site 00C62   ; OUT ($BF),A
site 00C67   ; OUT ($BE),A
site 00C6A   ; OUT ($BE),A
site 0190D   ; OUT ($BF),A
site 01911   ; OUT ($BF),A
site 01924   ; OUT ($BF),A
site 01928   ; OUT ($BF),A
site 01946   ; OUTI
site 01948   ; OUTI
site 0194A   ; OUTI
site 0194C   ; OUTI
site 0194E   ; OUTI
site 01950   ; OUTI
site 01952   ; OUTI
site 01954   ; OUTI
site 01956   ; OUTI
site 01958   ; OUTI
site 0195A   ; OUTI
site 0195C   ; OUTI
site 0195E   ; OUTI
site 01960   ; OUTI
site 01962   ; OUTI
site 01964   ; OUTI
site 01966   ; OUTI
site 01968   ; OUTI
site 0196A   ; OUTI
site 0196C   ; OUTI
site 0196E   ; OUTI
site 01970   ; OUTI
site 01972   ; OUTI
site 01974   ; OUTI
site 01976   ; OUTI
site 01978   ; OUTI
site 0197A   ; OUTI
site 0197C   ; OUTI
site 0197E   ; OUTI
site 01980   ; OUTI
site 01982   ; OUTI
site 01984   ; OUTI
site 01986   ; OUTI
site 01988   ; OUTI
site 0198A   ; OUTI
site 0198C   ; OUTI
site 0198E   ; OUTI
site 01990   ; OUTI
site 01992   ; OUTI
site 01994   ; OUTI
site 01996   ; OUTI
site 01998   ; OUTI
site 0199A   ; OUTI
site 0199C   ; OUTI
site 0199E   ; OUTI
site 019A0   ; OUTI
site 019A2   ; OUTI
site 019A4   ; OUTI
site 019A6   ; OUTI
site 019A8   ; OUTI
site 019AA   ; OUTI
site 019AC   ; OUTI
site 019AE   ; OUTI
site 019B0   ; OUTI
site 019B2   ; OUTI
site 019B4   ; OUTI
site 019B6   ; OUTI
site 019B8   ; OUTI
site 019BA   ; OUTI
site 019BC   ; OUTI
site 019BE   ; OUTI
site 019C0   ; OUTI
site 019C2   ; OUTI
site 019C4   ; OUTI
site 019C6   ; OUTI
site 019C8   ; OUTI
site 019CA   ; OUTI
site 019CC   ; OUTI
site 019CE   ; OUTI
site 019D0   ; OUTI
site 019D2   ; OUTI
site 019D4   ; OUTI
site 019D6   ; OUTI
site 019D8   ; OUTI
site 019DA   ; OUTI
site 019DC   ; OUTI
site 019DE   ; OUTI
site 019E0   ; OUTI
site 019E2   ; OUTI
site 019E4   ; OUTI
site 019E6   ; OUTI
site 019E8   ; OUTI
site 019EA   ; OUTI
site 019EC   ; OUTI
site 019EE   ; OUTI
site 019F0   ; OUTI
site 019F2   ; OUTI
site 019F4   ; OUTI
site 019F6   ; OUTI
site 019F8   ; OUTI
site 019FA   ; OUTI
site 019FC   ; OUTI
site 019FE   ; OUTI
site 01A00   ; OUTI
site 01A02   ; OUTI
site 01A04   ; OUTI
site 01A06   ; OUTI
site 01A08   ; OUTI
site 01A0A   ; OUTI
site 01A0C   ; OUTI
site 01A0E   ; OUTI
site 01A10   ; OUTI
site 01A12   ; OUTI
site 01A14   ; OUTI
site 01A16   ; OUTI
site 01A18   ; OUTI
site 01A1A   ; OUTI
site 01A1C   ; OUTI
site 01A1E   ; OUTI
site 01A20   ; OUTI
site 01A22   ; OUTI
site 01A24   ; OUTI
site 01A26   ; OUTI
site 01A28   ; OUTI
site 01A2A   ; OUTI
site 01A2C   ; OUTI
site 01A2E   ; OUTI
site 01A30   ; OUTI
site 01A32   ; OUTI
site 01A34   ; OUTI
site 01A36   ; OUTI
site 01A38   ; OUTI
site 01A3A   ; OUTI
site 01A3C   ; OUTI
site 01A3E   ; OUTI
site 01A40   ; OUTI
site 01A42   ; OUTI
site 01A44   ; OUTI
site 06194   ; OUT ($BF),A
site 06198   ; OUT ($BF),A
site 061C4   ; OUTI
site 061C6   ; OUTI
site 061C8   ; OUTI
site 061CA   ; OUT (C),A
site 061CC   ; OUTI
site 061CE   ; OUTI
site 061D0   ; OUTI
site 061D2   ; OUT (C),A
site 061D4   ; OUTI
site 061D6   ; OUTI
site 061D8   ; OUTI
site 061DA   ; OUT (C),A
site 061DC   ; OUTI
site 061DE   ; OUTI
site 061E0   ; OUTI
site 061E2   ; OUT (C),A
site 061E4   ; OUTI
site 061E6   ; OUTI
site 061E8   ; OUTI
site 061EA   ; OUT (C),A
site 061EC   ; OUTI
site 061EE   ; OUTI
site 061F0   ; OUTI
site 061F2   ; OUT (C),A
site 061F4   ; OUTI
site 061F6   ; OUTI
site 061F8   ; OUTI
site 061FA   ; OUT (C),A
site 061FC   ; OUTI
site 061FE   ; OUTI
site 06200   ; OUTI
site 06202   ; OUT (C),A
site 06204   ; OUTI
site 06206   ; OUTI
site 06208   ; OUTI
site 0620A   ; OUT (C),A
site 0620C   ; OUTI
site 0620E   ; OUTI
site 06210   ; OUTI
site 06212   ; OUT (C),A
site 06214   ; OUTI
site 06216   ; OUTI
site 06218   ; OUTI
site 0621A   ; OUT (C),A
site 0621C   ; OUTI
site 0621E   ; OUTI
site 06220   ; OUTI
site 06222   ; OUT (C),A
site 06224   ; OUTI
site 06226   ; OUTI
site 06228   ; OUTI
site 0622A   ; OUT (C),A
site 0622C   ; OUTI
site 0622E   ; OUTI
site 06230   ; OUTI
site 06232   ; OUT (C),A
site 06234   ; OUTI
site 06236   ; OUTI
site 06238   ; OUTI
site 0623A   ; OUT (C),A
site 0623C   ; OUTI
site 0623E   ; OUTI
site 06240   ; OUTI
site 06242   ; OUT (C),A
site 06245   ; OUTI
site 06247   ; OUTI
site 06249   ; OUTI
site 0624B   ; OUT (C),A
site 0624D   ; OUTI
site 0624F   ; OUTI
site 06251   ; OUTI
site 06253   ; OUT (C),A
site 06255   ; OUTI
site 06257   ; OUTI
site 06259   ; OUTI
site 0625B   ; OUT (C),A
site 0625D   ; OUTI
site 0625F   ; OUTI
site 06261   ; OUTI
site 06263   ; OUT (C),A
site 06265   ; OUTI
site 06267   ; OUTI
site 06269   ; OUTI
site 0626B   ; OUT (C),A
site 0626D   ; OUTI
site 0626F   ; OUTI
site 06271   ; OUTI
site 06273   ; OUT (C),A
site 06275   ; OUTI
site 06277   ; OUTI
site 06279   ; OUTI
site 0627B   ; OUT (C),A
site 0627D   ; OUTI
site 0627F   ; OUTI
site 06281   ; OUTI
site 06283   ; OUT (C),A
site 06285   ; OUTI
site 06287   ; OUTI
site 06289   ; OUTI
site 0628B   ; OUT (C),A
site 0628D   ; OUTI
site 0628F   ; OUTI
site 06291   ; OUTI
site 06293   ; OUT (C),A
site 06295   ; OUTI
site 06297   ; OUTI
site 06299   ; OUTI
site 0629B   ; OUT (C),A
site 0629D   ; OUTI
site 0629F   ; OUTI
site 062A1   ; OUTI
site 062A3   ; OUT (C),A
site 062A5   ; OUTI
site 062A7   ; OUTI
site 062A9   ; OUTI
site 062AB   ; OUT (C),A
site 062AD   ; OUTI
site 062AF   ; OUTI
site 062B1   ; OUTI
site 062B3   ; OUT (C),A
site 062B5   ; OUTI
site 062B7   ; OUTI
site 062B9   ; OUTI
site 062BB   ; OUT (C),A
site 062BD   ; OUTI
site 062BF   ; OUTI
site 062C1   ; OUTI
site 062C3   ; OUT (C),A
site 062C6   ; OUTI
site 062C8   ; OUTI
site 062CA   ; OUTI
site 062CC   ; OUT (C),A
site 062CE   ; OUTI
site 062D0   ; OUTI
site 062D2   ; OUTI
site 062D4   ; OUT (C),A
site 062D6   ; OUTI
site 062D8   ; OUTI
site 062DA   ; OUTI
site 062DC   ; OUT (C),A
site 062DE   ; OUTI
site 062E0   ; OUTI
site 062E2   ; OUTI
site 062E4   ; OUT (C),A
site 062E6   ; OUTI
site 062E8   ; OUTI
site 062EA   ; OUTI
site 062EC   ; OUT (C),A
site 062EE   ; OUTI
site 062F0   ; OUTI
site 062F2   ; OUTI
site 062F4   ; OUT (C),A
site 062F6   ; OUTI
site 062F8   ; OUTI
site 062FA   ; OUTI
site 062FC   ; OUT (C),A
site 062FE   ; OUTI
site 06300   ; OUTI
site 06302   ; OUTI
site 06304   ; OUT (C),A
site 06306   ; OUTI
site 06308   ; OUTI
site 0630A   ; OUTI
site 0630C   ; OUT (C),A
site 0630E   ; OUTI
site 06310   ; OUTI
site 06312   ; OUTI
site 06314   ; OUT (C),A
site 06316   ; OUTI
site 06318   ; OUTI
site 0631A   ; OUTI
site 0631C   ; OUT (C),A
site 0631E   ; OUTI
site 06320   ; OUTI
site 06322   ; OUTI
site 06324   ; OUT (C),A
site 06326   ; OUTI
site 06328   ; OUTI
site 0632A   ; OUTI
site 0632C   ; OUT (C),A
site 0632E   ; OUTI
site 06330   ; OUTI
site 06332   ; OUTI
site 06334   ; OUT (C),A
site 06336   ; OUTI
site 06338   ; OUTI
site 0633A   ; OUTI
site 0633C   ; OUT (C),A
site 0633E   ; OUTI
site 06340   ; OUTI
site 06342   ; OUTI
site 06344   ; OUT (C),A
site 06347   ; OUTI
site 06349   ; OUTI
site 0634B   ; OUTI
site 0634D   ; OUT (C),A
site 0634F   ; OUTI
site 06351   ; OUTI
site 06353   ; OUTI
site 06355   ; OUT (C),A
site 06357   ; OUTI
site 06359   ; OUTI
site 0635B   ; OUTI
site 0635D   ; OUT (C),A
site 0635F   ; OUTI
site 06361   ; OUTI
site 06363   ; OUTI
site 06365   ; OUT (C),A
site 06367   ; OUTI
site 06369   ; OUTI
site 0636B   ; OUTI
site 0636D   ; OUT (C),A
site 0636F   ; OUTI
site 06371   ; OUTI
site 06373   ; OUTI
site 06375   ; OUT (C),A
site 06377   ; OUTI
site 06379   ; OUTI
site 0637B   ; OUTI
site 0637D   ; OUT (C),A
site 0637F   ; OUTI
site 06381   ; OUTI
site 06383   ; OUTI
site 06385   ; OUT (C),A
site 06387   ; OUTI
site 06389   ; OUTI
site 0638B   ; OUTI
site 0638D   ; OUT (C),A
site 0638F   ; OUTI
site 06391   ; OUTI
site 06393   ; OUTI
site 06395   ; OUT (C),A
site 06397   ; OUTI
site 06399   ; OUTI
site 0639B   ; OUTI
site 0639D   ; OUT (C),A
site 0639F   ; OUTI
site 063A1   ; OUTI
site 063A3   ; OUTI
site 063A5   ; OUT (C),A
site 063A7   ; OUTI
site 063A9   ; OUTI
site 063AB   ; OUTI
site 063AD   ; OUT (C),A
site 063AF   ; OUTI
site 063B1   ; OUTI
site 063B3   ; OUTI
site 063B5   ; OUT (C),A
site 063B7   ; OUTI
site 063B9   ; OUTI
site 063BB   ; OUTI
site 063BD   ; OUT (C),A
site 063BF   ; OUTI
site 063C1   ; OUTI
site 063C3   ; OUTI
site 063C5   ; OUT (C),A
site 063C8   ; OUTI
site 063CA   ; OUTI
site 063CC   ; OUTI
site 063CE   ; OUT (C),A
site 063D0   ; OUTI
site 063D2   ; OUTI
site 063D4   ; OUTI
site 063D6   ; OUT (C),A
site 063D8   ; OUTI
site 063DA   ; OUTI
site 063DC   ; OUTI
site 063DE   ; OUT (C),A
site 063E0   ; OUTI
site 063E2   ; OUTI
site 063E4   ; OUTI
site 063E6   ; OUT (C),A
site 063E8   ; OUTI
site 063EA   ; OUTI
site 063EC   ; OUTI
site 063EE   ; OUT (C),A
site 063F0   ; OUTI
site 063F2   ; OUTI
site 063F4   ; OUTI
site 063F6   ; OUT (C),A
site 063F8   ; OUTI
site 063FA   ; OUTI
site 063FC   ; OUTI
site 063FE   ; OUT (C),A
site 06400   ; OUTI
site 06402   ; OUTI
site 06404   ; OUTI
site 06406   ; OUT (C),A
site 06408   ; OUTI
site 0640A   ; OUTI
site 0640C   ; OUTI
site 0640E   ; OUT (C),A
site 06410   ; OUTI
site 06412   ; OUTI
site 06414   ; OUTI
site 06416   ; OUT (C),A
site 06418   ; OUTI
site 0641A   ; OUTI
site 0641C   ; OUTI
site 0641E   ; OUT (C),A
site 06420   ; OUTI
site 06422   ; OUTI
site 06424   ; OUTI
site 06426   ; OUT (C),A
site 06428   ; OUTI
site 0642A   ; OUTI
site 0642C   ; OUTI
site 0642E   ; OUT (C),A
site 06430   ; OUTI
site 06432   ; OUTI
site 06434   ; OUTI
site 06436   ; OUT (C),A
site 06438   ; OUTI
site 0643A   ; OUTI
site 0643C   ; OUTI
site 0643E   ; OUT (C),A
site 06440   ; OUTI
site 06442   ; OUTI
site 06444   ; OUTI
site 06446   ; OUT (C),A
site 06448   ; OUTI
site 0644A   ; OUTI
site 0644C   ; OUTI
site 0644E   ; OUT (C),A
site 06450   ; OUTI
site 06452   ; OUTI
site 06454   ; OUTI
site 06456   ; OUT (C),A
site 06458   ; OUTI
site 0645A   ; OUTI
site 0645C   ; OUTI
site 0645E   ; OUT (C),A
site 06460   ; OUTI
site 06462   ; OUTI
site 06464   ; OUTI
site 06466   ; OUT (C),A
site 06468   ; OUTI
site 0646A   ; OUTI
site 0646C   ; OUTI
site 0646E   ; OUT (C),A
site 06470   ; OUTI
site 06472   ; OUTI
site 06474   ; OUTI
site 06476   ; OUT (C),A
site 06478   ; OUTI
site 0647A   ; OUTI
site 0647C   ; OUTI
site 0647E   ; OUT (C),A
site 06480   ; OUTI
site 06482   ; OUTI
site 06484   ; OUTI
site 06486   ; OUT (C),A
site 06488   ; OUTI
site 0648A   ; OUTI
site 0648C   ; OUTI
site 0648E   ; OUT (C),A
site 06490   ; OUTI
site 06492   ; OUTI
site 06494   ; OUTI
site 06496   ; OUT (C),A
site 06498   ; OUTI
site 0649A   ; OUTI
site 0649C   ; OUTI
site 0649E   ; OUT (C),A
site 064A0   ; OUTI
site 064A2   ; OUTI
site 064A4   ; OUTI
site 064A6   ; OUT (C),A
site 064A8   ; OUTI
site 064AA   ; OUTI
site 064AC   ; OUTI
site 064AE   ; OUT (C),A
site 064B0   ; OUTI
site 064B2   ; OUTI
site 064B4   ; OUTI
site 064B6   ; OUT (C),A
site 064B8   ; OUTI
site 064BA   ; OUTI
site 064BC   ; OUTI
site 064BE   ; OUT (C),A
site 064C0   ; OUTI
site 064C2   ; OUTI
site 064C4   ; OUTI
site 064C6   ; OUT (C),A
site 064C9   ; OUTI
site 064CB   ; OUTI
site 064CD   ; OUTI
site 064CF   ; OUT (C),A
site 064D1   ; OUTI
site 064D3   ; OUTI
site 064D5   ; OUTI
site 064D7   ; OUT (C),A
site 064D9   ; OUTI
site 064DB   ; OUTI
site 064DD   ; OUTI
site 064DF   ; OUT (C),A
site 064E1   ; OUTI
site 064E3   ; OUTI
site 064E5   ; OUTI
site 064E7   ; OUT (C),A
site 064E9   ; OUTI
site 064EB   ; OUTI
site 064ED   ; OUTI
site 064EF   ; OUT (C),A
site 064F1   ; OUTI
site 064F3   ; OUTI
site 064F5   ; OUTI
site 064F7   ; OUT (C),A
site 064F9   ; OUTI
site 064FB   ; OUTI
site 064FD   ; OUTI
site 064FF   ; OUT (C),A
site 06501   ; OUTI
site 06503   ; OUTI
site 06505   ; OUTI
site 06507   ; OUT (C),A
site 06509   ; OUTI
site 0650B   ; OUTI
site 0650D   ; OUTI
site 0650F   ; OUT (C),A
site 06511   ; OUTI
site 06513   ; OUTI
site 06515   ; OUTI
site 06517   ; OUT (C),A
site 06519   ; OUTI
site 0651B   ; OUTI
site 0651D   ; OUTI
site 0651F   ; OUT (C),A
site 06521   ; OUTI
site 06523   ; OUTI
site 06525   ; OUTI
site 06527   ; OUT (C),A
site 06529   ; OUTI
site 0652B   ; OUTI
site 0652D   ; OUTI
site 0652F   ; OUT (C),A
site 06531   ; OUTI
site 06533   ; OUTI
site 06535   ; OUTI
site 06537   ; OUT (C),A
site 06539   ; OUTI
site 0653B   ; OUTI
site 0653D   ; OUTI
site 0653F   ; OUT (C),A
site 06541   ; OUTI
site 06543   ; OUTI
site 06545   ; OUTI
site 06547   ; OUT (C),A
site 06549   ; OUTI
site 0654B   ; OUTI
site 0654D   ; OUTI
site 0654F   ; OUT (C),A
site 06551   ; OUTI
site 06553   ; OUTI
site 06555   ; OUTI
site 06557   ; OUT (C),A
site 06559   ; OUTI
site 0655B   ; OUTI
site 0655D   ; OUTI
site 0655F   ; OUT (C),A
site 06561   ; OUTI
site 06563   ; OUTI
site 06565   ; OUTI
site 06567   ; OUT (C),A
site 06569   ; OUTI
site 0656B   ; OUTI
site 0656D   ; OUTI
site 0656F   ; OUT (C),A
site 06571   ; OUTI
site 06573   ; OUTI
site 06575   ; OUTI
site 06577   ; OUT (C),A
site 06579   ; OUTI
site 0657B   ; OUTI
site 0657D   ; OUTI
site 0657F   ; OUT (C),A
site 06581   ; OUTI
site 06583   ; OUTI
site 06585   ; OUTI
site 06587   ; OUT (C),A
site 06589   ; OUTI
site 0658B   ; OUTI
site 0658D   ; OUTI
site 0658F   ; OUT (C),A
site 06591   ; OUTI
site 06593   ; OUTI
site 06595   ; OUTI
site 06597   ; OUT (C),A
site 06599   ; OUTI
site 0659B   ; OUTI
site 0659D   ; OUTI
site 0659F   ; OUT (C),A
site 065A1   ; OUTI
site 065A3   ; OUTI
site 065A5   ; OUTI
site 065A7   ; OUT (C),A
site 065A9   ; OUTI
site 065AB   ; OUTI
site 065AD   ; OUTI
site 065AF   ; OUT (C),A
site 065B1   ; OUTI
site 065B3   ; OUTI
site 065B5   ; OUTI
site 065B7   ; OUT (C),A
site 065B9   ; OUTI
site 065BB   ; OUTI
site 065BD   ; OUTI
site 065BF   ; OUT (C),A
site 065C1   ; OUTI
site 065C3   ; OUTI
site 065C5   ; OUTI
site 065C7   ; OUT (C),A
site 065CA   ; OUTI
site 065CC   ; OUTI
site 065CE   ; OUTI
site 065D0   ; OUT (C),A
site 065D2   ; OUTI
site 065D4   ; OUTI
site 065D6   ; OUTI
site 065D8   ; OUT (C),A
site 065DA   ; OUTI
site 065DC   ; OUTI
site 065DE   ; OUTI
site 065E0   ; OUT (C),A
site 065E2   ; OUTI
site 065E4   ; OUTI
site 065E6   ; OUTI
site 065E8   ; OUT (C),A
site 065EA   ; OUTI
site 065EC   ; OUTI
site 065EE   ; OUTI
site 065F0   ; OUT (C),A
site 065F2   ; OUTI
site 065F4   ; OUTI
site 065F6   ; OUTI
site 065F8   ; OUT (C),A
site 065FA   ; OUTI
site 065FC   ; OUTI
site 065FE   ; OUTI
site 06600   ; OUT (C),A
site 06602   ; OUTI
site 06604   ; OUTI
site 06606   ; OUTI
site 06608   ; OUT (C),A
site 0660A   ; OUTI
site 0660C   ; OUTI
site 0660E   ; OUTI
site 06610   ; OUT (C),A
site 06612   ; OUTI
site 06614   ; OUTI
site 06616   ; OUTI
site 06618   ; OUT (C),A
site 0661A   ; OUTI
site 0661C   ; OUTI
site 0661E   ; OUTI
site 06620   ; OUT (C),A
site 06622   ; OUTI
site 06624   ; OUTI
site 06626   ; OUTI
site 06628   ; OUT (C),A
site 0662A   ; OUTI
site 0662C   ; OUTI
site 0662E   ; OUTI
site 06630   ; OUT (C),A
site 06632   ; OUTI
site 06634   ; OUTI
site 06636   ; OUTI
site 06638   ; OUT (C),A
site 0663A   ; OUTI
site 0663C   ; OUTI
site 0663E   ; OUTI
site 06640   ; OUT (C),A
site 06642   ; OUTI
site 06644   ; OUTI
site 06646   ; OUTI
site 06648   ; OUT (C),A
site 0664A   ; OUTI
site 0664C   ; OUTI
site 0664E   ; OUTI
site 06650   ; OUT (C),A
site 06652   ; OUTI
site 06654   ; OUTI
site 06656   ; OUTI
site 06658   ; OUT (C),A
site 0665A   ; OUTI
site 0665C   ; OUTI
site 0665E   ; OUTI
site 06660   ; OUT (C),A
site 06662   ; OUTI
site 06664   ; OUTI
site 06666   ; OUTI
site 06668   ; OUT (C),A
site 0666A   ; OUTI
site 0666C   ; OUTI
site 0666E   ; OUTI
site 06670   ; OUT (C),A
site 06672   ; OUTI
site 06674   ; OUTI
site 06676   ; OUTI
site 06678   ; OUT (C),A
site 0667A   ; OUTI
site 0667C   ; OUTI
site 0667E   ; OUTI
site 06680   ; OUT (C),A
site 06682   ; OUTI
site 06684   ; OUTI
site 06686   ; OUTI
site 06688   ; OUT (C),A
site 0668A   ; OUTI
site 0668C   ; OUTI
site 0668E   ; OUTI
site 06690   ; OUT (C),A
site 06692   ; OUTI
site 06694   ; OUTI
site 06696   ; OUTI
site 06698   ; OUT (C),A
site 0669A   ; OUTI
site 0669C   ; OUTI
site 0669E   ; OUTI
site 066A0   ; OUT (C),A
site 066A2   ; OUTI
site 066A4   ; OUTI
site 066A6   ; OUTI
site 066A8   ; OUT (C),A
site 066AA   ; OUTI
site 066AC   ; OUTI
site 066AE   ; OUTI
site 066B0   ; OUT (C),A
site 066B2   ; OUTI
site 066B4   ; OUTI
site 066B6   ; OUTI
site 066B8   ; OUT (C),A
site 066BA   ; OUTI
site 066BC   ; OUTI
site 066BE   ; OUTI
site 066C0   ; OUT (C),A
site 066C2   ; OUTI
site 066C4   ; OUTI
site 066C6   ; OUTI
site 066C8   ; OUT (C),A
site 07592   ; OUTI
site 07595   ; OUTI
site 08507   ; OTIR
site 0857B   ; OUT ($7F),A
site 08727   ; OTIR
site 08839   ; OUT ($7F),A
site 08843   ; OUT ($7F),A
site 0885B   ; OUT ($7F),A
site 088D1   ; OUT ($7F),A
site 08932   ; OUT ($7F),A
site 0893E   ; OUT ($7F),A
site 08942   ; OUT ($7F),A
site 08968   ; OUT ($7F),A
site 08A70   ; OUT ($7F),A
site 08A7C   ; OUT ($7F),A
site 08AAA   ; OUT ($7F),A
mapst 0009E   ; LD ($FFFF),A
mapst 000A5   ; LD ($FFFF),A
mapldk 000BB   # LD HL,$FFFC; LD (HL),$80
maphl 000C1   # LD (HL),$00, HL = $FFFD
maphl 000C4   # LD (HL),$01, HL = $FFFE
maphl 000C7   # LD (HL),$02, HL = $FFFF
mapst 0010A   ; LD ($FFFF),A
mapst 0012C   ; LD ($FFFF),A
mapst 0016B   ; LD ($FFFF),A
mapst 00210   ; LD ($FFFF),A
mapst 0021F   ; LD ($FFFF),A
mapst 00744   ; LD ($FFFF),A
mapst 0086F   ; LD ($FFFF),A
mapst 008E2   ; LD ($FFFF),A
mapst 009BC   ; LD ($FFFF),A
mapst 00C95   ; LD ($FFFF),A
mapst 00D16   ; LD ($FFFF),A
mapst 00D39   ; LD ($FFFF),A
mapst 00DDE   ; LD ($FFFF),A
mapst 00E02   ; LD ($FFFF),A
mapst 00E5F   ; LD ($FFFF),A
mapst 00E6D   ; LD ($FFFF),A
mapst 00EED   ; LD ($FFFF),A
mapst 00F30   ; LD ($FFFF),A
mapst 00FBC   ; LD ($FFFF),A
mapst 011BB   ; LD ($FFFF),A
mapst 011D3   ; LD ($FFFF),A
mapst 011EE   ; LD ($FFFF),A
mapst 01293   ; LD ($FFFF),A
mapst 0130C   ; LD ($FFFF),A
mapst 01319   ; LD ($FFFF),A
mapst 01327   ; LD ($FFFF),A
mapst 01334   ; LD ($FFFF),A
mapst 01340   ; LD ($FFFF),A
mapst 014D3   ; LD ($FFFF),A
mapst 014F4   ; LD ($FFFF),A
mapst 01565   ; LD ($FFFF),A
mapst 0171C   ; LD ($FFFF),A
mapst 01908   ; LD ($FFFF),A
mapst 01936   ; LD ($FFFF),A
mapst 01C14   ; LD ($FFFF),A
mapst 02CC3   ; LD ($FFFF),A
mapst 02EB1   ; LD ($FFFF),A
mapst 02ED0   ; LD ($FFFF),A
mapst 02EE6   ; LD ($FFFF),A
mapst 04969   ; LD ($FFFF),A
mapld 049D0   # LD HL,$FFFF; LD (HL),$0C
mapst 04B04   ; LD ($FFFF),A
mapst 04CE3   ; LD ($FFFF),A
mapst 04D2B   ; LD ($FFFF),A
mapst 05063   ; LD ($FFFF),A
mapst 0618F   ; LD ($FFFF),A
mapst 066CD   ; LD ($FFFF),A
mapst 06D0A   ; LD ($FFFF),A
mapst 06D2E   ; LD ($FFFF),A
mapst 06FA0   ; LD ($FFFF),A
mapst 06FF8   ; LD ($FFFF),A
mapst 07029   ; LD ($FFFF),A
mapst 070A0   ; LD ($FFFF),A
mapst 070AE   ; LD ($FFFF),A
mapst 070D7   ; LD ($FFFF),A
mapst 070F6   ; LD ($FFFF),A
mapst 071F9   ; LD ($FFFF),A
mapst 07322   ; LD ($FFFF),A
mapst 07423   ; LD ($FFFF),A
mapst 074CD   ; LD ($FFFF),A
asm 00328 5          ; LD B,4 : EX AF,AF' : LD A,B : EX AF,AF': the routine is rle_tiles
    rst $00
    db far_io, pg_rle_tiles, ent_rle_tiles
    ret
endasm
libpage 0 rle_tiles  ; overlays/lib/rle_tiles.asm

asm 0619C 6          ; LD HL,($C083) : LD A,($C085): the rows are page 1, entry anim
    rst $00
    db far_io, pg_anim, ent_anim
    ret
endasm

page 1 anim
; anim: the tile animation rows of $61C3-$66C9. VRAM $0000 on: rows of the 3 bytes at
; ($C083) on and a 0, as many rows as $C085 picks (10: 160, 9: 144, 8: 128, 7: 112, 4: 64,
; 2: 32, any other: 96). It builds the rows in buf and writes them with one jt_vwrite call,
; in runs of 64 bytes (16 rows). Returns as the rows do: HL past the data, A = 0, C = $BE,
; B less 3 for each row; DE, IX and IY kept. F is not as the rows leave it: the callers
; ($01B9, $01E7) load A and test it before any flag is read. Interrupts stay as they were
; (the frame handler runs with them off). The data is read as the game sees it (jt_peek
; when HL is in $2000-$3FFF).
anim:
    ld (a_ix),ix
    ld (a_iy),iy
    ld (a_de),de
    ld a,b
    ld (a_b),a
    ld hl,($C083)
    ld (a_hl),hl
    ld a,($C085)
    ld c,160
    cp 10
    jr z,.go
    ld c,144
    cp 9
    jr z,.go
    ld c,128
    cp 8
    jr z,.go
    ld c,112
    cp 7
    jr z,.go
    ld c,64
    cp 4
    jr z,.go
    ld c,32
    cp 2
    jr z,.go
    ld c,96
.go:
    ld a,c
    ld (a_n),a
    ld b,c
    ld de,buf
    ld a,h
    and $E0
    cp $20
    jr z,.peek
.row:                   ; the data outside $2000-$3FFF: plain reads
    ldi
    ldi
    ldi
    xor a
    ld (de),a
    inc de
    inc bc              ; LDI counts BC down: keep B as the row count
    inc bc
    inc bc
    djnz .row
    jr .write
.peek:
    call jt_peek
    ld (de),a
    inc de
    inc hl
    call jt_peek
    ld (de),a
    inc de
    inc hl
    call jt_peek
    ld (de),a
    inc de
    inc hl
    xor a
    ld (de),a
    inc de
    djnz .peek
.write:
    ld a,(a_n)
    rrca
    rrca
    rrca
    rrca
    ld c,a              ; runs of 16 rows
    ld b,64
    ld hl,buf
    ld de,$0000
    ld ix,64
    ld iy,64
    ld a,1              ; the source in this page
    call jt_vwrite
    ld a,(a_n)          ; HL = start + 3 * rows, B = B - 3 * rows
    ld e,a
    ld d,0
    ld hl,(a_hl)
    add hl,de
    add hl,de
    add hl,de
    ld b,a
    add a,b
    add a,b
    ld b,a
    ld a,(a_b)
    sub b
    ld b,a
    ld c,$BE
    ld de,(a_de)
    ld ix,(a_ix)
    ld iy,(a_iy)
    xor a
    ret
a_ix:   dw 0
a_iy:   dw 0
a_de:   dw 0
a_hl:   dw 0
a_b:    db 0
a_n:    db 0
buf:    ds 640
endpage

# Alex Kidd in Shinobi World (USA, Europe, Brazil).cht, "Infinite Lives": RAM $C22F is the
# lives count, held at 9
poke "Infinite lives"
ar 00C2-2F09
endpoke

# Alex Kidd in Shinobi World (USA, Europe, Brazil).cht, "Infinite Hits": RAM $C22E is the
# hits left, held at 3 (full)
poke "Infinite energy"
ar 00C2-2E03
endpoke

# Alex Kidd in Shinobi World (USA, Europe, Brazil).cht, "Invincibility (blinking) (Disable
# to pickup items)": RAM $C227 is the blink flag, $C228 the blink timer; both held, so no hit
# lands and items cannot be picked up
poke "Invincibility"
ar 00C2-2781
ar 00C2-2830
endpoke

# Alex Kidd in Shinobi World (USA, Europe, Brazil).cht, "Get Hit Once For Invincibility":
# RAM $C228 held at $FF; after the first hit the blink never ends and no more hits land
poke "Invincible after hit"
ar 00C2-28FF
endpoke

# Alex Kidd in Shinobi World (USA, Europe) (Action Replay).cht, "Have Weapon": RAM $C22C is
# the weapon, 00 to 03 each give a different attack
poke "Weapon ??"
ar 00C2-2C??
endpoke

# Alex Kidd in Shinobi World (USA, Europe, Brazil).cht, "Moon Jump": RAM $C223 held at 0; a
# held jump climbs higher and stays up longer
poke "Higher jump"
ar 00C2-2300
endpoke

# Alex Kidd in Shinobi World (USA, Europe, Brazil).cht, "Multi-Jump": RAM $C222 is the
# in-air flag, held at 0; a jump can be pressed again in the air
poke "Multi-jump"
ar 00C2-2200
endpoke

# Alex Kidd in Shinobi World (USA, Europe, Brazil).cht, "Start with ?? Health Units, instead
# of 3": the first code sets the hits at the start of a game, the second after a life is lost
poke "Start with 4 hits"
gg 040-028-E66
gg 040-44E-E66
endpoke

# Alex Kidd in Shinobi World (USA, Europe, Brazil).cht, "Start with ?? Lives, instead of 2"
poke "Start with 3 lives"
gg 03D-EFE-E62
endpoke
