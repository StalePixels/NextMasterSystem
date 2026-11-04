# Golden Axe (USA, Europe, Brazil) (En), CRC32 C08132FB, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, checked against a reference I/O log
# (600 s of random input).
# Decisions:
# - $0030-$0032 are $FF filler that no code uses, so $30 is the io vector.
# - The game draws the play field by writing name table rows from RAM with the unrolled
#   OUTI chain $0284-$0A8D, entered part way down (JP $098E from $2F83 and others), so
#   every OUTI in the chain is a site.
# - The tile writers $0A8F-$0E8E (OUTI, OUTI, OUTI, OUT (C),A per tile row) and
#   $0E90-$0EC3 (OUTI, OUT (C),A) are code: unrolled runs between the RETs at $0A8E,
#   $0E8F and $0EC4, in the same block as the chain above. No path, recording or
#   address in the cart reaches them; their sites are patched so that an entry that
#   the scan cannot see still works.
# - The main loop at $00BB runs the game state from the word table at $00D1 by
#   $C002. The scanner reads only part of the table; the states $17C2, $184F and
#   $7D1D write the sprite table at $17CA, $185C and $7EE6-$7F00.
# - HALT: EI; HALT at $01CC, $01FC, $17F2 and $7D14 wait for one frame interrupt
#   (eihalt). $17C2 and $184F are single HALTs at the start of a state, and $3117 is
#   HALT; HALT; RET: each jumps to a cave in the unused $FF bytes at $7F20, where the
#   waits run as HALT codes. The HALTs at $1237, $1588, $30CE and $3102 wait in a loop
#   for the frame counter $C002, which the interrupt handler sets, and need no patch.
# - The mapper store byte patterns in banks 7 and above are data (sound and graphics
#   tables); $4D199 follows the data bytes at $4D195.
name Golden Axe
cart C08132FB
hz any		; No-Intro regions USA, Europe, Brazil
vector 30 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
site 0011A   ; IN A,($BF)
site 0011C   ; IN A,($DD)
site 0020B   ; OTIR
site 00250   ; OUT ($BE),A
site 00255   ; OUT ($BE),A
site 0025F   ; OUT ($BE),A
site 0026A   ; OUT ($BE),A
site 00271   ; OUT ($BE),A
site 00284   ; OUTI
site 0028B   ; OUT (C),A
site 002A1   ; OUTI
site 002CC   ; OUT ($BE),A
site 002FB   ; OUT ($BE),A
site 0033E   ; OUT ($3F),A
site 00340   ; IN A,($DD)
site 00349   ; OUT ($3F),A
site 0034B   ; IN A,($DD)
site 00353   ; OUT ($3F),A
site 0036B   ; IN A,($DC)
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
site 0096A   ; OUTI
site 0096C   ; OUTI
site 0096E   ; OUTI
site 00970   ; OUTI
site 00972   ; OUTI
site 00974   ; OUTI
site 00976   ; OUTI
site 00978   ; OUTI
site 0097A   ; OUTI
site 0097C   ; OUTI
site 0097E   ; OUTI
site 00980   ; OUTI
site 00982   ; OUTI
site 00984   ; OUTI
site 00986   ; OUTI
site 00988   ; OUTI
site 0098A   ; OUTI
site 0098C   ; OUTI
site 0098E   ; OUTI
site 00990   ; OUTI
site 00992   ; OUTI
site 00994   ; OUTI
site 00996   ; OUTI
site 00998   ; OUTI
site 0099A   ; OUTI
site 0099C   ; OUTI
site 0099E   ; OUTI
site 009A0   ; OUTI
site 009A2   ; OUTI
site 009A4   ; OUTI
site 009A6   ; OUTI
site 009A8   ; OUTI
site 009AA   ; OUTI
site 009AC   ; OUTI
site 009AE   ; OUTI
site 009B0   ; OUTI
site 009B2   ; OUTI
site 009B4   ; OUTI
site 009B6   ; OUTI
site 009B8   ; OUTI
site 009BA   ; OUTI
site 009BC   ; OUTI
site 009BE   ; OUTI
site 009C0   ; OUTI
site 009C2   ; OUTI
site 009C4   ; OUTI
site 009C6   ; OUTI
site 009C8   ; OUTI
site 009CA   ; OUTI
site 009CC   ; OUTI
site 009CE   ; OUTI
site 009D0   ; OUTI
site 009D2   ; OUTI
site 009D4   ; OUTI
site 009D6   ; OUTI
site 009D8   ; OUTI
site 009DA   ; OUTI
site 009DC   ; OUTI
site 009DE   ; OUTI
site 009E0   ; OUTI
site 009E2   ; OUTI
site 009E4   ; OUTI
site 009E6   ; OUTI
site 009E8   ; OUTI
site 009EA   ; OUTI
site 009EC   ; OUTI
site 009EE   ; OUTI
site 009F0   ; OUTI
site 009F2   ; OUTI
site 009F4   ; OUTI
site 009F6   ; OUTI
site 009F8   ; OUTI
site 009FA   ; OUTI
site 009FC   ; OUTI
site 009FE   ; OUTI
site 00A00   ; OUTI
site 00A02   ; OUTI
site 00A04   ; OUTI
site 00A06   ; OUTI
site 00A08   ; OUTI
site 00A0A   ; OUTI
site 00A0C   ; OUTI
site 00A0E   ; OUTI
site 00A10   ; OUTI
site 00A12   ; OUTI
site 00A14   ; OUTI
site 00A16   ; OUTI
site 00A18   ; OUTI
site 00A1A   ; OUTI
site 00A1C   ; OUTI
site 00A1E   ; OUTI
site 00A20   ; OUTI
site 00A22   ; OUTI
site 00A24   ; OUTI
site 00A26   ; OUTI
site 00A28   ; OUTI
site 00A2A   ; OUTI
site 00A2C   ; OUTI
site 00A2E   ; OUTI
site 00A30   ; OUTI
site 00A32   ; OUTI
site 00A34   ; OUTI
site 00A36   ; OUTI
site 00A38   ; OUTI
site 00A3A   ; OUTI
site 00A3C   ; OUTI
site 00A3E   ; OUTI
site 00A40   ; OUTI
site 00A42   ; OUTI
site 00A44   ; OUTI
site 00A46   ; OUTI
site 00A48   ; OUTI
site 00A4A   ; OUTI
site 00A4C   ; OUTI
site 00A4E   ; OUTI
site 00A50   ; OUTI
site 00A52   ; OUTI
site 00A54   ; OUTI
site 00A56   ; OUTI
site 00A58   ; OUTI
site 00A5A   ; OUTI
site 00A5C   ; OUTI
site 00A5E   ; OUTI
site 00A60   ; OUTI
site 00A62   ; OUTI
site 00A64   ; OUTI
site 00A66   ; OUTI
site 00A68   ; OUTI
site 00A6A   ; OUTI
site 00A6C   ; OUTI
site 00A6E   ; OUTI
site 00A70   ; OUTI
site 00A72   ; OUTI
site 00A74   ; OUTI
site 00A76   ; OUTI
site 00A78   ; OUTI
site 00A7A   ; OUTI
site 00A7C   ; OUTI
site 00A7E   ; OUTI
site 00A80   ; OUTI
site 00A82   ; OUTI
site 00A84   ; OUTI
site 00A86   ; OUTI
site 00A88   ; OUTI
site 00A8A   ; OUTI
site 00A8C   ; OUTI
otir 00FC7   ; OUTI
site 010CD   ; OUT ($BF),A
site 010D9   ; OUT ($BF),A
site 010F9   ; OUT ($BF),A
site 01105   ; OUT ($BF),A
site 01127   ; OUT ($BF),A
site 0112B   ; OUT ($BF),A
site 01140   ; OUT ($BF),A
site 01144   ; OUT ($BF),A
site 0114D   ; OUT ($BF),A
site 01151   ; OUT ($BF),A
site 0117B   ; OUT ($BF),A
site 0117F   ; OUT ($BF),A
site 011A8   ; OUT ($BF),A
site 011AC   ; OUT ($BF),A
site 01829   ; OUTI
site 0182B   ; OUTI
site 01840   ; OUT ($BE),A
site 0188C   ; OUT ($BE),A
site 018B1   ; OUT ($BE),A
site 018B3   ; OUT ($BE),A
site 0297C   ; OUT ($BE),A
site 029BD   ; OUTI
site 029C2   ; OUTI
site 02A7F   ; OUT ($BE),A
site 02A85   ; IN A,($BE)
site 02A8B   ; OUT ($BE),A
site 02A93   ; IN A,($BE)
site 02A98   ; OUTI
site 02A9E   ; OUT ($BE),A
site 02B9F   ; OUT ($BF),A
site 02BA3   ; OUT ($BF),A
site 02BB3   ; OUT ($BE),A
site 02C60   ; OUTI
site 02C62   ; OUTI
site 02C66   ; OUTI
site 02C68   ; OUTI
site 02CE3   ; OUTI
site 02CE5   ; OUTI
site 02CE9   ; OUTI
site 02CEB   ; OUTI
site 02D57   ; OUTI
site 02D59   ; OUTI
site 02F6A   ; OUT ($BF),A
site 02F6E   ; OUT ($BF),A
site 02F7A   ; OUT ($BF),A
site 02F7E   ; OUT ($BF),A
site 032AA   ; OUT ($BE),A
site 0812F   ; OUT ($7F),A
site 08147   ; OUT ($7F),A
site 08162   ; OUT ($7F),A
site 08166   ; OUT ($7F),A
site 0818B   ; OTIR
site 08194   ; OTIR
site 082CB   ; OUT ($7F),A
site 082CF   ; OUT ($7F),A
site 08335   ; OUT ($7F),A
site 08339   ; OUT ($7F),A
site 0835C   ; OUT ($7F),A
site 08360   ; OUT ($7F),A
site 08369   ; OUT ($7F),A
site 0836D   ; OUT ($7F),A
site 08370   ; OUT ($7F),A
site 08561   ; OUT ($7F),A
site 085F1   ; OUT ($7F),A
site 0861F   ; OUT ($7F),A
site 08623   ; OUT ($7F),A
site 08633   ; OUT ($7F),A
site 08638   ; OUT ($7F),A
site 086CF   ; OUTI
site 086D1   ; OUTI
site 086D3   ; OUTI
site 086D5   ; OUTI
site 086D7   ; OUTI
site 086D9   ; OUTI
site 086DB   ; OUTI
site 086DD   ; OUTI
site 086DF   ; OUTI
site 086E1   ; OUTI
site 086E3   ; OUTI
site 0871C   ; OUT ($7F),A
site 08772   ; OUT ($7F),A
site 087B3   ; OUT ($7F),A
site 08815   ; OUT ($7F),A
site 08835   ; OUT ($7F),A
site 08875   ; OUT ($7F),A
site 0887F   ; OUT ($7F),A
site 088C7   ; OUT ($7F),A
site 017CA   ; OUT ($BE),A
site 0185C   ; OUT ($BE),A
site 07EE6   ; OUT ($BE),A
site 07EEC   ; OUT ($BE),A
site 07EF9   ; OUT ($BE),A
site 07F00   ; OUT ($BE),A
# The tile writers at $0A8F (three OUTI and one OUT (C),A a row) and $0E90
# (one OUTI and one OUT (C),A a row): unrolled code between the RETs at $0A8E,
# $0E8F and $0EC4, next to the reached chains, with no reference in the cart.
site 00A8F   ; OUTI
site 00A91   ; OUTI
site 00A93   ; OUTI
site 00A95   ; OUT (C),A
site 00A97   ; OUTI
site 00A99   ; OUTI
site 00A9B   ; OUTI
site 00A9D   ; OUT (C),A
site 00A9F   ; OUTI
site 00AA1   ; OUTI
site 00AA3   ; OUTI
site 00AA5   ; OUT (C),A
site 00AA7   ; OUTI
site 00AA9   ; OUTI
site 00AAB   ; OUTI
site 00AAD   ; OUT (C),A
site 00AAF   ; OUTI
site 00AB1   ; OUTI
site 00AB3   ; OUTI
site 00AB5   ; OUT (C),A
site 00AB7   ; OUTI
site 00AB9   ; OUTI
site 00ABB   ; OUTI
site 00ABD   ; OUT (C),A
site 00ABF   ; OUTI
site 00AC1   ; OUTI
site 00AC3   ; OUTI
site 00AC5   ; OUT (C),A
site 00AC7   ; OUTI
site 00AC9   ; OUTI
site 00ACB   ; OUTI
site 00ACD   ; OUT (C),A
site 00ACF   ; OUTI
site 00AD1   ; OUTI
site 00AD3   ; OUTI
site 00AD5   ; OUT (C),A
site 00AD7   ; OUTI
site 00AD9   ; OUTI
site 00ADB   ; OUTI
site 00ADD   ; OUT (C),A
site 00ADF   ; OUTI
site 00AE1   ; OUTI
site 00AE3   ; OUTI
site 00AE5   ; OUT (C),A
site 00AE7   ; OUTI
site 00AE9   ; OUTI
site 00AEB   ; OUTI
site 00AED   ; OUT (C),A
site 00AEF   ; OUTI
site 00AF1   ; OUTI
site 00AF3   ; OUTI
site 00AF5   ; OUT (C),A
site 00AF7   ; OUTI
site 00AF9   ; OUTI
site 00AFB   ; OUTI
site 00AFD   ; OUT (C),A
site 00AFF   ; OUTI
site 00B01   ; OUTI
site 00B03   ; OUTI
site 00B05   ; OUT (C),A
site 00B07   ; OUTI
site 00B09   ; OUTI
site 00B0B   ; OUTI
site 00B0D   ; OUT (C),A
site 00B0F   ; OUTI
site 00B11   ; OUTI
site 00B13   ; OUTI
site 00B15   ; OUT (C),A
site 00B17   ; OUTI
site 00B19   ; OUTI
site 00B1B   ; OUTI
site 00B1D   ; OUT (C),A
site 00B1F   ; OUTI
site 00B21   ; OUTI
site 00B23   ; OUTI
site 00B25   ; OUT (C),A
site 00B27   ; OUTI
site 00B29   ; OUTI
site 00B2B   ; OUTI
site 00B2D   ; OUT (C),A
site 00B2F   ; OUTI
site 00B31   ; OUTI
site 00B33   ; OUTI
site 00B35   ; OUT (C),A
site 00B37   ; OUTI
site 00B39   ; OUTI
site 00B3B   ; OUTI
site 00B3D   ; OUT (C),A
site 00B3F   ; OUTI
site 00B41   ; OUTI
site 00B43   ; OUTI
site 00B45   ; OUT (C),A
site 00B47   ; OUTI
site 00B49   ; OUTI
site 00B4B   ; OUTI
site 00B4D   ; OUT (C),A
site 00B4F   ; OUTI
site 00B51   ; OUTI
site 00B53   ; OUTI
site 00B55   ; OUT (C),A
site 00B57   ; OUTI
site 00B59   ; OUTI
site 00B5B   ; OUTI
site 00B5D   ; OUT (C),A
site 00B5F   ; OUTI
site 00B61   ; OUTI
site 00B63   ; OUTI
site 00B65   ; OUT (C),A
site 00B67   ; OUTI
site 00B69   ; OUTI
site 00B6B   ; OUTI
site 00B6D   ; OUT (C),A
site 00B6F   ; OUTI
site 00B71   ; OUTI
site 00B73   ; OUTI
site 00B75   ; OUT (C),A
site 00B77   ; OUTI
site 00B79   ; OUTI
site 00B7B   ; OUTI
site 00B7D   ; OUT (C),A
site 00B7F   ; OUTI
site 00B81   ; OUTI
site 00B83   ; OUTI
site 00B85   ; OUT (C),A
site 00B87   ; OUTI
site 00B89   ; OUTI
site 00B8B   ; OUTI
site 00B8D   ; OUT (C),A
site 00B8F   ; OUTI
site 00B91   ; OUTI
site 00B93   ; OUTI
site 00B95   ; OUT (C),A
site 00B97   ; OUTI
site 00B99   ; OUTI
site 00B9B   ; OUTI
site 00B9D   ; OUT (C),A
site 00B9F   ; OUTI
site 00BA1   ; OUTI
site 00BA3   ; OUTI
site 00BA5   ; OUT (C),A
site 00BA7   ; OUTI
site 00BA9   ; OUTI
site 00BAB   ; OUTI
site 00BAD   ; OUT (C),A
site 00BAF   ; OUTI
site 00BB1   ; OUTI
site 00BB3   ; OUTI
site 00BB5   ; OUT (C),A
site 00BB7   ; OUTI
site 00BB9   ; OUTI
site 00BBB   ; OUTI
site 00BBD   ; OUT (C),A
site 00BBF   ; OUTI
site 00BC1   ; OUTI
site 00BC3   ; OUTI
site 00BC5   ; OUT (C),A
site 00BC7   ; OUTI
site 00BC9   ; OUTI
site 00BCB   ; OUTI
site 00BCD   ; OUT (C),A
site 00BCF   ; OUTI
site 00BD1   ; OUTI
site 00BD3   ; OUTI
site 00BD5   ; OUT (C),A
site 00BD7   ; OUTI
site 00BD9   ; OUTI
site 00BDB   ; OUTI
site 00BDD   ; OUT (C),A
site 00BDF   ; OUTI
site 00BE1   ; OUTI
site 00BE3   ; OUTI
site 00BE5   ; OUT (C),A
site 00BE7   ; OUTI
site 00BE9   ; OUTI
site 00BEB   ; OUTI
site 00BED   ; OUT (C),A
site 00BEF   ; OUTI
site 00BF1   ; OUTI
site 00BF3   ; OUTI
site 00BF5   ; OUT (C),A
site 00BF7   ; OUTI
site 00BF9   ; OUTI
site 00BFB   ; OUTI
site 00BFD   ; OUT (C),A
site 00BFF   ; OUTI
site 00C01   ; OUTI
site 00C03   ; OUTI
site 00C05   ; OUT (C),A
site 00C07   ; OUTI
site 00C09   ; OUTI
site 00C0B   ; OUTI
site 00C0D   ; OUT (C),A
site 00C0F   ; OUTI
site 00C11   ; OUTI
site 00C13   ; OUTI
site 00C15   ; OUT (C),A
site 00C17   ; OUTI
site 00C19   ; OUTI
site 00C1B   ; OUTI
site 00C1D   ; OUT (C),A
site 00C1F   ; OUTI
site 00C21   ; OUTI
site 00C23   ; OUTI
site 00C25   ; OUT (C),A
site 00C27   ; OUTI
site 00C29   ; OUTI
site 00C2B   ; OUTI
site 00C2D   ; OUT (C),A
site 00C2F   ; OUTI
site 00C31   ; OUTI
site 00C33   ; OUTI
site 00C35   ; OUT (C),A
site 00C37   ; OUTI
site 00C39   ; OUTI
site 00C3B   ; OUTI
site 00C3D   ; OUT (C),A
site 00C3F   ; OUTI
site 00C41   ; OUTI
site 00C43   ; OUTI
site 00C45   ; OUT (C),A
site 00C47   ; OUTI
site 00C49   ; OUTI
site 00C4B   ; OUTI
site 00C4D   ; OUT (C),A
site 00C4F   ; OUTI
site 00C51   ; OUTI
site 00C53   ; OUTI
site 00C55   ; OUT (C),A
site 00C57   ; OUTI
site 00C59   ; OUTI
site 00C5B   ; OUTI
site 00C5D   ; OUT (C),A
site 00C5F   ; OUTI
site 00C61   ; OUTI
site 00C63   ; OUTI
site 00C65   ; OUT (C),A
site 00C67   ; OUTI
site 00C69   ; OUTI
site 00C6B   ; OUTI
site 00C6D   ; OUT (C),A
site 00C6F   ; OUTI
site 00C71   ; OUTI
site 00C73   ; OUTI
site 00C75   ; OUT (C),A
site 00C77   ; OUTI
site 00C79   ; OUTI
site 00C7B   ; OUTI
site 00C7D   ; OUT (C),A
site 00C7F   ; OUTI
site 00C81   ; OUTI
site 00C83   ; OUTI
site 00C85   ; OUT (C),A
site 00C87   ; OUTI
site 00C89   ; OUTI
site 00C8B   ; OUTI
site 00C8D   ; OUT (C),A
site 00C8F   ; OUTI
site 00C91   ; OUTI
site 00C93   ; OUTI
site 00C95   ; OUT (C),A
site 00C97   ; OUTI
site 00C99   ; OUTI
site 00C9B   ; OUTI
site 00C9D   ; OUT (C),A
site 00C9F   ; OUTI
site 00CA1   ; OUTI
site 00CA3   ; OUTI
site 00CA5   ; OUT (C),A
site 00CA7   ; OUTI
site 00CA9   ; OUTI
site 00CAB   ; OUTI
site 00CAD   ; OUT (C),A
site 00CAF   ; OUTI
site 00CB1   ; OUTI
site 00CB3   ; OUTI
site 00CB5   ; OUT (C),A
site 00CB7   ; OUTI
site 00CB9   ; OUTI
site 00CBB   ; OUTI
site 00CBD   ; OUT (C),A
site 00CBF   ; OUTI
site 00CC1   ; OUTI
site 00CC3   ; OUTI
site 00CC5   ; OUT (C),A
site 00CC7   ; OUTI
site 00CC9   ; OUTI
site 00CCB   ; OUTI
site 00CCD   ; OUT (C),A
site 00CCF   ; OUTI
site 00CD1   ; OUTI
site 00CD3   ; OUTI
site 00CD5   ; OUT (C),A
site 00CD7   ; OUTI
site 00CD9   ; OUTI
site 00CDB   ; OUTI
site 00CDD   ; OUT (C),A
site 00CDF   ; OUTI
site 00CE1   ; OUTI
site 00CE3   ; OUTI
site 00CE5   ; OUT (C),A
site 00CE7   ; OUTI
site 00CE9   ; OUTI
site 00CEB   ; OUTI
site 00CED   ; OUT (C),A
site 00CEF   ; OUTI
site 00CF1   ; OUTI
site 00CF3   ; OUTI
site 00CF5   ; OUT (C),A
site 00CF7   ; OUTI
site 00CF9   ; OUTI
site 00CFB   ; OUTI
site 00CFD   ; OUT (C),A
site 00CFF   ; OUTI
site 00D01   ; OUTI
site 00D03   ; OUTI
site 00D05   ; OUT (C),A
site 00D07   ; OUTI
site 00D09   ; OUTI
site 00D0B   ; OUTI
site 00D0D   ; OUT (C),A
site 00D0F   ; OUTI
site 00D11   ; OUTI
site 00D13   ; OUTI
site 00D15   ; OUT (C),A
site 00D17   ; OUTI
site 00D19   ; OUTI
site 00D1B   ; OUTI
site 00D1D   ; OUT (C),A
site 00D1F   ; OUTI
site 00D21   ; OUTI
site 00D23   ; OUTI
site 00D25   ; OUT (C),A
site 00D27   ; OUTI
site 00D29   ; OUTI
site 00D2B   ; OUTI
site 00D2D   ; OUT (C),A
site 00D2F   ; OUTI
site 00D31   ; OUTI
site 00D33   ; OUTI
site 00D35   ; OUT (C),A
site 00D37   ; OUTI
site 00D39   ; OUTI
site 00D3B   ; OUTI
site 00D3D   ; OUT (C),A
site 00D3F   ; OUTI
site 00D41   ; OUTI
site 00D43   ; OUTI
site 00D45   ; OUT (C),A
site 00D47   ; OUTI
site 00D49   ; OUTI
site 00D4B   ; OUTI
site 00D4D   ; OUT (C),A
site 00D4F   ; OUTI
site 00D51   ; OUTI
site 00D53   ; OUTI
site 00D55   ; OUT (C),A
site 00D57   ; OUTI
site 00D59   ; OUTI
site 00D5B   ; OUTI
site 00D5D   ; OUT (C),A
site 00D5F   ; OUTI
site 00D61   ; OUTI
site 00D63   ; OUTI
site 00D65   ; OUT (C),A
site 00D67   ; OUTI
site 00D69   ; OUTI
site 00D6B   ; OUTI
site 00D6D   ; OUT (C),A
site 00D6F   ; OUTI
site 00D71   ; OUTI
site 00D73   ; OUTI
site 00D75   ; OUT (C),A
site 00D77   ; OUTI
site 00D79   ; OUTI
site 00D7B   ; OUTI
site 00D7D   ; OUT (C),A
site 00D7F   ; OUTI
site 00D81   ; OUTI
site 00D83   ; OUTI
site 00D85   ; OUT (C),A
site 00D87   ; OUTI
site 00D89   ; OUTI
site 00D8B   ; OUTI
site 00D8D   ; OUT (C),A
site 00D8F   ; OUTI
site 00D91   ; OUTI
site 00D93   ; OUTI
site 00D95   ; OUT (C),A
site 00D97   ; OUTI
site 00D99   ; OUTI
site 00D9B   ; OUTI
site 00D9D   ; OUT (C),A
site 00D9F   ; OUTI
site 00DA1   ; OUTI
site 00DA3   ; OUTI
site 00DA5   ; OUT (C),A
site 00DA7   ; OUTI
site 00DA9   ; OUTI
site 00DAB   ; OUTI
site 00DAD   ; OUT (C),A
site 00DAF   ; OUTI
site 00DB1   ; OUTI
site 00DB3   ; OUTI
site 00DB5   ; OUT (C),A
site 00DB7   ; OUTI
site 00DB9   ; OUTI
site 00DBB   ; OUTI
site 00DBD   ; OUT (C),A
site 00DBF   ; OUTI
site 00DC1   ; OUTI
site 00DC3   ; OUTI
site 00DC5   ; OUT (C),A
site 00DC7   ; OUTI
site 00DC9   ; OUTI
site 00DCB   ; OUTI
site 00DCD   ; OUT (C),A
site 00DCF   ; OUTI
site 00DD1   ; OUTI
site 00DD3   ; OUTI
site 00DD5   ; OUT (C),A
site 00DD7   ; OUTI
site 00DD9   ; OUTI
site 00DDB   ; OUTI
site 00DDD   ; OUT (C),A
site 00DDF   ; OUTI
site 00DE1   ; OUTI
site 00DE3   ; OUTI
site 00DE5   ; OUT (C),A
site 00DE7   ; OUTI
site 00DE9   ; OUTI
site 00DEB   ; OUTI
site 00DED   ; OUT (C),A
site 00DEF   ; OUTI
site 00DF1   ; OUTI
site 00DF3   ; OUTI
site 00DF5   ; OUT (C),A
site 00DF7   ; OUTI
site 00DF9   ; OUTI
site 00DFB   ; OUTI
site 00DFD   ; OUT (C),A
site 00DFF   ; OUTI
site 00E01   ; OUTI
site 00E03   ; OUTI
site 00E05   ; OUT (C),A
site 00E07   ; OUTI
site 00E09   ; OUTI
site 00E0B   ; OUTI
site 00E0D   ; OUT (C),A
site 00E0F   ; OUTI
site 00E11   ; OUTI
site 00E13   ; OUTI
site 00E15   ; OUT (C),A
site 00E17   ; OUTI
site 00E19   ; OUTI
site 00E1B   ; OUTI
site 00E1D   ; OUT (C),A
site 00E1F   ; OUTI
site 00E21   ; OUTI
site 00E23   ; OUTI
site 00E25   ; OUT (C),A
site 00E27   ; OUTI
site 00E29   ; OUTI
site 00E2B   ; OUTI
site 00E2D   ; OUT (C),A
site 00E2F   ; OUTI
site 00E31   ; OUTI
site 00E33   ; OUTI
site 00E35   ; OUT (C),A
site 00E37   ; OUTI
site 00E39   ; OUTI
site 00E3B   ; OUTI
site 00E3D   ; OUT (C),A
site 00E3F   ; OUTI
site 00E41   ; OUTI
site 00E43   ; OUTI
site 00E45   ; OUT (C),A
site 00E47   ; OUTI
site 00E49   ; OUTI
site 00E4B   ; OUTI
site 00E4D   ; OUT (C),A
site 00E4F   ; OUTI
site 00E51   ; OUTI
site 00E53   ; OUTI
site 00E55   ; OUT (C),A
site 00E57   ; OUTI
site 00E59   ; OUTI
site 00E5B   ; OUTI
site 00E5D   ; OUT (C),A
site 00E5F   ; OUTI
site 00E61   ; OUTI
site 00E63   ; OUTI
site 00E65   ; OUT (C),A
site 00E67   ; OUTI
site 00E69   ; OUTI
site 00E6B   ; OUTI
site 00E6D   ; OUT (C),A
site 00E6F   ; OUTI
site 00E71   ; OUTI
site 00E73   ; OUTI
site 00E75   ; OUT (C),A
site 00E77   ; OUTI
site 00E79   ; OUTI
site 00E7B   ; OUTI
site 00E7D   ; OUT (C),A
site 00E7F   ; OUTI
site 00E81   ; OUTI
site 00E83   ; OUTI
site 00E85   ; OUT (C),A
site 00E87   ; OUTI
site 00E89   ; OUTI
site 00E8B   ; OUTI
site 00E8D   ; OUT (C),A
site 00E90   ; OUTI
site 00E92   ; OUT (C),A
site 00E94   ; OUTI
site 00E96   ; OUT (C),A
site 00E98   ; OUTI
site 00E9A   ; OUT (C),A
site 00E9C   ; OUTI
site 00E9E   ; OUT (C),A
site 00EA0   ; OUTI
site 00EA2   ; OUT (C),A
site 00EA4   ; OUTI
site 00EA6   ; OUT (C),A
site 00EA8   ; OUTI
site 00EAA   ; OUT (C),A
site 00EAC   ; OUTI
site 00EAE   ; OUT (C),A
site 00EB0   ; OUTI
site 00EB2   ; OUT (C),A
site 00EB4   ; OUTI
site 00EB6   ; OUT (C),A
site 00EB8   ; OUTI
site 00EBA   ; OUT (C),A
site 00EBC   ; OUTI
site 00EBE   ; OUT (C),A
site 00EC0   ; OUTI
site 00EC2   ; OUT (C),A
mapldk 00089   # LD HL,$FFFC; LD (HL),$80
maphl 0008F   # LD (HL),$00, HL = $FFFD
maphl 00092   # LD (HL),$01, HL = $FFFE
maphl 00095   # LD (HL),$02, HL = $FFFF
mapst 000AF   ; LD ($FFFF),A
mapst 0012E   ; LD ($FFFF),A
mapst 00140   ; LD ($FFFF),A
mapst 00159   ; LD ($FFFF),A
mapst 001E5   ; LD ($FFFF),A
mapst 01172   ; LD ($FFFF),A
mapst 01184   ; LD ($FFFF),A
mapst 011B1   ; LD ($FFFF),A
mapst 0126B   ; LD ($FFFF),A
mapst 0139B   ; LD ($FFFF),A
mapst 013C3   ; LD ($FFFF),A
mapst 0140A   ; LD ($FFFF),A
mapst 01451   ; LD ($FFFF),A
mapst 01498   ; LD ($FFFF),A
mapst 014DF   ; LD ($FFFF),A
mapst 015C5   ; LD ($FFFF),A
mapst 01762   ; LD ($FFFF),A
mapst 0176F   ; LD ($FFFF),A
mapst 017FC   ; LD ($FFFF),A
mapst 022C1   ; LD ($FFFF),A
mapst 02944   ; LD ($FFFF),A
mapst 029FF   ; LD ($FFFF),A
mapst 02ABE   ; LD ($FFFF),A
mapst 02AC6   ; LD ($FFFF),A
mapst 02B77   ; LD ($FFFF),A
mapst 02C19   ; LD ($FFFF),A
mapst 02CC5   ; LD ($FFFF),A
mapst 02D02   ; LD ($FFFF),A
mapst 031C0   ; LD ($FFFF),A
mapst 03226   ; LD ($FFFF),A
mapst 0322E   ; LD ($FFFF),A
mapst 07B57   ; LD ($FFFF),A
mapst 07B6A   ; LD ($FFFF),A
mapst 07BAA   ; LD ($FFFF),A
mapst 07BB8   ; LD ($FFFF),A
mapst 07CEC   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 017CE   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 02685   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 032EF   # LD ($FFFF),A; after LD ($C01A),A; 32 bytes of valid code before it
mapst 07C0D   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 07C91   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 07D32   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 07D40   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
# HALT patches.
eihalt 001CC   ; EI; HALT
eihalt 001FC   ; EI; HALT
eihalt 017F2   ; EI; HALT
eihalt 07D14   ; EI; HALT
label cave_17c2 07F20
label cave_184f 07F30
label cave_3117 07F40
asm 017C2 5    ; HALT; DI; LD DE,$7F00
    jp cave_17c2
