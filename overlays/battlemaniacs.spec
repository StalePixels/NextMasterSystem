# Battlemaniacs (Brazil) (En), CRC32 1CBB7BF1, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a 600 s reference I/O log.
#
# Decisions:
# - The start-up clear at $3096 (LD HL,$C500; LD BC,$1BFF; LDIR) runs to $E0FF. On a Master
#   System $E000-$E0FF is the mirror of $C000-$C0FF; on the Next it is the runtime's page, and
#   the clear wiped it. The cave at $0153 ($FF fill) clears $C500-$DFFF and then $C000-$C0FF,
#   as the mirror did. It is entered and left with JP: the clear covers the game's stack.
#   The 600 s reference log shows no other store into $E000-$FFFB.
# - Delay $0D2E (B units, 0 means 256, of a 16 x 256-pass NOP; DJNZ loop, the same bytes as The
#   Lion King's $0F78): a busy loop of 70,615 T-states a unit with the frame handler that cuts into
#   it (measured on the reference: 50 units in 3,530,756 T), 19.73 ms at 3.58 MHz. The copyright,
#   trademark, Virgin and title screens and the intro pages are timed with it. At 28 MHz the loop
#   ran about 8 times too fast: the Next skipped from the copyright screen to the intro and never
#   showed the title. Page entry delay waits the Master System's real time on the Next's raster
#   line: 312 lines a unit at 60 Hz (307 at 50 Hz) with interrupts on, 3 fewer with them off.
# - Power-on delay $025F-$026B (LD B,4 : LD HL,$FFFF : DEC HL ... DJNZ): 4 x 65,535 passes of 24
#   T-states with interrupts off, 1.76 s on the reference. It runs as 90 units of the delay entry
#   with interrupts off and leaves B, HL and A at 0, as the loop does.
# - The io vector is $08 ($FF fill; the game uses only RST $38). The game's LD ($0007),A between
#   VDP writes are delays that write the cart area; they change the cart copy's byte at $0007,
#   which no code runs, and stay as they are.
# - Fighter art ($0B8C, from the cart into the sprite tiles at $2000-$29FF) and the sprite table
#   ($03E4, in the main loop after it waits for V counter $C0) reach the Next's screen at the
#   once-a-frame work that follows them, which comes after the game's whole write in each frame,
#   so each picture pairs table and art as a Master System picture does. No overlay change.
# - No tilecache: measured with and without, play had 9 and 13 frames over 100% (worst 107% and
#   111%), for 1.1 s more loading.
# - Spec gaps (data/scan-verdicts.tsv): unused are the bank 0 routines $054F, $0B6F and $0DB6
#   and the sound driver's own interrupt entry at bank 3 $9463; false are the byte patterns in
#   graphics banks 7, 9, 10 and 13.
name Battlemaniacs
cart 1CBB7BF1
hz 60		; No-Intro region Brazil
vector 08 io
asm 0309C 7   ; LD BC,$1BFF; LD (HL),$00; LDIR: the clear of $C500-$E0FF
    jp $0153
    nop
    nop
    nop
    nop
