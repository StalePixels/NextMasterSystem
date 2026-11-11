# Wimbledon II (Europe, Brazil) (En), CRC32 7F3AFE58, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs of 600 s
# (random input) and 120 s (no input), then decided by hand.
#
# Decisions:
# - No free RST vector, so $0000-$0002 (DI; IM 1) is the io vector and the game starts
#   at $0003.
# - The main loop at $0193 runs the game state from a table of 3-byte entries (bank,
#   address) at $0D5C-$0E45 through CALL $0017 (JP (HL)) at $01A8, as in Wimbledon. The
#   sites in those handlers were taken from a scan with the table's addresses as entry
#   points.
# - Bank 0 has a block of JP vectors at $0070-$016B for the other banks. The routines
#   behind them were scanned with the vectors as entry points. So were the routines at
#   $0789, $082E and $088B in bank 0 and $4C42 in bank 1, which have the same form as
#   their neighbours but no caller that the scan found.
# - Not patched: IN A,($06) at $00B6 is the middle of the vector JP $06DB at $00B5;
#   OUT ($2B),A at $5A34 and IN A,($F6) at $7A45 are in bank-1 data that the scanner
#   reads as code through the table at $2DA9, which has 7 entries (index $C900-9, 0-6)
#   but is read on into the text after it.
name Wimbledon II
cart 7F3AFE58
hz 50		; No-Intro region Europe
vector 00 io
start 0003
site 0001A   ; OUT (C),L
site 0001C   ; OUT (C),H
site 0003A   ; IN A,($BF)
site 00171   ; IN A,(C)
site 00178   ; OUT ($BF),A
site 0017C   ; OUT ($BF),A
site 001F0   ; OUT ($3F),A
site 001F2   ; IN A,($DD)
site 001FC   ; OUT ($3F),A
site 001FE   ; IN A,($DD)
site 00246   ; OUT ($3E),A
site 00249   ; OUT ($F2),A
site 00251   ; OUT ($3E),A
site 00255   ; OUT ($3F),A
site 0025D   ; IN A,($BF)
site 0025F   ; IN A,($BF)
site 0026B   ; IN A,($BF)
site 00285   ; IN A,($DD)
site 002B0   ; OUT ($BF),A
site 002B4   ; OUT ($BF),A
site 002B9   ; OUT ($BE),A
site 00394   ; OUT ($BF),A
site 00398   ; OUT ($BF),A
site 0039B   ; IN A,($BF)
site 003AC   ; OUT ($BF),A
site 003B0   ; OUT ($BF),A
site 003B3   ; IN A,($DC)
site 003D0   ; IN A,($DD)
site 003F5   ; IN A,($BF)
site 00400   ; OUT ($BF),A
site 00403   ; OUT ($BF),A
site 00410   ; OUT ($BE),A
site 0054F   ; OUTI
site 00551   ; OUTI
site 00553   ; OUTI
site 00555   ; OUTI
site 00557   ; OUTI
site 00559   ; OUTI
site 0055B   ; OUTI
site 0055D   ; OUTI
site 0055F   ; OUTI
site 00561   ; OUTI
site 00563   ; OUTI
site 00565   ; OUTI
site 00567   ; OUTI
site 00569   ; OUTI
site 0056B   ; OUTI
site 0056D   ; OUTI
site 0056F   ; OUTI
site 00571   ; OUTI
site 00573   ; OUTI
site 00575   ; OUTI
site 00577   ; OUTI
site 00579   ; OUTI
site 0057B   ; OUTI
site 0057D   ; OUTI
site 0057F   ; OUTI
site 00581   ; OUTI
site 00583   ; OUTI
site 00585   ; OUTI
site 00587   ; OUTI
site 00589   ; OUTI
site 0058B   ; OUTI
site 0058D   ; OUTI
site 0058F   ; OUTI
site 00591   ; OUTI
site 00593   ; OUTI
site 00595   ; OUTI
site 00597   ; OUTI
site 00599   ; OUTI
site 0059B   ; OUTI
site 0059D   ; OUTI
site 0059F   ; OUTI
site 005A1   ; OUTI
site 005A3   ; OUTI
site 005A5   ; OUTI
site 005A7   ; OUTI
site 005A9   ; OUTI
site 005AB   ; OUTI
site 005AD   ; OUTI
site 005AF   ; OUTI
site 005B1   ; OUTI
site 005B3   ; OUTI
site 005B5   ; OUTI
site 005B7   ; OUTI
site 005B9   ; OUTI
site 005BB   ; OUTI
site 005BD   ; OUTI
site 005BF   ; OUTI
site 005C1   ; OUTI
site 005C3   ; OUTI
site 005C5   ; OUTI
site 005C7   ; OUTI
site 005C9   ; OUTI
site 005CB   ; OUTI
site 005CD   ; OUTI
site 005CF   ; OUTI
site 005D1   ; OUTI
site 005D3   ; OUTI
site 005D5   ; OUTI
site 005D7   ; OUTI
site 005D9   ; OUTI
site 005DB   ; OUTI
site 005DD   ; OUTI
site 005DF   ; OUTI
site 005E1   ; OUTI
site 005E3   ; OUTI
site 005E5   ; OUTI
site 005E7   ; OUTI
site 005E9   ; OUTI
site 005EB   ; OUTI
site 005ED   ; OUTI
site 005EF   ; OUTI
site 005F1   ; OUTI
site 005F3   ; OUTI
site 005F5   ; OUTI
site 005F7   ; OUTI
site 005F9   ; OUTI
site 005FB   ; OUTI
site 005FD   ; OUTI
site 005FF   ; OUTI
site 00601   ; OUTI
site 00603   ; OUTI
site 00605   ; OUTI
site 00607   ; OUTI
site 00609   ; OUTI
site 0060B   ; OUTI
site 0060D   ; OUTI
site 0060F   ; OUTI
site 00611   ; OUTI
site 00613   ; OUTI
site 00615   ; OUTI
site 00617   ; OUTI
site 00619   ; OUTI
site 0061B   ; OUTI
site 0061D   ; OUTI
site 0061F   ; OUTI
site 00621   ; OUTI
site 00623   ; OUTI
site 00625   ; OUTI
site 00627   ; OUTI
site 00629   ; OUTI
site 0062B   ; OUTI
site 0062D   ; OUTI
site 0062F   ; OUTI
site 00631   ; OUTI
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
site 00656   ; OTIR
site 00668   ; OUT ($BE),A
site 0066E   ; OUT ($BE),A
site 00682   ; OUT ($BE),A
site 00685   ; OUT ($BE),A
site 0069A   ; OUTI
site 0069F   ; OUT ($BE),A
site 006B5   ; OUT (C),A
site 006BD   ; OUT (C),A
site 006DD   ; OUT (C),E
site 006DF   ; OUT (C),D
site 006F0   ; OUT (C),E
site 006F6   ; OUT (C),D
site 00751   ; OUT (C),B
site 00774   ; OUT (C),A
site 007B3   ; OUT ($BE),A
site 00CCE   ; OUT (C),A
site 00CD4   ; OUT (C),A
site 00CE0   ; OUT (C),A
site 00CE6   ; OUT (C),A
site 0189D   ; OUT ($BF),A
site 018A1   ; OUT ($BF),A
site 018A6   ; OUT ($BF),A
site 018AA   ; OUT ($BF),A
site 018B5   ; OTIR
site 018C2   ; OTIR
site 01A52   ; OUT (C),E
site 01A54   ; OUT (C),D
site 01A6B   ; OUT (C),E
site 01A6D   ; OUT (C),D
site 01A70   ; OUTI
site 01A72   ; OUTI
site 01A7C   ; OUT (C),E
site 01A7E   ; OUT (C),D
site 01A81   ; OUTI
site 01A83   ; OUTI
site 01A8D   ; OUT (C),E
site 01A8F   ; OUT (C),D
site 01A92   ; OUTI
site 01A94   ; OUTI
site 01A9E   ; OUT (C),E
site 01AA0   ; OUT (C),D
site 01AA3   ; OUTI
site 01AA5   ; OUTI
site 01AAF   ; OUT (C),E
site 01AB1   ; OUT (C),D
site 01AB4   ; OUTI
site 01AB6   ; OUTI
site 01AC0   ; OUT (C),E
site 01AC2   ; OUT (C),D
site 01AC5   ; OUTI
site 01AC7   ; OUTI
site 01AD1   ; OUT (C),E
site 01AD3   ; OUT (C),D
site 01AD6   ; OUTI
site 01AD8   ; OUTI
site 01AE2   ; OUT (C),E
site 01AE4   ; OUT (C),D
site 01AE7   ; OUTI
site 01AE9   ; OUTI
site 01AF3   ; OUT (C),E
site 01AF5   ; OUT (C),D
site 01AF8   ; OUTI
site 01AFA   ; OUTI
site 01B04   ; OUT (C),E
site 01B06   ; OUT (C),D
site 01B09   ; OUTI
site 01B0B   ; OUTI
site 01B15   ; OUT (C),E
site 01B17   ; OUT (C),D
site 01B1A   ; OUTI
site 01B1C   ; OUTI
site 01B26   ; OUT (C),E
site 01B28   ; OUT (C),D
site 01B2B   ; OUTI
site 01B2D   ; OUTI
site 01B37   ; OUT (C),E
site 01B39   ; OUT (C),D
site 01B3C   ; OUTI
site 01B3E   ; OUTI
site 01B48   ; OUT (C),E
site 01B4A   ; OUT (C),D
site 01B4D   ; OUTI
site 01B4F   ; OUTI
site 01B59   ; OUT (C),E
site 01B5B   ; OUT (C),D
site 01B5E   ; OUTI
site 01B60   ; OUTI
site 01B6A   ; OUT (C),E
site 01B6C   ; OUT (C),D
site 01B6F   ; OUTI
site 01B71   ; OUTI
site 01B7B   ; OUT (C),E
site 01B7D   ; OUT (C),D
site 01B80   ; OUTI
site 01B82   ; OUTI
site 01B8C   ; OUT (C),E
site 01B8E   ; OUT (C),D
site 01B91   ; OUTI
site 01B93   ; OUTI
site 01B9D   ; OUT (C),E
site 01B9F   ; OUT (C),D
site 01BA2   ; OUTI
site 01BA4   ; OUTI
site 01BAE   ; OUT (C),E
site 01BB0   ; OUT (C),D
site 01BB3   ; OUTI
site 01BB5   ; OUTI
site 01BBF   ; OUT (C),E
site 01BC1   ; OUT (C),D
site 01BC4   ; OUTI
site 01BC6   ; OUTI
site 01BD0   ; OUT (C),E
site 01BD2   ; OUT (C),D
site 01BD5   ; OUTI
site 01BD7   ; OUTI
site 01BE1   ; OUT (C),E
site 01BE3   ; OUT (C),D
site 01BE6   ; OUTI
site 01BE8   ; OUTI
site 01BF2   ; OUT (C),E
site 01BF4   ; OUT (C),D
site 01BF7   ; OUTI
site 01BF9   ; OUTI
site 01C03   ; OUT (C),E
site 01C05   ; OUT (C),D
site 01C08   ; OUTI
site 01C0A   ; OUTI
site 01C14   ; OUT (C),E
site 01C16   ; OUT (C),D
site 01C19   ; OUTI
site 01C1B   ; OUTI
site 01C25   ; OUT (C),E
site 01C27   ; OUT (C),D
site 01C2A   ; OUTI
site 01C2C   ; OUTI
site 01C36   ; OUT (C),E
site 01C38   ; OUT (C),D
site 01C3B   ; OUTI
site 01C3D   ; OUTI
site 01C4A   ; OUT ($BF),A
site 01C4E   ; OUT ($BF),A
site 01C53   ; OUT ($BF),A
site 01C57   ; OUT ($BF),A
site 01CA4   ; OUT (C),A
site 01CB6   ; OUT (C),A
site 01E5F   ; OUT (C),D
site 01F0C   ; OUT (C),E
site 01F0E   ; OUT (C),D
site 01F11   ; OUT (C),A
site 01F18   ; OUT (C),A
site 01F1F   ; OUT (C),A
site 01F26   ; OUT (C),A
site 022D0   ; OUT ($BF),A
site 022D4   ; OUT ($BF),A
site 02300   ; IN A,($7E)
site 0230A   ; OUT ($BF),A
site 0230E   ; OUT ($BF),A
site 02323   ; OUT ($BF),A
site 02327   ; OUT ($BF),A
site 0232B   ; OUT ($BE),A
site 023B1   ; OUT (C),E
site 023B3   ; OUT (C),D
site 0240F   ; OUT (C),E
site 02411   ; OUT (C),D
site 0246C   ; OUTI
site 0246E   ; OUT (C),A
site 02471   ; OUTI
site 02473   ; OUTI
site 02475   ; OUTI
site 02477   ; OUT (C),A
site 0247A   ; OUTI
site 0247C   ; OUTI
site 0247E   ; OUTI
site 02480   ; OUT (C),A
site 02483   ; OUTI
site 02485   ; OUTI
site 02487   ; OUTI
site 02489   ; OUT (C),A
site 0248C   ; OUTI
site 0248E   ; OUTI
site 02490   ; OUTI
site 02492   ; OUT (C),A
site 02495   ; OUTI
site 02497   ; OUTI
site 02499   ; OUTI
site 0249B   ; OUT (C),A
site 0249E   ; OUTI
site 024A0   ; OUTI
site 024A2   ; OUTI
site 024A4   ; OUT (C),A
site 024A7   ; OUTI
site 024A9   ; OUTI
site 024AB   ; OUTI
site 024AD   ; OUT (C),A
site 04348   ; OUTI
site 04369   ; OUT (C),A
site 0436B   ; OUT (C),D
site 04381   ; OUT (C),A
site 04383   ; OUT (C),D
site 0447F   ; OUT (C),A
site 04484   ; OUT (C),A
site 04497   ; OUT (C),A
site 0449D   ; OUT (C),A
site 0450D   ; OUT (C),A
site 0450F   ; OUT (C),D
site 04513   ; OUT (C),A
site 04515   ; OUT (C),D
site 0451B   ; OUT (C),A
site 0451D   ; OUT (C),E
site 047AA   ; OUT (C),A
site 047AF   ; OUT (C),A
site 047B6   ; OUT (C),A
site 047BB   ; OUT (C),A
site 047E5   ; OUT (C),A
site 047EB   ; OUT (C),A
site 047F2   ; OUT (C),A
site 047F8   ; OUT (C),A
site 048CB   ; OUT (C),D
site 048CD   ; OUT (C),D
site 048DF   ; OUT ($BF),A
site 048E2   ; OUT ($BF),A
site 048ED   ; OUT ($BE),A
site 048F2   ; OUT ($BE),A
site 048FA   ; OUT ($BF),A
site 048FD   ; OUT ($BF),A
site 04901   ; OUT ($BE),A
site 04906   ; OUT ($BE),A
site 04912   ; OUT ($BF),A
site 04915   ; OUT ($BF),A
site 04919   ; OUT ($BE),A
site 0491E   ; OUT ($BE),A
site 04955   ; OUT (C),A
site 0495A   ; OUT (C),A
site 04B70   ; OUT (C),A
site 04BC1   ; OUT (C),A
site 14005   ; OUT (C),A
site 14007   ; OUT (C),B
site 1400A   ; OUT (C),A
site 1400C   ; OUT (C),B
site 1412C   ; OUT (C),A
site 1412E   ; OUT (C),B
site 14136   ; OUT (C),A
site 14138   ; OUT (C),B
site 20005   ; OUT (C),A
site 20007   ; OUT (C),B
site 2000A   ; OUT (C),A
site 2000C   ; OUT (C),B
site 3C1FA   ; OUT ($7F),A
site 3C452   ; OTIR
site 3C56A   ; OUT ($7F),A
site 3C574   ; OUT ($7F),A
site 3C591   ; OUT ($7F),A
site 3C6B9   ; OUT ($7F),A
site 3C6D3   ; OUT ($7F),A
site 3C76C   ; OUT ($7F),A
site 3C819   ; OUT ($7F),A
site 3C822   ; OUT ($7F),A
site 3C832   ; OUT ($7F),A
site 3C8B2   ; OUT ($7F),A
mapldk 0017E   # LD HL,$FFFC; LD (HL),$00
maphl 00184   # LD (HL),$00, HL = $FFFD
maphl 00187   # LD (HL),$01, HL = $FFFE
maphl 0018A   # LD (HL),$02, HL = $FFFF
mapst 001A5   ; LD ($FFFF),A
mapst 0029D   ; LD ($FFFF),A
mapst 0036D   ; LD ($FFFF),A
mapst 00720   ; LD ($FFFF),A
mapst 0075D   ; LD ($FFFF),A
mapst 00782   ; LD ($FFFF),A
mapst 007C1   ; LD ($FFFF),A
mapst 007D4   ; LD ($FFFF),A
mapst 00840   ; LD ($FFFF),A
mapst 0089C   ; LD ($FFFF),A
mapst 009DB   ; LD ($FFFF),A
mapst 009E2   ; LD ($FFFF),A
mapst 00A02   ; LD ($FFFF),A
mapst 00A1D   ; LD ($FFFF),A
mapst 01803   ; LD ($FFFF),A
mapst 0181C   ; LD ($FFFF),A
mapst 01F01   ; LD ($FFFF),A
mapst 01F33   ; LD ($FFFF),A
mapst 023B8   ; LD ($FFFF),A
mapst 02405   ; LD ($FFFF),A
mapst 02416   ; LD ($FFFF),A
mapst 02463   ; LD ($FFFF),A
mapst 0430D   ; LD ($FFFF),A
mapst 04355   ; LD ($FFFF),A
mapst 04397   ; LD ($FFFF),A
mapst 043C0   ; LD ($FFFF),A
mapst 04402   ; LD ($FFFF),A
mapst 04434   ; LD ($FFFF),A
mapst 04A4B   ; LD ($FFFF),A
mapst 04A69   ; LD ($FFFF),A
mapst 04A74   ; LD ($FFFF),A
mapst 04A98   ; LD ($FFFF),A
mapst 04ADF   ; LD ($FFFF),A
mapst 04B32   ; LD ($FFFF),A
mapst 04BAA   ; LD ($FFFF),A
mapst 04BE5   ; LD ($FFFF),A
mapst 04C1C   ; LD ($FFFF),A
mapst 04C30   ; LD ($FFFF),A
mapst 04C50   ; LD ($FFFF),A
mapst 04C61   ; LD ($FFFF),A

