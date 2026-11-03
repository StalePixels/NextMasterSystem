# NextMasterSystem: build/nms.nex
#
#   make          build everything
#   make TRACE=1  the trace build, build/trace/nms.nex: the runtime with its
#                 checks for test tools (src/runtime/vdpcheck.asm)
#   make clean    remove build/
#
# The z88dk tools (zcc, z88dk-z80asm) run in z88dk's Docker image, with this
# folder mounted at its own path, so relative and absolute paths both work in
# the container. The host needs Docker, make, sh, awk and sed.
# Z88DK_IMAGE=... picks another image.

# This file, so that every product below can depend on it.
THIS_MAKEFILE := $(lastword $(MAKEFILE_LIST))

BUILD  := build
RTDEFS :=
ifeq ($(TRACE),1)
BUILD  := build/trace
RTDEFS := -DTRACE_BUILD
endif
RT     := src/runtime
SH     := src/shell
ABS    := $(CURDIR)

# One container per tool call. The files it writes belong to the host user.
Z88DK_IMAGE ?= z88dk/z88dk:latest
Z88DK_RUN = docker run --rm --user $(shell id -u):$(shell id -g) -e HOME=/tmp \
            -v $(ABS):$(ABS) -w $(1) $(Z88DK_IMAGE)
ZCC    = $(call Z88DK_RUN,$(ABS)) zcc
Z80ASM = $(call Z88DK_RUN,$(ABS)/$(RT)) z88dk-z80asm

# ---- the banked C modules ------------------------------------------------
# Each module is a directory under src/shell with its C and assembly files,
# linked into the high half of one 16K bank. To add a module: add its name
# here, set <name>_SEG, add its PAGE_ number to src/shell/nm.h. See
# docs/design.md, "Adding a C module".
MODULES := session loader info overlay splash
session_SEG := BANK_54_H
loader_SEG  := BANK_55_H
info_SEG    := BANK_56_H
overlay_SEG := BANK_57_H
splash_SEG  := BANK_103_H
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
$$(BUILD)/$(1)/%.o: $$(SH)/$(1)/%.c $$(BUILD)/memplan.h $$(BUILD)/fwsyms.h $$(BUILD)/boot.h $$(SH)/nm.h $$(SH)/nms.h
	@mkdir -p $$(@D)
	$$(ZCC) $$(CFLAGS) -c $$(SEGFLAGS_$(1)) $$< -o $$@
$$(BUILD)/$(1)/%.o: $$(SH)/$(1)/%.asm $$(BUILD)/memplan.h
	@mkdir -p $$(@D)
	$$(ZCC) $$(CFLAGS) $$(AFLAGS) -c $$< -o $$@
endef
$(foreach m,$(MODULES),$(eval $(call module_rules,$(m))))

