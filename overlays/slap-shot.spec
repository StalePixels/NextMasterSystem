# Slap Shot (USA, Europe, Brazil) (En), CRC32 702C3E98, 256K, Sega mapper.
# Drafted by tools/mkspec.py from the sitescan output with the 60 s sweep log, then decided by hand.
#
# Decisions:
# - No RST vector holds $FF filler: $0000-$0002 (DI; IM 1) becomes the io vector, and the game
#   starts at $0003. The game has no RST $00 of its own.
# - Two places jump to $0000, which on the Next is the io vector: $1566 (the end of the state
#   machine of $149D) and $73C4 (the reset button: $0294 reads port $DD bit 4, clears RAM and
#   goes to $73A9). Each goes to the cave at $0018 (zero bytes after the RST $10 vector, which
#   no code runs), which does what $0000 does: DI, then on to $0003.
# - Unreached code patched as code: the routines of the jump block at $0080 that no run
#   reached ($0F09 through $0094, $102E through $00C8, $1381 through $00F8), the FM sound
#   detection $04A7 (nothing calls it), $1150 (the twin of $1100, nothing names it) and the
#   bank 4 column writer $942F (called from $9423).
# - $09F3 times one frame with a counted loop to tell a 60 Hz machine from a 50 Hz one
#   ($C01E: 1 for 60 Hz). On the Next the loop ends before the frame does, so $C01E is 0 at
#   both rates. $C01E only picks a short wait in the frame handler ($7412), so play is the same.
# - priority: the score table after a goal is drawn with the priority bit, so it covers the
#   players, as on a Master System.
# - Bank 7 is the sound driver, with the FM sound chip's writes at $84E0 and $84E6.
name Slap Shot
cart 702C3E98
hz any		; No-Intro regions USA, Europe, Brazil
priority	; the score table after a goal (tiles $11: priority bit) covers the players
vector 00 io
start 0003
label cv_reset 00018
asm 00018 4    ; zero bytes after the RST $10 vector, which no code runs: the reset of $0000
    di
    jp $0003
endasm
asm 01566 3    ; JP $0000: the end of the state machine of $149D
    jp cv_reset
endasm
asm 073C4 3    ; JP $0000: the reset button ($0294, $73A9)
    jp cv_reset
endasm
asm 00FE2 29   ; the rectangle writer (JP at $00B8): C rows of B cells at VRAM HL, each cell
    rst $00     ; the byte from DE and A, with OUTI and OUT (C),A; through jt_vwrite (page 0)
    db far_io, pg_rect, ent_rect
    ret
endasm
asm 01219 10   ; NOP; NOP; OUTI; JR NZ,$1219; DEC A; JR NZ,$1219; RET: the loop of the VRAM
    rst $00     ; copy $120C, A blocks of B bytes from HL; one OTIR a block
    db $B3
    dec a
    jr nz,$1219
    ret
