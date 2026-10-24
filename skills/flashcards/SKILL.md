---
name: flashcards
description: Make concise flashcards from the student's notes or materials (one fact per card, cloze deletions for definitions), save them as a deck, and give the student a self-contained HTML flip-card app with FSRS spaced repetition plus Anki-importable CSV export. Use when the student asks for flashcards, cards, a deck, spaced repetition, Anki, or something to memorize terms, definitions, formulas, dates or vocabulary. For question-and-answer practice with feedback use quiz instead.
---

# Flashcards and spaced repetition

Good cards are small, precise and testable. A deck of 30 sharp cards beats 150 vague ones.

## Writing cards

Build from the student's notes or sources for the requested topic. Read the error log (`study/<course>/errors.jsonl`) too: open mistakes make excellent cards.

- **One fact per card.** If the back needs "and", split the card.
- **Cloze deletions for definitions and key sentences:** `A {{c1::producer}} makes its own food from inorganic molecules.` Delete the key term, not filler. Add a hint when the blank is ambiguous: `{{c1::stroma::location}}`. Use separate cloze numbers (`c1`, `c2`) only when each blank is worth its own review.
- **Basic cards for questions:** "Why ...?", "What happens when ...?", "Compare X and Y in one difference."
- **Standalone context.** A card must make sense in a shuffled deck months from now: name the topic in the question ("In photosynthesis, ..."), never "this process" or "the above".
- **No lists longer than three items** on one card; turn longer lists into several cards or a mnemonic.
- **No yes/no questions** and no answers that can be guessed from the question's wording.
- **Formulas:** LaTeX with `$...$`; ask for the formula from its meaning, and the meaning from the formula, as two cards.
- **Vocabulary for language courses:** both directions as two cards.
- **Every card cites its source** (`[S1 p.3]`) and carries a `topic` from `course.json`.
- **Size:** about 15–40 cards per topic. Before adding to an existing deck, check for duplicates.

Show the student the cards as a compact table (front | back | source) and fix any they flag before saving.

## Saving the deck

Save the deck JSON to `study/<course>/decks/<deck-id>.json` (deck ID: `<course>-<topic>`, for example `bio-101-photosynthesis`):

```json
{
  "id": "bio-101-photosynthesis",
  "title": "Photosynthesis",
  "course": "bio-101",
  "created": "2026-10-23",
  "cards": [
    { "id": "c1", "type": "basic", "front": "In photosynthesis, where do the light-dependent reactions occur?", "back": "In the **thylakoid membranes**.", "topic": "light-reactions", "source": "[S1 ¶4]", "tags": [] },
    { "id": "c2", "type": "cloze", "text": "The {{c1::Calvin cycle}} fixes carbon dioxide in the {{c2::stroma}}.", "extra": "Also called the light-independent reactions.", "topic": "calvin-cycle", "source": "[S1 ¶6]", "tags": [] }
  ]
}
```

Card IDs must stay stable when you edit a deck (they key the student's review progress and Anki's update-on-reimport). New cards get new IDs; never renumber.

## Study app (HTML)

1. Read `${CLAUDE_SKILL_DIR}/assets/flashcards.html`.
2. Replace only the JSON inside `<script type="application/json" id="deck-data">` with the deck. Keep it valid JSON: escape backslashes (`"\\frac"`), write `<\/` for any `</`, and don't use `$` for money.
3. Save as `study/<course>/decks/<deck-id>.html` and tell the student to open it in a browser, on a computer or phone.

What it does: flip cards (tap or Space), rate Again / Hard / Good / Easy (keys 1–4), and schedules each card with **FSRS** (the open-source Free Spaced Repetition Scheduler, default parameters, 90% target recall, adjustable). Cram mode, a searchable card list and a progress page are included. Progress is saved in the browser; if storage is blocked it keeps working and says so. **Export progress** moves it to another device, and **Copy summary for Claude** gives you recall by topic and the cards they keep forgetting, which you can use to update weak spots or rewrite bad cards.

## Anki export

```bash
python "${CLAUDE_SKILL_DIR}/scripts/anki_export.py" "study/<course>/decks/<deck-id>.json"
```

- Use `python3` on macOS and Linux if `python` isn't found. No packages needed.
- Writes `<deck-id>-basic.csv` and `<deck-id>-cloze.csv` next to the deck, with Anki headers (note type, deck, tags, stable GUIDs). In Anki 2.1.55 or newer: **File → Import**, choose each file, check the note type and deck, then **Import**. Re-importing after edits updates the same notes.
- `--deck-name "Biology 101::Photosynthesis"` sets the Anki deck; `--no-header` writes plain CSV for older Anki versions.

Without file access, show the cards as a table and offer the JSON, HTML and CSV as files.

## Quality rules

- **Accuracy over speed.** Every card must be correct according to the student's sources. Never invent facts; if a source is unclear, leave the card out and say why.
- **Cite every card**; mark anything from general knowledge as such in `extra` or the back.
- **Active recall.** Cards test retrieval: the front asks, the back answers. Never put the answer on the front.
- **Academic integrity.** Cards are for learning. Don't make cards meant to be used during an exam.
- **Study Mode.** If Study Mode is on, offer to run the first few cards inline with the student before handing over the app.
