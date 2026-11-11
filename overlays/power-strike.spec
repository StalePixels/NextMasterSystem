# Power Strike (USA, Europe, Brazil) (En), CRC32 4077EFD9, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# The export release of Aleste (aleste.spec): the same code, moved by a few bytes in most
# places. Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - Scan entries: $0042, $017C, $0187, $0192, $019D, $02BA, $030D, $03F5, $040E and $0581,
#   the VDP routines of bank 0 that no path reaches (Aleste's $0042, $015A, $0165, $0170,
#   $017B, $0298, $03D3, $03EC and $055F, and $02EB). Each starts after a RET or a JP and is
#   a whole routine (DI, the VDP address routine, the data port, EI, RET), so their I/O
#   sites are patched.
# - The power-on code at $0003-$000E sets the mapper with four LD (HL),A stores ($FFFC=0,
#   $FFFD=0, $FFFE=1, $FFFF=1), a form no spec line takes. The asm block stores $FFFC and
#   $FFFF through the runtime's mapper store (inline codes $10 and $13, the third byte
#   skipped); slots 0 and 1 already hold banks 0 and 1 at the start.
# - The I/O ports $F0-$F2 are the FM unit: the game looks for it at power on ($00D8) and its
#   sound driver in bank 7 writes it when it is there.
# - The unrolled OUTI runs at $0F8C, $101E and $1155 are entered part way through by a RET
#   to a pushed address; every OUTI in them is a site.
# - The byte scan row at bank 4 $9FD3 is graphics.
name Power Strike
cart 4077EFD9
hz any		; No-Intro regions USA, Europe, Brazil
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
asm 00003 12         ; LD HL,$FFFC : XOR A : LD (HL),A : INC L : LD (HL),A : INC L : INC A : LD (HL),A : INC L : LD (HL),A
    xor a
    rst $00
    db $10,$FF
    inc a
    rst $00
    db $13,$FF
endasm
asm 00641 2   ; IM 1 -> IM 2
    im 2
endasm
asm 0064F 2   ; IM 1 -> IM 2
    im 2
