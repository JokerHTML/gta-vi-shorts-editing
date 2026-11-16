# Evals

Three eval cases for this skill. These are documentation evals, not
executable tests: each gives a prompt, the expected output, and
specific observable assertions a reviewer checks by hand. Run them
when the skill changes, or when you want to check that an agent using
the skill actually follows it. A case passes only when EVERY
assertion holds.

## How to run

Give the agent the prompt exactly as written, with the skill loaded.
Then check the agent's output against the assertions. Do not grade on
style or polish: grade only on the assertions listed.

---

## Eval 1: Standard news Short (happy path)

Prompt:

> Plan a GTA VI news Short using the skill. Topic: Rockstar confirms
> GTA VI pre-load starts November 10 on PlayStation 5 and Xbox Series
> X and S. The game launches November 19. Air date is November 15.
> Write the fact ledger, the banned list, the paste-ready ChatGPT
> brief, and the pre-render plan. Do not build video or audio.

Expected output:

- A fact ledger with labelled rows (CONFIRMED for the launch date and
  platforms, REPORTED for anything sourced to an outlet), each row
  naming its source.
- A banned list that bans "pre-load unlocks the game early" and any
  PC date.
- A ChatGPT brief with the six beats (hook, what, plot, scale,
  caveat, countdown), numbers as words, 12 tags, and a thumbnail
  brief with base and backup frames.
- A pre-render plan with a beat map, a timeline draft, an asset list,
  and the validation sign-off.

Assertions (all must hold):

1. The ledger has a row for the November 10 pre-load date AND a row
   for the November 19 launch date, each with its own source.
2. The countdown in the brief reads "Four days to launch." (Nov 19
   minus Nov 15 is 4, M30).
3. The script beats contain no digits anywhere.
4. The banned list contains a ban on claiming pre-load unlocks the
   game early, with the replacement wording "pre-loaded files stay
   locked until your region's unlock time" or equivalent.
5. The pre-render plan's timeline draft shows need plus 10 percent
   slack (M20) and names the bed choice with licence and source URL,
   or records VO-only with the M4 condition.
6. The thumbnail brief names a base frame AND a backup frame, both
   official Rockstar frames, with the safe-margin note (130px sides,
   150px top, 200px bottom).

## Eval 2: Disputed fact (edge case: contradiction in sources)

Prompt:

> Plan a GTA VI news Short using the skill. Topic: a burger chain
> promotion with a disputed detail. Outlet A says the promotion runs
> in nine Florida locations; outlet B says eleven. Rockstar has posted
> nothing about it. Air date is November 15. Write the fact ledger,
> the banned list, and the paste-ready ChatGPT brief. Do not build
> video or audio.

Expected output:

- A ledger row for the location count labelled REPORTED - DISPUTED,
  naming both outlets and their numbers.
- A ledger row stating Rockstar has posted nothing, labelled
  CONFIRMED AS UNPOSTED or equivalent, checked at Rockstar's own
  channels.
- A banned list that bans naming either count as fact and bans saying
  Rockstar announced the promotion.
- A brief whose script says the count is disputed, or omits the count
  and says the locations are unconfirmed.

Assertions (all must hold):

1. The location-count row is labelled REPORTED - DISPUTED, not
   CONFIRMED and not REPORTED.
2. The script does NOT state "nine locations" or "eleven locations"
   as fact anywhere (script, card text, or thumbnail text).
3. The banned list bans "Rockstar announced the promotion" with the
   replacement "Rockstar has posted nothing about the promotion".
4. The brief's FACTS section carries the M32 line naming the seller or distributor page the
   negative claim was checked against (added to the fill-in template v1.2.0), not just the brand page. The ledger row carries the same check (M32 lives in the ledger); the brief line is what makes the eval assertable from the brief alone.
5. The script's caveat beat states the dispute plainly, in words the
   viewer can follow, without resolving it.

## Eval 3: Pool too small (edge case: STOP before VO)

Prompt:

> Plan a GTA VI news Short using the skill. Topic: a new GTA VI
> trailer frame story. The script is 104 spoken words. The verified
> clean pool is 900 frames (full-res checked). Gap pattern is
> 8/5/8/5/8/5 frames. Write the POOL-GATE-RECORD.md and say what
> happens next. Do not build video or audio.

Expected output:

- A POOL-GATE-RECORD.md showing the arithmetic: speech frames from
  the planning pace, gap frames, tail pad, need, ceil(10 percent) slack,
  need plus slack, verified pool, and a STOP verdict.
- The statement that no VO, cards, or mix are built.

Assertions (all must hold):

1. Speech frames are computed from the planning pace of 2.5
   words/sec: ceil(104 / 2.5 * 30) = 1248f. Any other pace figure is
   a fail (the pace is measured-from-trio, not a guess).
2. Need is 1248 + 39 + 2 = 1289f, slack is ceil(10% of need) = ceil(128.9) = 129f, need plus slack is
   1418f.
3. The verdict is STOP, because 900f is smaller than 1418f.
4. The output states explicitly that VO, cards, and mix do NOT start.
5. The output proposes a next step that is one of: narrow the topic
   to fit the pool, or find more verified clean frames. It does NOT
   propose building anyway, borrowing frames from another video's
   allocation, or counting contact-sheet tiles as clean.

## Measurement artefacts (v1.2.0)

`evals.json` records the suite (10 should-trigger + 10 should-not-trigger prompts, pass rate, last run, worked-case results — target 90%+), `grading.json` the /60 + /100 rubrics and trio scores, `timing.json` the render + script timings. Re-run the suite whenever the skill changes and record a without-skill baseline (same prompts, no skill loaded). See `references/analytics-iteration.md`.
