# Double Dragon (World), CRC32 A55D89F3, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, checked against reference I/O logs
# (600 s of random input, 180 s of the attract mode).
# Scan entries: the object state tables read by LD HL,table; LD A,(IX+$1F); RST $20;
# JP (HL) (tables at $1D5B, $2A19, $2AAA, $373F, $3CE5, $404A, $43E1, $4616, $49BC,
# $4C4F, $69AB, $6B15, $6C3E, $6D4B, $6E95, $727E, $7482), the object handlers stored
# into (IX+$02) and (IX+$03), and $0706, $09FA, $3ACC and bank 11 $8175. The scan runs
# with --no-harvest: the harvest takes $2001 from LD (IX+$06),$01; LD (IX+$07),$20,
# and $0190 from a count; both are data.
# Decisions:
# - No RST vector is free, so $0000-$0002 (DI; IM 1) is the io vector and the game
#   starts at $0003.
# - Every HALT the game runs is patched through a code cave in the $FF bytes at $7CBC
#   (bank 1, always in slot 1). The HALTs after LD ($C240),A give the interrupt one
#   frame to run each VRAM job (name table blocks, $140C); the ones after CALL $5BD4
#   give it one frame to take each text job at $C910 (the ending); the HALT; DJNZ
#   loops wait B frames.
# - The unreached byte patterns in banks 6, 7, 9, 10 and 13 are tile graphics; the
#   ones in bank 15 and at $3CF7 are word tables. The LD ($FFFF),A pattern at $26580
#   (bank 9) is graphics.
# - The frame handler's first call ($0970) copies the sprite table from $C700-$C7BF to
#   VRAM $3F00 with 192 single OUT ($BE),A writes, forwards and backwards on alternate
#   frames ($09A2/$09B1 and $09C9/$09D8). Through single traps that took the handler
#   past line 248, where the runtime takes the sprite table once a frame, so the Next
#   showed a half-written table (broken and missing sprites). Page 0 writes the same
#   bytes with jt_vwrite.
name Double Dragon
cart A55D89F3
hz any		; No-Intro region World
vector 00 io
start 0003
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00011   ; OUT ($BF),A
site 00014   ; OUT ($BF),A
site 00048   ; OUT ($BE),A
site 0005E   ; OUT (C),B
site 00070   ; OUT ($BE),A
site 000B3   ; OUT ($BE),A
site 000C0   ; OUT ($BE),A
site 0020E   ; IN A,($BF)
site 00231   ; IN A,($DD)
site 002BF   ; OTIR
site 002FB   ; OUT ($3E),A
site 00303   ; OUT ($F2),A
site 00306   ; IN A,($F2)
site 00318   ; OUT ($F2),A
site 00320   ; OUT ($3E),A
site 00328   ; OUT ($3F),A
site 0032A   ; IN A,($DD)
site 00334   ; OUT ($3F),A
site 00336   ; IN A,($DD)
site 0033F   ; OUT ($3F),A
site 00588   ; IN A,($BF)
site 005E9   ; IN A,($BF)
site 005FA   ; IN A,($BF)
site 00613   ; IN A,($BF)
site 00659   ; IN A,($BF)
site 00677   ; IN A,($BF)
site 006B9   ; IN A,($DC)
site 006C2   ; IN A,($DD)
otir 006DF   ; OUTI
site 0070E   ; OUT (C),A
site 008DE   ; IN A,($DC)
site 008E1   ; IN A,($DD)
site 008E7   ; IN A,($DC)
site 008EE   ; IN A,($DD)
site 009AB   ; OUT ($BE),A
site 009BD   ; OUT ($BE),A
site 009C3   ; OUT ($BE),A
site 009D3   ; OUT ($BE),A
site 009E5   ; OUT ($BE),A
site 009EB   ; OUT ($BE),A
site 00A04   ; OUT ($BE),A
site 00A1C   ; OUT (C),A
site 014C9   ; OUT ($BE),A
site 014D8   ; IN A,($BE)
site 014E1   ; OUT ($BE),A
site 014EC   ; IN A,($BE)
site 014F5   ; OUT ($BE),A
site 01501   ; OUT ($BE),A
site 01759   ; OUT ($BE),A
site 0175F   ; OUT ($BE),A
site 01780   ; OUT ($BE),A
site 01786   ; OUT ($BE),A
site 01816   ; OUT ($BE),A
site 0181C   ; OUT ($BE),A
site 01834   ; OUT ($BE),A
site 01839   ; OUT ($BE),A
site 018B3   ; OUT ($BE),A
site 01E87   ; IN A,($DC)
site 01E8E   ; IN A,($DD)
site 03AE8   ; OUT (C),L
site 03AEC   ; OUT (C),H
site 2C100   ; OUT ($F0),A
site 2C109   ; OUT ($F1),A
site 2C128   ; OUT ($7F),A
site 2C12C   ; OUT ($F0),A
site 2C132   ; OUT ($F1),A
site 2C149   ; OUT ($7F),A
site 2C159   ; OUT (C),D
site 2C15F   ; OUT ($F1),A
site 2C185   ; OUT ($7F),A
site 2C189   ; OUT ($7F),A
site 2C18E   ; OUT ($7F),A
site 2C1B3   ; OTIR
site 2C1C1   ; OTIR
site 2C1DD   ; OUT ($7F),A
site 2C1E1   ; OUT ($7F),A
site 2C1E7   ; OUT ($F0),A
site 2C1F5   ; OUT ($F1),A
site 2C1FA   ; OUT ($F0),A
site 2C200   ; OUT ($F1),A
site 2C20C   ; OUTI
site 2C212   ; OUTI
site 2C3E8   ; OUT ($7F),A
site 2C3EC   ; OUT ($7F),A
site 2C414   ; OUT ($7F),A
site 2C418   ; OUT ($7F),A
site 2C41C   ; OUT ($7F),A
site 2C420   ; OUT ($7F),A
site 2C423   ; OUT ($7F),A
site 2C489   ; OUT ($F0),A
site 2C490   ; OUT ($F1),A
site 2C498   ; OUT ($F0),A
site 2C49E   ; OUT ($F1),A
site 2C593   ; OUT ($F0),A
site 2C59D   ; OUT (C),L
site 2C5A6   ; OUT ($F0),A
site 2C5C1   ; OUT (C),H
site 2C5C9   ; OUT ($F0),A
site 2C5D7   ; OUT ($F1),A
site 2C5E3   ; OUT ($F0),A
site 2C5EC   ; OUT ($F1),A
site 2C7A1   ; OUT ($F0),A
site 2C7AA   ; OUT (C),A
site 2C7AF   ; OUT ($F0),A
site 2C7B5   ; OUTI
site 2C809   ; OUT ($7F),A
site 2C8E2   ; OUT ($7F),A
site 2C909   ; OUT ($7F),A
site 2C90E   ; OUT ($7F),A
site 2C93A   ; OUT ($F0),A
site 2C948   ; OUT ($F1),A
site 2C959   ; OUT ($F0),A
site 2C9ED   ; OUTI
site 2C9EF   ; OUTI
site 2C9F1   ; OUTI
site 2C9F3   ; OUTI
site 2C9F5   ; OUTI
site 2C9F7   ; OUTI
site 2C9F9   ; OUTI
site 2C9FB   ; OUTI
site 2C9FD   ; OUTI
site 2C9FF   ; OUTI
site 2CA01   ; OUTI
site 2CA0B   ; OUT (C),D
site 2CA14   ; OUT ($F1),A
site 2CA56   ; OUT ($7F),A
site 2CAAC   ; OUT ($7F),A
site 2CAEB   ; OUT ($7F),A
site 2CB4D   ; OUT ($7F),A
site 2CB6D   ; OUT ($7F),A
site 2CBAD   ; OUT ($7F),A
site 2CBB7   ; OUT ($7F),A
site 2CBFF   ; OUT ($7F),A
mapst 000A3   ; LD ($FFFF),A
mapst 0022E   ; LD ($FFFF),A
mapst 0055E   ; LD ($FFFF),A
mapst 005A1   ; LD ($FFFF),A
mapst 005C9   ; LD ($FFFF),A
mapst 00609   ; LD ($FFFF),A
mapst 00906   ; LD ($FFFF),A
mapst 00A7F   ; LD ($FFFF),A
mapst 00B2A   ; LD ($FFFF),A
mapst 00B52   ; LD ($FFFF),A
mapst 00BF0   ; LD ($FFFF),A
mapst 010A3   ; LD ($FFFF),A
mapst 010B0   ; LD ($FFFF),A
mapst 01175   ; LD ($FFFF),A
mapst 01396   ; LD ($FFFF),A
mapst 013DC   ; LD ($FFFF),A
mapst 01745   ; LD ($FFFF),A
mapst 017B3   ; LD ($FFFF),A
mapst 01ABD   ; LD ($FFFF),A
label cv_mbox 07CBC
label cv_waitb 07CC2
label cv_text 07CC7
label cv_reset 07CCD
asm 07CBC 6    ; unused $FF bytes: cave for LD ($C240),A; HALT
    ld ($C240),a
    rst $00
    db halt_io
    ret
