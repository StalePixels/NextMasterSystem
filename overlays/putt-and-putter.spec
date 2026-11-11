# Putt & Putter (Europe, Brazil) (En), CRC32 357D4F78, 128K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input), then decided by hand.
#
# Decisions:
# - The scan runs with --no-harvest and --entry 7:8000. The harvested addresses $0030
#   and $0600 are object fields, not code. The sound driver is bank 7 at $8000, called
#   through the far call $02A9 (B = bank, HL = address) from $0B27; the scanner takes
#   that call's target in bank 2.
# - $0030-$0037 are eight NOPs that nothing calls: the io vector. $0000 stays the reset.
# - The bank 2 code in the scan is data: the tables read at $00ED (3 entries, then the
#   VDP register values at $00F3) and $0D7A (3 entries, then data) are read too long.
# - Code that nothing in the cart calls, patched as code: the OUTD run $058D-$060D, the
#   VRAM writers $0779 and $45CF, the tile list loader $07E2 and the sound test and
#   other screens at $0E0D-$1050.
# - The far call $02A9 returns through $02B6 (POP AF; LD ($FFFF),A; RET).
# - No priority: the reference logs show no frame with priority cells on the screen.
# - The frame handler writes register 1 with the display off and 8x8 sprites at $013F
#   and with the display on and 8x16 sprites at $0151, around its VRAM work. On the Next
#   that work runs past the ULA interrupt and into the next picture: the once-a-frame
#   work took the sprites as 8x8 (and dropped the sprite cache at each change), and the
#   top of the picture showed the backdrop until the display went on. The first write
#   is made the same as the second ($0142 AND $BF -> OR $42); on a Master System the
#   display-off write falls in the vertical blank, where it shows nothing.
name Putt & Putter
cart 357D4F78
hz 50		; No-Intro regions Europe, Brazil
vector 30 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00029 2   ; IM 1 -> IM 2 (RST $28 restart)
    im 2
endasm
asm 00142 2   ; AND $BF -> OR $42: the frame handler's register 1 write keeps display and 8x16 on
    or $42
