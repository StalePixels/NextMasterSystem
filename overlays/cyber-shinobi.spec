# Cyber Shinobi, The (Europe, Brazil) (En), CRC32 1350E4F8, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - $036A-$0969 is an unrolled block of 768 OUTIs that ends in the RET at $096A. The game
#   calls into it at many places for VRAM copies; every OUTI in it is a site.
# - $0970 copies that block to RAM at $D780 and turns every fourth OUTI into OUT ($BE),A:
#   a writer of 3-plane tiles with the fourth plane 0. Only the tile job dispatcher at $6B29
#   enters it, with JP (IX) at $6B58 to the entry its job record names. A code cave there
#   sends an entry in RAM to page 0, which writes the same bytes with jt_vwrite; an entry in
#   ROM jumps to the ROM block as before. The RAM copy itself is never run.
# - The stage records at $0D0B-$0E4C name the targets of the jumps at $0B01, $1B74, $2459
#   and $2505 (the stage loaders at $0BB2-$0CE2 and the stage handlers); the scan with
#   them as entry points proves the stage loaders' mapper stores.
# - The line handler ($1B75) runs the clock ($6C97) and the sound driver (bank 6 $8000) only
#   when the V counter reads below $40, at the line 62 event. On the Next the game reads it
#   a line or more late ($40 to $6D), so the test at $1B77 is CP $7F: the later line events
#   of the frame read $7F and $BE and are still skipped.
# - The status panel is lines 0-63; the line 62 event sets H scroll for the play area. hsplit
#   moves the map column with it: without it the play area showed the wrong map columns.
# - No priority: the priority cells are the status panel's rows, which sprites reach only at
#   its last 3 lines. With priority on, each rewrite of the play area's name table rows
#   ($046A, $6C45) cost several times more and play frames went over 100%.
# - The sprite clip window does the panel's priority instead. Every cell of name table rows
#   0-7 (lines 0-63) has the priority bit and no pixel of colour 0, and no other cell has the
#   bit, so on a Master System no sprite pixel shows on lines 0-63 while the panel is there.
#   The panel is there while the line 62 event runs: that event ($1B95) marks the frame
#   (page 0 clipln), and the frame interrupt ($010E) sets the sprite clip window from line 64
#   for the next frame when the frame was marked, and back to the whole picture once when
#   it was not (page 0 clipfr).
# - Spec gaps (data/scan-verdicts.tsv): false are byte patterns in the graphics banks 3, 5,
#   7, 11, 12 and 14.
name The Cyber Shinobi
cart 1350E4F8
hz 50		; No-Intro regions Europe, Brazil
hsplit
vector 18 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
site 000B8   ; OTIR
site 000FB   ; IN A,($BF)
site 00101   ; IN A,($DD)
site 00225   ; OUT ($BE),A
site 0022A   ; OUT ($BE),A
site 00234   ; OUT ($BE),A
site 0023F   ; OUT ($BE),A
site 00246   ; OUT ($BE),A
site 00254   ; OUTI
site 0025B   ; OUT (C),A
site 00271   ; OUTI
site 0029C   ; OUT ($BE),A
site 002CC   ; OUT ($BE),A
site 00322   ; OUT (C),D
site 00332   ; IN A,($DC)
site 00344   ; OTIR
site 0034F   ; IN A,($BF)
site 00351   ; IN A,($BF)
site 0035D   ; IN A,($BF)
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
site 00700   ; OUTI
site 00702   ; OUTI
site 00704   ; OUTI
site 00706   ; OUTI
site 00708   ; OUTI
site 0070A   ; OUTI
site 0070C   ; OUTI
site 0070E   ; OUTI
site 00710   ; OUTI
site 00712   ; OUTI
site 00714   ; OUTI
site 00716   ; OUTI
site 00718   ; OUTI
site 0071A   ; OUTI
site 0071C   ; OUTI
site 0071E   ; OUTI
site 00720   ; OUTI
site 00722   ; OUTI
site 00724   ; OUTI
site 00726   ; OUTI
site 00728   ; OUTI
site 0072A   ; OUTI
site 0072C   ; OUTI
site 0072E   ; OUTI
site 00730   ; OUTI
site 00732   ; OUTI
site 00734   ; OUTI
site 00736   ; OUTI
site 00738   ; OUTI
site 0073A   ; OUTI
site 0073C   ; OUTI
site 0073E   ; OUTI
site 00740   ; OUTI
site 00742   ; OUTI
site 00744   ; OUTI
site 00746   ; OUTI
site 00748   ; OUTI
site 0074A   ; OUTI
site 0074C   ; OUTI
site 0074E   ; OUTI
site 00750   ; OUTI
site 00752   ; OUTI
site 00754   ; OUTI
site 00756   ; OUTI
site 00758   ; OUTI
site 0075A   ; OUTI
site 0075C   ; OUTI
site 0075E   ; OUTI
site 00760   ; OUTI
site 00762   ; OUTI
site 00764   ; OUTI
site 00766   ; OUTI
site 00768   ; OUTI
site 0076A   ; OUTI
site 0076C   ; OUTI
site 0076E   ; OUTI
site 00770   ; OUTI
site 00772   ; OUTI
site 00774   ; OUTI
site 00776   ; OUTI
site 00778   ; OUTI
site 0077A   ; OUTI
site 0077C   ; OUTI
site 0077E   ; OUTI
site 00780   ; OUTI
site 00782   ; OUTI
site 00784   ; OUTI
site 00786   ; OUTI
site 00788   ; OUTI
site 0078A   ; OUTI
site 0078C   ; OUTI
site 0078E   ; OUTI
site 00790   ; OUTI
site 00792   ; OUTI
site 00794   ; OUTI
site 00796   ; OUTI
site 00798   ; OUTI
site 0079A   ; OUTI
site 0079C   ; OUTI
site 0079E   ; OUTI
site 007A0   ; OUTI
site 007A2   ; OUTI
site 007A4   ; OUTI
site 007A6   ; OUTI
site 007A8   ; OUTI
site 007AA   ; OUTI
site 007AC   ; OUTI
site 007AE   ; OUTI
site 007B0   ; OUTI
site 007B2   ; OUTI
site 007B4   ; OUTI
site 007B6   ; OUTI
site 007B8   ; OUTI
site 007BA   ; OUTI
site 007BC   ; OUTI
site 007BE   ; OUTI
site 007C0   ; OUTI
site 007C2   ; OUTI
site 007C4   ; OUTI
site 007C6   ; OUTI
site 007C8   ; OUTI
site 007CA   ; OUTI
site 007CC   ; OUTI
site 007CE   ; OUTI
site 007D0   ; OUTI
site 007D2   ; OUTI
site 007D4   ; OUTI
site 007D6   ; OUTI
site 007D8   ; OUTI
site 007DA   ; OUTI
site 007DC   ; OUTI
site 007DE   ; OUTI
site 007E0   ; OUTI
site 007E2   ; OUTI
site 007E4   ; OUTI
site 007E6   ; OUTI
site 007E8   ; OUTI
site 007EA   ; OUTI
site 007EC   ; OUTI
site 007EE   ; OUTI
site 007F0   ; OUTI
site 007F2   ; OUTI
site 007F4   ; OUTI
site 007F6   ; OUTI
site 007F8   ; OUTI
site 007FA   ; OUTI
site 007FC   ; OUTI
site 007FE   ; OUTI
site 00800   ; OUTI
site 00802   ; OUTI
site 00804   ; OUTI
site 00806   ; OUTI
site 00808   ; OUTI
site 0080A   ; OUTI
site 0080C   ; OUTI
site 0080E   ; OUTI
site 00810   ; OUTI
site 00812   ; OUTI
site 00814   ; OUTI
site 00816   ; OUTI
site 00818   ; OUTI
site 0081A   ; OUTI
site 0081C   ; OUTI
site 0081E   ; OUTI
site 00820   ; OUTI
site 00822   ; OUTI
site 00824   ; OUTI
site 00826   ; OUTI
site 00828   ; OUTI
site 0082A   ; OUTI
site 0082C   ; OUTI
site 0082E   ; OUTI
site 00830   ; OUTI
site 00832   ; OUTI
site 00834   ; OUTI
site 00836   ; OUTI
site 00838   ; OUTI
site 0083A   ; OUTI
site 0083C   ; OUTI
site 0083E   ; OUTI
site 00840   ; OUTI
site 00842   ; OUTI
site 00844   ; OUTI
site 00846   ; OUTI
site 00848   ; OUTI
site 0084A   ; OUTI
site 0084C   ; OUTI
site 0084E   ; OUTI
site 00850   ; OUTI
site 00852   ; OUTI
site 00854   ; OUTI
site 00856   ; OUTI
site 00858   ; OUTI
site 0085A   ; OUTI
site 0085C   ; OUTI
site 0085E   ; OUTI
site 00860   ; OUTI
site 00862   ; OUTI
site 00864   ; OUTI
site 00866   ; OUTI
site 00868   ; OUTI
site 0086A   ; OUTI
site 0086C   ; OUTI
site 0086E   ; OUTI
site 00870   ; OUTI
site 00872   ; OUTI
site 00874   ; OUTI
site 00876   ; OUTI
site 00878   ; OUTI
site 0087A   ; OUTI
site 0087C   ; OUTI
site 0087E   ; OUTI
site 00880   ; OUTI
site 00882   ; OUTI
site 00884   ; OUTI
site 00886   ; OUTI
site 00888   ; OUTI
site 0088A   ; OUTI
site 0088C   ; OUTI
site 0088E   ; OUTI
site 00890   ; OUTI
site 00892   ; OUTI
site 00894   ; OUTI
site 00896   ; OUTI
site 00898   ; OUTI
site 0089A   ; OUTI
site 0089C   ; OUTI
site 0089E   ; OUTI
site 008A0   ; OUTI
site 008A2   ; OUTI
site 008A4   ; OUTI
site 008A6   ; OUTI
site 008A8   ; OUTI
site 008AA   ; OUTI
site 008AC   ; OUTI
site 008AE   ; OUTI
site 008B0   ; OUTI
site 008B2   ; OUTI
site 008B4   ; OUTI
site 008B6   ; OUTI
site 008B8   ; OUTI
site 008BA   ; OUTI
site 008BC   ; OUTI
site 008BE   ; OUTI
site 008C0   ; OUTI
site 008C2   ; OUTI
site 008C4   ; OUTI
site 008C6   ; OUTI
site 008C8   ; OUTI
site 008CA   ; OUTI
site 008CC   ; OUTI
site 008CE   ; OUTI
site 008D0   ; OUTI
site 008D2   ; OUTI
site 008D4   ; OUTI
site 008D6   ; OUTI
site 008D8   ; OUTI
site 008DA   ; OUTI
site 008DC   ; OUTI
site 008DE   ; OUTI
site 008E0   ; OUTI
site 008E2   ; OUTI
site 008E4   ; OUTI
site 008E6   ; OUTI
site 008E8   ; OUTI
site 008EA   ; OUTI
site 008EC   ; OUTI
site 008EE   ; OUTI
site 008F0   ; OUTI
site 008F2   ; OUTI
site 008F4   ; OUTI
site 008F6   ; OUTI
site 008F8   ; OUTI
site 008FA   ; OUTI
site 008FC   ; OUTI
site 008FE   ; OUTI
site 00900   ; OUTI
site 00902   ; OUTI
site 00904   ; OUTI
site 00906   ; OUTI
site 00908   ; OUTI
site 0090A   ; OUTI
site 0090C   ; OUTI
site 0090E   ; OUTI
site 00910   ; OUTI
site 00912   ; OUTI
site 00914   ; OUTI
site 00916   ; OUTI
site 00918   ; OUTI
site 0091A   ; OUTI
site 0091C   ; OUTI
site 0091E   ; OUTI
site 00920   ; OUTI
site 00922   ; OUTI
site 00924   ; OUTI
site 00926   ; OUTI
site 00928   ; OUTI
site 0092A   ; OUTI
site 0092C   ; OUTI
site 0092E   ; OUTI
site 00930   ; OUTI
site 00932   ; OUTI
site 00934   ; OUTI
site 00936   ; OUTI
site 00938   ; OUTI
site 0093A   ; OUTI
site 0093C   ; OUTI
site 0093E   ; OUTI
site 00940   ; OUTI
site 00942   ; OUTI
site 00944   ; OUTI
site 00946   ; OUTI
site 00948   ; OUTI
site 0094A   ; OUTI
site 0094C   ; OUTI
site 0094E   ; OUTI
site 00950   ; OUTI
site 00952   ; OUTI
site 00954   ; OUTI
site 00956   ; OUTI
site 00958   ; OUTI
site 0095A   ; OUTI
site 0095C   ; OUTI
site 0095E   ; OUTI
site 00960   ; OUTI
site 00962   ; OUTI
site 00964   ; OUTI
site 00966   ; OUTI
site 00968   ; OUTI
otir 0096B   ; OUTI
site 00A4F   ; OUT ($BF),A
site 00A53   ; OUT ($BF),A
site 00A56   ; OUT ($BF),A
site 00A5A   ; OUT ($BF),A
site 00B0A   ; OUT ($BF),A
site 00B0E   ; OUT ($BF),A
site 00B11   ; OUT ($BE),A
site 00F10   ; OUT ($BE),A
site 018E4   ; OUT ($BE),A
site 019C7   ; OUT ($BE),A
site 01A00   ; OUT ($BE),A
site 01A39   ; OUT ($BE),A
site 01A3C   ; OUT ($BE),A
site 01A42   ; OUT ($BE),A
site 01B75   ; IN A,($7E)
site 01B7E   ; OUT ($BF),A
site 01B82   ; OUT ($BF),A
site 01B87   ; OUT ($BF),A
site 01B8B   ; OUT ($BF),A
site 06C37   ; OUTI
site 06C39   ; OUTI
site 06C44   ; OUTI
site 06C46   ; OUTI
site 06F54   ; OUT ($BE),A
site 06F5C   ; OUT ($BE),A
site 070C6   ; OUT ($BE),A
site 070CE   ; OUT ($BE),A
site 0747A   ; OUT ($BF),A
site 0747E   ; OUT ($BF),A
site 181CA   ; OUT ($7F),A
site 182B2   ; OUT ($7F),A
site 18444   ; OTIR
site 1855A   ; OUT ($7F),A
site 18564   ; OUT ($7F),A
site 18581   ; OUT ($7F),A
site 18685   ; OUT ($7F),A
site 18713   ; OUT ($7F),A
site 18798   ; OUT ($06),A
site 187E2   ; OUT ($7F),A
site 187EB   ; OUT ($7F),A
site 187FB   ; OUT ($7F),A
site 1886F   ; OUT ($7F),A
mapldk 00088   # LD HL,$FFFC; LD (HL),$80
maphl 0008E   # LD (HL),$00, HL = $FFFD
maphl 00091   # LD (HL),$01, HL = $FFFE
maphl 00094   # LD (HL),$02, HL = $FFFF
mapst 00112   ; LD ($FFFF),A
mapst 009A4   ; LD ($FFFF),A
mapst 009B2   ; LD ($FFFF),A
mapst 009C0   ; LD ($FFFF),A
mapst 00B61   ; LD ($FFFF),A
mapst 01049   ; LD ($FFFF),A
mapst 01102   ; LD ($FFFF),A
mapst 01180   ; LD ($FFFF),A
mapst 01273   ; LD ($FFFF),A
mapst 0133B   ; LD ($FFFF),A
mapst 01419   ; LD ($FFFF),A
mapst 015C0   ; LD ($FFFF),A
mapst 015CE   ; LD ($FFFF),A
mapst 01632   ; LD ($FFFF),A
mapst 01671   ; LD ($FFFF),A
mapst 018E8   ; LD ($FFFF),A
mapst 0198A   ; LD ($FFFF),A
mapst 01AD8   ; LD ($FFFF),A
mapst 01B8F   ; LD ($FFFF),A
mapst 02173   ; LD ($FFFF),A
mapst 024BB   ; LD ($FFFF),A
mapst 024D8   ; LD ($FFFF),A
mapst 024FF   ; LD ($FFFF),A
mapst 06B40   ; LD ($FFFF),A
mapst 06BB1   ; LD ($FFFF),A
mapst 06BD6   ; LD ($FFFF),A
mapst 06D00   ; LD ($FFFF),A
mapst 06E05   ; LD ($FFFF),A
mapst 06E18   ; LD ($FFFF),A
mapst 06EEA   ; LD ($FFFF),A
mapst 06FC1   ; LD ($FFFF),A
mapst 07061   ; LD ($FFFF),A
mapst 07152   ; LD ($FFFF),A
mapst 07297   ; LD ($FFFF),A
mapst 072AA   ; LD ($FFFF),A
mapst 072F2   ; LD ($FFFF),A
mapst 0733E   ; LD ($FFFF),A
mapst 07580   ; LD ($FFFF),A
mapst 07593   ; LD ($FFFF),A
mapst 07671   ; LD ($FFFF),A
mapst 07684   ; LD ($FFFF),A
mapst 076D2   ; LD ($FFFF),A
mapst 076DA   ; LD ($FFFF),A
mapst 077D3   ; LD ($FFFF),A
mapst 077E4   ; LD ($FFFF),A
mapst 077F7   ; LD ($FFFF),A
mapst 07852   ; LD ($FFFF),A
mapst 07871   ; LD ($FFFF),A
mapst 078D8   ; LD ($FFFF),A
mapst 00BD4   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 00BF5   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 00C0C   # LD ($FFFF),A; after LD A,$07; JP/CALL target from $1C426 $3C4D0; 32 bytes of valid code before it
mapst 00C30   # LD ($FFFF),A; after LD A,$0C; JP/CALL target from $29FAE; 32 bytes of valid code before it
mapst 00C57   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 00C65   # LD ($FFFF),A; after LD A,$0C; 32 bytes of valid code before it
mapst 00C97   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 00CA5   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 00CC9   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 00CD7   # LD ($FFFF),A; after LD A,$0D; 32 bytes of valid code before it
mapst 0669A   # LD ($FFFF),A; after LD A,$0C; JP/CALL target from $3ECCA; 32 bytes of valid code before it
asm 01B77 2    ; CP $40: the line event at line 62 reads the V counter a line or more late
    cp $7F
