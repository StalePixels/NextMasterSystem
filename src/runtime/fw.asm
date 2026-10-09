; fw.asm: NextMasterSystem resident framework. Lives in 8K page FW_PAGE, mapped
; at $E000-$FFFF (MMU7) while the game runs. The game reaches it through
; RST vectors that the overlay points at the jump table below. Work that
; runs once per frame (tile conversion, sprites, copper, keyboard) is in
; fw2.asm, page FW2_PAGE, mapped at $2000 only while it runs.
;
; Handler frame. Every RST handler starts with FASTENTRY. On the game's
; stack it leaves the RST return slot (now holding the game's HL) and AF:
; 4 bytes below the game's SP, as in stage A. Then it moves to fw_stack and
; pushes BC and DE there, so handlers may use every register:
;   game F = (fw_sp), A = (fw_sp)+1, L = (fw_sp)+2, H = (fw_sp)+3
;   game B = G_B, C = G_C, D = G_D, E = G_E (fixed addresses)
; fw_exit pops BC/DE, reloads AF from the game stack (so handlers change
; game A or F there) and returns to fw_ret with the game's HL restored.
; Handlers run with interrupts off; the entry patches an EI or NOP into
; the exit so the game's IFF comes back as it was.

		MACRO FASTENTRY
		local fe_ok
		ex (sp),hl		; HL = inline byte address, game HL in the slot
		push af
		ld a,i			; P/V = IFF2
		di
		ld a,$00		; NOP
		jp po,fe_ok
		ld a,$FB		; EI
fe_ok:		ld (exit_ei),a
		pop af			; game A into game_a only after the DI: a
		ld (game_a),a		; handler run by an interrupt taken before
		push af			; it would overwrite game_a
		ld (fw_sp),sp
		ld sp,fw_stack_top
		push bc
		push de
		ld a,(hl)		; inline byte
		inc hl
		ld (fw_ret),hl
		ENDM

; one output byte of a tile row: planes in B,C,D,E; H = table page
		MACRO CONVBYTE k
		ld l,e
		ld a,(hl)
		add a,a
		ld l,d
		or (hl)
		add a,a
		ld l,c
		or (hl)
		add a,a
		ld l,b
		or (hl)
		ld (ix+k),a
		ENDM

; The SMS picture sits PIC_X pixels right of the ULA area's left edge. In
; MAME a copper WAIT for column h takes effect at pixel 8h+2, so with
; PIC_X = 2 the lock-right switch lands exactly on SMS column 24.
PIC_X		equ 2

; Next tilemaps in bank 7 (MAP_PAGE). M0 holds SMS columns 0-31 in Next
; columns 0-31 and SMS columns 0-7 again in 32-39. A8 is M0 turned by 8
; columns: SMS 8-31, 0-7, 0-7. Showing A8 is the same as showing M0 with
; the X offset 64 pixels further on, so a copper switch from M0 to A8 in
; the middle of a line makes the 320-pixel Next map wrap like the
; 256-pixel SMS map.
MAP_A8		equ $0A00		; offset of A8 in MAP_PAGE (after M0's 32 rows)
NR6E_M0		equ $80
NR6E_A8		equ $80 | (MAP_A8 >> 8)

;		org $E000  (section origin)
; ---- jump table. Entries never move. ----
fw_jt:
		jp fw_out_n		; $E000 OUT (n),A   (RST + inline n)
		jp fw_in_n		; $E003 IN A,(n)    (RST + inline n)
		jp fw_ed		; $E006 ED xx group (RST + inline xx)
		jp fw_ld_de_a		; $E009 LD (DE),A, mapper aware (RST, no inline)
		jp fw_start		; $E00C start the game (loader only)
		jp fw_fatal		; $E00F stop with red border
		jp fw_outi_run		; $E012 run of OUTIs to the end of an unrolled block (RST + inline count)
		jp fw_io		; $E015 any I/O instruction (RST + inline op), ABI 2
		jp fw_io0		; $E018 the same, as the RST $00 vector (ABI 3)
FW_ABI		equ 5			; 5: overlay flags (priority tiles, line-0 palette)
		public FW_ABI
; $E01B: a JP to the outer shell's resume entry. The shell writes its target
; (the two bytes at $E01C) before it starts a game. fw_quit jumps here.
fw_resume:	jp 0

		defs ($E020)-0xE000-$
; ---- state that tools read from outside (fixed addresses) ----
fw_status:	db 0			; $E020 loader progress / error code
fw_crc:		ds 4			; $E021 cart CRC32
fw_size:	ds 4			; $E025 cart size (after copier header)
fw_npages:	db 0			; $E029 cart 8K pages
fw_lastop:	db 0			; $E02A last ED op
fw_frames:	dw 0			; $E02B frames of vblank work done
cur_mmu:	ds 8			; $E02D game's MMU0-7 pages

; VDP state; test tools read vdp_latch..cram at fixed addresses ($E035-$E06C)
vdp_latch:	db 0			; $E035
vdp_code:	db 0
vdp_addr:	dw 0
vdp_rbuf:	db 0
vdp_status:	db 0			; $E03A
vdp_regs:	ds 16			; $E03B
nt_base:	dw $3800		; $E04B name table base (from register 2)
cram:		ds 32			; $E04D
fw_start_addr:	dw 0			; $E06D game start address (overlay START op)
fw_start_sp:	dw $DFF0		; $E06F game SP at the start (overlay START op)
isr_n:		db 0			; $E071 frame handler entries, mod 256 (read by test tools)

; ---- other state ----
game_a:		db 0
fw_sp:		dw 0			; game SP while a handler runs
fw_ret:		dw 0			; game return address while a handler runs
irq_sp:		dw 0			; game SP while the vblank interrupt runs
sat_hi:		db $3F			; sprite attribute table address high byte
tiles_dirty:	db 0			; some page in dirty_pages is set
sat_dirty:	db 1			; sprites must be rebuilt
cop_dirty:	db 1			; copper list must be rebuilt
nt_dirty:	db 0			; name table base changed: maps rebuilt
vbl_done:	db 0			; vblank work done for this frame
fdone:		db 0			; frame flag delivered for this frame
line_pend:	db 0			; SMS line interrupt pending
rast_hook:	dw 0			; overlay per-line H scroll hook in fw2 (HOOK op), 0 = none
ramp_hook:	dw 0			; overlay RAM code patch table in fw2 (HOOK kind 2)
m224:		db 0			; 224-line mode (register 0 bit 1 and register 1 bit 4)
pic_end:	db 192			; Next line after the SMS picture: 192, or 208 in 224-line mode
op_n:		db 0			; inline byte of a mapper op site (op_mapper)
op_nx:		ds 3			; the 3 bytes after a 3-byte mapper site (op_mapper)
shadow_i:	db 0			; the game's I register (ed_ldia, ed_ldai)
hl_on:		db 0			; this frame's H scroll comes from the hook's table
ev_next:	db 192			; SMS line of the next scheduled event (192 = frame)
kbd_dc:		db $FF			; keyboard as SMS $DC bits, read once a frame
pause_req:	db 0			; Pause pressed: emulate the NMI
quit_req:	db 0			; BREAK pressed: back to the browser
h_x:		dw 0			; tilemap X offset for the current H scroll
h_sw:		db 0			; copper column of the M0->A8 switch, 0 = none
cop_sw:		db $FF			; switch column in the copper list now
cop_v:		db $FF			; V scroll in the copper list now
cop_mode:	db $FF			; 0 normal list, 1 lock-right list
bd_cur:		db $FF			; backdrop colour in the ULA palette now
tr_free:	dw $FFFF		; pixel values no sprite-palette tile on screen uses
bg_free:	dw 0			; pixel values no background tile on screen uses
					; (kept only while tr_free is 0)
psg_latch:	db 0			; latched channel*2 + type
psg_tone:	dw 0,0,0		; 10-bit tone registers
psg_vol:	db 15,15,15,15
psg_noise:	db 0
ay_cur:		db 0			; AY chip selected now ($FF AY0, $FE AY1)
; overlay switches (header flags): bit 0 priority tiles in Layer 2 (fw2
; pri_frame), bit 1 line-0 palette (toppal: cram_x in fw2, pal_vbl here)
fw_flags:	db 0
pri_x:		db 254			; Layer 2 X scroll for the current H scroll (K - 2)
lay15:		db 0			; NextReg $15 layer order bits: 4 = L S U (priority tiles)
pal43:		db %00000010		; NextReg $43 display bits: ULA second; bits 3 and 2
					; (second sprite and Layer 2 palettes) while toppal shows them
tm_ctl:		db %00000010		; NextReg $6B without bit 4 (second tilemap palette)
pal_ph:		db 1			; toppal: 1 from the frame event to the first line event
dis_pend:	db 0			; toppal: a display-off write waits for the phase end
disp_on:	db 0			; the display enable shown: $40 on, 0 off
pal_vm:		ds 4			; toppal: CRAM entries written in the last vblank phase
cram_top:	ds 32			; toppal: CRAM as the second palettes hold it
isr_sp:		dw 0			; return slot of the last frame handler entry
isr_ret:	dw 0			; the address the entry put in it
isr_pc:		dw 0			; that address while isr_tramp holds the slot
isr_k:		db 0
line_held:	db 0			; a line event waits for a frame handler's end
isr_go:		dw 0
irq_s:		dw 0
irq_pend:	db 0			; a frame event is held (irq_frame)
nr_saved:	ds 48			; NextReg values to restore on quit
fw_stack:	ds 120
fw_stack_top:
G_B		equ fw_stack_top-1
G_C		equ fw_stack_top-2
G_D		equ fw_stack_top-3
G_E		equ fw_stack_top-4
; assert (low fw_stack_top) >= 8, "reg_addr needs the frame inside one page" (checked by tools/check-layout)

		align 256
		include "tables.inc"	; mapattr (256), pal_hi/lo, joy, ay_vol
		include "trvars.inc"	; trace.asm variables, in the rest of the page
trvars_end:

		align 256
; assert trvars_end <= $, "trvars.inc runs into region_tab's page" (checked by tools/check-layout)
region_tab:	ds 64			; per 256-byte VRAM page: 0 tile, 1 name table, 2 sprite table,
					; 3 name table rows 24-27 (tiles too)
dirty_pages:	ds 64			; per page: a bit per tile to convert; must
					; follow region_tab in the same page (+64)
io_tab:		dw out_nop, out_nop, out_psg, out_psg, out_vdata, out_vctrl, out_nop, out_nop
		dw in_ff, in_ff, in_vcount, in_hcount, in_vdata, in_status, in_dc, in_dd
wr_tab:		dw ret_nop, ret_nop, psg_w, psg_w, vdata_w, vctrl_w, ret_nop, ret_nop
rd_tab:		dw rd_ff, rd_ff, rd_vcount, rd_hcount, rd_vdata, rd_status, rd_dc, rd_dd
; small data in the rest of this page
pal_rows:	ds 24			; per screen row: rows from it to the bottom where
					; sprite-palette tiles show pixel value 0 more than
					; background ones, less the others (fw3 pal_scan)
tm_lo:		db $FF,$FE,$FC,$F8,$F0,$E0,$C0,$80	; tmask
tm_hi:		db $01,$03,$07,$0F,$1F,$3F,$7F,$FF

		align 256
		include "tables3.inc"	; trace_table (256)

; ======================================================================
; Entries
; ======================================================================

; RST target, ABI 2: one inline op byte for every I/O instruction.
;   $00-$07 OUT (n),A to port class 0-7    $08-$0F IN A,(n) from class 0-7
;   anything else: the second byte of an ED instruction
; Port class = A7 A6 A0 of the SMS port (the SMS decodes only those).
fw_io:
		FASTENTRY
		cp $10
		jp nc,ed_dispatch
io_jump:	add a,a
		add a,255&(io_tab)
		ld l,a
		ld h,255&((io_tab)>>8)
		ld a,(hl)
		inc l
		ld h,(hl)
		ld l,a
		jp (hl)

; RST target, ABI 1: OUT (n),A with the port as inline byte.
fw_out_n:
		FASTENTRY
		call port_class
		jr io_jump

; RST target, ABI 1: IN A,(n) with the port as inline byte. Flags unchanged.
fw_in_n:
		FASTENTRY
		call port_class
		or 8
		jr io_jump

; RST target, ABI 1: ED group with the second byte inline.
fw_ed:
		FASTENTRY
		jp ed_dispatch

; RST $00 vector. A game that jumps to $0000 to reset lands here too;
; an RST $00 leaves the address after an $C7 byte on the stack, a jump
; does not. A reset goes to the game's start address with its start SP.
fw_io0:
		ex (sp),hl
		push af
		dec hl
		ld a,(hl)
		inc hl
		cp $C7
		jr nz,fw_io0__reset
		pop af
		ex (sp),hl
		jp fw_io
fw_io0__reset:		di
		ld sp,(fw_start_sp)
		ld hl,(fw_start_addr)
		jp (hl)

fw_exit:
		pop de
		pop bc
		ld sp,(fw_sp)
		pop af			; game AF, possibly changed
		ld hl,(fw_ret)
		ex (sp),hl		; return address in the slot, game HL back
exit_ei:	nop			; patched: EI or NOP
mx_ret:		ret

; A = port -> A = class (A7 A6 A0)
port_class:
		ld l,a
		and 1
		ld h,a
		ld a,l
		rlca
		rlca
		and 3
		add a,a
		or h
		ret

; ---- single OUT handlers: value in game_a ----
out_nop:	jp fw_exit
out_psg:	ld a,(game_a)
		ld c,a
		call psg_w
		jp fw_exit
out_vdata:	ld a,(game_a)
		ld c,a
		call vdata_w
		jp fw_exit
out_vctrl:	ld a,(game_a)
		ld c,a
		call vctrl_w
		jp fw_exit

; ---- single IN handlers: result into game A ----
in_ff:		call rd_ff
		jr in_ret
in_vcount:	call rd_vcount
		jr in_ret
in_hcount:	call rd_hcount
		jr in_ret
in_vdata:	call rd_vdata
		jr in_ret
in_status:	call rd_status
		jr in_ret
in_dc:		call rd_dc
		jr in_ret
in_dd:		call rd_dd
in_ret:		ld hl,(fw_sp)
		inc hl
		ld (hl),a
		jp fw_exit

; A = class -> write routine address in HL
class_wr:	add a,a
		add a,255&(wr_tab)
		ld l,a
		ld h,255&((wr_tab)>>8)
		ld a,(hl)
		inc l
		ld h,(hl)
		ld l,a
		ret
; A = class -> read routine address in HL
class_rd:	add a,a
		add a,255&(rd_tab)
		ld l,a
		ld h,255&((rd_tab)>>8)
		ld a,(hl)
		inc l
		ld h,(hl)
		ld l,a
		ret
call_hl:	jp (hl)
ret_nop:	ret

; ======================================================================
; ED group: OTIR, OUTI, OUT (C),r, IN r,(C)
; ======================================================================
ed_dispatch:
		ld (fw_lastop),a
		cp $A3
		jp z,ed_outi
		ld b,a
		and $C7
		cp $41
		jp z,ed_out_c_r
		ld a,b
		cp $18
		jp c,op_mapper		; $10-$17: mapper stores
		cp $20
		jp c,tr_start		; $18-$1F: OUT (n),A trace (ABI 3)
		cp $40
		jp c,op_mapper		; $20-$3F: more mapper stores (ABI 4)
		cp TRACE_OUTI
		jp z,tr_start
		cp TRACE_OUTD
		jp z,tr_start
		cp $AB
		jp z,ed_outd
		cp $B3
		jp z,ed_otir
		cp $BB
		jp z,ed_otdr
		cp $A2
		jp z,ed_ini
		cp $B2
		jp z,ed_inir
		and $C7
		cp $40
		jp z,ed_in_r_c
		cp $81
		jp z,tr_start_b		; $81+8r: OUT (C),r trace (ABI 3)
		ld a,b
		cp $47
		jr z,ed_ldia
		cp $57
		jr z,ed_ldai
		jp fw_fatal
; LD I,A and LD A,I: the framework's IM 2 needs I, so the game's I is kept
; in shadow_i (Wonder Boy III keeps flags in it). LD A,I: S and Z from the
; value, P/V = the game's IFF2, H = N = 0, C kept.
ed_ldia:	ld a,(game_a)
		ld (shadow_i),a
		jp fw_exit
ed_ldai:	ld hl,(fw_sp)
		inc hl
		ld a,(shadow_i)
		ld (hl),a
		dec hl
		or a
		push af
		pop bc
		ld a,c
		and %11000000
		ld c,a
		ld a,(hl)
		and 1
		or c
		ld c,a
		ld a,(exit_ei)
		cp $FB			; EI: the game's interrupts were on
		ld a,c
		jr nz,ed_ldai__n
		or 4
ed_ldai__n:		ld (hl),a
		jp fw_exit
tr_start_b:	ld a,b
		jp tr_start

		include "trace.asm"

; A = r (0 B,1 C,2 D,3 E,4 H,5 L,6 F,7 A) -> HL = address of the game register
reg_addr:
		cp 4
		jr nc,reg_addr__hl
		cpl			; -r-1
		add a,255&(fw_stack_top)
		ld l,a
		ld h,255&((fw_stack_top)>>8)
		ret
reg_addr__hl:		sub 4
		add a,255&(reg_addr__offs)
		ld l,a
		ld a,255&((reg_addr__offs)>>8)
		adc a,0
		ld h,a
		ld a,(hl)
		ld hl,(fw_sp)
		add hl,a
		ret
reg_addr__offs:		db 3,2,0,1

; game C -> A = port class
game_class:	ld a,(G_C)
		jp port_class

ed_out_c_r:
		ld a,b
		rrca
		rrca
		rrca
		and 7
		ld c,0			; OUT (C),0 for r = 6
		cp 6
		jr z,ed_out_c_r__v
		call reg_addr
		ld c,(hl)
ed_out_c_r__v:		push bc
		call game_class
		call class_wr
		pop bc
		call call_hl
		jp fw_exit

ed_in_r_c:
		push bc			; B = op
		call game_class
		call class_rd
		call call_hl		; A = value
		pop bc
		ld c,a
		ld a,b
		rrca
		rrca
		rrca
		and 7
		cp 6
		jr z,ed_in_r_c__flags		; IN F,(C): flags only
		push bc
		call reg_addr
		pop bc
		ld (hl),c
ed_in_r_c__flags:		; S Z P/V from the value, H = N = 0, C kept
		ld hl,(fw_sp)
		ld a,(hl)
		and 1
		ld b,a
		ld a,c
		or a			; S Z P set from value, H N C clear
		push af
		pop de			; E = flags
		ld a,e
		or b
		ld (hl),a
		jp fw_exit

; game HL -> HL
game_hl:	ld hl,(fw_sp)
		inc hl
		inc hl
		ld a,(hl)
		inc hl
		ld h,(hl)
		ld l,a
		ret
; HL -> game HL
set_game_hl:	ex de,hl
		ld hl,(fw_sp)
		inc hl
		inc hl
		ld (hl),e
		inc hl
		ld (hl),d
		ret

; OTIR: B bytes from (HL) to port C; B = 0, HL += count, Z and N set.
ed_otir:
		call game_hl
		ld a,(G_B)
		ld b,a
		call out_block		; HL = source after the block
		call set_game_hl
		xor a
		ld (G_B),a
		ld hl,(fw_sp)
		ld a,(hl)
		or $42
		ld (hl),a
		jp fw_exit

; OUTD: one byte from (HL) to port C; HL--, B--, Z if B = 0, N set.
ed_outd:
		call game_hl
		ld b,1
		push hl
		call out_block
		pop hl
		dec hl
		jr ed_outi__tail

; OTDR: OUTD until B = 0, byte by byte (rare; no block path).
ed_otdr:
		call game_hl
ed_otdr__l:		push hl
		ld b,1
		call out_block
		pop hl
		dec hl
		ld a,(G_B)
		dec a
		ld (G_B),a
		jr nz,ed_otdr__l
		call set_game_hl
		ld hl,(fw_sp)
		ld a,(hl)
		or $42
		ld (hl),a
		jp fw_exit

; OUTI: one byte from (HL) to port C; HL++, B--, Z if B = 0, N set.
ed_outi:
		call game_hl
		ld b,1
		call out_block
ed_outi__tail:		call set_game_hl
		ld hl,G_B
		dec (hl)
		ld b,(hl)
		ld hl,(fw_sp)
		ld a,(hl)
		and %10111111
		or $02
		inc b
		dec b
		jr nz,ed_outi__nz
		or $40
ed_outi__nz:		ld (hl),a
		jp fw_exit

; INI / INIR: (HL) = IN (C); HL++; B-- (INIR until B = 0). Z if B = 0, N set.
ed_inir:	ld a,(G_B)
		jr ed_in_block
ed_ini:		ld a,1
ed_in_block:	ld (ed_in_block__n),a
		call game_class
		call class_rd
		ld (ed_in_block__call+1),hl
		call game_hl
		ld a,(ed_in_block__n)
		ld b,a
ed_in_block__l:		push bc
		push hl
ed_in_block__call:		call 0
		pop hl
		pop bc
		ld (hl),a
		inc hl
		djnz ed_in_block__l
		call set_game_hl
		ld a,(ed_in_block__n)
		ld b,a
		ld a,(G_B)
		sub b
		ld (G_B),a
		ld hl,(fw_sp)
		ld b,a
		ld a,(hl)
		and %10111111
		or $02
		inc b
		dec b
		jr nz,ed_in_block__nz
		or $40
ed_in_block__nz:		ld (hl),a
		jp fw_exit
ed_in_block__n:		db 0

; RST target, ABI 1: run of OUTIs. The site is one ED A3 in an unrolled
; block that ends in RET; the overlay replaces every ED A3 with RST + n,
; n = OUTIs from this one to the end of the block. The handler does the n
; OUTIs and returns to the RET after the block.
fw_outi_run:
		FASTENTRY		; A = n, fw_ret = site + 2
		ld b,a
		dec a
		add a,a
		ld hl,(fw_ret)
		add hl,a
		ld (fw_ret),hl		; the RET after the block
		ld a,(G_B)
		sub b
		ld (G_B),a
		push af
		call game_hl
		call out_block
		call set_game_hl
		pop af
		ld hl,(fw_sp)
		ld a,(hl)
		and %10111111
		or $02
		ld (hl),a
		ld a,(G_B)
		or a
		jr nz,fw_outi_run__nz
		set 6,(hl)
fw_outi_run__nz:		jp fw_exit

; HL = source in game memory, B = count (0 = 256), port = game C.
; Returns HL = source + count.
out_block:
		push hl
		push bc
		call game_class
		pop bc
		pop hl
		ld e,a
		cp 4
		jr nz,out_block__slow
		ld a,b
		dec a
		jr z,out_block__slow		; one byte: the plain data port write is cheaper
		ld a,(vdp_code)
		cp 3
		jp nz,vram_block
		jp cram_block
out_block__slow:		; byte by byte through the port's write routine
		push hl
		ld a,e
		call class_wr
		ld (out_block__call+1),hl
		pop hl
out_block__loop:		push bc
		push hl
		ld c,(hl)
out_block__call:		call 0
		pop hl
		pop bc
		inc hl
		djnz out_block__loop
		ret

; HL = source, B = count (0 = 256): CRAM writes at vdp_addr, then one
; update of the transparent value and fallback. Returns HL = source + count.
cram_block:
		xor a
		ld (vdp_latch),a
cram_block__l:		push bc
		ld c,(hl)
		push hl
		ld a,c
		ld (vdp_rbuf),a
		ld hl,(vdp_addr)
		push hl
		call cram_set
		pop hl
		inc hl
		res 6,h
		ld (vdp_addr),hl
		pop hl
		pop bc
		inc hl
		djnz cram_block__l
		push hl
		call fallback_update
		pop hl
		ret

; ======================================================================
; Frame and line interrupts. Hardware IM2 (I = $FD): the Next line
; interrupt arrives at $FD00, the ULA frame interrupt at $FD16.
; The line interrupt stands in for both SMS interrupts: it is scheduled at
; the end of SMS line k for each SMS line-counter event and at the end of
; line 192 for the frame event (ev_next). The framework's RETI
; acknowledges the Next interrupt and goes to the game's $0038 with
; interrupts off and the interrupted PC on the stack, as an SMS IRQ does;
; the ISR's own EI; RET or RETI returns to the game.
; ======================================================================
fw_line_irq:
		push af
		push hl
		push bc
		ld a,(hl_on)		; per-line H scroll from a hook table: the game's
		or a			; line interrupts are not delivered
		jr z,fw_line_irq__ev
		ld a,(ev_next)
		cp 192
		jr nc,fw_line_irq__frame
		ld a,192
		call ev_program
		jp fw_line_irq__noirq
fw_line_irq__ev:
fw_line_irq__hk2:		ds 3			; toppal: call pal_pic
		ld a,(ev_next)
		cp 192
		jr nc,fw_line_irq__frame
		; SMS line event at line A
		ld c,a
		ld a,1
		ld (line_pend),a
		xor a
		ld (fdone),a
		ld (vbl_done),a
		ld a,(vdp_regs+10)
		add a,c
		jr c,fw_line_irq__tofr
		inc a
		jr z,fw_line_irq__tofr
		cp 192
		jr nc,fw_line_irq__tofr
		ld b,a			; next event line
		call cur_line
		cp b
		jr c,fw_line_irq__ok		; still ahead
		inc a			; already passed: take it on the next line
		cp 192
		jr nc,fw_line_irq__tofr
		ld b,a
fw_line_irq__ok:		ld a,b
		jr fw_line_irq__set
fw_line_irq__tofr:		ld a,192
fw_line_irq__set:		call ev_program
		ld a,(vdp_regs+0)
		and $10			; IE1
		jr z,fw_line_irq__noirq
		ld hl,6			; a frame handler still runs (on the SMS it ends
		add hl,sp		; in the vertical blank, before any line event):
		ld (irq_s),hl		; the event waits for its end (isr_tramp)
		push de
		call frm_run
		pop de
		jr z,fw_line_irq__callgame
		ld a,1
		ld (line_held),a
		ld a,(irq_pend)		; isr_tramp in the slot if no frame event is held
		or a
		jr nz,fw_line_irq__noirq
		push de
		ld hl,(isr_sp)
		ld e,(hl)
		ld a,e
		cp 255&(isr_tramp)
		jr z,fw_line_irq__lh
		ld (hl),255&(isr_tramp)
		inc hl
		ld d,(hl)
		ld (hl),255&((isr_tramp)>>8)
		ld (isr_pc),de
fw_line_irq__lh:		pop de
		jr fw_line_irq__noirq
fw_line_irq__frame:
fw_line_irq__hk1:		ds 3			; toppal: call pal_vbl

		ld a,1
		ld (fdone),a
		xor a
		ld (vbl_done),a
		; first event of the next frame
		ld a,(hl_on)
		or a
		ld a,192
		jr nz,fw_line_irq__f2
		ld a,(vdp_regs+0)
		and $10
		ld a,192
		jr z,fw_line_irq__f2
		ld a,(vdp_regs+10)
		cp 192
		jr c,fw_line_irq__f2
		ld a,192
fw_line_irq__f2:		call ev_program
		pop bc
		pop hl
		pop af
		jp irq_frame		; status bit 7, and $0038 with IE0
fw_line_irq__noirq:		pop bc
		pop hl
		pop af
		ei
		reti
fw_line_irq__callgame:	; acknowledge the Next interrupt now and enter the game's $0038
		; with interrupts off and the interrupted PC on the stack, as the
		; SMS takes an IRQ: a game that leaves its ISR another way (R-Type
		; resets SP and jumps) must not leave the interrupt unacknowledged
		pop bc
		pop hl
		pop af
		push hl
		ld hl,$0038
		ex (sp),hl
mx_irq:		reti

; The frame event for the game, from fw_line_irq: game registers as
; interrupted, SP at the interrupted PC, the Next interrupt in service. Sets
; status bit 7 and, with IE0, enters $0038 as the SMS takes an interrupt.
; While the frame handler that the last frame event entered still runs (it
; turned interrupts on, and the Next is slower than the SMS: OutRun,
; Sonic) the event is held (irq_pend): the handler's return slot then gets
; isr_tramp in place of its return address (saved in isr_pc), and the held
; event goes in the moment the handler returns, as on the SMS the handler
; would have ended within its frame. Line events that come while a frame
; handler still runs wait there too (on the SMS the frame handler ends in
; the vertical blank, before any line event). "Still runs" (frm_run): SP is
; below that entry's return slot and the slot still holds what was put
; there; a handler that changes its return address (Ecco) or leaves by
; resetting SP (R-Type) counts as returned. An event held for 8 frames
; goes in anyway.
irq_frame:	ld (irq_s),sp
		push hl
		push af
		push de
		call frm_run
		jr z,irq_back
		ld a,(irq_pend)
		or a
		jr nz,irq_frame__again
		ld hl,(isr_sp)		; first hold: the return through isr_tramp
		ld e,(hl)
		inc hl
		ld d,(hl)
		ld hl,isr_tramp
		or a
		sbc hl,de
		jr z,irq_frame__lh	; a line event already holds it: isr_pc is the game's
		ld hl,(isr_sp)
		ld (hl),255&(isr_tramp)
		inc hl
		ld (hl),255&((isr_tramp)>>8)
		ld (isr_pc),de
irq_frame__lh:
		ld a,1
		ld (irq_pend),a
		jr irq_hold
irq_frame__again:		cp 8
		jr nc,irq_back		; held for 8 frames: give it anyway
		inc a
		ld (irq_pend),a
irq_hold:	pop de
		pop af
		pop hl
		ei
mx_irqh:	reti
irq_back:	pop de
irq_go:		xor a
		ld (irq_pend),a
		ld hl,vdp_status
		set 7,(hl)
		ld a,(vdp_regs+1)
		and $20			; IE0
		jr z,irq_flag
		ld hl,isr_n
		inc (hl)
		ld hl,(irq_s)
		call frm_rec
		pop af
		pop hl
		push hl
		ld hl,$0038
		ex (sp),hl
mx_irqf:	reti
irq_flag:	pop af			; IE0 off: the flag only
		pop hl
		ei
mx_irqo:	reti

; HL = return slot of a frame handler entry: remember it and its address
frm_rec:	ld (isr_sp),hl
		ld a,(hl)
		ld (isr_ret),a
		inc hl
		ld a,(hl)
		ld (isr_ret+1),a
		ret

; NZ when the frame handler entered last still runs: SP (irq_s) below its
; slot, and the slot still holds the address put there or isr_tramp.
; Uses A, HL, DE.
frm_run:	ld hl,(irq_s)
		ld de,(isr_sp)
		or a
		sbc hl,de
		jr nc,frm_run__no
		ex de,hl
		ld e,(hl)
		inc hl
		ld d,(hl)
		ld hl,(isr_ret)
		or a
		sbc hl,de
		jr z,frm_run__yes
		ld hl,isr_tramp
		or a
		sbc hl,de
		jr z,frm_run__yes
frm_run__no:		xor a
		ret
frm_run__yes:		or 1
		ret

; A frame handler with a held event returns here: a held frame event goes
; in now (then a held line event), else on to the saved return address.
; Interrupts off while deciding, then the game's IFF as it was.
isr_tramp:	push hl
		push af
		ld a,i
		di
		push af			; P/V = the game's IFF
		ld a,(irq_pend)
		or a
		jr nz,isr_tramp__frm
		ld a,(line_held)
		or a
		jr z,isr_tramp__ret
		pop af
		push af
		jp po,isr_tramp__ret		; the game's interrupts are off: it waits
		xor a
		ld (line_held),a
		ld a,(vdp_regs+0)
		and $10			; IE1
		jr z,isr_tramp__ret
		xor a			; a line entry
		jr isr_tramp__in
isr_tramp__frm:		pop af
		push af
		jp po,isr_tramp__ret
		xor a
		ld (irq_pend),a
		ld hl,vdp_status
		set 7,(hl)
		ld a,(vdp_regs+1)
		and $20			; IE0
		jr z,isr_tramp__ret
		ld hl,isr_n
		inc (hl)
		ld a,1
isr_tramp__in:		ld (isr_k),a		; 1: a frame entry
		pop af			; the handler starts with interrupts off
		pop af
		pop hl
		push hl			; the slot again, with the saved return address
		ld hl,(isr_pc)
		ex (sp),hl
		ld (isr_go),sp
		push af
		ld a,(isr_k)
		or a
		jr z,isr_tramp__go
		push hl
		ld hl,(isr_go)
		call frm_rec
		pop hl
isr_tramp__go:		pop af
		jp $0038
isr_tramp__ret:		pop af			; P/V = IFF
		ld hl,(isr_pc)
		jp po,isr_tramp__di
		pop af
		ex (sp),hl
		ei
		ret
isr_tramp__di:		pop af
		ex (sp),hl
		ret

; Register 0 (IE1) or 10 written: maybe a first line event (ev_recheck2, fw2)
ev_recheck:
		push de
		ld hl,ev_recheck2
		call fw2_call
		pop de
		ret

; Line-0 palette (overlay flag 2, toppal). On the SMS the frame handler's
; palette writes land in the vertical blank; on the Next they can land in
; the first lines of the next picture. The second tilemap, sprite and Layer
; 2 palettes hold the palette as the vertical blank leaves it (cram_x in
; fw2 writes them: every CRAM write from the frame event to the first line
; event, and later writes to entries that phase did not write). They are
; shown from the frame event (the end of line 192, so from line 0 on) to
; the first line event of the next frame, then the first palettes, which
; get every write, are shown again. Called from fw_line_irq (AF, HL, BC
; saved there).
pal_vbl:	ld hl,pal_vbl2		; in fw2 (fw_line_irq saved HL)
		jp fw2_call
pal_pic:	ld hl,pal_pic2
		jp fw2_call


; Name table marks for priority tiles, in MAP_PAGE: $1BC0 + row (the row
; may have priority cells), $1BE0 + row (the row has marked cells), $1C00 +
; cell (bit 0 marked: redraw it; bit 1: Layer 2 holds it). Only a cell
; that gets the priority bit, or that Layer 2 holds, is marked, so games
; that write the name table a lot pay little while no priority cell is on
; screen.
; pri_mark1: HL = name table offset o (0-$7FF), C = the byte written, from
; nt_put. Keeps HL, BC, DE.
pri_mark1:	nextreg $51,MAP_PAGE	; nt_put maps it again and puts slot 1 back
		push hl
		push de
		ld e,l			; bit 0: the entry's high byte
		srl h
		rr l			; cell = o >> 1
		ld a,h
		add a,$3C
		ld h,a			; HL = its mark
		bit 0,e
		jr z,pri_mark1__lo
		bit 4,c
		jr z,pri_mark1__lo
		set 0,(hl)		; the priority bit written
		call pri_rowp
		jr pri_mark1__x
pri_mark1__lo:		bit 1,(hl)		; else only a cell Layer 2 holds
		jr z,pri_mark1__x
		set 0,(hl)
		call pri_rowr
pri_mark1__x:		pop de
		pop hl
		ret
; HL = mark ($3C00 + cell): its row's flags, "marked" (pri_rowr) and also
; "has priority cells" (pri_rowp). Leaves HL = $3BE0 + row.
pri_rowp:	call pri_rowr
		ld a,l
		sub $20
		ld l,a
		ld (hl),1
		add a,$20
		ld l,a
		ret
pri_rowr:	ld a,h
		sub $3C
		ld h,a
		ld a,l
		and $E0
		or h
		rlca
		rlca
		rlca			; row = cell >> 5
		add a,$E0
		ld l,a
		ld h,$3B
		ld (hl),1
		ret
; pri_markr: DE = VRAM address, BC = count (1-256, in one 256-byte page),
; from nt_range: the shadow (already written) in slot 0, MAP_PAGE in slot 1.
; Keeps BC, DE.
pri_markr:	push bc
		push de
		ld hl,(nt_base)
		ex de,hl
		or a
		sbc hl,de		; o
		push hl
		add hl,bc
		dec hl
		srl h
		rr l			; last cell
		ex (sp),hl
		srl h
		rr l			; first cell
		pop de
		ex de,hl
		or a
		sbc hl,de
		ld b,l
		inc b			; cells
		ex de,hl		; HL = first cell
		push hl
		add hl,hl
		ld de,(nt_base)
		add hl,de
		inc hl
		ld a,h
		and $1F
		ld h,a
		push hl
		pop ix			; its high byte in the shadow (nt_range sets IX after)
		pop hl
		ld a,h
		add a,$3C
		ld h,a			; its mark
pri_markr__c:		bit 4,(ix+0)
		jr z,pri_markr__np
		set 0,(hl)
		push hl
		call pri_rowp
		pop hl
		jr pri_markr__n
pri_markr__np:		bit 1,(hl)
		jr z,pri_markr__n
		set 0,(hl)
		push hl
		call pri_rowr
		pop hl
pri_markr__n:		inc hl
		inc ix
		inc ix
		djnz pri_markr__c
		pop de
		pop bc
		ret

; A = SMS line k: next line interrupt at the end of line k
ev_program:
		ld (ev_next),a
		cp 192
		jr nz,ev_program__l
		ld a,(pic_end)		; the frame event: line 208 in 224-line mode
ev_program__l:		inc a			; (line events there are not moved: none used yet)
		nextreg $23,a
		ret

; A = current Next line (0-255; 255 for lines 255 and above)
cur_line:
		push bc
		ld bc,$243B
		ld a,$1E
		out (c),a
		inc b
		in a,(c)
		dec b
		rrca
		jr c,cur_line__big
		ld a,$1F
		out (c),a
		inc b
		in a,(c)
		pop bc
		ret
cur_line__big:		ld a,255
		pop bc
		ret

; ULA frame interrupt, line 248 of the 311-line frame: the framework's
; once-a-frame work. Pause becomes the SMS NMI: the RETI goes to $0066 with
; the interrupted PC on the stack (interrupts on during the NMI handler).
fw_ula_irq:
		push af
		push hl
		ld (irq_sp),sp
		ld sp,fw_stack_top
		push bc
		push de
		push ix
		push iy
		ld a,(vbl_done)
		or a
		call z,vbl_work
		pop iy
		pop ix
		pop de
		pop bc
		ld sp,(irq_sp)
		ld a,(quit_req)
		or a
		jp nz,fw_quit
		ld a,(pause_req)
		or a
		jr z,fw_ula_irq__out
		xor a
		ld (pause_req),a
		pop hl
		pop af
		push hl
		ld hl,$0066
		ex (sp),hl
		ei
		reti
fw_ula_irq__out:		pop hl
		pop af
		ei
mx_ula:		reti

; Once-a-frame work, interrupts off. Maps FW2 at $2000, the VRAM shadow at
; $4000-$7FFF and the Next tile definitions at $8000-$BFFF, calls fw2_vbl,
; then puts the game's pages back.
vbl_work:
		ld a,1
		ld (vbl_done),a
		nextreg $51,FW2_PAGE
		nextreg $52,SHADOW_PAGE
		nextreg $53,SHADOW_PAGE+1
		nextreg $54,TILE_PAGE
		nextreg $55,TILE_PAGE+1
		call fw2_vbl
restore_mmu:	ld a,(cur_mmu+0)
		nextreg $50,a
		ld a,(cur_mmu+1)
		nextreg $51,a
		ld a,(cur_mmu+2)
		nextreg $52,a
		ld a,(cur_mmu+3)
		nextreg $53,a
		ld a,(cur_mmu+4)
		nextreg $54,a
		ld a,(cur_mmu+5)
		nextreg $55,a
		ld a,(cur_mmu+6)
		nextreg $56,a
		ret

; ======================================================================
; LD (DE),A with Sega mapper decode. RST target, one-byte site.
; ======================================================================
fw_ld_de_a:
		ex (sp),hl
		push af
		ld a,i
		di
		ld a,$00
		jp po,fw_ld_de_a__di
		ld a,$FB
fw_ld_de_a__di:		ld (exit_ei),a
		pop af			; game_a only with interrupts off (FASTENTRY)
		ld (game_a),a
		push af
		ld (fw_ret),hl
		ld (fw_sp),sp
		ld sp,fw_stack_top
		push bc
		push de
		ld a,(game_a)
		ld (de),a
		ld c,a
		ld a,d
		inc a
		jr nz,fw_ld_de_a__done		; D != $FF
		ld a,e
		cp $FD
		jr c,fw_ld_de_a__done		; below $FFFD ($FFFC: cart RAM, ignored)
		sub $FD			; 0,1,2 = slot pair
		add a,a			; first MMU slot
		ld e,a
		ld a,c			; bank
		call map_bank
fw_ld_de_a__done:		jp fw_exit

; Mapper stores (ops $10-$17 and $20-$3F): cold_mapper in fw2 does them,
; with FW2 mapped at $2000 for the call (A = op).
; The site's inline byte n is read here: with FW2 at $2000 a site in
; $2000-$3FFF would read FW2 instead of the game's code.
op_mapper:
		ld hl,(fw_ret)
		push af
		ld a,(hl)
		ld (op_n),a
		inc hl			; and the next instruction after a 3-byte site
		ld de,op_nx
		ld bc,3
		ldir
		pop af
		ld hl,cold_mapper
		call fw2_call
		jp fw_exit

; HL = routine in fw2: call it with FW2 mapped at $2000 (MMU1), then put the
; game's page back. Not for use inside vbl_work. Keeps A from the routine
; only in F (A is used to restore MMU1).
fw2_call:
		nextreg $51,FW2_PAGE
		call call_hl
		push af
		ld a,(cur_mmu+1)
		nextreg $51,a
		pop af
		ret

; E = first MMU slot (0, 2, 4), A = 16K bank. Maps 2 pages, keeps cur_mmu.
; Slot 2 stays cart RAM while $FFFC bit 3 is set.
map_bank:
		ld b,a
		ld a,e
		cp 4
		ld a,($FFFC)
		jr nz,map_bank__rom
		and 8
		ret nz
map_bank__rom:		ld a,b
map_bank_rom:
		add a,a
		ld b,a
		ld a,(fw_npages)
		ld c,a
		ld a,b
		call mod_c
		ld b,a
		ld d,0
		ld hl,cur_mmu
		add hl,de
		add a,CART_PAGE
		ld (hl),a
		ld a,e
		add a,$50
		call nr_write_sel
		ld a,(hl)
		call nr_write_val
		inc b
		ld a,b
		call mod_c
		inc hl
		add a,CART_PAGE
		ld (hl),a
		ld a,e
		add a,$51
		call nr_write_sel
		ld a,(hl)
		call nr_write_val
		ret

; A = A mod C (C > 0)
mod_c:
mod_c__l:		cp c
		ret c
		sub c
		jr mod_c__l

nr_write_sel:
		push bc
		ld bc,$243B
		out (c),a
		pop bc
		ret
nr_write_val:
		push bc
		ld bc,$253B
		out (c),a
		pop bc
		ret
; A = NextReg A
nr_read:
		push bc
		ld bc,$243B
		out (c),a
		inc b
		in a,(c)
		pop bc
		ret

; ======================================================================
; Port reads (A = result)
; ======================================================================
rd_ff:		ld a,$FF
		ret
rd_hcount:	ld a,$80
		ret
rd_dd:		ld a,$FF
		ret

; $DC: Kempston / Mega Drive pad on port $1F, ANDed with the keyboard.
rd_dc:
		in a,($1F)
		and $3F
		add a,255&(joy_table)
		ld l,a
		ld h,255&((joy_table)>>8)
		ld a,(kbd_dc)
		and (hl)
		ret

; V counter from the Next active line ($1E/$1F). Line 0 is the first line
; of the 256x192 area, as on the SMS. Lines above $F2 jump back like the
; PAL SMS counter, to $BC (the last line read here is 310; the PAL SMS has
; 313 lines; the count reaches $FF on the last line, which games wait
; for: Micro Machines). A game that
; polls the counter also gets
; the once-a-frame work done here when interrupts never deliver it.
rd_vcount:
		ld bc,$243B
		ld a,$1E
		out (c),a
		inc b
		in d,(c)
		dec b
		ld a,$1F
		out (c),a
		inc b
		in a,(c)
		ld e,a
		bit 0,d
		jr nz,rd_vcount__vbl
		ld hl,pic_end
		cp (hl)
		jr c,rd_vcount__active
		ld c,(hl)
		inc c
		inc c
		cp c
		jr c,rd_vcount__ret
rd_vcount__vbl:		ld a,(vbl_done)
		or a
		jr nz,rd_vcount__ret
		push de
		push ix
		push iy
		call vbl_work
		pop iy
		pop ix
		pop de
		jr rd_vcount__ret
rd_vcount__active:	xor a
		ld (vbl_done),a
		ld (fdone),a
rd_vcount__ret:		ld a,(m224)
		or a
		jr nz,rd_vcount__v224
		ld a,e
		bit 0,d
		jr nz,rd_vcount__hi
		cp $F3
		ret c
rd_vcount__hi:		sub 55			; $F3 -> $BC ... line 310, the last one read here, -> $FF
					; (the PAL SMS count has 313 lines: $BA and $BB are left
					; out so that games waiting for $FF see it)
		ret
rd_vcount__v224:		; 224-line mode: SMS line = Next line + 16; the PAL count runs
		; $00-$FF, $00-$02, then from $CC (not $CA: 311 lines here) to $FF
		ld a,e
		bit 0,d
		jr nz,rd_vcount__h2
		cp 240
		jr nc,rd_vcount__m2
		add a,16
		ret
rd_vcount__m2:		cp 243
		jr nc,rd_vcount__m3
		sub 240
		ret
rd_vcount__m3:		add a,$CC-243
		ret
rd_vcount__h2:		cp 295-256
		jr nc,rd_vcount__top
		add a,$CC+13
		ret
rd_vcount__top:		sub 295-256
		ret

; Status: bit 7 frame, bit 5 sprite collision; reading clears them and the
; line interrupt flag. A game that polls with interrupts off gets bit 7
; once a frame from the line number.
rd_status:
		xor a
		ld (vdp_latch),a
		ld (line_pend),a
		call cur_line
		ld hl,pic_end
		cp (hl)
		jr c,rd_status__active
		jr z,rd_status__read
		ld a,(fdone)
		or a
		jr nz,rd_status__read
		inc a
		ld (fdone),a
		ld hl,vdp_status
		set 7,(hl)
		jr rd_status__read
rd_status__active:	xor a
		ld (fdone),a
rd_status__read:		ld a,(vdp_status)
		ld b,a
		and $1F
		ld (vdp_status),a
		ld a,b
		ret

rd_vdata:
		xor a
		ld (vdp_latch),a
		ld a,(vdp_rbuf)
		push af
		call vram_read_ahead
		pop af
		ret

; rbuf = VRAM[addr], addr++
vram_read_ahead:
		ld hl,(vdp_addr)
		ld a,h
		rlca
		rlca
		rlca
		and 1
		add a,SHADOW_PAGE
		nextreg $50,a
		ld a,h
		and $1F
		ld d,a
		ld e,l
		ld a,(de)
		ld (vdp_rbuf),a
		ld a,(cur_mmu+0)
		nextreg $50,a
		inc hl
		res 6,h
		ld (vdp_addr),hl
		ret

; ======================================================================
; VDP writes (C = value)
; ======================================================================
vctrl_w:
		ld hl,vdp_latch
		ld a,(hl)
		or a
		jr nz,vctrl_w__second
		inc (hl)
		ld a,c
		ld (vdp_addr),a		; first byte: address low at once
		ret
vctrl_w__second:	ld (hl),0
		ld a,c
		and $3F
		ld (vdp_addr+1),a
		ld a,c
		rlca
		rlca
		and 3
		ld (vdp_code),a
		cp 2
		jr z,vctrl_w__reg
		or a
		ret nz
		jp vram_read_ahead
vctrl_w__reg:		ld a,c
		and $0F
		ld c,a
		ld a,(vdp_addr)
		jp vdp_reg_w

vdata_w:
		xor a
		ld (vdp_latch),a
		ld a,c
		ld (vdp_rbuf),a
		ld hl,(vdp_addr)
		ld a,(vdp_code)
		cp 3
		jr z,vdata_w__cram
		call vram_put
vdata_w__inc:		inc hl
		res 6,h
		ld (vdp_addr),hl
		ret
vdata_w__cram:		push hl
		call cram_write
		pop hl
		jr vdata_w__inc

; HL = VRAM address, C = value. Writes the shadow, then marks the tile
; page dirty, or writes the Next map entries, or flags the sprite table.
; Keeps HL.
vram_put:
		ld a,h
		rlca
		rlca
		rlca
		and 1
		add a,SHADOW_PAGE
		nextreg $50,a
		ld a,h
		and $1F
		ld d,a
		ld e,l
		ld a,c
		ld (de),a
		ld a,(cur_mmu+0)
		nextreg $50,a
		ld e,h
		ld d,255&((region_tab)>>8)
		ld a,(de)
		or a
		jr nz,vram_put__nt
vram_put__dirty:		set 6,e			; dirty_pages: the tile's bit
		push de
		ld e,l
		ld a,l
		call tmask
		pop de
		ex de,hl
		or (hl)
		ld (hl),a
		ex de,hl
		ld (tiles_dirty),a
		ret
vram_put__nt:		dec a
		jp z,nt_put
		dec a
		jr nz,vram_put__both
		ld a,1
		ld (sat_dirty),a
		ld a,l			; bytes $40-$7F of the sprite table page are
		and $C0			; unused by the VDP and can hold tiles 506-507
		cp $40
		ret nz
		jr vram_put__dirty
vram_put__both:		; 3: name table rows 24-27, which games also use for tiles
		call nt_put
		ld e,h
		ld d,255&((region_tab)>>8)
		jr vram_put__dirty

; E = first byte, A = last byte (offsets in a 256-byte page) -> A = the
; dirty_pages bits of the tiles they cover. Uses C.
tmask:		push hl
		rlca
		rlca
		rlca
		and 7
		ld hl,tm_hi
		add hl,a
		ld c,(hl)
		ld a,e
		rlca
		rlca
		rlca
		and 7
		ld hl,tm_lo
		add hl,a
		ld a,(hl)
		and c
		pop hl
		ret

; HL = VRAM address inside the name table, C = value. Writes the entry
; byte into M0 and A8 (two or four places). Keeps HL.
nt_put:
		push hl
		ld de,(nt_base)
		or a
		sbc hl,de		; o = 0..$6FF
nt_put__hk:		ds 3			; priority tiles: call pri_mark1
		ld a,l
		rrca
		and 31
		ld b,a			; SMS column
		bit 0,l
		jr z,nt_put__even
		ld e,c
		ld d,255&((mapattr_table)>>8)
		ld a,(de)
		ld c,a
nt_put__even:		ld a,l
		rlca
		rlca
		and 3
		ld e,a
		ld a,h
		add a,a
		add a,a
		or e			; row 0..27
		ld e,a
		ld d,16
		mul d,e			; row * 16
		add hl,de		; Next offset in M0 = o + row * 16
		ld a,MAP_PAGE
		nextreg $51,a
		set 5,h
		ld (hl),c
		ld a,b
		cp 8
		jr nc,nt_put__hi
		ld de,64		; SMS 0-7 also in M0 columns 32-39
		add hl,de
		ld (hl),c
		ld de,MAP_A8-16		; A8 columns 24-31
		add hl,de
		ld (hl),c
		ld de,16		; and A8 columns 32-39
		add hl,de
		ld (hl),c
		jr nt_put__done
nt_put__hi:		ld de,MAP_A8-16		; A8 column = SMS column - 8
		add hl,de
		ld (hl),c
nt_put__done:		ld a,(cur_mmu+1)
		nextreg $51,a
		pop hl
		ret

; HL = source in game memory, B = count (0 = 256): VRAM writes at vdp_addr.
; Copies into the shadow in pieces that stay inside one 8K shadow page,
; through slot 3 when the source is in $0000-$1FFF and slot 0 otherwise,
; then handles the name table, tile and sprite table parts of the range.
; Returns HL = source + count.
vram_block:
		push ix
		xor a
		ld (vdp_latch),a
		ld c,b
		ld b,0
		ld a,c
		or a
		jr nz,vram_block__n
		inc b			; BC = 256
vram_block__n:		ld (blk_cnt),bc
		ld de,(vdp_addr)
		ld (blk_start),de
		ld a,h
		cp $20
		ld a,$50		; slot 0 register
		ld ix,$0000
		jr nc,vram_block__slot
		ld a,$53		; slot 3 register
		ld ix,$6000
vram_block__slot:		ld (blk_nr),a
vram_block__chunk:		; DE = VRAM address, BC = left, HL = source
		push bc
		push hl
		ld a,(blk_nr)
		call nr_write_sel
		ld a,d
		rlca
		rlca
		rlca
		and 1
		add a,SHADOW_PAGE
		call nr_write_val
		; room = $2000 - (DE & $1FFF)
		ld a,d
		and $1F
		ld h,a
		ld l,e
		push hl			; offset in page
		ex de,hl
		ld hl,$2000
		or a
		sbc hl,de		; room
		pop de			; offset
		push ix
		ex (sp),hl		; HL = slot base, room on stack
		add hl,de
		ex de,hl		; DE = destination
		pop hl			; room
		pop ix			; IX = source (was HL)
		pop bc			; left
		push bc
		or a
		sbc hl,bc		; room - left
		jr nc,vram_block__all		; all of it fits
		add hl,bc		; HL = room
		ld b,h
		ld c,l
vram_block__all:		; BC = this piece
		push bc
		push ix
		pop hl			; source
		ldir
		dec hl
		ld a,(hl)
		ld (vdp_rbuf),a		; each write loads the read buffer
		inc hl
		ex de,hl		; DE = source after
		pop bc			; piece
		ld hl,(vdp_addr)
		add hl,bc
		res 6,h
		ld (vdp_addr),hl
		pop hl			; left
		or a
		sbc hl,bc
		ld b,h
		ld c,l
		ex de,hl		; HL = source
		ld de,(vdp_addr)
		ld a,(blk_nr)
		cp $50
		ld ix,$0000
		jr z,vram_block__ix
		ld ix,$6000
vram_block__ix:		ld a,b
		or c
		jr nz,vram_block__chunk
		; put the slot back
		ld a,(blk_nr)
		sub $50
		add a,255&(cur_mmu)
		ld e,a
		ld d,255&((cur_mmu)>>8)
		ld a,(blk_nr)
		call nr_write_sel
		ld a,(de)
		call nr_write_val
		push hl
		; regions of [blk_start, blk_start + blk_cnt)
		ld de,(blk_start)
		ld bc,(blk_cnt)
vram_block__seg:		ld a,e
		neg			; 256 - E (0 means 256)
		ld l,a
		ld h,0
		or a
		jr nz,vram_block__s1
		inc h
vram_block__s1:		; HL = room in this 256-byte page; piece = min(room, left)
		push hl
		or a
		sbc hl,bc
		pop hl
		jr c,vram_block__s2
		ld h,b
		ld l,c
vram_block__s2:		push bc
		push hl			; piece
		ld l,d
		ld h,255&((region_tab)>>8)
		ld a,(hl)
		or a
		jr nz,vram_block__s3
vram_block__st:		set 6,l			; tile page: the tiles of [E, E+piece) dirty
		pop bc			; piece
		push bc
		push bc
		ld a,e
		add a,c
		dec a
		call tmask
		pop bc
		or (hl)
		ld (hl),a
		ld (tiles_dirty),a
		jr vram_block__s5
vram_block__s3:		dec a
		jr z,vram_block__s4
		dec a
		jr z,vram_block__s3s
		pop bc			; 3: name table rows 24-27 and tiles
		push bc
		push hl
		call nt_range
		pop hl
		jr vram_block__st
vram_block__s3s:		ld a,1
		ld (sat_dirty),a
		; tiles in the unused bytes $40-$7F: start < $80 and end > $40
		ld a,e
		cp $80
		jr nc,vram_block__s5
		pop bc			; piece
		push bc
		push hl
		ld h,0
		ld l,e
		add hl,bc		; end (exclusive)
		ld a,h
		or a
		jr nz,vram_block__s3d
		ld a,l
		cp $41
		jr c,vram_block__s3n
vram_block__s3d:		ld l,d
		ld h,255&((region_tab)>>8)
		set 6,l
		ld a,(hl)
		or $0C			; tiles 2 and 3 of the page
		ld (hl),a
		ld (tiles_dirty),a
vram_block__s3n:		pop hl
		jr vram_block__s5
vram_block__s4:		pop bc
		push bc
		call nt_range		; DE = start, BC = count
vram_block__s5:		pop bc			; piece
		ex de,hl
		add hl,bc
		res 6,h
		ex de,hl
		pop hl			; left
		or a
		sbc hl,bc
		ld b,h
		ld c,l
		ld a,b
		or c
		jr nz,vram_block__seg
		pop hl
		pop ix
		ret

; DE = VRAM address in the name table, BC = count (1-256, inside one
; 256-byte page): writes those bytes from the shadow into the Next maps,
; as nt_put does, with the shadow page in slot 0 and MAP_PAGE in slot 1.
; IX walks M0, IY walks A8 (A8 = M0 + MAP_A8 - 16 for SMS columns 8-31;
; columns 0-7 also go to M0 + 64, A8 + 48 and A8 + 64). Keeps DE.
nt_range:
		push de
		push ix
		push iy
		ld a,d
		rlca
		rlca
		rlca
		and 1
		add a,SHADOW_PAGE
		nextreg $50,a
		nextreg $51,MAP_PAGE
nt_range__hk:		ds 3			; priority tiles: call pri_markr
		ld b,c			; count, 0 = 256
		ld c,e			; VRAM address low = name table offset low
		ld hl,(nt_base)
		ex de,hl
		or a
		sbc hl,de		; o = 0..$6FF
		push hl
		add hl,hl
		add hl,hl		; H = o >> 6 = row
		ld e,h
		ld d,16
		mul d,e
		pop hl
		add hl,de
		ld de,$2000
		add hl,de
		push hl
		pop ix			; M0 position
		ld de,MAP_A8-16
		add hl,de
		push hl
		pop iy			; A8 position
		ld hl,4
		add hl,sp
		ld e,(hl)		; the VRAM address again (pushed first)
		inc hl
		ld d,(hl)
		ld a,d
		and $1F
		ld d,a			; source in slot 0
nt_range__l:		ld a,(de)
		bit 0,c
		jr z,nt_range__ev
		ld (nt_range__t+1),a
nt_range__t:		ld a,(mapattr_table)	; attribute byte
nt_range__ev:		ld (ix+0),a
		bit 4,c
		jr nz,nt_range__hi
		bit 5,c
		jr nz,nt_range__hi
		ld (ix+64),a		; SMS columns 0-7: M0 32-39, A8 24-31, A8 32-39
		ld (iy+64),a
		ld (iy+80),a
		jr nt_range__nx
nt_range__hi:		ld (iy+0),a
nt_range__nx:		inc de
		inc ix
		inc iy
		inc c
		ld a,c
		and $3F
		jr nz,nt_range__same
		push bc			; next row: the Next maps have 16 more bytes
		ld bc,16
		add ix,bc
		add iy,bc
		pop bc
nt_range__same:		djnz nt_range__l
		ld a,(cur_mmu+0)
		nextreg $50,a
		ld a,(cur_mmu+1)
		nextreg $51,a
		pop iy
		pop ix
		pop de
		ret

blk_cnt:	dw 0
blk_start:	dw 0
blk_nr:		db 0

; L = address (low 5 bits = CRAM index), C = colour. Tilemap palette entry
; index; entries 16-31 also go to the sprite palette (entries 0-15).
cram_write:
		call cram_set
		jp fallback_update
; As cram_write, without the transparent value and fallback update
cram_set:
		ld a,l
		and $1F
		ld e,a
		ld d,0
		ld hl,cram
		add hl,de
		ld a,c
		and $3F
		ld (hl),a
		ld c,a
		ld a,(pal43)		; display bits (second ULA palette active)
		or %00110000		; write the first tilemap palette
		nextreg $43,a
		ld a,e
		nextreg $40,a
		call pal_out
		ld a,e
		cp 16
		jr c,cram_hk
		ld a,(pal43)
		or %00100000		; first sprite palette
		nextreg $43,a
		ld a,e
		sub 16
		nextreg $40,a
		call pal_out
cram_hk:	ret			; NOP with priority tiles or toppal: cram_x (fw2)
		ld hl,cram_x		; also writes the Layer 2 and second palettes
		jp fw2_call
; C = SMS colour: two writes to NextReg $44
pal_out:	ld a,c
		add a,255&(pal_hi_table)
		ld l,a
		ld h,255&((pal_hi_table)>>8)
		ld a,(hl)
		nextreg $44,a
		ld a,c
		add a,255&(pal_lo_table)
		ld l,a
		ld h,255&((pal_lo_table)>>8)
		ld a,(hl)
		nextreg $44,a
		ret

; Transparent pixel value, fallback colour and backdrop: fallback2 in fw2
; (for handlers; code in fw2 and fw3 calls fallback2 itself)
fallback_update:
		ld hl,fallback2
		jp fw2_call

; The display enable (register 1 bit 6) to the tilemap and sprites (disp_on;
; fallback2 and l2_vis follow disp_on). Uses A, B, C.
r1_hw:		ld a,(vdp_regs+1)
		and $40
		ld (disp_on),a
		ld a,%10000011		; tilemap on, 512 tiles, over the ULA
		ld b,%01100011		; sprites on, over border, clip, sprite 0 on top
		jr nz,r1_hw__b
		ld a,%00000010
		ld b,%01100010
r1_hw__b:		ld (tm_ctl),a
		ld c,a
		ld a,(pal43)		; bit 3: toppal shows the second palettes
		and 8
		add a,a
		or c
		nextreg $6B,a
		ld a,(lay15)		; layer order (Layer 2 on top with priority tiles)
		or b
		nextreg $15,a
		ret

; C = register, A = value
vdp_reg_w:
		ld e,a
		ld b,0
		ld hl,vdp_regs
		add hl,bc
		ld d,(hl)		; old value
		ld (hl),e
		ld a,c
		or a
		jp z,vdp_reg_w__r0
		dec a
		jp z,vdp_reg_w__r1
		dec a
		jp z,vdp_reg_w__r2
		sub 3
		jp z,vdp_reg_w__r5
		dec a
		jp z,vdp_reg_w__r6
		dec a
		jp z,fallback_update	; 7
		dec a
		jp z,hscroll_set	; 8
		dec a
		jp z,vdp_reg_w__r9
		dec a
		ret nz
		jp ev_recheck		; 10
vdp_reg_w__r0:		ld a,e
		xor d
		and $28			; mask column 0, sprite shift
		ld a,1
		jr z,vdp_reg_w__r0b
		ld (sat_dirty),a
		push de
		ld hl,clip_update
		call fw2_call
		pop de
vdp_reg_w__r0b:		ld a,e
		xor d
		and $02			; M2: 224-line mode with register 1 bit 4
		call nz,vdp_reg_w__mode_check
		ld a,e
		xor d
		and $10			; IE1
		call nz,ev_recheck
		ld a,e
		xor d
		and $C0			; lock bits
		ret z
		ld a,1
		ld (cop_dirty),a
		ret
vdp_reg_w__r1:		ld a,1
		ld (sat_dirty),a
		ld a,e
		and $40
		jr nz,vdp_reg_w__r1on
		ld a,(fw_flags)		; display off in the vertical blank phase (toppal):
		and 2			; on the SMS the frame handler turns it on again
		jr z,vdp_reg_w__r1off		; before line 0. Kept on; pal_pic2 or pal_vbl2
		ld a,(pal_ph)		; turns it off if it is still off then.
		or a
		jr z,vdp_reg_w__r1off
		ld (dis_pend),a
		jr vdp_reg_w__r1m
vdp_reg_w__r1on:		xor a
		ld (dis_pend),a
vdp_reg_w__r1off:		push de
		call r1_hw
		call fallback_update
		ld hl,l2_vis		; Layer 2 on or off with the display
		call fw2_call
		pop de
vdp_reg_w__r1m:		ld a,e
		xor d
		and $10			; M1: 224-line mode with register 0 bit 1
		ret z
vdp_reg_w__mode_check:	push de
		ld hl,mode_switch
		call fw2_call
		pop de
		ret
vdp_reg_w__r2:		ld hl,nt_base_set
		jp fw2_call
vdp_reg_w__r5:		ld a,e
		and $7E
		rrca
		ld (sat_hi),a		; (reg5 & $7E) << 7, high byte
		ld a,1
		ld (sat_dirty),a
		ld hl,region_update
		jp fw2_call
vdp_reg_w__r6:		ld a,1
		ld (sat_dirty),a
		ret
vdp_reg_w__r8:		jp hscroll_set
vdp_reg_w__r9:		ld a,1
		ld (cop_dirty),a
		ret

; Horizontal scroll, register 8 = E. The whole screen scrolls by one
; value (per-line scroll is not done). K = -h mod 256 is the first SMS map
; pixel shown at SMS x = 0; the tilemap X offset is K - 34 (34 = left
; border + PIC_X). When K > 64 the 320-pixel Next map would wrap in the
; middle of the line, so the copper switches to map A8 between SMS x
; 256-K and 320-K, at copper column (288 - K) / 8.
hscroll_set:
		ld a,(hl_on)		; the hook's table sets every line
		or a
		ret nz
		ld a,e
		neg			; K
		ld e,a
		sub 2
		ld (pri_x),a		; Layer 2 X: map column K at SMS x 0 (PIC_X = 2)
		ld d,0
		ld hl,-34
		add hl,de
		bit 7,h
		jr z,hscroll_set__pos
		ld de,320
		add hl,de
hscroll_set__pos:		ld (h_x),hl
		; With line interrupts off no game can time a write to a line, and
		; a write that lands in the picture (handlers are slower than the
		; SMS, so a vblank write can run late) would tear it. The copper
		; then sets X at line 0 (or after the locked rows) from the next
		; frame on, together with the map switch column.
		ld a,(vdp_regs+0)
		and $10
		jr nz,hscroll_set__lineint
		ld a,1
		ld (cop_dirty),a
		jr hscroll_set__nodir
hscroll_set__lineint:	ld a,(vdp_regs+0)
		and $40
		jr z,hscroll_set__direct
		; register 0 bit 6: lines 0-15 keep X for H = 0; the copper sets h_x
		; after line 15. Direct only while the beam is in lines 16-191.
		ld a,1
		ld (cop_dirty),a
		call cur_line
		cp 16
		jr c,hscroll_set__nodir
		cp 192
		jr nc,hscroll_set__nodir
hscroll_set__direct:	ld a,h
		nextreg $2F,a
		ld a,l
		nextreg $30,a
		ld a,(pri_x)
		nextreg $16,a
hscroll_set__nodir:
		ld a,(vdp_regs+8)
		neg
		cp 65
		ld b,0
		jr c,hscroll_set__sw		; K <= 64: no switch
		; M0 and A8 show the same pixels at SMS x 256-K to 320-K; the
		; switch at column c acts at SMS x 8c (MAME). c = (291 - K) / 8
		; puts 8c + K in 284-291, near the middle (288), so a switch that
		; lands up to 29 pixels later or 28 earlier still looks right
		; (the real Next's copper and tile fetch timing is not MAME's).
		ld b,a
		ld a,255&((291-256))	; 291 - K (K > 64, so it fits in a byte)
		sub b
		rrca
		rrca
		rrca
		and $1F
		ld b,a
hscroll_set__sw:		ld a,b
		ld (h_sw),a
		ld hl,cop_sw
		cp (hl)
		ret z
		ld a,1
		ld (cop_dirty),a
		ret

; ======================================================================
; PSG (SN76489) -> AY. C = byte written to the PSG.
; Tone channels 0-2 -> AY 0 channels A-C. Noise -> AY 1 channel A: white
; noise on the AY noise generator, periodic noise as a tone at the
; periodic noise's pitch. Latch/data protocol as SMS Power describes it:
; the latch is never cleared by a data byte, tone registers change at once.
; ======================================================================
psg_w:		ld hl,psg_w2		; the PSG code is in fw2
		jp fw2_call

; A = chip ($FF AY 0, $FE AY 1), E = register, D = value
ay_write:
		ld bc,$FFFD
		ld hl,ay_cur
		cp (hl)
		jr z,ay_write__same
		ld (hl),a
		out (c),a
ay_write__same:		out (c),e
		ld b,$BF
		out (c),d
		ret

; ======================================================================
; Fatal stop: red border, interrupts off.
; ======================================================================
fw_fatal:
		di
		ld a,2
		out ($FE),a
fw_fatal__h:		jr fw_fatal__h

; ======================================================================
; Leave the game (BREAK): put NextZXOS's pages and registers back and go
; to the loader's browser. Entered from the vblank interrupt with the
; game's stack; never returns to the game.
; ======================================================================
fw_quit:
		di
		ld sp,fw_stack_top
		nextreg $51,FW2_PAGE
		call fw_quit2		; fw2: all but slots 0 and 1
		nextreg $50,$FF
		nextreg $51,$FF
		; MMU7 stays the framework until the loader runs (it maps page 1)
		ld a,$3F
		ld i,a
		im 1
		jp fw_resume

; ======================================================================
; Start the game. Called by the loader (via the jump table) with:
;   cart pages loaded at CART_PAGE.., fw_npages, fw_start_addr set,
;   patch applied, NextZXOS's pages saved, nr_saved filled.
; Never returns.
; ======================================================================
fw_start:
		di
		ld sp,fw_stack_top
		nextreg $51,FW2_PAGE	; the set-up is in fw2 (fw2_start)
		call fw2_start
		call restore_mmu
		; the SMS RAM copy of the mapper registers holds the reset values
		; too: games write them with stores the overlay does not patch,
		; and read them back (R-Type restores both banks from $DFFE)
		ld hl,$0000
		ld ($DFFC),hl
		ld hl,$0201
		ld ($DFFE),hl
		ld sp,(fw_start_sp)
		im 2
		ld hl,(fw_start_addr)
		push hl
		xor a
		ld b,a
		ld c,a
		ld d,a
		ld e,a
		ld h,a
		ld l,a
		ret			; to the game's start address


fw_code_end:
; assert fw_code_end <= $FD00, "framework code overflows into the IM2 table" (checked by tools/check-layout)

; Hardware IM2 mode gives only the vectors of the interrupts turned on:
; $00 (line) and $16 (ULA). The other entries up to $16 read $FEFE.
; $FD18-$FEF7 holds trace code (trace.asm).
		defs ($FD00)-0xE000-$
im2_table:	dw fw_line_irq		; line interrupt: vector $00
		ds 20,$FE
		dw fw_ula_irq		; ULA interrupt: vector $16
		defs ($FEFE)-0xE000-$
		ei
		reti
; assert tr_tg >= TR_DBUF + TR_DLIM && tr_fx >= tr_tg + TR_NT*4 && tr_fx + TR_NT*4 <= $FFFC, "trace buffers overlap" (checked by tools/check-layout)
; assert $ <= $FFFC, "framework overflows the mapper registers" (checked by tools/check-layout)
