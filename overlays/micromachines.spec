# Micro Machines, drafted by tools/mkspec.py from sitescan output.
name Micro Machines
cart A577CE46
hz 50		; No-Intro regions Europe
# line-0 palette and display: the race turns the display off for part of each
# frame's work; on the Next that ran into the picture as a black band (batch 5)
toppal
# priority: the boats pass under priority tiles (the rack in the bath race,
# in 224-line mode)
priority
# No free RST vector: the cart starts by disabling interrupts, setting SP to $DFFF and calling $0100.
# $0000-$0002 becomes the vector; the game starts at the CALL ($0005) with SP $DFFF.
vector 00 io
start 0005 DFFF
asm 00450 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00454 2   ; IM 1 -> IM 2
    im 2
endasm
asm 0808B 2   ; IM 1 -> IM 2
    im 2
endasm
site 00043   ; IN A,($BF)
site 001E0   ; IN A,($BF)
site 002C5   ; IN A,($7E)
site 00322   ; IN A,($7E)
site 0034D   ; OUT ($BF),A
site 00351   ; OUT ($BF),A
site 00356   ; OUT ($BF),A
site 0035A   ; OUT ($BF),A
site 003C9   ; OUT ($03),A
site 003DE   ; IN A,($7E)
site 0043F   ; OUT ($05),A
site 009C5   ; IN A,($05)
site 009C7   ; IN A,($04)
site 009CF   ; IN A,($05)
site 009D1   ; IN A,($04)
site 009DC   ; IN A,($DC)
site 00BCF   ; OUT ($BF),A
site 00BD2   ; OUT ($BF),A
site 00BDB   ; OTIR
site 00BE4   ; OTIR
site 00BED   ; OTIR
site 01301   ; OUT ($BF),A
site 01306   ; OUT ($BF),A
site 0130D   ; OUT ($BE),A
site 01317   ; OUT ($BE),A
site 02D25   ; OUT ($BF),A
site 02D29   ; OUT ($BF),A
site 02D2C   ; OUT ($BE),A
site 02D30   ; OUT ($BE),A
site 02D56   ; OUT ($BF),A
site 02D5A   ; OUT ($BF),A
site 02D5D   ; OUT ($BE),A
site 031DD   ; OUT ($BF),A
site 031E2   ; OUT ($BF),A
site 031E9   ; OUT ($BE),A
site 031F3   ; OUT ($BF),A
site 031F7   ; OUT ($BF),A
site 03200   ; OTIR
site 03204   ; OUT ($BF),A
site 03208   ; OUT ($BF),A
site 03211   ; OTIR
site 0323A   ; OUT ($BF),A
site 0323E   ; OUT ($BF),A
site 03244   ; OUT ($BE),A
site 03269   ; OUT ($BF),A
site 0326D   ; OUT ($BF),A
site 0326F   ; OUTI
site 03273   ; OUT ($BF),A
site 03277   ; OUT ($BF),A
site 03279   ; OUTI
site 0327D   ; OUT ($BF),A
site 03281   ; OUT ($BF),A
site 03283   ; OUTI
site 03287   ; OUT ($BF),A
site 0328B   ; OUT ($BF),A
site 0328D   ; OUTI
site 03291   ; OUT ($BF),A
site 03295   ; OUT ($BF),A
site 03297   ; OUTI
site 0329B   ; OUT ($BF),A
site 0329F   ; OUT ($BF),A
site 032A1   ; OUTI
site 032A5   ; OUT ($BF),A
site 032A9   ; OUT ($BF),A
site 032AB   ; OUTI
site 032AF   ; OUT ($BF),A
site 032B3   ; OUT ($BF),A
site 032B5   ; OUTI
site 032C9   ; OUT ($BF),A
site 032CD   ; OUT ($BF),A
site 032F2   ; OTIR
site 032FA   ; OUT ($BE),A
site 0331B   ; OUT ($BF),A
site 0331F   ; OUT ($BF),A
site 03321   ; OUTI
site 03325   ; OUT ($BF),A
site 03329   ; OUT ($BF),A
site 0332B   ; OUTI
site 0332F   ; OUT ($BF),A
site 03333   ; OUT ($BF),A
site 03335   ; OUTI
site 03339   ; OUT ($BF),A
site 0333D   ; OUT ($BF),A
site 0333F   ; OUTI
site 03343   ; OUT ($BF),A
site 03347   ; OUT ($BF),A
site 03349   ; OUTI
site 0334D   ; OUT ($BF),A
site 03351   ; OUT ($BF),A
site 03353   ; OUTI
site 03357   ; OUT ($BF),A
site 0335B   ; OUT ($BF),A
site 0335D   ; OUTI
site 03361   ; OUT ($BF),A
site 03365   ; OUT ($BF),A
site 03367   ; OUTI
site 03383   ; OUT ($BF),A
site 03387   ; OUT ($BF),A
site 03389   ; OUTI
site 0338D   ; OUT ($BF),A
site 03391   ; OUT ($BF),A
site 03393   ; OUTI
site 03397   ; OUT ($BF),A
site 0339B   ; OUT ($BF),A
site 0339D   ; OUTI
site 033A1   ; OUT ($BF),A
site 033A5   ; OUT ($BF),A
site 033A7   ; OUTI
site 033AB   ; OUT ($BF),A
site 033AF   ; OUT ($BF),A
site 033B1   ; OUTI
site 033B5   ; OUT ($BF),A
site 033B9   ; OUT ($BF),A
site 033BB   ; OUTI
site 033BF   ; OUT ($BF),A
site 033C3   ; OUT ($BF),A
site 033C5   ; OUTI
site 033C9   ; OUT ($BF),A
site 033CD   ; OUT ($BF),A
site 033CF   ; OUTI
site 033EB   ; OUT ($BF),A
site 033EF   ; OUT ($BF),A
site 033F1   ; OUTI
site 033F5   ; OUT ($BF),A
site 033F9   ; OUT ($BF),A
site 033FB   ; OUTI
site 033FF   ; OUT ($BF),A
site 03403   ; OUT ($BF),A
site 03405   ; OUTI
site 03409   ; OUT ($BF),A
site 0340D   ; OUT ($BF),A
site 0340F   ; OUTI
site 03413   ; OUT ($BF),A
site 03417   ; OUT ($BF),A
site 03419   ; OUTI
site 0341D   ; OUT ($BF),A
site 03421   ; OUT ($BF),A
site 03423   ; OUTI
site 03427   ; OUT ($BF),A
site 0342B   ; OUT ($BF),A
site 0342D   ; OUTI
site 03431   ; OUT ($BF),A
site 03435   ; OUT ($BF),A
site 03437   ; OUTI
site 03F24   ; OUT ($BF),A
site 03F28   ; OUT ($BF),A
site 03F38   ; OUT ($BF),A
site 03F3C   ; OUT ($BF),A
site 0518C   ; OUT ($7E),A
site 05190   ; OUT ($7E),A
site 05194   ; OUT ($7E),A
site 05198   ; OUT ($7E),A
site 06660   ; OUT ($BF),A
site 06663   ; OUT ($BF),A
site 06666   ; OUT ($BE),A
site 06718   ; OUT ($BF),A
site 0671C   ; OUT ($BF),A
site 06729   ; OTIR
site 0672C   ; OUT ($BE),A
site 0673C   ; OUT ($BF),A
site 06740   ; OUT ($BF),A
site 0674D   ; OTIR
site 0757F   ; OUT ($BF),A
site 07583   ; OUT ($BF),A
site 07586   ; OUT ($BE),A
site 07588   ; OUT ($BE),A
site 0778E   ; OUT ($BF),A
site 07792   ; OUT ($BF),A
site 07797   ; OUT ($BF),A
site 0779B   ; OUT ($BF),A
site 078F8   ; OUT (C),L
site 078FA   ; OUT (C),H
site 078FE   ; OUT (C),A
site 07902   ; OUT (C),A
site 07909   ; OUT (C),B
site 0790B   ; OUT (C),H
site 0793E   ; OUT (C),L
site 07940   ; OUT (C),H
site 0794F   ; OUT (C),A
site 07953   ; OUT (C),A
site 07A9F   ; OUT ($BF),A
site 07AA3   ; OUT ($BF),A
site 07DC7   ; OUT ($BF),A
site 07DCB   ; OUT ($BF),A
site 07DD1   ; OTIR
site 07DED   ; OUT ($BF),A
site 07DF1   ; OUT ($BF),A
site 07DF7   ; OTIR
site 07E4A   ; OUT ($BF),A
site 07E4E   ; OUT ($BF),A
site 07E58   ; OTIR
site 07E5C   ; OUT ($BE),A
site 07E70   ; OUT ($BF),A
site 07E74   ; OUT ($BF),A
site 07E7F   ; OTIR
site 07E83   ; OUT ($BE),A
site 07E94   ; OUT ($BF),A
site 07E98   ; OUT ($BF),A
site 07E9E   ; OUT ($BE),A
site 07EAE   ; OUT ($BF),A
site 07EB2   ; OUT ($BF),A
site 07EB7   ; OUT ($BF),A
site 07EBB   ; OUT ($BF),A
site 07F09   ; OUT ($BF),A
site 07F0D   ; OUT ($BF),A
site 07F1D   ; OUT ($BF),A
site 07F21   ; OUT ($BF),A
# The loop at $7F2C writes the race's tiles: 4 bytes a row, from $C000, $C800, $D000 and a 0,
# up to row ($DF1C) * 256 - $C000 (2048 rows, 8K of VRAM, as a race loads). Through the I/O
# traps a row took about 5,700 cycles, 21 frames of the race load. The page entry tile_up
# writes the rows with jt_vwrite.
asm 07F23 35   ; LD HL,$C000 ... the loop ... RET
    rst $00
    db far_io, pg_tile_up, ent_tile_up
    ret
