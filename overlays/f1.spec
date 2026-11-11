# F1 (Europe, Brazil) (En), CRC32 EC788661, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# - Started as the mkspec.py draft of a scan with hand entries (scratchpad/b7-f1/scan.sh): the
#   sound code in banks 3 and 4, mapped by RST $18 with the bank in E, and the line handler
#   chains at $7262-$736D and $7716-$77D1, reached through JP (HL) with HL' at $7261.
# - The io vector is at $00. The game's code has no RST $00, and no call or jump to $0000.
# - Unused code that no path names: the development kit's monitor ($0008, $003B, $0068-$0360),
#   $2678-$270B, $7BE5, $7CEA and $9F8A in bank 3. The cave below is in the monitor.
# - Line interrupts: the rastercode routine gives the per-line H of the title's credits row
#   and of the one-player race's road (f1-raster.asm). hsplit gives the other screens' line
#   splits (the race before the start and with the car off the road: H = 0 from line 87) the
#   right map columns.
name F1
hz 50
rastercode f1-raster.asm
hsplit
cart EC788661
# No free RST vector: $0000-$0002 (DI; LD SP part) becomes the vector,
# the game starts at $0004 with the SP its LD SP,nn set.
vector 00 io
start 0004 DFEC
label f1_r8zero 07D4D   ; register 8 = 0, register 9 = 0
label f1_vaddr 07D6E    ; VDP address = DE
label f1_letter 07B72   ; writes the letter A at the VDP address
label cv_title 00100    ; the cave below
# The title's frame handler $79D1 starts with CALL $7D4D. With the raster table on
# (register 10 = $B6, the title), the game gets no line interrupts, so the cave also does
# the work of the line handler $7A3B after its register 8 write: step the credits scroll
# ($C70D) and, every 8 steps, write the next letter from bank 4. Bank switch through the
# game's RST $18 (E = bank), as $7A40 does.
asm 079D1 3   ; CALL $7D4D
    call cv_title
endasm
asm 00100 80   ; cave in the development kit's monitor, which no path reaches
cvt:
    call f1_r8zero
    ld a,(vdp_regs+10)
    cp $B6
    ret nz
    ld a,($FFFF)
    push af
    ld e,4
    rst $18
    ld a,($C70D)
    ld c,a
    dec a
    ld ($C70D),a
    ld a,c
    and 7
    jr nz,.done
    ld hl,($C70E)
    ld a,(hl)
    and a
    jr nz,.text
    ld hl,$A1C2
.text:
    ld b,1
    ld c,$4F
    ld de,($C710)
    call f1_vaddr
    inc e
    inc e
    ld a,e
    and $3F
    or $C0
    ld e,a
    ld ($C710),de
    ld a,(hl)
    call f1_letter
    inc hl
    ld ($C70E),hl
.done:
    pop af
    ld e,a
    rst $18
    ret
endasm
asm 00396 2   ; IM 1 -> IM 2
    im 2
