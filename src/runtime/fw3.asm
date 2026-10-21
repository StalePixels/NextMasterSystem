; fw3.asm: the framework's third page (FW3_PAGE), mapped at $0000 (MMU0)
; only while the once-a-frame work runs (fw2_vbl maps it; restore_mmu puts
; the game's page back): the copper lists (normal, per-line H scroll from
; an overlay's RASTER routine, 224-line), keyboard, map rebuild, tile
; conversion, sprites, the transparent pixel value scans and their tables,
; and the overlay switches (fw2_switches, at game start from fw2_start).
; Nothing here may run from a handler, except tile_flush and tile_flushk
; through tflush2, and pic_ready3 through pic_ready (fw2.asm), which map
; this page and the vblank work's other slots for them.

;		org $0000  (section origin)
tm_mask:	ds 1024			; per SMS tile: 16-bit set of pixel values it uses,
					; 0 = not known (a tile uses at least one value)
bits16:		dw 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768

; ----------------------------------------------------------------------
; Transparent pixel value. The tilemap treats one 4-bit pixel value as
; transparent and shows the fallback colour, CRAM v, there; that is right
; for background-palette tiles but wrong for sprite-palette tiles that use
; v (they should show CRAM 16+v). Every 8 frames this collects the pixel
; values used by the tiles that the name table shows with the sprite
; palette, into tr_free (values they do not use); fallback2 (fw2.asm)
; picks v from it when no v has CRAM v = CRAM 16+v. Each tile counts once
; a pass: ps_seen holds, per tile, the pass that last took its values.
; ----------------------------------------------------------------------
pal_scan:
		ld a,(ps_gen)
		inc a
		jr nz,pal_scan__g
		ld hl,ps_seen		; pass numbers wrapped: none seen
		ld de,ps_seen+1
		ld bc,511
		ld (hl),0
		ldir
		ld a,1
pal_scan__g:		ld (ps_gen),a
		ld c,a			; C = this pass
		ld hl,0
		ld (ps_acc),hl		; values used
		ld hl,(nt_base)		; L = 0
		ld a,h
		add a,$40
		ld h,a			; name table in the shadow
		ld a,7			; 7 pages of 128 entries: 896
pal_scan__pg:		push af
		ld b,128
pal_scan__l:		inc l
		bit 3,(hl)		; high byte: sprite palette
		jr nz,pal_scan__sp
pal_scan__n:		inc l
		djnz pal_scan__l
		inc h
		pop af
		dec a
		jr nz,pal_scan__pg
		ld de,(ps_acc)
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
pal_scan__sp:		ld a,(hl)
		and 1
		add a,255&(ps_seen>>8)
		ld d,a
		dec l
		ld e,(hl)
		inc l			; DE = ps_seen + tile
		ld a,(de)
		cp c
		jr z,pal_scan__n		; taken in this pass already
		ld a,c
		ld (de),a
		push bc
		push hl
		ld a,d
		sub 255&(ps_seen>>8)
		ld b,a
		ld c,e
		call tile_mask
		ld a,(ps_acc)
		or l
		ld (ps_acc),a
		ld a,(ps_acc+1)
		or h
		ld (ps_acc+1),a
		pop hl
		pop bc
		jr pal_scan__n

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

; BC = tile -> HL = set of pixel values in its Next definition (cached in
; tm_mask). Keeps BC.
tile_mask:
		ld h,b
		ld l,c
		add hl,hl
		ld de,tm_mask
		add hl,de
		ld e,(hl)
		inc hl
		ld d,(hl)
		ld a,d
		or e
		jr z,tile_mask__new
		ex de,hl
		ret
tile_mask__new:		push hl			; its tm_mask entry + 1
		push bc
		ld h,b
		ld l,c
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		ld de,$8000
		add hl,de		; its definition: 32 bytes, 32-byte aligned
		ld de,0
		ld b,255&(nibm>>8)
tile_mask__c:		ld c,(hl)
		ld a,(bc)
		or e
		ld e,a
		inc b
		ld a,(bc)
		or d
		ld d,a
		dec b
		inc l
		ld c,(hl)
		ld a,(bc)
		or e
		ld e,a
		inc b
		ld a,(bc)
		or d
		ld d,a
		dec b
		inc l
		ld a,l
		and $1F
		jr nz,tile_mask__c
tile_mask__done:	pop bc
		pop hl
		ld (hl),d
		dec hl
		ld (hl),e
		ex de,hl
		ret


; ----------------------------------------------------------------------
; Copper. Normal list: three head slots (cop_head), then 5 instructions per
; line y:
;   [WAIT y,c | NOOP] [MOVE $6E,A8 | NOOP] [WAIT y,40] [MOVE $6E,M0]
;   [MOVE $31,V | NOOP]   (the 224-line wrap, for line y+1)
; then WAIT 200,0; MOVE $31,V+224; MOVE $6E,M0; HALT.
; c = h_sw (fw2 hscroll_set), 0 = none. A scroll change rewrites
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
		jr z,cop_update__sw
		push de			; E = V for cop_wrap; cop_switches uses DE
		call cop_switches
		pop de
cop_update__sw:		ld a,(cop_v)
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
cf_hk:		call cop_head		; hsplit: sg_head
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

; The switch pair of every line again for the new column A (0 = none): lines
; 16-191 with register 0 bit 6 (the locked rows have none), else 0-191.
; From one column to another only the first byte of each line's WAIT y,c
; changes, so only that byte is written (about 80 cycles a line, about 10
; lines in all; writing the pairs whole takes about 25). To or from no
; switch (column 0: the game has not written H yet) the pair is written
; whole: WAIT y,c; MOVE $6E,A8, or for no switch WAIT y,40; MOVE $6E,M0,
; which does the same as the line's next pair. The rewrite runs in the
; vertical blank work and must end before line 0, where the copper starts
; the list again.
cop_switches:
		ld d,a			; D = new column
		ld a,(cop_sw)
		ld e,a			; E = old column
		ld a,d
		ld (cop_sw),a
		ld a,(cop_mode)
		or a
		ld b,0
		jr z,cop_switches__b
		ld b,16
cop_switches__b:	push de
		ld e,b
		ld d,10
		mul d,e
		ld hl,6
		add hl,de		; HL = 2 * (3 + 5B): line B's first slot
		pop de
		ld a,d
		or a
		jr z,cop_switches__pair
		ld a,e
		or a
		jr z,cop_switches__pair
		ld a,d			; a column before and after: one byte a line
		add a,a
		or $80
		ld d,a			; D = the first byte of WAIT y,c
cs_end:		ld a,192		; hsplit: the line of segment 1 (sg_end)
		sub b
		ld c,a			; C = lines
cop_switches__one:	ld a,h
		or %11000000
		nextreg $62,a		; write index MSB, copper mode kept
cop_switches__ol:	ld a,l
		nextreg $61,a		; write index LSB (the MSB stays)
		ld a,d
		nextreg $60,a
		ld a,l
		add a,10
		ld l,a
		jr c,cop_switches__oc
		dec c
		jr nz,cop_switches__ol
		ret
cop_switches__oc:	inc h			; the MSB changes (the write may have carried into it)
		dec c
		jr nz,cop_switches__one
		ret
cop_switches__pair:	ld a,d			; E = the first byte of WAIT y,c, D = the map
		or a
		ld a,$80 + (END_H << 1)
		ld d,NR6E_M0
		jr z,cop_switches__p
		ld a,(cop_sw)
		add a,a
		or $80
		ld d,NR6E_A8
cop_switches__p:	ld e,a
cop_switches__pl:	ld a,l
		nextreg $61,a
		ld a,h
		or %11000000
		nextreg $62,a
		ld a,e
		nextreg $60,a		; WAIT y,c
		ld a,b
		nextreg $60,a
		nextreg $60,$6E		; MOVE $6E,map
		ld a,d
		nextreg $60,a
		ld a,l
		add a,10
		ld l,a
		jr nc,cop_switches__pn
		inc h
cop_switches__pn:	inc b
		ld a,b
		cp 192
		jr nz,cop_switches__pl
		ret

; ----------------------------------------------------------------------
; Mid-frame H scroll, with the hsplit switch (fw_flags bit 5). A line event
; split (Asterix's status bar, Choplifter's bands): a register 8 write in the
; picture moves the tilemap at once (hscroll_set__direct in fw2), so the
; lines still to come need the map switch column of the new H as well. The
; normal list is then a set of segments (sg_tab): segment 0 from line 0, with
; column cop_sw from the H the vertical blank work sees, and one more from
; each line where a mid-frame write comes, with that write's column. A write
; rewrites only the lines from the beam's line down to the next segment,
; where the game's next write in the frame comes again, and only when the
; column changes or the split moved. A segment whose write did not come in a
; frame is merged into the one above by sg_frame, so for one frame after a
; game stops a split the lines below it keep the old column.
; fw2_switches turns it on by pointing three calls elsewhere, so a game
; without the switch runs the same instructions as before: r8_hk in fw2
; (vdp_reg_w) at hs_reg8, also in fw2, which calls sg_write after hscroll_set;
; vb_cop in fw2 (the once-a-frame work) at sg_vbl; and cf_hk (cop_update's
; whole rebuild) at sg_head. cop_switches rewrites segment 0's lines only:
; the sg_ routines keep its line count's end (cs_end) at segment 1's line.
; ----------------------------------------------------------------------
SG_MAX		equ 8			; segments, segment 0 included
SG_TOL		equ 8			; lines a split may move from one frame to the next
sg_n:		db 1			; segments in the list
sg_tab:		db 0,0,0, 192		; per segment: first line, column (segment 0's is
		ds SG_MAX*3-1		; copied from cop_sw), 1 when its write came in
					; this frame; then 192

; The list rebuilt whole: one segment.
sg_head:	call sg_reset
		jp cop_head

; One segment again.
sg_reset:	ld a,1
		ld (sg_n),a
		ld a,192
		ld (sg_tab+3),a
		ld (cs_end+1),a
		ret

; Once a frame, in place of rast_frame (vb_cop): sg_frame, then rast_frame.
sg_vbl:		call sg_frame
		jp rast_frame

; hs_reg8 (fw2), with this page at $0000 in a handler, interrupts off,
; after hscroll_set: register 8 was written, h_sw is its column. Keeps IX.
sg_write:
		ld a,(vdp_regs+0)
		and $10
		ret z			; line interrupts off: hscroll_set leaves X to the copper
		ld a,(m224)
		ld hl,cop_mode
		or (hl)
		and $FD
		ret nz			; not the normal list (224 lines, lock right, raster, or not built)
		ld a,(cop_sw)
		or a
		ret z			; no switches in the list yet
		ld (sg_tab+1),a
		ld a,(h_sw)
		ld b,a			; B = column
		call cur_line
		cp 192
		ret nc			; vertical blank: h_sw takes it from line 0
		ld c,a			; C = the beam's line
		cp 16
		jr nc,sg_write__go
		ld a,(cop_mode)		; lines 0-15 of a lock top list have no switch,
		or a			; and with register 0 bit 6 X stays (hscroll_set)
		ret nz
		ld a,(vdp_regs+0)
		and $40
		ret nz
sg_write__go:		push ix
		call sg_wr
		pop ix
sg_end:		ld a,(sg_tab+3)
		ld (cs_end+1),a
		ret
sg_wr:		ld ix,sg_tab
		ld de,3
		ld l,0			; L = i, the segment that holds line C
sg_wr__f:		ld a,c
		cp (ix+3)		; the next segment's first line, 192 past the last
		jr c,sg_wr__fi
		add ix,de
		inc l
		jr sg_wr__f
sg_wr__fi:		ld a,l			; segment i's split again, up to SG_TOL lines later?
		or a
		jr z,sg_wr__nx
		ld a,c
		sub (ix+0)
		cp SG_TOL+1
		jr nc,sg_wr__nx
		ld a,(ix+2)
		or a
		jr z,sg_wr__k
sg_wr__nx:		ld a,(sg_n)		; or segment i+1's, up to SG_TOL lines earlier?
		dec a
		cp l
		jr z,sg_wr__new		; i is the last
		ld a,(ix+3)
		sub c
		cp SG_TOL+1
		jr nc,sg_wr__new
		ld a,(ix+5)
		or a
		jr nz,sg_wr__new
		add ix,de
		jr sg_wr__k
sg_wr__new:		ld a,(ix+1)		; a new split in segment i
		cp b
		ret z			; its lines have this column already
		ld a,(sg_n)
		cp SG_MAX
		ret nc			; no free segment: the lines keep their column
		inc a
		ld (sg_n),a
		sub l
		dec a			; old n - i: segments i+1 .. n-1 and the 192
		ld h,a
		add a,a
		add a,h
		push bc
		ld c,a
		ld b,0			; BC = their bytes
		push ix
		pop hl
		add hl,bc
		inc hl
		inc hl			; HL = the last byte to move
		ld d,h
		ld e,l
		inc de
		inc de
		inc de
		lddr			; one segment up
		pop bc
		ld de,3
		add ix,de		; IX = the new segment i+1
		ld (ix+0),c
		ld a,(ix-2)
		ld (ix+1),a		; segment i's column: no line changes yet
sg_wr__k:		ld (ix+2),1		; IX = segment k (k >= 1): its write came
		ld a,(ix+0)		; its split in the list now
		ld (ix+0),c
		sub c
		jr z,sg_wr__col
		jr c,sg_wr__down
		ld e,a			; earlier than in the list: lines C to the old split
		ld a,b
		cp (ix+1)
		jr nz,sg_wr__col	; sg_wr__col writes them with the rest
		ld a,(ix-2)
		cp b
		ret z
		ld a,b
		ld b,c
		ld c,e
		jr cop_wlines		; take this column
sg_wr__down:		neg			; later than in the list: the lines from the old
		push bc			; split to C take segment k-1's column
		ld e,a
		ld a,c
		sub e
		ld b,a
		ld c,e
		ld a,(ix-2)
		cp (ix+1)
		call nz,cop_wlines
		pop bc
sg_wr__col:		ld a,b
		cp (ix+1)
		ret z
		ld (ix+1),a
		ld a,(ix+3)		; the lines from C to the next split take the column
		sub c
		ld e,a
		ld a,b
		ld b,c
		ld c,e
; A = column (1-39), B = first line, C = lines (0-192): writes the first
; byte of WAIT y,c of each line, whose switch pair already has a switch, as
; cop_switches does. The copper keeps running. Uses A, C, DE, HL.
cop_wlines:
		inc c
		dec c
		ret z
		add a,a
		or $80
		push af
		ld e,b
		ld d,10
		mul d,e
		ld hl,6
		add hl,de		; HL = 2 * (3 + 5B): line B's first slot
		pop de			; D = the first byte of WAIT y,c
cop_wlines__one:	ld a,h
		or %11000000
		nextreg $62,a
cop_wlines__l:		ld a,l
		nextreg $61,a
		ld a,d
		nextreg $60,a
		ld a,l
		add a,10
		ld l,a
		jr c,cop_wlines__c
		dec c
		jr nz,cop_wlines__l
		ret
cop_wlines__c:		inc h
		dec c
		jr nz,cop_wlines__one
		ret

; Once a frame, before rast_frame and cop_update: a segment whose write did
; not come in the frame is merged into the one above it (its lines take that
; column).
sg_frame:
		ld a,(sg_n)
		cp 2
		ret c
		ld a,(m224)
		ld hl,cop_mode
		or (hl)
		and $FD
		jp nz,sg_reset
		ld a,(cop_sw)
		ld (sg_tab+1),a
		push ix
		push iy
		ld ix,sg_tab+3		; read
		ld iy,sg_tab+3		; write
		ld a,(sg_n)
		dec a
		ld b,a			; B = segments 1 .. n-1
		ld c,1			; C = segments kept
sg_frame__l:		ld a,(ix+2)
		or a
		jr z,sg_frame__drop
		ld (iy+2),0
		ld a,(ix+0)
		ld (iy+0),a
		ld a,(ix+1)
		ld (iy+1),a
		ld de,3
		add iy,de
		inc c
		jr sg_frame__nx
sg_frame__drop:		ld a,(iy-2)		; the column of the last segment kept
		cp (ix+1)
		jr z,sg_frame__nx
		push bc
		ld e,a
		ld b,(ix+0)
		ld a,(ix+3)		; the next segment's split (not yet moved down)
		sub b
		ld c,a
		ld a,e
		call cop_wlines
		pop bc
sg_frame__nx:		ld de,3
		add ix,de
		djnz sg_frame__l
		ld (iy+0),192
		ld a,c
		ld (sg_n),a
		pop iy
		pop ix
		jp sg_end

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
		ld (tw_cnt),a
		ld (tw_cnt+1),a
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

; tile_flush with tiles from cart ROM on (tilecache: fw2_switches points
; the vertical blank work and tflush2 here). When kn_block (fw2) has noted
; tiles from cart ROM, a tile with its kn_pages bit and no dirty_pages bit
; is copied from its converted page (TKC_PAGE in slot 6 for the tables,
; the converted page there for the copy); the rest are converted from the
; shadow as above.
tile_flushk:
		ld a,(kn_any)
		or a
		jp z,tile_flush
		xor a
		ld (kn_any),a
		ld (tiles_dirty),a
		ld (tw_cnt),a
		ld (tw_cnt+1),a
		nextreg $56,TKC_PAGE
		ld hl,dirty_pages
		ld b,64
tile_flushk__l:	ld e,l
		ld d,255&(KN_PAGES>>8)
		ld a,(de)
		ld c,a			; known
		or (hl)
		jr z,tile_flushk__n
		ld (cv_mask),a
		ld a,(hl)
		cpl
		and c
		ld (cv_ko),a		; known and not written since
		xor a
		ld (de),a
		ld (hl),a
		push hl
		push bc
		ld a,l
		sub 255&(dirty_pages)
		call conv_pagek
		pop bc
		pop hl
tile_flushk__n:	inc l
		djnz tile_flushk__l
		ld a,(cur_mmu+6)
		nextreg $56,a
		ret

; A = VRAM page (0-63), cv_mask = its tiles to convert or copy, cv_ko =
; those of them to copy from their converted page
conv_pagek:
		ld c,a
		ld a,(cv_ko)
		or a
		ld a,c
		jp z,conv_page
		ld (cv_page),a
		add a,$40
		ld iyh,a
		ld iyl,0
		ld a,(cv_page)
		add a,$80
		ld ixh,a
		ld ixl,0
		ld a,(cv_mask)
convk__tile:	ld (cv_m),a
		ld hl,cv_ko
		srl (hl)
		jr c,convk__copy
		rra
		jr c,convk__conv
		ld bc,32
		add ix,bc
		add iy,bc
		jp convk__next
convk__conv:	ld a,8
convk__row:	ld (cv_n),a
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
		jr nz,convk__row
		jp convk__next
convk__copy:	ld a,(cv_page)		; HL = TK_PG + tile (cv_page * 8 + IXL / 32)
		ld b,a
		add a,a
		add a,a
		add a,a
		ld l,a
		ld a,ixl
		rlca
		rlca
		rlca
		and 7
		or l
		ld l,a
		ld a,b
		rlca
		rlca
		rlca
		and 1
		add a,255&(TK_PG>>8)
		ld h,a
		ld a,(hl)		; the converted page
		inc h
		inc h
		ld e,(hl)
		inc h
		inc h
		ld d,(hl)		; the tile's address there, in slot 6
		nextreg $56,a
		ex de,hl
		push ix
		pop de
		rept 32
		ldi
		endr
		nextreg $56,TKC_PAGE
		push de
		pop ix
		ld bc,32
		add iy,bc
convk__next:	ld a,(cv_m)
		srl a
		jp nz,convk__tile
		jp conv_page__bk

cv_ko:		db 0

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
conv_page__bk:	; drop the pixel value sets and cached patterns of those tiles
		ld a,(cv_page)
		ld l,a
		ld h,0
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		ld de,tm_mask
		add hl,de		; the page's 8 tm_mask entries
		ld a,(cv_mask)
		ld b,8
conv_page__v:		rra
		jr nc,conv_page__vn
		ld (hl),0
		inc hl
		ld (hl),0
		dec hl
conv_page__vn:		inc hl
		inc hl
		djnz conv_page__v
		ld a,(cv_page)
		ld e,a
		ld d,0
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
		ld c,a			; an odd tile also drops its even partner: in
		srl a			; 8x16 mode the pattern cached for the even
		and $55			; tile holds the odd tile as its lower half
		or c
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


; ----------------------------------------------------------------------
; Per-line H scroll from an overlay hook (rastercode). A game that writes
; register 8 from a line interrupt on (nearly) every line cannot have its
; interrupts delivered on the Next: one costs more than a line. Its overlay
; brings a small routine that works out, from the game's RAM and registers,
; the register 8 value of every line, as the game's line interrupt handler
; would set it. Called once a frame: rast_hook with HL = hl_tab (192 bytes)
; and IX = vdp_regs, game RAM at $C000; carry set = the table is valid this
; frame. While it is (hl_on), the game gets no line interrupts, register 8
; writes go nowhere but vdp_regs, and the copper list is rebuilt from the
; table every frame (cop_raster).
; ----------------------------------------------------------------------
rast_frame:
		ld hl,(rast_hook)
		ld a,h
		or l
		ret z
		ld (rast_frame__c+1),hl
		ld hl,hl_tab
		ld ix,vdp_regs
		or a
rast_frame__c:		call 0
		ld a,0
		adc a,a			; 1 when the table is valid
		ld hl,hl_on
		cp (hl)
		ld (hl),a
		jr z,rast_frame__same
		or a
rf_new:		jp nz,cop_raster	; rastseg: seg_new (fw2_switches)
		; back to the normal list: rebuilt in full, X from register 8
		ld a,$FF
		ld (cop_mode),a
		ld (cop_sw),a
		ld a,1
		ld (cop_dirty),a
		ld a,(vdp_regs+8)
		ld e,a
		jp hscroll_set
rast_frame__same:		or a
		ret z
rf_inc:		jp cop_raster__inc	; rastseg: seg_inc (fw2_switches)
; The copper list from hl_tab, in fixed slots: a head of four MOVEs ($31
; V, $6E M0, $2F and $30 the X of line 0), then five instructions for each
; line y, at instruction 4 + 5y, and HALT after line 191:
;   K = -H > 64 (map switch):  WAIT y,c   MOVE $6E,A8  WAIT y,40  MOVE $6E,M0     MOVE $30,lo X(y+1)
;   no switch:                 MOVE $2F,hi X(y)  NOOP  WAIT y,40  MOVE $2F,hi X(y+1)  MOVE $30,lo X(y+1)
; (line 191: X(191) for X(y+1)). The MOVEs after WAIT y,40 and the first
; two slots of line y+1 when it has no switch all run in line y's
; horizontal blank. With a switch X(y) < 256, so hi X(y) is already right;
; hi X(y+1) can then differ only when line y+1 has no switch, and its
; first slot sets it. A line's slots depend only on H(y) and H(y+1), so
; from one frame to the next only the lines next to an H that changed are
; written (hl_prev holds the H of every line in the list). The list is
; written in full when the hook's table becomes valid. The copper keeps
; running while the list is rewritten: it restarts at the top of every
; frame, and the rewrite stays ahead of it.
cop_raster:
		ld a,1			; full
		jr cop_raster__go
cop_raster__inc:	xor a
cop_raster__go:	ld (rx_full),a
		ld a,$FF
		ld (cop_mode),a		; the normal list is gone
		ld a,(vdp_regs+0)
		and $40
		jr z,cop_raster__nl
		ld hl,hl_tab		; register 0 bit 6: lines 0-15 at H = 0
		ld b,16
cop_raster__lk:		ld (hl),0
		inc hl
		djnz cop_raster__lk
cop_raster__nl:		ld a,(rx_tabok)
		or a
		call z,rx_mktab
		nextreg $61,0
		nextreg $62,%11000000	; write index 0, copper running
		ld a,(vdp_regs+9)
		cp 224
		jr c,cop_raster__v
		sub 224
cop_raster__v:		add a,224
		ld c,a
		nextreg $60,$31
		ld a,c
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		ld a,(hl_tab)
		call h2x
		nextreg $60,$2F
		ld a,d
		nextreg $60,a
		nextreg $60,$30
		ld a,e
		nextreg $60,a
		xor a
		ld (rx_nexti),a		; the write index is at line 0
		ld bc,$243B		; the lines go through the NextReg ports
		ld a,$60
		out (c),a
		inc b			; BC = $253B: copper data
		ld a,(rx_full)
		or a
		jr z,cop_raster__scan0
		; full: every line, then HALT
		ld hl,hl_tab
cop_raster__fl:		ld a,(hl)
		inc h
		ld (hl),a		; hl_prev
		dec h
		call rx_line
		inc l
		ld a,l
		cp 192
		jr c,cop_raster__fl
		ld a,$FF
		out (c),a		; HALT
		out (c),a
		ret
		; incremental: lines max(y - 1, rx_nexti) to y for each y whose H changed
cop_raster__scan0:	ld hl,hl_tab
cop_raster__scan:	ld a,(hl)
		inc h
		cp (hl)
		jr nz,cop_raster__ch
		dec h
cop_raster__sn:		inc l
		ld a,l
		cp 192
		jr c,cop_raster__scan
		ret
cop_raster__ch:		ld (hl),a		; hl_prev
		dec h
		ld a,l
		or a
		jr z,cop_raster__s0
		dec a
cop_raster__s0:		ld e,a			; y - 1 (0 for line 0)
		ld a,(rx_nexti)
		cp e
		jr nc,cop_raster__s1
		ld a,e
cop_raster__s1:		push hl			; A = first line to write, L = y
		ld l,a
cop_raster__w:		ld a,(rx_nexti)
		cp l
		call nz,rx_at
		call rx_line
		pop de
		ld a,l
		cp e
		push de
		inc l
		jr c,cop_raster__w
		pop hl
		jr cop_raster__sn

; L = line: the copper write index to its slots (instruction 4 + 5L).
; BC = $253B, and back to that with $60 selected.
rx_at:		ld e,l
		ld d,10
		mul d,e
		ld a,e
		add a,8
		ld e,a
		adc a,d
		sub e
		ld d,a			; DE = 8 + 10L
		dec b
		ld a,$61
		out (c),a
		inc b
		out (c),e
		dec b
		ld a,$62
		out (c),a
		inc b
		ld a,d
		or %11000000		; the copper keeps running
		out (c),a
		dec b
		ld a,$60
		out (c),a
		inc b
		ret

; HL = hl_tab + y (hl_tab is page aligned, so L = y): line y's five
; slots at the write index, through BC = $253B with $60 selected. Keeps HL
; and BC; rx_nexti = y + 1.
rx_line:
		ld a,l
		inc a
		ld (rx_nexti),a
		ld e,(hl)		; H(y)
		ld d,255&(rx_tab>>8)	; DE = H(y)'s column in rx_tab
		ld a,(de)
		or a
		jr z,rx_line__nosw
		add a,a
		or $80
		out (c),a		; WAIT y,c
		out (c),l
		ld a,$6E		; MOVE $6E,A8
		out (c),a
		ld a,NR6E_A8
		out (c),a
		ld a,$80 + (END_H << 1)	; WAIT y,40
		out (c),a
		out (c),l
		ld a,$6E		; MOVE $6E,M0
		out (c),a
		ld a,NR6E_M0
		out (c),a
		call rx_next
		inc d
		jr rx_line__lo
rx_line__nosw:		ld a,$2F		; MOVE $2F,hi X(y)
		out (c),a
		inc d
		ld a,(de)
		out (c),a
		xor a			; NOOP
		out (c),a
		out (c),a
		ld a,$80 + (END_H << 1)	; WAIT y,40
		out (c),a
		out (c),l
		call rx_next
		ld a,$2F		; MOVE $2F,hi X(y+1)
		out (c),a
		ld a,(de)
		out (c),a
		inc d
rx_line__lo:		ld a,$30		; MOVE $30,lo X(y+1)
		out (c),a
		ld a,(de)
		out (c),a
		ret
; DE = H(y+1)'s hi X in rx_tab (line 191: H(191)'s)
rx_next:	ld a,l
		cp 191
		jr z,rx_next__e
		inc l
		ld e,(hl)
		dec l
		jr rx_next__t
