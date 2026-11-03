# Cosmic Spacehead, drafted by tools/mkspec.py from sitescan output.
name Cosmic Spacehead
cart 29822980
hz 50		; No-Intro regions Europe
# No free RST vector: the cart starts NOP; DI; IM 1; LD SP,$DFA0 and $0003-$0037
# is mostly unused. $0000-$0002 becomes the vector; the game starts at $0004
# with SP $DFA0 (the runtime starts it in IM 2).
vector 00 io
start 0004 DFA0
asm 0031A 2   ; IM 1 -> IM 2
    im 2
endasm
codem 00267   ; LD ($8000),A
codem 00275   ; LD ($0000),A
codem 00279   ; LD ($4000),A
codem 0027D   ; LD ($8000),A
codem 034BF   ; LD ($8000),A
codem 03C3D   ; LD ($8000),A
# At power-on the game unpacks code from $B610 to RAM $C000-$CD6F (its routine
# at $B4CA, CALL at $0013) and jumps to it ($0023: JP $C000). The reference log
# shows parts of it running after the start too. Page 0 makes it use the
# runtime: the cave at $0023 calls ram_patch, which checks the image and writes
# the I/O RST with its inline code over each of its 138 I/O instructions, and a
# JP to a cave below over each of its four HALTs. A different image stops the
# game (jt_fatal).
asm 00023 7    ; JP $C000 (and 4 unused bytes)
    rst $00
    db far_io, pg_ram_patch, ent_ram_patch
    jp $C000
endasm
# The RAM image's HALTs, from the JPs that ram_patch writes over them:
# $C04A and $C3AF (HALT : DJNZ, then on to $C04D), $C030 (HALT : LD A,$72),
# $C46F (HALT : LD A,$80). Bank 0 $3FAE-$3FFF is unused (zero bytes no code reaches).
label hwait 03FC0
label h72 03FC7
label h80 03FCE
asm 03FC0 21
    rst $00
    db halt_io
    djnz $3FC0
    jp $C04D
    rst $00
    db halt_io
    ld a,$72
    jp $C033
    rst $00
    db halt_io
    ld a,$80
    jp $C472
