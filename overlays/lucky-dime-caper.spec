# The Lucky Dime Caper Starring Donald Duck (Europe, Brazil) (En), CRC32 A1710F13, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of random
# input, 180 s of the attract mode) and the scan entries below.
# Decisions:
# - No RST vector has $FF filler, so $0000-$0002 (DI; IM 1) is the io vector and the
#   game starts at $0003. The game's own code has no RST $00.
# - The game builds 768 OUTI instructions and a RET in RAM at $C66F-$CC6F ($0708) and
#   writes VRAM by jumping into that chain: the entry sets the byte count, 64 bytes for
#   every 128 bytes before $CC6F. Code in RAM is not patched, so every jump into the chain
#   is a code cave below that far-calls page 0, which writes the same bytes with
#   jt_vwrite. The chain itself is left in RAM and is no longer run.
# - The routines that end in a jump into the chain ($42DC, $1C95) stop the scanner's
#   paths after each call to them. The code after those calls ($083F, $1C3C, $1C42,
#   $1C51-$1C5A, $1C6D, $4BFF, $73A5, $785E, $7CDB, $7D8B) is a scan entry, and so are
#   the bank 0 VDP routines $04BA (rectangle with a fill byte), $051E (planar RLE),
#   $054D, $0580 (1-bit tiles) and $0708, the slot 1 routines $4519, $47CE, $482B,
#   $4842, $4855, $52DE and $683D, and the routines in slot 2 that $1C5F, $1C67, $1C6A
#   and $3323 call after mapping bank 6 or 7 ($A52A bank 6; $8BD0, $A025, $85FE bank 7).
# - The I/O byte patterns that no path reached are in banks with no code (2, 3, 4, 5, 8,
#   9, 11, 14, 15): tile graphics, maps and tables (verdict false).
name The Lucky Dime Caper Starring Donald Duck
cart A1710F13
hz 50		; No-Intro region Europe, Brazil
# The intro story writes priority cells over Scrooge's chair ($04A1, from frame 224 of the
# attract mode): Scrooge stands behind the chair's back.
priority
vector 00 io
start 0003

# VRAM fill ($0490, DE = $4000 + VRAM address, HL = a word, BC = the number of words): RST $28,
# then L and H to the data port BC times; the boot clears VRAM with it and screen changes
# clear the name table. Through the runtime each word cost about 2,900 cycles: the Game Over
# screen, which fills the name table every frame, ran at 89% of the frame. The entry writes
# the same words with jt_vwrite and returns as the loop does (BC = 0, A = 0, interrupts on).
asm 00490 5		; RST $28; LD A,L; OUT ($BE),A; PUSH AF (first byte)
    rst $00
    db far_io, pg_fill, ent_fill
    ret
endasm
# Tile unpacker at $04EF (the Sega planar RLE decoder: the plane loop at $04EF calls the core
# at $04FC, which ends a plane with RET Z), called with HL = the data and DE = a VRAM write
# address: four bit planes, each to every fourth VRAM byte, the next plane one byte later.
# It sets the VRAM address with RST $28 for every byte: the screen changes ran at about 84%
# of the frame for 40 frames and more. The library page rle_tiles does the whole routine; it
# returns as $04EF does, and also sets A' = 4, which no caller holds across the call. The
# core's OUT ($BE),A at $050B keeps its site line.
asm 004EF 5		; LD B,4; PUSH BC; PUSH DE; CALL $04FC (first byte)
    rst $00
    db far_io, pg_rle_tiles, ent_rle_tiles
    ret
endasm
# Donald's tiles ($1C95, from the frame handler at $1C39 and from $4BF9 and $7CD5): DE =
# $4000, RST $28, then ($C037) x 64 bytes from $D400 (5 to 10; any other value 4) through
# the chain. RST $28 ends with EI, and the chain runs with interrupts on; the entry does
# the same.
asm 01C98 5		; RST $28; LD C,$BE; LD HL,$D400 (first byte)
    rst $00
    db far_io, pg_donald, ent_donald
    ret
