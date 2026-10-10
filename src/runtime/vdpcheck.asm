; vdpcheck.asm: the trace build's VDP address check (make TRACE=1; fw.asm
; includes this file only then, and fw4.asm includes vdpcheck4.asm). Part 1
; holds the counters, which test tools read at tc_cnt, tc_ret, and the
; entries the runtime calls; each entry maps fw4 for its call (tc_far), and
; the checks and the records are there. It counts the interrupt handlers that
; change the VDP address while the game code they interrupted is in the
; middle of a VDP data stream.
;
; At each frame or line handler entry delivered to the game (irq_go,
; isr_tramp, fw_line_irq), tc_enter keeps a record of the VDP state
; (vdp_latch, vdp_code, vdp_addr) and of the handler's return address, and
; puts tc_ret in the return slot in its place. The handler's RET or RETI
; then goes to tc_ret, which compares the VDP state with the record and
; goes on to the return address. Records nest: a handler entered inside
; another one returns first. Game handlers often switch to a stack of their
; own, so the return slot is the only sure sign of the exit.
;
; The game is "in a stream" when the first control byte waits for its
; second, or when a data access followed the last completed control write
; (tc_dat).
;
; Counters (tc_cnt, 16 bits each, wrap):
;   tc_ent   handler entries recorded
;   tc_mid   of them, entries while the game was in a stream
;   tc_race  of those, handlers that left the VDP state changed
;   tc_bite  of those, the game then used the changed state: its next VDP
;            access found the state as the handler left it (no new address
;            set, by a control write or by page code writing vdp_addr), and
;            was a data access (the data went to the wrong place), or a
;            control write when the game had written the first control byte
;            before the handler and the handler left the latch clear (the
;            game's second byte became a first byte)
;   tc_ovf   entries not recorded, because TC_MAX records were open
; then, for the last bite, the address the handler returned to (tc_bpc) and
; the game's return address from the handler of the biting access
; (tc_bsite, fw_ret: just after the patched site).
;
; Limits: a game that reads or changes its handler's return address sees
; tc_ret there. A handler that never returns (it resets SP and jumps)
; leaves its record open; once TC_MAX are open, entries are not recorded.

TC_MAX		equ 8			; nested handler records
TC_REC		equ 7			; return address (2), latch, code, addr (2), in a stream

tc_cnt:
tc_ent:		dw 0
tc_mid:		dw 0
tc_race:	dw 0
tc_bite:	dw 0
tc_ovf:		dw 0
tc_bpc:		dw 0			; the last bite: where the handler returned to
tc_bsite:	dw 0			; and fw_ret of the access that bit
tc_rpc:		dw 0			; where the handler of the last race returned to

; A VDP data access (vdata_w, rd_vdata, vram_block, cram_block, fw_vwrite).
; Keeps every register.
tc_data:	push hl
		ld hl,tc_data4
		jr tc_far
; A VDP control write (vctrl_w). Keeps every register.
tc_ctrl:	push hl
		ld hl,tc_ctrl4
		jr tc_far
; The second control byte (vctrl_w__second). Keeps every register.
tc_setup:	push hl
		ld hl,tc_setup4
		jr tc_far
; A handler entry, interrupts off, HL = its return slot. Keeps every
; register.
tc_enter:	push hl
		ld hl,tc_enter4
; (SP) = the caller's HL, HL = a routine in fw4 that keeps every register:
; call it with fw4 in slot 1 and the caller's HL, then put back the page
; that slot 1 held, read from the NextReg (the caller can run with any
; page there). Interrupts off. Keeps every register.
tc_far:		ld (tc_far__c+1),hl
		push af
		push bc
		ld bc,$243B
		ld a,$51
		out (c),a
		inc b
		in a,(c)
		ld (tc_far__p+1),a
		pop bc
		pop af
		pop hl
		nextreg $51,FW4_PAGE
tc_far__c:	call 0
		push af
tc_far__p:	ld a,0
		nextreg $51,a
		pop af
		ret

; The handler returns here, with the game's registers and interrupt state.
; An interrupt taken before the DI nests a record of its own, which returns
; here first. tc_ret4 (fw4) closes the record and patches the jumps.
tc_ret:		push af
		ld a,i			; P/V = IFF2
		di
		push af
		call tc_retx
		pop af			; P/V = IFF2
		jp po,tc_ret__di
		pop af
		ei			; takes effect after the jump
tc_goei:	jp 0
tc_ret__di:	pop af
tc_go:		jp 0
tc_retx:	push hl
		ld hl,tc_ret4
		jr tc_far
