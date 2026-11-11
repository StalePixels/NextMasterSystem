# Strider II (Europe, Brazil) (En), CRC32 B8F0915A, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output, then decided by hand. A 10-minute
# reference I/O log ran no I/O or mapper instruction that the scan does not find.
#
# Decisions:
# - No free RST vector: $0000-$0002 (DI; IM 1) becomes the io vector, and the game starts
#   at $0003, where it sets SP itself.
# - The frame handler $0038 only counts frames ($D45C). The line handler (register 10 =
#   $70 or $77) calls the sound driver through $7BA8; the driver is in bank 15, behind the
#   jump table at $8800.
# - Code in slot 2 runs only from bank 15 (the sound driver). The other banks the game maps
#   there (2-5, 10, 11, 13 and 14) are data.
# - The timing test $880F (bank 15) counts a loop over one frame and stores 1 in $D003 for
#   60 Hz, 0 for 50 Hz. At 28 MHz the count is always large, so $D003 is 0: right for
#   hz 50. Its ten HALTs are patched (below).
# - The jump table at $45B4 holds 4-byte records (a handler and a parameter word); the
#   scanner reads it as words, and the parameters ($0C00, $0B00, ...) lead it into data.
#   Those paths give the RST rows and the task-switch RETs at $0825-$1012. The jump into
#   RAM at $0448 is a decode from $0447, inside LD ($D486),A, not code.
# - Spec gaps (data/scan-verdicts.tsv): unused are the VRAM dump $025C, the colour write
#   $0286 and the random colour write $050A in bank 0, the bank-crossing tail $6910 in bank
#   1 and the timing loop $883A in bank 15, which nothing names; false are two byte
#   patterns in bank 3 data.
name Strider II
cart B8F0915A
hz 50		; No-Intro regions Europe, Brazil
vector 00 io
start 0003
# Start-up mapper writes $0012-$0020 (LD HL,$FFFC, then LD (HL),A with 0, 0, 1 and 2):
# the same values through the runtime. $0200, where the game goes next, sets A and HL.
asm 00012 15
    ld hl,$FFFC
    rst $00
    db $30
    inc l
    rst $00
    db $30
    inc l
    rst $00
    db $31
    inc l
    rst $00
    db $32
endasm
# Timing test $880F (bank 15): EI; LD B,$0A; HALT; DJNZ waits ten interrupts. The HALT ends
# on the runtime's own interrupts too, so each pass waits for the game's interrupt instead.
asm 3C80F 6
    ld b,$0A
.w: rst $00
    db eihalt_io
    djnz .w
endasm
# VRAM fill $023A (DE = VRAM address, HL = the word, BC = words) and VRAM copy $024E (DE =
# VRAM address, HL = source, BC = bytes), as native code in page 0 (entries vfill and vcopy).
# Through the traps the 16K fill $76E7 and the copies at the screen loads ran about 2 s for
# each black gap of the intro; the Master System takes about 0.7 s. $023E and $0252 stay as
# they are: $0593 and $0B5A call $023E directly. The cave is in the unused VRAM dump
# routine $025C.
asm 0023A 4    ; EX DE,HL; CALL $0279
    jp cave_fill
endasm
asm 0024E 4    ; EX DE,HL; CALL $0279
    jp cave_copy
endasm
label cave_fill 0025C
label cave_copy 00261
asm 0025C 10   ; unused VRAM dump routine $025C: cave_fill, then cave_copy
    rst $00
    db far_io, pg_vfill, ent_vfill
    ret
    rst $00
    db far_io, pg_vcopy, ent_vcopy
    ret
endasm
# Sprite tile upload $1B69-$1C57, as native code in page 0 (entry sprt), the same routine as
# Strider's $175B with its list at ($D498) and its VRAM address at ($D494). For each entry of
# the list (flag, bank - 2, source; $AA ends it) the game maps the bank at $FFFF and writes
# 32 bytes with OUTI (B = $40, counted down by both OUTI and DJNZ), or with a non-zero flag
# 32 bytes mirrored through the table at $0100.
asm 01B6F 5    ; LD C,$BF; LD HL,($D494)
    rst $00
    db far_io, pg_sprt, ent_sprt
    ret
