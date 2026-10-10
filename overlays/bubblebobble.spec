# Bubble Bobble, drafted by tools/mkspec.py from sitescan output.
name Bubble Bobble
cart E843BA7E
hz 50		; No-Intro regions Europe, Brazil
# No free RST vector: the JP at $0000 becomes the vector, the game
# starts at its target.
vector 00 io
start 00C6
asm 0011F 2   ; IM 1 -> IM 2
    im 2
endasm
site 000EA   ; OUT ($3E),A
site 00105   ; OUT ($BE),A
site 0017A   ; IN A,($BF)
site 0029D   ; OUT ($BE),A
site 002B0   ; OUT ($BE),A
site 002CD   ; OUT ($BE),A
site 002DF   ; OUT ($BE),A
site 0031C   ; OUT ($BE),A
site 00320   ; OUT ($BE),A
site 00324   ; OUT ($BE),A
site 00329   ; OUT ($BE),A
site 0040A   ; OUT ($BF),A
site 0040F   ; OUT ($BF),A
site 00417   ; OUT ($BF),A
site 0041E   ; OUT ($BF),A
site 00423   ; OUT ($BF),A
site 00428   ; OUT ($BF),A
site 00445   ; OUT ($BE),A
site 00467   ; OUT ($BE),A
site 00476   ; OUT ($BE),A
site 00485   ; OUT ($BE),A
site 004F9   ; OUT ($BE),A
site 004FF   ; OUT ($BE),A
site 005FA   ; OUT ($BE),A
site 00601   ; OUT ($BE),A
site 00626   ; OUT ($BE),A
site 0062D   ; OUT ($BE),A
site 00657   ; OUT ($DE),A
site 00659   ; IN A,($DC)
site 00660   ; IN A,($DD)
site 0066F   ; OUT ($DE),A
site 00671   ; IN A,($DC)
site 0067F   ; IN A,($DD)
site 007A4   ; OUT ($BE),A
site 007AA   ; OUT ($BE),A
site 007C1   ; OUT ($BE),A
site 007C7   ; OUT ($BE),A
site 0087D   ; OUT ($BE),A
site 00883   ; OUT ($BE),A
site 00896   ; OUT ($BE),A
site 0089C   ; OUT ($BE),A
site 008B3   ; OUT ($BE),A
site 008B9   ; OUT ($BE),A
site 008CC   ; OUT ($BE),A
site 008D2   ; OUT ($BE),A
site 008E9   ; OUT ($BE),A
site 008EF   ; OUT ($BE),A
site 00902   ; OUT ($BE),A
site 00908   ; OUT ($BE),A
site 0094A   ; OUT ($BE),A
site 00950   ; OUT ($BE),A
site 0095C   ; OUT ($BE),A
site 00962   ; OUT ($BE),A
site 00988   ; OUT ($BE),A
site 0098E   ; OUT ($BE),A
site 00999   ; OUT ($BE),A
site 0099F   ; OUT ($BE),A
site 00CB3   ; OUT ($BF),A
site 00CBA   ; OUT ($BF),A
site 00CBF   ; OUT ($BE),A
site 00CCF   ; OUT ($BE),A
site 00D45   ; OUT ($BF),A
site 00D4C   ; OUT ($BF),A
site 00D51   ; OUT ($BE),A
site 00DD7   ; OUT ($BF),A
site 00DDE   ; OUT ($BF),A
site 00DE3   ; OUT ($BE),A
site 00E66   ; OUT ($BF),A
site 00E6D   ; OUT ($BF),A
site 00E72   ; OUT ($BE),A
site 00EC2   ; OUT ($BF),A
site 00EC9   ; OUT ($BF),A
site 00ECE   ; OUT ($BE),A
site 00F55   ; OUT ($BF),A
site 00F5C   ; OUT ($BF),A
site 00F61   ; OUT ($BE),A
site 00FAF   ; OUT ($BF),A
site 00FB6   ; OUT ($BF),A
site 00FBB   ; OUT ($BE),A
site 010BA   ; OUT ($BF),A
site 010C1   ; OUT ($BF),A
site 010C6   ; OUT ($BE),A
site 0114C   ; OUT ($BF),A
site 01153   ; OUT ($BF),A
site 01158   ; OUT ($BE),A
site 011DB   ; OUT ($BF),A
site 011E2   ; OUT ($BF),A
site 011E7   ; OUT ($BE),A
site 01237   ; OUT ($BF),A
site 0123E   ; OUT ($BF),A
site 01243   ; OUT ($BE),A
site 012CA   ; OUT ($BF),A
site 012D1   ; OUT ($BF),A
site 012D6   ; OUT ($BE),A
site 01324   ; OUT ($BF),A
site 0132B   ; OUT ($BF),A
site 01330   ; OUT ($BE),A
site 02638   ; OUT ($BE),A
site 0263E   ; OUT ($BE),A
site 02B8F   ; OUT ($BE),A
site 02B94   ; OUT ($BE),A
site 02B98   ; OUT ($BE),A
site 02B9D   ; OUT ($BE),A
site 02DB2   ; OUT ($BE),A
site 02DB7   ; OUT ($BE),A
site 02DBE   ; OUT ($BE),A
site 02DC3   ; OUT ($BE),A
site 02DCF   ; OUT ($BE),A
site 02DD4   ; OUT ($BE),A
site 02DDB   ; OUT ($BE),A
site 02DE0   ; OUT ($BE),A
site 02DED   ; OUT ($BE),A
site 02DF3   ; OUT ($BE),A
site 02DF8   ; OUT ($BE),A
site 02DFE   ; OUT ($BE),A
site 02E09   ; OUT ($BE),A
site 02E0F   ; OUT ($BE),A
site 02E14   ; OUT ($BE),A
site 02E1A   ; OUT ($BE),A
site 02E9C   ; OUT ($BF),A
site 02EA3   ; OUT ($BF),A
site 02EA8   ; OUT ($BE),A
site 030E0   ; OUT ($BF),A
site 030E7   ; OUT ($BF),A
site 030EC   ; OUT ($BE),A
site 033E0   ; OUT ($BE),A
site 035A4   ; OUT ($BF),A
site 035AB   ; OUT ($BF),A
site 035B0   ; OUT ($BE),A
site 0362A   ; OUT ($BF),A
site 03631   ; OUT ($BF),A
site 03636   ; OUT ($BE),A
site 03857   ; OUT ($BF),A
site 0385E   ; OUT ($BF),A
site 03863   ; OUT ($BE),A
site 03BF4   ; OUT ($BF),A
site 03BFB   ; OUT ($BF),A
site 03C00   ; OUT ($BE),A
site 03C92   ; OUT ($BF),A
site 03C99   ; OUT ($BF),A
site 03CA4   ; OUT ($BE),A
site 03CAA   ; OUT ($BE),A
site 03CB0   ; OUT ($BE),A
site 03CB9   ; OUT ($BE),A
site 03CEE   ; OUT ($BE),A
site 03CF4   ; OUT ($BE),A
site 03CFA   ; OUT ($BE),A
site 03D03   ; OUT ($BE),A
site 03DBF   ; OUT ($BF),A
site 03DC6   ; OUT ($BF),A
site 03DD1   ; OUT ($BE),A
site 03DD6   ; OUT ($BE),A
site 03DDC   ; OUT ($BE),A
site 03DE2   ; OUT ($BE),A
site 03E17   ; OUT ($BE),A
site 03E1C   ; OUT ($BE),A
site 03E22   ; OUT ($BE),A
site 03E28   ; OUT ($BE),A
site 0871E   ; OUT ($BE),A
site 08724   ; OUT ($BE),A
site 08736   ; OUT ($BE),A
site 0873C   ; OUT ($BE),A
site 087CB   ; OUT ($BE),A
site 087D1   ; OUT ($BE),A
site 087D5   ; OUT ($BE),A
site 087DB   ; OUT ($BE),A
site 0A81C   ; OUT ($BE),A
site 0A820   ; OUT ($BE),A
site 0A824   ; OUT ($BE),A
site 0A829   ; OUT ($BE),A
site 0A866   ; OUT ($BE),A
site 0A86A   ; OUT ($BE),A
site 0A86E   ; OUT ($BE),A
site 0A873   ; OUT ($BE),A
site 0AAD2   ; OUT ($BE),A
site 0AAD8   ; OUT ($BE),A
site 0AAE4   ; OUT ($BE),A
site 0AAEA   ; OUT ($BE),A
site 0AAF3   ; OUT ($BE),A
site 0AAF9   ; OUT ($BE),A
site 0AB05   ; OUT ($BE),A
site 0AB0B   ; OUT ($BE),A
site 0AC61   ; OUT ($BE),A
site 0AC67   ; OUT ($BE),A
site 0AC89   ; OUT ($BE),A
site 0AD1B   ; IN A,($BE)
site 0AD1F   ; IN A,($BE)
site 0AD23   ; IN A,($BE)
site 0AD45   ; OUT ($BE),A
site 0AD4A   ; OUT ($BE),A
site 0AD50   ; OUT ($BE),A
site 0ED6B   ; OUT ($BE),A
site 0ED70   ; OUT ($BE),A
site 0ED77   ; OUT ($BE),A
site 0ED7C   ; OUT ($BE),A
site 0ED88   ; OUT ($BE),A
site 0ED8D   ; OUT ($BE),A
site 0ED94   ; OUT ($BE),A
site 0ED99   ; OUT ($BE),A
site 1001E   ; OUT ($7F),A
site 10036   ; OUT ($7F),A
site 1003F   ; OUT ($7F),A
site 1004D   ; OUT ($7F),A
site 10051   ; OUT ($7F),A
site 1DEAA   ; IN A,($BE)
site 1DEB0   ; IN A,($BE)
site 1DEC5   ; OUT ($BE),A
site 1DECB   ; OUT ($BE),A
site 1DF90   ; OUT ($BE),A
site 1DF96   ; OUT ($BE),A
# Bank 0 VDP helpers the 60 s detector run never reached, checked by hand
# (the scanner rated them low: the game starts its tasks by switching stacks and returning,
# so static flow stops there). The other CHECK low lines are not checked.
site 00404   ; IN A,($BF)
site 00432   ; OUT ($BE),A
site 0043A   ; IN A,($BE)
site 00454   ; IN A,($BE)
site 005C1   ; OUT ($BE),A
site 005C8   ; OUT ($BE),A
site 00B86   ; OUT ($BF),A
site 00B8D   ; OUT ($BF),A
site 00B92   ; OUT ($BE),A
site 00BAE   ; OUT ($BF),A
site 00BB5   ; OUT ($BF),A
site 00BBA   ; OUT ($BE),A
# Round change: the playfield scrolls to the next round and these write each new
# name table row. The JR NZ before each first OUT jumps into the operand of
# LD H,$AF, which runs as XOR A.
site 02791   ; OUT ($BE),A
site 02797   ; OUT ($BE),A
site 0285B   ; OUT ($BE),A
site 02861   ; OUT ($BE),A
mapst 000D6   ; LD ($FFFE),A
# CHECK mapper at 0011D ($011D bank 0): LDIR $FFFC-$FFFF
mapst 00123   ; LD ($FFFF),A
mapst 00135   ; LD ($FFFF),A
mapst 00191   ; LD ($FFFF),A
mapst 001F0   ; LD ($FFFF),A
mapst 0021B   ; LD ($FFFF),A
mapst 0030E   ; LD ($FFFF),A
mapst 00CAE   ; LD ($FFFF),A
mapst 00CDA   ; LD ($FFFF),A
mapst 00D40   ; LD ($FFFF),A
mapst 00D5B   ; LD ($FFFF),A
mapst 00DD2   ; LD ($FFFF),A
mapst 00DED   ; LD ($FFFF),A
mapst 00E61   ; LD ($FFFF),A
mapst 00E7B   ; LD ($FFFF),A
mapst 00EBD   ; LD ($FFFF),A
mapst 00ED7   ; LD ($FFFF),A
mapst 00F50   ; LD ($FFFF),A
mapst 00F6C   ; LD ($FFFF),A
mapst 00FA4   ; LD ($FFFF),A
mapst 00FC6   ; LD ($FFFF),A
mapst 01003   ; LD ($FFFF),A
mapst 010B5   ; LD ($FFFF),A
mapst 010D1   ; LD ($FFFF),A
mapst 01147   ; LD ($FFFF),A
mapst 01163   ; LD ($FFFF),A
mapst 011D6   ; LD ($FFFF),A
mapst 011F0   ; LD ($FFFF),A
mapst 01232   ; LD ($FFFF),A
mapst 0124C   ; LD ($FFFF),A
mapst 012C5   ; LD ($FFFF),A
mapst 012E1   ; LD ($FFFF),A
mapst 01319   ; LD ($FFFF),A
mapst 0133B   ; LD ($FFFF),A
mapst 01378   ; LD ($FFFF),A
mapst 026A2   ; LD ($FFFF),A
mapst 02BBF   ; LD ($FFFF),A
mapst 02BC7   ; LD ($FFFF),A
mapst 02EB2   ; LD ($FFFE),A
mapst 02EB7   ; LD ($FFFF),A
mapst 02ED8   ; LD ($FFFF),A
mapst 030F6   ; LD ($FFFE),A
mapst 030FB   ; LD ($FFFF),A
mapst 0311C   ; LD ($FFFF),A
mapst 035BA   ; LD ($FFFE),A
mapst 035BF   ; LD ($FFFF),A
mapst 03640   ; LD ($FFFE),A
mapst 03645   ; LD ($FFFF),A
mapst 0386D   ; LD ($FFFE),A
mapst 03872   ; LD ($FFFF),A
mapst 03C0B   ; LD ($FFFE),A
mapst 03C10   ; LD ($FFFF),A
mapst 03C9D   ; LD ($FFFF),A
mapst 03D0D   ; LD ($FFFF),A
mapst 03DCA   ; LD ($FFFF),A
mapst 03E32   ; LD ($FFFF),A
mapst 08743   ; LD ($FFFE),A
mapst 0A833   ; LD ($FFFE),A
mapst 0A858   ; LD ($FFFE),A
mapst 0A87D   ; LD ($FFFE),A
# CHECK indirect_unresolved at 004CA ($04CA bank 0): RET 
# CHECK indirect_unresolved at 00525 ($0525 bank 0): RET 
# CHECK indirect_unresolved at 02DE3 ($2DE3 bank 0): RET 
# CHECK indirect_unresolved at 02E1D ($2E1D bank 0): RET 
# CHECK indirect_unresolved at 0ACA4 ($ACA4 bank 2): RET 
# CHECK low: site 016BD  IN A,($3E)  (unmapped_read)
# CHECK low: site 016C2  IN A,($3E)  (unmapped_read)
# CHECK low: site 01736  IN A,($3E)  (unmapped_read)
# CHECK low: site 0173B  IN A,($3E)  (unmapped_read)
# CHECK low: site 01796  IN A,($3E)  (unmapped_read)
# CHECK low: site 017E9  IN A,($3E)  (unmapped_read)
# CHECK low: site 0181B  IN A,($7E)  (v_counter)
# CHECK low: site 01874  IN A,($3E)  (unmapped_read)
# CHECK low: site 01886  OUT ($BE),A  (vdp_data)
# CHECK low: site 0189F  OUT ($BE),A  (vdp_data)
# CHECK low: site 018A6  IN A,($3E)  (unmapped_read)
# CHECK low: site 01BB8  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 01CF4  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 02207  IN A,($3E)  (unmapped_read)
# CHECK low: site 0234B  IN A,($3E)  (unmapped_read)
# CHECK low: site 024B3  IN A,($3E)  (unmapped_read)
# CHECK low: site 027C0  IN A,($3E)  (unmapped_read)
# CHECK low: site 02C04  IN A,($7E)  (v_counter)
# CHECK low: site 02C4A  IN A,($7E)  (v_counter)
# CHECK low: site 02C96  IN A,($BE)  (vdp_data)
# CHECK low: site 02D9B  IN A,($C0)  (joypad_a)
# CHECK low: site 03070  IN A,($C0)  (joypad_a)
# CHECK low: site 0309F  IN A,($3E)  (unmapped_read)
# CHECK low: site 03273  IN A,($3E)  (unmapped_read)
# CHECK low: site 03278  IN A,($3E)  (unmapped_read)
# CHECK low: site 03291  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 03319  IN A,($3E)  (unmapped_read)
# CHECK low: site 03332  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0336C  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0340F  OUT ($BE),A  (vdp_data)
# CHECK low: site 03768  OUT ($BF),A  (vdp_control)
# CHECK low: site 0376F  OUT ($BF),A  (vdp_control)
# CHECK low: site 03774  OUT ($BE),A  (vdp_data)
# CHECK low: site 03A63  IN A,($7E)  (v_counter)
# CHECK low: site 03AD8  IN A,($7E)  (v_counter)
# CHECK low: site 03B1C  IN A,($7E)  (v_counter)
# CHECK low: site 03C83  IN A,($3E)  (unmapped_read)
# CHECK low: site 03D3C  OUT ($BF),A  (vdp_control)
# CHECK low: site 03D43  OUT ($BF),A  (vdp_control)
# CHECK low: site 03D4D  OUT ($BE),A  (vdp_data)
# CHECK low: site 03D53  OUT ($BE),A  (vdp_data)
# CHECK low: site 03D59  OUT ($BE),A  (vdp_data)
# CHECK low: site 03D62  OUT ($BE),A  (vdp_data)
# CHECK low: site 03D7B  OUT ($BE),A  (vdp_data)
# CHECK low: site 03D81  OUT ($BE),A  (vdp_data)
# CHECK low: site 03D87  OUT ($BE),A  (vdp_data)
# CHECK low: site 03D90  OUT ($BE),A  (vdp_data)
# CHECK low: site 03DB0  IN A,($3E)  (unmapped_read)
# CHECK low: site 03E61  OUT ($BF),A  (vdp_control)
# CHECK low: site 03E68  OUT ($BF),A  (vdp_control)
# CHECK low: site 03E72  OUT ($BE),A  (vdp_data)
# CHECK low: site 03E77  OUT ($BE),A  (vdp_data)
# CHECK low: site 03E7D  OUT ($BE),A  (vdp_data)
# CHECK low: site 03E83  OUT ($BE),A  (vdp_data)
# CHECK low: site 03E9C  OUT ($BE),A  (vdp_data)
# CHECK low: site 03EA1  OUT ($BE),A  (vdp_data)
# CHECK low: site 03EA7  OUT ($BE),A  (vdp_data)
# CHECK low: site 03EAD  OUT ($BE),A  (vdp_data)
# CHECK low: site 04173  OUT ($BE),A  (vdp_data)
# CHECK low: site 046D6  IN A,($7E)  (v_counter)
# CHECK low: site 0482E  IN A,($BE)  (vdp_data)
# CHECK low: site 04861  OUT ($BE),A  (vdp_data)
# CHECK low: site 04B00  IN A,($3E)  (unmapped_read)
# CHECK low: site 04C1D  IN A,($3E)  (unmapped_read)
# CHECK low: site 04C64  IN A,($3E)  (unmapped_read)
# CHECK low: site 04D4B  OUT ($BE),A  (vdp_data)
# CHECK low: site 04D51  OUT ($BE),A  (vdp_data)
# CHECK low: site 04D71  IN A,($3E)  (unmapped_read)
# CHECK low: site 04D92  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 04DD7  OUT ($BE),A  (vdp_data)
# CHECK low: site 04DDD  OUT ($BE),A  (vdp_data)
# CHECK low: site 04E0F  OUT ($BE),A  (vdp_data)
# CHECK low: site 04E15  OUT ($BE),A  (vdp_data)
# CHECK low: site 04E28  IN A,($3E)  (unmapped_read)
# CHECK low: site 04E35  IN A,($3E)  (unmapped_read)
# CHECK low: site 04EC4  IN A,($3E)  (unmapped_read)
# CHECK low: site 04F0A  IN A,($3E)  (unmapped_read)
# CHECK low: site 04F36  IN A,($3E)  (unmapped_read)
# CHECK low: site 04FFA  IN A,($3E)  (unmapped_read)
# CHECK low: site 0523D  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 05280  IN A,($7E)  (v_counter)
# CHECK low: site 052DF  IN A,($3E)  (unmapped_read)
# CHECK low: site 05301  IN A,($C0)  (joypad_a)
# CHECK low: site 05354  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 05380  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 053F2  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 055A5  IN A,($3E)  (unmapped_read)
# CHECK low: site 0576F  OUT ($BE),A  (vdp_data)
# CHECK low: site 05784  OUT ($BE),A  (vdp_data)
# CHECK low: site 05864  OUT ($DD),A  (no_effect)
# CHECK low: site 058B9  IN A,($3E)  (unmapped_read)
# CHECK low: site 058E9  IN A,($3E)  (unmapped_read)
# CHECK low: site 059DB  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 05D3A  IN A,($3E)  (unmapped_read)
# CHECK low: site 05E2F  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 05F01  OUT ($BE),A  (vdp_data)
# CHECK low: site 05F07  OUT ($BE),A  (vdp_data)
# CHECK low: site 05F0E  OUT ($BE),A  (vdp_data)
# CHECK low: site 05F14  OUT ($BE),A  (vdp_data)
# CHECK low: site 060B6  IN A,($7E)  (v_counter)
# CHECK low: site 06663  OUT ($BE),A  (vdp_data)
# CHECK low: site 06668  OUT ($BE),A  (vdp_data)
# CHECK low: site 06674  OUT ($BE),A  (vdp_data)
# CHECK low: site 06679  OUT ($BE),A  (vdp_data)
# CHECK low: site 0677D  OUT ($BE),A  (vdp_data)
# CHECK low: site 06782  OUT ($BE),A  (vdp_data)
# CHECK low: site 06789  OUT ($BE),A  (vdp_data)
# CHECK low: site 0678E  OUT ($BE),A  (vdp_data)
# CHECK low: site 0679A  OUT ($BE),A  (vdp_data)
# CHECK low: site 0679F  OUT ($BE),A  (vdp_data)
# CHECK low: site 067A6  OUT ($BE),A  (vdp_data)
# CHECK low: site 067AB  OUT ($BE),A  (vdp_data)
# CHECK low: site 07838  IN A,($3E)  (unmapped_read)
# CHECK low: site 078DA  IN A,($3E)  (unmapped_read)
# CHECK low: site 078EA  IN A,($3E)  (unmapped_read)
# CHECK low: site 0799A  IN A,($3E)  (unmapped_read)
# CHECK low: site 07B54  IN A,($3E)  (unmapped_read)
# CHECK low: site 07FBB  IN A,($7E)  (v_counter)
# CHECK low: site 080E0  OUT ($DD),A  (no_effect)
# CHECK low: site 089AF  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 08B84  OUT ($BE),A  (vdp_data)
# CHECK low: site 08B8A  OUT ($BE),A  (vdp_data)
# CHECK low: site 09038  OUT ($DD),A  (no_effect)
# CHECK low: site 091E2  OUT ($BE),A  (vdp_data)
# CHECK low: site 091E7  OUT ($BE),A  (vdp_data)
# CHECK low: site 09284  OUT ($BE),A  (vdp_data)
# CHECK low: site 09289  OUT ($BE),A  (vdp_data)
# CHECK low: site 09881  OUT ($BE),A  (vdp_data)
# CHECK low: site 09887  OUT ($BE),A  (vdp_data)
# CHECK low: site 098BB  OUT ($BE),A  (vdp_data)
# CHECK low: site 098C1  OUT ($BE),A  (vdp_data)
# CHECK low: site 0991A  OUT ($BE),A  (vdp_data)
# CHECK low: site 09920  OUT ($BE),A  (vdp_data)
# CHECK low: site 09931  OUT ($BE),A  (vdp_data)
# CHECK low: site 09937  OUT ($BE),A  (vdp_data)
# CHECK low: site 0993E  OUT ($BE),A  (vdp_data)
# CHECK low: site 09944  OUT ($BE),A  (vdp_data)
# CHECK low: site 0994B  OUT ($BE),A  (vdp_data)
# CHECK low: site 09951  OUT ($BE),A  (vdp_data)
# CHECK low: site 09961  OUT ($BE),A  (vdp_data)
# CHECK low: site 09967  OUT ($BE),A  (vdp_data)
# CHECK low: site 09982  OUT ($BE),A  (vdp_data)
# CHECK low: site 09987  OUT ($BE),A  (vdp_data)
# CHECK low: site 0998C  OUT ($BE),A  (vdp_data)
# CHECK low: site 09991  OUT ($BE),A  (vdp_data)
# CHECK low: site 0999C  OUT ($BE),A  (vdp_data)
# CHECK low: site 099A0  OUT ($BE),A  (vdp_data)
# CHECK low: site 099A5  OUT ($BE),A  (vdp_data)
# CHECK low: site 099AA  OUT ($BE),A  (vdp_data)
# CHECK low: site 09A07  OUT ($BE),A  (vdp_data)
# CHECK low: site 09A0D  OUT ($BE),A  (vdp_data)
# CHECK low: site 09A14  OUT ($BE),A  (vdp_data)
# CHECK low: site 09A1A  OUT ($BE),A  (vdp_data)
# CHECK low: site 09A28  OUT ($BE),A  (vdp_data)
# CHECK low: site 09A2E  OUT ($BE),A  (vdp_data)
# CHECK low: site 09A35  OUT ($BE),A  (vdp_data)
# CHECK low: site 09A3B  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A0B8  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A0BC  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A0C0  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A0C5  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A120  OUT ($DD),A  (no_effect)
# CHECK low: site 0A3E5  OUT ($DD),A  (no_effect)
# CHECK low: site 0A485  OUT ($DD),A  (no_effect)
# CHECK low: site 0A57D  IN A,($3E)  (unmapped_read)
# CHECK low: site 0A64C  IN A,($3E)  (unmapped_read)
# CHECK low: site 0AA12  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AC0A  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AC10  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AC18  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AC1E  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AC25  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AC2B  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AC38  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AC3E  OUT ($BE),A  (vdp_data)
# CHECK low: site 0B5FE  IN A,($3E)  (unmapped_read)
# CHECK low: site 0B682  IN A,($7E)  (v_counter)
# CHECK low: site 0B6A2  IN A,($3E)  (unmapped_read)
# CHECK low: site 0B72F  IN A,($3E)  (unmapped_read)
# CHECK low: site 0B78B  IN A,($3E)  (unmapped_read)
# CHECK low: site 0B80A  IN A,($3E)  (unmapped_read)
# CHECK low: site 0C1C7  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0C1D1  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0C477  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0C498  IN A,($7E)  (v_counter)
# CHECK low: site 0C5BA  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0C71D  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0C727  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0C8DD  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0C95E  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0C96A  IN A,($7E)  (v_counter)
# CHECK low: site 0C989  OUT ($BE),A  (vdp_data)
# CHECK low: site 0C98E  OUT ($BE),A  (vdp_data)
# CHECK low: site 0C993  OUT ($BE),A  (vdp_data)
# CHECK low: site 0CF06  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0CFDC  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0D118  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0D160  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0D258  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0D2CC  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0D96E  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0DA02  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0DA4E  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0DA95  OUT ($BE),A  (vdp_data)
# CHECK low: site 0DA9B  OUT ($BE),A  (vdp_data)
# CHECK low: site 0DAC0  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0DACA  IN A,($7E)  (v_counter)
# CHECK low: site 0DB55  IN A,($C1)  (joypad_b_misc)
# CHECK low: site 0DC46  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0DD76  OUT ($3E),A  (memory_control)
# CHECK low: site 0DE2D  OUT ($3E),A  (memory_control)
# CHECK low: site 0DECB  IN A,($3E)  (unmapped_read)
# CHECK low: site 0DEDA  IN A,($7E)  (v_counter)
# CHECK low: site 0DF9B  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0E204  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0E2D0  IN A,($7E)  (v_counter)
# CHECK low: site 0E56F  OUT ($BE),A  (vdp_data)
# CHECK low: site 0E575  OUT ($BE),A  (vdp_data)
# CHECK low: site 0E5BC  IN A,($7E)  (v_counter)
# CHECK low: site 0E617  OUT ($BE),A  (vdp_data)
# CHECK low: site 0E61D  OUT ($BE),A  (vdp_data)
# CHECK low: site 0E80C  OUT ($BE),A  (vdp_data)
# CHECK low: site 0E812  OUT ($BE),A  (vdp_data)
# CHECK low: site 0E847  OUT ($BE),A  (vdp_data)
# CHECK low: site 0E84D  OUT ($BE),A  (vdp_data)
# CHECK low: site 0EBD9  OUTD  (port in C)
# CHECK low: site 0FDA6  IN A,($7E)  (v_counter)
# CHECK low: site 0FE6D  IN A,($7E)  (v_counter)
# CHECK low: site 0FE79  IN A,($7E)  (v_counter)
# CHECK low: site 0FE85  IN A,($7E)  (v_counter)
# CHECK low: site 0FE91  IN A,($7E)  (v_counter)
# CHECK low: site 0FE9D  IN A,($7E)  (v_counter)
# CHECK low: site 0FEA9  IN A,($7E)  (v_counter)
# CHECK low: site 0FEC3  IN A,($7E)  (v_counter)
# CHECK low: site 0FEF7  IN A,($7E)  (v_counter)
# CHECK low: site 0FF26  IN A,($7E)  (v_counter)
# CHECK low: site 0FF2B  IN A,($7E)  (v_counter)
# CHECK low: site 0FF48  IN A,($7E)  (v_counter)
# CHECK low: site 0FF70  IN A,($3E)  (unmapped_read)
# CHECK low: site 0FF76  IN A,($7E)  (v_counter)
# CHECK low: site 0FF83  IN A,($7E)  (v_counter)
# CHECK low: site 0FF90  IN A,($7E)  (v_counter)
# CHECK low: site 1034B  OUT ($7F),A  (psg)
# CHECK low: site 1034F  OUT ($7F),A  (psg)
# CHECK low: site 10353  OUT ($7F),A  (psg)
# CHECK low: site 10357  OUT ($7F),A  (psg)
# CHECK low: site 1036D  OUT ($DC),A  (no_effect)
# CHECK low: site 13408  OUT ($BE),A  (vdp_data)
# CHECK low: site 1340E  OUT ($BE),A  (vdp_data)
# CHECK low: site 13413  OUT ($BE),A  (vdp_data)
# CHECK low: site 13417  OUT ($BE),A  (vdp_data)
# CHECK low: site 13456  OUT ($BE),A  (vdp_data)
# CHECK low: site 1345C  OUT ($BE),A  (vdp_data)
# CHECK low: site 13461  OUT ($BE),A  (vdp_data)
# CHECK low: site 13466  OUT ($BE),A  (vdp_data)
# CHECK low: site 134EF  OUT ($BE),A  (vdp_data)
# CHECK low: site 134F4  OUT ($BE),A  (vdp_data)
# CHECK low: site 134FC  OUT ($BE),A  (vdp_data)
# CHECK low: site 13502  OUT ($BE),A  (vdp_data)
# CHECK low: site 13507  OUT ($BE),A  (vdp_data)
# CHECK low: site 1350D  OUT ($BE),A  (vdp_data)
# CHECK low: site 1365A  IN A,($3E)  (unmapped_read)
# CHECK low: site 13662  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 136C1  IN A,($3E)  (unmapped_read)
# CHECK low: site 136D1  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 136FC  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 138E0  OUT ($BE),A  (vdp_data)
# CHECK low: site 138E4  OUT ($BE),A  (vdp_data)
# CHECK low: site 138E8  OUT ($BE),A  (vdp_data)
# CHECK low: site 138ED  OUT ($BE),A  (vdp_data)
# CHECK low: site 13AA0  OUT ($BE),A  (vdp_data)
# CHECK low: site 13AA5  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B36  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B3C  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B42  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B48  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B56  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B5C  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B62  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B68  OUT ($BE),A  (vdp_data)
# CHECK low: site 13B9C  OUT ($BE),A  (vdp_data)
# CHECK low: site 13BA2  OUT ($BE),A  (vdp_data)
# CHECK low: site 13C7C  OUT ($BE),A  (vdp_data)
# CHECK low: site 13C82  OUT ($BE),A  (vdp_data)
# CHECK low: site 17C7E  IN A,($DC)  (joypad_a)
# CHECK low: site 17CAE  IN A,($DC)  (joypad_a)
# CHECK low: site 17DC3  OUT ($BE),A  (vdp_data)
# CHECK low: site 17DC8  OUT ($BE),A  (vdp_data)
site 17FA8   ; OUT ($BE),A
site 17FAC   ; OUT ($BE),A
site 17FB0   ; OUT ($BE),A
site 17FB5   ; OUT ($BE),A
# CHECK low: site 1DC55  IN A,($3E)  (unmapped_read)
# CHECK low: site 1DCB2  IN A,($7E)  (v_counter)
# CHECK low: site 1DCD4  IN A,($3E)  (unmapped_read)
# CHECK low: site 1DCDF  IN A,($3E)  (unmapped_read)
# CHECK low: site 1DD42  IN A,($3E)  (unmapped_read)
# CHECK low: site 1DD4D  IN A,($3E)  (unmapped_read)
# CHECK low: site 1DFA1  IN A,($7E)  (v_counter)
# CHECK low: site 1E05C  IN A,($3E)  (unmapped_read)
# CHECK low: site 1E0A8  IN A,($3E)  (unmapped_read)
# CHECK low: site 1E0D3  IN A,($3E)  (unmapped_read)
# CHECK low: site 1E11C  IN A,($7E)  (v_counter)
# CHECK low: site 1E14D  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 1E5E5  IN A,($3E)  (unmapped_read)
# CHECK low: site 1E5EA  IN A,($3E)  (unmapped_read)
# CHECK low: site 1E858  OUT ($BE),A  (vdp_data)
# CHECK low: site 1E85D  OUT ($BE),A  (vdp_data)
# CHECK low: site 1ED13  OUT ($DD),A  (no_effect)
# CHECK low: site 1ED1B  OUT ($DD),A  (no_effect)
# CHECK low: site 1EDC3  OUT ($DD),A  (no_effect)
# CHECK low: site 1F102  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F107  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F4AD  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F4B2  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F7BF  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F7C5  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F7D7  OUT ($BE),A  (vdp_data)
# CHECK low: site 1F7DD  OUT ($BE),A  (vdp_data)
# CHECK low: site 20051  IN A,($7E)  (v_counter)
# CHECK low: site 22193  IN A,($C0)  (joypad_a)
# CHECK low: site 22197  IN A,($C0)  (joypad_a)
# CHECK low: site 23F95  OUT ($BF),A  (vdp_control)
# CHECK low: site 2DC1C  IN A,($3F)  (unmapped_read)
# CHECK low: site 2F4A4  OUT ($BE),A  (vdp_data)
# CHECK low: site 2FA0B  IN A,($BE)  (vdp_data)
# CHECK low: site 2FA39  OUT ($BE),A  (vdp_data)
# CHECK low: site 2FCEE  OUT ($BE),A  (vdp_data)
# CHECK low: site 2FCF3  OUT ($BE),A  (vdp_data)
# CHECK low: site 2FCFE  OUT ($BE),A  (vdp_data)
# CHECK low: site 2FD03  OUT ($BE),A  (vdp_data)
# CHECK low: site 39B95  IN A,($C0)  (joypad_a)
# CHECK low: site 3B13F  IN A,($3F)  (unmapped_read)
# Mapper stores the flow scan did not reach (sitescan's byte scan, rated high):
# the game starts its tasks by switching stacks and returning, so no scanned
# path reaches them. By their context they are all code, and the SMS reference
# MAME saw 118 of them write the mapper in 10 minutes of play.
mapst 006A2   ; LD ($FFFF),A
mapst 006AB   ; LD ($FFFF),A
mapst 006C5   ; LD ($FFFE),A
mapst 006CC   ; LD ($FFFF),A
mapst 006E3   ; LD ($FFFE),A
mapst 006EA   ; LD ($FFFF),A
mapst 00AF3   ; LD ($FFFF),A
mapst 00B81   ; LD ($FFFF),A
mapst 00B9B   ; LD ($FFFF),A
mapst 00BA9   ; LD ($FFFF),A
mapst 00BC3   ; LD ($FFFF),A
mapst 00BCD   ; LD ($FFFF),A
mapst 014E5   ; LD ($FFFE),A
mapst 014EA   ; LD ($FFFF),A
mapst 01513   ; LD ($FFFE),A
mapst 01518   ; LD ($FFFF),A
mapst 0151E   ; LD ($FFFF),A
mapst 0153B   ; LD ($FFFF),A
mapst 01541   ; LD ($FFFF),A
mapst 0155A   ; LD ($FFFF),A
mapst 01560   ; LD ($FFFF),A
mapst 0157F   ; LD ($FFFF),A
mapst 01585   ; LD ($FFFF),A
mapst 01596   ; LD ($FFFF),A
mapst 0159C   ; LD ($FFFF),A
mapst 015AD   ; LD ($FFFF),A
mapst 015C3   ; LD ($FFFE),A
mapst 015C8   ; LD ($FFFF),A
mapst 015DC   ; LD ($FFFF),A
mapst 015EA   ; LD ($FFFE),A
mapst 015F6   ; LD ($FFFF),A
mapst 01604   ; LD ($FFFF),A
mapst 01613   ; LD ($FFFF),A
mapst 0166D   ; LD ($FFFF),A
mapst 016F1   ; LD ($FFFF),A
mapst 0170C   ; LD ($FFFF),A
mapst 01799   ; LD ($FFFF),A
mapst 01972   ; LD ($FFFF),A
mapst 0197A   ; LD ($FFFF),A
mapst 01987   ; LD ($FFFF),A
mapst 019DC   ; LD ($FFFF),A
mapst 01A97   ; LD ($FFFF),A
mapst 01ADB   ; LD ($FFFF),A
mapst 01B1C   ; LD ($FFFF),A
mapst 01B2B   ; LD ($FFFF),A
mapst 01B5B   ; LD ($FFFF),A
mapst 01B65   ; LD ($FFFF),A
mapst 01B73   ; LD ($FFFF),A
mapst 01BFC   ; LD ($FFFF),A
mapst 01CAA   ; LD ($FFFF),A
mapst 01CF9   ; LD ($FFFF),A
mapst 01D27   ; LD ($FFFF),A
mapst 01D2F   ; LD ($FFFF),A
mapst 01D3A   ; LD ($FFFF),A
mapst 01D5A   ; LD ($FFFF),A
mapst 01D65   ; LD ($FFFF),A
mapst 01D9A   ; LD ($FFFE),A
mapst 01D9F   ; LD ($FFFF),A
mapst 01DBC   ; LD ($FFFE),A
mapst 01DC1   ; LD ($FFFF),A
mapst 01DE0   ; LD ($FFFF),A
mapst 01E09   ; LD ($FFFF),A
mapst 01FA4   ; LD ($FFFF),A
mapst 020AA   ; LD ($FFFF),A
mapst 020D1   ; LD ($FFFF),A
mapst 020F3   ; LD ($FFFF),A
mapst 020FE   ; LD ($FFFF),A
mapst 02115   ; LD ($FFFF),A
mapst 02120   ; LD ($FFFF),A
mapst 02128   ; LD ($FFFF),A
mapst 02162   ; LD ($FFFF),A
mapst 0217F   ; LD ($FFFF),A
mapst 021A2   ; LD ($FFFF),A
mapst 021AA   ; LD ($FFFF),A
mapst 0220A   ; LD ($FFFF),A
mapst 022FD   ; LD ($FFFF),A
mapst 02320   ; LD ($FFFF),A
mapst 0232C   ; LD ($FFFF),A
mapst 02374   ; LD ($FFFF),A
mapst 0237D   ; LD ($FFFF),A
mapst 02390   ; LD ($FFFF),A
mapst 0239E   ; LD ($FFFF),A
mapst 023A7   ; LD ($FFFF),A
mapst 023B8   ; LD ($FFFF),A
mapst 023C0   ; LD ($FFFF),A
mapst 023F9   ; LD ($FFFF),A
mapst 02414   ; LD ($FFFF),A
mapst 024AE   ; LD ($FFFE),A
mapst 024B6   ; LD ($FFFF),A
mapst 025B6   ; LD ($FFFE),A
mapst 0260D   ; LD ($FFFF),A
mapst 026D6   ; LD ($FFFF),A
mapst 02881   ; LD ($FFFF),A
mapst 028D3   ; LD ($FFFE),A
mapst 028D8   ; LD ($FFFF),A
mapst 028FF   ; LD ($FFFE),A
mapst 02904   ; LD ($FFFF),A
mapst 02953   ; LD ($FFFE),A
mapst 02979   ; LD ($FFFE),A
mapst 02AE2   ; LD ($FFFF),A
mapst 02B18   ; LD ($FFFE),A (byte scan: medium; in the same routine as 02AE2 to 02B3B)
mapst 02B1D   ; LD ($FFFF),A
mapst 02B34   ; LD ($FFFE),A
mapst 02B3B   ; LD ($FFFF),A
mapst 02B5F   ; LD ($FFFF),A
mapst 02B67   ; LD ($FFFF),A
mapst 02B80   ; LD ($FFFF),A
mapst 02BE0   ; LD ($FFFF),A
mapst 02BFC   ; LD ($FFFF),A
mapst 02C29   ; LD ($FFFF),A
mapst 02C42   ; LD ($FFFF),A
mapst 02C6E   ; LD ($FFFF),A
mapst 02C7C   ; LD ($FFFF),A
mapst 02C8D   ; LD ($FFFF),A
mapst 02D47   ; LD ($FFFF),A
mapst 02E7F   ; LD ($FFFF),A
mapst 02E93   ; LD ($FFFE),A
mapst 02E98   ; LD ($FFFF),A
mapst 02FC2   ; LD ($FFFF),A
mapst 03080   ; LD ($FFFF),A
mapst 030D7   ; LD ($FFFE),A
mapst 030DC   ; LD ($FFFF),A
mapst 031C1   ; LD ($FFFF),A
mapst 031EC   ; LD ($FFFF),A
mapst 0321A   ; LD ($FFFF),A
mapst 03267   ; LD ($FFFF),A
mapst 0331C   ; LD ($FFFF),A
mapst 03327   ; LD ($FFFE),A
mapst 0332C   ; LD ($FFFF),A
mapst 03349   ; LD ($FFFE),A
mapst 033F5   ; LD ($FFFF),A
mapst 03418   ; LD ($FFFF),A
mapst 0359A   ; LD ($FFFE),A
mapst 0359F   ; LD ($FFFF),A
mapst 0360F   ; LD ($FFFE),A
mapst 03614   ; LD ($FFFF),A
mapst 0367B   ; LD ($FFFF),A
mapst 0368A   ; LD ($FFFF),A
mapst 0375E   ; LD ($FFFE),A
mapst 03763   ; LD ($FFFF),A
mapst 0377E   ; LD ($FFFE),A
mapst 03783   ; LD ($FFFF),A
mapst 0384D   ; LD ($FFFE),A
mapst 03852   ; LD ($FFFF),A
mapst 03BEA   ; LD ($FFFE),A
mapst 03BEF   ; LD ($FFFF),A
mapst 03C19   ; LD ($FFFF),A
mapst 03C22   ; LD ($FFFF),A
mapst 03D47   ; LD ($FFFF),A
mapst 03D99   ; LD ($FFFF),A
mapst 03E6C   ; LD ($FFFF),A
mapst 03EB7   ; LD ($FFFF),A
mapst 04575   ; LD ($FFFF),A
mapst 0458C   ; LD ($FFFF),A
mapst 04741   ; LD ($FFFF),A
mapst 04749   ; LD ($FFFF),A
mapst 0475A   ; LD ($FFFF),A
mapst 04762   ; LD ($FFFF),A
mapst 04773   ; LD ($FFFF),A
mapst 048C7   ; LD ($FFFF),A
mapst 0490F   ; LD ($FFFF),A
mapst 04951   ; LD ($FFFF),A
mapst 04A68   ; LD ($FFFF),A
mapst 04A79   ; LD ($FFFF),A
mapst 04A99   ; LD ($FFFF),A
mapst 04BEC   ; LD ($FFFF),A
mapst 04C01   ; LD ($FFFF),A
mapst 04C0D   ; LD ($FFFF),A
mapst 04E2B   ; LD ($FFFF),A
mapst 04F6E   ; LD ($FFFF),A
mapst 05038   ; LD ($FFFF),A
mapst 05065   ; LD ($FFFF),A
mapst 0509C   ; LD ($FFFF),A
mapst 050CD   ; LD ($FFFF),A
mapst 05214   ; LD ($FFFF),A
mapst 0525E   ; LD ($FFFF),A
mapst 05490   ; LD ($FFFF),A
mapst 05583   ; LD ($FFFF),A
mapst 05594   ; LD ($FFFF),A
mapst 055BC   ; LD ($FFFF),A
mapst 055C7   ; LD ($FFFF),A
mapst 05629   ; LD ($FFFF),A
mapst 0565E   ; LD ($FFFF),A
mapst 05698   ; LD ($FFFF),A
mapst 056F0   ; LD ($FFFF),A
mapst 05811   ; LD ($FFFF),A
mapst 0581C   ; LD ($FFFF),A
mapst 0597B   ; LD ($FFFF),A
mapst 05A0A   ; LD ($FFFF),A
mapst 05A3F   ; LD ($FFFF),A
mapst 05A69   ; LD ($FFFF),A
mapst 05B7C   ; LD ($FFFF),A
mapst 05BA9   ; LD ($FFFF),A
mapst 05BE0   ; LD ($FFFF),A
mapst 05C11   ; LD ($FFFF),A
mapst 05CE8   ; LD ($FFFF),A
mapst 05DC2   ; LD ($FFFF),A
mapst 05DD8   ; LD ($FFFF),A
mapst 05F6D   ; LD ($FFFF),A
mapst 06011   ; LD ($FFFF),A
mapst 0601D   ; LD ($FFFF),A
mapst 06032   ; LD ($FFFF),A
mapst 060C3   ; LD ($FFFF),A
mapst 060D1   ; LD ($FFFF),A
mapst 06372   ; LD ($FFFF),A
mapst 06383   ; LD ($FFFF),A
mapst 0638B   ; LD ($FFFF),A
mapst 0639B   ; LD ($FFFF),A
mapst 06434   ; LD ($FFFF),A
mapst 0643C   ; LD ($FFFF),A
mapst 0644F   ; LD ($FFFF),A
mapst 06463   ; LD ($FFFF),A
mapst 0646B   ; LD ($FFFF),A
mapst 0647F   ; LD ($FFFF),A
mapst 06487   ; LD ($FFFF),A
mapst 064D6   ; LD ($FFFF),A
mapst 064F1   ; LD ($FFFF),A
mapst 0658C   ; LD ($FFFF),A
mapst 065B4   ; LD ($FFFF),A
mapst 065D5   ; LD ($FFFF),A
mapst 065F6   ; LD ($FFFF),A
mapst 06617   ; LD ($FFFF),A
mapst 06638   ; LD ($FFFF),A
mapst 06753   ; LD ($FFFF),A
mapst 06765   ; LD ($FFFF),A
mapst 0685E   ; LD ($FFFF),A
mapst 068A1   ; LD ($FFFF),A
mapst 075B5   ; LD ($FFFF),A
mapst 075D5   ; LD ($FFFF),A
mapst 07626   ; LD ($FFFF),A
mapst 077BA   ; LD ($FFFF),A
mapst 077E0   ; LD ($FFFF),A
mapst 077F0   ; LD ($FFFF),A
mapst 0780B   ; LD ($FFFF),A
mapst 07813   ; LD ($FFFF),A
mapst 0781E   ; LD ($FFFF),A
mapst 07867   ; LD ($FFFF),A
mapst 07875   ; LD ($FFFF),A
mapst 07882   ; LD ($FFFF),A
mapst 078AC   ; LD ($FFFF),A
mapst 078C9   ; LD ($FFFF),A
mapst 078FF   ; LD ($FFFF),A
mapst 07922   ; LD ($FFFF),A
mapst 07985   ; LD ($FFFF),A
mapst 0799D   ; LD ($FFFF),A
mapst 079CA   ; LD ($FFFF),A
mapst 079ED   ; LD ($FFFF),A
mapst 079F5   ; LD ($FFFF),A
mapst 07A05   ; LD ($FFFF),A
mapst 07A29   ; LD ($FFFF),A
mapst 07A39   ; LD ($FFFF),A
mapst 07A4D   ; LD ($FFFF),A
mapst 07A6A   ; LD ($FFFF),A
mapst 07A7A   ; LD ($FFFF),A
mapst 07A93   ; LD ($FFFF),A
mapst 07A9B   ; LD ($FFFF),A
mapst 07AAE   ; LD ($FFFF),A
mapst 07AC1   ; LD ($FFFF),A
mapst 07AE9   ; LD ($FFFF),A
mapst 07B57   ; LD ($FFFF),A
mapst 07BA2   ; LD ($FFFF),A
mapst 07C2C   ; LD ($FFFF),A
mapst 07C47   ; LD ($FFFF),A
mapst 07C6F   ; LD ($FFFF),A
mapst 07C77   ; LD ($FFFF),A
mapst 07C8B   ; LD ($FFFF),A
mapst 07C93   ; LD ($FFFF),A
mapst 07CA4   ; LD ($FFFF),A
mapst 07CC3   ; LD ($FFFF),A
mapst 07CCF   ; LD ($FFFF),A
mapst 07CFB   ; LD ($FFFF),A
mapst 07D0D   ; LD ($FFFF),A
mapst 07D24   ; LD ($FFFF),A
mapst 07D2C   ; LD ($FFFF),A
mapst 07D34   ; LD ($FFFF),A
mapst 07D3C   ; LD ($FFFF),A
mapst 07D47   ; LD ($FFFF),A
mapst 07D60   ; LD ($FFFF),A
mapst 07D6C   ; LD ($FFFF),A
mapst 07D79   ; LD ($FFFF),A
mapst 07D9C   ; LD ($FFFF),A
mapst 07DAA   ; LD ($FFFF),A
mapst 07DD3   ; LD ($FFFF),A
mapst 07DF3   ; LD ($FFFF),A
mapst 07E3E   ; LD ($FFFF),A
mapst 07E73   ; LD ($FFFF),A
mapst 07E7E   ; LD ($FFFF),A
mapst 07E92   ; LD ($FFFF),A
mapst 07ECD   ; LD ($FFFF),A
mapst 07EDA   ; LD ($FFFF),A
mapst 07EEA   ; LD ($FFFF),A
mapst 07EFD   ; LD ($FFFF),A
mapst 07F05   ; LD ($FFFF),A
mapst 07F43   ; LD ($FFFF),A
mapst 07F9D   ; LD ($FFFF),A
mapst 07FAA   ; LD ($FFFF),A
mapst 08702   ; LD ($FFFE),A
mapst 08778   ; LD ($FFFE),A
mapst 08795   ; LD ($FFFE),A
mapst 0892A   ; LD ($FFFE),A
mapst 08992   ; LD ($FFFE),A
mapst 09365   ; LD ($FFFE),A
mapst 0939D   ; LD ($FFFE),A
mapst 093A6   ; LD ($FFFE),A
mapst 093DE   ; LD ($FFFE),A
mapst 093E7   ; LD ($FFFE),A
mapst 0941F   ; LD ($FFFE),A
mapst 09428   ; LD ($FFFE),A
mapst 09460   ; LD ($FFFE),A
mapst 09469   ; LD ($FFFE),A
mapst 094A1   ; LD ($FFFE),A
mapst 094AA   ; LD ($FFFE),A
mapst 094E2   ; LD ($FFFE),A
mapst 094EB   ; LD ($FFFE),A
mapst 09523   ; LD ($FFFE),A
mapst 09976   ; LD ($FFFE),A
mapst 099B1   ; LD ($FFFE),A
mapst 09F25   ; LD ($FFFE),A
mapst 09F4E   ; LD ($FFFE),A
mapst 09F5F   ; LD ($FFFE),A
mapst 09F70   ; LD ($FFFE),A
mapst 09FBC   ; LD ($FFFE),A
mapst 09FCD   ; LD ($FFFE),A
mapst 0A042   ; LD ($FFFE),A
mapst 0A056   ; LD ($FFFE),A
mapst 0A072   ; LD ($FFFE),A
mapst 0A0AA   ; LD ($FFFE),A
mapst 0A586   ; LD ($FFFE),A
mapst 0A5A3   ; LD ($FFFE),A
mapst 0A65A   ; LD ($FFFE),A
mapst 0A66B   ; LD ($FFFE),A
mapst 0A671   ; LD ($FFFE),A
mapst 0A68E   ; LD ($FFFE),A
mapst 0A80E   ; LD ($FFFE),A
mapst 0A885   ; LD ($FFFE),A
mapst 0A896   ; LD ($FFFE),A
mapst 0A8B3   ; LD ($FFFE),A
mapst 0A8DF   ; LD ($FFFE),A
mapst 0A944   ; LD ($FFFE),A
mapst 0A964   ; LD ($FFFE),A
mapst 0A9FB   ; LD ($FFFE),A
mapst 0AA25   ; LD ($FFFE),A
mapst 0AA42   ; LD ($FFFE),A
mapst 0AE1D   ; LD ($FFFE),A
mapst 0AE52   ; LD ($FFFE),A
mapst 0AE87   ; LD ($FFFE),A
mapst 0AEB0   ; LD ($FFFE),A
mapst 0AEB6   ; LD ($FFFE),A
mapst 0AEEB   ; LD ($FFFE),A
mapst 0AF20   ; LD ($FFFE),A
mapst 0AF3D   ; LD ($FFFE),A
mapst 0AF4E   ; LD ($FFFE),A
mapst 0AF5F   ; LD ($FFFE),A
mapst 0AF70   ; LD ($FFFE),A
mapst 0AF7E   ; LD ($FFFE),A
mapst 0AFB3   ; LD ($FFFE),A
mapst 0AFE8   ; LD ($FFFE),A
mapst 0AFEE   ; LD ($FFFE),A
mapst 0B023   ; LD ($FFFE),A
mapst 0B058   ; LD ($FFFE),A
mapst 0B05E   ; LD ($FFFE),A
mapst 0B081   ; LD ($FFFE),A
mapst 0B092   ; LD ($FFFE),A
mapst 0B098   ; LD ($FFFE),A
mapst 0B0A9   ; LD ($FFFE),A
mapst 0B6A5   ; LD ($FFFE),A
mapst 0B6B6   ; LD ($FFFE),A
mapst 0B7A1   ; LD ($FFFE),A
mapst 0B7B2   ; LD ($FFFE),A
mapst 0B7B9   ; LD ($FFFE),A
mapst 0B7CA   ; LD ($FFFE),A
mapst 0B7E2   ; LD ($FFFE),A
mapst 0B7F3   ; LD ($FFFE),A
mapst 1335A   ; LD ($FFFE),A
mapst 13375   ; LD ($FFFE),A
mapst 13386   ; LD ($FFFE),A
mapst 133AF   ; LD ($FFFE),A
mapst 133FC   ; LD ($FFFE),A
mapst 13424   ; LD ($FFFE),A
mapst 13437   ; LD ($FFFE),A
mapst 1344A   ; LD ($FFFE),A
mapst 138D2   ; LD ($FFFE),A
mapst 138F7   ; LD ($FFFE),A
mapst 138FD   ; LD ($FFFE),A
mapst 139D4   ; LD ($FFFE),A
mapst 139F0   ; LD ($FFFE),A
mapst 13A25   ; LD ($FFFE),A
mapst 13A67   ; LD ($FFFE),A
mapst 13B76   ; LD ($FFFE),A
mapst 13BEB   ; LD ($FFFE),A
mapst 13C03   ; LD ($FFFE),A
mapst 13C3F   ; LD ($FFFE),A
mapst 13C50   ; LD ($FFFE),A
mapst 17708   ; LD ($FFFE),A
mapst 17719   ; LD ($FFFE),A
mapst 17F45   ; LD ($FFFE),A
mapst 17F56   ; LD ($FFFE),A
mapst 17F69   ; LD ($FFFE),A
mapst 17F8A   ; LD ($FFFE),A
mapst 17F9D   ; LD ($FFFE),A
mapst 1DE4F   ; LD ($FFFE),A
mapst 1DE6A   ; LD ($FFFE),A
mapst 1DEF0   ; LD ($FFFE),A
mapst 1DF19   ; LD ($FFFE),A
mapst 1E0EE   ; LD ($FFFE),A
mapst 1E0FF   ; LD ($FFFE),A
mapst 1E105   ; LD ($FFFE),A
mapst 1E116   ; LD ($FFFE),A
mapst 1E41B   ; LD ($FFFE),A
mapst 1E427   ; LD ($FFFE),A
mapst 1E46E   ; LD ($FFFE),A
mapst 1E6A4   ; LD ($FFFE),A
mapst 1E6B5   ; LD ($FFFE),A
mapst 1E6D2   ; LD ($FFFE),A
mapst 1E6E3   ; LD ($FFFE),A
mapst 1E6ED   ; LD ($FFFE),A
mapst 1E6FE   ; LD ($FFFE),A
mapst 1E7C2   ; LD ($FFFE),A
mapst 1E7D3   ; LD ($FFFE),A
mapst 1E876   ; LD ($FFFE),A
mapst 1E887   ; LD ($FFFE),A
mapst 1EC23   ; LD ($FFFE),A
mapst 1EC34   ; LD ($FFFE),A
mapst 1EF68   ; LD ($FFFE),A
mapst 1EF79   ; LD ($FFFE),A
mapst 1EF8A   ; LD ($FFFE),A
mapst 1EF9B   ; LD ($FFFE),A
mapst 1F0A1   ; LD ($FFFE),A
mapst 1F0B2   ; LD ($FFFE),A
mapst 1F79E   ; LD ($FFFE),A
mapst 1F7AF   ; LD ($FFFE),A
