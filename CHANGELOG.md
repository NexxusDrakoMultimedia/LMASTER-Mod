<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# Changelog

Every change the LMASTER Mod makes to *Let's Make a Soccer Team!*
(PAL, SLES-54151), listed against the original game ("vanilla").

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and version numbers follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Each change says which edition has it: **Lite** has the fixes only;
**Full** has the fixes plus every gameplay change. A change marked
*(needs extra testing)* is built and checked with tools, but hasn't been
tried in enough real games yet. Telling us how it goes is the point of
a testing release.

## [Unreleased]

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

[Unreleased]: https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/compare/v0.1.0-beta.2...HEAD
[0.1.0-beta.2]: https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/compare/v0.1.0-beta.1...v0.1.0-beta.2
[0.1.0-beta.1]: https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/releases/tag/v0.1.0-beta.1
