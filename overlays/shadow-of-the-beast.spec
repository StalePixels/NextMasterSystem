# Shadow of the Beast (Europe, Brazil) (En), CRC32 1575581D, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
#
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - No free RST vector: $0000-$0002 (DI; IM 1) becomes the io vector, and the game starts at
#   $0003 (JP $08B8). The game has no RST $00 of its own.
# - $0006-$0027 is a table of 17 level set-up routines ($0DBF, $0DE7, $0E36, $1198, $11BD,
#   $0F60, $0FC3, $1038, $10B5, $1124, $1BA8, $1BDB, $1BF1, $1BFE, $1C09, $1C20), read by the
#   JP (HL) at $0D97 with the level number $DA4F. $0008-$0037 is data, not code. The I/O sites
#   at $0E21, $0E28, $0E30, $1270 and $1278 and the mapper stores at $0DFF-$11E1 and
#   $1BBB-$1C40 are in those routines.
# - Play: the line interrupt comes every 5 lines, and the line handler ($1E57) writes register
#   8 for each parallax band from the list at ($DA47): the clouds at lines 5, 15, 30 and 55,
#   the mountains at 65, the grass at 160, 165, 175 and 185. hsplit gives each band its map
#   columns.
# - The play frame handler ($1D4B) uploads the hero's tiles in $2FEA, up to 16 tiles a frame,
#   one tile a pass through the OUTI run $152F or through the bit-reverse table at $0100 for
#   the mirrored hero. Through the runtime that took about 11,000 cycles a tile, and the
#   handler ran from line 194 to line 30-60 of the next picture: the line events of the top
#   bands were lost, and the once-a-frame work ran inside the picture, so many frames showed
#   the mountains with wrong tiles and wrong columns. Page 0 tcopy and tflip write the tiles
#   with jt_vwrite, and ncol writes the mountain's name table column ($1415, from $13B4) the
#   same way. The handler now ends before line 248.
name Shadow of the Beast
cart 1575581D
hz 50		; No-Intro region Europe
hsplit
vector 00 io
start 0003
site 00A5D   ; OUT ($BF),A
site 00A64   ; OUT ($BF),A
site 00A7F   ; OUT ($7F),A
site 00A83   ; OUT ($7F),A
site 00A87   ; OUT ($7F),A
site 00A8B   ; OUT ($7F),A
site 00AA2   ; IN A,($DC)
site 00AF8   ; IN A,($DC)
site 00BA4   ; OUT ($BE),A
site 00BC5   ; OUT ($BE),A
site 00C05   ; OUT ($BE),A
site 00C0C   ; OUT ($BE),A
site 00C1F   ; OUT ($BE),A
site 00C26   ; OUT ($BE),A
site 00C48   ; OUT ($BE),A
site 00C4F   ; OUT ($BE),A
site 00C91   ; OUT ($BE),A
site 00C97   ; OUT ($BE),A
site 00E21   ; OUT ($BF),A (level set-up code, from the table at $0006)
site 00E28   ; OUT ($BF),A (level set-up code, from the table at $0006)
site 00E30   ; OUT ($BE),A (level set-up code, from the table at $0006)
site 00E98   ; OUT ($BE),A
site 00E9F   ; OUT ($BE),A
site 00EB3   ; OUT ($BE),A
site 00EBA   ; OUT ($BE),A
site 00EC5   ; OUT ($BE),A
site 00ECC   ; OUT ($BE),A
site 00EE8   ; OUT ($BF),A
site 00EEF   ; OUT ($BF),A
site 00F29   ; OUT ($BE),A
site 00F2F   ; OUT ($BE),A
site 01270   ; OUT ($BE),A (level set-up code, from the table at $0006)
site 01278   ; OUT ($BE),A (level set-up code, from the table at $0006)
site 012AE   ; OUT ($BF),A
site 012B5   ; OUT ($BF),A
site 012BA   ; OUT ($BF),A
site 012C1   ; OUT ($BF),A
site 01312   ; OUT ($7F),A
asm 01415 22  ; the name table column loop of $13B4 (12 cells from $C300), through page 0 (ncol)
    rst $00
    db far_io, pg_ncol, ent_ncol
    ret
