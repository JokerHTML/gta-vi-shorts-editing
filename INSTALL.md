# INSTALL.md — GTA VI Shorts Editing Skill v1.2.0

Literal install commands for a fresh machine. Primary platform: **Ubuntu 24.04 LTS**.
macOS: Homebrew equivalents are noted. Windows: use WSL2 running Ubuntu 24.04; there is
no native Windows route. Run `scripts/setup-check.sh` after installing — it verifies
versions, not just presence.

## ffmpeg 8.x (Ubuntu 24.04 ships ffmpeg 7.x — the system package is the wrong version)

Static build from johnvansickle.com (full build, includes libx264, loudnorm, signalstats):

```bash
cd /tmp
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar xf ffmpeg-release-amd64-static.tar.xz
cd ffmpeg-*-amd64-static
sudo cp ffmpeg ffprobe /usr/local/bin/
ffmpeg -version   # must read 8.x
ffmpeg -hide_banner -h filter=loudnorm | grep -q loudnorm && echo "loudnorm OK"
```

macOS: `brew install ffmpeg` (Homebrew tracks current ffmpeg; verify with `ffmpeg -version`).

## Node 24 + npm 10 (Ubuntu 24.04 ships Node 18)

Via NodeSource:

```bash
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
sudo apt-get install -y nodejs
node --version   # must read v24.x
npm --version    # must read 10.x
```

Or via nvm: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash`,
then `nvm install 24 && nvm use 24`. macOS: `brew install node@24`.

## Python 3.12

Ubuntu 24.04 ships Python 3.12 as the system Python:

```bash
sudo apt-get update && sudo apt-get install -y python3 python3-venv python3-pip
python3 --version   # must read 3.12.x
```

macOS: `brew install python@3.12`.

## Kokoro TTS (kokoro-onnx 0.6.1)

```bash
python3 -m venv $HOME/workspace/.venvs/v1fix1
$HOME/workspace/.venvs/v1fix1/bin/pip install kokoro-onnx==0.6.1 numpy soundfile
mkdir -p $HOME/.cache/kokoro-onnx
cd $HOME/.cache/kokoro-onnx
# Model files, from the kokoro-onnx GitHub release "model-files-v1.0"
# (thewh1teagle/kokoro-onnx; the pip package ships code, NOT the model):
curl -fLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -fLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
ls -la   # kokoro-v1.0.onnx ~310 MB; voices-v1.0.bin ~27 MB
```

**espeak-ng symlink (the most common Kokoro failure).** The loader demands its baked-in
data path symlinked to the venv's espeak-ng-data. Read the path the loader error names on
your machine and symlink THAT path:

```bash
ln -s $HOME/workspace/.venvs/v1fix1/lib/python3.12/site-packages/espeakng_loader/espeak-ng-data <loader-path>/espeak-ng-data
ls -l <loader-path>/espeak-ng-data   # must show the symlink, not "No such file"
# one-sentence test synthesis, then listen to the output file
```

The symlink lives outside the workspace: re-apply after any VM replacement.

## faster-whisper (1.2.1)

```bash
python3 -m venv $HOME/workspace/.venvs/fw
$HOME/workspace/.venvs/fw/bin/pip install faster-whisper==1.2.1
# Whisper models (tiny, base, small) download on first use into
# $HOME/.cache/huggingface/ (about 1.4 GB for the set the trio used).
```

## Remotion 4.0.543 (Pro Pack template)

```bash
cd pro-pack/remotion-template
npm install   # all @remotion/* packages stay on the same exact version, 4.0.543
```

If `/tmp` is a small tmpfs (512 MB on the build machine), run installs with
`TMPDIR=$HOME/workspace/tmp --no-cache-dir` or `pip install` fails with
"No space left on device". Run `npm install` and renders from a workspace directory,
not from `/tmp`.

## yt-dlp (fetching official trailers)

```bash
sudo apt-get install -y yt-dlp
# or: pip install yt-dlp
```

## Verify

```bash
bash free-skill/scripts/setup-check.sh
# Expected: RESULT: ALL CHECKS PASS (with versions named).
# The script checks Node >= 24, npm >= 10, Python 3.12, ffmpeg 8.x with
# loudnorm, Remotion, yt-dlp, the espeak-ng path, Kokoro model files, and
# free disk space. Exit 0 names exactly what was verified.
```
