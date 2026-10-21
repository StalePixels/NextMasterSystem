# Glossary

The terms that the NextMasterSystem docs, specs and tools use. Each entry says what the thing is, gives the name it has in the code or on a spec line, and names the doc and section that describe it in full.

Two kinds of number appear in the entries. A "cart offset" is a position in the cart. A "Z80 address" is a position in the 64K address space the game's code sees. They are the same for the first 32K of a cart and differ above that.

**A8.** One of the two Next tilemaps the runtime keeps for the background. It is the map M0 turned by 8 columns. The copper switches a line from M0 to A8 part-way along, so the 320-pixel Next map wraps like the 256-pixel Master System map. Code: `MAP_A8`. Read more: design.md, "The once-a-frame work" (the copper list).

**ABI (runtime ABI).** The version number of the runtime's interface to overlays: the jump table, the inline codes and the state variables at fixed addresses. An overlay file records the ABI it needs. The runtime refuses a file that needs a higher number than its own. Code: `FW_ABI` in `src/runtime/fw.asm`; header byte 6 of a `.nms` file. Read more: nms-format.md, "Versions".

**Alias.** A second cart CRC32 that an overlay accepts, for another region, revision or dump of the same game. Aliases are listed in the file's `CRCS` chunk and collected in the index. The primary CRC32 and the aliases together are the overlay's accepted CRC32s. Read more: nms-format.md, "`CRCS`: accepted carts".

**`asm` block.** A spec block that replaces game bytes with assembly. `asm ADDR LEN` starts it, `endasm` ends it. The lines between are assembled with `sjasmplus` as if at the Z80 address of cart offset `ADDR`. The code replaces `LEN` cart bytes; unused bytes become `NOP`. The cart supplies the `CHECK` for those bytes. Read more: overlays.md, "Writing code in a spec".

**AY.** The sound chips of the Next. The runtime plays the Master System's sound on them in place of the Master System's own sound chip (the PSG), so the sound is close but not the same. Read more: readme.txt, "WHAT WORKS".

**Bank.** A block of memory that can be switched in as a unit. The word has two meanings in these docs, and both blocks are 16K. A cart bank is a 16K block of the cart, which the mapper shows in a cart slot. A NEX bank is a 16K block of the NEX layout, made of two 8K Next pages: bank `n` is pages `2n` and `2n+1`. Read more: design.md, "Pages"; sitescan.md, "How it works" (banks).

**Bank call, bank header.** Two ways `sitescan.py` finds code in a banked cart slot that no path reached. A bank call is `LD A,n`, then `LD ($FFFF),A`, then `CALL` or `JP` into `$8000-$BFFF`; the target becomes an entry point in bank n. A bank header is a bank that starts with several `JP nn` instructions into `$8000-$BFFF`; each is an entry point in that bank. Read more: sitescan.md, "How it works".

**Banked code window.** The 8K Next slot at `$E000-$FFFF` (slot 7) in which the shell maps one module's page at a time. A far call (`nm_far`) maps the page there. Read more: design.md, "Banked code".

**Banked module.** A part of the C shell that lives in its own 8K page and runs only while a far call (`nm_far`) has mapped it at `$E000`. Modules keep no mutable data of their own. Code: `PAGE_` constants in `src/shell/nm.h`. Read more: design.md, "Banked code" and "Adding a C module".

**Block write.** A run of bytes sent to the VDP data port by one instruction (`OTIR`) or by an unrolled run of `OUTI`. The runtime handles it as one block, not byte by byte. Read more: design.md, "The once-a-frame work" (the tile cache); "Runs of outputs".

**BREAK.** The Next key that leaves a game for the browser, and leaves the browser for NextZXOS. Read more: design.md, "Coming back".

**Byte scan.** A second pass of `sitescan.py` that looks at every byte of the cart for I/O instruction and mapper store patterns that no code path reached. It rates each hit by how much the bytes around it look like code. Rows are `io_unreached` and `mapper_unreached`. Read more: sitescan.md, "Byte scans".

**Cart.** A Master System game cartridge, and the `.sms` file that holds its contents. Read more: nms-format.md, "Conventions".

**Cart image.** The bytes of a cart as the loader holds them in memory, after any copier header is removed. `PATCH` operations change it. Read more: nms-format.md, "Conventions".

**Cart offset.** A byte position in the cart image, after any copier header is removed. Spec lines give it in hex. Read more: nms-format.md, "Conventions".

**Cart RAM.** RAM on some carts, switched in by the Sega mapper (`$FFFC` bit 3). The runtime keeps it in memory pages 96 to 99. It works during play and is not saved. Code: `CARTRAM_PAGE`. Read more: readme.txt, "KNOWN LIMITS IN EVERY GAME".

**CDL.** A code/data log written by the Mesen2 emulator (`CDLv2`). `sitescan.py` reads one with `--cdl` and uses it only to add entry points. Read more: sitescan.md, "Running it".

**`CHECK` (comment in a draft spec).** A comment that `mkspec.py` writes where it could not decide. `CHECK high`, `CHECK medium` and `CHECK low` mark a byte pattern found by the byte scan, rated by the evidence. The author reads the code around it and makes it a spec line only if it is code. This is a different thing from the `CHECK` operation above. Read more: overlays.md, "3. Edit the spec".

**`CHECK` (operation).** An operation in a `PTCH` chunk: the CRC32 of a range of the cart image must equal a stored value. The file holds only the CRC32, never the bytes. If a `CHECK` fails, the loader applies no change and reports a different dump. Every byte a `PATCH` writes must lie inside a checked range. Read more: nms-format.md, "`PTCH`: operations".