endasm
site 014DE   ; OUT ($BF),A
site 014E2   ; OUT ($BF),A
site 014F1   ; OUTI
site 014F3   ; OUTI
site 014F5   ; OUTI
site 014F7   ; OUTI
site 01508   ; OUTI
site 01520   ; OUTI
site 01522   ; OUTI
site 0152F   ; OUTI
site 01531   ; OUTI
site 01533   ; OUTI
site 01535   ; OUTI
site 01537   ; OUTI
site 01539   ; OUTI
site 0153B   ; OUTI
site 0153D   ; OUTI
site 0153F   ; OUTI
site 01541   ; OUTI
site 01543   ; OUTI
site 01545   ; OUTI
site 01547   ; OUTI
site 01549   ; OUTI
site 0154B   ; OUTI
site 0154D   ; OUTI
site 0154F   ; OUTI
site 01551   ; OUTI
site 01553   ; OUTI
site 01555   ; OUTI
site 01557   ; OUTI
site 01559   ; OUTI
site 0155B   ; OUTI
site 0155D   ; OUTI
site 0155F   ; OUTI
site 01561   ; OUTI
site 01563   ; OUTI
site 01565   ; OUTI
site 01567   ; OUTI
site 01569   ; OUTI
site 0156B   ; OUTI
site 0156D   ; OUTI
site 01591   ; OUT ($BF),A
site 0159C   ; OUT ($BF),A
site 0172F   ; OUT ($BE),A
site 01736   ; OUT ($BE),A
site 0177B   ; IN A,($BE)
site 01782   ; IN A,($BE)
site 01788   ; OUT ($BE),A
site 01790   ; OUT ($BE),A
site 017C0   ; OUT ($BF),A
site 017C6   ; OUT ($BF),A
site 017CC   ; IN A,($BE)
site 01817   ; OUT ($BE),A
site 0181C   ; OUT ($BE),A
site 01853   ; OUT ($BF),A
site 0185A   ; OUT ($BF),A
site 01860   ; OUT ($BF),A
site 01867   ; OUT ($BF),A
site 01CCB   ; OUT ($BF),A
site 01CD2   ; OUT ($BF),A
site 01CDF   ; OUT ($BE),A
site 01CE7   ; OUT ($BF),A
site 01CEE   ; OUT ($BF),A
site 01CFB   ; OUT ($BE),A
site 01D0E   ; IN A,($DC)
site 01D4C   ; IN A,($BF)
site 01D76   ; OUT ($BF),A
site 01D7A   ; OUT ($BF),A
site 01DB5   ; OUT ($BF),A
site 01DB9   ; OUT ($BF),A
site 01DC9   ; OUT ($BF),A
site 01DCD   ; OUT ($BF),A
site 01E4A   ; IN A,($DD)
site 01E80   ; OUT ($BF),A
site 01E84   ; OUT ($BF),A
site 01EA3   ; OUT ($BF),A
site 01EAA   ; OUT ($BF),A
site 01EEB   ; OUT ($BE),A
site 0206D   ; OUT ($BF),A
site 02070   ; OUT ($BF),A
site 02074   ; OUT ($BE),A
site 02078   ; OUT ($BE),A
site 02136   ; OUT ($BF),A
site 02139   ; OUT ($BF),A
site 0213C   ; OUT ($BE),A
site 02140   ; OUT ($BE),A
site 02171   ; OUT ($BE),A
site 02178   ; OUT ($BE),A
site 02181   ; OUT ($BE),A
site 02188   ; OUT ($BE),A
site 0221B   ; IN A,($DD)
site 02271   ; IN A,($DC)
asm 03064 18  ; CALL $152F ... JP $3078: the tile upload of $2FEA, through page 0 (tcopy)
    rst $00
    db far_io, pg_tcopy, ent_tcopy
    jp $3078
