; A maze game for the Sega Master System, 32K cart, no mapper.
;
; The player walks a maze with the D-pad. Walking into the exit makes a new
; maze. Each maze comes from a random depth-first generator.
;
; Build: make boot in public/ (sjasmplus, then boot.py writes the checksum).

VDP_DATA    equ $BE
VDP_CTRL    equ $BF
PSG         equ $7F
PAD1        equ $DC

MW          equ 15              ; maze cells across
MH          equ 11              ; maze cells down
SPEED       equ 2               ; pixels a frame; 8 / SPEED frames a tile

; map values
FLOOR       equ 0
WALL        equ 1
EXIT        equ 2

; tile numbers (boot.py)
T_FLOOR     equ 0
T_WALL      equ 1
T_EXIT      equ 17
T_PLAYER    equ 18

; RAM
vbl         equ $C000           ; set by the frame interrupt
seed        equ $C001           ; 2: random state
pad         equ $C003           ; D-pad bits, 1 = held: up, down, left, right
px          equ $C004           ; player tile column
py          equ $C005           ; player tile row
mdir        equ $C006           ; move direction: 0 up, 1 down, 2 left, 3 right
mstep       equ $C007           ; frames left of the move, 0 = on a tile
face        equ $C008           ; 0 right, 1 left
snd_t       equ $C009           ; frames left of the exit sound
snd_p       equ $C00A           ; 2: its tone period
gsp         equ $C00C           ; 2: generator stack pointer
cur         equ $C00E           ; generator: current cell
nbuf        equ $C010           ; 4: generator: open neighbour steps
gstack      equ $C100           ; generator stack, one cell a byte
visited     equ $C200           ; 256, page aligned: cell visited flags
mapbuf      equ $C300           ; 32 bytes of floor above the map
map         equ $C320           ; 32 x 24 bytes, the maze in tiles 0-30 x 0-22
ntbuf       equ $C700           ; 28 x 32 name table entries

; a cell is one byte: row * 16 + column. Its tile is (2 * column + 1, 2 * row + 1).

    org $0000
    di
    im 1
    jp start

    ds $0038 - $, $FF

; frame interrupt
    push af
    in a,(VDP_CTRL)             ; read the status: clears the interrupt
    ld a,1
    ld (vbl),a
    pop af
    ei
    reti

    ds $0066 - $, $FF

; pause button
    retn

start:
    ld sp,$DFF0
    ld hl,vdp_init
    ld b,vdp_init_end - vdp_init
    ld c,VDP_CTRL
    otir
    ld hl,psg_off
    ld b,4
    ld c,PSG
    otir
    ld hl,$C000                 ; CRAM entry 0
    call vaddr
    ld hl,palette
    ld b,32
    ld c,VDP_DATA
    otir
    ld hl,$4000                 ; tiles from VRAM $0000
    call vaddr
    ld hl,tiles
    ld de,tiles_end - tiles
    call vcopy
    ld a,r
    ld l,a
    ld h,$A7
    ld (seed),hl
    xor a
    ld (snd_t),a
    call new_maze

main:
    call wait_vbl
    call put_sprite
    call sound
    call rand
    in a,(PAD1)
    cpl
    and $0F
    ld (pad),a
    call move
    jr main

; wait for the next frame interrupt
wait_vbl:
    ld hl,vbl
    xor a
    ld (hl),a
.w: cp (hl)
    jr z,.w
    ret

; HL = VDP address with the code in bits 14-15
vaddr:
    ld a,l
    out (VDP_CTRL),a
    ld a,h
    out (VDP_CTRL),a
    ret

; write DE bytes from HL to the VDP data port
vcopy:
    ld c,VDP_DATA
.l: ld a,d
    or a
    jr z,.t
    ld b,0
    otir
    dec d
    jr .l
.t: ld a,e
    or a
    ret z
    ld b,a
    otir
    ret

; A = random byte (xorshift, 16 bits)
rand:
    ld hl,(seed)
    ld a,h
    rra
    ld a,l
    rra
    xor h
    ld h,a
    ld a,l
    rra
    ld a,h
    rra
    xor l
    ld l,a
    xor h
    ld h,a
    ld (seed),hl
    ret

; display off, make and draw a maze, player at the top left, display on
new_maze:
    di
    ld a,$A0
    out (VDP_CTRL),a
    ld a,$81
    out (VDP_CTRL),a
    call gen
    call render
    ld a,1
    ld (px),a
    ld (py),a
    xor a
    ld (mstep),a
    ld (face),a
    call put_sprite
    in a,(VDP_CTRL)             ; drop an interrupt raised while drawing
    ld a,$E0
    out (VDP_CTRL),a
    ld a,$81
    out (VDP_CTRL),a
    ei
    ret

; ---- maze generator ---------------------------------------------------------
; Depth-first: from the top left cell, step to a random cell not yet visited,
; opening the wall between; back up when no such cell is next to this one.
gen:
    ld hl,mapbuf
    ld de,mapbuf + 1
    ld bc,32 + 24 * 32 - 1
    ld (hl),FLOOR
    ldir
    ld hl,map
    ld c,23
