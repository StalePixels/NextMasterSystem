# Golden Axe Warrior (USA, Europe, Brazil) (En), CRC32 C7DED988, 256K, Sega mapper, battery-backed cart RAM.
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log.
name Golden Axe Warrior
cart C7DED988
hz 50		; No-Intro regions USA, Europe, Brazil, so "any" by region; but at 60 Hz the frame
		; handler (V counter wait to $E0 at $0183, then the sprite and sound work) and the game's
		; main loop do not fit in the Next's 264-line frame, and play ran at about half speed. At 50
		; Hz the game takes its PAL path (the rate check at $00AB, page 0 delay) as on a PAL
		; Master System, and play matches the reference step for step.
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the runtime does DI and IM 2).
vector 00 io
start 0003
site 0002A   ; OUT ($BF),A
site 0002D   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 000AE   ; IN A,($BF)
site 000B0   ; IN A,($BF)
site 000BA   ; IN A,($BF)
site 00144   ; OUTD
site 00146   ; OUT (C),B
site 00148   ; OUTD
site 0014A   ; OUT (C),B
site 0014C   ; OUTD
site 0014E   ; OUT (C),B
site 00156   ; OUT ($BF),A
site 0015A   ; OUT ($BF),A
site 00165   ; OUT ($BF),A
site 00168   ; OUT ($BF),A
site 00183   ; IN A,($7E)
site 00189   ; OUT ($BF),A
site 0018D   ; OUT ($BF),A
site 00195   ; OUTI
site 001BA   ; IN A,($DC)
site 001C8   ; IN A,($DD)
site 00239   ; OUT ($BF),A
site 0023D   ; OUT ($BF),A
# Line interrupt handlers $0263, $0275 and $0280: $0240, $024F and $022B store their
# address in $C02C, and $025E jumps through it.
site 0026B   ; OUT ($BF),A
site 0026F   ; OUT ($BF),A
site 00276   ; OUT ($BF),A
site 0027A   ; OUT ($BF),A
# $050C copies the name table to $D600 (IN A,($BE) loop).
site 0051A   ; IN A,($BE)
# The intro script at $10F1 (records of a time byte and a handler word, run by $10DF) starts
# $0D8C and $0DD2, which no path reaches.
site 00DA9   ; OUT ($BE),A
site 00DB2   ; OUT ($BE),A
site 00E1E   ; OUT ($BE),A
site 00282   ; OUT ($BF),A
site 00286   ; OUT ($BF),A
site 0028D   ; OUT ($BE),A
site 002B4   ; OUT ($BF),A
site 002B9   ; OUT ($BF),A
site 002D0   ; OUTI
site 002E6   ; OUTI
site 00305   ; OUT ($BF),A
site 00308   ; OUT ($BF),A
site 00310   ; OUTI
site 0033B   ; OUT ($BE),A
site 00378   ; OUT (C),D
site 0038E   ; OUTI
site 0039E   ; OUT ($BE),A
site 003A3   ; OUT ($BE),A
site 003B0   ; OUTI
site 003CB   ; OUT ($BF),A
site 003CE   ; OUT ($BF),A
site 003DC   ; OUT ($BE),A
site 00589   ; OUT ($BE),A
site 007A2   ; OUT (C),L
site 007A4   ; OUT (C),H
site 007A9   ; OUTI
site 0091A   ; OUT ($BF),A
site 0091E   ; OUT ($BF),A
site 00928   ; OUTI
site 00930   ; IN A,($BF)
site 00ABB   ; IN A,($BF)
site 00C54   ; OUT ($BE),A
site 00C58   ; IN A,($BE)
site 00C5C   ; IN A,($BE)
site 00C60   ; IN A,($BE)
site 00E36   ; OUT ($BE),A
site 00E99   ; OUT (C),E
site 00F21   ; IN A,($7E)
site 01D3C   ; OUT (C),E
site 01D3E   ; OUT (C),D
site 01D46   ; INI
site 01D4D   ; OUT (C),E
site 01D4F   ; OUT (C),D
site 01D7B   ; OUT ($BE),A
site 01D85   ; OUT ($BE),A
site 01D8F   ; OUT ($BE),A
site 01D99   ; OUT ($BE),A
site 01F63   ; OUT ($BF),A
site 01F68   ; OUT ($BF),A
site 01F8A   ; OUT ($BE),A
site 01F95   ; OUT ($BE),A
site 02009   ; OUT ($BE),A
site 0200E   ; OUT ($BE),A
site 02100   ; OUT ($BF),A
site 02104   ; OUT ($BF),A
site 0210B   ; OUTI
site 02191   ; OUTI
site 0219A   ; OUTI
site 022A5   ; OUT ($BF),A
site 022A9   ; OUT ($BF),A
site 022B3   ; OUTI
site 022BB   ; IN A,($BF)
site 022C8   ; OUT ($BF),A
site 022CC   ; OUT ($BF),A
site 022D6   ; OUTI
site 022DE   ; IN A,($BF)
site 02B4A   ; IN A,($BE)
site 02B50   ; OUT ($BE),A
site 03153   ; IN A,($BE)
site 03183   ; IN A,($BE)
site 03191   ; OUT ($BE),A
site 03B16   ; OUT ($BF),A
site 03B1A   ; OUT ($BF),A
site 03B26   ; OUTI
site 03B28   ; OUT ($BE),A
site 03B2A   ; OUTI
site 03B2C   ; OUTI
site 03B2E   ; OUTI
site 03B30   ; OUT ($BE),A
site 03B32   ; OUTI
site 03B34   ; OUTI
site 03B36   ; OUTI
site 03B38   ; OUT ($BE),A
site 03B3A   ; OUTI
site 03B3C   ; OUTI
site 03B3E   ; OUTI
site 03B40   ; OUT ($BE),A
site 03B42   ; OUTI
site 03B44   ; OUTI
site 03B46   ; OUTI
site 03B48   ; OUT ($BE),A
site 03B4A   ; OUTI
site 03B4C   ; OUTI
site 03B4E   ; OUTI
site 03B50   ; OUT ($BE),A
site 03B52   ; OUTI
site 03B54   ; OUTI
site 03B56   ; OUTI
site 03B58   ; OUT ($BE),A
site 03B5A   ; OUTI
site 03B5C   ; OUTI
site 03B5E   ; OUTI
site 03B60   ; OUT ($BE),A
site 06DE2   ; OUT ($BE),A
site 07818   ; OUT ($BE),A
site 083AC   ; OUT ($BE),A
site 084B8   ; IN A,($BE)
site 084BE   ; OUT ($BE),A
site 10000   ; OUTI
site 10002   ; OUTI
site 10004   ; OUTI
site 10006   ; OUTI
site 10008   ; OUTI
site 1000A   ; OUTI
site 1000C   ; OUTI
site 1000E   ; OUTI
site 10010   ; OUTI
site 10012   ; OUTI
site 10014   ; OUTI
site 10016   ; OUTI
site 10018   ; OUTI
site 1001A   ; OUTI
site 1001C   ; OUTI
site 1001E   ; OUTI
site 10020   ; OUTI
site 10022   ; OUTI
site 10024   ; OUTI
site 10026   ; OUTI
site 10028   ; OUTI
site 1002A   ; OUTI
site 1002C   ; OUTI
site 1002E   ; OUTI
site 10030   ; OUTI
site 10032   ; OUTI
site 10034   ; OUTI
site 10036   ; OUTI
site 10038   ; OUTI
site 1003A   ; OUTI
site 1003C   ; OUTI
site 1003E   ; OUTI
site 10040   ; OUTI
site 10042   ; OUTI
site 10044   ; OUTI
site 10046   ; OUTI
site 10048   ; OUTI
site 1004A   ; OUTI
site 1004C   ; OUTI
site 1004E   ; OUTI
site 10050   ; OUTI
site 10052   ; OUTI
site 10054   ; OUTI
site 10056   ; OUTI
site 10058   ; OUTI
site 1005A   ; OUTI
site 1005C   ; OUTI
site 1005E   ; OUTI
site 10060   ; OUTI
site 10062   ; OUTI
site 10064   ; OUTI
site 10066   ; OUTI
site 10068   ; OUTI
site 1006A   ; OUTI
site 1006C   ; OUTI
site 1006E   ; OUTI
site 10070   ; OUTI
site 10072   ; OUTI
site 10074   ; OUTI
site 10076   ; OUTI
site 10078   ; OUTI
site 1007A   ; OUTI
site 1007C   ; OUTI
site 1007E   ; OUTI
site 10080   ; OUTI
site 10082   ; OUTI
site 10084   ; OUTI
site 10086   ; OUTI
site 10088   ; OUTI
site 1008A   ; OUTI
site 1008C   ; OUTI
site 1008E   ; OUTI
site 10090   ; OUTI
site 10092   ; OUTI
site 10094   ; OUTI
site 10096   ; OUTI
site 10098   ; OUTI
site 1009A   ; OUTI
site 1009C   ; OUTI
site 1009E   ; OUTI
site 100A0   ; OUTI
site 100A2   ; OUTI
site 100A4   ; OUTI
site 100A6   ; OUTI
site 100A8   ; OUTI
site 100AA   ; OUTI
site 100AC   ; OUTI
site 100AE   ; OUTI
site 100B0   ; OUTI
site 100B2   ; OUTI
site 100B4   ; OUTI
site 100B6   ; OUTI
site 100B8   ; OUTI
site 100BA   ; OUTI
site 100BC   ; OUTI
site 100BE   ; OUTI
site 100C0   ; OUTI
site 100C2   ; OUTI
site 100C4   ; OUTI
site 100C6   ; OUTI
site 100C8   ; OUTI
site 100CA   ; OUTI
site 100CC   ; OUTI
site 100CE   ; OUTI
site 100D0   ; OUTI
site 100D2   ; OUTI
site 100D4   ; OUTI
site 100D6   ; OUTI
site 100D8   ; OUTI
site 100DA   ; OUTI
site 100DC   ; OUTI
site 100DE   ; OUTI
site 100E0   ; OUTI
site 100E2   ; OUTI
site 100E4   ; OUTI
site 100E6   ; OUTI
site 100E8   ; OUTI
site 100EA   ; OUTI
site 100EC   ; OUTI
site 100EE   ; OUTI
site 100F0   ; OUTI
site 100F2   ; OUTI
site 100F4   ; OUTI
site 100F6   ; OUTI
site 100F8   ; OUTI
site 100FA   ; OUTI
site 100FC   ; OUTI
site 100FE   ; OUTI
site 13D98   ; OUT ($BE),A
site 181AD   ; OUT ($7F),A
site 18279   ; OUT ($7F),A
site 1840B   ; OTIR
site 18521   ; OUT ($7F),A
site 1852B   ; OUT ($7F),A
site 18548   ; OUT ($7F),A
site 1864C   ; OUT ($7F),A
site 186D8   ; OUT ($7F),A
site 1875D   ; OUT ($06),A
site 187A7   ; OUT ($7F),A
site 187B0   ; OUT ($7F),A
site 187C0   ; OUT ($7F),A
site 18841   ; OUT ($7F),A
mapldk 0008C   # LD HL,$FFFC; LD (HL),$80
maphl 00092   # LD (HL),$00, HL = $FFFD
maphl 00095   # LD (HL),$01, HL = $FFFE
maphl 00098   # LD (HL),$02, HL = $FFFF
mapst 00152   ; LD ($FFFF),A
mapst 0019F   ; LD ($FFFF),A
mapst 001FA   ; LD ($FFFC),A
mapst 001FF   ; LD ($FFFF),A
mapst 00210   ; LD ($FFFC),A
mapst 00214   ; LD ($FFFF),A
mapst 002C8   ; LD ($FFFF),A
mapst 00327   ; LD ($FFFF),A
mapst 0043F   ; LD ($FFFC),A
mapst 0044A   ; LD ($FFFC),A
mapst 00455   ; LD ($FFFF),A
mapst 00526   ; LD ($FFFF),A
mapst 0081E   ; LD ($FFFF),A
mapst 00A6E   ; LD ($FFFF),A
mapst 00BB4   ; LD ($FFFF),A
mapst 00C4A   ; LD ($FFFF),A
mapst 00C6A   ; LD ($FFFF),A
mapst 00D20   ; LD ($FFFF),A
mapst 00D3E   ; LD ($FFFF),A
mapst 00EC9   ; LD ($FFFF),A
mapst 00F3F   ; LD ($FFFF),A
mapst 0104F   ; LD ($FFFF),A
mapst 011D2   ; LD ($FFFF),A
mapst 01216   ; LD ($FFFF),A
mapst 01270   ; LD ($FFFF),A
mapst 01479   ; LD ($FFFF),A
mapst 016F2   ; LD ($FFFF),A
mapst 01725   ; LD ($FFFF),A
mapst 0172D   ; LD ($FFFF),A
mapst 0173D   ; LD ($FFFF),A
mapst 01782   ; LD ($FFFF),A
mapst 0188F   ; LD ($FFFF),A
mapst 0189A   ; LD ($FFFF),A
mapst 01919   ; LD ($FFFF),A
mapst 0197B   ; LD ($FFFF),A
mapst 01E50   ; LD ($FFFF),A
mapst 01F72   ; LD ($FFFF),A
mapst 02269   ; LD ($FFFF),A
mapst 0235B   ; LD ($FFFF),A
mapst 02B14   ; LD ($FFFF),A
mapst 02E21   ; LD ($FFFF),A
mapst 02FEB   ; LD ($FFFF),A
mapst 03004   ; LD ($FFFF),A
mapst 031F1   ; LD ($FFFF),A
mapst 03229   ; LD ($FFFF),A
mapst 03272   ; LD ($FFFF),A
mapst 03B0C   ; LD ($FFFF),A
mapst 04B38   ; LD ($FFFF),A
mapst 04C62   ; LD ($FFFF),A
mapst 05B3C   ; LD ($FFFF),A
mapst 05BAD   ; LD ($FFFF),A
mapst 05E98   ; LD ($FFFF),A
mapst 069C4   ; LD ($FFFF),A
mapst 06A68   ; LD ($FFFF),A
mapst 06B30   ; LD ($FFFF),A
mapst 06C6E   ; LD ($FFFF),A
mapst 06E30   ; LD ($FFFF),A
mapst 07001   ; LD ($FFFF),A
mapst 07063   ; LD ($FFFF),A
mapst 070DA   ; LD ($FFFF),A
mapst 0712F   ; LD ($FFFF),A
mapst 0719A   ; LD ($FFFF),A
mapst 071E9   ; LD ($FFFF),A
mapst 07284   ; LD ($FFFF),A
mapst 077B9   ; LD ($FFFF),A
# Scanner notes. The stores to $8010 and $8030 ($0429, $0437, $7438) are cart RAM writes ($FFFC
# bit 3 maps cart RAM into slot 2; the game uses it as work RAM) and run natively. The LD (BC),A
# rows in bank 6 ($89B4-$8AA5) and the RST $38 calls at $8AC7/$8AD2 are sound data read as code.
# The JP (HL) at $0021 (RST $18/$08 tables), $0262 (line handler hook $C02C), $0F35 (frame hook
# $DCEC: $0F36, $0F37, $104A, $1055) and $10F0 (intro script $10F1) are covered: their targets
# are scanned or given above. Byte-scan rows not patched have a false verdict in
# data/scan-verdicts.tsv (operand bytes and packed tile data); the rest of the CHECK low rows are
# packed graphics in banks 5-15 with no code.
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00492   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 00D8E   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
# Video rate check $00AB-$00C0: the game waits for the frame flag, counts BC from 2,502 down
# ($00B5, 26 T-states a pass: 65,047 T-states, 1.09 NTSC frames or 0.91 PAL frames), then reads
# the flag again: set means NTSC ($80 in $DE03), clear means PAL. At 28 MHz the count took a tenth
# of a frame, so the game always took PAL: at 60 Hz the sound driver ($801B, bank 6) played its
# music 6/5 too fast (it skips every sixth frame only for NTSC) and the frame handler waited for
# V counter $F0 in place of $E0 ($017C). The cave in place of the count far-calls page 0 delay,
# which waits the count's Master System time.
asm 000B5 5          ; DEC BC : LD A,C : OR B : JR NZ,$00B5
    rst $00
    db far_io, pg_delay, ent_delay
    nop
