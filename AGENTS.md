<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# AGENTS.md

Instructions for any AI assistant working on this repo, such as ChatGPT
(Codex), Gemini, Perplexity or Claude. They apply whichever tool you are.

## What this repo is

The LMASTER Mod is a fan-made fix-and-restore mod for the PAL PS2 game
*Let's Make a Soccer Team!* (SLES-54151). This repo is **packaging
only**: it pins the commits of LMAST-Reverse (the mod's code) and
LMAST-Realism (pictures) a release is built from, builds one xdelta patch
per edition (Lite, Full, Max), checks them, and zips them with the
player docs. It contains no game data, no mod code and no `.xdelta`.

| Path | Holds |
|---|---|
| `VERSION` | the release's version, one line |
| `release.toml` | the LMAST-Reverse and LMAST-Realism commits to build from, the vanilla disc's hashes, and the editions with their `patch_disc.py --mod` groups |
| `CHANGELOG.md` | what each release changes, in players' words (Keep a Changelog) |
| `TESTING.md` | what each edition still needs tested in PCSX2, for the current version |
| `README.md` | the players' guide: editions, patching, saves, widescreen, reporting |
| `CREDITS.md`, `CONTRIBUTORS.md` | credits |
| `tools/build_release.py` | builds, checks, hashes and zips a release |
| `fonts/` | Roboto Condensed (Apache License 2.0) that `modern-font` and the title banner draw with, and its licence |
| `docs/RELEASING.md` | the maintainer's release guide, including how versions are numbered |
| `docs/social/` | the opening posts of the mod's Discord and Neoseeker threads |
| `build/`, `dist/` | scratch and output, git-ignored. The build clears `build/` |

The mod's code and research live in the sibling repos
[LMAST-Reverse](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse)
(`../LMAST-Reverse`; `DOC/LMASTER_MOD.md` documents every switch) and
[LMAST-Realism](https://github.com/NexxusDrakoMultimedia/LMAST-Realism)
(`../LMAST-Realism`). A change to what the mod does to the game belongs
there, not here.

## Before you start

- Run `git status`. Other work may be in the tree. Stage files by name
  (never `git add -A` or `git add .`).
- Read `docs/RELEASING.md` before touching a version, a pin, the
  changelog or `TESTING.md`. It is the source of truth for the process.
- Find out who you are working with from git (`git config user.name`)
  before you write a credit. The maintainer is Pyra Drake, also known as
  Nexxus Drako.

## Commands

Python 3.11+ (standard library only). Run from the repo root.

```bash
python tools/build_release.py "<path to the Redump .iso>"                 # build, check, zip
python tools/build_release.py "<iso>" --keep-isos                          # also keep the built discs in build/
git log --format="%(trailers:key=Co-Authored-By,valueonly)" | sort | uniq -c   # co-author counts
```

The build takes about ten minutes, so run it in the background. It
refuses to run unless the disc is the Redump dump, the LMAST-Reverse and
LMAST-Realism clones sit at the commits `release.toml` pins and are
clean, `VERSION` is valid semver, `CHANGELOG.md` has a section for it,
`TESTING.md` names the same version and commit, and no edition includes a
test-only switch. It also fails when `modern-font`, `title-banner` or
`realism` is skipped for a missing file. It passes `VERSION` to
`patch_disc.py` as `--version`, which the title banner shows.

There is no test suite: the build is the check. For a doc-only change,
`check_changelog` and `check_testing` in `tools/build_release.py` verify
the parts the build would refuse.

## Build manifests

LMAST-Reverse's `SRC/manifest.py` writes a small JSON file for a build:
the edition, every switch with its group and description, the options
(`--eras-offset`, `--skip-nation`, font and Realism names, `--version`),
the LMASTER seed and the tools commit. It is documented in
`../LMAST-Reverse/DOC/LMASTER_MOD.md#build-manifests`. In this repo it
matters in two places:

- **Bug reports.** Ask for the player's `<name>.manifest.json` (File >
  Build disc writes one beside the patch) or, for a release patch, the
  edition and version. `python SRC/manifest.py show <file>` in
  LMAST-Reverse prints what that build changes from the retail game, and
  `diff <a> <b>` compares two builds.
- **Releases.** `tools/build_release.py` runs `manifest.py make` for each
  edition (the edition's `--mod` and the release's `--version`, with
  `--no-date --no-writes`, the patch, the Redump disc's SHA-1 and the
  executable's CRC) and ships `manifest-<edition>.json` in the release
  folder. It then runs `manifest.py check` against the edition in
  `release.toml` and the pinned commit, and checks the manifest's CRC
  against the one the build found. The build refuses to run if the
  pinned LMAST-Reverse has no `SRC/manifest.py`, so a pin from before
  `d8ab61f` no longer builds. The first full build to run this is the
  release after 0.6.0.

## Making a release

`docs/RELEASING.md` has the full steps. In short: pin the commits, set
`VERSION`, add the CHANGELOG section, bring `TESTING.md` up to date,
update the README, build, test in PCSX2, commit, tag, publish, announce.

- **Numbering** (SemVer, read for a game mod): MAJOR for a save break,
  MINOR for new fixes or gameplay, PATCH for a correction with nothing
  new. While the major number is 0, a change that would be MAJOR bumps
  MINOR. Git tags are the version with a `v`.
- **The PCSX2 CRCs are in the README** (the widescreen table and "Things
  to know"). They change whenever an edition changes the game's
  executable, and only a build shows the new values (`HASHES.txt`). The
  README is copied into the zip, so update it and **build again**;
  the CRCs come out the same.
- **`TESTING.md`** is derived from LMAST-Reverse's `TESTING.md` and the
  untested rows of `DOC/LMASTER_MOD.md` at the pinned commit, never from
  memory. Add a check for each new *(needs extra testing)* change, filed
  under the editions that have it, and drop checks confirmed since.
- **Don't tag, push, publish or post** unless the user asks. Each is
  public. Pushing a tag and creating the release are separate asks from
  committing.
- Release posts: a full opening post per thread is kept in
  `docs/social/`; each release's announcement is written fresh from its
  CHANGELOG section and isn't kept in git. Keep a patch release's posts
  short.

## Conventions

- Every new `.py` file starts with
  `# SPDX-License-Identifier: GPL-3.0-or-later` and
  `# Copyright (C) 2026 Nexxus Drako Multimedia`; every new `.md` file
  starts with the same two lines as HTML comments. Files under another
  licence say so.
- UTF-8, LF line endings, a final newline, four-space Python, lines of
  at most 100 characters (`.editorconfig`).
- Write for players: short sentences, what they will notice, which
  editions have it. No em dashes: rebuild the sentence with a full stop,
  comma, colon or brackets.
- A change not yet tried in enough real games is marked
  *(needs extra testing)* in the changelog, and has a check in
  `TESTING.md`.
- A result from the game names who saw it and when. Don't claim a test
  nobody ran. If you couldn't run a step, say so.
- The `docs/social/` files are pasted as they are, so they carry no
  licence header. Discord posts hold at most 2,000 characters. Neoseeker
  uses nTags: `[link name=words]url[/link]`, `[ul]` and `[li]`, not
  BBCode `[url]` or `[list]`.
- Before you rename or delete a heading, search for links to its anchor
  and update them.

## Boundaries

- **No game data.** Never commit or attach a disc image, an extracted
  game file, a save, or a `.xdelta`. `.gitignore` covers them. The one
  third-party file in the repo is the font in `fonts/`.
- **Test-only switches never ship.** `skip-tutorial` and `launcher` must
  not appear in `release.toml`.
- **The pins decide the release.** Changing `release.toml`'s commits
  changes what ships: bump the version, `TESTING.md` and the changelog
  with it, and rebuild. The README's links to LMAST-Reverse's
  `LMASTER_MOD.md` carry the same hash.
- **Don't reach into the sibling repos from here.** If a fix is needed
  in LMAST-Reverse or LMAST-Realism, say so and let the user make it
  there, then pin the new commit.
- **Everything outward-facing waits for the user's say-so**: pushing,
  tagging, publishing a release, and posting announcements.

## Environment notes

- The primary platform is Windows. In Git Bash, `/c/...` paths work for
  git and shell tools but **not** for Windows Python, which reads
  `/c/Users/...` as `C:\c\Users\...`. Pass Windows paths
  (`C:\Users\...`) to `tools/build_release.py`, for example through
  PowerShell.
- Build in the background and wait for it to finish. Don't poll, and
  don't start a second build while one is running.
- The build clears `build/`, so keep drafts (release notes, posts) out
  of it, or write them after the build finishes.
- The disc image used to build is the user's own Redump dump, kept in
  the LMAST-Reverse folder.
- PCSX2 picks a widescreen patch by the disc's CRC from the filename,
  `SLES-54151_<CRC>.pnach`, so the old CRC's file stops applying when a
  release changes it.

## Credit

- Credit yourself on a commit with a `Co-Authored-By` line at the end of
  the message, as the user's instructions give it.
- Add a person to `CONTRIBUTORS.md` when their test result or report
  goes into a document, by the name they choose.
