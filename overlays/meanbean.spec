# Dr. Robotnik's Mean Bean Machine (Europe, Brazil) (En), CRC32 6C696221, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with two 10-minute reference I/O logs (random
# input from the title; a scripted scenario game) and entry points for the game's VDP library
# in bank 0 ($2732-$29EB, one routine after each RET) and its callers that no path reached
# ($2CE5, $4D49; $8E25, $929E, $92A7, $A319, $A322 in bank 2). Most of the game's code runs
# from object handlers that $26A2 reaches by JP (HL) from RAM, so the static pass alone finds
# little of it. The unrolled OUTI run $3301-$34FF is patched whole: the game enters it at $3401,
# $3481 and $34C1.
# Spec gaps (data/scan-verdicts.tsv): false are graphics data in banks 7, 9, 10 and 11 and an
# operand in bank 2. The CHECK low lines below are byte patterns that were not judged.
name Dr. Robotnik's Mean Bean Machine
cart 6C696221
hz 50		; No-Intro regions Europe, Brazil
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
# Well drawer $81F1 in bank 2 (the row loop $8222-$82E1), as native code in page 0 (entry well).
# It writes a player's well to the name table: 13 rows of 6 cells, 2 bytes a cell, 64 bytes
# apart in VRAM, from the bean grid at HL. Each cell's word comes from the grid byte: empty
# ($08A0), a bean ($1F + the byte, high byte ($D1DD)), a bean that pops (the frame table at
# $81E0 in bank 2) or a garbage bean ($FF, the table at $826F). Through the traps it cost about
# 320,000 Next cycles a frame while beans pop (two single OUTs a cell), and the game lost a frame
# in three.
asm 08222 6    ; XOR A; LD ($D4B9),A; LD B,$0D, up to the row loop
    rst $00
    db far_io, pg_well, ent_well
    ret
endasm
page 0 well
; well: HL = the grid byte before the first row, DE = the VRAM address of the first cell. Does
; what the game's loop at $8222-$82E1 does: ($D4B9) = 0; for each of 13 rows, 6 cells from
; (HL + 1), the grid pointer stepping one byte a cell and one more at the end of a row, the
; address in ($D1FA) as the game keeps it; ($D4B9) = 1 and the pop frame counter stepped as the
; game does. The 13 rows of 12 bytes go to VRAM in one jt_vwrite call. Runs with interrupts off,
; on its own stack. Returns HL and DE as the game's loop leaves them, B = 0, C kept, Z set.
; Runtime entries used: jt_vwrite.
well:   ld a,i                  ; P/V = the game's interrupt state
        di
        ld a,0
        jp po,.ie
        inc a
.ie:    ld (sv_ie),a
        ld (sv_sp),sp
        ld sp,pstk
        push ix
        push iy
        push bc
        ld (sv_de),de
        xor a
        ld ($D4B9),a
        ld iy,buf
        ld c,13
.row:   inc hl
        ld b,6
.cell:  ld ($D1FA),hl
        ld a,(hl)
        and a
        jr z,.empty
        and $7F
        cp $5E
        jr z,.bean
        cp $51
        jr z,.bean
        ld a,(hl)
        cp $FF
        jr nz,.pop
        ld d,$10                ; garbage bean
        ld a,($D401)
        or a
        jr nz,.g1
        ld d,$18
.g1:    ld a,($DBD2)
        cp $02
        jr nz,.g2
        ld de,$10A7
        jr .put
.g2:    push hl
        ld hl,$826F
        ld a,b
        add a,l
        ld l,a
        adc a,h
        sub l
        ld h,a
        ld e,(hl)
        pop hl
        ld a,$01
        or d
        ld d,a
        jr .put
.empty: ld de,$08A0
        jr .put
.pop:   push hl                 ; the game's $827B: the pop frame counter 152 bytes back
        ld de,$FF68
        add hl,de
        ld a,(hl)
        and a
        jr z,.pop0
        inc a
        and $0F
        ld (hl),a
        ld hl,$D4B9
        ld (hl),$01
        ld e,a
        ld d,$00
        ld hl,$81E0
        add hl,de
        ld e,(hl)
        pop hl
        ld a,(hl)
        and $70
        srl a
        srl a
        add a,e
        add a,$80
        jr .hi
