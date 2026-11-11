# Alien Storm (Europe, Brazil) (En), CRC32 7F30F793, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the sound driver entry (7:8000) and a
# reference I/O log (600 s of random input), then decided by hand.
#
# Decisions:
# - $0030-$0037 is zero bytes that no path reaches and no RST names, so $30 is the io
#   vector. The game uses RST $08, $10, $18, $20, $28 and $38. IM 1 is at $0001 and in the
#   soft reset at $0029 (RST $28); both become IM 2.
# - The bank 2 code the scan lists ($A012, $A43B and the stores and HALTs there) is graphics,
#   reached through a 22nd entry of the jump table at $0656 that is the VDP register data at
#   $0680. It gets no lines.
# - Bank 0 routines that no path or recording reaches, each whole after a RET, are patched as
#   code: the OUTI run $02DB-$031A (its second half, from $031B, is the palette and tile run),
#   the OUTD run $038E-$040D, the OTIR at $057F, the pad reads $0772 and $079E and the scroll
#   register writes $0AD8.
# - hsplit: the title's Earth band is a line interrupt split with its own H scroll ($3BD2);
#   without the switch the band showed the wrong map columns.
# - $01DD writes the sprite table in two halves through 16 runtime calls; the runtime's
#   once-a-frame work came between them and drew the Y bytes of one sprite order with the X
#   and tile bytes of the other, and the player and the enemies vanished. Page 0 (sat) writes
#   the table with one jt_vwrite call and the palette only where it changed.
# - $0454 and $0582 upload tiles 32 runtime calls a tile; through the runtime the frame
#   handler ran into the next picture with the display off, and the top lines of the picture
#   were black. Page 0 (tcopy, tflip) writes each upload with jt_vwrite.
# - $055F, the player tile upload that bank 1 ($46A4, $4C06) calls when the player is not
#   mirrored, sends 32 bytes a tile through the OUTI at $0577, one runtime call a byte. In the
#   running stage it took about 160,000 cycles in each frame that loads the player's tiles,
#   and those frames ran over 100%. It goes through tcopy too.
# - The video rate test at $016C read 50 Hz on the Next, and the game ran its 50 Hz speed-up
#   at 60 Hz. Page 0 (vrate) gives the Next's rate.
name Alien Storm
cart 7F30F793
hz any		; No-Intro regions Europe, Brazil
hsplit
vector 30 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00029 2   ; IM 1 -> IM 2
    im 2
