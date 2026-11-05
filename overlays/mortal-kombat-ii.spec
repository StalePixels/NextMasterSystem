# Mortal Kombat II (Europe, Brazil) (En), CRC32 2663BF18, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a 600 s reference I/O log (random input),
# then extended.
# Spec gaps (data/scan-verdicts.tsv): unused are a development-kit monitor at bank 2 $8000 (as in
# Mortal Kombat) and an interrupt handler at bank 31 $ABC7 that no word names; false are graphics
# and table bytes, and two operand bytes. The code the scan left unreached is patched below.
# Register 0 has line interrupts on and register 10 is always $FF, so no line interrupt fires.
name Mortal Kombat II
cart 2663BF18
hz 50		; No-Intro regions Europe, Brazil
# No free RST vector: $0000-$0002 (DI; LD SP part) becomes the vector,
# the game starts at $0004 with the SP its LD SP,nn set.
vector 00 io
start 0004 DFEE
# Delay $3BFC (bank 0): LD HL,$0000, then DEC HL : LD A,L : OR H : JR NZ,$3BFF : RET at $3BFF,
# 65536 passes of 26 T-states; $3BF6 runs it B times. The power-on hold ($5011), the legal text
# and logo holds ($9AD7) and bank 4 $BC73/$BC7A use it. A busy loop, so at 28 MHz every hold was
# about 8 times too short and the text screens went past before they showed.
# Page entry delay waits the same real time on the Next's raster line: a Master System frame of
# 71,364 T-states (PAL, 313 lines of 228) is a Next frame of 311 lines, so a pass is 29/256 of a line.
asm 03BFF 6          ; DEC HL : LD A,L : OR H : JR NZ,$3BFF : RET
    rst $00
    db far_io, pg_delay, ent_delay
    ret
endasm
# Frame wait $58A2 (bank 1): EI : HALT until the frame interrupt sets bit 5 of $C44F, then
# IN A,($7E) : DI : RET at $58B6. That read, just after the frame event, would run the runtime's
# frame work before the game's frame (rd_vcount: a read in the vertical blank with the work not
# yet done). The cave makes the read with vbl_done set, so it returns the same count and the work
# runs at the ULA interrupt, after the game has written the frame.
asm 058B6 4          ; IN A,($7E) : DI : RET
    rst $00
    db far_io, pg_vread, ent_vread
endasm
# Bank switch $7CF7 (bank 1, reached from $7B07, before the screen streamer $7BE5): LD HL,$FFFF :
# LD D,(HL) : LD (HL),A, a mapper store through HL with A, which no spec line form takes. The cave
# far-calls page entry bankd, which does the same through the runtime's mapper store; a NOP fills
# the fifth byte. Without it the streamer set a junk VDP address at $7C0B (registers 1-3 became $80),
# the frame interrupt went off and the game hung on a black screen after the difficulty menu.
asm 07CF7 5          ; LD HL,$FFFF : LD D,(HL) : LD (HL),A
    rst $00
    db far_io, pg_bankd, ent_bankd
    nop
endasm
page 0 delay vread bankd
; delay: as the game's $3BFF-$3C04, in real time. HL passes of 26 T-states (0 means 65536).
; Returns as the game's loop does: HL = 0, A = 0, flags as OR H with A = 0 (Z, P/V set; S, H, N, C
; clear); BC and DE kept. The interrupt state stays as it was, so the game's frame interrupt runs
; during the wait as during the game's loop; each line read runs with interrupts off, so a handler
; cannot change the NextReg select port between the select and the read. The entry uses no stack of
; its own (the game's interrupts can come while it runs, and they need the game's stack).
    macro RDLINE        ; HL = the Next's raster line, below (dlen); A, F, BC changed
        di
        ld bc,$243B
.again: ld a,$1E
        out (c),a
        inc b
        in h,(c)
        dec b
        ld a,$1F
        out (c),a
        inc b
        in l,(c)
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        xor h
        and 1
        jr nz,.again
        ld a,h
        and 1
        ld h,a
        jr z,.inrange           ; a read of line 511 comes at some line changes: a line of
        ld a,(dlen)             ; (dlen) or more is read again
        cp l
        jr c,.again
        jr z,.again
.inrange:
        ld a,(dirq)
        or a
        jr z,.noei
        ei
.noei:
    endm
delay:  ld (sv_bc),bc
        ld (sv_de),de
        ld a,h
        or l
        jr nz,.cnt
        ld hl,7424              ; 65536 passes
        jr .set
.cnt:   ex de,hl                ; DE = passes
        ld hl,0
        ld a,0                  ; A:HL = passes * 29, 24 bits
        ld b,29
.mul:   add hl,de
        adc a,0
        djnz .mul
        ld l,h
        ld h,a                  ; HL = passes * 29 / 256 lines
.set:   ld (dleft),hl
        ld a,i                  ; P/V: interrupts on at entry
        ld a,0
        jp po,.di
        inc a
.di:    ld (dirq),a
        di
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld hl,311               ; lines in a 50 Hz frame
        bit 2,a
        jr z,.hz
        ld hl,264               ; 60 Hz
.hz:    ld (dlen),hl
        RDLINE
        ld (dprev),hl
.poll:  RDLINE
        ld (dcur),hl
        ld de,(dprev)
        or a
        sbc hl,de               ; lines since the last read
        jr nc,.pos
        ld a,d                  ; a lower line: the frame wrapped only from line 256 or later.
        or a                    ; At line 256 the low byte can read 0 before the high byte
        jp z,.poll              ; reads 1: such a read is dropped
        ld de,(dlen)
        add hl,de               ; the frame wrapped
.pos:   ex de,hl
        ld hl,(dcur)
        ld (dprev),hl
        ld hl,(dleft)
        or a
        sbc hl,de
        ld (dleft),hl
        jr c,.end
        ld a,h
        or l
        jr nz,.poll
.end:   ld bc,(sv_bc)
        ld de,(sv_de)
        ld hl,0
        xor a
        ret
dirq:   db 0
dlen:   dw 0
dprev:  dw 0
dcur:   dw 0
dleft:  dw 0
sv_bc:  dw 0
sv_de:  dw 0
; vread: as the game's $58B6-$58B9 (IN A,($7E) : DI : RET, the far call returns to the RET at
; $58B9): the V counter read through the runtime's I/O RST with vbl_done ($E086) set first, so the
; read does not run the frame work, which the ULA interrupt then runs. A = the V counter,
; interrupts off; the other registers and F as the read leaves them.
VR_DONE equ $E086
vread:  ld a,1
        ld (VR_DONE),a
        rst $00
        db $0A                  ; IN A,(n), port class 2 ($7E: the V counter)
        di
        ret
; bankd: as the game's $7CF7-$7CFB: D = the slot 2 bank before the store, then A stored to $FFFF
; through the runtime's mapper store (inline code $13, LD ($FFFF),A, with its skipped third byte).
; HL is $FFFF on return as after the game's code; A, F and the other registers are kept.
bankd:  push af
        ld a,($FFFF)
        ld d,a
        pop af
        rst $00
        db $13, $FF
        ld hl,$FFFF
        ret
endpage
# Fighter tile streamer $2F2F (bank 0): a list at DE of run lengths; each run sends B groups of
# 4 bytes from HL to the VDP data port, through five loops that made one runtime call for every
# byte (about a quarter of the runtime's time in a fight). Code caves replace each loop with a
# page 1 entry that makes the same bytes in a buffer and writes them at the VDP address with
# jt_vwrite.
#   $2FD9: B groups, each 1 byte skipped and 4 bytes sent               -> grp_s
#   $3000: B groups of 4 bytes sent                                     -> grp_c
#   $304D: as $2FD9, each byte through the table at $0500 (PUSH DE ... POP DE) -> grp_sx
#   $3078: as $3000, each byte through the table at $0500             -> grp_cx
#   $302E: B zero bytes                                                 -> zfill
asm 02FD9 26         ; LD B,A : loop to JP NZ,$2FDA
    rst $00
    db far_io, pg_grp_s, ent_grp_s
    jp $2FF3
