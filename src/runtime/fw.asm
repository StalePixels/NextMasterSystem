; fw.asm: NextMasterSystem resident framework. Lives in 8K page FW_PAGE, mapped
; at $E000-$FFFF (MMU7) while the game runs. The game reaches it through
; RST vectors that the overlay points at the jump table below. The other
; framework pages are mapped only while they run: fw2.asm (FW2_PAGE, at
; $2000: the once-a-frame work, VDP register writes, mapper stores),
; fw3.asm (FW3_PAGE, at $0000 inside the once-a-frame work) and fw4.asm
; (FW4_PAGE, at $2000: game start and quit, the PSG, the trace builder).
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
FW_ABI		equ 7			; 6: code pages (far call, jt_far, jt_peek); 7: jt_vwrite
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

; ---- jump table, second part (ABI 6). Entries never move. ----
jt_far:		jp fw_far		; $E072 far call into a code page (CALL + inline page, entry)
jt_peek:	jp fw_peek		; $E075 for page code: A = the byte the game sees at HL
jt_vwrite:	jp fw_vwrite		; $E078 for page code: write bytes into VRAM (ABI 7)

; ---- other state ----
game_a:		db 0
fw_sp:		dw 0			; game SP while a handler runs
fw_ret:		dw 0			; game return address while a handler runs
irq_sp:		dw 0			; game SP while the vblank interrupt runs
tiles_dirty:	db 0			; some page in dirty_pages is set
tw_cnt:		dw 0			; bytes written to tiles since their last conversion
sat_dirty:	db 1			; sprites must be rebuilt
vbl_done:	db 0			; vblank work done for this frame
vbl_poll:	db 0			; a V counter read did it since the last ULA interrupt
vbl_arm:	db 0			; frame events left that arm vbl_chk
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
io_ctl:		db $FF			; last write to port $3F (I/O control: TH/TR direction and level)
pause_req:	db 0			; Pause pressed: emulate the NMI
quit_req:	db 0			; BREAK pressed: back to the browser
tr_free:	dw $FFFF		; pixel values no sprite-palette tile on screen uses
; overlay switches (header flags): bit 0 priority tiles in Layer 2 (fw2
; pri_frame), bit 1 line-0 palette (toppal: cram_x in fw2, pal_vbl here),
; bit 2 tiles from cart ROM (tilecache: kn_entry here, kn_block in fw2),
; bit 3 the game sets the video rate (hz=50 or hz=60), bit 4 60 Hz (hz_setup
; in fw3)
fw_flags:	db 0
pal43:		db %00000010		; NextReg $43 display bits: ULA second; bits 3 and 2
					; (second sprite and Layer 2 palettes) while toppal shows them
isr_sp:		dw 0			; return slot of the last frame handler entry
isr_ret:	dw 0			; the address the entry put in it
isr_pc:		dw 0			; that address while isr_tramp holds the slot
isr_k:		db 0
line_held:	db 0			; a line event waits for a frame handler's end
isr_go:		dw 0
irq_s:		dw 0
irq_pend:	db 0			; a frame event is held (irq_frame)
far_p:		db 0			; far call: the file's page number
far_e:		db 0			; far call: the entry number
far_prev:	db 0			; far call: slot 1's page before the call
far_tgt:	dw 0			; far call: the entry address
pg_under:	db 0			; the game's slot 1 page that the outermost far call replaced
vw_mode:	db 0			; jt_vwrite: 0 the source as the game sees it, else as mapped
vw_runs:	db 0			; jt_vwrite: runs left (0 = 256)
vw_left:	db 0			; jt_vwrite: bytes left in this run - 1
vw_sstep:	dw 0			; jt_vwrite: source step from run to run
vw_vstep:	dw 0			; jt_vwrite: VRAM step from run to run
vw_sp:		dw 0			; jt_vwrite: the caller's SP
vw_stack:	ds 64			; jt_vwrite: its own stack, in this page
vw_stack_top:
nr_saved	equ vw_stack		; NextReg values to restore on quit, from the
					; loader: fw4_start keeps them in fw4 (nr_keep)
fw_stack:	ds 120
fw_stack_top:
G_B		equ fw_stack_top-1
G_C		equ fw_stack_top-2
G_D		equ fw_stack_top-3
G_E		equ fw_stack_top-4
; assert (low fw_stack_top) >= 8, "reg_addr needs the frame inside one page" (checked by tools/check-layout)

; Code in the rest of this page.
; vram_block's end while tiles from cart ROM are on (fw2_switches puts a
; call to this in kn_hk): (SP + 2) = the source after the block. A block
; read from RAM or the trace buffer ($C000 up) gets tw_check's work alone;
; any other goes to kn_block (fw2) with DE = the source after it.
kn_entry:	ld hl,3
		add hl,sp
		ld a,(hl)
		cp $C0
		jp nc,tw_check
		ld d,a
		dec hl
		ld e,(hl)
		ld hl,kn_block
		jp fw2_call

; ======================================================================
; Leave the game (BREAK): put NextZXOS's pages and registers back and go
; to the loader's browser. Entered from the vblank interrupt with the
; game's stack; never returns to the game.
; ======================================================================
fw_quit:
		di
		ld sp,fw_stack_top
		nextreg $51,FW4_PAGE
		jp fw_quit4		; fw4: all but slot 1, then fw_quit_t
fw_quit_t:	nextreg $51,$FF
		; MMU7 stays the framework until the loader runs (it maps page 1)
		jp fw_resume

		IFDEF TRACE_BUILD
		include "vdpcheck.asm"
		ENDIF
fw_gap_end:
; assert fw_gap_end <= mapattr_table, "the code after fw_stack runs into the tables' page" (checked by tools/check-layout)

		align 256
		include "tables.inc"	; mapattr (256), pal_hi/lo, joy, ay_vol
		include "trvars.inc"	; trace.asm variables, in the rest of the page
trvars_end:

		align 256
