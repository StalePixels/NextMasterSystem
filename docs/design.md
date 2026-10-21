# NextMasterSystem design notes

NextMasterSystem runs Sega Master System games on the ZX Spectrum Next. The program is one NEX file, `nms.nex`. It has two parts.

- The **outer shell** is C. It shows the NextZXOS file browser, reads the cart, finds the game's overlay, applies it, shows an information screen about the game, and starts the game. When the player presses BREAK in a game, control returns to the shell, and the browser opens again. BREAK in the browser leaves NextMasterSystem for NextZXOS. A future graphical interface will be added to the shell.
- The **runtime** is Z80 assembly. It runs while a game runs. It receives every I/O instruction the game makes. It drives the Next's tilemap, sprites, copper and sound chips. The build assembles the runtime separately, and puts it into the NEX as four ready-made 8K pages.

This file describes the layout of both parts. It also covers how the shell is split over banked memory, and how to extend it.

## Memory map

The Next has 8K pages. The CPU sees eight of them at a time, one in each 8K slot of the 64K address space. NextRegs `$50` to `$57` choose the page for each slot. These are MMU0 to MMU7.

### While the shell runs

| Address | Slot | Content |
|---|---|---|
| `$0000` to `$3FFF` | 0, 1 | NextZXOS ROM. The shell never changes it. |
| `$4000` to `$7FFF` | 2, 3 | NextZXOS bank 5: screen and system variables. The shell writes here only on the information screen, and only to the ULA screen from `$4000` to `$5AFF`. |
| `$8000` to `$9FFF` | 4 | Resident part: C start-up code, `main`, far-call code, operating system glue, shared state, library routines. |
| `$A000` to `$A0FF` | 5 | `OVL_BUF`: the loader reads the overlay index and the overlay file through these 256 bytes (`OVL_BUFSIZE`). |
| `$A100` to `$BDFF` | 5 | Free. |
| `$BE00` to `$BFDF` | 5 | Stack. It grows down from `$BFE0`. |
| `$C000` to `$DFFF` | 6 | A data window. The loader maps the cart's RAM pages here one at a time. |
| `$E000` to `$FFFF` | 7 | The **banked code window**. A far call (`nm_far`) maps a module's page here. |

Slots 4 and 5 are NEX bank 2. They are always mapped. Everything the shell hands to the operating system lives there. See "Pointers given to the operating system" below.

The Makefile passes `--main-fence 0xA000` to the linker. The build fails if code, data or BSS of the resident part grows past `$A000`. `OVL_BUF` starts at `$A000`.

### Pages

Page numbers are 8K pages. A NEX bank is two pages. So bank `n` is pages `2n` and `2n+1`. `src/runtime/memplan.inc` is the authoritative list of the runtime's pages. The Makefile turns it into `build/memplan.h` for the C code. In short:

| Pages | Use |
|---|---|
| 10, 11, 14 | NextZXOS's tile definitions and tilemaps, in banks 5 and 7. The runtime borrows them while a game runs and keeps copies in pages 27, 30 and 31. |
| 24, 25 | Runtime, parts 1 and 2, in bank 12. Part 1 runs at `$E000`, part 2 at `$2000`. |
| 26, 28, 29 | SMS RAM and the 16K VRAM copy. |
| 32 and up | The cart, up to 512K. |
| 96 to 99 | Cart RAM. |
| 100, 101 | Runtime parts 3 and 4, in bank 50. Part 3 runs at `$0000` during the once-a-frame work only, part 4 at `$2000`. |
| 102 to 107 | Layer 2, used for priority tiles in 192-line mode (256x192). |
| 108 to 115 | The shell's banked C modules, in banks 54 to 57. |
| 116 to 123 | The overlay's code pages: page number n of the file in page 116 + n. |
| 124 | The trace cache. |
| 125 | The tile cache (`tilecache`): the `kn_pages` marks and, per tile, where its converted copy is. |
| 126, 127 | Free. |
| 128 to 191 | The converted cart (the tile cache): cart page n, converted to Next tile rows, in page 128 + n. |
| 192 to 201 | Layer 2 for priority tiles in 224-line mode (320x256). |
| 202 to 223 | Free. |

The NEX file asks for the 2 MB memory flag, because pages above 95 are used.

### While a game runs

The runtime owns the machine. `jp` to `$E00C` starts it. The jump table at `$E000` is the overlay ABI. Its entries never move. `FW_ABI` in `src/runtime/fw.asm` is its version. The state variables at `$E020` to `$E071` are at fixed addresses too. The table's second part follows them at `$E072`: `jt_far`, the far call into a code page, and `jt_peek`, which reads a byte as the game sees it (ABI 6), then `jt_vwrite`, which writes a block of bytes into VRAM for page code (ABI 7). Existing overlays depend on all of these.

A far call (`jt_far`) maps a code page at `$2000-$3FFF` (MMU1), where the runtime's parts 2 and 4 are mapped only while they run. While a page entry runs, `cur_mmu+1` names the code page, so every routine that puts slot 1 back after it borrowed it puts the code page back. The game's interrupt handler never runs with a code page in its `$2000-$3FFF`. `far_find` points the two places where the runtime enters the game's `$0038` (`irq_t1` and `irq_t2` in part 1) at `pg_irq`, which calls `irq_slot1` in part 2. When `cur_mmu+1` names a code page, `irq_slot1` maps the game's page under it (`pg_under`) for the handler and puts `pg_tramp` (part 1) in the handler's return slot; `pg_tramp` maps the code page back and goes on to the interrupted address. When no code page is in the window, `irq_slot1` points the two places back at `$0038`, so a game whose overlay has no code pages takes its interrupts with no extra work. The pause NMI (`fw_ula_irq`, which enters the game's `$0066`) calls `nmi_slot1` in part 2 each time: it does the same as `irq_slot1` for the NMI's return slot when a code page is in the window, and leaves `irq_t1` and `irq_t2` as they are. One `pg_tramp` return can wait at a time. If a frame or line event comes while the game's NMI handler runs, after the NMI took a code page out of the window, `irq_slot1` sees no code page and points `irq_t1` and `irq_t2` back at `$0038`; until the next far call, an interrupt in the rest of that page entry then finds the code page in the window. `far_find` in `fw2.asm` looks the entry up in `pg_tab`, the table of code pages in the runtime's part 2. [nms-format.md](nms-format.md) describes the far call and the rules for page code.

### The runtime's pages

The game owns `$0000-$DFFF`: its cart pages in slots 0 to 5 and the SMS RAM in slot 6. Only slot 7 is the runtime's for the whole game. The other three runtime pages borrow a slot of the game's for as long as they run.

