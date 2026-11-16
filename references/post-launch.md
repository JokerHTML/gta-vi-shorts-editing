# Post-launch variant (air date on or after Nov 19, 2026)

GTA VI launches November 19, 2026 (PS5 + Xbox Series X/S, no PC announced). The
pre-launch countdown machinery retires on that date: after launch there is no
"[N] days to launch", no launch-date tag to target, and no countdown card to fill.
The retirement rule: **air date ≥ Nov 19, 2026 → use this variant, never the
countdown variant.**

## Replacement sixth beat

Pre-launch beat 6 was the countdown ("[N] days to launch."). Post-launch beat 6 is
**"what to do / what's next"**: one concrete next step for the viewer, ledger-sourced
(e.g. "Pre-loading is live on PlayStation and Xbox — check your store region for your
unlock time", or the topic's own next step). Same length as the countdown beat
(one short sentence), same position (last beat, last line of the description).

## Replacement card type

The countdown card is replaced by a **next-step card**: same countdown layout, new
content — headline is the next step in words ("CHECK YOUR STORE REGION"), qualifier
and source chip unchanged in form. The template's `countdown` card entry in
`src/data.ts` becomes the next-step card after launch; rename the entry in your own
copy and keep the M30 rule: the next step is re-derived from the ACTUAL air date,
never carried from the build date.

## Replacement tag set

Drop the launch-date tags (`GTA VI November 19`, `GTA VI launch`, `GTA VI countdown`).
Replace with post-launch tags drawn from the topic: `GTA VI launch day`, `GTA VI
gameplay`, `GTA VI first look`, plus the topic's own tags. Keep the count at 12 and
the verbatim brief order. Never ship a post-launch video with a pre-launch tag set:
the tags are the discoverability, and stale tags target a search that no longer exists.

## What stays the same

Everything else: the ledger, the banned list, M30 (relative dates re-derived at
scheduling — "today" now means launch day or later, check it), M31 (time + eligibility
in the lead claim), the pool gate, the render/grade/loudnorm pipeline, and the
red-team gate. The launch-week speed protocol (format menu: news recap / breakdown /
reaction-clip / countdown → post-launch: news recap / breakdown / reaction-clip /
what-to-do) still applies: ship fast, one variable at a time, retention read at 48h.
