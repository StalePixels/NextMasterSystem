# Kung Fu Kid (USA, Europe, Brazil) (En), CRC32 1E949D1F, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output with two reference I/O logs of
# 600 s (start presses, then random input; start presses, then walking right with
# kicks and jumps), then decided by hand.
#
# Decisions:
# - Every logged I/O and mapper site is a static site. The bank 1 sites that the
#   logs do not run ($525F, $5FB1-$6628) are on plain code paths that static flow
#   reaches.
# - The jump table at $6C9E (bank 1), read at $15FE, is indexed by an object's
#   type, and $15D4 skips type 0. Entry 0 ($A9F2) is the word before the table's
#   real entries: bank 2 at $A9F2 is sprite layout data. The OUT ($02),A at $AA9F,
#   the calls into RAM and the RETs there, and the stores at $00F9, $0A2E, $0A3B,
#   $0AF0 and $0AFC reached from them, are that data; they get no spec lines.
# - The JP (HL) at $020C dispatches through the tables at $020D and $6C9E, which
#   the scanner reads.
# - The byte scan's OUT ($BE),A at $1368 is in a routine at $134D, the twin of
#   $1371 (VRAM read, bit reverse, write back), that nothing in the cart names:
#   unused in data/scan-verdicts.tsv. The medium byte scan rows in banks 5 and 6
#   are compressed graphics: false in data/scan-verdicts.tsv.
# - priority is off. The game sets the priority bit only on the text screens
#   (ROUND, GAME OVER), which show no sprites (reference VRAM dumps).
# - No HALT, no line interrupts. Play frames take a median 33% of a frame on the
#   Next, at most 77% (MAME tbblue, game frames 300-2400).
name Kung Fu Kid
cart 1E949D1F
hz any		; No-Intro regions USA, Europe, Brazil
# No free RST vector: $0008-$002F holds data bytes and RST $30 holds RST $38.
# The JP at $0000 becomes the vector, the game starts at its target.
vector 00 io
start 008C
asm 00090 2   ; IM 1 -> IM 2
    im 2