endasm
asm 0184F 4    ; HALT; DI; LD A,$02
    jp cave_184f
endasm
asm 03117 3    ; HALT; HALT; RET
    jp cave_3117
endasm
asm 07F20 9    ; unused $FF bytes: cave for the HALT at $17C2
    rst $30
    db halt_io
    di
    ld de,$7F00
    jp $17C7
endasm
asm 07F30 8    ; unused $FF bytes: cave for the HALT at $184F
    rst $30
    db halt_io
    di
    ld a,$02
    jp $1853
endasm
asm 07F40 4    ; unused $FF bytes: cave for the HALTs at $3117
    rst $30
    db halt_io
    rst $30
    db haltret_io
endasm
# Step rate. The game runs one step of its logic per pass of the state routine at $1214,
# then waits at $1230 (or at $30C7 or $30FB, in the mode that $C030 selects) until the
# frame handler has sent the step's four upload frames ($C002 = 4). A Master System
# cannot finish the logic in those four frames: in the attract demo and stage 1 a step
# takes 5 to 8 frames there, more when more is on screen. The Next finishes it sooner and
# would play up to half as fast again. Page 0 times the logic of each step on the Next in
# Next lines, without the game's frame handler (marks at the handler's start $0120 and
# end $0131), turns the lines into Master System cycles, adds the frame handler's own
# Master System cycles frame by frame, and holds the step until as many frame events have
# passed as a Master System would need: an NTSC one at 60 Hz, a PAL one at 50 Hz. The
# constants come from steps paired with the reference (sg1000m3): the attract demo and
# stage 1 play.
label cave_irqend 07F50
label cave_irqbeg 07F68
asm 00120 3    ; LD HL,$C011: the frame handler's start time goes through the cave
    jp cave_irqbeg
