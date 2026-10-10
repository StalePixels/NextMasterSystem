# Canyon Racer 0.01alpha (haroldoop, Unlicense). 7626 bytes.
# Sites: the 27 from research/4-work/out/canyonracer.io.tsv, plus $1BD6,
# which a linear disassembly of the code ($0100-$1DC9) finds in load_tiles
# (the padding branch for tiles with fewer than 4 bitplanes; never runs).
# The game's code uses no RST; $0010-$0012 is z88dk header text.
name Canyon Racer 0.01alpha
cart EEAD16C7
hz 60		; a 60 Hz homebrew game
vector 10 out_n
vector 18 in_n
vector 20 ed
site 0135   ; OTIR
site 1B6E   ; OUT ($BF),A
site 1B72   ; OUT ($BF),A
site 1B76   ; OTIR
site 1BAD   ; OUT ($BF),A
site 1BB2   ; OUT ($BF),A
site 1BC4   ; OUT ($BE),A
site 1BD6   ; OUT ($BE),A
site 1D07   ; IN A,($DC)
site 1D15   ; OUT ($BF),A
site 1D19   ; OUT ($BF),A
site 1D1C   ; OUT ($BF),A
site 1D20   ; OUT ($BF),A
site 1D66   ; OUT ($BE),A
site 1D6A   ; OUT ($BE),A
site 1D75   ; OUT ($BF),A
site 1D7A   ; OUT ($BF),A
site 1D8D   ; OUT ($BF),A
site 1D91   ; OUT ($BF),A
site 1D94   ; OUT ($BE),A
site 1D9A   ; OUT ($BF),A
site 1D9E   ; OUT ($BF),A
site 1DA1   ; OUT ($BE),A
site 1DA4   ; OUT ($BE),A
site 1DAE   ; OUT ($BF),A
site 1DB1   ; OUT ($BF),A
site 1DBE   ; IN A,($7E)
site 1DC1   ; IN A,($7E)
# the framework's interrupts need IM 2 (vector table at $FD00)
asm 0122 2   ; IM 1 -> IM 2
    im 2
endasm
# Sprite routines as native code in page 0. At 60 Hz the frame's work ran into the next
# picture: the colour 0 writes at $16DE (black) and $1715 (red, the crash flash) landed in
# it, and the lines between them showed a black band. The game's own share of that work
# is mostly sprite table writes through the traps.
# The loop at $178B-$17C0 hides sprites i to 9 (i at SP+$AD) with the sprite set routine,
# about 6,800 Next cycles a sprite through the traps: about 68,000 a frame after a crash.
# Its test at $17B1 now does every pass of the loop in one far call.
asm 17B1 16
    call jt_far
    db pg_sprhide, ent_sprhide
    jp $17C1
endasm
# The sprite set routine ($1D7E, z88dk C, 4 stack arguments: tile, Y, X, sprite n) writes
# Y to VRAM $3F00 + n and X and the tile to $3F80 + 2n with four control writes and three
# data writes, about 6,300 Next cycles through the traps.
asm 1D7E 6
    call jt_far
    db pg_sprset, ent_sprset
    ret
endasm
page 0 sprset sprhide
; sprset: does what the game's code at $1D7E-$1DA6 does, with two jt_vwrite calls. The
; arguments are above the far call's three words and the game's return address.
; Returns with the registers and flags that code leaves: A = D = tile, B = Y, C = X,
; E = n, HL = the address of n's argument.
sprset: ld hl,8
        add hl,sp
        ld d,(hl)               ; tile
        inc hl
        inc hl
        ld b,(hl)               ; Y
        inc hl
        inc hl
        ld c,(hl)               ; X
        inc hl
        inc hl
        ld e,(hl)               ; n
        push hl
        push de
        push bc
        ld a,b
        ld (sy),a
        ld a,c
        ld (sxt),a
        ld a,d
        ld (sxt+1),a
        ld d,$3F                ; DE = $3F00 + n: Y
        ld hl,sy
        ld bc,$0101             ; one run of one byte
        ld a,1                  ; the source as mapped now (this page)
        call jt_vwrite
        ld a,e
        add a,a
        or $80
        ld e,a                  ; DE = $3F80 + 2n: X, tile
        ld hl,sxt
        ld b,2
        ld a,1
        call jt_vwrite
        pop bc
        pop de
        pop hl
        ld a,e
        add a,a
        or $80                  ; the flags the game's code leaves
        ld a,d
        ret
sy:     db 0
sxt:    db 0, 0
; sprhide: does what the loop at $178B-$17C0 does from its test at $17B1: for the
; game's i (16 bits at SP+$AD in its frame, above the far call's three words) from i
; to 9, sprite i gets Y = $F0, X = $F0 and tile 0, then i = 10. Two jt_vwrite calls:
; the Y bytes from $3F00 + i, the X and tile pairs from $3F80 + 2i. A negative i is
; not handled (the game counts sprites up from 0). With at least one pass, BC = 9 as
; the loop's last POP leaves it; the code after the loop sets A, DE, HL and the flags.
sprhide: ld hl,$AD+6
        add hl,sp
        ld a,(hl)
        inc hl
        or a
        ld e,a                  ; E = i
        ld a,(hl)
        or a
        ret nz                  ; i >= 256: no pass
        ld a,e
        cp 10
        ret nc                  ; i >= 10: no pass
        ld (hl),0
        dec hl
        ld (hl),10              ; i = 10
        neg
        add a,10
        ld b,a                  ; B = 10 - i sprites
        ld c,1                  ; one run
        ld d,$3F                ; DE = $3F00 + i: Y
        ld hl,hide_y
        ld a,1                  ; the source as mapped now (this page)
        call jt_vwrite
        ld a,e
        add a,a
        or $80
        ld e,a                  ; DE = $3F80 + 2i: X, tile
        sla b                   ; 2 bytes a sprite
        ld hl,hide_xt
        ld a,1
        call jt_vwrite
        ld bc,9
        ret
hide_y: db $F0,$F0,$F0,$F0,$F0,$F0,$F0,$F0,$F0,$F0
hide_xt: db $F0,0,$F0,0,$F0,0,$F0,0,$F0,0,$F0,0,$F0,0,$F0,0,$F0,0,$F0,0
endpage