; assert trvars_end <= $, "trvars.inc runs into region_tab's page" (checked by tools/check-layout)
region_tab:	ds 64			; per 256-byte VRAM page: 0 tile, 1 name table, 2 sprite table,
					; 3 name table rows 24-27, or 0-3 at V scroll 32 (tiles too)
dirty_pages:	ds 64			; per page: a bit per tile to convert; must
					; follow region_tab in the same page (+64)
io_tab:		dw out_nop, out_ioctl, out_psg, out_psg, out_vdata, out_vctrl, out_nop, out_nop
		dw in_ff, in_ff, in_vcount, in_hcount, in_vdata, in_status, in_dc, in_dd
wr_tab:		dw ret_nop, ioctl_w, psg_w, psg_w, vdata_w, vctrl_w, ret_nop, ret_nop
rd_tab:		dw rd_ff, rd_ff, rd_vcount, rd_hcount, rd_vdata, rd_status, rd_dc, rd_dd
; small data in the rest of this page
tm_lo:		db $FF,$FE,$FC,$F8,$F0,$E0,$C0,$80	; tmask
tm_hi:		db $01,$03,$07,$0F,$1F,$3F,$7F,$FF


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

; fw_line_irq patches a JP vbl_chk over fw_exit's first 3 bytes (POP DE,
; POP BC and the first byte of LD SP); vbl_work puts them back.
fw_exit:
		pop de
		pop bc
		ld sp,(fw_sp)
fw_exit_af:	pop af			; game AF, possibly changed
		ld hl,(fw_ret)
		ex (sp),hl		; return address in the slot, game HL back
exit_ei:	nop			; patched: EI or NOP
mx_ret:		ret

; A game whose frame handler keeps interrupts off past the ULA interrupt's
; line holds that interrupt, and the vblank work then runs when the handler
; turns them on, which can be inside the next picture: the copper update
; tears it there. fw_ula_irq sets vbl_arm when it comes in the picture; for
; VBL_ARM_N frame events after that (fw_line_irq), fw_exit goes through
; vbl_chk and jt_vwrite's end through vbl_chkv, from the frame event to the
; vblank work. Past the ULA interrupt's line (or already in the next
; picture) the work runs there, and the held interrupt skips it (vbl_poll).
; Unarmed, they cost nothing extra.
VBL_ARM_N	equ 250			; frames (5 s)
VBL_LINE	equ 248			; the ULA interrupt's line at 50 Hz; 224 at 60 Hz
					; (hz_setup in fw3 writes it into vbl_due)
; fw_exit while a display-off write is held (dis_patch in fw2): every
; DIS_N-th trap has dis_tick2 (fw2) count the frames that start while the
; game keeps interrupts off, as no frame event or vertical blank work comes
; then. A trap costs about 30 cycles more, the DIS_N-th about 500.
DIS_N		equ 32
dis_chk:	ld hl,dis_n
		dec (hl)
		jr nz,dis_chk__x
		ld hl,dis_tick2
		call fw2_call
dis_chk__x:	pop de
		pop bc
		ld sp,(fw_sp)
		jp fw_exit_af
dis_n:		db DIS_N		; traps to the next dis_tick2
vbl_chk:	call vbl_due
		call c,vbl_run
		pop de
		pop bc
		ld sp,(fw_sp)
		jp fw_exit_af
; A = vbl_arm, not 0: count the frame event, put vbl_chk in fw_exit and
; vbl_chkv in jt_vwrite's end (vbl_work takes them out).
vbl_on:		dec a
		ld (vbl_arm),a
		ld hl,vbl_chk
		ld (fw_exit+1),hl
		ld a,$C3		; JP
		ld (fw_exit),a
		ld hl,vbl_chkv
		ld (vw_tw+1),hl
		ret
; jt_vwrite's end (vw_tw), on its own stack: the work on fw_stack.
vbl_chkv:	call tw_check
		call vbl_due
		ret nc
		ld hl,0
		add hl,sp
		ld sp,fw_stack_top
		push hl
		call vbl_run
		pop hl
		ld sp,hl
		ret
; Carry: the vblank work is due. Armed at the frame event, the line's low
; byte is enough: from the ULA interrupt's line to 255, or below pic_end for
; lines 256 and later and the next picture. Uses A, BC, HL.
vbl_due:	ld bc,$243B
		ld a,$1F
		out (c),a
		inc b
		in a,(c)		; the line's low byte
vbl_due__line:	cp VBL_LINE		; the ULA interrupt's line (hz_setup)
		ccf
		ret c
		ld hl,pic_end
		cp (hl)
		ret

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
out_ioctl:	ld a,(game_a)
		ld (io_ctl),a
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
ioctl_w:	ld a,c
		ld (io_ctl),a
		ret

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
		cp $80
		jp z,op_far		; $80: far call into a code page (ABI 6)
		jp fw_fatal
; LD I,A and LD A,I: the framework's IM 2 needs I, so the game's I is kept
; in shadow_i (Wonder Boy III keeps flags in it). LD A,I: S and Z from the
; value, P/V = the game's IFF2, H = N = 0, C kept.
ed_ldia:	ld a,(game_a)
		ld (shadow_i),a
		jp fw_exit
ed_ldai:	ld hl,ed_ldai4		; in fw4
		call fw4_call
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
		IFDEF TRACE_BUILD
		call tc_data
		ENDIF
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
		jp nc,fw_line_irq__frame
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
		call cur_line		; a line event held into the blank does not
		ld hl,pic_end		; arm the work: a V counter read may have done it
		cp (hl)
		jr nc,fw_line_irq__late
		xor a
		ld (vbl_done),a
fw_line_irq__late:
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
		call cur_line		; arm the work only on time: a frame event held
		ld hl,pic_end		; later may follow a V counter read that did it
		sub (hl)		; in this blank already
		cp 2
		jr nc,fw_line_irq__fl
		xor a
		ld (vbl_done),a
		ld a,(vbl_arm)		; vbl_chk until the vblank work runs
		or a
		call nz,vbl_on
