# Alex Kidd - The Lost Stars (World), CRC32 C13896D5, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, checked against reference I/O logs
# (600 s of random input, 180 s of the attract mode): the scan found every I/O and mapper
# site that the logs ran.
# Decisions:
# - No RST vector holds $FF fill, and the game uses no RST but $38, so $0000-$0002 (IM 1;
#   the first byte of LD SP,$DFF0) is the io vector and the game starts at $0005 with SP $DFF0.
# - $02A8, $02DA, $0542, $05FF, $0619 and $0635 are VRAM write routines that nothing calls;
#   their I/O is patched, at no cost.
# - The byte-scan I/O patterns in banks 5 to 15 lie where no path or recording reaches; the
#   medium ones are data: packed data in bank 5, level data in bank 9 and a word table at
#   $B3C0 in banks 12 to 15 (data/scan-verdicts.tsv).
# - The tile unpacker $0551 (called with HL = the packed data in slot 2 and DE = a VRAM
#   address) unpacks four bit planes, each to every fourth VRAM byte, the next plane one
#   byte on. Each plane is a list of codes: 00 00 ends it, 00 n v is n bytes v, FF v is two
#   bytes v, and any other byte is itself. The game sets the VRAM address before every byte,
#   so a byte cost three traps: the Next showed round 1 about 50 frames after the reference
#   (sg1000m3, the same presses), and with the page about 50 frames before it. Page 0,
#   entry unpack, does the whole routine: it unpacks each plane into buf and writes buf with
#   jt_vwrite (runs of one byte, VRAM step 4). The VRAM after it is the same as with the
#   traps (checked byte for byte at game frame 1100). The cave at $0551 replaces EX DE,HL; LD C,4; PUSH HL; LD A,(DE) with the far call and a RET;
#   the routine's own I/O keeps its site lines but no longer runs.
# - priority: the castles and towers along the ground of round 1 have tiles with the priority
#   bit (written by the column streamer $3E9E); the reference logs show priority tiles on the
#   screen in 31,933 of 35,954 frames. It costs about 1% of a play frame (median 19.1% with
#   it, 18.0% without).
name Alex Kidd - The Lost Stars
cart C13896D5
hz any		; No-Intro region World
vector 00 io
priority
start 0005 DFF0
site 0003E   ; OUT ($BF),A
site 00043   ; OUT ($BF),A
site 00092   ; OUT (C),L
site 00094   ; OUT (C),H
site 00099   ; OUT (C),L
site 0009B   ; OUT (C),H
site 000DB   ; IN A,($BF)
site 00114   ; IN A,($DD)
site 0020C   ; OUT ($DE),A
site 0020E   ; IN A,($DC)
site 00219   ; IN A,($DD)
site 00250   ; OUT ($BF),A
site 00257   ; OUT ($BF),A
site 0025C   ; OUT ($BF),A
site 00261   ; OUT ($BF),A
site 00269   ; IN A,($BE)
site 00273   ; OUT ($BE),A
site 00278   ; OUT ($BE),A
site 0027C   ; OUT ($BE),A
site 00280   ; OUT ($BE),A
site 00291   ; OUT ($BE),A
site 00296   ; OUT ($BE),A
site 0029A   ; OUT ($BE),A
site 0029E   ; OUT ($BE),A
site 002B0   ; OUT ($BE),A
site 002B5   ; OUT ($BE),A
site 002B9   ; OUT ($BE),A
site 002BF   ; OUT ($BE),A
site 002D1   ; OUT ($BE),A
site 002E0   ; OUT ($BE),A
site 002E5   ; OUT ($BE),A
site 002F7   ; OUT ($BF),A
site 002FB   ; OUT ($BF),A
site 00308   ; OUT ($BF),A
site 0030C   ; OUT ($BF),A
site 00319   ; OUT ($BF),A
site 0031D   ; OUT ($BF),A
site 0032A   ; OUT ($BF),A
site 0032E   ; OUT ($BF),A
site 0037B   ; OUT ($BF),A
site 0037F   ; OUT ($BF),A
site 00384   ; OUT ($BE),A
site 003FD   ; OUTI
site 003FF   ; OUTI
site 00401   ; OUTI
site 00403   ; OUTI
site 00405   ; OUTI
site 00407   ; OUTI
site 00409   ; OUTI
site 0040B   ; OUTI
site 0040D   ; OUTI
site 0040F   ; OUTI
site 00411   ; OUTI
site 00413   ; OUTI
site 00415   ; OUTI
site 00417   ; OUTI
site 00419   ; OUTI
site 0041B   ; OUTI
site 0041D   ; OUTI
site 0041F   ; OUTI
site 00421   ; OUTI
site 00423   ; OUTI
site 00425   ; OUTI
site 00427   ; OUTI
site 00429   ; OUTI
site 0042B   ; OUTI
site 0042D   ; OUTI
site 0042F   ; OUTI
site 00431   ; OUTI
site 00433   ; OUTI
site 00435   ; OUTI
site 00437   ; OUTI
site 00439   ; OUTI
site 0043B   ; OUTI
site 0043D   ; OUTI
site 0043F   ; OUTI
site 00441   ; OUTI
site 00443   ; OUTI
site 00445   ; OUTI
site 00447   ; OUTI
site 00449   ; OUTI
site 0044B   ; OUTI
site 0044D   ; OUTI
site 0044F   ; OUTI
site 00451   ; OUTI
site 00453   ; OUTI
site 00455   ; OUTI
site 00457   ; OUTI
site 00459   ; OUTI
site 0045B   ; OUTI
site 0045D   ; OUTI
site 0045F   ; OUTI
site 00461   ; OUTI
site 00463   ; OUTI
site 00465   ; OUTI
site 00467   ; OUTI
site 00469   ; OUTI
site 0046B   ; OUTI
site 0046D   ; OUTI
site 0046F   ; OUTI
site 00471   ; OUTI
site 00473   ; OUTI
site 00475   ; OUTI
site 00477   ; OUTI
site 00479   ; OUTI
site 0047B   ; OUTI
site 0047D   ; OUTI
site 0047F   ; OUTI
site 00481   ; OUTI
site 00483   ; OUTI
site 00485   ; OUTI
site 00487   ; OUTI
site 00489   ; OUTI
site 0048B   ; OUTI
site 0048D   ; OUTI
site 0048F   ; OUTI
site 00491   ; OUTI
site 00493   ; OUTI
site 00495   ; OUTI
site 00497   ; OUTI
site 00499   ; OUTI
site 0049B   ; OUTI
site 0049D   ; OUTI
site 0049F   ; OUTI
site 004A1   ; OUTI
site 004A3   ; OUTI
site 004A5   ; OUTI
site 004A7   ; OUTI
site 004A9   ; OUTI
site 004AB   ; OUTI
site 004AD   ; OUTI
site 004AF   ; OUTI
site 004B1   ; OUTI
site 004B3   ; OUTI
site 004B5   ; OUTI
site 004B7   ; OUTI
site 004B9   ; OUTI
site 004BB   ; OUTI
site 004BD   ; OUTI
site 004BF   ; OUTI
site 004C1   ; OUTI
site 004C3   ; OUTI
site 004C5   ; OUTI
site 004C7   ; OUTI
site 004C9   ; OUTI
site 004CB   ; OUTI
site 004CD   ; OUTI
site 004CF   ; OUTI
site 004D1   ; OUTI
site 004D3   ; OUTI
site 004D5   ; OUTI
site 004D7   ; OUTI
site 004D9   ; OUTI
site 004DB   ; OUTI
site 004DD   ; OUTI
site 004DF   ; OUTI
site 004E1   ; OUTI
site 004E3   ; OUTI
site 004E5   ; OUTI
site 004E7   ; OUTI
site 004E9   ; OUTI
site 004EB   ; OUTI
site 004ED   ; OUTI
site 004EF   ; OUTI
site 004F1   ; OUTI
site 004F3   ; OUTI
site 004F5   ; OUTI
site 004F7   ; OUTI
site 004F9   ; OUTI
site 004FB   ; OUTI
site 00544   ; OUT ($BF),A
site 0054B   ; OUT ($BF),A
site 0054E   ; OUT ($BE),A
site 00561   ; OUT ($BF),A
site 00568   ; OUT ($BF),A
site 0056D   ; OUT ($BE),A
site 00579   ; OUT ($BF),A
site 00580   ; OUT ($BF),A
site 00585   ; OUT ($BE),A
site 0058B   ; OUT ($BF),A
site 00592   ; OUT ($BF),A
site 00597   ; OUT ($BE),A
site 005A9   ; OUT ($BF),A
site 005B0   ; OUT ($BF),A
site 005B5   ; OUT ($BE),A
site 005D5   ; OUTI
site 005E7   ; OUT ($BE),A
site 005F1   ; OUT ($BE),A
site 005F6   ; OUT ($BE),A
site 00609   ; OUT ($BE),A
site 0060E   ; OUT ($BE),A
site 0061B   ; OUT ($BF),A
site 00622   ; OUT ($BF),A
site 00627   ; OUT ($BE),A
site 0063C   ; OUT ($BE),A
site 00644   ; OUT ($BE),A
site 00650   ; OUT ($3F),A
site 00652   ; IN A,($DD)
site 0065C   ; OUT ($3F),A
site 0065E   ; IN A,($DD)
site 00667   ; OUT ($3F),A
site 00B47   ; OUT ($3E),A
site 00B4F   ; OUT ($F2),A
site 00B52   ; IN A,($F2)
site 00B64   ; OUT ($F2),A
site 00B6C   ; OUT ($3E),A
site 01F3D   ; OUT ($BE),A
site 01F42   ; OUT ($BE),A
site 03EB4   ; OUT ($BE),A
site 03EB8   ; OUT ($BE),A
site 03F47   ; OUT ($BF),A
site 03F4A   ; OUT ($BF),A
site 0C134   ; OUT ($F0),A
site 0C13D   ; OUT ($F1),A
site 0C152   ; OUT ($7F),A
site 0C156   ; OUT ($F0),A
site 0C15C   ; OUT ($F1),A
site 0C173   ; OUT ($7F),A
site 0C183   ; OUT (C),D
site 0C189   ; OUT ($F1),A
site 0C19C   ; OUT ($F0),A
site 0C1A2   ; OUT ($F1),A
site 0C1AD   ; OUTI
site 0C1B4   ; OUTI
site 0C1C3   ; OUT ($7F),A
site 0C1C7   ; OUT ($F0),A
site 0C1CD   ; OUT ($F1),A
site 0C343   ; OUT ($7F),A
site 0C347   ; OUT ($7F),A
site 0C3DD   ; OUT ($7F),A
site 0C405   ; OUT ($7F),A
site 0C45E   ; OUT ($F0),A
site 0C465   ; OUT ($F1),A
site 0C46D   ; OUT ($F0),A
site 0C473   ; OUT ($F1),A
site 0C568   ; OUT ($F0),A
site 0C56F   ; OUT (C),L
site 0C578   ; OUT ($F0),A
site 0C593   ; OUT (C),H
site 0C59B   ; OUT ($F0),A
site 0C5A9   ; OUT ($F1),A
site 0C5B1   ; OUT ($F0),A
site 0C5BB   ; OUT ($F1),A
site 0C777   ; OUT ($F0),A
site 0C77D   ; OUTI
site 0C7E8   ; OUT ($7F),A
site 0C8D7   ; OUT ($7F),A
site 0C8DB   ; OUT ($7F),A
site 0C8F8   ; OUT ($7F),A
site 0C91A   ; OUT ($7F),A
site 0C929   ; OUT ($F0),A
site 0C934   ; OUT ($F1),A
site 0C945   ; OUT ($F0),A
site 0C959   ; OUT ($F0),A
site 0C96D   ; OUT ($F1),A
site 0C9D2   ; OTIR
site 0C9DF   ; OUT (C),D
site 0C9E5   ; OUT ($F1),A
site 0CA20   ; OUT ($7F),A
site 0CA71   ; OUT ($7F),A
site 0CAFB   ; OUT ($7F),A
site 0CB1B   ; OUT ($7F),A
site 0CB5B   ; OUT ($7F),A
site 0CB65   ; OUT ($7F),A
site 0CBAD   ; OUT ($7F),A
site 0E9E7   ; OUT ($7F),A
site 0E9EA   ; OUT ($F2),A
site 0EA04   ; OUT ($7F),A
site 0EA14   ; OUT ($F2),A
mapldk 00069   # LD HL,$FFFC; LD (HL),$80
maphl 0006F   # LD (HL),$00, HL = $FFFD
maphl 00072   # LD (HL),$01, HL = $FFFE
mapldk 0067B   # LD HL,$FFFC; LD (HL),$80
maphl 00681   # LD (HL),$00, HL = $FFFD
maphl 00684   # LD (HL),$01, HL = $FFFE
mapst 009E0   ; LD ($FFFF),A
asm 00551 5          ; tile unpacker: EX DE,HL; LD C,$04; PUSH HL; LD A,(DE)
    rst $00
    db far_io, pg_unpack, ent_unpack
    ret
