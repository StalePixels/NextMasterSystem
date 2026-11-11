# Scramble Spirits (Europe, Brazil) (En), CRC32 9A8B28EC, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from the sitescan output, with the scan entries below, then
# decided by hand.
#
# Decisions:
# - Scan entries 5:AA40, 5:AA21, 5:9A9F, 5:BB9C and 5:B600: the calls and jumps into slot 2
#   at $5C20-$726C (bank 1) run with bank 5 paged: each routine pages it with LD A,$05;
#   CALL $01A3 first, or runs from an object handler that bank 5 code calls. They add no
#   I/O sites and no mapper stores.
# - The I/O sites at $04D5 (routine $04D0) and $04E5 (routine $04E2) are in two VDP data
#   write loops that nothing in the cart names. They are patched all the same.
# - The two JP (HL) at $4283 and $467B index the words at $4778 and $45DC with an object
#   type; those bytes are code and tables of other kinds, not jump tables, and neither jump
#   ran in a 5-minute reference run. They are left as they are.
# - The other byte patterns that no path reached are tile graphics and tables (verdict false).
# - The interrupt handler at $01AA pages banks 2, 3, 4, 7, 8, 10, 13, 14 and 15 into slot 2
#   to copy tiles; the bank comes back from $C0FF at $0208.
# - $0184 copies BC bytes from HL to VRAM at DE, one OUT a byte. Its one caller is the
#   interrupt handler's tile upload ($040D, from the slots at $C200-$C340), in play and at the
#   screen loads; through the traps one call took up to 4.6 Next frames. Page 0 entry copy
#   does it with jt_vwrite, in runs of 256 bytes. The site at $0188 has no line: the patch at
#   $0184 replaces the whole routine.
name Scramble Spirits
cart 9A8B28EC
hz 50		; No-Intro regions Europe, Brazil
# No free RST vector: the JP at $0000 becomes the vector, the game starts at its target.
vector 00 io
start 0069
asm 0006A 2   ; IM 1 -> IM 2
    im 2
endasm
asm 02298 2   ; IM 1 -> IM 2
    im 2
endasm
asm 00184 5          ; CALL $0167 : the loop to RET at $0190: BC bytes from HL to VRAM at DE
    rst $00
    db far_io, pg_copy, ent_copy
    ret
endasm
page 0 copy
; copy: $0184-$0190. Sets the VRAM address from DE, as CALL $0167 does, and writes BC bytes
; (BC = 0: none) from HL, as the game sees them, with jt_vwrite. It runs on a stack in this
; page and returns what the game's loop leaves: HL + BC, BC = 0, A = 0, Z set, carry clear,
; DE kept. jt_vwrite runs with interrupts off and keeps the interrupt state.
PSTACK  equ $3FF0
copy:   ld (sv_sp),sp
        ld sp,PSTACK
        push ix
        push iy
        ld (hl0),hl
        ld (de0),de
        ld (cnt),bc
        ld a,b
        or a
        jr z,.low
        ld c,b                  ; B runs of 256 bytes
        ld b,0
        ld ix,256
        ld iy,256
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,h
        add a,c
        ld h,a
        ld a,d
        add a,c
        ld d,a                  ; bits 14 and 15 are ignored, so the address wraps at $4000
.low:   ld a,(cnt)
        or a
        jr z,.done
        ld b,a
        ld c,1
        ld ix,0
        ld iy,0
        xor a
        call jt_vwrite
.done:  pop iy
        pop ix
        ld sp,(sv_sp)
        ld hl,(hl0)
        ld de,(cnt)
        add hl,de
        ld de,(de0)
        ld bc,0
        xor a
        ret
