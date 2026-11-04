# Ys - The Vanished Omens (USA, Europe, Brazil) (En), CRC32 B33E2827, 256K, Sega mapper,
# battery-backed cart RAM.
# Drafted by tools/mkspec.py from sitescan output with two 600 s reference I/O logs (random
# input from power on; button presses, then random input), plus these entries given with
# --entry, because no scanned path or recording reached them:
# - the room event handlers: bank 1 $4C13-$609E, every handler address in the per-room jump
#   tables that the table at $4ABF names ($4BA6 indexes it by ($C181) & $7F; 4-byte entries,
#   data address then jump table; the RST $08 at $4BB8 dispatches);
# - bank 7 $8180, the unrolled OUTI and OUT ($BE),A run that $8856 enters through
#   PUSH DE; RET at addresses from the table at bank 7 $8000;
# - bank 9 $BEFB, the VDP routine that bank 0 $3113-$3140 calls (CALL $BEFB after bank 9 is
#   mapped at $3108).
# Decisions:
# - No free RST vector ($0008, $0018 and $0028 are the game's; $0010, $0020 and $0030 are
#   inside them), so $0000 is the io vector.
# - The status bar is a split screen: the line handlers at $0587-$05EC set register 8 to 0
#   at line 159 and move the name table (register 2) to $2000 at lines 159 and 175 and back
#   to $3800 at lines 167 and 183. Each register 2 move rebuilds the Next maps, so the
#   playfield showed black in many frames. Register 2 stays $FF here (the two LD A,$F9 at
#   $0595 and $05CD load $FF), so the playfield shows in every frame. The rows from the
#   $2000 table, the status bar's PLAYER and ENEMY lines, cannot show on the Next without
#   a second name table in the engine.
# - The I/O ports $F0 and $F2 are the FM unit: the game looks for it at power on.
# - The byte-scan I/O patterns that no path reached are graphics and two word tables
#   (data/scan-verdicts.tsv).
name Ys - The Vanished Omens
hz any		; No-Intro regions USA, Europe, Brazil
cart B33E2827
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
# The status bar split: register 2 stays $FF (name table $3800); see the header.
asm 00595 2   ; LD A,$F9 -> LD A,$FF
    ld a,$ff
endasm
asm 005CD 2   ; LD A,$F9 -> LD A,$FF
    ld a,$ff
