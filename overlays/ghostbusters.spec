# Ghostbusters (USA, Europe, Brazil) (En), CRC32 1DDC3059, 128K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output.
# Decisions:
# - $00A2-$0555 is the game's VDP and joypad library. Some of its routines are on no
#   scanned path but are called from code the scanner cannot reach: $0533 from bank 1
#   $5FB2, $6D23 and $6D3D, $00EE from $08F4. Every I/O instruction in the library is
#   patched, so code outside the scanned paths finds it patched.
# - $0EE7 (in the table at $0DAE-$0FAF) and $13A06 (bank 4, graphics) are data.
# - $590A in bank 1 is the game's tile unpacker, the Sega planar RLE format: four bit planes, each
#   a list of runs (a count byte n, then n AND $7F literal bytes when n has bit 7, or one byte
#   repeated n times; 0 ends the plane), each byte to every fourth VRAM byte. Its loop writes a
#   byte and skips three with IN A,($BE), so each byte costs four traps: a crash in the drive
#   showed a grey screen for about 130 frames on the Next where a Master System shows it for
#   about 30. The library page rle_tiles does the same work. The game passes a VRAM address in
#   DE and sets bit 6 itself at $591F, so the cave sets it before the far call. The only caller
#   ($574A) drops DE, A and the flags after the call. The unpacker's own I/O sites no longer run.
name Ghostbusters
cart 1DDC3059
hz any		; No-Intro region USA, Europe, Brazil
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0001D   ; OTIR
site 00039   ; IN A,($BF)
site 00052   ; IN A,($BF)
site 0008F   ; OUT ($BF),A
site 00094   ; OUT ($BF),A
site 000A9   ; IN A,($BE) (VDP library, not on a scanned path)
site 000B4   ; OUT ($BE),A
site 000C0   ; OUT ($BF),A (VDP library, not on a scanned path)
site 000C5   ; OUT ($BF),A (VDP library, not on a scanned path)
site 000D1   ; OUT ($BF),A
site 000D6   ; OUT ($BF),A
site 000E4   ; OUT ($BE),A
site 000F5   ; IN A,($BE) (VDP library, not on a scanned path)
site 0010A   ; OUT ($BE),A
site 0012C   ; IN D,(C) (VDP library, not on a scanned path)
site 00131   ; IN E,(C) (VDP library, not on a scanned path)
site 00136   ; IN H,(C) (VDP library, not on a scanned path)
site 0013B   ; IN L,(C) (VDP library, not on a scanned path)
site 00146   ; OUT (C),D (VDP library, not on a scanned path)
site 0014B   ; OUT (C),E (VDP library, not on a scanned path)
site 00150   ; OUT (C),H (VDP library, not on a scanned path)
site 00155   ; OUT (C),L (VDP library, not on a scanned path)
site 0016E   ; OUT ($DF),A
site 00176   ; OUT (C),D
site 00178   ; IN A,(C)
site 0017D   ; OUT (C),E
site 0017F   ; IN A,(C)
site 00184   ; OUT (C),B
site 001BE   ; OUT ($DE),A
site 001C0   ; IN A,($DC)
site 001F9   ; OUT ($DE),A (VDP library, not on a scanned path)
site 001FB   ; IN A,($DC) (VDP library, not on a scanned path)
site 00203   ; IN A,($DD)
site 00210   ; OUT ($DE),A
site 00212   ; IN A,($DC)
site 0021C   ; OUT ($DE),A (VDP library, not on a scanned path)
site 0021E   ; IN A,($DD) (VDP library, not on a scanned path)
site 00357   ; OUT (C),H (VDP library, not on a scanned path)
site 0035C   ; OUT (C),L (VDP library, not on a scanned path)
site 00382   ; OUT (C),B
site 0038A   ; OUT (C),A
site 003A2   ; OUT (C),B (VDP library, not on a scanned path)
site 00443   ; OUT (C),A (VDP library, not on a scanned path)
site 0047B   ; OUT (C),H
site 0047F   ; OUT (C),L
site 0049B   ; OUTI
site 004A3   ; OUT (C),A
site 004B8   ; OUT ($BE),A (VDP library, not on a scanned path)
site 004C0   ; OUT ($BE),A (VDP library, not on a scanned path)
site 004DA   ; OUTI
site 004E2   ; OUT (C),A
site 004FE   ; OUTI
site 0051C   ; OUTI
site 00521   ; OUTI
site 0053B   ; OUT (C),D (VDP library, not on a scanned path)
site 00540   ; OUT (C),E (VDP library, not on a scanned path)
site 005C4   ; IN A,($DD)
site 00726   ; OUT ($BE),A
site 0072C   ; OUT ($BE),A
site 0074D   ; OUT ($BF),A
site 00751   ; OUT ($BF),A
site 0075E   ; OTIR
site 00762   ; OUT ($BE),A
site 0076F   ; OUT ($BF),A
site 00773   ; OUT ($BF),A
site 0077B   ; OTIR
site 00839   ; OUT (C),A
site 00841   ; OUT (C),A
site 008AA   ; OUT ($BE),A
site 008B1   ; OUT ($BE),A
site 00917   ; IN A,($7E)
site 0091D   ; OUT ($BF),A
site 00921   ; OUT ($BF),A
site 012C7   ; OUT ($BE),A
site 012CD   ; OUT ($BE),A
site 014B1   ; OUT ($BE),A
site 014B5   ; OUT ($BE),A
site 058D4   ; OTIR
site 0591C   ; OUT ($BF),A
site 05921   ; OUT ($BF),A
site 0592D   ; OUT ($BE),A
site 0592F   ; IN A,($BE)
site 05931   ; IN A,($BE)
site 05933   ; IN A,($BE)
site 05947   ; OUT ($BE),A
site 05949   ; IN A,($BE)
site 0594B   ; IN A,($BE)
site 0594D   ; IN A,($BE)
site 07885   ; OUT ($3F),A
site 07887   ; IN A,($DD)
site 07891   ; OUT ($3F),A
site 07893   ; IN A,($DD)
site 0789C   ; OUT ($3F),A
site 1C170   ; OUT ($7F),A
site 1C17B   ; OUT ($7F),A
site 1C4E5   ; OUT ($7F),A
site 1C53F   ; OUT ($7F),A
site 1C559   ; OTIR
site 1C560   ; OUT ($7F),A
site 1C564   ; OUT ($7F),A
libpage 0 rle_tiles
asm 0590A 7          ; LD B,4; PUSH BC; PUSH DE; CALL $5918: the unpacker's plane loop
    set 6,d          ; the VRAM write command, as the game's $591F makes it
    rst $00
    db far_io, pg_rle_tiles, ent_rle_tiles
    ret
