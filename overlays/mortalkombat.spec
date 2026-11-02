# Mortal Kombat (Europe, Brazil) (En), CRC32 302DC686, 512K, Sega mapper.
# Drafted by tools/mkspec.py from sitescan output with the 60 s reference I/O log, then extended.
# The scanner loses slot 1 after the first store of a variable bank to $FFFE, so it does not follow
# the calls into bank 1 ($4000-$7FFF), which is in slot 1 whenever code runs there; and bank 0 $73A4
# is a banked-call trampoline with an inline bank and address after each CALL. The sites below were
# found with these extra entry points (sitescan.py --entry):
#   bank 1 (slot 1): 4000 4017 4040 4047 4068 4088 40B6 40BF 40CA 40D4 4216 4232 424B 425E 42A9
#     42BD 4305 4336 43A9 556D 55A7 58DC 5A7A 5A8A 5B91 5BAE 5CD7 5D64 5DEE 5E02 5E14 5E34 5E68
#     5F6D 6029 6072 60E6 613A 61AB 61E7 621A 6275 62C8 62CE 6318 63C2 63CA 63EB 6404 643C 6457
#     6510 6587 6608 6628 662A 66D5 66F2 66F7 67E5 67E7 6AC7 6B6B 6BE2 6C71 6D31 6D74 6DC1 6DFC
#     6E60 6E74 6E8F 6E9D 6EA8 6EB3 6EF9 6FCC 711E 7172 71C3 73A4 73E9 770B 7806 7813 7820 78C4
#     78C5 78CB 78DB 7B34 7B4B 7B5F;
#   bank 0: 0E00 3C19; bank 2: B406 B434 B49C B546 B54F B57A; bank 3: 8AE0 8AFB 8B05 8B20;
#   bank 5: 910A 9210 9340 96A2 96C0 9B84 9CCD 9DC9 9F9B A081; bank 6: 867F 906E 91AC 92C4 9353
#     940C 942E 99E0 9C9E 9CB6 9DBA 9E88 A0B1 A146 A158 B0D6 B0F1 B93A B957 BA89 BE5F.
# The reference log ran the bank 1 text writers ($66C7, $6EA8) and the screen writers at $6C62 and
# $7171 that these entries reach; unpatched, the high score table showed no names.
# Spec gaps (data/scan-verdicts.tsv): unused are a development-kit monitor at bank 2 $8000 and its
# two copies in bank 31 ($8001, $9D00), and the routine $7272; known is the level data LDIR at $5FBC;
# false are graphics and table bytes.
# Register 0 has line interrupts on and register 10 is always $FF, so no line interrupt fires.
# Priority cells are only the HUD rows 0-1 in a fight; priority is off.
name Mortal Kombat
hz 50		; No-Intro regions Europe, Brazil
cart 302DC686
# No free RST vector: $0000-$0002 (DI; LD SP part) becomes the vector,
# the game starts at $0004 with the SP its LD SP,nn set.
vector 00 io
start 0004 DFEE
# Delay $40BF (bank 1): DEC HL : LD A,L : OR H : JR NZ,$40BF : RET, 26 T-states a pass, HL passes
# (0 means 65536). $40BC (HL = 0), $40B6 (B times $40BC), $4068 and $4088 build the logo, title and
# text-screen holds from it. A busy loop, so at 28 MHz every hold was about 8 times too short.
# Page entry delay waits the same real time on the Next's raster line: a Master System frame of
# 71,364 T-states (PAL, 313 lines of 228) is a Next frame of 311 lines, so a pass is 29/256 of a line.
asm 040BF 6          ; DEC HL : LD A,L : OR H : JR NZ,$40BF : RET
    rst $00
    db far_io, pg_delay, ent_delay
    ret
endasm
# Sprite tile streamer $334F (bank 0): after one VDP address write it sends the fighters' sprite tiles
# in groups of 4 bytes, through five loops that each made one runtime call (about 9,000 cycles) for
# every 4 bytes; in a fight they took about a fifth of every frame. Code caves replace each loop with
# a page 1 entry that makes the same bytes and writes them at the VDP address with one wfast call.
# wfast copies tile data straight into the runtime's VRAM copy; any other write goes through jt_vwrite.
# The fighters' tiles are streamed again every game step, so these entries and the renderer's (pages
# 3 and 4) set the game's speed in a fight: each reads its source straight (LDI, LDIR, an unrolled
# loop) when the source avoids $2000-$3FFF, the slot the page is in, and byte by byte through jt_peek
# only when it does not.
#   $34D3: B groups, each 1 byte skipped and 4 bytes sent       -> grp_s
#   $34FA: B groups of 4 bytes sent                               -> grp_c
#   $3547: as $34D3, each byte through the table at $0A00 (mirror) -> grp_sx
#   $3572: as $34FA, each byte through the table at $0A00          -> grp_cx
#   $3529: B zero bytes                                           -> zfill
asm 034D3 26         ; LD B,A : loop to JP NZ,$34D4
    rst $00
    db far_io, pg_grp_s, ent_grp_s
    jp $34ED
endasm
asm 034FA 24         ; LD B,A : loop to JR NZ,$34FB
    rst $00
    db far_io, pg_grp_c, ent_grp_c
    jp $3512
endasm
asm 03529 6          ; XOR A : OUT ($BE),A : NOP : DJNZ $352A
    rst $00
    db far_io, pg_zfill, ent_zfill
endasm
asm 03547 30         ; LD B,A : PUSH DE : LD D,$0A : loop to JP NZ,$354B : POP DE
    rst $00
    db far_io, pg_grp_sx, ent_grp_sx
    jp $3565
endasm
asm 03572 28         ; LD B,A : PUSH DE : LD D,$0A : loop to JR NZ,$3576 : POP DE
    rst $00
    db far_io, pg_grp_cx, ent_grp_cx
    jp $358E
endasm
page 1 grp_s grp_c grp_sx grp_cx zfill
    OPT --zxnext        ; NEXTREG
; The group loops of $334F, as the game's code leaves them: A = the last byte sent, B = 0, HL past
; the source bytes read; C, DE, IX, IY and the alternate registers kept; F changed (the game's code
; after each loop sets it again). A = the group count at entry, 0 meaning 256. The bytes are made in
; buf and written at the VDP address with one wfast call, which leaves VRAM and the VDP state as the
; game's data writes would. The game's interrupts stay as they are (its handler does not touch the
; VDP or $FFFD); wfast uses the stack for the call of jt_vwrite.
grp_s:  ld (sv_bc),bc
        ld c,1                  ; skip one byte before each group
        jr grp
grp_c:  ld (sv_bc),bc
        ld c,0
        jr grp
grp_sx: ld (sv_bc),bc
        ld c,3                  ; skip, and the table
        jr grp
grp_cx: ld (sv_bc),bc
        ld c,2
grp:    ld (sv_de),de
        ld (cnt),a
        ld b,a
        ld (sv_ix),ix
        push hl                 ; the source span: cnt * 4, or cnt * 5 with the skip
        ld l,a
        ld h,0
        or a
        jr nz,.sp1
        inc h                   ; cnt 0 = 256
.sp1:   ld e,l
        ld d,h
        add hl,hl
        add hl,hl
        bit 0,c
        jr z,.sp2
        add hl,de
.sp2:   ex de,hl
        pop hl
        call srcok
        jr nz,.slow
        ld de,buf               ; fast path: the source avoids this page's slot, read it straight
        ld a,(cnt)
        bit 1,c
        jr nz,.ftab
        bit 0,c
        jr nz,.fskip
.fcopy: ldi
        ldi
        ldi
        ldi
        dec a
        jr nz,.fcopy
        jp .done
.fskip: inc hl
        ldi
        ldi
        ldi
        ldi
        dec a
        jr nz,.fskip
        jp .done
.ftab:  ld ixl,a                ; groups; each byte through the table at $0A00 (BC)
        ld a,c
        ld b,$0A
        rra
        jr nc,.ftc
.fts:   inc hl
        rept 4
        ld c,(hl)
        inc hl
        ld a,(bc)
        ld (de),a
        inc de
        endr
        dec ixl
        jr nz,.fts
        jp .done
.ftc:   rept 4
        ld c,(hl)
        inc hl
        ld a,(bc)
        ld (de),a
        inc de
        endr
        dec ixl
        jr nz,.ftc
        jp .done
.slow:  ld de,buf
.grp:   bit 0,c
        jr z,.noskip
        inc hl
.noskip:
        ld a,4
        ld (left),a
.byte:  ld a,h                  ; the source byte as the game sees it
        and $E0
        cp $20
        jr z,.peek
        ld a,(hl)
        jr .got
.peek:  call jt_peek
.got:   bit 1,c
        jr z,.store
        ld (.xl+1),a
.xl:    ld a,($0A00)            ; the low byte is set above
.store: ld (de),a
        inc de
        inc hl
        ld a,(left)
        dec a
        ld (left),a
        jr nz,.byte
        djnz .grp
        ld (sv_ix),ix
.done:  dec de
        ld a,(de)
        ld (last),a
        ld (sv_hl),hl
        ld (sv_iy),iy
        ld a,(cnt)              ; 4 * cnt bytes (cnt 0 = 256)
        ld l,a
        ld h,0
        or a
        jr nz,.nz
        inc h
.nz:    add hl,hl
        add hl,hl
        ld de,buf
        call wfast
        ld hl,(sv_hl)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld b,0
        ld a,1
        dec a                   ; F as the game's DEC B to 0 leaves it
        ld a,(last)
        ret
; srcok: Z when the DE bytes (1 to 1280) from HL avoid $2000-$3FFF, where this page sits in place
; of the game's bank 0, and do not wrap past $FFFF; NZ else. Keeps BC, DE and HL.
srcok:  push hl
        add hl,de
        jr c,.bad               ; past $FFFF
        dec hl                  ; the last byte
        ld a,h
        cp $20
        jr c,.ok                ; ends below $2000
        pop hl
        push hl
        ld a,h
        cp $40
        jr nc,.ok               ; starts at $4000 or above
.bad:   pop hl
        or 1
        ret
.ok:    pop hl
        xor a
        ret
; zfill: as $3529-$352E: B zero bytes (B is 4 to 252 here) at the VDP address. Returns A = 0, B = 0,
; the other registers kept.
zfill:  ld (sv_bc),bc
        ld (sv_de),de
        ld (sv_hl),hl
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld l,b                  ; B zero bytes (0 = 256)
        ld h,0
        ld a,b
        or a
        jr nz,.n
        inc h
.n:     ld de,zero
        call wfast
        ld hl,(sv_hl)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld b,0
        xor a
        ret
; wchunk: HL bytes (1 to 1024) from DE at the VDP address, in runs of up to 256 bytes.
wchunk: ld (wflag),a
.next:  ld a,h
        or l
        ret z
        ld c,l
        ld a,h
        or a
        jr z,.last
        dec h
        ld c,0
        jr .go
.last:  ld hl,0
.go:    ld (wleft),hl
        ex de,hl
        ld de,(vdp_addr)
        ld b,c
        ld c,1
        ld ix,0
        ld iy,0
        ld a,(wflag)
        call jt_vwrite
        ld c,b
        ld a,c
        or a
        jr nz,.add
        inc h
        jr .st
.add:   add a,l
        ld l,a
        jr nc,.st
        inc h
.st:    ex de,hl
        ld hl,(wleft)
        jr .next
wflag:  db 0
wleft:  dw 0
; wfast: HL bytes (1 to 1024) from DE in this page, written at the VDP address as the game's data
; writes would leave VRAM and the VDP state. When every byte lands in tile data, it does the work
; of jt_vwrite's tile path itself: the VRAM copy, the tiles' dirty_pages marks, tiles_dirty and
; tw_cnt, the VDP address, code, latch and read buffer, then the call jt_vwrite's end makes (vw_tw:
; tw_check, or vbl_chkv while the frame work check is armed). Else it goes through wchunk
; (jt_vwrite). Interrupts are off while the VRAM copy is in slots 4-5, then as they were; this
; page's own stack (wf_stk) is used while the copy is mapped. A whole tile (32 bytes from a tile's
; start) is compared with the copy first, and copied and marked only when a byte differs: a tile
; with no dirty_pages mark already has its Next tile definition made from the bytes in the copy,
; so the conversion and the sprite pattern upload of an unchanged tile are skipped. Part tiles,
; and every tile of a write that wraps past $3FFF, are copied and marked.
; Changes every register but IX, IY and the alternates. Runtime internals: SHADOW_PAGE 28, 29 (the
; VRAM copy), region_tab $E400 (0: a tile page), dirty_pages $E440, tiles_dirty $E082, tw_cnt
; $E083, vw_tw $F9E6 (its CALL target at $F9E7), vw_stack_top $E0FC (the stack for that call).
WF_SHADOW equ 28
WF_REGION equ $E400
WF_DIRTY  equ $E440
WF_TDIRTY equ $E082
WF_TWCNT  equ $E083
WF_VWTW   equ $F9E6
WF_VWSTK  equ $E0FC
wfast:  ld (wf_n),hl
        ld (wf_src),de
        ld de,(vdp_addr)
        ld a,d
        and $3F
        ld d,a
        ld (wf_va),de
        dec hl
        add hl,de
        ld a,h
        and $3F
        ld c,a                  ; the last byte's VRAM page
        ld b,d                  ; the first
.chk:   ld l,b
        ld h,WF_REGION>>8
        ld a,(hl)
        or a
        jr nz,.slow             ; not tile data
        ld a,b
        cp c
        jr z,.fast
        inc b
        res 6,b
        jr .chk
.slow:  ld hl,(wf_n)
        ld de,(wf_src)
        ld a,1
        jp wchunk
.fast:  xor a
        ld (wf_one),a
        ld a,i
        ld a,0
        jp po,.di
        inc a
.di:    ld (wf_ei),a
        di
        nextreg $54,WF_SHADOW
        nextreg $55,WF_SHADOW+1
        ld hl,$4000
        ld de,(wf_va)
        or a
        sbc hl,de               ; bytes up to the end of VRAM
        ld de,(wf_n)
        or a
        sbc hl,de
        jr nc,.one              ; no wrap
        ld (wf_rest),hl         ; minus the bytes after the wrap
        ld hl,$4000
        ld de,(wf_va)
        or a
        sbc hl,de
        ld b,h
        ld c,l
        ld hl,(wf_src)
        set 7,d
        ldir
        ld de,(wf_rest)
        push hl
        ld hl,0
        or a
        sbc hl,de
        ld b,h
        ld c,l
        pop hl
        ld de,$8000
        ldir
        jp .copied
.one:   ld (wf_sp2),sp
        ld sp,wf_stk            ; this page's own stack while the copy is in slots 4-5
        ld hl,(wf_src)
        ld de,(wf_va)
        set 7,d                 ; the copy at $8000 + VRAM address
        ld bc,(wf_n)
        ld (wf_left),bc
        ld a,1
        ld (wf_one),a
        xor a
        ld (wf_any),a
.seg:   ld bc,(wf_left)         ; tile by tile: a whole tile is copied and marked only when one of
        ld a,b                  ; its bytes differs from the copy (the Next's tile is then not
        or c                    ; converted again for bytes it already shows); a part tile always
        jp z,.segd
        ld a,e
        and 31
        jr nz,.part
        ld a,b
        or a
        jr nz,.whole
        ld a,c
        cp 32
        jr nc,.whole
.part:  ld a,e                  ; bytes to the tile's end (1 to 32), or fewer when fewer are left
        and 31
        neg
        add a,32
        inc b
        dec b
        jr nz,.pc
        cp c
        jr c,.pc
        ld a,c
.pc:    call .tmark
        ld c,a
        ld b,0
        push hl
        ld hl,(wf_left)
        or a
        sbc hl,bc
        ld (wf_left),hl
        pop hl
        ldir
        jr .seg
.whole: push de
        push hl
        ld b,32
.cmp:   ld a,(de)
        cp (hl)
        jr nz,.ne
        inc hl
        inc e
        djnz .cmp
        pop af                  ; the same 32 bytes: HL is past them, DE moves on 32
        pop de
        ex de,hl
        ld bc,32
        add hl,bc
        ex de,hl
        jr .wl
.ne:    pop hl
        pop de
        call .tmark
        ld bc,32
        ldir
.wl:    push hl
        ld hl,(wf_left)
        ld bc,32
        or a
        sbc hl,bc
        ld (wf_left),hl
        pop hl
        jr .seg
.tmark: push af                 ; the dirty_pages bit of the tile at DE ($8000 + VRAM address)
        push hl
        push bc
        ld a,e
        rlca
        rlca
        rlca
        and 7
        ld c,a
        ld b,0
        ld hl,wf_bits
        add hl,bc
        ld c,(hl)
        ld a,d
        and $3F
        add a,WF_DIRTY & $FF
        ld l,a
        ld h,WF_DIRTY >> 8
        ld a,(hl)
        or c
        ld (hl),a
        ld a,1
        ld (wf_any),a
        pop bc
        pop hl
        pop af
        ret
