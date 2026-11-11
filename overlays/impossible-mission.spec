# Impossible Mission (Europe, Brazil) (En), CRC32 64D6AF3B, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - No free RST vector: $0000-$0002 (JP $00B1) is the io vector, and the game starts at $00B1,
#   which sets its own stack.
# - The spec patches nothing in the code that nothing in the cart reaches (verdict unused): the
#   VDP address setters $0486 and $048D, the unrolled OUTI block $04F7-$053C, and the character
#   expanders $6718-$6793 of the dispatcher at $6667, whose one table ($67ED) names only $6794.
#   $6718 calls $04C9, inside the routine that the page entry copy replaces.
# - No code runs from slot 2: banks 2-7 are data.
name Impossible Mission
cart 64D6AF3B
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
start 00B1
asm 000B5 2   ; IM 1 -> IM 2
    im 2
endasm
mapldk 000B7   # LD HL,$FFFC; LD (HL),$00
maphl 000BD   # LD (HL),$00, HL = $FFFD
maphl 000C0   # LD (HL),$01, HL = $FFFE
maphl 000C3   # LD (HL),$02, HL = $FFFF
mapst 00238   ; LD ($FFFF),A
mapst 00F24   ; LD ($FFFF),A
mapst 00F7C   ; LD ($FFFF),A
mapst 01113   ; LD ($FFFF),A
mapst 012C2   ; LD ($FFFF),A
mapst 01324   ; LD ($FFFF),A
mapst 01446   ; LD ($FFFF),A
mapst 0159B   ; LD ($FFFF),A
mapst 01C8D   ; LD ($FFFF),A
mapst 01ECA   ; LD ($FFFF),A
mapst 01F70   ; LD ($FFFF),A
mapst 024D4   ; LD ($FFFF),A
mapst 02D36   ; LD ($FFFF),A
mapst 03656   ; LD ($FFFF),A
mapst 03F78   ; LD ($FFFF),A
mapst 04103   ; LD ($FFFF),A
mapst 04114   ; LD ($FFFF),A
mapst 04130   ; LD ($FFFF),A
mapst 04142   ; LD ($FFFF),A
mapst 0492D   ; LD ($FFFF),A
mapst 04968   ; LD ($FFFF),A
mapst 0498F   ; LD ($FFFF),A
mapst 049A3   ; LD ($FFFF),A
mapst 04A82   ; LD ($FFFF),A
mapst 04A93   ; LD ($FFFF),A
mapst 04D18   ; LD ($FFFF),A
mapst 0501A   ; LD ($FFFF),A
mapst 05031   ; LD ($FFFF),A
mapst 06510   ; LD ($FFFF),A
mapst 065FB   ; LD ($FFFF),A
mapst 06676   ; LD ($FFFF),A
mapst 066B4   ; LD ($FFFF),A
site 000CC   ; OUT ($3E),A
site 000D0   ; OUT ($3F),A
site 00136   ; IN A,($BF)
site 00164   ; IN A,($DC)
site 00170   ; IN A,($DD)
site 00210   ; IN A,($BF)
site 00233   ; IN A,($BF)
site 00263   ; OTIR
site 00265   ; IN A,($DD)
site 0036F   ; OUT ($BF),A
site 00373   ; OUT ($BF),A
site 00376   ; OUT ($BE),A
site 00380   ; OUT ($BF),A
site 00384   ; OUT ($BF),A
site 00387   ; OUT ($BE),A
site 003C1   ; IN A,($BF)
site 00413   ; IN A,($BF)
site 00471   ; OUT ($BF),A
site 00478   ; OUT ($BF),A
site 0047C   ; OUT ($BF),A
site 00483   ; OUT ($BF),A
site 0049C   ; OUT ($BF),A
site 004A0   ; OUT ($BF),A
site 004A3   ; OUT ($BE),A
site 004A7   ; OUT ($BF),A
site 004AE   ; OUT ($BF),A
site 004B4   ; OUTI
site 004BC   ; OUT (C),B
site 004C0   ; OUT (C),B
site 004C3   ; OUT ($BE),A
site 004EF   ; OUT (C),B
site 007F2   ; OUT ($7F),A
site 007F5   ; OUT ($7F),A
site 007F9   ; OUT ($7F),A
site 00807   ; OTIR
site 0081F   ; OUT ($7F),A
site 00B30   ; IN A,($BF)
site 0633F   ; OUT ($7F),A
site 06363   ; OUT ($7F),A
site 06387   ; OUT ($7F),A
site 063A2   ; OUT ($7F),A
site 063AF   ; OUT ($7F),A
site 063BB   ; OUT ($7F),A
site 063CA   ; OUT ($7F),A
site 06515   ; OUT ($7F),A
site 06518   ; OUT ($7F),A
site 0651C   ; OUT ($7F),A
site 0651F   ; OUT ($7F),A
site 06523   ; OUT ($7F),A
site 06526   ; OUT ($7F),A
site 06529   ; OUT ($7F),A
site 0653C   ; OUTI
site 0653E   ; OUTI
site 06540   ; OUTI
site 06559   ; OUTI
site 0655B   ; OUTI
site 0655D   ; OUTI
site 0656D   ; OUT ($7F),A
site 06571   ; OUT ($7F),A
site 06575   ; OUT ($7F),A
site 06709   ; OUT ($BE),A
site 06711   ; OUT ($BE),A
# $6714 jumps through the routine address at $C0EC, from the character set table at $C400 that
# $6603 fills from the cart; the reference ran these four writes.
site 067D7   ; OUT ($BE),A
site 067DC   ; OUT ($BE),A
site 067E1   ; OUT ($BE),A
site 067E6   ; OUT ($BE),A
# Every HALT the game has is EI then HALT: the main loops and the screen waits pace frames with them.
eihalt 006A7
eihalt 0119F
eihalt 01487
eihalt 020BA
eihalt 021C1
eihalt 02358
eihalt 0235A
eihalt 0237B
eihalt 023B7
eihalt 02FD8
eihalt 03091
eihalt 03267
eihalt 03372
eihalt 037B7
eihalt 0405C
eihalt 0405E
eihalt 04907
eihalt 04920
eihalt 04A22
eihalt 04A46
eihalt 04A4D
eihalt 04FBD
eihalt 04FC4
eihalt 04FE2
eihalt 04FF1

