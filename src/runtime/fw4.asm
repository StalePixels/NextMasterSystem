; fw4.asm: the framework's fourth page (FW4_PAGE), mapped at $2000 (MMU1)
; like fw2 for the length of one call (fw4_call in fw.asm): handler work that
; needs nothing in fw2. Game start and quit, the PSG, and the trace builder.
; Code here never calls into fw2: both pages use slot 1.

;		org $2000  (section origin)
		include "tables3.inc"	; trace_table (256), page aligned

; ----------------------------------------------------------------------
; Game start, first part, called by fw_start (fw.asm) with this page at
; $2000: NextRegs, sound, video registers, palettes, hidden sprites,
; cleared pages. fw2_start does the rest.
; ----------------------------------------------------------------------
fw4_start:
		ld hl,nr_saved		; the loader's NextReg list, kept here: jt_vwrite
		ld de,nr_keep		; uses its place in part 1 as its stack
		ld bc,NR_KEEP
		ldir
		; DivMMC automap off: the game's $0000-$3FFF is RAM, and $0038 and
		; $0066 are automap entry points.
		ld a,$0A
		call nr_read
		and %11101111
		nextreg $0A,a
		nextreg $07,3		; 28 MHz (PoC-only)
		; joystick 1 as Mega Drive pad on port $1F (Kempston bits plus
		; A and Start)
		ld a,$05
		call nr_read
		and %00110111
		or %01001000
		nextreg $05,a
		; TurboSound on, AY 0 and AY 1 mono
		ld a,$08
		call nr_read
		or %00000010
		nextreg $08,a
		ld a,$09
		call nr_read
		or %01100000
		nextreg $09,a
		xor a
		ld (ay_cur),a		; forces the first chip select
		ld a,$FF
		call ay_quiet
		ld a,$FE
		call ay_quiet
		ld a,$FF
		ld e,7
		ld d,%00111000		; AY 0: tones on, noise off
		call ay_write
		; DACs to their middle value (silence without a DC step)
		nextreg $2C,$80
		nextreg $2D,$80
		nextreg $2E,$80
		; video
		nextreg $68,%00000000	; ULA on: clipped to SMS column 0, it shows the backdrop there (bd_update)
		nextreg $15,%01100010	; sprites off for now, over border, clip, 0 on top
		nextreg $6B,%00000010	; tilemap off until the game turns the display on
		nextreg $6C,0
		nextreg $6E,NR6E_M0	; map: bank 7 offset 0
		nextreg $6F,$00		; tiles: bank 5 offset 0
		nextreg $4C,0		; tile pixel value 0 is transparent
		nextreg $4B,0		; sprite pixel value 0 is transparent
		nextreg $4A,0
		nextreg $2F,255&(((288-PIC_X))>>8)	; X offset for H scroll 0
		nextreg $30,255&((288-PIC_X))
		nextreg $31,224
		nextreg $62,0		; copper stopped
		; sprite palette: all black
		nextreg $43,%00100010
		nextreg $40,0
		ld b,0
fw4_start__spal:		nextreg $44,0
		nextreg $44,0
		djnz fw4_start__spal
		; tilemap palette 0: all black
		nextreg $43,%00110010
		nextreg $40,0
		ld b,0
fw4_start__pal:		nextreg $44,0
		nextreg $44,0
		djnz fw4_start__pal
		; the second tilemap and sprite palettes (toppal) and both Layer 2
		; palettes: all black; Layer 2 entries 0 and 16 (pixel value 0)
		; hold the global transparent colour L2_TRANS
		ld a,%01110010
		call pal_black
		ld a,%01100010
		call pal_black
		ld a,%00010010
		call pal_l2
		ld a,%01010010
		call pal_l2
		call spr_hide
		; clear tile definitions, maps, VRAM shadow, SMS RAM
		ld a,TILE_PAGE
		call clear_page
		ld a,TILE_PAGE+1
		call clear_page
		ld a,MAP_PAGE
		call clear_page
		ld a,SHADOW_PAGE
		call clear_page
		ld a,SHADOW_PAGE+1
		call clear_page
		ld a,SMSRAM_PAGE
		call clear_page
		ld a,(fw_flags)		; Layer 2 pages, with priority tiles
		rra
		jr nc,fw4_start__nl2
		ld b,6
		ld a,L2_PAGE