endasm
asm 03000 24         ; LD B,A : loop to JR NZ,$3001
    rst $00
    db far_io, pg_grp_c, ent_grp_c
    jp $3018
endasm
asm 0304D 30         ; LD B,A : PUSH DE : LD D,$05 : loop to JP NZ,$3051 : POP DE
    rst $00
    db far_io, pg_grp_sx, ent_grp_sx
    jp $306B
endasm
asm 03078 28         ; LD B,A : PUSH DE : LD D,$05 : loop to JR NZ,$307C : POP DE
    rst $00
    db far_io, pg_grp_cx, ent_grp_cx
    jp $3094
endasm
asm 0302E 7          ; LD B,A : XOR A : OUT ($BE),A : NOP : DJNZ $3030
    rst $00
    db far_io, pg_zfill, ent_zfill
    jp $3035
endasm
# Name table streamer $3880 (bank 0): after the VDP address, a row of D bytes (OUTI : DEC D : JR NZ
# at $38A8) or E bytes (OUTI : DEC E : JR NZ at $38CA) from HL, each OUTI one runtime call. Code caves
# call page 1 entries that write the row with jt_vwrite; a NOP fills the fifth byte.
asm 038A8 5          ; OUTI : DEC D : JR NZ,$38A8
    rst $00
    db far_io, pg_run_d, ent_run_d
    nop
endasm
asm 038CA 5          ; OUTI : DEC E : JR NZ,$38CA
    rst $00
    db far_io, pg_run_e, ent_run_e
    nop
endasm
page 1 grp_s grp_c grp_sx grp_cx zfill run_d run_e
; The group loops of $2F2F, as the game's code leaves them: B = 0, HL past the source bytes read,
; A = the last byte sent; C, DE, IX, IY and the alternate registers kept; F changed (the game's
; code after each loop sets it again). A = the group count at entry, 0 meaning 256. The bytes are
; made in buf and written at the VDP address with jt_vwrite (wchunk), which leaves VRAM and the VDP
; state as the game's data writes would. Each entry runs with interrupts off on this page's stack
; (ENTER), and turns them on again, if they were on, only back on the game's stack just before its
; RET (leave).
    macro ENTER         ; A = the mode; records the interrupt state, DI, this page's stack
        ld (mode),a
        ld a,i                  ; P/V = IFF2
        di
        ld a,0
        jp po,.di
        inc a
.di:    ld (ei_f),a
        ld (g_sp),sp
        ld sp,stk_top
    endm
grp_s:  ld (cnt),a
        ld a,1                  ; skip one byte before each group
        jr grp
grp_c:  ld (cnt),a
        xor a
        jr grp
grp_sx: ld (cnt),a
        ld a,3                  ; skip, and the table
        jr grp
grp_cx: ld (cnt),a
        ld a,2
grp:    ENTER
        ld (sv_bc),bc
        ld (sv_de),de
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld a,(cnt)              ; BC = groups (0 = 256)
        ld c,a
        ld b,0
        or a
        jr nz,.nz
        inc b
.nz:    ld (gl),bc
        push hl
        ld h,b
        ld l,c
        add hl,hl
        add hl,hl               ; 4 * groups
        ld a,(mode)
        rra
        jr nc,.len
        add hl,bc               ; 5 * groups
.len:   ex de,hl                ; DE = source bytes
        pop hl                  ; HL = source
        call srcok
        ld de,buf
        jr nz,.slow
.g:     ld a,(mode)             ; fast: the source read directly
        rra
        jr nc,.ns
        inc hl
.ns:    rra
        jr c,.x
        ldi
        ldi
        ldi
        ldi
        jr .gn
.x:     ld b,4
.xl:    ld a,(hl)
        inc hl
        push hl
        ld l,a
        ld h,$05
        ld a,(hl)
        pop hl
        ld (de),a
        inc de
        djnz .xl
.gn:    ld bc,(gl)
        dec bc
        ld (gl),bc
        ld a,b
        or c
        jr nz,.g
        jr .write
.slow:  ld a,(mode)             ; slow: the source through jt_peek
        rra
        jr nc,.ps
        inc hl
.ps:    ld b,4
.pl:    call jt_peek
        inc hl
        ld c,a
        ld a,(mode)
        and 2
        ld a,c
        jr z,.pw
        push hl
        ld l,a
        ld h,$05
        ld a,(hl)
        pop hl
.pw:    ld (de),a
        inc de
        djnz .pl
        ld bc,(gl)
        dec bc
        ld (gl),bc
        ld a,b
        or c
        jr nz,.slow
.write: ld (sv_hl),hl
        dec de
        ld a,(de)
        ld (last),a
        ld a,(cnt)              ; 4 * groups bytes
        ld l,a
        ld h,0
        or a
        jr nz,.w1
        inc h
.w1:    add hl,hl
        add hl,hl
        ld de,buf
        ld a,1
        call wchunk
        ld hl,(sv_hl)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld b,0
        jp leave
; zfill: as $302E-$3034: A zero bytes at the VDP address (0 meaning 256). Returns A = 0, B = 0,
; the other registers kept.
zfill:  ld (cnt),a
        ENTER
        ld (sv_bc),bc
        ld (sv_de),de
        ld (sv_hl),hl
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld a,(cnt)
        ld l,a
        ld h,0
        or a
        jr nz,.n
        inc h
.n:     ld de,zero
        ld a,1
        call wchunk
        ld hl,(sv_hl)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld b,0
        xor a
        ld (last),a
        jp leave
