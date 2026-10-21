; fw2.asm: the framework's second page (FW2_PAGE), mapped at $2000 (MMU1)
; while vbl_work (fw.asm) runs the once-a-frame work, with interrupts off,
; and for one call from a handler (fw2_call in fw.asm): VDP register
; writes, mapper stores, CRAM extras, the code page table. During vbl_work
; the VRAM shadow is at $4000-$7FFF (VRAM address + $4000) and the Next
; tile definitions at $8000-$BFFF (tile * 32 + $8000). Code here never
; calls into fw4: both pages use slot 1.

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
kn_any:		db 0			; some page in kn_pages is set (kn_block, tile_flushk)
pause_prev:	db 0
pal_vm:		ds 4			; toppal: CRAM entries written in the last vblank phase
cram_top:	ds 32			; toppal: CRAM as the second palettes hold it
cop_dirty:	db 1			; copper list must be rebuilt
nt_dirty:	db 0			; name table base changed: maps rebuilt
h_x:		dw 0			; tilemap X offset for the current H scroll
h_sw:		db 0			; copper column of the M0->A8 switch: 39 (past the picture) for K <= 64, 0 until H is written
cop_sw:		db $FF			; switch column in the copper list now
cop_v:		db $FF			; V scroll in the copper list now
cop_mode:	db $FF			; 0 normal list, 1 lock-right list
bd_cur:		db $FF			; backdrop colour in the ULA palette now
bg_free:	dw 0			; pixel values no background tile on screen uses
					; (kept only while tr_free is 0)
pri_x:		db 254			; Layer 2 X scroll for the current H scroll (K - 2)
lay15:		db 0			; NextReg $15 layer order bits: 4 = L S U (priority tiles)
tm_ctl:		db %00000010		; NextReg $6B without bit 4 (second tilemap palette)
pal_ph:		db 1			; toppal: 1 from the frame event to the first line event
dis_pend:	db 0			; toppal: a display-off write waits for the phase end
dis_ck:		db 0			; vertical blank works since it was held, + 1 (dis_count)
dis_poll:	db 0			; 1: traps with interrupts off count frames (dis_tick2)
dis_wr:		db 0			; frames started since it was held (dis_tick2)
dis_ln:		dw 0			; the Next line at the last count (dis_tick2)
disp_on:	db 0			; the display enable shown: $40 on, 0 off
pal_rows:	ds 24			; per screen row: rows from it to the bottom where
					; sprite-palette tiles show pixel value 0 more than
					; background ones, less the others (fw3 pal_scan)

fw2_init:
		ld hl,tm_mask
		ld de,tm_mask+1
		ld bc,1023
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
; Game start, with fw3 at $0000: the pal_scan pass marks and nibm
fw2_init3:
		ld hl,ps_seen
		ld de,ps_seen+1
		ld bc,511
		ld (hl),0
		ldir
		xor a
		ld (ps_gen),a
		ld hl,nibm		; nibm: bit (high nibble) | bit (low nibble)
fw2_init3__nb:		ld a,l
		call fw2_init3__bit
		push de
		ld a,l
		rrca
		rrca
		rrca
		rrca
		call fw2_init3__bit
		pop bc
		ld a,e
		or c
		ld (hl),a
		inc h
		ld a,d
		or b
		ld (hl),a
		dec h
		inc l
		jr nz,fw2_init3__nb
		ret
; A (low nibble) -> DE = 1 << A, from bits16 in fw3
fw2_init3__bit:	and $0F
		add a,a
		ld de,bits16
		add de,a
		push hl
		ex de,hl
		ld e,(hl)
		inc hl
		ld d,(hl)
		pop hl
		ret

