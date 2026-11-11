# Ottifants, The (Europe, Brazil) (En,Fr,De,Es,It), CRC32 82EF2A7D, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from a sitescan run with three reference logs, then decided by
# hand.
#
# Decisions:
# - io vector at $10: $0010-$0017 are zero bytes and the game uses no RST there. The vector
#   writes $0010-$0012 only; the bank helper at $0050 reads $0016 (0), which stays as it is.
#   The game's reset at $0000 stays as it is.
# - $0007-$026E is a development monitor, the same as in Fire & Ice. The game uses one part
#   of it: RST $18 ($2874) jumps to the bank helper at $0050, whose store at $0055 is patched.
#   The rest of the monitor is never run; its I/O and mapper stores are left as they are.
#   The words $01CA, $01D7 and $01DF that bank 1 stores to $C9D9 are values ($2771 compares
#   them with SBC HL,DE), not code addresses in the monitor.
# - Bank 1 holds object code that the scan does not reach through its handler tables. It
#   calls the bank switch at $4BE1 ($56B2, $5774, $5B3D), so the stores at $4BEC and at
#   $404F (the same form, LD A,$06 : OR E before it) are patched.
# - Code runs only in banks 0 and 1. Slot 2 holds data for the whole game: no call or jump
#   goes into it, and the reference logs ran no code there.
# - Unused routines (no call, jump or address word in banks 0 and 1 names them): the VRAM
#   read at $2465 and the bank $0C routine at $0996.
name The Ottifants
cart 82EF2A7D
hz 50		; No-Intro regions Europe, Brazil
vector 10 io
asm 00276 2   ; IM 1 -> IM 2
    im 2
