# Appendix: Templates (Steps 0, 3)

Short markdown-table schemas for the three records every build
writes. Copy the tables into your run folder and fill them in. One
row per fact, per ban, per pool slice: no prose summaries in place of
rows. A record with no rows is not a record.

## Fact ledger (Step 0)

One row per fact. The label is one of CONFIRMED, REPORTED, REACTION,
CONFIRMED AS UNANNOUNCED, or REPORTED - DISPUTED. The verification
note names the sources actually read, not the topic in general. A
negative claim ("no X announced", "no price published") names the
seller or distributor page it was checked against, not just the brand
page (M32).

| # | Fact (in words, never digits) | Source (outlet, date) | Label | Verification note |
|---|---|---|---|---|
| F1 | GTA VI launches Thursday, November nineteenth, on PlayStation Five and Xbox Series X and S. | Rockstar Newswire, Nov 6, 2025 | CONFIRMED | Read on the Newswire page; launch date and platforms stated directly. |
| F2 | [Your fact, written as it will be spoken.] | [Outlet, date] | [Label] | [What you opened and read.] |

Worked example: V1's complete ledger (12 rows, F1-F12) is in
`examples/v1-macca-friends.md` under "## Fact ledger (complete)". Note F6
there: the same fact reported two ways by two outlets is one row
labelled REPORTED - DISPUTED, and the script never names the disputed
value.

## Banned list (Step 0)

One row per ban. Each ban states what is forbidden AND what the
script says instead. A ban with no replacement wording is unfinished:
the writer will fill the gap by inventing something.

| # | Banned in this video | Say instead |
|---|---|---|
| B1 | Naming the crab landlord definitively (outlets disagree: Pinche vs Pinchy; Rockstar names no one). | "his crab landlord" only. |
| B2 | Claiming full episodes are watchable, or any episode count / length. | "Nobody outside Rockstar has said how many episodes, how long they run, or whether full episodes are watchable." |
| B3 | The word "leak" or any leak handle. | Nothing: the story is an official teaser, so the word never appears. |

Worked example: V1's complete banned list (10 rows, B1-B10) is in
`examples/v1-macca-friends.md` under "## Banned list (complete)",
including B9/B10, the two relative-date bans that M30 enforces at
scheduling.

## POOL-GATE-RECORD.md (Step 3, M20)

Record the arithmetic, not just the verdict. Count ONLY
full-res-verified clean frames: head, middle, tail, AND fade
boundaries checked at full resolution. A contact-sheet tile verdict
never counts a span clean.

| Item | Value |
|---|---|
| Script spoken words | [N] |
| Planning pace (measured-from-trio, see SKILL.md M20) | 2.5 words/sec (slowest of V1 2.94, V2 2.50, V3 2.66) |
| Speech frames needed | ceil(words / 2.5 * 30) = [N]f |
| Gap frames (varied gaps, M3) | [N]f |
| Tail pad | 2f |
| Need (speech + gaps + tail) | [N]f |
| Slack (ceil(10 percent of need) — round UP) | [N]f |
| Need + slack | [N]f |
| Verified clean pool (full-res only) | [N]f |
| Verdict | PASS (pool >= need + slack) / STOP (pool < need + slack: no VO, no cards, no mix; report) |

Then list every counted slice, one row per slice:

| Slice | Source timecode / frame | Frames counted | Full-res check (head/mid/tail/fades) | Clean? |
|---|---|---|---|---|
| [e.g. Grassrivers_03 hero still] | [frame name] | [N]f | head/mid/tail/fades viewed | Yes |
| [e.g. T2 35.2-38.0 motion] | [span] | [N]f | head/mid/tail viewed | Yes |

Across a multi-video run, keep a running pool ledger: every build
deducts its used slices from the remaining clean total, so exhaustion
is forecast, not discovered at build 7. A slice cut for content
safety in ANY video of the run is banned in EVERY video of the run,
by source timecode (M23): check triage against the run's shared
blocklist before counting anything.

## trailer-windows.md (Step 0)

One row per claimed motion span. No two videos use the same span.

| Span | Source + timecode | Claimed by (video) | Full-res 1fps survey | Clean? |
|---|---|---|---|---|
| [e.g. T2 35.2-38.0 highway] | [Trailer 2, 35.2-38.0] | [video slug] | head/mid/tail viewed at 1fps | Yes |
| [e.g. LT 55.2-57.0 beach] | [Launch Trailer, 55.2-57.0] | [video slug] | head/mid/tail viewed at 1fps | Yes (ends 57.0: frame 57.1 is BLOCKED) |

## RUN-ALLOCATION.md (Step 0, multi-video runs)

| Frame / span | Assigned to (video) | Role (hero / beat / backup) | Status |
|---|---|---|---|
| [e.g. Grassrivers_03] | [video slug] | hero | used |
| [e.g. VC_11] | [video slug] | hero backup | contingency only — cut only if the hero fails a later gate, never also a beat |

A frame belongs to exactly ONE video as hero-or-beat. Within one video, the same
still reused with a different crop window is allowed only with a different window AND
a named reason in the shot plan; the same window twice is a double-assignment defect.

## Build report (Steps 9, 12)

One file per video, `work/<slug>/reports/build-report.md`. It carries BOTH statuses,
separately (M15): **Technical status** (PASS / FAIL, with the measured numbers and the
artifact file each number came from) and **Creative status** (REVIEW PENDING until the
owner rules; never self-certified premium — "Premium" needs 85/100 plus no critical
failure plus human watch/listen approval). Sections: bed choice (licence + source URL,
M35); active-area measurements per source (M29); pool-gate result; render command;
fix/grade/loudnorm results on the delivered file; QC measurements (M25: every number
names its artifact file); deviations with their consequences.

## QC report (Step 12, builder QC)

`work/<slug>/reports/qc-report.md`. One row per check, each naming the artifact file
and the measured value: duration; resolution/fps; loudness (LUFS + TP, delivered file);
silencedetect hits; cropdetect per motion span (head/mid/tail each); STT match (stems in
order, verbatim modulo expected normalizations); card frames read (M28); thumbnail
full-size views (builder / red-team / coordinator). A claim its own artifact
contradicts FAILS the QC report itself (M25).

## vo_check.json / word_timings.json (Step 5)

`vo_check.json` keys: `voice`, `speed`, `model` (`small`), `stems` (list of
`{stem, file, words, heard_words, match}`), `verdict`. `word_timings.json` keys:
`words` (list of `{word, start, end}` in seconds, from faster-whisper word
timestamps). Caption words are script words only; timing comes from these timestamps.

## timeline.json (Step 6)

Keys: `fps` (30), `stems` (list of `{stem, start_frame, end_frame}`),
`gaps_frames` (list, varied per M3), `total_frames` (speech + gaps + 2f tail pad),
`duration_seconds`.