; The vb_ labels mark the phases for tools/measure.lua (NM_VBPH).
fw2_vbl:
		nextreg $50,FW3_PAGE	; fw3 at $0000 (restore_mmu puts the game's page back)
		ld hl,$C1D1		; POP DE, POP BC: fw_exit without vbl_chk (fw.asm)
		ld (fw_exit),hl
		ld a,$ED
		ld (fw_exit+2),a
		ld hl,tw_check		; jt_vwrite's end without vbl_chkv
		ld (vw_tw+1),hl
		ld a,(dis_pend)		; a display-off write held (vdp_reg_w__r1)
		or a
		call nz,dis_count
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
tf_vbl:		call nz,tile_flush	; tilecache: tile_flushk (fw2_switches)
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
; Game start, second part, called by fw_start (fw.asm) after fw4_start,
; with this page at $2000: clip windows, framework state, the game's
; first pages in cur_mmu. fw_start then maps them and starts the game.
; ----------------------------------------------------------------------
fw2_start:
		nextreg $50,FW3_PAGE	; fw2_state and fw2_switches are there, fw2_init
		call fw2_state		; clears tm_mask there
		call fw2_switches
		call fw2_init
		call fw2_init3
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
		; the SMS RAM copy of the mapper registers holds the reset values
		; too: games write them with stores the overlay does not patch,
		; and read them back (R-Type restores both banks from $DFFE)
		nextreg $56,SMSRAM_PAGE	; (fw_start maps cur_mmu after)
		ld hl,$0000
		ld ($DFFC),hl
		ld hl,$0201
		ld ($DFFE),hl
		call fallback2		; the fallback for the start state (cram all 0)
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
		ret z			; $FFFF+1 = $0000: a ROM write, no register
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
		call map_bank_fw2	; $FFFD maps MMU1, where this page runs
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
		nextreg $68,0		; ULA on (the 224-line copper list turns it off in the border lines)
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
		call l2_mode
		call l2_vis
		call clip_update
		call dis_apply		; a held display-off write applies: the game is
					; building a screen in the other mode, not
					; finishing a frame (vdp_reg_w__r1)
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
		ld a,(vdp_regs+9)	; and rows 0-3 while V scroll 32 hides them
		cp 32			; (OutRun's HUD letters are tiles $1C0-$1C7
		jr nz,region_update__sat	; there); their tiles are converted once now,
		ld a,(nt_base+1)	; as they may have been written as name table
		ld l,a
		ld (hl),3
		set 6,l
		ld (hl),$FF
		ld (tiles_dirty),a
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
		ld a,(m224)		; Layer 2 (priority tiles): pixels PIC_X (+ 8) to 255,
		or a			; lines 0-191; in 224-line mode (320x256) as the tilemap
		jr nz,clip_update__l2w
		ld a,e
		add a,a
		add a,PIC_X
		nextreg $18,a
		nextreg $18,255
		nextreg $18,0
		nextreg $18,191
		jr clip_update__tm
clip_update__l2w:	ld a,16+PIC_X/2
		add a,e
		nextreg $18,a
		nextreg $18,143+PIC_X/2
		ld a,b
		nextreg $18,a
		ld a,c
		nextreg $18,a
clip_update__tm:	ld a,16+PIC_X/2
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

; ----------------------------------------------------------------------
; VDP register writes, through fw2_call from vctrl_w (fw.asm).
; ----------------------------------------------------------------------
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

; Converts the tiles VRAM writes have marked, as the vblank work does, from
; a handler: fw3, the shadow and the tile definitions in the vblank work's
; slots, then the game's pages back. A game that loads a level with
; interrupts and the display off would otherwise have them all converted
; in its first vblank after, a frame's time or more. Keeps DE, IX, IY.
tflush2:	ld a,(tiles_dirty)
		or a
		ret z
		ld hl,0
		jr tflush2__go
; The display goes on after the Next had it off (vdp_reg_w__r1on): first
; the picture is made whole, as the vertical blank work would make it, so
; it never shows what the game wrote while the display was off half done.
; The tiles written then are converted, the maps rebuilt if the name table
; moved (nt_dirty), and Layer 2's priority cells drawn (pri_frame: the
; marked cells, the cells of tiles converted again). A game that builds a
; screen with interrupts off gets no vertical blank work until it turns the
; display on, or after. Keeps DE, IX, IY.
pic_ready:	ld hl,pic_ready3	; in fw3
tflush2__go:	push de
		push ix
		push iy
		push hl
		nextreg $50,FW3_PAGE
		nextreg $52,SHADOW_PAGE
		nextreg $53,SHADOW_PAGE+1
		nextreg $54,TILE_PAGE
		nextreg $55,TILE_PAGE+1
tf_tw:		call tile_flush		; tilecache: tile_flushk (fw2_switches)
		pop hl
		ld a,h
		or l
		call nz,jp_hl
		ld a,(cur_mmu+6)	; pic_ready3 maps slot 6
		nextreg $56,a
		ld a,(cur_mmu+0)
		nextreg $50,a
		ld a,(cur_mmu+2)
		nextreg $52,a
		ld a,(cur_mmu+3)
		nextreg $53,a
		ld a,(cur_mmu+4)
		nextreg $54,a
		ld a,(cur_mmu+5)
		nextreg $55,a
		pop iy
		pop ix
		pop de
		ret

; tw_check's flush (fw.asm) and kn_block's: TW_MAX * 256 bytes or more
; written to tiles since their last conversion. While the display is off
; the tiles wait for the conversion when it goes on (vdp_reg_w__r1on) or
; for the vertical blank work: a game that loads with the display off
; often writes a tile in more than one pass (one plane, then the next),
; and a conversion between the passes is work done again. tw_cnt starts
; again, so this runs once each TW_MAX * 256 bytes. Keeps DE, IX, IY.
tw_flush:	ld a,(vdp_regs+1)
		and $40
		jp nz,tflush2
		ld (tw_cnt),a
		ld (tw_cnt+1),a
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
		jp z,fallback2		; 7
		dec a
r8_hk:		jp z,hscroll_set	; 8 (hsplit: hs_reg8, fw2_switches)
		dec a
		jp z,vdp_reg_w__r9
		dec a
		ret nz
		jp ev_recheck2		; 10
vdp_reg_w__r0:		ld a,e
		xor d
		and $28			; mask column 0, sprite shift
		ld a,1
		jr z,vdp_reg_w__r0b
		ld (sat_dirty),a
		push de
		call clip_update
		pop de
vdp_reg_w__r0b:		ld a,e
		xor d
		and $02			; M2: 224-line mode with register 1 bit 4
		call nz,vdp_reg_w__mode_check
		ld a,e
		xor d
		and $10			; IE1
		call nz,ev_recheck2
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
		ld a,(dis_pend)		; turns it off if it is still off then, or the
		or a			; vertical blank work after two frames (dis_count).
		jr nz,vdp_reg_w__r1x		; A second off write while one is held: off now
		ld a,(pal_ph)
		or a
		jr z,vdp_reg_w__r1off
		ld (dis_pend),a
		ld (dis_ck),a		; 1: the vblank work counts from here (dis_count)
		call dis_arm		; and the traps, while interrupts are off
		jr vdp_reg_w__r1m
vdp_reg_w__r1x:		call dis_off
		jr vdp_reg_w__r1off
vdp_reg_w__r1on:		call dis_off
		ld a,(disp_on)		; the display goes on
		or a
		jr nz,vdp_reg_w__r1h
		call pic_ready		; the Next had it off: the picture first
		jr vdp_reg_w__r1off
vdp_reg_w__r1h:		bit 6,d			; the off write was held (toppal): the tiles
		call z,tflush2		; written while it was off are converted now
vdp_reg_w__r1off:		push de
		call r1_hw
		call fallback2
		call l2_vis		; Layer 2 on or off with the display
		pop de
vdp_reg_w__r1m:		ld a,e
		xor d
		and $10			; M1: 224-line mode with register 0 bit 1
		ret z
