# Monopoly (USA, Europe), CRC32 69538469, 128K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with hand entry points, then decided by hand.
#
# Decisions:
# - Entry points given to the scan by hand (sitescan --entry): the computer players run as a
#   task of their own. $4023 switches to its stack ($CCB3, the word at $3FA9) and $4059 jumps to
#   the word at $CB54 ($4060, $430B or $42DD) with $405D as its return; $41C4 and $4315 switch
#   back. $4082 jumps to $B72E with bank 6 in slot 2 ($4044).
# - No free RST vector ($0008-$0037 is code): $0000-$0002 (DI; IM 1) is the io vector and the
#   game starts at $0003. The game runs no RST $00. The reset button ($0040 in the frame
#   handler, $0092 in the pause handler) and the ends of the demo ($0105) and of a game
#   ($01CF) jump to $0000; each goes to the cave at $333C, which does what $0000 does: DI,
#   then on to $0003.
# - $333C-$3341 are six zero bytes after JP NC,$3342 and JP C,$33E3: no path runs them.
# - Cart RAM: $74ED and $74F7 map it at $8000 ($FFFC bit 3) to save the whole of RAM
#   ($C000-$DFFF) with a sum at $9FFE ($7460) and to load it back ($749B).
# - Unused: the trampolines at $49BD, $4FF4 and $5002 (no call, jump or address names them;
#   their mapper stores are patched all the same) and the tile-row writer at $5285.
# - $7559 writes one bitplane of tile rows: for each byte a VDP address pair ($529C) and a data
#   write, the address moving on by 4. The 3D board walk runs it for whole screens. Page 0 entry
#   plane4 does the same writes with jt_vwrite, one call for each run.
# - CPU loops time the game: the computer players' wait after each of their actions ($4257, HL
#   units of 3229 T-states, ($CB60) units, skipped while a button is held), the delay before
#   each read of the pad in the menus ($69CE), the key repeat ($5C81, $5C91) and a pause ($55FD).
#   On the Next they run several times faster: the name cursor ran 10 times faster and the
#   computer players hurried. Page 0 entries aiwait, padwait, rptwait1, rptwait2 and pause
#   wait each loop's Master System time in video lines. The short loops are left as they are:
#   the button debounce at $4361 and $436C (256 DJNZ), $72D9 between sound driver calls and
#   bank 6 $85E5.
# - Not code: the words at $3FA9-$3FFD (a table of addresses, read as OUT ($3F),A), the
#   tile data in bank 7 ($9AA5) and the records at $6259-$63AF (read as RST $28).
name Monopoly
cart 69538469
hz any		; No-Intro regions USA, Europe
vector 00 io
start 0003
label cv_reset 0333C
asm 0333C 4    ; six zero bytes no path runs: the reset of $0000
    di
    jp $0003
endasm
asm 00040 3    ; JP Z,$0000: the reset button, in the frame handler
    jp z,cv_reset
endasm
asm 00092 3    ; JP Z,$0000: the reset button, in the pause handler
    jp z,cv_reset
endasm
asm 00105 3    ; JP $0000: a press ends the demo
    jp cv_reset
endasm
asm 001CF 3    ; JP $0000: the end of a game ($C32F set)
    jp cv_reset
endasm
asm 07559 5    ; LD A,(HL); INC HL; OR A; RET Z; LD B,A: the bitplane writer, in page code
    rst $00
    db far_io, pg_plane4, ent_plane4
    ret
endasm
asm 04257 6    ; the computer players' wait: HL units of a $7A-count loop, in page code
    rst $00
    db far_io, pg_aiwait, ent_aiwait
    jr $4266
endasm
asm 069CF 6    ; LD BC,$3000 and its loop: the delay before each read of the pad, in page code
    rst $00
    db far_io, pg_padwait, ent_padwait
    pop bc
    ret
endasm
asm 05C82 6    ; LD BC,$0800 and its loop: the key repeat's first delay, in page code
    rst $00
    db far_io, pg_rptwait1, ent_rptwait1
    jr $5C8A
endasm
asm 05C92 6    ; LD BC,$3800 and its loop: the key repeat's held delay, in page code
    rst $00
    db far_io, pg_rptwait2, ent_rptwait2
    jr $5C9A
endasm
asm 055FD 5    ; LD DE,$3A00 and its loop: a pause, in page code
    rst $00
    db far_io, pg_pause, ent_pause
    ret
