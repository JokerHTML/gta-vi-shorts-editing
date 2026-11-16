# Exact Commands

When to load: load this file when you need a literal command or code
fragment for VO synthesis, Whisper checking, concat, stills and motion
cutting, mix checking, loudnorm, or the M36 colour-tag fix (Steps 4-11).
The SKILL.md body names the step; the literal invocation lives here.

Only the commands in the "verbatim" sections are verbatim from the
build sources. Anything labelled template is NOT verbatim history:
syntax-verify it before use, against the delivered file, using the
verification procedure at the end of this file.

Paths below use `$HOME` as a placeholder for the reader's home
directory.

## Exact commands

Only the commands below are verbatim from the build sources. Anything labelled template is NOT verbatim history: syntax-verify it before use.

### Kokoro VO synthesis (verbatim)

```python
kokoro = Kokoro("$HOME/.cache/kokoro-onnx/kokoro-v1.0.onnx",
                 "$HOME/.cache/kokoro-onnx/voices-v1.0.bin")
samples, sr = kokoro.create(text, voice="am_adam", speed=1.1, lang="en-us")
```

```python
def trim_dbfs(x, sr, thresh_db=-40.0):
    peak = np.max(np.abs(x))
    if peak == 0:
        return x
    thresh = peak * 10 ** (thresh_db / 20.0)
    idx = np.where(np.abs(x) > thresh)[0]
    if len(idx) == 0:
        return x
    return x[idx[0]:idx[-1] + 1]
```

### faster-whisper VO check (verbatim)

```python
model = WhisperModel("small", device="cpu", compute_type="int8")
segments, info = model.transcribe(path, language="en", beam_size=5, word_timestamps=True)
```

Normalization used in the check: lower-case, strip `. , — '`, then replace Whisper digit forms: `"13th"` to `"thirteenth"`, `"31st"` to `"thirty first"`, `"21st"` to `"twenty first"`, `"18th"` to `"eighteenth"`, `"19th"` to `"nineteenth"`, `"7 pm"` to `"seven p m"`, `"ign"` to `"ign"`.

### VO concat (verbatim)

```python
# gaps in frames between stems (varied, M3)
GAPS_F = [8, 5, 8, 5, 8, 5]
```

```python
cmd = ["ffmpeg", "-y", "-v", "error"] + inputs + [
    "-filter_complex", concat, "-map", "[aout]",
    "-ar", "24000", "-ac", "1", os.path.join(WORK, "vo_concat.wav"),
]
```

Each stem contributes `"-i", s["file"]` and each gap contributes `"-f", "lavfi", "-t", str(gap_s), "-i", "anullsrc=r=24000:cl=mono"`, and `concat = "".join(labels) + f"concat=n={len(labels)}:v=0:a=1[aout]"`.

### Cut stills and motion (verbatim)

Precrop plus static still clip:

```python
run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf",
     f"crop=1215:2160:{x}:0", "-frames:v", "1", out], f"precrop {name}")
run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", img,
     "-vf", "scale=1080:1920,format=yuv420p", "-frames:v", str(frames),
     "-c:v", "libx264", "-crf", "0", "-preset", "veryfast", out], name)
```

Motion span (9:16 window from the measured active picture only):

```python
run(["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(dur), "-i", src,
     "-vf", f"crop={win_w}:{win_h}:{win_x}:{win_y},scale=1080:1920,fps=30,format=yuv420p",
     "-frames:v", str(frames),
     "-c:v", "libx264", "-crf", "0", "-preset", "veryfast", out], name)
```

V3 motion windows (verbatim values): T2 spans `972x1728 @1434,216` (y=216 active area); LT span `1080x1920 @1380,120` (y=120 active area).

V2 still recipe (A/B recipe, CRF 18):

```python
r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src,
                    "-vf", f"crop=1215:2160:{cx}:0,scale=1080:1920",
                    "-q:v", "2", jpg])
r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-t", "4", "-i", jpg,
                    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-r", "30", mp4])
r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "12.0", "-i", LT, "-t", "2.1",
                    "-vf", "crop=1080:1920:1700:120,scale=1080:1920,setsar=1",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-r", "30", "-an", out])
```

Frame-count verification (verbatim pattern):

```python
p = subprocess.run(["ffprobe", "-v", "error", "-count_frames",
                    "-select_streams", "v:0", "-show_entries", "stream=nb_read_frames,width,height",
                    "-of", "csv=p=0", os.path.join(CLIPS, f)],
                   capture_output=True, text=True)
```

