# Course folder layout and file formats

Every Studying with Claude skill reads and writes the same files, so a quiz can find the notes, the dashboard can find the quiz history, and the error log feeds `review-mistakes`. All paths are relative to the student's working folder.

```
study/
├── courses.json                 registry of courses + which one is active
└── <course-slug>/               one folder per subject, e.g. bio-101
    ├── course.json              name, level, exams, topic list
    ├── sources/
    │   ├── index.json           one entry per source (S1, S2, ...)
    │   └── S<n>-<slug>.md       extracted text with location anchors
    ├── notes/<topic-slug>.md    rich notes (notes skill)
    ├── decks/<deck-id>.json     flashcard decks (+ .html, -basic.csv, -cloze.csv)
    ├── quizzes/
    │   ├── history.jsonl        one line per answered question
    │   └── <quiz-id>.html       long quizzes (quiz template)
    ├── mock-exams/<id>.html     timed mock exams (+ <id>-results.json)
    ├── errors.jsonl             error log: every wrong answer and why
    ├── plans/exam-plan-<exam-slug>.md
    ├── podcasts/<topic-slug>.md
    └── cheatsheet.md
```

Slugs are lowercase ASCII words joined by hyphens (`cell-respiration`). Dates are ISO 8601 (`2026-11-14`, or `2026-11-14T15:04:00` for timestamps, local time). JSON files are UTF-8 and pretty-printed with 2 spaces; `.jsonl` files hold one compact JSON object per line and are only ever appended to or rewritten whole.

## courses.json

```json
{
  "active": "bio-101",
  "courses": [
    { "slug": "bio-101", "name": "Biology 101", "created": "2026-10-23" }
  ]
}
```

## course.json

```json
{
  "slug": "bio-101",
  "name": "Biology 101",
  "level": "university, year 1",
  "language": "en",
  "guide": null,
  "exams": [
    {
      "slug": "midterm",
      "name": "Midterm",
      "date": "2026-11-14",
      "format": "40 multiple choice + 3 short answer, 90 minutes",
      "topics": ["photosynthesis", "cell-respiration"]
    }
  ],
  "topics": [
    {
      "id": "photosynthesis",
      "name": "Photosynthesis",
      "parent": null,
      "sources": ["S1 ¶1-¶9"],
      "weight": null
    },
    {
      "id": "light-reactions",
      "name": "Light-dependent reactions",
      "parent": "photosynthesis",
      "sources": ["S1 ¶3-¶5"],
      "weight": null
    }
  ]
}
```

- `guide`: file name of an exam guide from the `exam-guides` skill (for example `ap-biology.md`) when the course follows a standard exam, else `null`.
- `topics[].weight`: share of the exam (0–1) when known from a syllabus or guide, else `null`.
- `topics[].sources`: the anchors where the topic is taught. Keep the list short; it is a pointer, not an index.

## sources/index.json

```json
{
  "sources": [
    {
      "id": "S1",
      "title": "Photosynthesis lecture handout",
      "file": "sources/S1-photosynthesis-handout.md",
      "original": "C:/Users/me/Downloads/week5-handout.pdf",
      "type": "pdf",
      "kind": "lecture",
      "added": "2026-10-23",
      "notes": "Pages 4-5 are scanned; transcribed from the page images."
    }
  ]
}
```

- `type`: `pdf`, `docx`, `pptx`, `image`, `web`, `youtube`, `audio`, `video`, `text`.
- `kind`: `lecture`, `textbook`, `slides`, `handout`, `own-notes`, `past-paper`, `syllabus`, `transcript`, `web`, `other`.
- Source IDs are never reused, even if a source is deleted.

## Citation anchors

Every extracted source file marks locations, and every fact Claude writes cites one:

| Source type | Anchor in the source file | Citation in notes, quizzes and cards |
|---|---|---|
| PDF | `## [p.3]` heading per page | `[S1 p.3]` |
| Slides | `## [slide 5] Title` heading per slide | `[S2 slide 5]` |
| Word, text, web | `[¶12]` before each paragraph, `## [§3] Heading` for headings | `[S3 ¶12]` or `[S3 §3]` |
| Audio, video, YouTube | `[00:12:34]` before each transcript paragraph | `[S4 12:34]` |
| Image of notes | `## [img 1]` per image, `[line 4]` where useful | `[S5 img 1]` |

Ranges are fine: `[S1 p.3-4]`, `[S3 ¶4-¶6]`. Anything that isn't in the student's sources is written as *(general knowledge, not in your materials)*.

## quizzes/history.jsonl

One line per answered question, from any skill that asks questions (quiz, mock-exam, review-mistakes, feynman checks):

```json
{"ts":"2026-10-23T15:04:00","quiz":"q-20261023-1","mode":"quiz","round":1,"topic":"light-reactions","type":"mcq","difficulty":2,"correct":true,"source":"[S1 ¶4]"}
```

- `mode`: `quiz`, `mock-exam`, `review-mistakes`, `feynman`.
- `type`: `mcq`, `fill`, `tf`, `short`, `significance`.
- `difficulty`: 1 recall, 2 understand, 3 apply, 4 analyze/evaluate.
- `correct`: `true`, `false`, or `"partial"` for open-ended answers given partial credit.

## errors.jsonl

One line per mistake. `review-mistakes` rewrites this file when it updates entries.

```json
{"id":"e-20261023-001","ts":"2026-10-23T15:04:00","topic":"calvin-cycle","type":"mcq","question":"Which molecule supplies the electrons that reduce 3-PGA in the Calvin cycle?","student_answer":"ATP","correct_answer":"NADPH","why_wrong":"Mixed up the roles of ATP (energy) and NADPH (electrons) in the Calvin cycle.","source":"[S1 ¶7]","times_missed":1,"streak":0,"resolved":false,"resolved_ts":null}
```

- `why_wrong` describes the misconception in one sentence, not just "wrong answer".
- `streak` counts correct answers on new questions about the same mistake since the last miss. An entry is `resolved` when `streak` reaches 2 and the two correct answers were in different sessions.

## decks/<deck-id>.json

```json
{
  "id": "bio-101-photosynthesis",
  "title": "Photosynthesis",
  "course": "bio-101",
  "created": "2026-10-23",
  "cards": [
    { "id": "c1", "type": "basic", "front": "Where in the chloroplast do the light-dependent reactions happen?", "back": "In the thylakoid membranes.", "topic": "light-reactions", "source": "[S1 ¶4]", "tags": ["photosynthesis"] },
    { "id": "c2", "type": "cloze", "text": "The {{c1::Calvin cycle}} fixes carbon dioxide in the {{c2::stroma}}.", "extra": "Also called the light-independent reactions.", "topic": "calvin-cycle", "source": "[S1 ¶6]", "tags": [] }
  ]
}
```

Cloze syntax is Anki's: `{{c1::answer}}` or `{{c1::answer::hint}}`. Each distinct cloze number becomes its own card.
