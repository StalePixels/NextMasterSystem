# Power Strike II (Europe, Brazil) (En), CRC32 A109A6FE, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (60 s and 10 min of
# random input, 120 s of the intro with no input) and these entries:
# - 1F:88CF, 1F:88EB, 1F:AEFB: bank 31 routines that map a picture's bank into slot 1 before
#   they read it (the intro pictures were wrong tiles without their mapper stores).
# - 2:464D: a bank 2 routine that maps slot 2 through $FFFF.
# - Line interrupts. $0038 jumps to $DF00 for a line interrupt. The game copies a 240-byte
#   block there with $A39A (bank 31) and picks the handler by writing $DF01 (and $DF02):
#   $A438, $A948 and $AD5D start with a JP to a chain of handlers in the cart (1F:A94B-AA2F,
#   AD60-AEDC); each handler writes the next one's address. $A3BD (copied by $A3AE) is run in
#   RAM: it starts JR $+2, and each handler writes the JR offset to pick the next one
#   (1F:A3BF, A3CF, A3DF, A40A). The site lines patch the cart bytes, so the copy carries the
#   patches. The intro recording ran the $A3BD block; no recording ran the $A94B chain.
# - The tables at $29ED (21 entries) and $2EEF (entries 1-12), read by $29DD and $2EE1.
# - Stage code in banks 4 and 5, run in slot 2 through $1C05 (bank from $C536, address from
#   $C3E4): 4:9E15, A376, AB82, B3A6 and 5:8071, 87D6, 9534, A2BD (one copy for each stage:
#   it sets VDP register 0 bit 5 and fills VRAM through $0BB8), 5:A84A and 5:A8A4. No
#   recording left stage 1; the copies call $0BB8, $0BAF and $0CD0 as stage 1's code does.
name Power Strike II
hz 50		; No-Intro regions Europe, Brazil
cart A109A6FE
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 0001E   ; IN A,($7E)
site 00039   ; IN A,($BF)
site 0008D   ; OUT ($BF),A
site 00091   ; OUT ($BF),A
site 00096   ; OUT ($BF),A
site 0009A   ; OUT ($BF),A
site 0009F   ; OUT ($BF),A
site 000A3   ; OUT ($BF),A
site 000A8   ; OUT ($BF),A
site 000AC   ; OUT ($BF),A
site 000BF   ; OUT ($BF),A
site 000C3   ; OUT ($BF),A
site 000C6   ; OUT ($BF),A
site 000CA   ; OUT ($BF),A
site 000D0   ; IN A,($DD)
site 00145   ; IN A,($DD)
site 00958   ; OUT ($BF),A
site 0095C   ; OUT ($BF),A
site 00973   ; OUT ($BE),A
site 00A09   ; IN A,($DC)
site 00ADB   ; IN A,($BF)
site 00AE5   ; OUT ($BF),A
site 00AE8   ; OUT ($BF),A
site 00AFF   ; OUT ($BF),A
site 00B03   ; OUT ($BF),A
site 00B07   ; OUT ($BE),A
site 00B35   ; OUT ($BF),A
site 00B39   ; OUT ($BF),A
site 00B53   ; OUT ($BF),A
site 00B57   ; OUT ($BF),A
site 00B62   ; OUT ($BF),A
site 00B66   ; OUT ($BF),A
site 00BB0   ; OUT ($BF),A
site 00BB5   ; OUT ($BF),A
site 00BBC   ; OUT ($BE),A
site 00BC3   ; OUT ($BE),A
site 00BD0   ; OUT ($BE),A
site 00BD7   ; OUT ($BE),A
site 00BF7   ; OUT ($BE),A
site 00BFE   ; OUT ($BE),A
site 00C10   ; OUT ($BF),A
site 00C15   ; OUT ($BF),A
site 00C24   ; OUT ($BE),A
site 00C2B   ; OUT ($BE),A
site 00C8E   ; OUT ($BF),A
site 00C95   ; OUT ($BF),A
site 00C9F   ; OUT ($BE),A
site 00CA6   ; OUT ($BE),A
site 00CAF   ; OUT ($BE),A
site 00CB4   ; OUT ($BE),A
site 00CD2   ; OUT ($BF),A
site 00CD9   ; OUT ($BF),A
site 00CE3   ; OUT ($BE),A
site 00CEA   ; OUT ($BE),A
site 00CF1   ; OUT ($BE),A
site 00CF6   ; OUT ($BE),A
site 00F86   ; OUT ($BF),A
site 00F8A   ; OUT ($BF),A
site 00FB5   ; OUTI
site 00FB8   ; OUTI
site 00FBB   ; OUTI
site 00FBE   ; OUTI
site 00FC5   ; OUT ($BF),A
site 00FC9   ; OUT ($BF),A
site 00FE0   ; OUTI
site 00FE2   ; OUTI
site 00FE4   ; OUTI
site 00FE6   ; OUTI
site 00FE8   ; OUTI
site 00FEA   ; OUTI
site 00FEC   ; OUTI
site 00FEE   ; OUTI
site 00FF7   ; OUT ($BF),A
site 00FFB   ; OUT ($BF),A
site 01012   ; OUT ($BE),A
site 0103E   ; OUTI
site 01041   ; OUTI
site 01044   ; OUTI
site 01047   ; OUTI
site 0104E   ; OUT ($BE),A
site 01053   ; OUT ($BF),A
site 01057   ; OUT ($BF),A
site 0106E   ; OUTI
site 01070   ; OUTI
site 01072   ; OUTI
site 01074   ; OUTI
site 01076   ; OUTI
site 01078   ; OUTI
site 0107A   ; OUTI
site 0107C   ; OUTI
site 010A6   ; OUTD
site 010A9   ; OUTD
site 010AC   ; OUTD
site 010AF   ; OUTD
site 010B6   ; OUT ($BE),A
site 010BB   ; OUT ($BF),A
site 010BF   ; OUT ($BF),A
site 010DB   ; OUTI
site 010DD   ; OUTD
site 010E1   ; OUTI
site 010E3   ; OUTD
site 010E7   ; OUTI
site 010E9   ; OUTD
site 010ED   ; OUTI
site 010EF   ; OUTD
site 010F9   ; OUT ($BF),A
site 010FD   ; OUT ($BF),A
site 01104   ; OUTI
site 01106   ; OUTI
site 01108   ; OUTI
site 0110A   ; OUTI
site 0110C   ; OUTI
site 0110E   ; OUTI
site 01110   ; OUTI
site 01112   ; OUTI
site 01114   ; OUTI
site 01116   ; OUTI
site 01118   ; OUTI
site 0111A   ; OUTI
site 0111C   ; OUTI
site 0111E   ; OUTI
site 01120   ; OUTI
site 01122   ; OUTI
site 01124   ; OUTI
site 01126   ; OUTI
site 01128   ; OUTI
site 0112A   ; OUTI
site 0112C   ; OUTI
site 0112E   ; OUTI
site 01130   ; OUTI
site 01132   ; OUTI
site 01134   ; OUTI
site 01136   ; OUTI
site 01138   ; OUTI
site 0113A   ; OUTI
site 0113C   ; OUTI
site 0113E   ; OUTI
site 01140   ; OUTI
site 01142   ; OUTI
site 01166   ; OUT ($BF),A
site 0116C   ; OUT ($BF),A
site 01178   ; OUTI
site 0117A   ; OUTI
site 0117C   ; OUTI
site 0117E   ; OUTI
site 01180   ; OUTI
site 01182   ; OUTI
site 01184   ; OUTI
site 01186   ; OUTI
site 011B0   ; OUTI
site 011B3   ; OUTI
site 011B7   ; OUTI
site 011BA   ; OUTI
site 01212   ; OUT ($BF),A
site 01219   ; OUT ($BF),A
site 01226   ; OUTI
site 01228   ; OUTI
site 0122A   ; OUTI
site 0122C   ; OUTI
site 0123C   ; OUTI
site 0123E   ; OUTI
site 01240   ; OUTI
site 01242   ; OUTI
site 01251   ; OUT ($BF),A
site 01258   ; OUT ($BF),A
site 01272   ; OUTI
site 01275   ; OUTI
site 01279   ; OUTI
site 0127C   ; OUTI
site 01286   ; OUTI
site 01288   ; OUTI
site 0128A   ; OUTI
site 0128C   ; OUTI
site 0128E   ; OUTI
site 01290   ; OUTI
site 01292   ; OUTI
site 01294   ; OUTI
site 012A2   ; OUT ($BF),A
site 012A9   ; OUT ($BF),A
site 012C3   ; OUTI
site 012C6   ; OUTI
site 012CA   ; OUTI
site 012CD   ; OUTI
site 01505   ; OUT (C),A
site 01507   ; OUT (C),H
site 0150B   ; OUT ($BE),A
site 01511   ; OUT ($BE),A
site 01529   ; OUT ($BF),A
site 0152D   ; OUT ($BF),A
site 01537   ; OUT ($BF),A
site 0153B   ; OUT ($BF),A
site 01579   ; OUT ($BF),A
site 0157D   ; OUT ($BF),A
site 017CF   ; OUT ($BF),A
site 017D6   ; OUT ($BF),A
site 017D9   ; OUT ($BE),A
site 017DF   ; OUT ($BE),A
site 01B6E   ; OUT ($BF),A
site 01B72   ; OUT ($BF),A
site 01B87   ; OUT ($BE),A
site 01B8E   ; OUT ($BE),A
site 02249   ; OUT ($BF),A
site 02250   ; OUT ($BF),A
site 02259   ; OUTI
site 02AE1   ; OUT ($BF),A
site 02AE5   ; OUT ($BF),A
site 03213   ; OUT ($7F),A
site 03219   ; OUT ($7F),A
site 03225   ; OUT ($7F),A
site 03243   ; OUT ($7F),A
site 0324A   ; OUT ($7F),A
site 09CFF   ; OUT ($BF),A
site 09D06   ; OUT ($BF),A
site 09D0B   ; OUT ($BE),A
site 11E25   ; OUT ($BF),A
site 11E29   ; OUT ($BF),A
site 12386   ; OUT ($BF),A
site 1238A   ; OUT ($BF),A
site 12B92   ; OUT ($BF),A
site 12B96   ; OUT ($BF),A
site 133B6   ; OUT ($BF),A
site 133BA   ; OUT ($BF),A
site 14081   ; OUT ($BF),A
site 14085   ; OUT ($BF),A
site 147E6   ; OUT ($BF),A
site 147EA   ; OUT ($BF),A
site 15544   ; OUT ($BF),A
site 15548   ; OUT ($BF),A
site 162CD   ; OUT ($BF),A
site 162D1   ; OUT ($BF),A
site 16872   ; OUT ($BE),A
site 16877   ; OUT ($BE),A
site 1687C   ; OUT ($BE),A
site 16885   ; OUT ($BE),A
site 168B5   ; OUT ($BF),A
site 168B9   ; OUT ($BF),A
site 7C827   ; OUT ($BF),A
site 7C82C   ; OUT ($BF),A
site 7C82F   ; OUT ($BE),A
site 7C83D   ; OUT ($BF),A
site 7C842   ; OUT ($BF),A
site 7C849   ; OUT ($BE),A
site 7C850   ; OUT ($BE),A
site 7C857   ; OUT ($BF),A
site 7C85C   ; OUT ($BF),A
site 7C877   ; OUT ($BF),A
site 7C87C   ; OUT ($BF),A
site 7C883   ; OUT ($BE),A
site 7C88A   ; OUT ($BE),A
site 7C891   ; OUT ($BF),A
site 7C896   ; OUT ($BF),A
site 7C97B   ; OUT (C),A
site 7C987   ; OUTI
site 7CA89   ; OUT (C),A
site 7CA9B   ; OUTI
site 7CB66   ; OUT (C),A
site 7CB78   ; OUTI
site 7CB81   ; OUT ($BF),A
site 7CB89   ; OUT ($BF),A
site 7E3C1   ; OUT ($BF),A
site 7E3C5   ; OUT ($BF),A
site 7E3D1   ; OUT ($BF),A
site 7E3D5   ; OUT ($BF),A
site 7E3E0   ; OUT ($BF),A
site 7E3E4   ; OUT ($BF),A
site 7E3EB   ; OUT ($BF),A
site 7E3EE   ; IN A,($7E)
site 7E3F1   ; IN A,($7E)
site 7E3FF   ; OUT ($BF),A
site 7E40F   ; OUT ($BF),A
site 7E413   ; OUT ($BF),A
site 7E41A   ; OUT ($BF),A
site 7E41E   ; OUT ($BF),A
site 7E43C   ; OUT ($BF),A
site 7E440   ; OUT ($BF),A
site 7E447   ; OUT ($BF),A
site 7E44B   ; OUT ($BF),A
site 7E94D   ; OUT ($BF),A
site 7E951   ; OUT ($BF),A
site 7E962   ; OUT ($BF),A
site 7E966   ; OUT ($BF),A
site 7E969   ; OUT ($BF),A
site 7E96D   ; OUT ($BF),A
site 7E97E   ; OUT ($BF),A
site 7E982   ; OUT ($BF),A
site 7E987   ; OUT ($BF),A
site 7E98B   ; OUT ($BF),A
site 7E99C   ; OUT ($BF),A
site 7E9A0   ; OUT ($BF),A
site 7E9A5   ; OUT ($BF),A
site 7E9A9   ; OUT ($BF),A
site 7E9BA   ; OUT ($BF),A
site 7E9BE   ; OUT ($BF),A
site 7E9C3   ; OUT ($BF),A
site 7E9C7   ; OUT ($BF),A
site 7E9D8   ; OUT ($BF),A
site 7E9DC   ; OUT ($BF),A
site 7E9E1   ; OUT ($BF),A
site 7E9E5   ; OUT ($BF),A
site 7E9F6   ; OUT ($BF),A
site 7E9FA   ; OUT ($BF),A
site 7E9FF   ; OUT ($BF),A
site 7EA03   ; OUT ($BF),A
site 7EA13   ; OUT ($BF),A
site 7EA17   ; OUT ($BF),A
site 7EA1C   ; OUT ($BF),A
site 7EA20   ; OUT ($BF),A
site 7EA30   ; OUT ($BF),A
site 7EA34   ; OUT ($BF),A
site 7EA3B   ; OUT ($BF),A
site 7EA3F   ; OUT ($BF),A
site 7ECBE   ; OUT ($BF),A
site 7ECC1   ; OUT ($BF),A
site 7ECC9   ; OUT ($BE),A
site 7ECCE   ; OUT ($BE),A
site 7ECD4   ; OUT ($BF),A
site 7ECD7   ; OUT ($BF),A
site 7ECE0   ; OUT ($BE),A
site 7ECE5   ; OUT ($BE),A
site 7ED62   ; OUT ($BF),A
site 7ED66   ; OUT ($BF),A
site 7ED76   ; OUT ($BF),A
site 7ED7A   ; OUT ($BF),A
site 7ED7F   ; OUT ($BF),A
site 7ED83   ; OUT ($BF),A
site 7ED95   ; OUT ($BF),A
site 7ED99   ; OUT ($BF),A
site 7EDAB   ; OUT ($BF),A
site 7EDAF   ; OUT ($BF),A
site 7EDC1   ; OUT ($BF),A
site 7EDC5   ; OUT ($BF),A
site 7EDD7   ; OUT ($BF),A
site 7EDDB   ; OUT ($BF),A
site 7EDED   ; OUT ($BF),A
site 7EDF1   ; OUT ($BF),A
site 7EE03   ; OUT ($BF),A
site 7EE07   ; OUT ($BF),A
site 7EE19   ; OUT ($BF),A
site 7EE1D   ; OUT ($BF),A
site 7EE2F   ; OUT ($BF),A
site 7EE33   ; OUT ($BF),A
site 7EE45   ; OUT ($BF),A
site 7EE49   ; OUT ($BF),A
site 7EE5B   ; OUT ($BF),A
site 7EE5F   ; OUT ($BF),A
site 7EE71   ; OUT ($BF),A
site 7EE75   ; OUT ($BF),A
site 7EE87   ; OUT ($BF),A
site 7EE8B   ; OUT ($BF),A
site 7EE9D   ; OUT ($BF),A
site 7EEA1   ; OUT ($BF),A
site 7EEB3   ; OUT ($BF),A
site 7EEB7   ; OUT ($BF),A
site 7EEC9   ; OUT ($BF),A
site 7EECD   ; OUT ($BF),A
site 7EEDD   ; OUT ($BF),A
site 7EEE1   ; OUT ($BF),A
site 7EEE8   ; OUT ($BF),A
site 7EEEC   ; OUT ($BF),A
site 7EF1B   ; OUT ($BF),A
site 7EF20   ; OUT ($BF),A
site 7EF25   ; OUT ($BE),A
site 7EF2B   ; OUT ($BE),A
mapst 00007   ; LD ($FFFC),A
mapst 0000A   ; LD ($FFFD),A
mapst 0000D   ; LD ($FFFE),A
mapst 00010   ; LD ($FFFF),A
mapst 00085   ; LD ($FFFE),A
mapsthl 000DA   ; LD ($FFFE),HL
mapsthl 000E1   ; LD ($FFFE),HL
mapst 000F6   ; LD ($FFFE),A
mapst 00112   ; LD ($FFFE),A
mapst 0011A   ; LD ($FFFF),A
mapst 00122   ; LD ($FFFE),A
mapst 00173   ; LD ($FFFE),A
mapsthl 00196   ; LD ($FFFE),HL
mapsthl 00204   ; LD ($FFFE),HL
mapsthl 0025B   ; LD ($FFFE),HL
mapsthl 00310   ; LD ($FFFE),HL
mapst 0031B   ; LD ($FFFE),A
mapst 0032E   ; LD ($FFFE),A
mapst 00338   ; LD ($FFFF),A
mapst 003C0   ; LD ($FFFE),A
mapst 0040E   ; LD ($FFFE),A
mapst 00592   ; LD ($FFFE),A
mapst 00964   ; LD ($FFFF),A
mapst 0097F   ; LD ($FFFF),A
mapst 0099B   ; LD ($FFFE),A
mapst 009CB   ; LD ($FFFE),A
mapst 009E9   ; LD ($FFFE),A
mapsthl 00A05   ; LD ($FFFE),HL
mapsthl 00B9B   ; LD ($FFFE),HL
mapst 0115A   ; LD ($FFFE),A
mapst 0115D   ; LD ($FFFF),A
mapst 01197   ; LD ($FFFE),A
mapst 011E2   ; LD ($FFFE),A
mapst 0120C   ; LD ($FFFF),A
mapst 0131A   ; LD ($FFFE),A
mapst 01880   ; LD ($FFFE),A
mapst 0188A   ; LD ($FFFF),A
mapst 01B7A   ; LD ($FFFF),A
mapst 01B9A   ; LD ($FFFF),A
mapsthl 01BAD   ; LD ($FFFE),HL
mapst 01C08   ; LD ($FFFF),A
mapsthl 0221B   ; LD ($FFFE),HL
mapsthl 02224   ; LD ($FFFE),HL
mapsthl 0226C   ; LD ($FFFE),HL
mapst 0228D   ; LD ($FFFF),A
mapst 022BF   ; LD ($FFFF),A
mapst 022D2   ; LD ($FFFF),A
mapsthl 023CF   ; LD ($FFFE),HL
mapsthl 0245E   ; LD ($FFFE),HL
mapsthl 024D0   ; LD ($FFFE),HL
mapst 02873   ; LD ($FFFF),A
mapst 0288A   ; LD ($FFFF),A
mapst 0289B   ; LD ($FFFF),A
mapst 02923   ; LD ($FFFF),A
mapst 029C9   ; LD ($FFFF),A
mapst 030E9   ; LD ($FFFF),A
mapst 03250   ; LD ($FFFF),A
mapst 03310   ; LD ($FFFF),A
mapst 034AD   ; LD ($FFFF),A
mapst 034F9   ; LD ($FFFF),A
mapst 035B4   ; LD ($FFFF),A
mapst 03897   ; LD ($FFFF),A
mapst 0393E   ; LD ($FFFF),A
mapst 0394B   ; LD ($FFFF),A
mapst 03A44   ; LD ($FFFF),A
mapst 03A75   ; LD ($FFFF),A
mapst 08021   ; LD ($FFFF),A
mapst 08088   ; LD ($FFFF),A
mapst 080DB   ; LD ($FFFF),A
mapst 08146   ; LD ($FFFF),A
mapst 08169   ; LD ($FFFF),A
mapst 0818B   ; LD ($FFFF),A
mapst 081AE   ; LD ($FFFF),A
mapst 08666   ; LD ($FFFF),A
mapst 0867F   ; LD ($FFFF),A
mapst 08697   ; LD ($FFFE),A
mapst 09CD6   ; LD ($FFFF),A
mapst 09D17   ; LD ($FFFF),A
mapst 0C76F   ; LD ($FFFE),A
mapst 0C793   ; LD ($FFFE),A
mapst 0C7C6   ; LD ($FFFE),A
mapst 0C7EB   ; LD ($FFFE),A
mapst 0D958   ; LD ($FFFE),A
mapst 0D997   ; LD ($FFFE),A
mapst 0D9EF   ; LD ($FFFE),A
mapst 7C8D1   ; LD ($FFFE),A
mapst 7C8ED   ; LD ($FFFE),A
mapst 7C941   ; LD ($FFFE),A
mapst 7C992   ; LD ($FFFE),A
mapst 7C9E0   ; LD ($FFFE),A
mapst 7CA2C   ; LD ($FFFE),A
mapst 7CAA6   ; LD ($FFFE),A
mapst 7CAFE   ; LD ($FFFE),A
mapst 7CDB1   ; LD ($FFFE),A
mapst 7CF7D   ; LD ($FFFE),A
mapst 7E051   ; LD ($FFFE),A
mapst 7E170   ; LD ($FFFE),A
mapst 7E1BD   ; LD ($FFFE),A
mapst 7E2C5   ; LD ($FFFE),A
mapst 7EEFE   ; LD ($FFFE),A
mapst 7CD80   # LD ($FFFE),A; after LD A,(IX+$00); 32 bytes of valid code before it
# The intro's name table rows. $8F2A (bank 31), on each frame that $C8CC is set, writes six
# rows of 20 name table words from RAM buffers through $8F64: for each word a control write of
# its address (DE, then DE + 2), the two data bytes, with DI and EI around them. 240 single
# writes a frame held the Next frame at 83% runtime and slowed the intro. The far call to nrow
# writes each row with one jt_vwrite.
asm 7CF64 6   ; LD B,$14; LD A,E; DI; OUT ($BF),A -> far call to nrow, then RET
    rst $00
    db far_io, pg_nrow, ent_nrow
    ret
