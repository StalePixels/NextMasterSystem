# Strider (USA, Europe, Brazil) (En), CRC32 9802ED31, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output; a 10-minute reference I/O log ran no I/O
# instruction that the spec leaves out. The frame handler $0038 counts frames; the line handler
# (register 10 = $70 or $77) runs the sound driver $BC92 in bank 12.
# Spec gaps (data/scan-verdicts.tsv): unused is the PSG mute routine $04D4, which nothing names;
# false are byte patterns in data (a RAM address table in bank 1, graphics in bank 3, maps in
# banks 7, 16 and 23).
name Strider
cart 9802ED31
hz any		; No-Intro regions USA, Europe, Brazil
vector 00 io
start 0003
# Name table column streamer $1290 (the column loop $12F0-$134D), as native code in page 0.
# It writes 14 metatiles down one name table column: 28 cells, 2 bytes each, 64 bytes apart in
# VRAM, wrapping from $3F00 to $3800. Each metatile number comes from the map at DE (256 bytes
# a row); its two cells come from the tables at $C000-$C7FF (pages ($D073) and ($D074)). Through
# the traps the loop cost about 130,000 Next cycles a frame in play (8 traps a pass).
asm 012F0 5    ; LD B,$0E; LD A,($D05C), up to the loop
    rst $00
    db far_io, pg_ntcol, ent_ntcol
    ret
endasm
# Sprite tile upload $175B-$1843, as native code in page 0 (entry sprt). For each entry of the
# list at ($D099) (flag, bank - 2, source; $AA ends it) the game maps the bank at $FFFF and writes
# 32 bytes with OUTI (B = $40, counted down by both OUTI and DJNZ), or with a non-zero flag
# 32 bytes mirrored through the table at $0100. Through the traps it cost about 100,000 Next
# cycles a frame in play.
asm 0175B 5    ; LD C,$BF; LD HL,($D095)
    rst $00
    db far_io, pg_sprt, ent_sprt
    ret
endasm
# Sprite table builder $1546: the game puts the sprites of up to 15 objects at the start of the
# table at ($D08B) (Y at +0, X and tile at +$80), then the 9 HUD sprites (clock, score, lives)
# from $D245, unless ($D260) is set. Every 8 frames the game streams a new set of object tiles
# into the other half of its sprite tiles; the runtime then uploads about 35 Next patterns, and
# its sprite update ends about 90 lines after it starts, past the HUD lines. The HUD sprites came
# last in that pass, so for one frame the Next showed the HUD with old attributes or patterns:
# blank or garbled. The entry hudf puts the HUD sprites first, so the runtime writes them before
# the HUD lines are drawn. The HUD is now in front of the objects, where on a Master System the
# objects are in front of it.
asm 01546 29   ; $1546-$1562, up to the object loop $1563
    rst $00
    db far_io, pg_hudf, ent_hudf
    ld ix,$CCA4
    ld b,$0F
    jp $1563
endasm
asm 0157F 1    ; after the object loop: the HUD is already in the table
    ret
endasm
page 0 ntcol sprt hudf
; ntcol: HL = the VRAM address of the column's top cell, DE = the map entry of its top metatile,
; ($D073) and ($D074) the table pages of the upper and lower cells. Does what the game's loop at
; $12F0-$134D does: with ($D05C) = 0, 14 passes of (upper, lower) cells of metatile (DE); else
; 14 passes of the lower cells of (DE), then the upper cells of (DE + 256). D steps by 1 a pass.
; The cells go into buf, then to VRAM with jt_vwrite, one call for each part of the column
; above and below the wrap from $3F00 to $3800. Runs with interrupts off, on its own stack.
; Returns the registers the game's loop leaves: HL = the address after the last cell's step,
; A = H, B = 0, C = the last metatile read, D = D + 14, E kept, Z set.
; Runtime entries used: jt_peek, jt_vwrite.
ntcol:  ld a,i                  ; P/V = the game's interrupt state
        di
        ld a,0
        jp po,.ie
        inc a
.ie:    ld (sv_ie),a
        ld (sv_sp),sp
        ld sp,pstk
        push ix
        push iy
        ld (sv_hl),hl
        ld iy,buf
        ld b,14
        ld a,($D05C)
        or a
        jr nz,.odd
