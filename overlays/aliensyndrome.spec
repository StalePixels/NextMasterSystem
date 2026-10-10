# Alien Syndrome, 5CBFE997, drafted by tools/mkspec.py from sitescan output (with the detector log).
name Alien Syndrome
cart 5CBFE997
hz any		; No-Intro regions USA, Europe, Brazil
# tilecache: whole tiles copied from cart ROM are not converted again (MAME,
# game frames 300-2300: framework cycles -1.8%, frames over 100% 14 -> 4)
tilecache
# No free RST vector: $0000-$0002 (the game's interrupt-disable and the start of its stack setup) becomes the vector,
# the game starts at $0004 with the SP its LD SP,nn set.
vector 00 io
start 0004 CFB0
asm 00004 2   ; IM 1 -> IM 2
    im 2
endasm
# The row writer at $08AD writes C rows of B name table cells: the low byte
# of each cell from DE, the high byte in A, each row at HL, the next row
# $40 bytes on. The game calls it with interrupts on. Through the I/O trap
# each cell costs two framework calls, so a row of the title logo takes a
# fifth of a frame; the frame handler then comes in the middle of a row and
# moves the VDP address (it writes the sprite table), and the rest of the
# row goes to the wrong place. Code page 0 does the same work in bulk: it
# builds each row in a buffer and writes it with one call to the
# framework's jt_vwrite. It leaves the registers, the flags and the VDP
# state as the game's routine does.
asm 008AD 5   ; the routine's first instructions -> far call to page 0, then return
    rst $00
    db far_io, pg_rows, ent_rows
    ret
endasm
page 0 rows
; rows: HL = name table address, DE = the cells' low bytes, A = their high
; byte, B = cells per row (0 = 256), C = rows (0 = 256). Returns as the
; game's routine does: HL and DE past the last row, A kept, B kept, C = 0,
; F from its last steps (an ADD HL,BC, then a DEC C). The game sets the
; VDP address from HL with bit 6 of H set, a VRAM write; it calls this with
; name table addresses ($3800-$3EFF), and jt_vwrite writes VRAM only.
rows:   push ix
        push iy
.row:   push bc                 ; B cells, C rows
        push af                 ; A = the high byte
        push hl                 ; the row's address
        ex de,hl                ; HL = the low bytes
        ld de,buf
        ld c,a
        push bc
.cell:  call jt_peek            ; the low byte, as the game sees it
        ld (de),a
        inc de
        ld a,c
        ld (de),a
        inc de
        inc hl
        djnz .cell
        pop bc                  ; B = cells
        ex (sp),hl              ; the source end under the row's address
        push hl
        ex de,hl                ; DE = the row's VRAM address
        ld a,b
        dec a
        cp 128
        jr nc,.two
        ld a,b                  ; up to 128 cells: one run of 2 * B bytes
        add a,a
        ld b,a
        ld c,1
        jr .go
.two:   ld c,2                  ; more: two runs of B bytes, one after the other
.go:    ld ix,0
        ld a,b
        ld ixl,a
        or a
        jr nz,.step
        inc ixh                 ; 256
.step:  push ix
        pop iy                  ; both steps = the run's length
        ld hl,buf
        ld a,1                  ; the source as mapped: buf in this page
        call jt_vwrite
        pop hl                  ; the row's address
        pop de                  ; the source end
        pop af
        ld bc,$0040             ; the next row
        add hl,bc
        pop bc
        dec c
        jr nz,.row
        pop iy
        pop ix
        ret
