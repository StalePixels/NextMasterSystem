# OutRun Europa (Europe, Brazil) (En), CRC32 3932ADBC, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output with two reference logs
# (scratchpad/b7-outrun-europa/reflogs/: 120 s with no input, 600 s of random input), then
# decided by hand. Every I/O and mapper site in the logs is on a scanned path.
# OutRun Europa is not built on OutRun (outrun.spec): no routine of that cart is in this one.
#
# Decisions:
# - The power-on code clears $C000-$FFEF with one LDIR ($0003-$000E). $E000-$FFEF is the RAM
#   mirror on a Master System and the runtime's page on the Next, so the clear stops at $DFFF.
#   The reference logs show no other store into the mirror.
# - $00B0-$029E of bank 0 is a development-kit debugger left in the cart (the text "SEGA DL1
#   *** PDS CONVERTER (C)1990" is at $0071). It talks to a host through the joypad port
#   ($0205, $0236) and stores into the cart area ($0116, $0200). No call, jump or table in
#   the cart names its entry $00B0 or the JP $00B0 at $0202, and no log ran it: its I/O sites
#   are not patched.
# - The routines at $28EE (fills VRAM with D for BC bytes) and $29A9 (reads the joypad of
#   player 2) have no caller in the cart and no log ran them: not patched.
# - The OUT (C),A sites at $2D8F, $2D95, $2DC7 and $2DCD (the sprite table writer) take the
#   port from C; the logs show $BE at all four.
# - $3FD5 (OUT (C),B) is in a data table at $3FC0.
# - The game step ($2D1B, reached from the main loop's CALL $133F at $0503) ends with EI; RET at
#   $2D55, so the frame interrupt that the step held off is taken at $0506 with SP $DFED: its
#   return slot is $DFEB, holding $0506. The next CALL $133F writes $0506 into $DFEB again,
#   and the runtime then holds every frame event for up to 8 frames, as if that handler still
#   ran: in play the handler ran only about every second frame and the step's wait for the
#   frame flag ($3167) took 2-6 frames. The cave at $0040 (filler) ends the step with EI; NOP;
#   RET, so the interrupt is taken at $0049, an address no CALL pushes.
# - Step rate. A step is the logic up to $2D1B, then the sprite table, the wait for a frame
#   event ($2D25), the register 2 move and the uploads. The game does not pace its steps: a
#   Master System takes as long as the work needs. In the attract demo (sg1000m3, the logic's
#   cycles at a PAL frame of 71364) a step takes 4 frames in most steps (313 of 502), 3 in 41
#   and 5 or 6 in the busy ones; with page 0 the Next takes 2 or 3. The cave at $0040 notes
#   isr_n at each step's start (oe_mark), and the cave at $004A holds the logic's end until 3
#   frame events have passed since then (oe_ready), so with the game's own wait a step takes
#   at least 4 frames.
# - Three unrolled OUTI copies cost most of the runtime's time in play, one trap for each
#   block: the hidden name table's rows 2-17 ($2C16: 16 rows of 64 bytes, the source stepping
#   128 a row), the road tiles from the RAM buffer at $C36E ($2DE8: ($C052) blocks of 32 bytes
#   to VRAM ($C04E)) and the tile list at $C053 ($2E6B: blocks of 32 bytes from a cart bank in
#   slot 2). The caves far-call page 0 (ntrows, blk32), which writes the same bytes with one
#   jt_vwrite call, then go on where the game's loops end ($2D19, $2E4B, $2F2B).
# - ntdiff: each game step writes the hidden name table, then moves register 2 to it ($2D33).
# - The interrupt handler at $3088 reads the reset button ($315C) and restarts the game
#   from $0403 when it is pressed.
name OutRun Europa
cart 3932ADBC
hz 50		; No-Intro regions Europe, Brazil
ntdiff
vector 18 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00040 10  ; filler: the step's end, as $2D52-$2D56 with a NOP before the RET
    rst $18
    db far_io, pg_oe_mark, ent_oe_mark
    call $30BD
    ei
    nop           ; the held frame interrupt is taken here, at $0049
    ret
endasm
asm 02D52 3   ; CALL $30BD (then EI; RET at $2D55)
    jp $0040
endasm
asm 0004A 15  ; filler: the step rate hold, then DI; CALL $2D57 as $2D1B
.hold:
    rst $18
    db far_io, pg_oe_ready, ent_oe_ready
    jr nc,.hold
    di
    call $2D57
    jp $2D1F
