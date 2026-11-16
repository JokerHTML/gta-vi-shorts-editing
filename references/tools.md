# Tools

When to load: load this file when you need a tool version, a venv path,
or a gotcha before installing or running anything (Step 4, Step 5,
Step 10). The SKILL.md body states only the tool names; the versions,
paths, and gotchas live here.

Paths below use `$HOME` as a placeholder for the reader's home
directory. On the Nov 15 build machine `$HOME` was `/home/hatch`;
replace it with your own home directory, or set the matching
environment variable. The `setup-check.sh` script in `scripts/`
resolves these paths for you.

## Tools

VM reality: Ubuntu 24.04, 4 CPUs, about 8 GB RAM, CPU-only (no GPU), 65 GB free disk. RAM is the binding constraint: run heavy tools ONE at a time.

| Tool | Version | Path or note | Use |
|---|---|---|---|
| ffmpeg | 8.1.2 | system, with libass, libfontconfig, libfreetype, libfribidi, libmp3lame, libopus, libvpx, libx264, libx265; no libvmaf | Encode, decode, drawtext, zoompan, ASS subtitles, loudnorm, signalstats |
| yt-dlp | 2026.10.21 | `$HOME/.local/bin/yt-dlp` | Download source clips and reference videos |
| Python | 3.12.3 | system | Base interpreter |
| Node / npm | 24.22.1 / 10.9.4 | system | Remotion |
| Kokoro TTS | kokoro-onnx 0.6.1 | venv `$HOME/workspace/.venvs/v1fix1`, voice am_adam | Voiceover |
| faster-whisper | 1.2.1 (av 13.1.0) | venv `$HOME/workspace/.venvs/fw` | STT plus word timestamps |
| Whisper models | tiny, tiny.en, base, base.en, small, small.en | `$HOME/.cache/huggingface` (1.4 GB) | tiny is fast; small is more accurate |
| PIL / numpy / scipy / opencv / pydub / soundfile | pillow 10.2.0, numpy 2.5.4, scipy 1.11.4, opencv 5.0.0, pydub 0.25.1 | system python | Graphics plus audio basics |
| Fonts | Inter, Anton, Manrope, SpaceGrotesk, IBM Plex Mono, Instrument Serif plus 1900 system fonts | `$HOME/.fonts/needcraft/`, `/usr/share/fonts/` | Captions and cards (Inter is the pipeline standard) |
| moviepy | 2.2.1 | venv `$HOME/workspace/.venvs/proedit` (1.4 GB), Python 3.12.3 | Timeline compositing in Python |
| scenedetect-headless | 0.7.3 | proedit venv | Cut and scene detection |
| librosa | 1.0.1 | proedit venv | Audio analysis: tempo, BPM, beat tracking, onsets |
| pedalboard | 0.9.26 | proedit venv | Compressor, EQ, de-esser, limiter, reverb, highpass |
| noisereduce | 3.0.3 | proedit venv | Spectral-gating noise reduction for VO |
| pysubs2 | 1.9.1 | proedit venv | Read and write ASS/SRT subtitles |
| rembg | 2.0.87 | proedit venv | Background removal for thumbnails and cutouts |
| onnxruntime | 1.32.0 | proedit venv | Inference backend for rembg |
| ffmpeg-python | 0.2.0 | proedit venv | Build ffmpeg filter graphs in Python |
| auto-editor | 29.3.1 | proedit venv | Auto-cut silences and dead air |
| opentimelineio | 0.18.1 | proedit venv | Timeline interchange, EDL/FCPXML export |
| opencv-python-headless | 5.0.0.93 | proedit venv | Frame analysis, tracking, motion detection |
| pillow (proedit venv) | 11.3.0 pinned | proedit venv | Image ops |
| numpy / scipy / soundfile / imageio / av (proedit venv) | numpy 2.5.4, scipy 1.18.1, soundfile 0.14.0, imageio 2.38.1, av 13.1.0 pinned | proedit venv | Dependencies of the above |
| ImageMagick | 6.9.12-98 | `convert`, `identify` (v6: there is NO `magick` binary; that is v7) | Image ops |
| mediainfo | 24.01 | `/usr/bin/mediainfo` | Media inspection |
| sox | 14.4.2 | `/usr/bin/sox` | Audio ops |
| Blender | 5.3.0 | `$HOME/workspace/video-edit-tools/blender/blender-5.3.0-linux-x64/blender` | Headless 3D motion graphics; use BLENDER_WORKBENCH for fast CPU-safe renders |
| Remotion | 4.0.543 | `$HOME/workspace/video-edit-tools/remotion-test/` | React motion graphics; all `@remotion/*` packages must stay on the SAME exact version |

