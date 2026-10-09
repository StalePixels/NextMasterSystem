; trace.asm: one handler call for a run or a loop of output instructions.
; Included in fw.asm (resident page).
;
; A trace op ($18-$1F OUT (n),A, $C3 OUTI, $CB OUTD, $81+8r OUT (C),r;
; tools/tracedef.py) marks an output site whose neighbourhood holds more
; outputs: an unrolled run, OUTI / OUT (C),A pairs, or a loop. The handler
; copies the game's code from the site on (and back to the loop head
; when a jump goes back over the site) into a buffer, with each patched
; output turned into a call that appends its byte to TR_DBUF, and runs it
; with the game's registers. The copy is kept: up to TR_NC traces are
; found again by site address, the pages mapped there and the port
; classes; their code fills TR_CODE.. and all are dropped when it is full. Instructions are copied only from the set in
; trace_table (no memory writes, stack, calls or other I/O); the copy ends
; before the first one outside it, and leaves through m_exit with the
; game's PC there. Jumps inside the copied range become jumps inside the
; buffer; jumps out of it leave through m_exit. Every output in a trace
; goes to the site's port; the bytes are sent in one block (vram_block for
; VRAM data) when the buffer fills and at the exit.
;
; Limits: reads through (HL), (BC), (DE) of $E000-$FFFF see the framework,
; not the SMS RAM mirror. If the copy cannot be made the site runs as a
; single output.

TR_CODE		equ $FD18		; trace code: $FD18-$FEFD, after the two IM2
TR_CEND		equ $FEFE		; vectors in use
TR_BUDGET	equ 120			; most bytes of code for one trace
TR_NC		equ 16			; traces kept (cache entries)
TR_CE		equ 8			; bytes per cache entry
TR_DBUF		equ $FF00		; output bytes: $FF00-$FF6F
TR_DLIM		equ $70
TR_NT		equ 8			; jump targets and fixups kept
TK_SITE		equ 8
TRACE_OUTI	equ $C3
TRACE_OUTD	equ $CB

; variables: trvars.inc (in the page gap after tables.inc)
tr_tg		equ $FF70		; TR_NT jump targets: source address, buffer address
tr_fx		equ $FF90		; TR_NT fixups: buffer position, target source address
tr_cache:	ds TR_NC*TR_CE		; site, page at site, slot and page at the
					; end, code address (0 plain, 1-3 a run), key

; ----------------------------------------------------------------------
; Entry from ed_dispatch: A = trace op, fw_ret = site + 2.
; ----------------------------------------------------------------------
tr_start:
		ld (tr_op),a
		ld (tr_ix),ix
		ld hl,(fw_ret)
		dec hl
		dec hl
		ld (tr_S),hl
		ld a,(hl)
		ld (tr_rst),a
		xor a
		ld (tr_size),a
		ld (tr_flags),a
		ld (tr_ntg),a
		ld (tr_nfx),a
		ld (tr_loop),a
		ld (tr_nout),a
		ld hl,0			; no loop head yet
		ld (tr_back),hl
		call game_class
		ld (tr_gcls),a		; class of port C
		ld b,a
		ld a,(tr_op)		; key: the class, + $10 for a port C trace;
		sub $18			; an OUT (n),A trace takes no port C outputs,
		cp 8			; so C does not matter to it
		ld c,0
		jr c,tr_start__cls
		ld a,b
		ld c,$10
tr_start__cls:		ld (tr_class),a
		or c
		ld (tr_key),a
		; The cache knows this site: run its copy, or what was decided
		; for it (0 plain, 1 site by site, 2 OUTIs, 3 OUTDs as one block).
		call tr_lookup
		jr nz,tr_start__new
		ld hl,(tr_go+1)
		ld a,h
		or a
		jp nz,tr_start__run
		or l
		jp z,tr_plain
		push af
		call tr_rscan
		pop af
tr_start__mark:		dec a
		jp z,tr_runs
		dec a
		jp z,tr_outis
		jp tr_outds
tr_start__new:		; Patched outputs in a row with no loop jump after them are
		; done here (tr_outis, tr_runs); loops are copied and run.
		call tr_rscan
		ld a,6			; a loop jump within 6 instructions after the run?
		ld (tr_a),a