endasm
site 00047   ; IN A,($BF)
site 00049   ; IN A,($C1)
site 00286   ; IN A,($BF)
site 00BC1   ; OUT ($7F),A
site 00C3E   ; OUT ($7F),A
site 00C56   ; OUT ($7F),A
site 00C62   ; OUT ($7F),A
site 00C78   ; OUT ($7F),A
site 00C82   ; OUT ($7F),A
site 00D50   ; OUT ($7F),A
site 00D5B   ; OUT ($7F),A
site 00D62   ; OUT ($7F),A
site 00E71   ; OUT ($BF),A
site 00E75   ; OUT ($BF),A
site 0110F   ; OUT ($BF),A
site 01113   ; OUT ($BF),A
site 0111F   ; OUT ($BE),A
site 01126   ; OUT ($BF),A
site 0112A   ; OUT ($BF),A
site 01131   ; OUT ($BE),A
site 01137   ; OUT ($BE),A
site 0192E   ; OUT ($BF),A
site 01931   ; OUT ($BF),A
site 0194B   ; OUT ($BE),A
site 01950   ; OUT ($BE),A
site 01964   ; OUT ($BF),A
site 01967   ; OUT ($BF),A
site 0229B   ; OUT ($BF),A
site 0229F   ; OUT ($BF),A
site 022A2   ; OUT ($BF),A
site 022A6   ; OUT ($BF),A
site 022C8   ; IN A,($DC)
site 02440   ; OUT ($BF),A
site 02445   ; OUT ($BF),A
site 02449   ; OUT ($BE),A
site 02453   ; OUT ($BF),A
site 02458   ; OUT ($BF),A
site 0245D   ; OUT ($BE),A
site 0247C   ; OUT ($BF),A
site 02480   ; OUT ($BF),A
site 02486   ; OUT ($BE),A
site 02490   ; OUT ($BF),A
site 02494   ; OUT ($BF),A
site 02498   ; OUT ($BE),A
site 024A6   ; OUT ($BF),A
site 024AA   ; OUT ($BF),A
site 02800   ; IN A,($BF)
site 02823   ; OUT ($BF),A
site 02827   ; OUT ($BF),A
site 02842   ; OUT ($BF),A
site 02846   ; OUT ($BF),A
site 0286B   ; IN A,($DD)
site 028B8   ; OUT ($BF),A
site 028BD   ; OUT ($BF),A
site 028D6   ; OTIR
site 028DA   ; OUT ($BE),A
site 028DF   ; OUT ($BF),A
site 028E4   ; OUT ($BF),A
site 028EC   ; OTIR
site 028F1   ; OUT ($BE),A
site 028F7   ; OUT ($BF),A
site 028FB   ; OUT ($BF),A
site 0292A   ; OUT ($BF),A
site 0292E   ; OUT ($BF),A
site 02FDA   ; OUT ($BE),A
site 02FE0   ; OUT ($BE),A
site 0302D   ; OUT ($BF),A
site 03030   ; OUT ($BE),A
site 03036   ; OUT ($BE),A
site 030EE   ; OUT ($BE),A
site 03131   ; OUT ($BE),A
site 0316E   ; OUTI
site 03170   ; OUTI
site 03173   ; OUTI
site 03175   ; OUTI
site 031A4   ; OUTI
site 031A6   ; OUTI
site 031AE   ; OUTI
site 031B0   ; OUTI
site 031B2   ; OUTI
site 031B4   ; OUTI
site 031B6   ; OUTI
site 031B8   ; OUTI
site 031BA   ; OUTI
site 031BC   ; OUTI
site 031BE   ; OUTI
site 031C0   ; OUTI
site 031C2   ; OUTI
site 031C4   ; OUTI
site 031C6   ; OUTI
site 031C8   ; OUTI
site 031CA   ; OUTI
site 031CC   ; OUTI
site 031CE   ; OUTI
site 031D0   ; OUTI
site 031D2   ; OUTI
site 031D4   ; OUTI
site 031D6   ; OUTI
site 031D8   ; OUTI
site 031DA   ; OUTI
site 031DC   ; OUTI
site 031DE   ; OUTI
site 031E0   ; OUTI
site 031E2   ; OUTI
site 031E4   ; OUTI
site 031E6   ; OUTI
site 031E8   ; OUTI
site 031EA   ; OUTI
site 031EC   ; OUTI
site 03210   ; OUT ($BF),A
site 03216   ; OUT ($BF),A
site 0322A   ; OUT ($BE),A
site 03231   ; OUT ($BE),A
site 0324F   ; OUT ($BE),A
site 03256   ; OUT ($BE),A
site 03327   ; OUT ($BF),A
site 0332C   ; OUT ($BF),A
site 0332F   ; IN A,($BE)
site 03334   ; IN A,($BE)
site 03358   ; OUT ($BF),A
site 0335D   ; OUT ($BF),A
site 03361   ; OUT ($BE),A
site 0336D   ; OUT ($BE),A
site 03385   ; OUT ($BF),A
site 03388   ; OUT ($BF),A
site 033AA   ; IN A,($BE)
site 033B5   ; IN A,($BE)
site 033BF   ; IN A,($BE)
site 033CB   ; IN A,($BE)
site 0343F   ; OUT ($BF),A
site 03444   ; OUT ($BF),A
site 03448   ; OUT ($BE),A
site 0344F   ; OUT ($BE),A
site 03454   ; OUT ($BE),A
site 03459   ; OUT ($BE),A
site 03D0A   ; OUT ($BF),A
site 03D0E   ; OUT ($BF),A
site 03D15   ; OUT ($BE),A
mapst 00055   ; LD ($FFFF),A
mapst 00278   ; LD ($FFFC),A
mapst 0027B   ; LD ($FFFD),A
mapst 0027F   ; LD ($FFFE),A
mapst 00283   ; LD ($FFFF),A
mapst 00417   ; LD ($FFFF),A
mapst 0088E   ; LD ($FFFF),A
mapst 00927   ; LD ($FFFF),A
mapst 01508   ; LD ($FFFF),A
mapst 01866   ; LD ($FFFF),A
mapst 0189B   ; LD ($FFFF),A
mapst 018CD   ; LD ($FFFF),A
mapst 018F0   ; LD ($FFFF),A
mapst 021F2   ; LD ($FFFF),A
mapst 0223F   ; LD ($FFFF),A
mapst 024EC   ; LD ($FFFF),A
mapst 02834   ; LD ($FFFF),A
mapst 02855   ; LD ($FFFF),A
mapst 02914   ; LD ($FFFF),A
mapst 02939   ; LD ($FFFF),A
mapst 02A72   ; LD ($FFFF),A
mapst 02A80   ; LD ($FFFF),A
mapst 02B10   ; LD ($FFFF),A
mapst 02B20   ; LD ($FFFF),A
mapst 03194   ; LD ($FFFF),A
mapst 0320B   ; LD ($FFFF),A
mapst 03277   ; LD ($FFFF),A
mapst 032A0   ; LD ($FFFF),A
mapst 03411   ; LD ($FFFF),A
mapst 034A9   ; LD ($FFFF),A
mapst 036E0   ; LD ($FFFF),A
mapst 0371D   ; LD ($FFFF),A
mapst 0404F   ; LD ($FFFF),A
mapst 04BEC   ; LD ($FFFF),A
mapst 04E3D   ; LD ($FFFF),A
mapst 04E90   ; LD ($FFFF),A
mapst 04ECD   ; LD ($FFFF),A
mapst 04EDD   ; LD ($FFFF),A
mapst 04EF4   ; LD ($FFFF),A
mapst 04F0F   ; LD ($FFFF),A
mapst 05090   ; LD ($FFFF),A

