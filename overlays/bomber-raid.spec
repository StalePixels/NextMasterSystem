# Bomber Raid (World), CRC32 3084CF11, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output, with the scan entries below, then
# decided by hand.
#
# Decisions:
# - Scan entries 3:8000, 3:805C, 4:8000 and 4:805C: the mission code. $29C2 and $2AE0
#   call $8000 and $805C in slot 2 with the bank from the table at $2C45, indexed by the
#   mission ($C040): $83, $83, $84, $83, $84, so banks 3 and 4. Their I/O sites are
#   patched; the screen fill at the start of a mission ($8243 and $8472) runs through them.
# - The two JP (HL) at $6E73 and $6F6F jump through the tables at $6E74 and $7035, indexed
#   by an object type: $6EB0, $6EC6, $6EFA, $6F29 and $6F70, $6F75, $6F7E, $6F8D. Those
#   routines do no I/O and store no mapper register.
# - The I/O sites at $03B3 (routine $03B3), $0815 and $081A (routine $07D0, reached only
#   from the jump at $00F8), $0AC4-$0AD1 (routine $0A8E) and $4C57-$4C63 (routine $4C22),
#   and the mapper stores at $06FB and $0702 (routine $06F4), are in whole routines of
#   banks 0 and 1 that nothing in the cart names. They are patched all the same.
# - The other byte patterns that no path reached are tile graphics in banks that no code
#   runs from (verdict false).
# - The bank numbers the game writes to $FFFF have bit 7 set ($82-$8B); the runtime
#   takes them modulo the cart size.
name Bomber Raid
cart 3084CF11
hz any		; No-Intro region World
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00045   ; IN A,($BF)
site 0021D   ; OUT ($BF),A
site 00222   ; OUT ($BF),A
site 00232   ; OUT ($BF),A
site 00237   ; OUT ($BF),A
site 0024A   ; OUT ($BF),A
site 0024F   ; OUT ($BF),A
site 00255   ; OUTD
site 00260   ; OUT ($BF),A
site 00265   ; OUT ($BF),A
site 0026B   ; OUTI
site 0026D   ; OUTD
site 00274   ; OUTI
site 00276   ; OUTI
site 00278   ; OUTI
site 0027A   ; OUTI
site 0027C   ; OUTI
site 0027E   ; OUTI
site 00280   ; OUTI
site 00282   ; OUTI
site 00284   ; OUTI
site 00286   ; OUTI
site 00288   ; OUTI
site 0028A   ; OUTI
site 0028C   ; OUTI
site 0028E   ; OUTI
site 00290   ; OUTI
site 00292   ; OUTI
site 00294   ; OUTI
site 00296   ; OUTI
site 00298   ; OUTI
site 0029A   ; OUTI
site 0029C   ; OUTI
site 0029E   ; OUTI
site 002A0   ; OUTI
site 002A2   ; OUTI
site 002A4   ; OUTI
site 002A6   ; OUTI
site 002A8   ; OUTI
site 002AA   ; OUTI
site 002AC   ; OUTI
site 002AE   ; OUTI
site 002B0   ; OUTI
site 002B2   ; OUTI
site 002B4   ; OUTI
site 002B6   ; OUTI
site 002B8   ; OUTI
site 002BA   ; OUTI
site 002BC   ; OUTI
site 002BE   ; OUTI
site 002C0   ; OUTI
site 002C2   ; OUTI
site 002C4   ; OUTI
site 002C6   ; OUTI
site 002C8   ; OUTI
site 002CA   ; OUTI
site 002CC   ; OUTI
site 002CE   ; OUTI
site 002D0   ; OUTI
site 002D2   ; OUTI
site 002D4   ; OUTI
site 002D6   ; OUTI
site 002D8   ; OUTI
site 002DA   ; OUTI
site 002DC   ; OUTI
site 002DE   ; OUTI
site 002E0   ; OUTI
site 002E2   ; OUTI
site 002E4   ; OUTI
site 002E6   ; OUTI
site 002E8   ; OUTI
site 002EA   ; OUTI
site 002EC   ; OUTI
site 002EE   ; OUTI
site 002F0   ; OUTI
site 002F2   ; OUTI
site 002FC   ; OUT ($BF),A
site 00301   ; OUT ($BF),A
otir 0030C   ; OUTI
site 00317   ; IN A,($DD)
site 00343   ; IN A,($BF)
site 003A3   ; OUT ($BF),A
site 003A7   ; OUT ($BF),A
site 003AC   ; OUT ($BF),A
site 003B0   ; OUT ($BF),A
site 003B3   ; IN A,($DC)
site 00424   ; IN A,($DC)
site 00444   ; IN A,($DD)
site 00480   ; OUT ($BF),A
site 00485   ; OUT ($BF),A
site 004D5   ; IN A,($DD)
site 00567   ; IN A,($BF)
otir 00570   ; OUTI
site 00575   ; OUT ($BE),A
site 00592   ; OUT ($3E),A
site 0059A   ; OUT ($F2),A
site 0059D   ; IN A,($F2)
site 005AF   ; OUT ($F2),A
site 005B7   ; OUT ($3E),A
site 005B9   ; IN A,($DC)
site 005C0   ; IN A,($DD)
site 0078F   ; OUT ($BF),A
site 00792   ; OUT ($BF),A
site 00796   ; OUT ($BF),A
site 0079B   ; OUT ($BF),A
site 007A3   ; OUT ($BE),A
site 007A8   ; OUT ($BE),A
site 007BE   ; OUTI
site 007C2   ; OUT (C),A
site 00815   ; OUT ($BE),A
site 0081A   ; OUT ($BE),A
site 00870   ; OUT ($BE),A
site 00877   ; OUT ($BE),A
otir 0096E   ; OUTI
site 00988   ; OUT ($BE),A
site 009B5   ; OUT ($BF),A
site 009BA   ; OUT ($BF),A
site 009BD   ; OUT ($BE),A
site 009C3   ; OUT ($BE),A
site 009D0   ; OUT ($BF),A
site 009D5   ; OUT ($BF),A
site 00AC4   ; OUT ($BF),A
site 00AC9   ; OUT ($BF),A
site 00AD1   ; IN A,($BE)
site 01815   ; OUT ($3F),A
site 01817   ; IN A,($DD)
site 01821   ; OUT ($3F),A
site 01823   ; IN A,($DD)
site 01837   ; IN A,($BF)
site 01868   ; IN A,($BF)
site 01D9B   ; IN A,($BF)
site 01E1F   ; IN A,($BF)
site 0201F   ; IN A,($BF)
site 020A5   ; IN A,($BF)
site 02145   ; IN A,($BF)
site 02236   ; IN A,($BF)
site 022AD   ; IN A,($BF)
site 02325   ; IN A,($BF)
site 029D0   ; IN A,($BF)
site 02A12   ; IN A,($DC)
site 02A19   ; IN A,($BF)
site 02B71   ; IN A,($BF)
site 02D34   ; IN A,($BF)
site 02DC5   ; IN A,($BF)
site 04C57   ; OUT ($BF),A
site 04C5C   ; OUT ($BF),A
site 04C5F   ; OUT ($BE),A
site 04C63   ; OUT ($BE),A
site 053E4   ; IN A,($BF)
site 05473   ; IN A,($BF)
site 05B94   ; IN A,($BF)
site 05BDF   ; IN A,($BF)
site 0C246   ; IN A,($BF)
site 0C47D   ; OUTI
site 0C490   ; IN A,($BF)
site 10246   ; IN A,($BF)
site 1047D   ; OUTI
site 10490   ; IN A,($BF)
site 140B8   ; IN A,($BF)
site 180EC   ; OUTI
site 180F0   ; OUT (C),A
site 1C146   ; OUT ($F0),A
site 1C14F   ; OUT ($F1),A
site 1C171   ; OUT ($7F),A
site 1C175   ; OUT ($F0),A
site 1C17B   ; OUT ($F1),A
site 1C197   ; OUT ($7F),A
site 1C1A7   ; OUT (C),D
site 1C1AD   ; OUT ($F1),A
site 1C1D7   ; OUT ($7F),A
site 1C1DB   ; OUT ($7F),A
site 1C209   ; OTIR
site 1C21C   ; OUT ($F0),A
site 1C22A   ; OUT ($F1),A
site 1C233   ; OTIR
site 1C23D   ; OUT ($F0),A
site 1C243   ; OUT ($F1),A
site 1C24F   ; OUTI
site 1C255   ; OUTI
site 1C2B7   ; OUT ($7F),A
site 1C2BB   ; OUT ($7F),A
site 1C2BF   ; OUT ($7F),A
site 1C350   ; OUT ($7F),A
site 1C354   ; OUT ($7F),A
site 1C36B   ; OUT ($7F),A
site 1C393   ; OUT ($7F),A
site 1C397   ; OUT ($7F),A
site 1C39B   ; OUT ($7F),A
site 1C39F   ; OUT ($7F),A
site 1C3A2   ; OUT ($7F),A
site 1C408   ; OUT ($F0),A
site 1C40F   ; OUT ($F1),A
site 1C417   ; OUT ($F0),A
site 1C41D   ; OUT ($F1),A
site 1C51E   ; OUT ($F0),A
site 1C528   ; OUT (C),L
site 1C531   ; OUT ($F0),A
site 1C54C   ; OUT (C),H
site 1C554   ; OUT ($F0),A
site 1C562   ; OUT ($F1),A
site 1C56E   ; OUT ($F0),A
site 1C577   ; OUT ($F1),A
site 1C72C   ; OUT ($F0),A
site 1C735   ; OUT (C),A
site 1C73A   ; OUT ($F0),A
site 1C740   ; OUTI
site 1C767   ; OUT ($F0),A
site 1C76F   ; OUT (C),A
site 1C776   ; OUT ($F0),A
site 1C77E   ; OUT (C),A
site 1C7BF   ; OUT ($7F),A
site 1C85F   ; OUT ($7F),A
site 1C899   ; OUT ($7F),A
site 1C89D   ; OUT ($7F),A
site 1C8A7   ; OUT ($7F),A
site 1C8B5   ; OUT ($7F),A
site 1C8E1   ; OUT ($F0),A
site 1C8EF   ; OUT ($F1),A
site 1C903   ; OUT (C),A
site 1C90E   ; OUT ($F0),A
site 1C914   ; OUTI
site 1C91F   ; OUT ($F0),A
site 1C9B6   ; OUTI
site 1C9B8   ; OUTI
site 1C9BA   ; OUTI
site 1C9BC   ; OUTI
site 1C9BE   ; OUTI
site 1C9C0   ; OUTI
site 1C9C2   ; OUTI
site 1C9C4   ; OUTI
site 1C9C6   ; OUTI
site 1C9C8   ; OUTI
site 1C9CA   ; OUTI
site 1C9D4   ; OUT (C),D
site 1C9DA   ; OUT ($F1),A
site 1CA19   ; OUT ($7F),A
site 1CA6F   ; OUT ($7F),A
site 1CAAE   ; OUT ($7F),A
site 1CB10   ; OUT ($7F),A
site 1CB30   ; OUT ($7F),A
site 1CB7C   ; OUT ($7F),A
site 1CB86   ; OUT ($7F),A
site 1CBCE   ; OUT ($7F),A
site 2C028   ; IN A,($BF)
site 2C381   ; IN A,($BF)
site 2C488   ; IN A,($BF)
site 2C4E6   ; IN A,($BF)
site 2C9D2   ; IN A,($BF)
site 2CED6   ; IN A,($BF)
site 2CF19   ; IN A,($BF)
site 2CF50   ; IN A,($BF)
site 2DA3F   ; OUTI
site 2DA52   ; IN A,($BF)
site 2DF21   ; IN A,($BF)
site 2E57A   ; IN A,($BF)
mapst 00394   ; LD ($FFFF),A
mapst 0049D   ; LD ($FFFF),A
mapst 004A4   ; LD ($FFFF),A
mapst 004AE   ; LD ($FFFF),A
mapst 004B5   ; LD ($FFFF),A
mapldk 004E8   # LD HL,$FFFC; LD (HL),$00
maphl 004EE   # LD (HL),$00, HL = $FFFD
maphl 004F1   # LD (HL),$01, HL = $FFFE
maphl 004F4   # LD (HL),$02, HL = $FFFF
mapst 0058A   ; LD ($FFFF),A
mapst 006E3   ; LD ($FFFF),A
mapst 006EA   ; LD ($FFFF),A
mapst 006FB   ; LD ($FFFF),A
mapst 00702   ; LD ($FFFF),A
mapst 00917   ; LD ($FFFF),A
mapst 0091E   ; LD ($FFFF),A
mapst 01E10   ; LD ($FFFF),A
mapst 01E17   ; LD ($FFFF),A
mapst 01E3B   ; LD ($FFFF),A
mapst 01E42   ; LD ($FFFF),A
mapst 01E6B   ; LD ($FFFF),A
mapst 01E72   ; LD ($FFFF),A
mapst 02007   ; LD ($FFFF),A
mapst 02011   ; LD ($FFFF),A
mapst 02038   ; LD ($FFFF),A
mapst 0203F   ; LD ($FFFF),A
mapst 022A3   ; LD ($FFFF),A
mapst 022AA   ; LD ($FFFF),A
mapst 022C3   ; LD ($FFFF),A
mapst 022CA   ; LD ($FFFF),A
mapst 0237A   ; LD ($FFFF),A
mapst 02381   ; LD ($FFFF),A
mapst 025BB   ; LD ($FFFF),A
mapst 025C2   ; LD ($FFFF),A
mapst 029BF   ; LD ($FFFF),A
mapst 029C6   ; LD ($FFFF),A
mapst 02ADD   ; LD ($FFFF),A
mapst 02AE4   ; LD ($FFFF),A
mapst 02AF2   ; LD ($FFFF),A
mapst 02AF9   ; LD ($FFFF),A
mapst 04DB0   ; LD ($FFFF),A
mapst 04DB7   ; LD ($FFFF),A
mapst 04DC1   ; LD ($FFFF),A
mapst 04DC8   ; LD ($FFFF),A
mapst 05B9D   ; LD ($FFFF),A
mapst 05BA4   ; LD ($FFFF),A

# Bomber Raid (World) (Action Replay).cht, "Infinite Lives": RAM $C042 is the lives count,
# held at 9
poke "Infinite lives"
ar 00C0-4209
endpoke

# Bomber Raid (World) (Action Replay).cht, "Infinite Secondary Weapon": RAM $C153 is the
# bomb count (button 2), held at 9
poke "Infinite bombs"
ar 00C1-5309
endpoke

# Bomber Raid (World) (Action Replay).cht, "Always Have Max Speed": RAM $C150 held at 4
# makes the plane move faster
poke "Max speed"
ar 00C1-5004
endpoke

# Bomber Raid (World) (Action Replay).cht, "Always Invincible": RAM $C154 is the timer
# that starts when the plane is hit, held at 5
poke "Invincibility"
ar 00C1-5405
endpoke

# Bomber Raid (World) (Action Replay).cht, "Always Have Max Shot Power": RAM $C155 held
# at $25 makes the shots wide bursts
poke "Max shot power"
ar 00C1-5525
endpoke

# Bomber Raid (World).cht, "'Battle Wings' Title Screen": RAM $C116 held at $FF shows the
# BATTLE WINGS title in place of the BOMBER RAID title
poke "Battle Wings title"
ar 00C1-16FF
endpoke
