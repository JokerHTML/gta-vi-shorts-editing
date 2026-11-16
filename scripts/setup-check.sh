#!/usr/bin/env bash
# setup-check.sh - Install / prerequisites check for the GTA VI Shorts Editing skill.
#
# Checks versions (not just presence) of ffmpeg 8.x, Node 24, npm 10,
# Python 3.12, plus Remotion, yt-dlp, the Kokoro model files, the espeak-ng
# data path, and free disk space, and prints install hints for anything
# missing. Exit 0 = everything listed below was verified (the result line
# names exactly what was verified). Exit 1 = something is missing or the
# wrong version (the missing item is named; install it, then re-run).
#
# Untested on a fresh machine: this script was tested on the Nov 16
# build machine only, where the venvs already existed. If you run it
# somewhere new and a check misfires, the check output names the exact
# path or command it looked for, so you can see what it expected.
#
# Paths: $HOME is your home directory. Override the venv locations
# with KOKORO_VENV and FW_VENV if yours live elsewhere.
#   KOKORO_VENV=$HOME/workspace/.venvs/v1fix1
#   FW_VENV=$HOME/workspace/.venvs/fw
set -u

FAIL=0
say_ok()   { printf 'OK    %s\n' "$1"; }
say_fail() { printf 'MISS  %s -- %s\n' "$1" "$2"; FAIL=1; }

KOKORO_VENV="${KOKORO_VENV:-$HOME/workspace/.venvs/v1fix1}"
FW_VENV="${FW_VENV:-$HOME/workspace/.venvs/fw}"
KOKORO_MODELS="${KOKORO_MODELS:-$HOME/.cache/kokoro-onnx}"

# ffmpeg 8.x (needs libx264, loudnorm, signalstats; no libvmaf on the build machine)
if command -v ffmpeg >/dev/null 2>&1; then
  FFVER=$(ffmpeg -version 2>/dev/null | head -1 | grep -o "[0-9]\+\.[0-9\.]\+" | head -1)
  FFMAJOR=${FFVER%%.*}
  if [ "$FFMAJOR" = "8" ]; then
    say_ok "ffmpeg 8.x: $(ffmpeg -version 2>/dev/null | head -1)"
  else
    say_fail "ffmpeg version ($FFVER)" "need ffmpeg 8.x; Ubuntu 24.04 ships 7.x — use the static build in INSTALL.md"
  fi
  if ffmpeg -hide_banner -h filter=loudnorm 2>/dev/null | grep -q loudnorm; then
    say_ok "ffmpeg loudnorm filter present"
  else
    say_fail "ffmpeg loudnorm filter" "your ffmpeg lacks loudnorm; install a full ffmpeg build"
  fi
  if ffmpeg -hide_banner -h filter=signalstats 2>/dev/null | grep -q signalstats; then
    say_ok "ffmpeg signalstats filter present"
  else
    say_fail "ffmpeg signalstats filter" "needed by post-render-fix.sh range gate; install a full ffmpeg build"
  fi
else
  say_fail "ffmpeg" "install ffmpeg 8.x via the static build in INSTALL.md"
fi

if command -v ffprobe >/dev/null 2>&1; then
  say_ok "ffprobe present"
else
  say_fail "ffprobe" "ships with ffmpeg; install ffmpeg"
fi

# Node 24 / npm 10 (Remotion 4 needs Node 24)
if command -v node >/dev/null 2>&1; then
  NODEMAJOR=$(node --version | grep -o "[0-9]\+" | head -1)
  if [ "$NODEMAJOR" = "24" ]; then
    say_ok "node 24: $(node --version)"
  else
    say_fail "node version ($(node --version))" "need Node 24; Ubuntu 24.04 ships Node 18 — use NodeSource or nvm (see INSTALL.md)"
  fi
else
  say_fail "node" "install Node 24 (nodesource or nvm, see INSTALL.md)"
fi
if command -v npm >/dev/null 2>&1; then
  NPMMAJOR=$(npm --version | grep -o "^[0-9]\+")
  if [ "$NPMMAJOR" = "10" ]; then
    say_ok "npm 10: $(npm --version)"
  else
    say_fail "npm version ($(npm --version))" "need npm 10 (ships with Node 24)"
  fi
else
  say_fail "npm" "ships with Node; install Node 24"
fi

# Python 3.12
if command -v python3 >/dev/null 2>&1; then
  PYVER=$(python3 --version 2>&1 | grep -o "[0-9]\+\.[0-9\+\.]\+" | head -1)
  if [ "${PYVER%%.*}" = "3" ] && [ "$(echo "$PYVER" | cut -d. -f2)" = "12" ]; then
    say_ok "python3 3.12: $(python3 --version 2>&1)"
  else
    say_fail "python3 version ($PYVER)" "need Python 3.12"
  fi