fw4_start__l2c:		push af
		push bc
		call clear_page
		pop bc
		pop af
		inc a
		djnz fw4_start__l2c
		ld b,10			; and the 320x256 Layer 2 of 224-line mode
		ld a,L2W_PAGE
fw4_start__l2w:		push af
		push bc
		call clear_page
		pop bc
		pop af
		inc a
		djnz fw4_start__l2w
fw4_start__nl2:
		ld b,4			; cart RAM ($FFFC bit 3); not kept on the SD card
		ld a,CARTRAM_PAGE
fw4_start__cr:		push af
		push bc
		call clear_page
		pop bc
		pop af
		inc a
		djnz fw4_start__cr
		ld a,(fw_flags)		; tilecache: the converted cart
		and 4
		call nz,tc_build
		jp tr_reset		; no traces from another game

; ----------------------------------------------------------------------
; The converted cart (kn_block in fw2): every 4 bytes of cart page n,
; converted as one row of a tile, into page CONVT_PAGE + n at the same
; offset. fw2 at $0000 for conv_tables, the cart page at $4000, the
; converted page at $6000; slots 0, 2 and 3 are put back after. Interrupts
; are off: SP walks the source.
; ----------------------------------------------------------------------
TCB_T		equ 255&((conv_tables-$2000)>>8)	; conv_tables with fw2 at $0000
tc_build:
		ld a,$50
		call nr_read
		ld (tcb_mmu),a
		ld a,$52
		call nr_read
		ld (tcb_mmu+1),a
		ld a,$53
		call nr_read
		ld (tcb_mmu+2),a
		nextreg $50,FW2_PAGE
		ld (tcb_sp),sp
		ld a,(fw_npages)
		ld (tcb_n),a
		ld a,CART_PAGE
tc_build__pg:	ld (tcb_pg),a
		nextreg $52,a
		add a,CONVT_PAGE-CART_PAGE
		nextreg $53,a
		ld sp,$4000
		ld ix,$6000
tc_build__row:	pop bc			; C, B, E, D = the row's four plane bytes
		pop de
		ld h,TCB_T
		ld l,d
		ld a,(hl)
		add a,a
		ld l,e
		or (hl)
		add a,a
		ld l,b
		or (hl)
		add a,a
		ld l,c
		or (hl)
		ld (ix+0),a
		inc h
		ld l,d
		ld a,(hl)
		add a,a
		ld l,e
		or (hl)
		add a,a
		ld l,b
		or (hl)
		add a,a
		ld l,c
		or (hl)
		ld (ix+1),a
		inc h
		ld l,d
		ld a,(hl)
		add a,a
		ld l,e
		or (hl)
		add a,a
		ld l,b
		or (hl)
		add a,a
		ld l,c
		or (hl)
		ld (ix+2),a
		inc h
		ld l,d
		ld a,(hl)
		add a,a
		ld l,e
		or (hl)
		add a,a
		ld l,b
		or (hl)
		add a,a
		ld l,c
		or (hl)
		ld (ix+3),a
		ld a,ixl
		add a,4
		ld ixl,a
		jr nc,tc_build__row
		inc ixh
		ld a,ixh
		cp $80
		jr nz,tc_build__row
		ld a,(tcb_n)
		dec a
		ld (tcb_n),a
		jr z,tc_build__end
		ld a,(tcb_pg)
		inc a
		jr tc_build__pg
