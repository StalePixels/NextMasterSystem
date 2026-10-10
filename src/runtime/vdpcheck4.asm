; vdpcheck4.asm: the trace build's VDP address check, its part in fw4
; (fw4.asm includes this file only in the trace build). vdpcheck.asm in
; part 1 describes the check and calls these through tc_far, with this page
; at $2000.

tc_n:		db 0			; open records
tc_dat:		db 0			; a data access since the last completed control write
tc_armed:	db 0			; a race: 1 the next VDP access decides tc_bite,
					; 2 the next control write is a bite
tc_rec:		ds TC_MAX*TC_REC
tc_rpcn:	dw 0			; the return address of the record being closed
tc_exit:	ds 4			; the VDP state the handler of the last race left

; HL -> (HL)++, 16 bits. Uses DE.
tc_inc:		ld e,(hl)
		inc hl
		ld d,(hl)
		inc de
		ld (hl),d
		dec hl
		ld (hl),e
		ret

; HL = the newest record (tc_n >= 1). Uses A, DE.
tc_top:		ld a,(tc_n)
		dec a
		ld e,a
		ld d,TC_REC
		mul d,e
		ld hl,tc_rec
		add hl,de
		ret

; A handler entry, interrupts off, HL = its return slot. Keeps every
; register.
tc_enter4:	push af
		push bc
		push de
		push hl
		ld hl,tc_ent
		call tc_inc
		ld a,(tc_n)
		cp TC_MAX
		jr c,tc_enter4__room
		ld hl,tc_ovf
		call tc_inc
		jr tc_enter4__x
tc_enter4__room:	inc a
		ld (tc_n),a
		call tc_top		; HL = the new record
		ex de,hl
		pop hl			; the slot
		push hl
		ld a,(hl)		; the return address into the record,
		ld (hl),255&(tc_ret)	; tc_ret into the slot
		ld (de),a
		inc hl
		inc de
		ld a,(hl)
		ld (hl),255&((tc_ret)>>8)
		ld (de),a
		inc de
		ld hl,vdp_latch		; latch, code, addr
		ld bc,4
		ldir
		ld a,(vdp_latch)	; in a stream?
		ld hl,tc_dat
		or (hl)
		ld (de),a
		jr z,tc_enter4__s
		ld hl,tc_mid
		call tc_inc
tc_enter4__s:	pop hl			; a frame entry's slot: what frm_run expects
		push hl			; there is now tc_ret
		ld de,(isr_sp)
		or a
		sbc hl,de
		jr nz,tc_enter4__x
		ld hl,tc_ret
		ld (isr_ret),hl
tc_enter4__x:	pop hl
		pop de
		pop bc
		pop af
		ret

; tc_ret's work (vdpcheck.asm), through tc_far: close the newest record,
; put its return address in tc_go and tc_goei, and count a race.
tc_ret4:
		push bc
		push de
		push hl
		call tc_top		; the newest record
		ld e,(hl)
		inc hl
		ld d,(hl)		; DE = the return address
		inc hl
		ld (tc_go+1),de
		ld (tc_goei+1),de
		ld (tc_rpcn),de
		ld a,(tc_n)
		dec a
		ld (tc_n),a
		ld de,4
		push hl
		add hl,de
		ld a,(hl)		; in a stream
		pop hl
		or a
		jr z,tc_ret__x
		ld de,vdp_latch
		ld c,(hl)		; the latch at the entry
		ld b,4
tc_ret__cmp:	ld a,(de)
		cp (hl)
		jr nz,tc_ret__race
		inc hl
		inc de
		djnz tc_ret__cmp
		jr tc_ret__x
tc_ret__race:	ld hl,(tc_rpcn)
		ld (tc_rpc),hl
		ld hl,vdp_latch
		ld de,tc_exit
		ld bc,4
		ldir
		ld hl,tc_race
		call tc_inc
		ld a,(vdp_latch)	; first byte written before, latch clear now: 2
		cpl
		and c
		and 1
		inc a
		ld (tc_armed),a
tc_ret__x:	pop hl
		pop de
		pop bc
		ret

; A VDP access after a race: a bite when the state is still as the handler
; left it. Count it and note where. Uses A, B, DE, HL.
tc_bit:		ld hl,vdp_latch
		ld de,tc_exit
		ld b,4
tc_bit__cmp:	ld a,(de)
		cp (hl)
		ret nz			; the game set a new state first
		inc hl
		inc de
		djnz tc_bit__cmp
		ld hl,tc_bite
		call tc_inc
		ld hl,(tc_rpc)
		ld (tc_bpc),hl
		ld hl,(fw_ret)
		ld (tc_bsite),hl
		ret

; A VDP data access (vdata_w, rd_vdata, vram_block, cram_block). Keeps
; every register.
tc_data4:	push af
		ld a,1
		ld (tc_dat),a
		ld a,(tc_armed)
		or a
		jr z,tc_data__x
		xor a
		ld (tc_armed),a
		push bc
		push de
		push hl
		call tc_bit
		pop hl
		pop de
		pop bc
tc_data__x:	pop af
		ret

; A VDP control write (vctrl_w): a bite when the handler broke the latch,
; else the race no longer bites. Keeps every register.
tc_ctrl4:	push af
		ld a,(tc_armed)
		cp 2
		jr nz,tc_ctrl__x
		push bc
		push de
		push hl
		call tc_bit
		pop hl
		pop de
		pop bc
tc_ctrl__x:	xor a
		ld (tc_armed),a
		pop af
		ret

; The second control byte (vctrl_w__second): a new address or a register.
; Keeps every register.
tc_setup4:	push af
		xor a
		ld (tc_dat),a
		pop af
		ret
