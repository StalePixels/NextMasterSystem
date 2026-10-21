# sitescan

`tools/sitescan.py` finds the places in a Master System cart that a NextMasterSystem overlay has to patch. [overlays.md](overlays.md) shows where it fits in making an overlay. It is a recursive-descent Z80 disassembler: it starts at the reset and interrupt vectors, follows every jump and call it can prove, and reports:

- every `IN`, `OUT` and block I/O instruction, with its port and what that port does on an SMS;
- every store that reaches the Sega mapper registers ($FFFC-$FFFF), and every Codemasters-style store ($0000, $4000, $8000);
- stores through a register whose address it cannot prove to stay off $FFFC-$FFFF, in a separate list;
- `RST` instructions and the vectors they use;
- `LDIR`/`LDDR` copies from ROM into RAM, and any I/O in copied code that runs;
- jump tables it read, indirect jumps it could not resolve, and calls into a banked cart slot with a bank it could not work out;
- `IN`/`OUT` byte patterns in bytes that no path reached, each rated by how much the bytes around it look like code;
- mapper store byte patterns in bytes that no path reached, each rated by how much the bytes around it look like code;
- how many bytes it classified as code;
- a frame cost model: how many Next cycles each routine takes on the runtime, which foreground routines can be cut by the interrupt handler while they write the VDP, and which interrupt routines take longer than a frame;
- pattern rules: code shapes that broke or slowed particular games on the Next (inline jump tables, mailbox races, column and rectangle streamers, the Sega planar RLE decoder, H scroll from a table in the interrupt handler).

It uses only the Python 3 standard library. Run it with `python3 -I`.

## Running it

```sh
python3 -I tools/sitescan.py CART.sms --out OUTDIR [options]
```

Options:

| Option | Meaning |
|---|---|
| `--entry ADDR` or `--entry BANK:ADDR` | Extra entry point. ADDR and BANK are both hex: bank 10 is `A:8000`. Repeat it for more. Use it for the unresolved indirect jumps the summary lists. `BANK:ADDR` places code in slot 2 (or slot 1) with that bank. A bank beyond the cart's last bank stops the scanner with an error, because it is almost always a bank number written in decimal. |
| `--log FILE` | A dynamic log: `*.io.tsv`, `*.mapper.tsv` or `*.features.json`, described below. Repeatable. |
| `--logdir DIR` | Every `*.io.tsv`, `*.mapper.tsv` and `*.features.json` in DIR. |
| `--cdl FILE` | A Mesen2 code/data log (`CDLv2`). |
| `--mapper auto\|sega\|codemasters` | Mapper model. `auto` (the default) uses the Codemasters model only when the cart has proven Codemasters-style stores and no proven Sega mapper store. |
| `--name NAME` | Prefix for the output files. Default: the cart file name. |
| `--no-harvest` | Do not use code addresses found in stores to RAM, bank calls or bank headers as entry points (see below). |
| `--unroll N` | Distinct register states kept per instruction before they are merged. Default 8. |
| `--no-tracedef` | Run without `tracedef.py`. By default the scanner imports `tracedef.py` from the folder that holds `sitescan.py` and stops with an error when it is missing. With this flag the trace and run forms are not costed, so the costs differ from the overlay builder's; the summary says so. |
| `--handler ADDR` or `--handler BANK:ADDR` | The game's own interrupt handler entry, hex, for the frame cost model, when $0038 reaches it only through RAM or a table. It is also scanned as an `--entry`. Repeatable. |

The output does not depend on the Python hash seed: the same cart and options give the same files on every run. Keep `tracedef.py` next to `sitescan.py` if you copy the script.

A 512-byte copier header is skipped when the file size is 512 more than a multiple of 16 KB, as `mknms.py` does.

Example, a cart with a dynamic log:

```sh
python3 -I tools/sitescan.py game.sms --log game.io.tsv --out scan --name game
```

### Dynamic logs

A dynamic log is a list of PCs that an emulator saw the game run. The scanner reads three kinds, by file name:

- `*.io.tsv` and `*.mapper.tsv`: tab-separated, with a header line. The `pc` column is the PC in hex. An optional `insn_bytes` column holds the instruction's bytes in hex; when it is there, the scanner checks them against the cart. An optional `cart_offset` column holds the cart offset, in hex, that the PC ran from; it names the bank. A row with no `cart_offset` is used only for a slot that the cart does not bank: slot 0 with the Sega mapper, and slot 1 when the cart never writes $FFFE. In any other slot (slot 2 always, and every slot with the Codemasters mapper) the address alone does not say which bank ran, so the row is skipped, and the summary counts the skipped PCs for each log.
- `*.features.json`: any JSON. Every string in a list under the key `example_pcs` or `ram_code_writer_pcs` is a PC in hex. A list `example_offsets` or `ram_code_writer_offsets` of the same length next to it holds each PC's cart offset in hex, or an empty string; a PC with no offset follows the rule for rows with no `cart_offset`.

Dynamic logs and CDL files only add entry points. The scanner first runs without them; afterwards it adds only the logged PCs that the static pass did not already reach from the vectors and the `--entry` points (`static_starts_of()` in `sitescan.py`). Code that only harvested addresses, bank calls, bank headers or object handler entries reach counts as not reached here, so a logged PC in it is still a log seed. A logged PC that the static pass did reach still counts as evidence: the code that plain flow reaches from it, through calls but not through table entries, is `high` (`log_confirmed()`). A log row whose instruction bytes differ from the cart's bytes at that PC is dropped, and the summary says how many were dropped. A log from another cart therefore does nothing harmful, but `--logdir` on a directory that holds several carts' logs will still read them all.

## Output files

All files go to `--out`, named after `--name`.

### `NAME.sites.tsv`

One row per site, tab-separated, with a header line. This is the file an overlay builder reads.