tc_build__end:	ld sp,(tcb_sp)
		ld a,(tcb_mmu)
		nextreg $50,a
		ld a,(tcb_mmu+1)
		nextreg $52,a
		ld a,(tcb_mmu+2)
		nextreg $53,a
		ret
tcb_sp:		dw 0
tcb_n:		db 0
tcb_pg:		db 0
tcb_mmu:		ds 3

; ----------------------------------------------------------------------
; Leave the game (fw_quit in fw.asm jumps here): put NextZXOS's pages and
; registers back, slot 0 included, then fw_quit_t in fw.asm maps slot 1.
; ----------------------------------------------------------------------
fw_quit4:
		nextreg $62,0		; copper off
		nextreg $6B,0		; tilemap off
		nextreg $15,0		; sprites off
		ld bc,$123B		; Layer 2 off
		xor a
		out (c),a
		nextreg $71,0		; Layer 2 X scroll high bit (224-line mode)
		call spr_hide		; NextZXOS's $15 below may show the sprite layer
		nextreg $1C,%00001111	; every clip window back to the whole screen
		nextreg $18,0		; Layer 2
		nextreg $18,255
		nextreg $18,0
		nextreg $18,191
		nextreg $19,0		; sprites
		nextreg $19,255
		nextreg $19,0
		nextreg $19,191
		nextreg $1A,0		; ULA
		nextreg $1A,255
		nextreg $1A,0
		nextreg $1A,191
		nextreg $1B,0		; tilemap
		nextreg $1B,159
		nextreg $1B,0
		nextreg $1B,255
		nextreg $C0,0		; pulse interrupts
		nextreg $C4,1		; ULA interrupt only
		nextreg $22,0
		; silence the AY chips
		ld a,$FF
		call ay_quiet
		ld a,$FE
		call ay_quiet
		; NextZXOS's banks 5 and 7 back
		ld a,SAVE5_PAGE
		ld b,TILE_PAGE
		call copy_page
		ld a,SAVE5_PAGE+1
		ld b,TILE_PAGE+1
		call copy_page
		ld a,SAVE7_PAGE
		ld b,MAP_PAGE
		call copy_page
		; saved NextRegs
		ld hl,nr_keep
fw_quit4__r:		ld a,(hl)
		inc hl
		cp $FF
		jr z,fw_quit4__rd
		call nr_write_sel
		ld a,(hl)
		inc hl
		call nr_write_val
		jr fw_quit4__r
fw_quit4__rd:		nextreg $52,10
		nextreg $53,11
		nextreg $54,4
		nextreg $55,5
		nextreg $56,0
		nextreg $50,$FF
		ld a,$3F
		ld i,a
		im 1
		jp fw_quit_t

; All 128 hardware sprites hidden: 4-byte attributes with the visible bit
; clear. Uses A, BC, E.
spr_hide:	ld bc,$303B
		xor a
		out (c),a
		ld c,$57
		ld e,128
spr_hide__l:	out (c),a
		out (c),a
		out (c),a
		out (c),a
		dec e
		jr nz,spr_hide__l
		ret

ay_quiet:	ld e,7
		ld d,$3F
		push af
		call ay_write
		pop af
		ld e,8
		ld d,0
		push af
		call ay_write
		pop af
		ld e,9
		push af
		call ay_write
		pop af
		ld e,10
		jp ay_write

; A = source page, B = destination page: copy 8K (slots 0 and 6)
copy_page:	nextreg $50,a
		ld a,b
		nextreg $56,a
		ld hl,0
		ld de,$C000
		ld bc,$2000
		ldir
		ret


; A = page: fill it with zero, using slot 0.
clear_page:
		nextreg $50,a
		ld hl,0
		ld de,1
		ld bc,$1FFF
		ld (hl),0
		ldir
		nextreg $50,$FF
		ret

; A = NextReg $43 value: all 256 entries of that palette black
pal_black:	nextreg $43,a
		nextreg $40,0
		ld b,0
