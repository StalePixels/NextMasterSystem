# Fire & Ice (Brazil) (En), CRC32 8B24A640, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from a sitescan run with two reference logs and hand-made
# entries, then decided by hand.
#
# Decisions:
# - io vector at $10: $0010-$0017 are zero bytes, and the game uses no RST but RST $00.
#   The game's reset at $0000 stays as it is.
# - Scan entries: the object script commands, through the table of 114 words at $597E
#   (dispatch CALL $35B7 at $357A; the low 13 bits are the handler's offset from $597E),
#   the four handlers in the table at $5D35 (dispatch at $5D56), and the seven in the
#   table at $64D9 (dispatch at $63DB). The interrupt hook at $DFEE is $0000 or $483B
#   ($028B and $0445). The object handler table at $3540 holds six words, all scanned.
# - Code runs only in banks 0 and 1. Slot 2 holds only data (banks 2-14) for the whole
#   game: no call or jump goes into it.
# - $0007-$026E is a development monitor (writes to $8000-$8003, a register dump on its
#   own stack at $026F, an upload loop that copies to $C000). Nothing in the game reaches
#   it: the reset jumps over it to $0275, the NMI handler at $0066 only sets $C5C0, and
#   RST $18 ($0018: JP $0050) is not used. Its I/O and mapper stores are left as they are.
# - Unused routines (no call, jump, address load or table entry names them): the VRAM
#   read at $13B3, the RLE name table fill at $3A0F, and the bank $0C call at $099F.
name Fire & Ice
cart 8B24A640
hz 60		; No-Intro region Brazil
vector 10 io
asm 00276 2   ; IM 1 -> IM 2
    im 2
