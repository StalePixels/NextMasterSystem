# Shadow Dancer - The Secret of Shinobi (Europe, Brazil) (En), CRC32 3793C01A, 512K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with no reference I/O log: the SMS
# reference (MAME sg1000m3, a Mark III with no BIOS) never shows a picture of this cart.
# Decisions:
# - Page 0 replaces the game's tile unpacker, which writes VRAM one byte at a time
#   (a control write through RST $20, then one data write): vsync is the whole unpack
#   at $785C (screen and stage loads), vstream the main loop's background form at
#   $7900 (at most 255 bytes a pass, in play). Each byte cost three traps; jt_vwrite
#   writes the same bytes, and the first stage starts about 4 seconds sooner.
# - Page 0 also writes the whole name table of the door scenes ($17C2, every other
#   frame): through the traps it took more than a frame and slowed the doors down.
# - The play area has name table cells with the priority bit, so priority is on (about
#   1% of a frame more in play).
# - The CHECK rows of the draft are not patched. $77E0-$77F9 and $783A-$785B are
#   routines that nothing in the cart calls (verdict unused); the medium rows in banks
#   6 to 26 are data (verdict false); the low rows are data in banks that hold no
#   reached code.
name Shadow Dancer
cart 3793C01A
hz 50		; No-Intro regions Europe, Brazil
priority
# No free RST vector: $0000-$0002 (DI; IM 1) becomes the vector,
# the game starts at $0003 (the framework does DI and IM 2).
vector 00 io
start 0003
site 00021   ; OUT ($BF),A
site 00024   ; OUT ($BF),A
site 00039   ; IN A,($BF)
site 0009C   ; IN A,($BF)
site 0009E   ; IN A,($BF)
site 000AA   ; IN A,($BF)
site 000DF   ; OUT ($BE),A
site 002B4   ; OUT ($BF),A
site 002B8   ; OUT ($BF),A
site 002BC   ; OUT ($BF),A
site 002C0   ; OUT ($BF),A
site 002C4   ; OUT ($BF),A
site 002C8   ; OUT ($BF),A
site 0032B   ; OUT ($BF),A
site 0032F   ; OUT ($BF),A
site 00333   ; OUT ($BF),A
site 00337   ; OUT ($BF),A
site 0033B   ; OUT ($BF),A
site 0033F   ; OUT ($BF),A
site 00360   ; IN A,($DC)
site 0036C   ; IN A,($DD)
site 00373   ; IN A,($DC)
site 003D5   ; OUT ($BF),A
site 003D9   ; OUT ($BF),A
site 003DD   ; OUT ($BF),A
site 003E1   ; OUT ($BF),A
site 003E5   ; OUT ($BF),A
site 003E9   ; OUT ($BF),A
site 00586   ; OUT ($BF),A
site 0058A   ; OUT ($BF),A
site 0058E   ; OUT ($BF),A
site 00592   ; OUT ($BF),A
site 0083A   ; OUT (C),A
site 0083E   ; OUT (C),A
site 00845   ; OUT (C),A
site 00849   ; OUT (C),A
site 00871   ; OUTI
site 0088A   ; OUT ($BF),A
site 0088E   ; OUT ($BF),A
site 00993   ; OUT (C),A
site 00997   ; OUT (C),A
site 00A71   ; OUT ($BE),A
site 00A77   ; OUT ($BE),A
site 00B12   ; OUT ($BE),A
site 00B18   ; OUT ($BE),A
site 00C55   ; OUT ($BF),A
site 00C59   ; OUT ($BF),A
site 01193   ; OUT ($BE),A
site 01195   ; OUT ($BE),A
site 01197   ; OUT ($BE),A
site 01199   ; OUT ($BE),A
site 01468   ; OUT ($BF),A
site 0146F   ; OUT ($BF),A
site 0185E   ; OUT ($BF),A
site 01862   ; OUT ($BF),A
site 018AF   ; OUT ($BF),A
site 018B3   ; OUT ($BF),A
site 01B53   ; IN A,($BE)
site 01EDE   ; IN A,($DD)
site 01EEA   ; IN A,($DC)
site 02CA6   ; OUT ($BF),A
site 02CAA   ; OUT ($BF),A
site 02D60   ; OUTI
site 02D62   ; OUTI
site 02FEC   ; OUT ($BF),A
site 02FF0   ; OUT ($BF),A
site 03006   ; IN A,($BF)
site 0304C   ; OUT ($BE),A
site 03051   ; OUT ($BE),A
site 03088   ; OUT ($BE),A
site 037AE   ; OUT ($BE),A
site 037B5   ; OUT ($BE),A
site 038D1   ; OUT ($BE),A
site 038D6   ; OUT ($BE),A
site 0393E   ; IN A,($BE)
site 03955   ; IN A,($BE)
site 03A70   ; OUT ($BE),A
site 03A87   ; OUT ($BE),A
site 03B35   ; OUT ($BE),A
site 03B4F   ; OUT ($BF),A
site 03B53   ; OUT ($BF),A
site 03B58   ; OUT ($BF),A
site 03B5C   ; OUT ($BF),A
site 03B6D   ; OUT ($BE),A
site 03B74   ; OUT ($BE),A
site 03C5D   ; OUT ($BF),A
site 03C61   ; OUT ($BF),A
site 03C66   ; OUT ($BF),A
site 03C6A   ; OUT ($BF),A
site 03CD8   ; OUT ($BF),A
site 03CDC   ; OUT ($BF),A
site 0427C   ; OUT ($BF),A
site 04280   ; OUT ($BF),A
site 0429D   ; OUT ($BF),A
site 042A1   ; OUT ($BF),A
site 04448   ; IN A,($DC)
site 054BE   ; OUT ($BF),A
site 054C2   ; OUT ($BF),A
site 06667   ; OUT ($BF),A
site 0666B   ; OUT ($BF),A
site 0673E   ; OUT ($BF),A
site 06742   ; OUT ($BF),A
site 067D1   ; OUT ($BF),A
site 067D5   ; OUT ($BF),A
site 06916   ; OUT ($BF),A
site 0691A   ; OUT ($BF),A
site 0699A   ; OUT ($BE),A
site 069A0   ; OUT ($BE),A
site 06F08   ; OUT ($BE),A
site 06F0D   ; OUT ($BE),A
site 06FDC   ; OUT ($BE),A
site 0735F   ; OUT ($BE),A
site 07393   ; OUT ($BF),A
site 07397   ; OUT ($BF),A
site 073B3   ; OUT ($BF),A
site 073B7   ; OUT ($BF),A
otir 077A6   ; OUTI
site 077BA   ; OUT ($BE),A
site 077D4   ; OUT ($BE),A
site 077D8   ; OUT ($BE),A
site 07800   ; OUTI
site 07805   ; OUT ($BE),A
otir 0782C   ; OUTI
site 07884   ; OUT ($BE),A
site 07931   ; OUT ($BE),A
site 079EC   ; OUT ($BE),A
site 07B55   ; OUTI
site 07B57   ; OUTI
site 07B59   ; OUTI
site 07B5B   ; OUTI
site 07B5D   ; OUTI
site 07B5F   ; OUTI
site 07B61   ; OUTI
site 07B63   ; OUTI
site 07B65   ; OUTI
site 07B67   ; OUTI
site 07B69   ; OUTI
site 07B6B   ; OUTI
site 07B6D   ; OUTI
site 07B6F   ; OUTI
site 07B71   ; OUTI
site 07B73   ; OUTI
site 07B75   ; OUTI
site 07B77   ; OUTI
site 07B79   ; OUTI
site 07B7B   ; OUTI
site 07B7D   ; OUTI
site 07B7F   ; OUTI
site 07B81   ; OUTI
site 07B83   ; OUTI
site 07B85   ; OUTI
site 07B87   ; OUTI
site 07B89   ; OUTI
site 07B8B   ; OUTI
site 07B8D   ; OUTI
site 07B8F   ; OUTI
site 07B91   ; OUTI
site 07B93   ; OUTI
site 07B95   ; OUTI
site 07B97   ; OUTI
site 07B99   ; OUTI
site 07B9B   ; OUTI
site 07B9D   ; OUTI
site 07B9F   ; OUTI
site 07BA1   ; OUTI
site 07BA3   ; OUTI
site 07BA5   ; OUTI
site 07BA7   ; OUTI
site 07BA9   ; OUTI
site 07BAB   ; OUTI
site 07BAD   ; OUTI
site 07BAF   ; OUTI
site 07BB1   ; OUTI
site 07BB3   ; OUTI
site 07BB5   ; OUTI
site 07BB7   ; OUTI
site 07BB9   ; OUTI
site 07BBB   ; OUTI
site 07BBD   ; OUTI
site 07BBF   ; OUTI
site 07BC1   ; OUTI
site 07BC3   ; OUTI
site 07BC5   ; OUTI
site 07BC7   ; OUTI
site 07BC9   ; OUTI
site 07BCB   ; OUTI
site 07BCD   ; OUTI
site 07BCF   ; OUTI
site 07BD1   ; OUTI
site 07BD3   ; OUTI
site 07BD5   ; OUTI
site 07BD7   ; OUTI
site 07BD9   ; OUTI
site 07BDB   ; OUTI
site 07BDD   ; OUTI
site 07BDF   ; OUTI
site 07BE1   ; OUTI
site 07BE3   ; OUTI
site 07BE5   ; OUTI
site 07BE7   ; OUTI
site 07BE9   ; OUTI
site 07BEB   ; OUTI
site 07BED   ; OUTI
site 07BEF   ; OUTI
site 07BF1   ; OUTI
site 07BF3   ; OUTI
site 07BF5   ; OUTI
site 07BF7   ; OUTI
site 07BF9   ; OUTI
site 07BFB   ; OUTI
site 07BFD   ; OUTI
site 07BFF   ; OUTI
site 07C01   ; OUTI
site 07C03   ; OUTI
site 07C05   ; OUTI
site 07C07   ; OUTI
site 07C09   ; OUTI
site 07C0B   ; OUTI
site 07C0D   ; OUTI
site 07C0F   ; OUTI
site 07C11   ; OUTI
site 07C13   ; OUTI
site 07C15   ; OUTI
site 07C17   ; OUTI
site 07C19   ; OUTI
site 07C1B   ; OUTI
site 07C1D   ; OUTI
site 07C1F   ; OUTI
site 07C21   ; OUTI
site 07C23   ; OUTI
site 07C25   ; OUTI
site 07C27   ; OUTI
site 07C29   ; OUTI
site 07C2B   ; OUTI
site 07C2D   ; OUTI
site 07C2F   ; OUTI
site 07C31   ; OUTI
site 07C33   ; OUTI
site 07C35   ; OUTI
site 07C37   ; OUTI
site 07C39   ; OUTI
site 07C3B   ; OUTI
site 07C3D   ; OUTI
site 07C3F   ; OUTI
site 07C41   ; OUTI
site 07C43   ; OUTI
site 07C45   ; OUTI
site 07C47   ; OUTI
site 07C49   ; OUTI
site 07C4B   ; OUTI
site 07C4D   ; OUTI
site 07C4F   ; OUTI
site 07C51   ; OUTI
site 07C53   ; OUTI
site 07C55   ; OUTI
site 07C57   ; OUTI
site 07C59   ; OUTI
site 07C5B   ; OUTI
site 07C5D   ; OUTI
site 07C5F   ; OUTI
site 07C61   ; OUTI
site 07C63   ; OUTI
site 07C65   ; OUTI
site 07C67   ; OUTI
site 07C69   ; OUTI
site 07C6B   ; OUTI
site 07C6D   ; OUTI
site 07C6F   ; OUTI
site 07C71   ; OUTI
site 07C73   ; OUTI
site 07C75   ; OUTI
site 07C77   ; OUTI
site 07C79   ; OUTI
site 07C7B   ; OUTI
site 07C7D   ; OUTI
site 07C7F   ; OUTI
site 07C81   ; OUTI
site 07C83   ; OUTI
site 07C85   ; OUTI
site 07C87   ; OUTI
site 07C89   ; OUTI
site 07C8B   ; OUTI
site 07C8D   ; OUTI
site 07C8F   ; OUTI
site 07C91   ; OUTI
site 07C93   ; OUTI
site 07C95   ; OUTI
site 07C97   ; OUTI
site 07C99   ; OUTI
site 07C9B   ; OUTI
site 07C9D   ; OUTI
site 07C9F   ; OUTI
site 07CA1   ; OUTI
site 07CA3   ; OUTI
site 07CA5   ; OUTI
site 07CA7   ; OUTI
site 07CA9   ; OUTI
site 07CAB   ; OUTI
site 07CAD   ; OUTI
site 07CAF   ; OUTI
site 07CB1   ; OUTI
site 07CB3   ; OUTI
site 07CB5   ; OUTI
site 07CB7   ; OUTI
site 07CB9   ; OUTI
site 07CBB   ; OUTI
site 07CBD   ; OUTI
site 07CBF   ; OUTI
site 07CC1   ; OUTI
site 07CC3   ; OUTI
site 07CC5   ; OUTI
site 07CC7   ; OUTI
site 07CC9   ; OUTI
site 07CCB   ; OUTI
site 07CCD   ; OUTI
site 07CCF   ; OUTI
site 07CD1   ; OUTI
site 07CD3   ; OUTI
site 07CD5   ; OUTI
site 07CD7   ; OUTI
site 07CD9   ; OUTI
site 07CDB   ; OUTI
site 07CDD   ; OUTI
site 07CDF   ; OUTI
site 07CE1   ; OUTI
site 07CE3   ; OUTI
site 07CE5   ; OUTI
site 07CE7   ; OUTI
site 07CE9   ; OUTI
site 07CEB   ; OUTI
site 07CED   ; OUTI
site 07CEF   ; OUTI
site 07CF1   ; OUTI
site 07CF3   ; OUTI
site 07CF5   ; OUTI
site 07CF7   ; OUTI
site 07CF9   ; OUTI
site 07CFB   ; OUTI
site 07CFD   ; OUTI
site 07CFF   ; OUTI
site 07D01   ; OUTI
site 07D03   ; OUTI
site 07D05   ; OUTI
site 07D07   ; OUTI
site 07D09   ; OUTI
site 07D0B   ; OUTI
site 07D0D   ; OUTI
site 07D0F   ; OUTI
site 07D11   ; OUTI
site 07D13   ; OUTI
site 07D15   ; OUTI
site 07D17   ; OUTI
site 07D19   ; OUTI
site 07D1B   ; OUTI
site 07D1D   ; OUTI
site 07D1F   ; OUTI
site 07D21   ; OUTI
site 07D23   ; OUTI
site 07D25   ; OUTI
site 07D27   ; OUTI
site 07D29   ; OUTI
site 07D2B   ; OUTI
site 07D2D   ; OUTI
site 07D2F   ; OUTI
site 07D31   ; OUTI
site 07D33   ; OUTI
site 07D35   ; OUTI
site 07D37   ; OUTI
site 07D39   ; OUTI
site 07D3B   ; OUTI
site 07D3D   ; OUTI
site 07D3F   ; OUTI
site 07D41   ; OUTI
site 07D43   ; OUTI
site 07D45   ; OUTI
site 07D47   ; OUTI
site 07D49   ; OUTI
site 07D4B   ; OUTI
site 07D4D   ; OUTI
site 07D4F   ; OUTI
site 07D51   ; OUTI
site 07D53   ; OUTI
site 07D55   ; OUTI
site 07D57   ; OUTI
site 07D59   ; OUTI
site 07D5B   ; OUTI
site 07D5D   ; OUTI
site 07D5F   ; OUTI
site 07D61   ; OUTI
site 07D63   ; OUTI
site 07D65   ; OUTI
site 07D67   ; OUTI
site 07D69   ; OUTI
site 07D6B   ; OUTI
site 07D6D   ; OUTI
site 07D6F   ; OUTI
site 07D71   ; OUTI
site 07D73   ; OUTI
site 07D75   ; OUTI
site 07D77   ; OUTI
site 07D79   ; OUTI
site 07D7B   ; OUTI
site 07D7D   ; OUTI
site 07D7F   ; OUTI
site 07D81   ; OUTI
site 07D83   ; OUTI
site 07D85   ; OUTI
site 07D87   ; OUTI
site 07D89   ; OUTI
site 07D8B   ; OUTI
site 07D8D   ; OUTI
site 07D8F   ; OUTI
site 07D91   ; OUTI
site 07D93   ; OUTI
site 07D95   ; OUTI
site 07D97   ; OUTI
site 07D99   ; OUTI
site 07D9B   ; OUTI
site 07D9D   ; OUTI
site 07D9F   ; OUTI
site 07DA1   ; OUTI
site 07DA3   ; OUTI
site 07DA5   ; OUTI
site 07DA7   ; OUTI
site 07DA9   ; OUTI
site 07DAB   ; OUTI
site 07DAD   ; OUTI
site 07DAF   ; OUTI
site 07DB1   ; OUTI
site 07DB3   ; OUTI
site 07DB5   ; OUTI
site 07DB7   ; OUTI
site 07DB9   ; OUTI
site 07DBB   ; OUTI
site 07DBD   ; OUTI
site 07DBF   ; OUTI
site 07DC1   ; OUTI
site 07DC3   ; OUTI
site 07DC5   ; OUTI
site 07DC7   ; OUTI
site 07DC9   ; OUTI
site 07DCB   ; OUTI
site 07DCD   ; OUTI
site 07DCF   ; OUTI
site 07DD1   ; OUTI
site 07DD3   ; OUTI
site 07DD5   ; OUTI
site 07DD7   ; OUTI
site 07DD9   ; OUTI
site 07DDB   ; OUTI
site 07DDD   ; OUTI
site 07DDF   ; OUTI
site 07DE1   ; OUTI
site 07DE3   ; OUTI
site 07DE5   ; OUTI
site 07DE7   ; OUTI
site 07DE9   ; OUTI
site 07DEB   ; OUTI
site 07DED   ; OUTI
site 07DEF   ; OUTI
site 07DF1   ; OUTI
site 07DF3   ; OUTI
site 07DF5   ; OUTI
site 07DF7   ; OUTI
site 07DF9   ; OUTI
site 07DFB   ; OUTI
site 07DFD   ; OUTI
site 07DFF   ; OUTI
site 07E01   ; OUTI
site 07E03   ; OUTI
site 07E05   ; OUTI
site 07E07   ; OUTI
site 07E09   ; OUTI
site 07E0B   ; OUTI
site 07E0D   ; OUTI
site 07E0F   ; OUTI
site 07E11   ; OUTI
site 07E13   ; OUTI
site 07E15   ; OUTI
site 07E17   ; OUTI
site 07E19   ; OUTI
site 07E1B   ; OUTI
site 07E1D   ; OUTI
site 07E1F   ; OUTI
site 07E21   ; OUTI
site 07E23   ; OUTI
site 07E25   ; OUTI
site 07E27   ; OUTI
site 07E29   ; OUTI
site 07E2B   ; OUTI
site 07E2D   ; OUTI
site 07E2F   ; OUTI
site 07E31   ; OUTI
site 07E33   ; OUTI
site 07E35   ; OUTI
site 07E37   ; OUTI
site 07E39   ; OUTI
site 07E3B   ; OUTI
site 07E3D   ; OUTI
site 07E3F   ; OUTI
site 07E41   ; OUTI
site 07E43   ; OUTI
site 07E45   ; OUTI
site 07E47   ; OUTI
site 07E49   ; OUTI
site 07E4B   ; OUTI
site 07E4D   ; OUTI
site 07E4F   ; OUTI
site 07E51   ; OUTI
site 07E53   ; OUTI
site 07E55   ; OUTI
site 07E57   ; OUTI
site 07E59   ; OUTI
site 07E5B   ; OUTI
site 07E5D   ; OUTI
site 07E5F   ; OUTI
site 07E61   ; OUTI
site 07E63   ; OUTI
site 07E65   ; OUTI
site 07E67   ; OUTI
site 07E69   ; OUTI
site 07E6B   ; OUTI
site 07E6D   ; OUTI
site 07E6F   ; OUTI
site 07E71   ; OUTI
site 07E73   ; OUTI
site 07E75   ; OUTI
site 07E77   ; OUTI
site 07E79   ; OUTI
site 07E7B   ; OUTI
site 07E7D   ; OUTI
site 07E7F   ; OUTI
site 07E81   ; OUTI
site 07E83   ; OUTI
site 07E85   ; OUTI
site 07E87   ; OUTI
site 07E89   ; OUTI
site 07E8B   ; OUTI
site 07E8D   ; OUTI
site 07E8F   ; OUTI
site 07E91   ; OUTI
site 07E93   ; OUTI
site 07E95   ; OUTI
site 07E97   ; OUTI
site 07E99   ; OUTI
site 07E9B   ; OUTI
site 07E9D   ; OUTI
site 07E9F   ; OUTI
site 07EA1   ; OUTI
site 07EA3   ; OUTI
site 07EA5   ; OUTI
site 07EA7   ; OUTI
site 07EA9   ; OUTI
site 07EAB   ; OUTI
site 07EAD   ; OUTI
site 07EAF   ; OUTI
site 07EB1   ; OUTI
site 07EB3   ; OUTI
site 07EB5   ; OUTI
site 07EB7   ; OUTI
site 07EB9   ; OUTI
site 07EBB   ; OUTI
site 07EBD   ; OUTI
site 07EBF   ; OUTI
site 07EC1   ; OUTI
site 07EC3   ; OUTI
site 07EC5   ; OUTI
site 07EC7   ; OUTI
site 07EC9   ; OUTI
site 07ECB   ; OUTI
site 07ECD   ; OUTI
site 07ECF   ; OUTI
site 07ED1   ; OUTI
site 07ED3   ; OUTI
site 07ED5   ; OUTI
site 07ED7   ; OUTI
site 07ED9   ; OUTI
site 07EDB   ; OUTI
site 07EDD   ; OUTI
site 07EDF   ; OUTI
site 07EE1   ; OUTI
site 07EE3   ; OUTI
site 07EE5   ; OUTI
site 07EE7   ; OUTI
site 07EE9   ; OUTI
site 07EEB   ; OUTI
site 07EED   ; OUTI
site 07EEF   ; OUTI
site 07EF1   ; OUTI
site 07EF3   ; OUTI
site 07EF5   ; OUTI
site 07EF7   ; OUTI
site 07EF9   ; OUTI
site 07EFB   ; OUTI
site 07EFD   ; OUTI
site 07EFF   ; OUTI
site 07F01   ; OUTI
site 07F03   ; OUTI
site 07F05   ; OUTI
site 07F07   ; OUTI
site 07F09   ; OUTI
site 07F0B   ; OUTI
site 07F0D   ; OUTI
site 07F0F   ; OUTI
site 07F11   ; OUTI
site 07F13   ; OUTI
site 07F15   ; OUTI
site 07F17   ; OUTI
site 07F19   ; OUTI
site 07F1B   ; OUTI
site 07F1D   ; OUTI
site 07F1F   ; OUTI
site 07F21   ; OUTI
site 07F23   ; OUTI
site 07F25   ; OUTI
site 07F27   ; OUTI
site 07F29   ; OUTI
site 07F2B   ; OUTI
site 07F2D   ; OUTI
site 07F2F   ; OUTI
site 07F31   ; OUTI
site 07F33   ; OUTI
site 07F35   ; OUTI
site 07F37   ; OUTI
site 07F39   ; OUTI
site 07F3B   ; OUTI
site 07F3D   ; OUTI
site 07F3F   ; OUTI
site 07F41   ; OUTI
site 07F43   ; OUTI
site 07F45   ; OUTI
site 07F47   ; OUTI
site 07F49   ; OUTI
site 07F4B   ; OUTI
site 07F4D   ; OUTI
site 07F4F   ; OUTI
site 07F51   ; OUTI
site 07F53   ; OUTI
site 201B1   ; OUT ($7F),A
site 20299   ; OUT ($7F),A
site 2042B   ; OTIR
site 20541   ; OUT ($7F),A
site 2054B   ; OUT ($7F),A
site 20568   ; OUT ($7F),A
site 2066C   ; OUT ($7F),A
site 206FA   ; OUT ($7F),A
site 2077F   ; OUT ($06),A
site 207C9   ; OUT ($7F),A
site 207D2   ; OUT ($7F),A
site 207E2   ; OUT ($7F),A
site 20856   ; OUT ($7F),A
site 20C4A   ; OUT ($7F),A
site 20C4D   ; OUT ($F2),A
site 20C67   ; OUT ($7F),A
site 20C78   ; OUT ($F2),A
mapst 002F2   ; LD ($FFFF),A
mapst 002FB   ; LD ($FFFF),A
mapst 00318   ; LD ($FFFF),A
mapst 00320   ; LD ($FFFF),A
mapst 00485   ; LD ($FFFF),A
mapst 0048D   ; LD ($FFFF),A
mapst 004D3   ; LD ($FFFF),A
mapst 0059C   ; LD ($FFFF),A
mapst 005CE   ; LD ($FFFF),A
mapst 00629   ; LD ($FFFF),A
mapst 00660   ; LD ($FFFF),A
mapst 0074D   ; LD ($FFFF),A
mapst 0089B   ; LD ($FFFF),A
mapst 008B9   ; LD ($FFFF),A
mapst 008DC   ; LD ($FFFF),A
mapst 008F7   ; LD ($FFFF),A
mapst 00905   ; LD ($FFFF),A
mapst 00913   ; LD ($FFFF),A
mapst 00A43   ; LD ($FFFF),A
mapst 00A7C   ; LD ($FFFF),A
mapst 00AA0   ; LD ($FFFF),A
mapst 00AAA   ; LD ($FFFF),A
mapst 00ABF   ; LD ($FFFF),A
mapst 00ACB   ; LD ($FFFF),A
mapst 00AE1   ; LD ($FFFF),A
mapst 00B1D   ; LD ($FFFF),A
mapst 00B33   ; LD ($FFFF),A
mapst 00B47   ; LD ($FFFF),A
mapst 00B56   ; LD ($FFFF),A
mapst 00B66   ; LD ($FFFF),A
mapst 00B88   ; LD ($FFFF),A
mapst 00BD2   ; LD ($FFFF),A
mapst 00BD8   ; LD ($FFFF),A
mapst 00CD9   ; LD ($FFFF),A
mapst 00DBC   ; LD ($FFFF),A
mapst 00DCA   ; LD ($FFFF),A
mapst 00DD8   ; LD ($FFFF),A
mapst 00DE6   ; LD ($FFFF),A
mapst 00DF5   ; LD ($FFFF),A
mapst 00E04   ; LD ($FFFF),A
mapst 00E12   ; LD ($FFFF),A
mapst 00E20   ; LD ($FFFF),A
mapst 00E2F   ; LD ($FFFF),A
mapst 00E3D   ; LD ($FFFF),A
mapst 00E4B   ; LD ($FFFF),A
mapst 00E5A   ; LD ($FFFF),A
mapst 00E68   ; LD ($FFFF),A
mapst 00E76   ; LD ($FFFF),A
mapst 00E84   ; LD ($FFFF),A
mapst 00E92   ; LD ($FFFF),A
mapst 00EA1   ; LD ($FFFF),A
mapst 00EB0   ; LD ($FFFF),A
mapst 00EBE   ; LD ($FFFF),A
mapst 00ECC   ; LD ($FFFF),A
mapst 00EDA   ; LD ($FFFF),A
mapst 00EE8   ; LD ($FFFF),A
mapst 00EF7   ; LD ($FFFF),A
mapst 00F06   ; LD ($FFFF),A
mapst 00F1E   ; LD ($FFFF),A
mapst 00F2C   ; LD ($FFFF),A
mapst 00F3A   ; LD ($FFFF),A
mapst 00F49   ; LD ($FFFF),A
mapst 00F58   ; LD ($FFFF),A
mapst 00F67   ; LD ($FFFF),A
mapst 00F75   ; LD ($FFFF),A
mapst 014BA   ; LD ($FFFF),A
mapst 0156D   ; LD ($FFFF),A
mapst 0157B   ; LD ($FFFF),A
mapst 01629   ; LD ($FFFF),A
mapst 01637   ; LD ($FFFF),A
mapst 01645   ; LD ($FFFF),A
mapst 0168F   ; LD ($FFFF),A
mapst 0169D   ; LD ($FFFF),A
mapst 0177F   ; LD ($FFFF),A
mapst 0180F   ; LD ($FFFF),A
mapst 018C6   ; LD ($FFFF),A
mapst 018DA   ; LD ($FFFF),A
mapst 01901   ; LD ($FFFF),A
mapst 01915   ; LD ($FFFF),A
mapst 01934   ; LD ($FFFF),A
mapst 01942   ; LD ($FFFF),A
mapst 0194D   ; LD ($FFFF),A
mapst 01964   ; LD ($FFFF),A
mapst 01972   ; LD ($FFFF),A
mapst 019A1   ; LD ($FFFF),A
mapst 019AC   ; LD ($FFFF),A
mapst 019DB   ; LD ($FFFF),A
mapst 019E6   ; LD ($FFFF),A
mapst 019F4   ; LD ($FFFF),A
mapst 01A02   ; LD ($FFFF),A
mapst 01A1E   ; LD ($FFFF),A
mapst 01A53   ; LD ($FFFF),A
mapst 01A5E   ; LD ($FFFF),A
mapst 01A77   ; LD ($FFFF),A
mapst 01A82   ; LD ($FFFF),A
mapst 01AB7   ; LD ($FFFF),A
mapst 01AC2   ; LD ($FFFF),A
mapst 01AE9   ; LD ($FFFF),A
mapst 01AFC   ; LD ($FFFF),A
mapst 01B0A   ; LD ($FFFF),A
mapst 01B1A   ; LD ($FFFF),A
mapst 01B25   ; LD ($FFFF),A
mapst 01B3E   ; LD ($FFFF),A
mapst 01C2A   ; LD ($FFFF),A
mapst 01F03   ; LD ($FFFF),A
mapst 01F0C   ; LD ($FFFF),A
mapst 01F15   ; LD ($FFFF),A
mapst 01F47   ; LD ($FFFF),A
mapst 01F79   ; LD ($FFFF),A
mapst 01F9D   ; LD ($FFFF),A
mapst 02C1A   ; LD ($FFFF),A
mapst 02C75   ; LD ($FFFF),A
mapst 02CF3   ; LD ($FFFF),A
mapst 02D2D   ; LD ($FFFF),A
mapst 02D50   ; LD ($FFFF),A
mapst 02D86   ; LD ($FFFF),A
mapst 02DD5   ; LD ($FFFF),A
mapst 02E17   ; LD ($FFFF),A
mapst 02F30   ; LD ($FFFF),A
mapst 02F3E   ; LD ($FFFF),A
mapst 02FDA   ; LD ($FFFF),A
mapst 0301D   ; LD ($FFFF),A
mapst 03035   ; LD ($FFFF),A
mapst 0305E   ; LD ($FFFF),A
mapst 0364B   ; LD ($FFFF),A
mapst 03718   ; LD ($FFFF),A
mapst 0371F   ; LD ($FFFF),A
mapst 038C9   ; LD ($FFFF),A
mapst 038E4   ; LD ($FFFF),A
mapst 03B7E   ; LD ($FFFF),A
mapst 03B8C   ; LD ($FFFF),A
mapst 03BB4   ; LD ($FFFF),A
mapst 03BBB   ; LD ($FFFF),A
mapst 03C0F   ; LD ($FFFF),A
mapst 03C1E   ; LD ($FFFF),A
mapst 03C56   ; LD ($FFFF),A
mapst 03C94   ; LD ($FFFF),A
mapst 03CD1   ; LD ($FFFF),A
mapst 03D03   ; LD ($FFFF),A
mapst 0478E   ; LD ($FFFF),A
mapst 04872   ; LD ($FFFF),A
mapst 048A6   ; LD ($FFFF),A
mapst 049CF   ; LD ($FFFF),A
mapst 049D7   ; LD ($FFFF),A
mapst 04C26   ; LD ($FFFF),A
mapst 04C34   ; LD ($FFFF),A
mapst 05376   ; LD ($FFFF),A
mapst 0540A   ; LD ($FFFF),A
mapst 05421   ; LD ($FFFF),A
mapst 05446   ; LD ($FFFF),A
mapst 05488   ; LD ($FFFF),A
mapst 054C6   ; LD ($FFFF),A
mapst 05774   ; LD ($FFFF),A
mapst 05782   ; LD ($FFFF),A
mapst 05788   ; LD ($FFFF),A
mapst 05798   ; LD ($FFFF),A
mapst 057BB   ; LD ($FFFF),A
mapst 05815   ; LD ($FFFF),A
mapst 05A89   ; LD ($FFFF),A
mapst 05AA2   ; LD ($FFFF),A
mapst 05B3B   ; LD ($FFFF),A
mapst 05B78   ; LD ($FFFF),A
mapst 05C10   ; LD ($FFFF),A
mapst 05C2C   ; LD ($FFFF),A
mapst 05ECD   ; LD ($FFFF),A
mapst 05F26   ; LD ($FFFF),A
mapst 05F2C   ; LD ($FFFF),A
mapst 05F55   ; LD ($FFFF),A
mapst 06081   ; LD ($FFFF),A
mapst 06091   ; LD ($FFFF),A
mapst 0619E   ; LD ($FFFF),A
mapst 061AE   ; LD ($FFFF),A
mapst 06322   ; LD ($FFFF),A
mapst 06335   ; LD ($FFFF),A
mapst 0633E   ; LD ($FFFF),A
mapst 063EA   ; LD ($FFFF),A
mapst 06412   ; LD ($FFFF),A
mapst 0642A   ; LD ($FFFF),A
mapst 06452   ; LD ($FFFF),A
mapst 064CA   ; LD ($FFFF),A
mapst 064FF   ; LD ($FFFF),A
mapst 06585   ; LD ($FFFF),A
mapst 065C3   ; LD ($FFFF),A
mapst 065F2   ; LD ($FFFF),A
mapst 06602   ; LD ($FFFF),A
mapst 06610   ; LD ($FFFF),A
mapst 06620   ; LD ($FFFF),A
mapst 0666F   ; LD ($FFFF),A
mapst 06747   ; LD ($FFFF),A
mapst 0685E   ; LD ($FFFF),A
mapst 068C2   ; LD ($FFFF),A
mapst 068D6   ; LD ($FFFF),A
mapst 0691E   ; LD ($FFFF),A
mapst 06C95   ; LD ($FFFF),A
mapst 06CAA   ; LD ($FFFF),A
mapst 06EB2   ; LD ($FFFF),A
mapst 06EC0   ; LD ($FFFF),A
mapst 06FD4   ; LD ($FFFF),A
mapst 06FE5   ; LD ($FFFF),A
mapst 06FF4   ; LD ($FFFF),A
mapst 07015   ; LD ($FFFF),A
mapst 07065   ; LD ($FFFF),A
mapst 07087   ; LD ($FFFF),A
mapst 07097   ; LD ($FFFF),A
mapst 070A5   ; LD ($FFFF),A
mapst 070D4   ; LD ($FFFF),A
mapst 070F8   ; LD ($FFFF),A
mapst 0710E   ; LD ($FFFF),A
mapst 07171   ; LD ($FFFF),A
mapst 0717F   ; LD ($FFFF),A
mapst 07258   ; LD ($FFFF),A
mapst 0728F   ; LD ($FFFF),A
mapst 07294   ; LD ($FFFF),A
mapst 072C1   ; LD ($FFFF),A
mapst 072DE   ; LD ($FFFF),A
mapst 072F9   ; LD ($FFFF),A
mapst 073C3   ; LD ($FFFF),A
mapst 073E7   ; LD ($FFFF),A
mapst 07431   ; LD ($FFFF),A
mapst 07499   ; LD ($FFFF),A
mapst 076A3   ; LD ($FFFF),A
mapst 076B4   ; LD ($FFFF),A
mapst 076C5   ; LD ($FFFF),A
mapst 076D6   ; LD ($FFFF),A
mapst 076E7   ; LD ($FFFF),A
mapst 076F8   ; LD ($FFFF),A
mapst 07709   ; LD ($FFFF),A
mapst 0771A   ; LD ($FFFF),A
mapst 0772B   ; LD ($FFFF),A
mapst 0773C   ; LD ($FFFF),A
mapst 07754   ; LD ($FFFF),A
mapst 0775C   ; LD ($FFFF),A
mapst 07762   ; LD ($FFFF),A
mapst 0777C   ; LD ($FFFF),A
mapst 07793   ; LD ($FFFF),A
mapst 078E0   ; LD ($FFFF),A
mapst 07908   ; LD ($FFFF),A
mapst 079C3   ; LD ($FFFF),A
mapst 079D2   ; LD ($FFFF),A
mapst 07A5A   ; LD ($FFFF),A
mapst 07A7D   ; LD ($FFFF),A
mapst 07AE4   ; LD ($FFFF),A
# Mapper stores found by the byte scan in bytes no path reached:
mapst 00085   # LD ($FFFF),A; after LD A,$08; 32 bytes of valid code before it
mapst 0008D   # LD ($FFFF),A; after LD A,$02; JP/CALL target from $0A145 $63382; 32 bytes of valid code before it
asm 0785C 6   ; tile unpack to VRAM: LD A,(HL); INC HL; EXX; LD E,A; LD D,0
    rst $00
    db far_io, pg_vsync, ent_vsync
    ret
