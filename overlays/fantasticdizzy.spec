# Fantastic Dizzy, drafted by tools/mkspec.py from sitescan output.
name Fantastic Dizzy
cart B9664AE1
hz 50		; No-Intro regions Europe
# In play the frame handler turns the display off at its start and on again
# at $0279, after its VRAM work. On the Next that work, with the runtime's
# once-a-frame work that runs in it, ends well inside the next picture, so
# the top of the picture stayed black. toppal holds the display-off write
# until the display-on write takes it back (design.md, "Display off and on").
toppal
# No free RST vector. The cart starts with NOP; JP $03A6, and $0003-$0037 is
# data. $0000-$0002 becomes the vector; the game starts at $03A6 (DI; IM 1;
# LD SP,$DEFF).
vector 00 io
start 03A6 DEFF
# The title screens set H scroll by polling the V counter for given lines
# (lines 0-46 of the wavy logo, lines 155 and 182 of the title). A poll and
# the register 8 write after it cost more than a line through the traps, so
# the game missed lines and waited a frame for each: the wavy logo took
# minutes. The logo's loop is replaced by a code cave that stamps the frame,
# and the rastercode routine gives the same per-line H scroll from RAM.
# The polls also kept these loops to one pass a frame, so each cave that
# drops polls waits for the game's interrupt count ($DBDE, counted by the
# frame handler at $0157) to change from the pass before ($DF02).
rastercode fantasticdizzy-raster.asm
# Unreached code that the byte scan rates high, judged code by reading it:
# $5D60-$5DBC (bank 1) is a room change routine with the bank switches on the
# codem lines above (LD A,$0B : LD ($8000),A : CALL $8111 ... display off);
# $07F4 is a routine that writes 32 zeros to CRAM, called from banks 4 and 8.
site 05D77   ; OUT ($BF),A
site 05D7B   ; OUT ($BF),A
site 007F6   ; OUT ($BF),A
site 007FA   ; OUT ($BF),A
site 007FF   ; OUT ($BE),A
asm 26A8E 42   ; wavy logo: LD B,0 ... JR C,$AA96 (per-line register 8 loop)
    push hl             ; wait for a game frame interrupt since the last pass
    ld hl,$DF02
.sync:
    ld a,($DBDE)        ; the game's interrupt count
    cp (hl)
    jr z,.sync
    ld (hl),a
    pop hl
    ld a,($D0CE)        ; ($D0CF) ends as the loop leaves it
    add a,$2F
    and $3F
    ld ($D0CF),a
    ld a,(isr_n)        ; stamp for the rastercode routine
    ld ($DF00),a
    ld b,$2F
endasm
# The language choice writes its five names as sprites in two sets, ENGLISH
# and FRANCAIS for the upper half, DEUTSCH, ITALIANO and ESPANOL for the lower
# half: it polls the V counter for line 46, turns the display off, writes the
# first set to the sprite table, turns the display on at line 62, and does the
# same for the second set at lines 113 and 130. The Next shows one sprite table
# a frame, so the upper names never showed, and the missed polls cost a frame
# each (the screen ran four times as slow). The caves below drop the polls,
# the first set's write and the display-off calls: both sets go into the
# buffer, and the second write puts all five names in the table at once.
asm 26B47 34   ; poll line 46, CALL $06F6, CALL $0741, sprite buffer reset, poll line 62
    push hl             ; wait for a game frame interrupt since the last pass
    ld hl,$DF02
.sync:
    ld a,($DBDE)        ; the game's interrupt count
    cp (hl)
    jr z,.sync
    ld (hl),a
    pop hl
endasm
asm 26BBC 9    ; poll line 113, CALL $06F6 (display off)
endasm
asm 26BD8 6    ; poll line 130
endasm
asm 26BF1 6    ; poll line 133
endasm
# In play the frame handler ($BB87, two copies of the same code) splits the
# status bar from the play area: it waits for the sprite collision flag, which
# sprites 0 and 1 (two copies of tile $BF at Y 29) raise at line 30, then sets
# the play area's palette and H scroll. Without collline the Next raises the
# flag only from the once-a-frame work, and not at all when the display was
# still off for that picture, so the handler waited for ever; the next frame
# interrupt came in it (the handler turns interrupts on at $1F2A), the stack
# ran down over the game's variables and the game reset. collline raises the
# flag at line 30 as the SMS does. $BB87 starts with a status read that clears
# it, so that read must come before line 30: 118 Next lines after the frame
# event (play is in 224-line mode). workline moves the runtime's once-a-frame
# work (about 40,000 to 150,000 cycles) out of that time, from the ULA
# interrupt to line 56, after the split's palette and H scroll writes.
collline
workline 56
# In play the game writes register 8 twice a frame: the status bar's H (the
# cart byte at $0005) in the frame handler, and the play area's H, ($D795),
# at the split. With line interrupts off the runtime takes a register 8 write
# into the copper list for the next picture only, so the whole picture showed
# the play area's H. On the Master System the split's write comes about 1.9
# lines after the status read that sees the flag, so the H changes from line
# 33. pal8p stamps the split; the rastercode routine then gives play as two
# segments (rastseg): the status bar's H from line 0 and ($D795) from 33.
# The title polls for lines 155 and 182 to set the H scroll of its mountain
# and grass bands. The cave drops the polls and the two register 8 writes and
# stamps the frame; the rastercode routine then gives the three bands as
# segments (rastseg: H 0 from line 0, ($C127) from 155, ($C128) from 182).
rastseg
asm 26DA7 36   ; title: the polls for lines 155 and 182 and their register 8 writes
    push hl             ; wait for a game frame interrupt since the last pass
    ld hl,$DF02
.sync:
    ld a,($DBDE)        ; the game's interrupt count
    cp (hl)
    jr z,.sync
    ld (hl),a
    pop hl
    ld a,(isr_n)        ; stamp for the rastercode routine
    ld ($DF03),a
endasm
# In play the frame handler ($022D) turns the display off, does its VRAM work
# and turns the display on again at $0279. On the Master System that fits in
# the vertical blank. Through the traps it took about 420,000 cycles, so the
# display stayed off for most of the next picture, and the split above
# reached line 30 late. These routines in it are replaced by page 0:
# - $1F2A writes the room's cell list: 16 or 24 pairs of words at $D7D2 or
#   $D7B2 (to $D811), each a VDP address and a name table cell, popped off a
#   stack pointer and written with 4 OUT (C),r (about 146,000 cycles). The
#   caves at $1F3D and $200C call cells16 or cells24, which write each cell
#   with jt_vwrite, then go on at the routine's own EI : RET.
# - $394E writes 3 tiles from 2-plane data: 24 groups of OUTI, OUTI and two
#   OUT ($BE),A with A = 0, from bank $0D (phases 1-3 of the animated tiles,
#   one phase a frame). The cave after the bank switch calls tiles3, which
#   writes the 96 bytes with two jt_vwrite calls, then goes on at the
#   routine's end ($3A16).
# - $0263-$0278 writes all 32 CRAM entries each frame (status bar palette from
#   $007D, then $D971), and the split at $BB9D or $BBC9 writes entries 0-7
#   from $D969: about 1,700 cycles an entry with toppal. pal32 and pal8p
#   write only the entries whose colour differs from the runtime's copy.
# - $BC08 writes 4 name table bytes of the status bar, each with its own
#   control word (stat4); $BCDB writes 8 bytes of tile $13F with a data read
#   before each (anim8). Both use jt_vwrite.
asm 01F3D 10   ; DI : LD ($D79B),SP : LD SP,$D7D2 : LD C,$BF (cell list, 16 cells)
    di
    rst $00
    db far_io, pg_cells16, ent_cells16
    jp $200A            ; EI : RET
endasm
asm 0200C 10   ; DI : LD ($D79B),SP : LD SP,$D7B2 : LD C,$BF (cell list, 24 cells)
    di
    rst $00
    db far_io, pg_cells24, ent_cells24
    jp $2139            ; EI : RET
endasm
asm 03953 7    ; LD C,$BE : XOR A : OUTI : OUTI (3 tiles from 2-plane data)
    rst $00
    db far_io, pg_tiles3, ent_tiles3
    jp $3A16            ; bank 2 back : RET
endasm
asm 00263 22   ; LD A,$00 : OUT ($BF),A : LD A,$C0 : OUT ($BF),A : LD HL,$007D : LD C,$BE : CALL $37A9 : LD HL,$D971 : CALL $3789
    rst $00
    db far_io, pg_pal32, ent_pal32
    jp $0279
endasm
asm 0BB9D 19   ; LD A,$00 : OUT ($BF),A : LD A,$C0 : OUT ($BF),A : LD HL,$D969 : LD B,$08 : LD A,(HL) : OUT ($BE),A : INC HL : DJNZ
    rst $00
    db far_io, pg_pal8p, ent_pal8p
    jp $BBB0
endasm
asm 0BBC9 19   ; the same at $BBC9
    rst $00
    db far_io, pg_pal8p, ent_pal8p
    jp $BBDC
endasm
asm 0BC08 6    ; LD A,$5C : OUT ($BF),A : LD A,$78 (4 name table bytes)
    rst $00
    db far_io, pg_stat4, ent_stat4
    ret
endasm
asm 0BCDB 6    ; LD A,$E4 : OUT ($BF),A : LD A,$67 (8 tile bytes, every second byte)
    rst $00
    db far_io, pg_anim8, ent_anim8
    ret
endasm
page 0 cells16 cells24 tiles3 pal32 pal8p stat4 anim8
; cells16, cells24: as the game's $1F3D-$200B and $200C-$213A, with
; interrupts off. Each cell is a word pair: the VDP control word (low byte
; first), then the 2 data bytes. Cells that set VRAM write addresses with the
; same step from one to the next (the room's cell column: step $40) go out
; as one jt_vwrite call: runs of 2 bytes, source step 4, VRAM step the
; address step. Any other control word goes through the runtime's I/O RST,
; byte by byte, as the game's OUT (C),r would. Keeps every register except
; AF.
cells16:
        push hl
        ld hl,$D7D2
        jr cells
cells24:
        push hl
        ld hl,$D7B2
cells:  push bc
        push de
        push ix
        push iy
.next:  ld a,l
        cp $12                  ; the list ends at $D811
        jp z,.done
        ld e,(hl)
        inc hl
        ld d,(hl)
        dec hl
        ld a,d
        and $C0
        cp $40
        jr nz,.slow
        ld (cl_start),hl        ; the run's first cell
        ld (cl_first),de
        ld (cl_prev),de
        ld c,1                  ; cells in the run
        ld b,0                  ; 0: no step yet
.grow:  inc hl
        inc hl
        inc hl
        inc hl
        ld a,l
        cp $12
        jr z,.go
        ld e,(hl)
        inc hl
        ld d,(hl)
        dec hl
        ld a,d
        and $C0
        cp $40
        jr nz,.go
        push hl
        ex de,hl                ; HL = this cell's address
        ld de,(cl_prev)
        ld (cl_prev),hl
        or a
        sbc hl,de               ; HL = the step from the cell before
        ld a,b
        or a
        jr nz,.cmp
        ld (cl_step),hl
        inc b
        jr .take
.cmp:   ld de,(cl_step)
        or a
        sbc hl,de
        jr z,.take
        pop hl                  ; another step: the run ends before this cell
        jr .go
.take:  pop hl
        inc c
        jr .grow
.go:    push hl                 ; the first cell after the run
        ld hl,(cl_start)
        inc hl
        inc hl                  ; the first cell's data
        ld de,(cl_first)
        ld iy,(cl_step)         ; not used for a run of one cell
        ld ix,4
        ld b,2
        ld a,1                  ; the source as mapped now (RAM)
        call jt_vwrite
        pop hl
        jr .next
.slow:  ld a,e
        rst $00
        db $05                  ; OUT ($BF),A
        ld a,d
        rst $00
        db $05
        inc hl
        inc hl
        ld a,(hl)
        inc hl
        rst $00
        db $04                  ; OUT ($BE),A
        ld a,(hl)
        inc hl
        rst $00
        db $04
        jp .next
.done:  pop iy
        pop ix
        pop de
        pop bc
        pop hl
        ret
cl_start: dw 0
cl_first: dw 0
cl_prev:  dw 0
cl_step:  dw 0
; tiles3: as the game's $3953-$3A15. HL = the source (48 bytes in bank $0D,
; which the game maps at $8000), the VDP write address set. Builds the 96
; bytes in tbuf (each 2 source bytes, then 2 zero bytes) and writes them with
; one jt_vwrite call of 96 runs of one byte, steps 1, the form jt_vwrite runs
; fastest for tile data. Returns as the 48 OUTIs leave it: HL + 48, B - 48,
; C = $BE, A = 0.
tiles3: push bc
        push de
        push ix
        push iy
        ld de,tbuf
        ld bc,$18FF             ; B = 24 groups; the LDIs take only from C
.cp:    ldi
        ldi
        xor a
        ld (de),a
        inc de
        ld (de),a
        inc de
        djnz .cp
        push hl                 ; the source + 48
        ld hl,tbuf
        ld de,(vdp_addr)
        ld bc,$0160             ; 96 runs of one byte
        ld ix,1
        ld iy,1
        ld a,1                  ; the page's own bytes
        call jt_vwrite
        pop hl
        pop iy
        pop ix
        pop de
        pop bc
        ld a,b
        sub 48
        ld b,a
        ld c,$BE
        xor a
        ret
tbuf:   ds 96
; pal32: as the game's $0263-$0278, CRAM 0-7 from $007D and CRAM 8-31 from
; $D971; pal8p: as $BB9D-$BBAF and $BBC9-$BBDB, CRAM 0-7 from $D969. Both
; write only the entries whose colour differs from the runtime's copy
; (cram), and leave the VDP state as the game's writes would. pal32 returns
; HL = $D989, C = $BE, B - 32 and A = $C0; pal8p HL = $D971, B = 0 and
; A = the last byte, as the game's code leaves them. pal8p also stamps $DF06
; with isr_n and keeps in $DF07 the H that the lines above the split show
; (register 8 as the frame handler wrote it), for the rastercode routine.
pal32:  push de
        push bc
        ld hl,$007D
        ld de,p32buf
        ld bc,8
        ldir
        ld hl,$D971
        ld bc,24
        ldir
        ld hl,p32buf
        ld bc,$2000             ; 32 entries from index 0
        call cram_upd
        pop bc
        ld a,b
        sub 32
        ld b,a
        ld c,$BE
        ld hl,$D989
        ld a,$C0
        pop de
        ret
pal8p:  push de
        ld a,(isr_n)            ; stamp for the rastercode routine
        ld ($DF06),a
        ld a,(vdp_regs+8)       ; the status bar's H
        ld ($DF07),a
        ld hl,$D969
        ld bc,$0800             ; 8 entries from index 0
        call cram_upd
        ld a,($D970)
        pop de
        ret
; HL = the source, C = the first CRAM index, B = the entries. Each entry
; whose colour (low 6 bits) differs from cram gets the VDP address and a
; write through the I/O RST; then the VDP state is as B writes from index C
; leave it: address C + B, code 3, latch clear, read buffer the last byte.
; Returns HL past the source and B = 0; A, C, DE and F change.
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
p32buf: ds 32
; stat4: as the game's $BC08-$BC33: E to $385C and $3862, D to $389C and
; $38A2 (name table bytes), with two jt_vwrite calls, the last byte last.
; Returns A = D; keeps the other registers.
stat4:  push bc
        push hl
        push ix
        push iy
        ld hl,s4buf
        ld (hl),e
        inc hl
        ld (hl),e
        inc hl
        ld (hl),d
        inc hl
        ld (hl),d
        push de
        ld hl,s4buf
        ld de,$385C
        ld bc,$0102             ; 2 runs of one byte
        ld ix,1
        ld iy,6
        ld a,1                  ; the page's own bytes
        call jt_vwrite
        ld hl,s4buf+2
        ld de,$389C
        ld a,1
        call jt_vwrite
        pop de
        pop iy
        pop ix
        pop hl
        pop bc
        ld a,d
        ret
s4buf:  ds 4
; anim8: as the game's $BCDB-$BD0E. HL points at the colour byte C (bank 0).
; The game sets VRAM $27E4 and reads one byte before each write, so it
; writes C, $FF, C, $FF, C, $FF, C, $FF to $27E5, $27E7 ... $27F3: one
; jt_vwrite call of 8 runs of one byte, VRAM step 2. Returns B = $FF,
; C = the colour, A = $FF; keeps DE and HL.
anim8:  push de
        push ix
        push iy
        ld c,(hl)
        push hl
        ld hl,a8buf
        ld b,4
.f:     ld (hl),c
        inc hl
        ld (hl),$FF
        inc hl
        djnz .f
        push bc
        ld hl,a8buf
        ld de,$27E5
        ld bc,$0108             ; 8 runs of one byte
        ld ix,1
        ld iy,2
        ld a,1
        call jt_vwrite
        pop bc
        pop hl
        ld b,$FF
        ld a,b
        pop iy
        pop ix
        pop de
        ret
a8buf:  ds 8
endpage
# At power-on the game unpacks the Codemasters logo code from bank 9 ($8000-$8ACC)
# to RAM $C000 ($C000-$CF30) with its routine at $708B (CALL at $03DB) and runs
# it once (CALL $C003 at $03ED); its frame handler, in state 7 ($DBE3), calls
# $C000 (JP $CE71, the jingle) on each frame interrupt. It is Micro Machines'
# logo code, laid out at other addresses, paced with HALT in place of the V
# counter. Page 1 makes the RAM image use the runtime: the cave at $03E3, after
# the unpack, calls logo_patch, which checks the image and writes the I/O RST
# with its inline code over each of its 167 I/O instructions, and far calls
# over the HALTs that leave no room for one.
asm 003E3 7    ; LD A,$07 : LD ($DBE3),A : LD A,$0D
    rst $00
    db far_io, pg_logo_patch, ent_logo_patch
    ld a,$0D