pal_black__l:		nextreg $44,0
		nextreg $44,0
		djnz pal_black__l
		ret
; The same for a Layer 2 palette, with entries 0 and 16 (pixel value 0 of
; either SMS palette) transparent
pal_l2:		call pal_black
		nextreg $40,0
		nextreg $44,L2_TRANS
		nextreg $44,0
		nextreg $40,16
		nextreg $44,L2_TRANS
		nextreg $44,0
		ret

; LD A,I (ed_ldai in fw.asm, through fw4_call): the game's A = its I
; (shadow_i); S and Z from the value, P/V = the game's IFF2, H = N = 0, C
; kept.
ed_ldai4:	ld hl,(fw_sp)
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
		jr nz,ed_ldai4__n
		or 4
ed_ldai4__n:	ld (hl),a
		ret

; ----------------------------------------------------------------------
; PSG (SN76489) -> AY, called from a handler through psg_w (fw.asm) and
; fw4_call. See the header there.
; ----------------------------------------------------------------------
psg_w2:
		bit 7,c
		jr z,psg_w2__data
		ld a,c
		rrca
		rrca
		rrca
		rrca
		and 7
		ld (psg_latch),a
		ld b,a
		ld a,c
		and $0F
		ld e,a
		ld a,b
		rrca
		and 3
		ld d,a			; channel
		bit 0,b
		jr nz,psg_w2__vol
		cp 3
		jr z,psg_w2__noise
		call tone_ptr
		ld a,(hl)
		and $F0
		or e
		ld (hl),a
		ld a,d
		jp tone_upd
psg_w2__vol:		ld a,e
		jr psg_w2__setvol
psg_w2__noise:		ld a,e
		jr psg_w2__setnoise
psg_w2__data:		ld a,(psg_latch)
		ld b,a
		rrca
		and 3
		ld d,a
		bit 0,b
		jr nz,psg_w2__vdata
		cp 3
		jr z,psg_w2__ndata
		call tone_ptr
		ld a,c
		and $0F
		swapnib
		ld e,a
		ld a,(hl)
		and $0F
		or e
		ld (hl),a
		inc hl
		ld a,c
		and $3F
		swapnib
		and 3
		ld (hl),a
		ld a,d
		jp tone_upd
psg_w2__vdata:		ld a,c
		and $0F
psg_w2__setvol:	ld e,a
		ld a,d
		add a,255&(psg_vol)
		ld l,a
		ld a,255&((psg_vol)>>8)
		adc a,0
		ld h,a
		ld (hl),e
		ld a,e
		add a,255&(ay_vol_table)
		ld l,a
		ld h,255&((ay_vol_table)>>8)
		ld e,(hl)
		ld a,d
		cp 3
		jr z,psg_w2__nvol
		add a,8
		ld d,e
		ld e,a
		ld a,$FF
		jp ay_write
psg_w2__nvol:		ld d,e
		ld e,8
		ld a,$FE
		jp ay_write
psg_w2__ndata:		ld a,c
psg_w2__setnoise:	and 7
		ld (psg_noise),a
		jp noise_upd

; A = channel -> HL = &psg_tone[ch]
tone_ptr:	add a,a
		add a,255&(psg_tone)
		ld l,a
		ld a,255&((psg_tone)>>8)
		adc a,0
		ld h,a
		ret

; A = channel: DE = AY period, N * 250 / 256 rounded (the exact ratio is
; 1.75 MHz * 2 / 3.579545 MHz = 0.9778; 250/256 = 0.9766)
tone_period:
		call tone_ptr
		ld a,(hl)
		inc hl
		ld b,(hl)		; N high
		ld d,a
		ld e,250
		mul d,e
		ld a,e
		add a,128		; round
		ld a,d
		adc a,0
		ld c,a			; (N low * 250 + 128) >> 8
		ld d,b
		ld e,250
		mul d,e			; N high * 250
		ld a,e
		add a,c
		ld e,a
		ld a,d
		adc a,0
		ld d,a
		ret

