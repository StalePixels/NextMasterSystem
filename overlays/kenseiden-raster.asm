; Kenseiden: register 8 for every line of the intro's title wave, as the
; game's line interrupt handler sets it. Called once a frame by the runtime
; (rast_frame in fw3.asm) with HL = table of 192 bytes to fill, IX = the
; runtime's copy of VDP registers 0-10, game RAM at $C000. Carry set on
; return: the table is valid.
;
; The intro ($0ABD) copies the handler from $0CCB to $C600 and clears the
; table at $C700-$C7FF: entry n, at $C700+2n, is the H for event n and the
; register 10 value after it. It sets entry 0's register 10 to $1D and entry
; 49's to $FF; entries 2-49 hold the wave ($0AFE), the rest H 0. The frame
; handler ($019F) sets register 10 to 0. The counter takes a new register 10
; only when it reloads at the next event, so event 0 comes at line 0, event 1
; at line 1, event k at line 29+k for k = 2-49, and event 50 at line 79; then
; no more. The H of an event applies from the line after it: entries 0 and 1
; (both 0) to line 31, entry k from line 30+k, and entry 50 from line 80 to
; the bottom of the picture.
; Any other time (line interrupts off, or the other handler, from $5E80, at
; $C600) the table is not valid and the game gets its line events.
		org $3C00
		or a
		bit 4,(ix+0)		; line interrupts off: no table
		ret z
		ld a,($C600)
		cp $E5			; PUSH HL: the wave handler from $0CCB
		ret nz
		ld a,($C700)		; lines 0-30: entry 0 (entry 1 is also 0)
		ld b,31
.top:		ld (hl),a
		inc hl
		djnz .top
		ld de,$C702		; lines 31-79: entries 1-49
		ld b,49
.wave:		ld a,(de)
		ld (hl),a
		inc hl
		inc de
		inc de
		djnz .wave
		ld b,112
		ld a,(de)		; lines 80-191: entry 50
.low:		ld (hl),a
		inc hl
		djnz .low
		scf
		ret