endasm
# Code page 0. Three game routines wrote one byte a trap, each with its VRAM address written
# first; each is replaced by a far call from a code cave.
#
# Text plane upload $0786 (the text box renderer at $059B calls it after each character it
# draws): 1,040 bytes from the bitmap at $D100 to VRAM $2001, $2005, ... $3101 (plane 1 of the
# text tiles; OUTI and DJNZ both count B down, so each pass of 16 writes 8 bytes), each byte with
# its VRAM address written first: 3,120 traps, about 5 Next frames a call against 1.4 frames on
# the Master System, so text printed about 3.6 times too slowly. The cave after CALL $0BC6
# far-calls plane. The NOP after the EI: a frame event that came while plane ran goes in there,
# not at the RET's target. Taken at the RET's target ($06D9 from $06D6), its return slot later
# held the same $06D9 again, pushed by the next CALL $0786 at the same stack place, and the
# runtime's frm_run then took the handler for still running and held each frame event for 8
# frames (the frame wait at $0BC6 took 9 frames every other word).
asm 0078E 8          ; LD HL,$6001 : LD DE,$0004 : LD C,$BF
    rst $00
    db far_io, pg_plane, ent_plane
    ei
    nop
    ret
endasm
# Tile unpacker $032A (Sega planar RLE, 4 planes, step 4; $0327 sets $FFFF first): RST $28 sets
# the VRAM address before every byte, so each byte cost 3 traps (about 4,000 Next cycles). The
# cave at its start far-calls rle. Its OUT ($BE),A at $033B keeps its site line but no longer runs.
asm 0032A 5          ; LD C,$04 : LD B,C : PUSH BC : PUSH DE
    rst $00
    db far_io, pg_rle, ent_rle
    ret
