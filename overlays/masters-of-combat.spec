# Masters of Combat (Europe, Brazil) (En), CRC32 93141463, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (60 s and 600 s
# of random input) and entry points from the game state table at $12CD (56 entries of
# bank, address) and the fighters' move tables at $34EE (5 fighters, 14 moves each).
# Decisions:
# - No free RST vector ($0008, $0018, $0020, $0028 and $0030 are the game's, $0010 is
#   inside $0008's code), so $0000 is the io vector. The game never runs RST $00. The
#   reset button code at $0387 (the frame handler reads port $DD bit 4) ends with
#   JP $0000; it jumps to $0003, the game's start after DI and IM 1.
# - The game builds 128 OUTIs and a RET at $DE00 (at $02DE) and copies the sprite table
#   with CALL or JP to $DE00, $DE80 and $DEC0 (128, 64 and 32 bytes) at $0563-$0594.
#   The cart holds the same 128 OUTIs and RET at $06D7-$07D7, and the game calls into
#   it itself (CALL $0757 at $05AA). The six transfers go to $06D7, $0757 and $0797, and the
#   OUTI run is patched as sites.
# - Code is in banks 0, 1 and 15 (the sound driver) only. The byte patterns in banks
#   2-14 are graphics and data (verdict false).
# - $0C5A-$0C81 loads a list of blocks into VRAM; nothing in the cart names $0C5A, and
#   no recording ran it. Its two mapper stores are patched anyway.
# - Page 0 `tiles` does the fighter tile writer $0A01 (below). Through the runtime's traps
#   the Next took longer over a fight step than a Master System.
# - Step rate: $0315 times a frame at power-on and sets $C417 = $FF on a PAL Master System.
#   With $C417 = 0 (NTSC), $3161 adds a frame wait every fifth half-step, so both machines
#   make 25 steps a second. The Next's fast CPU always gives $FF, the PAL value, which is
#   right for `hz 50`.
name Masters of Combat
cart 93141463
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
start 0003
site 0001A   ; OUT (C),L
site 0001C   ; OUT (C),H
site 0003A   ; IN A,($BF)
site 00205   ; IN A,(C)
site 0020C   ; OUT ($BF),A
site 00210   ; OUT ($BF),A
site 00284   ; OUT ($3F),A
site 00286   ; IN A,($DD)
site 00290   ; OUT ($3F),A
site 00292   ; IN A,($DD)
site 00301   ; OUT ($3E),A
site 00304   ; OUT ($F2),A
site 0030C   ; OUT ($3E),A
site 00310   ; OUT ($3F),A
site 00318   ; IN A,($BF)
site 0031A   ; IN A,($BF)
site 00326   ; IN A,($BF)
site 00390   ; IN A,($DD)
site 004AD   ; OUT ($BF),A
site 004B1   ; OUT ($BF),A
site 004B4   ; IN A,($BF)
site 004C5   ; OUT ($BF),A
site 004C9   ; OUT ($BF),A
site 004CC   ; IN A,($DC)
site 004E9   ; IN A,($DD)
site 0050E   ; IN A,($BF)
site 00519   ; OUT ($BF),A
site 0051C   ; OUT ($BF),A
site 00529   ; OUT ($BE),A
site 006AB   ; OUTI
site 006AD   ; OUTI
site 006BA   ; OTIR
site 006BF   ; OUTI
site 006C1   ; OUTI
site 006CE   ; OTIR
site 00797   ; OUTI
site 00799   ; OUTI
site 0079B   ; OUTI
site 0079D   ; OUTI
site 0079F   ; OUTI
site 007A1   ; OUTI
site 007A3   ; OUTI
site 007A5   ; OUTI
site 007A7   ; OUTI
site 007A9   ; OUTI
site 007AB   ; OUTI
site 007AD   ; OUTI
site 007AF   ; OUTI
site 007B1   ; OUTI
site 007B3   ; OUTI
site 007B5   ; OUTI
site 007B7   ; OUTI
site 007B9   ; OUTI
site 007BB   ; OUTI
site 007BD   ; OUTI
site 007BF   ; OUTI
site 007C1   ; OUTI
site 007C3   ; OUTI
site 007C5   ; OUTI
site 007C7   ; OUTI
site 007C9   ; OUTI
site 007CB   ; OUTI
site 007CD   ; OUTI
site 007CF   ; OUTI
site 007D1   ; OUTI
site 007D3   ; OUTI
site 007D5   ; OUTI
site 007DE   ; OTIR
site 007F0   ; OUT ($BE),A
site 007F6   ; OUT ($BE),A
site 0080A   ; OUT ($BE),A
site 0080D   ; OUT ($BE),A
site 00822   ; OUTI
site 00827   ; OUT ($BE),A
site 00839   ; OUT (C),E
site 0083B   ; OUT (C),D
site 0084C   ; OUT (C),E
site 00852   ; OUT (C),D
site 00872   ; OUT ($BE),A
site 00875   ; OUT ($BE),A
site 0089E   ; OUT ($BE),A
site 008A2   ; OUT ($BE),A
site 008A6   ; OUT ($BE),A
site 008AA   ; OUT ($BE),A
site 008BB   ; OUT ($BE),A
site 008BF   ; OUT ($BE),A
site 008C4   ; OUT ($BE),A
site 008C8   ; OUT ($BE),A
site 00A0F   ; OUT (C),L
site 00A11   ; OUT (C),H
site 00A47   ; OUT ($BE),A
site 00A4E   ; OUT ($BE),A
site 00A55   ; OUT ($BE),A
site 00A5C   ; OUT ($BE),A
site 00A7D   ; OUT ($BE),A
site 00A84   ; OUT ($BE),A
site 00A8B   ; OUT ($BE),A
site 00A92   ; OUT ($BE),A
site 00AC5   ; OUT ($BE),A
site 00ACC   ; OUT ($BE),A
site 00AD3   ; OUT ($BE),A
site 00ADA   ; OUT ($BE),A
site 00AFD   ; OUT ($BE),A
site 00B06   ; OUT ($BE),A
site 00B0D   ; OUT ($BE),A
site 00B14   ; OUT ($BE),A
site 00B41   ; OUT ($BE),A
site 00B48   ; OUT ($BE),A
site 00B4F   ; OUT ($BE),A
site 00B59   ; OUT ($BE),A
site 00B80   ; OUT ($BE),A
site 00B87   ; OUT ($BE),A
site 00B8E   ; OUT ($BE),A
site 00B96   ; OUT ($BE),A
site 00BCF   ; OUT ($BE),A
site 00BD6   ; OUT ($BE),A
site 00BDD   ; OUT ($BE),A
site 00BE7   ; OUT ($BE),A
site 00C11   ; OUT ($BE),A
site 00C1A   ; OUT ($BE),A
site 00C21   ; OUT ($BE),A
site 00C2A   ; OUT ($BE),A
site 013B8   ; IN A,(C)
site 013BE   ; IN A,(C)
site 013FB   ; OUT (C),A
site 01401   ; IN A,(C)
site 01460   ; OUT (C),E
site 01462   ; OUT (C),D
site 014AE   ; OUT ($BE),A
site 014F7   ; OUT ($BE),A
site 01518   ; OUT ($BE),A
site 01FC7   ; OUT (C),A
site 01FCD   ; OUT (C),A
site 01FE3   ; OUT (C),A
site 01FE9   ; OUT (C),A
site 02B7F   ; OUT ($BE),A
site 02B83   ; OUT ($BE),A
site 02CC3   ; OUT ($BE),A
site 02CC6   ; OUT ($BE),A
site 03446   ; OUT ($BF),A
site 0344A   ; OUT ($BF),A
site 03FF6   ; IN A,($DC)
site 04030   ; IN A,($DC)
site 04034   ; IN A,($DD)
site 04180   ; OUT (C),A
site 04187   ; OUT (C),B
site 0418B   ; OUT (C),A
site 04192   ; OUT (C),A
site 04198   ; OUT (C),B
site 041C8   ; OUT (C),A
site 041CD   ; OUT (C),A
site 041D4   ; OUT (C),A
site 041D9   ; OUT (C),A
site 041E0   ; OUT (C),A
site 041E5   ; OUT (C),A
site 042EA   ; OUT (C),A
site 042EF   ; OUT (C),A
site 042F4   ; OUT (C),A
site 042FA   ; OUT (C),A
site 04331   ; OUT (C),A
site 04335   ; OUT (C),H
site 0433C   ; OUT (C),A
site 04340   ; OUT (C),L
site 0434E   ; OUT (C),A
site 04352   ; OUT (C),H
site 04370   ; OUT (C),A
site 04374   ; OUT (C),H
site 04501   ; OUT (C),A
site 04506   ; OUT (C),A
site 0450C   ; OUT (C),A
site 04513   ; OUT (C),A
site 04E22   ; OUTI
site 04E24   ; OUTI
site 04E26   ; OUTI
site 04E28   ; OUTI
site 3C1FA   ; OUT ($7F),A
site 3C452   ; OTIR
site 3C56A   ; OUT ($7F),A
site 3C574   ; OUT ($7F),A
site 3C591   ; OUT ($7F),A
site 3C6B9   ; OUT ($7F),A
site 3C74D   ; OUT ($7F),A
site 3C7FA   ; OUT ($7F),A
site 3C803   ; OUT ($7F),A
site 3C813   ; OUT ($7F),A
site 3C893   ; OUT ($7F),A
mapldk 00212   # LD HL,$FFFC; LD (HL),$00
maphl 00218   # LD (HL),$00, HL = $FFFD
maphl 0021B   # LD (HL),$01, HL = $FFFE
maphl 0021E   # LD (HL),$02, HL = $FFFF
mapst 00239   ; LD ($FFFF),A
mapst 003A8   ; LD ($FFFF),A
mapst 00487   ; LD ($FFFF),A
mapst 008E0   ; LD ($FFFF),A
mapst 008F4   ; LD ($FFFF),A
mapst 00905   ; LD ($FFFF),A
mapst 00915   ; LD ($FFFF),A
mapst 00A1E   ; LD ($FFFF),A
mapst 00A37   ; LD ($FFFF),A
mapst 00A41   ; LD ($FFFF),A
mapst 00A6D   ; LD ($FFFF),A
mapst 00A77   ; LD ($FFFF),A
mapst 00AB1   ; LD ($FFFF),A
mapst 00ABB   ; LD ($FFFF),A
mapst 00AE9   ; LD ($FFFF),A
mapst 00AF3   ; LD ($FFFF),A
mapst 00B2B   ; LD ($FFFF),A
mapst 00B3B   ; LD ($FFFF),A
mapst 00B6A   ; LD ($FFFF),A
mapst 00B7A   ; LD ($FFFF),A
mapst 00BB5   ; LD ($FFFF),A
mapst 00BC5   ; LD ($FFFF),A
mapst 00BF7   ; LD ($FFFF),A
mapst 00C07   ; LD ($FFFF),A
mapst 00C39   ; LD ($FFFF),A
mapst 00C40   ; LD ($FFFF),A
mapst 0143D   ; LD ($FFFF),A
mapst 0144D   ; LD ($FFFF),A
mapst 01AC0   ; LD ($FFFF),A
mapst 01B00   ; LD ($FFFF),A
mapst 01B76   ; LD ($FFFF),A
mapst 01BD4   ; LD ($FFFF),A
mapst 01D3C   ; LD ($FFFF),A
mapst 01D5F   ; LD ($FFFF),A
mapst 01E01   ; LD ($FFFF),A
mapst 01E17   ; LD ($FFFF),A
mapst 01E7C   ; LD ($FFFF),A
mapst 01E8D   ; LD ($FFFF),A
mapst 02130   ; LD ($FFFF),A
mapst 0214D   ; LD ($FFFF),A
mapst 0234C   ; LD ($FFFF),A
mapst 0235C   ; LD ($FFFF),A
mapst 0250F   ; LD ($FFFF),A
mapst 025CE   ; LD ($FFFF),A
mapst 025DA   ; LD ($FFFF),A
mapst 02945   ; LD ($FFFF),A
mapst 02959   ; LD ($FFFF),A
mapst 029A6   ; LD ($FFFF),A
mapst 029B9   ; LD ($FFFF),A
mapst 02ABD   ; LD ($FFFF),A
mapst 02ACD   ; LD ($FFFF),A
mapst 02B94   ; LD ($FFFF),A
mapst 02BA4   ; LD ($FFFF),A
mapst 02BEE   ; LD ($FFFF),A
mapst 02BFB   ; LD ($FFFF),A
mapst 02C0E   ; LD ($FFFF),A
mapst 02C52   ; LD ($FFFF),A
mapst 02C78   ; LD ($FFFF),A
mapst 02C8A   ; LD ($FFFF),A
mapst 02E7A   ; LD ($FFFF),A
mapst 02E8C   ; LD ($FFFF),A
mapst 02F1E   ; LD ($FFFF),A
mapst 02F30   ; LD ($FFFF),A
mapst 04467   ; LD ($FFFF),A
mapst 0448D   ; LD ($FFFF),A
mapst 044AC   ; LD ($FFFF),A
mapst 045B8   ; LD ($FFFF),A
mapst 045C8   ; LD ($FFFF),A
mapst 04974   ; LD ($FFFF),A
mapst 04999   ; LD ($FFFF),A
mapst 04E8A   ; LD ($FFFF),A
mapst 04E91   ; LD ($FFFF),A
mapst 04F5A   ; LD ($FFFF),A
mapst 04F5F   ; LD ($FFFF),A
mapst 04FBE   ; LD ($FFFF),A
mapst 04FC3   ; LD ($FFFF),A
mapst 04FEA   ; LD ($FFFF),A
mapst 04FF1   ; LD ($FFFF),A
mapst 05028   ; LD ($FFFF),A
mapst 0502D   ; LD ($FFFF),A
mapst 05049   ; LD ($FFFF),A
mapst 0505E   ; LD ($FFFF),A
mapst 06F33   ; LD ($FFFF),A
mapst 06F45   ; LD ($FFFF),A
mapst 072E1   ; LD ($FFFF),A
mapst 072FB   ; LD ($FFFF),A
mapst 00C61   # LD ($FFFF),A; after LD A,(HL); 32 bytes of valid code before it
mapst 00C7C   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
site 006D7   ; OUTI, the ROM copy of the RAM OUTI run
site 006D9   ; OUTI, the ROM copy of the RAM OUTI run
site 006DB   ; OUTI, the ROM copy of the RAM OUTI run
site 006DD   ; OUTI, the ROM copy of the RAM OUTI run
site 006DF   ; OUTI, the ROM copy of the RAM OUTI run
site 006E1   ; OUTI, the ROM copy of the RAM OUTI run
site 006E3   ; OUTI, the ROM copy of the RAM OUTI run
site 006E5   ; OUTI, the ROM copy of the RAM OUTI run
site 006E7   ; OUTI, the ROM copy of the RAM OUTI run
site 006E9   ; OUTI, the ROM copy of the RAM OUTI run
site 006EB   ; OUTI, the ROM copy of the RAM OUTI run
site 006ED   ; OUTI, the ROM copy of the RAM OUTI run
site 006EF   ; OUTI, the ROM copy of the RAM OUTI run
site 006F1   ; OUTI, the ROM copy of the RAM OUTI run
site 006F3   ; OUTI, the ROM copy of the RAM OUTI run
site 006F5   ; OUTI, the ROM copy of the RAM OUTI run
site 006F7   ; OUTI, the ROM copy of the RAM OUTI run
site 006F9   ; OUTI, the ROM copy of the RAM OUTI run
site 006FB   ; OUTI, the ROM copy of the RAM OUTI run
site 006FD   ; OUTI, the ROM copy of the RAM OUTI run
site 006FF   ; OUTI, the ROM copy of the RAM OUTI run
site 00701   ; OUTI, the ROM copy of the RAM OUTI run
site 00703   ; OUTI, the ROM copy of the RAM OUTI run
site 00705   ; OUTI, the ROM copy of the RAM OUTI run
site 00707   ; OUTI, the ROM copy of the RAM OUTI run
site 00709   ; OUTI, the ROM copy of the RAM OUTI run
site 0070B   ; OUTI, the ROM copy of the RAM OUTI run
site 0070D   ; OUTI, the ROM copy of the RAM OUTI run
site 0070F   ; OUTI, the ROM copy of the RAM OUTI run
site 00711   ; OUTI, the ROM copy of the RAM OUTI run
site 00713   ; OUTI, the ROM copy of the RAM OUTI run
site 00715   ; OUTI, the ROM copy of the RAM OUTI run
site 00717   ; OUTI, the ROM copy of the RAM OUTI run
site 00719   ; OUTI, the ROM copy of the RAM OUTI run
site 0071B   ; OUTI, the ROM copy of the RAM OUTI run
site 0071D   ; OUTI, the ROM copy of the RAM OUTI run
site 0071F   ; OUTI, the ROM copy of the RAM OUTI run
site 00721   ; OUTI, the ROM copy of the RAM OUTI run
site 00723   ; OUTI, the ROM copy of the RAM OUTI run
site 00725   ; OUTI, the ROM copy of the RAM OUTI run
site 00727   ; OUTI, the ROM copy of the RAM OUTI run
site 00729   ; OUTI, the ROM copy of the RAM OUTI run
site 0072B   ; OUTI, the ROM copy of the RAM OUTI run
site 0072D   ; OUTI, the ROM copy of the RAM OUTI run
site 0072F   ; OUTI, the ROM copy of the RAM OUTI run
site 00731   ; OUTI, the ROM copy of the RAM OUTI run
site 00733   ; OUTI, the ROM copy of the RAM OUTI run
site 00735   ; OUTI, the ROM copy of the RAM OUTI run
site 00737   ; OUTI, the ROM copy of the RAM OUTI run
site 00739   ; OUTI, the ROM copy of the RAM OUTI run
site 0073B   ; OUTI, the ROM copy of the RAM OUTI run
site 0073D   ; OUTI, the ROM copy of the RAM OUTI run
site 0073F   ; OUTI, the ROM copy of the RAM OUTI run
site 00741   ; OUTI, the ROM copy of the RAM OUTI run
site 00743   ; OUTI, the ROM copy of the RAM OUTI run
site 00745   ; OUTI, the ROM copy of the RAM OUTI run
site 00747   ; OUTI, the ROM copy of the RAM OUTI run
site 00749   ; OUTI, the ROM copy of the RAM OUTI run
site 0074B   ; OUTI, the ROM copy of the RAM OUTI run
site 0074D   ; OUTI, the ROM copy of the RAM OUTI run
site 0074F   ; OUTI, the ROM copy of the RAM OUTI run
site 00751   ; OUTI, the ROM copy of the RAM OUTI run
site 00753   ; OUTI, the ROM copy of the RAM OUTI run
site 00755   ; OUTI, the ROM copy of the RAM OUTI run
site 00757   ; OUTI, the ROM copy of the RAM OUTI run
site 00759   ; OUTI, the ROM copy of the RAM OUTI run
site 0075B   ; OUTI, the ROM copy of the RAM OUTI run
site 0075D   ; OUTI, the ROM copy of the RAM OUTI run
site 0075F   ; OUTI, the ROM copy of the RAM OUTI run
site 00761   ; OUTI, the ROM copy of the RAM OUTI run
site 00763   ; OUTI, the ROM copy of the RAM OUTI run
site 00765   ; OUTI, the ROM copy of the RAM OUTI run
site 00767   ; OUTI, the ROM copy of the RAM OUTI run
site 00769   ; OUTI, the ROM copy of the RAM OUTI run
site 0076B   ; OUTI, the ROM copy of the RAM OUTI run
site 0076D   ; OUTI, the ROM copy of the RAM OUTI run
site 0076F   ; OUTI, the ROM copy of the RAM OUTI run
site 00771   ; OUTI, the ROM copy of the RAM OUTI run
site 00773   ; OUTI, the ROM copy of the RAM OUTI run
site 00775   ; OUTI, the ROM copy of the RAM OUTI run
site 00777   ; OUTI, the ROM copy of the RAM OUTI run
site 00779   ; OUTI, the ROM copy of the RAM OUTI run
site 0077B   ; OUTI, the ROM copy of the RAM OUTI run
site 0077D   ; OUTI, the ROM copy of the RAM OUTI run
site 0077F   ; OUTI, the ROM copy of the RAM OUTI run
site 00781   ; OUTI, the ROM copy of the RAM OUTI run
site 00783   ; OUTI, the ROM copy of the RAM OUTI run
site 00785   ; OUTI, the ROM copy of the RAM OUTI run
site 00787   ; OUTI, the ROM copy of the RAM OUTI run
site 00789   ; OUTI, the ROM copy of the RAM OUTI run
site 0078B   ; OUTI, the ROM copy of the RAM OUTI run
site 0078D   ; OUTI, the ROM copy of the RAM OUTI run
site 0078F   ; OUTI, the ROM copy of the RAM OUTI run
site 00791   ; OUTI, the ROM copy of the RAM OUTI run
site 00793   ; OUTI, the ROM copy of the RAM OUTI run
site 00795   ; OUTI, the ROM copy of the RAM OUTI run

