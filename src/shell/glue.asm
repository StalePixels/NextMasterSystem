; glue.asm: resident glue between the C shell and the operating system and
; the runtime. Lives in bank 2 and is always mapped.
;
; Called from C with one pointer argument in HL (__z88dk_fastcall). IX is
; the C frame pointer, so every routine keeps it.

		include "memplan.inc"
		include "fwsyms.inc"

		extern _nm_name
		extern _nm_lname
		extern _nm_run

		public _nm_esx
		public _nm_p3dos
		public _nm_launch
		public _nm_resume
		public _nm_basic

NM_STACK_TOP	equ $BFE0		; same as NM_STACK_TOP in nm.h
M_P3DOS		equ $94
NM_LNAME_MAX	equ 127			; nm_lname is one byte longer

		section code_user

; ---------------------------------------------------------------------
; uint8_t nm_esx(struct nm_esx *p): { fn, a, bc, ix, de }. Returns 1 on
; error.
_nm_esx:
		push ix
		push hl			; p
		ld a,(hl)
		ld (esx_fn),a
		inc hl
		push hl			; -> a
		inc hl
		ld c,(hl)
		inc hl
		ld b,(hl)
		inc hl
		ld e,(hl)
		inc hl
		ld d,(hl)
		inc hl
		push de			; ix
		ld e,(hl)
		inc hl
		ld d,(hl)		; de
		pop ix
		pop hl
		ld a,(hl)
		rst 8
esx_fn:		db 0
		push af
		pop de			; D = A, E = F
		pop hl			; p
		inc hl
		ld (hl),d		; a
		inc hl
		ld (hl),c
		inc hl
		ld (hl),b		; bc
		ld a,e
		and 1
		ld l,a
		ld h,0
		pop ix
		ret

; ---------------------------------------------------------------------
; uint8_t nm_p3dos(struct nm_p3 *p): { a, hl, de, bc, f, routine, opt }.
; Sets MMU 6 and 7 to pages 0 and 1 for the call, as NextZXOS expects, and
; puts them back. Returns F.
_nm_p3dos:
		push ix
		push iy
		push hl			; p
		ld a,$56
		call nr_read
		ld (p3_mmu),a
		ld a,$57
		call nr_read
		ld (p3_mmu+1),a
		nextreg $56,0
		nextreg $57,1
		push hl
		pop ix
		ld iy,$5C3A
		ld l,(ix+1)
		ld h,(ix+2)
		ld e,(ix+3)
		ld d,(ix+4)
		ld c,(ix+5)
		ld b,(ix+6)
		ld a,(ix+0)
		exx			; the parameters are now the alternate registers
		ld e,(ix+8)
		ld d,(ix+9)
		ld c,7
		rst 8
		db M_P3DOS
		ld (p3_hl),hl
		ld (p3_de),de
		ld (p3_bc),bc
		push af
		pop hl
		ld (p3_af),hl
		exx
		; the name: success is carry and zero set
		ld a,(p3_af)
		and $41
		cp $41
		jr nz,p3_noname
		pop hl
		push hl
		push hl
		pop ix
		bit 0,(ix+10)
		jr z,p3_noname
		nextreg $56,14
		nextreg $57,15
		ld hl,(p3_hl)
		ld de,_nm_name
		ld b,12
p3_cp:		ld a,(hl)
		cp $FF
		jr z,p3_cpd
		ld (de),a
		inc hl
		inc de
		djnz p3_cp
p3_cpd:		xor a
		ld (de),a
		ld hl,(p3_de)		; the long name, $FF terminated
		ld de,_nm_lname
		ld b,NM_LNAME_MAX
p3_cl:		ld a,(hl)
		cp $FF
		jr z,p3_cld
		ld (de),a
		inc hl
		inc de
		djnz p3_cl
p3_cld:		xor a
		ld (de),a
