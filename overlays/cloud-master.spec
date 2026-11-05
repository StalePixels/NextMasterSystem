# Cloud Master (USA, Europe, Brazil) (En), CRC32 E7F62E6D, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of random
# input, 120 s with no input); the logs ran no I/O or mapper site that the scan did not find.
# Decisions:
# - $0010, $0018, $0028 and $0030 hold a RET and $0020 a VDP address routine, so $0000
#   is the io vector.
# - The sites marked "unreached library routine" are in VDP, joypad and interrupt routines
#   of bank 0 that no scanned path or recording reaches. They are code, so they are patched.
# - The three calls into slot 2 with an unknown bank ($0152, $0198, $01A2) go to the sound
#   driver in bank 2; the reference logs ran every slot 2 I/O instruction from bank 2, and
#   the scan covers the driver.
# - No tilecache: the tile loads in play go through the byte loop at $028F, which the switch
#   does not cover; it gave no gain in a measured run.
name Cloud Master
cart E7F62E6D
hz any		; No-Intro regions USA, Europe, Brazil
vector 00 io
start 0003
site 00073   ; IN A,($BF)
site 00077   ; OUT ($DE),A
site 00079   ; IN A,($DC)
site 0007B   ; IN A,($DD)
site 000AE   ; OUT ($BF),A
site 000B2   ; OUT ($BF),A
site 001AA   ; OUT ($F2),A
site 001AC   ; OUT ($F2),A
site 001B9   ; OUT ($F2),A
site 001C3   ; OUT ($3F),A
site 001C5   ; IN A,($DD)
site 001CF   ; OUT ($3F),A
site 001D1   ; IN A,($DD)
site 001D9   ; OUT ($3F),A
site 001E5   ; OUT ($3E),A
site 001ED   ; OUT ($F2),A
site 001F0   ; IN A,($F2)
site 00202   ; OUT ($F2),A
site 0020A   ; OUT ($3E),A
site 0020D   ; IN A,($BF)
site 00212   ; OUT ($BF),A
site 00217   ; OUT ($BF),A
site 0023A   ; OUT ($BF),A
site 0023F   ; OUT ($BF),A
site 00244   ; OUT ($BE),A
site 0024A   ; OUT ($BF),A
site 0024F   ; OUT ($BF),A
site 00254   ; OUT ($BE),A
site 0025D   ; OUT ($BE),A
site 00286   ; OUT ($BF),A
site 0028B   ; OUT ($BF),A
site 00290   ; OUT ($BE),A
site 002C6   ; OUT ($BF),A
site 002CB   ; OUT ($BF),A
site 002D2   ; OUT (C),B
site 002DD   ; OUT ($BF),A
site 002E2   ; OUT ($BF),A
site 002E7   ; OUT ($BE),A
site 002ED   ; OUT ($BE),A
site 00307   ; OUT ($BF),A
site 0030B   ; OUT ($BF),A
site 0033A   ; OUT ($BF),A
site 00340   ; OUT ($BF),A
site 003FA   ; OUT ($DE),A
site 003FC   ; IN A,($DC)
site 00403   ; IN A,($DD)
site 00412   ; OUT ($DE),A
site 00414   ; IN A,($DC)
site 00422   ; IN A,($DD)
site 00558   ; OUT ($BF),A
site 0055C   ; OUT ($BF),A
site 00561   ; OUT ($BE),A
site 00567   ; OUT ($BF),A
site 0056B   ; OUT ($BF),A
site 00572   ; OTIR
site 0059E   ; OUT ($BF),A
site 005A2   ; OUT ($BF),A
site 005A8   ; OTIR
site 0065F   ; OUT ($BF),A
site 00664   ; OUT ($BF),A
site 0067D   ; OTIR
site 0068F   ; OTIR
site 00715   ; OUT ($BF),A
site 00719   ; OUT ($BF),A
site 0072A   ; OTIR
site 0072E   ; OUT ($BF),A
site 00732   ; OUT ($BF),A
site 00738   ; OTIR
site 00772   ; OUTI
site 00774   ; OUTI
site 00787   ; OTIR
site 0078D   ; OTIR
site 0083E   ; OUT ($BF),A
site 00843   ; OUT ($BF),A
site 00847   ; OUT (C),L
site 0084E   ; OUT (C),H
site 00855   ; OUT (C),L
site 0085C   ; OUT (C),H
site 00867   ; OUT ($BF),A
site 0086C   ; OUT ($BF),A
site 00871   ; OUT (C),L
site 00878   ; OUT (C),H
site 0087F   ; OUT (C),L
site 00886   ; OUT (C),H
site 0088C   ; OUT ($BF),A
site 00891   ; OUT ($BF),A
site 0089B   ; OUT (C),L
site 0089D   ; OUT (C),H
site 008A0   ; OUT (C),L
site 008A2   ; OUT (C),H
site 008AB   ; OUT ($BF),A
site 008B0   ; OUT ($BF),A
site 008B5   ; OUT (C),L
site 008B7   ; OUT (C),H
site 008BA   ; OUT (C),L
site 008BC   ; OUT (C),H
site 008CE   ; OUT ($BF),A
site 008D3   ; OUT ($BF),A
site 008D7   ; OUT (C),L
site 008DD   ; OUT (C),H
site 008E7   ; OUT ($BF),A
site 008EC   ; OUT ($BF),A
site 008F1   ; OUT (C),L
site 008F7   ; OUT (C),H
site 0812D   ; OUT ($F0),A
site 08136   ; OUT ($F1),A
site 0814E   ; OUT ($7F),A
site 0815E   ; OUT (C),D
site 08164   ; OUT ($F1),A
site 08186   ; OUT ($7F),A
site 0818A   ; OUT ($7F),A
site 081B8   ; OTIR
site 081C6   ; OTIR
site 081D0   ; OUT ($F0),A
site 081D6   ; OUT ($F1),A
site 081E2   ; OUTI
site 081E8   ; OUTI
site 0832E   ; OUT ($7F),A
site 08332   ; OUT ($7F),A
site 083C2   ; OUT ($7F),A
site 083C6   ; OUT ($7F),A
site 083EE   ; OUT ($7F),A
site 083F2   ; OUT ($7F),A
site 083F6   ; OUT ($7F),A
site 083FA   ; OUT ($7F),A
site 083FD   ; OUT ($7F),A
site 08463   ; OUT ($F0),A
site 0846A   ; OUT ($F1),A
site 08472   ; OUT ($F0),A
site 08478   ; OUT ($F1),A
site 0856D   ; OUT ($F0),A
site 08577   ; OUT (C),L
site 08580   ; OUT ($F0),A
site 0859B   ; OUT (C),H
site 085A3   ; OUT ($F0),A
site 085B1   ; OUT ($F1),A
site 085BD   ; OUT ($F0),A
site 085C6   ; OUT ($F1),A
site 08787   ; OUT ($F0),A
site 08790   ; OUT (C),A
site 08795   ; OUT ($F0),A
site 0879B   ; OUTI
site 0880C   ; OUT ($7F),A
site 088D9   ; OUT ($7F),A
site 08900   ; OUT ($7F),A
site 08905   ; OUT ($7F),A
site 08931   ; OUT ($F0),A
site 0893F   ; OUT ($F1),A
site 0894D   ; OUT ($F0),A
site 089E4   ; OUTI
site 089E6   ; OUTI
site 089E8   ; OUTI
site 089EA   ; OUTI
site 089EC   ; OUTI
site 089EE   ; OUTI
site 089F0   ; OUTI
site 089F2   ; OUTI
site 089F4   ; OUTI
site 089F6   ; OUTI
site 089F8   ; OUTI
site 08A02   ; OUT (C),D
site 08A08   ; OUT ($F1),A
site 08A47   ; OUT ($7F),A
site 08A9D   ; OUT ($7F),A
site 08ADC   ; OUT ($7F),A
site 08B3E   ; OUT ($7F),A
site 08B5E   ; OUT ($7F),A
site 08B9E   ; OUT ($7F),A
site 08BA8   ; OUT ($7F),A
site 08BF0   ; OUT ($7F),A
mapst 000B6   ; LD ($FFFF),A
mapst 000BF   ; LD ($FFFF),A
mapst 00101   ; LD ($FFFD),A
mapst 0010B   ; LD ($FFFE),A
mapst 00115   ; LD ($FFFF),A
mapst 0011F   ; LD ($FFFC),A
mapst 0016D   ; LD ($FFFF),A
mapst 00185   ; LD ($FFFF),A
mapst 00751   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00179   # LD ($FFFF),A; after LD ($C00D),A; 32 bytes of valid code before it
# CHECK byte scan low: mapst 1A63D  LD ($FFFF),A  (no valid code after it)
# CHECK byte scan low: mapsthl 1C3FB  LD ($FFFE),HL  (no valid code after it)
# CHECK byte scan low: mapsthl 1CFBA  LD ($FFFD),HL  (no evidence)
# CHECK byte scan low: mapsthl 1D46C  LD ($FFFE),HL  (no valid code after it)
site 00021   ; OUT ($BF),A, unreached library routine
site 00024   ; OUT ($BF),A, unreached library routine
site 000D3   ; OUT ($BF),A, unreached library routine
site 000D7   ; OUT ($BF),A, unreached library routine
site 000DB   ; OUT ($BF),A, unreached library routine
site 000DF   ; OUT ($BF),A, unreached library routine
site 00224   ; OUT ($BF),A, unreached library routine
site 0022B   ; OUT ($BF),A, unreached library routine
site 00230   ; OUT ($BF),A, unreached library routine
site 00235   ; OUT ($BF),A, unreached library routine
site 00266   ; IN A,($BE), unreached library routine
site 0026E   ; IN A,($BE), unreached library routine
site 00271   ; OUT ($BE),A, unreached library routine
site 00276   ; OUT ($BF),A, unreached library routine
site 0027B   ; OUT ($BF),A, unreached library routine
site 00282   ; OTIR, unreached library routine
site 0029A   ; OUT ($BF),A, unreached library routine
site 0029F   ; OUT ($BF),A, unreached library routine
site 002AB   ; OTIR, unreached library routine
site 002AF   ; OTIR, unreached library routine
site 002BA   ; IN A,($BE), unreached library routine
site 0031B   ; OUT ($BF),A, unreached library routine
site 0031F   ; OUT ($BF),A, unreached library routine
site 0032C   ; OUT ($BF),A, unreached library routine
site 00330   ; OUT ($BF),A, unreached library routine
site 0038F   ; OUT ($BE),A, unreached library routine
site 003AB   ; OUT ($BE),A, unreached library routine
site 0043A   ; IN A,($DD), unreached library routine
site 00446   ; IN A,($DD), unreached library routine
site 00452   ; IN A,($DC), unreached library routine
site 00464   ; IN A,($DC), unreached library routine
site 00470   ; IN A,($DC), unreached library routine
site 0047E   ; IN A,($DC), unreached library routine
site 0048A   ; IN A,($DC), unreached library routine
site 00496   ; IN A,($DC), unreached library routine
site 004A2   ; IN A,($DC), unreached library routine
site 004AE   ; IN A,($DC), unreached library routine
site 004C0   ; IN A,($DC), unreached library routine
site 004CC   ; IN A,($DC), unreached library routine
site 004D8   ; IN A,($DC), unreached library routine
site 004E4   ; IN A,($DD), unreached library routine
site 006D5   ; OUT ($BF),A, unreached library routine
site 006DA   ; OUT ($BF),A, unreached library routine
site 006F4   ; OUT (C),A, unreached library routine
site 006FD   ; OUT (C),A, unreached library routine
# CHECK low: site 1431E  OUT (C),H  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 1677C  IN A,($3F)  (unmapped_read; 20 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1C5E5  IN A,($BF)  (vdp_status; no evidence)
# CHECK low: site 1D03E  OUT ($3F),A  (io_control; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1D8F6  IN A,($7F)  (h_counter; 4 RST or NOP opcodes around it (looks like data); 15 bytes of valid code before it)
# CHECK low: site 1E63D  INDR  (port in C; no evidence)
# CHECK low: site 1E690  IN A,($C0)  (joypad_a; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 1E8C4  IN A,($C0)  (joypad_a; branch target from $1CDE9 $1D061 $1E8B2; 23 bytes of valid code before it)
# CHECK medium: site 1EB42  IN A,($C0)  (joypad_a; 32 bytes of valid code before it)
# CHECK medium: site 1EC2E  IN A,($C0)  (joypad_a; 32 bytes of valid code before it)
# CHECK low: site 1EF21  IN A,($7F)  (h_counter; 13 RST or NOP opcodes around it (looks like data); 21 bytes of valid code before it)
# CHECK low: site 26FFD  OUT ($7E),A  (psg; 23 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 29ED6  IN A,($F0)  (joypad_a; no valid code after it)
# CHECK low: site 2CEF5  IN A,($3F)  (unmapped_read; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2ECFD  IN A,($3F)  (unmapped_read; no evidence)
# CHECK low: site 310F7  IN A,($3F)  (unmapped_read; no evidence)
# CHECK low: site 31C41  IN A,($3F)  (unmapped_read; 32 bytes of valid code before it; no valid code after it)