endasm
asm 02D1B 3   ; DI; CALL $2D57: the end of the step's logic
    jp $004A
endasm
asm 02C16 7   ; OUTI; CP (HL); CP (HL); OUTI; CP (HL): the first of 64 OUTIs a row, 16 rows
    rst $18
    db far_io, pg_ntrows, ent_ntrows
    jp $2D19      ; EI; RET, as after the last row
endasm
asm 02DE8 8   ; OUTI; NOP; OUTI; NOP; OUTI: the first of 32 OUTIs a block, ($C052) blocks
    rst $18
    db far_io, pg_blk32, ent_blk32
    jp $2E4B      ; as after the last block
    nop
endasm
asm 02E6B 8   ; OUTI; NOP; JP $2E71; OUTI: the first of 32 OUTIs a block, A blocks
    rst $18
    db far_io, pg_blk32, ent_blk32
    ex de,hl      ; as $2F2B-$2F2D after the last block
    jp $2E4E
endasm
asm 00003 3   ; LD BC,$3FEF: the power-on clear of $C000-$FFEF, whose $E000-$FFEF is the RAM mirror
    ld bc,$1FFF   ; $C000-$DFFF only: $E000-$FFFF is the runtime's page on the Next
endasm
site 00640   ; OUT ($BE),A
site 00645   ; OUT ($BE),A
site 0064A   ; OUT ($BE),A
site 0064F   ; OUT ($BE),A
site 02475   ; OUT ($3E),A
site 02479   ; OUT ($3F),A
site 025B7   ; OUT ($BE),A
site 025BC   ; OUT ($BE),A
site 025CE   ; OUT ($BE),A
site 02605   ; OUT ($BE),A
site 0260E   ; OUT ($BE),A
site 0283A   ; OUT (C),A
site 02840   ; OUT (C),E
site 0288E   ; OUT ($BE),A
site 02894   ; OUT ($BE),A
site 0289A   ; OUT ($BE),A
site 0289F   ; OUT ($BE),A
site 028B7   ; OUTI
site 02916   ; OUT ($BE),A
site 0292F   ; OUT ($BF),A
site 02935   ; OUT ($BF),A
site 02939   ; IN A,($DC)
site 02C1E   ; OUTI
site 02C22   ; OUTI
site 02C26   ; OUTI
site 02C2A   ; OUTI
site 02C2E   ; OUTI
site 02C32   ; OUTI
site 02C36   ; OUTI
site 02C3A   ; OUTI
site 02C3E   ; OUTI
site 02C42   ; OUTI
site 02C46   ; OUTI
site 02C4A   ; OUTI
site 02C4E   ; OUTI
site 02C52   ; OUTI
site 02C56   ; OUTI
site 02C5A   ; OUTI
site 02C5E   ; OUTI
site 02C62   ; OUTI
site 02C66   ; OUTI
site 02C6A   ; OUTI
site 02C6E   ; OUTI
site 02C72   ; OUTI
site 02C76   ; OUTI
site 02C7A   ; OUTI
site 02C7E   ; OUTI
site 02C82   ; OUTI
site 02C86   ; OUTI
site 02C8A   ; OUTI
site 02C8E   ; OUTI
site 02C92   ; OUTI
site 02C96   ; OUTI
site 02C9A   ; OUTI
site 02C9E   ; OUTI
site 02CA2   ; OUTI
site 02CA6   ; OUTI
site 02CAA   ; OUTI
site 02CAE   ; OUTI
site 02CB2   ; OUTI
site 02CB6   ; OUTI
site 02CBA   ; OUTI
site 02CBE   ; OUTI
site 02CC2   ; OUTI
site 02CC6   ; OUTI
site 02CCA   ; OUTI
site 02CCE   ; OUTI
site 02CD2   ; OUTI
site 02CD6   ; OUTI
site 02CDA   ; OUTI
site 02CDE   ; OUTI
site 02CE2   ; OUTI
site 02CE6   ; OUTI
site 02CEA   ; OUTI
site 02CEE   ; OUTI
site 02CF2   ; OUTI
site 02CF6   ; OUTI
site 02CFA   ; OUTI
site 02CFE   ; OUTI
site 02D02   ; OUTI
site 02D06   ; OUTI
site 02D0A   ; OUTI
site 02D0E   ; OUTI
site 02D12   ; OUTI
site 02D80   ; OUTD
site 02D8F   ; OUT (C),A
site 02D95   ; OUT (C),A
site 02DB4   ; OUTI
site 02DB8   ; OUTD
site 02DC7   ; OUT (C),A
site 02DCD   ; OUT (C),A
site 02DD7   ; OUT ($BF),A
site 02DDF   ; OUT ($BF),A
site 02DF1   ; OUTI
site 02DF4   ; OUTI
site 02DF7   ; OUTI
site 02DFA   ; OUTI
site 02DFD   ; OUTI
site 02E00   ; OUTI
site 02E03   ; OUTI
site 02E06   ; OUTI
site 02E09   ; OUTI
site 02E0C   ; OUTI
site 02E0F   ; OUTI
site 02E12   ; OUTI
site 02E15   ; OUTI
site 02E18   ; OUTI
site 02E1B   ; OUTI
site 02E1E   ; OUTI
site 02E21   ; OUTI
site 02E24   ; OUTI
site 02E27   ; OUTI
site 02E2A   ; OUTI
site 02E2D   ; OUTI
site 02E30   ; OUTI
site 02E33   ; OUTI
site 02E36   ; OUTI
site 02E39   ; OUTI
site 02E3C   ; OUTI
site 02E3F   ; OUTI
site 02E42   ; OUTI
site 02E45   ; OUTI
site 02E5A   ; OUT ($BF),A
site 02E62   ; OUT ($BF),A
site 02E77   ; OUTI
site 02E7D   ; OUTI
site 02E83   ; OUTI
site 02E89   ; OUTI
site 02E8F   ; OUTI
site 02E95   ; OUTI
site 02E9B   ; OUTI
site 02EA1   ; OUTI
site 02EA7   ; OUTI
site 02EAD   ; OUTI
site 02EB3   ; OUTI
site 02EB9   ; OUTI
site 02EBF   ; OUTI
site 02EC5   ; OUTI
site 02ECB   ; OUTI
site 02ED1   ; OUTI
site 02ED7   ; OUTI
site 02EDD   ; OUTI
site 02EE3   ; OUTI
site 02EE9   ; OUTI
site 02EEF   ; OUTI
site 02EF5   ; OUTI
site 02EFB   ; OUTI
site 02F01   ; OUTI
site 02F07   ; OUTI
site 02F0D   ; OUTI
site 02F13   ; OUTI
site 02F19   ; OUTI
site 02F1F   ; OUTI
site 02F25   ; OUTI
site 0309A   ; IN A,($BF)
site 0314E   ; OTIR
site 0315C   ; IN A,($DD)
site 09DEF   ; OUT ($7F),A
site 09DF3   ; OUT ($7F),A
site 09E00   ; OUT ($7F),A
site 09E04   ; OUT ($7F),A
site 09E35   ; OUT ($7F),A
site 09E4C   ; OUT ($7F),A
site 09E59   ; OUT ($7F),A
site 09E68   ; OUT ($7F),A
site 09E7F   ; OUT ($7F),A
site 09E8C   ; OUT ($7F),A
site 09EB2   ; OUT ($7F),A
site 09EC5   ; OUT ($7F),A
site 09EDC   ; OUT ($7F),A
site 09EE2   ; OUT ($7F),A
site 09F06   ; OUT ($7F),A
site 09F1D   ; OUT ($7F),A
site 09F2A   ; OUT ($7F),A
site 09F87   ; OUT ($7F),A
site 0A180   ; OUT ($7F),A
site 0A185   ; OUT ($7F),A
site 0A199   ; OUT ($7F),A
site 0A1AC   ; OUT ($7F),A
site 0A1B8   ; OUT ($7F),A
site 0A1CB   ; OUT ($7F),A
mapst 00590   ; LD ($FFFF),A
mapst 005E6   ; LD ($FFFF),A
mapst 00633   ; LD ($FFFF),A
mapst 00659   ; LD ($FFFF),A
mapst 006B6   ; LD ($FFFF),A
mapst 0076C   ; LD ($FFFF),A
mapst 0090C   ; LD ($FFFF),A
mapst 009BB   ; LD ($FFFF),A
mapst 00A27   ; LD ($FFFF),A
mapst 00CD7   ; LD ($FFFF),A
mapst 0130B   ; LD ($FFFF),A
mapst 013E1   ; LD ($FFFF),A
mapst 01418   ; LD ($FFFF),A
mapst 015CC   ; LD ($FFFF),A
mapst 01629   ; LD ($FFFF),A
mapst 01780   ; LD ($FFFF),A
mapst 0204E   ; LD ($FFFF),A
mapst 0247D   ; LD ($FFFC),A
mapst 02482   ; LD ($FFFD),A
mapst 02487   ; LD ($FFFE),A
mapst 0248C   ; LD ($FFFF),A
mapst 024BB   ; LD ($FFFF),A
mapst 024DB   ; LD ($FFFF),A
mapst 025D5   ; LD ($FFFF),A
mapst 0262E   ; LD ($FFFF),A
mapst 0263D   ; LD ($FFFF),A
mapst 02669   ; LD ($FFFF),A
mapst 02692   ; LD ($FFFF),A
mapst 02E54   ; LD ($FFFF),A
mapst 030C3   ; LD ($FFFF),A
mapst 030CA   ; LD ($FFFF),A
mapst 03178   ; LD ($FFFF),A
mapst 0266F   # LD ($FFFF),A; after LD A,$02; JP/CALL target from $0016E; 32 bytes of valid code before it

