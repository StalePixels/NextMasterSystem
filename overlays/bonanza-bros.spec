# Bonanza Bros. (Europe, Brazil) (En), CRC32 CAEA8002, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with entry points from the game's state
# table and a reference I/O log (10 minutes, random input).
# Decisions:
# - No free RST vector ($0008-$0030 are the game's), so $0000 is the io vector.
# - The main loop at $014B calls state handlers through the 3-byte table at $08B0 (bank,
#   address), indexed by $C410 (states 0-$18). The scanner does not resolve this CALL $0017
#   at $0160; the entries that it does not reach otherwise ($08FB, $08FF, $0903, $090B, $091F,
#   $1BCF, $1C23, $21F1, bank 5 $9CF0, bank 7 $A350) were scanned as entry points.
# - The dispatch at $26BD reads the table at $32F5 (23 entries, index $CA5B) and $2B5F the
#   table at $3323 (16 entries, AND $0F). The scanner reads both tables on into the sprite
#   data that starts at $3343 and decodes $3343-$3C12 as code. That block is data: its two
#   IN A,($3B) at $39DF and $39E1 are not patched.
# - The RAM routines at $D700 and $D800 ($0C67) are runs of LDD and LDI with a RET: no I/O.
name Bonanza Bros.
cart CAEA8002
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
# The line interrupt at line 30 sets the play area's H scroll below the HUD. Through the
# runtime its register 8 write comes a line and a half late, and line 32 showed with the HUD's
# H scroll 0 (white and red dashes under the HUD where the play area scrolls). The routine
# gives the scroll of every line.
rastercode bonanza-bros-raster.asm
# The HUD (name table rows 0-3, lines 0-31) is all priority tiles with no colour 0 pixel, so
# on a Master System no sprite shows there. The game parks objects there (Y $07 and $0F,
# for example the safe of stage 5 over the "SC" of SCORE) and they hide behind it. The
# `priority` switch costs this game too much: the intro's priority cells leave tile 0
# marked as a priority tile, so each write of the animated tiles 0-7 redraws the HUD's cells,
# and the frame interrupt's display-on write then ends inside the picture.
# Code page 0 instead writes the sprite table for the three routines that write it, with
# every sprite of Y $00-$19 or $E0-$FF moved to Y $C0 (off the picture, the value the game
# gives unused sprites) while the HUD is up. A sprite of Y $19 has its last 2 lines below
# the HUD, and those are lost; random play on the reference had a sprite crossing the HUD's
# lower edge in 6 of 16,323 frames, always at Y $19.
# The HUD test reads the high bytes of name table cells (0,0) and (16,3): both have the
# priority bit on the play HUD only (the intro has priority cells in rows 0-3 too, but not
# at (16,3)).
asm 003D8 5   ; LD HL,$C4C0 : INC (HL) : LD A,(HL) -> far call, then return
    rst $00
    db far_io, pg_sat_rot, ent_sat_rot
    ret
endasm
asm 00A87 7   ; XOR A : LD ($C5BE),A : LD HL,$7F00 -> far call, then return
    rst $00
    db far_io, pg_sat_rot, ent_sat_flat
    ret
endasm
asm 00A9F 7   ; XOR A : LD ($C5BE),A : LD HL,$7F00 -> far call, then return
    rst $00
    db far_io, pg_sat_rot, ent_sat_rev
    ret
endasm
# The tile writer at $068A (B tiles of 32 bytes from DE to the VDP address in HL, called at
# $069F and $07C8) is a 32-OUTI run for each tile, about 5,600 cycles a tile. Page 0 writes
# them with one jt_vwrite call.
asm 0068A 11  ; RST $18 : EX DE,HL : LD D,B : CALL $05BE : DEC D : JP NZ,$068D : RET -> far call
    rst $00
    db far_io, pg_sat_rot, ent_tiles
    ret
endasm
# The animated tile writer at $316D maps bank 15 and writes 4 to 10 tiles at VRAM $0000 from
# the pointers at $C5A6, a 32-OUTI run for each tile. In play it runs in the frame interrupt
# every 4 or 8 frames, with the display off. Page 0 writes each tile with one jt_vwrite call.
asm 03177 6   ; LD A,B : LD DE,$4000 : LD C,$BF (after the bank 15 store) -> far call
    rst $00
    db far_io, pg_sat_rot, ent_anim
    ret