endasm
asm 07F68 10   ; unused $FF bytes: the handler's start time, then LD HL,$C011
    rst $30
    db far_io, pg_gax_in, ent_gax_in
    ld hl,$C011
    jp $0123
endasm
asm 01214 4    ; LD A,($C030); OR A: a step starts
    rst $30
    db far_io, pg_gax_start, ent_gax_start
endasm
asm 01230 10   ; the wait for $C002 = 4: also waits for the Master System's frames
    rst $30
    db far_io, pg_gax_ready, ent_gax_ready
    jr c,$123A
    halt
    jr $1230
    nop
endasm
asm 030C7 10   ; the same wait in the steps of the other mode ($C030 not 0, from $1218)
    rst $30
    db far_io, pg_gax_ready, ent_gax_ready
    jr c,$30D1
    halt
    jr $30C7
    nop
endasm
asm 030FB 10   ; and again
    rst $30
    db far_io, pg_gax_ready, ent_gax_ready
    jr c,$3105
    halt
    jr $30FB
    nop
endasm
asm 00131 3    ; LD A,($C007): the end of the frame handler's work goes through the cave
    jp cave_irqend
endasm
asm 07F50 21   ; unused $FF bytes: the sound call of $0131-$013E, then the handler's end time
    ld a,($C007)
    or a
    jr z,1f
    call $86C8
    jr 2f
