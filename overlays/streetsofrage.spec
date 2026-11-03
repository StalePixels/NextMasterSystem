# Streets of Rage (Europe, Brazil) (En), CRC32 4AB3790F, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a 60 s and a 10 min reference I/O log
# (title, character select, round 1). The game runs code only in banks 0, 1 and 31: every
# jump or call into slot 2 maps bank 31 (the sound driver) first, through $1D2B. The I/O byte
# patterns in the other banks are data (data/scan-verdicts.tsv). The power-on LDIR at $0271
# writes 0, 0, 1, 2 to $FFFC-$FFFF, the mapping the game starts with, and is not patched.
# No line interrupts, no HALT. The frame handler at $0200 runs with interrupts off and ends
# with EI; RET.
name Streets of Rage
hz 50		; No-Intro regions Europe, Brazil
# The lamp posts in play are priority cells (a column of rows 5-23): sprites go behind them.
priority
cart 4AB3790F
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
site 00048   ; OUT ($BE),A
site 0005E   ; OUT (C),B
site 0008A   ; OUT ($BE),A
site 00098   ; OUT ($BE),A
site 00231   ; IN A,($DD)
site 00240   ; IN A,($BF)
site 002B4   ; IN A,($7E)
site 002C0   ; OTIR
site 00300   ; OUT ($BE),A
site 00314   ; OUT ($BE),A
site 0031A   ; OUT ($BE),A
site 0032D   ; OUT ($BE),A
site 00341   ; OUT ($BE),A
site 00347   ; OUT ($BE),A
site 0035C   ; OUT (C),A
site 00378   ; OUT ($BE),A
site 0037E   ; OUT ($BE),A
site 003A5   ; OUT ($BF),A
site 003AA   ; OUT ($BF),A
site 003B1   ; OUT ($BE),A
site 00644   ; IN A,($DC)
site 00970   ; OUT ($BE),A
site 0099B   ; OUT ($BE),A
site 009E2   ; OUT ($BE),A
site 009F1   ; OUT ($BE),A
site 009F4   ; OUT ($BE),A
site 00B54   ; OUT ($BE),A
site 00B85   ; OUT ($BF),A
site 00B89   ; OUT ($BF),A
site 00BAD   ; OUT ($BF),A
site 00BB1   ; OUT ($BF),A
site 00BBA   ; OUT ($BE),A
site 00BC0   ; OUT ($BF),A
site 00BC4   ; OUT ($BF),A
site 00BCA   ; OUT ($BE),A
site 0131F   ; OUT ($BF),A
site 01322   ; OUT ($BF),A
site 01325   ; OUT ($BE),A
site 01375   ; OUT ($BF),A
site 01379   ; OUT ($BF),A
site 01381   ; IN A,($BE)
site 01385   ; IN A,($BE)
site 014A3   ; OUT ($BF),A
site 014A7   ; OUT ($BF),A
site 014B0   ; OUT ($BE),A
site 014BB   ; OUT ($BF),A
site 014BF   ; OUT ($BF),A
site 014C8   ; OUT ($BE),A
site 014CC   ; OUT ($BE),A
site 0170B   ; OUT ($BF),A
site 0170E   ; OUT ($BF),A
site 01711   ; OUT ($BE),A
site 01714   ; OUT ($BE),A
site 01983   ; OUT ($BE),A
site 01991   ; OUT ($BE),A
site 01A09   ; OUT ($BE),A
site 01A5E   ; OUT ($BF),A
site 01A62   ; OUT ($BF),A
site 01A68   ; OUT ($BE),A
site 01A6A   ; OUT ($BE),A
site 01ABA   ; OUT ($BF),A
site 01ABD   ; OUT ($BF),A
site 01AC0   ; OUT ($BE),A
site 01AC7   ; OUT ($BE),A
site 01DE4   ; IN A,($DC)
site 01E27   ; OUT ($BE),A
site 077AF   ; OUT ($BE),A
site 077B3   ; OUT ($BE),A
site 0789B   ; OUT ($BF),A
site 0789E   ; OUT ($BF),A
site 078A1   ; OUT ($BE),A
site 078A7   ; OUT ($BE),A
site 078C1   ; IN A,($BE)
site 078C6   ; IN A,($BE)
site 078DB   ; OUT ($BE),A
site 078E2   ; OUT ($BE),A
site 07914   ; OUT ($BE),A
site 0791A   ; OUT ($BE),A
site 079D9   ; OUT ($BF),A
site 079DC   ; OUT ($BF),A
site 07AAF   ; OUT ($BE),A
site 07AB4   ; OUT ($BE),A
site 07AB9   ; OUT ($BE),A
site 07ABE   ; OUT ($BE),A
site 07E15   ; OUT ($BF),A
site 07E18   ; OUT ($BF),A
site 07E1B   ; OUT ($BE),A
site 07E1E   ; OUT ($BE),A
site 07E3A   ; OUT ($BF),A
site 07E3E   ; OUT ($BF),A
site 07E44   ; OUT ($BE),A
site 07E47   ; OUT ($BE),A
site 7C1C4   ; OUT ($7F),A
site 7C1CD   ; OUT ($7F),A
site 7C1DD   ; OUT ($7F),A
site 7C1EE   ; OUT ($7F),A
site 7C218   ; OUT ($7F),A
site 7C231   ; OUT ($7F),A
site 7C669   ; OUT ($7F),A
site 7C66D   ; OUT ($7F),A
site 7C671   ; OUT ($7F),A
site 7C675   ; OUT ($7F),A
site 7C679   ; OUT ($7F),A
mapst 00074   ; LD ($FFFF),A
mapst 00225   ; LD ($FFFF),A
mapst 0022E   ; LD ($FFFF),A
mapst 0039B   ; LD ($FFFF),A
mapst 0149E   ; LD ($FFFF),A
mapst 01D2E   ; LD ($FFFF),A
mapst 07888   ; LD ($FFFF),A
# The sprite table. The frame handler ($0200) first calls $02DD, which writes the Y table
# ($CA00, 64 bytes, to VRAM $3F00) and the X and tile table ($CA40 and $CA80 interleaved, 128
# bytes, to $3F80), in table order and reversed in turn ($C020 bit 0), so that more than 8
# sprites on a line flicker in turn. Its loops pad each write with PUSH HL; POP HL, so they
# cannot run as a trace: 192 single writes cost about 220,000 cycles a frame, and the frame
# handler then kept interrupts off past the Next's frame work, which ran between the Y writes
# and the X writes and paired new Y values with old X and tile values (the player missing or
# in pieces). The far call to sat writes both tables with one jt_vwrite each.
asm 002F1 6   ; RRCA; JR C,$0320; LD DE,$7F00 -> far call to sat, then RET
    rst $00
    db far_io, pg_sat, ent_sat
    ret
