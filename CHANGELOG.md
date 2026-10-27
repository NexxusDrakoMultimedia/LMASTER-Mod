<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# Changelog

Every change the LMASTER Mod makes to *Let's Make a Soccer Team!*
(PAL, SLES-54151), listed against the original game ("vanilla").

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and version numbers follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Each change says which editions have it. **Lite** has the fixes only;
**Full** adds the third tier, fairer fixtures and restored content;
**Max** adds the harder economy and balance changes on top of Full. (In
the 0.1.0 betas there were two editions, and the beta's "Full" was
today's Max.) A change marked *(needs extra testing)* is built and
checked with tools, but hasn't been tried in enough real games yet.
Please tell us how it goes.

## [Unreleased]

## [0.1.0] - 2026-10-27

The first stable release. Built from LMAST-Reverse commit
[`a3c3834`](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/commit/a3c38349e3da9e2c12b03f890194cc36d24cb66f).
This section lists every change from the original game. The beta
sections below show how 0.1.0 got here.

**Coming from 0.1.0-beta.3?**

- The beta's Full edition is now called **Max**. The new **Full** is Max
  without the harder economy and balance changes.
- Full now saves careers to its own `-F` folders. Max keeps `-M`, the
  folder beta.3's Full used, so beta.3 Full careers may load on Max (not
  tested; a new career is safest). Both now keep VS data in `-V`.
- Other Club Info now lists the third tier's clubs. The lower cups'
  brackets have their byes in the first round only, and the game's rules
  texts now describe the third tier.

### Added

- **A third tier** (Full and Max). Every nation now has a third
  division, played out of sight: English League 1, French League
  Division 3, Third German League, Italian League C, Spanish League
  Division 3 and Third Dutch League. The game had them planned, with
  names and clubs, but never used them.
  - Each season only the second division's **last** club goes down, and
    the third tier's winner comes up. Your rival can go down too.
  - In your nation, the second division keeps its real size (24 clubs in
    England): two of its clubs start in the third tier instead.
  - The third tier's clubs show in Other Club Info and the world
    rankings, and play their nation's lower cup (the English League Cup
    or the Club Cups), which now starts in the first week of December.
    *(the cups need extra testing)*
  - The game's rules texts, advisor and news explain the new rules in all
    five languages, and fix a few slips in those texts along the way.
    *(needs extra testing)*
- **The "Renew Mobile Site" PR event** (Lite, Full and Max). It was on
  the disc, complete with its text, but the game always hid it. It now
  turns up from the 2010–11 season like "Renew Home Page" does.
  *(needs extra testing)*
- **The "two months" and "nine months" injury lines** (Full and Max),
  cut before release, are back, in all five languages.
  *(needs extra testing)*
- **Separate saves** (Full and Max). Full saves careers to `-F` folders
  on the memory card and Max to `-M`, so neither mixes with the original
  game's careers, or with each other's. VS data goes to `-V`, shared by
  both. *(Max's folder is tested; Full's needs extra testing)*
- **Optional widescreen patches for PCSX2** (Lite, Full and Max): matches
  in 16:9 without stretching, menus and HUD kept at their normal shape.
  *(needs extra testing)*

### Changed

- **A harsher end** (Full and Max). Finish last in the second division
  and the game is over after that one season. (In the original, it took
  finishing in the bottom two for two seasons running.)
  *(needs extra testing)*
- **Fairer league fixtures** (Full and Max). No club plays more than two
  league games in a row at home, or away. Some leagues sent a club to
  the same ground up to nine times running.
- **A harder economy** (Max only):
  - Facilities cost more to build and to keep up, and much more at the
    top: the biggest stadium costs £350M.
  - Ticket prices go up to £80 (the original stopped at £50). Crowds
    shrink as the price climbs past £50.
  - Advertising buys half as much for the money, and the budget goes up
    to £10M.
  - Late-game income is smaller: sponsor fees and TV offers above £2M
    are halved above that amount, and season-ticket demand is halved.
- **Balance changes** (Max only):
  - Long injuries (six months or more) are about twice as common, mostly
    for tired players, so squad rotation matters more.
    *(needs extra testing)*
  - Transfer fees are twice as high, up to £250M, and follow player
    quality more: lesser players cost about four times the original fee,
    and the very best reach about £246M. *(fees above £120M need extra
    testing)*
  - Club reputation rises half as fast; losses are as before.
  - A bigger fanbase sells more merchandise and brings bigger crowds and
    TV offers; a small one brings less. *(crowds and TV need extra
    testing)*
  - Merchandise stock costs more to make, so it earns smaller profits.
  - PR events cost twice as much to book.
  - Overseas bases cost twice as much to set up, invest in and keep up.
    *(needs extra testing)*
  - Training camps cost twice as much, and tours three times as much.
    *(needs extra testing)*