endasm
# Intro picture dissolve $0E79: 7 passes, each writes byte 3 of every tile row from $0003 to
# $23FF (2,304 bytes, a 4-byte mask pattern rotated by 2 bits a byte), each byte with its VRAM
# address first: about 18 Next frames a pass against 3.9 on the Master System. The cave in place
# of the inner loop $0E8B-$0E9D far-calls dslv and goes on at $0EA0. The loop's OUT (C),E at
# $0E99 keeps its site line but no longer runs.
asm 00E8B 7          ; EXX : DI : OUT (C),L : OUT (C),H : EI
    rst $00
    db far_io, pg_dslv, ent_dslv
    jp $0EA0
endasm
# Intro screen writers. Each sets the VRAM address with RST $28 for every byte or pair, so each
# byte cost 2 or 3 traps. The caves far-call page 0 fill, copy and dsl2. The OUT sites inside
# them keep their site lines but no longer run.
# $0E2B: $FF to byte 3 of every tile row from $0003 to $23FF (2,304 bytes).
asm 00E2B 5          ; PUSH HL : LD DE,$4003 : RST $28
    rst $00
    db far_io, pg_fill, ent_fill
    ret
endasm
# $0E14: 2,304 bytes from $C900 to DE, DE + 4, ... (one bit plane of the picture).
asm 00E14 7          ; PUSH HL : LD HL,$C900 : LD BC,$0900
    rst $00
    db far_io, pg_copy, ent_copy
    ret
    nop
    nop