endasm
site 0008F   ; IN A,($BF)
site 00093   ; OUT ($BF),A
site 00097   ; OUT ($BF),A
site 000EA   ; OUT ($3E),A
site 000ED   ; OUT ($F2),A
site 000F5   ; OUT ($3E),A
site 000F9   ; OUT ($3F),A
site 000FC   ; IN A,($BF)
site 0012A   ; OUT ($BF),A
site 0012E   ; OUT ($BF),A
site 00148   ; OUT ($BF),A
site 0014C   ; OUT ($BF),A
site 00152   ; IN A,($DD)
site 0015D   ; OUT ($BF),A
site 00161   ; OUT ($BF),A
site 00170   ; IN A,($BF)
site 00172   ; IN A,($BF)
site 0017E   ; IN A,($BF)
site 00199   ; IN A,($BF)
site 001A4   ; OUT ($BF),A
site 001A7   ; OUT ($BF),A
site 001B7   ; OUT ($BE),A
site 001D4   ; OUT ($BF),A
site 001DA   ; OUT ($BF),A
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
site 0031B   ; OUTI
site 0031D   ; OUTI
site 0031F   ; OUTI
site 00321   ; OUTI
site 00323   ; OUTI
site 00325   ; OUTI
site 00327   ; OUTI
site 00329   ; OUTI
site 0032B   ; OUTI
site 0032D   ; OUTI
site 0032F   ; OUTI
site 00331   ; OUTI
site 00333   ; OUTI
site 00335   ; OUTI
site 00337   ; OUTI
site 00339   ; OUTI
site 0033B   ; OUTI
site 0033D   ; OUTI
site 0033F   ; OUTI
site 00341   ; OUTI
site 00343   ; OUTI
site 00345   ; OUTI
site 00347   ; OUTI
site 00349   ; OUTI
site 0034B   ; OUTI
site 0034D   ; OUTI
site 0034F   ; OUTI
site 00351   ; OUTI
site 00353   ; OUTI
site 00355   ; OUTI
site 00357   ; OUTI
site 00359   ; OUTI
site 0035C   ; OUTI
site 0035E   ; OUTI
site 00360   ; OUTI
site 00362   ; OUTI
site 00364   ; OUTI
site 00366   ; OUTI
site 00368   ; OUTI
site 0036A   ; OUTI
site 0036C   ; OUTI
site 0036E   ; OUTI
site 00370   ; OUTI
site 00372   ; OUTI
site 00374   ; OUTI
site 00376   ; OUTI
site 00378   ; OUTI
site 0037A   ; OUTI
site 0037D   ; OUTI
site 0037F   ; OUTI
site 00381   ; OUTI
site 00383   ; OUTI
site 00385   ; OUTI
site 00387   ; OUTI
site 00389   ; OUTI
site 0038B   ; OUTI
site 0038E   ; OUTD
site 00390   ; OUTD
site 00392   ; OUTD
site 00394   ; OUTD
site 00396   ; OUTD
site 00398   ; OUTD
site 0039A   ; OUTD
site 0039C   ; OUTD
site 0039E   ; OUTD
site 003A0   ; OUTD
site 003A2   ; OUTD
site 003A4   ; OUTD
site 003A6   ; OUTD
site 003A8   ; OUTD
site 003AA   ; OUTD
site 003AC   ; OUTD
site 003AE   ; OUTD
site 003B0   ; OUTD
site 003B2   ; OUTD
site 003B4   ; OUTD
site 003B6   ; OUTD
site 003B8   ; OUTD
site 003BA   ; OUTD
site 003BC   ; OUTD
site 003BE   ; OUTD
site 003C0   ; OUTD
site 003C2   ; OUTD
site 003C4   ; OUTD
site 003C6   ; OUTD
site 003C8   ; OUTD
site 003CA   ; OUTD
site 003CC   ; OUTD
site 003CE   ; OUTD
site 003D0   ; OUTD
site 003D2   ; OUTD
site 003D4   ; OUTD
site 003D6   ; OUTD
site 003D8   ; OUTD
site 003DA   ; OUTD
site 003DC   ; OUTD
site 003DE   ; OUTD
site 003E0   ; OUTD
site 003E2   ; OUTD
site 003E4   ; OUTD
site 003E6   ; OUTD
site 003E8   ; OUTD
site 003EA   ; OUTD
site 003EC   ; OUTD
site 003EE   ; OUTD
site 003F0   ; OUTD
site 003F2   ; OUTD
site 003F4   ; OUTD
site 003F6   ; OUTD
site 003F8   ; OUTD
site 003FA   ; OUTD
site 003FC   ; OUTD
site 003FE   ; OUTD
site 00400   ; OUTD
site 00402   ; OUTD
site 00404   ; OUTD
site 00406   ; OUTD
site 00408   ; OUTD
site 0040A   ; OUTD
site 0040C   ; OUTD
site 00414   ; OUT ($BF),A
site 00418   ; OUT ($BF),A
site 0041E   ; OUT ($BE),A
site 00422   ; OUT ($BE),A
site 0043D   ; OUT ($BE),A
site 00444   ; OUT ($BE),A
site 0054A   ; OUT ($BE),A
site 0054F   ; OUT ($BE),A
site 00577   ; OUTI
site 0057F   ; OTIR
site 00590   ; OUTI
site 00596   ; OUTI
site 0059C   ; OUTI
site 005A2   ; OUTI
site 005A8   ; OUTI
site 005AE   ; OUTI
site 005B4   ; OUTI
site 005BA   ; OUTI
site 005C0   ; OUTI
site 005C6   ; OUTI
site 005CC   ; OUTI
site 005D2   ; OUTI
site 005D8   ; OUTI
site 005DE   ; OUTI
site 005E4   ; OUTI
site 005EA   ; OUTI
site 005F0   ; OUTI
site 005F6   ; OUTI
site 005FC   ; OUTI
site 00602   ; OUTI
site 00608   ; OUTI
site 0060E   ; OUTI
site 00614   ; OUTI
site 0061A   ; OUTI
site 00620   ; OUTI
site 00626   ; OUTI
site 0062C   ; OUTI
site 00632   ; OUTI
site 00638   ; OUTI
site 0063E   ; OUTI
site 00644   ; OUTI
site 0064A   ; OUTI
site 006EF   ; OUT ($BF),A
site 006F3   ; OUT ($BF),A
site 00720   ; IN A,($DC)
site 0073D   ; IN A,($DD)
site 0077E   ; IN A,($DC)
site 007A0   ; IN A,($DC)
site 007A4   ; IN A,($DD)
site 00AD8   ; OUT ($BF),A
site 00ADC   ; OUT ($BF),A
site 00AE1   ; OUT ($BF),A
site 00AE5   ; OUT ($BF),A
site 00AEC   ; OUT ($BF),A
site 00AF1   ; OUT ($BF),A
otir 00AF7   ; OUTI
site 00B5B   ; OUT ($BF),A
site 00B61   ; OUT ($BF),A
site 00B67   ; OUT ($BE),A
site 00B6D   ; OUT ($BE),A
site 00D2E   ; OUT ($BF),A
site 00D32   ; OUT ($BF),A
site 00D37   ; OUT ($BE),A
site 00D3B   ; OUT ($BE),A
site 01ED8   ; OUT ($BF),A
site 01EDC   ; OUT ($BF),A
site 01EE0   ; OUT ($BE),A
site 01EE7   ; OUT ($BE),A
site 01F79   ; OUT ($BF),A
site 01F7C   ; OUT ($BF),A
site 01FA0   ; OUT ($BE),A
site 01FA7   ; OUT ($BE),A
site 02812   ; OUT ($BF),A
site 02817   ; OUT ($BF),A
site 0281C   ; OUT ($BE),A
site 02824   ; OUT ($BE),A
site 02834   ; OUT ($BF),A
site 02839   ; OUT ($BF),A
site 0283E   ; OUT ($BE),A
site 02846   ; OUT ($BE),A
site 02EA1   ; IN A,($BE)
site 02EA9   ; OUT ($BE),A
site 02EAE   ; OUT ($BF),A
site 02EB6   ; OUT ($BF),A
site 02EC1   ; OUT ($BF),A
site 02EC8   ; OUT ($BF),A
site 033D8   ; OUT ($BF),A
site 033DD   ; OUT ($BF),A
site 033E3   ; IN A,($BE)
site 0344C   ; OUT ($BF),A
site 03451   ; OUT ($BF),A
site 03457   ; IN A,($BE)
site 036B4   ; OUT (C),E
site 036B6   ; OUT (C),D
site 036B9   ; OUTI
site 036BF   ; OUTI
site 03AC6   ; OUT ($BF),A
site 03ACA   ; OUT ($BF),A
site 03BEC   ; OUT ($BF),A
site 03BF0   ; OUT ($BF),A
site 03C09   ; OUT ($BF),A
site 03C0D   ; OUT ($BF),A
site 03C13   ; OUT ($BE),A
site 03C1B   ; OUT ($BF),A
site 03C1F   ; OUT ($BF),A
site 03C2A   ; OUT ($BF),A
site 03C2E   ; OUT ($BF),A
site 03C45   ; OUT ($BF),A
site 03C4B   ; OUT ($BF),A
site 03C57   ; OUT ($BE),A
site 03C5C   ; OUT ($BF),A
site 03C60   ; OUT ($BF),A
site 03C6D   ; OUT ($BF),A
site 03C71   ; OUT ($BF),A
site 03C76   ; OUT ($BF),A
site 03C7A   ; OUT ($BF),A
site 03E6D   ; OUT ($BF),A
site 03E71   ; OUT ($BF),A
site 03F49   ; OUT ($BF),A
site 03F4E   ; OUT ($BF),A
site 03F57   ; OUT ($BE),A
site 03F61   ; OUT ($BE),A
site 04157   ; OUT ($BF),A
site 0415C   ; OUT ($BF),A
site 04165   ; OUT ($BE),A
site 0416F   ; OUT ($BE),A
site 05841   ; IN A,($BE)
site 05848   ; IN A,($BE)
site 05868   ; IN A,($BE)
site 0586E   ; IN A,($BE)
site 05887   ; OUT ($BE),A
site 0588D   ; OUT ($BE),A
site 058A1   ; OUT ($BE),A
site 058AA   ; OUT ($BE),A
site 05A43   ; OUT ($BF),A
site 05A47   ; OUT ($BF),A
site 1C19E   ; OUT ($7F),A
site 1C26D   ; OUT ($7F),A
site 1C404   ; OTIR
site 1C51A   ; OUT ($7F),A
site 1C524   ; OUT ($7F),A
site 1C541   ; OUT ($7F),A
site 1C645   ; OUT ($7F),A
site 1C6D1   ; OUT ($7F),A
site 1C774   ; OUT ($7F),A
site 1C77D   ; OUT ($7F),A
site 1C78D   ; OUT ($7F),A
site 1C7EA   ; OUT ($7F),A
site 1C807   ; OUT ($7F),A
mapst 0004F   ; LD ($FFFF),A
mapldk 00099   # LD HL,$FFFC; LD (HL),$00
maphl 0009F   # LD (HL),$00, HL = $FFFD
maphl 000A2   # LD (HL),$01, HL = $FFFE
maphl 000A5   # LD (HL),$02, HL = $FFFF
mapst 004B9   ; LD ($FFFF),A
mapst 0051C   ; LD ($FFFF),A
mapst 006AC   ; LD ($FFFF),A
mapst 006B5   ; LD ($FFFF),A
mapst 00802   ; LD ($FFFF),A
mapst 00BA2   ; LD ($FFFF),A
mapst 00BE1   ; LD ($FFFF),A
mapst 00CB1   ; LD ($FFFF),A
mapst 00D84   ; LD ($FFFF),A
mapst 0228F   ; LD ($FFFF),A
mapst 0232B   ; LD ($FFFF),A
mapst 0236C   ; LD ($FFFF),A
mapst 023BC   ; LD ($FFFF),A
mapst 023CF   ; LD ($FFFF),A
mapst 02654   ; LD ($FFFF),A
mapst 02746   ; LD ($FFFF),A
mapst 02EEC   ; LD ($FFFF),A
mapst 02F5B   ; LD ($FFFF),A
mapst 02F9E   ; LD ($FFFF),A
mapst 02FC7   ; LD ($FFFF),A
mapst 02FD7   ; LD ($FFFF),A
mapst 02FE7   ; LD ($FFFF),A
mapst 02FF9   ; LD ($FFFF),A
mapst 03100   ; LD ($FFFF),A
mapst 0311F   ; LD ($FFFF),A
mapst 03147   ; LD ($FFFF),A
mapst 03185   ; LD ($FFFF),A
mapst 031CA   ; LD ($FFFF),A
mapst 03233   ; LD ($FFFF),A
mapst 03253   ; LD ($FFFF),A
mapst 03351   ; LD ($FFFF),A
mapst 0339B   ; LD ($FFFF),A
mapst 033AF   ; LD ($FFFF),A
mapst 0347D   ; LD ($FFFF),A
mapst 034A7   ; LD ($FFFF),A
mapst 035E6   ; LD ($FFFF),A
mapst 03607   ; LD ($FFFF),A
mapst 03A29   ; LD ($FFFF),A
mapst 03F45   ; LD ($FFFF),A
mapst 04153   ; LD ($FFFF),A
mapst 04414   ; LD ($FFFF),A
mapst 0466C   ; LD ($FFFF),A
mapst 0468C   ; LD ($FFFF),A
mapst 046AB   ; LD ($FFFF),A
mapst 046EF   ; LD ($FFFF),A
mapst 04976   ; LD ($FFFF),A
mapst 04BCE   ; LD ($FFFF),A
mapst 04BEE   ; LD ($FFFF),A
mapst 04C0D   ; LD ($FFFF),A
mapst 04C51   ; LD ($FFFF),A
mapst 056B9   ; LD ($FFFF),A
mapst 05E5F   ; LD ($FFFF),A
mapst 05EB1   ; LD ($FFFF),A
mapst 05EC9   ; LD ($FFFF),A
mapst 05F06   ; LD ($FFFF),A
mapst 05F24   ; LD ($FFFF),A
mapst 0606B   ; LD ($FFFF),A
mapst 0611B   ; LD ($FFFF),A
mapst 06140   ; LD ($FFFF),A
mapst 06189   ; LD ($FFFF),A
mapst 0624F   ; LD ($FFFF),A
mapst 062D5   ; LD ($FFFF),A
mapst 06C70   ; LD ($FFFF),A
mapst 06D9E   ; LD ($FFFF),A
mapst 06F01   ; LD ($FFFF),A
mapst 06F17   ; LD ($FFFF),A
mapst 07003   ; LD ($FFFF),A
mapst 0703C   ; LD ($FFFF),A
mapst 07078   ; LD ($FFFF),A
mapst 07108   ; LD ($FFFF),A
mapst 07118   ; LD ($FFFF),A
mapst 07128   ; LD ($FFFF),A
mapst 07198   ; LD ($FFFF),A
mapst 07230   ; LD ($FFFF),A
mapst 072A5   ; LD ($FFFF),A
mapst 072C1   ; LD ($FFFF),A
mapst 072D1   ; LD ($FFFF),A
mapst 0730F   ; LD ($FFFF),A
mapst 0731F   ; LD ($FFFF),A
mapst 073AE   ; LD ($FFFF),A
mapst 0760D   ; LD ($FFFF),A
asm 00178 6    ; DEC BC; LD A,C; OR B; JP NZ,$0178: the video rate test's delay loop
    rst $30
    db far_io, pg_vrate, ent_vrate
    nop
    nop
