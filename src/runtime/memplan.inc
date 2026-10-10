; memplan.inc: the memory plan, in 8K pages. The outer shell reads the same
; numbers through build/memplan.h, which the Makefile generates from this file.
; Keep one definition per line in the form  NAME equ VALUE.

TILE_PAGE	equ 10			; bank 5: Next tile definitions (NextZXOS's, saved)
MAP_PAGE	equ 14			; bank 7 low: Next tilemaps (NextZXOS's, saved)
FW_PAGE		equ 24			; bank 12 low: framework at $E000
FW2_PAGE	equ 25			; bank 12 high: framework part 2 at $2000
SMSRAM_PAGE	equ 26			; SMS RAM at $C000
SAVE7_PAGE	equ 27			; copy of page 14 while a game runs
SHADOW_PAGE	equ 28			; 16K SMS VRAM copy (pages 28, 29)
SAVE5_PAGE	equ 30			; copy of pages 10, 11 while a game runs
CART_PAGE	equ 32			; cart copy from page 32 up
CARTRAM_PAGE	equ 96			; cart RAM ($FFFC bit 3), 2 x 16K (pages 96-99)
FW3_PAGE	equ 100			; bank 50 low: framework part 3 at $0000 (vblank work only)
FW4_PAGE	equ 101			; bank 50 high: framework part 4 at $2000 (start, quit, trace builder)
L2_PAGE		equ 102			; Layer 2 for priority tiles: 16K banks 51-53 (pages 102-107)
L2_BANK		equ L2_PAGE/2
L2W_PAGE	equ 192			; Layer 2 320x256 for priority tiles in 224-line mode: 16K banks 96-100 (pages 192-201)
L2W_BANK	equ L2W_PAGE/2
L2_TRANS	equ $24			; global transparent colour: R 1 G 1, which no SMS colour makes
MAX_PAGES	equ 64			; 512K (pages 32-95)
CODE_PAGE	equ 116			; overlay code pages (PAGE chunks): page number n in RAM page CODE_PAGE+n
CODE_MAX	equ 8			; at most 8 code pages (pages 116-123)
CODE_ENTS	equ 64			; at most 64 entries over all code pages
TRC_PAGE	equ 124			; the trace cache (trace.asm), mapped at $0000 while it is used
TKC_PAGE	equ 125			; tiles from cart ROM: kn_pages and the tk_ tables (fw2 kn_block)
CONVT_PAGE	equ 128			; the cart converted to Next tile rows, page n in CONVT_PAGE+n (128-191)