| Column | Content |
|---|---|
| `addr` | CPU address of the instruction. For code run from RAM, the RAM address. |
| `bank` | 16 KB cart bank the instruction is in, or `ram`. |
| `offset` | Cart offset of the instruction (header skipped). For code run from RAM, the offset of the copy's source bytes, which is where a patch goes. |
| `bytes` | Instruction bytes. |
| `insn` | Disassembly. |
| `kind` | See below. |
| `target` | Port, store address and value, call target, table base, as the kind needs. |
| `class` | Port function on the SMS, or a short label for other kinds. |
| `confidence` | `high`, `medium`, `low` or `very-low`, see below. |
| `how` | How the scanner reached the instruction, see below. |
| `note` | Extra detail. |

Kinds:

| Kind | Meaning |
|---|---|
| `out`, `in` | `OUT (n),A`, `IN A,(n)`. |
| `out_c`, `in_c` | `OUT (C),r`, `IN r,(C)`. `target` is the value of C, or `unresolved`. |
| `block_out`, `block_in` | `OUTI`, `OTIR`, `OUTD`, `OTDR`, `INI`, `INIR`, `IND`, `INDR`. Port from C, as above. |
| `mapper` | A store proven to reach $FFFC-$FFFF. `target` is `register<-value`. |
| `codem_store` | A store proven to reach $0000, $4000 or $8000. In a Sega-mapper cart a store to $8000 can also be a cart RAM write. |
| `cartarea_store` | Another proven store into $0000-$BFFF. |
| `rst` | An `RST` instruction. `rst_vector` rows describe each vector used. |
| `ram_copy` | `LDIR`/`LDDR` from ROM to $C000-$FFFF with proven source, destination and length. `class` is `code` when a call or jump into the copy was found. |
| `ram_exec` | A jump or call into RAM with no known copy covering it. |
| `jump_table` | A table the scanner read. `note` lists the entries. |
| `indirect_resolved`, `indirect_unresolved` | `JP (HL)`, `JP (IX)`, `JP (IY)`, or a `RET` to a pushed address, resolved or not. |
| `bank_unresolved` | A jump or call into slot 2 (or a banked slot 1) with an unknown bank. The target was not followed. |
| `target_unresolved`, `inline_unresolved` | Other transfers not followed; calls to a routine that skips a variable amount of inline data after the call. |
| `inline_string` | A call to a routine that returns past a zero-terminated string after the call. The scan goes on after the zero byte. `target` is the routine, `note` the string length. |
| `io_unreached` | `D3 n`, `DB n` or an `ED` I/O opcode in bytes no path reached, found by the byte scan (see below). `note` lists the evidence. |
| `mapper_unreached` | A mapper store byte pattern in bytes no path reached, found by the byte scan (see below). `target` is the spec line form that patches it: `mapst`, `mapsthl`, `mapstbc`, `mapstde`, `mapld`, `mapldk` or `codem`. `note` lists the evidence. |
| `inline_table` | Pattern rule 1: a call of an inline table dispatcher. `target` is the table start, `class` the dispatcher, `note` the entries and why the table ends. |
| `mailbox_race` | Pattern rule 2: the second of two foreground stores to a mailbox byte. `target` is the mailbox address. |
| `streamer` | Pattern rule 3: the head of a loop that streams a column or rectangle to the VDP. `target` is the routine. |
| `rle_decoder` | Pattern rule 4: a copy of the Sega planar RLE decoder core. `target` is `core`, `variant`, `variant-de` or `jr-z`. |
| `raster_hscroll` | Pattern rule 5: interrupt code that reads the H scroll value from a table. `target` is the interrupt routine, `class` `pointer` or `patched address`. |

Port classes follow the SMS decoding of address lines A7, A6 and A0: `memory_control`, `io_control`, `unmapped_read`, `psg`, `v_counter`, `h_counter`, `vdp_data`, `vdp_control`, `vdp_status`, `joypad_a`, `joypad_b_misc`, `no_effect` (a write to $C0-$FF), `fm_address`, `fm_data` and `fm_control` for writes to $F0-$F2, and `fm_detect` for a read of $F2.

Port and value notes in `target`: a plain value was proven inside the routine. `(callers)` means the routine receives the value from its callers and every known caller passes it. `(partial)` means some callers pass it and for others it is unknown.

Confidence and `how`:

- `high`: reached by proven control flow from the vectors or a `--entry` (`how` is `static`), or from a dynamic log or CDL entry point (`log-seed`, `cdl-seed`).
- `medium`: reached only through something the scanner inferred: a jump table whose length it guessed (`+table`), an address harvested from a store to RAM (`pointer-harvest`), a call after a bank switch that no path reached (`bank-call`), a module header at the start of a bank (`bank-header`), or an object handler address stored into a handler field (`handler-table`, `handler-store`, `handler-spawn`).
- A `medium` site is raised to `high` when the byte scans rate it `high` with the code that only `medium` paths reach left out: evidence adds up, it never lowers a rating. `how` then ends in ` + byte pattern`, and `note` holds the byte scan evidence.
- `io_unreached` and `mapper_unreached` rows have their own scale, described under "Byte scans". The `how` of an `io_unreached` row is `byte pattern in bytes no path reached`; of a `mapper_unreached` row, `byte scan, no path reached it`.
- `+seen-in-log` is added when a dynamic log also has that instruction: the same cart offset, or, for a row with no `cart_offset`, the same PC outside slot 2. Such a row is `high` whatever path reached it: the reference ran that instruction.
- `+log-reached` is added when plain flow from a logged PC reaches the instruction, and the row is then `high` (see "Dynamic logs").

### `NAME.unproven.tsv`

Stores through HL, DE, BC, IX or IY, and block copies, whose address the scanner could not prove to stay off $FFFC-$FFFF. Columns: `addr`, `bank`, `offset`, `bytes`, `insn`, `address` (what is known about the address), `reason`, `how`. A store is left out of this list when its address is proven, when the high byte of the address register is known and the page cannot be $FF, when the address is a known base plus an index whose range cannot reach $FFFC, or when the address is a slot in the routine's own stack frame (`IX` set from `SP`, as SDCC does).

### `NAME.summary.txt`