tr_start__la:		call tr_dec
		or a
		jr z,tr_start__nolp
		cp 3
		jr c,tr_start__la1
		cp TK_SITE
		jr z,tr_start__nolp
		cp 4			; JR cc
		jr z,tr_start__lp
		cp 5			; DJNZ
		jr z,tr_start__lp
		cp 7			; JP cc
		jr nz,tr_start__nolp
tr_start__lp:		ld hl,(tr_S)		; a loop when it jumps back to the site or before
		or a
		sbc hl,de
		jr nc,tr_start__compile
		jr tr_start__nolp
tr_start__la1:		ld a,b
		add hl,a
		ld a,(tr_a)
		dec a
		ld (tr_a),a
		jr nz,tr_start__la
tr_start__nolp:		ld a,(tr_nrun)		; a run with no loop: OUTIs or OUTDs as one
		cp 2			; block, others site by site (not cached:
		jr c,tr_start__compile		; the scan is cheap, the cache is small)
		ld a,(tr_allouti)
		inc a
		jr tr_start__mark
tr_start__compile:	; a cache entry and room for its code
		ld hl,(tr_aptr)
		ld de,TR_BUDGET
		add hl,de
		ld de,TR_CEND
		or a
		sbc hl,de
		call nc,tr_reset	; full: drop every trace
		call tr_alloc
		; forward from the site
		ld hl,(tr_S)
tr_start__fw:		call tr_dec
		call tr_take
		jr c,tr_start__fend
		ld a,(tr_k)
		cp 3
		jr c,tr_start__fnext
		cp TK_SITE
		jr z,tr_start__fsite
		; a jump, target DE. Back to the site or before it: the loop
		; closes here, the copy ends after it.
		push hl
		ld hl,(tr_S)
		or a
		sbc hl,de		; site - target
		pop hl
		jr c,tr_start__fwd
		ld a,1
		ld (tr_loop),a
		jr z,tr_start__fstop
		ld (tr_back),de
		jr tr_start__fstop
tr_start__fwd:		ld a,(tr_k)
		cp 3			; JR
		jr z,tr_start__fstop
		cp 6			; JP
		jr z,tr_start__fstop
tr_start__fsite:		ld a,(tr_nout)
		inc a
		ld (tr_nout),a
tr_start__fnext:		ld a,b
		add hl,a
		jr tr_start__fw
tr_start__fstop:		ld a,b
		add hl,a
tr_start__fend:		ld (tr_E),hl
		ld de,(tr_S)
		or a
		sbc hl,de
		jp z,tr_fail		; the site itself did not fit
		ld a,(tr_loop)		; no loop and fewer than 3 outputs: not
		or a			; worth a copy
		jr nz,tr_start__worth
		ld a,(tr_nout)
		cp 3
		jp c,tr_fail
tr_start__worth:
		; loop head: decode from it, it must reach the site
		ld hl,(tr_S)
		ld (tr_H),hl
		ld hl,(tr_back)
		ld a,h
		or l
		jr z,tr_start__emit
		ld a,(tr_size)
		ld (tr_keep),a
		ld a,(tr_flags)
		ld (tr_keep+1),a
		ld a,(tr_ntg)
		ld (tr_keep+2),a
tr_start__hd:		ld de,(tr_S)
		push hl
		or a
		sbc hl,de
		pop hl
		jr z,tr_start__hok
		jr nc,tr_start__hfail
		call tr_dec
		call tr_take
		jr c,tr_start__hfail
		ld a,(tr_k)
		cp 3
		jr z,tr_start__hfail
		cp 6
		jr z,tr_start__hfail
		ld a,b
		add hl,a
		jr tr_start__hd
tr_start__hfail:		ld a,(tr_keep)
		ld (tr_size),a
		ld a,(tr_keep+1)
		ld (tr_flags),a
		ld a,(tr_keep+2)
		ld (tr_ntg),a
		jr tr_start__emit
tr_start__hok:		ld hl,(tr_back)
		ld (tr_H),hl
tr_start__emit:		; ---- pass 2: write the trace code ----
		ld ix,(tr_aptr)
		ld hl,(tr_H)
tr_start__em:		ld de,(tr_E)
		push hl
		or a
		sbc hl,de
		pop hl
		jp z,tr_start__emend
		ld de,(tr_S)
		push hl
		or a
		sbc hl,de
		pop hl
		jr nz,tr_start__ns
		ld (tr_go+1),ix
