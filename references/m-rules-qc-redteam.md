# M-rules: QC, red-team & the owner gate

Part of the GTA VI Shorts Editing Skill v1.2.0. Load when: Load at builder QC or the red-team gate.

M-numbers are stable and never renumbered. The full rule text lives here; SKILL.md carries only the gates summary and the reference index.

## Contents

- [M6](#m6)
- [M8](#m8)
- [M12](#m12)
- [M15](#m15)
- [M19](#m19)
- [M23](#m23)
- [M25](#m25)

## <a id="m6"></a>**M6 Frame-per-beat inspection.**

Frame-per-beat inspection of rendered frames; defects found, fixed, and re-verified before encode.

## <a id="m8"></a>**M8 Owner's watch/listen is FINAL.**

Owner's watch/listen stated as FINAL throughout; no listen claimed from this environment. No gate score substitutes for it.

## <a id="m12"></a>**M12 Every number is a tool measurement.**

Every number is a tool measurement on the delivered file (cut count is a counted list; STT diffs explained, not hidden).

## <a id="m15"></a>**M15 TECHNICAL PASS is not CREATIVE PASS.**

Every build report carries Technical status AND Creative status separately. "Premium" needs 85/100 plus no critical failure plus human watch/listen approval. Until the owner rules, the report says "Creative REVIEW PENDING", never self-certified premium. Relationship between the two bars (decided v1.1.0): the 85/100 "Premium" bar is the CREATIVE bar (M15); the at least 90/100 red-team gate is the RELEASE bar. The release bar is strictly higher. A video can be Premium at 85+ yet still be blocked from release until it clears 90/100 plus 48/60 plus zero criticals. Premium is necessary but not sufficient; the release gate governs shipping.

## <a id="m19"></a>**M19 FULL-SLICE CONTENT-SAFETY SAMPLING.**

Before any gate signs off content safety, sample EVERY backdrop slice across its full span: head, middle, AND tail at minimum, checking (a) no social-UI overlay, (b) no sexualized framing, (c) no torso-dominant close-up, (d) the ledger label matches the inspected frames, not the slice name. Stage-open-only sampling is insufficient by construction. A frame description written from a label instead of an inspected frame is a defect in the report, not just the video. A defect found only by red-team full-slice sampling is a late catch, not the plan.

## <a id="m23"></a>**M23 SHARED SAFETY BLOCKLIST ACROSS A MULTI-VIDEO RUN.**

Any slice or span cut for content-safety in ANY video of a run is banned in EVERY video of that run, immediately, by source timecode. The coordinator keeps one running blocklist and every builder checks triage against it before building. A triage label never overrides inspected frames: a slice described as an "object" close-up must still be viewed at full resolution across its full span (M19) before it counts clean.

## <a id="m25"></a>**M25 QC CLAIMS MUST MATCH THEIR OWN ARTIFACTS; RED-TEAM RE-MEASURES, NEVER TRUSTS.**

Every measurement claimed in a build report must be traceable to the artifact file it cites: the report names the file and the number comes from that file. A claim its own artifact contradicts (silencedetect "0 hits" when the file shows hits; STT "100%" from a garbled work file) FAILS the QC report itself, not just the measurement: the video is not cleared until an independent re-measure from the DELIVERED file confirms the numbers. Red-team re-runs silencedetect, loudnorm, STT, and frame checks from the delivered file as a matter of course; a builder's numbers are never taken on trust, however clean the scorecard looks. M12 governs that numbers are tool measurements; M25 governs that the claimed measurement actually exists in the cited artifact.
