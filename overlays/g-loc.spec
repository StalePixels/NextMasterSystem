# G-LOC - Air Battle (Europe, Brazil) (En), CRC32 05CDC24E, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - The game calls banked code through $037F with the bank in B: bank 7 at $8000 (the
#   sound driver, from $1447 and $1460) and bank 5 at $8003 (from $4DC2). The scan takes
#   them as entries 7:8000 and 5:8003; its rows for $8003 in bank 2 are data.
# - The frame handler ($021E) turns the display off, does the VDP work that the foreground
#   asked for in $C201, and turns the display on. On the Master System the work ends in the
#   vertical blank. Through the runtime it runs on into the picture, and the picture showed
#   black from the top down to the line where it ended (in play down to line 43, and in about
#   one frame in eight down to line 165). Its first register 1 write sets the display bit as
#   its last one does, so the display stays on.
# - In play the handler draws the 12 horizon rows from a ROM map every 4th frame while
#   ($CB17) is set (page hz_fill, hz_rows), most often with the map already on the screen.
#   The page writes only the cells that differ from the VRAM copy.
# - The byte scan rows at $0696 and $069A (code from $0694, named only by the JP at $0130
#   that nothing calls) and the unrolled OUTD block $0F0B-$0F8A (nothing names it) are not
#   patched (verdict unused). $2F2AC is in bank 11, which is data (verdict false).
name G-LOC - Air Battle
cart 05CDC24E
hz 50		; No-Intro regions Europe, Brazil
# $0030-$0032 are zero bytes between RST $28 and the interrupt handler; no RST $30 in the cart.
vector 30 io
# Name table rows 0-1 (the black band at the top) and 14-16 (the cockpit's top edge) are
# priority cells: the game's sprites go behind them.
priority
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00029 2   ; IM 1 -> IM 2 (RST $28 restart)
    im 2
endasm
site 001B7   ; IN A,($BF)
site 001BB   ; OUT ($BF),A
site 001BF   ; OUT ($BF),A
site 0020F   ; OUT ($F2),A
site 00217   ; OUT ($3E),A
site 0021B   ; OUT ($3F),A
site 0021E   ; IN A,($BF)
site 00220   ; IN A,($DD)
asm 0022A 2   ; AND $BF -> OR $40: the frame handler's register 1 write keeps the display on
    or $40
