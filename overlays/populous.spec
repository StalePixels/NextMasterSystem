# Populous (Europe, Brazil) (En), CRC32 C7A1FDEF, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with hand entry points and a reference
# I/O log of 900 s (random input), then decided by hand.
#
# Decisions:
# - The frame handler at $0038 calls $D228, a JP to $045A that the game writes at $008A-$0094
#   (and at $4719 to $46ED). Both are scanned as handler entries.
# - Indirect jumps resolved by hand (sitescan --entry):
#   - $1AA3, sound effect table $1A84 indexed by $D5A6 (2, 4, 6, 8 or 10): $1AA4, $1AE5,
#     $1B51, $1B82, $1B1B.
#   - $3C3E, table $7978 (A below $0D): adds $3BBD to the six targets the scanner proved.
#   - $21C0, table $7495 indexed by $D565: $2381, $22C6, $2467, $2676, $27D5 ($21C1 is
#     index 0; the table ends at the word $0064).
#   - $242C, icon table $7589 indexed by row $D55C (0-5) and column $D55D (0-7): $2635,
#     $279E, $28ED, $4056, $4017, $296A, $2971, $4333, $242E, $421E, $42AC, $25BA. The
#     other cells hold $242D (a RET) and $006B (the NMI pause toggle).
#   - $B93B and $B9A1 (bank 9, sound driver), through $D232 and $D23A: the music data
#     names the instrument routines as 01 lo hi: $B9FB, $BA37, $BA64. The returns pushed
#     before them, $B93C and $B9A2, are entries too.
#   - $6F1F (RET after LD SP,($D572)) returns to the routine's caller: $6CFE saves SP in
#     $D572 before the routine uses the stack to fill RAM.
# - Timing: the game times its intro, palette fades and sound effects with CPU delay loops, and
#   page 0 keeps their Master System time (below). Its play step is bound by the view renderer
#   $6A88; page 1 runs it at full speed and holds the step to the Master System's time (below).
# - Not code, not patched: $3AB5 (a table of $DA-$DD bytes) and $1D367 (bank 7, data).
# - Unused (no call, jump, address load or table entry names them, and the reference log
#   did not run them): the button wait at $044D-$0458 and the debug number printer at
#   $4551-$459E.
name Populous
cart C7A1FDEF
hz 50		; No-Intro regions Europe, Brazil
# $0020-$0037 are filler bytes; the game uses only RST $08 and RST $38.
vector 20 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
# Delay loops. The game times its logo, title, story pages, palette fades and sound effects
# with CPU loops, which run about 8 times faster on the Next. Page 0 waits for each loop's
# Master System time instead, counted in Next video lines (228 T-states a line at 50 Hz).
# The page uses the game's stack (the far call and at most two calls more) and leaves
# interrupts as the game had them: the game's interrupt code writes only $FFFF.
# - d26: DEC BC; LD A,B; OR C; JR NZ (26 T-states a step) at $0079 (power on), $00B3 (the
#   title), $03E9 and $041B (the logo), $1AD8, $1B0E, $1B44, $1B79 and $1BAA (sound effects),
#   $215D (palette fade) and $43F8.
# - d350f: $3516-$3525, the rest of $350F, which times the story pages: BC steps of 100 (the
#   first) or 256 reads of $D20A, ending early when it is not 0.
# - d34f7: $34FE-$350E, the rest of $34F7, which holds the logo: BC steps of 100 (the first) or
#   256 joypad reads, ending early on button 1 or 2.
asm 00079 5   ; DEC BC; LD A,B; OR C; JR NZ,$0079
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 000B3 5   ; DEC BC; LD A,B; OR C; JR NZ,$00B3
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 003E9 5   ; DEC BC; LD A,B; OR C; JR NZ,$03E9
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 0041B 5   ; DEC BC; LD A,B; OR C; JR NZ,$041B
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 01AD8 5   ; DEC BC; LD A,B; OR C; JR NZ,$1AD8
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 01B0E 5   ; DEC BC; LD A,B; OR C; JR NZ,$1B0E
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 01B44 5   ; DEC BC; LD A,B; OR C; JR NZ,$1B44
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 01B79 5   ; DEC BC; LD A,B; OR C; JR NZ,$1B79
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 01BAA 5   ; DEC BC; LD A,B; OR C; JR NZ,$1BAA
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 0215D 5   ; DEC BC; LD A,B; OR C; JR NZ,$215D
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 043F8 5   ; DEC BC; LD A,B; OR C; JR NZ,$43F8
    rst $20
    db far_io, pg_d26, ent_d26
    nop
endasm
asm 03516 16  ; LD E,$64 ... JR $3517: the wait of $350F
    rst $20
    db far_io, pg_d350f, ent_d350f
    ret
    ds 11
endasm
asm 034FE 17  ; LD E,$64 ... JR $3500: the wait of $34F7
    rst $20
    db far_io, pg_d34f7, ent_d34f7
    ret
    ds 12
endasm
# The view renderer $6A88 (bank 1, called once a game step from $0190) builds each 8x8 tile of
# the landscape in software and sends it with OUT ($BE),A, 32 bytes a tile, then the name table
# cells. Through the runtime, one trap a byte, a game step took about 15.5 frames at 50 Hz against
# about 9.5 at 60 Hz on the Master System, so the game played at half speed. Page 1 entry view runs
# the same code, $6A8B-$6CFD, with each data write stored into a buffer and each address written
# to the VDP control port sending the buffer with one jt_vwrite call. The site lines of the
# replaced code stay, so that the scan's rows are covered.
asm 06A8B 5   ; LD A,($D563); LD L,A; EX AF,AF': the code after CALL $6CFE
    rst $20
    db far_io, pg_view, ent_view
    ret
