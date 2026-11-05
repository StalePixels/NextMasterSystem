# Zillion II - The Tri Formation (World), CRC32 2F2E3BC9, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output (no reference logs).
# Decisions:
# - No free RST vector ($0008, $0010, $0020 and $0030 are the game's), so $0000 is
#   the io vector.
# - The byte patterns that no path reached: $0275 is in the rectangle clear $026F, which
#   nothing in the cart calls (verdict unused); $050DD, $059E5 and $16BB6 are bytes of
#   word tables (verdict false).
# - The unresolved JP (HL) at $0029 comes from entry 0 of the table at $49A2, which is
#   the operand of the JP $0020 before it; the game never uses entry 0 ($4996 returns
#   when $C03D is 0).
name Zillion II - The Tri Formation
cart 2F2E3BC9
hz any		; No-Intro region World
vector 00 io
start 0003
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
otir 00033   ; OUTI
site 00109   ; OUT ($3E),A
site 00111   ; OUT ($F2),A
site 00114   ; IN A,($F2)
site 00126   ; OUT ($F2),A
site 0012E   ; OUT ($3E),A
site 00138   ; OUT ($3F),A
site 0013A   ; IN A,($DD)
site 00143   ; OUT ($3F),A
site 00145   ; IN A,($DD)
site 0014D   ; OUT ($3F),A
site 00186   ; IN A,($BF)
site 00188   ; IN A,($DD)
site 001E8   ; OUT ($BE),A
otir 001F5   ; OUTI
site 00203   ; OUTI
site 00207   ; OUT (C),A
site 00216   ; INI
site 00231   ; OUT ($BE),A
site 00236   ; OUT ($BE),A
site 00243   ; OUTI
site 0025A   ; OUTI
site 00260   ; OUT (C),A
site 00294   ; OUT (C),D
otir 002BB   ; OUTI
otir 002C8   ; OUTI
site 002E1   ; OUTD
site 002E7   ; OUT ($BE),A
site 002F9   ; OUTI
site 002FB   ; OUTD
site 00309   ; OTIR
site 0030C   ; OUT ($BE),A
site 00343   ; OUT ($BF),A
site 00346   ; OUT ($BF),A
site 00349   ; OUT ($BE),A
site 00371   ; OUT ($BE),A
site 003D9   ; OUT ($DF),A
site 003E5   ; OUT ($DE),A
site 003E7   ; IN A,($DE)
site 003F1   ; IN A,($DC)
site 003F7   ; IN A,($DD)
site 008DC   ; OTIR
site 0093D   ; OUT ($BE),A
site 00945   ; OUT ($BE),A
site 00A4F   ; OUT ($BE),A
site 00A56   ; OUT ($BE),A
site 00A71   ; OUT ($BE),A
site 00A79   ; OUT ($BE),A
site 01AC8   ; OUT ($BE),A
site 01ACE   ; OUT ($BE),A
site 01B31   ; OUT ($BE),A
site 02D71   ; OUT ($BE),A
site 02D7D   ; OUT ($BE),A
site 045B7   ; OUTI
site 045B9   ; OUTI
site 045BB   ; OUTI
site 045BD   ; OUT ($BE),A
site 045BF   ; OUTI
site 045C1   ; OUTI
site 045C3   ; OUTI
site 045C5   ; OUT ($BE),A
site 045C7   ; OUTI
site 045C9   ; OUTI
site 045CB   ; OUTI
site 045CD   ; OUT ($BE),A
site 045CF   ; OUTI
site 045D1   ; OUTI
site 045D3   ; OUTI
site 045D5   ; OUT ($BE),A
site 045D7   ; OUTI
site 045D9   ; OUTI
site 045DB   ; OUTI
site 045DD   ; OUT ($BE),A
site 045DF   ; OUTI
site 045E1   ; OUTI
site 045E3   ; OUTI
site 045E5   ; OUT ($BE),A
site 045E7   ; OUTI
site 045E9   ; OUTI
site 045EB   ; OUTI
site 045ED   ; OUT ($BE),A
site 045EF   ; OUTI
site 045F1   ; OUTI
site 045F3   ; OUTI
site 045F5   ; OUT ($BE),A
site 04613   ; OUTI
site 0461B   ; OUTI
site 04623   ; OUTI
site 0462B   ; OUT ($BE),A
site 04633   ; OUTI
site 0463B   ; OUTI
site 04643   ; OUTI
site 0464B   ; OUT ($BE),A
site 04653   ; OUTI
site 0465B   ; OUTI
site 04663   ; OUTI
site 0466B   ; OUT ($BE),A
site 04673   ; OUTI
site 0467B   ; OUTI
site 04683   ; OUTI
site 0468B   ; OUT ($BE),A
site 04693   ; OUTI
site 0469B   ; OUTI
site 046A3   ; OUTI
site 046AB   ; OUT ($BE),A
site 046B3   ; OUTI
site 046BB   ; OUTI
site 046C3   ; OUTI
site 046CB   ; OUT ($BE),A
site 046D3   ; OUTI
site 046DB   ; OUTI
site 046E3   ; OUTI
site 046EB   ; OUT ($BE),A
site 046F3   ; OUTI
site 046FB   ; OUTI
site 04703   ; OUTI
site 0470B   ; OUT ($BE),A
site 049EC   ; OUT ($BE),A
site 049F1   ; IN A,($BE)
site 04BC5   ; OUT ($BE),A
site 04BCC   ; OUT ($BE),A
site 080FF   ; OUT ($F0),A
site 08108   ; OUT ($F1),A
site 08120   ; OUT ($7F),A
site 08130   ; OUT (C),D
site 08136   ; OUT ($F1),A
site 08149   ; OUT ($F0),A
site 0814F   ; OUT ($F1),A
site 0815B   ; OUTI
site 08161   ; OUTI
site 082C0   ; OUT ($7F),A
site 082C4   ; OUT ($7F),A
site 0835E   ; OUT ($7F),A
site 08386   ; OUT ($7F),A
site 083DF   ; OUT ($F0),A
site 083E6   ; OUT ($F1),A
site 083EE   ; OUT ($F0),A
site 083F4   ; OUT ($F1),A
site 084E9   ; OUT ($F0),A
site 084F0   ; OUT (C),L
site 084F9   ; OUT ($F0),A
site 08514   ; OUT (C),H
site 0851C   ; OUT ($F0),A
site 0852A   ; OUT ($F1),A
site 08532   ; OUT ($F0),A
site 0853C   ; OUT ($F1),A
site 086F6   ; OUT ($F0),A
site 086FC   ; OUT ($F1),A
site 08708   ; OUT ($F0),A
site 0870E   ; OUTI
site 08779   ; OUT ($7F),A
site 08851   ; OUT ($7F),A
site 08855   ; OUT ($7F),A
site 08872   ; OUT ($7F),A
site 08894   ; OUT ($7F),A
site 088A3   ; OUT ($F0),A
site 088AE   ; OUT ($F1),A
site 088BF   ; OUT ($F0),A
site 088D3   ; OUT ($F0),A
site 088E7   ; OUT ($F1),A
site 0894C   ; OTIR
site 08959   ; OUT (C),D
site 0895F   ; OUT ($F1),A
site 0899A   ; OUT ($7F),A
site 089EB   ; OUT ($7F),A
site 08A76   ; OUT ($7F),A
site 08A94   ; OUT ($7F),A
site 08AD4   ; OUT ($7F),A
site 08ADE   ; OUT ($7F),A
site 08B26   ; OUT ($7F),A
mapst 0008D   ; LD ($FFFF),A
mapst 000B7   ; LD ($FFFF),A
mapst 001A3   ; LD ($FFFF),A
mapst 001C7   ; LD ($FFFF),A
mapst 001D2   ; LD ($FFFF),A
mapst 004A2   ; LD ($FFFF),A
mapst 00AC5   ; LD ($FFFF),A
mapst 00AF5   ; LD ($FFFF),A
mapst 00BB9   ; LD ($FFFF),A
mapst 00BDB   ; LD ($FFFF),A
mapst 00BEE   ; LD ($FFFF),A
mapst 00C1C   ; LD ($FFFF),A
mapst 00D6E   ; LD ($FFFF),A
mapst 00D9A   ; LD ($FFFF),A
mapst 00E1F   ; LD ($FFFF),A
mapst 00E80   ; LD ($FFFF),A
mapst 00EE2   ; LD ($FFFF),A
mapst 00F0E   ; LD ($FFFF),A
mapst 00F22   ; LD ($FFFF),A
mapst 0152F   ; LD ($FFFF),A
mapst 0155E   ; LD ($FFFF),A
mapst 015B1   ; LD ($FFFF),A
mapst 015C2   ; LD ($FFFF),A
mapst 015D4   ; LD ($FFFF),A
mapst 0192E   ; LD ($FFFF),A
mapst 02D16   ; LD ($FFFF),A
mapst 02DA1   ; LD ($FFFF),A
mapst 02DFF   ; LD ($FFFF),A
mapst 02E46   ; LD ($FFFF),A
mapst 0459B   ; LD ($FFFF),A
mapst 049AC   ; LD ($FFFF),A
mapst 04AB3   ; LD ($FFFF),A
mapst 04ACD   ; LD ($FFFF),A
mapst 04B59   ; LD ($FFFF),A
mapst 04BA5   ; LD ($FFFF),A
mapst 04BEB   ; LD ($FFFF),A
mapst 04BFB   ; LD ($FFFF),A
mapst 04E79   ; LD ($FFFF),A
mapst 07A95   ; LD ($FFFF),A
mapst 07C81   ; LD ($FFFF),A
mapst 07F81   ; LD ($FFFF),A
mapst 07F9E   ; LD ($FFFF),A
mapst 07FE6   ; LD ($FFFF),A

# Zillion II - The Tri Formation (World) (Action Replay).cht, "Infinite Lives": RAM $C01F
# is the number of lives; held at 9, a lost life does not use one up
poke "Infinite lives"
ar 00C0-1F09
endpoke

# Zillion II - The Tri Formation (World) (Action Replay).cht, "Infinite Health": RAM $C018
# is the life bar. The file holds it at $47, more than a full bar ($3F), which draws the bar
# with wrong tiles after a hit; the block holds $3F.
poke "Infinite health"
ar 00C0-183F
endpoke

# Zillion II - The Tri Formation (World) (Action Replay).cht, "Pick-Up One "Z" For Max Gun
# Power": RAM $C01E is the gun power shown on the status bar as "x"; held at 3, the gun is at
# its top level
poke "Max gun power"
ar 00C0-1E03
endpoke
