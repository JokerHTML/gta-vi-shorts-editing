# GTA VI Shorts Editing

Build premium, zero-fake English GTA VI news Shorts with a proven, checkable method: fact ledger, ChatGPT script, Kokoro voiceover, exact subtitles, official stills and trailer motion, designed fact cards, loudness and colour gates, and an independent red-team gate before upload.

## Install

```bash
npx skills add JokerHTML/gta-vi-shorts-editing
```

Manual copy fallback: copy this folder into `.claude/skills/` in your project, or into `~/.claude/skills/` to use it in every project.

Note: the GitHub repo must be named `gta-vi-shorts-editing` so the skill name matches the directory, as the Agent Skills frontmatter rule requires.

## Usage

Invoke this skill when you are planning, scripting, editing, checking, or uploading a GTA VI news Short.

Quickstart:

1. Research the topic and write a fact ledger with a banned list.
2. Get the script, SEO, and thumbnail brief from ChatGPT, then hand-count the script to 90-105 words.
3. Run the M20 pool gate before any voiceover work.
4. Synthesise Kokoro VO, check it with faster-whisper, cut stills and motion from the measured active picture, and build the mix.
5. Render in Remotion, apply the grade plus the M36 colour fix plus loudnorm, run builder QC, and pass the red-team gate before scheduling.

## Proof

Three Shorts were built with this method on November 15, 2026, on the Joker Gaming channel, and all three were scheduled the same day. No views, earnings, or subscriber counts are claimed here, because none were verified for this skill.

- GTA VI Built a Whole Cartoon Inside the Game - https://youtube.com/shorts/OC5KczRGYSQ - 40.00s - 96/100 + 60/60 PASS
- New Zealand Plays GTA VI First. Here's Your Unlock Time - https://youtube.com/shorts/aF6RgIg_mHI - 45.9s - 90/100 + 53/60 PRE-FIX verdict, a FAIL (MAJOR-1 colour). The shipped file is the MAJOR-fixed file, technically re-verified, expected approx 94/100, not a measured re-score
- Burger Shot Is Real Now. You Can Eat It in Florida - https://youtube.com/shorts/74I0MXC-aIQ - 40.8s - 97/100 + 57/60 PASS, per RUN-NOTES.md only; no standalone red-team report file exists for this video

Full worked examples with scripts, SEO, shot plans, and scores are in `examples/`.

## Free vs Pro

| Free (this repo) | Pro pack ($49 one-time, Gumroad) |
| Complete SKILL.md: all 36 rules, full workflow, verified commands, upload checklist, thumbnail method, red-team rubric | Remotion project template with the colour-safe pipeline (M36 fix script included) |
| 3 worked examples with full scripts, SEO, shot plans, scores | Colour LUT (.cube) + grade pipeline for the locked v3 recipe |
| Tools table with exact versions + gotchas | Thumbnail prompt pack (7 adapted prompts + layout templates + safe-zone guide) |
| Rockstar IP + honesty rules | Subtitle style presets (ASS files, both documented caption styles) |
| | Full M1-M36 + advanced checklists (printable) |
| | 3 worked-example project breakdowns with frame-accurate timelines |
| | Launch-week updates included |

## Repo layout

```text
gta-vi-shorts-editing/
  SKILL.md            The skill: workflow, all 36 rules, commands, rubric, thumbnail method, tools
  README.md           This file
  LICENSE             MIT licence
  examples/
    v1-macca-friends.md
    v2-unlock-times.md
    v3-burger-shot.md
```

## License

MIT. See `LICENSE`. Copyright 2026 Muhammad Saad Ranjha.

## Disclaimer

This skill is unofficial and independent. It is not affiliated with, endorsed by, or sponsored by Rockstar Games or Take-Two Interactive. It contains techniques, commands, and checklists only. It contains no Rockstar footage, trailer files, logo files, game music, or leaked material. Monetised GTA gameplay videos are common in practice, but that practice is tolerated, not licensed, and Take-Two can request removal at any time.
