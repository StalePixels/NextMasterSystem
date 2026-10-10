# Pit Pot (Fushigi no Oshiro Pit Pot, Japan), CRC32 E6795C53, 32K, no mapper.
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand
# against the detector's dynamic I/O log.
#
# Decisions:
# - RST $08, $18, $20 and $30 are in use, so the only free vector is $00.
#   $0000-$0002 (the game's interrupt-disable and interrupt mode 1 setup) becomes JP to the io entry and the game starts at
#   $0003. The framework does DI and IM 2, so the IM 1 at $0001 is not poked.
# - $003F is an OUTI loop that jumps back to itself, patched as OTIR.
# - Every high and medium confidence I/O site is kept. All of them except the
#   ones below run in the detector log. Kept without a log hit, as real code
#   reached by static flow: $00FE (OTIR to $BF, reached from $0090 when
#   $C002 bit 2 is set) and $038B-$0449 (a second input read of $C0/$C1 with
#   writes to $DE, taken when the flag tested at $037D and the carry from RLCA
#   select it).
# - $22E9, $22EF (pointer-harvest) and $3170, $3174 (table) are kept; the log
#   runs them.
# - The CHECK rows of the draft are dropped. None is an I/O instruction. They
#   are stores, calls and returns the scanner followed from data at $01FA5,
#   $03F05-$03F66 and $07F17-$07FDC, and two returns at $334F and $3370 that it
#   could not resolve. The detector log has no I/O at any of them.
# - priority: name table writes set bit 12 (the priority bit) at $0029, and
#   the detector saw priority tiles on screen in 124 frames.
name Pit Pot
cart E6795C53
hz 60		; No-Intro regions Japan
vector 00 io
start 0003
priority
otir 0003F   ; OUTI
site 00009   ; OUT ($BF),A
site 00013   ; OUT ($BE),A
site 00023   ; OUTI
site 00029   ; OUT (C),A
site 00031   ; OUT ($BF),A
site 00034   ; OUT ($BF),A
site 0005D   ; OUT ($BE),A
site 000FE   ; OTIR
site 001B4   ; IN A,($BF)
site 00217   ; OUT ($BF),A
site 0021A   ; OUT ($BF),A
site 0021E   ; IN A,($BE)
site 00239   ; OUT ($BE),A
site 0023E   ; OUT ($BE),A
site 0024E   ; OUTI
site 00254   ; OUT (C),A
site 00278   ; OUT (C),D
site 002C0   ; OUTI
site 002C6   ; OUT (C),A
site 002CE   ; OUTD
site 002D9   ; OTIR
site 00314   ; OUT ($BF),A
site 00317   ; OUT ($BF),A
site 0031A   ; OUT ($BE),A
site 00356   ; OUT ($DF),A
site 00360   ; OUT ($DE),A
site 00362   ; IN A,($DE)
site 0036B   ; OUT ($7F),A
site 0036F   ; OUT ($7F),A
site 00373   ; OUT ($7F),A
site 00377   ; OUT ($7F),A
site 00386   ; IN A,($C0)
site 0038B   ; IN A,($C0)
site 00390   ; IN A,($C1)
site 003A0   ; OUT ($DE),A
site 003A2   ; IN A,($C0)
site 003A7   ; OUT ($DE),A
site 003A9   ; IN A,($C0)
site 003B4   ; OUT ($DE),A
site 003B6   ; IN A,($C0)
site 003C1   ; OUT ($DE),A
site 003C3   ; IN A,($C0)
site 003D5   ; OUT ($DE),A
site 003D7   ; IN A,($C0)
site 003E2   ; OUT ($DE),A
site 003E4   ; IN A,($C0)
site 003FB   ; OUT ($DE),A
site 003FD   ; IN A,($C0)
site 00402   ; IN A,($C1)
site 0040C   ; OUT ($DE),A
site 0040E   ; IN A,($C0)
site 00420   ; OUT ($DE),A
site 00422   ; IN A,($C0)
site 0042D   ; OUT ($DE),A
site 0042F   ; IN A,($C0)
site 0043A   ; OUT ($DE),A
site 0043C   ; IN A,($C1)
site 00447   ; OUT ($DE),A
site 00449   ; IN A,($C1)
site 022E9   ; OUT ($BE),A
site 022EF   ; OUT ($BE),A
site 03170   ; OUT ($BE),A
site 03174   ; OUT ($BE),A
site 049B4   ; OUT ($7F),A
site 049D2   ; OTIR

