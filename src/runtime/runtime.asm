; runtime.asm: the three runtime pages, assembled as sections of one module
; so they share symbols. Each section is written to its own file by
; z80asm -split-bin: fw (page at $E000), fw2 (page at $2000), fw3 (page at
; $0000). Each section is padded to one 8K page. See docs/design.md.

		include "memplan.inc"

		section fw
		org $E000
		include "fw.asm"
		defs 0x2000-$		; pad to one 8K page (an overflow is an assembler error)

		section fw2
		org $2000
		include "fw2.asm"
		defs 0x2000-$		; pad to one 8K page (an overflow is an assembler error)

		section fw3
		org $0000
		include "fw3.asm"
		defs 0x2000-$		; pad to one 8K page (an overflow is an assembler error)