1:  call $8007
2:  rst $30
    db far_io, pg_gax_irq, ent_gax_irq
    jp $013F
endasm
page 0 gax_start gax_ready gax_irq gax_in
; Times the logic of each game step and holds the step at the Master System's rate.
; Uses no runtime internals: NextRegs $05, $1E and $1F through ports $243B/$253B, and
; isr_n. Works on a stack of its own in this page, with interrupts off.
RATIO   equ 620             ; Master System cycles per Next line of the game's logic
OFF50   equ 32000*16/RATIO  ; and a step's Master System cycles that the lines miss, at 50 Hz
OFF60   equ 64000*16/RATIO  ; at 60 Hz
EVK     equ 3               ; Next lines from the frame event to gax_in
CMAX    equ 2000            ; the most logic lines counted
FR60    equ 59736*16/RATIO  ; an NTSC Master System frame, in 1/16 Next lines of logic
FR50    equ 71364*16/RATIO  ; a PAL one
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
; seg: HL = (HL - DE) modulo the frame's lines.
seg:
        or a
        sbc hl,de
        ret nc
        ld de,(lpf)
        add hl,de
        ret
; gax_start: at $1214. Returns A = ($C030) with the flags of OR A, as the game's code.
gax_start:
        ld a,i              ; P/V = the interrupt state
        di
        ld (sv_sp),sp
        ld sp,stk_top
        push af
        push bc
        push de
        push hl
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld hl,311
        ld de,FR50
        bit 2,a
        jr z,1f
        ld hl,264
        ld de,FR60
