# Sega Chess (Europe, Brazil) (En), CRC32 A8061AEF, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with hand entry points and the 60 s reference
# I/O log, then decided by hand.
#
# Decisions:
# - Entry points given to the scan by hand (sitescan --entry): the engine's routines in bank 14,
#   which bank 0 calls with bank 14 in slot 2 ($1D5E, $28CC): $909B, $915F, $8149, $8334,
#   $8441, $8528, $8769, $9400, $87AD, $8750; and the code after each CALL $0742, which prints
#   the text that follows the call up to a $FE byte ($FF takes two operand bytes, $FC one).
# - The engine runs as a task of its own: $1D6F starts it on the stack at $CB00, $28AD switches
#   to the main task and $28DD back ($D5C8, $D5CA). The RET at $28CB, $2932 and $4E74 and the
#   RET at bank 14 $9C8C (LD SP,($C33D)) go back to code that is scanned. The JP (HL) at bank 14
#   $8F89 and the evaluation routines reached through IY ($9AEA, $9AF2) are not followed: bank 14
#   holds no I/O byte pattern rated above very low.
# - $0591, $0594, $059B, $059E, $0BDA, $0BDF, $0BE4 and bank 1 $4C36, $4C47, $4C73 write A to
#   $0000, as a delay between VDP accesses: a no-op on the Master System, a write to the cart's
#   copy on the Next. They become NOPs.
# - $05D9 counts a frame with a CPU loop to tell 50 Hz from 60 Hz ($C1B2 = 50 or 60). On the
#   Next the loop ends before the frame does, so the game takes 50 Hz, as hz 50 runs it.
# - Unused: the development monitor at $00AF-$02A8 (after the text SEGA DL1 *** PDS CONVERTER)
#   and the VRAM loader $08BF-$08D5. Not code: the byte patterns in banks 6 and 10 (tiles) and
#   13 and 15 (speech samples).
name Sega Chess
cart A8061AEF
hz 50		; No-Intro regions Europe, Brazil
# $0003-$0037 are $FF filler bytes; the game uses no RST.
vector 08 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 00421   ; OUT ($3F),A
site 0044C   ; IN A,($BF)
site 00463   ; IN A,($DD)
site 0049D   ; OTIR
site 004A5   ; IN A,($DD)
site 004AF   ; IN A,($DC)
site 004B9   ; IN A,($DD)
site 004BE   ; IN A,($DC)
site 004C8   ; IN A,($DD)
site 004CD   ; IN A,($DC)
site 004D7   ; IN A,($DC)
site 004DC   ; IN A,($DC)
site 004E6   ; IN A,($DC)
site 004EB   ; IN A,($DC)
site 004F5   ; IN A,($DD)
site 004FA   ; IN A,($DC)
site 00504   ; IN A,($DD)
site 0058F   ; OUT ($BF),A
site 00599   ; OUT ($BF),A
site 005A4   ; OUT ($BE),A
site 005AA   ; OUT ($BF),A
site 005B1   ; OUT ($BF),A
site 005B5   ; OUT ($BF),A
site 005BD   ; OUT ($BF),A
site 005C1   ; OUT ($BF),A
site 005C7   ; OUT ($BF),A
site 005DC   ; IN A,($BF)
site 005DE   ; IN A,($BF)
site 005EA   ; IN A,($BF)
site 00625   ; IN A,($BF)
site 00627   ; IN A,($BF)
site 0065B   ; OUT ($BE),A
site 00661   ; OUT ($BE),A
site 0070A   ; OUT ($BE),A
site 007C9   ; OUT ($BE),A
site 007DA   ; OUT ($BE),A
site 007E0   ; OUT ($BE),A
site 00813   ; OUTI
site 008E1   ; OUT ($BE),A
site 008F1   ; OUT ($BE),A
site 00AB1   ; OUTI
site 00ADA   ; OUTI
site 00BD8   ; OUTI
site 00BDD   ; OUTI
site 00BE2   ; OUTI
site 00BE7   ; OUTI
site 00C03   ; OUTI
site 00C08   ; OUTI
site 00C0D   ; OUTI
site 00C12   ; OUTI
site 00C32   ; INI
site 00C37   ; INI
site 00C3C   ; INI
site 00C41   ; INI
site 00C5D   ; INI
site 00C62   ; INI
site 00C67   ; INI
site 00C6C   ; INI
site 01248   ; OUT ($7F),A
site 0124B   ; OUT ($7F),A
site 0124F   ; OUT ($7F),A
site 01252   ; OUT ($7F),A
site 01256   ; OUT ($7F),A
site 01259   ; OUT ($7F),A
site 0125C   ; OUT ($7F),A
site 0126E   ; OUTI
site 01270   ; OUTI
site 01272   ; OUTI
site 01289   ; OUTI
site 0128B   ; OUTI
site 0128D   ; OUTI
site 0134C   ; OUT ($BE),A
site 03644   ; INI
site 03658   ; OUTI
site 04A79   ; OUT ($BE),A
site 04C39   ; IN A,($BE)
site 04C4A   ; OUT ($BE),A
site 04C76   ; IN A,($BE)
site 04EA3   ; OUTI
site 04F30   ; OUTI
site 050B3   ; OUTI
site 05189   ; OUTI
site 05542   ; OUTI
site 05640   ; OUT ($BF),A
site 05647   ; OUT ($BF),A
site 05658   ; OUTI
site 05684   ; OUT ($BF),A
site 0568B   ; OUT ($BF),A
site 05690   ; OUT (C),A
site 05695   ; OUT (C),A
site 24C90   ; OUT ($7F),A
site 24C94   ; OUT ($7F),A
site 24C98   ; OUT ($7F),A
site 24C9C   ; OUT ($7F),A
site 24CAC   ; OUT ($7F),A
site 24CC3   ; OUT ($7F),A
site 24CD0   ; OUT ($7F),A
site 24CDF   ; OUT ($7F),A
site 24CF6   ; OUT ($7F),A
site 24D03   ; OUT ($7F),A
site 24D1A   ; OUT ($7F),A
site 24D2D   ; OUT ($7F),A
site 24D44   ; OUT ($7F),A
site 24D4A   ; OUT ($7F),A
site 24D5F   ; OUT ($7F),A
site 24D76   ; OUT ($7F),A
site 24D83   ; OUT ($7F),A
site 24DD4   ; OUT ($7F),A
mapldk 00411   # LD HL,$FFFC; LD (HL),$00
maphl 00417   # LD (HL),$00, HL = $FFFD
maphl 0041A   # LD (HL),$01, HL = $FFFE
maphl 0041D   # LD (HL),$02, HL = $FFFF
mapst 0051D   ; LD ($FFFF),A
mapst 00524   ; LD ($FFFF),A
mapst 0054B   ; LD ($FFFF),A
mapst 00553   ; LD ($FFFF),A
mapst 00B1B   ; LD ($FFFF),A
mapst 00B24   ; LD ($FFFF),A
mapst 00B2E   ; LD ($FFFF),A
mapst 00B37   ; LD ($FFFF),A
mapst 00F95   ; LD ($FFFF),A
mapst 010D5   ; LD ($FFFF),A
mapst 01243   ; LD ($FFFF),A
mapst 01299   ; LD ($FFFF),A
mapst 01D64   ; LD ($FFFF),A
mapst 01D6B   ; LD ($FFFF),A
mapst 028D2   ; LD ($FFFF),A
mapst 028D9   ; LD ($FFFF),A
mapst 02EF2   ; LD ($FFFF),A
mapst 03B29   ; LD ($FFFF),A
mapst 03ED4   ; LD ($FFFF),A
mapst 04DF6   ; LD ($FFFF),A
mapst 04F42   ; LD ($FFFF),A
mapst 04F7B   ; LD ($FFFF),A
mapst 04FF7   ; LD ($FFFF),A
mapst 05182   ; LD ($FFFF),A
mapst 05192   ; LD ($FFFF),A
mapst 051C8   ; LD ($FFFF),A
mapst 051F9   ; LD ($FFFF),A
mapst 0525E   ; LD ($FFFF),A
mapst 05302   ; LD ($FFFF),A
mapst 053CB   ; LD ($FFFF),A
mapst 05427   ; LD ($FFFF),A
mapst 05451   ; LD ($FFFF),A
mapst 0545B   ; LD ($FFFF),A
mapst 05652   ; LD ($FFFF),A
mapst 0566D   ; LD ($FFFF),A
asm 00591 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 00594 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 0059B 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 0059E 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 00BDA 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 00BDF 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 00BE4 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 04C36 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 04C47 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
asm 04C73 3    ; LD ($0000),A: a write to ROM, a no-op on the Master System
    nop
    nop
    nop
