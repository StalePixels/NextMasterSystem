# Streets of Rage II (Europe, Brazil) (En), CRC32 04E9C089, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the 60 s and 10 min reference I/O logs
# and these extra entry points (the scanner does not follow them):
#   the bank 0 jump table at $0090-$015F (70 x JP nn, the routines the banked modules call);
#   the inline jump tables after each RST $08. $0008 is JP $37E8: POP HL; RST $30; JP (HL), and
#   RST $30 adds 2A to HL through RST $18 (ADD A,L; LD L,A; RET NC; INC H; RET), whose RET NC is
#   a branch, so pattern rule 1 does not take RST $08 as a dispatcher. Each table ends where it
#   reaches its lowest target.
# Every I/O site that no reference log ran was read by hand. The game runs code only in banks
# 0, 1, 3, 6, 9, 12 and 13; the other banks hold tables and graphics or sound data.
# Spec gaps (data/scan-verdicts.tsv): unused are the VRAM copy at $38BE and the header check at
# $3A2F, which nothing names; false are a word table in bank 1 ($4F71), a word table in bank 12
# ($31FD2) and byte patterns in the data banks.
# In play a game step takes 3 frames on both machines: the main loop waits in RST $10 ($37EB)
# until an interrupt clears $C622. In play the frame handler ($366F, $CB9B = 1) sets
# H scroll 0 for the status bar and a line interrupt at line $1E - ($CA68); the line handler
# ($36C1) sets the play area's H scroll at line 31, turns line interrupts off and ends the wait.
# No HALT, no LD A,R. The random numbers come from a shift register at $CA42 ($3A69).
name Streets of Rage II
cart 04E9C089
hz 50		; No-Intro regions Europe, Brazil
# Play has priority cells in the status bar (rows 0-3) and the fence (rows 20-23): sprites go
# behind them.
priority
# The status bar is a line interrupt split (H 0 above, the play area's H from line 32): the
# copper's map switch column must follow the line handler's write.
hsplit
# No free RST vector: the JP at $0000 becomes the vector, the game
# starts at its target.
vector 00 io
start 019C
asm 0019D 2   ; IM 1 -> IM 2
    im 2
