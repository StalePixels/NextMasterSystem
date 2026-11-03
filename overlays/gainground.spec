# Gain Ground (Europe, Brazil) (En), CRC32 3EC5E627, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input), plus these routine starts given with --entry, because no scanned path
# or recording reached them:
# - the game modes of the main loop's table at $00AA (bank, address): bank 7 $AF20,
#   $AFC6; bank 15 $800F, $8B9C, $8CF2, $9137; bank 0 $13AC, $00DA, $00DB, $0C94, $0CE1,
#   $0F32, $00EF;
# - the object handlers of the two-level tables at $17B5 (dispatched at $17AE) and $32AA
#   (dispatched at $309A), the 12 entries of the table at bank 14 $A9F8 (dispatched at
#   $54B3), and bank 14 $865E and $872D (called at $1334 and $5203).
# Decisions:
# - No free RST vector, so $0000 is the io vector.
# - The frame handler ($0136) turns the display off, uploads the queued name table
#   blocks and the sprite table, and turns the display on. When the HUD portrait
#   changes, the uploads run into the picture and the top 30-40 lines showed black.
#   toppal holds the display-off write, so the picture stays whole.
# - The HUD (name table columns 24-31, rows 0-23) has the priority bit, and sprites that
#   leave the play area to the right go behind it. In the reference those are the only
#   cells with the priority bit, and the HUD tiles have no colour-0 pixels while the
#   display is on, so the HUD hides every sprite pixel at x 192-255. The priority switch
#   did that at a cost of frames up to 123% while the HUD portrait changes; page 0 does
#   it with the sprite clip window instead (hud_clip, below).
name Gain Ground
cart 3EC5E627
hz 50		; No-Intro regions Europe, Brazil
toppal
vector 00 io
start 0003
site 0006E   ; IN A,($BF)
site 00072   ; OUT ($BF),A
site 00076   ; OUT ($BF),A
site 00119   ; IN A,($BF)
site 0013F   ; OUT ($BF),A
site 00143   ; OUT ($BF),A
site 0016D   ; OUT ($BF),A
site 00171   ; OUT ($BF),A
site 00188   ; OUT ($BF),A
site 0018C   ; OUT ($BF),A
site 00196   ; OUT ($BF),A
site 0019A   ; OUT ($BF),A
site 001D4   ; IN A,($DD)
site 001F3   ; OUT ($BF),A
site 001F7   ; OUT ($BF),A
site 00201   ; IN A,($BF)
site 0020C   ; OUT ($BF),A
site 0020F   ; OUT ($BF),A
site 00215   ; OUT ($BE),A
site 00221   ; OUT ($BE),A
site 0023E   ; OUT ($BF),A
site 00241   ; OUT ($BF),A
site 0029B   ; OUTI
site 0029D   ; OUTI
site 0029F   ; OUTI
site 002A1   ; OUTI
site 002A3   ; OUTI
site 002A5   ; OUTI
site 002A7   ; OUTI
site 002A9   ; OUTI
site 002AB   ; OUTI
site 002AD   ; OUTI
site 002AF   ; OUTI
site 002B1   ; OUTI
site 002B3   ; OUTI
site 002B5   ; OUTI
site 002B7   ; OUTI
site 002B9   ; OUTI
site 002BB   ; OUTI
site 002BD   ; OUTI
site 002BF   ; OUTI
site 002C1   ; OUTI
site 002C3   ; OUTI
site 002C5   ; OUTI
site 002C7   ; OUTI
site 002C9   ; OUTI
site 002CB   ; OUTI
site 002CD   ; OUTI
site 002CF   ; OUTI
site 002D1   ; OUTI
site 002D3   ; OUTI
site 002D5   ; OUTI
site 002D7   ; OUTI
site 002D9   ; OUTI
site 002DB   ; OUTI
site 002DD   ; OUTI
site 002DF   ; OUTI
site 002E1   ; OUTI
site 002E3   ; OUTI
site 002E5   ; OUTI
site 002E7   ; OUTI
site 002E9   ; OUTI
site 002EB   ; OUTI
site 002ED   ; OUTI
site 002EF   ; OUTI
site 002F1   ; OUTI
site 002F3   ; OUTI
site 002F5   ; OUTI
site 002F7   ; OUTI
site 002F9   ; OUTI
site 002FB   ; OUTI
site 002FD   ; OUTI
site 002FF   ; OUTI
site 00301   ; OUTI
site 00303   ; OUTI
site 00305   ; OUTI
site 00307   ; OUTI
site 00309   ; OUTI
site 0030B   ; OUTI
site 0030D   ; OUTI
site 0030F   ; OUTI
site 00311   ; OUTI
site 00313   ; OUTI
site 00315   ; OUTI
site 00317   ; OUTI
site 00319   ; OUTI
site 0031C   ; OUTD
site 0031E   ; OUTD
site 00320   ; OUTD
site 00322   ; OUTD
site 00324   ; OUTD
site 00326   ; OUTD
site 00328   ; OUTD
site 0032A   ; OUTD
site 0032C   ; OUTD
site 0032E   ; OUTD
site 00330   ; OUTD
site 00332   ; OUTD
site 00334   ; OUTD
site 00336   ; OUTD
site 00338   ; OUTD
site 0033A   ; OUTD
site 0033C   ; OUTD
site 0033E   ; OUTD
site 00340   ; OUTD
site 00342   ; OUTD
site 00344   ; OUTD
site 00346   ; OUTD
site 00348   ; OUTD
site 0034A   ; OUTD
site 0034C   ; OUTD
site 0034E   ; OUTD
site 00350   ; OUTD
site 00352   ; OUTD
site 00354   ; OUTD
site 00356   ; OUTD
site 00358   ; OUTD
site 0035A   ; OUTD
site 0035C   ; OUTD
site 0035E   ; OUTD
site 00360   ; OUTD
site 00362   ; OUTD
site 00364   ; OUTD
site 00366   ; OUTD
site 00368   ; OUTD
site 0036A   ; OUTD
site 0036C   ; OUTD
site 0036E   ; OUTD
site 00370   ; OUTD
site 00372   ; OUTD
site 00374   ; OUTD
site 00376   ; OUTD
site 00378   ; OUTD
site 0037A   ; OUTD
site 0037C   ; OUTD
site 0037E   ; OUTD
site 00380   ; OUTD
site 00382   ; OUTD
site 00384   ; OUTD
site 00386   ; OUTD
site 00388   ; OUTD
site 0038A   ; OUTD
site 0038C   ; OUTD
site 0038E   ; OUTD
site 00390   ; OUTD
site 00392   ; OUTD
site 00394   ; OUTD
site 00396   ; OUTD
site 00398   ; OUTD
site 0039A   ; OUTD
site 003A9   ; OUT ($BE),A
site 003AC   ; OUT ($BE),A
site 003C7   ; OUT ($BE),A
site 003CA   ; OUT ($BE),A
site 004BE   ; OUT ($BF),A
site 004C4   ; OUT ($BF),A
site 004CE   ; OUTI
site 004D3   ; OUTI
site 004EC   ; OUT ($BF),A
site 004F2   ; OUT ($BF),A
site 00501   ; OUTI
site 00508   ; OUT (C),A
site 0092F   ; OUT ($BF),A
site 00933   ; OUT ($BF),A
site 0094F   ; IN A,($DC)
site 0096C   ; IN A,($DD)
site 00EDF   ; IN A,($DC)
site 00F03   ; IN A,($DC)
site 00F07   ; IN A,($DD)
site 1C0FD   ; OUT ($7F),A
site 1C12B   ; OTIR, sound command $B1/$B2 ($810B, $8102), table at bank 7 $898F
site 1C134   ; OTIR, the same routine
site 1C170   ; OUT ($7F),A, sound commands $A5-$AF ($8166), dispatcher at bank 7 $813B
site 1C174   ; OUT ($7F),A, the same branch
site 1C1C3   ; OUT ($7F),A
site 1C1C7   ; OUT ($7F),A
site 1C1D0   ; OUT ($7F),A
site 1C1E1   ; OUT ($7F),A
site 1C1F7   ; OUT ($7F),A
site 1C1FB   ; OUT ($7F),A
site 1C1FF   ; OUT ($7F),A
site 1C202   ; OUT ($7F),A
site 1C20B   ; OUT ($7F),A
site 1C40C   ; OUT ($7F),A
site 1C49C   ; OUT ($7F),A
site 1C4C3   ; OUT ($7F),A
site 1C4C8   ; OUT ($7F),A
site 1C564   ; OUTI
site 1C566   ; OUTI
site 1C568   ; OUTI
site 1C56A   ; OUTI
site 1C56C   ; OUTI
site 1C56E   ; OUTI
site 1C570   ; OUTI
site 1C572   ; OUTI
site 1C574   ; OUTI
site 1C576   ; OUTI
site 1C578   ; OUTI
site 1C5AE   ; OUT ($7F),A
site 1C604   ; OUT ($7F),A
site 1C643   ; OUT ($7F),A
site 1C6A5   ; OUT ($7F),A
site 1C6C5   ; OUT ($7F),A
site 1C711   ; OUT ($7F),A
site 1C71B   ; OUT ($7F),A
site 1C763   ; OUT ($7F),A
site 1EF3A   ; OUT ($3F),A
site 1EF3C   ; IN A,($DD)
site 1EF46   ; OUT ($3F),A
site 1EF48   ; IN A,($DD)
site 1EF96   ; OUT ($3E),A
site 1EF99   ; OUT ($F2),A
site 1EFA1   ; OUT ($3E),A
site 1EFA5   ; OUT ($3F),A
site 1EFAB   ; IN A,($BF)
site 1EFAD   ; IN A,($BF)
site 1EFB9   ; IN A,($BF)
site 1EFC8   ; OUT ($3F),A
site 1EFCA   ; IN A,($DD)
site 1EFD4   ; OUT ($3F),A
site 1EFD6   ; IN A,($DD)
site 1EFE4   ; OUT ($3F),A
site 1EFEB   ; OUT ($3F),A
site 3C245   ; OUT ($BF),A
site 3C24B   ; OUT ($BF),A
site 3C255   ; OUTI
site 3C25A   ; OUTI
# Once a frame, both frame handlers ($0136 and $0178) far-call hud_clip in place of
# their frame counter increment.
asm 00161 7          ; LD HL,($C20E) : INC HL : LD ($C20E),HL
    rst $00
    db far_io, pg_hud_clip, ent_hud_clip
    nop
    nop
    nop