.segd:  ld sp,(wf_sp2)
.copied:
        dec hl
        ld a,(hl)
        ld (vdp_rbuf),a
        ld bc,$243B             ; the game's pages back in slots 4-5 (interrupts are off)
        ld a,$54
        out (c),a
        inc b
        ld a,(cur_mmu+4)
        out (c),a
        dec b
        ld a,$55
        out (c),a
        inc b
        ld a,(cur_mmu+5)
        out (c),a
        ld hl,(wf_va)
        ld de,(wf_n)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (vdp_addr),hl        ; the VDP address after the last byte
        ld a,(wf_one)
        or a
        jr z,.markall
        ld a,(wf_any)           ; marked tile by tile above
        or a
        jr z,.marked
        jr .tdirty
.markall:
        ld hl,(wf_va)           ; tiles to mark: (address mod 32 + n + 31) / 32
        ld a,l
        and 31
        ld e,a
        ld d,0
        ld hl,(wf_n)
        add hl,de
        ld de,31
        add hl,de
        add hl,hl
        add hl,hl
        add hl,hl
        ld b,h
        ld hl,(wf_va)           ; HL = the first tile, address / 32
        ld a,l
        rlca
        rlca
        rlca
        and 7
        ld l,a
        ld a,h
        add a,a
        add a,a
        add a,a
        or l
        ld l,a
        ld a,h
        rlca
        rlca
        rlca
        and 1
        ld h,a
.mark:  ld a,l                  ; dirty_pages + tile / 8 gets the tile's bit
        and 7
        add a,wf_bits & $FF
        ld e,a
        ld a,0
        adc a,wf_bits >> 8
        ld d,a
        ld a,(de)
        ld c,a
        ld a,h
        rrca
        rrca
        rrca                    ; tile bit 8 as page bit 5
        ld e,a
        ld a,l
        rrca
        rrca
        rrca
        and $1F
        or e
        add a,WF_DIRTY & $FF
        ld e,a
        ld d,WF_DIRTY >> 8
        ld a,(de)
        or c
        ld (de),a
        inc hl
        res 1,h                 ; tiles wrap at 512
        djnz .mark
.tdirty:
        ld a,1
        ld (WF_TDIRTY),a
.marked:
        ld hl,(WF_TWCNT)
        ld de,(wf_n)
        add hl,de
        ld (WF_TWCNT),hl
        xor a
        ld (vdp_latch),a
        inc a
        ld (vdp_code),a
        ld (wf_sp),sp
        ld sp,WF_VWSTK          ; jt_vwrite's own stack, free while it does not run
        ld hl,(WF_VWTW+1)
        call .jphl              ; tw_check, or vbl_chkv
        ld sp,(wf_sp)
        ld a,(wf_ei)
        or a
        ret z
        ei
        ret
.jphl:  jp (hl)
wf_bits: db $01,$02,$04,$08,$10,$20,$40,$80
wf_rest: dw 0
wf_sp:  dw 0
wf_n:   dw 0
wf_src: dw 0
wf_va:  dw 0
wf_ei:  db 0
wf_one: db 0
wf_any: db 0
wf_left: dw 0
wf_sp2: dw 0
        ds 16                   ; wfast's stack while the VRAM copy is mapped
wf_stk:
cnt:    db 0
left:   db 0
last:   db 0
sv_bc:  dw 0
sv_de:  dw 0
sv_hl:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
zero:   ds 256
buf:    ds 1024
endpage
# Sprite table upload $40CA (bank 1): the Y list from $C5xx, then the X and tile list from $C580, in an
# order that rotates every frame. Each byte was a single OUTI through the runtime (about 4,700 cycles).
# Code caves at the two loops call page 2 entries that run the same loops into a buffer and write it
# with one jt_vwrite call at the VDP address the game set.
asm 0410E 5          ; LD C,$BE : LD A,L : OUTI   (the Y loop; JR Z,$4121 follows)
    rst $00
    db far_io, pg_saty, ent_saty
    nop
endasm
asm 04141 7          ; LD A,L : OUTI : ADD A,E : JR C,$4158 : NOP   (the X and tile loop)
    rst $00
    db far_io, pg_satx, ent_satx
    ret
endasm
page 2 saty satx
; saty: as the game's $410E-$4120, the Y loop: B bytes from HL, each next address worked out from L,
; D and E. Returns as the loop leaves them: B = 0 with Z set (so the game's JR Z,$4121 goes on to
; the $D0 end mark), C = $BE, A = L before the last byte, HL after it; DE kept.
; satx: as the game's $4141-$4157, the X and tile loop, up to its RET. Both write the bytes at the
; VDP address with one jt_vwrite call; the game's interrupts stay as they are (its handler does not
; touch the VDP or $FFFD), and the only stack used is the call of jt_vwrite.
    macro OUTX              ; OUTI into the buffer at IX: A and the other flags kept, Z from B
        ld (ta),a
        ld a,(hl)
        ld (ix+0),a
        inc ix
        ld a,(ta)
        inc hl
        dec b
    endm
saty:   ld (sv_ix),ix
        ld ix,buf
        ld c,$BE
.l1:    ld a,l
        OUTX
        jr z,.e1
        add a,e
        ld l,a
        sub d
        jp c,.l1
        add a,2
        ld l,a
        jp .l1
.e1:    call flush
        ld a,(ta)
        cp a                    ; Z set, as B = 0 left it
        ret
satx:   ld (sv_ix),ix
        ld ix,buf
.l2:    ld a,l
        OUTX
        add a,e
        jr c,.p58
        OUTX
        jr z,.e2
        ld l,a
        sub d
        jp c,.l2
        add a,$80
        ld l,a
        jp .l2
.p58:   OUTX
        jr z,.e2
        ld l,a
        sub d
        add a,$80
        ld l,a
        jp .l2
.e2:    call flush
        ld a,(ta)
        cp a
        ret
; flush: write buf up to IX at the VDP address; keeps A, BC, DE, HL; IX and IY as at the entry.
flush:  ld (ta),a
        ld (sv_bc),bc
        ld (sv_de),de
        ld (sv_hl),hl
        ld (sv_iy),iy
        ld (sv_end),ix
        ld hl,(sv_end)
        ld de,buf
        or a
        sbc hl,de
        ld b,l                  ; one run of 1 to 256 bytes (0 = 256)
        ld c,1
        ld hl,buf
        ld de,(vdp_addr)
        ld ix,0
        ld iy,0
        ld a,1
        call jt_vwrite
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld hl,(sv_hl)
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld a,(ta)
        ret
ta:     db 0
sv_bc:  dw 0
sv_de:  dw 0
sv_hl:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
sv_end: dw 0
buf:    ds 256
endpage
# Fighter tile renderer $2A62 (bank 0): it masks the fighter's tile rows over the background rows
# and sends them as name-table-free tile data, 4 bytes a row. Each byte went through the runtime:
# the unrolled 8-row form as one run per byte group, the loops as single OUTIs and OUTs. Code caves
# call page 3 entries that make the same bytes and write them with wfast (jt_vwrite for
# anything but tile data).
#   $2A80: 8 groups (mask byte at HL, then 4 rows (DE) AND mask OR (HL)), B kept -> msk8
#   $2C79, $2CC6: the same, B groups                                         -> msk
#   $2C4E, $2CFB: A groups of 4 bytes from HL (OUTI, with INC B after 3 of the 4) -> cp4
asm 02A80 240        ; 8 x (LD C,(HL) : INC HL : 4 x (LD A,(DE) : AND C : OR (HL) : OUT ($BE),A : INC DE : INC HL))
    rst $00
    db far_io, pg_msk8, ent_msk8
    jp $2B70
endasm
asm 02C79 32         ; LD C,(HL) : INC HL : 4 x (...) : DJNZ $2C79 : JP $2B70
    rst $00
    db far_io, pg_msk, ent_msk
    jp $2B70
endasm
asm 02CC6 32         ; LD C,(HL) : INC HL : 4 x (...) : DJNZ $2CC6
    rst $00
    db far_io, pg_msk, ent_msk
endasm
asm 02C4E 20         ; 4 x (OUTI : JR $+2 : INC B) : DEC A : JR NZ,$2C4E
    rst $00
    db far_io, pg_cp4, ent_cp4
endasm
asm 02CFB 20         ; 4 x (OUTI : JR $+2 : INC B) : DEC A : JR NZ,$2CFB
    rst $00
    db far_io, pg_cp4, ent_cp4
endasm
page 3 msk8 msk cp4
    OPT --zxnext        ; NEXTREG
; msk8, msk: as the renderer's masked rows. msk8 does 8 groups and keeps B; msk does B groups (0
; means 256) and returns B = 0. A group is a mask byte c at HL, then 4 bytes ((DE) AND c) OR (HL+1..4).
; Both return as the game's code leaves them: C = the last mask, A = the last byte and F as its OR
; left it, DE 4 and HL 5 bytes a group further on; IX, IY and the alternate registers kept.
; cp4: as 4 x (OUTI : JR $+2 : INC B) : DEC A : JR NZ: A groups of 4 bytes from HL (0 means 256).
; Returns A = 0 with Z set, HL past the bytes, B less the groups (the fourth OUTI of a group has no
; INC B after it); C and DE kept.
; Every entry writes at the VDP address with wfast. The game's interrupts stay as they are (its
; handler does not touch the VDP or $FFFD); the stack is used for the call of jt_vwrite.
    macro RDHL              ; A = the byte the game sees at HL
        ld a,h
        and $E0
        cp $20
        jr nz,.direct
        call jt_peek
        jr .done
.direct:
        ld a,(hl)
.done:
    endm
msk8:   ld (sv_b),bc
        ld b,8
        call mskrun
        ld a,(sv_b+1)
        ld b,a
        jr mskf
msk:    call mskrun
        ld b,0
mskf:   ld a,(lastp)            ; A and F as the last AND C : OR (HL) left them
        ld (.or+1),a
        ld a,(lastd)
        and c
.or:    or 0
        ret
; mskrun: B groups into buf, then written; leaves DE and HL advanced, IX and IY kept.
mskrun: ld (sv_ix),ix
        ld (sv_de0),de
        ld ix,buf
        ld a,b                  ; fast path: HL (5 bytes a group) and DE (4) avoid this page's slot
        push hl
        ld l,a
        ld h,0
        or a
        jr nz,.g1
        inc h                   ; 0 = 256 groups
.g1:    ld e,l
        ld d,h
        add hl,hl
        add hl,hl
        ld (sv_g4),hl
        add hl,de
        ex de,hl                ; DE = 5 bytes a group
        pop hl
        call srcok
        jr nz,.slow
        push hl
        ld hl,(sv_de0)
        ld de,(sv_g4)
        call srcok
        pop hl
        jr nz,.slow
        ld de,(sv_de0)
.fg:    ld c,(hl)               ; the game's group, with the OUT as a store into buf
        inc hl
        rept 4
        ld a,(de)
        and c
        or (hl)
        ld (ix+0),a
        inc ix
        inc de
        inc hl
        endr
        djnz .fg
        dec de                  ; the last byte's parts, from which msk8 and msk make A and F
        ld a,(de)
        inc de
        ld (lastd),a
        dec hl
        ld a,(hl)
        inc hl
        ld (lastp),a
        ld a,c
        ld (lastm),a
        jp .tail
.slow:  ld de,(sv_de0)
.grp:   RDHL
        ld c,a                  ; the mask
        ld (lastm),a
        inc hl
        ld a,4
        ld (left),a
.row:   ex de,hl
        RDHL
        ex de,hl
        ld (lastd),a
        RDHL
        ld (lastp),a
        ld (.o+1),a
        ld a,(lastd)
        and c
.o:     or 0
        ld (ix+0),a
        inc ix
        inc de
        inc hl
        ld a,(left)
        dec a
        ld (left),a
        jr nz,.row
        djnz .grp
.tail:  ld a,(ix-1)
        ld (lastb),a
        ld (sv_hl),hl
        ld (sv_de),de
        ld (sv_iy),iy
        ld (sv_end),ix
        ld hl,(sv_end)
        ld de,buf
        or a
        sbc hl,de               ; bytes: 4 to 1024
        ld de,buf
        call wfast
        ld hl,(sv_hl)
        ld de,(sv_de)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld a,(lastm)
        ld c,a
        ret
; srcok: Z when the DE bytes (1 to 1280) from HL avoid $2000-$3FFF, where this page sits in place
; of the game's bank 0, and do not wrap past $FFFF; NZ else. Keeps BC, DE and HL.
srcok:  push hl
        add hl,de
        jr c,.bad               ; past $FFFF
        dec hl                  ; the last byte
        ld a,h
        cp $20
        jr c,.ok                ; ends below $2000
        pop hl
        push hl
        ld a,h
        cp $40
        jr nc,.ok               ; starts at $4000 or above
.bad:   pop hl
        or 1
        ret
.ok:    pop hl
        xor a
        ret
; wchunk: HL bytes (1 to 1024) from DE at the VDP address, in runs of up to 256 bytes. A is jt_vwrite's source flag. Changes every register
; but the alternates.
wchunk: ld (wflag),a
.next:  ld a,h
        or l
        ret z
        ld c,l                  ; this chunk: L bytes, or 256 while 256 or more are left
        ld a,h
        or a
        jr z,.last
        dec h
        ld c,0
        jr .go
.last:  ld hl,0
.go:    ld (wleft),hl
        ex de,hl                ; HL = the source
        ld de,(vdp_addr)
        ld b,c                  ; one run of the chunk
        ld c,1
        ld ix,0
        ld iy,0
        ld a,(wflag)
        call jt_vwrite
        ld c,b
        ld a,c                  ; the source after the chunk
        or a
        jr nz,.add
        inc h
        jr .st
.add:   add a,l
        ld l,a
        jr nc,.st
        inc h
.st:    ex de,hl
        ld hl,(wleft)
        jr .next
cp4:    ld (sv_hl),hl
        ld (sv_bc),bc
        ld (sv_de),de
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld (cnt4),a
        ld l,a                  ; bytes = 4 * groups (0 = 256 groups)
        ld h,0
        or a
        jr nz,.nz
        inc h
.nz:    add hl,hl
        add hl,hl
        ld (sv_n),hl
        ld b,h
        ld c,l
        ld hl,(sv_hl)
        ld de,(sv_n)
        call srcok
        ld de,buf
        jr nz,.copy
        ldir                    ; the source avoids this page's slot: copied straight
        jr .copied
.copy:  RDHL                    ; the bytes as the game sees them, into buf
        ld (de),a
        inc de
        inc hl
        dec bc
        ld a,b
        or c
        jr nz,.copy
.copied:
        ld hl,(sv_n)
        ld de,buf
        call wfast
        ld hl,(sv_hl)
        ld de,(sv_n)
        add hl,de
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld a,(cnt4)             ; the last OUTI of each group has no INC B: B goes down by the groups
        neg
        add a,b
        ld b,a
        xor a                   ; A = 0, Z set
        ret
; wfast: HL bytes (1 to 1024) from DE in this page, written at the VDP address as the game's data
; writes would leave VRAM and the VDP state. When every byte lands in tile data, it does the work
; of jt_vwrite's tile path itself: the VRAM copy, the tiles' dirty_pages marks, tiles_dirty and
; tw_cnt, the VDP address, code, latch and read buffer, then the call jt_vwrite's end makes (vw_tw:
; tw_check, or vbl_chkv while the frame work check is armed). Else it goes through wchunk
; (jt_vwrite). Interrupts are off while the VRAM copy is in slots 4-5, then as they were; this
; page's own stack (wf_stk) is used while the copy is mapped. A whole tile (32 bytes from a tile's
; start) is compared with the copy first, and copied and marked only when a byte differs: a tile
; with no dirty_pages mark already has its Next tile definition made from the bytes in the copy,
; so the conversion and the sprite pattern upload of an unchanged tile are skipped. Part tiles,
; and every tile of a write that wraps past $3FFF, are copied and marked.
; Changes every register but IX, IY and the alternates. Runtime internals: SHADOW_PAGE 28, 29 (the
; VRAM copy), region_tab $E400 (0: a tile page), dirty_pages $E440, tiles_dirty $E082, tw_cnt
; $E083, vw_tw $F9E6 (its CALL target at $F9E7), vw_stack_top $E0FC (the stack for that call).
WF_SHADOW equ 28
WF_REGION equ $E400
WF_DIRTY  equ $E440
WF_TDIRTY equ $E082
WF_TWCNT  equ $E083
WF_VWTW   equ $F9E6
WF_VWSTK  equ $E0FC
wfast:  ld (wf_n),hl
        ld (wf_src),de
        ld de,(vdp_addr)
        ld a,d
        and $3F
        ld d,a
        ld (wf_va),de
        dec hl
        add hl,de
        ld a,h
        and $3F
        ld c,a                  ; the last byte's VRAM page
        ld b,d                  ; the first
.chk:   ld l,b
        ld h,WF_REGION>>8
        ld a,(hl)
        or a
        jr nz,.slow             ; not tile data
        ld a,b
        cp c
        jr z,.fast
        inc b
        res 6,b
        jr .chk
.slow:  ld hl,(wf_n)
        ld de,(wf_src)
        ld a,1
        jp wchunk
.fast:  xor a
        ld (wf_one),a
        ld a,i
        ld a,0
        jp po,.di
        inc a
