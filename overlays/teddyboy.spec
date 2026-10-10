# Teddy Boy (USA, Europe, Brazil), CRC32 2728FAA3, 32K, no mapper.
# The game uses RST $08, $10, $18, $20 and $30, and its RST $20 routine
# runs through $0028, so no RST vector is free except $00: $0000-$0002
# (the game's interrupt-disable and interrupt mode 1 setup) becomes JP to the io entry and the game starts at $0003
# (the framework has already done DI and IM 2).
# Sites: tools/sitescan.py (static, with the detector's dynamic log),
# all high and medium confidence I/O rows, plus the low-confidence rows
# at $01AB, $01B0, $01B5, $51DF, $51E4, which a linear disassembly shows
# are real code. $003F is an OUTI loop that jumps back to itself, patched as OTIR.
name Teddy Boy
cart 2728FAA3
hz any		; No-Intro regions USA, Europe, Brazil
vector 00 io
start 0003
otir 003F   ; OUTI
site 0009   ; OUT ($BF),A
site 0013   ; OUT ($BE),A
site 0029   ; OUT (C),A
site 0031   ; OUT ($BF),A
site 0034   ; OUT ($BF),A
site 010C   ; IN A,($BF)
site 010E   ; IN A,($C1)
site 027C   ; OTIR
site 02B5   ; OUT ($BE),A
site 02C0   ; OUTI
site 02C2   ; OUTI
site 02C5   ; OUT (C),A
site 02C8   ; OUT (C),A
site 02E0   ; OUT ($DF),A
site 02E8   ; OUT ($DE),A
site 02EA   ; IN A,($DE)
site 02F3   ; OUT ($7F),A
site 02F7   ; OUT ($7F),A
site 02FB   ; OUT ($7F),A
site 02FF   ; OUT ($7F),A
site 030E   ; IN A,($C0)
site 0313   ; IN A,($C0)
site 0318   ; IN A,($C1)
site 0328   ; OUT ($DE),A
site 032A   ; IN A,($C0)
site 032F   ; OUT ($DE),A
site 0331   ; IN A,($C0)
site 033C   ; OUT ($DE),A
site 033E   ; IN A,($C0)
site 0349   ; OUT ($DE),A
site 034B   ; IN A,($C0)
site 035D   ; OUT ($DE),A
site 035F   ; IN A,($C0)
site 036A   ; OUT ($DE),A
site 036C   ; IN A,($C0)
site 0383   ; OUT ($DE),A
site 0385   ; IN A,($C0)
site 038A   ; IN A,($C1)
site 0394   ; OUT ($DE),A
site 0396   ; IN A,($C0)
site 03A8   ; OUT ($DE),A
site 03AA   ; IN A,($C0)
site 03B5   ; OUT ($DE),A
site 03B7   ; IN A,($C0)
site 03C2   ; OUT ($DE),A
site 03C4   ; IN A,($C1)
site 03CF   ; OUT ($DE),A
site 03D1   ; IN A,($C1)
site 35E0   ; OUT ($BE),A
site 35E6   ; OUT ($BE),A
site 5148   ; OUT ($7F),A
site 51BB   ; OUT ($7F),A
site 51D5   ; OTIR
site 01AB   ; OUT ($BF),A
site 01B0   ; OUT ($BF),A
site 01B5   ; OUTI
site 51DF   ; OUT ($7F),A
site 51E4   ; OUT ($7F),A
# Three VRAM loops of the round set-up, as native code in page 0. The game runs them
# with interrupts off and the display off, between $0D95 and $0EA6; through the traps
# they take about 15 frames of each round start.
#   $0023: the RST $20 loop (B name table cells: a byte from HL, then the attribute
#          byte at $C050), which $017F calls once per row.
#   $004A: the 1-bit-to-4-bit tile expansion (BC bytes from HL, plane mask in
#          $C051). Its callers enter at $0047, which stores A there first, or at
#          $004A itself ($31B2, $31BC).
#   $019B: the name table fill of $018C and $0195 (B,C cells of the value in HL).
# Each entry turns interrupts off while it runs: the game's frame handler calls
# code in $2000-$3FFF.
asm 0023 5           ; OUTI : LD A,($C050), the start of the RST $20 loop
    rst $00
    db far_io, pg_pairs, ent_pairs
    ret
endasm
asm 004A 5           ; LD A,(HL) : EXX : LD C,$BE, the start of the tile expansion loop
    rst $00
    db far_io, pg_expand, ent_expand
    ret
endasm
asm 019B 14          ; the fill loop, up to its RET at $01A8
    rst $00
    db far_io, pg_fill, ent_fill
    ret
