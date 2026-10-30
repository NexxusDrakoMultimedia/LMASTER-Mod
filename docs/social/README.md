<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<!-- Copyright (C) 2026 Nexxus Drako Multimedia -->

# Social media posts

The opening posts of the mod's threads, kept here so they stay in step
with the README. For the maintainer; players want the
[README](../../README.md).

| File | Where | Markup |
|---|---|---|
| [`discord-op.md`](discord-op.md) | the mod's Discord channel or forum post, pinned | Discord Markdown, at most 2,000 characters |
| [`neoseeker-op.txt`](neoseeker-op.txt) | the first post of the mod's Neoseeker thread | Neoseeker's [nTags](https://forums.neoseeker.com/markup_help.php) |

Each file is pasted as it is, so neither carries a licence header; this
README's covers them (GPL-3.0-or-later).

## Keeping them current

Both link to the latest release and to `main`, so most releases change
nothing here. On each release:

- **Neoseeker:** update the "Current version" line, then edit the
  thread's first post.
- **Both:** if a release adds an edition or a headline feature, or
  changes what a player needs or how saves work, update the matching
  line, as in the README.

A release's own announcement is written fresh each time, from its
CHANGELOG section, and isn't kept here.

## Markup notes

- **Discord:** wrap links in `<…>` so they don't each make a preview
  card. `-#` is small text. A message holds 2,000 characters
  (`wc -m discord-op.md`).
- **Neoseeker:** links are `[link name=words]url[/link]`; lists are
  `[ul]` or `[ol]` with a `[li]` before each item. The `*` and `#` list
  shortcuts on the help page don't render in posts, and BBCode's
  `[url=…]` and `[list]` aren't nTags. Two apostrophes in a row (`''`)
  turn into italics. Use **Preview** before saving.