# OutRun Europa (Europe, Brazil).cht, "Infinite Shields": RAM $C0DE is the shield bar, held at
# 10, so hits no longer lower it and the race goes on
poke "Infinite shields"
ar 00C0-DE0A
endpoke

# OutRun Europa (Europe, Brazil).cht, "Freeze Timer": RAM $C15C is the counter that ticks the
# race clock down, held at $13, so the time left never falls and the race does not end on time
poke "Infinite time"
ar 00C1-5C13
endpoke

# OutRun Europa (Europe, Brazil).cht, "Infinite Turbos": the cart byte at $0C8F is changed
# from $32 to $3A, so the turbo count in RAM $C150 is not stored back after a turbo is used
poke "Infinite turbos"
gg 3AC-8FF-2A2
endpoke

page 0 blk32 ntrows oe_mark oe_ready
; blk32: as the game's unrolled blocks at $2DE8 and $2E6B: A blocks of 32 bytes (0 means 256)
; from HL, as the game sees it, to VRAM from the VDP address, with one jt_vwrite call.
; Returns the registers as the OUTIs leave them: HL past the bytes, B less 32 x A, A = 0 and
; Z set; C, DE, IX and IY kept. The game has interrupts off here (DI at $2D28).
blk32:  ld (g_sp),sp
        ld sp,stk_top
        push de
        push ix
        push iy
        push bc
        ld e,a
        push de                 ; E = the blocks
        ld c,a
        ld b,32
        ld de,(vdp_addr)
        ld ix,32
        ld iy,32
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop de
        pop bc
        ld a,e
        and 7
        rrca
        rrca
        rrca                    ; (blocks x 32) mod 256
        neg
        add a,b
        ld b,a
        ld d,0
        ld a,e
        or a
        jr nz,.n
        inc d                   ; 0 blocks: 256