tr_start__ns:		call tr_mark
		call tr_dec
		cp 3
		jp c,tr_start__copy
		cp TK_SITE
		jp z,tr_start__site
		; jump: A = kind, DE = target. Inside [H, E]?
		ld (tr_k),a
		push hl
		ld hl,(tr_H)
		ex de,hl		; HL = target, DE = H
		push hl
		or a
		sbc hl,de
		pop hl
		jr c,tr_start__ext
		ld de,(tr_E)
		push hl
		ex de,hl
		or a
		sbc hl,de		; E - target
		pop de			; DE = target
		jr c,tr_start__ext2
		; internal
		pop hl
		ld a,(tr_k)
		cp 5
		jr z,tr_start__idj
		ld c,$C3		; JR, JP
		cp 3
		jr z,tr_start__ij
		cp 6
		jr z,tr_start__ij
		ld a,(hl)		; JR cc / JP cc
		ld c,a
		cp $40
		jr nc,tr_start__ij
		add a,$A2		; JR cc -> JP cc
		ld c,a
tr_start__ij:		ld (ix+0),c
		inc ix
		call tr_fixup
		inc ix
		inc ix
		jp tr_start__next
tr_start__idj:		ld (ix+0),$10		; DJNZ +2; JR +3; JP target
		ld (ix+1),$02
		ld (ix+2),$18
		ld (ix+3),$03
		ld (ix+4),$C3
		ld bc,5
		add ix,bc
		call tr_fixup
		inc ix
		inc ix
		jr tr_start__next2
tr_start__ext:		ex de,hl		; DE = target
tr_start__ext2:		pop hl
		ld a,(tr_k)
		cp 3
		jr z,tr_start__xu
		cp 6
		jr z,tr_start__xu
		cp 5
		jr z,tr_start__xdj
		ld a,(hl)		; JR cc / JP cc: JP !cc over the exit
		cp $40
		jr nc,tr_start__xc
		add a,$A2
tr_start__xc:		xor 8
		ld (ix+0),a
		push ix
		pop bc
		push hl
		ld hl,8
		add hl,bc
		ld (ix+1),l
		ld (ix+2),h
		pop hl
		inc ix
		inc ix
		inc ix
		jr tr_start__xu
tr_start__xdj:		ld (ix+0),$10		; DJNZ +2; JR +5; exit to target
		ld (ix+1),$02
		ld (ix+2),$18
		ld (ix+3),$05
		inc ix
		inc ix
		inc ix
		inc ix
tr_start__xu:		call tr_exitstub
		jr tr_start__next2
tr_start__copy:		; B bytes as they are
		push hl
tr_start__cp:		ld a,(hl)
		ld (ix+0),a
		inc hl
		inc ix
		djnz tr_start__cp
		pop hl
		jr tr_start__next2
tr_start__next:
tr_start__next2:		call tr_dec		; B = length again
		ld a,b
		add hl,a
		jp tr_start__em
tr_start__site:		; E = op
		ld a,e
		ld bc,m_outa
		cp 8
		jr c,tr_start__s3
		sub $18
		cp 8
		jr c,tr_start__s3
		ld a,e
		ld bc,m_outi
		cp $A3
		jr z,tr_start__s3
		cp TRACE_OUTI
		jr z,tr_start__s3
		ld bc,m_outd
		cp $AB
		jr z,tr_start__s3
		cp TRACE_OUTD
		jr z,tr_start__s3
		rrca			; OUT (C),r: r = (op >> 3) & 7
		rrca
		rrca
		and 7
		ld bc,m_outa
		cp 7
		jr z,tr_start__s3
		ld (ix+0),$08		; EX AF,AF'
		ld c,$AF		; r = 6: XOR A (OUT (C),0)
		cp 6
		jr z,tr_start__s6
		add a,$78		; LD A,r
		ld c,a
tr_start__s6:		ld (ix+1),c
		inc ix
		inc ix
		ld bc,tr_put
		call tr_call
		ld (ix+0),$08
		inc ix
		jr tr_start__next2
tr_start__s3:		call tr_call
		jr tr_start__next2