hl0:    dw 0
cnt:    dw 0
de0:    dw 0
sv_sp:  dw 0
endpage
site 0009B   ; OUT ($BE),A
site 000A1   ; OUT ($BE),A
site 0014E   ; OTIR
site 00168   ; OUT ($BF),A
site 0016B   ; OUT ($BF),A
site 0016F   ; OUT ($BF),A
site 00172   ; OUT ($BF),A
site 0017B   ; OUT ($BE),A
site 0019B   ; OUT ($BE),A
site 001F4   ; IN A,($BF)
site 001F6   ; IN A,($DD)
site 00250   ; OUT ($3E),A
site 00258   ; OUT ($F2),A
site 0025B   ; IN A,($F2)
site 0026D   ; OUT ($F2),A
site 00275   ; OUT ($3E),A
site 002EA   ; OUT ($BE),A
site 002FD   ; OUT ($BE),A
site 00301   ; OUT ($BE),A
site 003BA   ; OUT ($BE),A
site 003BF   ; OUT ($BE),A
site 004AF   ; OUT ($DE),A
site 004B1   ; IN A,($DC)
site 004C4   ; IN A,($DD)
site 004D5   ; OUT ($BE),A
site 004DC   ; OUT ($BE),A
site 004E5   ; OUT ($BE),A
site 0C128   ; OUT ($F0),A
site 0C131   ; OUT ($F1),A
site 0C178   ; OUT ($7F),A
site 0C188   ; OUT (C),D
site 0C18E   ; OUT ($F1),A
site 0C1A3   ; OUT ($F0),A
site 0C1B1   ; OUT ($F1),A
site 0C1DB   ; OTIR
site 0C1F9   ; OTIR
site 0C20B   ; OUT ($F0),A
site 0C219   ; OUT ($F1),A
site 0C21E   ; OUT ($F0),A
site 0C22C   ; OUT ($F1),A
site 0C22F   ; OUT ($F0),A
site 0C235   ; OUT ($F1),A
site 0C241   ; OUTI
site 0C247   ; OUTI
site 0C29F   ; OUT ($7F),A
site 0C2A3   ; OUT ($7F),A
site 0C338   ; OUT ($7F),A
site 0C33C   ; OUT ($7F),A
site 0C35F   ; OUT ($7F),A
site 0C363   ; OUT ($7F),A
site 0C36C   ; OUT ($7F),A
site 0C370   ; OUT ($7F),A
site 0C373   ; OUT ($7F),A
site 0C3D9   ; OUT ($F0),A
site 0C3E0   ; OUT ($F1),A
site 0C3E8   ; OUT ($F0),A
site 0C3EE   ; OUT ($F1),A
site 0C4E3   ; OUT ($F0),A
site 0C4ED   ; OUT (C),L
site 0C4F6   ; OUT ($F0),A
site 0C511   ; OUT (C),H
site 0C519   ; OUT ($F0),A
site 0C527   ; OUT ($F1),A
site 0C533   ; OUT ($F0),A
site 0C53C   ; OUT ($F1),A
site 0C703   ; OUT ($F0),A
site 0C70C   ; OUT (C),A
site 0C711   ; OUT ($F0),A
site 0C717   ; OUTI
site 0C7A0   ; OUT ($7F),A
site 0C874   ; OUT ($7F),A
site 0C89B   ; OUT ($7F),A
site 0C8A0   ; OUT ($7F),A
site 0C8CC   ; OUT ($F0),A
site 0C8DA   ; OUT ($F1),A
site 0C8E8   ; OUT ($F0),A
site 0C8FC   ; OUT ($F0),A
site 0C990   ; OUTI
site 0C992   ; OUTI
site 0C994   ; OUTI
site 0C996   ; OUTI
site 0C998   ; OUTI
site 0C99A   ; OUTI
site 0C99C   ; OUTI
site 0C99E   ; OUTI
site 0C9A0   ; OUTI
site 0C9A2   ; OUTI
site 0C9A4   ; OUTI
site 0C9AE   ; OUT (C),D
site 0C9B4   ; OUT ($F1),A
site 0C9F3   ; OUT ($7F),A
site 0CA49   ; OUT ($7F),A
site 0CA88   ; OUT ($7F),A
site 0CAEA   ; OUT ($7F),A
site 0CB0A   ; OUT ($7F),A
site 0CB56   ; OUT ($7F),A
site 0CB60   ; OUT ($7F),A
site 0CBA8   ; OUT ($7F),A
site 123E3   ; OUT ($DE),A
site 123E5   ; IN A,($DC)
site 123F8   ; IN A,($DD)
site 137C7   ; OUT ($3F),A
site 137C9   ; IN A,($DD)
site 137D3   ; OUT ($3F),A
site 137D5   ; IN A,($DD)
site 137DE   ; OUT ($3F),A
mapst 0007E   ; LD ($FFFF),A
mapst 001A6   ; LD ($FFFF),A
mapst 001E0   ; LD ($FFFF),A
mapst 00208   ; LD ($FFFF),A
mapst 00336   ; LD ($FFFF),A
mapst 00416   ; LD ($FFFF),A
mapst 0043E   ; LD ($FFFF),A

# Scramble Spirits (Europe, Brazil).cht, "Infinite Lives P1": RAM $C1CA is the life counter of
# player 1, held at 9; the game starts with 5 and a life is lost at each death
poke "Infinite lives"
ar 00C1-CA09
endpoke

# Scramble Spirits (Europe, Brazil).cht, "Invulnerability": RAM $C237 is the player's hit
# timer, held at $73; enemy fire and collisions no longer take a life
poke "Invincibility"
ar 00C2-3773
endpoke
