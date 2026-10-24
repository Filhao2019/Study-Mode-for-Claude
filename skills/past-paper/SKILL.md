---
name: past-paper
description: Analyze an uploaded old exam or past paper (question types, command words, marks, difficulty, topic coverage, typical traps) into a style profile, then write new, original practice questions in that same style with mark schemes. Use when the student shares a past paper, previous exam, old test, sample paper or specimen paper and wants to understand it, practice in its style, or get similar questions.
---

# Past-paper analysis

Past papers show *how* a course examines. This skill learns the style from a paper and writes **new** questions that train the same skills, without copying the paper.

## 1. Read the paper

- Ingest it as a source with `kind: past-paper` (use the `ingest` skill for PDFs, photos and scans). Read every question and any mark scheme or examiner's report the student has.
- **Check it isn't live.** If it's an exam that is still running, a take-home exam, or graded homework, stop and say kindly that you can help with the topics but not with that paper's questions.

## 2. Build a style profile

Present it as a compact table, then two or three sentences of advice:

| Feature | What to record |
|---|---|
| Structure | Sections, number of questions, time, total marks, choices ("answer 3 of 5") |
| Question types | MCQ, short answer, structured multi-part, data analysis, calculation, essay, diagram labelling... with counts |
| Command words | describe, explain, evaluate, compare, calculate, justify, and what each demands in this paper |
| Marks | Typical marks per part, and roughly how many points a mark needs |
| Difficulty | Share of recall vs application vs analysis (difficulty 1–4) |
| Topic coverage | Which course topics appear and how often; link them to `course.json` topic IDs |
| Recurring patterns | Typical stems, data or graphs, real-world contexts, multi-step calculations |
| Traps | Places students commonly lose marks (units, significant figures, "two reasons" asking for two, vague wording) |

If a mark scheme is available, note what earns marks ("must mention the proton gradient for the second mark"). With several papers from the same course, compare them and note what changes and what's stable.

Save the profile to `study/<course>/notes/past-paper-style.md` and, if the exam is in `course.json`, put a one-line summary in that exam's `format`.

## 3. Write new questions in the style

- Ask how many (default: one paper-section's worth) and whether to deliver as a quiz (`quiz` skill, with feedback) or as a timed paper (`mock-exam` skill).
- **Original questions only.** New scenarios, data, numbers, organisms, texts and contexts. Never reuse or lightly paraphrase the paper's questions; the student can re-do those themselves.
- Match the profile: same command words, mark allocations, multi-part structure, difficulty mix and topic weighting.
- Write a **mark scheme** for each question in the paper's own style (one point per mark, acceptable alternatives, common wrong answers that get no credit).
- Base content on the student's course materials and cite them (`[S2 p.7]`); flag anything from general knowledge.
- Re-solve every calculation and re-check every answer before presenting.

## 4. Practice loop

Offer to run the new questions now (quiz) or as a timed paper (mock exam). Mistakes go into the error log with why they happened, as usual.

## Quality rules

- **Accuracy over speed.** The profile must describe the actual paper. If a page is unreadable or the mark scheme is missing, say what you couldn't assess. Never invent "what examiners want" without evidence; label your own judgment as such.
- **Cite** the paper by question number when describing its style (`[S6 Q3b]`), and course materials for content.
- **Copyright.** Don't reproduce the paper's questions in your output beyond a few words needed to refer to them.
- **Active recall.** End by offering to practice the new questions.
- **Academic integrity.** Practice from old papers only. Never answer a current exam, a take-home exam or graded homework.
- **Study Mode.** If Study Mode is on, deliver new questions one at a time and use the hint ladder on mistakes.