.di:    ld (wf_ei),a
        di
        nextreg $54,WF_SHADOW
        nextreg $55,WF_SHADOW+1
        ld hl,$4000
        ld de,(wf_va)
        or a
        sbc hl,de               ; bytes up to the end of VRAM
        ld de,(wf_n)
        or a
        sbc hl,de
        jr nc,.one              ; no wrap
        ld (wf_rest),hl         ; minus the bytes after the wrap
        ld hl,$4000
        ld de,(wf_va)
        or a
        sbc hl,de
        ld b,h
        ld c,l
        ld hl,(wf_src)
        set 7,d
        ldir
        ld de,(wf_rest)
        push hl
        ld hl,0
        or a
        sbc hl,de
        ld b,h
        ld c,l
        pop hl
        ld de,$8000
        ldir
        jp .copied
.one:   ld (wf_sp2),sp
        ld sp,wf_stk            ; this page's own stack while the copy is in slots 4-5
        ld hl,(wf_src)
        ld de,(wf_va)
        set 7,d                 ; the copy at $8000 + VRAM address
        ld bc,(wf_n)
        ld (wf_left),bc
        ld a,1
        ld (wf_one),a
        xor a
        ld (wf_any),a
.seg:   ld bc,(wf_left)         ; tile by tile: a whole tile is copied and marked only when one of
        ld a,b                  ; its bytes differs from the copy (the Next's tile is then not
        or c                    ; converted again for bytes it already shows); a part tile always
        jp z,.segd
        ld a,e
        and 31
        jr nz,.part
        ld a,b
        or a
        jr nz,.whole
        ld a,c
        cp 32
        jr nc,.whole
.part:  ld a,e                  ; bytes to the tile's end (1 to 32), or fewer when fewer are left
        and 31
        neg
        add a,32
        inc b
        dec b
        jr nz,.pc
        cp c
        jr c,.pc
        ld a,c
.pc:    call .tmark
        ld c,a
        ld b,0
        push hl
        ld hl,(wf_left)
        or a
        sbc hl,bc
        ld (wf_left),hl
        pop hl
        ldir
        jr .seg
.whole: push de
        push hl
        ld b,32
.cmp:   ld a,(de)
        cp (hl)
        jr nz,.ne
        inc hl
        inc e
        djnz .cmp
        pop af                  ; the same 32 bytes: HL is past them, DE moves on 32
        pop de
        ex de,hl
        ld bc,32
        add hl,bc
        ex de,hl
        jr .wl
.ne:    pop hl
        pop de
        call .tmark
        ld bc,32
        ldir
.wl:    push hl
        ld hl,(wf_left)
        ld bc,32
        or a
        sbc hl,bc
        ld (wf_left),hl
        pop hl
        jr .seg
.tmark: push af                 ; the dirty_pages bit of the tile at DE ($8000 + VRAM address)
        push hl
        push bc
        ld a,e
        rlca
        rlca
        rlca
        and 7
        ld c,a
        ld b,0
        ld hl,wf_bits
        add hl,bc
        ld c,(hl)
        ld a,d
        and $3F
        add a,WF_DIRTY & $FF
        ld l,a
        ld h,WF_DIRTY >> 8
        ld a,(hl)
        or c
        ld (hl),a
        ld a,1
        ld (wf_any),a
        pop bc
        pop hl
        pop af
        ret
.segd:  ld sp,(wf_sp2)
.copied:
        dec hl
        ld a,(hl)
        ld (vdp_rbuf),a
        ld bc,$243B             ; the game's pages back in slots 4-5 (interrupts are off)
        ld a,$54
        out (c),a
        inc b
        ld a,(cur_mmu+4)
        out (c),a
        dec b
        ld a,$55
        out (c),a
        inc b
        ld a,(cur_mmu+5)
        out (c),a
        ld hl,(wf_va)
        ld de,(wf_n)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (vdp_addr),hl        ; the VDP address after the last byte
        ld a,(wf_one)
        or a
        jr z,.markall
        ld a,(wf_any)           ; marked tile by tile above
        or a
        jr z,.marked
        jr .tdirty
.markall:
        ld hl,(wf_va)           ; tiles to mark: (address mod 32 + n + 31) / 32
        ld a,l
        and 31
        ld e,a
        ld d,0
        ld hl,(wf_n)
        add hl,de
        ld de,31
        add hl,de
        add hl,hl
        add hl,hl
        add hl,hl
        ld b,h
        ld hl,(wf_va)           ; HL = the first tile, address / 32
        ld a,l
        rlca
        rlca
        rlca
        and 7
        ld l,a
        ld a,h
        add a,a
        add a,a
        add a,a
        or l
        ld l,a
        ld a,h
        rlca
        rlca
        rlca
        and 1
        ld h,a
.mark:  ld a,l                  ; dirty_pages + tile / 8 gets the tile's bit
        and 7
        add a,wf_bits & $FF
        ld e,a
        ld a,0
        adc a,wf_bits >> 8
        ld d,a
        ld a,(de)
        ld c,a
        ld a,h
        rrca
        rrca
        rrca                    ; tile bit 8 as page bit 5
        ld e,a
        ld a,l
        rrca
        rrca
        rrca
        and $1F
        or e
        add a,WF_DIRTY & $FF
        ld e,a
        ld d,WF_DIRTY >> 8
        ld a,(de)
        or c
        ld (de),a
        inc hl
        res 1,h                 ; tiles wrap at 512
        djnz .mark
.tdirty:
        ld a,1
        ld (WF_TDIRTY),a
.marked:
        ld hl,(WF_TWCNT)
        ld de,(wf_n)
        add hl,de
        ld (WF_TWCNT),hl
        xor a
        ld (vdp_latch),a
        inc a
        ld (vdp_code),a
        ld (wf_sp),sp
        ld sp,WF_VWSTK          ; jt_vwrite's own stack, free while it does not run
        ld hl,(WF_VWTW+1)
        call .jphl              ; tw_check, or vbl_chkv
        ld sp,(wf_sp)
        ld a,(wf_ei)
        or a
        ret z
        ei
        ret
.jphl:  jp (hl)
wf_bits: db $01,$02,$04,$08,$10,$20,$40,$80
wf_rest: dw 0
wf_sp:  dw 0
wf_n:   dw 0
wf_src: dw 0
wf_va:  dw 0
wf_ei:  db 0
wf_one: db 0
wf_any: db 0
wf_left: dw 0
wf_sp2: dw 0
        ds 16                   ; wfast's stack while the VRAM copy is mapped
wf_stk:
cnt4:   db 0
left:   db 0
lastb:  db 0
lastm:  db 0
lastd:  db 0
lastp:  db 0
sv_b:   dw 0
sv_bc:  dw 0
sv_de:  dw 0
sv_hl:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
sv_end: dw 0
wleft:  dw 0
wflag:  db 0
sv_de0: dw 0
sv_g4:  dw 0
sv_n:   dw 0
buf:    ds 1024
endpage
# Fighter tile renderer $2A62, the other forms, and the name table row writer $3D85 (bank 0). Each
# loop sent its bytes one runtime call per OUT or OUTI, or one per 4 bytes. Code caves call page 4
# entries (and, for $2F0E, $3217 and $32D0, the page 3 entry cp4) that make the same bytes and write
# them with wfast (jt_vwrite for anything but tile data).
#   $2D3C: 8 mirrored groups (mask and data through the table at $0A00, background from the other
#          register set), B kept                                         -> mskf8
#   $2F49, $2FA9: the same, B groups                                     -> mskf
#   $3069, $3107, $3142: B groups of 4 bytes from HL                     -> cp
#   $31C5, $3305: the same, DE stepped with HL                           -> cpde
#   $2BA9, $3032, $325F: B groups of 4 bytes, each through the table at D -> xl
#   $2F0E, $3217, $32D0: as $2C4E                                        -> cp4 (page 3)
#   $3DDE, $3E00: OUTI : DEC D (or E) : JR NZ                            -> outd, oute
asm 02D3C 384        ; 8 x (LD A,(DE) : LD L,A : LD C,(HL) : INC DE : 4 x (LD A,(DE) : LD L,A : LD A,C : EXX : AND (HL) : INC HL : EXX : OR (HL) : OUT ($BE),A : INC DE))
    rst $00
    db far_io, pg_mskf8, ent_mskf8
endasm
asm 02F49 50         ; the same group : DJNZ $2F49
    rst $00
    db far_io, pg_mskf, ent_mskf
endasm
asm 02FA9 50         ; the same group : DJNZ $2FA9
    rst $00
    db far_io, pg_mskf, ent_mskf
endasm
asm 03069 24         ; 4 x (LD A,(HL) : OUT ($BE),A : INC HL), NOPs : DJNZ $3069
    rst $00
    db far_io, pg_cp, ent_cp
endasm
asm 03107 26         ; 4 x (LD A,(HL) : OUT ($BE),A : NOP : NOP : INC HL) : DJNZ $3107
    rst $00
    db far_io, pg_cp, ent_cp
endasm
asm 03142 25         ; 4 x (LD A,(HL) : OUT ($BE),A : INC HL), NOPs and a LD A,(DE) : DJNZ $3142
    rst $00
    db far_io, pg_cp, ent_cp
endasm
asm 031C5 22         ; 4 x (LD A,(HL) : OUT ($BE),A : INC DE : INC HL) : DJNZ $31C5
    rst $00
    db far_io, pg_cpde, ent_cpde
endasm
asm 03305 22         ; 4 x (LD A,(HL) : OUT ($BE),A : INC DE : INC HL) : DJNZ $3305
    rst $00
    db far_io, pg_cpde, ent_cpde
endasm
asm 02BA9 30         ; 4 x (LD E,(HL) : LD A,(DE) : NOP : NOP : OUT ($BE),A : INC HL) : DJNZ $2BA9
    rst $00
    db far_io, pg_xl, ent_xl
endasm
asm 03032 22         ; 4 x (LD E,(HL) : LD A,(DE) : OUT ($BE),A : INC HL) : DJNZ $3032
    rst $00
    db far_io, pg_xl, ent_xl
endasm
asm 0325F 30         ; 4 x (LD E,(HL) : LD A,(DE) : NOP : NOP : OUT ($BE),A : INC HL) : DJNZ $325F
    rst $00
    db far_io, pg_xl, ent_xl
endasm
asm 02F0E 20         ; 4 x (OUTI : JR $+2 : INC B) : DEC A : JR NZ,$2F0E
    rst $00
    db far_io, pg_cp4, ent_cp4
endasm
asm 03217 20         ; 4 x (OUTI : JR $+2 : INC B) : DEC A : JR NZ,$3217
    rst $00
    db far_io, pg_cp4, ent_cp4
endasm
asm 032D0 20         ; 4 x (OUTI : JR $+2 : INC B) : DEC A : JR NZ,$32D0
    rst $00
    db far_io, pg_cp4, ent_cp4
endasm
asm 03DDE 5          ; OUTI : DEC D : JR NZ,$3DDE
    rst $00
    db far_io, pg_outd, ent_outd
endasm
asm 03E00 5          ; OUTI : DEC E : JR NZ,$3E00
    rst $00
    db far_io, pg_oute, ent_oute
endasm
page 4 mskf8 mskf cp cpde xl outd oute
    OPT --zxnext        ; NEXTREG
