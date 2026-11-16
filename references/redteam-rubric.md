# Red-team rubric (full)

Part of the GTA VI Shorts Editing Skill v1.2.0. SKILL.md carries the thresholds; this file carries the full area tables and methods.

### The 60-point rubric

| Area (max) | What it scores |
|---|---|
| Facts (10) | Ledger trace; banned list clean; qualifiers; dates exact |
| VO (10) | All script words verified in order by STT; bypasses proven |
| Captions (8) | Spelling, timing, no card overlap, phrase style, no lone function words |
| Cards (8) | Ledger-sourced; no black-opening defect; qualifiers at headline size |
| Visuals (10) | Allocated frames only; motion clean; bars checked per span; M24 pacing |
| Thumbnail (7) | Real logo verified; hook verbatim; safe margins; one focal image |
| Technical (7) | Loudness in band; colour tags correct; hashes match; no silent tail |
| **Total (60)** | **Pass at 48 or above, with zero criticals and no unresolved MAJOR** |

### The 100-point rubric (published v1.2.0)

The /100 quality score is a whole-number judgement by the independent reviewer, scored against this breakdown — derived from the trio's actual deductions, so a buyer can reproduce it. Minors dock from their area on BOTH scores only when the minor class hits that area; wording-precision minors (M34 qualifier drops, M22 static-tail) dock /100 only, which is why V1 kept 60/60 while losing 4 points on /100.

| Area (max) | What it scores |
|---|---|
| Facts & honesty (25) | Ledger trace, banned list, qualifiers, dates, M30–M32 |
| VO & script (15) | M18/M26 pattern, VO fidelity, bypasses proven |
| Captions (10) | Spelling, timing, overlap, phrase style |
| Cards (15) | Ledger-sourced, qualifier at headline size, readable on frame |
| Visuals & pacing (15) | Allocation, motion, bars, M22/M24 pacing, first frame complete |
| Thumbnail (10) | Real logo, hook verbatim, safe margins, focal image |
| Technical (10) | Loudness, colour tags, duration, format |
| **Total (100)** | **Pass at 90 or above, with zero criticals and no unresolved MAJOR** |

Severity vocabulary: **CRITICAL** is release-blocking, zero allowed. **MAJOR** must be fixed before release even if numeric bars are met. **MINOR** is docked points, no rebuild required, still recorded with evidence and frame numbers. **Observation** is noted with no deduction. V1's 3 minors mapped: hero-backup spent as a beat −2 (Visuals); M34 "ABOUT" dropped −1 (Cards, /100 only); M22 stem 6 no visual change −1 (Visuals, /100 only). V3's 3 minors: card fade-in 0.87s (Cards, /100 only, not fixed); Y-clamp ringing 0.65% (Technical, both scores); stale vo_check.json (VO, fixed before ship).

Red-team methods: ffprobe plus sha256 on delivered files; ffmpeg loudnorm plus silencedetect plus blackdetect plus RMS profiles; faster-whisper `small` STT with word timestamps on audio from the delivered MP4, plus `base` and `tiny` cross-checks (control synthesis decides disagreements); fresh Kokoro am_adam at 1.1 control syntheses plus sample-identity comparison; frame grabs viewed full-size (all segments, all cards first/mid/last, motion head/mid/tail, thumbnail) plus luma measurements of card fade-ins; grep checks for banned words and digits; clip-list cross-check for double-assignment; logo hash verification; SEO verbatim diff (title, description, tags).

