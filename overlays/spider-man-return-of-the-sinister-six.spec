# Spider-Man - Return of the Sinister Six (Europe, Brazil) (En), CRC32 EBE45388, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input).
# Decisions:
# - $0020 is the io vector: RST $20 is free and its bytes are $FF filler. The cart
#   starts with DI; IM 1; LD SP,$DFF8, and the IM 1 at $0001 becomes IM 2.
# - The game does its frame work from a line interrupt: register 0 is $36 (line
#   interrupts on) and register 10 is $C0. On the Master System the line counter of 192
#   runs out at line 192, once a frame, and the frame interrupt comes after it. The
#   handler at $0038 reads the status and calls the frame routine $04D7 only when bit 7
#   (the frame flag) is clear, that is, for the line interrupt. The runtime schedules no
#   line event for a counter of 192 or more, so only the frame event came, the frame
#   routine never ran and the game waited for ever at $5A92. The CALL Z at $003D becomes
#   a CALL: the frame interrupt (register 1 is $A0 or $E0, frame interrupt always on)
#   runs the frame routine once a frame, one line later than the line interrupt does.
# - The sprite tile uploaders $0C2F (32 bytes from the source, an OUTI loop with
#   JP/NOP/DJNZ between the OUTIs) and $0C66 (32 bytes, each one mapped through the
#   table at $C700) are far calls into page 0. Through the I/O traps one tile cost about
#   19,600 cycles, and play frames that upload many tiles ran over a frame. The page
#   builds the same 32 bytes and writes them with one jt_vwrite call. The sites inside
#   the two routines stay in the spec; nothing runs them now.
name Spider-Man - Return of the Sinister Six
cart EBE45388
hz 50		; No-Intro regions Europe, Brazil
vector 20 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 0003D 3   ; CALL Z,$04D7 -> CALL $04D7
    call $04D7
endasm
asm 00C2F 5   ; sprite tile copy: PUSH DE; PUSH HL; LD E,A; LD D,$00
    rst $20
    db far_io, pg_tilecopy, ent_tilecopy
    ret
endasm
asm 00C66 5   ; sprite tile copy through $C700: PUSH DE; PUSH HL; LD E,A; LD D,$00
    rst $20
    db far_io, pg_tilemap, ent_tilemap
    ret