**Chunk.** A tagged section of an `.nms` file: a four-character tag, a length and the data. A reader skips tags it does not know. Tags are `CRCS`, `PTCH`, `CONF`, `META`, `ICON`, `PAGE`, `SIGN` and `END `. Read more: nms-format.md, "Chunks".

**Class (port class).** One of eight groups of I/O port numbers, worked out from address lines A7, A6 and A0 as the Master System decodes them. The inline code of a patched `OUT (n),A` or `IN A,(n)` carries the class, not the port number. Read more: nms-format.md, "Inline codes"; sitescan.md, "`NAME.sites.tsv`" (port classes).

**Code cave.** A few filler bytes in the cart that the game never runs, overwritten by an `asm` block with a short routine of our own. In `fantasyzone2.spec` the bytes between the routine of `RST $08` and the `RST $18` vector hold a far call to a code page and a `RET`. The game's two 3-byte `CALL $CC00` sites become `call sat_far`, a call to that routine. Code: `label` and `asm` lines in `overlays/fantasyzone2.spec` (`sat_far`). Read more: overlays.md, "Code pages" for the far call the routine makes.

**Code page.** An 8K block of Z80N code of our own, stored in an overlay's `PAGE` chunk. It runs at `$2000-$3FFF` while one of its entries runs. A spec uses one to replace a game routine that is too slow through the runtime's traps. Code: `page` block in a spec; `CODE_PAGE`, `CODE_MAX` in `src/runtime/memplan.inc`; `pg_tab`. Read more: overlays.md, "Code pages"; nms-format.md, "`PAGE`: code pages".

**`codem`.** Spec line for a Codemasters mapper store, `LD ($0000/$4000/$8000),A`. It becomes `RST` plus an inline code and one skipped byte. See "Mapper spec lines". Read more: nms-format.md, "Inline codes".

**Codemasters mapper.** A mapper used by some carts, for example Micro Machines. It switches banks by stores to `$0000`, `$4000` and `$8000`, not by the Sega registers at `$FFFC-$FFFF`. Spec line: `codem`. Read more: sitescan.md, "Running it" (`--mapper`).

**`CONF`.** The chunk of settings in an `.nms` file: text lines of `key=value`. The keys the runtime acts on are `priority`, `toppal`, `tilecache`, `hsplit`, `collline`, `rastseg`, `workline` and `hz`. Read more: nms-format.md, "`CONF`: settings".

**Confidence.** The rating of a row in `NAME.sites.tsv`: `high`, `medium`, `low` or `very-low`. `high` is reached by proven control flow from the vectors, an `--entry` address or a dynamic log. `medium` is reached through something the scanner inferred, such as a guessed table length or a harvested address. The byte scans have their own scale. Read more: sitescan.md, "`NAME.sites.tsv`" and "Byte scans".

**Continuation.** In a `RAMSITES` operation, the address the game jumps to once its RAM code is built. The cart image is patched to call the runtime there first; the runtime patches the RAM code and then jumps to the continuation. Spec line: `ramhook`. Read more: nms-format.md, "`RAMSITES`".

**Converted cart.** The cart converted to Next tile rows, with cart page `n` in memory page `128 + n`. The runtime builds it at game start when `tilecache` is on, and the tile cache copies tiles from it. Code: `CONVT_PAGE`, `tc_build`. Read more: design.md, "Pages".

**Copier header.** 512 extra bytes at the start of some cart files. A file whose size is 512 more than a multiple of 16K has one. The tools and the loader leave it out before they compute the CRC32 or use any cart offset. Read more: nms-format.md, "Conventions".

**Copper.** The Next's coprocessor. It writes NextRegs at chosen screen positions. The runtime uses it for scroll changes in the middle of a picture and for the per-line horizontal scroll of a `RASTER` overlay. Code: `cop_update`, `cop_raster`, `cop_224`, `cop_seg` in `fw3.asm`. Read more: design.md, "The once-a-frame work".

**Copper list.** The program the copper runs, rewritten by the runtime once a frame. Read more: design.md, "The once-a-frame work".

**CRAM.** Colour RAM of the VDP. It holds the palettes: first the background palette, then the sprite palette. The runtime keeps a copy at `cram` in the jump table's state area and applies each CRAM write to the Next palettes. `jt_vwrite` does not write CRAM; CRAM writes go through the I/O `RST`. Read more: design.md, "CRAM writes"; nms-format.md, "Writing VRAM from page code".

**CRC32.** The checksum used to identify carts and to check files. It is the same CRC32 that zip and PNG use. Read more: nms-format.md, "Conventions".

**`CRCS`.** The chunk that lists every cart CRC32 an overlay accepts. The first is the primary CRC32. Read more: nms-format.md, "`CRCS`: accepted carts".

**`cur_mmu`.** Eight bytes at `$E02D`: the page the game has in each of the eight slots. The runtime restores the game's pages from it after borrowing a slot. Read more: design.md, "The runtime's pages".

**Dispatcher.** In `sitescan.py`, a routine that takes its return address, adds twice A to it, reads a word through it and jumps to that word, so that a table of addresses follows the call. Rule 1 of the pattern rules finds them. Read more: sitescan.md, "Rule 1: inline jump tables".

**Display enable.** Bit 6 of VDP register 1. The runtime turns the Next's tilemap, sprites and Layer 2 on or off with it. While it is off, the picture shows the fallback colour. Code: `r1_hw`, `disp_on`. Read more: design.md, "Display off and on".