; Each entry returns as the game's loop leaves the registers, and writes its bytes at the VDP address
; with wfast. The game's interrupts stay as they are (its handler does not touch the VDP or
; $FFFD); the only stack used is the calls of jt_vwrite and jt_peek, and cp, cpde and xl keep F
; on the stack, as the game's loops leave F as it was.
; mskf8, mskf: the mirrored masked rows. The other register set (X) is the one active at the site:
; DE the sprite bytes, H the table page ($0A); the main set (Y) holds HL, the background rows. A
; group is c = T(DE), then 4 bytes (c AND (HL')) OR T(DE+1..4), T(n) the byte at H*256+n. They
; return X with DE 5 a group further on, L the last sprite byte, C the last c, A the last byte and F
; as its OR left it, and Y with HL 4 a group further on. mskf8 does 8 groups and keeps B; mskf does
; B groups (0 = 256) and returns B = 0.
; cp: B groups (0 = 256) of 4 bytes from HL; cpde also steps DE with HL. A = the last byte, B = 0.
; xl: B groups of 4 bytes, each E = (HL), A = (DE); returns E and A of the last byte, B = 0.
; outd, oute: D (or E) bytes from HL (0 = 256), as OUTI : DEC r : JR NZ; returns that register 0
; with Z and N set and C kept, B less the count, HL past the bytes, A kept.
    macro RDHL              ; A = the byte the game sees at HL
        ld a,h
        and $E0
        cp $20
        jr nz,.direct
        call jt_peek
        jr .done
.direct:
        ld a,(hl)
.done:
    endm
mskf8:  ld (xbc),bc
        ld a,1
        ld (keepb),a
        ld b,8
        jr mskf_go
mskf:   ld (xbc),bc
        xor a
        ld (keepb),a
mskf_go:
        ld (xde),de
        ld a,h
        ld (tblh),a
        exx
        ld (ybc),bc
        ld (yde),de
        ld (bg),hl
        exx
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld a,h                  ; fast path: the table, the background and the sprite bytes all
        and $E0                 ; avoid this page's slot ($2000-$3FFF), so they are read straight
        cp $20
        jp z,.slow
        ld a,b
        ld l,a
        ld h,0
        or a
        jr nz,.g1
        inc h                   ; 0 = 256 groups
.g1:    ld (grps),hl
        add hl,hl
        add hl,hl
        ld (span4),hl
        ex de,hl                ; DE = 4 bytes a group
        ld hl,(bg)
        call srcok
        jp nz,.slow
        ld hl,(grps)
        ld de,(span4)
        add hl,de
        ex de,hl                ; DE = 5 bytes a group
        ld hl,(xde)
        call srcok
        jp nz,.slow
        ld de,(xde)             ; X: DE the sprite bytes, H the table, B the groups
        ld a,(tblh)
        ld h,a
        exx
        ld hl,(bg)              ; Y: HL the background rows, DE the buffer
        ld de,buf
        exx
.fg:    ld a,(de)               ; the game's group, with the OUT as a store into buf
        inc de
        ld l,a
        ld c,(hl)
        rept 4
        ld a,(de)
        ld l,a
        ld a,c
        exx
        and (hl)
        inc hl
        exx
        or (hl)
        exx
        ld (de),a
        inc de
        exx
        inc de
        endr
        djnz .fg
        push af                 ; A and F as the game's last OR leaves them
        exx
        pop bc
        ld (sv_af),bc
        ld (bg),hl
        ld (fl_end),de
        exx
        ld (xde),de
        ld a,l
        ld (lastd),a
        ld a,c
        ld (lastc),a
        ld ix,(fl_end)
        call flush
        exx
        ld hl,(bg)
        ld de,(yde)
        ld bc,(ybc)
        exx
        ld de,(xde)
        ld a,(tblh)
        ld h,a
        ld a,(lastd)
        ld l,a
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld bc,(sv_af)
        push bc
        ld bc,(xbc)             ; mskf8 keeps B, mskf returns B = 0
        ld a,(keepb)
        or a
        jr nz,.fkb
        ld b,0
.fkb:   ld a,(lastc)
        ld c,a
        pop af
        ret
.slow:  ld ix,buf
.grp:   ex de,hl                ; HL = the sprite bytes
        RDHL
        inc hl
        ex de,hl
        call tlook
        ld (lastc),a
        ld c,a
        ld a,4
        ld (left),a
.row:   ex de,hl
        RDHL
        inc hl
        ex de,hl
        ld (lastd),a
        call tlook
        ld (lastf),a
        ld hl,(bg)
        RDHL
        inc hl
        ld (bg),hl
        ld (lastb),a
        and c
        ld hl,lastf
        or (hl)
        ld (ix+0),a
        inc ix
        ld a,(left)
        dec a
        ld (left),a
        jr nz,.row
        djnz .grp
        ld (xde),de
        call flush
        exx
        ld hl,(bg)
        ld de,(yde)
        ld bc,(ybc)
        exx
        ld de,(xde)
        ld a,(tblh)
        ld h,a
        ld a,(lastd)
        ld l,a
        ld bc,(xbc)             ; mskf8 keeps B, mskf returns B = 0
        ld a,(keepb)
        or a
        jr nz,.kb
        ld b,0
.kb:    ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld a,(lastc)
        ld c,a
        ld a,(lastf)
        ld (.or+1),a
        ld a,(lastb)
        and c
.or:    or 0
        ret
; srcok: Z when the DE bytes (1 to 1280) from HL avoid $2000-$3FFF, where this page sits in place
; of the game's bank 0, and do not wrap past $FFFF; NZ else. Keeps BC, DE and HL.
srcok:  push hl
        add hl,de
        jr c,.bad               ; past $FFFF
        dec hl                  ; the last byte
        ld a,h
        cp $20
        jr c,.ok                ; ends below $2000
        pop hl
        push hl
        ld a,h
        cp $40
        jr nc,.ok               ; starts at $4000 or above
.bad:   pop hl
        or 1
        ret
.ok:    pop hl
        xor a
        ret
; tlook: A = T(A), the byte at (tblh)*256 + A; keeps the other registers but F.
tlook:  ld (.t+1),a
        ld a,(tblh)
        ld (.t+2),a
.t:     ld a,($0000)
        ret
cp:     push af
        ld (sv_de),de
        ld de,0
        jr cpgo
cpde:   push af
        ld (sv_de),de
        ld de,1
cpgo:   ld (destep),de
        ld (sv_bc),bc
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld ix,buf
        ld c,b                  ; groups
        push hl                 ; fast path: the source avoids this page's slot, copied straight
        ld a,b
        ld l,a
        ld h,0
        or a
        jr nz,.n1
        inc h                   ; 0 = 256 groups
.n1:    add hl,hl
        add hl,hl
        ld (cp_n),hl
        ex de,hl
        pop hl
        call srcok
        jr nz,.grp
        ld a,(destep)
        or a
        jr z,.nd
        push hl                 ; cpde: DE steps with HL
        ld hl,(sv_de)
        ld de,(cp_n)
        add hl,de
        ld (sv_de),hl
        pop hl
.nd:    ld de,buf
        ld bc,(cp_n)
        ldir
        push de
        pop ix
        jr .fl
.grp:   ld b,4
.byte:  RDHL
        ld (ix+0),a
        inc ix
        inc hl
        ld de,(sv_de)
        push hl
        ld hl,(destep)
        add hl,de
        ld (sv_de),hl
        pop hl
        djnz .byte
        dec c
        jr nz,.grp
.fl:    call flush
        ld de,(sv_de)
        ld bc,(sv_bc)
        ld b,0
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        pop af
        ld a,(lastw)
        ret
xl:     push af
        ld (sv_bc),bc
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld ix,buf
        ld c,b
.grp:   ld b,4
.byte:  RDHL
        ld e,a
        inc hl
        push hl
        ex de,hl
        RDHL
        ex de,hl
        pop hl
        ld (ix+0),a
        inc ix
        djnz .byte
        dec c
        jr nz,.grp
        ld a,e
        ld (laste),a
        call flush
        ld a,(laste)
        ld e,a
        ld bc,(sv_bc)
        ld b,0
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        pop af
        ld a,(lastw)
        ret
outd:   push af
        ex (sp),hl
        ld (sv_af),hl
        ex (sp),hl
        pop af
        ld (sv_bc),bc
        ld a,d
        ld d,0
        jr outgo
oute:   push af
        ex (sp),hl
        ld (sv_af),hl
        ex (sp),hl
        pop af
        ld (sv_bc),bc
        ld a,e
        ld e,0
outgo:  ld (sv_de),de
        ld (cnt),a
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld (sv_hl),hl
        ld b,a
        call ntfast             ; name table rows: written here
        jr z,.done
        ld hl,(sv_hl)
        ld a,(cnt)
        ld b,a                  ; one run of the count (0 = 256)
        ld c,1
        ld de,(vdp_addr)
        ld ix,0
        ld iy,0
        xor a                   ; the source as the game sees it
        call jt_vwrite
.done:  ld hl,(sv_hl)
        ld a,(cnt)
        ld e,a
        ld d,0
        or a
        jr nz,.n
        inc d
.n:     add hl,de
        ld bc,(sv_bc)
        ld a,b
        sub e
        ld b,a                  ; B less the count (mod 256)
        ld de,(sv_de)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld a,(sv_af)            ; F: Z and N set, C kept, as DEC r to 0 leaves it; A kept
        and 1
        or $42
        ld (sv_af),a
        push hl
        ld hl,(sv_af)
        ex (sp),hl
        pop af
        ret
; ntfast: the fighter's name table rows that the row writer $3D85 sends with outd and oute. When the
; B bytes (0 = 256) from HL land in name table rows 0-23 (the table at $3800, VDP code 1) and the
; source lies in $6000-$FFFF, they are written here as jt_vwrite's name table path (vw_ntmap, as
; nt_put) leaves them: into the VRAM copy, then each cell they touch into both Next tilemaps, M0
; (row r, column c at r * 80 + 2c, SMS columns 0-7 again in columns 32-39) and A8 (M0 + $0A00 - 16
; for columns 8-31; columns 0-7 at M0 + $0A00 + 48 and + 64), the tile byte and the attribute that
; mapattr_table gives for the high byte; then the VDP address after the last byte, the latch clear
; and the read buffer. The maps change at once, as through jt_vwrite.
; Priority is off (no Layer 2 marks). Z when done; NZ and nothing written otherwise. Interrupts
; are off while slots 0 and 2 hold the map and the copy, on this page's stack (wf_stk). Runtime
; internals: SHADOW_PAGE+1 29 (VRAM $2000-$3FFF), MAP_PAGE 14, mapattr_table $E200, nt_base $E04B,
; cur_mmu, vdp_code, vdp_addr, vdp_latch, vdp_rbuf.
NF_SHADOW equ 29
NF_MAP    equ 14
NF_ATTR   equ $E200
NF_NTB    equ $E04B
ntfast: ld a,(vdp_code)
        cp 1
        ret nz
        ld de,(NF_NTB)
        ld a,e
        or a
        ret nz
        ld a,d
        cp $38
        ret nz
        ld e,b                  ; DE = the bytes, 1 to 256
        ld d,0
        ld a,b
        or a
        jr nz,.n1
        inc d
.n1:    ld (nf_n),de
        push hl                 ; the source: $6000 up to $FFFF, no wrap
        add hl,de
        pop hl
        jr nc,.s1
        or 1                    ; past $FFFF
        ret
.s1:    ld a,h
        cp $60
        jr nc,.s2
        or 1
        ret
.s2:    ld (nf_src),hl
        ld hl,(vdp_addr)
        ld a,h
        and $3F
        ld h,a
        ld (nf_va),hl
        ld a,h
        cp $38
        jr nc,.v1
        or 1
        ret
.v1:    add hl,de
        dec hl                  ; the last byte
        ld a,h
        cp $3E
        jr c,.go
        or 1
        ret
.go:    ld a,i
        ld a,0
        jp po,.di
        inc a
.di:    ld (nf_ei),a
        di
        ld (nf_sp),sp
        ld sp,wf_stk
        nextreg $50,NF_MAP
        nextreg $52,NF_SHADOW
        ld hl,(nf_va)
        ld de,$2000
        add hl,de
        ex de,hl                ; DE = the copy ($4000 + VRAM address - $2000)
        ld hl,(nf_src)
        ld bc,(nf_n)
        ldir
        dec hl
        ld a,(hl)
        ld (vdp_rbuf),a
        ld hl,(nf_va)           ; cells: (va - $3800) / 2 to (va + n - 1 - $3800) / 2
        ld de,(nf_n)
        add hl,de
        dec hl
        ld de,$3800
        or a
        sbc hl,de
        srl h
        rr l
        ld (nf_k1),hl
        ld hl,(nf_va)
        or a
        sbc hl,de
        srl h
        rr l
.cell:  ld (nf_k),hl
        add hl,hl
        ld de,$5800
        add hl,de               ; the cell in the copy
        ld c,(hl)               ; C = the tile byte
        inc hl
        ld e,(hl)
        ld d,NF_ATTR >> 8
        ld a,(de)
        ld b,a                  ; B = the attribute
        ld hl,(nf_k)
        ld a,l
        and 31
        ld (nf_col),a
        add hl,hl
        add hl,hl
        add hl,hl               ; H = row
        ld d,h
        ld e,80
        mul d,e
        ld a,(nf_col)
        add a,a
        add a,e
        ld l,a
        ld a,d
        adc a,0
        ld h,a                  ; HL = the cell in M0
        ld (hl),c
        inc hl
        ld (hl),b
        dec hl
        ld a,(nf_col)
        cp 8
        jr nc,.hi
        push hl
        ld de,64                ; M0 columns 32-39
        add hl,de
        ld (hl),c
        inc hl
        ld (hl),b
        pop hl
        ld de,$0A00+48          ; A8 columns 24-31
        add hl,de
        ld (hl),c
        inc hl
        ld (hl),b
        ld de,15                ; A8 columns 32-39
        add hl,de
        ld (hl),c
        inc hl
        ld (hl),b
        jr .nx
.hi:    ld de,$0A00-16          ; A8 column = SMS column - 8
        add hl,de
        ld (hl),c
        inc hl
        ld (hl),b
.nx:    ld hl,(nf_k)
        ld de,(nf_k1)
        or a
        sbc hl,de
        add hl,de
        inc hl
        jp nz,.cell
        ld a,(cur_mmu+0)
        nextreg $50,a
        ld a,(cur_mmu+2)
        nextreg $52,a
        ld sp,(nf_sp)
        ld hl,(nf_va)
        ld de,(nf_n)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (vdp_addr),hl
        xor a
        ld (vdp_latch),a
        ld a,(nf_ei)
        or a
        jr z,.z
        ei
.z:     xor a
        ret
nf_n:   dw 0
nf_src: dw 0
nf_va:  dw 0
nf_k:   dw 0
nf_k1:  dw 0
nf_sp:  dw 0
nf_col: db 0
nf_ei:  db 0
; flush: write buf up to IX at the VDP address (wfast); keeps HL and DE; sets lastw.
flush:  ld (fl_hl),hl
        ld (fl_de),de
        ld a,(ix-1)
        ld (lastw),a
        ld (fl_end),ix
        ld hl,(fl_end)
        ld de,buf
        or a
        sbc hl,de               ; bytes, 1 to 1024
        call wfast
        ld hl,(fl_hl)
        ld de,(fl_de)
        ret
; wchunk: HL bytes (1 to 1024) from DE at the VDP address, in runs of up to 256 bytes.
wchunk: ld (wflag),a
.next:  ld a,h
        or l
        ret z
        ld c,l
        ld a,h
        or a
        jr z,.last
        dec h
        ld c,0
        jr .go
.last:  ld hl,0
.go:    ld (wleft),hl
        ex de,hl
        ld de,(vdp_addr)
        ld b,c
        ld c,1
        ld ix,0
        ld iy,0
        ld a,(wflag)
        call jt_vwrite
        ld c,b
        ld a,c
        or a
        jr nz,.add
        inc h
        jr .st
.add:   add a,l
        ld l,a
        jr nc,.st
        inc h
.st:    ex de,hl
        ld hl,(wleft)
        jr .next
wflag:  db 0
wleft:  dw 0
; wfast: HL bytes (1 to 1024) from DE in this page, written at the VDP address as the game's data
; writes would leave VRAM and the VDP state. When every byte lands in tile data, it does the work
; of jt_vwrite's tile path itself: the VRAM copy, the tiles' dirty_pages marks, tiles_dirty and
; tw_cnt, the VDP address, code, latch and read buffer, then the call jt_vwrite's end makes (vw_tw:
; tw_check, or vbl_chkv while the frame work check is armed). Else it goes through wchunk
; (jt_vwrite). Interrupts are off while the VRAM copy is in slots 4-5, then as they were; this
; page's own stack (wf_stk) is used while the copy is mapped. A whole tile (32 bytes from a tile's
; start) is compared with the copy first, and copied and marked only when a byte differs: a tile
; with no dirty_pages mark already has its Next tile definition made from the bytes in the copy,
; so the conversion and the sprite pattern upload of an unchanged tile are skipped. Part tiles,
; and every tile of a write that wraps past $3FFF, are copied and marked.
; Changes every register but IX, IY and the alternates. Runtime internals: SHADOW_PAGE 28, 29 (the
; VRAM copy), region_tab $E400 (0: a tile page), dirty_pages $E440, tiles_dirty $E082, tw_cnt
; $E083, vw_tw $F9E6 (its CALL target at $F9E7), vw_stack_top $E0FC (the stack for that call).
WF_SHADOW equ 28
WF_REGION equ $E400
WF_DIRTY  equ $E440
WF_TDIRTY equ $E082
WF_TWCNT  equ $E083
WF_VWTW   equ $F9E6
WF_VWSTK  equ $E0FC
wfast:  ld (wf_n),hl
        ld (wf_src),de
        ld de,(vdp_addr)
        ld a,d
        and $3F
        ld d,a
        ld (wf_va),de
        dec hl
        add hl,de
        ld a,h
        and $3F
        ld c,a                  ; the last byte's VRAM page
        ld b,d                  ; the first
.chk:   ld l,b
        ld h,WF_REGION>>8
        ld a,(hl)
        or a
        jr nz,.slow             ; not tile data
        ld a,b
        cp c
        jr z,.fast
        inc b
        res 6,b
        jr .chk
.slow:  ld hl,(wf_n)
        ld de,(wf_src)
        ld a,1
        jp wchunk
.fast:  xor a
        ld (wf_one),a
        ld a,i
        ld a,0
        jp po,.di
        inc a
.di:    ld (wf_ei),a
        di
        nextreg $54,WF_SHADOW
        nextreg $55,WF_SHADOW+1
        ld hl,$4000
        ld de,(wf_va)
        or a
        sbc hl,de               ; bytes up to the end of VRAM
        ld de,(wf_n)
        or a
        sbc hl,de
        jr nc,.one              ; no wrap
        ld (wf_rest),hl         ; minus the bytes after the wrap
        ld hl,$4000
        ld de,(wf_va)
        or a
        sbc hl,de
        ld b,h
        ld c,l
        ld hl,(wf_src)
        set 7,d
        ldir
        ld de,(wf_rest)
        push hl
        ld hl,0
        or a
        sbc hl,de
        ld b,h
        ld c,l
        pop hl
        ld de,$8000
        ldir
        jp .copied
.one:   ld (wf_sp2),sp
        ld sp,wf_stk            ; this page's own stack while the copy is in slots 4-5
        ld hl,(wf_src)
        ld de,(wf_va)
        set 7,d                 ; the copy at $8000 + VRAM address
        ld bc,(wf_n)
        ld (wf_left),bc
        ld a,1
        ld (wf_one),a
        xor a
        ld (wf_any),a
.seg:   ld bc,(wf_left)         ; tile by tile: a whole tile is copied and marked only when one of
        ld a,b                  ; its bytes differs from the copy (the Next's tile is then not
        or c                    ; converted again for bytes it already shows); a part tile always
        jp z,.segd
        ld a,e
        and 31
        jr nz,.part
        ld a,b
        or a
        jr nz,.whole
        ld a,c
        cp 32
        jr nc,.whole
.part:  ld a,e                  ; bytes to the tile's end (1 to 32), or fewer when fewer are left
        and 31
        neg
        add a,32
        inc b
        dec b
        jr nz,.pc
        cp c
        jr c,.pc
        ld a,c
.pc:    call .tmark
        ld c,a
        ld b,0
        push hl
        ld hl,(wf_left)
        or a
        sbc hl,bc
        ld (wf_left),hl
        pop hl
        ldir
        jr .seg
.whole: push de
        push hl
        ld b,32
.cmp:   ld a,(de)
        cp (hl)
        jr nz,.ne
        inc hl
        inc e
        djnz .cmp
        pop af                  ; the same 32 bytes: HL is past them, DE moves on 32
        pop de
        ex de,hl
        ld bc,32
        add hl,bc
        ex de,hl
        jr .wl
.ne:    pop hl
        pop de
        call .tmark
        ld bc,32
        ldir
.wl:    push hl
        ld hl,(wf_left)
        ld bc,32
        or a
        sbc hl,bc
        ld (wf_left),hl
        pop hl
        jr .seg
.tmark: push af                 ; the dirty_pages bit of the tile at DE ($8000 + VRAM address)
        push hl
        push bc
        ld a,e
        rlca
        rlca
        rlca
        and 7
        ld c,a
        ld b,0
        ld hl,wf_bits
        add hl,bc
        ld c,(hl)
        ld a,d
        and $3F
        add a,WF_DIRTY & $FF
        ld l,a
        ld h,WF_DIRTY >> 8
        ld a,(hl)
        or c
        ld (hl),a
        ld a,1
        ld (wf_any),a
        pop bc
        pop hl
        pop af
        ret
.segd:  ld sp,(wf_sp2)
.copied:
        dec hl
        ld a,(hl)
        ld (vdp_rbuf),a
        ld bc,$243B             ; the game's pages back in slots 4-5 (interrupts are off)
        ld a,$54
        out (c),a
        inc b
        ld a,(cur_mmu+4)
        out (c),a
        dec b
        ld a,$55
        out (c),a
        inc b
        ld a,(cur_mmu+5)
        out (c),a
        ld hl,(wf_va)
        ld de,(wf_n)
        add hl,de
        ld a,h
        and $3F
        ld h,a
        ld (vdp_addr),hl        ; the VDP address after the last byte
        ld a,(wf_one)
        or a
        jr z,.markall
        ld a,(wf_any)           ; marked tile by tile above
        or a
        jr z,.marked
        jr .tdirty
.markall:
        ld hl,(wf_va)           ; tiles to mark: (address mod 32 + n + 31) / 32
        ld a,l
        and 31
        ld e,a
        ld d,0
        ld hl,(wf_n)
        add hl,de
        ld de,31
        add hl,de
        add hl,hl
        add hl,hl
        add hl,hl
        ld b,h
        ld hl,(wf_va)           ; HL = the first tile, address / 32
        ld a,l
        rlca
        rlca
        rlca
        and 7
        ld l,a
        ld a,h
        add a,a
        add a,a
        add a,a
        or l
        ld l,a
        ld a,h
        rlca
        rlca
        rlca
        and 1
        ld h,a
