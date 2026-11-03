# Bank Panic (Europe, Brazil) (En), CRC32 655FB1F4, 32K, no mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output with a reference I/O log
# of 300 s, then decided by hand.
#
# Decisions:
# - RST $08 is the game's VDP address routine; $10 is free ($FF bytes), so it
#   is the io vector.
# - Every high and medium confidence I/O site is kept, except those inside the
#   routines that page 0 replaces ($0281, $02E0, $100D, $1011, $103C, $1040).
#   The reference log runs all of them except $1E21-$1E5B and $7E4E/$7E55,
#   which static flow reaches.
# - The CHECK rows of the draft are not patched. $01FE (read a VRAM word),
#   $0232 (read a VRAM block) and $0321 (the region check through port $3F)
#   are Sega library routines that nothing in the cart calls (verdict
#   unused). $3C1C is in tile graphics and $47AF in a data table (verdict
#   false); the low rows are in data too.
# - The game does all its work in the frame handler at $00FE. Line interrupts
#   at lines 37, 75 and 182 write register 8 for the band of doors, the floor
#   and the status row, so hsplit is on: without it, door plates on the right
#   of the doors band show at the wrong map columns while the room scrolls.
#   Name table writes set the priority bit and priority tiles are on screen,
#   so priority is on.
name Bank Panic
cart 655FB1F4
hz 50		; No-Intro regions Europe, Brazil
vector 10 io
priority
hsplit
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 0010C   ; IN A,($BF)
site 00111   ; IN A,($DD)
site 001C1   ; OTIR
site 001F6   ; OUT ($BE),A
site 0020D   ; OUT ($BE),A
site 00214   ; OUT ($BE),A
site 00219   ; OUT ($BE),A
site 00224   ; OUT ($BE),A
site 0022B   ; OUT ($BE),A
site 00250   ; OUT ($BE),A
site 00255   ; OUT ($BE),A
site 00264   ; OUTI
site 0026B   ; OUT (C),A
site 002A6   ; OUT (C),D
site 002BE   ; OUT ($BE),A
site 00350   ; OUT ($DF),A
site 00358   ; OUT ($DE),A
site 0035A   ; IN A,($DE)
site 00370   ; IN A,($DC)
site 00376   ; IN A,($DC)
site 0037B   ; IN A,($DD)
site 003A6   ; IN A,($DC)
site 003AC   ; IN A,($DC)
site 003B1   ; IN A,($DD)
site 004CE   ; OUT ($BE),A
site 005AA   ; OTIR
site 005B8   ; OTIR
site 00772   ; OUT ($BE),A
site 0099C   ; OUTI
site 009A2   ; OUT (C),A
site 009CA   ; OUTI
site 009D0   ; OUTI
site 00B69   ; OUT ($BE),A
site 00B6F   ; OUT ($BE),A
site 00B77   ; OUT ($BE),A
site 00B7C   ; OUT ($BE),A
site 010E0   ; OUT ($BE),A
site 010EF   ; OUT ($BE),A
site 010F4   ; OUT ($BE),A
site 011A7   ; OUT ($BE),A
site 01456   ; OTIR
site 01504   ; OTIR
site 0150C   ; OUT (C),A
site 0150E   ; OUTI
site 01510   ; OUTI
site 01512   ; OUTI
site 01546   ; OUT ($BE),A
site 01565   ; OUT ($BE),A
site 0156F   ; OUT ($BE),A
site 0163F   ; OUT (C),A
site 01656   ; OUT (C),A
site 0165F   ; OUT (C),A
site 01E21   ; OTIR
site 01E26   ; OTIR
site 01E2B   ; OTIR
site 01E5B   ; OUT ($BE),A
site 077B2   ; OUT ($7F),A
site 077D0   ; OTIR
site 07E4E   ; OUT ($BE),A
site 07E55   ; OUT ($BE),A

# $027C writes B rows of C bytes from HL, one map row (64 bytes) apart from
# the VDP control word DE: an OTIR a row. The game draws the door columns
# with it when the room scrolls, 17 rows of one cell, two columns a frame,
# and other blocks at screen set-up. Through the traps a scroll frame spent
# about 233,000 cycles in it; the frame handler then ran past line 37 and the
# line interrupt that sets the door band's scroll came late (the tops of the
# doors showed the old scroll). It is native code in page 0: one jt_vwrite.
asm 0027C 22   ; the routine, up to its RET at $0291
    rst $10
    db far_io, pg_col, ent_col
    ret