endasm
page 0 sat_rot sat_flat sat_rev tiles anim
; The game's sprite buffer: Y bytes at $C300 (64), X and tile pairs at $C340 (128).
; sat_rot ($03D8, other screens): $C4C0 += 1, k = $C4C0 AND 7; Y from entry 8k on, X and tile
;   from entry 8k on, both round to the start (the paths at $03F4-$04D4). The game's path 0
;   also calls the delay at $000F twice; that is left out.
; sat_flat ($0A87, play): entries in order.
; sat_rev ($0A9F, play): entries $C5F3-1 down to 0, then $C5F4-1 down to $C5F3; Y $C0 for
;   the slots after them; X and tile only for the first $C5F4 slots.
; Each clears $C5BE as the game's routines do, and returns A = 0, C = $BE (the game's code
; after these reloads A and sets C, B, DE and HL before use) and keep IX and IY. Interrupts
; stay off: the game calls them from its frame interrupt.
sat_rot:
        ld hl,$C4C0
        inc (hl)
        ld a,(hl)
        and 7
        add a,a
        add a,a
        add a,a                 ; A = 8k, the first entry
        ld b,a
        ld c,64
        ld de,ybuf
        ld l,b
        ld h,$C3                ; HL = $C300 + 8k
        push bc
.y:     ld a,(hl)
        ld (de),a
        inc de
        inc l
        ld a,l
        cp $40
        jr c,.yn
        ld l,0                  ; round to entry 0
.yn:    dec c
        jr nz,.y
        pop bc
        ld a,b
        add a,a
        add a,$40
        ld l,a                  ; HL = $C340 + 16k
        ld de,xbuf
        ld c,128
.x:     ld a,(hl)
        ld (de),a
        inc de
        inc l
        ld a,l
        cp $C0
        jr c,.xn
        ld l,$40
.xn:    dec c
        jr nz,.x
        ld b,128
        jp put
sat_flat:
        ld hl,$C300
        ld de,ybuf
        ld bc,64
        ldir
        ld hl,$C340
        ld de,xbuf
        ld bc,128
        ldir
        ld b,128
        jp put
sat_rev:
        ld a,($C5F4)
        cp 65
        jr c,.n4
        ld a,64
.n4:    ld (n4),a
        ld a,($C5F3)
        ld hl,n4
        cp (hl)
        jr c,.n3
        ld a,(hl)
.n3:    ld (n3),a
        ld de,ybuf              ; Y: entries n3-1 .. 0, then n4-1 .. n3, then $C0
        ld ix,xbuf
        ld c,0                  ; C = the first entry of the run
        ld b,a                  ; B = entries in the run
        call .run
        ld a,(n3)
        ld c,a
        ld a,(n4)
        sub c
        ld b,a
        call .run
        ld a,(n4)
        sub 64
        neg
        jr z,.pad0
        ld b,a
        ld a,$C0
.pad:   ld (de),a
        inc de
        djnz .pad
.pad0:  ld a,(n4)
        add a,a
        ld b,a                  ; X and tile: 2 * n4 bytes (0 = none)
        jr put
; B entries from C+B-1 down to C: Y to (DE), X and tile to (IX)
.run:   ld a,b
        or a
        ret z
.r:     ld a,c
        add a,b
        dec a                   ; the entry
        ld l,a
        ld h,$C3
        ld a,(hl)
        ld (de),a
        inc de
        ld a,l
        add a,a
        add a,$40
        ld l,a                  ; $C340 + 2 * entry
        ld a,(hl)
        ld (ix+0),a
        inc l
        ld a,(hl)
        ld (ix+1),a
        inc ix
        inc ix
        djnz .r
        ret
; ybuf holds 64 Y bytes, xbuf B bytes of X and tile (B = 0: none). Hide the sprites under
; the HUD when it is up, then write $3F00 and $3F80.
put:    push ix
        push iy
        push bc
        call hud
        jr nz,.w
        ld hl,ybuf
        ld b,64
.f:     ld a,(hl)
        cp $1A
        jr c,.h
        cp $E0
        jr c,.k
.h:     ld (hl),$C0
.k:     inc hl
        djnz .f