# ---- the runtime pages ---------------------------------------------------
RT_SRC := $(wildcard $(RT)/*.asm) $(wildcard $(RT)/*.inc)
RT_BINS := $(BUILD)/rt/runtime_fw.bin $(BUILD)/rt/runtime_fw2.bin $(BUILD)/rt/runtime_fw3.bin \
           $(BUILD)/rt/runtime_fw4.bin

BOOT_BINS := $(BUILD)/boot/cart0.bin $(BUILD)/boot/cart1.bin $(BUILD)/boot/cart2.bin \
             $(BUILD)/boot/cart3.bin $(BUILD)/boot/ovl.bin

.PHONY: all clean
all: $(BUILD)/nms.nex

$(BUILD)/rt/runtime.map: $(RT_SRC)
	@mkdir -p $(BUILD)/rt
	$(Z80ASM) -mz80n -b -m -s -split-bin $(RTDEFS) -O$(ABS)/$(BUILD)/rt runtime.asm

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
          nr_saved:NR_SAVED fw_resume:FW_RESUME pg_tab:PG_TAB \
          pk_n:PK_N pk_vbl:PK_VBL vb_kbd:VB_KBD kbd_scan:KBD_SCAN
$(BUILD)/fwsyms.inc $(BUILD)/fwsyms.h: $(BUILD)/rt/runtime.map
	@echo "; generated from the runtime map, do not edit" > $(BUILD)/fwsyms.inc
	@echo "/* generated from the runtime map, do not edit */" > $(BUILD)/fwsyms.h
	@for p in $(FWSYMS); do \
	  s=$${p%%:*}; n=$${p##*:}; \
	  a=$$(awk -v s=$$s '$$1 == s { print $$3; exit }' $<); \
	  [ -n "$$a" ] || { echo "symbol $$s not in $<" >&2; exit 1; }; \
	  echo "defc $$n = $$a" >> $(BUILD)/fwsyms.inc; \
	  echo "#define $$n ($$a)" | sed 's/\$$/0x/' >> $(BUILD)/fwsyms.h; \
	done
	@a=$$(awk '$$1 == "FW_ABI" { print $$3; exit }' $<); \
	  echo "#define FW_ABI ($${a/\$$/0x})" | sed 's/\$$/0x/' >> $(BUILD)/fwsyms.h

# ---- the shell --------------------------------------------------------------
$(BUILD)/res/%.o: $(SH)/%.c $(BUILD)/memplan.h $(BUILD)/fwsyms.h $(SH)/nm.h $(SH)/nms.h
	@mkdir -p $(@D)
	$(ZCC) $(CFLAGS) -c $< -o $@

$(BUILD)/res/%.o: $(SH)/%.asm $(BUILD)/memplan.h $(BUILD)/fwsyms.inc $(BUILD)/rt/runtime.map
	@mkdir -p $(@D)
	$(ZCC) $(CFLAGS) $(AFLAGS) -c $< -o $@

$(BUILD)/res/fwpages.o: $(RT_BINS)
$(BUILD)/res/bootpages.o: $(BOOT_BINS)
$(BUILD)/info/info.o $(BUILD)/splash/splash.o: $(SH)/info/l2screen.h

$(BUILD)/nms.nex: $(RESIDENT_OBJ) $(BANK_OBJ) $(RT_BINS) $(BOOT_BINS) tools/check-layout
	$(ZCC) $(CFLAGS) $(AFLAGS) -m $(RESIDENT_OBJ) $(BANK_OBJ) -o $(BUILD)/nms \
	    -create-app -subtype=nex -Cz"--main-fence 0xA000 --nex-border 0"
	@rm -f $(BUILD)/nms
	tools/check-layout $(BUILD)/rt/runtime.map $(BUILD)/nms.map build/boot.sms build/boot/boot.nms

# A change to the build rules rebuilds everything.
$(RESIDENT_OBJ) $(BANK_OBJ) $(BUILD)/rt/runtime.map $(BUILD)/memplan.h \
$(BUILD)/fwsyms.inc $(BUILD)/fwsyms.h $(BUILD)/nms.nex: $(THIS_MAKEFILE)

clean:
	rm -rf build

# ---- the boot pages ---------------------------------------------------------
# build/boot.sms: a 32K Master System cart, assembled on the host with
# sjasmplus. boot.py makes the tile graphics and writes the header checksum.
# build/boot/boot.nms: its overlay file, built by tools/mknms.py from
# src/boot/boot.spec with the spec's cart line set to the cart's CRC32.
# bootpages.asm puts both into nms.nex, in the pages BOOT_PAGE and
# BOOT_OVL_PAGE (src/runtime/memplan.inc); $(BUILD)/boot.h has their sizes.
BOOT := src/boot

.PHONY: boot
boot: build/boot.sms

build/boot/tiles.inc: $(BOOT)/boot.py
	@mkdir -p $(@D)
	python3 -I $(BOOT)/boot.py tiles $@

build/boot.sms: $(BOOT)/boot.asm build/boot/tiles.inc $(BOOT)/boot.py
	sjasmplus --nologo --msg=war -Ibuild/boot --raw=$@ --lst=build/boot/boot.lst $(BOOT)/boot.asm
	python3 -I $(BOOT)/boot.py header $@

build/boot/boot.nms: $(BOOT)/boot.spec build/boot.sms tools/mknms.py
	@mkdir -p build/boot/ovl
	@rm -f build/boot/ovl/*.nms
	crc=$$(python3 -I -c 'import sys, zlib; print("%08X" % zlib.crc32(open(sys.argv[1], "rb").read()))' build/boot.sms) && \
	  sed "s/^cart .*/cart $$crc/" $(BOOT)/boot.spec > build/boot/boot.spec && \
	  python3 -I tools/mknms.py build/boot/boot.spec build/boot.sms build/boot/ovl && \
	  mv build/boot/ovl/$$crc.nms $@

# The cart in four 8K pieces and the overlay file, for bootpages.asm.
$(BOOT_BINS) $(BUILD)/boot.h: build/boot.sms build/boot/boot.nms
	@mkdir -p $(BUILD)/boot
	@for i in 0 1 2 3; do \
	  dd if=build/boot.sms of=$(BUILD)/boot/cart$$i.bin bs=8192 skip=$$i count=1 2>/dev/null || exit 1; \
	done
	cp build/boot/boot.nms $(BUILD)/boot/ovl.bin
	@echo "/* generated by the Makefile, do not edit */" > $(BUILD)/boot.h
	@echo "#define BOOT_CART_SIZE $$(wc -c < build/boot.sms | tr -d ' ')ul" >> $(BUILD)/boot.h
	@echo "#define BOOT_OVL_SIZE $$(wc -c < build/boot/boot.nms | tr -d ' ')ul" >> $(BUILD)/boot.h