endasm
asm 00180 7    ; AND A; LD A,1; JP M,$0187; DEC A: the rate from vrate, BC = 0 as after the loop
    ld a,b
    ld bc,0
    jp $0187
endasm
asm 00454 5    ; PUSH BC; PUSH DE; PUSH HL; CALL $01D3: the tile upload, through page 0 (tcopy)
    rst $30
    db far_io, pg_tcopy, ent_tcopy
    ret
endasm
asm 00582 5    ; PUSH BC; PUSH DE; PUSH HL; CALL $01D3: the mirrored tile upload, through page 0 (tflip)
    rst $30
    db far_io, pg_tflip, ent_tflip
    ret
endasm
asm 0055F 7    ; PUSH BC; PUSH DE; PUSH HL; DI; CALL $01D3: the player tile upload, through page 0 (tcopy)
    rst $30
    db far_io, pg_tcopy, ent_tcopy
    xor a               ; A = 0 and EI, as the game's routine leaves them
    ei
    ret
endasm
asm 001DD 5    ; LD IX,$029B; LD A,($C20E): the sprite table and palette upload, through page 0 (sat)
    rst $30
    db far_io, pg_sat, ent_sat
    ret
endasm
page 0 sat tcopy tflip vrate
; sat: in place of $01DD-$029A, the frame handler's sprite table and palette upload. The game keeps the
; sprite table in RAM as 8 blocks of 8 Y bytes ($C300-$C33F) and 8 blocks of 16 X and tile
; bytes ($C340-$C3BF). $01DD writes the Y blocks to $3F00 and the X and tile blocks to $3F80
; through the unrolled OUTI runs $037D and $035C, 16 runtime calls, in the order of the
; table at $029B when bit 0 of $C20E is set and in the reverse order ($02BB) when it is
; clear; the order changes every frame. Through the runtime the frame handler passes line
; 224 between the two halves, and the runtime's once-a-frame work then draws the Y bytes
; of one order with the X and tile bytes of the other. sat builds the 256 bytes of $3F00-
; $3FFF in the page in the game's order and writes them with one jt_vwrite call, so the
; once-a-frame work sees the whole table or none of it. $3F40-$3F7F, which the VDP does not
; read, is written as 0, as the reference holds it. Then the palette: the game writes all 32
; CRAM entries from $C3C0 every frame through the OUTI run $031B, about 85,000 cycles through
; the runtime; sat writes only the entries whose colour differs from the runtime's copy
; (cram_upd). Keeps the interrupt state (off: the frame handler, or the start-up at $01CF);
; returns as the game's routine: C = $BE, HL = $C3E0; A, B, DE change. Uses jt_vwrite and
; the runtime internals cram, vdp_addr, vdp_code, vdp_latch and vdp_rbuf.
sat:    ld (s_sp),sp
        ld sp,stk
        push ix
        push iy
        ld a,($C20E)
        and 1
        ld bc,8                 ; Y blocks: $C300 up, or $C338 down
        ld (s_ys),bc
        ld bc,16                ; X and tile blocks: $C340 up, or $C3B0 down
        ld (s_xs),bc
        ld hl,$C300
        ld (s_y0),hl
        ld hl,$C340
        ld (s_x0),hl
        jr nz,1f
        ld hl,-8
        ld (s_ys),hl
        ld hl,-16
        ld (s_xs),hl
        ld hl,$C338
        ld (s_y0),hl
        ld hl,$C3B0
        ld (s_x0),hl
