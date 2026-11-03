# Columns (USA, Europe, Brazil) (En), CRC32 665FDA92, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output with a reference I/O log
# of 600 s, then decided by hand.
#
# Decisions:
# - Every RST vector holds game code ($08 is the game's VDP address routine,
#   $28 and $30 load A and jump to $003B), so the JP at $0000 is the io vector and the
#   game starts at its target, $0083.
# - Every high and medium confidence I/O site is kept. The sites that the
#   reference log does not run are on plain code paths that static flow reaches.
# - The byte scan rows are not patched; data/scan-verdicts.tsv has them as
#   unused: the head of the unrolled OUTI run $076B-$1111 (the game enters it
#   only at $1013, $1093 and $10D3), the unrolled OUT runs at $112D and
#   $1145, the VRAM routines at $0614, $0628 and $0674, and the sound stop
#   routine at $46AE. Nothing in the cart names any of them. The low rows at
#   $001A and $001D are in a VDP address routine at $0018 that nothing calls.
# - The cartarea_store rows at $4C73-$4CD2 and the jump into RAM at $4D10
#   (bank 1) are data, a sound table that the scanner decodes as code through
#   entry $4C6F of the table it reads at $4B03. They get no spec lines.
# - The seven indirect jumps the scanner could not follow ($051C, $13C4,
#   $13ED, $1423, $144C, $28BD, $2DA4) lead to no I/O that the 600 s log
#   saw unpatched.
# - priority is off. The game sets the priority bit on every name table
#   cell, and rewrites the well's 108 cells every frame, so with the switch
#   the runtime redraws priority cells all the time: 210% of a frame in
#   those frames, and the game runs at about a third of its speed. On the
#   Master System the bit matters only for the star sprites, single pixels
#   that hide behind the non-zero pixels of the side panels and the well's
#   frame. Page 0 (satup) does that work instead, when the game writes the
#   sprite table.
name Columns
cart 665FDA92
hz any		; No-Intro regions USA, Europe, Brazil
# No free RST vector: the JP at $0000 becomes the vector, the game
# starts at its target.
vector 00 io
start 0083
asm 00087 2   ; IM 1 -> IM 2
    im 2
endasm
# Sprite table upload ($0438-$0456, called from the frame handler): the game
# writes 64 Y bytes from $C300 to VRAM $3F00, then 128 X and tile bytes from
# $C340 to $3F80. Page 0 writes the same bytes, with the Y of each star sprite
# that the Master System would hide behind the background moved off the
# screen.
asm 00438 5
    rst $00
    db far_io, pg_satup, ent_satup
    ret
endasm
page 0 satup
    OPT --zxnext        ; NEXTREG, MUL, ADD HL,A, ADD DE,A
; satup: the game's sprite table upload, with the priority rule for the star
; sprites. A star is a sprite whose tile is 64-68 and whose pattern is one
; pixel, at its top left. On the Master System a sprite pixel is hidden
; where the background cell has the priority bit and its pixel is not 0. A
; star's only pixel is at (X, Y + 1); when that background pixel hides it,
; the Y written is $C0, below the 192 lines, so the star is not shown. The
; game's RAM copy is not changed. The game uses no scroll, no left shift and
; 8x8 sprites, and keeps the name table at $3800 (the reference I/O log).
; Runs in the frame handler with interrupts off, on a stack of its own.
; Keeps every register. Runtime internals: SHADOW_PAGE 28, 29 (the VRAM
; copy, mapped here in slots 2 and 3, VRAM $0000-$3FFF at $4000-$7FFF).
satup:  ld (su_sp),sp
        ld sp,su_stk
        push af
        push bc
        push de
        push hl
        push ix
        push iy
        ld hl,$C300             ; the game's Y bytes, to change here
        ld de,su_y
        ld bc,64
        ldir
        ld bc,$243B             ; keep MMU2 and MMU3
        ld a,$52
        out (c),a
        inc b
        in a,(c)
        ld (su_m2),a
        dec b
        ld a,$53
        out (c),a
        inc b
        in a,(c)
        ld (su_m3),a
        nextreg $52,28          ; the VRAM copy at $4000
        nextreg $53,29