endasm
# The title. The title screen is a panel (name table columns 0-15) and a frame (rows 0 and
# 23, column 31) round a window where the game runs a demo, so the score routine ($5AB8,
# bank 2) puts the score's ones digit in the sprite table at x $3E, y $04, over HI-SCORE.
# Every panel and frame cell has the priority bit and no colour-0 pixels, so on the Master
# System no sprite pixel shows outside the window (x 128-247, lines 8-183). The priority
# switch costs the intro up to 1,457% of a frame. Once a frame the frame handler calls
# title_clip, a code cave in the unused bytes at the end of bank 0, in place of its frame
# counter increment; title_clip sets the sprite clip window to the window while the
# title's frame is on screen. The CALL uses the stack at the depth where the handler itself
# calls $0F83 and $11E6. A far call (1,740 cycles) is too slow here: the intro has frames
# close to full, and it falls about 10 frames behind by frame 3,460.
label title_clip 03F00
asm 000CC 4   ; LD HL,$C410; INC (HL) -> CALL title_clip
    call title_clip
    nop
endasm
page 0 nrow
; nrow: HL = the source (40 bytes), DE = the VDP control word of the first cell. Writes the
; 40 bytes to VRAM from DE as $8F64-$8F7A do and returns as they do: HL and DE 40 bytes on,
; B = 0, A = the last byte written, C, IX, IY and F kept, interrupts on. Runs with interrupts
; off on a stack of its own.
nrow:   di
        ld (.sp),sp
        ld sp,stk
        push af
        push bc
        push ix
        push iy
        ld bc,$2801             ; 40 bytes, 1 run
        ld ix,40
        ld iy,40
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld bc,40
        add hl,bc
        ex de,hl
        add hl,bc
        ex de,hl
        pop iy
        pop ix
        pop bc
        ld b,0
        pop af                  ; F as at the call
        dec hl
        ld a,(hl)               ; the last byte written
        inc hl
        ld sp,(.sp)
        ei
        ret
