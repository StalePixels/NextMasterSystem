# Asterix and the Secret Mission (Europe, Brazil) (En,Fr,De), CRC32 DEF9B14E, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with the reference I/O logs of the title
# (300 s, no input), random input (600 s) and play (two 600 s runs, Asterix and Obelix).
# Scan entries (sitescan --entry), routines that no scanned path reaches:
#   E:8000, F:8000: the sound driver, called by the frame handler at $1890 with bank
#     ($C01C)+$0E in slot 2; the reference logs mapped only banks 14 and 15 there.
#   1D:8000 and the 20 words of its table at $801B: the object code in bank 29, called
#     from $7114 after LD A,$1D; RST $30. It does no I/O of its own.
#   $25F1, $25FD, $2B62, $2C19, $2C25, $2D7D, $2EDA, $2EFE, $303D, $3073: VDP routines in
#     bank 0, each after a RET or JP. $2C25 is LD BC,$00BE and an unrolled run of 32 OUTI
#     ending in RET at $2C68; the bytes around it look entered part way through, so every
#     OUTI in it is a site.
# Byte scan I/O patterns judged not code (verdicts in data/scan-verdicts.tsv): $3FD3 is the
# operand of JP NZ,$3FDB; bank 14 from $A000 on is an older program built for another address
# (its tables hold $D9xx-$DCxx words), which no path or recording reaches; the rest are in
# banks where no code runs (graphics, maps, tables).
name Asterix and the Secret Mission
cart DEF9B14E
hz 50		; No-Intro regions Europe, Brazil
# The title's curtains, at both sides of the screen, are priority cells: the characters that
# walk off the screen go behind them.
priority
# No free RST vector: $0000-$0002 (DI; JP $0165) becomes the vector, the game starts at
# $0165, where IM 1 becomes IM 2.
vector 00 io
start 0165
asm 00165 2   ; IM 1 -> IM 2
    im 2
endasm

# The sprite table: the frame handler's $2AA2 writes the 64 Y bytes and then the 64 X and
# tile pairs from 64 records of 3 bytes at $C300 (Y, X, tile), with one OUTI a byte: 192
# traps, about 29% of a frame in play. The page writes them with two jt_vwrite calls.
asm 02AA2 40   ; LD DE,$7F00 : RST $08 ... RET (the whole routine, to $2AC9)
    rst $00
    db far_io, pg_sprites, ent_sprites
    ret
endasm
page 0 sprites
; sprites: VRAM $3F00-$3F3F from $C300, $C303 ... (the Y bytes), then $3F80-$3FFF from the
; pairs at $C301, $C304 ... (X, tile). Returns what the game's routine leaves: A = $7F,
; BC = $00BE, DE = $7F80, HL = $C3C1, Z set. Keeps IX and IY. The game's stack holds only
; the far call's own words; IX and IY are kept in the page.
sprites:
        ld (.ix),ix
        ld (.iy),iy
        xor a                   ; the source as the game sees it
        ld hl,$C300
        ld de,$3F00
        ld bc,$0140             ; B = 1 byte a run, C = 64 runs
        ld ix,3
        ld iy,1
        call jt_vwrite
        xor a
        ld hl,$C301
        ld de,$3F80
        ld bc,$0240             ; B = 2 bytes a run, C = 64 runs
        ld iy,2
        call jt_vwrite
        ld ix,(.ix)
        ld iy,(.iy)
        ld hl,$C3C1
        ld de,$7F80
        ld bc,$00BE
        ld a,$7F
        cp a                    ; Z set, as the last OUTI leaves it
        ret