endasm
site 07F65   ; OUT ($BF),A
site 07F69   ; OUT ($BF),A
site 07F76   ; OUT ($BF),A
site 07F7A   ; OUT ($BF),A
site 07F80   ; OUT ($BE),A
site 07F8A   ; OUT ($BF),A
site 07F8E   ; OUT ($BF),A
site 07F9B   ; OUT ($BF),A
site 07F9F   ; OUT ($BF),A
site 07FAC   ; OUT ($BF),A
site 07FB0   ; OUT ($BF),A
site 07FBD   ; OUT ($BF),A
site 07FC1   ; OUT ($BF),A
site 07FCE   ; OTIR
site 07FD2   ; OUT ($BE),A
site 08047   ; OUT ($05),A
site 083D9   ; OUT ($BE),A
site 083DC   ; OUT ($BE),A
site 086DB   ; OUT ($BE),A
site 086DE   ; OUT ($BE),A
site 08747   ; OUT ($BE),A
site 0874A   ; OUT ($BE),A
site 0874F   ; OUT ($BE),A
site 08752   ; OUT ($BE),A
site 087A8   ; OUT ($BE),A
site 087AB   ; OUT ($BE),A
site 08817   ; OUT ($BE),A
site 0881A   ; OUT ($BE),A
site 08B47   ; OUT ($03),A
site 08B5F   ; OUT ($03),A
site 090D4   ; OUT ($BE),A
site 09105   ; IN A,($DC)
site 09113   ; IN A,($DD)
site 09136   ; IN A,($DC)
site 0913D   ; OUT ($03),A
site 0914A   ; IN A,($DC)
site 09151   ; OUT ($03),A
site 09160   ; OUT ($BF),A
site 09164   ; OUT ($BF),A
site 09169   ; OUT ($BF),A
site 0916D   ; OUT ($BF),A
site 0917C   ; OUT ($BE),A
site 09180   ; OUT ($BE),A
site 091BE   ; OUT ($BE),A
site 091C1   ; OUT ($BE),A
site 093DE   ; OUT ($BE),A
site 093E1   ; OUT ($BE),A
site 093F7   ; OUT ($BE),A
site 0940A   ; OUT ($BE),A
site 0940D   ; OUT ($BE),A
site 0941E   ; OUT ($BE),A
site 095B9   ; OUT ($BE),A
site 095BD   ; OUT ($BE),A
site 09885   ; OUT ($BE),A
site 09D7A   ; OUT ($BF),A
site 09D7E   ; OUT ($BF),A
site 09D93   ; OUT ($BF),A
site 09D97   ; OUT ($BF),A
site 09F7B   ; OTIR
site 0A286   ; OUT ($BE),A
site 0A28C   ; OUT ($BE),A
site 0A293   ; OUT ($BE),A
site 0A310   ; OUT ($BE),A
site 0A5B1   ; OUT ($BE),A
site 0A5B7   ; OUT ($BE),A
site 0A675   ; OUT ($BF),A
site 0A679   ; OUT ($BF),A
site 0ABF4   ; OUT ($BE),A
site 0ABF8   ; OUT ($BE),A
site 0AD12   ; OUT ($BE),A
site 0AD16   ; OUT ($BE),A
site 0AD23   ; OUT ($BE),A
site 0AD27   ; OUT ($BE),A
site 0AD30   ; OUT ($BE),A
site 0AD34   ; OUT ($BE),A
site 0AD3B   ; OUT ($BE),A
site 0AD3F   ; OUT ($BE),A
site 0B022   ; IN A,($00)
site 0B341   ; OUT ($BE),A
site 0B352   ; OUT ($BE),A
site 0B35B   ; OUT ($BF),A
site 0B35E   ; OUT ($BF),A
site 0B362   ; OUT ($BF),A
site 0B365   ; OUT ($BF),A
site 0B7F6   ; OUT ($BE),A
site 0B7FC   ; OUT ($BE),A
site 0BA07   ; OUT ($BE),A
site 0BA0B   ; OUT ($BE),A
site 0BA16   ; OUT ($BE),A
site 0BA1A   ; OUT ($BE),A
site 0BA26   ; OUT ($BE),A
site 0BA2A   ; OUT ($BE),A
site 0BA35   ; OUT ($BE),A
site 0BA39   ; OUT ($BE),A
site 0BB39   ; OUT ($BE),A
site 0BB54   ; OUT ($BF),A
site 0BB58   ; OUT ($BF),A
site 0BB5C   ; OUT ($BF),A
site 0BB60   ; OUT ($BF),A
site 0BB6E   ; OUT ($BF),A
site 0BB72   ; OUT ($BF),A
site 0BB75   ; IN A,($7E)
site 0BB7D   ; OUT ($BF),A
site 0BB81   ; OUT ($BF),A
site 0BB86   ; IN A,($7E)
site 0BB8E   ; OUT ($BF),A
site 0BB92   ; OUT ($BF),A
site 0BCD9   ; OUT ($BE),A
site 0BCDE   ; OUT ($BE),A
site 0BD02   ; OUT ($BF),A
site 0BD06   ; OUT ($BF),A
site 0BD0A   ; OUT ($BF),A
site 0BD0E   ; OUT ($BF),A
site 0BD12   ; OUT ($BF),A
site 0BD16   ; OUT ($BF),A
site 0BD1A   ; OUT ($BF),A
site 0BD1E   ; OUT ($BF),A
site 0BD21   ; OUT ($BF),A
site 0BD25   ; OUT ($BF),A
site 0BD28   ; OUT ($BF),A
site 0BD2C   ; OUT ($BF),A
site 0BD44   ; OTIR
site 0BD4D   ; OUT ($BE),A
site 0BF25   ; OUT ($BE),A
site 0BF28   ; OUT ($BE),A
site 0BF3B   ; OTIR
site 17E97   ; OUT ($BF),A
site 17E9B   ; OUT ($BF),A
site 17EA8   ; OUT ($BF),A
site 17EAC   ; OUT ($BF),A
site 17EB9   ; OTIR
site 1BE84   ; OUT ($BF),A
site 1BE88   ; OUT ($BF),A
site 1BE8C   ; OUT ($BF),A
site 1BE90   ; OUT ($BF),A
site 1BE94   ; OUT ($BF),A
site 1BE98   ; OUT ($BF),A
site 1BE9C   ; OUT ($BF),A
site 1BEA0   ; OUT ($BF),A
site 1BEA3   ; OUT ($BF),A
site 1BEA7   ; OUT ($BF),A
site 1BEAA   ; OUT ($BF),A
site 1BEAE   ; OUT ($BF),A
site 1BEC0   ; OUT ($BF),A
site 1BEC4   ; OUT ($BF),A
site 1BED2   ; OUT ($BE),A
site 1BED6   ; OUT ($BE),A
site 1BEDA   ; OUT ($BE),A
site 1BEDE   ; OUT ($BE),A
site 1BEE3   ; OUT ($BE),A
site 1BEE7   ; OUT ($BE),A
site 1BEEB   ; OUT ($BE),A
site 1BEEF   ; OUT ($BE),A
site 1BEF5   ; OUT ($BF),A
site 1BEF9   ; OUT ($BF),A
site 1BF07   ; OUT ($BE),A
site 1BF0B   ; OUT ($BE),A
site 1BF10   ; OUT ($BE),A
site 1BF14   ; OUT ($BE),A
site 23C8D   ; IN A,($00)
site 23CAA   ; OUT ($7E),A
site 23CAE   ; OUT ($7E),A
site 23CB2   ; OUT ($7E),A
site 23CB6   ; OUT ($7E),A
site 23D18   ; OUT ($BF),A
site 23D1B   ; OUT ($BF),A
site 23D28   ; OUT ($BE),A
site 23D2C   ; OUT ($BE),A
site 23D77   ; OUT ($BF),A
site 23D7A   ; OUT ($BF),A
site 23D87   ; OUT ($BE),A
site 23DB8   ; OUT ($BF),A
site 23DBC   ; OUT ($BF),A
site 23DC3   ; OUT ($BE),A
site 23DC7   ; OUT ($BE),A
site 23DD0   ; OUT ($BF),A
site 23DD4   ; OUT ($BF),A
site 23DDB   ; OUT ($BE),A
site 23DDF   ; OUT ($BE),A
site 2B5D7   ; OUT ($7E),A
site 2B5DB   ; OUT ($7E),A
site 2B5DF   ; OUT ($7E),A
site 2B5E3   ; OUT ($7E),A
site 2B65B   ; OUT ($7E),A
site 2B662   ; OUT ($7E),A
site 2B667   ; OUT ($7E),A
site 2B680   ; OUT ($7E),A
site 2B687   ; OUT ($7E),A
site 2B68C   ; OUT ($7E),A
site 2B6B3   ; OUT ($7E),A
site 2B6B6   ; OUT ($7E),A
site 2B6BF   ; OUT ($7E),A
site 2B6C3   ; OUT ($7E),A
site 2B6C6   ; OUT ($7E),A
site 2B6DC   ; OUT ($7E),A
site 2B702   ; OUT ($7E),A
site 2B70A   ; OUT ($7E),A
site 2B720   ; OUT ($7E),A
site 2B746   ; OUT ($7E),A
site 2B74E   ; OUT ($7E),A
site 2B76B   ; OUT ($7E),A
site 2B772   ; OUT ($7E),A
site 2B787   ; OUT ($7E),A
site 2B78E   ; OUT ($7E),A
site 2B852   ; OUT ($7E),A
site 2B856   ; OUT ($7E),A
site 2B859   ; OUT ($7E),A
site 2B866   ; OUT ($7E),A
site 2B86A   ; OUT ($7E),A
site 2B86D   ; OUT ($7E),A
site 30F8C   ; OUT ($7E),A
site 30F9D   ; OUT ($7E),A
site 30FAE   ; OUT ($7E),A
site 30FBA   ; OUT ($7E),A
site 30FBF   ; OUT ($7E),A
site 30FC7   ; OUT ($7E),A
site 30FD4   ; OUT ($7E),A
site 30FE7   ; OUT ($7E),A
site 35801   ; OUT ($BF),A
site 35805   ; OUT ($BF),A
site 35812   ; OTIR
site 35816   ; OUT ($BE),A
site 3594C   ; OUT ($BF),A
site 3594F   ; OUT ($BF),A
site 3595C   ; OUT ($BF),A
site 3595F   ; OUT ($BF),A
site 3596C   ; OUT ($BF),A
site 3596F   ; OUT ($BF),A
site 35978   ; OUT ($BE),A
site 3597C   ; OUT ($BE),A
site 35980   ; OUT ($BE),A
site 35985   ; OUT ($BE),A
site 35992   ; OUT ($BF),A
site 35995   ; OUT ($BF),A
site 35998   ; OUT ($BE),A
site 3599C   ; OUT ($BE),A
site 359A0   ; OUT ($BE),A
site 359A5   ; OUT ($BE),A
site 359C5   ; OUT ($BF),A
site 359C8   ; OUT ($BF),A
site 359CF   ; OUT ($BE),A
site 359D6   ; OUT ($BE),A
site 359DD   ; OUT ($BE),A
site 359E2   ; OUT ($BE),A
site 35FB6   ; IN A,($00)
site 36D98   ; OUT ($BF),A
site 36D9B   ; OUT ($BF),A
site 36D9E   ; OUT ($BE),A
site 37741   ; IN A,($DC)
site 3774F   ; IN A,($DD)
site 37776   ; IN A,($DC)
site 3777D   ; OUT ($03),A
site 3BB19   ; IN A,($BF)
site 3BB38   ; OTIR
site 3BB3B   ; OUT ($BE),A
site 3BB4C   ; OTIR
site 3BB4F   ; OUT ($BE),A
site 3BB6D   ; OUT ($BE),A
site 3BB72   ; OUT ($BE),A
# The game runs a RAM copy of this ROM block (ROM $3BB99-$3BCB9 is RAM $D9D9-$DAF9).
# The scan rated the next sites low; the SMS reference runs all of them.
site 3BB99   ; OUT ($BE),A
site 3BBA1   ; OUT ($BE),A
site 3BBA7   ; OUT ($BE),A
site 3BBAF   ; OUT ($BE),A
# The loop at RAM $DA1B-$DA34 (ROM $3BBDB) writes the row of faces on the character
# choice screen: E name table cells (the byte at HL, then $01), HL going to the next
# source row ($30 on) after each 32 cells. The game runs it about eight times a
# frame while the row scrolls. Through the I/O traps (a run of OUT (C),A that is
# made again at every entry, as the code is in RAM) one call took about 67,000
# cycles, and the frame handler ran into the next frame: the held display-off
# write then applied at the next frame event, and the top of the screen flickered.
# The page entry face_row writes the cells with one jt_vwrite call. The 22 bytes
# after the far call are NOPs up to the game's JP $DB48 at $DA35.
asm 3BBDB 26   ; LD B,0 ... JP $DA1D (the loop)
    rst $00
    db far_io, pg_face_row, ent_face_row