**Dump.** A cart file as one person made it. Different dumps of one game can differ, so NextMasterSystem identifies a dump by its CRC32. The docs write "dump" where the text is about one particular copy and its CRC32, and "cart" otherwise. Read more: nms-format.md, "`CRCS`: accepted carts".

**Dynamic log.** A list of addresses that an emulator saw the game run, given to `sitescan.py` with `--log`. The scanner uses it only to add entry points. Read more: sitescan.md, "Dynamic logs".

**Entry (page entry).** A routine in a code page that a far call can reach. A `page` line lists the entry names; entry numbers follow the order of the names. A patch names an entry by `pg_NAME` and `ent_NAME`. Read more: overlays.md, "Code pages".

**Entry point (scanner).** An address from which `sitescan.py` starts reading code: the reset and interrupt vectors, call and `RST` targets, table entries, `--entry` addresses, log addresses, and addresses it harvests. Read more: sitescan.md, "How it works".

**esxDOS.** The file system interface of the Next that the shell uses to read carts and overlay files. Code: `nm_esx`, `F_GETCWD`, `F_SEEK`. Read more: design.md, "Loading an overlay file".

**Fallback colour.** The colour the picture shows where the Master System shows its backdrop colour, including while the display is off. Read more: design.md, "Display off and on".

**Far call (code page).** A call from a site into a code-page entry. The runtime maps the page into `$2000-$3FFF`, runs the entry with the game's registers, then maps the old page back and returns to the byte after the page and entry numbers. Two forms: `RST` with the inline code `$80`, then page and entry; or `CALL jt_far`, then page and entry. Code: `jt_far`, `far_io`. Read more: nms-format.md, "The far call".

**Far call (shell).** A call from the resident C code into a banked module. `nm_far` maps the module's page at `$E000`, calls the function, and maps the old page back. It is not the same mechanism as the code page far call. Code: `nm_far`, `NM_FAR`, in `src/shell/far.c`. Read more: design.md, "Far calls".

**`FASTENTRY`.** The macro that starts every `RST` handler in `fw.asm`. It saves the game's registers on the game's stack and on the runtime's own stack, so a handler may use every register. Read more: `src/runtime/fw.asm`, "Handler frame".

**Frame cost model.** The part of `sitescan.py` that estimates, from the code alone, how many Next cycles each routine takes on the runtime, which foreground routines an interrupt can cut into while they write the VDP, and which interrupt routines run longer than a frame. Its results are places to look at, not proven faults. Read more: sitescan.md, "Frame cost model".

**Frame event.** The Master System's frame interrupt, delivered to the game's handler by the runtime at the end of line 192 (line 208 in 224-line mode). Read more: design.md, "The video rate".

**Frame handler.** The game's own interrupt routine that runs on the frame event. Read more: design.md, "The once-a-frame work".

**Frame overrun.** A frame whose work takes longer than the Next frame, so the game slows down or shows faults. A game that fits in a frame on the Master System can overrun on the Next, because every I/O instruction runs through a trap. `frame overrun` is one of the `flags` values in `META`. Read more: nms-format.md, "`META`: the game's details"; sitescan.md, "Findings".

**`fw_resume`.** The jump table entry at `$E01B`: a `jp` whose target the shell sets before it starts a game. The runtime's quit routine jumps to it after it restores NextZXOS's pages and registers. Read more: design.md, "Coming back".

**H scroll, V scroll.** The VDP's horizontal and vertical scroll values. A `RASTER` routine computes the value of VDP register 8 (H scroll) for each line. Read more: nms-format.md, "`RASTER`".

**HALT pacing.** A game loop that waits for the next interrupt with `HALT`, so that it runs once a frame or counts frames. On the Next a native `HALT` also ends on the runtime's own interrupts, so an overlay patches each such `HALT` into a wait for the game's own interrupt. Spec lines `eihalt` and `haltret`; inline codes `$76`, `$FB`, `$C9`. Code: `op_halt`, `hw_loop`, `hw_irq`. Read more: design.md, "HALT"; overlays.md, "HALT".

**Handler.** Two things. A runtime handler is the code that receives a patched instruction through an `RST`, such as `fw_io`. A game handler is the game's own interrupt routine, such as the routine at `$0038`. Read more: design.md, "While a game runs".

**`hz`.** Spec line and `CONF` key for the video rate of a game: `50`, `60` or `any`. With `50` or `60` the runtime sets the Next to that rate at game start. With `any`, or no line, the game runs at the rate the Next booted at. Code: `hz_setup` in `fw3.asm`. Read more: overlays.md, "Switches"; design.md, "The video rate".

**`ICON`.** The chunk that holds a 32x32 icon. The runtime does not read it yet. Read more: nms-format.md, "`ICON`: the icon".

**Index.** The file `ovl/index`. It maps every accepted CRC32 to the primary CRC32, which is the overlay's file name. The entries are sorted, so the loader finds a cart by binary search without opening each overlay. Built by `tools/mknmsindex.py`. Read more: nms-format.md, "The index".

**Information screen.** The screen the shell shows after it loads a game and before it starts it: file name, CRC32, title, status, video rate and switches. Any key or fire starts the game. Code: `info_show` in `src/shell/info/info.c`. Read more: design.md, "The information screen".

**Inline code.** The byte after an `RST` to the runtime that says which instruction the `RST` replaced, for example `$00-$07` for `OUT (n),A` and `$80` for a far call. The codes are part of the ABI and never change meaning. Read more: nms-format.md, "Inline codes".