p3_noname:	ld a,(p3_mmu)
		nextreg $56,a
		ld a,(p3_mmu+1)
		nextreg $57,a
		pop hl			; p
		inc hl
		ld de,(p3_hl)
		ld (hl),e
		inc hl
		ld (hl),d
		inc hl
		ld de,(p3_de)
		ld (hl),e
		inc hl
		ld (hl),d
		inc hl
		ld de,(p3_bc)
		ld (hl),e
		inc hl
		ld (hl),d
		inc hl
		ld a,(p3_af)
		ld (hl),a		; f
		ld l,a
		ld h,0
		pop iy
		pop ix
		ret

; A = NextReg number, returns its value in A
nr_read:	push bc
		ld bc,$243B
		out (c),a
		inc b
		in a,(c)
		pop bc
		ret

; ---------------------------------------------------------------------
; void nm_launch(struct nm_launch *p): save the NextZXOS pages the runtime
; overwrites, copy the start-up values into the runtime and jump to it.
; Layout of *p: see struct nm_launch in nm.h.
L_NPAGES	equ 8
L_START		equ 9
L_SP		equ 11
L_HOOK		equ 13
L_HOOK2		equ 15
L_FLAGS		equ 17
L_NR		equ 18
L_NR_LEN	equ 43

_nm_launch:
		di
		push hl
		pop ix
		nextreg $56,0
		ld a,TILE_PAGE
		ld b,SAVE5_PAGE
		call lcopy_page
		ld a,TILE_PAGE+1
		ld b,SAVE5_PAGE+1
		call lcopy_page
		ld a,MAP_PAGE
		ld b,SAVE7_PAGE
		call lcopy_page
		nextreg $50,$FF
		nextreg $51,$FF
		nextreg $57,FW_PAGE
		push ix
		pop hl
		ld de,FW_CRC
		ld bc,9			; CRC, size, page count
		ldir
		ld l,(ix+L_START)
		ld h,(ix+L_START+1)
		ld (FW_START_ADDR),hl
		ld l,(ix+L_SP)
		ld h,(ix+L_SP+1)
		ld (FW_START_SP),hl
		ld l,(ix+L_HOOK)
		ld h,(ix+L_HOOK+1)
		ld (RAST_HOOK),hl
		ld l,(ix+L_HOOK2)
		ld h,(ix+L_HOOK2+1)
		ld (RAMP_HOOK),hl
		ld a,(ix+L_FLAGS)
		ld (FW_FLAGS),a
		ld hl,_nm_resume
		ld (FW_RESUME+1),hl
		push ix
		pop hl
		ld de,L_NR
		add hl,de
		ld de,NR_SAVED
		ld bc,L_NR_LEN
		ldir
		jp $E00C		; jump table: start the game

; A = source page, B = destination page (slots 0 and 1)
lcopy_page:	nextreg $50,a
		ld a,b
		nextreg $51,a
		ld hl,0
		ld de,$2000
		ld bc,$2000
		ldir
		ret

; ---------------------------------------------------------------------
; The runtime jumps here (through fw_resume) when BREAK ends a game. MMU 7
; is still the runtime's page; the stack is the runtime's.
_nm_resume:
		di
		ld sp,NM_STACK_TOP
		nextreg $56,0
		nextreg $57,1
		jp _nm_run

; ---------------------------------------------------------------------
; void nm_basic(void): leave for NextZXOS. Runs the BASIC command NEW through
; IDE_BASIC, which starts NextZXOS's BASIC again and never returns here.
; Needs the BASIC memory layout: ROM 3, RAM 5, 2 and 0, ERR_NR clear, and a
; stack between STKEND and RAMTOP. If the call does return, it soft-resets.
_nm_basic:
		di
		ld hl,($5CB2)		; RAMTOP
		ld sp,hl
		ld iy,$5C3A
		ld (iy+0),$FF
		nextreg $56,0
		nextreg $57,1
		ld hl,basic_new
		ld de,0
		ld bc,0
		xor a
		exx
		ld de,$01C0		; IDE_BASIC
		ld c,0			; RAM 0 at $C000
		rst 8
		db M_P3DOS
		nextreg $02,1		; soft reset
		jr $

basic_new:	db $E6,$0D		; NEW, ENTER

		section bss_user
p3_mmu:		defs 2
p3_hl:		defs 2
p3_de:		defs 2
p3_bc:		defs 2
p3_af:		defs 2