Gotchas: (1) pip plus /tmp: /tmp is a 512 MB tmpfs, so plain `pip install` fails with "No space left on device". ALWAYS install with `TMPDIR=$HOME/workspace/video-edit-tools/tmp` (and `--no-cache-dir` for big installs). (2) av MUST stay at 13.1.0 in the proedit venv: faster-whisper 1.2.1 calls `av.open(..., metadata_errors=...)`; av 19.x removed that kwarg and faster-whisper crashes. Do not upgrade av. (3) pillow is pinned to 11.3.0 because moviepy 2.2.1 requires `pillow<12.0` while rembg 2.0.87 requires `pillow>=12.3.0`; they cannot both be satisfied. Runtime was verified working with 11.3.0 for both. Do not "fix" the warning by upgrading pillow (breaks moviepy) or downgrading rembg. (4) MoviePy 2.x TextClip needs a font FILE path, for example `/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf`; a bare font name fails. (5) rembg default session is about 1 GB (`bria-rmbg`); always pass an explicit light session: `new_session('u2net')` (176 MB). (6) RAM: about 8 GB total, often only about 800 MB free when browser tasks are running. Run one heavy tool at a time; never run apt plus a model load together. (7) apt mirror is very slow (about 12.5 kB/s observed); for anything over 50 MB use a direct download. `libasound2` does not exist on Ubuntu 24.04; it is `libasound2t64`. (8) Kokoro espeak-ng quirk: the loader demands its baked-in data path symlinked to the venv's espeak-ng-data. On the Nov 15 build machine that path was the nested `/home/runner/work/espeakng-loader/espeakng-loader/espeak-ng/_dynamic/share/espeak-ng-data/phontab`; on your machine, read the path the loader error names and symlink THAT path. Literal form:

```bash
ln -s $HOME/workspace/.venvs/v1fix1/lib/python3.12/site-packages/espeakng_loader/espeak-ng-data <loader-path>/espeak-ng-data
ls -l <loader-path>/espeak-ng-data   # must show the symlink
```

Then run a one-sentence test synthesis and listen to it. The symlink lives OUTSIDE the workspace: re-apply after any VM replacement. (9) Remotion licence: free for individuals and companies of up to 3 people; a paid company licence is required at 4 or more people. **Automators tier:** Remotion's FAQ treats programmatic rendering (`npx remotion render`, `renderMedia()`) as automation, which can require the Automators licence ($0.01/render, $100/month minimum) — and this skill exists precisely to drive rendering through agents. Check Remotion's licence FAQ before building an agent pipeline; a buyer building one may need a paid licence this skill cannot grant. (10) Literal install commands live in `INSTALL.md` (ffmpeg 8 static build, Node 24 via NodeSource/nvm); the system packages on Ubuntu 24.04 are ffmpeg 7.x and Node 18, not the required versions.

Not installed, with reason: DaVinci Resolve (needs a GPU plus a desktop GUI); libvmaf (system ffmpeg was not built with it; use signalstats instead); aeneas (superseded by faster-whisper word timestamps, unmaintained); DeepFilterNet (needs PyTorch, about 2 GB, heavy on this VM); OpenCut (needs Adobe Premiere Pro); Kdenlive, Shotcut, Olive (desktop GUI editors, not scriptable); Natron (GUI compositing; Blender plus ffmpeg cover it); GIMP (PIL plus ImageMagick cover scripted image work).