.w:     ld hl,ybuf
        ld de,$3F00
        ld bc,$4001             ; 64 bytes, one run
        ld ix,64
        ld iy,64
        ld a,1                  ; the source as mapped: this page
        call jt_vwrite
        pop bc
        ld a,b
        or a
        jr z,.e
        ld hl,xbuf
        ld de,$3F80
        ld c,1
        ld ix,128
        ld iy,128
        ld a,1
        call jt_vwrite
.e:     pop iy
        pop ix
        xor a
        ld ($C5BE),a
        ld c,$BE
        ret
; Z when name table cells (0,0) and (16,3) both have the priority bit: the play HUD.
; VDP reads through the io vector: OUT ($BF),A is code $05, IN A,($BE) code $0C.
hud:    ld a,$01
        rst $00
        db $05
        ld a,$38                ; read $3801
        rst $00
        db $05
        rst $00
        db $0C
        and $10
        xor $10
        ret nz
        ld a,$E1
        rst $00
        db $05
        ld a,$38                ; read $38E1
        rst $00
        db $05
        rst $00
        db $0C
        and $10
        xor $10
        ret
; tiles ($068A): HL = VDP address (a VRAM write, or CRAM with bits 14-15 set), DE = the
; source, B = tiles (0 = 256). Returns as the game's routine does: A kept, B = B - 32 * tiles,
; C = $BE, D = 0, E = the address's low byte, HL = the source past the last tile, Z set.
tiles:  ld (.a),a
        ld a,b
        ld (.n),a
        ld a,h
        and $C0
        cp $C0
        jr z,.cram
        push ix
        push iy
        push de
        push hl
        ld c,b                  ; one run of 32 bytes a tile
        ex de,hl                ; HL = the source, DE = the VRAM address
        ld b,32
        ld ix,32
        ld iy,32
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop hl
        pop de
        pop iy
        pop ix
        jr .ret
.cram:  push hl                 ; CRAM: the address, then 32 bytes a tile through OTIR
        push de
        ld a,l
        rst $00
        db $05
        ld a,h
        rst $00
        db $05
        ex de,hl                ; HL = the source
        ld a,(.n)
        ld d,a
.ct:    push hl
        ld bc,$20BE
        rst $00
        db $B3
        pop hl
        ld bc,32
        add hl,bc
        dec d
        jr nz,.ct
        pop de
        pop hl
.ret:   ld a,(.n)               ; HL = the source + 32 * tiles, E = the address's low byte
        ld c,a
        ld b,0
        or a
        jr nz,.r1
        inc b                   ; 256 tiles
.r1:    ld a,l
        ex de,hl                ; HL = the source, E = the address's low byte
        ld e,a
        ld a,5
.r2:    sla c
        rl b
        dec a
        jr nz,.r2
        add hl,bc
        ld a,(.n)               ; B = tiles - 32 * tiles
        ld b,a
        add a,a
        add a,a
        add a,a
        add a,a
        add a,a
        neg
        add a,b
        ld b,a
        ld c,$BE
        ld d,0
        ld a,(.a)
        cp a                    ; Z
        ret
