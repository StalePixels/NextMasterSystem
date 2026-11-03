; bootpages.asm: the boot pages, as the Makefile writes them under build/boot/,
; put into the NEX file in the banks the memory plan names (BOOT_PAGE,
; BOOT_OVL_PAGE in src/runtime/memplan.inc). The shell reads them as files
; (nm_mopen in os.c); they are never run from the addresses the linker gives
; them.
;
;   bank 101, low half   page 202   the cart image, bytes $0000-$1FFF
;   bank 101, high half  page 203   bytes $2000-$3FFF
;   bank 102, low half   page 204   bytes $4000-$5FFF
;   bank 102, high half  page 205   bytes $6000-$7FFF
;   bank 103, low half   page 206   the overlay file

		section BANK_101_L
		binary "boot/cart0.bin"

		section BANK_101_H
		binary "boot/cart1.bin"

		section BANK_102_L
		binary "boot/cart2.bin"

		section BANK_102_H
		binary "boot/cart3.bin"

		section BANK_103_L
		binary "boot/ovl.bin"
