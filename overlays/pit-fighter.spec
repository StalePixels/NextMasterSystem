# Pit-Fighter (Europe), CRC32 B840A446, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (60 s and 600 s of
# random input) and entry points for the far calls (below).
# Decisions:
# - $0008-$0394 is a development monitor that the game never runs (no RST $08, $20 or $28
#   and no jump into it in either log). $0010-$0012 are zero bytes there, so $0010 is the io
#   vector. The game never runs RST $00 or RST $10.
# - RST $18 ($0051) is the far call: slot 2 gets bank ($0016) OR E, with $80 at $0016.
#   The scanner does not read $0016, so the far calls' targets are given as entry points.
# - At $1C3C the game copies 2500 bytes from bank 31 $B480 (offset $7F480) to $C000-$C9C3.
#   The frame and line interrupt handler runs there: $0038 jumps to $C387, which reads the
#   reset button and goes on at $C5C0. Its I/O instructions are patched in the bank 31
#   source, so the copy carries the RST and inline code into RAM.
# - $C3AB-$C45F in that copy is code nothing runs (a copy of $03AB with a cartridge
#   check); its mapper stores are left as they are: the bytes are the RAM's initial
#   values.
name Pit-Fighter
cart B840A446
hz 50		; No-Intro region Europe
vector 10 io
rastercode pit-fighter-raster.asm
asm 00396 2   ; IM 1 -> IM 2
    im 2