.n:     ex de,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,de               ; HL = the source + 32 x blocks
        pop iy
        pop ix
        pop de
        ld sp,(g_sp)
        xor a
        ret
; ntrows: as the game's loop at $2C16-$2D18: 16 rows of 64 bytes from HL, as the game sees
; it, the source stepping 128 a row, to VRAM from the VDP address, one row after another.
; Returns HL + $800, A = 0 and Z set; B, C, DE, IX and IY kept, as the loop leaves them.
; The game has interrupts off here (DI at $2C03).
ntrows: ld (g_sp),sp
        ld sp,stk_top
        push de
        push ix
        push iy
        ld de,(vdp_addr)
        push bc
        ld b,64
        ld c,16
        ld ix,128
        ld iy,64
        xor a
        call jt_vwrite
        pop bc
        ld de,$0800
        add hl,de
        pop iy
        pop ix
        pop de
        ld sp,(g_sp)
        xor a
        ret
; oe_mark: from the cave at $0040, interrupts off: a step starts at this frame event.
; Keeps every register but A.
oe_mark:
        ld a,(isr_n)
        ld (s0),a
        ret
; oe_ready: from the cave at $004A. Carry set when 3 frame events have passed since oe_mark.
; Keeps every register but F.
oe_ready:
        ld (sv_a),a
        ld a,(isr_n)
        push hl
        ld hl,s0
        sub (hl)
        pop hl
        cp 3
        ccf
        ld a,(sv_a)
        ret
sv_a:   db 0
s0:     db 0
g_sp:   dw 0
        ds 32
stk_top:
endpage
