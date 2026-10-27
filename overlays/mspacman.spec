# Ms. Pac-Man (Europe, Brazil) (En), CRC32 3CD816C6, 128K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log.
# The game measures the CPU against the frame at $4B03-$4B2C (10 HALTs, then a loop counted over
# one frame) and stores 1 at $DF0F below 1800 counts (NTSC), 0 above (PAL). At 28 MHz the count is
# far above, so the game takes its PAL path, as on a PAL Master System; it sets the title time
# ($4910) and the speeds ($4B52) from it. A reference on sg1000m3 (NTSC) needs $DF0F forced to 0.
# The frame handler $0074 writes registers 8 and 9 from $D708 and $D707; the line handler (line
# 164, register 10 = $A4) runs the sound driver ($1A7A or $4320).
name Ms. Pac-Man
cart 3CD816C6
hz 50		; No-Intro regions Europe, Brazil
priority		; tile $6E with the priority bit in columns 0, 1, 30 and 31 hides sprites in the tunnels
# The intermissions move the name table (register 2): without ntdiff each move rebuilt the whole
# Next map (815,000 cycles) and Layer 2 in one vertical blank, and the act ran 30 frames long.
ntdiff
# No free RST vector: $0000-$0002 (DI; JP $00EC) becomes the vector; the game starts at $00EC.
vector 00 io
start 00EC
asm 000EC 2   ; IM 1 -> IM 2
    im 2
endasm
asm 0431B 2   ; IM 1 -> IM 2
    im 2
endasm
site 00075   ; IN A,($BF)
site 000F8   ; OUT ($3E),A
site 00637   ; IN A,($0E)
site 01B18   ; OUT ($7F),A
site 01B20   ; OUT ($7F),A
site 01B2B   ; OUT ($7F),A
site 01B32   ; OUT ($7F),A
site 01B3A   ; OUT ($7F),A
site 023AD   ; OUT (C),L
site 023B2   ; OUT ($BF),A
site 023CF   ; OUTI
site 023D1   ; OUTI
site 023D3   ; OUTI
site 023D5   ; OUTI
site 023D7   ; OUTI
site 023D9   ; OUTI
site 023DB   ; OUTI
site 023DD   ; OUTI
site 023DF   ; OUTI
site 023E1   ; OUTI
site 023E3   ; OUTI
site 023E5   ; OUTI
site 023E7   ; OUTI
site 023E9   ; OUTI
site 023EB   ; OUTI
site 023ED   ; OUTI
site 023EF   ; OUTI
site 023F1   ; OUTI
site 023F3   ; OUTI
site 023F5   ; OUTI
site 023F7   ; OUTI
site 023F9   ; OUTI
site 023FB   ; OUTI
site 023FD   ; OUTI
site 023FF   ; OUTI
site 02401   ; OUTI
site 02403   ; OUTI
site 02405   ; OUTI
site 02407   ; OUTI
site 02409   ; OUTI
site 0240B   ; OUTI
site 0240D   ; OUTI
site 02435   ; OUT (C),L
site 0243A   ; OUT ($BF),A
# $2459 (OUTI) is inside the asm block at $2457 (tq)
site 02474   ; OUT ($BF),A
site 02478   ; OUT ($BF),A
site 02480   ; OUTI
site 02482   ; OUTI
site 02484   ; OUTI
site 02486   ; OUTI
site 02488   ; OUTI
site 0248A   ; OUTI
site 0248C   ; OUTI
site 0248E   ; OUTI
site 02490   ; OUTI
site 02492   ; OUTI
site 02494   ; OUTI
site 02496   ; OUTI
site 02498   ; OUTI
site 0249A   ; OUTI
site 0249C   ; OUTI
site 0249E   ; OUTI
site 024A0   ; OUTI
site 024A2   ; OUTI
site 024A4   ; OUTI
site 024A6   ; OUTI
site 024A8   ; OUTI
site 024AA   ; OUTI
site 024AC   ; OUTI
site 024AE   ; OUTI
site 024B0   ; OUTI
site 024B2   ; OUTI
site 024B4   ; OUTI
site 024B6   ; OUTI
site 024B8   ; OUTI
site 024BA   ; OUTI
site 024BC   ; OUTI
site 024BE   ; OUTI
site 024C0   ; OUTI
site 024C2   ; OUTI
site 024C5   ; OUT ($BF),A
site 024C8   ; OUT ($BF),A
site 024CC   ; OUTI
site 024CE   ; OUTI
site 024D0   ; OUTI
site 024D2   ; OUTI
site 024D4   ; OUTI
site 024D6   ; OUTI
site 024D8   ; OUTI
site 024DA   ; OUTI
site 024DC   ; OUTI
site 024DE   ; OUTI
site 024E0   ; OUTI
site 024E2   ; OUTI
site 024E4   ; OUTI
site 024E6   ; OUTI
site 024E8   ; OUTI
site 024EA   ; OUTI
site 024EC   ; OUTI
site 024EE   ; OUTI
site 024F0   ; OUTI
site 024F2   ; OUTI
site 024F4   ; OUTI
site 024F6   ; OUTI
site 024F8   ; OUTI
site 024FA   ; OUTI
site 024FC   ; OUTI
site 024FE   ; OUTI
site 02500   ; OUTI
site 02502   ; OUTI
site 02504   ; OUTI
site 02506   ; OUTI
site 02508   ; OUTI
site 0250A   ; OUTI
site 0250C   ; OUTI
site 0250E   ; OUTI
site 02510   ; OUTI
site 02512   ; OUTI
site 02514   ; OUTI
site 02516   ; OUTI
site 02518   ; OUTI
site 0251A   ; OUTI
site 0251C   ; OUTI
site 0251E   ; OUTI
site 02520   ; OUTI
site 02522   ; OUTI
site 02524   ; OUTI
site 02526   ; OUTI
site 02528   ; OUTI
site 0252A   ; OUTI
site 0252C   ; OUTI
site 0252E   ; OUTI
site 02530   ; OUTI
site 02532   ; OUTI
site 02534   ; OUTI
site 02536   ; OUTI
site 02538   ; OUTI
site 0253A   ; OUTI
site 0253C   ; OUTI
site 0253E   ; OUTI
site 02540   ; OUTI
site 02542   ; OUTI
site 02544   ; OUTI
site 02546   ; OUTI
site 02548   ; OUTI
site 0254A   ; OUTI
site 0254C   ; OUTI
site 0254E   ; OUTI
site 02550   ; OUTI
site 02552   ; OUTI
site 039EA   ; OUT ($BE),A
site 039F0   ; OUT ($BE),A
site 04080   ; OUT ($3F),A
site 04082   ; IN A,($DC)
site 040A1   ; IN A,($DD)
site 0413E   ; OUT ($3F),A
site 04140   ; IN A,($DC)
site 04154   ; IN A,($DD)
site 0428F   ; OUT ($BF),A
site 04292   ; OUT ($BF),A
site 042F8   ; IN A,($DD)
site 04326   ; OTIR
site 0433C   ; OUT ($BF),A
site 04346   ; OUT ($BF),A
site 0435D   ; OUT ($BE),A
site 0436C   ; OUT ($BF),A
site 04373   ; OUT ($BF),A
site 0437E   ; OUT ($BE),A
site 0458A   ; OUT ($BE),A
site 04591   ; OUT ($BE),A
site 045A8   ; OUT ($BE),A
site 045AF   ; OUT ($BE),A
site 0539A   ; OUT ($BE),A
site 053A2   ; OUT ($BE),A
site 053A9   ; OUT ($BE),A
site 053B1   ; OUT ($BE),A
site 0560C   ; OUT ($BE),A
site 05613   ; OUT ($BE),A
site 0563E   ; OUT ($BE),A
site 05645   ; OUT ($BE),A
site 077A3   ; OUT ($BE),A
site 077A8   ; OUT ($BE),A
site 077AD   ; OUT ($BE),A
site 077B2   ; OUT ($BE),A
site 07892   ; OUT ($BE),A
site 07899   ; OUT ($BE),A
site 0789E   ; OUT ($BE),A
site 078AB   ; OUT ($BE),A
site 078BA   ; OUT ($BE),A
site 078EE   ; OUT ($BE),A
site 078F5   ; OUT ($BE),A
site 07BC9   ; OUTI
site 07BCB   ; OUTI
site 07BCD   ; OUTI
site 07BCF   ; OUTI
site 07BD1   ; OUTI
site 07BD3   ; OUTI
site 07BD5   ; OUTI
site 07BD7   ; OUTI
site 07BD9   ; OUTI
site 07BDB   ; OUTI
site 07BDD   ; OUTI
site 07BDF   ; OUTI
site 07BE1   ; OUTI
site 07BE3   ; OUTI
site 07BE5   ; OUTI
site 07BE7   ; OUTI
site 07BE9   ; OUTI
site 07BEB   ; OUTI
site 07BED   ; OUTI
site 07BEF   ; OUTI
site 07BF1   ; OUTI
site 07BF3   ; OUTI
site 07BF5   ; OUTI
site 07BF7   ; OUTI
site 07BF9   ; OUTI
site 07BFB   ; OUTI
site 07BFD   ; OUTI
site 07BFF   ; OUTI
site 07C01   ; OUTI
site 07C03   ; OUTI
site 07C05   ; OUTI
site 07C07   ; OUTI
site 07C09   ; OUTI
site 07C0B   ; OUTI
site 07C0D   ; OUTI
site 07C0F   ; OUTI
site 07C11   ; OUTI
site 07C13   ; OUTI
site 07C15   ; OUTI
site 07C17   ; OUTI
site 07C19   ; OUTI
site 07C1B   ; OUTI
site 07C1D   ; OUTI
site 07C1F   ; OUTI
site 07C21   ; OUTI
site 07C23   ; OUTI
site 07C25   ; OUTI
site 07C27   ; OUTI
site 07C29   ; OUTI
site 07C2B   ; OUTI
site 07C2D   ; OUTI
site 07C2F   ; OUTI
site 07C31   ; OUTI
site 07C33   ; OUTI
site 07C35   ; OUTI
site 07C37   ; OUTI
site 07D15   ; OUT ($BE),A
site 07D1B   ; OUT ($BE),A
site 07D29   ; OUT ($BE),A
site 07D2F   ; OUT ($BE),A
site 07D41   ; OUT ($BE),A
site 07D47   ; OUT ($BE),A
mapldk 000FA   # LD HL,$FFFC; LD (HL),$80
maphl 00100   # LD (HL),$00, HL = $FFFD
maphl 00103   # LD (HL),$01, HL = $FFFE
maphl 00106   # LD (HL),$02, HL = $FFFF
mapst 01DA1   ; LD ($FFFC),A
mapst 01DBD   ; LD ($FFFC),A
mapst 023C7   ; LD ($FFFF),A
mapst 0244F   ; LD ($FFFF),A
mapst 04172   ; LD ($FFFF),A
mapst 0418A   ; LD ($FFFF),A
mapst 0419F   ; LD ($FFFF),A
mapst 041A9   ; LD ($FFFF),A
mapst 076F1   ; LD ($FFFF),A
mapst 07727   ; LD ($FFFF),A
mapst 0776F   ; LD ($FFFF),A
mapst 07861   ; LD ($FFFF),A
mapst 078CF   ; LD ($FFFF),A
mapst 0790A   ; LD ($FFFF),A
# Indirect transfers the scanner leaves open. RST $08 ($0008-$0013) jumps through a table of words
# that follows the RST: $2E83, $4DFC and $4EDD. The scanner reads on into those tables as code,
# which gives the store LD ($1862),HL at $2E9A and the jump to RAM at $2E8E: both are table bytes.
# $1850 is PUSH DE; RET through the table at $1851; $41A5 calls bank C at $8000 + B through JP (HL).
# The low-confidence byte patterns IN A,($DD) and IN A,($3E) at $3013, $4F97, $4FBF, $4FE4, $5008,
# $64FE and $652C are operands of LD IX,$DBnn; OUT ($DD),A at $37E9 is a DJNZ operand; $170CA and
# $181FE are data.
# Mapper stores found by the byte scan in bytes no path reached:
mapst 04249   # LD ($FFFF),A; after LD A,$1F; 32 bytes of valid code before it
mapst 07925   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 0792B   # LD ($FFFF),A; after LD A,$05; 32 bytes of valid code before it
# Code that no recording ran, read by hand (z88dk-dis): the VDP library at $4230-$42E7 (fill, VRAM
# read, palette loads), the screen setup loops at $56FF-$5726, $57B8, $5D35, $5E9A, $5F57-$5FC0 and
# $62D6, and the RLE decoders' bank stores at $77E8-$79DF. $423A-$424F is a debug VRAM dump that
# ends in JR $; its mapper stores are patched as well.
site 04231   ; OUT ($BE),A
site 04254   ; IN A,($BE)
site 042A1   ; OUT ($BF),A
site 042A8   ; OUT ($BF),A
site 042B7   ; OUT ($BE),A
site 042C0   ; OUT ($BF),A
site 042C7   ; OUT ($BF),A
site 042CF   ; OUT ($BE),A
site 042D7   ; OUT ($BF),A
site 042DE   ; OUT ($BF),A
site 042E4   ; OUT ($BE),A
site 056FF   ; OUT ($BE),A
site 05707   ; OUT ($BE),A
site 0571D   ; OUT ($BE),A
site 057BC   ; OUT ($BE),A
site 057C3   ; OUT ($BE),A
# $5D3A (OUT ($BE),A) is inside the asm block at $5D35 (ntcopy)
# $5E9F, $5EA5, $5F60, $5F67, $5F92, $5F97, $5FB3 and $5FB9 (OUT ($BE),A) are inside the asm blocks
# at $5E9A, $5F57, $5F8B and $5FAE (vloop)
site 062DB   ; OUT ($BE),A
site 062E1   ; OUT ($BE),A
mapst 04244   ; LD ($FFFC),A
mapst 077E8   ; LD ($FFFF),A
mapst 0795B   ; LD ($FFFF),A
mapst 07996   ; LD ($FFFF),A
mapst 079DF   ; LD ($FFFF),A
# The screen wipe at $7EA1: 9 steps, each after an EI; HALT. A step writes 4 zero bytes (one tile
# row) into each of 448 tiles, 32 bytes apart, from the VRAM address in HL ($7EDF + step: 0, 4,
# ..., 1C, then the RET byte $C9). Through the traps a step took several Next frames, most of it
# converting 448 tiles. The page entry wipe_step writes the zero rows straight into the VRAM copy
# and the Next tile definitions (runtime internals named in the page), and takes the loop's time
# on a PAL Master System.
eihalt 07EA6   ; EI; HALT before each step
asm 07EB5 34   ; DI, CALL $428C, 4 x OUT ($BE),A, EI and the loop over 448 tiles, up to $7ED6
    di
    rst $00
    db far_io, pg_wipe_step, ent_wipe_step
.w: ei                  ; the rest of the step's time, interrupts on: the game's handler
    ld b,0              ; runs here, at the game's stack depth; the loop looks at the time
.d: djnz .d             ; every few lines
    rst $00
    db far_io, pg_wipe_wait, ent_wipe_wait
    jr nz,.w
    ei
endasm
# $76F5: the VRAM loader (four RLE and copy modes) runs in page entry ldr, which writes VRAM
# directly or in runs and keeps the loader's Master System time on the raster.
asm 076F5 8    ; LD A,$05; LD ($FFFF),A; LD H,$00; ADD HL,HL
    rst $00
    db far_io, pg_ldr, ent_ldr
    jp c,$7A32
    ret
endasm
# $4B03: LD B,10; HALT; DJNZ waits 10 interrupts. The page entry halt10 does the same with the
# patched HALT.
asm 04B03 5    ; LD B,$0A; HALT; DJNZ $4B05
    jp halt10c
endasm
# The cave for $4B03 in filler bytes ($FF) that no code reaches, $7F38-$7F7F: the 10 HALTs with
# the patched HALT, at the game's stack depth, then back to $4B08.
label halt10c 07F38
asm 07F38 9
    ld b,10
.w: rst $00
    db halt_io
    djnz .w
    jp $4B08
endasm
# The game keeps two stacks and switches with LD SP ($DED0 and $DF51; $DF0C holds a saved one).
# A frame handler entered on the stack the game leaves stays recorded in the runtime (isr_sp,
# $E0A0); while the game then runs lower on the other stack, the runtime's frm_run takes that
# handler for one still running and holds the game's events (the options menu waited 8 frames
# for its first frame event). Each switch goes through a cave that switches, then far-calls
# spsw, which clears isr_sp. The caves are in the filler at $7F41-$7F7F.
label spc_01D5C 07F41
asm 01D5C 4    ; LD SP,($DF0C)
    jp spc_01D5C
