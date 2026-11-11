# Vigilante (USA, Europe, Brazil) (En), CRC32 DFB0B161, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with no reference logs.
#
# Decisions:
# - No free RST vector ($0018 holds a delay loop, $0028 the end of the RST $20 routine):
#   $0000-$0002 (DI; IM 1) becomes the io vector and the game starts at $0003. The reset
#   button's JP Z,$0000 at $022D goes to the start through fw_io0. The game has no RST $00.
name Vigilante
cart DFB0B161
hz any		; No-Intro regions USA, Europe, Brazil
vector 00 io
workline 1
start 0003
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
site 0020E   ; IN A,($BF)
site 00229   ; IN A,($DD)
site 00267   ; IN A,($7E)
site 00270   ; OUT ($BF),A
site 00274   ; OUT ($BF),A
site 00345   ; OTIR
site 0034C   ; OUT (C),A
site 0038A   ; OUT ($3E),A
site 00392   ; OUT ($F2),A
site 00395   ; IN A,($F2)
site 003A7   ; OUT ($F2),A
site 003AF   ; OUT ($3E),A
site 003B7   ; OUT ($3F),A
site 003B9   ; IN A,($DD)
site 003C3   ; OUT ($3F),A
site 003C5   ; IN A,($DD)
site 003CE   ; OUT ($3F),A
site 00727   ; IN A,($BF)
site 00879   ; IN A,($BF)
site 008BF   ; OUT ($BE),A
site 008C2   ; OUT ($BE),A
site 00902   ; IN A,($BF)
site 00A76   ; OUT ($BE),A
site 00A79   ; OUT ($BE),A
site 00AB4   ; IN A,($BF)
site 00AF5   ; OUT (C),L
site 00AF9   ; OUT (C),H
site 00B88   ; OUT ($BE),A
site 00B8B   ; OUT ($BE),A
site 00B9F   ; OUT ($BE),A
site 00BA2   ; OUT ($BE),A
site 00BDA   ; IN A,($BF)
site 00F90   ; OUT (C),L
site 00F94   ; OUT (C),H
site 00FA3   ; IN A,($BF)
site 01456   ; OUT ($BE),A
site 0145C   ; OUT ($BE),A
site 01462   ; OUT ($BE),A
site 01468   ; OUT ($BE),A
site 014A2   ; OUT ($BE),A
site 014A8   ; OUT ($BE),A
site 014AE   ; OUT ($BE),A
site 014B4   ; OUT ($BE),A
site 01537   ; OUT ($BE),A
site 0153D   ; OUT ($BE),A
site 01544   ; OUT ($BE),A
site 0154A   ; OUT ($BE),A
site 0156D   ; OUT ($BE),A
site 01573   ; OUT ($BE),A
site 015BA   ; OUT ($BE),A
site 015C0   ; OUT ($BE),A
site 015E5   ; OUT ($BE),A
site 015EB   ; OUT ($BE),A
site 01965   ; OUT ($BE),A
site 0196B   ; OUT ($BE),A
site 01AE8   ; OUT ($BE),A
site 01AEE   ; OUT ($BE),A
site 01AFC   ; OUT ($BE),A
site 01B02   ; OUT ($BE),A
site 01B96   ; IN A,($BF)
site 01C80   ; OUT ($BE),A
site 01C98   ; OUT (C),B
site 01CDB   ; OUT ($BE),A
site 01CE8   ; IN A,($DC)
site 01D17   ; OUT (C),A
site 01ED6   ; OUT ($BE),A
site 01EDC   ; OUT ($BE),A
site 01EE3   ; OUT ($BE),A
otir 01F04   ; OUTI
site 020D5   ; OUT ($BE),A
site 020DB   ; OUT ($BE),A
site 0215E   ; OUT ($BE),A
site 02164   ; OUT ($BE),A
site 0217C   ; OUT ($BE),A
site 02181   ; OUT ($BE),A
site 021AE   ; OUT ($BE),A
site 021BB   ; OUT ($BE),A
site 021ED   ; OUT ($BE),A
site 021FE   ; OUT ($BE),A
site 02204   ; OUT ($BE),A
site 0221B   ; OUT ($BE),A
site 0222C   ; OUT ($BE),A
site 02232   ; OUT ($BE),A
site 0224A   ; OUT ($BE),A
site 0225D   ; OUT ($BE),A
site 02266   ; OUT ($BE),A
site 02282   ; OUT ($BE),A
site 02293   ; OUT ($BE),A
site 02299   ; OUT ($BE),A
site 022B0   ; OUT ($BE),A
site 022C1   ; OUT ($BE),A
site 022C7   ; OUT ($BE),A
site 022DF   ; OUT ($BE),A
site 022F2   ; OUT ($BE),A
site 022FB   ; OUT ($BE),A
site 024C3   ; OUT ($BE),A
site 024D8   ; OUT ($BE),A
site 07A9D   ; OUT ($BF),A
site 07AA0   ; OUT ($BF),A
site 07B73   ; OUT ($BE),A
site 07B78   ; OUT ($BE),A
site 07B7D   ; OUT ($BE),A
site 07B82   ; OUT ($BE),A
site 24193   ; OUT ($F0),A
site 2419C   ; OUT ($F1),A
site 241BE   ; OUT ($7F),A
site 241C2   ; OUT ($F0),A
site 241C8   ; OUT ($F1),A
site 241E4   ; OUT ($7F),A
site 241F4   ; OUT (C),D
site 241FA   ; OUT ($F1),A
site 24224   ; OUT ($7F),A
site 24228   ; OUT ($7F),A
site 24256   ; OTIR
site 24269   ; OUT ($F0),A
site 24277   ; OUT ($F1),A
site 24280   ; OTIR
site 2428A   ; OUT ($F0),A
site 24290   ; OUT ($F1),A
site 2429C   ; OUTI
site 242A2   ; OUTI
site 24302   ; OUT ($7F),A
site 24306   ; OUT ($7F),A
site 2430A   ; OUT ($7F),A
site 2439B   ; OUT ($7F),A
site 2439F   ; OUT ($7F),A
site 243B6   ; OUT ($7F),A
site 243DE   ; OUT ($7F),A
site 243E2   ; OUT ($7F),A
site 243E6   ; OUT ($7F),A
site 243EA   ; OUT ($7F),A
site 243ED   ; OUT ($7F),A
site 24453   ; OUT ($F0),A
site 2445A   ; OUT ($F1),A
site 24462   ; OUT ($F0),A
site 24468   ; OUT ($F1),A
site 24569   ; OUT ($F0),A
site 24573   ; OUT (C),L
site 2457C   ; OUT ($F0),A
site 24597   ; OUT (C),H
site 2459F   ; OUT ($F0),A
site 245AD   ; OUT ($F1),A
site 245B9   ; OUT ($F0),A
site 245C2   ; OUT ($F1),A
site 2477A   ; OUT ($F0),A
site 24783   ; OUT (C),A
site 24788   ; OUT ($F0),A
site 2478E   ; OUTI
site 247B5   ; OUT ($F0),A
site 247BD   ; OUT (C),A
site 247C4   ; OUT ($F0),A
site 247CC   ; OUT (C),A
site 248C4   ; OUT ($7F),A
site 248F2   ; OUT ($7F),A
site 248F6   ; OUT ($7F),A
site 24900   ; OUT ($7F),A
site 2490E   ; OUT ($7F),A
site 2493A   ; OUT ($F0),A
site 24948   ; OUT ($F1),A
site 2495C   ; OUT (C),A
site 24967   ; OUT ($F0),A
site 2496D   ; OUTI
site 24978   ; OUT ($F0),A
site 24A0F   ; OUTI
site 24A11   ; OUTI
site 24A13   ; OUTI
site 24A15   ; OUTI
site 24A17   ; OUTI
site 24A19   ; OUTI
site 24A1B   ; OUTI
site 24A1D   ; OUTI
site 24A1F   ; OUTI
site 24A21   ; OUTI
site 24A23   ; OUTI
site 24A2D   ; OUT (C),D
site 24A33   ; OUT ($F1),A
site 24A72   ; OUT ($7F),A
site 24AC8   ; OUT ($7F),A
site 24B07   ; OUT ($7F),A
site 24B69   ; OUT ($7F),A
site 24B89   ; OUT ($7F),A
site 24BD5   ; OUT ($7F),A
site 24BDF   ; OUT ($7F),A
site 24C27   ; OUT ($7F),A
mapst 00232   ; LD ($FFFF),A
mapst 00254   ; LD ($FFFF),A
mapst 00290   ; LD ($FFFF),A
mapst 0031D   ; LD ($FFFF),A
mapst 003EE   ; LD ($FFFF),A
mapst 0043F   ; LD ($FFFF),A
mapst 00576   ; LD ($FFFF),A
mapst 0059E   ; LD ($FFFF),A
mapst 006E8   ; LD ($FFFF),A
mapst 00704   ; LD ($FFFF),A
mapst 0072F   ; LD ($FFFF),A
mapst 00850   ; LD ($FFFF),A
mapst 00863   ; LD ($FFFF),A
mapst 008A1   ; LD ($FFFF),A
mapst 008AC   ; LD ($FFFF),A
mapst 008DF   ; LD ($FFFF),A
mapst 00A42   ; LD ($FFFF),A
mapst 00A50   ; LD ($FFFF),A
mapst 00A63   ; LD ($FFFF),A
mapst 00A96   ; LD ($FFFF),A
mapst 00BB6   ; LD ($FFFF),A
mapst 00F7C   ; LD ($FFFF),A
mapst 01922   ; LD ($FFFF),A
mapst 0192D   ; LD ($FFFF),A
mapst 01A39   ; LD ($FFFF),A
mapst 01A44   ; LD ($FFFF),A
mapst 01AA3   ; LD ($FFFF),A
mapst 01B38   ; LD ($FFFF),A
mapst 01B5D   ; LD ($FFFF),A
mapst 01B75   ; LD ($FFFF),A
mapst 01E2D   ; LD ($FFFF),A
mapst 01F73   ; LD ($FFFF),A
mapst 020BE   ; LD ($FFFF),A
mapst 0210B   ; LD ($FFFF),A
mapst 02193   ; LD ($FFFF),A
mapst 0232A   ; LD ($FFFF),A
mapst 024A5   ; LD ($FFFF),A
mapst 026CC   ; LD ($FFFF),A
mapst 031EB   ; LD ($FFFF),A
mapst 07880   ; LD ($FFFF),A

