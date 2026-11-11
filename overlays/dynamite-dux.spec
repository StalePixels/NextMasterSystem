# Dynamite Dux (Europe, Brazil) (En), CRC32 0E1CC1E0, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with reference I/O logs (600 s of
# random input, 120 s with no input).
#
# Decisions:
# - $0018-$0037 is free ($FF bytes), so $18 is the io vector.
# - Scan entries: $021D, $0226, $022E, $024C, $026C, $0552, $05A7, $0917 and $0937, the
#   VDP routines of bank 0 that no path or recording reaches. Each starts after a RET or a
#   JR and is a whole routine that sets the VDP address and writes or reads the data
#   port, so their I/O sites are patched.
# - The routine $1C9C picks a word from the table after its CALL by comparing A with a
#   list of limits at HL. At $468F the list ($46A4) has 8 limits and an $FF end, so the
#   table at $4692 has 9 words; the scanner reads 14, and the words past the ninth are
#   the limit bytes. The paths from them ($1606, $221E, $2E28, $3632, $11FF) give the
#   RST $38 rows, the JP $C0FF and the LD ($55FF),A in $221E-$228A; no I/O site comes
#   only from them.
# - The sound driver in bank 15 writes the FM unit ports $F0 and $F1 from its command
#   table ($935A); those sites are patched like the PSG ones.
# - The byte scan rows in banks 6, 9 and 11 are graphics and map data (verdict false).
# - The block loader $0530 (HL = VRAM address, DE = source, BC = count; an OUTI loop at
#   $053D) copies tiles from ROM while the game plays, and through the runtime's OUTI path
#   it took frames past 100%. Its first 5 bytes are a far call to ldblk in page 0, which
#   writes the block with jt_vwrite, then RET.
name Dynamite Dux
cart 0E1CC1E0
hz 50		; No-Intro regions Europe, Brazil
vector 18 io
asm 00001 2   ; IM 1 -> IM 2
    im 2