endasm
site 00047   ; IN A,($BF)
site 00049   ; IN A,($C1)
site 00286   ; IN A,($BF)
site 00BB7   ; OUT ($7F),A
site 00C34   ; OUT ($7F),A
site 00C4C   ; OUT ($7F),A
site 00C58   ; OUT ($7F),A
site 00C6E   ; OUT ($7F),A
site 00C78   ; OUT ($7F),A
site 00D46   ; OUT ($7F),A
site 00D51   ; OUT ($7F),A
site 00D58   ; OUT ($7F),A
site 013A1   ; OUT ($BF),A
site 013A6   ; OUT ($BF),A
site 013AB   ; OUT ($BE),A
site 013CA   ; OUT ($BF),A
site 013CE   ; OUT ($BF),A
site 013D4   ; OUT ($BE),A
site 013DE   ; OUT ($BF),A
site 013E2   ; OUT ($BF),A
site 013E6   ; OUT ($BE),A
site 0141C   ; OUT ($BF),A
site 01420   ; OUT ($BF),A
site 0367F   ; OUT ($BF),A
site 03684   ; OUT ($BF),A
site 03687   ; IN A,($BE)
site 0368C   ; IN A,($BE)
site 036B0   ; OUT ($BF),A
site 036B5   ; OUT ($BF),A
site 036B9   ; OUT ($BE),A
site 036C5   ; OUT ($BE),A
site 036DD   ; OUT ($BF),A
site 036E0   ; OUT ($BF),A
site 03702   ; IN A,($BE)
site 0370D   ; IN A,($BE)
site 03717   ; IN A,($BE)
site 03723   ; IN A,($BE)
site 03797   ; OUT ($BF),A
site 0379C   ; OUT ($BF),A
site 037A0   ; OUT ($BE),A
site 037A7   ; OUT ($BE),A
site 037AC   ; OUT ($BE),A
site 037B1   ; OUT ($BE),A
site 03A62   ; OUT ($BF),A
site 03A65   ; OUT ($BF),A
site 03A82   ; OUT ($BE),A
site 03A87   ; OUT ($BE),A
site 03A9B   ; OUT ($BF),A
site 03A9E   ; OUT ($BF),A
site 03E8D   ; OUT ($BF),A
site 03E91   ; OUT ($BF),A
site 03E94   ; OUT ($BF),A
site 03E98   ; OUT ($BF),A
site 03EB1   ; IN A,($DC)
site 04060   ; OUT ($BF),A
site 04065   ; OUT ($BF),A
site 04069   ; OUT ($BE),A
site 04845   ; IN A,($BF)
site 04893   ; IN A,($BF)
site 04895   ; IN A,($DD)
site 048C6   ; OUT ($BF),A
site 048CA   ; OUT ($BF),A
site 048CF   ; OUT ($BF),A
site 048D3   ; OUT ($BF),A
site 048D8   ; OUT ($BF),A
site 048DD   ; OUT ($BF),A
site 048F6   ; OTIR
site 048FA   ; OUT ($BE),A
site 048FF   ; OUT ($BF),A
site 04904   ; OUT ($BF),A
site 0490C   ; OTIR
site 04911   ; OUT ($BE),A
site 04917   ; OUT ($BF),A
site 0491B   ; OUT ($BF),A
site 04937   ; OUT ($BF),A
site 0493B   ; OUT ($BF),A
site 04A3A   ; OUT ($BF),A
site 04A3E   ; OUT ($BF),A
site 04B57   ; OUT ($BF),A
site 04B5B   ; OUT ($BF),A
site 04FB8   ; OUT ($BF),A
site 04FBD   ; OUT ($BF),A
site 04FC0   ; OUT ($BE),A
site 04FC8   ; OUT ($BE),A
site 05010   ; OUT ($BF),A
site 05015   ; OUT ($BF),A
site 05018   ; OUT ($BE),A
site 05020   ; OUT ($BE),A
site 050A3   ; OUT ($BF),A
site 050A8   ; OUT ($BF),A
site 050D1   ; OUT ($BE),A
site 050D9   ; OUT ($BE),A
site 0510D   ; OUT ($BF),A
site 05112   ; OUT ($BF),A
site 05115   ; OUT ($BE),A
site 0511D   ; OUT ($BE),A
site 0575C   ; OUTI
site 0575E   ; OUTI
site 05761   ; OUTI
site 05763   ; OUTI
site 05792   ; OUTI
site 05794   ; OUTI
site 0579C   ; OUTI
site 0579E   ; OUTI
site 057A0   ; OUTI
site 057A2   ; OUTI
site 057A4   ; OUTI
site 057A6   ; OUTI
site 057A8   ; OUTI
site 057AA   ; OUTI
site 057AC   ; OUTI
site 057AE   ; OUTI
site 057B0   ; OUTI
site 057B2   ; OUTI
site 057B4   ; OUTI
site 057B6   ; OUTI
site 057B8   ; OUTI
site 057BA   ; OUTI
site 057BC   ; OUTI
site 057BE   ; OUTI
site 057C0   ; OUTI
site 057C2   ; OUTI
site 057C4   ; OUTI
site 057C6   ; OUTI
site 057C8   ; OUTI
site 057CA   ; OUTI
site 057CC   ; OUTI
site 057CE   ; OUTI
site 057D0   ; OUTI
site 057D2   ; OUTI
site 057D4   ; OUTI
site 057D6   ; OUTI
site 057D8   ; OUTI
site 057DA   ; OUTI
site 057FE   ; OUT ($BF),A
site 05803   ; OUT ($BF),A
site 05817   ; OUT ($BE),A
site 0581E   ; OUT ($BE),A
site 0583C   ; OUT ($BE),A
site 05843   ; OUT ($BE),A
site 070A7   ; OUT ($BF),A
site 070AB   ; OUT ($BF),A
site 070B2   ; OUT ($BE),A
mapst 0010C   ; LD ($FFFF),A
mapst 0011F   ; LD ($FFFF),A
mapst 00278   ; LD ($FFFC),A
mapst 0027B   ; LD ($FFFD),A
mapst 0027F   ; LD ($FFFE),A
mapst 00283   ; LD ($FFFF),A
mapst 00417   ; LD ($FFFF),A
mapst 008A2   ; LD ($FFFF),A
mapst 00933   ; LD ($FFFF),A
mapst 03313   ; LD ($FFFF),A
mapst 03322   ; LD ($FFFF),A
mapst 03336   ; LD ($FFFF),A
mapst 03345   ; LD ($FFFF),A
mapst 033DE   ; LD ($FFFF),A
mapst 035F8   ; LD ($FFFF),A
mapst 03769   ; LD ($FFFF),A
mapst 0399A   ; LD ($FFFF),A
mapst 039D2   ; LD ($FFFF),A
mapst 03DC3   ; LD ($FFFF),A
mapst 03E39   ; LD ($FFFF),A
mapst 040B1   ; LD ($FFFF),A
mapst 04772   ; LD ($FFFF),A
mapst 047A5   ; LD ($FFFF),A
mapst 047CD   ; LD ($FFFF),A
mapst 0486E   ; LD ($FFFF),A
mapst 0487E   ; LD ($FFFF),A
mapst 048B3   ; LD ($FFFF),A
mapst 04A55   ; LD ($FFFF),A
mapst 04A70   ; LD ($FFFF),A
mapst 051D0   ; LD ($FFFF),A
mapst 0524B   ; LD ($FFFF),A
mapst 053A7   ; LD ($FFFF),A
mapst 0541B   ; LD ($FFFF),A
mapst 05782   ; LD ($FFFF),A
mapst 057F9   ; LD ($FFFF),A
mapst 06D54   ; LD ($FFFF),A
mapst 06F47   ; LD ($FFFF),A
mapst 06F5B   ; LD ($FFFF),A
# Name table queue $57E2 (bank 1), called from the interrupt hook at $4874: a list at $C8F4
# of items, each a count byte (0 ends the list), a bank for slot 2, a VDP address (2 bytes)
# and then either one source address (count below $80: count rows of 16 cells, each cell the
# source byte, then the byte from the bit-reverse table at $0500 for the next source byte) or,
# with bit 7 of the count set, a row count and count&$7F source addresses, each that many rows
# (cells as the reversed byte, then the plain byte). All rows go to the VDP one after the other. At
# the end HL = $C8F4, ($CA84) = $C8F4 and ($C8F4) = 0. Through the runtime each cell cost two
# data port traps, about 2,300 Next cycles, and the routine took about a quarter of the frame
# in play. Page entry ntq builds each row of 16 cells in a buffer and writes it with one
# jt_vwrite call.
asm 057E2 5   ; LD HL,$C8F4; LD A,(HL); AND A
    rst $10
    db far_io, pg_ntq, ent_ntq
    ret