endasm
# $0D9F-$0DBB: one pass of the second picture's dissolve, planes 2 and 3 from $C900 ANDed with a
# mask rotated by 2 bits a pair, 1,536 pairs; the pass loop around it ($0D9E, $0DBD) stays.
asm 00D9F 7          ; LD HL,$C900 : LD DE,$4002 : RST $28
    rst $00
    db far_io, pg_dsl2, ent_dsl2
    jp $0DBD
endasm
# $0397 (also JP at $0086): VRAM fill, the word in HL written n times from DE (n = C + 256 * B,
# C = 0 counts 256), two OUT ($BE),A a word: 4,608 words in the intro took 32 Next frames against
# 5.3 on the Master System. The cave at its start far-calls vfill.
asm 00397 5          ; RST $28 : LD A,C : OR A : JR Z,$039D
    rst $00
    db far_io, pg_vfill, ent_vfill
    ret
endasm
# Frame handler tile animation $3B07 (when the foreground leaves a bank in $C042): E tiles to
# VRAM $3E00, each row 3 bytes from the table and a 0, through 24 OUTI and 8 OUT ($BE),A a
# tile: about 125,000 Next cycles a call, 69 lines of the frame handler. At 60 Hz the handler
# then ran past the next frame event every frame, its next entry came late and waited most of a
# frame for V counter $E0 at $0183, and the game ran at half speed. The cave after the game's
# address write far-calls anim, which writes the same bytes with one jt_vwrite.
asm 03B20 5          ; LD C,$BE : OUTI : first byte of the next OUTI
    rst $00
    db far_io, pg_anim, ent_anim
    ret
endasm
page 0 plane rle dslv delay fill copy dsl2 vfill anim
; Shared: gsp, the game's SP at the far call; pstack, this page's stack. Code that runs with
; interrupts on runs on the game's stack (dwait, win): an interrupt taken on this page's stack
; would lose its return address. pline reads the Next's raster line with interrupts off, so no
; handler changes the NextReg select port between the select and the read.
;
; plane: as the game's $078E-$07B3, with interrupts off, in the Master System's time of that
; code: 85,353 T-states, 372 Next lines at 50 Hz (71,364 T-states to 311 lines), 377 at 60 Hz
; (59,736 to 264). The game writes the 1,040 bytes from $D100 to VRAM $2001 + 4n each time,
; though a character changes only a few of them; every byte written marks its tile for
; conversion, so plane compares the bytes with the VRAM copy (mapped in slot 0 for the compare)
; and writes only the runs that differ, and the last byte always, with jt_vwrite (runs of 1
; byte, VRAM step 4), so the VDP address ends where the game's writes leave it. Past MAXRUN runs
; it writes all 1,040. Runtime internals used: SHADOW_PAGE 28 (memplan.inc, the VRAM copy,
; pages 28-29); cur_mmu $E02D is public. Returns as the game's code does, with an odd number of
; EXX: the main set HL = $D510, BC = $00BE, DE = the alternate DE at entry; the alternate set
; HL = $7041, DE = $0004, C = $BF, B = the main B at entry; A = 0, Z and N set. IX and IY are
; kept. Interrupts stay off; the cave turns them on, as the game's EI does.
plane:  di
        ld (gsp),sp
        ld sp,pstack
        push bc                 ; the main B at entry
        exx
        push de                 ; the alternate DE at entry
        exx
        push ix
        push iy
        call rate
        ld hl,372
        jr z,.hz
        ld hl,377
.hz:    call tstart
        ld a,29                 ; SHADOW_PAGE + 1: VRAM $2000-$3FFF at $0000
        db $ED,$92,$50          ; nextreg $50,a
        ld hl,$D100
        ld de,$0001
        ld bc,1040
        ld ix,runs
        xor a
        ld (nrun),a
        ld (inrun),a
.cmp:   dec bc
        ld a,b
        or c
        jr z,.diff              ; the last byte is always written
        ld a,(de)
        cp (hl)
        jr nz,.diff
        xor a
        ld (inrun),a
        jr .next
.diff:  ld a,(inrun)
        or a
        jr z,.new
        inc (iy+2)              ; one more byte in this run
        jr nz,.next
        inc (iy+3)
        jr .next
.new:   ld a,(nrun)
        cp MAXRUN
        jr z,.full
        inc a
        ld (nrun),a
        ld (inrun),a
        push ix
        pop iy
        ld (ix+0),l
        ld (ix+1),h
        ld (ix+2),1
        ld (ix+3),0
        inc ix
        inc ix
        inc ix
        inc ix
.next:  ld a,b
        or c
        jr z,.cend
        inc hl
        inc de
        inc de
        inc de
        inc de
        jr .cmp
.full:  ld ix,runs              ; too many runs: all 1,040 bytes as one
        ld hl,$D100
        ld (ix+0),l
        ld (ix+1),h
        ld hl,1040
        ld (ix+2),l
        ld (ix+3),h
        ld a,1
        ld (nrun),a
.cend:  ld a,($E02D)            ; cur_mmu+0: the game's page back in slot 0
        db $ED,$92,$50          ; nextreg $50,a
        ld hl,runs
        ld (rptr),hl
        ld ix,1
        ld iy,4
.run:   ld a,(nrun)
        or a
        jr z,.wait
        dec a
        ld (nrun),a
        ld hl,(rptr)
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld c,(hl)
        inc hl
        ld b,(hl)
        inc hl
        ld (rptr),hl
        ex de,hl                ; HL = the source, BC = the bytes
        push hl                 ; DE = $2001 + 4 * (HL - $D100)
        ld de,$D100
        or a
        sbc hl,de
        add hl,hl
        add hl,hl
        ld de,$2001
        add hl,de
        ex de,hl
        pop hl
.part:  ld a,b
        or c
        jr z,.run
        push bc
        ld a,b                  ; this call: min(BC, 256) runs of 1 byte
        or a
        ld a,c
        jr z,.lt
        xor a                   ; 256
.lt:    ld c,a
        ld b,1
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,c                  ; HL + runs, DE + 4 * runs
        or a
        jr nz,.ad
        inc h
        ld a,d
        add a,4
        ld d,a
        pop bc
        dec b
        jr .pt