endasm
mapst 00B05   # LD ($FFFF),A; JP/CALL target from $215F1; 32 bytes of valid code before it
mapst 03171   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
# The engine searches until its move time (the level table at bank 14 $90C4, checked at $287C) is
# up, so its strength is the number of positions it searches in that time. Bank 14 $9400 generates
# the moves of one position and yields to the main task there (CALL $28AD): one call a position.
# The Next runs that cycle (the engine's work, the main task's turn and the interrupts) faster
# than a Master System, so it searched more positions a move and played stronger. The call goes
# through the cave at $0010 (filler bytes after the io vector) to page 0 entry node, which holds
# each cycle to the Master System's time: it waits NUM/256 of the cycle's Next time more.
label cv_node 00010
asm 00010 7    ; filler bytes: the page entry node, then the engine's yield
    rst $08
    db far_io, pg_node, ent_node
    jp $28AD
endasm
asm 39400 3    ; CALL $28AD: the yield at each position the engine searches
    call cv_node
endasm
# Speech. The player at $1228 (phrases set DE at $11C9-$1218, from banks 13 and 15) writes each
# sample byte as two 4-bit steps: the channel 0 and 1 volumes and the noise volume, three OUTI each,
# timed by DJNZ waits. With interrupts off a byte takes 1025 T-states on a Master System (289 us
# at the PAL clock). Through the runtime, six OUTI traps and the waits took 10,964 Next cycles
# (392 us), so the speech played at 0.74 of its speed. Page 0 entry speech plays the loop
# $125E-$1297 with the runtime's PSG-to-AY volume conversion, timed with CTC channel 0. The site
# lines of the replaced OUTI stay, so that the scan's rows are covered.
asm 0125E 7    ; LD BC,$12A7; LD A,(DE); SRL A; ...: the sample loop
    rst $08
    db far_io, pg_speech, ent_speech
    jp $1298