endasm
site 0003A   ; IN A,($BF)
site 00070   ; IN A,($BF)
site 00074   ; OUT ($BF),A
site 00078   ; OUT ($BF),A
site 000FC   ; OUT ($F2),A
site 00104   ; OUT ($3E),A
site 00108   ; OUT ($3F),A
site 0010F   ; IN A,($BF)
site 00111   ; IN A,($BF)
site 0011D   ; IN A,($BF)
site 00137   ; IN A,($DD)
site 00144   ; OUT ($BF),A
site 00148   ; OUT ($BF),A
site 00156   ; OUT ($BF),A
site 0015A   ; OUT ($BF),A
site 001AF   ; OUT ($BF),A
site 001B3   ; OUT ($BF),A
site 001BE   ; OUT ($BF),A
site 001C2   ; OUT ($BF),A
site 001D4   ; OUT ($BF),A
site 001D8   ; OUT ($BF),A
site 001E2   ; OUT ($BF),A
site 001E6   ; OUT ($BF),A
site 001EC   ; OUT ($BF),A
site 001F0   ; OUT ($BF),A
site 00211   ; OUT ($BF),A
site 00215   ; OUT ($BF),A
site 00244   ; OUT ($BF),A
site 00248   ; OUT ($BF),A
site 0024D   ; OUT ($BF),A
site 00251   ; OUT ($BF),A
site 00272   ; OUT ($BF),A
site 00276   ; OUT ($BF),A
site 002BD   ; IN A,($DC)
site 002DA   ; IN A,($DD)
site 00436   ; OUT ($BF),A
site 0043C   ; OUT ($BF),A
site 00441   ; OUT (C),L
site 00443   ; OUT (C),H
site 00447   ; IN A,($BF)
site 00452   ; OUT ($BF),A
site 00455   ; OUT ($BF),A
site 0045B   ; OUT ($BE),A
site 00468   ; OUT ($BE),A
site 00633   ; OUTI
site 00635   ; OUTI
site 00637   ; OUTI
site 00639   ; OUTI
site 0063B   ; OUTI
site 0063D   ; OUTI
site 0063F   ; OUTI
site 00641   ; OUTI
site 00643   ; OUTI
site 00645   ; OUTI
site 00647   ; OUTI
site 00649   ; OUTI
site 0064B   ; OUTI
site 0064D   ; OUTI
site 0064F   ; OUTI
site 00651   ; OUTI
site 00653   ; OUTI
site 00655   ; OUTI
site 00657   ; OUTI
site 00659   ; OUTI
site 0065B   ; OUTI
site 0065D   ; OUTI
site 0065F   ; OUTI
site 00661   ; OUTI
site 00663   ; OUTI
site 00665   ; OUTI
site 00667   ; OUTI
site 00669   ; OUTI
site 0066B   ; OUTI
site 0066D   ; OUTI
site 0066F   ; OUTI
site 00671   ; OUTI
site 00673   ; OUTI
site 00675   ; OUTI
site 00677   ; OUTI
site 00679   ; OUTI
site 0067B   ; OUTI
site 0067D   ; OUTI
site 0067F   ; OUTI
site 00681   ; OUTI
site 00683   ; OUTI
site 00685   ; OUTI
site 00687   ; OUTI
site 00689   ; OUTI
site 0068B   ; OUTI
site 0068D   ; OUTI
site 0068F   ; OUTI
site 00691   ; OUTI
site 00693   ; OUTI
site 00695   ; OUTI
site 00697   ; OUTI
site 00699   ; OUTI
site 0069B   ; OUTI
site 0069D   ; OUTI
site 0069F   ; OUTI
site 006A1   ; OUTI
site 006A3   ; OUTI
site 006A5   ; OUTI
site 006A7   ; OUTI
site 006A9   ; OUTI
site 006AB   ; OUTI
site 006AD   ; OUTI
site 006AF   ; OUTI
site 006B1   ; OUTI
site 006B3   ; OUTI
site 006B5   ; OUTI
site 006B7   ; OUTI
site 006B9   ; OUTI
site 006BB   ; OUTI
site 006BD   ; OUTI
site 006BF   ; OUTI
site 006C1   ; OUTI
site 006C3   ; OUTI
site 006C5   ; OUTI
site 006C7   ; OUTI
site 006C9   ; OUTI
site 006CB   ; OUTI
site 006CD   ; OUTI
site 006CF   ; OUTI
site 006D1   ; OUTI
site 006D3   ; OUTI
site 006D5   ; OUTI
site 006D7   ; OUTI
site 006D9   ; OUTI
site 006DB   ; OUTI
site 006DD   ; OUTI
site 006DF   ; OUTI
site 006E1   ; OUTI
site 006E3   ; OUTI
site 006E5   ; OUTI
site 006E7   ; OUTI
site 006E9   ; OUTI
site 006EB   ; OUTI
site 006ED   ; OUTI
site 006EF   ; OUTI
site 006F1   ; OUTI
site 006F3   ; OUTI
site 006F5   ; OUTI
site 006F7   ; OUTI
site 006F9   ; OUTI
site 006FB   ; OUTI
site 006FD   ; OUTI
site 006FF   ; OUTI
site 00701   ; OUTI
site 00703   ; OUTI
site 00705   ; OUTI
site 00707   ; OUTI
site 00709   ; OUTI
site 0070B   ; OUTI
site 0070D   ; OUTI
site 0070F   ; OUTI
site 00711   ; OUTI
site 00713   ; OUTI
site 00715   ; OUTI
site 00717   ; OUTI
site 00719   ; OUTI
site 0071B   ; OUTI
site 0071D   ; OUTI
site 0071F   ; OUTI
site 00721   ; OUTI
site 00723   ; OUTI
site 00725   ; OUTI
site 00727   ; OUTI
site 00729   ; OUTI
site 0072B   ; OUTI
site 0072D   ; OUTI
site 0072F   ; OUTI
site 00731   ; OUTI
site 00741   ; OUT ($BE),A
site 00746   ; OUT ($BE),A
site 00763   ; OUT ($BE),A
site 00768   ; OUT ($BE),A
site 00781   ; OUT ($BF),A
site 00784   ; OUT ($BF),A
site 0078C   ; OUTI
site 00792   ; OUTI
site 00835   ; OUT ($BF),A
site 00839   ; OUT ($BF),A
site 00846   ; IN A,($BF)
site 00857   ; OUT ($BF),A
site 0085B   ; OUT ($BF),A
site 00A6A   ; OUT ($BE),A
site 00A6F   ; OUT ($BE),A
site 00AAF   ; OUT ($BE),A
site 00AB4   ; OUT ($BE),A
site 01DBF   ; OUT ($BF),A
site 01DC3   ; OUT ($BF),A
site 01DCE   ; OUT ($BF),A
site 01DD2   ; OUT ($BF),A
site 04588   ; OUT ($BE),A
site 0458B   ; OUT ($BE),A
site 045AC   ; OUT ($BF),A
site 045AF   ; OUT ($BF),A
site 045B2   ; OUT ($BE),A
site 045B5   ; OUT ($BE),A
site 045D1   ; OUT ($BF),A
site 045D5   ; OUT ($BF),A
site 045E0   ; OUT ($BE),A
site 045E3   ; OUT ($BE),A
site 048E6   ; OUT ($BE),A
site 06DEF   ; OUT ($BF),A
site 06DF2   ; OUT ($BF),A
site 06DF5   ; OUT ($BE),A
site 06DF8   ; OUT ($BE),A
site 06E02   ; OUT ($BF),A
site 06E05   ; OUT ($BF),A
site 06E08   ; OUT ($BE),A
site 06E0B   ; OUT ($BE),A
site 06E3B   ; OUT ($BF),A
site 06E3E   ; OUT ($BF),A
site 06E41   ; OUT ($BE),A
site 06E44   ; OUT ($BE),A
site 06E4E   ; OUT ($BF),A
site 06E51   ; OUT ($BF),A
site 06E54   ; OUT ($BE),A
site 06E57   ; OUT ($BE),A
site 1C1E2   ; OUT ($7F),A
site 1C308   ; OUT ($7F),A
site 1C49A   ; OTIR
site 1C5B2   ; OUT ($7F),A
site 1C5BC   ; OUT ($7F),A
site 1C5D9   ; OUT ($7F),A
site 1C6DD   ; OUT ($7F),A
site 1C769   ; OUT ($7F),A
site 1C80B   ; OUT ($7F),A
site 1C814   ; OUT ($7F),A
site 1C824   ; OUT ($7F),A
site 1C8A0   ; OUT ($7F),A
mapldk 0007A   # LD HL,$FFFC; LD (HL),$00
maphl 00080   # LD (HL),$00, HL = $FFFD
maphl 00083   # LD (HL),$01, HL = $FFFE
maphl 00086   # LD (HL),$02, HL = $FFFF
mapst 000E0   ; LD ($FFFF),A
mapst 00168   ; LD ($FFFF),A
mapst 0027E   ; LD ($FFFF),A
mapst 002AE   ; LD ($FFFF),A
mapst 002B7   ; LD ($FFFF),A
mapst 003F9   ; LD ($FFFF),A
mapst 0040A   ; LD ($FFFF),A
mapst 007F7   ; LD ($FFFF),A
mapst 00B03   ; LD ($FFFF),A
mapst 00B39   ; LD ($FFFF),A
mapst 01279   ; LD ($FFFF),A
mapst 019EB   ; LD ($FFFF),A
mapst 01A88   ; LD ($FFFF),A
mapst 01B71   ; LD ($FFFF),A
mapst 01BF7   ; LD ($FFFF),A
mapst 01C80   ; LD ($FFFF),A
mapld 01C85   # LD HL,$FFFF; LD (HL),$02
mapst 01CC1   ; LD ($FFFF),A
mapst 01CFC   ; LD ($FFFF),A
mapst 01EE8   ; LD ($FFFF),A
mapst 01FC0   ; LD ($FFFF),A
mapst 022F6   ; LD ($FFFF),A
mapst 02672   ; LD ($FFFF),A
mapst 03CC3   ; LD ($FFFF),A
mapst 03F18   ; LD ($FFFF),A
mapst 046FC   ; LD ($FFFF),A
mapst 066D1   ; LD ($FFFF),A
mapst 00EAA   # LD ($FFFF),A; after LD A,$06; 31 bytes of valid code before it
mapst 00F77   # LD ($FFFF),A; after LD A,$03; 32 bytes of valid code before it
mapst 00FF0   # LD ($FFFF),A; after LD A,$06; JP/CALL target from $0C06A $0C09A; 32 bytes of valid code before it
mapst 0102D   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
site 0058D   ; OUTD (unused run)
site 0058F   ; OUTD (unused run)
site 00591   ; OUTD (unused run)
site 00593   ; OUTD (unused run)
site 00595   ; OUTD (unused run)
site 00597   ; OUTD (unused run)
site 00599   ; OUTD (unused run)
site 0059B   ; OUTD (unused run)
site 0059D   ; OUTD (unused run)
site 0059F   ; OUTD (unused run)
site 005A1   ; OUTD (unused run)
site 005A3   ; OUTD (unused run)
site 005A5   ; OUTD (unused run)
site 005A7   ; OUTD (unused run)
site 005A9   ; OUTD (unused run)
site 005AB   ; OUTD (unused run)
site 005AD   ; OUTD (unused run)
site 005AF   ; OUTD (unused run)
site 005B1   ; OUTD (unused run)
site 005B3   ; OUTD (unused run)
site 005B5   ; OUTD (unused run)
site 005B7   ; OUTD (unused run)
site 005B9   ; OUTD (unused run)
site 005BB   ; OUTD (unused run)
site 005BD   ; OUTD (unused run)
site 005BF   ; OUTD (unused run)
site 005C1   ; OUTD (unused run)
site 005C3   ; OUTD (unused run)
site 005C5   ; OUTD (unused run)
site 005C7   ; OUTD (unused run)
site 005C9   ; OUTD (unused run)
site 005CB   ; OUTD (unused run)
site 005CD   ; OUTD (unused run)
site 005CF   ; OUTD (unused run)
site 005D1   ; OUTD (unused run)
site 005D3   ; OUTD (unused run)
site 005D5   ; OUTD (unused run)
site 005D7   ; OUTD (unused run)
site 005D9   ; OUTD (unused run)
site 005DB   ; OUTD (unused run)
site 005DD   ; OUTD (unused run)
site 005DF   ; OUTD (unused run)
site 005E1   ; OUTD (unused run)
site 005E3   ; OUTD (unused run)
site 005E5   ; OUTD (unused run)
site 005E7   ; OUTD (unused run)
site 005E9   ; OUTD (unused run)
site 005EB   ; OUTD (unused run)
site 005ED   ; OUTD (unused run)
site 005EF   ; OUTD (unused run)
site 005F1   ; OUTD (unused run)
site 005F3   ; OUTD (unused run)
site 005F5   ; OUTD (unused run)
site 005F7   ; OUTD (unused run)
site 005F9   ; OUTD (unused run)
site 005FB   ; OUTD (unused run)
site 005FD   ; OUTD (unused run)
site 005FF   ; OUTD (unused run)
site 00601   ; OUTD (unused run)
site 00603   ; OUTD (unused run)
site 00605   ; OUTD (unused run)
site 00607   ; OUTD (unused run)
site 00609   ; OUTD (unused run)
site 0060B   ; OUTD (unused run)

# Putt _ Putter _ Minigolf (Europe, Brazil).cht, "Infinite Balls": RAM $D178 is the BALL count
# on the status panel; held at $63 it shows BALL 99 and the count does not fall
poke "Infinite balls"
ar 00D1-7863
endpoke

# Putt _ Putter _ Minigolf (Europe, Brazil).cht, "Always On First Shot": RAM $D176 is the
# stroke number shown as NEXT on the status panel; held at 1 it stays NEXT 01 after every shot
poke "Always first shot"
ar 00D1-7601
endpoke

# Putt _ Putter _ Minigolf (Europe, Brazil).cht, "Enable Round Select after Select Mode
# screen": RAM $D020 at 1 shows a ROUND SELECT screen after the mode screen; the pad's Up
# changes the stage and Button 1 starts it
poke "Round select"
ar 00D0-2001
endpoke