endasm

# $02D3 unpacks one bit plane of Sega planar RLE tile data (sitescan pattern
# rule 4, core form with RET Z; $02C6 calls it for the four planes). It sets
# the VDP address for every byte: three traps a byte, about 90% of a frame for
# over 50 frames while a room is built. It is native code in page 0: the plane
# goes into a buffer and to VRAM with jt_vwrite.
asm 002D3 32   ; the routine, up to its JP $02D3 at $02F0
    rst $10
    db far_io, pg_rle, ent_rle
    ret
endasm

# The door drawing of $0FAD, as native code in page 0. When a door opens or
# shuts, the frame handler writes a door of 14 rows of 10 name table cells
# (from $1005) or 9 or 10 rows of 6 cells (from $1034 and $1063), 2 OUTIs a
# cell, wrapping each row at the end of the 32-cell map row. Through the
# traps that was 280 traps, about 96% of a frame in the runtime alone, and
# the frame overran. The row loops at $1008 and $1037 become far calls; the
# game's LD BC lines before them stay and give B, the rows.
asm 01008 44   ; the row loop from $1005, up to its RET at $1033
    ld c,$14
    rst $10
    db far_io, pg_door, ent_door
    ret
endasm
asm 01037 44   ; the row loop from $1034 and $1063, up to its RET at $1062
    ld c,$0C
    rst $10
    db far_io, pg_door, ent_door
    ret
endasm
page 0 col door rle
;; Both entries turn interrupts off and run on the page's own stack. They
;; put the game's interrupt state back with the byte before their RET.

; col: from $027C. B rows of C bytes from HL, at the VDP control word DE (a
; VRAM write address) and a map row (64 bytes) further on for each row.
; Returns as the routine does: B = 0, C = $BE, DE and HL moved on by the
; rows, A = the high byte of the last row's control word, Z set, carry from
; the last DE + 64.
col:    ld a,i                  ; P/V = IFF2
        di
        ld a,$FB                ; EI
        jp pe,.on
        xor a                   ; NOP
.on:    ld (.ei),a
        ld (gsp),sp
        ld sp,stk
        push ix
        push iy
        push hl
        push de
        push bc
        ld a,c
        ld ixl,a                ; source step: one row of bytes
        ld ixh,0
        ld iy,64                ; VRAM step: one map row
        ld a,b
        ld b,c                  ; B = bytes a run, C = runs
        ld c,a
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop bc
        pop de
        pop hl
        call adv
        pop iy
        pop ix
        ld sp,(gsp)
.ei:    nop                     ; EI when the game had interrupts on
        ret

; door: from $1008 and $1037, the door drawing of $0FAD. As col, but a row
; that runs past the end of its map row goes on at the start of the same map
; row, as the game's loop does. Returns B = 0, C = $BE, DE and HL moved on by
; the rows; A and F differ (the callers do not read them).
door:   ld a,i
        di
        ld a,$FB
        jp pe,.on
        xor a
.on:    ld (.ei),a
        ld (gsp),sp
        ld sp,stk
        push ix
        push iy
        push hl
        push de
        push bc
        ld a,b
        ld (rows),a
        ld a,c
        ld ixl,a
        ld ixh,0
        ld iy,64
        ld a,e
        and $3F
        ld b,a
        ld a,64
        sub b                   ; room to the end of the map row
        cp c
        jr nc,.one              ; the row fits
        ld b,a                  ; the part of each row up to the end of the map row
        ld a,(rows)
        ld c,a
        xor a
        call jt_vwrite
        ld a,b                  ; HL += that part
        add a,l
        ld l,a
        adc a,h
        sub l
        ld h,a
        ld a,e                  ; the rest from the start of the map row
        and $C0
        ld e,a
        ld a,ixl                ; bytes a row
        sub b
        ld b,a
        xor a
        call jt_vwrite
        jr .done
.one:   ld b,c                  ; whole rows
        ld a,(rows)
        ld c,a
        xor a
        call jt_vwrite