rx_next__e:		ld e,(hl)
rx_next__t:		ld d,1+(255&(rx_tab>>8))
		ret

; rx_tab: three 256-byte tables indexed by the register 8 value H: the
; switch column, then hi X, then lo X (h2x)
rx_mktab:
		ld hl,rx_tab
rx_mktab__l:		ld a,l
		call h2x
		ld (hl),b
		inc h
		ld (hl),d
		inc h
		ld (hl),e
		dec h
		dec h
		inc l
		jr nz,rx_mktab__l
		ld a,1
		ld (rx_tabok),a
		ret

; A = register 8 value H -> DE = tilemap X offset (K - 34 mod 320, K = -H),
; B = copper column of the M0 -> A8 switch, 0 = none (as hscroll_set, fw2.asm)
h2x:		neg
		ld b,a			; K
		cp 34
		jr c,h2x__lo
		sub 34			; K >= 34: X = K - 34
		ld e,a
		ld d,0
		jr h2x__sw
h2x__lo:		add a,30		; K < 34: X = K + 286
		ld e,a
		ld d,1
h2x__sw:		ld a,b
		cp 65
		ld b,0
		ret c
		ld b,a
		ld a,32			; (288 - K) / 8; 288 - K < 256 here
		sub b
		rrca
		rrca
		rrca
		and $1F
		ld b,a
		ret