.ad:    push af
        add a,l
        ld l,a
        jr nc,.a1
        inc h
.a1:    pop af
        push hl
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,de
        ex de,hl
        pop hl
        pop bc                  ; BC - runs (< 256 only for the last part: BC < 256)
        ld bc,0
.pt:    push hl
        push de
        call tick
        pop de
        pop hl
        jr .part
.wait:  call tick
        ld hl,(tgoal)
        or a
        sbc hl,de
        jr nc,.wait             ; HL >= DE? no: goal still above the lines passed
        pop iy
        pop ix
        pop de                  ; the alternate DE at entry, for the main set
        pop bc                  ; the main B at entry, for the alternate set
        ld c,$BF
        ld hl,$7041
        push de
        ld de,4
        exx
        pop de
        ld hl,$D510
        ld bc,$00BE
        ld a,1
        dec a
        call tstop
        ld sp,(gsp)
        ret
;
; rle: as the game's $032A-$0364. HL = the packed data (read as the game sees it), DE = the VRAM
; write command of plane 0. Each plane is a list of records: a count byte n, then n AND $7F bytes
; when n has bit 7, or one byte repeated n AND $7F times (a count of 0 there runs 256 times); a
; count byte of 0 ends the plane. Plane p goes to DE + p, DE + p + 4, ... The planes are unpacked
; into buf and written with jt_vwrite (runs of 1 byte, VRAM step 4) each time buf is full and at
; each plane's end; when DE is not a VRAM write command, or the command would change on the way,
; the bytes go through the ports one by one instead (.port). After each write, win lets a waiting
; interrupt in, as the game's RST $28 turns interrupts on after each byte. Each write of buf, and
; the return, waits (dwait, interrupts on) until the Master System's time of the game's loop for
; the bytes so far has passed (t_byte, t_rec, t_plane), so screens load in the Master System's
; time and a button still held from the screen before is not read by the next one. Returns as the game's code does: ($C031) = the
; address after plane 3's last byte, DE = that + 1 - 4 with A = E and the flags of the game's
; SUB C / DEC D, B = 0, C = 4, HL after plane 3's end byte; AF', IX, IY, BC', DE' and HL' kept;
; interrupts on when a byte was written, else as at entry.
rle:    ld (gsp),sp
        ld (r_de),de
        ld a,i                  ; P/V = the interrupt state at entry
        di
        ld sp,pstack
        ld a,$00                ; NOP
        jp po,.ie
        ld a,$FB                ; EI
.ie:    ld (.eib),a
        push ix
        push iy
        push hl
        call rate               ; the Master System's T-states a Next line: 229 at 50 Hz, 226 at 60
        ld hl,229
        jr z,.r5
        ld hl,226
.r5:    ld (tq_div),hl
        ld hl,0
        ld (tq_rem),hl
        ld (d_goal),hl
        call tstart
        pop hl
        ld a,4
        ld (r_n),a
.plane: ld de,(r_de)
        ld (r_v),de
        ld de,buf
.run:   call get
        or a
        jr z,.pend
        call t_rec
        ld c,a
        and $7F
        ld b,a
        ld a,$FB                ; a byte goes out: interrupts on at the end
        ld (.eib),a
        bit 7,c
        jr nz,.lit
        call get                ; one byte, B times
        ld c,a
.rep:   call t_byte
        ld a,c
        ld (de),a
        inc de
        ld a,e
        cp low buf_end
        call z,flush
        djnz .rep
        jr .run
.lit:   call t_byte
        call get                ; B bytes
        ld (de),a
        inc de
        ld a,e
        cp low buf_end
        call z,flush
        djnz .lit
        jr .run
.pend:  call t_plane
        call flush
        ld de,(r_de)
        inc de                  ; the next plane starts one VRAM byte later
        ld (r_de),de
        ld a,(r_n)
        dec a
        ld (r_n),a
        jr nz,.plane
        ld a,(.eib)
        or a
        jr z,.nw                ; no byte written: no wait
        push hl
        ld hl,(d_goal)
        call dwait
        pop hl
.nw:    pop iy
        pop ix
        ld de,(r_v)             ; the address after plane 3's last byte
        ld ($C031),de
        inc de
        ld bc,$0004
        ld a,e
        sub c
        ld e,a
        jr nc,.nc
        dec d
.nc:    call tstop
        ld sp,(gsp)
.eib:   nop                     ; EI when a byte was written or interrupts were on at entry
        ret
; The Master System's T-states of the game's loop, added to d_goal in Next lines (tq_div
; T-states a line, the rest carried in tq_rem): t_byte 135 a byte written (RST $28 and the
; loop), t_rec 62 a record (its count byte and the end of the record), t_plane 110 a plane's
; end (its 0 byte, the pushes and pops). Keep every register but F.
t_byte: push hl
        push de
        ld de,135
        jr t_add
t_rec:  push hl
        push de
        ld de,62
        jr t_add
t_plane: push hl
        push de
        ld de,110
        jr t_add
t_addde: push hl                ; DE = the T-states
        push de
t_add:  push af
        ld hl,(tq_rem)
        add hl,de
        ld de,(tq_div)
.l:     or a
        sbc hl,de
        jr c,.x
        push hl
        ld hl,(d_goal)
        inc hl
        ld (d_goal),hl
        pop hl
        jr .l
.x:     add hl,de
        ld (tq_rem),hl
        pop af
        pop de
        pop hl
        ret
; A = (HL) as the game sees it, HL + 1; F changes
get:    ld a,h
        and $E0
        cp $20
        jr z,.pk
        ld a,(hl)
        inc hl
        ret
.pk:    call jt_peek            ; the game's page under this one
        inc hl
        ret
; the bytes from buf to DE: to VRAM at r_v, r_v + 4, ...; r_v moves past them, DE = buf; keeps
; BC and HL. Then win.
flush:  push hl
        push bc
        ex de,hl
        ld de,buf
        or a
        sbc hl,de               ; HL = the bytes in buf
        jp z,.fd
        ld (f_cnt),hl
        ld (f_src),de
        ld hl,(d_goal)          ; the Master System's time of these bytes first
        call dwait
        ld hl,(f_cnt)
        ld de,(r_v)
        add hl,hl
        add hl,hl
        dec hl
        add hl,de               ; the last address + 3
        ld a,h
        xor d
        and $C0
        jr nz,.port             ; the command changes on the way
        ld a,d
        and $C0
        cp $40
        jr nz,.port             ; not a VRAM write command
        ld ix,1
        ld iy,4
        ld hl,(f_cnt)
