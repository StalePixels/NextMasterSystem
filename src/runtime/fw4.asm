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
		ld hl,cram		; the CRAM copy as the palettes now are: all 0
		ld b,32			; (page code that reads cram)
fw4_start__cz:		ld (hl),0
		inc hl
		djnz fw4_start__cz
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
		call wl_setup
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
		ld h,(hl)
		ld l,a
; HL = SN period N: DE = AY period, N * 250 / 256 rounded. Uses A, C.
n_period:
		ld d,l
		ld e,250
		mul d,e
		ld a,e
		add a,128		; round
		ld a,d
		adc a,0
		ld c,a			; (N low * 250 + 128) >> 8
		ld d,h
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
		; rates 0-2: the shift rate of tone periods 16, 32, 64
		ld b,a
		ld hl,16
		inc b
noise_upd__sh:		dec b
		jr z,noise_upd__have
		add hl,hl
		jr noise_upd__sh
noise_upd__t2:		ld a,2			; rate 3: tone 2's period
		call tone_ptr
		ld a,(hl)
		inc hl
		ld h,(hl)
		ld l,a
noise_upd__have:		ld a,(psg_noise)	; HL = N: the LFSR shifts at tone period N's rate
		and 4
		jr z,noise_upd__periodic
		; white: AY noise period = P, the AY period of N, 1..31
		call n_period
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
noise_upd__periodic:	; tone at 1/16 of the shift rate: AY period 16 * N * 250 / 256
		ld b,h			; = 16N - 3N/8, at most 4095
		ld c,l
		add hl,hl
		add hl,bc
		srl h
		rr l
		srl h
		rr l
		srl h
		rr l
		ex de,hl		; DE = 3N/8
		ld h,b
		ld l,c
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl		; 16N (N < 1024)
		or a
		sbc hl,de
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

; The segment list of the rastseg switch in 224-line mode, called by
; cop_seg in fw3 with this page at $2000 in place of part 2 (see cop_seg
; there for the list).
cop_seg4:	ld a,(rx_tabok)
		or a
		call z,rx_mktab
		ld a,(cs_mode)
		sub 4
		ld c,a			; C not 0: whole
		ld hl,hl_tab
		ld de,SG2_L		; E = segment
		ld b,0			; B = the line before
cop_seg__rd:	ld a,(hl)
		inc l
		inc e
		dec e
		jr z,cop_seg__r0
		cp b
		jr c,cop_seg__rx
		jr z,cop_seg__rx
		cp 224
		jr nc,cop_seg__rx
		jr cop_seg__r2
cop_seg__r0:	xor a			; the first segment: line 0
cop_seg__r2:	ld b,a
		ex de,hl
		cp (hl)
		jr z,cop_seg__r3
		ld (hl),a		; SG2_L: another line than in the list
		ld c,1
cop_seg__r3:	ex de,hl
		ld a,(hl)
		inc l
		set 5,e
		ld (de),a		; SG2_H
		res 5,e
		inc e
		ld a,e
		cp SG2_MAX
		jr c,cop_seg__rd
cop_seg__rx:	ld a,(cs_n)
		cp e
		jr z,cop_seg__nn
		ld c,1
cop_seg__nn:	ld a,e
		ld (cs_n),a
		ld a,c
		ld (cs_full),a
		; the head: X of line 16's segment, Y (also straight into $31), and
		; for a whole list the map and the ULA
		ld de,SG2_L
cop_seg__f:	ld a,e
		inc a
		ld hl,cs_n
		cp (hl)
		jr nc,cop_seg__f1
		inc e
		ld a,(de)
		cp 17
		jr c,cop_seg__f
		dec e
cop_seg__f1:	ld a,e
		call cs_seg
		nextreg $61,0
		nextreg $62,%11000000
		nextreg $60,$2F
		ld a,(cs_xh)
		nextreg $60,a
		nextreg $60,$30
		ld a,(cs_xl)
		nextreg $60,a
		nextreg $60,$31
		ld a,(vdp_regs+9)
		add a,240
		nextreg $60,a
		nextreg $31,a
		ld a,(cs_full)
		or a
		jr z,cop_seg__h
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		nextreg $60,$68
		nextreg $60,0
