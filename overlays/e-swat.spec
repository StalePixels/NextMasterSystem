# E-SWAT (USA, Europe, Brazil) (En), CRC32 C4BB1676, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input).
#
# Decisions:
# - $0010-$0026 is zero bytes that no path reaches and no RST names, so $10 is the io
#   vector. The game uses only RST $08.
# - Bank 4 $87DE reads the name table through the VDP ($87E9, $87EE, $87F5) to find the
#   ground for the enemies; the reference log ran it. It is reached through the object
#   state tables that the record at $C1A1 names ($8466, one record per level).
# - $0D18 (CALL $BCDA) and $0E45 (CALL $BD5E) call slot 2 with bank 2, the bank the game
#   keeps there ($82 at $0628, $0678, $0795, $07EB and $1C7A). $BD4C writes one VRAM byte
#   ($BD4E, $BD51, $BD5A).
# - Bank 0 VDP routines that no path or recording reaches, each a whole routine after a
#   RET, so their sites are patched: $082E (one data byte after CALL $070F), $0836 (the
#   rectangle queue that $07F2, entry $00D4 of the service table at $0080, fills) and
#   $0A74 (one cell).
# - $0B0A copies BC bytes from DE to VRAM at HL one byte at a time, setting the address
#   for each byte; the block list copier $079C and bank 1 $62C2 send up to about 100 bytes
#   a frame through it in play.
#   Through the runtime it took the play frames past 100%. Its first 5 bytes are a far
#   call to vcopy in page 0, which writes the block with jt_vwrite, then RET.
# - The video rate test at $049F times a CPU delay loop against the frame flag with
#   interrupts off; on the Next it always read 50 Hz. Page 0 (vrate) gives the Next's rate.
# - Step rate: a Master System takes more than one frame for many play steps, the Next
#   for none, so the game played about 1.5 times as fast (the clock, one tick every 80
#   steps). Page 0 times each step's logic in Next lines and holds the step for the frames
#   a Master System needs (below). $0018-$0023 (zero bytes) hold the cave around the frame
#   handler's CALL $0167.
# - hsplit: the line interrupt handler $1BF3 sets H scroll for the cloud bands of the
#   first level; without the switch the clouds broke at a band edge.
# - The byte scan rows in banks 3, 5, 6, 10, 12, 13, 14 and 15 and at $3974, $39B8 and
#   $3F56 are data (animation and pointer tables, graphics).
name E-SWAT
cart C4BB1676
hz any		; No-Intro regions USA, Europe, Brazil
hsplit
vector 10 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 0003A   ; IN A,($BF)
site 00048   ; IN A,($DC)
site 00201   ; OUT ($BF),A
site 00206   ; OUT ($BF),A
site 00216   ; OUT ($BF),A
site 0021B   ; OUT ($BF),A
site 0022E   ; OUT ($BF),A
site 00233   ; OUT ($BF),A
site 00239   ; OUTD
site 00244   ; OUT ($BF),A
site 00249   ; OUT ($BF),A
site 0024F   ; OUTI
site 00251   ; OUTD
site 00258   ; OUTI
site 0025A   ; OUTI
site 0025C   ; OUTI
site 0025E   ; OUTI
site 00260   ; OUTI
site 00262   ; OUTI
site 00264   ; OUTI
site 00266   ; OUTI
site 00268   ; OUTI
site 0026A   ; OUTI
site 0026C   ; OUTI
site 0026E   ; OUTI
site 00270   ; OUTI
site 00272   ; OUTI
site 00274   ; OUTI
site 00276   ; OUTI
site 00278   ; OUTI
site 0027A   ; OUTI
site 0027C   ; OUTI
site 0027E   ; OUTI
site 00280   ; OUTI
site 00282   ; OUTI
site 00284   ; OUTI
site 00286   ; OUTI
site 00288   ; OUTI
site 0028A   ; OUTI
site 0028C   ; OUTI
site 0028E   ; OUTI
site 00290   ; OUTI
site 00292   ; OUTI
site 00294   ; OUTI
site 00296   ; OUTI
site 00298   ; OUTI
site 0029A   ; OUTI
site 0029C   ; OUTI
site 0029E   ; OUTI
site 002A0   ; OUTI
site 002A2   ; OUTI
site 002A4   ; OUTI
site 002A6   ; OUTI
site 002A8   ; OUTI
site 002AA   ; OUTI
site 002AC   ; OUTI
site 002AE   ; OUTI
site 002B0   ; OUTI
site 002B2   ; OUTI
site 002B4   ; OUTI
site 002B6   ; OUTI
site 002B8   ; OUTI
site 002BA   ; OUTI
site 002BC   ; OUTI
site 002BE   ; OUTI
site 002C0   ; OUTI
site 002C2   ; OUTI
site 002C4   ; OUTI
site 002C6   ; OUTI
site 002C8   ; OUTI
site 002CA   ; OUTI
site 002CC   ; OUTI
site 002CE   ; OUTI
site 002D0   ; OUTI
site 002D2   ; OUTI
site 002D4   ; OUTI
site 002D6   ; OUTI
site 002E0   ; OUT ($BF),A
site 002E5   ; OUT ($BF),A
site 002FB   ; IN A,($DD)
site 0032F   ; IN A,($BF)
site 00356   ; OUT ($BF),A
site 0035A   ; OUT ($BF),A
site 0035F   ; OUT ($BF),A
site 00363   ; OUT ($BF),A
site 0036E   ; OUT ($BF),A
site 00373   ; OUT ($BF),A
site 0045F   ; IN A,($BF)
site 0046D   ; OUT ($BE),A
site 0048A   ; OUT ($3E),A
site 0048D   ; OUT ($F2),A
site 00495   ; OUT ($3E),A
site 00499   ; OUT ($3F),A
site 004A2   ; IN A,($BF)
site 004A4   ; IN A,($BF)
site 004B0   ; IN A,($BF)
site 00709   ; OUT ($BF),A
site 0070C   ; OUT ($BF),A
site 00710   ; OUT ($BF),A
site 00715   ; OUT ($BF),A
site 0071D   ; OUT ($BE),A
site 00722   ; OUT ($BE),A
site 00833   ; OUT ($BE),A
site 00861   ; OUT ($BF),A
site 00866   ; OUT ($BF),A
site 00869   ; OUT ($BE),A
site 0086F   ; OUT ($BE),A
site 0087C   ; OUT ($BF),A
site 00881   ; OUT ($BF),A
site 008B8   ; OUT ($BF),A
site 008BF   ; OUT ($BF),A
site 008C3   ; IN A,($BE)
site 008CA   ; IN A,($BE)
site 00A76   ; OUT ($BF),A
site 00A7B   ; OUT ($BF),A
site 00A7E   ; OUT ($BE),A
site 00A82   ; OUT ($BE),A
site 00AE6   ; OUT ($BF),A
site 00AEB   ; OUT ($BF),A
site 00AF0   ; OUT ($BE),A
site 00AF8   ; OUT ($BE),A
site 00C9F   ; OUT ($3F),A
site 01C10   ; OUT ($BF),A
site 01C14   ; OUT ($BF),A
site 01C22   ; OUT ($BF),A
site 01C26   ; OUT ($BF),A
site 01C5D   ; OUT ($BF),A
site 01C61   ; OUT ($BF),A
site 06EA0   ; IN A,($DD)
site 0BD4E   ; OUT ($BF),A
site 0BD51   ; OUT ($BF),A
site 0BD5A   ; OUT ($BE),A
site 107E9   ; OUT ($BF),A
site 107EE   ; OUT ($BF),A
site 107F5   ; IN A,($BE)
site 1C107   ; OUT ($7F),A
site 1C123   ; OUT ($7F),A
site 1C154   ; OTIR
site 1C15D   ; OTIR
site 1C19C   ; OUT ($7F),A
site 1C1A0   ; OUT ($7F),A
site 1C1EF   ; OUT ($7F),A
site 1C1F3   ; OUT ($7F),A
site 1C21B   ; OUT ($7F),A
site 1C21F   ; OUT ($7F),A
site 1C222   ; OUT ($7F),A
site 1C428   ; OUT ($7F),A
site 1C4C0   ; OUT ($7F),A
site 1C4E7   ; OUT ($7F),A
site 1C4EC   ; OUT ($7F),A
site 1C4FF   ; OUT ($7F),A
site 1C593   ; OUTI
site 1C595   ; OUTI
site 1C597   ; OUTI
site 1C599   ; OUTI
site 1C59B   ; OUTI
site 1C59D   ; OUTI
site 1C59F   ; OUTI
site 1C5A1   ; OUTI
site 1C5A3   ; OUTI
site 1C5A5   ; OUTI
site 1C5A7   ; OUTI
site 1C5DD   ; OUT ($7F),A
site 1C633   ; OUT ($7F),A
site 1C672   ; OUT ($7F),A
site 1C6D4   ; OUT ($7F),A
site 1C6F4   ; OUT ($7F),A
site 1C740   ; OUT ($7F),A
site 1C74A   ; OUT ($7F),A
site 1C792   ; OUT ($7F),A
otir 002F0   ; OUTI
otir 00468   ; OUTI
mapst 00347   ; LD ($FFFF),A
mapst 00393   ; LD ($FFFF),A
mapst 0039A   ; LD ($FFFF),A
mapst 003B4   ; LD ($FFFF),A
mapst 003BB   ; LD ($FFFF),A
mapldk 003DB   # LD HL,$FFFC; LD (HL),$00
maphl 003E1   # LD (HL),$00, HL = $FFFD
maphl 003E4   # LD (HL),$01, HL = $FFFE
maphl 003E7   # LD (HL),$02, HL = $FFFF
mapst 00482   ; LD ($FFFF),A
mapst 00621   ; LD ($FFFF),A
mapst 00628   ; LD ($FFFF),A
mapst 00649   ; LD ($FFFF),A
mapst 00650   ; LD ($FFFF),A
mapst 00671   ; LD ($FFFF),A
mapst 00678   ; LD ($FFFF),A
mapst 0078E   ; LD ($FFFF),A
mapst 00795   ; LD ($FFFF),A
mapst 007E4   ; LD ($FFFF),A
mapst 007EB   ; LD ($FFFF),A
mapst 00F6B   ; LD ($FFFF),A
mapst 00F72   ; LD ($FFFF),A
mapst 00F81   ; LD ($FFFF),A
mapst 00F88   ; LD ($FFFF),A
mapst 00F97   ; LD ($FFFF),A
mapst 00F9E   ; LD ($FFFF),A
mapst 00FAD   ; LD ($FFFF),A
mapst 00FB4   ; LD ($FFFF),A
mapst 00FC2   ; LD ($FFFF),A
mapst 00FC9   ; LD ($FFFF),A
mapst 00FD7   ; LD ($FFFF),A
mapst 00FDE   ; LD ($FFFF),A
mapst 00FEC   ; LD ($FFFF),A
mapst 00FF3   ; LD ($FFFF),A
mapst 01001   ; LD ($FFFF),A
mapst 01008   ; LD ($FFFF),A
mapst 01016   ; LD ($FFFF),A
mapst 0101D   ; LD ($FFFF),A
mapst 0102B   ; LD ($FFFF),A
mapst 01032   ; LD ($FFFF),A
mapst 0106E   ; LD ($FFFF),A
mapst 01075   ; LD ($FFFF),A
mapst 01081   ; LD ($FFFF),A
mapst 01088   ; LD ($FFFF),A
mapst 01094   ; LD ($FFFF),A
mapst 0109B   ; LD ($FFFF),A
mapst 010A6   ; LD ($FFFF),A
mapst 010AD   ; LD ($FFFF),A
mapst 010B8   ; LD ($FFFF),A
mapst 010BF   ; LD ($FFFF),A
mapst 010CA   ; LD ($FFFF),A
mapst 010D1   ; LD ($FFFF),A
mapst 010DC   ; LD ($FFFF),A
mapst 010E3   ; LD ($FFFF),A
mapst 010EE   ; LD ($FFFF),A
mapst 010F5   ; LD ($FFFF),A
mapst 01100   ; LD ($FFFF),A
mapst 01107   ; LD ($FFFF),A
mapst 01112   ; LD ($FFFF),A
mapst 01119   ; LD ($FFFF),A
mapst 01481   ; LD ($FFFF),A
mapst 0148C   ; LD ($FFFF),A
mapst 01493   ; LD ($FFFF),A
mapst 0149F   ; LD ($FFFF),A
mapst 014A6   ; LD ($FFFF),A
mapst 014B0   ; LD ($FFFF),A
mapst 014BE   ; LD ($FFFF),A
mapst 014C5   ; LD ($FFFF),A
mapst 0198C   ; LD ($FFFF),A
mapst 01994   ; LD ($FFFF),A
mapst 0199B   ; LD ($FFFF),A
mapst 01C6B   ; LD ($FFFF),A
mapst 01C73   ; LD ($FFFF),A
mapst 01C7A   ; LD ($FFFF),A
mapst 06278   ; LD ($FFFF),A
mapst 0628C   ; LD ($FFFF),A
mapst 062A4   ; LD ($FFFF),A
mapst 062DC   ; LD ($FFFF),A
mapst 062F2   ; LD ($FFFF),A
mapst 06307   ; LD ($FFFF),A
mapst 0630F   ; LD ($FFFF),A
label cave_irq 00018
asm 00018 12   ; unused zero bytes: CALL $0167 between the marks of the step timing
    rst $10
    db far_io, pg_esw_in, ent_esw_in
    call $0167
    rst $10
    db far_io, pg_esw_out, ent_esw_out
    ret