endasm
site 001C8   ; OUT ($3F),A
site 001CA   ; IN A,($DD)
site 001D4   ; OUT ($3F),A
site 001D6   ; IN A,($DD)
site 001E4   ; OUT ($3F),A
site 00224   ; OTIR
site 00EF9   ; OUT ($BF),A
site 00EFC   ; OUT ($BF),A
site 00EFF   ; OUT ($BE),A
site 036A2   ; OUT ($BF),A
site 036A6   ; OUT ($BF),A
site 036B1   ; OUT ($BF),A
site 036B5   ; OUT ($BF),A
site 036B9   ; OUT ($BF),A
site 036BD   ; OUT ($BF),A
site 036CB   ; OUT ($BF),A
site 036CF   ; OUT ($BF),A
site 03709   ; OUT ($BF),A
site 0370C   ; OUT ($BF),A
site 03711   ; OTIR
site 0372D   ; IN A,($BF)
site 03738   ; OUT ($BF),A
site 0373C   ; OUT ($BF),A
site 03741   ; OUT ($BF),A
site 03745   ; OUT ($BF),A
site 03757   ; OUT ($BF),A
site 0375B   ; OUT ($BF),A
site 03766   ; OUT ($BF),A
site 0376A   ; OUT ($BF),A
site 0376E   ; OUT ($BF),A
site 03772   ; OUT ($BF),A
site 0377E   ; OUT ($BF),A
site 03782   ; OUT ($BF),A
site 037B2   ; OUT ($BF),A
site 037B6   ; OUT ($BF),A
site 037D7   ; OUT ($BF),A
site 037DB   ; OUT ($BF),A
site 037DF   ; OUT ($BF),A
site 037E3   ; OUT ($BF),A
site 03873   ; OUT ($BF),A
site 03877   ; OUT ($BF),A
site 03882   ; OUT ($BF),A
site 03886   ; OUT ($BF),A
site 03894   ; OUT ($BF),A
site 03897   ; OUT ($BF),A
site 0389B   ; OUT ($BE),A
site 0389E   ; OUT ($BE),A
site 038A8   ; OUT ($BF),A
site 038AB   ; OUT ($BF),A
site 038AF   ; OUT ($BE),A
site 038B6   ; OUT ($BE),A
site 038EC   ; OUT ($BF),A
site 038EF   ; OUT ($BF),A
site 038F8   ; OTIR
site 038FF   ; OUT ($BF),A
site 03902   ; OUT ($BF),A
site 0390B   ; OTIR
site 03A00   ; IN A,($DC)
site 03A1C   ; IN A,($DD)
site 03C82   ; OUT ($BF),A
site 03C85   ; OUT ($BF),A
site 03C8D   ; OTIR
site 03D07   ; OUT ($BF),A
site 03D0A   ; OUT ($BF),A
site 03D0D   ; OUT ($BE),A
site 03D1B   ; OUT ($BF),A
site 03D1E   ; OUT ($BF),A
site 03D23   ; OUT ($BE),A
site 03D2B   ; OUT ($BE),A
site 03D3B   ; OUT ($BF),A
site 03D3E   ; OUT ($BF),A
site 03D4B   ; OUT ($BE),A
site 03D53   ; OUT ($BE),A
site 03D62   ; OUT ($BE),A
site 03D6B   ; OUT ($BE),A
site 03E10   ; OUT ($BF),A
site 03E15   ; OUT ($BF),A
site 03E1A   ; OUT ($BE),A
site 03E20   ; OUT ($BE),A
site 03FC0   ; OUT ($BF),A
site 03FC3   ; OUT ($BF),A
site 04014   ; OUT ($BE),A
site 0401C   ; OUT ($BE),A
site 0402A   ; IN A,($BE)
site 04031   ; IN A,($BE)
site 040A0   ; OUT ($BF),A
site 040A3   ; OUT ($BF),A
site 04129   ; OUT ($BF),A
site 0412C   ; OUT ($BF),A
site 04231   ; IN A,($BF)
site 04238   ; OUT ($BF),A
site 0423B   ; OUT ($BF),A
site 05B18   ; OUT ($7F),A
site 05B21   ; OUT ($7F),A
site 05B31   ; OUT ($7F),A
site 05B42   ; OUT ($7F),A
site 05B6C   ; OUT ($7F),A
site 05B85   ; OUT ($7F),A
site 05FBD   ; OUT ($7F),A
site 05FC1   ; OUT ($7F),A
site 05FC5   ; OUT ($7F),A
site 05FC9   ; OUT ($7F),A
site 05FCD   ; OUT ($7F),A
site 0C305   ; OUT ($BF),A
site 0C308   ; OUT ($BF),A
site 0C30E   ; OUT ($BE),A
site 0C32E   ; OUT ($BF),A
site 0C331   ; OUT ($BF),A
site 0C337   ; IN A,($BE)
site 0C55B   ; OUT ($BF),A
site 0C55E   ; OUT ($BF),A
site 0C561   ; OUT ($BE),A
site 0C566   ; OUT ($BE),A
site 0C57C   ; OUT ($BF),A
site 0C57F   ; OUT ($BF),A
site 0C583   ; OUT ($BE),A
site 0C589   ; OUT ($BE),A
site 0C5A1   ; OUT ($BF),A
site 0C5A4   ; OUT ($BF),A
site 0C5AA   ; OUT ($BE),A
site 0C5B0   ; OUT ($BE),A
site 0C5BE   ; OUT ($BE),A
site 0C5C3   ; OUT ($BE),A
site 0C602   ; OUT ($BF),A
site 0C605   ; OUT ($BF),A
site 0C609   ; OUT ($BE),A
site 0C60F   ; OUT ($BE),A
site 0C628   ; OUT ($BF),A
site 0C62B   ; OUT ($BF),A
site 0C62E   ; OUT ($BE),A
site 0C633   ; OUT ($BE),A
site 0C64D   ; OUT ($BE),A
site 0C653   ; OUT ($BE),A
site 0C66C   ; OUT ($BF),A
site 0C66F   ; OUT ($BF),A
site 0C673   ; OUT ($BE),A
site 0C679   ; OUT ($BE),A
site 0C699   ; OUT ($BF),A
site 0C69C   ; OUT ($BF),A
site 0C6A0   ; OUT ($BE),A
site 0C6A6   ; OUT ($BE),A
site 0C6B4   ; OUT ($BE),A
site 0C6BA   ; OUT ($BE),A
site 24332   ; OUT ($BF),A
site 24335   ; OUT ($BF),A
site 24338   ; OUT ($BE),A
site 2433E   ; OUT ($BE),A
site 264A5   ; OUT ($BF),A
site 264A8   ; OUT ($BF),A
site 264AB   ; OUT ($BE),A
site 264B1   ; OUT ($BE),A
site 264E7   ; OUT ($BF),A
site 264EA   ; OUT ($BF),A
site 264ED   ; OUT ($BE),A
site 264F3   ; OUT ($BE),A
site 26521   ; OUT ($BF),A
site 26524   ; OUT ($BF),A
site 26527   ; OUT ($BE),A
site 2652D   ; OUT ($BE),A
site 2655B   ; OUT ($BF),A
site 2655E   ; OUT ($BF),A
site 26563   ; OUT ($BE),A
site 26569   ; OUT ($BE),A
site 265A2   ; OUT ($BF),A
site 265A5   ; OUT ($BF),A
site 265A8   ; OUT ($BE),A
site 265AE   ; OUT ($BE),A
site 301FA   ; OUT ($BF),A
site 301FD   ; OUT ($BF),A
site 30200   ; OUT ($BE),A
site 30206   ; OUT ($BE),A
site 30211   ; OUT ($BF),A
site 30214   ; OUT ($BF),A
site 3022B   ; OUT ($BE),A
site 30231   ; OUT ($BE),A
site 30304   ; OUT ($BF),A
site 30307   ; OUT ($BF),A
site 3030A   ; OUT ($BE),A
site 30310   ; OUT ($BE),A
site 3059B   ; OUT ($BF),A
site 3059E   ; OUT ($BF),A
site 305A4   ; OUT ($BE),A
site 305AA   ; OUT ($BE),A
site 305B0   ; OUT ($BE),A
site 305B6   ; OUT ($BE),A
site 305DD   ; OUT ($BF),A
site 305E0   ; OUT ($BF),A
site 305E4   ; OUT ($BE),A
site 305EC   ; OUT ($BE),A
site 305F5   ; OUT ($BE),A
site 305FD   ; OUT ($BE),A
site 3064B   ; OUT ($BF),A
site 3064E   ; OUT ($BF),A
site 30659   ; OUT ($BE),A
site 3065F   ; OUT ($BE),A
site 34E35   ; OUT ($BF),A
site 34E38   ; OUT ($BF),A
site 34E40   ; OUT ($BE),A
site 34E46   ; OUT ($BE),A
site 34E67   ; OUT ($BF),A
site 34E6A   ; OUT ($BF),A
site 34E6E   ; OUT ($BE),A
site 34E74   ; OUT ($BE),A
site 3511A   ; OUT ($BF),A
site 3511D   ; OUT ($BF),A
site 35128   ; OUT ($BE),A
site 3512E   ; OUT ($BE),A
site 359F8   ; OUT ($BF),A
site 359FB   ; OUT ($BF),A
site 35A03   ; OUT ($BE),A
site 35A09   ; OUT ($BE),A
site 35A15   ; OUT ($BF),A
site 35A18   ; OUT ($BF),A
site 35A20   ; OUT ($BE),A
site 35A26   ; OUT ($BE),A
mapsthl 001A2   ; LD ($FFFC),HL
mapsthl 001A8   ; LD ($FFFE),HL
mapsthl 001ED   ; LD ($FFFE),HL
mapst 03715   ; LD ($FFFF),A
mapst 0371E   ; LD ($FFFF),A
mapst 03AE2   ; LD ($FFFF),A
mapst 03C7B   ; LD ($FFFF),A
mapst 03C92   ; LD ($FFFF),A
# The H scroll splits. The interrupt handler ($366F) sets H scroll for parts of the picture
# from line interrupts, in two modes ($CB9B, set at $418C when a round starts):
# - $CB9B = 1 (every round but round 3 area 2): the frame handler writes H 0 for the status
#   bar; the line handler ($36C1, ($C63B) not 0) writes the play area's H during line 31, so
#   it shows from line 32.
# - $CB9B = $FF (round 3 area 2, $C635 = 2 and $C636 = 1): the handler at $3748 steps ($C63B)
#   through four interrupts: H 0 below the picture; register 10 only at line 10; the band's H
#   (the moving wall; ($CB9E) + 2 each frame while ($CA73) is 0) during line 22, shown from
#   line 23 ($3787, ($C63B) = 2); the play area's H during line 111, shown from line 112
#   ($37A8, ($C63B) = 3), which also turns line interrupts off.
# The handler's path at $37BF ($CB9B = 2) is not reached: no code writes 2 to $CB9B (its writers
# are $0465, 0; $059D, 1; $418C, 1 or $FF).
# Through the runtime each of these H writes ends about 2 lines after its line event, and a new
# map switch column is written into the copper list line by line from the beam's line down, so
# the lines after a split showed the old H, and in frames where the column changed the lines
# below showed wrong map columns on the right. A far call to page code costs more than a line,
# so the fix is a code cave: the two status reads at the head of the handler ($3676) become a
# JP to irqhd in free bytes at the end of bank 1 ($61E0-$7FEF are 0, and slot 1 always holds
# bank 1), which jumps back to $367A. For a split write, irqhd works out the split's first line
# L and its K = -H as the handler's path will, then:
# - while the runtime has a split segment (so the list has its switch pairs; sg_n as read at
#   the last split write, which keeps the work before the X write short), gives copper lines
#   L and L+1 K's map switch column;
# - from the start of line L-1 (at once if the beam is past it) writes K's values into NextReg
#   $2F, $30 and, with priority tiles, $16;
# - gives copper lines L+2 to L+31 K's column.
#   In MAME a WAIT written during line L-1, or a tilemap X written later than about a third into
#   it, shows only from line L+1, so the work before the X write is kept short. They cover the lines above the runtime's
#   segment, which starts where the game's write lands, and the lines the runtime rewrites
#   after the beam when the column changes; the runtime gives them the same column.
# Then it makes the two status reads through the runtime. The game's own register writes go
# through the runtime as before and leave the VDP state, h_x, pri_x and the hsplit segments as
# the game's code does; they set the same X again. At the next frame interrupt (($C63B) 0, or
# $CB9B 0) every copper line irqhd wrote goes back to the column the runtime's segments give it
# (sg_tab), so from there to the next split the copper list is as the runtime keeps it.
# irqhd runs on a stack of its own ($D340-$D37F; interrupts are off in the handler) and keeps
# its state at $D300-$D320. The game never writes $D300-$D3FF: a write watch on the reference
# over the runs of this port (power-on, intro, title, menus, options, rounds 1, 2, 4, 5 and 6,
# round 3 area 2, game over, continue, high scores) saw none.
#
# irqhd uses these runtime internals, with their addresses in the runtime map of public/ at
# 9753a1e (build/rt/runtime.map); an engine change that moves one must change this cave:
#   vdp_regs $E03B     the VDP registers (0: bit 4 line interrupts, bit 6 locked rows; 1: bit 6
#                      display)
#   fw_flags $E09E     bit 0 priority tiles, bit 5 hsplit
#   m224 $E08F         224-line mode
#   cur_mmu $E02D      the game's MMU0 page, put back after the reads of part 3
#   sg_n $08A6, sg_tab $08A7
#                      in runtime part 3 (page FW3_PAGE, 100, mapped at $0000 for the reads):
#                      the number of hsplit segments, and per segment (SG_MAX 8) its first
#                      line, its copper column and a flag, then 192
#   hscroll_set (fw2)  X = K - 34 mod 320 into NextReg $2F/$30 and K - 2 into $16 (Layer 2, not
#                      in 224-line mode); map switch column 39 for K <= 64, else (291 - K) / 8
#   cop_wlines (fw3)   the first byte of each line's WAIT, $80 + 2 x column, at copper address
#                      6 + 10 x line (NextReg $62 = $C0 + high byte, $61, $60)
label irqhd 07000
asm 03676 4   ; IN A,($BF); IN A,($BF) -> JP irqhd, which returns to $367A
    jp irqhd
