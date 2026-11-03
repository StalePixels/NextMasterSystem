; Land of Illusion: register 8 for every line, as the game's line interrupt
; handler ($0F0C) sets it. Called once a frame by the runtime (rast_frame in
; fw3.asm) with HL = table of 192 bytes to fill, IX = the runtime's copy of
; VDP registers 0-10, game RAM at $C000. Carry set on return: the table is valid.
;
; The frame code ($0EBF) picks the split from ($C1CF):
; 0: H = ($C018), register 10 = $9F; the event at line 159 sets H = 0 for the
;    status bar from line 160.
; 1: H = ($C1D1), register 10 = $5F; the event at line 95 sets H = 0 from
;    line 96.
; 2: H = 0, register 10 = $2F; events at lines 47, 95 and 143: the one at 95
;    sets H = ($C1D1) from line 96, the one at 143 sets H = 0 from line 144.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,($C1CF)
		or a
		jr z,.m0
		dec a
		jr z,.m1
		xor a			; mode 2: lines 0-95 H = 0
		ld b,96
		call .fill
		ld a,($C1D1)		; lines 96-143 H = ($C1D1)
		ld b,48
		call .fill
		xor a			; lines 144-191 H = 0
		ld b,48
		jr .last
.m1:		ld a,($C1D1)		; mode 1: lines 0-95 H = ($C1D1)
		ld b,96
		call .fill
		xor a			; lines 96-191 H = 0
		ld b,96
		jr .last
.m0:		ld a,($C018)		; mode 0: lines 0-159 H = ($C018)
		ld b,160
		call .fill
		xor a			; lines 160-191 H = 0
		ld b,32
.last:		call .fill
		scf
		ret
.fill:		ld (hl),a
		inc hl
		djnz .fill
		ret