endasm
asm 00041 3    ; CALL $0167: the frame handler's work, through the cave
    call cave_irq
endasm
asm 003C7 4    ; LD A,($C013); OR A: the step's logic ends
    rst $10
    db far_io, pg_esw_end, ent_esw_end
endasm
asm 003D3 5    ; XOR A; LD ($C001),A; RET: the step ends, held at the Master System's rate
    rst $10
    db far_io, pg_esw_hold, ent_esw_hold
    ret
endasm
asm 00D31 4    ; EI; CALL $00A8: the logic of a step other than play ends
    rst $10
    db far_io, pg_esw_stop, ent_esw_stop
endasm
asm 004AA 6    ; DEC BC; LD A,C; OR B; JP NZ,$04AA: the video rate test's delay loop
    rst $10
    db far_io, pg_vrate, ent_vrate
    nop
    nop
endasm
asm 004B2 7    ; AND A; LD A,1; JP M,$04B9; DEC A: the rate from vrate, BC = 0 as after the loop
    ld a,b
    ld bc,0
    jp $04B9
endasm
asm 00B0A 5          ; DI : LD A,L : OUT ($BF),A : LD A,H -> far call to vcopy, RET
    rst $10
    db far_io, pg_vcopy, ent_vcopy
    ret
endasm
page 0 vcopy vrate esw_in esw_out esw_end esw_stop esw_hold
; vcopy: HL = the VRAM address, DE = the source, BC = the count (1 to 65535). Writes the
; block to VRAM as the byte loop $0B0A-$0B26 does, and returns as it does: HL and DE past
; the block, BC = 0, A = 0 with Z set, interrupts on. A count of 0 writes nothing (the
; game's loop would write 64K). Runs with interrupts off on a stack of its own; uses
; jt_vwrite.
vcopy:  ld (.sp),sp
        ld sp,stk
        di
        push ix
        push iy
        push hl
        add hl,bc
        ld (.vend),hl           ; the VRAM address after the block
        ex de,hl                ; HL = the source
        push hl
        add hl,bc
        ld (.send),hl           ; the source after the block
        pop hl
        pop de                  ; DE = the VRAM address
        ld a,b
        or a
        jr z,.part
        push bc
        push hl
        push de
        ld c,b                  ; B runs of 256 bytes
        ld b,0
        ld ix,256
        ld iy,256
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop de
        pop hl
        pop bc
        ld a,h                  ; source and VRAM address B * 256 on
        add a,b
        ld h,a
        ld a,d
        add a,b
        ld d,a
.part:  ld a,c
        or a
        jr z,.done
        ld b,c                  ; one run of the bytes left
        ld c,1
        ld ix,256
        ld iy,256
        xor a
        call jt_vwrite
.done:  ld hl,(.vend)
        ld de,(.send)
        ld bc,0
        pop iy
        pop ix
        ld sp,(.sp)
        xor a
        ei
        ret
.sp:    dw 0
.vend:  dw 0
.send:  dw 0
        ds 32
stk:
; vrate: at $04AA, the video rate test at $049F. The test waits for the frame flag, runs
; the delay loop $04AA (2710 passes of 24 T-states, 65040 T-states: longer than an NTSC
; frame, shorter than a PAL one) and reads the flag again: set means 60 Hz, and $04B9
; stores 1 in $C0DD, else 0 (the game then runs its 50 Hz speed-up). The test runs with
; interrupts off, and the runtime raises the frame flag again only from its frame event,
; so on the Next it always reads 50 Hz. The entry gives the answer instead: B = 1 when
; the Next runs at 60 Hz (NextReg $05 bit 2), else 0. Keeps every other register but A
; and F. The status read at $04B0 stays, and the patch at $04B2 stores B.
vrate:  push af
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld b,0
        bit 2,a
        jr z,1f
        inc b
1:      pop af
        ret
; Step rate. Each game step ends at $03C7, which waits until $C001 (frame interrupts since
; the step started) reaches B, and $03D3 clears $C001 for the next step. A Master System
; cannot finish a play step in one frame as often as the Next does: in the first round's
; attract demo the clock ($3628, one tick every 80 steps) falls one unit in about 117
; frames on the reference (sg1000m3) and in 80 on the Next. esw_in and esw_out mark the
; frame handler's work (the cave at $0018 around CALL $0167), and lcnt counts the Next
; lines of the step's own logic without it, from $03D3 to the first of $0D31 (the frame
; wait of the states other than play) and $03C7. esw_hold, at $03D3, turns the lines into
; the frames a Master System needs for the step, one more for each CAP lines, and waits
; with interrupts on until the game's frame counter $C01F has passed that many frame
; events since the step started. Uses no runtime internals: NextRegs $05, $1E and $1F
; through $243B/$253B.
CAP60   equ 98              ; logic lines a NTSC Master System frame holds
CAP50   equ 98*311/264      ; a PAL one
; rd_line: HL = the Next's current line. Uses A, BC.
rd_line:
        ld bc,$243B
        ld a,$1E
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
        cp h
        jr nz,rd_line
        ld a,h
        and 1
        ld h,a
        ret
