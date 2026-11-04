; Ayrton Senna's Super Monaco GP II: register 8 for every line, as the game's
; line interrupt handler ($0038 with the status bit 7 clear) sets it. Called
; once a frame by the runtime (rast_frame in fw3.asm) with HL = table of 192
; bytes to fill, IX = the runtime's copy of VDP registers 0-10, game RAM at
; $C000. Carry set on return: the table is valid.
;
; In the race ($C03C not 0) the frame handler ($0282) sets register 10 = $1F,
; H = ($C030) and the event counter $C07B = $F6. Each line event adds 1 to
; $C07B and then, by the new count K:
;   K = 0-$2F      H = (($C07C) * 256 + K), the road table
;   K = $30-$7F    H = 0, register 10 = $FF
;   K = $F8        H = ($C31B)
;   K = ($C04D)    H = ($C323); when K is also $FF, register 10 = 0
;   K = $FF        register 10 = 0
;   other K        register 10 = 7
; So the race has events at line 31, then every 8 lines from line 63 to the
; event with K = $FF, then one every line for the 48 road lines and the
; event K = $30 that sets H = 0 for the HUD below the road.
;
; Only a frame with every-line events (K = $FF, register 10 = 0) gets a
; table. Any other frame returns carry clear and the game takes its line
; interrupts.
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
		ld a,($C03C)		; not the race: no table
		or a
		ret z
		xor a
		ld (.m+1),a		; no every-line event yet
		ld a,$F6
		ld (.k+1),a		; event counter, as the frame handler sets it
		ld c,(ix+8)		; H until the first event
		ld d,$1F		; D = register 10, used at the next reload
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
.hand:		cp $30
		jr c,.tab
		cp $80
		jr c,.k30
		cp $F8
		jr z,.kf8
		push hl
		ld hl,$C04D
		cp (hl)
		pop hl
		jr z,.c4d
		inc a
		jr z,.kff
		ld d,7
		ret
.c4d:		inc a			; Z: K = $FF
		ld a,($C323)
		ld c,a
		ret nz
.kff:		ld d,0
		ld a,1
		ld (.m+1),a
		ret
.kf8:		ld a,($C31B)
		ld c,a
		ret
.k30:		ld c,0
		ld d,$FF
		ret
.tab:		push hl			; H = (($C07C) * 256 + K)
		ld l,a
		ld a,($C07C)
		ld h,a
		ld c,(hl)
		pop hl
		ret