endasm
page 0 node speech
; node: called before each yield at $9400. A cycle is the Next time from the end of the last
; call to this one, counted in video lines (311 a frame at 50 Hz) on a scale that starts at line
; 249, where the runtime's once-a-frame work counts fw_frames. A cycle longer than CAP lines, or
; one that the count cannot place (4 frames or more), is a gap (the search starts, or the engine
; was idle) and gets no wait. Otherwise the call waits NUM/256 of the cycle. Keeps BC, DE, HL; A and F change, as the
; yield's own return path changes them.
; Runs on its own stack with interrupts off, and waits on the game's stack with interrupts on and
; no stack use. With interrupts off at the call it does not wait.
        OPT --zxnext            ; MUL D,E
LPF     equ 311
CAP     equ 933
NUM     equ 432
node:   ld a,i                  ; P/V = IFF2; read twice, as an interrupt in LD A,I clears it
        jp pe,1F
        ld a,i
1:      di
        ld (n_sp),sp
        ld sp,n_stk
        push bc
        push de
        push hl
        ld a,0
        jp po,2F
        inc a
2:      ld (n_ien),a
        or a
        jp z,.stamp
        ld a,(n_ok)
        or a
        jp z,.stamp
        ld bc,(n_pf)
        ld de,(n_pl)
        call since              ; HL = the cycle in lines
        bit 7,h
        jp nz,.stamp            ; below 0: the frame work is not counted yet
        ld de,CAP+1
        or a
        sbc hl,de
        jp nc,.stamp            ; a gap
        add hl,de
        push hl                 ; HL = HL x NUM / 256 (NUM 256-511)
        ld d,h
        ld e,NUM & 255
        mul d,e
        ld a,l
        ld h,d
        ld l,e
        ld d,a
        ld e,NUM & 255
        mul d,e
        ld e,d
        ld d,0
        add hl,de
        pop de
        add hl,de
        push hl
        call stamp              ; the target: now + HL lines
        pop bc
        add hl,bc
        ld bc,LPF
3:      or a
        sbc hl,bc
        jr c,4F
        inc de
        jr 3B
4:      add hl,bc
        ld (n_tf),de
        ld (n_tl),hl
        ld sp,(n_sp)            ; the wait, on the game's stack
.wait:  ei
        nop
        di
        ld bc,$243B
5:      ld a,$1E
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
        dec b
        cp h
        jr nz,5B
        ld a,h
        and 1
        ld h,a
        ld de,249               ; HL = the line from 249
        or a
        sbc hl,de
        jr nc,6F
        ld de,LPF
        add hl,de
6:      ex de,hl
        ld hl,(fw_frames)
        ld bc,(n_tf)
        or a
        sbc hl,bc               ; frames past the target's frame
        jr z,7F
        jp p,.end               ; past it
        ld a,h                  ; more than 4 frames before it: the count is lost, stop
        cp $FF
        jr nz,.end
        ld a,l
        cp $FC
        jr c,.end
        jr .wait
7:      ld hl,(n_tl)
        scf
        sbc hl,de               ; target line - 1 - now
        jr nc,.wait
.end:   ld sp,n_stk-6
.stamp: call stamp
        ld (n_pf),de
        ld (n_pl),hl
        ld a,1
        ld (n_ok),a
        ld a,(n_ien)
        or a
        jr z,8F
        pop hl
        pop de
        pop bc
        ld sp,(n_sp)
        ei
        ret
8:      pop hl
        pop de
        pop bc
        ld sp,(n_sp)
        ret

