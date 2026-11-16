# CHANGELOG.md — GTA VI Shorts Editing Skill

## 1.2.0 — 2026-11-16 (local only — NOT yet pushed to GitHub, NOT yet on Gumroad)

**Live vs local:** the live GitHub repo (`JokerHTML/gta-vi-shorts-editing`) still serves
v1.0.0 and the live Gumroad page still carries the pre-1.2.0 listing. Both updates need
Saad's word. Do not link the repo as v1.2.0 until a push is confirmed.

- Token move: M-rule detail moved to `references/m-rules-*.md` (6 grouped files,
  M-numbers stable, no renumbering); SKILL.md slimmed from 426 lines to ~231 lines.
- Canonical pipeline: fix-then-grade, one loudnorm pass; `post-render-fix.sh` gains a
  signalstats pre-fix range gate; `grade-pipeline.md` takes the fixed file (no range
  conversion, no loudnorm); render command gains `--crf=12`; "lossless master" renamed
  high-quality master (crf 12 is lossy).
- /100 rubric published (`references/redteam-rubric.md` + summary in SKILL.md), derived
  from the trio's actual deductions.
- Complete V1 fact ledger (12 rows) + banned list (10 rows) shipped in
  `examples/v1-macca-friends.md`.
- Install fixed: `INSTALL.md` with literal commands (ffmpeg 8 static build, Node 24 via
  NodeSource/nvm, Kokoro model download URLs, literal `ln -s` espeak-ng form, supported
  OS stated). `setup-check.sh` now checks versions, Remotion, yt-dlp, espeak-ng path,
  disk space. `validate-build.py` now stem-aware banned matching, fails on zero
  phrases/cards, and states its coverage.
- Step 11 rewritten (two-pass disambiguated; V3's exact audio-only retarget documented).
  V2/V3 grade contradiction resolved: V2 shipped ungraded (recorded as a deviation).
- M13 given GTA diagram beats; M1 restated for buyers; M20 slack is ceil(10%);
  M9/M7/M26 procedures added; M26 15s window procedure with worked example.
- Caption route declared (Remotion canonical; ASS fallback with burn-in order + Studio
  caption-upload step). Post-launch variant (`references/post-launch.md`).
- New research lessons applied: hook shortlist + human pick; karaoke captions;
  visual-velocity check; mix ladder + sidechain ducking; loop/re-hook; first-frame-as-
  thumbnail; licence-safe music ladder; pause discipline; originality + 7s rules;
  analytics-iteration page; delivery-spec + ingest checklist; picture lock + version
  naming; `voice.md` (channel defaults); day-plan; `pitfalls.md`; named gates
  (source-deck → timestamp → layout → technical → human/vision); `when_not_to_use`
  routing; demo/preview-first render; evals measurement artefacts
  (`evals/evals.json`, `grading.json`, `timing.json`, should-trigger / should-not-
  trigger prompts); worked-example number fixes; safe-zone guide + cover regenerated;
  template fixes (Captions repeat-keyword, Shot motion parameter, CardFigure text-fit,
  distinct placeholder accents, thumbnail logo margin, Inter Bold faces).
- Pro Pack: version 1.2.0 everywhere (template `package.json`, ZIP filename);
  `contents.md` states the versioning rule, the update mechanism (Gumroad email to
  buyers + versioned ZIP re-upload), the solo-operator scope, and the one-sentence
  commercial/team-use licence. Listing differentiation corrected (AI Leverage GTA 6
  Shorts Kit named; moat is accuracy + rules + proof + release bar).
- "Launch-week updates included" now has a mechanism (see `contents.md`); if the
  mechanism is not operated, drop the line.
- Grade A is no longer cited as a quality signal (security grade only).

## 1.1.0 — 2026-11-16

Polish pass: verbatim V1 ChatGPT brief + fill-in template, install section, sourcing
guide, pre-render plan, ledger/banned/pool schemas, troubleshooting + FAQ, setup-check
and validate-build scripts, three eval cases, workflow checklist, success criteria,
hook score (PROVISIONAL), results log (PROVISIONAL), word-count convention, M20 pace
and slack, safe-zone margins, canonical caption size, refresh rule. No M-rule dropped
or renumbered. **Not pushed to GitHub** (live repo still v1.0.0 at the 1.2.0 audit).

## 1.0.0 — 2026-11-15

First public version. M1–M36, full workflow, verified commands, upload checklist,
thumbnail method, red-team rubric, three worked examples. **Live on GitHub.**
