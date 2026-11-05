# Rampart (Europe), CRC32 426E5C8A, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand.
#
# Decisions:
# - $000C-$0037 is NOP filler that no code reaches: RST $10 is the io vector, and
#   $0013-$0037 and $005D-$0065 (between the frame handler's RETI and the NMI entry)
#   hold the fill caves below. With the io vector at $0000 the title menu does not start
#   the game. Both IM 1 instructions become IM 2: $0001 (power on) and $0007 (the soft
#   reset at $0006 that the frame handler takes when the Reset button is down).
# - The territory fill ($0960, an object handler) walks a map whose rows are 34 bytes
#   apart. Its column walks run past $DFFF into the RAM mirror ($E00A-$E49A in a 600 s
#   reference log of random input), which on a Master System is RAM at $C000-$C49A and
#   on the Next is the runtime's page. Its cell stack grows down from $C648 and runs
#   below $C000 ($BFA6-$BFFF in the same log), where a Master System ignores the
#   stores and the Next would write the cart in slot 2. The reference logs show no other
#   code that touches the mirror or stores below $C000. Each cell access in the fill
#   calls a cave that clears bit 5 of H for $E000-$FFFF. The cell stores and the stack
#   push skip stores below $C000: once the stack has run below $C000, the fill pops
#   cart bytes as cell addresses and marks cells in the cart, which a Master System
#   ignores (the stack pointer is always even, so a pair of stack stores never
#   straddles $C000). The caves use up to 6 bytes of the game's stack; in the reference
#   log the game's own stack reaches $DFD7.
# - The name table routine at bank 1 $67A0 (after the RET at $679F) and the
#   port $3F routine at bank 1 $6D02 (LD A,$FF; OUT ($3F),A; RET, after the RET at
#   $6D01) are code that no scanned path reaches; their sites are patched.
# - The game runs code only in banks 0 and 1; banks 2-15 are data that it pages
#   into slot 2. The byte patterns that no path reached in banks 6, 7, 11, 13, 14
#   and 15 are data; OUT ($3F),A at $1E1FD and IN A,($F1) at $3594A have the
#   verdict false.
name Rampart
cart 426E5C8A
hz 50		; No-Intro region Europe
vector 10 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00007 2   ; IM 1 -> IM 2
    im 2
endasm
label fmap 00013
label rmw 0001A
label cpush 0002B
label rdb 0005D
asm 00013 37   ; NOP filler: fill caves
; fmap: HL at $E000-$FFFF becomes its RAM address at $C000-$DFFF. A = H as it came in;
; F changed.
    ld a,h
    cp $E0
    ret c
    res 5,h
    ret
; rmw: the cell at HL = (cell AND $5F) OR (IX+9), as LD A,(HL); AND $5F; OR (IX+9);
; LD (HL),A, with the mirror at $E000-$FFFF read and written as RAM, and no store
; below $C000 (cart ROM on a Master System). HL kept; A, F changed.
    push hl
    call fmap
    cp $C0
    jr c,.ro
    ld a,(hl)
    and $5F
    or (ix+9)
    ld (hl),a
.ro:
    pop hl
    ret
; cpush: push HL on the fill's cell stack at DE, as DEC DE; LD A,H; LD (DE),A; DEC DE;
; LD A,L; LD (DE),A, without the stores when they are below $C000. A, F changed.
    dec de
    dec de
    ld a,d
    cp $C0
    ret c
    ld a,l
    ld (de),a
    inc de
    ld a,h
    ld (de),a
    dec de
    ret
endasm
asm 0005D 9   ; free bytes after the frame handler's RETI: fill cave
; rdb: A = the cell at HL and BIT 7,A, as LD A,(HL); BIT 7,A, with the mirror at
; $E000-$FFFF read as RAM. HL kept.
    push hl
    call fmap
    ld a,(hl)
    pop hl
    bit 7,a
    ret
endasm
asm 00972 7   ; LD A,(HL); AND $5F; OR (IX+$09); LD (HL),A
    call rmw
endasm
asm 00980 3   ; LD A,(HL); BIT 7,A
    call rdb
endasm
asm 0098E 7   ; LD A,(HL); AND $5F; OR (IX+$09); LD (HL),A
    call rmw
endasm
asm 0099C 3   ; LD A,(HL); BIT 7,A
    call rdb
endasm
asm 009E9 3   ; LD A,(HL); BIT 7,A
    call rdb
endasm
asm 009F2 6   ; DEC DE; LD A,H; LD (DE),A; DEC DE; LD A,L; LD (DE),A
    call cpush
endasm
asm 009F8 7   ; LD A,(HL); AND $5F; OR (IX+$09); LD (HL),A
    call rmw