endasm
site 000A9   ; OUT ($DF),A
site 000D9   ; IN A,($BF)
site 000E2   ; OTIR
site 002CD   ; OUT ($BF),A
site 002D3   ; OUT ($BF),A
site 002D9   ; OUT ($BE),A
site 003FA   ; OUT ($BE),A
site 00400   ; OUT ($BE),A
site 01094   ; IN A,($DC)
site 01097   ; IN A,($DD)
site 010B0   ; IN A,($DC)
site 01168   ; OUT ($BF),A
site 0116C   ; OUT ($BF),A
site 011E9   ; OUT ($BF),A
site 011EE   ; OUT ($BF),A
site 011F7   ; OUT ($BE),A
site 01208   ; OUT ($BE),A
site 01218   ; OUT ($BE),A
site 0121D   ; OUT ($BE),A
site 0122D   ; OUT ($BE),A
site 01233   ; OUT ($BE),A
site 0124D   ; OUT ($BE),A
site 01251   ; OUT ($BE),A
site 01263   ; OUT ($BF),A
site 01268   ; OUT ($BF),A
site 0126D   ; OUT ($BE),A
site 0128A   ; OUT (C),D
site 012B0   ; OUT ($BF),A
site 012B5   ; OUT ($BF),A
site 012BA   ; OUT ($BE),A
site 012E9   ; OUT ($BF),A
site 012EE   ; OUT ($BF),A
site 012F3   ; OUT ($BE),A
site 01337   ; OUT ($BF),A
site 0133A   ; OUT ($BF),A
site 01340   ; IN A,($BE)
site 0138F   ; OUT ($BE),A
site 013A1   ; OUT ($BE),A
site 013A7   ; OUT ($BE),A
site 013B2   ; OUT ($BE),A
site 013B8   ; OUT ($BE),A
site 013C6   ; OUT ($BE),A
site 013CC   ; OUT ($BE),A
site 013DE   ; IN A,($BF)
site 013F8   ; IN A,($DD)
site 01421   ; OTIR
site 01428   ; OTIR
site 01446   ; OTIR
site 01456   ; OTIR
site 01463   ; OTIR
site 05248   ; OUT ($3F),A
site 0524A   ; IN A,($DD)
site 05254   ; OUT ($3F),A
site 05256   ; IN A,($DD)
site 0525F   ; OUT ($3F),A
site 05FB1   ; OUT ($BE),A
site 05FB7   ; OUT ($BE),A
site 06277   ; OUT ($BF),A
site 0627A   ; OUT ($BF),A
site 06282   ; IN A,($BE)
site 063DF   ; OTIR
site 06401   ; OTIR
site 0641B   ; OUT ($BF),A
site 0641F   ; OUT ($BF),A
site 06425   ; OUT ($BE),A
site 064D6   ; OUT ($BF),A
site 064DA   ; OUT ($BF),A
site 064DF   ; OUT ($BF),A
site 064E3   ; OUT ($BF),A
site 0650D   ; OUT ($BF),A
site 06512   ; OUT ($BF),A
site 06522   ; OUTI
site 06527   ; OUTI
site 06530   ; OUT ($BF),A
site 06535   ; OUT ($BF),A
site 0653E   ; OUTI
site 06553   ; OUT ($BF),A
site 0655A   ; OUT ($BF),A
site 06578   ; OUT ($BE),A
site 065A5   ; OUT ($BF),A
site 065A9   ; OUT ($BF),A
site 065AE   ; OUT ($BE),A
site 06628   ; OUT ($BE),A
site 0E4C9   ; OUT ($7F),A
site 0E8EF   ; OUT ($7F),A
site 0E949   ; OUT ($7F),A
site 0E963   ; OTIR
site 0E96A   ; OUT ($7F),A
site 0E96E   ; OUT ($7F),A
mapst 00094   ; LD ($FFFF),A
mapst 000FC   ; LD ($FFFF),A
mapst 0023C   ; LD ($FFFF),A
mapst 002BA   ; LD ($FFFF),A
mapst 002C8   ; LD ($FFFF),A
mapst 003CB   ; LD ($FFFF),A
mapst 003E8   ; LD ($FFFF),A
mapst 0047D   ; LD ($FFFF),A
mapst 0066E   ; LD ($FFFF),A
mapst 007E0   ; LD ($FFFF),A
mapst 00829   ; LD ($FFFF),A
mapst 00844   ; LD ($FFFF),A
mapst 0085E   ; LD ($FFFF),A
mapst 00893   ; LD ($FFFF),A
mapst 00943   ; LD ($FFFF),A
mapst 00BCE   ; LD ($FFFF),A
mapst 00DE0   ; LD ($FFFF),A
mapst 00EF2   ; LD ($FFFF),A
mapst 00F2E   ; LD ($FFFF),A
mapst 00FE2   ; LD ($FFFF),A
mapst 0112E   ; LD ($FFFF),A
mapst 01404   ; LD ($FFFF),A
mapst 01435   ; LD ($FFFF),A
mapst 01499   ; LD ($FFFF),A
mapst 014A4   ; LD ($FFFF),A
mapst 01653   ; LD ($FFFF),A
mapst 016E1   ; LD ($FFFF),A
mapst 05523   ; LD ($FFFF),A
mapst 05538   ; LD ($FFFF),A
mapst 055BF   ; LD ($FFFF),A
mapst 055DC   ; LD ($FFFF),A
mapst 0566B   ; LD ($FFFF),A
mapst 0568F   ; LD ($FFFF),A
mapst 06385   ; LD ($FFFF),A
mapst 063C4   ; LD ($FFFF),A
mapst 063DA   ; LD ($FFFF),A
mapst 06683   ; LD ($FFFF),A
mapst 066A0   ; LD ($FFFF),A

# Kung Fu Kid (USA, Europe, Brazil).cht, "Infinite Lives": RAM $C081 is the number of lives
poke "Infinite lives"
ar 00C0-8109
endpoke

# Kung Fu Kid (USA, Europe, Brazil).cht, "Invincibility": RAM $C459 is the health, $28 when
# full. Hits still land, but the health is refilled each frame
poke "Infinite health"
ar 00C4-5928
endpoke

# Kung Fu Kid (USA, Europe, Brazil).cht, "Infinite Time": RAM $C4BC is the time, in BCD
poke "Infinite time"
ar 00C4-BC99
endpoke