fw_line_irq__fl:
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
mx_lirq:	reti
fw_line_irq__callgame:	; acknowledge the Next interrupt now and enter the game's $0038
		; with interrupts off and the interrupted PC on the stack, as the
		; SMS takes an IRQ: a game that leaves its ISR another way (R-Type
		; resets SP and jumps) must not leave the interrupt unacknowledged
		IFDEF TRACE_BUILD
		ld hl,(irq_s)
		call tc_enter
		ENDIF
		pop bc
		pop hl
		pop af
		push hl
irq_t1:		ld hl,$0038		; pg_irq while a far call has run (irq_slot1)
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
		IFDEF TRACE_BUILD
		ld hl,(irq_s)
		call tc_enter
		ENDIF
		pop af
		pop hl
		push hl
irq_t2:		ld hl,$0038		; pg_irq while a far call has run (irq_slot1)
		ex (sp),hl
mx_irqf:	reti
irq_flag:	pop af			; IE0 off: the flag only
		pop hl
		ei
mx_irqo:	reti

; The game's interrupt entry while far_find has patched irq_t1 and irq_t2
; (fw_line_irq, irq_go): the game's registers, interrupts off, the return
; slot at SP and in irq_s. irq_slot1 (fw2) gives the handler the game's
; page in slot 1, then on to the game's $0038.
pg_irq:		push af
		push hl
		ld hl,irq_slot1
		call fw2_call		; slot 1 = cur_mmu+1 after it
		pop hl
		pop af
mx_pgi:		jp $0038

; A game interrupt handler that interrupted a code page entry returns here
; (irq_slot1 put this in its return slot): the code page goes back in slot
; 1, then on to the interrupted address with the interrupt state the
; handler left.
pg_tramp:	push af
		ld a,i			; P/V = IFF2
		di
pg_tramp_p:	ld a,0			; patched: the code page
		ld (cur_mmu+1),a
		nextreg $51,a
		jp po,pg_tramp__di
		pop af
		ei
mx_pgt1:
pg_tramp_j1:	jp 0			; patched: the interrupted address
pg_tramp__di:	pop af
mx_pgt2:
pg_tramp_j2:	jp 0			; patched: the same

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
isr_tramp__go:
		IFDEF TRACE_BUILD
		push hl
		ld hl,(isr_go)
		call tc_enter
		pop hl
		ENDIF
		pop af
mx_itj:		jp $0038
isr_tramp__ret:		pop af			; P/V = IFF
		ld hl,(isr_pc)
		jp po,isr_tramp__di
		pop af
		ex (sp),hl
		ei
mx_itr:		ret
isr_tramp__di:		pop af
		ex (sp),hl
mx_itd:		ret

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
		call pri_cells
		ld a,d
		and $1F
		ld d,a
		push de
		pop ix			; its high byte in the shadow (nt_range sets IX after)
		call pri_markc
		pop de
		pop bc
		ret
; DE = VRAM address in the name table, BC = count (1-256): HL = the mark of
; the first cell written ($3C00 + cell), B = the cells, DE = the VRAM
; address of the first cell's high byte.
pri_cells:	ld hl,(nt_base)
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
		ex de,hl
		pop hl
		ld a,h
		add a,$3C
		ld h,a			; its mark
		ret
; HL = the mark of a cell, B = cells (1-256), IX = the cell's high byte
; (the entries in a row, 2 bytes apart): each cell with the priority bit
; is marked and its row gets "has priority cells", any other cell that
; Layer 2 holds is marked. MAP_PAGE in slot 1. Uses A, B, HL, IX.
pri_markc:	bit 4,(ix+0)
		jr z,pri_markc__np
		set 0,(hl)
		push hl
		call pri_rowp
		pop hl
		jr pri_markc__n
pri_markc__np:	bit 1,(hl)
		jr z,pri_markc__n
		set 0,(hl)
		push hl
		call pri_rowr
		pop hl
pri_markc__n:	inc hl
		inc ix
		inc ix
		djnz pri_markc
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

; ULA frame interrupt, line 248 of the 311-line frame at 50 Hz, line 224 of
; the 264-line frame at 60 Hz: the framework's
; once-a-frame work. The work runs once a frame: here, or earlier in the
; blank from a V counter read (rd_vcount) or a trap (vbl_chk), which set
; vbl_poll so that this interrupt, held by a game that keeps interrupts off
; and arriving late, does not run it a second time. vbl_done stops a second V counter read in
; the same blank; reads in the picture, and frame and line events that come
; on time, clear it. Pause becomes the SMS NMI: the RETI goes to $0066 with
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
		call cur_line		; held into the picture: arm vbl_chk
		ld hl,pic_end
		cp (hl)
		jr nc,fw_ula_irq__w
		ld a,VBL_ARM_N
		ld (vbl_arm),a
fw_ula_irq__w:	ld a,(vbl_poll)		; a V counter read or vbl_chk did this frame's work
		or a
		call z,vbl_work
		xor a
		ld (vbl_poll),a
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
		push de
		ld hl,6			; the interrupted PC: the NMI's return slot
		add hl,sp
		ex de,hl
		ld hl,nmi_slot1		; no code page in slot 1 for the game's NMI
		call fw2_call
		pop de
		pop hl
		pop af
		push hl
		ld hl,$0066
		ex (sp),hl
		ei
mx_ulan:	reti
fw_ula_irq__out:		pop hl
		pop af
		ei
mx_ula:		reti

; The vblank work from a trap (rd_vcount, vbl_chk): the held ULA interrupt
; skips it (vbl_poll). Keeps IX and IY.
vbl_run:	push ix
		push iy
		call vbl_work
		ld a,1
		ld (vbl_poll),a
		pop iy
		pop ix
		ret

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
; game's page back. Not for use inside vbl_work, nor from fw2 or fw4 code.
; Keeps A and F from the routine.
fw2_call:
		nextreg $51,FW2_PAGE
		call call_hl
		push af
		ld a,(cur_mmu+1)
		nextreg $51,a
		pop af
		ret
; The same for a routine in fw4 (FW4_PAGE). Keeps A and F from the routine.
fw4_call:
		nextreg $51,FW4_PAGE
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

