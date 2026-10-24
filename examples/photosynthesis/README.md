# Example: photosynthesis

A worked example of the plugin on one short, original handout. Everything in `outputs/` was made by the plugin's skills from [`input.md`](input.md).

| Step | Command | Output |
|---|---|---|
| 1. Ingest | `/study:ingest examples/photosynthesis/input.md` | [`outputs/ingest/S1-photosynthesis-handout.md`](outputs/ingest/S1-photosynthesis-handout.md) (anchored source), [`index.json`](outputs/ingest/index.json), [`course.json`](outputs/ingest/course.json) (topic list) |
| 2. Notes | `/study:notes photosynthesis` | [`outputs/notes-photosynthesis.md`](outputs/notes-photosynthesis.md) |
| 3. Quiz | `/study:quiz photosynthesis` | [`outputs/quiz-session.md`](outputs/quiz-session.md) (adaptive loop, two rounds) and [`outputs/quiz-photosynthesis.html`](outputs/quiz-photosynthesis.html) (18-question long quiz; data in [`quiz-photosynthesis.json`](outputs/quiz-photosynthesis.json)) |
| 4. Flashcards | `/study:flashcards photosynthesis` | [`outputs/flashcards/bio-101-photosynthesis.json`](outputs/flashcards/bio-101-photosynthesis.json) (deck), [`.html`](outputs/flashcards/bio-101-photosynthesis.html) (study app with FSRS), [`-basic.csv`](outputs/flashcards/bio-101-photosynthesis-basic.csv) and [`-cloze.csv`](outputs/flashcards/bio-101-photosynthesis-cloze.csv) (Anki) |

Open the `.html` files in any browser; they're single self-contained files that work offline (math renders when online).

In real use these files live in your course folder (`study/bio-101/sources/`, `notes/`, `quizzes/`, `decks/`); they're flattened here so the example is easy to browse.

The handout's paragraph 10 is marked "for interest only (not examined)", so the notes put it under *Side remarks*; paragraph 11 is a lecturer's exam tip, which became the notes' comparison table and the first likely exam question.