endasm
site 003A6   ; IN A,($BF)
site 00536   ; OUT (C),A
site 0053C   ; OUT (C),A
otir 00542   ; OUTI
site 0054B   ; OUT (C),A
site 00551   ; OUT (C),A
otir 00557   ; OUTI
site 006D2   ; OUT (C),A
site 006D9   ; OUT (C),A
site 006E0   ; OUT ($BE),A
site 006E8   ; OUT ($BF),A
site 006EF   ; OUT ($BF),A
site 00714   ; OUT (C),A
site 0071B   ; OUT (C),A
site 00722   ; OUT ($BE),A
site 0072B   ; OUT ($BE),A
site 0073F   ; OUT (C),A
site 00746   ; OUT (C),A
site 0074D   ; OUT ($BE),A
site 00756   ; OUT ($BE),A
site 0077E   ; OUT (C),A
site 00785   ; OUT (C),A
site 0078C   ; OUT ($BE),A
site 007B2   ; OUT ($BF),A
site 007BA   ; OUT ($BF),A
site 007C3   ; IN A,($7E)
site 007D3   ; IN A,($7E)
site 007DB   ; OUT ($BF),A
site 007E2   ; OUT ($BF),A
site 007E6   ; OUT ($BE),A
site 007F0   ; OUT ($BF),A
site 007F7   ; OUT ($BF),A
site 007FA   ; OUT ($BE),A
site 00811   ; OUT ($BF),A
site 00818   ; OUT ($BF),A
site 0081A   ; IN A,($7E)
site 0082A   ; IN A,($7E)
site 00831   ; OUT ($BF),A
site 00838   ; OUT ($BF),A
site 0083E   ; OUT ($BE),A
site 008B4   ; OUT ($BF),A
site 008BB   ; OUT ($BF),A
site 008C4   ; OUT ($BE),A
site 008CA   ; OUT ($BE),A
site 008CD   ; IN A,($DC)
site 008DF   ; IN A,($DD)
site 00B0C   ; OUT (C),A
site 00B13   ; OUT (C),A
site 00B1A   ; OUT ($BE),A
site 00B2B   ; OUT ($BF),A
site 00B2F   ; OUT ($BF),A
site 00B46   ; OUTI
site 00B48   ; OUTI
site 00B4B   ; OUTI
site 00B4D   ; OUTI
site 00B50   ; OUTI
site 00B52   ; OUTI
site 00B55   ; OUTI
site 00B57   ; OUTI
site 00B5A   ; OUTI
site 00B5C   ; OUTI
site 00B5F   ; OUTI
site 00B61   ; OUTI
site 00B64   ; OUTI
site 00B66   ; OUTI
site 00B69   ; OUTI
site 00B6B   ; OUTI
site 00B6E   ; OUTI
site 00B70   ; OUTI
site 00B73   ; OUTI
site 00B75   ; OUTI
site 00B78   ; OUTI
site 00B7A   ; OUTI
site 00B7D   ; OUTI
site 00B7F   ; OUTI
site 00B82   ; OUTI
site 00B84   ; OUTI
site 00B87   ; OUTI
site 00B89   ; OUTI
site 00B8C   ; OUTI
site 00B8E   ; OUTI
site 00B91   ; OUTI
site 00B93   ; OUTI
site 00B96   ; OUTI
site 00B98   ; OUTI
site 00B9B   ; OUTI
site 00B9D   ; OUTI
site 00BA0   ; OUTI
site 00BA2   ; OUTI
site 00BA5   ; OUTI
site 00BA7   ; OUTI
site 00BAA   ; OUTI
site 00BAC   ; OUTI
site 00BAF   ; OUTI
site 00BB1   ; OUTI
site 00BB4   ; OUTI
site 00BB6   ; OUTI
site 00BB9   ; OUTI
site 00BBB   ; OUTI
site 00BBE   ; OUTI
site 00BC0   ; OUTI
site 00BC3   ; OUTI
site 00BC5   ; OUTI
site 00BC8   ; OUTI
site 00BCA   ; OUTI
site 00BCD   ; OUTI
site 00BCF   ; OUTI
site 00BD2   ; OUTI
site 00BD4   ; OUTI
site 00BD7   ; OUTI
site 00BD9   ; OUTI
site 00BDC   ; OUTI
site 00BDE   ; OUTI
site 00BE1   ; OUTI
site 00BE3   ; OUTI
site 00BE6   ; OUTI
site 00BE8   ; OUTI
site 00BEB   ; OUTI
site 00BED   ; OUTI
site 00BF0   ; OUTI
site 00BF2   ; OUTI
site 00BF5   ; OUTI
site 00BF7   ; OUTI
site 00BFA   ; OUTI
site 00BFC   ; OUTI
site 00BFF   ; OUTI
site 00C01   ; OUTI
site 00C04   ; OUTI
site 00C06   ; OUTI
site 00C09   ; OUTI
site 00C0B   ; OUTI
site 00C0E   ; OUTI
site 00C10   ; OUTI
site 00C13   ; OUTI
site 00C15   ; OUTI
site 00C18   ; OUTI
site 00C1A   ; OUTI
site 00C1D   ; OUTI
site 00C1F   ; OUTI
site 00C22   ; OUTI
site 00C24   ; OUTI
site 00C27   ; OUTI
site 00C29   ; OUTI
site 00C2C   ; OUTI
site 00C2E   ; OUTI
site 00C31   ; OUTI
site 00C33   ; OUTI
site 00C36   ; OUTI
site 00C38   ; OUTI
site 00C3B   ; OUTI
site 00C3D   ; OUTI
site 00C40   ; OUTI
site 00C42   ; OUTI
site 00C45   ; OUTI
site 00C47   ; OUTI
site 00C4A   ; OUTI
site 00C4C   ; OUTI
site 00C4F   ; OUTI
site 00C51   ; OUTI
site 00C54   ; OUTI
site 00C56   ; OUTI
site 00C59   ; OUTI
site 00C5B   ; OUTI
site 00C5E   ; OUTI
site 00C60   ; OUTI
site 00C63   ; OUTI
site 00C65   ; OUTI
site 00C68   ; OUTI
site 00C6A   ; OUTI
site 00C6D   ; OUTI
site 00C6F   ; OUTI
site 00C72   ; OUTI
site 00C74   ; OUTI
site 00C77   ; OUTI
site 00C79   ; OUTI
site 00C7C   ; OUTI
site 00C7E   ; OUTI
site 00C81   ; OUTI
site 00C83   ; OUTI
site 00C87   ; OUT ($BF),A
site 00C8B   ; OUT ($BF),A
site 00C9E   ; OUTI
site 00CA2   ; OUTI
site 00CA6   ; OUTI
site 00CAA   ; OUTI
site 00CAE   ; OUTI
site 00CB2   ; OUTI
site 00CB6   ; OUTI
site 00CBA   ; OUTI
site 00CBE   ; OUTI
site 00CC2   ; OUTI
site 00CC6   ; OUTI
site 00CCA   ; OUTI
site 00CCE   ; OUTI
site 00CD2   ; OUTI
site 00CD6   ; OUTI
site 00CDA   ; OUTI
site 00CDE   ; OUTI
site 00CE2   ; OUTI
site 00CE6   ; OUTI
site 00CEA   ; OUTI
site 00CEE   ; OUTI
site 00CF2   ; OUTI
site 00CF6   ; OUTI
site 00CFA   ; OUTI
site 00CFE   ; OUTI
site 00D02   ; OUTI
site 00D06   ; OUTI
site 00D0A   ; OUTI
site 00D0E   ; OUTI
site 00D12   ; OUTI
site 00D16   ; OUTI
site 00D1A   ; OUTI
site 00D1E   ; OUTI
site 00D22   ; OUTI
site 00D26   ; OUTI
site 00D2A   ; OUTI
site 00D2E   ; OUTI
site 00D32   ; OUTI
site 00D36   ; OUTI
site 00D3A   ; OUTI
site 00D3E   ; OUTI
site 00D42   ; OUTI
site 00D46   ; OUTI
site 00D4A   ; OUTI
site 00D4E   ; OUTI
site 00D52   ; OUTI
site 00D56   ; OUTI
site 00D5A   ; OUTI
site 00D5E   ; OUTI
site 00D62   ; OUTI
site 00D66   ; OUTI
site 00D6A   ; OUTI
site 00D6E   ; OUTI
site 00D72   ; OUTI
site 00D76   ; OUTI
site 00D7A   ; OUTI
site 00D7E   ; OUTI
site 00D82   ; OUTI
site 00D86   ; OUTI
site 00D8A   ; OUTI
site 00D8E   ; OUTI
site 00D92   ; OUTI
site 00D96   ; OUTI
site 00D9A   ; OUTI
site 00DA7   ; OUT (C),A
site 00DFE   ; IN A,($BF)
site 00E6E   ; IN A,($BF)
site 013BF   ; OUT ($BF),A
site 013C6   ; OUT ($BF),A
site 013CD   ; IN A,($BE)
site 013ED   ; OTIR
site 0199D   ; OUT ($BF),A
site 019A4   ; OUT ($BF),A
site 019AB   ; OUT ($BE),A
site 019B6   ; OUT ($BE),A
site 019BB   ; OUT ($BE),A
site 019C2   ; OUT ($BF),A
site 019C9   ; OUT ($BF),A
site 019D1   ; OUT ($BE),A
site 019D6   ; OUT ($BE),A
site 019E0   ; OUT ($BE),A
site 01A2A   ; OUT ($BF),A
site 01A32   ; OUT ($BF),A
site 01A3F   ; OUT ($BE),A
site 01BC1   ; OUT ($BF),A
site 01BC8   ; OUT ($BF),A
site 01BCE   ; OUT ($BF),A
site 01BD5   ; OUT ($BF),A
site 01BDB   ; OUT ($BF),A
site 01BE2   ; OUT ($BF),A
site 01BE8   ; OUT ($BF),A
site 01BEF   ; OUT ($BF),A
site 01BF5   ; OUT ($BF),A
site 01BFC   ; OUT ($BF),A
site 01C02   ; OUT ($BF),A
site 01C09   ; OUT ($BF),A
site 01C0F   ; OUT ($BF),A
site 01C16   ; OUT ($BF),A
site 01C7F   ; OUT ($BF),A
site 01C86   ; OUT ($BF),A
site 01C8C   ; OUT ($BF),A
site 01C93   ; OUT ($BF),A
site 01C99   ; OUT ($BF),A
site 01CA0   ; OUT ($BF),A
site 01CE2   ; OUT ($BF),A
site 01CE9   ; OUT ($BF),A
site 01E3F   ; OUT ($BF),A
site 01E46   ; OUT ($BF),A
site 028C6   ; OUT ($BF),A
site 028CD   ; OUT ($BF),A
site 02915   ; OUT ($BF),A
site 0291C   ; OUT ($BF),A
site 029C4   ; OUT ($BF),A
site 029CB   ; OUT ($BF),A
site 02A47   ; OUT ($BF),A
site 02A4E   ; OUT ($BF),A
site 03136   ; OUT ($BF),A
site 0313E   ; OUT ($BF),A
site 03143   ; OUT ($BE),A
site 0314A   ; OUT ($BF),A
site 03152   ; OUT ($BF),A
site 03157   ; OUT ($BE),A
site 0315E   ; OUT ($BF),A
site 03166   ; OUT ($BF),A
site 0316B   ; OUT ($BE),A
site 0317D   ; OUT ($BF),A
site 03185   ; OUT ($BF),A
site 0318A   ; OUT ($BE),A
site 03191   ; OUT ($BF),A
site 03199   ; OUT ($BF),A
site 0319E   ; OUT ($BE),A
site 031A5   ; OUT ($BF),A
site 031AD   ; OUT ($BF),A
site 031B2   ; OUT ($BE),A
site 03268   ; OUT ($BF),A
site 03270   ; OUT ($BF),A
site 03282   ; OUT (C),A
site 0328A   ; OUT (C),A
site 032AC   ; OUT ($BF),A
site 032B3   ; OUT ($BF),A
site 0337A   ; OUT ($BF),A
site 03384   ; OUT ($BF),A
site 0338C   ; OUT ($BE),A
site 03395   ; OUT ($BE),A
site 033FB   ; OUT ($BF),A
site 03405   ; OUT ($BF),A
site 0340D   ; OUT ($BE),A
site 03416   ; OUT ($BE),A
site 035DB   ; OUT ($BF),A
site 035E0   ; OUT ($BF),A
site 035FA   ; OUT (C),E
site 03600   ; OUT (C),D
site 03649   ; OUT ($BF),A
site 03650   ; OUT ($BF),A
site 039A2   ; OUT ($BF),A
site 039A9   ; OUT ($BF),A
site 03AA7   ; OUT ($BF),A
site 03AAE   ; OUT ($BF),A
site 11B56   ; OUT ($BF),A
site 11B5D   ; OUT ($BF),A
site 11B62   ; OUT ($BE),A
site 136AC   ; OUT ($BF),A
site 136B3   ; OUT ($BF),A
site 1373C   ; OUT ($BF),A
site 13743   ; OUT ($BF),A
site 1374F   ; OUT ($BF),A
site 13756   ; OUT ($BF),A
site 1377D   ; IN A,($7E)
site 1378D   ; IN A,($7E)
site 13798   ; OUT ($BF),A
site 1379F   ; OUT ($BF),A
site 137A3   ; OUT ($BE),A
site 63796   ; OUT ($7F),A
site 6379A   ; OUT ($7F),A
site 6379E   ; OUT ($7F),A
site 637A2   ; OUT ($7F),A
site 637D9   ; OUT ($7F),A
site 637E4   ; OUT ($7F),A
site 63813   ; OUT ($7F),A
site 63825   ; OUT ($7F),A
site 6382D   ; OUT ($7F),A
site 63845   ; OUT ($7F),A
site 6384C   ; OUT ($7F),A
site 63995   ; OUT ($7F),A
site 6BD8C   ; OUT ($BF),A
site 6BD93   ; OUT ($BF),A
site 6FA14   ; OUT ($BF),A
site 6FA1B   ; OUT ($BF),A
site 7386D   ; OUT ($BF),A
site 73874   ; OUT ($BF),A
site 74177   ; OUT ($7F),A
site 7417B   ; OUT ($7F),A
site 7417F   ; OUT ($7F),A
site 74183   ; OUT ($7F),A
site 741F3   ; OUT ($7E),A
site 74235   ; OUT ($7F),A
site 74245   ; OUT ($7F),A
site 74257   ; OUT ($7F),A
site 7DD7B   ; OUT ($BF),A
site 7DD82   ; OUT ($BF),A
site 7DDB8   ; OUT ($BF),A
site 7DDBF   ; OUT ($BF),A
site 7DDF0   ; OUT ($BF),A
site 7DDF7   ; OUT ($BF),A
site 7DDFD   ; OUT ($BF),A
site 7DE04   ; OUT ($BF),A
mapst 00056   ; LD ($FFFF),A
mapst 00398   ; LD ($FFFC),A
mapst 0039B   ; LD ($FFFD),A
mapst 0039F   ; LD ($FFFE),A
mapst 003A3   ; LD ($FFFF),A
mapst 000D1   # LD ($FFFF),A; after POP AF; 10 bytes of valid code before it
mapst 000DF   # LD ($FFFF),A; after LD A,$CE; JP/CALL target from $3E8EA $3EEDA
mapst 0020D   # LD ($FFFF),A; JP/CALL target from $222EE $2366E; 32 bytes of valid code before it
mapst 0021F   # LD ($FFFF),A; after LD A,$CE; 32 bytes of valid code before it
mapst 00230   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 00255   # LD ($FFFF),A; after LD A,$CE
mapst 00261   # LD ($FFFF),A; after LD A,$82; 16 bytes of valid code before it
mapst 0027A   # LD ($FFFF),A; after LD A,$CE
mapst 0028D   # LD ($FFFF),A; after LD A,$00; 23 bytes of valid code before it
mapst 002D9   # LD ($FFFF),A; after LD A,$CE
mapst 002F0   # LD ($FFFF),A; after LD A,$82; JP/CALL target from $68059; 27 bytes of valid code before it
mapst 002FC   # LD ($FFFF),A; after LD A,$CE; JP/CALL target from $0CDDD $14631 $204D9 $206A1
mapst 0031B   # LD ($FFFF),A; after LD A,$82; 32 bytes of valid code before it
mapst 0032A   # LD ($FFFF),A; after LD A,$CE
mapst 00343   # LD ($FFFF),A; after LD A,$82; 29 bytes of valid code before it
mapst 009BA   # LD ($FFFF),A; after LD A,($C13A); 32 bytes of valid code before it
mapst 009E8   # LD ($FFFF),A; after LD A,($C142); 32 bytes of valid code before it
site 7F808   ; IN A,($DD)    $C388, the reset button in the interrupt entry
site 7FA5B   ; OUT ($BF),A   $C5DB
site 7FA62   ; OUT ($BF),A   $C5E2
site 7FA70   ; OUT ($BF),A   $C5F0
site 7FA77   ; OUT ($BF),A   $C5F7
site 7FB0D   ; OUT ($BF),A   $C68D
site 7FB15   ; OUT ($BF),A   $C695
# Screen holds. The game holds a screen with LDIRs that copy all 64K onto itself (HL = DE = 0,
# BC = 0): three at $9A68 and three at $9A84 (bank 4), eight at $B724 (bank 4). On the
# reference each three take 4.61 million cycles and the eight 12.37 million, interrupts
# included: 65 and 173 frames of a PAL Master System (71,364 cycles). The Next's CPU runs
# them in a fraction of that. Each run becomes that many frame waits: clear $C3A2, wait for
# the frame handler to set it (as the game's own waits at $0773 and $0855 do).
asm 11A5F 15        ; LD HL,0 : LD DE,0 : LD BC,0 : LDIR x3
    ld b,65