endasm
# The tile queue. The frame handler calls $0069, which runs one queued copy from $C380: $C380
# bit 7 set = queued, bit 0 = mode; $C381 the bank for slot 2; $C382 the VRAM address; $C384
# the source; $C386 and $C387 the count, as B and C of a DJNZ loop inside a DEC C loop: B
# bytes (0 = 256), then C - 1 passes of 256. Mode 0 copies the bytes ($0089); mode 1 writes
# each byte through the table at $0100 ($0096), which reverses its bits (tiles flipped left
# to right). Both loops write one byte at a time through the traps: one entry cost up to about
# 330,000 cycles and put a few round 1 frames over budget.
# The far call to qcopy, after the mapper write at $0074, writes the queued bytes with
# jt_vwrite.
asm 00078 5   ; LD E,(HL); INC HL; LD D,(HL); INC HL; RST $10 -> far call to qcopy, then RET
    rst $00
    db far_io, pg_qcopy, ent_qcopy
    ret
endasm
page 0 sat qcopy
; sat: A = the new $C020 (bit 0 set: reversed order). Writes VRAM $3F00-$3F3F and
; $3F80-$3FFF as $02F4-$031F (in order) or $0320-$034B (reversed) do. Keeps BC, IX, IY;
; A, DE, HL and F change, as in the game's routine. Runs with interrupts off (frame handler)
; on a stack of its own.
sat:    ld (.sp),sp
        ld sp,stk
        push bc
        push ix
        push iy
        rra
        jr c,.rev
        ld hl,$CA00             ; in order: Y[i] = $CA00+i, X[i] = $CA40+i, N[i] = $CA80+i
        ld de,ybuf
        ld bc,64
        ldir
        ld hl,$CA40
        ld b,64
.f:     ld a,(hl)
        ld (de),a
        inc de
        set 7,l                 ; $CA40+i -> $CA80+i ... $CA7F -> $CABF: L + $40
        res 6,l
        ld a,(hl)
        ld (de),a
        inc de
        res 7,l
        set 6,l
        inc l
        djnz .f
        jr .out
.rev:   ld hl,$CA3F             ; reversed: Y[i] = $CA3F-i, X[i] = $CA7F-i, N[i] = $CABF-i
        ld de,ybuf
        ld b,64
.ry:    ld a,(hl)
        ld (de),a
        inc de
        dec l
        djnz .ry
        ld hl,$CA7F
        ld b,64
.rx:    ld a,(hl)
        ld (de),a
        inc de
        set 7,l
        res 6,l
        ld a,(hl)
        ld (de),a
        inc de
        res 7,l
        set 6,l
        dec l
        djnz .rx