1:      ld (lpf),hl
        ld (fr),de
        ld hl,OFF50
        jr z,3f
        ld hl,OFF60
3:      ld (off),hl
        call rd_line
        ld (last),hl
        ld hl,0
        ld (cacc),hl
        ld a,(isr_n)
        ld (s0),a
        ld a,1
        ld (active),a
        xor a
        ld (frames),a
        pop hl
        pop de
        pop bc
        pop af
        ld sp,(sv_sp)
        jp po,2f
        ld a,($C030)
        or a
        ei
        ret
2:      ld a,($C030)
        or a
        ret
; gax_in: at the start of the game's frame handler ($0120), interrupts off. The logic
; ran from the last mark to the frame event, which came EVK lines before this point.
; Keeps A.
gax_in:
        ld (sv_a),a
        ld a,(active)
        or a
        jr z,2f
        ld (sv_sp),sp
        ld sp,stk_top
        call rd_line
        ld de,(last)
        call seg
        ld de,EVK
        or a
        sbc hl,de
        jr nc,1f
        ld hl,0
1:      ld de,(cacc)
        add hl,de
        ld (cacc),hl
        ld sp,(sv_sp)
2:      ld a,(sv_a)
        ret
; gax_irq: at the end of the game's frame handler ($0131), interrupts off. The logic
; goes on from now.
gax_irq:
        ld a,(active)
        or a
        ret z
        ld (sv_sp),sp
        ld sp,stk_top
        call rd_line
        ld (last),hl
        ld sp,(sv_sp)
        ret
