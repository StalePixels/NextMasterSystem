; F1: register 8 for every line of the title and of the one-player race.
; Called once a frame by the runtime with HL = table of 192 bytes to fill,
; IX = the runtime's copy of VDP registers 0-10, game RAM at $C000. Carry set
; on return: the table is valid, and the game gets no line interrupts.
;
; Race: the frame handler $700C writes register 8 = ($C9A3) and, while the
; road is drawn ($C99E not 0), register 10 = $2B and the line handler chain
; $7789/$7798 ($7931). Line 43 sets register 10 = 0, so from line 87 each line
; interrupt writes register 8 = the next byte of the table at $C230, 47 of
; them, then 0. Lines 0-87 have H = ($C9A3), lines 88-134 the table, lines
; 135-191 H = 0.
;
; Title: the frame handler $79D1 writes register 8 = 0; the line handler
; $7A3B, at line 182 (register 10 = $B6, set at $6911), writes register 8 =
; ($C70D) for the credits row, lines 184-191. The rest of that handler's
; work (the scroll step and the next letter) runs from the frame handler,
; in the cave cv_title of f1.spec.
;
; Every other screen: carry clear.
		org $3C00
		bit 4,(ix+0)		; line interrupts off: no table
		jr z,.no
		ld a,(ix+10)
		cp $2B
		jr z,.race
		cp $B6
		jr nz,.no
		ld de,$79D1		; title: frame handler $79D1
		call .hnd
		jr nz,.no
		ld a,(ix+8)
		ld b,184
.t0:		ld (hl),a
		inc hl
		djnz .t0
		ld a,($C70D)
		ld b,8
.t1:		ld (hl),a
		inc hl
		djnz .t1
		scf
		ret
.race:		ld de,$700C		; race: frame handler $700C
		call .hnd
		jr nz,.no
		ld a,($C99E)
		or a
		jr z,.no
		ld a,(ix+8)
		ld b,88
.r0:		ld (hl),a
		inc hl
		djnz .r0
		ex de,hl
		ld hl,$C230
		ld bc,47
		ldir
		ex de,hl
		xor a
		ld b,57
.r1:		ld (hl),a
		inc hl
		djnz .r1
		scf
		ret
.no:		or a
		ret
; Z when the word at $C882 (the frame handler) is DE.
.hnd:		ld a,($C882)
		cp e
		ret nz
		ld a,($C883)
		cp d
		ret
