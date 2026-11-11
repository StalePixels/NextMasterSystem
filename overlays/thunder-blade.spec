# Thunder Blade (USA, Europe, Brazil) (En), CRC32 AE920E4B, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output.
# Decisions:
# - At power-on $40F8 fills $C600-$CB7F with 704 OUTI and puts a RET at $CB80. The game
#   calls into that chain at $C600, $C680, $CAA8, $CB14, $CB58, $CB6C and $CB70 to write
#   the name table, tiles, the sprite table and the palette. Those I/O instructions are not
#   in the cart image, so each call is replaced with a far call to page 0, which writes the
#   same bytes with jt_vwrite (the palette through the runtime's OTIR). The OUTI loops and
#   the unrolled run of OUTI and OUT ($BE),A ($1D3D-$223C) next to those calls go into the
#   same page entries, so they have no site lines (verdict known for the unrolled run).
# - The game writes the whole name table every frame and scrolls with register 9, so the
#   rows entry writes only the cells that differ from the VRAM copy.
# - The routines at $0BFD, $0C09, $0C6B, $0C90 and $0CD0 are Sega's VDP library routines
#   (read a word, write a word, expand a 1-bit tile, fill tiles, planar RLE). No scanned
#   path reaches them; their I/O sites are patched all the same.
# - The other byte patterns that no path reached are graphics and data (verdict false).
name Thunder Blade
cart AE920E4B
hz any		; No-Intro regions USA, Europe, Brazil
vector 18 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00E71 25         ; CALL $C600 and the OUTI loops to $0E89: 1600 name table bytes from HL
    ld b,25
    rst $18
    db far_io, pg_rows, ent_rows
    jp $0E8A
endasm
asm 03163 25         ; CALL $C600 and the OUTI loops to $317B: 1536 name table bytes from HL
    ld b,24
    rst $18
    db far_io, pg_rows, ent_rows
    jp $317C
endasm
asm 01D35 8          ; JR Z,$1D3D : CALL $C680 : JP $223D: 20 tiles from HL, the unrolled run to $223C
    rst $18
    db far_io, pg_tiles, ent_tiles
    jp $223D
    nop
endasm
asm 0131B 24         ; the sprite table writes to $3F0A and $3F94 through $CB14 and $CAA8
    rst $18
    db far_io, pg_spra, ent_spra
    ret
endasm
asm 0223D 20         ; the sprite table writes to $3F00 and $3F80 through $CB6C and $CB58
    rst $18
    db far_io, pg_sprb, ent_sprb
    jp $2251
endasm
asm 03148 5          ; LD C,$BE : JP $CB70: 8 palette bytes from HL
    rst $18
    db far_io, pg_pal8, ent_pal8
    ret
endasm
page 0 rows tiles spra sprb pal8
; Each entry replaces game code that writes the VDP through the OUTI chain the game builds
; in RAM at $C600-$CB80 ($40F8: 704 OUTI, then RET) or through unrolled OUTI in the cart.
; Each keeps the interrupt state it finds, runs on a stack in this page with interrupts off,
; and returns the registers the game's code leaves (flags are not kept: no caller tests
; them). Runtime internals used: vdp_addr, read as the start of the write; cur_mmu; the
; VRAM copy in pages 28-29 (SHADOW_PAGE).
PSTACK  equ $3FF0
TBUF    equ $3C00             ; 640 bytes of tiles
PBUF    equ $3E80             ; 8 palette bytes

        macro ENTER
        ld (sv_a),a
        ld a,i                  ; P/V = IFF2
        di
        ld a,0
        jp po,1F
        inc a
1:      ld (sv_ie),a
        ld (sv_sp),sp
        ld sp,PSTACK
        push ix
        push iy
        ld a,(sv_a)
        endm

        macro LEAVE
        pop iy
        pop ix
        ld sp,(sv_sp)
        ld a,(sv_ie)
        or a
        ld a,(sv_a)
        jr z,1F
        ei
1:      ret
        endm

