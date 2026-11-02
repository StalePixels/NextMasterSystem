# Super Monaco GP (Europe, Brazil) (En), CRC32 55BF81A0, 256K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of
# attract mode (30 minutes, no input) and play (10 minutes, start script and random input).
# Byte scan I/O patterns judged code and patched (no recording ran them, and no call to them
# was found): $021B-$0239 (two VRAM block writers after the RST $30 routine), $0252-$0298 (the
# FM sound unit check; the game calls only the RET at $0251), $0611-$0619, $0EEB-$0F05 (VRAM
# writers with delays), $6F94 (a digit written after RST $08 in a bank 1 routine), bank 11
# $B982-$B98E (VRAM writer after the module at $B942).
# Byte scan I/O patterns judged not code (verdicts in data/scan-verdicts.tsv): every hit in
# banks 4-15 except those above is graphics, map or sound data.
# The cart area stores and the jump into RAM in bank 15 $88E5-$89ED are data: the sound
# command table at $86A8 is read past its end into a table of pointers.
# The two unresolved calls at $1954 and $1965 go to $3AEC, which jumps through the word table
# at $3C7C; its targets $3B07, $3C1A and $3C41 are all reached by the scan.
name Super Monaco GP
cart 55BF81A0
hz 50		; No-Intro regions Europe, Brazil
# The line interrupt handler sets H scroll on almost every line of the two roads of the split
# screen (lines 72-117 and 144-189 in the race). A rastercode routine builds the per-line table.
# The game does not depend on its line interrupts otherwise: only the handler and the frame
# handler use the event counter $C039.
rastercode supermonacogp-raster.asm
# No priority: no reference VRAM dump (attract, menus, race) holds a priority cell.
# No tilecache: race frames in the runtime, median 39.4% of a frame without it, 39.5% with it.
# No hsplit: outside the race the game has at most one line interrupt split a frame, with
# no band of wrong map columns seen.
# No free RST vector: the JP at $0000 becomes the vector, the game
# starts at its target.
vector 00 io
start 00F1
asm 000F2 2   ; IM 1 -> IM 2
    im 2