; gax_ready: at $1230, $30C7 and $30FB, in the game's wait loops. The first call ends
; the step's logic and works out the frames a Master System takes for the step.
; Returns carry set when the step may end: $C002 >= 4 and that many frame events
; since the step started.
gax_ready:
        ld a,i
        di
        ld (sv_sp),sp
        ld sp,stk_top
        push af
        push bc
        push de
        push hl
        ld a,(active)
        or a
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
1:      ld (cacc),hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,(utab)
        add hl,de
        ld de,(off)
        add hl,de
        ex de,hl            ; DE = Master System time from the first frame event
        ld hl,(fr)          ; HL = the end of the frame it is in
        ld b,0              ; B = frame events after the first
2:      ld a,e
        sub l
        ld a,d
        sbc a,h
        jr c,3f
        inc b
        push hl
        ld a,b
        cp 7
        jr c,5f
        ld a,7
5:      add a,a
        ld l,a
        ld h,0
        push de
        ld de,utab
        add hl,de
        ld e,(hl)
        inc hl
        ld d,(hl)
        ex de,hl
        pop de
        add hl,de
        ex de,hl            ; DE += the frame handler's time in that frame
        pop hl
        push de
        ld de,(fr)
        add hl,de
        pop de
        ld a,b
        cp 30
        jr c,2b