endasm
site 0022C   ; OUT ($BF),A
site 00230   ; OUT ($BF),A
site 00241   ; OUT ($BF),A
site 00245   ; OUT ($BF),A
site 002A6   ; OUT ($BF),A
site 002AA   ; OUT ($BF),A
site 00304   ; OUT ($BF),A
site 00308   ; OUT ($BF),A
site 00318   ; IN A,($BF)
site 0031A   ; IN A,($BF)
site 00326   ; IN A,($BF)
site 0045D   ; OUT ($BF),A
site 00461   ; OUT ($BF),A
site 0046D   ; IN A,($BF)
site 00479   ; OUT ($BF),A
site 0047D   ; OUT ($BF),A
site 00484   ; IN A,($DC)
site 004BE   ; IN A,($DD)
site 00605   ; OUT ($BF),A
site 00608   ; OUT ($BF),A
site 00610   ; OUTI
site 00616   ; OUTI
site 0062E   ; OUT ($BF),A
site 00631   ; OUT ($BF),A
site 00637   ; OUTI
site 00639   ; OUTI
site 0064E   ; OUT ($BF),A
site 00652   ; OUT ($BF),A
site 00664   ; OUT ($BF),A
site 00668   ; OUT ($BF),A
site 00680   ; OUT ($BF),A
site 00684   ; OUT ($BF),A
site 006B0   ; OUT ($BF),A
site 006B4   ; OUT ($BF),A
site 006CE   ; OUT ($BF),A
site 006D2   ; OUT ($BF),A
site 00810   ; OUT ($BE),A
site 00815   ; OUT ($BE),A
site 00832   ; OUT ($BE),A
site 00837   ; OUT ($BE),A
site 00B69   ; OUTI
site 00B6B   ; OUT ($BE),A
site 00B6D   ; OUTI
site 00B6F   ; OUT ($BE),A
site 00B71   ; OUTI
site 00B73   ; OUT ($BE),A
site 00B75   ; OUTI
site 00B77   ; OUT ($BE),A
site 00B79   ; OUTI
site 00B7B   ; OUT ($BE),A
site 00B7D   ; OUTI
site 00B7F   ; OUT ($BE),A
site 00B81   ; OUTI
site 00B83   ; OUT ($BE),A
site 00B85   ; OUTI
site 00B87   ; OUT ($BE),A
site 00B89   ; OUTI
site 00B8B   ; OUT ($BE),A
site 00B8D   ; OUTI
site 00B8F   ; OUT ($BE),A
site 00B91   ; OUTI
site 00B93   ; OUT ($BE),A
site 00B95   ; OUTI
site 00B97   ; OUT ($BE),A
site 00B99   ; OUTI
site 00B9B   ; OUT ($BE),A
site 00B9D   ; OUTI
site 00B9F   ; OUT ($BE),A
site 00BA1   ; OUTI
site 00BA3   ; OUT ($BE),A
site 00BA5   ; OUTI
site 00BA7   ; OUT ($BE),A
site 00BA9   ; OUTI
site 00BAB   ; OUT ($BE),A
site 00BAD   ; OUTI
site 00BAF   ; OUT ($BE),A
site 00BB1   ; OUTI
site 00BB3   ; OUT ($BE),A
site 00BB5   ; OUTI
site 00BB7   ; OUT ($BE),A
site 00BB9   ; OUTI
site 00BBB   ; OUT ($BE),A
site 00BBD   ; OUTI
site 00BBF   ; OUT ($BE),A
site 00BC1   ; OUTI
site 00BC3   ; OUT ($BE),A
site 00BC5   ; OUTI
site 00BC7   ; OUT ($BE),A
site 00BC9   ; OUTI
site 00BCB   ; OUT ($BE),A
site 00BCD   ; OUTI
site 00BCF   ; OUT ($BE),A
site 00BD1   ; OUTI
site 00BD3   ; OUT ($BE),A
site 00BD5   ; OUTI
site 00BD7   ; OUT ($BE),A
site 00BD9   ; OUTI
site 00BDB   ; OUT ($BE),A
site 00BDD   ; OUTI
site 00BDF   ; OUT ($BE),A
site 00BE1   ; OUTI
site 00BE3   ; OUT ($BE),A
site 00BE5   ; OUTI
site 00BE7   ; OUT ($BE),A
site 00BE9   ; OUTI
site 00BEB   ; OUT ($BE),A
site 00BED   ; OUTI
site 00BEF   ; OUT ($BE),A
site 00BF1   ; OUTI
site 00BF3   ; OUT ($BE),A
site 00BF5   ; OUTI
site 00BF7   ; OUT ($BE),A
site 00BF9   ; OUTI
site 00BFB   ; OUT ($BE),A
site 00BFD   ; OUTI
site 00BFF   ; OUT ($BE),A
site 00C01   ; OUTI
site 00C03   ; OUT ($BE),A
site 00C05   ; OUTI
site 00C07   ; OUT ($BE),A
site 00C09   ; OUTI
site 00C0B   ; OUT ($BE),A
site 00C0D   ; OUTI
site 00C0F   ; OUT ($BE),A
site 00C11   ; OUTI
site 00C13   ; OUT ($BE),A
site 00C15   ; OUTI
site 00C17   ; OUT ($BE),A
site 00C19   ; OUTI
site 00C1B   ; OUT ($BE),A
site 00C1D   ; OUTI
site 00C1F   ; OUT ($BE),A
site 00C21   ; OUTI
site 00C23   ; OUT ($BE),A
site 00C25   ; OUTI
site 00C27   ; OUT ($BE),A
site 00C29   ; OUTI
site 00C2B   ; OUT ($BE),A
site 00C2D   ; OUTI
site 00C2F   ; OUT ($BE),A
site 00C31   ; OUTI
site 00C33   ; OUT ($BE),A
site 00C35   ; OUTI
site 00C37   ; OUT ($BE),A
site 00C39   ; OUTI
site 00C3B   ; OUT ($BE),A
site 00C3D   ; OUTI
site 00C3F   ; OUT ($BE),A
site 00C41   ; OUTI
site 00C43   ; OUT ($BE),A
site 00C45   ; OUTI
site 00C47   ; OUT ($BE),A
site 00C49   ; OUTI
site 00C4B   ; OUT ($BE),A
site 00C4D   ; OUTI
site 00C4F   ; OUT ($BE),A
site 00C51   ; OUTI
site 00C53   ; OUT ($BE),A
site 00C55   ; OUTI
site 00C57   ; OUT ($BE),A
site 00C59   ; OUTI
site 00C5B   ; OUT ($BE),A
site 00C5D   ; OUTI
site 00C5F   ; OUT ($BE),A
site 00C61   ; OUTI
site 00C63   ; OUT ($BE),A
site 00C65   ; OUTI
site 00C67   ; OUT ($BE),A
site 00C76   ; OUT ($BF),A
site 00C79   ; OUT ($BF),A
site 00C7E   ; OUT (C),L
site 00C80   ; OUT (C),H
site 00C84   ; IN A,($BF)
site 00C8F   ; OUT ($BF),A
site 00C92   ; OUT ($BF),A
site 00C98   ; OUT ($BE),A
site 00CA5   ; OUT ($BE),A
site 00E0A   ; OUTI
site 00E0C   ; OUTI
site 00E0E   ; OUTI
site 00E10   ; OUTI
site 00E12   ; OUTI
site 00E14   ; OUTI
site 00E16   ; OUTI
site 00E18   ; OUTI
site 00E1A   ; OUTI
site 00E1C   ; OUTI
site 00E1E   ; OUTI
site 00E20   ; OUTI
site 00E22   ; OUTI
site 00E24   ; OUTI
site 00E26   ; OUTI
site 00E28   ; OUTI
site 00E2A   ; OUTI
site 00E2C   ; OUTI
site 00E2E   ; OUTI
site 00E30   ; OUTI
site 00E32   ; OUTI
site 00E34   ; OUTI
site 00E36   ; OUTI
site 00E38   ; OUTI
site 00E3A   ; OUTI
site 00E3C   ; OUTI
site 00E3E   ; OUTI
site 00E40   ; OUTI
site 00E42   ; OUTI
site 00E44   ; OUTI
site 00E46   ; OUTI
site 00E48   ; OUTI
site 00E4A   ; OUTI
site 00E4C   ; OUTI
site 00E4E   ; OUTI
site 00E50   ; OUTI
site 00E52   ; OUTI
site 00E54   ; OUTI
site 00E56   ; OUTI
site 00E58   ; OUTI
site 00E5A   ; OUTI
site 00E5C   ; OUTI
site 00E5E   ; OUTI
site 00E60   ; OUTI
site 00E62   ; OUTI
site 00E64   ; OUTI
site 00E66   ; OUTI
site 00E68   ; OUTI
site 00E6A   ; OUTI
site 00E6C   ; OUTI
site 00E6E   ; OUTI
site 00E70   ; OUTI
site 00E72   ; OUTI
site 00E74   ; OUTI
site 00E76   ; OUTI
site 00E78   ; OUTI
site 00E7A   ; OUTI
site 00E7C   ; OUTI
site 00E7E   ; OUTI
site 00E80   ; OUTI
site 00E82   ; OUTI
site 00E84   ; OUTI
site 00E86   ; OUTI
site 00E88   ; OUTI
site 00E8A   ; OUTI
site 00E8C   ; OUTI
site 00E8E   ; OUTI
site 00E90   ; OUTI
site 00E92   ; OUTI
site 00E94   ; OUTI
site 00E96   ; OUTI
site 00E98   ; OUTI
site 00E9A   ; OUTI
site 00E9C   ; OUTI
site 00E9E   ; OUTI
site 00EA0   ; OUTI
site 00EA2   ; OUTI
site 00EA4   ; OUTI
site 00EA6   ; OUTI
site 00EA8   ; OUTI
site 00EAA   ; OUTI
site 00EAC   ; OUTI
site 00EAE   ; OUTI
site 00EB0   ; OUTI
site 00EB2   ; OUTI
site 00EB4   ; OUTI
site 00EB6   ; OUTI
site 00EB8   ; OUTI
site 00EBA   ; OUTI
site 00EBC   ; OUTI
site 00EBE   ; OUTI
site 00EC0   ; OUTI
site 00EC2   ; OUTI
site 00EC4   ; OUTI
site 00EC6   ; OUTI
site 00EC8   ; OUTI
site 00ECA   ; OUTI
site 00ECC   ; OUTI
site 00ECE   ; OUTI
site 00ED0   ; OUTI
site 00ED2   ; OUTI
site 00ED4   ; OUTI
site 00ED6   ; OUTI
site 00ED8   ; OUTI
site 00EDA   ; OUTI
site 00EDC   ; OUTI
site 00EDE   ; OUTI
site 00EE0   ; OUTI
site 00EE2   ; OUTI
site 00EE4   ; OUTI
site 00EE6   ; OUTI
site 00EE8   ; OUTI
site 00EEA   ; OUTI
site 00EEC   ; OUTI
site 00EEE   ; OUTI
site 00EF0   ; OUTI
site 00EF2   ; OUTI
site 00EF4   ; OUTI
site 00EF6   ; OUTI
site 00EF8   ; OUTI
site 00EFA   ; OUTI
site 00EFC   ; OUTI
site 00EFE   ; OUTI
site 00F00   ; OUTI
site 00F02   ; OUTI
site 00F04   ; OUTI
site 00F06   ; OUTI
site 00F08   ; OUTI
site 00F98   ; OUT ($BE),A
site 00F9B   ; OUT ($BE),A
site 00FB6   ; OUT ($BE),A
site 00FB9   ; OUT ($BE),A
site 0E25F   ; OUT ($BF),A
site 0E262   ; OUT ($BF),A
site 0E26B   ; OUTI
site 0E271   ; OUTI
site 15C1C   ; OUT ($BF),A
site 15C24   ; OUT ($BF),A
site 1C1C9   ; OUT ($7F),A
site 1C2B2   ; OUT ($7F),A
site 1C444   ; OTIR
site 1C55A   ; OUT ($7F),A
site 1C564   ; OUT ($7F),A
site 1C581   ; OUT ($7F),A
site 1C685   ; OUT ($7F),A
site 1C711   ; OUT ($7F),A
site 1C7B3   ; OUT ($7F),A
site 1C7BC   ; OUT ($7F),A
site 1C7CC   ; OUT ($7F),A
site 1C848   ; OUT ($7F),A
mapst 00049   ; LD ($FFFF),A
mapldk 001C1   # LD HL,$FFFC; LD (HL),$00
maphl 001C7   # LD (HL),$00, HL = $FFFD
maphl 001CA   # LD (HL),$01, HL = $FFFE
maphl 001CD   # LD (HL),$02, HL = $FFFF
mapst 00310   ; LD ($FFFF),A
mapst 00384   ; LD ($FFFF),A
mapst 0038D   ; LD ($FFFF),A
mapst 006EF   ; LD ($FFFF),A
mapst 00700   ; LD ($FFFF),A
mapst 0102D   ; LD ($FFFF),A
mapst 01091   ; LD ($FFFF),A
mapst 01584   ; LD ($FFFF),A
mapst 01666   ; LD ($FFFF),A
mapst 01705   ; LD ($FFFF),A
mapst 0177E   ; LD ($FFFF),A
mapst 0179E   ; LD ($FFFF),A
mapst 017AF   ; LD ($FFFF),A
mapst 01934   ; LD ($FFFF),A
mapst 01945   ; LD ($FFFF),A
mapst 01992   ; LD ($FFFF),A
mapst 019A6   ; LD ($FFFF),A
mapst 01AC1   ; LD ($FFFF),A
mapst 01B38   ; LD ($FFFF),A
mapst 01C80   ; LD ($FFFF),A
mapst 0217C   ; LD ($FFFF),A
mapst 021C7   ; LD ($FFFF),A
mapst 022DA   ; LD ($FFFF),A
mapst 023D7   ; LD ($FFFF),A
mapst 023FF   ; LD ($FFFF),A
mapst 02469   ; LD ($FFFF),A
mapst 0248D   ; LD ($FFFF),A
mapst 03082   ; LD ($FFFF),A
mapst 0309C   ; LD ($FFFF),A
mapst 030B9   ; LD ($FFFF),A
mapst 030C8   ; LD ($FFFF),A
mapst 030E6   ; LD ($FFFF),A
mapst 030FA   ; LD ($FFFF),A
mapst 03144   ; LD ($FFFF),A
mapst 03278   ; LD ($FFFF),A
mapst 03416   ; LD ($FFFF),A
mapst 03E56   ; LD ($FFFF),A
mapst 03E6C   ; LD ($FFFF),A
mapst 03F08   ; LD ($FFFF),A
mapst 040CC   ; LD ($FFFF),A
mapst 0417E   ; LD ($FFFF),A
mapst 0424C   ; LD ($FFFF),A
mapst 0425D   ; LD ($FFFF),A
mapst 0447C   ; LD ($FFFF),A
mapst 044AB   ; LD ($FFFF),A
mapst 044BE   ; LD ($FFFF),A
mapst 04598   ; LD ($FFFF),A
mapst 0462A   ; LD ($FFFF),A
mapst 04CB1   ; LD ($FFFF),A
mapst 04CC5   ; LD ($FFFF),A
mapst 04CF3   ; LD ($FFFF),A
mapst 04D0D   ; LD ($FFFF),A
mapst 04D58   ; LD ($FFFF),A
mapst 04E30   ; LD ($FFFF),A
mapst 053DE   ; LD ($FFFF),A
mapst 054A9   ; LD ($FFFF),A
mapst 054C2   ; LD ($FFFF),A
mapst 05530   ; LD ($FFFF),A
mapst 0553D   ; LD ($FFFF),A
mapst 0554A   ; LD ($FFFF),A
mapst 05556   ; LD ($FFFF),A
mapst 05573   ; LD ($FFFF),A
mapst 055A4   ; LD ($FFFF),A
asm 030DA 6   ; LD HL,($CB18) : CALL $06AD (12 name table rows, tiles from ROM) -> page hz_fill
    rst $30
    db far_io, pg_hz_fill, ent_hz_fill
    nop
    nop