**Interrupt mode (IM 1, IM 2).** Z80 modes that decide where a maskable interrupt goes. Master System games usually use IM 1, which jumps to `$0038`. The runtime needs IM 2, so many specs change `IM 1` to `IM 2` in a two-byte `asm` block, and the runtime keeps the game's I register. Read more: overlays.md, "Writing code in a spec"; sitescan.md, "Known limits".

**`io` vector.** The `RST` vector that a spec points at the runtime's general I/O entry (`vector 10 io`). Sites patched through it get the trace forms. Without one, every site is a single output. `vector 00 io` also turns a game's `JP $0000` into a jump to its start address. Read more: overlays.md, "3. Edit the spec"; mknms.py, spec lines (`python3 tools/mknms.py --help`).

**`jt_far`.** The jump table entry at `$E072` for the code page far call. See "Far call (code page)".

**`jt_peek`.** The jump table entry at `$E075` for page code. It returns in A the byte the game sees at the address in HL. Page code uses it for any address that can lie in `$2000-$3FFF`, because a plain read there reads the code page. Read more: nms-format.md, "Rules for page code".

**`jt_vwrite`.** The jump table entry at `$E078` (ABI 7) for page code. It writes blocks of bytes into VRAM in runs: the same bytes in the same places as a control write of each run's address followed by data writes to the VDP data port. It updates the VRAM copy, the Next tilemaps, priority marks, tile conversion marks and the sprite table mark. Read more: nms-format.md, "Writing VRAM from page code".

**Jump table.** The table of `JP` instructions at `$E000` that is the overlay ABI. Entries never move; new ones go at the end with a raised `FW_ABI`. Code: `fw_jt`; entries `jt_out_n`, `jt_in_n`, `jt_ed`, `jt_ld_de_a`, `jt_start`, `jt_fatal`, `jt_outi_run`, `jt_io`, `jt_io0`, `fw_resume`, `jt_far`, `jt_peek`, `jt_vwrite`. Read more: overlays.md, "Names that every block knows".

**Kempston.** The Next's joystick interface that the shell polls, with the keyboard, to wait for a key or fire press on the information screen. Read more: design.md, "The information screen".

**`label`.** Spec line `label NAME ADDR` that gives a game address (a cart offset) a name for use in `asm` blocks. It is visible in every block of the spec. It may not reuse a name that every block already knows. Read more: overlays.md, "Labels".

**Layer 2.** A Next bitmap layer. The runtime uses it for priority tiles, at 256x192 in 192-line mode and 320x256 in 224-line mode. Code: `L2_PAGE`, `L2W_PAGE`, `L2_TRANS`. Read more: overlays.md, "Switches" (`priority`).

**Library page.** A code page that more than one game uses. Its source is one file in `overlays/lib/`, which starts with its contract: the game routine it replaces, its entries and registers, and what it needs from the game. A spec uses it with the line `libpage N NAME`, and each overlay carries its own built copy in a `PAGE` chunk. `build-overlays.py` stops when two overlays carry different bytes for one library page. Read more: overlays.md, "Library pages".

**Line event.** An SMS line interrupt, programmed by the game. The runtime delivers it to the game's handler. Read more: design.md, "The video rate".

**Line mode (192-line, 224-line).** The Master System picture heights. 192 lines is the usual size. 224 lines is the taller picture some games use (Micro Machines). The runtime uses a different copper list and a wider Layer 2 for priority tiles in 224-line mode. Read more: design.md, "Known limits".

**Loader.** The part of the shell that reads the cart, finds and checks the overlay, and applies it. Code: `loader_load` in `src/shell/loader/loader.c`. Read more: design.md, "Loading an overlay file".

**Locked top rows.** Rows at the top of the Master System picture that ignore horizontal scroll (VDP register 0 bit 6), used for score bars. The runtime does them with the copper, but not in 224-line mode. Read more: design.md, "Known limits".

**M0.** The first of the two Next tilemaps the runtime keeps for the background. It holds SMS columns 0 to 31 in Next columns 0 to 31 and SMS columns 0 to 7 again in columns 32 to 39. See "A8".

**Mailbox.** In `sitescan.py`, a RAM byte that the interrupt handler reads and then sets to 0, written by foreground code. If two foreground stores can write it before the handler runs, the first value is lost. Rule 2 of the pattern rules lists them as places to check. Read more: sitescan.md, "Rule 2: mailbox races".

**Mapper.** Hardware in the cart that decides which 16K block of the cart shows in each cart slot. The Sega mapper has registers at `$FFFC-$FFFF`; the Codemasters mapper uses stores to `$0000`, `$4000` and `$8000`. The Next has no such hardware, so an unpatched mapper store would write RAM and the bank would not change. Each mapper store is patched into a call to the runtime. Read more: sitescan.md, "Byte scans".

**Mapper register.** On the Sega mapper, `$FFFC` controls cart RAM, `$FFFD` is the bank in cart slot 0, `$FFFE` the bank in cart slot 1 and `$FFFF` the bank in cart slot 2. Read more: sitescan.md, "How it works"; "Known limits".

**Mapper spec lines.** Spec lines that patch a mapper store. Each becomes `RST` plus an inline code, and the runtime skips the bytes the longer instruction had.

