# Voice profile (Step 4)

Channel voice defaults, persisted so the first run on a new channel is not a guess.
Fill this in once per channel, then load it before the first VO of every video.

## Joker Gaming (GTA VI news Shorts)

| Field | Value |
|---|---|
| Engine | Kokoro (kokoro-onnx 0.6.1) |
| Voice | `am_adam` |
| Speed | 1.1 (locked) |
| Trim | −40 dBFS |
| Sample rate | 24 kHz |
| Stems | One per script sentence |
| Planning pace | 2.5 words/sec (slowest measured: V1 2.94, V2 2.50, V3 2.66) |
| Known bypasses | "Kaseya" → spoken "Kuh-say-uh" (7 spellings tested); on-screen text stays "Kaseya" |
| Fallback TTS | Piper `en_US-lessac-medium` — if Kokoro fails (model issue, espeak quirk, voice unsuited to a topic). A different voice re-verifies the pace/word-count math, which was measured on `am_adam` at 1.1. Never swap voices mid-video. |

## First-run profile (new channel)

On a new channel, run one test sentence through the full chain (synthesis → STT →
listen) before the first real VO, and record: the voice, the speed, the measured
words/sec on that channel's scripts, and any bypasses found. That record is this
file's next row. A channel with no recorded profile has no locked voice: do not
assume `am_adam` at 1.1 fits a different channel's tone.