.mark:  ld a,l                  ; dirty_pages + tile / 8 gets the tile's bit
        and 7
        add a,wf_bits & $FF
        ld e,a
        ld a,0
        adc a,wf_bits >> 8
        ld d,a
        ld a,(de)
        ld c,a
        ld a,h
        rrca
        rrca
        rrca                    ; tile bit 8 as page bit 5
        ld e,a
        ld a,l
        rrca
        rrca
        rrca
        and $1F
        or e
        add a,WF_DIRTY & $FF
        ld e,a
        ld d,WF_DIRTY >> 8
        ld a,(de)
        or c
        ld (de),a
        inc hl
        res 1,h                 ; tiles wrap at 512
        djnz .mark
.tdirty:
        ld a,1
        ld (WF_TDIRTY),a
.marked:
        ld hl,(WF_TWCNT)
        ld de,(wf_n)
        add hl,de
        ld (WF_TWCNT),hl
        xor a
        ld (vdp_latch),a
        inc a
        ld (vdp_code),a
        ld (wf_sp),sp
        ld sp,WF_VWSTK          ; jt_vwrite's own stack, free while it does not run
        ld hl,(WF_VWTW+1)
        call .jphl              ; tw_check, or vbl_chkv
        ld sp,(wf_sp)
        ld a,(wf_ei)
        or a
        ret z
        ei
        ret
.jphl:  jp (hl)
wf_bits: db $01,$02,$04,$08,$10,$20,$40,$80
wf_rest: dw 0
wf_sp:  dw 0
wf_n:   dw 0
wf_src: dw 0
wf_va:  dw 0
wf_ei:  db 0
wf_one: db 0
wf_any: db 0
wf_left: dw 0
wf_sp2: dw 0
        ds 16                   ; wfast's stack while the VRAM copy is mapped
wf_stk:
xbc:    dw 0
xde:    dw 0
keepb:  db 0
ybc:    dw 0
yde:    dw 0
bg:     dw 0
tblh:   db 0
lastc:  db 0
lastd:  db 0
lastf:  db 0
lastb:  db 0
laste:  db 0
lastw:  db 0
left:   db 0
cnt:    db 0
destep: dw 0
sv_bc:  dw 0
sv_de:  dw 0
sv_hl:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
fl_hl:  dw 0
fl_de:  dw 0
fl_end: dw 0
fl_left: dw 0
cp_n:   dw 0
grps:   dw 0
span4:  dw 0
sv_af:  dw 0
buf:    ds 1024
endpage
# Frame wait $3FC6 (bank 0): after the frame interrupt sets its flag it reads the V counter at $3FDA
# (IN A,($7E) : DI : RET). On the Next that read, just after the frame event, ran the runtime's
# frame work (rd_vcount: a read in the vertical blank with the work not yet done), and the game then
# wrote its sprite table ($40CA) after the sprite update: the new poses showed one frame later than
# on a Master System. The cave makes the read with vbl_done set, so it returns the same count and
# the work runs at the ULA interrupt (line 248, or 224 at 60 Hz), after the sprite table is written.
asm 03FDA 4          ; IN A,($7E) : DI : RET
    rst $00
    db far_io, pg_vread, ent_vread
endasm
page 0 delay vread
; delay: as the game's $40BF-$40C4, in real time. HL passes of 26 T-states (0 means 65536).
; Returns as the game's loop does: HL = 0, A = 0, flags as OR H with A = 0 (Z, P/V set; S, H, N, C
; clear); BC and DE kept. The interrupt state stays as it was, so the game's frame interrupt runs
; during the wait as during the game's loop; each line read runs with interrupts off, so a handler
; cannot change the NextReg select port between the select and the read. The entry uses no stack of
; its own (the game's interrupts can come while it runs, and they need the game's stack).
    macro RDLINE        ; HL = the Next's raster line, below (dlen); A, F, BC changed
        di
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
        xor h
        and 1
        jr nz,.again
        ld a,h
        and 1
        ld h,a
        jr z,.inrange           ; a read of line 511 comes at some line changes: a line of
        ld a,(dlen)             ; (dlen) or more is read again
        cp l
        jr c,.again
        jr z,.again
.inrange:
        ld a,(dirq)
        or a
        jr z,.noei
        ei
.noei:
    endm
delay:  ld (sv_bc),bc
        ld (sv_de),de
        ld a,h
        or l
        jr nz,.cnt
        ld hl,7424              ; 65536 passes
        jr .set
.cnt:   ex de,hl                ; DE = passes
        ld hl,0
        ld a,0                  ; A:HL = passes * 29, 24 bits
        ld b,29
.mul:   add hl,de
        adc a,0
        djnz .mul
        ld l,h
        ld h,a                  ; HL = passes * 29 / 256 lines
.set:   ld (dleft),hl
        ld a,i                  ; P/V: interrupts on at entry
        ld a,0
        jp po,.di
        inc a
.di:    ld (dirq),a
        di
        ld bc,$243B
        ld a,$05
        out (c),a
        inc b
        in a,(c)
        ld hl,311               ; lines in a 50 Hz frame
        bit 2,a
        jr z,.hz
        ld hl,264               ; 60 Hz
.hz:    ld (dlen),hl
        RDLINE
        ld (dprev),hl
.poll:  RDLINE
        ld (dcur),hl
        ld de,(dprev)
        or a
        sbc hl,de               ; lines since the last read
        jr nc,.pos
        ld a,d                  ; a lower line: the frame wrapped only from line 256 or later.
        or a                    ; At line 256 the low byte can read 0 before the high byte
        jp z,.poll              ; reads 1: such a read is dropped
        ld de,(dlen)
        add hl,de               ; the frame wrapped
.pos:   ex de,hl
        ld hl,(dcur)
        ld (dprev),hl
        ld hl,(dleft)
        or a
        sbc hl,de
        ld (dleft),hl
        jr c,.end
        ld a,h
        or l
        jr nz,.poll
.end:   ld bc,(sv_bc)
        ld de,(sv_de)
        ld hl,0
        xor a
        ret
dirq:   db 0
dlen:   dw 0
dprev:  dw 0
dcur:   dw 0
dleft:  dw 0
sv_bc:  dw 0
sv_de:  dw 0
; vread: as the game's $3FDA-$3FDD (IN A,($7E) : DI : RET, the far call returns to the RET at
; $3FDE): the V counter read through the runtime's I/O RST with vbl_done ($E086) set first, so the
; read does not run the frame work, which the ULA interrupt then runs. A = the V counter,
; interrupts off; the other registers and F as the read leaves them.
VR_DONE equ $E086
vread:  ld a,1
        ld (VR_DONE),a
        rst $00
        db $0A                  ; IN A,(n), port class 2 ($7E: the V counter)
        di
        ret