.sp:    dw 0
        ds 32
stk:
endpage
# title_clip: the frame counter increment ($C410), then the sprite clip window: the title's
# window (SMS x 128-247, lines 8-183) while the name table holds the title's frame (cells
# (16,0), (15,1), (31,1) and (16,23) have the priority bit, (16,1) does not), else the
# window clip_update (fw2.asm) sets. Runs in the frame handler with interrupts off.
# Runtime internals: the VRAM copy in pages 28-29 (SHADOW_PAGE in memplan.inc), mapped at
# $4000 for the reads; the sprite clip values of clip_update. Returns HL = $C410 and
# changes A and F, as the replaced code does. Bank 0 stays in slot 0 ($FFFD is written only
# at power-on).
asm 03F00 157   ; unused ($FF bytes): the title_clip cave
    OPT --zxnext            ; NEXTREG, ADD HL,nn
        ld hl,$C410
        inc (hl)
        ld hl,(nt_base)
        ld a,h
        and $3F
        ld h,a
        rlca
        rlca
        rlca
        and 1
        add a,28                ; SHADOW_PAGE
        nextreg $52,a
        ld a,h
        and $1F
        or $40
        ld h,a
        add hl,(0*32+16)*2+1    ; the attribute byte of cell (16,0)
        bit 4,(hl)
        jr z,title_clip__no
        add hl,62               ; (15,1)
        bit 4,(hl)
        jr z,title_clip__no
        inc hl
        inc hl                  ; (16,1)
        bit 4,(hl)
        jr nz,title_clip__no
        add hl,30               ; (31,1)
        bit 4,(hl)
        jr z,title_clip__no
        add hl,1378             ; (16,23)
        bit 4,(hl)
        jr z,title_clip__no
        scf
        jr title_clip__m