The same results, readable: the constant banks the code writes to $FFFE and $FFFF, I/O sites by port function, mapper and Codemasters stores, unproven-store counts by reason and register, RST vectors, RAM copies, tables, unresolved transfers, harvested entry points (with the instruction that stored each one), object handler entries (with their kind and the store or call each came from), bank call entries (with the bank switch before each one), bank header entries, harvested addresses that were rejected, paths that stopped on bytes that do not look like code, overlapping decodes, unreached I/O patterns, mapper stores found by the byte scan, coverage per bank, a comparison with the dynamic logs when logs were given, and the frame cost findings (below).

### `NAME.cost.tsv`

One row per routine from the frame cost model (see "Frame cost model" below), costliest first.

| Column | Content |
|---|---|
| `entry`, `bank`, `offset` | The routine's entry. |
| `context` | `irq`: the interrupt vectors and the routines they call on paths that return; `fg`: foreground; `both`: called from both. |
| `iff` | Interrupt enable state at entry: `on`, `off`, `mixed` or `unknown`. |
| `vdp` | `data` and/or `control` when the routine's own instructions write those VDP ports. |
| `returns` | `no` when no path returns; the cost then follows every path to where the flow ends. |
| `cost_lo`, `cost_hi` | Next cycles of one call on its costliest path. The range comes from VDP data writes to an unknown VRAM region. |
| `frames` | `cost_hi` divided by the Next frame. |
| `count` | `known`: every loop count on the path is known; `partial`: known for the callers the scanner found, but some callers pass values it does not know; `unknown`: some loop count is unknown and that loop counts as one pass. |
| `args` | The entry values from a caller that give the cost, when loop counts come from the caller. |
| `loops` | The routine's outer loops: head address, `x` count (`?` unknown), cost of one pass. |

### `NAME.dis.txt`

The disassembly of everything reached, sorted by cart offset, with site kinds marked. A blank line separates runs of code that are not contiguous.

## How it works

The scanner works routine by routine. A routine starts at a vector, a call or `RST` target, a table entry, a command-line or log entry point, or a harvested address. Inside a routine it runs a data-flow analysis over the instructions it reaches, keeping an abstract value for every register:

- a constant;
- "the value this register had when the routine was entered", which is later resolved through the routine's callers;
- addresses built from a table base: base plus an unknown index, base plus an index of known range, a byte or word read from such a table, or the routine's own return address;
- for an unknown byte in A, the range of values it can have and the RAM byte or structure field it was loaded from, which give table lengths (below);
- the stack, byte by byte, relative to SP at routine entry. `PUSH`, `POP`, `EX (SP)`, `INC SP`, `DEC SP`, `ADD HL,SP`, `LD SP,HL` and `LD SP,IX` keep it in step. Bytes above the return address are the caller's stack arguments, which are resolved at each call site the same way as register arguments. This covers SDCC code, which passes arguments on the stack and reads them through an `IX` frame or by popping past the return address.

Constants come from immediates, from arithmetic on constants, and from reads of ROM at a constant address. Up to `--unroll` distinct states are kept per instruction before they are merged, so short counted loops are followed pass by pass. `DJNZ` with a known B follows only the branch that is taken. In the same way, with A a constant, a conditional jump, call or return follows only the branch that A takes when the condition is the carry flag after `CP n`, `SUB n` or `ADD A,n`, the zero flag after `BIT 7,A`, or the sign flag after an instruction that sets it from A (`refine_a()`).

Each routine gets a summary: whether it returns, whether it skips inline bytes after the call, which registers it keeps, sets to a constant, or computes from its caller's registers, and whether it is a table dispatcher. Calls use the callee's summary. Because summaries depend on each other, the whole scan repeats until nothing changes, or until a round repeats an earlier one (this happens when a table read longer in one round decodes code that cuts it shorter in the next; the summary says so).

Control flow it follows:

- `JP`, `JR`, `CALL`, `RST`, `DJNZ`, conditional forms, `RET`, `RETI`, `RETN`.
- `PUSH` of a constant followed by `RET` (a jump), and a routine that adjusts its own return address with `EX (SP),HL` (inline arguments after the call).
- The code after a call that returns with no inline bytes is reached as surely as the call itself, also when the callee was resolved in more than one bank or through its callers.
- `JP (HL)` with HL a constant, a word read from a table at a constant base, a table address passed in by the caller (the table is read at each call site), or the return address (an `RST` or `CALL` followed by an inline table). Both the 16-bit form (`ADD HL,DE`) and the 8-bit form (`ADD A,L / LD L,A / ADC A,H / SUB L / LD H,A`) of "base plus index" are recognised. The 8-bit form also works when HL holds the table address as a constant and A an unknown index, as in a table helper that the caller enters with `LD HL,table; JP helper`, or the same instructions written inline.
- `JP (HL)` with HL a word read from a table whose base the code keeps in a RAM variable (`LD HL,(nn)`, then the index added and the word read). The table is read at each constant base that the code stores into that variable (`LD (nn),HL` and the other pairs), and at the constants stored into another variable whose word is copied into it (`ram_bases()`). Such a read is not capped at 256 words: the tables for each value of the variable often lie in one run, and the read ends by the usual table rules. The constants of one variable are found in the code the previous round reached.
- A call to a routine that returns past a zero-terminated string after the call (`zstr_skipper()`): the routine takes its return address into HL, reads bytes with `LD A,(HL); INC HL; OR A` (or `AND A`) and `JR Z` or `JP Z` to an exit, and the exit puts HL back as the return address (`EX (SP),HL` then `RET`, with `DI` or `EI` around them) or jumps to it (`JP (HL)`). The scan goes on after the first zero byte that follows the call, and the string bytes count as table bytes. Text printers are written this way.
- `JP (HL)` into a list of `JP nn` or `JR d` instructions, as compiled `switch` statements use.
- A `JP (HL)` or `RET` to "base plus unknown offset" that is not a table: the scanner continues at the base, which covers entry into unrolled code such as a chain of `OUTI` or `LDI`.
- A helper whose `JP (HL)` jumps to the caller's HL: each caller's HL becomes a call target.