; run_d / run_e: as $38A8 / $38CA: D (or E) bytes (0 = 256) from HL at the VDP address. Returns
; D (or E) = 0, B less the count, HL past the bytes; A, C, the other registers kept; F changed
; (the game's code after each loop sets it again).
run_d:  ld (last),a
        ld a,d
        ld d,0
        jr run
run_e:  ld (last),a
        ld a,e
        ld e,0
run:    ld (cnt),a
        ENTER
        ld (sv_bc),bc
        ld (sv_de),de
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld a,(cnt)              ; BC = bytes (0 = 256)
        ld c,a
        ld b,0
        or a
        jr nz,.nz
        inc b
.nz:    ld (gl),bc
        push hl
        ld d,b
        ld e,c
        call srcok
        pop hl
        ld de,buf
        jr nz,.slow
        ldir
        jr .write
.slow:  call jt_peek
        ld (de),a
        inc de
        inc hl
        dec bc
        ld a,b
        or c
        jr nz,.slow
.write: ld (sv_hl),hl
        ld hl,(gl)
        ld de,buf
        ld a,1
        call wchunk
        ld hl,(sv_hl)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld a,(cnt)
        neg
        add a,b
        ld b,a                  ; B less the count
        jp leave
; leave: back to the game's stack, A = (last), interrupts on again if they were on at entry.
leave:  ld sp,(g_sp)
        ld a,(ei_f)
        or a
        ld a,(last)
        ret z
        ei
        ret
; srcok: Z when the DE bytes from HL avoid $2000-$3FFF, where this page sits in place of the
; game's bank 0, and do not wrap past $FFFF; NZ else. Keeps BC, DE and HL.
srcok:  push hl
        add hl,de
        jr c,.bad               ; past $FFFF
        dec hl                  ; the last byte
        ld a,h
        cp $20
        jr c,.ok                ; ends below $2000
        pop hl
        push hl
        ld a,h
        cp $40
        jr nc,.ok               ; starts at $4000 or above
.bad:   pop hl
        or 1
        ret
.ok:    pop hl
        xor a
        ret
; wchunk: HL bytes (1 to 1024) from DE at the VDP address, in runs of up to 256 bytes. A: as
; jt_vwrite's A. Changes every register; IX and IY are left 0.
wchunk: ld (wflag),a
.next:  ld a,h
        or l
        ret z
        ld c,l
        ld a,h
        or a
        jr z,.last
        dec h
        ld c,0
        jr .go
.last:  ld hl,0
.go:    ld (wleft),hl
        ex de,hl
        ld de,(vdp_addr)
        ld b,c
        ld c,1
        ld ix,0
        ld iy,0
        ld a,(wflag)
        call jt_vwrite
        ld c,b
        ld a,c
        or a
        jr nz,.add
        inc h
        jr .st
.add:   add a,l
        ld l,a
        jr nc,.st
        inc h
.st:    ex de,hl
        ld hl,(wleft)
        jr .next
wflag:  db 0
wleft:  dw 0
cnt:    db 0
mode:   db 0
last:   db 0
ei_f:   db 0
g_sp:   dw 0
gl:     dw 0
sv_bc:  dw 0
sv_de:  dw 0
sv_hl:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
stk:    ds 64
stk_top:
zero:   ds 256
buf:    ds 1024
endpage
# Sprite table writer $67E1 (bank 1): the Y list from $C502 and then the X and tile list from $C580,
# in an order that rotates every frame. Each byte was a single OUTI through the runtime (about 4,500
# cycles each, about a tenth of the runtime's time in a fight). Code caves at the two loops call
# page 2 entries that run the same index steps into a buffer and write it with one jt_vwrite call
# at the VDP address the game set.
asm 06827 7          ; LD C,$BE : the Y loop $6829-$6839 (JR Z,$683A ends it)
    rst $00
    db far_io, pg_saty, ent_saty
    jp $683A
endasm
asm 06855 5          ; LD B,D : SET 7,D : SLA E : the X and tile loop $685A-$687C (RET at $6870)
    rst $00
    db far_io, pg_satx, ent_satx
    ret
endasm
page 2 saty satx
; saty: as $6827-$6839. B bytes (0 = 256) from $C5xx, starting at L; after each byte L becomes
; L+E, and when that is not below D, L+E-D+2 (8-bit). Returns C = $BE, B = 0, A = the last L read,
; HL = $C5xx just past the last byte read; D, E, IX, IY and the alternates kept.
; satx: as $6855-$6870 (the game's SLA D at $6853 has run). D2 = D OR $80, E2 = E*2, B = D bytes
; (0 = 256), in pairs from $C5xx
; starting at L; after each pair L becomes L+E2, and when that carries or is not below D2,
; L+E2-D2+$80 (8-bit). Returns as the game's RET at $6870: B = 0, A = the last L+E2, HL just past
; the last byte read, D = D2, E = E2; C, IX, IY and the alternates kept.
; Both run with interrupts off on this page's stack and turn them on again, if they were on, only
; back on the game's stack just before their RET.
    macro ENTER
        ld a,i                  ; P/V = IFF2
        di
        ld a,0
        jp po,.di
        inc a
.di:    ld (ei_f),a
        ld (g_sp),sp
        ld sp,stk_top
        ld (sv_ix),ix
        ld (sv_iy),iy
    endm
saty:   ENTER
        ld c,b                  ; count (0 = 256)
        push de
        ld ix,buf
        ld a,l
.loop:  ld l,a
        ld (lastl),a
        ld a,(hl)               ; HL is $C5xx: RAM, never in this page's slot
        ld (ix+0),a
        inc ix
        inc hl
        dec c
        jr z,.done
        ld a,(lastl)
        add a,e
        cp d
        jr c,.loop
        sub d
        add a,2
        jr .loop
.done:  ld (sv_hl),hl
        ld a,b                  ; bytes written: B (0 = 256)
        call flush
        pop de
        ld hl,(sv_hl)
        ld bc,$00BE
        jp leave
satx:   ENTER
        ld a,d
        ld b,a                  ; B = D
        or $80
        ld d,a                  ; D2
        sla e                   ; E2
        push bc
        ld c,b                  ; bytes left (0 = 256)
        ld ix,buf
        ld a,l
.loop:  ld l,a
        ld (lastl),a
        ld a,(hl)
        ld (ix+0),a
        inc hl
        ld a,(hl)
        ld (ix+1),a
        inc hl
        inc ix
        inc ix
        dec c
        dec c
        jr z,.done
        ld a,(lastl)
        add a,e
        jr c,.wrap
        cp d
        jr c,.loop
.wrap:  sub d
        add a,$80
        jr .loop
.done:  ld (sv_hl),hl
        ld a,(lastl)
        add a,e
        ld (lastl),a
        pop bc
        ld a,b
        push de
        call flush
        pop de
        ld hl,(sv_hl)
        ld b,0
        jp leave
; flush: A bytes (0 = 256) from buf at the VDP address with one jt_vwrite. Changes AF, BC, HL,
; IX and IY.
flush:  ld b,a
        ld c,1
        ld hl,buf
        push de
        ld de,(vdp_addr)
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        pop de
        ret
; leave: back to the game's stack with IX and IY restored, A = (lastl); interrupts on again if
; they were on. F changed.
leave:  ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld sp,(g_sp)
        ld a,(ei_f)
        or a
        ld a,(lastl)
        ret z
        ei
        ret
lastl:  db 0
ei_f:   db 0
g_sp:   dw 0
sv_hl:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
stk:    ds 64
stk_top:
buf:    ds 256
endpage
# Fighter tile renderer $2566 (bank 0): it masks the fighter's tile rows over the background rows
# and sends them as tile data, 4 bytes a group. Each byte went through the runtime. Code caves call
# page 3 entries that make the same bytes in a buffer and write them with jt_vwrite.
#   $2586: 8 groups (mask byte at HL, then 4 rows (DE) AND mask OR (HL)), B kept -> msk8
#   $277F, $27CC: the same group, B groups (DJNZ)                             -> msk
#   $2801: A groups of 4 bytes from HL (OUTI, with INC B after 3 of the 4)    -> cp4
#   $26AF, $2D65: B groups of 4 bytes, each through the table at D            -> xl
asm 02586 240        ; 8 x (LD C,(HL) : INC HL : 4 x (LD A,(DE) : AND C : OR (HL) : OUT ($BE),A : INC DE : INC HL))
    rst $00
    db far_io, pg_msk8, ent_msk8
    jp $2676
endasm
asm 0277F 32         ; LD C,(HL) : INC HL : 4 x (...) : DJNZ $277F
    rst $00
    db far_io, pg_msk, ent_msk
    jp $279F
endasm
asm 027CC 32         ; LD C,(HL) : INC HL : 4 x (...) : DJNZ $27CC
    rst $00
    db far_io, pg_msk, ent_msk
    jp $27EC
endasm
asm 02801 20         ; 4 x (OUTI : JR $+2 : INC B), no INC B after the last : DEC A : JR NZ,$2801
    rst $00
    db far_io, pg_cp4, ent_cp4
    jp $2815
endasm
asm 026AF 30         ; 4 x (LD E,(HL) : LD A,(DE) : NOP : NOP : OUT ($BE),A : INC HL) : DJNZ $26AF
    rst $00
    db far_io, pg_xl, ent_xl
    jp $26CD
endasm
asm 02D65 30         ; 4 x (LD E,(HL) : LD A,(DE) : NOP : NOP : OUT ($BE),A : INC HL) : DJNZ $2D65
    rst $00
    db far_io, pg_xl, ent_xl
    jp $2D83
endasm
page 3 msk8 msk cp4 xl
; Each entry returns the registers and flags as the game's code leaves them:
;   msk8: A = the last byte sent, C = the last mask, DE + 32, HL + 40, B kept, F as the last OR.
;   msk:  the same for B groups (0 = 256): DE + 4B, HL + 5B, B = 0.
;   cp4:  A groups (0 = 256) of 4 bytes from HL: HL + 4A, B - A, A = 0, F as DEC A to 0 with
;         the carry kept.
;   xl:   B groups (0 = 256): each of 4 bytes is the byte at D:(HL); HL + 4B, E = the last (HL),
;         A = the last byte sent, B = 0, F as at entry.
; Every other register is kept. Sources are read as the game sees them (jt_peek for $2000-$3FFF,
; where this page sits). Each entry saves the game's AF with one transient PUSH on the game's
; stack, then runs with interrupts off on this page's stack, and turns them on again, if they were
; on, only back on the game's stack just before its RET.
    macro ENTER
        ld (sv_hl),hl
        push af
        pop hl
        ld (sv_af),hl
        ld a,i                  ; P/V = IFF2
        di
        ld a,$00                ; NOP
        jp po,.di
        ld a,$FB                ; EI
.di:    ld (leave.e),a
        ld (g_sp),sp
        ld sp,stk_top
        ld (sv_bc),bc
        ld (sv_de),de
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld hl,(sv_af)
        push hl
        pop af
        ld hl,(sv_hl)
    endm
; msk8 / msk: groups of a mask byte and 4 rows.
msk8:   ENTER
        ld a,1
        ld (keepb),a
        ld a,8
        jr mskgo
msk:    ENTER
        xor a
        ld (keepb),a
        ld a,b
mskgo:  ld (cnt),a
        ld ix,buf
        ld b,a
.g:     call rdhl
        ld (lastm),a
        inc hl
        ld c,4
.r:     ex de,hl
        call rdhl
        ex de,hl
        push bc
        ld b,a
        ld a,(lastm)
        and b
        ld b,a
        call rdhl
        or b
        pop bc
        ld (ix+0),a
        inc ix
        inc de
        inc hl
        dec c
        jr nz,.r
        djnz .g
        ld (sv_hl),hl
        ld (sv_de),de
        ld a,(ix-1)
        ld (last),a
        ld a,(cnt)
        call wgrp
        ld hl,(sv_hl)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld a,(lastm)
        ld c,a
        ld a,(keepb)
        or a
        jr nz,.k
        ld b,0
.k:     ld a,(last)
        or a                    ; F as the last OR (HL) left it
        jp leave
; cp4: A groups of 4 bytes from HL.
cp4:    ENTER
        ld (cnt),a
        ld ix,buf
        ld c,a
.g:     ld b,4
.b:     call rdhl
        ld (ix+0),a
        inc ix
        inc hl
        djnz .b
        dec c
        jr nz,.g
        ld (sv_hl),hl
        ld a,(cnt)
        call wgrp
        ld hl,(sv_hl)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld a,(cnt)
        neg
        add a,b
        ld b,a                  ; B - groups
        ld a,(sv_af)            ; F at entry: its carry
        rra
        ld a,1
        dec a                   ; A = 0, Z, N; carry kept
        jp leave
; xl: B groups of 4 bytes, each the byte at D:(HL).
xl:     ENTER
        ld a,b
        ld (cnt),a
        ld ix,buf
.g:     ld c,4
.b:     call rdhl
        ld e,a
        ex de,hl
        call rdhl
        ex de,hl
        ld (ix+0),a
        inc ix
        inc hl
        dec c
        jr nz,.b
        djnz .g
        ld (sv_hl),hl
        ld (sv_de),de
        ld a,(ix-1)
        ld (last),a
        ld a,(cnt)
        call wgrp
        ld hl,(sv_af)           ; F as at entry, A = the last byte sent
        ld a,(last)
        ld h,a
        ld (sv_af),hl
        ld hl,(sv_hl)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld b,0
        push hl
        ld hl,(sv_af)
        ex (sp),hl
        pop af
; leave: IX and IY restored, back to the game's stack, then EI if interrupts were on at entry
; (written at .e by ENTER), and RET. Keeps every register and flag it is given.
leave:  ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld sp,(g_sp)
.e:     nop
        ret
; rdhl: A = the byte the game sees at HL. Keeps every register but A and F.
rdhl:   ld a,h
        and $E0
        cp $20
        jp z,jt_peek
        ld a,(hl)
        ret
; wgrp: A groups (0 = 256) of 4 bytes from buf at the VDP address. Changes every register but
; IX and IY, which are left 0.
wgrp:   ld l,a
        ld h,0
        or a
        jr nz,.n
        inc h
.n:     add hl,hl
        add hl,hl
        ld de,buf
        ld a,1
; wchunk: HL bytes (1 to 1024) from DE at the VDP address, in runs of up to 256 bytes. A: as
; jt_vwrite's A.
wchunk: ld (wflag),a
.next:  ld a,h
        or l
        ret z
        ld c,l
        ld a,h
        or a
        jr z,.last
        dec h
        ld c,0
        jr .go
.last:  ld hl,0
.go:    ld (wleft),hl
        ex de,hl
        ld de,(vdp_addr)
        ld b,c
        ld c,1
        ld ix,0
        ld iy,0
        ld a,(wflag)
        call jt_vwrite
        ld c,b
        ld a,c
        or a
        jr nz,.add
        inc h
        jr .st
.add:   add a,l
        ld l,a
        jr nc,.st
        inc h
.st:    ex de,hl
        ld hl,(wleft)
        jr .next
wflag:  db 0
wleft:  dw 0
cnt:    db 0
keepb:  db 0
lastm:  db 0
last:   db 0
g_sp:   dw 0
sv_af:  dw 0
sv_bc:  dw 0
sv_de:  dw 0
sv_hl:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
stk:    ds 64
stk_top:
buf:    ds 1024
endpage
site 0194B   ; OUT ($BF),A
site 01950   ; OUT ($BF),A
site 01956   ; OUT ($BF),A
site 0195B   ; OUT ($BF),A
site 019E6   ; OUT ($BF),A
site 019EA   ; OUT ($BF),A
site 019F0   ; OUT ($BF),A
site 019F4   ; OUT ($BF),A
site 019FA   ; OUT ($BF),A
site 019FE   ; OUT ($BF),A
site 01A04   ; OUT ($BF),A
site 01A08   ; OUT ($BF),A
site 01A0E   ; OUT ($BF),A
site 01A12   ; OUT ($BF),A
site 01A32   ; OUTI
site 01A48   ; OUT ($BE),A
site 01A50   ; OUT ($BE),A
site 01A5A   ; OUT ($BE),A
site 01A64   ; OUT ($BE),A
site 01A7B   ; OUT ($BE),A
site 01A86   ; OUT ($BE),A
site 01A8B   ; OUT ($BE),A
site 01A95   ; OUT ($BE),A
site 01B65   ; OUT ($BF),A
site 01B69   ; OUT ($BF),A
site 01B6F   ; OUT ($BF),A
site 01B73   ; OUT ($BF),A
site 01B90   ; OUT ($BF),A
site 01B94   ; OUT ($BF),A
site 01CB9   ; OUT ($BF),A
site 01CBD   ; OUT ($BF),A
site 02754   ; OUTI
site 02759   ; OUTI
site 0275E   ; OUTI
site 02763   ; OUTI
site 0284E   ; OUT ($BE),A
site 02859   ; OUT ($BE),A
site 02864   ; OUT ($BE),A
site 0286F   ; OUT ($BE),A
site 0287E   ; OUT ($BE),A
site 02889   ; OUT ($BE),A
site 02894   ; OUT ($BE),A
site 0289F   ; OUT ($BE),A
site 028AE   ; OUT ($BE),A
site 028B9   ; OUT ($BE),A
site 028C4   ; OUT ($BE),A
site 028CF   ; OUT ($BE),A
site 028DE   ; OUT ($BE),A
site 028E9   ; OUT ($BE),A
site 028F4   ; OUT ($BE),A
site 028FF   ; OUT ($BE),A
site 0290E   ; OUT ($BE),A
site 02919   ; OUT ($BE),A
site 02924   ; OUT ($BE),A
site 0292F   ; OUT ($BE),A
site 0293E   ; OUT ($BE),A
site 02949   ; OUT ($BE),A
site 02954   ; OUT ($BE),A
site 0295F   ; OUT ($BE),A
site 0296E   ; OUT ($BE),A
site 02979   ; OUT ($BE),A
site 02984   ; OUT ($BE),A
site 0298F   ; OUT ($BE),A
site 0299E   ; OUT ($BE),A
site 029A9   ; OUT ($BE),A
site 029B4   ; OUT ($BE),A
site 029BF   ; OUT ($BE),A
site 02A14   ; OUTI
site 02A19   ; OUTI
site 02A1E   ; OUTI
site 02A23   ; OUTI
site 02A5B   ; OUT ($BE),A
site 02A66   ; OUT ($BE),A
site 02A71   ; OUT ($BE),A
site 02A7C   ; OUT ($BE),A
site 02ABB   ; OUT ($BE),A
site 02AC6   ; OUT ($BE),A
site 02AD1   ; OUT ($BE),A
site 02ADC   ; OUT ($BE),A
site 02B3A   ; OUT ($BE),A
site 02B3F   ; OUT ($BE),A
site 02B44   ; OUT ($BE),A
site 02B49   ; OUT ($BE),A
site 02B70   ; OUT ($BE),A
site 02B76   ; OUT ($BE),A
site 02B7C   ; OUT ($BE),A
site 02B82   ; OUT ($BE),A
site 02C0E   ; OUT ($BE),A
site 02C14   ; OUT ($BE),A
site 02C1A   ; OUT ($BE),A
site 02C20   ; OUT ($BE),A
site 02C49   ; OUT ($BE),A
site 02C50   ; OUT ($BE),A
site 02C56   ; OUT ($BE),A
site 02C5C   ; OUT ($BE),A
site 02CCC   ; OUT ($BE),A
site 02CD1   ; OUT ($BE),A
site 02CD6   ; OUT ($BE),A
site 02CDB   ; OUT ($BE),A
site 02D1D   ; OUTI
site 02D22   ; OUTI
site 02D27   ; OUTI
site 02D2C   ; OUTI
site 02DD6   ; OUTI
site 02DDB   ; OUTI
site 02DE0   ; OUTI
site 02DE5   ; OUTI
site 02E0C   ; OUT ($BE),A
site 02E11   ; OUT ($BE),A
site 02E16   ; OUT ($BE),A
site 02E1B   ; OUT ($BE),A
site 02EE5   ; OUT ($BF),A
site 02EEA   ; OUT ($BF),A
site 0357E   ; OUT ($BF),A
site 03583   ; OUT ($BF),A
site 035CB   ; OUT ($BF),A
site 035D0   ; OUT ($BF),A
site 035EF   ; OUT ($BF),A
site 035F4   ; OUT ($BF),A
site 0360D   ; OUT ($BF),A
site 03612   ; OUT ($BF),A
site 03632   ; OUT ($BE),A
site 03639   ; OUT ($BE),A
site 03641   ; OUT ($BF),A
site 03646   ; OUT ($BF),A
site 03650   ; OUT ($BE),A
site 03657   ; OUT ($BE),A
site 036AA   ; OUT ($BE),A
site 036B1   ; OUT ($BE),A
site 03720   ; OUT ($BF),A
site 03725   ; OUT ($BF),A
site 037A0   ; OUT ($BF),A
site 037A5   ; OUT ($BF),A
site 037B6   ; OUT ($BE),A
site 037BC   ; OUT ($BE),A
site 037D4   ; OUTI
site 037DA   ; OUTI
site 037F4   ; OUTI
site 037FA   ; OUTI
site 03807   ; OUT ($BF),A
site 0380E   ; OUT ($BF),A
site 03817   ; IN A,($BF)
site 03832   ; IN A,($DD)
site 038D4   ; OUT ($BF),A
site 038D9   ; OUT ($BF),A
site 03C14   ; OUT ($BF),A
site 03C18   ; OUT ($BF),A
site 03C42   ; OUT (C),A
site 03C4A   ; OUTI
site 05068   ; OUT ($BF),A
site 0506C   ; OUT ($BF),A
site 05072   ; OUT ($BF),A
site 05076   ; OUT ($BF),A
site 0507C   ; OUT ($BF),A
site 05080   ; OUT ($BF),A
site 05086   ; OUT ($BF),A
site 0508A   ; OUT ($BF),A
site 05090   ; OUT ($BF),A
site 05094   ; OUT ($BF),A
site 0509A   ; OUT ($BF),A
site 0509E   ; OUT ($BF),A
site 050A4   ; OUT ($BF),A
site 050A8   ; OUT ($BF),A
site 050AE   ; OUT ($BF),A
site 050B2   ; OUT ($BF),A
site 050B8   ; OUT ($BF),A
site 050BC   ; OUT ($BF),A
site 050C2   ; OUT ($BF),A
site 050C6   ; OUT ($BF),A
site 050D1   ; OUT ($BF),A
site 050D5   ; OUT ($BF),A
site 055C5   ; IN A,($DC)
site 055E0   ; IN A,($DC)
site 055EB   ; IN A,($DD)
site 056BC   ; OUT ($BF),A
site 056C1   ; OUT ($BF),A
site 056E7   ; OUT ($BE),A
site 05746   ; OUT ($BE),A
site 057A3   ; OUT ($BF),A
site 057A7   ; OUT ($BF),A
site 057E1   ; OUT ($BF),A
site 057E5   ; OUT ($BF),A
site 057E8   ; OUT ($BE),A
site 057ED   ; OUT ($BF),A
site 057F1   ; OUT ($BF),A
site 0582A   ; OUT ($BF),A
site 0582E   ; OUT ($BF),A
site 05844   ; OUT ($BF),A
site 05848   ; OUT ($BF),A
site 058A7   ; IN A,($BF)
site 058BE   ; OUT ($7F),A
site 058C2   ; OUT ($7F),A
site 058C6   ; OUT ($7F),A
site 058CA   ; OUT ($7F),A
site 058D7   ; OUT ($BF),A
site 058DB   ; OUT ($BF),A
site 058E0   ; OUT ($BF),A
site 058E4   ; OUT ($BF),A
site 0596E   ; OUT ($BF),A
site 05973   ; OUT ($BF),A
otir 05999   ; OUTI
site 059C6   ; OUTI
site 059D8   ; OUT ($BE),A
site 059EA   ; OUT ($BF),A
site 059F0   ; OUT ($BF),A
site 059FD   ; OUT ($BE),A
site 05A03   ; OUT ($BE),A
site 05A15   ; OUT ($BE),A
site 05A3F   ; OUT ($BE),A
site 05ACF   ; OUT ($BE),A
site 05AE5   ; OUT ($BE),A
site 05AFB   ; OUT ($BE),A
site 05B11   ; OUT ($BE),A
site 05B3E   ; OUT ($BE),A
site 05B46   ; OUT ($BE),A
site 05BB7   ; OUTI
site 05BC4   ; OUT ($BE),A
site 05C4C   ; OUT ($BF),A
site 05C51   ; OUT ($BF),A
site 05C64   ; OUT ($BE),A
site 05C6D   ; OUT ($BE),A
site 05C74   ; OUT ($BF),A
site 05C79   ; OUT ($BF),A
site 05C82   ; OUT ($BE),A
site 05C88   ; OUT ($BE),A
site 05D75   ; OUT ($BF),A
site 05D7A   ; OUT ($BF),A
site 05DB7   ; OUTI
site 05DBC   ; OUTI
site 05DD2   ; OUT ($BF),A
site 05DD7   ; OUT ($BF),A
site 05E11   ; OUTI
site 05E14   ; OUTI
site 05E17   ; OUTI
site 05E1A   ; OUTI
site 05E22   ; OUTI
site 05E25   ; OUTI
site 05E28   ; OUTI
site 05E2B   ; OUTI
site 05E33   ; OUTI
site 05E36   ; OUTI
site 05E39   ; OUTI
site 05E3C   ; OUTI
site 05E44   ; OUTI
site 05E47   ; OUTI
site 05E4A   ; OUTI
site 05E4D   ; OUTI
site 05E55   ; OUTI
site 05E58   ; OUTI
site 05E5B   ; OUTI
site 05E5E   ; OUTI
site 05E66   ; OUTI
site 05E69   ; OUTI
site 05E6C   ; OUTI
site 05E6F   ; OUTI
site 05E77   ; OUTI
site 05E7A   ; OUTI
site 05E7D   ; OUTI
site 05E80   ; OUTI
site 05E88   ; OUTI
site 05E8B   ; OUTI
site 05E8E   ; OUTI
site 05E91   ; OUTI
site 05E99   ; OUTI
site 05E9C   ; OUTI
site 05E9F   ; OUTI
site 05EA2   ; OUTI
site 05EAA   ; OUTI
site 05EAD   ; OUTI
site 05EB0   ; OUTI
site 05EB3   ; OUTI
site 05EBB   ; OUTI
site 05EBE   ; OUTI
site 05EC1   ; OUTI
site 05EC4   ; OUTI
site 05ECC   ; OUTI
site 05ECF   ; OUTI
site 05ED2   ; OUTI
site 05ED5   ; OUTI
site 05EDD   ; OUTI
site 05EE0   ; OUTI
site 05EE3   ; OUTI
site 05EE6   ; OUTI
site 05EEE   ; OUTI
site 05EF1   ; OUTI
site 05EF4   ; OUTI
site 05EF7   ; OUTI
site 05EFF   ; OUTI
site 05F02   ; OUTI
site 05F05   ; OUTI
site 05F08   ; OUTI
site 05F10   ; OUTI
site 05F13   ; OUTI
site 05F16   ; OUTI
site 05F19   ; OUTI
site 05F24   ; OUTI
site 05F27   ; OUTI
site 05FF9   ; OUT ($BF),A
site 05FFE   ; OUT ($BF),A
site 06005   ; OUT ($BE),A
site 0600A   ; OUTI
site 0600E   ; OUTI
site 06012   ; OUTI
site 0641E   ; OUT ($BE),A
site 0642C   ; OUT ($BE),A
site 067DE   ; OUT ($BE),A
site 067F1   ; OUT ($BF),A
site 067F4   ; OUT ($BF),A
site 0683C   ; OUT ($BE),A
site 06844   ; OUT ($BF),A
site 06847   ; OUT ($BF),A
otir 07C16   ; OUTI
site 07C23   ; OUT ($BF),A
site 07C27   ; OUT ($BF),A
site 09B6A   ; OUT ($BE),A
site 09B6E   ; OUT ($BE),A
site 09B7B   ; OUT ($BE),A
site 09B86   ; OUT ($BE),A
site 09B8C   ; OUT ($BE),A
site 09B98   ; OUT ($BE),A
site 09B9E   ; OUT ($BE),A
site 09BA4   ; OUT ($BE),A
site 09BAA   ; OUT ($BE),A
site 09BB0   ; OUT ($BE),A
site 09BB6   ; OUT ($BE),A
site 09BBC   ; OUT ($BE),A
site 09BC2   ; OUT ($BE),A
site 09BC6   ; OUT ($BE),A
site 09BCA   ; OUT ($BE),A
site 09D86   ; IN A,($BF)
site 09D88   ; IN A,($BF)
site 09D94   ; IN A,($BF)
site 0A5E4   ; OUT ($BF),A
site 0A5E9   ; OUT ($BF),A
site 0A5EE   ; OUTI
site 104EF   ; OUT ($BF),A
site 104FE   ; OUT ($BF),A
site 10513   ; OUTI
site 1052C   ; OUT ($BF),A
site 1053B   ; OUT ($BF),A
site 10550   ; OUTI
site 13B4E   ; OUT ($BF),A
site 13B52   ; OUT ($BF),A
site 13B58   ; OUT ($BF),A
site 13B5C   ; OUT ($BF),A
site 13B62   ; OUT ($BF),A
site 13B66   ; OUT ($BF),A
site 13C2C   ; OUT ($BF),A
site 13C30   ; OUT ($BF),A
site 13C61   ; OUT ($BE),A
site 13C67   ; OUT ($BE),A
site 13E18   ; OUT ($BF),A
site 13E24   ; OUT ($BF),A
site 13E43   ; OUT ($BE),A
site 13E46   ; OUTI
site 13E48   ; OUTI
site 13E4C   ; OUT ($BE),A
site 14FA4   ; IN A,($BE)
site 14FAB   ; IN A,($BE)
site 14FB7   ; OUT ($BE),A
site 14FBD   ; OUT ($BE),A
site 14FD5   ; INI
site 1506C   ; OUTI
site 1512F   ; OUT ($BF),A
site 15133   ; OUT ($BF),A
site 151D9   ; OUT ($BF),A
site 151DD   ; OUT ($BF),A
site 1527C   ; OUT ($BF),A
site 15281   ; OUT ($BF),A
site 15298   ; OUTI
site 1529F   ; OUTI
site 15303   ; OUT ($BE),A
site 1530F   ; OUT ($BE),A
site 15394   ; OUT ($BF),A
site 15399   ; OUT ($BF),A
site 153BB   ; OUT ($BE),A
site 153C2   ; OUT ($BE),A
site 153D2   ; OUT ($BF),A
site 153D7   ; OUT ($BF),A
site 153DE   ; OUT ($BE),A
site 153E5   ; OUT ($BE),A
site 15414   ; IN A,($BE)
site 1542F   ; OUT ($BE),A
site 1543A   ; OUT ($BE),A
site 15442   ; OUT ($BE),A
site 15475   ; OUT ($BE),A
site 1547C   ; OUT ($BE),A
site 1548D   ; OUT ($BE),A
site 15494   ; OUT ($BE),A
site 34457   ; OUT ($BF),A
site 3445B   ; OUT ($BF),A
site 7E7FA   ; OUT ($7F),A
site 7E7FE   ; OUT ($7F),A
site 7E802   ; OUT ($7F),A
site 7E805   ; OUT ($7F),A
site 7E809   ; OUT ($7F),A
site 7E80C   ; OUT ($7F),A
site 7E810   ; OUT ($7F),A
site 7E814   ; OUT ($7F),A
site 7E818   ; OUT ($7F),A
site 7E81C   ; OUT ($7F),A
site 7E837   ; OUT ($7F),A
site 7E83B   ; OUT ($7F),A
site 7E841   ; OUT ($7F),A
site 7E84A   ; OUT ($7F),A
site 7E880   ; OUT ($7F),A
site 7E88A   ; OUT ($7F),A
site 7E897   ; OUT ($7F),A
site 7E8A1   ; OUT ($7F),A
site 7E8D2   ; OUT ($7F),A
site 7E8E9   ; OUT ($7F),A
site 7E8FD   ; OUT ($7F),A
site 7E90C   ; OUT ($7F),A
site 7E923   ; OUT ($7F),A
site 7E937   ; OUT ($7F),A
site 7E964   ; OUT ($7F),A
site 7E977   ; OUT ($7F),A
site 7E98E   ; OUT ($7F),A
site 7E994   ; OUT ($7F),A
site 7E9B8   ; OUT ($7F),A
site 7E9CF   ; OUT ($7F),A
site 7E9E3   ; OUT ($7F),A
site 7EA40   ; OUT ($7F),A
site 7EC41   ; OUT ($7F),A
site 7EC46   ; OUT ($7F),A
site 7EC5A   ; OUT ($7F),A
site 7EC6D   ; OUT ($7F),A
site 7EC79   ; OUT ($7F),A
site 7EC8C   ; OUT ($7F),A
mapst 00006   ; LD ($FFFC),A
mapst 0000B   ; LD ($FFFD),A
mapst 00010   ; LD ($FFFE),A
mapst 00015   ; LD ($FFFF),A
mapst 019E0   ; LD ($FFFE),A
mapst 01A18   ; LD ($FFFF),A
mapst 01A67   ; LD ($FFFE),A
mapst 01AA5   ; LD ($FFFF),A
mapst 01AB5   ; LD ($FFFF),A
mapst 01ADD   ; LD ($FFFF),A
mapst 01B19   ; LD ($FFFF),A
mapst 01B34   ; LD ($FFFF),A
mapst 01B4B   ; LD ($FFFF),A
mapst 01BB6   ; LD ($FFFF),A
mapst 01BFF   ; LD ($FFFF),A
mapst 01C13   ; LD ($FFFF),A
mapst 01D55   ; LD ($FFFF),A
mapst 01D92   ; LD ($FFFF),A
mapst 01DB2   ; LD ($FFFE),A
mapst 01EE9   ; LD ($FFFE),A
mapst 01F74   ; LD ($FFFF),A
mapst 01F7F   ; LD ($FFFF),A
mapst 01FB8   ; LD ($FFFF),A
mapst 0218C   ; LD ($FFFE),A
mapst 02232   ; LD ($FFFE),A
mapst 023EA   ; LD ($FFFF),A
mapst 024C0   ; LD ($FFFE),A
mapst 02736   ; LD ($FFFE),A
mapst 02E7F   ; LD ($FFFE),A
mapst 03044   ; LD ($FFFE),A
mapst 03748   ; LD ($FFFF),A
maphl 03C25   # LD (HL),$04, HL = $FFFF
mapst 03C53   ; LD ($FFFF),A
mapst 03CEB   ; LD ($FFFF),A
mapst 03CF1   ; LD ($FFFF),A
mapst 03E21   ; LD ($FFFF),A
mapst 042F8   ; LD ($FFFF),A
mapst 04358   ; LD ($FFFF),A
mapst 04395   ; LD ($FFFF),A
mapst 043A7   ; LD ($FFFF),A
mapst 043DF   ; LD ($FFFF),A
mapst 04503   ; LD ($FFFF),A
mapst 04F66   ; LD ($FFFF),A
mapst 0502E   ; LD ($FFFF),A
mapst 050FD   ; LD ($FFFF),A
mapst 0511A   ; LD ($FFFF),A
mapst 0512B   ; LD ($FFFF),A
mapst 05230   ; LD ($FFFF),A
mapst 05283   ; LD ($FFFF),A
mapst 052E5   ; LD ($FFFF),A
mapst 0562C   ; LD ($FFFF),A
mapst 05638   ; LD ($FFFF),A
mapst 057CC   ; LD ($FFFF),A
mapst 057F8   ; LD ($FFFF),A
mapst 0597A   ; LD ($FFFF),A
mapst 059A1   ; LD ($FFFF),A
mapst 05A8E   ; LD ($FFFF),A
mapst 05AAD   ; LD ($FFFF),A
mapst 05BA1   ; LD ($FFFF),A
mapst 05CDA   ; LD ($FFFF),A
mapst 05D09   ; LD ($FFFF),A
mapst 05F63   ; LD ($FFFF),A
mapst 05FF4   ; LD ($FFFF),A
mapst 06226   ; LD ($FFFF),A
mapst 0623C   ; LD ($FFFF),A
mapst 06315   ; LD ($FFFF),A
mapst 06335   ; LD ($FFFF),A
mapst 06360   ; LD ($FFFF),A
mapst 064B7   ; LD ($FFFF),A
mapst 064D6   ; LD ($FFFF),A
mapst 06519   ; LD ($FFFF),A
mapst 06526   ; LD ($FFFF),A
mapst 06AC0   ; LD ($FFFF),A
mapst 06D6D   ; LD ($FFFF),A
mapst 07776   ; LD ($FFFF),A
mapst 0779D   ; LD ($FFFF),A
mapst 07894   ; LD ($FFFF),A
mapst 078FF   ; LD ($FFFF),A
mapst 07907   ; LD ($FFFF),A
mapst 0790F   ; LD ($FFFF),A
mapst 07917   ; LD ($FFFF),A
maphl 07922   # LD (HL),$05, HL = $FFFF
mapst 07928   ; LD ($FFFF),A
mapst 07B34   ; LD ($FFFF),A
mapst 07BB9   ; LD ($FFFF),A
mapst 07D0E   ; LD ($FFFF),A
maphl 07E38   # LD (HL),$05, HL = $FFFF
mapst 07E3E   ; LD ($FFFF),A
maphl 07E47   # LD (HL),$05, HL = $FFFF
mapst 07E4D   ; LD ($FFFF),A
maphl 07E56   # LD (HL),$05, HL = $FFFF
mapst 07E5C   ; LD ($FFFF),A
mapst 07E6B   ; LD ($FFFF),A
mapst 3403C   ; LD ($FFFE),A
mapst 3404E   ; LD ($FFFE),A
# Seen in the reference log, but left on no path by the scan: the register writes of the screen
# set-up $7B4F-$7B7C (bank 1) and the name table writer $7CD3/$7CDA.
site 07B52   ; OUT ($BF),A
site 07B56   ; OUT ($BF),A
site 07B6C   ; OUT ($BF),A
site 07B70   ; OUT ($BF),A
site 07B76   ; OUT ($BF),A
site 07B7A   ; OUT ($BF),A
site 07CD3   ; OUT ($BE),A
site 07CDA   ; OUT ($BE),A
# Mapper stores seen in the reference log: LD HL,$FFFF : LD A,(HL) (or LD C,(HL)) : PUSH AF :
# LD (HL),n, and the plain forms at $52B0 and $7C36.
maphl 051F8   ; LD (HL),$02
mapld 052B0   ; LD HL,$FFFF : LD (HL),$04
maphl 061BC   ; LD (HL),$04
maphl 06230   ; LD (HL),$04
maphl 06AB6   ; LD (HL),$05
maphl 07887   ; LD (HL),$04
maphl 07E65   ; LD (HL),$0D
mapst 07C36   ; LD ($FFFF),A
# Code that the scan and the 600 s reference log did not reach, checked by hand (data/scan-verdicts.tsv
# holds the verdicts for the rest of the gaps):
# - the RST $30 vector ($0030: LD A,$09 : OUT ($C0),A : JP $0000);
# - the unrolled OUTI chain $0900-$09FF (RET at $0A00), entered at $09C0 by the tile uploader $6920
#   in bank 1, which $1F6A (bank 0) jumps to; $693C/$6941 set its VRAM address;
# - bank 1: the word writer $4FE6/$4FED, register 6 at $51A7/$51AB, the fill $5A28/$5A2F (after the
#   VRAM read at $5A1F), the OUTI pair $5DF0/$5DF5, the name table writer $6031/$6038, and the
#   bank switches at the end of the copy $58E7 and of the bank checksum $646A;
# - bank 5: register writes at $99FC-$9A0A, $9AE7/$9AEB, $A517/$A51B and the fill at $A560;
# - bank 13 (entered at $8004 from $7E67 with bank 13 in slot 2): register writes, OUTI loops and
#   the sprite table writes of a full-screen scene.
site 00032   ; OUT ($C0),A
site 00900   ; OUTI
site 00902   ; OUTI
site 00904   ; OUTI
site 00906   ; OUTI
site 00908   ; OUTI
site 0090A   ; OUTI
site 0090C   ; OUTI
site 0090E   ; OUTI
site 00910   ; OUTI
site 00912   ; OUTI
site 00914   ; OUTI
site 00916   ; OUTI
site 00918   ; OUTI
site 0091A   ; OUTI
site 0091C   ; OUTI
site 0091E   ; OUTI
site 00920   ; OUTI
site 00922   ; OUTI
site 00924   ; OUTI
site 00926   ; OUTI
site 00928   ; OUTI
site 0092A   ; OUTI
site 0092C   ; OUTI
site 0092E   ; OUTI
site 00930   ; OUTI
site 00932   ; OUTI
site 00934   ; OUTI
site 00936   ; OUTI
site 00938   ; OUTI
site 0093A   ; OUTI
site 0093C   ; OUTI
site 0093E   ; OUTI
site 00940   ; OUTI
site 00942   ; OUTI
site 00944   ; OUTI
site 00946   ; OUTI
site 00948   ; OUTI
site 0094A   ; OUTI
site 0094C   ; OUTI
site 0094E   ; OUTI
site 00950   ; OUTI
site 00952   ; OUTI
site 00954   ; OUTI
site 00956   ; OUTI
site 00958   ; OUTI
site 0095A   ; OUTI
site 0095C   ; OUTI
site 0095E   ; OUTI
site 00960   ; OUTI
site 00962   ; OUTI
site 00964   ; OUTI
site 00966   ; OUTI
site 00968   ; OUTI
site 0096A   ; OUTI
site 0096C   ; OUTI
site 0096E   ; OUTI
site 00970   ; OUTI
site 00972   ; OUTI
site 00974   ; OUTI
site 00976   ; OUTI
site 00978   ; OUTI
site 0097A   ; OUTI
site 0097C   ; OUTI
site 0097E   ; OUTI
site 00980   ; OUTI
site 00982   ; OUTI
site 00984   ; OUTI
site 00986   ; OUTI
site 00988   ; OUTI
site 0098A   ; OUTI
site 0098C   ; OUTI
site 0098E   ; OUTI
site 00990   ; OUTI
site 00992   ; OUTI
site 00994   ; OUTI
site 00996   ; OUTI
site 00998   ; OUTI
site 0099A   ; OUTI
site 0099C   ; OUTI
site 0099E   ; OUTI
site 009A0   ; OUTI
site 009A2   ; OUTI
site 009A4   ; OUTI
site 009A6   ; OUTI
site 009A8   ; OUTI
site 009AA   ; OUTI
site 009AC   ; OUTI
site 009AE   ; OUTI
site 009B0   ; OUTI
site 009B2   ; OUTI
site 009B4   ; OUTI
site 009B6   ; OUTI
site 009B8   ; OUTI
site 009BA   ; OUTI
site 009BC   ; OUTI
site 009BE   ; OUTI
site 009C0   ; OUTI
site 009C2   ; OUTI
site 009C4   ; OUTI
site 009C6   ; OUTI
site 009C8   ; OUTI
site 009CA   ; OUTI
site 009CC   ; OUTI
site 009CE   ; OUTI
site 009D0   ; OUTI
site 009D2   ; OUTI
site 009D4   ; OUTI
site 009D6   ; OUTI
site 009D8   ; OUTI
site 009DA   ; OUTI
site 009DC   ; OUTI
site 009DE   ; OUTI
site 009E0   ; OUTI
site 009E2   ; OUTI
site 009E4   ; OUTI
site 009E6   ; OUTI
site 009E8   ; OUTI
site 009EA   ; OUTI
site 009EC   ; OUTI
site 009EE   ; OUTI
site 009F0   ; OUTI
site 009F2   ; OUTI
site 009F4   ; OUTI
site 009F6   ; OUTI
site 009F8   ; OUTI
site 009FA   ; OUTI
site 009FC   ; OUTI
site 009FE   ; OUTI
site 04FE6   ; OUT ($BE),A
site 04FED   ; OUT ($BE),A
site 051A7   ; OUT ($BF),A
site 051AB   ; OUT ($BF),A
site 05A28   ; OUT ($BE),A
site 05A2F   ; OUT ($BE),A
site 05DF0   ; OUTI
site 05DF5   ; OUTI
site 06031   ; OUT ($BE),A
site 06038   ; OUT ($BE),A
site 0693C   ; OUT ($BF),A
site 06941   ; OUT ($BF),A
mapst 058F8   ; LD ($FFFF),A
mapst 0646E   ; LD ($FFFF),A
site 159FC   ; OUT ($BF),A
site 15A00   ; OUT ($BF),A
site 15A06   ; OUT ($BF),A
site 15A0A   ; OUT ($BF),A
site 15AE7   ; OUT ($BF),A
site 15AEB   ; OUT ($BF),A
site 16517   ; OUT ($BF),A
site 1651B   ; OUT ($BF),A
site 16560   ; OUT ($BE),A
site 341AF   ; OUT ($BF),A
site 341B3   ; OUT ($BF),A
site 341B9   ; OUT ($BF),A
site 341BD   ; OUT ($BF),A
site 34205   ; OUTI
site 34213   ; OUT ($BF),A
site 34217   ; OUT ($BF),A
site 3421D   ; OUT ($BF),A
site 34221   ; OUT ($BF),A
site 34339   ; OUT ($BE),A
site 3433F   ; OUT ($BE),A
site 3438F   ; OUTI
site 343B8   ; OUT ($BE),A
site 343C4   ; OUT ($BE),A
site 343DD   ; OUT ($BE),A
site 343E0   ; OUT ($BE),A
site 3466A   ; OUT ($BE),A
site 34673   ; OUT ($BE),A
site 3467C   ; OUT ($BE),A
site 34685   ; OUT ($BE),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00328   # LD ($FFFE),A; after LD A,$01; JP/CALL target from $05578 $15988 $15A53 $16613; 32 bytes of valid code before it
mapst 01833   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
mapst 0187B   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
mapst 03D1E   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 04FFD   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 051BA   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 05BF4   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 05CAF   # LD ($FFFF),A; after LD A,($C40C); 32 bytes of valid code before it
mapst 06176   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 0618A   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 06935   # LD ($FFFF),A; after LD A,($C3B0); 32 bytes of valid code before it
mapst 07B8D   # LD ($FFFF),A; after LD A,(HL); 32 bytes of valid code before it
mapst 07E7A   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it

# Mortal Kombat II (Europe, Brazil).cht and Mortal Kombat II (Europe) (Action Replay).cht,
# "Infinite Time": RAM $C436 is the ones digit of the round clock; held at 9, the clock never
# counts down once the tens digit is 0
poke "Infinite time"
ar 00C4-3609
endpoke

# Mortal Kombat II (Europe, Brazil).cht and Mortal Kombat II (Europe) (Action Replay).cht,
# "Infinite Health P1": RAM $C488 is player 1's energy, $47 when full
poke "Infinite health P1"
ar 00C4-8849
endpoke

# Mortal Kombat II (Europe, Brazil).cht, "P1 Invincibility": five patches in bank 1 that stop
# the hit damage to player 1
poke "Invincibility"
gg 00F-D59-91D
gg 00F-D69-193
gg 7BF-D79-80E
gg FEF-D89-5D0
gg 88F-D99-7F0
endpoke

# Mortal Kombat II (Europe, Brazil).cht and Mortal Kombat II (Europe) (Action Replay).cht,
# "Infinite Credits (Continues)": RAM $C40B is the credit count, 7 at the start; a match lost
# takes one
poke "Infinite credits"
ar 00C4-0B09
endpoke

# Mortal Kombat II (Europe, Brazil).cht and Mortal Kombat II (Europe) (Action Replay).cht,
# "No Health P2": RAM $C48A is player 2's energy, held at 0, so the opponent is beaten at once
poke "Opponent no health"
ar 00C4-8A00
endpoke

# Mortal Kombat II (Europe, Brazil).cht, "P2 Infinite Health": a patch in bank 1 that stops the
# hit damage to player 2
poke "P2 infinite health"
gg 00B-4D9-F79
endpoke

# Mortal Kombat II (Europe, Brazil).cht, "Player 2 Can't Win Fights No Matter How Many Rounds are
# Won": RAM $C412 is the rounds won by player 2, held at 0, so no match is ever lost
poke "Opponent cannot win"
ar 00C4-1200
endpoke

# Mortal Kombat II (Europe, Brazil).cht, "Player 1 Only has to win 1 Round to Advance": RAM
# $C410 is the rounds won by player 1, held at 2, so the first round won takes the match
poke "One round wins match"
ar 00C4-1002
endpoke