endasm
site 00039   ; IN A,($BF)
site 00C3B   ; OUT ($BF),A
site 00C43   ; OUT ($BF),A
site 00C59   ; OUTI
site 00C61   ; OUTI
site 00C72   ; OUT ($BF),A
site 00C7A   ; OUT ($BF),A
site 00C92   ; OUT ($BE),A
site 00C97   ; OUT ($BE),A
site 00C9C   ; OUT ($BE),A
site 00CA1   ; OUT ($BE),A
site 00CA6   ; OUT ($BE),A
site 00CAB   ; OUT ($BE),A
site 00CB0   ; OUT ($BE),A
site 00CB5   ; OUT ($BE),A
site 00CBA   ; OUT ($BE),A
site 00CBF   ; OUT ($BE),A
site 00CC4   ; OUT ($BE),A
site 00CC9   ; OUT ($BE),A
site 00CCE   ; OUT ($BE),A
site 00CD3   ; OUT ($BE),A
site 00CD8   ; OUT ($BE),A
site 00CDD   ; OUT ($BE),A
site 00CE2   ; OUT ($BE),A
site 00CE7   ; OUT ($BE),A
site 00CEC   ; OUT ($BE),A
site 00CF1   ; OUT ($BE),A
site 00CF6   ; OUT ($BE),A
site 00CFB   ; OUT ($BE),A
site 00D00   ; OUT ($BE),A
site 00D05   ; OUT ($BE),A
site 00D0A   ; OUT ($BE),A
site 00D0F   ; OUT ($BE),A
site 00D14   ; OUT ($BE),A
site 00D19   ; OUT ($BE),A
site 00D1E   ; OUT ($BE),A
site 00D23   ; OUT ($BE),A
site 00D28   ; OUT ($BE),A
site 00D2D   ; OUT ($BE),A
site 056F2   ; OUT ($BF),A
site 056F6   ; OUT ($BF),A
site 056FC   ; OUT ($BE),A
site 05721   ; OUT ($BF),A
site 05728   ; OUT ($BF),A
site 0572C   ; IN A,($DD)
site 05739   ; IN A,($DC)
site 05778   ; OUT ($BF),A
site 0577F   ; OUT ($BF),A
site 057BA   ; OUT ($BE),A
site 05A85   ; OUT ($BF),A
site 05A8A   ; OUT ($BF),A
site 05B62   ; OUT ($BE),A
site 05F41   ; OUT ($BE),A
site 05F45   ; OUT ($BE),A
site 05F5F   ; OUT ($BE),A
site 05F63   ; OUT ($BE),A
site 05FB2   ; OUT ($BF),A
site 05FBA   ; OUT ($BF),A
site 05FBE   ; OUT ($BE),A
site 05FC4   ; OUT ($BE),A
site 05FFE   ; OUT ($BE),A
site 06002   ; OUT ($BE),A
site 0601E   ; OUT ($BE),A
site 06023   ; OUT ($BE),A
site 060BB   ; OUT ($BF),A
site 060BF   ; OUT ($BF),A
site 060D2   ; OUT ($BE),A
site 060D8   ; OUT ($BE),A
site 060DF   ; OUT ($BF),A
site 060E3   ; OUT ($BF),A
site 060F4   ; OUT ($BE),A
site 06101   ; OUT ($BE),A
site 06109   ; OUT ($BF),A
site 0610E   ; OUT ($BF),A
site 06113   ; OUT ($BE),A
site 1C100   ; OTIR
site 1C13E   ; OUTI
site 1C140   ; OUTI
site 1C142   ; OUTI
site 1C14D   ; OUTI
site 1C14F   ; OUTI
site 1C151   ; OUTI
site 1C15C   ; OUTI
site 1C15E   ; OUTI
site 1C160   ; OUTI
site 1C16B   ; OUTI
site 1C72E   ; OUT ($7F),A
site 1C88F   ; OUT ($7F),A
site 1C898   ; OUT ($7F),A
site 1C8E5   ; OUT ($7F),A
site 1C8EE   ; OUT ($7F),A
site 1C93B   ; OUT ($7F),A
site 1C944   ; OUT ($7F),A
site 1C98D   ; OUT ($7F),A
site 1C9B5   ; OUT ($7F),A
site 1C9E7   ; OUT ($7F),A
site 1CA22   ; OUT ($7F),A
site 1CA2A   ; OUT ($7F),A
site 1CA39   ; OUT ($7F),A
site 1CA42   ; OUT ($7F),A
site 1CA6E   ; OUT ($7F),A
site 1CA77   ; OUT ($7F),A
site 1CA99   ; OUT ($7F),A
site 1CACB   ; OUT ($7F),A
site 1CB06   ; OUT ($7F),A
site 1CB0E   ; OUT ($7F),A
site 1CB1D   ; OUT ($7F),A
site 1CB26   ; OUT ($7F),A
site 1CB52   ; OUT ($7F),A
site 1CB5B   ; OUT ($7F),A
site 1CB7D   ; OUT ($7F),A
site 1CBAF   ; OUT ($7F),A
site 1CBEA   ; OUT ($7F),A
site 1CBF2   ; OUT ($7F),A
site 1CC01   ; OUT ($7F),A
site 1CC0A   ; OUT ($7F),A
site 1CC36   ; OUT ($7F),A
site 1CC3F   ; OUT ($7F),A
site 1CC61   ; OUT ($7F),A
site 1CC93   ; OUT ($7F),A
site 1CCBF   ; OUT ($7F),A
mapst 00007   ; LD ($FFFC),A
mapst 0000A   ; LD ($FFFD),A
mapst 0000F   ; LD ($FFFE),A
mapst 00014   ; LD ($FFFF),A
mapst 004E0   ; LD ($FFFF),A
mapst 004F4   ; LD ($FFFF),A
mapst 00506   ; LD ($FFFF),A
mapst 0052F   ; LD ($FFFF),A
mapst 00538   ; LD ($FFFF),A
mapst 00664   ; LD ($FFFF),A
mapst 0068C   ; LD ($FFFF),A
mapst 00774   ; LD ($FFFF),A
mapst 057D0   ; LD ($FFFF),A
mapst 05B6C   ; LD ($FFFF),A
mapst 05C8F   ; LD ($FFFF),A
page 0 tilecopy tilemap
; Entry tilecopy: the game's routine $0C2F, whole.
; Entry tilemap: the game's routine $0C66, whole.
;   Reads:   A = the tile slot: the word at $C800+2*A, plus $2000, is the VRAM address;
;            BC = the tile: the word at $C800+2*BC, plus the word at (IX+8), is the
;            source of its 32 bytes (read as the game sees it, through jt_peek in
;            $2000-$3FFF). tilecopy writes the source bytes; tilemap writes, for each
;            source byte n, the byte at $C700+n.
;   Returns: DE, HL, IX, IY and the alternate registers kept. tilecopy: A = the second
;            control byte, BC = $FFBE, as the game's OUTI loop leaves them. tilemap:
;            A = the last byte written, BC = the word at $C800+2*BC. F changes. Interrupts
;            on, as the game's EI leaves them.
;   The VDP is left as the game's writes leave it: the address after the 32 bytes.
; Runtime internals used: jt_peek, jt_vwrite.
tilecopy:
        ld (t_a),a
        xor a
        jr tile