endasm
page 0 ram_patch
; ram_patch: from the cave at $0023, after the unpack. Checks the 3440 bytes
; from $C000 (two 16-bit sums, as Fantastic Dizzy's logo_patch), then writes
; RST $00 and the inline code over each I/O instruction in io_at (OUT (n),A:
; the port class; IN A,(n): 8 + the class; ED xx: xx), and JP nn over each
; HALT in jps. Keeps BC, DE, HL, IX; A, F change.
ram_patch:
        push bc
        push de
        push hl
        push ix
        ld hl,$C000
        ld bc,3440
        ld de,0
        ld ix,0
.ck:    ld a,(hl)
        add a,e
        ld e,a
        jr nc,.ck1
        inc d
.ck1:   add ix,de
        inc hl
        dec bc
        ld a,b
        or c
        jr nz,.ck
        ld hl,$D32C
        or a
        sbc hl,de
        jr nz,.bad
        push ix
        pop hl
        ld de,$BA6D
        sbc hl,de
        jr nz,.bad
        ld hl,io_at
.io:    ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,d
        or e
        jr z,.jps
        ld a,(de)
        inc de
        cp $ED
        jr z,.ed
        ld c,a
        ld a,(de)               ; the port
        ld b,0
        rla                     ; A7
        rl b
        rla                     ; A6
        rl b
        ld a,(de)
        rra                     ; A0
        rl b                    ; B = A7 A6 A0
        ld a,c
        cp $D3
        jr z,.out
        cp $DB
        jr nz,.bad
        ld a,8
        add a,b
        ld b,a
.out:   ld a,b
        jr .put
.ed:    ld a,(de)
.put:   dec de
        ex de,hl
        ld (hl),$C7             ; RST $00
        inc hl
        ld (hl),a
        ex de,hl
        jr .io
.jps:   ld hl,jps
.jp:    ld e,(hl)
        inc hl
        ld d,(hl)
        inc hl
        ld a,d
        or e
        jr z,.done
        ld a,(de)
        cp $76
        jr nz,.bad
        ld a,$C3
        ld (de),a
        inc de
        ldi
        ldi
        jr .jp
.done:  pop ix
        pop hl
        pop de
        pop bc
        ret
.bad:   jp jt_fatal
jps:    dw $C04A, hwait
        dw $C3AF, hwait
        dw $C030, h72
        dw $C46F, h80
        dw 0
io_at:
        dw $C033,$C037,$C03B,$C03E,$C07C,$C080,$C08C,$C090,$C097,$C09B,$C0BE,$C0C1
        dw $C0C5,$C0D9,$C0E6,$C0EA,$C0FE,$C101,$C105,$C109,$C10D,$C112,$C11B,$C11F
        dw $C123,$C127,$C12C,$C131,$C135,$C13E,$C141,$C143,$C145,$C156,$C158,$C15A
        dw $C15C,$C16B,$C16D,$C16F,$C171,$C179,$C17D,$C185,$C189,$C190,$C199,$C19D
        dw $C1A3,$C1A6,$C1AE,$C1B2,$C1B8,$C1BB,$C1C3,$C1C7,$C1CD,$C1D1,$C1D8,$C1DC
        dw $C1E1,$C1E5,$C1EC,$C1F0,$C1F4,$C1F8,$C1FC,$C200,$C20C,$C214,$C218,$C21E
        dw $C221,$C22D,$C233,$C237,$C23D,$C240,$C24C,$C24F,$C26C,$C270,$C2AA,$C2AE
        dw $C2B2,$C2B5,$C2D6,$C2DA,$C2DE,$C2E1,$C309,$C30D,$C311,$C314,$C31E,$C322
        dw $C332,$C335,$C339,$C33C,$C340,$C344,$C348,$C34B,$C34E,$C351,$C364,$C368
        dw $C372,$C379,$C386,$C38A,$C394,$C39B,$C39F,$C3A3,$C3A5,$C3BF,$C3C3,$C3CD
        dw $C3D4,$C3E1,$C3E5,$C3EF,$C3F6,$C3FA,$C3FE,$C402,$C406,$C40A,$C472,$C476
        dw $C481,$C485,$C48A,$C48D,$C490,$C495
        dw 0
endpage
site 0006F   ; OUT ($BF),A
site 00073   ; OUT ($BF),A
site 0008B   ; OUT ($BE),A
site 000A8   ; OTIR
site 000B3   ; OUT ($BE),A
site 000B7   ; OUT ($BE),A
site 000BE   ; OUT ($BE),A
site 000C2   ; OUT ($BE),A
site 000C9   ; OUT ($BE),A
site 000CD   ; OUT ($BE),A
site 000D4   ; OUT ($BE),A
site 000D8   ; OUT ($BE),A
site 001DB   ; IN A,($BF)
site 002AD   ; OUT ($BF),A
site 002B1   ; OUT ($BF),A
site 002B8   ; OUT ($BE),A
site 00507   ; OUT ($BF),A
site 00512   ; OUT ($BF),A
site 00519   ; OUT ($BF),A
site 00520   ; OUT ($BF),A
site 0052A   ; OUT ($BF),A
site 0052E   ; OUT ($BF),A
site 019E7   ; OUT ($BF),A
site 019EB   ; OUT ($BF),A
site 019F8   ; OUT ($BF),A
site 019FC   ; OUT ($BF),A
site 02763   ; IN A,($7E)
site 02B0C   ; OUT ($BF),A
site 02B10   ; OUT ($BF),A
site 02B1C   ; OUT ($BF),A
site 02B20   ; OUT ($BF),A
site 02B28   ; OUTI
site 02B2A   ; OUTI
site 02B2C   ; OUTI
site 02B2E   ; OUTI
site 02B30   ; OUTI
site 02B32   ; OUTI
site 02B34   ; OUTI
site 02B36   ; OUTI
site 02B38   ; OUTI
site 02B3A   ; OUTI
site 02B3C   ; OUTI
site 02B3E   ; OUTI
site 02B40   ; OUTI
site 02B42   ; OUTI
site 02B44   ; OUTI
site 02B46   ; OUTI
site 02B48   ; OUTI
site 02B4A   ; OUTI
site 02B4C   ; OUTI
site 02B4E   ; OUTI
site 02B50   ; OUTI
site 02B52   ; OUTI
site 02B54   ; OUTI
site 02B56   ; OUTI
site 02B58   ; OUTI
site 02B5A   ; OUTI
site 02B5C   ; OUTI
site 02B5E   ; OUTI
site 02B60   ; OUTI
site 02B62   ; OUTI
site 02B64   ; OUTI
site 02B66   ; OUTI
site 02B68   ; OUTI
site 02B6A   ; OUTI
site 02B6C   ; OUTI
site 02B6E   ; OUTI
site 02B70   ; OUTI
site 02B72   ; OUTI
site 02B74   ; OUTI
site 02B76   ; OUTI
site 02B78   ; OUTI
site 02B7A   ; OUTI
site 02B7C   ; OUTI
site 02B7E   ; OUTI
site 02B80   ; OUTI
site 02B82   ; OUTI
site 02B84   ; OUTI
site 02B86   ; OUTI
site 02B88   ; OUTI
site 02B8A   ; OUTI
site 02B8C   ; OUTI
site 02B8E   ; OUTI
site 02B90   ; OUTI
site 02B92   ; OUTI
site 02B94   ; OUTI
site 02B96   ; OUTI
site 02B98   ; OUTI
site 02B9A   ; OUTI
site 02B9C   ; OUTI
site 02B9E   ; OUTI
site 02BA0   ; OUTI
site 02BA2   ; OUTI
site 02BA4   ; OUTI
site 02BA6   ; OUTI
site 02D1E   ; OUT ($BF),A
site 02D23   ; OUT ($BF),A
site 02D3B   ; OUT ($BE),A
site 02D45   ; OUT ($BF),A
site 02D4F   ; OUT ($BF),A
site 02D66   ; OUTI
site 02D68   ; OUT ($BE),A
site 02D6A   ; OUTI
site 02D6C   ; OUT ($BE),A
site 02D6E   ; OUTI
site 02D70   ; OUT ($BE),A
site 02D72   ; OUTI
site 02D74   ; OUT ($BE),A
site 02D76   ; OUTI
site 02D78   ; OUT ($BE),A
site 02D7A   ; OUTI
site 02D7C   ; OUT ($BE),A
site 02D7E   ; OUTI
site 02D80   ; OUT ($BE),A
site 02D82   ; OUTI
site 02D84   ; OUT ($BE),A
site 02D86   ; OUTI
site 02D88   ; OUT ($BE),A
site 02D8A   ; OUTI
site 02D8C   ; OUT ($BE),A
site 02D99   ; OUT ($BE),A
site 02D9B   ; OUT (C),D
site 02DAD   ; OTIR
site 02DC3   ; OUTI
site 02DC6   ; OUT ($BF),A
site 02DC8   ; OUTI
site 02DCB   ; OUT ($BF),A
site 02DCD   ; OUTI
site 02DE4   ; OUTI
site 02DE7   ; OUT ($BF),A
site 02DE9   ; OUTI
site 02DEC   ; OUT ($BF),A
site 02DEE   ; OUTI
site 02DF2   ; OUT ($BF),A
site 02DF4   ; OUTI
site 02DF7   ; OUT ($BF),A
site 02DFC   ; OUT ($BF),A
site 02DFE   ; OUTI
site 02E01   ; OUT ($BF),A
site 02E03   ; OUTI
site 02E06   ; OUT ($BF),A
site 02E08   ; OUTI
site 02E0C   ; OUT ($BF),A
site 02E0E   ; OUTI
site 02E11   ; OUT ($BF),A
site 02E16   ; OUT ($BF),A
site 02E18   ; OUTI
site 02E1B   ; OUT ($BF),A
site 02E1D   ; OUTI
site 02E20   ; OUT ($BF),A
site 02E22   ; OUTI
site 02E26   ; OUT ($BF),A
site 02E28   ; OUTI
site 02E2D   ; OUTI
site 02E30   ; OUT ($BF),A
site 02E32   ; OUTI
site 02E35   ; OUT ($BF),A
site 02E37   ; OUTI
site 02E3B   ; OUT ($BF),A
site 02E3D   ; OUTI
site 02E40   ; OUT ($BF),A
site 02E45   ; OUT ($BF),A
site 02E47   ; OUTI
site 02E4A   ; OUT ($BF),A
site 02E4C   ; OUTI
site 02E4F   ; OUT ($BF),A
site 02E51   ; OUTI
site 02E55   ; OUT ($BF),A
site 02E57   ; OUTI
site 02E5A   ; OUT ($BF),A
site 02E5F   ; OUT ($BF),A
site 02E61   ; OUTI
site 02E64   ; OUT ($BF),A
site 02E66   ; OUTI
site 02E69   ; OUT ($BF),A
site 02E6B   ; OUTI
site 02E6F   ; OUT ($BF),A
site 02E71   ; OUTI
site 02E74   ; OUT ($BF),A
site 02E79   ; OUT ($BF),A
site 02E7B   ; OUTI
site 02E7E   ; OUT ($BF),A
site 02E80   ; OUTI
site 02E83   ; OUT ($BF),A
site 02E85   ; OUTI
site 02E89   ; OUT ($BF),A
site 02E8B   ; OUTI
site 02E8E   ; OUT ($BF),A
site 02E93   ; OUT ($BF),A
site 02E9E   ; OUT ($BE),A
site 02EA1   ; OUT ($BE),A
site 02ECD   ; OUT ($BF),A
site 02ED2   ; OUT ($BF),A
site 02F05   ; OUT ($BF),A
site 02F0A   ; OUT ($BF),A
site 02F12   ; OUT ($BE),A
site 02F15   ; OUT ($BE),A
site 0349D   ; OUT ($BF),A
site 034A1   ; OUT ($BF),A
site 034E6   ; OUT ($BF),A
site 034EA   ; OUT ($BF),A
site 03506   ; OUT ($BF),A
site 0350A   ; OUT ($BF),A
site 037E8   ; OUT ($BE),A
site 037EB   ; OUT ($BE),A
site 037EE   ; OUT ($BE),A
site 037F0   ; OUT ($BE),A
site 03806   ; OUT ($BE),A
site 03809   ; OUT ($BE),A
site 0380C   ; OUT ($BE),A
site 0380E   ; OUT ($BE),A
site 03824   ; OUT ($BE),A
site 03827   ; OUT ($BE),A
site 0382A   ; OUT ($BE),A
site 0382E   ; OUT ($BE),A
site 03844   ; OUT ($BE),A
site 03847   ; OUT ($BE),A
site 0384A   ; OUT ($BE),A
site 0384D   ; OUT ($BE),A
site 03863   ; OUT ($BE),A
site 03865   ; OUT ($BE),A
site 03868   ; OUT ($BE),A
site 0386B   ; OUT ($BE),A
site 03881   ; OUT ($BE),A
site 03883   ; OUT ($BE),A
site 03885   ; OUT ($BE),A
site 03888   ; OUT ($BE),A
site 039D4   ; OUT ($BF),A
site 039D8   ; OUT ($BF),A
site 039DF   ; OUT ($BE),A
site 039E2   ; OUT ($BE),A
site 039F4   ; OUT ($BF),A
site 039F8   ; OUT ($BF),A
site 039FD   ; OUT ($BE),A
site 03A00   ; OUT ($BE),A
site 03C80   ; OTIR
site 03CB3   ; IN A,($DC)
site 03CC2   ; IN A,($00)
site 03CE4   ; IN A,($DC)
site 03CEE   ; IN A,($DD)
site 03D01   ; OUT ($BF),A
site 03D05   ; OUT ($BF),A
site 03D0C   ; OUT ($BE),A
site 03D0E   ; OUT ($BE),A
site 03D60   ; OUT ($BF),A
site 03D64   ; OUT ($BF),A
site 08ECC   ; OUT ($BF),A
site 08ED2   ; OUT ($BF),A
site 08ED5   ; OUT ($BF),A
site 08F4B   ; OUT ($BE),A
site 08F4D   ; OUT ($BE),A
site 08F4F   ; OUT ($BE),A
site 08F51   ; OUT ($BE),A
site 08F53   ; OUT ($BE),A
site 08F55   ; OUT ($BE),A
site 08F57   ; OUT ($BE),A
site 08F59   ; OUT ($BE),A
site 08F5B   ; OUT ($BE),A
site 08F5D   ; OUT ($BE),A
site 08F5F   ; OUT ($BE),A
site 08F61   ; OUT ($BE),A
site 08F63   ; OUT ($BE),A
site 08F65   ; OUT ($BE),A
site 08F67   ; OUT ($BE),A
site 08F69   ; OUT ($BE),A
site 08F6C   ; OUTI
site 08F6E   ; OUTI
site 08F71   ; OUT ($BE),A
site 08F73   ; OUT ($BE),A
site 08F75   ; OUTI
site 08F77   ; OUTI
site 08F79   ; OUT ($BE),A
site 08F7B   ; OUT ($BE),A
site 08F7D   ; OUTI
site 08F7F   ; OUTI
site 08F81   ; OUT ($BE),A
site 08F83   ; OUT ($BE),A
site 08F85   ; OUTI
site 08F87   ; OUTI
site 08F89   ; OUT ($BE),A
site 08F8B   ; OUT ($BE),A
site 08F8E   ; OUTI
site 08F90   ; OUTI
site 08F92   ; OUTI
site 08F95   ; OUT ($BE),A
site 08F97   ; OUTI
site 08F99   ; OUTI
site 08F9B   ; OUTI
site 08F9D   ; OUT ($BE),A
site 08F9F   ; OUTI
site 08FA1   ; OUTI
site 08FA3   ; OUTI
site 08FA5   ; OUT ($BE),A
site 08FA7   ; OUTI
site 08FA9   ; OUTI
site 08FAB   ; OUTI
site 08FAD   ; OUT ($BE),A
site 1C994   ; OUT ($BF),A
site 1C998   ; OUT ($BF),A
site 1C9B0   ; OUT ($BF),A
site 1C9B4   ; OUT ($BF),A
site 1C9B9   ; OUT ($BE),A
site 1DA39   ; OUT ($BF),A
site 1DA3D   ; OUT ($BF),A
site 1DA4A   ; OUT ($BF),A
site 1DA4E   ; OUT ($BF),A
site 1DA56   ; OUT ($BE),A
site 1ED60   ; OUT ($BF),A
site 1ED64   ; OUT ($BF),A
site 1ED89   ; OUT ($BE),A
site 1ED8D   ; OUT ($BE),A
site 1ED91   ; OUT ($BE),A
site 1ED94   ; OUT ($BE),A
site 202E9   ; OUT ($7E),A
site 202FD   ; OUT ($7E),A
site 20311   ; OUT ($7E),A
site 20319   ; OUT ($7E),A
site 20324   ; OUT ($7E),A
site 20331   ; OUT ($7E),A
site 20344   ; OUT ($7E),A
site 2407E   ; OUT ($BF),A
site 24082   ; OUT ($BF),A
site 242FF   ; OUT ($BF),A
site 24303   ; OUT ($BF),A
site 244FA   ; OUT ($BF),A
site 244FE   ; OUT ($BF),A
site 25A36   ; OUT ($BF),A
site 25A3A   ; OUT ($BF),A
site 2644A   ; OUT ($BF),A
site 2644E   ; OUT ($BF),A
site 2645D   ; OUT ($BF),A
site 26461   ; OUT ($BF),A
site 27C3A   ; OUT ($BF),A
site 27C3E   ; OUT ($BF),A
site 27CF6   ; OUT ($BF),A
site 27CFA   ; OUT ($BF),A
site 300A5   ; IN A,($7E)
site 300AF   ; OUT ($BF),A
site 300B3   ; OUT ($BF),A
site 300B5   ; IN A,($BF)
site 300D5   ; OUT ($BF),A
site 300D9   ; OUT ($BF),A
site 3010B   ; OUT ($BF),A
site 3010F   ; OUT ($BF),A
site 3024C   ; OUT ($BF),A
site 30250   ; OUT ($BF),A
site 3025D   ; OUT ($BF),A
site 30261   ; OUT ($BF),A
site 30266   ; OUT ($BE),A
site 3026A   ; OUT ($BE),A
site 3026C   ; OUT ($BE),A
site 3026E   ; OUT ($BE),A
site 30274   ; OUT ($BF),A
site 30278   ; OUT ($BF),A
site 3027E   ; OUT ($BE),A
site 30280   ; OUT ($BE),A
site 30282   ; OUT ($BE),A
site 30284   ; OUT ($BE),A
site 3028A   ; OUT ($BF),A
site 3028E   ; OUT ($BF),A
site 30293   ; OUT ($BE),A
site 30297   ; OUT ($BE),A
site 3029A   ; OUT ($BE),A
site 3029C   ; OUT ($BE),A
site 302D6   ; OUT ($BF),A
site 302DA   ; OUT ($BF),A
site 303D8   ; OUT ($BF),A
site 303DC   ; OUT ($BF),A
site 3065E   ; OUT ($BF),A
site 30662   ; OUT ($BF),A
site 3066E   ; OUT ($BF),A
site 30672   ; OUT ($BF),A
site 30682   ; OUT ($BF),A
site 30686   ; OUT ($BF),A
site 30760   ; OUT ($BF),A
site 30764   ; OUT ($BF),A
site 30770   ; OUT ($BF),A
site 30774   ; OUT ($BF),A
site 30779   ; OUT ($BE),A
site 307C0   ; OUT ($BF),A
site 307C4   ; OUT ($BF),A
site 307EB   ; IN A,($7E)
site 3309A   ; OUT ($BF),A
site 3309E   ; OUT ($BF),A
site 332A2   ; OUT ($BF),A
site 332A6   ; OUT ($BF),A
site 3F58D   ; OUT ($BF),A
site 3F591   ; OUT ($BF),A
site 3F5A6   ; OUT ($BF),A
site 3F5AA   ; OUT ($BF),A
site 3F5B7   ; OUT ($BF),A
site 3F5BB   ; OUT ($BF),A
site 3FF60   ; OUT ($BF),A
site 3FF64   ; OUT ($BF),A
