# M-rules: Render, grade & colour

Part of the GTA VI Shorts Editing Skill v1.2.0. Load when: Load at render, grade, colour-fix, or loudnorm time.

M-numbers are stable and never renumbered. The full rule text lives here; SKILL.md carries only the gates summary and the reference index.

## Contents

- [M9](#m9)
- [M10](#m10)
- [M21](#m21)
- [M29](#m29)
- [M36](#m36)

## <a id="m9"></a>**M9 Synthetic flat-frame test FIRST.**

Synthetic flat-frame test FIRST (lossless, 3 levels); LUT layouts tested on tiny chart images, never full encodes.

Procedure (flat-frame test): render three 1080x1920 flat frames (Y=16, Y=128, Y=235) through the grade chain with `ffmpeg -f lavfi -i color=c=0x808080:s=1080x1920:d=0.1` (one per level), then `ffprobe`/signalstats the outputs. Test every LUT layout on a tiny 64x64 chart image first (`ffmpeg -i chart.png -vf lut3d=... out.png`); never test a layout on a full encode. If any level clips or banding appears, fix the chain before rendering.

## <a id="m10"></a>**M10 Grade applied, not neutral.**

Grade applied (S-curve 0.94 shoulder plus saturation 1.00), not neutral. The 1.05 value in the older rule was the pre-Remotion value; the measured v3 recipe locks 1.00, and 1.00 is now the rule. The v3 recipe value wins because it is the one measured on shipped videos.

## <a id="m21"></a>**M21 PIXEL-CHECK BARS ON EVERY MOTION SPAN, NEVER ONE REPRESENTATIVE SPAN.**

Builder QC must pixel-verify letterbox bars separately on EVERY motion span in the timeline: head, middle, and tail frames of each span, and name each span's verdict in the QC report. A bar-check that names only one span verifies only that span; every unnamed span is UNVERIFIED, not passed. Any span found barred is re-cut as a fill-crop and re-verified before red-team, never left for red-team to catch.

## <a id="m29"></a>**M29 SOURCE ACTIVE-AREA MEASUREMENT BEFORE ANY CROP: M21'S MISSING FIRST STEP.**

Before any motion span is cropped, measure the active picture bounds of the source frame (row-profile at full resolution: first and last non-black rows) and record the active area in the build report. A 3840x2160 trailer file is NOT a full-frame picture: both trailers carry baked-in letterbox (Trailer 2 active y=216..1943; Launch Trailer active y=120..2039). Any crop taken from the file's full frame inherits those bars. M21's per-span pixel check is then run on the DELIVERED file (head, mid, tail per span), never on the construction argument: "impossible by construction" is not a measurement, and it fails M25 when the delivered file contradicts it. Checked at pool and triage stage (active area named per source) and re-checked on the delivered file (M21).

## <a id="m36"></a>**M36 REMOTION COLOUR-SPACE FIX IS SETPARAMS-IN-FILTER-CHAIN, VERIFIED ON THE DELIVERED FILE.**

A Remotion/Chromium render outputs yuvj420p / full-range video even with `--pixel-format=yuv420p`: the flag does not prevent it. The fix is a re-encode with `scale=in_range=pc:out_range=tv` plus `setparams=range=tv:color_primaries=bt709:color_trc=bt709:colorspace=bt709` in the filter chain (output-level `-color_trc` / `-color_primaries` flags do NOT stick: libx264 takes VUI from frame properties). Loudnorm is re-applied in the same pass and re-measured. The delivered file is then verified by ffprobe: yuv420p, tv range, bt709 space plus transfer plus primaries, all four fields, before red-team. A render whose colour tags are unverified on the delivered file is UNVERIFIED, not passed, whatever the render command claimed.