endasm
page 0 plane4 aiwait padwait rptwait1 rptwait2 pause
; plane4: does what the game's routine at $7559-$757D does, with jt_vwrite. HL points at runs:
; a count byte n, 0 to end; bit 7 set: n AND $7F bytes follow (0 means 256), each written
; once; bit 7 clear: one byte follows, written n times. Each byte goes to VRAM DE (bit 14 set
; by the caller), then DE moves on by 4: one bitplane of a tile row after another. The game
; sets the VDP address with $529C (DI) for every byte, so it leaves interrupts off once it has
; written a byte. Returns as the game's RET Z does: HL after the 0, DE after the last byte,
; A = 0 and Z set; B and C are the game's last values (its caller pops both).
; Runs on its own stack with interrupts off.
plane4: ld a,i                  ; P/V = IFF2; read twice, as an interrupt in LD A,I clears it
        jp pe,1F
        ld a,i
1:      di
        ld (p_sp),sp
        ld sp,p_stk
        ld a,0
        jp po,2F
        inc a
2:      ld (p_ien),a
        push ix
        push iy
        ld iy,4                 ; the VRAM step
.run:   call jt_peek            ; A = the count byte, as the game sees it
        inc hl
        or a
        jr z,.end
        ld c,a                  ; C: the count byte, as the game keeps it
        ld b,a
        res 7,b                 ; B: the bytes in the run, 0 means 256
        xor a
        ld (p_ien),a            ; a byte is written: the game's $529C has turned interrupts off
        push bc
        ld ix,1                 ; bit 7 set: the bytes follow, one source byte for each
        bit 7,c
        jr nz,3F
        ld ix,0                 ; bit 7 clear: one source byte, written B times
3:      ld c,b                  ; runs of 1 byte: B runs
        ld b,1
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop bc
        push bc                 ; DE += 4 * runs (0 runs is 256)
        ld a,b
        ld b,0
        or a
        jr nz,4F
        inc b
4:      ld c,a
        sla c
        rl b
        sla c
        rl b
        ex de,hl
        add hl,bc
        ex de,hl
        pop bc
        ld a,b                  ; HL: past the bytes (bit 7 set) or past the one byte
        bit 7,c
        jr z,5F
        push bc
        ld c,a
        ld b,0
        or a
        jr nz,6F
        inc b
6:      add hl,bc
        pop bc
        jr .run
5:      inc hl
        jr .run
.end:   pop iy
        pop ix
        ld b,0                  ; the game's DJNZ leaves B = 0
        ld a,(p_ien)
        or a
        ld sp,(p_sp)
        ld a,0                  ; A = 0, Z set, as the game's RET Z leaves them
        jr z,7F
        cp a
        ei
        ret
7:      cp a
        ret
p_sp:   dw 0
p_ien:  db 0
        ds 64
p_stk:
;
; The waits: the game times these with CPU loops, which run many times faster on the Next. Each
; entry waits the loop's Master System time instead, in video lines: a Master System line is 228
; T-states, and the Next's line (311 a frame at 50 Hz, 264 at 60 Hz) takes about as long. The
; time owed is kept in lines and 1/256 lines; the beam's line (NextRegs $1E and $1F) takes off
; the lines that pass. They wait on the game's stack, with no stack use, and with the game's
; interrupt state, so that its interrupt handler runs as it would in the loop.
; aiwait: HL units (0 means 65536) of the loop $4257-$4265: 3229 T-states (14 41/256 lines) a
; unit. Returns HL = 0, A = 0, Z set, as the loop leaves them.
; padwait: $69CF-$69D6, BC = $3000: 1401 74/256 lines. rptwait1: $5C82-$5C89, BC = $0800: 233
; 144/256 lines. rptwait2: $5C92-$5C99, BC = $3800: 1634 210/256 lines. They return A = 0, Z
; set; BC is the caller's, as the POP BC after the loop leaves it.
; pause: $55FD-$5604, DE = $3A00: 1693 59/256 lines. Returns DE = 0, A = 0, Z set.
; Keep every other register.
        OPT --zxnext
        MACRO WENTER            ; IFF2 to w_ien, interrupts off, the page's stack
        ld (w_hl),hl
        ld a,i                  ; P/V = IFF2; read twice, as an interrupt in LD A,I clears it
        jp pe,.ie
        ld a,i
.ie:    di
        ld (w_sp),sp
        ld sp,w_stk
        ld a,0
        jp po,.io
        inc a
.io:    ld (w_ien),a
        push bc
        push de
        call wstart
        ENDM
aiwait: WENTER
        ld hl,(w_hl)
