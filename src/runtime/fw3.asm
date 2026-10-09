; fw3.asm: the framework's third page (FW3_PAGE), mapped at $0000 (MMU0)
; only while the once-a-frame work runs (fw2_vbl maps it; restore_mmu puts
; the game's page back): the normal copper list, the transparent pixel
; value scans and their tables. Nothing here may run from a handler.

;		org $0000  (section origin)
tm_mask:	ds 1024			; per SMS tile: 16-bit set of pixel values it uses
tm_valid:	ds 64			; per tile, one bit: tm_mask is current
bits16:		dw 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768

; ----------------------------------------------------------------------
; Transparent pixel value. The tilemap treats one 4-bit pixel value as
; transparent and shows the fallback colour, CRAM v, there; that is right
; for background-palette tiles but wrong for sprite-palette tiles that use
; v (they should show CRAM 16+v). Every 8 frames this collects the pixel
; values used by the tiles that the name table shows with the sprite
; palette, into tr_free (values they do not use); fallback2 (fw2.asm)
; picks v from it when no v has CRAM v = CRAM 16+v.
; ----------------------------------------------------------------------
pal_scan:
		ld hl,(nt_base)
		ld a,h
		add a,$40
		ld h,a			; name table in the shadow
		ld de,0			; values used
		ld bc,896
pal_scan__l:		inc hl
		ld a,(hl)		; high byte
		bit 3,a
		jr z,pal_scan__n
		push bc
		push hl
		push de
		and 1
		ld b,a
		dec hl
		ld c,(hl)		; BC = tile
		call tile_mask
		pop de
		ld a,e
		or l
		ld e,a
		ld a,d
		or h
		ld d,a
		pop hl
		pop bc
pal_scan__n:		inc hl
		dec bc
		ld a,b
		or c
		jr nz,pal_scan__l
		ld a,e
		cpl
		ld l,a
		ld a,d
		cpl
		ld h,a
		ld de,(tr_free)
		or a
		sbc hl,de
		jr nz,pal_scan__ch
		ld a,d			; unchanged; with no free value the rows may have
		or e			; changed: update anyway
		ret nz
pal_scan__ch:		add hl,de
		ld (tr_free),hl
		jp fallback2

; With no free pixel value (tr_free = 0), pixel value 0 shows CRAM 0 or
; CRAM 16 (fallback2 in fw2.asm). For screen row pr_cur (one a
; frame, all 24 in 24 frames): do sprite-palette or background-palette
; tiles show pixel value 0 more? Then pal_rows[s] for screen row s = the
; sprite rows less the background rows from s to the bottom (V scroll
; taken to the row).
pal_rows_step:
		ld a,(vdp_regs+9)
		rrca
		rrca
		rrca
		and $1F
		ld (pr_r0),a		; name table row at screen row 0
		ld a,(pr_cur)
		ld b,a			; screen row
		inc a
		cp 24
		jr c,pal_rows_step__c
		xor a
pal_rows_step__c:		ld (pr_cur),a
		ld c,1
pal_rows_step__row:		push bc
		ld a,(pr_r0)
		add a,b
		cp 28
		jr c,pal_rows_step__r
		sub 28
pal_rows_step__r:		ld e,a			; name table row
		ld d,64
		mul d,e
		ld hl,(nt_base)
		add hl,de
		ld a,h
		add a,$40
		ld h,a
		xor a
		ld (pr_n),a		; sprite cells less background cells using 0
		ld (pr_bgm),a		; values background cells use
		ld (pr_bgm+1),a
		ld b,32
pal_rows_step__cell:		push bc
		ld c,(hl)
		inc hl
		ld a,(hl)
		inc hl
		push hl
		ld e,a
		and 1
		ld b,a
		push de
		call tile_mask
		pop de
		bit 3,e
		jr nz,pal_rows_step__sp
		ld a,(pr_bgm)		; background palette: its values
		or l
		ld (pr_bgm),a
		ld a,(pr_bgm+1)
		or h
		ld (pr_bgm+1),a
		bit 0,l
		jr z,pal_rows_step__nx
		ld hl,pr_n
		dec (hl)
		jr pal_rows_step__nx
pal_rows_step__sp:		bit 0,l
		jr z,pal_rows_step__nx
		ld hl,pr_n
		inc (hl)
pal_rows_step__nx:		pop hl
		pop bc
		djnz pal_rows_step__cell
		pop bc
		ld a,(pr_n)		; +1 sprite palette, -1 background
		or a
		jr z,pal_rows_step__z
		ld a,1
		jp p,pal_rows_step__z
		ld a,$FF
pal_rows_step__z:		ld hl,pr_flag
		ld e,b
		ld d,0
		add hl,de
		ld (hl),a
		ld hl,pr_bgrow		; this row's background values
		add hl,de
		add hl,de
		ld a,(pr_bgm)
		ld (hl),a
		inc hl
		ld a,(pr_bgm+1)
		ld (hl),a
		inc b
		dec c
		jp nz,pal_rows_step__row
		; sums from the bottom
		ld hl,pr_flag+23
		ld de,pal_rows+23
		ld b,24
		xor a
pal_rows_step__sum:		add a,(hl)
		ld (de),a
		dec hl
		dec de
		djnz pal_rows_step__sum
		; bg_free = values no row's background tiles use
		ld hl,pr_bgrow
		ld de,0
		ld b,24
pal_rows_step__or:		ld a,(hl)
		or e
		ld e,a
		inc hl
		ld a,(hl)
		or d
		ld d,a
		inc hl
		djnz pal_rows_step__or
		ld a,e
		cpl
		ld e,a
		ld a,d
		cpl
		ld d,a
		ld (bg_free),de
		jp fallback2

pr_cur:		db 0
pr_r0:		db 0
pr_n:		db 0
pr_flag:	ds 24
pr_bgm:		dw 0
pr_bgrow:	ds 48			; per screen row: values its background tiles use

; BC = tile -> HL = set of pixel values in its Next definition (cached)
tile_mask:
		push bc
		ld a,c
		and 7
		ld d,1
		jr z,tile_mask__b
tile_mask__s:		sla d
		dec a
		jr nz,tile_mask__s
tile_mask__b:		ld h,b
		ld l,c
		srl h
		rr l
		srl h
		rr l
		srl h
		rr l
		ld bc,tm_valid
		add hl,bc
		ld a,(hl)
		and d
		jr nz,tile_mask__cached
		ld a,(hl)
		or d
		ld (hl),a
		pop bc
		push bc
		ld h,b
		ld l,c
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		ld de,$8000
		add hl,de
		ld de,0
		ld b,32
tile_mask__c:		ld a,(hl)
		push af
		rrca
		rrca
		rrca
		rrca
		call tile_mask__set
		pop af
		call tile_mask__set
		inc hl
		djnz tile_mask__c
		pop hl
		add hl,hl
		push de
		ld de,tm_mask
		add hl,de
		pop de
		ld (hl),e
		inc hl
		ld (hl),d
		ex de,hl
		ret
tile_mask__cached:	pop hl
		add hl,hl
		ld de,tm_mask
		add hl,de
		ld a,(hl)
		inc hl
		ld h,(hl)
		ld l,a
		ret
; DE |= 1 << (A & 15)
tile_mask__set:		push hl
		and $0F
		add a,a
		ld hl,bits16
		add hl,a
		ld a,(hl)
		or e
		ld e,a
		inc hl
		ld a,(hl)
		or d
		ld d,a
		pop hl
		ret


; ----------------------------------------------------------------------
; Copper. Normal list: three head slots (cop_head), then 5 instructions per
; line y:
;   [WAIT y,c | NOOP] [MOVE $6E,A8 | NOOP] [WAIT y,40] [MOVE $6E,M0]
;   [MOVE $31,V | NOOP]   (the 224-line wrap, for line y+1)
; then WAIT 200,0; MOVE $31,V+224; MOVE $6E,M0; HALT.
; c = h_sw (fw.asm hscroll_set), 0 = no switch. A scroll change rewrites
; only the instructions it moves. Register 0 bit 7 (lock right) uses the
; stage A list instead (WAIT/MOVE $31 around column 24 on every line).
; ----------------------------------------------------------------------
LOCK_H		equ 24			; copper column for SMS column 24 (see PIC_X)
END_H		equ 40			; copper column after the right edge

cop_update:
		ld a,(m224)
		or a
		jp nz,cop_224
		xor a
		ld (cop_dirty),a
		ld a,(vdp_regs+9)
		cp 224
		jr c,cop_update__v
		sub 224
cop_update__v:		ld e,a			; E = V
		; Y offset for the lines still to come in this frame. The vblank
		; work runs late when a game's frame handler keeps interrupts off
		; into the picture (Ecco); past the wrap line the copper has set
		; V already, and V + 224 there would show the rest of the picture
		; 32 lines lower until the next frame.
		cp 33
		jr c,cop_update__y224		; no wrap line in the picture
		call cur_line
		cp 192
		jr nc,cop_update__y224		; vertical blank
		add a,e
		jr c,cop_update__y			; line >= 256 - V: past the wrap line too
		cp 224-1
		jr c,cop_update__y224		; line < 224 - V - 1: before the wrap line
cop_update__y:		ld a,e
		jr cop_update__yset
cop_update__y224:		ld a,e
		add a,224
cop_update__yset:		nextreg $31,a
		nextreg $6E,NR6E_M0
		ld a,(vdp_regs+0)
		and $80
		jr z,cop_update__nolr
		ld a,e			; with V = 0 the locked right columns look the
		or a			; same: the normal list, which does the H
		jp nz,cop_lockright	; scroll wrap and the locked top rows
cop_update__nolr:
		ld a,(vdp_regs+0)
		and $40
		rrca
		rrca
		rrca
		rrca
		rrca			; 2 with register 0 bit 6 (lock top rows), else 0
		ld hl,cop_mode
		cp (hl)
		jr nz,cop_update__full
		or a
		jr z,cop_update__nt
		nextreg $2F,255&((286)>>8)	; lines 0-15: H = 0
		nextreg $30,255&(286)
cop_update__nt:		ld a,(h_sw)
		ld hl,cop_sw
		cp (hl)
		call nz,cop_switches
		ld a,(cop_v)
		cp e
		call nz,cop_wrap
		; X goes into the list (from the next frame on) and, so that the
		; lines still to come in this frame match the switch columns just
		; written, straight into the registers too
		ld a,(cop_mode)
		or a
		jr nz,cop_update__top
		ld hl,-3		; the head: X for this H from line 0
		call cop_at
		call cop_head
		jr cop_update__xnow
cop_update__top:		ld hl,15*5
		call cop_at
		call cop_nosw__l15
		ld hl,15*5+3
		call cop_at
		call cop_topx
		call cur_line
		cp 16
		ret c			; the copper sets X after line 15
cop_update__xnow:		ld a,(h_x+1)
		nextreg $2F,a
		ld a,(h_x)
		nextreg $30,a
		ld a,(pri_x)
		nextreg $16,a
		ret
cop_update__full:		; whole list
		ld (cop_mode),a
		or a
		jr z,cop_update__f0
		nextreg $2F,255&((286)>>8)
		nextreg $30,255&(286)
cop_update__f0:
		ld a,e
		ld (cop_v),a
		ld a,(h_sw)
		ld (cop_sw),a
		ld d,a			; D = c
		nextreg $62,0
		nextreg $61,0
		call cop_head
		ld a,224
		sub e
		dec a
		ld c,a			; line whose block holds the wrap (224-V-1)
		ld b,0			; y
cop_update__line:		ld a,d
		or a
		jr z,cop_update__nosw
		call cop_topline	; Z: no switch on this line (lock top)
		jr z,cop_update__nosw
		ld a,d			; cop_topline changed A
		add a,a
		or $80
		nextreg $60,a		; WAIT y,c
		ld a,b
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_A8
		jr cop_update__e1
cop_update__nosw:		call cop_nosw
cop_update__e1:		nextreg $60,$80 + (END_H << 1)
		ld a,b
		nextreg $60,a
		ld a,(cop_mode)
		or a
		jr z,cop_update__m0
		ld a,b
		cp 15
		jr nz,cop_update__m0
		call cop_topx		; line 15: X for H after the locked rows
		jr cop_update__e2
cop_update__m0:		nextreg $60,$6E
		nextreg $60,NR6E_M0
		ld a,e
		cp 33
		jr c,cop_update__nowr		; wrap below the picture
		ld a,b
		cp c
		jr nz,cop_update__nowr
		nextreg $60,$31
		ld a,e
		nextreg $60,a
		jr cop_update__e2
cop_update__nowr:		nextreg $60,0
		nextreg $60,0
cop_update__e2:		inc b
		ld a,b
		cp 192
		jr nz,cop_update__line
		call cop_tail
		nextreg $62,%11000000	; run, restart every frame
		ret

; Three head slots, run when the copper restarts at line 0: with register 0
; bit 6, X for H = 0 (rows 0-1), so the locked rows are right even when the
; vblank work runs late and a direct X write is still in force; otherwise
; X for the current H (h_x). The third is the Layer 2 X (priority tiles).
cop_head:
		ld a,(cop_mode)
		cp 2
		jr nz,cop_head__n
		nextreg $60,$2F
		nextreg $60,255&((286)>>8)
		nextreg $60,$30
		nextreg $60,255&(286)
		nextreg $60,$16
		nextreg $60,254
		ret
cop_head__n:		nextreg $60,$2F
		ld a,(h_x+1)
		nextreg $60,a
		nextreg $60,$30
		ld a,(h_x)
		nextreg $60,a
		nextreg $60,$16
		ld a,(pri_x)
		nextreg $60,a
		ret

; The switch pair of line B when it has none: NOOP NOOP, but on line 15
; with register 0 bit 6 WAIT 15,40; MOVE $16 (the Layer 2 X after the
; locked rows; cop_topx does the tilemap X in the line's last two slots)
cop_nosw:	ld a,(cop_mode)
		cp 2
		jr nz,cop_nosw__n
		ld a,b
		cp 15
		jr nz,cop_nosw__n
cop_nosw__l15:		nextreg $60,$80 + (END_H << 1)
		nextreg $60,15
		nextreg $60,$16
		ld a,(pri_x)
		nextreg $60,a
		ret
cop_nosw__n:		nextreg $60,0
		nextreg $60,0
		nextreg $60,0
		nextreg $60,0
		ret

; B = line: Z set when the line is in the locked top rows (no switch)
cop_topline:
		ld a,(cop_mode)
		or a
		jr z,cop_topline__no
		ld a,b
		cp 16
		jr nc,cop_topline__no
		xor a
		ret
cop_topline__no:		or 1
		ret

; MOVE $2F,X high; MOVE $30,X low (X = h_x): line 15's last two slots
; with register 0 bit 6. (Its wrap slot is lost; V = 208 then wraps late.)
cop_topx:
		nextreg $60,$2F
		ld a,(h_x+1)
		nextreg $60,a
		nextreg $60,$30
		ld a,(h_x)
		nextreg $60,a
		ret

; WAIT 200; MOVE $31,V+224; MOVE $6E,M0; [MOVE $2F/$30 = 286]; HALT   (E = V)
cop_tail:
		nextreg $60,$80
		nextreg $60,200
		nextreg $60,$31
		ld a,e
		add a,224
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		ld a,(cop_mode)
		cp 2
		jr nz,cop_tail__h
		nextreg $60,$2F		; lock top: X for H = 0 from line 0 on, even
		nextreg $60,255&((286)>>8)	; when the vblank work runs late
		nextreg $60,$30
		nextreg $60,255&(286)
		nextreg $60,$16
		nextreg $60,254
cop_tail__h:		nextreg $60,$FF
		nextreg $60,$FF
		ret

; HL = instruction index: copper write address (copper keeps running)
cop_at:
		inc hl			; past the three head slots
		inc hl
		inc hl
		add hl,hl
		ld a,l
		nextreg $61,a
		ld a,h
		or %11000000
		nextreg $62,a
		ret

; rewrite the switch pair of every line (A = new column)
cop_switches:
		ld (cop_sw),a
		ld d,a
		ld b,0
cop_switches__l:		ld l,b
		ld h,5
		push de
		ld e,l
		ld d,h
		mul d,e
		ex de,hl
		pop de
		call cop_at
		ld a,d
		or a
		jr z,cop_switches__no
		call cop_topline
		jr z,cop_switches__no
		ld a,d			; cop_topline changed A
		add a,a
		or $80
		nextreg $60,a
		ld a,b
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_A8
		jr cop_switches__n
cop_switches__no:		call cop_nosw
cop_switches__n:		inc b
		ld a,b
		cp 192
		jr nz,cop_switches__l
		ret

; move the wrap MOVE from the old V to the new one (E = new V)
cop_wrap:
		ld a,(cop_v)
		call cop_wrap__slot
		jr nc,cop_wrap__n1
		nextreg $60,0		; old slot: NOOP
		nextreg $60,0
cop_wrap__n1:		ld a,e
		ld (cop_v),a
		call cop_wrap__slot
		jr nc,cop_wrap__n2
		nextreg $60,$31
		ld a,e
		nextreg $60,a
cop_wrap__n2:		ld hl,960+1
		call cop_at
		nextreg $60,$31
		ld a,e
		add a,224
		nextreg $60,a
		ret
; A = V: carry set and copper address at the wrap slot if V >= 33
cop_wrap__slot:		cp 33
		ccf
		ret nc
		push de
		ld b,a
		ld a,224-1
		sub b			; line 224-V-1
		ld e,a
		ld d,5
		mul d,e
		ld hl,4
		add hl,de
		pop de
		call cop_at
		scf
		ret

; Register 0 bit 7: columns 24-31 ignore V. Stage A's list: on every line
; one WAIT/MOVE at the column 24 boundary and one after the right edge.
cop_lockright:
		ld a,1
		ld (cop_mode),a
		ld a,e
		ld (cop_v),a
		add a,224
		ld d,a			; D = Y offset before the wrap line
		nextreg $62,0
		nextreg $61,0
		call cop_head
		ld a,224
		sub e
		ld c,a			; C = wrap line (224-V), may be >= 192
		ld b,0			; B = line
cop_lockright__line:		ld a,b
		inc a
		cp c
		ld h,d
		jr c,cop_lockright__before
		ld h,e
cop_lockright__before:	ld a,$80 + (LOCK_H << 1)
		nextreg $60,a
		ld a,b
		nextreg $60,a
		nextreg $60,$31
		nextreg $60,224		; V = 0 for the locked columns
		ld a,$80 + (END_H << 1)
		nextreg $60,a
		ld a,b
		nextreg $60,a
		nextreg $60,$31
		ld a,h
		nextreg $60,a
		inc b
		ld a,b
		cp 192
		jr nz,cop_lockright__line
		call cop_tail
		nextreg $62,%11000000
		ret


; ----------------------------------------------------------------------
; Keyboard: Q up, A down, O left, P right, SPACE button 1, M button 2,
; ENTER (or Mega Drive Start) Pause, CAPS SHIFT + SPACE leaves the game.
; ----------------------------------------------------------------------
kbd_scan:
		ld e,$FF
		ld bc,$FBFE
		in a,(c)
		rra
		jr c,kbd_scan__k1
		res 0,e			; Q up
kbd_scan__k1:		ld b,$FD
		in a,(c)
		rra
		jr c,kbd_scan__k2
		res 1,e			; A down
kbd_scan__k2:		ld b,$DF
		in a,(c)
		rra
		jr c,kbd_scan__k3
		res 3,e			; P right
kbd_scan__k3:		rra
		jr c,kbd_scan__k4
		res 2,e			; O left
kbd_scan__k4:		ld b,$7F
		in a,(c)
		ld d,a
		rra
		jr c,kbd_scan__k5
		res 4,e			; SPACE button 1
kbd_scan__k5:		bit 2,d
		jr nz,kbd_scan__k6
		res 5,e			; M button 2
kbd_scan__k6:		ld a,e
		ld (kbd_dc),a
		ld b,$FE
		in a,(c)
		or d
		and 1
		jr nz,kbd_scan__k7
		ld a,1
		ld (quit_req),a		; CAPS SHIFT + SPACE
kbd_scan__k7:		ld b,$BF
		in a,(c)
		cpl
		and 1
		ld d,a
		in a,($1F)
		rlca
		and 1
		or d			; 1 = Pause held
		ld hl,pause_prev
		ld d,(hl)
		ld (hl),a
		or a
		ret z
		ld a,d
		or a
		ret nz
		ld a,1
		ld (pause_req),a
		ret

; ----------------------------------------------------------------------
; Tiles: convert every dirty tile from the shadow into its Next tile
; definition, and drop its cached sprite pattern. dirty_pages holds a bit
; per tile for each 256-byte VRAM page (8 tiles).
; ----------------------------------------------------------------------
tile_flush:
		xor a
		ld (tiles_dirty),a
		ld hl,dirty_pages
		ld b,64
tile_flush__l:		ld a,(hl)
		or a
		jr z,tile_flush__n
		ld (hl),0
		push hl
		push bc
		ld (cv_mask),a
		ld a,l
		sub 255&(dirty_pages)
		call conv_page
		pop bc
		pop hl
tile_flush__n:		inc l
		djnz tile_flush__l
		ret

; A = VRAM page (0-63), cv_mask = its tiles to convert
conv_page:
		ld (cv_page),a
		add a,$40
		ld iyh,a
		ld iyl,0
		ld a,(cv_page)
		add a,$80
		ld ixh,a
		ld ixl,0
		ld a,(cv_mask)
conv_page__tile:		ld (cv_m),a
		rra
		jr c,conv_page__conv
		ld bc,32
		add ix,bc
		add iy,bc
		jr conv_page__next
conv_page__conv:		ld a,8
conv_page__row:		ld (cv_n),a
		ld b,(iy+0)
		ld c,(iy+1)
		ld d,(iy+2)
		ld e,(iy+3)
		ld h,255&((conv_tables)>>8)
		CONVBYTE 0
		inc h
		CONVBYTE 1
		inc h
		CONVBYTE 2
		inc h
		CONVBYTE 3
		ld bc,4
		add ix,bc
		add iy,bc
		ld a,(cv_n)
		dec a
		jr nz,conv_page__row
conv_page__next:		ld a,(cv_m)
		srl a
		jr nz,conv_page__tile
		; drop the pixel value sets and cached patterns of those tiles
		ld a,(cv_page)
		ld e,a
		ld d,0
		ld hl,tm_valid
		add hl,de
		ld a,(cv_mask)
		cpl
		and (hl)
		ld (hl),a
		ld hl,pri_tiles		; a tile Layer 2 holds for priority cells
		add hl,de
		ld a,(cv_mask)
		and (hl)
		jr z,conv_page__np
		ld (pri_redo),a
conv_page__np:		ld l,e
		ld h,0
		add hl,hl
		add hl,hl
		add hl,hl
		ld de,tile_slot
		add hl,de
		ld a,(cv_mask)
		ld b,8
conv_page__d:		rra
		jr nc,conv_page__dn
		ld (hl),0
conv_page__dn:		inc hl
		djnz conv_page__d
		ld a,1
		ld (sat_dirty),a
		ret

cv_page:	db 0
cv_mask:	db 0
cv_m:		db 0

; ----------------------------------------------------------------------
; Name table base changed: rebuild both Next maps from the shadow.
; MAP_PAGE goes to slot 6 ($C000); vbl_work puts the game's page back.
; ----------------------------------------------------------------------
map_rebuild:
		xor a
		ld (nt_dirty),a
		inc a
		ld (pri_full),a		; Layer 2 too
		nextreg $56,MAP_PAGE
		ld hl,0			; o
map_rebuild__l:		push hl
		ld de,(nt_base)
		add hl,de
		ld de,$4000
		add hl,de
		ld c,(hl)		; value
		pop hl
		push hl
		call nt_put2
		pop hl
		inc hl
		ld a,(m224)
		add a,7			; 28 rows, or 32 in 224-line mode
		cp h
		jr nz,map_rebuild__l
		ret

; HL = o (0..$7FF), C = value: as nt_put in fw.asm, into slot 6
nt_put2:
		ld a,l
		rrca
		and 31
		ld b,a
		bit 0,l
		jr z,nt_put2__even
		ld e,c
		ld d,255&((mapattr_table)>>8)
		ld a,(de)
		ld c,a
nt_put2__even:		ld a,l
		rlca
		rlca
		and 3
		ld e,a
		ld a,h
		add a,a
		add a,a
		or e
		ld e,a
		ld d,16
		mul d,e
		add hl,de
		ld a,h
		or $C0
		ld h,a
		ld (hl),c
		ld a,b
		cp 8
		jr nc,nt_put2__hi
		ld de,64
		add hl,de
		ld (hl),c
		ld de,MAP_A8-16
		add hl,de
		ld (hl),c
		ld de,16
		add hl,de
		ld (hl),c
		ret
nt_put2__hi:		ld de,MAP_A8-16
		add hl,de
		ld (hl),c
		ret


; ----------------------------------------------------------------------
; Sprites. SMS sprite i -> Next sprite i (4-bit pattern, sprite 0 on top).
; Each SMS 8x8 tile (or 8x16 pair) used by a sprite gets a 16x16 Next
; pattern slot, drawn in its top-left corner; 128 slots, reused when a
; slot was not used this frame. One pass: each sprite's pattern is found
; (or uploaded, which moves the attribute index, so it is set back) and
; its attributes written. Zoom = Next scale x2. Then the collision flag.
; ----------------------------------------------------------------------
spr_update:
		ld a,(sat_dirty)
		or a
		jp z,spr_coll
		xor a
		ld (sat_dirty),a
		ld a,(vdp_regs+1)
		and 2
		ld b,a
		ld a,(vdp_regs+6)
		and 4
		or b
		ld hl,spr_mode
		cp (hl)
		jr z,spr_update__same
		ld (hl),a
		call fw2_init		; drop the whole cache
		ld a,(vdp_regs+1)
		and 2
		ld b,a
		ld a,(vdp_regs+6)
		and 4
		or b
		ld (spr_mode),a
spr_update__same:		ld hl,spr_frame
		inc (hl)
		; this frame's constants
		ld a,(vdp_regs+6)
		and 4
		rrca
		rrca
		add a,255&((tile_slot)>>8)
		ld (sp_th),a		; tile_slot page for tiles 0-255 or 256-511
		ld a,(vdp_regs+1)
		and 2
		ld a,$FF
		jr z,spr_update__m
		ld a,$FE		; 8x16: even tile
spr_update__m:		ld (sp_mask),a
		ld a,(vdp_regs+0)
		and 8
		ld a,34			; X offset: border + PIC_X
		jr z,spr_update__x
		ld a,26			; register 0 bit 3: 8 pixels left
spr_update__x:		ld (sp_xo),a
		ld a,(vdp_regs+1)
		rra
		ld a,$80		; 4-bit pattern
		jr nc,spr_update__z
		or %00001010		; zoom: X and Y scale 2
spr_update__z:		ld (sp_a4),a
		ld a,(vdp_regs+1)	; sprite height 8, 16 or 32: sp_ytop = 256 - height
		and 3
		ld b,a
		ld a,$F8
		jr z,spr_update__yt
		ld a,$F0
		dec b
		jr z,spr_update__yt
		dec b
		jr z,spr_update__yt
		ld a,$E0
spr_update__yt:		ld (sp_ytop),a
		ld a,(m224)		; 224-line mode: the picture starts 16 lines
		or a			; higher and ends at line 224
		ld a,33
		ld b,$BF
		jr z,spr_update__y2
		ld a,17
		ld b,$DF
spr_update__y2:		ld (spr_update__ya+1),a
		ld a,b
		ld (spr_update__yb+1),a
		ld bc,$303B
		xor a
		out (c),a
		ld a,(sat_hi)
		add a,$40
		ld h,a
		ld l,0			; HL = Y of sprite 0
spr_update__loop:		ld a,(hl)
		cp $D0
		jr nz,spr_update__n0
		ld a,(m224)		; $D0 ends the list in 192-line mode only
		or a
		jp z,spr_update__end
		ld a,$D0
spr_update__n0:
spr_update__yb:		cp $BF			; $DF in 224-line mode (spr_update sets it)
		jr c,spr_update__vis
		; below the picture, or above it: Y >= 256 - height shows its
		; bottom rows at the top. Sprites wholly off the picture are hidden:
		; the Next would count them in its collision flag.
		ld e,a
		ld a,(sp_ytop)
		dec a
		cp e
		ld a,e
		jr nc,spr_update__hid
spr_update__vis:
spr_update__ya:		add a,33		; Y + 1 + 32 (+ 16 in 224-line mode), top wrap
		ld d,a
		ld a,l
		add a,a
		or $80
		ld l,a
		ld c,(hl)		; X
		inc l
		ld a,(sp_mask)
		and (hl)		; tile
		push hl
		ld l,a
		ld a,(sp_th)
		ld h,a
		ld a,(hl)
		bit 7,a
		jr z,spr_update__miss
		and $7F
		ld b,a			; slot
		ld l,a
		ld h,255&((slot_stamp)>>8)
		ld a,(spr_frame)
		ld (hl),a
spr_update__got:		pop hl
		ld a,(sp_xo)
		add a,c
		out ($57),a		; X low
		ld a,d
		out ($57),a		; Y
		ld a,0
		adc a,a
		out ($57),a		; X bit 8, no mirror, palette 0
		ld a,b
		srl a
		or $C0
		out ($57),a		; visible, 5 bytes, pattern
		ld a,b
		and 1
		rrca
		rrca			; N6 to bit 6
		ld c,a
		ld a,(sp_a4)
		or c
		out ($57),a
		ld a,l			; L = $81 + 2i: back to the Y of sprite i+1
		sub $7F
		rrca
		and $7F
		ld l,a
		cp 64
		jr nz,spr_update__loop
		jr spr_update__end
spr_update__miss:		; upload: cache_get moves port $303B, so set the index back
		ld a,(sp_th)
		sub 255&((tile_slot)>>8)
		ld h,a			; HL = tile 0-511
		push de
		push bc
		call cache_get
		pop bc
		pop de
		ld b,a
		pop hl
		push hl
		ld a,l
		sub $81
		rrca
		and $7F			; i
		push bc
		ld bc,$303B
		out (c),a
		pop bc
		ld a,b
		cp $FF
		jr nz,spr_update__got
		pop hl			; every slot in use: hidden
		ld a,l
		sub $81
		rrca
		and $7F
		ld l,a
spr_update__hid:		xor a
		out ($57),a
		out ($57),a
		out ($57),a
		out ($57),a
		inc l
		ld a,l
		cp 64
		jp nz,spr_update__loop
spr_update__end:		ld a,l
		ld (spr_count),a
		; hide sprites left over from last frame
		ld e,a
		ld a,(spr_last)
		sub e
		jr c,spr_update__done
		jr z,spr_update__done
		ld e,a
		xor a
spr_update__hl:		out ($57),a
		out ($57),a
		out ($57),a
		out ($57),a
		dec e
		jr nz,spr_update__hl
spr_update__done:		ld a,(spr_count)
		ld (spr_last),a
spr_coll:	ld bc,$303B
		in a,(c)
		rra
		ret nc
		ld hl,vdp_status
		set 5,(hl)
		ret

sp_th:		db 0
sp_mask:	db 0
sp_xo:		db 0
sp_a4:		db 0
sp_ytop:	db 0

; HL = SMS tile (0-511) -> A = pattern slot, uploaded if needed; $FF if
; every slot is in use this frame.
cache_get:
		ld (spr_t),hl
		ld de,tile_slot
		add hl,de
		ld a,(hl)
		bit 7,a
		jr z,cache_get__miss
		and $7F
		ld e,a
		ld d,0
		ld hl,slot_stamp
		add hl,de
		ld a,(spr_frame)
		ld (hl),a
		ld a,e
		ret
cache_get__miss:		push hl
		ld b,128
cache_get__f:		ld a,(spr_rr)
		inc a
		and $7F
		ld (spr_rr),a
		ld e,a
		ld d,0
		ld hl,slot_stamp
		add hl,de
		ld a,(spr_frame)
		cp (hl)
		jr nz,cache_get__got
		djnz cache_get__f
		pop hl
		ld a,$FF
		ret
cache_get__got:		ld (hl),a		; stamp
		; forget the slot's old tile
		ld hl,slot_tile
		add hl,de
		add hl,de
		ld c,(hl)
		inc hl
		ld b,(hl)
		push hl
		ld a,b
		cp $FF
		jr z,cache_get__nold
		push de
		ld hl,tile_slot
		add hl,bc
		ld (hl),0
		pop de
cache_get__nold:		pop hl
		ld bc,(spr_t)
		ld (hl),b
		dec hl
		ld (hl),c
		pop hl
		ld a,e
		or $80
		ld (hl),a
		; upload: E = slot, spr_t = tile
		push de
		ld a,e
		srl a
		bit 0,e
		jr z,cache_get__u0
		or $80
cache_get__u0:		ld bc,$303B
		out (c),a
		ld hl,(spr_t)
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		ld de,$8000
		add hl,de		; Next tile definition
		ld c,$5B
		ld e,8
cache_get__r0:		outi
		outi
		outi
		outi
		xor a
		out (c),a
		out (c),a
		out (c),a
		out (c),a
		dec e
		jr nz,cache_get__r0
		ld e,8
		ld a,(vdp_regs+1)
		and 2
		jr z,cache_get__r2
cache_get__r1:		outi			; 8x16: the next tile below
		outi
		outi
		outi
		xor a
		out (c),a
		out (c),a
		out (c),a
		out (c),a
		dec e
		jr nz,cache_get__r1
		jr cache_get__ud
cache_get__r2:		xor a
		ld b,64
cache_get__r3:		out (c),a
		djnz cache_get__r3
cache_get__ud:		pop de
		ld a,e
		ret


fw3_end:
; assert fw3_end <= $2000, "fw3 overflows its page" (checked by tools/check-layout)