endasm
site 00039   ; IN A,($BF)
site 00042   ; IN A,($BF)
site 0004B   ; OUT ($BF),A
site 00050   ; OUT ($BF),A
site 00075   ; OTIR
site 00093   ; OUT ($3F),A
site 00095   ; IN A,($DD)
site 0009F   ; OUT ($3F),A
site 000A1   ; IN A,($DD)
site 000AA   ; OUT ($3F),A
site 000BA   ; IN A,($BF)
site 000C0   ; IN A,($BF)
site 000C7   ; IN A,($BF)
site 000DD   ; OUT ($3E),A
site 000E5   ; OUT ($F2),A
site 000E8   ; IN A,($F2)
site 000FA   ; OUT ($F2),A
site 00102   ; OUT ($3E),A
site 00106   ; IN A,($BF)
site 0011B   ; OUTI
site 0011D   ; OUT ($BF),A
site 00124   ; OUT ($BF),A
site 00128   ; OUT ($BF),A
site 00130   ; OUT ($BE),A
site 00138   ; OUT ($BF),A
site 0013C   ; OUT ($BF),A
site 00140   ; OUT ($BE),A
site 00183   ; IN A,($BE)
site 0018E   ; IN A,($BE)
site 00199   ; OUT ($BE),A
site 001A4   ; OUT ($BE),A
site 001AA   ; OUT ($BF),A
site 001AF   ; OUT ($BF),A
site 001B5   ; OUT ($BF),A
site 001BA   ; OUT ($BF),A
site 001C0   ; OUT ($BF),A
site 001C5   ; OUT ($BF),A
site 001CB   ; OUT ($BF),A
site 001D0   ; OUT ($BF),A
site 001DE   ; OUT ($BE),A
site 001F0   ; IN A,($BE)
site 00204   ; OUT ($BE),A
site 00226   ; OUT (C),H
site 0022B   ; OUT (C),L
site 0025F   ; OUTI
site 00267   ; OUT (C),A
site 0029F   ; IN A,($BE)
site 002A4   ; IN A,($BE)
site 002A9   ; OUT ($BE),A
site 002B1   ; OUT ($BE),A
site 002DC   ; IN A,($BE)
site 002E1   ; IN A,($BE)
site 002E6   ; OUT ($BE),A
site 002EC   ; OUT ($BE),A
site 0031B   ; OUT ($BE),A
site 00321   ; OUT ($BE),A
site 003AB   ; OUT ($BE),A
site 003B3   ; OUT ($BE),A
site 003E5   ; OUT ($BE),A
site 003EA   ; IN A,($BE)
site 003FE   ; OUT ($BE),A
site 00404   ; IN A,($BE)
site 0040E   ; OUT ($BE),A
site 00413   ; OUT ($DF),A
site 0041B   ; OUT (C),D
site 0041D   ; IN A,(C)
site 00422   ; OUT (C),E
site 00424   ; IN A,(C)
site 00429   ; OUT (C),B
site 00463   ; OUT ($DE),A
site 00465   ; IN A,($DC)
site 0049E   ; OUT ($DE),A
site 004A0   ; IN A,($DC)
site 004A8   ; IN A,($DD)
site 004B5   ; OUT ($DE),A
site 004B7   ; IN A,($DC)
site 004C1   ; OUT ($DE),A
site 004C3   ; IN A,($DD)
site 00590   ; OTIR
site 0059A   ; OUT ($BE),A
site 005B4   ; OUTI
site 005B7   ; IN A,($BE)
site 005C3   ; OUT (C),A
site 005C6   ; IN A,($BE)
site 005E8   ; OUTI
site 005EB   ; IN A,($BE)
site 005EE   ; IN A,($BE)
site 005F1   ; IN A,($BE)
site 005FD   ; OUT (C),A
site 00600   ; IN A,($BE)
site 00603   ; IN A,($BE)
site 00606   ; IN A,($BE)
site 0061D   ; OUT ($F2),A
site 00F14   ; IN A,($DD)
site 00F49   ; OUT ($BF),A
site 00F4D   ; OUT ($BF),A
site 00F56   ; OUT ($BF),A
site 00F5A   ; OUT ($BF),A
site 00F7D   ; OUT ($BF),A
site 00F81   ; OUT ($BF),A
site 00F8C   ; OUTI
site 00F8E   ; OUTI
site 00F90   ; OUTI
site 00F92   ; OUTI
site 00F94   ; OUTI
site 00F96   ; OUTI
site 00F98   ; OUTI
site 00F9A   ; OUTI
site 00F9C   ; OUTI
site 00F9E   ; OUTI
site 00FA0   ; OUTI
site 00FA2   ; OUTI
site 00FA4   ; OUTI
site 00FA6   ; OUTI
site 00FA8   ; OUTI
site 00FAA   ; OUTI
site 00FAC   ; OUTI
site 00FAE   ; OUTI
site 00FB0   ; OUTI
site 00FB2   ; OUTI
site 00FB4   ; OUTI
site 00FB6   ; OUTI
site 00FB8   ; OUTI
site 00FBA   ; OUTI
site 00FBC   ; OUTI
site 00FBE   ; OUTI
site 00FC0   ; OUTI
site 00FC2   ; OUTI
site 00FC4   ; OUTI
site 00FC6   ; OUTI
site 00FC8   ; OUTI
site 00FCA   ; OUTI
site 00FCC   ; OUTI
site 00FCE   ; OUTI
site 00FD0   ; OUTI
site 00FD2   ; OUTI
site 00FD4   ; OUTI
site 00FD6   ; OUTI
site 00FD8   ; OUTI
site 00FDA   ; OUTI
site 00FDC   ; OUTI
site 00FDE   ; OUTI
site 00FE0   ; OUTI
site 00FE2   ; OUTI
site 00FE4   ; OUTI
site 00FE6   ; OUTI
site 00FE8   ; OUTI
site 00FEA   ; OUTI
site 00FEC   ; OUTI
site 00FEE   ; OUTI
site 00FF0   ; OUTI
site 00FF2   ; OUTI
site 00FF4   ; OUTI
site 00FF6   ; OUTI
site 00FF8   ; OUTI
site 00FFA   ; OUTI
site 00FFC   ; OUTI
site 00FFE   ; OUTI
site 01000   ; OUTI
site 01002   ; OUTI
site 01004   ; OUTI
site 01006   ; OUTI
site 01008   ; OUTI
site 0100A   ; OUTI
site 0100E   ; OUT ($BF),A
site 01012   ; OUT ($BF),A
site 0101E   ; OUTI
site 01020   ; OUTI
site 01022   ; OUTI
site 01024   ; OUTI
site 01026   ; OUTI
site 01028   ; OUTI
site 0102A   ; OUTI
site 0102C   ; OUTI
site 0102E   ; OUTI
site 01030   ; OUTI
site 01032   ; OUTI
site 01034   ; OUTI
site 01036   ; OUTI
site 01038   ; OUTI
site 0103A   ; OUTI
site 0103C   ; OUTI
site 0103E   ; OUTI
site 01040   ; OUTI
site 01042   ; OUTI
site 01044   ; OUTI
site 01046   ; OUTI
site 01048   ; OUTI
site 0104A   ; OUTI
site 0104C   ; OUTI
site 0104E   ; OUTI
site 01050   ; OUTI
site 01052   ; OUTI
site 01054   ; OUTI
site 01056   ; OUTI
site 01058   ; OUTI
site 0105A   ; OUTI
site 0105C   ; OUTI
site 0105E   ; OUTI
site 01060   ; OUTI
site 01062   ; OUTI
site 01064   ; OUTI
site 01066   ; OUTI
site 01068   ; OUTI
site 0106A   ; OUTI
site 0106C   ; OUTI
site 0106E   ; OUTI
site 01070   ; OUTI
site 01072   ; OUTI
site 01074   ; OUTI
site 01076   ; OUTI
site 01078   ; OUTI
site 0107A   ; OUTI
site 0107C   ; OUTI
site 0107E   ; OUTI
site 01080   ; OUTI
site 01082   ; OUTI
site 01084   ; OUTI
site 01086   ; OUTI
site 01088   ; OUTI
site 0108A   ; OUTI
site 0108C   ; OUTI
site 0108E   ; OUTI
site 01090   ; OUTI
site 01092   ; OUTI
site 01094   ; OUTI
site 01096   ; OUTI
site 01098   ; OUTI
site 0109A   ; OUTI
site 0109C   ; OUTI
site 0109E   ; OUTI
site 010A0   ; OUTI
site 010A2   ; OUTI
site 010A4   ; OUTI
site 010A6   ; OUTI
site 010A8   ; OUTI
site 010AA   ; OUTI
site 010AC   ; OUTI
site 010AE   ; OUTI
site 010B0   ; OUTI
site 010B2   ; OUTI
site 010B4   ; OUTI
site 010B6   ; OUTI
site 010B8   ; OUTI
site 010BA   ; OUTI
site 010BC   ; OUTI
site 010BE   ; OUTI
site 010C0   ; OUTI
site 010C2   ; OUTI
site 010C4   ; OUTI
site 010C6   ; OUTI
site 010C8   ; OUTI
site 010CA   ; OUTI
site 010CC   ; OUTI
site 010CE   ; OUTI
site 010D0   ; OUTI
site 010D2   ; OUTI
site 010D4   ; OUTI
site 010D6   ; OUTI
site 010D8   ; OUTI
site 010DA   ; OUTI
site 010DC   ; OUTI
site 010DE   ; OUTI
site 010E0   ; OUTI
site 010E2   ; OUTI
site 010E4   ; OUTI
site 010E6   ; OUTI
site 010E8   ; OUTI
site 010EA   ; OUTI
site 010EC   ; OUTI
site 010EE   ; OUTI
site 010F0   ; OUTI
site 010F2   ; OUTI
site 010F4   ; OUTI
site 010F6   ; OUTI
site 010F8   ; OUTI
site 010FA   ; OUTI
site 010FC   ; OUTI
site 010FE   ; OUTI
site 01100   ; OUTI
site 01102   ; OUTI
site 01104   ; OUTI
site 01106   ; OUTI
site 01108   ; OUTI
site 0110A   ; OUTI
site 0110C   ; OUTI
site 0110E   ; OUTI
site 01110   ; OUTI
site 01112   ; OUTI
site 01114   ; OUTI
site 01116   ; OUTI
site 01118   ; OUTI
site 0111A   ; OUTI
site 0111C   ; OUTI
site 01155   ; OUTI
site 01157   ; OUTI
site 01159   ; OUTI
site 0115B   ; OUTI
site 0115D   ; OUTI
site 0115F   ; OUTI
site 01161   ; OUTI
site 01163   ; OUTI
site 01165   ; OUTI
site 01167   ; OUTI
site 01169   ; OUTI
site 0116B   ; OUTI
site 0116D   ; OUTI
site 0116F   ; OUTI
site 01171   ; OUTI
site 01173   ; OUTI
site 01175   ; OUTI
site 01177   ; OUTI
site 01179   ; OUTI
site 0117B   ; OUTI
site 0117D   ; OUTI
site 0117F   ; OUTI
site 01181   ; OUTI
site 01183   ; OUTI
site 01185   ; OUTI
site 01187   ; OUTI
site 01189   ; OUTI
site 0118B   ; OUTI
site 0118D   ; OUTI
site 0118F   ; OUTI
site 01191   ; OUTI
site 01193   ; OUTI
site 01195   ; OUTI
site 01197   ; OUTI
site 01199   ; OUTI
site 0119B   ; OUTI
site 0119D   ; OUTI
site 0119F   ; OUTI
site 011A1   ; OUTI
site 011A3   ; OUTI
site 011A5   ; OUTI
site 011A7   ; OUTI
site 011A9   ; OUTI
site 011AB   ; OUTI
site 011AD   ; OUTI
site 011AF   ; OUTI
site 011B1   ; OUTI
site 011B3   ; OUTI
site 011B5   ; OUTI
site 011B7   ; OUTI
site 011B9   ; OUTI
site 011BB   ; OUTI
site 011BD   ; OUTI
site 011BF   ; OUTI
site 011C1   ; OUTI
site 011C3   ; OUTI
site 011C5   ; OUTI
site 011C7   ; OUTI
site 011C9   ; OUTI
site 011CB   ; OUTI
site 011CD   ; OUTI
site 011CF   ; OUTI
site 011D1   ; OUTI
site 011D3   ; OUTI
site 0120E   ; OUT (C),E
site 01210   ; OUT (C),D
site 01214   ; OUTI
site 01216   ; OUTI
site 01218   ; OUTI
site 0121A   ; OUTI
site 0121C   ; OUTI
site 0121E   ; OUTI
site 01220   ; OUTI
site 01222   ; OUTI
site 01224   ; OUTI
site 01226   ; OUTI
site 01228   ; OUTI
site 0122A   ; OUTI
site 0122C   ; OUTI
site 0122E   ; OUTI
site 01230   ; OUTI
site 01232   ; OUTI
site 01E01   ; OUT ($BF),A
site 01E05   ; OUT ($BF),A
site 01E0F   ; INI
site 01E1B   ; OUT ($BF),A
site 01E1F   ; OUT ($BF),A
otir 01E29   ; OUTI
site 02020   ; OUT ($FF),A
site 03E86   ; OUT ($BE),A
site 03E8D   ; OUT ($BE),A
site 03E95   ; IN A,($BE)
site 03E9C   ; IN A,($BE)
site 06533   ; OUT ($BE),A
site 1C132   ; OUT ($F0),A
site 1C13F   ; OUT ($F1),A
site 1C151   ; OUT ($F0),A
site 1C158   ; OUT ($F1),A
site 1C161   ; OUT ($F1),A
site 1C176   ; OUT ($F0),A
site 1C17A   ; OUT ($F1),A
site 1C189   ; OUT ($F0),A
site 1C18E   ; OUT ($F1),A
site 1C19A   ; OUT ($F1),A
site 1C1AD   ; OUT ($F0),A
site 1C1B1   ; OUT ($F1),A
site 1C1D1   ; OUT ($F0),A
site 1C1D6   ; OUT ($F1),A
site 1C1EB   ; OUT ($7F),A
site 1C1F1   ; OUT ($7F),A
site 1C1FD   ; OUT ($7F),A
site 1C21A   ; OUT ($7F),A
site 1C223   ; OUT ($7F),A
site 1C828   ; OUT ($F0),A
site 1C82C   ; OUT ($F1),A
site 1C83D   ; OUT ($F2),A
mapst 0081D   ; LD ($FFFF),A
mapst 0082C   ; LD ($FFFF),A
mapst 00836   ; LD ($FFFF),A
mapst 0083D   ; LD ($FFFF),A
mapst 00863   ; LD ($FFFF),A
mapst 0086D   ; LD ($FFFF),A
mapst 00877   ; LD ($FFFF),A
mapst 0087E   ; LD ($FFFF),A
mapst 00888   ; LD ($FFFF),A
mapst 00892   ; LD ($FFFF),A
mapst 008A0   ; LD ($FFFF),A
mapst 008A7   ; LD ($FFFF),A
mapst 0126A   ; LD ($FFFF),A
mapst 01284   ; LD ($FFFF),A
mapst 01298   ; LD ($FFFF),A
mapst 0129F   ; LD ($FFFF),A
mapst 01670   ; LD ($FFFF),A
mapst 016E4   ; LD ($FFFF),A
mapst 01988   ; LD ($FFFF),A
mapst 01E3D   ; LD ($FFFF),A
mapst 01EEB   ; LD ($FFFF),A
mapst 01EFF   ; LD ($FFFF),A
mapst 01F69   ; LD ($FFFF),A
mapst 02DAA   ; LD ($FFFF),A
mapst 02E68   ; LD ($FFFF),A

