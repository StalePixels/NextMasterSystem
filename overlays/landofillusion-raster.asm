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
; Modes 1 and 2 are set by object code in bank 31 ($7C5C9, $7D36A).
;
; Priority tiles: the runtime draws them in Layer 2 and moves Layer 2's X
; (pri_x, NextReg $16) only on a register 8 write (hscroll_set in fw2.asm),
; which goes nowhere while this table is valid, and the raster copper list
; (cop_raster in fw3.asm) does not write $16. With a valid table the routine
; takes the longest run of lines with one H (the first of equal length), sets
; Layer 2's X for that H as hscroll_set does, and clips Layer 2 (NextReg $18,
; x as clip_update in fw2.asm) to the lines of that run only. In mode 0 that
; is the playfield, lines 0-159; the status bar below, at H = 0, is left to
; the tilemap (in play no sprite reaches its lines). When every line has one H
; the clip is the whole picture. Without a table it puts the runtime's clip
; back; rast_frame then sets $16 again through hscroll_set. The game's
; register 0 writes in play change only bit 4, which leaves the clip alone
; (clip_update runs on a change of bit 3 or 5).
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		jp z,.nol2
		xor a
		ld (.n),a		; next line
		ld (.bl),a		; the longest run: none yet
		ld (.rl),a		; the run being read: none yet
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
		call .close
		ld a,(.bs)
		ld d,a			; D = first line
		ld hl,.bl
		add a,(hl)
		dec a
		ld c,a			; C = last line
		ld a,1
		ld (.cl),a
		call .clip
		ld a,(.bh)		; Layer 2 X: map column K = -H at SMS x 0,
		neg			; minus PIC_X (2), as pri_x
		sub 2
		db $ED,$92,$16		; NEXTREG $16,A
		scf
		ret

; Fill B lines of the table with H = A. A fill with the H of the run being
; read lengthens that run; another H ends it and starts a new run.
.fill:		ld c,a
		ld a,(.rl)
		or a
		jr z,.fnew		; no run yet
		ld a,(.rh)
		cp c
		jr z,.fadd
		call .close
.fnew:		ld a,c
		ld (.rh),a
		ld a,(.n)
		ld (.rs),a
		xor a
		ld (.rl),a
.fadd:		ld a,(.rl)
		add a,b
		ld (.rl),a
		ld a,(.n)
		add a,b
		ld (.n),a
		ld a,c
.fl:		ld (hl),a
		inc hl
		djnz .fl
		ret

; The run being read ends: longer than the longest so far, it becomes the
; longest (the first of equal length stays).
.close:		ld a,(.bl)
		ld e,a
		ld a,(.rl)
		cp e
		ret c
		ret z
		ld (.bl),a
		ld a,(.rs)
		ld (.bs),a
		ld a,(.rh)
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

.n:		db 0			; next line to fill
.rs:		db 0			; the run being read: first line
.rl:		db 0			; its lines
.rh:		db 0			; its H
.bs:		db 0			; the longest run: first line
.bl:		db 0			; its lines
.bh:		db 0			; its H
.cl:		db 0			; 1 while the clip is this routine's