# The frame handler's palette upload at $0545 (called at $02C4, $02DA and $0426): CRAM 0-31
# from $C3C0 through the unrolled OUTI run at $060F-$064D, every frame. Through the runtime
# that is about 190,000 cycles a frame, and with the rest of the handler the frame handler
# runs past the next frame event. Its EI at $0298 then takes the next interrupt at once, and
# the stack grows by 28 bytes a frame until it leaves RAM and the game restarts. Page 0 entry
# pal writes only the entries whose colour changes.
asm 00545 5   ; LD HL,$C000; RST $18; LD HL,$C3C0 (JP $060F follows)
    rst $00
    db far_io, pg_pal, ent_pal
    ret
endasm

# The frame handler's sprite tile upload at $2409 sends 8 tiles through $2467: each tile
# row is 3 bytes (OUTI) and a zero byte (OUT (C),A), 32 bytes from 32 source bytes. Through
# the runtime each row is two traps, about 50,000 cycles a tile and up to 530,000 in a frame
# with the rest of the handler: past the next frame event, so the handler's EI at $0298
# takes the next interrupt at once and the stack grows until the game restarts. Page 0
# entry t3 writes the tile with jt_vwrite.
asm 02467 5   ; XOR A; OUTI; OUTI; OUTI (8 rows of OUTI x3, OUT (C),A, INC HL follow)
    rst $00
    db far_io, pg_t3, ent_t3
    ret