endasm
site 00047   ; IN A,($BF)
site 0019A   ; OUT ($BF),A
site 0019F   ; OUT ($BF),A
site 001AF   ; OUT ($BF),A
site 001B4   ; OUT ($BF),A
site 001C7   ; OUT ($BF),A
site 001CC   ; OUT ($BF),A
site 001D2   ; OUTD
site 001DD   ; OUT ($BF),A
site 001E2   ; OUT ($BF),A
site 001E8   ; OUTI
site 001EA   ; OUTD
site 001F1   ; OUTI
site 001F3   ; OUTI
site 001F5   ; OUTI
site 001F7   ; OUTI
site 001F9   ; OUTI
site 001FB   ; OUTI
site 001FD   ; OUTI
site 001FF   ; OUTI
site 00201   ; OUTI
site 00203   ; OUTI
site 00205   ; OUTI
site 00207   ; OUTI
site 00209   ; OUTI
site 0020B   ; OUTI
site 0020D   ; OUTI
site 0020F   ; OUTI
site 00211   ; OUTI
site 00213   ; OUTI
site 00215   ; OUTI
site 00217   ; OUTI
site 00219   ; OUTI
site 0021B   ; OUTI
site 0021D   ; OUTI
site 0021F   ; OUTI
site 00221   ; OUTI
site 00223   ; OUTI
site 00225   ; OUTI
site 00227   ; OUTI
site 00229   ; OUTI
site 0022B   ; OUTI
site 0022D   ; OUTI
site 0022F   ; OUTI
site 00231   ; OUTI
site 00233   ; OUTI
site 00235   ; OUTI
site 00237   ; OUTI
site 00239   ; OUTI
site 0023B   ; OUTI
site 0023D   ; OUTI
site 0023F   ; OUTI
site 00241   ; OUTI
site 00243   ; OUTI
site 00245   ; OUTI
site 00247   ; OUTI
site 00249   ; OUTI
site 0024B   ; OUTI
site 0024D   ; OUTI
site 0024F   ; OUTI
site 00251   ; OUTI
site 00253   ; OUTI
site 00255   ; OUTI
site 00257   ; OUTI
site 00259   ; OUTI
site 0025B   ; OUTI
site 0025D   ; OUTI
site 0025F   ; OUTI
site 00261   ; OUTI
site 00263   ; OUTI
site 00265   ; OUTI
site 00267   ; OUTI
site 00269   ; OUTI
site 0026B   ; OUTI
site 0026D   ; OUTI
site 0026F   ; OUTI
site 00279   ; OUT ($BF),A
site 0027E   ; OUT ($BF),A
otir 00289   ; OUTI
site 00294   ; IN A,($DD)
site 002B9   ; OUT ($BF),A
site 002BD   ; OUT ($BF),A
site 002C2   ; OUT ($BF),A
site 002C6   ; OUT ($BF),A
site 002C9   ; IN A,($DC)
site 002DE   ; IN A,($DD)
site 00300   ; OUT ($BF),A
site 00305   ; OUT ($BF),A
site 003F0   ; OUT ($BF),A
site 003F6   ; OUT ($BF),A
site 003FD   ; OTIR
site 00417   ; OUT ($BF),A
site 0041A   ; OUT ($BF),A
site 00424   ; OUTI
site 00426   ; OUTI
site 00474   ; IN A,($BF)
otir 0047D   ; OUTI
site 00482   ; OUT ($BE),A
site 00494   ; OUT ($3E),A
site 00499   ; OUT ($F2),A
site 004A1   ; OUT ($3E),A
site 009FA   ; IN A,($BF)
site 009FC   ; IN A,($BF)
site 00A08   ; IN A,($BF)
site 00A28   ; OUT ($3F),A
site 00A2A   ; IN A,($DD)
site 00A34   ; OUT ($3F),A
site 00A36   ; IN A,($DD)
site 00A3F   ; OUT ($3F),A
site 00A46   ; OUT ($3F),A
site 00FAE   ; OUT ($BF),A
site 00FB3   ; OUT ($BF),A
site 00FBC   ; OUT ($BF),A
site 00FC3   ; OUT ($BF),A
site 00FCE   ; OUT ($BE),A
site 00FD3   ; OUT ($BE),A
site 013F0   ; OUT ($BF),A
site 013F7   ; OUT ($BF),A
site 013FE   ; OUT ($BE),A
site 01404   ; OUT ($BE),A
site 01477   ; OUT ($BF),A
site 0147C   ; OUT ($BF),A
site 01482   ; IN A,($BE)
site 01489   ; IN A,($BE)
site 01B5B   ; IN A,($DC)
site 03E80   ; OUT ($BF),A
site 03E85   ; OUT ($BF),A
site 03EAA   ; OUT ($BE),A
site 03EB0   ; OUT ($BE),A
site 073B3   ; OUT ($BF),A
site 073B7   ; OUT ($BF),A
site 073BB   ; OUT ($BE),A
site 0F7DE   ; OUT ($BF),A
site 0F7E3   ; OUT ($BF),A
site 0F7EA   ; OUT ($BE),A
site 1C0FA   ; OUT ($7F),A
site 1C12B   ; OTIR
site 1C134   ; OTIR
site 1C171   ; OUT ($7F),A
site 1C175   ; OUT ($7F),A
site 1C1CB   ; OUT ($7F),A
site 1C1CF   ; OUT ($7F),A
site 1C1F7   ; OUT ($7F),A
site 1C1FB   ; OUT ($7F),A
site 1C1FF   ; OUT ($7F),A
site 1C202   ; OUT ($7F),A
site 1C3CD   ; OUT ($7F),A
site 1C3FA   ; OUT ($7F),A
site 1C421   ; OUT ($7F),A
site 1C426   ; OUT ($7F),A
site 1C4C2   ; OUTI
site 1C4C4   ; OUTI
site 1C4C6   ; OUTI
site 1C4C8   ; OUTI
site 1C4CA   ; OUTI
site 1C4CC   ; OUTI
site 1C4CE   ; OUTI
site 1C4D0   ; OUTI
site 1C4D2   ; OUTI
site 1C4D4   ; OUTI
site 1C4D6   ; OUTI
site 1C4E0   ; OUT (C),D
site 1C4E6   ; OUT ($F1),A
site 1C525   ; OUT ($7F),A
site 1C57B   ; OUT ($7F),A
site 1C5BA   ; OUT ($7F),A
site 1C60D   ; OUT ($7F),A
site 1C62D   ; OUT ($7F),A
site 1C679   ; OUT ($7F),A
site 1C683   ; OUT ($7F),A
site 1C6CB   ; OUT ($7F),A
mapst 00322   ; LD ($FFFF),A
mapst 00329   ; LD ($FFFF),A
mapst 00333   ; LD ($FFFF),A
mapst 0033A   ; LD ($FFFF),A
mapldk 00434   # LD HL,$FFFC; LD (HL),$00
maphl 0043A   # LD (HL),$00, HL = $FFFD
maphl 0043D   # LD (HL),$01, HL = $FFFE
maphl 00440   # LD (HL),$02, HL = $FFFF
mapst 0048C   ; LD ($FFFF),A
mapst 00A17   ; LD ($FFFF),A
mapst 00D8D   ; LD ($FFFF),A
mapst 00D94   ; LD ($FFFF),A
mapst 00EB3   ; LD ($FFFF),A
mapst 00EBA   ; LD ($FFFF),A
mapst 00EE8   ; LD ($FFFF),A
mapst 00EEF   ; LD ($FFFF),A
mapst 00EFE   ; LD ($FFFF),A
mapst 00F05   ; LD ($FFFF),A
mapst 010F2   ; LD ($FFFF),A
mapst 010F9   ; LD ($FFFF),A
mapst 01129   ; LD ($FFFF),A
mapst 01149   ; LD ($FFFF),A
mapst 014BD   ; LD ($FFFF),A
mapst 014C4   ; LD ($FFFF),A
mapst 014EC   ; LD ($FFFF),A
mapst 014F6   ; LD ($FFFF),A
mapst 01506   ; LD ($FFFF),A
mapst 01510   ; LD ($FFFF),A
mapst 01519   ; LD ($FFFF),A
mapst 01520   ; LD ($FFFF),A
mapst 0152C   ; LD ($FFFF),A
mapst 01533   ; LD ($FFFF),A
mapst 0153F   ; LD ($FFFF),A
mapst 01549   ; LD ($FFFF),A
mapst 01552   ; LD ($FFFF),A
mapst 01563   ; LD ($FFFF),A
mapst 04557   ; LD ($FFFF),A
mapst 0455E   ; LD ($FFFF),A
mapst 0499D   ; LD ($FFFF),A
mapst 049A4   ; LD ($FFFF),A
mapst 049C2   ; LD ($FFFF),A
mapst 049C9   ; LD ($FFFF),A
mapst 049E2   ; LD ($FFFF),A
mapst 049E9   ; LD ($FFFF),A
mapst 049FA   ; LD ($FFFF),A
mapst 04A01   ; LD ($FFFF),A
mapst 04AE0   ; LD ($FFFF),A
mapst 04AE7   ; LD ($FFFF),A
mapst 04C0A   ; LD ($FFFF),A
mapst 04C11   ; LD ($FFFF),A
mapst 0545E   ; LD ($FFFF),A
mapst 05465   ; LD ($FFFF),A
mapst 073AE   ; LD ($FFFF),A
mapst 00ED2   # LD ($FFFF),A; after LD A,$87; 32 bytes of valid code before it
mapst 00ED9   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 011A1   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it