endasm
page 0 sprt vfill vcopy
; sprt: B = the most tiles to write. Does what the game's code at $1B6F-$1C57 does, with the
; register sets as it leaves them: the control writes of VRAM address ($D494) through the
; runtime (C = $BF), interrupts on, DE = $20; then for each list entry, in the other register
; set: map the bank, and write 32 bytes from the source, or 32 bytes of the source through the
; table at $0100 (D = 1); back in the first set, HL += $20 and count B down. An entry $AA
; returns at once in the list's register set with A = $AA and Z set; when B reaches 0,
; ($D494) = HL. IX and IY are kept. Runs on the game's stack with interrupts on, as the game's
; code does; each jt_vwrite call keeps them off while it runs.
; Runtime entries used: the io RST (OUT (C),r and the mapper store $FFFF), jt_vwrite, jt_peek.
sprt:   di
        ld c,$BF
        ld hl,($D494)
        rst $00
        db $69                  ; OUT (C),L
        ld a,h
        set 6,a
        rst $00
        db $79                  ; OUT (C),A: port $BF
        ei
        ld a,h
        and $3F
        ld (vaddr+1),a
        ld a,l
        ld (vaddr),a
        ld de,$0020
.item:  exx
        ld hl,($D498)
        ld a,(hl)
        cp $AA
        ret z
        inc hl
        ld c,a
        ld a,(hl)
        inc hl
        add a,2
        rst $00
        db $13,0                ; LD ($FFFF),A
        ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld ($D498),hl
        ex de,hl
        ld a,c
        and a
        jr nz,.flip
        ld (sv_bc),bc           ; 32 bytes from the source as the game sees it
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld ix,32
        ld iy,32
        ld bc,$2001
        push de
        ld de,(vaddr)
        xor a
        call jt_vwrite
        pop de
        ld bc,32
        call vstep
        add hl,bc
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld bc,$00BE             ; as OUTI leaves it
        xor a
        exx
        add hl,de
        djnz .item
        ld ($D494),hl
        ret
.flip:  ld (sv_bc),bc           ; 32 bytes through the table at $0100
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld iy,buf
        ld d,1
        ld b,32
.fb:    ld a,h
        and $E0
        cp $20
        jr z,.fpk
        ld e,(hl)
        jr .fe
.fpk:   call jt_peek
        ld e,a
.fe:    ld a,(de)
        inc l
        ld (iy+0),a
        inc iy
        djnz .fb
        ld (sv_a),a
        push de
        push hl
        ld hl,buf
        ld de,(vaddr)
        ld ix,32
        ld iy,32
        ld bc,$2001
        ld a,1                  ; buf is in this page
        call jt_vwrite
        pop hl
        pop de
        ld bc,32
        call vstep
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld bc,(sv_bc)
        ld a,(sv_a)
        exx
        add hl,de
        dec b
        jp nz,.item
        ld ($D494),hl
        ret

; vstep: vaddr += BC. Keeps BC, DE, HL.
vstep:  push hl
        ld hl,(vaddr)
        add hl,bc
        ld a,h
        and $3F
        ld h,a
        ld (vaddr),hl
        pop hl
        ret

;
; vfill: DE = the VRAM address, HL = the word, BC = the number of words (not 0). Does what
; the game's $023A does: the control writes of address DE, then BC times the bytes L and H.
; Returns as the game's routine: HL = DE with bit 14 clear, DE = the word, BC = 0, A = 0,
; Z set, carry clear, interrupts on. The bytes go from fbuf, 256 at a time, with jt_vwrite;
; interrupts are on between the calls, as in the game's loop. Runs on the game's stack and
; uses only the return address of each call, as the game's routine does.
; Runtime entries used: jt_vwrite.
vfill:  di
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld (vf_v0),de
        ld (vf_v),de
        ld (vf_w),hl
        ld (vf_n),bc
        ld hl,fbuf
        ld de,(vf_w)
        ld b,128
.b:     ld (hl),e
        inc hl
        ld (hl),d
        inc hl
        djnz .b
        ei
