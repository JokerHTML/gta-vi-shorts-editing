# M-rules: Visuals, cards & thumbnails

Part of the GTA VI Shorts Editing Skill v1.2.0. Load when: Load at storyboard, card design, thumbnail build, or frame inspection.

M-numbers are stable and never renumbered. The full rule text lives here; SKILL.md carries only the gates summary and the reference index.

## Contents

- [M2](#m2)
- [M13](#m13)
- [M14](#m14)
- [M16](#m16)
- [M17](#m17)
- [M22](#m22)
- [M24](#m24)
- [M27](#m27)
- [M28](#m28)
- [M33](#m33)
- [M34](#m34)

## <a id="m2"></a>**M2 Creative bar judged, not just technical.**

Creative bar judged, not just technical (hook, premium graphics, evidence chips, diagram).

## <a id="m13"></a>**M13 SHOW-TEST.**

Every diagram or illustration beat must show the real object AND the action AND a visible consequence in one glance (for example an unlock-time diagram showing a world map plus a midnight line sweeping across time zones plus the New Zealand label flipping LOCKED to PLAYABLE; or a map-scale diagram showing Vice City plus the Leonida state outline plus a scale bar that grows as the VO names the comparison). If a beat only labels the thing, draws its shape, or loops a decorative motion with no object and no consequence, it FAILS: redraw it, do not ship it. Applied at storyboard stage and re-checked on inspected frames. Note: M13 governs diagram beats only. It does not govern the fact-card strip (Step 8): the Nov 15 briefs mislabelled the card strip "M13", and that label is retired.

GTA VI diagram beats (proven pattern, from the trio's card/map work): an unlock-time zone diagram (V2's subject: midnight sweeping time zone to time zone, New Zealand first, Mexico last); a map-scale diagram (Vice City inside Leonida, scale bar anchored to a ledger row). A diagram that only labels the map, draws its shape, or loops a decorative pan with no object and no consequence FAILS: redraw it.

## <a id="m14"></a>**M14 NO FORCED CUT-COUNT TARGET.**

Never force a visual change every 2 seconds. A beat holds as long as the information needs; a still can hold with readable evidence plus a purposeful reveal. Cut on information change, not on a timer.

## <a id="m16"></a>**M16 NO EMPTY BEAT OPENINGS.**

Every beat's first frame must already be visually complete: focal object plus headline or chip present at the beat's frame 1. Nothing the viewer needs may arrive seconds later as a pop into an empty zone, and no beat may open header-only on a near-black field for more than about 1s. If a beat's opening frame looks unfinished or dead, re-stage the beat: move the pop earlier, fill the zone, lighten the field. Do not ship it on a docked point. Checked at storyboard stage and re-checked on inspected first-frames.

## <a id="m17"></a>**M17 EVERY VIEWER-FACING WORD NEEDS ITS OWN LEDGER ROW.**

No card, footer, chip, panel, or caption wording may be written from a paraphrase of a ledger row about something else, or from no row at all. A row saying "X is separate from Y" NEVER licenses a label for Y. EACH SIDE of a contrast card needs its own row. Any descriptor (nationality, genre, identity, provenance) with no row is either sourced as a new row or cut back to the sourced wording. Checked at storyboard stage AND by grepping render text for unledgered adjectives before red-team; red-team catching it is late, not the plan.

## <a id="m22"></a>**M22 CUT ON EVERY INFORMATION BEAT, NEVER ONE-SPEED SCROLL.**

Every VO information change gets a hard cut (or a distinct motion change) at that beat: a new shot, a new camera move, or a new card state, timed to the spoken word. A continuous scroll, drift, or single-speed hold across two information changes FAILS storyboard, whatever the scorecard says, because it is audio laid over visuals, not an edit. Checked at storyboard stage (beat map must name the cut frame for every information beat) and re-checked on the rendered file (frame-diff or shot list must show a change at each beat).

## <a id="m24"></a>**M24 SLOW BACKGROUND CLIPS: NEVER FAST, NEVER RAPID-FIRE CHANGES.**

No video's background clips may move too fast or change too quickly: rapid background movement and quick-fire clip changes hurt the eyes and break natural connection with the scene. Background movement stays slow; each clip holds long enough for the viewer to register what it shows and connect with it naturally. Cuts still land on information beats (M22), but the movement INSIDE a span is slow, and a span never flashes by before the eye settles. The test at storyboard and on the rendered file: can the viewer rest their eyes on the background and follow it, or does it strain? If it strains, it is too fast: slow it down, do not ship it on a docked point. Applies to every video from Nov 6 onward, Joker Gaming and NeedCraft alike, and the red-team scores pacing against it.

## <a id="m27"></a>**M27 THUMBNAIL TEXT SAFE MARGINS: NO TEXT TOUCHING, CROSSING, OR RUNNING OFF ANY EDGE.**

Every hook-cover thumbnail's text must sit well INSIDE the frame with clear safe margins on ALL four sides. Text touching, crossing, or running off any edge, including text that only looks fine in a small preview, is a DEFECT and the thumbnail is rebuilt, never shipped on a docked point. The check is done by VIEWING the actual thumbnail file at full size (1080x1920) before delivery, not from a contact sheet or a small preview: the builder views it, the red-team views it, and the coordinator views it, three full-size views, all passing, before the thumbnail ships. Applies to every thumbnail from Nov 8 onward, Joker Gaming and NeedCraft alike. In thumbnail briefs, spell the margin out: all text inside the central safe zone with a clear margin from every edge; the thumbnail brief's word-scan includes a safe-margin view.

## <a id="m28"></a>**M28 CARD-TO-IMAGE CONTRADICTION CHECK: READ THE CARD ON THE FRAME.**

At storyboard AND on inspected rendered frames, read every card, chip, and label exactly as the viewer sees it, composited over its actual image, and ask three questions: (1) does the image SHOW what the card says? (2) does the image CONTRADICT the card? (3) does the card cover or collide with text already in the frame? If any answer fails, re-stage the beat: move the card, change the image, or rewrite the card. Do not ship it on a docked point. A card whose words are ledger-sourced (M17) and whose frame is safety-clean (M19) can still be wrong TOGETHER: the words and the picture are checked separately by every gate, and nobody reads them as one statement. The check is a named step at storyboard (card placement named against its frame) and on inspected frames (builder plus red-team each read the card in place).

## <a id="m33"></a>**M33 A TARGETED REBUILD RE-VERIFIES THE WHOLE REBUILT CARD, ELEMENT BY ELEMENT.**

When a fix re-renders one card, the builder's QC re-verifies EVERY design element on that card against the previous version: pill, source line, scrim, margins, legibility, not just the line that changed. A targeted fix is a rebuild of that card, and the card is checked whole, not by delta. Checked by viewing the rebuilt card's graphic file directly AND its delivered frames, side by side with the same frame of the previous version.

## <a id="m34"></a>**M34 FIGURE CARDS CARRY THEIR QUALIFIER WORD: ON THE CARD, WITH THE FIGURE, AT HEADLINE SIZE.**

A figure's qualifier ("over" / "plus" / "more than" / "above" / "estimated" / "net of") must appear ON the card WITH the figure, at headline size, never only in the VO, the description, or a small sub-line. A qualifier that lives only in the VO does not cure a headline figure that reads as exact. Checked at storyboard (every figure card names its qualifier word, its size, and the spoken syllable it syncs to) and on inspected rendered frames (read the figure plus qualifier together, as a viewer would; if the card alone reads as an exact figure, it FAILS). A dropped qualifier is a figure misstatement, not a wording preference. M31's logic ("a sub-line never cures a headline") applies to figures as well as to time and eligibility.
