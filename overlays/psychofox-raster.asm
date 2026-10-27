; Psycho Fox: register 8 for every line in frames of the wave effect (bank 11
; $8000). Called once a frame by the runtime (rast_frame in fw3.asm) with HL =
; table of 192 bytes to fill, IX = the runtime's copy of VDP registers 0-10,
; game RAM at $C000. Carry set on return: the table is valid.
;
; The game's wave: $8000 writes H = -($C022) (the call to $7EB4), rotates the
; 32-byte table at $C180 by one, turns line interrupts on with register 10 =
; 1 and waits in a HALT loop for 96 of them, one every 2 lines (line 1, 3 ...
; 191). After interrupt k (1 to 96) it writes H = -($C022 + ($C180 + (k - 1)
; mod 32)), which applies from line 2k + WAVE_D. The page entry `wave` in
; psychofox.spec takes the place of that loop and stamps $DFF8 with isr_n;
; the table is valid only in the frame whose frame handler entry has that
; stamp, so it follows the wave's frames exactly.
WAVE_D	equ 0
		org $3C00
		ld a,($DFF8)
		ld b,a
		ld a,($E071)		; isr_n
		cp b
		jr z,.go
		or a
		ret
.go:		ld a,($C022)
		ld c,a
		neg
		ld b,2+WAVE_D		; lines 0 to 1 + WAVE_D: H = -($C022)
.top:		ld (hl),a
		inc hl
		djnz .top
		ld de,$C180
		ld b,96-1-(WAVE_D)	; the pairs of lines after interrupts 1 to 95
.pair:		ld a,(de)
		add a,c
		neg
		ld (hl),a
		inc hl
		ld (hl),a
		inc hl
		inc e			; $C180-$C19F wraps within its 32 bytes
		ld a,e
		and $9F
		ld e,a
		djnz .pair
		IF WAVE_D = 0
		ELSE
		ld a,(de)		; line 191 after interrupt 95: the write of 96 applies
		add a,c			; after the picture
		neg
		ld (hl),a
		ENDIF
		scf
		ret