# $04C6 sets the VRAM write address HL and copies BC bytes from DE to the data port with an
# OUTI loop (it doubles BC because OUTI and DJNZ both count B down). The frame handler calls it with BC = $0600 for the whole name table from $C900 in
# one of its three phases, and the room screens call it with up to $3380. Through the I/O RST
# that copy fills the frame, and the game loop between the handler's phases does not run. The
# page entry copy writes the same bytes with jt_vwrite.
asm 004C6 32   ; the routine, up to its RET at $04E5
    rst $00
    db far_io, pg_copy, ent_copy
    ret
endasm
page 0 copy
;; The entry turns interrupts off and runs on the page's own stack. It puts the game's
;; interrupt state back with the byte before its RET.

; copy: from $04C6. HL = VRAM address, DE = source, BC = bytes.
; Returns as the routine does: HL = the source moved on by the bytes, DE = the VRAM address
; it was given, A = 0, B = 0, C = $BE, Z set.
copy:   ld a,i                  ; P/V = IFF2
        di
        ld a,$FB                ; EI
        jp pe,.on
        xor a                   ; NOP
.on:    ld (.ei),a
        ld (gsp),sp
        ld sp,stk
        push ix
        push iy
        push hl                 ; the VRAM address, returned in DE
        ex de,hl                ; HL = source, DE = VRAM address
        ld a,c
        or a
        jr z,.whole
        push bc                 ; first the C bytes that are not a whole 256
        ld b,c
        ld c,1
        ld ix,0
        ld iy,0
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop bc
        push bc
        ld b,0
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        pop bc
.whole: ld a,b
        or a
        jr z,.done
        ld c,b                  ; B runs of 256 bytes
        ld b,0
        ld ix,256
        ld iy,256
        xor a
        call jt_vwrite
        ld a,h
        add a,c
        ld h,a
.done:  pop de
        pop iy
        pop ix
        ld bc,$00BE
        xor a
        ld sp,(gsp)
.ei:    nop                     ; EI when the game had interrupts on
        ret

gsp:    dw 0
        ds 32
stk:
endpage

# The speech player at $6510 writes each 4-bit sample with three OUTI to the PSG and waits
# ($C008) DJNZ steps between samples. The OUTI go through the runtime and the DJNZ runs at
# 28 MHz, so with the game's delays the speech plays at 0.80 of the Master System's time and
# sounds high. These are the delays that give each sample the Master System's time (1898
# T-states a byte at $3D); nothing else reads $C008.
poke 0117E 3D A1   ; LD A,$3D at $117D
poke 0407A 3D A1   ; LD A,$3D at $4079
poke 0114E 36 71   ; LD A,$36 at $114D
poke 01164 30 47   ; LD A,$30 at $1163

# Impossible Mission (Europe, Brazil).cht, "Infinite Time - Seconds", "Infinite Time - Minutes" and
# "Infinite Time - Hours": RAM $C0CC, $C0CB and $C0CA are the clock seconds, minutes and hours
# in BCD. Held at 0, the clock reads 00:00:00 and the 10 minutes added for each death are lost
poke "Infinite time"
ar 00C0-CC00
ar 00C0-CB00
ar 00C0-CA00
endpoke

# Impossible Mission (Europe, Brazil).cht, "Freeze Timer": RAM $C0CD is the tick counter
# between clock seconds. Held at $32, the clock does not run; each death still adds 10 minutes
poke "Freeze clock"
ar 00C0-CD32
endpoke