endasm
asm 030EE 6   ; LD HL,($CB18) : CALL $06CB (12 rows of 32 cells, source step 40) -> page hz_rows
    rst $30
    db far_io, pg_hz_rows, ent_hz_rows
    nop
    nop
endasm
page 0 hz_fill hz_rows
; The horizon. In play the frame handler ($30BD, every 4th frame while ($CB17) is not 0) maps
; bank ($CB17) in slot 2 and draws the 12 sky and sea rows, name table $3880-$3B7F, from a map
; there at ($CB18), with the attribute byte A in every cell: $06AD takes 384 tiles in a row,
; $06CB 12 rows of 32 tiles with a source step of 40. Through the runtime the 768 bytes cost
; about 400,000 cycles, and most of the time the map is the one already on the screen.
; Each entry builds the 768 bytes in v_buf, compares them with the VRAM copy and writes only
; the runs of cells that differ, with jt_vwrite, then the last byte once more, so that the VDP
; address, code and read buffer end as after the game's writes. The game never reads VRAM.
; In: A = the attribute byte. Out: AF, BC, DE and HL changed (the handler restores them all
; from its stack); IX, IY, the alternate registers and the interrupt state kept.
; Runs on a stack of its own, with interrupts off.
; Runtime internals used: jt_vwrite, cur_mmu, and SHADOW_PAGE 28-29 (the VRAM copy; page 29,
; VRAM $2000-$3FFF, is in slot 0 while the compare reads it).
hz_fill:
        ld c,0                  ; one source row of 384 tiles
        jr hz_go