buf:    ds 512
endpage
site 00048   ; IN A,($BF)
site 00079   ; IN A,($DD)
site 00093   ; OUT ($BF),A
site 00097   ; OUT ($BF),A
site 0009C   ; OUT ($BF),A
site 000A0   ; OUT ($BF),A
site 000CC   ; OUT ($BF),A
site 000D1   ; OUT ($BF),A
otir 000DA   ; OUTI
site 000E4   ; OUT ($BF),A
site 000E9   ; OUT ($BF),A
otir 000F2   ; OUTI
otir 0010B   ; OUTI
otir 0011E   ; OUTI
site 0012C   ; OUT ($BF),A
site 00131   ; OUT ($BF),A
otir 0013A   ; OUTI
site 00144   ; OUT ($BF),A
site 00149   ; OUT ($BF),A
otir 00152   ; OUTI
otir 0016C   ; OUTI
otir 00180   ; OUTI
site 0018C   ; OUT ($BF),A
site 00191   ; OUT ($BF),A
otir 0019C   ; OUTI
site 001AF   ; OUT ($BF),A
site 001B4   ; OUT ($BF),A
site 00208   ; OUT ($BF),A
site 0020F   ; OUT ($BF),A
site 00217   ; IN A,($BE)
site 0021F   ; OUT ($BF),A
site 00226   ; OUT ($BF),A
site 0022E   ; IN A,($BE)
site 00269   ; OUT ($BF),A
site 0026F   ; OUT ($BF),A
site 00277   ; IN A,($BE)
site 00410   ; OUT ($BF),A
site 00419   ; OUT ($BF),A
site 00427   ; OUTI
site 0042F   ; INI
site 004B7   ; IN A,($BF)
otir 004C0   ; OUTI
site 004C5   ; OUT ($BE),A
site 004E2   ; OUT ($3E),A
site 004EA   ; OUT ($F2),A
site 004ED   ; IN A,($F2)
site 004FF   ; OUT ($F2),A
site 00507   ; OUT ($3E),A
site 00867   ; OUT ($BF),A
site 0086A   ; OUT ($BF),A
site 0086E   ; OUT ($BF),A
site 00873   ; OUT ($BF),A
site 0087B   ; OUT ($BE),A
otir 0088B   ; OUTI
site 0089B   ; OUT ($BE),A
site 008A0   ; OUT ($BE),A
site 008B6   ; OUTI
site 008BA   ; OUT (C),A
site 00983   ; OUT ($BE),A
site 00986   ; OUT ($BE),A
site 01070   ; IN A,($DC)
site 011CD   ; IN A,($DC)
site 011F2   ; IN A,($DD)
site 01271   ; OUT ($BF),A
site 01276   ; OUT ($BF),A
site 01279   ; OUT ($BE),A
site 0127D   ; OUT ($BE),A
site 0128A   ; OUT ($BF),A
site 0128F   ; OUT ($BF),A
site 012E0   ; OUT ($BF),A
site 012E5   ; OUT ($BF),A
site 012EA   ; OUT ($BE),A
site 012EF   ; OUT ($BE),A
site 012FD   ; OUT ($BF),A
site 01302   ; OUT ($BF),A
site 02A6F   ; OUT ($3F),A
site 02A71   ; IN A,($DD)
site 02A7B   ; OUT ($3F),A
site 02A7D   ; IN A,($DD)
site 0AB2B   ; OUT ($BF),A
site 0AB2E   ; OUT ($BF),A
site 0AB36   ; INIR
site 0AB52   ; OUT ($BF),A
site 0AB57   ; OUT ($BF),A
site 0AB5F   ; OTIR
site 1C2FD   ; OUT ($F0),A
site 1C303   ; OUT ($F1),A
site 1C346   ; OUT ($7F),A
site 1C51B   ; OUT ($F0),A
site 1C521   ; OUT ($F1),A
site 1C52C   ; OUTI
site 1C533   ; OUTI
site 1C5AD   ; OUT ($F0),A
site 1C5B3   ; OUT ($F1),A
site 1C67C   ; OUT ($F0),A
site 1C683   ; OUT ($F1),A
site 1C704   ; OUT ($F0),A
site 1C70A   ; OUT ($F1),A
site 1C7EB   ; OUT ($7F),A
site 1C7F9   ; OUT ($7F),A
site 1C803   ; OUT ($7F),A
site 1CA1C   ; OUTI
site 1CA23   ; OUTI
site 1CA6C   ; OUT ($7F),A
site 1CB0F   ; OUT ($7F),A
site 1CB13   ; OUT ($7F),A
site 1CB1C   ; OUT ($7F),A
site 1CBDA   ; OTIR
site 1CBE8   ; OUT (C),D
site 1CBEE   ; OUT ($F1),A
site 1CC04   ; OUT ($7F),A
site 1CC08   ; OUT ($7F),A
site 1CC0C   ; OUT ($7F),A
site 1CCCA   ; OUT ($F0),A
site 1CCD1   ; OUT ($F1),A
site 1CCDD   ; OUT ($F0),A
site 1CCF4   ; OUT ($F1),A
site 1CCFE   ; OUT ($F0),A
site 1CD08   ; OUT ($F1),A
# not patched (data, read as code through a table): site 1D2A4
# not patched (data, read as code through a table): site 1D2B7
site 1E049   ; OUT ($7F),A
site 1E04C   ; OUT ($F2),A
site 1E066   ; OUT ($7F),A
site 1E076   ; OUT ($F2),A
mapst 00257   ; LD ($FFFF),A
mapst 0025E   ; LD ($FFFF),A
mapst 00319   ; LD ($FFFF),A
# CHECK mapper at 0043D ($043D bank 0): LD (HL),$00 $FFFC<-$00
# CHECK mapper at 00440 ($0440 bank 0): LD (HL),$00 $FFFD<-$00
# CHECK mapper at 00443 ($0443 bank 0): LD (HL),$01 $FFFE<-$01
# CHECK mapper at 00446 ($0446 bank 0): LD (HL),$02 $FFFF<-$02
mapst 004DA   ; LD ($FFFF),A
mapst 00547   ; LD ($FFFF),A
mapst 0054E   ; LD ($FFFF),A
mapst 00569   ; LD ($FFFF),A
mapst 005A6   ; LD ($FFFF),A
mapst 005DC   ; LD ($FFFF),A
mapst 007C8   ; LD ($FFFF),A
mapst 007CF   ; LD ($FFFF),A
mapst 00A4B   ; LD ($FFFF),A
mapst 00A52   ; LD ($FFFF),A
mapst 00B2B   ; LD ($FFFF),A
mapst 00B69   ; LD ($FFFF),A
mapst 00B73   ; LD ($FFFF),A
mapst 00BAA   ; LD ($FFFF),A
mapst 00BB4   ; LD ($FFFF),A
mapst 00C2E   ; LD ($FFFF),A
mapst 00DEB   ; LD ($FFFF),A
mapst 00E1E   ; LD ($FFFF),A
mapst 00E28   ; LD ($FFFF),A
mapst 00F18   ; LD ($FFFF),A
mapst 00F22   ; LD ($FFFF),A
mapst 00F62   ; LD ($FFFF),A
mapst 00F6C   ; LD ($FFFF),A
mapst 00FD3   ; LD ($FFFF),A
mapst 01252   ; LD ($FFFF),A
mapst 012AA   ; LD ($FFFF),A
mapst 012C9   ; LD ($FFFF),A
mapst 0131E   ; LD ($FFFF),A
mapst 01B3D   ; LD ($FFFF),A
mapst 01B5E   ; LD ($FFFF),A
mapst 02082   ; LD ($FFFF),A
mapst 0208B   ; LD ($FFFF),A
mapst 02A54   ; LD ($FFFF),A
mapst 04097   ; LD ($FFFF),A
mapst 0409E   ; LD ($FFFF),A
mapst 040CF   ; LD ($FFFF),A
mapst 040D6   ; LD ($FFFF),A
mapst 040F6   ; LD ($FFFF),A
mapst 040FD   ; LD ($FFFF),A
mapst 0410B   ; LD ($FFFF),A
mapst 04112   ; LD ($FFFF),A
mapst 04153   ; LD ($FFFF),A
mapst 0415A   ; LD ($FFFF),A
mapst 04167   ; LD ($FFFF),A
mapst 0416E   ; LD ($FFFF),A
mapst 041A7   ; LD ($FFFF),A
mapst 041AE   ; LD ($FFFF),A
mapst 041BC   ; LD ($FFFF),A
mapst 041C3   ; LD ($FFFF),A
mapst 041D1   ; LD ($FFFF),A
mapst 041D8   ; LD ($FFFF),A
mapst 041E6   ; LD ($FFFF),A
mapst 041ED   ; LD ($FFFF),A
mapst 041FE   ; LD ($FFFF),A
mapst 04205   ; LD ($FFFF),A
mapst 0445F   ; LD ($FFFF),A
mapst 04466   ; LD ($FFFF),A
mapst 04470   ; LD ($FFFF),A
mapst 04477   ; LD ($FFFF),A
mapst 06553   ; LD ($FFFF),A
mapst 0655D   ; LD ($FFFF),A
mapst 065F6   ; LD ($FFFF),A
mapst 06600   ; LD ($FFFF),A
mapst 0668C   ; LD ($FFFF),A
mapst 06696   ; LD ($FFFF),A
mapst 06722   ; LD ($FFFF),A
mapst 0672C   ; LD ($FFFF),A
mapst 07A4F   ; LD ($FFFF),A
mapst 07A67   ; LD ($FFFF),A
mapst 07ADB   ; LD ($FFFF),A
mapst 07AED   ; LD ($FFFF),A
mapst 07B03   ; LD ($FFFF),A
mapst 07B33   ; LD ($FFFF),A
mapst 07EB1   ; LD ($FFFF),A
mapst 07EB7   ; LD ($FFFF),A
mapst 07ED1   ; LD ($FFFF),A
mapst 07EDD   ; LD ($FFFF),A
mapst 07F04   ; LD ($FFFF),A
mapst 07FA6   ; LD ($FFFF),A
# CHECK cartarea_store at 006D1 ($06D1 bank 0): LD (BC),A $0006
# CHECK cartarea_store at 01039 ($1039 bank 0): LD (DE),A $0705
# CHECK cartarea_store at 1C038 ($8038 bank 7): LD (BC),A $8201
# CHECK cartarea_store at 1C03C ($803C bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C03D ($803D bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C04B ($804B bank 7): LD (BC),A $0202
# CHECK cartarea_store at 1C04C ($804C bank 7): LD (BC),A $0202
# CHECK cartarea_store at 1C066 ($8066 bank 7): LD (BC),A $0808
# CHECK cartarea_store at 1C067 ($8067 bank 7): LD (BC),A $0808
# CHECK cartarea_store at 1C06B ($806B bank 7): LD (BC),A $0201
# CHECK cartarea_store at 1C08A ($808A bank 7): LD (BC),A $0202
# CHECK cartarea_store at 1C08B ($808B bank 7): LD (BC),A $0202
# CHECK cartarea_store at 1C08E ($808E bank 7): LD (BC),A $0204
# CHECK cartarea_store at 1C08F ($808F bank 7): LD (BC),A $0204
# CHECK cartarea_store at 1C094 ($8094 bank 7): LD (BC),A $0001
# CHECK cartarea_store at 1C11F ($811F bank 7): LD (BC),A $3EF3
# CHECK cartarea_store at 1C123 ($8123 bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C127 ($8127 bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C12B ($812B bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C12E ($812E bank 7): LD (BC),A $0102
# CHECK cartarea_store at 1C136 ($8136 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C13F ($813F bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C148 ($8148 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C151 ($8151 bank 7): LD (BC),A $0282
# CHECK cartarea_store at 1C159 ($8159 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C162 ($8162 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C16A ($816A bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C174 ($8174 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C17D ($817D bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C187 ($8187 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C18F ($818F bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C19B ($819B bank 7): LD (BC),A $8201
# CHECK cartarea_store at 1C1A3 ($81A3 bank 7): LD (BC),A $8202
# CHECK cartarea_store at 1C1A9 ($81A9 bank 7): LD (BC),A $0D07
# CHECK cartarea_store at 1C1AE ($81AE bank 7): LD (BC),A $0C07
# CHECK cartarea_store at 1C1C7 ($81C7 bank 7): LD (BC),A $110A
# CHECK cartarea_store at 1C1E4 ($81E4 bank 7): LD (BC),A $100B
# CHECK cartarea_store at 1C1E5 ($81E5 bank 7): LD (BC),A $100B
# CHECK cartarea_store at 1C1E6 ($81E6 bank 7): LD (BC),A $100B
# CHECK cartarea_store at 1C1E7 ($81E7 bank 7): LD (BC),A $100B
# CHECK cartarea_store at 1C1E8 ($81E8 bank 7): LD (BC),A $100B
# CHECK cartarea_store at 1C1E9 ($81E9 bank 7): LD (BC),A $100B
# CHECK cartarea_store at 1C1ED ($81ED bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C1F1 ($81F1 bank 7): LD (BC),A $0100
# CHECK cartarea_store at 1C1F7 ($81F7 bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1C1FF ($81FF bank 7): LD (BC),A $0303
# CHECK cartarea_store at 1CDB4 ($8DB4 bank 7): LD (DE),A $7904
# CHECK cartarea_store at 1CDE0 ($8DE0 bank 7): LD (BC),A $0601
# CHECK cartarea_store at 1CDF2 ($8DF2 bank 7): LD (BC),A $0901
# CHECK cartarea_store at 1CE05 ($8E05 bank 7): LD (BC),A $0180
# CHECK cartarea_store at 1CE09 ($8E09 bank 7): LD (BC),A $0180
# CHECK cartarea_store at 1CE11 ($8E11 bank 7): LD (BC),A $A780
# CHECK cartarea_store at 1CE19 ($8E19 bank 7): LD (BC),A $8180
# CHECK cartarea_store at 1CE3B ($8E3B bank 7): LD (BC),A $02BF
# CHECK cartarea_store at 1CF2D ($C132 bank ram): LD ($A28F),HL $A28F,$A290
# CHECK cartarea_store at 1D09C ($909C bank 7): LD (DE),A $4E01
# CHECK cartarea_store at 1D0A3 ($90A3 bank 7): LD (BC),A $90E8
# CHECK cartarea_store at 1D1D7 ($91D7 bank 7): LD (BC),A $91E3
# CHECK cartarea_store at 1D29A ($929A bank 7): LD (BC),A $0371
# CHECK cartarea_store at 1D2A0 ($92A0 bank 7): LD (BC),A $0372
# CHECK cartarea_store at 1D2A3 ($92A3 bank 7): LD (BC),A $0372
# CHECK cartarea_store at 1D2E6 ($92E6 bank 7): LD (BC),A $02FC
# CHECK cartarea_store at 1D2EE ($92EE bank 7): LD (BC),A $92FC
# CHECK cartarea_store at 1D2F0 ($92F0 bank 7): LD (BC),A $91FB,$92FC
# CHECK cartarea_store at 1D2FA ($92FA bank 7): LD (BC),A $92FB
# CHECK cartarea_store at 1D308 ($9308 bank 7): LD (BC),A $9414
# CHECK cartarea_store at 1D312 ($9312 bank 7): LD (BC),A $9313
# CHECK cartarea_store at 1D341 ($9341 bank 7): LD (BC),A $934D
# CHECK cartarea_store at 1D36A ($936A bank 7): LD (BC),A $01FC
# CHECK cartarea_store at 1D380 ($9380 bank 7): LD (BC),A $8D87,$8E86,$8F85,$9084...
# CHECK cartarea_store at 1D395 ($9395 bank 7): LD (BC),A $93A0
# CHECK cartarea_store at 1D3B3 ($93B3 bank 7): LD (BC),A $2271
# CHECK cartarea_store at 1D3B5 ($93B5 bank 7): LD (BC),A $2271
# CHECK cartarea_store at 1D3D0 ($93D0 bank 7): LD (DE),A $4E01
# CHECK cartarea_store at 1D3D7 ($93D7 bank 7): LD (BC),A $94A0
# CHECK cartarea_store at 1D3E0 ($93E0 bank 7): LD (BC),A $94F2
# CHECK cartarea_store at 1D3E9 ($93E9 bank 7): LD (BC),A $94FD
# CHECK cartarea_store at 1D4FE ($94FE bank 7): LD (BC),A $ACF2
# CHECK cartarea_store at 1D502 ($9502 bank 7): LD (BC),A $ACF2
# CHECK cartarea_store at 1D506 ($9506 bank 7): LD (BC),A $ACF2
# CHECK cartarea_store at 1D50A ($950A bank 7): LD (BC),A $ACF3
# CHECK cartarea_store at 1D59D ($959D bank 7): LD (BC),A $9687
# CHECK cartarea_store at 1D5A6 ($95A6 bank 7): LD (BC),A $9787
# CHECK cartarea_store at 1D5AF ($95AF bank 7): LD (BC),A $9887
# CHECK cartarea_store at 1D5B7 ($95B7 bank 7): LD (BC),A $9987
# CHECK cartarea_store at 1D5B9 ($95B9 bank 7): LD (BC),A $9987
# CHECK cartarea_store at 1D5C7 ($95C7 bank 7): LD (BC),A $9987
# CHECK cartarea_store at 1D5D0 ($95D0 bank 7): LD (BC),A $9988
# CHECK cartarea_store at 1D5D9 ($95D9 bank 7): LD (BC),A $9989
# CHECK cartarea_store at 1D5E1 ($95E1 bank 7): LD (BC),A $998A
# CHECK cartarea_store at 1D5FE ($95FE bank 7): LD (BC),A $998D
# CHECK cartarea_store at 1D60A ($960A bank 7): LD (BC),A $1380
# CHECK cartarea_store at 1D630 ($9630 bank 7): LD (BC),A $1680
# CHECK cartarea_store at 1D63F ($963F bank 7): LD (BC),A $0180
# CHECK cartarea_store at 1D653 ($9653 bank 7): LD (BC),A $9671
# CHECK cartarea_store at 1D656 ($9656 bank 7): LD (BC),A $9672
# CHECK cartarea_store at 1D68A ($968A bank 7): LD (HL),L $766D
# CHECK cartarea_store at 1D6B2 ($96B2 bank 7): LD (BC),A $96BD
# CHECK cartarea_store at 1D6D6 ($96D6 bank 7): LD (BC),A $1680
# CHECK cartarea_store at 1D7EA ($97EA bank 7): LD (DE),A $3203
# CHECK cartarea_store at 1D82A ($982A bank 7): LD (BC),A $2E02
# CHECK cartarea_store at 1D848 ($9848 bank 7): LD (BC),A $2002
# CHECK cartarea_store at 1D864 ($9864 bank 7): LD (BC),A $1E02
# CHECK cartarea_store at 1D9C3 ($99C3 bank 7): LD (DE),A $0B02
# CHECK cartarea_store at 1D9D3 ($99D3 bank 7): LD (BC),A $9FD0
# CHECK cartarea_store at 1D9D6 ($99D6 bank 7): LD (BC),A $9FD0
# CHECK cartarea_store at 1D9D7 ($99D7 bank 7): LD (BC),A $9FD0
# CHECK cartarea_store at 1D9DF ($99DF bank 7): LD (BC),A $A0D0
# CHECK cartarea_store at 1EE55 ($AE55 bank 7): LD (DE),A $B102
# CHECK cartarea_store at 1EE68 ($AE68 bank 7): LD (BC),A $2300
# CHECK cartarea_store at 1EE71 ($AE71 bank 7): LD (BC),A $2400,$A282
# CHECK cartarea_store at 1EEA8 ($AEA8 bank 7): LD (DE),A $0280,$029E
# CHECK cartarea_store at 1EEB4 ($AEB4 bank 7): LD (DE),A $0280,$029E
# CHECK cartarea_store at 1EEBA ($AEBA bank 7): LD (BC),A $A482
# CHECK cartarea_store at 1EEE6 ($AEE6 bank 7): LD (DE),A $02A4
# CHECK cartarea_store at 1EEF8 ($AEF8 bank 7): LD (DE),A $02A4
# CHECK cartarea_store at 1EF05 ($AF05 bank 7): LD (BC),A $AA84
# CHECK cartarea_store at 1EF32 ($AF32 bank 7): LD (DE),A $02B5,$9090,$90A1,$90A2...
# CHECK cartarea_store at 1EF3E ($AF3E bank 7): LD (DE),A $02B5,$90A1,$90A2,$90A4...
# CHECK cartarea_store at 1EF44 ($AF44 bank 7): LD (BC),A $A482
# CHECK cartarea_store at 1EF68 ($AF68 bank 7): LD (DE),A $0291,$02A4,$02F7,$9091...
# CHECK cartarea_store at 1EF7A ($AF7A bank 7): LD (DE),A $9090
# CHECK cartarea_store at 1EF85 ($AF85 bank 7): LD (DE),A $02A2,$9090,$90A2,$91A2
# CHECK cartarea_store at 1EF9B ($AF9B bank 7): LD (DE),A $02A1,$908F,$9090,$90A1...
# CHECK cartarea_store at 1EFAB ($AFAB bank 7): LD (DE),A $02A4,$90A4,$91A4
# CHECK cartarea_store at 1EFBB ($AFBB bank 7): LD (HL),$24 $1629
# CHECK cartarea_store at 1EFE8 ($AFE8 bank 7): LD (DE),A $9090
# CHECK cartarea_store at 1EFEC ($AFEC bank 7): LD (HL),$9D $172A
# CHECK cartarea_store at 1EFFD ($AFFD bank 7): LD (HL),$24 $172A
# CHECK cartarea_store at 1F027 ($B027 bank 7): LD (DE),A $9180,$91F2
# CHECK cartarea_store at 1F033 ($B033 bank 7): LD (DE),A $9180,$91F2
# CHECK cartarea_store at 1F039 ($B039 bank 7): LD (BC),A $A400,$A404,$A408,$A40C...
# CHECK cartarea_store at 1F04A ($B04A bank 7): LD (HL),$A4 $B610
# CHECK cartarea_store at 1F053 ($B053 bank 7): LD (DE),A $9180
# CHECK cartarea_store at 1F05F ($B05F bank 7): LD (DE),A $9180
# CHECK cartarea_store at 1F065 ($B065 bank 7): LD (BC),A $A403,$A407,$A40B,$A40F...
# CHECK cartarea_store at 1F078 ($B078 bank 7): LD (DE),A $9180
# CHECK cartarea_store at 1F089 ($B089 bank 7): LD (DE),A $9180
# CHECK cartarea_store at 1F0F6 ($B0F6 bank 7): LD (HL),$A4 $B610
# CHECK cartarea_store at 1F138 ($B138 bank 7): LD (DE),A $A801
# CHECK cartarea_store at 1F171 ($B171 bank 7): LD (BC),A $B1AA
# CHECK ram_exec at 1CDC8 ($8DC8 bank 7): CALL M,$F38D $F38D
# CHECK ram_exec at 1CE33 ($8E33 bank 7): CALL P,$F500 $F500
# CHECK ram_exec at 1CE3C ($8E3C bank 7): JP $F502 $F502
# CHECK ram_exec at 1D2D7 ($92D7 bank 7): CALL M,$F200 $F200
# CHECK ram_exec at 1D2E3 ($92E3 bank 7): CALL M,$F200 $F200
# CHECK ram_exec at 1D385 ($9385 bank 7): JP NZ,$C7BA $C7BA
# CHECK ram_exec at 1D5DA ($95DA bank 7): CALL PE,$FC95 $FC95
# CHECK ram_exec at 1D5EB ($95EB bank 7): JP P,$F0F8 $F0F8
# CHECK ram_exec at 1D62D ($962D bank 7): JP P,$D30F $D30F
# CHECK ram_exec at 1D66F ($966F bank 7): JP P,$F803 $F803
# CHECK ram_exec at 1D685 ($9685 bank 7): JP P,$FF02 $FF02
# CHECK ram_exec at 1D69A ($969A bank 7): CALL M,$DC01 $DC01
# CHECK ram_exec at 1D6A5 ($96A5 bank 7): CALL M,$F900 $F900
# CHECK ram_exec at 1D830 ($9830 bank 7): JP P,$F301 $F301
# CHECK ram_exec at 1D875 ($9875 bank 7): CALL M,$F200 $F200
# CHECK ram_exec at 1D9B5 ($99B5 bank 7): JP PE,$E400 $E400
# CHECK ram_exec at 1D9BE ($99BE bank 7): JP PE,$F400 $F400
# CHECK ram_exec at 1D9D9 ($99D9 bank 7): JP PE,$E406 $E406
# CHECK ram_exec at 1EC26 ($AC26 bank 7): CALL M,$C007 $C007
# CHECK ram_exec at 1EC29 ($AC29 bank 7): CALL M,$C00F $C00F
# CHECK ram_exec at 1ECC0 ($ACC0 bank 7): CALL M,$FC07 $FC07
# CHECK ram_exec at 1ECC8 ($ACC8 bank 7): CALL M,$F00F $F00F
# CHECK ram_exec at 1ECD0 ($ACD0 bank 7): CALL M,$CF03 $CF03
# CHECK ram_exec at 1ECE3 ($ACE3 bank 7): JP $FC80 $FC80
# CHECK ram_exec at 1ED8F ($AD8F bank 7): CALL M,$FC07 $FC07
# CHECK ram_exec at 1ED9E ($AD9E bank 7): CALL M,$FF01 $FF01
# CHECK ram_exec at 1EDAB ($ADAB bank 7): CALL M,$FF03 $FF03
# CHECK ram_exec at 1EDC1 ($ADC1 bank 7): CALL M,$FE07 $FE07
# CHECK ram_exec at 1EDFB ($ADFB bank 7): CALL M,$FF00 $FF00
# CHECK ram_exec at 1EE24 ($AE24 bank 7): CALL M,$FF01 $FF01
# CHECK ram_exec at 1F1C9 ($B1C9 bank 7): CALL P,$C000 $C000
# CHECK ram_exec at 1F1D9 ($B1D9 bank 7): CALL PO,$F4B2 $F4B2
# CHECK indirect_unresolved at 00325 ($0325 bank 0): JP (HL) 
# CHECK indirect_unresolved at 00325 ($0325 bank 0): JP (HL) 
# CHECK indirect_unresolved at 006FF ($06FF bank 0): RET NZ 
# CHECK indirect_unresolved at 1C335 ($8335 bank 7): JP (HL) 
# CHECK indirect_unresolved at 1CFF0 ($8FF0 bank 7): JP (HL) 
# CHECK indirect_unresolved at 1D205 ($9205 bank 7): JP (HL) 
# CHECK indirect_unresolved at 1D28C ($928C bank 7): RET P 
# CHECK indirect_unresolved at 1D28E ($928E bank 7): RET PO 
# CHECK indirect_unresolved at 1D2B0 ($92B0 bank 7): RET M 
# CHECK indirect_unresolved at 1D2B5 ($92B5 bank 7): RET NZ 
# CHECK indirect_unresolved at 1D2C8 ($92C8 bank 7): RET P 
# CHECK indirect_unresolved at 1D2CA ($92CA bank 7): RET PO 
# CHECK indirect_unresolved at 1ECDF ($ACDF bank 7): RET PO 
# CHECK indirect_unresolved at 1ECE1 ($ACE1 bank 7): RET P 
# CHECK indirect_unresolved at 1EE21 ($AE21 bank 7): RST $28 $0028
# CHECK bank_unresolved at 001FC ($01FC bank 0): RET NZ $89F1
# CHECK bank_unresolved at 001FC ($01FC bank 0): RET NZ $85F9
# CHECK bank_unresolved at 001FD ($01FD bank 0): RET Z $89F1
# CHECK bank_unresolved at 001FD ($01FD bank 0): RET Z $85F9
# CHECK bank_unresolved at 00261 ($0261 bank 0): RET $89F1
# CHECK bank_unresolved at 00261 ($0261 bank 0): RET $85F9
# CHECK bank_unresolved at 00439 ($0439 bank 0): RET $89F1
# CHECK bank_unresolved at 00439 ($0439 bank 0): RET $85F9
# CHECK bank_unresolved at 00503 ($0503 bank 0): RET NC $89F1
# CHECK bank_unresolved at 00503 ($0503 bank 0): RET NC $85F9
# CHECK bank_unresolved at 00603 ($0603 bank 0): RET NZ $89F1
# CHECK bank_unresolved at 00603 ($0603 bank 0): RET NZ $85F9
# CHECK bank_unresolved at 006FA ($06FA bank 0): CALL $AE42 $AE42
# CHECK bank_unresolved at 00719 ($0719 bank 0): CALL $AE42 $AE42
# CHECK bank_unresolved at 0072F ($072F bank 0): CALL $AE42 $AE42
# CHECK bank_unresolved at 00734 ($0734 bank 0): CALL $AE42 $AE42
# CHECK bank_unresolved at 011BE ($11BE bank 0): CALL $AA16 $AA16
# CHECK bank_unresolved at 01CC2 ($1CC2 bank 0): CALL $AA16 $AA16
# CHECK bank_unresolved at 0673A ($673A bank 1): CALL $92D4 $92D4
# CHECK bank_unresolved at 06769 ($6769 bank 1): CALL $9303 $9303
# CHECK bank_unresolved at 06781 ($6781 bank 1): CALL $9217 $9217
# CHECK bank_unresolved at 06797 ($6797 bank 1): CALL $9254 $9254
# CHECK bank_unresolved at 067B1 ($67B1 bank 1): CALL $91B1 $91B1
# CHECK bank_unresolved at 07F92 ($7F92 bank 1): CALL $B8CA $B8CA
# CHECK low: site 008D1  OUTI  (port in C)
# CHECK low: site 008D5  OUTI  (port in C)
# CHECK low: site 00928  OUT ($BE),A  (vdp_data)
# CHECK low: site 0092D  OUT ($BE),A  (vdp_data)
# CHECK low: site 0825C  OUT ($F0),A  (fm_address)
# CHECK low: site 0E260  OTDR  (port in C)
# CHECK low: site 0EBA0  OTDR  (port in C)
# CHECK low: site 11A53  IN C,(C)  (port in C)
# CHECK low: site 12270  IN A,($BD)  (vdp_status)
# CHECK low: site 12274  IN A,($BD)  (vdp_status)
# CHECK low: site 13150  IN A,($BD)  (vdp_status)
# CHECK low: site 13154  IN A,($BD)  (vdp_status)
# CHECK low: site 18D24  OUT ($DD),A  (no_effect)
# CHECK low: site 190E1  OUT ($3F),A  (io_control)
# CHECK low: site 1AD60  IN A,($C0)  (joypad_a)
# CHECK low: site 1BB65  OUT ($F1),A  (fm_data)
# CHECK low: site 1BB69  OUT ($F1),A  (fm_data)
# CHECK low: site 1BCF1  OUT ($F1),A  (fm_data)
# CHECK low: site 1BCF5  OUT ($F1),A  (fm_data)
# CHECK low: site 1BDA4  IN A,($BF)  (vdp_status)
# CHECK low: site 1BDF8  IN A,($BF)  (vdp_status)
# CHECK low: site 1BE24  IN A,($BF)  (vdp_status)
# CHECK low: site 1BE78  IN A,($BF)  (vdp_status)
# CHECK low: site 22BD8  IN D,(C)  (port in C)
# CHECK low: site 22F5C  OUT ($C0),A  (no_effect)
# CHECK low: site 25228  IN A,($7E)  (v_counter)
# CHECK low: site 25238  IN A,($7E)  (v_counter)
# CHECK low: site 26B3C  OUT ($BF),A  (vdp_control)
# CHECK low: site 26B44  IN A,($BF)  (vdp_status)
# CHECK low: site 26B98  IN A,($BF)  (vdp_status)
# CHECK low: site 26BBC  OUT ($BF),A  (vdp_control)
# CHECK low: site 26BC4  IN A,($BF)  (vdp_status)
# CHECK low: site 26C18  IN A,($BF)  (vdp_status)
# CHECK low: site 26C44  IN A,($BF)  (vdp_status)
# CHECK low: site 26C98  IN A,($BF)  (vdp_status)
# CHECK low: site 26CA4  IN A,($BF)  (vdp_status)
# CHECK low: site 26CF8  IN A,($BF)  (vdp_status)
# CHECK low: site 26D24  IN A,($BF)  (vdp_status)
# CHECK low: site 26D78  IN A,($BF)  (vdp_status)
# CHECK low: site 26DA4  IN A,($BF)  (vdp_status)
# CHECK low: site 26DF8  IN A,($BF)  (vdp_status)
# CHECK low: site 2D478  IN A,($DC)  (joypad_a)
# CHECK low: site 2DAB5  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 2F6D1  IN A,($DD)  (joypad_b_misc)
# CHECK low: site 314D0  IN A,($DC)  (joypad_a)
# CHECK low: site 31A90  IN A,($DC)  (joypad_a)
# CHECK low: site 328CA  OTIR  (port in C)
# CHECK low: site 3474C  IN A,($7F)  (h_counter)
# CHECK low: site 34EE0  IN A,($BF)  (vdp_status)
# CHECK low: site 383CD  IN A,($DC)  (joypad_a)
# CHECK low: site 383D1  IN A,($DC)  (joypad_a)
# CHECK low: site 3851D  IN A,($DC)  (joypad_a)
# CHECK low: site 38AA5  IN A,($DC)  (joypad_a)
# CHECK low: site 38FA5  IN A,($DC)  (joypad_a)
# CHECK low: site 39E6D  IN A,($DC)  (joypad_a)
# CHECK low: site 39E71  IN A,($DC)  (joypad_a)
# CHECK low: site 39EDD  IN A,($DC)  (joypad_a)
# CHECK low: site 3D206  IN A,($DC)  (joypad_a)
# CHECK low: site 3D42E  IN A,($DC)  (joypad_a)
# CHECK low: site 3D491  IN A,($DC)  (joypad_a)
# CHECK low: site 3E056  IN A,($DC)  (joypad_a)
# CHECK low: site 3E8D1  OUTD  (port in C)
# CHECK low: site 3E8D7  OUTD  (port in C)
# CHECK low: site 3EC52  IN A,($DC)  (joypad_a)
# Mapper stores the draft missed: LD ($FFFF),A in bank 1 that no scanned
# path reached, found by sitescan's byte scan. They are pairs around calls into
# banks $8A, $8E and $8F: the game reads the current bank from $DFFF, saves it, selects
# the new bank, makes the call, then restores the saved bank.
# Byte scan hits left out: they decode as data (RST and NOP runs, no valid
# code after them, or no code leading to them).
mapst 04309   ; LD ($FFFF),A
mapst 04310   ; LD ($FFFF),A
mapst 04498   ; LD ($FFFF),A
mapst 044A0   ; LD ($FFFF),A
mapst 044AA   ; LD ($FFFF),A
mapst 044B1   ; LD ($FFFF),A
mapst 044BB   ; LD ($FFFF),A
mapst 044C2   ; LD ($FFFF),A
mapst 044CC   ; LD ($FFFF),A
mapst 044D3   ; LD ($FFFF),A
mapst 044DD   ; LD ($FFFF),A
mapst 044E4   ; LD ($FFFF),A
mapst 044EE   ; LD ($FFFF),A
mapst 044F5   ; LD ($FFFF),A
mapst 044FF   ; LD ($FFFF),A
mapst 04506   ; LD ($FFFF),A
mapst 04510   ; LD ($FFFF),A
mapst 04517   ; LD ($FFFF),A
mapst 04521   ; LD ($FFFF),A
mapst 04528   ; LD ($FFFF),A
mapst 04532   ; LD ($FFFF),A
mapst 04539   ; LD ($FFFF),A
mapst 04543   ; LD ($FFFF),A
mapst 0454A   ; LD ($FFFF),A
mapst 04554   ; LD ($FFFF),A
mapst 0455B   ; LD ($FFFF),A
mapst 04565   ; LD ($FFFF),A
mapst 0456C   ; LD ($FFFF),A
mapst 04576   ; LD ($FFFF),A
mapst 0457D   ; LD ($FFFF),A
mapst 04587   ; LD ($FFFF),A
mapst 0458E   ; LD ($FFFF),A
mapst 04598   ; LD ($FFFF),A
mapst 0459F   ; LD ($FFFF),A
mapst 045A9   ; LD ($FFFF),A
mapst 045B0   ; LD ($FFFF),A
mapst 045BA   ; LD ($FFFF),A
mapst 045C1   ; LD ($FFFF),A
mapst 045CB   ; LD ($FFFF),A
mapst 045D2   ; LD ($FFFF),A
mapst 045DC   ; LD ($FFFF),A
mapst 045E3   ; LD ($FFFF),A
mapst 045ED   ; LD ($FFFF),A
mapst 045F4   ; LD ($FFFF),A
mapst 045FE   ; LD ($FFFF),A
mapst 04605   ; LD ($FFFF),A
mapst 0460F   ; LD ($FFFF),A
mapst 04616   ; LD ($FFFF),A
mapst 04E8B   ; LD ($FFFF),A
mapst 04F52   ; LD ($FFFF),A
mapst 07C91   ; LD ($FFFF),A
mapst 07C9F   ; LD ($FFFF),A
mapst 07CB1   ; LD ($FFFF),A
mapst 07CB9   ; LD ($FFFF),A
mapst 07CD8   ; LD ($FFFF),A
mapst 07CFD   ; LD ($FFFF),A
mapst 07D4D   ; LD ($FFFF),A
mapst 07D56   ; LD ($FFFF),A
mapst 07D6C   ; LD ($FFFF),A
mapst 07D88   ; LD ($FFFF),A
mapst 07DF4   ; LD ($FFFF),A
mapst 07E15   ; LD ($FFFF),A
# not patched (data): mapst 0C831  LD ($FFFF),A  (17 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
# not patched (data): mapst 0C8AD  LD ($FFFF),A  (32 bytes of valid code before it; no valid code after it)
# not patched (data): mapsthl 11030  LD ($FFFC),HL  (7 RST or NOP opcodes around it (looks like data); 32 bytes of valid code before it)