endasm
# The loops at RAM $DA6C, $DA81 and $DA98 (ROM $3BC2C, $3BC41, $3BC58) write E rows of
# tile pattern, each 3 bytes from HL and a 0, after the character choice: about
# 5,500 cycles a row through the traps, up to 670,000 a call, so the frame handler
# ran past the next frame and the screen went off for a frame (the flicker at the
# pick). The page entry tile_rows writes them with two jt_vwrite calls.
asm 3BC2C 12   ; LD B,3 ... JR NZ (the loop)
    rst $00
    db far_io, pg_tile_rows, ent_tile_rows
endasm
asm 3BC41 12   ; the same loop
    rst $00
    db far_io, pg_tile_rows, ent_tile_rows
endasm
asm 3BC58 12   ; the same loop
    rst $00
    db far_io, pg_tile_rows, ent_tile_rows
endasm
site 3BC6E   ; OUT ($BE),A
site 3BC74   ; OUT ($BE),A
site 3BCB6   ; OTIR
site 3BCB9   ; OUT ($BE),A
site 3BCC1   ; OUT ($BF),A
site 3BCC4   ; OUT ($BF),A
site 3BCC8   ; OUT ($BF),A
# RAM $DB0B, the second byte of the address set at $DB07 (CALL $DB07 at $BD49 and $BD8E). The
# race uses $DB07 on as data (LD IY,$DB07 at $38C8, then LD (IY+n),A at $398E on), and the
# copier at $B971 (bank 14) writes the block again. A full race with this site runs to the
# result screen.
site 3BCCB   ; OUT ($BF),A
# RAM code at $DBC0 (copied from ROM $0075 by the start-up code at $010E,
# reached by JP $DBC0 at $80BB as the race loads): maps banks 0 and 1.
# Unpatched, its writes went into the cart copy and wrote $00 over the
# vector at $0000 (batch 5).
codem 00077   ; LD ($0000),A
codem 0007C   ; LD ($4000),A
codem 0000E   ; LD ($8000),A
codem 00017   ; LD ($8000),A
codem 001CC   ; LD ($8000),A
codem 001D6   ; LD ($8000),A
codem 00291   ; LD ($8000),A
codem 002EB   ; LD ($8000),A
codem 0036A   ; LD ($8000),A
codem 0045A   ; LD ($8000),A
codem 00465   ; LD ($8000),A
codem 00A9F   ; LD ($8000),A
codem 00AA9   ; LD ($8000),A
codem 00AB3   ; LD ($8000),A
codem 00ABD   ; LD ($8000),A
codem 00ACE   ; LD ($8000),A
codem 00AD9   ; LD ($8000),A
codem 00AE3   ; LD ($8000),A
codem 00AED   ; LD ($8000),A
codem 00AF7   ; LD ($8000),A
codem 00B00   ; LD ($8000),A
codem 00B0B   ; LD ($8000),A
codem 00EE8   ; LD ($8000),A
codem 012C1   ; LD ($8000),A
codem 012CC   ; LD ($8000),A
codem 012D7   ; LD ($8000),A
codem 01ABF   ; LD ($8000),A
codem 01CF6   ; LD ($8000),A
codem 01DE9   ; LD ($8000),A
codem 01F08   ; LD ($8000),A
codem 01F10   ; LD ($8000),A
codem 01F28   ; LD ($8000),A
codem 01F30   ; LD ($8000),A
codem 01F55   ; LD ($8000),A
codem 01F69   ; LD ($8000),A
codem 02019   ; LD ($8000),A
codem 02025   ; LD ($8000),A
codem 022DD   ; LD ($8000),A
codem 022E5   ; LD ($8000),A
codem 03172   ; LD ($8000),A
codem 03184   ; LD ($8000),A
codem 03190   ; LD ($8000),A
codem 0319B   ; LD ($8000),A
codem 032E7   ; LD ($8000),A
codem 0343C   ; LD ($8000),A
codem 03447   ; LD ($8000),A
codem 03A25   ; LD ($8000),A
codem 03B57   ; LD ($8000),A
codem 03B69   ; LD ($8000),A
codem 03D50   ; LD ($8000),A
codem 03DBF   ; LD ($8000),A
codem 03DD3   ; LD ($8000),A
codem 03E26   ; LD ($8000),A
codem 03E31   ; LD ($8000),A
codem 03F19   ; LD ($8000),A
codem 03F2D   ; LD ($8000),A
codem 03F47   ; LD ($8000),A
codem 03F50   ; LD ($8000),A
codem 03FB6   ; LD ($8000),A
codem 03FBF   ; LD ($8000),A
codem 04733   ; LD ($8000),A
codem 0473B   ; LD ($8000),A
codem 04829   ; LD ($8000),A
codem 04831   ; LD ($8000),A
codem 048C4   ; LD ($8000),A
codem 048CD   ; LD ($8000),A
codem 049F1   ; LD ($8000),A
codem 0516B   ; LD ($8000),A
codem 05176   ; LD ($8000),A
codem 0519F   ; LD ($8000),A
codem 051AA   ; LD ($8000),A
codem 051D1   ; LD ($8000),A
codem 05527   ; LD ($8000),A
codem 0552E   ; LD ($8000),A
codem 05546   ; LD ($8000),A
codem 0554D   ; LD ($8000),A
codem 05598   ; LD ($8000),A
codem 055AC   ; LD ($8000),A
codem 0562F   ; LD ($8000),A
codem 0563B   ; LD ($8000),A
codem 059E6   ; LD ($8000),A
codem 05AAA   ; LD ($8000),A
codem 05AB2   ; LD ($8000),A
codem 064C0   ; LD ($8000),A
codem 06613   ; LD ($8000),A
codem 0661E   ; LD ($8000),A
codem 06629   ; LD ($8000),A
codem 06634   ; LD ($8000),A
codem 06647   ; LD ($8000),A
codem 06713   ; LD ($8000),A
codem 06737   ; LD ($8000),A
codem 06A8E   ; LD ($8000),A
codem 0728C   ; LD ($8000),A
codem 07329   ; LD ($8000),A
codem 073C4   ; LD ($8000),A
codem 073CD   ; LD ($8000),A
codem 0746D   ; LD ($8000),A
codem 07479   ; LD ($8000),A
codem 07482   ; LD ($8000),A
codem 07626   ; LD ($8000),A
codem 07664   ; LD ($8000),A
codem 07A75   ; LD ($8000),A
codem 07A8B   ; LD ($8000),A
codem 07C69   ; LD ($8000),A
codem 07C74   ; LD ($8000),A
codem 07CD8   ; LD ($8000),A
codem 07D11   ; LD ($8000),A
codem 07D64   ; LD ($8000),A
codem 07DD8   ; LD ($8000),A
codem 07DFC   ; LD ($8000),A
codem 07E01   ; LD ($8000),A
codem 07F50   ; LD ($8000),A
codem 07F59   ; LD ($8000),A
codem 0AFC1   ; LD ($8000),A
codem 0AFC9   ; LD ($8000),A
codem 3BB08   ; LD ($8000),A
codem 3BB11   ; LD ($8000),A
codem 3BB28   ; LD ($8000),A
codem 3BCF8   ; LD ($8000),A
codem 3BD0A   ; LD ($8000),A
# between the two above, the same routine's third LD ($8000),A (RAM $DB41);
# no run reached it (batch 5)
codem 3BD01   ; LD ($8000),A
# Sites in the mode handlers. The main loop ($808E) calls $80E6, which jumps through the
# word table at $80BE, indexed by the byte at $D699 ($80F9 CALL $8100, JP (HL)). The
# sites below are in code that the handler at the table entry named on each line reaches
# by jumps and calls; the SMS reference runs did not reach them.
# Entry $8FC4, by the jumps at $8FDC, $900B and $9019 (CALL $B35A sets the VRAM address).
site 09021   ; OUT ($BE),A
site 09024   ; OUT ($BE),A
# Entry $8CE7, through the calls and jumps at $996E, $997B and $99D3 (the first two sites), and
# $9A6D and $9AE9 (the other two).
site 099EB   ; OUT ($BE),A
site 099EF   ; OUT ($BE),A
site 09B11   ; OUT ($BE),A
site 09B15   ; OUT ($BE),A
# Entry $B56D, by CALL $A0F0 (the loop at $A109 writes 12 cells).
site 0A10B   ; OUT ($BE),A
site 0A10E   ; OUT ($BE),A
# Entry $8EF0, by CALL $A9C6 (a tile and its attribute byte).
site 0A9E4   ; OUT ($BE),A
site 0A9E8   ; OUT ($BE),A
# Entry $8C35, by CALL $AFCD, CALL $BB95 and CALL $BD94 (at $BBDA).
site 0BD9E   ; OTIR
# Entry $8BAB (the word at $80C0 of the table), by CALL $AF10 at $8BAB and JR NZ,$AF6F at $AF1F:
# the text write at $AF8F (CALL $B35A at $AF7F sets the VRAM address).
site 0AF8F   ; OUT ($BE),A
# RAM routines in the block that the game copies from ROM $3B97D to RAM $D7BD. The block
# is entered at RAM $DA38 (ROM $3BBF8) by JP $DA38 at $9814 (entry $8CE7, by CALL $97EA
# and the jump at $9804) and at RAM $DABD (ROM $3BC7D) by JP $DABD at $AECA (entry $8E15,
# by CALL $AE94).
site 3BBFF   ; OUT ($BE),A
site 3BC03   ; OUT ($BE),A
site 3BC83   ; OUT ($BE),A
site 3BC87   ; OUT ($BE),A
# CHECK ram_exec at 08018 ($8018 bank 2): CALL $C000 $C000
# CHECK ram_exec at 080BB ($80BB bank 2): JP $DBC0 $DBC0
# CHECK ram_exec at 0B031 ($B031 bank 2): JP $C000 $C000
# CHECK indirect_unresolved at 080F9 ($80F9 bank 2): CALL $8100 
# CHECK bank_unresolved at 3BCE0 ($DB20 bank ram): CALL $8CE8 $8CE8
# CHECK low: site 0862A  IN A,($3E)  (unmapped_read)
# CHECK low: site 09021  OUT ($BE),A  (vdp_data)
# CHECK low: site 09024  OUT ($BE),A  (vdp_data)
# CHECK low: site 099EB  OUT ($BE),A  (vdp_data)
# CHECK low: site 099EF  OUT ($BE),A  (vdp_data)
# CHECK low: site 09B11  OUT ($BE),A  (vdp_data)
# CHECK low: site 09B15  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A10B  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A10E  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A7C0  IN A,($DC)  (joypad_a)
# CHECK low: site 0A7D6  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 0A9E4  OUT ($BE),A  (vdp_data)
# CHECK low: site 0A9E8  OUT ($BE),A  (vdp_data)
# CHECK low: site 0AF8F  OUT ($BE),A  (vdp_data)
# CHECK low: site 0B731  IN A,($3E)  (unmapped_read)
# CHECK low: site 0BB65  OUT ($BF),A  (vdp_control)
# CHECK low: site 0BB69  OUT ($BF),A  (vdp_control)
# CHECK low: site 0BD9E  OTIR  (port in C)
# CHECK low: site 0BF67  OUT ($BE),A  (vdp_data)
# CHECK low: site 0BF6A  OUT ($BE),A  (vdp_data)
# CHECK low: site 0BF7D  OTIR  (port in C)
# CHECK low: site 0F1D2  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 12386  IN A,($C0)  (joypad_a)
# CHECK low: site 1248A  IN A,($C0)  (joypad_a)
# CHECK low: site 136D1  IN A,($7F)  (h_counter)
# CHECK low: site 13A24  IN A,($7F)  (h_counter)
# CHECK low: site 1584E  IN A,($DC)  (joypad_a)
# CHECK low: site 15F8E  INIR  (port in C)
# CHECK low: site 16B6B  IN D,(C)  (port in C)
# CHECK low: site 16C15  IN A,($F0)  (joypad_a)
# CHECK low: site 1760D  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 1A9C9  IN A,($3F)  (unmapped_read)
# CHECK low: site 1B542  IN B,(C)  (port in C)
# CHECK low: site 1DBCC  IN A,($DC)  (joypad_a)
# CHECK low: site 1E6D0  OUT (C),B  (port in C)
# CHECK low: site 1F497  OUTI  (port in C)
# CHECK low: site 1F58B  IN A,($F1)  (joypad_b_misc)
# CHECK low: site 1F632  OUT ($3F),A  (io_control)
# CHECK low: site 21515  IN A,($DC)  (joypad_a)
# CHECK low: site 25A10  IN A,($DC)  (joypad_a)
# CHECK low: site 25A44  IN A,($DC)  (joypad_a)
# CHECK low: site 25B90  IN A,($DC)  (joypad_a)
# CHECK low: site 25C1C  IN A,($DC)  (joypad_a)
# CHECK low: site 25C50  IN A,($DC)  (joypad_a)
# CHECK low: site 25EBC  IN A,($DC)  (joypad_a)
# CHECK low: site 267EA  IN A,($F0)  (joypad_a)
# CHECK low: site 27294  OUT (C),B  (port in C)
# CHECK low: site 277F2  OUTI  (port in C)
# CHECK low: site 27875  OUT ($7F),A  (psg)
# CHECK low: site 278F7  OUT (C),C  (port in C)
# CHECK low: site 27ABB  IN A,($C0)  (joypad_a)
# CHECK low: site 2A4AB  OUT (C),H  (port in C)
# CHECK low: site 2A99E  OUT (C),C  (port in C)
# CHECK low: site 2CD52  IN A,($7E)  (v_counter)
# CHECK low: site 2CEAE  IN A,($7F)  (h_counter)
# CHECK low: site 2D022  IN A,($7E)  (v_counter)
# CHECK low: site 2E093  IN A,($7E)  (v_counter)
# CHECK low: site 300DB  IN A,($BD)  (vdp_status)
# CHECK low: site 33BC5  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 33CF2  OUT ($3F),A  (io_control)
# CHECK low: site 33D5B  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 33D66  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 33D71  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 35CF8  OUT ($F0),A  (fm_address)
# CHECK low: site 384C9  OUT (C),A  (port in C)
# CHECK low: site 389F8  IND  (port in C)
# CHECK low: site 3BBFD  IN A,($7E)  (v_counter)
# CHECK low: site 3BBFF  OUT ($BE),A  (vdp_data)
# CHECK low: site 3BC03  OUT ($BE),A  (vdp_data)
# CHECK low: site 3BC83  OUT ($BE),A  (vdp_data)
# CHECK low: site 3BC87  OUT ($BE),A  (vdp_data)
# CHECK low: site 3C012  IN A,($BD)  (vdp_status)
# CHECK low: site 3CA93  OUT (C),B  (port in C)
# CHECK low: site 3CDEC  INIR  (port in C)
# CHECK low: site 3DC1D  IN A,($7F)  (h_counter)
# CHECK low: site 3ED81  OUT ($BF),A  (vdp_control)
# CHECK low: site 3ED87  OUT ($BE),A  (vdp_data)
# CHECK low: site 3ED90  IN A,($7E)  (v_counter)
# CHECK low: site 3EDCF  OUT ($BE),A  (vdp_data)
# CHECK low: site 3EE14  OTIR  (port in C)
# CHECK low: site 3EE28  IN A,($7F)  (h_counter)
# CHECK low: site 3EE68  OUTI  (port in C)
# CHECK low: site 3EE6C  OUT (C),D  (port in C)
# CHECK low: site 3EE92  IN A,($DC)  (joypad_a)
# CHECK low: site 3EFC0  IN A,($DC)  (joypad_a)
# CHECK low: site 3EFDD  OUT ($7E),A  (psg)
# CHECK low: site 3F060  OTIR  (port in C)
# CHECK low: site 3F4F8  OUT ($7E),A  (psg)
# CHECK low: site 3F8AF  OTIR  (port in C)
# CHECK low: site 3F8C0  IN A,($DC)  (joypad_a)
# CHECK low: site 3F948  INIR  (port in C)
# CHECK low: site 3F9DF  OTIR  (port in C)
# CHECK low: site 3F9FB  OUTI  (port in C)
# CHECK low: site 3FA05  IN A,($7E)  (v_counter)
# CHECK low: site 3FA3B  OUT ($BE),A  (vdp_data)
# CHECK low: site 3FA74  OUT ($BF),A  (vdp_control)
# At power-on the game unpacks code from bank 15 ($AD49) to RAM $C000 with its routine at
# $D7BD (CALL $D7BD at $8015) and runs it once (CALL $C000 at $8018): the Codemasters logo
# with its jingle, or the cart test when buttons 1 and 2 are held. No other code runs it,
# and the next unpack writes over it. Page 1 replaces every routine of that code that does
# I/O. The CALL $C000 goes through the cave at $BB63, where logo_patch checks the RAM image
# and writes a far call at the start of each routine; the game's own code in RAM still runs
# the logo's frame loop. The cave is the routine at $BB63 (register 1 = $70), which no CALL,
# JP, JR or word reaches.
# The code that $B02E unpacks from $B753 and jumps to (JP $C000 at $B031) runs only when
# $DC3C is not 0, and the only store to $DC3C is LD ($DC3C),A with A = 0 at $8007: it is
# never run (its ports $00-$05 are the Game Gear's).
label logo_cave 0BB63
asm 08018 3    ; CALL $C000
    call logo_cave
