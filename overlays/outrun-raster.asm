; OutRun: register 8 for every line, as the game's line interrupt handler
; (copied from ROM $07F0 to $DE80 at start) sets it. Called once a frame by
; the framework (src/fw2.asm, rast_frame) with HL = table of 192 bytes to
; fill, IX = framework copy of VDP registers 0-10, game RAM at $C000.
; Carry set on return: the table is valid.
;
; In the blank the frame code writes register 10 = ($C191) and register 8 =
; ($C1B3); at the top of the picture it writes register 10 = 0. So the first
; event is at line ($C191), then one on every line to 192. The handler: V =
; V counter, H = (($DE88) * 256 + (2 * V & $FF)), where $DE88 picks the
; buffer page. The frame code's values are taken from RAM, not from the
; registers, because on the Next it may not have run yet this frame.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,($C1B3)
		ld c,a			; H down to the first event
		ld a,($C191)
		ld e,a			; first event line
		ld a,($DE88)
		ld d,a			; table page
		ld b,0			; line
.l:		ld (hl),c
		inc hl
		ld a,b
		cp e
		jr c,.n			; before the first event
		push hl			; event at line B: H = (D * 256 + 2B)
		ld h,d
		ld a,b
		add a,a
		ld l,a
		ld c,(hl)
		pop hl
.n:		inc b
		ld a,b
		cp 192
		jr nz,.l
		scf
		ret
