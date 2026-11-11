# Super Space Invaders (Europe), CRC32 1D6244EE, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output with a reference I/O log, then decided by hand.
#
# Decisions:
# - $0010-$0017 are $00 filler that no code reaches, and the game uses only RST $18 (its bank
#   call: LD E,n : RST $18 puts bank n in slot 2): $10 is the io vector.
# - The interrupt handler runs from RAM: $3C2F copies bank 15 $AB62-$BEE9 to $C000, and $0038
#   jumps to $C8E5. Its sites are patched in the bank 15 bytes the copy reads, so the copy
#   carries them. The unrolled sprite table upload ($CA52-$CCA9) is entered by sprite count
#   through JP (IX) at $CA50 and $CBA8; every OUTI in it is patched.
# - The game turns the handler off by storing $C9FB (EI : RET) at $C8E5 and on again by
#   storing $DBF5 (PUSH AF and the IN opcode). The IN at $C8E6 is a patched site, so each
#   restore stores $D7F5 (RST $10) instead; the inline code at $C8E7 is not touched.
# - The sound routine at bank 11 $AE6E silences the PSG at $AE84-$AE92; the handler calls it
#   at $C99C and $C9B2.
# - Code that no scanned path or recording reaches, patched as code (it costs nothing if it never
#   runs): bank 4 $AE7A (waits 50 frames, then silences the PSG at $AE9D-$AEA9) and the channel
#   mute at bank 9 $B51E, in the routine at $B517 with the patched $B527.
# - LDIR at $3CC1-$3CC7 (HL = DE = 0, BC = 0) and at $07B2, $0831, $085E, $4A05, $4A27, $4A6D,
#   $4A8F and bank 11 $AEF8 copy memory onto itself as delays; the mapper sees the same values
#   again, so they are not patched.
# - The handler saves AF', BC, DE, HL and IX, but not BC', DE' and HL'. The sound drivers it
#   calls (bank 9 $AC23 from $C970, bank 11 $AE6E from $C99C and $C9B2) use EXX and change
#   them, and the sprite builder at $09A2-$09F3 keeps its sprite count in C'. A frame interrupt
#   inside the builder stores a wrong count at $C2C1, and the handler's JP (IX) into the sprite
#   upload then runs into the developer monitor. The three calls go to caves in the $00 bytes at
#   $0300 (no code runs there: $0292 JP NZ,$0400 always jumps, ROM $0007 is 1) that save BC',
#   DE' and HL' in page 0 around the driver; the registers are kept in the page, not on the
#   game's stack.
# - The score panel (name table columns 24-31) has the priority bit: the saucer at the top of
#   the screen passes behind it. The game loads new tiles under the panel's top border cells
#   after they are on screen; prichg draws those cells again from the new tiles.
name Super Space Invaders
cart 1D6244EE
hz 50		; No-Intro region Europe
vector 10 io
priority
prichg
asm 00276 2   ; IM 1 -> IM 2
    im 2
endasm
label altcave9 00300
label altcave11 00308
asm 00300 24  ; $00 bytes: the caves that keep BC', DE' and HL' across the sound drivers
    call altsv
    call $AC23          ; bank 9, put in slot 2 by the handler
    jr altrs
    call altsv
    call $AE6E          ; bank 11, put in slot 2 by the handler
altrs:
    rst $10
    db far_io, pg_alt_rest, ent_alt_rest
    ret
altsv:
    rst $10
    db far_io, pg_alt_save, ent_alt_save
    ret
endasm
asm 3F4D2 3   ; CALL $AC23 at RAM $C970 in the handler
    call altcave9
endasm
asm 3F4FE 3   ; CALL $AE6E at RAM $C99C in the handler
    call altcave11
endasm
asm 3F514 3   ; CALL $AE6E at RAM $C9B2 in the handler
    call altcave11
endasm
page 0 alt_save alt_rest
; BC', DE' and HL' of the game, kept across the handler's sound driver calls
alt_save:
    exx
    ld (sv_bc),bc
    ld (sv_de),de
    ld (sv_hl),hl
    exx
    ret
