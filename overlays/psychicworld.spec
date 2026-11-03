# Psychic World (Europe, Brazil) (En), CRC32 5C0B1F0F, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input), plus these routine starts given with --entry, because no scanned path
# or recording reached them:
# - the game modes of the main loop's table at $0287 (bank, address): bank 3 $8000,
#   $8004, $8008; bank 5 $8000, $8004, $8008, $800C; bank 0 $02B1, $02CC, $0E49, $1127,
#   $11CC;
# - the round effect routines of the table at $5489 (the frame code calls them through
#   $DFE5 at $53B4): bank 1 $554A, $5838, $5D68, $5F5E, $6529, $6571, $6748, $6789,
#   $67A2, $67E9, $6815;
# - the object handlers of the table at $9BB5 in bank 2 (slot 2 holds bank 2 in play),
#   dispatched at $5338, and the handler states of the tables at $5FF4 (bank 1) and
#   $B83B (bank 5).
# Decisions:
# - No free RST vector, so $0000 is the io vector.
# - The frame handler ($02CD) turns the display off, uploads the sprite table and the
#   palette, runs a task, sets the H scroll and turns the display on. On the Next it
#   turns the display on again in the picture, and the play area showed black from its
#   top down to as far as the status bar in about half of the frames. toppal holds the
#   display-off write, so the picture stays whole.
# - A line interrupt at the status bar sets H scroll 0 ($0E27), so hsplit is on:
#   without it the right edge of the status bar showed the radar box's colours while
#   the play area scrolled.
# - Page 0, entry pal32, replaces the palette upload $0505-$050F, 32 CRAM writes every
#   frame through the OUTI run at $0550: it writes only the entries whose colour
#   differs from cram. It uses the runtime's cram and VDP state variables.
# - The status bar (name table rows 16-23, but for the radar box) has the priority bit,
#   so priority is on.
# - Page 0, entries bar_hp, bar_esp, bar_hp0 and bar_esp0, draw the H.P. and ESP bars.
#   The game draws a whole bar, 20 priority cells, each time its value changes ($2948,
#   $29A2; a hit takes 4 H.P.), and the runtime then draws all 20 again in Layer 2.
#   When that came in the frame of the play area's column update ($0E2D), the frame
#   handler's H scroll write came at line 152, below the status bar split at line 130:
#   the status bar lines below it showed the play area's scroll for a frame, and its
#   right edge the radar box's colours in the next one. bar_hp and bar_esp write only
#   the cells that differ between the bar's old value and its new one. The round start
#   ($28C9) draws the status bar from its image and then each bar whole ($28FF, $2907):
#   bar_hp0 and bar_esp0 write all its cells there.
# - The CHECK rows of the draft are not patched: the LD (BC),A rows in bank 4 write
#   ROM, the RAM calls at $896E and $8974 are bank 4 data read as code, and the bytes
#   at $1ACCB (bank 6) and $2364B (bank 8) are graphics (verdict false).
name Psychic World
cart 5C0B1F0F
hz 50		; No-Intro regions Europe, Brazil
priority
toppal
hsplit
vector 00 io
start 0003
site 0001A   ; OUT (C),L
site 0001C   ; OUT (C),H
site 00149   ; IN A,(C)
site 0014E   ; OUT (C),H
site 00150   ; OUT (C),L
site 002CD   ; IN A,($BF)
site 002DC   ; OUT ($BF),A
site 002E0   ; OUT ($BF),A
site 00302   ; OUT ($BF),A
site 00306   ; OUT ($BF),A
site 0030D   ; OUT ($BF),A
site 00311   ; OUT ($BF),A
site 00379   ; OUT ($BF),A
site 0037D   ; OUT ($BF),A
site 00392   ; IN A,($DD)
site 00397   ; IN A,($BF)
site 0041A   ; OUT ($BF),A
site 0041E   ; OUT ($BF),A
site 00432   ; OUT ($BF),A
site 00436   ; OUT ($BF),A
site 00439   ; IN A,($DC)
site 00456   ; IN A,($DD)
site 0047B   ; IN A,($BF)
site 00486   ; OUT ($BF),A
site 00489   ; OUT ($BF),A
site 0048F   ; OUT ($BE),A
site 00499   ; OUT ($BE),A
site 004E8   ; OUTD
site 004FC   ; OUTI
site 004FE   ; OUTD
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
site 00599   ; OUT ($BE),A
site 0059C   ; OUT ($BE),A
site 005AF   ; OTIR
site 005C0   ; OUT ($BE),A
site 005C5   ; OUT ($BE),A
site 005DE   ; OUT ($BE),A
site 005E5   ; OUT ($BE),A
site 005FD   ; OUT ($BE),A
site 00600   ; OUT ($BE),A
site 00616   ; OUT (C),D
site 0061C   ; OUT (C),A
site 00883   ; OUT (C),B
site 008C0   ; OUT ($BE),A
site 008EB   ; OUT (C),A
site 00D31   ; OUT ($BE),A
site 00D3A   ; OUT ($BE),A
site 00E37   ; OUTI
site 00E39   ; OUTI
site 02C30   ; OUT (C),A
site 02C3E   ; OUT (C),A
site 02C4C   ; OUT (C),A
site 02C5A   ; OUT (C),A
site 02C68   ; OUT (C),A
site 02C76   ; OUT (C),A
site 03B9F   ; OUT (C),A
site 03BA5   ; OUT (C),A
site 0554D   ; OUT ($BF),A
site 05551   ; OUT ($BF),A
site 060A4   ; OUT (C),A
site 060AF   ; OUT (C),A
site 06123   ; OUT (C),A
site 0612E   ; OUT (C),A
site 0997E   ; OUT (C),A
site 0C02B   ; OUT ($3F),A
site 0C02D   ; IN A,($DD)
site 0C037   ; OUT ($3F),A
site 0C039   ; IN A,($DD)
site 0C07F   ; OUT ($3E),A
site 0C082   ; OUT ($F2),A
site 0C08A   ; OUT ($3E),A
site 0C08E   ; OUT ($3F),A
site 0C097   ; IN A,($BF)
site 0C099   ; IN A,($BF)
site 0C0A5   ; IN A,($BF)
site 0C0B4   ; OUT ($3F),A
site 0C0B6   ; IN A,($DD)
site 0C0C0   ; OUT ($3F),A
site 0C0C2   ; IN A,($DD)
site 0C0C7   ; OUT ($3F),A
site 10198   ; OUT ($7F),A
site 10269   ; OUT ($7F),A
site 103FB   ; OTIR
site 10511   ; OUT ($7F),A
site 1051B   ; OUT ($7F),A
site 10538   ; OUT ($7F),A
site 1063C   ; OUT ($7F),A
site 106C8   ; OUT ($7F),A
site 1074D   ; OUT ($06),A
site 10797   ; OUT ($7F),A
site 107A0   ; OUT ($7F),A
site 107B0   ; OUT ($7F),A
site 10824   ; OUT ($7F),A
site 14212   ; OUT (C),A
site 1421A   ; OUT (C),A
site 14238   ; OUT (C),A
site 14240   ; OUT (C),A
site 1424F   ; OUT (C),A
site 14255   ; OUT (C),A
site 14266   ; OUT ($BE),A
site 1426E   ; OUT ($BE),A
mapldk 00152   # LD HL,$FFFC; LD (HL),$00
maphl 00158   # LD (HL),$00, HL = $FFFD
maphl 0015B   # LD (HL),$01, HL = $FFFE
maphl 0015E   # LD (HL),$02, HL = $FFFF
mapst 00179   ; LD ($FFFF),A
mapst 001AB   ; LD ($FFFF),A
mapst 001B2   ; LD ($FFFF),A
mapst 002FA   ; LD ($FFFF),A
mapst 0068C   ; LD ($FFFF),A
mapst 006EF   ; LD ($FFFF),A
mapst 00714   ; LD ($FFFF),A
mapst 0071B   ; LD ($FFFF),A
mapst 00858   ; LD ($FFFF),A
mapst 0085F   ; LD ($FFFF),A
mapst 0089D   ; LD ($FFFF),A
mapst 008CE   ; LD ($FFFF),A
mapst 008E2   ; LD ($FFFF),A
mapst 008F9   ; LD ($FFFF),A
mapst 00BBF   ; LD ($FFFF),A
mapst 00C34   ; LD ($FFFF),A
mapst 02C1D   ; LD ($FFFF),A
mapst 02C7C   ; LD ($FFFF),A
mapst 03120   ; LD ($FFFF),A
mapst 040B1   ; LD ($FFFF),A
mapst 0425A   ; LD ($FFFF),A
mapst 042E5   ; LD ($FFFF),A
asm 00505 11  ; palette upload: LD HL,$C000; RST $18; LD HL,$C3C0; CALL $0550; RET
    rst $00
    db far_io, pg_pal32, ent_pal32
    ret