# Ottifants, The (Europe, Brazil) (En,Fr,De,Es,It).cht, "Invulnerability": RAM $C8C8 is the
# hit timer; held at $16 a hit does no damage
poke "Invincibility"
ar 00C8-C816
endpoke

# Ottifants, The (Europe, Brazil) (En,Fr,De,Es,It).cht, "Infinite Lives": RAM $D121 is the
# number of lives
poke "Infinite lives"
ar 00D1-2109
endpoke

# Scroll column writer (from $2F64, in the frame hook): per cell a control write, two data
# writes, four traps a cell through the runtime. Page entry col runs both column loops and
# writes each part with one jt_vwrite call.
asm 02FD1 7   ; LD A,L; OUT ($BF),A; LD A,H; OR $40; OUT ($BF),A (the loop $2FD1-$301A)
    rst $10
    db far_io, pg_col, ent_col
    jp $301C
endasm
asm 03027 5   ; LD A,L; OUT ($BF),A; LD A,H (the loop $3027-$3070, then RET at $3072)
    rst $10
    db far_io, pg_col, ent_col
    ret
endasm
# Scroll row writer $3073 (in the frame hook, and from the level draw at $2F22): a control
# write of the row's address, then two data writes a cell. Entry rowa keeps the address, which
# the game has in HL at $30B8 and loses before the loop; entry row runs the first row loop,
# row2 the second (address in HL), and each writes its part with one jt_vwrite call.
asm 030B8 8   ; LD A,L; OUT ($BF),A; LD A,H; OR $40; OUT ($BF),A
    rst $10
    db far_io, pg_rowa, ent_rowa
    nop
    nop
    nop
    nop
endasm
asm 030E6 7   ; LD A,(DE); OUT ($BE),A; INC DE; LD A,(DE); AND $F6 (the loop $30E6-$310F)
    rst $10
    db far_io, pg_row, ent_row
    jp $3111
endasm
asm 03121 5   ; LD A,L; OUT ($BF),A; LD A,H (the control writes $3121-$3128, the loop
    rst $10   ; $3129-$3152, then RET)
    db far_io, pg_row2, ent_row2
    ret
endasm
# Name table queue $31F4 (bank 0), called from $284B in the frame hook: a list at $C5FC
# of items, each a count byte (0 ends the list), a bank for slot 2, a VDP address (2 bytes)
# and then either one source address (count below $80: count rows of 16 cells, each cell the
# source byte, then the byte from the bit-reverse table at $0500 for the next source byte) or,
# with bit 7 of the count set, a row count and count&$7F source addresses, each that many rows
# (cells as the reversed byte, then the plain byte). All rows go to the VDP one after the
# other. At the end HL = $C5FC, ($C78C) = $C5FC and ($C5FC) = 0. Through the runtime each cell
# costs two data port traps. The routine is Fire & Ice's ($57E2 there), and page entry ntq is
# that spec's entry with this game's addresses: it builds each row of 16 cells in a buffer and
# writes it with one jt_vwrite call.
asm 031F4 5   ; LD HL,$C5FC; LD A,(HL); AND A
    rst $10
    db far_io, pg_ntq, ent_ntq
    ret
endasm
page 0 ntq col rowa row row2
; ntq: the whole of $31F4-$326E. Called with interrupts off (from the frame handler). Runs
; on a stack of its own. Returns HL = $C5FC; A, F, BC, DE changed; IX and IY kept.
ntq:    ld (q_sp),sp
        ld sp,q_stack
        push ix
        push iy
        ld hl,$C5FC
