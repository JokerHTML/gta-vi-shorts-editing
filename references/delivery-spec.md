# Delivery spec & ingest checklist

## Delivery spec (the delivered file)

| Field | Value |
|---|---|
| Container | MP4 (faststart) |
| Resolution / fps | 1080×1920, 30fps |
| Video codec | libx264, CRF 18, preset slow, yuv420p |
| Colour | tv range, bt709 space + transfer + primaries (all four fields, ffprobe-verified) |
| Audio codec | AAC 192k, stereo |
| Loudness | −16 to −14 LUFS, true peak ≤ −1.0 dBTP, measured on the delivered file |
| Duration | 30–59 seconds |
| Captions | Burned-in karaoke captions (Remotion route) or ASS fallback + `.srt` uploaded to Studio |

Export rule: never re-upload from a social app. Export once from the pipeline above;
a re-upload from Instagram/TikTok/YouTube re-compresses the file and breaks the gates.

## Ingest checklist (before a build starts)

- [ ] Source material is official only (Rockstar Newswire / official download pages /
      official Rockstar Games YouTube channel). No leak pages, no fan re-uploads.
- [ ] 3-2-1 backup: the raw render, the fixed file, and the delivered file each exist in
      3 copies, on 2 different media, with 1 copy off the build machine.
- [ ] Folder template per video: `work/<slug>/` with `vo/`, `clips/`, `cards/`,
      `renders/` (raw, fixed, delivered), `reports/` (pool gate, build report, QC
      report, red-team verdict), `seo/` (title, description, tags, thumbnail brief).
- [ ] Topic log row written (`TOPIC-LOG.md`); allocation checked (`RUN-ALLOCATION.md`
      on multi-video runs); blocklist checked (M23).
- [ ] `setup-check.sh` passes on the build machine.

## Picture lock & version naming

**Picture lock** is the point after which no visual changes are made: it is declared
in the build report once builder QC passes on the delivered file. After picture lock,
only audio-only fixes (gain/limiter, the V3-style loudnorm retarget) are allowed
without a new version; any visual change re-opens the version.

Version naming: `<topic>_v01_review` (first render for review), `<topic>_v02_revision`
(each fix round), `<topic>_v03_final` (the shipped file). Append the date:
`<topic>_v03_final_2026-11-15.mp4`. Never overwrite a version file; a new version is
a new file, and the red-team verdict names the exact file it scored.