cop_seg__h:	ld hl,10
		ld (cs_idx),hl
		ld b,16			; B = SMS line: 16-223 are Next lines 0-207
cop_seg__l1:	ld a,(cs_nx)
		cp b
		call z,cs_next
		ld a,b
		cp 208
		jr nz,cop_seg__l1b
		ld de,192
		ld a,$80
		call cs_u		; ULA off from Next line 192
cop_seg__l1b:	ld c,224		; the run ends at the next segment, line 208 or 224
		ld a,b
		cp 208
		jr nc,cop_seg__l1c
		ld c,208
cop_seg__l1c:	ld a,(cs_nx)
		cp c
		jr nc,cop_seg__l1d
		ld c,a
cop_seg__l1d:	ld a,c
		sub b
		ld c,a			; C = lines
		ld a,b
		sub 16
		ld e,a
		ld d,0
		push bc
		call cs_run
		pop bc
		ld a,b
		add a,c
		ld b,a
		cp 224
		jr nz,cop_seg__l1
		ld de,208
		xor a
		call cs_u		; ULA on from Next line 208
		xor a
		call cs_seg
		call cs_xmv		; X for the lines above line 0
		call cur_line
		ld hl,pic_end
		cp (hl)
		jr c,cop_seg__nd	; the copper has not passed that MOVE yet
		ld a,(cs_xh)
		nextreg $2F,a
		ld a,(cs_xl)
		nextreg $30,a
cop_seg__nd:	ld de,(cop_top)
		ld a,$80
		call cs_u		; ULA off from cop_top
		ld hl,(cop_top)		; cs_s256: the first of SMS lines 0-15 on Next line 256 or later
		ld a,h
		or a
		ld a,0
		jr nz,cop_seg__s
		sub l
cop_seg__s:	ld (cs_s256),a
		ld b,0			; SMS lines 0-15 are Next lines cop_top on
cop_seg__l2:	ld a,b
		or a
		jr z,cop_seg__l2a
		ld a,(cs_nx)
		cp b
		call z,cs_next
cop_seg__l2a:	ld c,16			; the run ends at the next segment, line 16, or cs_s256
		ld a,(cs_s256)
		cp b
		jr c,cop_seg__l2b
		jr z,cop_seg__l2b
		cp c
		jr nc,cop_seg__l2b
		ld c,a
cop_seg__l2b:	ld a,(cs_nx)
		cp c
		jr nc,cop_seg__l2c
		ld c,a
cop_seg__l2c:	ld a,c
		sub b
		ld c,a			; C = lines
		ld hl,(cop_top)
		ld a,b
		add hl,a
		ex de,hl		; DE = its first Next line
		push bc
		call cs_run
		pop bc
		ld a,b
		add a,c
		ld b,a
		cp 16
		jr nz,cop_seg__l2
		ld a,(cs_full)
		or a
		jr z,cop_seg__e
		nextreg $60,$FF		; HALT
		nextreg $60,$FF
cop_seg__e:	ld hl,SG2_H		; the H now in the list
		ld de,SG2_P
		ld bc,SG2_MAX
		ldir
		ret
; the next segment and its X MOVEs. Keeps B.
cs_next:	ld a,(cs_k)
		inc a
		call cs_seg
; MOVE $2F,X hi; MOVE $30,X lo of the segment
cs_xmv:		ld a,(cs_full)
		or a
		jr z,cs_xmv__i
		nextreg $60,$2F
		ld a,(cs_xh)
		nextreg $60,a
		nextreg $60,$30
		ld a,(cs_xl)
		nextreg $60,a
		jr cs_adv4
cs_xmv__i:	ld a,(cs_chg)
		or a
		jr z,cs_adv4
		ld hl,(cs_idx)
		inc hl
		call cs_at
		ld a,(cs_xh)
		nextreg $60,a
		inc hl
		inc hl
		call cs_at
		ld a,(cs_xl)
		nextreg $60,a
cs_adv4:	ld a,4
cs_adv:		ld hl,(cs_idx)
		add hl,a
		ld (cs_idx),hl
		ret
