# Digital SAT

> Starter outline, original summary. Official source: **College Board SAT Suite** (satsuite.collegeboard.org) and the Bluebook app's full-length practice tests. Last checked: October 2026.

## Format

| Section | Modules | Questions | Time |
|---|---|---|---|
| Reading and Writing | 2 modules × 27 | 54 | 64 min (32 per module) |
| *Break* | | | 10 min |
| Math | 2 modules × 22 | 44 | 70 min (35 per module) |

- Total testing time 2 h 14 min, taken in the **Bluebook** app.
- **Multistage adaptive:** how you do on module 1 decides whether module 2 of that section is the easier or harder version. Module 1 matters.
- Scores: 200–800 per section, 400–1600 total. No penalty for wrong answers.
- Reading and Writing: short passages, one question each. Math: about three quarters multiple choice, a quarter student-produced responses. A calculator is allowed on all of Math (a graphing calculator is built into Bluebook), and a reference sheet is provided.
- Each module includes a few unscored pretest questions you can't identify, so treat every question as scored.

## Topic outline (approximate share of each section)

| Section | Domain (`id`) | Share | What's in it |
|---|---|---|---|
| Reading and Writing | Information and Ideas (`rw-information-ideas`) | ~26% | central ideas, evidence (textual and quantitative), inferences |
| | Craft and Structure (`rw-craft-structure`) | ~28% | words in context, text structure and purpose, cross-text connections |
| | Expression of Ideas (`rw-expression-ideas`) | ~20% | rhetorical synthesis from notes, transitions |
| | Standard English Conventions (`rw-conventions`) | ~26% | boundaries (punctuation between clauses), form, structure and sense (agreement, verb forms) |
| Math | Algebra (`math-algebra`) | ~35% | linear equations, inequalities, systems, linear functions |
| | Advanced Math (`math-advanced`) | ~35% | nonlinear functions, quadratics, exponentials, equivalent expressions |
| | Problem-Solving and Data Analysis (`math-data`) | ~15% | ratios, rates, percentages, units, statistics, probability, data displays |
| | Geometry and Trigonometry (`math-geometry`) | ~15% | area and volume, lines and angles, triangles, right-triangle trigonometry, circles |

## Skills the exam rewards

- Precise reading of short texts: what the passage *says*, not what's plausible.
- Grammar rules applied quickly (especially punctuation that joins or separates clauses).
- Fluent algebra and translating word problems into equations; knowing when graphing the equation is faster.
- Pacing: about 71 seconds per Reading and Writing question and about 95 seconds per Math question.

## Common traps

- Answer choices that are true in general but not supported by the passage.
- "Rhetorical synthesis" questions: the right answer meets the stated goal, not the most detailed one.
- Student-produced responses: entering a correct value in an unaccepted form, or forgetting a negative sign.
- Rushing module 1 to "save time" for module 2.

## Using the plugin

- `/study:course new SAT` seeds the domains above.
- Use College Board's official Bluebook practice tests for full-length timing; Claude-made `/study:mock-exam` sets are for extra practice and can't reproduce the adaptive scoring, so treat their percentages as estimates, never as SAT scores.
- After each official practice test, log missed question types with `/study:quiz` follow-ups and track them in `/study:weak-spots`.