endasm
asm 0BB63 9    ; the unused routine at $BB63
    rst $00
    db far_io, pg_logo_patch, ent_logo_patch
    jp $C000
endasm
# Codemasters mapper stores the flow scan did not reach (byte scan):
# 000B1 runs from RAM: the routine at $0173 (called from $0120) copies the
# game's 18-byte restart routine at $00AE to $DC99 and runs it there; the routine
# maps bank 2 into slot 2, resets the stack and jumps to $8000. The cart
# image is patched before the game copies it, so the copy carries the patch.
codem 000B1   ; LD ($8000),A
# 05B7A (selects bank $8E through $8000, then jumps to $A003, after two RETs) has no jump, call
# or pointer to it anywhere in the cart: left unpatched.

page 0 face_row tile_rows
; face_row: the game's loop at RAM $DA1B. In: HL = the source (the game has its
; bank at $8000), E = cells (0 = 256), the VDP address set for a VRAM write.
; Each cell is the source byte and $01; after each 32nd cell but the last, HL
; goes $30 on. Returns as the loop ends: HL past the source, E = 0, B = 0,
; C = $BE, A = 1, Z set; D kept. Interrupts off while it runs (the game's
; frame handler maps banks), then as they were.
face_row:
        ld a,i                  ; P/V = IFF2
        push af
        di
        push ix
        push iy
        push de
        ld b,e                  ; the game's cell counter
        ld de,buf