title_clip__no:
        or a
title_clip__m:
        ld a,(cur_mmu+2)        ; NEXTREG and LD keep the carry
        nextreg $52,a
        nextreg $1C,%00000010   ; reset the sprite clip index
        jr nc,title_clip__std
        nextreg $19,17+64       ; SMS x 128 (over-border units of 2 pixels)
        nextreg $19,144-4       ; SMS x 247
        nextreg $19,32+8        ; line 8
        nextreg $19,32+183      ; line 183
        ld hl,$C410
        ret
title_clip__std:
        ld a,(vdp_regs+0)
        and $20                 ; column 0 hidden: the window starts 8 pixels in
        jr z,title_clip__x
        ld a,4
title_clip__x:
        add a,17
        nextreg $19,a
        nextreg $19,144         ; SMS x 255
        ld a,(vdp_regs+0)       ; 224-line mode: register 0 bit 1 and register 1 bit 4
        and 2
        jr z,title_clip__192
        ld a,(vdp_regs+1)
        and $10
        jr z,title_clip__192
        nextreg $19,16
        nextreg $19,239
        ld hl,$C410
        ret
title_clip__192:
        nextreg $19,32
        nextreg $19,223
        ld hl,$C410
        ret
endasm
# Power Strike II (Europe, Brazil).cht, "Infinite Lives": RAM $C314 is the lives count
poke "Infinite lives"
ar 00C3-1409
endpoke