# The sprite table and the fighters' art. The frame handler's $21C4 writes the sprite table
# from the buffer at $D000 when $C020 is set (48 entries of Y, X, N; the order and the place
# of the first 12 depend on $CB00 and on bit 0 of the frame count $C009) and passes the
# player's new-art flag $CB1A on to $C136. The line handler at line 30 then uploads the new
# art with $2480: the player's from ($CB16) to VRAM $2000 (576 bytes for a punch), and the art
# of the first of the two enemies ($CB40, $CB80) whose flag (IX+$1A) the game set with the
# same sprite table. On a Master System the art lands at line 32, before the fighters' lines
# (from 113). On the Next the once-a-frame work took the new table in one frame and the art a
# frame later, so for one frame the new pose showed the old tiles (stray tiles at punch starts
# and turns). The 144 single writes of the table also took about 85,000 cycles, past the ULA
# interrupt's line. Page entry sprites, from $21D1 (after $21C4's test of $C020), does $21C4's
# work and then $2480's, all with jt_vwrite: the table and the art reach the VRAM copy before
# the once-a-frame work. workline 1: the table and the art take about 80,000 and up to about
# 220,000 cycles, so the handler runs past the ULA interrupt's line, and vbl_chk ran the work
# at a runtime call between the two. With the switch the ULA interrupt does not arm vbl_chk,
# and the work runs at the ULA interrupt, which waits for the handler's EI, or at line 1. The
# line handler's own CALL $2480 finds the flags clear, and still
# uploads the second enemy's art when both enemies changed, as on the Master System.
asm 021D1 5    ; LD A,$00 : LD ($C020),A
    rst $00
    db far_io, pg_sprites, ent_sprites
    ret