endasm
asm 02948 5   ; H.P. bar draw: LD (HL),A; LD HL,$7CEA; SUB 8 (the loop at $294C is not reached)
    rst $00
    db far_io, pg_bar_hp, ent_bar_hp
    ret
endasm
asm 029A2 5   ; ESP bar draw: LD (HL),A; LD HL,$7C6A; SUB 8 (the loop at $29A6 is not reached)
    rst $00
    db far_io, pg_bar_esp, ent_bar_esp
    ret
endasm
asm 028FF 5   ; round start, H.P. bar: LD A,(HL); INC HL; CALL $2948
    rst $00
    db far_io, pg_bar_hp0, ent_bar_hp0
    nop
endasm
asm 02907 5   ; round start, ESP bar: LD A,(HL); INC HL; CALL $29A2
    rst $00
    db far_io, pg_bar_esp0, ent_bar_esp0
    nop
endasm
page 0 pal32 bar_hp bar_esp bar_hp0 bar_esp0
; pal32: as the game's $0505-$050F, the 32 bytes at $C3C0 to CRAM 0-31.
; Writes only the entries whose colour differs from cram; the VDP state is then
; as the 32 writes leave it. Changes A, BC, DE, HL, F.
pal32:  ld hl,$C3C0
        ld c,0
        ld b,32