.blk:   ld hl,(vf_n)
        ld a,h
        or a
        jr nz,.full
        ld a,l
        cp 128
        jr c,.rest
.full:  ld bc,128
        sbc hl,bc               ; carry is clear here
        ld (vf_n),hl
        ld b,0                  ; 256 bytes
        call vf_run
        jr .blk
.rest:  or a
        jr z,.end
        add a,a
        ld b,a
        call vf_run
.end:   ld hl,(vf_v0)
        res 6,h
        ld de,(vf_w)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld bc,0
        xor a
        ei
        ret

; vf_run: write B bytes (0 = 256) from fbuf to VRAM (vf_v), then vf_v += 256.
vf_run: ld hl,fbuf
        ld de,(vf_v)
        ld c,1
        ld ix,256
        ld iy,256
        ld a,1                  ; fbuf is in this page
        call jt_vwrite
        inc d
        ld (vf_v),de
        ret

; vcopy: DE = the VRAM address, HL = the source, BC = the number of bytes (not 0). Does what
; the game's $024E does: the control writes of address DE, then BC bytes from HL. Returns as
; the game's routine: HL = DE with bit 14 clear, DE = the source + BC, BC = 0, A = 0, Z set,
; carry clear, interrupts on. 256 bytes a jt_vwrite call, the source as the game sees it;
; interrupts are on between the calls. Runs on the game's stack as vfill does.
; Runtime entries used: jt_vwrite.
vcopy:  di
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld (vf_v0),de
        ld (vf_v),de
        ld (vf_s),hl
        ld (vf_n),bc
        ei
.blk:   ld hl,(vf_n)
        ld a,h
        or a
        jr z,.rest
        dec h
        ld (vf_n),hl
        ld b,0
        call vc_run
        jr .blk
.rest:  ld a,l
        or a
        jr z,.end
        ld b,a
        call vc_run
.end:   ld hl,(vf_v0)
        res 6,h
        ld de,(vf_s)
        ld ix,(sv_ix)
        ld iy,(sv_iy)
        ld bc,0
        xor a
        ei
        ret

; vc_run: write B bytes (0 = 256) from (vf_s) to VRAM (vf_v); both advance by B.
vc_run: ld hl,(vf_s)
        ld de,(vf_v)
        ld c,1
        ld ix,256
        ld iy,256
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,b
        or a
        jr nz,.part
        inc h
        inc d
        jr .st
.part:  ld c,b
        ld b,0
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
.st:    ld (vf_s),hl
        ld (vf_v),de
        ret

vf_v0:  dw 0
vf_v:   dw 0
vf_w:   dw 0
vf_n:   dw 0
vf_s:   dw 0
fbuf:   ds 256

