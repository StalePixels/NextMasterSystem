; l2draw.asm: drawing on the information screen's Layer 2 (info.c).
; Banked with info.c.

		section BANK_56_H
		include "memplan.inc"

		public _l2_glyph

; void l2_glyph(struct l2g *p) __z88dk_fastcall
; struct l2g { uint8_t y, x; const uint8_t *glyph; uint8_t fg, bg; }
; One 8x8 character at (x, y) of the 256x192 Layer 2 in pages L2_PAGE and
; up, from 8 glyph bytes (top row first, left pixel in bit 7): set bits in
; fg, clear bits in bg, or left as they are when bg is $E3. Each line's page
; is mapped at $C000 (MMU 6) for its pixels. Keeps IX and IY.
_l2_glyph:	push ix
		push iy
		ld a,(hl)
		ld iyh,a		; y
		inc hl
		ld a,(hl)
		ld iyl,a		; x
		inc hl
		ld e,(hl)
		inc hl
		ld d,(hl)		; the glyph
		inc hl
		ld a,(hl)
		ld ixh,a		; fg
		inc hl
		ld a,(hl)
		ld ixl,a		; bg
		ex de,hl
		exx
		ld b,8			; lines
		exx
l2_glyph__row:	ld a,iyh		; page L2_PAGE + y / 32 at $C000
		rlca
		rlca
		rlca
		and 7
		add a,L2_PAGE
		nextreg $56,a
		ld a,iyh		; DE = $C000 + (y & 31) * 256 + x
		and 31
		or $C0
		ld d,a
		ld a,iyl
		ld e,a
		inc iyh
		ld c,(hl)
		inc hl
		ld b,8
l2_glyph__px:	sla c
		ld a,ixh
		jr c,l2_glyph__put
		ld a,ixl
		cp $E3
		jr z,l2_glyph__next
l2_glyph__put:	ld (de),a
l2_glyph__next:	inc e
		djnz l2_glyph__px
		exx
		dec b
		exx
		jr nz,l2_glyph__row
		pop iy
		pop ix
		ret