endasm
page 1 view
; view: $6A8B-$6CFD as the game has it, with OUT ($BE),A as LD (IY+0),A; INC IY and
; OUT ($BF),A as CALL vctl. Reads the game's RAM, slot 1 and slot 2 directly: none of it is in
; $2000-$3FFF. Ends as the game's RET Z at $6BA3 (A = 0, Z), with the buffer sent. Keeps IY.
; Uses the game's stack: the far call, two calls more and at most six pushes.
view:   ld a,($d563)
        ld (vtiles),a
        call vt0
        ld (vsiy),iy
        ld iy,vbuf
        xor a
        ld (vlat),a
        ld a,($d563)
v6A8E:
        ld l,a
        ex af,af'
        ld h,$d2
        ld b,(hl)
        xor a
        rr b
        rra
        rr b
        rra
        rr b
        rra
        call vctl
        ld a,$40
        or b
        call vctl
        ld h,$d1
        ld a,(hl)
        dec h
        or a
        jp z,v6BD2
        ld e,a
        ld a,l
        ld d,(hl)
        ld h,$80
        exx
        ld l,a
        ld h,$ce
        ld a,(hl)
        add a,a
        jp z,v6B0B
        ld e,a
        jp nc,v6B32
        inc h
        ld l,(hl)
        ld d,$a8
        ld h,d
        ld b,$08
v6AC3:
        exx
        ld l,d
        ld b,(hl)
        ld l,e
        ld c,(hl)
        inc h
        exx
        ld a,(de)
        inc e
        or (hl)
        inc l
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        or (hl)
        inc h
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        dec e
        or (hl)
        dec l
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        or (hl)
        inc h
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        djnz v6AC3
        jp v6B96
v6B0B:
        inc h
        ld l,(hl)
        ld h,$66
        ld d,$08
v6B11:
        ld h,$66
        exx
        ld l,d
        ld b,(hl)
        ld l,e
        ld c,(hl)
        inc h
        exx
        ld b,$04
v6B1C:
        ld a,(hl)
        inc h
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        djnz v6B1C
        inc l
        dec d
        jp nz,v6B11
        jp v6B96
v6B32:
        inc h
        ld l,(hl)
        ex de,hl
        ld b,l
        srl l
        ld h,$74
        ld c,(hl)
        ld l,b
        ld b,$62
        push bc
        pop ix
        ld h,$a8
        ld b,$08
v6B45:
        ld d,$66
        ld c,(ix+$00)
        inc ix
        exx
        ld l,d
        ld b,(hl)
        ld l,e
        ld c,(hl)
        inc h
        exx
        ld a,(de)
        inc d
        and c
        or (hl)
        inc l
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        and c
        or (hl)
        inc h
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        and c
        or (hl)
        dec l
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        and c
        or (hl)
        inc h
        exx
        and c
        ld l,e
        or (hl)
        and b
        ld l,d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        inc e
        djnz v6B45
v6B96:
        ex af,af'
v6B97:
        dec a
        jp nz,v6A8E
        ld de,$d404
        ld hl,$7630
v6BA1:
        ld a,(hl)
        or a
        jp z,vfin
        ld b,a
        inc l
        ld a,(hl)
        inc l
        call vctl
        push hl
        ld h,(hl)
        ld l,a
        ld a,h
        add a,$20
        call vctl
v6BB2:
        ld a,(de)
        or a
        jp z,v6BCB
        ld c,d
        ld a,d
        add a,$9c
        ld d,a
        ld a,(de)
        ld (iy+0),a
        inc iy
        ld d,c
        xor a
        inc l
v6BC1:
        inc hl
        ld (iy+0),a
        inc iy
        inc de
        djnz v6BB2
        pop hl
        inc l
        jp v6BA1
v6BCB:
        ld a,(hl)
        ld (iy+0),a
        inc iy
        inc l
        ld a,(hl)
        jp v6BC1
v6BD2:
        ld a,(hl)
        or a
        jp z,v6C96
        ld e,a
        ld d,$80
        ld a,l
        ex de,hl
        exx
        ld l,a
        ld h,$ce
        ld a,(hl)
        add a,a
        jp z,v6C23
        ld e,a
        jp nc,v6C43
        inc h
        ld l,(hl)
        ld d,$a8
        ld h,d
        ld b,$08
v6BEE:
        exx
        ld b,(hl)
        inc h
        exx
        ld a,(de)
        inc e
        or (hl)
        inc l
        exx
        and b
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        or (hl)
        inc h
        exx
        and b
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        dec e
        or (hl)
        dec l
        exx
        and b
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        or (hl)
        inc h
        exx
        and b
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        djnz v6BEE
        jp v6B96
v6C23:
        inc h
        ld a,(hl)
        exx
        ld e,a
        ld a,$08
v6C29:
        ex af,af'
        ld c,(hl)
        inc h
        ld b,$04
        ld d,$66
v6C30:
        ld a,(de)
        inc d
        and c
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        djnz v6C30
        inc e
        ex af,af'
        dec a
        jp nz,v6C29
        exx
        ld a,l
        jp v6B97
v6C43:
        inc h
        ld l,(hl)
        ex de,hl
        ld b,l
        srl l
        ld h,$74
        ld c,(hl)
        ld l,b
        ld b,$62
        push bc
        exx
        pop de
        exx
        ld h,$a8
        ld b,$08
v6C57:
        ld d,$66
        exx
        ld c,(hl)
        inc h
        ld a,(de)
        inc e
        exx
        ld c,a
        ld a,(de)
        inc d
        and c
        or (hl)
        inc l
        exx
        and c
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        and c
        or (hl)
        inc h
        exx
        and c
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        and c
        or (hl)
        dec l
        exx
        and c
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        ld a,(de)
        inc d
        and c
        or (hl)
        inc h
        exx
        and c
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        exx
        inc e
        djnz v6C57
        jp v6B96