; A = channel 0-2: AY 0 tone period; channel 2 also moves the noise rate
tone_upd:
		push af
		call tone_period
		pop af
		push af
		add a,a
		ld c,a			; AY register (fine)
		ld b,d
		ld d,e
		ld e,c
		ld a,$FF
		push bc
		call ay_write
		pop bc
		inc c
		ld e,c
		ld d,b
		ld a,$FF
		call ay_write
		pop af
		cp 2
		ret nz
		ld a,(psg_noise)
		and 3
		cp 3
		ret nz
; noise register -> AY 1 channel A
noise_upd:
		ld a,(psg_noise)
		and 3
		cp 3
		jr z,noise_upd__t2
		; rates 0-2: the same as tone periods 16, 32, 64
		ld b,a
		ld hl,16
		inc b
noise_upd__sh:		dec b
		jr z,noise_upd__got
		add hl,hl
		jr noise_upd__sh
noise_upd__got:		ex de,hl
		ld a,e			; N
		ld d,a
		ld e,250
		mul d,e
		ld e,d
		ld d,0			; AY-equivalent period P
		jr noise_upd__have
noise_upd__t2:		ld a,2
		call tone_period	; DE = P of tone 2
noise_upd__have:		ld a,(psg_noise)
		and 4
		jr z,noise_upd__periodic
		; white: AY noise period = P, 1..31
		ld a,d
		or a
		ld a,31
		jr nz,noise_upd__np
		ld a,e
		cp 32
		jr c,noise_upd__np0
		ld a,31
noise_upd__np0:		or a
		jr nz,noise_upd__np
		inc a
noise_upd__np:		ld d,a
		ld e,6
		ld a,$FE
		call ay_write
		ld d,%00110111		; noise A on, tones off
		jr noise_upd__mix
noise_upd__periodic:	; tone at 1/16 of the shift rate: AY period 16 * P, at most 4095
		ex de,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		ld a,h
		cp $10
		jr c,noise_upd__pok
		ld hl,$0FFF
noise_upd__pok:		push hl
		ld d,l
		ld e,0
		ld a,$FE
		call ay_write
		pop hl
		ld d,h
		ld e,1
		ld a,$FE
		call ay_write
		ld d,%00111110		; tone A on, noise off
noise_upd__mix:		ld e,7
		ld a,$FE
		jp ay_write


		include "trbuild.asm"

; ======================================================================
; jt_vwrite's one-byte form (fw.asm fw_vwrite), run with this page in
; slot 1 in place of MAP_PAGE: runs of one byte, a source step of 0 or 1, and all the
; source inside one 8K page. Each byte goes to the shadow and marks its
; tile, as vw_tiles does; the tile marks of a VRAM page are kept in C and
; written when the page changes and at the end. The first byte outside the
; tiles hands the rest of the runs to vw_run.
vt_try:		ld a,d
		ld (vt_r0+1),a
