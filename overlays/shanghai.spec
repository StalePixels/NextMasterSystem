# Shanghai (USA, Europe), CRC32 AAB67EC3, 128K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log, then decided by hand.
#
# Decisions:
# - io vector $18: $0012-$0037 is $00 filler that no code runs or reads, and the game uses
#   no RST but $38. ($08 and $10 fall inside the reset code at $0000-$0011.)
# - The VDP command queue: $3480 puts a handler address and its arguments into a ring at
#   $C092-$C0C3, and $33E2 (from the interrupt handler) runs each handler through the JP (HL)
#   at $340E. The handlers are $34BC, $34D5 and the OUTI ladder at $34F6-$3597, which the
#   callers name with LD DE,$34BC / $34D5 / $354D; the reference log runs them. Every I/O
#   instruction in them is patched.
# - Port $F0-$F2 (FM): $2E4A tests for the FM unit by writing $F2 and reading it back. The read
#   gives no match, so the game takes its PSG path, as on a Master System with no FM unit.
# - The pointer harvest takes the data pointers $367E and $375F (stored into $C24D, read as
#   bytes at $3621), $781F (stored into $C022, the source of the OUTI copy at $3226) and
#   $6FA0 for code; the RST $38 and stores decoded from them are data and get no patch.
# - $379E-$37AC (write the word HL at VRAM address DE) is named by no call, jump, address load
#   or table anywhere in the cart and was not run in the reference log: unused.
# - Bank 5 holds the sound driver. Banks 2, 3, 4, 6 and 7 hold no code: the scanner reaches
#   bank 4 only through $8011 and $8014, data pointers that $6E87 reads bits from, so the
#   stores it decodes there are data. The byte patterns in banks 3 and 6 are data.
name Shanghai
cart AAB67EC3
hz any		; No-Intro regions USA, Europe
vector 18 io
asm 02D5C 2   ; IM 1 -> IM 2
    im 2