tr_start__emend:		call tr_mark
		ld de,(tr_E)
		call tr_exitstub
		; resolve the fixups
		ld a,(tr_nfx)
		or a
		jr z,tr_start__store
		ld b,a
		ld hl,tr_fx
tr_start__fx:		push bc
		ld c,(hl)		; position
		inc hl
		ld b,(hl)
		inc hl
		ld e,(hl)		; target source
		inc hl
		ld d,(hl)
		inc hl
		push hl
		push bc
		call tr_find		; HL = buffer address, Z if not found
		pop bc
		jr z,tr_start__fxbad
		ld a,l
		ld (bc),a
		inc bc
		ld a,h
		ld (bc),a
		pop hl
		pop bc
		djnz tr_start__fx
tr_start__store:		ld (tr_aptr),ix
		ld de,(tr_go+1)
		call tr_store
		jr tr_start__run
tr_start__fxbad:		pop hl
		pop bc
		jp tr_fail
tr_start__run:		; ---- run it with the game's registers ----
		push iy
		ex af,af'
		push af
		ex af,af'
		ld (tr_spsv),sp
		ld iy,TR_DBUF
		ld bc,(G_C)
		ld de,(G_E)
		ld sp,(fw_sp)
		pop af
		pop hl
		ld sp,(tr_spsv)
tr_go:		jp 0

; The next cache entry (round robin) into tr_idx, invalid until stored
tr_alloc:	ld a,(tr_rr)
		ld (tr_idx),a
		inc a
		and TR_NC-1
		ld (tr_rr),a
		ld a,(tr_idx)
		call tr_entry
		ld (hl),0
		inc hl
		ld (hl),0
		ret

; Patched sites in a row from the site: tr_nrun, tr_allouti (1 all OUTI,
; 2 all OUTD, 0 other);
; HL = the first byte after them
tr_rscan:	ld hl,(tr_S)
		ld bc,$0003		; B = sites, C: bit 0 all OUTI, bit 1 all OUTD
tr_rscan__rs:		inc hl
		ld a,(hl)
		cp $A3
		jr z,tr_rscan__oi
		cp TRACE_OUTI
		jr z,tr_rscan__oi
		cp $AB
		jr z,tr_rscan__od
		cp TRACE_OUTD
		jr z,tr_rscan__od
		ld c,0
		jr tr_rscan__rs1
tr_rscan__oi:		res 1,c
		jr tr_rscan__rs1
tr_rscan__od:		res 0,c
tr_rscan__rs1:		inc hl
		inc b
		ld a,b
		cp 255
		jr z,tr_rscan__rs2
		ld a,(tr_rst)
		cp (hl)
		jr z,tr_rscan__rs
tr_rscan__rs2:		ld a,b
		ld (tr_nrun),a
		ld a,c
		ld (tr_allouti),a
		ret

; The trace cannot be copied: remember that, run the site plain.
tr_fail:	ld a,(tr_nrun)		; a run: done in one call
		cp 2
		jr nc,tr_fail__run
		ld de,0
		call tr_store
		jp tr_plain
tr_fail__run:		ld a,(tr_allouti)
		inc a
		ld e,a
		ld d,0
		push de
		call tr_store
		pop de
		ld a,e
		jp tr_start__mark

; A = cache entry -> HL = its address
tr_entry:	ld e,a
		ld d,TR_CE
		mul d,e
		ld hl,tr_cache
		add hl,de
		ret

; A = MMU slot -> A = the game's page there
tr_page:	push hl
		ld hl,cur_mmu
		add hl,a
		ld a,(hl)
		pop hl
		ret

; DE = code address (0 = plain): fill cache entry tr_idx for this site
tr_store:	push de
		ld a,(tr_idx)
		call tr_entry
		ld de,(tr_S)
		ld (hl),e
		inc hl
		ld (hl),d
		inc hl
		ld a,d
		rlca
		rlca
		rlca
		and 7
		call tr_page
		ld (hl),a
		inc hl
		ld de,(tr_E)
		dec de
		ld a,d
		rlca
		rlca
		rlca
		and 7
		ld (hl),a
		inc hl
		call tr_page
		ld (hl),a
		inc hl
		pop de
		ld (hl),e
		inc hl
		ld (hl),d
		inc hl
		ld a,(tr_key)
		ld (hl),a
		ret

