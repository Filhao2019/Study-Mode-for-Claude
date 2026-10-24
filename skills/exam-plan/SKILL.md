---
name: exam-plan
description: Build a day-by-day study schedule from today to an exam date that mixes new material, spaced review of earlier topics, and practice tests, weighted toward weak topics, with a lighter load on the final day. Use when the student has an exam or test date and asks for a study plan, revision timetable, schedule, or "how should I prepare", or says how many days or weeks they have left.
---

# Exam plan

A realistic plan the student can actually follow: specific tasks each day, spaced review built in, practice tests at the right moments, and a calm final day.

## Gather (ask only what's missing, in one message)

- **Exam:** name, date, format and topics (from `study/<course>/course.json` if saved; an exam guide from `exam-guides` for standard exams).
- **Time available:** hours per weekday and per weekend day, and days they can't study.
- **Where they stand:** read `quizzes/history.jsonl` and `errors.jsonl` for topic accuracy (see weak-spots). Without history, ask which topics feel weakest, or suggest a short diagnostic quiz first.
- **Today's date** comes from the environment. Never guess it. Count the days carefully, including the exam day.

## How to build the plan

1. **Classify topics:** *new* (not studied yet), *weak* (accuracy under 70% or open mistakes), *ok* (70–85%), *strong* (over 85%). Weight by exam importance when known (`weight` in `course.json` or the guide).
2. **Phases** for a plan of a week or more:
   - **Learn (about the first 50–60% of days):** new material, one or two topics a day, each followed by a short quiz the same day.
   - **Consolidate (about the next 30%):** weak topics first, mixed (interleaved) practice across topics, past-paper style questions.
   - **Final stretch (last 2–3 days):** a full mock exam about 3 days before (not the last day), then review of its mistakes, cheat sheet and flashcards only.
3. **Spaced review:** after a topic is first studied, schedule short reviews about **1, 3, 7 and 14 days later** (whichever fit before the exam). Reviews are 10–20 minute tasks: flashcards, a 5-question quiz, or re-explaining from memory.
4. **Practice tests:** at least one mid-plan practice test or mixed quiz, and one full mock exam near the end. Each is followed the next day by a mistakes-review session.
5. **Final day is light:** at most about an hour. Skim the cheat sheet, a short flashcard round, check logistics (time, place, ID, calculator, pens), and sleep early. No new material.
6. **Balance:** put the hardest tasks early in a session, keep one lighter day a week on longer plans, and never schedule more than the hours the student gave you. If the content doesn't fit, say so and cut by priority (low-weight strong topics first), rather than overloading.
7. **Short plans (3 days or fewer):** triage. Focus on high-weight weak topics with active recall, one timed practice set, and the light final day. Say honestly what's realistic.

## Output

A short intro (days left, hours available, the strategy in two sentences), then a table:

```markdown
| Day | Date | Focus (new) | Review (spaced) | Practice | Time |
|---|---|---|---|---|---|
| 1 | Mon 3 Nov | Light reactions: notes + quiz (`/study:notes light reactions`) | | 5-question quiz | 1.5 h |
| 2 | Tue 4 Nov | Calvin cycle | Light reactions flashcards (day+1) | | 1.5 h |
| ... | | | | | |
| 12 | Fri 14 Nov | **Exam day**: light review only | Cheat sheet skim | | ≤1 h |
```

Under the table: a checklist of commands to run each day is optional, plus "If you miss a day" advice (shift review tasks, never skip the mock exam). Save to `study/<course>/plans/exam-plan-<exam-slug>.md` and add the exam to `course.json` if it isn't there.

When the student comes back mid-plan, re-plan from today using the latest quiz results instead of starting over.

## Quality rules

- **Accuracy over speed.** Use the real exam date, real topic list and real hours. Never invent the exam's format; if unknown, ask or mark it as an assumption.
- **Active recall over passive reading.** Every study block includes retrieval (a quiz, flashcards, explaining from memory), not just rereading.
- **Wellbeing.** Plans include breaks and sleep. If the student describes an unrealistic load or serious stress, say so kindly and suggest talking to a teacher or counselor if it's more than exam nerves.
- **Academic integrity.** Plans prepare students to take exams themselves; never plan around getting answers during the exam.
- **Study Mode.** If Study Mode is on, present the plan and then ask one question to confirm it fits their week.