endasm
site 003A6   ; IN A,($BF)
site 0040E   ; IN A,($BF)
site 0146F   ; OUT ($7F),A
site 0149A   ; OUT ($7F),A
site 014A3   ; OUT ($7F),A
site 014A8   ; OUT ($7F),A
site 014D3   ; OUT ($7F),A
site 014DC   ; OUT ($7F),A
site 01652   ; OUT ($BE),A
site 01656   ; OUT ($BE),A
site 01665   ; OUT ($BE),A
site 01669   ; OUT ($BE),A
site 0166D   ; OUT ($BE),A
site 01671   ; OUT ($BE),A
site 01680   ; OUT ($BE),A
site 01684   ; OUT ($BE),A
site 01688   ; OUT ($BE),A
site 0168C   ; OUT ($BE),A
site 016A6   ; OUT ($BE),A
site 016AB   ; OUT ($BE),A
site 016B0   ; OUT ($BE),A
site 016B4   ; OUT ($BE),A
site 016C9   ; OUT ($BE),A
site 016CE   ; OUT ($BE),A
site 016D3   ; OUT ($BE),A
site 016D7   ; OUT ($BE),A
site 016F1   ; OUT ($BE),A
site 016F5   ; OUT ($BE),A
site 01734   ; OUT ($BE),A
site 01738   ; OUT ($BE),A
site 01747   ; OUT ($BE),A
site 0174B   ; OUT ($BE),A
site 0174F   ; OUT ($BE),A
site 01753   ; OUT ($BE),A
site 01762   ; OUT ($BE),A
site 01766   ; OUT ($BE),A
site 0176A   ; OUT ($BE),A
site 0176E   ; OUT ($BE),A
site 01788   ; OUT ($BE),A
site 0178D   ; OUT ($BE),A
site 01792   ; OUT ($BE),A
site 01796   ; OUT ($BE),A
site 017AB   ; OUT ($BE),A
site 017B0   ; OUT ($BE),A
site 017B5   ; OUT ($BE),A
site 017B9   ; OUT ($BE),A
site 017CF   ; OUT ($BE),A
site 017D3   ; OUT ($BE),A
site 0180F   ; OUT ($BE),A
site 01813   ; OUT ($BE),A
site 01817   ; OUT ($BE),A
site 0181B   ; OUT ($BE),A
site 01825   ; OUT ($BE),A
site 0182A   ; OUT ($BE),A
site 0182E   ; OUT ($BE),A
site 01832   ; OUT ($BE),A
site 01836   ; OUT ($BE),A
site 0183A   ; OUT ($BE),A
site 01844   ; OUT ($BE),A
site 01849   ; OUT ($BE),A
site 0184D   ; OUT ($BE),A
site 01851   ; OUT ($BE),A
site 019BD   ; OUT ($BE),A
site 019C1   ; OUT ($BE),A
otir 01F4A   ; OUTI
otir 01F7E   ; OUTI
site 01FCC   ; OTIR
site 01FD5   ; OTIR
site 01FEA   ; OTIR
site 02028   ; OUT ($BE),A
site 0202D   ; OUT ($BE),A
site 020CD   ; OTIR
site 020E9   ; OTIR
site 023E1   ; OUT ($BE),A
site 023E6   ; OUT ($BE),A
otir 02421   ; OUTI
site 02475   ; OUT ($BE),A
site 0247E   ; OUT ($BE),A
site 02496   ; OTIR
site 024D8   ; OUT ($BE),A
site 024DD   ; OUT ($BE),A
site 0323D   ; OUT ($BE),A
site 03242   ; OUT ($BE),A
site 03304   ; OUT ($7F),A
site 03354   ; OUT ($7F),A
site 03439   ; OUT ($7F),A
site 03489   ; OUT ($7F),A
site 035CA   ; OUT ($BE),A
site 035D5   ; OUT ($BE),A
site 035DE   ; OUT ($BE),A
site 0361F   ; OUT ($BE),A
site 0362A   ; OUT ($BE),A
site 03633   ; OUT ($BE),A
site 037FA   ; OUTI
site 037FC   ; OUTI
site 037FE   ; OUTI
site 03800   ; OUTI
site 03802   ; OUTI
site 03804   ; OUTI
site 03806   ; OUTI
site 03808   ; OUTI
site 0380A   ; OUTI
site 0380C   ; OUTI
site 0380E   ; OUTI
site 03810   ; OUTI
site 03812   ; OUTI
site 03814   ; OUTI
site 03816   ; OUTI
site 03818   ; OUTI
site 0381A   ; OUTI
site 0381C   ; OUTI
site 0381E   ; OUTI
site 03820   ; OUTI
site 03822   ; OUTI
site 03824   ; OUTI
site 03826   ; OUTI
site 03828   ; OUTI
site 0382A   ; OUTI
site 0382C   ; OUTI
site 0382E   ; OUTI
site 03830   ; OUTI
site 03832   ; OUTI
site 03834   ; OUTI
site 03836   ; OUTI
site 03838   ; OUTI
site 03879   ; OUT ($BE),A
site 0387E   ; OUT ($BE),A
site 03883   ; OUT ($BE),A
site 03888   ; OUT ($BE),A
site 0388D   ; OUT ($BE),A
site 03892   ; OUT ($BE),A
site 03897   ; OUT ($BE),A
site 0389C   ; OUT ($BE),A
site 038A1   ; OUT ($BE),A
site 038A6   ; OUT ($BE),A
site 038AB   ; OUT ($BE),A
site 038B0   ; OUT ($BE),A
site 038B5   ; OUT ($BE),A
site 038BA   ; OUT ($BE),A
site 038BF   ; OUT ($BE),A
site 038C4   ; OUT ($BE),A
site 038C9   ; OUT ($BE),A
site 038CE   ; OUT ($BE),A
site 038D3   ; OUT ($BE),A
site 038D8   ; OUT ($BE),A
site 038DD   ; OUT ($BE),A
site 038E2   ; OUT ($BE),A
site 038E7   ; OUT ($BE),A
site 038EC   ; OUT ($BE),A
site 038F1   ; OUT ($BE),A
site 038F6   ; OUT ($BE),A
site 038FB   ; OUT ($BE),A
site 03900   ; OUT ($BE),A
site 03905   ; OUT ($BE),A
site 0390A   ; OUT ($BE),A
site 0390F   ; OUT ($BE),A
site 03914   ; OUT ($BE),A
site 0393C   ; OUTI
site 0393E   ; OUTI
site 03940   ; OUTI
site 03942   ; OUTI
site 03944   ; OUTI
site 03946   ; OUTI
site 03948   ; OUTI
site 0394A   ; OUTI
site 0394C   ; OUTI
site 0394E   ; OUTI
site 03950   ; OUTI
site 03952   ; OUTI
site 03954   ; OUTI
site 03956   ; OUTI
site 03958   ; OUTI
site 0395A   ; OUTI
site 0395C   ; OUTI
site 0395E   ; OUTI
site 03960   ; OUTI
site 03962   ; OUTI
site 03964   ; OUTI
site 03966   ; OUTI
site 03968   ; OUTI
site 0396A   ; OUTI
site 0396C   ; OUTI
site 0396E   ; OUTI
site 03970   ; OUTI
site 03972   ; OUTI
site 03974   ; OUTI
site 03976   ; OUTI
site 03978   ; OUTI
site 0397A   ; OUTI
site 0397C   ; OUTI
site 0397E   ; OUTI
site 03980   ; OUTI
site 03982   ; OUTI
site 03984   ; OUTI
site 03986   ; OUTI
site 03988   ; OUTI
site 0398A   ; OUTI
site 0398C   ; OUTI
site 0398E   ; OUTI
site 03990   ; OUTI
site 03992   ; OUTI
site 03994   ; OUTI
site 03996   ; OUTI
site 03998   ; OUTI
site 0399A   ; OUTI
site 0399C   ; OUTI
site 0399E   ; OUTI
site 039A0   ; OUTI
site 039A2   ; OUTI
site 039A4   ; OUTI
site 039A6   ; OUTI
site 039A8   ; OUTI
site 039AA   ; OUTI
site 039AC   ; OUTI
site 039AE   ; OUTI
site 039B0   ; OUTI
site 039B2   ; OUTI
site 039B4   ; OUTI
site 039B6   ; OUTI
site 039B8   ; OUTI
site 039BA   ; OUTI
site 039C7   ; OUT ($BE),A
site 039CC   ; OUT ($BE),A
site 039D1   ; OUT ($BE),A
site 039D6   ; OUT ($BE),A
site 039DB   ; OUT ($BE),A
site 039E0   ; OUT ($BE),A
site 039E5   ; OUT ($BE),A
site 039EA   ; OUT ($BE),A
site 039EF   ; OUT ($BE),A
site 039F4   ; OUT ($BE),A
site 039F9   ; OUT ($BE),A
site 039FE   ; OUT ($BE),A
site 03A03   ; OUT ($BE),A
site 03A08   ; OUT ($BE),A
site 03A0D   ; OUT ($BE),A
site 03A12   ; OUT ($BE),A
site 03A17   ; OUT ($BE),A
site 03A1C   ; OUT ($BE),A
site 03A21   ; OUT ($BE),A
site 03A26   ; OUT ($BE),A
site 03A2B   ; OUT ($BE),A
site 03A30   ; OUT ($BE),A
site 03A35   ; OUT ($BE),A
site 03A3A   ; OUT ($BE),A
site 03A3F   ; OUT ($BE),A
site 03A44   ; OUT ($BE),A
site 03A49   ; OUT ($BE),A
site 03A4E   ; OUT ($BE),A
site 03A53   ; OUT ($BE),A
site 03A58   ; OUT ($BE),A
site 03A5D   ; OUT ($BE),A
site 03A62   ; OUT ($BE),A
site 03A67   ; OUT ($BE),A
site 03A6C   ; OUT ($BE),A
site 03A71   ; OUT ($BE),A
site 03A76   ; OUT ($BE),A
site 03A7B   ; OUT ($BE),A
site 03A80   ; OUT ($BE),A
site 03A85   ; OUT ($BE),A
site 03A8A   ; OUT ($BE),A
site 03A8F   ; OUT ($BE),A
site 03A94   ; OUT ($BE),A
site 03A99   ; OUT ($BE),A
site 03A9E   ; OUT ($BE),A
site 03AA3   ; OUT ($BE),A
site 03AA8   ; OUT ($BE),A
site 03AAD   ; OUT ($BE),A
site 03AB2   ; OUT ($BE),A
site 03AB7   ; OUT ($BE),A
site 03ABC   ; OUT ($BE),A
site 03AC1   ; OUT ($BE),A
site 03AC6   ; OUT ($BE),A
site 03ACB   ; OUT ($BE),A
site 03AD0   ; OUT ($BE),A
site 03AD5   ; OUT ($BE),A
site 03ADA   ; OUT ($BE),A
site 03ADF   ; OUT ($BE),A
site 03AE4   ; OUT ($BE),A
site 03AE9   ; OUT ($BE),A
site 03AEE   ; OUT ($BE),A
site 03AF3   ; OUT ($BE),A
site 03AF8   ; OUT ($BE),A
site 03AFD   ; OUT ($BE),A
site 03B02   ; OUT ($BE),A
site 03B17   ; OUT ($BE),A
site 03B1D   ; OUT ($BE),A
site 03B2E   ; OUT ($BE),A
site 03B34   ; OUT ($BE),A
site 03B45   ; OUT ($BE),A
site 03B4C   ; OUT ($BE),A
site 04624   ; OUT ($BE),A
site 04636   ; OUT ($BE),A
site 0463D   ; OUT ($BE),A
site 04CFB   ; OUT ($BE),A
site 04D01   ; OUT ($BE),A
site 04D34   ; OUT ($BE),A
site 04D3A   ; OUT ($BE),A
site 04D40   ; OUT ($BE),A
site 04D46   ; OUT ($BE),A
site 04D4E   ; OUT ($BE),A
site 04D54   ; OUT ($BE),A
site 04D6A   ; OUT ($BE),A
site 04D70   ; OUT ($BE),A
site 04D81   ; OUT ($BE),A
site 04D87   ; OUT ($BE),A
site 04D91   ; OUT ($BE),A
site 04D97   ; OUT ($BE),A
site 04D9F   ; OUT ($BE),A
site 04DA5   ; OUT ($BE),A
site 04DBE   ; OUT ($BE),A
site 04DC5   ; OUT ($BE),A
site 05E2C   ; OUT ($7F),A
site 05F6F   ; OUT ($7F),A
site 05F73   ; OUT ($7F),A
site 060A9   ; OUT ($7F),A
site 06792   ; OUT ($BE),A
otir 06813   ; OUTI
site 06840   ; OUT ($BE),A
site 06846   ; OUT ($BE),A
site 06882   ; OUT ($BE),A
site 068E3   ; OUT ($BE),A
site 068E9   ; OUT ($BE),A
site 06913   ; OUT ($BF),A
site 06919   ; OUT ($BF),A
site 06934   ; OUT ($BF),A
site 0693A   ; OUT ($BF),A
site 06A14   ; OUT ($7F),A
site 06A18   ; OUT ($7F),A
site 06A1C   ; OUT ($7F),A
site 06A37   ; OUT ($7F),A
site 06A53   ; OUT ($7F),A
site 06A66   ; OUT ($7F),A
site 06A74   ; OUT ($7F),A
site 06A7B   ; OUT ($7F),A
site 06A8D   ; OUT ($7F),A
site 06AA9   ; OUT ($7F),A
site 06AD4   ; OUT ($7F),A
site 06AD8   ; OUT ($7F),A
site 06ADD   ; OUT ($7F),A
site 06AE2   ; OUT ($7F),A
site 06B0A   ; OUT ($7F),A
site 06B0E   ; OUT ($7F),A
site 06B3A   ; OUT ($7F),A
site 06B46   ; OUT ($7F),A
site 06B53   ; OUT ($7F),A
site 06B5C   ; OUT ($7F),A
site 06B69   ; OUT ($7F),A
site 06B72   ; OUT ($7F),A
site 06B76   ; OUT ($7F),A
site 06B8F   ; OUT ($7F),A
site 06BA9   ; IN A,($BF)
site 06C6E   ; OUT ($BF),A
site 06C72   ; OUT ($BF),A
site 06CA5   ; OUTI
site 06CA7   ; OUTI
site 06CB2   ; OUTI
site 06CB4   ; OUTI
site 06CB6   ; OUTI
site 06CB8   ; OUTI
site 06D88   ; OUT ($BE),A
site 06D8C   ; OUT ($BE),A
site 06DAF   ; OUT ($BE),A
site 06DB3   ; OUT ($BE),A
site 06DC9   ; IN A,($DD)
site 06DD6   ; IN A,($DC)
site 06DDE   ; IN A,($DD)
site 06DFD   ; IN A,($DD)
site 06E12   ; OUT ($BF),A
site 06E16   ; OUT ($BF),A
site 06E36   ; OUT ($BE),A
site 06E3D   ; OUT ($BE),A
site 06E4C   ; OUT ($BE),A
site 06E53   ; OUT ($BE),A
site 06E64   ; OUT ($BE),A
site 06E6B   ; OUT ($BE),A
site 06E7A   ; OUT ($BE),A
site 06E81   ; OUT ($BE),A
site 06F5A   ; OUT ($BE),A
site 06F6F   ; OTIR
otir 06F88   ; OUTI
otir 06F99   ; OUTI
site 06FA4   ; IN A,($DD)
site 06FAE   ; OUT ($BF),A
site 06FB2   ; OUT ($BF),A
site 070A8   ; OUT ($BF),A
site 070AC   ; OUT ($BF),A
site 070C3   ; OUT ($BE),A
site 07140   ; OUT ($BE),A
site 07144   ; OUT ($BE),A
site 0714C   ; IN A,($DD)
site 07197   ; OUT ($BE),A
site 0719E   ; OUT ($BE),A
site 071B4   ; OUT ($BE),A
site 071BB   ; OUT ($BE),A
site 071F5   ; OUT ($BE),A
site 071FC   ; OUT ($BE),A
site 07212   ; OUT ($BE),A
site 07219   ; OUT ($BE),A
site 07231   ; IN A,($BF)
site 07262   ; OUT ($BF),A
site 07268   ; OUT ($BF),A
site 0727A   ; OUT ($BF),A
site 07280   ; OUT ($BF),A
site 07286   ; OUT ($BF),A
site 0728C   ; OUT ($BF),A
site 07296   ; OUT ($BF),A
site 0729C   ; OUT ($BF),A
site 072A5   ; OUT ($BF),A
site 072AB   ; OUT ($BF),A
site 072B4   ; OUT ($BF),A
site 072BA   ; OUT ($BF),A
site 072D6   ; OUT ($BE),A
site 072E8   ; OUT ($BE),A
site 072FF   ; OUT ($BE),A
site 07316   ; OUT ($BE),A
site 0732D   ; OUT ($BE),A
site 07344   ; OUT ($BE),A
site 0735B   ; OUT ($BE),A
site 07362   ; OUT ($BF),A
site 07368   ; OUT ($BF),A
site 07376   ; OUT ($BE),A
site 07383   ; OUT ($BE),A
site 07388   ; OUT ($BE),A
site 0738D   ; OUT ($BE),A
site 07392   ; OUT ($BE),A
site 07397   ; OUT ($BE),A
site 0739C   ; OUT ($BE),A
site 073A1   ; OUT ($BE),A
site 073A6   ; OUT ($BE),A
site 073AB   ; OUT ($BE),A
site 073B0   ; OUT ($BE),A
site 073B5   ; OUT ($BE),A
site 073BA   ; OUT ($BE),A
site 073BF   ; OUT ($BE),A
site 073C4   ; OUT ($BE),A
site 073C9   ; OUT ($BE),A
site 073CE   ; OUT ($BE),A
site 073D3   ; OUT ($BE),A
site 073D8   ; OUT ($BE),A
site 073DD   ; OUT ($BE),A
site 073E2   ; OUT ($BE),A
site 073E7   ; OUT ($BE),A
site 073EC   ; OUT ($BE),A
site 073F1   ; OUT ($BE),A
site 073F6   ; OUT ($BE),A
site 073FB   ; OUT ($BE),A
site 07400   ; OUT ($BE),A
site 07405   ; OUT ($BE),A
site 0740A   ; OUT ($BE),A
site 0740F   ; OUT ($BE),A
site 07414   ; OUT ($BE),A
site 07419   ; OUT ($BE),A
site 0741E   ; OUT ($BE),A
site 07423   ; OUT ($BE),A
site 07428   ; OUT ($BE),A
site 0742D   ; OUT ($BE),A
site 07432   ; OUT ($BE),A
site 07437   ; OUT ($BE),A
site 0743C   ; OUT ($BE),A
site 07441   ; OUT ($BE),A
site 07446   ; OUT ($BE),A
site 0744B   ; OUT ($BE),A
site 07450   ; OUT ($BE),A
site 07455   ; OUT ($BE),A
site 0745A   ; OUT ($BE),A
site 0745F   ; OUT ($BE),A
site 07464   ; OUT ($BE),A
site 07469   ; OUT ($BE),A
site 0746E   ; OUT ($BE),A
site 07473   ; OUT ($BE),A
site 07478   ; OUT ($BE),A
site 0747D   ; OUT ($BE),A
site 07482   ; OUT ($BE),A
site 07487   ; OUT ($BE),A
site 0748C   ; OUT ($BE),A
site 07491   ; OUT ($BE),A
site 07496   ; OUT ($BE),A
site 0749B   ; OUT ($BE),A
site 074A0   ; OUT ($BE),A
site 074A5   ; OUT ($BE),A
site 074AA   ; OUT ($BE),A
site 074B9   ; OUT ($BE),A
site 074BE   ; OUT ($BE),A
site 074C3   ; OUT ($BE),A
site 074C8   ; OUT ($BE),A
site 074CD   ; OUT ($BE),A
site 074D2   ; OUT ($BE),A
site 074D7   ; OUT ($BE),A
site 074DC   ; OUT ($BE),A
site 074E1   ; OUT ($BE),A
site 074E6   ; OUT ($BE),A
site 074EB   ; OUT ($BE),A
site 074F0   ; OUT ($BE),A
site 074F5   ; OUT ($BE),A
site 074FA   ; OUT ($BE),A
site 074FF   ; OUT ($BE),A
site 07504   ; OUT ($BE),A
site 07509   ; OUT ($BE),A
site 0750E   ; OUT ($BE),A
site 07513   ; OUT ($BE),A
site 07518   ; OUT ($BE),A
site 0751D   ; OUT ($BE),A
site 07522   ; OUT ($BE),A
site 07527   ; OUT ($BE),A
site 0752C   ; OUT ($BE),A
site 07531   ; OUT ($BE),A
site 07536   ; OUT ($BE),A
site 0753B   ; OUT ($BE),A
site 07540   ; OUT ($BE),A
site 07545   ; OUT ($BE),A
site 0754A   ; OUT ($BE),A
site 0754F   ; OUT ($BE),A
site 07554   ; OUT ($BE),A
site 07559   ; OUT ($BE),A
site 0755E   ; OUT ($BE),A
site 07563   ; OUT ($BE),A
site 07568   ; OUT ($BE),A
site 0756D   ; OUT ($BE),A
site 07572   ; OUT ($BE),A
site 07577   ; OUT ($BE),A
site 0757C   ; OUT ($BE),A
site 07581   ; OUT ($BE),A
site 07586   ; OUT ($BE),A
site 0758B   ; OUT ($BE),A
site 07590   ; OUT ($BE),A
site 07595   ; OUT ($BE),A
site 0759A   ; OUT ($BE),A
site 0759F   ; OUT ($BE),A
site 075A4   ; OUT ($BE),A
site 075A9   ; OUT ($BE),A
site 075AE   ; OUT ($BE),A
site 075B3   ; OUT ($BE),A
site 075B8   ; OUT ($BE),A
site 075BD   ; OUT ($BE),A
site 075C2   ; OUT ($BE),A
site 075C7   ; OUT ($BE),A
site 075CC   ; OUT ($BE),A
site 075D1   ; OUT ($BE),A
site 075D6   ; OUT ($BE),A
site 075DB   ; OUT ($BE),A
site 075E0   ; OUT ($BE),A
site 075E5   ; OUT ($BE),A
site 075EA   ; OUT ($BE),A
site 075EF   ; OUT ($BE),A
site 075F4   ; OUT ($BE),A
site 075F9   ; OUT ($BE),A
site 075FE   ; OUT ($BE),A
site 07603   ; OUT ($BE),A
site 07608   ; OUT ($BE),A
site 0760D   ; OUT ($BE),A
site 07612   ; OUT ($BE),A
site 07617   ; OUT ($BE),A
site 0761C   ; OUT ($BE),A
site 07621   ; OUT ($BE),A
site 07626   ; OUT ($BE),A
site 0762B   ; OUT ($BE),A
site 07630   ; OUT ($BE),A
site 07635   ; OUT ($BE),A
site 0763A   ; OUT ($BE),A
site 0763F   ; OUT ($BE),A
site 07644   ; OUT ($BE),A
site 07649   ; OUT ($BE),A
site 0764E   ; OUT ($BE),A
site 07653   ; OUT ($BE),A
site 07658   ; OUT ($BE),A
site 0765D   ; OUT ($BE),A
site 07662   ; OUT ($BE),A
site 07667   ; OUT ($BE),A
site 0766C   ; OUT ($BE),A
site 07671   ; OUT ($BE),A
site 07676   ; OUT ($BE),A
site 0767B   ; OUT ($BE),A
site 07680   ; OUT ($BE),A
site 07685   ; OUT ($BE),A
site 0768A   ; OUT ($BE),A
site 0768F   ; OUT ($BE),A
site 07694   ; OUT ($BE),A
site 07699   ; OUT ($BE),A
site 0769E   ; OUT ($BE),A
site 076A3   ; OUT ($BE),A
site 076A8   ; OUT ($BE),A
site 076AD   ; OUT ($BE),A
site 076B2   ; OUT ($BE),A
site 076B7   ; OUT ($BE),A
site 076BC   ; OUT ($BE),A
site 076C1   ; OUT ($BE),A
site 076C6   ; OUT ($BE),A
site 076CB   ; OUT ($BE),A
site 076D0   ; OUT ($BE),A
site 076D5   ; OUT ($BE),A
site 076DA   ; OUT ($BE),A
site 076DF   ; OUT ($BE),A
site 076E4   ; OUT ($BE),A
site 076E9   ; OUT ($BE),A
site 076EE   ; OUT ($BE),A
site 076F3   ; OUT ($BE),A
site 076F8   ; OUT ($BE),A
site 076FD   ; OUT ($BE),A
site 07702   ; OUT ($BE),A
site 07707   ; OUT ($BE),A
site 0770C   ; OUT ($BE),A
site 07719   ; OUT ($BF),A
site 0771F   ; OUT ($BF),A
site 0772E   ; OUT ($BF),A
site 07734   ; OUT ($BF),A
site 07740   ; OUT ($BF),A
site 07746   ; OUT ($BF),A
site 0774E   ; OUT ($BF),A
site 07754   ; OUT ($BF),A
site 07760   ; OUT ($BF),A
site 07766   ; OUT ($BF),A
site 0776E   ; OUT ($BF),A
site 07774   ; OUT ($BF),A
site 0777D   ; OUT ($BF),A
site 07783   ; OUT ($BF),A
site 0778C   ; OUT ($BF),A
site 07792   ; OUT ($BF),A
site 077A1   ; OUT ($BF),A
site 077A7   ; OUT ($BF),A
site 077AD   ; OUT ($BF),A
site 077B3   ; OUT ($BF),A
site 077BE   ; OUT ($BF),A
site 077C4   ; OUT ($BF),A
site 077D1   ; OUT ($BF),A
site 077D7   ; OUT ($BF),A
site 079D4   ; IN A,($DD)
site 079E2   ; IN A,($DC)
site 079EB   ; IN A,($DD)
site 07A47   ; OUT ($BF),A
site 07A4D   ; OUT ($BF),A
site 07AA6   ; OUT ($BE),A
site 07AEF   ; OUT ($BE),A
site 07AF8   ; OUT ($BE),A
site 07B0E   ; OUT ($BE),A
site 07B25   ; OUT ($BE),A
site 07B2B   ; OUT ($BE),A
site 07B38   ; OUT ($BE),A
site 07B3F   ; OUT ($BE),A
site 07B73   ; OUT ($BE),A
site 07B7B   ; OUT ($BE),A
site 07BA5   ; OUT ($BF),A
site 07BAB   ; OUT ($BF),A
site 07BB6   ; OUT ($BE),A
site 07BD3   ; OUT ($BE),A
site 07BDB   ; OUT ($BF),A
site 07BE1   ; OUT ($BF),A
site 07C85   ; OUT ($BE),A
site 07C8A   ; IN A,($DD)
site 07CDD   ; OUT ($BE),A
site 07CE2   ; OUT ($BE),A
site 07D0D   ; OUT ($BE),A
site 07D13   ; OUT ($BE),A
site 07D27   ; OUT ($BE),A
site 07D32   ; OUT ($BE),A
site 07D4E   ; OUT ($BF),A
site 07D54   ; OUT ($BF),A
site 07D57   ; OUT ($BF),A
site 07D5D   ; OUT ($BF),A
site 07D6F   ; OUT ($BF),A
site 07D75   ; OUT ($BF),A
site 07D79   ; IN A,($BF)
site 07D87   ; OUT ($BF),A
site 07D8D   ; OUT ($BF),A
site 07D9C   ; OUT ($BE),A
site 07DB0   ; OUT ($BF),A
site 07DBA   ; OUT ($BF),A
site 07DCA   ; IN A,($DC)
site 07DD1   ; IN A,($DC)
site 07DD5   ; IN A,($DD)
site 07DE3   ; IN A,($DC)
site 07DE7   ; IN A,($DD)
site 07E89   ; OTIR
site 0DCBC   ; OUT ($7F),A
site 0DCC0   ; OUT ($7F),A
site 0DCC4   ; OUT ($7F),A
site 0DCC8   ; OUT ($7F),A
site 0DE1E   ; OUT ($7F),A
site 0DE2B   ; OUT ($7F),A
site 0DE4B   ; OUT ($7F),A
site 0DE5C   ; OUT ($7F),A
site 0DE6D   ; OUT ($7F),A
site 0DE7E   ; OUT ($7F),A
site 0DF41   ; OUT ($7F),A
site 12436   ; OUT ($BE),A
site 1243C   ; OUT ($BE),A
site 12464   ; OUT ($BE),A
site 12469   ; OUT ($BE),A
mapst 00056   ; LD ($FFFF),A
mapst 00398   ; LD ($FFFC),A
mapst 0039B   ; LD ($FFFD),A
mapst 0039F   ; LD ($FFFE),A
mapst 003A3   ; LD ($FFFF),A
mapst 06DF0   ; LD ($FFFF),A
mapst 07159   ; LD ($FFFF),A
mapst 07A2A   ; LD ($FFFF),A
mapst 07A83   ; LD ($FFFF),A

# F1 (Europe, Brazil).cht, "Position Modifier": RAM $C992 is the player's race position
# that the status panel shows (P); the code holds it at the value the player sets
poke "Race position"
ar 00C9-92??
endpoke

# F1 (Europe, Brazil).cht, "Freeze Lap Timer - 1P Race" ($C8BB), "P1 Freeze Lap Timer -
# 2P Race" ($C8AB) and "P2 Freeze Lap Timer - 2P Race" ($C8BB): RAM $C8AB and $C8BB are the
# hundredths counters of the lap clocks of player 1 and player 2 (a one player race uses
# $C8BB); held at 0 the clock does not run
poke "Freeze lap timer"
ar 00C8-AB00
ar 00C8-BB00
endpoke