endasm
asm 07000 512  ; irqhd, in free bytes of bank 1
        OPT --zxnext            ; NEXTREG, MUL
VREGS   equ $E03B
FWFL    equ $E09E
M224    equ $E08F
CURMMU  equ $E02D
SGN     equ $08A6
SGTAB   equ $08A7
FW3PG   equ 100
IHLO    equ $D300               ; first copper line irqhd wrote since the last frame interrupt
IHHI    equ $D301               ; last line + 1 (0: none)
IHL     equ $D302               ; the split's first line L
IHK     equ $D303               ; its K
IHCOL   equ $D304               ; K's column
IHSP    equ $D305               ; the game's SP
IHN     equ $D307               ; sg_n
IHTAB   equ $D308               ; a copy of sg_tab, 25 bytes
IHSTK   equ $D380               ; the cave's stack, $D340-$D37F
        ld (IHSP),sp            ; irqhd
        ld sp,IHSTK
        push de
        push hl
        ld a,(FWFL)             ; hsplit
        and $20
        jp z,.frame
        ld a,(M224)
        or a
        jp nz,.frame
        ld a,(VREGS)
        and $50
        cp $10                  ; line interrupts on, no locked rows
        jp nz,.frame
        ld a,(VREGS+1)
        and $40
        jp z,.frame
        ld a,($C63B)
        ld e,a
        ld a,($CB9B)
        cp 1
        jr z,.m1
        rla
        jp nc,.frame
        ld a,e                  ; $CB9B negative: state 2 (band) or 3 (play area)
        cp 3
        jr z,.s3
        cp 2
        jp nz,.frame
        ld a,($CA73)            ; the band: K = ($CB9E) + 2 unless ($CA73)
        or a
        ld a,($CB9E)
        jr nz,.s2k
        add a,2