1:  xor a
    ld ($C3A2),a
2:  ld a,($C3A2)
    or a
    jr z,2B
    djnz 1B
endasm
asm 11A7B 15        ; LD HL,0 : LD DE,0 : LD BC,0 : LDIR x3
    ld b,65
1:  xor a
    ld ($C3A2),a
2:  ld a,($C3A2)
    or a
    jr z,2B
    djnz 1B
endasm
asm 1371B 25        ; LD HL,0 : LD DE,0 : LD BC,0 : LDIR x8
    ld b,173
1:  xor a
    ld ($C3A2),a
2:  ld a,($C3A2)
    or a
    jr z,2B
    djnz 1B
endasm
# The game puts back the first two bytes of the RAM handler, PUSH AF and the IN opcode, with
# LD HL,$DBF5 : LD ($C5C0),HL at $1E76, $2E1C, $31F7 and $32C2. That would undo the site at
# $C5C1 (7FA41): the stored IN opcode becomes the io RST.
poke 01E78 DB D7   ; LD HL,$DBF5 -> LD HL,$D7F5
poke 02E1E DB D7
poke 031F9 DB D7
poke 032C4 DB D7
# Line interrupts. In a fight register 10 is $1F: a line interrupt every 32 lines. The handler
# at $C5C0 reads the status; with bit 7 clear it is a line interrupt, and when the V counter
# reads $1F (the first one) it sets the H scroll for the play area below the status bar and
# runs the game's step ($C683-$C6C9). On the Next the handler reads the V counter about two
# lines later ($21), so the step never ran; and the interrupt of line 191 comes after the
# frame flag is set, so the frame part (the fight clock, the joypads, the sprites) ran twice
# a frame. Page 0 makes the two decisions:
# - irq (at $C5C1, in place of IN A,($BF) : LD ($C39C),A : RLA : JP NC,$C676): reads the
#   status and stores it as the game does. A frame flag runs the frame part only once after
#   the frame's line interrupts (v_lf, set by each line interrupt); with line interrupts off
#   in register 0 (vdp_regs+0 bit 4) every frame flag runs it. Returns A and carry as RLA
#   leaves them, or A = $80 and no carry for a second frame flag: the line part then leaves
#   at its AND $C0, before it reads the V counter (a V counter read below the picture runs
#   the runtime's once-a-frame work).
# - split (at $C683, in place of IN A,($7E) : CP $1F): Z when the V counter reads $1F-$2E.
asm 7FA41 9         ; $C5C1
    rst $10
    db far_io, pg_irq, ent_irq
    jp nc,$C676