.row:
    ld b,31
.col:
    ld (hl),WALL
    inc hl
    djnz .col
    inc hl
    dec c
    jr nz,.row
    ld hl,visited
    ld de,visited + 1
    ld bc,255
    ld (hl),0
    ldir
    ld hl,gstack
    ld (gsp),hl
    xor a
    call visit
.loop:
    ld hl,(gsp)
    ld de,gstack
    or a
    sbc hl,de
    jp z,.done
    ld hl,(gsp)
    dec hl
    ld a,(hl)
    ld (cur),a
    ld c,a
    ld b,0
    ld hl,nbuf
    and $F0                     ; up
    jr z,.nu
    ld a,c
    sub 16
    call isfree
    jr nz,.nu
    ld (hl),-16
    inc hl
    inc b
.nu:
    ld a,c                      ; down
    and $F0
    cp (MH - 1) * 16
    jr z,.nd
    ld a,c
    add a,16
    call isfree
    jr nz,.nd
    ld (hl),16
    inc hl
    inc b
.nd:
    ld a,c                      ; left
    and $0F
    jr z,.nl
    ld a,c
    dec a
    call isfree
    jr nz,.nl
    ld (hl),-1
    inc hl
    inc b
.nl:
    ld a,c                      ; right
    and $0F
    cp MW - 1
    jr z,.nr
    ld a,c
    inc a
    call isfree
    jr nz,.nr
    ld (hl),1
    inc b
.nr:
    ld a,b
    or a
    jr nz,.pick
    ld hl,(gsp)                 ; no way on: back up
    dec hl
    ld (gsp),hl
    jr .loop
.pick:
    call rand
.mod:
    cp b
    jr c,.got
    sub b
    jr .mod
.got:
    ld e,a
    ld d,0
    ld hl,nbuf
    add hl,de
    ld b,(hl)                   ; B = the step to the new cell
    ld a,(cur)
    call celladdr
    ld a,b
    call stepoff
    add hl,de
    ld (hl),FLOOR               ; open the wall between
    ld a,(cur)
    add a,b
    call visit
    jp .loop
.done:
    ld hl,map + 21 * 32 + 30    ; the exit, in the right wall of the bottom right cell
    ld (hl),EXIT
    ret

; Z if cell A has not been visited; keeps BC, HL
isfree:
    push hl
    ld h,visited >> 8
    ld l,a
    ld a,(hl)
    or a
    pop hl
    ret

; mark cell A visited, open its tile, push it
visit:
    push af
    ld h,visited >> 8
    ld l,a
    ld (hl),1
    call celladdr
    ld (hl),FLOOR
    pop af
    ld hl,(gsp)
    ld (hl),a
    inc hl
    ld (gsp),hl
    ret

; HL = map address of the tile of cell A; DE changes
celladdr:
    ld l,a
    and $0F
    add a,a
    ld e,a
    ld d,0
    ld a,l
    and $F0
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,de
    ld de,map + 33
    add hl,de
    ret

; DE = map offset of one tile in the direction of cell step A
stepoff:
    ld de,-32
    cp -16
    ret z
    ld de,32
    cp 16
    ret z
    ld de,-1
    cp -1
    ret z
    ld de,1
    ret

; ---- drawing ----------------------------------------------------------------
; the name table from the map: walls take their tile from their wall neighbours
render:
    ld ix,map
    ld hl,ntbuf
    ld c,24
.row:
    ld b,32
.col:
    ld a,(ix+0)
    or a
    jr z,.put
    cp EXIT
    ld a,T_EXIT
    jr z,.put
    ld e,T_WALL
    ld a,(ix-32)
    cp WALL
    jr nz,.n1
    inc e
.n1:
    ld a,(ix+1)
    cp WALL
    jr nz,.n2
    inc e
    inc e
.n2:
    ld a,(ix+32)
    cp WALL
    jr nz,.n3
    ld a,e
    add a,4
    ld e,a
.n3:
    ld a,(ix-1)
    cp WALL
    jr nz,.n4
    ld a,e
    add a,8
    ld e,a
.n4:
    ld a,e
.put:
    ld (hl),a
    inc hl
    ld (hl),0
    inc hl
    inc ix
    djnz .col
    dec c
    jr nz,.row
    ld b,0                      ; rows 24-27: 128 floor entries
.z: ld (hl),0
    inc hl
    djnz .z
    ld hl,$7800                 ; name table at VRAM $3800
    call vaddr
    ld hl,ntbuf
    ld de,28 * 64
    jp vcopy

; the player sprite, with the terminator after it
put_sprite:
    ld a,(px)
    add a,a
    add a,a
    add a,a
    add a,4                     ; the map is 4 pixels right (H scroll 4)
    ld d,a
    ld a,(py)
    add a,a
    add a,a
    add a,a
    add a,3                     ; 4 pixels down (V scroll 220), less 1 for the sprite line
    ld e,a
    ld a,(mstep)
    or a
    jr z,.pos
    neg
    add a,8 / SPEED
    add a,a                     ; pixels moved: (8 / SPEED - mstep) * SPEED, SPEED 2
    ld c,a
    ld a,(mdir)
    or a
    jr nz,.d1
    ld a,e
    sub c
    ld e,a
    jr .pos