endasm
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0006D   ; OUT ($BF),A
site 00071   ; OUT ($BF),A
site 00079   ; OUT ($BF),A
site 0007D   ; OUT ($BF),A
site 00081   ; OUT ($BF),A
site 00085   ; OUT ($BF),A
site 00092   ; OUT ($BF),A
site 00096   ; OUT ($BF),A
site 0009A   ; OUT ($BF),A
site 0009E   ; OUT ($BF),A
site 000A5   ; OUT ($BF),A
site 000A9   ; OUT ($BF),A
site 000B3   ; OUT ($BF),A
site 000B7   ; OUT ($BF),A
site 000C2   ; OUT ($BF),A
site 000C6   ; OUT ($BF),A
site 000CA   ; OUT ($BF),A
site 000CE   ; OUT ($BF),A
site 000D9   ; OUT ($BF),A
site 000DD   ; OUT ($BF),A
site 000E8   ; OUT ($BF),A
site 000EC   ; OUT ($BF),A
site 001E4   ; OUT ($BE),A
site 001EA   ; OUT ($BE),A
site 001F9   ; OTIR
site 00215   ; OUT ($BF),A
site 00218   ; OUT ($BF),A
site 00242   ; OUT ($BE),A
site 00279   ; OUT ($F2),A
site 0027C   ; IN A,($F2)
site 0028E   ; OUT ($F2),A
site 00296   ; OUT ($3E),A
site 002B8   ; OUT ($3F),A
site 002BA   ; IN A,($DD)
site 002C4   ; OUT ($3F),A
site 002C6   ; IN A,($DD)
site 002CF   ; OUT ($3F),A
site 002F8   ; OUT ($BF),A
site 002FC   ; OUT ($BF),A
site 00301   ; OUT ($BF),A
site 00305   ; OUT ($BF),A
site 0030A   ; OUT ($BF),A
site 0030E   ; OUT ($BF),A
site 0036E   ; IN A,($DD)
site 003F8   ; OUT ($BE),A
site 003FC   ; OUT ($BE),A
site 00401   ; OUT ($BE),A
site 00405   ; OUT ($BE),A
site 0040A   ; OUT ($BE),A
site 0040E   ; OUT ($BE),A
site 00417   ; OUT ($BE),A
site 0041B   ; OUT ($BE),A
site 00420   ; OUT ($BE),A
site 00424   ; OUT ($BE),A
site 00429   ; OUT ($BE),A
site 0042D   ; OUT ($BE),A
site 00447   ; OUT ($BE),A
site 0044B   ; OUT ($BE),A
site 0044F   ; OUT ($BE),A
site 00453   ; OUT ($BE),A
site 00465   ; OUT ($BE),A
site 00469   ; OUT ($BE),A
site 0046D   ; OUT ($BE),A
site 00471   ; OUT ($BE),A
site 00485   ; OUT ($BE),A
site 00489   ; OUT ($BE),A
site 0049E   ; OUT ($BE),A
site 00538   ; OUT ($BE),A
site 0053C   ; OUT ($BE),A
site 00541   ; OUT ($BE),A
site 00545   ; OUT ($BE),A
site 0054A   ; OUT ($BE),A
site 0054E   ; OUT ($BE),A
site 00557   ; OUT ($BE),A
site 0055B   ; OUT ($BE),A
site 00560   ; OUT ($BE),A
site 00564   ; OUT ($BE),A
site 00569   ; OUT ($BE),A
site 0056D   ; OUT ($BE),A
site 00587   ; OUT ($BE),A
site 0058B   ; OUT ($BE),A
site 0058F   ; OUT ($BE),A
site 00593   ; OUT ($BE),A
site 005A5   ; OUT ($BE),A
site 005A9   ; OUT ($BE),A
site 005AD   ; OUT ($BE),A
site 005B1   ; OUT ($BE),A
site 005C5   ; OUT ($BE),A
site 005C9   ; OUT ($BE),A
site 005DE   ; OUT ($BE),A
site 0060E   ; OTIR
site 0093E   ; OTIR
site 0094B   ; OTIR
site 00980   ; OTIR
site 0098D   ; OTIR
site 00D02   ; OUT ($BE),A
site 00D06   ; OUT ($BE),A
site 00D0A   ; OUT ($BE),A
site 00D0E   ; OUT ($BE),A
site 00D1C   ; OUT ($BE),A
site 00D20   ; OUT ($BE),A
site 00D24   ; OUT ($BE),A
site 00D28   ; OUT ($BE),A
site 00D2C   ; OUT ($BE),A
site 00D30   ; OUT ($BE),A
site 00D3E   ; OUT ($BE),A
site 00D42   ; OUT ($BE),A
site 00D46   ; OUT ($BE),A
site 00D55   ; OUT ($BE),A
site 00D67   ; OUT ($BE),A
site 00D8A   ; OUT ($BE),A
site 00D8E   ; OUT ($BE),A
site 00D92   ; OUT ($BE),A
site 00D96   ; OUT ($BE),A
site 00DA4   ; OUT ($BE),A
site 00DA8   ; OUT ($BE),A
site 00DAC   ; OUT ($BE),A
site 00DB0   ; OUT ($BE),A
site 00DB4   ; OUT ($BE),A
site 00DB8   ; OUT ($BE),A
site 00DC6   ; OUT ($BE),A
site 00DCA   ; OUT ($BE),A
site 00DCE   ; OUT ($BE),A
site 00DDD   ; OUT ($BE),A
site 00DEF   ; OUT ($BE),A
site 00E17   ; IN A,($BF)
site 00E19   ; IN A,($BF)
site 00E25   ; IN A,($BF)
site 00E34   ; OUT ($BF),A
site 00E38   ; OUT ($BF),A
site 00E3F   ; OUTI
site 00E41   ; OUTI
site 00E43   ; OUTI
site 00E45   ; OUTI
site 00E47   ; OUTI
site 00E49   ; OUTI
site 00E4B   ; OUTI
site 00E4D   ; OUTI
site 00E4F   ; OUTI
site 00E51   ; OUTI
site 00E53   ; OUTI
site 00E55   ; OUTI
site 00E57   ; OUTI
site 00E59   ; OUTI
site 00E5B   ; OUTI
site 00E5D   ; OUTI
site 00E5F   ; OUTI
site 00E61   ; OUTI
site 00E63   ; OUTI
site 00E65   ; OUTI
site 00E67   ; OUTI
site 00E69   ; OUTI
site 00E6B   ; OUTI
site 00E6D   ; OUTI
site 00E6F   ; OUTI
site 00E71   ; OUTI
site 00E73   ; OUTI
site 00E75   ; OUTI
site 00E77   ; OUTI
site 00E79   ; OUTI
site 00E7B   ; OUTI
site 00E7D   ; OUTI
site 00EAE   ; OUTI
site 00EBF   ; OUTI
site 00EC1   ; OUTI
site 00ECA   ; OUT ($DE),A
site 00ECC   ; IN A,($DC)
site 00EDF   ; IN A,($DD)
site 01076   ; OUT ($BE),A
site 0107C   ; OUT ($BE),A
site 0108D   ; OUT ($BE),A
site 011F8   ; OUT ($BF),A
site 011FB   ; OUT ($BF),A
site 011FE   ; OUT ($BE),A
site 013F2   ; OUT ($BE),A
site 013F7   ; OUT ($BE),A
site 013FC   ; OUT ($BE),A
site 01401   ; OUT ($BE),A
site 017FB   ; OUT ($BE),A
site 01821   ; OUT ($BE),A
site 051DB   ; OUT ($BE),A
site 051E9   ; OUT ($BE),A
site 0520A   ; OUT ($BE),A
site 05218   ; OUT ($BE),A
site 05F4D   ; OUT ($BE),A
site 05F54   ; OUT ($BE),A
site 05F5E   ; OUT ($BE),A
site 05F64   ; OUT ($BE),A
site 05F6A   ; OUT ($BE),A
site 05F70   ; OUT ($BE),A
site 05F87   ; OUT ($BE),A
site 05F90   ; OUT ($BE),A
site 05F96   ; OUT ($BE),A
site 05F9C   ; OUT ($BE),A
site 05FA2   ; OUT ($BE),A
site 05FA8   ; OUT ($BE),A
site 05FC7   ; OUT ($BE),A
site 05FD0   ; OUT ($BE),A
site 05FD4   ; OUT ($BE),A
site 05FDD   ; OUT ($BE),A
site 05FEC   ; OUT ($BE),A
site 05FF5   ; OUT ($BE),A
site 05FFD   ; OUT ($BE),A
site 06006   ; OUT ($BE),A
site 0600E   ; OUT ($BE),A
site 06017   ; OUT ($BE),A
site 06025   ; OUT ($BE),A
site 0602E   ; OUT ($BE),A
site 06036   ; OUT ($BE),A
site 0603F   ; OUT ($BE),A
site 06413   ; OUT ($BE),A
site 0641E   ; OUT ($BE),A
site 06426   ; OUT ($BE),A
site 06479   ; OUT ($BE),A
site 06481   ; OUT ($BE),A
site 06495   ; OUT ($BE),A
site 064A0   ; OUT ($BE),A
site 064A8   ; OUT ($BE),A
site 064B2   ; OUT ($BE),A
site 064BA   ; OUT ($BE),A
site 064D4   ; OUT ($BE),A
site 064DC   ; OUT ($BE),A
site 0650A   ; OUT ($BE),A
site 06515   ; OUT ($BE),A
site 0651D   ; OUT ($BE),A
site 06534   ; OUT ($BE),A
site 0655C   ; OUT ($BE),A
site 06567   ; OUT ($BE),A
site 0656F   ; OUT ($BE),A
site 06586   ; OUT ($BE),A
site 067C2   ; OUT ($BE),A
site 067C8   ; OUT ($BE),A
site 067D6   ; OUT ($BE),A
site 067DC   ; OUT ($BE),A
site 067E2   ; OUT ($BE),A
site 067E8   ; OUT ($BE),A
site 067EE   ; OUT ($BE),A
site 067F4   ; OUT ($BE),A
site 06830   ; OUT ($BE),A
site 06836   ; OUT ($BE),A
site 06844   ; OUT ($BE),A
site 0684B   ; OUT ($BE),A
site 06851   ; OUT ($BE),A
site 06884   ; OUT ($BE),A
site 0688C   ; OUT ($BE),A
site 0689E   ; OUT ($BE),A
site 068A6   ; OUT ($BE),A
site 068B0   ; OUT ($BE),A
site 068B8   ; OUT ($BE),A
site 0699F   ; OUT ($BE),A
site 06A0D   ; OUT ($BE),A
site 06A2D   ; OUT ($BE),A
site 06A36   ; OUT ($BE),A
site 06A5C   ; OUT ($BE),A
site 06A63   ; OUT ($BE),A
site 06A94   ; OUT ($BE),A
site 06AA4   ; OUT ($BE),A
site 06C28   ; OUT ($BE),A
site 06C4A   ; OUT ($BE),A
site 06C50   ; OUT ($BE),A
site 06C56   ; OUT ($BE),A
site 06C72   ; OUT ($BE),A
site 06C78   ; OUT ($BE),A
site 06D23   ; OUT ($BE),A
site 06D68   ; OUT ($BE),A
site 06D6F   ; OUT ($BE),A
site 071BD   ; OUT ($BE),A
site 07238   ; OUT ($BE),A
site 0723B   ; OUT ($BE),A
site 0723E   ; OUT ($BE),A
site 07240   ; OUT ($BE),A
site 07261   ; OUT ($BE),A
site 07264   ; OUT ($BE),A
site 07266   ; OUT ($BE),A
site 07268   ; OUT ($BE),A
site 07284   ; OUT ($BE),A
site 07287   ; OUT ($BE),A
site 0728A   ; OUT ($BE),A
site 0728C   ; OUT ($BE),A
site 072AD   ; OUT ($BE),A
site 072B0   ; OUT ($BE),A
site 072B3   ; OUT ($BE),A
site 072B5   ; OUT ($BE),A
site 07352   ; OUT ($BE),A
site 073EE   ; OUT ($BE),A
site 073F2   ; OUT ($BE),A
site 07415   ; OUT ($BE),A
site 07419   ; OUT ($BE),A
site 07435   ; OUT ($BE),A
site 07439   ; OUT ($BE),A
site 0743E   ; OUT ($BE),A
site 07442   ; OUT ($BE),A
site 0744A   ; OUT ($BE),A
site 074DC   ; OUT ($BE),A
site 100C8   ; OUT ($BE),A
site 100F1   ; OUT ($BE),A
site 30020   ; OUT ($BE),A
site 30030   ; OUT ($BE),A
site 30F5C   ; OUT ($BE),A
site 30F6C   ; OUT ($BE),A
site 30FE4   ; OUT ($BE),A
site 30FEA   ; OUT ($BE),A
site 31067   ; OUT ($BE),A
site 3106D   ; OUT ($BE),A
site 3C1BC   ; OUT ($7F),A
site 3C39A   ; OTIR
site 3C4D4   ; OUT ($7F),A
site 3C4DE   ; OUT ($7F),A
site 3C4FB   ; OUT ($7F),A
site 3C5FF   ; OUT ($7F),A
site 3C68D   ; OUT ($7F),A
site 3C713   ; OUT ($7F),A
site 3C723   ; OUT ($7F),A
site 3C783   ; OUT ($7F),A
site 3C7A1   ; OUT ($7F),A
site 3FC4D   ; OUT ($BE),A
site 3FC53   ; OUT ($BE),A
mapst 000F9   ; LD ($FFFC),A
mapst 000FD   ; LD ($FFFD),A
mapst 00102   ; LD ($FFFE),A
mapst 0024D   ; LD ($FFFF),A
mapst 00368   ; LD ($FFFF),A
mapst 00378   ; LD ($FFFF),A
mapst 011E2   ; LD ($FFFF),A
# Byte scan I/O patterns judged code (see the head of the file).
site 0021F   ; OUT ($BE),A
site 00230   ; OUT ($BE),A
site 00271   ; OUT ($3E),A
site 00612   ; OUT ($BE),A
site 00EF0   ; OUT ($BE),A
site 00EF7   ; OUT ($BE),A
site 00F00   ; OUT ($BE),A
site 06F94   ; OUT ($BE),A
site 2F984   ; OUT ($BE),A
# The line interrupt handler's RAM copies ($D500, $D580, from $00D3 and $00E2): with the
# raster table its interrupts are not delivered, but its I/O is patched in the ROM source.
plain 000D9
plain 000DD
plain 000E8
plain 000EC
# Code page 0: the game's VRAM writers send one byte per OUT ($BE),A, each a trap of about 1,200
# cycles, and the loads between screens took twice the reference's frames (a block of 28,672
# bytes from $17FA took 60 frames). Three code caves call the page; the game's loops stay in the
# cart, unreached, with their site lines.
#   $17E9 (block: bank, VRAM address, source, 16-bit count from the table at HL): the cave at
#     $17F2, after the RST $08 that sets the VRAM address, replaces the reads of source and count
#     and the loop at $17FA; entry blk.
#   $1807 (rectangle: VRAM address, source, width, rows, rows 64 bytes apart in VRAM): the cave
#     at $1818, after the reads of the source, replaces the reads of width and rows and the loop
#     at $1820; entry rect.
#   $1082 (RST $20: name table $3800-$3EFF cleared to 0): the cave at $1082 replaces the address
#     write and the loop at $1089; entry clr.
asm 017F2 8   ; INC HL; LD E,(HL); INC HL; LD D,(HL); INC HL; LD C,(HL); INC HL; LD B,(HL)
    rst $00
    db far_io, pg_blk, ent_blk
    ret
