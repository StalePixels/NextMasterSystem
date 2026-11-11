# Mortal Kombat 3 (Brazil) (En), CRC32 395AE757, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a 600 s reference I/O log (random input),
# then decided by hand. Every I/O and mapper site in the log is one the static scan finds.
#
# Decisions:
# - The power-on code at $0307-$0313, and the same code at $0CD5-$0CE1 (called from the start
#   code at $09CD), set the mapper with four LD (HL),A stores ($FFFC=0, $FFFD=0, $FFFE=1, $FFFF=2),
#   a form no spec line takes. Asm blocks store $FFFC, $FFFE and $FFFF through the runtime's
#   mapper store (inline codes $10, $12 and $13, the third byte skipped).
# - $1D7E and $1E35 (the source pointer step of the streamers $1CDA and $1DC9) are LD HL,$FFFF :
#   INC (HL) : LD HL,$8000, the next bank in slot 2 when the pointer passes $BFFF. Code caves
#   far-call page 0 entry binc, which does the same through the runtime's mapper store.
# - The LD ($FFFF),A stores at $0894, $08A0 (the sound driver calls into bank 31), $19E3,
#   $1A3F, $233D and $5897, which no scan path reaches, are real code: each sits in a whole
#   routine after a RET, beside stores the scan does reach.
# - Spec gaps (data/scan-verdicts.tsv): all false, an operand ($54C9), graphics (bank 19) and a
#   table (bank 26).
# - Page 1's entries do the game's costliest work (the fighter tile compositor and the screen
#   streamer) and hold each game step at the Master System's rate; see the blocks below.
name Mortal Kombat 3
cart 395AE757
hz 60		; No-Intro region Brazil
vector 08 io
asm 00302 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00307 13         ; LD HL,$FFFC : XOR A : LD (HL),A : INC L : LD (HL),A : INC L : INC A : LD (HL),A : INC L : INC A : LD (HL),A
    xor a
    rst $08
    db $10,$FF
    inc a
    rst $08
    db $12,$FF
    inc a
    rst $08
    db $13,$FF
endasm
asm 00CD5 13         ; the same at $0CD5
    xor a
    rst $08
    db $10,$FF
    inc a
    rst $08
    db $12,$FF
    inc a
    rst $08
    db $13,$FF
endasm
asm 01D7E 7          ; LD HL,$FFFF : INC (HL) : LD HL,$8000
    rst $08
    db far_io, pg_binc, ent_binc
endasm
asm 01E35 7          ; LD HL,$FFFF : INC (HL) : LD HL,$8000
    rst $08
    db far_io, pg_binc, ent_binc