alt_rest:
    exx
    ld bc,(sv_bc)
    ld de,(sv_de)
    ld hl,(sv_hl)
    exx
    ret
sv_bc: dw 0
sv_de: dw 0
sv_hl: dw 0
endpage
mapst 00055   ; LD ($FFFF),A
mapst 00278   ; LD ($FFFC),A
mapst 0027B   ; LD ($FFFD),A
mapst 0027F   ; LD ($FFFE),A
mapst 00283   ; LD ($FFFF),A
site 00286   ; IN A,($BF)
site 00766   ; OUT (C),A
site 0076C   ; OUT (C),A
otir 00772   ; OUTI
site 00877   ; OUT (C),A
site 0087E   ; OUT (C),A
site 00885   ; OUT ($BE),A
site 0088D   ; OUT ($BF),A
site 00894   ; OUT ($BF),A
site 008AA   ; OUT (C),A
site 008B1   ; OUT (C),A
site 008B8   ; OUT ($BE),A
site 008C1   ; OUT ($BE),A
site 008D2   ; OUT ($BF),A
site 008D9   ; OUT ($BF),A
site 008DC   ; OUT ($BE),A
site 0093E   ; OUT ($BF),A
site 00945   ; OUT ($BF),A
site 0094B   ; OUT ($BE),A
site 00951   ; OUT ($BE),A
site 00AEE   ; IN A,($DC)
site 00AFD   ; IN A,($DD)
site 01E58   ; OUT (C),A
site 01E5F   ; OUT (C),A
site 01E66   ; OUT ($BE),A
site 02531   ; OUT ($BF),A
site 0253A   ; OUT ($BF),A
site 02548   ; OUT (C),A
site 0255E   ; OUT ($BF),A
site 02565   ; OUT ($BF),A
site 0258A   ; OUT ($BF),A
site 02593   ; OUT ($BF),A
site 025A4   ; OUT (C),A
site 025BA   ; OUT ($BF),A
site 025C1   ; OUT ($BF),A
site 025CB   ; OUT ($BF),A
site 025D4   ; OUT ($BF),A
site 025E9   ; OUT (C),A
site 025FF   ; OUT ($BF),A
site 02606   ; OUT ($BF),A
site 0268B   ; OUT ($7F),A
site 0268F   ; OUT ($7F),A
site 02693   ; OUT ($7F),A
site 02697   ; OUT ($7F),A
site 03C33   ; OUT ($BF),A
site 03C3A   ; OUT ($BF),A
site 03C40   ; OUT ($BF),A
site 03C47   ; OUT ($BF),A
site 03C4D   ; OUT ($BF),A
site 03C54   ; OUT ($BF),A
site 03C5A   ; OUT ($BF),A
site 03C61   ; OUT ($BF),A
site 03C67   ; OUT ($BF),A
site 03C6E   ; OUT ($BF),A
site 03C74   ; OUT ($BF),A
site 03C7B   ; OUT ($BF),A
site 03C81   ; OUT ($BF),A
site 03C88   ; OUT ($BF),A
site 03C8E   ; OUT ($BF),A
site 03C95   ; OUT ($BF),A
site 03C9B   ; OUT ($BF),A
site 03CA2   ; OUT ($BF),A
site 03D51   ; OUT ($BF),A
site 03D58   ; OUT ($BF),A
site 03DF8   ; OUT ($BF),A
site 03DFF   ; OUT ($BF),A
site 03E3C   ; OUT ($BF),A
site 03E43   ; OUT ($BF),A
site 03FA8   ; IN A,($BF)
site 04011   ; OUT ($BF),A
site 04017   ; OUT ($BF),A
site 04024   ; OUT ($BF),A
site 0402A   ; OUT ($BF),A
site 04035   ; OUT ($BE),A
site 0403B   ; OUT ($BE),A
site 05038   ; OUT (C),A
site 0503F   ; OUT (C),A
site 05046   ; OUT ($BE),A
site 051B6   ; OUT ($BF),A
site 051BF   ; OUT ($BF),A
site 051D6   ; OUT ($BF),A
site 051DF   ; OUT ($BF),A
site 051F6   ; OUT ($BF),A
site 051FF   ; OUT ($BF),A
site 0520D   ; OUT (C),A
site 12C7E   ; OUT ($BF),A
site 12C85   ; OUT ($BF),A
site 12E67   ; OUT ($7F),A
site 12E6B   ; OUT ($7F),A
site 12E6F   ; OUT ($7F),A
site 12E73   ; OUT ($7F),A
site 12E9D   ; OUT ($7F),A
site 12EA1   ; OUT ($7F),A
site 12EA5   ; OUT ($7F),A
site 12EA9   ; OUT ($7F),A
site 274CE   ; OUT ($7F),A
site 274E6   ; OUT ($7F),A
site 274F1   ; OUT ($7F),A
site 27501   ; OUT ($7F),A
site 27514   ; OUT ($7F),A
site 2751E   ; OUT ($7F),A
site 27527   ; OUT ($7F),A
site 27530   ; OUT ($7F),A
site 2753F   ; OUT ($7F),A
site 27562   ; OUT ($7F),A
site 2756E   ; OUT ($7F),A
site 27576   ; OUT ($7F),A
site 27582   ; OUT ($7F),A
site 2758A   ; OUT ($7F),A
site 27596   ; OUT ($7F),A
site 2EE86   ; OUT ($7F),A
site 2EE8A   ; OUT ($7F),A
plain 2EE86
plain 2EE8A
site 2EE8E   ; OUT ($7F),A
site 2EE92   ; OUT ($7F),A
site 2EEC2   ; OUT ($7F),A
site 2EECD   ; OUT ($7F),A
site 2EEFC   ; OUT ($7F),A
site 2EF0E   ; OUT ($7F),A
site 2EF16   ; OUT ($7F),A
site 2EF2E   ; OUT ($7F),A
site 2EF35   ; OUT ($7F),A
site 2F082   ; OUT ($7F),A
site 36B71   ; OUT ($BF),A
site 36B76   ; OUT ($BF),A
site 36B7C   ; OUT ($BE),A
site 3B242   ; OUT ($BF),A
site 3B249   ; OUT ($BF),A
site 3B524   ; OUT ($BF),A
site 3B52B   ; OUT ($BF),A
site 3B533   ; OUT ($BE),A
site 3B539   ; OUT ($BE),A
# The interrupt handler, run from its RAM copy at $C8E5-$CD90 (bank 15 $AB62 copied to $C000).
site 3F448   ; $C8E6 IN A,($BF)
site 3F460   ; $C8FE OUT ($BF),A
plain 3F460
site 3F467   ; $C905 OUT ($BF),A
plain 3F467
site 3F47C   ; $C91A OUT ($BF),A
plain 3F47C
site 3F482   ; $C920 OUT ($BF),A
plain 3F482
site 3F488   ; $C926 OUT ($BE),A
plain 3F488
site 3F49B   ; $C939 OUT ($BF),A
plain 3F49B
site 3F4A1   ; $C93F OUT ($BF),A
plain 3F4A1
site 3F4A7   ; $C945 OUT ($BE),A
plain 3F4A7
site 3F4AE   ; $C94C IN A,($DD)
site 3F4BB   ; $C959 IN A,($DD)
site 3F53D   ; $C9DB OUT ($BF),A
plain 3F53D
site 3F544   ; $C9E2 OUT ($BF),A
plain 3F544
site 3F559   ; $C9F7 OUT ($BF),A
plain 3F559
site 3F560   ; $C9FE OUT ($BF),A
plain 3F560
site 3F57A   ; $CA18 OUT (C),A
plain 3F57A
site 3F581   ; $CA1F OUT (C),A
plain 3F581
site 3F588   ; $CA26 OUT ($BE),A
plain 3F588
site 3F599   ; $CA37 OUT ($BF),A
plain 3F599
site 3F59D   ; $CA3B OUT ($BF),A
plain 3F59D
site 3F5B4   ; $CA52 OUTI
plain 3F5B4
site 3F5B6   ; $CA54 OUTI
plain 3F5B6
site 3F5B9   ; $CA57 OUTI
plain 3F5B9
site 3F5BB   ; $CA59 OUTI
plain 3F5BB
site 3F5BE   ; $CA5C OUTI
plain 3F5BE
site 3F5C0   ; $CA5E OUTI
plain 3F5C0
site 3F5C3   ; $CA61 OUTI
plain 3F5C3
site 3F5C5   ; $CA63 OUTI
plain 3F5C5
site 3F5C8   ; $CA66 OUTI
plain 3F5C8
site 3F5CA   ; $CA68 OUTI
plain 3F5CA
site 3F5CD   ; $CA6B OUTI
plain 3F5CD
site 3F5CF   ; $CA6D OUTI
plain 3F5CF
site 3F5D2   ; $CA70 OUTI
plain 3F5D2
site 3F5D4   ; $CA72 OUTI
plain 3F5D4
site 3F5D7   ; $CA75 OUTI
plain 3F5D7
site 3F5D9   ; $CA77 OUTI
plain 3F5D9
site 3F5DC   ; $CA7A OUTI
plain 3F5DC
site 3F5DE   ; $CA7C OUTI
plain 3F5DE
site 3F5E1   ; $CA7F OUTI
plain 3F5E1
site 3F5E3   ; $CA81 OUTI
plain 3F5E3
site 3F5E6   ; $CA84 OUTI
plain 3F5E6
site 3F5E8   ; $CA86 OUTI
plain 3F5E8
site 3F5EB   ; $CA89 OUTI
plain 3F5EB
site 3F5ED   ; $CA8B OUTI
plain 3F5ED
site 3F5F0   ; $CA8E OUTI
plain 3F5F0
site 3F5F2   ; $CA90 OUTI
plain 3F5F2
site 3F5F5   ; $CA93 OUTI
plain 3F5F5
site 3F5F7   ; $CA95 OUTI
plain 3F5F7
site 3F5FA   ; $CA98 OUTI
plain 3F5FA
site 3F5FC   ; $CA9A OUTI
plain 3F5FC
site 3F5FF   ; $CA9D OUTI
plain 3F5FF
site 3F601   ; $CA9F OUTI
plain 3F601
site 3F604   ; $CAA2 OUTI
plain 3F604
site 3F606   ; $CAA4 OUTI
plain 3F606
site 3F609   ; $CAA7 OUTI
plain 3F609
site 3F60B   ; $CAA9 OUTI
plain 3F60B
site 3F60E   ; $CAAC OUTI
plain 3F60E
site 3F610   ; $CAAE OUTI
plain 3F610
site 3F613   ; $CAB1 OUTI
plain 3F613
site 3F615   ; $CAB3 OUTI
plain 3F615
site 3F618   ; $CAB6 OUTI
plain 3F618
site 3F61A   ; $CAB8 OUTI
plain 3F61A
site 3F61D   ; $CABB OUTI
plain 3F61D
site 3F61F   ; $CABD OUTI
plain 3F61F
site 3F622   ; $CAC0 OUTI
plain 3F622
site 3F624   ; $CAC2 OUTI
plain 3F624
site 3F627   ; $CAC5 OUTI
plain 3F627
site 3F629   ; $CAC7 OUTI
plain 3F629
site 3F62C   ; $CACA OUTI
plain 3F62C
site 3F62E   ; $CACC OUTI
plain 3F62E
site 3F631   ; $CACF OUTI
plain 3F631
site 3F633   ; $CAD1 OUTI
plain 3F633
site 3F636   ; $CAD4 OUTI
plain 3F636
site 3F638   ; $CAD6 OUTI
plain 3F638
site 3F63B   ; $CAD9 OUTI
plain 3F63B
site 3F63D   ; $CADB OUTI
plain 3F63D
site 3F640   ; $CADE OUTI
plain 3F640
site 3F642   ; $CAE0 OUTI
plain 3F642
site 3F645   ; $CAE3 OUTI
plain 3F645
site 3F647   ; $CAE5 OUTI
plain 3F647
site 3F64A   ; $CAE8 OUTI
plain 3F64A
site 3F64C   ; $CAEA OUTI
plain 3F64C
site 3F64F   ; $CAED OUTI
plain 3F64F
site 3F651   ; $CAEF OUTI
plain 3F651
site 3F654   ; $CAF2 OUTI
plain 3F654
site 3F656   ; $CAF4 OUTI
plain 3F656
site 3F659   ; $CAF7 OUTI
plain 3F659
site 3F65B   ; $CAF9 OUTI
plain 3F65B
site 3F65E   ; $CAFC OUTI
plain 3F65E
site 3F660   ; $CAFE OUTI
plain 3F660
site 3F663   ; $CB01 OUTI
plain 3F663
site 3F665   ; $CB03 OUTI
plain 3F665
site 3F668   ; $CB06 OUTI
plain 3F668
site 3F66A   ; $CB08 OUTI
plain 3F66A
site 3F66D   ; $CB0B OUTI
plain 3F66D
site 3F66F   ; $CB0D OUTI
plain 3F66F
site 3F672   ; $CB10 OUTI
plain 3F672
site 3F674   ; $CB12 OUTI
plain 3F674
site 3F677   ; $CB15 OUTI
plain 3F677
site 3F679   ; $CB17 OUTI
plain 3F679
site 3F67C   ; $CB1A OUTI
plain 3F67C
site 3F67E   ; $CB1C OUTI
plain 3F67E
site 3F681   ; $CB1F OUTI
plain 3F681
site 3F683   ; $CB21 OUTI
plain 3F683
site 3F686   ; $CB24 OUTI
plain 3F686
site 3F688   ; $CB26 OUTI
plain 3F688
site 3F68B   ; $CB29 OUTI
plain 3F68B
site 3F68D   ; $CB2B OUTI
plain 3F68D
site 3F690   ; $CB2E OUTI
plain 3F690
site 3F692   ; $CB30 OUTI
plain 3F692
site 3F695   ; $CB33 OUTI
plain 3F695
site 3F697   ; $CB35 OUTI
plain 3F697
site 3F69A   ; $CB38 OUTI
plain 3F69A
site 3F69C   ; $CB3A OUTI
plain 3F69C
site 3F69F   ; $CB3D OUTI
plain 3F69F
site 3F6A1   ; $CB3F OUTI
plain 3F6A1
site 3F6A4   ; $CB42 OUTI
plain 3F6A4
site 3F6A6   ; $CB44 OUTI
plain 3F6A6
site 3F6A9   ; $CB47 OUTI
plain 3F6A9
site 3F6AB   ; $CB49 OUTI
plain 3F6AB
site 3F6AE   ; $CB4C OUTI
plain 3F6AE
site 3F6B0   ; $CB4E OUTI
plain 3F6B0
site 3F6B3   ; $CB51 OUTI
plain 3F6B3
site 3F6B5   ; $CB53 OUTI
plain 3F6B5
site 3F6B8   ; $CB56 OUTI
plain 3F6B8
site 3F6BA   ; $CB58 OUTI
plain 3F6BA
site 3F6BD   ; $CB5B OUTI
plain 3F6BD
site 3F6BF   ; $CB5D OUTI
plain 3F6BF
site 3F6C2   ; $CB60 OUTI
plain 3F6C2
site 3F6C4   ; $CB62 OUTI
plain 3F6C4
site 3F6C7   ; $CB65 OUTI
plain 3F6C7
site 3F6C9   ; $CB67 OUTI
plain 3F6C9
site 3F6CC   ; $CB6A OUTI
plain 3F6CC
site 3F6CE   ; $CB6C OUTI
plain 3F6CE
site 3F6D1   ; $CB6F OUTI
plain 3F6D1
site 3F6D3   ; $CB71 OUTI
plain 3F6D3
site 3F6D6   ; $CB74 OUTI
plain 3F6D6
site 3F6D8   ; $CB76 OUTI
plain 3F6D8
site 3F6DB   ; $CB79 OUTI
plain 3F6DB
site 3F6DD   ; $CB7B OUTI
plain 3F6DD
site 3F6E0   ; $CB7E OUTI
plain 3F6E0
site 3F6E2   ; $CB80 OUTI
plain 3F6E2
site 3F6E5   ; $CB83 OUTI
plain 3F6E5
site 3F6E7   ; $CB85 OUTI
plain 3F6E7
site 3F6EA   ; $CB88 OUTI
plain 3F6EA
site 3F6EC   ; $CB8A OUTI
plain 3F6EC
site 3F6EF   ; $CB8D OUTI
plain 3F6EF
site 3F6F1   ; $CB8F OUTI
plain 3F6F1
site 3F6F5   ; $CB93 OUT ($BF),A
plain 3F6F5
site 3F6F9   ; $CB97 OUT ($BF),A
plain 3F6F9
site 3F70C   ; $CBAA OUTI
plain 3F70C
site 3F710   ; $CBAE OUTI
plain 3F710
site 3F714   ; $CBB2 OUTI
plain 3F714
site 3F718   ; $CBB6 OUTI
plain 3F718
site 3F71C   ; $CBBA OUTI
plain 3F71C
site 3F720   ; $CBBE OUTI
plain 3F720
site 3F724   ; $CBC2 OUTI
plain 3F724
site 3F728   ; $CBC6 OUTI
plain 3F728
site 3F72C   ; $CBCA OUTI
plain 3F72C
site 3F730   ; $CBCE OUTI
plain 3F730
site 3F734   ; $CBD2 OUTI
plain 3F734
site 3F738   ; $CBD6 OUTI
plain 3F738
site 3F73C   ; $CBDA OUTI
plain 3F73C
site 3F740   ; $CBDE OUTI
plain 3F740
site 3F744   ; $CBE2 OUTI
plain 3F744
site 3F748   ; $CBE6 OUTI
plain 3F748
site 3F74C   ; $CBEA OUTI
plain 3F74C
site 3F750   ; $CBEE OUTI
plain 3F750
site 3F754   ; $CBF2 OUTI
plain 3F754
site 3F758   ; $CBF6 OUTI
plain 3F758
site 3F75C   ; $CBFA OUTI
plain 3F75C
site 3F760   ; $CBFE OUTI
plain 3F760
site 3F764   ; $CC02 OUTI
plain 3F764
site 3F768   ; $CC06 OUTI
plain 3F768
site 3F76C   ; $CC0A OUTI
plain 3F76C
site 3F770   ; $CC0E OUTI
plain 3F770
site 3F774   ; $CC12 OUTI
plain 3F774
site 3F778   ; $CC16 OUTI
plain 3F778
site 3F77C   ; $CC1A OUTI
plain 3F77C
site 3F780   ; $CC1E OUTI
plain 3F780
site 3F784   ; $CC22 OUTI
plain 3F784
site 3F788   ; $CC26 OUTI
plain 3F788
site 3F78C   ; $CC2A OUTI
plain 3F78C
site 3F790   ; $CC2E OUTI
plain 3F790
site 3F794   ; $CC32 OUTI
plain 3F794
site 3F798   ; $CC36 OUTI
plain 3F798
site 3F79C   ; $CC3A OUTI
plain 3F79C
site 3F7A0   ; $CC3E OUTI
plain 3F7A0
site 3F7A4   ; $CC42 OUTI
plain 3F7A4
site 3F7A8   ; $CC46 OUTI
plain 3F7A8
site 3F7AC   ; $CC4A OUTI
plain 3F7AC
site 3F7B0   ; $CC4E OUTI
plain 3F7B0
site 3F7B4   ; $CC52 OUTI
plain 3F7B4
site 3F7B8   ; $CC56 OUTI
plain 3F7B8
site 3F7BC   ; $CC5A OUTI
plain 3F7BC
site 3F7C0   ; $CC5E OUTI
plain 3F7C0
site 3F7C4   ; $CC62 OUTI
plain 3F7C4
site 3F7C8   ; $CC66 OUTI
plain 3F7C8
site 3F7CC   ; $CC6A OUTI
plain 3F7CC
site 3F7D0   ; $CC6E OUTI
plain 3F7D0
site 3F7D4   ; $CC72 OUTI
plain 3F7D4
site 3F7D8   ; $CC76 OUTI
plain 3F7D8
site 3F7DC   ; $CC7A OUTI
plain 3F7DC
site 3F7E0   ; $CC7E OUTI
plain 3F7E0
site 3F7E4   ; $CC82 OUTI
plain 3F7E4
site 3F7E8   ; $CC86 OUTI
plain 3F7E8
site 3F7EC   ; $CC8A OUTI
plain 3F7EC
site 3F7F0   ; $CC8E OUTI
plain 3F7F0
site 3F7F4   ; $CC92 OUTI
plain 3F7F4
site 3F7F8   ; $CC96 OUTI
plain 3F7F8
site 3F7FC   ; $CC9A OUTI
plain 3F7FC
site 3F800   ; $CC9E OUTI
plain 3F800
site 3F804   ; $CCA2 OUTI
plain 3F804
site 3F808   ; $CCA6 OUTI
plain 3F808
site 3F815   ; $CCB3 OUT (C),A
plain 3F815
site 3F858   ; $CCF6 OUT (C),A
plain 3F858
site 3F85C   ; $CCFA OUT (C),A
plain 3F85C
site 3F860   ; $CCFE OUT ($BE),A
plain 3F860
site 3F88C   ; $CD2A OUT ($BF),A
plain 3F88C
site 3F890   ; $CD2E OUT ($BF),A
plain 3F890
site 3F895   ; $CD33 OUT ($BE),A
plain 3F895
site 3F89A   ; $CD38 OUT ($BE),A
plain 3F89A
site 3F89F   ; $CD3D OUT ($BE),A
plain 3F89F
site 3F8A4   ; $CD42 OUT ($BE),A
plain 3F8A4
site 3F8A9   ; $CD47 OUT ($BE),A
plain 3F8A9
site 3F8AE   ; $CD4C OUT ($BE),A
plain 3F8AE
site 3F8B3   ; $CD51 OUT ($BE),A
plain 3F8B3
site 3F8BA   ; $CD58 OUT ($BF),A
plain 3F8BA
site 3F8BF   ; $CD5D OUT ($BF),A
plain 3F8BF
site 3F8CF   ; $CD6D OUT ($BE),A
plain 3F8CF
site 3F8E4   ; $CD82 OUT ($BF),A
plain 3F8E4
site 3F8EB   ; $CD89 OUT ($BF),A
plain 3F8EB
# Restores of the handler start: LD HL,$DBF5 becomes LD HL,$D7F5 (RST $10, the patched IN).
poke 01E3F DB D7
poke 01E6F DB D7
poke 01EEF DB D7
poke 0248A DB D7
poke 024EC DB D7
poke 03F8B DB D7
poke 04050 DB D7
poke 04AC4 DB D7
poke 04B22 DB D7
poke 04BE9 DB D7
poke 04C16 DB D7
poke 04D4B DB D7
poke 06C92 DB D7
poke 12C6C DB D7
poke 12CDA DB D7
poke 12D36 DB D7
poke 1F9FD DB D7
poke 2C68E DB D7
poke 2C6F8 DB D7
poke 2C762 DB D7
poke 2C7E6 DB D7
poke 3617C DB D7
poke 36215 DB D7
poke 372F0 DB D7
poke 3B255 DB D7
poke 3B2BC DB D7
poke 3B2FE DB D7
poke 3B471 DB D7
poke 3EA2F DB D7

# Super Space Invaders (Europe).cht, "Infinite Lives": RAM $C2EE is the lives count; held at 3 it
# does not fall and the game does not end
poke "Infinite lives"
ar 00C2-EE03
endpoke

# Super Space Invaders (Europe).cht, "Invulnerability": RAM $C2FB is a timer that the game sets
# when a life is lost; held at $35 the hit count does not fall
poke "Invulnerability"
ar 00C2-FB35
endpoke
