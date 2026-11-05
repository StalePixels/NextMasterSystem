# Olympic Gold (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv), CRC32 6A5A1E39, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, checked against reference I/O logs
# (600 s of random input, 180 s of the attract mode): the scan found every I/O and mapper
# site that the logs ran, and the logs ran no I/O outside banks 0 and 1.
# Decisions:
# - No RST vector is free ($0028 is the end of the power-on code), so $0000-$0002 (DI; IM 1)
#   is the io vector and the game starts at $0003, where it sets its own stack.
# - The power-on code sets the mapper with four LD (HL),A stores ($0019-$0027: $FFFC=$80,
#   $FFFD=0, $FFFE=1, $FFFF=2), a form no spec line takes. The cave stores $FFFC and $FFFF
#   through the runtime's mapper store (inline codes $10 and $13, the third byte skipped);
#   slots 0 and 1 already hold banks 0 and 1 at the start.
# - The RET at $4030 (bank 1) jumps through a table of three words at $4031 ($4037, $403D,
#   $4053), all code in bank 1; the RETI at $00EB returns to the word at $C9C8 when the
#   game has set it (stored by $07FF, $0828, $0A21, $0A3C, $0EA2, $0EC7, $0EDA, $0F9C).
# - Byte-scan I/O in banks 0 and 1 that no path or recording reached is code: the text
#   printer $0A41 ($0A73, $0A7B), the name table clear $2D55 ($2D60-$2D88), the register 7
#   write $4EEC ($4EEE, $4EF5) and the character write $57D2 ($57D4, $57DC).
# - The byte-scan patterns in banks 2 to 15 lie where no path or recording reaches: data
#   (data/scan-verdicts.tsv).
# - hsplit: the field events split the picture with line interrupts: register 10 is $23, the
#   handler sets it to $6E at line 35 and writes H scroll at line 72 and 0 at line 183 (the status
#   bar), from $04CE. Without it the last write of the picture (0) set the scroll of every line,
#   the hammer flight in the attract mode never scrolled, the hammer picture stayed up with the
#   logo's palette, and the logo then showed with the wrong tiles. The switch serves the
#   frames where the raster routine gives no table.
# - rastercode (olympic-gold-raster.asm): the line handler counts its events in $C88C, and a
#   late first event merges with the second (one line interrupt pending), so the count falls
#   behind and the status bar gets the play area's H. In swimming the frame handler and the
#   runtime's once-a-frame work often run past line 71, and the bar scrolled with the pool. The
#   routine gives every line its H from the game's RAM (lines 0-72 the top's, 73-183 ($C892),
#   184-191 0) while $C88B is not 0, so the split no longer depends on when the events come.
#   Layer 2 then stays at the X for H = 0 (the bar's priority cells, and the archery inset,
#   which does not scroll). Cost: the raster copper list, about 25,000 cycles a frame in the
#   hammer's flight, where H changes every frame.
# - priority and prichg: the status bar of the events holds tiles with the priority bit, so the
#   athletes' sprites pass behind it; the reference logs show priority tiles on the screen in
#   7,638 of 10,787 attract frames. The game rewrites tiles that those cells show while they stay
#   on the screen; without prichg Layer 2 kept old pixels beside the timer digits of the 100 m.
# - The game's VRAM writers ($07FC, $0A04, $0E98, $0ED0) run with interrupts on and store a
#   restart address in $C9C8; the interrupt handler, which writes VDP registers, returns there
#   instead of to the interrupted code, so a write cut by an interrupt starts again. The runtime
#   enters $0038 with the interrupted PC on the stack, as the Master System does, so this works
#   unchanged.
name Olympic Gold
cart 6A5A1E39
hz 50		; No-Intro region Europe
vector 00 io
hsplit
priority
prichg
rastercode olympic-gold-raster.asm
start 0003
asm 00019 15         ; LD HL,$FFFC : LD A,$80 : LD (HL),A : INC L : XOR A : LD (HL),A : INC L : INC A : LD (HL),A : INC L : INC A : LD (HL),A
    ld a,$80
    rst $00
    db $10,$FF
    ld a,$02
    rst $00
    db $13,$FF
endasm
asm 00307 24         ; VRAM block copy: EX DE,HL : CALL $032C : EX DE,HL : ... the OUTI loop to the RET at $031E
    di
    rst $00
    db far_io, pg_bc0, ent_bc0
    ei
    ret z
.n: di
    rst $00
    db far_io, pg_bcn, ent_bcn
    ei
    jr nz,.n
    ret