rx_full:	db 0
rx_nexti:	db 0			; line whose slots the copper write index is at
rx_tabok:	db 0

; ----------------------------------------------------------------------
; Sprite collision line, with the collline switch (fw_flags bit 6). The SMS
; raises the status collision bit at the first line where two sprites meet;
; the Next's sprite status (spr_coll) comes only from the once-a-frame work,
; after the picture. With the switch, fw2_switches points vb_spr (fw2) at
; cl_vbl and rs_hk (rd_status in fw.asm) at cl_rd: cl_scan works out that
; line from the sprite table once a frame (cl_line, a Next line), and a
; status read in the picture from that line on raises the bit (cl_read in
; fw4), once a picture. Without the switch both calls keep their targets.
; ----------------------------------------------------------------------
; The first line where the boxes of two sprites meet (8 or 16 lines high,
; 8 pixels wide, both doubled with zoom), from the sprite table in the VRAM
; copy at $4000: SMS line max(Y1, Y2) + 1 of the pair with the lowest one,
; as a Next line in cl_line (16 lower in 224-line mode, 0 for the 16 lines
; above it), $FF for none. A box is not the sprite's pixels: two sprites
; whose boxes meet only at transparent pixels count as a collision here.
; Pairs are taken only while their line can beat the best one so far.
cl_scan:	ld a,(vdp_regs+1)
		ld bc,$0808		; B = height, C = width
		bit 1,a
		jr z,cl_scan__h
		ld b,16