endasm
label cv_tiles 07988
asm 06B52 8    ; PUSH DE; POP IX; LD C,$BE; XOR A; JP (IX)
    jp cv_tiles
endasm
asm 07988 17   ; unused $FF bytes of bank 1: the tile job's jump to its writer
    push de
    pop ix
    ld c,$BE
    xor a
    bit 7,d
    jr nz,.ram
    jp (ix)                     ; the OUTI block in ROM
.ram:
    rst $18
    db far_io, pg_ramtiles, ent_ramtiles
    ret
endasm
label cv_frame 0799A
label cv_lnev 079A1
asm 0010E 3    ; CALL $0125: the frame interrupt's work
    call cv_frame
endasm
asm 01B95 3    ; CALL $6C97: the clock tick at the line 62 event
    call cv_lnev
endasm
asm 0799A 14   ; unused $FF bytes of bank 1: the sprite clip at the frame and the line event
    rst $18
    db far_io, pg_clipfr, ent_clipfr
    jp $0125
    rst $18
    db far_io, pg_clipln, ent_clipln
    jp $6C97
endasm
page 0 ramtiles clipln clipfr
    OPT --zxnext        ; ADD HL,A, ADD DE,A, ADD HL,nn
; ramtiles: as the game's RAM tile writer at $D780-$DD80 (the copy of $036A-$096A that
; $0970 makes, with every fourth OUTI turned into OUT ($BE),A), entered at IX. Slot k of
; the 768 (from $D780 + 2k) writes a source byte, or 0 when k & 3 = 3. HL = the source,
; C = $BE, A = 0, the VDP address set. Builds the bytes of slots k to 767 in buf, then
; writes them from the VDP address with jt_vwrite in runs of 256, the rest last, so the
; VDP address ends after the last byte, as the game's writes leave it. Returns HL past the
; source bytes, B less their count, A = 0, Z when B is 0; C, DE, IX and IY kept.
ramtiles:
        ld (sv_hl0),hl
        ld (sv_bc),bc
        ld (sv_de),de
        ld (sv_ix),ix
        ld (sv_iy),iy
        push hl
        push ix
        pop hl
        ld de,$D780
        or a
        sbc hl,de
        srl h
        rr l                    ; HL = k, the entry slot (0-767)
        ex de,hl
        ld hl,768
        or a
        sbc hl,de
        ld (cnt),hl             ; the bytes to write
        ld b,h
        ld c,l
        ld a,e
        and 3
        ld e,a                  ; E = k & 3
        pop hl                  ; the source
        ld ix,buf
