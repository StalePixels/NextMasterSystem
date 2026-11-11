# Chuck Rock II - Son of Chuck (Europe), CRC32 C30E690A, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of the title and
# demo (300 s, no input) and random input (600 s).
# Code runs from banks 0 and 1 (slot 1 always holds bank 1); the banks the game maps into
# slot 2 hold data. The reset jumps to $7A80 and the frame interrupt to $7A35. The main loop
# ($7B08-$7BC2) does one game step every second frame.
# $D2C3 is 1 when the boot count of loop passes in one frame ($7AAF) is below $0720 (a 60 Hz
# machine); it is 1 on the 60 Hz reference and 0 on the Next.
# Byte scan patterns judged not patched (verdicts in data/scan-verdicts.tsv): stale bytes of a
# development build at $0069-$00C1 in bank 0 and a stale copy of the main loop at $7BC5-$7C35 in
# bank 1 (unused); an operand at $242E and $3225, and bytes in the data banks (false).
name Chuck Rock II
cart C30E690A
hz 50		; No-Intro region Europe
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00874   ; OUT ($BF),A
site 00879   ; OUT ($BF),A
site 008DF   ; OUT ($BE),A
site 00900   ; OUT ($BE),A
site 00B52   ; OUT ($BF),A
site 00B57   ; OUT ($BF),A
site 00B6C   ; OTIR
site 00B79   ; OUT ($BF),A
site 00B7D   ; OUT ($BF),A
site 00B8C   ; OUTI
site 00B9B   ; OUT ($BE),A
site 00BA6   ; OUT ($BF),A
site 00BAA   ; OUT ($BF),A
site 00BAF   ; OUTI
site 00BB2   ; OUTI
site 00BB9   ; OUT ($BF),A
site 00BBD   ; OUT ($BF),A
site 00BC2   ; OTIR
site 00BD3   ; OUTI
site 00BD5   ; OUTI
site 00BD8   ; OTIR
site 00C01   ; OUT ($BF),A
site 00C06   ; OUT ($BF),A
site 00C17   ; OUTI
site 00C97   ; OUT ($BF),A
site 00C9B   ; OUT ($BF),A
site 00CAB   ; OUT ($BF),A
site 00CAF   ; OUT ($BF),A
site 010F5   ; OUT ($7F),A
site 010F9   ; OUT ($7F),A
site 01112   ; OUT ($7F),A
site 01116   ; OUT ($7F),A
site 01126   ; OUT ($7F),A
site 0113D   ; OUT ($7F),A
site 0114A   ; OUT ($7F),A
site 01159   ; OUT ($7F),A
site 01170   ; OUT ($7F),A
site 0117D   ; OUT ($7F),A
site 0119E   ; OUT ($7F),A
site 011B1   ; OUT ($7F),A
site 011C8   ; OUT ($7F),A
site 011CE   ; OUT ($7F),A
site 011ED   ; OUT ($7F),A
site 01204   ; OUT ($7F),A
site 01211   ; OUT ($7F),A
site 0126E   ; OUT ($7F),A
site 01716   ; OUT ($BF),A
site 0171A   ; OUT ($BF),A
site 01720   ; OUTI
site 01728   ; OUT ($BF),A
site 0172C   ; OUT ($BF),A
site 01731   ; OUTI
site 01738   ; OUTI
site 0174A   ; OUT ($BF),A
site 0174E   ; OUT ($BF),A
site 0175A   ; OUTI
site 01766   ; OUT ($7F),A
site 0176A   ; OUT ($7F),A
site 0176E   ; OUT ($7F),A
site 01772   ; OUT ($7F),A
site 01784   ; IN A,($DC)
site 017A5   ; OUT ($BF),A
site 017A9   ; OUT ($BF),A
site 017B5   ; OUTI
site 01B37   ; OUT ($BF),A
site 01B3C   ; OUT ($BF),A
site 01B44   ; OUT ($BE),A
site 01B4B   ; OUT ($BE),A
site 01B52   ; OUT ($BE),A
site 01B59   ; OUT ($BE),A
site 01B60   ; OUT ($BF),A
site 01B65   ; OUT ($BF),A
site 01B6D   ; OUT ($BE),A
site 01B74   ; OUT ($BE),A
site 01B7B   ; OUT ($BE),A
site 01B82   ; OUT ($BE),A
site 01F87   ; OUT ($BF),A
site 01F8C   ; OUT ($BF),A
site 01F94   ; OUT ($BE),A
site 01F9B   ; OUT ($BE),A
site 01FA2   ; OUT ($BE),A
site 01FA9   ; OUT ($BE),A
site 01FB0   ; OUT ($BF),A
site 01FB5   ; OUT ($BF),A
site 01FBD   ; OUT ($BE),A
site 01FC4   ; OUT ($BE),A
site 01FCB   ; OUT ($BE),A
site 01FD2   ; OUT ($BE),A
site 02B67   ; OUT ($BF),A
site 02B6B   ; OUT ($BF),A
site 02B77   ; OUT ($BE),A
site 02B81   ; OUT ($BE),A
site 02B87   ; OUT ($BE),A
site 02B8B   ; OUT ($BF),A
site 02B8F   ; OUT ($BF),A
site 02B9B   ; OUT ($BE),A
site 02BA5   ; OUT ($BE),A
site 02BAB   ; OUT ($BE),A
site 02BD2   ; OUT ($BF),A
site 02BD6   ; OUT ($BF),A
site 02BDE   ; OTIR
site 0447B   ; OUTI
site 0447D   ; OUT ($BF),A
site 045F9   ; OUT ($BF),A
site 045FD   ; OUT ($BF),A
site 04609   ; OUTI
site 04665   ; OUT ($BF),A
site 04669   ; OUT ($BF),A
site 046BE   ; OUT ($BE),A
site 046C4   ; OUT ($BE),A
site 046CA   ; OUT ($BE),A
site 046D0   ; OUT ($BE),A
site 046EC   ; OUT ($BE),A
site 046F2   ; OUT ($BE),A
site 046F8   ; OUT ($BE),A
site 046FE   ; OUT ($BE),A
site 04732   ; OUT ($BE),A
site 04738   ; OUT ($BE),A
site 0473E   ; OUT ($BE),A
site 04744   ; OUT ($BE),A
site 04760   ; OUT ($BE),A
site 04766   ; OUT ($BE),A
site 0476C   ; OUT ($BE),A
site 04772   ; OUT ($BE),A
site 0478F   ; OUT ($BF),A
site 04794   ; OUT ($BF),A
site 0479B   ; OUT ($BE),A
site 04921   ; OUT ($BF),A
site 04925   ; OUT ($BF),A
site 0492B   ; OUT (C),A
site 04933   ; OUT ($BF),A
site 04937   ; OUT ($BF),A
site 04941   ; OUT ($BE),A
site 04947   ; OUT ($BE),A
site 04951   ; OUT (C),A
site 0497D   ; OUT ($BF),A
site 04981   ; OUT ($BF),A
site 049ED   ; OUT ($BF),A
site 049F0   ; OUT ($BF),A
site 04A06   ; OUT ($BE),A
site 04A0C   ; OUT ($BE),A
site 04A12   ; OUT ($BE),A
site 04A18   ; OUT ($BE),A
site 04A38   ; OUT ($BF),A
site 04A3B   ; OUT ($BF),A
site 04A52   ; OUT ($BE),A
site 04A58   ; OUT ($BE),A
site 04A5E   ; OUT ($BE),A
site 04A64   ; OUT ($BE),A
site 04BD8   ; IN A,($DC)
site 04CC4   ; IN A,($DC)
site 04DCA   ; IN A,($DC)
site 05138   ; IN A,($DC)
site 05177   ; OUT ($BF),A
site 0517B   ; OUT ($BF),A
site 05224   ; OUT ($BF),A
site 05228   ; OUT ($BF),A
site 05240   ; OUT ($BE),A
site 05246   ; OUT ($BE),A
site 0524C   ; OUT ($BE),A
site 05252   ; OUT ($BE),A
site 0526E   ; OUT ($BE),A
site 05274   ; OUT ($BE),A
site 0527A   ; OUT ($BE),A
site 05280   ; OUT ($BE),A
site 05332   ; OUT ($BF),A
site 05336   ; OUT ($BF),A
site 0537A   ; IN A,($DC)
site 05457   ; OUT ($BF),A
site 0545B   ; OUT ($BF),A
site 0549A   ; IN A,($DC)
site 054B5   ; IN A,($DC)
site 054BA   ; IN A,($DC)
site 0663F   ; IN A,($DD)
site 066AA   ; IN A,($DC)
site 066DF   ; IN A,($DD)
site 066E6   ; IN A,($DC)
site 06719   ; IN A,($DD)
site 06720   ; IN A,($DC)
site 06781   ; IN A,($DD)
site 06788   ; IN A,($DC)
site 067C0   ; IN A,($DC)
site 067D5   ; IN A,($DC)
site 067DF   ; IN A,($DD)
site 067E6   ; IN A,($DC)
site 0681D   ; IN A,($DC)
site 06832   ; IN A,($DD)
site 06839   ; IN A,($DC)
site 06878   ; OUT ($BF),A
site 0687C   ; OUT ($BF),A
site 06A94   ; OUT ($BE),A
site 06A9A   ; OUT ($BE),A
site 06AA0   ; OUT ($BE),A
site 06AA6   ; OUT ($BE),A
site 06AAC   ; OUT ($BE),A
site 06AB2   ; OUT ($BE),A
site 06AB8   ; OUT ($BE),A
site 06ABE   ; OUT ($BE),A
site 06AC4   ; OUT ($BE),A
site 06ACA   ; OUT ($BE),A
site 06AD0   ; OUT ($BE),A
site 06AD6   ; OUT ($BE),A
site 06ADC   ; OUT ($BE),A
site 06AE2   ; OUT ($BE),A
site 06AE8   ; OUT ($BE),A
site 06AEE   ; OUT ($BE),A
site 06AF4   ; OUT ($BE),A
site 06AFA   ; OUT ($BE),A
site 06B00   ; OUT ($BE),A
site 06B06   ; OUT ($BE),A
site 06B0C   ; OUT ($BE),A
site 06B12   ; OUT ($BE),A
site 06B18   ; OUT ($BE),A
site 06B1E   ; OUT ($BE),A
site 06B24   ; OUT ($BE),A
site 06B2A   ; OUT ($BE),A
site 06B30   ; OUT ($BE),A
site 06B36   ; OUT ($BE),A
site 06B3C   ; OUT ($BE),A
site 06B42   ; OUT ($BE),A
site 06B48   ; OUT ($BE),A
site 06B4E   ; OUT ($BE),A
site 06BCB   ; OUT ($BE),A
site 06BD1   ; OUT ($BE),A
site 06BD7   ; OUT ($BE),A
site 06BDD   ; OUT ($BE),A
site 06BE3   ; OUT ($BE),A
site 06BE9   ; OUT ($BE),A
site 06BEF   ; OUT ($BE),A
site 06BF5   ; OUT ($BE),A
site 06BFB   ; OUT ($BE),A
site 06C01   ; OUT ($BE),A
site 06C07   ; OUT ($BE),A
site 06C0D   ; OUT ($BE),A
site 06C13   ; OUT ($BE),A
site 06C19   ; OUT ($BE),A
site 06C1F   ; OUT ($BE),A
site 06C25   ; OUT ($BE),A
site 06C2B   ; OUT ($BE),A
site 06C31   ; OUT ($BE),A
site 06C37   ; OUT ($BE),A
site 06C3D   ; OUT ($BE),A
site 06C43   ; OUT ($BE),A
site 06C49   ; OUT ($BE),A
site 06C4F   ; OUT ($BE),A
site 06C55   ; OUT ($BE),A
site 06C5B   ; OUT ($BE),A
site 06C61   ; OUT ($BE),A
site 06C67   ; OUT ($BE),A
site 06C6D   ; OUT ($BE),A
site 06C73   ; OUT ($BE),A
site 06C79   ; OUT ($BE),A
site 06C7F   ; OUT ($BE),A
site 06C85   ; OUT ($BE),A
site 06E6D   ; OUT ($BF),A
site 06E79   ; OUT ($BF),A
site 07742   ; OUT ($BF),A
site 07746   ; OUT ($BF),A
site 07753   ; OUTI
site 077FB   ; IN A,($DC)
site 07801   ; IN A,($DC)
site 07807   ; IN A,($DC)
site 07A37   ; IN A,($BF)
site 07B08   ; IN A,($DD)
mapst 00004   ; LD ($FFFC),A
mapst 00007   ; LD ($FFFD),A
mapst 0000B   ; LD ($FFFE),A
mapst 00B05   ; LD ($FFFF),A
mapst 00B40   ; LD ($FFFF),A
mapst 00B5D   ; LD ($FFFF),A
mapst 00BE0   ; LD ($FFFF),A
mapst 00FA6   ; LD ($FFFF),A
mapst 0108D   ; LD ($FFFF),A
mapst 010A0   ; LD ($FFFF),A
mapst 01740   ; LD ($FFFF),A
mapst 0179C   ; LD ($FFFF),A
mapst 01A7C   ; LD ($FFFF),A
mapst 01B10   ; LD ($FFFF),A
mapst 01BB8   ; LD ($FFFF),A
mapst 01F60   ; LD ($FFFF),A
mapst 021B8   ; LD ($FFFF),A
mapst 03240   ; LD ($FFFF),A
mapst 0337E   ; LD ($FFFF),A
mapst 045F0   ; LD ($FFFF),A
mapst 04616   ; LD ($FFFF),A
mapst 0462A   ; LD ($FFFF),A
mapst 04670   ; LD ($FFFF),A
mapst 048AE   ; LD ($FFFF),A
mapst 048EF   ; LD ($FFFF),A
mapst 0496B   ; LD ($FFFF),A
mapst 049B3   ; LD ($FFFF),A
mapst 049DA   ; LD ($FFFF),A
mapst 0516E   ; LD ($FFFF),A
mapst 051AD   ; LD ($FFFF),A
mapst 05329   ; LD ($FFFF),A
mapst 05368   ; LD ($FFFF),A
mapst 05445   ; LD ($FFFF),A
mapst 0548D   ; LD ($FFFF),A
mapst 054C4   ; LD ($FFFF),A
mapst 06034   ; LD ($FFFF),A
mapst 061DD   ; LD ($FFFF),A
mapst 0639A   ; LD ($FFFF),A
mapst 064C2   ; LD ($FFFF),A
mapst 06524   ; LD ($FFFF),A
mapst 0654D   ; LD ($FFFF),A
mapst 066B4   ; LD ($FFFF),A
mapst 06866   ; LD ($FFFF),A
mapst 068AA   ; LD ($FFFF),A
mapst 06D62   ; LD ($FFFF),A
mapst 06F7A   ; LD ($FFFF),A
mapst 07186   ; LD ($FFFF),A
mapst 07738   ; LD ($FFFF),A
mapst 078EB   ; LD ($FFFF),A
mapst 07A6A   ; LD ($FFFF),A
mapst 07A73   ; LD ($FFFF),A
# Native routines of the object script interpreter ($73DB: one script byte selects a routine
# through the table at $0700). The scripts, in the data banks, name these routines directly, so
# no static path reaches them; the recordings ran $3240 and $337E.
mapst 02996   ; LD ($FFFF),A
mapst 031A2   ; LD ($FFFF),A
mapst 031F3   ; LD ($FFFF),A
mapst 03240   ; LD ($FFFF),A
mapst 0337E   ; LD ($FFFF),A
mapst 033B0   ; LD ($FFFF),A
mapst 034B3   ; LD ($FFFF),A
mapst 03591   ; LD ($FFFF),A
mapst 0359C   ; LD ($FFFF),A
# Joypad reads in object code that the scan does not reach: $5631 (a routine that $562A sets
# into the pointer at $DA80) and $797D (an object handler).
site 05638   ; IN A,($DC)
site 07984   ; IN A,($DC)
site 07991   ; IN A,($DC)
site 0799E   ; IN A,($DC)
site 079A7   ; IN A,($DC)

# The object sprite writer ($6A2B, called from the object drawers, for example $6DD9, with the
# object's graphics bank in slot 2) writes each sprite's tiles at the VDP address that runs on
# from one sprite to the next, every game step, with interrupts on: one 32-byte tile each, with
# LD BC,$40BE : OUTI : NOP : DJNZ ($6A7B, $6BB2, $6D19; OUTI and DJNZ both take one from B), or
# unrolled, each byte mapped through the table at $0100 in bank 0 ($6A8D, $6BC4). The runtime converts every tile written,
# changed or not, and most sprites show the same tiles from one step to the next; in busy
# scenes the writes alone took about a third of a frame and the game fell behind the Master
# System's pace. Each write becomes a far call to page 0, which writes only the 32-byte tiles
# that differ from the VRAM copy. No game code enters the loops past their first instruction.
asm 06A7B 8    ; LD BC,$40BE : OUTI : NOP : DJNZ $6A7E
    rst $00
    db far_io, pg_spt, ent_spt
    jp $6A83
endasm
asm 06BB2 8    ; LD BC,$40BE : OUTI : NOP : DJNZ $6BB5
    rst $00
    db far_io, pg_spt, ent_spt
    jp $6BBA
endasm
asm 06D19 8    ; LD BC,$40BE : OUTI : NOP : DJNZ $6D1C
    rst $00
    db far_io, pg_spt, ent_spt
    jp $6D21
endasm
asm 06A8D 7    ; PUSH DE : LD D,$01 : LD E,(HL) : INC HL : LD A,(DE) : NOP
    rst $00
    db far_io, pg_spm, ent_spm
    jp $6B51
endasm
asm 06BC4 7    ; PUSH DE : LD D,$01 : LD E,(HL) : INC HL : LD A,(DE) : NOP
    rst $00
    db far_io, pg_spm, ent_spm
    jp $6C88
endasm
# The name table update list writer $0BC5 (the frame handler at $7A5A, and $6658 and $7798):
# the list at $DD78 holds entries of a count N, a VDP address (low, high) and 2N bytes, and
# ends with $FF; each entry goes as two OUTI to the control port and an OTIR of 2N bytes to
# the data port. Through the runtime's traps a frame with many entries (the view scrolling)
# spent about half a frame here. It becomes a far call to page 0, ntl, which writes each VRAM
# entry with one jt_vwrite. No game code enters the routine past its first instruction.
asm 00BC5 7    ; LD D,$BF : LD E,$BE : LD HL,$DD78
    rst $00
    db far_io, pg_ntl, ent_ntl
    ret
endasm
page 0 spt spm ntl
; spt: in HL = a 32-byte tile (in slot 2). Out as the game's loop leaves them for the code
; after it: HL past the bytes, BC = $00BE; DE, IX, IY, the alternate registers and the
; interrupt state kept.
; spm: in HL = 32 bytes, each an index into the table at $0100 in bank 0 (slot 0); writes the
; 32 table bytes. Out: HL past the bytes; DE, IX, IY, the alternate registers and the
; interrupt state kept.
; Both turn interrupts off (slot 0 holds the VRAM copy while they compare) and run on a stack
; of their own in the page.
; Runtime internals used: jt_vwrite, vdp_latch, vdp_code, vdp_addr, vdp_rbuf, cur_mmu, and
; SHADOW_PAGE 28-29 (the VRAM copy, mapped into slot 0 while put compares).
spt:    ld a,i                  ; P/V = IFF2, kept by LD and DI
        di
        ld a,0
        jp po,.ioff
        inc a
.ioff:  ld (v_iff),a
        ld (v_ssp),sp
        ld sp,stk
        push de
        push ix
        push iy
        ld bc,32
        xor a                   ; the source as the game sees it
        call put
        pop iy
        pop ix
        pop de
        ld bc,$00BE
        jp exit

spm:    ld a,i
        di
        ld a,0
        jp po,.ioff
        inc a
.ioff:  ld (v_iff),a
        ld (v_ssp),sp
        ld sp,stk
        push de
        push ix
        push iy
        ld de,v_buf
        ld b,32
.m:     ld a,(hl)
        inc hl
        push hl
        ld l,a
        ld h,$01                ; the table at $0100, in the game's slot 0
        ld a,(hl)
        pop hl
        ld (de),a
        inc de
        djnz .m
        push hl
        ld hl,v_buf
        ld bc,32
        ld a,1                  ; the source as mapped now: v_buf
        call put
        pop hl
        pop iy
        pop ix
        pop de
exit:   ld sp,(v_ssp)
        ld a,(v_iff)
        or a
        ret z
        ei
        ret

; ntl: writes the list at $DD78 (entries: count N, VDP address low and high, 2N bytes; $FF
; ends it). An entry whose address is a VRAM write goes with one jt_vwrite; any other entry
; goes as the game's routine sends it, with OTIR through the runtime (2 bytes to the control
; port, then the data). Out as the game's routine leaves them: A kept, B = 0, C = $BE, D = $BF,
; E = $BE, HL at the $FF, Z set; IX, IY and the interrupt state kept. Runs with interrupts
; off, on a stack of its own in the page.
ntl:    ld (v_a),a
        ld a,i
        di
        ld a,0
        jp po,.ioff
        inc a
.ioff:  ld (v_iff),a
        ld (v_ssp),sp
        ld sp,stk
        push ix
        push iy
        ld hl,$DD78
.en:    ld a,(hl)
        cp $FF
        jr z,.end
        inc hl
        add a,a                 ; B = 2N, modulo 256 (0 = 256), as SLA B
        ld b,a
        inc hl
        ld a,(hl)               ; the address high byte: code in bits 6-7
        dec hl
        and $C0
        cp $40
        jr nz,.slow
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld c,1
        ld ix,256
        ld iy,256
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,b                  ; HL past the bytes
        or a
        jr z,.n256
        add a,l
        ld l,a
        jr nc,.en
        inc h
        jr .en
.n256:  inc h
        jr .en
.slow:  push bc
        ld bc,$02BF             ; the address through the runtime
        rst $00
        db $B3
        pop bc
        ld c,$BE                ; the bytes
        rst $00
        db $B3
        jr .en
.end:   pop iy
        pop ix
        ld bc,$00BE
        ld de,$BFBE
        ld sp,(v_ssp)
        ld a,(v_iff)
        or a
        jr z,.di
        cp a                    ; Z set
        ld a,(v_a)
        ei
        ret
.di:    cp a
        ld a,(v_a)
        ret

; put: BC bytes (32 or 64) from HL to VRAM at the VDP address; A = the source mode for
; jt_vwrite. Each 32-byte tile is compared with the VRAM copy and written only if it differs;
; the VDP address, code, latch and read buffer are then set as the game's writes leave them.
; Anything else (an address not on a tile, the VDP not in a VRAM write, a source below $4000
; read as the game sees it) is written whole. Out: HL past the bytes; AF, BC, DE, IX and IY
; changed.
put:    ld (v_mode),a
        ld (v_n),bc
        or a
        jr nz,.src
        ld a,h
        cp $40
        jp c,.all