.fl:    ld a,h
        or l
        jr z,.fw
        ld c,0                  ; 256 runs
        ld a,h
        or a
        jr nz,.fn
        ld c,l
.fn:    push hl
        ld b,1
        ld hl,(f_src)
        ld de,(r_v)
        ld a,1                  ; the source as mapped: buf in this page
        call jt_vwrite
        ld e,c
        ld d,0
        ld a,c
        or a
        jr nz,.fm
        inc d                   ; 256
.fm:    add hl,de
        ld (f_src),hl
        ld hl,(r_v)
        add hl,de
        add hl,de
        add hl,de
        add hl,de
        ld (r_v),hl
        pop hl
        or a
        sbc hl,de
        jr .fl
.port:  ld hl,(f_cnt)           ; DE = r_v
        ld bc,(f_src)
.pl:    ld a,e
        rst $00
        db $05                  ; OUT ($BF),A
        ld a,d
        rst $00
        db $05
        ld a,(bc)
        rst $00
        db $04                  ; OUT ($BE),A
        inc bc
        inc de
        inc de
        inc de
        inc de
        dec hl
        ld a,h
        or l
        jr nz,.pl
        ld (r_v),de
.fw:    call win
.fd:    ld de,buf
        pop bc
        pop hl
        ret
;
; dslv: as the game's inner loop $0E8B-$0E9D, from the game's first VRAM write on, in the
; Master System's time of the loop: 100 T-states a byte, so byte n goes out 0.44 Next lines
; (n * 100 T-states as a share of a frame) after the first. Writes the 2,304 bytes to VRAM $0003,
; $0007, ... $23FF in 36 chunks of 64 with jt_vwrite; chunk k goes when 28k lines have passed
; (64 bytes are 27.9 lines at 50 Hz, 28.3 at 60 Hz), then it waits to 1,008 lines, the loop's
; whole time. The byte values: E at entry rotated right by 2 bits before each byte. It waits
; with interrupts on, as the game's loop turns them on after each byte. Returns as the loop's
; end does: the main set as at entry (E is back to its entry value after 2,304 rotations), A =
; $64; the alternate set HL = $6403, DE and BC as at entry. IX and IY kept; interrupts on.
dslv:   di
        ld (gsp),sp
        ld sp,pstack
        push bc
        push de
        push hl
        push ix
        push iy
        ld a,e                  ; the 4-byte pattern, 64 times
        ld hl,dbuf
        ld b,64
.f:     rrca
        rrca
        ld (hl),a
        inc hl
        rrca
        rrca
        ld (hl),a
        inc hl
        rrca
        rrca
        ld (hl),a
        inc hl
        rrca
        rrca
        ld (hl),a
        inc hl
        djnz .f
        ld hl,1008
        call tstart
        ld hl,0
        ld (d_goal),hl
        ld hl,$0003
        ld (d_v),hl
        ld a,36
.ch:    ld (d_n),a
        ld hl,(d_goal)
        call dwait
        ld hl,dbuf
        ld de,(d_v)
        ld bc,$0140             ; 64 runs of 1 byte
        ld ix,1
        ld iy,4
        ld a,1                  ; the source is this page
        call jt_vwrite
        ld hl,(d_v)
        inc h                   ; VRAM + 256
        ld (d_v),hl
        ld hl,(d_goal)
        ld de,28
        add hl,de
        ld (d_goal),hl
        ld a,(d_n)
        dec a
        jr nz,.ch
        ld hl,1008
        call dwait
        pop iy
        pop ix
        pop hl
        pop de
        pop bc
        exx
        ld hl,$6403
        exx
        ld a,$64
        call tstop
        ld sp,(gsp)
        ei
        ret
;
; delay: as the game's count at $00B5-$00B9 from BC = 2,502, in its Master System time: 65,047
; T-states, 284 Next lines at 50 Hz (71,364 T-states to 311 lines), 288 at 60 Hz (59,736 to
; 264). When a frame event (Next line 192) falls in that time it sets the frame flag in
; vdp_status ($E03A, public), so the game's status read after the count sees it as on the
; Master System: set at 60 Hz, clear at 50 Hz. Interrupts stay off (the game has them off here).
; Returns as the count ends: BC = 0,
; A = 0 with the flags of OR B (Z set). DE, HL, IX, IY kept.
delay:  di
        ld (gsp),sp
        ld sp,pstack
        push de
        push hl
        call rate
        ld hl,284
        jr z,.r
        ld hl,288
.r:     call tstart
        ld hl,192               ; lines to the next frame event (Next line 192)
        ld de,(pprev)
        or a
        sbc hl,de
        jr z,.lp
        jr nc,.fe
.lp:    ld de,(plen)
        add hl,de
.fe:    ld (dfe),hl
.w:     call tick
        ld hl,(tgoal)
        or a
        sbc hl,de
        jr nc,.w
        ld hl,(dfe)             ; a frame event in the count's time: the frame flag, as the
        ex de,hl                ; VDP sets it (with interrupts off, the runtime sets it only
        or a                    ; at a status read below the picture, once a picture)
        sbc hl,de
        jr c,.nf
        ld hl,$E03A             ; vdp_status
        set 7,(hl)
.nf:    pop hl
        pop de
        ld bc,0
        xor a
        or b
        call tstop
        ld sp,(gsp)
        ret
;
; fill, copy, dsl2: as the game's loops at $0E2B-$0E3E, $0E14-$0E2A and $0D9F-$0DBB, in their
; Master System time (wrp: 124, 133 and 178 T-states a byte or pair), with interrupts on as the
; game's RST $28 leaves them. fill returns HL kept, DE = $6403, A = $64 with the flags of CP $64;
; copy returns HL kept, DE + $2400, BC = 0, A = 0 with Z; dsl2 returns HL = $D500, DE = $5802,
; A = $58 with the flags of CP $58, BC kept (C rotates back to its entry value). IX, IY kept.
fill:   di
        ld (gsp),sp
        ld sp,pstack
        push hl
        push ix
        push iy
        call pinit
        ld hl,ffbyte
        ld de,$0003
        ld bc,2304
        ld a,1                  ; 1 byte a run
        ld (w_b),a
        ld (w_a),a              ; the source is this page
        ld ix,0                 ; source step 0: the same $FF
        ld iy,124
        call wrp
        pop iy
        pop ix
        pop hl
        ld de,$6403
        ld a,$64
        cp $64
        call tstop
        ld sp,(gsp)
        ei
        ret
