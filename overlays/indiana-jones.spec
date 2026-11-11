# Indiana Jones and the Last Crusade (Europe, Brazil) (En), CRC32 8AEB574B, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - No free RST vector: $0000-$0002 (DI; IM 1) becomes the io vector, and the game starts
#   at $0003. The game has no RST of its own and no JP $0000.
# - The reset code clears $C000-$FF7F with one LDIR ($0089-$0093). $E000-$FEFF is the RAM
#   mirror on a Master System and the runtime's page on the Next, so the clear stops at $DFFF.
# - $6B59 counts loop passes in one frame to tell a 50 Hz machine from a 60 Hz one and keeps
#   the result in $C985 (0: 50 Hz; 1: 60 Hz). The count depends on the CPU speed: on the
#   Next it is out of range and the test runs again for ever. The test at $6B60 sets the
#   50 Hz value. Its four HALTs no longer run.
# - Code that no scanned path reaches, patched as code (it costs nothing if it never runs):
#   $116B (writes $1F to $FFFF, reads all of VRAM into $8000-$BFFF, then loops for ever),
#   $130F (writes colour B to CRAM entry C) and $1773 (reads Button 2 into $C92E).
# - The LD (BC),A stores at $0539-$0570 are in the level tables at $0532-$0575, whose
#   addresses the game keeps in $C983: the pointer harvest took them for code.
# - The sprite tile stream at $455A writes, for each entry of the list at ($C95B), a
#   32-byte tile from slot 2: with OUTI (its DJNZ takes a second 1 off B), or, for a sprite
#   that faces left, through the flip table at $C400 with one OUT a byte ($4597-$4638).
#   Through the runtime that costs up to 70% of a play frame and puts play frames over 100%,
#   and the game, which runs one step a frame and waits for the frame interrupt at $06C1,
#   then loses a frame. Page 0 (stream) does the whole routine: the VDP address as the game
#   writes it, then each tile with jt_vwrite, the flipped ones from a buffer.
name Indiana Jones and the Last Crusade
cart 8AEB574B
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
start 0003
asm 00090 3   ; LD BC,$3F80: the reset clear of $C000-$FF7F, whose $E000-$FEFF is the RAM mirror
    ld bc,$1FFF   ; $C000-$DFFF only: $E000-$FFFF is the runtime's page on the Next
endasm
asm 06B60 4   ; EI; HALT; HALT; HALT: the speed test of $6B59, which counts loop passes in a frame
    xor a         ; $C985 = 0, the 50 Hz value
    jp $6B8A
endasm
asm 0455A 5   ; LD C,$BF; LD HL,($C945): the sprite tile stream goes to page code
    rst $00
    db far_io, pg_stream, ent_stream
    ret
endasm
page 0 stream
; stream ($455A): B = the list entries to write. ($C945) = the VRAM address, ($C95B) = the
; list: per entry a flag (0: 32 bytes as they are; else 32 bytes through the flip table at
; $C400), the bank less 12 for slot 2, and the source address; $AA ends the list early.
; Does what $455A-$4642 do: the VDP address written once, the tiles in order, ($C95B) past
; each entry, and at the end of B entries ($C945) + $20 an entry back into ($C945) (not when
; the list ends early). Keeps IX, IY and the alternate registers; returns HL = the count
; address, B = 0, as the game's code leaves them.
stream: ld (.ix),ix
        ld (.iy),iy
        ld hl,($C945)
        ld (.hv),hl
        ld (.va),hl
        ld a,b
        ld (.n),a
        di
        ld a,l
        rst $00
        db $05                  ; OUT ($BF),A: the address, low byte
        ld a,h
        set 6,a
        rst $00
        db $05                  ; OUT ($BF),A: the address, high byte and the write code
        ei
.next:  ld hl,($C95B)
        ld a,(hl)
        cp $AA
        jp z,.out               ; the list ends: ($C945) stays
        inc hl
        ld c,a
        ld a,(hl)
        inc hl
        add a,$0C
        rst $00
        db $13, 0               ; LD ($FFFF),A: the tile's bank to slot 2
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld ($C95B),hl
        ex de,hl                ; HL = the source
        ld a,c
        or a
        jp nz,.flip
        ld b,32
        ld de,32
        xor a                   ; the source as the game sees it
        jp .write
