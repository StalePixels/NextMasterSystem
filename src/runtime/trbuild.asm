; trbuild.asm: the trace builder, in the fourth framework page (fw4.asm,
; mapped at $2000). tr_start (trace.asm) calls tr_build through fw4_call
; when the cache has no copy for a site. It decides how the site runs and
; writes the copy of the game's code into TR_CODE. With this page in slot 1
; the game's own $2000-$3FFF is not mapped, so every read of the game's
; code goes through tr_rd (trace.asm), which maps the game's page for it.
;
; tr_build: tr_S, tr_class and tr_key set, and tr_nrun, tr_allouti and
; tr_after from tr_rscan. Returns
; A = 0: the copy is in the cache and tr_go jumps to it; 1-3: run the
; sites as one run (tr_start__mark); $FF: run the site plain.
; When the copy cannot be made, the cache keeps that: a run of sites is
; then done in one call, a single site runs plain.
tr_build:	call tr_build1
		cp $FF
		ret nz
		ld a,(tr_nrun)
		cp 2
		jr nc,tr_build__frun
		ld de,0
		call tr_store
		ld a,$FF
		ret
tr_build__frun:	ld a,(tr_allouti)
		inc a
		ld e,a
		ld a,(tr_nrun)
		ld d,a
		push de
		call tr_store
		pop de
		ld a,e
		ret
; A = 0, 1-3 as tr_build, $FF: the copy cannot be made.
tr_build1:
		ld hl,(tr_S)		; no loop head until one is found
		ld (tr_H),hl
		ld hl,(tr_after)	; from the first byte after the run:
		ld a,6			; a loop jump within 6 instructions after it?
		ld (tr_a),a
tr_build__la:		call tr_dec
		or a
		jr z,tr_build__nolp
		cp 3
		jr c,tr_build__la1
		cp TK_SITE
		jr z,tr_build__nolp
		cp 4			; JR cc
		jr z,tr_build__lp
		cp 5			; DJNZ
		jr z,tr_build__lp
		cp 7			; JP cc
		jr nz,tr_build__nolp
tr_build__lp:		ld hl,(tr_S)		; a loop when it jumps back to the site or before
		or a
		sbc hl,de
		jr nc,tr_build__compile
		jr tr_build__nolp
tr_build__la1:		ld a,b
		add hl,a
		ld a,(tr_a)
		dec a
		ld (tr_a),a
		jr nz,tr_build__la
tr_build__nolp:		ld a,(tr_nrun)		; a run with no loop: OUTIs or OUTDs as one
		cp 2			; block, others site by site, kept in the
		jr c,tr_build__compile		; cache with no code: its length (D) and kind (E)
		ld hl,(tr_after)
		ld (tr_E),hl
		ld a,(tr_allouti)
		inc a
		ld e,a
		ld a,(tr_nrun)
		ld d,a
		push de
		call tr_store
		pop de
		ld a,e
		ret			; 2 all OUTI, 3 all OUTD, 1 other
tr_build__compile:	; room for its code: below the IM2 vectors, else after them
		ld hl,(tr_aptr)
		ld de,TR_HOLE
		or a
		sbc hl,de
		jr nc,tr_build__room	; after them already
		ld de,TR_BUDGET
		add hl,de
		jr nc,tr_build__go	; fits below them
		ld hl,TR_HEND
		ld (tr_aptr),hl
tr_build__room:		ld hl,(tr_aptr)
		ld de,TR_BUDGET
		add hl,de
		ld de,TR_CEND
		or a
		sbc hl,de
		call nc,tr_newcode	; full: drop every copy
tr_build__go:
		; forward from the site
		ld hl,(tr_S)
tr_build__fw:		call tr_dec
		call tr_take
		jr c,tr_build__fend
		ld a,(tr_k)
		cp 3
		jr c,tr_build__fnext
		cp TK_SITE
		jr z,tr_build__fsite
		; a jump, target DE. Back to the site or before it: the loop
		; closes here, the copy ends after it.
		push hl
		ld hl,(tr_S)
		or a
		sbc hl,de		; site - target
		pop hl
		jr c,tr_build__fwd
		ld a,1
		ld (tr_loop),a
		jr z,tr_build__fstop
		ld (tr_back),de
		jr tr_build__fstop
tr_build__fwd:		ld a,(tr_k)		; forward, or back to code after the site
		cp 3			; JR
		jr z,tr_build__fstop
		cp 6			; JP
		jr z,tr_build__fstop
		jr tr_build__fnext
tr_build__fsite:		ld a,(tr_nout)
		inc a
		ld (tr_nout),a
tr_build__fnext:		ld a,b
		add hl,a
		jr tr_build__fw
tr_build__fstop:		ld a,b
		add hl,a
tr_build__fend:		ld (tr_E),hl
		ld de,(tr_S)
		or a
		sbc hl,de
		jp z,tr_build__fail		; the site itself did not fit
		ld a,(tr_loop)		; no loop and fewer than 3 outputs: not
		or a			; worth a copy
		jr nz,tr_build__worth
		ld a,(tr_nout)
		cp 3
		jp c,tr_build__fail