3:      ld a,b
        cp 3
        jr nc,6f
        ld a,3
6:      ld (frames),a
4:      ld a,(isr_n)
        ld hl,s0
        sub (hl)
        ld hl,frames
        cp (hl)
        ld a,0
        jr c,7f
        ld a,($C002)
        cp 4
        ld a,0
        jr c,7f
        inc a
7:      ld (rdy),a
        pop hl
        pop de
        pop bc
        pop af
        ld sp,(sv_sp)
        jp po,8f
        ld a,(rdy)
        rrca
        ei
        ret
8:      ld a,(rdy)
        rrca
        ret
; The frame handler's time on a Master System in each frame of a step, in 1/16 Next
; lines of logic: the first frame event (the upload of $C002 = 0), the next three
; uploads, then the sound alone (measured in the attract demo, sg1000m3).
utab:   dw 46057*16/RATIO, 51529*16/RATIO, 37327*16/RATIO, 2838*16/RATIO
        dw 2948*16/RATIO, 2000*16/RATIO, 2000*16/RATIO, 2000*16/RATIO
active: db 0
frames: db 0
rdy:    db 0
s0:     db 0
last:   dw 0
cacc:   dw 0
lpf:    dw 311
fr:     dw FR50
off:    dw OFF50
sv_sp:  dw 0
sv_a:   db 0
stk:    ds 64
stk_top:
endpage