endasm
page 0 sprites
; sprites: from $21D1, in the frame handler (interrupts off), when $C020 is set. Does $21C4's
; work from $21D1: $C020 = 0, the sprite table from $D000 (entries of 3 bytes: Y, X, N) and
; $C136 = $CB1A, $CB1A = 0. Then $2480's: the player's art when $C136 bit 7 is set ($2188),
; then the first enemy whose art flag is set ($2494). Each object's art is a header (C, B: the
; game's DJNZ counts) and the bytes, in the bank the object names, mirrored through the
; bit-reverse table at $0100 when its flag bit 0 is set ($21B7, $24D4). Leaves the VDP address
; after the last byte and slot 2 holding the last bank mapped, as the game's routines do.
; Changes AF, BC, DE, HL, IX, IY and the alternate HL; the frame handler saves all of them.
BUFSZ   equ 4096
sprites:
        xor a
        ld ($C020),a
        ld a,($CB00)            ; $21D6: $0D and $1C put entries 0-11 at 36-47
        cp $0D
        jr z,.b
        cp $1C
        jr z,.b
        ld de,$3F00             ; $21E3: entries 0-11 at 0-11, 12-47 at 12-47
        ld bc,$3F80
        call sat12
        ld de,$3F0C
        ld bc,$3F98
        jr .rest