endasm
asm 0307D 175 ; the unrolled mirrored tile upload of $2FEA, through page 0 (tflip)
    rst $00
    db far_io, pg_tflip, ent_tflip
    jp $3078
endasm
site 0316A   ; OUT ($BF),A
site 03171   ; OUT ($BF),A
site 03177   ; IN A,($BE)
site 0317F   ; IN A,($BE)
site 03397   ; OUT ($BF),A
site 0339C   ; OUT ($BF),A
site 0351A   ; IN A,($DC)
site 0352A   ; OUT ($BF),A
site 03531   ; OUT ($BF),A
site 03544   ; IN A,($BF)
site 03567   ; IN A,($DD)
site 03573   ; IN A,($BF)
site 035A4   ; IN A,($DD)
site 035DA   ; OUT ($BF),A
site 035DE   ; OUT ($BF),A
site 03601   ; OUTI
site 03603   ; OUTI
site 0361C   ; OUTI
site 0361E   ; OUTI
site 03620   ; OUTI
site 03622   ; OUT (C),A
site 03624   ; OUTI
site 03626   ; OUTI
site 03628   ; OUTI
site 0362A   ; OUT (C),A
site 0362C   ; OUTI
site 0362E   ; OUTI
site 03630   ; OUTI
site 03632   ; OUT (C),A
site 03634   ; OUTI
site 03636   ; OUTI
site 03638   ; OUTI
site 0363A   ; OUT (C),A
site 0363C   ; OUTI
site 0363E   ; OUTI
site 03640   ; OUTI
site 03642   ; OUT (C),A
site 03644   ; OUTI
site 03646   ; OUTI
site 03648   ; OUTI
site 0364A   ; OUT (C),A
site 0364C   ; OUTI
site 0364E   ; OUTI
site 03650   ; OUTI
site 03652   ; OUT (C),A
site 03654   ; OUTI
site 03656   ; OUTI
site 03658   ; OUTI
site 0365A   ; OUT (C),A
site 039A2   ; OUT ($BF),A
site 039A6   ; OUT ($BF),A
site 039AB   ; OUT ($BE),A
site 03FA7   ; OUT ($BF),A
site 03FB3   ; OUT ($BF),A
site 03FB7   ; OUT ($BE),A
site 073A5   ; OUT ($BF),A
site 073A8   ; OUT ($BF),A
site 073AF   ; OUT ($BF),A
site 073B3   ; OUT ($BF),A
site 073BF   ; OUT ($BF),A
site 073C3   ; OUT ($BF),A
site 073C9   ; OUT ($BE),A
site 073D2   ; OUT ($BF),A
site 073D6   ; OUT ($BF),A
site 073F5   ; OUT ($BF),A
site 073F9   ; OUT ($BF),A
site 0745F   ; OUT ($BE),A
site 07472   ; OUT ($BF),A
site 07479   ; OUT ($BF),A
site 07493   ; OUT ($BF),A
site 07497   ; OUT ($BF),A
site 0749D   ; OUT ($BE),A
site 074A6   ; OUT ($BF),A
site 074AA   ; OUT ($BF),A
site 074BB   ; OUT ($BF),A
site 074C2   ; OUT ($BF),A
site 07504   ; OUT ($BE),A
site 0750E   ; OUT ($BE),A
site 0752F   ; OUT ($7F),A
site 075A3   ; OUT ($BF),A
site 075A7   ; OUT ($BF),A
site 075C8   ; OUT ($BF),A
site 075CB   ; OUT ($BF),A
site 075D7   ; OUT ($BE),A
site 075E5   ; OUT ($BF),A
site 075E9   ; OUT ($BF),A
site 075ED   ; OUT ($BE),A
site 075F7   ; OUT ($BF),A
site 075FB   ; OUT ($BF),A
site 0760A   ; OUT ($BE),A
site 07611   ; OUT ($BE),A
site 07626   ; OUT ($BE),A
site 0762D   ; OUT ($BE),A
site 07653   ; OUT ($BF),A
site 07657   ; OUT ($BF),A
site 0765A   ; OUT ($BE),A
site 076AD   ; OUT ($BF),A
site 076B3   ; OUT ($BF),A
site 076B9   ; IN A,($BE)
site 076CD   ; OUT ($BE),A
site 07D24   ; OUTI
site 07D37   ; OUTI
site 07D3C   ; OUTI
site 07D61   ; OUT ($BF),A
site 07D68   ; OUT ($BF),A
site 07D6E   ; OUT ($BE),A
site 1D37B   ; OUT ($7F),A
site 1D3EA   ; OUT ($7F),A
site 1D3F3   ; OUT ($7F),A
site 1D415   ; OUT ($7F),A
site 1D41E   ; OUT ($7F),A
site 1D440   ; OUT ($7F),A
site 1D449   ; OUT ($7F),A
site 1D458   ; OUT ($7F),A
site 1D467   ; OUT ($7F),A
site 1D476   ; OUT ($7F),A
site 1D48D   ; OUT ($7F),A
mapst 00A17   ; LD ($FFFF),A
mapst 00A2C   ; LD ($FFFF),A
mapst 00CEF   ; LD ($FFFF),A
mapst 00D59   ; LD ($FFFF),A
mapst 00D9A   ; LD ($FFFF),A
mapst 00E6B   ; LD ($FFFF),A
mapst 012CD   ; LD ($FFFF),A
mapst 01308   ; LD ($FFFF),A
mapst 01316   ; LD ($FFFF),A
mapst 01322   ; LD ($FFFF),A
mapst 0132B   ; LD ($FFFF),A
mapst 01337   ; LD ($FFFF),A
mapst 01355   ; LD ($FFFF),A
mapst 014AC   ; LD ($FFFF),A
mapst 0173D   ; LD ($FFFF),A
mapst 017E2   ; LD ($FFFF),A
mapst 017F7   ; LD ($FFFF),A
mapst 0183A   ; LD ($FFFF),A
mapst 01880   ; LD ($FFFF),A
mapst 01891   ; LD ($FFFF),A
mapst 018BD   ; LD ($FFFF),A
mapst 019B6   ; LD ($FFFF),A
mapst 01B75   ; LD ($FFFF),A
mapst 01DD4   ; LD ($FFFF),A
mapst 01E31   ; LD ($FFFF),A
mapst 01FCB   ; LD ($FFFF),A
mapst 0208A   ; LD ($FFFF),A
mapst 02406   ; LD ($FFFF),A
mapst 02F9D   ; LD ($FFFF),A
mapst 0300C   ; LD ($FFFF),A
mapst 0301F   ; LD ($FFFF),A
mapst 0338F   ; LD ($FFFF),A
mapst 033DC   ; LD ($FFFF),A
mapst 0348B   ; LD ($FFFF),A
mapst 035F7   ; LD ($FFFF),A
mapst 036B6   ; LD ($FFFF),A
mapst 036DF   ; LD ($FFFF),A
mapst 039FC   ; LD ($FFFF),A
mapst 075BB   ; LD ($FFFF),A
# Mapper stores of the level set-up routines (the table at $0006), which the scan reaches only
# through the byte scan:
mapst 00DFF   # LD ($FFFF),A; after LD A,$08; 32 bytes of valid code before it
mapst 00F6A   # LD ($FFFF),A; after LD ($D9E8),A; 32 bytes of valid code before it
mapst 00FCD   # LD ($FFFF),A; after LD ($D9E8),A; 32 bytes of valid code before it
mapst 01022   # LD ($FFFF),A; after LD A,$08; 31 bytes of valid code before it
mapst 01045   # LD ($FFFF),A; after LD ($D9E8),A; 32 bytes of valid code before it
mapst 010BF   # LD ($FFFF),A; after LD ($D9E8),A; 32 bytes of valid code before it
mapst 0112D   # LD ($FFFF),A; after LD ($D9E8),A; 32 bytes of valid code before it
mapst 01182   # LD ($FFFF),A; after LD A,$08; 31 bytes of valid code before it
mapst 011E1   # LD ($FFFF),A; after LD ($D9E8),A; 32 bytes of valid code before it
mapst 01BBB   # LD ($FFFF),A; after LD A,$03; 32 bytes of valid code before it
mapst 01BE7   # LD ($FFFF),A; after LD A,$0F; 32 bytes of valid code before it
mapst 01C40   # LD ($FFFF),A; after LD ($D9E8),A; 32 bytes of valid code before it