.flip:  ld d,$C4
        ld bc,.buf
        rept 32
        ld e,(hl)
        ld a,(de)
        inc l
        ld (bc),a
        inc bc
        endr
        ld hl,.buf
        ld b,32
        ld de,32
        ld a,1                  ; the source as mapped now: the buffer in this page
.write: push de
        pop ix
        push de
        pop iy
        ld c,1
        ld de,(.va)
        call jt_vwrite
        add iy,de               ; the VRAM address after the tile
        ld (.va),iy
        ld hl,(.hv)
        ld de,$20
        add hl,de
        ld (.hv),hl
        ld a,(.n)
        dec a
        ld (.n),a
        jp nz,.next
        ld ($C945),hl
.out:   ld hl,(.hv)
        ld b,0
        ld ix,(.ix)
        ld iy,(.iy)
        ret
.ix:    dw 0
.iy:    dw 0
.hv:    dw 0
.va:    dw 0
.n:     db 0
.buf:   ds 32
endpage
site 0000D   ; OUT ($3E),A
site 00011   ; OUT ($3F),A
site 00039   ; IN A,($BF)
site 0026D   ; IN A,($DD)
site 00351   ; IN A,($DD)
site 00B47   ; OUT ($BF),A
site 00B4C   ; OUT ($BF),A
site 00B54   ; OUTI
site 00BCD   ; OUT ($BE),A
site 00BD4   ; OUT ($BE),A
site 00BDB   ; OUT ($BE),A
site 00BE2   ; OUT ($BE),A
site 00BF1   ; OUT ($BE),A
site 00BF8   ; OUT ($BE),A
site 00BFF   ; OUT ($BE),A
site 00C06   ; OUT ($BE),A
site 00CB8   ; OUT ($BE),A
site 00CC8   ; OUT ($BE),A
site 00CDB   ; OUT ($BE),A
site 00CF4   ; OUT ($BE),A
site 00D2E   ; OUT ($BE),A
site 00D3E   ; OUT ($BE),A
site 00D51   ; OUT ($BE),A
site 00D62   ; OUT ($BE),A
site 00EFB   ; OUT ($BF),A
site 00F02   ; OUT ($BF),A
site 00F0A   ; OUT ($BE),A
site 00F12   ; OUT ($BE),A
site 00F24   ; OUT ($BF),A
site 00F2B   ; OUT ($BF),A
site 00F33   ; OUT ($BE),A
site 00F3B   ; OUT ($BE),A
site 00F54   ; OUT ($BF),A
site 00F5B   ; OUT ($BF),A
site 00F63   ; OUT ($BE),A
site 00F6B   ; OUT ($BE),A
site 00F7D   ; OUT ($BF),A
site 00F85   ; OUT ($BF),A
site 00F8D   ; OUT ($BE),A
site 00F95   ; OUT ($BE),A
site 01014   ; OUT ($BF),A
site 0101B   ; OUT ($BF),A
site 0102F   ; OUT ($BE),A
site 01037   ; OUT ($BE),A
site 01045   ; OUT ($BF),A
site 0104C   ; OUT ($BF),A
site 01054   ; OUT ($BE),A
site 0105C   ; OUT ($BE),A
site 0106A   ; OUT ($BF),A
site 01071   ; OUT ($BF),A
site 01084   ; OUT ($BE),A
site 0108C   ; OUT ($BE),A
site 0109C   ; OUT ($BF),A
site 010A3   ; OUT ($BF),A
site 010AB   ; OUT ($BE),A
site 010B3   ; OUT ($BE),A
site 010C1   ; OUT ($BF),A
site 010C8   ; OUT ($BF),A
site 0112E   ; OUT ($BF),A
site 01138   ; OUT ($BF),A
site 01141   ; OUT ($BE),A
site 01149   ; OUT ($BE),A
site 01155   ; OUT ($BE),A
site 01161   ; IN A,($BE)
site 011B1   ; OUT ($BF),A
site 011BA   ; OUT ($BF),A
site 012A4   ; OUT ($BF),A
site 012AC   ; OUT ($BF),A
site 012B6   ; OUT ($BE),A
site 01311   ; OUT ($BF),A
site 01315   ; OUT ($BF),A
site 01319   ; OUT ($BE),A
site 013A5   ; OUT ($BE),A
site 01655   ; OUT ($3F),A
site 01657   ; IN A,($DC)
site 016D5   ; OTIR
site 016E5   ; IN A,($DC)
site 0174C   ; OUT ($3F),A
site 0174E   ; IN A,($DC)
site 01760   ; IN A,($DD)
site 01773   ; IN A,($DC)
site 01839   ; OUT ($BE),A
site 01844   ; OUT ($BE),A
site 01A8E   ; OUT ($BE),A
site 01A94   ; OUT ($BE),A
site 01ACD   ; OUT ($BE),A
site 01AD6   ; OUT ($BE),A
site 01ADD   ; OUT ($BE),A
site 01AED   ; OUT ($BE),A
site 01AF6   ; OUT ($BE),A
site 01B3C   ; OUT ($BE),A
site 01B44   ; OUT ($BE),A
site 023B3   ; OUT ($BE),A
site 023BB   ; OUT ($BE),A
site 023CB   ; OUT ($BE),A
site 023D3   ; OUT ($BE),A
site 0241B   ; IN A,($DD)
site 024DA   ; OUT ($BE),A
site 024E2   ; OUT ($BE),A
site 024E8   ; OUT ($BE),A
site 024F0   ; OUT ($BE),A
site 04560   ; OUT (C),L
site 04565   ; OUT ($BF),A
site 0458B   ; OUTI
site 0459C   ; OUT ($BE),A
site 045A1   ; OUT ($BE),A
site 045A6   ; OUT ($BE),A
site 045AB   ; OUT ($BE),A
site 045B0   ; OUT ($BE),A
site 045B5   ; OUT ($BE),A
site 045BA   ; OUT ($BE),A
site 045BF   ; OUT ($BE),A
site 045C4   ; OUT ($BE),A
site 045C9   ; OUT ($BE),A
site 045CE   ; OUT ($BE),A
site 045D3   ; OUT ($BE),A
site 045D8   ; OUT ($BE),A
site 045DD   ; OUT ($BE),A
site 045E2   ; OUT ($BE),A
site 045E7   ; OUT ($BE),A
site 045EC   ; OUT ($BE),A
site 045F1   ; OUT ($BE),A
site 045F6   ; OUT ($BE),A
site 045FB   ; OUT ($BE),A
site 04600   ; OUT ($BE),A
site 04605   ; OUT ($BE),A
site 0460A   ; OUT ($BE),A
site 0460F   ; OUT ($BE),A
site 04614   ; OUT ($BE),A
site 04619   ; OUT ($BE),A
site 0461E   ; OUT ($BE),A
site 04623   ; OUT ($BE),A
site 04628   ; OUT ($BE),A
site 0462D   ; OUT ($BE),A
site 04632   ; OUT ($BE),A
site 04637   ; OUT ($BE),A
site 04645   ; OUT ($BF),A
site 04649   ; OUT ($BF),A
site 04652   ; OUTI
site 04654   ; OUTI
site 04656   ; OUTI
site 04658   ; OUTI
site 0465A   ; OUTI
site 0465C   ; OUTI
site 0465E   ; OUTI
site 04660   ; OUTI
site 04662   ; OUTI
site 04664   ; OUTI
site 04666   ; OUTI
site 04668   ; OUTI
site 0466A   ; OUTI
site 0466C   ; OUTI
site 0466E   ; OUTI
site 04670   ; OUTI
site 04672   ; OUTI
site 04674   ; OUTI
site 04676   ; OUTI
site 04678   ; OUTI
site 0467A   ; OUTI
site 0467C   ; OUTI
site 0467E   ; OUTI
site 04680   ; OUTI
site 04682   ; OUTI
site 04684   ; OUTI
site 04686   ; OUTI
site 04688   ; OUTI
site 0468A   ; OUTI
site 0468C   ; OUTI
site 0468E   ; OUTI
site 04690   ; OUTI
site 04692   ; OUTI
site 04694   ; OUTI
site 04696   ; OUTI
site 04698   ; OUTI
site 0469A   ; OUTI
site 0469C   ; OUTI
site 0469E   ; OUTI
site 046A0   ; OUTI
site 046A2   ; OUTI
site 046A4   ; OUTI
site 046A6   ; OUTI
site 046A8   ; OUTI
site 046AA   ; OUTI
site 046AC   ; OUTI
site 046AE   ; OUTI
site 046B0   ; OUTI
site 046B2   ; OUTI
site 046B4   ; OUTI
site 046B6   ; OUTI
site 046B8   ; OUTI
site 046BA   ; OUTI
site 046BC   ; OUTI
site 046BE   ; OUTI
site 046C0   ; OUTI
site 046C2   ; OUTI
site 046C4   ; OUTI
site 046C6   ; OUTI
site 046C8   ; OUTI
site 046CA   ; OUTI
site 046CC   ; OUTI
site 046CE   ; OUTI
site 046D0   ; OUTI
site 046D3   ; OUT ($BF),A
site 046D6   ; OUT ($BF),A
site 046D9   ; OUTI
site 046DB   ; OUTI
site 046DD   ; OUTI
site 046DF   ; OUTI
site 046E1   ; OUTI
site 046E3   ; OUTI
site 046E5   ; OUTI
site 046E7   ; OUTI
site 046E9   ; OUTI
site 046EB   ; OUTI
site 046ED   ; OUTI
site 046EF   ; OUTI
site 046F1   ; OUTI
site 046F3   ; OUTI
site 046F5   ; OUTI
site 046F7   ; OUTI
site 046F9   ; OUTI
site 046FB   ; OUTI
site 046FD   ; OUTI
site 046FF   ; OUTI
site 04701   ; OUTI
site 04703   ; OUTI
site 04705   ; OUTI
site 04707   ; OUTI
site 04709   ; OUTI
site 0470B   ; OUTI
site 0470D   ; OUTI
site 0470F   ; OUTI
site 04711   ; OUTI
site 04713   ; OUTI
site 04715   ; OUTI
site 04717   ; OUTI
site 04719   ; OUTI
site 0471B   ; OUTI
site 0471D   ; OUTI
site 0471F   ; OUTI
site 04721   ; OUTI
site 04723   ; OUTI
site 04725   ; OUTI
site 04727   ; OUTI
site 04729   ; OUTI
site 0472B   ; OUTI
site 0472D   ; OUTI
site 0472F   ; OUTI
site 04731   ; OUTI
site 04733   ; OUTI
site 04735   ; OUTI
site 04737   ; OUTI
site 04739   ; OUTI
site 0473B   ; OUTI
site 0473D   ; OUTI
site 0473F   ; OUTI
site 04741   ; OUTI
site 04743   ; OUTI
site 04745   ; OUTI
site 04747   ; OUTI
site 04749   ; OUTI
site 0474B   ; OUTI
site 0474D   ; OUTI
site 0474F   ; OUTI
site 04751   ; OUTI
site 04753   ; OUTI
site 04755   ; OUTI
site 04757   ; OUTI
site 04759   ; OUTI
site 0475B   ; OUTI
site 0475D   ; OUTI
site 0475F   ; OUTI
site 04761   ; OUTI
site 04763   ; OUTI
site 04765   ; OUTI
site 04767   ; OUTI
site 04769   ; OUTI
site 0476B   ; OUTI
site 0476D   ; OUTI
site 0476F   ; OUTI
site 04771   ; OUTI
site 04773   ; OUTI
site 04775   ; OUTI
site 04777   ; OUTI
site 04779   ; OUTI
site 0477B   ; OUTI
site 0477D   ; OUTI
site 0477F   ; OUTI
site 04781   ; OUTI
site 04783   ; OUTI
site 04785   ; OUTI
site 04787   ; OUTI
site 04789   ; OUTI
site 0478B   ; OUTI
site 0478D   ; OUTI
site 0478F   ; OUTI
site 04791   ; OUTI
site 04793   ; OUTI
site 04795   ; OUTI
site 04797   ; OUTI
site 04799   ; OUTI
site 0479B   ; OUTI
site 0479D   ; OUTI
site 0479F   ; OUTI
site 047A1   ; OUTI
site 047A3   ; OUTI
site 047A5   ; OUTI
site 047A7   ; OUTI
site 047A9   ; OUTI
site 047AB   ; OUTI
site 047AD   ; OUTI
site 047AF   ; OUTI
site 047B1   ; OUTI
site 047B3   ; OUTI
site 047B5   ; OUTI
site 047B7   ; OUTI
site 047B9   ; OUTI
site 047BB   ; OUTI
site 047BD   ; OUTI
site 047BF   ; OUTI
site 047C1   ; OUTI
site 047C3   ; OUTI
site 047C5   ; OUTI
site 047C7   ; OUTI
site 047C9   ; OUTI
site 047CB   ; OUTI
site 047CD   ; OUTI
site 047CF   ; OUTI
site 047D1   ; OUTI
site 047D3   ; OUTI
site 047D5   ; OUTI
site 047D7   ; OUTI
site 06AFE   ; OUT ($BE),A
site 06B03   ; OUT ($BE),A
site 06B08   ; OUT ($BE),A
site 06B0D   ; OUT ($BE),A
site 06B22   ; OUT ($BE),A
site 06B54   ; OUT ($BE),A
site 07D0D   ; OUT ($7F),A
site 07D29   ; OUT ($7F),A
site 07D48   ; OUT ($7F),A
site 07D60   ; OUT ($7F),A
site 07D6D   ; OUT ($7F),A
site 07D78   ; OUT ($7F),A
site 07D87   ; OUT ($7F),A
mapst 00407   ; LD ($FFFF),A
mapst 00B32   ; LD ($FFFF),A
mapst 00B81   ; LD ($FFFF),A
mapst 00B97   ; LD ($FFFF),A
mapst 00E92   ; LD ($FFFF),A
mapst 00FAE   ; LD ($FFFF),A
mapst 0116E   ; LD ($FFFF),A
mapst 013BA   ; LD ($FFFF),A
mapst 01434   ; LD ($FFFF),A
mapst 015E7   ; LD ($FFFF),A
mapst 0162E   ; LD ($FFFF),A
mapst 02378   ; LD ($FFFF),A
mapst 02459   ; LD ($FFFF),A
mapst 04579   ; LD ($FFFF),A
mapst 06A65   ; LD ($FFFF),A
mapst 06A96   ; LD ($FFFF),A
mapst 06ACA   ; LD ($FFFF),A
mapst 06B35   ; LD ($FFFF),A