endasm

# Wimbledon II (Europe) (Action Replay).cht, "CPU/P2 Never Scores": RAM $CAD0 is the CPU
# player's point count in the current game; held at 0, the CPU never gets a point
poke "CPU never scores"
ar 00CA-D000
endpoke

# Wimbledon II (Europe) (Action Replay).cht, "P1 Score Modifier": RAM $CAD1 is player 1's
# point count in the current game (0 = 0, 1 = 15, 2 = 30, 3 = 40), held at the value chosen
poke "P1 score ??"
ar 00CA-D1??
endpoke

# Wimbledon II _ Wimbledon (Europe, Brazil).cht, "P2 Games Won Modifier": RAM $CAD2 is the
# CPU player's game count in the set, held at the value chosen; at 5 the CPU's next game
# ends a one-set match
poke "CPU games ??"
ar 00CA-D2??
endpoke

# Wimbledon II _ Wimbledon (Europe, Brazil).cht, "Infinite Attribute Points": RAM $CB2F is the
# points left to spend in Tour Mode, held at 80
poke "Infinite points"
ar 00CB-2F50
endpoke

# Wimbledon II _ Wimbledon (Europe, Brazil).cht, "Start with ?? Attribute Points, instead of
# 20": a Tour Mode player starts with 30 points to spend
poke "Start with 30 points"
gg 1E9-A37-B3A
endpoke