vdp_reg_w__mode_check:	push de
		call mode_switch
		pop de
		ret
vdp_reg_w__r2:		ld a,e			; the same value again: the base, the page roles
		cp d			; and the maps stand (nt_put keeps the maps), so
		ret z			; no map_rebuild, nor Layer 2's whole rebuild after it
		jp nt_base_set
vdp_reg_w__r5:		ld a,e
		and $7E
		rrca
		ld (sat_hi),a		; (reg5 & $7E) << 7, high byte
		ld a,1
		ld (sat_dirty),a
		jp region_update
vdp_reg_w__r6:		ld a,1
		ld (sat_dirty),a
		ret
vdp_reg_w__r8:		jp hscroll_set
vdp_reg_w__r9:		ld a,1
		ld (cop_dirty),a
		ld a,d			; V scroll to or from 32: rows 0-3 hidden or not
		cp 32
		ld a,0
		jr nz,vdp_reg_w__r9o
		inc a
vdp_reg_w__r9o:		ld b,a
		ld a,e
		cp 32
		ld a,0
		jr nz,vdp_reg_w__r9n
		inc a
vdp_reg_w__r9n:		cp b
		ret z
		jp region_update

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
		ld a,(m224)		; 224-line mode: pri224 sets Layer 2 X
		or a
		jr nz,hscroll_set__nodir
		ld a,(pri_x)
		nextreg $16,a