cl_scan__h:	rra
		jr nc,cl_scan__z
		sla b
		sla c
cl_scan__z:	ld a,b
		ld (cl_scan__hy+1),a
		ld (cl_scan__hn+1),a
		ld a,c
		ld (cl_scan__wx+1),a
		ld a,(sat_hi)
		add a,$40
		ld h,a
		ld l,0			; HL = Y of sprite 0
		ld a,(m224)
		or a
		ld a,64
		jr nz,cl_scan__n
		ld a,$D0		; 192-line mode: Y = $D0 ends the list
		ld bc,64
		cpir
		ld a,l
		jr nz,cl_scan__n
		dec a
cl_scan__n:	ld (cl_scan__ni+1),a
		ld (cl_scan__nj+1),a
		ld l,0
		ld e,$F0		; E = the best line so far (SMS), none
cl_scan__i:	ld a,l
cl_scan__ni:	cp 64
		jr nc,cl_scan__done
		ld a,(hl)
		inc a
		cp e
		jr nc,cl_scan__in	; no pair with this one beats E
		ld d,a			; D = its first line
		push hl
		ld a,l
		add a,a
		or $80
		ld l,a
		ld c,(hl)		; C = its X
		pop hl
		push hl
cl_scan__j:	inc l
		ld a,l
