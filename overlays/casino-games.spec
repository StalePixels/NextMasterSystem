# Casino Games (USA, Europe), CRC32 3CFF6E80, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with hand entry points, then decided by hand.
#
# Decisions:
# - Entry points given to the scan by hand (sitescan --entry): the game runs as tasks. Each
#   task starts at the DE of an LD DE,nn before CALL or JP $0C0A or $0C0C, and runs with bank 2
#   in slot 2 ($0BEB). The VRAM routines at $01B2, $01BD, $01C8, $01D3 and $0233 and the sound
#   calls at $05F8 and $062B are reached the same way.
# - The frame handler jumps through $C00D for line interrupts and calls the hook at $C00F once
#   a frame. Pinball's intro sets per-line handlers: $1031 (register 8 from a table at $D600,
#   one entry for each line) and $106C (register 2 from the same table).
# - No free RST vector ($0008-$0037 is code): $0000-$0002 (DI; IM 1) is the io vector and the
#   game starts at $0003. The game runs no RST $00 and jumps to no $0000.
# - $0829, $0867 and $08AD unpack tiles: for each byte a data write, then one or three data
#   port reads to skip the other bitplanes. Page 0 entries unpk2 and unpk4 do the same writes
#   with jt_vwrite, one call for each run.
# - The game shows the SEGA logo only on a Japanese machine ($00AF stores the region in $C006,
#   bank 2 $8000 skips the logo when it is set).
# - The DJNZ waits at $036E-$037C in the frame handler time a palette write and are left.
# - Not code: the bytes in banks 7, 9, 12 and 13 that read as I/O (tile graphics, a word table).
name Casino Games
cart 3CFF6E80
hz any		; No-Intro regions USA, Europe
vector 00 io
start 0003
asm 00CD2 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00CDD 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00CE8 2   ; IM 1 -> IM 2
    im 2
endasm
site 0003A   ; IN A,($BF)
site 00047   ; OUT ($BF),A
site 0004C   ; OUT ($BF),A
site 00075   ; OTIR
site 00093   ; OUT ($3F),A
site 00095   ; IN A,($DD)
site 0009F   ; OUT ($3F),A
site 000A1   ; IN A,($DD)
site 000AA   ; OUT ($3F),A
site 000B8   ; OUT ($3E),A
site 000C0   ; OUT ($F2),A
site 000C3   ; IN A,($F2)
site 000D5   ; OUT ($F2),A
site 000DD   ; OUT ($3E),A
site 000E6   ; IN A,($BF)
site 000EC   ; IN A,($BF)
site 000F3   ; IN A,($BF)
site 00105   ; IN A,($BF)
site 0011A   ; OUTI
site 0011C   ; OUT ($BF),A
site 00123   ; OUT ($BF),A
site 00127   ; OUT ($BF),A
site 0012F   ; OUT ($BE),A
site 00137   ; OUT ($BF),A
site 0013B   ; OUT ($BF),A
site 0013F   ; OUT ($BE),A
site 001B9   ; IN A,($BE)
site 001C4   ; IN A,($BE)
site 001CF   ; OUT ($BE),A
site 001DA   ; OUT ($BE),A
site 001E0   ; OUT ($BF),A
site 001E3   ; OUT ($BF),A
site 001E9   ; OUT ($BF),A
site 001EC   ; OUT ($BF),A
site 001F2   ; OUT ($BF),A
site 001F7   ; OUT ($BF),A
site 001FD   ; OUT ($BF),A
site 00202   ; OUT ($BF),A
site 00210   ; OUT ($BE),A
site 00223   ; OUT ($BE),A
site 00229   ; OUT ($BE),A
site 00241   ; INI
asm 00829 5    ; DI; CALL $01FB; EI: the unpacker with a VRAM step of 2, in page code
    rst $00
    db far_io, pg_unpk2, ent_unpk2
    ret
endasm
asm 00867 5    ; DI; CALL $01FB; EI: the unpacker with a VRAM step of 4, in page code
    rst $00
    db far_io, pg_unpk4, ent_unpk4
    ret