; ======================================================================
; Port reads (A = result)
; ======================================================================
rd_ff:		ld a,$FF
		ret
rd_hcount:	ld a,$80
		ret
; $DD: no second pad. Bits 7 and 6 are the TH lines of ports B and A, as
; on an export console: a TH set to output in $3F (bit 3, bit 1 clear)
; reads back the level written there (bit 7, bit 5); an input reads 1.
; Games read this to tell an export console from a Japanese one.
rd_dd:		ld a,(io_ctl)
		ld l,a
		rlca
		rlca
		rlca
		rlca			; direction bits 3, 1 to bits 7, 5
		or l			; bit 7 = TH-B, bit 5 = TH-A
		ld l,a
		and $20
		add a,a			; TH-A to bit 6
		ld h,a
		ld a,l
		and $80
		or h
		or $3F
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
; of the 256x192 area, as on the SMS. The count from the line is the PAL
; SMS one at 50 Hz and the NTSC one at 60 Hz: vc50 and vc60 in fw3, one of
; which hz_setup copies to rd_vcount__ret at game start. A game that polls
; the counter also gets the once-a-frame work done here when interrupts
; never deliver it.
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
		call vbl_run
		pop de
		jr rd_vcount__ret
rd_vcount__active:	xor a
		ld (vbl_done),a
		ld (fdone),a
VC_LEN		equ 49			; the longer of vc50 and vc60 in fw3
rd_vcount__ret:	ds VC_LEN		; the count from D and E: vc50 or vc60 (fw3), copied
					; here by hz_setup

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
		IFDEF TRACE_BUILD
		call tc_data
		ENDIF
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
		IFDEF TRACE_BUILD
		call tc_ctrl
		ENDIF
		ld hl,vdp_latch
		ld a,(hl)
		or a
		jr nz,vctrl_w__second
		inc (hl)
		ld a,c
		ld (vdp_addr),a		; first byte: address low at once
		ret
vctrl_w__second:	ld (hl),0
		IFDEF TRACE_BUILD
		call tc_setup
		ENDIF
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
		ld hl,vdp_reg_w		; in fw2
		jp fw2_call

vdata_w:
		IFDEF TRACE_BUILD
		call tc_data
		ENDIF
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
		push hl
		ld hl,tw_cnt
		inc (hl)
		jr nz,vram_put__c
		inc hl
		inc (hl)
		call tw_check
vram_put__c:		pop hl
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
		IFDEF TRACE_BUILD
		call tc_data
		ENDIF
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
		push hl
		ld hl,(tw_cnt)
		add hl,bc
		ld (tw_cnt),hl
		pop hl
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
		jp nz,vram_block__seg
kn_hk:		call tw_check		; tilecache: call kn_entry (fw2_switches)
		pop hl
		pop ix
		ret

; TW_MAX * 256 bytes or more written to tiles since their last conversion:
; a game that writes many tiles with interrupts off (a level loaded) has
; them converted now, as it writes, and not all in its first vblank after,
; which then takes a frame's time or more. Keeps every register.
TW_MAX		equ 2
tw_check:	push af
		ld a,(tw_cnt+1)
		cp TW_MAX
		jr c,tw_check__no
		push bc
		push de
		push hl
		ld hl,tw_flush
		call fw2_call
		pop hl
		pop de
		pop bc
tw_check__no:		pop af
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

; ======================================================================
; PSG (SN76489) -> AY. C = byte written to the PSG.
; Tone channels 0-2 -> AY 0 channels A-C. Noise -> AY 1 channel A: white
; noise on the AY noise generator, periodic noise as a tone at the
; periodic noise's pitch. Latch/data protocol as SMS Power describes it:
; the latch is never cleared by a data byte, tone registers change at once.
; ======================================================================
psg_w:		ld hl,psg_w2		; the PSG code is in fw4
		jp fw4_call

; ======================================================================
; Fatal stop: red border, interrupts off.
; ======================================================================
fw_fatal:
		di
		ld a,2
		out ($FE),a
fw_fatal__h:		jr fw_fatal__h

; ======================================================================
; Start the game. Called by the loader (via the jump table) with:
;   cart pages loaded at CART_PAGE.., fw_npages, fw_start_addr set,
;   patch applied, NextZXOS's pages saved, nr_saved filled.
; Never returns.
; ======================================================================
fw_start:
		di
		ld sp,fw_stack_top
		nextreg $51,FW4_PAGE	; the set-up is in fw4 (fw4_start) and fw2 (fw2_start)
		call fw4_start
		nextreg $51,FW2_PAGE
		call fw2_start
		call restore_mmu
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

; ======================================================================
; Code pages (ABI 6). A far call maps an overlay's code page at $2000
; (MMU1), calls one of its entries with the game's registers and
; interrupt state, and maps the old page back when the entry returns.
; While the entry runs, cur_mmu+1 holds the code page, so every place
; that puts slot 1 back (fw2_call, fw4_call, nt_put, vbl_work) puts the
; page back. A game interrupt handler entered meanwhile gets the game's
; page there: far_find points the interrupt entries at pg_irq, and
; irq_slot1 (fw2) does the rest.
; far_find (fw2) looks the entry up in the table the loader fills.
; ======================================================================
; RST io + $80 + page + entry. FASTENTRY has run: leave as fw_exit does,
; with interrupts still off, and go on with the far call.
op_far:		ld hl,(fw_ret)
		call far_ops
		ld (fw_ret),hl
		ld a,(exit_ei)
		ld (far_ei),a
		pop de
		pop bc
		ld sp,(fw_sp)
		pop af
		ld hl,(fw_ret)
		ex (sp),hl
		jr far_go
; CALL jt_far + page + entry
fw_far:		ex (sp),hl
		push af
		ld a,i			; P/V = IFF2
		di
		ld a,$00		; NOP
		jp po,fw_far__di
		ld a,$FB		; EI
fw_far__di:	ld (far_ei),a
		call far_ops
		pop af
		ex (sp),hl		; the return address after the two bytes
