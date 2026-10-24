---
name: mock-exam
description: Create a timed, full-length practice exam that matches the real exam's format (sections, question types, number of questions, timing, marks), delivered as a self-contained HTML exam with a countdown and graded at the end with a score breakdown by section, topic and question type. Use when the student asks for a mock exam, practice exam, practice test, past-paper-style full test, timed test, or exam simulation. For short untimed practice use quiz.
---

# Mock exam

A dress rehearsal: same structure, same timing, same pressure, no feedback until the end. Then an honest score and a breakdown that shows what to fix.

## 1. Pin down the format

Find the real exam's format, in this order:

1. `course.json` → `exams[].format` for this exam.
2. A past paper the student has ingested (`kind: past-paper`): use the `past-paper` skill's style analysis.
3. A standard exam (ENEM, SAT, AP, IB): the `exam-guides` skill has the published structure.
4. Otherwise ask: sections, question types and counts, time allowed, marks per question, calculator or notes rules.

Confirm in one line ("Full-length: 2 sections, 60 MCQ in 90 min + 6 free-response in 90 min. OK, or shorter?"). Offer a **half-length** version (same proportions, half the questions and time) when a full one is too long for today.

## 2. Write the exam

- **Match the blueprint:** the same sections, order, question types, number of questions and marks, and topic weighting (from the guide or syllabus). Cover the exam's topics, weighted toward what the exam stresses, not just the student's favorite topics.
- **Realistic difficulty:** mostly middle difficulty with some easy and some hard questions, like the real thing. Use the exam's command words (describe, explain, evaluate, calculate, justify).
- **Original questions only.** Never copy real exam questions; write new ones in the same style, with new scenarios, data and numbers.
- **Every question** has a `topic`, `points`, the answer (or a mark scheme with marks per point for written answers), a short explanation, and a `source` citation from the student's materials where possible.
- **Check your answer key** before saving: re-solve every calculation and re-check every MCQ's single correct option.

## 3. Deliver it

Fill `${CLAUDE_SKILL_DIR}/assets/mock-exam.html`: replace only the JSON inside `<script type="application/json" id="exam-data">`, keep it valid JSON (escape backslashes, write `<\/` for `</`, no `$` for money), and save as `study/<course>/mock-exams/<exam-id>.html`.

```json
{
  "id": "mock-midterm-1",
  "title": "Biology 101 Midterm: mock exam 1",
  "course": "Biology 101",
  "timing": "sections",
  "instructions": "No notes or calculator. Answer every question.",
  "sections": [
    { "id": "A", "name": "Section A: Multiple choice", "timeMinutes": 45, "questions": [
      { "id": "a1", "type": "mcq", "topic": "light-reactions", "points": 1, "prompt": "...", "options": ["...", "...", "...", "..."], "answer": 2, "explanation": "...", "source": "[S1 p.4]" }
    ] },
    { "id": "B", "name": "Section B: Structured questions", "timeMinutes": 45, "questions": [
      { "id": "b1", "type": "short", "topic": "calvin-cycle", "points": 4, "prompt": "... (4 marks)",
        "rubric": [ { "point": "...", "marks": 1 }, { "point": "...", "marks": 1 } ], "modelAnswer": "...", "source": "[S1 p.6]" }
    ] }
  ],
  "bands": [ { "min": 80, "label": "On track for the top grade" }, { "min": 60, "label": "Passing, with gaps" }, { "min": 0, "label": "Needs more practice" } ]
}
```

- `timing`: `"sections"` (each section has its own `timeMinutes` and closes when finished, as in most real exams) or `"total"` with a top-level `timeLimitMinutes` (one clock, free navigation).
- Types: `mcq`, `tf`, `fill`, `short`, `significance`, `essay`. Written answers use `rubric` (or `keyPoints`) and `modelAnswer`.
- `bands` are optional rough labels. **Never present a percentage as an official scaled score** (SAT 400–1600, AP 1–5, IB 1–7, ENEM TRI). If the student asks, explain that official scaling isn't public or depends on the cohort, and give the percentage instead.

Without file access, run the exam in the chat: give all questions at once with the time limit, ask the student to note start and end times, and grade when they submit.

## 4. Grade

- Objective questions are graded automatically by the page.
- Written answers: the page shows the mark scheme for self-marking, and a **Copy written answers for Claude** button. When the student pastes them, grade strictly against the mark scheme. If the `study:exam-grader` agent is available, delegate the written answers to it for consistent, independent marking; otherwise grade them yourself with the same rubric. Give marks per point with a one-line reason.
- When the student pastes **Copy results for Claude**, log every answer to `quizzes/history.jsonl` with `"mode":"mock-exam"` and the results' `submitted` time as `ts` (`correct` is already `true`, `"partial"` or `false`), add each lost-mark answer to `errors.jsonl` with why it was wrong, and save the results JSON next to the exam (`<exam-id>-results.json`).

## 5. Debrief

Short and specific: score and how it compares with their last mock (if any); the strongest and weakest sections and topics; time management (did a section run out, were questions left blank); the three highest-value fixes, each with a command (`/study:review-mistakes`, `/study:quiz <topic>`, `/study:feynman <concept>`); and when to take the next mock (not the day before the exam).

## Quality rules

- **Accuracy over speed.** A wrong answer key does real harm. Double-check every key and mark scheme against the sources; if the sources don't settle a question, cut it.
- **Cite** each answer's source in the explanation; mark general-knowledge material as such.
- **Active recall.** No hints or feedback during the exam; full explanations after.
- **Academic integrity.** Mock exams are practice. Never reproduce a live or upcoming real exam, and never help during an actual exam. If the student seems to be in one, say kindly that you can't help until it's over.
- **Study Mode.** If Study Mode is on, the exam itself stays exam-like; use Study Mode's style in the debrief (ask them to diagnose one mistake before you explain it).