endasm
site 0003A   ; IN A,($BF)
site 0003C   ; IN A,($DD)
site 00698   ; OUT ($BE),A
site 00EA0   ; OUT ($BE),A
site 00EA7   ; OUT ($BE),A
site 00EAE   ; OUT ($BE),A
site 00EB5   ; OUT ($BE),A
site 00EC5   ; OUT ($BE),A
site 00ECC   ; OUT ($BE),A
site 00ED3   ; OUT ($BE),A
site 00EDA   ; OUT ($BE),A
site 00FD8   ; OUT ($BE),A
site 00FDF   ; OUT ($BE),A
site 01323   ; OUT ($BE),A
site 0132A   ; OUT ($BE),A
site 013AA   ; OUT ($BE),A
site 013B1   ; OUT ($BE),A
site 013C9   ; OUT ($BE),A
site 013D0   ; OUT ($BE),A
site 019DD   ; OUT ($BE),A
site 019E4   ; OUT ($BE),A
site 01A44   ; OUT ($BE),A
site 01A4B   ; OUT ($BE),A
site 01A73   ; OUT ($BE),A
site 01A7A   ; OUT ($BE),A
site 01AB4   ; OUT ($BE),A
site 01ABB   ; OUT ($BE),A
site 01B2C   ; OUT ($BE),A
site 01B33   ; OUT ($BE),A
site 01B7E   ; OUT ($BE),A
site 01B85   ; OUT ($BE),A
site 03608   ; OUT ($BE),A
site 0360F   ; OUT ($BE),A
site 03640   ; IN A,($BE)
site 03648   ; IN A,($BE)
site 03670   ; OUT ($BE),A
site 03677   ; OUT ($BE),A
site 0375E   ; OUT ($BE),A
site 03765   ; OUT ($BE),A
site 03939   ; OUT ($BE),A
site 03940   ; OUT ($BE),A
site 03956   ; OUT ($BE),A
site 0395D   ; OUT ($BE),A
site 03963   ; OUT ($BE),A
site 0396A   ; OUT ($BE),A
site 041F1   ; OUT ($BE),A
site 041F8   ; OUT ($BE),A
site 042A5   ; OUT ($BE),A
site 042AC   ; OUT ($BE),A
site 044E4   ; OUT ($BE),A
site 044E9   ; OUT ($BE),A
site 04500   ; OUT ($BE),A
site 04508   ; OUT ($BE),A
site 0451F   ; OUT ($BE),A
site 04526   ; OUT ($BE),A
site 0484B   ; OUT ($BE),A
site 04852   ; OUT ($BE),A
site 04859   ; OUT ($BE),A
site 0485F   ; OUT ($BE),A
site 04886   ; OUT ($BE),A
site 0488D   ; OUT ($BE),A
site 048B7   ; OUT ($BE),A
site 048BC   ; OUT ($BE),A
site 04B1F   ; OUT ($BE),A
site 04B27   ; OUT ($BE),A
site 04B2E   ; OUT ($BE),A
site 04B39   ; OUT ($BE),A
site 04B4C   ; OUT ($BE),A
site 04B54   ; OUT ($BE),A
site 04B5B   ; OUT ($BE),A
site 04B63   ; OUT ($BE),A
site 04B8A   ; OUT ($BE),A
site 04B92   ; OUT ($BE),A
site 04BBA   ; OUT ($BE),A
site 04BC1   ; OUT ($BE),A
site 04C6E   ; OUT ($7F),A
site 04C83   ; OUT ($7F),A
site 04CA1   ; OUT ($7F),A
site 04CB2   ; OUT ($7F),A
site 04CEF   ; OUT ($7F),A
site 05DBF   ; OUT ($BE),A
site 05DC4   ; OUT ($BE),A
site 05DDB   ; OUT ($BE),A
site 05DE2   ; OUT ($BE),A
site 05DED   ; OUT ($BE),A
site 05DF4   ; OUT ($BE),A
site 05DFC   ; OUT ($BE),A
site 05E03   ; OUT ($BE),A
site 05E09   ; OUT ($BE),A
site 05E10   ; OUT ($BE),A
site 05E27   ; OUT ($BE),A
site 05E2C   ; OUT ($BE),A
site 06778   ; OUT ($BF),A
site 0677F   ; OUT ($BF),A
site 06786   ; OUT ($BE),A
site 0678D   ; OUT ($BF),A
site 06794   ; OUT ($BF),A
site 0679A   ; OUT ($BE),A
site 06803   ; OUT ($BF),A
site 0680A   ; OUT ($BF),A
site 06813   ; OUT ($BE),A
site 06819   ; OUT ($BE),A
site 06831   ; OUT ($BF),A
site 06838   ; OUT ($BF),A
site 06844   ; OUT ($BE),A
site 0684A   ; OUT ($BE),A
site 06887   ; OUT ($BF),A
site 0688E   ; OUT ($BF),A
site 0689B   ; OUT ($BE),A
site 068A2   ; OUT ($BE),A
site 068C6   ; OUT ($BF),A
site 068CD   ; OUT ($BF),A
site 068DD   ; OUT ($BE),A
site 068E4   ; OUT ($BE),A
site 06900   ; OUT ($BF),A
site 06907   ; OUT ($BF),A
site 0691D   ; OUT ($BE),A
site 06975   ; OUT ($BF),A
site 0697C   ; OUT ($BF),A
site 06981   ; OUT ($BE),A
site 0698B   ; OUT ($BF),A
site 06992   ; OUT ($BF),A
site 06996   ; OUT ($BF),A
site 0699B   ; OUT ($BF),A
site 069B0   ; OUT ($BE),A
site 069B6   ; OUT ($BE),A
site 069D7   ; OTIR
site 069DA   ; OUT ($BE),A
site 069EB   ; OUT ($BE),A
site 069F7   ; OUT ($BF),A
site 069FA   ; OUT ($BF),A
site 06A34   ; OUT ($BF),A
site 06A3B   ; OUT ($BF),A
site 06A41   ; OUT ($BE),A
site 06AF6   ; OUT ($BE),A
site 06B10   ; OUT ($BE),A
otir 06C73   ; OUTI
otir 06C83   ; OUTI
site 06D17   ; IN A,($DC)
site 06D24   ; IN A,($DC)
site 06D27   ; IN A,($DD)
mapst 00083   ; LD ($FFFC),A
mapst 0017C   ; LD ($FFFF),A
mapst 001A2   ; LD ($FFFF),A
mapst 004B1   ; LD ($FFFF),A
mapst 00506   ; LD ($FFFF),A
mapst 00523   ; LD ($FFFF),A
mapst 0054A   ; LD ($FFFF),A
mapst 0063E   ; LD ($FFFF),A
mapst 010A2   ; LD ($FFFF),A
mapst 010CF   ; LD ($FFFF),A
mapst 01146   ; LD ($FFFF),A
mapst 0122F   ; LD ($FFFF),A
mapst 01486   ; LD ($FFFF),A
mapst 014A1   ; LD ($FFFF),A
mapst 014F8   ; LD ($FFFF),A
mapst 01536   ; LD ($FFFF),A
mapst 0153F   ; LD ($FFFF),A
mapst 0157D   ; LD ($FFFF),A
mapst 01586   ; LD ($FFFF),A
mapst 015B3   ; LD ($FFFF),A
mapst 015D0   ; LD ($FFFF),A
mapst 015FD   ; LD ($FFFF),A
mapst 0161D   ; LD ($FFFF),A
mapst 0164B   ; LD ($FFFF),A
mapst 01651   ; LD ($FFFF),A
mapst 0167F   ; LD ($FFFF),A
mapst 01A99   ; LD ($FFFF),A
mapst 01AC0   ; LD ($FFFF),A
mapst 01BE1   ; LD ($FFFF),A
mapst 02E64   ; LD ($FFFF),A
mapst 02E92   ; LD ($FFFF),A
mapst 02F03   ; LD ($FFFF),A
mapst 02F45   ; LD ($FFFF),A
mapst 0387A   ; LD ($FFFF),A
mapst 03888   ; LD ($FFFF),A
mapst 03972   ; LD ($FFFF),A
mapst 03DE1   ; LD ($FFFF),A
mapst 040B0   ; LD ($FFFF),A
mapst 0437E   ; LD ($FFFF),A
mapst 0438C   ; LD ($FFFF),A
mapst 04397   ; LD ($FFFF),A
mapst 043B9   ; LD ($FFFF),A
mapst 043E9   ; LD ($FFFF),A
mapst 05B8E   ; LD ($FFFF),A
mapst 05C65   ; LD ($FFFF),A
mapst 05C7F   ; LD ($FFFF),A
mapst 05CC8   ; LD ($FFFF),A
mapst 0605F   ; LD ($FFFF),A
mapst 0613F   ; LD ($FFFF),A
mapst 062D7   ; LD ($FFFF),A
mapst 06414   ; LD ($FFFF),A
mapst 06441   ; LD ($FFFF),A
mapst 06459   ; LD ($FFFF),A
mapst 06509   ; LD ($FFFF),A
mapst 06520   ; LD ($FFFF),A
mapst 06538   ; LD ($FFFF),A
mapst 06572   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 001E4   ; LD ($FFFF),A (byte scan: after LD A,$0E)
mapst 0020A   ; LD ($FFFF),A (byte scan: after POP AF)
site 067B3   ; OUT ($BE),A
site 067B9   ; OUT ($BE),A
site 06D04   ; OUT ($3F),A

# Rampart (Europe).cht, "Timer counts down slower": the frame count that makes one second goes
# from 60 to 90 (code at $0E4A and $0E4E)
poke "Slower timer"
gg 5AE-4AF-19A
gg 5AE-4EF-19A
endpoke

# Rampart (Europe).cht, "Timer counts down much slower": the frame count that makes one second
# goes from 60 to 127
poke "Much slower timer"
gg 7FE-4AF-19A
gg 7FE-4EF-19A
endpoke

# Rampart (Europe).cht, "Always get 3 Cannons, unless you don't have any more space for them":
# RAM $C68C, the number of cannons left to place, starts at 3 and not 2
poke "3 cannons"
gg 00F-24E-D5D
gg 3EF-25E-D5E
gg 03F-26E-6EA
endpoke

# Rampart (Europe).cht, "Always get 4 Cannons, unless you don't have any more space for them":
# RAM $C68C starts at 4 and not 2
poke "4 cannons"
gg 00F-24E-D5D
gg 3EF-25E-D5E
gg 04F-26E-6EA
endpoke