v6C96:
        ld h,$ce
        ld a,(hl)
        add a,a
        ld e,a
        jp nc,v6CC1
        inc h
        ld l,(hl)
        ld d,$a8
        ld h,d
        ld b,$08
v6CA4:
        ld a,(de)
        inc e
        or (hl)
        inc l
        ld (iy+0),a
        inc iy
        ld a,(de)
        inc d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        ld a,(de)
        dec e
        or (hl)
        dec l
        ld (iy+0),a
        inc iy
        ld a,(de)
        inc d
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        djnz v6CA4
        jp v6B96
v6CC1:
        inc h
        ld l,(hl)
        ex de,hl
        ld b,l
        srl l
        ld h,$74
        ld c,(hl)
        ld l,b
        ld b,$62
        push bc
        exx
        pop de
        exx
        ld h,$a8
        ld b,$08
v6CD5:
        ld d,$66
        exx
        ld a,(de)
        inc e
        exx
        ld c,a
        ld a,(de)
        inc d
        and c
        or (hl)
        inc l
        ld (iy+0),a
        inc iy
        ld a,(de)
        inc d
        and c
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        ld a,(de)
        inc d
        and c
        or (hl)
        dec l
        ld (iy+0),a
        inc iy
        ld a,(de)
        inc d
        and c
        or (hl)
        inc h
        ld (iy+0),a
        inc iy
        inc e
        djnz v6CD5
        jp v6B96

vfin:   call vflush
        push af
        push bc
        push de
        push hl
        call vhold
        pop hl
        pop de
        pop bc
        pop af
        ld iy,(vsiy)
        ret

; vctl: a write of A to the VDP control port. The first byte is kept; the second, with code 1
; (a VRAM write), sends the buffer to the address before it and sets the new address. Any other
; code sends the buffer, then both bytes through the runtime. Keeps every register and flag.
vctl:   push af
        push hl
        ld hl,vlat
        inc (hl)
        bit 0,(hl)
        jr z,1F
        pop hl
        pop af
        ld (valo),a
        ret
1:      ld (hl),0
        pop hl
        pop af
        push af
        ld (vahi),a
        and $c0
        cp $40
        jr nz,2F
        call vflush
        ld a,(valo)
        ld (vadr),a
        ld a,(vahi)
        ld (vadr+1),a
        pop af
        ret
2:      call vflush
        ld a,(valo)
        rst $20                 ; OUT ($BF),A
        db $05
        ld a,(vahi)
        rst $20
        db $05
        pop af
        ret

; vflush: sends the buffer (vbuf up to IY) to the VRAM address (vadr), 256 bytes a call, and
; moves (vadr) past it; IY back to vbuf. Keeps every other register and the flags.
vflush: push af
        push bc
        push de
        push hl
        push ix
        push iy
        pop hl
        ld de,vbuf
        or a
        sbc hl,de
        ld (vlen),hl
        ld (vsrc),de
3:      ld hl,(vlen)
        ld a,h
        or l
        jr z,5F
        ld bc,256
        ld a,h
        or a
        jr nz,4F
        ld b,0
        ld c,l
4:      or a
        sbc hl,bc
        ld (vlen),hl
        push bc
        pop ix
        push bc
        pop iy
        ld b,c                  ; bytes in the run (0: 256)
        ld c,1
        ld hl,(vsrc)
        ld de,(vadr)
        ld a,1                  ; the source as mapped now: the buffer in this page
        call jt_vwrite
        push ix
        pop bc
        add hl,bc
        ld (vsrc),hl
        ex de,hl
        add hl,bc
        ld (vadr),hl
        jr 3B
5:      call vtick
        ld iy,vbuf
        pop ix
        pop hl
        pop de
        pop bc
        pop af
        ret

; vhold: holds the game step to the Master System's time. In the reference (sg1000m3, 60 Hz)
; a step took 8.2 frames with 155 tiles in $D563, 9.4 with 176 and 9.6 with 189: about
; 1.87 + 0.041 x tiles frames, which is 487 + 10.7 x tiles Next lines (64 us each). On the Next
; the rest of the step, from the return of view to the next call, takes about 110 lines, and
; the game runs it with interrupts off. So view itself lasts 377 + 10.7 x tiles lines, counted
; on the Next's video line from the start of view: vtick adds the lines since its last call,
; and is called at each tile's flush and in the wait, less than a frame apart. The wait reads the
; V counter through the runtime, so that the frame work goes on. Changes A, BC, DE, HL.
vhold:  ld a,(vtiles)           ; lines to hold: 377 + 10 x tiles + 11/16 x tiles
        ld l,a
        ld h,0
        ld d,h
        ld e,l
        add hl,hl
        add hl,hl
        add hl,de
        add hl,hl               ; 10 x tiles
        push hl
        ld h,0
        ld l,e
        add hl,hl
        add hl,hl
        add hl,de
        add hl,hl
        add hl,de               ; 11 x tiles
        ld b,4
1:      srl h
        rr l
        djnz 1B
        pop de
        add hl,de
        ld de,377
        add hl,de
        ex de,hl                ; DE = lines to hold
2:      push de
        call vtick
        pop de
        ld hl,(vel)
        or a
        sbc hl,de
        ret nc
        rst $20                 ; IN A,($7E)
        db $0A
        jr 2B

; vt0: the start of view: the line now, no lines counted. Changes A, BC, HL.
vt0:    call vline
        ld (vlp),hl
        ld hl,0
        ld (vel),hl
        ret