; rows: B rows of 64 bytes from HL (SMS RAM) to VRAM at the VDP address (the name table at
; $3800). The game writes the whole table every frame and scrolls with register 9, so most
; frames change few cells: each 2-byte cell is compared with the VRAM copy (pages 28-29, the
; runtime's SHADOW_PAGE, mapped into slot 0 with interrupts off), and only the runs of cells
; that differ are written with jt_vwrite. When the last cell is unchanged its last byte is
; written again at the end, so the VDP address and read buffer end as after the game's writes. A table that crosses an 8K
; page of the VRAM copy is written whole. Returns HL after the bytes, B = 0, C = $BE.
rows:   ENTER
        ld (vsrc),hl
        ld a,b                  ; length = rows * 64
        rrca
        rrca
        ld c,a
        and $3F
        ld b,a
        ld a,c
        and $C0
        ld c,a
        ld (vlen),bc
        ld de,(vdp_addr)
        ld a,d
        and $3F
        ld d,a
        ld (vstart),de
        ld a,d
        and $1F
        ld h,a
        ld l,e
        add hl,bc               ; the end inside the 8K page?
        ld a,h
        cp $20
        jr c,.diff
        jr nz,.whole
        ld a,l
        or a
        jr z,.diff
.whole: ld hl,(vsrc)
        ld de,(vstart)
        ld bc,(vlen)
        call vlin
        jp .end
.diff:  xor a
        ld (vrun),a
        srl b                   ; cells = length / 2
        rr c
        ld (vcnt),bc
        ld hl,(vsrc)
        ld a,d
        and $1F
        ld d,a                  ; DE = the cell in the VRAM copy at slot 0
        call vmap
.cell:  ld a,(de)
        cp (hl)
        jr nz,.chg
        inc de
        inc hl
        ld a,(de)
        cp (hl)
        dec hl
        dec de
        jr nz,.chg
        call vflush             ; unchanged: end the open run
        xor a
        ld (vlast),a
        jr .next
.chg:   ld a,(vrun)
        or a
        jr nz,.grow
        inc a
        ld (vrun),a
        ld (vrs),hl
        ld (vrd),de
        ld bc,0
        ld (vrn),bc
.grow:  ld a,1
        ld (vlast),a
        ld bc,(vrn)
        inc bc
        inc bc
        ld (vrn),bc
.next:  inc hl
        inc hl
        inc de
        inc de
        ld bc,(vcnt)
        dec bc
        ld (vcnt),bc
        ld a,b
        or c
        jr nz,.cell
        call vflush
        ld a,(cur_mmu+0)        ; the game's page back in slot 0
        db $ED,$92,$50          ; nextreg $50,a
        ld a,(vlast)
        or a
        jp nz,.end              ; the last cell was written
        ld hl,(vlen)            ; the last byte once more
        dec hl
        push hl
        ld de,(vstart)
        add hl,de
        ex de,hl
        pop hl
        ld bc,(vsrc)
        add hl,bc
        ld bc,1
        call vlin
.end:   ld hl,(vsrc)
        ld bc,(vlen)
        add hl,bc
        ld bc,$00BE
        LEAVE

; vmap: the VRAM copy's page of the table (vstart) into slot 0. Keeps BC, DE, HL.
vmap:   ld a,(vstart+1)
        rlca
        rlca
        rlca
        and 1
        add a,28
        db $ED,$92,$50          ; nextreg $50,a
        ret

; vflush: write the open run, if any, then map the VRAM copy again. Keeps DE, HL.
vflush: ld a,(vrun)
        or a
        ret z
        xor a
        ld (vrun),a
        ld a,(cur_mmu+0)
        db $ED,$92,$50          ; nextreg $50,a
        push de
        push hl
        ld hl,(vrd)             ; slot 0 offset to the VRAM address
        ld a,(vstart+1)
        and $20
        or h
        ld d,a
        ld e,l
        ld hl,(vrs)
        ld bc,(vrn)
        call vlin
        pop hl
        pop de
        jr vmap

; vlin: BC bytes (1 to 65535) from HL to VRAM from DE, with jt_vwrite (the source as the
; game sees it). Changes AF, BC, DE, HL, IX, IY.
vlin:   ld a,c
        ld (vl_c),a
        ld a,b
        or a
        jr z,.rest
        ld c,b                  ; B runs of 256 bytes
        ld b,0
        ld ix,256
        ld iy,256
        xor a
        call jt_vwrite
        ld a,h
        add a,c
        ld h,a
        ld a,d
        add a,c
        ld d,a
.rest:  ld a,(vl_c)
        or a
        ret z
        ld b,a
        ld c,1
        ld ix,0
        ld iy,0
        xor a
        jp jt_vwrite

; tiles: $1D32 has read the flag byte into A and moved HL past it. A = 0: 160 groups of
; 3 bytes from HL, each with a 0 as the fourth byte (the unrolled run $1D3D-$223C, OUTI x3
; and OUT ($BE),A), expanded into TBUF and written as one block; else 640 bytes from HL
; (CALL $C680). Returns HL after the
; source bytes, C = $BE, A as it came.
tiles:  ENTER
        ld de,(vdp_addr)
        or a
        jr z,.p3
        push hl
        ld b,128
        ld c,5
        ld ix,128
        ld iy,128
        xor a
        call jt_vwrite
        pop hl
        ld bc,640
        add hl,bc
        jr .out
.p3:    ld a,h                  ; a source in $2000-$3FFF is the game's page there:
        cp $40                  ; two jt_vwrite calls that read it as the game sees it
        jr nc,.buf
        add a,2                 ; HL + 480 <= $2000 also reads the game's bytes
        cp $20
        jp nc,.slow
.buf:   push hl
        push de
        ld de,TBUF              ; expand to 4 bytes a group in TBUF
        ld b,160
.grp:   ld a,(hl)
        ld (de),a
        inc hl
        inc de
        ld a,(hl)
        ld (de),a
        inc hl
        inc de
        ld a,(hl)
        ld (de),a
        inc hl
        inc de
        xor a
        ld (de),a
        inc de
        djnz .grp
        pop de
        ld hl,TBUF
        ld b,128
        ld c,5
        ld ix,128
        ld iy,128
        ld a,1                  ; the source is this page
        call jt_vwrite
        pop hl
        ld bc,480
        add hl,bc
        jr .out
.slow:  push hl
        push de
        ld b,3
        ld c,160
        ld ix,3
        ld iy,4
        xor a
        call jt_vwrite
        pop de
        inc de
        inc de
        inc de
        ld hl,zero
        ld b,1
        ld c,160
        ld ix,0
        ld iy,0+4
        ld a,1
        call jt_vwrite
        pop hl
        ld bc,480
        add hl,bc
.out:   ld c,$BE
        LEAVE

; spra: $131B-$1332: 54 bytes from $C500 to $3F0A, 108 bytes from $C536 to $3F94.
; Returns what the game leaves: HL = $C5A2, DE = $7F94, C = $BE, A = $7F, B less 162.
spra:   ENTER
        ld a,b
        sub 162
        ld (sv_b),a
        ld hl,$C500
        ld de,$3F0A
        ld b,54
        ld c,1
        ld ix,54
        ld iy,54
        xor a
        call jt_vwrite
        ld hl,$C536
        ld de,$3F94
        ld b,108
        ld c,1
        ld ix,108
        ld iy,108
        xor a
        call jt_vwrite
        ld a,$7F
        ld (sv_a),a
        ld hl,$C5A2
        ld de,$7F94
        ld a,(sv_b)
        ld b,a
        ld c,$BE
        LEAVE

; sprb: $223D-$2250: 10 bytes from $C38A to $3F00, 20 bytes from $C394 to $3F80.
; Returns HL = $C3A8, DE = $7F80, C = $BE, A = $7F, B less 30.
sprb:   ENTER
        ld a,b
        sub 30
        ld (sv_b),a
        ld hl,$C38A
        ld de,$3F00
        ld b,10
        ld c,1
        ld ix,10
        ld iy,10
        xor a
        call jt_vwrite
        ld hl,$C394
        ld de,$3F80
        ld b,20
        ld c,1
        ld ix,20
        ld iy,20
        xor a
        call jt_vwrite
        ld a,$7F
        ld (sv_a),a
        ld hl,$C3A8
        ld de,$7F80
        ld a,(sv_b)
        ld b,a
        ld c,$BE
        LEAVE

; pal8: $3148-$314C: 8 bytes from HL to CRAM, through the runtime's OTIR. The bytes ($31C0
; on) can lie in $2000-$3FFF, where this page is mapped, so they are read with jt_peek into
; PBUF first. Returns HL + 8, B = 0, C = $BE.
pal8:   ENTER
        ld de,PBUF
        ld b,8
