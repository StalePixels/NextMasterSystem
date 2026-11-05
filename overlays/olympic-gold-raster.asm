; Olympic Gold: register 8 for every line, as the game's line interrupt handler sets it.
; Called once a frame by the runtime (rast_frame in fw3.asm) with HL = table of 192 bytes to
; fill, IX = the runtime's copy of VDP registers 0-10, game RAM at $C000. Carry set on
; return: the table is valid.
;
; While ($C88B) is not 0 (the events with a scrolling picture and a status bar), the frame
; interrupt ($00A1-$00C9) sets H for the top of the picture (-($C88E), or -($C88E) / 2 when
; ($C88B) bit 2 is clear), keeps -($C88E) in ($C892) and sets register 10 to $23. The line
; interrupt handler ($0041) counts its events in ($C88C): the first, at line 35, sets register
; 10 to $6E; the second, at line 71, sets H = ($C892); the third, at line 182, sets H = 0 for
; the status bar. Each write lands in the line after its event, so H changes from lines 73 and
; 184. The count is the fault this routine removes: the SMS keeps one line interrupt pending,
; so when the first event is taken after line 71 the first two become one, the count falls
; behind, and the bar gets the pool's H. On the Next that happens whenever the frame handler
; and the runtime's once-a-frame work run past line 71 (swimming).
;
; With a valid table the runtime gives the game no line interrupts, and register 8 writes go
; only to the register copy, so (IX+8) is the H the frame handler wrote last, the top's.
; ($C892) is from the same run of the handler.
;
; Priority tiles: the runtime draws them in Layer 2 and moves Layer 2's X (pri_x, NextReg
; $16) only on a register 8 write (hscroll_set in fw2.asm), which goes nowhere while this
; table is valid, and the raster copper list (cop_raster in fw3.asm) does not write $16. In
; these events the priority cells are the status bar's (row 23, H = 0) and, in archery, the
; inset at the top, which does not scroll; so the routine sets Layer 2's X for H = 0 (K - 2
; with K = 0, as hscroll_set does). Without a table, rast_frame sets $16 again through
; hscroll_set.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,($C88B)
		or a
		ret z			; no split: the game's line handler does nothing
		ld a,(ix+8)		; lines 0-72: the top's H
		ld b,73
.top:		ld (hl),a
		inc hl
		djnz .top
		ld a,($C892)		; lines 73-183: the play area's H
		ld b,111
.play:		ld (hl),a
		inc hl
		djnz .play
		xor a			; lines 184-191: the status bar, H = 0
		ld b,8
.bar:		ld (hl),a
		inc hl
		djnz .bar
		db $ED,$91,$16,254	; NEXTREG $16,254: Layer 2 X for H = 0
		scf
		ret
