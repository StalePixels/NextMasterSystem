# Alex Kidd - High-Tech World (USA, Europe, Brazil) (En), CRC32 013C0A94, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input).
# Decisions:
# - No free RST vector, so $0000 is the io vector.
# - $037B (OUT ($BE),A in the fill loop $0375-$0385) is patched: nothing in the cart
#   calls the routine, but it is code and the patch costs nothing.
# - The line handler at line 7 of the title ($01D8, state 1) writes H scroll at $0234,
#   and in some frames ($C1DA runs out) a name table column of 8 cells first ($0213-$0233:
#   two control writes and two OUTI for each cell). Through single traps the column took
#   about 30 lines, so the H write came near line 40, and the top rows of the scrolling logo
#   ("ALEX") kept H 0 in those frames. Page 0, entry col8, writes the column with one
#   jt_vwrite call. With it the H write still came at line 17, a line into the logo, so
#   the cave at $0213 writes H first (line 8 or 9; line 14 on the Master System, in rows
#   that show only the backdrop) and then the column. The handler's end ($01C8) takes
#   every register from the stack, so the page leaves the registers as jt_vwrite returns
#   them, but for IX and IY.
# - hsplit is off: the title's split (H from line 8, H 0 from line 81) gave the same
#   pixels with it and without it.
# - The other CHECK rows of the draft are data (graphics and tables in banks 1, 4, 6).
name Alex Kidd - High-Tech World
cart 013C0A94
hz any		; No-Intro regions USA, Europe, Brazil
priority
vector 00 io
start 0003
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
otir 00033   ; OUTI
site 0014C   ; IN A,($BF)
site 0015F   ; IN A,($DD)
asm 00213 33           ; line handler: H scroll first, then the name table column in page 0
    ex de,hl            ; HL = the column's command word
    ld de,($C1DD)
    ld d,$88
    rst $08             ; register 8, as at $0234
    ex de,hl
    rst $00
    db far_io, pg_col8, ent_col8
    jp $023B            ; register 10 = $FF, then the handler's end