endasm
asm 007FC 9          ; column writer: LD HL,$0802 : LD ($C9C8),HL : LD HL,($C8A2)
    di
    rst $00
    db far_io, pg_col, ent_col
    ei
    ret
endasm
asm 00A04 10         ; font tile writer: SUB $20 : LD L,A : LD H,0 : ADD HL,HL (x5)
    di
    rst $00
    db far_io, pg_chr, ent_chr
    ei
    ret
endasm
asm 00E9F 9          ; tile queue, one entry: LD HL,$0EA5 : LD ($C9C8),HL : LD HL,($C880)
    di
    rst $00
    db far_io, pg_q64, ent_q64
    ei
    jr $0E98
endasm
asm 00ED7 9          ; flipped tile queue, one entry: LD HL,$0EDD : LD ($C9C8),HL : LD HL,($C882)
    di
    rst $00
    db far_io, pg_q32, ent_q32
    ei
    jr $0ED0
endasm
asm 0113E 5          ; tile queue of the frame handler: LD HL,$C600 : LD B,$10
    rst $00
    db far_io, pg_tq, ent_tq
    ret
endasm
page 0 col chr q64 q32 tq bc0 bcn
; The game's four VRAM writers that run with interrupts on and store a restart address in
; $C9C8, done with jt_vwrite. Each cave turns interrupts off before its far call and on after
; it, so the game's interrupt handler never finds a runtime entry open and the restart address
; is never stored. Entry tq does the tile queue that the frame handler runs after the sprite
; table ($113E), which cost the handler a frame or more in the pole vault. Entries bc0 and bcn
; do the VRAM block copy $0307. Entries chr, q64, q32 and tq leave a tile alone when the VRAM
; copy already holds its bytes (vsame, vskip). Each entry leaves the registers, RAM and mapper as
; the game's code does.
; Runtime internals used: jt_vwrite, jt_peek, the io vector at $00 (mapper store, inline code
; $13), SHADOW_PAGE 28-29 (the VRAM copy, mapped in slot 0 while bytes are compared, with
; interrupts off), cur_mmu, vdp_addr, vdp_code, vdp_latch, vdp_rbuf.

; Entry col: $07FC, the loop of the column writer. Both its entries come here after their own
; set-up: $07EA (14 rows, ($C8A2) moved on by $240) and $07DD (23 rows, called from $75AB in
; bank 1; the swimming pool). Reads ($C8A2) (the VRAM address), ($C8A0) (the source) and
; ($C8A4) (the rows, 0 = 256). Writes 2 bytes a row, from rows $40 bytes apart to rows $40
; bytes apart. Returns: HL = 0, DE = source + rows x $40, BC = $0040, A = 0 with Z (the
; count), A' = the last byte written; ($C8A2) = 0, ($C9C8) = 0.
col:    ld hl,($C8A0)           ; HL = source
        push hl
        ld de,($C8A2)           ; DE = VRAM address
        ld a,($C8A4)
        ld c,a                  ; C = rows
        ld b,$02                ; 2 bytes a run
        push ix
        push iy
        ld ix,$0040
        ld iy,$0040
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop iy
        pop ix
        pop de                  ; DE = source
        ld a,($C8A4)
        ld l,a
        ld h,0
        or a
        jr nz,.n
        inc h                   ; 0 rows = 256
.n:     add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,de               ; HL = source + rows x $40
        push hl
        ld de,-$003F
        add hl,de               ; the last byte written: last row, second byte
        call jt_peek            ; as the game sees it
        ex af,af'
        pop de
        ld hl,0
        ld ($C8A2),hl
        ld ($C9C8),hl
        ld bc,$0040
        xor a
        ret

; Entry chr: $0A04. A = a character, DE = the VRAM address. Writes the character's 32 bytes
; from the font at $B800 in bank 15. Returns: bank 15 in slot 2, ($C9CA) = the font address,
; ($C9CC) = DE, HL = font address + 32, DE kept, BC = 0, A = (DE high) OR $40.
; The status bar (row 23) has a tile of its own for each cell, all with the priority bit, and
; the game writes the race clock's characters into theirs again in every frame, nearly always
; the same. Each write marks the tile as changed, and with prichg the vertical blank work then
; draws those cells in Layer 2 again, about 30,000 cycles a cell. With the work at the ULA
; interrupt, that took the swimming event's line interrupts past line 71, so the game's count
; of them fell behind and the bar got the pool's scroll. So a character whose 32 bytes are
; already in the VRAM copy is not written; the VDP state is set as the writes leave it
; (vdp_addr, vdp_code, vdp_latch, vdp_rbuf). Runtime internals: SHADOW_PAGE 28-29 (in slot 0
; while compared; interrupts are off), cur_mmu.
chr:    sub $20
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld bc,$B800
        add hl,bc
        ld ($C9CA),hl
        ld ($C9CC),de
        ld a,$0F
        rst $00                 ; LD ($FFFF),A through the runtime
        db $13, $FF
        ld b,32
        call vsame
        jr nz,.w                ; a byte differs
        ld b,32
        call vskip
        jr .x
