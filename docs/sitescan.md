# sitescan

`tools/sitescan.py` finds the places in a Master System cart that a NextMasterSystem overlay has to patch. [overlays.md](overlays.md) shows where it fits in making an overlay. It is a recursive-descent Z80 disassembler: it starts at the reset and interrupt vectors, follows every jump and call it can prove, and reports:

- every `IN`, `OUT` and block I/O instruction, with its port and what that port does on an SMS;
- every store that reaches the Sega mapper registers ($FFFC-$FFFF), and every Codemasters-style store ($0000, $4000, $8000);
- stores through a register whose address it cannot prove to stay off $FFFC-$FFFF, in a separate list;
- `RST` instructions and the vectors they use;
- `LDIR`/`LDDR` copies from ROM into RAM, and any I/O in copied code that runs;
- jump tables it read, indirect jumps it could not resolve, and calls into a banked slot with a bank it could not work out;
- `IN`/`OUT` byte patterns in bytes that no path reached, as a low-confidence list;
- mapper store byte patterns in bytes that no path reached, each rated by how much the bytes around it look like code;
- how many bytes it classified as code.

It uses only the Python 3 standard library. Run it with `python3 -I`.

## Running it

```sh
python3 -I tools/sitescan.py CART.sms --out OUTDIR [options]
```

Options:

| Option | Meaning |
|---|---|
| `--entry ADDR` or `--entry BANK:ADDR` | Extra entry point, hex. Repeat it for more. Use it for the unresolved indirect jumps the summary lists. `BANK:ADDR` places code in slot 2 (or slot 1) with that bank. |
| `--log FILE` | A dynamic log: `*.io.tsv`, `*.mapper.tsv` or `*.features.json`, described below. Repeatable. |
| `--logdir DIR` | Every `*.io.tsv`, `*.mapper.tsv` and `*.features.json` in DIR. |
| `--cdl FILE` | A Mesen2 code/data log (`CDLv2`). |
| `--mapper auto\|sega\|codemasters` | Mapper model. `auto` (the default) uses the Codemasters model only when the cart has proven Codemasters-style stores and no proven Sega mapper store. |
| `--name NAME` | Prefix for the output files. Default: the cart file name. |
| `--no-harvest` | Do not use code addresses found in stores to RAM as entry points (see below). |
| `--unroll N` | Distinct register states kept per instruction before they are merged. Default 8. |

A 512-byte copier header is skipped when the file size is 512 more than a multiple of 16 KB, as `mknms.py` does.

Example, a cart with a dynamic log:

```sh
python3 -I tools/sitescan.py game.sms --log game.io.tsv --out scan --name game
```

### Dynamic logs

A dynamic log is a list of PCs that an emulator saw the game run. The scanner reads three kinds, by file name:

- `*.io.tsv` and `*.mapper.tsv`: tab-separated, with a header line. The `pc` column is the PC in hex. An optional `insn_bytes` column holds the instruction's bytes in hex; when it is there, the scanner checks them against the cart.
- `*.features.json`: any JSON. Every string in a list under the key `example_pcs` or `ram_code_writer_pcs` is a PC in hex.

Dynamic logs and CDL files only add entry points. The scanner first runs without them; afterwards it adds only the logged PCs that the static pass did not already reach. A log row whose instruction bytes differ from the cart's bytes at that PC is dropped, and the summary says how many were dropped. A log from another cart therefore does nothing harmful, but `--logdir` on a directory that holds several carts' logs will still read them all.

## Output files

All files go to `--out`, named after `--name`.

### `NAME.sites.tsv`

One row per site, tab-separated, with a header line. This is the file an overlay builder reads.

| Column | Content |
|---|---|
| `addr` | CPU address of the instruction. For code run from RAM, the RAM address. |
| `bank` | 16 KB ROM bank the instruction is in, or `ram`. |
| `offset` | ROM file offset of the instruction (header skipped). For code run from RAM, the offset of the copy's source bytes, which is where a patch goes. |
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
| `io_unreached` | `D3 n`, `DB n` or an `ED` I/O opcode in bytes no path reached. |
| `mapper_unreached` | A mapper store byte pattern in bytes no path reached, found by the byte scan (see below). `target` is the spec line form that patches it: `mapst`, `mapsthl`, `mapstbc`, `mapstde`, `mapld`, `mapldk` or `codem`. `note` lists the evidence. |

Port classes follow the SMS decoding of address lines A7, A6 and A0: `memory_control`, `io_control`, `unmapped_read`, `psg`, `v_counter`, `h_counter`, `vdp_data`, `vdp_control`, `vdp_status`, `joypad_a`, `joypad_b_misc`, `no_effect` (a write to $C0-$FF), `fm_address`, `fm_data` and `fm_control` for writes to $F0-$F2, and `fm_detect` for a read of $F2.

Port and value notes in `target`: a plain value was proven inside the routine. `(callers)` means the routine receives the value from its callers and every known caller passes it. `(partial)` means some callers pass it and for others it is unknown.

Confidence and `how`:

- `high`: reached by proven control flow from the vectors or a `--entry` (`how` is `static`), or from a dynamic log or CDL entry point (`log-seed`, `cdl-seed`).
- `medium`: reached only through something the scanner inferred: a jump table whose length it guessed (`+table`), or an address harvested from a store to RAM (`pointer-harvest`).
- `low`, `very-low`: `io_unreached` rows. `low` when the port is one SMS games use ($BE, $BF, $BD, $7E, $7F, $DC, $DD, $C0, $C1, $3E, $3F, $F0-$F2) or the opcode is an `ED` I/O form; `very-low` otherwise.
- `mapper_unreached` rows have their own scale, described under "Byte scan for mapper stores". Their `how` is `byte scan, no path reached it`.
- `+seen-in-log` is added when a dynamic log also has that PC.

### `NAME.unproven.tsv`

Stores through HL, DE, BC, IX or IY, and block copies, whose address the scanner could not prove to stay off $FFFC-$FFFF. Columns: `addr`, `bank`, `offset`, `bytes`, `insn`, `address` (what is known about the address), `reason`, `how`. A store is left out of this list when its address is proven, when the high byte of the address register is known and the page cannot be $FF, when the address is a known base plus an index whose range cannot reach $FFFC, or when the address is a slot in the routine's own stack frame (`IX` set from `SP`, as SDCC does).

### `NAME.summary.txt`

The same results, readable: the constant banks the code writes to $FFFE and $FFFF, I/O sites by port function, mapper and Codemasters stores, unproven-store counts by reason and register, RST vectors, RAM copies, tables, unresolved transfers, harvested entry points (with the instruction that stored each one), harvested addresses that were rejected, paths that stopped on bytes that do not look like code, overlapping decodes, unreached I/O patterns, mapper stores found by the byte scan, coverage per bank, and a comparison with the dynamic logs when logs were given.

### `NAME.dis.txt`

The disassembly of everything reached, sorted by ROM offset, with site kinds marked. A blank line separates runs of code that are not contiguous.

## How it works

The scanner works routine by routine. A routine starts at a vector, a call or `RST` target, a table entry, a command-line or log entry point, or a harvested address. Inside a routine it runs a data-flow analysis over the instructions it reaches, keeping an abstract value for every register:

- a constant;
- "the value this register had when the routine was entered", which is later resolved through the routine's callers;
- addresses built from a table base: base plus an unknown index, base plus an index of known range, a byte or word read from such a table, or the routine's own return address;
- the stack, byte by byte, relative to SP at routine entry. `PUSH`, `POP`, `EX (SP)`, `INC SP`, `DEC SP`, `ADD HL,SP`, `LD SP,HL` and `LD SP,IX` keep it in step. Bytes above the return address are the caller's stack arguments, which are resolved at each call site the same way as register arguments. This covers SDCC code, which passes arguments on the stack and reads them through an `IX` frame or by popping past the return address.

Constants come from immediates, from arithmetic on constants, and from reads of ROM at a constant address. Up to `--unroll` distinct states are kept per instruction before they are merged, so short counted loops are followed pass by pass. `DJNZ` with a known B follows only the branch that is taken.

Each routine gets a summary: whether it returns, whether it skips inline bytes after the call, which registers it keeps, sets to a constant, or computes from its caller's registers, and whether it is a table dispatcher. Calls use the callee's summary. Because summaries depend on each other, the whole scan repeats until nothing changes, or until a round repeats an earlier one (this happens when a table read longer in one round decodes code that cuts it shorter in the next; the summary says so).

Control flow it follows:

- `JP`, `JR`, `CALL`, `RST`, `DJNZ`, conditional forms, `RET`, `RETI`, `RETN`.
- `PUSH` of a constant followed by `RET` (a jump), and a routine that adjusts its own return address with `EX (SP),HL` (inline arguments after the call).
- `JP (HL)` with HL a constant, a word read from a table at a constant base, a table address passed in by the caller (the table is read at each call site), or the return address (an `RST` or `CALL` followed by an inline table). Both the 16-bit form (`ADD HL,DE`) and the 8-bit form (`ADD A,L / LD L,A / ADC A,H / SUB L / LD H,A`) of "base plus index" are recognised.
- `JP (HL)` into a list of `JP nn` or `JR d` instructions, as compiled `switch` statements use.
- A `JP (HL)` or `RET` to "base plus unknown offset" that is not a table: the scanner continues at the base, which covers entry into unrolled code such as a chain of `OUTI` or `LDI`.
- A helper whose `JP (HL)` jumps to the caller's HL: each caller's HL becomes a call target.

A table's length is not known. The scanner reads entries until one is not a code address, does not decode as a few valid instructions, points into the table, the table reaches the lowest target above its start, or the next entry position was an instruction start in the previous round. A first entry that is not valid is skipped once, for tables indexed from 1. Everything reached only through a table is `medium` confidence.

Banks: slot 0 is always bank 0. Slot 2 starts unknown at the vectors and takes the value written to $FFFF (or to $8000 in the Codemasters model). A jump or call into $8000-$BFFF goes to that bank when the value is a constant, or to each bank the callers pass when the routine receives it. Code that is itself in slot 2 assumes its own bank. Slot 1 is taken as bank 1 unless the cart writes $FFFE (or $4000 in the Codemasters model) with another value or an unknown one; after that slot 1 is tracked the same way as slot 2.