endasm
mapst 002CB   ; LD ($FFFF),A
mapst 002D4   ; LD ($FFFF),A
mapst 00563   ; LD ($FFFF),A
mapst 0057C   ; LD ($FFFF),A
mapst 0058D   ; LD ($FFFF),A
mapst 005D1   ; LD ($FFFF),A
mapst 010AF   ; LD ($FFFF),A
mapst 016C0   ; LD ($FFFF),A
mapst 016C8   ; LD ($FFFF),A
mapst 05734   ; LD ($FFFF),A
mapst 058BF   ; LD ($FFFF),A

# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database

# Ghostbusters (USA, Europe, Brazil).cht, "Infinite Money": RAM $CE01 is the middle byte of the
# credit (BCD, tens of dollars: $CE00-$CE02 = 00 08 00 shows $8000); held at $99 the credit
# never falls below $99,000, through the car purchase and the driving costs
poke "Infinite money"
ar 00CE-0199
endpoke

# Ghostbusters (USA, Europe, Brazil).cht, "Infinite Overall Time": RAM $CE0B rises with game
# time and the City's PK Energy bar on the map follows it; held at 0 the bar stays empty
poke "PK energy stays low"
ar 00CE-0B00
endpoke

# Ghostbusters (USA, Europe, Brazil).cht, "Infinite Ghostbusters": RAM $CE0D is the number of
# Ghostbusters; held at 3 a Ghostbuster slimed in the ghost-catching scene is not lost
poke "Infinite Ghostbusters"
ar 00CE-0D03
endpoke

# Ghostbusters (USA, Europe, Brazil).cht, "Infinite Beam Power": RAM $CE81 is the beam power;
# held at $5F the beams in the ghost-catching scene never use it up
poke "Infinite beam power"
ar 00CE-815F
endpoke