.w:     push ix
        push iy
        ld ix,$0020
        ld iy,$0020
        ld bc,$2001             ; 32 bytes, one run
        xor a
        call jt_vwrite
        pop iy
        pop ix
.x:     ld bc,$0020
        add hl,bc
        ld bc,0
        ld a,d
        or $40
        ret

; Entry q64: one entry of the tile queue at ($C880): VRAM address (2 bytes, as the two control
; writes), bank - 8, source address. Writes 64 bytes from the source in that bank.
; Returns: the bank in slot 2, ($C880) = the next entry, DE = the next entry, HL = 0,
; BC = $00BE, A = bank.
q64:    ld hl,($C880)
        ld e,(hl)
        inc hl
        ld d,(hl)               ; DE = VRAM address
        inc hl
        ld a,(hl)
        inc hl
        add a,$08
        rst $00                 ; LD ($FFFF),A through the runtime
        db $13, $FF
        ld c,(hl)
        inc hl
        ld b,(hl)
        inc hl
        push hl                 ; the next entry
        push af
        ld h,b
        ld l,c                  ; HL = source
        ld b,64
        call vsame
        jr nz,.w
        ld b,64                 ; the two tiles unchanged
        call vskip
        jr .x
.w:     push ix
        push iy
        ld ix,$0040
        ld iy,$0040
        ld bc,$4001             ; 64 bytes, one run
        xor a
        call jt_vwrite
        pop iy
        pop ix
.x:     pop af
        pop de
        ld ($C880),de
        ld hl,0
        ld bc,$00BE
        ret

; Entry q32: one entry of the queue at ($C882), in the same form. Writes 32 bytes from the
; source, each one through the game's bit-reverse table at $0100 (the tile mirrored), with the
; source address stepping in its low byte only (INC L), as the game's code does.
; Returns: the bank in slot 2, ($C882) = the next entry, BC = the next entry, D = $01,
; E = the last source byte, A = the last byte written, HL = 0.
q32:    ld hl,($C882)
        ld e,(hl)
        inc hl
        ld d,(hl)               ; DE = VRAM address
        inc hl
        ld (q_vram),de
        ld a,(hl)
        inc hl
        add a,$08
        rst $00                 ; LD ($FFFF),A through the runtime
        db $13, $FF
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld (q_next),hl
        ex de,hl                ; HL = source
        push ix
        push iy
        ld d,$01
        ld bc,q_buf
        ld ixl,32
.l:     ld e,(hl)
        ld a,(de)
        inc l
        ld (bc),a
        inc bc
        dec ixl
        jr nz,.l
        ld (q_e),de
        ld de,(q_vram)
        ld hl,q_buf
        ld b,32
        call vsame_now
        jr nz,.w
        ld b,32                 ; the tile unchanged
        call vskip
        jr .x
.w:     ld ix,$0020
        ld iy,$0020
        ld bc,$2001             ; 32 bytes, one run
        ld a,1                  ; the source as mapped now: the buffer in this page
        call jt_vwrite
.x:     pop iy
        pop ix
        ld a,(q_buf+31)
        ld bc,(q_next)
        ld ($C882),bc
        ld de,(q_e)
        ld hl,0
        ret
; Entry tq: $113E, in the frame handler (interrupts off). Up to 16 entries of the queue at
; $C600 in the form of q64 ($AA ends it), each 32 bytes from the source in its bank.
; Returns: as the game's loop does. At the $AA: Z, A = $AA, HL = its address, B = the entries
; left. After 16: B = 0, HL = $C650, A = the last bank. C = $BE; DE = the address after the last
; entry done; the last entry's bank in slot 2.
tq:     ld hl,$C600
        ld b,$10
.e:     ld a,(hl)
        cp $AA
        ret z
        push bc
        ld e,(hl)
        inc hl
        ld d,(hl)               ; DE = VRAM address
        inc hl
        ld a,(hl)
        inc hl
        add a,$08
        rst $00                 ; LD ($FFFF),A through the runtime
        db $13, $FF
        ld c,(hl)
        inc hl
        ld b,(hl)
        inc hl
        push hl                 ; the next entry
        push af
        ld h,b
        ld l,c                  ; HL = source
        ld b,32
        call vsame
        jr nz,.w
        ld b,32                 ; the tile unchanged
        call vskip
        jr .x