# Power Strike II (Europe, Brazil).cht, "Invulnerability" (Game Genie): $8434 in bank 3 is
# changed from $A7 to $00, so the ship takes no hits
poke "Invincible"
gg 004-347-7F4
endpoke

# Power Strike II (Europe, Brazil).cht, "Start with ?? Lives, instead of 2": the cart byte
# at $028D is the lives count of a new game
poke "Start lives ??"
gg ??2-8DF-E62
endpoke

# Power Strike II (Europe, Brazil).cht, "Keep Primary Weapon Power after Dying", "Keep Secondary
# Weapon Power after Dying", "... after Continuing": a death and a continue no longer lower
# the weapon power
poke "Keep weapon power"
gg 3A9-947-2A2
gg 3A9-9C7-2A2
gg 3A9-D27-2A2
gg 3A9-D57-2A2
endpoke

# Power Strike II (Europe, Brazil).cht, "Max Primary Weapon Power": RAM $C330 is the
# primary weapon power
poke "Max main weapon"
ar 00C3-300E
endpoke

# Power Strike II (Europe, Brazil).cht, "Max Secondary Weapon Power": RAM $C331 is the
# secondary weapon power
poke "Max sub weapon"
ar 00C3-3105
endpoke

# Power Strike II (Europe, Brazil).cht, "Temporary Invincibility after Dying and at Start of
# Level Lasts 1.5x Longer" and "... 2x Longer": the cart byte at $806A (bank 3) is the start
# value of the $D026 timer, 120 in the game; the player sets the length
poke "Spawn invincible ??"
gg ??0-6A7-08B
endpoke

# Power Strike II (Europe, Brazil).cht, "Set Difficulty to Hidden Comfort Difficulty": RAM
# $C300 is the rank; $00 is RANK0 COMFORT, which the Options menu does not offer
poke "Comfort rank"
ar 00C3-0000
endpoke

# Power Strike II (Europe, Brazil).cht, "Enable Debug Options": RAM $C30D = 1 adds STAGE,
# DEATH and BOSS TEST to the Options menu (STAGE picks the round a new game starts in) and
# TITLE LOGO, ENDING TEST and ROUND DEMO to the main menu
poke "Debug menus, stage"
ar 00C3-0D01
endpoke