.s2k:   ld d,23
        jr .go
.s3:    ld d,112                ; the play area after the band
        jr .k65
.m1:    ld a,e                  ; $CB9B = 1: the line handler's path when ($C63B) is not 0
        or a
        jp z,.frame
        ld d,32
.k65:   ld a,($CA65)
.go:    ld (IHK),a
        ld e,a
        ld a,d
        ld (IHL),a
        ld a,e                  ; K's column
        cp 65
        ld d,39
        jr c,.cl
        ld d,a
        ld a,255&(291-256)
        sub d
        rrca
        rrca
        rrca
        and $1F
        ld d,a
.cl:    ld a,d
        ld (IHCOL),a
        ld a,(IHK)              ; HL = X = K - 34 mod 320
        ld e,a
        ld d,0
        ld hl,-34
        add hl,de
        bit 7,h
        jr z,.xp
        ld de,320
        add hl,de
.xp:    push hl
        ld a,(IHN)              ; sg_n at the last split write
        cp 2
        jr c,.xw                ; no split segment: the list may have no switch pairs
        ld a,(IHCOL)            ; copper lines L and L+1 first
        ld d,a
        ld a,(IHL)
        ld b,a
        ld e,2
        call wlines
.xw:    pop hl
        ld a,(IHL)
        dec a
        ld b,a