1:      ld de,buf
        ld hl,(s_y0)
        ld a,8
2:      push hl
        ld bc,8
        ldir
        pop hl
        ld bc,(s_ys)
        add hl,bc
        dec a
        jr nz,2b
        ld de,buf+128
        ld hl,(s_x0)
        ld a,8
3:      push hl
        ld bc,16
        ldir
        pop hl
        ld bc,(s_xs)
        add hl,bc
        dec a
        jr nz,3b
        ld hl,buf
        ld de,$3F00
        ld bc,$0001             ; one run of 256 bytes
        ld ix,256
        ld iy,256
        ld a,1                  ; the source as mapped now: buf is in this page
        call jt_vwrite
        ld hl,$C3C0
        ld bc,$2000             ; 32 entries from index 0
        call cram_upd
        ld c,$BE
        ld hl,$C3E0
        pop iy
        pop ix
        ld sp,(s_sp)
        ret
; HL = the source, C = the first CRAM index, B = the entries. Each entry whose colour (low 6
; bits) differs from cram gets the VDP address and a write through the I/O RST; then the VDP
; state is as B writes from index C leave it: address C + B, code 3, latch clear, read buffer
; the last byte.
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
        rst $30
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
s_sp:   dw 0
s_ys:   dw 0
s_xs:   dw 0
s_y0:   dw 0
s_x0:   dw 0
        ds 32