copy:   di
        ld (gsp),sp
        ld sp,pstack
        push hl
        push de
        push ix
        push iy
        call pinit
        pop iy
        pop ix
        pop de
        push de
        push ix
        push iy
        ld hl,$C900
        ld bc,2304
        ld a,1
        ld (w_b),a
        xor a                   ; the source as the game sees it
        ld (w_a),a
        ld ix,1
        ld iy,133
        call wrp
        pop iy
        pop ix
        pop de
        pop hl
        push hl
        ld hl,$2400
        add hl,de
        ex de,hl
        pop hl
        ld bc,0
        xor a
        or c
        call tstop
        ld sp,(gsp)
        ei
        ret
dsl2:   di
        ld (gsp),sp
        ld sp,pstack
        push bc
        push ix
        push iy
        ld hl,$C900             ; the pairs ANDed with the mask, into bufb
        ld de,bufb
        ld b,0                  ; 1,536 pairs: 6 x 256
        ld a,6
.o:     push af
.p:     ld a,(hl)
        and c
        ld (de),a
        inc hl
        inc de
        ld a,(hl)
        and c
        ld (de),a
        inc hl
        inc de
        rlc c
        rlc c
        djnz .p
        pop af
        dec a
        jr nz,.o
        call pinit
        ld hl,bufb
        ld de,$0002
        ld bc,1536
        ld a,2                  ; 2 bytes a run
        ld (w_b),a
        ld a,1                  ; the source is this page
        ld (w_a),a
        ld ix,2
        ld iy,178
        call wrp
        pop iy
        pop ix
        pop bc
        ld hl,$D500
        ld de,$5802
        ld a,$58
        cp $58
        call tstop
        ld sp,(gsp)
        ei
        ret
;
; anim: as the game's loop $3B20-$3B66, with interrupts off (it runs in the frame handler):
; E tiles (E = 0: 256), each 8 rows of 3 bytes from HL (read as the game sees it) and a 0, to
; VRAM at the address the game wrote (vdp_addr, $E037, public), with jt_vwrite (E runs of 32
; bytes). Returns as the loop does: HL + 24 * E, E = 0 with Z set, B - 24 * E, C = $BE, A = 0;
; the VDP address after the last byte. IX, IY, D kept. It runs inside the frame handler, which
; can interrupt another entry of this page while that one waits with interrupts on, so it has
; its own stack (astack) and buffer (abuf), up to 32 tiles.
anim:   ld (agsp),sp
        ld sp,astack
        push ix
        push iy
        push bc
        ld ix,abuf
        ld c,e
.t:     ld b,8
.r:     call get
        ld (ix+0),a
        call get
        ld (ix+1),a
        call get
        ld (ix+2),a
        ld (ix+3),0
        inc ix
        inc ix
        inc ix
        inc ix
        djnz .r
        dec c
        jr nz,.t
        push hl
        push de
        ld hl,abuf
        ld c,e                  ; E runs of 32 bytes
        ld b,32
        ld de,($E037)           ; vdp_addr
        ld ix,32
        ld iy,32
        ld a,1                  ; the source is this page
        call jt_vwrite
        pop de
        pop hl
        pop bc
        ld a,e                  ; B - 24 * E
        add a,a
        add a,e
        add a,a
        add a,a
        add a,a
        neg
        add a,b
        ld b,a
        ld c,$BE
        ld e,0
        xor a
        pop iy
        pop ix
        ld sp,(agsp)
        ret
;
; vfill: as the game's $0397-$03AA: the word HL (L first) n times from the VRAM command DE,
; n = C + 256 * B (C = 0: 256 * B), in its Master System time (67 T-states a word), with
; interrupts on as its RST $28 leaves them. When DE is not a VRAM write command it writes
; through the ports instead, with interrupts off. Returns as the game's code does: B = C = 0,
; A = H with Z set, DE and HL kept; IX, IY kept.
vfill:  di
        ld (gsp),sp
        ld sp,pstack
        push hl
        push de
        push ix
        push iy
        ld (vword),hl
        ld a,c                  ; n
        or a
        jr z,.n0
        ld l,c
        ld h,b
        jr .n
.n0:    ld l,0
        ld h,b
.n:     push hl
        ld a,d
        and $C0
        cp $40
        jr nz,.port
        call pinit
        pop bc
        pop iy
        pop ix
        pop de
        push de
        push ix
        push iy
        ld hl,vword
        ld a,2
        ld (w_b),a
        ld (w_vs),a
        ld a,1                  ; the source is this page
        ld (w_a),a
        ld ix,0
        ld iy,67
        call wrp
        jr .x
.port:  pop bc                  ; BC = n
        ld a,e
        rst $00
        db $05                  ; OUT ($BF),A
        ld a,d
        rst $00
        db $05
        ld hl,(vword)
.pl:    ld a,l
        rst $00
        db $04                  ; OUT ($BE),A
        ld a,h
        rst $00
        db $04
        dec bc
        ld a,b
        or c
        jr nz,.pl
.x:     pop iy
        pop ix
        pop de
        pop hl
        ld bc,0
        ld a,h
        cp a
        call tstop
        ld sp,(gsp)
        ei
        ret
; pinit: starts the Master System time count (d_goal, in Next lines from now). Changes A, BC,
; DE, HL.
pinit:  call rate               ; the Master System's T-states a Next line: 229 at 50 Hz, 226 at 60
        ld hl,229
        jr z,.r
        ld hl,226
.r:     ld (tq_div),hl
        ld hl,0
        ld (tq_rem),hl
        ld (d_goal),hl
        jp tstart
; wrp: BC runs of w_b bytes from HL (source step IX, jt_vwrite's A in w_a) to VRAM DE, DE + s,
; ... (s = w_vs, 4 unless the caller sets it; wrp puts 4 back); IY = the Master System's T-states of a run. Before each chunk of 64 runs it waits (dwait,
; interrupts on) until the time of the runs before it has passed, and after the last until the
; time of all of them has. Changes every register but the alternates.
wrp:    ld (w_src),hl
        ld (w_dst),de
        ld (w_runs),bc
        ld (w_ixs),ix
        ld (w_t),iy
        ld a,(w_vs)
        ld (w_vs2),a
.l:     ld hl,(w_runs)
        ld a,h
        or l
        jr z,.x
        ld bc,64
        or a
        sbc hl,bc
        jr nc,.k
        add hl,bc               ; fewer than 64 left
        ld c,l
        ld hl,0