endasm
site 0002A   ; OUT ($BF),A
site 0002D   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0010E   ; OUTD
site 00110   ; OUT (C),B
site 00112   ; OUTD
site 00114   ; OUT (C),B
site 00116   ; OUTD
site 00118   ; OUT (C),B
site 0011D   ; OUT (C),L
site 0011F   ; OUT (C),H
site 00138   ; IN A,($DD)
site 00178   ; OUT ($BF),A
site 0017C   ; OUT ($BF),A
site 00180   ; OUT ($BF),A
site 00184   ; OUT ($BF),A
site 00189   ; OUT ($BF),A
site 0018D   ; OUT ($BF),A
site 0021D   ; OUT ($BE),A
site 00221   ; OUT ($BE),A
site 00227   ; OUT ($BE),A
site 0022B   ; OUT ($BE),A
site 00231   ; OUT ($BE),A
site 00235   ; OUT ($BE),A
site 00245   ; OUT ($BE),A
site 00249   ; OUT ($BE),A
site 0024F   ; OUT ($BE),A
site 00253   ; OUT ($BE),A
site 00259   ; OUT ($BE),A
site 0025D   ; OUT ($BE),A
site 0026D   ; OUT ($BE),A
site 00271   ; OUT ($BE),A
site 00277   ; OUT ($BE),A
site 0027B   ; OUT ($BE),A
site 00281   ; OUT ($BE),A
site 00285   ; OUT ($BE),A
site 0029F   ; OUT ($BE),A
site 002A3   ; OUT ($BE),A
site 002BC   ; OUT ($BE),A
site 002BF   ; OUT ($BE),A
site 002CF   ; OUT ($BF),A
site 002D2   ; OUT ($BF),A
site 002E6   ; OUTI
site 002E8   ; OUT ($BE),A
site 002EA   ; OUTI
site 002EC   ; OUT ($BE),A
site 002EE   ; OUTI
site 002F0   ; OUT ($BE),A
site 002F2   ; OUTI
site 002F4   ; OUT ($BE),A
site 002F6   ; OUTI
site 002F8   ; OUT ($BE),A
site 002FA   ; OUTI
site 002FC   ; OUT ($BE),A
site 002FE   ; OUTI
site 00300   ; OUT ($BE),A
site 00302   ; OUTI
site 00304   ; OUT ($BE),A
site 00306   ; OUTI
site 00308   ; OUT ($BE),A
site 0030A   ; OUTI
site 0030C   ; OUT ($BE),A
site 0030E   ; OUTI
site 00310   ; OUT ($BE),A
site 00312   ; OUTI
site 00314   ; OUT ($BE),A
site 00316   ; OUTI
site 00318   ; OUT ($BE),A
site 0031A   ; OUTI
site 0031C   ; OUT ($BE),A
site 0031E   ; OUTI
site 00320   ; OUT ($BE),A
site 00322   ; OUTI
site 00324   ; OUT ($BE),A
site 0032E   ; OUT ($BF),A
site 00331   ; OUT ($BF),A
site 00336   ; OUT ($BE),A
site 00345   ; OUT ($BF),A
site 00348   ; OUT ($BF),A
otir 00353   ; OUTI
site 00367   ; OUT ($BF),A
site 0036A   ; OUT ($BF),A
site 00377   ; OUT (C),E
site 00379   ; OUT (C),D
site 00380   ; OUT ($BE),A
site 00384   ; OUT ($BE),A
site 00395   ; OUT ($BF),A
site 00398   ; OUT ($BF),A
site 003A3   ; OTIR
site 003AA   ; OUT ($BF),A
site 003AD   ; OUT ($BF),A
site 003D6   ; OUTI
site 003D8   ; OUTI
site 003DB   ; OUTI
site 003DD   ; OUTI
site 003F5   ; OUT ($BF),A
site 003F9   ; OUT ($BF),A
site 00401   ; OUTI
site 00415   ; OUT ($BF),A
site 00419   ; OUT ($BF),A
site 00420   ; OUTI
site 00422   ; OUTI
site 00424   ; OUTI
site 00428   ; OUT ($BF),A
site 0042C   ; OUT ($BF),A
site 00437   ; OUT ($BF),A
site 0043A   ; OUT ($BF),A
site 0043F   ; OUTI
site 00441   ; OUTI
site 00443   ; OUTI
site 00445   ; OUTI
site 00447   ; OUTI
site 00449   ; OUTI
site 0044B   ; OUTI
site 0044D   ; OUTI
site 0044F   ; OUTI
site 00451   ; OUTI
site 00453   ; OUTI
site 00455   ; OUTI
site 00457   ; OUTI
site 00459   ; OUTI
site 0045B   ; OUTI
site 0045D   ; OUTI
site 0045F   ; OUTI
site 00461   ; OUTI
site 00463   ; OUTI
site 00465   ; OUTI
site 00467   ; OUTI
site 00469   ; OUTI
site 0046B   ; OUTI
site 0046D   ; OUTI
site 0046F   ; OUTI
site 00471   ; OUTI
site 00473   ; OUTI
site 00475   ; OUTI
site 00477   ; OUTI
site 00479   ; OUTI
site 0047B   ; OUTI
site 0047D   ; OUTI
site 0047F   ; OUTI
site 00481   ; OUTI
site 00483   ; OUTI
site 00485   ; OUTI
site 00487   ; OUTI
site 00489   ; OUTI
site 0048B   ; OUTI
site 0048D   ; OUTI
site 0048F   ; OUTI
site 00491   ; OUTI
site 00493   ; OUTI
site 00495   ; OUTI
site 00497   ; OUTI
site 00499   ; OUTI
site 0049B   ; OUTI
site 0049D   ; OUTI
site 0049F   ; OUTI
site 004A1   ; OUTI
site 004A3   ; OUTI
site 004A5   ; OUTI
site 004A7   ; OUTI
site 004A9   ; OUTI
site 004AB   ; OUTI
site 004AD   ; OUTI
site 004AF   ; OUTI
site 004B1   ; OUTI
site 004B3   ; OUTI
site 004B5   ; OUTI
site 004B7   ; OUTI
site 004B9   ; OUTI
site 004BB   ; OUTI
site 004BD   ; OUTI
site 004BF   ; OUTI
site 004C1   ; OUTI
site 004C3   ; OUTI
site 004C5   ; OUTI
site 004C7   ; OUTI
site 004C9   ; OUTI
site 004CB   ; OUTI
site 004CD   ; OUTI
site 004CF   ; OUTI
site 004D1   ; OUTI
site 004D3   ; OUTI
site 004D5   ; OUTI
site 004D7   ; OUTI
site 004D9   ; OUTI
site 004DB   ; OUTI
site 004DD   ; OUTI
site 004DF   ; OUTI
site 004E1   ; OUTI
site 004E3   ; OUTI
site 004E5   ; OUTI
site 004E7   ; OUTI
site 004E9   ; OUTI
site 004EB   ; OUTI
site 004ED   ; OUTI
site 004EF   ; OUTI
site 004F1   ; OUTI
site 004F3   ; OUTI
site 004F5   ; OUTI
site 004F7   ; OUTI
site 004F9   ; OUTI
site 004FB   ; OUTI
site 004FD   ; OUTI
site 004FF   ; OUTI
site 00501   ; OUTI
site 00503   ; OUTI
site 00505   ; OUTI
site 00507   ; OUTI
site 00509   ; OUTI
site 0050B   ; OUTI
site 0050D   ; OUTI
site 0050F   ; OUTI
site 00511   ; OUTI
site 00513   ; OUTI
site 00515   ; OUTI
site 00517   ; OUTI
site 00519   ; OUTI
site 0051B   ; OUTI
site 0051D   ; OUTI
site 0051F   ; OUTI
site 00521   ; OUTI
site 00523   ; OUTI
site 00525   ; OUTI
site 00527   ; OUTI
site 00529   ; OUTI
site 0052B   ; OUTI
site 0052D   ; OUTI
site 0052F   ; OUTI
site 00531   ; OUTI
site 00533   ; OUTI
site 00535   ; OUTI
site 00537   ; OUTI
site 00539   ; OUTI
site 0053B   ; OUTI
site 0053D   ; OUTI
site 00547   ; OUT ($BF),A
site 0054B   ; OUT ($BF),A
site 00559   ; OUT ($BF),A
site 0055D   ; OUT ($BF),A
site 00577   ; OUT ($BF),A
site 0057B   ; OUT ($BF),A
site 0058F   ; OUT ($BF),A
site 00593   ; OUT ($BF),A
site 00597   ; OUT ($BF),A
site 0059B   ; OUT ($BF),A
site 0059F   ; OUT ($BF),A
site 005A3   ; OUT ($BF),A
site 005B6   ; OUT ($BF),A
site 005BA   ; OUT ($BF),A
site 005C7   ; OUT ($BF),A
site 005CB   ; OUT ($BF),A
site 005CF   ; OUT ($BF),A
site 005D3   ; OUT ($BF),A
site 005E0   ; OUT ($BF),A
site 005E4   ; OUT ($BF),A
site 005E8   ; OUT ($BF),A
site 005EC   ; OUT ($BF),A
site 0060B   ; OUT ($BF),A
site 0060F   ; OUT ($BF),A
site 00617   ; OUTI
site 0063F   ; OUT (C),L
site 00641   ; OUT (C),H
site 00649   ; OUTI
site 00652   ; OUTI
site 00654   ; OUTI
site 00659   ; OUTI
site 00676   ; OUT (C),L
site 00678   ; OUT (C),H
site 00680   ; OUTI
site 00689   ; OUTI
site 0068B   ; OUTI
site 00690   ; OUTI
site 006A6   ; OUT ($BE),A
site 006CB   ; OUTI
site 006DB   ; OUT ($BE),A
site 006E0   ; OUT ($BE),A
site 006ED   ; OUTI
site 006F3   ; OUT (C),A
site 00707   ; OUTI
site 0072C   ; OUT (C),D
site 0073C   ; OUTI
site 00742   ; OUT (C),A
site 00754   ; OUT ($BF),A
site 00757   ; OUT ($BF),A
site 00765   ; OUT ($BE),A
site 00773   ; IN A,($DC)
site 00AB0   ; IN A,($BF)
site 00BAA   ; OUT ($BE),A
site 00BAF   ; OUT ($BE),A
site 00D64   ; IN A,($BE)
site 00D6D   ; OUT ($BE),A
site 01FAD   ; IN A,($BE)
site 01FCA   ; OUT ($BE),A
site 0280E   ; OUT (C),L
site 02810   ; OUT (C),H
site 02830   ; OUT ($BF),A
site 02833   ; OUT ($BF),A
site 0283C   ; OUTI
site 02845   ; OUTI
site 0285D   ; OUT (C),E
site 0285F   ; OUT (C),D
site 02881   ; OUT (C),L
site 02883   ; OUT (C),H
site 02891   ; OUTI
site 02893   ; OUTI
site 028B6   ; OUT (C),L
site 028B8   ; OUT (C),H
site 028C6   ; OUTI
site 028C8   ; OUTI
site 03AC1   ; OUT ($BE),A
site 03B09   ; OUT ($BE),A
site 03B0F   ; OUT ($BE),A
site 03E91   ; OUT ($BE),A
site 03E97   ; OUT ($BE),A
site 0719C   ; IN A,($7E)
site 07C18   ; IN A,($7E)
site 07E17   ; OUT ($BE),A
site 07E1C   ; OUT ($BE),A
site 08101   ; OUT ($F0),A
site 0810A   ; OUT ($F1),A
site 08123   ; OUT ($7F),A
site 08133   ; OUT (C),D
site 08139   ; OUT ($F1),A
site 0816C   ; OTIR
site 0817A   ; OTIR
site 08184   ; OUT ($F0),A
site 0818A   ; OUT ($F1),A
site 081A2   ; OUTI
site 081A8   ; OUTI
site 08299   ; OUT ($7F),A
site 0829D   ; OUT ($7F),A
site 082C5   ; OUT ($7F),A
site 082C9   ; OUT ($7F),A
site 082CD   ; OUT ($7F),A
site 082D0   ; OUT ($7F),A
site 08339   ; OUT ($F0),A
site 08340   ; OUT ($F1),A
site 08348   ; OUT ($F0),A
site 0834E   ; OUT ($F1),A
site 08441   ; OUT ($F0),A
site 0844B   ; OUT (C),L
site 08454   ; OUT ($F0),A
site 0846F   ; OUT (C),H
site 08477   ; OUT ($F0),A
site 08485   ; OUT ($F1),A
site 08491   ; OUT ($F0),A
site 0849A   ; OUT ($F1),A
site 0864B   ; OUT ($F0),A
site 08654   ; OUT (C),A
site 08659   ; OUT ($F0),A
site 0865F   ; OUTI
site 086AD   ; OUT ($7F),A
site 0874F   ; OUT ($7F),A
site 08776   ; OUT ($7F),A
site 0877B   ; OUT ($7F),A
site 087A7   ; OUT ($F0),A
site 087B5   ; OUT ($F1),A
site 08849   ; OUTI
site 0884B   ; OUTI
site 0884D   ; OUTI
site 0884F   ; OUTI
site 08851   ; OUTI
site 08853   ; OUTI
site 08855   ; OUTI
site 08857   ; OUTI
site 08859   ; OUTI
site 0885B   ; OUTI
site 0885D   ; OUTI
site 08867   ; OUT (C),D
site 0886D   ; OUT ($F1),A
site 088AF   ; OUT ($7F),A
site 08905   ; OUT ($7F),A
site 08944   ; OUT ($7F),A
site 08997   ; OUT ($7F),A
site 089B7   ; OUT ($7F),A
site 08A03   ; OUT ($7F),A
site 08A0D   ; OUT ($7F),A
site 08A55   ; OUT ($7F),A
site 1C180   ; OUTI
site 1C182   ; OUT ($BE),A
site 1C184   ; OUT ($BE),A
site 1C186   ; OUT ($BE),A
site 1C188   ; OUTI
site 1C18A   ; OUT ($BE),A
site 1C18C   ; OUT ($BE),A
site 1C18E   ; OUT ($BE),A
site 1C190   ; OUTI
site 1C192   ; OUT ($BE),A
site 1C194   ; OUT ($BE),A
site 1C196   ; OUT ($BE),A
site 1C198   ; OUTI
site 1C19A   ; OUT ($BE),A
site 1C19C   ; OUT ($BE),A
site 1C19E   ; OUT ($BE),A
site 1C1A0   ; OUTI
site 1C1A2   ; OUT ($BE),A
site 1C1A4   ; OUT ($BE),A
site 1C1A6   ; OUT ($BE),A
site 1C1A8   ; OUTI
site 1C1AA   ; OUT ($BE),A
site 1C1AC   ; OUT ($BE),A
site 1C1AE   ; OUT ($BE),A
site 1C1B0   ; OUTI
site 1C1B2   ; OUT ($BE),A
site 1C1B4   ; OUT ($BE),A
site 1C1B6   ; OUT ($BE),A
site 1C1B8   ; OUTI
site 1C1BA   ; OUT ($BE),A
site 1C1BC   ; OUT ($BE),A
site 1C1BE   ; OUT ($BE),A
site 1C1C0   ; OUTI
site 1C1C2   ; OUT ($BE),A
site 1C1C4   ; OUT ($BE),A
site 1C1C6   ; OUT ($BE),A
site 1C1C8   ; OUTI
site 1C1CA   ; OUT ($BE),A
site 1C1CC   ; OUT ($BE),A
site 1C1CE   ; OUT ($BE),A
site 1C1D0   ; OUTI
site 1C1D2   ; OUT ($BE),A
site 1C1D4   ; OUT ($BE),A
site 1C1D6   ; OUT ($BE),A
site 1C1D8   ; OUTI
site 1C1DA   ; OUT ($BE),A
site 1C1DC   ; OUT ($BE),A
site 1C1DE   ; OUT ($BE),A
site 1C1E0   ; OUTI
site 1C1E2   ; OUT ($BE),A
site 1C1E4   ; OUT ($BE),A
site 1C1E6   ; OUT ($BE),A
site 1C1E8   ; OUTI
site 1C1EA   ; OUT ($BE),A
site 1C1EC   ; OUT ($BE),A
site 1C1EE   ; OUT ($BE),A
site 1C1F0   ; OUTI
site 1C1F2   ; OUT ($BE),A
site 1C1F4   ; OUT ($BE),A
site 1C1F6   ; OUT ($BE),A
site 1C1F8   ; OUTI
site 1C1FA   ; OUT ($BE),A
site 1C1FC   ; OUT ($BE),A
site 1C1FE   ; OUT ($BE),A
site 1C200   ; OUTI
site 1C202   ; OUT ($BE),A
site 1C204   ; OUT ($BE),A
site 1C206   ; OUT ($BE),A
site 1C208   ; OUTI
site 1C20A   ; OUT ($BE),A
site 1C20C   ; OUT ($BE),A
site 1C20E   ; OUT ($BE),A
site 1C210   ; OUTI
site 1C212   ; OUT ($BE),A
site 1C214   ; OUT ($BE),A
site 1C216   ; OUT ($BE),A
site 1C218   ; OUTI
site 1C21A   ; OUT ($BE),A
site 1C21C   ; OUT ($BE),A
site 1C21E   ; OUT ($BE),A
site 1C220   ; OUTI
site 1C222   ; OUT ($BE),A
site 1C224   ; OUT ($BE),A
site 1C226   ; OUT ($BE),A
site 1C228   ; OUTI
site 1C22A   ; OUT ($BE),A
site 1C22C   ; OUT ($BE),A
site 1C22E   ; OUT ($BE),A
site 1C230   ; OUTI
site 1C232   ; OUT ($BE),A
site 1C234   ; OUT ($BE),A
site 1C236   ; OUT ($BE),A
site 1C238   ; OUTI
site 1C23A   ; OUT ($BE),A
site 1C23C   ; OUT ($BE),A
site 1C23E   ; OUT ($BE),A
site 1C240   ; OUTI
site 1C242   ; OUT ($BE),A
site 1C244   ; OUT ($BE),A
site 1C246   ; OUT ($BE),A
site 1C248   ; OUTI
site 1C24A   ; OUT ($BE),A
site 1C24C   ; OUT ($BE),A
site 1C24E   ; OUT ($BE),A
site 1C250   ; OUTI
site 1C252   ; OUT ($BE),A
site 1C254   ; OUT ($BE),A
site 1C256   ; OUT ($BE),A
site 1C258   ; OUTI
site 1C25A   ; OUT ($BE),A
site 1C25C   ; OUT ($BE),A
site 1C25E   ; OUT ($BE),A
site 1C260   ; OUTI
site 1C262   ; OUT ($BE),A
site 1C264   ; OUT ($BE),A
site 1C266   ; OUT ($BE),A
site 1C268   ; OUTI
site 1C26A   ; OUT ($BE),A
site 1C26C   ; OUT ($BE),A
site 1C26E   ; OUT ($BE),A
site 1C270   ; OUTI
site 1C272   ; OUT ($BE),A
site 1C274   ; OUT ($BE),A
site 1C276   ; OUT ($BE),A
site 1C278   ; OUTI
site 1C27A   ; OUT ($BE),A
site 1C27C   ; OUT ($BE),A
site 1C27E   ; OUT ($BE),A
site 1C280   ; OUTI
site 1C282   ; OUT ($BE),A
site 1C284   ; OUT ($BE),A
site 1C286   ; OUT ($BE),A
site 1C288   ; OUTI
site 1C28A   ; OUT ($BE),A
site 1C28C   ; OUT ($BE),A
site 1C28E   ; OUT ($BE),A
site 1C290   ; OUTI
site 1C292   ; OUT ($BE),A
site 1C294   ; OUT ($BE),A
site 1C296   ; OUT ($BE),A
site 1C298   ; OUTI
site 1C29A   ; OUT ($BE),A
site 1C29C   ; OUT ($BE),A
site 1C29E   ; OUT ($BE),A
site 1C2A0   ; OUTI
site 1C2A2   ; OUT ($BE),A
site 1C2A4   ; OUT ($BE),A
site 1C2A6   ; OUT ($BE),A
site 1C2A8   ; OUTI
site 1C2AA   ; OUT ($BE),A
site 1C2AC   ; OUT ($BE),A
site 1C2AE   ; OUT ($BE),A
site 1C2B0   ; OUTI
site 1C2B2   ; OUT ($BE),A
site 1C2B4   ; OUT ($BE),A
site 1C2B6   ; OUT ($BE),A
site 1C2B8   ; OUTI
site 1C2BA   ; OUT ($BE),A
site 1C2BC   ; OUT ($BE),A
site 1C2BE   ; OUT ($BE),A
site 1C2C0   ; OUTI
site 1C2C2   ; OUT ($BE),A
site 1C2C4   ; OUT ($BE),A
site 1C2C6   ; OUT ($BE),A
site 1C2C8   ; OUTI
site 1C2CA   ; OUT ($BE),A
site 1C2CC   ; OUT ($BE),A
site 1C2CE   ; OUT ($BE),A
site 1C2D0   ; OUTI
site 1C2D2   ; OUT ($BE),A
site 1C2D4   ; OUT ($BE),A
site 1C2D6   ; OUT ($BE),A
site 1C2D8   ; OUTI
site 1C2DA   ; OUT ($BE),A
site 1C2DC   ; OUT ($BE),A
site 1C2DE   ; OUT ($BE),A
site 1C2E0   ; OUTI
site 1C2E2   ; OUT ($BE),A
site 1C2E4   ; OUT ($BE),A
site 1C2E6   ; OUT ($BE),A
site 1C2E8   ; OUTI
site 1C2EA   ; OUT ($BE),A
site 1C2EC   ; OUT ($BE),A
site 1C2EE   ; OUT ($BE),A
site 1C2F0   ; OUTI
site 1C2F2   ; OUT ($BE),A
site 1C2F4   ; OUT ($BE),A
site 1C2F6   ; OUT ($BE),A
site 1C2F8   ; OUTI
site 1C2FA   ; OUT ($BE),A
site 1C2FC   ; OUT ($BE),A
site 1C2FE   ; OUT ($BE),A
site 1C300   ; OUTI
site 1C302   ; OUT ($BE),A
site 1C304   ; OUT ($BE),A
site 1C306   ; OUT ($BE),A
site 1C308   ; OUTI
site 1C30A   ; OUT ($BE),A
site 1C30C   ; OUT ($BE),A
site 1C30E   ; OUT ($BE),A
site 1C310   ; OUTI
site 1C312   ; OUT ($BE),A
site 1C314   ; OUT ($BE),A
site 1C316   ; OUT ($BE),A
site 1C318   ; OUTI
site 1C31A   ; OUT ($BE),A
site 1C31C   ; OUT ($BE),A
site 1C31E   ; OUT ($BE),A
site 1C320   ; OUTI
site 1C322   ; OUT ($BE),A
site 1C324   ; OUT ($BE),A
site 1C326   ; OUT ($BE),A
site 1C328   ; OUTI
site 1C32A   ; OUT ($BE),A
site 1C32C   ; OUT ($BE),A
site 1C32E   ; OUT ($BE),A
site 1C330   ; OUTI
site 1C332   ; OUT ($BE),A
site 1C334   ; OUT ($BE),A
site 1C336   ; OUT ($BE),A
site 1C338   ; OUTI
site 1C33A   ; OUT ($BE),A
site 1C33C   ; OUT ($BE),A
site 1C33E   ; OUT ($BE),A
site 1C340   ; OUTI
site 1C342   ; OUT ($BE),A
site 1C344   ; OUT ($BE),A
site 1C346   ; OUT ($BE),A
site 1C348   ; OUTI
site 1C34A   ; OUT ($BE),A
site 1C34C   ; OUT ($BE),A
site 1C34E   ; OUT ($BE),A
site 1C350   ; OUTI
site 1C352   ; OUT ($BE),A
site 1C354   ; OUT ($BE),A
site 1C356   ; OUT ($BE),A
site 1C358   ; OUTI
site 1C35A   ; OUT ($BE),A
site 1C35C   ; OUT ($BE),A
site 1C35E   ; OUT ($BE),A
site 1C360   ; OUTI
site 1C362   ; OUT ($BE),A
site 1C364   ; OUT ($BE),A
site 1C366   ; OUT ($BE),A
site 1C368   ; OUTI
site 1C36A   ; OUT ($BE),A
site 1C36C   ; OUT ($BE),A
site 1C36E   ; OUT ($BE),A
site 1C370   ; OUTI
site 1C372   ; OUT ($BE),A
site 1C374   ; OUT ($BE),A
site 1C376   ; OUT ($BE),A
site 1C378   ; OUTI
site 1C37A   ; OUT ($BE),A
site 1C37C   ; OUT ($BE),A
site 1C37E   ; OUT ($BE),A
site 1C380   ; OUTI
site 1C382   ; OUT ($BE),A
site 1C384   ; OUT ($BE),A
site 1C386   ; OUT ($BE),A
site 1C388   ; OUTI
site 1C38A   ; OUT ($BE),A
site 1C38C   ; OUT ($BE),A
site 1C38E   ; OUT ($BE),A
site 1C390   ; OUTI
site 1C392   ; OUT ($BE),A
site 1C394   ; OUT ($BE),A
site 1C396   ; OUT ($BE),A
site 1C398   ; OUTI
site 1C39A   ; OUT ($BE),A
site 1C39C   ; OUT ($BE),A
site 1C39E   ; OUT ($BE),A
site 1C3A0   ; OUTI
site 1C3A2   ; OUT ($BE),A
site 1C3A4   ; OUT ($BE),A
site 1C3A6   ; OUT ($BE),A
site 1C3A8   ; OUTI
site 1C3AA   ; OUT ($BE),A
site 1C3AC   ; OUT ($BE),A
site 1C3AE   ; OUT ($BE),A
site 1C3B0   ; OUTI
site 1C3B2   ; OUT ($BE),A
site 1C3B4   ; OUT ($BE),A
site 1C3B6   ; OUT ($BE),A
site 1C3B8   ; OUTI
site 1C3BA   ; OUT ($BE),A
site 1C3BC   ; OUT ($BE),A
site 1C3BE   ; OUT ($BE),A
site 1C3C0   ; OUTI
site 1C3C2   ; OUT ($BE),A
site 1C3C4   ; OUT ($BE),A
site 1C3C6   ; OUT ($BE),A
site 1C3C8   ; OUTI
site 1C3CA   ; OUT ($BE),A
site 1C3CC   ; OUT ($BE),A
site 1C3CE   ; OUT ($BE),A
site 1C3D0   ; OUTI
site 1C3D2   ; OUT ($BE),A
site 1C3D4   ; OUT ($BE),A
site 1C3D6   ; OUT ($BE),A
site 1C3D8   ; OUTI
site 1C3DA   ; OUT ($BE),A
site 1C3DC   ; OUT ($BE),A
site 1C3DE   ; OUT ($BE),A
site 1C3E0   ; OUTI
site 1C3E2   ; OUT ($BE),A
site 1C3E4   ; OUT ($BE),A
site 1C3E6   ; OUT ($BE),A
site 1C3E8   ; OUTI
site 1C3EA   ; OUT ($BE),A
site 1C3EC   ; OUT ($BE),A
site 1C3EE   ; OUT ($BE),A
site 1C3F0   ; OUTI
site 1C3F2   ; OUT ($BE),A
site 1C3F4   ; OUT ($BE),A
site 1C3F6   ; OUT ($BE),A
site 1C3F8   ; OUTI
site 1C3FA   ; OUT ($BE),A
site 1C3FC   ; OUT ($BE),A
site 1C3FE   ; OUT ($BE),A
site 1C400   ; OUTI
site 1C402   ; OUT ($BE),A
site 1C404   ; OUT ($BE),A
site 1C406   ; OUT ($BE),A
site 1C408   ; OUTI
site 1C40A   ; OUT ($BE),A
site 1C40C   ; OUT ($BE),A
site 1C40E   ; OUT ($BE),A
site 1C410   ; OUTI
site 1C412   ; OUT ($BE),A
site 1C414   ; OUT ($BE),A
site 1C416   ; OUT ($BE),A
site 1C418   ; OUTI
site 1C41A   ; OUT ($BE),A
site 1C41C   ; OUT ($BE),A
site 1C41E   ; OUT ($BE),A
site 1C420   ; OUTI
site 1C422   ; OUT ($BE),A
site 1C424   ; OUT ($BE),A
site 1C426   ; OUT ($BE),A
site 1C428   ; OUTI
site 1C42A   ; OUT ($BE),A
site 1C42C   ; OUT ($BE),A
site 1C42E   ; OUT ($BE),A
site 1C430   ; OUTI
site 1C432   ; OUT ($BE),A
site 1C434   ; OUT ($BE),A
site 1C436   ; OUT ($BE),A
site 1C438   ; OUTI
site 1C43A   ; OUT ($BE),A
site 1C43C   ; OUT ($BE),A
site 1C43E   ; OUT ($BE),A
site 1C440   ; OUTI
site 1C442   ; OUT ($BE),A
site 1C444   ; OUT ($BE),A
site 1C446   ; OUT ($BE),A
site 1C448   ; OUTI
site 1C44A   ; OUT ($BE),A
site 1C44C   ; OUT ($BE),A
site 1C44E   ; OUT ($BE),A
site 1C450   ; OUTI
site 1C452   ; OUT ($BE),A
site 1C454   ; OUT ($BE),A
site 1C456   ; OUT ($BE),A
site 1C458   ; OUTI
site 1C45A   ; OUT ($BE),A
site 1C45C   ; OUT ($BE),A
site 1C45E   ; OUT ($BE),A
site 1C460   ; OUTI
site 1C462   ; OUT ($BE),A
site 1C464   ; OUT ($BE),A
site 1C466   ; OUT ($BE),A
site 1C468   ; OUTI
site 1C46A   ; OUT ($BE),A
site 1C46C   ; OUT ($BE),A
site 1C46E   ; OUT ($BE),A
site 1C470   ; OUTI
site 1C472   ; OUT ($BE),A
site 1C474   ; OUT ($BE),A
site 1C476   ; OUT ($BE),A
site 1C478   ; OUTI
site 1C47A   ; OUT ($BE),A
site 1C47C   ; OUT ($BE),A
site 1C47E   ; OUT ($BE),A
site 1C480   ; OUTI
site 1C482   ; OUT ($BE),A
site 1C484   ; OUT ($BE),A
site 1C486   ; OUT ($BE),A
site 1C488   ; OUTI
site 1C48A   ; OUT ($BE),A
site 1C48C   ; OUT ($BE),A
site 1C48E   ; OUT ($BE),A
site 1C490   ; OUTI
site 1C492   ; OUT ($BE),A
site 1C494   ; OUT ($BE),A
site 1C496   ; OUT ($BE),A
site 1C498   ; OUTI
site 1C49A   ; OUT ($BE),A
site 1C49C   ; OUT ($BE),A
site 1C49E   ; OUT ($BE),A
site 1C4A0   ; OUTI
site 1C4A2   ; OUT ($BE),A
site 1C4A4   ; OUT ($BE),A
site 1C4A6   ; OUT ($BE),A
site 1C4A8   ; OUTI
site 1C4AA   ; OUT ($BE),A
site 1C4AC   ; OUT ($BE),A
site 1C4AE   ; OUT ($BE),A
site 1C4B0   ; OUTI
site 1C4B2   ; OUT ($BE),A
site 1C4B4   ; OUT ($BE),A
site 1C4B6   ; OUT ($BE),A
site 1C4B8   ; OUTI
site 1C4BA   ; OUT ($BE),A
site 1C4BC   ; OUT ($BE),A
site 1C4BE   ; OUT ($BE),A
site 1C4C0   ; OUTI
site 1C4C2   ; OUT ($BE),A
site 1C4C4   ; OUT ($BE),A
site 1C4C6   ; OUT ($BE),A
site 1C4C8   ; OUTI
site 1C4CA   ; OUT ($BE),A
site 1C4CC   ; OUT ($BE),A
site 1C4CE   ; OUT ($BE),A
site 1C4D0   ; OUTI
site 1C4D2   ; OUT ($BE),A
site 1C4D4   ; OUT ($BE),A
site 1C4D6   ; OUT ($BE),A
site 1C4D8   ; OUTI
site 1C4DA   ; OUT ($BE),A
site 1C4DC   ; OUT ($BE),A
site 1C4DE   ; OUT ($BE),A
site 1C4E0   ; OUTI
site 1C4E2   ; OUT ($BE),A
site 1C4E4   ; OUT ($BE),A
site 1C4E6   ; OUT ($BE),A
site 1C4E8   ; OUTI
site 1C4EA   ; OUT ($BE),A
site 1C4EC   ; OUT ($BE),A
site 1C4EE   ; OUT ($BE),A
site 1C4F0   ; OUTI
site 1C4F2   ; OUT ($BE),A
site 1C4F4   ; OUT ($BE),A
site 1C4F6   ; OUT ($BE),A
site 1C4F8   ; OUTI
site 1C4FA   ; OUT ($BE),A
site 1C4FC   ; OUT ($BE),A
site 1C4FE   ; OUT ($BE),A
site 1C500   ; OUTI
site 1C502   ; OUT ($BE),A
site 1C504   ; OUT ($BE),A
site 1C506   ; OUT ($BE),A
site 1C508   ; OUTI
site 1C50A   ; OUT ($BE),A
site 1C50C   ; OUT ($BE),A
site 1C50E   ; OUT ($BE),A
site 1C510   ; OUTI
site 1C512   ; OUT ($BE),A
site 1C514   ; OUT ($BE),A
site 1C516   ; OUT ($BE),A
site 1C518   ; OUTI
site 1C51A   ; OUT ($BE),A
site 1C51C   ; OUT ($BE),A
site 1C51E   ; OUT ($BE),A
site 1C520   ; OUTI
site 1C522   ; OUT ($BE),A
site 1C524   ; OUT ($BE),A
site 1C526   ; OUT ($BE),A
site 1C528   ; OUTI
site 1C52A   ; OUT ($BE),A
site 1C52C   ; OUT ($BE),A
site 1C52E   ; OUT ($BE),A
site 1C530   ; OUTI
site 1C532   ; OUT ($BE),A
site 1C534   ; OUT ($BE),A
site 1C536   ; OUT ($BE),A
site 1C538   ; OUTI
site 1C53A   ; OUT ($BE),A
site 1C53C   ; OUT ($BE),A
site 1C53E   ; OUT ($BE),A
site 1C540   ; OUTI
site 1C542   ; OUT ($BE),A
site 1C544   ; OUT ($BE),A
site 1C546   ; OUT ($BE),A
site 1C548   ; OUTI
site 1C54A   ; OUT ($BE),A
site 1C54C   ; OUT ($BE),A
site 1C54E   ; OUT ($BE),A
site 1C550   ; OUTI
site 1C552   ; OUT ($BE),A
site 1C554   ; OUT ($BE),A
site 1C556   ; OUT ($BE),A
site 1C558   ; OUTI
site 1C55A   ; OUT ($BE),A
site 1C55C   ; OUT ($BE),A
site 1C55E   ; OUT ($BE),A
site 1C560   ; OUTI
site 1C562   ; OUT ($BE),A
site 1C564   ; OUT ($BE),A
site 1C566   ; OUT ($BE),A
site 1C568   ; OUTI
site 1C56A   ; OUT ($BE),A
site 1C56C   ; OUT ($BE),A
site 1C56E   ; OUT ($BE),A
site 1C570   ; OUTI
site 1C572   ; OUT ($BE),A
site 1C574   ; OUT ($BE),A
site 1C576   ; OUT ($BE),A
site 1C578   ; OUTI
site 1C57A   ; OUT ($BE),A
site 1C57C   ; OUT ($BE),A
site 1C57E   ; OUT ($BE),A
site 1C580   ; OUTI
site 1C582   ; OUT ($BE),A
site 1C584   ; OUT ($BE),A
site 1C586   ; OUT ($BE),A
site 1C588   ; OUTI
site 1C58A   ; OUT ($BE),A
site 1C58C   ; OUT ($BE),A
site 1C58E   ; OUT ($BE),A
site 1C590   ; OUTI
site 1C592   ; OUT ($BE),A
site 1C594   ; OUT ($BE),A
site 1C596   ; OUT ($BE),A
site 1C598   ; OUTI
site 1C59A   ; OUT ($BE),A
site 1C59C   ; OUT ($BE),A
site 1C59E   ; OUT ($BE),A
site 1C5A0   ; OUTI
site 1C5A2   ; OUT ($BE),A
site 1C5A4   ; OUT ($BE),A
site 1C5A6   ; OUT ($BE),A
site 1C5A8   ; OUTI
site 1C5AA   ; OUT ($BE),A
site 1C5AC   ; OUT ($BE),A
site 1C5AE   ; OUT ($BE),A
site 1C5B0   ; OUTI
site 1C5B2   ; OUT ($BE),A
site 1C5B4   ; OUT ($BE),A
site 1C5B6   ; OUT ($BE),A
site 1C5B8   ; OUTI
site 1C5BA   ; OUT ($BE),A
site 1C5BC   ; OUT ($BE),A
site 1C5BE   ; OUT ($BE),A
site 1C5C0   ; OUTI
site 1C5C2   ; OUT ($BE),A
site 1C5C4   ; OUT ($BE),A
site 1C5C6   ; OUT ($BE),A
site 1C5C8   ; OUTI
site 1C5CA   ; OUT ($BE),A
site 1C5CC   ; OUT ($BE),A
site 1C5CE   ; OUT ($BE),A
site 1C5D0   ; OUTI
site 1C5D2   ; OUT ($BE),A
site 1C5D4   ; OUT ($BE),A
site 1C5D6   ; OUT ($BE),A
site 1C5D8   ; OUTI
site 1C5DA   ; OUT ($BE),A
site 1C5DC   ; OUT ($BE),A
site 1C5DE   ; OUT ($BE),A
site 1C5E0   ; OUTI
site 1C5E2   ; OUT ($BE),A
site 1C5E4   ; OUT ($BE),A
site 1C5E6   ; OUT ($BE),A
site 1C5E8   ; OUTI
site 1C5EA   ; OUT ($BE),A
site 1C5EC   ; OUT ($BE),A
site 1C5EE   ; OUT ($BE),A
site 1C5F0   ; OUTI
site 1C5F2   ; OUT ($BE),A
site 1C5F4   ; OUT ($BE),A
site 1C5F6   ; OUT ($BE),A
site 1C5F8   ; OUTI
site 1C5FA   ; OUT ($BE),A
site 1C5FC   ; OUT ($BE),A
site 1C5FE   ; OUT ($BE),A
site 1C600   ; OUTI
site 1C602   ; OUT ($BE),A
site 1C604   ; OUT ($BE),A
site 1C606   ; OUT ($BE),A
site 1C608   ; OUTI
site 1C60A   ; OUT ($BE),A
site 1C60C   ; OUT ($BE),A
site 1C60E   ; OUT ($BE),A
site 1C610   ; OUTI
site 1C612   ; OUT ($BE),A
site 1C614   ; OUT ($BE),A
site 1C616   ; OUT ($BE),A
site 1C618   ; OUTI
site 1C61A   ; OUT ($BE),A
site 1C61C   ; OUT ($BE),A
site 1C61E   ; OUT ($BE),A
site 1C620   ; OUTI
site 1C622   ; OUT ($BE),A
site 1C624   ; OUT ($BE),A
site 1C626   ; OUT ($BE),A
site 1C628   ; OUTI
site 1C62A   ; OUT ($BE),A
site 1C62C   ; OUT ($BE),A
site 1C62E   ; OUT ($BE),A
site 1C630   ; OUTI
site 1C632   ; OUT ($BE),A
site 1C634   ; OUT ($BE),A
site 1C636   ; OUT ($BE),A
site 1C638   ; OUTI
site 1C63A   ; OUT ($BE),A
site 1C63C   ; OUT ($BE),A
site 1C63E   ; OUT ($BE),A
site 1C640   ; OUTI
site 1C642   ; OUT ($BE),A
site 1C644   ; OUT ($BE),A
site 1C646   ; OUT ($BE),A
site 1C648   ; OUTI
site 1C64A   ; OUT ($BE),A
site 1C64C   ; OUT ($BE),A
site 1C64E   ; OUT ($BE),A
site 1C650   ; OUTI
site 1C652   ; OUT ($BE),A
site 1C654   ; OUT ($BE),A
site 1C656   ; OUT ($BE),A
site 1C658   ; OUTI
site 1C65A   ; OUT ($BE),A
site 1C65C   ; OUT ($BE),A
site 1C65E   ; OUT ($BE),A
site 1C660   ; OUTI
site 1C662   ; OUT ($BE),A
site 1C664   ; OUT ($BE),A
site 1C666   ; OUT ($BE),A
site 1C668   ; OUTI
site 1C66A   ; OUT ($BE),A
site 1C66C   ; OUT ($BE),A
site 1C66E   ; OUT ($BE),A
site 1C670   ; OUTI
site 1C672   ; OUT ($BE),A
site 1C674   ; OUT ($BE),A
site 1C676   ; OUT ($BE),A
site 1C678   ; OUTI
site 1C67A   ; OUT ($BE),A
site 1C67C   ; OUT ($BE),A
site 1C67E   ; OUT ($BE),A
site 1C680   ; OUTI
site 1C682   ; OUT ($BE),A
site 1C684   ; OUT ($BE),A
site 1C686   ; OUT ($BE),A
site 1C688   ; OUTI
site 1C68A   ; OUT ($BE),A
site 1C68C   ; OUT ($BE),A
site 1C68E   ; OUT ($BE),A
site 1C690   ; OUTI
site 1C692   ; OUT ($BE),A
site 1C694   ; OUT ($BE),A
site 1C696   ; OUT ($BE),A
site 1C698   ; OUTI
site 1C69A   ; OUT ($BE),A
site 1C69C   ; OUT ($BE),A
site 1C69E   ; OUT ($BE),A
site 1C6A0   ; OUTI
site 1C6A2   ; OUT ($BE),A
site 1C6A4   ; OUT ($BE),A
site 1C6A6   ; OUT ($BE),A
site 1C6A8   ; OUTI
site 1C6AA   ; OUT ($BE),A
site 1C6AC   ; OUT ($BE),A
site 1C6AE   ; OUT ($BE),A
site 1C6B0   ; OUTI
site 1C6B2   ; OUT ($BE),A
site 1C6B4   ; OUT ($BE),A
site 1C6B6   ; OUT ($BE),A
site 1C6B8   ; OUTI
site 1C6BA   ; OUT ($BE),A
site 1C6BC   ; OUT ($BE),A
site 1C6BE   ; OUT ($BE),A
site 1C82F   ; OUT (C),E
site 1C833   ; OUT ($BF),A
site 1C837   ; OUT ($BE),A
site 1C83B   ; OUT ($BE),A
site 1C841   ; OUT (C),E
site 1C845   ; OUT ($BF),A
site 1C84A   ; OUT ($BE),A
site 1C850   ; OUT ($BE),A
site 1C864   ; OUT ($BF),A
site 1C868   ; OUT ($BF),A
site 27F30   ; OUTI
site 27F36   ; OUT (C),A
site 2BF38   ; OUT ($BE),A
site 2BF3E   ; OUT ($BE),A
site 31F5E   ; OUT ($BE),A
site 31F64   ; OUT ($BE),A
mapst 0004F   ; LD ($FFFF),A
mapldk 0008C   # LD HL,$FFFC; LD (HL),$80
maphl 00092   # LD (HL),$00, HL = $FFFD
maphl 00095   # LD (HL),$01, HL = $FFFE
maphl 00098   # LD (HL),$02, HL = $FFFF
mapst 000B8   ; LD ($FFFF),A
mapst 00132   ; LD ($FFFF),A
mapst 0015E   ; LD ($FFFC),A
mapst 00163   ; LD ($FFFF),A
mapst 00195   ; LD ($FFFC),A
mapst 00199   ; LD ($FFFF),A
mapst 001C8   ; LD ($FFFF),A
mapst 001DC   ; LD ($FFFF),A
mapst 00298   ; LD ($FFFC),A
mapst 002AD   ; LD ($FFFC),A
mapst 002C4   ; LD ($FFFF),A
mapst 00601   ; LD ($FFFF),A
mapst 00605   ; LD ($FFFC),A
mapst 0061C   ; LD ($FFFC),A
mapst 00620   ; LD ($FFFF),A
mapst 0079F   ; LD ($FFFC),A
mapst 007D1   ; LD ($FFFC),A
mapst 00B02   ; LD ($FFFF),A
mapst 00B6D   ; LD ($FFFF),A
mapst 00B7A   ; LD ($FFFF),A
mapst 00BA3   ; LD ($FFFF),A
mapst 00BDD   ; LD ($FFFF),A
mapld 00C40   # LD HL,$FFFF; LD (HL),$0C
mapst 00C4F   ; LD ($FFFF),A
mapst 00C5B   ; LD ($FFFF),A
mapst 00DD7   ; LD ($FFFF),A
mapst 00E5C   ; LD ($FFFF),A
mapst 00F9F   ; LD ($FFFF),A
mapst 00FB3   ; LD ($FFFF),A
mapst 01B3E   ; LD ($FFFF),A
mapst 01D87   ; LD ($FFFF),A
mapst 01DB4   ; LD ($FFFF),A
mapst 01DD3   ; LD ($FFFF),A
mapst 01DF0   ; LD ($FFFF),A
mapst 01E4D   ; LD ($FFFF),A
mapst 01E67   ; LD ($FFFF),A
mapst 01E93   ; LD ($FFFF),A
mapst 01EEB   ; LD ($FFFF),A
mapst 01F86   ; LD ($FFFF),A
mapst 01F8E   ; LD ($FFFF),A
mapst 01FEB   ; LD ($FFFF),A
mapst 01FFF   ; LD ($FFFC),A
mapst 02012   ; LD ($FFFC),A
mapst 02018   ; LD ($FFFF),A
mapst 0204F   ; LD ($FFFF),A
mapst 020E3   ; LD ($FFFC),A
mapst 020EF   ; LD ($FFFC),A
mapst 026DF   ; LD ($FFFF),A
mapst 026F5   ; LD ($FFFF),A
mapst 02761   ; LD ($FFFF),A
mapst 02ACB   ; LD ($FFFC),A
mapst 02B12   ; LD ($FFFC),A
mapst 02B18   ; LD ($FFFC),A
mapst 02B5E   ; LD ($FFFC),A
mapst 02B7F   ; LD ($FFFC),A
mapst 02BCB   ; LD ($FFFC),A
mapst 02BF3   ; LD ($FFFF),A
mapst 037FE   ; LD ($FFFF),A
mapst 03818   ; LD ($FFFF),A
mapst 03829   ; LD ($FFFF),A
mapst 0389B   ; LD ($FFFF),A
mapst 038C6   ; LD ($FFFF),A
mapst 038E4   ; LD ($FFFF),A
mapst 0398E   ; LD ($FFFF),A
mapst 03BAE   ; LD ($FFFF),A
mapst 03CCD   ; LD ($FFFF),A
mapst 03CDB   ; LD ($FFFF),A
mapst 03D49   ; LD ($FFFF),A
mapst 03DA5   ; LD ($FFFF),A
mapst 03DC3   ; LD ($FFFF),A
mapst 03DE2   ; LD ($FFFF),A
mapst 03DFD   ; LD ($FFFF),A
mapst 03E2F   ; LD ($FFFF),A
mapst 03E4F   ; LD ($FFFF),A
mapst 03E88   ; LD ($FFFF),A
mapst 03EFF   ; LD ($FFFF),A
mapst 03F33   ; LD ($FFFF),A
mapst 03F44   ; LD ($FFFF),A
mapst 04286   ; LD ($FFFC),A
mapst 0433B   ; LD ($FFFF),A
mapst 04348   ; LD ($FFFF),A
mapst 0446C   ; LD ($FFFF),A
mapst 0447D   ; LD ($FFFF),A
mapst 04574   ; LD ($FFFF),A
mapst 046B0   ; LD ($FFFF),A
mapst 04773   ; LD ($FFFF),A
mapst 04965   ; LD ($FFFF),A
mapst 04AB2   ; LD ($FFFC),A
mapst 04AB8   ; LD ($FFFC),A
mapst 04CFD   ; LD ($FFFF),A
mapst 04D8F   ; LD ($FFFF),A
mapst 04DBD   ; LD ($FFFC),A
mapst 04DDD   ; LD ($FFFC),A
mapst 060C2   ; LD ($FFFF),A
mapst 0642E   ; LD ($FFFF),A
mapst 064D8   ; LD ($FFFF),A
mapst 065A7   ; LD ($FFFF),A
mapst 06671   ; LD ($FFFF),A
mapst 066D9   ; LD ($FFFF),A
mapst 06780   ; LD ($FFFF),A
mapst 0684E   ; LD ($FFFF),A
mapst 06904   ; LD ($FFFF),A
mapst 06A28   ; LD ($FFFF),A
mapst 06B2A   ; LD ($FFFF),A
mapst 06B3E   ; LD ($FFFF),A
mapst 06B7F   ; LD ($FFFF),A
mapst 06B93   ; LD ($FFFF),A
mapst 06BA9   ; LD ($FFFF),A
mapst 06BBF   ; LD ($FFFF),A
mapst 07C35   ; LD ($FFFF),A
mapst 07C43   ; LD ($FFFF),A
mapst 07C5E   ; LD ($FFFF),A
mapst 07C84   ; LD ($FFFF),A
mapst 07CA9   ; LD ($FFFF),A
mapst 07CDE   ; LD ($FFFF),A
mapst 07CEE   ; LD ($FFFF),A
mapst 07D2D   ; LD ($FFFF),A
# CHECK cartarea_store at 007BD ($07BD bank 0): 36 00  LD (HL),$00 $8010
# CHECK cartarea_store at 0084B ($084B bank 0): 32 D5 45  LD ($45D5),A $45D5
# CHECK cartarea_store at 00BFE ($0BFE bank 0): 12  LD (DE),A $8400
# CHECK cartarea_store at 00C0D ($0C0D bank 0): 12  LD (DE),A $8401
# CHECK cartarea_store at 020E8 ($20E8 bank 0): CB B6  RES 6,(HL) $85B1,$85B3,$85B5,$85B7...
# CHECK cartarea_store at 04138 ($4138 bank 1): 36 EB  LD (HL),$EB $812E
# CHECK cartarea_store at 0462F ($462F bank 1): 36 E8  LD (HL),$E8 $8100
# CHECK cartarea_store at 04632 ($4632 bank 1): 36 18  LD (HL),$18 $8101
# CHECK cartarea_store at 04638 ($4638 bank 1): 36 E9  LD (HL),$E9 $8102,$8104,$8106,$8108...
# CHECK cartarea_store at 0463B ($463B bank 1): 36 18  LD (HL),$18 $8103,$8105,$8107,$8109...
# CHECK cartarea_store at 04640 ($4640 bank 1): 36 E8  LD (HL),$E8 $8104,$8106,$8108,$810A...
# CHECK cartarea_store at 04643 ($4643 bank 1): 36 1A  LD (HL),$1A $8105,$8107,$8109,$810B...
# CHECK cartarea_store at 04648 ($4648 bank 1): 36 EA  LD (HL),$EA $8106,$810C,$8112,$8118...
# CHECK cartarea_store at 0464B ($464B bank 1): 36 18  LD (HL),$18 $8107,$810D,$8113,$8115...
# CHECK cartarea_store at 04651 ($4651 bank 1): 36 E7  LD (HL),$E7 $8108,$810A,$810E,$8110...
# CHECK cartarea_store at 04654 ($4654 bank 1): 36 18  LD (HL),$18 $8109,$810F,$8111,$8115...
# CHECK cartarea_store at 04659 ($4659 bank 1): 36 EA  LD (HL),$EA $810A,$8110,$8112,$8116...
# CHECK cartarea_store at 0465C ($465C bank 1): 36 1A  LD (HL),$1A $810B,$8111,$8113,$8117...
# CHECK cartarea_store at 04662 ($4662 bank 1): 36 E8  LD (HL),$E8 $810C,$8112,$8114,$8118...
# CHECK cartarea_store at 04665 ($4665 bank 1): 36 1C  LD (HL),$1C $810D,$8113,$8115,$8119...
# CHECK cartarea_store at 0466B ($466B bank 1): 36 E9  LD (HL),$E9 $810E,$8110,$8112,$8114...
# CHECK cartarea_store at 0466E ($466E bank 1): 36 1C  LD (HL),$1C $810F,$8111,$8113,$8115...
# CHECK cartarea_store at 04673 ($4673 bank 1): 36 E8  LD (HL),$E8 $8110,$8112,$8114,$8116...
# CHECK cartarea_store at 04676 ($4676 bank 1): 36 1E  LD (HL),$1E $8111,$8113,$8115,$8117...
# CHECK indirect_unresolved at 00012 ($0012 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 00544 ($0544 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 04BB8 ($4BB8 bank 1): CF  RST $08 $0008
# CHECK indirect_unresolved at 06758 ($6758 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 0831F ($831F bank 2): C9  RET 
# CHECK indirect_unresolved at 1C876 ($8876 bank 7): C9  RET 
# CHECK bank_unresolved at 060E2 ($60E2 bank 1): CD D3 B9  CALL $B9D3 $B9D3
# CHECK bank_unresolved at 06152 ($6152 bank 1): CD 30 BA  CALL $BA30 $BA30
# CHECK bank_unresolved at 07E63 ($7E63 bank 1): CD FC 9E  CALL $9EFC $9EFC
# Mapper stores found by the byte scan in bytes no path reached:
mapst 03108   # LD ($FFFF),A; after LD A,$09; 32 bytes of valid code before it
mapld 03158   # LD HL,$FFFF; LD (HL),$09; after LD HL,$FFFF; 32 bytes of valid code before it
mapst 03176   # LD ($FFFC),A; after LD A,$08; 32 bytes of valid code before it
mapst 0317E   # LD ($FFFC),A; after XOR A: cart RAM off after reading a save slot word
mapst 0318A   # LD ($FFFC),A; after LD A,$08; 30 bytes of valid code before it
mapst 0318F   # LD ($FFFC),A; after another mapper store, LD ($FFFC),A at $0318A; 32 bytes of valid code before it
mapst 03E9D   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 03EB8   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
# CHECK medium: site 0D84F  OUT ($3F),A  (io_control; branch target from $0D843)
# CHECK medium: site 0DFFD  OUT ($DC),A  (no_effect; 14 bytes of valid code before it)
# CHECK low: site 0E028  OUTD  (port in C; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0E0D0  OUT (C),E  (port in C; no valid code after it)
# CHECK low: site 0E21F  OUT ($DC),A  (no_effect; no evidence)
# CHECK low: site 0E47E  OUT ($DC),A  (no_effect; 11 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0E525  OUT ($DC),A  (no_effect; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0E5FE  OUT ($DC),A  (no_effect; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0E80D  OUT ($DC),A  (no_effect; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0EC29  OUT ($DC),A  (no_effect; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0EF59  OUT ($F0),A  (fm_address; 5 RST or NOP opcodes around it (looks like data))
# CHECK low: site 0F60B  OUT ($DC),A  (no_effect; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0F629  OUT ($DC),A  (no_effect; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0F836  OUT ($DC),A  (no_effect; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0F863  OUT ($DC),A  (no_effect; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 13777  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK low: site 141C1  OUT ($7F),A  (psg; no evidence)
# CHECK low: site 14278  IN A,($BD)  (vdp_status; no evidence)
# CHECK high: site 165AC  IND  (port in C; branch target from $16573; 29 bytes of valid code before it)
# CHECK medium: site 178C5  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 1C14A  INIR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 28315  IN A,($BF)  (vdp_status; 9 RST or NOP opcodes around it (looks like data); 23 bytes of valid code before it)
# CHECK medium: site 2BE7C  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 2C019  OUT ($DD),A  (no_effect; no valid code after it)
# CHECK low: site 2C021  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 2C03C  OUT ($DD),A  (no_effect; no valid code after it)
# CHECK low: site 2C044  OUT ($DD),A  (no_effect; no valid code after it)
# CHECK low: site 2CCE5  OTDR  (port in C; no valid code after it)
# CHECK low: site 2CCE8  OTDR  (port in C; 10 bytes of valid code before it; no valid code after it)
# CHECK low: site 2CCF0  OTDR  (port in C; no evidence)
# CHECK low: site 2CD05  INDR  (port in C; no evidence)
# CHECK low: site 306A1  OUT ($DC),A  (no_effect; no evidence)
# CHECK low: site 306FD  OUT ($DC),A  (no_effect; 5 RST or NOP opcodes around it (looks like data); 18 bytes of valid code before it)
# CHECK medium: site 30E85  OUT ($DC),A  (no_effect; 12 bytes of valid code before it)
# CHECK low: site 30ED7  OUT ($DC),A  (no_effect; no valid code after it)
# CHECK low: site 31131  OUT ($DC),A  (no_effect; no valid code after it)
# CHECK low: site 3129E  OUT ($DC),A  (no_effect; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 31DD9  OUT ($F0),A  (fm_address; 28 bytes of valid code before it; no valid code after it)
# CHECK low: site 34BAD  OUT ($BD),A  (vdp_control; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 355C9  IN A,($F1)  (joypad_b_misc; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3712E  IN A,($BF)  (vdp_status; no evidence)
# CHECK medium: site 38351  OUT ($F2),A  (fm_control; 30 bytes of valid code before it)
# CHECK low: site 389A2  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 392CF  IN A,($BF)  (vdp_status; no evidence)
# CHECK high: site 39747  OUT ($F0),A  (fm_address; branch target from $39730; 32 bytes of valid code before it)
# CHECK medium: site 3AF60  IN A,($BD)  (vdp_status; 10 bytes of valid code before it)
# CHECK low: site 3D2BA  OUTI  (port in C; no evidence)
# CHECK low: site 3E35A  IN A,($7F)  (h_counter; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3E35D  OUT (C),A  (port in C; 5 RST or NOP opcodes around it (looks like data); 31 bytes of valid code before it)
# CHECK low: site 3EFD3  OUT ($DD),A  (no_effect; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 3FA60  OUT ($F2),A  (fm_control; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