endasm
asm 07CC2 5    ; unused $FF bytes: cave for HALT; DJNZ
    rst $00
    db halt_io
    djnz $-2
    ret
endasm
asm 07CC7 6    ; unused $FF bytes: cave for CALL $5BD4; HALT
    call $5BD4
    rst $00
    db halt_io
    ret
endasm
asm 07CCD 8    ; unused $FF bytes: cave for CALL $1090; HALT; JP $029C
    call $1090
    rst $00
    db halt_io
    jp $029C
endasm
asm 00919 4    ; CALL $1090; HALT, then JP $029C (restart)
    jp cv_reset
endasm
asm 01519 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 0151F 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 0152F 3    ; HALT; DJNZ: waits B frames
    call cv_waitb
endasm
asm 01534 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 0153A 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 0154A 3    ; HALT; DJNZ: waits B frames
    call cv_waitb
endasm
asm 01556 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 0155C 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 01562 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 01572 3    ; HALT; DJNZ: waits B frames
    call cv_waitb
endasm
asm 01577 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 0157D 4    ; LD ($C240),A; HALT: the interrupt runs VRAM job A
    call cv_mbox
endasm
asm 0158D 3    ; HALT; DJNZ: waits B frames
    call cv_waitb
endasm
asm 01E94 4    ; CALL $1090; HALT, then JP $029C (restart)
    jp cv_reset