.cell:  call rd                 ; the source byte
        ld (de),a
        inc de
        ld a,1
        ld (de),a
        inc de
        inc hl
        dec b
        jr z,.done
        ld a,b
        and $1F
        jr nz,.cell
        push bc
        ld bc,$0030
        add hl,bc
        pop bc
        jr .cell
.done:  pop de
        push de
        push hl
        ld l,e                  ; 2 bytes a cell (0 = 256 cells)
        ld h,0
        ld a,e
        or a
        jr nz,.n
        inc h
.n:     add hl,hl
        ld a,16                 ; pieces end at name table columns 8 and 32
        call wr_buf
        pop hl
        pop de
        ld e,0
        ld bc,$00BE
        pop iy
        pop ix
        pop af
        jp po,.di
        ei
.di:    xor a                   ; Z set, A = 1, as the loop leaves them
        ld a,1
        ret

; tile_rows: the game's loop B = 3, C = $BE, OTIR, XOR A, OUT ($BE),A, DEC E,
; JR NZ. In: HL = the source, E = rows (not 0), the VDP address set for a VRAM
; write. Each row is 3 bytes from HL and a 0. Returns as the loop ends: HL past
; the source, E = 0, B = 0, C = $BE, A = 0, Z set; D kept.
tile_rows:
        ld a,i
        push af
        di
        push ix
        push iy
        push de
        ld b,e                  ; rows
        ld de,buf
