; Library page rle_tiles: a fast copy of a game's Sega planar RLE tile unpacker.
;
; entries: rle_tiles
;
; What it replaces. The game's tile unpacker in the jr-z form of the Sega planar
; RLE decoder, which sitescan.py reports as pattern rule 4 (an rle_decoder row
; with target jr-z): the core reads a count byte with JR Z,exit where the usual
; core has RET Z, and the loop over the four bit planes is in the same routine.
; Called with HL = the packed data and DE = a VRAM write address, the game's
; routine unpacks four bit planes. Each plane is a list of runs: a count byte n,
; then n AND $7F bytes when n has bit 7, or one byte repeated n times; a count
; byte of 0 ends the plane. The plane's bytes go to every fourth VRAM byte from
; its start, and each plane starts one VRAM byte after the one before. The game
; sets the VRAM address and writes each byte through the ports with interrupts
; off, so every byte costs a trap.
;
; Entry rle_tiles. Does what the whole game routine does. It unpacks each plane
; into buf, and writes buf to VRAM with jt_vwrite (runs of one byte, VRAM step
; 4) each time buf is full and at the plane's end. When DE is not a VRAM write
; command, or the command would change on the way, it writes through the ports
; byte by byte instead (flush, at .port), with interrupts off, as the game does.
;   Reads:   HL (the data, read as the game sees it, through jt_peek when HL is
;            in $2000-$3FFF) and DE.
;   Returns: as the game routine does. A = 0 with the flags of OR A; B = 0;
;            C kept; DE = DE + 4; HL after the fourth plane's end byte; A' = 4
;            with the flags of CP 2; interrupts on when it wrote a byte, as
;            they were when it wrote none. IX, IY, BC', DE' and HL' are
;            kept.
;
; What it needs from the game:
;   - The io vector at $00 (spec line "vector 00 io"): the port path writes with
;     rst $00 and the inline codes of OUT ($BF),A and OUT ($BE),A.
;   - A code cave of 5 bytes at the start of the game routine, which replaces
;     its first instructions (LD B,4; EX AF,AF'; LD A,B; EX AF,AF') with the
;     far call and a RET:
;         rst $00
;         db far_io, pg_rle_tiles, ent_rle_tiles
;         ret
;     The routine's own OUT ($BE),A keeps its site line, but no longer runs.
;   - Interrupt code that does not write the mapper register $FFFD: the entry
;     leaves interrupts as they are while it unpacks (nms-format.md, "Rules for
;     page code"). jt_vwrite turns them off while it writes.
;   - Runtime ABI 7 (jt_vwrite).
; It uses no name that a spec defines, so every overlay carries the same bytes.
rle_tiles:
        push ix
        push iy
        ld (r_bc),bc
        ld (r_de),de
        xor a
        ld (r_any),a
        ld a,4
        ld (r_n),a
.plane: ld de,(r_de)
        ld (r_v),de             ; this plane's next VRAM address
        ld de,buf
.run:   call get
        or a
        jr z,.pend
        ld c,a
        and $7F
        ld b,a                  ; 0 for a count byte of $80: 256 bytes
        ld a,1
        ld (r_any),a
        bit 7,c
        jr nz,.lit
        call get                ; one byte, B times
        ld c,a
.rep:   ld a,c
        ld (de),a
        inc de
        ld a,d
        cp buf_end >> 8
        call z,flush
        djnz .rep
        jr .run
.lit:   call get                ; B bytes
        ld (de),a
        inc de
        ld a,d
        cp buf_end >> 8
        call z,flush
        djnz .lit
        jr .run
.pend:  call flush
        ld de,(r_de)
        inc de                  ; the next plane starts one VRAM byte later
        ld (r_de),de
        ld a,(r_n)
        dec a
        ld (r_n),a
        jr nz,.plane
        ld a,4
        cp 2
        ex af,af'               ; A' = 4, F' as CP 2 leaves it
        ld bc,(r_bc)
        ld b,0
        ld de,(r_de)            ; DE + 4
        pop iy
        pop ix
        ld a,(r_any)
        or a
        jr z,.ret
        ei                      ; the game's loop ends each byte with EI
.ret:   xor a                   ; A = 0: Z, P/V set, S, H, N, C clear, as OR A
        ret
; A = (HL) as the game sees it, HL + 1; F changes
get:    ld a,h
        and $E0
        cp $20
        jr z,.pk
        ld a,(hl)
        inc hl
        ret
.pk:    call jt_peek            ; the game's page under this one
        inc hl
        ret
; the bytes from buf to DE: to VRAM at r_v, r_v + 4, ...; r_v moves past them,
; DE = buf; keeps BC and HL
flush:  push hl
        push bc
        ex de,hl
        ld de,buf
        or a
        sbc hl,de               ; HL = the bytes in buf
        jp z,.fd
        ld (f_cnt),hl
        ld (f_src),de
        ld de,(r_v)
        add hl,hl
        add hl,hl
        dec hl
        add hl,de               ; the last address + 3
        ld a,h
        xor d
        and $C0
        jr nz,.port             ; the command changes on the way
        ld a,d
        and $C0
        cp $40
        jr nz,.port             ; not a VRAM write command
        ld ix,1
        ld iy,4
        ld hl,(f_cnt)
.fl:    ld a,h
        or l
        jr z,.fd
        ld c,0                  ; 256 runs
        ld a,h
        or a
        jr nz,.fn
        ld c,l
.fn:    push hl
        ld b,1
        ld hl,(f_src)
        ld de,(r_v)
        ld a,1                  ; the source as mapped: buf in this page
        call jt_vwrite
        ld e,c
        ld d,0
        ld a,c
        or a
        jr nz,.fm
        inc d                   ; 256
.fm:    add hl,de
        ld (f_src),hl
        ld hl,(r_v)
        add hl,de
        add hl,de
        add hl,de
        add hl,de
        ld (r_v),hl
        pop hl
        or a
        sbc hl,de
        jr .fl
.port:  ld a,i                  ; P/V = the interrupt state
        di                      ; as the game's loop writes each byte
        push af
        ld hl,(f_cnt)           ; DE = r_v
        ld bc,(f_src)
.pl:    ld a,e
        rst $00
        db $05                  ; OUT ($BF),A
        ld a,d
        rst $00
        db $05
        ld a,(bc)
        rst $00
        db $04                  ; OUT ($BE),A
        inc bc
        inc de
        inc de
        inc de
        inc de
        dec hl
        ld a,h
        or l
        jr nz,.pl
        ld (r_v),de
        pop af
        jp po,.fd
        ei
.fd:    ld de,buf
        pop bc
        pop hl
        ret
r_bc:   dw 0
r_de:   dw 0
r_v:    dw 0
r_n:    db 0
r_any:  db 0
f_cnt:  dw 0
f_src:  dw 0
        align 256
buf:    ds $400                 ; 1K: a flush is a few jt_vwrite calls
buf_end:
