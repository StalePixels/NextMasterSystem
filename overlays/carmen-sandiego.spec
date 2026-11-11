# Where in the World is Carmen Sandiego (USA), CRC32 428B1E7C, 128K, Sega mapper.
# Drafted by tools/mkspec.py from the sitescan output, then decided by hand.
#
# Decisions:
# - $0008-$0037 are zero bytes that no code reaches, and the game has no RST of its own:
#   $20 is the io vector. $0000 cannot be: the reset button test at $3785 resets the
#   game with JP Z,$0000.
# - Scan entry points (sitescan --entry): the line interrupt handlers. The frame handler
#   at $048E jumps through ($C042) for a line interrupt and through ($C044) for a frame
#   interrupt. The handlers chain each other through $C042: $05FD, $0623, $0628, $063E,
#   $064C, $0651, $065B, $066B, $0683, $068D, then $04D8; $05E9 and $069E alternate.
#   $052A is the RET that one frame-interrupt setting ($0D27-$0D2D) stores.
# - Bank 1: the table at $4B7D holds 10 routines (called through $4600 for an index
#   under 10) and then pointers to compressed text (read through $4604). The routines
#   end in CALL $4D36, which pops its return address as a table of text pointers and
#   does not return there. The scanner decodes that text ($4BC3-$55C0) as code: its RST
#   calls, its jumps into RAM and slot 2 and its stores into ROM are not code. $0100-$01FF
#   is a bit-reversal table, which that text reaches.
# - No code runs in slot 2: banks 2-7 are graphics, text and data.
# - Code that no call, jump or table entry in the cart names, patched as code (it costs
#   nothing if it never runs): the VDP routines at $3432 (one byte with interrupts off),
#   $345D (fill), $34DF (sprite table clear), $3539, $3574, $3593, $35AC and $363E (tile
#   writes), the line handler variant at $05CC, and the bank 7 routine at $153F, which
#   runs on into $1520.
# - hsplit: the city screens scroll the street at the top, and the line handlers ($05E9,
#   $063E) set the H scroll back to 0 for the text panel below. Without the switch the
#   map screen after a flight showed a band of repeated text on the right of the panel.
# - The panel split. On the city, witness, ticket agent and map screens the frame handler
#   sets H for the picture above, and a chain of line handlers runs one per line from line
#   93: $0623 (nothing), $0628 (CRAM $1F), $063E (H = 0, so the panel's H is 0 from line
#   96), then one CRAM entry a line for the panel's palette (lines 99-114) and the VRAM
#   queue ($068D). Through the runtime each of these events comes about two lines after
#   the one before, so the H write came at about line 100 and the panel's first row (the
#   heading) showed the picture's H. A rastercode routine cannot do it: while its table is
#   valid the game gets no line events, and these carry the panel's palette and the VRAM
#   queue. The cave at $0008 takes the place of $0623 in the chain (the pointer at $061F):
#   its page entry waits for line 96 on the Next's line register and writes H = 0 through
#   the runtime, then the chain goes on as before. $063E's own write comes later with the
#   same value and changes nothing.
name Where in the World is Carmen Sandiego
cart 428B1E7C
hz 60		; No-Intro region USA
vector 20 io
hsplit
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
asm 0061E 3   ; LD HL,$0623 -> the cave at $0008
    ld hl,$0008
endasm
asm 00008 10  ; cave: the line event after line 93, in place of $0623
    rst $20
    db far_io, pg_split, ent_split
    ld hl,$0628         ; $0623's next handler, as $0623 sets it
    jp $05F5
endasm
page 0 split
; split: the panel's H = 0 at line 96, as the Master System applies the write of $063E.
; Runs in the game's line handler (interrupts off). Waits while the Next's line register
; (NextReg $1E, $1F) is under 96, then writes register 8 = 0 through the runtime's I/O
; entry (inline code 5, OUT ($BF),A), which also moves the copper's map switch column for
; the lines from the beam's line down (hsplit). Keeps BC; A and F change, as in $0623.
split:
        push bc
        ld bc,$243B
.w:     ld a,$1E
        out (c),a
        inc b
        in a,(c)
        dec b
        rrca
        jr c,.go                ; line 256 or more: past the panel's first line
        ld a,$1F
        out (c),a
        inc b
        in a,(c)
        dec b
        cp 96
        jr c,.w
.go:    pop bc
        xor a
        rst $20
        db 5                    ; OUT ($BF),A: H = 0
        ld a,$88
        rst $20
        db 5                    ; OUT ($BF),A: register 8
        ret