.row:   ld c,3
.byte:  call rd
        ld (de),a
        inc de
        inc hl
        dec c
        jr nz,.byte
        xor a
        ld (de),a
        inc de
        djnz .row
        pop de
        push de
        push hl
        ld l,e                  ; 4 bytes a row
        ld h,0
        add hl,hl
        add hl,hl
        xor a                   ; pieces of up to 256 bytes
        call wr_buf
        pop hl
        pop de
        ld e,0
        ld bc,$00BE
        pop iy
        pop ix
        pop af
        jp po,.di
        ei
.di:    xor a                   ; A = 0, Z set, as the loop leaves them
        ret

; A = the byte the game sees at HL: a plain read outside $2000-$3FFF (this
; page), jt_peek there. Keeps BC, DE, HL.
rd:     ld a,h
        and $E0
        cp $20
        jr z,.pk
        ld a,(hl)
        ret
.pk:    jp jt_peek

; Writes HL bytes (1-1024) of buf to VRAM from the VDP address, one jt_vwrite
; call a piece. A = 16: a piece ends where a name table row's column 8 or
; column 32 starts (VRAM offset 16 or 64 in its 64-byte row), so jt_vwrite
; takes its fast form for name table entries. A = 0: pieces of up to 256
; bytes. Uses A, BC, DE, HL, IX, IY.
wr_buf: ld (pc_mode),a
        ld (rem),hl
        ld hl,(vdp_addr)
        ld a,h
        and $3F
        ld d,a
        ld e,l                  ; DE = the VRAM address
        ld hl,buf
.seg:   ld a,(pc_mode)
        or a
        ld b,0                  ; 256
        jr z,.lim
        ld a,e
        and $3F
        ld c,a                  ; the offset in the row
        cp 16
        ld a,16
        jr c,.b
        ld a,64
.b:     sub c
        ld b,a                  ; bytes up to the boundary
.lim:   push hl
        ld hl,(rem)
        ld a,h
        or a
        jr nz,.full             ; 256 or more left
        ld a,b
        dec a                   ; B - 1 (B = 0: 255)
        cp l
        jr c,.full              ; B <= left
        ld b,l                  ; fewer left: all of them
.full:  ld a,l
        sub b
        ld l,a
        jr nc,.r
        dec h
.r:     ld a,b
        or a
        jr nz,.r2
        dec h                   ; B = 0: 256 bytes
.r2:    ld (rem),hl
        pop hl                  ; HL = the next byte of buf
        ld c,1
        ld ix,0
        ld iy,0
        ld a,1                  ; buf as mapped: in this page
        call jt_vwrite          ; keeps BC, DE, HL
        ld c,b
        ld b,0
        ld a,c
        or a
        jr nz,.adv
        inc b                   ; 256
.adv:   add hl,bc               ; buf on
        ex de,hl
        add hl,bc               ; the VRAM address on, within $0000-$3FFF
        ld a,h
        and $3F
        ld h,a
        ex de,hl
        push hl
        ld hl,(rem)
        ld a,h
        or l
        pop hl
        jr nz,.seg
        ret
pc_mode: db 0
rem:    dw 0
buf:    ds 1024
endpage

page 1 logo_patch logo_init logo_end logo_out psg_off psg_vol psg_tone tile_up
; The routines of the logo code that the game unpacks to RAM $C000 at power-on.
; logo_patch writes the far calls into that code; each other entry does what the
; game's routine at its RAM address does, with VRAM writes through jt_vwrite and
; the other I/O through the runtime (RST $00). They run with interrupts off, as
; the logo code does (DI at $C000), and leave them so.

; logo_patch: from the cave at $BB63, after the unpack and before JP $C000.
; Checks the 3680 bytes from $C000 (two 16-bit sums) and writes the far calls;
; a different image stops the game (jt_fatal). Keeps BC, DE, HL, IX; A, F change.
logo_patch:
        push bc
        push de
        push hl
        push ix
        ld hl,$C000
        ld bc,3680
        ld de,0                 ; the sum of the bytes
        ld ix,0                 ; the sum of those sums
.ck:    ld a,(hl)
        add a,e
        ld e,a
        jr nc,.ck1
        inc d
.ck1:   add ix,de
        inc hl
        dec bc
        ld a,b
        or c
        jr nz,.ck
        ld hl,$1514
        or a
        sbc hl,de
        jr nz,.bad
        push ix
        pop hl
        ld de,$F015
        sbc hl,de
        jr nz,.bad
        ld hl,stubs
.st:    ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,d
        or e
        jr z,.done
        ld c,(hl)
        inc hl
        ld b,0
        ldir
        jr .st
.done:  pop ix
        pop hl
        pop de
        pop bc
        ret
.bad:   jp jt_fatal

; The far calls: RAM address, length, bytes. RST $00 is the io vector.
stubs:  dw $C032                ; CALL $C051 ... RET: the end of the logo
        db 5, $C7, far_io, pg_logo_end, ent_logo_end, $C9
        dw $C0BF                ; the screen set-up, and the cart test
        db 7, $C7, far_io, pg_logo_init, ent_logo_init
        db $D0, $C1, $C9        ; RET NC; POP BC; RET (the test ends as JP $C050)
        dw $C417                ; CALL $C051 ... OTIR; RET: a logo step's writes
        db 5, $C7, far_io, pg_logo_out, ent_logo_out, $C9
        dw $CA99                ; the PSG volumes off
        db 5, $C7, far_io, pg_psg_off, ent_psg_off, $C9
        dw $CAB1                ; three PSG volumes from the jingle data
        db 5, $C7, far_io, pg_psg_vol, ent_psg_vol, $C9
        dw $CACA                ; a PSG tone
        db 5, $C7, far_io, pg_psg_tone, ent_psg_tone, $C9
        dw 0

; logo_init: the routine at $C0BF. The register, CRAM and VRAM set-up of the
; logo screen; with buttons 1 and 2 held, the cart test (test) instead of the
; logo's name table cells. Returns with carry clear after the set-up, and with
; carry set after the test. AF, BC, DE, HL change, as in the game's routine;
; its caller sets every register it uses.
logo_init:
        push ix
        push iy
        ld hl,$CAEE             ; the jingle's data
        ld ($D7DD),hl
        ld hl,$CB4F
        ld ($D7DF),hl
        xor a
        ld ($D7DC),a
        ld hl,$C0A9             ; VDP registers 0 to 10 (22 control bytes)
        ld bc,$16BF
        rst $00
        db $B3                  ; OTIR
        xor a                   ; CRAM 0 to 3
        rst $00
        db $05                  ; OUT ($BF),A
        ld a,$C0
        rst $00
        db $05
        ld hl,$C9C2
        ld bc,$04BE
        rst $00
        db $B3
        ld a,$10                ; CRAM 16 to 19, the same 4 bytes
        rst $00
        db $05
        ld a,$C0
        rst $00
        db $05
        ld hl,$C9C2
        ld bc,$04BE
        rst $00
        db $B3
        ld de,$3F00             ; the sprite table: Y of sprites 0 and 1, then 0
        call vaddr
        ld a,$6F
        call vb
        ld a,$77
        call vb
        ld b,$7E
        xor a
