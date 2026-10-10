# Wonder Boy III - The Dragon's Trap, drafted by tools/mkspec.py from sitescan output.
# Sites from the batch 5 detector run with gameplay presses
# (its dynamic I/O log), which also logged the
# bank 0 VDP routines at $0AC6-$0B4C and $0F75-$0F83. The remaining CHECK low
# lines were looked at: operands of other instructions (a call to $41ED, a relative jump to $3400)
# or data.
# RST $20 is a jump through the table of words that follows the RST, indexed by A.
# A scan that followed every such table found no other I/O instruction: the game
# does its VDP I/O through RST $28 (OUT ($BF),A) and RST $30 (OUT ($BE),A), and
# every mapper store in that code is in the list below.
name Wonder Boy III - The Dragon's Trap
cart 679E1676
# No free RST vector: $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00028   ; OUT ($BF),A
site 00030   ; OUT ($BE),A
site 0003A   ; IN A,($BF)
site 00135   ; IN A,($DC)
site 00142   ; IN A,($DD)
site 0017F   ; OUT ($BF),A
site 00184   ; OUT ($BF),A
site 00188   ; OUT ($BE),A
site 001A4   ; OUT ($BF),A
site 001A8   ; OUT ($BF),A
site 001B4   ; OUT ($BE),A
site 001BA   ; OUT ($BF),A
site 001BE   ; OUT ($BF),A
site 001C8   ; OUT ($BE),A
site 001CC   ; OUT ($BE),A
site 001EE   ; OUT ($BF),A
site 001F2   ; OUT ($BF),A
site 001F7   ; OUT ($BF),A
site 001FB   ; OUT ($BF),A
site 00213   ; OUT ($BF),A
site 00218   ; OUT ($BF),A
site 0021C   ; OUT ($BE),A
site 00220   ; OUT ($BE),A
site 00239   ; OUT ($3F),A
site 0023D   ; IN A,($DD)
site 00247   ; OUT ($3F),A
site 0024B   ; IN A,($DD)
site 00255   ; OUT ($F2),A
site 00266   ; OUT ($F2),A
site 00268   ; IN A,($F2)
site 0028B   ; OUT ($F2),A
site 0028F   ; IN A,($BF)
site 00299   ; OUT ($3F),A
site 00AC6   ; OUT ($BF),A
site 00ACB   ; OUT ($BF),A
site 00B43   ; OUT ($BE),A
site 00B46   ; OUT ($BE),A
site 00B49   ; OUT ($BE),A
site 00B4C   ; OUT ($BE),A
site 00F75   ; OUT ($BF),A
site 00F7A   ; OUT ($BF),A
site 00F7F   ; OUT ($BE),A
site 00F83   ; OUT ($BE),A
site 0C00F   ; OUT ($F0),A
site 0C013   ; OUT ($F1),A
site 0C01E   ; OUT ($7F),A
site 0C022   ; OUT ($7F),A
site 0C026   ; OUT ($7F),A
site 0C02A   ; OUT ($7F),A
site 0C50B   ; OUT ($7F),A
site 0C5F0   ; OUT ($7F),A
site 0C5F3   ; OUT ($7F),A
site 0C648   ; OUT ($7F),A
site 0C66E   ; OUT ($7F),A
site 0C6D4   ; OUT ($7F),A
site 0C780   ; OUT ($7F),A
site 0C7D7   ; OUT ($F0),A
site 0C7E0   ; OUT ($F1),A
site 0C7F0   ; OUT ($F0),A
site 0C7F5   ; OUT ($F1),A
site 0C831   ; OUT ($F0),A
site 0C856   ; OUT ($F1),A
site 0C881   ; OUT ($F0),A
site 0C88E   ; OUT ($F1),A
site 0C8E0   ; OUT ($F0),A
site 0C8E4   ; OUT ($F1),A
site 0C900   ; OUT (C),E
site 0C903   ; OUT (C),A
site 0C9CE   ; OUT ($F0),A
site 0C9D2   ; OUT ($F1),A
site 0C9E4   ; OUT ($F0),A
site 0C9E8   ; OUT ($F1),A
site 0CA0A   ; OUT ($F0),A
site 0CA0F   ; OUT ($F1),A
site 0CA2D   ; OUT ($F0),A
site 0CA31   ; OUT ($F1),A
site 0CA3D   ; OUT ($F0),A
site 0CA44   ; OUT ($F1),A
site 0CA64   ; OUT ($F0),A
site 0CA71   ; OUT ($F1),A
site 0CA7B   ; OUT ($F0),A
site 0CA80   ; OUT ($F0),A
# Bank 2 $97F8-$98A5 is a name table writer the detector runs never reached;
# its outputs, checked by hand (the scanner rated them low):
site 09809   ; OUT ($BF),A
site 09810   ; OUT ($BF),A
site 09821   ; OUT ($BE),A
site 09828   ; OUT ($BE),A
site 0982E   ; OUT ($BE),A
site 09835   ; OUT ($BE),A
site 09874   ; OUT ($BE),A
site 0987A   ; OUT ($BE),A
site 09885   ; OUT ($BF),A
site 0988D   ; OUT ($BF),A
mapst 0008A   ; LD ($FFFF),A
mapst 01031   ; LD ($FFFF),A
mapst 0103F   ; LD ($FFFF),A
mapst 0105E   ; LD ($FFFF),A
mapst 01067   ; LD ($FFFF),A
# CHECK indirect_unresolved at 00026 ($0026 bank 0): RET 
# CHECK indirect_unresolved at 0C390 ($8390 bank 3): RET 
# CHECK low: site 03424  IN A,($7E)  (v_counter)
# CHECK low: site 04037  OUT (C),B  (port in C)
# CHECK low: site 0407F  OUT (C),B  (port in C)
# CHECK low: site 040A6  OUT (C),B  (port in C)
# CHECK low: site 040ED  OUT (C),B  (port in C)
# CHECK low: site 13E43  IN A,($C0)  (joypad_a)
# CHECK low: site 13E58  IN A,($C0)  (joypad_a)
# CHECK low: site 1718B  IN A,($DC)  (joypad_a)
# CHECK low: site 1718F  IN A,($DC)  (joypad_a)
# CHECK low: site 17270  IN A,($DC)  (joypad_a)
# CHECK low: site 29497  INDR  (port in C)
# CHECK low: site 2F627  OUT ($BF),A  (vdp_control)
# CHECK low: site 38C74  INDR  (port in C)
# CHECK low: site 38CD4  INDR  (port in C)
# CHECK low: site 38F1D  IN A,($DC)  (joypad_a)
# CHECK low: site 39E85  IN A,($3E)  (unmapped_read)
# CHECK low: site 3B6FC  IN B,(C)  (port in C)
# CHECK low: site 3CA51  OUT ($BF),A  (vdp_control)
# The game keeps flags in the I register (stores to and reads from I in bank 3); the
# framework needs I for IM 2 and keeps the game's I itself (batch 5)
site 0C1AC   ; LD I,A
site 0C1B4   ; LD I,A
site 0C1FB   ; LD I,A
site 0C262   ; LD I,A
site 0C286   ; LD I,A
site 0C29A   ; LD I,A
site 0C2A0   ; LD I,A
site 0C2CF   ; LD I,A
site 0C2E3   ; LD I,A
site 0C2F7   ; LD I,A
site 0C2FD   ; LD I,A
site 0C1EF   ; LD A,I
site 0C211   ; LD A,I
site 0C25E   ; LD A,I
site 0C27C   ; LD A,I
site 0C292   ; LD A,I
site 0C2B0   ; LD A,I
site 0C2CB   ; LD A,I
site 0C2D9   ; LD A,I
site 0C2EF   ; LD A,I
site 0C320   ; LD A,I
site 0C330   ; LD A,I
site 0C345   ; LD A,I
site 0C348   ; LD A,I
site 0C3BB   ; LD A,I
# Mapper stores the draft missed: LD ($FFFF),A in banks 0-1 that no
# scanned path reached, found by sitescan's byte scan. Most follow LD A,n; the
# ones after a register-to-A copy (00A7D, 00D79) and POP AF restore or set the bank
# around a call, checked by hand.
mapst 00121   ; LD ($FFFF),A
mapst 004C8   ; LD ($FFFF),A
mapst 006AD   ; LD ($FFFF),A
mapst 006B5   ; LD ($FFFF),A
mapst 00A7D   ; LD ($FFFF),A
mapst 00A92   ; LD ($FFFF),A
mapst 00C22   ; LD ($FFFF),A
mapst 00D79   ; LD ($FFFF),A
mapst 00D80   ; LD ($FFFF),A
mapst 01223   ; LD ($FFFF),A
mapst 01BE6   ; LD ($FFFF),A
mapst 02868   ; LD ($FFFF),A
mapst 028FC   ; LD ($FFFF),A
mapst 0294A   ; LD ($FFFF),A
mapst 04810   ; LD ($FFFF),A
mapst 04830   ; LD ($FFFF),A
mapst 04927   ; LD ($FFFF),A
mapst 04D3C   ; LD ($FFFF),A
mapst 04D7F   ; LD ($FFFF),A
mapst 04DDE   ; LD ($FFFF),A
mapst 04E12   ; LD ($FFFF),A
mapst 04E32   ; LD ($FFFF),A
mapst 04E4B   ; LD ($FFFF),A
mapst 060A3   ; LD ($FFFF),A
mapst 0612D   ; LD ($FFFF),A
mapst 0614E   ; LD ($FFFF),A
mapst 06378   ; LD ($FFFF),A
mapst 0676F   ; LD ($FFFF),A
mapst 067D1   ; LD ($FFFF),A
mapst 07C08   ; LD ($FFFF),A
mapst 07C91   ; LD ($FFFF),A