asm 0038D 3          ; JP $0000 after the reset button: $0000 is the io vector
    jp $0003
endasm
asm 0056A 3          ; CALL $DE80: 64 OUTIs in RAM
    call $0757
endasm
asm 00574 3          ; JP $DE00: 128 OUTIs in RAM
    jp $06D7
endasm
asm 0057E 3          ; CALL $DEC0: 32 OUTIs in RAM
    call $0797
endasm
asm 00584 3          ; CALL $DEC0
    call $0797
endasm
asm 0058E 3          ; CALL $DE80
    call $0757
endasm
asm 00594 3          ; JP $DE80
    jp $0757
endasm

# Masters of Combat (Europe, Brazil).cht, "Infinite Health P1": RAM $C947 is the health of
# player 1, held at $88 (the bar starts at $A0); player 1 no longer loses a round to blows
poke "Infinite health"
ar 00C9-4788
endpoke

# Masters of Combat (Europe, Brazil).cht, "Infinite Time": RAM $C807 is the round clock, held
# at $63 (99); the round never ends on time
poke "Infinite time"
ar 00C8-0763
endpoke

# The fighter tile writer $0A01: B tiles of 8 rows, 3 bytes a row (planes 0-2), from the
# tile list at DE in bank (IX+$2E); each list word points at a tile in bank (IX+$2D). The
# form (IX+$2B) picks plain, flipped left to right through the bit-reverse table at $0100,
# flipped top to bottom, or both ($0A2A, $0A9E, $0B1E, $0BA2); plane 3 is 0, or plane 1 OR
# plane 2 when (IX+$2A) is not 0. Each tile was 32 VDP data writes, with two mapper stores,
# all with interrupts off: in a fight the Next took longer over a game step than a Master
# System. Page 0 `tiles` does the same writes with two mapper stores and one jt_vwrite.
asm 00A13 9          ; LD A,(IX+$2B) : LD HL,$0A22 : CALL $0016 (the form's routine)
    rst $00
    db far_io, pg_tiles, ent_tiles
endasm

page 0 tiles
; tiles: as the game's $0A13-$0A1B and the form routine it calls. In: B tiles (1-255), DE the
; tile list, IX the fighter, the VDP address set, interrupts off. The list's bank goes into
; slot 2, the list is read, then the tiles' bank goes into slot 2 (as the game leaves it) and
; every tile is converted into tbuf and written with one jt_vwrite, which leaves the VDP
; state as the game's writes would. Out: HL past the list, DE past the last tile's rows, B 0,
; IX and IY kept, interrupts off. Runtime internals used: jt_vwrite, jt_peek, vdp_addr.
tiles:  ld (g_sp),sp
        ld sp,stk_top
        push ix
        ld a,b
        ld (cnt),a
        ld a,(ix+$2B)
        and 3
        ld c,a
        ld a,(ix+$2A)
        or a
        jr z,.p3
        set 2,c
.p3:    ld a,c
        ld (mode),a
        ld a,(ix+$2E)           ; the list's bank
        rst $00
        db $13,$FF              ; LD ($FFFF),A
        ex de,hl
        ld de,lbuf
        ld a,(cnt)
        ld b,a
.ls:    call rd
        ld (de),a
        inc hl
        inc de
        call rd
        ld (de),a
        inc hl
        inc de
        djnz .ls
        push hl                 ; HL past the list, as the game leaves it
        ld a,(ix+$2D)           ; the tiles' bank
        rst $00
        db $13,$FF
        ld ix,lbuf
        ld iy,tbuf
        ld a,(cnt)
        ld b,a
.tl:    push bc
        ld l,(ix+0)
        ld h,(ix+1)
        inc ix
        inc ix
        ld a,(mode)
        bit 1,a
        ld de,3                 ; source step a row
        jr z,.nv
        ld de,21
        add hl,de
        ld de,-3                ; flipped top to bottom: row 7 first
.nv:    ld b,8
.rw:    push de
        call rd
        call flip
        ld (iy+0),a
        inc hl
        call rd
        call flip
        ld (iy+1),a
        ld c,a
        inc hl
        call rd
        call flip
        ld (iy+2),a
        ld e,a
        ld a,(mode)
        and 4
        jr z,.z3
        ld a,e
        or c
.z3:    ld (iy+3),a
        dec hl
        dec hl
        pop de
        add hl,de
        ld de,4
        add iy,de
        ld de,3
        ld a,(mode)
        bit 1,a
        jr z,.nv2
        ld de,-3
.nv2:   djnz .rw
        pop bc
        djnz .tl
        ex de,hl                ; DE past the last tile's rows
        ld hl,tbuf
        ld de,(vdp_addr)
        ld a,(cnt)
        ld c,a
        ld b,32
        ld ix,32
        ld iy,32
        ld a,1                  ; the source as mapped now: this page
        call jt_vwrite
        pop hl                  ; past the list
        ld b,0
        pop ix
        ld sp,(g_sp)
        ret
; rd: A = the game's byte at HL (jt_peek for $2000-$3FFF, where this page is).
rd:     ld a,h
        and $E0
        cp $20
        jp z,jt_peek
        ld a,(hl)
        ret
; flip: with the left-to-right form, A through the game's bit-reverse table at $0100.
flip:   push hl
        ld l,a
        ld a,(mode)
        rra
        ld a,l
        jr nc,.n
        ld h,$01
        ld a,(hl)
.n:     pop hl
        ret
g_sp:   dw 0
cnt:    db 0
mode:   db 0
stk:    ds 64
stk_top:
lbuf:   ds 512
tbuf:   ds 32*128               ; B is at most 128 ($1242, $126B)
endpage