| Spec line | Instruction it replaces |
|---|---|
| `mapper` | `LD (DE),A`, one byte |
| `mapst` | `LD ($FFFC-$FFFF),A` |
| `mapsthl` | `LD ($FFFC-$FFFE),HL` |
| `mapstbc` | `LD ($FFFC-$FFFE),BC` |
| `mapstde` | `LD ($FFFC-$FFFE),DE` |
| `mapld` | `LD HL,$FFFF` then `LD (HL),n` |
| `mapldk` | `LD HL,$FFFC+k` then `LD (HL),n` |
| `maphl` | `LD (HL),n` with n below 16, where HL holds a mapper register address |
| `codem` | Codemasters `LD ($0000/$4000/$8000),A` |

Read more: nms-format.md, "Inline codes"; mknms.py spec lines (`python3 tools/mknms.py --help`).

**Memory plan.** The list of the 8K pages that the runtime and the shell use, in `src/runtime/memplan.inc`. The Makefile turns it into `build/memplan.h` for the C code. Read more: design.md, "Pages".

**`META`.** The chunk of game details for the browser and the information screen: `title`, `id`, `dump`, `year`, `publisher`, `regions`, `status`, `flags`, `issues`, `tested`, `version`, `author`. Read more: nms-format.md, "`META`: the game's details".

**MMU.** The Next hardware that maps 8K pages into the eight slots of the CPU address space. MMU0 to MMU7 are the slots; NextRegs `$50` to `$57` choose their pages. "MMU1" means slot 1, `$2000-$3FFF`. Read more: design.md, "Memory map".

**`mx_` label.** A label that starts with `mx_` in the runtime, on every instruction that leaves runtime code for game code (`RET`, `RETI` or `JP`). The measuring tool puts breakpoints on them. A new way back to the game needs one, or game time counts as runtime time. Read more: design.md, "The runtime's pages".

**Name table.** The VRAM area that holds the background map: one 2-byte cell for each 8x8 tile position, 64 bytes to a row. Its base address comes from VDP register 2 (`nt_base`). The runtime copies each cell into the Next tilemaps. Read more: design.md, "Display off and on"; nms-format.md, "Writing VRAM from page code".

**Native code.** Z80 or Z80N code that runs directly on the Next, as opposed to an I/O instruction that runs through a trap. A native instruction costs its Z80 T-states plus one cycle for every memory read. Read more: sitescan.md, "Costs".

**NEX.** The Next's executable file format. `nms.nex` is NextMasterSystem as one NEX file. The NEX asks for the 2 MB memory flag. Read more: design.md, "Pages".

**NextReg.** One of the Next's configuration registers, written by number. The docs write them as NextReg `$05` (video rate), `$07` (CPU speed), `$50` to `$57` (MMU). Read more: design.md, "Memory map", "The video rate".

**NextZXOS.** The Next's operating system. The shell uses its file browser and gives control back to it on BREAK. Read more: design.md, the opening section and "Coming back".

**NMI.** The Z80's non-maskable interrupt, which the Master System Pause button triggers. The runtime delivers it to the game's handler at `$0066`. Code: `fw_ula_irq`, `nmi_slot1`. Read more: design.md, "While a game runs".

**No-Intro.** A published list of verified cart dumps with names and CRC32 values. The `META` key `dump` and the spec's region rules for `hz` use its names. Read more: nms-format.md, "`META`: the game's details"; overlays.md, "Switches".

**`notrace`.** Spec line: no trace forms in this overlay. See "Trace". Read more: mknms.py spec lines (`python3 tools/mknms.py --help`).

**Once-a-frame work.** The work the runtime does once in each frame: the copper list, keyboard, map rebuild, tile conversion, priority tiles and sprites. It runs from the ULA interrupt, from a V counter read in the vertical blank, or from a handler exit past the interrupt's line; with the `workline` switch, from a line interrupt in the picture. Code: `vbl_work` in `fw.asm`, `fw2_vbl`. The game's own work in a frame, as in "frame work does not fit in a frame", is a different thing. Read more: design.md, "The once-a-frame work".

**Operation (`PTCH`).** One entry in a `PTCH` chunk: `CHECK`, `PATCH`, `START`, `RAMSITES` or `RASTER`, ended by `END`. The loader reads them twice: the first pass checks, the second applies. Read more: nms-format.md, "`PTCH`: operations".

**Outer shell.** The C part of `nms.nex`: the file browser, the loader, the information screen and the return from a game. The runtime is the other part. Read more: design.md, the opening section.

**Overlay.** The set of changes for one game, stored as an `.nms` file named after the cart's CRC32, in the `ovl` folder next to `nms.nex`. Built from a spec. Also the name of one shell module (`src/shell/overlay/overlay.c`) that finds and applies it. Read more: nms-format.md; overlays.md.

**Overrun.** See "Frame overrun". In `sitescan.py` an overrun finding is an interrupt routine that costs more than a frame. Read more: sitescan.md, "Findings".

**`ovl` folder.** The folder next to `nms.nex` on the SD card that holds the overlay files and `index`. The shell finds it from the folder it was started from. Read more: nms-format.md, opening paragraphs.

**`OVL_BUF`.** The 256-byte buffer at `$A000` through which the loader reads the overlay index and overlay files. No file is ever held whole in memory. Read more: design.md, "Loading an overlay file".

**`PAGE`.** The chunk that holds one code page, with its entry addresses. Read more: nms-format.md, "`PAGE`: code pages".

**Page (Next page).** The Next maps memory in 8K pages. Page numbers in the docs are 8K page numbers. The memory plan gives each page its use. A code page is one page with a use of its own; the docs write "Next page" where "page" alone could mean a code page. Read more: design.md, "Pages".