stk:
buf:    ds 256
; tcopy: in place of $0454. HL = the VRAM address, DE = the source, B = the tiles (0 means
; 256). The game's routine sets the address and sends each tile's 32 bytes through the OUTI
; run $031B, 32 runtime calls a tile; tcopy writes the B * 32 bytes with one jt_vwrite call,
; the source as the game sees it. Returns as the game's routine: BC, DE, HL kept, A = H, the
; interrupt state kept.
tcopy:  ld a,i                  ; P/V = the interrupt state
        di
        ld (t_sp),sp
        ld sp,t_stk
        push af
        push ix
        push iy
        push hl
        push de
        push bc
        ex de,hl                ; HL = the source, DE = the VRAM address
        ld c,b                  ; C runs of 32 bytes
        ld b,32
        ld ix,32
        ld iy,32
        xor a                   ; the source as the game sees it
        call jt_vwrite
        jp t_end
; tflip: in place of $0582. HL = the VRAM address, DE = the source, B = the tiles (0 means
; 256). The game's routine sends each source byte b as the byte at $7E00 + b (bank 1, a
; table of the bytes with their bits in reverse order: the tile mirrored left to right),
; one runtime call a byte. tflip looks the bytes up into fbuf and writes them with
; jt_vwrite, FCHUNK tiles a call. Returns as the game's routine: BC, DE, HL kept, A = the
; last source byte, the interrupt state kept.
FCHUNK  equ 64
tflip:  ld a,i
        di
        ld (t_sp),sp
        ld sp,t_stk
        push af
        push ix
        push iy
        push hl
        push de
        push bc
        ld (f_vram),hl
        ld l,b                  ; f_left = the tiles, 1 to 256
        ld h,0
        dec l
        inc hl
        ld (f_left),hl