.b:     ld de,$3F24             ; $2278: entries 0-11 at 36-47, 12-47 at 0-35
        ld bc,$3FC8
        call sat12
        ld de,$3F00
        ld bc,$3F80
.rest:  push bc
        ld a,($C009)
        and 1
        jr z,.down
        ld hl,$D024             ; entries 12-47 in order
        ld ix,3
        jr .y
.down:  ld hl,$D08D             ; entries 47-12, the order turned round
        ld ix,-3
.y:     push hl
        ld bc,$0124             ; 36 runs of 1: Y
        ld iy,1
        xor a
        call jt_vwrite
        pop hl
        inc hl
        pop de
        ld bc,$0224             ; 36 runs of 2: X, N
        ld iy,2
        xor a
        call jt_vwrite
        ld a,($CB1A)
        ld ($C136),a
        xor a
        ld ($CB1A),a
        jr art
; sat12: entries 0-11, Y to VRAM DE, X and N to VRAM BC.
sat12:  push bc
        ld hl,$D000
        ld bc,$010C             ; 12 runs of 1: Y
        ld ix,3
        ld iy,1
        xor a
        call jt_vwrite
        pop de
        inc hl
        ld bc,$020C             ; 12 runs of 2: X, N
        ld iy,2
        xor a
        jp jt_vwrite
art:    ld hl,$C136
        bit 7,(hl)
        jr z,.en
        ld (hl),0
        ld a,($CB28)
        rst $00
        db $13,$00              ; LD ($FFFF),A through the runtime
        ld hl,($CB16)
        ld a,h
        or l
        jr z,.en
        ld de,$2000
        ld a,($CB1B)
        call upload
.en:    ld ix,$CB40
        call enemy
        ret nz
        ld ix,$CB80
; enemy: $2494 for the object at IX. Returns NZ when it wrote art, Z when not.
enemy:  ld a,(ix+$00)
        or a
        ret z
        bit 7,(ix+$1A)
        ret z
        ld (ix+$1A),0
        ld a,(ix+$28)
        rst $00
        db $13,$00              ; LD ($FFFF),A through the runtime
        ld l,(ix+$16)
        ld h,(ix+$17)
        ld a,h
        or l
        ret z
        ld e,(ix+$18)
        ld d,(ix+$19)
        ld a,(ix+$1B)
        push ix
        call upload
        pop ix
        ld a,(ix+$1E)
        ld (ix+$1F),a
        xor a
        inc a
        ret