.k:     ld (w_runs),hl
        ld a,c
        ld (w_k),a
        ld hl,(d_goal)
        call dwait
        ld hl,(w_src)
        ld de,(w_dst)
        ld a,(w_b)
        ld b,a
        ld a,(w_k)
        ld c,a
        ld ix,(w_ixs)
        ld a,(w_vs2)
        ld iyl,a
        ld iyh,0
        ld a,(w_a)
        call jt_vwrite
        ld a,(w_k)
        ld b,a
.a:     ld hl,(w_src)           ; source + step, VRAM + 4, time + a run, for each run
        ld de,(w_ixs)
        add hl,de
        ld (w_src),hl
        ld hl,(w_dst)
        ld a,(w_vs2)
        ld e,a
        ld d,0
        add hl,de
        ld (w_dst),hl
        ld de,(w_t)
        call t_addde
        djnz .a
        jr .l
.x:     ld a,4
        ld (w_vs),a
        ld hl,(d_goal)
        jp dwait
;
; rate: Z for 50 Hz, NZ for 60 Hz (NextReg $05 bit 2). Changes A, BC.
rate:   ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        bit 2,a
        ret
; tstart: starts the line count, HL = the lines to its goal (tgoal), and CTC channel 0 as a
; free timer (28 MHz clock, prescaler 256, time constant 256, no interrupt: a count every 256
; cycles, a turn every 65,536 cycles, about 36 lines). Interrupts off. Changes A, BC, DE, HL.
tstart: ld (tgoal),hl
        call rate
        ld hl,311
        jr z,.r
        ld hl,264
.r:     ld (plen),hl
        ld hl,0
        ld (pel),hl
        ld bc,$183B
        ld a,$27                ; timer, prescaler 256, time constant next, reset
        out (c),a
        xor a                   ; time constant 256
        out (c),a
        in a,(c)
        ld (t_c),a
        call pline
        ld (pprev),hl
        ret
; tstop: stops CTC channel 0 (the docs of NextZXOS do not say whether it uses the CTC; every
; entry that ran tstart calls this before it returns). Keeps every register and the flags.
tstop:  push af
        push bc
        ld bc,$183B
        ld a,$03                ; control word, reset: the channel stops
        out (c),a
        pop bc
        pop af
        ret
; tick: adds the time since the last call to pel, in lines; DE = pel. The line difference gives
; the gap modulo a frame, and gaps of a frame or more come (the game's interrupt handler and the
; runtime's once-a-frame work while a wait has interrupts on, a jt_vwrite that converts many
; tiles). Of the gaps d, d + one frame and d + two frames (1,824 cycles a line), it takes the
; one whose cycle count agrees best with the CTC's count (as Psycho Fox's tick). Interrupts
; off. Changes A, DE, HL.
tick:   push bc
        push ix
        call pline
        ld de,(pprev)
        ld (pprev),hl
        or a
        sbc hl,de               ; d = now - last, modulo the frame
        jr nc,.d
        ld de,(plen)
        add hl,de
.d:     ld bc,$183B             ; CTC channel 0 count, down
        in a,(c)
        ld c,a
        ld a,(t_c)
        sub c                   ; counts since the last read, modulo 256
        ld (t_g),a
        ld a,c
        ld (t_c),a
        ld ix,$FFFF             ; best distance so far (IXL), its gap in t_bg
        ld b,3                  ; d, d + a frame, d + two frames
.k:     push hl
        push bc
        ld d,h                  ; HL * 57 / 8 = the gap in CTC counts
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
        sbc hl,bc               ; x56
        add hl,de               ; x57
        srl h
        rr l
        srl h
        rr l
        srl h
        rr l
        ld a,(t_g)
        sub l                   ; circular distance to the CTC's count
        jp p,.ab
        neg
.ab:    cp ixl
        jr nc,.nb
        ld ixl,a
        ld (t_bg),de
.nb:    pop bc
        pop hl
        ld de,(plen)
        add hl,de
        djnz .k
        ld hl,(t_bg)
        ld de,(pel)
        add hl,de
        ld (pel),hl
        ex de,hl
        pop ix
        pop bc
        ret
; dwait: waits with interrupts on, on the game's stack, until pel reaches HL; returns with
; interrupts off on this page's stack. Each read (tick) runs with interrupts off, so no handler
; changes the NextReg select port between the select and the read. Changes A, BC, DE, HL.
dwait:  ld (d_t),hl
        ld (d_sp),sp
        ld sp,(gsp)
.l:     call tick
        ld hl,(d_t)
        ex de,hl
        or a
        sbc hl,de               ; pel - goal
        jr nc,.x
        ei                      ; a waiting interrupt comes in here
        nop
        di
        jr .l
.x:     ld sp,(d_sp)
        ret
; win: lets a waiting interrupt in, on the game's stack; interrupts off again after.
win:    ld (d_sp),sp
        ld sp,(gsp)
        ei
        nop
        di
        ld sp,(d_sp)
        ret
; pline: HL = the Next's raster line (interrupts are off). Changes A.
pline:  push bc
        ld bc,$243B
.a:     ld a,$1E
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
        jr nz,.a
        ld a,h
        and 1
        ld h,a
        pop bc
        ret
gsp:    dw 0
plen:   dw 311
pel:    dw 0
pprev:  dw 0
tgoal:  dw 0
t_c:    db 0
t_g:    db 0
t_bg:   dw 0
dfe:    dw 0
d_sp:   dw 0
d_t:    dw 0
d_goal: dw 0
d_v:    dw 0
d_n:    db 0
tq_rem: dw 0
w_src:  dw 0
w_dst:  dw 0
w_runs: dw 0
w_ixs:  dw 0
w_t:    dw 0
w_b:    db 0
w_a:    db 0
w_k:    db 0
w_vs:   db 4
w_vs2:  db 4
vword:  dw 0
ffbyte: db $FF
tq_div: dw 229
r_de:   dw 0
r_v:    dw 0
r_n:    db 0
f_cnt:  dw 0
f_src:  dw 0
        ds 64
pstack:
MAXRUN  equ 200
nrun:   db 0
inrun:  db 0
rptr:   dw 0
runs:   ds MAXRUN * 4
        align 256
dbuf:   ds 256
buf:    ds 128                  ; a flush every 128 bytes: interrupts wait no longer than that
buf_end:
        ds 128
bufb:   ds 3072                 ; dsl2: the masked pairs
abuf:   ds 1024                 ; anim: up to 32 tiles
agsp:   dw 0
        ds 32
astack:
endpage