.w:     push ix
        push iy
        ld ix,$0020
        ld iy,$0020
        ld bc,$2001             ; 32 bytes, one run
        xor a
        call jt_vwrite
        pop iy
        pop ix
.x:     pop af
        pop hl
        ld d,h
        ld e,l
        pop bc
        ld c,$BE
        djnz .e
        ret
;
;
; Entries bc0 and bcn: $0307, the game's VRAM block copy (HL = source, DE = VRAM address,
; BC = bytes). The game sets the address and then copies with OUTI, with interrupts on. The
; archery inset (the archer and the arrow's flight, top left) is 9 rows of 28 bytes from $CC67,
; copied whole at each update; its bottom row holds priority cells that do not change. The
; runtime marks every priority cell written, changed or not, for a Layer 2 redraw in the
; vertical blank work, and those redraws took the shots' frames to 200-390%. So, for a source
; from $4000 and an even address and length, only the 2-byte cells that differ from the VRAM
; copy are written, in runs with jt_vwrite, and then the last byte once more, so the VDP address
; and read buffer end as after the game's copy. Any other copy is written whole.
; The cave makes one far call for each run: bc0 does the first C bytes (256 when C = 0), bcn
; each further 256, and interrupts are on between the calls. Both return NZ while runs are
; left, with HL and DE moved on, B the runs of 256 left and C = 0. After the last run, as the
; game's loop leaves it: Z with carry clear, HL = source + bytes, D = the VRAM address high
; byte AND $BF, E = 0, BC = $00BE, A = the C given to bc0.
; Runtime internals: SHADOW_PAGE 28-29 (the VRAM copy, in slot 0 while a cell is compared;
; interrupts are off), cur_mmu (jt_vwrite puts the game's slot 0 back from it).
bc0:    ld a,c
        ld (bc_c),a
        ld a,d
        ld (bc_d),a
bcn:    push ix
        push iy
        push bc
        ld ix,$0100
        ld iy,$0100
        ld b,0
        ld a,c
        or a
        jr nz,.c
        inc b                   ; C = 0: 256 bytes
.c:     ld (bc_n),bc            ; the bytes of this run
        or e
        rra
        jr c,.whole             ; an odd address or length
        ld a,h
        cp $40
        jr nc,.cell
.whole: ld b,c                  ; the run whole
        ld c,1
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld bc,(bc_n)
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        jr .end
.cell:  ld a,d                  ; the VRAM copy's page of DE in slot 0
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a
        push de
        ld a,d
        and $1F
        ld d,a
        ld a,(de)
        cp (hl)
        jr nz,.d1
        inc de
        inc hl
        ld a,(de)
        cp (hl)
        dec hl
        pop de
        jr nz,.dif
        call bc_flush           ; unchanged: end the open run
        jr .nx
.d1:    pop de
.dif:   ld bc,(bc_rl)           ; differs: into the run
        ld a,b
        or c
        jr nz,.add
        ld (bc_rs),hl
        ld (bc_rd),de
.add:   inc bc
        inc bc
        ld (bc_rl),bc
.nx:    inc hl
        inc hl
        inc de
        inc de
        ld bc,(bc_n)
        dec bc
        dec bc
        ld (bc_n),bc
        ld a,b
        or c
        jr nz,.cell
        call bc_flush
        dec hl                  ; the last byte once more
        dec de
        ld bc,$0101
        xor a
        call jt_vwrite          ; and the game's page back in slot 0
        inc hl
        inc de
.end:   pop bc
        pop iy
        pop ix
        ld a,c
        or a
        jr z,.full
        ld c,0                  ; after a first run of C bytes, runs of 256
        ld a,b
        or a
        jr .tail
.full:  dec b
.tail:  ret nz
        ld a,(bc_d)
        and $BF
        ld d,a
        ld e,0
        ld bc,$00BE
        xor a                   ; Z, carry clear
        ld a,(bc_c)
        ret
; bc_flush: write the open run of changed cells, if any. Keeps DE, HL.
bc_flush:
        ld bc,(bc_rl)
        ld a,b
        or c
        ret z
        push hl
        push de
        ld hl,(bc_rs)
        ld de,(bc_rd)
        ld b,c                  ; bytes (0 = 256)
        ld c,1
        xor a
        call jt_vwrite          ; also puts the game's page back in slot 0
        ld hl,0
        ld (bc_rl),hl
        pop de
        pop hl
        ret
bc_c:   db 0
bc_d:   db 0
bc_n:   dw 0
bc_rl:  dw 0                    ; the open run: bytes, source, VRAM address
bc_rs:  dw 0
bc_rd:  dw 0
; vsame: HL = a source of B bytes (1-255), DE = their VRAM address, with the bytes inside one
; 8K page of the VRAM copy. Z when the VRAM copy already holds them. A source below $4000 is
; not compared (NZ): slot 0 holds the VRAM copy while it is, and $2000-$3FFF is this page;
; nor are bytes that run past the end of an 8K page of the VRAM copy.
; vsame_now compares any source as mapped now (a buffer in this page). Interrupts must be off.
; Keeps HL, DE; changes A, B, F.
vsame:  ld a,h
        cp $40
        jr nc,vsame_now
        or 1                    ; NZ
        ret
vsame_now:
        ld a,d                  ; past the end of an 8K page: not compared
        and $1F
        cp $1F
        jr nz,.p
        ld a,e
        add a,b
        jr nc,.p
        or 1                    ; NZ
        ret
.p:     push hl
        push de
        ld a,d                  ; the VRAM copy's page of DE in slot 0
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a
        ld a,d
        and $1F
        ld d,a
.c:     ld a,(de)
        cp (hl)
        jr nz,.d
        inc de
        inc hl
        djnz .c
.d:     ld a,(cur_mmu+0)        ; the game's page back in slot 0
        db $ED,$92,$50          ; nextreg $50,a
        pop de
        pop hl
        ld a,b
        or a
        ret

; vskip: the VDP state as writes of B bytes (1-255) from HL to VRAM at DE leave it, for bytes
; the VRAM copy already holds: the address after the last, code 1, the latch clear, the read
; buffer = the last byte. Keeps HL, DE; changes A, B, F.
vskip:  push hl
        push de
        ld a,b
        dec a
        add a,l
        ld l,a
        jr nc,.r
        inc h
.r:     ld a,(hl)
        ld (vdp_rbuf),a
        ex de,hl
        ld a,b
        add a,l
        ld l,a
        jr nc,.v
        inc h
.v:     ld a,h
        and $3F
        ld h,a
        ld (vdp_addr),hl
        xor a
        ld (vdp_latch),a
        inc a
        ld (vdp_code),a
        pop de
        pop hl
        ret
q_vram: dw 0
q_next: dw 0
q_e:    dw 0
q_buf:  ds 32
endpage
site 0000E   ; OUT ($3E),A
site 00039   ; IN A,($BF)
site 0026E   ; IN A,($BF)
site 002F8   ; OUT ($BE),A
site 00300   ; OUT ($BE),A
site 00322   ; IN A,($BE)
site 00330   ; OUT ($BF),A
site 00337   ; OUT ($BF),A
site 00348   ; OUT ($BF),A
site 00350   ; OUT ($BF),A
site 0035A   ; OUT ($BE),A
site 00362   ; OUT ($BF),A
site 00366   ; OUT ($BF),A
site 0036C   ; OUT ($BE),A
site 003C9   ; OUT ($3F),A
site 003CB   ; IN A,($DC)
site 00405   ; OUT ($3F),A
site 00407   ; IN A,($DC)
site 00417   ; IN A,($DD)
site 0047B   ; IN A,($DD)
site 00489   ; IN A,($DD)
site 004B9   ; OTIR
site 004CF   ; OUT ($BF),A
site 004D6   ; OUT ($BF),A
site 004E3   ; OUT ($BE),A
site 00815   ; OUT ($BE),A
site 0081B   ; OUT ($BE),A
site 0094C   ; OUT ($BE),A
site 00953   ; OUT ($BE),A
site 009FB   ; OUTI
site 00A33   ; OUTI
site 00EA9   ; OUT ($BF),A
site 00EAF   ; OUT ($BF),A
site 00EC0   ; OUTI
site 00EE1   ; OUT ($BF),A
site 00EE7   ; OUT ($BF),A
site 00EFC   ; OUT ($BE),A
site 00F01   ; OUT ($BE),A
site 00F06   ; OUT ($BE),A
site 00F0B   ; OUT ($BE),A
site 00F10   ; OUT ($BE),A
site 00F15   ; OUT ($BE),A
site 00F1A   ; OUT ($BE),A
site 00F1F   ; OUT ($BE),A
site 00F24   ; OUT ($BE),A
site 00F29   ; OUT ($BE),A
site 00F2E   ; OUT ($BE),A
site 00F33   ; OUT ($BE),A
site 00F38   ; OUT ($BE),A
site 00F3D   ; OUT ($BE),A
site 00F42   ; OUT ($BE),A
site 00F47   ; OUT ($BE),A
site 00F4C   ; OUT ($BE),A
site 00F51   ; OUT ($BE),A
site 00F56   ; OUT ($BE),A
site 00F5B   ; OUT ($BE),A
site 00F60   ; OUT ($BE),A
site 00F65   ; OUT ($BE),A
site 00F6A   ; OUT ($BE),A
site 00F6F   ; OUT ($BE),A
site 00F74   ; OUT ($BE),A
site 00F79   ; OUT ($BE),A
site 00F7E   ; OUT ($BE),A
site 00F83   ; OUT ($BE),A
site 00F88   ; OUT ($BE),A
site 00F8D   ; OUT ($BE),A
site 00F92   ; OUT ($BE),A
site 00F97   ; OUT ($BE),A
site 00FA8   ; OUT ($BF),A
site 00FAC   ; OUT ($BF),A
site 00FB5   ; OUTI
site 00FB7   ; OUTI
site 00FB9   ; OUTI
site 00FBB   ; OUTI
site 00FBD   ; OUTI
site 00FBF   ; OUTI
site 00FC1   ; OUTI
site 00FC3   ; OUTI
site 00FC5   ; OUTI
site 00FC7   ; OUTI
site 00FC9   ; OUTI
site 00FCB   ; OUTI
site 00FCD   ; OUTI
site 00FCF   ; OUTI
site 00FD1   ; OUTI
site 00FD3   ; OUTI
site 00FD5   ; OUTI
site 00FD7   ; OUTI
site 00FD9   ; OUTI
site 00FDB   ; OUTI
site 00FDD   ; OUTI
site 00FDF   ; OUTI
site 00FE1   ; OUTI
site 00FE3   ; OUTI
site 00FE5   ; OUTI
site 00FE7   ; OUTI
site 00FE9   ; OUTI
site 00FEB   ; OUTI
site 00FED   ; OUTI
site 00FEF   ; OUTI
site 00FF1   ; OUTI
site 00FF3   ; OUTI
site 00FF5   ; OUTI
site 00FF7   ; OUTI
site 00FF9   ; OUTI
site 00FFB   ; OUTI
site 00FFD   ; OUTI
site 00FFF   ; OUTI
site 01001   ; OUTI
site 01003   ; OUTI
site 01005   ; OUTI
site 01007   ; OUTI
site 01009   ; OUTI
site 0100B   ; OUTI
site 0100D   ; OUTI
site 0100F   ; OUTI
site 01011   ; OUTI
site 01013   ; OUTI
site 01015   ; OUTI
site 01017   ; OUTI
site 01019   ; OUTI
site 0101B   ; OUTI
site 0101D   ; OUTI
site 0101F   ; OUTI
site 01021   ; OUTI
site 01023   ; OUTI
site 01025   ; OUTI
site 01027   ; OUTI
site 01029   ; OUTI
site 0102B   ; OUTI
site 0102D   ; OUTI
site 0102F   ; OUTI
site 01031   ; OUTI
site 01033   ; OUTI
site 01037   ; OUT ($BF),A
site 0103B   ; OUT ($BF),A
site 0103E   ; OUTI
site 01040   ; OUTI
site 01042   ; OUTI
site 01044   ; OUTI
site 01046   ; OUTI
site 01048   ; OUTI
site 0104A   ; OUTI
site 0104C   ; OUTI
site 0104E   ; OUTI
site 01050   ; OUTI
site 01052   ; OUTI
site 01054   ; OUTI
site 01056   ; OUTI
site 01058   ; OUTI
site 0105A   ; OUTI
site 0105C   ; OUTI
site 0105E   ; OUTI
site 01060   ; OUTI
site 01062   ; OUTI
site 01064   ; OUTI
site 01066   ; OUTI
site 01068   ; OUTI
site 0106A   ; OUTI
site 0106C   ; OUTI
site 0106E   ; OUTI
site 01070   ; OUTI
site 01072   ; OUTI
site 01074   ; OUTI
site 01076   ; OUTI
site 01078   ; OUTI
site 0107A   ; OUTI
site 0107C   ; OUTI
site 0107E   ; OUTI
site 01080   ; OUTI
site 01082   ; OUTI
site 01084   ; OUTI
site 01086   ; OUTI
site 01088   ; OUTI
site 0108A   ; OUTI
site 0108C   ; OUTI
site 0108E   ; OUTI
site 01090   ; OUTI
site 01092   ; OUTI
site 01094   ; OUTI
site 01096   ; OUTI
site 01098   ; OUTI
site 0109A   ; OUTI
site 0109C   ; OUTI
site 0109E   ; OUTI
site 010A0   ; OUTI
site 010A2   ; OUTI
site 010A4   ; OUTI
site 010A6   ; OUTI
site 010A8   ; OUTI
site 010AA   ; OUTI
site 010AC   ; OUTI
site 010AE   ; OUTI
site 010B0   ; OUTI
site 010B2   ; OUTI
site 010B4   ; OUTI
site 010B6   ; OUTI
site 010B8   ; OUTI
site 010BA   ; OUTI
site 010BC   ; OUTI
site 010BE   ; OUTI
site 010C0   ; OUTI
site 010C2   ; OUTI
site 010C4   ; OUTI
site 010C6   ; OUTI
site 010C8   ; OUTI
site 010CA   ; OUTI
site 010CC   ; OUTI
site 010CE   ; OUTI
site 010D0   ; OUTI
site 010D2   ; OUTI
site 010D4   ; OUTI
site 010D6   ; OUTI
site 010D8   ; OUTI
site 010DA   ; OUTI
site 010DC   ; OUTI
site 010DE   ; OUTI
site 010E0   ; OUTI
site 010E2   ; OUTI
site 010E4   ; OUTI
site 010E6   ; OUTI
site 010E8   ; OUTI
site 010EA   ; OUTI
site 010EC   ; OUTI
site 010EE   ; OUTI
site 010F0   ; OUTI
site 010F2   ; OUTI
site 010F4   ; OUTI
site 010F6   ; OUTI
site 010F8   ; OUTI
site 010FA   ; OUTI
site 010FC   ; OUTI
site 010FE   ; OUTI
site 01100   ; OUTI
site 01102   ; OUTI
site 01104   ; OUTI
site 01106   ; OUTI
site 01108   ; OUTI
site 0110A   ; OUTI
site 0110C   ; OUTI
site 0110E   ; OUTI
site 01110   ; OUTI
site 01112   ; OUTI
site 01114   ; OUTI
site 01116   ; OUTI
site 01118   ; OUTI
site 0111A   ; OUTI
site 0111C   ; OUTI
site 0111E   ; OUTI
site 01120   ; OUTI
site 01122   ; OUTI
site 01124   ; OUTI
site 01126   ; OUTI
site 01128   ; OUTI
site 0112A   ; OUTI
site 0112C   ; OUTI
site 0112E   ; OUTI
site 01130   ; OUTI
site 01132   ; OUTI
site 01134   ; OUTI
site 01136   ; OUTI
site 01138   ; OUTI
site 0113A   ; OUTI
site 0113C   ; OUTI
site 01148   ; OUT ($BF),A
site 0114E   ; OUT ($BF),A
site 0115E   ; OUTI
site 01160   ; OUTI
site 01162   ; OUTI
site 01164   ; OUTI
site 01166   ; OUTI
site 01168   ; OUTI
site 0116A   ; OUTI
site 0116C   ; OUTI
site 0116E   ; OUTI
site 01170   ; OUTI
site 01172   ; OUTI
site 01174   ; OUTI
site 01176   ; OUTI
site 01178   ; OUTI
site 0117A   ; OUTI
site 0117C   ; OUTI
site 0117E   ; OUTI
site 01180   ; OUTI
site 01182   ; OUTI
site 01184   ; OUTI
site 01186   ; OUTI
site 01188   ; OUTI
site 0118A   ; OUTI
site 0118C   ; OUTI
site 0118E   ; OUTI
site 01190   ; OUTI
site 01192   ; OUTI
site 01194   ; OUTI
site 01196   ; OUTI
site 01198   ; OUTI
site 0119A   ; OUTI
site 0119C   ; OUTI
site 0125A   ; OUT ($BE),A
site 0125F   ; OUT ($BE),A
site 01264   ; OUT ($BE),A
site 01269   ; OUT ($BE),A
site 012D1   ; OUT ($BE),A
site 012D8   ; OUT ($BE),A
site 012DD   ; OUT ($BE),A
site 012EA   ; OUT ($BE),A
site 02BDE   ; OUT ($BE),A
site 02C23   ; OUT ($BE),A
site 02C2E   ; OUT ($BE),A
site 02C58   ; OUT ($BE),A
site 02C64   ; OUT ($BE),A
site 032FE   ; OUT ($BE),A
site 03306   ; OUT ($BE),A
site 04316   ; OUT ($7F),A
site 0431C   ; OUT ($7F),A
site 04327   ; OUT ($7F),A
site 0432E   ; OUT ($7F),A
site 04336   ; OUT ($7F),A
site 04665   ; OUT ($BE),A
site 0466A   ; OUT ($BE),A
site 04713   ; OUT ($BE),A
site 04718   ; OUT ($BE),A
site 07EA7   ; OUT ($BE),A
mapst 000D3   ; LD ($FFFF),A
mapst 00272   ; LD ($FFFF),A
mapst 002C1   ; LD ($FFFF),A
mapst 00755   ; LD ($FFFF),A
mapst 00846   ; LD ($FFFF),A
mapst 00864   ; LD ($FFFF),A
mapst 0090C   ; LD ($FFFF),A
mapst 009A3   ; LD ($FFFF),A
mapst 009E3   ; LD ($FFFF),A
mapst 00A1B   ; LD ($FFFF),A
mapst 00B87   ; LD ($FFFF),A
mapst 00BD1   ; LD ($FFFF),A
mapst 00C19   ; LD ($FFFF),A
mapst 00DD4   ; LD ($FFFF),A
mapst 00EB5   ; LD ($FFFF),A
mapst 00EED   ; LD ($FFFF),A
mapst 01154   ; LD ($FFFF),A
mapst 011AC   ; LD ($FFFF),A
mapst 011DD   ; LD ($FFFF),A
mapst 01226   ; LD ($FFFF),A
mapst 012A0   ; LD ($FFFF),A
mapst 012FA   ; LD ($FFFF),A
mapst 0132B   ; LD ($FFFF),A
mapst 0136D   ; LD ($FFFF),A
mapst 013E9   ; LD ($FFFF),A
mapst 01457   ; LD ($FFFF),A
mapst 01735   ; LD ($FFFF),A
mapst 01986   ; LD ($FFFF),A
mapst 01F25   ; LD ($FFFF),A
mapst 022EC   ; LD ($FFFF),A
mapst 0231E   ; LD ($FFFF),A
mapst 0236D   ; LD ($FFFF),A
mapst 023A8   ; LD ($FFFF),A
mapst 02B46   ; LD ($FFFF),A
mapst 0332F   ; LD ($FFFF),A
mapst 0384F   ; LD ($FFFF),A
mapst 03906   ; LD ($FFFF),A
mapst 03952   ; LD ($FFFF),A
mapst 03989   ; LD ($FFFF),A
mapst 03A43   ; LD ($FFFF),A
mapst 03A8D   ; LD ($FFFF),A
mapst 03B2E   ; LD ($FFFF),A
mapst 03B32   ; LD ($FFFF),A
mapst 03D09   ; LD ($FFFF),A
mapst 040E1   ; LD ($FFFF),A
mapst 0413E   ; LD ($FFFF),A
mapst 04274   ; LD ($FFFF),A
mapst 047AD   ; LD ($FFFF),A
mapst 056FA   ; LD ($FFFF),A
mapst 05733   ; LD ($FFFF),A
mapst 05C5D   ; LD ($FFFF),A
mapst 05F10   ; LD ($FFFF),A
mapst 05FE5   ; LD ($FFFF),A
mapst 0719C   ; LD ($FFFF),A
mapst 07302   ; LD ($FFFF),A
mapst 07A14   ; LD ($FFFF),A
mapst 07BD9   ; LD ($FFFF),A
site 00A73   ; byte scan, code (see Decisions)
site 00A7B   ; byte scan, code (see Decisions)
site 02D60   ; byte scan, code (see Decisions)
site 02D68   ; byte scan, code (see Decisions)
site 02D70   ; byte scan, code (see Decisions)
site 02D78   ; byte scan, code (see Decisions)
site 02D80   ; byte scan, code (see Decisions)
site 02D88   ; byte scan, code (see Decisions)
site 04EEE   ; byte scan, code (see Decisions)
site 04EF5   ; byte scan, code (see Decisions)
site 057D4   ; byte scan, code (see Decisions)
site 057DC   ; byte scan, code (see Decisions)

# Olympic Gold (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv).cht, "Infinite Arrows" (009-75B-3BE): the
# patch at $4975 stops the archery arrow count from going down (the byte is in banks 1 and 3)
poke "Infinite arrows"
gg 009-75B-3BE
endpoke

# Olympic Gold (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv).cht, "Start with ?? Arrows" (0A5-D6B-F72): the
# patch at $45D6 sets the number of arrows an archery round starts with (bank 1)
poke "Start arrows"
gg ??5-D6B-F72
endpoke

# Olympic Gold (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv).cht, "Infinite Stamina - Swimming"
# (669-E88-3BB): the patch at $79E8 keeps the swimmer's stamina bar full (bank 1)
poke "Infinite stamina"
gg 669-E88-3BB
endpoke
