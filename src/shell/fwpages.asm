; fwpages.asm: the runtime's three pages, as built by src/runtime, put into
; the NEX file in the banks the memory plan names. The runtime is assembled
; for its own addresses, so these sections only carry the bytes; they are
; never run from the addresses the linker gives them.
;
;   bank 12, low half   page 24 (FW_PAGE)    the runtime, run at $E000
;   bank 12, high half  page 25 (FW2_PAGE)   run at $2000
;   bank 50, low half   page 100 (FW3_PAGE)  run at $0000

		section BANK_12_L
		binary "runtime_fw.bin"

		section BANK_12_H
		binary "runtime_fw2.bin"

		section BANK_50_L
		binary "runtime_fw3.bin"