endasm
site 002EE   ; OUT ($BE),A
otir 002FB   ; OUTI
site 00309   ; OUTI
site 0030D   ; OUT (C),A
site 0031C   ; INI
site 00337   ; OUT ($BE),A
site 0033C   ; OUT ($BE),A
site 00349   ; OUTI
site 00360   ; OUTI
site 00366   ; OUT (C),A
site 0037B   ; OUT ($BE),A
site 0039A   ; OUT (C),D
otir 003C1   ; OUTI
otir 003CE   ; OUTI
otir 003E4   ; OUTI
site 003F0   ; OUTD
site 003F6   ; OUT ($BE),A
otir 00401   ; OUTI
site 00412   ; OUTI
site 00414   ; OUTD
site 00420   ; OTIR
site 00423   ; OUT ($BE),A
site 0045A   ; OUT ($BF),A
site 0045D   ; OUT ($BF),A
site 00460   ; OUT ($BE),A
site 00488   ; OUT ($BE),A
site 00526   ; IN A,($DC)
site 005A5   ; OUT ($BE),A
site 005AC   ; OUT ($BE),A
site 01B75   ; OUT ($BE),A
site 01B7C   ; OUT ($BE),A
site 03DBD   ; OUT ($BE),A
site 03DC2   ; IN A,($BE)
site 03DDD   ; OUT ($BE),A
site 03DE2   ; IN A,($BE)
site 03E86   ; OUTI
site 03E88   ; OUTI
site 03E8A   ; OUTI
site 03E8C   ; OUTI
site 03E8E   ; OUTI
site 03E90   ; OUTI
site 03E92   ; OUTI
site 03E94   ; OUTI
site 03E96   ; OUTI
site 03E98   ; OUTI
site 03E9A   ; OUTI
site 03E9C   ; OUTI
site 03E9E   ; OUTI
site 03EA0   ; OUTI
site 03EA2   ; OUTI
site 03EA4   ; OUTI
site 03EA6   ; OUTI
site 03EA8   ; OUTI
site 03EAA   ; OUTI
site 03EAC   ; OUTI
site 03EAE   ; OUTI
site 03EB0   ; OUTI
site 03EB2   ; OUTI
site 03EB4   ; OUTI
site 03EB6   ; OUTI
site 03EB8   ; OUTI
site 03EBA   ; OUTI
site 03EBC   ; OUTI
site 03EBE   ; OUTI
site 03EC0   ; OUTI
site 03EC2   ; OUTI
site 03EC4   ; OUTI
site 03EDC   ; OUTI
site 03EE2   ; OUTI
site 03EE8   ; OUTI
site 03EEE   ; OUTI
site 03EF4   ; OUTI
site 03EFA   ; OUTI
site 03F00   ; OUTI
site 03F06   ; OUTI
site 03F0C   ; OUTI
site 03F12   ; OUTI
site 03F18   ; OUTI
site 03F1E   ; OUTI
site 03F24   ; OUTI
site 03F2A   ; OUTI
site 03F30   ; OUTI
site 03F36   ; OUTI
site 03F3C   ; OUTI
site 03F42   ; OUTI
site 03F48   ; OUTI
site 03F4E   ; OUTI
site 03F54   ; OUTI
site 03F5A   ; OUTI
site 03F60   ; OUTI
site 03F66   ; OUTI
site 03F6C   ; OUTI
site 03F72   ; OUTI
site 03F78   ; OUTI
site 03F7E   ; OUTI
site 03F84   ; OUTI
site 03F8A   ; OUTI
site 03F90   ; OUTI
site 03F96   ; OUTI
site 03FD5   ; OUTI
site 03FD9   ; OUT (C),A
site 03FF0   ; OUTI
site 03FF4   ; OUT (C),A
site 04003   ; OUT ($BE),A
site 0400C   ; OUT ($BE),A
site 04025   ; OUT (C),L
site 04027   ; OUT (C),H
site 0402A   ; OUT (C),E
site 0402C   ; OUT (C),D
site 0405E   ; OUT ($BE),A
site 04066   ; OUT ($BE),A
site 04079   ; OUT ($BE),A
site 0408D   ; OUT ($BE),A
site 04099   ; OUT ($BE),A
site 040A3   ; OUT ($BE),A
site 040AB   ; OUT ($BE),A
site 05F7E   ; OUTI
site 05F84   ; OUT (C),A
site 07DD1   ; OUT ($BE),A
site 07DD8   ; OUT ($BE),A
site 07E31   ; OUT ($BE),A
site 07E34   ; OUT ($BE),A
site 0807E   ; OUT ($7F),A
site 080F0   ; OUT ($7F),A
site 080FB   ; OUT ($7F),A
site 084D4   ; OUT ($7F),A
site 08577   ; OUT ($7F),A
site 085E9   ; OUT ($7F),A
site 08603   ; OTIR
site 0860A   ; OUT ($7F),A
site 0860E   ; OUT ($7F),A
mapldk 00078   # LD HL,$FFFE; LD (HL),$01
maphl 0007E   # LD (HL),$00, HL = $FFFD
maphl 00081   # LD (HL),$00, HL = $FFFC
mapst 00085   ; LD ($FFFF),A
mapst 000AC   ; LD ($FFFF),A
mapst 0017A   ; LD ($FFFF),A
mapst 001BA   ; LD ($FFFF),A
mapst 001C5   ; LD ($FFFF),A
mapst 00248   ; LD ($FFFF),A
mapst 00727   ; LD ($FFFF),A
mapst 00744   ; LD ($FFFF),A
mapst 0074A   ; LD ($FFFF),A
mapst 00761   ; LD ($FFFF),A
mapst 00770   ; LD ($FFFF),A
mapst 00797   ; LD ($FFFF),A
mapst 0079D   ; LD ($FFFF),A
mapst 00804   ; LD ($FFFF),A
mapst 00823   ; LD ($FFFF),A
mapst 0089E   ; LD ($FFFF),A
mapst 008CB   ; LD ($FFFF),A
mapst 00915   ; LD ($FFFF),A
mapst 00959   ; LD ($FFFF),A
mapst 00C2F   ; LD ($FFFF),A
mapst 00C3D   ; LD ($FFFF),A
mapst 00C50   ; LD ($FFFF),A
mapst 00C7D   ; LD ($FFFF),A
mapst 00D2E   ; LD ($FFFF),A
mapst 00D43   ; LD ($FFFF),A
mapst 00D6D   ; LD ($FFFF),A
mapst 00DB1   ; LD ($FFFF),A
mapst 00DC4   ; LD ($FFFF),A
mapst 00EFE   ; LD ($FFFF),A
mapst 00F14   ; LD ($FFFF),A
mapst 00F75   ; LD ($FFFF),A
mapst 01061   ; LD ($FFFF),A
mapst 01462   ; LD ($FFFF),A
mapst 014FD   ; LD ($FFFF),A
mapst 0156E   ; LD ($FFFF),A
mapst 0163A   ; LD ($FFFF),A
mapst 016C9   ; LD ($FFFF),A
mapst 01A69   ; LD ($FFFF),A
mapst 01A83   ; LD ($FFFF),A
mapst 01B09   ; LD ($FFFF),A
mapst 01B55   ; LD ($FFFF),A
mapld 01B97   # LD HL,$FFFF; LD (HL),$84
mapst 01BA8   ; LD ($FFFF),A
mapst 03D4B   ; LD ($FFFF),A
mapst 03DFF   ; LD ($FFFF),A
mapst 03E6D   ; LD ($FFFF),A
mapst 040EA   ; LD ($FFFF),A
mapst 0411D   ; LD ($FFFF),A
mapst 0414A   ; LD ($FFFF),A
mapst 04166   ; LD ($FFFF),A
mapst 04172   ; LD ($FFFF),A
mapst 043C3   ; LD ($FFFF),A
mapst 04812   ; LD ($FFFF),A
mapst 04DF4   ; LD ($FFFF),A
mapst 04E14   ; LD ($FFFF),A
mapst 04ED3   ; LD ($FFFF),A
mapst 04EF5   ; LD ($FFFF),A
mapst 04EFD   ; LD ($FFFF),A
mapst 04F21   ; LD ($FFFF),A
mapst 04F68   ; LD ($FFFF),A
mapst 04F9C   ; LD ($FFFF),A
mapst 04FB0   ; LD ($FFFF),A
mapst 0503B   ; LD ($FFFF),A
mapst 050A6   ; LD ($FFFF),A
mapst 0525C   ; LD ($FFFF),A
mapst 05276   ; LD ($FFFF),A
mapst 05284   ; LD ($FFFF),A
mapst 052E5   ; LD ($FFFF),A
mapst 05311   ; LD ($FFFF),A
mapst 05324   ; LD ($FFFF),A
mapst 05367   ; LD ($FFFF),A
mapst 0554D   ; LD ($FFFF),A
mapst 0557C   ; LD ($FFFF),A
mapst 0558D   ; LD ($FFFF),A
mapst 055C1   ; LD ($FFFF),A
mapst 055FF   ; LD ($FFFF),A
mapst 0566D   ; LD ($FFFF),A
mapst 05692   ; LD ($FFFF),A
mapst 056BA   ; LD ($FFFF),A
mapst 056CD   ; LD ($FFFF),A
mapst 056DB   ; LD ($FFFF),A
mapst 0572E   ; LD ($FFFF),A
mapst 05740   ; LD ($FFFF),A
mapst 0578C   ; LD ($FFFF),A
mapst 057D9   ; LD ($FFFF),A
mapst 05834   ; LD ($FFFF),A
mapst 05A68   ; LD ($FFFF),A
mapst 05DDC   ; LD ($FFFF),A
mapst 05DF0   ; LD ($FFFF),A
mapst 05E3D   ; LD ($FFFF),A
mapst 05E7A   ; LD ($FFFF),A
mapst 05E88   ; LD ($FFFF),A
mapst 05F04   ; LD ($FFFF),A
mapst 05F1F   ; LD ($FFFF),A
mapst 05F59   ; LD ($FFFF),A
mapst 06FC4   ; LD ($FFFF),A
mapst 0703C   ; LD ($FFFF),A
mapst 0704D   ; LD ($FFFF),A
mapst 0709A   ; LD ($FFFF),A
mapst 070A8   ; LD ($FFFF),A
mapst 070C8   ; LD ($FFFF),A
mapst 070DF   ; LD ($FFFF),A
mapst 070ED   ; LD ($FFFF),A
mapst 070F3   ; LD ($FFFF),A
mapst 07119   ; LD ($FFFF),A
mapst 07133   ; LD ($FFFF),A
mapst 07247   ; LD ($FFFF),A
mapst 07252   ; LD ($FFFF),A
mapst 073AF   ; LD ($FFFF),A
mapst 073B7   ; LD ($FFFF),A
mapst 07461   ; LD ($FFFF),A
mapst 0746A   ; LD ($FFFF),A
mapst 07D72   ; LD ($FFFF),A
mapst 07DA0   ; LD ($FFFF),A
mapst 07DFA   ; LD ($FFFF),A
mapst 07E40   ; LD ($FFFF),A
# Mapper stores found by the byte scan in code no path reached:
mapst 00643   # LD ($FFFF),A; after LD A,$82; 32 bytes of valid code before it
mapst 00655   # LD ($FFFF),A; after LD A,$86; 32 bytes of valid code before it
mapst 00671   # LD ($FFFF),A; after LD A,$82; 32 bytes of valid code before it
mapst 04B2B   # LD ($FFFF),A; after LD A,$86; 32 bytes of valid code before it