endasm
asm 7FB03 4         ; $C683
    rst $10
    db far_io, pg_split, ent_split
endasm
page 0 irq split
irq:    rst $10
        db $0D                  ; IN A,($BF) through the runtime
        ld ($C39C),a
        bit 7,a
        jr nz,.frame
        ld a,1
        ld (v_lf),a
        ld a,($C39C)
        rla                     ; bit 7 clear: no carry
        ret
.frame: ld a,(vdp_regs)
        bit 4,a
        jr z,.go                ; line interrupts off
        ld a,($C354)
        or a
        jr nz,.go               ; a fight: the rastercode table, no line interrupts
        ld a,(v_lf)
        or a
        jr z,.skip
.go:    xor a
        ld (v_lf),a
        ld a,($C39C)
        rla                     ; bit 7 set: carry
        ret
.skip:  ld a,$80                ; no carry; bit 7 makes the line part leave
        or a                    ; before its V counter read
        ret
split:  rst $10
        db $0A                  ; IN A,($7E) through the runtime
        sub $1F
        cp $10
        jr nc,.no
        xor a                   ; Z
        ret
.no:    or 1                    ; NZ
        ret
v_lf:   db 0
endpage
# A fight. With line interrupts on and $C354 not 0 the rastercode routine
# pit-fighter-raster.asm gives the H scroll of every line, and the game gets no line
# interrupts; the step that the line 31 interrupt ran ($C697-$C6CB) runs at the end of the
# frame handler instead. The frame handler's end, LD A,1 : LD ($C3A2),A at $C665, jumps to a
# cave at $C580 in the RAM image (bytes the game never writes, zero in the cart): it sets
# $C3A2 as before, and in a fight keeps $C34E in $C5BE for the rastercode routine and runs
# $C697 with a return to the frame handler's end at $C66A. $C697 ends with POP AF : EI : RET,
# so the cave pushes its return and an AF; the cave turns interrupts off again after it.
asm 7FAE5 5         ; $C665
    jp $C580
endasm
asm 7FA00 36        ; $C580-$C5A3 in RAM
    disp $C580
    ld a,1
    ld ($C3A2),a
    ld a,(vdp_regs)
    bit 4,a
    jr z,.out
    ld a,($C354)
    or a
    jr z,.out
    ld a,($C34E)
    ld ($C5BE),a
    ld hl,.cont
    push hl
    push af
    jp $C697
.cont:
    di
.out:
    jp $C66A
    ent
endasm
# $0DB4 is a frame handler that bank 28 installs ($B878 stores it at $C391, the JP in the
# interrupt entry): the same start as $C5C0, so the same page entry makes its decision.
asm 00DB5 9         ; IN A,($BF) : LD ($C39C),A : RLA : JP NC,$0DFA
    rst $10
    db far_io, pg_irq, ent_irq
    jp nc,$0DFA
endasm

# Pit-Fighter (Europe).cht, "Infinite Energy": RAM $C751 holds player 1's energy, held at $FF
poke "Infinite energy"
ar 00C7-51FF
endpoke