.s1:    call vb
        djnz .s1
        ld a,$1E                ; X and tile of sprites 0 and 1, then 0
        ld ($D7D7),a
        call vb
        ld a,$5C
        call vb
        ld a,$28
        call vb
        ld a,$5C
        call vb
        ld b,$7F
        xor a
.s2:    call vb                 ; the last 3 go on at $0000
        djnz .s2
        ld de,$0000             ; tiles 0 to 40: rows $FF, 0, 0, 0
        call vaddr
        ld c,41
.t1:    ld b,8
.t1r:   ld a,$FF
        call vb
        xor a
        call vb
        call vb
        call vb
        djnz .t1r
        dec c
        jr nz,.t1
        ld hl,$C512             ; tiles 41 to 91: rows of 2 bytes from $C512, 0, 0
        ld c,51
.t2:    ld b,8                  ; the game's B = 24 counts its OUTIs too
.t2r:   ld a,(hl)
        inc hl
        call vb
        ld a,(hl)
        inc hl
        call vb
        xor a
        call vb
        call vb
        djnz .t2r
        dec c
        jr nz,.t2
        ld c,48                 ; tiles 92 to 139: rows of $FF, the next byte, 0, 0
.t3:    ld b,8                  ; the game's B = 16 counts its OUTIs too
.t3r:   ld a,$FF
        call vb
        ld a,(hl)
        inc hl
        call vb
        xor a
        call vb
        call vb
        djnz .t3r
        dec c
        jr nz,.t3
        ld de,$3800             ; the name table: tile $28 in front of sprites
        call vaddr
        ld c,24
.n1:    ld b,32
.n1c:   ld a,$28
        call vb
        ld a,$10
        call vb
        djnz .n1c
        dec c
        jr nz,.n1
        call vflush
        rst $00
        db $0E                  ; IN A,($DC)
        and $30
        jp z,test               ; buttons 1 and 2 held
        ld de,$3A4C             ; "CODEMASTERS": tiles 0, 2 ... 36
        call vaddr
        ld bc,$1300
.c1:    ld a,c
        call vb
        xor a
        call vb
        inc c
        inc c
        djnz .c1
        ld de,$3A8C             ; the row below: tiles 1, 3 ... 37
        call vaddr
        ld bc,$1301
.c2:    ld a,c
        call vb
        xor a
        call vb
        inc c
        inc c
        djnz .c2
        ld de,$3B8C             ; tiles $2A on, in front of sprites
        call vaddr
        ld bc,$142A
.c3:    ld a,c
        call vb
        ld a,$10
        call vb
        inc c
        djnz .c3
        ld de,$3BCC
        call vaddr
        ld b,$14
.c4:    ld a,c
        call vb
        ld a,$10
        call vb
        inc c
        djnz .c4
        ld de,$3C1E
        call vaddr
        ld a,c
        inc c
        call vb
        ld a,$10
        call vb
        ld a,c
        inc c
        call vb
        ld a,$10
        call vb
        ld c,$5E                ; the copyright lines: tiles $5E on
        ld de,$3D8C
        call vaddr
        ld b,$14
.c5:    ld a,c
        inc c
        call vb
        xor a
        call vb
        djnz .c5
        ld de,$3DD2
        call vaddr
        ld b,$0A
.c6:    ld a,c
        inc c
        call vb
        xor a
        call vb
        djnz .c6
        ld hl,$C510             ; two cells from $C510, then the digits of ($7FE3)
        ld b,2
.c7:    ld a,(hl)
        inc hl
        add a,c
        call vb
        xor a
        call vb
        djnz .c7
        ld a,($7FE3)
        ld b,a
        srl a
        srl a
        srl a
        srl a
        add a,c
        call vb
        xor a
        call vb
        ld a,b
        and $0F
        add a,c
        call vb
        xor a
        call vb
        call vflush
        ld hl,$D000             ; RAM $D000: 304 rows $FF, 0, 0, 0
        ld bc,$0130
.r:     ld (hl),$FF
        inc hl
        ld (hl),0
        inc hl
        ld (hl),0
        inc hl
        ld (hl),0
        inc hl
        dec bc
        ld a,b
        or c
        jr nz,.r
        ld a,$62                ; register 1 = $62: display on
        rst $00
        db $05
        ld a,$81
        rst $00
        db $05
        pop iy
        pop ix
        or a                    ; carry clear: the logo follows
        ret

; test: the cart test at $C26A. The game maps each bank into slot 2 and
; checks that its last byte is its number (banks 2 on), and adds up the cart
; in 16-bit words. On the Next the cart has the overlay's patches, so the sum
; is not the cart's; the loader has checked the cart's CRC32, so the sum is the
; header's ($7FE6), as the game finds for this dump. Then the screen: the sum,
; the 5 bytes from $7FE1, a bad bank's number, a face; on success CRAM 1 and 17
; = $0C, a wait for the buttons to come up and 256 frames, then the return as
; the game's JP $C050 (carry set); on failure CRAM $03, a PSG tone and a hang.
test:   xor a
        ld ($D7DA),a
        ld ($D7DB),a
        ld h,a
        ld l,a
        ld ($D7D8),hl
.bank:  ld a,($D7DA)
        rst $00
        db $2E, 0               ; LD ($8000),A: the bank into slot 2
        ld hl,$D7DA
        ld a,(hl)
        cp 2
        jr c,.nx
        ld a,($BFFF)
        cp (hl)
        jr z,.nx
        ld a,(hl)
        ld ($D7DB),a
        ld a,$FF
        ld ($D7DC),a
.nx:    inc (hl)
        ld b,(hl)
        ld a,($7FE0)            ; the number of banks
        cp b
        jr nz,.bank
        ld hl,($7FE6)
        ld ($D7D8),hl
        ld de,$3950
        call vaddr
        ld a,$88                ; "C" and the sum
        call vb
        xor a
        call vb
        ld a,($D7D9)
        call hexb
        ld a,($D7D8)
        call hex2
        ld hl,($D7D8)
        ld bc,($7FE6)
        or a
        sbc hl,bc
        jr z,.sum
        ld a,1
        ld ($D7DC),a
.sum:   ld de,$39D0
        call vaddr
        ld a,$89                ; "D" and the bytes from $7FE1
        call vb
        xor a
        call vb
        ld hl,$7FE1
        ld b,5
.d:     ld a,(hl)
        inc hl
        call hexb
        djnz .d
        ld a,($D7DB)
        and a
        jr z,.face
        ld de,$3A50
        call vaddr
        ld a,$87                ; a bad bank's number
        call vb
        xor a
        call vb
        ld a,($D7DB)
        call hexb
.face:  ld de,$3B1E
        call vaddr
        ld c,$54
        ld a,($D7DC)
        and a
        jr z,.f1
        ld c,$58
.f1:    ld a,c
        inc c
        call vb
        xor a
        call vb
        ld a,c
        inc c
        call vb
        xor a
        call vb
        ld de,$3B5E
        call vaddr
        ld a,c
        inc c
        call vb
        xor a
        call vb
        ld a,c
        call vb
        xor a
        call vb
        call vflush
        ld a,($D7DC)
        and a
        jr nz,.fail
        ld b,$0C
        call tcol
.up:    rst $00
        db $0E                  ; IN A,($DC)
        or $C0
        cp $FF
        jr nz,.up
        ld b,0
.w:     call vwait
        call v0wait
        djnz .w
        pop iy
        pop ix
        scf
        ret
.fail:  ld b,$03
        call tcol
        ld a,$8F
        rst $00
        db $02                  ; OUT ($7E),A
        ld a,$3F
        rst $00
        db $02
        ld a,$90
        rst $00
        db $02
.hang:  jr .hang