### Mix silencedetect check (verbatim)

```python
r = subprocess.run(["ffmpeg", "-v", "info", "-i", os.path.join(WORK, "mix.wav"),
                    "-af", "silencedetect=noise=-50dB:d=0.3", "-f", "null", "-"],
                   capture_output=True, text=True)
```

Mix constants (verbatim): `DUCK = 0.33`, `FADE = int(0.1 * SR)`, `SR = 24000`, `FPS = 30`, peak scale `10 ** (-1.5 / 20)`.

### Loudnorm: older stealth-patch recipe (verbatim, labelled)

The literal loudnorm command recorded on disk is the older stealth-patch one (single pass I=-14, TP=-1.5, verified to land -15.99 LUFS / -1.10 dBTP). It is NOT the Nov 15 trio recipe. The trio recipe is single-pass I=-15.5 (see the template below).

```python
r = subprocess.run([
    "ffmpeg", "-y", "-v", "error", "-i", f"{W}/video_cap.mp4", "-i", f"{W}/vo_concat.wav",
    "-map", "0:v", "-map", "1:a",
    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
    "-t", "37.79", "-movflags", "+faststart", f"{B}/final.mp4",
])
```

Measure step (verbatim, same file):

```python
r = subprocess.run([
    "ffmpeg", "-v", "info", "-i", f"{B}/final.mp4", "-vn",
    "-af", "loudnorm=print_format=json", "-f", "null", "-",
], capture_output=True, text=True)
```

### M36 colour-tag fix fragments (verbatim)

```
scale=in_range=pc:out_range=tv
setparams=range=tv:color_primaries=bt709:color_trc=bt709:colorspace=bt709
```

### Templates: syntax-verify before use (NOT verbatim history)

The five items below were recorded only as prose fragments in the sources. Do NOT present them as verbatim history. Verify each one against the delivered file before trusting it.

- **Remotion render (template, syntax-verify before use):** `npx remotion render src/index.ts JokerTemplate out/raw.mp4 --crf=12 --timeout=120000 --concurrency=2 --pixel-format=yuv420p` (also the `npm run render` script). Remotion 4 rejects CRF 0 for H.264 (render at crf 12 — the high-quality master, lossy not lossless); `--pixel-format=yuv420p` does not prevent full-range output. Verify: render completes all frames, output is 1080x1920 at 30fps.
- **Nov 15 loudnorm invocation (template, syntax-verify before use):** single-pass `loudnorm=I=-15.5:TP=-2.0:LRA=11` on the delivered file, then measure with `loudnorm=print_format=json`. Verify: measured input_i in -16 to -14 LUFS and input_tp at or below -1.0 dBTP. If out of band, fix with gain plus a limiter, never a second loudnorm pass.
- **Grade filter graph (template, syntax-verify before use):** chain order is deband, grain, S-curve (0.94 highlight shoulder), saturation 1.00, clamp AFTER grade (Y[20,234], U/V[16,240]), yuv420p, crf 18, preset slow, tags bt709 x4 plus tv. No literal filter graph with parameters exists in the sources. Verify: ffprobe shows yuv420p, tv, bt709 x4; signalstats shows the clamp holding on the delivered file.
- **M36 full re-encode (template, syntax-verify before use):** re-encode from the raw render with the two filter fragments above plus CRF 18, loudnorm re-applied in the same pass. Verify: ffprobe shows yuv420p, tv range, bt709 space, bt709 transfer, bt709 primaries, all four fields; loudness re-measured in band.
- **V1 colour remux (template, syntax-verify before use):** lossless remux (`-c copy`) with `-color_primaries`, `-color_trc`, and `-colorspace` set to bt709. The `h264_metadata` bitstream filter alone did NOT change the tag; the output-level remux is the working route. Verify: ffprobe tags read bt709 x4 and framemd5 of decoded frames is unchanged versus the pre-remux file.

### Verification procedure for any delivered file

Run ffprobe and read: `pix_fmt` (must be yuv420p), `color_range` (tv), `color_space`, `color_transfer`, `color_primaries` (all bt709). Run loudnorm with `print_format=json` and read `input_i` (-16 to -14 LUFS) and `input_tp` (at or below -1.0 dBTP). Run silencedetect (noise -50dB, d=0.3 on the mix; noise -40dB, d=0.5 on the delivered file) and read 0 hits. Run cropdetect and read 1080:1920:0:0 with no bars on every motion span.