# Wimbledon II _ Wimbledon (Europe, Brazil).cht, "Max Speed": RAM $C436 is the Tour Mode
# player's speed, held at 20
poke "Max speed"
ar 00C4-3614
endpoke

# Wimbledon II _ Wimbledon (Europe, Brazil).cht, "Max Power": RAM $C437 is the Tour Mode
# player's power, held at 20
poke "Max power"
ar 00C4-3714
endpoke

# Wimbledon II _ Wimbledon (Europe, Brazil).cht, "Max Skill": RAM $C438 is the Tour Mode
# player's skill, held at 20
poke "Max skill"
ar 00C4-3814
endpoke

# Wimbledon II _ Wimbledon (Europe, Brazil).cht, "Max Stamina": RAM $C439 is the Tour Mode
# player's stamina, held at 20
poke "Max stamina"
ar 00C4-3914
endpoke

page 0 pal t3
; pal: CRAM 0-31 from $C3C0. Each entry whose colour differs from the runtime's copy (cram,
; $E04D) gets the VDP address and a write through the I/O RST; the VDP is then left as the
; 32 writes leave it (cram_upd, as in California Games). Returns as the OUTI run does:
; HL = $C3E0, C = $BE, B 32 lower, A kept.
pal:    push af
        ld a,b
        sub 32
        push af
        push de
        ld hl,$C3C0
        ld bc,$2000             ; 32 entries from index 0
        call cram_upd
        pop de
        pop af
        ld b,a
        ld c,$BE
        pop af
        ret
