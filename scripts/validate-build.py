#!/usr/bin/env python3
"""validate-build.py - pre-render validator for the GTA VI Shorts Editing skill.

Checks, before any render:
  1. Word-count gate: a script file's token count AND spoken-word count
     must both sit inside 90-105 (see the word-count convention in SKILL.md).
  2. Banned-list grep (STEM-AWARE, v1.2.0): the script (and optional
     card/caption files) must not contain any banned word or phrase from a
     banned-list file. Matching is by word stem, so inflections are caught:
     a ban on "leak" also catches "leaked", "leaking", "leaks".
  3. Pool arithmetic: need + ceil(10 percent) slack against a verified clean
     pool, from the M20 numbers (see SKILL.md M20).
  4. Caption/card overlap: no caption phrase may overlap a card window
     (data.ts PHRASES vs SEGMENTS, or --phrases/--cards JSON). Fails loudly
     when zero phrases or zero cards are found in --data-ts mode (a vacuous
     pass is a defect, not a pass). Also checks phrase word count (2-4 words).
  5. NOT checked here (manual, per SKILL.md Step 2): title character count,
     tag count/order, description Sources line, countdown (M30), attribution
     roots (M26), qualifier presence (M34). This script checks word count,
     banned grep, pool arithmetic, and caption/card overlap — nothing else.

Pure stdlib. Exit 0 = all checks pass; exit 1 = one or more FAIL.

Usage:
  python3 validate-build.py --script script.txt --banned banned.txt
  python3 validate-build.py --script script.txt --banned banned.txt \
      --words 103 --speech-seconds 35.74 --gaps 8,10,6,12,9,8,10,7 \
      --pool-frames 1500
  python3 validate-build.py --script script.txt --banned banned.txt \
      --data-ts /path/to/data.ts

Word-count convention (verified against the Nov 15 trio scripts):
  TOKENS = whitespace-separated tokens, excluding a standalone em-dash.
  SPOKEN = tokens, with each hyphenated or em-dash-joined compound
  expanded into its spoken parts ("about-thirty-second" = 3 spoken
  words; "region" + "not" joined by an em-dash = 2), "&" spoken as "and" (1 for 1), and
  "Pre-loading" spoken as one word. A standalone em-dash counts 0.
  Trio check: V1 103 tokens / 105 spoken; V2 102 / 104; V3 103 / 105.
  (V3's file states 103 by tool count, dash excluded; its spoken count
  by this convention is 105. Whisper STT heard 103 on the clean VO:
  Whisper tokenisation is a different measurement and is not the gate.)

Tested on this machine against the trio
scripts in free-skill/examples/ (all three PASS), against a banned
script (FAIL, as expected), and against adversarial inputs (v1.2.0: a
script containing "leaked material" now FAILS a ban on "leak"; an empty
data.ts now FAILS instead of passing vacuously). If a check misfires on
your script, read
the printed counts: they name the exact rule that tripped.
"""
import argparse
import json
import math
import re
import sys

FAILURES = []


def check(label, ok, detail):
    print(f"{'PASS' if ok else 'FAIL'}  {label}: {detail}")
    if not ok:
        FAILURES.append(label)


def count_tokens(text):
    """Whitespace tokens, excluding a standalone em-dash."""
    return sum(1 for t in text.split() if t.strip(".,;:!?()\"'") not in ("—", "–", "-"))


def count_spoken(text):
    """Spoken words per the convention in the module docstring."""
    n = 0
    for tok in text.split():
        t = tok.strip(".,;:!?()\"'")
        if t in ("—", "–", "-"):
            continue
        if t == "&":
            n += 1
            continue
        if t.lower() == "pre-loading":
            n += 1
            continue
        parts = [p for p in re.split(r"[-—]", t) if p]
        n += len(parts) if len(parts) > 1 else 1
    return n


def read_script(path):
    text = open(path, encoding="utf-8").read()
    # Scope to the Script section: in free-skill/examples/ files the
    # script is a blockquote under "## Script", and the description is a
    # second blockquote under "## Description". Taking every blockquote
    # line in the file would count the description too.
    m = re.search(r"^## Script.*?\n(.*?)^## ", text, re.M | re.S)
    section = m.group(1) if m else text
    lines = [l[2:] for l in section.splitlines() if l.startswith("> ")]
    if lines:
        return " ".join(lines)
    return section.strip() if m else text.strip()