endasm
page 0 ntq
; ntq: the whole of $57E2-$585B. Called with interrupts off (from the frame handler). Runs
; on a stack of its own. Returns HL = $C8F4; A, F, BC, DE changed; IX and IY kept.
ntq:    ld (q_sp),sp
        ld sp,q_stack
        push ix
        push iy
        ld hl,$C8F4
.item:  ld a,(hl)
        and a
        jp z,.done
        ld b,a
        inc hl
        ld a,($FFFF)            ; the bank: as $57EC-$57F9
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
.done:  ld hl,$C8F4
        ld ($CA84),hl
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
q_sp:    dw 0
q_vaddr: dw 0
q_stage: ds 32
q_buf:   ds 32
         ds 64
q_stack:
endpage

# Fire _ Ice (Brazil).cht, "Infinite Lives": RAM $D56B is the lives counter (6 at the start;
# the HUD shows it); held at 6 a death leaves it at 6
poke "Infinite lives"
ar 00D5-6B06
endpoke

# Fire _ Ice (Brazil).cht, "Infinite Snowflakes": RAM $C1F4 is the snowflake counter; the code
# changes the store at $43FF that writes the decremented count back, so spending a snowflake
# leaves the count as it was. The player still has to collect snowflakes first
poke "Infinite snowflakes"
gg 423-FFB-2A2
endpoke

# Fire _ Ice (Brazil).cht, "Invulnerability" (Action Replay): RAM $CBB1 is the hit timer, set
# after a hit; held at $5E no hit costs a life
poke "Invincibility"
ar 00CB-B15E
endpoke