.item:  ld a,(hl)
        and a
        jp z,.done
        ld b,a
        inc hl
        ld a,($FFFF)            ; the bank: as $31FE-$320B
        ld c,a
        and $0F
        cp (hl)
        jr z,.same
        ld a,c
        and $F0
        or (hl)
        rst $10
        db $13, $FF
.same:  inc hl
        ld e,(hl)               ; the VDP address
        inc hl
        ld d,(hl)
        inc hl
        ld (q_vaddr),de
        ld a,b
        add a,a
        jr c,.parts
        ld e,(hl)               ; count rows from one source, cell = byte, reversed byte
        inc hl
        ld d,(hl)
        inc hl
        push hl
        ex de,hl
.row0:  push bc
        call stage
        push hl
        ld hl,q_stage
        ld de,q_buf
        ld b,16
.cell0: ld a,(hl)
        ld (de),a
        inc hl
        inc de
        ld a,(hl)
        inc hl
        push hl
        ld l,a
        ld h,high q_rev
        ld a,(hl)
        pop hl
        ld (de),a
        inc de
        djnz .cell0
        call put
        pop hl
        pop bc
        djnz .row0
        pop hl
        jp .item
.parts: res 7,b                 ; count&$7F parts of rows rows each: a rows byte, then the
        ld c,b                  ; sources; cell = reversed byte, byte
        ld b,(hl)
        inc hl
.part:  ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        push hl
        push bc
        ex de,hl
.row1:  push bc
        call stage
        push hl
        ld hl,q_stage
        ld de,q_buf
        ld b,16
.cell1: ld a,(hl)
        inc hl
        push hl
        ld l,a
        ld h,high q_rev
        ld a,(hl)
        pop hl
        ld (de),a
        inc de
        ld a,(hl)
        ld (de),a
        inc hl
        inc de
        djnz .cell1
        call put
        pop hl
        pop bc
        djnz .row1
        pop bc
        pop hl
        dec c
        jp nz,.part
        jp .item
.done:  ld hl,$C5FC
        ld ($C78C),hl
        ld (hl),0
        pop iy
        pop ix
        ld sp,(q_sp)
        ret
; stage: copy the 32 source bytes at HL as the game sees them into q_stage; HL += 32.
; A source with any byte in $2000-$3FFF is read through jt_peek.
stage:  ld a,h
        cp $40
        jr nc,.fast
        cp $1F
        jr c,.fast
        ld de,q_stage
        ld b,32
.slow:  call jt_peek
        ld (de),a
        inc hl
        inc de
        djnz .slow
        ret
.fast:  ld de,q_stage
        ld bc,32
        ldir
        ret
; put: write q_buf (32 bytes) at q_vaddr; q_vaddr += 32.
put:    push hl
        ld hl,q_buf
        ld de,(q_vaddr)
        ld bc,$2001
        ld ix,32
        ld iy,32
        ld a,1
        call jt_vwrite
        ld hl,32
        add hl,de
        ld (q_vaddr),hl
        pop hl
        ret
; q_rev: the bit-reverse table, the same bytes as the game's table at $0500.
        align 256
q_rev:
x = 0
        dup 256
        db ((x&1)<<7)|((x&2)<<5)|((x&4)<<3)|((x&8)<<1)|((x&16)>>1)|((x&32)>>3)|((x&64)>>5)|((x&128)>>7)
x = x + 1
        edup
; col: the column loops $2FD1-$301A and $3027-$3070 (the scroll column writer from $2F64).
; Called from the frame hook; runs with interrupts off on its own stack and restores the
; interrupt state at the end. In: HL = the VRAM address of the first
; cell, DE = its source, B = the cells, IX = the map pointer. Each cell is a control write
; of HL, then (DE) and (DE+1)&$F6 to the data port; HL += $40. Runs the game's loop with the
; data writes into c_buf, then writes the column with one jt_vwrite call (2 bytes a run,
; $40 apart). Returns every register as the game's loop leaves it.
col:
        ld a,i                  ; keep the interrupt state for cr_ei; run with interrupts off
        di
        ld a,$00
        jp po,$+5
        ld a,$FB
        ld (cr_ei),a
        ld (c_sp),sp
        ld sp,c_stack
        push iy
        ld (c_v),hl
        ld a,b
        ld (c_n),a
        ld iy,c_buf
