; Pit-Fighter: register 8 for every line in a fight. Called once a frame by the runtime
; (rast_frame in fw3.asm) with HL = table of 192 bytes to fill, IX = the runtime's copy of
; VDP registers 0-10, game RAM at $C000. Carry set on return: the table is valid.
;
; In a fight ($C354 not 0, line interrupts on in register 0) the game's line interrupt at
; line 31 writes register 8 from $C34E for the play area, below the status bar; the frame
; handler writes 0 for the top. With this table the game gets no line interrupts, and the
; spec runs the line 31 code at the end of the frame handler; it keeps $C34E as it was
; before that code in $C5BE, the value the line 31 write would give the next picture.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,($C354)		; no split outside a fight
		or a
		ret z
		ld a,(ix+8)		; lines 0-31: the frame handler's H
		ld b,32
.top:		ld (hl),a
		inc hl
		djnz .top
		ld a,($C5BE)		; lines 32-191: the play area's H
		ld b,160
.play:		ld (hl),a
		inc hl
		djnz .play
		scf
		ret
