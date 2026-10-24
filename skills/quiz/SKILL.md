---
name: quiz
description: Run an adaptive practice quiz on the student's course material with multiple choice, fill-in-the-blank, true/false, short answer and explain-the-significance questions. Each answer gets an explanation and source citation, difficulty rises on topics the student gets right, missed topics get new questions until they're mastered, and every wrong answer goes into the error log. Use when the student asks to be quizzed or tested, wants practice questions, or says "test me" on a topic, notes or source. For a timed full-length exam use mock-exam; to practice only past mistakes use review-mistakes.
---

# Adaptive quizzes

A quiz is for **learning**, not just scoring: every answer gets feedback, and the quiz keeps adapting until the missed ideas are actually mastered.

## Set up (one short message, only what you don't know)

- **Scope:** topics, a source, notes, or "everything so far". Default: the topics the student just studied, else the course topic list.
- **Length:** default rounds of 5 questions. More than 15 questions in one go, or "give me a full quiz", means using the HTML template (below).
- Start at **difficulty 2** unless the quiz history says otherwise. Read `study/<course>/quizzes/history.jsonl` and `errors.jsonl` first if they exist, so you don't re-ask what's mastered and you do revisit open mistakes.

## Question types

Mix them in every round (at least three types per round of five):

| Type | `type` | Good for | Rules |
|---|---|---|---|
| Multiple choice | `mcq` | Concepts, distinctions | 4 options, one correct. Distractors are real misconceptions, similar in length and style, never "all of the above" jokes |
| Fill in the blank | `fill` | Key terms, values | One blank, an unambiguous answer, list accepted variants |
| True/false | `tf` | Common misconceptions | Make the false ones plausible; avoid trick wording and double negatives |
| Short answer | `short` | Explaining mechanisms, applying ideas | 1–4 sentence answer, with a model answer and 2–4 key points |
| Explain the significance | `significance` | Why something matters, connections | Model answer covers role + wider importance |

**Difficulty levels:** 1 recall a fact or term · 2 explain or classify · 3 apply to a new example or calculate · 4 analyze, compare or evaluate. Questions must be answerable from the student's materials; cite where.

## The adaptive loop

1. **Ask round 1** (5 questions across the scope, difficulty 2). Inline, ask **one question at a time** and wait for the answer. If the student asks for the whole round at once, give it as a numbered list and grade it together.
2. **Give feedback after every answer:**
   - Correct: confirm in a few words and say *why* it's right.
   - Wrong: say so honestly, give the correct answer and an explanation that targets the misconception (not just the fact). Cite the source: `Source: [S1 p.4]`.
   - Open answers: grade against the key points: right, partly right (say which key point is missing) or wrong.
3. **Log every answer** (see Files) and add each wrong or partly-right answer to the error log, with **why** it was wrong. If the reason isn't obvious, ask briefly ("What made you pick B?") before logging.
4. **Plan the next round per topic:**
   - Topic answered correctly → next question on it is **one level harder** (max 4), and in a different format.
   - Topic missed → a **new** question on the same idea (new wording, new example or angle; never the same question again), at the same level or one lower.
   - After 2 misses on the same idea, stop quizzing it: teach it briefly with the hint ladder (nudge, then specific hint, then worked similar example), then ask a fresh question.
5. **Repeat** until every missed idea has been answered correctly at least once and each topic has had a step up in difficulty, or the student stops.
6. **Wrap up:** score per round, topics now solid, topics to revisit, entries added to the error log, and a next step (flashcards for shaky facts, `/study:review-mistakes` later, `/study:weak-spots` for the big picture).

## Long quizzes: HTML template

For more than 15 questions, or when the student wants to take the quiz on their phone or away from the chat, fill the template:

1. Read `${CLAUDE_SKILL_DIR}/assets/quiz.html`.
2. Replace only the JSON inside `<script type="application/json" id="quiz-data">` with the quiz. Keep it valid JSON: escape backslashes (`"\\frac{1}{2}"`), write `<\/` for any `</` inside strings, and don't use `$` for money (it is read as math).
3. Save as `study/<course>/quizzes/<quiz-id>.html` and tell the student to open it in a browser. It works offline; math renders when online.
4. The student taps **Copy results for Claude** at the end and pastes them back. Log every answer from the pasted JSON as a history line (use `correct`, which is the first try, and the results' `finished` time as `ts`), add the misses to the error log (ask briefly why they chose what they did if it isn't clear), then run the adaptive loop's next round on what they missed.

Quiz JSON:

```json
{
  "id": "q-20261023-1",
  "title": "Photosynthesis: practice quiz",
  "course": "Biology 101",
  "instructions": "Check each answer and read the explanation before moving on.",
  "shuffle": false,
  "topics": { "light-reactions": "Light-dependent reactions" },
  "questions": [
    { "id": "q1", "type": "mcq", "topic": "light-reactions", "difficulty": 1, "prompt": "Where do the **light-dependent reactions** occur?",
      "options": ["Stroma", "Thylakoid membranes", "Mitochondria", "Cell wall"], "answer": 1,
      "hint": "Where is chlorophyll embedded?", "explanation": "...", "source": "[S1 ¶4]" },
    { "id": "q2", "type": "tf", "prompt": "...", "answer": false, "explanation": "...", "source": "..." },
    { "id": "q3", "type": "fill", "prompt": "The Calvin cycle occurs in the ____.", "answer": ["stroma"], "explanation": "...", "source": "..." },
    { "id": "q4", "type": "short", "prompt": "...", "modelAnswer": "...", "keyPoints": ["...", "..."], "explanation": "...", "source": "..." },
    { "id": "q5", "type": "significance", "prompt": "Explain the significance of ...", "modelAnswer": "...", "keyPoints": ["..."], "source": "..." }
  ]
}
```

`answer` is a 0-based option index for `mcq`, `true`/`false` for `tf`, and a list of accepted answers for `fill` (matching ignores case, accents and surrounding punctuation). Prompts, options and explanations accept `**bold**`, `` `code` ``, lists and `$LaTeX$`.

## Files

In the active course (`study/courses.json`):

- Append one line per answered question to `study/<course>/quizzes/history.jsonl`:
  `{"ts":"2026-10-23T15:04:00","quiz":"q-20261023-1","mode":"quiz","round":1,"topic":"light-reactions","type":"mcq","difficulty":2,"correct":true,"source":"[S1 ¶4]"}`
  (`correct` is `true`, `false` or `"partial"`.)
- Append one line per wrong or partly-right answer to `study/<course>/errors.jsonl`:
  `{"id":"e-20261023-001","ts":"...","topic":"calvin-cycle","type":"mcq","question":"...","student_answer":"ATP","correct_answer":"NADPH","why_wrong":"Mixed up ATP (energy) and NADPH (electrons).","source":"[S1 ¶7]","times_missed":1,"streak":0,"resolved":false,"resolved_ts":null}`
  If the same mistake is already open in the log, increase its `times_missed` and reset `streak` to 0 instead of adding a duplicate.
- When the student now gets an open logged mistake right with a new question, increase its `streak` (see review-mistakes for when it counts as resolved).

Without file access, keep the running tally in the conversation and offer the log as a file at the end.

## Quality rules

- **Accuracy over speed.** Every question and answer must be supported by the student's materials. Never invent facts, and never mark a correct answer wrong (or a wrong one right) to keep things moving. If the sources are ambiguous on a question, drop it or say so.
- **Explain and cite every answer.** Give the explanation plus `[S# location]`. Mark general-knowledge material as such.
- **Active recall.** The quiz *is* active recall: ask, then reveal. Don't show answers before the student has tried.
- **Academic integrity.** Practice quizzes only. If the questions are from a graded quiz, homework or a live exam, say kindly that you can't answer those, and offer practice questions on the same topics instead.
- **Study Mode.** If Study Mode is on, before revealing the answer to a wrong attempt, give one hint and let them try again. Then explain.