page 0 tcopy tflip ncol
; tcopy and tflip: in place of the two tile upload loops of $2FEA (the hero's tiles, in the
; play frame handler). At the loop: HL = the source, D = the first tile ($D9E1), E = the most
; tiles this frame, and $0A5C has set the VRAM address $1000 + (D AND $7F) * 32. The game's
; loop sends one tile (32 bytes) a pass, then D = D + 1; when D reaches ($D9E2) it ends with
; D = $FF, else after E passes with D as it is. Each pass costs about 11,000 cycles through
; the runtime (the OUTI run $152F, or 32 single writes through the bit-reverse table at
; $0100 in tflip's case, which tflip copies into rtab once with jt_peek: slot 0 does not hold
; the cart while page code runs), and with 16 tiles the frame handler ran into the next picture.
; tcopy writes the tiles with one jt_vwrite call; tflip looks the bytes up into fbuf first.
; Both return to JP $3078 with D, A, B, C and HL as the game's loop leaves them, and keep
; the interrupt state, E, IX and IY.
tcopy:  call t_enter
        ld hl,(t_src)
        ld de,(t_vram)
        ld a,(t_n)
        ld c,a                  ; C runs of 32 bytes
        ld b,32
        ld ix,32
        ld iy,32
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,(t_n)              ; B = 1 - 32 * n, as after the OUTIs
        rrca
        rrca
        rrca
        and $E0
        neg
        inc a
        ld (t_b),a
        ld a,$BE
        ld (t_c),a
        jp t_exit