hz_rows:
        ld c,1                  ; 12 source rows of 32 tiles, 40 bytes apart
hz_go:  ld (v_sp),sp
        ld sp,v_stk
        ld b,a
        ld a,i                  ; P/V = IFF2, kept by LD and DI
        di
        push af
        push ix
        push iy
        ld a,b
        ld hl,($CB18)           ; the map, in slot 2
        ld de,v_buf
        dec c
        jr z,.rows
        ld bc,384
.fill:  ldi                     ; the tile
        ld (de),a               ; the attribute
        inc de
        jp pe,.fill
        jr .cmp
.rows:  ld c,12
.row:   ld b,32
.cell:  ldi
        inc bc                  ; LDI counted BC down; B keeps the cells
        ld (de),a
        inc de
        djnz .cell
        push bc
        ld bc,8
        add hl,bc
        pop bc
        dec c
        jr nz,.row
; Compare v_buf with the VRAM copy at $3880 (page 29 offset $1880, in slot 0) cell by cell,
; and note each run of differing cells as (first cell, cells) in v_list. Whole cells are
; written even where only the tile byte differs: jt_vwrite costs more for many runs of one
; byte than for the attribute bytes between them.
.cmp:   ld a,29                 ; SHADOW_PAGE + 1
        db $ED,$92,$50          ; nextreg $50,a
        ld hl,v_buf
        ld de,$1880
        ld ix,v_list
        ld c,0                  ; cells in the open run (0: none)
        ld iy,0                 ; the cell number
.cc:    ld a,(de)
        cp (hl)
        jr nz,.diff
        inc hl
        inc de
        ld a,(de)
        cp (hl)
        jr nz,.diff2
        inc hl
        inc de
        ld a,c                  ; the same: close the open run
        or a
        jr z,.next
        ld (ix+2),c
        inc ix
        inc ix
        inc ix
        ld c,0
        jr .next
.diff:  inc hl
        inc de
.diff2: inc hl
        inc de
        ld a,c
        or a
        jr nz,.more
        ld a,iyl                ; a new run from this cell
        ld (ix+0),a
        ld a,iyh
        ld (ix+1),a
.more:  inc c
        ld a,c
        cp 128                  ; at most 128 cells (256 bytes) in one run
        jr c,.next
        ld (ix+2),c
        inc ix
        inc ix
        inc ix
        ld c,0
.next:  inc iy
        ld a,iyh
        cp 384 >> 8
        jr nz,.cc
        ld a,iyl
        cp 384 & 255
        jr nz,.cc
        ld a,c
        or a
        jr z,.end
        ld (ix+2),c
        inc ix
        inc ix
        inc ix
.end:   ld (ix+0),$FF           ; the end of the list
        ld (ix+1),$FF
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 back
; Write each run: B = 2 x cells bytes from v_buf + 2 x first cell to $3880 + 2 x first cell.
        ld ix,v_list
