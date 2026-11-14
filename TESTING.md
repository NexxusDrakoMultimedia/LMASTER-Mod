<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# Testing the LMASTER Mod

What still needs a person playing the game in PCSX2, edition by
edition. The tools prove each patch writes the right bytes, but not that
the game does what we think with them. Anyone with the game and PCSX2
can help, and no code is needed.

This list is for **LMASTER Mod 0.5.0**, built from LMAST-Reverse commit
[`35090a0`](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/commit/35090a03a799ad1dab2dc0e0997c471e56223d88).
Its checks come from that commit's own
[`TESTING.md`](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/blob/35090a03a799ad1dab2dc0e0997c471e56223d88/TESTING.md)
and the status column of its
[`LMASTER_MOD.md`](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/blob/35090a03a799ad1dab2dc0e0997c471e56223d88/DOC/LMASTER_MOD.md#status).
The mod's code and its full test history live there; this file picks out
what the three editions players download still need.

## How to take part

1. **Pick a check** below, in the edition you play. Checks marked
   *short* take one match or a few screens; the others need part of a
   season or more.
2. **Patch your disc** as the [README](README.md) shows. Use a separate
   memory card for testing, so a test can't touch a career you care
   about.
3. **Play it** and note what you see. A screenshot (F8 in PCSX2) or a
   save state helps, and for numbers a save state is best: the exact
   value can be read from it.
4. **Report it**: open an
   [issue](https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/issues)
   or post on the [LMAST/SFCC English Fan
   Discord](https://discord.gg/7DNrGye9TZ) with the edition, the
   version, what you did, what you saw and the date. "It didn't work" is
   a result too: say what showed instead.

A confirmed check goes into LMAST-Reverse's docs as "Tested in PCSX2",
with who saw it and the date, and comes off this list at the next
release; the CHANGELOG then drops its *(needs extra testing)* mark.

## All three editions (Lite, Full and Max)

- [ ] **The travelling salesman's special training coach.** In a
      career from season 8, when the coach visits: hire him, and check
      that his "worked wonders" follow-up comes, then the "has waned"
      message 8 turns after it. Your players' attack patterns should be
      boosted in between. The Lead-Spike Boots (kick strength, tackle,
      contact strength) and the Football Theory Headphones (mental
      abilities) the same way.
- [ ] *Short.* **Pressing at every level**, by eye: a club of
      high-press players closes down harder than on the original disc.
      The patch is confirmed in memory; whether it plays differently is
      a judgement call.
- [ ] **PR events and the economy.** A PR event booked in a boom should
      succeed more often than in an average economy; in the original, a
      boom gave no bonus and an average economy took 10% off.
- [ ] *Short.* **The widescreen patch** in each edition: the picture is
      widened in a match, and menus and the HUD keep their shape.
- [ ] *Short.* **The title banner.** The title screen shows "LMASTER
      MOD" over the version and the edition's name in a navy and gold box
      at the top left, with the logo untouched and the menu below as
      before. Seen on a Lite disc in English; look in Full and Max, and
      switch the language to French, German, Spanish or Italian once.
- [ ] **The moving advert board at the last ground.** In a career with
      the moving board bought and a level-4 stadium, the rotating
      electric boards show at home games, and buying the LCD board
      replaces them; a computer club's level-4 ground shows the plain
      boards, not LCD. The board shop may also refuse the moving board at
      level 4: say what it does.
- [ ] *Short.* **The youth academy's second comment.** A youth
      candidate's page reads "almost no charisma" up to "superb
      charisma" under the summary, with no cut-off or stray spaces. Say
      which screen it was, and try another language if you can.

These can't easily be seen in the game, so a report is welcome if one
happens to show:

- **Long injuries** (the 18-month type) never start as short as a light
  knock.
- **Injuries to players aged 35 and over at full tiredness** look like
  other heavy injuries.
- **Overseas popularity** no longer jumps tenfold in one region (it
  depends on a hidden player rank).
- **A European Club Cup exit in the last 16** earns popularity (the
  points are hidden).

## Full and Max

- [ ] **The third tier's lower cups.** The German Club Cup's seeded
      bracket, one first-round tie in the first week of December and the
      other 7 clubs from the second round, played to its final; another
      nation's lower cup the same way; and the round names on the end of
      tournament screen.
- [ ] **Relegation follows this season's table.** At a season's end,
      the warning before it and the drop both follow the final table,
      not last season's.
- [ ] **A harsher end.** Finishing last in the second division ends the
      game after that one season.
- [ ] **The third tier's text in French, German, Italian or Spanish**
      (the English is tested): the advisor's introduction, the Game Over
      help, the 2nd German League's rules screen and its season-start
      news.
- [ ] **The real names in French, German, Italian or Spanish.** The news
      and rules texts that name a competition are hand-edited in those
      languages and haven't been seen in the game.
- [ ] *Short.* **Full's own save folders.** A Full career saves to
      `BESLES-54151-F000` and its VS data to `-V000` (Max's `-M` folder
      is tested).
- [ ] **The Special stadium late in a career**: it holds 100,000, and
      fills when sold out.
- [ ] **The "two months" and "nine months" injury lines** show on a
      long-injured player's condition, in each language you play in.
- [ ] **The modern font.** Look through the screens for text that is cut
      off, overlaps or sits badly: mainly the longest club, player and
      stadium names in the lists and tables, the news pages, the match
      screens (scoreboard, substitutions, results), the text-heavy
      messages, and the pad buttons and euro sign. Seen working on the
      pre-match and Select Hometown screens.
- [ ] **Computer clubs' sponsors and kit makers.** Every club shows a
      main sponsor and a supplier logo on its kit, each logo real and
      none blank, broken or oversized, two clubs differing, and the
      sponsors changing after a season. Seen on Real Betis, the English,
      Australian and New Zealand clubs and England's national team. Still
      to check: the other leagues, and the Italian, Spanish and Dutch
      clubs (Milan, Barcelona, Ajax and some smaller ones), whose kits are
      now generated in the club's colours: say which look wrong (colours
      or pattern) and what they should be.
- [ ] **LMAST Realism's club facilities screens, advertising boards and
      league logos on the disc.** They show the pack's pictures, with
      nothing garbled or missing: the facilities screens, an advertising
      board in a match, and the logos on the six-nation league screens.

## Max only

- [ ] **Long injuries twice as common**, mostly for tired players: over
      a season, rotate one squad and run another into the ground, and
      compare.
- [ ] **Overseas bases** cost twice as much to set up, invest in and keep
      up.
- [ ] **Transfer fees above £120M**, up to about £246M for the very best
      player at a top club, and whether the transfer screens show them
      correctly (lesser players' fees are tested).
- [ ] **The fanbase's crowds and TV offers**: a big fanbase brings
      bigger crowds and TV offers than a small one, and sells more
      merchandise at the top of the scale (lower merchandise income for
      a small fanbase is tested).
- [ ] **Training camps twice as dear, and tours three times**: a tour to
      a region where your club is little known about breaks even.