.even:  call rd_de              ; C = metatile (DE)
        ld a,($D073)
        call cell
        inc d
        ld a,($D074)
        call cell
        djnz .even
        jr .send
.odd:   call rd_de
        ld a,($D074)
        call cell
        inc d
        call rd_de
        ld a,($D073)
        call cell
        djnz .odd
.send:  ld a,c
        ld (sv_c),a
        ld (sv_de),de
        ; rows: walk the 28 addresses, one jt_vwrite for each run without a wrap
        ld hl,(sv_hl)
        ld (seg_v),hl
        ld hl,buf
        ld (seg_s),hl
        ld hl,(sv_hl)
        ld b,28
        ld c,0                  ; rows in this run
.row:   inc c
        ld a,l
        add a,$40
        ld l,a
        ld a,h
        adc a,0
        cp $3F
        jr c,.nw
        sub 7
        ld h,a
        call flush              ; the next row wraps: write this run
        ld (seg_v),hl
        ld c,0
        djnz .row
        jr .done
.nw:    ld h,a
        djnz .row
        call flush
.done:  ld de,(sv_de)           ; registers as the game's loop leaves them
        ld a,(sv_c)
        ld c,a
        pop iy
        pop ix
        ld sp,(sv_sp)
        ld a,(sv_ie)
        or a
        ld a,h
        ld b,1
        jr z,.di
        dec b
        ei
        ret
.di:    dec b
        ret

; cell: write the two bytes of cell C from table page A into buf at IY. Keeps BC, DE, HL.
cell:   push bc
        ld b,a
        ld a,(bc)
        ld (iy+0),a
        inc b
        ld a,(bc)
        ld (iy+1),a
        inc iy
        inc iy
        pop bc
        ret

; rd_de: C = the byte the game sees at DE. Keeps the rest except A and F.
rd_de:  ld a,d
        and $E0
        cp $20
        jr z,.pk
        ld a,(de)
        ld c,a
        ret
.pk:    ex de,hl
        call jt_peek
        ex de,hl
        ld c,a
        ret

; flush: write C rows (C >= 1) from (seg_s) to VRAM (seg_v), then advance seg_s.
; Keeps B, HL.
flush:  push bc
        push hl
        ld hl,(seg_s)
        ld de,(seg_v)
        ld b,2
        ld ix,2
        ld iy,$40
        ld a,1                  ; the source as mapped now: buf is in this page
        call jt_vwrite
        ld a,c                  ; seg_s += 2 * C
        add a,a
        ld e,a
        ld d,0
        add hl,de
        ld (seg_s),hl
        pop hl
        pop bc
        ret

; sprt: B = the most tiles to write. Does what the game's code at $175B-$1843 does, with the
; register sets as it leaves them: the control writes of VRAM address ($D095) through the
; runtime (C = $BF), interrupts on, DE = $20; then for each list entry, in the other register
; set: map the bank, and write 32 bytes from the source, or 32 bytes of the source through the
; table at $0100 (D = 1); back in the first set, HL += $20 and count B down. An entry $AA
; returns at once in the list's register set with A = $AA and Z set; when B reaches 0,
; ($D095) = HL. IX and IY are kept. Runs on the game's stack with interrupts on, as the game's
; code does; each jt_vwrite call keeps them off while it runs.
; Runtime entries used: the io RST (OUT (C),r and the mapper store $FFFF), jt_vwrite, jt_peek.
sprt:   di
        ld c,$BF
        ld hl,($D095)
        rst $00
        db $69                  ; OUT (C),L
        ld a,h
        set 6,a
        rst $00
        db $79                  ; OUT (C),A: port $BF
        ei
        ld a,h
        and $3F
        ld (vaddr+1),a
        ld a,l
        ld (vaddr),a
        ld de,$0020
.item:  exx
        ld hl,($D099)
        ld a,(hl)
        cp $AA
        ret z
        inc hl
        ld c,a
        ld a,(hl)
        inc hl
        add a,2
        rst $00
        db $13,0                ; LD ($FFFF),A
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld ($D099),hl
        ex de,hl
        ld a,c
        and a
        jr nz,.flip
        ld (sv_bc),bc           ; 32 bytes from the source as the game sees it
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld ix,32
        ld iy,32
        ld bc,$2001
        push de
        ld de,(vaddr)
        xor a
        call jt_vwrite
        pop de
        ld bc,32
        call vstep
        add hl,bc
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld bc,$00BE             ; as OUTI leaves it
        xor a
        exx
        add hl,de
        djnz .item
        ld ($D095),hl
        ret
