---
name: weak-spots
description: Show the student where they are weakest, with quiz accuracy per topic, open mistakes, time since practice and upcoming exams, in a self-contained HTML dashboard plus a short text summary that recommends what to study next and the command to run. Use when the student asks what to study next, where they're weak, how they're doing, for their progress or stats, or for a dashboard of their quiz results.
---

# Weak spots

Turn the student's logged answers into a clear picture of what's solid, what's shaky, and what to do next.

## Data

From the active course (`study/courses.json`):

- `study/<course>/course.json`: `topics` (with `weight` when known) and `exams`
- `study/<course>/quizzes/history.jsonl`: one answered question per line (`ts`, `topic`, `correct` as `true`, `false` or `"partial"`)
- `study/<course>/errors.jsonl`: the error log; open entries have `"resolved": false`
- Optional: a flashcard summary the student pasted from the flashcard app (recall by topic, cards they keep forgetting)

If there's no history yet, say so plainly and offer a short diagnostic quiz across all topics (`/study:quiz`) instead of an empty dashboard.

## How topics are ranked

The dashboard computes this itself; use the same logic in your text summary so they agree:

- **Accuracy** per topic, with partly-right answers counting half. Status: **weak** under 70%; with 3 or more answers, **okay** 70–84% and **strong** 85% or more; **too few answers** for 70% or more on fewer than 3 answers (not enough to call it mastered); **no data** with no answers.
- **Priority** combines weakness (accuracy smoothed so one lucky answer doesn't count as mastery), open mistakes, days since last practice (two weeks or more counts fully), and exam weight. A topic with demonstrated weakness and open mistakes outranks one that hasn't been quizzed yet; never-quizzed topics come next.
- **Trend** compares the older and newer halves of a topic's answers (needs 6 or more): improving, steady or slipping.
- **Suggested action:** 2+ open mistakes → `/study:review-mistakes <topic>`; fewer than 3 answers → `/study:quiz <topic>`; under 60% → `/study:explain-like <topic>` then a quiz; not practiced for a week → `/study:flashcards <topic>`; otherwise a harder quiz.

## Build the dashboard

1. Read `${CLAUDE_SKILL_DIR}/assets/dashboard.html`.
2. Replace only the JSON inside `<script type="application/json" id="progress-data">` with:
   ```json
   {
     "course": "Biology 101",
     "generated": "2026-10-23",
     "exams": [ { "name": "Midterm", "date": "2026-11-14" } ],
     "topics": [ { "id": "light-reactions", "name": "Light-dependent reactions", "weight": 0.35 } ],
     "history": [ { "ts": "2026-10-21T16:30:00", "topic": "light-reactions", "correct": true } ],
     "errors": [ { "topic": "calvin-cycle", "question": "...", "why_wrong": "...", "times_missed": 2, "resolved": false } ]
   }
   ```
   Copy the history lines as they are (only `ts`, `topic` and `correct` are needed). Include only open errors. Keep it valid JSON and write `<\/` for any `</`.
3. Save as `study/<course>/weak-spots.html` (overwrite the previous one) and tell the student to open it. It has light and dark mode, works on a phone, and filters by all time, 30 days or 7 days.

## Text summary (always give this too)

Three to six lines in the chat:

- overall accuracy and the number of answers it's based on
- the top three topics to study next, each with its reason ("58% over 12 answers, 3 open mistakes") and the command to run
- one encouraging, specific observation (a topic that improved, a mistake that got resolved)
- days to the next exam, and whether the exam plan needs adjusting

## Quality rules

- **Accuracy over speed.** Report only what the data shows. With fewer than about 5 answers on a topic, say the estimate is rough. Never invent progress.
- **Honest, kind framing.** Weak topics are the most useful thing to know before an exam; say so without sugar-coating or discouraging.
- **Active recall.** Every recommendation is an action that involves retrieval (quiz, review mistakes, flashcards, explaining), not rereading.
- **Academic integrity.** This dashboard tracks practice; it's not for completing graded work.
- **Study Mode.** If Study Mode is on, end with one question: which of the top three they want to start with.
