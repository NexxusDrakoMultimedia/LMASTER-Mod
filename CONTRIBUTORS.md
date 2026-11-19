<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# Contributors

The people, projects and communities who have helped the LMASTER Mod.
The copyright notices in each file name the copyright holder; this file
records who did the work and who made it possible. [`CREDITS.md`](CREDITS.md)
is the short version players see, and the research behind each change is
credited in
[LMAST-Reverse's `CONTRIBUTORS.md`](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse/blob/master/CONTRIBUTORS.md).

## Maintainer

| Name | Role | Contact |
|---|---|---|
| **Pyra Drake**, also known as **Nexxus Drako** (Nexxus Drako Multimedia) | project owner and maintainer; designs the mod, chooses what goes in each edition, runs the in-game tests in PCSX2, builds and publishes each release, and reviews every change | [NexxusDrakoMultimedia](https://github.com/NexxusDrakoMultimedia) on GitHub |

## Code and documentation

| Contributor | Contribution |
|---|---|
| **Pyra Drake** (Nexxus) | every commit in the repository, the choices behind each edition and release, and the in-game testing of the mod |
| **Claude** (Anthropic; Claude Opus 5.5 and Claude Sonnet 5.5) | the build script, the README, changelog, testing list, release guide and announcements, written under the maintainer's direction; credited with a `Co-Authored-By` line on each commit it helped write |

The README's [AI use](README.md#ai-use) section explains how AI is used
in this project. Every commit is authored by Pyra Drake; the assistants
appear in the `Co-Authored-By` lines. To see the counts for yourself:

```bash
git shortlog -sne
```

```bash
git log --format="%(trailers:key=Co-Authored-By,valueonly)" | sort | uniq -c
```

## Testers and reporters

Everyone who tests a release or reports a problem is credited here and
in the document that records the finding, by the name they choose. No
one is listed yet apart from the maintainer. See
[Getting listed](#getting-listed).

## Community

- **The [LMAST/SFCC English Fan Discord](https://discord.gg/7DNrGye9TZ)**,
  the English-speaking community of *Let's Make a Soccer Team!* and the
  *Sakatsuku* (SFCC) series, which this mod is made for.

## Projects this one builds on

| Project | Used for |
|---|---|
| [LMAST-Reverse](https://github.com/NexxusDrakoMultimedia/LMAST-Reverse) | all of the mod's code: the switches, the editions, the patch maker and the widescreen patch. This repository pins one of its commits for each release |
| [LMAST-Realism](https://github.com/NexxusDrakoMultimedia/LMAST-Realism) | the crests, badges, match pictures and league logos that Full and Max carry on the disc |

## Third-party software and data

The release contains none of these projects' code. Each keeps its own
license; a license is named here only where the repository states it.

| Project | Used for |
|---|---|
| [Python](https://www.python.org/) | `tools/build_release.py`, standard library only |
| [Redump](https://redump.info/) | the disc fingerprints (disc [12334](https://redump.info/disc/12334/)) the build checks, and the image every patch is made against |
| [xdelta3](https://github.com/jmacd/xdelta) | the patch format (VCDIFF, RFC 3284). The build uses it, when installed, to check each patch the way players apply it. Players use a tool such as Delta Patcher or xdelta UI, which this project does not include |
| [PCSX2](https://pcsx2.net/) | running the game for the in-game tests, and the widescreen patch format and CRC naming |
| [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed) by Christian Robertson (Copyright 2011 Google Inc.; [Apache License 2.0](fonts/LICENSE-Apache-2.0.txt)) | the face drawn into the game's text in Full and Max and into the title banner. The copy is in [`fonts/`](fonts/); only drawn pictures go into a disc, never the font file |
| [0RWX](https://0rwx.com/) by Namtao Productions (CC0) | the scale of AI usage the README declares this project at |
| [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/) | the formats of the changelog and the version numbers |

## Getting listed

Contributions of any kind are welcome: test results, bug reports,
documentation, build changes or research. See
[`CONTRIBUTING.md`](CONTRIBUTING.md) for how to send one.

- **Code or docs:** add yourself to the right table above in your pull
  request, or ask to be added.
- **Tests or reports:** say how you would like to be credited (your
  name, a handle, or not at all) and you will be added here, and in the
  document that records the finding.