.flip:  ld (sv_bc),bc           ; 32 bytes through the table at $0100
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld iy,buf
        ld d,1
        ld b,32
.fb:    ld a,h
        and $E0
        cp $20
        jr z,.fpk
        ld e,(hl)
        jr .fe
.fpk:   call jt_peek
        ld e,a
.fe:    ld a,(de)
        inc l
        ld (iy+0),a
        inc iy
        djnz .fb
        ld (sv_a),a
        push de
        push hl
        ld hl,buf
        ld de,(vaddr)
        ld ix,32
        ld iy,32
        ld bc,$2001
        ld a,1                  ; buf is in this page
        call jt_vwrite
        pop hl
        pop de
        ld bc,32
        call vstep
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld bc,(sv_bc)
        ld a,(sv_a)
        exx
        add hl,de
        dec b
        jp nz,.item
        ld ($D095),hl
        ret

; vstep: vaddr += BC. Keeps BC, DE, HL.
vstep:  push hl
        ld hl,(vaddr)
        add hl,bc
        ld a,h
        and $3F
        ld h,a
        ld (vaddr),hl
        pop hl
        ret

; hudf: the start of the sprite table builder $1546 with the HUD first. Sets ($D08D) and ($D08F),
; the next Y and the next X and tile in the table at ($D08B), and ($D091) = ($D097) XOR $40, as
; the game's code does. Unless ($D260) is set, copies the 9 HUD sprites from $D245 (Y, X, tile
; each) to the start of the table and moves both pointers past them. Writes $D0 at ($D08D), so
; the table ends there until an object adds its sprites. Keeps BC, IX and IY; runs on the game's
; stack with the game's interrupt state, and pushes nothing.
hudf:   ld (hf_bc),bc
        ld hl,($D08B)
        ld ($D08D),hl
        ld de,$0080
        add hl,de
        ld ($D08F),hl
        ld a,($D097)
        xor $40
        ld ($D091),a
        ld a,($D260)
        and a
        jr nz,.end
        ld de,($D08D)
        ld hl,$D245
        ld b,9
.y:     ld a,(hl)
        ld (de),a
        inc de
        inc hl
        inc hl
        inc hl
        djnz .y
        ld ($D08D),de
        ld de,($D08F)
        ld hl,$D246
        ld bc,$09FF             ; C never reaches 0, so LDI leaves B to DJNZ
.x:     ldi
        ldi
        inc hl
        djnz .x
        ld ($D08F),de
.end:   ld hl,($D08D)
        ld (hl),$D0
        ld bc,(hf_bc)
        ret

hf_bc:  dw 0
vaddr:  dw 0
sv_bc:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
sv_a:   db 0

sv_sp:  dw 0
sv_hl:  dw 0
sv_de:  dw 0
sv_c:   db 0
sv_ie:  db 0
seg_s:  dw 0
seg_v:  dw 0
buf:    ds 56
        ds 64
pstk:
endpage
# $BF03 (bank 12) sets the VDP registers, then counts a loop over one frame and retries until the
# count is in the range of a 3.58 MHz Z80 at 50 or 60 Hz; it stores 1 at $D04A for 60 Hz, 0 for 50 Hz.
# The sound driver ($BC92) skips every sixth frame when $D04A is 1. At 28 MHz the count is never in
# the range and the game retries for ever. The routine now takes the rate from NextReg $05 bit 2
# (the rate the Next runs the game at) and returns, as the original does, with interrupts off.
asm 33F03 53   ; $BF03-$BF37: the CPU-speed test
    di
    ld hl,$BF38
    call $04E1
    ld bc,$243B
    ld a,5
    out (c),a
    inc b
    in a,(c)
    and 4
    jr z,.pal
    ld a,1
.pal:
    ld ($D04A),a
    ret
