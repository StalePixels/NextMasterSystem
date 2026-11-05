# Spider-Man (USA, Europe, Brazil) (En), CRC32 908FF25C, 256K, Sega mapper.
# Pokes: codes from the libretro-database cheat catalogue (cht/Sega - Master System -
# Mark III/), CC-BY-SA 4.0: https://github.com/libretro/libretro-database
# Drafted by tools/mkspec.py from sitescan output with a reference I/O log (600 s of
# random input).
# Decisions:
# - $0030 is the io vector. RST $30 is free: the game uses $0008-$0028 and the bytes
#   $002D-$0037 are zero. $0000 cannot be the io vector: the cart starts with
#   DI; LD IY,$DF70; JP $0212, and the vector's JP would overwrite the LD IY, so the game
#   ran with IY wrong and hung before its first VDP write. The game starts at $0000.
# - The JP (IX) at $70A9 and $70BD enter the unrolled OUTI block $71EB-$726A at a
#   2-OUTI step that $6D2E-$6D4D works out from the byte count; every OUTI in the block
#   is a site.
# - $707A and $707F are in the routine $7078, which nothing in the cart calls (verdict
#   unused). The other byte patterns that no path reached are in the graphics banks 3,
#   4, 11, 12 and 13 (verdict false).
# - No priority: no name table cell in stage 1 has the priority bit.
name Spider-Man
cart 908FF25C
hz any		; No-Intro regions USA, Europe, Brazil
vector 30 io
asm 00213 2   ; IM 1 -> IM 2
    im 2
