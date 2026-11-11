# WWF Wrestlemania - Steel Cage Challenge (Europe, Brazil) (En), CRC32 2DB21448, 256K, Sega mapper.
# Pokes: codes from SMS Power, https://www.smspower.org/Cheats/WWFWrestleManiaSteelCageChallenge-SMS
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (60 s and 600 s of
# random input) and entry points for the far calls (below).
# Decisions:
# - $0008-$0394 is a development monitor that the game never runs (no RST $08 or $28 and no
#   jump into it in either log). $0010-$0012 are zero bytes there, so $0010 is the io vector.
#   The game never runs RST $00 or RST $10.
# - RST $18 ($0051) is the far call: slot 2 gets bank ($0016) OR E, with $00 at $0016.
#   $040E calls it with the bank in A. The match code in bank 1 calls bank 5 ($8309-$A516)
#   after the far call at $072C or $07E7, and $0939 jumps through the table at $092D to
#   bank 3 ($BE37, $BE99); these are given to the scanner as entry points.
# - $0038 jumps through the word at $DFEE, which the start code sets to $7833, the frame and
#   line interrupt handler in bank 1.
name WWF Wrestlemania - Steel Cage Challenge
cart 2DB21448
hz 50		; No-Intro region Europe
vector 10 io
asm 00396 2   ; IM 1 -> IM 2
    im 2
endasm
site 00047   ; IN A,($BF)
site 00049   ; IN A,($C1)
site 003A6   ; IN A,($BF)
site 00404   ; OUT ($BF),A
site 0040A   ; OUT ($BF),A
site 00434   ; IN A,($DC)
site 00907   ; OUT ($BE),A
site 0090C   ; OUT ($BE),A
site 00916   ; OUT ($BE),A
site 0096D   ; IN A,($DC)
site 00979   ; IN A,($DC)
site 00980   ; IN A,($DC)
site 01A9A   ; IN A,($BF)
site 01AC1   ; OUT ($7F),A
site 01AC5   ; OUT ($7F),A
site 01AD2   ; OUT ($7F),A
site 01AD6   ; OUT ($7F),A
site 01B07   ; OUT ($7F),A
site 01B1E   ; OUT ($7F),A
site 01B32   ; OUT ($7F),A
site 01B41   ; OUT ($7F),A
site 01B58   ; OUT ($7F),A
site 01B6C   ; OUT ($7F),A
site 01B99   ; OUT ($7F),A
site 01BAC   ; OUT ($7F),A
site 01BC3   ; OUT ($7F),A
site 01BC9   ; OUT ($7F),A
site 01BED   ; OUT ($7F),A
site 01C04   ; OUT ($7F),A
site 01C18   ; OUT ($7F),A
site 01C75   ; OUT ($7F),A
site 01E5E   ; OUT ($7F),A
site 01E63   ; OUT ($7F),A
site 01E77   ; OUT ($7F),A
site 01E8A   ; OUT ($7F),A
site 01E96   ; OUT ($7F),A
site 01EA9   ; OUT ($7F),A
site 02295   ; OUT (C),A
site 02299   ; OUT (C),A
site 0229D   ; OUT (C),D
site 022A1   ; OUT (C),A
site 022A6   ; OUT (C),D
site 022AA   ; OUT (C),A
site 022AE   ; OUT (C),A
site 022B2   ; OUT (C),D
site 022CC   ; OUT ($BE),A
site 023A9   ; OUT ($BE),A
site 023AE   ; OUT ($BE),A
site 02401   ; OUT ($BE),A
site 02417   ; OUT (C),A
site 0241C   ; OUT (C),D
site 0245A   ; IN A,($BF)
site 024D7   ; OUT ($BE),A
site 02844   ; IN A,($DC)
site 028BB   ; IN A,($DC)
site 028E0   ; IN A,($DC)
site 02959   ; OUT ($BE),A
site 02995   ; OUT ($BE),A
site 02C00   ; IN A,($DC)
site 02C16   ; IN A,($DC)
site 02C94   ; IN A,($DC)
site 02D5B   ; OUT ($BE),A
site 02D60   ; OUT ($BE),A
site 02D6D   ; OUT ($BE),A
site 02D74   ; OUT ($BE),A
site 061A7   ; IN A,($DC)
site 061BE   ; IN A,($DD)
site 06468   ; OUT (C),D
site 0646E   ; OUT (C),E
site 06474   ; OUT (C),H
site 0647A   ; OUT (C),L
site 06711   ; OUT (C),A
site 06719   ; OUT (C),A
site 06721   ; OUT (C),A
site 0672A   ; OUT (C),A
site 06749   ; OUT (C),A
site 06754   ; OUT (C),A
site 0675F   ; OUT (C),A
site 06768   ; OUT (C),A
site 067BB   ; OUT (C),A
site 067C2   ; OUT (C),A
site 067C9   ; OUT (C),A
site 067D1   ; OUT (C),A
site 067F9   ; OUT (C),A
site 06801   ; OUT (C),A
site 06809   ; OUT (C),A
site 06811   ; OUT (C),A
site 0683F   ; OUT (C),A
site 06847   ; OUT (C),A
site 0684F   ; OUT (C),A
site 06858   ; OUT (C),A
site 06877   ; OUT (C),A
site 06882   ; OUT (C),A
site 0688D   ; OUT (C),A
site 06896   ; OUT (C),A
site 07196   ; OUT ($BE),A
site 07841   ; IN A,($DD)
site 0787C   ; IN A,($BF)
site 078DB   ; OUT ($BE),A
site 078E2   ; OUT ($BE),A
site 07906   ; OUT ($BF),A
site 0790E   ; OUT ($BF),A
site 07913   ; OUT ($BF),A
site 0791B   ; OUT ($BF),A
site 0791F   ; IN A,($7E)
site 07926   ; OUT ($BF),A
site 0792A   ; OUT ($BF),A
site 07931   ; OUT ($BE),A
site 0793A   ; IN A,($BF)
site 07948   ; OUT ($BF),A
site 0794E   ; OUT ($BF),A
site 07962   ; OUT ($BF),A
site 07969   ; OUT ($BF),A
site 0BEDC   ; OUT ($BE),A
site 0BEE1   ; OUT ($BE),A
site 0FF54   ; OUT (C),A
site 0FF59   ; OUT (C),D
site 0FFC4   ; OUT (C),A
site 0FFC9   ; OUT (C),D
site 0FFD3   ; OUT (C),A
site 0FFD7   ; OUT (C),E
site 0FFDD   ; OUT (C),A
site 0FFE3   ; OUT (C),A
mapst 00056   ; LD ($FFFF),A
mapst 00398   ; LD ($FFFC),A
mapst 0039B   ; LD ($FFFD),A
mapst 0039F   ; LD ($FFFE),A
mapst 003A3   ; LD ($FFFF),A

# The fighter tile writer, bank 1: one tile of B rows (B is 8), 3 bytes a row (planes 0-2),
# from HL in slot 2, called from $2F54-$2F67 and $30A1-$30B4 with C = $BE and the VDP
# address set from $C1E0. Four forms: $66D5 flips top to bottom (it copies the tile into
# $C1FD-$C214 with the rows reversed, then writes from there), $6798 flips left to right
# through the bit-reverse table at $0500, $6776 does both, $6825 neither. Plane 3 is 0, or
# with $C1EE = 2 or 5 plane 0 OR plane 1 OR plane 2; in the left-to-right forms it is then the
# flipped plane 2 (the game's own code). Each row is 4 data writes with interrupts off; when
# the frame handler has run ($C1FC set) the row first sets the VDP address again from DE.
# Through the runtime's traps a row took about 6,600 Next cycles, and a match step on the
# Next took 5 to 6 frames where the reference takes 4 to 5. Page 0 does the same writes with
# one jt_vwrite.
asm 066D5 7          ; PUSH AF : PUSH BC : PUSH DE : PUSH HL : LD DE,$C212
    rst $10
    db far_io, pg_tl_v, ent_tl_v
    ret
endasm
asm 06776 7          ; PUSH AF : PUSH BC : PUSH DE : PUSH HL : LD DE,$C212
    rst $10
    db far_io, pg_tl_vh, ent_tl_vh
    ret
endasm
asm 06798 6          ; PUSH DE : EXX : POP DE : EXX : LD D,$05
    rst $10
    db far_io, pg_tl_h, ent_tl_h
    ret
endasm
asm 06825 5          ; LD A,($C1EE) : CP $02
    rst $10
    db far_io, pg_tl_p, ent_tl_p
    ret
endasm

page 0 tl_v tl_vh tl_h tl_p
; tl_v, tl_vh, tl_h, tl_p: as the game's $66D5, $6776, $6798 and $6825. In: B rows, C $BE,
; DE the VRAM address of the tile ($C1E0), HL the tile, interrupts on. Out as the game's code
; leaves them: HL past the rows read ($C215 in the top-to-bottom forms), DE and $C1E0 the
; address after the tile (DE' too in the left-to-right forms), B 0, C $BE, A and A' as the
; last row leaves them, $C1FC 0 when it was set, IX and IY kept, interrupts on.
; Runtime internals used: jt_vwrite, vdp_addr.
tl_v:   ld a,1
        jr go
tl_vh:  ld a,3
        jr go
tl_h:   ld a,2
        jr go
tl_p:   xor a
go:     di
        ld (g_sp),sp
        ld sp,stk_top
        push ix
        push iy
        ld (fl),a
        ld (de_in),de
        ld a,b
        ld (rows),a
        ld a,(fl)
        rra
        jr nc,.nov
        ld de,$C212             ; top to bottom: the rows reversed into $C1FD-$C214
        ld b,8
.cp:    ld a,(hl)
        inc hl
        ld (de),a
        inc de
        ld a,(hl)
        inc hl
        ld (de),a
        inc de
        ld a,(hl)
        inc hl
        ld (de),a
        dec de
        dec de
        dec de
        dec de
        dec de
        djnz .cp
        ld hl,$C1FD
.nov:   ld a,($C1EE)
        cp 2
        jr z,.or
        cp 5
        jr z,.or
        xor a
        jr .m
.or:    ld a,4
.m:     ld (orm),a
        ld ix,tbuf
        ld a,(rows)
        ld b,a
.rw:    ld a,(hl)
        call hf
        ld (ix+0),a
        ld c,a
        inc hl
        ld a,(hl)
        call hf
        ld (ix+1),a
        ld d,a
        inc hl
        ld a,(hl)
        call hf
        ld (ix+2),a
        ld e,a
        inc hl
        ld a,(orm)
        or a
        jr z,.z3                ; plane 3 is 0, A 0
        ld a,(fl)
        and 2
        ld a,e
        jr nz,.hq               ; left to right: A and A' the flipped plane 2
        ld (a2),a               ; plain: A' plane 2, A the OR
        ld a,c
        or d
        or e
        jr .p3
.hq:    ld (a2),a
        jr .p3
.z3:    xor a
.p3:    ld (ix+3),a
        ld (a1),a
        ld de,4
        add ix,de
        djnz .rw
        push hl
        ld hl,$C1FC             ; the frame handler ran: the game sets the address from DE
        ld a,(hl)
        or a
        ld de,(vdp_addr)
        jr z,.ad
        ld (hl),0
        ld de,(de_in)
.ad:    ld a,(rows)
        add a,a
        add a,a
        ld b,a
        ld c,1
        ld hl,tbuf
        ld ix,32
        ld iy,32
        ld a,1                  ; the source as mapped now: this page
        call jt_vwrite
        ld a,(rows)             ; DE and $C1E0: the address after the tile
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        ld de,(de_in)
        add hl,de
        ex de,hl
        ld ($C1E0),de
        ld a,(fl)
        and 2
        jr z,.nx
        exx
        ld de,($C1E0)
        exx
.nx:    pop hl
        ld bc,$00BE
        ld a,(orm)
        or a
        jr z,.a0
        ld a,(a2)
        ex af,af'
.a0:    ld a,(a1)
        pop iy
        pop ix
        ld sp,(g_sp)
        ei
        ret
; hf: in the left-to-right forms, A through the game's bit-reverse table at $0500.
hf:     push hl
        ld l,a
        ld a,(fl)
        and 2
        ld a,l
        jr z,.n
        ld h,$05
        ld a,(hl)
.n:     pop hl
        ret
g_sp:   dw 0
de_in:  dw 0
rows:   db 0
fl:     db 0
orm:    db 0
a1:     db 0
a2:     db 0
stk:    ds 64
stk_top:
tbuf:   ds 256*4
endpage

# smspower-WWFWrestleManiaSteelCageChallenge-SMS.html, "Enemy Zero Life": RAM $C48B is the
# opponent's energy byte (the player's is $C40B); 00 empties the opponent's energy bar
poke "Enemy zero life"
ar 00C4-8B00
endpoke