cl_scan__nj:	cp 64
		jr nc,cl_scan__je
		ld a,(hl)
		inc a
		sub d
		jr c,cl_scan__up
cl_scan__hy:	cp 8
		jr nc,cl_scan__j
		add a,d			; the line: the other one's first
		jr cl_scan__x
cl_scan__up:	neg
cl_scan__hn:	cp 8
		jr nc,cl_scan__j
		ld a,d			; the line: this one's first
cl_scan__x:	cp e
		jr nc,cl_scan__j
		ld b,a
		push hl
		ld a,l
		add a,a
		or $80
		ld l,a
		ld a,(hl)		; the other one's X
		pop hl
		sub c
		jr nc,cl_scan__wx
		neg
cl_scan__wx:	cp 8
		jr nc,cl_scan__j
		ld e,b			; a better pair
		jr cl_scan__j
cl_scan__je:	pop hl
cl_scan__in:	inc l
		jr cl_scan__i
cl_scan__done:	ld a,(m224)
		or a
		ld a,e
		jr z,cl_scan__192
		sub 16
		jr nc,cl_scan__192
		xor a			; the 16 lines above line 0: from line 0
cl_scan__192:	ld hl,pic_end
		cp (hl)
		jr c,cl_scan__set
		ld a,$FF
cl_scan__set:	ld (cl_line),a
		ret
		align 256