.ix:    dw 0
.iy:    dw 0
endpage
site 00009   ; OUT ($BF),A
site 0000C   ; OUT ($BF),A
site 0023E   ; OTIR
site 0027C   ; OUT ($BE),A
site 0029B   ; OTIR
site 0029D   ; OTIR
site 0029F   ; OTIR
site 002A1   ; OTIR
site 002A3   ; OTIR
site 002A5   ; OTIR
site 002B4   ; OTIR
site 0079D   ; OUTI
site 00966   ; OUT ($BE),A
site 00970   ; OUT ($BE),A
site 00973   ; OUT ($BE),A
site 009AF   ; OTIR
site 00A2B   ; OTIR
site 00B58   ; OTIR
site 00B7E   ; OUT ($BE),A
site 00B81   ; OUT ($BE),A
site 00B90   ; OUT ($BE),A
site 00BA6   ; OUT ($BE),A
site 00BAE   ; OUT ($BE),A
site 00BDF   ; OTIR
site 00BEA   ; OUT ($BE),A
site 00BED   ; OUT ($BE),A
site 00BFC   ; OUT ($BE),A
site 00C06   ; OUT ($BE),A
site 00C1A   ; OUT ($BE),A
site 00C22   ; OUT ($BE),A
site 00CBB   ; OTIR
site 0119B   ; OUT ($BE),A
site 011E6   ; OTIR
site 014A4   ; OUT ($BE),A
site 014B4   ; OUT ($BE),A
site 01662   ; OUT ($BE),A
site 0167D   ; OTIR
site 0181B   ; OUT ($3F),A
site 0181D   ; IN A,($DD)
site 01827   ; OUT ($3F),A
site 01829   ; IN A,($DD)
site 01832   ; OUT ($3F),A
site 0184F   ; IN A,($BF)
site 01851   ; IN A,($BF)
site 0185D   ; IN A,($BF)
site 0186B   ; IN A,($BF)
site 01871   ; IN A,($DD)
site 01948   ; OUT ($BE),A
site 0198B   ; OUT ($BE),A
site 0198F   ; OUT ($BE),A
site 01A71   ; OUT ($BF),A
site 01A75   ; OUT ($BF),A
site 01A7A   ; OUT ($BF),A
site 01A7E   ; OUT ($BF),A
site 01ABC   ; OUT ($BF),A
site 01AC0   ; OUT ($BF),A
site 01B56   ; OUT ($BE),A
site 01B5B   ; OUT ($BE),A
site 01B68   ; OUT ($BE),A
site 01B6D   ; OUT ($BE),A
site 01BA8   ; OUT ($BE),A
site 01BDE   ; OUT ($BE),A
site 01C5C   ; OUT ($BE),A
site 01C64   ; OUT ($BE),A
site 01C95   ; OUT ($BE),A
site 01CE8   ; OUTI
site 01CEA   ; IN A,($BE)
site 01CFE   ; OUT ($BE),A
site 01F21   ; OUTI
site 01F27   ; IN A,($BE)
site 01FC2   ; OUT ($BE),A
site 01FC8   ; OUT ($BE),A
site 01FCF   ; OUT ($BE),A
site 01FD5   ; OUT ($BE),A
site 01FE4   ; OUT ($BE),A
site 01FEA   ; IN A,($BE)
site 01FF1   ; OUT ($BE),A
site 01FF7   ; IN A,($BE)
site 01FFD   ; OUT ($BE),A
site 02003   ; IN A,($BE)
site 02009   ; OUT ($BE),A
site 02024   ; OUT ($BF),A
site 02028   ; OUT ($BF),A
site 0202D   ; OUT ($BF),A
site 02031   ; OUT ($BF),A
site 02074   ; OUT ($BF),A
site 02078   ; OUT ($BF),A
site 0207D   ; OUT ($BF),A
site 02081   ; OUT ($BF),A
site 024E9   ; OUT ($BE),A
site 02677   ; OUT ($BF),A
site 0267B   ; OUT ($BF),A
site 02682   ; OUTI
site 02686   ; OUTI
site 0297B   ; OUTI
site 0297F   ; OUTI
site 02983   ; OUTI
site 02987   ; OUT ($BE),A
site 02A00   ; OUTI
site 02A04   ; OUTI
site 02A08   ; OUTI
site 02A0C   ; OUTI
site 02A3C   ; OUT ($BF),A
site 02A40   ; OUT ($BF),A
site 02A47   ; OUTI
site 02A49   ; OUTI
site 02A4B   ; OUTI
site 02A4D   ; OUTI
site 02A4F   ; OUTI
site 02A51   ; OUTI
site 02A53   ; OUTI
site 02A55   ; OUTI
site 02A57   ; OUTI
site 02A59   ; OUTI
site 02A5B   ; OUTI
site 02A5D   ; OUTI
site 02A5F   ; OUTI
site 02A61   ; OUTI
site 02A63   ; OUTI
site 02A65   ; OUTI
site 02A67   ; OUTI
site 02A69   ; OUTI
site 02A6B   ; OUTI
site 02A6D   ; OUTI
site 02A6F   ; OUTI
site 02A71   ; OUTI
site 02A73   ; OUTI
site 02A75   ; OUTI
site 02A77   ; OUTI
site 02A79   ; OUTI
site 02A7B   ; OUTI
site 02A7D   ; OUTI
site 02A7F   ; OUTI
site 02A81   ; OUTI
site 02A83   ; OUTI
site 02A85   ; OUTI
site 02A8E   ; OUT ($BE),A
site 02ACC   ; OUT ($DE),A
site 02ACE   ; IN A,($DC)
site 02AD4   ; IN A,($00)
site 02B47   ; OUT ($BE),A
site 02B65   ; OUT ($BE),A
site 02B9F   ; OUT ($BF),A
site 02BA2   ; OUT ($BF),A
site 02BBC   ; OUT ($BE),A
site 02BC1   ; OUT ($BE),A
site 02C1D   ; OUTI
site 02C28   ; OUTI
site 02C2A   ; OUTI
site 02C2C   ; OUTI
site 02C2E   ; OUTI
site 02C30   ; OUTI
site 02C32   ; OUTI
site 02C34   ; OUTI
site 02C36   ; OUTI
site 02C38   ; OUTI
site 02C3A   ; OUTI
site 02C3C   ; OUTI
site 02C3E   ; OUTI
site 02C40   ; OUTI
site 02C42   ; OUTI
site 02C44   ; OUTI
site 02C46   ; OUTI
site 02C48   ; OUTI
site 02C4A   ; OUTI
site 02C4C   ; OUTI
site 02C4E   ; OUTI
site 02C50   ; OUTI
site 02C52   ; OUTI
site 02C54   ; OUTI
site 02C56   ; OUTI
site 02C58   ; OUTI
site 02C5A   ; OUTI
site 02C5C   ; OUTI
site 02C5E   ; OUTI
site 02C60   ; OUTI
site 02C62   ; OUTI
site 02C64   ; OUTI
site 02C66   ; OUTI
site 02CAE   ; OUTI
site 02CB5   ; OUT (C),A
site 02D2D   ; OUTI
site 02D34   ; OUT (C),A
site 02D81   ; OUT ($BF),A
site 02D86   ; OUT ($BF),A
site 02D8B   ; OUT ($BE),A
site 02D8F   ; OUT ($BE),A
site 02EEF   ; OUT (C),A
site 02EF6   ; OUT (C),A
site 02F29   ; INI
site 02F2D   ; INI
site 02F90   ; OUT (C),L
site 02F94   ; OUT (C),H
site 03085   ; OUTI
site 03089   ; OUTI
site 030C9   ; OUTI
site 030CB   ; OUTI
site 030CD   ; OUTI
site 030CF   ; OUTI
site 030D1   ; OUTI
site 030D3   ; OUTI
site 030D5   ; OUTI
site 030D7   ; OUTI
site 030D9   ; OUTI
site 030DB   ; OUTI
site 030DD   ; OUTI
site 030DF   ; OUTI
site 030E1   ; OUTI
site 030E3   ; OUTI
site 030E5   ; OUTI
site 030E7   ; OUTI
site 030E9   ; OUTI
site 030EB   ; OUTI
site 030ED   ; OUTI
site 030EF   ; OUTI
site 030F1   ; OUTI
site 030F3   ; OUTI
site 030F5   ; OUTI
site 030F7   ; OUTI
site 030F9   ; OUTI
site 030FB   ; OUTI
site 030FD   ; OUTI
site 030FF   ; OUTI
site 03101   ; OUTI
site 03103   ; OUTI
site 03105   ; OUTI
site 03107   ; OUTI
site 03109   ; OUTI
site 0310B   ; OUTI
site 0310D   ; OUTI
site 0310F   ; OUTI
site 03111   ; OUTI
site 03113   ; OUTI
site 03115   ; OUTI
site 03117   ; OUTI
site 03119   ; OUTI
site 0311B   ; OUTI
site 0311D   ; OUTI
site 0311F   ; OUTI
site 03121   ; OUTI
site 03123   ; OUTI
site 03125   ; OUTI
site 03127   ; OUTI
site 03129   ; OUTI
site 0312B   ; OUTI
site 0312D   ; OUTI
site 0312F   ; OUTI
site 03131   ; OUTI
site 03133   ; OUTI
site 03135   ; OUTI
site 03137   ; OUTI
site 03139   ; OUTI
site 0313B   ; OUTI
site 0313D   ; OUTI
site 0313F   ; OUTI
site 03141   ; OUTI
site 03143   ; OUTI
site 03145   ; OUTI
site 03147   ; OUTI
site 03177   ; OUTI
site 05807   ; OUT ($BE),A
site 0580B   ; OUT ($BE),A
site 05841   ; OUT ($BE),A
site 05845   ; OUT ($BE),A
site 05950   ; OUT ($BE),A
site 05954   ; OUT ($BE),A
site 05958   ; OUT ($BE),A
site 0595C   ; OUT ($BE),A
site 05981   ; OUT ($BE),A
site 05985   ; OUT ($BE),A
site 05989   ; OUT ($BE),A
site 0598D   ; OUT ($BE),A
site 05BDB   ; OUT ($BF),A
site 05BDF   ; OUT ($BF),A
site 06111   ; OUTI
site 06118   ; OUTI
site 0611A   ; OUTI
site 0611C   ; OUTI
site 0611E   ; OUTI
site 06120   ; OUTI
site 06122   ; OUTI
site 06124   ; OUTI
site 06126   ; OUTI
site 06128   ; OUTI
site 0612A   ; OUTI
site 0612C   ; OUTI
site 0612E   ; OUTI
site 06130   ; OUTI
site 06132   ; OUTI
site 06134   ; OUTI
site 06136   ; OUTI
site 06138   ; OUTI
site 0613A   ; OUTI
site 0613C   ; OUTI
site 0613E   ; OUTI
site 06140   ; OUTI
site 06142   ; OUTI
site 06144   ; OUTI
site 06146   ; OUTI
site 06148   ; OUTI
site 0614A   ; OUTI
site 0614C   ; OUTI
site 0614E   ; OUTI
site 06150   ; OUTI
site 06152   ; OUTI
site 06154   ; OUTI
site 06156   ; OUTI
site 06158   ; OUTI
site 0615A   ; OUTI
site 0615C   ; OUTI
site 0615E   ; OUTI
site 06160   ; OUTI
site 06162   ; OUTI
site 06164   ; OUTI
site 06166   ; OUTI
site 06168   ; OUTI
site 0616A   ; OUTI
site 0616C   ; OUTI
site 0616E   ; OUTI
site 06170   ; OUTI
site 06172   ; OUTI
site 06174   ; OUTI
site 06176   ; OUTI
site 06178   ; OUTI
site 0617A   ; OUTI
site 0617C   ; OUTI
site 0617E   ; OUTI
site 06180   ; OUTI
site 06182   ; OUTI
site 06184   ; OUTI
site 06186   ; OUTI
site 06188   ; OUTI
site 0618A   ; OUTI
site 0618C   ; OUTI
site 0618E   ; OUTI
site 06190   ; OUTI
site 06192   ; OUTI
site 06194   ; OUTI
site 06196   ; OUTI
site 06198   ; OUTI
site 0619A   ; OUTI
site 0619C   ; OUTI
site 0619E   ; OUTI
site 061A0   ; OUTI
site 061A2   ; OUTI
site 061A4   ; OUTI
site 061A6   ; OUTI
site 061A8   ; OUTI
site 061AA   ; OUTI
site 061AC   ; OUTI
site 061AE   ; OUTI
site 061B0   ; OUTI
site 061B2   ; OUTI
site 061B4   ; OUTI
site 061B6   ; OUTI
site 061B8   ; OUTI
site 061BA   ; OUTI
site 061BC   ; OUTI
site 061BE   ; OUTI
site 061C0   ; OUTI
site 061C2   ; OUTI
site 061C4   ; OUTI
site 061C6   ; OUTI
site 061C8   ; OUTI
site 061CA   ; OUTI
site 061CC   ; OUTI
site 061CE   ; OUTI
site 061D0   ; OUTI
site 061D2   ; OUTI
site 061D4   ; OUTI
site 061D6   ; OUTI
site 061D8   ; OUTI
site 061DA   ; OUTI
site 061DC   ; OUTI
site 061DE   ; OUTI
site 061E0   ; OUTI
site 061E2   ; OUTI
site 061E4   ; OUTI
site 061E6   ; OUTI
site 061E8   ; OUTI
site 061EA   ; OUTI
site 061EC   ; OUTI
site 061EE   ; OUTI
site 061F0   ; OUTI
site 061F2   ; OUTI
site 061F4   ; OUTI
site 061F6   ; OUTI
site 061F8   ; OUTI
site 061FA   ; OUTI
site 061FC   ; OUTI
site 061FE   ; OUTI
site 06200   ; OUTI
site 06202   ; OUTI
site 06204   ; OUTI
site 06206   ; OUTI
site 06208   ; OUTI
site 0620A   ; OUTI
site 0620C   ; OUTI
site 0620E   ; OUTI
site 06210   ; OUTI
site 06212   ; OUTI
site 06214   ; OUTI
site 06216   ; OUTI
site 06219   ; IN A,($DD)
site 07289   ; OUT ($BF),A
site 0728C   ; OUT ($BF),A
site 07290   ; OUTI
site 07294   ; OUTI
site 381ED   ; OUT ($7F),A
site 38313   ; OUT ($7F),A
site 384A5   ; OTIR
site 385BD   ; OUT ($7F),A
site 385C7   ; OUT ($7F),A
site 385E4   ; OUT ($7F),A
site 386E8   ; OUT ($7F),A
site 38774   ; OUT ($7F),A
site 38816   ; OUT ($7F),A
site 3881F   ; OUT ($7F),A
site 3882F   ; OUT ($7F),A
site 38895   ; OUT ($7F),A
site 388B2   ; OUT ($7F),A
site 3C1ED   ; OUT ($7F),A
site 3C313   ; OUT ($7F),A
site 3C4A5   ; OTIR
site 3C5BD   ; OUT ($7F),A
site 3C5C7   ; OUT ($7F),A
site 3C5E4   ; OUT ($7F),A
site 3C6E8   ; OUT ($7F),A
site 3C774   ; OUT ($7F),A
site 3C816   ; OUT ($7F),A
site 3C81F   ; OUT ($7F),A
site 3C82F   ; OUT ($7F),A
site 3C895   ; OUT ($7F),A
site 3C8B2   ; OUT ($7F),A
mapst 00033   ; LD ($FFFF),A
mapst 0016C   ; LD ($FFFC),A
mapst 00170   ; LD ($FFFD),A
mapst 00175   ; LD ($FFFE),A
mapst 0078A   ; LD ($FFFF),A
mapst 0188D   ; LD ($FFFF),A
mapst 01896   ; LD ($FFFF),A
mapst 020C5   ; LD ($FFFF),A
mapst 020F5   ; LD ($FFFF),A
mapst 02123   ; LD ($FFFF),A
mapst 0216B   ; LD ($FFFF),A
mapst 021F9   ; LD ($FFFF),A
mapst 02224   ; LD ($FFFF),A
mapst 02238   ; LD ($FFFF),A
mapst 02952   ; LD ($FFFF),A
mapst 029A6   ; LD ($FFFF),A
mapst 02C7F   ; LD ($FFFF),A
mapst 02CD9   ; LD ($FFFF),A
mapst 02CFE   ; LD ($FFFF),A
mapst 02D58   ; LD ($FFFF),A
mapst 030A4   ; LD ($FFFF),A
mapst 030B8   ; LD ($FFFF),A
mapst 03164   ; LD ($FFFF),A
mapst 05C0B   ; LD ($FFFF),A
mapst 05C47   ; LD ($FFFF),A
mapst 03038   # LD ($FFFF),A; after LD A,($C001); 32 bytes of valid code before it

# Asterix and the Secret Mission (Europe, Brazil) (En,Fr,De).cht, "Infinite Lives": RAM $C0DC
# is the lives count
poke "Infinite lives"
ar 00C0-DC09
endpoke

# Asterix and the Secret Mission (Europe, Brazil) (En,Fr,De).cht, "Infinite Hearts (Hits)":
# RAM $C0E3 is the hearts count, 3 when full
poke "Infinite hearts"
ar 00C0-E303
endpoke

# Asterix and the Secret Mission (Europe, Brazil) (En,Fr,De).cht, "Invulnerability": RAM $C527
# is the player's hit timer, non-zero while a hit by an enemy cannot land
poke "No enemy hits"
ar 00C5-2702
endpoke
