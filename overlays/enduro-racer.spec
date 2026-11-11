# Enduro Racer (USA, Europe, Brazil) (En), CRC32 00E73541, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - The byte scan rows at $0232 and $0264 are in the VDP routines $020D, $023C and
#   $0248 ($020D-$026B), and the row at $312F is in the PSG routine $312D: no call, jump
#   or table in the cart names their starts (verdict unused).
# - The other byte scan rows (banks 1, 2, 3, 5 and 7) are graphics and tables (verdict
#   false). Banks 2-7 hold data only: the bank writes at $0753 and $17B7 take their
#   bank from the tables at $07B1 and $07BB, which give data sources, never a call.
# - The indirect jump at $08B8 is the object dispatcher (the list at $C400); its
#   handlers come from the object tables the scanner reads.
# - The race's frame handler sends the bike's tiles to VRAM through $016A (384 or 704
#   bytes from $133D and $1378) and scrolls with the row writer $171C and the column
#   writer $1746 ($1649). Through single traps these took up to 1.7 Next frames, and the
#   game lost one step in four. The copy loop of $016A is a cave with the runtime's OTIR,
#   and $171C and $1746 are page code that writes VRAM with jt_vwrite (the page uses no
#   other runtime entry).
# - The frame handler writes the sprite table in the forward order on even frames and in
#   the reverse order on odd ones ($02A6-$02F6), to share the Master System's 8 sprites a
#   line. The Next has no such limit, and with the reverse order the TIME display (the
#   sprite table's first entries) was missing or cut in about one odd frame in ten. The
#   JR NZ at $02AC is gone, so the table always goes in the forward order; where two
#   sprites overlap, the same one is always in front.
name Enduro Racer
cart 00E73541
hz any		; No-Intro regions USA, Europe, Brazil
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 000C0   ; IN A,($BF)
site 000F9   ; IN A,($DD)
site 00155   ; OUT ($BF),A
site 00158   ; OUT ($BF),A
site 00160   ; OUT ($BE),A
site 00164   ; OUT ($BF),A
site 00167   ; OUT ($BF),A
asm 00176 11   ; the VRAM copy loop of $016A: OUTI; PUSH AF; POP AF; JP NZ (B bytes), A times
.lp:    rst $00          ; OTIR through the runtime: B bytes from HL to port C ($BE)
        db $B3
        dec a
        jr nz,.lp
        ret
endasm
site 001A8   ; OUT ($BE),A
site 001AD   ; OUT ($BE),A
site 001BC   ; OUTI
site 001C2   ; OUT (C),A
site 001D9   ; OUTI
site 00200   ; OUT (C),D
site 0028A   ; OUT ($BE),A
site 002B1   ; OUTI
site 002C1   ; OUTI
site 002C3   ; OUTI
site 002D7   ; OUTD
site 002DE   ; OUT ($BE),A
site 002ED   ; OUTI
site 002EF   ; OUTD
site 002FD   ; OTIR
site 00321   ; OUT ($3F),A
site 00323   ; IN A,($DD)
site 0032D   ; OUT ($3F),A
site 0032F   ; IN A,($DD)
site 00338   ; OUT ($3F),A
site 00368   ; IN A,($DC)
site 00389   ; IN A,($DC)
site 01294   ; OUT ($BE),A
site 02C5D   ; OUT ($7F),A
site 02D37   ; OUT ($7F),A
site 02D3F   ; OUT ($7F),A
site 02D4A   ; OUT ($7F),A
site 030B4   ; OUT ($7F),A
site 0310E   ; OUT ($7F),A
site 03128   ; OTIR
site 03134   ; OUT ($7F),A
site 03138   ; OUT ($7F),A
site 0442F   ; OUT ($BE),A
site 04434   ; OUT ($BE),A
site 04668   ; OUT ($BE),A
site 0466E   ; OUT ($BE),A
site 046CA   ; OUT ($BE),A
site 046D1   ; OUT ($BE),A
site 046D7   ; OUT ($BE),A
site 046DD   ; OUT ($BE),A
site 047C7   ; OUT ($BE),A
site 047CE   ; OUT ($BE),A
site 047D7   ; OUT ($BE),A
site 047DE   ; OUT ($BE),A
site 047F0   ; OUT ($BE),A
site 047F7   ; OUT ($BE),A
site 047FD   ; OUT ($BE),A
site 04804   ; OUT ($BE),A
site 04817   ; OUT ($BE),A
site 0481E   ; OUT ($BE),A
site 04A74   ; OUT ($BE),A
site 04A79   ; OUT ($BE),A
site 04A8B   ; OUT ($BE),A
site 04A91   ; OUT ($BE),A
site 051A8   ; OUT ($BE),A
site 051AE   ; OUT ($BE),A
mapst 00398   ; LD ($FFFF),A
mapst 005B4   ; LD ($FFFF),A
mapst 00753   ; LD ($FFFF),A
mapst 00788   ; LD ($FFFF),A
mapst 01344   ; LD ($FFFF),A
mapst 01387   ; LD ($FFFF),A
mapst 017B7   ; LD ($FFFF),A
mapst 04326   ; LD ($FFFF),A
mapst 04334   ; LD ($FFFF),A
mapst 04447   ; LD ($FFFF),A
mapst 0452F   ; LD ($FFFF),A
mapst 0453D   ; LD ($FFFF),A
mapst 04AB0   ; LD ($FFFF),A
mapst 050B0   ; LD ($FFFF),A
asm 002AC 2   ; JR NZ,$02CA: the sprite table always goes in the forward order
        nop
        nop