Code copied to RAM: an `LDIR`/`LDDR` with a proven ROM source, RAM destination and length is recorded. A jump or call into that RAM range is decoded from the copy's source bytes, at the RAM address.

Pointer harvest: a constant code-like address that the code stores into RAM ($C000-$FFFF), with `LD (nn),HL` and similar, or as two byte stores into a structure field that some `JP (HL)` in the cart jumps through, becomes an entry point. It is refused when the store writes several different values, when both bytes are equal ($0909 and the like), when the target starts with $FF, or when the bytes at the target do not decode as at least two valid instructions. After a scan, a harvested entry is dropped again if the code reached from it hits an invalid opcode, a jump into RAM or slot 2 that cannot be resolved, or an I/O port SMS games do not use. Harvested code is `medium` confidence.

Bytes that are not code: a path stops at an invalid opcode, at `RST $38` followed by $FF (erased fill), at a literal store into $0000-$7FFF other than $0000 and $4000, and at `LD SP,nn` with nn in ROM. The summary lists each place a path stopped and why.

### Byte scan for mapper stores

A mapper store that no path reaches is not patched, and on the Next it then writes RAM: the bank does not change, and the game reads the wrong bank later, often minutes into play. Code the flow scan misses is common in commercial games. So after the flow scan, the scanner looks at every byte of the cart, in every bank, for these patterns:

| Bytes | Instruction | Spec line |
|---|---|---|
| `32 nn FF`, nn $FC-$FF | `LD ($FFnn),A` | `mapst` |
| `22 nn FF`, nn $FC-$FE | `LD ($FFnn),HL` | `mapsthl` |
| `ED 43 nn FF`, `ED 53 nn FF`, nn $FC-$FE | `LD ($FFnn),BC`, `LD ($FFnn),DE` | `mapstbc`, `mapstde` |
| `21 nn FF 36 n`, nn $FC-$FF | `LD HL,$FFnn; LD (HL),n` | `mapld` ($FFFF), `mapldk` |
| `32 00 nn`, nn $00, $40 or $80, Codemasters model only | `LD ($nn00),A` | `codem` |

A pattern whose first byte a path reached as an instruction is skipped: the flow scan has classified it. Every other hit becomes a `mapper_unreached` row, rated by this evidence:

- a setter: the instruction just before the store loads the register it stores, in a way games do before a bank switch. For A that is `LD A,n`, `LD A,(HL)`, `LD A,(DE)`, `LD A,(BC)`, `LD A,(IX+d)`, `LD A,(IY+d)`, `LD A,(nn)` from RAM, `POP AF`, or `LD (nn),A` to RAM (a copy of the bank number). For HL, BC and DE it is `LD rr,nn`, `LD rr,(nn)` or `POP rr`. `NOP` and `LD A,A` between the two are skipped. Another mapper store pattern that ends within three bytes before the store also counts. The `LD HL,$FFnn; LD (HL),n` pattern carries its own setter;
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

## Known limits

- A routine reached only through a pointer the scanner cannot trace back to a constant (a handler address kept in RAM or computed at run time, a table it did not recognise) is missed. The summary lists unresolved indirect jumps; add their targets with `--entry`, or give a dynamic log or CDL.
- Table lengths are guesses. A table can be read too short (missed handlers) or too long (data decoded as code). Rows reached that way are `medium`.
- Pointer harvest can take a data value for a code address. The checks above catch the cases seen so far; the summary lists every harvested entry and the instruction that stored it, so a person can check them.
- Stores through IX and IY into object structures make up most of the unproven list in commercial games. The object pointer comes from the caller and usually from a RAM table, so the scanner cannot prove where it points.
- Memory other than the stack is not modelled. A value stored to RAM and loaded back later is unknown, so a pointer kept in a RAM variable (an interrupt handler hook, an object's handler) is only found through pointer harvest.
- When a table entry or call target is in a banked slot whose bank comes from RAM, the scanner does not follow it. The summary lists the table's first words and the constant banks the code writes to $FFFE and $FFFF anywhere, so a person can add `--entry BANK:ADDR`.
- Slot 0 is assumed to stay bank 0. A cart that writes $FFFD with a non-zero value shows that write as a `mapper` row, but code in slot 0 is still read from bank 0.
- A store whose address is unknown is assumed not to change the mapper. Only proven stores to $FFFE/$FFFF change the tracked banks.
- `$FFFC` writes (cart RAM paging) are reported but not modelled: reads of $8000-$BFFF are taken from ROM.
- BizHawk CDL files are not read; only Mesen2's `CDLv2` layout is.
- The byte scan finds only the patterns in its table. A store through a register set elsewhere, such as `LD (HL),A` with HL loaded earlier or `LD (IX+d),A`, is found only when a path reaches it.
- Interrupt mode 2 vectors are not followed. Only $0000, $0038 and $0066 are vector entry points.