def main():
    ap = argparse.ArgumentParser(description="Validate a GTA VI Shorts build before render.")
    ap.add_argument("--script", required=True, help="Script text file (bare text, or markdown blockquote form).")
    ap.add_argument("--banned", help="Banned-list file, one banned word or phrase per line (# comments allowed).")
    ap.add_argument("--extra-text", action="append", default=[], help="Extra file to grep for banned words (cards, captions). Repeatable.")
    ap.add_argument("--words", type=int, help="Spoken words in the script (defaults to the spoken count).")
    ap.add_argument("--speech-seconds", type=float, help="Measured VO speech seconds, for the pool check.")
    ap.add_argument("--gaps", help="Comma-separated gap frames, e.g. 8,10,6,12,9,8,10,7.")
    ap.add_argument("--pool-frames", type=int, help="Verified clean pool frames (full-res only).")
    ap.add_argument("--data-ts", help="Remotion data.ts: checks caption phrases against card windows.")
    args = ap.parse_args()

    script = read_script(args.script)
    tokens = count_tokens(script)
    spoken = count_spoken(script)
    check("Word count: tokens in 90-105", 90 <= tokens <= 105, f"{tokens} tokens")
    check("Word count: spoken in 90-105", 90 <= spoken <= 105, f"{spoken} spoken")
    if tokens != spoken:
        print(f"INFO  Tokens {tokens} vs spoken {spoken}: hyphenated compounds expand when spoken.")

    if args.banned:
        banned = [l.strip() for l in open(args.banned, encoding="utf-8")
                  if l.strip() and not l.strip().startswith("#")]
        haystacks = [("script", script)]
        for extra in args.extra_text:
            haystacks.append((extra, open(extra, encoding="utf-8").read()))
        for word in banned:
            for name, hay in haystacks:
                # Stem-aware match (v1.2.0, F11): a ban on "leak" must catch
                # "leaked", "leaking", "leaks". Match the word stem followed
                # by optional word characters, at a word boundary on the left.
                # Multi-word bans match as an exact phrase (case-insensitive).
                if " " in word:
                    hit = re.search(re.escape(word), hay, re.I)
                else:
                    hit = re.search(r"\b" + re.escape(word) + r"\w*", hay, re.I)
                check(f"Banned word absent: '{word}' ({name})", not hit,
                      "absent" if not hit else f"FOUND in {name}")

    if args.pool_frames is not None:
        words = args.words if args.words is not None else spoken
        if args.speech_seconds is not None:
            speech_frames = int(round(args.speech_seconds * 30))
        else:
            speech_frames = int(math.ceil(words / 2.5 * 30))
        gap_frames = sum(int(g) for g in args.gaps.split(",")) if args.gaps else 0
        need = speech_frames + gap_frames + 2
        slack = int(math.ceil(need * 0.10))
        check("M20 pool gate: pool >= need + 10% slack",
              args.pool_frames >= need + slack,
              f"need {need}f + slack {slack}f = {need + slack}f vs pool {args.pool_frames}f")
        print(f"INFO  Speech {speech_frames}f + gaps {gap_frames}f + tail 2f = need {need}f.")

    if args.data_ts:
        src = open(args.data_ts, encoding="utf-8").read()
        phrases = re.findall(
            r"\{\s*text:\s*'([^']*)'.*?start:\s*([\d.]+),\s*end:\s*([\d.]+)\s*\}",
            src, re.S)
        cards = re.findall(
            r"\{\s*kind:\s*'card',.*?startFrame:\s*(\d+),\s*endFrame:\s*(\d+)\s*\}",
            src, re.S)
        # Fail loudly on zero phrases or zero cards (v1.2.0, F11): an empty
        # file used to return ALL CHECKS PASS with nothing checked.
        check("data.ts: at least one caption phrase found", len(phrases) > 0,
              f"{len(phrases)} phrases" if phrases else "ZERO phrases found — check the data.ts format")
        check("data.ts: at least one card window found", len(cards) > 0,
              f"{len(cards)} cards" if cards else "ZERO cards found — check the data.ts format")
        card_windows = [(int(s) / 30.0, int(e) / 30.0) for s, e in cards]
        for text, start, end in phrases:
            start, end = float(start), float(end)
            overlap = [w for w in card_windows if start < w[1] and end > w[0]]
            check(f"Caption '{text[:30]}...' clear of card windows",
                  not overlap, f"{start}-{end}s" + (f" OVERLAPS card {overlap}" if overlap else ""))
            lone = text.strip().lower() in ("the", "a", "no")
            check(f"Caption '{text[:30]}...' is not a lone function word", not lone,
                  "ok" if not lone else "LONE FUNCTION WORD")
            # Phrase word-count check (v1.2.0, F35): phrases are 2-4 words.
            nwords = len(text.split())
            check(f"Caption '{text[:30]}...' is 2-4 words", 2 <= nwords <= 4,
                  f"{nwords} words")
            # Repeated-keyword flag (F19): a keyword occurring twice in one
            # phrase used to silently drop text in Captions.tsx.
            kw = re.search(r"keyword:\s*'([^']+)'", src[src.find(text):src.find(text) + 400] if text in src else "")
            if kw and text.lower().count(kw.group(1).lower()) > 1:
                check(f"Caption '{text[:30]}...' keyword occurs once", False,
                      f"keyword '{kw.group(1)}' occurs {text.lower().count(kw.group(1).lower())}x — prefer one occurrence per phrase")

    print()
    if FAILURES:
        print(f"RESULT: {len(FAILURES)} FAILING CHECK(S): {', '.join(FAILURES)}")
        return 1
    print("RESULT: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