A table's length comes from the code's own evidence, in this order:

1. The range of the index. For an unknown value in A the scanner keeps the range of values it can have on each path. A compare (`CP n`, `SUB n` or `ADD A,n`, then a jump, call or return on the carry flag), a bit 7 or sign test (`BIT 7,A`, `OR A` and the like, then a jump on the zero or sign flag) and a mask of the low bits (`AND $1F`) narrow it. The range follows the index through `ADD A,A`, `ADD A,n`, `SUB n`, `INC A`, `DEC A` and `RLCA`, and into the table address: `LD C,A; LD B,0; ADD HL,BC`, `LD L,A; LD H,0; ADD HL,DE`, the 8-bit form, and a helper that reads the table with the caller's A as the index. Fantasy Zone II's sound driver takes a command byte $81-$BB (`BIT 7,A`, `CP $BC`, `SUB $81; RET M`), so its sound tables have 59 entries.
2. The largest value the code stores into the index variable. When the index is a byte loaded from RAM (`LD A,(nn)`) or a field of a structure (`LD A,(IX+d)` or `(IY+d)`, any structure), the table has an entry for each index up to the largest value written by the stores into that variable that a path reached (`index_stores()`): `LD (nn),A`, `LD (IX+d),n` and the other byte stores, and `LD (nn),rr`, with constant values or values of known range. A store of an unknown value, or `INC`, `DEC`, a shift, `SET` or `RES` on the variable, gives no limit. Astro Warrior stores only 0 to 4 in its object state field (IX+$20), so each state table has at most 5 entries.
3. The table's contents. The read ends at the first entry that is not a code address, does not decode as a few valid instructions, or points into the table; where the table reaches the lowest target above its start; at a position that was an instruction start in the previous round; or where another table that the code reads starts. Such a table start is a constant base that the code reads with an index of known range added, directly or through a helper that reads at the base its caller passes (`note_table_base()`).

The first two give an upper limit (`table_cap()`), and the third ends the read within it. A first entry that is not valid is skipped once, for tables indexed from 1. The limits from the code apply to a `JP (HL)` through a word read from a constant base (`word` tables). A table passed to a dispatcher in a register (`arg-` tables) takes the limit of rule 1 at each call site where the caller narrows the index register with a mask or a compare, as in `AND $0F; LD HL,table; CALL dispatcher` (`arg_table_cap()`). A constant index at the call site gives no limit: it names the entry that call takes, not the size of the table. A table whose base the code keeps in RAM and a handler table end by their contents only. Everything reached only through a table is `medium` confidence.

Banks: cart slot 0 is always bank 0. Cart slot 2 starts unknown at the vectors and takes the value written to $FFFF (or to $8000 in the Codemasters model). The mapper decodes only the bank bits that the cart size needs and ignores the others, so the scanner reduces a constant bank value the same way before it uses it (`Scanner.bank_number()`): $8F written to $FFFF selects bank 15 of a 16-bank cart, and $81 written to $FFFE is bank 1, so slot 1 does not count as switched. A jump or call into $8000-$BFFF goes to that bank when the value is a constant, or to each bank the callers pass when the routine receives it. Code that is itself in slot 2 assumes its own bank. Slot 1 is taken as bank 1 unless the cart writes $FFFE (or $4000 in the Codemasters model) with another value or an unknown one; after that slot 1 is tracked the same way as slot 2.

Code copied to RAM: an `LDIR`/`LDDR` with a proven ROM source, RAM destination and length is recorded. A source wholly in slot 0 needs no known bank, and one wholly in slots 0 and 1 needs only the slot 1 bank. A jump or call into that RAM range is decoded from the copy's source bytes, at the RAM address.

Task switches: a `RET` that runs after `LD SP,HL`, `LD SP,IX`, `LD SP,IY` or `LD SP,(nn)` loaded SP with a value the scanner does not know goes to an address on another stack. Task schedulers switch tasks this way. The scanner does not follow such a `RET`; it lists it with the unresolved indirect jumps, with the `LD SP` instructions of its routine.

Pointer harvest: a constant code-like address that the code stores into RAM ($C000-$FFFF), with `LD (nn),HL` and similar, or as two byte stores into a structure field that some `JP (HL)` in the cart jumps through, becomes an entry point. In a cart with a task switch, the entries of a word table in ROM also become entry points when the code stores a word read from that table into RAM: a task scheduler starts a task by putting its start address, from a table of task entry points, on the task's stack. The table is read as a jump table is. Outside carts with a task switch, a table word stored to RAM is usually a data pointer, so it is not harvested. A harvested address is refused when the store writes several different values, when both bytes are equal ($0909 and the like), when the target starts with $FF, or when the bytes at the target do not decode as at least two valid instructions. After a scan, a harvested entry is dropped again if the code reached from it hits an invalid opcode, a jump into RAM or slot 2 that cannot be resolved, or an I/O port SMS games do not use. A task entry from a table is not dropped for a jump or call into RAM, because games call code they copied to RAM. A harvested entry whose store is in code that no path reaches any more, such as the code of an entry dropped this way, is dropped as well. Harvested code is `medium` confidence.

Bank calls: in slot 0 or slot 1, the bytes `LD A,n`, then `LD ($FFFF),A`, then `CALL nn` or `JP nn` with nn in $8000-$BFFF, at a place no path reached, make nn an entry point in the bank that n selects (`$8A` is bank 10 of a 16-bank cart). A `LD (nn),A` to RAM between the first two (a copy of the bank number) is allowed. Games start a module this way from a handler that is reached only through RAM. Only this exact byte form is found.

Bank headers: a bank that starts with two or more `JP nn`, every nn in $8000-$BFFF, is a module with its entries at the start of the bank. Each of those `JP` instructions is an entry point in that bank, whatever way the caller picks the bank.

