; Legend of Illusion: register 8 for every line, as the game's line interrupt
; handler ($079E) sets it. Called once a frame by the runtime (rast_frame in
; fw3.asm) with HL = table of 192 bytes to fill, IX = the runtime's copy of
; VDP registers 0-10, game RAM at $C000. Carry set on return: the table is valid.
;
; The frame code ($0713) turns line interrupts on in game states ($C301) 1, 2
; and 5, sets register 10 = ($C30E) and H = ($C41C), or ($C571) on level $0C
; ($C302). State 2 sets ($C30E) = $7F and ($C310) = 0 first.
; - ($C310) = 0: the first event (line ($C30E)) sets H = 0 for the status bar.
; - Else each event steps ($C30F) to i and reads the word table at $C311:
;   $FF sets H = 0 for the status bar and ends the bands; any other value is
;   the next register 10 value, with H = ($C331 + 2i).
; An event at line L sets H from line L+1. The line counter reloads at each
; event with the register 10 value of that moment, so the next event comes at
; L + 1 + (the value the event before wrote).
;
; Priority tiles: the runtime draws them in Layer 2 and moves Layer 2's X only
; on a register 8 write, which goes nowhere while this table is valid. With a
; valid table in 192-line mode, the routine takes the H of the longest run of
; lines with one H (the playfield), sets Layer 2's X for it (NextReg $16) and
; clips Layer 2 (NextReg $18) to the lines from the first to the last line with
; that H. The status bar below, at another H, is left to the tilemap. Lines
; inside with another H (the snow's ripple in stage 1) show Layer 2 at the
; playfield's H. Without a table it puts the runtime's clip back.
		org $3C00
		xor a
		ld (.n),a
		ld (.fc),a
		ld de,.fl
		ld (.fp),de
		ld a,($C301)
		cp 2
		jr z,.st2
		cp 1
		jr z,.cfg
		cp 5
		jr z,.cfg
		jp .nol2		; no bands in this state: no table
.st2:		ld b,$7F
		jr .single
.cfg:		ld a,($C30E)
		ld b,a
		ld a,($C310)
		or a
		jr nz,.bands
.single:	call .toph		; lines 0 to B: the frame's H
		call .fillto
		xor a			; the rest: H = 0
.end:		ld b,191
		call .fillto
		jp .l2
.bands:		call .toph		; lines 0 to the first event: the frame's H
		call .fillto
		ld a,b
		ld (.l),a
		ld (.r),a		; the counter reloads with ($C30E) at the first event
		ld de,$C311+2		; i = 1
.bl:		ld a,(.l)
		cp 191
		jr nc,.done
		ld a,(de)
		cp $FF
		jr z,.zero
		ld c,a			; the event writes register 10 = C
		ld a,(.r)
		ld b,a			; the counter reloads with the value before it
		ld a,c
		ld (.r),a
		ld a,(.l)
		add a,b
		jr c,.big
		inc a
		jr nz,.nxt
.big:		ld a,255
.nxt:		ld (.l),a
		ld b,a			; next event's line
		push de
		ld a,e
		add a,$20		; $C331 + 2i
		ld e,a
		ld a,(de)
		pop de
		call .fillto		; H from this event to the next one
		inc de
		inc de
		ld a,e
		cp $11+32		; i up to 15
		jr c,.bl
.done:		dec hl			; the lines left keep the last H
		ld a,(hl)
		inc hl
		jr .end
.zero:		xor a
		jr .end

; A = the frame's H: ($C571) on level $0C, else ($C41C).
.toph:		ld a,($C302)
		cp $0C
		ld a,($C41C)
		ret nz
		ld a,($C571)
		ret

; Fill the table from line (.n) to line min(B, 191) with A. Keeps B and DE.
.fillto:	push af
		ld a,(.n)
		ld c,a
		ld a,b
		cp 192
		jr c,.ft1
		ld a,191
.ft1:		sub c
		jr c,.ftnone		; that line is already filled
		inc a
		ld c,a
		ld a,(.n)
		ld (.fs),a
		add a,c
		ld (.n),a
		pop af
		call .rec
.ftl:		ld (hl),a
		inc hl
		dec c
		jr nz,.ftl
		ret
.ftnone:	pop af
		ret

.n:		db 0			; next line to fill
.l:		db 0			; line of the last event
.r:		db 0			; register 10 value the counter reloads with

; Note a fill (first line (.fs), C lines, H = A) in the list at .fl. Keeps all.
.rec:		push af
		push hl
		push de
		ld e,a
		ld hl,(.fp)
		ld a,(.fs)
		ld (hl),a
		inc hl
		ld (hl),c
		inc hl
		ld (hl),e
		inc hl
		ld (.fp),hl
		ld hl,.fc
		inc (hl)
		pop de
		pop hl
		pop af
		ret

; From the list of fills: the H of the longest run of lines with one H (.bh),
; then the first (D) and the last (C) line with that H.
.l2:		ld a,(ix+0)		; 224-line mode (register 0 bit 1, register 1
		and 2			; bit 4): the runtime's Layer 2 is another
		jr z,.l2go		; layout, left alone
		bit 4,(ix+1)
		jr nz,.l2ok
.l2go:		ld a,(.fc)
		or a
		jr z,.l2ok
		ld b,a
		ld a,(.fl+2)
		ld (.ch),a
		xor a
		ld (.crl),a
		ld (.blen),a
		ld hl,.fl
.ml:		inc hl			; the first line: not needed here
		ld c,(hl)		; lines
		inc hl
		ld a,(.ch)
		cp (hl)
		jr z,.madd
		call .mclose
		ld a,(hl)
		ld (.ch),a
		xor a
		ld (.crl),a
.madd:		ld a,(.crl)
		add a,c
		ld (.crl),a
		inc hl
		djnz .ml
		call .mclose
		ld a,(.fc)
		ld b,a
		ld hl,.fl
		ld d,$FF		; D = first line, $FF for none yet
.fsl:		push bc
		ld b,(hl)		; first line of the fill
		inc hl
		ld c,(hl)		; lines
		inc hl
		ld a,(.bh)
		cp (hl)
		inc hl
		jr nz,.fsn
		ld a,d
		inc a
		jr nz,.fs1
		ld d,b
.fs1:		ld a,b
		add a,c
		dec a
		ld e,a			; E = last line
.fsn:		pop bc
		djnz .fsl
		ld c,e			; C = last line
		ld a,(.bh)		; Layer 2 X: map column K = -H at SMS x 0,
		neg			; minus PIC_X (2), as the runtime's pri_x
		sub 2
		ld e,a
		ld a,1
		ld (.cl),a
		call .clip
		ld a,e
		db $ED,$92,$16		; NEXTREG $16,A
.l2ok:		scf
		ret

; The run (.crl lines at H (.ch)) ends: the longest so far (the first of equal
; length) goes to (.blen) and (.bh).
.mclose:	ld a,(.blen)
		ld d,a
		ld a,(.crl)
		cp d
		ret c
		ret z
		ld (.blen),a
		ld a,(.ch)
		ld (.bh),a
		ret

; No table: the runtime's Layer 2 clip, lines 0-191, if this routine changed it.
.nol2:		ld a,(.cl)
		or a
		ret z			; carry clear
		xor a
		ld (.cl),a
		ld d,a
		ld c,191
		call .clip
		or a
		ret

; Layer 2 clip: x from PIC_X (+ 8 when register 0 bit 5 hides column 0) to 255,
; lines D to C. The routine runs inside the once-a-frame work, where no handler
; that writes the clip (register 0) can come between the four writes.
.clip:		db $ED,$91,$1C,$01	; NEXTREG $1C,1: reset the Layer 2 clip index
		ld a,(ix+0)
		and $20
		rrca
		rrca			; 8 or 0
		add a,2			; PIC_X
		db $ED,$92,$18		; NEXTREG $18,A
		db $ED,$91,$18,255	; NEXTREG $18,255
		ld a,d
		db $ED,$92,$18		; NEXTREG $18,A
		ld a,c
		db $ED,$92,$18		; NEXTREG $18,A
		ret

.fs:		db 0			; first line of the fill being noted
.fc:		db 0			; fills in the list
.fp:		dw 0			; next free entry
.fl:		ds 3*24			; the fills: first line, lines, H
.ch:		db 0			; H of the run being merged
.crl:		db 0			; its lines
.blen:		db 0			; the longest run: its lines
.bh:		db 0			; its H
.cl:		db 0			; 1 while the clip is this routine's
