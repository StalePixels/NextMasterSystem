# Penguin Land (USA, Europe), CRC32 F97E9875, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with no reference I/O log, then decided by hand.
#
# Decisions:
# - Cart RAM: the routines at $403B-$40DC (bank 1) turn on cart RAM with $FFFC = $08, copy
#   $1B8 bytes between $DA80 and $800A and keep a $4B4F mark at $8008 and $9C10; every one of
#   those $FFFC stores is patched. The stores into $8008-$9C20 are cart RAM and need no patch.
# - $40DD-$40E6 (XOR A; LD ($DA80),A; LD A,$00; LD ($FFFC),A; RET) is named by no call, jump
#   or table, but its $FFFC store is patched like the others.
# - Port $F0-$F2 (FM): $01A2 tests for the FM unit by writing $F2 and reading it back. The read
#   gives no match, so the game takes its PSG path, as on a Master System with no FM unit.
# - The pointer harvest takes the data pointer $6400 (stored into $C11C at $2C24) and the
#   sprite tables at $2EF9 and $3390 for code; the stores, RST calls and transfers decoded from
#   them ($640C, $33A9, $0037, $2002, $0046, $0078) are bytes of data or of operands, and
#   get no patch.
# - No code runs from slot 2: banks 2-7 are data. The byte patterns there ($1C06C, $183DC and
#   the very-low rows) are data.
name Penguin Land
cart F97E9875
hz any		; No-Intro regions USA, Europe
# Priority tiles: the block in a round that a drip sprite runs down from has the priority
# bit, and the drip moves up behind it.
priority
# No free RST vector: $0000-$0002 (DI; LD SP part) becomes the vector,
# the game starts at $0004 with the SP its LD SP,nn set.
vector 00 io
start 0004 C0FF
asm 00004 2   ; IM 1 -> IM 2
    im 2
