<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# Releasing the LMASTER Mod

For the maintainer. Players want the [README](../README.md).

## How the repo fits together

| File | Holds |
|---|---|
| `VERSION` | the release's version, one line |
| `release.toml` | the LMAST-Reverse commit to build from, the vanilla disc's hashes, and the editions with their `patch_disc.py --mod` groups |
| `CHANGELOG.md` | what each release changes, in players' words ([Keep a Changelog](https://keepachangelog.com/en/1.1.0/)) |
| `tools/build_release.py` | builds, checks, hashes and zips a release |
| `README.md`, `CHANGELOG.md`, `LICENSE` | copied into every release zip |

The mod's code lives in LMAST-Reverse; this repo only decides **which
commit** and **which switches** make a release, and packages it. No disc
image, game file or `.xdelta` is ever committed here (`.gitignore`).
Patches go on the GitHub release.

## Version numbers

[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html),
`MAJOR.MINOR.PATCH[-PRERELEASE]`, read for a game mod as:

| Bump | When | Example |
|---|---|---|
| MAJOR | saves from the last version no longer work, or an edition's save folders change | 1.0.0 → 2.0.0 |
| MINOR | new fixes, restorations or gameplay changes; old saves still load | 0.1.0 → 0.2.0 |
| PATCH | a correction to an existing change, nothing new | 0.1.0 → 0.1.1 |
| `-beta.N` | a testing build before that version is final; bump N for each new test build | 0.1.0-beta.1 → 0.1.0-beta.2 → 0.1.0 |

While the major number is 0 the mod is still in testing, and any
release may change things. 1.0.0 is the first release you'd call
finished. Git tags are the version with a `v`: `v0.1.0-beta.1`.

Until a version is final, each new test build of it only bumps the
`-beta.N` number, whatever it adds or breaks: semver treats pre-releases
as unstable. So 0.1.0-beta.3 can follow beta.2 even with new features
and a save break. A save break still gets a warning at the top of its
CHANGELOG section and a line in the README's saves section.

## Making a release

1. **Pick the LMAST-Reverse commit.** Commit and push the work there
   first, so the release links to code anyone can see. Put its full hash
   in `release.toml` under `[source] commit`.
2. **Set the version** in `VERSION`.
3. **Update `CHANGELOG.md`.** Move what's under `## [Unreleased]` into a
   new `## [<version>] - <YYYY-MM-DD>` section (the build refuses to run
   without one), name the LMAST-Reverse commit, and add the compare link
   at the bottom. Write for players: what they'll notice, not addresses.
   Note which edition has each change, and mark anything not yet tested
   in PCSX2 *(needs extra testing)*; drop the mark once a test confirms it.
4. **Update the README**: the version (it appears in file names
   throughout), any step that changes, and each edition's PCSX2 CRC in the
   widescreen table and "Things to know". The CRCs change whenever an
   edition changes the game's program; take them from `HASHES.txt` after
   a first build, then build again.
5. **Build:**

   ```bash
   python tools/build_release.py "<path to the Redump .iso>"
   ```

   It refuses to build if the disc isn't the Redump dump, LMAST-Reverse
   isn't at the pinned commit or has uncommitted changes, `VERSION` isn't
   a valid semantic version, or an edition includes a test-only switch
   (`skip-tutorial`, `launcher`). For each edition it builds the disc,
   makes the patch, re-applies the patch and checks the result matches
   the built disc, and, if `xdelta3` is installed, applies it with
   xdelta3 too. `--keep-isos` keeps the built discs in `build/` for
   testing in PCSX2. The log is `build/build.log`.
6. **Test** every edition in PCSX2: boot, start a career, save, load.
7. **Commit and tag:**

   ```bash
   git commit -am "Release 0.1.0-beta.1"
   git tag -a v0.1.0-beta.1 -m "LMASTER Mod 0.1.0-beta.1"
   git push origin main v0.1.0-beta.1
   ```

8. **Publish** a GitHub release from the tag, attaching
   `dist/LMASTER-Mod-<version>.zip` and its `.sha256`. Paste that
   version's CHANGELOG section as the notes. Tick **Set as a pre-release**
   for a `-beta` version.

   ```bash
   gh release create v0.1.0-beta.1 dist/LMASTER-Mod-0.1.0-beta.1.zip dist/LMASTER-Mod-0.1.0-beta.1.zip.sha256 --prerelease --title "LMASTER Mod 0.1.0-beta.1 (testing)" --notes-file <notes.md>
   ```

## Adding an edition

Add an `[[edition]]` table to `release.toml` with a `name` and a `mod`
(any `patch_disc.py --mod` value, comma-separated switches allowed), and
a row for it in the README's edition table.
