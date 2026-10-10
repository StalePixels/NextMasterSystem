; trace.asm: one handler call for a run or a loop of output instructions.
; Included in fw.asm (resident page).
;
; A trace op ($18-$1F OUT (n),A, $C3 OUTI, $CB OUTD, $81+8r OUT (C),r;
; tools/tracedef.py) marks an output site whose neighbourhood holds more
; outputs: an unrolled run, OUTI / OUT (C),A pairs, or a loop. The handler
; copies the game's code from the site on (and back to the loop head
; when a jump goes back over the site) into a buffer, with each patched
; output turned into a call that appends its byte to TR_DBUF, and runs it
; with the game's registers. What was decided for a site is kept in the
; trace cache (TRC_PAGE): a copy, a run, or that the site runs plain. An
; entry is found by site address, the pages of the slots the code was read
; from and the port classes (nothing read from RAM is kept: tr_store).
; Copies fill the code area (TR_CODE-$FCFF, then $FD18-$FEFD); when it is
; full they are all dropped and the decisions stay (tr_newcode). Instructions are copied only from the set in
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

		IFDEF TRACE_BUILD
TR_CODE		equ $FB80		; the trace build's checks (vdpcheck.asm) end the framework code
		ELSE
TR_CODE		equ $FB00		; trace code: TR_CODE-$FCFF, below the IM2 table,
		ENDIF
TR_HOLE		equ $FD00		; then $FD18-$FEFD, after the two IM2 vectors
TR_HEND		equ $FD18		; in use (tools/check-layout checks that the
TR_CEND		equ $FEFE		; framework code ends before TR_CODE)
TR_RMAX		equ (TR_CODE>>8)-1	; most sites in one run: a cached run keeps its
					; length where a copy keeps its code address
TR_BUDGET	equ 120			; most bytes of code for one trace
TR_SETS		equ 256			; trace cache: TR_SETS sets of TR_WAYS entries in
TR_WAYS		equ 4			; TRC_PAGE, mapped at $0000 while it is used; a
TR_CE		equ 8			; site's set is (site low ^ site high)
TR_DBUF		equ $FF00		; output bytes: $FF00-$FF6F
TR_DLIM		equ $70
TR_NT		equ 8			; jump targets and fixups kept
TK_SITE		equ 8
TRACE_OUTI	equ $C3
TRACE_OUTD	equ $CB

; variables: trvars.inc (in the page gap after tables.inc)
tr_tg		equ $FF70		; TR_NT jump targets: source address, buffer address
tr_fx		equ $FF90		; TR_NT fixups: buffer position, target source address
; A cache entry: site, page at site, the other slot read + the code
; generation (tr_gen) in bits 3-7, the page there (tr_store), code address
; (0 plain; a run: its sites, kind 1-3), key. Site 0: empty.

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
		; The cache knows this site: run its copy (an address in TR_CODE),
		; or what was decided for it: 0 plain, else a run of H sites, L =
		; 1 site by site, 2 OUTIs, 3 OUTDs as one block.
		call tr_lookup
		jr nz,tr_start__new
		ld hl,(tr_go+1)
		ld a,h
		cp 255&(TR_CODE>>8)
		jp nc,tr_start__run
		or a
		jp z,tr_plain
		ld (tr_nrun),a
		ld a,l
tr_start__mark:		dec a
		jp z,tr_runs
		dec a
		jp z,tr_outis
		jp tr_outds
tr_start__new:		; patched outputs in a row with no loop jump after them are
		; done here (tr_outis, tr_runs); loops are copied (tr_build, fw4) and run
		call tr_rscan
		ld (tr_after),hl
		ld hl,tr_build
		call fw4_call		; A: 0 run the copy, 1-3 a run of sites, $FF plain
		or a
		jr z,tr_start__run
		inc a
		jp z,tr_plain
		dec a
		jp tr_start__mark
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

; Patched sites in a row from the site, at most TR_RMAX: tr_nrun,
; tr_allouti (1 all OUTI, 2 all OUTD, 0 other);
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
		cp TR_RMAX
		jr z,tr_rscan__rs2
		ld a,(tr_rst)
		cp (hl)
		jr z,tr_rscan__rs
tr_rscan__rs2:		ld a,b
		ld (tr_nrun),a
		ld a,c
		ld (tr_allouti),a
		ret

; A = MMU slot -> A = the game's page there
tr_page:	push hl
		ld hl,cur_mmu
		add hl,a
		ld a,(hl)
		pop hl
		ret

; A = page: Z if it is RAM (SMS RAM or cart RAM)
tr_ram:		cp SMSRAM_PAGE
		ret z
		and $FC
		cp CARTRAM_PAGE
		ret

; Put the game's page back in slot 0. Keeps every register but F, and
; leaves carry clear.
tr_game0:	push af
		ld a,(cur_mmu)
		nextreg $50,a
		pop af
		or a
		ret

; HL = the cache set of site tr_S, with TRC_PAGE mapped in slot 0
tr_set:		nextreg $50,TRC_PAGE
		ld hl,(tr_S)
		ld a,l
		xor h
		ld d,a
		ld e,TR_WAYS*TR_CE
		mul d,e
		ex de,hl
		ret

; A cached decision for this site and these pages? Z: yes, tr_go set.
tr_lookup:	call tr_set
		ld b,TR_WAYS
tr_lookup__l:	call tr_match
		jr z,tr_lookup__hit
		ld de,TR_CE
		add hl,de
		djnz tr_lookup__l
		call tr_game0
		or 1
		ret
tr_lookup__hit:	call tr_game0
		xor a
		ret

; HL = cache entry: Z if it is this site with these pages and key (and,
; for a copy, of this code generation), and then tr_go is set. Keeps B
; and HL.
tr_match:	ld de,(tr_S)
		ld a,(hl)
		cp e
		ret nz
		inc hl
		ld a,(hl)
		dec hl
		cp d
		ret nz
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
		jr nz,tr_match__no
		inc hl
		ld a,(hl)		; the other slot + the code generation
		ld c,a
		and 7
		call tr_page
		inc hl
		cp (hl)
		jr nz,tr_match__no
		inc hl
		ld e,(hl)
		inc hl
		ld d,(hl)
		inc hl
		ld a,(tr_key)
		cp (hl)
		jr nz,tr_match__no
		ld a,d			; a copy: its code is of this generation
		cp 255&(TR_CODE>>8)
		jr c,tr_match__ok
		ld a,c
		and $F8
		ld hl,tr_gen
		cp (hl)
		jr nz,tr_match__no
tr_match__ok:	ld (tr_go+1),de
		pop hl
		xor a
		ret
tr_match__no:		pop hl
		or 1
		ret

; A = the byte of the game's code at HL, for tr_build (fw4, in slot 1):
; $2000-$3FFF is read from the game's page there. Keeps the other registers.
tr_rd:		ld a,h
		and $E0
		cp $20
		jr z,tr_rd__s1
		ld a,(hl)
		ret
tr_rd__s1:	ld a,(cur_mmu+1)
		nextreg $51,a
		ld a,(hl)
		nextreg $51,FW4_PAGE
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
		cp 3			; one or two bytes: cheaper one by one
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