; HL = the source, C = the first CRAM index, B = the entries. Each entry
; whose colour (low 6 bits) differs from cram gets the VDP address and a
; write through the I/O RST; then the VDP state is as B writes from index C
; leave it: address C + B, code 3, latch clear, read buffer the last byte.
cram_upd:
        ld de,cram
        ld a,e
        add a,c
        ld e,a                  ; cram is inside one 256-byte page
.lp:    ld a,(hl)
        and $3F
        ex de,hl
        cp (hl)
        ex de,hl
        jr z,.same
        ld a,c
        ld (vdp_addr),a
        xor a
        ld (vdp_addr+1),a
        ld (vdp_latch),a
        ld a,3
        ld (vdp_code),a
        ld a,(hl)
        rst $00
        db $04                  ; OUT ($BE),A
.same:  inc hl
        inc de
        inc c
        djnz .lp
        dec hl
        ld a,(hl)
        inc hl
        ld (vdp_rbuf),a
        ld a,c
        ld (vdp_addr),a
        xor a
        ld (vdp_addr+1),a
        ld (vdp_latch),a
        ld a,3
        ld (vdp_code),a
        ret

; The H.P. bar (name table rows 19-20) and the ESP bar (rows 17-18). A bar is 10
; cells from its first cell's address; cell k is 2 by 2 name table entries at the
; address + 2k, and shows tile set clamp(v - 8k, 0, 8) of the bar's table, 4 bytes a
; set (the two entries of the top row, then of the bottom row). The game draws cells 0-9, and past the 10th only the
; cells that are not empty ($2948, $29A2).
; bar_hp, bar_esp: as $2948, $29A2. HL = the value ($DF11, $DF13), still the old one,
; which the bar shows; A = the new one. Stores A at HL and writes only the cells whose
; set differs between the two values.
; bar_hp0, bar_esp0: as $28FF-$2903, $2907-$290B. HL = the target ($DF10, $DF12):
; copies it into the value after it and writes every cell of the bar.
; All four return A = 0, carry clear and interrupts on, as the game's routine (its
; $05BB ends with EI); they change BC, DE, HL, F and keep IX, IY.
bar_hp:
        ld de,$7CEA             ; the first cell
        ld bc,$2E60             ; the tile sets
        jr bar_set
