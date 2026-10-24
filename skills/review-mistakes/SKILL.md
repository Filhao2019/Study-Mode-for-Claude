---
name: review-mistakes
description: Quiz the student only on their logged mistakes from the error log (every wrong quiz, mock-exam or Feynman answer, with the topic and why it was wrong), using new questions that target the same misconception, and mark mistakes resolved once they're answered correctly in two separate sessions. Use when the student asks to review mistakes, go over what they got wrong, practice their errors, revisit weak questions, or clear their error log.
---

# Review mistakes

The error log is the most valuable study list a student has: it's exactly what they don't know yet. This skill works through it until the mistakes stop happening.

## The error log

`study/<course>/errors.jsonl`, one entry per line:

```json
{"id":"e-20261023-001","ts":"2026-10-23T15:04:00","topic":"calvin-cycle","type":"mcq","question":"Which molecule supplies the electrons that reduce 3-PGA?","student_answer":"ATP","correct_answer":"NADPH","why_wrong":"Mixed up ATP (energy) and NADPH (electrons).","source":"[S1 ¶7]","times_missed":1,"streak":0,"resolved":false,"resolved_ts":null}
```

Other skills append to it; this skill updates entries in place (rewrite the whole file, keeping every line, including resolved ones).

## Steps

1. **Load open entries** (`resolved: false`). Filter by topic if the student named one. If there are none, congratulate them briefly and offer a quiz to find new gaps.
2. **Group by misconception**, not by question: several entries with the same `why_wrong` idea are one thing to fix. Order groups by `times_missed` (highest first), then by age (oldest first).
3. **Say what's ahead** in one line ("6 open mistakes in 3 groups: ATP vs NADPH, ...").
4. **For each group, ask one new question** that targets the same misconception from a different angle: a new example, a new format (if the original was MCQ, try short answer or true/false), or a reversed question. Don't repeat the original question word for word. One question at a time.
5. **Feedback:**
   - Correct: confirm, say why it's right, and increase `streak` by 1 for every entry in the group. If `streak` reaches 2 **and** the previous correct answer was in an earlier session (a different day), set `resolved: true` and `resolved_ts`. Otherwise tell them it'll come back once more in a later session to make sure it sticks.
   - Wrong: explain the misconception directly (what they're mixing up and how to tell the two apart), cite the source, set `streak` to 0, increase `times_missed`, and update `why_wrong` if their reasoning revealed something new. Then ask one more fresh question on it before moving on.
   - A group missed three or more times overall: suggest a different approach, such as `/study:feynman` on the concept, `/study:explain-like` at a simpler level, or a flashcard for the key distinction.
6. **Log each answer** to `quizzes/history.jsonl` with `"mode":"review-mistakes"`.
7. **Wrap up:** resolved now, still open, and when to review again (spacing: tomorrow for anything missed today, in 3–4 days for anything with streak 1).

Without file access, ask the student to paste their error log (or use mistakes from this conversation), and give the updated log back as a file at the end.

## Quality rules

- **Accuracy over speed.** Base explanations on the student's materials and cite them. If a logged "correct answer" looks wrong when you check the source, say so and fix the entry rather than drilling an error.
- **Active recall.** Always ask first; explain after the attempt.
- **Kind and specific.** Mistakes are progress markers, not failures. Name the pattern clearly.
- **Academic integrity.** Practice only, never answers to graded work.
- **Study Mode.** If Study Mode is on, on a wrong answer give a hint and let them retry once before explaining.
