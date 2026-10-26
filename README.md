<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# LMASTER Mod

**A fan-made fix-and-restore mod for *Let's Make a Soccer Team!* on
PlayStation 2 (European release).**

LMASTER fixes bugs the game shipped with, brings back features that were
switched off, and (in the Full edition) makes the economy and injuries
more of a challenge. The full list is in [CHANGELOG.md](CHANGELOG.md).

> **This is a testing release (0.1.0-beta.2).** It should play fine, but
> some changes haven't been seen in a real game yet. Keep a copy of your
> original disc image and your memory card, and please tell us what you
> find (see [Reporting a problem](#reporting-a-problem)).

---

## Which edition do I want?

| | **Lite** | **Full** |
|---|---|---|
| Bug fixes and restored features | ✅ | ✅ |
| Harder economy (dearer facilities, smaller late-game income) | | ✅ |
| Balance changes (injuries, transfers, fans, merchandise, PR, camps, tours) | | ✅ |
| Fairer league fixtures | | ✅ |
| Uses your existing saves | ✅ | Uses its own saves |

- **Pick Lite** if you want the game as it was meant to be, with the
  bugs fixed, and you want to carry on with your current careers.
- **Pick Full** if you want all that plus a tougher, deeper game. It
  keeps its saves apart from the original game, so nothing gets mixed up.

You can have both: patch two copies of the disc.

## What you need

1. **Your own copy of the game** as a disc image (`.iso`). The European
   release only: *Let's Make a Soccer Team!*, SLES-54151. This mod
   contains no game files. You must make the disc image from a game you
   own.
2. **The PCSX2 emulator** ([pcsx2.net](https://pcsx2.net)). The mod is
   made and tested on PCSX2 (see [Real PS2s](#real-ps2s)).
3. **A patching program** for `.xdelta` files:
   - Windows: **Delta Patcher** (recommended) or **xdelta UI**.
   - Mac or Linux: **xdelta3** (in most package managers, for example
     `brew install xdelta` or `sudo apt install xdelta3`).
4. **This mod's files**: `LMASTER-Mod-0.1.0-beta.2.zip` from the
   [Releases page](https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/releases).
   Unzip it anywhere.

## Step 1: Check your disc image

The patch only works on one exact disc image, the one listed by
[Redump](https://redump.info/disc/12334/). Your `.iso` must be
**3,548,184,576 bytes**, and its fingerprint must match one of these:

| Fingerprint | Value |
|---|---|
| CRC-32 | `1c34e97e` |
| MD5 | `adadf32f4fd418b60632813b011c3388` |
| SHA-1 | `78771805294c924b68fe4aa01ad52f70229abb9d` |

How to check on Windows: right-click an empty spot in the folder that
holds your `.iso`, choose **Open in Terminal**, and type
`Get-FileHash -Algorithm MD5 *.iso`. Or use any hashing program (if you
have 7-Zip, right-click the file and choose **CRC SHA**). These values
are also in `HASHES.txt`.

**Is your image a `.cso`, `.zso` or `.chd`?** Those are compressed and
can't be patched. Turn it back into an `.iso` first (for a CHD: `chdman
extractdvd`; for a CSO: **maxcso** with `--decompress`), check it as
above, then patch. You can compress the patched image again afterwards.

## Step 2: Patch it

**Make a copy of your original `.iso` first, and keep it.** You'll need
it for future versions of the mod.

**With Delta Patcher (Windows):**

1. Open Delta Patcher.
2. **Original file:** choose your `.iso`.
3. **XDelta patch:** choose `LMASTER-Mod-0.1.0-beta.2-Full.xdelta` or
   `LMASTER-Mod-0.1.0-beta.2-Lite.xdelta`.
4. Click the cog icon and **untick "Backup original file"** if you
   already made a copy (it saves several GB). Click **Apply patch**.
5. Wait. The disc is big, so this can take a minute or two. Delta
   Patcher overwrites the file you chose with the patched game, so
   rename it to something like `LMASTER Full.iso`.

**With xdelta3 (Mac, Linux or Windows command line):**

```bash
xdelta3 -d -s "original.iso" "LMASTER-Mod-0.1.0-beta.2-Full.xdelta" "LMASTER Full.iso"
```

**"The file you are trying to patch is not the right one"** means your
disc image doesn't match (Step 1). It may be compressed, a different
region, or a bad dump.

You can check the patched image against the values in `HASHES.txt`, but
if the patcher finished without an error, it's right.

## Step 3: Play

Open the patched `.iso` in PCSX2 just like the original. That's it.

### Real PS2s

The patched disc image is a normal PS2 disc image, so in principle it
should also work on a modded PlayStation 2 that can play disc images or
burned discs. Testing and supporting real hardware is beyond the scope
of this release, though: if you try it, you're on your own, but we'd
love to hear how it went. The widescreen patches are for PCSX2 only.

### Your saves

- **Lite** uses the same saves as the original game. Your careers carry
  on, now with the fixes. It's still wise to back up your memory card
  first (copy the card file from PCSX2's `memcards` folder).
- **Full** has its own save slots on the memory card, so the original
  game never sees Full's careers, and Full never sees the original's.
  This is on purpose: a career built under the original economy doesn't
  fit Full's rules, and the other way round. To start fresh, just start
  a new career. To bring an existing career over, see
  [Advanced: moving a career to Full](#advanced-moving-a-career-to-full).
  Importing players from *Virtua Pro Football* still works in both
  editions.

### Widescreen (optional)

The `widescreen` folder has a PCSX2 patch for each edition that shows
matches in 16:9 without stretching (you see more of the pitch at the
sides), and keeps the menus and the match HUD at their normal shape in
the middle of the screen. The intro and event movies stay stretched.

| Edition | Widescreen file |
|---|---|
| Full | `SLES-54151_E252BEB5.pnach` |
| Lite | `SLES-54151_CB787EAA.pnach` |

1. In PCSX2, open **Tools → Open Data Directory**, then the `patches`
   folder (create it if it isn't there).
2. Copy the file for your edition into it. You can copy both.
3. Right-click the patched game in PCSX2's game list, choose
   **Properties → Patches**, and tick **Widescreen 16:9**.
4. Boot the game. PCSX2 switches to 16:9 by itself.

It's the same widescreen patch as for the original game, under each
edition's new name; that patch only works on the original disc.

### Things to know

- **Savestates don't carry over** between the original and a patched
  disc. Save to the memory card in-game instead.
- **PCSX2 sees each patched disc as a different game.** Your per-game
  settings and any other `.pnach` cheats or patches for the original
  won't load on it automatically. The original's code is `3CB245D5`;
  Full's is `E252BEB5` and Lite's `CB787EAA` (also in `HASHES.txt`).
- Some changes show up only at certain times. The season plan, for
  example, can only be set at the start of a season.
- **Real logos and texture fixes aren't part of LMASTER.** They
  belong to the sister project
  [LMAST-Realism](https://github.com/NexxusDrakoMultimedia/LMAST-Realism).
  LMASTER only fixes and changes how the game plays.

## Reporting a problem

Found a bug, a crash, or something that doesn't look right? Please
[open an issue](https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/issues)
and tell us:

- which edition (Full or Lite) and version (0.1.0-beta.2),
- what you were doing, and what happened,
- a screenshot if you can.

Reports that a change works are just as useful, especially for the ones
marked *(needs extra testing)* in the [changelog](CHANGELOG.md).

## Advanced: moving a career to Full

This needs Python and the
[LMAST-Reverse](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse)
tools. They copy a career save to the Full edition's slot and leave the
original untouched. For a folder memory card:

```bash
python SRC/save.py rename <card>/BESLES-54151-G003 <card>
```

The steps for a single-file card are in LMAST-Reverse's
[INSTALL.md](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/blob/master/INSTALL.md#taking-a-career-over-to-a-modded-disc).

---

## Credits

**LMASTER Mod** by **Pyra Drake** of
**[Nexxus Drako Multimedia](https://github.com/NexxusDrakoMultimedia)**.

- Reverse engineering, mod design and testing: Pyra Drake / Nexxus Drako
  Multimedia, through the
  [LMAST-Reverse](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse)
  project. The reverse engineering was done with Claude (Anthropic).
- *Let's Make a Soccer Team!* © SEGA. This is an unofficial fan
  project. It isn't made, endorsed or supported by SEGA, and it
  contains none of the game's files.
- Widescreen patch from LMAST-Reverse.
- Disc fingerprints from [Redump](https://redump.info/).

See [CREDITS.md](CREDITS.md) for more.

## Disclaimer

**DISCLAIMER:** This project is a non-profit, fan-made modification and
is not affiliated with or endorsed by SEGA, Adidas, or any football
competition, league, club, federation, manager, chairman, or player.

## License

Copyright © 2026 Nexxus Drako Multimedia.

The LMASTER Mod patches, tools and documents are free software under the
**GNU General Public License, version 3 or (at your option) any later
version** (GPL-3.0-or-later). See [LICENSE](LICENSE). The game itself
is not covered by this license and remains SEGA's.

## For maintainers

How releases are built and numbered: [docs/RELEASING.md](docs/RELEASING.md).