endasm
site 00008   ; OUT ($BF),A
site 00010   ; OUT ($BE),A
site 0001A   ; IN A,($BE)
site 0003B   ; IN A,($BF)
site 00235   ; IN A,($DC)
site 0023D   ; IN A,($DD)
site 00C2D   ; IN A,($DD)
site 00C47   ; IN A,($7E)
site 00C58   ; IN A,($DC)
site 0119F   ; IN A,($DC)
site 056E2   ; OTIR
site 06EAC   ; OUT ($BF),A
site 06EB9   ; OUT ($BF),A
site 06ECE   ; OUT ($BF),A
site 06EDD   ; OUT ($BF),A
site 06EE9   ; OUT (C),A
site 06EEE   ; OUT (C),A
site 06EF3   ; OUT (C),A
site 06EF8   ; OUT (C),A
site 06EFD   ; OUT (C),A
site 06F02   ; OUT (C),A
site 06F07   ; OUT (C),A
site 06F0C   ; OUT (C),A
site 06F1D   ; OUT ($BF),A
site 06F2A   ; OUT ($BF),A
site 06F31   ; OUT ($BE),A
site 06F36   ; OUT ($BE),A
site 06F3B   ; OUT ($BE),A
site 06F40   ; OUT ($BE),A
site 06F45   ; OUT ($BE),A
site 06F4A   ; OUT ($BE),A
site 06F4F   ; OUT ($BE),A
site 06F54   ; OUT ($BE),A
site 06F59   ; OUT ($BE),A
site 06F5E   ; OUT ($BE),A
site 06F63   ; OUT ($BE),A
site 06F68   ; OUT ($BE),A
site 06F6D   ; OUT ($BE),A
site 06F72   ; OUT ($BE),A
site 06F77   ; OUT ($BE),A
site 06F7C   ; OUT ($BE),A
site 06F81   ; OUT ($BE),A
site 06F86   ; OUT ($BE),A
site 06F8B   ; OUT ($BE),A
site 06F90   ; OUT ($BE),A
site 06F95   ; OUT ($BE),A
site 06F9A   ; OUT ($BE),A
site 06F9F   ; OUT ($BE),A
site 06FA4   ; OUT ($BE),A
site 06FA9   ; OUT ($BE),A
site 06FAE   ; OUT ($BE),A
site 06FB3   ; OUT ($BE),A
site 06FB8   ; OUT ($BE),A
site 06FBD   ; OUT ($BE),A
site 06FC2   ; OUT ($BE),A
site 06FC7   ; OUT ($BE),A
site 06FCC   ; OUT ($BE),A
site 06FD1   ; OUT ($BE),A
site 06FD6   ; OUT ($BE),A
site 06FDB   ; OUT ($BE),A
site 06FE0   ; OUT ($BE),A
site 06FE5   ; OUT ($BE),A
site 06FEA   ; OUT ($BE),A
site 06FEF   ; OUT ($BE),A
site 06FF4   ; OUT ($BE),A
site 06FF9   ; OUT ($BE),A
site 06FFE   ; OUT ($BE),A
site 07003   ; OUT ($BE),A
site 07008   ; OUT ($BE),A
site 0700D   ; OUT ($BE),A
site 07012   ; OUT ($BE),A
site 07017   ; OUT ($BE),A
site 0701C   ; OUT ($BE),A
site 07021   ; OUT ($BE),A
site 07026   ; OUT ($BE),A
site 0702B   ; OUT ($BE),A
site 07030   ; OUT ($BE),A
site 07035   ; OUT ($BE),A
site 0703A   ; OUT ($BE),A
site 0703F   ; OUT ($BE),A
site 07044   ; OUT ($BE),A
site 07049   ; OUT ($BE),A
site 0704E   ; OUT ($BE),A
site 07053   ; OUT ($BE),A
site 07058   ; OUT ($BE),A
site 0705D   ; OUT ($BE),A
site 07062   ; OUT ($BE),A
site 07067   ; OUT ($BE),A
site 0706C   ; OUT ($BE),A
site 0709A   ; OUT ($BF),A
site 0709F   ; OUT ($BF),A
site 070AE   ; OUT ($BF),A
site 070B3   ; OUT ($BF),A
site 070CB   ; OUTI
site 070CD   ; OUTI
site 070D0   ; OUTI
site 070D2   ; OUTI
site 070D5   ; OUTI
site 070D7   ; OUTI
site 070DA   ; OUTI
site 070DC   ; OUTI
site 070DF   ; OUTI
site 070E1   ; OUTI
site 070E4   ; OUTI
site 070E6   ; OUTI
site 070E9   ; OUTI
site 070EB   ; OUTI
site 070EE   ; OUTI
site 070F0   ; OUTI
site 070F3   ; OUTI
site 070F5   ; OUTI
site 070F8   ; OUTI
site 070FA   ; OUTI
site 070FD   ; OUTI
site 070FF   ; OUTI
site 07102   ; OUTI
site 07104   ; OUTI
site 07107   ; OUTI
site 07109   ; OUTI
site 0710C   ; OUTI
site 0710E   ; OUTI
site 07111   ; OUTI
site 07113   ; OUTI
site 07116   ; OUTI
site 07118   ; OUTI
site 0711B   ; OUTI
site 0711D   ; OUTI
site 07120   ; OUTI
site 07122   ; OUTI
site 07125   ; OUTI
site 07127   ; OUTI
site 0712A   ; OUTI
site 0712C   ; OUTI
site 0712F   ; OUTI
site 07131   ; OUTI
site 07134   ; OUTI
site 07136   ; OUTI
site 07139   ; OUTI
site 0713B   ; OUTI
site 0713E   ; OUTI
site 07140   ; OUTI
site 07143   ; OUTI
site 07145   ; OUTI
site 07148   ; OUTI
site 0714A   ; OUTI
site 0714D   ; OUTI
site 0714F   ; OUTI
site 07152   ; OUTI
site 07154   ; OUTI
site 07157   ; OUTI
site 07159   ; OUTI
site 0715C   ; OUTI
site 0715E   ; OUTI
site 07161   ; OUTI
site 07163   ; OUTI
site 07166   ; OUTI
site 07168   ; OUTI
site 0716B   ; OUTI
site 0716D   ; OUTI
site 07170   ; OUTI
site 07172   ; OUTI
site 07175   ; OUTI
site 07177   ; OUTI
site 0717A   ; OUTI
site 0717C   ; OUTI
site 0717F   ; OUTI
site 07181   ; OUTI
site 07184   ; OUTI
site 07186   ; OUTI
site 07189   ; OUTI
site 0718B   ; OUTI
site 0718E   ; OUTI
site 07190   ; OUTI
site 07193   ; OUTI
site 07195   ; OUTI
site 07198   ; OUTI
site 0719A   ; OUTI
site 0719D   ; OUTI
site 0719F   ; OUTI
site 071A2   ; OUTI
site 071A4   ; OUTI
site 071A7   ; OUTI
site 071A9   ; OUTI
site 071AC   ; OUTI
site 071AE   ; OUTI
site 071B1   ; OUTI
site 071B3   ; OUTI
site 071B6   ; OUTI
site 071B8   ; OUTI
site 071BB   ; OUTI
site 071BD   ; OUTI
site 071C0   ; OUTI
site 071C2   ; OUTI
site 071C9   ; OUT ($BF),A
site 071CD   ; OUT ($BF),A
site 071D9   ; OUT (C),A
site 071DD   ; OUT ($BF),A
site 071E4   ; OUT ($BF),A
site 071EB   ; OUTI
site 071ED   ; OUTI
site 071EF   ; OUTI
site 071F1   ; OUTI
site 071F3   ; OUTI
site 071F5   ; OUTI
site 071F7   ; OUTI
site 071F9   ; OUTI
site 071FB   ; OUTI
site 071FD   ; OUTI
site 071FF   ; OUTI
site 07201   ; OUTI
site 07203   ; OUTI
site 07205   ; OUTI
site 07207   ; OUTI
site 07209   ; OUTI
site 0720B   ; OUTI
site 0720D   ; OUTI
site 0720F   ; OUTI
site 07211   ; OUTI
site 07213   ; OUTI
site 07215   ; OUTI
site 07217   ; OUTI
site 07219   ; OUTI
site 0721B   ; OUTI
site 0721D   ; OUTI
site 0721F   ; OUTI
site 07221   ; OUTI
site 07223   ; OUTI
site 07225   ; OUTI
site 07227   ; OUTI
site 07229   ; OUTI
site 0722B   ; OUTI
site 0722D   ; OUTI
site 0722F   ; OUTI
site 07231   ; OUTI
site 07233   ; OUTI
site 07235   ; OUTI
site 07237   ; OUTI
site 07239   ; OUTI
site 0723B   ; OUTI
site 0723D   ; OUTI
site 0723F   ; OUTI
site 07241   ; OUTI
site 07243   ; OUTI
site 07245   ; OUTI
site 07247   ; OUTI
site 07249   ; OUTI
site 0724B   ; OUTI
site 0724D   ; OUTI
site 0724F   ; OUTI
site 07251   ; OUTI
site 07253   ; OUTI
site 07255   ; OUTI
site 07257   ; OUTI
site 07259   ; OUTI
site 0725B   ; OUTI
site 0725D   ; OUTI
site 0725F   ; OUTI
site 07261   ; OUTI
site 07263   ; OUTI
site 07265   ; OUTI
site 07267   ; OUTI
site 07269   ; OUTI
site 0740A   ; OUT ($BE),A
site 0742B   ; OUT ($BE),A
site 07442   ; OUT ($BF),A
site 07446   ; OUT ($BF),A
site 0744B   ; OUT ($BE),A
site 07450   ; OUT ($BE),A
site 07455   ; OUT ($BE),A
site 0745A   ; OUT ($BF),A
site 0745E   ; OUT ($BF),A
site 07465   ; OUT ($BF),A
site 07469   ; OUT ($BF),A
site 074BB   ; OUT ($BE),A
site 24480   ; OUT ($7F),A
site 24495   ; OUT ($7F),A
site 2449E   ; OUT ($7F),A
site 244A9   ; OUT ($7F),A
site 244D4   ; OUT ($7F),A
site 24628   ; OUT ($7F),A
site 2465F   ; OUT ($7F),A
site 24668   ; OUT ($7F),A
site 24683   ; OUT ($7F),A
site 24687   ; OUT ($7F),A
site 2473D   ; OUT ($7F),A
site 24753   ; OUT ($7F),A
site 2476B   ; OUT ($7F),A
site 2476F   ; OUT ($7F),A
site 2477D   ; OUT ($7F),A
site 247BB   ; OUT ($7F),A
mapst 00047   ; LD ($FFFF),A
mapst 0004E   ; LD ($FFFF),A
mapldk 00215   # LD HL,$FFFC; LD (HL),$00
maphl 0021B   # LD (HL),$00, HL = $FFFD
maphl 0021E   # LD (HL),$01, HL = $FFFE
maphl 00221   # LD (HL),$02, HL = $FFFF
mapst 00269   ; LD ($FFFF),A
mapst 002C4   ; LD ($FFFF),A
mapst 002F1   ; LD ($FFFF),A
mapst 002FA   ; LD ($FFFF),A
mapst 00A5F   ; LD ($FFFF),A
mapst 00A79   ; LD ($FFFF),A
mapst 00C9D   ; LD ($FFFF),A
mapst 00CA3   ; LD ($FFFF),A
mapst 00E2C   ; LD ($FFFF),A
mapst 00E64   ; LD ($FFFF),A
mapst 00E7C   ; LD ($FFFF),A
mapst 00F46   ; LD ($FFFF),A
mapst 00FCC   ; LD ($FFFF),A
mapst 00FD3   ; LD ($FFFF),A
mapst 00FDC   ; LD ($FFFF),A
mapst 00FF1   ; LD ($FFFF),A
mapst 01017   ; LD ($FFFF),A
mapst 01168   ; LD ($FFFF),A
mapst 01172   ; LD ($FFFF),A
mapst 01181   ; LD ($FFFF),A
mapst 0118B   ; LD ($FFFF),A
mapst 041A0   ; LD ($FFFF),A
mapst 041B1   ; LD ($FFFF),A
mapst 061D9   ; LD ($FFFF),A
mapst 06214   ; LD ($FFFF),A
mapst 0664C   ; LD ($FFFF),A
mapst 0666C   ; LD ($FFFF),A
mapst 07367   ; LD ($FFFF),A
mapst 073D4   ; LD ($FFFF),A
mapst 073E2   ; LD ($FFFF),A
mapst 073FA   ; LD ($FFFF),A
mapst 074E1   ; LD ($FFFF),A
mapst 07522   ; LD ($FFFF),A
mapst 07528   ; LD ($FFFF),A
mapst 07575   ; LD ($FFFF),A
mapst 0757B   ; LD ($FFFF),A
mapst 075BC   ; LD ($FFFF),A
mapst 075C2   ; LD ($FFFF),A
mapst 075F4   ; LD ($FFFF),A
mapst 075FA   ; LD ($FFFF),A
mapst 076B9   ; LD ($FFFF),A
mapst 07CD1   ; LD ($FFFF),A
mapst 07CEB   ; LD ($FFFF),A
mapst 07D9D   ; LD ($FFFF),A
mapst 07DBF   ; LD ($FFFF),A

# Spider-Man (USA, Europe, Brazil).cht, "Infinite Health": RAM $DF7F is the health, $FF full
poke "Infinite health"
ar 00DF-7FFF
endpoke

# Spider-Man (USA, Europe, Brazil).cht, "Infinite Time": RAM $DF7A is the ones digit of the
# level clock, and $DF7B the tens digit. The code holds the ones digit at 8, so the clock never
# reaches 0 (at 0 the game takes a life). The clock shows 08 and the life that a level start
# spends is not spent
poke "Infinite time"
ar 00DF-7A08
endpoke