endasm
asm 038C8 4    ; CALL $5BD4; HALT: the interrupt takes the text job at $C910
    call cv_text
endasm
asm 038E1 4    ; CALL $5BD4; HALT: the interrupt takes the text job at $C910
    call cv_text
endasm
asm 038E8 4    ; CALL $5BD4; HALT: the interrupt takes the text job at $C910
    call cv_text
endasm
asm 038EF 4    ; CALL $5BD4; HALT: the interrupt takes the text job at $C910
    call cv_text
endasm
asm 0390B 4    ; CALL $5BD4; HALT: the interrupt takes the text job at $C910
    call cv_text
endasm
asm 03912 4    ; CALL $5BD4; HALT: the interrupt takes the text job at $C910
    call cv_text
endasm
asm 03919 4    ; CALL $5BD4; HALT: the interrupt takes the text job at $C910
    call cv_text
endasm
asm 03920 4    ; CALL $5BD4; HALT: the interrupt takes the text job at $C910
    call cv_text
endasm

# The sprite table copy: far calls to page 0 in place of the two call pairs of $0970.
asm 00988 13   ; LD DE,$7F00; CALL $09A2; LD DE,$7F80; CALL $09B1; RET
    rst $00
    db far_io, pg_sat_fwd, ent_sat_fwd
    ret
