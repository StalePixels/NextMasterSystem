; Bonanza Bros.: register 8 for every line, as the game sets it. Called once a frame by the
; runtime (rast_frame in fw3.asm) with HL = table of 192 bytes to fill, IX = the runtime's
; copy of VDP registers 0-10, game RAM at $C000. Carry set on return: the table is valid.
;
; The frame interrupt sets H = 0 ($0960 and $0995, LD HL,$8800 : RST $18) and copies the
; game's scroll ($CA00) to $CA0D ($095A, $098F). The line interrupt handler ($0C9C) sets
; H = -($CA0D) at each event; register 10 is 30, so the first event, at line 30, starts the
; play area's scroll below the HUD, and the later ones write the same value. An event at
; line L sets H from line L+1.
;
; The runtime calls this before the frame interrupt has copied $CA00 to $CA0D for the next
; picture, so the routine reads $CA00.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,(ix+10)
		cp 191
		ret nc			; no event in the picture: no table
		inc a
		ld b,a			; lines 0 to register 10: H = 0
		xor a
.top:		ld (hl),a
		inc hl
		djnz .top
		ld a,(ix+10)
		sub 191
		neg
		ld b,a			; lines register 10 + 1 to 191
		ld a,($CA00)
		neg
.play:		ld (hl),a
		inc hl
		djnz .play
		scf
		ret