The target of a bank call or a bank header entry must decode as at least two valid instructions; a `JP nn` there is followed to nn, so a header entry counts. Both kinds go through the same checks as harvested entries after a scan, and are `medium` confidence.

Object handlers: many games keep their objects in records in RAM. Each record has a handler field, a word that holds the address of the routine that updates the object, and a dispatcher runs each object by jumping through that field. A handler field is found from the dispatcher: an offset d such that code a path reached does `LD L,(IX+d)` and `LD H,(IX+d+1)` (IX or IY, in either order) right before `JP (HL)`, or the same loads into E and D right before `EX DE,HL; JP (HL)` (`handler_fields()` in `sitescan.py`). The handler addresses then come from the code that stores into a handler field: a store of the low byte, `LD (IX+d),r` or `LD (IX+d),n`, and a store of the high byte to d+1 through the same index register, in either order and at most four straight-line instructions apart (`handler_entries()`). What the two stores write decides the entry:

- `handler-store`: a constant word, as `LD (IX+d),n` twice or the two halves of `LD HL,nn`. The word is the handler.
- `handler-table`: a word read from a table in ROM with an index added, as in `LD HL,table; ADD HL,BC; ADD HL,BC; LD A,(HL); INC HL; LD A,(HL)`. Every entry of the table is a handler. The table is read as a jump table is, so its length is detected from its contents, not guessed from a count: it ends at the first entry that is not a code address or does not decode as valid instructions, at an entry that points into the table, where the table reaches the lowest entry address above its start, at an entry position that is the start of code, or where another table that the code reads starts. A call of a routine that jumps to the caller's HL, with HL a word read from such a table, also makes every entry of the table a handler.
- `handler-spawn`: a register pair that the storing routine received from its callers, as in a spawn routine that stores DE. The constant that each caller loads into the pair, such as `LD DE,handler; CALL spawn`, is a handler.

A handler runs later, from the dispatcher, so the slot 1 bank at the store does not say which bank it is in. When the slot 1 bank is unknown there and the code writes one constant bank to $FFFE and no other, a handler in slot 1, and the slot 1 bank at the start of each handler, is that bank. A handler in slot 2 is taken in the bank that slot 2 holds at the store. A handler address is refused when both its bytes are equal, when the target starts with $FF, or when the bytes at the target do not decode as at least two valid instructions. After a scan, a handler entry is dropped on the same signs of data as a harvested entry. Handler code is `medium` confidence. Entries found from handlers' own stores add more handlers in the next round, as harvested entries do. The summary lists each handler entry with its kind and the store or call it came from.

Bytes that are not code: a path stops at an invalid opcode, at `RST $38` followed by $FF (erased fill), at a literal store into $0000-$7FFF other than $0000 and $4000, and at `LD SP,nn` with nn in ROM. The summary lists each place a path stopped and why.

### Byte scans

After the flow scan, the scanner looks at every byte of the cart, in every bank, for I/O instructions and mapper stores that no path reached, and rates each one by how much the bytes around it look like code.

#### Mapper stores

A mapper store that no path reaches is not patched, and on the Next it then writes RAM: the bank does not change, and the game reads the wrong bank later, often minutes into play. Code the flow scan misses is common in commercial games. The scanner looks for these patterns:

| Bytes | Instruction | Spec line |
|---|---|---|
| `32 nn FF`, nn $FC-$FF | `LD ($FFnn),A` | `mapst` |
| `22 nn FF`, nn $FC-$FE | `LD ($FFnn),HL` | `mapsthl` |
| `ED 43 nn FF`, `ED 53 nn FF`, nn $FC-$FE | `LD ($FFnn),BC`, `LD ($FFnn),DE` | `mapstbc`, `mapstde` |
| `21 nn FF 36 n`, nn $FC-$FF | `LD HL,$FFnn; LD (HL),n` | `mapld` ($FFFF), `mapldk` |
| `32 00 nn`, nn $00, $40 or $80, Codemasters model only | `LD ($nn00),A` | `codem` |

A pattern whose first byte a path reached as an instruction is skipped: the flow scan has classified it. Every other hit becomes a `mapper_unreached` row, rated by this evidence:

- a setter: the instruction just before the store loads the register it stores, in a way games do before a bank switch. For A that is `LD A,n`, `LD A,(HL)`, `LD A,(DE)`, `LD A,(BC)`, `LD A,(IX+d)`, `LD A,(IY+d)`, `LD A,(nn)` from RAM, `POP AF`, or `LD (nn),A` to RAM (a copy of the bank number). For HL, BC and DE it is `LD rr,nn`, `LD rr,(nn)` or `POP rr`. Up to two `NOP`, `LD A,A` or `EX (SP),HL` (not for HL) between the two are skipped. Another mapper store pattern that ends within three bytes before the store also counts. The `LD HL,$FFnn; LD (HL),n` pattern carries its own setter;
- a jump target: a `JP nn` or `CALL nn` (plain or conditional) somewhere in the cart has the store's address as its target. For a store in bank 2 or above, only references from the same bank count;
- code before it: the 32 bytes before the store decode as a chain of valid instructions that ends exactly at the store;
- code after it: the store and up to five more instructions decode as valid instructions, up to the first unconditional jump or return. An invalid opcode, an instruction `implausible` to be code (a store into ROM, `LD SP` into ROM) or `RST $38` followed by $FF fails this test.

The rating:

- `low` when the pattern overlaps code that a path reached at another instruction boundary, when it lies in a jump table the scanner read, or when the code after it is not valid;
- otherwise `high` when it has a setter or is a jump target;
- otherwise `low` when four or more of the instructions in the chains before and after it are `RST` or `NOP`. Tile data and zero padding decode that way;
- otherwise `medium` when the 8 or more bytes before it decode as code;
- otherwise `low`.

`mkspec.py` makes a spec line from each `high` row and a `CHECK` comment from each other row. A `high` row is still a byte pattern: before an overlay ships, read the code around it in the cart. A `medium` row is usually code with a setter the list above does not know, such as `LD A,C`.

#### I/O instructions