endasm
asm 00153 23  ; $FF fill: the clear of $C500-$DFFF, then of $C000-$C0FF (the mirror's part)
    ld bc,$1AFF
    ld (hl),0
    ldir
    ld hl,$C000
    ld de,$C001
    ld bc,$00FF
    ld (hl),0
    ldir
    jp $30A3
endasm
asm 0025F 13  ; LD B,4 : LD HL,$FFFF : DEC HL : LD A,L : OR H : JP NZ : DJNZ
    ld b,90
    rst $08
    db far_io, pg_delay, ent_delay
    ld b,0
    ld hl,0
    xor a
endasm
asm 00D2E 5   ; PUSH BC : PUSH HL : LD H,B : LD C,$10
    rst $08
    db far_io, pg_delay, ent_delay
    ret
endasm
asm 00279 2   ; IM 1 -> IM 2
    im 2
endasm
site 00232   ; OTIR
site 00245   ; OUT ($3E),A
site 00249   ; OUT ($3F),A
site 00285   ; OUT ($BF),A
site 0028D   ; OUT ($BF),A
site 00298   ; OUT ($BF),A
site 002A0   ; OUT ($BF),A
site 002AE   ; OUT (C),E
site 002B4   ; OUT (C),D
site 002BB   ; OUT (C),A
site 002ED   ; OUT ($BF),A
site 002F5   ; OUT ($BF),A
site 002FF   ; OUT ($BF),A
site 00307   ; OUT ($BF),A
site 00311   ; OUT ($BF),A
site 00319   ; OUT ($BF),A
site 00323   ; OUT ($BF),A
site 0032B   ; OUT ($BF),A
site 00335   ; OUT ($BF),A
site 0033D   ; OUT ($BF),A
site 00347   ; OUT ($BF),A
site 0034F   ; OUT ($BF),A
site 00359   ; OUT ($BF),A
site 00361   ; OUT ($BF),A
site 0036B   ; OUT ($BF),A
site 00373   ; OUT ($BF),A
site 0037D   ; OUT ($BF),A
site 00385   ; OUT ($BF),A
site 0038F   ; OUT ($BF),A
site 00397   ; OUT ($BF),A
site 003A1   ; OUT ($BF),A
site 003A9   ; OUT ($BF),A
site 003B9   ; OUT ($BF),A
site 003C0   ; OUT ($BF),A
site 003C7   ; OUT ($BE),A
site 003CA   ; OUT ($BF),A
site 003D1   ; OUT ($BF),A
site 003DA   ; OUT ($BE),A
site 003FA   ; OUT ($BF),A
site 00401   ; OUT ($BF),A
site 0040D   ; OUT (C),A
site 00419   ; OUT ($BF),A
site 00420   ; OUT ($BF),A
site 0042E   ; OUT (C),A
site 00434   ; OUT (C),A
site 00449   ; IN A,($BF)
site 00457   ; IN A,($DD)
site 0048D   ; IN A,($7E)
site 004CE   ; OUT (C),A
site 004D8   ; OUT (C),B
site 004ED   ; OUT ($BF),A
site 004F5   ; OUT ($BF),A
site 004FF   ; OUT ($BF),A
site 00507   ; OUT ($BF),A
site 00514   ; OUT (C),L
site 0051A   ; OUT (C),H
site 00521   ; OUT (C),A
site 0052C   ; OUT (C),L
site 00532   ; OUT (C),H
site 0053C   ; OUT (C),E
site 00542   ; OUT (C),D
site 00573   ; IN A,($DC)
site 0057B   ; IN A,($DC)
site 00583   ; IN A,($DC)
site 0058B   ; IN A,($DC)
site 00593   ; IN A,($DC)
site 0059B   ; IN A,($DC)
site 0063F   ; IN A,($DD)
site 00647   ; IN A,($DD)
site 0064F   ; IN A,($DC)
site 00657   ; IN A,($DC)
site 0065F   ; IN A,($DD)
site 00667   ; IN A,($DD)
site 006AA   ; OUT (C),E
site 006B1   ; OUT (C),D
site 006B7   ; OUTI
site 00712   ; OUT (C),A
site 0071A   ; OUT (C),B
site 00723   ; OUT (C),A
site 0072B   ; OUT (C),B
site 008F1   ; OUT ($BF),A
site 008F9   ; OUT ($BF),A
site 008FF   ; OUT ($BE),A
site 00904   ; OUT ($BE),A
site 00972   ; OUT (C),A
site 00977   ; OUT (C),A
site 00983   ; OUT (C),L
site 0098A   ; OUT (C),A
site 00990   ; OUT (C),A
site 00995   ; OUT (C),A
site 009C2   ; OUT (C),E
site 009C9   ; OUT (C),D
site 009D1   ; OUT (C),A
site 00B64   ; OUT ($BF),A
site 00B6C   ; OUT ($BF),A
site 00B8F   ; OUT (C),E
site 00B95   ; OUT (C),D
site 00B9A   ; OUTI
site 00BBA   ; OUT (C),E
site 00BC0   ; OUT (C),D
site 00BC8   ; OUT ($BE),A
site 00BCD   ; OUT ($BE),A
site 00BD2   ; OUT ($BE),A
site 00BD7   ; OUT ($BE),A
site 00BDC   ; OUT ($BE),A
site 00BE1   ; OUT ($BE),A
site 00BE6   ; OUT ($BE),A
site 00BEB   ; OUT ($BE),A
site 00BF0   ; OUT ($BE),A
site 00BF5   ; OUT ($BE),A
site 00BFA   ; OUT ($BE),A
site 00BFF   ; OUT ($BE),A
site 00C04   ; OUT ($BE),A
site 00C09   ; OUT ($BE),A
site 00C0E   ; OUT ($BE),A
site 00C13   ; OUT ($BE),A
site 00C18   ; OUT ($BE),A
site 00C1D   ; OUT ($BE),A
site 00C22   ; OUT ($BE),A
site 00C27   ; OUT ($BE),A
site 00C2C   ; OUT ($BE),A
site 00C31   ; OUT ($BE),A
site 00C36   ; OUT ($BE),A
site 00C3B   ; OUT ($BE),A
site 00C40   ; OUT ($BE),A
site 00C45   ; OUT ($BE),A
site 00C4A   ; OUT ($BE),A
site 00C4F   ; OUT ($BE),A
site 00C54   ; OUT ($BE),A
site 00C59   ; OUT ($BE),A
site 00C5E   ; OUT ($BE),A
site 00C63   ; OUT ($BE),A
site 00D51   ; OUT ($BF),A
site 00D59   ; OUT ($BF),A
site 00D66   ; OUT (C),A
site 00D6F   ; OUT (C),A
site 00D85   ; OUT ($BF),A
site 00D8D   ; OUT ($BF),A
site 00D9D   ; OUT (C),A
site 00DA4   ; OUT (C),A
site 00E10   ; OUT (C),L
site 00E17   ; OUT (C),H
site 00E22   ; OUTI
site 00E2C   ; OUTI
site 00E7A   ; IN A,($DC)
site 00E81   ; IN A,($DD)
site 00E88   ; IN A,($DC)
site 00E92   ; IN A,($DD)
site 00FCA   ; IN A,($7E)
site 014C3   ; OUT (C),L
site 014CA   ; OUT (C),H
site 01517   ; OUT (C),E
site 01590   ; OUT ($BF),A
site 01599   ; OUT ($BF),A
site 015BA   ; OUT ($BE),A
site 0162E   ; OUT (C),E
site 01635   ; OUT (C),D
site 01656   ; OUT (C),A
site 0165B   ; OUT (C),A
site 01660   ; OUT (C),A
site 01665   ; OUT (C),A
site 0176D   ; OUT ($BF),A
site 01775   ; OUT ($BF),A
site 0177B   ; OUT ($BE),A
site 01780   ; OUT ($BE),A
site 01792   ; OUT ($BF),A
site 0179A   ; OUT ($BF),A
site 017A0   ; OUT ($BE),A
site 017A5   ; OUT ($BE),A
site 0180E   ; OUT ($BF),A
site 01817   ; OUT ($BF),A
site 01821   ; OUT ($BE),A
site 01A0F   ; OUT ($BF),A
site 01A17   ; OUT ($BF),A
site 01A22   ; OUT ($BE),A
site 01A27   ; OUT ($BE),A
site 01A2C   ; OUT ($BE),A
site 01A31   ; OUT ($BE),A
site 01A36   ; OUT ($BE),A
site 01A3B   ; OUT ($BE),A
site 01A40   ; OUT ($BE),A
site 01A45   ; OUT ($BE),A
site 01A4A   ; OUT ($BE),A
site 01A4F   ; OUT ($BE),A
site 01A54   ; OUT ($BE),A
site 01A59   ; OUT ($BE),A
site 01A5E   ; OUT ($BE),A
site 01A63   ; OUT ($BE),A
site 01A68   ; OUT ($BE),A
site 01A6D   ; OUT ($BE),A
site 01A72   ; OUT ($BE),A
site 01A77   ; OUT ($BE),A
site 01A7C   ; OUT ($BE),A
site 01A81   ; OUT ($BE),A
site 01A86   ; OUT ($BE),A
site 01A8B   ; OUT ($BE),A
site 01A90   ; OUT ($BE),A
site 01A95   ; OUT ($BE),A
site 01A9A   ; OUT ($BE),A
site 01A9F   ; OUT ($BE),A
site 01AA4   ; OUT ($BE),A
site 01AA9   ; OUT ($BE),A
site 01AAE   ; OUT ($BE),A
site 01AB3   ; OUT ($BE),A
site 01AB8   ; OUT ($BE),A
site 01ABD   ; OUT ($BE),A
site 01B28   ; OUT ($BF),A
site 01B32   ; OUT ($BF),A
site 01B3B   ; OUT ($BE),A
site 031D0   ; IN A,($7E)
site 031D8   ; IN A,($7E)
site 032E5   ; OUT ($BF),A
site 032ED   ; OUT ($BF),A
site 032F7   ; OUT ($BF),A
site 032FF   ; OUT ($BF),A
site 03309   ; OUT ($BF),A
site 03311   ; OUT ($BF),A
site 0364F   ; IN A,($DC)
site 0365F   ; IN A,($DC)
site 03669   ; IN A,($DC)
site 03679   ; IN A,($DC)
site 03683   ; IN A,($DC)
site 03693   ; IN A,($DC)
site 0369D   ; IN A,($DC)
site 036AD   ; IN A,($DC)
site 0370B   ; OUT ($BF),A
site 03713   ; OUT ($BF),A
site 0373D   ; OUT ($BF),A
site 03745   ; OUT ($BF),A
site 03A30   ; OUT ($BF),A
site 03A38   ; OUT ($BF),A
site 0545D   ; OUT (C),L
site 05463   ; OUT (C),H
site 0546B   ; OUT (C),A
site 05471   ; OUT (C),E
site 05493   ; OUT (C),D
site 05499   ; OUT (C),E
site 054A7   ; OUT (C),L
site 054AD   ; OUT (C),H
site 054B5   ; OUT (C),A
site 054BB   ; OUT (C),E
site 054D6   ; OUT (C),L
site 054DC   ; OUT (C),H
site 054E6   ; OUT (C),A
site 054EC   ; OUT (C),A
site 05591   ; OUT ($BF),A: in $557D, which $3111 and $3737 call with bank 1 in slot 1
site 05599   ; OUT ($BF),A: in $557D
site 055AF   ; OUT ($BF),A
site 055B7   ; OUT ($BF),A
site 055C4   ; OUT (C),L
site 055CA   ; OUT (C),H
site 055D6   ; OUT (C),L
site 055DC   ; OUT (C),H
site 055FF   ; OUT (C),L
site 05605   ; OUT (C),H
site 05611   ; OUT (C),A
site 05618   ; OUT (C),B
site 0561F   ; OUT (C),A
site 05627   ; OUT (C),L
site 0562D   ; OUT (C),H
site 05634   ; OUT (C),A
site 0563A   ; OUT (C),B
site 05641   ; OUT (C),A
site 057B7   ; OUT (C),L
site 057BD   ; OUT (C),H
site 057C4   ; OUT (C),E
site 057CA   ; OUT (C),D
site 0BC02   ; OUT ($BF),A
site 0BC07   ; OUT ($BF),A
site 0BC76   ; OUT ($BE),A
site 0BC96   ; OUT ($BE),A
site 0D1D7   ; OUT ($7F),A
site 0D1DB   ; OUT ($7F),A
site 0D1E8   ; OUT ($7F),A
site 0D1EC   ; OUT ($7F),A
site 0D21D   ; OUT ($7F),A
site 0D234   ; OUT ($7F),A
site 0D241   ; OUT ($7F),A
site 0D250   ; OUT ($7F),A
site 0D267   ; OUT ($7F),A
site 0D274   ; OUT ($7F),A
site 0D29A   ; OUT ($7F),A
site 0D2AD   ; OUT ($7F),A
site 0D2C4   ; OUT ($7F),A
site 0D2CA   ; OUT ($7F),A
site 0D2EE   ; OUT ($7F),A
site 0D305   ; OUT ($7F),A
site 0D312   ; OUT ($7F),A
site 0D36F   ; OUT ($7F),A
site 0D4D8   ; OUT ($7F),A
site 0D4DD   ; OUT ($7F),A
site 0D4F1   ; OUT ($7F),A
site 0D504   ; OUT ($7F),A
site 0D510   ; OUT ($7F),A
site 0D523   ; OUT ($7F),A
mapst 0006B   ; LD ($FFFE),A
mapst 00073   ; LD ($FFFE),A
mapst 0024C   ; LD ($FFFC),A
mapst 0024F   ; LD ($FFFD),A
mapst 00254   ; LD ($FFFE),A
mapst 00259   ; LD ($FFFF),A
mapst 0046B   ; LD ($FFFF),A
mapst 00472   ; LD ($FFFF),A
mapst 005C3   ; LD ($FFFF),A
mapst 006E5   ; LD ($FFFF),A
mapst 006EF   ; LD ($FFFF),A
mapst 009B8   ; LD ($FFFF),A
mapst 009DE   ; LD ($FFFF),A
mapst 00B7A   ; LD ($FFFF),A
mapst 00BA5   ; LD ($FFFF),A
mapst 00F44   ; LD ($FFFF),A
mapst 00F83   ; LD ($FFFF),A
mapst 01360   ; LD ($FFFF),A
mapst 01403   ; LD ($FFFF),A
mapst 01523   ; LD ($FFFF),A
mapst 0153A   ; LD ($FFFF),A
mapst 01574   ; LD ($FFFF),A
mapst 015A1   ; LD ($FFFF),A
mapst 015B5   ; LD ($FFFF),A
mapst 01603   ; LD ($FFFF),A
mapst 01625   ; LD ($FFFF),A
mapst 01740   ; LD ($FFFF),A
mapst 017EC   ; LD ($FFFF),A
mapst 02B8C   ; LD ($FFFF),A
mapst 02C23   ; LD ($FFFF),A
mapst 02D60   ; LD ($FFFF),A
mapst 02F75   ; LD ($FFFF),A
mapst 03236   ; LD ($FFFF),A
mapst 0346D   ; LD ($FFFF),A
mapst 0350F   ; LD ($FFFF),A
mapst 0358C   ; LD ($FFFF),A
mapst 036B6   ; LD ($FFFF),A
mapst 03728   ; LD ($FFFF),A
mapst 038F2   ; LD ($FFFF),A
mapst 03910   ; LD ($FFFF),A
mapst 03937   ; LD ($FFFF),A
mapst 0394B   ; LD ($FFFF),A
mapst 0395B   ; LD ($FFFF),A
mapst 039E2   ; LD ($FFFF),A
mapst 03A94   ; LD ($FFFF),A
mapst 03AA2   ; LD ($FFFF),A
mapst 03B90   ; LD ($FFFF),A
mapst 03BC4   ; LD ($FFFF),A
mapst 03BFE   ; LD ($FFFF),A
mapst 03C0C   ; LD ($FFFF),A
mapst 03C3B   ; LD ($FFFF),A
mapst 03C83   ; LD ($FFFF),A
mapst 03D85   ; LD ($FFFF),A
mapst 03EEB   ; LD ($FFFF),A
mapst 03F92   ; LD ($FFFF),A
mapst 03FFC   ; LD ($FFFF),A
mapst 04008   ; LD ($FFFF),A
mapst 04031   ; LD ($FFFF),A
mapst 0406B   ; LD ($FFFF),A
mapst 04079   ; LD ($FFFF),A
mapst 04097   ; LD ($FFFF),A
mapst 040CF   ; LD ($FFFF),A
mapst 048B5   ; LD ($FFFF),A
mapst 04FF1   ; LD ($FFFF),A
mapst 051B2   ; LD ($FFFF),A
mapst 051C2   ; LD ($FFFF),A
mapst 051D2   ; LD ($FFFF),A
mapst 05207   ; LD ($FFFF),A
mapst 0526B   ; LD ($FFFF),A
mapst 0527E   ; LD ($FFFF),A
mapst 0528E   ; LD ($FFFF),A
mapst 052F1   ; LD ($FFFF),A
mapst 05311   ; LD ($FFFF),A
mapst 05321   ; LD ($FFFF),A
mapst 05345   ; LD ($FFFF),A
mapst 0538A   ; LD ($FFFF),A
mapst 053B2   ; LD ($FFFF),A
mapst 053F0   ; LD ($FFFF),A
mapst 058F5   ; LD ($FFFF),A
mapst 0646B   ; LD ($FFFF),A
mapst 06480   ; LD ($FFFF),A
mapst 06490   ; LD ($FFFF),A
mapst 06519   ; LD ($FFFF),A
mapst 0656E   ; LD ($FFFF),A
mapst 065A1   ; LD ($FFFF),A
mapst 065D6   ; LD ($FFFF),A
mapst 067D1   ; LD ($FFFF),A
mapst 067F5   ; LD ($FFFF),A
mapst 06A39   ; LD ($FFFF),A
mapst 06A6A   ; LD ($FFFF),A
mapst 06D44   ; LD ($FFFF),A
mapst 06D50   ; LD ($FFFF),A
mapst 06D5B   ; LD ($FFFF),A
mapst 06D67   ; LD ($FFFF),A
mapst 06D6D   ; LD ($FFFF),A
# CHECK cartarea_store at 002B1 ($02B1 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 003BB ($03BB bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 003C4 ($03C4 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 003CC ($03CC bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 003D6 ($03D6 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00517 ($0517 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0052F ($052F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0053F ($053F bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00544 ($0544 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00714 ($0714 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00717 ($0717 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0071C ($071C bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00725 ($0725 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00728 ($0728 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 009C5 ($09C5 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 009CC ($09CC bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00B66 ($0B66 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00D55 ($0D55 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00D5D ($0D5D bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00D6C ($0D6C bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00D89 ($0D89 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00D91 ($0D91 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00E12 ($0E12 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00E1A ($0E1A bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 00E27 ($0E27 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 014C7 ($14C7 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01B2A ($1B2A bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01B2D ($1B2D bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01B34 ($1B34 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01B37 ($1B37 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01B3D ($1B3D bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 01B40 ($1B40 bank 0): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05460 ($5460 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0546E ($546E bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05496 ($5496 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 054AA ($54AA bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 054B8 ($54B8 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 054D9 ($54D9 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 055C7 ($55C7 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 055CD ($55CD bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 055D9 ($55D9 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05602 ($5602 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05608 ($5608 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05614 ($5614 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0561C ($561C bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0562A ($562A bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05630 ($5630 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 05637 ($5637 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 0563E ($563E bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 057BA ($57BA bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 057C0 ($57C0 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK cartarea_store at 057C7 ($57C7 bank 1): 32 07 00  LD ($0007),A $0007
# CHECK indirect_unresolved at 01B8B ($1B8B bank 0): CD 72 2F  CALL $2F72 
# CHECK indirect_unresolved at 05E9A ($5E9A bank 1): CD 72 2F  CALL $2F72 
# CHECK indirect_unresolved at 0BF67 ($7F67 bank 2): C9  RET 
# CHECK bank_unresolved at 01B8E ($1B8E bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 01C03 ($1C03 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 01C21 ($1C21 bank 0): CD 89 6C  CALL $6C89 $6C89
# CHECK bank_unresolved at 01C70 ($1C70 bank 0): CD EC 50  CALL $50EC $50EC
# CHECK bank_unresolved at 01C92 ($1C92 bank 0): CD 77 50  CALL $5077 $5077
# CHECK bank_unresolved at 01CFE ($1CFE bank 0): C4 90 60  CALL NZ,$6090 $6090
# CHECK bank_unresolved at 01F0C ($1F0C bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 01F25 ($1F25 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 01F43 ($1F43 bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 01FDD ($1FDD bank 0): CD B9 6A  CALL $6AB9 $6AB9
# CHECK bank_unresolved at 0202C ($202C bank 0): D4 6D 4D  CALL NC,$4D6D $4D6D
# CHECK bank_unresolved at 0206E ($206E bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 020CC ($20CC bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 02107 ($2107 bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 0214D ($214D bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 0224C ($224C bank 0): CD EC 50  CALL $50EC $50EC
# CHECK bank_unresolved at 02275 ($2275 bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 022C0 ($22C0 bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 02304 ($2304 bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 02404 ($2404 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02420 ($2420 bank 0): CD 5F 6C  CALL $6C5F $6C5F
# CHECK bank_unresolved at 0246D ($246D bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02495 ($2495 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 024FD ($24FD bank 0): CD 2C 6B  CALL $6B2C $6B2C
# CHECK bank_unresolved at 02551 ($2551 bank 0): CC 4D 60  CALL Z,$604D $604D
# CHECK bank_unresolved at 02598 ($2598 bank 0): CD 1A 51  CALL $511A $511A
# CHECK bank_unresolved at 025D7 ($25D7 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 025E9 ($25E9 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02620 ($2620 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 0263E ($263E bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 0264C ($264C bank 0): CD E0 6A  CALL $6AE0 $6AE0
# CHECK bank_unresolved at 02674 ($2674 bank 0): CD 24 4D  CALL $4D24 $4D24
# CHECK bank_unresolved at 0269C ($269C bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 026A7 ($26A7 bank 0): CC 6D 4D  CALL Z,$4D6D $4D6D
# CHECK bank_unresolved at 026B8 ($26B8 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02793 ($2793 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02966 ($2966 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 0299A ($299A bank 0): CD 79 6B  CALL $6B79 $6B79
# CHECK bank_unresolved at 029D3 ($29D3 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02C3C ($2C3C bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02C64 ($2C64 bank 0): CD 34 57  CALL $5734 $5734
# CHECK bank_unresolved at 02CAB ($2CAB bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02CC6 ($2CC6 bank 0): CD 34 57  CALL $5734 $5734
# CHECK bank_unresolved at 02CD5 ($2CD5 bank 0): CD 3D 6D  CALL $6D3D $6D3D
# CHECK bank_unresolved at 02CDC ($2CDC bank 0): CD EE 56  CALL $56EE $56EE
# CHECK bank_unresolved at 02CFC ($2CFC bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02D58 ($2D58 bank 0): CD 6D 4D  CALL $4D6D $4D6D
# CHECK bank_unresolved at 02F94 ($2F94 bank 0): CD C8 56  CALL $56C8 $56C8
# CHECK bank_unresolved at 03107 ($3107 bank 0): CD D1 50  CALL $50D1 $50D1
# CHECK bank_unresolved at 03111 ($3111 bank 0): CD 7D 55  CALL $557D $557D
# CHECK bank_unresolved at 0312D ($312D bank 0): CD D1 50  CALL $50D1 $50D1
# CHECK bank_unresolved at 03165 ($3165 bank 0): CD 1E 6D  CALL $6D1E $6D1E
# CHECK bank_unresolved at 03168 ($3168 bank 0): CD D0 51  CALL $51D0 $51D0
# CHECK bank_unresolved at 0319B ($319B bank 0): CD 3F 4E  CALL $4E3F $4E3F
# CHECK bank_unresolved at 0319E ($319E bank 0): CD D3 4D  CALL $4DD3 $4DD3
# CHECK bank_unresolved at 03216 ($3216 bank 0): CD DD 40  CALL $40DD $40DD
# CHECK bank_unresolved at 0321C ($321C bank 0): CD 14 48  CALL $4814 $4814
# CHECK bank_unresolved at 0321F ($321F bank 0): CD 85 58  CALL $5885 $5885
# CHECK bank_unresolved at 03222 ($3222 bank 0): CD F6 5F  CALL $5FF6 $5FF6
# CHECK bank_unresolved at 03231 ($3231 bank 0): CD 33 54  CALL $5433 $5433
# CHECK bank_unresolved at 0323C ($323C bank 0): CD F0 61  CALL $61F0 $61F0
# CHECK bank_unresolved at 032B6 ($32B6 bank 0): CD 6B 6D  CALL $6D6B $6D6B
# CHECK bank_unresolved at 0333A ($333A bank 0): CD 54 6D  CALL $6D54 $6D54
# CHECK bank_unresolved at 033AC ($33AC bank 0): CD 54 6D  CALL $6D54 $6D54
# CHECK bank_unresolved at 03409 ($3409 bank 0): CD 27 4E  CALL $4E27 $4E27
# CHECK bank_unresolved at 035A0 ($35A0 bank 0): C4 7C 6E  CALL NZ,$6E7C $6E7C
# CHECK bank_unresolved at 03737 ($3737 bank 0): CD 7D 55  CALL $557D $557D
# CHECK bank_unresolved at 03876 ($3876 bank 0): CD 34 57  CALL $5734 $5734
# CHECK bank_unresolved at 03889 ($3889 bank 0): CD C8 56  CALL $56C8 $56C8
# CHECK bank_unresolved at 0388C ($388C bank 0): CD 33 54  CALL $5433 $5433
# CHECK bank_unresolved at 03984 ($3984 bank 0): CD E7 57  CALL $57E7 $57E7
# CHECK bank_unresolved at 0398B ($398B bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 0398E ($398E bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 03991 ($3991 bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 039A1 ($39A1 bank 0): CD E7 57  CALL $57E7 $57E7
# CHECK bank_unresolved at 039A4 ($39A4 bank 0): CD 2A 58  CALL $582A $582A
# CHECK bank_unresolved at 039B3 ($39B3 bank 0): CD E7 57  CALL $57E7 $57E7
# CHECK bank_unresolved at 039B6 ($39B6 bank 0): CD 2A 58  CALL $582A $582A
# CHECK bank_unresolved at 03C60 ($3C60 bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 03D21 ($3D21 bank 0): CD E7 57  CALL $57E7 $57E7
# CHECK bank_unresolved at 03D26 ($3D26 bank 0): CD AB 57  CALL $57AB $57AB
# CHECK bank_unresolved at 03D32 ($3D32 bank 0): CD E7 57  CALL $57E7 $57E7
# CHECK bank_unresolved at 03D37 ($3D37 bank 0): CD AB 57  CALL $57AB $57AB
# CHECK bank_unresolved at 03D47 ($3D47 bank 0): CD 3D 6D  CALL $6D3D $6D3D
# CHECK bank_unresolved at 03D80 ($3D80 bank 0): CD E7 57  CALL $57E7 $57E7
# CHECK bank_unresolved at 03D8C ($3D8C bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 03D8F ($3D8F bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 03D92 ($3D92 bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 03D95 ($3D95 bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 03D98 ($3D98 bank 0): CD 90 57  CALL $5790 $5790
# CHECK bank_unresolved at 03D9B ($3D9B bank 0): CD 90 57  CALL $5790 $5790
# Mapper stores found by the byte scan in bytes no path reached:
mapst 038C0   # LD ($FFFF),A; after LD A,$06; JP/CALL target from $25932; 32 bytes of valid code before it
mapst 04CBA   # LD ($FFFF),A; after LD A,$03; 32 bytes of valid code before it
mapst 05148   # LD ($FFFF),A; after LD A,$CE; 32 bytes of valid code before it
mapst 06305   # LD ($FFFF),A; after LD A,$C8; 32 bytes of valid code before it
mapst 06898   # LD ($FFFF),A; after LD A,$C8; 32 bytes of valid code before it
mapst 068C4   # LD ($FFFF),A; after LD A,$C8; 32 bytes of valid code before it
mapst 06943   # LD ($FFFF),A; after LD A,$C8; 32 bytes of valid code before it
mapst 069CF   # LD ($FFFF),A; after LD A,$C8; 32 bytes of valid code before it
mapst 069F7   # LD ($FFFF),A; after LD A,$C8; 32 bytes of valid code before it
# CHECK low: site 00552  OUT ($BF),A  (vdp_control; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 00559  OUT ($BF),A  (vdp_control; after LD A,$87; 32 bytes of valid code before it)
# CHECK medium: site 00B70  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 00B76  OUT ($BF),A  (vdp_control; 32 bytes of valid code before it)
# CHECK medium: site 00DBC  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK high: site 00DC3  OUT (C),D  (port in C; branch target from $2494F $24C35; 32 bytes of valid code before it)
# CHECK high: site 00DC8  OUT (C),A  (port in C; branch target from $00DD5; 32 bytes of valid code before it)
# CHECK medium: site 00DCF  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK high: site 05591  OUT ($BF),A  (vdp_control; after LD A,$36; 32 bytes of valid code before it)
# CHECK high: site 05599  OUT ($BF),A  (vdp_control; after LD A,$80; 32 bytes of valid code before it)
# CHECK medium: site 0D464  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK medium: site 0D466  IN A,($C1)  (joypad_b_misc; 32 bytes of valid code before it)
# CHECK low: site 1009D  OUT ($C0),A  (no_effect; no valid code after it)
# CHECK low: site 10A8D  IN A,($F0)  (joypad_a; no evidence)
# CHECK low: site 10F07  IN A,($DD)  (joypad_b_misc; 16 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1173A  IN A,($F0)  (joypad_a; 15 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1D0C1  OUT ($BE),A  (vdp_data; no evidence)
# CHECK medium: site 1D888  OUT ($F0),A  (fm_address; 32 bytes of valid code before it)
# CHECK medium: site 1DAA9  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 1DB99  OUT ($7E),A  (psg; 32 bytes of valid code before it)
# CHECK medium: site 1EF19  IN A,($BF)  (vdp_status; 12 bytes of valid code before it)
# CHECK low: site 1EF1D  IN A,($BD)  (vdp_status; no evidence)
# CHECK low: site 1F5C2  IN B,(C)  (port in C; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2233D  IN A,($3F)  (unmapped_read; 19 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 24348  OUT (C),B  (port in C; no evidence)
# CHECK medium: site 25910  IN A,($F0)  (joypad_a; 32 bytes of valid code before it)
# CHECK low: site 26F0E  IN A,($BE)  (vdp_data; no evidence)
# CHECK medium: site 282BC  OUT ($3F),A  (io_control; 32 bytes of valid code before it)
# CHECK low: site 28E5B  IN A,($3F)  (unmapped_read; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 29E34  OUT ($7F),A  (psg; branch target from $29E02)
# CHECK low: site 2A215  OUT ($BD),A  (vdp_control; no evidence)
# CHECK low: site 2AA54  OUT (C),H  (port in C; 9 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 2C376  IN A,($C0)  (joypad_a; no evidence)
# CHECK low: site 2D041  IN C,(C)  (port in C; 31 bytes of valid code before it; no valid code after it)
# CHECK low: site 2E698  IN A,($3F)  (unmapped_read; 8 bytes of valid code before it; no valid code after it)
# CHECK medium: site 34FEE  OUT ($7F),A  (psg; 32 bytes of valid code before it)
# CHECK low: site 3525C  OUT ($C0),A  (no_effect; branch target from $352C2; no valid code after it)
# CHECK low: site 39EAB  OUT (C),B  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
page 0 delay
        OPT --zxnext
; delay: as the game's $0D2E-$0D42, in real time. Returns as the game's routine does: A, BC, DE, HL
; kept, F as after its last DEC H (Z and N set, carry kept). The interrupt state stays as it was;
; each line read runs with interrupts off, so a handler cannot change the NextReg select port
; between the select and the read. The stack holds no more than the game's routine puts there.
delay:  push af
        ld (sv_hl),hl
        ld (sv_de),de
        ld (sv_bc),bc
        ld a,i                  ; P/V: interrupts on at entry
        ld a,0
        jp po,.di
        inc a
.di:    ld (dirq),a
        ld l,b                  ; units: B, 0 means 256
        ld h,0
        ld a,b
        or a
        jr nz,.nz
        inc h
.nz:    ld (dunits),hl
        di
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld hl,311               ; lines in a 50 Hz frame
        ld de,307               ; a unit with the frame handler running
        bit 2,a
        jr z,.hz
        ld hl,264               ; 60 Hz
        ld de,312
.hz:    ld (dlen),hl
        ld a,(dirq)
        or a
        jr nz,.on
        ld hl,-3                ; interrupts off: no handler time, 304 or 309 lines
        add hl,de
        ex de,hl
.on:    ld (dunit),de
        call dline
        ld (dprev),hl
        ld hl,(dunit)
        ld (dleft),hl
.poll:  call dline              ; HL = this line
        ld de,(dprev)
        ld (dprev),hl
        or a
        sbc hl,de               ; lines since the last read
        jr nc,.pos
        ld de,(dlen)
        add hl,de               ; the frame wrapped
.pos:   ex de,hl
        ld hl,(dleft)
        or a
        sbc hl,de
.chk:   ld (dleft),hl
        bit 7,h
        jr nz,.unit
        ld a,h
        or l
        jr nz,.poll
.unit:  ld de,(dunits)          ; a unit is over
        dec de
        ld (dunits),de
        ld a,d
        or e
        jr z,.end
        ld de,(dunit)
        add hl,de
        jr .chk
.end:   ld hl,(sv_hl)
        ld de,(sv_de)
        ld bc,(sv_bc)
        pop af
        push hl
        ld h,1
        dec h                   ; the game's last DEC H: Z, N, carry kept
        pop hl
        ret
; HL = the Next's raster line (0-310). Interrupts off for the read, then as at the entry. The high
; bit is read again after the low byte, and the read repeats when it changed (line 255 to 256).
dline:  di
        ld bc,$243B
.again: ld a,$1E
        out (c),a
        inc b
        in h,(c)
        dec b
        ld a,$1F
        out (c),a
        inc b
        in l,(c)
        dec b
        ld a,$1E
        out (c),a
        inc b
        in a,(c)
        dec b
        xor h
        and 1
        jr nz,.again
        ld a,h
        and 1
        ld h,a
        ld a,(dirq)
        or a
        ret z
        ei
        ret
dirq:   db 0
dunits: dw 0
dunit:  dw 0
dlen:   dw 0
dprev:  dw 0
dleft:  dw 0
sv_hl:  dw 0
sv_de:  dw 0
sv_bc:  dw 0
endpage

# Battlemaniacs (Brazil) (Action Replay).cht, "Infinite Lives P1": RAM $C781 is the
# player 1 lives; held at 9 the player keeps them through every death
poke "Infinite lives"
ar 00C7-8109
endpoke

# Battlemaniacs (Brazil) (Action Replay).cht, "Infinite Green Orbs P1 (Hits)": RAM $C782
# is the player 1 energy, shown as orbs; held at 9 hits cost nothing
poke "Infinite energy"
ar 00C7-8209
endpoke

# Battlemaniacs (Brazil) (Action Replay).cht, "Infinite Continues": RAM $C794 is the
# continues left; held at 9 a game over never uses one up
poke "Infinite continues"
ar 00C7-9409
endpoke

# Battlemaniacs (Brazil).cht, "Level Select Enabled": RAM $C757 = 1 adds a level select
# screen after the player menu; Right changes the level, button 1 starts it
poke "Level select"
ar 00C7-5701
endpoke