; acc: lcnt += (the current line - last) modulo the frame's lines. Uses A, BC, DE, HL.
acc:
        call rd_line
        ld de,(last)
        or a
        sbc hl,de
        jr nc,1f
        ld de,(lpf)
        add hl,de
1:      ld de,(lcnt)
        add hl,de
        ld (lcnt),hl
        ret
; esw_in: the frame handler starts, interrupts off. Keeps every register.
esw_in:
        push af
        ld a,(active)
        or a
        jr z,2f
        ld (sv_sp),sp
        ld sp,stk_top
        push bc
        push de
        push hl
        call acc
        pop hl
        pop de
        pop bc
        ld sp,(sv_sp)
2:      pop af
        ret
; esw_out: the frame handler's work ends, interrupts off. Keeps every register.
esw_out:
        push af
        ld a,(active)
        or a
        jr z,2f
        ld (sv_sp),sp
        ld sp,stk_top
        push bc
        push de
        push hl
        call rd_line
        ld (last),hl
        pop hl
        pop de
        pop bc
        ld sp,(sv_sp)
2:      pop af
        ret
; stop: the step's logic ends: lcnt is final. Interrupts off. Uses A, BC, DE, HL.
stop:   ld a,(active)
        or a
        ret z
        call acc
        xor a
        ld (active),a
        inc a
        ld (done),a
        ret