1:      ld hl,(f_left)          ; A = the tiles in this chunk
        ld a,h
        or a
        ld a,FCHUNK
        jr nz,2f
        ld a,l
        cp FCHUNK+1
        jr c,2f
        ld a,FCHUNK
2:      ld (f_n),a
        ld b,a                  ; B * 32 bytes from DE, through the table, into fbuf
        ld hl,fbuf
3:      push bc
        ld b,32
4:      ld a,(de)
        inc de
        ld (f_last),a
        ld c,a
        push de
        ld e,c
        ld d,$7E
        ld a,(de)
        pop de
        ld (hl),a
        inc hl
        djnz 4b
        pop bc
        djnz 3b
        push de
        ld a,(f_n)
        ld c,a                  ; C runs of 32 bytes
        ld b,32
        ld de,(f_vram)
        ld hl,fbuf
        ld ix,32
        ld iy,32
        ld a,1                  ; fbuf is in this page
        call jt_vwrite
        ld l,c                  ; f_vram += C * 32
        ld h,0
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        add hl,hl
        ld de,(f_vram)
        add hl,de
        ld (f_vram),hl
        ld hl,(f_left)          ; f_left -= C
        ld b,0
        or a
        sbc hl,bc
        ld (f_left),hl
        pop de
        ld a,h
        or l
        jr nz,1b
        ld a,(f_last)
        ld (t_a),a
        pop bc
        pop de
        pop hl
        pop iy
        pop ix
        pop af
        ld sp,(t_sp)
        jp po,5f
        ld a,(t_a)
        ei
        ret
