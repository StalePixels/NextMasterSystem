; Battle Out Run: register 8 for every line, as the game's line interrupt
; handler ($02A8, with the per-line part copied from ROM $02E3 to $D200 at
; start) sets it. Called once a frame by the runtime with HL = table of 192
; bytes to fill, IX = the runtime's copy of VDP registers 0-10, game RAM at
; $C000. Carry set on return: the table is valid.
;
; The frame handler ($021B) writes register 10 = $2F (or $FF on screens with
; no road), register 8 = -($D281), and sets the line count ($C15C) to $FD.
; The line events then come at line 47 (register 10 = $1F, no scroll write),
; line 95 (register 8 = -($C171), register 10 = 0) and every line from 127:
; at line 127 + K, register 8 = ($D002 + 2K). Each write shows from the line
; after its event. The values are taken from RAM, not from the registers,
; because on the Next the handler may not have run yet this frame.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,(ix+10)
		inc a			; register 10 = $FF: no line events
		ret z
		ld a,($D281)		; lines 0-95: the frame handler's H
		neg
		ld b,96
.top:		ld (hl),a
		inc hl
		djnz .top
		ld a,($C171)		; lines 96-127: the band below the horizon
		neg
		ld b,32
.mid:		ld (hl),a
		inc hl
		djnz .mid
		ld de,$D002		; lines 128-191: the road, one table word a line
		ld b,64
.road:		ld a,(de)
		ld (hl),a
		inc hl
		inc de
		inc de
		djnz .road
		scf
		ret