# Unreached code, patched as code:
site 004AD   # OUT ($F2),A; in the FM sound detection $04A7, which nothing calls
site 004B0   # IN A,($F2); in $04A7
site 00F13   # OUT ($BE),A; in the VRAM clear $0F09 (JP at $0094)
site 01049   # OUT ($BE),A; in the number writer $102E (JP at $00C8)
site 01050   # OUT ($BE),A; in $102E
mapst 01181   # LD ($FFFF),A; in $1150, the twin of $1100, which nothing names
site 0138D   # OUT ($BE),A; in the tile row writer $1381 (JP at $00F8)
site 01392   # OUT ($BE),A; in $1381
site 11439   # OUTI; in the column writer $942F (bank 4), called from $9423
site 1143D   # OUT (C),A; in $942F

; Page 0: rect replaces the rectangle writer at $0FE2-$0FFE. At $0FE2 HL is the VRAM address of
; the first row, DE the source, B the cells in a row (1-128), C the rows and A the second byte
; of every cell. For each row it builds the B cells (the byte from DE, as the game sees it,
; then A) and writes them with one jt_vwrite call; the next row is $40 bytes on. Returns as
; the game's loop leaves it: HL and DE past the last row, B kept, C = 0, A kept, Z set,
; interrupts on (the game's $0FBA turns them on for every row).
page 0 rect
rect:
    di
    ld (.sp),sp
    ld sp,.stk
    push ix
    push iy
    ld (.attr),a
    ld a,b
    ld (.cells),a
    ld ix,0
    ld iy,$40
.row:
    push bc
    push hl
    ex de,hl        ; HL = source
    ld de,.buf
.cell:
    ld a,h
    and $E0
    cp $20
    jr z,.peek
    ld a,(hl)
    jr .put
.peek:
    call jt_peek    ; $2000-$3FFF holds this page: read the game's byte
.put:
    ld (de),a
    inc de
    ld a,(.attr)
    ld (de),a
    inc de
    inc hl
    djnz .cell
    pop de          ; DE = the row's VRAM address
    push hl         ; the source past the row
    ld a,(.cells)
    add a,a
    ld b,a          ; 2 bytes a cell (128 cells: 0, which is 256)
    ld c,1
    ld hl,.buf
    ld a,1          ; the buffer is in this page
    call jt_vwrite
    ex de,hl
    ld bc,$40
    add hl,bc       ; HL = the next row's VRAM address
    pop de          ; DE = the source
    pop bc
    dec c
    jr nz,.row
    pop iy
    pop ix
    ld a,(.attr)
    ld sp,(.sp)
    ei
    ret
.sp:    dw 0
.attr:  db 0
.cells: db 0
.buf:   ds 256
        ds 32
.stk:
endpage