5:      ld a,(t_a)
        ret
t_end:  pop bc
        pop de
        pop hl
        pop iy
        pop ix
        pop af
        ld sp,(t_sp)
        jp po,7f
        ld a,h
        ei
        ret
7:      ld a,h
        ret
; vrate: at $0178, the video rate test at $016C. The test waits for the frame flag with
; interrupts off, runs the delay loop $0178 (2710 passes of 24 T-states, 65040 T-states:
; longer than an NTSC frame, shorter than a PAL one) and reads the flag again: set means
; 60 Hz, and $0187 stores 1 in $C102, else 0. $C102 = 0 makes the game run its 50 Hz speed-up
; (movement steps doubled at $45B0, $4B12; a timer one shorter at $61FE). The runtime raises
; the frame flag again only from its frame event, which does not run with interrupts off, so
; on the Next the test always read 50 Hz. The entry gives the answer instead: B = 1 when the
; Next runs at 60 Hz (NextReg $05 bit 2), else 0. Keeps every other register but A and F.
; The status read at $017E stays, and the patch at $0180 stores B.
vrate:  push af
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld b,0
        bit 2,a
        jr z,1f
        inc b
1:      pop af
        ret
t_sp:   dw 0
t_a:    db 0
f_vram: dw 0
f_last: db 0
f_left: dw 0
f_n:    db 0
        ds 48
t_stk:
fbuf:   ds FCHUNK*32
endpage

# Alien Storm (Europe, Brazil).cht, "Infinite Health (L)": RAM $C113 is the health bar (L)
poke "Infinite health"
ar 00C1-130F
endpoke

# Alien Storm (Europe, Brazil).cht, "Infinite Weapon Energy (E)": RAM $C114 is the weapon
# energy bar (E)
poke "Infinite energy"
ar 00C1-140F
endpoke

# Alien Storm (Europe, Brazil).cht, "Infinite Lives": the patched byte is the credit decrement
# at Continue YES (the lives of the code name are the continue credits, RAM $C119)
poke "Infinite credits"
gg 3A4-BE8-2A2
endpoke
