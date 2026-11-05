# Sagaia (Europe, Brazil) (En), CRC32 66388128, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - RST $30 ($0030-$0037) is $FF filler: it is the io vector.
# - The VDP routines at $A824 and $B29C (bank 2) are code that only the recordings
#   reach; their I/O and mapper sites are patched.
# - $40DD in bank 1 is an inline jump table dispatcher (RLCA; POP HL; the word at
#   HL+2A). Calls to it from bank 2 have an unknown slot 1 bank for the scanner; a
#   breakpoint run showed bank 1 in slot 1 at every such call, and bank 2 in slot 2
#   at every call from bank 1 into slot 2.
# - The byte scan's mapper stores at $21FA, $2204, $26F2, $37B0 (bank 0) and $B659,
#   $B664 (bank 2) are code: each follows LD A,n in a whole routine.
# - Unused code: the VDP address routine at $1618 (no call, jump or table names it)
#   and the PSG silence routine at bank 7 $473F (the table at $4748 does not name
#   it).
# - The scanner's Codemasters-style stores LD (HL),A at $3680 and $369A write $FF to
#   the RAM flag at $C393 (HL from $3612; the scanner loses it at CALL $40BC). The
#   cart uses the Sega mapper: they are not patched.
# - Data: the OUT ($F0), OUT ($C0) and OUT ($C1) patterns in bank 7 are music data
#   (the game has no FM code: it never reads port $F2); IN A,($DC) at $7CE9 and
#   IN A,($DD) at $FFF0 are in tables of numbers; IN A,($7E) at $3FBD8 is graphics.
name Sagaia
cart 66388128
hz 50		; No-Intro regions Europe, Brazil
vector 30 io
asm 00083 2   ; IM 1 -> IM 2
    im 2
