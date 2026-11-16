# Pre-Render Plan (G10: plan, validate, execute)

Write this file AFTER the script is honest-checked (Step 2) and the
pool gate has passed (Step 3), and BEFORE any VO synthesis (Step 4).
Nothing renders until this plan is validated: a bad plan found here
costs a rewrite of one file; the same bad plan found after render
costs a rebuild of the whole video.

## The plan file

Save it as `work/pre-render-plan.md` in the run folder. One plan per
video. It has four parts: the beat map, the timeline draft, the asset
list, and the validation sign-off.

### 1. Beat map

One row per VO beat. The cut frame is named for every information
beat (M22), the card state for every card beat, and the hook score for
the hook beat (see SKILL.md, hook score, PROVISIONAL).

| Beat | VO line (first words) | Cut frame | Shot / card | What changes on screen |
|---|---|---|---|---|
| 1 (hook) | [First words] | f0 | [Hero still / motion] | [What the viewer sees] |
| 2 | [First words] | [frame] | [Shot / card] | [What changes] |
| 3 | [First words] | [frame] | [Shot / card] | [What changes] |

### 2. Timeline draft

| Item | Value |
|---|---|
| Script spoken words | [N] |
| Planned speech seconds (words / 2.5) | [N]s (planning pace, M20) |
| Gap pattern (varied, M3) | [e.g. 8/5/8/5/8/5 frames] |
| Total frames (speech + gaps + 2f tail) | [N]f = [N]s |
| Duration check | 30-59s: PASS / FAIL |
| Segments | [N] (about 1 shot per sentence, M22) |
| Card windows (frames) | [e.g. f157-350 hook card; f503-603 locations card] |
| Caption phrases | [N] phrases, 2-4 words each, none overlapping a card window |
| Bed | [Bed choice + licence + source URL, or VO-only with the M4 condition] |

### 3. Asset list

| Asset | Source | Verified? |
|---|---|---|
| [Still 1] | [Official set + frame] | Full-res M19 screen: yes |
| [Motion 1] | [Trailer + span, claimed in trailer-windows.md] | Active-area measured (M29): yes |
| [Logo] | [Your authentic logo file] | Hash verified (sha256 18ad6092...): yes |
| [VO] | Kokoro am_adam @ 1.1 (planned, not yet synthesised) | n/a until Step 4 |

### 4. Validation sign-off

Validate the plan against the checklist below BEFORE synthesising VO.
Any NO is a fix to the plan, not a note to carry forward.

- [ ] Every beat has a cut frame named (M22).
- [ ] Every card names its own layout, palette, and focal element, and
  no two cards share a layout in this video.
- [ ] Every figure card carries its qualifier word on the card, with
  the figure, at headline size (M34).
- [ ] Every card line traces to a ledger row (M17), including EACH SIDE
  of any contrast card.
- [ ] Every card is read on its frame: the image shows what the card
  says, does not contradict it, and the card covers no text already in
  the frame (M28).
- [ ] The countdown is derived from the ACTUAL air date (M30), and the
  time-of-day plus eligibility check has been run (M31).
- [ ] No caption phrase overlaps a card window.
- [ ] No caption phrase is a lone "the", "a", or "no".
- [ ] The pool gate passed with ceil(10 percent) slack (M20), and the used
  slices are deducted from the run's pool ledger.
- [ ] The bed choice is recorded with licence and source URL (M35),
  or VO-only is recorded with the M4 silencedetect condition.
- [ ] The hook scores 8 or above (PROVISIONAL hook score, see SKILL.md). The 4-second check is measured: the hook line's Kokoro stem duration at speed 1.1 must be under 4.0s (proxy: ≤10 words at the 2.5 words/sec planning pace). The score is uncalibrated until retention data exists.

## What happens next

If the plan validates, build in order: VO (Step 4), VO check (Step 5),
VO concat (Step 6), stills and motion (Step 7), cards and captions
(Step 8), mix (Step 9), render (Step 10). If any step's measured output
differs from this plan by more than the slack (for example VO runs
longer than planned speech seconds), STOP and re-validate the plan
with the measured numbers before continuing: never bend the render to
fit a stale plan. (M7: the plan's beat-length check is a planning estimate
at plan time — no VO exists yet — and the binding check runs AFTER VO
synthesis, against measured stem durations.)