tilemap:
        ld (t_a),a
        ld a,1
tile:   di
        ld (t_map),a
        ld (t_hl),hl
        ld (t_de),de
        ld (t_ix),ix
        ld (t_iy),iy
        ld a,(t_a)              ; DE = the VRAM address: the word at $C800+2*A, + $2000
        ld l,a
        ld h,0
        add hl,hl
        ld de,$C800
        add hl,de
        ld e,(hl)
        inc hl
        ld a,(hl)
        add a,$20
        ld d,a
        or $40
        ld (t_ctl),a            ; the game's second control byte
        ld h,b                  ; BC = the word at $C800+2*BC
        ld l,c
        add hl,hl
        ld bc,$C800
        add hl,bc
        ld c,(hl)
        inc hl
        ld b,(hl)
        ld (t_bc),bc
        ld l,(ix+8)             ; HL = the source: BC + the word at (IX+8)
        ld h,(ix+9)
        add hl,bc
        push de
        ld de,buf
        ld b,32
.byte:  call get
        ld c,a
        ld a,(t_map)
        or a
        ld a,c
        jr z,.put
        push hl
        ld h,$C7                ; tilemap: the byte at $C700+n
        ld l,c
        ld a,(hl)
        pop hl
.put:   ld (de),a
        inc de
        djnz .byte
        ld (t_last),a
        pop de
        ld hl,buf
        ld b,32
        ld c,1
        ld ix,32
        ld iy,32
        ld a,1                  ; the source as mapped: buf in this page
        call jt_vwrite
        ld ix,(t_ix)
        ld iy,(t_iy)
        ld hl,(t_hl)
        ld de,(t_de)
        ld a,(t_map)
        or a
        jr nz,.map
        ld bc,$FFBE
        ld a,(t_ctl)
        ei
        ret
.map:   ld bc,(t_bc)
        ld a,(t_last)
        ei
        ret
; A = (HL) as the game sees it, HL + 1; F changes
get:    ld a,h
        and $E0
        cp $20
        jr z,.pk
        ld a,(hl)
        inc hl
        ret
.pk:    call jt_peek
        inc hl
        ret
t_hl:   dw 0
t_de:   dw 0
t_ix:   dw 0
t_iy:   dw 0
t_bc:   dw 0
t_a:    db 0
t_map:  db 0
t_ctl:  db 0
t_last: db 0
buf:    ds 32
endpage

# Spider-Man - Return of the Sinister Six (Europe, Brazil).cht, "Infinite Health": RAM $C16A,
# the health bar (8 is full), is held at 8
poke "Infinite health"
ar 00C1-6A08
endpoke

# Spider-Man - Return of the Sinister Six (Europe, Brazil).cht, "Infinite Web": RAM $C16D, the
# web fluid (8 is full), is held at 8
poke "Infinite web"
ar 00C1-6D08
endpoke
