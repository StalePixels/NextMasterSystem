# Ecco - The Tides of Time (Brazil), CRC32 7C28703A, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, checked against reference I/O logs
# (600 s of random input, 180 s of the attract mode).
# Scan entries:
# - the targets of the game's keyed switch at bank 2 $B6E6 (CALL $B6E6, then 3-byte
#   entries of address and key, ended by a zero word and the default address), from
#   the calls at $A1EB, $A987, $A9FB and $AAE5;
# - the module entries: $04D0, $04D5, $04E8 and $04ED map bank N (3, 25, 15, 17) in
#   slot 1 and N+1 in slot 2 and jump through the word table at $4000 + 2L; the L values
#   the callers pass give 3:485B 3:402D 3:47E3 3:4A97 3:4839 3:4A22, 19:68A8 1A:B137,
#   10:AD87 10:AF3D and 11:4AA3; module code calls into slot 2 then name bank N+1;
# - 3:5317 and 10:B539 10:B556 10:B5AA 10:B5C1, VDP routines that the reference ran.
# Decisions:
# - hz 60: the only region is Brazil.
# - No RST vector is free, so $0000-$0002 (DI; IM 1) is the io vector and the game
#   starts at $0003.
# - The game has no HALT.
# - No hsplit: the line interrupt at line 23 sets the H scroll of the water surface
#   band; MAME runs of the surface scene with and without hsplit look the same.
# - LD ($FFFE),IX at $0E53 has no mapper line form; it jumps to a code cave in the
#   zero bytes at $3D40 (bank 0, the end of the bank's data).
# - Byte scan hits left out as data: IN D,(C) at $0EF65 (bank 3) and IN H,(C) at
#   $37F24 (bank 13) are in tables; OUT ($3E),A at $3E9DC is the end of
#   LD ($D355),BC and LD A,$FF.
name Ecco - The Tides of Time
cart 7C28703A
hz 60
vector 00 io
start 0003
site 00008   ; OUT ($BF),A
site 0000D   ; OUT ($BF),A
site 00078   ; IN A,($7E)
site 00085   ; OUT ($BF),A
site 0008C   ; OUT ($BF),A
site 00095   ; OUT ($BF),A
site 00099   ; OUT ($BF),A
site 0009F   ; OUT ($BE),A
site 000A7   ; OUT ($BF),A
site 000AB   ; OUT ($BF),A
site 000B0   ; OUT ($BE),A
site 000FD   ; IN A,($BF)
site 00187   ; OUT ($7F),A
site 0018B   ; OUT ($7F),A
site 0018F   ; OUT ($7F),A
site 00193   ; OUT ($7F),A
site 0019E   ; OUT ($BF),A
site 001A4   ; OUT ($BF),A
site 001B1   ; IN A,($7E)  (library routine $01B1: IN A,($7E); LD C,A; RET)
site 001B5   ; IN A,($7F)  (library routine $01B5: IN A,($7F); LD C,A; RET; called from bank 25 $6E88)
site 001BA   ; OUT ($BF),A
site 001BF   ; OUT ($BF),A
site 001D6   ; OTIR
site 001DE   ; OTIR
site 001E9   ; OTIR
site 00243   ; OUT ($BF),A
site 00248   ; OUT ($BF),A
site 00261   ; OUT ($BE),A
site 0026E   ; OUT ($BE),A
site 0027B   ; OUT ($BE),A
site 00288   ; OUT ($BE),A
site 0037F   ; OUT ($BF),A
site 00385   ; OUT ($BF),A
site 00685   ; IN A,($BF)  (routine $0671, after the wait loop at $0677)
site 00A29   ; IN A,($BF)
site 00A52   ; OUT ($BF),A
site 00A5A   ; OUT ($BF),A
site 00ADD   ; OUT ($BF),A
site 00AE1   ; OUT ($BF),A
site 00AFC   ; OTIR
site 00B09   ; OTIR
site 00B0E   ; OUT ($BF),A
site 00B12   ; OUT ($BF),A
site 00B14   ; OTIR
site 00B19   ; OUT ($BE),A
site 00B21   ; OUTI
site 00B2F   ; OUT ($BF),A
site 00B33   ; OUT ($BF),A
site 00B3B   ; OTIR
site 00B3D   ; OTIR
site 00B3F   ; OTIR
site 00B4C   ; OUT ($BF),A
site 00B50   ; OUT ($BF),A
site 00B58   ; OTIR
site 00B5A   ; OTIR
site 00B5C   ; OTIR
site 00B68   ; OUT ($BF),A
site 00B6C   ; OUT ($BF),A
site 00B74   ; OTIR
site 00B76   ; OTIR
site 00C40   ; OUT ($BF),A
site 00C47   ; OUT ($BF),A
site 00C51   ; OTIR
site 00C5D   ; OTIR
site 00C62   ; OTIR
site 00C9F   ; OUT ($BF),A
site 00CAD   ; OUT ($BF),A
site 00CAF   ; OUTI
site 00CB1   ; OUTI
site 00CBC   ; OUT ($BF),A
site 00CC4   ; OUT ($BF),A
site 00CC6   ; OUTI
site 00CC8   ; OUTI
site 00D42   ; OUT ($BF),A
site 00D47   ; OUT ($BF),A
site 00D4B   ; OTIR
site 00DB4   ; OUT ($BF),A
site 00DB9   ; OUT ($BF),A
site 00DBD   ; OTIR
site 00DD8   ; OTIR        (bank call helper $0DD2: RST $20; OTIR; restores the banks)
site 00DFE   ; OUT ($BF),A
site 00E06   ; OUT ($BF),A
site 00E10   ; OUT ($BF),A
site 00E18   ; OUT ($BF),A
site 00E1E   ; OUT ($BF),A
site 00E26   ; OUT ($BF),A
site 00E2E   ; OUT ($BF),A
site 00E36   ; OUT ($BF),A
site 00E68   ; OUT ($BF),A
site 00E6F   ; OUT ($BF),A
site 00E93   ; OUT ($BE),A
site 00EC5   ; OUT ($BF),A
site 00ECA   ; OUT ($BF),A
site 00ECF   ; OTIR
site 013CD   ; OUT ($BF),A
site 013D4   ; OUT ($BF),A
site 013DB   ; OUTI
site 013E1   ; OUTI
site 0141A   ; OUT ($BF),A
site 01423   ; OUT ($BF),A
site 0142A   ; OUTI
site 05DCC   ; OUT ($BE),A
site 05DD6   ; OUT ($BF),A
site 05DDB   ; OUT ($BF),A
site 05DF1   ; OUT ($BE),A
site 05DF9   ; IN A,($DC)
site 05E08   ; IN A,($DC)
site 05E14   ; IN A,($DC)
site 0D31E   ; OUT ($BF),A
site 0D323   ; OUT ($BF),A
site 0D339   ; OUT ($BE),A
site 0D341   ; OUT ($BE),A
site 0D349   ; OUT ($BE),A
site 0D350   ; OUT ($BE),A
site 304F6   ; OUT ($7F),A
site 3050B   ; OUT ($7F),A
site 30514   ; OUT ($7F),A
site 3051F   ; OUT ($7F),A
site 3054A   ; OUT ($7F),A
site 3069E   ; OUT ($7F),A
site 306D5   ; OUT ($7F),A
site 306DE   ; OUT ($7F),A
site 306FC   ; OUT ($7F),A
site 30700   ; OUT ($7F),A
site 307B6   ; OUT ($7F),A
site 307CC   ; OUT ($7F),A
site 307E4   ; OUT ($7F),A
site 307E8   ; OUT ($7F),A
site 307F6   ; OUT ($7F),A
site 30834   ; OUT ($7F),A
site 4353A   ; OUT ($BF),A
site 4353F   ; OUT ($BF),A
site 43544   ; OUT ($BE),A
site 43549   ; OUT ($BE),A
site 4354E   ; OUT ($BE),A
site 43553   ; OUT ($BE),A
site 43557   ; OUT ($BF),A
site 4355C   ; OUT ($BF),A
site 43565   ; OUT ($BE),A
site 4356B   ; OUT ($BE),A
site 43572   ; OUT ($BE),A
site 43578   ; OUT ($BE),A
site 43586   ; OUT ($BF),A
site 4358B   ; OUT ($BF),A
site 43594   ; OUT ($BE),A
site 4359A   ; OUT ($BE),A
site 435A1   ; OUT ($BE),A
site 435A7   ; OUT ($BE),A
site 435AB   ; OUT ($BF),A
site 435B0   ; OUT ($BF),A
site 435BC   ; OUT ($BE),A
site 435C2   ; OUT ($BF),A
site 435C7   ; OUT ($BF),A
site 435D3   ; OUT ($BE),A
mapst 00020   ; LD ($FFFE),A
mapst 00024   ; LD ($FFFF),A
mapldk 000E0   # LD HL,$FFFE; LD (HL),$0C
maphl 000E8   # LD (HL),$01, HL = $FFFE
mapsthl 0016F   ; LD ($FFFE),HL
mapsthl 001F9   # LD ($FFFE),HL; after POP HL; 32 bytes of valid code before it
mapst 0037B   ; LD ($FFFE),A
mapsthl 003BE   ; LD ($FFFE),HL
mapst 003C9   ; LD ($FFFE),A
mapst 003D0   ; LD ($FFFE),A
mapst 003D5   ; LD ($FFFC),A
mapst 003D8   ; LD ($FFFD),A
mapst 003DC   ; LD ($FFFE),A
mapst 003E0   ; LD ($FFFF),A
mapst 004F4   ; LD ($FFFE),A
mapst 004F8   ; LD ($FFFF),A
mapsthl 00509   ; LD ($FFFE),HL
mapst 00513   ; LD ($FFFE),A
mapsthl 0060C   ; LD ($FFFE),HL
mapstde 00B8B   ; LD ($FFFE),DE
mapsthl 00C7B   ; LD ($FFFE),HL
mapsthl 00DCE   ; LD ($FFFE),HL
mapstde 00DDA   ; LD ($FFFE),DE  (bank call helper $0DD2)
mapsthl 00E89   ; LD ($FFFE),HL
mapst 01005   ; LD ($FFFE),A
mapsthl 01026   ; LD ($FFFE),HL
mapstbc 01052   ; LD ($FFFE),BC
mapsthl 01271   ; LD ($FFFE),HL
mapsthl 0143A   ; LD ($FFFE),HL
mapst 01650   ; LD ($FFFE),A
mapsthl 01657   ; LD ($FFFE),HL
mapsthl 0167F   # LD ($FFFE),HL; after POP HL; 32 bytes of valid code before it
mapstbc 01749   ; LD ($FFFE),BC
mapstbc 017F6   ; LD ($FFFE),BC
mapstbc 01812   ; LD ($FFFE),BC
mapstbc 01879   ; LD ($FFFE),BC
mapstbc 018A3   ; LD ($FFFE),BC
mapstde 018BF   ; LD ($FFFE),DE
mapstde 01948   ; LD ($FFFE),DE
mapstbc 0195C   ; LD ($FFFE),BC
mapstde 01A65   ; LD ($FFFE),DE
mapstbc 01CB6   # LD ($FFFE),BC; after LD BC,$0201; 32 bytes of valid code before it
mapstde 01CBF   ; LD ($FFFE),DE  (routine $1CAE: maps banks 1 and 2, reads a byte, restores the banks)
mapstde 01CCC   ; LD ($FFFE),DE
mapstde 01CD9   ; LD ($FFFE),DE
# LD ($FFFE),IX; EI; RET at $0E53, the end of the copy routine $0E39, which restores
# both banks from IX after an LDIR. The cave in the zero bytes at $3D40 does the same
# through the LD ($FFFE),BC inline code, with no stack use; BC is 0 after the LDIR, as
# the cave leaves it.
asm 00E53 6
    jp ix_banks
endasm
label ix_banks 03D40
asm 03D40 13
    ld b,ixh
    ld c,ixl
    rst $00
    db $22, 0, 0       ; LD ($FFFE),BC
    ld bc,0
    ei
    ret
endasm

# Ecco - The Tides of Time (Brazil).cht, "Swim Through Objects Cheat"
poke "Swim through walls"
ar 00DB-3801
endpoke