endasm
# The sprite table ($42DC): 64 bytes from $D700 to VRAM $3F00, then 128 bytes from $D780
# to $3F80, through the chain. It writes the control port itself, with no EI.
asm 042DC 5		; XOR A; OUT ($BF),A; LD A,$7F
    rst $00
    db far_io, pg_sat, ent_sat
    ret
endasm
# Tile blocks from bank 1 after RST $28 with DE set by the caller: 128 bytes ($47A9, $483C),
# 384 bytes ($47B3), 64 bytes ($47C7).
asm 047A9 5		; RST $28; LD C,$BE; JP $CB6F (first 2 bytes)
    rst $00
    db far_io, pg_v128, ent_v128
    ret
endasm
asm 047B3 5		; RST $28; LD C,$BE; JP $C96F (first 2 bytes)
    rst $00
    db far_io, pg_v384, ent_v384
    ret
endasm
asm 047C7 5		; RST $28; LD C,$BE; JP $CBEF (first 2 bytes)
    rst $00
    db far_io, pg_v64, ent_v64
    ret
endasm
asm 0483C 5		; RST $28; LD C,$BE; JP $CB6F (first 2 bytes)
    rst $00
    db far_io, pg_v128, ent_v128
    ret
endasm
# $4842 and $4855: 64 bytes through the chain (CALL $CBEF), then 64 more through the
# unrolled OUTI at $4870-$496F, then RET. The OUTI sites there keep their lines.
asm 0486A 5		; RST $28; LD C,$BE; CALL $CBEF (first 2 bytes)
    rst $00
    db far_io, pg_v128, ent_v128
    ret
endasm
# Bank 7 $A025: 256 bytes from ($C5BB) to the address in DE.
asm 1E032 8		; RST $28; LD C,$BE; LD HL,($C5BB); JP $CA6F (first 2 bytes)
    ld hl,($C5BB)
    rst $00
    db far_io, pg_v256, ent_v256
    ret
endasm
page 0 donald sat v64 v128 v256 v384 fill
; donald: ($C037) runs of 64 bytes (5 to 10, any other value 4) from $D400 to VRAM $0000.
donald:	ld hl,$D400
	ld a,($C037)
	ld c,4
	cp 5
	jr c,runs
	cp 11
	jr nc,runs
	ld c,a
	jr runs
v64:	ld c,1
	jr runs
v128:	ld c,2
	jr runs
v256:	ld c,4
	jr runs
v384:	ld c,6
; runs: C runs of 64 bytes from HL (the source as the game sees it) to the VRAM address in
; DE, in one jt_vwrite call. Returns as the chain does: HL after the last byte, B less the
; count, C = $BE; interrupts on, as RST $28 leaves them.
runs:	push ix
	push iy
	push bc
	ld b,64
	ld ix,64
	ld iy,64
	xor a
	call jt_vwrite
	pop bc
	pop iy
	pop ix
	push de
	ld a,c			; HL += C * 64
	rrca
	rrca
	ld e,a
	and $C0			; (C * 64) AND $FF
	ld d,a
	ld a,b
	sub d
	ld b,a
	ld a,e
	and $3F			; (C * 64) / 256
	ld d,a
	ld a,e
	and $C0
	ld e,a
	add hl,de
	pop de
	ld c,$BE
	ei
	ret
; sat: 64 bytes from $D700 to VRAM $3F00, then 128 bytes from $D780 to $3F80. Returns A =
; $7F, C = $BE, HL = $D800, as the game's code does.
sat:	push ix
	push iy
	ld ix,64
	ld iy,64
	ld hl,$D700
	ld de,$3F00
	ld bc,$4001
	xor a
	call jt_vwrite
	ld hl,$D780
	ld de,$3F80
	ld bc,$4002
	xor a
	call jt_vwrite
	pop iy
	pop ix
	ld hl,$D800
	ld a,$7F
	ld c,$BE
	ret
; fill: BC words (0 means 65,536) of HL to the VRAM address in DE: buf holds 128 copies of
; the word, written as runs of 256 bytes from buf (source step 0), then one run of the rest.
fill:	push ix
	push iy
	push hl
	push de
	push bc
	ex de,hl		; DE = the word
	ld hl,buf
	ld b,128
