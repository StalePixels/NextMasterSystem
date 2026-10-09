; Hang On: register 8 for every line, as the game's line interrupt handler
; (copied from ROM $03B3 to $C4D0 at start) sets it. Called once a frame by
; the framework (src/fw2.asm, rast_frame) with HL = table of 192 bytes to
; fill, IX = framework copy of VDP registers 0-10, game RAM at $C000.
; Carry set on return: the table is valid.
;
; The handler: V = V counter; V < $5F: H = -($C051) and register 10 = 0;
; else H = ($C500 + V). The frame code leaves register 10 = $2F, so the
; first event is at line 47, the next 48 lines later (95, the register 10
; write takes effect at that reload), then every line. Lines up to the
; first event keep register 8 as the frame code set it.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld c,(ix+8)		; H until the first event
		ld a,(ix+10)
		ld e,a			; E = next event line
		ld d,a			; D = register 10, reloaded at the next event
		ld b,0			; line
.l:		ld (hl),c
		inc hl
		ld a,b
		cp e
		jr nz,.n
		cp $5F
		jr c,.top
		push hl			; H = ($C500 + V)
		ld h,$C5
		ld l,b
		ld c,(hl)
		pop hl
		jr .nx
.top:		ld a,($C051)		; H = -($C051), register 10 = 0
		neg
		ld c,a
		ld a,e
		add a,d
		inc a
		ld e,a
		ld d,0
		jr .n
.nx:		ld a,e			; next event: this line + register 10 + 1
		add a,d
		inc a
		ld e,a
.n:		inc b
		ld a,b
		cp 192
		jr nz,.l
		scf
		ret