endasm
asm 008AD 5    ; DI; CALL $01FB; EI: the slow unpacker with a VRAM step of 4, in page code
    rst $00
    db far_io, pg_unpk4, ent_unpk4
    ret
endasm
page 0 unpk2 unpk4
; unpk2, unpk4: do what the game's unpackers at $0829, $0867 and $08AD do, with jt_vwrite, one
; call for each run. HL points at runs: a count byte n, 0 to end; bit 7 clear: n bytes follow,
; each written once; bit 7 set: one byte follows, written n AND $7F times (0 means 256). The
; bytes go to VRAM DE, then on by the step (2 or 4): the game writes one byte and skips the
; others with data port reads. Returns as the game's RET Z does: HL after the 0, DE as at the
; call, A = 0 and Z set, C = $BE, B = 0 once a run is written, interrupts on (the game's EI
; after it sets the VDP address).
; Runs on its own stack with interrupts off.
unpk2:  di
        ld (u_sp),sp
        ld sp,u_stk
        push iy
        ld iy,2
        jr unpk
unpk4:  di
        ld (u_sp),sp
        ld sp,u_stk
        push iy
        ld iy,4
unpk:   push ix
        push de
.run:   call jt_peek            ; A = the count byte, as the game sees it
        inc hl
        or a
        jr z,.end
        ld b,1                  ; one byte for each run
        ld c,a
        res 7,c                 ; C: the runs, 0 means 256
        ld ix,0                 ; bit 7 set: one source byte, written C times
        bit 7,a
        jr nz,1F
        ld ix,1                 ; bit 7 clear: C source bytes
1:      push af
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop af
        ld b,0
        push hl                 ; DE += step * runs
        ld h,b
        ld l,c
        ld a,c
        or a
        jr nz,2F
        inc h                   ; 0 runs is 256
2:      ld a,iyl
3:      add hl,hl
        rrca
        bit 0,a
        jr z,3B
        add hl,de
        ex de,hl
        pop hl
        ld a,ixl                ; HL: past the bytes (IX = 1) or past the one byte
        or a
        jr z,4F
        add hl,bc
        ld a,c
        or a
        jr nz,.run
        inc h                   ; 256 bytes
        jr .run
4:      inc hl
        jr .run
.end:   pop de
        pop ix
        pop iy
        ld c,$BE
        ld sp,(u_sp)
        xor a                   ; A = 0, Z set, as the game's RET Z leaves them
        ei
        ret
u_sp:   dw 0
        ds 64