.w:	ld (hl),e
	inc hl
	ld (hl),d
	inc hl
	djnz .w
	pop bc
	pop de
	push de
	ld ix,0
	ld iy,256
	ld a,c			; the rest: (C AND $7F) words
	and $7F
	ld (rest),a
	ld a,b			; HL = BC / 128 runs of 256 bytes (0 words: 512)
	or c
	jr nz,.k
	ld hl,512
	jr .n
.k:	ld l,c
	ld h,b
	add hl,hl
	ld l,h
	ld h,0
	rl h
.n:	ld a,h
	or l
	jr z,.r
	ld c,l			; at most 256 runs a call
	ld a,h
	or a
	jr z,.c
	ld c,0
.c:	push hl
	ld b,0
	ld hl,buf
	ld a,1
	call jt_vwrite
	pop hl
	ld a,c			; DE += runs * 256 (256 runs wrap VRAM: DE stays); HL -= runs
	or a
	jr nz,.d
	dec h
	jr .n
.d:	add a,d
	ld d,a
	ld a,l
	sub c
	ld l,a
	jr nc,.n
	dec h
	jr .n
.r:	ld a,(rest)
	or a
	jr z,.e
	add a,a
	ld b,a
	ld c,1
	ld hl,buf
	ld a,1
	call jt_vwrite
.e:	pop de
	pop hl
	pop iy
	pop ix
	ld bc,0
	xor a
	ei
	ret
