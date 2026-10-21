; Super Monaco GP: register 8 for every line, as the game's line interrupt
; handler ($0038 with the status bit 7 clear) sets it. Called once a frame by
; the runtime (rast_frame in fw3.asm) with HL = table of 192 bytes to fill,
; IX = the runtime's copy of VDP registers 0-10, game RAM at $C000. Carry set
; on return: the table is valid.
;
; The frame handler ($02E8) sets register 10 = ($C091), H = ($C030) and the
; event counter $C039 = ($C092). Each line event adds 1 to $C039 and then,
; by the new count K:
;   K = 0          nothing
;   K = 1          H = -($C351), register 10 = 0
;   K = 2-$2F      H = ($D000 + K), through the RAM code at $D500, which
;                  writes K into the low byte of its own load address
;   K = $30        register 10 = $18, H = ($D030)
;   K = $31        H = -($C3D1), register 10 = 0
;   K = $32-$5F    H = ($D200 + K), through the RAM code at $D580
;   K = $60        register 10 = $FF
;   K > $60        H = ($C094), register 10 = $FF
; The race sets register 10 = $17 and K = $FF: the two roads of the split
; screen, each about 46 lines with a new H on every line.
;
; Only a frame with every-line events (K = 1 or $31, register 10 = 0) gets a
; table. Any other frame returns carry clear and the game takes its line
; interrupts, at most one or two a frame: the start and title screens scroll
; vertically, with the event at line 180 setting H = ($C094), and the table's
; copper list has no V scroll wrap line, so their lines past the wrap would
; show tilemap rows the game never wrote.
;
; Line counter model, as on the SMS: the first event is at line R10 (register
; 10 at the frame); at an event at line L the counter reloads with register 10
; as it is then, so the next event is at L + that value + 1; a register 10
; write in the handler takes effect at the reload after that. An H set at the
; event of line L applies from line L + 1.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		xor a
		ld (.m+1),a		; no every-line event yet
		ld a,($C039)
		ld (.k+1),a		; event counter, as the frame handler left it
		ld c,(ix+8)		; H until the first event
		ld d,(ix+10)		; D = register 10, used at the next reload
		ld e,d			; E = next event line
		ld b,0			; line
.l:		ld (hl),c
		inc hl
		ld a,b
		cp e
		jr nz,.n
		add a,d			; next event: this line + register 10 + 1
		jr c,.never
		inc a
		jr nz,.ev
.never:		ld a,$FF		; past the picture
.ev:		ld e,a
.k:		ld a,0			; K + 1, the handler's count
		inc a
		ld (.k+1),a
		call .hand
.n:		inc b
		ld a,b
		cp 192
		jr nz,.l
.m:		ld a,0			; 1: an every-line event came
		or a
		ret z			; carry clear: no table
		scf
		ret

; A = K. Sets C = H and D = register 10 as the handler does.
.hand:		or a
		ret z
		cp 1
		jr z,.k1
		cp $30
		jr c,.ta
		jr z,.k30
		cp $31
		jr z,.k31
		cp $60
		jr c,.tb
		jr z,.k60
		ld a,($C094)		; K > $60
		ld c,a
.k60:		ld d,$FF
		ret
.k1:		ld a,($C351)
		jr .ev0
.k31:		ld a,($C3D1)
.ev0:		neg			; H = -A, register 10 = 0
		ld c,a
		ld d,0
		ld a,1
		ld (.m+1),a
		ret
.k30:		ld d,$18
		ld a,($D030)
		ld c,a
		ret
.ta:		push hl			; H = ($D000 + K), high byte from the RAM code
		ld l,a
		ld a,($D505)
		ld h,a
		ld c,(hl)
		pop hl
		ret
.tb:		push hl			; H = ($D200 + K)
		ld l,a
		ld a,($D585)
		ld h,a
		ld c,(hl)
		pop hl
		ret