endasm
asm 01818 8   ; INC HL; LD B,(HL); INC HL; LD C,(HL); LD A,B; LD ($C020),A
    rst $00
    db far_io, pg_rect, ent_rect
    ret
endasm
asm 01082 7   ; LD DE,$7800; RST $08; LD BC,$0700
    rst $00
    db far_io, pg_clr, ent_clr
    ret
endasm
# The frame handler's own VRAM writes, each a trap of about 1,500 cycles or a run of OUTI traps
# (measured in the race: the HUD digits 17 traps and 37,000 cycles a frame, the two sprite
# attribute table writes 48,000; the palette write at $0E32 is 24,000 and stays: jt_vwrite writes
# VRAM only). Three more code caves call the page:
#   $03F1 (HUD speed digits, three tiles in two rows at $788A and $78CA, tile numbers in
#     $C0E0-$C0E5, attribute 8): the cave at $03F1 replaces the address write and the twelve
#     writes up to $042E and goes on at $042F; entry hud.
#   $0437 (lap timer digits at $784E, $7848 and $7844, and the position digit at $78C4): the cave
#     at $0437 replaces the writes up to $049E and goes on at $04A0; entry lap. The timer's
#     blink path (the jump to $0CE7 when $C33C is not 0) keeps its own writes.
#   $0EA4 (sprite attribute table, 64 Y bytes to $7F00 and 64 X, tile pairs to $7F80, from a
#     3-byte-per-sprite copy at $C200): the cave at $0EA4 replaces both address writes and loops;
#     entry sat.
asm 003F1 7   ; LD DE,$788A; RST $08; LD A,($C0E4)
    rst $00
    db far_io, pg_hud, ent_hud
    jp $042F
