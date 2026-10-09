; fw2.asm: the framework's once-a-frame work. Page FW2_PAGE, mapped at
; $2000 (MMU1) only while vbl_work (fw.asm) runs it, with interrupts off.
; At that time the VRAM shadow is at $4000-$7FFF (VRAM address + $4000)
; and the Next tile definitions at $8000-$BFFF (tile * 32 + $8000).

;		org $2000  (section origin)
		include "tables2.inc"	; conv_tables, 1K, page aligned
tile_slot:	ds 512			; per SMS tile: pattern slot | $80, 0 = none
; assert low tile_slot == 0, "spr_update indexes tile_slot by page" (checked by tools/check-layout)
slot_tile:	ds 256			; per pattern slot: SMS tile, $FFFF = none
slot_stamp:	ds 128			; per pattern slot: spr_frame of last use
; assert low slot_stamp == 0, "spr_update indexes slot_stamp by page" (checked by tools/check-layout)
spr_last:	db 64			; sprites written last frame
spr_mode:	db $FF			; reg1 bit 1 | reg6 bit 2 the cache was built for
spr_frame:	db 0
spr_rr:		db 0			; round-robin pointer for slot eviction
spr_count:	db 0
spr_t:		dw 0
cv_n:		db 0
pause_prev:	db 0

fw2_init:
		ld hl,tm_valid
		ld de,tm_valid+1
		ld bc,63
		ld (hl),0
		ldir
		ld hl,tile_slot
		ld de,tile_slot+1
		ld bc,511
		ld (hl),0
		ldir
		ld hl,slot_tile
		ld de,slot_tile+1
		ld bc,255
		ld (hl),$FF
		ldir
		ld hl,slot_stamp
		ld de,slot_stamp+1
		ld bc,127
		ld (hl),0
		ldir
		ld a,64
		ld (spr_last),a
		ld a,$FF
		ld (spr_mode),a
		ld a,1
		ld (spr_frame),a
		ret