; stamp: DE = fw_frames, HL = the beam's line counted from 249 (0-310). Interrupts off.
stamp:  ld bc,$243B
1:      ld a,$1E
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
        dec b
        cp h
        jr nz,1B
        ld a,h
        and 1
        ld h,a
        ld de,249
        or a
        sbc hl,de
        jr nc,2F
        ld de,LPF
        add hl,de
2:      ld de,(fw_frames)
        ret

; since: HL = lines from the stamp BC (frames), DE (line) to now, as a signed number; $7FFF when
; the frames differ by 4 or more.
since:  push de
        push bc
        call stamp
        pop bc
        ex de,hl                ; HL = frames now, DE = line now
        or a
        sbc hl,bc
        ld a,h
        or a
        jr nz,3F
        ld a,l
        cp 4
        jr nc,3F
        ex de,hl
        ld de,LPF
        or a
        jr z,2F
1:      add hl,de
        dec a
        jr nz,1B
2:      pop de
        or a
        sbc hl,de
        ret
3:      pop de
        ld hl,$7FFF
        ret

n_sp:   dw 0
n_ien:  db 0
n_ok:   db 0
n_pf:   dw 0
n_pl:   dw 0
n_tf:   dw 0
n_tl:   dw 0
        ds 32
n_stk:

; speech: the sample loop $125E-$1297 (interrupts off, from $1228). DE = the first sample byte, in
; slot 2. For each byte, the high then the low 4 bits k set PSG channels 0 and 1 to attenuation
; 15 - k, written as the runtime writes a PSG volume (psg_w2 in fw4.asm): AY 0 registers 8 and 9,
; with the value of ay_vol_table (tables.inc) for that attenuation. The loop's third OUTI, noise
; volume 15, is the value the noise volume already holds ($125C), and is not written. The writes
; keep the Master System's times: the low step 503 T-states after the high one, the next byte 522
; after that (PAL clock, 7.894 Next cycles a T-state), counted with CTC channel 0 (16 cycles a
; count). The bytes end at $1F, after the first. AY 0 is selected while the loop runs; the end
; selects AY 1 again, as the noise volume write at $125C left it for the runtime (ay_cur).
; Returns as the loop: DE at the $1F, HL = $12AA + 4 x the last low step, B = 0, C = $7F; A and F
; are taken from the stack at $1298. Runs on its own stack.
speech: ld (s_sp),sp
        ld sp,s_stk
        ld bc,$183B             ; CTC channel 0: timer, 16 cycles a count, from 256
        ld a,$07
        out (c),a
        xor a
        out (c),a
        in a,(c)
        ld (s_prev),a
        ld hl,0
        ld (s_owed),hl
        ld bc,$FFFD             ; AY 0
        ld a,$FF
        out (c),a
1:      ld a,(de)
        ld (s_last),a
        rrca
        rrca
        rrca
        rrca
        call vol
        ld hl,3971              ; 503 T-states
        call wait
        ld a,(de)
        call vol
        inc de
        ld hl,4121              ; 522 T-states
        call wait
        ld a,(de)
        cp $1F
        jr nz,1B
        ld bc,$FFFD             ; AY 1
        ld a,$FE
        out (c),a
        ld bc,$183B             ; stop the CTC channel
        ld a,$03
        out (c),a
        ld a,(s_last)
        and $0F
        add a,a
        add a,a
        add a,$AA
        ld l,a
        ld h,$12
        ld bc,$007F
        ld sp,(s_sp)
        ret

; vol: A low 4 bits = k: AY 0 registers 8 and 9 (channels A and B) = the volume of attenuation
; 15 - k. Changes A, BC, HL.
vol:    and $0F
        ld hl,s_ayv
        add hl,a
        ld a,(hl)
        ld bc,$FFFD
        ld l,8
        out (c),l
        ld b,$BF
        out (c),a
        ld b,$FF
        ld l,9
        out (c),l
        ld b,$BF
        out (c),a
        ret

; wait: HL Next cycles more to the next write. s_owed is the time still owed, in cycles; the CTC
; count since the last read takes 16 a count off. Below 0 is kept, so that the times do not
; drift. Keeps DE. Changes A, BC, HL.
wait:   push de
        ld de,(s_owed)
        add hl,de
1:      ld bc,$183B
        in e,(c)
        ld a,(s_prev)
        sub e
        ld d,a
        ld a,e
        ld (s_prev),a
        ld a,d
        ld d,0
        ld e,a
        ex de,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ex de,hl
        or a
        sbc hl,de
        bit 7,h
        jr nz,2F
        ld a,h
        or l
        jr nz,1B
2:      ld (s_owed),hl
        pop de
        ret

s_ayv:  db $00,$06,$06,$07,$08,$08,$09,$0A,$0A,$0B,$0C,$0C,$0D,$0E,$0E,$0F
s_sp:   dw 0
s_owed: dw 0
s_prev: db 0
s_last: db 0
        ds 16
s_stk:
endpage