; esw_end: at $03C7. Returns A = ($C013) with the flags of OR A, as the game's code.
esw_end:
        ld a,(active)
        or a
        jr z,2f
        ld a,i                  ; P/V = the interrupt state
        di
        ld (sv_sp),sp
        ld sp,stk_top
        push af
        push bc
        push de
        push hl
        call stop
        pop hl
        pop de
        pop bc
        pop af
        ld sp,(sv_sp)
        jp po,2f
        ei
2:      ld a,($C013)
        or a
        ret
; esw_stop: at $0D31, in place of EI; CALL $00A8.
esw_stop:
        di
        ld (sv_sp),sp
        ld sp,stk_top
        push bc
        push de
        push hl
        call stop
        pop hl
        pop de
        pop bc
        ld sp,(sv_sp)
        ei
        jp $00A8                ; the game's frame wait returns past the patch
; esw_hold: at $03D3. Returns as XOR A; LD ($C001),A: A = 0, Z set, carry clear.
esw_hold:
        ld a,i                  ; P/V = the interrupt state
        di
        ld (sv_sp),sp
        ld sp,stk_top
        push af
        push bc
        push de
        push hl
        jp po,.start            ; interrupts off: no wait
        ld a,(done)
        or a
        jr z,.start
        xor a
        ld (done),a
        ld hl,(lcnt)
        ld de,(cap)
        ld b,1                  ; B = the Master System's frames for the step