endasm
site 00081   ; OUT ($DF),A
site 00186   ; OUT ($3F),A
site 00188   ; IN A,($DD)
site 00191   ; OUT ($3F),A
site 00193   ; IN A,($DD)
site 0019B   ; OUT ($DE),A
site 001A7   ; OUT ($3E),A
site 001AF   ; OUT ($F2),A
site 001B2   ; IN A,($F2)
site 001C4   ; OUT ($F2),A
site 001CC   ; OUT ($3E),A
site 001DE   ; IN A,($BF)
site 0025F   ; IN A,($DD)
site 002BE   ; IN A,($DC)
site 00480   ; OUT ($BE),A
site 00485   ; OUT ($BE),A
site 0048A   ; OUT ($BE),A
site 0048F   ; OUT ($BE),A
site 004F1   ; OUT ($BF),A
site 004F6   ; OUT ($BF),A
site 004FA   ; OUT ($BF),A
site 004FD   ; OUT ($BF),A
site 00501   ; IN A,($BE)
site 00506   ; OUT ($BF),A
site 00509   ; OUT ($BF),A
site 0050C   ; OUT ($BE),A
site 00510   ; OUT ($BF),A
site 00513   ; OUT ($BF),A
site 00516   ; OUT ($BE),A
site 00520   ; OUT ($BF),A
site 00523   ; OUT ($BF),A
site 00526   ; OUT ($BE),A
site 0052B   ; OUT ($BE),A
site 00535   ; OUT ($BF),A
site 00538   ; OUT ($BF),A
site 0053B   ; OUT ($BE),A
site 00546   ; OUT ($BF),A
site 00549   ; OUT ($BF),A
site 0054E   ; OUT ($BE),A
site 00553   ; OUT ($BE),A
site 0055E   ; OUT ($BF),A
site 00561   ; OUT ($BF),A
site 00566   ; OUTI
site 00576   ; OUT ($BF),A
site 00579   ; OUT ($BF),A
site 00607   ; OUT ($BF),A
site 0060A   ; OUT ($BF),A
site 0060C   ; OTIR
site 006FD   ; IN A,($DC)
site 01E1D   ; OUT ($BF),A
site 01E21   ; OUT ($BF),A
site 01E26   ; OUT ($BE),A
site 01F46   ; OUT ($BE),A
site 01F5A   ; OUT ($BE),A
site 01F69   ; OUT ($BE),A
site 01F86   ; OUT ($BE),A
site 01F8B   ; OUT ($BE),A
site 01F90   ; OUT ($BE),A
site 01F95   ; OUT ($BE),A
site 021F9   ; OUT ($BF),A
site 021FC   ; OUT ($BF),A
site 02200   ; IN A,($BE)
site 02202   ; IN A,($BE)
site 02209   ; IN A,($BE)
site 0220B   ; IN A,($BE)
site 0220D   ; IN A,($BE)
site 0220F   ; IN A,($BE)
site 02219   ; IN A,($BE)
site 0221D   ; IN A,($BE)
site 02399   ; OUT ($BF),A
site 0239C   ; OUT ($BF),A
site 023A1   ; OUT ($BE),A
site 023A7   ; OUT ($BE),A
site 023AD   ; OUT ($BE),A
site 023B3   ; OUT ($BE),A
site 03863   ; OUT ($BF),A
site 03866   ; OUT ($BF),A
site 0386B   ; OUTI
site 03905   ; OUT ($BE),A
site 0390A   ; OUT ($BE),A
site 0390F   ; OUT ($BE),A
site 03914   ; OUT ($BE),A
site 039AE   ; OUT ($BF),A
site 039B1   ; OUT ($BF),A
site 039B5   ; OUTI
site 039B7   ; OUTI
site 039B9   ; OUTI
site 039BB   ; OUTI
site 039BD   ; OUTI
site 039BF   ; OUTI
site 039C1   ; OUTI
site 039C3   ; OUTI
site 039C5   ; OUTI
site 039C7   ; OUTI
site 039C9   ; OUTI
site 039CB   ; OUTI
site 039CD   ; OUTI
site 039CF   ; OUTI
site 039D1   ; OUTI
site 039D3   ; OUTI
site 039D5   ; OUTI
site 039D7   ; OUTI
site 039D9   ; OUTI
site 039DB   ; OUTI
site 039DD   ; OUTI
site 039DF   ; OUTI
site 039E1   ; OUTI
site 039E3   ; OUTI
site 039E5   ; OUTI
site 039E7   ; OUTI
site 039E9   ; OUTI
site 039EB   ; OUTI
site 039ED   ; OUTI
site 039EF   ; OUTI
site 039F1   ; OUTI
site 039F3   ; OUTI
site 039F5   ; OUTI
site 039F7   ; OUTI
site 039F9   ; OUTI
site 039FB   ; OUTI
site 039FD   ; OUTI
site 039FF   ; OUTI
site 03A01   ; OUTI
site 03A03   ; OUTI
site 03A05   ; OUTI
site 03A07   ; OUTI
site 03A09   ; OUTI
site 03A0B   ; OUTI
site 03A0D   ; OUTI
site 03A0F   ; OUTI
site 03A11   ; OUTI
site 03A13   ; OUTI
site 03A15   ; OUTI
site 03A17   ; OUTI
site 03A19   ; OUTI
site 03A1B   ; OUTI
site 03A1D   ; OUTI
site 03A1F   ; OUTI
site 03A21   ; OUTI
site 03A23   ; OUTI
site 03A25   ; OUTI
site 03A27   ; OUTI
site 03A29   ; OUTI
site 03A2B   ; OUTI
site 03A2D   ; OUTI
site 03A2F   ; OUTI
site 03A31   ; OUTI
site 03A33   ; OUTI
site 03A35   ; OUTI
site 03A37   ; OUTI
site 03A39   ; OUTI
site 03A3B   ; OUTI
site 03A3D   ; OUTI
site 03A3F   ; OUTI
site 03A41   ; OUTI
site 03A43   ; OUTI
site 03A45   ; OUTI
site 03A47   ; OUTI
site 03A49   ; OUTI
site 03A4B   ; OUTI
site 03A4D   ; OUTI
site 03A4F   ; OUTI
site 03A51   ; OUTI
site 03A53   ; OUTI
site 03A55   ; OUTI
site 03A57   ; OUTI
site 03A59   ; OUTI
site 03A5B   ; OUTI
site 03A5D   ; OUTI
site 03A5F   ; OUTI
site 03A61   ; OUTI
site 03A63   ; OUTI
site 03A65   ; OUTI
site 03A67   ; OUTI
site 03A69   ; OUTI
site 03A6B   ; OUTI
site 03A6D   ; OUTI
site 03A6F   ; OUTI
site 03A71   ; OUTI
site 03A73   ; OUTI
site 03A75   ; OUTI
site 03A77   ; OUTI
site 03A79   ; OUTI
site 03A7B   ; OUTI
site 03A7D   ; OUTI
site 03A7F   ; OUTI
site 03A81   ; OUTI
site 03A83   ; OUTI
site 03A85   ; OUTI
site 03A87   ; OUTI
site 03A89   ; OUTI
site 03A8B   ; OUTI
site 03A8D   ; OUTI
site 03A8F   ; OUTI
site 03A91   ; OUTI
site 03A93   ; OUTI
site 03A95   ; OUTI
site 03A97   ; OUTI
site 03A99   ; OUTI
site 03A9B   ; OUTI
site 03A9D   ; OUTI
site 03A9F   ; OUTI
site 03AA1   ; OUTI
site 03AA3   ; OUTI
site 03AA5   ; OUTI
site 03AA7   ; OUTI
site 03AA9   ; OUTI
site 03AAB   ; OUTI
site 03AAD   ; OUTI
site 03AAF   ; OUTI
site 03AB1   ; OUTI
site 03AB3   ; OUTI
site 03CF3   ; OUT ($BF),A
site 03CF6   ; OUT ($BF),A
site 03CF8   ; IN A,($BE)
site 03D11   ; OUT ($BF),A
site 03D16   ; OUT ($BF),A
site 03D30   ; OUT ($BE),A
site 03D36   ; OUT ($BE),A
site 03D4D   ; OUT ($BF),A
site 03D52   ; OUT ($BF),A
site 03D5C   ; IN A,($BE)
site 03D63   ; IN A,($BE)
site 03D65   ; IN A,($BE)
site 03D6B   ; IN A,($BE)
site 03DC6   ; OUT ($BE),A
site 03DCC   ; OUT ($BE),A
site 03DD1   ; OUT ($BE),A
site 03DD7   ; OUT ($BE),A
site 03DEA   ; OUT ($BF),A
site 03DEF   ; OUT ($BF),A
site 03E0A   ; OUT ($BF),A
site 03E0D   ; OUT ($BF),A
site 03E1C   ; OUT ($BE),A
site 03E22   ; OUT ($BE),A
site 03F47   ; OUT ($BE),A
site 03F4C   ; OUT ($BE),A
site 03F50   ; OUT ($BE),A
site 03F55   ; OUT ($BE),A
site 03F63   ; OUT ($BF),A
site 03F67   ; OUT ($BF),A
site 03F6E   ; OUT ($BE),A
site 03F73   ; OUT ($BE),A
site 045C1   ; OUT ($BF),A
site 045C5   ; OUT ($BF),A
site 045CD   ; OUT ($BE),A
site 045D2   ; OUT ($BE),A
site 045D7   ; OUT ($BE),A
site 045DC   ; OUT ($BE),A
site 04754   ; OUT ($BF),A
site 04758   ; OUT ($BF),A
site 0484E   ; OUT ($BF),A
site 04853   ; OUT ($BF),A
site 0485C   ; OUT ($BE),A
site 0486D   ; OUT ($BE),A
site 0487D   ; OUT ($BE),A
site 04882   ; OUT ($BE),A
site 04892   ; OUT ($BE),A
site 04898   ; OUT ($BE),A
site 048A9   ; OUT ($BF),A
site 048AE   ; OUT ($BF),A
site 048B3   ; OUT ($BE),A
site 048D3   ; OUT ($BF),A
site 048D8   ; OUT ($BF),A
site 048DD   ; OUT ($BE),A
site 04903   ; OUT ($BF),A
site 04907   ; OUT ($BF),A
site 051C0   ; OUT (C),B
site 051CA   ; OUT ($F1),A
site 0520F   ; OUT ($7F),A
site 0530D   ; OUT ($F0),A
site 05313   ; OUT ($F1),A
site 05330   ; OUTI
site 05337   ; OUTI
site 05358   ; OUT ($7F),A
site 0535C   ; OUT ($7F),A
site 053A6   ; OUT ($F0),A
site 053AD   ; OUT ($F1),A
site 053B5   ; OUT ($F0),A
site 053BB   ; OUT ($F1),A
site 054B5   ; OUT ($F0),A
site 054BC   ; OUT (C),L
site 054C5   ; OUT ($F0),A
site 054E0   ; OUT (C),H
site 054E8   ; OUT ($F0),A
site 054F6   ; OUT ($F1),A
site 054FE   ; OUT ($F0),A
site 05508   ; OUT ($F1),A
site 0568B   ; OUT ($F0),A
site 05692   ; OUTI
site 056E6   ; OUT ($7F),A
site 057A2   ; OUT ($7F),A
site 057A6   ; OUT ($7F),A
site 057C3   ; OUT ($7F),A
site 057E5   ; OUT ($7F),A
site 057F1   ; OUT ($F0),A
site 057FC   ; OUT ($F1),A
site 05806   ; OUT ($F0),A
site 05814   ; OUT ($F1),A
site 0587A   ; OTIR
site 05888   ; OUT (C),D
site 0588E   ; OUT ($F1),A
site 058CA   ; OUT ($7F),A
site 0591B   ; OUT ($7F),A
site 059A6   ; OUT ($7F),A
site 059C4   ; OUT ($7F),A
site 05A04   ; OUT ($7F),A
site 05A0E   ; OUT ($7F),A
site 05A56   ; OUT ($7F),A
mapst 000A1   ; LD ($FFFF),A
mapst 002FC   ; LD ($FFFF),A
mapst 004B9   ; LD ($FFFF),A
mapst 004C7   ; LD ($FFFF),A
mapst 0082C   ; LD ($FFFF),A
mapst 00875   ; LD ($FFFF),A
mapst 01C1D   ; LD ($FFFF),A
mapst 01CF8   ; LD ($FFFF),A
mapst 01E2A   ; LD ($FFFF),A
mapst 01E50   ; LD ($FFFF),A
mapst 01FDA   ; LD ($FFFF),A
mapst 01FEB   ; LD ($FFFF),A
mapst 0203F   ; LD ($FFFF),A
mapst 020CD   ; LD ($FFFF),A
mapst 022A1   ; LD ($FFFF),A
mapst 03615   ; LD ($FFFF),A
mapst 03846   ; LD ($FFFF),A
mapst 03998   ; LD ($FFFF),A
mapst 03AFC   ; LD ($FFFF),A
mapst 0403D   ; LD ($FFFC),A
mapst 04062   ; LD ($FFFC),A
mapst 04080   ; LD ($FFFC),A
mapst 04086   ; LD ($FFFC),A
mapst 04095   ; LD ($FFFC),A
mapst 0409B   ; LD ($FFFC),A
mapst 040C5   ; LD ($FFFC),A
mapst 040CB   ; LD ($FFFC),A
mapst 040D9   ; LD ($FFFC),A
mapst 044E9   ; LD ($FFFF),A
mapst 04518   ; LD ($FFFF),A
mapst 04546   ; LD ($FFFF),A
mapst 04727   ; LD ($FFFF),A
mapst 047D8   ; LD ($FFFF),A
mapst 047F1   ; LD ($FFFF),A
mapst 040E3   ; LD ($FFFC),A in $40DD-$40E6, which no path reaches

# Penguin Land (USA, Europe) (Action Replay).cht, "Infinite Eggs (Lives)": RAM $C119 is
# the egg count (the lives), held at 9
poke "Infinite eggs"
ar 00C1-1909
endpoke

# Penguin Land (USA, Europe) (Action Replay).cht, "Infinite Time": RAM $C11D is the
# time shown on screen, held at $63 (99)
poke "Infinite time"
ar 00C1-1D63
endpoke

# Penguin Land (USA, Europe).cht, "Start With ?? Eggs": the byte at $0B05 is the egg
# count that a new game starts with (LD A,3), replaced by the number set on the Pokes page
poke "Start with eggs"
gg ??B-05F-E66
endpoke