1:      push hl
        ld hl,14
        ld c,41
        call wait
        pop hl
        dec hl
        ld a,h
        or l
        jr nz,1B
        pop de
        pop bc
        jp wexit                ; HL = 0
padwait: WENTER
        ld hl,1401
        ld c,74
        jp wone
rptwait1: WENTER
        ld hl,233
        ld c,144
        jp wone
rptwait2: WENTER
        ld hl,1634
        ld c,210
wone:   call wait
        pop de
        pop bc
        ld hl,(w_hl)
        jp wexit
pause:  WENTER
        ld hl,1693
        ld c,59
        call wait
        pop de
        pop bc
        ld de,0
        ld hl,(w_hl)
wexit:  ld a,(w_ien)            ; A = 0 and Z set, the interrupt state as at the call
        or a
        ld sp,(w_sp)
        ld a,0
        jr z,2F
        cp a
        ei
        ret
2:      cp a
        ret

; wstart: no time owed; the lines a frame for the rate (NextReg $05 bit 2); the beam's line.
wstart: xor a
        ld (w_of),a
        ld h,a
        ld l,a
        ld (w_ol),hl
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld hl,311
        bit 2,a
        jr z,1F
        ld hl,264
1:      ld (w_lpf),hl
        call wline
        ld (w_prev),hl
        ret

; wline: HL = the beam's line, read until the high part reads the same twice. Changes A, BC.
wline:  ld bc,$243B
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
        ret

; wait: owe HL lines and C/256 more, then wait until nothing is owed. Called on the page's stack;
; waits on the game's stack. Changes A, BC, DE, HL.
wait:   ld a,(w_of)
        add a,c
        ld (w_of),a
        ld de,(w_ol)
        adc hl,de
        ld (w_ol),hl
        ld (w_psp),sp
        ld sp,(w_sp)            ; the wait, on the game's stack
.p:     ld a,(w_ien)
        or a
        jr z,.r
        ei
        nop
        di
.r:     ld bc,$243B             ; the beam's line, as wline reads it
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
        ld de,(w_prev)
        ld (w_prev),hl
        or a
        sbc hl,de               ; the lines since the last read
        jr nc,2F
        ld de,(w_lpf)
        add hl,de
2:      ex de,hl
        ld hl,(w_ol)
        or a
        sbc hl,de
        ld (w_ol),hl
        bit 7,h
        jr nz,3F
        ld a,h
        or l
        jr nz,.p
3:      ld sp,(w_psp)
        ret

w_hl:   dw 0
w_sp:   dw 0
w_psp:  dw 0
w_ien:  db 0
w_of:   db 0
w_ol:   dw 0
w_prev: dw 0
w_lpf:  dw 0
        ds 32