1:      or a
        sbc hl,de
        jr c,2f
        inc b
        ld a,b
        cp 8
        jr c,1b
2:      ld a,b
        ld (need),a
        ld sp,(sv_sp)           ; wait on the game's stack, interrupts on
        ei
3:      ld a,($C01F)
        ld hl,s0
        sub (hl)
        ld hl,need
        cp (hl)
        jr c,3b
        di
        ld hl,stk_top-8         ; AF, BC, DE, HL are still below stk_top
        ld sp,hl
.start: ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld hl,311
        ld de,CAP50
        bit 2,a
        jr z,4f
        ld hl,264
        ld de,CAP60
4:      ld (lpf),hl
        ld (cap),de
        call rd_line
        ld (last),hl
        ld hl,0
        ld (lcnt),hl
        ld a,($C01F)
        ld (s0),a
        ld a,1
        ld (active),a
        pop hl
        pop de
        pop bc
        pop af
        ld sp,(sv_sp)
        ld a,0
        ld ($C001),a
        jp po,5f
        xor a
        ei
        ret
5:      xor a
        ret
active: db 0
done:   db 0
need:   db 0
s0:     db 0
last:   dw 0
lcnt:   dw 0
lpf:    dw 264
cap:    dw CAP60
sv_sp:  dw 0
        ds 48