.done:  pop bc
        pop de
        pop hl
        call adv
        pop iy
        pop ix
        ld sp,(gsp)
.ei:    nop
        ret

; adv: B rows of C bytes done: HL += B * C, DE += B * 64, with the registers
; and flags the game's loops leave (see col).
adv:    ld a,c
        add a,l
        ld l,a
        adc a,h
        sub l
        ld h,a
        ld a,d                  ; as the row's RST $08 leaves A
        ex de,hl
        push bc
        ld bc,64
        cp a                    ; Z, as the row's last OUTI leaves it
        add hl,bc
        pop bc
        ex de,hl
        djnz adv
        ld c,$BE
        ret

; rle: from $02D3. Unpacks one plane from HL to every fourth VRAM byte from
; the VDP control word DE: runs of a count byte n, then n AND $7F bytes (0 =
; 256) when n has bit 7, or one byte n times; a count byte of 0 ends the plane.
; Returns as the routine does: A = 0 with the flags of OR A, HL after the end
; byte, DE + 4 for each byte, B = 0 and C = the last count byte (both kept
; when the plane is empty). A DE that is not a VRAM write command goes through
; the ports byte by byte, as the game does.
rle:    ld a,i
        di
        ld a,$FB
        jp pe,.on
        xor a
.on:    ld (.ei),a
        ld (gsp),sp
        ld sp,stk
        push ix
        push iy
        ld (vdest),de
        ld a,d
        and $C0
        sub $40                 ; 0 for a VRAM write command
        ld (slow),a
        xor a
        ld (nbuf),a
.run:   call jt_peek            ; the count byte, as the game sees it
        inc hl
        or a
        jr z,.end
        ld c,a
        and $7F
        ld b,a                  ; 0 counts 256, as DJNZ does
        bit 7,c
        jr z,.rep
.lit:   call jt_peek
        inc hl
        call put
        djnz .lit
        jr .run
.rep:   call jt_peek
.rl:    call put
        djnz .rl
        inc hl
        jr .run
.end:   call flush
        ld de,(vdest)
        pop iy
        pop ix
        ld sp,(gsp)
        xor a
        or a
.ei:    nop
        ret

; put: the byte in A to the plane. Keeps every register but F.
put:    push hl
        push af
        ld a,(slow)
        or a
        jr nz,.port
        ld a,(nbuf)
        ld l,a
        ld h,high buf
        pop af
        ld (hl),a
        push af
        ld a,l
        inc a
        ld (nbuf),a
        call z,flushfull        ; 256 bytes in buf
        pop af
        pop hl
        ret
.port:  pop af
        push af
        push de
        ld de,(vdest)
        push af
        ld a,e                  ; OUT ($BF),A twice, OUT ($BE),A
        rst $10
        db $05
        ld a,d
        rst $10
        db $05
        pop af
        rst $10
        db $04
        ld hl,4
        add hl,de
        ld (vdest),hl
        pop de
        pop af
        pop hl
        ret

; flush: buf to VRAM, one byte every 4 from vdest; vdest moves on.
flush:  ld a,(nbuf)
        or a
        ret z
        jr fl
flushfull:
        xor a                   ; 256 bytes
fl:     push bc
        push de
        push hl
        ld c,a                  ; runs of 1 byte (0 = 256)
        ld b,1
        ld hl,buf
        ld de,(vdest)
        ld ix,1
        ld iy,4
        ld a,1                  ; buf is in this page
        call jt_vwrite
        ld l,c                  ; vdest += 4 * runs
        ld h,0
        ld a,c
        or a
        jr nz,.n
        inc h
.n:     add hl,hl
        add hl,hl
        add hl,de
        ld (vdest),hl
        xor a
        ld (nbuf),a
        pop hl
        pop de
        pop bc
        ret

vdest:  dw 0
slow:   db 0
nbuf:   db 0
gsp:    dw 0
rows:   db 0
        ds 32
stk:
        align 256
buf:    ds 256
endpage

# $04DC: EI : HALT : RET, the wait for the next frame interrupt after a
# screen set-up. The HALT waits in the runtime for the game's own interrupt.
eihalt 004DC   ; EI : HALT

# Bank Panic (Europe) (Action Replay).cht, "Infinite Lives"
poke "Infinite lives"
ar 00C0-1F05
endpoke
