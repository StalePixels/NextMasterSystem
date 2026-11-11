# Baku Baku (Brazil) (En), CRC32 35D84DC2, 256K, Sega mapper.
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - No free RST vector: $0000-$0002 (DI; JP $0071) becomes the vector. The game starts at
#   $0071, after its own DI.
# - The game resets itself with RST $00 at $1172, $569E, $598B and $5DDD, each after a call
#   that fades the screen. The runtime takes an RST $00 for an I/O trap, so each call and
#   its RST become a jump to a cave in the unused zero bytes of bank 1 (slot 1 always holds
#   bank 1) that makes the call and does what $0000 does: DI, then JP $0071.
# - $7FFB (OUT (C),D to the scanner) is the cart header (the TMR SEGA checksum bytes).
# - $2872-$291C: the Game Gear link port code (ports $03 and $05), run only when $DCC0 is
#   set. The sites are patched, as on any code path.
# - Unused code (no call, jump, address load or table entry names it): the VDP status wait
#   at $0446, the rectangle fill at $0703, the bank copy at $08B3 and the VRAM fill at $544C.
# - No code runs from slot 2 except the sound driver in bank 15.
name Baku Baku
cart 35D84DC2
hz 60		; No-Intro region Brazil
vector 00 io
start 0071
asm 00071 2   ; IM 1 -> IM 2
    im 2
endasm
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 00089   ; IN A,($7E)
site 0013A   ; IN A,($BF)
site 0014D   ; IN A,($BF)
site 00158   ; OUT ($BF),A
site 0015C   ; OUT ($BF),A
site 00161   ; OUT ($BF),A
site 00165   ; OUT ($BF),A
site 00230   ; OTIR
site 0024E   ; OUT ($BF),A
site 00252   ; OUT ($BF),A
site 0026A   ; OUT ($BE),A
site 0027B   ; OUT ($BE),A
site 0028C   ; OUT ($BE),A
site 00293   ; OUT ($BE),A
site 002B5   ; OUT ($BE),A
site 002D2   ; OUT ($BE),A
site 003D4   ; OUT ($BE),A
site 003DA   ; OUT ($BE),A
site 00416   ; OUT ($3F),A
site 00418   ; IN A,($DD)
site 00422   ; OUT ($3F),A
site 00424   ; IN A,($DD)
site 0042D   ; OUT ($3F),A
site 00577   ; OUT ($BE),A
site 0062F   ; OUT ($BE),A
site 00649   ; IN A,($DC)
site 006B7   ; OUT ($BE),A
site 0073D   ; OUT ($BE),A
site 0074C   ; OUT ($BE),A
site 00751   ; OUT ($BE),A
site 00764   ; OUT ($BE),A
site 0078F   ; OUT ($BE),A
site 00794   ; OUT ($BE),A
site 007A7   ; OUT ($BE),A
site 007AC   ; OUT ($BE),A
site 007CB   ; OUT ($BE),A
site 00808   ; OUT ($BE),A
site 0090D   ; OUT ($BE),A
site 00944   ; OUT ($BE),A
site 00995   ; OUT ($BF),A
site 00998   ; OUT ($BF),A
site 014D8   ; OUT ($BE),A
site 014DE   ; OUT ($BE),A
site 01718   ; OTIR
site 02872   ; IN A,($05)
site 0287C   ; OUT ($03),A
site 02913   ; IN A,($05)
site 0291C   ; OUT ($03),A
site 02A8A   ; IN A,($DC)
site 04135   ; OUT ($BE),A
site 0413C   ; OUT ($BE),A
site 04440   ; OUT ($BE),A
site 04446   ; OUT ($BE),A
site 04A67   ; OUT ($BE),A
site 05CF5   ; OUT ($BE),A
site 06345   ; OUT ($BE),A
site 0634A   ; OUT ($BE),A
site 3C1FA   ; OUT ($7F),A
site 3C463   ; OTIR
site 3C581   ; OUT ($7F),A
site 3C58B   ; OUT ($7F),A
site 3C5A8   ; OUT ($7F),A
site 3C6D0   ; OUT ($7F),A
site 3C764   ; OUT ($7F),A
site 3C83E   ; OUT ($7F),A
site 3C847   ; OUT ($7F),A
site 3C857   ; OUT ($7F),A
site 3C8D7   ; OUT ($7F),A
label cv_reset1bc7 07F00
label cv_reset09c5 07F08
asm 07F00 8    ; unused zero bytes: CALL $1BC7, then the reset of $0000
    call $1BC7
    di
    jp $0071
    nop
endasm
asm 07F08 7    ; unused zero bytes: CALL $09C5, then the reset of $0000
    call $09C5
    di
    jp $0071
endasm
asm 0116F 4    ; CALL $1BC7; RST $00
    jp cv_reset1bc7
endasm
asm 05988 4    ; CALL $1BC7; RST $00
    jp cv_reset1bc7
endasm
asm 0569B 4    ; CALL $09C5; RST $00
    jp cv_reset09c5
endasm
asm 05DDA 4    ; CALL $09C5; RST $00
    jp cv_reset09c5
endasm
mapst 00033   ; LD ($FFFF),A
mapst 00078   ; LD ($FFFC),A
mapst 0007C   ; LD ($FFFD),A
mapst 00081   ; LD ($FFFE),A
mapst 00086   ; LD ($FFFF),A
mapst 00178   ; LD ($FFFF),A
mapst 0018F   ; LD ($FFFF),A
mapst 002A3   ; LD ($FFFF),A
mapst 00930   ; LD ($FFFF),A
mapst 0530E   ; LD ($FFFF),A
mapst 0532C   ; LD ($FFFF),A
mapst 0533F   ; LD ($FFFF),A
mapst 055BA   ; LD ($FFFF),A
mapst 055C7   ; LD ($FFFF),A
mapst 055D4   ; LD ($FFFF),A
mapst 058FB   ; LD ($FFFF),A
mapst 05908   ; LD ($FFFF),A