endasm
asm 07F41 11
    ld sp,($df0c)
    rst $00
    db far_io, pg_spsw, ent_spsw
    jp $1D60
endasm
label spc_04318 07F4C
asm 04318 3    ; LD SP,$DED0
    jp spc_04318
endasm
asm 07F4C 10
    ld sp,$ded0
    rst $00
    db far_io, pg_spsw, ent_spsw
    jp $431B
endasm
label spc_04DEA 07F56
asm 04DEA 3    ; LD SP,$DF51
    jp spc_04DEA
endasm
asm 07F56 10
    ld sp,$df51
    rst $00
    db far_io, pg_spsw, ent_spsw
    jp $4DED
endasm
label spc_01E54 07F60
asm 01E54 3    ; LD SP,$DED0
    jp spc_01E54
endasm
asm 07F60 10
    ld sp,$ded0
    rst $00
    db far_io, pg_spsw, ent_spsw
    jp $1E57
endasm
label spc_04E4B 07F6A
asm 04E4B 3    ; LD SP,$DED0
    jp spc_04E4B
endasm
asm 07F6A 10
    ld sp,$ded0
    rst $00
    db far_io, pg_spsw, ent_spsw
    jp $4E4E
endasm
label spc_05190 07F74
asm 05190 3    ; LD SP,$DED0
    jp spc_05190
endasm
asm 07F74 10
    ld sp,$ded0
    rst $00
    db far_io, pg_spsw, ent_spsw
    jp $5193
endasm
# The ends of the screens drawn with interrupts off (EI at $51B9, $516C, $48DE and $295F, found
# on the reference as the place of the first interrupt after each one). On the Master System the
# frame interrupt that came while interrupts were off is still asserted, and the handler runs
# right after the instruction that follows the EI: $D770 steps by 2 in that frame on the
# reference. The runtime gets no frame event while interrupts are off. Each EI goes through a
# cave that asks page entry irqp whether a frame passed in a paced page routine with interrupts
# off and frame interrupts are on, and if so enters
# the game's handler through RST $38 with interrupts off, as the CPU takes an interrupt. The
# HALTs at $2960 and $2961 become patched HALTs there. Caves in the zero filler at $7F80-$7FBC.
label eic_051B9 07F80
asm 051B9 4    ; EI; LD HL,$5BC8
    jp eic_051B9
endasm
asm 07F80 14
    ld hl,$5BC8
    rst $00
    db far_io, pg_irqp, ent_irqp
    jr z,.n
    rst $38
.n: ei
    jp $51BD
endasm
label eic_0516C 07F8E
asm 0516C 4    ; EI; LD HL,$5BE8
    jp eic_0516C
endasm
asm 07F8E 14
    ld hl,$5BE8
    rst $00
    db far_io, pg_irqp, ent_irqp
    jr z,.n
    rst $38
.n: ei
    jp $5170
endasm
label eic_048DE 07F9C
asm 048DE 4    ; EI; LD HL,$5BF9
    jp eic_048DE
endasm
asm 07F9C 14
    ld hl,$5BF9
    rst $00
    db far_io, pg_irqp, ent_irqp
    jr z,.n
    rst $38
.n: ei
    jp $48E2
endasm
label eic_0295F 07FAA
asm 0295F 3    ; EI; HALT; HALT
    jp eic_0295F
endasm
asm 07FAA 17
    rst $00
    db far_io, pg_irqp, ent_irqp
    jr z,.n
    rst $38          ; the held interrupt ends the first HALT
    jr .h2
.n: ei
    rst $00
    db halt_io
.h2:
    rst $00
    db halt_io
    jp $2962
endasm
# $44A6: the palette clear (32 zeros to CRAM, interrupts off when they were on). A frame event
# inside it is held until the EI at its end, on the Master System and on the Next. Page entry
# pal0 writes the zeros through the I/O RST and keeps the routine's Master System time (2,155
# T-states with the CALL).
asm 044A6 36   ; the whole routine $44A6-$44C9
    ld a,r
    push af
    di
    ld a,0
    jp po,.f
    inc a
.f: rst $00
    db far_io, pg_pal0, ent_pal0
    jr z,.n
    rst $38
.n: pop af
    jp po,.r
    ei
.r: ret
endasm
# The game's handler takes about 2,361 T-states for a line interrupt (the sound driver) and 420 for
# a frame interrupt on the reference. Handlers that come inside the screen wipe make each step that
# much longer on the Master System; on the Next they run while the step waits. To count the line
# entries the two sound driver calls of the line branch ($0096, $009C) go through caves in the zero
# filler $0044-$0065 that count them at $0060 (the cart copy is RAM); wipe_wait adds the time.
label isrc1 00044
label isrc2 0004D
asm 00044 18
    push hl
    ld hl,$0060
    inc (hl)
    pop hl
    jp $1A7A
    push hl
    ld hl,$0060
    inc (hl)
    pop hl
    jp $4320
endasm
asm 00096 3    ; CALL $4320
    call isrc2
endasm
asm 0009C 3    ; CALL $1A7A
    call isrc1
endasm
# The power-on and reset path clears RAM natively in a fraction of the Master System's time: the
# LDIR at $0112 (7,775 bytes, 163,270 T-states, about 2.7 NTSC frames) and, at power-on only, the
# loop at $013D (8,175 bytes at 39 T-states, about 5.3 frames). The menu restarts the game through
# JP $0000 before each game, so the LDIR runs then too. Page entries clrl and clrb do the same
# stores and keep the Master System time (pace).
label clrl_c 00056
asm 00111 3    ; LD (HL),L; LDIR
    jp clrl_c
endasm
asm 00056 8
    ld (hl),l
    rst $00
    db far_io, pg_clrl, ent_clrl
    jp $0114
endasm
asm 0013D 8    ; XOR A; LD (HL),A; INC HL; DEC BC; LD A,B; OR C; JR NZ,$013D
    rst $00
    db far_io, pg_clrb, ent_clrb
endasm
# $4361: a RAM fill (L = A, then BC bytes of A from DE). The game start ($2AC3) fills
# $C200-$D6FF with interrupts on: about 4.2 frames on the reference, a moment on the Next. Page
# entry fill43 fills, then waits with interrupts on until the Master System time has passed
# (43 T-states a byte, and the handlers that came meanwhile, as in wipe_wait).
asm 04361 10   ; LD L,A and the loop at $4362-$4369, RET
    rst $00
    db far_io, pg_fill43, ent_fill43
    ret
endasm
# $7799: the RLE tile decoder's output routine. It writes the 32-byte tile buffer at $D857 to the
# VDP data port, row by row, the 4 planes 8 bytes apart in the buffer; the title picture and the
# text screens are drawn with it. The page entry tile4 writes the same bytes with jt_vwrite.
asm 07799 5    ; LD IY,$D857; PUSH BC
    rst $00
    db far_io, pg_tile4, ent_tile4
    ret
endasm
# $421C: the VRAM fill loop: BC words of DE from the VDP address. The page entry fillw writes them
# with jt_vwrite.
asm 0421C 16   ; the loop at $421C-$422B
    rst $00
    db far_io, pg_fillw, ent_fillw
    ret
endasm
# The game start screen ($2902-$295F) runs with interrupts off: the maze set-up in RAM, six
# loads, the name table and the text. On the Next the RAM work ran in a fraction of its Master
# System time and the name table upload, through the traps, in about four times it. Page entries
# cred_46be, cred_51d4, cred_4693 and cred_2b88 add the RAM work's Master System time to the
# budget (the loads and the EI wait for it); ntab writes the name table with jt_vwrite in its
# time. Each patch replaces the routine's first instruction, which the entry does.
asm 046BE 4    ; LD IY,$C200
    rst $00
    db far_io, pg_cred_46be, ent_cred_46be
endasm
asm 051D4 5    ; LD A,($DEFD); CP $01
    rst $00
    db far_io, pg_cred_51d4, ent_cred_51d4
    nop
endasm
asm 04693 6    ; LD HL,$C2C0; LD DE,$0000
    rst $00
    db far_io, pg_cred_4693, ent_cred_4693
    nop
    nop
endasm
asm 02B88 4    ; LD IX,$D793
    rst $00
    db far_io, pg_cred_2b88, ent_cred_2b88
endasm
asm 04574 5    ; LD HL,$3800; CALL $428C: the whole routine runs in ntab
    rst $00
    db far_io, pg_ntab, ent_ntab
    ret
endasm
# $436B: the palette upload (32 bytes from $D87F); page entry palup writes CRAM with cramw in
# the routine's Master System time.
asm 0436B 5    ; XOR A; OUT ($BF),A; LD A,(IX+0): the whole routine runs in palup
    rst $00
    db far_io, pg_palup, ent_palup
    ret
endasm
# $43FD: a delay loop, BC steps of 26 T-states, before the palette uploads at $4E80 and $4919;
# page entry dly keeps its Master System time.
asm 043FD 6    ; DEC BC; LD A,B; OR C; JR NZ,$43FD; RET
    rst $00
    db far_io, pg_dly, ent_dly
    ret
    nop
endasm
# $5D35: the name table copy loop (1,536 bytes, each with its own address write); page entry
# ntcopy writes them with jt_vwrite in the loop's Master System time.
asm 05D35 7    ; DI; CALL $428C; LD A,(DE); OUT ($BE),A, then on to $5D44
    rst $00
    db far_io, pg_ntcopy, ent_ntcopy
    jp $5D44
endasm
# $791B: the RAM decoder (the intermission pictures into $C200), in page entry rdec with its
# Master System time. Banks from $20 on stay with the game's code: the cave in
# the zero filler at $7FBE runs the original then.
label rdc 07FBE
asm 0791B 3    ; EXX; LD L,A: on to the cave
    jp rdc
endasm
asm 07FBE 17
    rst $00
    db far_io, pg_rdec, ent_rdec
    ret nc
    exx
    ld l,a
    ld a,($ffff)
    push af
    call $7929
    jp $7924
endasm
# The VRAM loops of act 1's second scene ($5F3F): the name table rows at $5F57, the tile copy at
# $5F8B, the name table fill at $5FAE, and the same fill at $5E9A. Each writes with an address
# write per row or word, inside DI/EI; through the traps the scene started 18 frames after the
# reference. Page entries vrow, vtile and vfill start the loop: the writes go with jt_vwrite, 256
# bytes a call, and vstep waits out the loop's Master System time and the handlers that come
# meanwhile (icredit). The windows for the game's handlers are in the patch, at the game's stack
# depth; the page code runs with interrupts off on its own stack.
asm 05F57 34   ; DI; CALL $428C; 32 x 2 OUT ($BE),A per row; EI; HL += $40; DJNZ, up to $5F78
    rst $00
    db far_io, pg_vrow, ent_vrow
.w: ei
    nop
    rst $00
    db far_io, pg_vstep, ent_vstep
    jr nz,.w
    jp $5F79
endasm
asm 05F8B 26   ; DI; CALL $428C; 2 x OUT ($BE),A; EI; the loop over BC words, up to $5FA4
    rst $00
    db far_io, pg_vtile, ent_vtile
.w: ei
    nop
    rst $00
    db far_io, pg_vstep, ent_vstep
    jr nz,.w
    jp $5FA5
endasm
asm 05FAE 21   ; DI; CALL $428C; OUT ($BE),E and D; EI; the loop over BC words, up to $5FC2
    rst $00
    db far_io, pg_vfill, ent_vfill
.w: ei
    nop
    rst $00
    db far_io, pg_vstep, ent_vstep
    jr nz,.w
    jp $5FC3
endasm
asm 05E9A 21   ; the same fill loop as $5FAE, up to $5EAE
    rst $00
    db far_io, pg_vfill, ent_vfill
.w: ei
    nop
    rst $00
    db far_io, pg_vstep, ent_vstep
    jr nz,.w
    jp $5EAF
endasm
# $2444: the tile upload queue. For each entry it pages the bank in and sends 64 bytes (two tiles)
# with OUTI in a DJNZ loop at $2457, interrupts on, from the VDP address set once at $2435. Through
# the traps, a queue at a level start ran past the frame: level 1 play took a frame more than on
# the reference (1E6C to 2145: 10.22 frames against 9.01). Page entry tq writes the 64 bytes with
# jt_vwrite. The game's frame waits for the frame interrupt, so the loop's own time is not kept.
asm 02457 6    ; LD B,$40; OUTI; DJNZ $2459
    rst $00
    db far_io, pg_tq, ent_tq
    ei
    nop
endasm
page 0 wipe_step wipe_wait tile4 fillw ldr spsw irqp pal0 clrl clrb fill43 cred_46be cred_51d4 cred_4693 cred_2b88 ntab palup dly ntcopy rdec vrow vtile vfill vstep ltick tq
        OPT --zxnext            ; NEXTREG, ADD HL,A
; wipe_step: HL = the VRAM address of the first run (H = 0). Does what the game's loop at
; $7EB5-$7ED6 does: 4 zero bytes at HL + 32 * n for n = 0 to 447, through the VDP data port, in
; the time that loop takes on a PAL Master System (249 T-states a tile, 111,552 for 448: 489 raster
; lines). Returns with the registers the loop leaves: HL + 448 * 32, DE = $0020, BC = 0, A = 0
; with Z set, interrupts on. IX and IY are kept.
; A run inside tile data (region_tab 0 for its 256-byte page) is written straight into the VRAM
; copy and the Next tile definitions. A run whose 4 bytes already hold 0 changes nothing and is
; skipped. A changed tile gets what the runtime's conv_page (fw3.asm) does after it converts a
; tile: its tm_mask entry cleared, its tile_slot entry (and for an odd tile its even partner's,
; the 8x16 pattern) cleared, pri_redo and its pri_chg bit set when pri_tiles holds it, and
; sat_dirty set. A run outside tile data, and every run after it, goes through jt_vwrite.
; Runtime internals used (addresses from build/rt/runtime.map):
;   SHADOW_PAGE 28, 29: the VRAM copy, here in slots 2-3 ($4000 + VRAM address)
;   TILE_PAGE 10, 11: the Next tile definitions, 32 bytes a tile in VRAM order, slots 4-5 ($8000 + address)
;   FW3_PAGE 100: tm_mask at offset 0 (2 bytes a tile), here in slot 4
;   FW2_PAGE 25 (runs at $2000): tile_slot $2400, pri_redo $346A, pri_tiles $3538,
;     pri_chg $3578, here in slot 5
;   part 1 ($E000): region_tab $E400, sat_dirty $E085, cur_mmu $E02D, vdp_latch $E035,
;     vdp_code $E036, vdp_addr $E037, vdp_rbuf $E039
; The work runs with interrupts off, with a window between chunks of 32 runs. A frame handler
; that ran in a window leaves isr_sp ($E0A0) inside this page's stack frames; it is set to 0
; before the return, or the runtime's frm_run would later take a deeper game stack for a frame
; handler still running and hold the game's frame events. The rest of the
; step's time is waited in the patch, at the game's stack depth, with wipe_wait.
W_SHADOW	equ 28
W_TILES		equ 10
W_FW3		equ 100
W_FW2		equ 25
W_REGION	equ $E4			; high byte of region_tab
W_SATDIRTY	equ $E085
W_CURMMU	equ $E02D
W_TMASK		equ $8000		; tm_mask with FW3 in slot 4
W_TSLOT		equ $A000+$0400		; tile_slot with FW2 in slot 5
W_PRIREDO	equ $A000+$146A
W_PRITILES	equ $A000+$1538
W_PRICHG	equ $A000+$1578
W_ISRSP		equ $E0A0		; isr_sp: the return slot of the last frame handler entry
W_T		equ 111547+56		; the loop at $7EB5 (249 T-states a tile, the last JR 5 fewer) and $7EA8-$7EB4

wipe_step:
        push ix
        push iy
        push hl
        xor a
        ld (wpl_n),a
        ld hl,wpb               ; no priority tile changed yet
        ld b,64
