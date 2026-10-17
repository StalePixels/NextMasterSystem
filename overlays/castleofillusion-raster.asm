; Castle of Illusion: register 8 for every line, as the game's line interrupt
; handler ($06FE) sets it. Called once a frame by the runtime (rast_frame in
; fw3.asm) with HL = table of 192 bytes to fill, IX = the runtime's copy of
; VDP registers 0-10, game RAM at $C000. Carry set on return: the table is valid.
;
; Mode ($C060) 9, the castle scenes of the intro: the frame code ($0657) sets
; H = ($DC01) and register 10 = 7, so an event comes every 8 lines (lines 7,
; 15, 23 ...). At event n the handler sets H = ($DC01 + 2n), which applies from
; line 8n.
; Any other mode: the frame code ($06A3) sets H = ($C018) and register 10 =
; $9F; the event at line 159 sets H = 0 for the status bar from line 160.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,($C060)
		cp 9
		jr z,.bands
		ld a,($C018)		; lines 0-159: H = ($C018)
		ld b,160
.top:		ld (hl),a
		inc hl
		djnz .top
		xor a			; lines 160-191: H = 0
		ld b,32
.bar:		ld (hl),a
		inc hl
		djnz .bar
		scf
		ret
.bands:		ld de,$DC01		; 24 bands of 8 lines: H = ($DC01 + 2n)
		ld c,24
.band:		ld a,(de)
		inc de
		inc de
		ld b,8
.line:		ld (hl),a
		inc hl
		djnz .line
		dec c
		jr nz,.band
		scf
		ret