vt_r0:		ld a,(region_tab)	; (patched: the first byte's VRAM page)
		or a
		jp nz,vt_out		; not a tile: the general path at once
		ld a,ixh
		or a
		jp nz,vt_out
		ld a,ixl
		cp 2
		jp nc,vt_out		; a source step other than 0 or 1
		ld b,a
		push hl
		or a
		jr z,vt_try__s
		ld a,(vw_runs)
		dec a			; runs - 1
		add a,l
		ld l,a
		jr nc,vt_try__s
		inc h
		jr nz,vt_try__s
		pop hl
		jp vt_out		; the source runs past $FFFF
vt_try__s:	ld a,h			; the last byte's source
		pop hl
		xor h
		and $E0
		jp nz,vt_out		; the source crosses an 8K page
		ld a,b
		or a
		ld a,$23		; INC HL
		jr nz,vt_try__i
		xor a			; NOP
vt_try__i:	ld (vt_inc),a
		ld (vt_dv+2),iy
		ld a,h
		and $E0
		call vw_map
		ld a,h
		and $1F
		ld h,a			; the source in slot 0
		ld a,$FF
		ld (vt_pg+1),a		; no VRAM page yet
		ld a,(vw_runs)
		ld b,a			; runs (0 = 256)
		ld c,0			; the tile marks of the current VRAM page
vt_loop:	ld a,d			; HL = source, DE = VRAM address
vt_pg:		cp $FF			; (patched: the VRAM page of the last byte)
		jr nz,vt_page
vt_b:		ld a,(hl)
		set 7,d
		ld (de),a		; the shadow
		res 7,d
		ld a,e
		rlca
		rlca
		rlca
		and 7
		or 255&vt_bit
		ld (vt_bt+1),a
vt_bt:		ld a,(vt_bit)		; (patched: the byte's tile in the page)
		or c
		ld c,a
vt_inc:		inc hl			; (patched: INC HL or NOP)
vt_dv:		add de,0		; (patched: the VRAM step)
		ld a,d
		and $3F
		ld d,a
		djnz vt_loop
		call vt_flush
		push hl
		ld hl,(tw_cnt)		; tile bytes written: runs (0 = 256)
		ld a,(vw_runs)
		dec a
		add hl,a
		inc hl
		ld (tw_cnt),hl
		ex de,hl		; the VDP address: after the last byte
		ld bc,(vw_vstep)
		or a
		sbc hl,bc
		inc hl
		ld a,h
		and $3F
		ld h,a
		ld (vdp_addr),hl
		pop hl
		jp vw_end
vt_page:	call vt_flush
		ld a,d
		ld (vt_pg+1),a
		ld (vt_rg+1),a
vt_rg:		ld a,(region_tab)	; (patched: the VRAM page)
		or a
		jr z,vt_b
		ld a,(vw_runs)		; not a tile page: the rest through vw_run
		sub b			; the bytes written
		push hl
		ld hl,(tw_cnt)
		add hl,a
		ld (tw_cnt),hl
		pop hl
		ld a,b
		ld (vw_runs),a		; the runs left (0 = 256)
		ld a,(vw_k+1)
		or h
		ld h,a			; HL = the source as the caller gave it
		ld c,0			; one byte in each run
vt_out:		jp vt_back		; MAP_PAGE back in slot 1, then vw_run
; C = tile marks for the VRAM page in vt_pg: into dirty_pages, then C = 0.
vt_flush:	ld a,c
		or a
		ret z
		push hl
		ld a,(vt_pg+1)
		or $40
		ld l,a
		ld h,255&((region_tab)>>8)	; dirty_pages
		ld a,c
		or (hl)
		ld (hl),a
		ld (tiles_dirty),a
		pop hl
		ld c,0
		ret
		align 8
vt_bit:		db $01,$02,$04,$08,$10,$20,$40,$80	; the bit of tile k in a VRAM page


; A = NextReg A
nr_read:
		push bc
		ld bc,$243B
		out (c),a
		inc b
		in a,(c)
		pop bc
		ret

NR_KEEP		equ 48			; at most 48 bytes, the room at nr_saved (fw.asm)
nr_keep:	ds NR_KEEP		; NextReg values to restore on quit
psg_latch:	db 0			; latched channel*2 + type
psg_tone:	dw 0,0,0		; 10-bit tone registers
psg_vol:	db 15,15,15,15
psg_noise:	db 0
ay_cur:		db 0			; AY chip selected now ($FF AY0, $FE AY1)

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

		IFDEF TRACE_BUILD
		include "vdpcheck4.asm"
		ENDIF

fw4_end:
; assert fw4_end <= $4000 (an overflow is an assembler error in runtime.asm)
