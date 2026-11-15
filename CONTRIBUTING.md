<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# Contributing to the LMASTER Mod

Thank you for helping. This guide covers how to report a problem, how to
test a release, and how to send a change to this repository. Everyone
taking part follows the [Code of Conduct](CODE_OF_CONDUCT.md).

This repository only **packages** the mod: it pins the LMAST-Reverse and
LMAST-Realism commits a release is built from, and builds, checks and
zips the patches. The mod's code, and the research behind every change,
live in
[LMAST-Reverse](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse).
If you want to change what the mod does to the game, start there (see
[Where a change belongs](#where-a-change-belongs)).

The maintainer, Pyra Drake (Nexxus Drako), reviews every change and makes
most of the in-game tests. Questions are welcome on the
[LMAST/SFCC English Fan Discord](https://discord.gg/7DNrGye9TZ) or in an
[issue](https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/issues).

## Ways to help

You don't need to write code to help.

| Kind | How |
|---|---|
| Test a release | Pick a check from [`TESTING.md`](TESTING.md), in the edition you play. Report the edition, the version, what you did, what you saw and the date. A screenshot (F8 in PCSX2) or a save state helps. You need your own copy of the game and PCSX2 |
| Report a bug | Open an [issue](https://github.com/NexxusDrakoMultimedia/LMASTER-Mod/issues) ([below](#reporting-a-bug)) |
| Tell us a change works | Reports that something works are as useful as bug reports, especially for changes marked *(needs extra testing)* in the [changelog](CHANGELOG.md) |
| Improve the docs | Fix an error or an unclear step in the README, `TESTING.md` or [`docs/RELEASING.md`](docs/RELEASING.md) |
| Improve the build | `tools/build_release.py` and its checks |

## Where a change belongs

| You want to... | Go to |
|---|---|
| Fix a bug in the game, or change what an edition does | [LMAST-Reverse](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse): each change is a switch of its `patch_disc.py`, documented in `DOC/LMASTER_MOD.md` |
| Change the pictures from LMAST Realism | [LMAST-Realism](https://github.com/NexxusDrakoMultimedia/LMAST-Realism) |
| Change how a release is built, checked, versioned or described | This repository |
| Fix the README, changelog wording, testing list or opening posts | This repository |

Which edition a change goes in is the maintainer's call. The rule is
that a fix that can't break a retail career already in progress goes in
Lite, and anything that may break such a save goes in Full or Max, which
keep their careers in their own save folders.

## Ground rules

- **No game data in the repo.** Disc images, game files, extracted
  data, textures, audio, saves and `.xdelta` patches are never
  committed (`.gitignore` covers `*.iso`, `*.cso`, `*.zso`, `*.chd`,
  `*.xdelta`, `build/` and `dist/`). Patches go on the GitHub release,
  not in git. The one file of someone else's in the repo is the font
  under `fonts/` (Apache License 2.0, with its licence beside it).
- **No test-only switches in a release.** `skip-tutorial` and `launcher`
  must never appear in `release.toml`. The build refuses them.
- **Label what isn't tested.** A change not yet tried in enough real
  games is marked *(needs extra testing)* in the changelog and has a
  check in `TESTING.md`.
- **Don't claim what you haven't seen.** Say what was tested, in which
  edition, by whom and when. Say what is still unknown instead of
  guessing.
- **Standard library only.** `tools/build_release.py` uses plain Python
  3.11+ and needs nothing installed.

## Reporting a bug

Please include:

- which edition (Lite, Full or Max) and which version of the mod,
- that your disc matches the Redump dump (disc
  [12334](https://redump.info/disc/12334/), SLES-54151). `HASHES.txt` in
  the release lists the hashes, and the patcher says if it doesn't fit,
- the PCSX2 version, and anything unusual in its settings,
- what you did, what you expected and what happened. A screenshot or a
  save state helps a lot.

Don't attach disc images or game files. Say which screen it was and
what showed instead.

## Setting up

You only need this to change the build or to make a release.

1. Python 3.11 or later (the build reads `release.toml` with `tomllib`).
2. Clone this repository beside two others, because the build looks for
   them as siblings:

   ```text
   LMASTER-Mod/      this repository
   LMAST-Reverse/    at the commit release.toml pins
   LMAST-Realism/    at the commit release.toml pins
   ```

3. Your own Redump image of the game, and optionally `xdelta3` on your
   `PATH`, so the build also applies each patch the way players do.

The font the title banner and `modern-font` draw with is already in
`fonts/`.

## Making a change

1. Fork the repository and make a branch from `main`. Check
   `git status` first: other work may be in progress in the same tree.
2. Keep the change small and say why in the commit. A doc change and the
   check or link it affects go in one commit.
3. If you changed the build, run it for real:

   ```bash
   python tools/build_release.py "<path to the Redump .iso>"
   ```

   It takes about ten minutes. It checks that the disc is the Redump
   dump, the LMAST-Reverse and LMAST-Realism clones are at the pinned
   commits and clean, `VERSION` is a valid semantic version,
   `CHANGELOG.md` has a section for it, `TESTING.md` names the same
   version and commit, and no edition includes a test-only switch. For
   each edition it builds the disc, makes the patch, applies it again
   and compares the result.
4. If you changed a doc or the README, check every link and anchor you
   touched, and that nothing still names an old version, commit or CRC.
5. Open a pull request against `main` and say what you ran and what you
   saw.

Releases are made by the maintainer, following
[`docs/RELEASING.md`](docs/RELEASING.md). That document is also the
place to read how versions are numbered.

## Style

- Every new `.py` file starts with
  `# SPDX-License-Identifier: GPL-3.0-or-later` and
  `# Copyright (C) 2026 Nexxus Drako Multimedia`; every new `.md` file
  starts with the same two lines as HTML comments. The exceptions are
  files under another licence, which say so.
- Files are UTF-8 with LF line endings and a final newline
  ([`.editorconfig`](.editorconfig)). Python uses four spaces and lines
  of at most 100 characters.
- Write for players: what they will notice, not addresses and hashes.
  Use short sentences, say which editions a change touches, and use no
  em dashes (rebuild the sentence with a full stop, comma, colon or
  brackets).
- The changelog follows
  [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and version
  numbers follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
  as [`docs/RELEASING.md`](docs/RELEASING.md) reads them for a game mod.
- Link a heading with its anchor, and before you rename or delete a
  heading, search the repository for links to it.

## Commits and pull requests

- Write the message in the imperative, saying what the change does, for
  example "Update PCSX2 CRCs for 0.5.1".
- Stage files by name, never `git add -A` or `git add .`, so scratch
  files and other work don't slip in.
- Credit co-authors, including AI assistants, with a
  `Co-Authored-By: Name <email>` line at the end of the message.
- In the pull request, say what you tested: the build, and any in-game
  check with what showed.

## Using AI assistants

Most of this project was written with Claude, and contributions made
with any AI assistant are welcome. You are responsible for what you
submit: check its claims, and credit the assistant with a
`Co-Authored-By` line. The project is declared AI:X on the
[0RWX scale](https://0rwx.com/) ([README](README.md#ai-use)); say in
your pull request how you used AI. [`AGENTS.md`](AGENTS.md) is the file
to give your assistant.

## Being credited

Everyone who contributes is listed in
[`CONTRIBUTORS.md`](CONTRIBUTORS.md). Add yourself in your pull request,
or say how you would like to be credited (your name, a handle, or not at
all) when you send a test result.

## License

By contributing, you agree that your work is licensed under the GNU
General Public License, version 3 or later ([`LICENSE`](LICENSE)), and
that you have the right to license it that way.