; Drop every cached trace (a new game, or the code area is full)
tr_reset:	ld hl,tr_cache
		ld b,TR_NC*TR_CE
tr_reset__z:		ld (hl),0
		inc hl
		djnz tr_reset__z
		ld hl,TR_CODE
		ld (tr_aptr),hl
		ret

; A cached trace for this site and these pages? Z: yes, tr_go set.
tr_lookup:	ld hl,tr_cache
		ld b,TR_NC
tr_lookup__l:		ld de,(tr_S)
		ld a,(hl)
		cp e
		jr nz,tr_lookup__n
		inc hl
		ld a,(hl)
		dec hl
		cp d
		jr nz,tr_lookup__n
		push hl
		inc hl
		inc hl
		ld a,d
		rlca
		rlca
		rlca
		and 7
		call tr_page
		cp (hl)
		jr nz,tr_lookup__np
		inc hl
		ld a,(hl)
		call tr_page
		inc hl
		cp (hl)
		jr nz,tr_lookup__np
		inc hl
		ld e,(hl)
		inc hl
		ld d,(hl)
		inc hl
		ld a,(tr_key)
		cp (hl)
		jr nz,tr_lookup__np
		ld (tr_go+1),de
		pop hl
		xor a
		ret
tr_lookup__np:		pop hl
tr_lookup__n:		ld de,TR_CE
		add hl,de
		djnz tr_lookup__l
		or 1
		ret

; BC = routine: write CALL BC at IX
tr_call:	ld (ix+0),$CD
		ld (ix+1),c
		ld (ix+2),b
		inc ix
		inc ix
		inc ix
		ret

; DE = game PC: write CALL m_exit; DW DE at IX
tr_exitstub:	ld bc,m_exit
		call tr_call
		ld (ix+0),e
		ld (ix+1),d
		inc ix
		inc ix
		ret

; DE = target source address: fixup at IX (2 bytes)
tr_fixup:	push hl
		ld a,(tr_nfx)
		inc a
		ld (tr_nfx),a
		dec a
		add a,a
		add a,a
		ld hl,tr_fx
		add hl,a
		push ix
		pop bc
		ld (hl),c
		inc hl
		ld (hl),b
		inc hl
		ld (hl),e
		inc hl
		ld (hl),d
		pop hl
		ret

; HL = source address: every target entry for it gets the buffer address IX
tr_mark:	ld a,(tr_ntg)
		or a
		ret z
		push hl
		push bc
		push de
		ex de,hl		; DE = address
		ld b,a
		ld hl,tr_tg
tr_mark__l:		ld a,(hl)
		inc hl
		cp e
		jr nz,tr_mark__n1
		ld a,(hl)
		cp d
		jr nz,tr_mark__n1
		inc hl
		ld a,ixl
		ld (hl),a
		inc hl
		ld a,ixh
		ld (hl),a
		inc hl
		jr tr_mark__n
tr_mark__n1:		inc hl
		inc hl
		inc hl
tr_mark__n:		djnz tr_mark__l
		pop de
		pop bc
		pop hl
		ret

; DE = target source address -> HL = its buffer address; Z if none
tr_find:	ld a,(tr_ntg)
		or a
		ret z
		ld b,a
		ld hl,tr_tg
tr_find__l:		ld a,(hl)
		inc hl
		cp e
		jr nz,tr_find__n
		ld a,(hl)
		cp d
		jr nz,tr_find__n
		inc hl
		ld a,(hl)
		inc hl
		ld h,(hl)
		ld l,a
		or h
		ret nz
		ret
tr_find__n:		inc hl
		inc hl
		inc hl
		djnz tr_find__l
		xor a
		ret

; ----------------------------------------------------------------------
; HL = game address: decode one instruction.
; A = kind (0 not allowed, 1 copy, 2 CB copy, 3 JR, 4 JR cc, 5 DJNZ, 6 JP,
; 7 JP cc, 8 patched output site), B = length, C = worst-case code bytes,
; DE = jump target, or E = the site's op. tr_wc, tr_co set.
; ----------------------------------------------------------------------
tr_dec:
		xor a
		ld (tr_wc),a
		ld (tr_co),a
		ld a,(tr_rst)
		cp (hl)
		jr z,tr_dec__site
		ld e,(hl)
		ld d,255&((trace_table)>>8)
		ld a,(de)
		or a
		ret z
		ld c,a
		and 3
		ld b,a
		bit 7,c
		jr z,tr_dec__nwc
		ld a,1
		ld (tr_wc),a