.a:     db 0
.n:     db 0
; anim ($3177): B = the count the game gives. The game's code writes 4 tiles, and then more up
; to the count, 10 at most: 4 for a count of 4, the count for 5-10, else 10. Tile i comes
; from the pointer at $C5A6 + 2i (bank 15 is mapped) and goes to VRAM $0000 + 32i. Returns
; A = 0, C = $BE (the game's code after it sets A and B before use), IX and IY kept.
anim:   ld a,b
        cp 4
        jr z,.n4
        jr c,.n10
        cp 11
        jr c,.nn
.n10:   ld a,10
        jr .nn
.n4:    ld a,4
.nn:    ld (.c),a
        push ix
        push iy
        ld hl,$C5A6
        ld de,$0000
.t:     push hl
        ld a,(hl)
        inc hl
        ld h,(hl)
        ld l,a                  ; HL = the tile's source
        ld bc,$2001             ; one run of 32 bytes
        ld ix,32
        ld iy,32
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop hl
        inc hl
        inc hl
        ex de,hl
        ld bc,32
        add hl,bc
        ex de,hl
        ld a,(.c)
        dec a
        ld (.c),a
        jr nz,.t
        pop iy
        pop ix
        xor a
        ld c,$BE
        ret
.c:     db 0
n3:     db 0
n4:     db 0
ybuf:   ds 64
xbuf:   ds 128
endpage
start 0003
site 0001A   ; OUT (C),L
site 0001C   ; OUT (C),H
site 0003A   ; IN A,($BF)
site 00129   ; IN A,(C)
site 00130   ; OUT ($BF),A
site 00134   ; OUT ($BF),A
site 0034B   ; OUT ($BF),A
site 0034F   ; OUT ($BF),A
site 00352   ; IN A,($BF)
site 0035F   ; IN A,($DC)
site 0037C   ; IN A,($DD)
site 003A4   ; IN A,($BF)
site 003AF   ; OUT ($BF),A
site 003B2   ; OUT ($BF),A
site 003BF   ; OUT ($BE),A
site 004FE   ; OUTI
site 00500   ; OUTI
site 00502   ; OUTI
site 00504   ; OUTI
site 00506   ; OUTI
site 00508   ; OUTI
site 0050A   ; OUTI
site 0050C   ; OUTI
site 0050E   ; OUTI
site 00510   ; OUTI
site 00512   ; OUTI
site 00514   ; OUTI
site 00516   ; OUTI
site 00518   ; OUTI
site 0051A   ; OUTI
site 0051C   ; OUTI
site 0051E   ; OUTI
site 00520   ; OUTI
site 00522   ; OUTI
site 00524   ; OUTI
site 00526   ; OUTI
site 00528   ; OUTI
site 0052A   ; OUTI
site 0052C   ; OUTI
site 0052E   ; OUTI
site 00530   ; OUTI
site 00532   ; OUTI
site 00534   ; OUTI
site 00536   ; OUTI
site 00538   ; OUTI
site 0053A   ; OUTI
site 0053C   ; OUTI
site 0053E   ; OUTI
site 00540   ; OUTI
site 00542   ; OUTI
site 00544   ; OUTI
site 00546   ; OUTI
site 00548   ; OUTI
site 0054A   ; OUTI
site 0054C   ; OUTI
site 0054E   ; OUTI
site 00550   ; OUTI
site 00552   ; OUTI
site 00554   ; OUTI
site 00556   ; OUTI
site 00558   ; OUTI
site 0055A   ; OUTI
site 0055C   ; OUTI
site 0055E   ; OUTI
site 00560   ; OUTI
site 00562   ; OUTI
site 00564   ; OUTI
site 00566   ; OUTI
site 00568   ; OUTI
site 0056A   ; OUTI
site 0056C   ; OUTI
site 0056E   ; OUTI
site 00570   ; OUTI
site 00572   ; OUTI
site 00574   ; OUTI
site 00576   ; OUTI
site 00578   ; OUTI
site 0057A   ; OUTI
site 0057C   ; OUTI
site 0057E   ; OUTI
site 00580   ; OUTI
site 00582   ; OUTI
site 00584   ; OUTI
site 00586   ; OUTI
site 00588   ; OUTI
site 0058A   ; OUTI
site 0058C   ; OUTI
site 0058E   ; OUTI
site 00590   ; OUTI
site 00592   ; OUTI
site 00594   ; OUTI
site 00596   ; OUTI
site 00598   ; OUTI
site 0059A   ; OUTI
site 0059C   ; OUTI
site 0059E   ; OUTI
site 005A0   ; OUTI
site 005A2   ; OUTI
site 005A4   ; OUTI
site 005A6   ; OUTI
site 005A8   ; OUTI
site 005AA   ; OUTI
site 005AC   ; OUTI
site 005AE   ; OUTI
site 005B0   ; OUTI
site 005B2   ; OUTI
site 005B4   ; OUTI
site 005B6   ; OUTI
site 005B8   ; OUTI
site 005BA   ; OUTI
site 005BC   ; OUTI
site 005BE   ; OUTI
site 005C0   ; OUTI
site 005C2   ; OUTI
site 005C4   ; OUTI
site 005C6   ; OUTI
site 005C8   ; OUTI
site 005CA   ; OUTI
site 005CC   ; OUTI
site 005CE   ; OUTI
site 005D0   ; OUTI
site 005D2   ; OUTI
site 005D4   ; OUTI
site 005D6   ; OUTI
site 005D8   ; OUTI
site 005DA   ; OUTI
site 005DC   ; OUTI
site 005DE   ; OUTI
site 005E0   ; OUTI
site 005E2   ; OUTI
site 005E4   ; OUTI
site 005E6   ; OUTI
site 005E8   ; OUTI
site 005EA   ; OUTI
site 005EC   ; OUTI
site 005EE   ; OUTI
site 005F0   ; OUTI
site 005F2   ; OUTI
site 005F4   ; OUTI
site 005F6   ; OUTI
site 005F8   ; OUTI
site 005FA   ; OUTI
site 005FC   ; OUTI
site 00605   ; OTIR
site 00617   ; OUT ($BE),A
site 0061D   ; OUT ($BE),A
site 00631   ; OUT ($BE),A
site 00634   ; OUT ($BE),A
site 00649   ; OUTI
site 0064E   ; OUT ($BE),A
site 00660   ; OUT (C),E
site 00662   ; OUT (C),D
site 00673   ; OUT (C),E
site 00679   ; OUT (C),D
site 006D6   ; OUT ($BE),A
site 00941   ; OUT ($BF),A
site 00945   ; OUT ($BF),A
site 00947   ; IN A,($DD)
site 00969   ; OUT ($BF),A
site 0096D   ; OUT ($BF),A
site 0099E   ; OUT ($BF),A
site 009A2   ; OUT ($BF),A
site 009EE   ; OUT ($BE),A
site 00A1A   ; OUT ($BE),A
site 00AB7   ; OTDR
site 00AC7   ; OTDR
site 00AD4   ; OUT ($BE),A
site 00AED   ; OUTI
site 00AEF   ; OUTD
site 00B08   ; OUTI
site 00B0A   ; OUTD
site 00BF1   ; OUT ($BE),A
site 00BF9   ; OUT ($BE),A
site 00CA1   ; OUT ($BF),A
site 00CA5   ; OUT ($BF),A
site 00CBC   ; OUT ($BF),A
site 00CBF   ; OUT ($BF),A
site 00CC3   ; OUT ($BE),A
site 00CCC   ; OUT ($BE),A
site 01283   ; OUT (C),E
site 01285   ; OUT (C),D
site 0128B   ; OUT ($BE),A
site 01295   ; OUT ($BE),A
site 0129B   ; OUT ($BE),A
site 012A5   ; OUT ($BE),A
site 012AB   ; OUT ($BE),A
site 012B5   ; OUT ($BE),A
site 012BB   ; OUT ($BE),A
site 012C5   ; OUT ($BE),A
site 01874   ; OUT (C),A
site 0195C   ; OUT (C),A
site 01964   ; OUT (C),A
site 0317D   ; OUT (C),E
site 0317F   ; OUT (C),D
site 04A14   ; OUT ($BE),A
site 04A1B   ; OUT ($BE),A
site 04D0C   ; OUT (C),E
site 04D0E   ; OUT (C),D
site 04D13   ; OUT (C),A
site 04E86   ; IN A,(C)
site 04E89   ; IN A,(C)
site 05040   ; OUT ($BE),A
site 05047   ; OUT ($BE),A
site 05052   ; OUT ($BE),A
site 05059   ; OUT ($BE),A
site 0C2BD   ; OUT (C),A
site 0C2C0   ; OUT (C),A
site 0C335   ; OUT (C),A
site 0C337   ; OUT (C),B
site 0C373   ; OUT (C),A
site 0C375   ; OUT (C),B
site 0C3A7   ; OUT (C),A
site 0C3A9   ; OUT (C),B
site 0C3BB   ; OUT (C),A
site 0C3BD   ; OUT (C),B
site 0C3F2   ; OUT (C),A
site 0C3F4   ; OUT (C),B
site 0C406   ; OUT (C),A
site 0C408   ; OUT (C),B
site 0CB63   ; OUT ($BE),A
site 0CB6A   ; OUT ($BE),A
site 0CDE2   ; OUT (C),A
site 0CDE8   ; OUT (C),B
site 0CDED   ; OUT (C),A
site 0CDEF   ; OUT (C),B
site 0CEEC   ; OUT (C),A
site 0CEF2   ; OUT (C),A
site 0CEFC   ; OUT (C),A
site 0CF02   ; OUT (C),A
site 0F9D1   ; OUT ($3F),A
site 0F9D3   ; IN A,($DD)
site 0F9DD   ; OUT ($3F),A
site 0F9DF   ; IN A,($DD)
site 0FA31   ; OUT ($3E),A
site 0FA34   ; OUT ($F2),A
site 0FA3C   ; OUT ($3E),A
site 0FA40   ; OUT ($3F),A
site 0FA48   ; IN A,($BF)
site 0FA4A   ; IN A,($BF)
site 0FA56   ; IN A,($BF)
site 15FF4   ; OUT (C),A
site 15FF8   ; OUT (C),A
site 16026   ; OUT (C),A
site 1602B   ; OUT (C),B
site 16031   ; OUT (C),A
site 16035   ; OUT (C),B
site 181D5   ; OUT ($7F),A
site 183B8   ; OTIR
site 184CE   ; OUT ($7F),A
site 184D8   ; OUT ($7F),A
site 184F5   ; OUT ($7F),A
site 185F9   ; OUT ($7F),A
site 18685   ; OUT ($7F),A
site 1874B   ; OUT ($7F),A
site 18754   ; OUT ($7F),A
site 18764   ; OUT ($7F),A
site 187D8   ; OUT ($7F),A
site 1892C   ; OUT ($7F),A
site 18930   ; OUT ($7F),A
site 18955   ; OUT ($7F),A
mapldk 00136   # LD HL,$FFFC; LD (HL),$00
maphl 0013C   # LD (HL),$00, HL = $FFFD
maphl 0013F   # LD (HL),$01, HL = $FFFE
maphl 00142   # LD (HL),$02, HL = $FFFF
mapst 0015D   ; LD ($FFFF),A
mapst 0018F   ; LD ($FFFF),A
mapst 00196   ; LD ($FFFF),A
mapst 001CD   ; LD ($FFFF),A
mapst 001EA   ; LD ($FFFF),A
mapst 00201   ; LD ($FFFF),A
mapst 006A3   ; LD ($FFFF),A
mapst 006B4   ; LD ($FFFF),A
mapst 006DF   ; LD ($FFFF),A
mapst 006F2   ; LD ($FFFF),A
mapst 0075E   ; LD ($FFFF),A
mapst 007BA   ; LD ($FFFF),A
mapst 00974   ; LD ($FFFF),A
mapst 009A6   ; LD ($FFFF),A
mapst 00FDC   ; LD ($FFFF),A
mapst 01008   ; LD ($FFFF),A
mapst 01013   ; LD ($FFFF),A
mapst 01040   ; LD ($FFFF),A
mapst 0104B   ; LD ($FFFF),A
mapst 0107B   ; LD ($FFFF),A
mapst 01151   ; LD ($FFFF),A
mapst 0116A   ; LD ($FFFF),A
mapst 01869   ; LD ($FFFF),A
mapst 01883   ; LD ($FFFF),A
mapst 022E5   ; LD ($FFFF),A
mapst 02300   ; LD ($FFFF),A
mapst 0265E   ; LD ($FFFF),A
mapst 03174   ; LD ($FFFF),A

# Bonanza Bros. (Europe, Brazil).cht, "Infinite Lives": RAM $C4E1 is the life count, the
# lives shown are one less
poke "Infinite lives"
ar 00C4-E10A
endpoke

# Bonanza Bros. (Europe, Brazil).cht, "Infinite Time - One's Digit": RAM $C585 is the
# ones digit of the seconds. Held at 9, it never reaches 0, so the clock never runs out.
poke "Infinite time"
ar 00C5-8509
endpoke

# Bonanza Bros. (Europe, Brazil).cht, "Infinite Continues (Credits)": RAM $C4E2 is the
# number of continues
poke "Infinite continues"
ar 00C4-E209
endpoke

# Bonanza Bros. (Europe, Brazil).cht, "Enable Stage Select in Options Menu": RAM $C41E set
# to $FF adds a STAGE row to the Options screen
poke "Stage select"
ar 00C4-1EFF
endpoke