endasm
page 0 binc
; binc: as LD HL,$FFFF : INC (HL) : LD HL,$8000: the slot 2 bank plus one, stored through the
; runtime's mapper store (inline code $13, LD ($FFFF),A, its third byte skipped). Returns
; HL = $8000; A and F changed (the game's POP AF after each cave restores them).
binc:   ld a,($FFFF)
        inc a
        rst $08
        db $13, $FF
        ld hl,$8000
        ret
endpage
# Fighter tile compositor $3343 (bank 0), a task the main loop $358F runs twice a game step (10
# then 15 list entries, B). It runs with SP on the list at $CD68: each entry is a bank for slot 2
# and a pointer to 64 bytes of fighter graphics, and makes two tiles: for each tile row the
# background row is read from VRAM (tile $100 + n, from the pairs at $CE9A, mirrored through the
# table at $7E00 when the pair's flag differs from $CF58), masked and ORed with the fighter row,
# and written at the VRAM address $CD6A. Every byte was a runtime call (with the address writes
# of $05BD and $05BF, about half of the runtime's time in a fight, and the fight ran at about
# two thirds of the Master System's speed). The cave at $3347 (EXX : LD SP,($CD68)) far-calls page
# 1 entry comp, which does the whole task on its own stack, then returns as $34F8 does.
asm 03347 5          ; EXX : LD SP,($CD68)
    rst $08
    db far_io, pg_comp, ent_comp
    ret
endasm
# Step rate. A game step is the pass $358F: logic, a frame wait ($0777 from $0396), the
# compositor (10 entries) and the screen streamer $2E2B, logic, a wait, the compositor (15
# entries) and the streamer $2E32. On a Master System that work takes 2 to 5 frames after each
# wait (sg1000m3: mostly 4 and 5); the Next, with page 1, does it in 1 or 2 and played a fight
# about a fifth faster, and at that rate the second fighter's tiles were wrong in most frames.
# Page 1 counts the Master System cycles of the compositor (exact, entry by entry) and of the
# streamer (rows of 64 bytes), and the wait holds until as many frame events have passed since
# the last wait as a Master System needs for that work. Screens without the compositor and the
# streamer wait one frame, as before.
asm 00777 11         ; EI : XOR A : LD ($D3EE),A : the loop to JR NZ,$077C (the RET at $0782 stays)
    rst $08
    db far_io, pg_wait, ent_wait
endasm
# Screen streamer $2E32 (bank 0): B rows from the list at $CEC5 (a bank for slot 2, a mode and a
# source), 64 bytes each (OUTI or OUTD with DJNZ counts B down twice a byte), written one after
# another from the VRAM address $CEC7: forward (OUTI), backward (OUTD), or through the mirror
# table at $7E00 either way. Each row was a runtime block of
# about 21,000 cycles, and 32 rows filled more than a Next frame. The cave far-calls page 1
# entry strm, which builds each row in a buffer and writes it with jt_vwrite, then EI : RET as
# the game's $2E90.
asm 02E32 6          ; LD ($CEB7),SP : LD C,$BF
    rst $08
    db far_io, pg_strm, ent_strm
    ei
    ret
endasm
page 1 comp strm wait
; comp: as the game's $3347-$34FC with SP restored from $CEB9 (the SP at $3347). For each list
; entry (B of them, ended early by an entry with $FF in its low byte): the slot 2 bank through the
; runtime's mapper store, IX = the graphics, two tiles. Each tile: the 32 bytes at VRAM $2000 +
; 32n read from the VRAM copy (SHADOW_PAGE 28-29, in slot 0 with interrupts off), mirrored through
; $7E00+v when ($CEBB) differs from ($CF58), each row ANDed with NOT the OR of its 4 fighter bytes
; and ORed with them, then written at ($CD6A) with one jt_vwrite. The game's variables $CD68,
; $CE9A, $CEB3, $CEB5-$CEB8, $CEBB and $CD6A are left as its code leaves them, and so are the
; registers: the EXX parity, B, C (the last mask), DE = 4, HL = ($CD6A), IX past the graphics,
; A and the flags. Interrupts: off after the first entry, as after the game's $05BF; with no
; entry done they are as at entry.
; Runtime internals used: jt_vwrite, jt_peek, cur_mmu, SHADOW_PAGE (28).
comp:   ld (g_sp),sp
        ld sp,stk_top
        push af
        ld a,i                  ; P/V = IFF2
        di
        ld a,0
        jp po,.di
        inc a
.di:    ld (ei_f),a
        xor a
        ld (did),a
        pop af
.top:   exx
        ld hl,($CD68)
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,e
        cp $FF
        jr z,.out               ; the end of the list: $CD68 stays
        ld a,d
        rst $08
        db $13,$FF              ; LD ($FFFF),A
        ld c,(hl)
        inc hl
        ld b,(hl)
        inc hl
        ld ($CD68),hl
        push bc
        pop ix
        ld a,1
        ld (did),a
        ld hl,124               ; Master System cycles of the entry's own code
        call addacc
        call half
        call half
        exx
        dec b
        jr nz,.top
        ld a,($CEB8)            ; A as the game leaves it; F as DEC B
.out:   push af
        ld a,(did)
        or a
        jr nz,.keep
        ld a,(ei_f)
        or a
        jr z,.keep
        pop af
        ld sp,(g_sp)
        ei
        ret
.keep:  pop af
        ld sp,(g_sp)
        ret
; half: one tile. Uses and leaves the main set as the game's inner loop does.
half:   ld hl,($CE9A)
        ld a,(hl)
        inc hl
        ld c,(hl)
        inc hl
        ld ($CE9A),hl
        ld l,a
        ld h,1
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl               ; $2000 + 32n
        ld ($CEB3),hl
        srl c
        ld a,c
        ld ($CEBB),a
        ld hl,$CF58
        xor (hl)
        ld (flip),a
        ld hl,($CEB3)           ; the background tile from the VRAM copy
        ld a,h
        and $20
        rlca
        rlca
        rlca
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a: the VRAM copy in slot 0
        ld a,h
        and $1F
        ld h,a
        ld de,vbuf
        ld bc,32
        ldir
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 back
        push ix                 ; the fighter rows as the game sees them
        pop hl
        ld de,fbuf
        ld b,32
.fb:    ld a,h
        and $E0
        cp $20
        jr nz,.fd
        call jt_peek
        jr .fs
.fd:    ld a,(hl)
.fs:    ld (de),a
        inc hl
        inc de
        djnz .fb
        ld de,32
        add ix,de
        ld hl,6176              ; Master System cycles of the tile, 8 rows not mirrored
        ld a,(flip)
        or a
        jr z,.nf
        ld hl,6528              ; mirrored: 44 more a row
.nf:    call addacc
        ld a,(flip)
        or a
        jr z,.nofl
        ld hl,vbuf
        ld b,32
.fl:    ld e,(hl)
        ld d,$7E
        ld a,(de)
        ld (hl),a
        inc hl
        djnz .fl
.nofl:  ld hl,fbuf
        ld de,vbuf
        ld b,8
.g:     push bc
        ld a,(hl)
        inc hl
        or (hl)
        inc hl
        or (hl)
        inc hl
        or (hl)
        dec hl
        dec hl
        dec hl
        cpl
        ld c,a                  ; the mask
        ld b,4
.r:     ld a,(de)
        and c
        or (hl)
        ld (de),a
        inc hl
        inc de
        djnz .r
        ld a,c
        ld (lastm),a
        pop bc
        djnz .g
        ld hl,vbuf+28
        ld de,$CEB5
        ld bc,4
        ldir
        ld hl,($CEB3)
        ld de,32
        add hl,de
        ld ($CEB3),hl
        push iy                 ; the tile, with every register kept
        push ix
        exx
        push bc
        push de
        push hl
        exx
        ex af,af'
        push af
        ex af,af'
        ld hl,vbuf
        ld de,($CD6A)
        ld bc,$2001             ; 32 bytes, one run
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        pop af
        ex af,af'
        exx
        pop hl
        pop de
        pop bc
        exx
        pop ix
        pop iy
        ld hl,($CD6A)
        ld de,32
        add hl,de
        ld ($CD6A),hl
        ld a,(lastm)
        ld c,a
        ld b,0
        ld de,4
        ret
; addacc: acc += HL (saturating at $FFFF... in 32 bits). Keeps BC, DE, HL; A and F changed.
addacc: push hl
        push de
        ex de,hl
        ld hl,(acc)
        add hl,de
        ld (acc),hl
        jr nc,.n
        ld hl,acc+2
        inc (hl)
.n:     pop de
        pop hl
        ret
; strm: as the game's $2E32-$2E8F (it returns to EI : RET). $CEB7 = the game's SP; the VDP
; address = ($CEC7) through the runtime (OUT ($BF) twice, as the game's code); then for each of B
; rows (with the EXX of the game's loop): a list entry DE, HL from ($CEC5); D = $AA ends the list
; (the alternate set stays in use, as at the game's JR Z,$2E8C); else D to the mapper, ($CEC5)
; past the entry, ($CEB3) = HL and the row by mode E: bit 0 = through the table at $7E00 with
; only L stepping, bit 1 = backward from HL+63. The rows go one after another in VRAM, while
; the main set's HL steps by $40 a row and ends in ($CEC7) when all B rows are done. Each row
; adds 2090 Master System cycles to acc. Interrupts off at the end, as at the game's $2E8C.
; Registers as the game's code leaves them: the main set's B (0 when all rows are done), DE =
; $40, HL; the alternate set's DE (DE = $003F after a backward row), HL past the row, B = 0,
; C = $BE after a plain row; A and F changed.
strm:   di
        ld (g_sp),sp
        push hl
        ld hl,6
        add hl,sp
        inc hl
        inc hl                  ; the push
        ld ($CEB7),hl
        pop hl
        ld sp,stk_top
        ld c,$BF
        ld hl,($CEC7)
        ld a,l
        rst $08
        db $05                  ; OUT ($BF),A: the address's low byte
        ld a,h
        set 6,a
        rst $08
        db $05
        ld (vaddr),hl
        ld de,$0040
.row:   exx
        ld hl,($CEC5)
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,d
        cp $AA
        jr z,.end
        rst $08
        db $13,$FF              ; LD ($FFFF),A
        ld c,(hl)
        inc hl
        ld b,(hl)
        inc hl
        ld ($CEC5),hl
        ld h,b
        ld l,c
        ld ($CEB3),hl
        push de
        ld de,2090
        ex de,hl
        call addacc
        ex de,hl
        pop de
        call srow
        exx
        add hl,de
        djnz .row
        ld ($CEC7),hl
.end:   ld sp,(g_sp)
        ret
; srow: one row of 64 bytes from HL in mode E (alternate set in use) to (vaddr). Leaves the
; set as the game's code does; IX and IY kept.
srow:   ld a,e
        and 3
        ld (smode),a
        ld de,sbuf
        ld b,64
        dec a
        jr z,.tf                ; mode 1: table, forward
        dec a
        jr z,.bk                ; mode 2: backward
        dec a
        jr z,.tb                ; mode 3: table, backward
.fw:    call rdhl               ; mode 0
        ld (de),a
        inc hl
        inc de
        djnz .fw
        ld bc,$00BE
        jr .out
.tf:    call rdhl
        push hl
        ld l,a
        ld h,$7E
        ld a,(hl)
        pop hl
        ld (de),a
        inc l
        inc de
        djnz .tf
        ld d,$7E
        ld e,a                  ; not the game's E: set below
        jr .out
.bk:    push hl
        ld bc,63
        add hl,bc
        ld b,64
.bkl:   call rdhl
        ld (de),a
        dec hl
        inc de
        djnz .bkl
        pop hl
        ld bc,64
        add hl,bc
        ld bc,$00BE
        ld de,$003F
        jr .out
.tb:    push hl
        ld a,l
        add a,63
        ld l,a
        jr nc,.tb0
        inc h
.tb0:   call rdhl
        push hl
        ld l,a
        ld h,$7E
        ld a,(hl)
        pop hl
        ld (de),a
        dec l
        inc de
        djnz .tb0
        pop hl
        inc hl
        ld de,$003F
.out:   push iy
        push ix
        push hl
        push de
        push bc
        ld hl,sbuf
        ld de,(vaddr)
        ld bc,$4001             ; 64 bytes, one run
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        ld hl,(vaddr)
        ld de,64
        add hl,de
        ld (vaddr),hl
        pop bc
        pop de
        pop hl
        pop ix
        pop iy
        ld a,(smode)
        cp 1
        ret nz
        ld de,$7E00             ; mode 1 leaves D = $7E and E = the last source byte
        dec l
        ld e,(hl)
        inc l
        ret
; rdhl: A = the byte the game sees at HL. Keeps every register but A and F.
rdhl:   ld a,h
        and $E0
        cp $20
        jp z,jt_peek
        ld a,(hl)
        ret
; wait: as the game's $0777-$0781 (EI, $D3EE cleared, wait until the frame handler sets it to 1),
; returns to the RET at $0782 with A = 0, Z set, interrupts on. With work counted in acc, the
; wait is made again until the frame events since the last wait cover acc plus OFF Master
; System cycles at FE cycles a frame. Runs on the game's stack, with interrupts on while it
; waits, as the game's loop does. Keeps BC, DE, HL.
; FE and OFF come from fights paired with the reference (sg1000m3, the same input): with them
; the step counter $D3E9 runs at 0.232 a frame on the Next against 0.234 on the reference.
FE      equ 52000               ; Master System cycles a frame for the main loop's work
OFF     equ 55000               ; and the logic between two waits besides the counted work
wait:   push hl
        push de
        push bc
        ld hl,(acc)
        ld a,(acc+2)
        ld c,a
        ld b,0                  ; frames the work needs
        ld a,h
        or l
        or c
        jr z,.go
        ld de,OFF
        add hl,de
        jr nc,.f
        inc c
.f:     ld de,FE                ; B = C:HL / FE, rounded up
.dv:    inc b
        or a
        sbc hl,de
        ld a,c
        sbc a,0
        ld c,a
        jr c,.go
        ld a,h
        or l
        or c
        jr nz,.dv
.go:    ld a,(s0)               ; frames since the last wait's end
        ld c,a
        ld a,(isr_n)
        sub c
        ld c,a
        ld a,b
        sub c                   ; frames still needed
        jr z,.one
        jr nc,.set
.one:   ld a,1                  ; always the one wait of the game's loop
.set:   ld (need),a
.w:     xor a
        ld ($D3EE),a
        ei
.p:     ld a,($D3EE)
        dec a
        jr nz,.p
        ld a,(need)
        dec a
        ld (need),a
        jr nz,.w
        ld a,(isr_n)
        ld (s0),a
        ld hl,0
        ld (acc),hl
        ld (acc+2),hl
        pop bc
        pop de
        pop hl
        xor a
        ret
acc:    ds 4
vaddr:  dw 0
smode:  db 0
sbuf:   ds 64
s0:     db 0
need:   db 0
flip:   db 0
lastm:  db 0
did:    db 0
ei_f:   db 0
g_sp:   dw 0
vbuf:   ds 32
fbuf:   ds 32
stk:    ds 96
stk_top:
endpage
# Second fighter's name table cells. After each step's first wait (when $D3E9 is odd), $03DD calls
# $32C9 (put the background back in the cells of the list at $CD6C+X, X = ($CE99), from the save at
# $CDD0+2X), $3131 (the new cell list at $CD6C+X), $3274 (save the background under the new cells
# from VRAM at $CDD0+2X) and $3205 (write the fighter's cells of the list at $CD6C+(X XOR $32),
# tiles $15C+(X XOR $32) on). Between the first and the last of these the name table has no
# fighter. On a Master System the block ends in the border; on the Next its VDP traps took 100 to
# 160 lines, so the fighter was missing from the frame whenever the raster passed it in that
# time. The cave runs page 2: ntsave keeps the restore without writing it, $3131 runs as before,
# and ntput reads the background from the VRAM copy (with the kept restore on top), then writes
# the restored cells and the fighter's cells at once.
asm 003DD 12         ; CALL $32C9 : CALL $3131 : CALL $3274 : CALL $3205
    rst $08
    db far_io, pg_ntsave, ent_ntsave
    call $3131
    rst $08
    db far_io, pg_ntput, ent_ntput
    nop
endasm
page 2 ntsave ntput
; ntsave: as $32C9 without its VDP writes. With the same checks ($D39A = 6, the list's or the
; save's first byte $FF: nothing to restore), it copies the ($CE98) entries (0 = 256) of the old
; cell list and their saved background into rlist (per cell: VRAM address, 2 bytes) and leaves
; $CEB9 and $CEB3 as the game's code does. Registers other than SP are not kept ($3131 follows).
; ntput: as $3274 then $3205. The background under the new cells is read from the VRAM copy
; (SHADOW_PAGE 28-29 in slot 0, interrupts off), and a cell in rlist reads as rlist has it, as
; after the game's restore. Then the restored cells that no fighter cell covers, and the fighter's
; cells, are written with jt_vwrite: the same name table as the game's order leaves, with no time
; between taking the old fighter away and drawing the new one. Variables $CE98, $CEB3, $CEB7 and
; $CEB9 are left as the game leaves them, and IX and IY as $3205 leaves them; interrupts off.
; Cells lie in the name table $3800-$3FFF ($31C5 table), so (address AND $7FF)/2 indexes them.
; Runtime internals used: jt_vwrite, cur_mmu, SHADOW_PAGE (28).
ntsave: ld hl,0
        ld (rn),hl
        ld a,($D39A)
        cp 6
        ret z
        ld a,($CE99)
        ld e,a
        ld d,0
        ld hl,$CD6C
        add hl,de
        ld a,(hl)
        cp $FF
        ret z
        push hl                 ; the old cell list
        ld hl,$CDD0
        add hl,de
        add hl,de
        ld ($CEB9),hl
        ld a,(hl)
        cp $FF
        jr nz,.go
        pop hl
        ret
.go:    ex de,hl                ; DE = the saved background
        ld a,($CE98)
        ld l,a
        ld h,0
        or a
        jr nz,.n
        inc h                   ; 0 = 256 entries
.n:     add hl,hl               ; two cells an entry
        ld (rn),hl
        ld b,a
        pop hl
        ld ix,rlist
.lp:    ld c,(hl)
        inc hl
        ld a,(hl)
        inc hl
        ld (ix+0),c
        ld (ix+1),a
        ld (ix+5),a
        ld a,c
        add a,$40               ; the cell below
        ld (ix+4),a
        jr nc,.nc
        inc (ix+5)
.nc:    ld a,(de)
        ld (ix+2),a
        inc de
        ld a,(de)
        ld (ix+3),a
        inc de
        ld a,(de)
        ld (ix+6),a
        inc de
        ld a,(de)
        ld (ix+7),a
        inc de
        push de
        ld de,8
        add ix,de
        pop de
        djnz .lp
        xor a
        ld ($CEB3),a
        ret
ntput:  di
        ld hl,(rn)              ; the kept restore into ovl, marked with flags bit 0
        ld a,h
        or l
        jr z,.rd0
        ld (cnt),hl
        ld ix,rlist
.ra:    ld l,(ix+0)
        ld h,(ix+1)
        call cidx
        push hl
        ld de,flags
        add hl,de
        set 0,(hl)
        pop hl
        add hl,hl
        ld de,ovl
        add hl,de
        ld a,(ix+2)
        ld (hl),a
        inc hl
        ld a,(ix+3)
        ld (hl),a
        ld de,4
        add ix,de
        ld hl,(cnt)
        dec hl
        ld (cnt),hl
        ld a,h
        or l
        jr nz,.ra
.rd0:   ld a,($CE99)            ; $3274: the background under the new cells
        ld e,a
        ld d,0
        ld hl,$CD6C
        add hl,de
        push hl
        pop ix
        ld hl,$CDD0
        add hl,de
        add hl,de
        ld ($CEB9),hl
        ex de,hl
        ld a,($CF52)
        ld b,a                  ; 0 = 256
.rd:    ld l,(ix+0)
        ld h,(ix+1)
        call rcell
        push bc
        ld bc,$40
        add hl,bc
        pop bc
        call rcell
        inc ix
        inc ix
        djnz .rd
        xor a
        ld ($CEB3),a
        ld (fon),a
        ld a,($CF55)            ; $3205: the fighter's cells, marked with flags bit 1
        or a
        jr z,.wr
        ld a,($CE99)
        xor $32
        ld e,a
        ld d,0
        ld hl,$CD6C
        add hl,de
        ld a,(hl)
        cp $FF
        jr z,.wr
        ld (flst),hl
        ld hl,$015C
        add hl,de
        ld ($CEB9),hl
        ld (ftile),hl
        ld a,($CF53)
        ld ($CE98),a
        ld (fcnt),a
        ld a,($CF57)
        add a,a
        ld ($CEB7),a
        ld (fflag),a
        ld a,1
        ld (fon),a
        ld ix,(flst)
        ld a,(fcnt)
        ld b,a
.mk:    ld l,(ix+0)
        ld h,(ix+1)
        push hl
        call cidx
        ld de,flags
        add hl,de
        set 1,(hl)
        pop hl
        ld de,$40
        add hl,de
        call cidx
        ld de,flags
        add hl,de
        set 1,(hl)
        inc ix
        inc ix
        djnz .mk
.wr:    ld hl,(rn)              ; the restored cells no fighter cell covers
        ld a,h
        or l
        jr z,.wf
        ld (cnt),hl
        ld ix,rlist
.wa:    ld l,(ix+0)
        ld h,(ix+1)
        push hl
        call cidx
        ld de,flags
        add hl,de
        ld a,(hl)
        ld (hl),0               ; flags cleared as they are used
        pop de                  ; DE = the cell's VRAM address
        bit 1,a
        jr nz,.ws
        push ix
        pop hl
        inc hl
        inc hl
        push ix
        ld bc,$0201             ; 2 bytes, one run
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        pop ix
.ws:    ld de,4
        add ix,de
        ld hl,(cnt)
        dec hl
        ld (cnt),hl
        ld a,h
        or l
        jr nz,.wa
.wf:    ld a,(fon)              ; the fighter's cells, two a list entry
        or a
        ret z
        ld ix,(flst)
        ld a,(fcnt)
        ld b,a
.wl:    push bc
        ld hl,(ftile)
        ld a,(fflag)
        ld c,a
        ld a,l
        ld (tbuf),a
        ld a,h
        or c
        ld (tbuf+1),a
        inc hl
        ld a,l
        ld (tbuf+2),a
        ld a,h
        or c
        ld (tbuf+3),a
        inc hl
        ld (ftile),hl
        ld l,(ix+0)
        ld h,(ix+1)
        push hl
        call cidx
        ld de,flags
        add hl,de
        ld (hl),0
        pop hl
        push hl
        ld de,$40
        add hl,de
        call cidx
        ld de,flags
        add hl,de
        ld (hl),0
        pop de
        push ix
        ld hl,tbuf
        ld bc,$0202             ; 2 bytes, two runs: the cell and the cell below
        ld ix,2
        ld iy,$40
        ld a,1
        call jt_vwrite
        pop ix
        inc ix
        inc ix
        pop bc
        djnz .wl
        xor a
        ld ($CEB3),a
        ld iy,$CEB7
        ret
; cidx: HL = the cell index (address AND $7FF)/2 of the name table address HL. A and F changed.
cidx:   ld a,h
        and 7
        ld h,a
        srl h
        rr l
        ret
; rcell: the 2 bytes of the cell at VRAM address HL to (DE), DE += 2: from ovl when the cell is
; restored (flags bit 0), else from the VRAM copy. Keeps BC, HL and IX.
rcell:  push bc
        push hl
        call cidx
        push hl
        ld bc,flags
        add hl,bc
        bit 0,(hl)
        pop hl
        jr z,.v
        add hl,hl
        ld bc,ovl
        add hl,bc
        ld a,(hl)
        ld (de),a
        inc de
        inc hl
        ld a,(hl)
        ld (de),a
        inc de
        pop hl
        pop bc
        ret
.v:     pop hl
        push hl
        ld a,h
        and $20
        rlca
        rlca
        rlca
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a: the VRAM copy in slot 0
        ld a,h
        and $1F
        ld h,a
        ld a,(hl)
        ld (de),a
        inc de
        inc hl
        ld a,(hl)
        ld (de),a
        inc de
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0 back
        pop hl
        pop bc
        ret
rn:     dw 0
cnt:    dw 0
flst:   dw 0
ftile:  dw 0
fcnt:   db 0
fflag:  db 0
fon:    db 0
tbuf:   ds 4
rlist:  ds 2048
ovl:    ds 2048
flags:  ds 1024
endpage
site 0004B   ; IN A,($BF)
site 003B7   ; OUT ($BF),A
site 003BB   ; OUT ($BF),A
site 00558   ; OUT ($BF),A
site 0055C   ; OUT ($BF),A
site 00563   ; OUT ($BF),A
site 00567   ; OUT ($BF),A
site 0056E   ; OUT ($BF),A
site 00572   ; OUT ($BF),A
site 00590   ; OUT ($BF),A
site 0059A   ; OUT ($BF),A
site 005A3   ; OUT ($BE),A
site 005AB   ; OUT ($BE),A
site 005C1   ; OUT ($BF),A
site 005C4   ; OUT ($BF),A
site 0071E   ; OUT ($BF),A
site 00722   ; OUT ($BF),A
site 0072D   ; OUT ($BF),A
site 00731   ; OUT ($BF),A
site 0073B   ; OUT ($BF),A
site 0073F   ; OUT ($BF),A
site 0074A   ; OUT ($BF),A
site 0074E   ; OUT ($BF),A
site 00759   ; OUT ($BF),A
site 00760   ; OUT ($BF),A
site 0076F   ; OUT ($BE),A
site 00783   ; IN A,($DC)
site 00787   ; IN A,($DC)
site 0078C   ; IN A,($DD)
site 007CC   ; OUT ($BE),A
site 01658   ; OUT ($BE),A
site 018D6   ; OUTI
site 018E2   ; OUT ($BE),A
site 01CC6   ; OUT ($BF),A
site 01CCD   ; OUT ($BF),A
site 01CD4   ; OUT ($BE),A
site 01CDE   ; OUT ($BF),A
site 01CE5   ; OUT ($BF),A
site 01CF6   ; OUT ($BE),A
site 01D3A   ; OUT ($BF),A
site 01D41   ; OUT ($BF),A
site 01D47   ; IN A,($BE)
site 01D4F   ; OUT ($BF),A
site 01D58   ; OUT ($BF),A
site 01D5F   ; OUT ($BE),A
site 01EB6   ; OUT ($BE),A
site 01EBD   ; OUT ($BE),A
site 01EC4   ; OUT ($BE),A
site 01ECB   ; OUT ($BE),A
site 01EEE   ; OUT ($BE),A
site 01EF5   ; OUT ($BE),A
site 01EFC   ; OUT ($BE),A
site 01F03   ; OUT ($BE),A
site 0210B   ; OUT ($BF),A
site 02112   ; OUT ($BF),A
site 02119   ; OUT ($BE),A
site 02121   ; OUT ($BE),A
site 02132   ; OUT ($BF),A
site 02137   ; OUT ($BF),A
site 02154   ; OUT ($BE),A
site 0215C   ; OUT ($BE),A
site 02187   ; OUT ($BF),A
site 0218E   ; OUT ($BF),A
site 02195   ; OUT ($BE),A
site 0219D   ; OUT ($BE),A
site 021AE   ; OUT ($BF),A
site 021C0   ; OUT ($BF),A
site 021C7   ; OUT ($BE),A
site 021CF   ; OUT ($BE),A
site 02265   ; OUT ($BF),A
site 0226A   ; OUT ($BF),A
site 02280   ; OUT ($BE),A
site 02288   ; OUT ($BE),A
site 02295   ; OUT ($BF),A
site 0229A   ; OUT ($BF),A
site 022A1   ; OUT ($BE),A
site 022A9   ; OUT ($BE),A
site 022B6   ; OUT ($BF),A
site 022BB   ; OUT ($BF),A
site 022D0   ; OUT ($BE),A
site 022D8   ; OUT ($BE),A
site 022EA   ; OUT ($BF),A
site 022EF   ; OUT ($BF),A
site 022F6   ; OUT ($BE),A
site 022FE   ; OUT ($BE),A
site 0230B   ; OUT ($BF),A
site 02310   ; OUT ($BF),A
site 0235F   ; OUT ($BF),A
site 02363   ; OUT ($BF),A
site 02369   ; OUT ($BE),A
site 0236F   ; OUT ($BF),A
site 02373   ; OUT ($BF),A
site 02379   ; OUT ($BE),A
site 02A60   ; OUT ($BF),A
site 02A64   ; OUT ($BF),A
otir 02A6C   ; OUTI
site 02A72   ; OUT ($BF),A
site 02A76   ; OUT ($BF),A
otir 02A7D   ; OUTI
site 02AA9   ; OUT ($BF),A
site 02AAD   ; OUT ($BF),A
site 02AC5   ; OUTI
site 02AC7   ; OUTI
site 02AC9   ; OUTI
site 02ACB   ; OUTI
site 02ACD   ; OUTI
site 02ACF   ; OUTI
site 02AD1   ; OUTI
site 02AD3   ; OUTI
site 02AD5   ; OUTI
site 02AD7   ; OUTI
site 02AD9   ; OUTI
site 02ADB   ; OUTI
site 02ADD   ; OUTI
site 02ADF   ; OUTI
site 02AE1   ; OUTI
site 02AE3   ; OUTI
site 02AE5   ; OUTI
site 02AE7   ; OUTI
site 02AE9   ; OUTI
site 02AEB   ; OUTI
site 02AED   ; OUTI
site 02AEF   ; OUTI
site 02AF1   ; OUTI
site 02AF3   ; OUTI
site 02AF5   ; OUTI
site 02AF7   ; OUTI
site 02AF9   ; OUTI
site 02AFB   ; OUTI
site 02AFD   ; OUTI
site 02AFF   ; OUTI
site 02B01   ; OUTI
site 02B03   ; OUTI
site 02B05   ; OUTI
site 02B07   ; OUTI
site 02B09   ; OUTI
site 02B0B   ; OUTI
site 02B0D   ; OUTI
site 02B0F   ; OUTI
site 02B11   ; OUTI
site 02B13   ; OUTI
site 02B15   ; OUTI
site 02B17   ; OUTI
site 02B19   ; OUTI
site 02B1B   ; OUTI
site 02B1D   ; OUTI
site 02B1F   ; OUTI
site 02B21   ; OUTI
site 02B23   ; OUTI
site 02B25   ; OUTI
site 02B27   ; OUTI
site 02B29   ; OUTI
site 02B2B   ; OUTI
site 02B2D   ; OUTI
site 02B2F   ; OUTI
site 02B31   ; OUTI
site 02B33   ; OUTI
site 02B35   ; OUTI
site 02B37   ; OUTI
site 02B39   ; OUTI
site 02B3B   ; OUTI
site 02B3D   ; OUTI
site 02B3F   ; OUTI
site 02B41   ; OUTI
site 02B43   ; OUTI
site 02B5D   ; OUTI
site 02B5F   ; OUTI
site 02B61   ; OUTI
site 02B63   ; OUTI
site 02B65   ; OUTI
site 02B67   ; OUTI
site 02B69   ; OUTI
site 02B6B   ; OUTI
site 02B6D   ; OUTI
site 02B6F   ; OUTI
site 02B71   ; OUTI
site 02B73   ; OUTI
site 02B75   ; OUTI
site 02B77   ; OUTI
site 02B79   ; OUTI
site 02B7B   ; OUTI
site 02B7D   ; OUTI
site 02B7F   ; OUTI
site 02B81   ; OUTI
site 02B83   ; OUTI
site 02B85   ; OUTI
site 02B87   ; OUTI
site 02B89   ; OUTI
site 02B8B   ; OUTI
site 02B8D   ; OUTI
site 02B8F   ; OUTI
site 02B91   ; OUTI
site 02B93   ; OUTI
site 02B95   ; OUTI
site 02B97   ; OUTI
site 02B99   ; OUTI
site 02B9B   ; OUTI
site 02B9D   ; OUTI
site 02B9F   ; OUTI
site 02BA1   ; OUTI
site 02BA3   ; OUTI
site 02BA5   ; OUTI
site 02BA7   ; OUTI
site 02BA9   ; OUTI
site 02BAB   ; OUTI
site 02BAD   ; OUTI
site 02BAF   ; OUTI
site 02BB1   ; OUTI
site 02BB3   ; OUTI
site 02BB5   ; OUTI
site 02BB7   ; OUTI
site 02BB9   ; OUTI
site 02BBB   ; OUTI
site 02BBD   ; OUTI
site 02BBF   ; OUTI
site 02BC1   ; OUTI
site 02BC3   ; OUTI
site 02BC5   ; OUTI
site 02BC7   ; OUTI
site 02BC9   ; OUTI
site 02BCB   ; OUTI
site 02BCD   ; OUTI
site 02BCF   ; OUTI
site 02BD1   ; OUTI
site 02BD3   ; OUTI
site 02BD5   ; OUTI
site 02BD7   ; OUTI
site 02BD9   ; OUTI
site 02BDB   ; OUTI
site 02BF0   ; OUT ($BF),A
site 02BF4   ; OUT ($BF),A
site 02C0D   ; OUTI
site 02C0F   ; OUTI
site 02C11   ; OUTI
site 02C13   ; OUTI
site 02C15   ; OUTI
site 02C17   ; OUTI
site 02C19   ; OUTI
site 02C1B   ; OUTI
site 02C1D   ; OUTI
site 02C1F   ; OUTI
site 02C21   ; OUTI
site 02C23   ; OUTI
site 02C25   ; OUTI
site 02C27   ; OUTI
site 02C29   ; OUTI
site 02C2B   ; OUTI
site 02C2D   ; OUTI
site 02C2F   ; OUTI
site 02C31   ; OUTI
site 02C33   ; OUTI
site 02C35   ; OUTI
site 02C37   ; OUTI
site 02C39   ; OUTI
site 02C3B   ; OUTI
site 02C3D   ; OUTI
site 02C3F   ; OUTI
site 02C41   ; OUTI
site 02C43   ; OUTI
site 02C45   ; OUTI
site 02C47   ; OUTI
site 02C49   ; OUTI
site 02C4B   ; OUTI
site 02C4D   ; OUTI
site 02C4F   ; OUTI
site 02C51   ; OUTI
site 02C53   ; OUTI
site 02C55   ; OUTI
site 02C57   ; OUTI
site 02C59   ; OUTI
site 02C5B   ; OUTI
site 02C5D   ; OUTI
site 02C5F   ; OUTI
site 02C61   ; OUTI
site 02C63   ; OUTI
site 02C65   ; OUTI
site 02C67   ; OUTI
site 02C69   ; OUTI
site 02C6B   ; OUTI
site 02C6D   ; OUTI
site 02C6F   ; OUTI
site 02C71   ; OUTI
site 02C73   ; OUTI
site 02C75   ; OUTI
site 02C77   ; OUTI
site 02C79   ; OUTI
site 02C7B   ; OUTI
site 02C7D   ; OUTI
site 02C7F   ; OUTI
site 02C81   ; OUTI
site 02C83   ; OUTI
site 02C85   ; OUTI
site 02C87   ; OUTI
site 02C89   ; OUTI
site 02C8B   ; OUTI
site 02C8D   ; OUTI
site 02C8F   ; OUTI
site 02C91   ; OUTI
site 02C93   ; OUTI
site 02C95   ; OUTI
site 02C97   ; OUTI
site 02C99   ; OUTI
site 02C9B   ; OUTI
site 02C9D   ; OUTI
site 02C9F   ; OUTI
site 02CA1   ; OUTI
site 02CA3   ; OUTI
site 02CA5   ; OUTI
site 02CA7   ; OUTI
site 02CA9   ; OUTI
site 02CAB   ; OUTI
site 02CAD   ; OUTI
site 02CAF   ; OUTI
site 02CB1   ; OUTI
site 02CB3   ; OUTI
site 02CB5   ; OUTI
site 02CB7   ; OUTI
site 02CB9   ; OUTI
site 02CBB   ; OUTI
site 02CBD   ; OUTI
site 02CBF   ; OUTI
site 02CC1   ; OUTI
site 02CC3   ; OUTI
site 02CC5   ; OUTI
site 02CC7   ; OUTI
site 02CC9   ; OUTI
site 02CCB   ; OUTI
site 02CCD   ; OUTI
site 02CCF   ; OUTI
site 02CD1   ; OUTI
site 02CD3   ; OUTI
site 02CD5   ; OUTI
site 02CD7   ; OUTI
site 02CD9   ; OUTI
site 02CDB   ; OUTI
site 02CDD   ; OUTI
site 02CDF   ; OUTI
site 02CE1   ; OUTI
site 02CE3   ; OUTI
site 02CE5   ; OUTI
site 02CE7   ; OUTI
site 02CE9   ; OUTI
site 02CEB   ; OUTI
site 02CED   ; OUTI
site 02CEF   ; OUTI
site 02CF1   ; OUTI
site 02CF3   ; OUTI
site 02CF5   ; OUTI
site 02CF7   ; OUTI
site 02CF9   ; OUTI
site 02CFB   ; OUTI
site 02CFD   ; OUTI
site 02CFF   ; OUTI
site 02D01   ; OUTI
site 02D03   ; OUTI
site 02D05   ; OUTI
site 02D07   ; OUTI
site 02D09   ; OUTI
site 02D0B   ; OUTI
site 02D29   ; OUTI
site 02D2B   ; OUTI
site 02D2D   ; OUTI
site 02D2F   ; OUTI
site 02D31   ; OUTI
site 02D33   ; OUTI
site 02D35   ; OUTI
site 02D37   ; OUTI
site 02D39   ; OUTI
site 02D3B   ; OUTI
site 02D3D   ; OUTI
site 02D3F   ; OUTI
site 02D41   ; OUTI
site 02D43   ; OUTI
site 02D45   ; OUTI
site 02D47   ; OUTI
site 02D49   ; OUTI
site 02D4B   ; OUTI
site 02D4D   ; OUTI
site 02D4F   ; OUTI
site 02D51   ; OUTI
site 02D53   ; OUTI
site 02D55   ; OUTI
site 02D57   ; OUTI
site 02D59   ; OUTI
site 02D5B   ; OUTI
site 02D5D   ; OUTI
site 02D5F   ; OUTI
site 02D61   ; OUTI
site 02D63   ; OUTI
site 02D65   ; OUTI
site 02D67   ; OUTI
site 02D69   ; OUTI
site 02D6B   ; OUTI
site 02D6D   ; OUTI
site 02D6F   ; OUTI
site 02D71   ; OUTI
site 02D73   ; OUTI
site 02D75   ; OUTI
site 02D77   ; OUTI
site 02D79   ; OUTI
site 02D7B   ; OUTI
site 02D7D   ; OUTI
site 02D7F   ; OUTI
site 02D81   ; OUTI
site 02D83   ; OUTI
site 02D85   ; OUTI
site 02D87   ; OUTI
site 02D89   ; OUTI
site 02D8B   ; OUTI
site 02D8D   ; OUTI
site 02D8F   ; OUTI
site 02D91   ; OUTI
site 02D93   ; OUTI
site 02D95   ; OUTI
site 02D97   ; OUTI
site 02D99   ; OUTI
site 02D9B   ; OUTI
site 02D9D   ; OUTI
site 02D9F   ; OUTI
site 02DA1   ; OUTI
site 02DA3   ; OUTI
site 02DA5   ; OUTI
site 02DA7   ; OUTI
site 02DA9   ; OUTI
site 02DAB   ; OUTI
site 02DAD   ; OUTI
site 02DAF   ; OUTI
site 02DB1   ; OUTI
site 02DB3   ; OUTI
site 02DB5   ; OUTI
site 02DB7   ; OUTI
site 02DB9   ; OUTI
site 02DBB   ; OUTI
site 02DBD   ; OUTI
site 02DBF   ; OUTI
site 02DC1   ; OUTI
site 02DC3   ; OUTI
site 02DC5   ; OUTI
site 02DC7   ; OUTI
site 02DC9   ; OUTI
site 02DCB   ; OUTI
site 02DCD   ; OUTI
site 02DCF   ; OUTI
site 02DD1   ; OUTI
site 02DD3   ; OUTI
site 02DD5   ; OUTI
site 02DD7   ; OUTI
site 02DD9   ; OUTI
site 02DDB   ; OUTI
site 02DDD   ; OUTI
site 02DDF   ; OUTI
site 02DE1   ; OUTI
site 02DE3   ; OUTI
site 02DE5   ; OUTI
site 02DE7   ; OUTI
site 02DE9   ; OUTI
site 02DEB   ; OUTI
site 02DED   ; OUTI
site 02DEF   ; OUTI
site 02DF1   ; OUTI
site 02DF3   ; OUTI
site 02DF5   ; OUTI
site 02DF7   ; OUTI
site 02DF9   ; OUTI
site 02DFB   ; OUTI
site 02DFD   ; OUTI
site 02DFF   ; OUTI
site 02E01   ; OUTI
site 02E03   ; OUTI
site 02E05   ; OUTI
site 02E07   ; OUTI
site 02E09   ; OUTI
site 02E0B   ; OUTI
site 02E0D   ; OUTI
site 02E0F   ; OUTI
site 02E11   ; OUTI
site 02E13   ; OUTI
site 02E15   ; OUTI
site 02E17   ; OUTI
site 02E19   ; OUTI
site 02E1B   ; OUTI
site 02E1D   ; OUTI
site 02E1F   ; OUTI
site 02E21   ; OUTI
site 02E23   ; OUTI
site 02E25   ; OUTI
site 02E27   ; OUTI
site 02E3D   ; OUT (C),L
site 02E42   ; OUT ($BF),A
site 02E6B   ; OUTI
site 02E7D   ; OUTD
site 02EA1   ; OUT ($BE),A
site 02EA6   ; OUT ($BE),A
site 02EAB   ; OUT ($BE),A
site 02EB0   ; OUT ($BE),A
site 02EB5   ; OUT ($BE),A
site 02EBA   ; OUT ($BE),A
site 02EBF   ; OUT ($BE),A
site 02EC4   ; OUT ($BE),A
site 02EC9   ; OUT ($BE),A
site 02ECE   ; OUT ($BE),A
site 02ED3   ; OUT ($BE),A
site 02ED8   ; OUT ($BE),A
site 02EDD   ; OUT ($BE),A
site 02EE2   ; OUT ($BE),A
site 02EE7   ; OUT ($BE),A
site 02EEC   ; OUT ($BE),A
site 02EF1   ; OUT ($BE),A
site 02EF6   ; OUT ($BE),A
site 02EFB   ; OUT ($BE),A
site 02F00   ; OUT ($BE),A
site 02F05   ; OUT ($BE),A
site 02F0A   ; OUT ($BE),A
site 02F0F   ; OUT ($BE),A
site 02F14   ; OUT ($BE),A
site 02F19   ; OUT ($BE),A
site 02F1E   ; OUT ($BE),A
site 02F23   ; OUT ($BE),A
site 02F28   ; OUT ($BE),A
site 02F2D   ; OUT ($BE),A
site 02F32   ; OUT ($BE),A
site 02F37   ; OUT ($BE),A
site 02F3C   ; OUT ($BE),A
site 02F41   ; OUT ($BE),A
site 02F46   ; OUT ($BE),A
site 02F4B   ; OUT ($BE),A
site 02F50   ; OUT ($BE),A
site 02F55   ; OUT ($BE),A
site 02F5A   ; OUT ($BE),A
site 02F5F   ; OUT ($BE),A
site 02F64   ; OUT ($BE),A
site 02F69   ; OUT ($BE),A
site 02F6E   ; OUT ($BE),A
site 02F73   ; OUT ($BE),A
site 02F78   ; OUT ($BE),A
site 02F7D   ; OUT ($BE),A
site 02F82   ; OUT ($BE),A
site 02F87   ; OUT ($BE),A
site 02F8C   ; OUT ($BE),A
site 02F91   ; OUT ($BE),A
site 02F96   ; OUT ($BE),A
site 02F9B   ; OUT ($BE),A
site 02FA0   ; OUT ($BE),A
site 02FA5   ; OUT ($BE),A
site 02FAA   ; OUT ($BE),A
site 02FAF   ; OUT ($BE),A
site 02FB4   ; OUT ($BE),A
site 02FB9   ; OUT ($BE),A
site 02FBE   ; OUT ($BE),A
site 02FC3   ; OUT ($BE),A
site 02FC8   ; OUT ($BE),A
site 02FCD   ; OUT ($BE),A
site 02FD2   ; OUT ($BE),A
site 02FD7   ; OUT ($BE),A
site 02FDC   ; OUT ($BE),A
site 02FEF   ; OUT ($BE),A
site 02FF4   ; OUT ($BE),A
site 02FF9   ; OUT ($BE),A
site 02FFE   ; OUT ($BE),A
site 03003   ; OUT ($BE),A
site 03008   ; OUT ($BE),A
site 0300D   ; OUT ($BE),A
site 03012   ; OUT ($BE),A
site 03017   ; OUT ($BE),A
site 0301C   ; OUT ($BE),A
site 03021   ; OUT ($BE),A
site 03026   ; OUT ($BE),A
site 0302B   ; OUT ($BE),A
site 03030   ; OUT ($BE),A
site 03035   ; OUT ($BE),A
site 0303A   ; OUT ($BE),A
site 0303F   ; OUT ($BE),A
site 03044   ; OUT ($BE),A
site 03049   ; OUT ($BE),A
site 0304E   ; OUT ($BE),A
site 03053   ; OUT ($BE),A
site 03058   ; OUT ($BE),A
site 0305D   ; OUT ($BE),A
site 03062   ; OUT ($BE),A
site 03067   ; OUT ($BE),A
site 0306C   ; OUT ($BE),A
site 03071   ; OUT ($BE),A
site 03076   ; OUT ($BE),A
site 0307B   ; OUT ($BE),A
site 03080   ; OUT ($BE),A
site 03085   ; OUT ($BE),A
site 0308A   ; OUT ($BE),A
site 0308F   ; OUT ($BE),A
site 03094   ; OUT ($BE),A
site 03099   ; OUT ($BE),A
site 0309E   ; OUT ($BE),A
site 030A3   ; OUT ($BE),A
site 030A8   ; OUT ($BE),A
site 030AD   ; OUT ($BE),A
site 030B2   ; OUT ($BE),A
site 030B7   ; OUT ($BE),A
site 030BC   ; OUT ($BE),A
site 030C1   ; OUT ($BE),A
site 030C6   ; OUT ($BE),A
site 030CB   ; OUT ($BE),A
site 030D0   ; OUT ($BE),A
site 030D5   ; OUT ($BE),A
site 030DA   ; OUT ($BE),A
site 030DF   ; OUT ($BE),A
site 030E4   ; OUT ($BE),A
site 030E9   ; OUT ($BE),A
site 030EE   ; OUT ($BE),A
site 030F3   ; OUT ($BE),A
site 030F8   ; OUT ($BE),A
site 030FD   ; OUT ($BE),A
site 03102   ; OUT ($BE),A
site 03107   ; OUT ($BE),A
site 0310C   ; OUT ($BE),A
site 03111   ; OUT ($BE),A
site 03116   ; OUT ($BE),A
site 0311B   ; OUT ($BE),A
site 03120   ; OUT ($BE),A
site 03125   ; OUT ($BE),A
site 0312A   ; OUT ($BE),A
site 03252   ; OUT ($BE),A
site 03259   ; OUT ($BE),A
site 03260   ; OUT ($BE),A
site 03267   ; OUT ($BE),A
site 032A6   ; IN A,($BE)
site 032AE   ; IN A,($BE)
site 032B6   ; IN A,($BE)
site 032BE   ; IN A,($BE)
site 0330B   ; OUT ($BE),A
site 03313   ; OUT ($BE),A
site 0331B   ; OUT ($BE),A
site 03323   ; OUT ($BE),A
site 0339D   ; IN A,($BE)
site 033A6   ; IN A,($BE)
site 033AF   ; IN A,($BE)
site 033B8   ; IN A,($BE)
site 033C5   ; IN A,($BE)
site 033D0   ; IN A,($BE)
site 033DB   ; IN A,($BE)
site 033E6   ; IN A,($BE)
site 03403   ; OUT ($BE),A
site 0340B   ; OUT ($BE),A
site 03413   ; OUT ($BE),A
site 0341B   ; OUT ($BE),A
site 03468   ; IN A,($BE)
site 03471   ; IN A,($BE)
site 0347A   ; IN A,($BE)
site 03483   ; IN A,($BE)
site 03490   ; IN A,($BE)
site 0349B   ; IN A,($BE)
site 034A6   ; IN A,($BE)
site 034B1   ; IN A,($BE)
site 034CE   ; OUT ($BE),A
site 034D6   ; OUT ($BE),A
site 034DE   ; OUT ($BE),A
site 034E6   ; OUT ($BE),A
site 05152   ; OUT ($BE),A
site 0515C   ; OUT ($BE),A
site 0516F   ; OUT ($BE),A
site 05177   ; OUT ($BE),A
site 05185   ; OUT ($BE),A
site 0518F   ; OUT ($BE),A
site 0519A   ; OUT ($BE),A
site 051A4   ; OUT ($BE),A
site 051B4   ; OUT ($BE),A
site 051BE   ; OUT ($BE),A
site 051CD   ; OUT ($BE),A
site 051D7   ; OUT ($BE),A
site 051EA   ; OUT ($BE),A
site 051F2   ; OUT ($BE),A
site 051FB   ; OUT ($BE),A
site 05205   ; OUT ($BE),A
site 0726A   ; OUT ($B7),A
site 7C45F   ; OUT ($7F),A
site 7CAE3   ; OUT ($7F),A
site 7CBB0   ; OTIR
site 7CBC6   ; OUT ($7F),A
site 7CBDC   ; OUT ($7F),A
site 7CBEE   ; OUT ($7F),A
site 7E6B7   ; OUT ($BE),A
site 7E6BE   ; OUT ($BE),A
site 7E727   ; IN A,($BE)
site 7E731   ; OUT ($BE),A
site 7E807   ; OUT ($BE),A
site 7E812   ; OUT ($BE),A
site 7E873   ; OUT ($BE),A
site 7E880   ; OUT ($BE),A
site 7FCF2   ; OUT ($BE),A
site 7FCFC   ; OUT ($BE),A
mapst 00348   ; LD ($FFFF),A
mapst 0076A   ; LD ($FFFF),A
mapst 0087F   ; LD ($FFFF),A
mapst 00887   ; LD ($FFFF),A
mapst 008AA   ; LD ($FFFF),A
mapst 008B1   ; LD ($FFFF),A
mapst 008BE   ; LD ($FFFF),A
mapst 008C8   ; LD ($FFFF),A
mapst 008D2   ; LD ($FFFF),A
mapst 008D9   ; LD ($FFFF),A
mapst 008E3   ; LD ($FFFF),A
mapst 008EA   ; LD ($FFFF),A
mapst 008F4   ; LD ($FFFF),A
mapst 008FB   ; LD ($FFFF),A
mapst 00905   ; LD ($FFFF),A
mapst 0090C   ; LD ($FFFF),A
mapst 00916   ; LD ($FFFF),A
mapst 0091D   ; LD ($FFFF),A
mapst 00927   ; LD ($FFFF),A
mapst 0092E   ; LD ($FFFF),A
mapst 00938   ; LD ($FFFF),A
mapst 0093F   ; LD ($FFFF),A
mapst 00949   ; LD ($FFFF),A
mapst 00950   ; LD ($FFFF),A
mapst 0095A   ; LD ($FFFF),A
mapst 00961   ; LD ($FFFF),A
mapst 0096B   ; LD ($FFFF),A
mapst 00972   ; LD ($FFFF),A
mapst 0097C   ; LD ($FFFF),A
mapst 00984   ; LD ($FFFF),A
mapst 00994   ; LD ($FFFF),A
mapst 00A10   ; LD ($FFFF),A
mapst 00BAF   ; LD ($FFFF),A
mapst 00CBF   ; LD ($FFFF),A
mapst 00D6E   ; LD ($FFFF),A
mapst 00E16   ; LD ($FFFF),A
mapst 00EB5   ; LD ($FFFF),A
mapst 0101B   ; LD ($FFFF),A
mapst 011F9   ; LD ($FFFF),A
mapst 01237   ; LD ($FFFF),A
mapst 0127C   ; LD ($FFFF),A
mapst 012D2   ; LD ($FFFF),A
mapst 014C4   ; LD ($FFFF),A
mapst 014DB   ; LD ($FFFF),A
mapst 0156F   ; LD ($FFFF),A
mapst 015F4   ; LD ($FFFF),A
mapst 01646   ; LD ($FFFF),A
mapst 016FC   ; LD ($FFFF),A
mapst 0172A   ; LD ($FFFF),A
mapst 017C8   ; LD ($FFFF),A
mapst 01825   ; LD ($FFFF),A
mapst 0184D   ; LD ($FFFF),A
mapst 0185C   ; LD ($FFFF),A
mapst 01877   ; LD ($FFFF),A
mapst 0188B   ; LD ($FFFF),A
mapst 018A1   ; LD ($FFFF),A
mapst 018B7   ; LD ($FFFF),A
mapst 018F7   ; LD ($FFFF),A
mapst 01987   ; LD ($FFFF),A
mapst 01A95   ; LD ($FFFF),A
mapst 01C92   ; LD ($FFFF),A
mapst 01C98   ; LD ($FFFF),A
mapst 01D9A   ; LD ($FFFF),A
mapst 01DA0   ; LD ($FFFF),A
mapst 01E65   ; LD ($FFFF),A
mapst 0208A   ; LD ($FFFF),A
mapst 021E8   ; LD ($FFFF),A
mapst 024C4   ; LD ($FFFF),A
mapst 024D1   ; LD ($FFFF),A
mapst 028AE   ; LD ($FFFF),A
mapst 02972   ; LD ($FFFF),A
mapst 029B5   ; LD ($FFFF),A
mapst 029F4   ; LD ($FFFF),A
mapst 02A07   ; LD ($FFFF),A
mapst 02E52   ; LD ($FFFF),A
mapst 03146   ; LD ($FFFF),A
mapst 03154   ; LD ($FFFF),A
mapst 03354   ; LD ($FFFF),A
mapst 03508   ; LD ($FFFF),A
mapst 03532   ; LD ($FFFF),A
mapst 03563   ; LD ($FFFF),A
mapst 03628   ; LD ($FFFF),A
mapst 03644   ; LD ($FFFF),A
mapst 03728   ; LD ($FFFF),A
mapst 0373D   ; LD ($FFFF),A
mapst 0376B   ; LD ($FFFF),A
mapst 039AF   ; LD ($FFFF),A
mapst 03B96   ; LD ($FFFF),A
mapst 04446   ; LD ($FFFF),A
mapst 05282   ; LD ($FFFF),A
mapst 05897   ; LD ($FFFF),A
mapst 05F2C   ; LD ($FFFF),A
mapst 06172   ; LD ($FFFF),A
mapst 061A6   ; LD ($FFFF),A
mapst 061AF   ; LD ($FFFF),A
mapst 07934   ; LD ($FFFF),A
mapst 0795E   ; LD ($FFFF),A
mapst 07BB2   ; LD ($FFFF),A
mapst 07D62   ; LD ($FFFF),A
mapst 00894   ; LD ($FFFF),A
mapst 008A0   ; LD ($FFFF),A
mapst 019E3   ; LD ($FFFF),A
mapst 01A3F   ; LD ($FFFF),A
mapst 0233D   ; LD ($FFFF),A

# Mortal Kombat 3 (Brazil) (Action Replay).cht and Mortal Kombat 3 (Brazil).cht, "Infinite
# Credits (Continues)": RAM $D3A5 is the number of credits, spent by each continue
poke "Infinite credits"
ar 00D3-A509
endpoke

# Mortal Kombat 3 (Brazil).cht, "Infinite Health P1": the code changes a byte in the routine
# that takes health from player 1; the health bar stays full when player 1 is hit
poke "Infinite health"
gg CEA-584-D5D
endpoke

# Mortal Kombat 3 (Brazil).cht, "P1 Wins Soon As The Round Starts": two bytes in bank 0 are
# changed to $00; the opponent's bar is empty at the start of the round and player 1 wins it
poke "Win round at once"
gg 006-11C-19A
gg 006-12C-19A
endpoke