; The vb_ labels mark the phases for tools/measure.lua (NM_VBPH).
fw2_vbl:
		nextreg $50,FW3_PAGE	; fw3 at $0000 (restore_mmu puts the game's page back)
		; the copper first: a full rebuild must end before line 0, or that
		; frame runs without its copper list
vb_cop:		call rast_frame
		ld a,(hl_on)
		or a
		jr nz,vb_kbd
		ld a,(cop_dirty)
		or a
		call nz,cop_update
vb_kbd:		call kbd_scan
vb_map:		ld a,(nt_dirty)
		or a
		call nz,map_rebuild
vb_tile:	ld a,(tiles_dirty)
		or a
		call nz,tile_flush
vb_pal:		ld a,(fw_frames)
		and 7
		call z,pal_scan
		ld hl,(tr_free)		; no free pixel value: one more row of pal_rows
		ld a,h
		or l
		call z,pal_rows_step
vb_pri:		call pri_frame
vb_spr:		call spr_update
vb_end:		ld hl,(fw_frames)
		inc hl
		ld (fw_frames),hl
		ret

; ----------------------------------------------------------------------
; Game start set-up, called by fw_start (fw.asm) with this page at $2000:
; NextRegs, sound, video, cleared pages, framework state, the game's
; first pages in cur_mmu. fw_start then maps them and starts the game.
; ----------------------------------------------------------------------
fw2_start:
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
		call clip_update
		nextreg $2F,255&(((288-PIC_X))>>8)	; X offset for H scroll 0
		nextreg $30,255&((288-PIC_X))
		nextreg $31,224
		nextreg $62,0		; copper stopped
		; sprite palette: all black
		nextreg $43,%00100010
		nextreg $40,0
		ld b,0
fw2_start__spal:		nextreg $44,0
		nextreg $44,0
		djnz fw2_start__spal
		; tilemap palette 0: all black
		nextreg $43,%00110010
		nextreg $40,0
		ld b,0
fw2_start__pal:		nextreg $44,0
		nextreg $44,0
		djnz fw2_start__pal
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
		; all 128 sprites hidden
		ld bc,$303B
		xor a
		out (c),a
		ld c,$57
		ld e,128
fw2_start__spr:		out (c),a
		out (c),a
		out (c),a
		out (c),a		; 4-byte form, not visible
		dec e
		jr nz,fw2_start__spr
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
		jr nc,fw2_start__nl2
		ld b,6
		ld a,L2_PAGE
fw2_start__l2c:		push af
		push bc
		call clear_page
		pop bc
		pop af
		inc a
		djnz fw2_start__l2c
fw2_start__nl2:
		ld b,4			; cart RAM ($FFFC bit 3); not kept on the SD card
		ld a,CARTRAM_PAGE
fw2_start__cr:		push af
		push bc
		call clear_page
		pop bc
		pop af
		inc a
		djnz fw2_start__cr
		; framework state
		ld hl,vdp_regs
		ld b,16
fw2_start__zr:		ld (hl),0
		inc hl
		djnz fw2_start__zr
		ld a,192
		ld (pic_end),a
		ld a,$FF
		ld (vdp_regs+10),a
		ld (cop_sw),a
		ld (cop_v),a
		ld (cop_mode),a
		ld hl,$3800
		ld (nt_base),hl
		ld a,$3F
		ld (sat_hi),a
		call region_update
		ld hl,dirty_pages
		ld b,64
fw2_start__zd:		ld (hl),0
		inc l
		djnz fw2_start__zd
		xor a
		ld (tiles_dirty),a
		ld (vbl_done),a
		ld (quit_req),a
		ld (pause_req),a
		ld (vdp_status),a
		ld (vdp_latch),a
		ld (h_sw),a
		ld (m224),a
		inc a
		ld (sat_dirty),a
		ld (cop_dirty),a
		ld hl,0
		ld (fw_frames),hl
		dec hl
		ld (tr_free),hl
		ld a,$FF
		ld (bd_cur),a
		call tr_reset		; no traces from another game
		nextreg $1C,%00000100	; ULA clip: SMS column 0 only
		nextreg $1A,0
		nextreg $1A,PIC_X+7
		nextreg $1A,0
		nextreg $1A,191
		ld hl,286
		ld (h_x),hl
		call fw2_switches
		nextreg $50,FW3_PAGE	; fw2_init clears tm_valid there
		call fw2_init
		; interrupts: hardware IM2 mode (held until acknowledged), vector
		; table at $FD00 (I = $FD). Line interrupt (SMS frame and line
		; events) and ULA interrupt (framework work) on.
		nextreg $C0,%00000001
		nextreg $C5,0
		nextreg $C6,0
		nextreg $C4,%00000011
		nextreg $22,%00000010	; line interrupt on, ULA on, line MSB 0
		ld a,192
		call ev_program
		ld a,$FD
		ld i,a
		; SMS mapping: cart in 0-5 (mapper reset state 0,1,2), RAM in 6
		ld a,$FF
		ld ($FFFC),a		; mapper register copies read back by games
		xor a
		ld ($FFFC),a
		ld ($FFFD),a
		inc a
		ld ($FFFE),a
		inc a
		ld ($FFFF),a
		ld a,(fw_npages)
		ld c,a
		ld b,0
		ld hl,cur_mmu
fw2_start__map:		ld a,b
		call mod_c
		add a,CART_PAGE
		ld (hl),a
		inc hl
		inc b
		ld a,b
		cp 6
		jr nz,fw2_start__map
		ld (hl),SMSRAM_PAGE
		inc hl
		ld (hl),FW_PAGE
		ld a,8
		ld (fw_status),a
		ret

; ----------------------------------------------------------------------
; Mapper stores, called by op_mapper (fw.asm) from a handler, with this
; page at $2000 for the call. A = op:
;   $10-$13  LD ($FFFC+k),A, site 32 nn FF: RST, op, one byte skipped
;   $14      LD HL,$FFFF; LD (HL),n, site 21 FF FF 36 n: RST, op, n, two
;            bytes skipped; game HL = $FFFF afterwards
;   $15-$17  LD ($FFFC+k),HL, site 22 nn FF: RST, op, one byte skipped
;   $20-$23  LD ($FFFC+k),BC, site ED 43 nn FF: RST, op, two bytes skipped
;   $24-$27  LD ($FFFC+k),DE, site ED 53 nn FF: RST, op, two bytes skipped
;   $28-$2B  LD HL,$FFFC+k; LD (HL),n, site 21 nn FF 36 n: RST, op, n, two
;            bytes skipped; game HL = $FFFC+k afterwards
;   $2C-$2E  Codemasters mapper: LD ($0000/$4000/$8000),A, site 32 00 nn:
;            RST, op, one byte skipped; slot 0/1/2 gets bank A
;   $2F      apply the overlay's RAM code patch table (HOOK kind 2) and go
;            on at its continuation address (site: a JP, 3 bytes)
;   $30-$3F  LD (HL),n with n = op - $30 and game HL = $FFFC-$FFFF (36 n)
; The value goes to $FFFC+k in the framework page (games read the
; registers back there) and to the RAM copy at $DFFC+k, as on the SMS,
; then the slot is remapped ($FFFC: cart RAM, fffc_apply).
; ----------------------------------------------------------------------
cold_mapper:
		cp $20
		jp nc,cold_mapper__new
		ld hl,(fw_ret)
		cp $15
		jr nc,cold_mapper__hl
		cp $14
		jr z,cold_mapper__ld
		inc hl			; skip the third byte of LD (nn),A
		ld (fw_ret),hl
		and 3
		add a,$FC
		ld e,a
		; LD (nn),A into SMS RAM right after it (games keep a copy of the
		; bank: Sonic's ld ($FFFE),a; ld ($D235),a): done here too, so that
		; no interrupt comes between the two. On the Next the frame
		; interrupt can land there, and Sonic's handler then puts back the
		; old bank from the copy.
		ld a,(op_nx)
		cp $32
		jr nz,cold_mapper__nf
		ld a,(op_nx+2)
		cp $C0
		jr c,cold_mapper__nf
		cp $E0
		jr nc,cold_mapper__nf
		ld hl,(op_nx+1)
		ld a,(game_a)
		ld (hl),a
		ld hl,(fw_ret)
		inc hl
		inc hl
		inc hl
		ld (fw_ret),hl
cold_mapper__nf:		ld a,(game_a)
		jr cold_mapper__st
cold_mapper__ld:		ld a,$FF
cold_mapper__ldk:		ld e,a			; E = register low byte
		ld a,(op_n)		; n (read by op_mapper)
		inc hl
		inc hl
		inc hl
		ld (fw_ret),hl
		push af
		push de
		ld l,e
		ld h,$FF
		call set_game_hl
		pop de
		pop af
cold_mapper__st:		ld d,$FF
		ld (de),a
		ld d,$DF
		ld (de),a
		ld c,a
		ld a,e
		sub $FD
		jp c,fffc_apply		; $FFFC: cart RAM control
		add a,a			; first MMU slot
		ld e,a
		ld a,c
		jp map_bank
cold_mapper__hl:		; $15-$17: LD ($FFFC+k),HL: L to register k, H to k+1
		inc hl
		ld (fw_ret),hl
		sub $15
		add a,$FC
		push af
		call game_hl
		pop af
cold_mapper__pair:		; A = register low byte, HL = value
		push hl
		ld e,a
		ld a,l
		call cold_mapper__one
		pop hl
		inc e
		ld a,h
cold_mapper__one:		; E = register low byte, A = value
		push de
		ld d,$FF
		ld (de),a
		ld d,$DF
		ld (de),a
		ld c,a
		ld a,e
		sub $FD
		jr nc,cold_mapper__o1
		call fffc_apply
		jr cold_mapper__o2
cold_mapper__o1:		add a,a
		ld e,a
		ld a,c
		call map_bank
cold_mapper__o2:		pop de
		ret
cold_mapper__new:		cp $28
		jr nc,cold_mapper__n2
		; $20-$27: LD ($FFFC+k),BC or DE
		ld c,a
		ld hl,(fw_ret)
		inc hl
		inc hl
		ld (fw_ret),hl
		and 3
		add a,$FC
		bit 2,c
		ld hl,(G_C)		; L = game C, H = game B
		jr z,cold_mapper__pair
		ld hl,(G_E)		; L = game E, H = game D
		jr cold_mapper__pair
cold_mapper__n2:		cp $2C
		jr nc,cold_mapper__n3
		and 3			; $28-$2B
		add a,$FC
		ld hl,(fw_ret)
		jp cold_mapper__ldk
cold_mapper__n3:		cp $2F
		jr nc,cold_mapper__n4		; Z: $2F
		; $2C-$2E: Codemasters mapper, LD ($0000/$4000/$8000),A (site 32 00
		; nn): slot k gets bank A. No RAM copy, no fixed first 1K.
		ld hl,(fw_ret)
		inc hl
		ld (fw_ret),hl
		sub $2C
		add a,a
		ld e,a
		ld a,(game_a)
		jp map_bank_rom
cold_mapper__n4:		jr nz,cold_mapper__n5
		; $2F: RAM code patch table (HOOK kind 2): apply it, then go on at
		; its continuation address (the site replaced a JP to there)
		ld hl,(ramp_hook)
		ld e,(hl)
		inc hl
		ld d,(hl)
		inc hl
		ld (fw_ret),de
		ld b,(hl)		; entries: dw address; db 2 old, 2 new bytes
		inc hl
cold_mapper__rp:		ld e,(hl)
		inc hl
		ld d,(hl)
		inc hl
		ld a,(de)
		cp (hl)
		jr nz,cold_mapper__rpn
		inc hl
		inc de
		ld a,(de)
		cp (hl)
		dec de
		dec hl
		jr nz,cold_mapper__rpn
		inc hl
		inc hl
		ld a,(hl)
		ld (de),a
		inc de
		inc hl
		ld a,(hl)
		ld (de),a
		inc hl
		djnz cold_mapper__rp
		ret
cold_mapper__rpn:		inc hl
		inc hl
		inc hl
		inc hl
		djnz cold_mapper__rp
		ret
cold_mapper__n5:		sub $30			; $30-$3F
		ret c
		push af
		call game_hl
		pop af
		ld e,l
		jp cold_mapper__st

; C = value written to $FFFC. Bit 3 maps cart RAM (bank: bit 2) into slot 2
; in place of the $FFFF bank; clearing it maps the $FFFF bank back.
fffc_apply:
		ld a,c
		and 8
		jr z,fffc_apply__rom
		ld a,c
		and 4
		rrca			; 16K RAM bank * 2 pages
		add a,CARTRAM_PAGE
		ld (cur_mmu+4),a
		nextreg $54,a
		inc a
		ld (cur_mmu+5),a
		nextreg $55,a
		ret
fffc_apply__rom:		ld a,($FFFF)
		ld e,4
		jp map_bank_rom

; ----------------------------------------------------------------------
; Line interrupt schedule after a register 0 (IE1) or 10 write (called
; through fw2_call). The SMS reloads its line counter from register 10 on
; every line of the vertical blank, so a write there sets the next frame's
; first event. In the picture, a write does not move a scheduled event; but
; when none is scheduled and IE1 is now on (a frame ISR that set register 10
; and IE1 late, as handlers are slower than the SMS: Sonic's water line), the
; first event is register 10, or the next line if that line has passed.
; ----------------------------------------------------------------------
ev_recheck2:
		ld a,(hl_on)
		or a
		ret nz
		ld a,(vdp_regs+0)
		and $10
		ret z
		ld a,(vdp_regs+10)
		cp 192
		ret nc
		ld b,a
		call cur_line
		cp 192
		jr nc,ev_recheck2__set		; vertical blank: first event of the next frame
		ld c,a
		ld a,(ev_next)
		cp 192
		ret c			; an event is scheduled: the counter runs on
		ld a,c
		cp b
		jr c,ev_recheck2__set		; still ahead
		inc a			; passed: on the next line
		cp 192
		ret nc
		ld b,a
ev_recheck2__set:		ld a,b
		jp ev_program


; ----------------------------------------------------------------------
; Per-line H scroll from an overlay hook (rastercode). A game that writes
; register 8 from a line interrupt on (nearly) every line cannot have its
; interrupts delivered on the Next: one costs more than a line. Its overlay
; brings a small routine that works out, from the game's RAM and registers,
; the register 8 value of every line, as the game's line interrupt handler
; would set it. Called once a frame: rast_hook with HL = hl_tab (192 bytes)
; and IX = vdp_regs, game RAM at $C000; carry set = the table is valid this
; frame. While it is (hl_on), the game gets no line interrupts, register 8
; writes go nowhere but vdp_regs, and the copper list is rebuilt from the
; table every frame (cop_raster).
; ----------------------------------------------------------------------
rast_frame:
		ld hl,(rast_hook)
		ld a,h
		or l
		ret z
		ld (rast_frame__c+1),hl
		ld hl,hl_tab
		ld ix,vdp_regs
		or a
rast_frame__c:		call 0
		ld a,0
		adc a,a			; 1 when the table is valid
		ld hl,hl_on
		cp (hl)
		ld (hl),a
		jr z,rast_frame__same
		or a
		jr nz,cop_raster
		; back to the normal list: rebuilt in full, X from register 8
		ld a,$FF
		ld (cop_mode),a
		ld (cop_sw),a
		ld a,1
		ld (cop_dirty),a
		ld a,(vdp_regs+8)
		ld e,a
		jp hscroll_set
rast_frame__same:		or a
		ret z
; The copper list from hl_tab: head MOVE $31 V, $6E M0, X of line 0; for
; each line y, when its K = -H > 64 the map switch pair (WAIT y,c; MOVE
; $6E,A8), then at the end of the line (WAIT y,40) M0 back and X for line
; y+1 where it changes. At most RX_MAX instructions; past that the list
; stops (later lines keep the last X). The copper keeps running while the
; list is rewritten: it restarts at the top of every frame, and the rewrite
; stays ahead of it.
RX_MAX		equ 1014
cop_raster:
		ld a,$FF
		ld (cop_mode),a		; the normal list is gone
		ld a,(vdp_regs+0)
		and $40
		jr z,cop_raster__nl
		ld hl,hl_tab		; register 0 bit 6: lines 0-15 at H = 0
		ld b,16
cop_raster__lk:		ld (hl),0
		inc hl
		djnz cop_raster__lk
cop_raster__nl:		nextreg $61,0
		nextreg $62,%11000000	; write index 0, copper running
		ld a,(vdp_regs+9)
		cp 224
		jr c,cop_raster__v
		sub 224
cop_raster__v:		add a,224
		ld c,a
		nextreg $60,$31
		ld a,c
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		ld a,(hl_tab)
		call h2x
		nextreg $60,$2F
		ld a,d
		nextreg $60,a
		nextreg $60,$30
		ld a,e
		nextreg $60,a
		ld (rx_cur),de
		ld a,b
		ld (rx_sw),a		; switch column of line 0
		ld iy,6
		ld ix,hl_tab+1		; H of line y+1
		ld c,0			; line y
cop_raster__line:		push iy
		pop hl
		ld de,RX_MAX
		or a
		sbc hl,de
		jp nc,cop_raster__end
		ld a,(rx_sw)
		or a
		jr z,cop_raster__ns
		add a,a
		or $80
		nextreg $60,a		; WAIT y,c
		ld a,c
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_A8
		inc iy
		inc iy
cop_raster__ns:		ld a,c
		cp 191
		ld de,(rx_cur)
		ld b,0
		jr z,cop_raster__nx
		ld a,(ix+0)
		call h2x		; DE = X, B = switch column of line y+1
cop_raster__nx:		ld a,b
		ld (rx_nsw),a		; switch column of line y+1 (the game's AF' must
					; not be touched: vbl work runs inside game code)
		ld hl,(rx_cur)
		or a
		sbc hl,de
		ld a,h
		or l
		ld b,a			; B != 0: X changes
		ld a,(rx_sw)
		or b
		jr z,cop_raster__next
		nextreg $60,$80 + (END_H << 1)	; WAIT y,40
		ld a,c
		nextreg $60,a
		inc iy
		ld a,(rx_sw)
		or a
		jr z,cop_raster__nm
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		inc iy
cop_raster__nm:		ld a,b
		or a
		jr z,cop_raster__next
		ld hl,(rx_cur)
		ld a,h
		cp d
		jr z,cop_raster__lo
		nextreg $60,$2F
		ld a,d
		nextreg $60,a
		inc iy
cop_raster__lo:		ld a,l
		cp e
		jr z,cop_raster__st
		nextreg $60,$30
		ld a,e
		nextreg $60,a
		inc iy
cop_raster__st:		ld (rx_cur),de
cop_raster__next:		ld a,(rx_nsw)
		ld (rx_sw),a
		inc ix
		inc c
		ld a,c
		cp 192
		jp nz,cop_raster__line
cop_raster__end:		nextreg $60,$FF		; HALT
		nextreg $60,$FF
		ret

; A = register 8 value H -> DE = tilemap X offset (K - 34 mod 320, K = -H),
; B = copper column of the M0 -> A8 switch, 0 = none (as hscroll_set, fw.asm)
h2x:		neg
		ld b,a			; K
		cp 34
		jr c,h2x__lo
		sub 34			; K >= 34: X = K - 34
		ld e,a
		ld d,0
		jr h2x__sw
h2x__lo:		add a,30		; K < 34: X = K + 286
		ld e,a
		ld d,1
h2x__sw:		ld a,b
		cp 65
		ld b,0
		ret c
		ld b,a
		ld a,32			; (288 - K) / 8; 288 - K < 256 here
		sub b
		rrca
		rrca
		rrca
		and $1F
		ld b,a
		ret

rx_cur:		dw 0
rx_sw:		db 0
rx_nsw:		db 0
hl_tab:		ds 192


; ----------------------------------------------------------------------
; 224-line mode (register 0 bit 1 with register 1 bit 4; SMS2 VDP). The
; picture is 224 lines: SMS line 0 is shown 16 lines above the 192-line
; area, line 223 16 lines below it; the name table has 32 rows at
; (register 2 bits 3-2) << 12 + $700 and V scroll wraps at 256 lines.
; ----------------------------------------------------------------------
mode_switch:
		ld a,(vdp_regs+0)
		and 2
		jr z,mode_switch__set
		ld a,(vdp_regs+1)
		and $10
		jr z,mode_switch__set
		ld a,1
mode_switch__set:		ld hl,m224
		cp (hl)
		ret z
		ld (hl),a
		or a
		ld a,192
		jr z,mode_switch__p
		ld a,208
mode_switch__p:		ld (pic_end),a
		ld a,$FF
		ld (cop_mode),a
		ld (cop_sw),a
		ld (cop_v),a
		ld a,1
		ld (cop_dirty),a
		ld (sat_dirty),a
		ld (pri_full),a
		call l2_vis
		call clip_update
		; fall into nt_base_set

; Register 2: name table base (and the VRAM page roles, and the maps)
nt_base_set:
		ld a,(vdp_regs+2)
		ld e,a
		ld a,(m224)
		or a
		ld a,e
		jr nz,nt_base_set__l
		and $0E			; bits 3-1 -> address bits 13-11
		add a,a
		add a,a
		jr nt_base_set__s
nt_base_set__l:		and $0C			; bits 3-2 -> 13-12, + $700
		add a,a
		add a,a
		or $07
nt_base_set__s:		ld (nt_base+1),a
		xor a
		ld (nt_base),a
		inc a
		ld (nt_dirty),a
		; fall into region_update

; region_tab from nt_base and sat_hi
region_update:
		ld hl,region_tab
		ld b,64
region_update__clr:		ld (hl),0
		inc l
		djnz region_update__clr
		ld a,(nt_base+1)
		ld l,a
		ld a,(m224)
		or a
		ld b,8			; 224 lines: 32 rows, all name table
		jr nz,region_update__nt
		ld b,6			; rows 0-23: $600 bytes
region_update__nt:		ld (hl),1
		inc l
		djnz region_update__nt
		ld a,(m224)
		or a
		jr nz,region_update__sat
		ld (hl),3		; rows 24-27: games keep tiles there too
region_update__sat:		ld a,(sat_hi)
		ld l,a
		ld (hl),2
		ret

; Tilemap and sprite clip windows; register 0 bit 5 hides SMS column 0;
; lines 32-223 of the 256-line display, 16-239 in 224-line mode.
clip_update:
		ld a,(vdp_regs+0)
		and $20
		jr z,clip_update__c
		ld a,4
clip_update__c:		ld e,a
		ld a,(m224)
		or a
		ld bc,32*256+223
		jr z,clip_update__y
		ld bc,16*256+239
clip_update__y:		nextreg $1C,%00001011	; reset tilemap, sprite and Layer 2 clip indexes
		ld a,e			; Layer 2 (priority tiles): pixels PIC_X (+ 8) to 255,
		add a,a			; lines 0-191 (off in 224-line mode)
		add a,PIC_X
		nextreg $18,a
		nextreg $18,255
		nextreg $18,0
		nextreg $18,191
		ld a,16+PIC_X/2
		add a,e
		nextreg $1B,a
		nextreg $1B,143+PIC_X/2
		ld a,b
		nextreg $1B,a
		ld a,c
		nextreg $1B,a
		ld a,16+1
		add a,e
		nextreg $19,a		; over-border units of 2 pixels
		nextreg $19,144
		ld a,b
		nextreg $19,a
		ld a,c
		nextreg $19,a
		ret

; The copper list in 224-line mode: one X, one Y (V - 16; the 32-row map
; wraps at 256 by itself) and, when K = -H > 64, the map switch pair on
; each of the 224 lines (Next lines 0-207, then 296-311 for the 16 lines
; above line 0). Per-line H scroll and the lock bits are not done here.
cop_224:
		xor a
		ld (cop_dirty),a
		ld a,$FF
		ld (cop_mode),a
		ld (cop_sw),a
		nextreg $61,0
		nextreg $62,%11000000
		ld a,(vdp_regs+9)
		add a,240
		ld c,a
		nextreg $60,$2F
		ld a,(h_x+1)
		nextreg $60,a
		nextreg $2F,a
		nextreg $60,$30
		ld a,(h_x)
		nextreg $60,a
		nextreg $30,a
		nextreg $60,$31
		ld a,c
		nextreg $60,a
		nextreg $31,a
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		ld a,(h_sw)
		or a
		jr z,cop_224__end
		ld d,a
		ld bc,0
cop_224__l1:		call cop_224__sw
		inc bc
		ld a,c
		cp 208
		jr nz,cop_224__l1
		ld bc,296
cop_224__l2:		call cop_224__sw
		inc bc
		ld a,c
		cp 255&(312)
		jr nz,cop_224__l2
cop_224__end:		nextreg $60,$FF		; HALT
		nextreg $60,$FF
		ret
cop_224__sw:		ld a,d			; BC = line, D = switch column
		add a,a
		or $80
		or b
		nextreg $60,a		; WAIT line,column
		ld a,c
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_A8
		ld a,$80 + (END_H << 1)
		or b
		nextreg $60,a		; WAIT line,40
		ld a,c
		nextreg $60,a
		nextreg $60,$6E
		nextreg $60,NR6E_M0
		ret

; ----------------------------------------------------------------------
; Overlay switches (fw_flags, from the overlay header): set the hooks in
; fw.asm on or off and the state they use. Called by fw2_start, so a game
; loaded after another one starts clean.
; ----------------------------------------------------------------------
fw2_switches:
		ld a,(fw_flags)
		and 1
		ld hl,nt_put__hk
		ld de,pri_mark1
		call hook_set
		ld a,(fw_flags)
		and 1
		ld hl,nt_range__hk
		ld de,pri_markr
		call hook_set
		ld a,(fw_flags)
		and 2
		ld hl,fw_line_irq__hk1
		ld de,pal_vbl
		call hook_set
		ld a,(fw_flags)
		and 2
		ld hl,fw_line_irq__hk2
		ld de,pal_pic
		call hook_set
		ld a,(fw_flags)
		and 3
		ld a,$C9		; RET: no extra palette writes
		jr z,fw2_switches__c
		xor a			; NOP: cram_x writes them
fw2_switches__c:		ld (cram_hk),a
		; Layer 2 (priority tiles): 256x192 from L2_BANK, above the sprites;
		; its transparent colour is one the SMS palette never makes
		ld a,(fw_flags)
		rra
		ld a,L2_TRANS
		ld b,4			; layer order L S U
		jr c,fw2_switches__p
		ld a,$E3		; the reset value
		ld b,0
fw2_switches__p:		nextreg $14,a
		ld a,b
		ld (lay15),a
		nextreg $12,L2_BANK
		nextreg $70,0
		nextreg $16,254
		nextreg $17,0
		ld bc,$123B		; hidden until the display is on (l2_vis)
		xor a
		out (c),a
		ld (pri_redo),a
		ld (pri_ys),a
		ld (isr_sp),a		; no frame handler running, none held
		ld (isr_sp+1),a
		ld (irq_pend),a
		ld (line_held),a
		ld (dis_pend),a
		ld (disp_on),a
		ld (shadow_i),a
		ld (pal_vm),a
		ld (pal_vm+1),a
		ld (pal_vm+2),a
		ld (pal_vm+3),a
		ld hl,pri_lf		; pri_lf, pri_tiles, pri_chg
		ld de,pri_lf+1
		ld bc,192+64+64-1
		ld (hl),a
		ldir
		ld hl,cram_top
		ld b,32
fw2_switches__zt:		ld (hl),a
		inc hl
		djnz fw2_switches__zt
		inc a
		ld (pri_full),a
		ld (pal_ph),a
		ld a,254
		ld (pri_x),a
		ld a,%00000010
		ld (pal43),a
		ld (tm_ctl),a
		ret

; The tilemap always treats one 4-bit pixel value as transparent (NextReg
; $4C), and shows the fallback colour (NextReg $4A) there. The framework
; picks the value v for which CRAM v (background palette) equals CRAM 16+v
; (sprite palette), so a pixel of value v shows the right colour in tiles
; of either palette; if there is none, v = 0 and tiles that use the sprite
; palette show CRAM 0 instead of CRAM 16 for that value. The fallback is
; CRAM v while the display is on, the backdrop (register 7) when it is off.
fallback2:
		ld hl,cram
		ld b,16
fallback2__f:		ld a,l
		add a,16
		ld e,a
		ld d,h
		ld a,(de)
		cp (hl)
		jr z,fallback2__got
		inc l
		djnz fallback2__f
		; none: the first value no sprite-palette tile on screen uses
		; (tr_free, from fw3 pal_scan), else 0
		ld de,(tr_free)
		ld b,0
fallback2__t:		srl d
		rr e
		jr c,fallback2__tg
		inc b
		ld a,b
		cp 16
		jr nz,fallback2__t
		; sprite-palette tiles use every value: a value v no background
		; tile uses (bg_free, fw3 pal_rows_step) is right with CRAM 16+v
		ld de,(bg_free)
		ld b,0
fallback2__u:		srl d
		rr e
		jr c,fallback2__ug
		inc b
		ld a,b
		cp 16
		jr nz,fallback2__u
		; none either: pixel value 0 shows CRAM 0 or CRAM 16, the
		; palette whose tiles show more of it in the rows still to come
		; (pal_rows); with the beam below the picture, in the whole
		; picture
		call cur_line
		cp 192
		jr c,fallback2__cl
		xor a
fallback2__cl:		rrca
		rrca
		rrca
		and $1F
		ld hl,pal_rows
		add hl,a
		ld a,(hl)
		ld hl,cram
		or a
		jp m,fallback2__got
		jr z,fallback2__got
		nextreg $4C,0
		ld hl,cram+16
		jr fallback2__disp
fallback2__ug:		ld a,b
		nextreg $4C,a
		add a,255&((cram+16))
		ld l,a
		ld h,255&((cram)>>8)
		jr fallback2__disp
fallback2__tg:		ld a,b
		add a,255&(cram)
		ld l,a
		ld h,255&((cram)>>8)
fallback2__got:		ld a,l
		sub 255&(cram)
		nextreg $4C,a
fallback2__disp:		ld a,(disp_on)
		or a
		jr nz,fallback2__on
		ld a,(vdp_regs+7)
		and $0F
		or $10
		ld e,a
		ld d,0
		ld hl,cram
		add hl,de
fallback2__on:		ld a,(pal43)		; toppal shows the second palettes: their colour
		and 8
		jr z,fallback2__on1
		ld de,cram_top-cram
		add hl,de
fallback2__on1:		ld a,(hl)
		add a,255&(pal_hi_table)
		ld l,a
		ld h,255&((pal_hi_table)>>8)
		ld a,(hl)
		nextreg $4A,a
; The SMS shows the backdrop colour (CRAM 16 + register 7) in the masked
; column 0. The tilemap is clipped off there and the ULA, clipped to that
; column, shows through; every entry of the second ULA palette (the active
; one while a game runs) holds the backdrop colour, so the ULA's screen
; bytes do not matter.
bd_update:
		ld a,(vdp_regs+7)
		and $0F
		add a,255&((cram+16))
		ld l,a
		ld h,255&((cram)>>8)
		ld a,(hl)
		ld hl,bd_cur
		cp (hl)
		ret z
		ld (hl),a
		ld c,a
		ld a,(pal43)
		or %01000000		; write the second ULA palette
		nextreg $43,a
		nextreg $40,0
		ld b,32
bd_update__w:		push bc
		call pal_out
		pop bc
		djnz bd_update__w
		ret


; Line-0 palette (toppal), see pal_vbl in fw.asm: through fw2_call from
; fw_line_irq at the frame event (pal_vbl2) and at a line event (pal_pic2)
pal_vbl2:	call dis_apply		; off over a whole phase: it is off
		ld a,1
		ld (pal_ph),a
		ld hl,0
		ld (pal_vm),hl
		ld (pal_vm+2),hl
		ld a,%00001100
		jr pal_show
pal_pic2:	ld a,(ev_next)		; a line event (not the frame event)
		cp 192
		ret nc
		ld a,(pal_ph)
		or a
		ret z
		xor a
		ld (pal_ph),a
		call dis_apply
		xor a
; A = display bits 3 and 2 of NextReg $43 (second sprite, Layer 2 palettes)
pal_show:	or %00000010
		ld (pal43),a
		nextreg $43,a
		and 8
		add a,a			; NextReg $6B bit 4: second tilemap palette
		ld hl,tm_ctl
		or (hl)
		nextreg $6B,a
		push de
		call fallback2		; the fallback colour from the palette shown
		pop de
		ret

; A display-off write held in the vertical blank phase (vdp_reg_w .r1)
dis_apply:	ld a,(dis_pend)
		or a
		ret z
		xor a
		ld (dis_pend),a
		call r1_hw
		call fallback2
		jp l2_vis

; ----------------------------------------------------------------------
; Leave the game (fw_quit in fw.asm, which maps slots 0 and 1 afterwards):
; put NextZXOS's pages and registers back.
; ----------------------------------------------------------------------
fw_quit2:
		nextreg $62,0		; copper off
		nextreg $6B,0		; tilemap off
		nextreg $1C,%00000100	; ULA clip back to the whole screen
		nextreg $1A,0
		nextreg $1A,255
		nextreg $1A,0
		nextreg $1A,191
		nextreg $15,0		; sprites off
		ld bc,$123B		; Layer 2 off
		xor a
		out (c),a
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
		ld hl,nr_saved
fw_quit2__r:		ld a,(hl)
		inc hl
		cp $FF
		jr z,fw_quit2__rd
		call nr_write_sel
		ld a,(hl)
		inc hl
		call nr_write_val
		jr fw_quit2__r
fw_quit2__rd:		nextreg $52,10
		nextreg $53,11
		nextreg $54,4
		nextreg $55,5
		nextreg $56,0
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


; Layer 2 shown while the display is on, with priority tiles, not in
; 224-line mode (the 256x192 Layer 2 does not reach those lines)
l2_vis:		ld a,(fw_flags)
		rra
		ld a,0
		jr nc,l2_vis__o
		ld a,(m224)
		or a
		ld a,0
		jr nz,l2_vis__o
		ld a,(disp_on)
		or a
		jr z,l2_vis__o
		ld a,2
l2_vis__o:		ld bc,$123B
		out (c),a
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

; HL = hook (3 bytes), DE = routine: Z clear = CALL routine, Z set = NOPs
hook_set:	jr z,hook_set__off
		ld (hl),$CD
		inc hl
		ld (hl),e
		inc hl
		ld (hl),d
		ret
hook_set__off:		ld (hl),0
		inc hl
		ld (hl),0
		inc hl
		ld (hl),0
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

; ----------------------------------------------------------------------
; CRAM write E = index, C = colour, after cram_set (fw.asm) wrote the first
; tilemap and sprite palettes; through fw2_call from a handler.
; Priority tiles: the first Layer 2 palette (entries 0 and 16 stay
; transparent). toppal (see pal_vbl in fw.asm): in the vertical blank
; phase, or for an entry that phase did not write (a change the frame
; handler does not put back), the second palettes and cram_top too.
; ----------------------------------------------------------------------
cram_x:
		ld a,(fw_flags)
		rra
		jr nc,cram_x__np
		ld a,e
		and $0F
		jr z,cram_x__np
		ld a,(pal43)
		or %00010000		; first Layer 2 palette
		nextreg $43,a
		ld a,e
		nextreg $40,a
		call pal_out
cram_x__np:		ld a,(fw_flags)
		and 2
		ret z
		ld a,e
		call vm_bit		; HL = pal_vm byte, A = the entry's bit
		ld b,a
		ld a,(pal_ph)
		or a
		jr z,cram_x__pic
		ld a,b			; vertical blank phase
		or (hl)
		ld (hl),a
		jr cram_x__top
cram_x__pic:		ld a,b			; in the picture: the vertical blank puts it back
		and (hl)
		ret nz
cram_x__top:		ld hl,cram_top
		ld a,e
		add hl,a
		ld (hl),c
		ld a,(pal43)
		or %01110000		; second tilemap palette
		nextreg $43,a
		ld a,e
		nextreg $40,a
		call pal_out
		ld a,e
		cp 16
		jr c,cram_x__l2
		ld a,(pal43)
		or %01100000		; second sprite palette
		nextreg $43,a
		ld a,e
		sub 16
		nextreg $40,a
		call pal_out
cram_x__l2:		ld a,(fw_flags)
		rra
		ret nc
		ld a,e
		and $0F
		ret z
		ld a,(pal43)
		or %01010000		; second Layer 2 palette
		nextreg $43,a
		ld a,e
		nextreg $40,a
		jp pal_out

; A = CRAM index 0-31 -> HL = its byte of pal_vm, A = its bit
vm_bit:		ld b,a
		rrca
		rrca
		rrca
		and 3
		ld hl,pal_vm
		add hl,a
		ld a,b
		and 7
		push hl
		ld hl,pri_bit
		add hl,a
		ld a,(hl)
		pop hl
		ret

pri_bit:	db 1,2,4,8,16,32,64,128

; ----------------------------------------------------------------------
; Priority tiles (overlay flag 1). SMS name table entries with bit 12 (the
; high byte's bit 4) are drawn a second time into Layer 2 (256x192, 8 bits
; a pixel, pages L2_PAGE to L2_PAGE+5), which lies above the sprites
; (NextReg $15 layer order L S U). A pixel byte is the palette bit * 16 +
; the pixel value: Layer 2 palette entry = CRAM entry, and entries 0 and 16
; are transparent, so sprites show through pixel value 0 as on the SMS.
; Across, Layer 2 holds the SMS map as it is (both are 256 pixels wide and
; wrap there); its X scroll (pri_x, NextReg $16) follows H scroll in
; hscroll_set and the copper list. Down, it is a ring of the 192 lines on
; screen: screen line y is Layer 2 line (pri_ys + y) mod 192 and shows map
; line (V + y) mod 224. When V moves by d, pri_ys moves by d and only the
; lines that come into view are drawn (pri_line). Name table writes mark
; cells (pri_mark1, pri_markr in fw.asm; marks in MAP_PAGE, here mapped at
; $0000); a changed tile that a priority cell shows marks pri_chg. Runs in
; the vblank work after tile_flush, with the shadow at $4000 and the Next
; tile definitions at $8000; Layer 2 pages go to slot 6.
; Not done: 224-line mode (Layer 2 off), the locked right columns with V
; scroll (they show the V-scrolled cells), per-line H scroll from a
; rastercode hook.
; ----------------------------------------------------------------------
pri_frame:
		ld a,(fw_flags)
		rra
		ret nc
		ld a,(m224)
		or a
		ret nz
		nextreg $50,MAP_PAGE	; the marks: $1BE0 + row, $1C00 + cell
		ld a,$FF
		ld (pri_pg),a
		ld a,(vdp_regs+9)
		cp 224
		jr c,pri_frame__v
		sub 224
pri_frame__v:		ld (pri_nv),a
		ld a,(pri_full)
		or a
		jp nz,pri_rebuild
		; V moved by d (mod 224): the ring moves with it
		ld a,(pri_nv)
		ld hl,pri_v
		sub (hl)
		jr z,pri_frame__cells
		jr nc,pri_frame__d0
		add a,224
pri_frame__d0:		ld b,a			; d, 1-223
		ld a,(pri_nv)
		ld (hl),a
		ld a,b
		cp 113
		jr nc,pri_frame__up
		ld hl,pri_ys		; d = 1-112: lines 192-d to 191 come into view
		add a,(hl)
		jr c,pri_frame__y1s
		cp 192
		jr c,pri_frame__y1
pri_frame__y1s:		sub 192
pri_frame__y1:		ld (hl),a
		ld a,192
		sub b
		ld c,a
pri_frame__dn:		push bc
		call pri_line
		pop bc
		inc c
		ld a,c
		cp 192
		jr nz,pri_frame__dn
		jr pri_frame__cells
pri_frame__up:		ld a,224		; d = -(224 - A): lines 0 to 223-A come into view
		sub b
		ld b,a
		ld hl,pri_ys
		ld a,(hl)
		sub b
		jr nc,pri_frame__y2
		add a,192
pri_frame__y2:		ld (hl),a
		ld c,0
pri_frame__upl:		push bc
		call pri_line
		pop bc
		inc c
		ld a,c
		cp b
		jr nz,pri_frame__upl
pri_frame__cells:		ld a,(pri_redo)		; tiles of priority cells changed
		or a
		ld a,0
		call nz,pri_redraw
		ld b,0			; marked cells, row by row
pri_frame__r:		ld h,$1B
		ld a,b
		add a,$E0
		ld l,a
		ld a,(hl)
		or a
		jr z,pri_frame__rn
		ld (hl),0
		push bc
		call pri_rowcells
		pop bc
pri_frame__rn:		inc b
		ld a,b
		cp 28
		jr nz,pri_frame__r
pri_done:	ld a,(pri_ys)
		nextreg $17,a
		nextreg $50,FW3_PAGE
		ret

; The whole of Layer 2 from the name table (start, name table base, mode)
pri_rebuild:
		xor a
		ld (pri_full),a
		ld (pri_ys),a
		ld a,(pri_nv)
		ld (pri_v),a
		ld c,0			; clear the lines that hold pixels
pri_rebuild__l:		ld hl,pri_lf
		ld a,c
		add hl,a
		ld a,(hl)
		or a
		jr z,pri_rebuild__n
		ld (hl),0
		ld a,c
		ld (pr_l),a
		push bc
		call pri_clr
		pop bc
pri_rebuild__n:		inc c
		ld a,c
		cp 192
		jr nz,pri_rebuild__l
		ld hl,$1BC0		; no marks
		ld de,$1BC1
		ld bc,$0440-1
		ld (hl),0
		ldir
		ld hl,pri_tiles
		ld b,64
pri_rebuild__t:		ld (hl),0
		inc hl
		djnz pri_rebuild__t
		xor a			; which rows have priority cells
		ld (pr_r),a
		ld (pr_c),a
pri_rebuild__rr:		call pri_ent
		ld b,32
pri_rebuild__rc:		bit 4,(hl)
		jr nz,pri_rebuild__rp
		inc hl
		inc hl
		djnz pri_rebuild__rc
		jr pri_rebuild__rn
pri_rebuild__rp:		ld a,(pr_r)
		add a,$C0
		ld l,a
		ld h,$1B
		ld (hl),1
pri_rebuild__rn:		ld hl,pr_r
		inc (hl)
		ld a,(hl)
		cp 28
		jr nz,pri_rebuild__rr
		ld a,1
		call pri_redraw
		jp pri_done

; A = 1: every priority cell of the rows on screen; A = 0: those whose tile
; changed (pri_chg). Then pri_chg is cleared.
pri_redraw:
		ld (pr_all),a
		xor a
		ld (pri_redo),a
		ld (pr_r),a
pri_redraw__r:		ld a,(pr_r)		; row on screen: y0 = 8r - V mod 224 < 192 or > 216
		add a,a
		add a,a
		add a,a
		ld hl,pri_v
		sub (hl)
		jr nc,pri_redraw__y
		add a,224
pri_redraw__y:		cp 192
		jr c,pri_redraw__vis
		cp 217
		jr c,pri_redraw__nr
pri_redraw__vis:		xor a
		ld (pr_c),a
		call pri_ent		; HL = the row's first entry (high byte)
		ld b,32
pri_redraw__c:		bit 4,(hl)
		jr z,pri_redraw__n
		push hl
		push bc
		ld a,32
		sub b
		ld (pr_c),a
		ld a,(pr_all)
		or a
		jr nz,pri_redraw__d
		call pri_ent
		call pri_tbit		; HL = its pri_chg byte, A = bit
		and (hl)
		jr z,pri_redraw__s
pri_redraw__d:		call pri_cell
pri_redraw__s:		pop bc
		pop hl
pri_redraw__n:		inc hl
		inc hl
		djnz pri_redraw__c
pri_redraw__nr:		ld a,(pr_r)
		inc a
		ld (pr_r),a
		cp 28
		jr nz,pri_redraw__r
		ld hl,pri_chg
		ld b,64
pri_redraw__z:		ld (hl),0
		inc hl
		djnz pri_redraw__z
		ret

; Row B: each marked cell (bit 0 of its mark) again
pri_rowcells:
		ld a,b
		ld (pr_r),a
		ld l,b
		ld h,0
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		ld de,$1C00
		add hl,de
		ld c,0
pri_rowcells__c:		bit 0,(hl)
		jr z,pri_rowcells__n
		res 0,(hl)
		push hl
		push bc
		ld a,c
		ld (pr_c),a
		call pri_cell
		pop bc
		pop hl
pri_rowcells__n:		inc hl
		inc c
		ld a,c
		cp 32
		jr nz,pri_rowcells__c
		ret

; Cell (pr_r, pr_c): its lines on screen into Layer 2: its pixels when it
; has the priority bit, else zeros where Layer 2 may hold pixels; bit 1 of
; its mark says Layer 2 holds it
pri_cell:
		call pri_ent
		call pri_mk
		ld a,(pr_th)
		and $10
		jr nz,pri_cell__p
		bit 1,(hl)
		ret z			; Layer 2 holds nothing of it
		res 1,(hl)
		jr pri_cell__lines
pri_cell__p:		set 1,(hl)
		call pri_tile
pri_cell__lines:		ld a,(pr_r)
		add a,a
		add a,a
		add a,a
		ld e,a			; map line of the cell's top
		ld d,0			; line in the cell
pri_cell__k:		ld a,e
		add a,d
		ld hl,pri_v
		sub (hl)
		jr nc,pri_cell__y
		add a,224
pri_cell__y:		cp 192			; screen line y
		jr nc,pri_cell__nx
		ld hl,pri_ys
		add a,(hl)
		jr c,pri_cell__w
		cp 192
		jr c,pri_cell__l
pri_cell__w:		sub 192
pri_cell__l:		ld (pr_l),a
		ld a,d
		ld (pr_k),a
		push de
		ld hl,pri_lf
		ld a,(pr_l)
		add hl,a
		ld a,(pr_th)
		and $10
		jr z,pri_cell__clr
		ld (hl),1
		call pri_put
		jr pri_cell__nd
pri_cell__clr:		ld a,(hl)
		or a
		call nz,pri_put		; no priority bit: zeros
pri_cell__nd:		pop de
pri_cell__nx:		inc d
		ld a,d
		cp 8
		jr nz,pri_cell__k
		ret

; Screen line C comes into view: Layer 2 line (pri_ys + C) mod 192 gets
; map line (V + C) mod 224 (cleared first if it holds pixels)
pri_line:
		ld a,(pri_ys)
		add a,c
		jr c,pri_line__w
		cp 192
		jr c,pri_line__l
pri_line__w:		sub 192
pri_line__l:		ld (pr_l),a
		ld hl,pri_lf
		add hl,a
		ld a,(hl)
		or a
		jr z,pri_line__cl
		ld (hl),0
		push bc
		call pri_clr
		pop bc
pri_line__cl:		ld a,(pri_v)
		add a,c
		jr c,pri_line__w2
		cp 224
		jr c,pri_line__m
pri_line__w2:		sub 224
pri_line__m:		ld b,a
		and 7
		ld (pr_k),a
		ld a,b
		rrca
		rrca
		rrca
		and $1F
		ld (pr_r),a
		add a,$C0		; the row may have priority cells?
		ld l,a
		ld h,$1B
		ld a,(hl)
		or a
		ret z
		xor a
		ld (pr_c),a
		call pri_ent		; HL = high byte of the row's first entry
		ld b,32
pri_line__c:		bit 4,(hl)
		jr z,pri_line__n
		push hl
		push bc
		ld a,(hl)
		ld (pr_th),a
		dec hl
		ld a,(hl)
		ld (pr_tl),a
		ld a,32
		sub b
		ld (pr_c),a
		call pri_put
		call pri_tile
		call pri_mk
		set 1,(hl)
		ld hl,pri_lf
		ld a,(pr_l)
		add hl,a
		ld (hl),1
		pop bc
		pop hl
pri_line__n:		inc hl
		inc hl
		djnz pri_line__c
		ret

; Entry (pr_r, pr_c) from the shadow into pr_tl, pr_th; HL = its high byte
pri_ent:	ld a,(pr_r)
		ld l,a
		ld h,0
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		ld a,(pr_c)
		add a,a
		add hl,a
		ld de,(nt_base)
		add hl,de
		ld a,h
		add a,$40		; the shadow is at $4000 here
		ld h,a
		ld a,(hl)
		ld (pr_tl),a
		inc hl
		ld a,(hl)
		ld (pr_th),a
		ret

; HL = the mark of cell (pr_r, pr_c)
pri_mk:		ld a,(pr_r)
		ld l,a
		ld h,0
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		ld a,(pr_c)
		add hl,a
		ld a,h
		add a,$1C
		ld h,a
		ret

; The tile of pr_tl/pr_th into pri_tiles
pri_tile:	ld hl,pri_tiles
		call pri_tb
		or (hl)
		ld (hl),a
		ret
; HL = pri_chg byte of the tile, A = its bit
pri_tbit:	ld hl,pri_chg
; HL = table of 64 (a bit per tile, a byte per VRAM page) -> HL += tile >> 3,
; A = 1 << (tile & 7)
pri_tb:		ld a,(pr_tl)
		rrca
		rrca
		rrca
		and $1F
		ld e,a
		ld a,(pr_th)
		and 1
		rrca
		rrca
		rrca
		or e
		add hl,a
		ld a,(pr_tl)
		and 7
		ld de,pri_bit
		add de,a
		ld a,(de)
		ret

; Slot 6 = the Layer 2 page of line pr_l; HL = the line's start there
pri_page:	ld a,(pr_l)
		rlca
		rlca
		rlca
		and 7
		add a,L2_PAGE
		ld hl,pri_pg
		cp (hl)
		jr z,pri_page__s
		ld (hl),a
		nextreg $56,a
pri_page__s:		ld a,(pr_l)
		and $1F
		or $C0
		ld h,a
		ld l,0
		ret

; Layer 2 line pr_l: all zeros (interrupts are off in the vblank work)
pri_clr:	call pri_page
		inc h
		ld (pri_sp),sp
		ld sp,hl
		ld hl,0
		ld b,16
pri_clr__z:		push hl
		push hl
		push hl
		push hl
		push hl
		push hl
		push hl
		push hl
		djnz pri_clr__z
		ld sp,(pri_sp)
		ret

; Layer 2 line pr_l, pixels 8 pr_c to 8 pr_c + 7: line pr_k of the cell's
; tile (pr_tl, pr_th: flips, palette), or zeros without the priority bit
pri_put:	call pri_page
		ld a,(pr_c)
		add a,a
		add a,a
		add a,a
		ld l,a
		ex de,hl		; DE = destination
		ld a,(pr_th)
		ld b,a
		and $10
		jp z,pri_put__clr
		ld a,b
		and 1
		ld h,a
		ld a,(pr_tl)
		ld l,a
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl		; tile * 32
		ld a,(pr_k)
		bit 2,b			; V flip
		jr z,pri_put__nv
		xor 7
pri_put__nv:		add a,a
		add a,a
		add hl,a
		ld a,h
		add a,$80		; Next tile definitions at $8000
		ld h,a
		ld a,b
		and 8
		add a,a
		ld c,a			; $10: the sprite palette (entries 16-31)
		bit 1,b			; H flip
		jr nz,pri_put__f
		rept 4
		ld a,(hl)
		swapnib
		and $0F
		or c
		ld (de),a
		inc e
		ld a,(hl)
		and $0F
		or c
		ld (de),a
		inc e
		inc hl
		endr
		ret
pri_put__f:		inc hl
		inc hl
		inc hl
		rept 4
		ld a,(hl)
		and $0F
		or c
		ld (de),a
		inc e
		ld a,(hl)
		swapnib
		and $0F
		or c
		ld (de),a
		inc e
		dec hl
		endr
		ret
pri_put__clr:		xor a
		rept 8
		ld (de),a
		inc e
		endr
		ret

pri_full:	db 1			; rebuild Layer 2 from the name table
pri_redo:	db 0			; pri_chg has bits
pri_v:		db 0			; V that the ring holds
pri_nv:		db 0
pri_ys:		db 0			; Layer 2 Y scroll
pri_pg:		db $FF			; Layer 2 page in slot 6 now
pr_all:		db 0
pr_r:		db 0			; cell row, column
pr_c:		db 0
pr_k:		db 0			; line in the cell
pr_l:		db 0			; Layer 2 line
pr_tl:		db 0			; name table entry
pr_th:		db 0
pri_sp:		dw 0
pri_lf:		ds 192			; per Layer 2 line: it may hold pixels
pri_tiles:	ds 64			; per VRAM page: tiles drawn for priority cells
pri_chg:	ds 64			; per VRAM page: those of them converted again
; assert pri_chg == pri_lf + 256, "fw2_switches clears these three together" (checked by tools/check-layout)

; ----------------------------------------------------------------------
; PSG (SN76489) -> AY, called from a handler through psg_w (fw.asm) and
; fw2_call. See the header there.
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


fw2_end:
; assert fw2_end <= $3C00, "fw2 overflows into rast_code" (checked by tools/check-layout)
		defs ($3C00)-0x2000-$
rast_code:	; the overlay's per-line H scroll hook (CODE op), up to $4000
