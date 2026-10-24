#!/usr/bin/env python3
"""Export a Studying with Claude deck (JSON) to Anki-importable CSV files.

Writes up to two files, because Anki imports one note type per file:
  <deck-id>-basic.csv   note type "Basic":  Front, Back
  <deck-id>-cloze.csv   note type "Cloze":  Text, Back Extra

Each file starts with Anki's file headers (Anki 2.1.55 or newer), so Anki picks the
separator, note type, deck, tags and GUID column automatically. Re-exporting
after editing the deck and importing again updates the same notes instead of
making duplicates, because every card keeps a stable GUID.

Usage:
  python anki_export.py study/bio-101/decks/bio-101-photosynthesis.json
  python anki_export.py deck.json --out-dir exports --deck-name "Biology 101::Photosynthesis"
  python anki_export.py deck.json --no-header      (plain CSV for older Anki versions)

In Anki: File > Import, pick the CSV, check the note type and deck, then Import.
No extra packages are needed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import io
import json
import re
import sys
from pathlib import Path

CLOZE = re.compile(r"\{\{c\d+::")


def to_anki_html(text: str) -> str:
    """Convert the small Markdown subset used in decks into HTML that Anki renders."""
    text = str(text or "")
    stash: list[str] = []

    def keep(fragment: str) -> str:
        stash.append(fragment)
        return f"\x00{len(stash) - 1}\x00"

    text = re.sub(r"```[\w-]*\n?(.*?)```", lambda m: keep("<pre><code>" + html.escape(m.group(1).rstrip("\n")) + "</code></pre>"),
                  text, flags=re.S)
    # Anki's MathJax uses \( \) and \[ \]; decks use $ and $$.
    text = re.sub(r"\$\$(.+?)\$\$", lambda m: keep(r"\[" + html.escape(m.group(1), quote=False) + r"\]"), text, flags=re.S)
    text = re.sub(r"(?<!\\)\$([^$\n]+?)\$", lambda m: keep(r"\(" + html.escape(m.group(1), quote=False) + r"\)"), text)
    text = re.sub(r"`([^`\n]+)`", lambda m: keep("<code>" + html.escape(m.group(1)) + "</code>"), text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*([^*\n]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(^|[^*])\*([^*\n]+)\*", r"\1<i>\2</i>", text)
    text = text.replace("\n", "<br>")
    return re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)


def tag(value: str) -> str:
    return re.sub(r"\s+", "_", str(value).strip())


def guid(deck_id: str, card_id: str) -> str:
    return "swc-" + hashlib.sha1(f"{deck_id}/{card_id}".encode("utf-8")).hexdigest()[:16]


def with_source(body: str, source: str | None) -> str:
    if not source:
        return body
    note = f'<span style="font-size:0.8em;opacity:0.7">Source: {html.escape(source, quote=False)}</span>'
    return f"{body}<br><br>{note}" if body else note


def write_csv(path: Path, rows: list[list[str]], headers: list[str]) -> None:
    buffer = io.StringIO()
    for line in headers:
        buffer.write(line + "\n")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerows(rows)
    path.write_text(buffer.getvalue(), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Export a deck JSON file to Anki-importable CSV.")
    parser.add_argument("deck", help="Deck JSON file (see the course layout for the format)")
    parser.add_argument("--out-dir", help="Folder for the CSV files. Default: next to the deck")
    parser.add_argument("--deck-name", help='Anki deck name; use "::" for subdecks. Default: course::title')
    parser.add_argument("--no-header", action="store_true", help="Plain CSV without Anki headers (Front, Back, Tags)")
    args = parser.parse_args(argv)

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    path = Path(args.deck)
    try:
        deck = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Deck not found: {path}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"{path} is not valid JSON: {exc}", file=sys.stderr)
        return 1

    deck_id = str(deck.get("id") or path.stem)
    title = str(deck.get("title") or deck_id)
    course = deck.get("course")
    deck_name = args.deck_name or (f"{course}::{title}" if course else title)
    out_dir = Path(args.out_dir) if args.out_dir else path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    basic, cloze, problems = [], [], []
    for index, card in enumerate(deck.get("cards", []), start=1):
        card_id = str(card.get("id") or f"n{index}")
        tags = " ".join(tag(t) for t in [course, card.get("topic"), *card.get("tags", [])] if t)
        kind = card.get("type", "basic")
        if kind == "cloze":
            text = card.get("text", "")
            if not CLOZE.search(text):
                problems.append(f"card {card_id}: cloze card without a {{{{c1::...}}}} deletion, skipped")
                continue
            cloze.append([to_anki_html(text), with_source(to_anki_html(card.get("extra", "")), card.get("source")), tags,
                          guid(deck_id, card_id)])
        else:
            front, back = card.get("front", ""), card.get("back", "")
            if not front.strip() or not back.strip():
                problems.append(f"card {card_id}: missing front or back, skipped")
                continue
            basic.append([to_anki_html(front), with_source(to_anki_html(back), card.get("source")), tags, guid(deck_id, card_id)])

    def headers(notetype: str, fields: str) -> list[str]:
        if args.no_header:
            return []
        return ["#separator:Comma", "#html:true", f"#notetype:{notetype}", f"#deck:{deck_name}",
                f"#columns:{fields},Tags,GUID", "#tags column:3", "#guid column:4"]

    written = []
    for rows, notetype, fields, suffix in ((basic, "Basic", "Front,Back", "basic"), (cloze, "Cloze", "Text,Back Extra", "cloze")):
        if not rows:
            continue
        if args.no_header:
            rows = [row[:3] for row in rows]
        target = out_dir / f"{deck_id}-{suffix}.csv"
        write_csv(target, rows, headers(notetype, fields))
        written.append(f"{target} ({len(rows)} {notetype} notes)")

    for problem in problems:
        print("Warning: " + problem, file=sys.stderr)
    if not written:
        print("No cards to export.", file=sys.stderr)
        return 1
    for line in written:
        print("Wrote " + line)
    print(f'Import each file in Anki with File > Import; notes go to the deck "{deck_name}".')
    return 0


if __name__ == "__main__":
    sys.exit(main())