rest:	db 0
buf:	ds 256
endpage
libpage 1 rle_tiles  ; overlays/lib/rle_tiles.asm
site 0002A   ; OUT ($BF),A
site 0002F   ; OUT ($BF),A
site 000A9   ; IN A,($7E)
site 000B5   ; OTIR
site 00105   ; IN A,($BF)
site 00107   ; IN A,($DD)
site 00222   ; IN A,($BF)
site 002E0   ; IN A,($BE)
site 00300   ; OUT ($BE),A
site 00497   ; OUT ($BE),A
site 004A1   ; OUT ($BE),A
site 004AC   ; OUT ($BE),A
site 004B3   ; OUT ($BE),A
site 004C1   ; OUTI
site 004C8   ; OUT (C),A
site 004DE   ; OUTI
site 0050B   ; OUT ($BE),A
site 0053A   ; OUT ($BE),A
site 00594   ; OUT (C),D
site 005BA   ; IN A,($DC)
site 00614   ; IN A,($BF)
site 00616   ; IN A,($BF)
site 00622   ; IN A,($BF)
site 024AD   ; OUTI
site 042E1   ; OUT ($BF),A
site 042EC   ; OUT ($BF),A
site 042EF   ; OUT ($BF),A
site 04523   ; OUT ($BF),A
site 04527   ; OUT ($BF),A
site 0453A   ; OUT (C),L
site 0453F   ; OUT ($BF),A
site 04544   ; OUT ($BE),A
site 0454A   ; OUT ($BE),A
site 046CC   ; OUT ($BF),A
site 046D0   ; OUT ($BF),A
site 046E5   ; OUT (C),L
site 046EA   ; OUT ($BF),A
site 046EE   ; OUT ($BE),A
site 046F3   ; OUT ($BE),A
site 04872   ; OUTI
site 04876   ; OUTI
site 0487A   ; OUTI
site 0487E   ; OUTI
site 04882   ; OUTI
site 04886   ; OUTI
site 0488A   ; OUTI
site 0488E   ; OUTI
site 04892   ; OUTI
site 04896   ; OUTI
site 0489A   ; OUTI
site 0489E   ; OUTI
site 048A2   ; OUTI
site 048A6   ; OUTI
site 048AA   ; OUTI
site 048AE   ; OUTI
site 048B2   ; OUTI
site 048B6   ; OUTI
site 048BA   ; OUTI
site 048BE   ; OUTI
site 048C2   ; OUTI
site 048C6   ; OUTI
site 048CA   ; OUTI
site 048CE   ; OUTI
site 048D2   ; OUTI
site 048D6   ; OUTI
site 048DA   ; OUTI
site 048DE   ; OUTI
site 048E2   ; OUTI
site 048E6   ; OUTI
site 048EA   ; OUTI
site 048EE   ; OUTI
site 048F2   ; OUTI
site 048F6   ; OUTI
site 048FA   ; OUTI
site 048FE   ; OUTI
site 04902   ; OUTI
site 04906   ; OUTI
site 0490A   ; OUTI
site 0490E   ; OUTI
site 04912   ; OUTI
site 04916   ; OUTI
site 0491A   ; OUTI
site 0491E   ; OUTI
site 04922   ; OUTI
site 04926   ; OUTI
site 0492A   ; OUTI
site 0492E   ; OUTI
site 04932   ; OUTI
site 04936   ; OUTI
site 0493A   ; OUTI
site 0493E   ; OUTI
site 04942   ; OUTI
site 04946   ; OUTI
site 0494A   ; OUTI
site 0494E   ; OUTI
site 04952   ; OUTI
site 04956   ; OUTI
site 0495A   ; OUTI
site 0495E   ; OUTI
site 04962   ; OUTI
site 04966   ; OUTI
site 0496A   ; OUTI
site 0496E   ; OUTI
site 0729E   ; OUT ($BE),A
site 072A5   ; OUT ($BE),A
site 07F9B   ; OUT ($BE),A
site 07F9F   ; OUT ($BE),A
site 1A540   ; OUTI
site 1A542   ; OUTI
site 1A544   ; OUTI
site 1A546   ; OUTI
site 1A548   ; OUTI
site 1A54A   ; OUTI
site 1A54C   ; OUTI
site 1A54E   ; OUTI
site 281DE   ; OUT ($7F),A
site 283BA   ; OTIR
site 284EA   ; OUT ($7F),A
site 284F4   ; OUT ($7F),A
site 28511   ; OUT ($7F),A
site 28615   ; OUT ($7F),A
site 28733   ; OUT ($7F),A
site 2873C   ; OUT ($7F),A
site 2874C   ; OUT ($7F),A
site 287E1   ; OUT ($7F),A
site 2881A   ; OUT ($7F),A
mapldk 0008E   # LD HL,$FFFC; LD (HL),$80
maphl 00094   # LD (HL),$00, HL = $FFFD
maphl 00097   # LD (HL),$01, HL = $FFFE
maphl 0009A   # LD (HL),$02, HL = $FFFF
mapst 000EA   ; LD ($FFFF),A
mapst 00123   ; LD ($FFFF),A
mapst 0012A   ; LD ($FFFF),A
mapst 00359   ; LD ($FFFF),A
mapst 00436   ; LD ($FFFF),A
mapst 005DF   ; LD ($FFFF),A
mapst 00638   ; LD ($FFFF),A
mapst 00726   ; LD ($FFFF),A
mapst 00731   ; LD ($FFFF),A
mapst 0073F   ; LD ($FFFF),A
mapst 007E6   ; LD ($FFFF),A
mapst 0080C   ; LD ($FFFF),A
mapst 00841   ; LD ($FFFF),A
mapst 00889   ; LD ($FFFF),A
mapst 008E8   ; LD ($FFFF),A
mapst 009C3   ; LD ($FFFF),A
mapst 009F4   ; LD ($FFFF),A
mapst 00BA1   ; LD ($FFFF),A
mapst 00BFC   ; LD ($FFFF),A
mapst 00C0A   ; LD ($FFFF),A
mapst 00F3C   ; LD ($FFFF),A
mapst 010DC   ; LD ($FFFF),A
mapst 01102   ; LD ($FFFF),A
mapst 0111A   ; LD ($FFFF),A
mapst 0117A   ; LD ($FFFF),A
mapst 0118A   ; LD ($FFFF),A
mapst 01198   ; LD ($FFFF),A
mapst 011CD   ; LD ($FFFF),A
mapst 01C5C   ; LD ($FFFF),A
mapst 01C64   ; LD ($FFFF),A
mapst 01ECF   ; LD ($FFFF),A
mapst 01F0F   ; LD ($FFFF),A
mapst 02949   ; LD ($FFFF),A
mapst 0295B   ; LD ($FFFF),A
mapst 03407   ; LD ($FFFF),A
mapst 0352E   ; LD ($FFFF),A
mapst 036D7   ; LD ($FFFF),A
mapst 03719   ; LD ($FFFF),A
mapst 03F2B   ; LD ($FFFF),A
mapst 04275   ; LD ($FFFF),A
mapst 0433C   ; LD ($FFFF),A
mapst 04375   ; LD ($FFFF),A
mapst 043E7   ; LD ($FFFF),A
mapst 043FC   ; LD ($FFFF),A
mapst 04415   ; LD ($FFFF),A
mapst 0455C   ; LD ($FFFF),A
mapst 04575   ; LD ($FFFF),A
mapst 04772   ; LD ($FFFF),A
mapst 047DB   ; LD ($FFFF),A
mapst 04839   ; LD ($FFFF),A
mapst 04867   ; LD ($FFFF),A
mapst 04973   ; LD ($FFFF),A
mapst 052E0   ; LD ($FFFF),A
mapst 0536F   ; LD ($FFFF),A
mapst 06848   ; LD ($FFFF),A
mapst 068DF   ; LD ($FFFF),A
mapst 0711E   ; LD ($FFFF),A
mapst 071F8   ; LD ($FFFF),A
mapst 072E1   ; LD ($FFFF),A
mapst 07323   ; LD ($FFFF),A
mapst 07347   ; LD ($FFFF),A
mapst 07355   ; LD ($FFFF),A
mapst 073A7   ; LD ($FFFF),A
mapst 0746A   ; LD ($FFFF),A
mapst 077B1   ; LD ($FFFF),A
mapst 077BF   ; LD ($FFFF),A
mapst 077DC   ; LD ($FFFF),A
mapst 07C45   ; LD ($FFFF),A
mapst 07C53   ; LD ($FFFF),A
mapst 07C6D   ; LD ($FFFF),A
mapst 07C93   ; LD ($FFFF),A
mapst 07D2F   ; LD ($FFFF),A
mapst 07D8D   ; LD ($FFFF),A
mapst 07F56   ; LD ($FFFF),A