The I/O byte scan looks for `D3 n` (`OUT (n),A`), `DB n` (`IN A,(n)`) and the `ED` I/O opcodes. A pattern is skipped when either of its bytes was reached as code, or when it lies in a jump table that was read. Every other hit becomes an `io_unreached` row, rated with the same evidence and the same scale as a mapper store, with these differences:

- the setter is checked only for `OUT (n),A`: the instruction before it loads A, as in the mapper store list;
- a jump target also counts a `JR`, `JR cc` or `DJNZ` that targets the instruction, and any branch that targets a one-byte instruction just before it, which then runs on into it. Games branch into the operand of an instruction this way: the operand byte runs as a one-byte instruction and falls into the `OUT`. Branches are decoded at every byte, so data can supply one;
- a hit that would be `high` only because it is a jump target, with no setter and fewer than 8 bytes of valid code before it, is `medium`;
- an `OUTI` is `high` when an unbroken run of `OUTI` after it, in the same bank, leads to an `OUTI` that a path reached. A game enters an unrolled `OUTI` block at an address it computes from the byte count, so the `OUTI`s before the first entry that was reached are code too;
- a port SMS games do not use is always `very-low`. The ports SMS games use are $BE, $BF, $BD, $7E, $7F, $DC, $DD, $C0, $C1, $3E, $3F and $F0-$F2.

The summary lists every `io_unreached` row except the `very-low` ones, with its evidence.

## Frame cost model

On the Next every SMS I/O instruction runs through the runtime's trap. A name table `OUTI` takes about 2,100 Next cycles against 16 T-states on an SMS. A game that streams VDP data in the foreground with interrupts on, or that does much I/O in its interrupt handler, can overrun the Next frame although it fits on the SMS. The model finds those routines from the code alone.

### Costs

All costs are Next CPU cycles at 28 MHz. A Next frame is 567,264 cycles. The cost table is `COST_VDATA` and `COST_PORT` in `sitescan.py`, with a comment that says where it was measured.

- A native instruction costs its Z80 T-states plus one cycle for every memory read: the instruction's own bytes and the data it reads. Writes add nothing. This matches the measured cycles exactly.
- An I/O instruction costs the measured trap time, by form and port class: `OUT (n),A`, `OUT (C),r`, single `OUTI`/`OUTD`, `OTIR` (and `OUTI; JR NZ,-2`, which the overlay turns into an `OTIR`), runs of `OUTI`, traces, and the `IN` forms. Block forms have a fixed part and a part per byte.
- Which sites become traces or runs is decided as the overlay builder decides it, with `tracedef.choose` on the cart with the I/O sites patched, and whether each becomes a run or a copied trace with `tracedef.verdict`. A trace costs its fixed part once per loop and a smaller part per output, on top of the native code of the loop.
- A VDP data write costs more or less by the VRAM region it lands in: tile data, sprite table or name table. The scanner does not know the region, so the cost is a range from the cheapest to the dearest of the three. Name table writes are the high end. A CRAM write that changes an entry costs more again and is not in the range.

### Routines and loops

The model works on each routine's flow graph, using only proven flow: a jump through a table whose length the scanner guessed is not followed. A routine's cost is its costliest path from the entry to a return. A path that jumps into the reset code at $0000 does not return and is not counted. When no path returns, the cost follows every path to where the flow ends.

A loop costs its count times its costliest pass. The count is known when the loop counts a register down to zero and the register's value at the loop head is known:

- `DJNZ`, or `JR NZ`/`JP NZ` after `OUTI`, `OUTD`, `INI`, `IND` or `DEC r` (with only flag-neutral instructions, or a `PUSH AF`/`POP AF` pair, in between): the count is in B or r;
- `DEC rr; LD A,hi; OR lo; JR NZ`: the count is in the pair.

The value comes from the routine's own constants or, when the routine receives it, from each caller (`args`). The cost is the worst over the callers' values. A loop inside another loop that counts the same register uses up the count, so the outer loop counts as one pass. When a count is not known, the loop counts as one pass and the routine's `count` is `unknown`.

A call adds the callee's cost with the values the caller passes.

### Context and interrupts

Routines called from $0038, $0066 or a `--handler` entry, on paths that return, are the interrupt context (`irq`). The rest are foreground. The interrupt enable state is followed through `DI`, `EI` and calls, from off at the vectors, into each routine through its callers.

### Findings

The summary's "Frame cost" section lists:

- the interrupt handler's cost (the costliest of $0038 and the `--handler` entries) and whether the interrupt context writes the VDP control port;
- the interrupt handler's cost from its entry to its first `EI` (the maskable interrupt enters with interrupts off), or to its return when no `EI` comes first. It is shown in cycles and in Next lines of 1,824 cycles. The SMS frame event is the end of line 192, so the handler leaves interrupts off until line 192 plus its cost in lines. The line is flagged `TEAR RISK` when the cheapest path ends past line 248, where the Next ULA interrupt comes: the held interrupt then runs the runtime's once-a-frame work in the middle of the picture. When only the costliest path ends past line 248, the line says so and carries no flag. The line is a worst-case estimate, to be checked by measurement. A called routine counts in full, up to its own first `EI`. A loop that holds the `EI` counts one pass;
- race: foreground routines whose own instructions write the VDP with interrupts on and whose cost is more than the frame minus the handler's cost (the frame alone when the handler's worst case is a frame or more), while the interrupt context writes the VDP control port. The handler can then run in the middle of the routine's writes and move the VDP address. A routine is listed only when none of its callees is over the limit on its own;
- overrun: interrupt routines that cost more than a frame, with the same rule for callees;
- the costliest foreground routines that write the VDP with interrupts on and return.

The costs are upper bounds: the costliest path through every branch, with loop counts at their largest known value. A game often guards its VDP work with a flag that the handler checks, which the model does not see. Each finding is a place to look at, not a proven fault.

## Pattern rules

Each rule adds rows of its own kind to `NAME.sites.tsv` and a part of the "Pattern rules" section at the end of the summary. The rules run after the main scan and the frame cost model and never change their rows: a site that only rule 1 reaches is a new row, and an `io_unreached` row for the same bytes stays.