endasm
asm 001B5 7          ; LD HL,($C20E) : INC HL : LD ($C20E),HL
    rst $00
    db far_io, pg_hud_clip, ent_hud_clip
    nop
    nop
    nop
endasm
page 0 hud_clip
; hud_clip: the game's frame counter increment ($C20E), then the sprite clip window:
; right edge at SMS x 191 while the HUD shows (name table cell column 24, row 12 has
; the priority bit), at x 255 when it does not. Runs in the frame handler with
; interrupts off. Runtime internals: the VRAM copy in pages 28-29 (SHADOW_PAGE in
; memplan.inc), mapped at $4000 for one read; the sprite clip values of clip_update
; (fw2.asm) for a 192-line screen. Changes A, HL, F, as the replaced code does.
    OPT --zxnext            ; NEXTREG, ADD HL,nn
hud_clip:
    ld hl,($C20E)
    inc hl
    ld ($C20E),hl
    ld hl,(nt_base)
    add hl,(12*32+24)*2+1   ; the attribute byte of cell (24,12)
    ld a,h
    and $3F
    ld h,a
    rlca
    rlca
    rlca
    and 1
    add a,28                ; SHADOW_PAGE
    nextreg $52,a
    ld a,h
    and $1F
    or $40
    ld h,a
    ld l,(hl)
    ld a,(cur_mmu+2)
    nextreg $52,a
    nextreg $1C,%00000010   ; reset the sprite clip index
    ld a,(vdp_regs+0)
    and $20                 ; column 0 hidden: the window starts 8 pixels in
    jr z,hud_clip__x
    ld a,4