.d1:
    dec a
    jr nz,.d2
    ld a,e
    add a,c
    ld e,a
    jr .pos
.d2:
    dec a
    jr nz,.d3
    ld a,d
    sub c
    ld d,a
    jr .pos
.d3:
    ld a,d
    add a,c
    ld d,a
.pos:
    ld a,(face)
    add a,a
    ld b,a
    ld a,(mstep)
    and 2                       ; legs apart in the first half of a step
    jr z,.f
    inc b
.f: ld a,T_PLAYER
    add a,b
    ld b,a
    ld hl,$7F00                 ; sprite table at VRAM $3F00
    call vaddr
    ld a,e
    out (VDP_DATA),a
    ld a,$D0
    out (VDP_DATA),a
    ld hl,$7F80
    call vaddr
    ld a,d
    out (VDP_DATA),a
    ld a,b
    out (VDP_DATA),a
    ret

; ---- player -----------------------------------------------------------------
move:
    ld a,(mstep)
    or a
    jr nz,.go
    ld a,(py)                   ; on a tile: the exit makes a new maze
    ld l,a
    ld h,0
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    ld a,(px)
    ld e,a
    ld d,0
    add hl,de
    ld de,map
    add hl,de
    ld a,(hl)
    cp EXIT
    jr z,.exit
    ld a,(pad)                  ; the first held direction that is open
    ld c,a
    ld b,0
.try:
    srl c
    jr nc,.next
    push hl
    ld a,b
    add a,a
    ld e,a
    ld d,0
    ld hl,dirtab
    add hl,de
    ld e,(hl)
    inc hl
    ld d,(hl)
    pop hl
    push hl
    add hl,de
    ld a,(hl)
    pop hl
    cp WALL
    jr nz,.start
.next:
    inc b
    ld a,b
    cp 4
    jr nz,.try
    ret
.start:
    ld a,b
    ld (mdir),a
    cp 2
    jr c,.nf
    ld a,3
    sub b
    ld (face),a
.nf:
    ld a,8 / SPEED
    ld (mstep),a
.go:
    ld a,(mstep)
    dec a
    ld (mstep),a
    ret nz
    ld a,(mdir)                 ; the step ends on the next tile
    or a
    jr nz,.m1
    ld hl,py
    dec (hl)
    ret
.m1:
    dec a
    jr nz,.m2
    ld hl,py
    inc (hl)
    ret
.m2:
    dec a
    jr nz,.m3
    ld hl,px
    dec (hl)
    ret
.m3:
    ld hl,px
    inc (hl)
    ret
.exit:
    call snd_start
    jp new_maze

dirtab:
    dw -32, 32, -1, 1

; ---- sound ------------------------------------------------------------------
; a rising tone on PSG channel 0 for 24 frames
snd_start:
    ld a,24
    ld (snd_t),a
    ld hl,336
    ld (snd_p),hl
    ret

sound:
    ld a,(snd_t)
    or a
    ret z
    dec a
    ld (snd_t),a
    jr z,.off
    ld hl,(snd_p)
    ld de,-12
    add hl,de
    ld (snd_p),hl
    ld a,l
    and $0F
    or $80
    out (PSG),a
    ld a,l
    srl h
    rra
    srl h
    rra
    srl h
    rra
    srl h
    rra
    and $3F
    out (PSG),a
    ld a,(snd_t)
    neg
    add a,24
    srl a
    or $90
    out (PSG),a
    ret
.off:
    ld a,$9F
    out (PSG),a
    ret

; ---- data -------------------------------------------------------------------
vdp_init:
    db $06, $80                 ; mode 4, 192 lines
    db $A0, $81                 ; display off, frame interrupt on, 8x8 sprites
    db $FF, $82                 ; name table at $3800
    db $FF, $83
    db $FF, $84
    db $FF, $85                 ; sprite table at $3F00
    db $FB, $86                 ; sprite tiles from $0000
    db $00, $87                 ; border: sprite colour 0
    db $04, $88                 ; H scroll 4: the 31 maze columns in the middle
    db $DC, $89                 ; V scroll 220: the 23 maze rows in the middle
    db $FF, $8A                 ; no line interrupts
vdp_init_end:

psg_off:
    db $9F, $BF, $DF, $FF

palette:
    ; background: floor, floor dot, hedge dark, mid, light, leaf, exit yellow, white, orange
    db $1A, $15, $04, $08, $0C, $1D, $0F, $3F, $07, $00, $00, $00, $00, $00, $00, $00
    ; sprites: border, dark blue, light blue, skin, eye
    db $04, $20, $34, $1B, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00, $00

tiles:
    include "tiles.inc"
tiles_end:

    ds $7FF0 - $, $FF

; cart header: export Master System, 32K; boot.py writes the checksum
    db "TMR SEGA"
    db $FF, $FF
    dw 0
    db $00, $00, $00
    db $4C