endasm
asm 0171C 5   ; LD A,($C314); AND $1F: the start of the name table row writer $171C
        rst $00
        db far_io, pg_row, ent_row
        ret
endasm
asm 01746 5   ; LD A,$20; LD ($C312),A: the start of the name table column writer $1746
        rst $00
        db far_io, pg_col, ent_col
        ret
endasm
page 0 row col
; row: does what the game's $171C does. HL = the source of a name table row of 32 cells,
; DE = the VRAM address of cell ($C314) AND $1F of the row. The cells from there to the
; row's end go first, then the rest from the row's start ($C306), each run in one
; jt_vwrite call. Returns B = 0, HL and DE after the last bytes written.
row:    push ix
        push iy
        ld ix,64                ; defined steps (one run each call)
        ld iy,64
        ld a,($C314)
        and $1F
        ld c,a
        ld a,$20
        sub c
        ld c,a                  ; C = the cells up to the row's end, 1 to 32
        add a,a
        ld b,a                  ; their bytes
        call .run
        ld a,$20
        sub c                   ; the cells before the start cell
        jr z,.done
        add a,a
        ld b,a
        ld de,($C306)           ; the row's start
        call .run
.done:  ld b,0
        pop iy
        pop ix
        ret
; .run: B bytes from HL to VRAM DE; HL and DE step past them. Keeps C.
.run:   push bc
        ld c,1
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop bc
        ld a,b
        add a,l
        ld l,a
        adc a,h
        sub l
        ld h,a
        ld a,b
        add a,e
        ld e,a
        adc a,d
        sub e
        ld d,a
        ret

; col: does what the game's $1746 does: ($C312) = $20, then the 27 cells of a name table
; column, 2 bytes each, from the ring buffer $D300-$DF3F (row step $72) to VRAM from
; ($C308) + $40 down (row step $40, the name table wraps from $7F00 to $7800). One
; jt_vwrite call a row. Returns B = 0, HL = the next source, DE = the next VRAM address.
col:    ld a,$20
        ld ($C312),a
        ld hl,($C308)
        ld de,$0040
        add hl,de
        ld de,$7F00
        sbc hl,de
        jr c,.c1
        ld hl,$7800
        jr .c2
.c1:    add hl,de
.c2:    ld b,$1B
        ld a,($C300)
        neg
        and $F8
        rrca
        rrca
        ld e,a
        ld d,$00
        add hl,de
        push hl
        ld hl,($C30A)
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld e,l
        ld d,h
        add hl,hl
        add hl,hl
        add hl,hl
        sbc hl,de
        ld de,$D300
        add hl,de
        ld de,$0040
        add hl,de
        pop de
        push ix
        push iy
        ld ix,$72               ; defined steps (one run each call)
        ld iy,$40
.lp:    push bc
        ld bc,$0201             ; one run of 2 bytes
        xor a
        call jt_vwrite
        pop bc
        inc hl                  ; the next source row, as the game steps it
        push de
        ld de,$0071
        add hl,de
        ld de,$DF40
        sbc hl,de
        jr c,.s1
        ld de,$D300
.s1:    add hl,de
        pop de
        push hl                 ; the next VRAM row
        ld hl,$0040
        add hl,de
        ld a,h
        cp $7F
        jr nz,.s2
        ld h,$78
.s2:    ex de,hl
        pop hl
        djnz .lp
        pop iy
        pop ix
        ret
endpage

# Enduro Racer _ Super Cross (USA, Europe, Brazil).cht, "Invincible": RAM $C416 is the hit
# timer; held at 1 a crash into a rock no longer explodes the bike
poke "Invincible"
ar 00C4-1601
endpoke

# Enduro Racer _ Super Cross (USA, Europe, Brazil).cht, "Infinite Time": RAM $C392 is the
# time left, in BCD seconds; $60 is a full clock
poke "Infinite time"
ar 00C3-9260
endpoke

# Enduro Racer _ Super Cross (USA, Europe, Brazil).cht, "Have No Damage": RAM $C396 is the
# damage meter (the D= value); the code holds it at 0
poke "No damage"
ar 00C3-9600
endpoke

# Enduro Racer _ Super Cross (USA, Europe, Brazil).cht, "Infinite Points": RAM $C39A is the
# points for the tune-up screen, in BCD; the screen shows 99PTS.
poke "Max points"
ar 00C3-9A99
endpoke

# Enduro Racer _ Super Cross (USA, Europe, Brazil).cht, "Enable Track Select on Title
# Screen": RAM $C373 = 4 shows the track number on the title screen, and Up or Down picks it
poke "Track select"
ar 00C3-7304
endpoke