endasm
asm 00437 7   ; LD DE,$784E; RST $08; LD A,($C36B)
    rst $00
    db far_io, pg_lap, ent_lap
    jp $04A0
endasm
asm 00EA4 10  ; LD DE,$7F00; RST $08; LD BC,$40BE; LD HL,$C200
    rst $00
    db far_io, pg_sat, ent_sat
    ret
endasm
page 0 blk rect clr hud lap sat
; blk: as the game's code at $17F2-$1806. HL points to the byte before the source address in the
; parameter table; the VRAM address is set. Reads the source (DE) and the count (BC) and writes
; BC bytes from DE to VRAM with jt_vwrite (runs of 256, then the rest). Returns as the game's
; loop does: DE = source + count, BC = 0, A = 0 with Z set, HL at the count's high byte.
blk:    inc hl
        call jt_peek
        ld e,a
        inc hl
        call jt_peek
        ld d,a
        inc hl
        call jt_peek
        ld c,a
        inc hl
        call jt_peek
        ld b,a
        push hl
        push ix
        push iy
        push de                 ; the source
        push bc                 ; the count
        ex de,hl                ; HL = source
        ld de,(vdp_addr)
        ld ix,256
        ld iy,256
        ld a,b
        or c
        jr nz,.n0
        push bc
        ld c,0                  ; count 0: the game's loop writes 65536 bytes, 256 runs
        jr .full
