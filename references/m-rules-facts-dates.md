# M-rules: Facts, ledger, dates & pool gate

Part of the GTA VI Shorts Editing Skill v1.2.0. Load when: Load when researching a topic, building the ledger, or checking dates at scheduling.

M-numbers are stable and never renumbered. The full rule text lives here; SKILL.md carries only the gates summary and the reference index.

## Contents

- [M1](#m1)
- [M20](#m20)
- [M30](#m30)
- [M31](#m31)
- [M32](#m32)

## <a id="m1"></a>**M1 Playbooks read first.**

For buyers: read SKILL.md plus every reference file the workflow checklist loads for your step, before planning. The internal playbooks named in the original rule (concept report, OS, SOP, mistakes record) are not shipped; the shipped references are the buyer-facing digest of them. Original wording (internal): playbooks read first (concept report, ledger, OS, SOP, mistakes record), before planning.

## <a id="m20"></a>**M20 POOL-ARITHMETIC GATE BEFORE VO, COUNTED IN FULL-RES FRAMES ONLY.**

Before any VO synthesis, estimate needed frames from the script (word count times measured pace plus gaps and holds), triage the backdrop pool, and count ONLY full-res-verified clean frames: head, middle, tail, AND fade boundaries checked at full resolution; a contact-sheet tile verdict never counts a span clean. If the verified pool is smaller than need plus slack, STOP before VO, cards, and mix and report: never build VO, cards, and mix on an unproven pool. Across a multi-video run, keep a running pool ledger: every build deducts its used slices from the remaining clean total, so exhaustion is forecast, not discovered at build 7. Pace and slack (measured from the trio, see Step 3): planning pace 2.5 words/sec, need = ceil(spoken words / 2.5 * 30) + gap frames + 2f tail, slack = ceil(10 percent of need) — round UP to the next whole frame. Example: need 1289f, slack = ceil(128.9) = 129f, need + slack = 1418f. A hand-computed 128.9 is not a verdict; 1418f is.

## <a id="m30"></a>**M30 RELATIVE DATES RE-DERIVED AT SCHEDULING, NEVER CARRIED FROM THE BUILD DATE.**

At scheduling time, and again at any re-schedule, every relative-date word in the script, on every card, in the SEO, and on the thumbnail is re-derived from the ACTUAL air date (countdown = launch date minus air date; "today/tomorrow/begins today" checked against the air date, not the build date). A countdown or relative date written for the build date is STALE the moment the air date moves, and no gate before scheduling reads it. The check is a named step at scheduling (parent or coordinator, grep plus read-back on the delivered files), and a mismatch is a fix1 rebuild (VO re-record plus card re-render), never a silent ship and never a parent rewrite of a ChatGPT line: the corrected line comes back through ChatGPT verbatim. Internal docs carry the same rule: a tracker line quoting a countdown names its air date beside it, so a later reader never mistakes a build-date countdown for a live one.

## <a id="m31"></a>**M31 LEAD CLAIM CARRIES TIME + ELIGIBILITY; A SUB-LINE NEVER CURES A HEADLINE.**

The title, the hook card, and the VO opening line must each carry the time AND the eligibility of the claim they make: when something opens, and who it is open to, in the claim itself, not in a sub-line, not later in the video. A qualifier that lives only as small type under a giant headline, or that arrives on screen 20+ seconds in, does NOT cure a headline that implies the opposite. At storyboard, the lead claim is read as a viewer at air time would read it: what does this title or hook say is true RIGHT NOW, for ME? If the answer is wrong at air time (sale opens 7 hours later; winners only), the claim is rewritten, via ChatGPT, never patched with a sub-line. The check is run at storyboard AND at scheduling (M30's re-derivation step, extended: time-of-day plus eligibility, not just dates). M30 covers relative DATES; M31 covers time-of-day implication and eligibility, which M30 explicitly does not.

## <a id="m32"></a>**M32 VERIFY A NEGATIVE CLAIM AT THE PLACE THE THING WOULD BE PUBLISHED OR SOLD, NOT ONLY AT THE BRAND'S OWN PAGES.**

A claim of the form "no X published / no price / not announced / no set times" must be checked at EVERY place X could appear, above all the seller's or distributor's page, where the thing is actually sold, never only at the brand's own pages. The brand's page is the wrong place to verify a price: the price lives on the seller. The check is a named step at storyboard (the ledger row for a negative claim names the seller or distributor source it was checked against, not just the brand source) AND at audit (the auditor re-checks the seller page independently, with fresh eyes and fresh sources). A negative claim with no seller-page check is UNVERIFIED, not true.