vaddr:  dw 0
sv_bc:  dw 0
sv_ix:  dw 0
sv_iy:  dw 0
sv_a:   db 0
buf:    ds 32
endpage
site 00039   ; IN A,($BF)
site 0023F   ; OUT ($BE),A
site 00247   ; OUT ($BE),A
site 00253   ; OUT ($BE),A
site 0027D   ; OUT ($BF),A
site 00280   ; OUT ($BF),A
site 002A1   ; OUT ($BF),A
site 002A5   ; OUT ($BF),A
site 002AE   ; OUT ($BE),A
site 003CA   ; OUT ($3F),A
site 003CC   ; IN A,($DC)
site 0044A   ; IN A,($DD)
site 00463   ; IN A,($DD)
site 00481   ; IN A,($DD)
site 004BA   ; OTIR
site 004E6   ; OUT ($BF),A
site 004F0   ; OUT ($BF),A
site 00507   ; OUT ($BE),A
site 014C5   ; OUT ($BE),A
site 014CC   ; OUT ($BE),A
site 014D3   ; OUT ($BE),A
site 014DA   ; OUT ($BE),A
site 014E9   ; OUT ($BE),A
site 014F0   ; OUT ($BE),A
site 014F7   ; OUT ($BE),A
site 014FE   ; OUT ($BE),A
site 0169A   ; OUT ($BF),A
site 016A1   ; OUT ($BF),A
site 016A8   ; OUT ($BE),A
site 016B0   ; OUT ($BE),A
site 016C1   ; OUT ($BF),A
site 016C8   ; OUT ($BF),A
site 016CF   ; OUT ($BE),A
site 016D7   ; OUT ($BE),A
site 016EF   ; OUT ($BF),A
site 016F6   ; OUT ($BF),A
site 016FD   ; OUT ($BE),A
site 01705   ; OUT ($BE),A
site 01716   ; OUT ($BF),A
site 0171E   ; OUT ($BF),A
site 01725   ; OUT ($BE),A
site 0172D   ; OUT ($BE),A
site 017AB   ; OUT ($BF),A
site 017B2   ; OUT ($BF),A
site 017C5   ; OUT ($BE),A
site 017CD   ; OUT ($BE),A
site 017DA   ; OUT ($BF),A
site 017E1   ; OUT ($BF),A
site 017E8   ; OUT ($BE),A
site 017F0   ; OUT ($BE),A
site 017FD   ; OUT ($BF),A
site 01804   ; OUT ($BF),A
site 01816   ; OUT ($BE),A
site 0181E   ; OUT ($BE),A
site 0182D   ; OUT ($BF),A
site 01834   ; OUT ($BF),A
site 0183B   ; OUT ($BE),A
site 01843   ; OUT ($BE),A
site 01850   ; OUT ($BF),A
site 01857   ; OUT ($BF),A
site 01B75   ; OUT (C),L
site 01B7A   ; OUT ($BF),A
site 01BA0   ; OUTI
site 01BB1   ; OUT ($BE),A
site 01BB6   ; OUT ($BE),A
site 01BBB   ; OUT ($BE),A
site 01BC0   ; OUT ($BE),A
site 01BC5   ; OUT ($BE),A
site 01BCA   ; OUT ($BE),A
site 01BCF   ; OUT ($BE),A
site 01BD4   ; OUT ($BE),A
site 01BD9   ; OUT ($BE),A
site 01BDE   ; OUT ($BE),A
site 01BE3   ; OUT ($BE),A
site 01BE8   ; OUT ($BE),A
site 01BED   ; OUT ($BE),A
site 01BF2   ; OUT ($BE),A
site 01BF7   ; OUT ($BE),A
site 01BFC   ; OUT ($BE),A
site 01C01   ; OUT ($BE),A
site 01C06   ; OUT ($BE),A
site 01C0B   ; OUT ($BE),A
site 01C10   ; OUT ($BE),A
site 01C15   ; OUT ($BE),A
site 01C1A   ; OUT ($BE),A
site 01C1F   ; OUT ($BE),A
site 01C24   ; OUT ($BE),A
site 01C29   ; OUT ($BE),A
site 01C2E   ; OUT ($BE),A
site 01C33   ; OUT ($BE),A
site 01C38   ; OUT ($BE),A
site 01C3D   ; OUT ($BE),A
site 01C42   ; OUT ($BE),A
site 01C47   ; OUT ($BE),A
site 01C4C   ; OUT ($BE),A
site 01C5A   ; OUT ($BF),A
site 01C5E   ; OUT ($BF),A
site 01C68   ; OUTI
site 01C6A   ; OUTI
site 01C6C   ; OUTI
site 01C6E   ; OUTI
site 01C70   ; OUTI
site 01C72   ; OUTI
site 01C74   ; OUTI
site 01C76   ; OUTI
site 01C78   ; OUTI
site 01C7A   ; OUTI
site 01C7C   ; OUTI
site 01C7E   ; OUTI
site 01C80   ; OUTI
site 01C82   ; OUTI
site 01C84   ; OUTI
site 01C86   ; OUTI
site 01C88   ; OUTI
site 01C8A   ; OUTI
site 01C8C   ; OUTI
site 01C8E   ; OUTI
site 01C90   ; OUTI
site 01C92   ; OUTI
site 01C94   ; OUTI
site 01C96   ; OUTI
site 01C98   ; OUTI
site 01C9A   ; OUTI
site 01C9C   ; OUTI
site 01C9E   ; OUTI
site 01CA0   ; OUTI
site 01CA2   ; OUTI
site 01CA4   ; OUTI
site 01CA6   ; OUTI
site 01CA8   ; OUTI
site 01CAA   ; OUTI
site 01CAC   ; OUTI
site 01CAE   ; OUTI
site 01CB0   ; OUTI
site 01CB2   ; OUTI
site 01CB4   ; OUTI
site 01CB6   ; OUTI
site 01CB8   ; OUTI
site 01CBA   ; OUTI
site 01CBC   ; OUTI
site 01CBE   ; OUTI
site 01CC0   ; OUTI
site 01CC2   ; OUTI
site 01CC4   ; OUTI
site 01CC6   ; OUTI
site 01CC8   ; OUTI
site 01CCA   ; OUTI
site 01CCC   ; OUTI
site 01CCE   ; OUTI
site 01CD0   ; OUTI
site 01CD2   ; OUTI
site 01CD4   ; OUTI
site 01CD6   ; OUTI
site 01CD8   ; OUTI
site 01CDA   ; OUTI
site 01CDC   ; OUTI
site 01CDE   ; OUTI
site 01CE0   ; OUTI
site 01CE2   ; OUTI
site 01CE4   ; OUTI
site 01CE6   ; OUTI
site 01CE9   ; OUT ($BF),A
site 01CEC   ; OUT ($BF),A
site 01CEF   ; OUTI
site 01CF1   ; OUTI
site 01CF3   ; OUTI
site 01CF5   ; OUTI
site 01CF7   ; OUTI
site 01CF9   ; OUTI
site 01CFB   ; OUTI
site 01CFD   ; OUTI
site 01CFF   ; OUTI
site 01D01   ; OUTI
site 01D03   ; OUTI
site 01D05   ; OUTI
site 01D07   ; OUTI
site 01D09   ; OUTI
site 01D0B   ; OUTI
site 01D0D   ; OUTI
site 01D0F   ; OUTI
site 01D11   ; OUTI
site 01D13   ; OUTI
site 01D15   ; OUTI
site 01D17   ; OUTI
site 01D19   ; OUTI
site 01D1B   ; OUTI
site 01D1D   ; OUTI
site 01D1F   ; OUTI
site 01D21   ; OUTI
site 01D23   ; OUTI
site 01D25   ; OUTI
site 01D27   ; OUTI
site 01D29   ; OUTI
site 01D2B   ; OUTI
site 01D2D   ; OUTI
site 01D2F   ; OUTI
site 01D31   ; OUTI
site 01D33   ; OUTI
site 01D35   ; OUTI
site 01D37   ; OUTI
site 01D39   ; OUTI
site 01D3B   ; OUTI
site 01D3D   ; OUTI
site 01D3F   ; OUTI
site 01D41   ; OUTI
site 01D43   ; OUTI
site 01D45   ; OUTI
site 01D47   ; OUTI
site 01D49   ; OUTI
site 01D4B   ; OUTI
site 01D4D   ; OUTI
site 01D4F   ; OUTI
site 01D51   ; OUTI
site 01D53   ; OUTI
site 01D55   ; OUTI
site 01D57   ; OUTI
site 01D59   ; OUTI
site 01D5B   ; OUTI
site 01D5D   ; OUTI
site 01D5F   ; OUTI
site 01D61   ; OUTI
site 01D63   ; OUTI
site 01D65   ; OUTI
site 01D67   ; OUTI
site 01D69   ; OUTI
site 01D6B   ; OUTI
site 01D6D   ; OUTI
site 01D6F   ; OUTI
site 01D71   ; OUTI
site 01D73   ; OUTI
site 01D75   ; OUTI
site 01D77   ; OUTI
site 01D79   ; OUTI
site 01D7B   ; OUTI
site 01D7D   ; OUTI
site 01D7F   ; OUTI
site 01D81   ; OUTI
site 01D83   ; OUTI
site 01D85   ; OUTI
site 01D87   ; OUTI
site 01D89   ; OUTI
site 01D8B   ; OUTI
site 01D8D   ; OUTI
site 01D8F   ; OUTI
site 01D91   ; OUTI
site 01D93   ; OUTI
site 01D95   ; OUTI
site 01D97   ; OUTI
site 01D99   ; OUTI
site 01D9B   ; OUTI
site 01D9D   ; OUTI
site 01D9F   ; OUTI
site 01DA1   ; OUTI
site 01DA3   ; OUTI
site 01DA5   ; OUTI
site 01DA7   ; OUTI
site 01DA9   ; OUTI
site 01DAB   ; OUTI
site 01DAD   ; OUTI
site 01DAF   ; OUTI
site 01DB1   ; OUTI
site 01DB3   ; OUTI
site 01DB5   ; OUTI
site 01DB7   ; OUTI
site 01DB9   ; OUTI
site 01DBB   ; OUTI
site 01DBD   ; OUTI
site 01DBF   ; OUTI
site 01DC1   ; OUTI
site 01DC3   ; OUTI
site 01DC5   ; OUTI
site 01DC7   ; OUTI
site 01DC9   ; OUTI
site 01DCB   ; OUTI
site 01DCD   ; OUTI
site 01DCF   ; OUTI
site 01DD1   ; OUTI
site 01DD3   ; OUTI
site 01DD5   ; OUTI
site 01DD7   ; OUTI
site 01DD9   ; OUTI
site 01DDB   ; OUTI
site 01DDD   ; OUTI
site 01DDF   ; OUTI
site 01DE1   ; OUTI
site 01DE3   ; OUTI
site 01DE5   ; OUTI
site 01DE7   ; OUTI
site 01DE9   ; OUTI
site 01DEB   ; OUTI
site 01DED   ; OUTI
site 060F9   ; OUT ($BF),A
site 060FE   ; OUT ($BF),A
site 06104   ; OUT ($BE),A
site 0610A   ; OUT ($BE),A
site 06117   ; OUT ($BF),A
site 0611E   ; OUT ($BF),A
site 0614B   ; OUT ($BF),A
site 06150   ; OUT ($BF),A
site 06157   ; OUT ($BE),A
site 0615E   ; OUT ($BE),A
site 0616B   ; OUT ($BF),A
site 06172   ; OUT ($BF),A
site 061E7   ; OUT ($BF),A
site 061EE   ; OUT ($BF),A
site 061FA   ; OUT ($BE),A
site 06201   ; OUT ($BE),A
site 0620D   ; OUT ($BF),A
site 06212   ; OUT ($BF),A
site 06218   ; OUT ($BF),A
site 0621F   ; OUT ($BF),A
site 06228   ; OUT ($BE),A
site 0622F   ; OUT ($BE),A
site 0623C   ; OUT ($BF),A
site 06243   ; OUT ($BF),A
site 067A9   ; OUT ($BE),A
site 067AE   ; OUT ($BE),A
site 067B3   ; OUT ($BE),A
site 067B8   ; OUT ($BE),A
site 0681F   ; OUT ($BE),A
site 06826   ; OUT ($BE),A
site 0682B   ; OUT ($BE),A
site 06838   ; OUT ($BE),A
site 0684B   ; OUT ($BE),A
site 0687F   ; OUT ($BE),A
site 06886   ; OUT ($BE),A
site 0719A   ; OUT ($BE),A
site 071A0   ; OUT ($BE),A
site 0764D   ; OUT ($BE),A
site 07655   ; OUT ($BE),A
site 0765B   ; OUT ($BE),A
site 07663   ; OUT ($BE),A
site 07677   ; OUT ($BE),A
site 0767F   ; OUT ($BE),A
site 07685   ; OUT ($BE),A
site 0768D   ; OUT ($BE),A
site 076D7   ; OUT ($BE),A
site 076DF   ; OUT ($BE),A
site 07E65   ; OUT ($BF),A
site 07E68   ; OUT ($BF),A
site 07E6F   ; OUT ($BE),A
site 07F01   ; OUT ($BF),A
site 07F06   ; OUT ($BF),A
site 07F1E   ; OUT ($BE),A
site 07F24   ; OUT ($BE),A
site 3CC06   ; OUT ($7F),A
site 3CC0C   ; OUT ($7F),A
site 3CC17   ; OUT ($7F),A
site 3CC1E   ; OUT ($7F),A
site 3CC26   ; OUT ($7F),A
mapst 00206   ; LD ($FFFF),A
mapst 0029D   ; LD ($FFFF),A
mapst 00333   ; LD ($FFFF),A
mapst 0036D   ; LD ($FFFF),A
mapst 0040E   ; LD ($FFFF),A
mapst 00420   ; LD ($FFFF),A
mapst 0042B   ; LD ($FFFF),A
mapst 0043A   ; LD ($FFFF),A
mapst 006E2   ; LD ($FFFF),A
mapst 0148F   ; LD ($FFFF),A
mapst 01632   ; LD ($FFFF),A
mapst 01746   ; LD ($FFFF),A
mapst 018EC   ; LD ($FFFF),A
mapst 019AE   ; LD ($FFFF),A
mapst 01B09   ; LD ($FFFF),A
mapst 01B8E   ; LD ($FFFF),A
mapst 01E67   ; LD ($FFFF),A
mapst 0208E   ; LD ($FFFF),A
mapst 025F5   ; LD ($FFFF),A
mapst 02671   ; LD ($FFFF),A
mapst 02730   ; LD ($FFFF),A
mapst 02859   ; LD ($FFFF),A
mapst 0303B   ; LD ($FFFF),A
mapst 034B4   ; LD ($FFFF),A
mapst 037DC   ; LD ($FFFF),A
mapst 03AA8   ; LD ($FFFF),A
mapst 03E64   ; LD ($FFFF),A
mapst 041C6   ; LD ($FFFF),A
mapst 0424D   ; LD ($FFFF),A
mapst 048C6   ; LD ($FFFF),A
mapst 0491C   ; LD ($FFFF),A
mapst 04BE6   ; LD ($FFFF),A
mapst 04C3D   ; LD ($FFFF),A
mapst 05003   ; LD ($FFFF),A
mapst 0504D   ; LD ($FFFF),A
mapst 05A1A   ; LD ($FFFF),A
mapst 05B36   ; LD ($FFFF),A
mapst 066FD   ; LD ($FFFF),A
mapst 0672D   ; LD ($FFFF),A
mapst 06775   ; LD ($FFFF),A
mapst 067EE   ; LD ($FFFF),A
mapst 06860   ; LD ($FFFF),A
mapst 0689B   ; LD ($FFFF),A
mapst 068B0   ; LD ($FFFF),A
mapst 068E0   ; LD ($FFFF),A
mapst 06966   ; LD ($FFFF),A
mapst 069E1   ; LD ($FFFF),A
mapst 06BDA   ; LD ($FFFF),A
mapst 078AA   ; LD ($FFFF),A
mapst 07B4B   ; LD ($FFFF),A
mapst 07B77   ; LD ($FFFF),A
mapst 07B87   ; LD ($FFFF),A
mapst 07B8F   ; LD ($FFFF),A
mapst 07B9B   ; LD ($FFFF),A
mapst 07BA3   ; LD ($FFFF),A
mapst 07BAE   ; LD ($FFFF),A
mapst 07BBA   ; LD ($FFFF),A
mapst 07BC0   ; LD ($FFFF),A
mapst 07BC8   ; LD ($FFFF),A
mapst 07E36   ; LD ($FFFF),A
mapst 07E85   ; LD ($FFFF),A

# Strider II (Europe, Brazil).cht, "Infinite Lives": RAM $D4E8 is the lives count, held
# at 9
poke "Infinite lives"
ar 00D4-E809
endpoke

# Strider II (Europe, Brazil).cht, "Infinite Health": RAM $D4F2 is the energy gauge (the
# game fills it to $60), held at $7E
poke "Infinite energy"
ar 00D4-F27E
endpoke

# Strider II (Europe, Brazil).cht, "Invincibility": the cart byte at $55A5 (slot 1) becomes
# $C9 (RET), so the hit routine leaves at once and enemies do not hurt the player
poke "Invincibility"
gg C95-A5A-2A2
endpoke

# Strider II (Europe, Brazil).cht, "Infinite Time": RAM $D68D is the tens digit of the
# seconds on the clock, held at the tile for 7, so the clock never reaches 0:00
poke "Infinite time"
ar 00D6-8D37
endpoke
