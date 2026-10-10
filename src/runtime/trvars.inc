; trvars.inc: trace.asm variables, placed by fw.asm in the gap after
; tables.inc so that the code area keeps its room.
tr_rst:		db 0			; opcode of the io RST
tr_op:		db 0			; the site's op
tr_class:	db 0			; port class of every output in the trace
tr_flags:	db 0			; bit 0: a C-port output, bit 1: C written
tr_size:	db 0			; worst-case bytes of trace code so far
tr_k:		db 0			; kind of the instruction being taken
tr_wc:		db 0			; it writes C
tr_co:		db 0			; it is an output to port C
tr_S:		dw 0			; site
tr_E:		dw 0			; end of the copied range
tr_H:		dw 0			; start of the copied range
tr_back:	dw 0			; first jump target before the site
tr_ntg:		db 0
tr_nfx:		db 0
tr_keep:	ds 3			; size, flags, ntg before the head scan
tr_tmp:		dw 0
tr_a:		db 0
tr_spsv:	dw 0
tr_ix:		dw 0			; the game's IX (pass 2 uses IX)
tr_nrun:	db 0			; patched sites in a row from the site
tr_allouti:	db 0			; the run is all OUTI
tr_pc:		dw 0
tr_cok:		db 0			; port C's class is the trace's
tr_loop:	db 0			; the copy ends in a jump back over the site
tr_nout:	db 0			; outputs in the copied range
tr_gen:		db 0			; code generation << 3 (tr_newcode)
tr_aptr:	dw TR_CODE		; next free byte of trace code
tr_key:		db 0			; trace class, + $10 for a port C trace
tr_gcls:	db 0			; class of port C at the site
tr_after:	dw 0			; the first byte after the run (tr_rscan), for tr_build