tr_dec__nwc:		ld a,c
		rrca
		rrca
		and 7
		cp 2
		jr z,tr_dec__cb
		cp 3
		jr nc,tr_dec__jump
		ld c,b
		ret			; A = 1
tr_dec__cb:		inc hl
		ld e,(hl)
		dec hl
		ld a,e
		and 7
		cp 6
		jr z,tr_dec__bad
		cp 1
		jr nz,tr_dec__cbok
		ld a,e
		and $C0
		cp $40
		jr z,tr_dec__cbok		; BIT b,C does not write C
		ld a,1
		ld (tr_wc),a
tr_dec__cbok:		ld a,2
		ld c,a
		ret
tr_dec__bad:		xor a
		ret
tr_dec__jump:		push af
		cp 6
		jr nc,tr_dec__abs
		inc hl			; relative: HL + 2 + e
		ld a,(hl)
		dec hl
		ld e,a
		rlca
		sbc a,a
		ld d,a
		push hl
		add hl,de
		inc hl
		inc hl
		ex de,hl
		pop hl
		jr tr_dec__size
tr_dec__abs:		inc hl
		ld e,(hl)
		inc hl
		ld d,(hl)
		dec hl
		dec hl
tr_dec__size:		pop af
		ld c,5
		cp 3
		ret z
		cp 6
		ret z
		ld c,9
		cp 5
		ret z
		ld c,8
		ret
tr_dec__site:		inc hl
		ld e,(hl)
		dec hl
		ld b,2
		ld c,3
		ld a,e
		cp 8
		jr c,tr_dec__sok
		sub $18
		cp 8
		jr c,tr_dec__sok
		ld a,e
		cp $A3
		jr z,tr_dec__sc
		cp TRACE_OUTI
		jr z,tr_dec__sc
		cp $AB
		jr z,tr_dec__sc
		cp TRACE_OUTD
		jr z,tr_dec__sc
		and $C7
		cp $41
		jr z,tr_dec__sr
		cp $81
		jr nz,tr_dec__bad
tr_dec__sr:		ld a,e
		and $38
		cp $38
		jr z,tr_dec__sc		; OUT (C),A
		ld c,6
tr_dec__sc:		ld a,1
		ld (tr_co),a
tr_dec__sok:		ld a,TK_SITE
		ret

; After tr_dec: may the instruction join the trace? Carry set: no.
; Keeps HL, B, DE; updates size, flags and the target list.
tr_take:
		or a
		scf
		ret z
		ld (tr_k),a
		ld a,(tr_size)
		add a,c
		ret c
		cp TR_BUDGET-5+1	; room for it and the end stub
		ccf
		ret c
		ld c,a			; new size
		ld a,(tr_k)
		cp TK_SITE
		jr z,tr_take__site
		cp 3
		jr c,tr_take__wc
		ld a,(tr_ntg)		; a jump: room for its target?
		cp TR_NT
		ccf
		ret c
tr_take__wc:		ld a,(tr_wc)
		or a
		jr z,tr_take__tg
		ld a,(tr_flags)
		bit 0,a
		scf
		ret nz			; C-port outputs and C written: stop
		or 2
		ld (tr_flags),a
tr_take__tg:		ld a,(tr_k)
		cp 3
		jr c,tr_take__ok
		push hl
		ld a,(tr_ntg)
		inc a
		ld (tr_ntg),a
		dec a
		add a,a
		add a,a
		ld hl,tr_tg
		add hl,a
		ld (hl),e
		inc hl
		ld (hl),d
		inc hl
		ld (hl),0
		inc hl
		ld (hl),0
		pop hl
		jr tr_take__ok
tr_take__site:		ld a,(tr_co)
		or a
		jr nz,tr_take__csite
		ld a,e			; OUT (n),A: its class must be the trace's
		and 7
		push hl
		ld hl,tr_class
		cp (hl)
		pop hl
		scf
		ret nz
		jr tr_take__ok
