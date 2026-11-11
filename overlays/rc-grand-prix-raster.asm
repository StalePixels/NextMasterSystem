; R.C. Grand Prix: register 8 for every line of the title screen, whose credits
; line scrolls below a still picture. Called once a frame by the runtime with
; HL = table of 192 bytes to fill, IX = the runtime's copy of VDP registers
; 0-10, game RAM at $C000. Carry set on return: the table is valid.
;
; The title loop ($15AF) sets register 10 = $B7 ($158A) and, after each frame
; wait, register 8 = 0 ($15B3). The line handler $15DD (through the word at
; $C372) then sets register 8 = ($C380), so lines 0-183 have H = 0 and lines
; 184-191, the credits row, have H = ($C380). On other screens (register 10 is
; not $B7, or line interrupts are off) the routine returns carry clear.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,(ix+10)
		cp $B7
		jr z,.go
		or a
		ret
.go:		xor a
		ld b,184
.top:		ld (hl),a
		inc hl
		djnz .top
		ld a,($C380)
		ld b,8
.row:		ld (hl),a
		inc hl
		djnz .row
		scf
		ret
