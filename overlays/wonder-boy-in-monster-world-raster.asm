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
;
; Priority tiles: with the priority switch the runtime draws the priority
; cells a second time in Layer 2 and moves Layer 2's X (NextReg $16) only on a
; register 8 write, which goes only into its copy of the registers while this
; table is valid; its per-line copper list does not write $16. So the routine
; sets Layer 2's X for one band (X = -H - 2, as the runtime's pri_x, with
; PIC_X = 2) and clips Layer 2 (NextReg $18) to that band's lines:
; - Play: the playfield, lines N + 1 to 191. Lines 0 to N are the status bar
;   (name table rows 0-3), where every cell has the priority bit and no pixel
;   of colour 0, so on a Master System no sprite shows there. The routine
;   clips the sprites (NextReg $19) to lines N + 1 to 191 instead, and the
;   tilemap shows the bar.
; - The title: lines 0 to N; sprites not clipped.
; - States 6 and 7: the longer of the bands below the status bar; sprites
;   clipped to lines N + 1 to 191.
; The clip values are the runtime's (clip_update in fw2.asm): Layer 2 x from
; PIC_X (+ 8 when register 0 bit 5 hides column 0) to 255; sprite x from 17
; (+ 4) to 144 in units of 2 pixels, sprite y = SMS line + 32. Without a table
; the routine puts the runtime's full clips back; the runtime then sets X
; (hscroll_set). In 224-line mode it leaves Layer 2 and the sprites alone.
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
.no:		ld a,(.cl)		; the runtime's clips back, if this routine
		or a			; changed them
		ret z			; carry clear
		xor a
		ld (.cl),a
		ld b,a
		ld d,a
		ld e,191
		call .clip
		or a
		ret
.title:		ld de,$C0A1
		call .two
		ld b,0			; Layer 2: lines 0 to N at the frame's H
		ld d,b
		ld e,c
		ld a,(ix+8)
		jr .lay
.play:		ld de,$C66C
		call .two
		ld a,c			; Layer 2 and sprites: lines N + 1 to 191
		inc a
		ld b,a
		ld d,a
		ld e,191
		ld a,($C66C)
		jr .lay
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
		ld a,c			; sprites: lines N + 1 to 191
		inc a
		ld b,a
		cp 10			; N >= 9: the band at ($C66C) is the longer
		jr c,.three3
		ld d,a			; Layer 2: lines N + 1 to 2N + 82
		ld a,c
		add a,a
		add a,82
		ld e,a
		ld a,($C66C)
		jr .lay
.three3:	ld a,c			; Layer 2: lines 2N + 83 to 191
		add a,a
		add a,83
		ld d,a
		ld e,191
		ld a,($C6E0)
; A = the band's H, D to E its lines, sprites from line B: Layer 2's X and
; the clips. The table is valid.
.lay:		bit 1,(ix+0)		; 224-line mode (register 0 bit 1, register 1
		jr z,.lay1		; bit 4): the runtime's Layer 2 is another
		bit 4,(ix+1)		; layout, left alone
		jr nz,.ok
.lay1:		neg			; Layer 2 X: map column K = -H at SMS x 0,
		sub 2			; minus PIC_X (2), as the runtime's pri_x
		db $ED,$92,$16		; NEXTREG $16,A
		ld a,1
		ld (.cl),a
		call .clip
.ok:		scf
		ret
; Lines 0 to N at the frame's H, lines N + 1 to 191 at (DE). Keeps C, DE.
.two:		ld a,(ix+8)
		ld b,c
		inc b
		call .fill
		ld a,191
		sub c
		ld b,a
		ld a,(de)
.fill:		ld (hl),a
		inc hl
		djnz .fill
		ret
; Layer 2 clip lines D to E, sprite clip lines B to 191. The routine runs
; inside the once-a-frame work, where no handler that writes the clips
; (register 0) can come between the writes.
.clip:		db $ED,$91,$1C,$03	; NEXTREG $1C,3: reset the Layer 2 and sprite clip indexes
		ld a,(ix+0)
		and $20
		rrca
		rrca
		rrca			; 4 or 0: column 0 hidden, in units of 2 pixels
		ld c,a
		add a,a
		add a,2			; PIC_X
		db $ED,$92,$18		; NEXTREG $18,A
		db $ED,$91,$18,255	; NEXTREG $18,255
		ld a,d
		db $ED,$92,$18		; NEXTREG $18,A
		ld a,e
		db $ED,$92,$18		; NEXTREG $18,A
		ld a,c
		add a,17
		db $ED,$92,$19		; NEXTREG $19,A
		db $ED,$91,$19,144	; NEXTREG $19,144
		ld a,b
		add a,32
		db $ED,$92,$19		; NEXTREG $19,A
		db $ED,$91,$19,223	; NEXTREG $19,223
		ret
.cl:		db 0			; 1 while the clips are this routine's