tr_take__csite:		ld a,(tr_key)		; port C output: only in a port C trace
		and $10
		scf
		ret z
		ld a,(tr_flags)
		bit 1,a
		scf
		ret nz			; C written: its port is unknown
		or 1
		ld (tr_flags),a
tr_take__ok:		ld a,c
		ld (tr_size),a
		or a
		ret

; A run of patched outputs, done here one by one into TR_DBUF and sent
; at the end. It stops before an output to another port class.
; DE = game HL, HL = code, B = sites left, C = 1 once an OUTI/OUTD ran.
tr_runs:
		push iy
		ld iy,TR_DBUF
		ld a,(tr_gcls)
		ld b,a
		ld a,(tr_class)
		cp b
		ld a,1
		jr z,tr_runs__ck
		xor a
tr_runs__ck:		ld (tr_cok),a
		call game_hl
		ex de,hl
		ld hl,(tr_S)
		ld a,(tr_nrun)
		ld b,a
		ld c,0
tr_runs__l:		ld (tr_pc),hl
		inc hl
		ld a,(hl)
		inc hl
		cp $A3
		jr z,tr_runs__outi
		cp TRACE_OUTI
		jr z,tr_runs__outi
		cp 8
		jr c,tr_runs__n
		sub $18
		cp 8
		jr c,tr_runs__n
		add a,$18
		cp $AB
		jr z,tr_runs__outd
		cp TRACE_OUTD
		jr z,tr_runs__outd
		push af
		and $C7
		cp $41
		jr z,tr_runs__ocr
		cp $81
		jr z,tr_runs__ocr
		pop af
		jr tr_runs__stop
tr_runs__ocr:		ld a,(tr_cok)
		or a
		jr z,tr_runs__stopp
		pop af
		rrca
		rrca
		rrca
		and 7
		cp 7
		jr z,tr_runs__a
		cp 6
		jr z,tr_runs__zero
		cp 4
		jr c,tr_runs__reg
		ld a,d			; H
		jr z,tr_runs__put
		ld a,e			; L
		jr tr_runs__put
tr_runs__zero:		xor a
		jr tr_runs__put
tr_runs__reg:		push hl
		call reg_addr
		ld a,(hl)
		pop hl
		jr tr_runs__put
tr_runs__n:		push hl			; OUT (n),A: class A must be the trace's
		ld hl,tr_class
		cp (hl)
		pop hl
		jr nz,tr_runs__stop
tr_runs__a:		ld a,(game_a)
tr_runs__put:		ld (iy+0),a
		inc iy
		ld a,iyl
		cp TR_DLIM
		call nc,tr_runs__fl
		djnz tr_runs__l
		jr tr_runs__end
tr_runs__outi:		ld a,(tr_cok)
		or a
		jr z,tr_runs__stop
		ld a,(de)
		inc de
		jr tr_runs__bdec
tr_runs__outd:		ld a,(tr_cok)
		or a
		jr z,tr_runs__stop
		ld a,(de)
		dec de
tr_runs__bdec:		ld c,1
		push hl
		ld hl,G_B
		dec (hl)
		pop hl
		jr tr_runs__put
tr_runs__fl:		push bc
		push de
		push hl
		call tr_flush
		pop hl
		pop de
		pop bc
		ret
tr_runs__stopp:		pop af
tr_runs__stop:		ld hl,(tr_pc)
tr_runs__end:		ld (fw_ret),hl
		ex de,hl
		call set_game_hl
		ld a,c
		or a
		jr z,tr_runs__fl2
		ld hl,(fw_sp)		; flags as OUTI leaves them: Z from B, N set
		ld a,(hl)
		and %10111111
		or $02
		ld b,a
		ld a,(G_B)
		or a
		ld a,b
		jr nz,tr_runs__nz
		or $40
tr_runs__nz:		ld (hl),a
tr_runs__fl2:		call tr_flush
		pop iy
		ld ix,(tr_ix)
		jp fw_exit

; A run of tr_nrun OUTDs: bytes from game HL downwards, through TR_DBUF.
tr_outds:
		push iy
		ld a,(tr_nrun)
		ld c,a
		ld l,a
		ld h,0
		add hl,hl
		ld de,(tr_S)
		add hl,de
		ld (fw_ret),hl		; after the run
		ld a,(G_B)
		sub c
		ld (G_B),a
		call game_hl
		ld b,c
		ld iy,TR_DBUF