; Interrupts off, the game's registers, (SP) = the return address.
far_go:		push hl
		push af
		nextreg $51,FW2_PAGE
		call far_find		; HL = entry address, A = its RAM page
		ld (cur_mmu+1),a
		nextreg $51,a
		ld (far_tgt),hl
		pop af
		pop hl
		push hl
		ld hl,(far_prev)	; L = the page to put back
		ex (sp),hl
		push hl
		ld hl,far_ret
		ex (sp),hl
		push hl
		ld hl,(far_tgt)
		ex (sp),hl		; entry, far_ret, old page, return address
far_ei:		nop			; patched: EI or NOP
mx_farg:	ret
; The entry returns here: slot 1 back as it was before the call.
far_ret:	ex (sp),hl		; L = the old page
		push af
		ld a,l
		ld (cur_mmu+1),a
		nextreg $51,a
		pop af
		pop hl
mx_farr:	ret
; HL = the two inline bytes: far_p, far_e. Returns HL past them.
far_ops:	ld a,(hl)
		ld (far_p),a
		inc hl
		ld a,(hl)
		ld (far_e),a
		inc hl
		ret

; A = the byte the game sees at HL, for code in a code page: an address
; in $2000-$3FFF reads the game's page there (pg_under), not the code
; page. Keeps the other registers; F changes. Interrupts stay as they
; are: cur_mmu+1 always names the page in slot 1.
fw_peek:	ld a,h
		and $E0
		cp $20
		jr z,fw_peek__w
		ld a,(hl)
mx_pk:		ret
fw_peek__w:	push bc
		ld a,(cur_mmu+1)
		ld b,a
		ld a,(pg_under)
		ld (cur_mmu+1),a
		nextreg $51,a
		ld c,(hl)
		ld a,b
		ld (cur_mmu+1),a
		nextreg $51,a
		ld a,c
		pop bc
mx_pkw:		ret

