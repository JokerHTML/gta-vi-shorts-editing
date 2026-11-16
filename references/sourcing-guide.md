# Sourcing Guide (Steps 0, 7, 9)

Where the material comes from, what "official" means, and what to use
when the trio's own bed is not available. Read this before you cut a
single frame or pick a music bed.

## What "official" means

Official material is material published by Rockstar Games itself, or
by the game's own official channels. Anything else is not official,
however good it looks.

Official sources:

- Rockstar Newswire: rockstargames.com/newswire (trailers, artwork,
  launch information, dates).
- Rockstar's official download and asset pages on rockstargames.com
  (launch gallery stills, artwork packs, the 99-pack still set the
  trio used).
- The official Rockstar Games YouTube channel (Trailer 1, Trailer 2,
  Launch Trailer, Extended Look).
- A press outlet's own published page, ONLY for the facts in the
  ledger (for example IGN reporting on Skinny Louie). A press page is
  a fact source, never a footage source: never cut frames from a press
  outlet's video or screenshot and present them as official.

NOT official, never usable as source material:

- Fan re-uploads of trailers on any platform.
- Leak accounts, leak screenshots, datamined material.
- Screenshots or clips taken from another creator's video.
- AI-generated "GTA VI" images, or any image an image generator drew.
- A real-world photo presented as in-game footage, or vice versa. If
  a real-world photo is needed (V3 had no real Burger Shot photo in
  the official pool), it comes only from a named press source with its
  own ledger row, and it is labelled as a press photo in the video.

## How the trio obtained its material

Stills: the Rockstar launch gallery and the 99-pack still set,
downloaded from Rockstar's own pages. Every still used in the trio is
named by its set and frame in the run's POOL-GATE-RECORD.md (for
example Grassrivers_03, Vice_City_11, Vice_City_09). Keep the same
record: set, frame name, and the full-res M19 screen result.

Motion: Trailer 2 and the Launch Trailer, downloaded from Rockstar's
official YouTube channel. Motion spans are claimed in
`trailer-windows.md` before finalising, one span per video, and cut
only from the MEASURED active picture (M29: Trailer 2 active
y=216..1943; Launch Trailer active y=120..2039). Never cut from the
file's full frame: both trailers carry baked-in letterbox.

Logo: the authentic GTA VI gradient logo, composited with PIL or
Remotion from the logo file. Never let an image generator draw the
logo: it garbles it. **Where the logo comes from:** Rockstar's official
downloads hub — `rockstargames.com/VI/downloads`, Artwork & Wallpapers
section, with-logo variants (use the section's Download All zip). Rockstar
does not redistribute a standalone logo file. **Extraction route (if the
hub file is unavailable):** take a frame from the official cover-art reveal
on Rockstar's channel, crop to the logo only, and hash-verify it. The
verified gradient logo hashes to sha256
starting `18ad6092` and md5 starting `116fe9fe`; verify the hash of
any logo file you use against those prefixes before it goes on a
thumbnail. Never take the logo from fan sites or leak pages.

## The music bed: what the trio used, and what you use instead

The trio's bed is the "6-video-run signature bed": an ORIGINAL
composition by Joker Gaming, C-G-Am-F sine pads, seed 20261031, -27 dB,
48 seconds, 24 kHz. It is Joker's own asset. It is NOT shipped in this
skill or in the Pro Pack, and you may not take it from anywhere else.
Do not ship a video with a bed you do not have rights to.

Use one of these instead. Record the choice, with its licence and
source URL, in the build report (M35 rights check).

1. Recreate the pad bed from the documented recipe. Any synth or DAW
   can make it: C-G-Am-F sine pads, **4 seconds per chord, root-position
   voicing at C4 (C4-G3, G3-D4, A3-E4, F3-C4), 0.3s attack / 0.8s release,
   loop point at the bar line (every 16 seconds), level -27 dBFS RMS**,
   looped to length. A bed you synthesised yourself from this recipe is your own asset,
   with no licence to clear. This is the closest replacement for the
   trio's bed, and the one the skill recommends first. Verify yours by
   measuring: RMS -27 dBFS (±2 dB) on the rendered bed, no clipping.
2. YouTube Audio Library (youtube.com/audiolibrary/music): free
   tracks for YouTube use. Pick an ambient pad, no vocals, loopable
   to 40-60 seconds. Read the track's own licence line before use:
   some tracks need attribution in the description, some do not.
   Record the track name and its licence line. **Attribution placement:**
   if a track requires attribution, it goes on the LAST description line,
   after the countdown line — the one allowed addition to the description
   format. Never put attribution in the script, on a card, or in the title.
3. Pixabay Music (pixabay.com/music): free under the Pixabay Content
   Licence, which allows commercial use without attribution. Pick an
   ambient pad the same way, and record the track page URL.
4. Free Music Archive (freemusicarchive.org): free tracks under
   Creative Commons licences that differ per track. Read the track's
   licence before use: some forbid commercial use, some require
   attribution. Record the licence, not just the track name.

Whichever you pick: duck it to 0.33 under VO and 1.0 in gaps, with
0.1s fades (Step 9), and tile it to length if it is shorter than the
video. Never use a commercial song or original clip audio at any
volume (M35): a low volume does not dodge Content ID, and the fix for
a claim is a clean rebuild without the song plus a re-upload, never a
dispute on audio you have no rights to.

If no bed is available at all, VO-only is allowed ONLY if
silencedetect on the delivered file proves no dead gaps (M4). A bed
mix is the default: V2 chose VO-only and was docked MINOR-1 for the
digital silence in its gaps and tail.