endasm
site 000AC   ; OUT (C),L
site 000AE   ; OUT (C),H
site 000B3   ; OUT (C),L
site 000B5   ; OUT (C),H
site 000EA   ; IN A,($BF)
site 0011D   ; IN A,($DD)
site 001AC   ; OUT ($DE),A
site 001AE   ; IN A,($DC)
site 001B9   ; IN A,($DD)
site 00212   ; OUT ($BF),A
site 00219   ; OUT ($BF),A
site 0021E   ; OUT ($BF),A
site 00223   ; OUT ($BF),A
site 0022B   ; IN A,($BE)
site 00235   ; OUT ($BE),A
site 0023A   ; OUT ($BE),A
site 0023E   ; OUT ($BE),A
site 00242   ; OUT ($BE),A
site 00251   ; IN A,($BE)
site 00263   ; OUT ($BE),A
site 00276   ; OUT ($BE),A
site 00288   ; OUT ($BF),A
site 0028C   ; OUT ($BF),A
site 0029F   ; OUT ($BF),A
site 002A3   ; OUT ($BF),A
site 002B0   ; OUT ($BF),A
site 002B4   ; OUT ($BF),A
site 002C1   ; OUT ($BF),A
site 002C5   ; OUT ($BF),A
site 002E8   ; OUT ($BF),A
site 002ED   ; OUT ($BF),A
site 00339   ; OUT ($BF),A
site 0033D   ; OUT ($BF),A
site 00342   ; OUT ($BE),A
site 003D1   ; OTIR
site 003D4   ; OUTI
site 003D6   ; OUTI
site 003D8   ; OUTI
site 003DA   ; OUTI
site 003DC   ; OUTI
site 003DE   ; OUTI
site 003E0   ; OUTI
site 003E2   ; OUTI
site 003E4   ; OUTI
site 003E6   ; OUTI
site 003E8   ; OUTI
site 003EA   ; OUTI
site 003EC   ; OUTI
site 003EE   ; OUTI
site 003F0   ; OUTI
site 003F2   ; OUTI
site 003F4   ; OUTI
site 003F6   ; OUTI
site 003F8   ; OUTI
site 003FA   ; OUTI
site 003FC   ; OUTI
site 003FE   ; OUTI
site 00400   ; OUTI
site 00402   ; OUTI
site 00404   ; OUTI
site 00406   ; OUTI
site 00408   ; OUTI
site 0040A   ; OUTI
site 0040C   ; OUTI
site 0040E   ; OUTI
site 00410   ; OUTI
site 00412   ; OUTI
site 00414   ; OUTI
site 00416   ; OUTI
site 00418   ; OUTI
site 0041A   ; OUTI
site 0041C   ; OUTI
site 0041E   ; OUTI
site 00420   ; OUTI
site 00422   ; OUTI
site 00424   ; OUTI
site 00426   ; OUTI
site 00428   ; OUTI
site 0042A   ; OUTI
site 0042C   ; OUTI
site 0042E   ; OUTI
site 00430   ; OUTI
site 00432   ; OUTI
site 00434   ; OUTI
site 00436   ; OUTI
site 00438   ; OUTI
site 0043A   ; OUTI
site 0043C   ; OUTI
site 0043E   ; OUTI
site 00440   ; OUTI
site 00442   ; OUTI
site 00444   ; OUTI
site 00446   ; OUTI
site 00448   ; OUTI
site 0044A   ; OUTI
site 0044C   ; OUTI
site 0044E   ; OUTI
site 00450   ; OUTI
site 00452   ; OUTI
site 00454   ; OUTI
site 00456   ; OUTI
site 00458   ; OUTI
site 0045A   ; OUTI
site 0045C   ; OUTI
site 0045E   ; OUTI
site 00460   ; OUTI
site 00462   ; OUTI
site 00464   ; OUTI
site 00466   ; OUTI
site 00468   ; OUTI
site 0046A   ; OUTI
site 0046C   ; OUTI
site 0046E   ; OUTI
site 00470   ; OUTI
site 00472   ; OUTI
site 00474   ; OUTI
site 00476   ; OUTI
site 00478   ; OUTI
site 0047A   ; OUTI
site 0047C   ; OUTI
site 0047E   ; OUTI
site 00480   ; OUTI
site 00482   ; OUTI
site 00484   ; OUTI
site 00486   ; OUTI
site 00488   ; OUTI
site 0048A   ; OUTI
site 0048C   ; OUTI
site 0048E   ; OUTI
site 00490   ; OUTI
site 00492   ; OUTI
site 00494   ; OUTI
site 00496   ; OUTI
site 00498   ; OUTI
site 0049A   ; OUTI
site 0049C   ; OUTI
site 0049E   ; OUTI
site 004A0   ; OUTI
site 004A2   ; OUTI
site 004A4   ; OUTI
site 004A6   ; OUTI
site 004A8   ; OUTI
site 004AA   ; OUTI
site 004AC   ; OUTI
site 004AE   ; OUTI
site 004B0   ; OUTI
site 004B2   ; OUTI
site 004B4   ; OUTI
site 004B6   ; OUTI
site 004B8   ; OUTI
site 004BA   ; OUTI
site 004BC   ; OUTI
site 004BE   ; OUTI
site 004C0   ; OUTI
site 004C2   ; OUTI
site 004C4   ; OUTI
site 004C6   ; OUTI
site 004C8   ; OUTI
site 004CA   ; OUTI
site 004CC   ; OUTI
site 004CE   ; OUTI
site 004D0   ; OUTI
site 004D2   ; OUTI
site 004D8   ; OUT ($BF),A
site 004DF   ; OUT ($BF),A
site 004E2   ; OUT ($BE),A
site 0054F   ; OUT ($BE),A
site 00559   ; OUT ($BE),A
site 0055F   ; OUT ($BE),A
site 0057B   ; OUT ($BE),A
site 00580   ; OUT ($BE),A
site 0058B   ; OUT ($3F),A
site 0058D   ; IN A,($DD)
site 00597   ; OUT ($3F),A
site 00599   ; IN A,($DD)
site 005A2   ; OUT ($3F),A
site 005BD   ; OUT ($BF),A
site 005C4   ; OUT ($BF),A
site 005E1   ; OUT ($BE),A
site 005EC   ; OUT ($BE),A
site 005F7   ; OUT ($BE),A
site 00602   ; OUT ($BE),A
site 008FF   ; OUT ($BF),A
site 00906   ; OUT ($BF),A
site 0091F   ; OUT ($BF),A
site 00926   ; OUT ($BF),A
site 00945   ; OUT ($BF),A
site 0094C   ; OUT ($BF),A
site 00992   ; OUT ($BE),A
site 0099D   ; OUT ($BE),A
site 009A8   ; OUT ($BE),A
site 009B2   ; OUT ($BE),A
site 027B9   ; OUT ($BF),A
site 027BD   ; OUT ($BF),A
site 027C2   ; OUT ($BF),A
site 027C6   ; OUT ($BF),A
site 3CE8C   ; OUT ($F0),A
site 3CE95   ; OUT ($F1),A
site 3CEAD   ; OUT ($7F),A
site 3CEBD   ; OUT (C),D
site 3CEC3   ; OUT ($F1),A
site 3CEF6   ; OTIR
site 3CF04   ; OTIR
site 3CF0E   ; OUT ($F0),A
site 3CF14   ; OUT ($F1),A
site 3CF20   ; OUTI
site 3CF26   ; OUTI
site 3CFF7   ; OUT ($7F),A
site 3CFFB   ; OUT ($7F),A
site 3D023   ; OUT ($7F),A
site 3D027   ; OUT ($7F),A
site 3D02B   ; OUT ($7F),A
site 3D02F   ; OUT ($7F),A
site 3D032   ; OUT ($7F),A
site 3D098   ; OUT ($F0),A
site 3D09F   ; OUT ($F1),A
site 3D0A7   ; OUT ($F0),A
site 3D0AD   ; OUT ($F1),A
site 3D1A0   ; OUT ($F0),A
site 3D1AA   ; OUT (C),L
site 3D1B3   ; OUT ($F0),A
site 3D1CE   ; OUT (C),H
site 3D1D6   ; OUT ($F0),A
site 3D1E4   ; OUT ($F1),A
site 3D1F0   ; OUT ($F0),A
site 3D1F9   ; OUT ($F1),A
site 3D398   ; OUT ($F0),A
site 3D3A1   ; OUT (C),A
site 3D3A6   ; OUT ($F0),A
site 3D3AC   ; OUTI
site 3D3FF   ; OUT ($7F),A
site 3D471   ; OUT ($7F),A
site 3D498   ; OUT ($7F),A
site 3D49D   ; OUT ($7F),A
site 3D4C9   ; OUT ($F0),A
site 3D4D7   ; OUT ($F1),A
site 3D56B   ; OUTI
site 3D56D   ; OUTI
site 3D56F   ; OUTI
site 3D571   ; OUTI
site 3D573   ; OUTI
site 3D575   ; OUTI
site 3D577   ; OUTI
site 3D579   ; OUTI
site 3D57B   ; OUTI
site 3D57D   ; OUTI
site 3D57F   ; OUTI
site 3D589   ; OUT (C),D
site 3D58F   ; OUT ($F1),A
site 3D5CE   ; OUT ($7F),A
site 3D624   ; OUT ($7F),A
site 3D663   ; OUT ($7F),A
site 3D6B6   ; OUT ($7F),A
site 3D6D6   ; OUT ($7F),A
site 3D722   ; OUT ($7F),A
site 3D72C   ; OUT ($7F),A
site 3D774   ; OUT ($7F),A
mapldk 00069   # LD HL,$FFFC; LD (HL),$80
maphl 0006F   # LD (HL),$00, HL = $FFFD
maphl 00072   # LD (HL),$01, HL = $FFFE
mapst 008A4   ; LD ($FFFF),A
mapst 01F82   ; LD ($FFFF),A
asm 00530 5          ; CALL $0210 : EX DE,HL : LD A,B -> far call to ldblk, RET
    rst $18
    db far_io, pg_ldblk, ent_ldblk
    ret