hscroll_set__nodir:
		; M0 and A8 show the same pixels at SMS x 256-K to 320-K; the
		; switch at column c acts at SMS x 8c (MAME). c = (291 - K) / 8
		; puts 8c + K in 284-291, near the middle (288), so a switch that
		; lands up to 29 pixels later or 28 earlier still looks right
		; (the real Next's copper and tile fetch timing is not MAME's).
		; With K <= 64 no switch is needed; the list has one all the same,
		; at column 39 (SMS x 312, past the picture's right edge), so a
		; scroll across K = 64 changes only the first byte of each line's
		; WAIT (cop_switches and cop_224, fw3).
		ld a,(vdp_regs+8)
		neg
		cp 65
		ld b,39
		jr c,hscroll_set__sw		; K <= 64
		ld b,a
		ld a,255&((291-256))	; 291 - K (K > 64, so it fits in a byte)
		sub b
		rrca
		rrca
		rrca
		and $1F
		ld b,a
hscroll_set__sw:				ld a,b
		ld (h_sw),a
		ld hl,cop_sw
		cp (hl)
		ret z
		ld a,1
		ld (cop_dirty),a
		ret
; Register 8 = E with the hsplit switch (r8_hk above): hscroll_set, then
; sg_write (fw3, mapped at $0000 for it; interrupts are off in a handler), so
; that a write that moves the tilemap in the picture also moves the map
; switch column of the lines still to come.
hs_reg8:	call hscroll_set
		nextreg $50,FW3_PAGE
		call sg_write
		ld a,(cur_mmu+0)
		nextreg $50,a
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

; A display-off write held in the vertical blank phase (vdp_reg_w .r1).
; Keeps DE: it runs from fw_line_irq (pal_vbl2, pal_pic2), which saves
; only AF, HL and BC of the interrupted game, from the vertical blank work
; (dis_count) and from mode_switch.
dis_apply:	ld a,(dis_pend)
		or a
		ret z
		call dis_off
		push de
		call r1_hw
		call fallback2
		call l2_vis
		pop de
		ret

; dis_pend off, and dis_chk out of fw_exit. Uses A.
dis_off:	xor a
		ld (dis_pend),a
		ld (dis_poll),a
		ld a,(fw_exit+1)
		cp 255&(dis_chk)
		ret nz
		ld a,(fw_exit+2)
		cp 255&((dis_chk)>>8)
		ret nz
		ld a,$D1		; POP DE, POP BC, and LD SP,(nn)'s first byte
		ld (fw_exit),a
		ld a,$C1
		ld (fw_exit+1),a
		ld a,$ED
		ld (fw_exit+2),a
		ret
; A display-off write is held, and the vertical blank work runs: the third
; time it runs with the write still held, the write applies (dis_apply).
; The display has then been off for more than two frames: the game builds a
; screen with interrupts off (Micro Machines' menus), and gets no frame or
; line event, which would apply it; the Next would go on showing the
; picture the game rebuilds. A game whose frame work only runs late (the
; Next is slower than the SMS) turns the display on before that: the
; Micro Machines race writes it off at line 211 and on again up to 300
; lines later, one vertical blank work later at most. Uses A, HL.
dis_count:	ld hl,dis_ck
		inc (hl)
		ld a,(hl)
		cp 4
		jp nc,dis_apply
		jr dis_patch		; the work took dis_chk out of fw_exit

; A display-off write is held outside the game's frame handler: from here
; the traps that return to a game with interrupts off count the frames that
; start (dis_chk in fw.asm). A game that loads with interrupts off (Micro
; Machines before a race, from its main code) gets no vertical blank work,
; so dis_count never runs; the third frame that starts with the write still
; held applies it (dis_tick2). A write held inside the frame handler (the
; game's $0038 entry has not returned: SP below its return slot, which still
; holds the return address or isr_tramp, as frm_run tests) is not counted
; here: the handler turns the display on again, or returns and the frame
; events and vertical blank work go on; a late handler that runs past the
; next frame (the Micro Machines race) would pay for every trap. Keeps DE.
; Uses A, BC, HL.
dis_arm:	push de
		ld hl,(fw_sp)
		ld de,(isr_sp)
		or a
		sbc hl,de
		jr nc,dis_arm__go	; SP at or above the slot: no frame handler runs
		ex de,hl
		ld e,(hl)
		inc hl
		ld d,(hl)		; DE = what the slot holds
		ld hl,(isr_ret)
		or a
		sbc hl,de
		jr z,dis_arm__no
		ld hl,isr_tramp
		or a
		sbc hl,de
		jr z,dis_arm__no
dis_arm__go:	pop de
		ld a,1
		ld (dis_poll),a
		xor a
		ld (dis_wr),a
		call dis_line
		ld (dis_ln),hl
		jr dis_patch
dis_arm__no:	pop de
		ret
; fw_exit through dis_chk, unless vbl_chk is there (its vertical blank work
; counts with dis_count, which calls this again after it)
dis_patch:	ld a,(fw_exit)
		cp $C3			; JP
		ret z
		ld hl,dis_chk
		ld (fw_exit+1),hl
		ld a,$C3
		ld (fw_exit),a
		ret
; HL = the Next's raster line (0-310). Uses A, BC.
dis_line:	ld bc,$243B
		ld a,$1E
		out (c),a
		inc b
		in h,(c)		; line bit 8
		dec b
		ld a,$1F
		out (c),a
		inc b
		in l,(c)
		dec b
		ld a,$1E
		out (c),a
		inc b
		in a,(c)
		cp h
		jr nz,dis_line		; bit 8 changed between the reads
		ld a,h
		and 1
		ld h,a
		ret
; From dis_chk (fw.asm, through fw2_call) at every DIS_N-th trap's exit:
; with the game's interrupts off, a frame started since the last count when
; the line is lower than then. A game that holds interrupts off for a load
; makes many traps a frame; one that makes fewer than DIS_N in a frame has
; its frames counted late, never early. Uses A, BC, DE, HL.
dis_tick2:	ld a,DIS_N
		ld (dis_n),a
		ld a,(dis_poll)
		or a
		ret z
		ld a,(exit_ei)		; interrupts on: the vertical blank work counts
		or a
		ret nz
		call dis_line
		ld de,(dis_ln)
		ld (dis_ln),hl
		or a
		sbc hl,de
		ret nc
		ld hl,dis_wr
		inc (hl)
		ld a,(hl)
		cp 3
		ret c
		jp dis_apply
jp_hl:		jp (hl)

; Layer 2 shown while the display is on, with priority tiles, not in
; 224-line mode (the 256x192 Layer 2 does not reach those lines)
l2_vis:		ld a,(fw_flags)
		rra
		ld a,0
		jr nc,l2_vis__o
		ld a,(disp_on)
		or a
		jr z,l2_vis__o
		ld a,2
l2_vis__o:		ld bc,$123B
		out (c),a
		ret

; Layer 2's resolution and pages for the mode: 256x192 from L2_BANK, or
; 320x256 from L2W_BANK in 224-line mode (pri224)
l2_mode:	ld a,(m224)
		or a
		jr nz,l2_mode__w
		nextreg $70,0
		nextreg $12,L2_BANK
		nextreg $71,0
		ret
l2_mode__w:	nextreg $70,%00010000
		nextreg $12,L2W_BANK
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
; 224-line mode: pri224. Not done: the locked right columns with V scroll
; (they show the V-scrolled cells), the locked top rows in 224-line mode,
; per-line H scroll from a rastercode hook.
; ----------------------------------------------------------------------
pri_frame:
		ld a,(fw_flags)
		rra
		ret nc
		nextreg $50,MAP_PAGE	; the marks: $1BE0 + row, $1C00 + cell
		ld a,$FF
		ld (pri_pg),a
		ld a,(m224)
		or a
		jp nz,pri224
		ld a,(vdp_regs+9)
		cp 224
		jr c,pri_frame__v
		sub 224
pri_frame__v:		ld (pri_nv),a
		ld a,(pri_full)
		or a
		jp nz,pri_hide		; then pri_rebuild
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
pri_end:	nextreg $50,FW3_PAGE
		ld a,(pri_hid)
		or a
		ret z
		xor a			; a whole rebuild is done: Layer 2 as the
		ld (pri_hid),a		; display shows it, but hidden while a
		ld a,(dis_pend)		; display-off write is held (the game
		or a			; builds a screen: Layer 2 shows with it
		ret nz			; when the display goes on, vdp_reg_w)
		jp l2_vis

; A whole rebuild of Layer 2 (start, name table base, mode) draws every
; priority cell and clears the rest, which can take frames (Micro
; Machines, 695 cells in 224-line mode: 8 frames). Layer 2 is hidden until
; it is complete (pri_end), so it never shows half the cells of one screen
; and half of another.
pri_hide:	call pri_hid1
		jp pri_rebuild
p2_hide:	call pri_hid1
		jp p2_rebuild
pri_hid1:	ld a,1
		ld (pri_hid),a
		xor a
		ld bc,$123B
		out (c),a
		ret
pri_hid:	db 0			; Layer 2 hidden for a whole rebuild

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
; Priority tiles in 224-line mode. Layer 2 is 320x256 (pages L2W_PAGE to
; L2W_PAGE+9, a column of 256 bytes after the other, 32 columns a page),
; so it covers the 224 lines and all 32 rows of the SMS map: Layer 2 line
; y holds map line y, and the Y scroll (NextReg $17) is V - 16, as SMS line
; 0 is 16 lines above the 192-line area. Across, the 320 columns are 40
; groups of 8, and a ring of 33 groups holds the 32 map cell columns: map
; cell column p2_kc + i in group p2_bg + i (mod 40), and p2_kc once more in
; group p2_bg + 32, so the 256 pixels from any map column in p2_kc's cell
; are 256 Layer 2 columns in a row. When H scroll moves the first map
; column shown into another cell, the ring moves with it and only the cell
; columns that change group are drawn (p2_col). P2_ROWS keeps, per group,
; the rows that may hold pixels. Marks and pri_chg work as in 192-line mode.
; ----------------------------------------------------------------------
pri224:		ld a,(pri_full)
		or a
		jp nz,p2_hide		; then p2_rebuild
		ld a,(vdp_regs+8)
		neg			; K: the first map column shown
		ld (p2_k),a
		rrca
		rrca
		rrca
		and $1F
		ld hl,p2_kc
		sub (hl)
		and $1F			; cells moved right (mod 32)
		jr z,p2_cells
		cp 16
		jr nc,p2_left
		ld b,a			; right: cell columns kc+1..kc+d into groups bg+33..bg+32+d
		ld c,1
p2_right__l:	push bc
		ld a,(p2_kc)
		add a,c
		and $1F
		ld (pr_c),a
		ld a,(p2_bg)
		add a,32
		add a,c
		call p2_mod40
		call p2_col
		pop bc
		inc c
		djnz p2_right__l
		dec c			; d
		ld a,(p2_kc)
		add a,c
		and $1F
		ld (p2_kc),a
		ld a,(p2_bg)
		add a,c
		call p2_mod40
		ld (p2_bg),a
		jr p2_cells
p2_left:	neg
		add a,32		; e: cells moved left
		ld c,a
		ld a,(p2_kc)
		sub c
		and $1F
		ld (p2_kc),a
		ld a,(p2_bg)
		sub c
		jr nc,p2_left__b
		add a,40
p2_left__b:	ld (p2_bg),a
		ld b,c			; cell columns kc'..kc'+e-1 into groups bg'..bg'+e-1
		ld c,0
p2_left__l:	push bc
		ld a,(p2_kc)
		add a,c
		and $1F
		ld (pr_c),a
		ld a,(p2_bg)
		add a,c
		call p2_mod40
		call p2_col
		pop bc
		inc c
		djnz p2_left__l
		ld a,(p2_kc)		; and kc' once more after the ring
		ld (pr_c),a
		ld a,(p2_bg)
		add a,32
		call p2_mod40
		call p2_col
p2_cells:	ld a,(pri_redo)		; tiles of priority cells changed
		or a
		call nz,p2_redraw
		ld b,0			; marked cells, row by row
p2_cells__r:	ld h,$1B
		ld a,b
		add a,$E0
		ld l,a
		ld a,(hl)
		or a
		jr z,p2_cells__rn
		ld (hl),0
		ld a,b
		ld (pr_r),a
		push bc
		xor a
p2_cells__c:	ld (pr_c),a
		call pri_mk
		bit 0,(hl)
		jr z,p2_cells__cn
		res 0,(hl)
		call p2_cell
p2_cells__cn:	ld a,(pr_c)
		inc a
		cp 32
		jr nz,p2_cells__c
		pop bc
p2_cells__rn:	inc b
		ld a,b
		cp 32
		jr nz,p2_cells__r
p2_done:	ld a,(p2_bg)		; Layer 2 X: map column K at SMS x 0, at Next
		ld l,a			; X 34 (left border + PIC_X)
		ld h,0
		add hl,hl
		add hl,hl
		add hl,hl		; 8 bg
		ld a,(p2_k)
		and 7
		add hl,a
		ld de,320-34
		add hl,de
		ld de,-320
p2_done__m:	add hl,de
		jr c,p2_done__m
		ld de,320
		add hl,de		; (8 bg + (K and 7) - 34) mod 320
		ld a,l
		nextreg $16,a
		ld a,h
		nextreg $71,a
		ld a,(vdp_regs+9)
		sub 16
		nextreg $17,a
		jp pri_end

; A = 0-79 -> A mod 40
p2_mod40:	cp 40
		ret c
		sub 40
		ret

; The whole of Layer 2 from the name table (start, mode, name table base)
p2_rebuild:	xor a
		ld (pri_full),a
		ld (pri_redo),a		; every cell is drawn from its tile now
		ld hl,pri_chg
		ld b,64
p2_rebuild__c:	ld (hl),a
		inc hl
		djnz p2_rebuild__c
		ld hl,$1BC0		; no marks
		ld de,$1BC1
		ld bc,$0440-1
		ld (hl),a
		ldir
		ld hl,pri_tiles
		ld b,64
p2_rebuild__t:	ld (hl),0
		inc hl
		djnz p2_rebuild__t
		ld a,(vdp_regs+8)
		neg
		ld (p2_k),a
		rrca
		rrca
		rrca
		and $1F
		ld (p2_kc),a
		xor a
		ld (p2_bg),a
		ld b,40			; every group: the ring's 33, the other 7 cleared
p2_rebuild__g:	push bc
		ld a,40
		sub b
		ld (p2_g),a
		cp 33
		jr nc,p2_rebuild__x
		ld c,a
		ld a,(p2_kc)
		add a,c
		and $1F
		ld (pr_c),a
		ld a,c
		call p2_col
		jr p2_rebuild__n
p2_rebuild__x:	call p2_gclr
p2_rebuild__n:	pop bc
		djnz p2_rebuild__g
		jp p2_done

; Group A gets cell column pr_c: the rows it held are cleared, then each
; priority cell of the column is drawn
p2_col:		ld (p2_g),a
		call p2_gclr
		xor a
p2_col__r:	ld (pr_r),a
		call pri_ent
		ld a,(pr_th)
		and $10
		jr z,p2_col__n
		call pri_mk
		set 1,(hl)
		call pri_tile
		call p2_put
p2_col__n:	ld a,(pr_r)
		inc a
		cp 32
		jr nz,p2_col__r
		ret

; Group p2_g: the cells of the rows it may hold pixels in cleared
p2_gclr:	call p2_rowp		; HL = its 4 row bytes
		ld c,0			; row
p2_gclr__b:	ld a,(hl)
		ld (hl),0
		ld b,8
p2_gclr__r:	rrca
		jr nc,p2_gclr__n
		push af
		push bc
		push hl
		ld a,c
		ld (pr_r),a
		call p2_zero
		pop hl
		pop bc
		pop af
p2_gclr__n:	inc c
		djnz p2_gclr__r
		inc hl
		ld a,c
		cp 32
		jr nz,p2_gclr__b
		ret

; HL = P2_ROWS entry of group p2_g (4 bytes, bit r = row r)
p2_rowp:	ld a,(p2_g)
		add a,a
		add a,a
		ld hl,P2_ROWS
		add hl,a
		ret
; HL = the byte of row pr_r in group p2_g's P2_ROWS entry, A = its bit
p2_rowb:	call p2_rowp
		ld a,(pr_r)
		rrca
		rrca
		rrca
		and 3
		add hl,a
		ld a,(pr_r)
		and 7
		ld de,pri_bit
		add de,a
		ld a,(de)
		ret

; Cell (pr_r, pr_c) again, in its group and, for column p2_kc, the group
; after the ring too: its tile with the priority bit, else zeros where the
; group holds pixels. Bit 1 of its mark: Layer 2 holds it.
p2_cell:	call pri_ent
		call pri_mk
		ld a,(pr_th)
		and $10
		jr nz,p2_cell__p
		res 1,(hl)
		jr p2_cell__g
p2_cell__p:	set 1,(hl)
p2_cell__g:	ld a,(pr_c)
		ld hl,p2_kc
		sub (hl)
		and $1F
		ld hl,p2_bg
		add a,(hl)
		call p2_mod40
		call p2_cell1
		ld a,(pr_c)
		ld hl,p2_kc
		cp (hl)
		ret nz
		ld a,(p2_bg)
		add a,32
		call p2_mod40
p2_cell1:	ld (p2_g),a
		ld a,(pr_th)
		and $10
		jr z,p2_cell1__z
		call pri_tile
		jp p2_put
p2_cell1__z:	call p2_rowb		; zeros where the group holds pixels
		and (hl)
		ret z
		jp p2_zero

; Slot 6 = the Layer 2 page of group p2_g; DE = the cell (p2_g, pr_r) there
p2_page:	ld a,(p2_g)
		ld e,a
		rrca
		rrca
		and $3F
		add a,L2W_PAGE
		ld hl,pri_pg
		cp (hl)
		jr z,p2_page__s
		ld (hl),a
		nextreg $56,a
p2_page__s:	ld a,e
		and 3
		add a,a
		add a,a
		add a,a
		or $C0
		ld d,a
		ld a,(pr_r)
		add a,a
		add a,a
		add a,a
		ld e,a
		ret

; Cell (p2_g, pr_r): zeros, and its row's bit in P2_ROWS cleared
p2_zero:	call p2_rowb
		cpl
		and (hl)
		ld (hl),a
		call p2_page
		ld c,e
		xor a
		ld b,8
p2_zero__c:
		rept 8
		ld (de),a
		inc e
		endr
		ld e,c
		inc d
		djnz p2_zero__c
		ret

; Cell (p2_g, pr_r): the tile of pr_tl/pr_th, a column of Layer 2 after the
; other for its 8 pixels; its row's bit in P2_ROWS set
p2_put:		call p2_rowb
		or (hl)
		ld (hl),a
		call p2_page
		ld a,(pr_th)
		ld b,a
		and 1
		ld h,a
		ld a,(pr_tl)
		ld l,a
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl
		add hl,hl		; tile * 32
		ld a,h
		add a,$80		; Next tile definitions at $8000
		ld h,a
		ld a,b
		and 8
		add a,a
		ld c,a			; $10: the sprite palette (entries 16-31)
		ld a,b
		ld (p2_fl),a
		bit 2,a			; V flip: from the last row up
		jr z,p2_put__v
		ld a,28
		add hl,a
p2_put__v:	ld a,8
		ld (p2_n),a
p2_put__r:	ld b,4
		ld a,(p2_fl)
		bit 1,a			; H flip
		jr nz,p2_put__f
p2_put__p:	ld a,(hl)
		swapnib
		and $0F
		or c
		ld (de),a
		inc d
		ld a,(hl)
		and $0F
		or c
		ld (de),a
		inc d
		inc hl
		djnz p2_put__p
		jr p2_put__n
p2_put__f:	inc hl
		inc hl
		inc hl
p2_put__q:	ld a,(hl)
		and $0F
		or c
		ld (de),a
		inc d
		ld a,(hl)
		swapnib
		and $0F
		or c
		ld (de),a
		inc d
		dec hl
		djnz p2_put__q
		ld a,5
		add hl,a
p2_put__n:	ld a,d
		sub 8
		ld d,a
		inc e
		ld a,(p2_fl)
		bit 2,a
		jr z,p2_put__d
		ld a,l			; V flip: back 2 rows
		sub 8
		ld l,a
		jr nc,p2_put__d
		dec h
p2_put__d:	ld a,(p2_n)
		dec a
		ld (p2_n),a
		jr nz,p2_put__r
		ret

; pri_redo: every priority cell whose tile changed (pri_chg), then pri_chg
; is cleared
p2_redraw:	xor a
		ld (pri_redo),a
		ld (pr_r),a
p2_redraw__r:	xor a
		ld (pr_c),a
		call pri_ent		; HL = the row's first entry (high byte)
		ld b,32
p2_redraw__c:	bit 4,(hl)
		jr z,p2_redraw__n
		push hl
		push bc
		ld a,32
		sub b
		ld (pr_c),a
		call pri_ent
		call pri_tbit		; HL = its pri_chg byte, A = bit
		and (hl)
		call nz,p2_cell
		pop bc
		pop hl
p2_redraw__n:	inc hl
		inc hl
		djnz p2_redraw__c
		ld a,(pr_r)
		inc a
		ld (pr_r),a
		cp 32
		jr nz,p2_redraw__r
		ld hl,pri_chg
		ld b,64
p2_redraw__z:	ld (hl),0
		inc hl
		djnz p2_redraw__z
		ret

p2_k:		db 0			; K, the first map column shown
p2_kc:		db 0			; the ring's first cell column
p2_bg:		db 0			; and its group
p2_g:		db 0			; the group being drawn
p2_fl:		db 0			; the entry's high byte while it is drawn
p2_n:		db 0			; rows left to draw
P2_ROWS		equ $1400		; per group, 4 bytes: the rows that may hold pixels
					; (MAP_PAGE, here at $0000, after the A8 map)

; ----------------------------------------------------------------------
; Code pages (far_go in fw.asm calls this with this page at $2000): the
; RAM page and address of entry far_e of the file's page far_p. Returns
; A = the RAM page, HL = the entry. A page the file does not have, or an
; entry the page does not list, stops the game (fw_fatal). Keeps BC, DE.
; Notes slot 1's page before the call in far_prev, and in pg_under too
; when it is not a code page (the outermost call: the game's own page).
far_find:	ld hl,pg_irq		; the game's interrupt entries through pg_irq
		ld (irq_t1+1),hl	; (irq_slot1 puts $0038 back)
		ld (irq_t2+1),hl
		ld a,(cur_mmu+1)
		ld (far_prev),a
		sub CODE_PAGE
		cp CODE_MAX
		jr c,far_find__in
		ld a,(far_prev)
		ld (pg_under),a
far_find__in:	ld a,(far_p)
		cp CODE_MAX
		jp nc,fw_fatal
		ld hl,pg_ram
		add hl,a
		ld a,(hl)
		or a
		jp z,fw_fatal
		push de
		ld d,a			; the RAM page
		ld a,CODE_MAX
		add hl,a		; pg_n
		ld a,(far_e)
		cp (hl)
		jp nc,fw_fatal
		ld e,a
		ld a,CODE_MAX
		add hl,a		; pg_first
		ld a,e
		add a,(hl)		; the entry's place in pg_ent
		ld hl,pg_ent
		add hl,a
		add hl,a
		ld a,(hl)
		inc hl
		ld h,(hl)
		ld l,a
		ld a,d
		pop de
		ret
; From pg_irq (fw.asm): a game interrupt entry, its return slot at irq_s,
; while irq_t1 and irq_t2 lead to pg_irq. The game's handler must not see
; a code page in $2000-$3FFF. If cur_mmu+1 names one (the interrupt came
; while a far call's entry ran), cur_mmu+1 becomes the game's page under it
; (pg_under), and pg_tramp (fw.asm) goes in the return slot to put the code
; page back when the handler returns. If not, no far call is running, and
; irq_t1 and irq_t2 go back to $0038. fw2_call then maps cur_mmu+1 in slot
; 1, which also covers an interrupt between a write of cur_mmu+1 and its
; NEXTREG. One such return is pending at a time: while a frame handler
; runs, the runtime holds further events (frm_run). Uses A, HL.
irq_slot1:	ld a,(cur_mmu+1)
		sub CODE_PAGE
		cp CODE_MAX
		jr c,irq_slot1__cp
		ld hl,$0038
		ld (irq_t1+1),hl
		ld (irq_t2+1),hl
		ret
irq_slot1__cp:	ld a,(cur_mmu+1)
		ld (pg_tramp_p+1),a
		push de
		ld hl,(irq_s)
		ld e,(hl)
		inc hl
		ld d,(hl)
		ld (pg_tramp_j1+1),de
		ld (pg_tramp_j2+1),de
		ld (hl),pg_tramp>>8
		dec hl
		ld (hl),255&pg_tramp
		ld hl,(isr_sp)		; a frame entry (irq_go, frm_rec): its noted
		ld a,(irq_s)		; return address is now pg_tramp, so that
		cp l			; frm_run still sees the handler run
		jr nz,irq_slot1__nf
		ld a,(irq_s+1)
		cp h
		jr nz,irq_slot1__nf
		ld hl,(isr_ret)
		or a
		sbc hl,de
		jr nz,irq_slot1__nf
		ld hl,pg_tramp
		ld (isr_ret),hl
irq_slot1__nf:	pop de
		ld a,(pg_under)
		ld (cur_mmu+1),a
		ret
; From fw_ula_irq (fw.asm): the pause NMI goes to the game's $0066, its
; return slot at DE. As irq_slot1, the handler gets the game's page in
; slot 1 if a far call's entry runs, and returns through pg_tramp. irq_t1
; and irq_t2 stay as they are, and the NMI is not a frame entry. Uses A,
; HL, DE.
nmi_slot1:	ld a,(cur_mmu+1)
		sub CODE_PAGE
		cp CODE_MAX
		ret nc
		ld a,(cur_mmu+1)
		ld (pg_tramp_p+1),a
		ex de,hl
		ld e,(hl)
		inc hl
		ld d,(hl)
		ld (pg_tramp_j1+1),de
		ld (pg_tramp_j2+1),de
		ld (hl),pg_tramp>>8
		dec hl
		ld (hl),255&pg_tramp
		ld a,(pg_under)
		ld (cur_mmu+1),a
		ret
; ----------------------------------------------------------------------
; Tiles from cart ROM. tc_build (fw4) converts the whole cart at game start
; into CONVT_PAGE: page n of the cart in page CONVT_PAGE + n, every 4 bytes
; converted as one row of a tile, at the same offset. vram_block calls
; kn_block (fw2_call) after every block. For a block not read from RAM,
; kn_note takes each tile the block wrote whole, from one cart page, with
; its source 4-byte aligned like its VRAM address (so its rows are rows of
; the converted page): it notes the tile's converted copy in TKC_PAGE (page
; and address in slot 6) and sets its kn_pages bit in place of its
; dirty_pages bit. tile_flush (fw3) copies such a tile from the converted
; page instead of converting the shadow. Any later write to the tile sets
; its dirty_pages bit, and the shadow is converted as before.
; TKC_PAGE, at $C000 while it is used:
KN_PAGES	equ $C000+(255&dirty_pages)	; per VRAM page a bit per tile, at the same
					; low byte as dirty_pages
TK_PG		equ $C100		; per tile (512): the converted page
TK_LO		equ $C300		; per tile: the address, low byte
TK_HI		equ $C500		; per tile: the address, high byte ($C0-$DF)
; ----------------------------------------------------------------------
; From kn_entry (fw.asm) at the end of vram_block, through fw2_call, for a
; block not read from RAM or the trace buffer: DE = the source after the
; block. Ends with tw_check's work.
kn_block:
		call kn_note
		ld a,(tw_cnt+1)
		cp TW_MAX
		ret c
		jp tw_flush
; DE = the source after the block
kn_note:
		ld hl,(blk_cnt)
		ex de,hl
		or a
		sbc hl,de		; HL = the block's source
		ld de,(blk_start)
		ld a,l
		sub e
		and 3
		ret nz			; source and VRAM address not aligned alike
		push hl
		ld hl,(blk_cnt)
		add hl,de		; the VRAM end
		ld a,h
		cp $40
		jr c,kn_block__e
		jp nz,kn_block__r
		ld a,l
		or a
		jp nz,kn_block__r	; the block wraps past $3FFF
kn_block__e:	ld a,l
		and $E0
		ld l,a
		ld (kn_end),hl		; the end of the last whole tile
		ld hl,31
		add hl,de
		ld a,l
		and $E0
		ld l,a			; HL = the first whole tile
		or a
		sbc hl,de		; its offset in the block
		ld b,h
		ld c,l
		pop hl
		add hl,bc		; HL = its source
		ex de,hl
		add hl,bc
		ex de,hl		; DE = the first whole tile
		push hl
		ld hl,(kn_end)
		or a
		sbc hl,de
		jp c,kn_block__r
		jp z,kn_block__r	; no whole tile
		add hl,hl
		add hl,hl
		add hl,hl
		ld a,h
		ld (kn_n),a		; whole tiles
		ld a,e
		call tmask		; the first tile's bit
		ld (kn_bit),a
		ld a,e			; BC = TK_PG + tile (VRAM address / 32)
		rlca
		rlca
		rlca
		and 7
		ld c,a
		ld a,d
		add a,a
		add a,a
		add a,a
		or c
		ld c,a
		ld a,d
		rlca
		rlca
		rlca
		and 1
		add a,255&(TK_PG>>8)
		ld b,a
		pop hl
		nextreg $56,TKC_PAGE
kn_block__t:	; DE = the tile's VRAM address, HL = its source, BC = TK_PG + tile
		push hl
		ld h,255&((region_tab)>>8)
		ld l,d
		ld a,(hl)
		pop hl
		or a
		jp z,kn_block__rg
		cp 3
		jp z,kn_block__rg	; name table rows that hold tiles too
		cp 2
		jp nz,kn_block__nx	; the name table
		ld a,e
		and $C0
		cp $40
		jp nz,kn_block__nx	; sprite table bytes the VDP reads
kn_block__rg:	ld a,h
		or $E0
		inc a
		jr nz,kn_block__in
		ld a,l
		cp $E1
		jp nc,kn_block__nx	; the source runs into the next 8K slot
kn_block__in:	ld a,h
		rlca
		rlca
		rlca
		and 7
		cp 6
		jp nc,kn_block__nx	; SMS RAM
		push hl
		ld hl,cur_mmu
		add hl,a
		ld a,(hl)
		ld hl,fw_npages
		sub CART_PAGE
		jr c,kn_block__np
		cp (hl)
		jr nc,kn_block__np	; cart RAM
		pop hl
kn_block__nt:	add a,CONVT_PAGE
		ld (bc),a		; TK_PG: the converted page
		inc b
		inc b
		ld a,l
		ld (bc),a		; TK_LO
		inc b
		inc b
		ld a,h
		and $1F
		or $C0
		ld (bc),a		; TK_HI: in slot 6
		dec b
		dec b
		dec b
		dec b
		push hl
		ld h,255&((region_tab)>>8)
		ld l,d
		set 6,l			; dirty_pages entry off, kn_pages entry on
		ld a,(kn_bit)
		cpl
		and (hl)
		ld (hl),a
		ld h,255&(KN_PAGES>>8)
		ld a,(kn_bit)
		or (hl)
		ld (hl),a
		ld (kn_any),a
		pop hl
		jp kn_block__nx
kn_block__np:	pop hl
kn_block__nx:	ld a,(kn_bit)
		rlca
		ld (kn_bit),a
		inc bc
		ld a,e
		add a,32
		ld e,a
		jr nc,kn_block__d
		inc d
kn_block__d:	ld a,l
		add a,32
		ld l,a
		jr nc,kn_block__s
		inc h
kn_block__s:	ld a,(kn_n)
		dec a
		ld (kn_n),a
		jp nz,kn_block__t
kn_block__x:	ld a,(cur_mmu+6)
		nextreg $56,a
		ret
kn_block__r:	pop hl
		ret

kn_end:		dw 0
kn_n:		db 0
kn_bit:		db 0

; The table of the overlay's code pages. The loader clears it before it
; reads a file and fills it from the file's PAGE chunks, through MMU6.
pg_tab:
pg_ram:		ds CODE_MAX		; RAM page of each page number, 0 = none
pg_n:		ds CODE_MAX		; its number of entries
pg_first:	ds CODE_MAX		; its first entry in pg_ent
pg_ent:		ds 2*CODE_ENTS		; entry addresses, in $2000-$3FFF


fw2_end:
; assert fw2_end <= $3C00, "fw2 overflows into rast_code" (checked by tools/check-layout)
		defs ($3C00)-0x2000-$
rast_code:	; the overlay's per-line H scroll hook (CODE op), up to $4000