endasm
site 0000E   ; OUT ($3E),A
site 00039   ; IN A,($BF)
site 00264   ; OUT ($BE),A
site 0026C   ; OUT ($BE),A
site 00278   ; OUT ($BE),A
site 00284   ; IN A,($BE)
site 002C0   ; OUT ($BF),A
site 002C3   ; OUT ($BF),A
site 002D3   ; OUT ($BF),A
site 002DA   ; OUT ($BF),A
site 002E3   ; OUT ($BE),A
site 002EC   ; OUT ($BF),A
site 002F3   ; OUT ($BF),A
site 002FC   ; OUT ($BE),A
site 00305   ; OUT ($BF),A
site 0030C   ; OUT ($BF),A
site 00312   ; OUT ($BE),A
site 003E2   ; OUT ($3F),A
site 003E4   ; IN A,($DC)
site 0045F   ; IN A,($DD)
site 00478   ; IN A,($DD)
site 004B7   ; IN A,($DD)
site 004F0   ; OUT ($BF),A
site 004FA   ; OUT ($BF),A
site 00511   ; OUT ($BE),A
site 0083D   ; OUT ($BE),A
site 00C32   ; OUT ($BF),A
site 00C36   ; OUT ($BF),A
site 00C39   ; OUT ($BE),A
site 01148   ; OUT ($BE),A
site 0114F   ; OUT ($BE),A
site 01156   ; OUT ($BE),A
site 0115D   ; OUT ($BE),A
site 0116C   ; OUT ($BE),A
site 01173   ; OUT ($BE),A
site 0117A   ; OUT ($BE),A
site 01181   ; OUT ($BE),A
site 012FB   ; OUT ($BF),A
site 01302   ; OUT ($BF),A
site 01309   ; OUT ($BE),A
site 01311   ; OUT ($BE),A
site 01322   ; OUT ($BF),A
site 01329   ; OUT ($BF),A
site 01330   ; OUT ($BE),A
site 01338   ; OUT ($BE),A
site 01350   ; OUT ($BF),A
site 01357   ; OUT ($BF),A
site 0135E   ; OUT ($BE),A
site 01366   ; OUT ($BE),A
site 01377   ; OUT ($BF),A
site 0137F   ; OUT ($BF),A
site 01386   ; OUT ($BE),A
site 0138E   ; OUT ($BE),A
site 0140C   ; OUT ($BF),A
site 01413   ; OUT ($BF),A
site 01426   ; OUT ($BE),A
site 0142E   ; OUT ($BE),A
site 0143B   ; OUT ($BF),A
site 01442   ; OUT ($BF),A
site 01449   ; OUT ($BE),A
site 01451   ; OUT ($BE),A
site 0145E   ; OUT ($BF),A
site 01465   ; OUT ($BF),A
site 01477   ; OUT ($BE),A
site 0147F   ; OUT ($BE),A
site 0148E   ; OUT ($BF),A
site 01495   ; OUT ($BF),A
site 0149C   ; OUT ($BE),A
site 014A4   ; OUT ($BE),A
site 014B1   ; OUT ($BF),A
site 014B8   ; OUT ($BF),A
site 01761   ; OUT (C),L
site 01766   ; OUT ($BF),A
site 0178C   ; OUTI
site 0179D   ; OUT ($BE),A
site 017A2   ; OUT ($BE),A
site 017A7   ; OUT ($BE),A
site 017AC   ; OUT ($BE),A
site 017B1   ; OUT ($BE),A
site 017B6   ; OUT ($BE),A
site 017BB   ; OUT ($BE),A
site 017C0   ; OUT ($BE),A
site 017C5   ; OUT ($BE),A
site 017CA   ; OUT ($BE),A
site 017CF   ; OUT ($BE),A
site 017D4   ; OUT ($BE),A
site 017D9   ; OUT ($BE),A
site 017DE   ; OUT ($BE),A
site 017E3   ; OUT ($BE),A
site 017E8   ; OUT ($BE),A
site 017ED   ; OUT ($BE),A
site 017F2   ; OUT ($BE),A
site 017F7   ; OUT ($BE),A
site 017FC   ; OUT ($BE),A
site 01801   ; OUT ($BE),A
site 01806   ; OUT ($BE),A
site 0180B   ; OUT ($BE),A
site 01810   ; OUT ($BE),A
site 01815   ; OUT ($BE),A
site 0181A   ; OUT ($BE),A
site 0181F   ; OUT ($BE),A
site 01824   ; OUT ($BE),A
site 01829   ; OUT ($BE),A
site 0182E   ; OUT ($BE),A
site 01833   ; OUT ($BE),A
site 01838   ; OUT ($BE),A
site 01846   ; OUT ($BF),A
site 0184A   ; OUT ($BF),A
site 01853   ; OUTI
site 01855   ; OUTI
site 01857   ; OUTI
site 01859   ; OUTI
site 0185B   ; OUTI
site 0185D   ; OUTI
site 0185F   ; OUTI
site 01861   ; OUTI
site 01863   ; OUTI
site 01865   ; OUTI
site 01867   ; OUTI
site 01869   ; OUTI
site 0186B   ; OUTI
site 0186D   ; OUTI
site 0186F   ; OUTI
site 01871   ; OUTI
site 01873   ; OUTI
site 01875   ; OUTI
site 01877   ; OUTI
site 01879   ; OUTI
site 0187B   ; OUTI
site 0187D   ; OUTI
site 0187F   ; OUTI
site 01881   ; OUTI
site 01883   ; OUTI
site 01885   ; OUTI
site 01887   ; OUTI
site 01889   ; OUTI
site 0188B   ; OUTI
site 0188D   ; OUTI
site 0188F   ; OUTI
site 01891   ; OUTI
site 01893   ; OUTI
site 01895   ; OUTI
site 01897   ; OUTI
site 01899   ; OUTI
site 0189B   ; OUTI
site 0189D   ; OUTI
site 0189F   ; OUTI
site 018A1   ; OUTI
site 018A3   ; OUTI
site 018A5   ; OUTI
site 018A7   ; OUTI
site 018A9   ; OUTI
site 018AB   ; OUTI
site 018AD   ; OUTI
site 018AF   ; OUTI
site 018B1   ; OUTI
site 018B3   ; OUTI
site 018B5   ; OUTI
site 018B7   ; OUTI
site 018B9   ; OUTI
site 018BB   ; OUTI
site 018BD   ; OUTI
site 018BF   ; OUTI
site 018C1   ; OUTI
site 018C3   ; OUTI
site 018C5   ; OUTI
site 018C7   ; OUTI
site 018C9   ; OUTI
site 018CB   ; OUTI
site 018CD   ; OUTI
site 018CF   ; OUTI
site 018D1   ; OUTI
site 018D4   ; OUT ($BF),A
site 018D7   ; OUT ($BF),A
site 018DA   ; OUTI
site 018DC   ; OUTI
site 018DE   ; OUTI
site 018E0   ; OUTI
site 018E2   ; OUTI
site 018E4   ; OUTI
site 018E6   ; OUTI
site 018E8   ; OUTI
site 018EA   ; OUTI
site 018EC   ; OUTI
site 018EE   ; OUTI
site 018F0   ; OUTI
site 018F2   ; OUTI
site 018F4   ; OUTI
site 018F6   ; OUTI
site 018F8   ; OUTI
site 018FA   ; OUTI
site 018FC   ; OUTI
site 018FE   ; OUTI
site 01900   ; OUTI
site 01902   ; OUTI
site 01904   ; OUTI
site 01906   ; OUTI
site 01908   ; OUTI
site 0190A   ; OUTI
site 0190C   ; OUTI
site 0190E   ; OUTI
site 01910   ; OUTI
site 01912   ; OUTI
site 01914   ; OUTI
site 01916   ; OUTI
site 01918   ; OUTI
site 0191A   ; OUTI
site 0191C   ; OUTI
site 0191E   ; OUTI
site 01920   ; OUTI
site 01922   ; OUTI
site 01924   ; OUTI
site 01926   ; OUTI
site 01928   ; OUTI
site 0192A   ; OUTI
site 0192C   ; OUTI
site 0192E   ; OUTI
site 01930   ; OUTI
site 01932   ; OUTI
site 01934   ; OUTI
site 01936   ; OUTI
site 01938   ; OUTI
site 0193A   ; OUTI
site 0193C   ; OUTI
site 0193E   ; OUTI
site 01940   ; OUTI
site 01942   ; OUTI
site 01944   ; OUTI
site 01946   ; OUTI
site 01948   ; OUTI
site 0194A   ; OUTI
site 0194C   ; OUTI
site 0194E   ; OUTI
site 01950   ; OUTI
site 01952   ; OUTI
site 01954   ; OUTI
site 01956   ; OUTI
site 01958   ; OUTI
site 0195A   ; OUTI
site 0195C   ; OUTI
site 0195E   ; OUTI
site 01960   ; OUTI
site 01962   ; OUTI
site 01964   ; OUTI
site 01966   ; OUTI
site 01968   ; OUTI
site 0196A   ; OUTI
site 0196C   ; OUTI
site 0196E   ; OUTI
site 01970   ; OUTI
site 01972   ; OUTI
site 01974   ; OUTI
site 01976   ; OUTI
site 01978   ; OUTI
site 0197A   ; OUTI
site 0197C   ; OUTI
site 0197E   ; OUTI
site 01980   ; OUTI
site 01982   ; OUTI
site 01984   ; OUTI
site 01986   ; OUTI
site 01988   ; OUTI
site 0198A   ; OUTI
site 0198C   ; OUTI
site 0198E   ; OUTI
site 01990   ; OUTI
site 01992   ; OUTI
site 01994   ; OUTI
site 01996   ; OUTI
site 01998   ; OUTI
site 0199A   ; OUTI
site 0199C   ; OUTI
site 0199E   ; OUTI
site 019A0   ; OUTI
site 019A2   ; OUTI
site 019A4   ; OUTI
site 019A6   ; OUTI
site 019A8   ; OUTI
site 019AA   ; OUTI
site 019AC   ; OUTI
site 019AE   ; OUTI
site 019B0   ; OUTI
site 019B2   ; OUTI
site 019B4   ; OUTI
site 019B6   ; OUTI
site 019B8   ; OUTI
site 019BA   ; OUTI
site 019BC   ; OUTI
site 019BE   ; OUTI
site 019C0   ; OUTI
site 019C2   ; OUTI
site 019C4   ; OUTI
site 019C6   ; OUTI
site 019C8   ; OUTI
site 019CA   ; OUTI
site 019CC   ; OUTI
site 019CE   ; OUTI
site 019D0   ; OUTI
site 019D2   ; OUTI
site 019D4   ; OUTI
site 019D6   ; OUTI
site 019D8   ; OUTI
site 019FC   ; OUT ($BF),A
site 01A01   ; OUT ($BF),A
site 01A09   ; OUTI
site 01A0B   ; OUTI
site 01A0D   ; OUTI
site 01A0F   ; OUTI
site 01A11   ; OUTI
site 01A13   ; OUTI
site 01A15   ; OUTI
site 01A17   ; OUTI
site 01A19   ; OUTI
site 01A1B   ; OUTI
site 01A1D   ; OUTI
site 01A1F   ; OUTI
site 01A21   ; OUTI
site 01A23   ; OUTI
site 01A25   ; OUTI
site 01A27   ; OUTI
site 01A29   ; OUTI
site 01A2B   ; OUTI
site 01A2D   ; OUTI
site 01A2F   ; OUTI
site 01A31   ; OUTI
site 01A33   ; OUTI
site 01A35   ; OUTI
site 01A37   ; OUTI
site 01A39   ; OUTI
site 01A3B   ; OUTI
site 01A3D   ; OUTI
site 01A3F   ; OUTI
site 01A41   ; OUTI
site 01A43   ; OUTI
site 01A45   ; OUTI
site 01A47   ; OUTI
site 070E4   ; OUT ($BE),A
site 070ED   ; OUT ($BE),A
site 0713D   ; OUT ($BE),A
site 07146   ; OUT ($BE),A
site 07611   ; OUT ($BE),A
site 07616   ; OUT ($BE),A
site 0761B   ; OUT ($BE),A
site 07620   ; OUT ($BE),A
site 07635   ; OUT ($BE),A
site 07667   ; OUT ($BE),A
site 07881   ; OUT ($BF),A
site 07884   ; OUT ($BF),A
site 0788B   ; OUT ($BE),A
site 07892   ; OUT ($BE),A
site 07A7A   ; OUT ($BE),A
site 07A84   ; OUT ($BE),A
site 07A8C   ; OUT ($BE),A
site 07A96   ; OUT ($BE),A
site 07C42   ; OUT ($BE),A
site 07C4C   ; OUT ($BE),A
site 07EC0   ; OUT ($BE),A
site 07EC5   ; OUT ($BE),A
site 33CF6   ; OUT ($7F),A
site 33D12   ; OUT ($7F),A
site 33D31   ; OUT ($7F),A
site 33D49   ; OUT ($7F),A
site 33D56   ; OUT ($7F),A
site 33D6A   ; OUT ($7F),A
site 33D79   ; OUT ($7F),A
mapst 00088   ; LD ($FFFF),A
mapst 00094   ; LD ($FFFF),A
mapst 00215   ; LD ($FFFF),A
mapst 00227   ; LD ($FFFF),A
mapst 0041E   ; LD ($FFFF),A
mapst 00436   ; LD ($FFFF),A
mapst 0048E   ; LD ($FFFF),A
mapst 0055E   ; LD ($FFFF),A
mapst 005B3   ; LD ($FFFF),A
mapst 005F2   ; LD ($FFFF),A
mapst 00716   ; LD ($FFFF),A
mapst 00727   ; LD ($FFFF),A
mapst 007D7   ; LD ($FFFF),A
mapst 007E8   ; LD ($FFFF),A
mapst 008AD   ; LD ($FFFF),A
mapst 00C95   ; LD ($FFFF),A
mapst 00E05   ; LD ($FFFF),A
mapst 010F3   ; LD ($FFFF),A
mapst 01112   ; LD ($FFFF),A
mapst 01293   ; LD ($FFFF),A
mapst 013A7   ; LD ($FFFF),A
mapst 0177A   ; LD ($FFFF),A
mapst 019F6   ; LD ($FFFF),A
mapst 034F3   ; LD ($FFFF),A
mapst 037DB   ; LD ($FFFF),A
mapst 03873   ; LD ($FFFF),A
mapst 04B41   ; LD ($FFFF),A
mapst 04B49   ; LD ($FFFF),A
mapst 04B55   ; LD ($FFFF),A
mapst 05596   ; LD ($FFFF),A
mapst 05607   ; LD ($FFFF),A
mapst 0588D   ; LD ($FFFF),A
mapst 05904   ; LD ($FFFF),A
mapst 05925   ; LD ($FFFF),A
mapst 05965   ; LD ($FFFF),A
mapst 0599B   ; LD ($FFFF),A
mapst 059D2   ; LD ($FFFF),A
mapst 05F35   ; LD ($FFFF),A
mapst 05FCC   ; LD ($FFFF),A
mapst 06C01   ; LD ($FFFF),A
mapst 06C12   ; LD ($FFFF),A
mapst 07576   ; LD ($FFFF),A
mapst 075A9   ; LD ($FFFF),A
mapst 075DD   ; LD ($FFFF),A
mapst 07648   ; LD ($FFFF),A
mapst 07672   ; LD ($FFFF),A
mapst 07A42   ; LD ($FFFF),A
mapst 07E5B   ; LD ($FFFF),A
mapst 07E6C   ; LD ($FFFF),A
mapst 07E94   ; LD ($FFFF),A

# Strider (USA, Europe, Brazil).cht, "Infinite Lives": RAM $D485 is the lives count
poke "Infinite lives"
ar 00D4-8509
endpoke

# Strider (USA, Europe, Brazil).cht, "Infinite Hits": RAM $D487 is the energy, 4 when full
poke "Infinite energy"
ar 00D4-8704
endpoke

# Strider (USA, Europe, Brazil).cht, "Invulnerability": RAM $D489 is the timer that is
# non-zero while a hit cannot land
poke "Invulnerability"
ar 00D4-8939
endpoke

# Strider (USA, Europe, Brazil).cht, "Infinite Time (One's Digit)": RAM $D265 is the
# counter that drives the clock; held at 9 the clock stops
poke "Infinite time"
ar 00D2-6509
endpoke

# Strider (USA, Europe, Brazil).cht, "Hit Anywhere": the five codes work only together
poke "Hit anywhere"
gg 3A7-73A-C41
gg 182-EEA-4CA
gg 142-EFA-B36
gg 005-EE9-C49
gg 005-E89-E69
endpoke