endasm
page 0 unpack
; Entry unpack: the game's tile unpacker $0551, whole.
;   Reads:   HL = the packed data (read as the game sees it, through jt_peek in
;            $2000-$3FFF), DE = the VRAM address of plane 0.
;   Returns: as the game routine does. HL after the fourth plane's 00 00; DE = DE + 4;
;            A = 0, C = 0, flags of DEC C from 1 with carry clear; B = 0 when a
;            00 n v run came, else B kept. IX, IY and the alternate registers kept;
;            interrupts as they were (jt_vwrite turns them off while it writes).
; Runtime internals used: jt_peek, jt_vwrite.
unpack:
        ld (u_ix),ix
        ld (u_iy),iy
        ld a,b
        ld (u_b),a
        ld (u_v),de             ; plane 0 VRAM address
        ld a,4
        ld (u_n),a
.plane: ld de,(u_v)
        ld (u_c),de             ; VRAM address of buf's first byte
        ld de,buf
.next:  call get
        or a
        jr z,.zero
        inc a
        jr z,.two
        dec a
        call put
        jr .next
.two:   call get                ; FF v: v twice
        call put
        call put
        jr .next
.zero:  call get                ; 00 n v: n bytes v; 00 00 ends the plane
        or a
        jr z,.pend
        ld b,a
        call get