| Page | Source | Mapped | Holds |
|---|---|---|---|
| 24, part 1 | `fw.asm`, `trace.asm` | `$E000`, always | the jump table and fixed state, every I/O handler entry and the hot handlers (VDP data and control, V counter, status, blocks, name table, `LD (DE),A` to the mapper), the interrupt entries, the trace run-time routines, the far call and `jt_vwrite`. Variables that only parts 2 and 3 use are in part 2, and those only part 4 uses are in part 4. Some code (`kn_entry`, `fw_quit`, the V counter's fast path `vc_fast`, `map_bank_fw2`) is in the rest of the page that holds `fw_stack`, up to the tables at `$E200` (`fw_gap_end`). The trace build's entries in `vdpcheck.asm` are at the end of the code. `$FB00-$FFFF` hold the trace code area (from `$FBC0` in the trace build), the IM2 table, the trace output buffer and the mapper registers. |
| 25, part 2 | `fw2.asm` | `$2000`, by `fw2_call` from a handler, and during the once-a-frame work | the once-a-frame work's entry and its tile and sprite tables, the notes of tiles written whole from cart ROM (`kn_block`), VDP register writes and the display enable, mapper stores, CRAM extras (`toppal`, priority tiles), the transparent value and fallback colour, the priority tile redraw, the code page table, and from `$3C00` the overlay's `RASTER` routine or `RAMSITES` table. |
| 100, part 3 | `fw3.asm` | `$0000`, during the once-a-frame work, in `tflush2` and `pic_ready`, and at game start | the copper lists (the per-line H scroll list of a `RASTER` overlay and the 224-line list too), keyboard, map rebuild, tile conversion, sprites, the transparent value scans, the runtime's start state (`fw2_state`) and the overlay switches (`fw2_switches`), both run by `fw2_start`. |
| 101, part 4 | `fw4.asm`, `trbuild.asm` | `$2000`, by `fw4_call` from a handler, by `fw_start` and `fw_quit`, by `jt_vwrite`, and by `cop_seg` in the once-a-frame work | game start (with the converted cart, `tc_build`, when `tilecache` is on) and quit, the NextReg values to restore on quit (`nr_keep`), the PSG, `LD A,I` (`ed_ldai4`), the trace builder with its instruction table, `jt_vwrite`'s one-byte form, the `collline` status read (`cl_read`, `cl_fresh`), the `rastseg` segment list (`cop_seg4`), the `workline` decisions (`wl_setup`, `wl_line4`, `wl_ula4`), and in the trace build the VDP check's work (`vdpcheck4.asm`). |

The rules that keep this working:

- Code in parts 2 and 4 never calls `fw2_call` or `fw4_call`, and never calls the other part: both use slot 1. The one place where part 4 runs in the once-a-frame work is `cop_seg` (part 3), which maps part 4 at `$2000` for `cop_seg4` and part 2 back after it. Both calls put slot 1 back to `cur_mmu+1`, which names the game's page there or the code page a far call mapped.
- Part 3 runs inside the once-a-frame work, with part 2 at `$2000`. The exceptions are `tflush2` and `pic_ready` in part 2, which a handler calls through `fw2_call` to convert tiles and, for `pic_ready`, to finish the picture before the display goes on: they map part 3, the VRAM copy and the tile definitions in the slots the once-a-frame work uses (`pic_ready` also slot 6), and put the game's pages back after; `fw2_start` at game start, which maps part 3 for `fw2_state`, `fw2_switches` and `fw2_init`; `hs_reg8` in part 2 (`hsplit`), which maps part 3 at `$0000` for `sg_write`; and `cl_fresh` in part 4 (`collline`), which maps part 3 at `$0000` and the VRAM copy at `$4000` for `cl_scan`. Each puts the game's pages back from `cur_mmu` after. Nothing else a handler runs may call part 3.
- A routine in part 1 that borrows slot 0 or slot 1 puts back the game's page, from `cur_mmu`. So code in part 3 (slot 0) does not call those routines, and code in parts 2 and 4 does not call the ones that borrow slot 1. `map_bank` maps slot 1 too when it maps the `$FFFD` bank into slots 0 and 1: part 2 jumps to it as its last step, or calls `map_bank_fw2`, which maps part 2 back at `$2000` after it.
- The trace builder (part 4) reads the game's code through `tr_rd` in part 1: for an address in `$2000-$3FFF` it maps the game's page for the read and part 4 back after it.
- The trace cache page is mapped at `$0000` only inside `tr_lookup` in part 1, and `tr_store` and `tr_reset` in part 4; each puts the game's page back from `cur_mmu` (`tr_reset` at game start leaves page `$FF`). The builder reads no game code while the cache page is mapped.
- The loader writes the NextReg values to restore on quit at `nr_saved` in part 1, and `fw4_start` copies them to `nr_keep` in part 4: `nr_saved` is the same memory as `vw_stack`.
- `jt_vwrite` (part 1) maps the source's page into slot 0, `MAP_PAGE` into slot 1 and the VRAM copy into slots 4 and 5 for the whole call, with interrupts off and its stack in part 1, and puts all four back from `cur_mmu` at the end. Its one-byte form (`vt_try`: runs of one byte, a source step of 0 or 1, the source inside one 8K page, tile data only) runs in part 4 with part 4 in slot 1 in place of `MAP_PAGE`; at the first byte outside the tiles it jumps to `vt_back` in part 1, which maps `MAP_PAGE` again and goes on with the general path.

The build checks each page's end (`tools/check-layout`). New handler code that must see the game's memory or borrow slot 1 goes in part 1. Code that needs only the runtime's state goes in part 2, or in part 4 if it does not need part 2. Part 1 has little room in either build: code added there needs code of the same size moved to another part, or, in the trace build, the trace code area started later.

Every instruction that leaves runtime code for game code (a `RET`, `RETI` or `JP` to the game) has a label that starts with `mx_`. `tools/mame/run.py --measure` puts its exit breakpoints on all of them, and its entry breakpoints on the handler entries, the interrupt entries, the far call and its return, `jt_vwrite`, `jt_peek`, `pg_irq`, `pg_tramp` and `isr_tramp`. A new way back to the game needs its `mx_` label, or the measure counts game time as runtime time.

### The once-a-frame work

`vbl_work` in `fw.asm` does the once-a-frame work: the copper list, the keyboard, the map rebuild, tile conversion, the transparent value scans, the priority tiles and the sprites (`fw2_vbl` in `fw2.asm`, with part 3 at `$0000`). It runs once in each frame, from one of three places:

- the ULA interrupt, at line 248 (line 224 at 60 Hz, see "The video rate" below);
- a V counter read (`rd_vcount`) in the vertical blank, for a game that waits for the picture with interrupts off. It sets `vbl_poll`, and the next ULA interrupt then does not run the work again. That interrupt may arrive late, at the game's `EI` in the picture.
- a handler's exit (`vbl_chk`) or the end of `jt_vwrite` (`vbl_chkv`) once the beam is past the ULA interrupt's line, for a game whose frame handler keeps interrupts off into the next picture. The ULA interrupt waits for the game's `EI` then, and the copper update's direct X scroll write would tear the picture at that line. It also sets `vbl_poll`.

The third place adds nothing to a handler until a game needs it. When the ULA interrupt comes in the picture, `fw_ula_irq` sets `vbl_arm` to 250. Each frame event on time (`fw_line_irq`) while `vbl_arm` is not 0 counts it down and writes a `JP vbl_chk` over the first 3 bytes of `fw_exit` and `vbl_chkv` into the call at `vw_tw`; `fw2_vbl` writes the original bytes back. So only the handlers between the frame event and the once-a-frame work pay for the check, about 140 cycles each, and only in the 5 seconds after the last ULA interrupt that came in the picture. Armed at the frame event, the check needs only the line's low byte: the ULA interrupt's line to 255, or below `pic_end` for lines 256 and later and for the next picture. Every game pays the check in the ULA interrupt (a line read) and the patch and its undo, about 270 cycles a frame.

Work that a handler does after a trap that crossed the ULA interrupt's line still delays the once-a-frame work: in Sonic, when the display goes on just before line 248, `tflush2` converts up to 50 lines of tiles before the work starts. The copper update after it must still end before line 0, where the copper starts the list again: a scroll that moves the map switch column rewrites one byte of each line (about 10 lines in all, see the copper list below).

The `workline` switch (`CONF` `workline=N`, `wl_n` in part 4) moves the work to a line interrupt at SMS line N of the picture. It is for a game whose frame handler must reach a line of the next picture on time: Fantastic Dizzy's split routine must read the status before line 30, 118 Next lines after the frame event, and the work at the ULA interrupt took up to about 150,000 cycles of that time. `wl_setup` in `fw4.asm` (from `fw4_start`) points four places elsewhere: `ula_hk` in `fw_ula_irq` calls `wl_ula` in place of `cur_line`; `fl_hk` in `fw_line_irq` calls `wl_line` in place of `LD A,(hl_on)`; and the `JR NZ` at `rv_hk` in `rd_vcount` and at `vf_hk` in `vc_fast` become `JR`, so a V counter read below the picture never runs the work. Both calls go to part 4 through `fw4_call`:

- `wl_ula4`, at the ULA interrupt, writes the Next line of SMS line N (N - 16 in 224-line mode) into NextReg `$23`, sets `wl_pend` to 1 and `vbl_poll` to 1, so the interrupt does no work. It returns A = 255, so `fw_ula_irq` does not arm `vbl_chk`. The work runs at once (`vbl_poll` 0), as without the switch, when a line event is set (`ev_next` below 192), when the interrupt came late into the picture past line N, and when `wl_pend` is still 1: the work line did not come since the last ULA interrupt (the game kept interrupts off past the frame event, or set a line event that took NextReg `$23`). It then puts `ev_next`'s event back into NextReg `$23`.
- `wl_line4`, at each line interrupt, tells the work line from the others: `wl_pend` 1, the beam in the picture and no SMS line event set. For the work line it sets `wl_pend` to 2, and `wl_line` goes on into `fw_ula_irq` with the registers as the line interrupt found them; there `wl_ula4` sees 2, puts the frame event back into NextReg `$23` and has the work run. For any other line interrupt it returns `hl_on` in A, and `fw_line_irq` goes on as without the switch.

Without the switch the four places keep their instructions, `wl_setup` only puts them back at game start, and every frame runs the same instructions as before. With it, the work runs in the picture: the sprites, the copper list and the converted tiles change at line N, and in 224-line mode `cop_224` writes the head with the H written last before line N and writes X and Y straight into the registers at that line. `tools/mame/run.py --measure` logs the work line as a `V` entry from `fw_ula_irq`; the few hundred cycles from `fw_line_irq` to there are not counted.

`vbl_done` stops a second V counter read in the same blank from running the work again. A V counter read in the picture clears it. The frame event and SMS line events clear it only when they come on time, because one held by the game's `DI` can come after a V counter read that already did the work.

The parts of the work that cost the most:

- **Tile conversion.** A VRAM write to tile data marks the tile in `dirty_pages`, and the once-a-frame work converts the marked tiles. Two cases convert them earlier, from the handler that writes: the display going on (see "Display off and on" below), and 512 bytes or more written to tiles since the last conversion (`tw_cnt`, `TW_MAX`). So a game that loads a level with interrupts off has its tiles converted while it loads, not all in its first vertical blank after. The 512-byte conversion (`tw_flush` in `fw2.asm`) waits while the display is off (register 1 bit 6 clear): it starts `tw_cnt` again and converts nothing, and the tiles are converted when the display goes on, or in the once-a-frame work. Games that load with the display off often write a tile in more than one pass, and a conversion between the passes would be done again. Name table rows 24-27, and rows 0-3 while the V scroll is 32, count as tile data as well as name table, because games keep tiles in the rows the picture does not show (OutRun keeps its HUD letters in rows 0-3). Rows 0-3 count only at V scroll 32, the one value that hides all of them; when they start to count, their 8 tiles are converted once.
- **The tile cache** (the `tilecache` switch, `fw_flags` bit 2): tiles that a block write takes whole from cart ROM are copied, not converted. At game start, `tc_build` in `fw4.asm` converts every 4 bytes of the cart, as one row of a tile, into the converted cart (`CONVT_PAGE`, page n of the cart in page 128 + n). It takes about 1.1 seconds for each 256K of cart. `fw2_switches` puts a call to `kn_entry` in `vram_block`'s last call (`kn_hk`, else `call tw_check`), and points the two calls of `tile_flush` (`tf_vbl` in the once-a-frame work, `tf_tw` in `tflush2`) at `tile_flushk`. After a block write (`vram_block`: OTIR, OUTI runs, the trace's blocks), `kn_entry` sends a block read from RAM or the trace buffer (source at `$C000` or above) to `tw_check`, and any other block to `kn_block` in `fw2.asm`, which does `tw_check`'s work at its end. `kn_note` takes each tile the block wrote whole from one cart page, with the source 4-byte aligned like the VRAM address. It sets the tile's `kn_pages` mark in place of its `dirty_pages` mark, and notes the converted page and address in `TKC_PAGE`. `tile_flushk` copies those 32 bytes from the converted cart. Any other write to the tile sets its `dirty_pages` mark, and a tile with that mark is converted from the VRAM copy, as before. `jt_vwrite` and single writes do not take this path. With the switch off, none of this runs: the block's end is `call tw_check` and the conversion is `tile_flush`, as without the feature.
- **The transparent value scan** (`pal_scan` in `fw3.asm`, every 8 frames). It collects the pixel values of the tiles that the name table shows with the sprite palette. Each tile is taken once a pass (`ps_seen`). `tm_mask` keeps the value set of each tile, 0 when not known; tile conversion clears the entries of the tiles it converts.
- **The copper list** (`cop_update` in `fw3.asm`). The Next map is 320 pixels wide and the SMS map 256, so for most H scroll values the list switches each line from map M0 to map A8 at a copper column, between SMS x 256 - K and 320 - K (K = -H), where both maps show the same pixels. `hscroll_set` in `fw2.asm` puts that column (`h_sw`, (291 - K) / 8) near the middle of the range. With K up to 64 no switch is needed, but the list has one all the same, at column 39 (SMS x 312, past the picture's right edge). So from one column to the next only the first byte of each line's WAIT changes, and `cop_switches` writes only that byte (about 10 lines in all). Both instructions of each line are written only at the game's first H write, when the list has no switch yet (`h_sw` 0). The list is rewritten while the copper waits at its end, in the vertical blank; the copper reads the list from the top again at line 0. The 224-line list (`cop_224`) works the same way: every one of its 224 lines has a switch pair (column 39 for K up to 64, and before the game's first H write), so it is written whole only when it is not yet the 224-line list (`cop_mode` 3: at the switch to 224-line mode, at game start, after a `RASTER` list). After that an H or V write rewrites the list's head (X and Y) and writes X and Y straight into the registers, and a new column rewrites only the first byte of each line's WAIT (about 80 cycles a line). `cop_sw` stays `$FF` in this mode, so every H write marks the list and the head follows it. A whole 224-line list costs about 64,000 cycles; the head alone, under 1,000 (measured in Fantastic Dizzy's play).
- **Mid-frame H scroll** (the `hsplit` switch, `fw_flags` bit 5). With line interrupts on, a register 8 write moves the tilemap at once (`hscroll_set`), but `cop_update` writes the map switch column only from the H the once-a-frame work sees. A game that sets H in a line event, for a status bar or for parallax bands, then shows the wrong map columns in a band on the right of the lines below the write, whenever its H needs another column than the frame's. With the switch, `fw2_switches` points three calls elsewhere: `r8_hk` in `vdp_reg_w` at `hs_reg8`, also in part 2, which calls `sg_write` in part 3 after `hscroll_set`; `vb_cop` in `fw2_vbl` at `sg_vbl`, which runs `sg_frame` before `rast_frame`; and `cf_hk` in `cop_update`'s whole rebuild at `sg_head`. The normal list is then a set of segments (`sg_tab`, at most `SG_MAX`): segment 0 from line 0, with column `cop_sw`, and one more from each line where a write in the picture came, with that write's column. A write rewrites the first byte of each line's WAIT (`cop_wlines`) from the beam's line down to the next segment, and only when its column changed or its line moved: the game's next write in the frame is expected at the next segment, as in the frame before. A write up to `SG_TOL` lines from a segment's line is that segment's split again. `sg_frame` merges each segment whose write did not come in the frame into the one above, so for one frame after a game stops a split the lines below it keep the old column. `cop_switches` rewrites only segment 0's lines (the sg_ routines keep segment 1's line in `cs_end`), and a whole rebuild starts again with one segment. A column change costs about 80 cycles for each line it rewrites: Asterix rewrites 160 lines from line 32 each time its play area's scroll crosses a column. Measured with `tools/mame/run.py --measure` over the same game frames, the runtime's share of a frame goes up by a median of 1,766 cycles in Asterix's play (one split a frame) and 4,383 in Choplifter's attract mode (six). Without the switch the three calls keep their targets, and the frame runs the same instructions as without the feature.
- **The per-line H scroll copper list** of a `RASTER` overlay (`cop_raster` in `fw3.asm`). The list has a fixed place for each line: a head of four instructions, then five instructions for each line, then `HALT`. The instructions of line y depend only on the H scroll of lines y and y+1. So from one frame to the next, only the lines next to an H scroll that changed are written again (`hl_prev` holds the H scroll of every line in the list). The list is written in full when the overlay's table becomes valid.
- **The segment list** of a `RASTER` overlay with the `rastseg` switch (`fw_flags` bit 7), in 224-line mode (`cop_seg` in `fw3.asm`, `cop_seg4` in `fw4.asm`). A per-line list for 224 lines would need about 1,125 of the copper's 1,024 instructions, so the routine gives segments, pairs of (first line, H), and the list is the 224-line list with an X for each segment: the head's X is that of the segment of line 16 (Next line 0); a segment that starts at another line has MOVE `$2F`, MOVE `$30` after the switch pair of the line above it, in that line's horizontal blank; and the X of the segment of line 0 follows the ULA-on pair at Next line 208, for the 16 lines above line 0 at the end of the list (it is also written straight into the registers when the beam is below the picture). Each line's switch pair has its segment's column. `fw2_switches` points `rf_new` and `rf_inc` in `rast_frame` at `seg_new` and `seg_inc`, which take `cop_seg` in 224-line mode and `cop_raster` in 192-line mode; without the switch they keep their targets. When the segments start at the same lines as those in the list (`cop_mode` 4), only the head and, for each segment whose H changed, its X and the first byte of each of its lines' WAIT are written, run by run; else the list is written whole. The segment tables are kept in `hl_prev`, and `cop_raster` writes the whole per-line list when it takes over from a segment list. `cop_seg` maps part 4 at `$2000` in place of part 2 for `cop_seg4`, which uses only part 1 and part 3; the once-a-frame work runs with interrupts off.