endasm
page 0 pairs expand fill
; pairs: from $0023 (the RST $20 loop; RST $28 also comes here, through the
; JP NZ,$0023 at $002C). B cells (0 = 256) at the VDP address the game has
; set: the byte at HL, then the byte at $C050, for each cell. Returns as the
; loop does: HL past the source, B = 0, C = $BE, A = ($C050), Z set.
pairs:  ld a,i                  ; P/V = IFF2: the interrupt state to restore
        di
        push af
        ld a,(vdp_code)
        cp 3
        jr z,.slow              ; a CRAM address: through the framework
        push ix
        push iy
        push de
        ld de,(vdp_addr)
        ld c,b                  ; C runs (0 = 256) of 1 byte, 2 bytes apart in VRAM
        ld b,1
        ld ix,1
        ld iy,2
        xor a                   ; the source as the game sees it
        call jt_vwrite          ; the cells' low bytes
        push hl
        ld hl,$C050
        inc de
        ld ix,0
        xor a
        call jt_vwrite          ; the attribute byte into each cell
        pop hl
        ld e,c                  ; HL += cells
        ld d,0
        ld a,c
        or a
        jr nz,.add
        inc d
.add:   add hl,de
        pop de
        pop iy
        pop ix
        ld b,0
        jr .out
.slow:  rst $00                 ; OUTI through the framework
        db $A3
        ld a,($C050)
        rst $00                 ; OUT (C),A
        db $79
        inc b
        dec b
        jr nz,.slow
.out:   ld c,$BE
        pop af
        jp po,.di
        ei
.di:    ld a,($C050)
        inc b                   ; Z, as the last OUTI leaves it
        dec b
        ret

; expand: from $004A. ($C051) = plane mask, BC = source bytes (not 0), HL =
; source, at the VDP address the game has set (each caller sets a VRAM write
; address with RST $08 first). For each source byte, 4 bytes: the byte for
; each plane whose mask bit (bit 0 first) is set, else 0. Returns as the
; game's code does: HL past the source, BC = 0, A = 0, Z set; alternate B = 0,
; C = $BE, H = the last source byte, D = the last byte written.
expand: ld a,i
        di
        push af
        push ix
        push de
.blk:   ld a,b                  ; this block: up to 64 source bytes
        or a
        ld a,64
        jr nz,.k
        ld a,c
        cp 64
        jr c,.k
        ld a,64
.k:     ld (.n),a
        push bc
        ld c,a
        ld ix,buf
.byte:  call jt_peek            ; the source byte, as the game sees it
        ld d,a
        ld a,($C051)
        ld e,a
        ld b,4
.bit:   ld a,d
        rr e
        jr c,.put
        xor a
.put:   ld (ix+0),a
        inc ix
        djnz .bit
        inc hl
        dec c
        jr nz,.byte
        push hl
        push de
        push iy
        ld de,(vdp_addr)
        ld hl,buf
        ld a,(.n)
        add a,a
        add a,a
        ld b,a                  ; 4 bytes a source byte (64 -> 256 = 0)
        ld c,1
        ld a,1                  ; buf is in this page
        call jt_vwrite
        pop iy
        pop de
        pop hl
        pop bc
        ld a,(.n)               ; BC -= this block
        neg
        add a,c
        ld c,a
        jr c,.nb
        dec b
.nb:    ld a,b
        or c
        jr nz,.blk
        ld a,(ix-1)
        ld (.last),a
        ld a,d
        exx                     ; the alternate registers as the game's loop leaves them
        ld h,a
        ld a,(.last)
        ld d,a
        ld bc,$00BE
        exx
        pop de
        pop ix
        pop af
        jp po,.di
        ei
.di:    xor a
        ld b,a
        ld c,a
        ret
.n:     db 0
.last:  db 0

; fill: from $019B (the loop of $0195). Writes the cell value HL (L, then H)
; C + 256 * (B - 1) times (C = 0 counts 256), as the game's loop does with B
; and C after its INC B. Returns as the loop does: A = H, BC = 0, Z set; DE
; and HL kept.
fill:   ld a,i
        di
        push af
        ld a,(vdp_code)
        cp 3
        jr z,.slow
        push ix
        push iy
        push de
        push hl
        ld (cell),hl
        ld ix,0                 ; the same 2 bytes for every cell
        ld iy,2
.ch:    push bc                 ; C runs, then 256 runs for each more B
        ld de,(vdp_addr)
        ld hl,cell
        ld b,2
        ld a,1                  ; cell is in this page
        call jt_vwrite
        pop bc
        ld c,0
        djnz .ch
        pop hl
        pop de
        pop iy
        pop ix
        jr .out
.slow:  ld a,l                  ; OUT ($BE),A twice per cell, through the framework
        rst $00
        db $04
        ld a,h
        rst $00
        db $04
        dec c
        jr nz,.slow
        djnz .slow
.out:   pop af
        jp po,.di
        ei
.di:    ld a,h
        ld bc,0
        inc c                   ; Z, as the last DEC C leaves it
        dec c
        ret
cell:   dw 0
buf:    ds 256
endpage