; su_ok: 0 for each of tiles 64-68 that is a star (the pixel at (0,0) only)
        ld de,$6000+64*32       ; DE = tile 64's pattern
        ld hl,su_ok
        ld c,5
.tl:    push hl
        ex de,hl
        ld a,(hl)               ; row 0: the left pixel only
        inc hl
        or (hl)
        inc hl
        or (hl)
        inc hl
        or (hl)
        inc hl
        xor $80
        ld b,28                 ; rows 1-7: no pixels
.tz:    or (hl)
        inc hl
        djnz .tz
        ex de,hl                ; DE = the next tile
        pop hl
        ld (hl),a
        inc hl
        dec c
        jr nz,.tl
; each sprite up to the $D0 end mark
        ld hl,su_y
        ld ix,$C340             ; X, tile
        ld b,64
.sp:    ld a,(hl)
        cp $D0
        jp z,.end
        cp $BF                  ; the pixel's line Y + 1 is off the screen
        jr nc,.nx
        ld a,(ix+1)
        sub 64
        cp 5
        jr nc,.nx
        push hl
        ld hl,su_ok
        add hl,a
        ld a,(hl)
        pop hl
        or a
        jr nz,.nx
        push hl
        push bc
        ld a,(hl)
        inc a
        ld c,a                  ; C = the line
        and $F8
        ld e,a
        ld d,8
        mul d,e                 ; DE = the cell row * 64
        ld a,(ix+0)
        rrca
        rrca
        and $3E
        add de,a                ; + the cell column * 2
        ld hl,$7800             ; the name table, $3800 in the copy
        add hl,de
        ld e,(hl)
        inc hl
        ld d,(hl)               ; DE = the cell
        bit 4,d
        jr z,.vis               ; no priority bit
        ld a,c
        and 7
        bit 2,d                 ; V flip
        jr z,.nv
        xor 7
.nv:    add a,a
        add a,a
        ld l,a                  ; L = the pattern row * 4
        ld a,e                  ; HL = $4000 + tile * 32 + row * 4
        rrca
        rrca
        rrca
        ld c,a
        and $1F
        or $40
        bit 0,d
        jr z,.lo
        or $20
.lo:    ld h,a
        ld a,c
        and $E0
        or l
        ld l,a
        ld a,(hl)               ; C = the row's pixels that are not 0
        inc hl
        or (hl)
        inc hl
        or (hl)
        inc hl
        or (hl)
        ld c,a
        ld a,(ix+0)
        and 7
        bit 1,d                 ; H flip
        jr z,.nh
        xor 7
.nh:    ld hl,su_bit
        add hl,a
        ld a,(hl)
        and c
        jr z,.vis
        pop bc
        pop hl
        ld (hl),$C0             ; hidden: below the screen
        jr .nx
.vis:   pop bc
        pop hl
.nx:    inc hl
        inc ix
        inc ix
        dec b
        jp nz,.sp
.end:   ld a,(su_m2)
        nextreg $52,a
        ld a,(su_m3)
        nextreg $53,a
        ld hl,su_y              ; the Y bytes, from this page
        ld de,$3F00
        ld bc,$4001
        ld ix,64
        ld iy,64
        ld a,1
        call jt_vwrite
        ld hl,$C340             ; the X and tile bytes, as the game sees them
        ld de,$3F80
        ld bc,$8001
        ld ix,128
        ld iy,128
        xor a
        call jt_vwrite
        pop iy
        pop ix
        pop hl
        pop de
        pop bc
        pop af
        ld sp,(su_sp)
        ret
su_bit: db $80,$40,$20,$10,$08,$04,$02,$01
su_ok:  ds 5
su_m2:  db 0
su_m3:  db 0
su_sp:  dw 0
su_y:   ds 64
        ds 128