endasm
site 02128   ; OUT ($BF),A
site 0212B   ; OUT ($BF),A
site 0213B   ; OUT ($BE),A
site 02142   ; OUT ($BE),A
site 02149   ; OUT ($BE),A
site 02150   ; OUT ($BE),A
site 02168   ; OUT ($BF),A
site 0216B   ; OUT ($BF),A
site 02172   ; OUTI
site 02237   ; OUT ($BE),A
site 02242   ; OUT ($BE),A
site 02275   ; OUT ($BE),A
site 02285   ; OUT ($BE),A
site 023B3   ; OUT ($BE),A
site 023BB   ; OUT ($BE),A
site 023CD   ; OUT ($BE),A
site 023D5   ; OUT ($BE),A
site 02682   ; OUT ($BE),A
site 0268A   ; OUT ($BE),A
site 0269C   ; OUT ($BE),A
site 026A4   ; OUT ($BE),A
site 026FF   ; OUT ($BE),A
site 02707   ; OUT ($BE),A
site 02719   ; OUT ($BE),A
site 02721   ; OUT ($BE),A
site 0275F   ; OUT ($BF),A
site 02763   ; OUT ($BF),A
site 0276D   ; OUT ($BE),A
site 0287E   ; OUT ($BF),A
site 02883   ; OUT ($BF),A
site 02897   ; OUT ($BE),A
site 0289D   ; OUT ($BE),A
site 028A3   ; OUT ($BE),A
site 028A9   ; OUT ($BE),A
site 02A35   ; OUT ($BF),A
site 02A38   ; OUT ($BF),A
site 02A50   ; OUT ($BE),A
site 02A58   ; OUT ($BE),A
site 02A60   ; OUT ($BE),A
site 02A66   ; OUT ($BE),A
site 02D6E   ; OUT ($3F),A
site 02DE0   ; OUT ($3F),A
site 02DE2   ; IN A,($DD)
site 02DEC   ; OUT ($3F),A
site 02DEE   ; IN A,($DD)
site 02E06   ; IN A,($BF)
site 02E0C   ; IN A,($BF)
site 02E13   ; IN A,($BF)
site 02E42   ; OUT ($3E),A
site 02E4A   ; OUT ($F2),A
site 02E4D   ; IN A,($F2)
site 02E5F   ; OUT ($F2),A
site 02E67   ; OUT ($3E),A
site 02E77   ; OUT ($F2),A
site 02E79   ; IN A,($F2)
site 0303E   ; OUT ($BF),A
site 03042   ; OUT ($BF),A
site 03078   ; IN A,($BF)
site 03086   ; IN A,($DD)
site 0309D   ; OUT ($BF),A
site 030A1   ; OUT ($BF),A
site 030AF   ; OUT ($BF),A
site 030B3   ; OUT ($BF),A
site 030DA   ; OUT ($BF),A
site 030DE   ; OUT ($BF),A
site 0318E   ; OUT ($BF),A
site 03192   ; OUT ($BF),A
site 031D4   ; OUT ($BF),A
site 031D8   ; OUT ($BF),A
site 031E5   ; OUT (C),A
site 031E7   ; OUT (C),A
site 031E9   ; OUT (C),A
site 031EB   ; OUT (C),A
site 031ED   ; OUT (C),A
site 031EF   ; OUT (C),A
site 031F1   ; OUT (C),A
site 031F3   ; OUT (C),A
site 031F5   ; OUT (C),A
site 031F7   ; OUT (C),A
site 031F9   ; OUT (C),A
site 031FB   ; OUT (C),A
site 031FD   ; OUT (C),A
site 031FF   ; OUT (C),A
site 03201   ; OUT (C),A
site 03203   ; OUT (C),A
site 03205   ; OUT (C),A
site 03207   ; OUT (C),A
site 03209   ; OUT (C),A
site 0320B   ; OUT (C),A
site 0320D   ; OUT (C),A
site 0320F   ; OUT (C),A
site 03211   ; OUT (C),A
site 03213   ; OUT (C),A
site 03215   ; OUT (C),A
site 03217   ; OUT (C),A
site 03219   ; OUT (C),A
site 0321B   ; OUT (C),A
site 0321D   ; OUT (C),A
site 0321F   ; OUT (C),A
site 03221   ; OUT (C),A
site 03223   ; OUT (C),A
site 03226   ; OUTI
site 03228   ; OUTI
site 0322A   ; OUTI
site 0322C   ; OUTI
site 0322E   ; OUTI
site 03230   ; OUTI
site 03232   ; OUTI
site 03234   ; OUTI
site 03236   ; OUTI
site 03238   ; OUTI
site 0323A   ; OUTI
site 0323C   ; OUTI
site 0323E   ; OUTI
site 03240   ; OUTI
site 03242   ; OUTI
site 03244   ; OUTI
site 03246   ; OUTI
site 03248   ; OUTI
site 0324A   ; OUTI
site 0324C   ; OUTI
site 0324E   ; OUTI
site 03250   ; OUTI
site 03252   ; OUTI
site 03254   ; OUTI
site 03256   ; OUTI
site 03258   ; OUTI
site 0325A   ; OUTI
site 0325C   ; OUTI
site 0325E   ; OUTI
site 03260   ; OUTI
site 03262   ; OUTI
site 03264   ; OUTI
site 03281   ; IN A,($DC)
site 032A1   ; IN A,($DC)
site 032A4   ; IN A,($DD)
site 0335B   ; OUT ($BF),A
site 0335F   ; OUT ($BF),A
site 03365   ; OUTI
site 03367   ; OUTI
site 03369   ; OUTI
site 0336B   ; OUTI
site 0336D   ; OUTI
site 0336F   ; OUTI
site 03371   ; OUTI
site 03373   ; OUTI
site 03375   ; OUTI
site 03377   ; OUTI
site 03379   ; OUTI
site 0337B   ; OUTI
site 0337D   ; OUTI
site 0337F   ; OUTI
site 03381   ; OUTI
site 03383   ; OUTI
site 03385   ; OUTI
site 03387   ; OUTI
site 03389   ; OUTI
site 0338B   ; OUTI
site 0338D   ; OUTI
site 0338F   ; OUTI
site 03391   ; OUTI
site 03393   ; OUTI
site 03395   ; OUTI
site 03397   ; OUTI
site 03399   ; OUTI
site 0339B   ; OUTI
site 0339D   ; OUTI
site 0339F   ; OUTI
site 033A1   ; OUTI
site 033A3   ; OUTI
site 033B7   ; OUT ($BF),A
site 033BB   ; OUT ($BF),A
site 033C4   ; OUTI
site 034C5   ; OUTI
site 034C7   ; OUTI
site 034CC   ; OTIR
site 034D9   ; OUT ($BF),A
site 034DD   ; OUT ($BF),A
site 034E8   ; OUT ($BE),A
site 034EA   ; OUTI
site 034ED   ; OUT ($BE),A
site 034F0   ; OUT ($BE),A
site 034FD   ; OUTI
site 034FF   ; OUTI
site 03509   ; OUTI
site 0350B   ; OUTI
site 03515   ; OUTI
site 03517   ; OUTI
site 03521   ; OUTI
site 03523   ; OUTI
site 0352D   ; OUTI
site 0352F   ; OUTI
site 03539   ; OUTI
site 0353B   ; OUTI
site 03545   ; OUTI
site 03547   ; OUTI
site 03551   ; OUTI
site 03553   ; OUTI
site 03556   ; OUTI
site 03558   ; OUTI
site 0355A   ; OUTI
site 0355C   ; OUTI
site 0355E   ; OUTI
site 03560   ; OUTI
site 03562   ; OUTI
site 03564   ; OUTI
site 03566   ; OUTI
site 03568   ; OUTI
site 0356A   ; OUTI
site 0356C   ; OUTI
site 0356E   ; OUTI
site 03570   ; OUTI
site 03572   ; OUTI
site 03574   ; OUTI
site 03576   ; OUTI
site 03578   ; OUTI
site 0357A   ; OUTI
site 0357C   ; OUTI
site 0357E   ; OUTI
site 03580   ; OUTI
site 03582   ; OUTI
site 03584   ; OUTI
site 03586   ; OUTI
site 03588   ; OUTI
site 0358A   ; OUTI
site 0358C   ; OUTI
site 0358E   ; OUTI
site 03590   ; OUTI
site 03592   ; OUTI
site 03594   ; OUTI
site 036F1   ; OUTI
site 03798   ; OUT ($BF),A
site 0379B   ; OUT ($BF),A
site 037B1   ; OUT ($BF),A
site 037B4   ; OUT ($BF),A
site 037B7   ; OUT ($BE),A
site 037BE   ; OUT ($BE),A
site 037CE   ; OUT ($BE),A
site 037E5   ; OUT ($BE),A
site 037EA   ; OUT ($BE),A
site 037F8   ; OUTI
site 0380E   ; OUT ($BE),A
site 03813   ; OUT ($BE),A
site 03818   ; OUT ($BE),A
site 0381D   ; OUT ($BE),A
site 03822   ; OUT ($BE),A
site 03827   ; OUT ($BE),A
site 0382C   ; OUT ($BE),A
site 03831   ; OUT ($BE),A
site 0383D   ; OUT ($BF),A
site 03844   ; OUT ($BF),A
site 0384C   ; OUT ($BF),A
site 03850   ; OUT ($BF),A
site 03854   ; OUT ($BE),A
site 03859   ; OUT ($BF),A
site 0385D   ; OUT ($BF),A
site 03861   ; OUT ($BE),A
site 038CE   ; OUT ($BE),A
site 038E2   ; OUT ($BE),A
site 038E7   ; OUT ($BE),A
site 038EE   ; OUT ($BE),A
site 038F5   ; OUT ($BE),A
site 03904   ; OUT ($BE),A
site 03909   ; OUT ($BE),A
site 03921   ; OUT ($BE),A
site 03927   ; OUT ($BE),A
site 03978   ; OUT ($BE),A
site 0397C   ; IN A,($BE)
site 03980   ; IN A,($BE)
site 03984   ; IN A,($BE)
site 0398E   ; OUT ($BE),A
site 03992   ; IN A,($BE)
site 03996   ; IN A,($BE)
site 0399A   ; IN A,($BE)
site 039B0   ; OUT ($BE),A
site 039B6   ; OUT ($BE),A
site 03A6E   ; OUT ($BF),A
site 03A72   ; OUT ($BF),A
site 03A76   ; OUT ($BE),A
site 03B1A   ; OUT ($BF),A
site 03B1E   ; OUT ($BF),A
site 03B21   ; OUT ($BE),A
site 03B25   ; OUT ($BE),A
site 03B2D   ; OUT ($BE),A
site 03B31   ; OUT ($BF),A
site 03B35   ; OUT ($BF),A
site 03B38   ; OUT ($BE),A
site 03B40   ; OUT ($BE),A
site 03B47   ; OUT ($BE),A
site 03B4F   ; OUT ($BE),A
site 03B5B   ; OUT ($BF),A
site 03B5F   ; OUT ($BF),A
site 03B6B   ; OTIR
site 03B73   ; OUT ($BF),A
site 03B76   ; OUT ($BF),A
site 03B7B   ; OTIR
site 053D3   ; OUT ($BF),A
site 053D6   ; OUT ($BF),A
site 053DD   ; INI
site 06EAD   ; OUT ($BF),A
site 06EB2   ; OUT ($BF),A
site 06EB6   ; OUT ($BE),A
site 06EBC   ; OUT ($BE),A
site 06EC2   ; OUT ($BE),A
site 06EC8   ; OUT ($BE),A
site 06F68   ; OUT ($BE),A
site 06F6F   ; OUT ($BE),A
site 06F79   ; OUT ($BE),A
site 06F7F   ; OUT ($BE),A
site 0728A   ; OUT ($BF),A
site 0728E   ; OUT ($BF),A
site 07293   ; OUT ($BE),A
site 0729B   ; OUT ($BE),A
site 072AC   ; OUT ($BE),A
site 072B4   ; OUT ($BE),A
site 0769E   ; OUT ($BF),A
site 076A2   ; OUT ($BF),A
site 07742   ; OUT ($BF),A
site 07745   ; OUT ($BF),A
site 0774B   ; IN A,($BE)
site 07751   ; IN A,($BE)
site 07757   ; IN A,($BE)
site 0775D   ; IN A,($BE)
site 07765   ; OUT ($BF),A
site 0776A   ; OUT ($BF),A
site 0776E   ; OUT ($BE),A
site 07774   ; OUT ($BE),A
site 0777A   ; OUT ($BE),A
site 07780   ; OUT ($BE),A
site 1412D   ; OUT ($F0),A
site 14136   ; OUT ($F1),A
site 1414E   ; OUT ($7F),A
site 1415E   ; OUT (C),D
site 14164   ; OUT ($F1),A
site 14197   ; OTIR
site 141A5   ; OTIR
site 141AF   ; OUT ($F0),A
site 141B5   ; OUT ($F1),A
site 141C1   ; OUTI
site 141C7   ; OUTI
site 1434C   ; OUT ($7F),A
site 14350   ; OUT ($7F),A
site 14378   ; OUT ($7F),A
site 1437C   ; OUT ($7F),A
site 1437F   ; OUT ($7F),A
site 143E5   ; OUT ($F0),A
site 143EC   ; OUT ($F1),A
site 143F4   ; OUT ($F0),A
site 143FA   ; OUT ($F1),A
site 144EF   ; OUT ($F0),A
site 144F9   ; OUT (C),L
site 14502   ; OUT ($F0),A
site 1451D   ; OUT (C),H
site 14525   ; OUT ($F0),A
site 14533   ; OUT ($F1),A
site 1453F   ; OUT ($F0),A
site 14548   ; OUT ($F1),A
site 14709   ; OUT ($F0),A
site 14712   ; OUT (C),A
site 14717   ; OUT ($F0),A
site 1471D   ; OUTI
site 1478E   ; OUT ($7F),A
site 14856   ; OUT ($7F),A
site 1487D   ; OUT ($7F),A
site 14882   ; OUT ($7F),A
site 148AE   ; OUT ($F0),A
site 148BC   ; OUT ($F1),A
site 148CD   ; OUT ($F0),A
site 14961   ; OUTI
site 14963   ; OUTI
site 14965   ; OUTI
site 14967   ; OUTI
site 14969   ; OUTI
site 1496B   ; OUTI
site 1496D   ; OUTI
site 1496F   ; OUTI
site 14971   ; OUTI
site 14973   ; OUTI
site 14975   ; OUTI
site 1497F   ; OUT (C),D
site 14985   ; OUT ($F1),A
site 149C4   ; OUT ($7F),A
site 14A1A   ; OUT ($7F),A
site 14A59   ; OUT ($7F),A
site 14ABB   ; OUT ($7F),A
site 14ADB   ; OUT ($7F),A
site 14B1B   ; OUT ($7F),A
site 14B25   ; OUT ($7F),A
site 14B6D   ; OUT ($7F),A
mapldk 00001   # LD HL,$FFFC; LD (HL),$00
maphl 00007   # LD (HL),$00, HL = $FFFD
maphl 0000A   # LD (HL),$01, HL = $FFFE
maphl 0000D   # LD (HL),$02, HL = $FFFF
mapst 00080   ; LD ($FFFF),A
mapst 00087   ; LD ($FFFC),A
mapst 0008D   ; LD ($FFFC),A
mapldk 02D5E   # LD HL,$FFFC; LD (HL),$00
maphl 02D64   # LD (HL),$00, HL = $FFFD
maphl 02D67   # LD (HL),$01, HL = $FFFE
maphl 02D6A   # LD (HL),$02, HL = $FFFF