endasm
page 1 logo_patch halt72 wait50 wait256 halt80 anim9 ltiles wtiles
; logo_patch: from the cave at $03E3, after the unpack. Checks the 3889 bytes
; from $C000 (two 16-bit sums, as Micro Machines' logo_patch) and writes into
; them: RST $00 and the inline code over each I/O instruction (io_at, io_code),
; RST $00 and eihalt_io over the two EI : HALT pairs, and a far call over the
; four HALTs that are one byte between other instructions (fars), and far
; calls over two loops of tile writes (caves: anim9, ltiles). A different
; image stops the game (jt_fatal). Then does what the cave replaced: state 7
; in $DBE3. Keeps BC, DE, HL, IX; A, F change.
logo_patch:
        push bc
        push de
        push hl
        push ix
        ld hl,$C000
        ld bc,3889
        ld de,0                 ; the sum of the bytes
        ld ix,0                 ; the sum of those sums
.ck:    ld a,(hl)
        add a,e
        ld e,a
        jr nc,.ck1
        inc d
.ck1:   add ix,de
        inc hl
        dec bc
        ld a,b
        or c
        jr nz,.ck
        ld hl,$6BE5
        or a
        sbc hl,de
        jr nz,.bad
        push ix
        pop hl
        ld de,$395E
        sbc hl,de
        jr nz,.bad
        ld hl,io_at
        ld de,io_code
        ld b,167
.io:    push bc
        ld c,(hl)
        inc hl
        ld b,(hl)
        inc hl                  ; BC = the instruction's RAM address
        ld a,$C7                ; RST $00
        ld (bc),a
        inc bc
        ld a,(de)
        inc de
        ld (bc),a
        pop bc
        djnz .io
        ld hl,$C008             ; EI : HALT
        ld (hl),$C7
        inc hl
        ld (hl),eihalt_io
        ld hl,$C063             ; EI : HALT (the 15-frame wait)
        ld (hl),$C7
        inc hl
        ld (hl),eihalt_io
        ld hl,fars
.fc:    ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,d
        or e
        jr z,.done
        ld bc,5
        ldir
        jr .fc
.done:  ld hl,caves
.cv:    ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,d
        or e
        jr z,.cvd
        ld bc,7
        ldir
        jr .cv
.cvd:   ld a,7
        ld ($DBE3),a
        pop ix
        pop hl
        pop de
        pop bc
        ret
.bad:   jp jt_fatal
; The far calls over the one-byte HALTs: RAM address, 5 bytes.
fars:   dw $C095                ; HALT : LD A,$72 : OUT ($BF),A
        db $C7, far_io, pg_halt72, ent_halt72, 0
        dw $C0A5                ; LD B,$32 : HALT : DJNZ $C0A7
        db $C7, far_io, pg_wait50, ent_wait50, 0
        dw $C38F                ; LD B,$00 : HALT : DJNZ $C391 (the cart test)
        db $C7, far_io, pg_wait256, ent_wait256, 0
        dw $C426                ; HALT : LD A,$80 : OUT ($BF),A (a logo step)
        db $C7, far_io, pg_halt80, ent_halt80, 0
        dw 0
; The far calls over whole loops: RAM address, far call, JP to the end.
caves:  dw $CEB7                ; LD B,$48 ... DJNZ $CEB9 (frame handler tiles)
        db $C7, far_io, pg_anim9, ent_anim9, $C3, $CC, $CE
        dw $C170                ; XOR A : OUT ($BF),A ... JR NZ,$C1A8 (tiles)
        db $C7, far_io, pg_ltiles, ent_ltiles, $C3, $B8, $C1
        dw 0
; halt72, halt80: HALT, then A = $72 or $80 and OUT ($BF),A, as the code they
; replace. wait50, wait256: 50 or 256 HALTs, B = 0 after, as LD B,n : HALT :
; DJNZ. Each HALT goes through the runtime (halt_io) with the game's interrupt
; state.
halt72: rst $00
        db halt_io
        ld a,$72
        rst $00
        db $05                  ; OUT ($BF),A
        ret
halt80: rst $00
        db halt_io
        ld a,$80
        rst $00
        db $05
        ret
wait50: ld b,$32
        jr waitb
wait256:
        ld b,0
waitb:  rst $00
        db halt_io
        djnz waitb
        ret
; The loops below build their bytes in ebuf, 128 bytes of SMS RAM that the
; game never writes ($DF10-$DF8F), and send them with jt_vwrite in runs of one
; byte, steps 1: with the source outside the code page, jt_vwrite writes tile
; data in its fast one-byte form.
EBUF    equ $DF10
; anim9: as the image's $CEB7-$CECB, which the frame handler runs on each
; frame interrupt while the logo runs: 9 tiles from 2-plane data, 72 rows of
; 4 bytes (2 source bytes, 0, then the OR of the two) to the VDP write
; address set. Through the I/O RST these 288 writes took about 340,000
; cycles a frame. Returns as the loop leaves the registers: HL + 144, B = 0,
; A = C = the last byte.
anim9:  push de
        ld de,EBUF
        ld b,72
.cp:    ld a,(hl)
        ld (de),a
        inc e
        ld c,a
        inc hl
        ld a,(hl)
        ld (de),a
        inc e
        inc hl
        or c
        ld c,a
        xor a
        ld (de),a
        inc e
        ld a,c
        ld (de),a
        inc e
        ld a,e
        cp 255&(EBUF+128)
        call z,eput
        djnz .cp
        call eput
        ld a,c
        pop de
        ret
; ltiles: as the image's $C170-$C1B6, run once at the logo's start with
; interrupts off: from VRAM $0000, 328 rows of $FF, 0, 0, 0; then 408 rows
; of 2 bytes from HL ($C4D7), 0, 0; then 384 rows of $FF, 1 byte from HL,
; 0, 0 (each OUTI also counts B down, so the DJNZ loops run 8 rows). Returns HL past the source, A = B = E = 0, C = $BE, D = $FF, as the
; loops leave them.
ltiles: ld hl,0
        call vset
        ld bc,328
.t1:    ld a,$FF
        ld (de),a
        inc e
        xor a
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld a,e
        cp 255&(EBUF+128)
        call z,eput
        dec bc
        ld a,b
        or c
        jr nz,.t1
        ld hl,$C4D7
        ld bc,408
.t2:    ld a,(hl)
        ld (de),a
        inc e
        inc hl
        ld a,(hl)
        ld (de),a
        inc e
        inc hl
        xor a
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld a,e
        cp 255&(EBUF+128)
        call z,eput
        dec bc
        ld a,b
        or c
        jr nz,.t2
        ld bc,384
.t3:    ld a,$FF
        ld (de),a
        inc e
        ld a,(hl)
        ld (de),a
        inc e
        inc hl
        xor a
        ld (de),a
        inc e
        ld (de),a
        inc e
        ld a,e
        cp 255&(EBUF+128)
        call z,eput
        dec bc
        ld a,b
        or c
        jr nz,.t3
        call eput
        ld bc,$00BE
        ld de,$FF00
        xor a
        ret
; wtiles: as the game's $A92F-$A97B (bank 9), which builds the wavy logo's
; 241 tiles with the display off after the Codemasters logo: from VRAM $0000,
; each tile 8 rows of 4 bytes, from two planes at IX and IX + 8 ($C12E on, 16
; bytes a tile): plane 0, plane 1, then for each of the two flags of the
; tile's entry in the table at $083E (index from HL, $BA90 on) the OR of the
; planes or 0. Through the I/O RST these 7,712 writes took about 9,000,000
; cycles. Returns as the loops leave the registers: B = 0, C kept, DE = the
; last row's planes, HL past the indexes, IX past the planes, A = the last
; byte.
wtiles: push bc
        ld hl,0
        call vset
        ld hl,$BA90
        ld ix,$C12E
        ld b,241
.t:     push bc
        push hl
        ld a,(hl)
        add a,a
        ld c,a
        ld b,0
        ld hl,$083E
        add hl,bc               ; the tile's two flags
        ld a,(hl)
        ld (wflag),a
        inc hl
        ld a,(hl)
        ld (wflag+1),a
        ld b,8
.r:     ld a,(ix+0)
        ld (de),a
        inc e
        ld c,a
        ld a,(ix+8)
        ld (de),a
        inc e
        or c
        ld c,a
        ld a,(wflag)
        or a
        jr z,.z0
        ld a,c
.z0:    ld (de),a
        inc e
        ld a,(wflag+1)
        or a
        jr z,.z1
        ld a,c
.z1:    ld (de),a
        inc e
        ld a,e
        cp 255&(EBUF+128)
        call z,eput
        inc ix
        djnz .r
        ld bc,8
        add ix,bc
        pop hl
        inc hl
        pop bc
        djnz .t
        call eput
        ld e,(ix-9)
        ld d,(ix-1)
        ld a,(wflag+1)
        or a
        jr z,.z2
        ld a,e
        or d
.z2:    pop bc
        ld b,0
        ret
wflag:  ds 2
; HL = VRAM address: the VDP state as a control write of it with code 1
; leaves it; DE = EBUF.
vset:   ld (vdp_addr),hl
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        ld de,EBUF
        ret
; DE = the end of the bytes in ebuf: they go to the VDP in one jt_vwrite
; call at the VDP address, and DE = EBUF. Keeps every other register except
; F.
eput:   push af
        ld a,e
        sub 255&EBUF            ; the byte count
        jr z,eputx              ; none
        push bc
        push hl
        push ix
        push iy
        ld c,a
        ld b,1
        ld ix,1
        ld iy,1
        ld hl,EBUF
        ld de,(vdp_addr)
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop iy
        pop ix
        pop hl
        pop bc
eputx:  ld de,EBUF
        pop af
        ret
; The RAM addresses of the image's I/O instructions, and their inline codes:
; OUT (n),A the port class of n (4 = $BE, 5 = $BF, 2 = $7E), IN A,($DC) $0E,
; and the second byte of the ED group (OTIR, OUTI, OUT (C),D, OUT (C),E).
io_at:
        dw $C011, $C017, $C01B, $C023, $C027, $C02B
        dw $C02F, $C033, $C036, $C03C, $C040, $C04B
        dw $C04F, $C09C, $C0A0, $C0A3, $C0D9, $C0DD
        dw $C0E9, $C0ED, $C0F4, $C0F8, $C122, $C126
        dw $C12E, $C132, $C136, $C13E, $C141, $C145
        dw $C149, $C14D, $C152, $C15B, $C15F, $C163
        dw $C167, $C16C, $C171, $C175, $C17E, $C181
        dw $C183, $C185, $C196, $C198, $C19A, $C19C
        dw $C1AB, $C1AD, $C1AF, $C1B1, $C1B8, $C1C1
        dw $C1C5, $C1CB, $C1CE, $C1D6, $C1DA, $C1E0
        dw $C1E3, $C1EB, $C1EF, $C1F5, $C1F9, $C200
        dw $C204, $C209, $C20D, $C214, $C218, $C21C
        dw $C220, $C224, $C228, $C22E, $C232, $C238
        dw $C23B, $C241, $C245, $C24B, $C24E, $C25A
        dw $C25D, $C27A, $C27E, $C2B8, $C2BC, $C2C0
        dw $C2C3, $C2E4, $C2E8, $C2EC, $C2EF, $C317
        dw $C31B, $C31F, $C322, $C32C, $C330, $C340
        dw $C343, $C347, $C34A, $C34E, $C352, $C356
        dw $C359, $C35C, $C35F, $C369, $C36D, $C371
        dw $C375, $C379, $C37D, $C381, $C385, $C387
        dw $C399, $C39D, $C3A1, $C3A5, $C3A9, $C3AD
        dw $C3B1, $C3B5, $C3B9, $C3BD, $C3C1, $C42D
        dw $C438, $C43C, $C441, $C444, $C447, $C44C
        dw $CA60, $CA64, $CA68, $CA6C, $CA7C, $CA85
        dw $CA8B, $CAAC, $CAAF, $CE96, $CE9A, $CEA0
        dw $CEA3, $CEBB, $CEBF, $CEC5, $CEC8, $CED0
        dw $CED3, $CEDD, $CEE6, $CEE9, $CEF9, $CEFC
        dw $CF06, $CF0A, $CF16, $CF19, $CF21
io_code:
        db $B3, $05, $05, $04, $04, $04, $04, $04, $04, $04, $04, $04, $04, $05, $04, $04
        db $04, $04, $04, $04, $04, $04, $05, $05, $B3, $05, $05, $B3, $05, $05, $04, $04
        db $04, $04, $04, $04, $04, $04, $05, $05, $04, $04, $04, $04, $A3, $A3, $51, $51
        db $51, $A3, $59, $59, $0E, $05, $05, $04, $04, $05, $05, $04, $04, $05, $05, $04
        db $04, $05, $05, $04, $04, $05, $05, $04, $04, $04, $04, $05, $05, $04, $04, $05
        db $05, $04, $04, $04, $04, $05, $05, $05, $05, $04, $04, $05, $05, $04, $04, $05
        db $05, $04, $04, $05, $05, $04, $04, $04, $04, $05, $05, $04, $04, $04, $04, $05
        db $05, $04, $05, $05, $04, $05, $05, $0E, $05, $05, $04, $05, $05, $04, $05, $05
        db $02, $02, $02, $05, $04, $04, $04, $05, $05, $B3, $02, $02, $02, $02, $02, $02
        db $02, $02, $02, $05, $05, $05, $05, $04, $04, $04, $04, $05, $05, $04, $05, $05
        db $04, $04, $05, $05, $05, $05, $04
endpage
asm 003A7 2   ; IM 1 -> IM 2
    im 2
endasm
asm 003F6 2   ; IM 1 -> IM 2
    im 2
endasm
site 00149   ; IN A,($BF)
site 00234   ; OUT ($BF),A
site 00238   ; OUT ($BF),A
site 0023D   ; OUT ($BF),A
site 00241   ; OUT ($BF),A
site 0027B   ; OUT ($BF),A
site 0027F   ; OUT ($BF),A
site 002EF   ; OUT ($BF),A
site 002F3   ; OUT ($BF),A
site 002F8   ; OUT ($BF),A
site 002FC   ; OUT ($BF),A
site 00316   ; OUT ($BF),A
site 0031A   ; OUT ($BF),A
site 00326   ; OUT ($BF),A
site 0032A   ; OUT ($BF),A
site 00339   ; OUT ($BF),A
site 0033D   ; OUT ($BF),A
site 00351   ; OUT ($BF),A
site 00355   ; OUT ($BF),A
site 00359   ; OUT ($BF),A
site 0035D   ; OUT ($BF),A
site 00370   ; OUT ($BF),A
site 00374   ; OUT ($BF),A
site 00382   ; OUT ($BF),A
site 00386   ; OUT ($BF),A
site 0038A   ; OUT ($BF),A
site 0038E   ; OUT ($BF),A
site 0039A   ; OUT ($BF),A
site 0039E   ; OUT ($BF),A
site 00411   ; OUT ($BF),A
site 00415   ; OUT ($BF),A
site 00418   ; OUT ($BF),A
site 0041C   ; OUT ($BF),A
site 00420   ; OUT ($BF),A
site 00424   ; OUT ($BF),A
site 0042A   ; OUT ($BE),A
site 0044F   ; OUT ($BF),A
site 00453   ; OUT ($BF),A
site 004A1   ; OUT ($BF),A
site 004A5   ; OUT ($BF),A
site 004B9   ; OUT ($BF),A
site 004BD   ; OUT ($BF),A
site 0059B   ; OUT ($BF),A
site 0059F   ; OUT ($BF),A
site 005DB   ; OUTI
site 005DD   ; OUTI
site 005DF   ; OUT ($BE),A
site 005E1   ; OUT ($BE),A
site 00601   ; OUTI
site 00603   ; OUTI
site 00605   ; OUT ($BE),A
site 00607   ; OUT ($BE),A
site 0062A   ; OUTI
site 0062C   ; OUTI
site 0062E   ; OUT ($BE),A
site 00630   ; OUT ($BE),A
site 0065B   ; OUT ($BF),A
site 0065F   ; OUT ($BF),A
site 0066C   ; OUT ($BF),A
site 00670   ; OUT ($BF),A
site 006CB   ; OUT ($BF),A
site 006CF   ; OUT ($BF),A
site 006D5   ; OUT ($BE),A
site 006DF   ; OUT ($BF),A
site 006E3   ; OUT ($BF),A
site 006E9   ; OUT ($BE),A
site 00701   ; IN A,($DC)
site 00712   ; IN A,($DD)
site 00720   ; IN A,($DD)
site 00743   ; OUT ($BF),A
site 00747   ; OUT ($BF),A
site 00753   ; OUT ($BF),A
site 00757   ; OUT ($BF),A
site 00CF1   ; OUT ($7E),A
site 00D01   ; OUT ($7E),A
site 00D11   ; OUT ($7E),A
site 00D1D   ; OUT ($7E),A
site 00D22   ; OUT ($7E),A
site 00D29   ; OUT ($7E),A
site 00D3B   ; OUT ($7E),A
site 00D4A   ; OUT ($7E),A
site 01C91   ; OUT ($BF),A
site 01C95   ; OUT ($BF),A
site 01CA2   ; OUT ($BE),A
site 01CA8   ; OUT ($BE),A
site 01CAB   ; OUT ($BE),A
site 01CAD   ; OUT ($BE),A
site 01CDE   ; OUT ($BF),A
site 01CE2   ; OUT ($BF),A
site 01CEC   ; OUT ($BE),A
site 01D82   ; OUT ($BF),A
site 01D86   ; OUT ($BF),A
site 01D91   ; OUT ($BE),A
site 01D94   ; OUT ($BE),A
site 01F48   ; OUT (C),E
site 01F4A   ; OUT (C),D
site 01F4E   ; OUT (C),E
site 01F50   ; OUT (C),D
site 01F54   ; OUT (C),E
site 01F56   ; OUT (C),D
site 01F5A   ; OUT (C),E
site 01F5C   ; OUT (C),D
site 01F60   ; OUT (C),E
site 01F62   ; OUT (C),D
site 01F66   ; OUT (C),E
site 01F68   ; OUT (C),D
site 01F6C   ; OUT (C),E
site 01F6E   ; OUT (C),D
site 01F72   ; OUT (C),E
site 01F74   ; OUT (C),D
site 01F78   ; OUT (C),E
site 01F7A   ; OUT (C),D
site 01F7E   ; OUT (C),E
site 01F80   ; OUT (C),D
site 01F84   ; OUT (C),E
site 01F86   ; OUT (C),D
site 01F8A   ; OUT (C),E
site 01F8C   ; OUT (C),D
site 01F90   ; OUT (C),E
site 01F92   ; OUT (C),D
site 01F96   ; OUT (C),E
site 01F98   ; OUT (C),D
site 01F9C   ; OUT (C),E
site 01F9E   ; OUT (C),D
site 01FA2   ; OUT (C),E
site 01FA4   ; OUT (C),D
site 01FA8   ; OUT (C),E
site 01FAA   ; OUT (C),D
site 01FAE   ; OUT (C),E
site 01FB0   ; OUT (C),D
site 01FB4   ; OUT (C),E
site 01FB6   ; OUT (C),D
site 01FBA   ; OUT (C),E
site 01FBC   ; OUT (C),D
site 01FC0   ; OUT (C),E
site 01FC2   ; OUT (C),D
site 01FC6   ; OUT (C),E
site 01FC8   ; OUT (C),D
site 01FCC   ; OUT (C),E
site 01FCE   ; OUT (C),D
site 01FD2   ; OUT (C),E
site 01FD4   ; OUT (C),D
site 01FD8   ; OUT (C),E
site 01FDA   ; OUT (C),D
site 01FDE   ; OUT (C),E
site 01FE0   ; OUT (C),D
site 01FE4   ; OUT (C),E
site 01FE6   ; OUT (C),D
site 01FEA   ; OUT (C),E
site 01FEC   ; OUT (C),D
site 01FF0   ; OUT (C),E
site 01FF2   ; OUT (C),D
site 01FF6   ; OUT (C),E
site 01FF8   ; OUT (C),D
site 01FFC   ; OUT (C),E
site 01FFE   ; OUT (C),D
site 02002   ; OUT (C),E
site 02004   ; OUT (C),D
site 02017   ; OUT (C),E
site 02019   ; OUT (C),D
site 0201D   ; OUT (C),E
site 0201F   ; OUT (C),D
site 02023   ; OUT (C),E
site 02025   ; OUT (C),D
site 02029   ; OUT (C),E
site 0202B   ; OUT (C),D
site 0202F   ; OUT (C),E
site 02031   ; OUT (C),D
site 02035   ; OUT (C),E
site 02037   ; OUT (C),D
site 0203B   ; OUT (C),E
site 0203D   ; OUT (C),D
site 02041   ; OUT (C),E
site 02043   ; OUT (C),D
site 02047   ; OUT (C),E
site 02049   ; OUT (C),D
site 0204D   ; OUT (C),E
site 0204F   ; OUT (C),D
site 02053   ; OUT (C),E
site 02055   ; OUT (C),D
site 02059   ; OUT (C),E
site 0205B   ; OUT (C),D
site 0205F   ; OUT (C),E
site 02061   ; OUT (C),D
site 02065   ; OUT (C),E
site 02067   ; OUT (C),D
site 0206B   ; OUT (C),E
site 0206D   ; OUT (C),D
site 02071   ; OUT (C),E
site 02073   ; OUT (C),D
site 02077   ; OUT (C),E
site 02079   ; OUT (C),D
site 0207D   ; OUT (C),E
site 0207F   ; OUT (C),D
site 02083   ; OUT (C),E
site 02085   ; OUT (C),D
site 02089   ; OUT (C),E
site 0208B   ; OUT (C),D
site 0208F   ; OUT (C),E
site 02091   ; OUT (C),D
site 02095   ; OUT (C),E
site 02097   ; OUT (C),D
site 0209B   ; OUT (C),E
site 0209D   ; OUT (C),D
site 020A1   ; OUT (C),E
site 020A3   ; OUT (C),D
site 020A7   ; OUT (C),E
site 020A9   ; OUT (C),D
site 020AD   ; OUT (C),E
site 020AF   ; OUT (C),D
site 020B3   ; OUT (C),E
site 020B5   ; OUT (C),D
site 020B9   ; OUT (C),E
site 020BB   ; OUT (C),D
site 020BF   ; OUT (C),E
site 020C1   ; OUT (C),D
site 020C5   ; OUT (C),E
site 020C7   ; OUT (C),D
site 020CB   ; OUT (C),E
site 020CD   ; OUT (C),D
site 020D1   ; OUT (C),E
site 020D3   ; OUT (C),D
site 020D7   ; OUT (C),E
site 020D9   ; OUT (C),D
site 020DD   ; OUT (C),E
site 020DF   ; OUT (C),D
site 020E3   ; OUT (C),E
site 020E5   ; OUT (C),D
site 020E9   ; OUT (C),E
site 020EB   ; OUT (C),D
site 020EF   ; OUT (C),E
site 020F1   ; OUT (C),D
site 020F5   ; OUT (C),E
site 020F7   ; OUT (C),D
site 020FB   ; OUT (C),E
site 020FD   ; OUT (C),D
site 02101   ; OUT (C),E
site 02103   ; OUT (C),D
site 02107   ; OUT (C),E
site 02109   ; OUT (C),D
site 0210D   ; OUT (C),E
site 0210F   ; OUT (C),D
site 02113   ; OUT (C),E
site 02115   ; OUT (C),D
site 02119   ; OUT (C),E
site 0211B   ; OUT (C),D
site 0211F   ; OUT (C),E
site 02121   ; OUT (C),D
site 02125   ; OUT (C),E
site 02127   ; OUT (C),D
site 0212B   ; OUT (C),E
site 0212D   ; OUT (C),D
site 02131   ; OUT (C),E
site 02133   ; OUT (C),D
site 02179   ; OUT ($BF),A
site 0217D   ; OUT ($BF),A
site 023B8   ; OUT ($BF),A
site 023BC   ; OUT ($BF),A
site 023F4   ; OUT ($BF),A
site 023F8   ; OUT ($BF),A
site 02422   ; OUT ($BF),A
site 02426   ; OUT ($BF),A
site 0248B   ; OUT ($BF),A
site 0248F   ; OUT ($BF),A
site 0249A   ; OUT ($BE),A
site 024A3   ; OUT ($BF),A
site 024A7   ; OUT ($BF),A
site 024B2   ; OUT ($BE),A
site 024BB   ; OUT ($BF),A
site 024BF   ; OUT ($BF),A
site 024CA   ; OUT ($BE),A
site 026B6   ; OUT ($BF),A
site 026BA   ; OUT ($BF),A
site 026C3   ; OUT ($BE),A
site 026C6   ; OUT ($BE),A
site 0275B   ; OUT ($BF),A
site 0275F   ; OUT ($BF),A
site 02764   ; OUT ($BE),A
site 02766   ; OUT ($BE),A
site 02768   ; OUT ($BE),A
site 0276A   ; OUT ($BE),A
site 0276C   ; OUT ($BE),A
site 0276E   ; OUT ($BE),A
site 02770   ; OUT ($BE),A
site 02772   ; OUT ($BE),A
site 0279F   ; OUT ($BF),A
site 027A2   ; OUT ($BF),A
site 027C3   ; OUT ($BF),A
site 027C6   ; OUT ($BF),A
site 027CA   ; OUT ($BE),A
site 027CD   ; OUT ($BE),A
site 027D1   ; OUT ($BE),A
site 027D4   ; OUT ($BE),A
site 027D8   ; OUT ($BE),A
site 027DB   ; OUT ($BE),A
site 027DF   ; OUT ($BE),A
site 027E2   ; OUT ($BE),A
site 02B83   ; OUT ($BF),A
site 02B87   ; OUT ($BF),A
site 02C38   ; OUT ($BF),A
site 02C3D   ; OUT ($BF),A
site 02C71   ; OUT ($BF),A
site 02C75   ; OUT ($BF),A
site 02D17   ; OUT ($BF),A
site 02D1B   ; OUT ($BF),A
site 02D3A   ; OUT ($BF),A
site 02D3E   ; OUT ($BF),A
site 02D68   ; OUT ($BF),A
site 02D6C   ; OUT ($BF),A
site 02E06   ; OUT ($BF),A
site 02E0A   ; OUT ($BF),A
site 02E27   ; OUT ($BF),A
site 02E2B   ; OUT ($BF),A
site 02E55   ; OUT ($BF),A
site 02E59   ; OUT ($BF),A
site 02EDE   ; OUT ($BF),A
site 02EE2   ; OUT ($BF),A
site 02EFC   ; OUT ($BF),A
site 02F00   ; OUT ($BF),A
site 02F2A   ; OUT ($BF),A
site 02F2E   ; OUT ($BF),A
site 02FC0   ; OUT ($BF),A
site 02FC4   ; OUT ($BF),A
site 02FDE   ; OUT ($BF),A
site 02FE2   ; OUT ($BF),A
site 02FEA   ; OUT ($BE),A
site 02FEC   ; OUT ($BE),A
site 02FF1   ; OUT ($BE),A
site 02FF4   ; OUT ($BE),A
site 02FFA   ; OUT ($BE),A
site 02FFC   ; OUT ($BE),A
site 0301A   ; OUT ($BF),A
site 0301E   ; OUT ($BF),A
site 03026   ; OUT ($BE),A
site 03028   ; OUT ($BE),A
site 0302A   ; OUT ($BE),A
site 0302C   ; OUT ($BE),A
site 0302E   ; OUT ($BE),A
site 03030   ; OUT ($BE),A
site 03032   ; OUT ($BE),A
site 03034   ; OUT ($BE),A
site 03036   ; OUT ($BE),A
site 03038   ; OUT ($BE),A
site 0303A   ; OUT ($BE),A
site 0303C   ; OUT ($BE),A
site 03041   ; OUT ($BE),A
site 03044   ; OUT ($BE),A
site 0304A   ; OUT ($BE),A
site 0304C   ; OUT ($BE),A
site 0304E   ; OUT ($BE),A
site 03050   ; OUT ($BE),A
site 03052   ; OUT ($BE),A
site 03054   ; OUT ($BE),A
site 03056   ; OUT ($BE),A
site 03058   ; OUT ($BE),A
site 0305A   ; OUT ($BE),A
site 0305C   ; OUT ($BE),A
site 0305E   ; OUT ($BE),A
site 03060   ; OUT ($BE),A
site 0321D   ; OUT ($BF),A
site 03220   ; OUT ($BF),A
site 03223   ; OUT ($BE),A
site 03226   ; OUT ($BE),A
site 0322D   ; OUT ($BF),A
site 03230   ; OUT ($BF),A
site 03233   ; OUT ($BE),A
site 03236   ; OUT ($BE),A
site 033B3   ; OUT ($BF),A
site 033B6   ; OUT ($BF),A
site 033B9   ; OUT ($BE),A
site 033BB   ; OUT ($BE),A
site 033CD   ; OUT ($BF),A
site 033D0   ; OUT ($BF),A
site 033D3   ; OUT ($BE),A
site 033E5   ; OUT ($BF),A
site 033E8   ; OUT ($BF),A
site 033EB   ; OUT ($BE),A
site 03670   ; OUT ($BF),A
site 03674   ; OUT ($BF),A
site 0367E   ; OUT ($BE),A
site 0369C   ; OUT ($BF),A
site 036A0   ; OUT ($BF),A
site 036AA   ; OUT ($BE),A
site 036AE   ; OUT ($BE),A
site 036B9   ; OUTI
site 036BB   ; OUTI
site 036BD   ; OUTI
site 036BF   ; OUTI
site 036C1   ; OUTI
site 036C3   ; OUTI
site 036C5   ; OUTI
site 036C7   ; OUTI
site 036C9   ; OUTI
site 036CB   ; OUTI
site 036CD   ; OUTI
site 036CF   ; OUTI
site 036D1   ; OUTI
site 036D3   ; OUTI
site 036D5   ; OUTI
site 036D7   ; OUTI
site 036D9   ; OUTI
site 036DB   ; OUTI
site 036DD   ; OUTI
site 036DF   ; OUTI
site 036E1   ; OUTI
site 036E3   ; OUTI
site 036E5   ; OUTI
site 036E7   ; OUTI
site 036E9   ; OUTI
site 036EB   ; OUTI
site 036ED   ; OUTI
site 036EF   ; OUTI
site 036F1   ; OUTI
site 036F3   ; OUTI
site 036F5   ; OUTI
site 036F7   ; OUTI
site 036F9   ; OUTI
site 036FB   ; OUTI
site 036FD   ; OUTI
site 036FF   ; OUTI
site 03701   ; OUTI
site 03703   ; OUTI
site 03705   ; OUTI
site 03707   ; OUTI
site 03709   ; OUTI
site 0370B   ; OUTI
site 0370D   ; OUTI
site 0370F   ; OUTI
site 03711   ; OUTI
site 03713   ; OUTI
site 03715   ; OUTI
site 03717   ; OUTI
site 03719   ; OUTI
site 0371B   ; OUTI
site 0371D   ; OUTI
site 0371F   ; OUTI
site 03721   ; OUTI
site 03723   ; OUTI
site 03725   ; OUTI
site 03727   ; OUTI
site 03729   ; OUTI
site 0372B   ; OUTI
site 0372D   ; OUTI
site 0372F   ; OUTI
site 03731   ; OUTI
site 03733   ; OUTI
site 03735   ; OUTI
site 03737   ; OUTI
site 03739   ; OUTI
site 0373B   ; OUTI
site 0373D   ; OUTI
site 0373F   ; OUTI
site 03741   ; OUTI
site 03743   ; OUTI
site 03745   ; OUTI
site 03747   ; OUTI
site 03749   ; OUTI
site 0374B   ; OUTI
site 0374D   ; OUTI
site 0374F   ; OUTI
site 03751   ; OUTI
site 03753   ; OUTI
site 03755   ; OUTI
site 03757   ; OUTI
site 03759   ; OUTI
site 0375B   ; OUTI
site 0375D   ; OUTI
site 0375F   ; OUTI
site 03761   ; OUTI
site 03763   ; OUTI
site 03765   ; OUTI
site 03767   ; OUTI
site 03769   ; OUTI
site 0376B   ; OUTI
site 0376D   ; OUTI
site 0376F   ; OUTI
site 03771   ; OUTI
site 03773   ; OUTI
site 03775   ; OUTI
site 03777   ; OUTI
site 03779   ; OUTI
site 0377B   ; OUTI
site 0377D   ; OUTI
site 0377F   ; OUTI
site 03781   ; OUTI
site 03783   ; OUTI
site 03785   ; OUTI
site 03787   ; OUTI
site 03789   ; OUTI
site 0378B   ; OUTI
site 0378D   ; OUTI
site 0378F   ; OUTI
site 03791   ; OUTI
site 03793   ; OUTI
site 03795   ; OUTI
site 03797   ; OUTI
site 03799   ; OUTI
site 0379B   ; OUTI
site 0379D   ; OUTI
site 0379F   ; OUTI
site 037A1   ; OUTI
site 037A3   ; OUTI
site 037A5   ; OUTI
site 037A7   ; OUTI
site 037A9   ; OUTI
site 037AB   ; OUTI
site 037AD   ; OUTI
site 037AF   ; OUTI
site 037B1   ; OUTI
site 037B3   ; OUTI
site 037B5   ; OUTI
site 037B7   ; OUTI
site 037BE   ; OUT ($BF),A
site 037C2   ; OUT ($BF),A
site 037C6   ; OUT ($BE),A
site 037C8   ; OUT ($BE),A
site 037CD   ; OUT ($BE),A
site 03838   ; OUT ($BF),A
site 0383D   ; OUT ($BF),A
site 03892   ; OUT ($BF),A
site 03897   ; OUT ($BF),A
site 03948   ; OUT ($BF),A
site 0394C   ; OUT ($BF),A
site 0395A   ; OUT ($BE),A
site 0395C   ; OUT ($BE),A
site 0395E   ; OUTI
site 03960   ; OUTI
site 03962   ; OUT ($BE),A
site 03964   ; OUT ($BE),A
site 03966   ; OUTI
site 03968   ; OUTI
site 0396A   ; OUT ($BE),A
site 0396C   ; OUT ($BE),A
site 0396E   ; OUTI
site 03970   ; OUTI
site 03972   ; OUT ($BE),A
site 03974   ; OUT ($BE),A
site 03976   ; OUTI
site 03978   ; OUTI
site 0397A   ; OUT ($BE),A
site 0397C   ; OUT ($BE),A
site 0397E   ; OUTI
site 03980   ; OUTI
site 03982   ; OUT ($BE),A
site 03984   ; OUT ($BE),A
site 03986   ; OUTI
site 03988   ; OUTI
site 0398A   ; OUT ($BE),A
site 0398C   ; OUT ($BE),A
site 0398E   ; OUTI
site 03990   ; OUTI
site 03992   ; OUT ($BE),A
site 03994   ; OUT ($BE),A
site 03996   ; OUTI
site 03998   ; OUTI
site 0399A   ; OUT ($BE),A
site 0399C   ; OUT ($BE),A
site 0399E   ; OUTI
site 039A0   ; OUTI
site 039A2   ; OUT ($BE),A
site 039A4   ; OUT ($BE),A
site 039A6   ; OUTI
site 039A8   ; OUTI
site 039AA   ; OUT ($BE),A
site 039AC   ; OUT ($BE),A
site 039AE   ; OUTI
site 039B0   ; OUTI
site 039B2   ; OUT ($BE),A
site 039B4   ; OUT ($BE),A
site 039B6   ; OUTI
site 039B8   ; OUTI
site 039BA   ; OUT ($BE),A
site 039BC   ; OUT ($BE),A
site 039BE   ; OUTI
site 039C0   ; OUTI
site 039C2   ; OUT ($BE),A
site 039C4   ; OUT ($BE),A
site 039C6   ; OUTI
site 039C8   ; OUTI
site 039CA   ; OUT ($BE),A
site 039CC   ; OUT ($BE),A
site 039CE   ; OUTI
site 039D0   ; OUTI
site 039D2   ; OUT ($BE),A
site 039D4   ; OUT ($BE),A
site 039D6   ; OUTI
site 039D8   ; OUTI
site 039DA   ; OUT ($BE),A
site 039DC   ; OUT ($BE),A
site 039DE   ; OUTI
site 039E0   ; OUTI
site 039E2   ; OUT ($BE),A
site 039E4   ; OUT ($BE),A
site 039E6   ; OUTI
site 039E8   ; OUTI
site 039EA   ; OUT ($BE),A
site 039EC   ; OUT ($BE),A
site 039EE   ; OUTI
site 039F0   ; OUTI
site 039F2   ; OUT ($BE),A
site 039F4   ; OUT ($BE),A
site 039F6   ; OUTI
site 039F8   ; OUTI
site 039FA   ; OUT ($BE),A
site 039FC   ; OUT ($BE),A
site 039FE   ; OUTI
site 03A00   ; OUTI
site 03A02   ; OUT ($BE),A
site 03A04   ; OUT ($BE),A
site 03A06   ; OUTI
site 03A08   ; OUTI
site 03A0A   ; OUT ($BE),A
site 03A0C   ; OUT ($BE),A
site 03A0E   ; OUTI
site 03A10   ; OUTI
site 03A12   ; OUT ($BE),A
site 03A14   ; OUT ($BE),A
site 03A25   ; OUT ($BF),A
site 03A29   ; OUT ($BF),A
site 03A37   ; OUT ($BF),A
site 03A3B   ; OUT ($BF),A
site 03DFF   ; OUT ($BF),A
site 03E03   ; OUT ($BF),A
site 03E08   ; OUT ($BF),A
site 03E0D   ; OUT ($BF),A
site 03E1A   ; OUT ($BE),A
site 03E26   ; OUT ($BF),A
site 03E2A   ; OUT ($BF),A
site 03E4C   ; OUT ($BF),A
site 03E50   ; OUT ($BF),A
site 03E54   ; OUT ($BF),A
site 03E58   ; OUT ($BF),A
site 03E63   ; OUT ($BE),A
site 03E6A   ; OUT ($BF),A
site 03E6E   ; OUT ($BF),A
site 03E74   ; OUT ($BF),A
site 03E78   ; OUT ($BF),A
site 03E7C   ; OUT ($BF),A
site 03E80   ; OUT ($BF),A
site 03E8B   ; OUT ($BE),A
site 03E92   ; OUT ($BF),A
site 03E96   ; OUT ($BF),A
site 03E9C   ; OUT ($BF),A
site 03EA0   ; OUT ($BF),A
site 03EA4   ; OUT ($BF),A
site 03EA8   ; OUT ($BF),A
site 03EB3   ; OUT ($BE),A
site 03EBA   ; OUT ($BF),A
site 03EBE   ; OUT ($BF),A
site 03EC4   ; OUT ($BF),A
site 03EC8   ; OUT ($BF),A
site 03ED0   ; OUT ($BE),A
site 03ED7   ; OUT ($BF),A
site 03EDB   ; OUT ($BF),A
site 03EE3   ; OUT ($BE),A
site 03EF5   ; OUT ($BF),A
site 03EF9   ; OUT ($BF),A
site 03F01   ; OUT ($BF),A
site 03F06   ; OUT ($BF),A
site 03F09   ; OUT ($BE),A
site 03F18   ; OUT ($BF),A
site 03F1C   ; OUT ($BF),A
site 03F59   ; OUT ($BF),A
site 03F5D   ; OUT ($BF),A
site 03F64   ; OUT ($BF),A
site 03F68   ; OUT ($BF),A
site 06FDF   ; OUT ($BF),A
site 06FE2   ; OUT ($BF),A
site 07006   ; OUT ($BE),A
site 0700C   ; OUT ($BE),A
site 0700F   ; OUT ($BE),A
site 07011   ; OUT ($BE),A
site 07038   ; OUT ($BF),A
site 0703B   ; OUT ($BF),A
site 0703E   ; OUT ($BE),A
site 07040   ; OUT ($BE),A
site 07053   ; OUT ($BF),A
site 07056   ; OUT ($BF),A
site 07059   ; OUT ($BE),A
site 0706B   ; OUT ($BF),A
site 0706E   ; OUT ($BF),A
site 07071   ; OUT ($BE),A
site 071D9   ; OUT ($BF),A
site 071DD   ; OUT ($BF),A
site 072F1   ; OUT ($BF),A
site 072F5   ; OUT ($BF),A
site 0B4A6   ; IN A,($DC)
site 0B4B0   ; IN A,($DD)
site 0B4D1   ; IN A,($DD)
site 0B707   ; OUT ($BF),A
site 0B70B   ; OUT ($BF),A
site 0B712   ; OTIR
site 0B73C   ; OUT ($BF),A
site 0B740   ; OUT ($BF),A
site 0B74B   ; OUT ($BE),A
site 0B74D   ; IN A,($BE)
site 0B754   ; OUT ($BF),A
site 0B758   ; OUT ($BF),A
site 0B763   ; OUT ($BE),A
site 0B765   ; IN A,($BE)
site 0B7B4   ; OUT ($BF),A
site 0B7B7   ; OUT ($BF),A
site 0B7BB   ; OUT ($BE),A
site 0B7BD   ; IN A,($BE)
site 0B7C1   ; OUT ($BE),A
site 0B7C3   ; IN A,($BE)
site 0B7C7   ; OUT ($BF),A
site 0B7CA   ; OUT ($BF),A
site 0B7CE   ; OUT ($BE),A
site 0B7D0   ; IN A,($BE)
site 0B7D4   ; OUT ($BE),A
site 0B7D8   ; OUT ($BF),A
site 0B7DB   ; OUT ($BF),A
site 0B7DF   ; OUT ($BE),A
site 0B7E1   ; IN A,($BE)
site 0B7E5   ; OUT ($BE),A
site 0B7E7   ; IN A,($BE)
site 0B7EB   ; OUT ($BF),A
site 0B7EE   ; OUT ($BF),A
site 0B7F2   ; OUT ($BE),A
site 0B7F4   ; IN A,($BE)
site 0B7F8   ; OUT ($BE),A
site 0BB87   ; IN A,($BF)
site 0BB96   ; IN A,($BF)
site 0BBB3   ; OUT ($BF),A
site 0BBB7   ; OUT ($BF),A
site 0BBBA   ; IN A,($BF)
site 0BBC3   ; OUT ($BF),A
site 0BBC7   ; OUT ($BF),A
site 0BBDF   ; OUT ($BF),A
site 0BBE3   ; OUT ($BF),A
site 0BBE7   ; OUT ($BF),A
site 0BBEB   ; OUT ($BF),A
site 0BC0E   ; OUT ($BF),A
site 0BC11   ; OUT ($BE),A
site 0BC15   ; OUT ($BF),A
site 0BC19   ; OUT ($BF),A
site 0BC1C   ; OUT ($BE),A
site 0BC20   ; OUT ($BF),A
site 0BC24   ; OUT ($BF),A
site 0BC27   ; OUT ($BE),A
site 0BC2B   ; OUT ($BF),A
site 0BC2F   ; OUT ($BF),A
site 0BC32   ; OUT ($BE),A
site 0BCE1   ; OUT ($BF),A
site 0BCE6   ; IN A,($BE)
site 0BCE9   ; OUT ($BE),A
site 0BCEB   ; IN A,($BE)
site 0BCEE   ; OUT ($BE),A
site 0BCF0   ; IN A,($BE)
site 0BCF3   ; OUT ($BE),A
site 0BCF5   ; IN A,($BE)
site 0BCF8   ; OUT ($BE),A
site 0BCFA   ; IN A,($BE)
site 0BCFD   ; OUT ($BE),A
site 0BCFF   ; IN A,($BE)
site 0BD02   ; OUT ($BE),A
site 0BD04   ; IN A,($BE)
site 0BD07   ; OUT ($BE),A
site 0BD09   ; IN A,($BE)
site 0BD0C   ; OUT ($BE),A
# After the Codemasters logo the game builds the wavy logo's tiles with the
# display off ($A92F-$A97B, bank 9): 7,712 writes through the I/O RST took
# about 16 frames. wtiles (page 1) writes them with jt_vwrite.
asm 2692F 77   ; LD A,$00 : OUT ($BF),A : LD A,$40 : OUT ($BF),A ... DJNZ $A940 (241 tiles)
    rst $00
    db far_io, pg_wtiles, ent_wtiles
    jp $A97C
endasm
site 2698B   ; OUT ($BF),A
site 2698F   ; OUT ($BF),A
site 26998   ; OUT ($BE),A
site 2699B   ; OUT ($BE),A
site 269A7   ; OUT ($BF),A
site 269AB   ; OUT ($BF),A
site 269B3   ; OTIR
site 269CD   ; OUT ($BF),A
site 269D1   ; OUT ($BF),A
site 269DC   ; OUT ($BE),A
site 269DE   ; OUT ($BE),A
site 269E0   ; OUT ($BE),A
site 269E2   ; OUT ($BE),A
site 269E4   ; OUT ($BE),A
site 269E6   ; OUT ($BE),A
site 269E8   ; OUT ($BE),A
site 269EA   ; OUT ($BE),A
site 26A3D   ; OUT ($BF),A
site 26A41   ; OUT ($BF),A
site 26AB9   ; OUT ($BF),A
site 26ABD   ; OUT ($BF),A
site 26B6B   ; OUT ($BF),A
site 26B6F   ; OUT ($BF),A
site 26BE0   ; OUT ($BF),A
site 26BE4   ; OUT ($BF),A
site 26BE7   ; OUT ($BE),A
site 26BEB   ; OUT ($BF),A
site 26BEF   ; OUT ($BF),A
site 26BFB   ; OUT ($BF),A
site 26BFE   ; OUT ($BF),A
site 26C1A   ; OUT ($BF),A
site 26C1E   ; OUT ($BF),A
site 26C22   ; OUT ($BE),A
site 26C82   ; OUT ($BF),A
site 26C86   ; OUT ($BF),A
site 26C89   ; OUT ($BE),A
site 26CE4   ; OUT ($BF),A
site 26CE8   ; OUT ($BF),A
site 26CFA   ; OUT ($BE),A
site 26D00   ; OUT ($BE),A
site 26D19   ; OUT ($BE),A
site 26D21   ; OUT ($BE),A
site 26D36   ; OUT ($BF),A
site 26D3A   ; OUT ($BF),A
site 26D42   ; OUT ($BE),A
site 26D48   ; OUT ($BF),A
site 26D4C   ; OUT ($BF),A
site 26DCC   ; OUT ($BF),A
site 26DD0   ; OUT ($BF),A
site 26DD6   ; OUT ($BF),A
site 26DDA   ; OUT ($BF),A
site 26DE1   ; OUT ($BF),A
site 26DE5   ; OUT ($BF),A
site 26DF2   ; OUT ($BF),A
site 26DF6   ; OUT ($BF),A
site 26E03   ; OUT ($BE),A
site 26E07   ; OUT ($BE),A
site 26E0A   ; OUT ($BE),A
site 27159   ; OUT ($BF),A
site 2715C   ; OUT ($BF),A
site 27162   ; OUT ($BE),A
site 27165   ; OUT ($BE),A
site 27169   ; OUT ($BE),A
site 2716C   ; OUT ($BE),A
site 27170   ; OUT ($BE),A
site 27173   ; OUT ($BE),A
site 27177   ; OUT ($BE),A
site 2717A   ; OUT ($BE),A
site 2717E   ; OUT ($BE),A
site 27181   ; OUT ($BE),A
site 27185   ; OUT ($BE),A
site 27188   ; OUT ($BE),A
site 2E266   ; OUT ($BF),A
site 2E26A   ; OUT ($BF),A
site 2E273   ; OUT ($BE),A
site 2E27D   ; OUT ($BF),A
site 2E281   ; OUT ($BF),A
site 2E287   ; OUT ($BE),A
site 2E289   ; OUT ($BE),A
site 2E28B   ; OUT ($BE),A
site 2E28E   ; OUT ($BE),A
site 2E29D   ; OUT ($BF),A
site 2E2A1   ; OUT ($BF),A
site 2E2AB   ; OUT ($BE),A
site 2E2AE   ; OUT ($BE),A
site 2E2BD   ; OUT ($BF),A
site 2E2C0   ; OUT ($BF),A
site 2E2C6   ; OUT ($BE),A
site 2E2C9   ; OUT ($BE),A
site 2E2E2   ; OUT ($BF),A
site 2E2E5   ; OUT ($BF),A
site 2E2EB   ; OUT ($BE),A
site 2E2EE   ; OUT ($BE),A
site 2E2FC   ; OUT ($BF),A
site 2E300   ; OUT ($BF),A
site 2E308   ; IN A,($BE)
site 2E30A   ; IN A,($BE)
site 2E320   ; OUT ($BF),A
site 2E324   ; OUT ($BF),A
site 2E32D   ; OUT ($BE),A
site 2E331   ; OUT ($BE),A
site 2E335   ; OUT ($BE),A
site 2E33A   ; OUT ($BE),A
site 2E345   ; OUT ($BF),A
site 2E349   ; OUT ($BF),A
site 2E351   ; IN A,($BE)
site 2E353   ; IN A,($BE)
site 2E35F   ; OUT ($BF),A
site 2E363   ; OUT ($BF),A
site 2E36C   ; OUT ($BE),A
site 2E370   ; OUT ($BE),A
site 2E374   ; OUT ($BE),A
site 2E379   ; OUT ($BE),A
site 2E384   ; OUT ($BF),A
site 2E388   ; OUT ($BF),A
site 2E390   ; IN A,($BE)
site 2E392   ; IN A,($BE)
site 2E39E   ; OUT ($BF),A
site 2E3A2   ; OUT ($BF),A
site 2E3AD   ; OUT ($BE),A
site 2E3B0   ; OUT ($BE),A
site 2E3B2   ; OUT ($BE),A
site 2E3B4   ; OUT ($BE),A
site 2E3C0   ; OUT ($BE),A
site 2E3C2   ; OUT ($BE),A
site 2E3C4   ; OUT ($BE),A
site 2E3C6   ; OUT ($BE),A
site 2E3CD   ; OUT ($BF),A
site 2E3D1   ; OUT ($BF),A
site 2E3D6   ; OUT ($BE),A
site 2E3DC   ; OUT ($BF),A
site 2E3E0   ; OUT ($BF),A
site 2E3EF   ; OUT ($BE),A
site 2E3F4   ; OUT ($BE),A
site 2E3F7   ; OUT ($BE),A
site 2E3F9   ; OUT ($BE),A
site 2E435   ; OUT ($BF),A
site 2E439   ; OUT ($BF),A
site 2E441   ; OUT ($BE),A
site 2E481   ; OUT ($BF),A
site 2E484   ; OUT ($BF),A
site 2E48B   ; OUT ($BE),A
site 2E48E   ; OUT ($BE),A
site 2E4E9   ; OUT ($BF),A
site 2E4ED   ; OUT ($BF),A
site 2E4F5   ; OTIR
site 2E525   ; OUT ($BF),A
site 2E529   ; OUT ($BF),A
site 2E556   ; OUT ($BF),A
site 2E55A   ; OUT ($BF),A
site 2E579   ; OUT ($BF),A
site 2E57D   ; OUT ($BF),A
site 2E593   ; OUT ($BE),A
site 2E5AC   ; OUT ($BF),A
site 2E5B0   ; OUT ($BF),A
site 2E681   ; OUT ($BF),A
site 2E685   ; OUT ($BF),A
site 2E69E   ; OUT ($BF),A
site 2E6A2   ; OUT ($BF),A
site 2E93A   ; OUT ($BF),A
site 2E93E   ; OUT ($BF),A
site 2E940   ; IN A,($7E)
site 2E949   ; OUT ($BF),A
site 2E94D   ; OUT ($BF),A
site 2E94F   ; IN A,($7E)
site 2E958   ; OUT ($BF),A
site 2E95C   ; OUT ($BF),A
site 2E95E   ; IN A,($7E)
site 2E967   ; OUT ($BF),A
site 2E96B   ; OUT ($BF),A
site 2E96D   ; IN A,($7E)
site 2E974   ; OUT ($BF),A
site 2E978   ; OUT ($BF),A
site 2EC5F   ; OUT ($BF),A
site 2EC62   ; OUT ($BF),A
site 2EC6A   ; OUT ($BE),A
site 2EC6D   ; OUT ($BE),A
site 2EE18   ; OUT ($BF),A
site 2EE1C   ; OUT ($BF),A
site 2EE28   ; OUT ($BF),A
site 2EE2C   ; OUT ($BF),A
site 2EE4D   ; OUT ($BF),A
site 2EE50   ; OUT ($BF),A
site 2EE55   ; OUT ($BE),A
site 2EE57   ; OUT ($BE),A
site 2EE66   ; OUT ($BF),A
site 2EE69   ; OUT ($BF),A
site 2EE6E   ; OUT ($BE),A
site 2EE70   ; OUT ($BE),A
site 2EF0F   ; OUT ($BF),A
site 2EF12   ; OUT ($BF),A
site 2EF2A   ; OUT ($BE),A
site 2EF2D   ; OUT ($BE),A
site 2EF30   ; IN A,($BE)
site 2EF32   ; IN A,($BE)
site 2F16C   ; OUT ($BF),A
site 2F170   ; OUT ($BF),A
site 2F178   ; OTIR
site 2F1A2   ; OUT ($BF),A
site 2F1A6   ; OUT ($BF),A
site 2F1C3   ; OUT ($BF),A
site 2F1C7   ; OUT ($BF),A
site 2F1F8   ; OUT ($BF),A
site 2F1FC   ; OUT ($BF),A
site 2F209   ; OUT ($BF),A
site 2F20D   ; OUT ($BF),A
site 2F225   ; OUT ($BE),A
site 2F407   ; OUT ($BE),A
site 2F40C   ; OUT ($BE),A
site 2F417   ; OUT ($BE),A
site 2F420   ; OUT ($BE),A
site 2F460   ; OUT ($BF),A
site 2F464   ; OUT ($BF),A
site 2F466   ; IN A,($7E)
site 2F46F   ; OUT ($BF),A
site 2F473   ; OUT ($BF),A
site 2F475   ; IN A,($7E)
site 2F47E   ; OUT ($BF),A
site 2F482   ; OUT ($BF),A
site 2F484   ; IN A,($7E)
site 2F48D   ; OUT ($BF),A
site 2F491   ; OUT ($BF),A
site 2F493   ; IN A,($7E)
site 2F49A   ; OUT ($BF),A
site 2F49E   ; OUT ($BF),A
site 2F536   ; OUT ($BF),A
site 2F53A   ; OUT ($BF),A
site 2F54C   ; OUT ($BE),A
site 2F552   ; OUT ($BE),A
site 2F56B   ; OUT ($BE),A
site 2F573   ; OUT ($BE),A
site 2F6C7   ; OUT ($BF),A
site 2F6CB   ; OUT ($BF),A
site 314E1   ; OUT ($BF),A
site 314E4   ; OUT ($BF),A
site 314E8   ; IN A,($BE)
site 314EA   ; IN A,($BE)
site 314ED   ; OUT ($BE),A
site 314F1   ; OUT ($BE),A
site 31535   ; OUT ($BF),A
site 31538   ; OUT ($BF),A
site 3155B   ; OUT ($BE),A
site 31560   ; OUT ($BE),A
site 31563   ; OUT ($BE),A
site 31566   ; OUT ($BE),A
site 31571   ; OUT ($BE),A
site 31576   ; OUT ($BE),A
site 3157A   ; OUT ($BE),A
site 3157D   ; OUT ($BE),A
site 31588   ; OUT ($BE),A
site 3158D   ; OUT ($BE),A
site 31590   ; OUT ($BE),A
site 31594   ; OUT ($BE),A
site 3159F   ; OUT ($BE),A
site 315A4   ; OUT ($BE),A
site 315A8   ; OUT ($BE),A
site 315AA   ; OUT ($BE),A
site 315B4   ; OUT ($BF),A
site 315B8   ; OUT ($BF),A
site 315C2   ; OUT ($BE),A
site 315C7   ; OUT ($BE),A
site 315CA   ; OUT ($BE),A
site 315CC   ; OUT ($BE),A
site 3165E   ; OUT ($BF),A
site 31662   ; OUT ($BF),A
site 3166E   ; OUT ($BF),A
site 31672   ; OUT ($BF),A
site 3167E   ; OUT ($BF),A
site 31682   ; OUT ($BF),A
site 3173B   ; OUT ($BF),A
site 3173F   ; OUT ($BF),A
site 31747   ; OUT ($BE),A
site 3174E   ; OUT ($BF),A
site 31752   ; OUT ($BF),A
site 31759   ; OUT ($BF),A
site 3175D   ; OUT ($BF),A
site 31764   ; OUT ($BF),A
site 31768   ; OUT ($BF),A
site 3176F   ; OUT ($BF),A
site 31773   ; OUT ($BF),A
site 3177A   ; OUT ($BF),A
site 3177E   ; OUT ($BF),A
site 31785   ; OUT ($BF),A
site 31789   ; OUT ($BF),A
site 31790   ; OUT ($BF),A
site 31794   ; OUT ($BF),A
site 3179B   ; OUT ($BF),A
site 3179F   ; OUT ($BF),A
site 317A6   ; OUT ($BF),A
site 317AA   ; OUT ($BF),A
site 317B5   ; OUT ($BE),A
site 317B8   ; OUT ($BE),A
site 317BE   ; OUT ($BE),A
site 317C0   ; OUT ($BE),A
site 317C9   ; OUT ($BE),A
site 317CB   ; OUT ($BE),A
site 317CF   ; OUT ($BE),A
site 317D1   ; OUT ($BE),A
site 317D8   ; OUT ($BE),A
site 317DB   ; OUT ($BE),A
site 317DF   ; OUT ($BE),A
site 317E3   ; OUT ($BE),A
site 317EB   ; OUT ($BF),A
site 317EF   ; OUT ($BF),A
site 317FA   ; OUT ($BE),A
site 317FD   ; OUT ($BE),A
site 31801   ; OUT ($BE),A
site 31805   ; OUT ($BE),A
site 3180D   ; OUT ($BF),A
site 31811   ; OUT ($BF),A
site 31813   ; IN A,($BE)
site 3181A   ; IN A,($BE)
site 31836   ; OUT ($BF),A
site 3183A   ; OUT ($BF),A
site 31842   ; OUT ($BE),A
site 31849   ; OUT ($BF),A
site 3184D   ; OUT ($BF),A
site 3184F   ; IN A,($BE)
site 31856   ; IN A,($BE)
site 31872   ; OUT ($BF),A
site 31876   ; OUT ($BF),A
site 3187E   ; OUT ($BE),A
site 318BF   ; OUT ($BF),A
site 318C3   ; OUT ($BF),A
site 318CB   ; OUT ($BE),A
site 318CE   ; OUT ($BE),A
site 318D1   ; OUT ($BE),A
site 318D3   ; OUT ($BE),A
site 318DA   ; OUT ($BF),A
site 318DE   ; OUT ($BF),A
site 318E3   ; OUT ($BE),A
site 318E6   ; OUT ($BE),A
site 318E9   ; OUT ($BE),A
site 318EB   ; OUT ($BE),A
site 3199E   ; OUT ($BF),A
site 319A2   ; OUT ($BF),A
site 319A5   ; OUT ($BF),A
site 319A9   ; OUT ($BF),A
site 319B5   ; OUT ($BF),A
site 319B8   ; OUT ($BF),A
site 319BC   ; OUT ($BE),A
site 319C0   ; OUT ($BE),A
site 319CE   ; OUT ($BF),A
site 319D1   ; OUT ($BF),A
site 319D5   ; OUT ($BE),A
site 319D9   ; OUT ($BE),A
site 319E3   ; OUT ($BF),A
site 319E7   ; OUT ($BF),A
site 31EE7   ; OUT ($BF),A
site 31EEA   ; OUT ($BF),A
site 31EEF   ; OUT ($BE),A
site 31EF2   ; OUT ($BE),A
site 31F00   ; OUT ($BF),A
site 31F04   ; OUT ($BF),A
site 31F08   ; OUT ($BE),A
site 31F0C   ; OUT ($BE),A
site 31F10   ; OUT ($BE),A
site 31F14   ; OUT ($BE),A
site 31F18   ; OUT ($BF),A
site 31F1C   ; OUT ($BF),A
site 31F20   ; OUT ($BE),A
site 31F24   ; OUT ($BE),A
site 31F28   ; OUT ($BE),A
site 31F2C   ; OUT ($BE),A
site 31F3B   ; OUT ($BF),A
site 31F3F   ; OUT ($BF),A
site 31F46   ; OUT ($BF),A
site 31F4A   ; OUT ($BF),A
site 320EE   ; OUT ($BF),A
site 320F1   ; OUT ($BF),A
site 320F3   ; IN A,($BE)
site 320F5   ; IN A,($BE)
site 320F8   ; OUT ($BE),A
site 320FA   ; IN A,($BE)
site 320FD   ; OUT ($BE),A
site 32125   ; OUT ($BF),A
site 32128   ; OUT ($BF),A
site 3212A   ; IN A,($BE)
site 3212C   ; IN A,($BE)
site 3212F   ; OUT ($BE),A
site 32131   ; IN A,($BE)
site 32134   ; OUT ($BE),A
site 3221D   ; OUT ($BF),A
site 32221   ; OUT ($BF),A
site 3222C   ; OUT ($BE),A
site 3222F   ; OUT ($BE),A
site 32232   ; OUT ($BE),A
site 32234   ; OUT ($BE),A
site 3246B   ; IN A,($BE)
site 32473   ; IN A,($BE)
site 324B0   ; OUT ($BE),A
site 324BC   ; OUT ($BF),A
site 324C0   ; OUT ($BF),A
site 324C4   ; IN A,($BE)
site 324C6   ; IN A,($BE)
site 324CA   ; OUT ($BE),A
site 324CE   ; OUT ($BE),A
site 324D4   ; IN A,($BE)
site 324D6   ; IN A,($BE)
site 324D8   ; IN A,($BE)
site 324DC   ; OUT ($BE),A
site 324E2   ; OUT ($BF),A
site 324E6   ; OUT ($BF),A
site 324ED   ; OUT ($BF),A
site 324F1   ; OUT ($BF),A
site 324F8   ; OUT ($BF),A
site 324FC   ; OUT ($BF),A
site 32503   ; OUT ($BF),A
site 32507   ; OUT ($BF),A
site 3250E   ; OUT ($BF),A
site 32512   ; OUT ($BF),A
site 32519   ; OUT ($BF),A
site 3251D   ; OUT ($BF),A
site 32524   ; OUT ($BF),A
site 32528   ; OUT ($BF),A
site 3252C   ; IN A,($BE)
site 3252E   ; IN A,($BE)
site 32531   ; OUT ($BE),A
site 32535   ; OUT ($BE),A
site 3253B   ; OUT ($BF),A
site 3253F   ; OUT ($BF),A
site 32543   ; IN A,($BE)
site 32545   ; IN A,($BE)
site 32548   ; OUT ($BE),A
site 3254C   ; OUT ($BE),A
site 32552   ; OUT ($BF),A
site 32556   ; OUT ($BF),A
site 3255A   ; IN A,($BE)
site 3255C   ; IN A,($BE)
site 3255F   ; OUT ($BE),A
site 32563   ; OUT ($BE),A
site 32569   ; OUT ($BF),A
site 3256D   ; OUT ($BF),A
site 32571   ; IN A,($BE)
site 32573   ; IN A,($BE)
site 32576   ; OUT ($BE),A
site 3257A   ; OUT ($BE),A
site 32580   ; OUT ($BF),A
site 32584   ; OUT ($BF),A
site 3258A   ; OUT ($BE),A
site 3258C   ; OUT ($BE),A
site 3258F   ; OUT ($BE),A
site 32593   ; OUT ($BE),A
site 3259B   ; OUT ($BE),A
site 3259D   ; OUT ($BE),A
site 325A0   ; OUT ($BE),A
site 325A2   ; OUT ($BE),A
site 325A9   ; IN A,($BE)
site 325AB   ; IN A,($BE)
site 325AF   ; OUT ($BE),A
site 325B1   ; OUT ($BE),A
site 325B8   ; OUT ($BF),A
site 325BC   ; OUT ($BF),A
site 325C4   ; OUT ($BE),A
site 325C7   ; OUT ($BE),A
site 325D5   ; OUT ($BE),A
site 325D9   ; OUT ($BE),A
codem 001B9   ; LD ($8000),A
codem 001D0   ; LD ($8000),A
codem 001E9   ; LD ($8000),A
codem 00217   ; LD ($8000),A
codem 0022F   ; LD ($8000),A
codem 003BA   ; LD ($0000),A
codem 003BE   ; LD ($4000),A
codem 003C2   ; LD ($8000),A
codem 003D2   ; LD ($8000),A
codem 003E0   ; LD ($8000),A
codem 003EA   ; LD ($8000),A
codem 003F2   ; LD ($8000),A
codem 0045A   ; LD ($8000),A
codem 00462   ; LD ($8000),A
codem 005B2   ; LD ($8000),A
codem 005BC   ; LD ($8000),A
codem 005C6   ; LD ($8000),A
codem 005D0   ; LD ($8000),A
codem 005E7   ; LD ($8000),A
codem 005F9   ; LD ($8000),A
codem 00610   ; LD ($8000),A
codem 00622   ; LD ($8000),A
codem 00636   ; LD ($8000),A
codem 009F0   ; LD ($8000),A
codem 00A3B   ; LD ($8000),A
codem 00A41   ; LD ($8000),A
codem 00CBF   ; LD ($8000),A
codem 00D2D   ; LD ($8000),A
codem 01C10   ; LD ($8000),A
codem 01C32   ; LD ($8000),A
codem 01C7D   ; LD ($8000),A
codem 01C89   ; LD ($8000),A
codem 01CC8   ; LD ($8000),A
codem 01CD6   ; LD ($8000),A
codem 01D06   ; LD ($8000),A
codem 01D19   ; LD ($8000),A
codem 01D25   ; LD ($8000),A
codem 01D30   ; LD ($8000),A
codem 01D44   ; LD ($8000),A
codem 01D4F   ; LD ($8000),A
codem 01D6C   ; LD ($8000),A
codem 01D7A   ; LD ($8000),A
codem 0228C   ; LD ($8000),A
codem 0229E   ; LD ($8000),A
codem 02341   ; LD ($8000),A
codem 02353   ; LD ($8000),A
codem 023E1   ; LD ($8000),A
codem 023EF   ; LD ($8000),A
codem 0240F   ; LD ($8000),A
codem 0241D   ; LD ($8000),A
codem 026A1   ; LD ($8000),A
codem 026AF   ; LD ($8000),A
codem 026E0   ; LD ($8000),A
codem 0272D   ; LD ($8000),A
codem 02784   ; LD ($8000),A
codem 0278D   ; LD ($8000),A
codem 02798   ; LD ($8000),A
codem 027ED   ; LD ($8000),A
codem 02807   ; LD ($8000),A
codem 02836   ; LD ($8000),A
codem 02850   ; LD ($8000),A
codem 02857   ; LD ($8000),A
codem 02866   ; LD ($8000),A
codem 0286D   ; LD ($8000),A
codem 0287C   ; LD ($8000),A
codem 02883   ; LD ($8000),A
codem 02892   ; LD ($8000),A
codem 02B2A   ; LD ($8000),A
codem 02B33   ; LD ($8000),A
codem 02C41   ; LD ($8000),A
codem 02C54   ; LD ($8000),A
codem 02D27   ; LD ($8000),A
codem 02D35   ; LD ($8000),A
codem 02D55   ; LD ($8000),A
codem 02D63   ; LD ($8000),A
codem 02D90   ; LD ($8000),A
codem 02D9E   ; LD ($8000),A
codem 02E14   ; LD ($8000),A
codem 02E22   ; LD ($8000),A
codem 02E42   ; LD ($8000),A
codem 02E50   ; LD ($8000),A
codem 02E7E   ; LD ($8000),A
codem 02E89   ; LD ($8000),A
codem 02EE9   ; LD ($8000),A
codem 02EF7   ; LD ($8000),A
codem 02F17   ; LD ($8000),A
codem 02F25   ; LD ($8000),A
codem 02F54   ; LD ($8000),A
codem 02F62   ; LD ($8000),A
codem 02FC9   ; LD ($8000),A
codem 02FD7   ; LD ($8000),A
codem 03005   ; LD ($8000),A
codem 03013   ; LD ($8000),A
codem 0329C   ; LD ($8000),A
codem 032AC   ; LD ($8000),A
codem 03569   ; LD ($8000),A
codem 035A3   ; LD ($8000),A
codem 035B5   ; LD ($8000),A
codem 035FE   ; LD ($8000),A
codem 0360F   ; LD ($8000),A
codem 0365D   ; LD ($8000),A
codem 0366B   ; LD ($8000),A
codem 03689   ; LD ($8000),A
codem 03697   ; LD ($8000),A
codem 037F2   ; LD ($8000),A
codem 03800   ; LD ($8000),A
codem 038C5   ; LD ($8000),A
codem 038DE   ; LD ($8000),A
codem 038F1   ; LD ($8000),A
codem 03950   ; LD ($8000),A
codem 03A18   ; LD ($8000),A
codem 03A42   ; LD ($8000),A
codem 03A9B   ; LD ($8000),A
codem 03ABB   ; LD ($8000),A
codem 03B20   ; LD ($8000),A
codem 03B65   ; LD ($8000),A
codem 03E11   ; LD ($8000),A
codem 03E21   ; LD ($8000),A
codem 03E45   ; LD ($8000),A
codem 03FAF   ; LD ($8000),A
codem 06378   ; LD ($8000),A
codem 0638D   ; LD ($8000),A
codem 06F22   ; LD ($8000),A
codem 06F32   ; LD ($8000),A
codem 06F40   ; LD ($8000),A
codem 06F50   ; LD ($8000),A
codem 06FA6   ; LD ($8000),A
codem 06FB1   ; LD ($8000),A
codem 0707F   ; LD ($8000),A
codem 07087   ; LD ($8000),A
codem 07209   ; LD ($8000),A
codem 0721F   ; LD ($8000),A
codem 07304   ; LD ($8000),A
codem 07325   ; LD ($8000),A
codem 0733A   ; LD ($8000),A
# CHECK cartarea_store at 02209 ($2209 bank 0): 32 AE 04  LD ($04AE),A $04AE
# CHECK ram_exec at 001FE ($01FE bank 0): CD 00 C0  CALL $C000 $C000
# CHECK ram_exec at 003ED ($03ED bank 0): CD 03 C0  CALL $C003 $C003
# CHECK indirect_unresolved at 01F29 ($1F29 bank 0): C9  RET 
# CHECK indirect_unresolved at 0200B ($200B bank 0): C9  RET 
# CHECK indirect_unresolved at 0213A ($213A bank 0): C9  RET 
# CHECK indirect_unresolved at 02B78 ($2B78 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 02B78 ($2B78 bank 0): E9  JP (HL) 
# CHECK indirect_unresolved at 06F93 ($6F93 bank 1): E9  JP (HL) 
# CHECK bank_unresolved at 00257 ($0257 bank 0): CD FD B6  CALL $B6FD $B6FD
# CHECK bank_unresolved at 0025A ($025A bank 0): CD C8 BC  CALL $BCC8 $BCC8
# CHECK bank_unresolved at 0025D ($025D bank 0): CD EE BB  CALL $BBEE $BBEE
# CHECK bank_unresolved at 0028F ($028F bank 0): CD D3 B5  CALL $B5D3 $B5D3
# CHECK bank_unresolved at 00292 ($0292 bank 0): CD 32 BB  CALL $BB32 $BB32
# CHECK bank_unresolved at 0029C ($029C bank 0): CD A2 B4  CALL $B4A2 $B4A2
# CHECK bank_unresolved at 0029F ($029F bank 0): CD EA B6  CALL $B6EA $B6EA
# CHECK bank_unresolved at 002A2 ($02A2 bank 0): CD 35 B5  CALL $B535 $B535
# CHECK bank_unresolved at 002A5 ($02A5 bank 0): CD 30 B9  CALL $B930 $B930
# CHECK bank_unresolved at 002A8 ($02A8 bank 0): CD 35 BC  CALL $BC35 $BC35
# CHECK bank_unresolved at 002B1 ($02B1 bank 0): CD 87 BB  CALL $BB87 $BB87
# CHECK bank_unresolved at 002C2 ($02C2 bank 0): CD A2 B4  CALL $B4A2 $B4A2
# CHECK bank_unresolved at 002C5 ($02C5 bank 0): CD EA B6  CALL $B6EA $B6EA
# CHECK bank_unresolved at 002C8 ($02C8 bank 0): CD 35 B5  CALL $B535 $B535
# CHECK bank_unresolved at 002CB ($02CB bank 0): CD 30 B9  CALL $B930 $B930
# CHECK bank_unresolved at 002CE ($02CE bank 0): CD 35 BC  CALL $BC35 $BC35
# CHECK bank_unresolved at 002DE ($02DE bank 0): CD 9A B5  CALL $B59A $B59A
# CHECK bank_unresolved at 002E1 ($02E1 bank 0): CD 81 B8  CALL $B881 $B881
# CHECK bank_unresolved at 002E7 ($02E7 bank 0): CD 87 BB  CALL $BB87 $BB87
# CHECK bank_unresolved at 0030A ($030A bank 0): CD 1F BB  CALL $BB1F $BB1F
# CHECK bank_unresolved at 0030D ($030D bank 0): CD EE BB  CALL $BBEE $BBEE
# CHECK bank_unresolved at 00334 ($0334 bank 0): CD C8 BC  CALL $BCC8 $BCC8
# CHECK bank_unresolved at 0033F ($033F bank 0): CD A2 B4  CALL $B4A2 $B4A2
# CHECK bank_unresolved at 00342 ($0342 bank 0): CD 9A B5  CALL $B59A $B59A
# CHECK bank_unresolved at 00345 ($0345 bank 0): CD D3 B5  CALL $B5D3 $B5D3
# CHECK bank_unresolved at 00348 ($0348 bank 0): CD 63 BB  CALL $BB63 $BB63
# CHECK bank_unresolved at 0034B ($034B bank 0): CD BA BB  CALL $BBBA $BBBA
# CHECK bank_unresolved at 00362 ($0362 bank 0): CD 50 BC  CALL $BC50 $BC50
# CHECK bank_unresolved at 003A0 ($03A0 bank 0): CD A2 B4  CALL $B4A2 $B4A2
# CHECK bank_unresolved at 00455 ($0455 bank 0): CD F8 BD  CALL $BDF8 $BDF8
# CHECK bank_unresolved at 004AE ($04AE bank 0): CD C2 BE  CALL $BEC2 $BEC2
# CHECK bank_unresolved at 004EC ($04EC bank 0): CD 6A B5  CALL $B56A $B56A
# CHECK bank_unresolved at 004FD ($04FD bank 0): CD 1F BB  CALL $BB1F $BB1F
# CHECK bank_unresolved at 0053D ($053D bank 0): CD 5F BD  CALL $BD5F $BD5F
# CHECK bank_unresolved at 0056D ($056D bank 0): CD 2E BA  CALL $BA2E $BA2E
# CHECK bank_unresolved at 00570 ($0570 bank 0): CD AE B9  CALL $B9AE $B9AE
# CHECK bank_unresolved at 00579 ($0579 bank 0): CD D9 B4  CALL $B4D9 $B4D9
# CHECK bank_unresolved at 0057F ($057F bank 0): CD 1F B7  CALL $B71F $B71F
# CHECK bank_unresolved at 0058E ($058E bank 0): CD 6B A9  CALL $A96B $A96B
# CHECK bank_unresolved at 00591 ($0591 bank 0): CD 15 97  CALL $9715 $9715
# CHECK bank_unresolved at 00594 ($0594 bank 0): CD 5C B6  CALL $B65C $B65C
# CHECK bank_unresolved at 0169A ($169A bank 0): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 01B04 ($1B04 bank 0): C3 FB B7  JP $B7FB $B7FB
# CHECK bank_unresolved at 01B14 ($1B14 bank 0): C3 FB B7  JP $B7FB $B7FB
# CHECK bank_unresolved at 01B24 ($1B24 bank 0): CD FB B7  CALL $B7FB $B7FB
# CHECK bank_unresolved at 01B35 ($1B35 bank 0): C3 FB B7  JP $B7FB $B7FB
# CHECK bank_unresolved at 01B45 ($1B45 bank 0): CD FB B7  CALL $B7FB $B7FB
# CHECK bank_unresolved at 01B56 ($1B56 bank 0): C3 FB B7  JP $B7FB $B7FB
# CHECK bank_unresolved at 01B66 ($1B66 bank 0): CD FB B7  CALL $B7FB $B7FB
# CHECK bank_unresolved at 01B77 ($1B77 bank 0): C3 FB B7  JP $B7FB $B7FB
# CHECK bank_unresolved at 023D9 ($23D9 bank 0): CD FC 8F  CALL $8FFC $8FFC
# CHECK bank_unresolved at 029DE ($29DE bank 0): CD 7F B6  CALL $B67F $B67F
# CHECK bank_unresolved at 029ED ($29ED bank 0): CD EF B8  CALL $B8EF $B8EF
# CHECK bank_unresolved at 02A0A ($2A0A bank 0): CD 5B B9  CALL $B95B $B95B
# CHECK bank_unresolved at 03C3D ($3C3D bank 0): CD 1F B7  CALL $B71F $B71F
# CHECK bank_unresolved at 03C53 ($3C53 bank 0): CD A2 B4  CALL $B4A2 $B4A2
# CHECK bank_unresolved at 03F6A ($3F6A bank 0): CD D3 B5  CALL $B5D3 $B5D3
# CHECK bank_unresolved at 03F89 ($3F89 bank 0): CD A2 B4  CALL $B4A2 $B4A2
# CHECK bank_unresolved at 07234 ($7234 bank 1): CD 6A B5  CALL $B56A $B56A
# CHECK bank_unresolved at 07245 ($7245 bank 1): CD 1F BB  CALL $BB1F $BB1F
# CHECK bank_unresolved at 072A0 ($72A0 bank 1): CD 9A B5  CALL $B59A $B59A
# CHECK bank_unresolved at 072B3 ($72B3 bank 1): CD D9 B4  CALL $B4D9 $B4D9
# CHECK bank_unresolved at 072B9 ($72B9 bank 1): CD 1F B7  CALL $B71F $B71F
# CHECK bank_unresolved at 0755C ($755C bank 1): CD 59 B8  CALL $B859 $B859
# CHECK bank_unresolved at 0756F ($756F bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 075F1 ($75F1 bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 0762F ($762F bank 1): CD 7F B6  CALL $B67F $B67F
# CHECK bank_unresolved at 07649 ($7649 bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 0766E ($766E bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 076A0 ($76A0 bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07708 ($7708 bank 1): CD 7F B6  CALL $B67F $B67F
# CHECK bank_unresolved at 0770E ($770E bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 07720 ($7720 bank 1): C3 EF B8  JP $B8EF $B8EF
# CHECK bank_unresolved at 07779 ($7779 bank 1): CD 7F B6  CALL $B67F $B67F
# CHECK bank_unresolved at 0777F ($777F bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 07791 ($7791 bank 1): C3 EF B8  JP $B8EF $B8EF
# CHECK bank_unresolved at 077F4 ($77F4 bank 1): CD 7F B6  CALL $B67F $B67F
# CHECK bank_unresolved at 07802 ($7802 bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 0780C ($780C bank 1): C3 EF B8  JP $B8EF $B8EF
# CHECK bank_unresolved at 0786E ($786E bank 1): CD 59 B8  CALL $B859 $B859
# CHECK bank_unresolved at 07881 ($7881 bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 07952 ($7952 bank 1): CD 59 B8  CALL $B859 $B859
# CHECK bank_unresolved at 07965 ($7965 bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 079DA ($79DA bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 079E3 ($79E3 bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07A8C ($7A8C bank 1): CD 7F B6  CALL $B67F $B67F
# CHECK bank_unresolved at 07AB1 ($7AB1 bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 07B59 ($7B59 bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07B62 ($7B62 bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07BFB ($7BFB bank 1): CD 59 B8  CALL $B859 $B859
# CHECK bank_unresolved at 07C0F ($7C0F bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 07D41 ($7D41 bank 1): CD 59 B8  CALL $B859 $B859
# CHECK bank_unresolved at 07D57 ($7D57 bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 07DCA ($7DCA bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07DDD ($7DDD bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07E5F ($7E5F bank 1): CD 59 B8  CALL $B859 $B859
# CHECK bank_unresolved at 07E72 ($7E72 bank 1): CD 0F BD  CALL $BD0F $BD0F
# CHECK bank_unresolved at 07F0F ($7F0F bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07F17 ($7F17 bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07F2F ($7F2F bank 1): CD 96 B4  CALL $B496 $B496
# CHECK bank_unresolved at 07F3A ($7F3A bank 1): CD 96 B4  CALL $B496 $B496
# Mapper stores found by the byte scan in bytes no path reached:
codem 05D62   # LD ($8000),A; after LD A,$0B; JP/CALL target from $3660C; 32 bytes of valid code before it
codem 05D70   # LD ($8000),A; after LD A,$02; 32 bytes of valid code before it
codem 05DF1   # LD ($8000),A; after LD A,$0A; 32 bytes of valid code before it
codem 05E0E   # LD ($8000),A; after LD A,$02; 32 bytes of valid code before it
codem 05ECF   # LD ($8000),A; after LD A,$0C; 32 bytes of valid code before it
codem 05ED8   # LD ($8000),A; after LD A,$02; 32 bytes of valid code before it
codem 05FBD   # LD ($8000),A; after LD A,$0A; 32 bytes of valid code before it
codem 05FC8   # LD ($8000),A; after LD A,$02; 32 bytes of valid code before it
# CHECK byte scan low: codem 25837  LD ($0000),A  (no valid code after it)
# CHECK byte scan low: codem 28580  LD ($8000),A  (no evidence)
# CHECK byte scan medium: codem 39980  LD ($0000),A  (32 bytes of valid code before it)
# CHECK low: site 05E0B  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 09F26  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 09F51  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 09F6B  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 09F9F  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 09FAA  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 09FBD  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0A083  OUT ($3E),A  (memory_control; no evidence)
# CHECK low: site 0A57A  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 0A756  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0A805  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0A90B  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 0BD46  IN A,($3E)  (unmapped_read; no evidence)
# CHECK medium: site 0DC9C  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 0DE6D  IN D,(C)  (port in C; 17 bytes of valid code before it)
# CHECK low: site 0F6BE  IN A,($DD)  (joypad_b_misc; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0F779  IN A,($DD)  (joypad_b_misc; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 0F7BC  IN A,($DD)  (joypad_b_misc; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 0FCDB  OUT ($3F),A  (io_control; 32 bytes of valid code before it)
# CHECK low: site 104E9  IN A,($7F)  (h_counter; no evidence)
# CHECK medium: site 11AE3  INDR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 11C88  IN A,($F1)  (joypad_b_misc; branch target from $11C85)
# CHECK low: site 12327  OUT ($BF),A  (vdp_control; no evidence)
# CHECK medium: site 12590  INDR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 12600  OUT ($F1),A  (fm_data; 32 bytes of valid code before it)
# CHECK medium: site 13B6E  OUT ($BF),A  (vdp_control; branch target from $13B7C)
# CHECK high: site 13CA5  IN A,($BF)  (vdp_status; branch target from $13C5E $13C65; 32 bytes of valid code before it)
# CHECK low: site 145E3  IN A,($DC)  (joypad_a; no evidence)
# CHECK medium: site 14780  INDR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 147F0  OUT ($F1),A  (fm_data; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 14B53  OUTI  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 14C5A  IN A,($DD)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK medium: site 1588A  OUT ($DD),A  (no_effect; 20 bytes of valid code before it)
# CHECK low: site 159D1  IN A,($BD)  (vdp_status; no valid code after it)
# CHECK medium: site 15D66  OUT ($F1),A  (fm_data; 32 bytes of valid code before it)
# CHECK medium: site 16B23  IND  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 19627  INDR  (port in C; 30 bytes of valid code before it)
# CHECK low: site 19F3A  IN A,($7E)  (v_counter; no evidence)
# CHECK medium: site 1A39F  INDR  (port in C; 11 bytes of valid code before it)
# CHECK low: site 1F80C  IN A,($F1)  (joypad_b_misc; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 1F833  IN A,($3E)  (unmapped_read; 32 bytes of valid code before it)
# CHECK medium: site 2034B  IN A,($F1)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK medium: site 20376  IN A,($3E)  (unmapped_read; 32 bytes of valid code before it)
# CHECK medium: site 215A7  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK low: site 222D9  OUT ($BF),A  (vdp_control; no valid code after it)
# CHECK medium: site 22AC3  IN A,($3E)  (unmapped_read; 26 bytes of valid code before it)
# CHECK medium: site 24013  OTIR  (port in C; 10 bytes of valid code before it)
# CHECK medium: site 24019  OUT ($BF),A  (vdp_control; 16 bytes of valid code before it)
# CHECK high: site 24025  OUT ($BE),A  (vdp_data; after LD A,$28; 28 bytes of valid code before it)
# CHECK high: site 24106  OTIR  (port in C; branch target from $240FA; 32 bytes of valid code before it)
# CHECK low: site 2410C  IN A,($7F)  (h_counter; no evidence)
# CHECK medium: site 2414B  OUTI  (port in C; 20 bytes of valid code before it)
# CHECK medium: site 2414E  OUT (C),D  (port in C; 23 bytes of valid code before it)
# CHECK low: site 24165  IN A,($DC)  (joypad_a; no evidence)
# CHECK high: site 24280  IN A,($DC)  (joypad_a; branch target from $24286; 23 bytes of valid code before it)
# CHECK high: site 2429A  OUT ($7E),A  (psg; after LD A,$8F; 32 bytes of valid code before it)
# CHECK medium: site 2431B  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK high: site 247B8  OUT ($7E),A  (psg; after LD A,$9F; branch target from $24797; 25 bytes of valid code before it)
# CHECK medium: site 24A6F  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 24E60  OUT ($F1),A  (fm_data; 10 bytes of valid code before it; no valid code after it)
# CHECK low: site 25A00  IN B,(C)  (port in C; no evidence)
# CHECK low: site 25DF4  OUTD  (port in C; no evidence)
# CHECK high: site 275A4  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 275A8  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 275B0  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK high: site 275B4  OUT ($BF),A  (vdp_control; after LD A,$0C; 32 bytes of valid code before it)
# CHECK high: site 275B8  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 275BF  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK high: site 275C4  IN A,($7E)  (v_counter; branch target from $275C8; 32 bytes of valid code before it)
# CHECK high: site 275CD  OUT ($BF),A  (vdp_control; after LD A,($C127); 32 bytes of valid code before it)
# CHECK high: site 275D1  OUT ($BF),A  (vdp_control; after LD A,$88; 32 bytes of valid code before it)
# CHECK high: site 275D3  IN A,($7E)  (v_counter; branch target from $275D7; 32 bytes of valid code before it)
# CHECK high: site 275DC  OUT ($BF),A  (vdp_control; after LD A,($C128); 32 bytes of valid code before it)
# CHECK high: site 275E0  OUT ($BF),A  (vdp_control; after LD A,$88; 32 bytes of valid code before it)
# CHECK high: site 275E2  IN A,($7E)  (v_counter; branch target from $275E6; 32 bytes of valid code before it)
# CHECK medium: site 275E9  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 275ED  OUT ($BF),A  (vdp_control; after LD A,$88; 32 bytes of valid code before it)
# CHECK high: site 28062  IN A,($BE)  (vdp_data; branch target from $28E72; 32 bytes of valid code before it)
# CHECK high: site 2806A  IN A,($BE)  (vdp_data; branch target from $2806E; 32 bytes of valid code before it)
# CHECK high: site 28095  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $28098; 32 bytes of valid code before it)
# CHECK low: site 280A5  IN A,($3E)  (unmapped_read; no evidence)
# CHECK high: site 280D6  OUT ($BF),A  (vdp_control; after LD A,$10; 32 bytes of valid code before it)
# CHECK high: site 280DA  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 280E2  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK low: site 280F0  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 280FB  OUT ($3E),A  (memory_control; no evidence)
# CHECK high: site 2813D  OUT ($BF),A  (vdp_control; after LD A,$20; 32 bytes of valid code before it)
# CHECK high: site 28141  OUT ($BF),A  (vdp_control; after LD A,$70; 32 bytes of valid code before it)
# CHECK medium: site 28143  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2814A  IN A,($BE)  (vdp_data; branch target from $2814E; 32 bytes of valid code before it)
# CHECK high: site 28152  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 28156  OUT ($BF),A  (vdp_control; after LD A,$5F; 32 bytes of valid code before it)
# CHECK high: site 2815E  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $2816D; 32 bytes of valid code before it)
# CHECK high: site 28162  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 28166  OUT ($BE),A  (vdp_data; after LD A,$FF; 32 bytes of valid code before it)
# CHECK medium: site 28168  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 281AA  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 281AD  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 281C6  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $281CC; 32 bytes of valid code before it)
# CHECK medium: site 281C9  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 281FF  IN A,($3E)  (unmapped_read; no evidence)
# CHECK high: site 2829F  OUT ($BF),A  (vdp_control; after LD A,$B4; 32 bytes of valid code before it)
# CHECK high: site 282A3  OUT ($BF),A  (vdp_control; after LD A,$7E; 32 bytes of valid code before it)
# CHECK high: site 282A7  OUT ($BE),A  (vdp_data; after LD A,$F8; 32 bytes of valid code before it)
# CHECK medium: site 282AA  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 282AE  OUT ($BE),A  (vdp_data; after LD A,$F9; 32 bytes of valid code before it)
# CHECK medium: site 282B1  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 282B5  OUT ($BF),A  (vdp_control; after LD A,$F4; 32 bytes of valid code before it)
# CHECK high: site 282B9  OUT ($BF),A  (vdp_control; after LD A,$7E; 32 bytes of valid code before it)
# CHECK high: site 282BD  OUT ($BE),A  (vdp_data; after LD A,$FA; 32 bytes of valid code before it)
# CHECK medium: site 282C0  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 282C4  OUT ($BE),A  (vdp_data; after LD A,$FB; 32 bytes of valid code before it)
# CHECK medium: site 282C7  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 282CB  OUT ($BF),A  (vdp_control; after LD A,$34; 32 bytes of valid code before it)
# CHECK high: site 282CF  OUT ($BF),A  (vdp_control; after LD A,$77; 32 bytes of valid code before it)
# CHECK high: site 282D3  OUT ($BE),A  (vdp_data; after LD A,$FC; 32 bytes of valid code before it)
# CHECK medium: site 282D6  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 282DA  OUT ($BE),A  (vdp_data; after LD A,$FD; 32 bytes of valid code before it)
# CHECK medium: site 282DD  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 282E1  OUT ($BF),A  (vdp_control; after LD A,$74; 32 bytes of valid code before it)
# CHECK high: site 282E5  OUT ($BF),A  (vdp_control; after LD A,$77; branch target from $2BDA6; 32 bytes of valid code before it)
# CHECK high: site 282E9  OUT ($BE),A  (vdp_data; after LD A,$FE; 32 bytes of valid code before it)
# CHECK medium: site 282EC  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 282F0  OUT ($BE),A  (vdp_data; after LD A,$FF; 32 bytes of valid code before it)
# CHECK medium: site 282F3  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 28305  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 28309  OUT ($BF),A  (vdp_control; after LD A,$60; 32 bytes of valid code before it)
# CHECK high: site 28310  OUT ($BF),A  (vdp_control; after LD A,$A0; 32 bytes of valid code before it)
# CHECK high: site 28314  OUT ($BF),A  (vdp_control; after LD A,$60; 32 bytes of valid code before it)
# CHECK high: site 2860F  OUT ($BF),A  (vdp_control; after LD A,$30; 32 bytes of valid code before it)
# CHECK high: site 28613  OUT ($BF),A  (vdp_control; after LD A,$81; 32 bytes of valid code before it)
# CHECK medium: site 28A73  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 28A76  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 28A7A  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28A7C  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28A7E  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28A83  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28A87  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28A89  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28A92  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28A9B  OUT ($BF),A  (vdp_control; branch target from $28A97; 32 bytes of valid code before it)
# CHECK medium: site 28A9D  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28A9F  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AA3  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AA5  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AA7  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AA9  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AAB  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AAD  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AB6  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28ABF  OUT ($BF),A  (vdp_control; branch target from $28ABB; 32 bytes of valid code before it)
# CHECK medium: site 28AC1  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AC3  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AC7  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AC9  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28ACB  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28ACD  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28ACF  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AD1  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28ADA  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28AE3  OUT ($BF),A  (vdp_control; branch target from $28ADF; 32 bytes of valid code before it)
# CHECK medium: site 28AE5  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AE7  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AEB  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AED  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AF5  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 28AF8  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 28AFA  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28AFF  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B03  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B05  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B0E  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28B17  OUT ($BF),A  (vdp_control; branch target from $28B13; 32 bytes of valid code before it)
# CHECK medium: site 28B19  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B1B  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B1F  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B21  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B23  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B25  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B2E  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28B37  OUT ($BF),A  (vdp_control; branch target from $28B33; 32 bytes of valid code before it)
# CHECK medium: site 28B39  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B3B  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B3F  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B41  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B43  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B45  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B4E  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28B57  OUT ($BF),A  (vdp_control; branch target from $28B53; 32 bytes of valid code before it)
# CHECK medium: site 28B59  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B5B  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B5F  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28B61  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 28DAC  OUT ($BF),A  (vdp_control; 16 bytes of valid code before it)
# CHECK medium: site 28DAF  OUT ($BF),A  (vdp_control; 19 bytes of valid code before it)
# CHECK medium: site 28E6D  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 28E70  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28E7B  OUT ($BF),A  (vdp_control; branch target from $28E67; 32 bytes of valid code before it)
# CHECK medium: site 28E7E  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 28E96  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 28E99  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28E9C  OUT ($BE),A  (vdp_data; after LD A,(DE); 32 bytes of valid code before it)
# CHECK medium: site 28EA4  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 28EA7  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 28EAA  OUT ($BE),A  (vdp_data; after LD A,(DE); 32 bytes of valid code before it)
# CHECK high: site 28FED  OUT ($BF),A  (vdp_control; after LD A,$20; 32 bytes of valid code before it)
# CHECK high: site 28FF1  OUT ($BF),A  (vdp_control; after LD A,$61; 32 bytes of valid code before it)
# CHECK medium: site 29003  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 29009  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 29022  OUT ($BE),A  (vdp_data; branch target from $2901F; 32 bytes of valid code before it)
# CHECK high: site 2902A  OUT ($BE),A  (vdp_data; branch target from $29027; 32 bytes of valid code before it)
# CHECK high: site 293DA  OUT ($BF),A  (vdp_control; after LD A,$10; 32 bytes of valid code before it)
# CHECK high: site 293DE  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 293E6  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK high: site 293F6  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK high: site 293FA  OUT ($BF),A  (vdp_control; after LD A,$49; 32 bytes of valid code before it)
# CHECK medium: site 293FC  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 29404  IN A,($BE)  (vdp_data; branch target from $2940B; 32 bytes of valid code before it)
# CHECK high: site 29410  OUT ($BF),A  (vdp_control; after LD A,$A0; 32 bytes of valid code before it)
# CHECK high: site 29414  OUT ($BF),A  (vdp_control; after LD A,$4B; 32 bytes of valid code before it)
# CHECK high: site 29423  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $29426; 32 bytes of valid code before it)
# CHECK medium: site 29446  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 29449  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2944E  OUT ($BE),A  (vdp_data; after LD A,(DE); branch target from $29455; 32 bytes of valid code before it)
# CHECK high: site 29452  OUT ($BE),A  (vdp_data; after LD A,$10; 32 bytes of valid code before it)
# CHECK medium: site 29469  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2946C  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 29472  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2947A  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2947D  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 29481  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 294A8  IN A,($3E)  (unmapped_read; no evidence)
# CHECK low: site 294AD  IN A,($3E)  (unmapped_read; no evidence)
# CHECK high: site 294D1  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 294D5  OUT ($BF),A  (vdp_control; after LD A,$40; 32 bytes of valid code before it)
# CHECK medium: site 294E7  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 294ED  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 29506  OUT ($BE),A  (vdp_data; branch target from $29503; 32 bytes of valid code before it)
# CHECK high: site 2950E  OUT ($BE),A  (vdp_data; branch target from $2950B; 32 bytes of valid code before it)
# CHECK low: site 29EC9  IN A,($3E)  (unmapped_read; no evidence)
# CHECK high: site 29EF8  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 29EFC  OUT ($BF),A  (vdp_control; after LD A,$40; 32 bytes of valid code before it)
# CHECK medium: site 29F0E  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 29F14  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 29F30  OUT ($BE),A  (vdp_data; branch target from $29F2D; 32 bytes of valid code before it)
# CHECK high: site 29F38  OUT ($BE),A  (vdp_data; branch target from $29F35; 32 bytes of valid code before it)
# CHECK high: site 29F55  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK high: site 29F59  OUT ($BF),A  (vdp_control; after LD A,$69; 32 bytes of valid code before it)
# CHECK medium: site 29F6B  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 29F71  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 29F8A  OUT ($BE),A  (vdp_data; branch target from $29F87; 32 bytes of valid code before it)
# CHECK high: site 29F92  OUT ($BE),A  (vdp_data; branch target from $29F8F; 32 bytes of valid code before it)
# CHECK high: site 29FC1  OUT ($BF),A  (vdp_control; after LD A,$10; 32 bytes of valid code before it)
# CHECK high: site 29FC5  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 29FCD  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK high: site 29FD1  OUT ($BF),A  (vdp_control; after LD A,$40; 32 bytes of valid code before it)
# CHECK high: site 29FD5  OUT ($BF),A  (vdp_control; after LD A,$77; 32 bytes of valid code before it)
# CHECK high: site 29FFD  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $2A004 $2A027; 32 bytes of valid code before it)
# CHECK high: site 2A001  OUT ($BE),A  (vdp_data; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 2A028  OUT ($BF),A  (vdp_control; after LD A,$20; 32 bytes of valid code before it)
# CHECK high: site 2A02C  OUT ($BF),A  (vdp_control; after LD A,$61; 32 bytes of valid code before it)
# CHECK low: site 2A063  IN A,($3E)  (unmapped_read; no evidence)
# CHECK medium: site 2A128  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2A12B  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2A132  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 2A136  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 2A139  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A13B  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A142  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2A145  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2A14C  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 2A150  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 2A153  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A155  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A15C  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2A15F  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2A166  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 2A16A  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 2A16D  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A16F  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A178  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2A17B  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2A180  OUT ($BE),A  (vdp_data; after LD A,($D196); 32 bytes of valid code before it)
# CHECK high: site 2A18A  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 2A18E  OUT ($BF),A  (vdp_control; after LD A,$60; 32 bytes of valid code before it)
# CHECK high: site 2A195  OUT ($BF),A  (vdp_control; after LD A,$A0; 32 bytes of valid code before it)
# CHECK high: site 2A199  OUT ($BF),A  (vdp_control; after LD A,$60; 32 bytes of valid code before it)
# CHECK high: site 2A57C  OUT ($BF),A  (vdp_control; after LD A,$30; 32 bytes of valid code before it)
# CHECK high: site 2A580  OUT ($BF),A  (vdp_control; after LD A,$81; 32 bytes of valid code before it)
# CHECK high: site 2A592  OUT ($BF),A  (vdp_control; after LD A,$30; 32 bytes of valid code before it)
# CHECK high: site 2A596  OUT ($BF),A  (vdp_control; after LD A,$81; 32 bytes of valid code before it)
# CHECK medium: site 2A5D8  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2A5DB  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2A5DF  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A5E4  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A5E7  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A5EA  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A5EC  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A5EE  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A5F7  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2A600  OUT ($BF),A  (vdp_control; branch target from $2A5FC; 32 bytes of valid code before it)
# CHECK medium: site 2A602  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A604  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A608  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A60A  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A60C  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A60E  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A610  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A612  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A61B  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2A624  OUT ($BF),A  (vdp_control; branch target from $2A620; 32 bytes of valid code before it)
# CHECK medium: site 2A626  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A628  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A62C  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A62E  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A630  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A632  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A634  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A636  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A63F  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2A648  OUT ($BF),A  (vdp_control; branch target from $2A644; 32 bytes of valid code before it)
# CHECK medium: site 2A64A  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A64C  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A650  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A652  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2A9BE  OUT ($BF),A  (vdp_control; branch target from $2A9B7; 32 bytes of valid code before it)
# CHECK medium: site 2A9C1  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2A9CC  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2A9CF  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 2A9D4  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A9D7  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2A9E2  OUT ($BF),A  (vdp_control; branch target from $2A99F $2A9A5 $2A9AB $2A9B1; 32 bytes of valid code before it)
# CHECK medium: site 2A9E5  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2A9EF  OUT ($BE),A  (vdp_data; after LD A,(DE); branch target from $2A9FA; 32 bytes of valid code before it)
# CHECK high: site 2A9F2  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 2A9F6  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2A9F8  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 2AA75  IN A,($DD)  (joypad_b_misc; no evidence)
# CHECK low: site 2ABDA  OUT ($BF),A  (vdp_control; 13 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2ABDD  OUT ($BF),A  (vdp_control; 14 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 2ACE6  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $2ACF0; 32 bytes of valid code before it)
# CHECK medium: site 2ACE8  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2ACEA  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2ACED  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2ACFA  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $2AD05; 32 bytes of valid code before it)
# CHECK medium: site 2ACFC  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2ACFE  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2AD01  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2AD19  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $2AD25; 32 bytes of valid code before it)
# CHECK medium: site 2AD1B  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2AD1D  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2AD20  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2AD38  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $2AD44; 32 bytes of valid code before it)
# CHECK medium: site 2AD3A  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2AD3C  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2AD3F  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2C0E1  IN A,($BE)  (vdp_data; branch target from $2CAB9; 32 bytes of valid code before it)
# CHECK high: site 2C0E8  IN A,($BE)  (vdp_data; branch target from $2C0EC; 32 bytes of valid code before it)
# CHECK high: site 2C10B  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $2C10E; 32 bytes of valid code before it)
# CHECK high: site 2C13D  OUT ($BF),A  (vdp_control; after LD A,$30; 32 bytes of valid code before it)
# CHECK high: site 2C141  OUT ($BF),A  (vdp_control; after LD A,$81; 32 bytes of valid code before it)
# CHECK high: site 2C191  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 2C195  OUT ($BF),A  (vdp_control; after LD A,$40; 32 bytes of valid code before it)
# CHECK medium: site 2C1A7  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C1AD  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2C1C6  OUT ($BE),A  (vdp_data; branch target from $2C1C3; 32 bytes of valid code before it)
# CHECK high: site 2C1CE  OUT ($BE),A  (vdp_data; branch target from $2C1CB; 32 bytes of valid code before it)
# CHECK high: site 2C1F4  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 2C1F8  OUT ($BF),A  (vdp_control; after LD A,$60; 32 bytes of valid code before it)
# CHECK medium: site 2C20A  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C210  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2C229  OUT ($BE),A  (vdp_data; branch target from $2C226; 32 bytes of valid code before it)
# CHECK high: site 2C231  OUT ($BE),A  (vdp_data; branch target from $2C22E; 32 bytes of valid code before it)
# CHECK high: site 2C259  OUT ($BF),A  (vdp_control; after LD A,$10; 32 bytes of valid code before it)
# CHECK high: site 2C25D  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 2C265  OTIR  (port in C; 32 bytes of valid code before it)
# CHECK high: site 2C285  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 2C289  OUT ($BF),A  (vdp_control; after LD A,$77; 32 bytes of valid code before it)
# CHECK high: site 2C2B1  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $2C2B7; 32 bytes of valid code before it)
# CHECK high: site 2C2B4  OUT ($BE),A  (vdp_data; branch target from $2DC5D; 32 bytes of valid code before it)
# CHECK low: site 2C2F2  IN A,($3E)  (unmapped_read; no evidence)
# CHECK medium: site 2C417  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C41A  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2C421  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 2C425  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 2C428  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C42A  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C431  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C434  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2C43B  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 2C43F  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 2C442  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C444  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C44B  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C44E  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2C455  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 2C459  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 2C45C  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C45E  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C464  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C467  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C469  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C46B  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C47A  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C47D  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C480  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C482  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C485  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C48C  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C48F  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C491  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C493  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C497  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C499  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C49C  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2C4A2  OUT ($BF),A  (vdp_control; branch target from $2C4CD; 32 bytes of valid code before it)
# CHECK medium: site 2C4A5  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C4A7  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4A9  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4AD  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4AF  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4B2  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4B9  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C4BC  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C4BF  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4C1  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4C4  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2C4CE  OUT ($BF),A  (vdp_control; after LD A,$10; 32 bytes of valid code before it)
# CHECK high: site 2C4D2  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK medium: site 2C4E2  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C4E5  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C4E7  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4E9  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4ED  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C4F0  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C4F5  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C4FC  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C4FF  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C501  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C503  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C507  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C50A  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C50E  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2C544  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 2C548  OUT ($BF),A  (vdp_control; after LD A,$5A; 32 bytes of valid code before it)
# CHECK high: site 2C55A  OUT ($BF),A  (vdp_control; after LD A,$20; 32 bytes of valid code before it)
# CHECK high: site 2C55E  OUT ($BF),A  (vdp_control; after LD A,$5A; 32 bytes of valid code before it)
# CHECK high: site 2C56E  OUT ($BF),A  (vdp_control; after LD A,$40; 32 bytes of valid code before it)
# CHECK high: site 2C572  OUT ($BF),A  (vdp_control; after LD A,$5A; 32 bytes of valid code before it)
# CHECK high: site 2C593  OUT ($BF),A  (vdp_control; after LD A,$20; 32 bytes of valid code before it)
# CHECK high: site 2C597  OUT ($BF),A  (vdp_control; after LD A,$62; 32 bytes of valid code before it)
# CHECK high: site 2C59E  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK high: site 2C5A2  OUT ($BF),A  (vdp_control; after LD A,$62; 32 bytes of valid code before it)
# CHECK low: site 2C604  IN A,($3E)  (unmapped_read; no evidence)
# CHECK medium: site 2C736  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C739  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C73B  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C73D  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C741  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2C743  IN A,($BE)  (vdp_data; branch target from $2C711; 31 bytes of valid code before it)
# CHECK medium: site 2C745  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C747  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C750  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2C759  OUT ($BF),A  (vdp_control; branch target from $2C755; 32 bytes of valid code before it)
# CHECK medium: site 2C75B  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C75D  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C766  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C769  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C76B  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C76D  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C776  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2C77F  OUT ($BF),A  (vdp_control; branch target from $2C77B; 32 bytes of valid code before it)
# CHECK medium: site 2C781  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C783  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C787  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C78E  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C791  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C793  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C79C  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2C7A5  OUT ($BF),A  (vdp_control; branch target from $2C7A1; 32 bytes of valid code before it)
# CHECK medium: site 2C7A7  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C7A9  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C7AD  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C7AF  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C7B1  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C7B3  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2C99C  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2C99F  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2CAB4  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2CAB7  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2CAD3  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2CAD6  OUT ($BF),A  (vdp_control; branch target from $2CB01; 32 bytes of valid code before it)
# CHECK high: site 2CAE8  OUT ($BE),A  (vdp_data; after LD A,(IX+$00); 32 bytes of valid code before it)
# CHECK high: site 2CAED  OUT ($BE),A  (vdp_data; after LD A,(IX+$08); 32 bytes of valid code before it)
# CHECK medium: site 2CAEF  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2CAF1  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 2CAFD  OUT ($BE),A  (vdp_data; after LD A,(IX+$00); 32 bytes of valid code before it)
# CHECK high: site 2CB02  OUT ($BE),A  (vdp_data; after LD A,(IX+$10); 32 bytes of valid code before it)
# CHECK medium: site 2CB04  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2CB06  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 2D1ED  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2D1F0  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2D1F3  OUT ($BE),A  (vdp_data; after LD A,(DE); branch target from $2D1C1 $2D1C0; 32 bytes of valid code before it)
# CHECK medium: site 2D1FB  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 2D1FE  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 2D201  OUT ($BE),A  (vdp_data; after LD A,(DE); 32 bytes of valid code before it)
# CHECK high: site 3012C  IN A,($BE)  (vdp_data; branch target from $30B1B; 32 bytes of valid code before it)
# CHECK high: site 30134  IN A,($BE)  (vdp_data; branch target from $30138; 32 bytes of valid code before it)
# CHECK high: site 3015F  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $30162; 32 bytes of valid code before it)
# CHECK high: site 30186  OUT ($BF),A  (vdp_control; after LD A,$30; 32 bytes of valid code before it)
# CHECK high: site 3018A  OUT ($BF),A  (vdp_control; after LD A,$81; branch target from $33DC3; 32 bytes of valid code before it)
# CHECK high: site 301C6  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 301CA  OUT ($BF),A  (vdp_control; after LD A,$40; 32 bytes of valid code before it)
# CHECK high: site 301DB  OUT ($BE),A  (vdp_data; after LD A,(IX+$00); 32 bytes of valid code before it)
# CHECK high: site 301E0  OUT ($BE),A  (vdp_data; after LD A,(IX+$08); 32 bytes of valid code before it)
# CHECK high: site 301EF  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 301F3  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 30210  OUT ($BF),A  (vdp_control; after LD A,$00; 32 bytes of valid code before it)
# CHECK high: site 30214  OUT ($BF),A  (vdp_control; after LD A,$60; 32 bytes of valid code before it)
# CHECK medium: site 30226  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 3022C  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 30245  OUT ($BE),A  (vdp_data; branch target from $30242; 32 bytes of valid code before it)
# CHECK high: site 3024D  OUT ($BE),A  (vdp_data; branch target from $3024A; 32 bytes of valid code before it)
# CHECK high: site 3025D  OUT ($BF),A  (vdp_control; after LD A,$10; 32 bytes of valid code before it)
# CHECK high: site 30261  OUT ($BF),A  (vdp_control; after LD A,$C0; 32 bytes of valid code before it)
# CHECK high: site 30269  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $3026C; 32 bytes of valid code before it)
# CHECK high: site 302CE  OUT ($BF),A  (vdp_control; after LD A,$40; 32 bytes of valid code before it)
# CHECK high: site 302D2  OUT ($BF),A  (vdp_control; after LD A,$77; 32 bytes of valid code before it)
# CHECK high: site 302FA  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $3030E; 32 bytes of valid code before it)
# CHECK high: site 3030B  OUT ($BE),A  (vdp_data; branch target from $30302 $30308; 32 bytes of valid code before it)
# CHECK medium: site 303B2  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 303B5  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 303BD  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 303C1  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 303C4  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 303C6  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 303CD  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 303D0  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 303D8  OUT ($BE),A  (vdp_data; branch target from $303A5; 32 bytes of valid code before it)
# CHECK high: site 303DC  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 303DF  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 303E1  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 303E8  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 303EB  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 303F2  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK high: site 303F7  OUT ($BE),A  (vdp_data; after LD A,(HL); 32 bytes of valid code before it)
# CHECK medium: site 303FA  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 303FC  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 30628  OUT ($BF),A  (vdp_control; branch target from $30620; 32 bytes of valid code before it)
# CHECK medium: site 3062B  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 30636  OUT ($BE),A  (vdp_data; after LD A,$4C; 32 bytes of valid code before it)
# CHECK medium: site 30639  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 3063D  OUT ($BE),A  (vdp_data; after LD A,$A5; 32 bytes of valid code before it)
# CHECK medium: site 30640  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 3064B  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 3064E  OUT ($BF),A  (vdp_control; branch target from $305DC; 32 bytes of valid code before it)
# CHECK high: site 30652  OUT ($BE),A  (vdp_data; after LD A,$AC; 32 bytes of valid code before it)
# CHECK high: site 30655  OUT ($BE),A  (vdp_data; branch target from $3202E; 32 bytes of valid code before it)
# CHECK high: site 30659  OUT ($BE),A  (vdp_data; after LD A,$AF; 32 bytes of valid code before it)
# CHECK medium: site 3065C  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 30670  OUT ($BE),A  (vdp_data; after LD A,$9C; 32 bytes of valid code before it)
# CHECK medium: site 30673  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 30677  OUT ($BE),A  (vdp_data; after LD A,$AC; 32 bytes of valid code before it)
# CHECK medium: site 3067A  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 30685  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 30688  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 3068C  OUT ($BE),A  (vdp_data; after LD A,$C2; 32 bytes of valid code before it)
# CHECK medium: site 3068F  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK high: site 30693  OUT ($BE),A  (vdp_data; after LD A,$4C; 32 bytes of valid code before it)
# CHECK medium: site 30696  OUT ($BE),A  (vdp_data; 32 bytes of valid code before it)
# CHECK medium: site 30A8C  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 30A8F  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK high: site 30AC0  OUT ($BE),A  (vdp_data; after LD A,(HL); branch target from $30AD4; 32 bytes of valid code before it)
# CHECK high: site 30AD1  OUT ($BE),A  (vdp_data; branch target from $30AC8 $30ACE; 32 bytes of valid code before it)
# CHECK low: site 30B16  OUT ($BF),A  (vdp_control; 7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 30B19  OUT ($BF),A  (vdp_control; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 30B24  OUT ($BF),A  (vdp_control; branch target from $30B10; 32 bytes of valid code before it)
# CHECK medium: site 30B27  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 32028  IN D,(C)  (port in C; 32 bytes of valid code before it)
# CHECK low: site 32C30  IN A,($DC)  (joypad_a; no valid code after it)
# CHECK low: site 39DA2  OUT (C),B  (port in C; no evidence)
# CHECK medium: site 3B5C8  IN E,(C)  (port in C; 19 bytes of valid code before it)
# CHECK low: site 3B9AE  OTIR  (port in C; no evidence)
# The game paces its screens with EI : HALT (title, credits, room changes,
# frame delays counted with DJNZ). Each one waits in the runtime for the
# game's own frame interrupt, as on the Master System, and not for the
# runtime's own interrupts too.
eihalt 0040D   ; EI : HALT
eihalt 0044B   ; EI : HALT
eihalt 0049D   ; EI : HALT
eihalt 004A7   ; EI : HALT
eihalt 004B5   ; EI : HALT
eihalt 004FB   ; EI : HALT
eihalt 00657   ; EI : HALT
eihalt 006C7   ; EI : HALT
eihalt 01C8C   ; EI : HALT
eihalt 01CD9   ; EI : HALT
eihalt 01D7D   ; EI : HALT
eihalt 0213B   ; EI : HALT
eihalt 023B4   ; EI : HALT
eihalt 02487   ; EI : HALT
eihalt 0249F   ; EI : HALT
eihalt 024B7   ; EI : HALT
eihalt 024E0   ; EI : HALT
eihalt 026B2   ; EI : HALT
eihalt 02757   ; EI : HALT
eihalt 027B9   ; EI : HALT
eihalt 0280A   ; EI : HALT
eihalt 02853   ; EI : HALT
eihalt 02869   ; EI : HALT
eihalt 0287F   ; EI : HALT
eihalt 02C33   ; EI : HALT
eihalt 02C6D   ; EI : HALT
eihalt 02D13   ; EI : HALT
eihalt 02DA1   ; EI : HALT
eihalt 02DC7   ; EI : HALT
eihalt 02E02   ; EI : HALT
eihalt 02EB4   ; EI : HALT
eihalt 02EDA   ; EI : HALT
eihalt 02F43   ; EI : HALT
eihalt 02F8D   ; EI : HALT
eihalt 02FBC   ; EI : HALT
eihalt 02FDA   ; EI : HALT
eihalt 03016   ; EI : HALT
eihalt 0335E   ; EI : HALT
eihalt 037BA   ; EI : HALT
eihalt 03833   ; EI : HALT
eihalt 0388D   ; EI : HALT
eihalt 03B39   ; EI : HALT
eihalt 03B68   ; EI : HALT
eihalt 03B79   ; EI : HALT
eihalt 03B8A   ; EI : HALT
eihalt 03BA8   ; EI : HALT
eihalt 03C24   ; EI : HALT
eihalt 03DE4   ; EI : HALT
eihalt 03DFB   ; EI : HALT
eihalt 03E48   ; EI : HALT
eihalt 03E70   ; EI : HALT
eihalt 03E98   ; EI : HALT
eihalt 03EC0   ; EI : HALT
eihalt 03EF1   ; EI : HALT
eihalt 03F55   ; EI : HALT
eihalt 06FD8   ; EI : HALT
eihalt 06FFF   ; EI : HALT
eihalt 07021   ; EI : HALT
eihalt 071D5   ; EI : HALT
eihalt 07243   ; EI : HALT
eihalt 0727E   ; EI : HALT
eihalt 072ED   ; EI : HALT
eihalt 269A3   ; EI : HALT
eihalt 26A8C   ; EI : HALT
eihalt 26AF8   ; EI : HALT
eihalt 26B14   ; EI : HALT
eihalt 26C7E   ; EI : HALT
eihalt 26C8B   ; EI : HALT
eihalt 26CC5   ; EI : HALT
eihalt 26D2F   ; EI : HALT
eihalt 26DD2   ; EI : HALT
eihalt 2E552   ; EI : HALT
eihalt 2E97A   ; EI : HALT
eihalt 2F147   ; EI : HALT
eihalt 2F19E   ; EI : HALT
eihalt 2F1BF   ; EI : HALT
eihalt 2F1F1   ; EI : HALT
eihalt 2F6C3   ; EI : HALT
eihalt 31638   ; EI : HALT
eihalt 3165A   ; EI : HALT
eihalt 3166A   ; EI : HALT
eihalt 3167A   ; EI : HALT
eihalt 3199A   ; EI : HALT
eihalt 31EE4   ; EI : HALT
eihalt 31F37   ; EI : HALT
eihalt 31F78   ; EI : HALT
# The room-script tables in bank 1 ($5680-$5900: lists of handler words
# ended by 0, the handler at $83A7 taking 2 inline words) call handlers in
# bank 1 that switch to banks $0A-$0C and call the code there. The scanner
# does not follow the tables, so these sites were found with a scan given
# those calls as entries:
#   $5D4B (table word at $575A) -> $5D60: bank $0B, CALL $8111
#   $5DC3 (table word at $579C) -> $5DEF: bank $0A, CALL $809E
#   $5E3A (table word at $5860) -> $5E8C -> $5EC8: bank $0C, CALL $8168
#   $5F2A (table word at $5712) -> $5F6E -> $5FB6: bank $0A, CALL $9EC2
# Bank $0B's $8111 calls its game at $8145 and then turns the display off
# ($813B-$8144); the scanner does not see $8145 return, but $5D68 uses the
# value $8111 returns, as bank $0C's $8168 does after the same calls.
eihalt 2C139   ; EI : HALT
site 2C13D   ; OUT ($BF),A
site 2C141   ; OUT ($BF),A
site 28062   ; IN A,($BE)
site 2806A   ; IN A,($BE)
site 28095   ; OUT ($BE),A
site 280D6   ; OUT ($BF),A
site 280DA   ; OUT ($BF),A
site 280E2   ; OTIR
site 2813D   ; OUT ($BF),A
site 28141   ; OUT ($BF),A
site 28143   ; IN A,($BE)
site 2814A   ; IN A,($BE)
site 28152   ; OUT ($BF),A
site 28156   ; OUT ($BF),A
site 2815E   ; OUT ($BE),A
site 28162   ; OUT ($BE),A
site 28166   ; OUT ($BE),A
site 28168   ; OUT ($BE),A
site 281AA   ; OUT ($BF),A
site 281AD   ; OUT ($BF),A
site 281C6   ; OUT ($BE),A
site 281C9   ; OUT ($BE),A
site 2829F   ; OUT ($BF),A
site 282A3   ; OUT ($BF),A
site 282A7   ; OUT ($BE),A
site 282AA   ; OUT ($BE),A
site 282AE   ; OUT ($BE),A
site 282B1   ; OUT ($BE),A
site 282B5   ; OUT ($BF),A
site 282B9   ; OUT ($BF),A
site 282BD   ; OUT ($BE),A
site 282C0   ; OUT ($BE),A
site 282C4   ; OUT ($BE),A
site 282C7   ; OUT ($BE),A
site 282CB   ; OUT ($BF),A
site 282CF   ; OUT ($BF),A
site 282D3   ; OUT ($BE),A
site 282D6   ; OUT ($BE),A
site 282DA   ; OUT ($BE),A
site 282DD   ; OUT ($BE),A
site 282E1   ; OUT ($BF),A
site 282E5   ; OUT ($BF),A
site 282E9   ; OUT ($BE),A
site 282EC   ; OUT ($BE),A
site 282F0   ; OUT ($BE),A
site 282F3   ; OUT ($BE),A
site 28305   ; OUT ($BF),A
site 28309   ; OUT ($BF),A
site 28310   ; OUT ($BF),A
site 28314   ; OUT ($BF),A
site 2860F   ; OUT ($BF),A
site 28613   ; OUT ($BF),A
site 28A73   ; OUT ($BF),A
site 28A76   ; OUT ($BF),A
site 28A7A   ; IN A,($BE)
site 28A7C   ; IN A,($BE)
site 28A7E   ; IN A,($BE)
site 28A83   ; IN A,($BE)
site 28A87   ; IN A,($BE)
site 28A89   ; IN A,($BE)
site 28A92   ; OUT ($BF),A
site 28A9B   ; OUT ($BF),A
site 28A9D   ; IN A,($BE)
site 28A9F   ; IN A,($BE)
site 28AA3   ; IN A,($BE)
site 28AA5   ; IN A,($BE)
site 28AA7   ; IN A,($BE)
site 28AA9   ; IN A,($BE)
site 28AAB   ; IN A,($BE)
site 28AAD   ; IN A,($BE)
site 28AB6   ; OUT ($BF),A
site 28ABF   ; OUT ($BF),A
site 28AC1   ; IN A,($BE)
site 28AC3   ; IN A,($BE)
site 28AC7   ; IN A,($BE)
site 28AC9   ; IN A,($BE)
site 28ACB   ; IN A,($BE)
site 28ACD   ; IN A,($BE)
site 28ACF   ; IN A,($BE)
site 28AD1   ; IN A,($BE)
site 28ADA   ; OUT ($BF),A
site 28AE3   ; OUT ($BF),A
site 28AE5   ; IN A,($BE)
site 28AE7   ; IN A,($BE)
site 28AEB   ; IN A,($BE)
site 28AED   ; IN A,($BE)
site 28AF5   ; OUT ($BF),A
site 28AF8   ; OUT ($BF),A
site 28AFA   ; IN A,($BE)
site 28AFF   ; IN A,($BE)
site 28B03   ; IN A,($BE)
site 28B05   ; IN A,($BE)
site 28B0E   ; OUT ($BF),A
site 28B17   ; OUT ($BF),A
site 28B19   ; IN A,($BE)
site 28B1B   ; IN A,($BE)
site 28B1F   ; IN A,($BE)
site 28B21   ; IN A,($BE)
site 28B23   ; IN A,($BE)
site 28B25   ; IN A,($BE)
site 28B2E   ; OUT ($BF),A
site 28B37   ; OUT ($BF),A
site 28B39   ; IN A,($BE)
site 28B3B   ; IN A,($BE)
site 28B3F   ; IN A,($BE)
site 28B41   ; IN A,($BE)
site 28B43   ; IN A,($BE)
site 28B45   ; IN A,($BE)
site 28B4E   ; OUT ($BF),A
site 28B57   ; OUT ($BF),A
site 28B59   ; IN A,($BE)
site 28B5B   ; IN A,($BE)
site 28B5F   ; IN A,($BE)
site 28B61   ; IN A,($BE)
site 28DAC   ; OUT ($BF),A
site 28DAF   ; OUT ($BF),A
site 28E6D   ; OUT ($BF),A
site 28E70   ; OUT ($BF),A
site 28E7B   ; OUT ($BF),A
site 28E7E   ; OUT ($BF),A
site 28E96   ; OUT ($BF),A
site 28E99   ; OUT ($BF),A
site 28E9C   ; OUT ($BE),A
site 28EA4   ; OUT ($BF),A
site 28EA7   ; OUT ($BF),A
site 28EAA   ; OUT ($BE),A
site 28FED   ; OUT ($BF),A
site 28FF1   ; OUT ($BF),A
site 29003   ; OUT ($BE),A
site 29009   ; OUT ($BE),A
site 29022   ; OUT ($BE),A
site 2902A   ; OUT ($BE),A
site 293DA   ; OUT ($BF),A
site 293DE   ; OUT ($BF),A
site 293E6   ; OTIR
site 293F6   ; OUT ($BF),A
site 293FA   ; OUT ($BF),A
site 293FC   ; IN A,($BE)
site 29404   ; IN A,($BE)
site 29410   ; OUT ($BF),A
site 29414   ; OUT ($BF),A
site 29423   ; OUT ($BE),A
site 29446   ; OUT ($BF),A
site 29449   ; OUT ($BF),A
site 2944E   ; OUT ($BE),A
site 29452   ; OUT ($BE),A
site 29469   ; OUT ($BF),A
site 2946C   ; OUT ($BF),A
site 29472   ; OUT ($BE),A
site 2947A   ; OUT ($BF),A
site 2947D   ; OUT ($BF),A
site 29481   ; OUT ($BE),A
site 294D1   ; OUT ($BF),A
site 294D5   ; OUT ($BF),A
site 294E7   ; OUT ($BE),A
site 294ED   ; OUT ($BE),A
site 29506   ; OUT ($BE),A
site 2950E   ; OUT ($BE),A
site 29EF8   ; OUT ($BF),A
site 29EFC   ; OUT ($BF),A
site 29F0E   ; OUT ($BE),A
site 29F14   ; OUT ($BE),A
site 29F30   ; OUT ($BE),A
site 29F38   ; OUT ($BE),A
site 29F55   ; OUT ($BF),A
site 29F59   ; OUT ($BF),A
site 29F6B   ; OUT ($BE),A
site 29F71   ; OUT ($BE),A
site 29F8A   ; OUT ($BE),A
site 29F92   ; OUT ($BE),A
site 29FC1   ; OUT ($BF),A
site 29FC5   ; OUT ($BF),A
site 29FCD   ; OTIR
site 29FD1   ; OUT ($BF),A
site 29FD5   ; OUT ($BF),A
site 29FFD   ; OUT ($BE),A
site 2A001   ; OUT ($BE),A
site 2A028   ; OUT ($BF),A
site 2A02C   ; OUT ($BF),A
site 2A128   ; OUT ($BF),A
site 2A12B   ; OUT ($BF),A
site 2A132   ; OUT ($BE),A
site 2A136   ; OUT ($BE),A
site 2A139   ; OUT ($BE),A
site 2A13B   ; OUT ($BE),A
site 2A142   ; OUT ($BF),A
site 2A145   ; OUT ($BF),A
site 2A14C   ; OUT ($BE),A
site 2A150   ; OUT ($BE),A
site 2A153   ; OUT ($BE),A
site 2A155   ; OUT ($BE),A
site 2A15C   ; OUT ($BF),A
site 2A15F   ; OUT ($BF),A
site 2A166   ; OUT ($BE),A
site 2A16A   ; OUT ($BE),A
site 2A16D   ; OUT ($BE),A
site 2A16F   ; OUT ($BE),A
site 2A178   ; OUT ($BF),A
site 2A17B   ; OUT ($BF),A
site 2A180   ; OUT ($BE),A
site 2A18A   ; OUT ($BF),A
site 2A18E   ; OUT ($BF),A
site 2A195   ; OUT ($BF),A
site 2A199   ; OUT ($BF),A
site 2A57C   ; OUT ($BF),A
site 2A580   ; OUT ($BF),A
site 2A592   ; OUT ($BF),A
site 2A596   ; OUT ($BF),A
site 2A5D8   ; OUT ($BF),A
site 2A5DB   ; OUT ($BF),A
site 2A5DF   ; IN A,($BE)
site 2A5E4   ; IN A,($BE)
site 2A5E7   ; IN A,($BE)
site 2A5EA   ; IN A,($BE)
site 2A5EC   ; IN A,($BE)
site 2A5EE   ; IN A,($BE)
site 2A5F7   ; OUT ($BF),A
site 2A600   ; OUT ($BF),A
site 2A602   ; IN A,($BE)
site 2A604   ; IN A,($BE)
site 2A608   ; IN A,($BE)
site 2A60A   ; IN A,($BE)
site 2A60C   ; IN A,($BE)
site 2A60E   ; IN A,($BE)
site 2A610   ; IN A,($BE)
site 2A612   ; IN A,($BE)
site 2A61B   ; OUT ($BF),A
site 2A624   ; OUT ($BF),A
site 2A626   ; IN A,($BE)
site 2A628   ; IN A,($BE)
site 2A62C   ; IN A,($BE)
site 2A62E   ; IN A,($BE)
site 2A630   ; IN A,($BE)
site 2A632   ; IN A,($BE)
site 2A634   ; IN A,($BE)
site 2A636   ; IN A,($BE)
site 2A63F   ; OUT ($BF),A
site 2A648   ; OUT ($BF),A
site 2A64A   ; IN A,($BE)
site 2A64C   ; IN A,($BE)
site 2A650   ; IN A,($BE)
site 2A652   ; IN A,($BE)
site 2A9BE   ; OUT ($BF),A
site 2A9C1   ; OUT ($BF),A
site 2A9CC   ; OUT ($BE),A
site 2A9CF   ; OUT ($BE),A
site 2A9D4   ; OUT ($BE),A
site 2A9D7   ; OUT ($BE),A
site 2A9E2   ; OUT ($BF),A
site 2A9E5   ; OUT ($BF),A
site 2A9EF   ; OUT ($BE),A
site 2A9F2   ; OUT ($BE),A
site 2A9F6   ; IN A,($BE)
site 2A9F8   ; IN A,($BE)
site 2ABDA   ; OUT ($BF),A
site 2ABDD   ; OUT ($BF),A
site 2ACE6   ; OUT ($BE),A
site 2ACE8   ; OUT ($BE),A
site 2ACEA   ; OUT ($BE),A
site 2ACED   ; OUT ($BE),A
site 2ACFA   ; OUT ($BE),A
site 2ACFC   ; OUT ($BE),A
site 2ACFE   ; OUT ($BE),A
site 2AD01   ; OUT ($BE),A
site 2AD19   ; OUT ($BE),A
site 2AD1B   ; OUT ($BE),A
site 2AD1D   ; OUT ($BE),A
site 2AD20   ; OUT ($BE),A
site 2AD38   ; OUT ($BE),A
site 2AD3A   ; OUT ($BE),A
site 2AD3C   ; OUT ($BE),A
site 2AD3F   ; OUT ($BE),A
site 2C0E1   ; IN A,($BE)
site 2C0E8   ; IN A,($BE)
site 2C10B   ; OUT ($BE),A
site 2C191   ; OUT ($BF),A
site 2C195   ; OUT ($BF),A
site 2C1A7   ; OUT ($BE),A
site 2C1AD   ; OUT ($BE),A
site 2C1C6   ; OUT ($BE),A
site 2C1CE   ; OUT ($BE),A
site 2C1F4   ; OUT ($BF),A
site 2C1F8   ; OUT ($BF),A
site 2C20A   ; OUT ($BE),A
site 2C210   ; OUT ($BE),A
site 2C229   ; OUT ($BE),A
site 2C231   ; OUT ($BE),A
site 2C259   ; OUT ($BF),A
site 2C25D   ; OUT ($BF),A
site 2C265   ; OTIR
site 2C285   ; OUT ($BF),A
site 2C289   ; OUT ($BF),A
site 2C2B1   ; OUT ($BE),A
site 2C2B4   ; OUT ($BE),A
site 2C417   ; OUT ($BF),A
site 2C41A   ; OUT ($BF),A
site 2C421   ; OUT ($BE),A
site 2C425   ; OUT ($BE),A
site 2C428   ; OUT ($BE),A
site 2C42A   ; OUT ($BE),A
site 2C431   ; OUT ($BF),A
site 2C434   ; OUT ($BF),A
site 2C43B   ; OUT ($BE),A
site 2C43F   ; OUT ($BE),A
site 2C442   ; OUT ($BE),A
site 2C444   ; OUT ($BE),A
site 2C44B   ; OUT ($BF),A
site 2C44E   ; OUT ($BF),A
site 2C455   ; OUT ($BE),A
site 2C459   ; OUT ($BE),A
site 2C45C   ; OUT ($BE),A
site 2C45E   ; OUT ($BE),A
site 2C464   ; OUT ($BF),A
site 2C467   ; OUT ($BF),A
site 2C469   ; IN A,($BE)
site 2C46B   ; IN A,($BE)
site 2C47A   ; OUT ($BF),A
site 2C47D   ; OUT ($BF),A
site 2C480   ; OUT ($BE),A
site 2C482   ; IN A,($BE)
site 2C485   ; OUT ($BE),A
site 2C48C   ; OUT ($BF),A
site 2C48F   ; OUT ($BF),A
site 2C491   ; IN A,($BE)
site 2C493   ; IN A,($BE)
site 2C497   ; OUT ($BE),A
site 2C499   ; IN A,($BE)
site 2C49C   ; OUT ($BE),A
site 2C4A2   ; OUT ($BF),A
site 2C4A5   ; OUT ($BF),A
site 2C4A7   ; IN A,($BE)
site 2C4A9   ; IN A,($BE)
site 2C4AD   ; OUT ($BE),A
site 2C4AF   ; IN A,($BE)
site 2C4B2   ; OUT ($BE),A
site 2C4B9   ; OUT ($BF),A
site 2C4BC   ; OUT ($BF),A
site 2C4BF   ; OUT ($BE),A
site 2C4C1   ; IN A,($BE)
site 2C4C4   ; OUT ($BE),A
site 2C4CE   ; OUT ($BF),A
site 2C4D2   ; OUT ($BF),A
site 2C4E2   ; OUT ($BF),A
site 2C4E5   ; OUT ($BF),A
site 2C4E7   ; IN A,($BE)
site 2C4E9   ; IN A,($BE)
site 2C4ED   ; OUT ($BF),A
site 2C4F0   ; OUT ($BF),A
site 2C4F5   ; OUT ($BE),A
site 2C4FC   ; OUT ($BF),A
site 2C4FF   ; OUT ($BF),A
site 2C501   ; IN A,($BE)
site 2C503   ; IN A,($BE)
site 2C507   ; OUT ($BF),A
site 2C50A   ; OUT ($BF),A
site 2C50E   ; OUT ($BE),A
site 2C544   ; OUT ($BF),A
site 2C548   ; OUT ($BF),A
site 2C55A   ; OUT ($BF),A
site 2C55E   ; OUT ($BF),A
site 2C56E   ; OUT ($BF),A
site 2C572   ; OUT ($BF),A
site 2C593   ; OUT ($BF),A
site 2C597   ; OUT ($BF),A
site 2C59E   ; OUT ($BF),A
site 2C5A2   ; OUT ($BF),A
site 2C736   ; OUT ($BF),A
site 2C739   ; OUT ($BF),A
site 2C73B   ; IN A,($BE)
site 2C73D   ; IN A,($BE)
site 2C741   ; IN A,($BE)
site 2C743   ; IN A,($BE)
site 2C745   ; IN A,($BE)
site 2C747   ; IN A,($BE)
site 2C750   ; OUT ($BF),A
site 2C759   ; OUT ($BF),A
site 2C75B   ; IN A,($BE)
site 2C75D   ; IN A,($BE)
site 2C766   ; OUT ($BF),A
site 2C769   ; OUT ($BF),A
site 2C76B   ; IN A,($BE)
site 2C76D   ; IN A,($BE)
site 2C776   ; OUT ($BF),A
site 2C77F   ; OUT ($BF),A
site 2C781   ; IN A,($BE)
site 2C783   ; IN A,($BE)
site 2C787   ; IN A,($BE)
site 2C78E   ; OUT ($BF),A
site 2C791   ; OUT ($BF),A
site 2C793   ; IN A,($BE)
site 2C79C   ; OUT ($BF),A
site 2C7A5   ; OUT ($BF),A
site 2C7A7   ; IN A,($BE)
site 2C7A9   ; IN A,($BE)
site 2C7AD   ; IN A,($BE)
site 2C7AF   ; IN A,($BE)
site 2C7B1   ; IN A,($BE)
site 2C7B3   ; IN A,($BE)
site 2C99C   ; OUT ($BF),A
site 2C99F   ; OUT ($BF),A
site 2CAB4   ; OUT ($BF),A
site 2CAB7   ; OUT ($BF),A
site 2CAD3   ; OUT ($BF),A
site 2CAD6   ; OUT ($BF),A
site 2CAE8   ; OUT ($BE),A
site 2CAED   ; OUT ($BE),A
site 2CAEF   ; IN A,($BE)
site 2CAF1   ; IN A,($BE)
site 2CAFD   ; OUT ($BE),A
site 2CB02   ; OUT ($BE),A
site 2CB04   ; IN A,($BE)
site 2CB06   ; IN A,($BE)
site 2D1ED   ; OUT ($BF),A
site 2D1F0   ; OUT ($BF),A
site 2D1F3   ; OUT ($BE),A
site 2D1FB   ; OUT ($BF),A
site 2D1FE   ; OUT ($BF),A
site 2D201   ; OUT ($BE),A
site 3012C   ; IN A,($BE)
site 30134   ; IN A,($BE)
site 3015F   ; OUT ($BE),A
site 30186   ; OUT ($BF),A
site 3018A   ; OUT ($BF),A
site 301C6   ; OUT ($BF),A
site 301CA   ; OUT ($BF),A
site 301DB   ; OUT ($BE),A
site 301E0   ; OUT ($BE),A
site 301EF   ; OUT ($BE),A
site 301F3   ; OUT ($BE),A
site 30210   ; OUT ($BF),A
site 30214   ; OUT ($BF),A
site 30226   ; OUT ($BE),A
site 3022C   ; OUT ($BE),A
site 30245   ; OUT ($BE),A
site 3024D   ; OUT ($BE),A
site 3025D   ; OUT ($BF),A
site 30261   ; OUT ($BF),A
site 30269   ; OUT ($BE),A
site 302CE   ; OUT ($BF),A
site 302D2   ; OUT ($BF),A
site 302FA   ; OUT ($BE),A
site 3030B   ; OUT ($BE),A
site 303B2   ; OUT ($BF),A
site 303B5   ; OUT ($BF),A
site 303BD   ; OUT ($BE),A
site 303C1   ; OUT ($BE),A
site 303C4   ; OUT ($BE),A
site 303C6   ; OUT ($BE),A
site 303CD   ; OUT ($BF),A
site 303D0   ; OUT ($BF),A
site 303D8   ; OUT ($BE),A
site 303DC   ; OUT ($BE),A
site 303DF   ; OUT ($BE),A
site 303E1   ; OUT ($BE),A
site 303E8   ; OUT ($BF),A
site 303EB   ; OUT ($BF),A
site 303F2   ; OUT ($BE),A
site 303F7   ; OUT ($BE),A
site 303FA   ; OUT ($BE),A
site 303FC   ; OUT ($BE),A
site 30628   ; OUT ($BF),A
site 3062B   ; OUT ($BF),A
site 30636   ; OUT ($BE),A
site 30639   ; OUT ($BE),A
site 3063D   ; OUT ($BE),A
site 30640   ; OUT ($BE),A
site 3064B   ; OUT ($BF),A
site 3064E   ; OUT ($BF),A
site 30652   ; OUT ($BE),A
site 30655   ; OUT ($BE),A
site 30659   ; OUT ($BE),A
site 3065C   ; OUT ($BE),A
site 30670   ; OUT ($BE),A
site 30673   ; OUT ($BE),A
site 30677   ; OUT ($BE),A
site 3067A   ; OUT ($BE),A
site 30685   ; OUT ($BF),A
site 30688   ; OUT ($BF),A
site 3068C   ; OUT ($BE),A
site 3068F   ; OUT ($BE),A
site 30693   ; OUT ($BE),A
site 30696   ; OUT ($BE),A
site 30A8C   ; OUT ($BF),A
site 30A8F   ; OUT ($BF),A
site 30AC0   ; OUT ($BE),A
site 30AD1   ; OUT ($BE),A
site 30B16   ; OUT ($BF),A
site 30B19   ; OUT ($BF),A
site 30B24   ; OUT ($BF),A
site 30B27   ; OUT ($BF),A
eihalt 2828E   ; EI : HALT
eihalt 28474   ; EI : HALT
eihalt 2860B   ; EI : HALT
eihalt 28A4E   ; EI : HALT
eihalt 28A63   ; EI : HALT
eihalt 28A6B   ; EI : HALT
eihalt 294A3   ; EI : HALT
eihalt 2A10E   ; EI : HALT
eihalt 2A46A   ; EI : HALT
eihalt 2A578   ; EI : HALT
eihalt 2A58E   ; EI : HALT
eihalt 2C3F7   ; EI : HALT
eihalt 2C6F1   ; EI : HALT
eihalt 30182   ; EI : HALT
eihalt 30395   ; EI : HALT
eihalt 305F7   ; EI : HALT