.pop0:  pop hl
.bean:  ld a,(hl)               ; the game's $82A4
        bit 7,a
        jr z,.b1
        ld a,($D1D7)
        and a
        jr z,.empty
        ld a,(hl)
        and $7F
.b1:    add a,$1F
.hi:    ld e,a
        ld a,($D1DD)
        ld d,a
.put:   ld (iy+0),e
        ld (iy+1),d
        inc iy
        inc iy
        inc hl
        dec b
        jp nz,.cell
        inc hl                  ; the game's INC HL at the end of a row
        dec c
        jp nz,.row
        ld (sv_hl),hl
        ld hl,buf
        ld de,(sv_de)
        ld b,12
        ld c,13
        ld ix,12
        ld iy,$40
        ld a,1                  ; the source as mapped now: buf is in this page
        call jt_vwrite
        ld hl,(sv_de)           ; DE as the game's loop leaves it: 13 rows on
        ld de,13*$40
        add hl,de
        ex de,hl
        ld hl,(sv_hl)
        pop bc
        ld b,0
        pop iy
        pop ix
        ld sp,(sv_sp)
        ld a,(sv_ie)
        or a
        jr z,.di
        xor a                   ; Z set, as the game's last DEC B leaves it
        ei
        ret
.di:    xor a
        ret
sv_ie:  db 0
sv_sp:  dw 0
sv_de:  dw 0
sv_hl:  dw 0
buf:    ds 13*12
        ds 64