.src:   ld a,(vdp_latch)
        or a
        jp nz,.all
        ld a,(vdp_code)
        cp 1
        jp nz,.all
        ld de,(vdp_addr)
        ld a,e
        and $1F
        jp nz,.all
        ld a,c                  ; pieces of 32 bytes
        rlca
        rlca
        rlca
        and 7
        ld b,a
.pc:    push bc
        ld a,d
        and $3F
        ld d,a
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        db $ED,$92,$50          ; nextreg $50,a: this tile's VRAM copy in slot 0
        push hl
        push de
        ld a,d
        and $1F
        ld d,a
        ld b,32
.cm:    ld a,(de)
        cp (hl)
        jr nz,.df
        inc hl
        inc de
        djnz .cm
        pop de                  ; the same: not written
        pop hl
        jr .nx
.df:    pop de
        pop hl
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0
        ld bc,$2001             ; one run of 32 bytes
        ld ix,32
        ld iy,32
        ld a,(v_mode)
        call jt_vwrite
.nx:    ld bc,32
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        pop bc
        djnz .pc
        ld a,(cur_mmu)
        db $ED,$92,$50          ; nextreg $50,a: the game's slot 0
        ld a,d                  ; the VDP state after the game's writes
        and $3F
        ld d,a
        ld (vdp_addr),de
        ld a,1
        ld (vdp_code),a
        xor a
        ld (vdp_latch),a
        dec hl
        ld a,(hl)
        ld (vdp_rbuf),a
        inc hl
        ret
.all:   ld de,(vdp_addr)
        ld a,(v_n)
        ld b,a
        ld c,1
        ld ix,64
        ld iy,64
        ld a,(v_mode)
        call jt_vwrite
        ld bc,(v_n)
        add hl,bc
        ret

v_iff:  db 0
v_a:    db 0
v_mode: db 0
v_ssp:  dw 0
v_n:    dw 0
v_buf:  ds 32
        ds 64
stk:
endpage

# Chuck Rock II - Son of Chuck (Europe).cht, "Infinite Lives": the code changes the store
# of the decremented life counter ($DD5C) at $5B67 into a load, so a life is never taken
poke "Infinite lives"
gg 3AB-67A-2A2
endpoke

# Chuck Rock II - Son of Chuck (Europe).cht, "Infinite Health": the code changes the store
# of the decremented health counter ($DD5D) at $5B17 into a load, so health never drops
poke "Infinite health"
gg 3AB-17A-2A2
endpoke

# Chuck Rock II - Son of Chuck (Europe).cht, "Invulnerability" (first code): the test of
# the hit timer ($DD5E) at $1E8E no longer sets the flags, so the hit routine is skipped
poke "Invulnerability"
gg 00E-8EE-3B4
endpoke
