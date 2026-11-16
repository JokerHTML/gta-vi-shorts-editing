# Thumbnail Method

When to load: load this file when you need the thumbnail prompts, the
Joker 9:16 adaptation, the level bar, or the logo rule (Step 1
thumbnail brief, Step 12 thumbnail view, Step 14 upload). The SKILL.md
body states only that the thumbnail must pass M27 and the word-scan
gate; the method lives here.

## Thumbnail method

### The 7 God of Prompt prompts (summarised)

Source: a transcription of @godofprompt's Instagram carousel, saved Nov 8, 2026, judged authentic and usable. Two honest notes: the "$500 designer" framing and income math in Prompt 7 are the creator's sales pitch, unverified, never quoted as fact; Prompt 7 is a sales DM template, NOT a thumbnail prompt, saved for the services and client lane only, never for thumbnail generation.

1. **STEAL THE PATTERN (research):** screenshot the top videos in the niche; Gemini reads them like a designer: what winning thumbnails have in common (faces, colors, number of words, where the text sits); 5 rules, one line each, plus one thing everyone does that you should do differently to stand out.
2. **PICK THE IDEA FIRST:** give the video title plus what happens in it; Gemini returns 3 thumbnail ideas, each with the one feeling it shows (shock, curiosity, hunger), what is in the picture, and text of 4 words or less that ADDS to the title instead of repeating it; then which one it would click and why.
3. **MAKE IT WITH YOUR FACE (generate):** make a YouTube thumbnail in 16:9 from idea [number], using the uploaded photo: keep the face exactly as it is, [shocked face, mouth open], [the object] on the right, a bold [yellow] background, huge white text with a thick black outline: "[your text]". High contrast, easy to read at the size of a stamp.
4. **FIX THE TEXT (edit):** make the text bigger and bolder, 2 lines at most, move it so it does not cover the face; check every word is spelled right; keep everything else exactly the same.
5. **MAKE 3 TO TEST:** make 2 more versions to test against it: one with a different face expression, one with a different background color; keep the text, face, and layout the same. YouTube Studio's Test and Compare runs up to 3 thumbnails on one video and keeps the winner.
6. **CHECK IT NEXT TO THE OTHERS (phone check):** upload a screenshot of the thumbnail next to the videos it will show up beside; on a phone, which one gets clicked first and why; give the one change that would make yours win, then make that change.
7. **SELL IT TO CREATORS (sales DM, NOT a thumbnail prompt):** short DM to [creator name] with [number] subscribers and thumbnails that look [plain / hard to read]; offer a free redo of their latest one, $50/thumbnail with 3 versions to test, or $400/month for up to 10; friendly, under 70 words, no pressure. Services and client lane only.

### Joker adaptation (9:16, official frame, real logo)

1. **16:9 becomes 9:16.** Every Joker thumbnail is a Shorts cover: exactly 1080x1920 (9:16). Always change the ratio in the prompt to 9:16 before sending.
2. **Face becomes official frame.** Prompt 3's "photo of me" does NOT apply to Joker: no faces, no face photo on file. Use the supplied official Rockstar frame as the base instead.
3. **Text is verbatim from the brief, never from the prompt.** The brief's exact text line replaces "[your text]". Every word on the cover must already be written verbatim in the prompt.
4. **M27 safe margins always apply.** All text well inside the frame, verified by viewing the actual thumbnail at full size. Prompt 4's fix-text step is the regen trigger: any spelling error, extra text, or edge-touching text means regenerate, never ship.
5. **PRO model only:** Gemini 3.1 Pro / Nano Banana Pro. Never Flash.
6. **Prompt 1 (pattern) is a research step**, run before a new thumbnail style. Prompt 2 (idea) is how to pick between 3 cover concepts when the brief offers a choice.
7. **Prompt 5 (3 versions)** applies only when the owner orders a Test and Compare run. Default is ONE cover per video, verified. Prompt 6 (phone check) is the full-size view plus margin measurement before upload.
8. **Prompt 7** is services-lane only, never in a thumbnail task.
9. **Never copy the creator's example thumbnails, text, or claims.** Use the prompt structures; the words, frames, and numbers are always ours.

### Level bar and logo rule (binding on every thumbnail)

Real GTA VI logo big at top plus short 1-3 word hook plus one strong focal image plus high contrast. Gemini NEVER draws the logo: it garbles it. The real logo must be composited separately (PIL or Remotion composite) from the authentic logo file — source: Rockstar's official downloads hub (`rockstargames.com/VI/downloads`, Artwork & Wallpapers, with-logo variants) or frame-extraction from the official cover-art reveal, hash-verified — and its hash is verified against the source (gradient logo sha256 starting `18ad6092`, md5 starting `116fe9fe`). **Text-size rule:** at 150px Anton, max ~18 characters per line inside the 130px side margins (V2's two-line 150px hook is the measured case); at 168px, max ~16 characters per line. Longer hook: shrink to 150px or split to two lines — never cross the safe zone. **Logo top margin:** ≥150px from the top edge (the template places it at 150px; V2's ~30px margin was docked MINOR-6). Primary route: Gemini Nano Banana Pro (God of Prompt Prompt 3 adapted plus Prompt 4 fix-text pass, 9:16 1080x1920, verbatim cover text, M27 margins). The builder ALSO delivers a Remotion or PIL composite fallback meeting the same level bar, so the video is never blocked on the thumbnail. Word-scan gate before delivery: every word on the cover checked against the brief's verbatim text; any spelling error, extra text, or edge-touching text means regenerate. Thumbnail brief fields: cover text verbatim, base frame plus backup frame (official Rockstar assets), 1080x1920 9:16, headline in a clean upper portion away from faces, generous clearly-visible safe margins on all four edges, no text touching, crossing, or approaching frame boundaries, verify the actual full-resolution thumbnail at 1080x1920 before delivery. Layout note: the hook may sit in the lower portion when the logo large at top forces it down; if the layout is clean and the hook is fully legible, that is resolved sensibly, not a defect.
