; Fantastic Dizzy: register 8 for every line of the wavy logo before the
; language choice, which the game sets by polling the V counter. Called once a
; frame by the runtime (rast_frame in fw3.asm) with HL = table of 192 bytes to
; fill, IX = the runtime's copy of VDP registers 0-10, game RAM at $C000.
; Carry set on return: the table is valid.
;
; The code cave at $AA8E replaces the game's polling loop. Once a frame while
; the logo runs, it writes the runtime's frame handler count (isr_n) into a
; stamp byte at $DF00, in RAM the game does not use. Line L of 0-46 gets
; H = ($C12E + ((($D0CE) + L) AND $3F)), the lines below get 0.
; A stamp more than 2 frames old means the logo has ended; it is then kept
; stale (isr_n + $80), so it never comes back into the window when isr_n
; wraps.
;
; The title, in 224-line mode, sets H for three bands: 0 from line 0, ($C127)
; from line 155 and ($C128) from line 182. Its code cave at $ADA7 stamps
; $DF03 once a frame; while that stamp is fresh and the VDP is in 224-line
; mode, the table is the rastseg list of the three segments (line, H), ended
; by line 255.
;
; Play, in 224-line mode, splits the status bar from the play area at the
; sprite collision line. pal8p (page 0), at the split, stamps $DF06 and keeps
; the status bar's H in $DF07; while that stamp is fresh and the VDP is in
; 224-line mode, the table is the status bar's H from line 0 and the play
; area's, ($D795), from line 33, where the Master System takes the split's
; register 8 write.
ISR_N		equ $E071		; isr_n in the runtime's fixed state
		org $3C00
		ld a,(ISR_N)
		ld c,a
		ld de,$DF00
		call age
		jr c,wave
		ld de,$DF03
		call age
		jr c,title
		ld de,$DF06
		call age
		ret nc			; carry clear: no table
		call m224
		jr z,none
		ld (hl),0		; play: the status bar's H from line 0
		inc hl
		ld a,($DF07)
		ld (hl),a
		inc hl
		ld (hl),33		; the play area's from line 33
		inc hl
		ld a,($D795)
		ld (hl),a
		inc hl
		ld (hl),255
		scf
		ret
title:		call m224
		jr z,none
		ld (hl),0		; lines 0-154: H = 0
		inc hl
		ld (hl),0
		inc hl
		ld (hl),155
		inc hl
		ld a,($C127)
		ld (hl),a
		inc hl
		ld (hl),182
		inc hl
		ld a,($C128)
		ld (hl),a
		inc hl
		ld (hl),255
		scf
		ret
none:		or a
		ret
; NZ in 224-line mode: register 0 bit 1 and register 1 bit 4
m224:		bit 1,(ix+0)
		ret z
		bit 4,(ix+1)
		ret
; carry set when the stamp at DE is 0-2 frames older than C (isr_n)
age:		ld a,(de)
		ld b,a
		ld a,c
		sub b
		cp 3
		ret c
		ld a,c
		add a,$80
		ld (de),a
		or a
		ret
wave:		ld a,($D0CE)
		ld c,a
		ld b,47
.w:		ld a,c
		and $3F
		add a,$2E
		ld e,a
		ld d,$C1
		ld a,(de)
		ld (hl),a
		inc hl
		inc c
		djnz .w
		xor a
		ld b,192-47
.z:		ld (hl),a
		inc hl
		djnz .z
		scf
		ret