**`page` block.** A spec block that defines a code page: `page N NAME...` up to `endpage`. The page source is assembled with `sjasmplus` at `$2000`. Read more: overlays.md, "Code pages".

**Page code.** The code in a code page. It must restore the stack pointer, interrupt state, MMU slots and registers before it returns. Read more: nms-format.md, "Rules for page code".

**`PATCH`.** A `PTCH` operation that writes new bytes into the cart image. The bytes stay inside one 8K page of the cart and inside a checked range. A patch holds only bytes that differ from the cart. Read more: nms-format.md, "`PTCH`: operations".

**Pattern rules.** The rules `sitescan.py` runs after the main scan for code shapes that broke or slowed particular games: inline jump tables, mailbox races, column and rectangle streamers, and the Sega planar RLE decoder. Each adds rows of its own kind to the sites file. Read more: sitescan.md, "Pattern rules".

**`pg_tab`.** The table of code pages in the runtime's second page. The loader clears it before it loads an overlay and fills it from each `PAGE` chunk. `far_find` looks up the entry in it. Read more: design.md, "The runtime's pages"; "Loading `PAGE` chunks".

**`plain`.** Spec line: this site keeps its plain inline code and gets no trace form. Read more: mknms.py spec lines (`python3 tools/mknms.py --help`).

**Pointer harvest.** `sitescan.py` takes a code-like address that the code stores into RAM as an entry point, with checks that refuse data values. Harvested code is `medium` confidence. Read more: sitescan.md, "How it works".

**`poke`.** Spec line `poke ADDR OLD NEW` that replaces hex bytes at a cart offset. Use it for data. Code goes in an `asm` block. Read more: overlays.md, "Writing code in a spec".

**Port class.** See "Class".

**Primary CRC32.** The CRC32 of the cart an overlay was made for. It names the overlay file and is the first entry in `CRCS`. Read more: nms-format.md, "Header: 16 bytes".

**Priority tiles.** Background tiles with the priority bit set in their name table cell, which the game wants drawn in front of sprites. The `priority` switch draws them again in Layer 2, above the sprites. Spec line and `CONF` key: `priority`. Code: `pri_frame`, `pri_rebuild`. Read more: overlays.md, "Switches".

**`PSG`.** The Master System's sound chip. The `sitescan.py` port class for it is `psg`. The Next has no PSG; its AY chips play the sound. See "AY".

**`PTCH`.** The chunk that holds the operations that check and change the cart image. Read more: nms-format.md, "`PTCH`: operations".

**`ramhook`, `ramsite`.** Spec lines for `RAMSITES`. `ramhook ADDR` is the `JP nn` at `ADDR` that the game runs after it builds its RAM code. `ramsite ADDR BB` is an I/O instruction with bytes `BB` that the game builds at RAM address `ADDR`. Read more: mknms.py spec lines (`python3 tools/mknms.py --help`).

**`RAMSITES`.** A `PTCH` operation for games that build code in RAM, so its I/O instructions are not in the cart image. It lists RAM addresses, the original bytes (by the low 16 bits of their CRC32) and the new bytes. The runtime patches the RAM when the game reaches the continuation. Spec lines: `ramhook` and `ramsite`. Read more: nms-format.md, "`RAMSITES`".

**`RASTER`.** A `PTCH` operation for games that set horizontal scroll on nearly every line. The file carries a routine, at most 1024 bytes, that works out the scroll value of each line from the game's RAM. The runtime calls it once a frame and builds a per-line copper list; with the `rastseg` switch, in 224-line mode, the routine gives segments and the list sets H only where it changes. Spec line: `rastercode FILE`. Code: `cop_raster`, `cop_seg`. Read more: nms-format.md, "`RASTER`".

**Reached, unreached.** In `sitescan.py`, a byte is reached when a code path from a vector or entry point leads to it. A pattern in unreached bytes may be data. Read more: sitescan.md, "Byte scans".

**Red border.** The signal that NextMasterSystem itself stopped: `jt_fatal` stops with a red border. A far call to a page or entry that the file does not have also stops with one. Read more: readme.txt, "REPORTING A PROBLEM"; nms-format.md, "The far call".

**Region.** The part of the world a cart was released for. It decides the `hz` value: Europe only means 50 Hz, USA or Japan without Europe means 60 Hz, a mix or World means `any`. Read more: overlays.md, "Switches".

**Resident part.** The part of the shell that is always mapped in slots 4 and 5 (`$8000-$BFFF`): start-up code, `main`, far-call code and shared state. Everything handed to the operating system lives there. Read more: design.md, "While the shell runs".

**`RST`.** The Z80 one-byte call to one of eight fixed addresses (`$00`, `$08` to `$38`). A patched I/O instruction becomes an `RST` plus an inline code. The spec's `vector` line writes a `JP` to the runtime at an `RST` address. Read more: nms-format.md, "Inline codes".

**Run (of bytes).** In `jt_vwrite`, a number of consecutive bytes (B) that go to consecutive VRAM addresses. C runs are written, with a source step and a VRAM step between runs. Read more: nms-format.md, "Writing VRAM from page code".

**Run (of outputs).** Consecutive patched output instructions (`OUT`, `OUTI`, `OUTD`) that the runtime handles in one call. A run is kept in the trace cache with its length. A run of only `OUTI` or only `OUTD` goes out as one block. Code: `tr_start`, `out_block`, `TR_RMAX`, `RUN_BREAK_EVEN` in `tools/tracedef.py`. Read more: design.md, "Runs of outputs".