tr_outds__l:		ld a,(hl)
		dec hl
		ld (iy+0),a
		inc iy
		ld a,iyl
		cp TR_DLIM
		jr c,tr_outds__n
		push bc
		push hl
		call tr_flush
		pop hl
		pop bc
tr_outds__n:		djnz tr_outds__l
		call set_game_hl
		call tr_flush
		pop iy
		jp tr_outis__flags

; A run of tr_nrun OUTIs: one block from game HL to port C.
tr_outis:
		ld ix,(tr_ix)
		ld a,(tr_nrun)
		ld b,a
		ld l,a
		ld h,0
		add hl,hl
		ld de,(tr_S)
		add hl,de
		ld (fw_ret),hl		; after the run
		ld a,(G_B)
		sub b
		ld (G_B),a
		call game_hl
		call out_block
		call set_game_hl
tr_outis__flags:		ld ix,(tr_ix)
		ld hl,(fw_sp)
		ld a,(hl)
		and %10111111
		or $02
		ld (hl),a
		ld a,(G_B)
		or a
		jp nz,fw_exit
		set 6,(hl)
		jp fw_exit

; The trace could not be made: run the site as a single output.
tr_plain:
		ld ix,(tr_ix)
		ld a,(tr_op)
		sub $18
		cp 8
		jp c,io_jump
		ld a,(tr_op)
		cp TRACE_OUTI
		ld b,$A3
		jr z,tr_plain__p
		cp TRACE_OUTD
		ld b,$AB
		jr z,tr_plain__p
		sub $40			; $81+8r -> $41+8r
		ld b,a
tr_plain__p:		ld a,b
		jp ed_dispatch

; ----------------------------------------------------------------------
; Run-time routines called by trace code. Game registers are live; IY is
; the output pointer; AF' is scratch (the game's AF' is saved).
; ----------------------------------------------------------------------
; A = byte (scratch AF, the game's AF in AF')
tr_put:		ld (iy+0),a
		inc iy
		ld a,iyl
		cp TR_DLIM
		ret c
		push bc
		push de
		push hl
		push ix
		call tr_flush
		pop ix
		pop hl
		pop de
		pop bc
		ret

m_outi:		ex af,af'
		ld a,(hl)
		call tr_put
		ex af,af'
		inc hl
		dec b			; Z and N as OUTI leaves them
		ret

m_outd:		ex af,af'
		ld a,(hl)
		call tr_put
		ex af,af'
		dec hl
		dec b
		ret

m_outa:		ld (tr_a),a
		ex af,af'
		ld a,(tr_a)
		call tr_put
		ex af,af'
		ret

; CALL m_exit; DW pc: store the game's registers, send the bytes, leave
; to pc.
m_exit:		ld (tr_tmp),hl
		pop hl
		push de
		ld e,(hl)
		inc hl
		ld d,(hl)
		ld (fw_ret),de
		pop de
		ld hl,(tr_tmp)
		ld (G_C),bc
		ld (G_E),de
		ld (tr_tmp),sp
		ld sp,(fw_sp)
		inc sp
		inc sp
		inc sp
		inc sp
		push hl
		push af
		ld sp,(tr_tmp)
		call tr_flush
		ex af,af'
		pop af
		ex af,af'
		pop iy
		ld ix,(tr_ix)
		jp fw_exit

; Send TR_DBUF..IY to the trace's port; IY back to TR_DBUF.
tr_flush:	push iy
		pop hl
		ld a,l
		ld iy,TR_DBUF
		or a
		ret z
		ld b,a
		ld a,(tr_class)
		cp 4
		jr nz,tr_flush__slow
		ld hl,TR_DBUF
		ld a,(vdp_code)
		cp 3
		jp z,cram_block
		ld a,b
		cp 16			; a few bytes: cheaper one by one
		jp nc,vram_block
tr_flush__slow:		push bc
		ld a,(tr_class)
		call class_wr
		ld (tr_flush__call+1),hl
		pop bc
		ld hl,TR_DBUF
tr_flush__l:		push bc
		push hl
		ld c,(hl)
tr_flush__call:		call 0
		pop hl
		pop bc
		inc hl
		djnz tr_flush__l
		ret
