# NextMasterSystem: build/nms.nex
#
#   make          build everything
#   make clean    remove build/
#
# Needs z88dk 2.4 (zcc and z88dk-z80asm on PATH), make, sh, awk and sed.

BUILD  := build
RT     := src/runtime
SH     := src/shell
ZCC    ?= zcc
Z80ASM ?= z88dk-z80asm
ABS    := $(CURDIR)

# ---- the banked C modules ------------------------------------------------
# Each module is a directory under src/shell with its C and assembly files,
# linked into the high half of one 16K bank. To add a module: add its name
# here, set <name>_SEG, add its PAGE_ number to src/shell/nm.h. See
# docs/design.md, "Adding a C module".
MODULES := session loader info
session_SEG := BANK_54_H
loader_SEG  := BANK_55_H
info_SEG    := BANK_56_H
# objects that must come first in their bank (the CRC32 table is page aligned)
loader_FIRST := $(BUILD)/loader/crc32.o

# ---- compiler flags ---------------------------------------------------------
CFLAGS := +zxn -vn -clib=sdcc_ix -startup=31 -O2 \
          -I$(SH) -I$(BUILD) -pragma-include:$(SH)/zpragma.inc
AFLAGS := -Ca-I$(ABS)/$(RT) -Ca-I$(ABS)/$(BUILD) -Ca-I$(ABS)/$(BUILD)/rt

RESIDENT_SRC := $(wildcard $(SH)/*.c)
RESIDENT_ASM := $(wildcard $(SH)/*.asm)
RESIDENT_OBJ := $(patsubst $(SH)/%.c,$(BUILD)/res/%.o,$(RESIDENT_SRC)) \
                $(patsubst $(SH)/%.asm,$(BUILD)/res/%.o,$(RESIDENT_ASM))

define module_rules
$(1)_SRC := $$(wildcard $$(SH)/$(1)/*.c) $$(wildcard $$(SH)/$(1)/*.asm)
$(1)_OBJ := $$(patsubst $$(SH)/%.c,$$(BUILD)/%.o,$$(filter %.c,$$($(1)_SRC))) \
            $$(patsubst $$(SH)/%.asm,$$(BUILD)/%.o,$$(filter %.asm,$$($(1)_SRC)))
$(1)_ORDERED := $$($(1)_FIRST) $$(filter-out $$($(1)_FIRST),$$($(1)_OBJ))
BANK_OBJ += $$($(1)_ORDERED)
SEGFLAGS_$(1) := --codeseg$$($(1)_SEG) --constseg$$($(1)_SEG) \
                 --dataseg$$($(1)_SEG) --bssseg$$($(1)_SEG)
$$(BUILD)/$(1)/%.o: $$(SH)/$(1)/%.c $$(BUILD)/memplan.h $$(BUILD)/fwsyms.h $$(SH)/nm.h
	@mkdir -p $$(@D)
	$$(ZCC) $$(CFLAGS) -c $$(SEGFLAGS_$(1)) $$< -o $$@
$$(BUILD)/$(1)/%.o: $$(SH)/$(1)/%.asm $$(BUILD)/memplan.h
	@mkdir -p $$(@D)
	$$(ZCC) $$(CFLAGS) $$(AFLAGS) -c $$< -o $$@
endef
$(foreach m,$(MODULES),$(eval $(call module_rules,$(m))))

# ---- the runtime pages ---------------------------------------------------
RT_SRC := $(wildcard $(RT)/*.asm) $(wildcard $(RT)/*.inc)
RT_BINS := $(BUILD)/rt/runtime_fw.bin $(BUILD)/rt/runtime_fw2.bin $(BUILD)/rt/runtime_fw3.bin

.PHONY: all clean
all: $(BUILD)/nms.nex

$(BUILD)/rt/runtime.map: $(RT_SRC)
	@mkdir -p $(BUILD)/rt
	cd $(RT) && $(Z80ASM) -mz80n -b -m -s -split-bin -O$(ABS)/$(BUILD)/rt runtime.asm

$(RT_BINS): $(BUILD)/rt/runtime.map

# The memory plan for C, from the one in assembly.
$(BUILD)/memplan.h: $(RT)/memplan.inc
	@mkdir -p $(BUILD)
	sed -n -e 's/\$$\([0-9A-Fa-f][0-9A-Fa-f]*\)/0x\1/g' \
	       -e 's/^\([A-Z][A-Z0-9_]*\)[[:space:]]*equ[[:space:]]*\([^;]*[^;[:space:]]\).*/#define \1 (\2)/p' \
	       $< > $@

# The runtime's addresses the shell needs, from the runtime's map.
FWSYMS := fw_crc:FW_CRC fw_start_addr:FW_START_ADDR fw_start_sp:FW_START_SP \
          rast_hook:RAST_HOOK ramp_hook:RAMP_HOOK fw_flags:FW_FLAGS \
          nr_saved:NR_SAVED fw_resume:FW_RESUME
$(BUILD)/fwsyms.inc $(BUILD)/fwsyms.h: $(BUILD)/rt/runtime.map
	@echo "; generated from the runtime map, do not edit" > $(BUILD)/fwsyms.inc
	@echo "/* generated from the runtime map, do not edit */" > $(BUILD)/fwsyms.h
	@for p in $(FWSYMS); do \
	  s=$${p%%:*}; n=$${p##*:}; \
	  a=$$(awk -v s=$$s '$$1 == s { print $$3; exit }' $<); \
	  [ -n "$$a" ] || { echo "symbol $$s not in $<" >&2; exit 1; }; \
	  echo "defc $$n = $$a" >> $(BUILD)/fwsyms.inc; \
	done
	@a=$$(awk '$$1 == "FW_ABI" { print $$3; exit }' $<); \
	  echo "#define FW_ABI ($${a/\$$/0x})" | sed 's/\$$/0x/' >> $(BUILD)/fwsyms.h

# ---- the shell --------------------------------------------------------------
$(BUILD)/res/%.o: $(SH)/%.c $(BUILD)/memplan.h $(BUILD)/fwsyms.h $(SH)/nm.h
	@mkdir -p $(@D)
	$(ZCC) $(CFLAGS) -c $< -o $@

$(BUILD)/res/%.o: $(SH)/%.asm $(BUILD)/memplan.h $(BUILD)/fwsyms.inc $(BUILD)/rt/runtime.map
	@mkdir -p $(@D)
	$(ZCC) $(CFLAGS) $(AFLAGS) -c $< -o $@

$(BUILD)/res/fwpages.o: $(RT_BINS)

$(BUILD)/nms.nex: $(RESIDENT_OBJ) $(BANK_OBJ) $(RT_BINS) tools/check-layout
	$(ZCC) $(CFLAGS) $(AFLAGS) -m $(RESIDENT_OBJ) $(BANK_OBJ) -o $(BUILD)/nms \
	    -create-app -subtype=nex -Cz"--main-fence 0xA000 --nex-border 0"
	@rm -f $(BUILD)/nms
	tools/check-layout $(BUILD)/rt/runtime.map $(BUILD)/nms.map

clean:
	rm -rf $(BUILD)