endasm
asm 0790B 6   ; tile stream, after the source bank is mapped: LD A,$FF; EX AF,AF'; LD HL,($C06A)
    rst $00
    db far_io, pg_vstream, ent_vstream
    ret
    nop
endasm
asm 017C2 27  ; door scenes, every other frame: the name table from $CF00, CRAM between
    rst $00
    db far_io, pg_ntrows04, ent_ntrows04
    call $7974                  ; the game's CRAM write, as at $17CF
    rst $00
    db far_io, pg_ntrows523, ent_ntrows523
    jp $02E4
endasm
page 0 vsync vstream ntrows04 ntrows523
; Both entries replace the game's tile unpacker, which writes VRAM one byte at a time:
; a control write of the address through RST $20, then one data write. A stream is a
; step byte s (vsync only), then s passes. Pass k writes from VRAM address A + k
; onwards, s bytes apart. A pass is packets, ended by a 0 byte: a count byte n (bit 7
; set: n & $7F bytes follow; clear: one byte follows, written n & $7F times; a count
; of 0 is 256). Here each packet is one jt_vwrite per 16 bytes (a run of 1 byte, the
; VRAM step s), with interrupts as at the call between them. The game reads the
; stream from the bank it mapped at $8000, so it is read as the game sees it.
;
; vsync: as the game's $785C-$7872. HL = the stream, DE = the VRAM address (bit 6 of D
; set). Returns HL past the stream, DE = the address + s, B = 0, A = 0, Z; C and
; IX, IY kept. The game's code also changes DE' and HL'.
vsync:  ld (sv_ix),ix
        ld (sv_iy),iy
        xor a
        ld (limit),a
        call jt_peek
        inc hl
        ld (step),a
        ld b,a                  ; passes, 0 is 256