**Runtime.** The Z80 assembly part of `nms.nex`. It runs while a game runs, receives every patched I/O instruction, and drives the Next's tilemap, sprites, copper and sound. It is assembled separately and placed in the NEX as ready-made 8K pages. Its source files and symbols start with `fw` and `jt_`: `fw.asm`, `fw2.asm`, `fw3.asm`, `fw4.asm`, the `fw_` and `jt_` symbols. Read more: design.md, the opening section and "The runtime's pages".

**Runtime parts.** The runtime's pages, named part 1 to part 4. Part 1 is mapped at `$E000` for the whole game. The others borrow a slot while they run: part 2 and part 4 at `$2000`, part 3 at `$0000`. Code: `fw.asm`, `fw2.asm`, `fw3.asm`, `fw4.asm`. Read more: design.md, "The runtime's pages".

**Sega mapper.** The common mapper. Its registers are at `$FFFC-$FFFF`. See "Mapper register".

**Sega planar RLE decoder.** A routine found in many carts that unpacks tile data stored as run-length encoded bitplanes. `sitescan.py` finds its core by byte pattern (`core`, `variant`, `variant-de`) and reports where it runs. Read more: sitescan.md, "Rule 4: Sega planar RLE decoder".

**Shell.** See "Outer shell".

**Site.** A place in the cart that an overlay patches: an I/O instruction, a mapper store or similar. `sitescan.py` lists sites. In a spec a `site ADDR` line turns the I/O instruction at `ADDR` into `RST` plus an inline code. Read more: sitescan.md, "`NAME.sites.tsv`"; overlays.md, "2. Draft a spec".

**`sitescan.py`.** The tool that scans a cart for sites. It is a recursive-descent Z80 disassembler that follows the code from the reset and interrupt vectors. Read more: sitescan.md.

**sjasmplus.** The assembler that `mknms.py` runs on `asm` blocks, `page` blocks and `rastercode` files. A spec without any of those does not need it. Read more: overlays.md, opening paragraphs.

**Slot.** A window of the CPU address space into which memory is mapped. The word has two meanings in these docs. A Next slot is 8K: the 64K space has eight, numbered 0 to 7, each mapped by an MMU register. A cart slot is 16K, on the cart mapper: slot 0 and slot 1 below `$8000`, slot 2 at `$8000-$BFFF`. The docs say "Next slot" or "cart slot" where the text does not already show which. Read more: design.md, "Memory map"; sitescan.md, "How it works".

**Spec.** A text file in `overlays/` (`*.spec`) that lists the changes for one game, one per line, and the settings. `mknms.py` builds the overlay from it and the player's cart. `#` or `;` starts a comment. Read more: overlays.md; `python3 tools/mknms.py --help`.

**Sprite attribute table (sprite table).** The area of VRAM that holds the sprites' positions and tile numbers. The runtime watches for writes to it and rebuilds the Next sprites. Code: `sat_hi`. Read more: nms-format.md, "Writing VRAM from page code".

**SPUN.** The Next's package manager, which installs NextMasterSystem. Read more: README.md, "Download".

**`START`.** A `PTCH` operation: the game starts at this address instead of `$0000`, with this stack pointer (0 means `$DFF0`). Spec line: `start ADDR [SP]`. Needed when the game's reset vector is the only free `RST` vector. Read more: nms-format.md, "`PTCH`: operations".

**Status.** The overall state of a game: `working`, `imperfect`, `not working` or `untested`. `META` carries it and the information screen shows it. Read more: nms-format.md, "`META`: the game's details"; readme.txt, "THE GAMES".

**Streamer.** In `sitescan.py`, a loop that writes the VDP control port at least twice and the data port at least once in a pass and moves an address by `$40` (one name table row): a column or rectangle writer. Rule 3 of the pattern rules reports them. Read more: sitescan.md, "Rule 3: column and rectangle streamers".

**Switch.** A spec line that turns on a runtime feature that costs time or memory and helps only some games: `priority`, `toppal`, `tilecache`, `hsplit`, `collline`, `rastseg`, `workline`, `hz`. `mknms.py` writes it into `CONF`. Measurement decides which overlays turn which on. Read more: overlays.md, "Switches".

**Task switch.** A `RET` that runs after the game loaded SP with a value the scanner does not know, so it returns to an address on another stack. Task schedulers do this. The scanner does not follow it. Read more: sitescan.md, "How it works".

**Tile.** An 8x8 pixel picture used by backgrounds and sprites. The Master System stores a tile as bitplane bytes; the Next uses its own tile definitions. Read more: design.md, "The once-a-frame work" (tile conversion).

**Tile conversion.** Turning Master System tile data written to VRAM into Next tile definitions. A write to tile data marks the tile in `dirty_pages`; the once-a-frame work converts the marked tiles. Code: `tile_flush`, `tflush2`, `tw_flush`. Read more: design.md, "The once-a-frame work".

**Tile cache (`tilecache`).** The feature, with its spec line and `CONF` key `tilecache`. Tiles that a block write copies whole from cart ROM are copied from the converted cart, made at game start, and not converted again. It costs loading time and memory. Code: `tc_build`, `kn_entry`, `kn_block`, `CONVT_PAGE`. Read more: overlays.md, "Switches"; design.md, "The once-a-frame work".

**Tilemap.** The Next's background hardware. The runtime keeps the two maps M0 and A8 in a page it borrows from NextZXOS (`MAP_PAGE`) and fills them from the name table. Read more: design.md, "Pages".