tflip:  call t_enter
        ld a,(r_ok)             ; the first time: the game's table into rtab
        or a
        jr nz,1f
        ld hl,$0100
        ld de,rtab
0:      call jt_peek
        ld (de),a
        inc de
        inc l
        jr nz,0b
        ld a,1
        ld (r_ok),a
1:      ld hl,(t_src)
        ld de,fbuf
        ld a,(t_n)
        ld b,a
2:      push bc
        ld b,32
3:      call jt_peek            ; the source byte as the game sees it
        inc hl
        ld (t_c),a              ; C = the last source byte, as after LD C,(HL)
        push hl
        ld l,a
        ld h,high rtab
        ld a,(hl)               ; the byte with its bits in reverse order
        pop hl
        ld (de),a
        inc de
        djnz 3b
        pop bc
        djnz 2b
        ld hl,fbuf
        ld de,(t_vram)
        ld a,(t_n)
        ld c,a
        ld b,32
        ld ix,32
        ld iy,32
        ld a,1                  ; fbuf is in this page
        call jt_vwrite
        ld a,1
        ld (t_b),a
        jp t_exit
; t_enter: keeps the state, works out t_n (the tiles), t_d (D after the loop), t_vram and the
; source; runs on the page's stack with interrupts off.
t_enter:
        ex (sp),hl              ; HL = the return into tcopy or tflip
        ld (t_ret),hl
        pop hl                  ; the game's HL
        ld (t_hl),hl
        ld (t_src),hl
        ld a,i                  ; P/V = the interrupt state
        di
        ld (t_sp),sp
        ld sp,t_stk
        push af
        push ix
        push iy
        push de
        ld a,d                  ; t_vram = $1000 + (D AND $7F) * 32
        and $7F
        ld l,a
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld bc,$1000
        add hl,bc
        ld (t_vram),hl
        ld a,($D9E2)            ; m = ($D9E2) - D: the pass where D reaches ($D9E2)
        ld (t_a),a
        sub d
        jr z,5f                 ; m = 0: only after 256 passes, so E passes
        cp e
        jr z,6f
        jr nc,5f                ; m > E: E passes