; HL = the source, C = the first CRAM index, B = the entries. Each entry
; whose colour (low 6 bits) differs from cram gets the VDP address and a
; write through the I/O RST; then the VDP state is as B writes from index C
; leave it: address C + B, code 3, latch clear, read buffer the last byte.
cram_upd:
        ld de,cram
        ld a,e
        add a,c
        ld e,a                  ; cram is inside one 256-byte page
.lp:    ld a,(hl)
        and $3F
        ex de,hl
        cp (hl)
        ex de,hl
        jr z,.same
        ld a,c
        ld (vdp_addr),a
        xor a
        ld (vdp_addr+1),a
        ld (vdp_latch),a
        ld a,3
        ld (vdp_code),a
        ld a,(hl)
        rst $00
        db $04                  ; OUT ($BE),A
.same:  inc hl
        inc de
        inc c
        djnz .lp
        dec hl
        ld a,(hl)
        inc hl
        ld (vdp_rbuf),a
        ld a,c
        ld (vdp_addr),a
        xor a
        ld (vdp_addr+1),a
        ld (vdp_latch),a
        ld a,3
        ld (vdp_code),a
        ret
;
; t3: one tile from HL to the VDP's address as $2467 writes it: 8 rows of 3 source bytes and
; a zero, the source 4 bytes a row. Returns as $2467 does: HL 32 higher, B 24 lower,
; C = $BE, A = 0. With the VDP on CRAM (code 3) the 32 bytes go through the I/O RST.
t3:     push bc
        push de
        push ix
        push iy
        ld a,(vdp_code)
        cp 3
        jr z,.slow
        ld de,(vdp_addr)
        ld bc,$0308             ; 8 runs of 3 bytes
        ld ix,4
        ld iy,4
        xor a                   ; the source as the game sees it
        call jt_vwrite
        inc de
        inc de
        inc de
        push hl
        ld hl,t3_zero
        ld bc,$0108             ; 8 runs of 1 byte, the same zero
        ld ix,0
        ld a,1                  ; the source as mapped now
        call jt_vwrite
        pop hl
        jr .done
.slow:  push hl
        ld e,8
.row:   ld d,3
.byte:  call jt_peek
        rst $00
        db $04                  ; OUT ($BE),A
        inc hl
        dec d
        jr nz,.byte
        xor a
        rst $00
        db $04
        inc hl
        dec e
        jr nz,.row
        pop hl
.done:  ld bc,32
        add hl,bc
        pop iy
        pop ix
        pop de
        pop bc
        ld a,b
        sub 24
        ld b,a
        ld c,$BE
        xor a
        ret
t3_zero: db 0
endpage