u_stk:
endpage
otir 0025B   ; OUTI
site 0027C   ; OUT (C),H
site 00281   ; OUT (C),L
site 002C3   ; IN A,($BE)
site 002C8   ; IN A,($BE)
site 002CD   ; OUT ($BE),A
site 002D5   ; OUT ($BE),A
site 002FB   ; IN A,($DD)
site 00320   ; OUT ($BF),A
site 00324   ; OUT ($BF),A
site 0033B   ; OUT ($BF),A
site 0033F   ; OUT ($BF),A
site 00342   ; OUT ($BF),A
site 00346   ; OUT ($BF),A
site 0034A   ; OUT ($BF),A
site 0034E   ; OUT ($BF),A
site 00358   ; OUT ($BF),A
site 0035C   ; OUT ($BF),A
site 00380   ; OUT ($BF),A
site 00384   ; OUT ($BF),A
site 003A3   ; OUT ($BF),A
site 003A6   ; OUT ($BF),A
otir 003B4   ; OUTI
site 003DC   ; OUT (C),E
site 003DE   ; OUT (C),D
otir 003E2   ; OUTI
site 004DD   ; OUTI
site 004DF   ; OUTI
site 004E1   ; OUTI
site 004E3   ; OUTI
site 004E5   ; OUTI
site 004E7   ; OUTI
site 004E9   ; OUTI
site 004EB   ; OUTI
site 004ED   ; OUTI
site 004EF   ; OUTI
site 004F1   ; OUTI
site 004F3   ; OUTI
site 004F5   ; OUTI
site 004F7   ; OUTI
site 004F9   ; OUTI
site 004FB   ; OUTI
site 004FD   ; OUTI
site 004FF   ; OUTI
site 00501   ; OUTI
site 00503   ; OUTI
site 00505   ; OUTI
site 00507   ; OUTI
site 00509   ; OUTI
site 0050B   ; OUTI
site 0050D   ; OUTI
site 0050F   ; OUTI
site 00511   ; OUTI
site 00513   ; OUTI
site 00515   ; OUTI
site 00517   ; OUTI
site 00519   ; OUTI
site 0051B   ; OUTI
site 0051D   ; OUTI
site 0051F   ; OUTI
site 00521   ; OUTI
site 00523   ; OUTI
site 00525   ; OUTI
site 00527   ; OUTI
site 00529   ; OUTI
site 0052B   ; OUTI
site 0052D   ; OUTI
site 0052F   ; OUTI
site 00531   ; OUTI
site 00533   ; OUTI
site 00535   ; OUTI
site 00537   ; OUTI
site 00539   ; OUTI
site 0053B   ; OUTI
site 0053D   ; OUTI
site 0053F   ; OUTI
site 00541   ; OUTI
site 00543   ; OUTI
site 00545   ; OUTI
site 00547   ; OUTI
site 00549   ; OUTI
site 0054B   ; OUTI
site 0054D   ; OUTI
site 0054F   ; OUTI
site 00551   ; OUTI
site 00553   ; OUTI
site 00555   ; OUTI
site 00557   ; OUTI
site 00559   ; OUTI
site 0055B   ; OUTI
site 0055D   ; OUTI
site 0055F   ; OUTI
site 00561   ; OUTI
site 00563   ; OUTI
site 00565   ; OUTI
site 00567   ; OUTI
site 00569   ; OUTI
site 0056B   ; OUTI
site 0056D   ; OUTI
site 0056F   ; OUTI
site 00571   ; OUTI
site 00573   ; OUTI
site 00575   ; OUTI
site 00577   ; OUTI
site 00579   ; OUTI
site 0057B   ; OUTI
site 0057D   ; OUTI
site 0057F   ; OUTI
site 00581   ; OUTI
site 00583   ; OUTI
site 00585   ; OUTI
site 00587   ; OUTI
site 00589   ; OUTI
site 0058B   ; OUTI
site 0058D   ; OUTI
site 0058F   ; OUTI
site 00591   ; OUTI
site 00593   ; OUTI
site 00595   ; OUTI
site 00597   ; OUTI
site 00599   ; OUTI
site 0059B   ; OUTI
site 0059D   ; OUTI
site 0059F   ; OUTI
site 005A1   ; OUTI
site 005A3   ; OUTI
site 005A5   ; OUTI
site 005A7   ; OUTI
site 005A9   ; OUTI
site 005AB   ; OUTI
site 005AD   ; OUTI
site 005AF   ; OUTI
site 005B1   ; OUTI
site 005B3   ; OUTI
site 005B5   ; OUTI
site 005B7   ; OUTI
site 005B9   ; OUTI
site 005BB   ; OUTI
site 005BD   ; OUTI
site 005BF   ; OUTI
site 005C1   ; OUTI
site 005C3   ; OUTI
site 005C5   ; OUTI
site 005C7   ; OUTI
site 005C9   ; OUTI
site 005CB   ; OUTI
site 005CD   ; OUTI
site 005CF   ; OUTI
site 005D1   ; OUTI
site 005D3   ; OUTI
site 005D5   ; OUTI
site 005D7   ; OUTI
site 005D9   ; OUTI
site 005DB   ; OUTI
site 0065F   ; OUT ($DF),A
site 00663   ; OUT ($DE),A
site 00666   ; IN A,($DC)
site 0066C   ; IN A,($DC)
site 0066F   ; IN A,($DD)
site 00838   ; OUTI
site 0083A   ; IN A,($BE)
site 00846   ; OUT (C),A
site 00848   ; IN A,($BE)
site 00876   ; OUTI
site 00878   ; IN A,($BE)
site 0087A   ; IN A,($BE)
site 0087C   ; IN A,($BE)
site 00888   ; OUT (C),A
site 0088A   ; IN A,($BE)
site 0088C   ; IN A,($BE)
site 0088E   ; IN A,($BE)
site 008BC   ; OUTI
site 008C1   ; IN A,($BE)
site 008C6   ; IN A,($BE)
site 008CB   ; IN A,($BE)
site 008DA   ; OUT ($BE),A
site 008DF   ; IN A,($BE)
site 008E4   ; IN A,($BE)
site 008E9   ; IN A,($BE)
site 00F1A   ; OUT ($BF),A
site 00F1E   ; OUT ($BF),A
site 00F22   ; OUT ($BE),A
site 00F30   ; OUT ($BF),A
site 00F34   ; OUT ($BF),A
site 00F43   ; OUT ($BF),A
site 00F47   ; OUT ($BF),A
site 00F68   ; OUT (C),L
site 00F6A   ; OUT (C),H
site 00F70   ; OUT ($BE),A
site 00F76   ; OUT ($BE),A
site 00FC6   ; OUT ($BF),A
site 00FCA   ; OUT ($BF),A
site 00FD8   ; OUT ($BF),A
site 00FDC   ; OUT ($BF),A
site 00FE1   ; OUT ($BE),A
site 00FFC   ; OUT ($BF),A
site 01000   ; OUT ($BF),A
site 0101C   ; OUT ($BF),A
site 01020   ; OUT ($BF),A
site 01031   ; IN A,($7E)
site 01037   ; OUT ($BF),A
site 0103B   ; OUT ($BF),A
site 01057   ; OUT ($BF),A
site 0105B   ; OUT ($BF),A
site 0106C   ; IN A,($7E)
site 01072   ; OUT ($BF),A
site 01076   ; OUT ($BF),A
site 01A63   ; INI
site 01A6B   ; INI
site 01A7E   ; INI
site 01A86   ; INI
site 01AA9   ; INI
site 01B0F   ; INI
otir 01C07   ; OUTI
otir 01C10   ; OUTI
otir 01C24   ; OUTI
otir 01C2D   ; OUTI
otir 01C8E   ; OUTI
site 02219   ; OUT ($BF),A
site 0221E   ; OUT ($BF),A
otir 02227   ; OUTI
site 07EC6   ; OUT ($BE),A
site 07ECC   ; OUT ($BE),A
site 3C15C   ; OUT ($F0),A
site 3C15F   ; OUT ($F1),A
site 3C188   ; OUT ($F0),A
site 3C190   ; OUT ($F1),A
site 3C1A0   ; OUT ($F0),A
site 3C1A3   ; OUT ($F1),A
site 3C1BC   ; OUT ($F1),A
site 3C1D0   ; OUT ($F0),A
site 3C1D7   ; OUT ($F1),A
site 3C1DE   ; OUT ($F1),A
site 3C1F1   ; OUT ($F0),A
site 3C1F4   ; OUT ($F1),A
site 3C206   ; OUT ($F0),A
site 3C20B   ; OUT ($F1),A
site 3C21D   ; OUT ($F1),A
site 3C231   ; OUT ($F0),A
site 3C234   ; OUT ($F1),A
site 3C247   ; OUT ($7F),A
site 3C24D   ; OUT ($7F),A
site 3C259   ; OUT ($7F),A
site 3C276   ; OUT ($7F),A
site 3C27F   ; OUT ($7F),A
site 3C9EC   ; OUT (C),A
site 3C9F0   ; OUT (C),A
site 3CA00   ; OUT ($F0),A
site 3CA04   ; OUT ($F1),A
site 3CA1F   ; OUT ($F0),A
site 3CA22   ; OUT ($F1),A
site 3CA3E   ; OUT ($F2),A
mapldk 00003   # LD HL,$FFFC; LD (HL),$80
maphl 00009   # LD (HL),$00, HL = $FFFD
maphl 0000C   # LD (HL),$01, HL = $FFFE
maphl 0000F   # LD (HL),$02, HL = $FFFF
mapst 0024B   ; LD ($FFFF),A
mapst 0039C   ; LD ($FFFF),A
mapst 00416   ; LD ($FFFF),A
mapst 0041D   ; LD ($FFFF),A
mapst 005E4   ; LD ($FFFF),A
mapst 005F4   ; LD ($FFFF),A
mapst 005FE   ; LD ($FFFF),A
mapst 00610   ; LD ($FFFF),A
mapst 00622   ; LD ($FFFF),A
mapst 00631   ; LD ($FFFF),A
mapst 0064E   ; LD ($FFFF),A
mapst 00752   ; LD ($FFFF),A
mapst 007A6   ; LD ($FFFF),A
mapld 007B0   # LD HL,$FFFF; LD (HL),$02
mapst 007E7   ; LD ($FFFF),A
mapst 007EF   ; LD ($FFFF),A
mapst 00819   ; LD ($FFFF),A
mapst 00821   ; LD ($FFFF),A
mapst 00850   ; LD ($FFFF),A
mapst 00858   ; LD ($FFFF),A
mapst 00896   ; LD ($FFFF),A
mapst 0089E   ; LD ($FFFF),A
mapst 00A58   ; LD ($FFFF),A
mapst 00A60   ; LD ($FFFF),A
mapst 00AB7   ; LD ($FFFF),A
mapst 00ABF   ; LD ($FFFF),A
mapst 00B36   ; LD ($FFFF),A
mapst 00B50   ; LD ($FFFF),A
mapst 00BED   ; LD ($FFFF),A
mapst 00E60   ; LD ($FFFF),A
mapst 00E68   ; LD ($FFFF),A
mapst 00E70   ; LD ($FFFF),A
mapst 00E78   ; LD ($FFFF),A
mapst 00E80   ; LD ($FFFF),A
mapst 00E88   ; LD ($FFFF),A
mapst 00E90   ; LD ($FFFF),A
mapst 00E98   ; LD ($FFFF),A
mapst 01266   ; LD ($FFFF),A
mapst 0126E   ; LD ($FFFF),A
mapst 014FF   ; LD ($FFFF),A
mapst 01506   ; LD ($FFFF),A
mapst 0186D   ; LD ($FFFF),A
mapst 019D3   ; LD ($FFFF),A
mapst 01F81   ; LD ($FFFF),A
mapst 02139   ; LD ($FFFF),A
mapst 02143   ; LD ($FFFF),A
mapst 0225B   ; LD ($FFFF),A
mapst 0227B   ; LD ($FFFF),A
mapst 02934   ; LD ($FFFF),A
mapst 0344D   ; LD ($FFFF),A
mapst 03524   ; LD ($FFFF),A
mapst 0355B   ; LD ($FFFF),A
mapst 03A05   ; LD ($FFFF),A
mapld 0448C   # LD HL,$FFFF; LD (HL),$06
mapld 044A5   # LD HL,$FFFF; LD (HL),$0D
mapld 04672   # LD HL,$FFFF; LD (HL),$0D
mapld 0468F   # LD HL,$FFFF; LD (HL),$0D
mapst 0494A   ; LD ($FFFF),A
mapst 05124   ; LD ($FFFF),A
mapld 05455   # LD HL,$FFFF; LD (HL),$0C
mapst 05754   ; LD ($FFFF),A
mapst 05785   ; LD ($FFFF),A
mapst 05939   ; LD ($FFFF),A
mapst 05966   ; LD ($FFFF),A
mapst 060C3   ; LD ($FFFF),A
mapst 061C8   ; LD ($FFFF),A
mapst 0666E   ; LD ($FFFF),A
mapst 06F44   ; LD ($FFFF),A
mapst 07174   ; LD ($FFFF),A
mapst 076B6   ; LD ($FFFF),A

# Casino Games (USA, Europe).cht, "Infinite Money": RAM $C927-$C929 is the player's money,
# six BCD digits; held at 999999 in every game
poke "Infinite money"
ar 00C9-2799
ar 00C9-2899
ar 00C9-2999
endpoke

# Casino Games (USA, Europe) (Action Replay).cht and Casino Games (USA, Europe).cht,
# "Infinite Pinballs": RAM $C845 is the ball counter of the pinball table; held at 0 the
# game never ends
poke "Infinite pinballs"
ar 00C8-4500
endpoke