; DE = Next line, A = the ULA's NextReg $68 value: WAIT line,0; MOVE $68,A
cs_u:		ld c,a
		ld a,(cs_full)
		or a
		jr z,cs_adv4
		ld a,$80
		or d
		nextreg $60,a
		ld a,e
		nextreg $60,a
		nextreg $60,$68
		ld a,c
		nextreg $60,a
		jr cs_adv4
; C lines from Next line DE, all of the segment and on the same side of
; line 256: their switch pairs, whole, or for a segment whose H changed the
; first byte of each WAIT (cop_224__run in fw3), or none
cs_run:		ld a,(cs_full)
		or a
		jr z,cs_run__i
cs_run__f:	call cs_pair
		inc de
		dec c
		jr nz,cs_run__f
		ret
cs_run__i:	ld a,(cs_chg)
		or a
		jr nz,cs_run__w
		ld e,c			; the list stands: past its pairs
		ld d,8
		mul d,e
		ld hl,(cs_idx)
		add hl,de
		ld (cs_idx),hl
		ret
cs_run__w:	ld a,(cs_col)
		or d
		ld d,a
		ld b,c
		ld hl,(cs_idx)
		call cop_224__run
		ld (cs_idx),hl
		ret
; DE = Next line: its switch pair with the segment's column. Keeps B, C, DE.
cs_pair:	ld a,(cs_full)
		or a
		jr z,cs_pair__i
		ld a,(cs_col)
		or d
		nextreg $60,a		; WAIT line,column
		ld a,e
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_A8
		ld a,$80 + (END_H << 1)
		or d
		nextreg $60,a		; WAIT line,40
		ld a,e
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		jr cs_adv8
cs_pair__i:	ld a,(cs_chg)
		or a
		jr z,cs_adv8
		ld hl,(cs_idx)
		call cs_at
		ld a,(cs_col)
		or d
		nextreg $60,a
cs_adv8:	ld a,8
		jp cs_adv
; HL = list byte: the copper write index (the copper keeps running)
cs_at:		ld a,l
		nextreg $61,a
		ld a,h
		or %11000000
		nextreg $62,a
		ret
; A = segment: cs_k, cs_nx, cs_chg, cs_col, cs_xh, cs_xl (rx_tab)
cs_seg:		ld (cs_k),a
		ld e,a
		ld d,255&(SG2_L>>8)
		inc a
		ld hl,cs_n
		cp (hl)
		ld a,224
		jr nc,cs_seg__l
		inc e
		ld a,(de)
		dec e
cs_seg__l:	ld (cs_nx),a
		set 5,e
		ld a,(de)		; H
		ld c,a
		res 5,e
		set 6,e
		ld a,(de)		; its H in the list
		sub c
		ld (cs_chg),a
		ld l,c
		ld h,255&(rx_tab>>8)
		ld a,(hl)
		or a
		jr nz,cs_seg__c
		ld a,39
cs_seg__c:	add a,a
		or $80
		ld (cs_col),a
		inc h
		ld a,(hl)
		ld (cs_xh),a
		inc h
		ld a,(hl)
		ld (cs_xl),a
		ret

; collline, from a status read (cl_rd, fw.asm, through fw4_call): in the
; picture, from the collision line on (cl_line, worked out by cl_scan in
; fw3), with the display on, the first read of each picture gets bit 5.
; cl_vbl (fw3) arms it again once a frame: 1, or 2 when the once-a-frame
; work ran in the picture (workline). With 2 the reads in the rest of that
; picture do not get the bit, and the sprite table that cl_scan read may be
; older than the next picture's: a read below the picture (the frame
; handler's) makes it 3, and the first read in the next picture works out
; cl_line again from the sprite table as the frame handler left it
; (cl_fresh), then goes on as with 1.
cl_read:	ld a,(cl_arm)
		or a
		ret z
		call cur_line
		ld hl,pic_end
		cp (hl)
		jr nc,cl_read__b	; not in the picture
		ld a,(cl_arm)
		cp 2
		ret z			; armed in this picture: from the next one on
		cp 3
		call z,cl_fresh
		call cur_line
		ld hl,cl_line
		cp (hl)
		ret c			; above the collision line
		ld a,(vdp_regs+1)
		and $40
		ret z			; display off: the SMS draws no sprites
		xor a
		ld (cl_arm),a
		ld hl,vdp_status
		set 5,(hl)
		ret