.wr:    ld l,(ix+0)
        ld h,(ix+1)
        ld a,h
        and l
        inc a
        jr z,.last
        add hl,hl               ; 2 bytes a cell
        ex de,hl
        ld hl,v_buf
        add hl,de
        push hl
        ld hl,$3880
        add hl,de
        ex de,hl                ; DE = the VRAM address
        pop hl                  ; HL = the source
        ld a,(ix+2)
        add a,a
        ld b,a                  ; 0 = 256
        ld c,1
        push ix
        ld ix,0
        ld iy,0
        ld a,1                  ; the source as mapped: v_buf in this page
        call jt_vwrite
        pop ix
        inc ix
        inc ix
        inc ix
        jr .wr
.last:  ld hl,v_buf+767         ; the last attribute byte once more
        ld de,$3B7F
        ld bc,$0101
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        pop af
        ld sp,(v_sp)
        ret po                  ; interrupts were off
        ei
        ret
v_sp:   dw 0
v_list: ds 3 * 385
v_buf:  ds 768
        ds 64
v_stk:
endpage

# G-LOC Air Battle (Europe, Brazil).cht, "Infinite Armour": RAM $CC0D is the armour, $07 is
# full; each hit takes one, and at 0 the game shows the continue screen
poke "Infinite armour"
ar 00CC-0D07
endpoke

# G-LOC Air Battle (Europe, Brazil).cht, "Infinite Missiles": RAM $CC0E is the missile count;
# the HUD shows 255
poke "Infinite missiles"
ar 00CC-0EFF
endpoke

# G-LOC Air Battle (Europe, Brazil).cht, "Infinite Time": RAM $CB2C is the seconds left in
# the mission; the HUD shows 255 SEC
poke "Infinite time"
ar 00CB-2CFF
endpoke

# G-LOC Air Battle (Europe) (Action Replay).cht, "Target Modifier" (Brazil file: 00CC-0F12):
# RAM $CC0F is the count of targets destroyed. A value at or above the mission's target
# count ends the mission at once: 0C and 12 were proved
poke "Target count"
ar 00CC-0F??
endpoke

# G-LOC Air Battle (Europe, Brazil).cht, "Terrain Modifier": RAM $CB42 is the terrain of the
# flight scene. 00 plain, 01 sea, 02 desert, 03 snow and cloud were proved
poke "Terrain"
ar 00CB-42??
endpoke