; upload: HL = the art's header, DE = the VRAM address, A bit 0 = mirrored. The bytes go
; through buf, BUFSZ at a time, each part with one jt_vwrite call.
upload: and 1
        ld (up_mir),a
        ld c,(hl)
        inc hl
        ld b,(hl)
        inc hl
        ld a,b                  ; bytes = B (0 is 256) + (C - 1) x 256
        or a
        jr nz,.nz
        ld b,c
        ld c,0
        jr .st
.nz:    dec c
        ld b,c
        ld c,a
.st:    ld (up_n),bc
        ld a,d
        and $3F
        ld d,a
.part:  ld bc,(up_n)
        push hl
        ld hl,BUFSZ
        or a
        sbc hl,bc
        pop hl
        jr nc,.k
        ld bc,BUFSZ
.k:     ld (up_k),bc
        push de
        ld de,buf
        ld a,(up_mir)
        or a
        jr nz,.mir
        ldir
        jr .w
.mir:   exx
        ld h,$01                ; the bit-reverse table
        exx
.m:     ld a,(hl)
        inc hl
        exx
        ld l,a
        ld a,(hl)
        exx
        ld (de),a
        inc de
        dec bc
        ld a,b
        or c
        jr nz,.m
.w:     pop de
        push hl
        call wbuf
        pop hl
        push hl
        ld hl,(up_n)
        ld bc,(up_k)
        or a
        sbc hl,bc
        ld (up_n),hl
        ld a,h
        or l
        pop hl
        jr nz,.part
        ret
; wbuf: the up_k bytes at buf to VRAM DE; DE = DE + up_k. In runs of 32 when up_k is a
; multiple of 32, else runs of 256 and the rest.
wbuf:   push de
        ld hl,(up_k)
        ld a,l
        and 31
        jr nz,.two
        add hl,hl
        add hl,hl
        add hl,hl
        ld c,h                  ; up_k / 32 runs
        ld b,32
        ld ix,32
        ld iy,32
        ld hl,buf
        ld a,1                  ; the source as mapped now (this page)
        call jt_vwrite
        jr .adv
.two:   ld a,h
        or a
        jr z,.r
        ld c,a                  ; up_k / 256 runs of 256
        ld b,0
        ld ix,256
        ld iy,256
        ld hl,buf
        ld a,1
        call jt_vwrite
.r:     ld hl,(up_k)
        ld l,0
        push hl
        add hl,de
        ex de,hl
        pop hl
        ld bc,buf
        add hl,bc
        ld a,(up_k)
        ld b,a                  ; the rest, one run
        ld c,1
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
.adv:   pop de
        ld hl,(up_k)
        add hl,de
        ld a,h
        and $3F
        ld d,a
        ld e,l
        ret
up_mir: db 0
up_n:   dw 0
up_k:   dw 0
buf:    ds BUFSZ
endpage

# Vigilante (USA, Europe, Brazil).cht, "Infinite Lives": RAM $C014 is the lives count; held at 9
# the game never reaches game over
poke "Infinite lives"
ar 00C0-1409
endpoke

# Vigilante (USA, Europe, Brazil).cht, "Infinite Health": RAM $C251 is the energy bar ($4F is
# full, $FF is dead) and $C254 follows it; both held at $47, the bar stays full
poke "Infinite energy"
ar 00C2-5147
ar 00C2-5447
endpoke

# Vigilante (USA, Europe, Brazil).cht, "Infinite Time": RAM $C291 is the time; held at $64 it
# shows 99 and never runs out
poke "Infinite time"
ar 00C2-9164
endpoke

# Vigilante (USA, Europe) (Action Replay).cht, "Level Select": RAM $C110 is the stage number.
# Values 00 to 04 start five different stages
poke "Start stage ??"
ar 00C1-10??
endpoke

# Vigilante (USA, Europe, Brazil).cht, "Always Have Nunchucks": RAM $C262 = $01 gives the
# player nunchucks in place of fists
poke "Nunchucks"
ar 00C2-6201
endpoke