endpage
site 00883   ; OUT ($F2),A
site 00E10   ; OUTI
site 00E12   ; OUTI
site 00E14   ; OUTI
site 00E16   ; OUTI
site 00E18   ; OUTI
site 00E1A   ; OUTI
site 00E1C   ; OUTI
site 00E1E   ; OUTI
site 00E20   ; OUTI
site 00E22   ; OUTI
site 00E24   ; OUTI
site 00E26   ; OUTI
site 00E28   ; OUTI
site 00E2A   ; OUTI
site 00E2C   ; OUTI
site 00E2E   ; OUTI
site 00E30   ; OUTI
site 00E32   ; OUTI
site 00E34   ; OUTI
site 00E36   ; OUTI
site 00E38   ; OUTI
site 00E3A   ; OUTI
site 00E3C   ; OUTI
site 00E3E   ; OUTI
site 00E40   ; OUTI
site 00E42   ; OUTI
site 00E44   ; OUTI
site 00E46   ; OUTI
site 00E48   ; OUTI
site 00E4A   ; OUTI
site 00E4C   ; OUTI
site 00E4E   ; OUTI
site 00E50   ; OUTI
site 00E52   ; OUTI
site 00E54   ; OUTI
site 00E56   ; OUTI
site 00E58   ; OUTI
site 00E5A   ; OUTI
site 00E5C   ; OUTI
site 00E5E   ; OUTI
site 00E60   ; OUTI
site 00E62   ; OUTI
site 00E64   ; OUTI
site 00E66   ; OUTI
site 00E68   ; OUTI
site 00E6A   ; OUTI
site 00E6C   ; OUTI
site 00E6E   ; OUTI
site 00E70   ; OUTI
site 00E72   ; OUTI
site 00E74   ; OUTI
site 00E76   ; OUTI
site 00E78   ; OUTI
site 00E7A   ; OUTI
site 00E7C   ; OUTI
site 00E7E   ; OUTI
site 00E80   ; OUTI
site 00E82   ; OUTI
site 00E84   ; OUTI
site 00E86   ; OUTI
site 00E88   ; OUTI
site 00E8A   ; OUTI
site 00E8C   ; OUTI
site 00E8E   ; OUTI
site 00E90   ; OUTI
site 00E92   ; OUTI
site 00E94   ; OUTI
site 00E96   ; OUTI
site 00E98   ; OUTI
site 00E9A   ; OUTI
site 00E9C   ; OUTI
site 00E9E   ; OUTI
site 00EA0   ; OUTI
site 00EA2   ; OUTI
site 00EA4   ; OUTI
site 00EA6   ; OUTI
site 00EA8   ; OUTI
site 00EAA   ; OUTI
site 00EAC   ; OUTI
site 00EAE   ; OUTI
site 00EB0   ; OUTI
site 00EB2   ; OUTI
site 00EB4   ; OUTI
site 00EB6   ; OUTI
site 00EB8   ; OUTI
site 00EBA   ; OUTI
site 00EBC   ; OUTI
site 00EBE   ; OUTI
site 00EC0   ; OUTI
site 00EC2   ; OUTI
site 00EC4   ; OUTI
site 00EC6   ; OUTI
site 00EC8   ; OUTI
site 00ECA   ; OUTI
site 00ECC   ; OUTI
site 00ECE   ; OUTI
site 00ED0   ; OUTI
site 00ED2   ; OUTI
site 00ED4   ; OUTI
site 00ED6   ; OUTI
site 00ED8   ; OUTI
site 00EDA   ; OUTI
site 00EDC   ; OUTI
site 00EDE   ; OUTI
site 00EE0   ; OUTI
site 00EE2   ; OUTI
site 00EE4   ; OUTI
site 00EE6   ; OUTI
site 00EE8   ; OUTI
site 00EEA   ; OUTI
site 00EEC   ; OUTI
site 00EEE   ; OUTI
site 00EF0   ; OUTI
site 00EF2   ; OUTI
site 00EF4   ; OUTI
site 00EF6   ; OUTI
site 00EF8   ; OUTI
site 00EFA   ; OUTI
site 00EFC   ; OUTI
site 00EFE   ; OUTI
site 01E74   ; OUT ($BF),A
site 01E79   ; OUT ($BF),A
site 01E7F   ; OUT ($BF),A
site 01E84   ; OUT ($BF),A
site 01F14   ; OUT ($BF),A
site 01F18   ; OUT ($BF),A
site 01F1E   ; OUT ($BF),A
site 01F22   ; OUT ($BF),A
site 01F28   ; OUT ($BF),A
site 01F2C   ; OUT ($BF),A
site 01F39   ; OUT ($BF),A
site 01F3D   ; OUT ($BF),A
site 01F43   ; OUT ($BF),A
site 01F47   ; OUT ($BF),A
site 01F66   ; OUTI
site 01F6C   ; OUT ($BE),A
site 01F84   ; OUT ($BE),A
site 01F8C   ; OUT ($BE),A
site 01F95   ; OUT ($BE),A
site 01F9F   ; OUT ($BE),A
site 01FB3   ; OUT ($BE),A
site 01FBE   ; OUT ($BE),A
site 01FC3   ; OUT ($BE),A
site 01FCD   ; OUT ($BE),A
site 020A1   ; OUT ($BF),A
site 020A5   ; OUT ($BF),A
site 020AB   ; OUT ($BF),A
site 020AF   ; OUT ($BF),A
site 020D6   ; OUT ($BF),A
site 020DA   ; OUT ($BF),A
site 02125   ; OUT ($BE),A
site 02137   ; OUT ($BE),A
site 0221B   ; OUT ($BF),A
site 0221F   ; OUT ($BF),A
site 0248A   ; OUT ($BE),A
site 033DF   ; OUT ($BF),A
site 033E4   ; OUT ($BF),A
site 035D2   ; OUTI
site 037CF   ; OUT ($01),A
site 03958   ; OUT ($BF),A
site 0395D   ; OUT ($BF),A
site 039A5   ; OUT ($BF),A
site 039AA   ; OUT ($BF),A
site 039C9   ; OUT ($BF),A
site 039CE   ; OUT ($BF),A
site 039E7   ; OUT ($BF),A
site 039EC   ; OUT ($BF),A
site 03A0A   ; OUT ($BE),A
site 03A11   ; OUT ($BE),A
site 03A19   ; OUT ($BF),A
site 03A1E   ; OUT ($BF),A
site 03A26   ; OUT ($BE),A
site 03A2D   ; OUT ($BE),A
site 03A80   ; OUT ($BE),A
site 03A87   ; OUT ($BE),A
site 03B48   ; OUT ($BF),A
site 03B4D   ; OUT ($BF),A
site 03B52   ; OUTI
site 03BBF   ; OUT ($BF),A
site 03BC4   ; OUT ($BF),A
site 03C00   ; OUT ($BE),A
site 03C06   ; OUT ($BE),A
site 03C34   ; OUTI
site 03C3A   ; OUTI
site 03C40   ; OUTI
site 03C46   ; OUTI
site 03C6B   ; OUT ($BE),A
site 03C71   ; OUT ($BE),A
site 03C85   ; OUT ($BE),A
site 03C8D   ; OUT ($BE),A
site 03D33   ; OUT ($BE),A
site 03D36   ; OUTI
site 03D38   ; OUTI
site 03D3C   ; OUT ($BE),A
site 03D45   ; IN A,($BF)
site 03D60   ; IN A,($DD)
site 03E0A   ; OUT ($BF),A
site 03E0F   ; OUT ($BF),A
site 03FCB   ; IN A,($BF)
site 040C7   ; OUT ($BE),A
site 040DA   ; OUT ($BF),A
site 040DD   ; OUT ($BF),A
site 04123   ; OUT ($BE),A
site 0412B   ; OUT ($BF),A
site 0412E   ; OUT ($BF),A
site 04148   ; OUTI
site 04158   ; OUTI
site 05573   ; OUT ($BF),A
site 05577   ; OUT ($BF),A
site 05594   ; OUT ($BF),A
site 05598   ; OUT ($BF),A
site 055B7   ; OUT ($BF),A
site 055BC   ; OUT ($BF),A
site 055FA   ; OUTI
site 0561C   ; OUT ($BF),A
site 05620   ; OUT ($BF),A
site 05626   ; OUT ($BF),A
site 0562A   ; OUT ($BF),A
site 05630   ; OUT ($BF),A
site 05634   ; OUT ($BF),A
site 056CD   ; OUT ($BE),A
site 056FB   ; OUT ($BF),A
site 056FF   ; OUT ($BF),A
site 0572D   ; OUT ($BE),A
site 059F6   ; OUT ($BE),A
site 059FE   ; OUT (C),E
site 05AEF   ; OUT ($BF),A
site 05AF3   ; OUT ($BF),A
site 05AF9   ; OUT ($BF),A
site 05AFD   ; OUT ($BF),A
site 05B03   ; OUT ($BF),A
site 05B07   ; OUT ($BF),A
site 05B0D   ; OUT ($BF),A
site 05B11   ; OUT ($BF),A
site 05B17   ; OUT ($BF),A
site 05B1B   ; OUT ($BF),A
site 05B21   ; OUT ($BF),A
site 05B25   ; OUT ($BF),A
site 05B2B   ; OUT ($BF),A
site 05B2F   ; OUT ($BF),A
site 05B35   ; OUT ($BF),A
site 05B39   ; OUT ($BF),A
site 05B3F   ; OUT ($BF),A
site 05B43   ; OUT ($BF),A
site 05B49   ; OUT ($BF),A
site 05B4D   ; OUT ($BF),A
site 05B58   ; OUT ($BF),A
site 05B5C   ; OUT ($BF),A
site 05C40   ; OUT ($BF),A
site 05C44   ; OUT ($BF),A
site 05DF9   ; OUT ($BE),A
site 05E0B   ; OUT ($BE),A
site 0613C   ; OUTI
site 06142   ; OUT ($BE),A
site 06214   ; OUT ($BE),A
site 06226   ; OUT ($BF),A
site 0622C   ; OUT ($BF),A
site 06239   ; OUT ($BE),A
site 0623F   ; OUT ($BE),A
site 06251   ; OUT ($BE),A
site 0631C   ; OUT ($BF),A
site 06321   ; OUT ($BF),A
site 06347   ; OUT ($BE),A
site 063A6   ; OUT ($BE),A
site 063D3   ; OUT ($BF),A
site 063D7   ; OUT ($BF),A
site 06416   ; OUT ($BF),A
site 0641A   ; OUT ($BF),A
site 0641D   ; OUT ($BE),A
site 06422   ; OUT ($BF),A
site 06426   ; OUT ($BF),A
site 06523   ; IN A,($DC)
site 0653E   ; IN A,($DC)
site 06549   ; IN A,($DD)
site 06598   ; OUT ($BF),A
site 0659C   ; OUT ($BF),A
site 065B0   ; OUT ($BF),A
site 065B4   ; OUT ($BF),A
site 065BA   ; OUT ($BF),A
site 065BE   ; OUT ($BF),A
site 06675   ; OUT ($BE),A
site 0668B   ; OUT ($BE),A
site 066A1   ; OUT ($BE),A
site 066B7   ; OUT ($BE),A
site 06710   ; OUT ($BE),A
site 06718   ; OUT ($BE),A
site 06B16   ; OUTI
site 06B23   ; OUT ($BE),A
otir 06E26   ; OUTI
site 06E57   ; OUTI
site 06E64   ; OUT ($BF),A
site 06E68   ; OUT ($BF),A
site 06E6D   ; OUT ($BF),A
site 06E71   ; OUT ($BF),A
site 06E80   ; OUT ($7F),A
site 06E84   ; OUT ($7F),A
site 06E88   ; OUT ($7F),A
site 06E8C   ; OUT ($7F),A
site 06F5C   ; OUT ($BF),A
site 06F61   ; OUT ($BF),A
site 06F9E   ; OUTI
site 06FA3   ; OUTI
site 06FB9   ; OUT ($BF),A
site 06FBE   ; OUT ($BF),A
site 06FF8   ; OUTI
site 06FFB   ; OUTI
site 06FFE   ; OUTI
site 07001   ; OUTI
site 07009   ; OUTI
site 0700C   ; OUTI
site 0700F   ; OUTI
site 07012   ; OUTI
site 0701A   ; OUTI
site 0701D   ; OUTI
site 07020   ; OUTI
site 07023   ; OUTI
site 0702B   ; OUTI
site 0702E   ; OUTI
site 07031   ; OUTI
site 07034   ; OUTI
site 0703C   ; OUTI
site 0703F   ; OUTI
site 07042   ; OUTI
site 07045   ; OUTI
site 0704D   ; OUTI
site 07050   ; OUTI
site 07053   ; OUTI
site 07056   ; OUTI
site 0705E   ; OUTI
site 07061   ; OUTI
site 07064   ; OUTI
site 07067   ; OUTI
site 0706F   ; OUTI
site 07072   ; OUTI
site 07075   ; OUTI
site 07078   ; OUTI
site 07080   ; OUTI
site 07083   ; OUTI
site 07086   ; OUTI
site 07089   ; OUTI
site 07091   ; OUTI
site 07094   ; OUTI
site 07097   ; OUTI
site 0709A   ; OUTI
site 070A2   ; OUTI
site 070A5   ; OUTI
site 070A8   ; OUTI
site 070AB   ; OUTI
site 070B3   ; OUTI
site 070B6   ; OUTI
site 070B9   ; OUTI
site 070BC   ; OUTI
site 070C4   ; OUTI
site 070C7   ; OUTI
site 070CA   ; OUTI
site 070CD   ; OUTI
site 070D5   ; OUTI
site 070D8   ; OUTI
site 070DB   ; OUTI
site 070DE   ; OUTI
site 070E6   ; OUTI
site 070E9   ; OUTI
site 070EC   ; OUTI
site 070EF   ; OUTI
site 070F7   ; OUTI
site 070FA   ; OUTI
site 070FD   ; OUTI
site 07100   ; OUTI
site 0710B   ; OUTI
site 0710E   ; OUTI
otir 072DC   ; OUTI
site 072E9   ; OUT ($BF),A
site 072ED   ; OUT ($BF),A
site 07383   ; OUTI
site 07389   ; OUTI
site 0B37E   ; OUT ($BE),A
site 0B382   ; OUT ($BE),A
site 0B38F   ; OUT ($BE),A
site 0B39A   ; OUT ($BE),A
site 0B3A0   ; OUT ($BE),A
site 0B3AC   ; OUT ($BE),A
site 0B3B2   ; OUT ($BE),A
site 0B3B8   ; OUT ($BE),A
site 0B3BE   ; OUT ($BE),A
site 0B3C4   ; OUT ($BE),A
site 0B3CA   ; OUT ($BE),A
site 0B3D0   ; OUT ($BE),A
site 0B3D6   ; OUT ($BE),A
site 0B3DA   ; OUT ($BE),A
site 0B3DE   ; OUT ($BE),A
site 0B527   ; IN A,($BF)
site 0B529   ; IN A,($BF)
site 0B535   ; IN A,($BF)
site 14EF5   ; OUT ($BF),A
site 14EF9   ; OUT ($BF),A
site 14F41   ; OUT ($BE),A
site 1522B   ; IN A,($BE)
site 15232   ; IN A,($BE)
site 1523E   ; OUT ($BE),A
site 15244   ; OUT ($BE),A
site 1525C   ; INI
site 152F3   ; OUTI
site 15848   ; OUT ($BF),A
site 1584C   ; OUT ($BF),A
site 15852   ; OUT ($BF),A
site 15856   ; OUT ($BF),A
site 15D2B   ; IN A,($BE)
site 15D43   ; OUT ($BE),A
site 15D4B   ; OUT ($BE),A
site 15D79   ; INI
site 15DA4   ; IN A,($BE)
site 15DBA   ; OUTI
site 68117   ; OUT ($7F),A
site 6812D   ; OUT ($7F),A
site 68144   ; OUT ($7F),A
site 68157   ; OUT ($7F),A
mapst 00006   ; LD ($FFFC),A
mapst 0000B   ; LD ($FFFD),A
mapst 00010   ; LD ($FFFE),A
mapst 00015   ; LD ($FFFF),A
mapst 01DA3   ; LD ($FFFF),A
mapst 01F0E   ; LD ($FFFE),A
mapst 01F5E   ; LD ($FFFF),A
mapst 01FA2   ; LD ($FFFE),A
mapst 01FDB   ; LD ($FFFF),A
mapst 02011   ; LD ($FFFF),A
mapst 0206A   ; LD ($FFFF),A
mapst 02087   ; LD ($FFFF),A
mapst 020F5   ; LD ($FFFF),A
mapst 0214E   ; LD ($FFFF),A
mapst 02165   ; LD ($FFFF),A
mapst 021C7   ; LD ($FFFF),A
mapst 022B4   ; LD ($FFFF),A
mapst 022E5   ; LD ($FFFF),A
mapst 022FF   ; LD ($FFFE),A
mapst 023FE   ; LD ($FFFE),A
mapst 02470   ; LD ($FFFF),A
mapst 0247B   ; LD ($FFFF),A
mapst 02684   ; LD ($FFFE),A
mapst 0272A   ; LD ($FFFE),A
mapst 028E2   ; LD ($FFFF),A
mapst 029B8   ; LD ($FFFE),A
mapst 02C30   ; LD ($FFFE),A
mapst 03379   ; LD ($FFFE),A
mapst 0353E   ; LD ($FFFE),A
mapst 03608   ; LD ($FFFF),A
mapst 03ACF   ; LD ($FFFF),A
mapst 03B43   ; LD ($FFFF),A
mapst 03BE0   ; LD ($FFFF),A
mapst 03D23   ; LD ($FFFF),A
mapst 0438E   ; LD ($FFFF),A
mapst 04468   ; LD ($FFFF),A
mapst 044AE   ; LD ($FFFF),A
mapst 044C0   ; LD ($FFFF),A
maphl 055AB   # LD (HL),$04, HL = $FFFF
mapst 055D7   ; LD ($FFFF),A
maphl 0560C   # LD (HL),$04, HL = $FFFF
mapst 056F5   ; LD ($FFFF),A
mapld 05826   # LD HL,$FFFF; LD (HL),$04
maphl 05909   # LD (HL),$04, HL = $FFFF
mapst 0594D   ; LD ($FFFF),A
mapst 059AD   ; LD ($FFFF),A
mapst 05AB5   ; LD ($FFFF),A
mapst 05B84   ; LD ($FFFF),A
mapst 05B9C   ; LD ($FFFF),A
mapst 05C37   ; LD ($FFFF),A
mapst 05C8F   ; LD ($FFFF),A
mapst 05CAB   ; LD ($FFFF),A
mapst 05D5A   ; LD ($FFFF),A
mapst 05D83   ; LD ($FFFF),A
mapst 05FB3   ; LD ($FFFF),A
# CHECK mapper at 05FBC ($5FBC bank 1): ED B0  LDIR $CB00-$1B315 $CB00-$14ABD $CB00-$10AFF $CB00-$1C5FE $CB00-$1C9FB
mapst 05FD3   ; LD ($FFFF),A
mapst 05FFE   ; LD ($FFFF),A
maphl 0658C   # LD (HL),$06, HL = $FFFF
mapst 065D1   ; LD ($FFFF),A
mapst 065F3   ; LD ($FFFF),A
mapst 06642   ; LD ($FFFF),A
mapst 06653   ; LD ($FFFF),A
mapst 06B00   ; LD ($FFFF),A
mapst 06E02   ; LD ($FFFF),A
mapst 06E2E   ; LD ($FFFF),A
mapst 06EC5   ; LD ($FFFF),A
mapst 06EF0   ; LD ($FFFF),A
mapst 071C6   ; LD ($FFFF),A
mapst 072FB   ; LD ($FFFF),A
mapst 073BC   ; LD ($FFFF),A
mapst 073C9   ; LD ($FFFF),A
mapst 07B61   ; LD ($FFFF),A
mapst 19A85   ; LD ($FFFE),A
mapst 19A97   ; LD ($FFFE),A
# CHECK cartarea_store at 00288 ($0288 bank 0): 22 22 22  LD ($2222),HL $2222,$2223
# CHECK cartarea_store at 002C8 ($02C8 bank 0): 32 32 32  LD ($3232),A $3232
# CHECK cartarea_store at 002CA ($02CA bank 0): 32 32 32  LD ($3232),A $3232
# CHECK cartarea_store at 002CC ($02CC bank 0): 32 32 32  LD ($3232),A $3232
# CHECK cartarea_store at 002CE ($02CE bank 0): 32 32 34  LD ($3432),A $3432
# CHECK cartarea_store at 002D0 ($02D0 bank 0): 34  INC (HL) $262E
# CHECK cartarea_store at 002D1 ($02D1 bank 0): 34  INC (HL) $262E
# CHECK cartarea_store at 002D2 ($02D2 bank 0): 34  INC (HL) $262E
# CHECK cartarea_store at 002D3 ($02D3 bank 0): 34  INC (HL) $262E
# CHECK cartarea_store at 002D4 ($02D4 bank 0): 34  INC (HL) $262E
# CHECK cartarea_store at 002D5 ($02D5 bank 0): 34  INC (HL) $262E
# CHECK cartarea_store at 002D6 ($02D6 bank 0): 34  INC (HL) $262E
# CHECK cartarea_store at 002D7 ($02D7 bank 0): 34  INC (HL) $262E
# CHECK cartarea_store at 002D8 ($02D8 bank 0): 36 36  LD (HL),$36 $262E
# CHECK cartarea_store at 002D9 ($02D9 bank 0): 36 36  LD (HL),$36 $212E,$262E
# CHECK cartarea_store at 002DA ($02DA bank 0): 36 36  LD (HL),$36 $262E
# CHECK cartarea_store at 002DB ($02DB bank 0): 36 36  LD (HL),$36 $212E,$262E
# CHECK cartarea_store at 002DC ($02DC bank 0): 36 36  LD (HL),$36 $262E
# CHECK cartarea_store at 002DD ($02DD bank 0): 36 36  LD (HL),$36 $212E,$262E
# CHECK cartarea_store at 002DE ($02DE bank 0): 36 36  LD (HL),$36 $262E
# CHECK cartarea_store at 002DF ($02DF bank 0): 36 38  LD (HL),$38 $212E,$262E
# CHECK cartarea_store at 00411 ($0411 bank 0): 02  LD (BC),A $0201
# CHECK cartarea_store at 00412 ($0412 bank 0): 02  LD (BC),A $0201
# CHECK cartarea_store at 00413 ($0413 bank 0): 02  LD (BC),A $0201
# CHECK cartarea_store at 00414 ($0414 bank 0): 02  LD (BC),A $0201
# CHECK cartarea_store at 00415 ($0415 bank 0): 02  LD (BC),A $0201
# CHECK cartarea_store at 00416 ($0416 bank 0): 02  LD (BC),A $0201
# CHECK cartarea_store at 00417 ($0417 bank 0): 02  LD (BC),A $0201
# CHECK cartarea_store at 00492 ($0492 bank 0): 12  LD (DE),A $161E
# CHECK cartarea_store at 00493 ($0493 bank 0): 12  LD (DE),A $161E
# CHECK cartarea_store at 00494 ($0494 bank 0): 12  LD (DE),A $161E
# CHECK cartarea_store at 00495 ($0495 bank 0): 12  LD (DE),A $161E
# CHECK cartarea_store at 00496 ($0496 bank 0): 12  LD (DE),A $161E
# CHECK cartarea_store at 00497 ($0497 bank 0): 12  LD (DE),A $161E
# CHECK cartarea_store at 00522 ($0522 bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 00523 ($0523 bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 00524 ($0524 bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 00525 ($0525 bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 00526 ($0526 bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 00527 ($0527 bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 00528 ($0528 bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 00529 ($0529 bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 0052A ($052A bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 0052B ($052B bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 0052C ($052C bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 0052D ($052D bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 0052E ($052E bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 0052F ($052F bank 0): 02  LD (BC),A $0202
# CHECK cartarea_store at 00631 ($0631 bank 0): 02  LD (BC),A $01C0
# CHECK cartarea_store at 00633 ($0633 bank 0): 02  LD (BC),A $01C0,$0200
# CHECK cartarea_store at 00635 ($0635 bank 0): 02  LD (BC),A $01C0,$0200
# CHECK cartarea_store at 00637 ($0637 bank 0): 02  LD (BC),A $01C0,$0200
# CHECK cartarea_store at 00639 ($0639 bank 0): 02  LD (BC),A $01C0,$0200
# CHECK cartarea_store at 0063B ($063B bank 0): 02  LD (BC),A $01C0,$0200
# CHECK cartarea_store at 0063D ($063D bank 0): 02  LD (BC),A $01C0,$0200
# CHECK cartarea_store at 0063F ($063F bank 0): 02  LD (BC),A $01C0,$0200
# CHECK cartarea_store at 00690 ($0690 bank 0): 02  LD (BC),A $0008,$00C8
# CHECK cartarea_store at 4CB51 ($CDA9 bank ram): 70  LD (HL),B $06BE,$394C
# CHECK cartarea_store at 4E0E0 ($E338 bank ram): 32 E5 44  LD ($44E5),A $44E5
# CHECK cartarea_store at 4F956 ($FBAE bank ram): 02  LD (BC),A $0105
# CHECK cartarea_store at 4F957 ($FBAF bank ram): 02  LD (BC),A $0105
# CHECK cartarea_store at 4F960 ($FBB8 bank ram): 02  LD (BC),A $0105
# CHECK cartarea_store at 4F965 ($FBBD bank ram): 02  LD (BC),A $0207
# CHECK cartarea_store at 4F977 ($FBCF bank ram): 02  LD (BC),A $03FD
# CHECK cartarea_store at 4FD0B ($FF63 bank ram): 02  LD (BC),A $0302
# CHECK cartarea_store at 4FD0C ($FF64 bank ram): 02  LD (BC),A $0302
# CHECK ram_exec at 073C2 ($73C2 bank 1): CD 02 C3  CALL $C302 $C302
# CHECK ram_exec at 155F8 ($95F8 bank 5): F8  RET M $C7A3
# CHECK indirect_unresolved at 00378 ($0378 bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0037A ($037A bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0037C ($037C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0037E ($037E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 00398 ($0398 bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0039A ($039A bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0039C ($039C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0039E ($039E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 003B8 ($03B8 bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 003BA ($03BA bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 003BC ($03BC bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 003BE ($03BE bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0061C ($061C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0061E ($061E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0062C ($062C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0062E ($062E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0063C ($063C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0063E ($063E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0064C ($064C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0064E ($064E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0065C ($065C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0065E ($065E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0066C ($066C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0066E ($066E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0068C ($068C bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0068E ($068E bank 0): C0  RET NZ 
# CHECK indirect_unresolved at 0120B ($120B bank 0): DD E9  JP (IX) 
# CHECK indirect_unresolved at 0121A ($121A bank 0): FD E9  JP (IY) 
# CHECK indirect_unresolved at 02A60 ($2A60 bank 0): FD E9  JP (IY) 
# CHECK indirect_unresolved at 044A1 ($44A1 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 044EB ($44EB bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 065DF ($65DF bank 1): CD B1 72  CALL $72B1 
# CHECK indirect_unresolved at 06FB2 ($6FB2 bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 06FEB ($6FEB bank 1): E9  JP (HL) 
# CHECK indirect_unresolved at 072F5 ($72F5 bank 1): C9  RET 
# CHECK indirect_unresolved at 15597 ($9597 bank 5): F8  RET M 
# CHECK indirect_unresolved at 19363 ($9363 bank 6): E9  JP (HL) 
# CHECK indirect_unresolved at 4CB3C ($CD94 bank ram): E9  JP (HL) 
# CHECK indirect_unresolved at 4F9FB ($FC53 bank ram): C0  RET NZ 
# CHECK bank_unresolved at 00018 ($0018 bank 0): C3 8A 5A  JP $5A8A $5A8A
# CHECK bank_unresolved at 01DBC ($1DBC bank 0): C3 72 60  JP $6072 $6072
# CHECK bank_unresolved at 01DDC ($1DDC bank 0): CD F9 6E  CALL $6EF9 $6EF9
# CHECK bank_unresolved at 01DE1 ($1DE1 bank 0): CD F9 6E  CALL $6EF9 $6EF9
# CHECK bank_unresolved at 01DF2 ($1DF2 bank 0): CD F9 6E  CALL $6EF9 $6EF9
# CHECK bank_unresolved at 01E03 ($1E03 bank 0): C3 F9 6E  JP $6EF9 $6EF9
# CHECK bank_unresolved at 01FDE ($1FDE bank 0): CD C7 6A  CALL $6AC7 $6AC7
# CHECK bank_unresolved at 01FE1 ($1FE1 bank 0): CD EE 5D  CALL $5DEE $5DEE
# CHECK bank_unresolved at 01FF5 ($1FF5 bank 0): CD 14 5E  CALL $5E14 $5E14
# CHECK bank_unresolved at 02005 ($2005 bank 0): CD 14 5E  CALL $5E14 $5E14
# CHECK bank_unresolved at 02008 ($2008 bank 0): CD C2 63  CALL $63C2 $63C2
# CHECK bank_unresolved at 0200B ($200B bank 0): CD 1A 62  CALL $621A $621A
# CHECK bank_unresolved at 02017 ($2017 bank 0): CD 1A 62  CALL $621A $621A
# CHECK bank_unresolved at 02030 ($2030 bank 0): CD FC 6D  CALL $6DFC $6DFC
# CHECK bank_unresolved at 0203D ($203D bank 0): CD FC 6D  CALL $6DFC $6DFC
# CHECK bank_unresolved at 0204A ($204A bank 0): CD FC 6D  CALL $6DFC $6DFC
# CHECK bank_unresolved at 02057 ($2057 bank 0): CD FC 6D  CALL $6DFC $6DFC
# CHECK bank_unresolved at 02083 ($2083 bank 0): CD 6D 5F  CALL $5F6D $5F6D
# CHECK bank_unresolved at 020B2 ($20B2 bank 0): CD B3 6E  CALL $6EB3 $6EB3
# CHECK bank_unresolved at 020C3 ($20C3 bank 0): CD 60 6E  CALL $6E60 $6E60
# CHECK bank_unresolved at 020EA ($20EA bank 0): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 02102 ($2102 bank 0): CD 68 5E  CALL $5E68 $5E68
# CHECK bank_unresolved at 02113 ($2113 bank 0): CD 68 5E  CALL $5E68 $5E68
# CHECK bank_unresolved at 02154 ($2154 bank 0): CD 10 65  CALL $6510 $6510
# CHECK bank_unresolved at 02157 ($2157 bank 0): CD AB 61  CALL $61AB $61AB
# CHECK bank_unresolved at 02160 ($2160 bank 0): CD 60 6E  CALL $6E60 $6E60
# CHECK bank_unresolved at 0216F ($216F bank 0): CD E9 73  CALL $73E9 $73E9
# CHECK bank_unresolved at 02176 ($2176 bank 0): CD E9 73  CALL $73E9 $73E9
# CHECK bank_unresolved at 02179 ($2179 bank 0): CD C3 71  CALL $71C3 $71C3
# CHECK bank_unresolved at 0217C ($217C bank 0): CD C1 6D  CALL $6DC1 $6DC1
# CHECK bank_unresolved at 0217F ($217F bank 0): CD E7 61  CALL $61E7 $61E7
# CHECK bank_unresolved at 02191 ($2191 bank 0): CD E9 73  CALL $73E9 $73E9
# CHECK bank_unresolved at 02198 ($2198 bank 0): CD E9 73  CALL $73E9 $73E9
# CHECK bank_unresolved at 02231 ($2231 bank 0): CD D4 40  CALL $40D4 $40D4
# CHECK bank_unresolved at 0223F ($223F bank 0): CD 60 6E  CALL $6E60 $6E60
# CHECK bank_unresolved at 0226D ($226D bank 0): CD 17 40  CALL $4017 $4017
# CHECK bank_unresolved at 02270 ($2270 bank 0): CD A9 42  CALL $42A9 $42A9
# CHECK bank_unresolved at 0228D ($228D bank 0): C4 5F BE  CALL NZ,$BE5F $BE5F
# CHECK bank_unresolved at 02290 ($2290 bank 0): CD D4 40  CALL $40D4 $40D4
# CHECK bank_unresolved at 022A0 ($22A0 bank 0): CD 57 64  CALL $6457 $6457
# CHECK bank_unresolved at 022A3 ($22A3 bank 0): CD C3 71  CALL $71C3 $71C3
# CHECK bank_unresolved at 022A6 ($22A6 bank 0): CD C1 6D  CALL $6DC1 $6DC1
# CHECK bank_unresolved at 022A9 ($22A9 bank 0): CD 34 5E  CALL $5E34 $5E34
# CHECK bank_unresolved at 022AC ($22AC bank 0): CD E7 61  CALL $61E7 $61E7
# CHECK bank_unresolved at 022AF ($22AF bank 0): CD AB 61  CALL $61AB $61AB
# CHECK bank_unresolved at 022CE ($22CE bank 0): CD 53 93  CALL $9353 $9353
# CHECK bank_unresolved at 022D1 ($22D1 bank 0): CD C4 92  CALL $92C4 $92C4
# CHECK bank_unresolved at 022D4 ($22D4 bank 0): CD E9 73  CALL $73E9 $73E9
# CHECK bank_unresolved at 022D7 ($22D7 bank 0): CD 2E 94  CALL $942E $942E
# CHECK bank_unresolved at 022EB ($22EB bank 0): CD C4 92  CALL $92C4 $92C4
# CHECK bank_unresolved at 022EE ($22EE bank 0): CD E9 73  CALL $73E9 $73E9
# CHECK bank_unresolved at 022F1 ($22F1 bank 0): CD 2E 94  CALL $942E $942E
# CHECK bank_unresolved at 022F4 ($22F4 bank 0): CD 36 43  CALL $4336 $4336
# CHECK bank_unresolved at 02326 ($2326 bank 0): CA AE 5B  JP Z,$5BAE $5BAE
# CHECK bank_unresolved at 0232E ($232E bank 0): DA AE 5B  JP C,$5BAE $5BAE
# CHECK bank_unresolved at 02336 ($2336 bank 0): DA AE 5B  JP C,$5BAE $5BAE
# CHECK bank_unresolved at 03D64 ($3D64 bank 0): CA 7A 5A  JP Z,$5A7A $5A7A
# CHECK bank_unresolved at 03E34 ($3E34 bank 0): CD 1E 71  CALL $711E $711E
# CHECK bank_unresolved at 03E40 ($3E40 bank 0): C3 1E 71  JP $711E $711E
# CHECK bank_unresolved at 044C6 ($44C6 bank 1): CD C4 92  CALL $92C4 $92C4
# CHECK bank_unresolved at 044CC ($44CC bank 1): CD 2E 94  CALL $942E $942E
# CHECK bank_unresolved at 044DF ($44DF bank 1): CD 0C 94  CALL $940C $940C
# CHECK bank_unresolved at 05B8A ($5B8A bank 1): CD 4F B5  CALL $B54F $B54F
# CHECK bank_unresolved at 0B3F4 ($B3F4 bank 2): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 0B3FA ($B3FA bank 2): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 14002 ($8002 bank 5): CD 40 40  CALL $4040 $4040
# CHECK bank_unresolved at 14029 ($8029 bank 5): CD 6D 5F  CALL $5F6D $5F6D
# CHECK bank_unresolved at 1402C ($802C bank 5): CD B3 6E  CALL $6EB3 $6EB3
# CHECK bank_unresolved at 1402F ($802F bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 1403B ($803B bank 5): CD CA 63  CALL $63CA $63CA
# CHECK bank_unresolved at 1403F ($803F bank 5): CD 32 42  CALL $4232 $4232
# CHECK bank_unresolved at 1404D ($804D bank 5): CD 68 40  CALL $4068 $4068
# CHECK bank_unresolved at 14050 ($8050 bank 5): CD B3 6E  CALL $6EB3 $6EB3
# CHECK bank_unresolved at 14071 ($8071 bank 5): CD 68 40  CALL $4068 $4068
# CHECK bank_unresolved at 14074 ($8074 bank 5): CD B3 6E  CALL $6EB3 $6EB3
# CHECK bank_unresolved at 14098 ($8098 bank 5): CD 68 40  CALL $4068 $4068
# CHECK bank_unresolved at 1409B ($809B bank 5): CD B3 6E  CALL $6EB3 $6EB3
# CHECK bank_unresolved at 140B0 ($80B0 bank 5): CD 68 40  CALL $4068 $4068
# CHECK bank_unresolved at 140B9 ($80B9 bank 5): CD C8 62  CALL $62C8 $62C8
# CHECK bank_unresolved at 14E86 ($8E86 bank 5): CD 1A 62  CALL $621A $621A
# CHECK bank_unresolved at 14E89 ($8E89 bank 5): CD CA 40  CALL $40CA $40CA
# CHECK bank_unresolved at 14E8F ($8E8F bank 5): CD 28 66  CALL $6628 $6628
# CHECK bank_unresolved at 14E99 ($8E99 bank 5): CD CA 63  CALL $63CA $63CA
# CHECK bank_unresolved at 14E9C ($8E9C bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 14EAB ($8EAB bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 14EB1 ($8EB1 bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 14EE8 ($8EE8 bank 5): CD D4 40  CALL $40D4 $40D4
# CHECK bank_unresolved at 14EEF ($8EEF bank 5): CC EE 5D  CALL Z,$5DEE $5DEE
# CHECK bank_unresolved at 14F06 ($8F06 bank 5): CD 10 65  CALL $6510 $6510
# CHECK bank_unresolved at 14F09 ($8F09 bank 5): CD AB 61  CALL $61AB $61AB
# CHECK bank_unresolved at 14F19 ($8F19 bank 5): CD 60 6E  CALL $6E60 $6E60
# CHECK bank_unresolved at 14F59 ($8F59 bank 5): CA 91 5B  JP Z,$5B91 $5B91
# CHECK bank_unresolved at 14F6D ($8F6D bank 5): CD F2 66  CALL $66F2 $66F2
# CHECK bank_unresolved at 14F80 ($8F80 bank 5): CD B6 40  CALL $40B6 $40B6
# CHECK bank_unresolved at 14F8B ($8F8B bank 5): CD 02 5E  CALL $5E02 $5E02
# CHECK bank_unresolved at 14FA4 ($8FA4 bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 14FC2 ($8FC2 bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 14FC8 ($8FC8 bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 14FDD ($8FDD bank 5): CD D4 40  CALL $40D4 $40D4
# CHECK bank_unresolved at 1500D ($900D bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 15052 ($9052 bank 5): CD D4 40  CALL $40D4 $40D4
# CHECK bank_unresolved at 15086 ($9086 bank 5): CD 18 63  CALL $6318 $6318
# CHECK bank_unresolved at 15098 ($9098 bank 5): CD 18 63  CALL $6318 $6318
# CHECK bank_unresolved at 1552F ($952F bank 5): CD 02 5E  CALL $5E02 $5E02
# CHECK bank_unresolved at 15532 ($9532 bank 5): CD CA 40  CALL $40CA $40CA
# CHECK bank_unresolved at 15535 ($9535 bank 5): CD C2 63  CALL $63C2 $63C2
# CHECK bank_unresolved at 15545 ($9545 bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 1554E ($954E bank 5): CD 6D 5F  CALL $5F6D $5F6D
# CHECK bank_unresolved at 15557 ($9557 bank 5): CD 08 66  CALL $6608 $6608
# CHECK bank_unresolved at 1555D ($955D bank 5): CD 75 62  CALL $6275 $6275
# CHECK bank_unresolved at 1556A ($956A bank 5): CD 16 42  CALL $4216 $4216
# CHECK bank_unresolved at 1556D ($956D bank 5): CD AB 61  CALL $61AB $61AB
# CHECK bank_unresolved at 15575 ($9575 bank 5): CD 60 6E  CALL $6E60 $6E60
# CHECK bank_unresolved at 1557E ($957E bank 5): CD B3 6E  CALL $6EB3 $6EB3
# CHECK bank_unresolved at 1558C ($958C bank 5): CD DC 58  CALL $58DC $58DC
# CHECK bank_unresolved at 1558F ($958F bank 5): CD 60 6E  CALL $6E60 $6E60
# CHECK bank_unresolved at 15593 ($9593 bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 1559D ($959D bank 5): CD E2 6B  CALL $6BE2 $6BE2
# CHECK bank_unresolved at 155A6 ($95A6 bank 5): CD 04 64  CALL $6404 $6404
# CHECK bank_unresolved at 155A9 ($95A9 bank 5): CD CA 63  CALL $63CA $63CA
# CHECK bank_unresolved at 155AE ($95AE bank 5): CD 47 40  CALL $4047 $4047
# CHECK bank_unresolved at 155CB ($95CB bank 5): CD 10 65  CALL $6510 $6510
# CHECK bank_unresolved at 155DC ($95DC bank 5): CD A9 42  CALL $42A9 $42A9
# CHECK bank_unresolved at 155F4 ($95F4 bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 155FB ($95FB bank 5): CD E2 6B  CALL $6BE2 $6BE2
# CHECK bank_unresolved at 15609 ($9609 bank 5): CD B3 6E  CALL $6EB3 $6EB3
# CHECK bank_unresolved at 1560D ($960D bank 5): CD E2 6B  CALL $6BE2 $6BE2
# CHECK bank_unresolved at 15616 ($9616 bank 5): CD 04 64  CALL $6404 $6404
# CHECK bank_unresolved at 1561C ($961C bank 5): CD CA 63  CALL $63CA $63CA
# CHECK bank_unresolved at 15623 ($9623 bank 5): CD 68 40  CALL $4068 $4068
# CHECK bank_unresolved at 15634 ($9634 bank 5): CD A9 42  CALL $42A9 $42A9
# CHECK bank_unresolved at 15637 ($9637 bank 5): CD AB 61  CALL $61AB $61AB
# CHECK bank_unresolved at 15646 ($9646 bank 5): CD 60 6E  CALL $6E60 $6E60
# CHECK bank_unresolved at 1564A ($964A bank 5): CD E2 6B  CALL $6BE2 $6BE2
# CHECK bank_unresolved at 1564D ($964D bank 5): CD 10 65  CALL $6510 $6510
# CHECK bank_unresolved at 15653 ($9653 bank 5): CD 57 64  CALL $6457 $6457
# CHECK bank_unresolved at 15679 ($9679 bank 5): CD A9 42  CALL $42A9 $42A9
# CHECK bank_unresolved at 1567C ($967C bank 5): CD 10 65  CALL $6510 $6510
# CHECK bank_unresolved at 1568E ($968E bank 5): CD 1A 62  CALL $621A $621A
# CHECK bank_unresolved at 15870 ($9870 bank 5): CD EE 5D  CALL $5DEE $5DEE
# CHECK bank_unresolved at 15875 ($9875 bank 5): CD 02 5E  CALL $5E02 $5E02
# CHECK bank_unresolved at 15886 ($9886 bank 5): CD 60 6E  CALL $6E60 $6E60
# CHECK bank_unresolved at 15889 ($9889 bank 5): CD 10 65  CALL $6510 $6510
# CHECK bank_unresolved at 1589D ($989D bank 5): CD D7 5C  CALL $5CD7 $5CD7
# CHECK bank_unresolved at 158A3 ($98A3 bank 5): CD D7 5C  CALL $5CD7 $5CD7
# CHECK bank_unresolved at 158C0 ($98C0 bank 5): CD 16 42  CALL $4216 $4216
# CHECK bank_unresolved at 158D8 ($98D8 bank 5): CD 04 64  CALL $6404 $6404
# CHECK bank_unresolved at 158DB ($98DB bank 5): CD CA 63  CALL $63CA $63CA
# CHECK bank_unresolved at 1590A ($990A bank 5): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 15924 ($9924 bank 5): CD A9 42  CALL $42A9 $42A9
# CHECK bank_unresolved at 1592B ($992B bank 5): CD 10 65  CALL $6510 $6510
# CHECK bank_unresolved at 15932 ($9932 bank 5): CD 16 42  CALL $4216 $4216
# CHECK bank_unresolved at 15D19 ($9D19 bank 5): CD 10 65  CALL $6510 $6510
# CHECK bank_unresolved at 15D22 ($9D22 bank 5): CD 16 42  CALL $4216 $4216
# CHECK bank_unresolved at 15D5F ($9D5F bank 5): CD 68 40  CALL $4068 $4068
# CHECK bank_unresolved at 15E14 ($9E14 bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15E1B ($9E1B bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15E20 ($9E20 bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15E2A ($9E2A bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15E3A ($9E3A bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15E4C ($9E4C bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15E75 ($9E75 bank 5): C3 9D 6E  JP $6E9D $6E9D
# CHECK bank_unresolved at 15E88 ($9E88 bank 5): C3 9D 6E  JP $6E9D $6E9D
# CHECK bank_unresolved at 15EA1 ($9EA1 bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15EA5 ($9EA5 bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15EAA ($9EAA bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 15EAF ($9EAF bank 5): CD 9D 6E  CALL $6E9D $6E9D
# CHECK bank_unresolved at 186CE ($86CE bank 6): CD 32 42  CALL $4232 $4232
# CHECK bank_unresolved at 186D1 ($86D1 bank 6): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 186D7 ($86D7 bank 6): CD 5E 42  CALL $425E $425E
# CHECK bank_unresolved at 186FB ($86FB bank 6): C2 4B 42  JP NZ,$424B $424B
# CHECK bank_unresolved at 18704 ($8704 bank 6): CD 32 42  CALL $4232 $4232
# CHECK bank_unresolved at 18707 ($8707 bank 6): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 1870D ($870D bank 6): CD B3 6E  CALL $6EB3 $6EB3
# CHECK bank_unresolved at 18710 ($8710 bank 6): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 1871A ($871A bank 6): CA 72 60  JP Z,$6072 $6072
# CHECK bank_unresolved at 18743 ($8743 bank 6): CD A4 73  CALL $73A4 $73A4
# CHECK bank_unresolved at 1875A ($875A bank 6): CD 34 7B  CALL $7B34 $7B34
# CHECK bank_unresolved at 1875E ($875E bank 6): C3 A9 43  JP $43A9 $43A9
# CHECK bank_unresolved at 192BA ($92BA bank 6): CD 13 78  CALL $7813 $7813
# CHECK bank_unresolved at 192BF ($92BF bank 6): CD 06 78  CALL $7806 $7806
# CHECK bank_unresolved at 192E3 ($92E3 bank 6): CD 5F 7B  CALL $7B5F $7B5F
# CHECK bank_unresolved at 19A4D ($9A4D bank 6): CD 31 6D  CALL $6D31 $6D31
# Sites the scanner reaches only with the extra entry points listed in the header.
site 00E00   ; OUTI
site 00E02   ; OUTI
site 00E04   ; OUTI
site 00E06   ; OUTI
site 00E08   ; OUTI
site 00E0A   ; OUTI
site 00E0C   ; OUTI
site 00E0E   ; OUTI
site 0378C   ; OUT ($01),A
site 03791   ; IN A,($01)
site 037A5   ; OUT ($01),A
site 037AA   ; IN A,($01)
site 037BB   ; OUT ($01),A
site 0381B   ; IN A,($01)
site 0382B   ; OUT ($01),A
site 0382F   ; IN A,($01)
site 0383D   ; OUT ($01),A
site 03C1E   ; OUT ($BE),A
site 03C25   ; OUT ($BE),A
site 060EC   ; IN A,($BE)
site 060F5   ; OUT ($BE),A
site 060FC   ; OUT ($BE),A
site 066D5   ; OUT ($BE),A
site 066DD   ; OUT ($BE),A
site 06BBA   ; OUT ($BE),A
site 06BC8   ; OUT ($BE),A
maphl 06BF0   # LD (HL),$04, HL = $FFFF
site 06C71   ; OUT ($BE),A
site 06C77   ; OUT ($BE),A
otir 06E78   ; OUTI
site 06EA8   ; OUT ($BE),A
site 06EAF   ; OUT ($BE),A
site 06FD7   ; OUTI
site 06FDC   ; OUTI
site 07172   ; OUT ($BF),A
site 07177   ; OUT ($BF),A
site 0718A   ; OUT ($BE),A
site 07193   ; OUT ($BE),A
site 0719A   ; OUT ($BF),A
site 0719F   ; OUT ($BF),A
site 071A8   ; OUT ($BE),A
site 071AE   ; OUT ($BE),A
site 0CAFB   ; OUTI
site 0CB20   ; OUTI
site 153BB   ; OUT ($BF),A
site 153C0   ; OUT ($BF),A
site 153E2   ; OUT ($BE),A
site 153E9   ; OUT ($BE),A
site 153F9   ; OUT ($BF),A
site 153FE   ; OUT ($BF),A
site 15405   ; OUT ($BE),A
site 1540C   ; OUT ($BE),A
site 1543B   ; IN A,($BE)
site 15456   ; OUT ($BE),A
site 15461   ; OUT ($BE),A
site 15469   ; OUT ($BE),A
site 1549C   ; OUT ($BE),A
site 154A3   ; OUT ($BE),A
site 154B4   ; OUT ($BE),A
site 154BB   ; OUT ($BE),A
site 15F9E   ; OUT ($BF),A
site 15FA2   ; OUT ($BF),A
site 15FA8   ; OUT ($BF),A
site 15FAC   ; OUT ($BF),A
site 16084   ; OUT ($BF),A
site 16088   ; OUT ($BF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 04241   # LD ($FFFF),A; after LD A,$1A; 32 bytes of valid code before it
mapst 04247   # LD ($FFFF),A; after POP AF; JP/CALL target from $2FE86; 32 bytes of valid code before it
mapst 0628F   # LD ($FFFF),A; after LD A,$04; 32 bytes of valid code before it
mapst 062BC   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 06BDE   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
mapst 06DAD   # LD ($FFFF),A; after LD A,($C4ED); 32 bytes of valid code before it
mapst 06DBD   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
# CHECK byte scan medium: mapst 07283  LD ($FFFF),A  (32 bytes of valid code before it)
mapst 073EB   # LD ($FFFF),A; after LD A,$06; 32 bytes of valid code before it
# CHECK byte scan medium: mapst 080F8  LD ($FFFF),A  (32 bytes of valid code before it)
# CHECK byte scan medium: mapst 7C0F9  LD ($FFFF),A  (32 bytes of valid code before it)
# CHECK byte scan medium: mapst 7D817  LD ($FFFF),A  (32 bytes of valid code before it)
mapst 7D8AA   # LD ($FFFF),A; after LD A,($D9E1); 32 bytes of valid code before it
mapst 7D8B4   # LD ($FFFF),A; after LD A,($D9E4); 32 bytes of valid code before it
mapst 7D8BB   # LD ($FFFF),A; after POP AF; 32 bytes of valid code before it
# CHECK byte scan low: mapst 7DA18  LD ($FFFE),A  (after LD A,$01; 32 bytes of valid code before it; no valid code after it)
mapst 7DA69   # LD ($FFFF),A; after LD A,$02; 32 bytes of valid code before it
mapst 7DAD3   # LD ($FFFF),A; after LD A,$1A; 32 bytes of valid code before it
# CHECK byte scan medium: mapst 7DDF8  LD ($FFFF),A  (32 bytes of valid code before it)
# CHECK medium: site 0196E  OUT (C),E  (port in C; 32 bytes of valid code before it)
# CHECK low: site 01CF2  OUT (C),A  (port in C; 4 RST or NOP opcodes around it (looks like data); 17 bytes of valid code before it)
# CHECK low: site 07BC1  OUTI  (port in C; 11 bytes of valid code before it; no valid code after it)
# CHECK high: site 08001  OUT ($BF),A  (vdp_control; branch target from $08020; 32 bytes of valid code before it)
# CHECK high: site 08009  OUT ($BF),A  (vdp_control; after LD A,$81; 32 bytes of valid code before it)
# CHECK high: site 0800E  OUT ($C0),A  (no_effect; after LD A,$0C; 32 bytes of valid code before it)
# CHECK high: site 08019  OUT ($C0),A  (no_effect; after LD A,$08; 32 bytes of valid code before it)
# CHECK low: site 08024  OUT ($C0),A  (no_effect; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 08041  OUT ($C0),A  (no_effect; 13 bytes of valid code before it)
# CHECK medium: site 080C8  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 080E9  OUT ($C0),A  (no_effect; 17 bytes of valid code before it)
# CHECK medium: site 0813B  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 08154  OUT ($C0),A  (no_effect; 12 bytes of valid code before it)
# CHECK low: site 08167  OUT ($C0),A  (no_effect; 31 bytes of valid code before it; no valid code after it)
# CHECK medium: site 0817C  OUT ($C0),A  (no_effect; 11 bytes of valid code before it)
# CHECK medium: site 081C2  OUT ($C0),A  (no_effect; 9 bytes of valid code before it)
# CHECK medium: site 081DD  OUT ($C0),A  (no_effect; 11 bytes of valid code before it)
# CHECK low: site 081E7  OUT ($C0),A  (no_effect; 21 bytes of valid code before it; no valid code after it)
# CHECK medium: site 08201  OUT ($C0),A  (no_effect; 18 bytes of valid code before it)
# CHECK medium: site 0866A  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK low: site 0A5CC  IN A,($C1)  (joypad_b_misc; no evidence)
# CHECK low: site 10951  INDR  (port in C; 16 bytes of valid code before it; no valid code after it)
# CHECK medium: site 12C44  OUT ($F1),A  (fm_data; 32 bytes of valid code before it)
# CHECK medium: site 13418  OUT ($C0),A  (no_effect; 19 bytes of valid code before it)
# CHECK low: site 13F98  IN L,(C)  (port in C; no evidence)
# CHECK low: site 167C3  OUT ($3F),A  (io_control; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 1701C  OTDR  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK low: site 17285  IN A,($7E)  (v_counter; 27 bytes of valid code before it; no valid code after it)
# CHECK high: site 1749F  OUT (C),L  (port in C; branch target from $1747C; 32 bytes of valid code before it)
# CHECK low: site 18565  OUT ($BE),A  (vdp_data; no evidence)
# CHECK low: site 1BCD1  OUT ($BE),A  (vdp_data; no evidence)
# CHECK low: site 1BCDF  OUT ($BE),A  (vdp_data; no evidence)
# CHECK low: site 206C6  IN A,($3E)  (unmapped_read; no valid code after it)
# CHECK low: site 27ECB  IN A,($7F)  (h_counter; 16 bytes of valid code before it; no valid code after it)
# CHECK low: site 28929  IN A,($7F)  (h_counter; no evidence)
# CHECK low: site 2BF38  OTDR  (port in C; no evidence)
# CHECK low: site 2BF43  IN A,($7F)  (h_counter; no evidence)
# CHECK medium: site 2CCBF  IN A,($3F)  (unmapped_read; branch target from $2CC5D)
# CHECK medium: site 2D861  IN A,($7F)  (h_counter; 32 bytes of valid code before it)
# CHECK low: site 32B93  OUT ($C1),A  (no_effect; 24 bytes of valid code before it; no valid code after it)
# CHECK low: site 33317  OUT ($BF),A  (vdp_control; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 33571  OUT (C),L  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 33A97  OUTI  (port in C; 32 bytes of valid code before it)
# CHECK low: site 33EBF  OTDR  (port in C; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 36CEE  IN A,($3E)  (unmapped_read; 9 bytes of valid code before it)
# CHECK low: site 37242  OUT ($F0),A  (fm_address; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK high: site 38722  IN A,($C1)  (joypad_b_misc; branch target from $38700; 32 bytes of valid code before it)
# CHECK medium: site 38992  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK low: site 3B339  IN A,($C1)  (joypad_b_misc; no evidence)
# CHECK low: site 3FCC5  IN A,($7F)  (h_counter; no valid code after it)
# CHECK low: site 441D4  OUT ($C0),A  (no_effect; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 44C90  IN E,(C)  (port in C; 32 bytes of valid code before it)
# CHECK low: site 4BDAB  OUT ($7F),A  (psg; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 4E578  IN A,($C0)  (joypad_a; 30 bytes of valid code before it)
# CHECK medium: site 4E726  IN A,($BE)  (vdp_data; 32 bytes of valid code before it)
# CHECK low: site 5050E  OUT (C),E  (port in C; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 55EEC  IN H,(C)  (port in C; no evidence)
# CHECK medium: site 5A637  OUT ($C1),A  (no_effect; 15 bytes of valid code before it)
# CHECK medium: site 631A6  OUT ($F0),A  (fm_address; 16 bytes of valid code before it)
# CHECK low: site 6375A  OUT ($F1),A  (fm_data; no evidence)
# CHECK low: site 654C9  IN H,(C)  (port in C; no evidence)
# CHECK low: site 656A0  IN A,($3F)  (unmapped_read; no evidence)
# CHECK low: site 67F94  IN A,($DD)  (joypad_b_misc; 22 bytes of valid code before it; no valid code after it)
# CHECK low: site 6ADF1  IN A,($C0)  (joypad_a; 5 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 6C246  OUT ($BF),A  (vdp_control; no evidence)
# CHECK low: site 6C9AD  OUT ($3F),A  (io_control; 4 RST or NOP opcodes around it (looks like data); 24 bytes of valid code before it)
# CHECK medium: site 6CB62  IN A,($BF)  (vdp_status; 32 bytes of valid code before it)
# CHECK low: site 6CEE0  OUT ($C0),A  (no_effect; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 6EAD6  INIR  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 6ED62  OUT ($C1),A  (no_effect; 32 bytes of valid code before it)
# CHECK low: site 726CD  IN A,($F1)  (joypad_b_misc; 8 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 73A74  IN A,($BE)  (vdp_data; 4 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK medium: site 73C9F  OUT (C),A  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 74609  IN A,($C0)  (joypad_a; 32 bytes of valid code before it)
# CHECK low: site 776E1  IN A,(C)  (port in C; 12 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 77ACD  IN B,(C)  (port in C; no evidence)
# CHECK medium: site 77FBC  IN A,($BD)  (vdp_status; 32 bytes of valid code before it)
# CHECK low: site 7A56B  IN A,($BF)  (vdp_status; 6 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# CHECK low: site 7A79F  IN B,(C)  (port in C; no evidence)
# CHECK high: site 7C002  OUT ($BF),A  (vdp_control; branch target from $7C021; 20 bytes of valid code before it)
# CHECK high: site 7C00A  OUT ($BF),A  (vdp_control; after LD A,$81; 28 bytes of valid code before it)
# CHECK high: site 7C00F  OUT ($C0),A  (no_effect; after LD A,$0C; 32 bytes of valid code before it)
# CHECK high: site 7C01A  OUT ($C0),A  (no_effect; after LD A,$08; 32 bytes of valid code before it)
# CHECK low: site 7C025  OUT ($C0),A  (no_effect; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 7C042  OUT ($C0),A  (no_effect; 13 bytes of valid code before it)
# CHECK medium: site 7C0C9  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 7C0EA  OUT ($C0),A  (no_effect; 17 bytes of valid code before it)
# CHECK medium: site 7C13C  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 7C155  OUT ($C0),A  (no_effect; 12 bytes of valid code before it)
# CHECK low: site 7C168  OUT ($C0),A  (no_effect; 31 bytes of valid code before it; no valid code after it)
# CHECK medium: site 7C17D  OUT ($C0),A  (no_effect; 11 bytes of valid code before it)
# CHECK medium: site 7C1C3  OUT ($C0),A  (no_effect; 9 bytes of valid code before it)
# CHECK medium: site 7C1DE  OUT ($C0),A  (no_effect; 11 bytes of valid code before it)
# CHECK low: site 7C1E8  OUT ($C0),A  (no_effect; 21 bytes of valid code before it; no valid code after it)
# CHECK medium: site 7C202  OUT ($C0),A  (no_effect; 18 bytes of valid code before it)
# CHECK high: site 7DD01  OUT ($BF),A  (vdp_control; branch target from $7DCF7 $7DD20; 32 bytes of valid code before it)
# CHECK high: site 7DD09  OUT ($BF),A  (vdp_control; after LD A,$81; 32 bytes of valid code before it)
# CHECK high: site 7DD0E  OUT ($C0),A  (no_effect; after LD A,$04; 32 bytes of valid code before it)
# CHECK high: site 7DD19  OUT ($C0),A  (no_effect; after LD A,$00; branch target from $7DCFE; 32 bytes of valid code before it)
# CHECK low: site 7DD24  OUT ($C0),A  (no_effect; 32 bytes of valid code before it; no valid code after it)
# CHECK medium: site 7DD41  OUT ($C0),A  (no_effect; 13 bytes of valid code before it)
# CHECK medium: site 7DDC8  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 7DDE9  OUT ($C0),A  (no_effect; 17 bytes of valid code before it)
# CHECK medium: site 7DE3B  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 7DE54  OUT ($C0),A  (no_effect; 12 bytes of valid code before it)
# CHECK low: site 7DE67  OUT ($C0),A  (no_effect; 31 bytes of valid code before it; no valid code after it)
# CHECK medium: site 7DE7C  OUT ($C0),A  (no_effect; 11 bytes of valid code before it)
# CHECK medium: site 7DEC2  OUT ($C0),A  (no_effect; 32 bytes of valid code before it)
# CHECK medium: site 7DEDD  OUT ($C0),A  (no_effect; 11 bytes of valid code before it)
# CHECK low: site 7DEE7  OUT ($C0),A  (no_effect; 21 bytes of valid code before it; no valid code after it)
# CHECK medium: site 7DF01  OUT ($C0),A  (no_effect; 18 bytes of valid code before it)
# CHECK medium: site 7E04D  IN B,(C)  (port in C; 32 bytes of valid code before it)
# CHECK medium: site 7E4FF  OUT ($BD),A  (vdp_control; 32 bytes of valid code before it)
# CHECK low: site 7EF3F  OUT (C),C  (port in C; no valid code after it)
# CHECK medium: site 7F54B  OUT ($DD),A  (no_effect; 19 bytes of valid code before it)
# CHECK medium: site 7FF11  IN A,($DC)  (joypad_a; 26 bytes of valid code before it)