.n0:    ld a,b
        or a
        jr z,.rest
        push bc
        ld c,b                  ; B runs of 256 bytes
.full:  ld b,0
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop bc
        ld a,h                  ; past the full runs
        add a,b
        ld h,a
        ld a,d
        add a,b
        ld d,a
.rest:  ld a,c
        or a
        jr z,.done
        ld b,c                  ; the last C bytes, one run
        ld c,1
        xor a
        call jt_vwrite
.done:  pop bc
        pop hl
        add hl,bc
        ex de,hl                ; DE = source + count
        pop iy
        pop ix
        pop hl
        ld bc,0
        xor a
        ret
; rect: as the game's code at $1818-$183F. DE = source, HL points to the source's high byte in
; the parameter table, ($C022) = VRAM address of row 0. Reads the width (B) and rows (C), keeps
; the width in $C020 and writes the rows with one jt_vwrite call (C runs of B bytes, B bytes
; apart in the source and 64 in VRAM). Returns as the game's loop does: B = C = 0, Z set,
; DE = source + width * rows, ($C022) = VRAM address of the last row, A = the last byte,
; HL = $0040, or the table pointer for a single row.
rect:   inc hl
        call jt_peek
        ld b,a
        inc hl
        call jt_peek
        ld c,a
        ld (rows),a
        ld a,b
        ld ($C020),a
        push ix
        push iy
        push hl                 ; the table pointer
        ld ix,0
        ld ixl,b
        or a
        jr nz,.w
        inc ixh                 ; width 0: 256