### Fixed (Lite, Full and Max)

- **Main sponsor negotiation is back.** You can negotiate with your main
  sponsor on the Sponsor screen again, as in the Japanese release. The
  European release switched it off.
- **The World National Cup's results can be viewed.** Its final was on
  the last week of the year, so the season ended before you could look
  at the results. Both national cups now start one week earlier.
- **Your rival's manager matches the rival's style.** Every rival club
  got the same manager whatever its style.
- **Training camps train what they say.** Each camp trained as the next
  type on the list, so a goalkeeper camp trained no goalkeeping.
- **Seven English training camps are in the right towns.** Liverpool's
  camp was in Scunthorpe, Manchester's in West London, and five more were
  in the wrong place.
- **Santiago's training camp has its description.** It showed none.
- **Canberra's training camp lists all its clubs.** Fukuoka and Kanagawa
  never appeared.
- **Drills have the right names.** Twelve drills (75–86) showed the name
  of the next drill, so "Pass training." trained shooting.
- **Season tickets sell by club status.** Every club above the lowest
  status sold season tickets as if it were small.
- **Players imported from *Virtua Pro Football* keep their best play
  styles.** They usually arrived with one style, or none.
- **PR events follow the economy as intended.** A booming economy never
  gave its bonus, and an average one took 10% off every event's chance
  of success. *(needs extra testing)*
- **Overseas popularity no longer grows ten times too fast.** A
  misplaced decimal point made it rise tenfold in a region where your
  best player from there had one particular (hidden) rank.
  *(needs extra testing: the rank and popularity are hidden in game)*
- **Going out in the European Club Cup's last 16 earns popularity.** The
  game paid clubs knocked out in the last 32 instead.
  *(needs extra testing)*
- **Long injuries can't heal as fast as light ones.** One 18-month injury
  type could start as short as a light knock. *(needs extra testing)*
- **Injuries to players aged 35 and over at full tiredness use the right
  table.** The game read past the end of its injury table for them.
  *(needs extra testing)*

## [0.1.0-beta.3] - 2026-10-27

The third testing build of 0.1.0. Built from LMAST-Reverse commit
[`ef028dc`](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/commit/ef028dc0c663878deed6c51405c4caad0d487fd3).

> **Full needs a new career.** The third tier (below) makes the save
> bigger, so Full careers from 0.1.0-beta.2 or earlier won't load on
> this version. They stay on the memory card, and still load on the
> disc they came from. Lite saves are unaffected.

### Added (Full only)

- **A third tier.** Every nation now has a third division, played out of
  sight: English League 1, French League Division 3, Third German
  League, Italian League C, Spanish League Division 3 and Third Dutch
  League. The game had them planned, with names and clubs, but never
  used them.
  - Each season only the second division's **last** club goes down, and
    the third tier's winner comes up. Your rival can go down too.
  - In your nation, the second division keeps its real size (24 clubs in
    England): two of its clubs start in the third tier instead.
  - The third tier's clubs also play their nation's lower cup (the
    English League Cup or the Club Cups), which now starts in the first
    week of December. *(needs extra testing)*
  - Known issue: Club Info's **Other Club Info** doesn't list the third
    tier's clubs yet.

### Changed (Full only)

- **A harsher end.** Finish last in the second division and the game is
  over after that one season. (In the original, it took finishing in the
  bottom two for two seasons running.) *(needs extra testing)*
- **Reputation rises half as fast.** Every gain in club status (wins,
  draws, final places, the yearly bonus) is halved; losses are as
  before. *(needs extra testing)*
- **Transfer fees follow player quality more.** Lesser players cost
  about four times the original fee, and the very best players reach
  about £246M. *(needs extra testing)*
- **Overseas bases** still cost twice as much, but no longer do twice as
  much per level: each pound now buys half as much as in the original.
  *(needs extra testing)*

### Fixed (Lite and Full)

- **Overseas popularity no longer grows ten times too fast.** A
  misplaced decimal point made it rise tenfold in a region where your
  best player from there had one particular (hidden) rank.
  *(needs extra testing: the rank and popularity are hidden in game)*
- **Going out in the European Club Cup's last 16 earns popularity.** The
  game paid clubs knocked out in the last 32 instead.
  *(needs extra testing)*

## [0.1.0-beta.2] - 2026-10-26

The second testing build of 0.1.0. Built from LMAST-Reverse commit
[`36c794a`](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/commit/36c794a3bceeecf1460f6dc1e8009f648f136491).
Saves from 0.1.0-beta.1 still load in the same edition.

