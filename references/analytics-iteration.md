# Analytics & iteration (Step 15)

Ship measurement, not just evals. After every video, record the result and read the
retention graph at 48 hours. This page is the loop; the results log is the record.

## The 48-hour retention read

Read the retention graph (YouTube Studio → Content → the Short → Analytics →
Retention) at 48h after publish, and diagnose by shape:

| Shape | Diagnosis | Next change (one variable) |
|---|---|---|
| Early cliff (big drop in the first 3–5s) | Hook problem | Rewrite the hook (new hook shortlist, new human pick); keep everything else |
| Slow slide (steady decline) | Pacing problem | Tighten visual velocity (more events per 2–3s, earlier first cut) |
| Stair-step drop (one sharp step) | One bad second | Find the exact second; fix that beat only (new shot, new card state, cut) |
| Rise at the end | Rewatch — the loop worked | Keep the loop design; reuse the re-hook shape on the next video |
| Flat then cliff at a card | Card problem | Re-stage the card (M28 read on frame; check the qualifier and the image) |

## The iteration ritual

1. One variable per upload. Change the hook OR the pacing OR one beat — never two.
2. Keep a 10-Short baseline before judging any change. Three videos are not a sample.
3. Never delete-and-reupload a flop. The flop's data is the lesson; a re-upload
   resets the data and teaches nothing.
4. Record the diagnosis and the one change in the results log row, beside the numbers.
5. Re-check the proof counts before any new publication that cites them (refresh rule).

## Evals measurement (how the skill itself is graded)

`evals/evals.json` records the eval suite (pass/fail per check, last run date);
`evals/grading.json` records the scoring rubric; `evals/timing.json` records
render timings. The suite includes 10 should-trigger prompts (the skill MUST engage:
GTA VI news Shorts tasks) and 10 should-not-trigger prompts (the skill MUST NOT
engage: non-GTA editing, leak-only topics, client-job paperwork, policy questions).
Target: 90%+ pass. `evals/README.md` carries the three worked eval cases. Re-run the
suite whenever the skill changes, and record a without-skill baseline (same prompts,
no skill loaded) so the improvement is measured, not asserted.