tr_build__worth:
		; loop head: decode from it, it must reach the site
		ld hl,(tr_S)
		ld (tr_H),hl
		ld hl,(tr_back)
		ld a,h
		or l
		jr z,tr_build__emit
		ld a,(tr_size)
		ld (tr_keep),a
		ld a,(tr_flags)
		ld (tr_keep+1),a
		ld a,(tr_ntg)
		ld (tr_keep+2),a
tr_build__hd:		ld de,(tr_S)
		push hl
		or a
		sbc hl,de
		pop hl
		jr z,tr_build__hok
		jr nc,tr_build__hfail
		call tr_dec
		call tr_take
		jr c,tr_build__hfail
		ld a,(tr_k)
		cp 3
		jr z,tr_build__hfail
		cp 6
		jr z,tr_build__hfail
		ld a,b
		add hl,a
		jr tr_build__hd
tr_build__hfail:		ld a,(tr_keep)
		ld (tr_size),a
		ld a,(tr_keep+1)
		ld (tr_flags),a
		ld a,(tr_keep+2)
		ld (tr_ntg),a
		jr tr_build__emit
tr_build__hok:		ld hl,(tr_back)
		ld (tr_H),hl
tr_build__emit:		; ---- pass 2: write the trace code ----
		ld ix,(tr_aptr)
		ld hl,(tr_H)
tr_build__em:		ld de,(tr_E)
		push hl
		or a
		sbc hl,de
		pop hl
		jp z,tr_build__emend
		ld de,(tr_S)
		push hl
		or a
		sbc hl,de
		pop hl
		jr nz,tr_build__ns
		ld (tr_go+1),ix
tr_build__ns:		call tr_mark
		call tr_dec
		cp 3
		jp c,tr_build__copy
		cp TK_SITE
		jp z,tr_build__site
		; jump: A = kind, DE = target. Inside [H, E]?
		ld (tr_k),a
		push hl
		ld hl,(tr_H)
		ex de,hl		; HL = target, DE = H
		push hl
		or a
		sbc hl,de
		pop hl
		jr c,tr_build__ext
		ld de,(tr_E)
		push hl
		ex de,hl
		or a
		sbc hl,de		; E - target
		pop de			; DE = target
		jr c,tr_build__ext2
		; internal
		pop hl
		ld a,(tr_k)
		cp 5
		jr z,tr_build__idj
		ld c,$C3		; JR, JP
		cp 3
		jr z,tr_build__ij
		cp 6
		jr z,tr_build__ij
		call tr_rd		; JR cc / JP cc
		ld c,a
		cp $40
		jr nc,tr_build__ij
		add a,$A2		; JR cc -> JP cc
		ld c,a
tr_build__ij:		ld (ix+0),c
		inc ix
		call tr_fixup
		inc ix
		inc ix
		jp tr_build__next
tr_build__idj:		ld (ix+0),$10		; DJNZ +2; JR +3; JP target
		ld (ix+1),$02
		ld (ix+2),$18
		ld (ix+3),$03
		ld (ix+4),$C3
		ld bc,5
		add ix,bc
		call tr_fixup
		inc ix
		inc ix
		jr tr_build__next2
tr_build__ext:		ex de,hl		; DE = target
tr_build__ext2:		pop hl
		ld a,(tr_k)
		cp 3
		jr z,tr_build__xu
		cp 6
		jr z,tr_build__xu
		cp 5
		jr z,tr_build__xdj
		call tr_rd		; JR cc / JP cc: JP !cc over the exit
		cp $40
		jr nc,tr_build__xc
		add a,$A2
tr_build__xc:		xor 8
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
		jr tr_build__xu
tr_build__xdj:		ld (ix+0),$10		; DJNZ +2; JR +5; exit to target
		ld (ix+1),$02
		ld (ix+2),$18
		ld (ix+3),$05
		inc ix
		inc ix
		inc ix
		inc ix
tr_build__xu:		call tr_exitstub
		jr tr_build__next2
tr_build__copy:		; B bytes as they are
		push hl
tr_build__cp:		call tr_rd
		ld (ix+0),a
		inc hl
		inc ix
		djnz tr_build__cp
		pop hl
		jr tr_build__next2
tr_build__next:
tr_build__next2:		call tr_dec		; B = length again
		ld a,b
		add hl,a
		jp tr_build__em
tr_build__site:		; E = op
		ld a,e
		ld bc,m_outa
		cp 8
		jr c,tr_build__s3
		sub $18
		cp 8
		jr c,tr_build__s3
		ld a,e
		ld bc,m_outi
		cp $A3
		jr z,tr_build__s3
		cp TRACE_OUTI
		jr z,tr_build__s3
		ld bc,m_outd
		cp $AB
		jr z,tr_build__s3
		cp TRACE_OUTD
		jr z,tr_build__s3
		rrca			; OUT (C),r: r = (op >> 3) & 7
		rrca
		rrca
		and 7
		ld bc,m_outa
		cp 7
		jr z,tr_build__s3
		ld (ix+0),$08		; EX AF,AF'
		ld c,$AF		; r = 6: XOR A (OUT (C),0)
		cp 6
		jr z,tr_build__s6
		add a,$78		; LD A,r
		ld c,a