su_stk:
endpage
site 0000A   ; OUT ($BF),A
site 0000F   ; OUT ($BF),A
site 0003B   ; OUT ($BF),A
site 0003F   ; OUT ($BF),A
site 000BE   ; IN A,($7E)
site 000C5   ; OUT ($BF),A
site 000C9   ; OUT ($BF),A
site 000D0   ; OUT ($BE),A
site 00108   ; IN A,($BF)
site 00111   ; OTIR
site 00128   ; OUT ($3F),A
site 0012A   ; IN A,($DD)
site 00134   ; OUT ($3F),A
site 00136   ; IN A,($DD)
site 0013F   ; OUT ($3F),A
site 001F8   ; IN A,($BF)
site 002A1   ; OUT ($BF),A
site 002A6   ; OUT ($BF),A
site 002E2   ; OUT ($BF),A
site 002E7   ; OUT ($BF),A
site 0032F   ; OUT ($BF),A
site 00334   ; OUT ($BF),A
site 0034A   ; OUT ($BF),A
site 0034F   ; OUT ($BF),A
site 00387   ; OUT ($BF),A
site 0038C   ; OUT ($BF),A
site 003A2   ; OUT ($BF),A
site 003A7   ; OUT ($BF),A
site 003DA   ; OUT ($BF),A
site 003DF   ; OUT ($BF),A
site 00405   ; OUT ($BF),A
site 0040A   ; OUT ($BF),A
site 00420   ; IN A,($DD)
site 004F3   ; IN A,($DC)
site 004F6   ; IN A,($DD)
site 00502   ; IN A,($DC)
otir 0060A   ; OUTI
site 0063B   ; OUT (C),A
site 00640   ; OUT (C),A
site 0064D   ; OUTI
site 0064F   ; OUTI
site 00662   ; OUTI
site 00666   ; OUTI
site 006C2   ; OUT ($BF),A
site 006C6   ; OUT ($BF),A
site 006F5   ; OUT ($BE),A
site 0075E   ; OUT (C),D
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
site 01035   ; OUTI
site 01037   ; OUTI
site 01039   ; OUTI
site 0103B   ; OUTI
site 0103D   ; OUTI
site 0103F   ; OUTI
site 01041   ; OUTI
site 01043   ; OUTI
site 01045   ; OUTI
site 01047   ; OUTI
site 01049   ; OUTI
site 0104B   ; OUTI
site 0104D   ; OUTI
site 0104F   ; OUTI
site 01051   ; OUTI
site 01053   ; OUTI
site 01055   ; OUTI
site 01057   ; OUTI
site 01059   ; OUTI
site 0105B   ; OUTI
site 0105D   ; OUTI
site 0105F   ; OUTI
site 01061   ; OUTI
site 01063   ; OUTI
site 01065   ; OUTI
site 01067   ; OUTI
site 01069   ; OUTI
site 0106B   ; OUTI
site 0106D   ; OUTI
site 0106F   ; OUTI
site 01071   ; OUTI
site 01073   ; OUTI
site 01075   ; OUTI
site 01077   ; OUTI
site 01079   ; OUTI
site 0107B   ; OUTI
site 0107D   ; OUTI
site 0107F   ; OUTI
site 01081   ; OUTI
site 01083   ; OUTI
site 01085   ; OUTI
site 01087   ; OUTI
site 01089   ; OUTI
site 0108B   ; OUTI
site 0108D   ; OUTI
site 0108F   ; OUTI
site 01091   ; OUTI
site 01093   ; OUTI
site 01095   ; OUTI
site 01097   ; OUTI
site 01099   ; OUTI
site 0109B   ; OUTI
site 0109D   ; OUTI
site 0109F   ; OUTI
site 010A1   ; OUTI
site 010A3   ; OUTI
site 010A5   ; OUTI
site 010A7   ; OUTI
site 010A9   ; OUTI
site 010AB   ; OUTI
site 010AD   ; OUTI
site 010AF   ; OUTI
site 010B1   ; OUTI
site 010B3   ; OUTI
site 010B5   ; OUTI
site 010B7   ; OUTI
site 010B9   ; OUTI
site 010BB   ; OUTI
site 010BD   ; OUTI
site 010BF   ; OUTI
site 010C1   ; OUTI
site 010C3   ; OUTI
site 010C5   ; OUTI
site 010C7   ; OUTI
site 010C9   ; OUTI
site 010CB   ; OUTI
site 010CD   ; OUTI
site 010CF   ; OUTI
site 010D1   ; OUTI
site 010D3   ; OUTI
site 010D5   ; OUTI
site 010D7   ; OUTI
site 010D9   ; OUTI
site 010DB   ; OUTI
site 010DD   ; OUTI
site 010DF   ; OUTI
site 010E1   ; OUTI
site 010E3   ; OUTI
site 010E5   ; OUTI
site 010E7   ; OUTI
site 010E9   ; OUTI
site 010EB   ; OUTI
site 010ED   ; OUTI
site 010EF   ; OUTI
site 010F1   ; OUTI
site 010F3   ; OUTI
site 010F5   ; OUTI
site 010F7   ; OUTI
site 010F9   ; OUTI
site 010FB   ; OUTI
site 010FD   ; OUTI
site 010FF   ; OUTI
site 01101   ; OUTI
site 01103   ; OUTI
site 01105   ; OUTI
site 01107   ; OUTI
site 01109   ; OUTI
site 0110B   ; OUTI
site 0110D   ; OUTI
site 0110F   ; OUTI
site 01111   ; OUTI
site 01114   ; OUTI
site 01116   ; OUT ($BE),A
site 01118   ; OUTI
site 0111A   ; OUT ($BE),A
site 0111C   ; OUTI
site 0111E   ; OUT ($BE),A
site 01120   ; OUTI
site 01122   ; OUT ($BE),A
site 01124   ; OUTI
site 01126   ; OUT ($BE),A
site 01128   ; OUTI
site 0112A   ; OUT ($BE),A
site 0162C   ; OUT ($BE),A
site 01632   ; OUT ($BE),A
site 01637   ; OUT ($BE),A
site 0163D   ; OUT ($BE),A
site 017F8   ; IN A,($DC)
otir 02898   ; OUTI
site 02BC7   ; OUT ($BF),A
site 02BCB   ; OUT ($BF),A
site 02BD4   ; OUT ($BE),A
site 02BDA   ; OUT ($BE),A
site 02BF2   ; OUT ($BE),A
site 02BF8   ; OUT ($BE),A
site 02C0B   ; OUT ($BE),A
site 02C11   ; OUT ($BE),A
site 02C44   ; IN A,($BE)
site 02C46   ; IN A,($BE)
site 02C74   ; IN A,($BE)
site 02C79   ; IN A,($BE)
site 02C85   ; OUT ($BE),A
site 02C8B   ; OUT ($BE),A
site 02C92   ; OUT ($BE),A
site 02C98   ; OUT ($BE),A
site 02C9F   ; OUT ($BF),A
site 02CA3   ; OUT ($BF),A
site 02CAC   ; OUT ($BE),A
site 02CB1   ; OUT ($BE),A
site 02CB8   ; OUT ($BF),A
site 02CBC   ; OUT ($BF),A
site 02CC5   ; OUT ($BE),A
site 02CCA   ; OUT ($BE),A
site 02CD1   ; OUT ($BF),A
site 02CD5   ; OUT ($BF),A
site 02CDE   ; OUT ($BE),A
site 02CE4   ; OUT ($BE),A
site 02CFC   ; OUT ($BE),A
site 02D02   ; OUT ($BE),A
site 02D15   ; OUT ($BE),A
site 02D1B   ; OUT ($BE),A
site 02D34   ; OUT ($BE),A
site 02D3B   ; OUT ($BE),A
site 02D42   ; IN A,($BE)
site 02D48   ; IN A,($BE)
otir 02E7F   ; OUTI
site 03479   ; OUTI
site 0347E   ; OUT (C),A
site 034CE   ; OUT ($BE),A
site 034D3   ; OUT ($BE),A
site 034E9   ; OUT ($BE),A
site 034EE   ; OUT ($BE),A
site 034FB   ; OUT ($BE),A
site 03500   ; OUT ($BE),A
site 0350C   ; OUT ($BE),A
site 03511   ; OUT ($BE),A
site 03535   ; OUTI
site 0353A   ; OUT (C),A
site 03580   ; OUT ($BE),A
site 03585   ; OUT ($BE),A
site 03591   ; OUT ($BE),A
site 03596   ; OUT ($BE),A
site 044C2   ; OUT ($BE),A
site 044C8   ; OUT ($BE),A
site 044D1   ; OUT ($BE),A
site 044D7   ; OUT ($BE),A
site 044E0   ; OUT ($BE),A
site 044E6   ; OUT ($BE),A
site 04998   ; OTIR
site 04AAF   ; OUT ($7F),A
site 04AB9   ; OUT ($7F),A
site 04AD6   ; OUT ($7F),A
site 04AE7   ; OUT ($7F),A
site 04B78   ; OUT ($7F),A
site 04B86   ; OUT ($7F),A
site 04BD0   ; OUT ($7F),A
mapldk 00089   # LD HL,$FFFC; LD (HL),$00
maphl 0008F   # LD (HL),$00, HL = $FFFD
maphl 00092   # LD (HL),$01, HL = $FFFE
maphl 00095   # LD (HL),$02, HL = $FFFF
mapst 0023B   ; LD ($FFFF),A
mapst 0027C   ; LD ($FFFF),A
mapst 01654   ; LD ($FFFF),A
mapst 0176C   ; LD ($FFFF),A
mapst 017B4   ; LD ($FFFF),A
mapst 0187B   ; LD ($FFFF),A
mapst 01BAE   ; LD ($FFFF),A
mapst 01BDD   ; LD ($FFFF),A
mapst 01C15   ; LD ($FFFF),A
mapst 01C26   ; LD ($FFFF),A
mapst 01C70   ; LD ($FFFF),A
mapst 01CC5   ; LD ($FFFF),A
mapst 01CF9   ; LD ($FFFF),A
mapst 01D1C   ; LD ($FFFF),A
mapst 01D2D   ; LD ($FFFF),A
mapst 01D90   ; LD ($FFFF),A
mapst 01DC9   ; LD ($FFFF),A
mapst 01E28   ; LD ($FFFF),A
mapst 01E3C   ; LD ($FFFF),A
mapst 01E81   ; LD ($FFFF),A
mapst 01EB7   ; LD ($FFFF),A
mapst 01EDD   ; LD ($FFFF),A
mapst 01EEE   ; LD ($FFFF),A
mapst 01F49   ; LD ($FFFF),A
mapst 01F7E   ; LD ($FFFF),A
mapst 01FC7   ; LD ($FFFF),A
mapst 01FFC   ; LD ($FFFF),A
mapst 0205F   ; LD ($FFFF),A
mapst 020A4   ; LD ($FFFF),A
mapst 020E2   ; LD ($FFFF),A
mapst 02114   ; LD ($FFFF),A
mapst 02125   ; LD ($FFFF),A
mapst 021AA   ; LD ($FFFF),A
mapst 021F1   ; LD ($FFFF),A
mapst 0222D   ; LD ($FFFF),A
mapst 02283   ; LD ($FFFF),A
mapst 022EF   ; LD ($FFFF),A
mapst 0234E   ; LD ($FFFF),A
mapst 0237D   ; LD ($FFFF),A
mapst 023BC   ; LD ($FFFF),A
mapst 023CD   ; LD ($FFFF),A
mapst 0241C   ; LD ($FFFF),A
mapst 02471   ; LD ($FFFF),A
mapst 024A0   ; LD ($FFFF),A
mapst 024C3   ; LD ($FFFF),A
mapst 024D4   ; LD ($FFFF),A
mapst 02542   ; LD ($FFFF),A
mapst 0257B   ; LD ($FFFF),A

# Columns (USA, Europe) (Action Replay).cht, "Level Select": RAM $C699 is the level
poke "Start level"
ar 00C6-99??
endpoke

# Columns _ Shapes and Columns (USA, Europe, Brazil).cht, "Stay at Current Level"
poke "Stay at level"
gg 3A6-6BC-2A2
endpoke