w_stk:
endpage
site 0003A   ; IN A,($BF)
site 0003C   ; IN A,($DD)
site 0008E   ; IN A,($DD)
site 000E9   ; IN A,($DC)
site 000EF   ; IN A,($DD)
site 023F9   ; OUT ($3F),A
site 023FB   ; IN A,($DD)
site 02403   ; IN A,($DC)
site 02426   ; IN A,($DC)
site 02429   ; IN A,($DD)
site 0434C   ; IN A,($DC)
site 04353   ; IN A,($DD)
site 05125   ; OUT ($BE),A
site 05130   ; OUT ($BE),A
site 05134   ; OUT ($BE),A
site 051B0   ; OUT ($BE),A
site 051B7   ; OUT ($BE),A
site 0529E   ; OUT ($BF),A
site 052A4   ; OUT ($BF),A
site 052AF   ; OUT ($BE),A
site 052C0   ; OUT ($BE),A
site 052C7   ; OUT ($BE),A
site 052E7   ; OUT ($BE),A
site 056F3   ; OUT ($BF),A
site 056FA   ; OUT ($BF),A
site 05701   ; OUT ($BE),A
site 0570B   ; OUT ($BE),A
site 05778   ; OUT ($BE),A
site 05CA1   ; IN A,($DC)
site 05CA7   ; IN A,($DD)
site 0650D   ; OUT ($BE),A
site 06661   ; OUT ($BE),A
site 06AEE   ; IN A,($BE)
site 06B01   ; IN A,($BE)
site 07565   ; OUT ($BE),A
site 077D5   ; OUT ($BE),A
site 07C59   ; OUT ($BE),A
site 07DAA   ; OUT ($BE),A
site 1C014   ; OUT ($7F),A
site 1C025   ; OUT ($7F),A
site 1C03B   ; OUT ($7F),A
site 1C043   ; OUT ($7F),A
site 1C34E   ; OUT ($3F),A
site 1C350   ; IN A,($DD)
site 1C35A   ; OUT ($3F),A
site 1C35C   ; IN A,($DD)
site 1C364   ; OUT ($3F),A
mapst 00015   ; LD ($FFFF),A
mapst 0002F   ; LD ($FFFF),A
mapst 00060   ; LD ($FFFC),A
mapst 00082   ; LD ($FFFF),A
mapst 0008B   ; LD ($FFFF),A
mapst 000FC   ; LD ($FFFF),A
mapst 00110   ; LD ($FFFF),A
mapst 00119   ; LD ($FFFF),A
mapst 00153   ; LD ($FFFF),A
mapst 00186   ; LD ($FFFF),A
mapst 001B1   ; LD ($FFFF),A
mapst 00393   ; LD ($FFFF),A
mapst 0044F   ; LD ($FFFF),A
mapst 00B7B   ; LD ($FFFF),A
mapst 00DB5   ; LD ($FFFF),A
mapst 0125F   ; LD ($FFFF),A
mapst 01273   ; LD ($FFFF),A
mapst 01670   ; LD ($FFFF),A
mapst 01764   ; LD ($FFFF),A
mapst 01825   ; LD ($FFFF),A
mapst 0193E   ; LD ($FFFF),A
mapst 01AB9   ; LD ($FFFF),A
mapst 01B14   ; LD ($FFFF),A
mapst 01F63   ; LD ($FFFF),A
mapst 02026   ; LD ($FFFF),A
mapst 02194   ; LD ($FFFF),A
mapst 023D4   ; LD ($FFFF),A
mapst 023DB   ; LD ($FFFF),A
mapst 023E1   ; LD ($FFFF),A
mapst 023E9   ; LD ($FFFF),A
mapst 0342F   ; LD ($FFFF),A
mapst 0399B   ; LD ($FFFF),A
mapst 039AD   ; LD ($FFFF),A
mapst 04046   ; LD ($FFFF),A
mapst 04093   ; LD ($FFFF),A
mapst 0409A   ; LD ($FFFF),A
mapst 040E3   ; LD ($FFFF),A
mapst 040EA   ; LD ($FFFF),A
mapst 040F6   ; LD ($FFFF),A
mapst 040FD   ; LD ($FFFF),A
mapst 041AD   ; LD ($FFFF),A
mapst 0431C   ; LD ($FFFF),A
mapst 0438A   ; LD ($FFFF),A
mapst 049B6   ; LD ($FFFF),A
mapst 04FB4   ; LD ($FFFF),A
mapst 04FC2   ; LD ($FFFF),A
mapst 04FD0   ; LD ($FFFF),A
mapst 04FDE   ; LD ($FFFF),A
mapst 04FEC   ; LD ($FFFF),A
mapst 0500F   ; LD ($FFFF),A
mapst 05399   ; LD ($FFFF),A
mapst 053C8   ; LD ($FFFF),A
mapst 054A5   ; LD ($FFFF),A
mapst 05764   ; LD ($FFFF),A
mapst 057BE   ; LD ($FFFF),A
mapst 057C9   ; LD ($FFFF),A
mapst 057F4   ; LD ($FFFF),A
mapst 05812   ; LD ($FFFF),A
mapst 0582C   ; LD ($FFFF),A
mapst 05855   ; LD ($FFFF),A
mapst 05866   ; LD ($FFFF),A
mapst 05892   ; LD ($FFFF),A
mapst 0589D   ; LD ($FFFF),A
mapst 058A6   ; LD ($FFFF),A
mapst 058D7   ; LD ($FFFF),A
mapst 058E9   ; LD ($FFFF),A
mapst 0591D   ; LD ($FFFF),A
mapst 059A6   ; LD ($FFFF),A
mapst 059DD   ; LD ($FFFF),A
mapst 05A4F   ; LD ($FFFF),A
mapst 05AE4   ; LD ($FFFF),A
mapst 05B3A   ; LD ($FFFF),A
mapst 05B5A   ; LD ($FFFF),A
mapst 05B67   ; LD ($FFFF),A
mapst 05DD2   ; LD ($FFFF),A
mapst 05E13   ; LD ($FFFF),A
mapst 05E31   ; LD ($FFFF),A
mapst 05E59   ; LD ($FFFF),A
mapst 05E93   ; LD ($FFFF),A
mapst 0641A   ; LD ($FFFF),A
mapst 06480   ; LD ($FFFF),A
mapst 064A9   ; LD ($FFFF),A
mapst 064D9   ; LD ($FFFF),A
mapst 06647   ; LD ($FFFF),A
mapst 066D0   ; LD ($FFFF),A
mapst 068BC   ; LD ($FFFF),A
mapst 06A2C   ; LD ($FFFF),A
mapst 06A43   ; LD ($FFFF),A
mapst 06A7E   ; LD ($FFFF),A
mapst 06A98   ; LD ($FFFF),A
mapst 06BAF   ; LD ($FFFF),A
mapst 06BC0   ; LD ($FFFF),A
mapst 06CC6   ; LD ($FFFF),A
mapst 06CFB   ; LD ($FFFF),A
mapst 06D15   ; LD ($FFFF),A
mapst 06D56   ; LD ($FFFF),A
mapst 06E4B   ; LD ($FFFF),A
mapst 06E68   ; LD ($FFFF),A
mapst 06E96   ; LD ($FFFF),A
mapst 06EA6   ; LD ($FFFF),A
mapst 06EF9   ; LD ($FFFF),A
mapst 06F0B   ; LD ($FFFF),A
mapst 06F2B   ; LD ($FFFF),A
mapst 06F6B   ; LD ($FFFF),A
mapst 06FA0   ; LD ($FFFF),A
mapst 06FEC   ; LD ($FFFF),A
mapst 06FF9   ; LD ($FFFF),A
mapst 07012   ; LD ($FFFF),A
mapst 07076   ; LD ($FFFF),A
mapst 0709D   ; LD ($FFFF),A
mapst 070D3   ; LD ($FFFF),A
mapst 070FA   ; LD ($FFFF),A
mapst 0713A   ; LD ($FFFF),A
mapst 0716F   ; LD ($FFFF),A
mapst 071C1   ; LD ($FFFF),A
mapst 0728B   ; LD ($FFFF),A
mapst 072F5   ; LD ($FFFF),A
mapst 07318   ; LD ($FFFF),A
mapst 0733A   ; LD ($FFFF),A
mapst 07357   ; LD ($FFFF),A
mapst 07380   ; LD ($FFFF),A
mapst 073A3   ; LD ($FFFF),A
mapst 073C5   ; LD ($FFFF),A
mapst 073EC   ; LD ($FFFF),A
mapst 074B2   ; LD ($FFFF),A
mapst 074F3   ; LD ($FFFC),A
mapst 074FC   ; LD ($FFFC),A
mapst 07597   ; LD ($FFFF),A
mapst 075F1   ; LD ($FFFF),A
mapst 07750   ; LD ($FFFF),A
mapst 07777   ; LD ($FFFF),A
mapst 07788   ; LD ($FFFF),A
mapst 077F9   ; LD ($FFFF),A
mapst 07808   ; LD ($FFFF),A
mapst 078F0   ; LD ($FFFF),A
mapst 07928   ; LD ($FFFF),A
mapst 07930   ; LD ($FFFF),A
mapst 0795F   ; LD ($FFFF),A
mapst 079A8   ; LD ($FFFF),A
mapst 079DE   ; LD ($FFFF),A
mapst 079F5   ; LD ($FFFF),A
mapst 07A1C   ; LD ($FFFF),A
mapst 07A24   ; LD ($FFFF),A
mapst 07A63   ; LD ($FFFF),A
mapst 07ADB   ; LD ($FFFF),A
mapst 07AF0   ; LD ($FFFF),A
mapst 07B1C   ; LD ($FFFF),A
mapst 07B42   ; LD ($FFFF),A
mapst 07B6C   ; LD ($FFFF),A
mapst 07B8F   ; LD ($FFFF),A
mapst 07BC9   ; LD ($FFFF),A
mapst 07BFA   ; LD ($FFFF),A
mapst 07C11   ; LD ($FFFF),A
mapst 07C31   ; LD ($FFFF),A
mapst 07C5F   ; LD ($FFFF),A
mapst 07C72   ; LD ($FFFF),A
mapst 07C99   ; LD ($FFFF),A
mapst 07CDB   ; LD ($FFFF),A
mapst 07D50   ; LD ($FFFF),A
mapst 07DFE   ; LD ($FFFF),A
mapst 07E4C   ; LD ($FFFF),A
mapst 07E5D   ; LD ($FFFF),A
mapst 07E65   ; LD ($FFFF),A
mapst 049BF   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
mapst 04FFA   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
mapst 05008   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