# Indiana Jones and the Last Crusade (Europe, Brazil).cht, "Infinite Lives": RAM $C987 is
# the spare lives; held at 9, a death no longer costs one
poke "Infinite lives"
ar 00C9-8709
endpoke

# Indiana Jones and the Last Crusade (Europe, Brazil).cht, "Infinite Time": RAM $CBBA is
# the ones digit of the clock; held at 9 the clock never counts down, so it never runs out
poke "Infinite time"
ar 00CB-BA09
endpoke

# Indiana Jones and the Last Crusade (Europe, Brazil).cht, "Infinite Whips": RAM $C973 is
# the whip count shown in the status bar; held at 9, a whip crack no longer spends one
poke "Infinite whips"
ar 00C9-7309
endpoke

# Indiana Jones and the Last Crusade (Europe, Brazil).cht, "Infinite Credits (Continues)":
# RAM $C9C0 is the credits left; held at 2, every game over offers the continue screen
poke "Infinite continues"
ar 00C9-C002
endpoke

# Indiana Jones and the Last Crusade (Europe, Brazil).cht, "Invincibility": two cart bytes
# change from RET NC ($D0) to RET ($C9); enemy hits no longer drain the health. Running
# out of time and some other damage still kill
poke "Invincibility"
gg C9A-C5A-A29
gg C91-E79-A29
endpoke
