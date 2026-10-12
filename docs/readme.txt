NEXTMASTERSYSTEM - Master System games on the ZX Spectrum Next
Release 1, October 2026
============================================================

NextMasterSystem plays Sega Master System games on a Spectrum
Next. It is not an emulator. The Master System and the Next both
have a Z80, so the game's own code runs on the Next's CPU.
Before the game starts, NextMasterSystem dynamically builds 
the cartridge images and changes every place the game directly
calls the original Sega hardware.

The changes for each game are in a small file called an
overlay. Each gam estakes a custom overlay - which generally
fit exactly one exact dump of one game.

NextMasterSystem finds the overlay by the CRC32 of the cart
file, so the file name does not matter, as long as it's on 
the supported game catalogue list.

No games, original game code, or origial game assets come 
with NextMasterSystem. You need your own dumps of the carts
as .sms files.


WHAT YOU NEED
-------------

- A Spectrum Next with 2 MB of RAM.
- Your own .sms cart dumps, with a CRC32 from the list below.
- A Master System or Mega Drive pad in joystick port 1, or the
  keyboard.


INSTALLING
----------

With SPUN, the Next's package manager, install
NextMasterSystem and SPUN puts the files in a folder for you.

Without SPUN, make a folder on your SD card, for example /NMS/,
and copy the files from the zip into it:

/NMS/nms.nex    the program
/NMS/ovl/       one overlay per game, named by CRC32, for
                example 2728FAA3.nms, and the file index
/NMS/readme.txt this file

Keep ovl/ inside the folder that holds nms.nex. Start
NextMasterSystem from that folder: it looks for ovl/ in the
folder it was started from. Your .sms files can be in any
folder.


HOW TO START
------------

1. In the NextZXOS browser, go to the folder with nms.nex
   (for example /NMS/) and start nms.nex.
2. NextMasterSystem opens the browser again, showing only .sms
   files. Go to your carts and press ENTER on a game.
3. NextMasterSystem reads the .sms dump, matches and patches it.
   A 512K cart takes a few seconds to load. Some games take
   longer, because they prepare their graphics while loading.
4. The information screen shows the game, its state (see the
   list below) and the video rate it will use. Press any key
   or fire to start.
5. Press BREAK to leave the game. You go back to the browser
   and can pick another game. Press BREAK in the browser to
   leave NextMasterSystem and go back to NextZXOS.

If NextMasterSystem has no overlay for the cart, or the file is
a different dump from the one in the list, you go back to the
browser with a message on the bottom line, for example:
  Unknown game: no ovl/C4C0C368.nms for it.

The browser shows only .sms files while NextMasterSystem runs.
NextMasterSystem puts your own browser filter back when you
leave with BREAK. If you reset the Next while the
NextMasterSystem browser is on the screen, the .sms filter
stays set: change it back in the NextZXOS browser. Sorry, thems
the NextZXOS API rules, and naught I can do to change that ;-)


CONTROLS
--------

Master System     Next
--------------    ------------------------------------
D-pad             joystick 1, or Q A O P
Button 1          fire 1 / pad B, or SPACE
Button 2          fire 2 / pad C, or M
Pause             pad Start, or ENTER
Leave             BREAK (from the game to the browser,
                  from the browser to NextZXOS)

VIDEO RATE: 50 OR 60 HZ
-----------------------

Master System games were made for 50 Hz (PAL, Europe) or
60 Hz (NTSC, USA and Japan) consoles. When a game was made for
one rate only, NextMasterSystem switches the Next to that rate
when the game starts. A game sold for both runs at the rate
your Next started with. The information screen shows which.
If you want to force a SMS game to start in a different mode
switch to that mode before you launch the game.

The browser and the information screen always use the rate
your Next started with. If your monitor cannot show the
game's rate, press BREAK: you go back to the browser at your
own rate.


WHAT WORKS
----------

- Backgrounds, with scrolling in all directions and the Master
  System's split screens (a fixed score bar above or beside a
  scrolling playfield).
- Sprites, including tall (8x16) and double-size sprites.
- "Priority" tiles that the game draws in front of sprites.
- Master System sound on the AY chips. In tests, notes were
  within about 10 cents of a real Master System. The sound is
  close, not the same: the AY chip is not the Master System's
  sound chip.
- Bank switching for carts up to 512K, the Codemasters type of
  cart (Micro Machines) and its taller 224-line picture.
- Battery-backed cart RAM, as RAM only (see below).
- Pause.


KNOWN LIMITS IN EVERY GAME
--------------------------

- Games are not saved. Cart RAM (Phantasy Star) works while
  you play, but it is empty every time the game starts.
- Colours are close but not exact. Each of the Master System's
  4 levels of red, green and blue shows as one of the Next's
  8 levels, so some colours look a little brighter.
- No 8-sprites-per-line limit. A real Master System hides the
  ninth sprite on a line, so you may see sprites the original
  hides.
- Light Phaser, paddle, Sports Pad and 3-D glasses games are
  not supported.
- FM sound is not supported. Games that offer it play their
  normal music.


THE GAMES
---------

Each line gives the game, the CRC32 of the dump the overlay
fits, and what is known. These states come from tests in the
MAME emulator and on a real Next.

"Working": reaches gameplay and plays like a real Master
System, apart from the limits above.

  Alex Kidd in Miracle World           AED9AAC4
  Alien Syndrome                       5CBFE997
  Astro Warrior                        299CBB74
  Bubble Bobble                        E843BA7E
  Ecco the Dolphin                     6687FAB9
  Fantasy Zone                         65D7E4E0
  Fantasy Zone II                      B8B141F9
  Fushigi no Oshiro Pit Pot            E6795C53
      Japanese release, English text.
  Ghost House                          F1F8FF2D
  Hang On                              071B045E
  My Hero                              62F0C23D
  Pro Wrestling                        FBDE42D3
  R-Type                               BB54B6B0
  Spy vs Spy                           78D7FAAB
  Super Tennis                         914514E3
  Teddy Boy                            2728FAA3
  TransBot                             4BC42857
  Wonder Boy                           73705C02
  Wonder Boy III - The Dragon's Trap   679E1676
  Wonder Boy in Monster Land           8CBEF0C1
  Zillion                              5718762C

"Imperfect": playable, with problems you will notice.

  Black Belt                           DA3A2F57
      The picture flickers a lot after the screen stops
      scrolling, and in some frames the score bar at the
      top is damaged.
  Choplifter                           4A21C15F
      Takes about 4 seconds longer to reach play. While the
      screen scrolls, the mountains sometimes jump and the
      scrolling bands do not join.
  Micro Machines                       A577CE46
      A race takes longer to load than on a Master System.
  OutRun                               5589D8D2
      At the start of a race, a few frames take longer than
      a frame to prepare.
  Phantasy Star                        00BEF1D7
      Not saved. In conversations, the people are drawn
      over the text boxes and the text.
  Sonic The Hedgehog                   B519E833
      In Green Hill, some frames take longer than a frame
      to prepare, so the game can slow down.
  Space Harrier                        CA1D3752
      Small boxes in the sky colour round some objects near
      the horizon.


REPORTING A PROBLEM
-------------------

Report problems at:

  https://github.com/StalePixels/NextMasterSystem/issues

Please send:

- your Next: model (KS1, KS2, KS3 or other), core version,
  video output (HDMI, VGA or RGB), and whether it starts at
  50 or 60 Hz;
- the game and what you did (for example "pressed start,
  walked right for 10 seconds");
- what you saw and heard;
- if it stopped: what was on the screen, and the border
  colour. A red border means NextMasterSystem itself stopped.