.pass:  push bc
        push de
        ld (vaddr),de
        call pkts               ; HL past the pass's 0 byte
        pop de
        inc de
        pop bc
        djnz .pass
        jp out0

; vstream: as the game's $790B-$7973, the background form that the main loop runs
; once a pass ($043C, $1EAE), at most 255 bytes a call. Its state: $C064 (not 0:
; work to do), $C065 (s), $C067 (the pass), $C068 (the pass's first address),
; $C06A (the next address), $C06C (the next count byte), $C06E (the bank). At the
; first packet that does not fit in what is left of the 255, it saves $C06C and
; $C06A and returns. Changes A, BC, DE, HL, F, as the game's code does (it also
; changes AF', DE', HL'); keeps IX and IY.
vstream:
        ld (sv_ix),ix
        ld (sv_iy),iy
        ld a,$FF
        ld (budget),a
        ld (limit),a
        ld a,($C065)
        ld (step),a             ; $C066 is always 0
.pass:  ld hl,($C06A)
        ld (vaddr),hl
        ld hl,($C06C)
        call pkts
        jr c,.full
        ld a,($C065)            ; the game's $7949
        ld d,a
        ld a,($C067)
        inc a
        cp d
        jr nc,.done
        ld ($C067),a
        ld ($C06C),hl
        ld hl,($C068)
        inc hl
        ld ($C068),hl
        ld ($C06A),hl
        jr .pass
.done:  xor a
        ld ($C064),a
        jr out0
.full:  ld ($C06C),hl           ; the game's $796C
        ld de,(vaddr)
        ld ($C06A),de
; ntrows04, ntrows523: as the game's $17C2-$17CB and $17D2-$17DA in the frame handler
; of the door scenes, run when bit 3 of $C0D1 is clear. The game writes name table rows
; 0-4 from $CF00 (the OUTI run at $7CD5), its CRAM ($7974), then rows 5-23 from $D040
; ($7B4B with BC = $02C0: the OUTI run $7B55-$7F54, then 704 bytes through $779C), every
; byte through the traps: 1536 bytes, more than a frame. Here each part is one jt_vwrite
; call of whole rows (runs of 64 bytes) in the game's order: the writes run past the
; vertical blank, and the picture must show whole rows, old or new. The VDP is
; left as the game's writes leave it: the address after row 4 or row 23, the last byte
; in the read buffer. Keeps IX and IY; the game's code after it ($02E4) needs no other
; register.
ntrows04:
        ld hl,$CF00
        ld de,$3800
        ld c,5
        jr ntrows
ntrows523:
        ld hl,$D040
        ld de,$3940
        ld c,19
ntrows: ld (sv_ix),ix
        ld (sv_iy),iy
        ld ix,64
        ld iy,64
        ld b,64                 ; whole rows, C of them, in the game's order
        xor a                   ; the source as the game sees it
        call jt_vwrite
out0:   ld ix,(sv_ix)
        ld iy,(sv_iy)
        xor a
        ret

; pkts: one pass from HL to VRAM (vaddr), step (step). Returns NC with HL past the
; pass's 0 byte, or, with limit not 0, C with HL on the first count byte that is
; more than budget. Changes A, BC, DE, IX, IY, F.
pkts:   call jt_peek
        or a
        jr z,.end
        ld c,a                  ; bit 7: the bytes follow
        and $7F
        ld b,a                  ; count, 0 is 256
        ld a,(limit)
        or a
        jr z,.go
        ld a,(budget)
        sub b
        ret c
        ld (budget),a
.go:    inc hl
        ld ix,0
        bit 7,c
        jr z,.one
        inc ix                  ; the source steps 1 a byte
.one:   ld iy,(step)            ; s and the 0 after it, as a word
        ld a,b
        ld (left),a
.chunk: ld a,(left)
        ld c,16
        or a
        jr z,.big
        cp c
        jr nc,.big
        ld c,a                  ; the last chunk, under 16 bytes
.big:   ld de,(vaddr)
        ld b,1
        xor a                   ; the source as the game sees it
        call jt_vwrite
        ld a,c                  ; vaddr += c * s, in 16 bits as the game adds it
        push hl
        ld hl,(step)
        ex de,hl
.adv:   add hl,de
        dec a
        jr nz,.adv
        ld (vaddr),hl
        pop hl
        ld a,ixl
        or a
        jr z,.same
        ld a,c                  ; the source moves on c bytes
        add a,l
        ld l,a
        adc a,h
        sub l
        ld h,a
.same:  ld a,(left)
        sub c
        ld (left),a
        jr nz,.chunk
        ld a,ixl
        or a
        jr nz,pkts              ; HL is past the bytes
        inc hl                  ; past the one byte
        jr pkts
.end:   inc hl
        or a                    ; NC
        ret

sv_ix:  dw 0
sv_iy:  dw 0
vaddr:  dw 0
step:   db 0, 0                 ; s, then 0: read as a word
budget: db 0
limit:  db 0
left:   db 0
endpage

# Shadow Dancer (Europe) (Action Replay).cht, "Infinite Lives"
poke "Infinite lives"
ar 00C0-5909
endpoke

# Shadow Dancer (Europe) (Action Replay).cht, "Unlimited Special Attacks"
poke "Infinite special attacks"
ar 00C0-5A03
endpoke

# Shadow Dancer - The Secret of Shinobi _ Shadow Dancer (Europe, Brazil).cht, "Invincibility"
# (one cheat field of 17 parts; all 17 are tested together)
poke "Invincibility"
gg C32-6FA-E61
gg C3A-75A-E61
gg C31-EA9-E61
gg C95-D3C-A29
gg C95-ACC-A29
gg C92-CDA-A29
gg C9B-2CB-082
gg C92-82A-A29
gg 4BC-49B-4CB
gg C97-07A-809
gg C90-B0A-809
gg C9A-7DA-A29
gg C9F-ABB-A29
gg C9E-33A-809
gg C9E-72A-A29
gg C93-CC9-809
gg 001-379-F7E
endpoke