Tested in PCSX2 since beta.1, on the Full edition: careers save to
Full's own memory card folder, transfer fees come out doubled, and
merchandise stock costs half its price to make. Those three no longer
need extra testing.

### Restored (Lite and Full)

- **The "Renew Mobile Site" PR event is back.** It was complete on the
  disc, with its text, but the game always hid it. It now turns up from
  the 2010–11 season like "Renew Home Page" does. *(needs extra testing)*

### Fixed (Lite and Full)

- **PR events follow the economy as intended.** A booming economy never
  gave its bonus, and an average one took 10% off every event's chance
  of success. *(needs extra testing)*

### Changed (Full only)

- **PR events cost twice as much** to book (and refund twice as much if
  cancelled). *(needs extra testing)*
- **Training camps cost twice as much, and tours three times as much.**
  A tour to a region where your club is little known now only about
  breaks even; tour income is unchanged. *(needs extra testing)*

## [0.1.0-beta.1] - 2026-10-24

The first testing release. Built from LMAST-Reverse commit
[`2678125`](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/commit/26781257a18ca9844da389b2a12666f5897c9ee0).

### Added (Lite and Full)

- **Optional widescreen patches for PCSX2**, one for each edition: matches
  in 16:9 without stretching, menus and HUD kept at their normal shape.
  The same widescreen patch as for the original game, checked to touch
  none of the code LMASTER changes. *(needs extra testing)*

### Restored (Lite and Full)

- **Main sponsor negotiation is back.** You can negotiate with your main
  sponsor on the Sponsor screen again, as in the Japanese release. The
  European release switched it off.
- **The World National Cup's results can be viewed.** Its final was on
  the last week of the year, so the season ended before you could look
  at the results. Both national cups now start one week earlier.

### Fixed (Lite and Full)

- **Your rival's manager matches the rival's style.** Every rival club
  got the same manager whatever its style.
- **Training camps train what they say.** Each camp trained as the next
  type on the list, so a goalkeeper camp trained no goalkeeping.
- **Seven English training camps are in the right towns.** Liverpool's
  camp was in Scunthorpe, Manchester's in West London, and five more were
  in the wrong place.
- **Santiago's training camp has its description.** It showed none.
- **Canberra's training camp lists all its clubs.** Fukuoka and Kanagawa
  never appeared.
- **Drills have the right names.** Twelve drills (75–86) showed the name
  of the next drill, so "Pass training." trained shooting.
- **Season tickets sell by club status.** Every club above the lowest
  status sold season tickets as if it were small, so top clubs sold far
  fewer than they should.
- **Players imported from *Virtua Pro Football* keep their best play
  styles.** They usually arrived with one style, or none.
- **Long injuries can't heal as fast as light ones.** One 18-month injury
  type could start as short as a light knock. *(needs extra testing)*
- **Injuries to players aged 35 and over at full tiredness use the right
  table.** The game read past the end of its injury table for them.
  *(needs extra testing)*

### Changed (Full only)

- **Separate saves.** The Full edition saves careers and VS data in its
  own memory card folders, so it never mixes with saves from the
  original game. See the README to bring a career over.
- **Fairer league fixtures.** No club plays more than two league games in
  a row at home, or away. Some leagues sent a club to the same ground up
  to nine times running.
- **A harder economy**:
  - Facilities cost more to build and to keep up, and much more at the
    top: the biggest stadium costs £350M.
  - Ticket prices go up to £80 (the original stopped at £50). Crowds
    shrink as the price climbs past £50.
  - Advertising buys half as much for the money, and the budget goes up
    to £10M.
  - Late-game income is smaller: sponsor fees and TV offers above £2M
    are halved above that amount, and season-ticket demand is halved.
- **Balance changes** *(needs extra testing)*:
  - Long injuries (six months or more) are about twice as common, mostly
    for tired players, so squad rotation matters more.
  - The "two months" and "nine months" injury lines, cut before release,
    are back, in all five languages.
  - Overseas bases cost twice as much and do twice as much per level.
  - Transfer fees are twice as high, up to £250M.
  - A bigger fanbase sells more merchandise and brings bigger crowds and
    TV offers. A small one brings less.
  - Merchandise stock costs more to make, so it earns smaller profits.

[Unreleased]: https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/compare/v0.1.0-beta.3...v0.1.0
[0.1.0-beta.3]: https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/compare/v0.1.0-beta.2...v0.1.0-beta.3
[0.1.0-beta.2]: https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/compare/v0.1.0-beta.1...v0.1.0-beta.2
[0.1.0-beta.1]: https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/releases/tag/v0.1.0-beta.1
