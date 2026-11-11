; Renegade: register 8 for every line, as the game's line interrupt handler
; sets it. Called once a frame by the runtime (rast_frame in fw3.asm) with
; HL = table of 192 bytes to fill, IX = the runtime's copy of VDP registers
; 0-10, game RAM at $C000. Carry set on return: the table is valid.
;
; With $C004 bit 4 set, the frame handler ($0346) turns line interrupts on,
; sets register 10 to 0 and points $D1FE at the band table at $D181. Entry
; k, at $D181+2k, holds the H for event k and the register 10 value that the
; handler ($0362) writes after it; a register 10 of 0 is the last entry
; ($037F turns line interrupts off). The counter takes a new register 10 only
; when it reloads at the next event, so event 0 comes at line 0, event 1 at
; line 1, and event k+2 at n(k) + 1 lines after event k+1. The H of an event
; applies from the line after it; line 0 shows the frame handler's H ($02EB).
; With a V scroll ($C201, written to register 9 at $02EB) the table is not
; valid; nestcave in the spec makes the same test.
		org $3C00
		or a
		ld a,($C004)
		bit 4,a			; no bands this frame: no table
		ret z
		ld a,($C201)		; V scroll: the per-line list does not wrap
		or a			; at line 224, so the game's events do it
		ret nz
		ld a,(ix+8)		; line 0
		ld (hl),a
		inc hl
		ld c,191		; lines left
		ld de,$D181
		ld b,1			; entry 0: line 1
.ent:		inc de
		ld a,(de)		; register 10 after this entry
		dec de
		or a
		jr z,.last
		push af
		ld a,(de)		; H
.fill:		ld (hl),a
		inc hl
		dec c
		jr z,.full
		djnz .fill
		pop af
		inc a
		ld b,a			; lines to the event after next
		inc de
		inc de
		jr .ent
.full:		pop af
		scf
		ret
.last:		ld a,(de)		; the last H to the bottom
.lf:		ld (hl),a
		inc hl
		dec c
		jr nz,.lf
		scf
		ret