.wz:    ld (hl),a
        inc hl
        djnz .wz
        pop hl
        ld (wstart),hl
        ld (wa),hl
        ld a,($0060)            ; the handler entries so far (line: the cave's count; frame:
        ld (wcl),a              ; the game's own counter $D770)
        ld a,($d770)
        ld (wcf),a
        ld hl,$FFFF             ; a new budget: the HALT before the step is not the step's time
        ld (lfr),hl
        call lsetup             ; the budget: the loop's time on a Master System
        call wlate
        exx
        push bc
        push de
        push hl
        ld hl,W_T/2             ; in two parts: HL' holds 16 bits
        exx
        call ladd
        exx
        ld hl,W_T-W_T/2
        exx
        call ladd
        exx
        pop hl
        pop de
        pop bc
        exx
        ld hl,448
        ld (wn),hl
.chunk: ld hl,(wn)
        ld a,h
        or l
        jp z,.done
        ld b,32
        ld a,h
        or a
        jr nz,.full
        ld a,l
        cp 32
        jr nc,.full
        ld b,l
.full:  ld a,b
        ld (wcnt),a
        xor a
        ld (wlist_n),a
        call wfe                ; not over the frame event's line
        di
        nextreg $52,W_SHADOW
        nextreg $53,W_SHADOW+1
        nextreg $54,W_TILES
        nextreg $55,W_TILES+1
.run:   ld hl,(wa)
        ld d,W_REGION           ; tile data only: region_tab 0 for both pages the run touches
        ld e,h
        ld a,(de)
        or a
        jp nz,.tail
        ld a,l
        add a,3
        jr nc,.one
        ld e,h
        inc e
        ld a,(de)
        or a
        jp nz,.tail
.one:   ld a,l                  ; a run that crosses into the next tile: jt_vwrite
        and 31
        cp 29
        jp nc,.tail
        ld a,h
        or $40
        ld h,a                  ; HL = the run in the VRAM copy
        ld a,(hl)
        inc hl
        or (hl)
        inc hl
        or (hl)
        inc hl
        or (hl)
        jr z,.next              ; already 0: nothing changes
        ld (hl),0
        dec hl
        ld (hl),0
        dec hl
        ld (hl),0
        dec hl
        ld (hl),0
        ld a,l
        and 3
        jr nz,.unal
        ld a,h
        add a,$40
        ld h,a                  ; the same bytes in the tile definitions: all pixels 0
        ld (hl),0
        inc hl
        ld (hl),0
        inc hl
        ld (hl),0
        inc hl
        ld (hl),0
        jr .note
.unal:  push hl                 ; the two rows the run touches, converted from the copy
        ld a,l
        and $FC
        ld l,a
        call convrow
        pop hl
        inc hl
        inc hl
        inc hl
        ld a,l
        and $FC
        ld l,a
        call convrow
.note:  ld hl,(wa)              ; the tile: address / 32, into the list
        add hl,hl
        add hl,hl
        add hl,hl
        ld e,h                  ; E = tile low 8 bits... tile = address >> 5 (0-511)
        ld a,(wa+1)
        rrca
        rrca
        rrca
        rrca
        rrca
        and 1
        ld d,a
        ld hl,wlist_n
        ld a,(hl)
        inc (hl)
        add a,a
        ld hl,wlist
        add hl,a
        ld (hl),e
        inc hl
        ld (hl),d
.next:  ld hl,(wa)
        ld de,32
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (wa),hl
        ld hl,(wn)
        dec hl
        ld (wn),hl
        ld hl,wcnt
        dec (hl)
        jp nz,.run
        call wbook
        call wmap
        ei                      ; a window for the handlers, as between the game's tiles
        nop
        di
        call ltick              ; count the lines as they pass, so no frame wrap is missed
        jp .chunk
.tail:  call wbook              ; this run and the rest through jt_vwrite
        call wmap
        ei
.tl:    ld hl,(wn)
        ld a,h
        or l
        jr z,.tdone
        ld bc,256
        ld a,h
        or a
        jr nz,.tc
        ld c,l
        ld b,0
.tc:    ld (wk),bc              ; runs in this call
        or a
        sbc hl,bc
        ld (wn),hl
        ld b,4                  ; C = runs (0 = 256)
        ld de,(wa)
        ld hl,wzero
        ld ix,0
        ld iy,32
        ld a,1                  ; the source is this page
        call jt_vwrite
        ld hl,(wk)              ; wa += 32 * runs
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,(wa)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (wa),hl
        jr .tl
.done:  ld hl,(wa)              ; the VDP state the last data write leaves
        ld de,-28
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld ($E037),hl           ; vdp_addr: the last run's address + 4
        ld a,1
        ld ($E036),a            ; vdp_code: VRAM write
        xor a
        ld ($E035),a            ; vdp_latch clear
        ld ($E039),a            ; vdp_rbuf: the last byte written
.tdone: call ptiles0
        ld hl,0                  ; no handler runs now: a handler that ran in a window left
        ld (W_ISRSP),hl         ; isr_sp inside this page's stack frames (see spsw)
        xor a
        ld (lheld),a            ; the wipe's windows took its interrupts
        pop iy
        pop ix
        ret

; wlate: the HALT before each step ends at the line interrupt (register 10, $A4: SMS line 164),
; and on the Master System the step starts 2,463 T-states (11 lines: the handler and $7EA8-$7EB4)
; after it, about 0.035 frames before the next line interrupt when it ends. The Next's handler
; (the sound driver through the traps) takes about 0.02 frames longer, and the step then ended a
; few lines before the next line interrupt or after it: then the HALT waited for the frame
; interrupt, and the wipe ended 0.11 frames late against the frame. When the line now lies
; between the line event and the frame event, the lines since the line event beyond 11 come off
; the budget (17 lines while the music plays, $D9E7 not 0: the sound driver takes 1,470 T-states
; more, see lcl). Line event: Next line pic_end ($E090) - 192 + register 10 ($E045) + 1. Uses A, DE, HL.
wlate:  call lline
        ld a,($E045)
        cp 192
        ret nc
        ld e,a
        ld a,($E090)
        sub 192
        add a,e
        inc a                   ; the line event's Next line (pic_end is below 256)
        ld e,a
        ld d,0
        ld a,h
        or a
        ret nz                  ; past line 255: not in the picture
        ld a,($E090)
        cp l
        ret c                   ; past the frame event
        ld a,l
        sub e
        ret c                   ; before the line event
        ld e,a
        ld a,($d9e7)            ; the handler's lines: 11, or 17 while the music plays (lcl:
        or a                    ; 1,470 T-states more, 6 lines)
        ld a,e
        jr z,.q
        sub 6
        ret c
.q:     sub 11
        ret c
        ret z
        ld e,a
        ld hl,(lbudget)
        or a
        sbc hl,de
        ld (lbudget),hl
        ret
; wipe_wait: interrupts on, so no frame event is missed. Takes the lines passed off the budget;
; NZ while the step's time on a
; Master System has not passed. Then Z, with the registers the game's loop leaves: HL = the first
; address + 448 * 32, DE = $0020, BC = 0, A = 0.
wipe_wait:
        ld hl,0                 ; the game is in its main code: no frame handler runs, and one
        ld (W_ISRSP),hl         ; that comes in this call leaves isr_sp in its stack frames
        exx                     ; the handlers since the last call: their Master System time
        push hl
        ld hl,0
        exx
        ld a,($0060)
        ld hl,wcl
        ld b,(hl)
        ld (hl),a
        sub b
        jr z,.nl
        ld b,a
.l:     exx
        call lcl                ; a line entry: the sound driver, the acknowledge and JP $0074
        add hl,de
        exx
        djnz .l
.nl:    ld a,($d770)
        ld hl,wcf
        ld b,(hl)
        ld (hl),a
        sub b
        jr z,.nf
        ld b,a
.f:     exx
        ld de,420+23            ; a frame entry
        add hl,de
        exx
        djnz .f
.nf:    call ladd
        exx
        pop hl
        exx
        call ltick
        ld hl,0
        ld (W_ISRSP),hl
        ld hl,(lbudget)
        bit 7,h
        jr nz,.done
        ld a,h
        or l
        ret nz
.done:  ld hl,0                  ; a handler that came during this call left isr_sp in its
        ld (W_ISRSP),hl         ; stack frames; none runs now (see spsw)
        ld hl,(wstart)
        ld de,448*32
        add hl,de
        ld de,$0020
        ld bc,0
        xor a
        ret

; wfe: when the runtime's next event (ev_next, $E097: a line event's SMS line, or 192 for the frame
; event at pic_end, $E090; Next line = that + 1, as ev_program sets it) is less than 24 lines on,
; waits for it with interrupts on, so that a chunk of the wipe step or ptiles (each up to about 20
; lines with interrupts off) does not hold it off. In act 1's end wipe, a line event held off past
; the frame event's line found the frame flag set: the game's handler took its frame branch and
; the line entry (the sound driver) was lost, 19 line entries in 21 frames. Interrupts are on at
; the return. Uses A, HL.
wfe:    ld a,($E097)
        cp 192
        jr nz,.l
        ld a,($E090)
.l:     inc a
        ld (wfe_l),a
        call lline
        ld a,h
        or a
        ret nz
        ld a,(wfe_l)
        sub l                   ; lines to the event
        ret c
        cp 24
        ret nc
        ei
.w:     call lline
        ld a,h
        or a
        ret nz
        ld a,(wfe_l)
        dec a
        cp l
        jr nc,.w                ; up to the event's line
        nop                     ; the event is taken here
        ret
wfe_l:  db 0
; Puts the game's pages back in slots 2-5.
wmap:   ld a,(W_CURMMU+2)
        nextreg $52,a
        ld a,(W_CURMMU+3)
        nextreg $53,a
        ld a,(W_CURMMU+4)
        nextreg $54,a
        ld a,(W_CURMMU+5)
        nextreg $55,a
        ret

; The runtime state of the tiles in wlist (interrupts off).
wbook:  ld a,(wlist_n)
        or a
        ret z
        ld b,a
        nextreg $54,W_FW3
        nextreg $55,W_FW2
        ld ix,wlist
.t:     ld e,(ix+0)
        ld d,(ix+1)             ; DE = tile
        ld hl,W_TMASK
        add hl,de
        add hl,de
        ld (hl),0               ; tm_mask: 2 bytes
        inc hl
        ld (hl),0
        ld hl,W_TSLOT
        add hl,de
        ld (hl),0               ; tile_slot
        bit 0,e
        jr z,.ev
        dec hl
        ld (hl),0               ; an odd tile drops its even partner too
.ev:    ld a,e                  ; pri_tiles: byte tile >> 3, bit tile & 7
        and 7
        ld c,a
        ld a,1
        jr z,.b0
.bs:    add a,a
        dec c
        jr nz,.bs
.b0:    ld c,a
        ld a,e
        srl d
        rra
        srl a
        srl a
        ld hl,W_PRITILES
        add hl,a
        ld a,(hl)
        and c
        jr z,.np
        ld a,1                  ; a priority tile: its cells are drawn again by ptiles at the
        ld (wpl_n),a            ; step's end (the runtime's redraw, pri_redo and pri_chg, took
        ld a,l                  ; about 1.7 frames a step: the level end wipe ran 16 frames
        sub W_PRITILES&255      ; late); wpb has the same bit layout as pri_tiles
        push hl
        ld hl,wpb
        add hl,a
        ld a,(hl)
        or c
        ld (hl),a
        pop hl
.np:    inc ix
        inc ix
        djnz .t
        ld a,1
        ld (W_SATDIRTY),a
        ret

; HL = a row in the VRAM copy ($4000 + address, 4-aligned). Writes its 4 converted bytes to the
; tile definitions ($8000 + address): 2 pixels a byte, high nibble first, plane 0 in bit 0.
convrow:
        ld d,h
        ld e,l
        ld a,d
        add a,$40
        ld d,a                  ; DE = the definition row
        ld b,(hl)
        inc hl
        ld c,(hl)
        inc hl
        ld a,(hl)
        inc hl
        ld l,(hl)
        ld h,a                  ; planes: B 0, C 1, H 2, L 3
        ld a,4
        ld (wcv),a
.byte:  sla l
        rla
        sla h
        rla
        sla c
        rla
        sla b
        rla
        sla l
        rla
        sla h
        rla
        sla c
        rla
        sla b
        rla
        ld (de),a
        inc de
        ld a,(wcv)
        dec a
        ld (wcv),a
        jr nz,.byte
        ret

wstart: dw 0
wcl:    db 0
wcf:    db 0
wa:     dw 0
wn:     dw 0
wk:     dw 0
wcnt:   db 0
wcv:    db 0
wzero:  db 0,0,0,0
wlist_n: db 0
wlist:  ds 64
; halt10: waits for 10 of the game's interrupts with the patched HALT, as LD B,10; HALT;
; DJNZ at $4B03 does. Returns with B = 0.
; tile4: as the game's routine at $7799-$77BF. Writes the tile buffer at $D857 from the VDP
; address: for row r of 8, the bytes at $D857 + r + 0, 8, 16 and 24. Returns with IY = $D857,
; E = $20, A = the last byte ($D876), F, B, C, D, HL and IX as they were. Runtime state read:
; vdp_code, vdp_addr. With a VDP code other than 1 (a VRAM write) it writes through the I/O RST,
; as the game does.
tile4:
        push af
        ld a,(vdp_code)
        cp 1
        jr nz,.slow
        push bc
        push de
        push hl
        push ix
        ld de,(vdp_addr)
        ld hl,$D857
        ld ix,1                 ; the source: the 8 bytes of one plane
        ld iy,4                 ; the VRAM: every fourth byte
        ld bc,$0108             ; 8 runs of 1 byte
        ld a,4                  ; 4 planes
.p:     push af
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop af
        inc de
        push bc
        ld bc,8
        add hl,bc
        pop bc
        dec a
        jr nz,.p
        pop ix
        pop hl
        pop de
        pop bc
        jr .done
.slow:  push bc
        ld iy,$D857
        ld b,8
.r:     ld a,(iy+0)
        rst $00
        db 4                    ; OUT ($BE),A
        ld a,(iy+8)
        rst $00
        db 4
        ld a,(iy+16)
        rst $00
        db 4
        ld a,(iy+24)
        rst $00
        db 4
        inc iy
        djnz .r
        pop bc
.done:  ld iy,$D857
        ld e,$20
        pop af
        ld a,($D876)
        ret
; fillw: as the game's loop at $421C-$422B: BC (1 to 65536) words E, D from the VDP address, in
; runs of up to 128 words through jt_vwrite, paced to the loop's Master System time (72 T-states a
; word, and 78 for the CALL $428C before it and the RET) as ldr is (pace). Returns with BC = 0,
; A = 0 and the flags of OR C (Z set), DE, HL and IX as they were. Runtime state read: vdp_code,
; vdp_addr; other codes go through the I/O RST, unpaced.
fillw:
        push de
        push hl
        push ix
        push iy
        exx
        push bc
        push de
        push hl
        ld hl,78
        exx
        push bc
        push de
        call lsetup
        pop de
        pop bc
        ld a,(vdp_code)
        cp 1
        jp nz,.slow
        ld hl,lbuf              ; 128 words of E, D
        push bc
        ld b,128
.f:     ld (hl),e
        inc hl
        ld (hl),d
        inc hl
        djnz .f
        pop bc
        ld de,(vdp_addr)
.c:     ld a,b
        or c
        jp z,.end
        ld hl,128               ; k = the words in this run, at most 128
        or a
        sbc hl,bc
        jr c,.full
        ld a,c                  ; BC <= 128
        jr .k
.full:  ld a,128
.k:     push bc
        push af
        add a,a                 ; 2k bytes (0 = 256)
        ld b,a
        ld c,1
        ld hl,lbuf
        ld ix,0
        ld iy,0
        ld a,1                  ; the source is this page
        call jt_vwrite
        ld de,(vdp_addr)
        pop af
        exx                     ; T += 72 k
        ld b,a
        ld de,72
.t:     add hl,de
        djnz .t
        exx
        call pace
        pop bc
        push hl
        ld h,0
        ld l,a
        ex de,hl
        ld h,b
        ld l,c
        or a
        sbc hl,de
        ld b,h
        ld c,l
        pop hl
        ld de,(vdp_addr)
        jp .c
.slow:  ld a,e
        rst $00
        db 4                    ; OUT ($BE),A
        ld a,d
        rst $00
        db 4
        dec bc
        ld a,b
        or c
        jr nz,.slow
.end:   exx
        pop hl
        pop de
        pop bc
        exx
        pop iy
        pop ix
        pop hl
        pop de
        ld bc,0
        xor a
        ret