**Tools.** `tools/sitescan.py` scans a cart. `tools/mkspec.py` drafts a spec from a scan. `tools/mknms.py` builds one `.nms` file from a spec and a cart. `tools/mknmsindex.py` builds `ovl/index`. `tools/build-overlays.py` builds a folder of specs and the index. `tools/tracedef.py` decides which sites get trace forms. `tools/gentables.py` regenerates the runtime's tables. `tools/check-layout` checks size and alignment rules at build time. Read more: README.md, "Overlay files"; overlays.md.

**`toppal`.** Spec line and `CONF` key. Shows the palette that the frame handler leaves from line 0 of the picture, for games whose frame handler writes the palette late. A display-off write between the frame event and the first line event is held until the picture would show it. Code: `pal_ph`, `dis_pend`. Read more: overlays.md, "Switches"; design.md, "Display off and on".

**Trace.** A copy of the game's code around a site, run by the runtime in a buffer, with each patched output turned into a call that appends its byte. The bytes then go to the port in one block. Used for runs and loops of outputs. Code: `tr_start`, `tr_build`; `tools/tracedef.py`. Read more: design.md, "Runs of outputs"; the header of `src/runtime/trace.asm`.

**Trace build.** `make TRACE=1`: a build of the runtime with extra checks for test tools, such as the VDP check that counts interrupt handlers that change the VDP address in the middle of a data stream. Not for release. Read more: design.md, "The trace build".

**Trace cache.** The table (in memory page `TRC_PAGE`) of what the runtime decided for each trace site: a copy, a run, or that the site runs as a single output. Code: `TRC_PAGE`, `tr_store`, `tr_newcode`. Read more: design.md, "Runs of outputs".

**Trace form.** The variant of a site's inline code that asks for a trace (`$18 + class`, `$C3`, `$CB`, `$81 + 8r`). `mknms.py` gives a site the trace form only when the spec has an `io` vector and the runtime can do more with the site than a single output. Read more: mknms.py spec lines (`python3 tools/mknms.py --help`); design.md, "Runs of outputs".

**Trap.** What a patched I/O instruction does: it runs through an `RST` into the runtime, which does on the Next what the instruction did on the Master System. A trap takes hundreds to thousands of Next cycles, against a few T-states on a Master System. A site that runs alone through a trap, with no trace form, is a single output. Read more: sitescan.md, "Frame cost model"; design.md, "Runs of outputs".

**ULA.** The Next's original Spectrum video chip. Its interrupt (line 248 at 50 Hz, line 224 at 60 Hz) starts the once-a-frame work, unless the overlay sets a work line. The browser and information screen use the ULA screen. Read more: design.md, "The video rate"; "The information screen".

**`Unknown game`.** The message the shell shows when it has no overlay for the cart, or the file is a different dump from the one the overlay was made for. It names the file it looked for. Read more: readme.txt, "HOW TO START".

**Unproven store.** In `sitescan.py`, a store through HL, DE, BC, IX or IY, or a block copy, whose address the scanner could not prove to stay off the mapper registers. Listed in `NAME.unproven.tsv`. Read more: sitescan.md, "`NAME.unproven.tsv`".

**V counter.** The VDP register a game reads from port `$7E` for the current line. The runtime returns a count that matches a PAL Master System at 50 Hz and an NTSC one at 60 Hz. Code: `vc_count`, `rd_vcount`, `vc_fast`. Read more: design.md, "The video rate".

**VDP.** The Master System's video chip. Games talk to it through I/O ports: a control port, a data port and a status port. The runtime keeps its state in software (`vdp_latch`, `vdp_code`, `vdp_addr`, `vdp_rbuf`, `vdp_status`, `vdp_regs`) and draws with the Next's hardware. Read more: overlays.md, "Names that every block knows".

**`vector`.** Spec line `vector ADDR KIND` that writes a `JP` to a runtime entry at `RST` address `ADDR`. Kinds: `out_n`, `in_n`, `ed`, `ld_de_a`, `outi_run`, `io`. Read more: mknms.py spec lines (`python3 tools/mknms.py --help`).

**VRAM.** The VDP's 16K of video memory: tile data, the name table and the sprite attribute table. The runtime keeps the VRAM copy. Read more: nms-format.md, "Writing VRAM from page code".

**VRAM copy.** The runtime's copy of the Master System's 16K VRAM, kept in memory pages 28 and 29. Tile conversion reads from it. Code: `SHADOW_PAGE`. Read more: design.md, "Pages".

**Walk.** The loader's first pass over an overlay file, from the start to `END `, in which every byte goes through a running CRC32 and each `PAGE` chunk is loaded where it is found. Read more: design.md, "Loading an overlay file".

**Work line (`workline`).** The switch, with its spec line `workline N` and `CONF` key `workline=N`, that moves the once-a-frame work from the ULA interrupt below the picture to a line interrupt at SMS line N of the picture. For a game whose frame handler must reach a line of the next picture on time. Code: `wl_ula4`, `wl_line4`, `wl_setup` in `fw4.asm`. Read more: overlays.md, "Switches"; design.md, "The once-a-frame work".

**Z80N.** The Next's CPU: a Z80 with extra instructions. The game's own code runs on it unchanged. Code pages may use any Z80N instruction. Read more: nms-format.md, "`PAGE`: code pages".

**z88dk.** The C and assembler toolchain that builds `nms.nex`: `zcc` compiles the shell and `z88dk-z80asm` assembles the runtime. Read more: design.md, "How the build fits together".
