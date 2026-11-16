# M-rules: Audio, mix & rights

Part of the GTA VI Shorts Editing Skill v1.2.0. Load when: Load when mixing, choosing a bed, or checking audio rights.

M-numbers are stable and never renumbered. The full rule text lives here; SKILL.md carries only the gates summary and the reference index.

## Contents

- [M4](#m4)
- [M35](#m35)
- [M38](#m38)

## <a id="m4"></a>**M4 Bed audible in every gap, never silence.**

Bed audible in every gap, never silence (silencedetect NONE). A bed mix is the default. VO-only is allowed ONLY if silencedetect on the delivered file proves no dead gaps (0 hits, noise -40dB, d=0.5). V2 chose VO-only and was still docked MINOR-1 for digital silence in its gaps and tail: allowed is not the same as clean.

## <a id="m35"></a>**M35 NO COMMERCIAL SONG OR ORIGINAL CLIP AUDIO IN A JOKER SHORT: VO-ONLY OR ROYALTY-FREE.**

Never keep a source clip's commercial song or original audio under the VO at any volume: a low volume does NOT dodge Content ID. The mix is VO-only, or VO plus royalty-free music (for example Flow music, as the Nov 13 trio used). The build checks audio RIGHTS, not just audio levels: loudnorm, STT, and every existing gate measure the mix; none of them checks whether the audio is licensed, so the rights check is a named step at assembly (source audio stripped; every music element named with its licence or source) AND at upload (Studio's copyright check must read clean before the video is left live; a claim means a clean rebuild without the song plus re-upload, never a dispute on audio we have no rights to).

## <a id="m38"></a>**M38 ONE BED, DUCKED ONCE; VO JOINS BY CONCAT AT 48 KHZ; DELIVERED AUDIO 48 KHZ; CLIP AUDIO MUTED.**

The mix is VO plus ONE bed, never re-cut mid-track: static -18 dB, duck 12 dB / threshold -30 / attack 20 ms / release 400 ms, fade in 1.5 s, fade out 3 s, looped; if no suitable bed file exists, VO-only — never synthesise a chopped sine-pad. VO joins: per segment highpass f=20, afade in/out 0.04 s, resample to 48 kHz, loudness-match segments, join with the concat filter (NOT acrossfade — it shortens the total and drifts caption sync), then ONE loudnorm pass (I=-15.5, TP=-2.0, LRA=11); no dead gaps. The delivered file's audio MUST be 48 kHz: ffmpeg's loudnorm upsamples to 96 kHz by default, so the bed mix (or final export) resamples to 48 kHz. Remotion's OffthreadVideo includes the source clip's audio by default — `muted` is required, or the trailer's music/dialogue bleeds under the VO (a Content ID risk, cf. M35); after any Remotion source edit, re-render with --bundle-cache=false, or verify the output audio — a stale webpack bundle silently renders the old code.