hl_tab:		ds 192			; H of every line, from the hook
; In place of spr_update: the sprite update without the Next's collision
; bit, then the bit for the picture just drawn if no status read in it
; raised it, then the line for the new table.
cl_vbl:		ld a,(vdp_status)
		push af
		call spr_update
		pop bc			; B = the status before
		ld hl,vdp_status
		res 5,(hl)
		ld a,b
		and $20
		or (hl)
		ld (hl),a
		ld a,(cl_arm)
		or a
		jr z,cl_vbl__arm
		ld a,(cl_line)
		inc a
		jr z,cl_vbl__arm	; no collision
		ld a,(vdp_regs+1)
		and $40
		jr z,cl_vbl__arm	; display off
		set 5,(hl)
cl_vbl__arm:	call cur_line		; run in the picture (workline): 2, armed from
		ld hl,pic_end		; the next picture on (cl_read)
		cp (hl)
		ld a,1
		jr nc,cl_vbl__a1
		inc a
cl_vbl__a1:	ld (cl_arm),a
		jp cl_scan
; (cl_vbl sits in the free bytes after hl_tab, cl_scan in those before it)
		align 256
hl_prev:	ds 192			; H of every line in the copper list
		align 256
rx_tab:		ds 768			; per H: column, hi X, lo X (rx_mktab)
nibm:		ds 512			; per byte of a tile definition: the set of its two
					; pixel values, low bytes then high bytes (fw2_init)
ps_seen:	ds 512			; per SMS tile: the pal_scan pass that took it last
ps_gen:		db 0			; pal_scan pass
ps_acc:		dw 0

; The copper list in 224-line mode: a head of one X, one Y (V - 16; the
; 32-row map wraps at 256 by itself), the map and the ULA on, then the map
; switch pair on each of the 224 lines (Next lines 0-207, then 16 lines for
; the 16 lines above line 0, from cop_top: the last 16 lines of the frame,
; 295-310 of the 311-line frame at 50 Hz and 248-263 of the 264-line frame
; at 60 Hz), with the ULA off in the 32 border lines, then HALT. As in the
; 192-line list, every line has a switch: for K = -H <= 64, and before the
; first H write, at column 39 (SMS x 312, past the picture's right edge).
; So the list is written whole only when it is not the 224-line list yet
; (cop_mode 3); after that an H or V write rewrites the head's three MOVEs,
; and a new column the first byte of each line's WAIT line,column (about 80
; cycles a line, against about 230 for the whole list). cop_sw stays $FF, so
; every H write marks the list (hscroll_set) and the head follows it.
; Per-line H scroll and the lock bits are not done here.
COP_TOP50	equ 295
COP_TOP60	equ 248
C224_L0		equ 10			; list byte of line 0's WAIT line,column
C224_L192	equ C224_L0+8*192+4	; line 192's, after the ULA-off pair
C224_TOP	equ C224_L192+8*16+8	; line cop_top's, after the ULA on and off pairs
cop_top:	dw COP_TOP50		; hz_setup
c224_w:		db 0			; the first byte of each WAIT line,column now (bit 8 apart)
cop_224:
		xor a
		ld (cop_dirty),a
		nextreg $61,0
		nextreg $62,%11000000
		ld a,(vdp_regs+9)
		add a,240
		ld c,a
		nextreg $60,$2F
		ld a,(h_x+1)
		nextreg $60,a
		nextreg $2F,a
		nextreg $60,$30
		ld a,(h_x)
		nextreg $60,a
		nextreg $30,a
		nextreg $60,$31
		ld a,c
		nextreg $60,a
		nextreg $31,a
		ld a,(h_sw)		; the switch column, 0 before the first H write
		or a
		jr nz,cop_224__c
		ld a,39
cop_224__c:	add a,a
		or $80
		ld d,a			; D = the first byte of WAIT line,column
		ld a,(cop_mode)
		cp 3
		jr nz,cop_224__full
		ld a,(c224_w)
		cp d
		ret z			; the list stands: only the head changed
		ld a,d
		ld (c224_w),a
		ld hl,C224_L0		; a new column: one byte a line
		ld b,192
		call cop_224__run
		ld hl,C224_L192
		ld b,16
		call cop_224__run
		ld a,(cop_top+1)
		or a
		ld a,(cop_top)
		jr z,cop_224__lo
		xor a
cop_224__lo:	neg			; E = lines of the 16 below line 256 (8 at 60 Hz)
		ld e,a
		ld hl,C224_TOP
		or a
		jr z,cop_224__hi
		ld b,a
		call cop_224__run
cop_224__hi:	ld a,16
		sub e
		ret z
		ld b,a
		inc d			; WAIT line bit 8
; B = lines from list byte HL, D = the byte: the first byte of each line's
; WAIT, 8 bytes apart. The copper keeps running.
cop_224__run:	ld a,h
		or %11000000
		nextreg $62,a		; write index MSB, copper mode kept
cop_224__rl:	ld a,l
		nextreg $61,a
		ld a,d
		nextreg $60,a
		ld a,l
		add a,8
		ld l,a
		jr c,cop_224__rc
		djnz cop_224__rl
		ret
cop_224__rc:	inc h
		djnz cop_224__run
		ret
cop_224__full:	ld a,3			; the whole list
		ld (cop_mode),a
		ld a,d
		ld (c224_w),a
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		nextreg $60,$68		; ULA on for lines 0-191 (its column 0 shows the backdrop)
		nextreg $60,0
		ld bc,0
cop_224__l1:		call cop_224__sw
		inc bc
		ld a,c
		cp 192
		jr nz,cop_224__l1
		call cop_224__uoff
cop_224__l1b:		call cop_224__sw
		inc bc
		ld a,c
		cp 208
		jr nz,cop_224__l1b
		call cop_224__uon
		ld bc,(cop_top)
		call cop_224__uoff
cop_224__l2:		call cop_224__sw
		inc bc
		ld a,c
cop_224__endl:	cp 255&(COP_TOP50+16)	; hz_setup
		jr nz,cop_224__l2
		nextreg $60,$FF		; HALT
		nextreg $60,$FF
		ret
; The 16 lines above and below the 192-line area are border to the ULA, and
; its border is opaque: tile pixels of the transparent value would show it
; (black) there instead of the fallback colour. The ULA is off in those
; lines (NextReg $68 bit 7); BC = line, keeps BC and D.
cop_224__uoff:		ld e,$80
		jr cop_224__u