page 0 col8
; col8: the line handler's name table column ($0213-$0233). DE = the VDP command word of
; the column's first cell ($4000 + address), 8 cells of 2 bytes from $CD00, one row
; (64 bytes) apart. Keeps IX and IY; HL, DE, BC, A and F as jt_vwrite returns them.
col8:
    ld (c8_ix),ix
    ld (c8_iy),iy
    ld hl,$CD00
    ld bc,$0208
    ld ix,2
    ld iy,64
    xor a
    call jt_vwrite
    ld ix,(c8_ix)
    ld iy,(c8_iy)
    ret
c8_ix: dw 0
c8_iy: dw 0
endpage

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Infinite Time - Seconds Digits": RAM
# $C10E is the clock minutes in BCD; held at 0, the clock never advances and never reaches 17:00
poke "Infinite time"
ar 00C1-0E00
endpoke

# Alex Kidd - High-Tech World (USA, Europe) (Action Replay) (diff2).cht, "Timer - Minutes
# Modifier": RAM $C10F is the clock hour in BCD, held at the value chosen (00 to 16)
poke "Clock hour ??"
ar 00C1-0F??
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Start Time Modifier": the clock
# starts a new game at 0:00 instead of 9:00, so the game runs to 17:00 over 17 hours
poke "Extra time"
gg 000-8B9-C4E
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Invincibility": the contact test of
# the first object slot returns before the hit flag is set
poke "Invincibility"
gg C9D-0DE-809
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Map Pieces [Replace ? With 1-8 For
# Each Piece]": RAM $C082 is the map piece shown on the map screen, 1 to 8 (9 is the fake piece)
poke "Map piece ??"
ar 00C0-82??
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Have Ladder": RAM $C084
poke "Have ladder"
ar 00C0-8401
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Have Restorer": RAM $C085
poke "Have restorer"
ar 00C0-8501
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Have Key": RAM $C086
poke "Have key"
ar 00C0-8601
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Have Pencil": RAM $C087
poke "Have pencil"
ar 00C0-8701
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Have Eraser": RAM $C088
poke "Have eraser"
ar 00C0-8801
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Have Cloth": RAM $C089
poke "Have cloth"
ar 00C0-8901
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Have Hang Glider": RAM $C08A
poke "Have hang glider"
ar 00C0-8A01
endpoke

# Alex Kidd - High-Tech World (USA, Europe, Brazil).cht, "Enable Scene Select after Starting a
# New Game" and "Enable Scene Select after Resuming a Saved Game": the game state set after
# the title menu becomes the scene select screen. Each line covers one menu choice
poke "Scene select"
gg 0D6-3EA-F7E
gg 0D6-38A-F7A
endpoke