.w:     ld iy,64
        ex de,hl                ; HL = source
        ld de,($C022)
        xor a
        call jt_vwrite
        push ix
        pop bc                  ; BC = width
        ld a,(rows)             ; rows, 0 = 256
.r:     add hl,bc               ; the next row's source
        dec a
        jr z,.e
        ex de,hl
        push bc
        ld bc,64
        add hl,bc
        pop bc
        ex de,hl
        jr .r
.e:     ld ($C022),de           ; VRAM of the last row
        ex de,hl                ; DE = source + width * rows
        ld h,d
        ld l,e
        dec hl
        call jt_peek            ; A = the last byte written
        pop hl                  ; the table pointer
        ld c,a
        ld a,(rows)
        dec a
        ld a,c
        jr z,.one
        ld hl,$0040
.one:   pop iy
        pop ix
        ld bc,0
        cp a                    ; Z, as after the game's DEC C
        ret
rows:   db 0
; clr: as the game's code at $1082-$1094: name table $3800-$3EFF set to 0, 7 runs of 256 zero
; bytes from this page. Returns DE = $7800, BC = 0, A = 0 with Z set, HL kept.
clr:    push hl
        push ix
        push iy
        ld hl,zeros
        ld de,$7800
        ld bc,$0007
        ld ix,0
        ld iy,256
        ld a,1                  ; the source as mapped now: this page
        call jt_vwrite
        pop iy
        pop ix
        pop hl
        ld bc,0
        xor a
        ret
zeros:  ds 256,0
; hud: as the game's code at $03F1-$042E. The tile numbers in $C0E4, $C0E2, $C0E0 go to $788A, $788C
; and $788E, and those in $C0E5, $C0E3, $C0E1 to $78CA, $78CC and $78CE, each followed by the
; attribute 8: two runs of 6 bytes, 64 apart in VRAM. The game goes on at $042F.
hud:    push bc
        push ix
        push iy
        ld a,($C0E4)
        ld (hbuf),a
        ld a,($C0E2)
        ld (hbuf+2),a
        ld a,($C0E0)
        ld (hbuf+4),a
        ld a,($C0E5)
        ld (hbuf+6),a
        ld a,($C0E3)
        ld (hbuf+8),a
        ld a,($C0E1)
        ld (hbuf+10),a
        ld hl,hbuf
        ld de,$788A
        ld bc,$0602             ; runs of 6 bytes, 2 runs
        ld ix,6
        ld iy,$0040
        ld a,1                  ; the source as mapped now: this page
        call jt_vwrite
        pop iy
        pop ix
        pop bc
        ret
hbuf:   db 0,8,0,8,0,8,0,8,0,8,0,8
; lap: as the game's code at $0437-$049E. The timer's tiles come from the word tables at $0BE1 (the
; ticks, $C36B), $0C1F (the seconds, $C36C) and $0C20 (the tenths, $C36D low nibble), each index
; doubled in 8 bits as the game does. Seconds (4 bytes at $7848) and ticks (4 bytes at $784E) are
; one call of 2 runs 6 apart; the tenths (2 bytes at $7844) and the position digit ($C365, less 1
; when $C301 is 3, plus $31, 1 byte at $78C4) are one call each. The game goes on at $04A0.
lap:    push ix
        push iy
        ld a,($C36B)
        add a,a
        ld l,a
        ld h,0
        ld de,$0BE1
        add hl,de
        ld a,(hl)
        ld (lbuf+4),a
        inc hl
        ld a,(hl)
        ld (lbuf+6),a
        ld a,($C36C)
        add a,a
        ld l,a
        ld h,0
        ld de,$0C1F
        add hl,de
        ld a,(hl)
        ld (lbuf),a
        inc hl
        ld a,(hl)
        ld (lbuf+2),a
        ld a,($C36D)
        and $0F
        add a,a
        ld l,a
        ld h,0
        ld de,$0C20
        add hl,de
        ld a,(hl)
        ld (lbuf+8),a
        ld a,($C365)
        ld c,a
        ld a,($C301)
        cp 3
        jr nz,.pos
        dec c