endasm
asm 00995 13   ; LD DE,$7F00; CALL $09C9; LD DE,$7F80; CALL $09D8; RET
    rst $00
    db far_io, pg_sat_rev, ent_sat_rev
    ret
endasm
page 0 sat_fwd sat_rev
; sat_fwd: what $09A2 and $09B1 write: Y from $C700-$C73F to VRAM $3F00-$3F3F, then X from
; $C740-$C77F and N from $C780-$C7BF in turn to $3F80-$3FFF.
; sat_rev: what $09C9 and $09D8 write: the same tables read backwards, Y from $C73F down,
; X from $C77F down and N from $C7BF down.
; Both build the 192 bytes in buf in VRAM order and write them with one jt_vwrite call
; (one run of 64 for Y at $3F00, one of 128 for X and N at $3F80). They run in the frame
; handler with interrupts off, on a stack of their own. They keep IX and IY; A, F, BC,
; DE and HL change, as in the game's routines, and the callers load their registers
; again. The VDP is left as the game's last write leaves it.
sat_fwd:
    ld (sv_sp),sp
    ld sp,stk_top
    ld hl,$C700
    ld de,buf
    ld bc,64
    ldir                ; Y
    ld hl,$C740         ; X
    ld bc,$C780         ; N
.xn:
    ld a,(hl)
    ld (de),a
    inc de
    ld a,(bc)
    ld (de),a
    inc de
    inc hl
    inc bc
    ld a,l
    cp $80
    jr nz,.xn
    jr sat_write
sat_rev:
    ld (sv_sp),sp
    ld sp,stk_top
    ld hl,$C73F
    ld de,buf
    ld b,64
.y:
    ld a,(hl)
    ld (de),a
    inc de
    dec hl
    djnz .y
    ld hl,$C77F         ; X
    ld bc,$C7BF         ; N
.xn:
    ld a,(hl)
    ld (de),a
    inc de
    ld a,(bc)
    ld (de),a
    inc de
    dec hl
    dec bc
    ld a,l
    cp $3F
    jr nz,.xn
sat_write:
    push ix
    push iy
    ld hl,buf
    ld de,$3F00
    ld bc,$4002         ; 2 runs of 64: $3F00 and $3F80 from buf and buf+64...
    ld ix,64
    ld iy,128
    ld a,1              ; the source is the page
    call jt_vwrite
    ld hl,buf+128       ; ...and the last 64 bytes at $3FC0
    ld de,$3FC0
    ld bc,$4001
    ld a,1
    call jt_vwrite
    pop iy
    pop ix
    ld sp,(sv_sp)
    ret
sv_sp:
    dw 0
buf:
    ds 192
    ds 64
stk_top:
endpage

# Double Dragon (World).cht, "Infinite Lives P1": RAM $CB2B is player 1's lives, held at 9
poke "Infinite lives P1"
ar 00CB-2B09
endpoke

# Double Dragon (World).cht, "Infinite Lives P2": RAM $CB6B is player 2's lives, held at 9
poke "Infinite lives P2"
ar 00CB-6B09
endpoke

# Double Dragon (World).cht, "Infinite Health P1": RAM $CB2A is player 1's energy, held at $55
poke "Infinite energy P1"
ar 00CB-2A55
endpoke

# Double Dragon (World).cht, "Infinite Energy P2": RAM $CB6A is player 2's energy, held at $55
poke "Infinite energy P2"
ar 00CB-6A55
endpoke

# Double Dragon (World).cht, "Level Select": RAM $C110 is the mission, 0 to 3 for missions 1 to 4
poke "Start mission ??"
ar 00C1-10??
endpoke

# Double Dragon (World).cht, "1-Hit Kills Enemies": an enemy starts with no energy
# and dies at its first hit
poke "Enemies die in one hit"
gg 7EB-D7E-3B7
endpoke