# Golden Axe (USA, Europe, Brazil).cht, "Infinite Lives": RAM $C005 is the lives count of
# player 1 and $C045 of player 2 (P2 slot not run). Held at 1, the game never ends
poke "Infinite lives"
ar 00C0-0501
ar 00C0-4501
endpoke

# Golden Axe (USA, Europe, Brazil).cht, "Infinite Energy": RAM $C187 is the energy of
# player 1, $1F when full
poke "Infinite energy"
ar 00C1-871F
endpoke

# Golden Axe (USA, Europe, Brazil).cht, "Invincibility": the cart byte at $244C is $77
# (LD (HL),A), the store of the new energy at $C187; $C9 (RET) skips it
poke "Invincibility"
gg C94-4CD-3B7
endpoke

# Golden Axe (USA, Europe, Brazil).cht, "Infinite Magic": RAM $C006 is the magic of
# player 1, which a spell uses up; held at 1, every spell can be cast again
poke "Infinite magic"
ar 00C0-0601
endpoke

# Golden Axe (USA, Europe, Brazil).cht, "Infinite Continues": RAM $C015 is the number of
# continues used; held at 0, the game never counts them out
poke "Infinite continues"
ar 00C0-1500
endpoke

# Golden Axe (USA, Europe, Brazil).cht, "Hit Anywhere": the cart byte at $251B is $CD (CALL
# $258F); $3A (LD A,(nn)) removes the call. Enemies fell without being in sword range
poke "Hit anywhere"
gg 3A5-1BD-D5D
endpoke

# Golden Axe (USA, Europe, Brazil).cht, "One Hit Kills": the cart byte at $2569 is $F8
# (RET M); $C9 (RET) always returns. Enemies died on the first hit
poke "One hit kills"
gg C95-69D-089
endpoke