.fill:  ld a,e
        cp 3
        jr z,.z
        ld a,h
        and $E0
        cp $20
        jr z,.peek
        ld a,(hl)
        jr .put
.peek:  call jt_peek
        jr .put
.z:     xor a
        ld (ix+0),a
        ld e,$FF
        jr .next
.put:   ld (ix+0),a
        inc hl
.next:  inc ix
        inc e
        dec bc
        ld a,b
        or c
        jr nz,.fill
        ld (sv_hl),hl
        ld hl,(vdp_addr)
        ld a,h
        and $3F
        ld d,a
        ld e,l
        ld hl,buf
        ld a,(cnt+1)
        or a
        jr z,.rest
        ld c,a                  ; whole runs of 256
        ld b,0
        ld ix,256
        ld iy,256
        ld a,1                  ; the source is this page
        call jt_vwrite
        ld a,(cnt+1)
        add a,h
        ld h,a
        ld a,(cnt+1)
        add a,d
        ld d,a
.rest:  ld a,(cnt)
        or a
        jr z,.done
        ld b,a
        ld c,1
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
.done:  ld hl,(sv_hl)
        ld de,(sv_bc)           ; B less the source bytes read
        ld bc,(sv_hl0)
        or a
        sbc hl,bc               ; HL = the source bytes read
        ld a,d
        sub l
        ld b,a
        ld c,e
        ld hl,(sv_hl)
        ld de,(sv_de)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld a,b
        or a
        ld a,0
        ret