endpage
site 001DB   ; IN A,($3B)
site 00219   ; OUT ($3F),A
site 00269   ; OUT ($3F),A
site 0026B   ; IN A,($DD)
site 00275   ; OUT ($3F),A
site 00277   ; IN A,($DD)
site 0028F   ; IN A,($BF)
site 00295   ; IN A,($BF)
site 0029C   ; IN A,($BF)
site 002C8   ; OUT ($3E),A
site 002D0   ; OUT ($F2),A
site 002D3   ; IN A,($F2)
site 002DF   ; OUT ($F2),A
site 002E3   ; OUT ($3E),A
site 00490   ; IN A,($BF)
site 0050A   ; OUT ($BF),A
site 00510   ; OUT ($BF),A
site 00516   ; OUT ($BE),A
site 0051C   ; OUT ($BF),A
site 00522   ; OUT ($BF),A
site 00528   ; OUT ($BE),A
site 00539   ; OUT ($BF),A
site 0053F   ; OUT ($BF),A
site 00547   ; OUT ($BE),A
site 0054D   ; OUT ($BF),A
site 00553   ; OUT ($BF),A
site 0056C   ; OUT ($BE),A
site 00573   ; OUT ($BE),A
site 005EA   ; OUT ($BF),A
site 005F0   ; OUT ($BF),A
site 00608   ; OUT ($BF),A
site 0060E   ; OUT ($BF),A
site 00615   ; OUT ($BE),A
site 0061C   ; OUT ($BE),A
site 0062A   ; OUT ($BF),A
site 00630   ; OUT ($BF),A
site 00637   ; OUT ($BE),A
site 0063F   ; OUT ($BF),A
site 00645   ; OUT ($BF),A
site 0065C   ; OUT ($BF),A
site 00662   ; OUT ($BF),A
site 00675   ; OUT (C),A
site 01CCD   ; OUTI
site 01CE0   ; OUTI
site 01CF2   ; OUT ($BE),A
site 0341D   ; OUT ($BF),A
site 03420   ; OUT ($BF),A
site 03424   ; OUT ($BF),A
site 03427   ; OUT ($BF),A
site 0342A   ; OUT ($BE),A
site 0342F   ; OUT ($BE),A
site 03453   ; OUT ($BE),A
site 03476   ; OUT ($BF),A
site 0347B   ; OUT ($BF),A
site 03482   ; OUTI
site 0348C   ; OUT ($BF),A
site 03491   ; OUT ($BF),A
site 0349C   ; OUT ($BE),A
site 034A2   ; OUT ($BE),A
site 034A8   ; OUT ($BE),A
site 034AE   ; OUT ($BE),A
site 034B4   ; OUT ($BE),A
site 034BA   ; OUT ($BE),A
site 034C0   ; OUT ($BE),A
site 034C6   ; OUT ($BE),A
site 034D3   ; OUT ($BF),A
site 034DA   ; OUT ($BF),A
site 0360E   ; OUT ($BE),A
site 03612   ; IN A,($BE)
site 03616   ; IN A,($BE)
site 0361A   ; IN A,($BE)
site 03624   ; OUT ($BE),A
site 03628   ; IN A,($BE)
site 0362C   ; IN A,($BE)
site 03630   ; IN A,($BE)
site 03667   ; OUT ($BF),A
site 0366B   ; OUT ($BF),A
site 03676   ; OUT ($BF),A
site 0367C   ; OUT ($BF),A
site 03691   ; OUT ($BF),A
site 03697   ; OUT ($BF),A
site 03732   ; IN A,($DC)
site 03760   ; IN A,($DC)
site 0377B   ; IN A,($DC)
site 03785   ; IN A,($DD)
site 037C9   ; IN A,($DC)
site 057FC   ; OUT ($BE),A
site 05916   ; OUT ($BF),A
site 0591C   ; OUT ($BF),A
site 05922   ; OUTI
site 06936   ; OUT ($F0),A
site 0693F   ; OUT ($F1),A
site 06957   ; OUT ($7F),A
site 06967   ; OUT (C),D
site 0696D   ; OUT ($F1),A
site 0698F   ; OUT ($7F),A
site 06993   ; OUT ($7F),A
site 069C1   ; OTIR
site 069CF   ; OTIR
site 069D9   ; OUT ($F0),A
site 069DF   ; OUT ($F1),A
site 069EB   ; OUTI
site 069F1   ; OUTI
site 06AEF   ; OUT ($7F),A
site 06AF3   ; OUT ($7F),A
site 06B83   ; OUT ($7F),A
site 06B87   ; OUT ($7F),A
site 06BAF   ; OUT ($7F),A
site 06BB3   ; OUT ($7F),A
site 06BB7   ; OUT ($7F),A
site 06BBB   ; OUT ($7F),A
site 06BBE   ; OUT ($7F),A
site 06C24   ; OUT ($F0),A
site 06C2B   ; OUT ($F1),A
site 06C33   ; OUT ($F0),A
site 06C39   ; OUT ($F1),A
site 06D2E   ; OUT ($F0),A
site 06D38   ; OUT (C),L
site 06D41   ; OUT ($F0),A
site 06D5C   ; OUT (C),H
site 06D64   ; OUT ($F0),A
site 06D72   ; OUT ($F1),A
site 06D7E   ; OUT ($F0),A
site 06D87   ; OUT ($F1),A
site 06F48   ; OUT ($F0),A
site 06F51   ; OUT (C),A
site 06F56   ; OUT ($F0),A
site 06F5C   ; OUTI
site 06FCD   ; OUT ($7F),A
site 0709A   ; OUT ($7F),A
site 070C1   ; OUT ($7F),A
site 070C6   ; OUT ($7F),A
site 070F2   ; OUT ($F0),A
site 07100   ; OUT ($F1),A
site 0710E   ; OUT ($F0),A
site 071A5   ; OUTI
site 071A7   ; OUTI
site 071A9   ; OUTI
site 071AB   ; OUTI
site 071AD   ; OUTI
site 071AF   ; OUTI
site 071B1   ; OUTI
site 071B3   ; OUTI
site 071B5   ; OUTI
site 071B7   ; OUTI
site 071B9   ; OUTI
site 071F2   ; OUT ($7F),A
site 07248   ; OUT ($7F),A
site 07287   ; OUT ($7F),A
site 072E9   ; OUT ($7F),A
site 07309   ; OUT ($7F),A
site 07349   ; OUT ($7F),A
site 07353   ; OUT ($7F),A
site 0739B   ; OUT ($7F),A
mapldk 00200   # LD HL,$FFFC; LD (HL),$00
maphl 00206   # LD (HL),$00, HL = $FFFD
maphl 00209   # LD (HL),$01, HL = $FFFE
maphl 0020C   # LD (HL),$02, HL = $FFFF
mapst 037E7   ; LD ($FFFF),A
mapst 0380C   ; LD ($FFFF),A
mapst 0388A   ; LD ($FFFF),A
mapst 0390E   ; LD ($FFFF),A
mapst 03A0A   ; LD ($FFFF),A
mapst 03A4D   ; LD ($FFFF),A
mapst 03A6C   ; LD ($FFFF),A
mapst 03AA4   ; LD ($FFFF),A
mapst 03ABA   ; LD ($FFFF),A
mapst 03ACA   ; LD ($FFFF),A
mapst 03AF3   ; LD ($FFFF),A
mapst 05939   ; LD ($FFFF),A
mapst 05940   ; LD ($FFFF),A
mapst 01542   ; LD ($FFFF),A
mapst 01572   ; LD ($FFFF),A
site 005DB   ; OUT ($BF),A
site 005E1   ; OUT ($BF),A
site 005E6   ; OUT ($BE),A
site 03436   ; OUT ($BF),A
site 03439   ; OUT ($BF),A
site 0343C   ; OUT ($BE),A
site 03443   ; OUT ($BE),A
site 0346A   ; OUT ($BE),A
site 0346F   ; OUT ($BE),A
site 034E2   ; OUT ($BF),A
site 034E6   ; OUT ($BF),A
site 034EA   ; OUT ($BE),A
site 034EF   ; OUT ($BF),A
site 034F3   ; OUT ($BF),A
site 034F7   ; OUT ($BE),A
site 03578   ; OUT ($BE),A
site 0357D   ; OUT ($BE),A
site 03584   ; OUT ($BE),A
site 0358B   ; OUT ($BE),A
site 03564   ; OUT ($BE),A
site 0359A   ; OUT ($BE),A
site 0359F   ; OUT ($BE),A
site 035B7   ; OUT ($BE),A
site 035BD   ; OUT ($BE),A
site 03646   ; OUT ($BE),A
site 0364C   ; OUT ($BE),A