; ldr: the game's VRAM loader $76F5-$7918 (entered from the wrapper $76E3 with L = the entry
; number), in page code that keeps the Master System's time. The code is the game's, instruction
; for instruction, with the same registers and RAM results ($D877-$D87E header, $D70F marker,
; $D857 tile buffer, IX = $D877, IY, E). Each block adds its T-states to HL' (TADD). The VRAM
; writes are collected: the tile output ($7799) goes straight into the VRAM copy and the Next tile
; definitions as in wipe_step (tout), the byte outputs (modes 0, 2 and 3) are buffered and written
; with jt_vwrite in runs of up to 256 bytes (lput, lflush). After each tile and each run, pace
; waits on the raster until the Master System would have reached the same point: 228 T-states a
; Next line at 50 Hz (PAL, 3,546,893 Hz), 226 at 60 Hz (NTSC, 3,579,545 Hz). The time before the
; loader (the caller's CALL $76E3 and the wrapper, 189 T-states) is counted at the start.
; Returns as the loader returns, with carry clear; with carry set and the registers of $772C
; when the bank is $20 or more (the patch then jumps to $7A32, as the game does).
; Runtime internals: as wipe_step, and vdp_code, vdp_addr, vdp_latch, vdp_rbuf.
	MACRO TADD n
	ex af,af'
	exx
	ld de,n
	add hl,de
	exx
	ex af,af'
	ENDM

ldr:    ex af,af'
        push af
        ex af,af'
        exx
        push bc
        push de
        push hl
        ld hl,189
        exx
        push hl
        call lsetup
        pop hl
        ; $76F5
        ld a,$05
        rst $00
        db $13, $FF             ; LD ($FFFF),A
        ld h,$00
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,$8000
        add hl,de
        ld de,$d877
        ld bc,$0008
        ldir
        ld ix,$d877
        ld h,(ix+$00)
        ld l,(ix+$01)
        ld b,(ix+$02)
        ld c,(ix+$03)
        dec bc
        ld e,$20
        ld iy,$d857
        ld a,(ix+$06)
        add a,$05
        rst $00
        db $13, $FF             ; LD ($FFFF),A
        cp $20
        jp nc,.bad
        TADD 7+13+7+33+10+11+10+10+163+14+76+6+7+14+19+7+13+7+10
        ld a,(hl)
        ld ($d70f),a
        inc hl
        dec bc
        ld a,(ix+$07)
        TADD 7+13+6+6+19
        cp $02
        jp z,.m2a
        cp $03
        jp z,.m3a
        and a
        jp nz,.m1a
        TADD 7+10+7+10+4+10+10
        jp m0
.m2a:   TADD 7+10
        jp m2
.m3a:   TADD 7+10+7+10
        jp m3
.m1a:   TADD 7+10+7+10+4+10
        jp m1
.bad:   TADD 7+13+7+33+10+11+10+10+163+14+76+6+7+14+19+7+13+7+10
        push af
        call pace
        pop af
        scf
        jp lret

; mode 1 ($7749): RLE into the 32-byte buffer, a tile out at each 32 bytes
m1:     ld d,(hl)
        inc hl
        dec bc
        ld a,($d70f)
        cp d
        jp z,.run
        TADD 36+7+33
        ld (iy+$00),d
        inc iy
        dec e
        call z,tout
        jp nz,.n1
        jp .l5b
.n1:    TADD 10
.l5b:   ld a,b
        inc a
        jp nz,.t49
        TADD 8+7+46
        ld b,(ix+$04)
        ld c,(ix+$05)
        ld a,b
        or c
        jp z,lexit11
        TADD 5+107
        dec bc
        ld a,(ix+$06)
        add a,$05
        inc a
        rst $00
        db $13, $FF
        ld (ix+$04),$00
        ld (ix+$05),$00
        ld hl,$8000
        jp m1
.t49:   TADD 8+12
        jp m1
.run:   TADD 36+12+23
        inc hl
        ld d,(hl)
        inc d
        dec hl
.l8a:   dec d
        jp z,.l80
        TADD 4+7+40+12
        ld a,(hl)
        ld (iy+$00),a
        inc iy
        dec e
        call z,tout
        jp z,.l8a
        TADD 10
        jp .l8a
.l80:   TADD 4+12+36
        inc hl
        dec bc
        inc hl
        dec bc
        jp .l5b

; tout: the call of $7799 (17 T-states) and its body (1212): the tile buffer to VRAM. Returns as
; $7799 does: IY = $D857, E = $20, A = ($D876), F, B, C, D and HL kept. Z is still set (the
; caller's DEC E), so the caller's JR Z after CALL Z tells a taken call.
tout:   TADD 17+1212
        push af
        push bc
        push de
        push hl
        push ix
        call tdirect
        pop ix
        pop hl
        pop de
        pop bc
        call pace
        pop af
        ld iy,$d857
        ld e,$20
        ld a,($d876)
        ret

; mode 0 ($78B0): RLE bytes to the VDP data port
m0:     ld d,(hl)
        inc hl
        dec bc
        ld a,($d70f)
        cp d
        jp z,.run
        TADD 36+7+15
        ld a,d
        call lput
.lbc:   ld a,b
        inc a
        jp nz,.tb0
        TADD 8+7+46
        ld b,(ix+$04)
        ld c,(ix+$05)
        ld a,b
        or c
        jp z,lexit11
        TADD 5+101
        ld a,(ix+$06)
        add a,$05
        inc a
        rst $00
        db $13, $FF
        ld (ix+$04),$00
        ld (ix+$05),$00
        ld hl,$8000
        jp m0
.tb0:   TADD 8+12
        jp m0
.run:   TADD 36+12+23
        inc hl
        ld d,(hl)
        inc d
        dec hl
.lea:   dec d
        jp z,.le0
        TADD 4+7+30
        ld a,(hl)
        call lput
        jp .lea
.le0:   TADD 4+12+36
        inc hl
        dec bc
        inc hl
        dec bc
        jp .lbc

; mode 2 ($78F2): bytes to the VDP data port as they are
m2:     ld a,(hl)
        inc hl
        dec bc
        call lput
        ld a,b
        inc a
        jp nz,.t
        TADD 38+7+46
        ld b,(ix+$04)
        ld c,(ix+$05)
        ld a,b
        or c
        jp z,lexit11
        TADD 5+101
        ld a,(ix+$06)
        add a,$05
        inc a
        rst $00
        db $13, $FF
        ld (ix+$04),$00
        ld (ix+$05),$00
        ld hl,$8000
        jp m2
.t:     TADD 38+12
        jp m2

; mode 3 ($7839): RLE into 3-byte groups, each written as 4 bytes ($788B)
m3:     ld e,$03
        TADD 7
.l3b:   ld d,(hl)
        inc hl
        dec bc
        ld a,($d70f)
        cp d
        jp z,.run
        TADD 36+7+33
        ld (iy+$00),d
        inc iy
        dec e
        call z,out3
        jp nz,.n1
        jp .l4d
.n1:    TADD 10
.l4d:   ld a,b
        inc a
        jp nz,.t3b
        TADD 8+7+46
        ld b,(ix+$04)
        ld c,(ix+$05)
        ld a,b
        or c
        jp z,lexit11
        TADD 5+107
        dec bc
        ld a,(ix+$06)
        add a,$05
        inc a
        rst $00
        db $13, $FF
        ld (ix+$04),$00
        ld (ix+$05),$00
        ld hl,$8000
        jp .l3b
.t3b:   TADD 8+12
        jp .l3b
.run:   TADD 36+12+23
        inc hl
        ld d,(hl)
        inc d
        dec hl
.l7c:   dec d
        jp z,.l72
        TADD 4+7+40+12
        ld a,(hl)
        ld (iy+$00),a
        inc iy
        dec e
        call z,out3
        jp z,.l7c
        TADD 10
        jp .l7c
.l72:   TADD 4+12+36
        inc hl
        dec bc
        inc hl
        dec bc
        jp .l4d

; out3: CALL $788B (17) and its body (190). Z stays set for the caller.
out3:   TADD 17+190
        ld iy,$d857
        ld a,(iy+$00)
        call lput
        ld a,(iy+$02)
        and $0f
        call lput
        ld a,(iy+$01)
        call lput
        ld a,(iy+$02)
        srl a
        srl a
        srl a
        srl a
        call lput
        ld e,$03
        cp a                    ; Z set, as the caller's DEC E left it
        ret

; the loader's RET Z (11 T-states): write what is buffered, wait, return
lexit11:
        TADD 11
        push af
        call lflush
        call pace
        pop af
lret:   ex af,af'
        pop af
        ex af,af'
        exx
        pop hl
        pop de
        pop bc
        exx
        ret

; lput: A to the VDP data port, buffered. All registers and flags kept.
lput:   ld (lbyte),a
        push af
        push hl
        push de
        ld hl,(lbn)
        ld de,lbuf
        add hl,de
        ld a,(lbyte)
        ld (hl),a
        ld hl,(lbn)
        inc hl
        ld (lbn),hl
        ld a,h
        or a
        jp z,.k
        call lflush             ; 256 bytes
        call pace
.k:     pop de
        pop hl
        pop af
        ret

; lflush: the buffered bytes to VRAM from the VDP address, as data port writes.
lflush: push af
        push bc
        push de
        push hl
        push ix
        push iy
        ld bc,(lbn)
        ld a,b
        or c
        jp z,.e
        ld a,($E036)            ; vdp_code
        cp 1
        jp nz,.slow
        ld b,c                  ; B = bytes (0 = 256), C = 1 run
        ld c,1
        ld hl,lbuf
        ld de,($E037)           ; vdp_addr
        ld ix,0
        ld iy,0
        ld a,1                  ; the source is this page
        call jt_vwrite
        jp .z
.slow:  ld hl,lbuf
.s:     ld a,(hl)
        rst $00
        db 4                    ; OUT ($BE),A
        inc hl
        dec bc
        ld a,b
        or c
        jp nz,.s
.z:     ld hl,0
        ld (lbn),hl
.e:     pop iy
        pop ix
        pop hl
        pop de
        pop bc
        pop af
        ret

; lsetup: T-states a line and lines a frame for the video rate. A new stretch (a game handler ran
; since the last paced routine, lkey) starts with budget 0 at the line now; the same stretch keeps
; the budget (see below).
lsetup: ld a,i                  ; P/V = IFF2
        push af
        di
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld b,a
        pop af
        jp po,.di
        ei
.di:    ld a,b
        ld hl,311
        ld de,228
        bit 2,a
        jp z,.hz
        ld hl,264
        ld de,226
.hz:    ld (lwlen),hl
        ld (ltpl),de
        ld hl,0
        ld (lbn),hl
        call lkey               ; a game handler since the last paced routine?
        ld de,(lfr)
        or a
        sbc hl,de
        jr nz,.new
        call ltick              ; no: the same stretch with interrupts off; the budget stays,
        jp lfin                 ; and the native code since the last paced routine comes off
                                ; it: code with no model counts as no Master System time, and
                                ; slow code (traps) is made up later. A credit (cred_*) still
                                ; open is waited out before this routine writes anything.
.new:   call lkey               ; a new stretch from here: a credit added now stays in it
        ld (lfr),hl
        ld hl,0
        ld (lbudget),hl
        jp lmark

; pace: the T-states in HL' become lines of budget; waits until the budget is used up.
; All registers and flags kept (HL' keeps the remainder).
pace:   push af
        push bc
        push de
        push hl
        call ladd
.w:     rst $00                 ; IN A,($7E): a V counter read, so the runtime's checks of
        db $0A                  ; the frame (vbl_chk, its vblank work) run while the loader waits
        call ltick
        ld hl,(lbudget)
        bit 7,h
        jr nz,.x
        ld a,h
        or l
        jr nz,.w
.x:     call lkey
        ld (lfr),hl
        pop hl
        pop de
        pop bc
        pop af
        ret

; ladd: the T-states in HL' become lines of budget (HL' keeps the remainder). Uses A, BC, DE, HL.
ladd:   exx
        push hl
        exx
        pop hl
        ld de,(ltpl)
        ld bc,(lbudget)
.d:     or a
        sbc hl,de
        jr c,.dd
        inc bc
        jr .d
.dd:    add hl,de
        ld (lbudget),bc
        push hl
        exx
        pop hl
        exx
        ret

; ltick: the lines passed since lprev come off the budget. Uses A, DE, HL.
; The line count gives the time modulo the Next's frame, and a gap of a frame or more comes: the
; runtime's once-a-frame work, run from the V counter read in pace or from a trap with the game's
; interrupts off, took over 2 frames at power-on. So CTC channel 0 runs as a free timer (lmark),
; and of the gaps d, d + one frame and d + two frames the one that agrees best with its count is
; taken (lwrap), as in the Psycho Fox overlay. The line and the count are read together with
; interrupts off.
ltick:  push bc
        ld a,i
        push af
        di
        ld a,0
        jp po,.ie
        inc a
.ie:    ld (lt_ie),a            ; 1: the interrupts were on
        ld (lt_sp),sp           ; the work on a stack of its own in this page (interrupts off):
        ld sp,lt_top            ; the game's second stack ($DF51) has its variables $DF0F-$DF11
        call lline              ; 64 bytes below, and this call chain wrote over them
        ld bc,$183B
        in a,(c)
        ld c,a
        ld a,(lctc)
        sub c                   ; CTC counts since lprev, mod 256 (it counts down)
        ld (lwg),a
        ld a,c
        ld (lctc),a
        ld de,(lprev)
        ld (lprev),hl
        push hl
        push de
        or a
        sbc hl,de
        jr nc,.pos
        ld de,(lwlen)
        add hl,de
.pos:   call lwrap              ; HL = the lines passed
        ex de,hl
        ld hl,(lbudget)
        or a
        sbc hl,de
        ld (lbudget),hl
        pop de
        pop hl
        ld a,(lt_ie)            ; the interrupts were off: did the frame event's line pass?
        or a                    ; Then the Master System's frame interrupt is now held for
        jr nz,.nh               ; the next EI (lheld, irqp)
        ld a,(lwk)
        or a
        jr nz,.held             ; a whole frame passed
        call lcross
        jr nc,.nh
.held:  ld a,1
        ld (lheld),a
.nh:    call lkey
        ld (lfr),hl
        ld sp,(lt_sp)
        pop af
        pop bc
        ret po
        ei
        ret

; lwrap: HL = the lines passed modulo the frame, lwg = the CTC counts passed modulo 256 (one count
; every 256 cycles, 57/8 counts a line). Returns HL = the lines passed with the whole frames that
; the CTC shows (0 to 2, in lwk). Uses A, DE.
lwrap:  push bc
        push ix
        ld ixl,$FF              ; the best distance so far
        xor a
        ld (lwk),a
        ld (lwb),hl
        ld b,3
        ld c,0                  ; k
.k:     push hl
        push bc
        ld d,h                  ; HL x 57 / 8: the lines in CTC counts
        ld e,l
        add hl,hl
        add hl,hl
        add hl,hl
        push hl
        add hl,hl
        add hl,hl
        add hl,hl
        pop bc
        or a
        sbc hl,bc
        add hl,de
        srl h
        rr l
        srl h
        rr l
        srl h
        rr l
        pop bc
        ld a,(lwg)
        sub l                   ; the circular distance to the CTC's count
        jp p,.ab
        neg
.ab:    cp ixl
        jr nc,.nb
        ld ixl,a
        ld a,c
        ld (lwk),a
        pop hl
        ld (lwb),hl
        push hl
.nb:    pop hl
        ld de,(lwlen)
        add hl,de
        inc c
        djnz .k
        ld hl,(lwb)
        pop ix
        pop bc
        ret

; lmark: lprev and lctc = now: the line and the CTC count, read together with interrupts off.
; Starts CTC channel 0 at the first call (a timer, prescaler 256, time constant 256, no
; interrupt). Uses A, HL.
lmark:  ld a,i
        push af
        di
        push bc
        ld bc,$183B
        ld a,(lctcr)
        or a
        jr nz,.on
        inc a
        ld (lctcr),a
        ld a,$27                ; timer, prescaler 256, time constant next, reset
        out (c),a
        xor a                   ; time constant 256
        out (c),a
.on:    call lline
        ld (lprev),hl
        in a,(c)
        ld (lctc),a
        pop bc
        pop af
        ret po
        ei
        ret
lt_sp:  dw 0
lt_ie:  db 0
        ds 48
lt_top:
lctc:   db 0
lctcr:  db 0
lwg:    db 0
lwk:    db 0
lwb:    dw 0

; lcross: DE = the line before, HL = the line now. Carry when the Next line of the frame event
; (pic_end + 1; pic_end at $E090, the line the runtime programs for it) lies in (DE, HL], with a
; frame wrap when HL < DE. Uses A, BC.
lcross: ld a,($E090)
        inc a
        ld c,a
        ld b,0                  ; BC = the event line
        push hl
        or a
        sbc hl,de
        pop hl
        jr c,.wrap
        push hl                 ; DE < E <= HL
        ld h,d
        ld l,e
        or a
        sbc hl,bc               ; DE - E: carry when DE < E
        pop hl
        ret nc
        push hl
        or a
        sbc hl,bc               ; HL - E: no carry when HL >= E
        pop hl
        ccf
        ret
.wrap:  push hl                 ; DE < E or HL >= E
        ld h,d
        ld l,e
        or a
        sbc hl,bc
        pop hl
        ret c
        push hl
        or a
        sbc hl,bc
        pop hl
        ccf
        ret

; lkey: HL = the stretch key: the game's frame counter $D770 and the line entry count at $0060
; (isrc1, isrc2). Two paced routines with the same key have no game handler between them: the
; same stretch with interrupts off. The runtime's fw_frames does not tell this: its frame work also
; runs at a trap's exit or a V counter read with the game's interrupts off. Uses A.
lkey:   ld a,($d770)
        ld l,a
        ld a,($0060)
        ld h,a
        ret

; lline: HL = the Next's raster line. The interrupt state is kept.
lline:  ld a,i                  ; P/V = IFF2
        push af
        di
        push bc
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
        dec b
        xor h
        and 1
        jp nz,.again
        pop bc
        ld a,h
        and 1
        ld h,a
        pop af
        ret po
        ei
        ret

; tdirect: the 32 bytes of the tile buffer ($D857, row r plane p at r + 8p) to VRAM from the VDP
; address. A whole tile of tile data with VDP code 1 goes into the VRAM copy and the tile
; definitions, with the state conv_page sets (wbook); anything else through jt_vwrite.
tdirect:
        ld hl,($E037)           ; vdp_addr
        ld a,($E036)
        cp 1
        jp nz,.slow
        ld a,l
        and 31
        jp nz,.slow
        ld d,W_REGION
        ld e,h
        ld a,(de)
        or a
        jp nz,.slow
        ld (taddr),hl
        ld a,i
        push af
        di
        nextreg $52,W_SHADOW
        nextreg $53,W_SHADOW+1
        nextreg $54,W_TILES
        nextreg $55,W_TILES+1
        ld a,h
        or $40
        ld h,a                  ; HL = the tile in the VRAM copy
        ld de,$d857
        ld b,8
.r:     ld a,(de)
        ld (hl),a
        inc hl
        push de
        ld a,e
        add a,8
        ld e,a
        ld a,(de)
        ld (hl),a
        inc hl
        ld a,e
        add a,8
        ld e,a
        ld a,(de)
        ld (hl),a
        inc hl
        ld a,e
        add a,8
        ld e,a
        ld a,(de)
        ld (hl),a
        inc hl
        pop de
        inc de
        push hl
        push de
        push bc
        dec hl
        dec hl
        dec hl
        dec hl
        call convrow
        pop bc
        pop de
        pop hl
        djnz .r
        ld hl,(taddr)           ; the tile: address / 32
        add hl,hl
        add hl,hl
        add hl,hl
        ld e,h
        ld a,(taddr+1)
        rrca
        rrca
        rrca
        rrca
        rrca
        and 1
        ld d,a
        ld (wlist),de
        ld a,1
        ld (wlist_n),a
        call wbook
        xor a
        ld (wlist_n),a
        call wmap
        ld hl,(taddr)           ; the VDP state the 32 data writes leave
        ld de,32
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld ($E037),hl
        xor a
        ld ($E035),a
        ld a,($d876)
        ld ($E039),a
        pop af
        ret po
        ei
        ret
.slow:  ld de,($E037)           ; 4 runs of 8 one-byte writes, 4 apart, as tile4
        ld hl,$d857
        ld ix,1
        push iy
        ld iy,4
        ld bc,$0108
        ld a,4
.p:     push af
        xor a
        call jt_vwrite
        pop af
        inc de
        push bc
        ld bc,8
        add hl,bc
        pop bc
        dec a
        jp nz,.p
        pop iy
        ret

lbyte:  db 0
lbn:    dw 0
ltpl:   dw 0
lwlen:  dw 0
lprev:  dw 0
lbudget: dw 0
lfr:    dw $FFFF
lheld:  db 0
taddr:  dw 0
lbuf:   ds 256
; spsw: after the game's LD SP. No frame handler runs now: isr_sp ($E0A0) = 0, so the runtime's
; frm_run does not take the stack the game left for a handler still running. Keeps every register.
spsw:   push hl
        ld hl,0
        ld (W_ISRSP),hl
        pop hl
        ret
; lfin: in the same stretch with interrupts off, a credit still open (lbudget above 0) is waited
; out on the raster. Keeps every register and HL'.
lfin:   push af
        push bc
        push de
        push hl
        call lkey
        ld de,(lfr)
        or a
        sbc hl,de
        jr nz,.x
        ld hl,(lbudget)
        bit 7,h
        jr nz,.x
        ld a,h
        or l
        jr z,.x
        exx
        push hl
        ld hl,0
        exx
        call pace
        exx
        pop hl
        exx
.x:     pop hl
        pop de
        pop bc
        pop af
        ret
; The credits: code with interrupts off between the game start ($2930) and its EI at $295F that
; runs natively on the Next, in a fraction of its Master System time, and writes only RAM. Each
; entry adds that time to the budget (lsetup: the same stretch keeps it) and does not wait: the
; next paced routine (ldr, ntab) or the EI (irqp, lfin) waits for it, and the native code
; meanwhile comes off it. Times are T-states counted from the code, and checked against the
; reference (sg1000m3, PAL path) on level 1. Each entry does the instruction it replaces.
	MACRO CR_IN
	push af
	push bc
	push de
	push hl
	exx
	push hl
	ld hl,0
	exx
	call lsetup
	ENDM
	MACRO CR_OUT
	exx
	pop hl
	exx
	pop hl
	pop de
	pop bc
	pop af
	ENDM
; cred_46be: at $46BE (LD IY,$C200), A = the maze ((IX+$2F)). From the CALL at $2930 to the
; first load at $2B1B: $46BE (the 1,344-word fill at $C200, 113,081; the maze decoder in bank 2
; through $4193, 332 + 3,413 a row, the rows at $5650 + maze; $472B 1,261; $45B5 7,747; $7D8D
; 2,264; the rest 254) and $2933-$2B1B ($2258, 23,987). $45B5, $7D8D and $2258 are the level 1
; times; they depend on the maze data.
cred_46be:
        ld (cmaze),a
        CR_IN
        ld bc,14887             ; 148,870 = 14,887 x 10
        ld e,10
        call lmul
        ld a,(cmaze)            ; the rows
        ld hl,$5650
        add hl,a
        call jt_peek
        ld e,a
        ld bc,3413
        call lmul
        CR_OUT
        ld iy,$C200
        ret
cmaze:  db 0
; cred_51d4: at $51D4 (LD A,($DEFD); CP $01, then a NOP): $2B1E-$2B22, the DI and $51D4 (the
; level text into RAM, twice through $52BE): 13,135 on level 1 (the number 1). The decimal
; conversion at $4C3A subtracts once more (176 T-states) for each unit of each digit of the
; number ($DA3C & $1F) + 1, so 352 more a unit of the digit sum: 14,895 on level 6, as the
; reference. Numbers of two digits (level 10 on) also print one more character: not counted.
cred_51d4:
        CR_IN
        ld bc,13135
        call ladd_bc
        ld a,($da3c)            ; the digit sum of (level & $1F) + 1, minus 1
        and $1F
        inc a
        ld c,0
.ds:    cp 10
        jr c,.d1
        sub 10
        inc c
        jr .ds
.d1:    add a,c
        dec a
        jr z,.d0
        ld c,a
        ld b,0
        ld e,176
        push bc
        call lmul
        pop bc
        ld e,176
        call lmul
.d0:    CR_OUT
        ld a,($defd)
        cp $01
        ret
; cred_4693: at $4693 (LD HL,$C2C0; LD DE,0, then 2 NOPs): the pellet count over ($DA39) rows of
; 32 cells (stride 2) from $C2C0, before it runs: 75 + 39 a row + 65 a cell that is not a pellet,
; 51 + P a $70 cell, 60 + P a $71 cell, P = 35 ($DEFB = 0) or 40. 76,861 on level 1, as the
; reference.
cred_4693:
        CR_IN
        push iy
        ld de,0                 ; DE: the $70 cells, IY: the $71 cells
        ld iy,0
        ld a,($da39)
        ld c,a                  ; rows (0: 256, as the game's DEC A; JR NZ)
        ld hl,$C2C0
.r:     ld b,32
.c:     ld a,(hl)
        cp $70
        jr z,.a
        cp $71
        jr z,.b
.nx:    inc hl
        inc hl
        djnz .c
        dec c
        jr nz,.r
        jr .sd
.a:     inc de
        jr .nx
.b:     inc iy
        jr .nx
.sd:    ld (cn70),de
        ld (cn71),iy
        pop iy
        ld a,($da39)            ; 39 a row
        ld c,a
        ld b,0
        or a
        jr nz,.r1
        inc b
.r1:    ld e,39
        push bc
        call lmul
        pop hl                  ; rows x 32 - pellets: the other cells, 65 each
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,(cn70)
        or a
        sbc hl,de
        ld de,(cn71)
        sbc hl,de
        ld b,h
        ld c,l
        ld e,65
        call lmul
        ld a,($defb)
        or a
        ld a,35
        jr z,.p
        ld a,40
.p:     push af
        add a,51
        ld e,a
        ld bc,(cn70)
        call lmul
        pop af
        add a,60
        ld e,a
        ld bc,(cn71)
        call lmul
        ld bc,75
        call ladd_bc
        CR_OUT
        ld hl,$C2C0
        ld de,0
        ret
cn70:   dw 0
cn71:   dw 0
; cred_2b88: at $2B88 (LD IX,$D793): $2B37-$2939: $2B88, the two 32-byte LDIRs and the rest of
; $2B18 (1,665), and $2BAD (the ghosts' set-up, 8,552). $2B88 takes 908 when ($D7CC) = 1; else
; each of its 8 steps calls the random number routine $41B3 (1,038 + 6 a set bit of the new
; $D8FF, from the 32-bit shift register at $D8FF-$D902, run here on a copy) and 17 more: 19,745 on
; level 1 and 11,125 on level 6, as the reference.
cred_2b88:
        CR_IN
        ld bc,908+1665+8552
        call ladd_bc
        ld a,($d7cc)
        cp 1
        jr z,.x
        ld de,($d8ff)           ; the shift register, as $41C5 runs it
        ld hl,($d901)
        ld c,8                  ; 8 calls
.c:     ld b,8
.r:     ld a,e
        and $48
        add a,$38
        rla
        rla
        rl h
        rl l
        rl d
        rl e
        djnz .r
        push de                 ; 1,038 + 17 + 6 x the set bits of E
        push hl
        push bc
        ld a,e
        ld e,0
.p:     or a
        jr z,.pe
        srl a
        jr nc,.p
        inc e
        jr .p
.pe:    ld a,e
        add a,a
        add a,e
        add a,a                 ; 6 x bits
        ld c,a
        ld b,0
        ld hl,1038+17
        add hl,bc
        ld b,h
        ld c,l
        call ladd_bc
        pop bc
        pop hl
        pop de
        dec c
        jr nz,.c
.x:     CR_OUT
        ld ix,$D793
        ret
; ntab: the name table upload $4574 (28 rows: 2 cells of tile $6E with the priority bit, the 28
; cells of the row from the copy at $C200 + 64 x row + 4, 2 cells of $6E) in its Master System
; time: 117 before the rows, 3,186 a row (the last 5 fewer), 10 for the RET (89,330 with the CALL;
; the reference takes 89,334 with the XOR A after it). The palette is all zeros through this
; whole screen (pal0 at the wipe end; the game loads it after $2962), so the order of the writes
; inside the screen does not show: the table goes in with three jt_vwrite calls (the middle 56
; bytes of each row from the copy, then the two border columns), the Layer 2 cells are drawn
; (pdraw), and only then does lsetup take the time since the last paced routine and wait for any
; credit still open, so the drawing takes place in the time of the credits before it. Through the
; traps the 1,792 writes took about 6.5 frames; the runtime's own redraw of the 112 border cells,
; in the once-a-frame work, took about 1.7 frames.
; Returns as the game's code: HL = $38 and L = (IX + 0), A = (IX + 0), DE = $C900, BC = 0, Z set.
ntab:   push ix
        push iy
        exx
        push bc
        push de
        push hl
        exx
        call ltick              ; the lines since the last paced routine
        ld hl,$C204             ; the middle of each row, from the copy as the game sees it
        ld de,$3804
        ld bc,$381C             ; 56 bytes, 28 runs
        ld ix,64
        ld iy,64
        xor a
        call jt_vwrite
        ld hl,ntb4              ; the border cells: $6E with the priority bit, twice
        ld de,$3800
        ld bc,$041C
        ld ix,0
        ld a,1
        call jt_vwrite
        call ltick              ; the lines so far (the middle took about 0.8 frames)
        ld hl,ntb4              ; the right border, the last run written: the VDP state the
        ld de,$383C             ; game leaves ($3F00, code 1, read buffer $10)
        ld bc,$041C
        ld ix,0
        ld iy,64
        ld a,1
        call jt_vwrite
        call jt_far             ; pdraw, page 1
        db pg_pdraw, ent_pdraw
        exx
        ld hl,0
        exx
        call lsetup
        ld bc,44665             ; 89,330 = 2 x 44,665
        call ladd_bc
        ld bc,44665
        call ladd_bc
        call pace
        exx
        pop hl
        pop de
        pop bc
        exx
        pop iy
        pop ix
        push ix
        pop hl
        call jt_peek            ; A = (IX + 0)
        ld l,a
        ld h,$38
        ld de,$C900
        ld bc,0
        cp a                    ; Z
        ret
ntb4:   db $6E,$10,$6E,$10
; ptiles0: the wipe step's priority tiles (ptiles, page 1) when wbook marked any: HL = wpb, A = the
; step's first VRAM address (low byte).
ptiles0:
        ld a,(wpl_n)
        or a
        ret z
        call wfe                ; ptiles runs with interrupts off: not over an event's line
        ld hl,wpb
        ld a,(wstart)
        call jt_far
        db pg_ptiles, ent_ptiles
        ret
wpl_n:  db 0
wpb:    ds 64
; irqp: first waits out a credit still open in this stretch (lfin): the screen's Master System time
; has passed at its EI. Then NZ when a frame passed while interrupts were off in a paced page routine (lheld, set by
; ltick; the runtime raises no frame event then) and register 1 (vdp_regs + 1, $E03C) has frame
; interrupts on: the interrupt the Master System would take at this EI. Then it also sets the
; frame flag in vdp_status ($E03A), which the game's handler reads. Clears lheld. Keeps A and
; every other register.
irqp:   call lfin
        push bc
        ld b,a
        ld a,(lheld)
        or a
        jr z,.x
        xor a
        ld (lheld),a
        ld a,($E03C)
        and $20
        jr z,.x
        ld a,($E03A)            ; the status the handler reads: the frame flag, as the VDP
        or $80                  ; holds it on the Master System
        ld ($E03A),a
        or a                    ; NZ
.x:     ld a,b
        pop bc
        ret
; pal0: the body of $44A6, A = 1 when the game's interrupts were on. Sets the CRAM address 0
; through the I/O RST, as the game does, writes 32 zeros with cramw, and keeps the routine's
; Master System time (pace).
; Returns as the game's code leaves HL, IX, B and E: HL + 32, IX + 32, B = 0, E = (IX + 31);
; C and D kept. Returns Z: a frame event while it runs stays pending in the Next's own interrupt
; and goes in at the routine's EI, as on the Master System (a trace shows the runtime entering
; the handler right after it), so the patch's RST $38 path is not taken.
pal0:   push af
        push bc
        push de
        push hl
        exx
        push bc
        push de
        push hl
        ld hl,2155
        exx
        call lsetup
        xor a
        rst $00
        db 5                    ; OUT ($BF),A: CRAM address 0
        ld a,$c0
        rst $00
        db 5
        ld hl,pz32              ; the 32 zeros (cramw): through the traps they cost about 20
        ld b,32                 ; lines with priority, and the line interrupt held meanwhile
        call cramw              ; then came after line 192
        call pace
        exx
        pop hl
        pop de
        pop bc
        exx
        push ix                 ; E = (IX + 31)
        pop hl
        ld de,31
        add hl,de
        call jt_peek
        ld (pe31),a
        ld de,32
        add ix,de               ; IX + 32
        pop hl
        add hl,de               ; HL + 32
        pop de
        ld a,(pe31)
        ld e,a
        pop bc
        ld b,0
        pop af
        xor a                   ; Z: a frame event in this short stretch with interrupts off
        ld (lheld),a            ; stays pending in the Next's interrupt and goes in at the EI
        ret
pe31:   db 0
pz32:   ds 32
; clrl: LDIR (HL to DE, BC bytes) in the Master System's time, 21 T-states a byte (16 for the
; last) and the LD (HL),L before it (7). Returns as LDIR leaves: HL and DE + BC, BC = 0, flags
; of LDIR (P/V clear, H and N clear). Interrupts as they were (off on this path).
clrl:   exx
        push bc
        push de
        push hl
        ld hl,7-5               ; the LD (HL),L, and the last byte's 16
        exx
        push bc
        push de
        push hl
        call lsetup
        pop hl
        pop de
        pop bc
        push bc
        push de
        push hl
        ld de,21                ; 21 a byte
        call lmul
        pop hl
        pop de
        pop bc
        ldir
        call pace
        exx
        pop hl
        pop de
        pop bc
        exx
        ret
; ladd_s: ladd keeping BC, DE, HL and A.
ladd_s: push af
        push bc
        push de
        push hl
        call ladd
        pop hl
        pop de
        pop bc
        pop af
        ret
; palup: the palette upload $436B (CRAM address 0, then the 32 bytes at $D87F, 56 T-states each)
; with cramw, in its Master System time: 96 before the loop with the CALL, 1,787 for the loop, 10
; for the RET. The 32 data writes through the traps took about 20 lines with priority, against 8.
; Returns as the game's code: A = the last byte, B = 0, HL = $D89F, the flags of XOR A.
palup:  push de
        push ix
        exx
        push bc
        push de
        push hl
        ld hl,17+4+11+19+7+11+7+10
        exx
        call lsetup
        call pace               ; the writes start where the loop starts
        xor a
        rst $00
        db 5                    ; OUT ($BF),A: CRAM address 0
        ld a,$C0
        rst $00
        db 5
        ld hl,$D87F
        ld b,32
        call cramw
        exx
        ld hl,1787+10
        exx
        call pace
        exx
        pop hl
        pop de
        pop bc
        exx
        pop ix
        pop de
        ld a,($D89E)
        ld b,a
        xor a
        ld a,b
        ld b,0
        ld hl,$D89F
        ret
; dly: the delay loop $43FD (DEC BC; LD A,B; OR C; JR NZ; RET: 26 T-states a step, the last JR 5
; fewer) in its Master System time, with the CALL: 26 x BC + 22. It times the palette upload
; after it ($4E80, $4919) on the raster; natively it ran about 8 times faster. Returns BC = 0, A = 0
; and the flags of OR C.
dly:    push de
        push hl
        exx
        push bc
        push de
        push hl
        ld hl,22
        exx
        push bc
        call lsetup
        pop bc
        ld e,26
        call lmul
        call pace
        exx
        pop hl
        pop de
        pop bc
        exx
        pop hl
        pop de
        ld bc,0
        xor a
        ret
; ntcopy: the loop at $5D35-$5D43: BC bytes from DE to the VDP at HL, each byte with its own
; address write (DI; CALL $428C; OUT ($BE),A; EI): 137 T-states a byte, the last 5 fewer, on the
; Master System; three traps a byte on the Next, about 10 frames for the 1,536 bytes of a name
; table. It copies the play area into the name table not shown ($3000 or $3800, by $D740), which
; register 2 then shows. Here the bytes go with jt_vwrite, 256 at a time, with interrupts on in
; between; then it waits with interrupts on for the loop's time and the Master System time of the
; handlers that came meanwhile (icredit), as fill43. Returns as the loop leaves: HL and DE + BC,
; BC = 0, A = 0 with Z set, interrupts on.
ntcopy: ld (nc_hl),hl
        ld (nc_de),de
        ld (nc_bc),bc
        exx
        push bc
        push de
        push hl
        ld hl,-5
        exx
        push ix
        push iy
        ld a,($0060)            ; the handler entries so far (see wipe_wait)
        ld (wcl),a
        ld a,($d770)
        ld (wcf),a
        ld hl,$FFFF
        ld (lfr),hl
        call lsetup
        ld bc,(nc_bc)           ; 137 a byte
        ld e,137
        call lmul
.w1:    ld hl,(nc_bc)           ; the writes, 256 at a time
        ld a,h
        or l
        jr z,.wt
        ld bc,256
        ld a,h
        or a
        jr nz,.n
        ld c,l
        ld b,0
.n:     or a
        sbc hl,bc
        ld (nc_bc),hl
        ld a,c                  ; B = bytes (0: 256), C = 1 run
        ld b,a
        ld c,1
        ld hl,(nc_de)
        ld de,(nc_hl)
        ld ix,0
        ld iy,0
        ld a,0
        push bc
        call jt_vwrite
        pop bc
        ld a,b                  ; DE and HL on by the bytes
        or a
        ld de,256
        jr z,.n2
        ld e,a
        ld d,0
.n2:    ld hl,(nc_de)
        add hl,de
        ld (nc_de),hl
        ld hl,(nc_hl)
        add hl,de
        ld (nc_hl),hl
        ei
        call ltick
        jr .w1
.wt:    ld hl,0                 ; the game is in its main code: no handler runs
        ld (W_ISRSP),hl
        ei
        call icredit
        call ltick
        ld hl,(lbudget)
        bit 7,h
        jr nz,.x
        ld a,h
        or l
        jr nz,.wt
.x:     ld hl,0
        ld (W_ISRSP),hl
        pop iy
        pop ix
        exx
        pop hl
        pop de
        pop bc
        exx
        ld hl,(nc_hl)
        ld de,(nc_de)
        ld bc,0
        xor a
        ei
        ret
nc_hl:  dw 0
nc_de:  dw 0
nc_bc:  dw 0
; rdec: the RAM decoder $791B-$7A31 (entered with A = the entry number, HL = the destination),
; as the game's code, in its Master System time: the same header ($D877-$D87E, the $D70F marker),
; the same two modes (0: RLE bytes straight to the destination; any other but 3: RLE into the
; 32-byte buffer at $D857, each full buffer written out row by row, 4 planes 8 bytes apart, by
; $7A09), the same bank steps. Each block adds its T-states (TADD) and the whole is paced at the
; end. The intermissions decode a picture into $C200 with it before each name table copy; natively
; it took a fraction of its time and the act ran 8 frames short. Mode 3 ($77C0: 3 bytes out as 4,
; two 12-bit name table entries) is the intermission pictures' mode. A bank of $20 or more is
; left to the game's code: then the entry returns with carry set and the bank as it found it,
; and the cave runs the original. Returns as the game's code leaves it: the register sets
; swapped by its EXX (the main set is the decoder's: BC = $FFFF, IX = $D877, IY = $D857; the
; alternate set is the caller's, with HL past the output), A and F as its POP AF, the bank put
; back.
rdec:   ld (rd_out),hl          ; the destination (the game's EXX makes it HL')
        ld (rd_bc),bc
        ld (rd_de),de
        ld (rd_idx),a
        ld a,($ffff)            ; the bank to put back (PUSH AF)
        ld (rd_bank),a
        ld a,5
        rst $00
        db $13, $FF             ; LD ($FFFF),A
        ld a,(rd_idx)
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,$8000+6
        add hl,de
        ld a,(hl)               ; the bank and the mode
        add a,5
        cp $20
        jr c,.go
.fb:    ld a,(rd_bank)          ; left to the game's code
        rst $00
        db $13, $FF
        ld a,(rd_idx)
        ld hl,(rd_out)
        ld bc,(rd_bc)
        ld de,(rd_de)
        scf
        ret
.go:    push ix
        push iy
        exx
        push bc
        push de
        push hl
        ld hl,17+49             ; the CALL $791B, its head and the CALL $7929
        exx
        call lsetup
        ld a,($0060)            ; the handler entries so far (see wipe_wait): with interrupts
        ld (wcl),a              ; on their Master System time comes on top (icredit)
        ld a,($d770)
        ld (wcf),a
        ld a,(rd_idx)
        ld l,a
        ld h,$00
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,$8000
        add hl,de
        ld de,$d877
        ld bc,$0008
        ldir
        ld ix,$d877
        ld h,(ix+$00)
        ld l,(ix+$01)
        ld b,(ix+$02)
        ld c,(ix+$03)
        dec bc
        ld e,$20
        ld iy,$d857
        ld a,(ix+$06)
        add a,$05
        rst $00
        db $13, $FF             ; LD ($FFFF),A
        ld a,(hl)
        ld ($d70f),a
        inc hl
        dec bc
        ld a,(ix+$07)
        cp 3
        jp z,.m3
        TADD 519
        or a
        jp nz,.m2
        TADD 10
; mode 0 ($7978): RLE bytes to the destination
.a0:    ld d,(hl)
        inc hl
        dec bc
        ld a,($d70f)
        cp d
        jr z,.r0
        push hl
        ld hl,(rd_out)
        ld (hl),d
        inc hl
        ld (rd_out),hl
        pop hl
        TADD 36+7+21
.c0:    call ladd_s             ; the T-states so far into the budget (HL' holds 16 bits)
        ld a,b
        inc a
        jr z,.e0
        TADD 8+12
        jp .a0
.e0:    TADD 8+7+46
        ld b,(ix+$04)
        ld c,(ix+$05)
        ld a,b
        or c
        jp z,.done
        TADD 5+88
        ld a,($ffff)
        inc a
        rst $00
        db $13, $FF
        ld (ix+$04),$00
        ld (ix+$05),$00
        ld hl,$8000
        jp .a0
.r0:    TADD 36+12+23
        inc hl
        ld d,(hl)
        inc d
        dec hl
.l0:    call ladd_s
        dec d
        jr z,.x0
        ld a,(hl)
        push hl
        ld hl,(rd_out)
        ld (hl),a
        inc hl
        ld (rd_out),hl
        pop hl
        TADD 51
        jr .l0
.x0:    TADD 16+36
        inc hl
        dec bc
        inc hl
        dec bc
        jp .c0
; the other modes ($79BB): RLE into the buffer, written out at each 32 bytes ($7A09)
.m2:    ld d,(hl)
        inc hl
        dec bc
        ld a,($d70f)
        cp d
        jr z,.r2
        TADD 36+7+33+10
        ld (iy+$00),d
        inc iy
        dec e
        call z,.fl
.c2:    call ladd_s             ; the T-states so far into the budget (HL' holds 16 bits)
        ld a,b
        inc a
        jr z,.e2
        TADD 8+12
        jp .m2
.e2:    TADD 8+7+46
        ld b,(ix+$04)
        ld c,(ix+$05)
        ld a,b
        or c
        jp z,.done
        TADD 5+94
        dec bc
        ld a,($ffff)
        inc a
        rst $00
        db $13, $FF
        ld (ix+$04),$00
        ld (ix+$05),$00
        ld hl,$8000
        jp .m2
.r2:    TADD 36+12+23
        inc hl
        ld d,(hl)
        inc d
        dec hl
.l2:    call ladd_s
        dec d
        jr z,.x2
        TADD 4+7+7+19+10+4+10+12
        ld a,(hl)
        ld (iy+$00),a
        inc iy
        dec e
        call z,.fl
        jr .l2
.x2:    TADD 16+36
        inc hl
        dec bc
        inc hl
        dec bc
        jp .c2
; mode 3 ($77C0): RLE into the buffer, each 3 bytes out as 4 ($7812: two 12-bit entries)
.m3:    TADD 519-14+7
        ld e,3
.a3:    ld d,(hl)
        inc hl
        dec bc
        ld a,($d70f)
        cp d
        jr z,.r3
        TADD 36+7+33+10
        ld (iy+$00),d
        inc iy
        dec e
        call z,.o3
.c3:    call ladd_s             ; the T-states so far into the budget (HL' holds 16 bits)
        ld a,b
        inc a
        jr z,.e3
        TADD 8+12
        jp .a3
.e3:    TADD 8+7+46
        ld b,(ix+$04)
        ld c,(ix+$05)
        ld a,b
        or c
        jp z,.done
        TADD 5+107
        dec bc
        ld a,(ix+$06)
        add a,$05
        inc a
        rst $00
        db $13, $FF
        ld (ix+$04),$00
        ld (ix+$05),$00
        ld hl,$8000
        jp .a3
.r3:    TADD 36+12+23
        inc hl
        ld d,(hl)
        inc d
        dec hl
.l3:    call ladd_s
        dec d
        jr z,.x3
        TADD 4+7+7+19+10+4+10+12
        ld a,(hl)
        ld (iy+$00),a
        inc iy
        dec e
        call z,.o3
        jr .l3
.x3:    TADD 16+36
        inc hl
        dec bc
        inc hl
        dec bc
        jp .c3
; $7812 (the CALL taken: 7 more, and 206 for the body): 3 buffer bytes out as 4. E = 3, IY = $D857.
.o3:    TADD 7+206
        push hl
        ld hl,(rd_out)
        ld iy,$d857
        ld a,(iy+$00)
        ld (hl),a
        inc hl
        ld a,(iy+$02)
        and $0f
        ld (hl),a
        inc hl
        ld a,(iy+$01)
        ld (hl),a
        inc hl
        ld a,(iy+$02)
        srl a
        srl a
        srl a
        srl a
        ld (hl),a
        inc hl
        ld (rd_out),hl
        pop hl
        ld e,3
        ret
; $7A09 (the CALL taken: 7 more than not taken, and 1,284 for the body): the buffer out, row by
; row, the 4 planes 8 bytes apart. Keeps BC, D, HL; E = $20, IY = $D857.
.fl:    TADD 7+1284
        push bc
        push hl
        ld hl,(rd_out)
        ld iy,$d857
        ld b,8
.fr:    ld a,(iy+$00)
        ld (hl),a
        inc hl
        ld a,(iy+$08)
        ld (hl),a
        inc hl
        ld a,(iy+$10)
        ld (hl),a
        inc hl
        ld a,(iy+$18)
        ld (hl),a
        inc hl
        inc iy
        djnz .fr
        ld (rd_out),hl
        pop hl
        pop bc
        ld e,$20
        ld iy,$d857
        ret
.done:  TADD 11+33              ; the RET Z, then POP AF, LD ($FFFF),A and the RET of $791B
        call ladd_s
.dw:    call icredit            ; the wait, with the handlers' time added
        call ltick
        ld hl,(lbudget)
        bit 7,h
        jr nz,.dx
        ld a,h
        or l
        jr nz,.dw
.dx:
        exx
        pop hl
        pop de
        pop bc
        exx
        ld (rd_fbc),bc          ; the decoder's main set, for the swap
        ld (rd_fde),de
        ld (rd_fhl),hl
        pop iy
        pop ix
        ld a,(rd_bank)          ; POP AF; LD ($FFFF),A: the bank back
        rst $00
        db $13, $FF
        exx                     ; the swap of the game's EXX: the alternate set gets the
        ld bc,(rd_bc)           ; caller's registers, HL past the output
        ld de,(rd_de)
        ld hl,(rd_out)
        exx
        ld bc,(rd_fbc)
        ld de,(rd_fde)
        ld hl,(rd_fhl)
        ld ix,$d877
        ld a,(rd_bank)
        or a                    ; carry clear
        ret
rd_out: dw 0
rd_bc:  dw 0
rd_de:  dw 0
rd_fbc: dw 0
rd_fde: dw 0
rd_fhl: dw 0
rd_idx: db 0
rd_bank: db 0
; cramw: B bytes (1-32) from HL (as mapped now) to CRAM, as the runtime's data port writes with
; VDP code 3 do (cram_block, cram_set, pal_out, cram_x; fw.asm, fw2.asm), in about a tenth of
; their time: for each byte at CRAM index vdp_addr & 31, the colour (low 6 bits) into cram, into
; the first tilemap palette (index e), for e 16-31 into the first sprite palette (e - 16), and with
; priority (fw_flags bit 0) for e & 15 not 0 into the first Layer 2 palette (e); the palette
; values from pal_hi_table and pal_lo_table, NextReg $43 with the display bits of pal43. Then
; vdp_addr steps by B, the latch is clear, vdp_rbuf holds the last byte, and fallback_update runs
; once, as after an OTIR. With toppal (fw_flags bit 1) it goes through the I/O RST (OTIR)
; instead: the second palettes and pal_vm are not done here. Interrupts off while it runs.
; Runtime internals (build/rt/runtime.map): cram $E04D, pal43 $E09F, pal_hi_table $E300,
; pal_lo_table $E340, fw_flags $E09E, vdp_addr $E037, vdp_latch $E035, vdp_rbuf $E039,
; fallback_update $F582 (calls fallback2 in fw2 through fw2_call, which puts back the page in
; slot 1 from cur_mmu + 1: this code page while an entry runs). Uses A, BC, DE, HL.
C_CRAM  equ $E04D
C_PAL43 equ $E09F
C_PHI   equ $E300
C_PLO   equ $E340
C_FLAGS equ $E09E
C_ADDR  equ $E037
C_LATCH equ $E035
C_RBUF  equ $E039
C_FBUP  equ $F582
cramw:  ld a,(C_FLAGS)
        and 2
        jr z,.go
        ld c,$BE                ; toppal: the runtime's OTIR
        rst $00
        db $B3
        ret
.go:    ld a,i
        push af
        di
.b:     ld a,(hl)
        ld (C_RBUF),a
        and $3F
        ld c,a                  ; C = the colour
        ld a,(C_ADDR)
        and $1F
        ld e,a                  ; E = the index
        push hl
        ld hl,C_CRAM
        add hl,a
        ld (hl),c
        ld a,c                  ; D = pal_hi, the high byte; L = pal_lo
        add a,C_PHI&255
        ld l,a
        ld h,C_PHI>>8
        ld d,(hl)
        ld a,c
        add a,C_PLO&255
        ld l,a
        ld h,C_PLO>>8
        ld l,(hl)
        ld a,(C_PAL43)
        or %00110000            ; the first tilemap palette
        nextreg $43,a
        ld a,e
        nextreg $40,a
        ld a,d
        nextreg $44,a
        ld a,l
        nextreg $44,a
        ld a,e
        cp 16
        jr c,.l2
        ld a,(C_PAL43)
        or %00100000            ; the first sprite palette
        nextreg $43,a
        ld a,e
        sub 16
        nextreg $40,a
        ld a,d
        nextreg $44,a
        ld a,l
        nextreg $44,a
.l2:    ld a,(C_FLAGS)
        rra
        jr nc,.n
        ld a,e
        and $0F
        jr z,.n
        ld a,(C_PAL43)
        or %00010000            ; the first Layer 2 palette
        nextreg $43,a
        ld a,e
        nextreg $40,a
        ld a,d
        nextreg $44,a
        ld a,l
        nextreg $44,a
.n:     pop hl
        inc hl
        push hl
        ld hl,(C_ADDR)
        inc hl
        res 6,h
        ld (C_ADDR),hl
        pop hl
        djnz .b
        xor a
        ld (C_LATCH),a
        push hl
        call C_FBUP
        pop hl
        pop af
        ret po
        ei
        ret
; ladd_bc: BC T-states into the budget, with HL' (which keeps the remainder). Uses A, BC, DE, HL.
ladd_bc:
        push bc
        exx
        pop de
        add hl,de
        exx
        jp ladd
; lmul: BC x E T-states (BC = 0: 65536) into the budget, with HL' (which keeps the remainder),
; in at most 511 steps: a loop that counts byte by byte took over a frame for 5,376 bytes, and
; ltick cannot see more than one frame wrap between two calls. Uses A, BC, DE, HL.
lmul:   ld d,0
        ld a,b
        or c
        jr nz,.nz
        ld h,e                  ; 65536: 256 x (E x 256)
        ld l,0
        jr .hi
.nz:    ld a,b
        or a
        jr z,.lo
        ld h,e                  ; B x (E x 256)
        ld l,0
.hi:    call .add
        djnz .hi
.lo:    ld a,c                  ; C x E
        or a
        ret z
        ld b,a
        ld l,e
        ld h,0
.l:     call .add
        djnz .l
        ret
.add:   push bc
        push de
        push hl
        push hl
        exx
        pop de
        add hl,de
        exx
        call ladd
        pop hl
        pop de
        pop bc
        ret
; clrb: the loop at $013D: BC zero bytes from HL, 39 T-states a byte (34 for the last). Returns
; with HL + BC, BC = 0, A = 0 and the flags of OR C (Z set). The loop clears $C000-$DFEE, which
; holds this call's own stack frames below the game's SP ($DED0); those bytes are not cleared.
clrb:   exx
        push bc
        push de
        push hl
        ld hl,0
        exx
        ld (cb_hl),hl
        ld (cb_bc),bc
        push de                 ; the game's DE
        call lsetup
        ld bc,(cb_bc)           ; T = 39 a byte, 34 for the last
        ld de,39
        call lmul
        exx
        ld de,-5
        add hl,de
        exx
        ld (csp),sp             ; clear [HL, HL + BC) but not this call's own stack frames,
        ld hl,(cb_hl)           ; [SP, $DED0): they are below the game's SP and the game
        ld bc,(cb_bc)           ; writes them before it reads them
.l:     ld a,b
        or c
        jr z,.e
        push hl
        ld de,(csp)
        or a
        sbc hl,de
        pop hl
        jr c,.z
        push hl
        ld de,$DED0
        or a
        sbc hl,de
        pop hl
        jr c,.k
.z:     ld (hl),0
.k:     inc hl
        dec bc
        ld a,c                  ; every 256 bytes: count the lines, and a V counter read
        or a                    ; (as pace), so the runtime's first once-a-frame work (about
        jr nz,.l                ; 2.5 frames at power-on) runs inside the loop's time and
        push hl                 ; not after it
        push bc
        rst $00
        db $0A
        call ltick
        pop bc
        pop hl
        jr .l
.e:     call pace
        pop de
        exx
        pop hl
        pop de
        pop bc
        exx
        ld hl,(cb_hl)
        ld bc,(cb_bc)
        add hl,bc               ; HL + BC
        ld bc,0
        xor a
        ret
cb_hl:  dw 0
cb_bc:  dw 0
csp:    dw 0
; fill43: as $4361-$436A: L = A, BC (1 to 65536) bytes of A from DE. Returns DE + BC, BC = 0,
; A = 0 with Z set (the loop's OR C), L = the fill byte, H kept. Interrupts stay as they were (on
; at $2AC3): the game's handlers run while it waits, and their Master System time is added.
fill43: ld l,a
        ld (fl_bc),bc
        ld (fl_de),de
        ld (fl_hl),hl
        exx
        push bc
        push de
        push hl
        exx
        ld a,($0060)            ; the handler entries so far (see wipe_wait)
        ld (wcl),a
        ld a,($d770)
        ld (wcf),a
        ld hl,$FFFF
        ld (lfr),hl
        call lsetup
        exx
        ld hl,17+4+10-5         ; the CALL, LD L,A and the RET; the last JR 5 fewer
        exx
        ld bc,(fl_bc)           ; T = 43 a byte
        ld de,43
        call lmul
        ld bc,(fl_bc)           ; the fill: (DE) = A, BC times, as the game's loop
        ld de,(fl_de)
        ld hl,(fl_hl)
.f:     ld a,l
        ld (de),a
        inc de
        dec bc
        ld a,c                  ; every 256 bytes: count the lines, so no frame wrap
        or a                    ; is missed
        jr nz,.f2
        push bc
        push de
        push hl
        call ltick
        pop hl
        pop de
        pop bc
.f2:    ld a,b
        or c
        jr nz,.f
        ld (fl_de),de
.w:     ld hl,0                 ; the game is in its main code: no handler runs
        ld (W_ISRSP),hl
        call icredit
        call ltick
        ld hl,(lbudget)
        bit 7,h
        jr nz,.x
        ld a,h
        or l
        jr nz,.w
.x:     ld hl,0
        ld (W_ISRSP),hl
        exx
        pop hl
        pop de
        pop bc
        exx
        ld de,(fl_de)
        ld hl,(fl_hl)
        ld bc,0
        xor a
        ret
fl_bc:  dw 0
fl_de:  dw 0
fl_hl:  dw 0
; lcl: DE = a line entry's Master System time. The sound driver takes 1,470 T-states more while
; the music sequencer runs ($D9E7 not 0, tested at $1C81): measured on the reference, 2,752 a
; line entry without music (mostly), 4,222 on average with it (4,008 to 11,074). Uses A.
lcl:    ld de,2361+23
        ld a,($d9e7)
        or a
        ret z
        ld de,2361+23+1470
        ret
; icredit: the game's handlers since wcl/wcf were taken: their Master System time into the
; budget (line entry 2,384 T-states, 3,854 with the music on (lcl), frame entry 443). Uses A, BC,
; DE, HL; HL' kept.
icredit:
        exx
        push hl
        ld hl,0
        exx
        ld a,($0060)
        ld hl,wcl
        ld b,(hl)
        ld (hl),a
        sub b
        jr z,.nl
        ld b,a
.l:     exx
        call lcl
        add hl,de
        exx
        djnz .l
.nl:    ld a,($d770)
        ld hl,wcf
        ld b,(hl)
        ld (hl),a
        sub b
        jr z,.nf
        ld b,a
.f:     exx
        ld de,420+23
        add hl,de
        exx
        djnz .f
.nf:    call ladd
        exx
        pop hl
        exx
        ret
; tq ($2457): HL = the source (the bank paged in at $8000), 64 bytes to VRAM from the VDP address,
; as LD B,$40 and the OUTI loop. Returns HL + 64, B = 0; DE, C, IX, IY and the alternate registers
; kept. Runs with interrupts off on its own stack; the patch turns them on again.
tq:     di
        ld (tq_sp),sp
        ld sp,tq_top
        push de
        push ix
        push iy
        push hl
        ld de,($E037)           ; vdp_addr
        ld b,64
        ld c,1
        ld ix,0
        ld iy,0
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop hl
        ld de,64
        add hl,de
        pop iy
        pop ix
        pop de
        ld b,0
        ld c,$be                ; C as the game's loop leaves it
        ld sp,(tq_sp)
        ret
tq_sp:  dw 0
        ds 32
tq_top:
; vrow, vtile, vfill, vstep: the VRAM loops of act 1's second scene (patches at $5F57, $5F8B, $5FAE
; and $5E9A). Each loop writes VRAM with an address write per row or word, interrupts off for the
; writes and on between them. The start entry takes the loop's registers, adds the loop's Master
; System time to a new budget, and writes the first 256 bytes; vstep writes the next 256 at each
; call, then waits out the budget and the Master System time of the game's handlers that ran in
; the patch's windows (icredit). NZ: call vstep again after a window; Z: done, with the registers
; the game's loop leaves. The entries run with interrupts off on the stack v_top; the remainder of
; the T-state count (HL' for ladd) is kept in v_rem between calls, and the game's alternate
; registers and IY are put back at the end.
; vrow ($5F57): HL = the VRAM address, IX = the source, B = rows of 64 bytes. 3,198 T-states a row
; (the last DJNZ 5 fewer). Leaves HL and IX on by the bytes, B = C = 0, A = H, Z set.
vrow:   di
        ld (v_sp),sp
        ld sp,v_top
        call vsave
        ld (v_dst),hl
        ld (v_src),ix
        ld l,b
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld (v_n),hl
        ld a,b                  ; BC = rows x 13: x 246 = x 3,198
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl               ; x 8
        ld e,a
        ld d,0
        add hl,de               ; x 9
        add hl,de
        add hl,de
        add hl,de               ; x 13
        ld b,h
        ld c,l
        ld e,246
        xor a
        jr vbeg
; vtile ($5F8B): IX = the source, HL = the VRAM address, BC = words. 199 T-states a word. Leaves
; HL and IX on by the bytes, BC = 0, A = 0 with Z set.
vtile:  di
        ld (v_sp),sp
        ld sp,v_top
        call vsave
        ld (v_dst),hl
        ld (v_src),ix
        ld h,b
        ld l,c
        add hl,hl
        ld (v_n),hl
        ld e,199
        ld a,1
        jr vbeg
; vfill ($5FAE, $5E9A): HL = the VRAM address, BC = words of E then D. 168 T-states a word.
; Leaves HL on by the bytes, BC = 0, A = 0 with Z set, DE and IX as they were.
vfill:  di
        ld (v_sp),sp
        ld sp,v_top
        call vsave
        ld (v_dst),hl
        ld (v_ix),ix
        ld (v_pair),de
        ld h,b
        ld l,c
        add hl,hl
        ld (v_n),hl
        ld hl,lbuf              ; the pattern, 128 x E, D, in the loader's buffer (free here)
        ld a,128
.p:     ld (hl),e
        inc hl
        ld (hl),d
        inc hl
        dec a
        jr nz,.p
        ld e,168
        ld a,2
; vbeg: A = the kind (0 vrow, 1 vtile, 2 vfill), BC x E = the loop's T-states, less 5 for its
; last JR or DJNZ. A new budget from now.
vbeg:   ld (v_kind),a
        push bc
        push de
        exx
        ld hl,-5
        exx
        ld a,($0060)            ; the handler entries so far (see wipe_wait)
        ld (wcl),a
        ld a,($d770)
        ld (wcf),a
        ld hl,$FFFF
        ld (lfr),hl
        call lsetup
        pop de
        pop bc
        call lmul
        exx
        ld (v_rem),hl
        exx
        jr vbody
; vstep: the next 256 bytes, or the wait (see above).
vstep:  di
        ld (v_sp),sp
        ld sp,v_top
vbody:  ld hl,0                 ; no handler runs now: one that ran in the window left isr_sp
        ld (W_ISRSP),hl         ; in its stack frames (see spsw)
        exx
        ld hl,(v_rem)
        exx
        ld hl,(v_n)
        ld a,h
        or l
        jr z,.wait
        ld bc,256
        ld a,h
        or a
        jr nz,.c
        ld c,l
        ld b,0
.c:     or a
        sbc hl,bc
        ld (v_n),hl
        ld (v_k),bc
        ld de,(v_dst)
        ld a,(v_kind)
        cp 2
        jr z,.f
        ld b,c                  ; B = bytes (0: 256), C = 1 run
        ld c,1
        ld hl,(v_src)
        ld ix,0
        ld iy,0
        xor a                   ; the source as the game sees it
        call jt_vwrite
        jr .adv
.f:     ld b,c                  ; one run from the pattern buffer: jt_vwrite takes a run of
        ld c,1                  ; 2-byte runs one at a time, about 0.7 frames for 256 bytes
        ld hl,lbuf
        ld ix,0
        ld iy,0
        ld a,1                  ; the source is this page
        call jt_vwrite
.adv:   ld de,(v_k)
        ld hl,(v_src)
        add hl,de
        ld (v_src),hl
        ld hl,(v_dst)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (v_dst),hl
        call ltick
        jr .nz
.wait:  call icredit
        call ltick
        ld hl,(lbudget)
        bit 7,h
        jr nz,.done
        ld a,h
        or l
        jr z,.done
.nz:    exx
        ld (v_rem),hl
        exx
        ld iy,(v_iy)
        or 1                    ; NZ: again after a window
        ld sp,(v_sp)
        ret
.done:  xor a
        ld (lheld),a            ; the windows took the interrupts
        ld hl,0
        ld (W_ISRSP),hl
        exx                     ; the game's alternate registers
        ld bc,(v_bc2)
        ld de,(v_de2)
        ld hl,(v_hl2)
        exx
        ld iy,(v_iy)
        ld a,(v_kind)
        or a
        jr nz,.d1
        ld hl,(v_dst)           ; vrow
        ld ix,(v_src)
        ld bc,0
        ld a,h
        cp a                    ; Z for the patch (the game's flags here are not read)
        ld sp,(v_sp)
        ret
.d1:    dec a
        jr nz,.d2
        ld hl,(v_dst)           ; vtile
        ld ix,(v_src)
        ld bc,0
        xor a
        ld sp,(v_sp)
        ret
.d2:    ld hl,(v_dst)           ; vfill
        ld ix,(v_ix)
        ld de,(v_pair)
        ld bc,0
        xor a
        ld sp,(v_sp)
        ret
; vsave: the game's alternate registers and IY. Uses nothing else.
vsave:  ld (v_iy),iy
        exx
        ld (v_bc2),bc
        ld (v_de2),de
        ld (v_hl2),hl
        exx
        ret
v_kind: db 0
v_n:    dw 0
v_k:    dw 0
v_src:  dw 0
v_dst:  dw 0
v_pair: dw 0
v_ix:   dw 0
v_iy:   dw 0
v_rem:  dw 0
v_bc2:  dw 0
v_de2:  dw 0
v_hl2:  dw 0
v_sp:   dw 0
        ds 96
v_top:
endpage
page 1 pdraw ptiles
        OPT --zxnext
; Page 1: the Layer 2 drawing of priority cells (pdraw, ptiles), entered from page 0 with jt_far.
; It calls page 0's ltick with jt_far.
W_SHADOW	equ 28
W_TILES		equ 10
W_FW2		equ 25
W_CURMMU	equ $E02D
W_FARPREV	equ $E0AF		; far_prev: slot 1's page before the far call that runs now
; pdraw: Layer 2 for the cells that name table writes have marked, as the runtime's pri_frame
; marked-cells pass (pri_rowcells, pri_cell, pri_put, pri_tile; fw2.asm) would draw them in the
; next vertical blank, here with interrupts off. Each cell drawn has its mark cleared, so the
; runtime draws it no more. The code is the Ninja Gaiden overlay's (pdraw, pcell), without its
; queue. Left to the runtime: everything when the priority switch is off, in 224-line mode, with
; a whole Layer 2 rebuild pending (pri_full), or with the name table below VRAM $2000. Runtime
; internals (build/rt/runtime.map):
;   MAP_PAGE 14 (slot 0 here): row "has priority cells" $1BC0 + row, row "marked" $1BE0 + row,
;     cell marks $1C00 + cell (bit 0 marked, bit 1 Layer 2 holds the cell);
;   L2_PAGE 102-107: Layer 2, 32 lines of 256 bytes a page (slot 3 here);
;   SHADOW_PAGE+1 29 (slot 2), TILE_PAGE 10, 11 (slots 4-5, $8000 + tile * 32);
;   FW2_PAGE 25 (slot 5 at $A000 to copy): pri_full $3469, pri_v $346B, pri_ys $346D,
;     pri_lf $3478 (192 bytes) and pri_tiles $3538 (64 bytes), copied in and back;
;   part 1: nt_base $E04B, m224 $E08F, fw_flags $E09E (bit 0: priority), cur_mmu $E02D.
P_MAP     equ 14
P_L2      equ 102
P_FULL    equ $A000+$1469
P_V       equ $A000+$146B
P_YS      equ $A000+$146D
P_LF      equ $A000+$1478       ; pri_lf, then pri_tiles 192 bytes on
P_M224    equ $E08F
P_FLAGS   equ $E09E
P_NTB     equ $E04B
pdraw:  ld a,(P_FLAGS)
        rra
        ret nc
        ld a,(P_M224)
        or a
        ret nz
        ld a,(P_NTB+1)
        cp $20
        ret c
        ld a,i
        push af
        di
        nextreg $55,W_FW2
        ld a,(P_FULL)
        or a
        jr nz,.back             ; a whole rebuild draws them all
        ld a,(P_V)
        ld (p_v),a
        ld a,(P_YS)
        ld (p_ys),a
        ld hl,P_LF
        ld de,p_lf
        ld bc,256
        ldir
        nextreg $50,P_MAP
        nextreg $52,W_SHADOW+1
        nextreg $54,W_TILES
        nextreg $55,W_TILES+1
        ld a,$FF
        ld (p_pg),a
        ld (c_th),a             ; no tile converted yet (the tiles may have changed)
        ld b,0                  ; each marked row
.r:     ld a,b
        add a,$E0
        ld l,a
        ld h,$1B
        ld a,(hl)
        or a
        jr z,.rn
        ld (hl),0
        push bc
        call prow
        ld a,(W_CURMMU+0)       ; count the lines (ltick, page 0, reads $0060 in slot 0), so no
        nextreg $50,a           ; frame wrap is missed
        call jt_far
        db pg_ltick, ent_ltick
        nextreg $50,P_MAP
        pop bc
.rn:    inc b
        ld a,b
        cp 28
        jr nz,.r
        nextreg $55,W_FW2
        ld hl,p_lf
        ld de,P_LF
        ld bc,256
        ldir
.back:  ld a,(W_CURMMU+0)
        nextreg $50,a
        ld a,(W_CURMMU+2)
        nextreg $52,a
        ld a,(W_CURMMU+3)
        nextreg $53,a
        ld a,(W_CURMMU+4)
        nextreg $54,a
        ld a,(W_CURMMU+5)
        nextreg $55,a
        pop af
        ret po
        ei
        ret
; ptiles: the Layer 2 cells of the priority tiles that this wipe step changed (wpb, from wbook):
; the step zeroes one row of each tile (row (first address & 31) / 4), so in each cell that
; Layer 2 holds (mark bit 1) whose name table entry has the priority bit and one of the tiles,
; that row's line is drawn again from the tile (pline), as the runtime's pri_redraw would draw
; the whole cell in the next vertical blank. The runtime's redraw of every cell of those tiles
; took about 1.7 frames a step, and redrawing whole cells here 1.2: the level end wipe ran 16
; and then 8 frames late. Same runtime internals as pdraw. Entered from page 0 (ptiles0) with HL = page
; 0's wpb and A = the step's first VRAM address (wstart, low byte); the copy is made with page 0
; in slot 2: far_prev ($E0AF) names it while this far call runs.
ptiles: ld (p_ws),a
        ld a,i                  ; page 0's wpb (HL, in page 0) into this page's copy: page 0
        push af                 ; (far_prev while this call runs) in slot 2 for the copy
        di
        ld a,(W_FARPREV)
        nextreg $52,a
        ld de,$2000
        add hl,de
        ld de,wpb
        ld bc,64
        ldir
        ld a,(W_CURMMU+2)
        nextreg $52,a
        pop af
        jp po,.wc
        ei
.wc:    ld a,(P_FLAGS)
        rra
        ret nc
        ld a,(P_M224)
        or a
        ret nz
        ld a,(P_NTB+1)
        cp $20
        ret c
        ld a,(p_ws)             ; the tile row of this step
        and $1F
        rrca
        rrca
        ld (p_k),a
        ld a,i
        push af
        di
        push ix
        nextreg $55,W_FW2
        ld a,(P_FULL)
        or a
        jp nz,.back
        ld a,(P_V)
        ld (p_v),a
        ld a,(P_YS)
        ld (p_ys),a
        ld hl,P_LF
        ld de,p_lf
        ld bc,192
        ldir
        nextreg $50,P_MAP
        nextreg $52,W_SHADOW+1
        nextreg $54,W_TILES
        nextreg $55,W_TILES+1
        ld a,$FF
        ld (p_pg),a
        ld hl,(P_NTB)           ; DE = the entries in the copy (+ $2000), HL = the marks
        ld de,$2000
        add hl,de
        ex de,hl
        ld hl,$1C00
        ld bc,0                 ; C = the cell's column, B = its row
.c:     bit 1,(hl)
        jr z,.cn
        inc de
        ld a,(de)
        dec de
        bit 4,a
        jr z,.cn
        push bc
        push hl
        and 1                   ; wpb: byte tile >> 3, bit tile & 7
        rrca
        rrca
        rrca
        ld l,a
        ld a,(de)
        rrca
        rrca
        rrca
        and $1F
        or l
        ld hl,wpb
        add hl,a
        ld a,(de)
        and 7
        ld b,a
        ld a,(hl)
        inc b
.sh:    dec b
        jr z,.tb
        rrca
        jr .sh
.tb:    rrca
        jr nc,.cp
        pop hl
        pop bc
        push bc
        push hl
        push de
        ld a,b
        ld (p_r),a
        ld a,c
        ld (p_c),a
        ld a,(de)
        ld (p_tl),a
        inc de
        ld a,(de)
        ld (p_th),a
        call pline
        pop de
.cp:    pop hl
        pop bc
.cn:    inc hl
        inc de
        inc de
        inc c
        ld a,c
        cp 32
        jr nz,.c
        ld c,0
        inc b
        ld a,b
        cp 28
        jr nz,.c
        nextreg $55,W_FW2
        ld hl,p_lf
        ld de,P_LF
        ld bc,192
        ldir
.back:  ld a,(W_CURMMU+0)
        nextreg $50,a
        ld a,(W_CURMMU+2)
        nextreg $52,a
        ld a,(W_CURMMU+3)
        nextreg $53,a
        ld a,(W_CURMMU+4)
        nextreg $54,a
        ld a,(W_CURMMU+5)
        nextreg $55,a
        pop ix
        pop af
        ret po
        ei
        ret
; pline: cell (p_r, p_c) with entry (p_tl, p_th): the line of tile row p_k (7 - p_k with V flip)
; into Layer 2 when it is on screen, from the tile definitions, as pri_put does.
pline:  ld a,(p_k)
        ld e,a
        ld a,(p_th)
        bit 2,a
        ld a,e
        jr z,.nv
        xor 7
.nv:    ld d,a                  ; D = the line in the cell
        ld a,(p_r)
        add a,a
        add a,a
        add a,a
        add a,d
        ld hl,p_v
        sub (hl)
        jr nc,.y
        add a,224
.y:     cp 192
        ret nc
        ld hl,p_ys
        add a,(hl)
        jr c,.w
        cp 192
        jr c,.l
.w:     sub 192
.l:     ld e,a                  ; the Layer 2 line
        ld hl,p_lf
        add hl,a
        ld (hl),1
        ld a,e
        rlca
        rlca
        rlca
        and 7
        add a,P_L2
        ld hl,p_pg
        cp (hl)
        jr z,.sp
        ld (hl),a
        nextreg $53,a
.sp:    ld a,e
        and $1F
        or $60
        ld d,a
        ld a,(p_c)
        add a,a
        add a,a
        add a,a
        ld e,a                  ; DE = the destination
        ld a,(p_th)
        and 1
        ld h,a
        ld a,(p_tl)
        ld l,a
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld a,(p_k)
        add a,a
        add a,a
        add hl,a
        ld a,h
        add a,$80
        ld h,a                  ; HL = the tile row in the definitions
        ld a,(p_th)
        and 8
        add a,a
        ld c,a                  ; $10: the sprite palette
        ld a,(p_th)
        and 2
        jr nz,.hf
        REPT 4
        ld a,(hl)
        swapnib
        and $0F
        or c
        ld (de),a
        inc e
        ld a,(hl)
        and $0F
        or c
        ld (de),a
        inc e
        inc hl
        ENDR
        ret
.hf:    inc hl
        inc hl
        inc hl
        REPT 4
        ld a,(hl)
        and $0F
        or c
        ld (de),a
        inc e
        ld a,(hl)
        swapnib
        and $0F
        or c
        ld (de),a
        inc e
        dec hl
        ENDR
        ret
p_k:    db 0
p_ws:   db 0
wpb:    ds 64              ; a copy of page 0's wpb (see ptiles)
; prow: B = row: each marked cell (pri_rowcells)
prow:   ld a,b
        ld (p_r),a
        ld l,b
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,$1C00
        add hl,de
        ld c,0
.c:     bit 0,(hl)
        jr z,.n
        res 0,(hl)
        push hl
        push bc
        ld a,c
        ld (p_c),a
        call pcell
        pop bc
        pop hl
.n:     inc hl
        inc c
        ld a,c
        cp 32
        jr nz,.c
        ret
; pcell: cell (p_r, p_c), HL = its mark (pri_cell)
pcell:  push hl
        ld a,(p_r)              ; the entry in the copy: nt_base + 64 r + 2 c, at + $2000
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld a,(p_c)
        add a,a
        add hl,a
        ld de,(P_NTB)
        add hl,de
        ld a,h
        add a,$20
        ld h,a
        ld a,(hl)
        ld (p_tl),a
        inc hl
        ld a,(hl)
        ld (p_th),a
        pop hl
        and $10
        jr nz,.p
        bit 1,(hl)
        ret z                   ; Layer 2 holds nothing of it
        res 1,(hl)
        jp .lines
.p:     set 1,(hl)
        ld a,(p_tl)             ; pri_tiles: byte (tile >> 3), bit (tile & 7)
        rrca
        rrca
        rrca
        and $1F
        ld e,a
        ld a,(p_th)
        and 1
        rrca
        rrca
        rrca
        or e
        ld hl,p_lf+192
        add hl,a
        ld a,(p_tl)
        and 7
        ld b,a
        ld a,1
        jr z,.b0
.bs:    add a,a
        djnz .bs
.b0:    or (hl)
        ld (hl),a
        ld a,(p_c)
        add a,a
        add a,a
        add a,a
        ld (p_x),a
        ld a,(p_tl)             ; the cell's 8 rows of pixels, converted once for each tile and
        ld hl,c_tl              ; attribute (c_tl, c_th) into cbuf: every border cell is $6E
        cp (hl)                 ; with the priority bit, so the 112 cells convert once
        jr nz,.cv
        ld a,(p_th)
        inc hl
        cp (hl)
        jp z,.have
.cv:    ld a,(p_tl)
        ld (c_tl),a
        ld a,(p_th)
        ld (c_th),a
        and 1
        ld h,a
        ld a,(p_tl)
        ld l,a
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld a,h
        add a,$80
        ld h,a                  ; the tile in the definitions
        ld a,(p_th)
        ld b,a
        ld de,4
        bit 2,b                 ; V flip: from the last row up
        jr z,.nv
        ld de,28
        add hl,de
        ld de,-4
.nv:    ld (p_step),de
        ld a,b
        and 8
        add a,a
        ld c,a                  ; $10: the sprite palette
        ld a,b
        and 2
        ld (p_hf),a
        ld de,cbuf
        ld b,8
.cr:    push bc
        push hl
        ld a,(p_hf)
        or a
        jr nz,.hf
        REPT 4
        ld a,(hl)
        swapnib
        and $0F
        or c
        ld (de),a
        inc de
        ld a,(hl)
        and $0F
        or c
        ld (de),a
        inc de
        inc hl
        ENDR
        jr .cn
.hf:    inc hl
        inc hl
        inc hl
        REPT 4
        ld a,(hl)
        and $0F
        or c
        ld (de),a
        inc de
        ld a,(hl)
        swapnib
        and $0F
        or c
        ld (de),a
        inc de
        dec hl
        ENDR
.cn:    pop hl
        push de
        ld de,(p_step)
        add hl,de
        pop de
        pop bc
        dec b
        jp nz,.cr
.have:  ld a,(p_r)              ; the map line of the cell's top, on screen: y0
        add a,a
        add a,a
        add a,a
        ld hl,p_v
        sub (hl)
        jr nc,.f0
        add a,224
.f0:    cp 192-7                ; all 8 lines on screen, on 8 Layer 2 lines in a row in one
        jp nc,.slow             ; page: 8 bytes a line straight from cbuf
        ld hl,p_ys
        add a,(hl)
        jr c,.fw
        cp 192
        jr c,.f1
.fw:    sub 192
.f1:    cp 192-7
        jp nc,.slow
        ld e,a
        and $1F
        cp 32-7
        jp nc,.slow
        ld a,e
        ld hl,p_lf
        add hl,a
        ld b,8
.f2:    ld (hl),1
        inc hl
        djnz .f2
        ld a,e
        rlca
        rlca
        rlca
        and 7
        add a,P_L2
        ld hl,p_pg
        cp (hl)
        jr z,.f3
        ld (hl),a
        nextreg $53,a
.f3:    ld a,e
        and $1F
        or $60
        ld d,a
        ld a,(p_x)
        ld e,a
        ld ixl,a
        ld hl,cbuf
        REPT 8
        ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        ldi
        ld a,e                  ; LDI carries into D when column 31 ends at E = 0: then D
        cp 1                    ; is on the next line already
        ld a,d
        sbc a,$FF
        ld d,a
        ld e,ixl
        ENDR
        ret
.slow:  ld hl,cbuf              ; per line: the Layer 2 line of its map line, 8 bytes
        ld (p_src),hl
        ld a,(p_r)
        add a,a
        add a,a
        add a,a
        ld hl,p_v
        sub (hl)
        jr nc,.y0
        add a,224
.y0:    ld b,8
.ln:    ld (p_y),a
        cp 192
        jr nc,.sk
        ld hl,p_ys
        add a,(hl)
        jr c,.wr
        cp 192
        jr c,.ok
.wr:    sub 192
.ok:    ld e,a                  ; the Layer 2 line
        ld hl,p_lf
        add hl,a
        ld (hl),1
        ld a,e
        rlca
        rlca
        rlca
        and 7
        add a,P_L2
        ld hl,p_pg
        cp (hl)
        jr z,.sp
        ld (hl),a
        nextreg $53,a
.sp:    ld a,e
        and $1F
        or $60
        ld d,a
        ld a,(p_x)
        ld e,a
        ld hl,(p_src)
        push bc
        REPT 8
        ldi
        ENDR
        pop bc
.sk:    ld hl,(p_src)
        ld de,8
        add hl,de
        ld (p_src),hl
        ld a,(p_y)
        inc a
        cp 224
        jr c,.yy
        xor a
.yy:    djnz .ln
        ret
.lines: ld a,(p_r)
        add a,a
        add a,a
        add a,a
        ld e,a                  ; map line of the cell's top
        ld d,0                  ; line in the cell
.k:     ld a,e
        add a,d
        ld hl,p_v
        sub (hl)
        jr nc,.y
        add a,224
.y:     cp 192
        jr nc,.nx
        ld hl,p_ys
        add a,(hl)
        jr c,.w
        cp 192
        jr c,.l
.w:     sub 192
.l:     ld (p_l),a              ; Layer 2 line
        push de
        ld hl,p_lf
        add hl,a
        ld a,(hl)
        or a
        call nz,pzero
        pop de
.nx:    inc d
        ld a,d
        cp 8
        jr nz,.k
        ret
; pzero: the cell's 8 bytes on Layer 2 line p_l to 0 (its page in slot 3)
pzero:  ld a,(p_l)
        rlca
        rlca
        rlca
        and 7
        add a,P_L2
        ld hl,p_pg
        cp (hl)
        jr z,.s
        ld (hl),a
        nextreg $53,a
.s:     ld a,(p_l)
        and $1F
        or $60
        ld d,a
        ld a,(p_c)
        add a,a
        add a,a
        add a,a
        ld e,a
        xor a
        ld b,8
.z:     ld (de),a
        inc e
        djnz .z
        ret
p_v:    db 0
p_y:    db 0
p_pal:  db 0
p_hf:   db 0
p_x:    db 0
p_src:  dw 0
p_step: dw 0
p_ys:   db 0
p_pg:   db 0
p_r:    db 0
p_c:    db 0
p_l:    db 0
p_tl:   db 0
p_th:   db 0
c_tl:   db 0
c_th:   db $FF
cbuf:   ds 64
p_lf:   ds 256
endpage