sv_hl:  dw 0
sv_hl0: dw 0
sv_bc:  dw 0
sv_de:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
cnt:    dw 0

; clipln: at the line 62 event, which runs only while the status panel is on the screen:
; marks the frame. Keeps every register.
clipln:
        push af
        ld a,1
        ld (cl_seen),a
        pop af
        ret

; clipfr: at the frame interrupt. After a marked frame, the sprite clip window starts at
; Next line 96 (line 64 of the picture, under the panel) for the next frame; it is written
; every such frame, so a clip_update of the runtime in between cannot leave it open. After
; an unmarked frame that follows a marked one, the window goes back to the runtime's own
; (as its clip_update: X from 17, or 21 when register 0 bit 5 hides column 0, to 144;
; lines 32-223, or 16-239 in 224-line mode). Runtime internal used: m224 ($E08F).
; Keeps every register.
clipfr:
        push af
        push bc
        ld a,(cl_seen)
        ld b,a
        xor a
        ld (cl_seen),a
        ld a,b
        or a
        jr nz,.on
        ld a,(cl_on)
        or a
        jr z,.out
        xor a
        ld (cl_on),a
        ld bc,32*256+223
        ld a,($E08F)            ; m224
        or a
        jr z,.set
        ld bc,16*256+239
        jr .set