.cp:    call jt_peek
        ld (de),a
        inc hl
        inc de
        djnz .cp
        push hl
        ld hl,PBUF
        ld bc,$08BE
        rst $18
        db $B3
        pop hl
        ld c,$BE
        LEAVE

zero:   db 0
vsrc:   dw 0
vlen:   dw 0
vstart: dw 0
vcnt:   dw 0
vrun:   db 0
vlast:  db 0
vrs:    dw 0
vrd:    dw 0
vrn:    dw 0
vl_c:   db 0
sv_a:   db 0
sv_b:   db 0
sv_ie:  db 0
sv_sp:  dw 0
endpage
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
mapldk 0009B   # LD HL,$FFFC; LD (HL),$80
maphl 000A1   # LD (HL),$00, HL = $FFFD
maphl 000A4   # LD (HL),$01, HL = $FFFE
maphl 000A7   # LD (HL),$02, HL = $FFFF
mapst 000AB   ; LD ($FFFF),A
site 00127   ; IN A,($BF)
site 0013A   ; IN A,($DD)
mapst 00158   ; LD ($FFFF),A
mapst 00187   ; LD ($FFFF),A
mapst 0044E   ; LD ($FFFF),A
mapst 0055A   ; LD ($FFFF),A
mapst 00568   ; LD ($FFFF),A
mapst 0063C   ; LD ($FFFF),A
mapst 0067F   ; LD ($FFFF),A
mapst 0068D   ; LD ($FFFF),A
mapst 00762   ; LD ($FFFF),A
mapst 0078C   ; LD ($FFFF),A
mapst 007A8   ; LD ($FFFF),A
mapst 00881   ; LD ($FFFF),A
mapst 008E0   ; LD ($FFFF),A
mapst 00901   ; LD ($FFFF),A
site 00ABF   ; OUT ($BE),A
site 00AC3   ; OUT ($BE),A
site 00ACF   ; OUT ($BE),A
site 00AD3   ; OUT ($BE),A
site 00AE4   ; OUT ($BE),A
site 00AE8   ; OUT ($BE),A
site 00AF3   ; OUT ($BE),A
site 00AF7   ; OUT ($BE),A
site 00B00   ; OUT ($BE),A
site 00B04   ; OUT ($BE),A
site 00B0C   ; OUT ($BE),A
site 00B10   ; OUT ($BE),A
site 00B14   ; OUT ($BE),A
site 00B18   ; OUT ($BE),A
site 00B29   ; OUT ($BE),A
site 00B2D   ; OUT ($BE),A
site 00B32   ; OUT ($3F),A
site 00B34   ; IN A,($DD)
site 00B3E   ; OUT ($3F),A
site 00B40   ; IN A,($DD)
site 00B49   ; OUT ($3F),A
site 00B7A   ; OUT ($3E),A
site 00B82   ; OUT ($F2),A
site 00B85   ; IN A,($F2)
site 00B97   ; OUT ($F2),A
site 00B9F   ; OUT ($3E),A
site 00BA5   ; IN A,($DC)
site 00BB7   ; OTIR
site 00BF0   ; OUT ($BE),A
site 00BF5   ; OUT ($BE),A
site 00C00   ; IN A,($BE)
site 00C05   ; IN A,($BE)
site 00C0C   ; OUT ($BE),A
site 00C13   ; OUT ($BE),A
site 00C18   ; OUT ($BE),A
site 00C23   ; OUT ($BE),A
site 00C2A   ; OUT ($BE),A
site 00C3D   ; OUTI
site 00C44   ; OUT (C),A
site 00C5A   ; OUTI
site 00C81   ; OUT (C),D
site 00C9B   ; OUT ($BE),A
site 00CBD   ; OUT ($BE),A
site 00CEC   ; OUT ($BE),A
mapst 00D6C   ; LD ($FFFF),A
mapst 00D8F   ; LD ($FFFF),A
mapst 00DC7   ; LD ($FFFF),A
mapst 00E09   ; LD ($FFFF),A
mapst 00F2B   ; LD ($FFFF),A
mapst 01044   ; LD ($FFFF),A
mapst 01843   ; LD ($FFFF),A
otir 01848   ; OUTI
mapst 01CFC   ; LD ($FFFF),A
mapst 01D0F   ; LD ($FFFF),A
mapst 01D20   ; LD ($FFFF),A
mapst 02877   ; LD ($FFFF),A
mapst 02DC8   ; LD ($FFFF),A
mapst 02DD8   ; LD ($FFFF),A
mapst 02DE5   ; LD ($FFFF),A
mapst 02EB5   ; LD ($FFFF),A
mapst 02F27   ; LD ($FFFF),A
mapst 03F73   ; LD ($FFFF),A
mapst 03F81   ; LD ($FFFF),A
mapst 03FDB   ; LD ($FFFF),A
mapst 04014   ; LD ($FFFF),A
mapst 04075   ; LD ($FFFF),A
mapst 05483   ; LD ($FFFF),A
mapst 05541   ; LD ($FFFF),A
mapst 0554A   ; LD ($FFFF),A
mapst 059E2   ; LD ($FFFF),A
mapst 05A03   ; LD ($FFFF),A
mapst 05A5F   ; LD ($FFFF),A
mapst 06547   ; LD ($FFFF),A
mapst 0655E   ; LD ($FFFF),A
mapst 0656C   ; LD ($FFFF),A
mapst 06616   ; LD ($FFFF),A
mapst 06640   ; LD ($FFFF),A
mapst 06651   ; LD ($FFFF),A
mapst 07038   ; LD ($FFFF),A
mapst 0706A   ; LD ($FFFF),A
mapst 0717C   ; LD ($FFFF),A
site 0817A   ; OUT ($F0),A
site 08183   ; OUT ($F1),A
site 0819B   ; OUT ($7F),A
site 081AB   ; OUT (C),D
site 081B1   ; OUT ($F1),A
site 081D3   ; OUT ($7F),A
site 081D7   ; OUT ($7F),A
site 08205   ; OTIR
site 08213   ; OTIR
site 0821D   ; OUT ($F0),A
site 08223   ; OUT ($F1),A
site 0822F   ; OUTI
site 08235   ; OUTI
site 08343   ; OUT ($7F),A
site 08347   ; OUT ($7F),A
site 083DC   ; OUT ($7F),A
site 083E0   ; OUT ($7F),A
site 08408   ; OUT ($7F),A
site 0840C   ; OUT ($7F),A
site 08410   ; OUT ($7F),A
site 08414   ; OUT ($7F),A
site 08417   ; OUT ($7F),A
site 0847D   ; OUT ($F0),A
site 08484   ; OUT ($F1),A
site 0848C   ; OUT ($F0),A
site 08492   ; OUT ($F1),A
site 08587   ; OUT ($F0),A
site 08591   ; OUT (C),L
site 0859A   ; OUT ($F0),A
site 085B5   ; OUT (C),H
site 085BD   ; OUT ($F0),A
site 085CB   ; OUT ($F1),A
site 085D7   ; OUT ($F0),A
site 085E0   ; OUT ($F1),A
site 08782   ; OUT ($F0),A
site 0878B   ; OUT (C),A
site 08790   ; OUT ($F0),A
site 08796   ; OUTI
site 087D6   ; OUT ($7F),A
site 08808   ; OUT ($7F),A
site 0882F   ; OUT ($7F),A
site 08834   ; OUT ($7F),A
site 08860   ; OUT ($F0),A
site 0886E   ; OUT ($F1),A
site 0887C   ; OUT ($F0),A
site 0890D   ; OUTI
site 0890F   ; OUTI
site 08911   ; OUTI
site 08913   ; OUTI
site 08915   ; OUTI
site 08917   ; OUTI
site 08919   ; OUTI
site 0891B   ; OUTI
site 0891D   ; OUTI
site 0891F   ; OUTI
site 08921   ; OUTI
site 0892B   ; OUT (C),D
site 08934   ; OUT ($F1),A
site 08976   ; OUT ($7F),A
site 089CC   ; OUT ($7F),A
site 08A0B   ; OUT ($7F),A
site 08A6D   ; OUT ($7F),A
site 08A8D   ; OUT ($7F),A
site 08ACD   ; OUT ($7F),A
site 08AD7   ; OUT ($7F),A
site 08B1F   ; OUT ($7F),A

# Thunder Blade (USA, Europe, Brazil).cht, "Infinite Lives": the patch at $250A (bank 0)
# turns the DEC (HL) that takes a life off $C00A into OR (HL), so the count never drops
poke "Infinite lives"
gg B65-0AD-3BE
endpoke

# Thunder Blade (USA, Europe, Brazil).cht, "Start with ?? lives": the patch at $04DC (bank 0)
# is the value that a new game stores in $C00A (3 on the cart)
poke "Start lives"
gg ??4-DCF-E66
endpoke