# Cloud Master (USA, Europe, Brazil).cht, "Infinite Lives" (3A5-B1E-2A2): the patch at $15B1
# changes the store of the lives counter $C4C9 after its decrement (LD ($C4C9),A) into a load, so a
# lost life no longer lowers it (bank 0)
poke "Infinite lives"
gg 3A5-B1E-2A2
endpoke

# Cloud Master (USA, Europe, Brazil).cht, "Invulnerability" (C37-9CA-E61): the patch at $579C
# changes the conditional jump after an OR A (JP NZ) into JP, and the player then survives hits
# (bank 1)
poke "Invulnerability"
gg C37-9CA-E61
endpoke

# Cloud Master (USA, Europe, Brazil).cht, "Maximum Firepower" (00C4-C307): $C4C3 = $07 gives a three-shot spread
poke "Maximum firepower"
ar 00C4-C307
endpoke

# Cloud Master (USA, Europe, Brazil).cht, "Maximum Speed" (00C4-C405): $C4C4 = $05 gives a faster walk
poke "Maximum speed"
ar 00C4-C405
endpoke

# Cloud Master (USA, Europe, Brazil).cht, "3-Way Special Magic [Button 2]" (00C4-C503): $C4C5
# = $03 gives button 2 a fire spread in several directions
poke "3-way magic"
ar 00C4-C503
endpoke