.on:    ld a,1
        ld (cl_on),a
        ld bc,96*256+223
.set:   ld a,(vdp_regs+0)
        and $20
        jr z,.x
        ld a,4
.x:     add a,17
        nextreg $1C,%00000010   ; reset the sprite clip index
        nextreg $19,a
        nextreg $19,144
        ld a,b
        nextreg $19,a
        ld a,c
        nextreg $19,a
.out:   pop bc
        pop af
        ret
cl_seen: db 0
cl_on:  db 0
buf:    ds 768
endpage

# Cyber Shinobi, The (Europe) (Action Replay).cht and Cyber Shinobi, The (Europe, Brazil).cht,
# "Infinite Lives": RAM $C00E is the number of lives
poke "Infinite lives"
ar 00C0-0E05
endpoke

# Cyber Shinobi, The (Europe) (Action Replay).cht and Cyber Shinobi, The (Europe, Brazil).cht,
# "Infinite Health": RAM $C11C is the life bar, $23 when full
poke "Infinite health"
ar 00C1-1C23
endpoke

# Cyber Shinobi, The (Europe) (Action Replay).cht and Cyber Shinobi, The (Europe, Brazil).cht,
# "Infinite Seconds - One's Digit", "Infinite Seconds - Ten's Digit", "Infinite Minutes -
# One's Digit" and "Infinite Minutes - Ten's Digit": RAM $C014-$C017 are the four digits of
# TIME LEFT, and all four are needed; the clock shows 99:99 and no longer runs out
poke "Infinite time"
ar 00C0-1409
ar 00C0-1509
ar 00C0-1609
ar 00C0-1709
endpoke

# Cyber Shinobi, The (Europe) (Action Replay).cht, "Have Ninjutsu And It Is Infinite": RAM
# $C011 is the ninjutsu level, shown as a bar of that many segments (8 is full). The
# Europe, Brazil file has $00 here, which shows no ninjutsu; the other file has a placeholder
poke "Ninjutsu"
ar 00C0-11??
endpoke

# Cyber Shinobi, The (Europe) (Action Replay).cht and Cyber Shinobi, The (Europe, Brazil).cht,
# "Have Shot And It Is Infinite": RAM $C012 is the shot level, spent by Button 1 with Up
poke "Infinite shot"
ar 00C0-1208
endpoke

# Cyber Shinobi, The (Europe) (Action Replay).cht and Cyber Shinobi, The (Europe, Brazil).cht,
# "Maximum Power": RAM $C010 is the POWER bar, $08 when full; a sword hit takes the power plus 1
# from the enemy's life
poke "Maximum power"
ar 00C0-1008
endpoke