6:      ld (t_n),a              ; m <= E: m passes, D = $FF
        ld a,$FF
        ld (t_d),a
        jr 7f
5:      ld a,e                  ; E passes, D = D + E
        ld (t_n),a
        add a,d
        ld (t_d),a
7:      ld hl,(t_hl)            ; HL after the loop = HL + 32 * n
        ld a,(t_n)
        ld c,a
        ld b,0
        ld a,5
8:      sla c
        rl b
        dec a
        jr nz,8b
        add hl,bc
        ld (t_hl),hl
        ld hl,(t_ret)
        jp (hl)
t_exit: pop de
        ld a,(t_d)
        ld d,a
        pop iy
        pop ix
        pop af
        ld sp,(t_sp)
        ld hl,(t_hl)
        ld a,(t_b)
        ld b,a
        ld a,(t_c)
        ld c,a
        ld a,(t_a)
        jp po,9f
        ei
9:      ret
; ncol: in place of $1415-$142A, the mountain's name table column: HL = the VRAM address of its
; first cell (with the write bit), DE = $C300, B = 12 cells, C = $40. The game's loop sets the
; address and writes the 2 bytes of each cell, then HL = HL + $40, 4 runtime calls a cell.
; ncol writes the 12 cells with one jt_vwrite call and returns with B = 0, HL and DE past the
; column, as the loop leaves them. Keeps the interrupt state.
ncol:   ld a,i
        di
        ld (t_sp),sp
        ld sp,t_stk
        push af
        push ix
        push iy
        push hl
        push bc
        ex de,hl                ; HL = the source, DE = the VRAM address
        ld c,b                  ; C cells
        ld b,2
        ld ix,2
        ld iy,$40
        xor a
        call jt_vwrite
        pop bc                  ; C = $40
        pop hl
        ld de,$40*12
        add hl,de
        ld de,$C300+2*12
        ld b,0
        pop iy
        pop ix
        pop af
        ld sp,(t_sp)
        jp po,1f
        ei
1:      ret
t_sp:   dw 0
t_ret:  dw 0
t_hl:   dw 0
t_src:  dw 0
t_vram: dw 0
t_n:    db 0
t_d:    db 0
t_a:    db 0
t_b:    db 0
t_c:    db 0
r_ok:   db 0
        ds 48
t_stk:
        ALIGN 256
rtab:   ds 256
fbuf:   ds 16*32                ; E is at most 16 ($3043)
endpage

# Shadow of the Beast (Europe) (Action Replay).cht, "Infinite Lives": RAM $DA50 is the
# number of lives (3 at the start); held at 9, a lost life no longer ends the game
poke "Infinite lives"
ar 00DA-5009
endpoke

# Shadow of the Beast (Europe) (Action Replay).cht, "Infinite Health": RAM $DA51 is the
# health (9 when full); held at 9, hits do not lower it
poke "Infinite health"
ar 00DA-5109
endpoke

# Shadow of the Beast (Europe, Brazil).cht, "Invulnerability": RAM $D9EC is the timer set
# by a hit; held at $56, no enemy hit lands
poke "Invincibility"
ar 00D9-EC56
endpoke

# Shadow of the Beast (Europe) (Action Replay).cht, "Always Have The Gun": RAM $DA54 set
# to 1 gives the gun; Button 1 fires bullets
poke "Always have gun"
ar 00DA-5401
endpoke

# Shadow of the Beast (Europe) (Action Replay).cht, "Always Have A Strange Weapon": RAM
# $DA52 set to 1 gives a thrown weapon; Button 1 throws it
poke "Strange weapon"
ar 00DA-5201
endpoke