; vtick: (vel) += the lines since the last call (the video line's 311 lines a frame at 50 Hz).
; Changes A, BC, DE, HL.
vtick:  call vline
        ld de,(vlp)
        ld (vlp),hl
        or a
        sbc hl,de
        jr nc,1F
        ld de,311
        add hl,de
1:      ld de,(vel)
        add hl,de
        ld (vel),hl
        ret

; vline: HL = the Next's video line. Changes A, BC. Keeps the interrupt state: LD A,I is read
; twice, because an interrupt taken during LD A,I leaves P/V clear.
vline:  ld a,i
        jp pe,1F
        ld a,i
1:      push af
        di
2:      ld bc,$243B
        ld a,$1E
        out (c),a
        inc b
        in h,(c)
        dec b
        ld a,$1F
        out (c),a
        inc b
        in l,(c)
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        cp h
        jr nz,2B
        ld a,h
        and 1
        ld h,a
        pop af
        ret po
        ei
        ret

vtiles: db 0
vlp:    dw 0
vel:    dw 0
vsiy:   dw 0
vlat:   db 0
valo:   db 0
vahi:   db 0
vadr:   dw 0
vlen:   dw 0
vsrc:   dw 0
vbuf    equ $3000               ; up to $3FFF
endpage
page 0 d26 d350f d34f7
; d26: BC steps of 26 T-states (BC = 0: 65536), the last JR 5 fewer. Returns BC = 0, A = 0 and
; the flags of XOR A (Z, as OR C leaves them). Keeps DE, HL.
d26:    ld (sv_de),de
        ld (sv_hl),hl
        call tstart
        ld a,26
1:      ld (sv_a),a
        call addbc
        ld a,(sv_a)
        dec a
        jr nz,1B
        xor a
        ld (pmode),a
        call wait
        ld de,(sv_de)
        ld hl,(sv_hl)
        ld bc,0
        xor a
        ret

; d350f: the wait at $3516: the first BC step 3,826 T-states, the others 9,758 (E runs from 0,
; 256 reads, because the loop goes back to $3517 and not to LD E,$64). Ends with A = ($D20A)
; and NZ as soon as it is not 0; else with BC = 0, A = 0 and Z. Keeps DE, HL (the routine
; leaves E = 0, which no caller reads).
d350f:  ld a,1
        jr pwait
; d34f7: the wait at $34FE: the first BC step 4,326 T-states, the others 11,034. Ends with
; A = (NOT joypad) AND $30 and NZ as soon as button 1 or 2 is down; else as d350f.
d34f7:  ld a,2
pwait:  ld (pmode),a
        ld (sv_de),de
        ld (sv_hl),hl
        ld (cnt),bc
        call tstart
        ld bc,3826
        ld a,(pmode)
        cp 1
        jr z,1F
        ld bc,4326
1:      call addbc
2:      call wait
        jr nz,4F
        ld bc,(cnt)
        dec bc
        ld (cnt),bc
        ld a,b
        or c
        jr z,3F
        ld bc,9758
        ld a,(pmode)
        cp 1
        jr z,1F
        ld bc,11034
1:      call addbc
        jr 2B
3:      ld de,(sv_de)
        ld hl,(sv_hl)
        xor a                   ; BC = 0, A = 0, Z
        ret
4:      ld de,(sv_de)
        ld hl,(sv_hl)
        ld bc,(cnt)
        or a                    ; A = the value read, NZ
        ret

; tstart: the line now is where the wait starts; nothing owed.
tstart: call rdline
        ld (lprev),hl
        ld hl,0
        ld (owed),hl
        ld (tfrac),hl
        ret

; addbc: BC T-states (0: 65536) more to wait, kept as whole lines in (owed) and the rest in
; (tfrac). Changes A, BC, DE, HL.
addbc:  ld a,b
        or c
        jr nz,1F
        ld de,287               ; 65536 = 287 x 228 + 100
        ld a,100
        jr 2F
1:      ld h,b
        ld l,c
        ld c,228
        xor a                   ; HL / 228: HL quotient, A remainder
        ld b,16
3:      add hl,hl
        rla
        jr c,4F
        cp c
        jr c,5F
4:      sub c
        inc l
5:      djnz 3B
        ex de,hl
2:      ld hl,(tfrac)
        ld b,0
        ld c,a
        add hl,bc
        ld bc,228
        or a
        sbc hl,bc
        jr nc,6F
        add hl,bc
        jr 7F
6:      inc de
7:      ld (tfrac),hl
        ld hl,(owed)
        add hl,de
        ld (owed),hl
        ret

; wait: waits until (owed) lines have passed since (lprev). With (pmode) 1 it ends early with
; NZ and A = ($D20A) when that is not 0; with 2, with NZ and A = (NOT joypad) AND $30 when
; button 1 or 2 is down. Else it ends with Z. A V counter read through the runtime in each pass
; lets the runtime's frame work run while interrupts are off. Changes A, BC, DE, HL.
wait:   rst $20                 ; IN A,($7E)
        db $0A
        ld a,(pmode)
        or a
        jr z,2F
        dec a
        jr nz,1F
        ld a,($D20A)
        or a
        ret nz
        jr 2F
1:      rst $20                 ; IN A,($DC)
        db $0E
        cpl
        and $30
        ret nz
2:      call rdline
        ld de,(lprev)
        ld (lprev),hl
        or a
        sbc hl,de
        jr nc,3F
        ld de,311
        add hl,de
3:      ex de,hl
        ld hl,(owed)
        or a
        sbc hl,de
        jr c,4F
        jr z,4F
        ld (owed),hl
        jr wait
4:      ld hl,0
        ld (owed),hl
        xor a
        ret

; rdline: HL = the Next's video line. Changes A, BC. Keeps the interrupt state: LD A,I is read
; twice, because an interrupt taken during LD A,I leaves P/V clear.
rdline: ld a,i
        jp pe,1F
        ld a,i
1:      push af
        di
2:      ld bc,$243B
        ld a,$1E
        out (c),a
        inc b
        in h,(c)
        dec b
        ld a,$1F
        out (c),a
        inc b
        in l,(c)
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        cp h
        jr nz,2B
        ld a,h
        and 1
        ld h,a
        pop af
        ret po
        ei
        ret

pmode:  db 0
sv_a:   db 0
sv_de:  dw 0
sv_hl:  dw 0
cnt:    dw 0
lprev:  dw 0
owed:   dw 0
tfrac:  dw 0
endpage
site 0003A   ; IN A,($BF)
site 00040   ; IN A,($DD)
site 0013B   ; IN A,($DD)
site 00198   ; OUT ($7F),A
site 0019C   ; OUT ($7F),A
site 001B4   ; IN A,($DC)
site 001D8   ; OUT ($BF),A
site 001DD   ; OUT ($BF),A
site 001E0   ; OUT ($BE),A
site 001EC   ; OUT ($BE),A
site 001F5   ; OUT ($BF),A
site 001FA   ; OUT ($BF),A
site 001FF   ; OUT ($BE),A
site 00371   ; OUT ($BF),A
site 00375   ; OUT ($BF),A
site 0037E   ; OUT ($BE),A
site 00383   ; OUT ($BF),A
site 00387   ; OUT ($BF),A
site 0038D   ; OUT ($BE),A
site 0039A   ; OUT ($BF),A
site 0039E   ; OUT ($BF),A
site 003A7   ; OUT ($BE),A
site 003BE   ; OUT ($BF),A
site 003C1   ; OUT ($BF),A
site 003C6   ; OUT ($BE),A
site 003D9   ; OUT ($BF),A
site 003DD   ; OUT ($BF),A
site 0040E   ; OUT ($BF),A
site 00412   ; OUT ($BF),A
site 00446   ; OUT ($BF),A
site 0044A   ; OUT ($BF),A
site 00469   ; OUT ($7F),A
site 00471   ; OUT ($7F),A
site 00483   ; OUT ($7F),A
site 0048C   ; OUT ($7F),A
site 00493   ; OUT ($7F),A
site 0154F   ; OUT ($BF),A
site 01553   ; OUT ($BF),A
site 0155B   ; OUT ($BE),A
site 01562   ; OUT ($BF),A
site 01566   ; OUT ($BF),A
site 0156F   ; OUT ($BE),A
site 01575   ; OUT ($BE),A
site 0157B   ; OUT ($BE),A
site 01588   ; OUT ($BE),A
site 0158E   ; OUT ($BE),A
site 01595   ; OUT ($BE),A
site 0159C   ; OUT ($BE),A
site 015A3   ; OUT ($BF),A
site 015A7   ; OUT ($BF),A
site 015AD   ; OUT ($BE),A
site 015B3   ; OUT ($BE),A
site 015B9   ; OUT ($BE),A
site 015BF   ; OUT ($BE),A
site 016AA   ; OUT ($BF),A
site 016AE   ; OUT ($BF),A
site 016B5   ; OUT ($BE),A
site 016BC   ; OUT ($BE),A
site 016C3   ; OUT ($BF),A
site 016C7   ; OUT ($BF),A
site 016CF   ; OUT ($BE),A
site 016D6   ; OUT ($BE),A
site 016DD   ; OUT ($BE),A
site 016E4   ; OUT ($BE),A
site 016E9   ; OUT ($BF),A
site 016ED   ; OUT ($BF),A
site 016FF   ; OUT ($BE),A
site 01728   ; OUT ($BF),A
site 0172C   ; OUT ($BF),A
site 01748   ; OUT ($BE),A
site 01751   ; OUT ($BF),A
site 01755   ; OUT ($BF),A
site 0175B   ; OUT ($BE),A
site 01764   ; OUT ($BF),A
site 01768   ; OUT ($BF),A
site 0176C   ; OUT ($BE),A
site 01773   ; OUT ($BE),A
site 0177A   ; OUT ($BE),A
site 01781   ; OUT ($BE),A
site 01794   ; OUT ($BE),A
site 017B4   ; OUT ($BE),A
site 017BB   ; OUT ($BE),A
site 017C3   ; OUT ($BE),A
site 017CC   ; OUT ($BE),A
site 017D3   ; OUT ($BE),A
site 017E5   ; OUT ($BE),A
site 01806   ; OUT ($BE),A
site 0180D   ; OUT ($BE),A
site 0181D   ; OUT ($BE),A
site 01823   ; OUT ($BE),A
site 0182A   ; OUT ($BE),A
site 0183B   ; OUT ($BE),A
site 01846   ; OUT ($BE),A
site 0184C   ; OUT ($BE),A
site 018C1   ; OUT ($BE),A
site 018C8   ; OUT ($BE),A
site 018CE   ; OUT ($BE),A
site 018D5   ; OUT ($BE),A
site 018FE   ; OUT ($BE),A
site 01905   ; OUT ($BE),A
site 0190B   ; OUT ($BE),A
site 01911   ; OUT ($BE),A
site 0193F   ; OUT ($BE),A
site 01945   ; OUT ($BE),A
site 0194B   ; OUT ($BE),A
site 01952   ; OUT ($BE),A
site 019AF   ; OUT ($BF),A
site 019B3   ; OUT ($BF),A
site 019B9   ; OUT ($BE),A
site 019E3   ; OUT ($BF),A
site 019E7   ; OUT ($BF),A
site 01A55   ; OUT ($BE),A
site 01A5B   ; OUT ($BE),A
site 01A61   ; OUT ($BE),A
site 01A69   ; OUT ($BE),A
site 01A7D   ; OUT ($7F),A
site 01A81   ; OUT ($7F),A
site 01AA6   ; OUT ($7F),A
site 01AAC   ; OUT ($7F),A
site 01AC4   ; OUT ($7F),A
site 01AD3   ; OUT ($7F),A
site 01AE2   ; OUT ($7F),A
site 01AE9   ; OUT ($7F),A
site 01AFE   ; OUT ($7F),A
site 01B02   ; OUT ($7F),A
site 01B09   ; OUT ($7F),A
site 01B18   ; OUT ($7F),A
site 01B1F   ; OUT ($7F),A
site 01B34   ; OUT ($7F),A
site 01B38   ; OUT ($7F),A
site 01B3F   ; OUT ($7F),A
site 01B4E   ; OUT ($7F),A
site 01B53   ; OUT ($7F),A
site 01B62   ; OUT ($7F),A
site 01B69   ; OUT ($7F),A
site 01B74   ; OUT ($7F),A
site 01B84   ; OUT ($7F),A
site 01B88   ; OUT ($7F),A
site 01B8C   ; OUT ($7F),A
site 01B90   ; OUT ($7F),A
site 01BA1   ; OUT ($7F),A
site 01BA5   ; OUT ($7F),A
site 01BCF   ; OUT ($7F),A
site 01BD3   ; OUT ($7F),A
site 01BDA   ; OUT ($7F),A
site 01BDF   ; OUT ($7F),A
site 01BE4   ; OUT ($7F),A
site 01BE9   ; OUT ($7F),A
site 01C28   ; OUT ($BF),A
site 01C2C   ; OUT ($BF),A
site 01C32   ; OUT ($BE),A
site 02165   ; IN A,($7E)
site 0216C   ; OUT ($BF),A
site 02170   ; OUT ($BF),A
site 02176   ; OUT ($BE),A
site 02186   ; IN A,($DC)
site 02347   ; OUT ($BF),A
site 0234B   ; OUT ($BF),A
site 0234E   ; OUT ($BE),A
site 02355   ; OUT ($BE),A
site 0236D   ; OUT ($BF),A
site 02371   ; OUT ($BF),A
site 02375   ; OUT ($BE),A
site 0237C   ; OUT ($BE),A
site 0244E   ; OUT ($BF),A
site 02452   ; OUT ($BF),A
site 0245B   ; OUT ($BE),A
site 02582   ; OUT ($BF),A
site 02586   ; OUT ($BF),A
site 0258B   ; OUT ($BE),A
site 02592   ; OUT ($BE),A
site 02599   ; OUT ($BF),A
site 0259D   ; OUT ($BF),A
site 025A2   ; OUT ($BE),A
site 025A9   ; OUT ($BE),A
site 025B0   ; OUT ($BE),A
site 025B7   ; OUT ($BE),A
site 025E8   ; OUT ($BF),A
site 025ED   ; OUT ($BF),A
site 025F1   ; OUT ($BE),A
site 025FC   ; OUT ($BE),A
site 02603   ; OUT ($BF),A
site 02608   ; OUT ($BF),A
site 0260D   ; OUT ($BE),A
site 0265D   ; OUT ($BF),A
site 02661   ; OUT ($BF),A
site 0266A   ; OUT ($BE),A
site 02766   ; OUT ($BF),A
site 0276A   ; OUT ($BF),A
site 0276F   ; OUT ($BE),A
site 02776   ; OUT ($BE),A
site 0277D   ; OUT ($BF),A
site 02781   ; OUT ($BF),A
site 02786   ; OUT ($BE),A
site 0278D   ; OUT ($BE),A
site 02794   ; OUT ($BE),A
site 0279B   ; OUT ($BE),A
site 027BC   ; OUT ($BF),A
site 027C0   ; OUT ($BF),A
site 027C9   ; OUT ($BE),A
site 028B5   ; OUT ($BF),A
site 028B9   ; OUT ($BF),A
site 028BE   ; OUT ($BE),A
site 028C5   ; OUT ($BE),A
site 028CC   ; OUT ($BF),A
site 028D0   ; OUT ($BF),A
site 028D5   ; OUT ($BE),A
site 028DC   ; OUT ($BE),A
site 028E3   ; OUT ($BE),A
site 028EA   ; OUT ($BE),A
site 029E6   ; IN A,($DD)
site 02AF0   ; OUT ($BF),A
site 02AF4   ; OUT ($BF),A
site 02AFE   ; OUT ($BE),A
site 02F0D   ; OUT ($BE),A
site 02FA5   ; OUT ($BE),A
site 02FAD   ; OUT ($BE),A
site 02FB1   ; OUT ($BF),A
site 02FB4   ; OUT ($BF),A
site 02FB8   ; OUT ($BE),A
site 02FC1   ; OUT ($BE),A
site 03278   ; IN A,($DC)
site 03293   ; OUT ($BF),A
site 03297   ; OUT ($BF),A
site 0329B   ; OUT ($BE),A
site 033B6   ; OUT ($BE),A
site 033BD   ; OUT ($BE),A
site 033DC   ; OUT ($BE),A
site 033F6   ; OUT ($BF),A
site 033FA   ; OUT ($BF),A
site 033FD   ; OUT ($BE),A
site 0340C   ; OUT ($BE),A
site 0344E   ; OUT ($BE),A
site 03454   ; OUT ($BE),A
site 0345B   ; OUT ($BE),A
site 03461   ; OUT ($BE),A
site 03488   ; OUT ($BE),A
site 03491   ; OUT ($BE),A
site 0349C   ; OUT ($BE),A
site 034A2   ; OUT ($BE),A
site 034AB   ; OUT ($BE),A
site 034D1   ; OUT ($BE),A
site 034D8   ; OUT ($BE),A
site 034DF   ; OUT ($BE),A
site 034E5   ; OUT ($BE),A
site 034F7   ; IN A,($DC)
site 0350F   ; IN A,($DC)
site 036E1   ; OUT ($7F),A
site 036E4   ; OUT ($7F),A
site 036E8   ; OUT ($7F),A
site 036EB   ; OUT ($7F),A
site 036EF   ; OUT ($7F),A
site 036F2   ; OUT ($7F),A
site 03706   ; OUT ($7F),A
site 03709   ; OUT ($7F),A
site 0370D   ; OUT ($7F),A
site 03710   ; OUT ($7F),A
site 03714   ; OUT ($7F),A
site 03717   ; OUT ($7F),A
site 0371D   ; OUT ($7F),A
site 03720   ; OUT ($7F),A
site 03724   ; OUT ($7F),A
site 03727   ; OUT ($7F),A
site 0372B   ; OUT ($7F),A
site 0372E   ; OUT ($7F),A
site 0374D   ; OUT ($7F),A
site 03751   ; OUT ($7F),A
site 03755   ; OUT ($7F),A
site 0375B   ; IN A,($DC)
site 0376F   ; OUT ($7F),A
site 03773   ; OUT ($7F),A
site 03777   ; OUT ($7F),A
site 0377B   ; OUT ($7F),A
site 03E9C   ; OUT ($BE),A
site 03EA3   ; OUT ($BE),A
site 040E8   ; OUT ($BF),A
site 040EC   ; OUT ($BF),A
site 040F1   ; OUT ($BF),A
site 040F5   ; OUT ($BF),A
site 040FB   ; OUT ($BE),A
site 04102   ; IN A,($DD)
site 041B0   ; OUT ($BF),A
site 041B4   ; OUT ($BF),A
site 041B9   ; OUT ($BE),A
site 041C0   ; OUT ($BE),A
site 041C7   ; OUT ($BF),A
site 041CB   ; OUT ($BF),A
site 041D0   ; OUT ($BE),A
site 041D7   ; OUT ($BE),A
site 041DD   ; OUT ($BE),A
site 041E4   ; OUT ($BE),A
site 041E9   ; OUT ($BF),A
site 041ED   ; OUT ($BF),A
site 041FD   ; OUT ($BE),A
site 04204   ; OUT ($BF),A
site 04208   ; OUT ($BF),A
site 04214   ; OUT ($BE),A
site 0421B   ; OUT ($BE),A
site 04327   ; OUT ($7F),A
site 04330   ; OUT ($7F),A
site 04378   ; OUT ($BF),A
site 0437C   ; OUT ($BF),A
site 04383   ; IN A,($BE)
site 0438B   ; OUT ($7F),A
site 04398   ; OUT ($7F),A
site 0439C   ; OUT ($7F),A
site 043A5   ; OUT ($7F),A
site 043AB   ; OUT ($BF),A
site 043AF   ; OUT ($BF),A
site 043B4   ; OUT ($BF),A
site 043B8   ; OUT ($BF),A
site 043C2   ; OUT ($BE),A
site 043C8   ; OUT ($BE),A
site 0440D   ; OUT ($7F),A
site 045A7   ; OUT ($BF),A
site 045AA   ; OUT ($BF),A
site 045B0   ; OUT ($BF),A
site 045B4   ; OUT ($BF),A
site 045B9   ; OUT ($BE),A
site 04613   ; OUT ($BF),A
site 04617   ; OUT ($BF),A
site 04620   ; OUT ($BE),A
site 04639   ; OUT ($BF),A
site 0463C   ; OUT ($BF),A
site 0463F   ; OUT ($BE),A
site 04645   ; OUT ($BE),A
site 04652   ; OUT ($BF),A
site 04656   ; OUT ($BF),A
site 0465F   ; OUT ($BE),A
site 04678   ; OUT ($BF),A
site 0467B   ; OUT ($BF),A
site 0467E   ; OUT ($BE),A
site 04684   ; OUT ($BE),A
site 046B0   ; OUT ($BF),A
site 046B4   ; OUT ($BF),A
site 046B7   ; OUT ($BE),A
site 046BF   ; OUT ($BF),A
site 046C3   ; OUT ($BF),A
site 046C6   ; OUT ($BE),A
site 046D5   ; OUT ($BF),A
site 046DA   ; OUT ($BF),A
site 046DD   ; OUT ($BE),A
site 046E2   ; OUT ($BF),A
site 046E7   ; OUT ($BF),A
site 046EA   ; OUT ($BE),A
site 048E9   ; OUT ($BF),A
site 048ED   ; OUT ($BF),A
site 04909   ; OUT ($BE),A
site 04930   ; OUT ($7F),A
site 04939   ; OUT ($7F),A
site 0493D   ; OUT ($7F),A
site 04A91   ; OUT ($BF),A
site 04A94   ; OUT ($BF),A
site 04AA1   ; IN A,($BE)
site 04AA7   ; IN A,($BE)
site 04AAD   ; IN A,($BE)
site 04AB3   ; IN A,($BE)
site 04AB9   ; OUT ($BF),A
site 04ABE   ; OUT ($BF),A
site 04ACC   ; OUT ($BE),A
site 04AD4   ; OUT ($BE),A
site 04ADC   ; OUT ($BE),A
site 04AE4   ; OUT ($BE),A
site 04AED   ; OUT ($BF),A
site 04AF1   ; OUT ($BF),A
site 04AFA   ; OUT ($BE),A
site 04B00   ; OUT ($BF),A
site 04B04   ; OUT ($BF),A
site 04B0F   ; OUT ($BE),A
site 04B18   ; OUT ($BF),A
site 04B1C   ; OUT ($BF),A
site 04B25   ; OUT ($BE),A
site 04B2E   ; OUT ($BF),A
site 04B32   ; OUT ($BF),A
site 04B3B   ; OUT ($BE),A
site 04B42   ; OUT ($BF),A
site 04B46   ; OUT ($BF),A
site 04B4A   ; OUT ($BE),A
site 04B4F   ; OUT ($BF),A
site 04B53   ; OUT ($BF),A
site 04B57   ; OUT ($BE),A
site 04B5E   ; OUT ($BE),A
site 04B65   ; OUT ($BE),A
site 04B6C   ; OUT ($BE),A
site 04B73   ; OUT ($BF),A
site 04B77   ; OUT ($BF),A
site 04B7B   ; OUT ($BE),A
site 04B82   ; OUT ($BE),A
site 04B88   ; OUT ($BE),A
site 04B8E   ; OUT ($BE),A
site 04B95   ; OUT ($BF),A
site 04B99   ; OUT ($BF),A
site 04BA4   ; OUT ($BE),A
site 04BB0   ; OUT ($BF),A
site 04BB7   ; OUT ($BF),A
site 04BC2   ; OUT ($BE),A
site 04BCC   ; OUT ($BF),A
site 04BD0   ; OUT ($BF),A
site 04BDB   ; OUT ($BE),A
site 04C1E   ; OUT ($BF),A
site 04C22   ; OUT ($BF),A
site 04C2C   ; OUT ($BE),A
site 04C34   ; OUT ($BE),A
site 04C41   ; OUT ($BF),A
site 04C45   ; OUT ($BF),A
site 04C4D   ; OUT ($BE),A
site 04C56   ; OUT ($BF),A
site 04C5A   ; OUT ($BF),A
site 04C60   ; OUT ($BE),A
site 04C68   ; OUT ($BF),A
site 04C6C   ; OUT ($BF),A
site 04C77   ; OUT ($BE),A
site 04C7C   ; OUT ($BE),A
site 06A9D   ; OUT ($BF),A
site 06AA2   ; OUT ($BF),A
site 06AD6   ; OUT ($BE),A
site 06AE5   ; OUT ($BE),A
site 06AF4   ; OUT ($BE),A
site 06B03   ; OUT ($BE),A
site 06B26   ; OUT ($BE),A
site 06B60   ; OUT ($BE),A
site 06B70   ; OUT ($BE),A
site 06B80   ; OUT ($BE),A
site 06B90   ; OUT ($BE),A
site 06BA8   ; OUT ($BF),A
site 06BB0   ; OUT ($BF),A
site 06BBC   ; OUT ($BE),A
site 06BC2   ; OUT ($BE),A
site 06BCC   ; OUT ($BE),A
site 06BFA   ; OUT ($BE),A
site 06C05   ; OUT ($BE),A
site 06C10   ; OUT ($BE),A
site 06C1B   ; OUT ($BE),A
site 06C35   ; OUT ($BE),A
site 06C69   ; OUT ($BE),A
site 06C75   ; OUT ($BE),A
site 06C81   ; OUT ($BE),A
site 06C8D   ; OUT ($BE),A
site 06CA8   ; OUT ($BE),A
site 06CAE   ; OUT ($BE),A
site 06CB4   ; OUT ($BE),A
site 06CBA   ; OUT ($BE),A
site 06CE1   ; OUT ($BE),A
site 06CE8   ; OUT ($BE),A
site 06CEF   ; OUT ($BE),A
site 06CF6   ; OUT ($BE),A
site 278AF   ; OUT ($7F),A
site 279D9   ; OUT ($7F),A
site 279DE   ; OUT ($7F),A
site 279F8   ; OUT ($7F),A
site 27A03   ; OUT ($7F),A
site 27A07   ; OUT ($7F),A
site 27A16   ; OUT ($7F),A
site 27A1F   ; OUT ($7F),A
site 27A2B   ; OUT ($7F),A
site 27A34   ; OUT ($7F),A
site 27A4A   ; OUT ($7F),A
site 27A58   ; OUT ($7F),A
site 27A61   ; OUT ($7F),A
site 27A77   ; OUT ($7F),A
site 27A85   ; OUT ($7F),A
site 27A8E   ; OUT ($7F),A
mapst 0000E   ; LD ($FFFF),A
mapst 000A8   ; LD ($FFFF),A
mapst 00396   ; LD ($FFFF),A
mapst 00422   ; LD ($FFFF),A
mapst 02A1B   ; LD ($FFFF),A
mapst 02A7A   ; LD ($FFFF),A
mapst 02AE7   ; LD ($FFFF),A
mapst 02B0A   ; LD ($FFFF),A
mapst 0309E   ; LD ($FFFF),A
mapst 030B6   ; LD ($FFFF),A
mapst 03303   ; LD ($FFFF),A
mapst 033A5   ; LD ($FFFF),A
mapst 03740   ; LD ($FFFF),A
mapst 03782   ; LD ($FFFF),A
mapst 03B09   ; LD ($FFFF),A
mapst 03B2E   ; LD ($FFFF),A
mapst 03B64   ; LD ($FFFF),A
mapst 03CCF   ; LD ($FFFF),A
mapst 03E07   ; LD ($FFFF),A
mapst 046F3   ; LD ($FFFF),A
mapst 046FA   ; LD ($FFFF),A
mapst 04707   ; LD ($FFFF),A
mapst 0470E   ; LD ($FFFF),A

# Populous (Europe, Brazil).cht, "Infinite/Max Supreme Power": RAM $D566 and $D567 are the
# two bytes of the manna count; both held at $FF fill the manna gauge on the top rail
poke "Infinite manna"
ar 00D5-66FF
ar 00D5-67FF
endpoke

# Populous (Europe, Brazil).cht, "Evil Rating": RAM $D3BD is the opponent's speed; $01 makes the
# battle screen read "EVIL IS VERY FAST"
poke "Evil very fast"
ar 00D3-BD01
endpoke

# Populous (Europe, Brazil).cht, "Evil Speed": RAM $D3BE is the opponent's rating; $01 makes the
# battle screen read "EVIL RATING IS VERY HIGH"
poke "Evil rating high"
ar 00D3-BE01
endpoke