cop_224__uon:		ld e,0
cop_224__u:		ld a,$80
		or b
		nextreg $60,a		; WAIT line,0
		ld a,c
		nextreg $60,a
		nextreg $60,$68
		ld a,e
		nextreg $60,a
		ret
cop_224__sw:		ld a,d			; BC = line, D = the first byte of WAIT line,column
		or b
		nextreg $60,a		; WAIT line,column
		ld a,c
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_A8
		ld a,$80 + (END_H << 1)
		or b
		nextreg $60,a		; WAIT line,40
		ld a,c
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		ret

; ----------------------------------------------------------------------
; Segment H scroll in 224-line mode, with the rastseg switch (fw_flags bit
; 7). The RASTER routine's table is then, in 224-line mode, a list of
; segments: pairs of (first SMS line, H), the lines rising, ended by a line
; of 224 or more (or one not above the one before), at most SG2_MAX; the
; first segment starts at line 0 whatever its line byte says. In 192-line
; mode the table is the per-line table, as without the switch.
; fw2_switches points rf_new and rf_inc (rast_frame) at seg_new and
; seg_inc; without the switch they keep their targets (cop_raster and
; cop_raster__inc).
; The list (cop_mode 4) is the 224-line list (cop_224) with an X for each
; segment: the head's X is that of line 16's segment (Next line 0); a
; segment that starts at another line has MOVE $2F, MOVE $30 after the
; switch pair of the line above it, in that line's horizontal blank; and
; the X of the segment of line 0 follows the ULA-on pair at Next line 208,
; for the 16 lines above line 0 at the end of the list. Each line's switch
; pair has its segment's column (39 for K <= 64). When the segments start
; at the same lines as the list's, only the head and the bytes of the
; segments whose H changed are written (the first byte of each WAIT
; line,column and the X of the MOVEs); else the list is written whole. The
; segment tables are kept in hl_prev, which cop_raster writes whole when it
; takes over from this list.
SG2_MAX		equ 32
SG2_L		equ hl_prev		; per segment: its first SMS line
SG2_H		equ hl_prev+32		; its H
SG2_P		equ hl_prev+64		; its H in the list
cs_n		equ hl_prev+96		; segments in the list
cs_full		equ hl_prev+97		; not 0: the list is written whole
cs_idx		equ hl_prev+98		; 2 bytes: the list byte the walk is at
cs_col		equ hl_prev+100		; the segment's first byte of WAIT line,column
cs_xh		equ hl_prev+101		; its X
cs_xl		equ hl_prev+102
cs_chg		equ hl_prev+103		; not 0: its H changed
cs_k		equ hl_prev+104		; the segment
cs_nx		equ hl_prev+105		; the next segment's first line, 224 for none
cs_mode		equ hl_prev+106		; cop_mode at the call
cs_s256		equ hl_prev+107		; the first of SMS lines 0-15 on Next line 256 or later

seg_new:	ld a,(m224)
		or a
		jp z,cop_raster
		jr cop_seg
seg_inc:	ld a,(m224)
		or a
		jr nz,cop_seg
		ld a,(cop_mode)
		cp 4
		jp z,cop_raster		; from the segment list: whole
		jp cop_raster__inc
; The list is written by cop_seg in part 4, mapped at $2000 in place of
; part 2 for the call: the once-a-frame work runs with interrupts off, and
; cop_seg uses only part 1 and this page. cop_mode is part 2's.
cop_seg:	ld a,(cop_mode)
		ld (cs_mode),a
		nextreg $51,FW4_PAGE
		call cop_seg4
		nextreg $51,FW2_PAGE
		ld a,4
		ld (cop_mode),a
		ret

; ----------------------------------------------------------------------
; Game start: the runtime state, the ULA clip and the tilemap X origin.
; Called by fw2_start with this page at $0000, before fw2_switches.
; ----------------------------------------------------------------------
fw2_state:
		call clip_update
		; framework state
		ld hl,vdp_regs
		ld b,16
fw2_state__zr:		ld (hl),0
		inc hl
		djnz fw2_state__zr
		ld a,192
		ld (pic_end),a
		ld a,$FF
		ld (vdp_regs+10),a
		ld (cop_sw),a
		ld (cop_v),a
		ld (cop_mode),a
		ld hl,$3800
		ld (nt_base),hl
		ld a,$3F
		ld (sat_hi),a
		call region_update
		ld hl,dirty_pages
		ld b,64
fw2_state__zd:		ld (hl),0
		inc l
		djnz fw2_state__zd
		xor a
		ld (kn_any),a
		ld a,(fw_flags)
		and 4
		jr z,fw2_state__nk
		nextreg $56,TKC_PAGE	; tilecache: no tiles from cart ROM noted (fw_start
		ld hl,KN_PAGES		; puts slot 6 back)
		ld b,64
fw2_state__zk:		ld (hl),0
		inc l
		djnz fw2_state__zk
fw2_state__nk:	xor a
		ld (tiles_dirty),a
		ld (vbl_done),a
		ld (vbl_poll),a
		ld (quit_req),a
		ld (pause_req),a
		ld (vdp_status),a
		ld (vdp_latch),a
		ld (h_sw),a
		ld (m224),a
		ld (hl_on),a		; no hook table from an earlier game
		inc a
		ld (sat_dirty),a
		ld (cop_dirty),a
		ld hl,0
		ld (fw_frames),hl
		dec hl
		ld (tr_free),hl
		ld a,$FF
		ld (bd_cur),a
		nextreg $1C,%00000100	; ULA clip: SMS column 0 only
		nextreg $1A,0
		nextreg $1A,PIC_X+7
		nextreg $1A,0
		nextreg $1A,191
		ld hl,286
		ld (h_x),hl
		ret

; ----------------------------------------------------------------------
; Overlay switches (fw_flags, from the overlay header): set the hooks in
; fw.asm on or off and the state they use. Called by fw2_start with this
; page at $0000, so a game loaded after another one starts clean.
; ----------------------------------------------------------------------
fw2_switches:
		ld a,(fw_flags)
		and 1
		ld hl,nt_put__hk
		ld de,pri_mark1
		call hook_set
		ld a,(fw_flags)
		and 1
		ld hl,nt_range__hk
		ld de,pri_markr
		call hook_set
		ld a,(fw_flags)
		and 1
		ld hl,vw_hk
		ld de,vw_pri
		call hook_set
		ld hl,vf_mode+1		; jt_vwrite's fast form: vf_prun before each run
		ld de,vf_mode+1
		ld a,(fw_flags)
		and 1
		jr z,fw2_switches__vf
		ld hl,vf_pj+1
		ld de,vf_prun
		ld (vf_mode+1),de