pstk:
endpage
site 0003A   ; IN A,($BF)
site 00085   ; OUT ($3F),A
site 0270C   ; OUT (C),A
site 0270E   ; OUT (C),B
site 0272B   ; IN A,($7E)
site 02736   ; IN A,($BF)
site 02738   ; IN A,($BF)
site 02744   ; IN A,($BF)
site 0275D   ; OUT ($BE),A
site 0276D   ; OUT ($BE),A
site 02772   ; OUT ($BE),A
site 0279F   ; OUT ($BE),A
site 027D2   ; OUT (C),A
site 027D8   ; OUT (C),A
site 027F6   ; OUT (C),A
site 027FD   ; OUT (C),A
site 02819   ; IN A,(C)
site 0281F   ; OUT (C),H
site 02899   ; IN A,(C)
site 028A0   ; OUT (C),A
site 028E3   ; OUT (C),E
site 028E5   ; OUT (C),D
site 028E7   ; OUT ($BE),A
site 028F7   ; OUT (C),E
site 028F9   ; OUT (C),D
site 028FB   ; OUT ($BE),A
site 02908   ; OUT (C),E
site 0290A   ; OUT (C),D
site 02915   ; OUT ($BE),A
site 02945   ; OUT (C),L
site 02947   ; OUT (C),H
site 0294C   ; IN A,($BE)
site 02950   ; OUT (C),E
site 02952   ; OUT (C),D
site 02954   ; OUT ($BE),A
site 02961   ; OUT ($BF),A
site 02969   ; OUT ($BF),A
site 02970   ; OUT ($BF),A
site 02978   ; OUT ($BF),A
site 0297E   ; OUT ($BF),A
site 02987   ; OUT ($BF),A
site 02996   ; OUT ($BF),A
site 0299A   ; OUT ($BF),A
site 029A5   ; OUT ($BF),A
site 029A9   ; OUT ($BF),A
site 029B4   ; OUT ($BF),A
site 029B8   ; OUT ($BF),A
site 029C3   ; OUT ($BF),A
site 029C7   ; OUT ($BF),A
site 029CC   ; OUT ($BF),A
site 029D0   ; OUT ($BF),A
site 029D5   ; OUT ($BF),A
site 029D9   ; OUT ($BF),A
site 029E4   ; OUT ($BF),A
site 029E8   ; OUT ($BF),A
site 029F3   ; OUT ($BF),A
site 029F7   ; OUT ($BF),A
site 029F9   ; IN A,($BF)
site 02B25   ; OUT ($BF),A
site 02B29   ; OUT ($BF),A
site 02B38   ; IN A,($DC)
site 02B7D   ; IN A,($DC)
site 02B84   ; IN A,($DD)
site 02BCC   ; IN A,($DD)
site 02CF0   ; IN A,($BE)
site 0328E   ; OUT ($BF),A
site 03292   ; OUT ($BF),A
site 0329D   ; OUT ($BF),A
site 032A1   ; OUT ($BF),A
site 03401   ; OUTI
site 03403   ; OUTI
site 03405   ; OUTI
site 03407   ; OUTI
site 03409   ; OUTI
site 0340B   ; OUTI
site 0340D   ; OUTI
site 0340F   ; OUTI
site 03411   ; OUTI
site 03413   ; OUTI
site 03415   ; OUTI
site 03417   ; OUTI
site 03419   ; OUTI
site 0341B   ; OUTI
site 0341D   ; OUTI
site 0341F   ; OUTI
site 03421   ; OUTI
site 03423   ; OUTI
site 03425   ; OUTI
site 03427   ; OUTI
site 03429   ; OUTI
site 0342B   ; OUTI
site 0342D   ; OUTI
site 0342F   ; OUTI
site 03431   ; OUTI
site 03433   ; OUTI
site 03435   ; OUTI
site 03437   ; OUTI
site 03439   ; OUTI
site 0343B   ; OUTI
site 0343D   ; OUTI
site 0343F   ; OUTI
site 03441   ; OUTI
site 03443   ; OUTI
site 03445   ; OUTI
site 03447   ; OUTI
site 03449   ; OUTI
site 0344B   ; OUTI
site 0344D   ; OUTI
site 0344F   ; OUTI
site 03451   ; OUTI
site 03453   ; OUTI
site 03455   ; OUTI
site 03457   ; OUTI
site 03459   ; OUTI
site 0345B   ; OUTI
site 0345D   ; OUTI
site 0345F   ; OUTI
site 03461   ; OUTI
site 03463   ; OUTI
site 03465   ; OUTI
site 03467   ; OUTI
site 03469   ; OUTI
site 0346B   ; OUTI
site 0346D   ; OUTI
site 0346F   ; OUTI
site 03471   ; OUTI
site 03473   ; OUTI
site 03475   ; OUTI
site 03477   ; OUTI
site 03479   ; OUTI
site 0347B   ; OUTI
site 0347D   ; OUTI
site 0347F   ; OUTI
site 03481   ; OUTI
site 03483   ; OUTI
site 03485   ; OUTI
site 03487   ; OUTI
site 03489   ; OUTI
site 0348B   ; OUTI
site 0348D   ; OUTI
site 0348F   ; OUTI
site 03491   ; OUTI
site 03493   ; OUTI
site 03495   ; OUTI
site 03497   ; OUTI
site 03499   ; OUTI
site 0349B   ; OUTI
site 0349D   ; OUTI
site 0349F   ; OUTI
site 034A1   ; OUTI
site 034A3   ; OUTI
site 034A5   ; OUTI
site 034A7   ; OUTI
site 034A9   ; OUTI
site 034AB   ; OUTI
site 034AD   ; OUTI
site 034AF   ; OUTI
site 034B1   ; OUTI
site 034B3   ; OUTI
site 034B5   ; OUTI
site 034B7   ; OUTI
site 034B9   ; OUTI
site 034BB   ; OUTI
site 034BD   ; OUTI
site 034BF   ; OUTI
site 034C1   ; OUTI
site 034C3   ; OUTI
site 034C5   ; OUTI
site 034C7   ; OUTI
site 034C9   ; OUTI
site 034CB   ; OUTI
site 034CD   ; OUTI
site 034CF   ; OUTI
site 034D1   ; OUTI
site 034D3   ; OUTI
site 034D5   ; OUTI
site 034D7   ; OUTI
site 034D9   ; OUTI
site 034DB   ; OUTI
site 034DD   ; OUTI
site 034DF   ; OUTI
site 034E1   ; OUTI
site 034E3   ; OUTI
site 034E5   ; OUTI
site 034E7   ; OUTI
site 034E9   ; OUTI
site 034EB   ; OUTI
site 034ED   ; OUTI
site 034EF   ; OUTI
site 034F1   ; OUTI
site 034F3   ; OUTI
site 034F5   ; OUTI
site 034F7   ; OUTI
site 034F9   ; OUTI
site 034FB   ; OUTI
site 034FD   ; OUTI
site 034FF   ; OUTI
site 04D85   ; OUT (C),L
site 04D89   ; OUT (C),H
site 04DA1   ; OUT (C),L
site 04DA5   ; OUT (C),H
site 04DE5   ; OUT (C),A
site 04DEB   ; OUT (C),A
site 04DF1   ; OUT (C),A
site 04DF7   ; OUT (C),A
site 04F67   ; OUT ($BE),A
site 04F6D   ; OUT ($BE),A
site 05377   ; OUT ($BF),A
site 0537B   ; OUT ($BF),A
site 0537F   ; OUT ($BF),A
site 05383   ; OUT ($BF),A
site 0538E   ; OUT ($BF),A
site 05392   ; OUT ($BF),A
site 05396   ; OUT ($BF),A
site 0539A   ; OUT ($BF),A
site 053A0   ; OUT ($BF),A
site 053A4   ; OUT ($BF),A
site 053B1   ; OUT ($BF),A
site 053B5   ; OUT ($BF),A
site 053B9   ; OUT ($BF),A
site 053BD   ; OUT ($BF),A
site 067A0   ; OUT (C),A
site 067A6   ; OUT (C),B
site 067AD   ; OUT (C),A
site 067B3   ; OUT (C),B
site 082C5   ; OUT (C),E
site 082CA   ; OUT (C),D
site 08854   ; IN A,(C)
site 08E2D   ; OUT ($BF),A
site 08E31   ; OUT ($BF),A
site 092A0   ; OUT ($BF),A
site 092A4   ; OUT ($BF),A
site 092A9   ; OUT ($BF),A
site 092AD   ; OUT ($BF),A
site 0A31B   ; OUT ($BF),A
site 0A31F   ; OUT ($BF),A
site 0A324   ; OUT ($BF),A
site 0A328   ; OUT ($BF),A
site 3C1E2   ; OUT ($7F),A
site 3C308   ; OUT ($7F),A
site 3C4A9   ; OTIR
site 3C5C1   ; OUT ($7F),A
site 3C5CB   ; OUT ($7F),A
site 3C5E8   ; OUT ($7F),A
site 3C6EC   ; OUT ($7F),A
site 3C777   ; OUT ($7F),A
site 3C819   ; OUT ($7F),A
site 3C822   ; OUT ($7F),A
site 3C832   ; OUT ($7F),A
site 3C898   ; OUT ($7F),A
site 3C8B5   ; OUT ($7F),A
site 3C968   ; IN A,($89)
mapst 0004A   ; LD ($FFFC),A
mapst 0004D   ; LD ($FFFD),A
mapst 00052   ; LD ($FFFE),A
mapst 00057   ; LD ($FFFF),A
mapst 00089   ; LD ($FFFC),A
mapst 0008C   ; LD ($FFFD),A
mapst 00091   ; LD ($FFFE),A
mapst 00096   ; LD ($FFFF),A
mapst 000D4   ; LD ($FFFF),A
mapst 0277D   ; LD ($FFFF),A
mapst 02794   ; LD ($FFFF),A
mapst 027AB   ; LD ($FFFF),A
mapst 027C2   ; LD ($FFFF),A
mapst 02832   ; LD ($FFFF),A
mapst 0284D   ; LD ($FFFF),A
mapst 02857   ; LD ($FFFF),A
mapst 02886   ; LD ($FFFF),A
mapst 028B3   ; LD ($FFFF),A
mapst 028BB   ; LD ($FFFF),A
mapst 02A98   ; LD ($FFFF),A
mapst 02AFF   ; LD ($FFFF),A
mapst 02D87   ; LD ($FFFF),A
mapst 02DAD   ; LD ($FFFF),A
mapst 02DBD   ; LD ($FFFF),A
mapst 02DE6   ; LD ($FFFF),A
mapst 02DF6   ; LD ($FFFF),A
mapst 02E1B   ; LD ($FFFF),A
mapst 030F6   ; LD ($FFFF),A
mapst 03168   ; LD ($FFFF),A
mapst 0327A   ; LD ($FFFF),A
mapst 032C7   ; LD ($FFFF),A
mapst 032E7   ; LD ($FFFF),A
mapst 032ED   ; LD ($FFFF),A
mapst 03557   ; LD ($FFFF),A
mapst 03591   ; LD ($FFFF),A
mapst 049E4   ; LD ($FFFF),A
mapst 04A06   ; LD ($FFFF),A
mapst 04C9F   ; LD ($FFFF),A
mapst 04CD7   ; LD ($FFFF),A
mapst 04DE1   ; LD ($FFFF),A
mapst 04DFB   ; LD ($FFFF),A
mapst 05074   ; LD ($FFFF),A
mapst 050AF   ; LD ($FFFF),A
mapst 050B7   ; LD ($FFFF),A
mapst 050F2   ; LD ($FFFF),A
mapst 050FA   ; LD ($FFFF),A
mapst 0517A   ; LD ($FFFF),A
mapst 05182   ; LD ($FFFF),A
mapst 052F4   ; LD ($FFFF),A
mapst 052FC   ; LD ($FFFF),A
mapst 05C4F   ; LD ($FFFF),A
mapst 05C84   ; LD ($FFFF),A
mapst 05CA1   ; LD ($FFFF),A
mapst 05CD4   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 03660   # LD ($FFFF),A; after LD A,$0E; 32 bytes of valid code before it
mapst 036A2   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 05843   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 05849   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 05948   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 05950   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 05972   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 0597A   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 05AB6   # LD ($FFFF),A; after LD A,$0A; 32 bytes of valid code before it
mapst 05AC8   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 05EF8   # LD ($FFFF),A; after LD A,$05; JP/CALL target from $199DD; 32 bytes of valid code before it
mapst 05F60   # LD ($FFFF),A; after LD A,$02; JP/CALL target from $1F5E3; 32 bytes of valid code before it
mapst 05FC7   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
mapst 0602E   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
# CHECK low: site 02CDE  IN A,($3E)  (unmapped_read; no evidence)
site 03301   ; OUTI
site 03303   ; OUTI
site 03305   ; OUTI
site 03307   ; OUTI
site 03309   ; OUTI
site 0330B   ; OUTI
site 0330D   ; OUTI
site 0330F   ; OUTI
site 03311   ; OUTI
site 03313   ; OUTI
site 03315   ; OUTI
site 03317   ; OUTI
site 03319   ; OUTI
site 0331B   ; OUTI
site 0331D   ; OUTI
site 0331F   ; OUTI
site 03321   ; OUTI
site 03323   ; OUTI
site 03325   ; OUTI
site 03327   ; OUTI
site 03329   ; OUTI
site 0332B   ; OUTI
site 0332D   ; OUTI
site 0332F   ; OUTI
site 03331   ; OUTI
site 03333   ; OUTI
site 03335   ; OUTI
site 03337   ; OUTI
site 03339   ; OUTI
site 0333B   ; OUTI
site 0333D   ; OUTI
site 0333F   ; OUTI
site 03341   ; OUTI
site 03343   ; OUTI
site 03345   ; OUTI
site 03347   ; OUTI
site 03349   ; OUTI
site 0334B   ; OUTI
site 0334D   ; OUTI
site 0334F   ; OUTI
site 03351   ; OUTI
site 03353   ; OUTI
site 03355   ; OUTI
site 03357   ; OUTI
site 03359   ; OUTI
site 0335B   ; OUTI
site 0335D   ; OUTI
site 0335F   ; OUTI
site 03361   ; OUTI
site 03363   ; OUTI
site 03365   ; OUTI
site 03367   ; OUTI
site 03369   ; OUTI
site 0336B   ; OUTI
site 0336D   ; OUTI
site 0336F   ; OUTI
site 03371   ; OUTI
site 03373   ; OUTI
site 03375   ; OUTI
site 03377   ; OUTI
site 03379   ; OUTI
site 0337B   ; OUTI
site 0337D   ; OUTI
site 0337F   ; OUTI
site 03381   ; OUTI
site 03383   ; OUTI
site 03385   ; OUTI
site 03387   ; OUTI
site 03389   ; OUTI
site 0338B   ; OUTI
site 0338D   ; OUTI
site 0338F   ; OUTI
site 03391   ; OUTI
site 03393   ; OUTI
site 03395   ; OUTI
site 03397   ; OUTI
site 03399   ; OUTI
site 0339B   ; OUTI
site 0339D   ; OUTI
site 0339F   ; OUTI
site 033A1   ; OUTI
site 033A3   ; OUTI
site 033A5   ; OUTI
site 033A7   ; OUTI
site 033A9   ; OUTI
site 033AB   ; OUTI
site 033AD   ; OUTI
site 033AF   ; OUTI
site 033B1   ; OUTI
site 033B3   ; OUTI
site 033B5   ; OUTI
site 033B7   ; OUTI
site 033B9   ; OUTI
site 033BB   ; OUTI
site 033BD   ; OUTI
site 033BF   ; OUTI
site 033C1   ; OUTI
site 033C3   ; OUTI
site 033C5   ; OUTI
site 033C7   ; OUTI
site 033C9   ; OUTI
site 033CB   ; OUTI
site 033CD   ; OUTI
site 033CF   ; OUTI
site 033D1   ; OUTI
site 033D3   ; OUTI
site 033D5   ; OUTI
site 033D7   ; OUTI
site 033D9   ; OUTI
site 033DB   ; OUTI
site 033DD   ; OUTI
site 033DF   ; OUTI
site 033E1   ; OUTI
site 033E3   ; OUTI
site 033E5   ; OUTI
site 033E7   ; OUTI
site 033E9   ; OUTI
site 033EB   ; OUTI
site 033ED   ; OUTI
site 033EF   ; OUTI
site 033F1   ; OUTI
site 033F3   ; OUTI
site 033F5   ; OUTI
site 033F7   ; OUTI
site 033F9   ; OUTI
site 033FB   ; OUTI
site 033FD   ; OUTI
site 033FF   ; OUTI
# CHECK low: site 037CD  OUT ($DC),A  (no_effect; no evidence)
# CHECK low: site 037D9  IN A,($DC)  (joypad_a; no evidence)
# CHECK low: site 04F28  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 04F31  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 06700  OUT ($DD),A  (no_effect; no evidence)
# CHECK low: site 07B7F  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 07B8A  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 0891A  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 09392  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09BBB  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09BC9  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09BD7  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09BE5  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09BF3  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09C01  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09C0F  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09C16  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 09C1D  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 0A1C9  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0A203  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 103DB  IN A,($C0)  (joypad_a; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1E7E5  IN A,($C0)  (joypad_a; no evidence)
# CHECK low: site 1F416  IN A,($3E)  (unmapped_read; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 26C85  IN B,(C)  (port in C; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2746E  IN A,($BF)  (vdp_status; no evidence)
# CHECK low: site 28FEC  OUT ($7F),A  (psg; no evidence)
# CHECK low: site 2AB27  OUT ($F0),A  (fm_address; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2AD60  OUT ($7F),A  (psg; 6 RST or NOP opcodes around it (looks like data); 29 bytes of valid code before it)
# CHECK low: site 2E652  IN A,($C0)  (joypad_a; 10 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2E983  IN A,($C0)  (joypad_a; no evidence)
# CHECK low: site 2EA54  OUT ($C0),A  (no_effect; no evidence)
# CHECK low: site 2EEF3  IN A,($C0)  (joypad_a; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2F0AB  IN B,(C)  (port in C; no evidence)

# Dr. Robotnik's Mean Bean Machine (Europe, Brazil).cht, "Stage Modifier - Scenario Mode": RAM $D410 is the stage
poke "Start stage"
ar 00D4-10??
endpoke

# Dr. Robotnik's Mean Bean Machine (Europe, Brazil).cht, the six "FAKE Score" digits: RAM $CCD3-$CCD8 is the left score
# Only the score display changes.
poke "Score 999999"
ar 00CC-D309
ar 00CC-D409
ar 00CC-D509
ar 00CC-D609
ar 00CC-D709
ar 00CC-D809
endpoke