# Power Strike (USA, Europe, Brazil).cht, "Infinite Lives": RAM $C812 is the lives count,
# held at 9
poke "Infinite lives"
ar 00C8-1209
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Invulnerability": RAM $C416 is the timer of the
# shield after a death, held at its full value of $3C so that the ship is never hit
poke "Invincibility"
ar 00C4-163C
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Start with ?? Lives, instead of 3": the byte
# loaded as the lives count at the start of a game, set here to 9
poke "Start with 9 lives"
gg 09C-E0F-E66
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Temporary Invincibility after Dying and at Start
# of Level Lasts ?? Longer": the shield timer after a death starts at $5A (90 frames)
# instead of $3C (60 frames)
poke "Long respawn shield"
gg 5A1-43B-19A
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Infinite Special Weapon": RAM $C83E is the ammo
# of the special weapon
poke "Infinite special weapon"
ar 00C8-3E64
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Max Regular Weapon Power": RAM $C813, $C815 and
# $C816 are the levels of the regular weapon
poke "Max weapon power"
ar 00C8-1308
ar 00C8-1503
ar 00C8-1604
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Keep Regular Weapon Power after Dying": the
# regular weapon levels are no longer reset when a life is lost
poke "Keep weapon on death"
gg 3A1-D49-2A2
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Max Special Weapon Power": RAM $C840 is the power
# of the special weapon, held at 3
poke "Max special weapon power"
ar 00C8-4003
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Special Weapon Modifier": RAM $C83C is the type
# of the special weapon, 1 to 5 (0 is none)
poke "Special weapon ??"
ar 00C8-3C??
endpoke

# Power Strike (USA, Europe, Brazil).cht, "Round Modifier": RAM $C881 is the round, 1 to 6
poke "Start round ??"
ar 00C8-81??
endpoke