### The video rate

The overlay's `hz` switch (`CONF` `hz=50` or `hz=60`) is `fw_flags` bit 3, with bit 4 set for 60 Hz. `hz_setup` in `fw3.asm`, the last step of `fw2_switches` at game start, writes the rate into NextReg `$05` bit 2. Without the switch (`hz=any`) it leaves the register as the Next booted. The Next takes a new rate at its next frame and reads back the old one until then, so `hz_setup` works from the rate it wrote, not from a read.

`hz_setup` then sets the line numbers that depend on the rate:

| | 50 Hz | 60 Hz |
|---|---|---|
| lines in the Next's frame (128K timing) | 311, 567,264 cycles | 264, 481,536 cycles |
| ULA interrupt line (`vbl_due`'s compare) | 248 | 224 |
| V counter (`vc_count` in `fw.asm`, with the numbers `vc50` or `vc60` in `fw3.asm`) | PAL: `$00-$F2`, then `$BC-$FF` | NTSC: `$00-$DA`, then `$D5-$FF` |
| V counter in 224-line mode | PAL: `$00-$FF`, `$00-$02`, then `$CC-$FF` | NTSC: `$00-$EA`, then `$E5-$FF` |
| the 224-line copper list's lines above line 0 (`cop_top`): the last 16 lines of the frame | 295-310 | 248-263 |

The count reaches `$FF` on the Next's last line at both rates, for games that wait for it (Micro Machines). The 60 Hz frame has two lines more than the NTSC SMS, so the count stays at its first value after the jump back for three lines. In 224-line mode the count is the 192-line count plus 16, at both rates. `hz_setup` writes three numbers of the rate into `vc_count`: the first line past the count's top, the line that the lines up to it count as, and the jump back.

A game that reads the counter twice and compares the reads needs each read to be short: Canyon Racer waits for both reads of a pair to give `$C0`, so both must fall on line 192, which is 1,824 cycles long. `IN A,(n)` from the V counter (inline code `$0A` at `fw_io`, or a port of class 2 at `fw_in_n`) therefore goes first to `vc_fast`, between the first two instructions of `FASTENTRY` and the rest (`FE_REST`). For a line below the count's jump back that does not start the once-a-frame work, it reads the line with interrupts off, does `rd_vcount`'s frame bookkeeping (`vbl_done`, `fdone`) and returns the count to the game, without `FASTENTRY`, the port decode and `fw_exit`: about 530 cycles from entry to exit, against about 900 through `rd_vcount`. Any other read returns to the entry and goes through `rd_vcount`, and so does every read while `fw_exit` is patched (`vbl_chk`, `dis_chk`), which must see each trap.

The frame event (line 192, or 208 in 224-line mode) and the line events are at the same Next lines at both rates. Only the time after the picture changes: 72 lines at 60 Hz against 119 at 50 Hz.

The browser and the information screen always run at the rate the Next booted at. BREAK out of the game puts NextReg `$05` back, with the other NextRegs the shell saved at start, before the shell draws anything (see "Coming back").

The F3 key changes the rate while a game runs when NextReg `$06` bit 5 allows it. The runtime then keeps the line numbers of the rate it started with.

### Display off and on

Register 1 bit 6 is the SMS display enable. `r1_hw` in `fw2.asm` turns the Next's tilemap and sprites on or off with it (`disp_on`), and `l2_vis` Layer 2. Off, the picture shows the fallback colour, as the SMS shows its backdrop.

When the display goes on after the Next had it off (`vdp_reg_w__r1on`), `pic_ready` makes the picture whole before `r1_hw` turns the layers on: it converts the tiles written while the display was off, rebuilds the maps when the name table moved (`nt_dirty`), and draws Layer 2's priority cells (`pri_frame`: the marked cells and the cells of tiles converted again). A game that builds a screen with interrupts off gets no once-a-frame work before it turns the display on, and the Next would otherwise show, for a frame or more, parts of the screen it built with the display off. The display-on write waits for this work: after a screen change in Micro Machines, several frames.

With `toppal`, a display-off write between the frame event and the first line event (`pal_ph`) is held (`dis_pend`): on the SMS the frame handler turns the display on again before line 0, and on the slower Next that write can come in the picture. The Micro Machines race writes the display off at line 211 and on again up to 300 lines later. A held write applies:

- at the first line event in the picture (`pal_pic2`) or the next frame event (`pal_vbl2`), for a game that takes its interrupts;
- at a second display-off write while one is held, or a switch to or from 224-line mode (`mode_switch`): the game is building a screen, not finishing a frame;
- at the third run of the once-a-frame work with the write still held (`dis_count`), more than two frames after it;
- for a write held outside the game's frame handler, at the third frame that starts with the write still held while the game keeps interrupts off (`dis_tick2`). Such a game gets no frame event and no once-a-frame work. From the held write until it applies or a display-on write takes it back, `fw_exit` goes through `dis_chk` (`dis_arm`, `dis_patch`), and every 32nd trap (`DIS_N`) that returns to the game with its interrupts off reads the Next's line: a line lower than at the count before is a new frame. Micro Machines loads a race this way: its main code writes the display off just after the frame handler, while the hold is still open, and keeps interrupts off for about 50 frames. A write held inside the frame handler is not counted this way, as the handler turns the display on again or returns; the Micro Machines race would otherwise pay about 30 cycles a trap.

A display-on write takes the held write back. While a write is held the layers stay on, and a display-on write converts only the tiles (`tflush2`), as the picture never went off.

A register 2 write of the value the register already holds changes nothing (`vdp_reg_w__r2`): the maps already show the name table (`nt_put`), so there is no `map_rebuild` and no whole Layer 2 rebuild after it. Micro Machines writes it again before each race.

A whole rebuild of Layer 2 (`pri_rebuild`, `p2_rebuild`: at game start, a new name table base or a mode switch) can take frames: Micro Machines' 695 priority cells in 224-line mode take 8. Layer 2 is hidden until the rebuild ends (`pri_hide`, `pri_end`), and stays hidden then while a display-off write is held.

### CRAM writes

A data port write with VDP code 3 writes CRAM: `vdata_w` in `fw.asm` for a single write, `cram_block` for a block (OTIR, OUTI runs and the trace's blocks). Both do what the Master System does for any data write: they clear the latch, keep the byte in the read buffer (`vdp_rbuf`) and step the address. Then `cram_set` takes the colour, the byte's low 6 bits, for the entry that the address's low 5 bits name, and writes it into `cram` and into the first tilemap palette, and for entries 16-31 into the first sprite palette too (`pal_out`). With priority tiles or `toppal`, the `RET` at `cram_hk` is a `NOP`, and `cram_x` in `fw2.asm` runs: priority tiles write the first Layer 2 palette; `toppal` marks the entry in `pal_vm` in the vertical blank phase, and writes the second palettes and `cram_top` as `pal_vbl` describes. `cram_write` then runs `fallback2` (`fallback_update`); `cram_block` runs it once, after the whole block.

`fw4_start` sets the palettes black and zeroes `cram`, so `cram` holds what the palettes hold from the start, also for a game started after another one, and `fw2_start` runs `fallback2` once for that state. Page code that compares colours with `cram` (Fantastic Dizzy's `cram_upd`) depends on this.

### The VDP status

A status read (`rd_status` in `fw.asm`) returns the status byte `vdp_status` and clears bits 7 and 5 and the line interrupt flag, as on the Master System. Bit 7, the frame flag, is set by the frame event, and by a read below the picture for a game that polls with interrupts off. Bit 5, the sprite collision flag, is set once a frame by the sprite update in the once-a-frame work (`spr_coll` in `fw3.asm`), from the Next's own sprite collision flag (port `$303B`): after the picture, and only when the Next showed the sprites.

The `collline` switch (`fw_flags` bit 6) raises bit 5 at the line where the Master System raises it. `fw2_switches` points two calls elsewhere: `vb_spr` in `fw2_vbl` at `cl_vbl` and `rs_hk` in `rd_status` at `cl_rd`; without the switch both keep their targets (`spr_update` and `cur_line`). `cl_vbl` runs the sprite update and keeps the status bit 5 it had before (the Next's flag says nothing about the line). It then sets bit 5 if the picture just drawn had a collision line and no read in it raised the bit, arms `cl_arm` for the next picture, and runs `cl_scan`. `cl_scan` works out the first line where the boxes of two sprites meet, from the sprite table in the VRAM copy, as a Next line in `cl_line` (`$FF` for none; 16 lines lower in 224-line mode, and line 0 for a meeting in the 16 lines above it). `cl_rd` calls `cl_read` in part 4: with `cl_arm` set and the display on, a read in the picture from `cl_line` on sets bit 5 and clears `cl_arm`, so the bit comes once a picture. When the work runs in the picture (`workline`), `cl_vbl` sets `cl_arm` to 2: the reads in the rest of that picture do not get the bit, and the sprite table that `cl_scan` read is older than the one the frame handler writes for the next picture. A read below the picture (the frame handler's) turns 2 into 3, and the first read in the next picture runs `cl_fresh`, which works `cl_line` out again with part 3 at `$0000` and the VRAM copy at `$4000` (about 5,000 cycles), then goes on as with 1. `sat_hi` is in part 1 so that `cl_scan` can run there with part 4 in slot 1. A box is not the sprite's pixels: sprites whose boxes meet only at transparent pixels count as a collision.

### HALT

On the Master System a `HALT` ends at the game's next interrupt: the frame interrupt, a line interrupt when register 0 enables them, or the pause NMI. On the Next the CPU also takes the runtime's own interrupts, and each of them ends a native `HALT`: the ULA interrupt of the once-a-frame work, every frame; a line interrupt whose event the game does not get (line interrupts off in register 0, a `RASTER` overlay's lines, an event held for a frame handler that still runs); a frame event with frame interrupts off in register 1, which only sets the status flag. A game that paces a loop with `HALT` then runs it too fast.

An overlay therefore patches each `HALT` the game runs into the I/O `RST` and an inline code: `$76` for a `HALT`, `$FB` for `EI` then `HALT`, `$C9` for `HALT` then `RET` ([nms-format.md](nms-format.md)). `op_halt` in `fw4.asm` points `irq_t1` and `irq_t2`, the two places where the runtime enters the game's `$0038`, at `hw_irq`, saves their target in `hw_irq_j`, and has `fw_exit` return to `hw_loop` in part 1 with the game's registers, the game's stack, and the address after the site (or the game's own return address, for `$C9`) on top of it. `hw_loop` runs `EI` then `HALT` until `hw_jr` jumps to `hw_done`; the runtime's own interrupts return to it and the wait goes on. When the runtime enters the game's handler, `hw_irq` calls `hw_hit` (part 4), which turns `hw_jr` to `hw_done` and puts the targets back, and goes on to the handler. The handler returns into the wait, which then returns to the game. While the wait runs, `frm_t1` (`fw_line_irq`) and `frm_t2` (`irq_frame`) call `frm_run__no` in place of `frm_run`, so no event is held for a frame handler that still runs: a handler that waits in a `HALT` (Pit Pot runs its game in its frame handler) takes the next event nested, as on the Master System. `hw_hit` puts `frm_run` back. With the game's interrupts off, a patched `HALT` halts in `hw_dead` with interrupts off, as the native one.

A game whose overlay patches no `HALT` runs the same instructions as before: the dispatch for the new codes comes after every other inline code, in place of the jump to `fw_fatal` that those codes took, and `frm_t1`, `frm_t2`, `irq_t1` and `irq_t2` keep their targets.

The pause NMI does not end a patched `HALT`; the wait ends at the next frame or line event the game gets.

### Runs of outputs

A run of patched outputs in a row (`tr_start` in `trace.asm`) is kept in the trace cache like a copied trace, with its length and kind in place of a code address. A run holds at most `TR_RMAX` sites (one less than the high byte of `TR_CODE`), so a length is never read as a code address; the sites after that start a new run. A run of only OUTI or only OUTD is sent as one block (`out_block`). The other runs collect their bytes and send them as one block from 3 bytes. `RUN_BREAK_EVEN` in `tools/tracedef.py` holds the run lengths that pay.

The trace cache keeps what was decided for each trace site: a copy, a run, or that the site runs as a single output because no copy can be made. It fills page `TRC_PAGE` with 256 sets of 4 entries. A site's set is the low byte of its address XOR the high byte; a new entry goes first in its set and the oldest entry of the set is dropped. An entry is found by the site address, the port classes, and the pages of the two slots the game's code was read from: the site's, and the loop head's when it is in another 8K slot, else the end's. A copy, run or decision read from RAM (SMS RAM or cart RAM) is not kept (`tr_store`): the game can write new code there while the page stays the same, so it is made again at every entry.

Copies go into the code area: `TR_CODE` to `$FCFF`, then `$FD18` to `$FEFD`, after the IM2 vectors. When it is full, every copy is dropped by starting a new code generation (`tr_newcode`). An entry keeps the generation its code was written in, and `tr_match` does not take a copy of an older one. The entries for runs and single outputs stay. When the generation number goes round (32 generations), the whole cache is emptied.

The overlay builder gives a site the trace form only where the runtime does more with it than a single output: `region` and `verdict` in `tools/tracedef.py` follow `tr_build` and `tr_rscan` step by step. The runtime takes port C's class from C at the site. The builder works it out from an `LD C,n` or `LD BC,nn` in the straight-line code before the site. When there is none, it takes the VDP data port for OUTI and OUTD, and no class for `OUT (C),r`. When that guess is wrong, the runtime fails to make the copy once and keeps the single-output decision in the cache.

The jump table has one entry for the shell in the free bytes after its last jump: `fw_resume` at `$E01B`, a `jp` whose two target bytes are at `$E01C`. The shell points it at its resume entry before it starts a game. The runtime's quit routine jumps to it after it has restored NextZXOS's pages and registers, so the shell finds the machine as it left it.

## Banked code

### Why 8K pages at `$E000`

Only one page is mapped at `$E000` at a time. The shell uses MMU7 for code and keeps MMU6 free. So a module can map cart data at `$C000` and work on it without unmapping itself. The linker sections are the high halves of 16K banks, `BANK_54_H` to `BANK_57_H`. z88dk links them at `$E000`. The low half of each bank is free for read-only data that code maps through MMU6. `BANK_54_L` to `BANK_57_L` are linked at `$C000`.

### Far calls

The trampoline is `nm_far` in `src/shell/far.c`:

```c
void *nm_far(uint8_t page, void *(*fn)(void *), void *arg);
```

It reads the current MMU7 page, maps `page` at `$E000`, calls `fn(arg)`, puts the old page back, and returns the result.

The calling convention:

- Every banked entry point has the type `void *fn(void *arg)`. To pass more than one value, pass a pointer to a structure in resident memory. To return a small number, cast it to `void *`.
- `page` is the page number the module is linked for. `src/shell/nm.h` has one `PAGE_` constant per module.
- Call a banked entry point only through `nm_far`, using the `NM_FAR` macro. A direct call works only if the caller is in the same page.
- Calls nest. Banked code may far-call another module, and `nm_far` restores each caller's page on the way out. The stack is resident, so it survives page changes.
- Code in a module calls the resident part directly. That covers the library, `nm_esx` and so on. Resident code never calls into a module except through `nm_far`.
- A pointer into a module's code or constants is valid only while its page is mapped. Do not keep one across a far call that may map another page.
- Interrupts are off for the whole run of the shell, so no interrupt handler sees a changed MMU7.

### Data in banked modules

- Modules keep no mutable data of their own. Shared state is in `struct nm_state`. The variable is `nm`, in `src/shell/state.c`. It is resident and cleared at start. Only the resident part is cleared, so do not rely on a module's uninitialised data being zero.
- `const` data in a module is fine. Messages and tables are examples. The data is read while the module's page is mapped.

### Pointers given to the operating system

NextZXOS and esxDOS read and write through pointers while their own pages are mapped at `$C000` and above. Anything passed to them has to be below `$C000`:

- Buffers and strings handed to `nm_esx` and `nm_p3dos` live in the resident part. This means a global variable, or a local variable on the stack.
- `nm_filter_sms` and `nm_filetypes` in `state.c` are examples. Putting them in a module would pass NextZXOS a pointer into a page it cannot see.

`nm_p3dos` also sets MMU6 and MMU7 to pages 0 and 1, which NextZXOS expects. It puts the old values back.

### The information screen

After `loader_load` has read the cart, found the overlay and applied it without error, and before it starts the game, it far-calls `info_show`. `info_show` is in `src/shell/info/info.c`, in the page `PAGE_INFO`. A failure returns to the browser with its message, and the screen is not shown.

`info_show` first leaves only the ULA screen showing: it hides all 128 hardware sprites and turns off the sprite layer, Layer 2, the tilemap and the copper, because a game ended with BREAK leaves its sprites in the attribute table. It writes 0 to port `$FF`, because the browser leaves a Timex mode on. It then clears the standard ULA screen and prints 32 columns of text. It takes the character shapes from the 48K ROM at `$3D00`, which is mapped while the shell runs. So the module has no font of its own. It prints:

- the file name. It is `nm_lname`, the long name that the browser gives in DE. `glue.asm` copies it next to the short name, cut to 127 characters. If the browser gave no long name, it is `nm_name`.
- the CRC32 and size, from `nm.launch`.
- from the overlay file, as the loader read it into `nm`: the `title` from its `META` chunk (`nm.title`), cut to 48 characters and broken over lines at spaces; the format version from the header, as major.minor; and the runtime ABI the file needs (both in `nm.nms_ver`).
- the game's status from the `META` chunk (`nm.status`): `working`, `imperfect`, `not working` or `untested`. A file with no `status` shows `untested`.
- the video rate the game will use: `50 Hz` or `60 Hz` for an overlay with `hz=50` or `hz=60`, else `boot rate (50 Hz)` or `boot rate (60 Hz)`, from NextReg `$05` bit 2.
- the flags, in words: `priority tiles`, `line-0 palette`, `tile cache`, `scroll split`, or `none`. They are the `CONF` switches as the loader read them, from `nm.launch.flags`.

It then waits. First it waits, for at most a short time, until no key and no joystick fire is held. This stops the key that picked the cart in the browser from counting. Then it polls every keyboard row, from port `$00FE`, and the Kempston joystick 1 fire bit, from port `$1F`, bit 4. It returns when one is pressed. Interrupts are off, so this is a polling loop. The game then starts as before.

### Loading an overlay file

`loader_load` in `src/shell/loader/loader.c` does this, in order. The file format is [nms-format.md](nms-format.md). The work is split over two modules: the loader (`PAGE_LOADER`) reads the cart, walks the file, and holds the CRC32 code; the overlay module (`src/shell/overlay/overlay.c`, `PAGE_OVERLAY`) does steps 2 and 4 to 7. The loader far-calls it for those (`overlay_find`, `overlay_apply`), and it far-calls the loader back for the two checks that need a CRC32 (`loader_check_range`, `loader_ramsite_old`). `src/shell/nms.h` has what they share.

The loader never holds a whole file in memory. It reads the index and the overlay file through `OVL_BUF`, 256 bytes, so a file or a chunk can be of any size. A small reader, resident in `src/shell/rd.c` (`struct rd`), hands out the bytes of one run of the file in order: `rd_take` gives the next few bytes in one piece, and `rd_piece` gives the next bytes in pieces for long data such as a `PATCH` or a `RASTER` routine. An operation may cross the end of the buffer: the reader moves the bytes not yet used to the start and reads more after them. `nm_seek` (esxDOS `F_SEEK`) starts a run anywhere in the file.

1. It reads the cart into pages 32 and up and computes its CRC32.
2. It finds the overlay file in `ovl/index` in the start folder (the current directory, read with `F_GETCWD` in `session_init` before the browser first opens; `.nexload` does not handle paths, so it is the folder holding the NEX), if the file is there. It searches the index in place with a binary search: for each entry it probes, it seeks to the entry and reads its 8 bytes. The entry gives the primary CRC32, which names the overlay file. A cart that is not in the index has no overlay. Without an index, the overlay file is the one named after the cart's own CRC32.
3. The walk. It reads `ovl/<CRC32>.nms` in the start folder once from the start to the end, and every byte up to the `END ` chunk goes through the running CRC32. It checks the header: the magic, format major version 1, and a runtime ABI not higher than `FW_ABI`. It reads each chunk header, checks that the chunk fits in the file, and notes where `CRCS`, `PTCH`, `CONF` and `META` start. It loads each `PAGE` chunk, as described below. It reads every other chunk only for the CRC32. `END ` must be last, with the right CRC32, and nothing may follow it. `CRCS` and `PTCH` must be there, and each of the four chunks may appear only once.
4. It seeks back to `CRCS` and checks that it lists the cart's CRC32. A list of any length works.
5. It seeks to `META` and keeps the `title` in `nm.title` and the `status` in `nm.status`, and seeks to `CONF` and keeps the switches `priority=1`, `toppal=1`, `tilecache=1`, `hsplit=1`, `collline=1`, `rastseg=1`, `hz=50` and `hz=60` in the runtime's flags (`NM_FL_x` in `nm.h`).
6. `PTCH`, first pass. It runs every `CHECK` operation against the cart pages, checks the bounds of every other operation, and works out the original instruction of every `RAMSITES` entry. Nothing is written yet, so a dump that fails a `CHECK` is left as it was read.
7. `PTCH`, second pass. It seeks back to the start of `PTCH` and applies the operations: `PATCH` into the cart pages, `START` into the start address and stack pointer, and `RAMSITES` or `RASTER` into the runtime's part 2 from `$3C00`, through MMU6. For `RAMSITES` it writes the table the runtime reads: the continuation, the count, and for each entry the address, the two original bytes and the two new bytes. It sets the hook addresses that the runtime reads, `rast_hook` and `ramp_hook`.

Only a failed read can stop the second pass. The cart is then part patched, and the loader reports the file as damaged. Picking the cart again reads it again from the card.

The failure codes and their messages are in `src/shell/nm.h` and `src/shell/session/session.c`. "Unknown game" names the file that the loader looked for.

#### Loading `PAGE` chunks

The walk loads each `PAGE` chunk where it finds it (`load_page` in `loader.c`). Before the walk, the loader clears the page numbers in `pg_tab`, the runtime's table of code pages, so no page of an earlier game stays in use. For each chunk:

1. It reads the page number, the number of entries and the entry addresses through `OVL_BUF` and the running CRC32, like any other chunk data, and checks them against the limits in [nms-format.md](nms-format.md).
2. It writes the entries into `pg_tab`, through MMU6 with the runtime's part 2 mapped at `$C000`. `PG_TAB` in `build/fwsyms.h` is the table's address.
3. It maps RAM page `CODE_PAGE` + the page number at `$C000` and copies the page's code into it through `OVL_BUF`, then runs the CRC32 over the page's bytes where they are. It fills the rest of the RAM page with zeros.

The code goes into its page once, during the walk, and is never read twice. If the walk then fails, the file is refused and the page is not used.

### Starting a game

`nm_launch` is in `src/shell/glue.asm`. It copies the start-up values into the runtime's state variables. It saves the NextZXOS pages that the runtime overwrites: the tile definitions and one tilemap page. It maps the runtime at `$E000`. Then it jumps to the jump table's start entry. It never returns. Only the resident part can do this, because the runtime replaces whatever is in slot 7.

### Coming back

BREAK in a game makes the runtime restore NextZXOS (`fw_quit` in `fw.asm`, `fw_quit4` in `fw4.asm`): it stops the copper, turns off the tilemap, the sprites and Layer 2, hides all 128 hardware sprites, sets every clip window back to the whole screen, silences the AY chips, copies NextZXOS's banks 5 and 7 back and restores the NextRegs the shell saved at start, among them `$05` with the video rate. It then jumps to `fw_resume`, which jumps to `nm_resume` in `glue.asm`. `nm_resume` sets the stack to `$BFE0`, maps pages 0 and 1 at `$C000` and `$E000`, and jumps to `nm_run`. The stack frames of the first pass are abandoned. The state in `nm` is kept, so a failure message from a rejected game is still shown.

BREAK or SPACE in the browser ends the program (`IDE_BROWSER` returns carry set and zero clear; carry clear is an error, which shows its message in the help line and opens the browser again). `session_pass` has already put the user's browser filter and flags back. `leave` in `session.c` then writes back the NextRegs saved at start (`nm.launch.nr`) and the CPU speed (`nm.speed`, NextReg `$07`, read before the shell sets full speed). It calls `nm_basic` in `glue.asm`, which disables interrupts, sets the stack to RAMTOP, clears `ERR_NR`, maps pages 0 and 1 at `$C000` and `$E000` and runs the BASIC command `NEW` through `IDE_BASIC`. NextZXOS starts its BASIC again and shows its menu, with the browser's filter and flags as the user left them. `NEW` does not return. Loading the NEX overwrote bank 2, which holds the BASIC stack, so the shell cannot return to the program that started it and `NEW` rebuilds BASIC. A card whose `autoexec.bas` starts NextMasterSystem starts it again after `NEW`. If `IDE_BASIC` does return, `nm_basic` soft-resets the machine with NextReg `$02`.

## Source layout

```
Makefile                 one-command build: make
src/runtime/             the assembly runtime (z80asm)
    runtime.asm          four sections: fw, fw2, fw3, fw4, one per page
    fw.asm trace.asm trvars.inc           part 1
    fw2.asm fw3.asm                       parts 2 and 3
    fw4.asm trbuild.asm                   part 4 (trbuild.asm: the trace builder)
    vdpcheck.asm vdpcheck4.asm            the trace build's VDP check (make TRACE=1), parts 1 and 4
    tables.inc tables2.inc tables3.inc    generated by tools/gentables.py
    memplan.inc          page numbers of the memory plan
src/shell/               the C shell
    nm.h                 shared declarations, PAGE_ numbers, failure codes
    main.c               main and the main loop (resident)
    far.c                the far-call trampoline (resident)
    state.c              shared state and strings handed to the OS (resident)
    os.c                 esxDOS file calls (resident)
    rd.c                 the overlay file reader (resident)
    nms.h                what the loader, the overlay module and rd.c share
    glue.asm             nm_esx, nm_p3dos, nm_launch, nm_resume (resident)
    fwpages.asm          puts the runtime's pages into their banks
    zpragma.inc          linker settings (stack, start address)
    session/session.c    browser loop and messages (BANK_54_H)
    loader/loader.c      cart reading, the overlay file's walk (BANK_55_H)
    loader/crc32.asm     CRC32 (BANK_55_H)
    info/info.c          the information screen (BANK_56_H)
    overlay/overlay.c    the overlay index, chunks and patching (BANK_57_H)
tools/check-layout       build-time layout checks
tools/mknms.py           builds an overlay file from a spec and the cart
tools/mknmsindex.py      builds ovl/index from a folder of overlay files
tools/build-overlays.py  builds a folder of specs and the index
tools/sitescan.py        scans a cart for the sites an overlay patches
tools/mkspec.py          drafts a spec from a scan
tools/gentables.py       regenerates the runtime's tables
build/                   all build output; build/nms.nex is the result
```

### How the build fits together

`make` needs Docker, make, sh, awk and sed. The z88dk tools (`zcc`, `z88dk-z80asm`) run in z88dk's Docker image, `z88dk/z88dk:latest` (`Z88DK_IMAGE` in the Makefile picks another). Each tool call is one `docker run` with the `public/` folder mounted at its own path, so the relative and absolute paths in the Makefile mean the same in the container. The Makefile's own work (`sed`, `awk`, `tools/check-layout`) runs on the host. The steps:

1. `z88dk-z80asm -split-bin` assembles `runtime.asm`. Its four sections have their own origins: `$E000`, `$2000`, `$0000` and `$2000`. The output is one file per section, each padded to 8192 bytes, plus a map file.
2. The Makefile reads the map for the few runtime addresses the shell needs. It writes them to `build/fwsyms.inc` and `build/fwsyms.h`. It also turns `memplan.inc` into `build/memplan.h`.
3. `zcc` compiles each C file. Resident files use the default sections. Module files get `--codeseg`, `--constseg`, `--dataseg` and `--bssseg` set to the module's bank section.
4. `fwpages.asm` puts the four runtime files into banks 12 and 50 as plain bytes with `binary`.
5. `zcc -create-app -subtype=nex` links everything and writes the NEX.
6. `tools/check-layout` runs. It checks size and alignment rules that the assembler cannot check. The rules are listed in that file.

The runtime is assembled at addresses that have nothing to do with where its bytes sit in the NEX. The NEX loader puts bank 12 and bank 50 into physical pages 24, 25, 100 and 101. The runtime maps them where it wants.

### The trace build

`make TRACE=1` builds `build/trace/nms.nex`: the same program with checks in the runtime that test tools read. The normal build has none of this code. To make room for it at the end of part 1's code, the trace build's trace code area starts at `$FBC0` instead of `$FB00` (`TR_CODE`), 192 bytes smaller. The checks are in `src/runtime/vdpcheck.asm`, which `fw.asm` includes when the assembler gets `-DTRACE_BUILD`, and `src/runtime/vdpcheck4.asm`, which `fw4.asm` includes then. Part 1 has the counters, `tc_ret` and the entries the runtime calls; each entry maps part 4 into slot 1 for the work (`tc_far`) and puts back the page that slot 1 held, read from the NextReg.

The VDP check counts the interrupt handlers that change the VDP address while the game code they interrupted is in the middle of a VDP data stream. At each frame or line handler entry it delivers, the runtime notes the VDP state (latch, code, address) and the handler's return address, and puts its own routine `tc_ret` in the return slot. The handler's `RET` or `RETI` goes to `tc_ret`, which compares the VDP state with the noted one and goes on to the return address. Game handlers often switch to a stack of their own, so the return slot is the only sure sign of the exit. The counters, 16 bits each, are at `tc_cnt` in the trace build's `build/trace/rt/runtime.map`, followed by two addresses for the last bite: where its handler returned to (`tc_bpc`), and `fw_ret` of the access that bit (`tc_bsite`, just after the site).

| Counter | Counts |
|---|---|
| `tc_ent` | handler entries noted |
| `tc_mid` | of them, entries while the game was in a stream: the first control byte waited for its second, or a data access followed the last control write |
| `tc_race` | of those, handlers that left the VDP state changed |
| `tc_bite` | of those, the cases where the game then used the changed state: its next VDP access found the state as the handler left it, and was a data access, or a control write after the game had written the first control byte and the handler left the latch clear |
| `tc_ovf` | entries not noted, because eight handler entries were still open |

`tc_race` follows the definition literally, so it also counts streams the game had already finished. `tc_bite` counts only the races that put data in the wrong place. A game that reads or changes its handler's return address sees `tc_ret` there, so the trace build can run such a game differently. A handler that never returns (it resets SP and jumps) leaves its entry open.

## Adding a C module

1. Make a directory `src/shell/<name>/`. Put the C and assembly files in it.
2. Choose a free bank. Banks 54 to 57 are taken, and banks 58 to 61 are the overlay's code pages. Bank 62 would be pages 124 and 125. Keep the pages below page 224, and clear of the pages in the memory map.
3. In the `Makefile`, add the name to `MODULES`. Set `<name>_SEG` to the bank's high half, for example `BANK_62_H`.
4. In `src/shell/nm.h`, add `PAGE_<NAME>`. Its value is the high half's page number, 125 for bank 62. Declare the entry points, each as `void *fn(void *arg)`.
5. Call it with `NM_FAR(PAGE_<NAME>, fn, arg)`.
6. Assembly files in a module start with `section BANK_62_H`.

A module has 8K for code and constants. When a module gets full, split it. The linker stops with a message when a section does not fit.

If a module needs data larger than a few hundred bytes, such as icons or a font, put it in the low half of its bank. That half is `BANK_62_L`, linked at `$C000`. Map the page with `ZXN_WRITE_MMU6`.

## Known limits

- The memory plan limits a cart to 512K. A cart between 512K and 512K plus 255 bytes passes the size check. It then uses one page too many. This is the prototype's check, kept as it was.
- A `PATCH` must stay inside one 8K cart page. A `RASTER` routine or a `RAMSITES` table must fit in the 1024 bytes from `$3C00` in the runtime's part 2. The shell refuses an overlay file that breaks these rules, and reports failure 7. It does not write past the page.
- `$E01B` to `$E01D` was unused in part 1 of the runtime. It now holds `fw_resume`. Overlays do not touch it.
- An overlay has at most 8 code pages and 64 page entries in all (`CODE_MAX` and `CODE_ENTS` in `src/runtime/memplan.inc`).
- A whole Layer 2 rebuild and a large priority redraw run inside one run of the once-a-frame work, or inside `pic_ready` at display-on, with interrupts off; the game gets no interrupt until they end (Micro Machines' 224-line screens: several frames).
- Priority tiles in 224-line mode (`pri224` in `fw2.asm`) use Layer 2 at 320x256, where it covers all 224 lines. Its X scroll is set in the once-a-frame work: when a game writes H scroll in the picture, the tilemap moves at once and the priority tiles at the next frame. The locked top rows (register 0 bit 6) are not done in that mode.
- In 224-line mode the 16 lines above and the 16 lines below the 192-line area are border lines to the ULA, and its border is opaque. The 224-line copper list (`cop_224` in `fw3.asm`) turns the ULA off in those lines (NextReg `$68` bit 7), so transparent tile pixels there show the fallback colour, as in the rest of the picture. In those lines the side borders show the fallback colour too, and SMS column 0 is not blanked when register 0 bit 5 asks for it (the ULA blanks it in the 192-line area).
