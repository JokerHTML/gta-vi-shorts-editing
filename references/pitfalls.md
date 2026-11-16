# Pitfalls (dated — what failed before, and how to avoid it)

## 2026-11-15

- **V2 shipped with the wrong colour tags** (yuvj420p / pc / bt470bg). Cause: the
  Remotion render outputs full-range despite `--pixel-format=yuv420p`, and the build
  trusted the render command instead of measuring the delivered file. Avoid: ffprobe
  the delivered file (M25/M36) before red-team, every time. Origin of M36.
- **V3 loudness took three passes** (single-pass −17.47, two-pass −16.05, retarget
  −15.21). Cause: the mono mix measured fine, but the stereo render added ~+3 dB and
  clipped at TP +0.18. Avoid: account for the mono-to-stereo shift in every loudnorm
  pass; measure the delivered file, never the mix.
- **V1's delivered file had sRGB transfer, not bt709**, though the build report claimed
  "bt709x4". Cause: the report was trusted over the file. Avoid: M25 — the claim must
  exist in the cited artifact. Fixed by a lossless remux, framemd5-verified identical.
- **V2's uniform 0.35s gaps** earned MINOR-1 for digital silence. Cause: the A/B stem
  recipe used uniform gaps; uniform gaps are retired. Avoid: varied gaps (M3) + a bed
  mix by default (M4).
- **V1's card dropped "ABOUT"** ("THIRTY-SECOND TEASER" reads exact). Cause: the brief
  itself wrote it that way. Avoid: enforce M34 at brief-spec stage, not only at
  storyboard.
- **The "leak" ban was evadable**: a script containing "leaked material" passed a ban
  on "leak" in the old validator (word-boundary grep). Fixed v1.2.0: stem-aware matching.

## 2026-11-16

- **Raw render measured already TV-range** (only the transfer was wrong, sRGB). The
  "Remotion always outputs full-range" premise is version-dependent. Avoid: the
  signalstats pre-fix gate in `post-render-fix.sh` (v1.2.0) — convert only when the
  values actually span full-range.
- **Live GitHub repo still v1.0.0** while the local skill is v1.2.0. Avoid: never link
  the repo as the current version until a push is confirmed; see `CHANGELOG.md`
  (live vs local).
- **SEO apply files went stale** (`seo-optimization-2026-11-15/README-OPTIMIZED.md` and
  `apply/SKILL.md`): applying them now would regress the README. Both are marked
  STALE-DO-NOT-APPLY. Avoid: check the apply folder's date against the live skill
  before applying anything.

## Standing

- **A timed-out or locked publish can land minutes later.** Never retry blind: check
  the feed first, warn of the duplicate risk, and never delete a duplicate without the
  owner's word.
- **A connector write that "failed" can execute later.** Re-verify via a live read
  before retrying any publish.
- **ChatGPT's word count is wrong on every trio script's first return.** Hand-count,
  always.