# The Lucky Dime Caper Starring Donald Duck, The (Europe, Brazil).cht, "Infinite Lives": RAM
# $C069 is the number of lives
poke "Infinite lives"
ar 00C0-6903
endpoke

# The Lucky Dime Caper Starring Donald Duck, The (Europe, Brazil).cht, "Infinite Energy And
# Weapons": RAM $C13E is Donald's energy (1 at the start of a life, $FF when he dies)
poke "Infinite energy"
ar 00C1-3E01
endpoke

# The Lucky Dime Caper Starring Donald Duck, The (Europe, Brazil).cht, "Invulnerability": RAM
# $C13F is the hit timer; a nonzero value stops hits
poke "Invincibility"
ar 00C1-3F2C
endpoke

# The Lucky Dime Caper Starring Donald Duck, The (Europe, Brazil).cht, "Infinite Time": RAM
# $C08D is the TIME bar
poke "Infinite time"
ar 00C0-8D0F
endpoke

# The Lucky Dime Caper Starring Donald Duck, The (Europe, Brazil).cht, "Maximum Hammer Power":
# RAM $C088 is the number of red diamonds shown at the left of the screen
poke "Max hammer power"
ar 00C0-8805
endpoke

# The Lucky Dime Caper Starring Donald Duck, The (Europe, Brazil).cht, "Make Donald Float In
# Mid-Air": RAM $C121 is a state byte; held at $12, the fall after a jump is slow
poke "Slow fall"
ar 00C1-2112
endpoke

# The Lucky Dime Caper Starring Donald Duck, The (Europe, Brazil).cht, "Jump Height Modifier":
# $1424 is the high byte of the jump's start speed
poke "High jump"
gg FB4-24E-199
endpoke