endasm
page 0 ldblk
; ldblk: HL = the VRAM address, DE = the source, BC = the count (1 to 65535). Writes the
; block to VRAM as $0530-$0547 do, and returns as they do: HL = the source after the block,
; DE = the VRAM address, B = 0, C = $BE, A = 0, IX and IY kept, interrupts as at the call.
; A count of 0 writes nothing (the game's loop would write 64K). Runs with interrupts off on
; a stack of its own; uses jt_vwrite.
ldblk:  ld (.sp),sp
        ld sp,stk
        ld a,i                  ; P/V = the interrupt state at the call
        di
        push af
        push ix
        push iy
        ld (.vram),hl
        ex de,hl                ; HL = the source, DE = the VRAM address
        push hl
        add hl,bc
        ld (.end),hl            ; the source after the block
        pop hl
        ld a,b
        or a
        jr z,.part
        push bc
        push hl
        push de
        ld c,b                  ; B runs of 256 bytes
        ld b,0
        ld ix,256
        ld iy,256
        xor a                   ; the source as the game sees it
        call jt_vwrite
        pop de
        pop hl
        pop bc
        ld a,h                  ; source and VRAM address B * 256 on
        add a,b
        ld h,a
        ld a,d
        add a,b
        ld d,a
.part:  ld a,c
        or a
        jr z,.done
        ld b,c                  ; one run of the bytes left
        ld c,1
        ld ix,256
        ld iy,256
        xor a
        call jt_vwrite
.done:  ld hl,(.end)
        ld de,(.vram)
        ld bc,$00BE
        pop iy
        pop ix
        pop af
        ld sp,(.sp)
        ld a,0
        jp po,.ret
        ei
.ret:   ret
.sp:    dw 0
.vram:  dw 0
.end:   dw 0
        ds 32
stk:
endpage

# Dynamite Dux (Europe, Brazil).cht, "Infinite Lives": the byte at cart offset $187D is
# DEC (HL) on the life counter at RAM $C04B; the code turns it into OR (HL), so a death
# no longer lowers the count and the game starts with 4 in the counter
poke "Infinite lives"
gg B68-7DE-3BE
endpoke

# Dynamite Dux (Europe, Brazil).cht, "Infinite Health": RAM $C227 is the energy bar, $FF is full
poke "Infinite health"
ar 00C2-27FF
endpoke

# Dynamite Dux (Europe, Brazil).cht, "Disable Health Loss from taking too much Time": RAM $C099
# is the counter of the slow energy drain, held at 0
poke "No time drain"
ar 00C0-9900
endpoke