.xl:    call sline              ; line L-1 (at once past it, or below the picture)
        cp b
        jr c,.xl
        ld a,h
        nextreg $2F,a
        ld a,l
        nextreg $30,a
        ld a,(FWFL)
        rra
        jr nc,.c1
        ld a,(IHK)
        sub 2
        nextreg $16,a
.c1:    call sgread
        ld a,(IHN)
        cp 2
        ld a,h
        ld (IHN),a
        jp c,.st
        ld a,(IHHI)             ; note the lines written
        or a
        ld a,(IHL)
        jr z,.lo
        ld hl,IHLO
        cp (hl)
        jr nc,.lo2
.lo:    ld (IHLO),a
.lo2:   add a,32
        ld hl,IHHI
        cp (hl)
        jr c,.c2
        ld (hl),a
.c2:    ld a,(IHCOL)            ; lines L+2 to L+31
        ld d,a
        ld a,(IHL)
        add a,2
        ld b,a
        ld e,30
        call wlines
        jr .st
.frame: ld a,($CB9B)            ; at the frame interrupt, the copper lines written go back
        or a                    ; to the runtime's segment columns
        jr z,.fr
        ld a,($C63B)
        or a
        jr nz,.st
.fr:    ld a,(IHHI)
        or a
        jr z,.st
        push ix
        ld c,a
        xor a
        ld (IHHI),a
        call sgcopy
        ld a,(IHLO)
        ld b,a                  ; B = line, C = last + 1
        ld e,b
        ld d,10
        mul d,e
        ld hl,6
        add hl,de
        ld ix,IHTAB             ; IX = the segment that holds line B