.pos:   ld a,c
        add a,$31
        ld (lbuf+10),a
        ld hl,lbuf
        ld de,$7848
        ld bc,$0402             ; runs of 4 bytes, 2 runs
        ld ix,4
        ld iy,6
        ld a,1
        call jt_vwrite
        ld hl,lbuf+8
        ld de,$7844
        ld bc,$0201
        ld ix,2
        ld iy,2
        ld a,1
        call jt_vwrite
        ld hl,lbuf+10
        ld de,$78C4
        ld bc,$0101
        ld ix,1
        ld iy,1
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        ret
lbuf:   db 0,9,0,9,0,9,0,9,0,9,0
; sat: as the game's code at $0EA4-$0EC6. 64 sprites of 3 bytes at $C200 (Y, X, tile): the Y bytes
; go to $7F00 and the X, tile pairs to $7F80. A call of jt_vwrite costs about 800 cycles a run, so
; the page gathers the Y bytes (64) and then the pairs (128) into sbuf and writes each as one run.
; Returns as the game's loop does: HL = $C2C1, DE = $7F80, BC = $00BE, Z set.
sat:    push ix
        push iy
        ld hl,$C200
        ld de,sbuf
        ld b,64
.gy:    ld a,(hl)
        ld (de),a
        inc de
        inc hl
        inc hl
        inc hl
        djnz .gy
        ld hl,$C201
        ld bc,128
.gx:    ldi
        ldi
        inc hl
        jp pe,.gx
        ld hl,sbuf
        ld de,$7F00
        ld bc,$4001             ; one run of 64 bytes
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        ld hl,sbuf+64
        ld de,$7F80
        ld bc,$8001             ; one run of 128 bytes
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        pop iy
        pop ix
        ld hl,$C2C1
        ld de,$7F80
        ld bc,$00BE
        ld a,$7F
        cp a
        ret
sbuf:   ds 192,0
endpage
# Race speed. The race loop's step ($191D-$1BEF) waits for the frame flag $C037 at $191D. On the
# Master System the step's work (about 70,800 T-states in the one-player race, 63,400 in the
# attract race) and the interrupt handlers (35,100 T-states a frame: the frame handler and 99 line
# interrupts) leave the step longer than a frame, so the wait never waits: on a PAL Master System
# (71,364 T-states a frame) a step takes its work / 36,269 frames, 1.95 in the race. On the Next
# a step fits in one frame. The cave at $191D far-calls page 1 `pace`, which keeps the Master
# System's time: it times each step's run on the Next, turns it into the step's Master System
# time, and releases the next step at the frame event where that time has passed.
asm 0191D 6   ; CALL $016F; LD HL,$C056
    rst $00
    db far_io, pg_pace, ent_pace
