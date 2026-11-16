# Troubleshooting and FAQ

## Troubleshooting

### The five template failure modes

These five are the known ways the Remotion template fails. Each has
a fix that was proven on the Nov 15 run. If a failure is not one of
these five, stop and read the error before retrying: a blind retry on
this machine has caused an OOM kill and a stuck lock before.

1. Remotion 4 rejects CRF 0 for H.264. The render command passes
   `--crf=12` (see the render command in the template README and the
   `npm run render` script). Do not ask
   for CRF 0: Remotion 4 refuses it. The high-quality master step the trio
   used is crf 12 — lossy, not lossless (CRF 12 is a lossy encode; the
   pipeline is master (lossy crf 12) → grade/fix (lossy crf 18), i.e. two
   lossy generations); the fix pass re-encodes to crf 18.
2. Frame timeout at the 30s default. A render that dies partway with a
   frame timeout needs `--timeout=120000` in the render command. It is
   already in the template's `npm run render` script: use the script,
   do not hand-type the command from memory.
3. Concurrent sibling render causes an OOM kill. Run ONE render at a
   time on a small machine. The trio lost a render at frame 107 of
   1200 to a concurrent sibling render. RAM is the binding constraint:
   about 8 GB total on the build machine, often only about 800 MB free
   while browser tasks run.
4. The render outputs yuvj420p / full-range video even with
   `--pixel-format=yuv420p`. The flag does not take effect in the
   Chromium screenshot pipeline. This is expected, not a failure of
   your command. Never ship the raw render: run
   `post-render-fix.sh` (Step 11), which re-encodes with the M36
   filter chain and verifies the tags.
5. Output-level colour flags do not stick. Setting `-color_trc` or
   `-color_primaries` on the ffmpeg output line does NOT change the
   tags: libx264 takes VUI from frame properties. The fix is
   `setparams` inside the filter chain (M36). If ffprobe still shows
   the wrong transfer or primaries after a fix pass, check that
   `setparams` is inside the `-filter_complex` or `-vf` chain, not on
   the output line.

### Loudnorm out of band

Symptom: the delivered file measures outside -16 to -14 LUFS, or true
peak above -1.0 dBTP.

1. Measure on the DELIVERED file, never on the mix or the raw render:
   the mono mix gains about +3 dB in the stereo render, so a mix that
   measures fine can clip in the render (V3 clipped at TP +0.18
   before loudnorm).
2. Fix with gain plus a limiter, never a second loudnorm pass. V1's
   first final read -16.30 (out by 0.30 LU): +0.5 dB measured -16.1
   and was rejected; +0.9 dB with alimiter (limit 0.794, attack 5,
   release 50, level=false) measured -15.9 / -1.72 and shipped.
3. If a single-pass target of I=-16 reads about -16.16 and fails the
   floor, retarget to I=-15.5 (the trio recipe). V3 needed three
   passes to land in band (-15.21 / -1.16): that is normal, not a
   defect in your mix.
4. Re-measure after every fix. A loudness number claimed without a
   fresh measurement on the delivered file fails M25.

### Colour tags wrong on the delivered file

Symptom: ffprobe shows anything other than yuv420p, tv range, bt709
space plus transfer plus primaries.

1. Re-encode from the raw render with the M36 chain:
   `scale=in_range=pc:out_range=tv` plus
   `setparams=range=tv:color_primaries=bt709:color_trc=bt709:colorspace=bt709`
   in the filter chain, CRF 18, preset slow, loudnorm re-applied in
   the same pass. `post-render-fix.sh` does exactly this and exits
   non-zero if any field is wrong.
2. Do NOT try the output-level flags first: they do not stick (failure
   mode 5 above). V2's MAJOR-1 was exactly this: the delivered file
   was yuvj420p / pc / bt470bg with transfer and primaries unknown,
   and the fix was the in-chain re-encode.
3. Verify with ffprobe on the delivered file before red-team. A render
   whose colour tags are unverified is UNVERIFIED, not passed (M36).

### Kokoro will not synthesise

1. Check the install with `scripts/setup-check.sh` (see the Install
   section in SKILL.md). The common causes are a missing model file
   in `$HOME/.cache/kokoro-onnx/` (kokoro-v1.0.onnx plus
   voices-v1.0.bin) and the espeak-ng data path (see the Install
   section: the loader needs its data path symlinked, and the exact
   path depends on the espeak-ng build).
2. Prove Kokoro by running it (M5): a new install gets a first-try
   synthesis of one sentence before any real VO is attempted.
3. If Kokoro mangles a word, bypass it in the SPOKEN text only, after
   testing spellings: "Kaseya" needed 7 tested spellings before
   "Kuh-say-uh" passed. On-screen text keeps the correct spelling.

### faster-whisper hears a different word from the script

Prove it with a fresh Kokoro control synthesis before changing the
caption: if the control synthesis hears the same way, it is a
Whisper artefact, not a VO defect. V2's "unlocked" hearing was
proved an artefact this way (fresh synthesis sample-identical to the
delivered stem, max diff 0.0). The caption uses script spelling.
Whisper-over-music artefacts are expected on the final mix: lines
mangled over the bed but heard correctly on the clean concat are
artefacts, not missing VO.

### A caption overlaps a card window

Fix the phrase timings in `data.ts`: no phrase may start, end, or sit
inside a card window. `Captions.tsx` suppresses overlaps at render
time, but a suppressed phrase is a data error, and the validator
script (`scripts/validate-build.py`) flags it before render. Move the
phrase, do not delete the card window.

## FAQ

**Do I need the Pro Pack to use this skill?**
No. The free skill is complete on its own: workflow, all 36 rules,
commands, rubric, thumbnail method, and worked examples. The Pro Pack
adds the working files: the Remotion template, the grade LUT, the
thumbnail prompt pack, subtitle presets, checklists, and
frame-accurate timeline breakdowns. Without the Pro Pack you bring
your own renderer that can hit the same gates.

**Where do I get the footage?**
From Rockstar, and only from Rockstar: the Newswire, the official
download pages, and the official YouTube channel. See
`references/sourcing-guide.md`. You supply your own official source
material: this skill contains no footage, trailers, logos, or music.

**Can I monetise Shorts made with this skill?**
Grey zone, stated honestly. Rockstar's policy is written for
non-commercial fan use and never names ad revenue. Monetised GTA
videos are common in practice, but that practice is tolerated, not
licensed, and Take-Two can request removal at any time. Never claim
Rockstar allows monetised GTA Shorts. Licensing requests go to
copyright@take2games.com.

**What if my verified pool is smaller than need plus slack?**
STOP before VO, cards, and mix (M20). Report it. Either narrow the
topic to one that fits the pool, or find more verified clean frames.
Never build VO, cards, and mix on an unproven pool.

**ChatGPT's word count differs from my hand count. Which wins?**
Your hand count wins, always. Count tokens and spoken words yourself
(see the word-count convention in SKILL.md). ChatGPT's count has been
wrong on every trio script's first return (V1 first return 114 words,
V2 first return 115 words, both superseded).

**Does this skill work for non-news GTA Shorts?**
It was built for GTA VI NEWS Shorts: the fact ledger, the brief beats,
and the upload checklist assume a news peg with a verifiable source.
For a non-news Short (gameplay, comedy, montage), the editing rules
still apply (captions, cards, grade, loudness, gates), but the brief
structure and the ledger labels do not fit. Use the editing rules,
write your own brief.

**What if the owner has not watched the video?**
It does not ship. The owner's watch/listen is final and overrides
every gate score (M8). No gate score substitutes for it.