hud_clip__x:
    add a,17
    nextreg $19,a
    ld a,l
    and $10
    ld a,144                ; SMS x 255 (over-border units of 2 pixels)
    jr z,hud_clip__r
    ld a,112                ; SMS x 191
hud_clip__r:
    nextreg $19,a
    nextreg $19,32
    nextreg $19,223
    ret
endpage
mapldk 00078   # LD HL,$FFFC; LD (HL),$00
maphl 0007E   # LD (HL),$00, HL = $FFFD
maphl 00081   # LD (HL),$01, HL = $FFFE
maphl 00084   # LD (HL),$0E, HL = $FFFF
mapst 0009C   ; LD ($FFFF),A
mapst 0015E   ; LD ($FFFF),A
mapst 001FB   ; LD ($FFFF),A
mapst 0043F   ; LD ($FFFF),A
mapst 004A2   ; LD ($FFFF),A
mapst 0052B   ; LD ($FFFF),A
mapst 00532   ; LD ($FFFF),A
mapst 008E2   ; LD ($FFFF),A
mapst 008EB   ; LD ($FFFF),A
mapst 00D5E   ; LD ($FFFF),A
mapst 00D95   ; LD ($FFFF),A
mapst 00DA1   ; LD ($FFFF),A
mapst 00DC4   ; LD ($FFFF),A
mapst 00DD0   ; LD ($FFFF),A
mapst 00DEA   ; LD ($FFFF),A
mapst 00DFA   ; LD ($FFFF),A
mapst 00E15   ; LD ($FFFF),A
mapst 00E1B   ; LD ($FFFF),A
mapst 00E48   ; LD ($FFFF),A
mapst 00E62   ; LD ($FFFF),A
mapst 00E73   ; LD ($FFFF),A
mapst 01477   ; LD ($FFFF),A
mapst 01520   ; LD ($FFFF),A
mapst 01547   ; LD ($FFFF),A
mapst 0154D   ; LD ($FFFF),A
mapst 01574   ; LD ($FFFF),A
mapst 01608   ; LD ($FFFF),A
mapst 0162A   ; LD ($FFFF),A
mapst 0163E   ; LD ($FFFF),A
mapst 01696   ; LD ($FFFF),A
mapst 016A0   ; LD ($FFFF),A
mapst 016B2   ; LD ($FFFF),A
mapst 016D0   ; LD ($FFFF),A
mapst 016E4   ; LD ($FFFF),A
mapst 01740   ; LD ($FFFF),A
mapst 0176D   ; LD ($FFFF),A
mapst 017B1   ; LD ($FFFF),A
mapst 01924   ; LD ($FFFF),A
mapst 019A2   ; LD ($FFFF),A
mapst 01DAB   ; LD ($FFFF),A
mapst 01E15   ; LD ($FFFF),A
mapst 01E68   ; LD ($FFFF),A
mapst 02392   ; LD ($FFFF),A
# The byte scan's low rows (0A3CD, 0AB30, 175DC, 2FD5B, 3A09A, and the mapper store
# pattern at 02127) are not patched: the five sites lie in graphics and table data in banks
# 2, 5, 11 and 14, and 02127 is inside the CALL $224F at 02125.

# Gain Ground (Europe, Brazil).cht, "Infinite Lives - Both Players"
poke "Infinite lives"
gg 00A-F7E-3BE
endpoke

# Gain Ground (Europe, Brazil).cht, "Infinite Time"
poke "Infinite time"
gg B62-60E-3BE
endpoke

# Gain Ground (Europe, Brazil).cht, "Level Select"
poke "Start round"
ar 00C4-00??
endpoke