cl_read__b:	ld hl,cl_arm		; below the picture: 2 becomes 3
		ld a,(hl)
		cp 2
		ret nz
		inc (hl)
		ret
; cl_scan (fw3 at $0000) with the VRAM copy at $4000, as in the once-a-frame
; work; the game's pages back after it. Keeps BC and DE. About 5,000 cycles.
cl_fresh:	ld a,1
		ld (cl_arm),a
		nextreg $50,FW3_PAGE
		nextreg $52,SHADOW_PAGE
		nextreg $53,SHADOW_PAGE+1
		push bc
		push de
		call cl_scan
		pop de
		pop bc
		ld a,(cur_mmu+0)
		nextreg $50,a
		ld a,(cur_mmu+2)
		nextreg $52,a
		ld a,(cur_mmu+3)
		nextreg $53,a
		ret

; ----------------------------------------------------------------------
; The work line (CONF workline=N). The once-a-frame work runs from a line
; interrupt at SMS line N of the picture, not from the ULA interrupt below
; the picture: a game whose frame handler must reach a line in the next
; picture on time (Fantastic Dizzy's status bar split) then has the time
; from the frame event to that line for itself. The ULA interrupt sets the
; line interrupt for line N (wl_ula4); the work line goes through
; fw_ula_irq, which runs the work (wl_line, wl_line4). The frame event and
; the SMS line events keep the line interrupt; with a line event set at the
; ULA interrupt the work runs there, as without the switch. A work line that
; did not come by the next ULA interrupt (the game kept interrupts off past
; the frame event, or set a line event) has the work run there. V counter
; reads below the picture do not run the work (rv_hk, vf_hk), and the ULA
; interrupt does not arm vbl_chk.
; ----------------------------------------------------------------------
wl_n		equ nr_keep+43		; N, 0 = off: the loader writes it after its
					; NextReg list (struct nm_launch: wline after nr)
wl_pend:	db 0			; 1: the line interrupt is set for the work line;
					; 2: the work line came, fw_ula_irq runs the work

; Game start (fw4_start): the four hooks on with the switch, off without
; it, so that a game loaded after another one starts clean.
wl_setup:	xor a
		ld (wl_pend),a
		ld hl,cur_line
		ld de,hl_on
		ld bc,$3A20		; B = LD A,(nn), C = JR NZ,e
		ld a,(wl_n)
		or a
		jr z,wl_setup__w
		ld hl,wl_ula
		ld de,wl_line
		ld bc,$CD18		; CALL nn, JR e
wl_setup__w:	ld (ula_hk+1),hl
		ld a,b
		ld (fl_hk),a
		ld (fl_hk+1),de
		ld a,c
		ld (rv_hk),a
		ld (vf_hk),a
		ret

; Each line interrupt (fl_hk, through wl_line). NZ: the work line (the line
; interrupt was set for it, the beam is in the picture and no SMS line event
; is set), and wl_pend 2 for wl_ula4. Else Z and A = hl_on.
wl_line4:	ld a,(wl_pend)
		dec a
		jr nz,wl_line4__n
		call cur_line
		ld hl,pic_end
		cp (hl)
		jr nc,wl_line4__n	; below the picture: the frame event
		ld a,(ev_next)
		cp 192
		jr nz,wl_line4__n	; an SMS line event
		ld a,2
		ld (wl_pend),a
		or a
		ret
wl_line4__n:	ld a,(hl_on)
		cp a
		ret

; fw_ula_irq (ula_hk, through wl_ula), at the ULA interrupt and at the work
; line. vbl_poll 0: the work runs now; 1: it waits for the work line. Returns
; A = 255, so that fw_ula_irq does not arm vbl_chk. Uses B, C, HL.
wl_ula4:	ld a,(wl_pend)
		or a
		jr z,wl_ula4__arm
		xor a			; the work line came (2), or did not come since the
		ld (wl_pend),a		; last ULA interrupt (1): the work now, and the
		ld a,(ev_next)		; next event back in the line interrupt
		call ev_program
		jr wl_ula4__now
wl_ula4__arm:	ld a,(ev_next)
		cp 192
		jr nz,wl_ula4__now	; a line event is set: the work now
		ld a,(pic_end)
		sub 192
		ld b,a			; 16 in 224-line mode
		ld a,(wl_n)
		sub b
		jr nc,wl_ula4__t
		xor a			; N in the 16 lines above line 0: Next line 0
wl_ula4__t:	ld c,a			; C = the Next line of SMS line N
		call cur_line
		ld hl,pic_end
		cp (hl)
		jr nc,wl_ula4__set	; below the picture
		cp c
		jr nc,wl_ula4__now	; held into the picture past the line
wl_ula4__set:	ld a,c
		nextreg $23,a
		ld a,1
		ld (wl_pend),a
		jr wl_ula4__x
wl_ula4__now:	xor a
wl_ula4__x:	ld (vbl_poll),a
		ld a,255
		ret

		IFDEF TRACE_BUILD
		include "vdpcheck4.asm"
		ENDIF

; From ed_dispatch (fw.asm, through fw4_call), A = an inline code it does not know. $76 is a
; HALT, $FB an EI then a HALT, $C9 a HALT then a RET (ABI 9); any other code
; stops the game. fw_exit then returns to hw_loop (fw.asm), which waits for
; the game's own interrupt, or with the game's interrupts off to hw_dead.
; The return address the wait ends with is on the game's stack: for $76
; and $FB the byte after the site, in a word below the RST's slot (the
; trap's game AF and HL move down one word); for $C9 the slot is the one
; fw_exit takes, so the wait returns to the game's own caller.
op_halt:	cp $C9
		jr z,op_halt__arm
		cp $76
		jr z,op_halt__site
		cp $FB
		jp nz,fw_fatal
		ld (exit_ei),a		; EI then HALT: the game's interrupts on
op_halt__site:	ld hl,(fw_sp)
		ld e,(hl)
		inc hl
		ld d,(hl)		; DE = game AF
		inc hl
		ld c,(hl)
		inc hl
		ld b,(hl)		; BC = game HL, from the RST's slot
		ld a,(fw_ret+1)
		ld (hl),a
		dec hl
		ld a,(fw_ret)
		ld (hl),a		; the slot = the byte after the site
		dec hl
		ld (hl),b
		dec hl
		ld (hl),c
		dec hl
		ld (hl),d
		dec hl
		ld (hl),e
		ld (fw_sp),hl
op_halt__arm:	ld a,(exit_ei)
		or a
		ld hl,hw_dead
		jr z,op_halt__go	; interrupts off: NOP in exit_ei
		ld hl,(irq_t1+1)
		ld de,hw_irq
		or a
		sbc hl,de
		jr z,op_halt__on	; already waiting
		add hl,de
		ld (hw_irq_j+1),hl
		ex de,hl
		ld (irq_t1+1),hl
		ld (irq_t2+1),hl
		ld hl,frm_run__no	; no event held while the game waits
		ld (frm_t1+1),hl
		ld (frm_t2+1),hl
op_halt__on:	xor a			; jr hw_wait
		ld (hw_jr+1),a
		ld hl,hw_loop
op_halt__go:	ld (fw_ret),hl
		ret
; From hw_irq (fw.asm, through fw4_call): the game's interrupt has come, so
; the wait ends, and irq_t1, irq_t2, frm_t1 and frm_t2 get their targets back.
hw_hit:		ld a,hw_done-hw_wait
		ld (hw_jr+1),a
		ld hl,(hw_irq_j+1)
		ld (irq_t1+1),hl
		ld (irq_t2+1),hl
		ld hl,frm_run
		ld (frm_t1+1),hl
		ld (frm_t2+1),hl
		ret

fw4_end:
; assert fw4_end <= $4000 (an overflow is an assembler error in runtime.asm)