endasm
site 00009   ; IN A,($BF)
site 0000C   ; OUT ($BF),A
site 0000F   ; OUT ($BF),A
site 0001C   ; OUT ($BE),A
site 0002D   ; OTIR
site 00087   ; OUT ($3E),A
site 000D3   ; IN A,($BF)
site 000D5   ; IN A,($BF)
site 000E0   ; IN A,($BF)
site 0010F   ; OUT ($7F),A
site 00114   ; OUT ($BF),A
site 00118   ; OUT ($BF),A
site 0011E   ; OUT ($BE),A
site 00159   ; IN A,($BF)
site 0015C   ; OUT ($BF),A
site 00161   ; OUT ($BF),A
site 00194   ; IN A,($BF)
site 00312   ; IN A,(C)
site 003F3   ; OUT ($BF),A
site 003F7   ; OUT ($BF),A
site 00400   ; OTIR
site 00436   ; OUT ($BF),A
site 0043B   ; OUT ($BF),A
site 0043E   ; OUT ($BE),A
site 00442   ; OUT ($BE),A
site 00472   ; IN A,($BF)
site 00478   ; OUT ($BF),A
site 0047C   ; OUT ($BF),A
site 00482   ; OTIR
site 00486   ; OUT ($BF),A
site 0048B   ; OUT ($BF),A
site 0048D   ; OTIR
site 0097F   ; OUT (C),A
site 00983   ; OUT (C),A
site 00986   ; IN A,($BF)
site 009A3   ; OUT ($BF),A
site 009A7   ; OUT ($BF),A
site 00A32   ; IN A,($7E)
site 00A60   ; IN A,($7E)
site 00A6F   ; IN A,($7E)
site 01632   ; IN A,($BF)
site 0177E   ; OUT ($BF),A
site 01783   ; OUT ($BF),A
site 01786   ; OUT ($BE),A
site 0178A   ; OUT ($BE),A
site 0179D   ; OUT ($BF),A
site 017A2   ; OUT ($BF),A
site 017A5   ; OUT ($BE),A
site 017A9   ; OUT ($BE),A
site 017B9   ; IN A,($7E)
site 017C5   ; IN A,($7E)
site 017D6   ; OUT ($BF),A
site 017DA   ; OUT ($BF),A
site 017DF   ; OUT ($BE),A
site 017EB   ; IN A,($BF)
site 01831   ; OUT (C),E
site 01833   ; OUT (C),D
site 01842   ; OTIR
site 01876   ; OUT ($BF),A
site 0187B   ; OUT ($BF),A
site 01881   ; OUT ($BE),A
site 01885   ; OUT ($BE),A
site 018BB   ; OUT ($BF),A
site 018C0   ; OUT ($BF),A
site 018C3   ; OUT ($BE),A
site 018C7   ; OUT ($BE),A
site 018F8   ; OUT ($BF),A
site 018FD   ; OUT ($BF),A
site 0190D   ; OUT ($BE),A
site 01911   ; OUT ($BE),A
site 01915   ; OUT ($BE),A
site 01919   ; OUT ($BE),A
site 01930   ; OUT ($BF),A
site 01935   ; OUT ($BF),A
site 0194F   ; OUT ($BE),A
site 01951   ; OUT ($BE),A
site 01953   ; OUT ($BE),A
site 01955   ; OUT ($BE),A
site 0196F   ; OUT ($BF),A
site 01974   ; OUT ($BF),A
site 019A7   ; OUT ($BE),A
site 019CD   ; OUT (C),L
site 019CF   ; OUT (C),H
site 019D8   ; OTIR
site 019DA   ; OTIR
site 019DC   ; OTIR
site 019DE   ; OTIR
site 019E0   ; OTIR
site 019E2   ; OTIR
site 019E4   ; OTIR
site 019EF   ; OUT ($BF),A
site 019F3   ; OUT ($BF),A
site 019F9   ; OUT ($BE),A
site 019FD   ; OUT ($BE),A
site 01A1A   ; OUT ($BF),A
site 01A1F   ; OUT ($BF),A
site 01A28   ; OTIR
site 01A4A   ; OUT ($BF),A
site 01A4F   ; OUT ($BF),A
site 01A52   ; OUT ($BE),A
site 01A56   ; OUT ($BE),A
site 01A8E   ; OUT ($BF),A
site 01A95   ; OUT ($BF),A
site 01AA6   ; OUT ($BE),A
site 01AAA   ; OUT ($BE),A
site 01AD6   ; OUT ($BF),A
site 01AD9   ; OUT ($BF),A
site 01ADC   ; OUT ($BE),A
site 01AE0   ; OUT ($BE),A
site 01AFE   ; OUT ($BF),A
site 01B01   ; OUT ($BF),A
site 01B06   ; OUT ($BE),A
site 01B0A   ; OUT ($BE),A
site 01B2B   ; IN A,(C)
site 01B2D   ; OUT (C),E
site 01B2F   ; OUT (C),D
site 01B40   ; OTIR
site 01B5C   ; IN A,(C)
site 01B5E   ; OUT (C),E
site 01B60   ; OUT (C),D
site 01B69   ; OTIR
site 01B77   ; OUT ($BF),A
site 01B7C   ; OUT ($BF),A
site 01B8E   ; OUT ($BE),A
site 01BB4   ; OUT ($BF),A
site 01BB7   ; OUT ($BF),A
site 01BC0   ; OUT ($BE),A
site 01BC4   ; OUT ($BE),A
site 01BD5   ; OUT ($BF),A
site 01BD8   ; OUT ($BF),A
site 01BDF   ; OUT ($BE),A
site 01BE3   ; OUT ($BE),A
site 01C18   ; OUT ($BF),A
site 01C1D   ; OUT ($BF),A
site 01C3C   ; OUT ($BE),A
site 01C40   ; OUT ($BE),A
site 01C50   ; OUT ($BF),A
site 01C55   ; OUT ($BF),A
site 01C5D   ; OUT ($BE),A
site 01C61   ; OUT ($BE),A
site 01C6E   ; OUT ($BF),A
site 01C73   ; OUT ($BF),A
site 01C94   ; OUT ($BE),A
site 01C98   ; OUT ($BE),A
site 0763F   ; IN A,($BE)
site 0767C   ; OUT ($BF),A
site 0767F   ; OUT ($BF),A
site 0A82A   ; OUT (C),E
site 0A82C   ; OUT (C),D
site 0A830   ; OTIR
site 0AC01   ; IN A,($BF)
site 0AC0B   ; IN A,(C)
site 0AC0E   ; OUT (C),E
site 0AC10   ; OUT (C),D
site 0AC1E   ; OUT ($BE),A
site 0AC22   ; OUT ($BE),A
site 0AC92   ; OUT ($BE),A
site 0AC96   ; OUT ($BE),A
site 0AD77   ; IN A,(C)
site 0AD7A   ; OUT (C),A
site 0AD7E   ; OUT (C),A
site 0AD93   ; OUT (C),A
site 0B0CB   ; OUT ($B0),A
site 0B0CD   ; IN A,($B0)
site 0B29C   ; OUT ($BF),A
site 0B2A0   ; OUT ($BF),A
site 0B2A7   ; OUT ($BE),A
site 0B302   ; OUT ($BF),A
site 0B306   ; OUT ($BF),A
site 0B310   ; OTIR
site 0B314   ; OTIR
site 0B320   ; OTIR
site 0B322   ; OTIR
site 0B324   ; OTIR
site 0B326   ; OTIR
site 0B34D   ; OUT ($BF),A
site 0B351   ; OUT ($BF),A
site 0B354   ; OUT ($BF),A
site 0B358   ; OUT ($BF),A
site 100F2   ; IN A,($BF)
site 1013F   ; IN A,($BF)
site 10153   ; IN A,($BF)
site 1019A   ; IN A,($BF)
site 101A0   ; OUT ($BF),A
site 101A3   ; OUT ($BF),A
site 101B5   ; OUT ($BE),A
site 101B9   ; OUT ($BE),A
site 101BD   ; OUT ($BE),A
site 101C2   ; OUT ($BE),A
site 12D62   ; IN A,($BF)
site 12D69   ; OUT ($BF),A
site 12D6C   ; OUT ($BF),A
site 12D6E   ; IN A,($BE)
site 12D73   ; IN A,($BE)
site 12D7B   ; OUT ($BF),A
site 12D7E   ; OUT ($BF),A
site 12D80   ; IN A,($BE)
site 12D85   ; OUT ($BE),A
site 1AFF0   ; OUT ($BF),A
site 1AFF5   ; OUT ($BF),A
site 1AFFA   ; OUT ($BE),A
site 1B000   ; OUT ($BE),A
site 1B536   ; OUT ($BF),A
site 1B53B   ; OUT ($BF),A
site 1B542   ; OUT ($BE),A
site 1B547   ; OUT ($BE),A
site 1B54E   ; OUT ($BE),A
site 1B553   ; OUT ($BE),A
site 1B55A   ; OUT ($BE),A
site 1B561   ; OUT ($BF),A
site 1B566   ; OUT ($BF),A
site 1B56D   ; OUT ($BE),A
site 1B572   ; OUT ($BE),A
site 1B579   ; OUT ($BE),A
site 1B57E   ; OUT ($BE),A
site 1B585   ; OUT ($BE),A
site 1B890   ; IN A,($BF)
site 1B89F   ; OUT ($BF),A
site 1B8A2   ; OUT ($BF),A
site 1B8A9   ; OUT ($BE),A
site 1B8AB   ; IN A,($BF)
site 1B8B4   ; OUT ($BF),A
site 1B8B8   ; OUT ($BF),A
site 1B8C0   ; OTIR
site 1B8C2   ; OTIR
site 1B8C4   ; OTIR
site 1B8C6   ; OTIR
site 1B8C8   ; OTIR
site 1B8CA   ; OTIR
site 1B8CC   ; OTIR
site 1B8CE   ; OTIR
site 1B8D0   ; OTIR
site 1B8E9   ; OTIR
site 1B901   ; OTIR
site 1B91B   ; OTIR
site 1B922   ; OTIR
site 1B929   ; OTIR
site 1B946   ; IN A,(C)
site 1B94C   ; OUT (C),B
site 1B94E   ; OUT (C),A
site 1B958   ; OTIR
site 1B95A   ; OTIR
site 1C0B5   ; OUT ($7F),A
site 1C0B9   ; OUT ($7F),A
site 1C0BD   ; OUT ($7F),A
site 1C0C1   ; OUT ($7F),A
site 1C3E2   ; OUT ($7F),A
site 1C429   ; OUT ($7F),A
site 1C44C   ; OUT ($7F),A
site 1C450   ; OUT ($7F),A
site 1C454   ; OUT ($7F),A
site 1C458   ; OUT ($7F),A
site 1C4F9   ; OUT ($7F),A
site 1C4FF   ; OUT ($7F),A
site 1C504   ; OUT ($7F),A
site 1C542   ; OUT ($7F),A
site 1C547   ; OUT ($7F),A
site 1C733   ; OUT ($7F),A
site 1C760   ; OUT ($7F),A
site 1C8B0   ; OUT ($7F),A
site 1C8BB   ; OUT ($7F),A
site 1C8C9   ; OUT ($7F),A
mapst 0008A   ; LD ($FFFC),A
mapst 0008D   ; LD ($FFFD),A
mapst 00092   ; LD ($FFFE),A
mapst 00097   ; LD ($FFFF),A
mapst 00140   ; LD ($FFFF),A
mapst 00222   ; LD ($FFFE),A
mapst 00255   ; LD ($FFFE),A
mapst 0025C   ; LD ($FFFE),A
mapst 002D1   ; LD ($FFFE),A
mapst 0032F   ; LD ($FFFE),A
mapst 003C6   ; LD ($FFFE),A
mapst 003CB   ; LD ($FFFF),A
mapst 004BF   ; LD ($FFFF),A
mapst 004F7   ; LD ($FFFF),A
mapst 0051B   ; LD ($FFFF),A
mapst 00592   ; LD ($FFFF),A
mapst 005D5   ; LD ($FFFE),A
mapst 005DA   ; LD ($FFFF),A
mapst 00747   ; LD ($FFFF),A
mapst 00775   ; LD ($FFFF),A
mapst 00844   ; LD ($FFFF),A
mapst 00DFF   ; LD ($FFFE),A
mapst 00F08   ; LD ($FFFE),A
mapst 00F3A   ; LD ($FFFE),A
mapst 0101D   ; LD ($FFFE),A
mapst 0106C   ; LD ($FFFE),A
mapst 010BE   ; LD ($FFFE),A
mapst 011A8   ; LD ($FFFF),A
mapst 011CA   ; LD ($FFFF),A
mapst 0121E   ; LD ($FFFE),A
mapst 012A8   ; LD ($FFFF),A
mapst 012B7   ; LD ($FFFF),A
mapst 012C6   ; LD ($FFFF),A
mapst 01301   ; LD ($FFFF),A
mapst 01310   ; LD ($FFFF),A
mapst 0131F   ; LD ($FFFF),A
mapst 01353   ; LD ($FFFF),A
mapst 01399   ; LD ($FFFF),A
mapst 013C9   ; LD ($FFFF),A
mapst 013FC   ; LD ($FFFF),A
mapst 01438   ; LD ($FFFE),A
mapst 0143D   ; LD ($FFFF),A
mapst 01458   ; LD ($FFFF),A
mapst 014B5   ; LD ($FFFF),A
mapst 01510   ; LD ($FFFF),A
mapst 0164F   ; LD ($FFFF),A
mapst 0169A   ; LD ($FFFF),A
mapst 016C1   ; LD ($FFFF),A
mapst 016DF   ; LD ($FFFF),A
mapst 0171E   ; LD ($FFFE),A
mapst 01723   ; LD ($FFFF),A
mapst 01751   ; LD ($FFFE),A
mapst 017E8   ; LD ($FFFF),A
mapst 018ED   ; LD ($FFFF),A
mapst 01929   ; LD ($FFFF),A
mapst 01964   ; LD ($FFFF),A
mapst 01B1E   ; LD ($FFFF),A
mapst 01B53   ; LD ($FFFF),A
mapst 01BF0   ; LD ($FFFF),A
mapst 01C27   ; LD ($FFFE),A
mapst 01DC6   ; LD ($FFFF),A
mapst 01DF6   ; LD ($FFFF),A
mapst 0220A   ; LD ($FFFF),A
mapst 02214   ; LD ($FFFF),A
mapst 02250   ; LD ($FFFE),A
mapst 022C3   ; LD ($FFFE),A
mapst 023A7   ; LD ($FFFE),A
mapst 02434   ; LD ($FFFF),A
mapst 02494   ; LD ($FFFF),A
mapst 0256A   ; LD ($FFFE),A
mapst 0261E   ; LD ($FFFF),A
mapst 02780   ; LD ($FFFE),A
mapst 027AF   ; LD ($FFFE),A
mapst 027CE   ; LD ($FFFE),A
mapst 02843   ; LD ($FFFE),A
mapst 02884   ; LD ($FFFE),A
mapst 02944   ; LD ($FFFE),A
mapst 029AB   ; LD ($FFFE),A
mapst 02A0F   ; LD ($FFFE),A
mapst 02A3F   ; LD ($FFFE),A
mapst 02AD7   ; LD ($FFFE),A
mapst 02AFA   ; LD ($FFFE),A
mapst 02B17   ; LD ($FFFF),A
mapst 02BBC   ; LD ($FFFE),A
mapst 02C07   ; LD ($FFFE),A
mapst 02C38   ; LD ($FFFE),A
mapst 02C43   ; LD ($FFFE),A
mapst 02C96   ; LD ($FFFE),A
mapst 02CD1   ; LD ($FFFE),A
mapst 02E2B   ; LD ($FFFE),A
mapst 02E38   ; LD ($FFFE),A
mapst 02E4A   ; LD ($FFFE),A
mapst 02E59   ; LD ($FFFE),A
mapst 02E75   ; LD ($FFFE),A
mapst 02E94   ; LD ($FFFE),A
mapst 02EED   ; LD ($FFFE),A
mapst 02F1B   ; LD ($FFFE),A
mapst 02F6B   ; LD ($FFFE),A
mapst 02F79   ; LD ($FFFE),A
mapst 02FB7   ; LD ($FFFE),A
mapst 03025   ; LD ($FFFF),A
mapst 03091   ; LD ($FFFE),A
mapst 030A0   ; LD ($FFFE),A
mapst 030AF   ; LD ($FFFE),A
mapst 030DB   ; LD ($FFFE),A
mapst 0311C   ; LD ($FFFE),A
mapst 03158   ; LD ($FFFF),A
mapst 03189   ; LD ($FFFE),A
mapst 031AC   ; LD ($FFFE),A
mapst 031BE   ; LD ($FFFE),A
mapst 031C9   ; LD ($FFFE),A
mapst 031D1   ; LD ($FFFE),A
mapst 031D9   ; LD ($FFFE),A
mapst 031E1   ; LD ($FFFF),A
mapst 032AE   ; LD ($FFFF),A
mapst 033BA   ; LD ($FFFF),A
mapst 03418   ; LD ($FFFF),A
mapst 03640   ; LD ($FFFE),A
mapst 036F0   ; LD ($FFFE),A
mapst 036F5   ; LD ($FFFF),A
mapst 03723   ; LD ($FFFE),A
mapst 03728   ; LD ($FFFF),A
mapst 03741   ; LD ($FFFF),A
mapst 03758   ; LD ($FFFF),A
mapst 03765   ; LD ($FFFF),A
mapst 03775   ; LD ($FFFF),A
mapst 037C2   ; LD ($FFFE),A
mapst 037F2   ; LD ($FFFE),A
mapst 03806   ; LD ($FFFE),A
mapst 03A15   ; LD ($FFFE),A
mapst 03B1E   ; LD ($FFFE),A
mapst 03B99   ; LD ($FFFF),A
mapst 03BC2   ; LD ($FFFF),A
mapst 03BEB   ; LD ($FFFF),A
mapst 03C10   ; LD ($FFFF),A
mapst 03E7B   ; LD ($FFFF),A
mapst 03F7C   ; LD ($FFFE),A
mapst 04002   ; LD ($FFFF),A
mapst 0596E   ; LD ($FFFF),A
mapst 05976   ; LD ($FFFF),A
mapst 0597C   ; LD ($FFFF),A
mapst 05984   ; LD ($FFFF),A
mapst 0598C   ; LD ($FFFF),A
mapst 05992   ; LD ($FFFF),A
mapst 0698E   ; LD ($FFFF),A
mapst 06994   ; LD ($FFFF),A
mapst 0A824   ; LD ($FFFE),A
mapst 0A834   ; LD ($FFFE),A
mapst 0B2F7   ; LD ($FFFE),A
mapst 0B2FD   ; LD ($FFFE),A
mapst 0B318   ; LD ($FFFE),A
mapst 1002F   ; LD ($FFFE),A
mapst 10034   ; LD ($FFFF),A
mapst 100F6   ; LD ($FFFF),A
mapst 10110   ; LD ($FFFF),A
mapst 10143   ; LD ($FFFF),A
mapst 10157   ; LD ($FFFF),A
mapst 1022B   ; LD ($FFFF),A
mapst 1027A   ; LD ($FFFF),A
mapst 103EF   ; LD ($FFFF),A
mapst 10813   ; LD ($FFFF),A
mapst 10870   ; LD ($FFFF),A
mapst 108CF   ; LD ($FFFF),A
mapst 10904   ; LD ($FFFF),A
mapst 10921   ; LD ($FFFF),A
mapst 10989   ; LD ($FFFF),A
mapst 109DE   ; LD ($FFFF),A
mapst 10A75   ; LD ($FFFF),A
mapst 10AE1   ; LD ($FFFF),A
mapst 10F0A   ; LD ($FFFF),A
mapst 11224   ; LD ($FFFF),A
mapst 11F62   ; LD ($FFFF),A
mapst 11FBA   ; LD ($FFFF),A
mapst 120D7   ; LD ($FFFF),A
mapst 1232F   ; LD ($FFFF),A
mapst 12460   ; LD ($FFFF),A
mapst 124FB   ; LD ($FFFF),A
mapst 12AB8   ; LD ($FFFF),A
mapst 12B82   ; LD ($FFFF),A
mapst 130A1   ; LD ($FFFF),A
mapst 13137   ; LD ($FFFF),A
mapst 13188   ; LD ($FFFF),A
mapst 13336   ; LD ($FFFF),A
mapst 1AEEB   ; LD ($FFFF),A
mapst 1AF1B   ; LD ($FFFF),A
mapst 1AF6A   ; LD ($FFFF),A
mapst 1AFC3   ; LD ($FFFF),A
mapst 1B16A   ; LD ($FFFE),A
mapst 1B190   ; LD ($FFFE),A
mapst 1B1A9   ; LD ($FFFE),A
mapst 1B1C1   ; LD ($FFFE),A
mapst 1B485   ; LD ($FFFE),A
mapst 1B730   ; LD ($FFFE),A
mapst 1B8AF   ; LD ($FFFE),A
mapst 1B92D   ; LD ($FFFE),A
mapst 021FA   # LD ($FFFF),A; after LD A,$03; 32 bytes of valid code before it
mapst 02204   # LD ($FFFF),A; after LD A,$02; JP/CALL target from $3087C; 32 bytes of valid code before it
mapst 026F2   # LD ($FFFE),A; after LD A,$01; 32 bytes of valid code before it
mapst 037B0   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
mapst 0B659   # LD ($FFFE),A; after LD A,$04; 32 bytes of valid code before it
mapst 0B664   # LD ($FFFE),A; after LD A,$01; 32 bytes of valid code before it

# Sagaia (Europe, Brazil).cht, "Infinite Lives": RAM $C826 is the lives count shown in
# the status bar; held at 9, the count stays at 9 through deaths
poke "Infinite lives"
ar 00C8-2609
endpoke

# Sagaia (Europe, Brazil).cht, "Invulnerability": RAM $C803 is the ship's hit state;
# held at $20, enemies and shots do not destroy the ship
poke "Invulnerability"
ar 00C8-0320
endpoke

# Sagaia (Europe, Brazil).cht, "Infinite Credits": RAM $C03F is the number of credits;
# held at 9, a continue no longer lowers it
poke "Infinite credits"
ar 00C0-3F09
endpoke