endasm
page 1 pace
; pace: the race loop's frame wait, CALL $016F at $191D, and the LD HL,$C056 after it.
;
; The step's run. pace releases a step after the frame's once-a-frame work (the ULA interrupt at
; line 248), so the step runs to its next call of pace with no interrupt. CTC channel 0 times it:
; started at the release as a timer of 16 cycles a count, read and stopped here. The beam's line
; at both ends gives the whole wraps of the 8-bit count (4,096 cycles each). A run with a frame
; event in it ($C037 not 0 here) or of 256 lines or more is not a step that ran alone: the step
; takes the time of the last one that did.
;
; The Master System time of a step, from the reference (sg1000m3) at the step's own instructions:
; the run less OVH cycles (the far call and this page's code) is 1.4666 Next cycles a T-state
; (attract race, paired step by step: spread 0.6%). A PAL Master System frame leaves 71,364 -
; 35,095 = 36,269 T-states to the step, so a count of 16 cycles is 16 / 1.4666 / 36,269 * 256 =
; 0.077005 in units of 1/256 frame (K = 5047 / 65536). The one-player race also runs the delay
; loop at $1A2F, 26,005 T-states in 31,008 cycles, a lower ratio than the rest: DLY is the time
; the run misses, 30 (fitted on the race paired step by step with the reference; the loop alone
; gives 34).
;
; p_debt is the Master System time still owed before the next step starts, in 1/256 frame. Each
; return here adds the step's time; each frame event takes 256 off. A step is released at the
; first frame event where less than a frame is owed; owed time below 0 is dropped, as a Master
; System never runs a step early to catch up. After a gap (fw_frames 16 or more past the last
; release: the race starts, or comes back from the pre-race loop) nothing is owed.
;
; Returns as the game's code does: $C037 = 0, $C042/$C045 (new presses) and $C041/$C044 from the
; game's routine at $0179, A and B as it leaves them, HL = $C056. Keeps C, DE, IX, IY. Interrupts
; on, as at the call. Runs on its own stack with interrupts off, and waits on the game's stack
; with interrupts on and no stack use.
        OPT --zxnext            ; MUL D,E
OVH     equ 171                 ; counts of 16 cycles
DLY     equ 30
pace:   di
        ld (p_sp),sp
        ld sp,p_stk
        push bc
        push de
        ld bc,$183B             ; CTC channel 0: the count, then stop it
        in e,(c)
        ld a,$03
        out (c),a
        call rdline             ; HL = the beam's line
        ld a,(p_ok)
        or a
        jp z,.gap
        push hl
        ld hl,(fw_frames)
        ld bc,(p_fw)
        or a
        sbc hl,bc               ; frames since the release
        ld a,h
        or a
        jp nz,.gap0
        ld a,l
        cp 16
        jp nc,.gap0
        pop hl
        ld a,($C037)
        or a
        jp nz,.inv              ; a frame event in the step's run
        ld bc,(p_l0)
        or a
        sbc hl,bc
        jr nc,.pos
        ld bc,311
        add hl,bc
.pos:   ld a,h
        or a
        jp nz,.inv              ; 256 lines or more
        ld a,e
        neg
        ld e,a                  ; E = counts since the start, mod 256
        ld d,l
        ld l,e
        ld e,114                ; counts in a line
        mul d,e                 ; DE = lines * 114
        ex de,hl                ; HL = lines * 114, DE = counts mod 256
        or a
        sbc hl,de
        ld bc,128
        add hl,bc               ; H = whole wraps
        ld l,e                  ; HL = counts since the start
        ld bc,OVH
        or a
        sbc hl,bc
        jp c,.inv
        ld b,h                  ; D = HL * 5047 / 65536 (5047 = 19 * 256 + 183)
        ld c,l
        ld d,c
        ld e,183
        mul d,e
        ld a,d                  ; lo * 183 / 256
        ld d,b
        ld e,183
        mul d,e
        ex de,hl
        ld d,c
        ld e,19
        mul d,e
        add hl,de
        ld e,a
        ld d,0
        add hl,de               ; hi * 183 + lo * 19 + lo * 183 / 256
        ld e,h                  ; / 256
        ld d,b
        ld b,e
        ld e,19
        mul d,e                 ; hi * 19
        ld l,b
        ld h,0
        add hl,de               ; HL = the step's time in 1/256 frame
        ld a,($C06C)
        or a
        jr z,.one
        ld de,DLY
        add hl,de
.one:   ld a,h                  ; a whole step (half a frame or more) is the fallback
        or a
        jr nz,.keep
        ld a,l
        cp 128
        jr c,.add
.keep:  ld (p_d),hl
        jr .add
.inv:   ld hl,(p_d)
.add:   ld de,(p_debt)
        add hl,de
        ld (p_debt),hl
        jr .wt
.gap0:  pop hl
.gap:   ld hl,0
        ld (p_debt),hl
.wt:    pop de
        pop bc
        ld (p_c),bc
        ld sp,(p_sp)
        ei
; Wait for a frame event: $C037 not 0 (the frame handler takes 1 off it). No stack use.
.fw:    ld hl,$C037
.f1:    ld a,(hl)
        or a
        jr z,.f1
        di
        ld a,(hl)
        ld (hl),0
        neg                     ; frame events since the last look
        ld l,a
        ld a,(p_debt+1)
        sub l
        ld (p_debt+1),a
        ei
        jr z,.go                ; less than a frame owed
        jp p,.fw                ; a frame or more owed
        ld hl,0                 ; owed time below 0 is dropped
        ld (p_debt),hl
; Release after the once-a-frame work: not on lines 192-250, where the frame handler has run
; and the ULA interrupt at 248 has not yet.
.go:    di
        ld sp,p_stk
        call rdline
        ld a,h
        or a
        jr nz,.rel              ; line 256 and on
        ld a,l
        cp 192
        jr c,.rel
        cp 251
        jr nc,.rel
        ld sp,(p_sp)
        ei
        jr .go
.rel:   ld (p_l0),hl
        ld hl,(fw_frames)
        ld (p_fw),hl
        ld a,1
        ld (p_ok),a
        ld bc,$183B             ; CTC channel 0: timer, 16 cycles a count, from 256
        ld a,$07
        out (c),a
        xor a
        out (c),a
        call $0179              ; the game's new presses from $C040/$C043
        ld hl,p_c
        ld c,(hl)
        ld sp,(p_sp)
        ld hl,$C056
        ei
        ret
; rdline: HL = the beam's Next line (0-310). Interrupts off. Uses A, BC.
rdline: ld bc,$243B
.r:     ld a,$1E
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
        jr nz,.r
        ld a,h
        and 1
        ld h,a
        ret
p_sp:   dw 0
p_c:    dw 0
p_l0:   dw 0
p_fw:   dw 0
p_ok:   db 0
p_debt: dw 0
p_d:    dw 500                  ; a step of the one-player race (1.95 frames)
        ds 32
p_stk:
endpage