bar_esp:
        ld de,$7C6A
        ld bc,$2E3C
bar_set:
        ld (b_base),bc
        ld (b_dst),de
        ld b,(hl)               ; old
        ld (hl),a
        ld (b_new),a
        cp b
        jp z,bar_ret            ; no cell changes
        jr nc,.max              ; A = the larger, B = the smaller
        ld c,a
        ld a,b
        ld b,c
.max:   dec a
        rrca
        rrca
        rrca
        and $1F
        ld (b_hi),a             ; the last cell that changes, (larger - 1) / 8
        ld a,b
        rrca
        rrca
        rrca
        and $1F                 ; the first, smaller / 8
        jr bar_draw
bar_hp0:
        ld de,$7CEA
        ld bc,$2E60
        jr bar_init
bar_esp0:
        ld de,$7C6A
        ld bc,$2E3C
bar_init:
        ld (b_base),bc
        ld (b_dst),de
        ld a,(hl)               ; the target
        inc hl
        ld (hl),a               ; the value
        ld (b_new),a
        or a
        jr z,.h9
        dec a
        rrca
        rrca
        rrca
        and $1F                 ; the last cell that is not empty, (v - 1) / 8
        cp 10
        jr nc,.hi
.h9:    ld a,9
.hi:    ld (b_hi),a
        xor a                   ; from cell 0
bar_draw:
        push ix
        push iy
.cell:  ld (b_k),a
        add a,a
        add a,a
        add a,a
        ld c,a                  ; 8k
        ld a,(b_new)
        sub c
        jr nc,.pos
        xor a
.pos:   cp 9
        jr c,.set
        ld a,8
.set:   or a                    ; A = the cell's set, 0-8
        jr nz,.wr
        ld a,(b_k)
        cp 10
        jr nc,.next             ; an empty cell past the 10th: not written
        xor a
.wr:    add a,a
        add a,a
        ld hl,(b_base)
        ld e,a
        ld d,0
        add hl,de               ; HL = the set's 4 bytes
        ld a,(b_k)
        add a,a
        ld e,a
        ex de,hl
        ld bc,(b_dst)
        add hl,bc
        ex de,hl                ; DE = the cell's VRAM address
        ld bc,$0202             ; 2 bytes a run, 2 runs (the cell's two rows)
        ld ix,2
        ld iy,$40
        xor a                   ; the source as the game sees it
        call jt_vwrite
.next:  ld a,(b_hi)
        ld c,a
        ld a,(b_k)
        cp c
        inc a                   ; keeps the carry
        jr c,.cell
        pop iy
        pop ix
bar_ret:
        xor a
        ei
        ret
b_base: dw 0                    ; the bar's tile sets
b_dst:  dw 0                    ; the bar's first cell
b_new:  db 0                    ; the new value
b_hi:   db 0                    ; the last cell to write
b_k:    db 0                    ; the cell
endpage

# Psychic World (Europe) (Action Replay).cht, "Infinite H.P."
poke "Infinite H.P."
ar 00DF-1050
endpoke

# Psychic World (Europe) (Action Replay).cht, "Infinite ESP"
poke "Infinite ESP"
ar 00DF-1250
endpoke

# Psychic World (Europe) (Action Replay).cht, "Maximum Shot Power"
poke "Maximum shot power"
ar 00DF-1805
endpoke
