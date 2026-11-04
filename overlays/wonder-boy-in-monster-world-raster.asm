; Wonder Boy in Monster World: register 8 for every line, as the game's line
; interrupt handlers set it. Called once a frame by the runtime (rast_frame in
; fw3.asm) with HL = table of 192 bytes to fill, IX = the runtime's copy of
; VDP registers 0-10, game RAM at $C000. Carry set on return: the table is
; valid.
;
; The frame handler sets H for the top of the picture (register 8, 0 under
; the status bar), register 10 = N, and the line handler in $C012, which the
; interrupt entry $0038 jumps to through $026F for a line interrupt. The
; counter takes a new register 10 only when it reloads at an event, so event 0
; comes at line N and event 1 at line 2N + 1; the H an event writes applies
; from the line after it. The handlers:
; - $0274 (play; bank 25 $A841, $A7E0): H = ($C66C) from line N + 1, then
;   $0294, which writes nothing. The frame handler copies $C0A1 to $C66C.
; - $02D5 (the title, $01AE, N = 184): H = ($C0A1) from line N + 1.
; - $0298 ($A7E5, $A8A7, $A877; game states 6 and 7): H = ($C66C) from
;   line N + 1 and register 10 = $50; $02B2 at event 1 writes nothing, so
;   event 2 comes at line 2N + 82; $02BB there: H = ($C6E0) from the line
;   after. No recording ran this chain.
; Any other handler ($0294 alone), or line interrupts off: the table is not
; valid, and the game gets its line events.
		org $3C00
		bit 4,(ix+0)		; line interrupts off: no table
		jr z,.no
		ld a,(ix+10)
		cp 191			; no event in the picture
		jr nc,.no
		ld c,a			; C = N
		ld de,($C012)
		ld a,d
		cp $02
		jr nz,.no
		ld a,e
		cp $74
		jr z,.play
		cp $D5
		jr z,.title
		cp $98
		jr z,.three
.no:		or a
		ret
.title:		ld de,$C0A1
		jr .two
.play:		ld de,$C66C
.two:		ld a,(ix+8)		; lines 0 to N: the frame's H
		ld b,c
		inc b
		call .fill
		ld a,191		; lines N + 1 to 191
		sub c
		ld b,a
		ld a,(de)
		call .fill
		scf
		ret
.three:		ld a,c
		cp 55			; event 2 below the picture: as $0274
		jr nc,.play
		ld a,(ix+8)		; lines 0 to N
		ld b,c
		inc b
		call .fill
		ld a,c			; lines N + 1 to 2N + 82: N + 82 lines
		add a,82
		ld b,a
		ld a,($C66C)
		call .fill
		ld a,c			; lines 2N + 83 to 191: 109 - 2N lines
		add a,a
		ld b,a
		ld a,109
		sub b
		ld b,a
		ld a,($C6E0)
		call .fill
		scf
		ret
.fill:		ld (hl),a
		inc hl
		djnz .fill
		ret