else
  say_fail "python3" "install Python 3.12"
fi

# yt-dlp (fetching official trailers)
if command -v yt-dlp >/dev/null 2>&1; then
  say_ok "yt-dlp: $(yt-dlp --version 2>/dev/null | head -1)"
else
  say_fail "yt-dlp" "install yt-dlp (apt or pip) — needed to fetch official trailers"
fi

# Remotion (template project, if present in the current directory tree)
if [ -f "package.json" ] && grep -q '"remotion"' package.json 2>/dev/null; then
  REMVER=$(grep -o '"remotion": "[^"]*"' package.json | grep -o "[0-9][0-9.]*")
  if [ "$REMVER" = "4.0.543" ]; then
    say_ok "remotion 4.0.543 in this project"
  else
    say_fail "remotion version ($REMVER)" "template pins 4.0.543; keep all @remotion/* on the same exact version"
  fi
else
  printf '%s\n' "NOTE  Remotion not checked: no package.json with remotion in this directory (run from the template folder to check it)."
fi

# espeak-ng data path (the known Kokoro failure)
ESPEAK_LINK=$(find /home/runner/work/espeakng-loader "$HOME/.cache" /usr/share/espeak-ng-data 2>/dev/null -maxdepth 0 -type l 2>/dev/null | head -1)
if [ -n "$ESPEAK_LINK" ]; then
  say_ok "espeak-ng symlink present: $ESPEAK_LINK"
else
  printf '%s\n' "NOTE  espeak-ng symlink not verified by this script: run a one-sentence Kokoro test synthesis — if the loader errors, read the path it names and symlink THAT path (see INSTALL.md)."
fi

# Free disk space (the known ENOSPC failure: /tmp is a 512 MB tmpfs)
FREE_MB=$(df --output=avail -m "$HOME" 2>/dev/null | tail -1 | tr -d ' ')
if [ -n "$FREE_MB" ] && [ "$FREE_MB" -ge 2048 ]; then
  say_ok "free disk in \$HOME: ${FREE_MB} MB"
elif [ -n "$FREE_MB" ]; then
  say_fail "free disk in \$HOME (${FREE_MB} MB)" "need at least 2 GB free for node_modules + renders"
fi

# Kokoro model files
if [ -f "$KOKORO_MODELS/kokoro-v1.0.onnx" ] && [ -f "$KOKORO_MODELS/voices-v1.0.bin" ]; then
  say_ok "Kokoro models in $KOKORO_MODELS (kokoro-v1.0.onnx + voices-v1.0.bin)"
else
  say_fail "Kokoro models in $KOKORO_MODELS" "download kokoro-v1.0.onnx and voices-v1.0.bin into \$HOME/.cache/kokoro-onnx/ (see SKILL.md Install)"
fi

# Kokoro venv + import
if [ -x "$KOKORO_VENV/bin/python" ]; then
  if "$KOKORO_VENV/bin/python" -c "import kokoro_onnx" 2>/dev/null; then
    say_ok "kokoro_onnx imports in $KOKORO_VENV"
  else
    say_fail "kokoro_onnx import in $KOKORO_VENV" "pip install kokoro-onnx==0.6.1 in that venv (use TMPDIR=\$HOME/workspace/tmp --no-cache-dir if /tmp is small)"
  fi
else
  say_fail "Kokoro venv $KOKORO_VENV" "create it and pip install kokoro-onnx==0.6.1, numpy, soundfile (see SKILL.md Install)"
fi

# faster-whisper venv + import
if [ -x "$FW_VENV/bin/python" ]; then
  if "$FW_VENV/bin/python" -c "import faster_whisper" 2>/dev/null; then
    say_ok "faster_whisper imports in $FW_VENV"
  else
    say_fail "faster_whisper import in $FW_VENV" "pip install faster-whisper==1.2.1 in that venv"
  fi
else
  say_fail "faster-whisper venv $FW_VENV" "create it and pip install faster-whisper==1.2.1 (see SKILL.md Install)"
fi

# ChatGPT / Gemini account note (no credential is ever checked here)
printf '%s\n' "NOTE  ChatGPT and Gemini accounts are NOT checked by this script."
printf '%s\n' "NOTE  You need a ChatGPT account for the Step 1 brief (scripts + SEO) and"
printf '%s\n' "NOTE  a Gemini account only if you use the Gemini thumbnail route."
printf '%s\n' "NOTE  No password, key, or token is ever asked for or stored by this skill."

if [ "$FAIL" -ne 0 ]; then
  echo "RESULT: MISSING ITEMS ABOVE -- install them, then re-run $0"
  exit 1
fi
echo "RESULT: ALL CHECKS PASS (ffmpeg 8.x + loudnorm + signalstats, node 24, npm 10, python 3.12, yt-dlp, Remotion where present, Kokoro models + venvs, disk space)" 