; CRAM 1 and 17 = B, then register 1 = $62.
tcol:   ld a,$01
        rst $00
        db $05
        ld a,$C0
        rst $00
        db $05
        ld a,b
        rst $00
        db $04                  ; OUT ($BE),A
        ld a,$11
        rst $00
        db $05
        ld a,$C0
        rst $00
        db $05
        ld a,b
        rst $00
        db $04
        ld a,$62
        rst $00
        db $05
        ld a,$81
        rst $00
        db $05
        ret

; hexb: the routine at $C084, a blank cell then hex2. hex2: the routine at
; $C08E, two cells with the hex digits of A (tiles $7C on). Use AF and AF'.
hexb:   ex af,af'
        ld a,$28
        call vb
        ld a,$10
        call vb
        ex af,af'
hex2:   push bc
        ld c,a
        and $F0
        rra
        rra
        rra
        rra
        add a,$7C
        call vb
        ld a,$10
        call vb
        ld a,c
        and $0F
        add a,$7C
        call vb
        ld a,$10
        call vb
        pop bc
        ret

; logo_end: the code from $C032 to the RET at $C050. A frame wait, one name
; table cell, then 150 frames. Returns A = 0, B = 0, Z set, as the game's loop;
; C, DE, HL kept.
logo_end:
        call vwait
        push de
        push ix
        push iy
        ld de,$3A72
        call vaddr
        ld a,$29
        call vb
        xor a
        call vb
        call vflush
        pop iy
        pop ix
        pop de
        ld b,$96
.w:     call vwait
        call v0wait
        djnz .w
        ret

; logo_out: the code from $C417 to the RET at $C441. In: HL = the 192 bytes of
; pattern, DE = their VRAM address ($4000 set). A frame wait, sprites 0 and 1
; one step on (the byte at $D7D7), then the 192 bytes. Returns as the game's
; OTIR leaves it: HL past the bytes, B = 0, C = $BE, A = D, Z set; DE kept.
logo_out:
        call vwait
        push hl
        push de
        ld a,($D7D7)
        add a,2
        ld ($D7D7),a
        ld (spr),a
        sub 2
        ld (spr+2),a
        ld a,$5C
        ld (spr+1),a
        ld hl,spr
        ld de,$3F80
        ld bc,$0301             ; 3 bytes, 1 run
        ld a,1                  ; the source in this page
        call jt_vwrite
        pop de
        pop hl
        ld bc,$C001             ; 192 bytes, 1 run
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld bc,$00C0
        add hl,bc
        ld c,$BE
        ld b,0
        ld a,d
        cp a
        ret

; psg_off: the code from $CA99 to the RET at $CAA9: the four volumes off.
psg_off:
        ld a,$9F
        rst $00
        db $02
        ld a,$BF
        rst $00
        db $02
        ld a,$DF
        rst $00
        db $02
        ld a,$FF
        rst $00
        db $02
        ret

; psg_vol: the code from $CAB1 to the RET at $CAC9: three volumes from the
; jingle data at ($D7DF).
psg_vol:
        ld hl,($D7DF)
        ld a,(hl)
        or $90
        rst $00
        db $02
        inc hl
        ld ($D7DF),hl
        ld a,(hl)
        or $B0
        rst $00
        db $02
        inc hl
        ld a,(hl)
        or $D0
        rst $00
        db $02
        inc hl
        ret

; psg_tone: the routine at $CACA. A = the note, E = the channel's latch bits;
; the tone from the table at $CBB1.
psg_tone:
        push hl
        add a,a
        ld c,a
        ld b,0
        ld hl,$CBB1
        add hl,bc
        ld a,(hl)
        ld b,a
        inc hl
        ld c,(hl)
        rla
        rl c
        rla
        rl c
        rla
        rl c
        rla
        rl c
        ld a,b
        and $0F
        or e
        rst $00
        db $02
        ld a,c
        rst $00
        db $02
        pop hl
        ret

; tile_up: the code from $7F23 to its RET at $7F45. Rows of 4 bytes from the VDP
; address: the bytes at $C000, $C800 and $D000 on, and a 0, until HL reaches
; ($DF1C) * 256. One jt_vwrite call for each of the 4 bytes of 256 rows. Returns
; as the game's loop leaves it: HL = $C000, BC = $C800, DE = $D000, each plus the
; rows, A = 0, Z set. Interrupts stay as they are.
tile_up:
        push ix
        push iy
        ld hl,(vdp_addr)
        ld a,h
        and $3F
        ld h,a
        ld (tu_v),hl            ; the VRAM address of the first row
        ld a,($DF1C)
        sub $C0
        ld (tu_n),a             ; chunks of 256 rows
        ld hl,$C000
.ch:    push hl
        ld bc,$0100             ; 1 byte a run, 256 runs
        ld iy,4                 ; the next row's byte, 4 VRAM bytes on
        ld ix,1
        ld de,(tu_v)
        xor a                   ; the source as the game sees it
        call jt_vwrite          ; the bytes from $C000
        ld a,h
        add a,8
        ld h,a
        inc de
        xor a
        call jt_vwrite          ; from $C800
        ld a,h
        add a,8
        ld h,a
        inc de
        xor a
        call jt_vwrite          ; from $D000
        ld hl,tu_z
        ld ix,0
        inc de
        ld a,1                  ; the 0 in this page
        call jt_vwrite
        ld hl,(tu_v)            ; the next 256 rows: 1K of VRAM on
        ld a,h
        add a,4
        and $3F
        ld h,a
        ld (tu_v),hl
        pop hl
        inc h
        ld a,(tu_n)
        dec a
        ld (tu_n),a
        jr nz,.ch
        ld b,h                  ; HL = $C000 + rows
        ld c,l
        ld a,b
        add a,8
        ld b,a                  ; BC = $C800 + rows
        ld d,h
        ld e,l
        ld a,d
        add a,$10
        ld d,a                  ; DE = $D000 + rows
        pop iy
        pop ix
        xor a                   ; A = 0, Z set
        ret
tu_v:   dw 0
tu_n:   db 0
tu_z:   db 0

; A frame wait: the routine at $C051, the V counter in $C0-$CF. Keeps AF.
vwait:  push af
.l:     rst $00
        db $0A                  ; IN A,($7E)
        cp $C0
        jr c,.l
        cp $D0
        jr nc,.l
        pop af
        ret

; The V counter at 0. Returns A = 0, Z set.
v0wait: rst $00
        db $0A
        and a
        jr nz,v0wait
        ret

; VRAM writes collect in vbuf and go out through jt_vwrite. vaddr: DE = the
; VRAM address of the next byte (bits 14 and 15 ignored). vb: A = the next data
; byte. vflush: writes what has collected. All keep every register but F.
vaddr:  call vflush
        push af
        ld a,d
        and $3F
        ld (vadr+1),a
        ld a,e
        ld (vadr),a
        pop af
        ret

vb:     push af
        push hl
        push de
        ld hl,(vcnt)
        ld de,vbuf
        add hl,de
        ld (hl),a
        ld hl,(vcnt)
        inc hl
        ld (vcnt),hl
        ld de,(vadr)
        add hl,de               ; the VRAM address past this byte
        bit 6,h
        jr nz,.fl               ; $4000: write now, then go on at $0000
        ld a,(vcnt+1)
        cp 4                    ; 1024 bytes
        jr c,.ok
.fl:    call vflush
.ok:    pop de
        pop hl
        pop af
        ret

vflush: push af
        push bc
        push de
        push hl
        push ix
        push iy
        ld hl,(vcnt)
        ld a,h
        or l
        jr z,.x
        ld de,(vadr)
        ld c,h                  ; whole runs of 256
        ld b,0
        ld hl,vbuf
        ld ix,256
        ld iy,256
        ld a,c
        or a
        jr z,.part
        ld a,1                  ; the source in this page
        call jt_vwrite          ; keeps BC, DE, HL, IX, IY
        ld a,h
        add a,c
        ld h,a
        ld a,d
        add a,c
        and $3F
        ld d,a
.part:  ld a,(vcnt)             ; the bytes left
        or a
        jr z,.adv
        ld b,a
        ld c,1
        ld a,1
        call jt_vwrite
.adv:   ld hl,(vadr)
        ld de,(vcnt)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (vadr),hl
        ld hl,0
        ld (vcnt),hl
.x:     pop iy
        pop ix
        pop hl
        pop de
        pop bc
        pop af
        ret

spr:    ds 3
vadr:   dw 0
vcnt:   dw 0
vbuf:   ds 1024
endpage