stk_top:
endpage

# E-SWAT (USA, Europe, Brazil).cht and (Rev 1).cht, "Infinite Lives": RAM $C0C1 is the number
# of continues left, 4 at the start; each Continue lowers it, and with none left the game
# ends. Held at 4 the Continue prompt comes back after every game over
poke "Infinite continues"
ar 00C0-C104
endpoke

# E-SWAT (USA, Europe, Brazil).cht, "Infinite Health": RAM $C064 is the health bar, 4 when full
poke "Infinite health"
ar 00C0-6404
endpoke

# E-SWAT (USA, Europe, Brazil).cht, "Invulnerability": RAM $C080 is the timer that makes the
# player immune after a hit; held at $39 no enemy hit takes health
poke "Invincible"
ar 00C0-8039
endpoke

# E-SWAT (USA, Europe, Brazil).cht, "Infinite Time - Ten's Digit" and "Infinite Time - One's
# Digit": RAM $C0CA and $C0CB are the two BCD digits of the clock, held at 99
poke "Infinite time"
ar 00C0-CA09
ar 00C0-CB09
endpoke

# E-SWAT (USA, Europe, Brazil).cht, "Infinite Ammo - Hundred's Digit", "- Ten's Digit" and
# "- One's Digit": RAM $C0D5, $C0D6 and $C0D7 are the three BCD digits of the gun's ammo,
# held at 999
poke "Infinite ammo"
ar 00C0-D509
ar 00C0-D609
ar 00C0-D709
endpoke

# E-SWAT (USA, Europe) (Action Replay).cht, "Level Select": RAM $C056 is the round, 0 for
# round 1; the player sets it before the game starts
poke "Start round"
ar 00C0-56??
endpoke