.rep:   call put
        djnz .rep
        xor a
        ld (u_b),a              ; B = 0, as the game's DJNZ leaves it
        jr .next
.pend:  ld a,e
        or a
        call nz,flush           ; the bytes left in buf (E of them)
        ld de,(u_v)
        inc de                  ; the next plane starts one VRAM byte later
        ld (u_v),de
        ld a,(u_n)
        dec a
        ld (u_n),a
        jr nz,.plane
        ld ix,(u_ix)
        ld iy,(u_iy)
        ld a,(u_b)
        ld b,a
        ld c,1
        or a                    ; carry clear, as the game's OR A before its exit
        dec c                   ; C = 0 with the flags of DEC C
        ld a,0
        ret
; A = (HL) as the game sees it, HL + 1; F changes
get:    ld a,h
        and $E0
        cp $20
        jr z,.pk
        ld a,(hl)
        inc hl
        ret
.pk:    call jt_peek
        inc hl
        ret
; A into buf at DE; a full buf (256 bytes) goes to VRAM. Keeps A, B and HL.
put:    ld (de),a
        inc e
        ret nz
        ld (u_a),a
        ld a,0                  ; 256 runs
        call flush
        ld a,(u_a)
        ret
; A bytes of buf (0: 256) to VRAM at u_c, u_c + 4, ...; u_c moves past them,
; DE = buf. Keeps B and HL.
flush:  ld (u_hl),hl
        ld (u_bc),bc
        ld c,a
        ld b,1
        ld hl,buf
        ld de,(u_c)
        ld ix,1
        ld iy,4
        ld a,1                  ; the source as mapped: buf in this page
        call jt_vwrite
        ld h,0
        ld l,c
        ld a,c
        or a
        jr nz,.n
        inc h                   ; 256