tr_build__s6:		ld (ix+1),c
		inc ix
		inc ix
		ld bc,tr_put
		call tr_call
		ld (ix+0),$08
		inc ix
		jr tr_build__next2
tr_build__s3:		call tr_call
		jr tr_build__next2
tr_build__emend:		call tr_mark
		ld de,(tr_E)
		call tr_exitstub
		; resolve the fixups
		ld a,(tr_nfx)
		or a
		jr z,tr_build__store
		ld b,a
		ld hl,tr_fx
tr_build__fx:		push bc
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
		jr z,tr_build__fxbad
		ld a,l
		ld (bc),a
		inc bc
		ld a,h
		ld (bc),a
		pop hl
		pop bc
		djnz tr_build__fx
tr_build__store:		ld de,(tr_go+1)
		call tr_store		; carry: not kept, its code space is free again
		jr c,tr_build__run
		ld (tr_aptr),ix
tr_build__run:		xor a			; run it
		ret
tr_build__fxbad:		pop hl
		pop bc
		jp tr_build__fail
tr_build__fail:	ld a,$FF		; not copied (tr_build)
		ret

; The code area is full: drop every copy by starting a new code generation
; (tr_match takes a copy only of the current one); the decisions for runs
; and plain sites stay. When the generation number goes round the whole
; cache is emptied, so an old number is never taken for a new one.
tr_newcode:	ld hl,TR_CODE
		ld (tr_aptr),hl
		ld a,(tr_gen)
		add a,8
		ld (tr_gen),a
		ret nz
		call tr_reset
		jp tr_game0

; Empty the trace cache and the code area: a new game (fw4_start), or the
; code generation number has gone round (tr_newcode). Leaves page $FF in
; slot 0 (clear_page).
tr_reset:	ld a,TRC_PAGE		; TR_SETS * TR_WAYS * TR_CE = 8K
		call clear_page
		xor a
		ld (tr_gen),a
		ld hl,TR_CODE
		ld (tr_aptr),hl
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
		call tr_rd
		ld e,a
		ld a,(tr_rst)
		cp e
		jr z,tr_dec__site
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
		call tr_rd
		ld e,a
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
		call tr_rd
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
		call tr_rd
		ld e,a
		inc hl
		call tr_rd
		ld d,a
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
		call tr_rd
		ld e,a
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

; DE = code address (0 = plain): fill cache entry tr_idx for this site.
; In fw4 (slot 1), called by tr_build.
; The entry keeps the pages of the two slots the copy was read from: the
; site's, and the loop head's when it is in another slot, else the end's
; (a copy crosses at most one 8K boundary). A copy read from RAM is not
; kept (carry set): the game can change the code there while the page
; stays the same, so the cache could not see it.
tr_store:	push de
		ld a,(tr_S+1)
		rlca
		rlca
		rlca
		and 7
		ld c,a			; C = the site's slot
		ld a,(tr_H+1)
		rlca
		rlca
		rlca
		and 7
		cp c
		jr nz,tr_store__o
		ld de,(tr_E)
		dec de
		ld a,d
		rlca
		rlca
		rlca
		and 7
tr_store__o:	ld b,a			; B = the other slot
		call tr_page
		ld e,a			; E = the page there
		ld a,b			; RAM is only in slots 4-6
		cp 4
		jr c,tr_store__r1
		ld a,e
		call tr_ram
		jr z,tr_store__ram
tr_store__r1:	ld a,c
		call tr_page
		ld d,a			; D = the page at the site
		ld a,c
		cp 4
		jr c,tr_store__r2
		ld a,d
		call tr_ram
		jr z,tr_store__ram
tr_store__r2:	; the new entry goes first in the site's set, the oldest
		; of the set is dropped
		push de
		ld a,(tr_gen)
		or b
		ld b,a
		push bc
		call tr_set
		push hl
		ld de,TR_WAYS*TR_CE-1
		add hl,de
		ld d,h
		ld e,l
		ld bc,-TR_CE
		add hl,bc
		ld bc,(TR_WAYS-1)*TR_CE
		lddr
		pop hl
		pop bc
		pop de
		ld a,(tr_S)
		ld (hl),a
		inc hl
		ld a,(tr_S+1)
		ld (hl),a
		inc hl
		ld (hl),d
		inc hl
		ld (hl),b
		inc hl
		ld (hl),e
		inc hl
		pop de
		ld (hl),e
		inc hl
		ld (hl),d
		inc hl
		ld a,(tr_key)
		ld (hl),a
		jp tr_game0
tr_store__ram:	pop de
		scf
		ret
