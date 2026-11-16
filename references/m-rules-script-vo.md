# M-rules: Script, voiceover & captions

Part of the GTA VI Shorts Editing Skill v1.2.0. Load when: Load when writing or checking the script, synthesising VO, or building captions.

M-numbers are stable and never renumbered. The full rule text lives here; SKILL.md carries only the gates summary and the reference index.

## Contents

- [M3](#m3)
- [M5](#m5)
- [M7](#m7)
- [M11](#m11)
- [M18](#m18)
- [M26](#m26)

## <a id="m3"></a>**M3 VO gaps varied, never metronome.**

VO gaps varied, never metronome. Trio practice: V1 gaps 8/10/6/12/9/8/10/7 frames; V3 gaps 8/5/8/5/8/5. V2 used 8 uniform gaps of 0.35s: that was a documented deviation (the A/B stem recipe), not a second standard, and the uniform-gap recipe is retired. Uniform gaps are not acceptable as a recipe.

## <a id="m5"></a>**M5 Kokoro proven by running.**

Kokoro proven by running (new install, first-try synthesis).

## <a id="m7"></a>**M7 Beat-length check pre-render.**

Beat-length check pre-render; timeline derived from measured VO durations. At pre-render-plan time no VO exists yet, so the plan's beat-length check is a planning estimate (word count x 2.5 words/sec); the binding check runs AFTER VO synthesis, against measured stem durations — re-validate the plan with the measured numbers before cutting (see references/pre-render-plan.md).

## <a id="m11"></a>**M11 Peak/word-pop captions only.**

Peak/word-pop captions only, never a running transcript; no permanent line. Adapted practice: word-pops on stressed words only; later practice is phrase captions of 2-4 words, fixed lower-third, spring pop-in, never one-word-at-a-time through function words.

## <a id="m18"></a>**M18 SCRIPT REPETITION SCAN.**

Before VO synthesis, read the script as a text, not as footage. No attribution word may open 3 or more VO lines; no phrase may repeat verbatim across beats; no single noun may carry every beat. Every gate scores the rendered file (frames, loudness, STT, factual labels); none of them reads script pattern, so a high-scoring render can still ship a script the owner rules bad on first listen. Varied attribution is the fix (reportedly / The demo / per the preview / Nelson says / Press:). Scope is never cut to fix repetition (M17 still binds every rewritten line). A repetition found after render is a rebuild, not a note.

## <a id="m26"></a>**M26 M18 TIGHTENING: COUNT ATTRIBUTION ROOTS BY OCCURRENCE, NOT BY POSITION.**

No attribution root ("reportedly" / "reported" / "confirmed" / "per" plus source, and any other attribution word) may occur more than TWICE in any 3 consecutive VO lines, regardless of where it sits in the line: mid-line counts exactly like line-opening. After VO, red-team checks STT word timestamps: 3 occurrences of the same attribution root within any about 15s window FAILS the script, whatever the text scan said. If it trips, the fix is a ChatGPT rewrite BEFORE render (a repetition found after render is a rebuild, not a note, per M18). The red-team's M18 re-listen is the gating check, and their fresh ear decides. The threshold is 2-in-3-lines and 3-in-15s, not zero repetition: a "reported" 3x case with only two in the opening stretch and the third 27.1s later in a different slot PASSED as a deliberate two-item list intro, not a tic.

Window procedure: take the STT word timestamps, list every occurrence of each attribution root with its timestamp, then slide a 15-second window over them: any window holding 3 occurrences of the same root FAILS. Worked example: "reportedly" at 2.1s, 9.4s and 14.8s = 3 inside 15s, FAIL; the same three at 2.1s, 9.4s and 29.2s = only 2 inside any 15s window, PASS (the V2 "reported" 3x case, third occurrence 27.1s later).