.fl:    ld a,b
        cp (ix+3)               ; the next segment's first line (192 past the last)
        jr c,.fc
        inc ix
        inc ix
        inc ix
        jr .fl
.fc:    ld a,(ix+1)
        add a,a
        or $80
        ld d,a
        ld a,h
        or %11000000
        nextreg $62,a
        ld a,l
        nextreg $61,a
        ld a,d
        nextreg $60,a
        ld de,10
        add hl,de
        inc b
        ld a,b
        cp c
        jr c,.fl
        pop ix
.st:    pop hl
        pop de
        rst $00                 ; IN A,($BF) twice, as the game
        db $0D
        rst $00
        db $0D
        ld sp,(IHSP)
        jp $367A
; H = sg_n from the runtime's part 3: MMU0 holds it for the read (interrupts are off).
; Uses A, H.
sgread: ld a,FW3PG
        nextreg $50,a
        ld a,(SGN)
        ld h,a
        ld a,(CURMMU)
        nextreg $50,a
        ret
; IHTAB = a copy of sg_tab (first line, column, write seen for each segment, then 192) from the
; runtime's part 3, mapped in MMU0 for the copy. Uses A, BC, DE, HL.
sgcopy: push bc
        ld a,FW3PG
        nextreg $50,a
        ld hl,SGTAB
        ld de,IHTAB
        ld bc,3*8+1
        ldir
        ld a,(CURMMU)
        nextreg $50,a
        pop bc
        ret
; D = column, B = first line, E = lines: the first byte of each line's WAIT, as cop_wlines
; writes it. Uses A, D, E, HL.
wlines: ld a,d
        add a,a
        or $80
        ld d,a
        push de
        ld e,b
        ld d,10
        mul d,e
        ld hl,6
        add hl,de
        pop de
.one:   ld a,h
        or %11000000
        nextreg $62,a
.l:     ld a,l
        nextreg $61,a
        ld a,d
        nextreg $60,a
        ld a,l
        add a,10
        ld l,a
        jr c,.c
        dec e
        jr nz,.l
        ret
.c:     inc h
        dec e
        jr nz,.one
        ret
; A = the beam's SMS line in 192-line mode (NextReg $1E, $1F), 255 below the picture.
; Keeps the other registers.
sline:  push bc
        push de
.rd:    ld bc,$243B
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        ld e,a
        dec b
        ld a,$1F
        out (c),a
        inc b
        in a,(c)
        ld d,a
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        cp e
        jr nz,.rd
        rra
        ld a,d
        jr c,.out
        cp 192
        jr c,.ok
.out:   ld a,255
.ok:    pop de
        pop bc
        ret
endasm

# Streets of Rage II (Europe, Brazil) (En).cht, "Infinite Lives P1"
poke "Infinite lives"
ar 00CC-FF09
endpoke

# Streets of Rage II (Europe, Brazil) (En).cht, "Infinite Time"
poke "Infinite time"
ar 00CD-F909
ar 00CD-FA09
endpoke

# Streets of Rage II (Europe, Brazil) (En).cht, "Infinite Energy P1"
poke "Infinite energy"
ar 00CC-E727
endpoke