fw2_switches__vf:	ld (vf_pm+2),hl
		ld a,(fw_flags)
		and 2
		ld hl,fw_line_irq__hk1
		ld de,pal_vbl
		call hook_set
		ld a,(fw_flags)
		and 2
		ld hl,fw_line_irq__hk2
		ld de,pal_pic
		call hook_set
		ld a,(fw_flags)
		and 3
		ld a,$C9		; RET: no extra palette writes
		jr z,fw2_switches__c
		xor a			; NOP: cram_x writes them
fw2_switches__c:		ld (cram_hk),a
		; tilecache: vram_block ends in kn_entry, tile_flushk converts
		ld hl,tw_check
		ld de,tile_flush
		ld a,(fw_flags)
		and 4
		jr z,fw2_switches__k
		ld hl,kn_entry
		ld de,tile_flushk
fw2_switches__k:	ld (kn_hk+1),hl
		ld (tf_vbl+1),de
		ld (tf_tw+1),de
		; hsplit: three calls go to the sg_ routines (see sg_tab)
		call sg_reset
		ld hl,hscroll_set
		ld de,rast_frame
		ld bc,cop_head
		ld a,(fw_flags)
		and $20
		jr z,fw2_switches__h
		ld hl,hs_reg8
		ld de,sg_vbl
		ld bc,sg_head
fw2_switches__h:	ld (r8_hk+1),hl
		ld (vb_cop+1),de
		ld (cf_hk+1),bc
		; collline: vb_spr at cl_vbl, rs_hk at cl_rd (see cl_vbl)
		ld hl,spr_update
		ld de,cur_line
		ld a,(fw_flags)
		and $40
		jr z,fw2_switches__cl
		ld hl,cl_vbl
		ld de,cl_rd
fw2_switches__cl:	ld (vb_spr+1),hl
		ld (rs_hk+1),de
		ld a,$FF
		ld (cl_line),a
		; rastseg: rf_new and rf_inc at seg_new and seg_inc (see seg_new)
		ld hl,cop_raster
		ld de,cop_raster__inc
		ld a,(fw_flags)
		and $80
		jr z,fw2_switches__rs
		ld hl,seg_new
		ld de,seg_inc
fw2_switches__rs:	ld (rf_new+1),hl
		ld (rf_inc+1),de
		; Layer 2 (priority tiles): 256x192 from L2_BANK, above the sprites;
		; its transparent colour is one the SMS palette never makes
		ld a,(fw_flags)
		rra
		ld a,L2_TRANS
		ld b,4			; layer order L S U
		jr c,fw2_switches__p
		ld a,$E3		; the reset value
		ld b,0
fw2_switches__p:		nextreg $14,a
		ld a,b
		ld (lay15),a
		call l2_mode
		nextreg $16,254
		nextreg $17,0
		ld bc,$123B		; hidden until the display is on (l2_vis)
		xor a
		out (c),a
		ld (pri_redo),a
		ld (pri_ys),a
		ld (isr_sp),a		; no frame handler running, none held
		ld (isr_sp+1),a
		ld (irq_pend),a
		ld (line_held),a
		ld (dis_pend),a
		ld (dis_poll),a
		ld (disp_on),a
		ld (shadow_i),a
		ld (pal_vm),a
		ld (pal_vm+1),a
		ld (pal_vm+2),a
		ld (pal_vm+3),a
		ld hl,pri_lf		; pri_lf, pri_tiles, pri_chg
		ld de,pri_lf+1
		ld bc,192+64+64-1
		ld (hl),a
		ldir
		ld hl,cram_top
		ld b,32
fw2_switches__zt:		ld (hl),a
		inc hl
		djnz fw2_switches__zt
		inc a
		ld (pri_full),a
		ld (pal_ph),a
		ld a,254
		ld (pri_x),a
		ld a,%00000010
		ld (pal43),a
		ld (tm_ctl),a
		jp hz_setup

; The video rate. With CONF hz=50 or hz=60 (fw_flags bit 3, bit 4 set for
; 60) NextReg $05 bit 2 gets that rate; with hz=any the Next keeps the rate
; it booted at. The Next takes a new rate at its next frame and reads back
; the old one until then, so the rate here is the one written. The quit
; puts the shell's NextReg $05 back (nr_keep). Then the line numbers that
; depend on the rate: 50 Hz, a 311-line frame, the ULA interrupt at line
; 248 and the PAL V counter (vc50); 60 Hz, a 264-line frame, the ULA
; interrupt at line 224 and the NTSC V counter (vc60).
hz_setup:	ld bc,$243B
		ld a,$05
		out (c),a
		inc b
		in e,(c)		; NextReg $05
		ld a,(fw_flags)
		bit 3,a
		jr z,hz_setup__r	; hz=any
		res 2,e
		and $10
		jr z,hz_setup__w
		set 2,e
hz_setup__w:	ld a,e
		nextreg $05,a
hz_setup__r:	bit 2,e
		ld a,VBL_LINE
		ld hl,vc50
		ld de,COP_TOP50
		jr z,hz_setup__set
		ld a,224
		ld hl,vc60
		ld de,COP_TOP60
hz_setup__set:	ld (vbl_due__line+1),a
		ld (cop_top),de
		ld a,e
		add a,16
		ld (cop_224__endl+1),a
		ld a,(hl)
		ld (vc_fast__lim+1),a
		ld (vc_count__lim+1),a
		inc hl
		ld a,(hl)
		ld (vc_count__min+1),a
		inc hl
		ld a,(hl)
		ld (vc_count__sub+1),a
		ret

; The V counter's numbers for vc_count and vc_fast (fw.asm): the first line
; past the count's top, the line that the lines from the top up to it count
; as, and the jump back. 50 Hz, the PAL count: lines from 243 ($F3) count
; from $BC; the PAL SMS has 313 lines, so $BA and $BB are left out and the
; count reaches $FF on the last line, 310, which games wait for (Micro
; Machines). 60 Hz, the NTSC count: lines from 219 count from $D5; the
; Next's frame has 264 lines, the NTSC SMS 262, so lines 219-221 all count
; $D5 and the last line, 263, counts $FF.
vc50:		db $F3, 0, 55
vc60:		db $DB, 221, 8

; HL = hook (3 bytes), DE = routine: Z clear = CALL routine, Z set = NOPs
hook_set:	jr z,hook_set__off
		ld (hl),$CD
		inc hl
		ld (hl),e
		inc hl
		ld (hl),d
		ret
hook_set__off:		ld (hl),0
		inc hl
		ld (hl),0
		inc hl
		ld (hl),0
		ret

; pic_ready (fw2), after the tiles: the maps if the name table moved, then
; Layer 2's priority cells. pri_frame maps MAP_PAGE at $0000 for its work
; and this page back at its end.
pic_ready3:	ld a,(nt_dirty)
		or a
		call nz,map_rebuild
		jp pri_frame

fw3_end:
; assert fw3_end <= $2000, "fw3 overflows its page" (checked by tools/check-layout)
