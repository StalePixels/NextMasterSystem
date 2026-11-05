# Taz-Mania (Europe, Brazil) (En), CRC32 7CC3E837, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - No free RST vector, so $0000-$0002 (DI; IM 1) is the io vector and the game starts
#   at $0003.
# - The frame handler runs a list of VDP commands at $0BBB through a table of 13
#   JP nn; NOP entries at $0BDD ($0C10-$0D37). The sites in those routines are listed
#   like the others.
# - The game sets banks through register-indexed stores: LD (HL),C with HL = $FFFD + B
#   ($0DFC and the command routines $0C19 and $0C30), and the frame handler puts slots
#   0-2 back from its copies at $C004-$C006 with three LDI at $0F66. Each goes through
#   a code cave in the $FF bytes from $7C00 (bank 1, always in slot 1).
# - The store LD ($7F40),A at $0D67 writes $D0 into cart filler that nothing reads; it
#   gets no line.
name Taz-Mania
cart 7CC3E837
hz 50		; No-Intro region Europe, Brazil
vector 00 io
start 0003
mapsthl 00084   ; LD ($FFFC),HL
mapsthl 0008A   ; LD ($FFFE),HL
mapst 00E64   ; LD ($FFFF),A
mapst 00EB1   ; LD ($FFFF),A
mapst 00F3E   ; LD ($FFFF),A
mapst 00F5A   ; LD ($FFFF),A
label cv_mapbc 07C00
label cv_restore 07C1C
asm 07C00 28   ; unused $FF bytes: cave for LD (HL),C with HL = $FFFD + B
    ld a,b
    cp 1
    ld a,c
    jr c,mb_0
    jr z,mb_1
    rst $00
    db $13, 0     ; LD ($FFFF),A
    jr mb_done
mb_1:
    rst $00
    db $12, 0     ; LD ($FFFE),A
    jr mb_done
mb_0:
    rst $00
    db $11, 0     ; LD ($FFFD),A
mb_done:
    ld hl,$FFFD   ; HL and A as the game's code leaves them
    ld a,b
    add a,l
    ld l,a
    ret
endasm
asm 07C1C 19   ; unused $FF bytes: cave for the frame handler's LDI x3 to $FFFD-$FFFF
    ld a,($C004)
    rst $00
    db $11, 0
    ld a,($C005)
    rst $00
    db $12, 0
    ld a,($C006)
    rst $00
    db $13, 0
    ret
endasm
asm 00E03 8    ; LD HL,$FFFD; LD A,B; ADD A,L; LD L,A; LD (HL),C; RET
    call cv_mapbc
    ret
endasm
asm 00C1E 7    ; LD HL,$FFFD; LD A,B; ADD A,L; LD L,A; LD (HL),C
    call cv_mapbc
endasm
asm 00C35 7    ; LD HL,$FFFD; LD A,B; ADD A,L; LD L,A; LD (HL),C
    call cv_mapbc
endasm
asm 00F60 12   ; LD DE,$FFFD; LD HL,$C004; LDI; LDI; LDI
    call cv_restore
endasm
site 00039   ; IN A,($BF)
site 00C12   ; OUTI
site 00C14   ; OUTI
site 00C42   ; OUTI
site 00C44   ; OUTI
site 00C47   ; OUTI
site 00C4E   ; OUTI
site 00C50   ; OUTI
site 00C54   ; OUT ($BE),A
site 00C5C   ; OUT ($BE),A
site 00C63   ; OUTI
site 00C65   ; OUTI
site 00C77   ; OUT ($BE),A
site 00C87   ; OUTI
site 00C89   ; OUTI
site 00C9B   ; OUT ($BE),A
site 00CA3   ; OUT ($BE),A
site 00CB3   ; OUTI
site 00CB5   ; OUTI
site 00CC4   ; OUT ($BE),A
site 00CD5   ; OUTI
site 00CD7   ; OUTI
site 00CE8   ; OUT ($BE),A
site 00CEE   ; OUT ($BE),A
site 00CFC   ; OUTI
site 00CFE   ; OUTI
site 00D01   ; OUTI
site 00D08   ; OUTI
site 00D0A   ; OUTI
site 00D14   ; OUT ($BE),A
site 00D24   ; OUTI
site 00D26   ; OUTI
site 00D2C   ; OUT ($BE),A
site 00D4D   ; OUT (C),L
site 00D4F   ; OUT (C),H
site 00D53   ; OUT ($BE),A
site 00D5B   ; OUT ($BE),A
site 00D6C   ; OUT ($BF),A
site 00D70   ; OUT ($BF),A
site 00D79   ; OTIR
site 00D7D   ; OUT ($BE),A
site 00D81   ; OUT ($BF),A
site 00D85   ; OUT ($BF),A
site 00D8E   ; OTIR
site 00D93   ; OUT ($BF),A
site 00D97   ; OUT ($BF),A
site 00D9C   ; OTIR
site 00DA0   ; OTIR
site 00DA4   ; OUT ($BF),A
site 00DA8   ; OUT ($BF),A
site 00DAB   ; OUT ($BE),A
site 00DAF   ; OUT ($BF),A
site 00DB3   ; OUT ($BF),A
site 00DB7   ; OUT ($BE),A
site 00DC1   ; IN A,($DC)
site 00DC9   ; IN A,($DC)
site 00DCE   ; IN A,($DD)
site 00E0B   ; IN A,($7E)
site 00E18   ; OTIR
site 00F25   ; OUT ($BF),A
site 00F29   ; OUT ($BF),A
site 0106F   ; OUT ($BF),A
site 01073   ; OUT ($BF),A
site 0107B   ; OUTI
site 010AD   ; OUT ($BF),A
site 010B1   ; OUT ($BF),A
site 010B9   ; OUTI
site 04BA9   ; IN A,($DC)
site 04BAE   ; IN A,($DD)
site 04BED   ; IN A,($DC)
site 0820A   ; OUT ($7F),A
site 08331   ; OUT ($7F),A
site 084C3   ; OTIR
site 085DB   ; OUT ($7F),A
site 085E5   ; OUT ($7F),A
site 08602   ; OUT ($7F),A
site 08706   ; OUT ($7F),A
site 08792   ; OUT ($7F),A
site 08834   ; OUT ($7F),A
site 0883D   ; OUT ($7F),A
site 0884D   ; OUT ($7F),A
site 088B7   ; OUT ($7F),A
site 088D4   ; OUT ($7F),A

# Taz-Mania (Europe, Brazil).cht, "Infinite Lives": RAM $C100 is the lives counter
poke "Infinite lives"
ar 00C1-0099
endpoke

# Taz-Mania (Europe, Brazil).cht, "Infinite Life": RAM $C103 is the energy bar (L), $20 is
# full; held full, hits do not take a life. A pit fall still costs a life on the Next.
poke "Infinite energy"
ar 00C1-0320
endpoke

# Taz-Mania (Europe, Brazil).cht, "Infinite Power": RAM $C106 is the spin power bar (P), held
# full so a spin never runs the bar down
poke "Infinite spin power"
ar 00C1-0620
endpoke

# Taz-Mania (Europe, Brazil).cht, "Invulnerability": RAM $C139 is the hit timer, held at $35
# so enemy and hazard contact costs no energy; a fall into a pit still takes a life
poke "Invulnerability"
ar 00C1-3935
endpoke