### Rule 1: inline jump tables

A dispatcher is an RST vector or a routine called from two or more places that takes its return address (`POP HL` or `EX (SP),HL`, after any pushes of other pairs), adds twice A to it (`ADD A,A`, `SLA A`, `RLCA`, `ADD HL,HL` or two `ADD HL,DE`/`ADD HL,BC`), reads a word through HL, and jumps to it (`JP (HL)`, or `RET` after `EX (SP),HL` or a push). The scanner reads the code from the entry on, following `JP nn` and expanding calls to short helpers that end in `RET`, so a dispatcher built from other RSTs is found. Wonder Boy III's `RST $20` is one. Dispatchers that the main scan already resolves are left out.

After each call of a dispatcher the scanner reads a table of words. The table ends at the first of:

- the entry count that an `AND n` (n one less than a power of two) just before the call allows, with an optional `DEC A` between them;
- a word that is not a code address for the call's slot: $0100-$7FFF from slots 0 and 1, $0100-$BFFF from slot 2;
- an entry that is a known code start: the start of a run of code in the listing or, in a second pass, a target of any table;
- the lowest target of the table that lies after it;
- a word more than $800 away from the range of the table's earlier words;
- 128 entries.

The targets become entry points (`table` kind, so entry registers are unknown) of a fresh scan. Its new tables add more entry points until none are new, at most eight rescans. `inline_table` rows list every table. Each I/O, mapper, Codemasters, cart area or RAM copy site of the last rescan that the main scan did not have becomes a row of its own kind, with `how` `inline-table` and confidence `medium`.

### Rule 2: mailbox races

A mailbox is a RAM byte that the interrupt context reads and stores 0 to. When two foreground plain stores (`LD`, not `SET`, `INC` or a load-modify-store) can write it with different values before the handler runs, the first value is lost. A store in a routine that also reads the byte is taken as a load-modify-store. Stores of 0 are clears and are left out.

A byte is not a mailbox when:

- the only 0 stores the interrupt context makes to it are `LD (HL),x` at the head of a RAM clear (`LDIR` follows): that store clears one byte of a range;
- the interrupt context also does `INC` or `DEC` on it: it is a counter;
- a foreground routine that does not write it reads it outside a wait loop: it is a state the foreground dispatches on.

For each pair of stores the rule finds the shortest path from the first to the second over every edge the scanner found, through calls and returns. A call the path does not enter costs its shortest time, with loops of known count counted in full; loops on the path itself count once. The time is in Next cycles (each I/O at its cheapest trap) and in SMS T-states (an SMS frame is 59,736).

The handler runs, and the path ends, at:

- a `HALT`;
- a wait loop: a loop with no stores and no calls that reads the VDP status, the V counter, or one fixed RAM byte in $C000-$FFFB (the interrupt's store to that byte need not have been seen);
- a call of a routine that always waits: every path from its entry to a return meets a `HALT`, a wait loop or a call of another always-waiting routine. Such a call is not costed at the routine's shortest run.

The search first uses only paths where each return matches a call on the path. Only when a pair has no such path does it allow a return with no known stack, to any caller of the routine. That pair is marked `needs a return with no known stack` in the summary.

One row per mailbox with a pair under a Next frame. A pair has `medium` confidence when its SMS time is at least 0.1 SMS frames and under one frame, and `low` otherwise: with a shorter window the interrupt rarely lands between the stores, and with a longer one it lands between them on the SMS as well, so only the Next can lose the store. The row is the pair of highest confidence; among equals one with a known stack, then the one with the longest SMS time. `class` is `under a frame, SMS over` when that SMS time is a frame or more, else `under a frame, caller unknown` when the pair needs a return with no known stack, else `under a frame`. Both times are lower bounds. The summary lists up to six pairs per mailbox.

Most rows are not races that lose a value; a row marks a place to check. Checked in MAME on the overlay carts, My Hero $C50C (0.51 SMS frames) is the known case, and it is `medium`.

### Rule 3: column and rectangle streamers

A streamer is a loop that, in one pass, writes the VDP control port at least twice and the data port at least once, directly or through calls, and moves an address by $40 or -$40 (one name table row). The step is an `ADD A,$40`, `SUB $40` or `ADD A,$C0`, an `ADD rr` with $40 or $FFC0, or the net change of a register pair over a path through the body: `INC`, `DEC`, `ADD rr` with a known value, the block instructions and `EX DE,HL` move it, a call keeps only the pairs its summary keeps. The innermost such loop is reported, with its pass count (rows), the data writes in one pass (inner loops and called loops multiplied by their counts), the cost of a pass and of the loop from the frame cost model, the routine's context (`irq`, `fg`, `both`), the outer loop if any, and the VDP write instructions it runs (address and cart offset).

### Rule 4: Sega planar RLE decoder

The scanner looks for the bytes `7E 23 B7 C8 4F E6 7F 47` (`LD A,(HL); INC HL; OR A; RET Z; LD C,A; AND $7F; LD B,A`) anywhere in the cart, and for two variants with `AND $7F` in the four bytes after them: `7E 23 B7 C8` (`variant`), and `1A 13 B7 C8` (`variant-de`: the same core reading the stream through DE, as in Hang On). A fourth form, `jr-z`, has `JR Z,exit` in place of `RET Z`: the bytes `7E 23 B7 28 d 4F E6 7F 47`, as in Castle of Illusion, where the plane loop that calls the core in the other forms is wrapped around it in the same routine. The bytes alone are not enough. The code from the core up to the `JR Z` target must also hold a jump back to the core, `BIT 7,C` (the choice between a run of one byte and a run of literal bytes), a count down of B (`DJNZ` or `DEC B`) and an `OUT` to the VDP data port. A copy that decodes into RAM has no data port write and is not reported.

For each copy a path reached it reports the routines that hold it, whether it is frame work (`irq`: a routine reached from the interrupt handler) or foreground, the control and data writes of its loop with their addresses, the routine's cost, and the calls of the routine. A copy no path reached is `unreached` with the count of `OUT ($BE),A` and control writes in the 64 bytes from the core.

### Rule 5: H scroll from a table

A game that changes the H scroll every few lines sets VDP register 8 from its line interrupt, and the runtime then needs a `rastercode` routine in the spec ([overlays.md](overlays.md)). The rule looks in every routine the interrupt handler runs for `LD A,src; OUT ($BF),A; LD A,$88; OUT ($BF),A`, a write of register 8, where `src` is a byte at an address that changes from one interrupt to the next, a table:

- `pointer`: `src` is `(HL)`, `(DE)`, `(BC)`, `(IX+d)` or `(IY+d)`, and the scanner cannot prove the pointer to a single address. Castle of Illusion steps a pointer into a table 2 bytes on each interrupt.
- `patched address`: `src` is `(nn)` in code run from RAM, and a store in the code writes the bytes of nn. Hang On and OutRun copy the handler to RAM and write a value worked out from the V counter into the address of the load.

A load from one fixed address is a single value for the whole picture and is left out. The row is the load. Its note gives the register write, the interrupt routine and the routine's V counter reads, if any. A flagged game does not always need a routine: Black Belt, with up to 11 changes a frame, plays without one.

## Known limits

- The model does not track the shadow registers. A loop that counts in B' (`EXX; DEC B; EXX; JP NZ`) has an unknown count, costed as one pass.
- The frame cost model costs every run of outputs in a row as a run of `OUTI`. A run of other outputs, or of `OUTI` mixed with them, costs more in the runtime.
- A task switch (`RET` after `LD SP`) is not followed. The task entries are found only when the code stores them into RAM from a word table in ROM; otherwise add them with `--entry`.
- A routine reached only through a pointer the scanner cannot trace back to a constant (a handler address kept in RAM or computed at run time, a table it did not recognise) is missed. The summary lists unresolved indirect jumps; add their targets with `--entry`, or give a dynamic log or CDL.
- The object handler rules read a handler table only up to the end of the slot it starts in, so a table that runs on from slot 1 into slot 2 gives only its first entries. A handler that calls into slot 2 starts with an unknown slot 2 bank, so it is dropped as data when it calls slot 2 code; add such handlers with `--entry`.
- A table length that only the table's contents give is a guess: the table can be read too short (missed handlers) or too long (data decoded as code). The largest stored index is a limit only for the stores the scanner sees: a block copy (`LDIR`) into the variable, or a store through a pointer it cannot resolve, can write a larger index. Rows reached through a table are `medium`.
- Pointer harvest can take a data value for a code address. The checks above catch the cases seen so far; the summary lists every harvested entry and the instruction that stored it, so a person can check them.
- Stores through IX and IY into object structures make up most of the unproven list in commercial games. The object pointer comes from the caller and usually from a RAM table, so the scanner cannot prove where it points.
- Memory other than the stack is not modelled. A value stored to RAM and loaded back later is unknown, so a pointer kept in a RAM variable (an interrupt handler hook, an object's handler) is only found through pointer harvest and the object handler rules.
- A dynamic log seed that starts at a bank switch store has an unknown bank after the store, because the value written comes from before the seed. A call into slot 2 right after it is listed as an unresolved transfer even when a bank call entry has scanned its target. Alien Syndrome's calls into banks 10 and 15 show this.
- A bank that a task scheduler sets for a task (Alien Syndrome passes the bank in D to its task start routine, `RST $30`) is not tracked, so the task's calls into slot 2 stay unresolved and their target code is not scanned unless given with `--entry`.
- When more than `--unroll` states reach one instruction, they are merged, and a register that differs between them becomes unknown. A shared table dispatcher that many routines enter with `JP` and their own table in HL (Pro Wrestling's at $0454) can lose HL this way, and its `JP (HL)` is listed as unresolved for that path. In Pro Wrestling each of those tables is still read from another path.
- When a table entry or call target is in a banked slot whose bank comes from RAM, the scanner does not follow it. The summary lists the table's first words and the constant banks the code writes to $FFFE and $FFFF anywhere, so a person can add `--entry BANK:ADDR`.
- Slot 0 is assumed to stay bank 0. A cart that writes $FFFD with a non-zero value shows that write as a `mapper` row, but code in slot 0 is still read from bank 0.
- A store whose address is unknown is assumed not to change the mapper. Only proven stores to $FFFE/$FFFF change the tracked banks.
- `$FFFC` writes (cart RAM paging) are reported but not modelled: reads of $8000-$BFFF are taken from ROM.
- BizHawk CDL files are not read; only Mesen2's `CDLv2` layout is.
- The byte scan finds only the patterns in its table. A store through a register set elsewhere, such as `LD (HL),A` with HL loaded earlier or `LD (IX+d),A`, is found only when a path reaches it.
- Rule 1 finds a dispatcher by its instruction shape; a dispatcher that branches before the jump is missed. Its table end rules are guesses like the main scan's, and a table read too long adds data as code (rows with `how` `inline-table` from such tables are noise).
- Rule 2 sees only stores whose address the scanner proves. Its times are shortest paths, so a pair it reports may never run that close, and its SMS times are too low.
- Rule 3 misses a loop whose address step comes from a table or from RAM.
- Rule 5 sees only the write order above, in code the interrupt handler reaches by proven flow. A register write through a helper routine, through `OUT (C),r`, or with other instructions between the four is missed.
- Interrupt mode 2 vectors are not followed. Only $0000, $0038 and $0066 are vector entry points.
- The frame cost model does not follow jumps through tables whose length is a guess, so a handler that dispatches its frame work through a table is undercounted. It does not count the runtime's own once-a-frame work (tile conversion, sprites, copper list), the trace builds (about 13,800 cycles the first time a trace site runs, and again for a copy after the code area fills), or the VRAM region of a write. A routine that drops its return address and jumps back into its caller's code is counted as returning to the caller as well.