; ======================================================================
; jt_vwrite (ABI 7), for page code: writes bytes into SMS VRAM as the
; game's VDP data port writes would, in runs with a step between them.
;   HL = the source of the first run, DE = the VRAM address of its first
;   byte (bits 14 and 15 are ignored), B = bytes in each run (0 = 256),
;   C = runs (0 = 256), IX = the source step and IY = the VRAM step, from
;   the start of one run to the start of the next (the VRAM address wraps
;   at $4000), A = 0: the source as the game sees it (an address in
;   $2000-$3FFF reads the game's page there, as jt_peek does), else the
;   source as mapped now (the code page in $2000-$3FFF).
; It writes the shadow and does what the data port handlers do for each
; byte: the name table entries in the Next tilemaps (M0 and A8, and the
; priority marks with the priority switch), the dirty marks of the tiles,
; and the sprite table flag. It leaves the VDP state as the control and
; data writes of the runs leave it: address after the last byte of the
; last run, code 1 (VRAM write), latch clear, read buffer = the last byte.
; Keeps BC, DE, HL, IX, IY, the alternate registers and the interrupt state;
; A and F change. The source is in $0000-$DFFF.
; Slots while it runs: 0 the source's page, 1 MAP_PAGE, 4 and 5 the shadow
; (VRAM v at $8000 + v). It runs with interrupts off, on its own stack.
; ======================================================================
fw_vwrite:	ld (vw_mode),a
		ld a,i			; P/V = IFF2
		di
		ld (vw_sp),sp
		ld sp,vw_stack_top
		push af
		push bc
		push de
		push hl
		push ix
		push iy
		exx
		push bc			; the fast form counts runs in C'
		exx
		IFDEF TRACE_BUILD
		call tc_ctrl		; the control write of the first run
		call tc_setup
		call tc_data
		ENDIF
		ld (vw_sstep),ix
		ld (vw_vstep),iy
		ld a,c
		ld (vw_runs),a
		ld c,b
		dec c			; C = bytes in each run - 1
		ld a,d
		and $3F
		ld d,a
		nextreg $54,SHADOW_PAGE
		nextreg $55,SHADOW_PAGE+1
		nextreg $51,MAP_PAGE
		ld a,$FF
		ld (vw_k+1),a		; no source page in slot 0 yet
		xor a
		ld (vdp_latch),a
		inc a
		ld (vdp_code),a
		ld a,c
		or a
		jp z,vt_go		; one byte in each run
; The fast form: runs of whole name table entries inside one row and one
; column group (0-7 or 8-31), a VRAM step that is a multiple of 64, so
; every run has the same column, and all the source inside one 8K page. A
; run then needs only adds to its pointers; with priority tiles, vf_prun
; marks its cells first. The first run outside the name table hands the
; rest to the pieces below (vf_gen).
		bit 0,c
		jp z,vw_run		; an odd length
		bit 0,e
		jp nz,vw_run		; an odd start
		ld a,iyl
		and $3F
		jp nz,vw_run
		ld a,iyh
		cp $40
		jp nc,vw_run		; the VRAM step: a multiple of 64 below $4000
		ld a,e
		and $3F
		ld b,a			; the run's first byte in its row
		scf
		adc a,c
		jp c,vw_run
		cp $41
		jp nc,vw_run		; past the row's end
		push hl
		ld hl,vf_hin
		ld a,b
		cp $10
		jr nc,vw_fast__g
		ld hl,vf_lon
		scf
		adc a,c
		cp $11
		jr c,vw_fast__g
		pop hl
		jp vw_run		; past column 8
vw_fast__g:	ld (vf_cj+1),hl
		pop hl
		ld a,ixh
		rla
		jp c,vw_run		; a source step from $8000
		push de			; v
		push hl			; s
		ld a,(vw_runs)
		dec a
		ld b,a			; runs - 1
		ld e,a
		ld d,ixh
		mul d,e
		ld a,d
		or a
		jr nz,vw_fast__no
		ld h,e
		ld l,0
		ld e,b
		ld d,ixl
		mul d,e
		add hl,de		; (runs - 1) * step
		jr c,vw_fast__no
		pop de
		push de
		add hl,de
		jr c,vw_fast__no
		ld e,c
		ld d,0
		add hl,de		; the last byte of the last run
		jr c,vw_fast__no
		pop de			; s
		ld a,h
		xor d
		and $E0
		ex de,hl		; HL = s
		pop de			; v
		jr z,vw_fast
		jp vw_run		; the source crosses an 8K page
vw_fast__no:	pop hl
		pop de
		jp vw_run
vw_fast:	ld a,h			; DE = v, HL = s, C = length - 1
		and $E0
		call vw_map
		ld a,h
		and $1F
		ld h,a			; the source in slot 0
		ld a,c
		ld (vf_lm+1),a
		inc a
		ld b,a			; length
		rrca
		ld (vf_hin+1),a		; entries in a run
		ld (vf_lon+1),a
		push hl
		push de
		ld e,b
		ld d,0
		dec a
		jr nz,vw_fast__m
		ld hl,(vf_cj+1)		; one entry: the forms without the loop
		ld de,vf_hin
		or a
		sbc hl,de
		ld hl,vf_hi1
		jr z,vw_fast__1
		ld hl,vf_lo1
vw_fast__1:	ld (vf_cj+1),hl
		ld de,0			; the map pointers do not move in the run
vw_fast__m:	push de
		ld e,b
		ld hl,(vw_sstep)
		or a
		sbc hl,de
		ld (vf_sa+2),hl		; source step - length
		ld hl,(vw_vstep)
		or a
		sbc hl,de
		ld (vf_va+2),hl		; VRAM step - length
		ld hl,(vw_vstep)
		srl h
		rr l
		srl h
		rr l
		ld bc,(vw_vstep)
		add hl,bc
		pop de
		sbc hl,de		; (carry clear) Next map step - the pointers' move in a run
		ld (vf_ma+1),hl
		ld a,$7F
		ld (vf_pg+1),a		; no VRAM page yet
		pop de
		call vw_m0
		push hl
		pop ix			; M0
		ld bc,MAP_A8-16
		add hl,bc
		push hl
		pop iy			; A8 for columns 8-31
		pop hl
		ld a,(vw_runs)
		exx
		ld c,a			; runs (0 = 256)
		exx
vf_run:		ld a,d			; HL = source, DE = VRAM or shadow address
vf_pg:		cp $7F			; (patched: the shadow page of the last run)
		jr nz,vf_page
vf_mode:	jp vf_hin		; (patched: the run's form, or vf_marks)
vf_page:	and $3F
		ld (vf_rg+1),a
		or $80
		ld d,a			; DE = the shadow: $8000 + VRAM address
		ld (vf_pg+1),a
vf_rg:		ld a,(region_tab)	; (patched: the VRAM page)
		ld bc,(vf_cj+1)
		dec a
		jr z,vf_page__m
		cp 2
		jp nz,vf_gen		; outside the name table
		ld bc,vf_marks		; name table rows 24-27: the tiles too
vf_page__m:
vf_pm:		ld (vf_mode+1),bc	; (patched: vf_pj+1 with priority tiles, fw2_switches)
		jr vf_mode
; Priority tiles: vf_mode jumps here for every run. The cells' marks from
; the source (its high bytes), as pri_markr does from the shadow, then on to
; the run's form.
vf_prun:	push hl
		push de
		push ix
		inc hl
		push hl
		pop ix			; IX = the first entry's high byte in the source
		ex de,hl
		ld a,h
		and $3F
		ld h,a			; the run's VRAM address
		ld de,(nt_base)
		or a
		sbc hl,de
		srl h
		rr l			; its first cell
		ld a,h
		add a,$3C
		ld h,a			; the cell's mark
		ld a,(vf_hin+1)
		ld b,a			; cells: the entries in a run
		call pri_markc
		pop ix
		pop de
		pop hl
vf_pj:		jp vf_hin		; (patched: the run's form or vf_marks)
vf_marks:	ld a,e			; the tiles' dirty marks
vf_lm:		add a,0			; (patched: length - 1)
		call tmask
		push hl
		ld c,a
		ld a,(vf_rg+1)
		or $40
		ld l,a
		ld h,255&((region_tab)>>8)
		ld a,c
		or (hl)
		ld (hl),a
		ld (tiles_dirty),a
		pop hl
vf_cj:		jp vf_hin		; (patched: the run's form: vf_hin, vf_lon, vf_hi1, vf_lo1)
vf_hin:		ld b,0			; (patched: entries in a run)
vf_hi:		ld a,(hl)		; columns 8-31: the shadow, M0 and A8
		ld (de),a
		ld (ix+0),a
		ld (iy+0),a
		inc hl
		inc de
		ld a,(hl)
		ld (de),a
		ld (vf_ht+1),a
vf_ht:		ld a,(mapattr_table)
		ld (ix+1),a
		ld (iy+1),a
		inc hl
		inc de
		inc ix
		inc ix
		inc iy
		inc iy
		djnz vf_hi
		jp vf_adv
vf_hi1:		ld a,(hl)		; the same for one entry
		ld (de),a
		ld (ix+0),a
		ld (iy+0),a
		inc hl
		inc de
		ld a,(hl)
		ld (de),a
		ld (vf_ht1+1),a
vf_ht1:		ld a,(mapattr_table)
		ld (ix+1),a
		ld (iy+1),a
		inc hl
		inc de
		jp vf_adv
vf_lo1:		ld a,(hl)
		ld (de),a
		ld (ix+0),a
		ld (ix+64),a
		ld (iy+64),a
		ld (iy+80),a
		inc hl
		inc de
		ld a,(hl)
		ld (de),a
		ld (vf_lt1+1),a
vf_lt1:		ld a,(mapattr_table)
		ld (ix+1),a
		ld (ix+65),a
		ld (iy+65),a
		ld (iy+81),a
		inc hl
		inc de
		jp vf_adv
vf_lon:		ld b,0			; (patched: entries in a run)
vf_lo:		ld a,(hl)		; columns 0-7: the shadow, M0 twice, A8 columns 24-31 and 32-39
		ld (de),a
		ld (ix+0),a
		ld (ix+64),a
		ld (iy+64),a
		ld (iy+80),a
		inc hl
		inc de
		ld a,(hl)
		ld (de),a
		ld (vf_lt+1),a
vf_lt:		ld a,(mapattr_table)
		ld (ix+1),a
		ld (ix+65),a
		ld (iy+65),a
		ld (iy+81),a
		inc hl
		inc de
		inc ix
		inc ix
		inc iy
		inc iy
		djnz vf_lo
vf_adv:
vf_sa:		add hl,0		; (patched: source step - length)
vf_va:		add de,0		; (patched: VRAM step - length)
vf_ma:		ld bc,0			; (patched: Next map step - length)
		add ix,bc
		add iy,bc
		exx
		dec c
		exx
		jp nz,vf_run
		ex de,hl		; the VDP address: after the last run
		ld bc,(vf_va+2)
		or a
		sbc hl,bc
		ld a,h
		and $3F
		ld h,a
		ld (vdp_addr),hl
		jp vw_end
vf_gen:		ld a,(vw_k+1)		; the rest of the runs in pieces
		or h
		ld h,a			; HL = s
		ld a,d
		and $3F
		ld d,a			; DE = v
		exx
		ld a,c
		exx
		ld (vw_runs),a
		ld a,(vf_lm+1)
		ld c,a			; length - 1
vw_run:		push hl			; the run's source and VRAM address
		push de
		ld a,c
; HL = source, DE = VRAM address, A = bytes left in the run - 1. A piece
; stays inside one 256-byte VRAM page and one 8K page of the source.
vw_seg:		ld (vw_left),a
		ld b,a
		ld a,e
		cpl			; bytes to the end of the VRAM page - 1
		cp b
		jr nc,vw_seg__1
		ld b,a
vw_seg__1:	ld a,h
		or $E0
		inc a
		jr nz,vw_seg__2		; more than 256 bytes to the source page's end
		ld a,l
		cpl
		cp b
		jr nc,vw_seg__2
		ld b,a
vw_seg__2:	ld a,h			; B = bytes in this piece - 1
		and $E0
vw_k:		cp $FF			; the source slot whose page slot 0 holds (patched)
		call nz,vw_map
		push hl
		push de
		push bc
		ld a,h
		and $1F
		ld h,a			; the source in slot 0
		ld a,d
		ld (vw_rg+1),a
		set 7,d			; the shadow
		ld c,b
		ld b,0
		inc bc			; BC = bytes in the piece
vw_rg:		ld a,(region_tab)	; (patched: the VRAM page)
		or a
		jr z,vw_tiles
		cp 2
		jr z,vw_sat
		push af			; 1 name table, 3 name table rows 24-27 and tiles
		push de
		push bc
		ldir
		pop bc
		pop de
		push de
		push bc
		call vw_ntmap
		pop bc
		pop de
		pop af
		cp 3
		jr nz,vw_next
		jr vw_marks
vw_tiles:	push de
		push bc
		ldir
		pop bc
		pop de
vw_marks:	ld hl,(tw_cnt)
		ld b,0
		dec c
		inc bc			; BC = count, 1-256
		add hl,bc
		ld (tw_cnt),hl
		ld a,e			; DE = first byte in the shadow, C = count (0 = 256)
		add a,c
		dec a			; last byte
		call tmask
		ld c,a
		ld a,(vw_rg+1)
		or $40
		ld l,a
		ld h,255&((region_tab)>>8)	; dirty_pages
		ld a,c
		or (hl)
		ld (hl),a
		ld (tiles_dirty),a
		jr vw_next
vw_sat:		ld a,1
		ld (sat_dirty),a
		ld a,e
		ldir
		cp $80			; tiles in the unused bytes $40-$7F: start < $80
		jr nc,vw_next
		ld c,a			; start
		ld a,e			; and end > $40 (0: the page's end)
		or a
		jr z,vw_sat__t
		cp $41
		jr c,vw_next
		cp $80
		jr c,vw_sat__e
vw_sat__t:	ld a,$80
vw_sat__e:	dec a
		ld d,a			; last byte written in $40-$7F
		ld a,c
		cp $40
		jr nc,vw_sat__s
		ld a,$40
vw_sat__s:	ld e,a			; first byte written in $40-$7F
		ld a,d
		call tmask		; the tiles there (2, 3 or both)
		ld c,a
		ld a,(vw_rg+1)
		or $40
		ld l,a
		ld h,255&((region_tab)>>8)
		ld a,c
		or (hl)
		ld (hl),a
		ld (tiles_dirty),a
vw_next:	pop bc
		pop de
		pop hl
		ld a,b			; source and VRAM address += bytes in the piece
		add hl,a
		inc hl
		ex de,hl
		add hl,a
		inc hl
		res 6,h
		ex de,hl
		ld a,(vw_left)
		sub b
		jr z,vw_rend
		dec a
		jp vw_seg
vw_rend:	ld (vdp_addr),de
		pop de
		pop hl
		ld a,(vw_runs)
		dec a
		jr z,vw_end
		ld (vw_runs),a
		push bc
		ld bc,(vw_sstep)
		add hl,bc
		ex de,hl
		ld bc,(vw_vstep)
		add hl,bc
		ld a,h
		and $3F
		ld h,a
		ex de,hl
		pop bc
		jp vw_run
vw_end:		ld hl,(vdp_addr)	; the read buffer: the last byte written
		dec hl
		ld a,h
		and $3F
		or $80
		ld h,a
		ld a,(hl)
		ld (vdp_rbuf),a
		ld a,(cur_mmu+0)
		nextreg $50,a
		ld a,(cur_mmu+1)
		nextreg $51,a
		ld a,(cur_mmu+4)
		nextreg $54,a
		ld a,(cur_mmu+5)
		nextreg $55,a
vw_tw:		call tw_check		; (patched: vbl_chkv while vbl_chk is armed)
		exx
		pop bc
		exx
		pop iy
		pop ix
		pop hl
		pop de
		pop bc
		pop af
		ld sp,(vw_sp)
		jp po,vw_end__di
		ei
vw_end__di:
mx_vw:		ret

;
; The one-byte form is vt_try in fw4 (FW4_PAGE in slot 1, where the name
; table form has MAP_PAGE). It hands runs back through vt_back, which maps
; MAP_PAGE again from this page.
vt_go:		nextreg $51,FW4_PAGE
		jp vt_try
vt_back:	nextreg $51,MAP_PAGE	; from vt_try: the rest through vw_run
		jp vw_run

; A = the source slot * 32: maps the page the source reads into slot 0.
; Keeps every register but A and F.
vw_map:		ld (vw_k+1),a
		rlca
		rlca
		rlca
		cp 1
		jr nz,vw_map__c
		ld a,(vw_mode)
		or a
		ld a,1
		jr nz,vw_map__c
		ld a,(pg_under)		; the game's page under the code page
		jr vw_map__n
vw_map__c:	push hl
		ld hl,cur_mmu
		add hl,a
		ld a,(hl)
		pop hl
vw_map__n:	nextreg $50,a
		ret

; vw_ntmap: A = bytes to the piece's boundary, B = bytes left (0 = 256):
; pushes B = bytes left after the piece, and sets B = the piece.
		MACRO VWPIECE
		local vp_c
		ld c,a
		ld a,b
		or a
		jr z,vp_c
		cp c
		jr nc,vp_c
		ld c,a
vp_c:		ld a,b
		sub c
		ld b,a
		push bc
		ld b,c
		ENDM

; DE = the shadow address of the first byte ($8000 + VRAM address, in the
; name table), C = count (0 = 256, inside one 256-byte page): writes those
; bytes into M0 and A8 as nt_put does, in pieces that end at column 8 and
; at the row's end. IX walks A8 (M0 + MAP_A8 - 16).
vw_ntmap:	ld b,c
vw_hk:		ds 3			; priority tiles: call vw_pri
		call vw_m0
		push hl
		pop ix
		push bc
		ld bc,MAP_A8-16
		add ix,bc		; IX = the A8 entry for columns 8-31
		pop bc
vw_ntmap__p:	ld a,e			; B = bytes left (0 = 256 only at the start)
		and $3F
		cp $10
		jr c,vw_ntmap__lo
		neg
		add a,$40		; bytes to the row's end
		VWPIECE
vw_ntmap__hl:	ld a,(de)		; columns 8-31: M0 and A8
		bit 0,e
		jr z,vw_ntmap__he
		ld (vw_ntmap__ht+1),a
vw_ntmap__ht:	ld a,(mapattr_table)	; (patched: the entry's high byte)
vw_ntmap__he:	ld (hl),a
		ld (ix+0),a
		inc e
		inc hl
		inc ix
		djnz vw_ntmap__hl
		pop bc
		ld a,e
		and $3F
		jr nz,vw_ntmap__nx
		push bc			; the next row: 16 more bytes in the Next maps
		ld bc,16
		add hl,bc
		add ix,bc
		pop bc
vw_ntmap__nx:	ld a,b
		or a
		jr nz,vw_ntmap__p
		ret
vw_ntmap__lo:	push hl
		pop iy
		push de
		ld de,64
		add iy,de		; IY = M0 + 64: SMS columns 0-7 again in 32-39
		pop de
		neg
		add a,$10		; bytes to column 8
		VWPIECE
vw_ntmap__ll:	ld a,(de)		; columns 0-7: M0 twice, A8 columns 24-31 and 32-39
		bit 0,e
		jr z,vw_ntmap__le
		ld (vw_ntmap__lt+1),a
vw_ntmap__lt:	ld a,(mapattr_table)
vw_ntmap__le:	ld (hl),a
		ld (iy+0),a
		ld (ix+64),a
		ld (ix+80),a
		inc e
		inc hl
		inc ix
		inc iy
		djnz vw_ntmap__ll
		pop bc
		jr vw_ntmap__nx
; DE = a VRAM address in the name table (bits 14 and 15 ignored): HL =
; its M0 entry, $2000 + o + row * 16 (o = the address - nt_base, row =
; o >> 6). Keeps BC and DE.
vw_m0:		ld a,d
		and $3F
		ld h,a
		ld l,e
		push bc
		ld bc,(nt_base)
		or a
		sbc hl,bc		; o = 0..$6FF
		pop bc
		ld a,l
		and $C0
		or h
		rlca
		rlca			; row
		push de
		ld e,a
		ld d,16
		mul d,e
		add hl,de
		pop de
		set 5,h
		ret

; Priority tiles: DE = the shadow address of the first byte, B = count (0 =
; 256): the marks of the cells written, as pri_markr does. MAP_PAGE in
; slot 1. Keeps BC and DE.
vw_pri:		push bc
		push de
		ld c,b
		ld b,0
		ld a,c
		or a
		jr nz,vw_pri__n
		inc b			; 256
vw_pri__n:	ld a,d
		and $3F
		ld d,a			; the VRAM address
		call pri_cells
		ld a,d
		and $3F
		or $80
		ld d,a
		push de
		pop ix			; the first cell's high byte in the shadow
		call pri_markc
		pop de
		pop bc
		ret

fw_code_end:
; assert fw_code_end <= TR_CODE, "framework code overflows into the trace code area" (checked by tools/check-layout)

; Hardware IM2 mode gives only the vectors of the interrupts turned on:
; $00 (line) and $16 (ULA). The other entries up to $16 read $FEFE.
; TR_CODE-$FCFF and $FD18-$FEFD hold trace code (trace.asm).
		defs ($FD00)-0xE000-$
im2_table:	dw fw_line_irq		; line interrupt: vector $00
		ds 20,$FE
		dw fw_ula_irq		; ULA interrupt: vector $16
		defs ($FEFE)-0xE000-$
		ei
		reti
; assert tr_tg >= TR_DBUF + TR_DLIM && tr_fx >= tr_tg + TR_NT*4 && tr_fx + TR_NT*4 <= $FFFC, "trace buffers overlap" (checked by tools/check-layout)
; assert $ <= $FFFC, "framework overflows the mapper registers" (checked by tools/check-layout)