.out:   ld hl,ybuf
        ld de,$3F00
        ld bc,$4001             ; 64 bytes, 1 run
        ld ix,64
        ld iy,64
        ld a,1                  ; the source as mapped now (this page)
        call jt_vwrite
        ld hl,xnbuf
        ld de,$3F80
        ld bc,$8001             ; 128 bytes, 1 run
        ld ix,128
        ld iy,128
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        pop bc
        ld sp,(.sp)
        ret
.sp:    dw 0
; qcopy: C = the queue byte from $C380, HL = $C382; the bank for slot 2 is mapped. Writes the
; queued copy as $007C-$00A0 do and returns B = C = 0, as they do. Keeps IX and IY; A, DE, HL
; and F change. Runs with interrupts off (frame handler) on a stack of its own. On its first
; call it copies the game's bit-reverse table at $0100 into rev and fills idt with 0-255.
; Each byte goes through rev (mode 1) or idt (mode 0) into qbuf, and each 256 bytes of qbuf
; go to VRAM with one jt_vwrite.
qcopy:  ld (.sp),sp
        ld sp,stk
        push ix
        push iy
        ld de,($C382)           ; the VRAM address
        ld hl,($C384)           ; the source
        ld a,($C386)            ; the count: B bytes, then C - 1 passes of 256
        ld b,a
        ld a,($C387)
        ld (.va),de
        bit 0,c
        ld c,a
        ld a,rev>>8             ; mode 1: through rev
        jr nz,.m1
        ld a,idt>>8             ; mode 0: through idt, which keeps each byte
.m1:    ld (.lut+1),a
        ld a,(rev+$40)          ; rev holds $02 at $40 once it is filled
        cp $02
        jr z,.tok
        push hl
        push bc
        ld hl,$0100
        ld de,rev
        ld bc,256
        ldir                    ; DE = idt
        xor a
.id:    ld (de),a
        inc e
        inc a
        jr nz,.id
        pop bc
        pop hl
.tok:   ld de,qbuf
.run:   ld ixl,b                ; bytes left in this pass (0 = 256)
        ld a,h                  ; a run that can reach $2000-$3FFF reads through jt_peek
        cp $1F
        jr c,.fast
        cp $40
        jr c,.slow
.fast:  push bc
.lut:   ld b,0                  ; the table's page: rev or idt (patched)
.fb:    ld c,(hl)
        ld a,(bc)
        ld (de),a
        inc hl
        inc e
        call z,.flush
        dec ixl
        jr nz,.fb
        pop bc
        jr .next
.slow:  push bc
        ld a,(.lut+1)
        ld b,a
.sb:    call jt_peek
        ld c,a
        ld a,(bc)
        ld (de),a
        inc hl
        inc e
        call z,.flush
        dec ixl
        jr nz,.sb
        pop bc
.next:  ld b,0                  ; each pass after the first is 256 bytes
        dec c
        jr nz,.run
        ld a,e                  ; the bytes left in qbuf
        and a
        jr z,.out
        ld b,a
        call .wr
.out:   ld bc,0
        pop iy
        pop ix
        ld sp,(.sp)
        ret
.flush: push bc                 ; qbuf is full: 256 bytes
        ld b,0
        call .wr
        pop bc
        ret
.wr:    push hl                 ; writes B bytes (0 = 256) of qbuf at .va, then moves .va on
        push ix
        ld hl,qbuf
        ld de,(.va)
        ld c,1
        ld ix,256
        ld iy,256
        ld a,1                  ; the source as mapped now (this page)
        call jt_vwrite
        ld a,b
        add a,e                 ; .va + B, 0 = 256
        ld e,a
        jr nc,.w1
        inc d
.w1:    ld a,b
        and a
        jr nz,.w2
        inc d
.w2:    ld (.va),de
        ld de,qbuf
        pop ix
        pop hl
        ret
.sp:    dw 0
.va:    dw 0
ybuf:   ds 64                   ; ybuf and xnbuf are one block: the Y loops run on into xnbuf
xnbuf:  ds 128
        ds 64
stk:
        align 256
rev:    ds 256                  ; a copy of the game's table at $0100
idt:    ds 256                  ; idt[i] = i
qbuf:   ds 256
endpage

# Streets of Rage (Europe) (Action Replay).cht, "Infinite Lives P1"
poke "Infinite lives"
ar 00C0-1309
endpoke

# Streets of Rage (Europe) (Action Replay).cht, "Infinite Time"
poke "Infinite time"
ar 00C3-4909
ar 00C3-4A09
endpoke

# Streets of Rage (Europe, Brazil).cht, "Infinite Health P1"
poke "Infinite health"
ar 00CB-1900
endpoke

# Streets of Rage (Europe, Brazil).cht, "Invulnerability"
poke "Invincibility"
ar 00CB-2538
endpoke