.cell:  call rde
        ld (iy+0),a
        inc de
        call rde
        and $F6
        ld (iy+1),a
        inc iy
        inc iy
        ld a,e
        add a,$07
        ld e,a
        and $18
        jr nz,.next
        push bc
        ld a,($D450)
        ld c,a
        ld b,$00
        add ix,bc
        call rix
        add a,a
        ld c,a
        ld a,$00
        adc a,$00
        ld b,a
        ld a,c
        add a,$F7
        ld c,a
        ld a,b
        adc a,$D1
        ld b,a
        ld a,(bc)
        ld e,a
        ld a,($D416)
        add a,e
        ld e,a
        inc bc
        ld a,(bc)
        adc a,$00
        ld d,a
        pop bc
.next:  ld a,$40
        add a,l
        ld l,a
        ld a,h
        adc a,$00
        ld h,a
        djnz .cell
        push af
        push bc
        push de
        push hl
        push ix
        ld hl,c_buf
        ld de,(c_v)
        ld a,(c_n)
        ld c,a
        ld b,2
        ld ix,2
        ld iy,$40
        ld a,1
        call jt_vwrite
        jr cr_out
; rowa: keep HL, the VRAM address of the row ($30B8), in r_v. Every register is kept.
rowa:   ld (r_v),hl
        ret
; row2: the second part of a row ($3121): HL is its VRAM address.
row2:   ld (r_v),hl
; row: the row loops $30E6-$310F and $3129-$3152 (the scroll row writer $3073). Called with
; interrupts off (from the frame hook) or on (from the level draw at $2F22). In: r_v = the
; row's VRAM address, DE = the source of the first cell, B = the cells, IX = the map pointer.
; Each cell is (DE) and (DE+1)&$F6 to the data port. Runs the game's loop with the data
; writes into c_buf, then writes the row at r_v with one jt_vwrite call. Runs with interrupts
; off on its own stack and restores the interrupt state at the end. Returns every register as
; the game's loop leaves it.
row:
        ld a,i                  ; keep the interrupt state for cr_ei; run with interrupts off
        di
        ld a,$00
        jp po,$+5
        ld a,$FB
        ld (cr_ei),a
        ld (c_sp),sp
        ld sp,c_stack
        push iy
        ld a,b
        ld (c_n),a
        ld iy,c_buf
.cell:  call rde
        ld (iy+0),a
        inc de
        call rde
        and $F6
        inc e
        ld (iy+1),a
        inc iy
        inc iy
        ld a,e
        and $07
        jr nz,.next
        call rix
        ld l,a
        ld h,$00
        inc ix
        add hl,hl
        ld a,l
        add a,$F7
        ld l,a
        ld a,h
        adc a,$D1
        ld h,a
        ld a,($D416)
        add a,(hl)
        ld e,a
        inc hl
        ld a,(hl)
        adc a,$00
        ld d,a
.next:  djnz .cell
        push af
        push bc
        push de
        push hl
        push ix
        ld hl,c_buf
        ld de,(r_v)
        ld a,(c_n)
        add a,a
        ld b,a
        ld c,1
        ld ix,64
        ld iy,64
        ld a,1
        call jt_vwrite
cr_out: pop ix
        pop hl
        pop de
        pop bc
        pop af
        pop iy
        ld sp,(c_sp)
cr_ei:  nop                     ; EI when interrupts were on at the entry
        ret
; rde: A = the byte the game sees at DE. rix: A = the byte the game sees at IX. F changes.
rde:    ld a,d
        cp $20
        jr c,.fast
        cp $40
        jr nc,.fast
        ex de,hl
        call jt_peek
        ex de,hl
        ret
.fast:  ld a,(de)
        ret
rix:    push hl
        push ix
        pop hl
        call jt_peek
        pop hl
        ret
c_sp:   dw 0
c_v:    dw 0
r_v:    dw 0
c_n:    db 0
c_buf:  ds 512
        ds 64
c_stack:
q_sp:    dw 0
q_vaddr: dw 0
q_stage: ds 32
q_buf:   ds 32
         ds 64
q_stack:
endpage