.n:     add hl,hl
        add hl,hl
        add hl,de
        ld (u_c),hl
        ld hl,(u_hl)
        ld bc,(u_bc)
        ld de,buf
        ret
u_ix:   dw 0
u_iy:   dw 0
u_hl:   dw 0
u_bc:   dw 0
u_v:    dw 0
u_c:    dw 0
u_n:    db 0
u_b:    db 0
u_a:    db 0
        align 256
buf:    ds 256
endpage

# Alex Kidd - The Lost Stars (World).cht, "Infinite Energy": RAM $CD1D counts the energy lost
# (it rises with time and with hits, and the game restarts when it reaches $14); held at 2,
# the bar stays nearly full
poke "Infinite energy"
ar 00CD-1D02
endpoke

# Alex Kidd - The Lost Stars (World).cht, "Invincible After 1 Hit [Time Still Decreases]":
# RAM $CD0A holds a countdown after a hit; held at 1, hits after the first take no energy,
# and the time drain on the bar goes on
poke "No damage after 1st hit"
ar 00CD-0A01
endpoke

# Alex Kidd - The Lost Stars (World).cht, "Unlimited Cloud Shots": RAM $CD01 is the shot
# count, which the shot routine lowers by one; held at $14, Alex always has shots
poke "Infinite cloud shots"
ar 00CD-0114
endpoke

# Alex Kidd - The Lost Stars (World).cht, "High Jump [Makes Buzzing Noise]": RAM $CD06 set
# to 1 shows a J on the status bar and Alex's jump rises a third higher
poke "High jump"
ar 00CD-0601
endpoke

# Alex Kidd - The Lost Stars (World).cht, "Level Select [Replace ? With 0-C]": RAM $C04D is
# the stage; 1 to 7 each start a different stage, 9 to C repeat 1 to 4, and 0 and 8 show a
# scrambled screen
poke "Start stage ??"
ar 00C0-4D??
endpoke
