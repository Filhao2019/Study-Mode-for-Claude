---
name: cheatsheet
description: Compress a whole course, or an exam's worth of topics, into a dense one-page final-review sheet with key definitions, formulas, processes, comparisons and the student's own common mistakes, printable on a single page. Use when the student asks for a cheat sheet, crib sheet, one-pager, summary sheet, formula sheet, last-minute review, or "everything on one page" before an exam.
---

# One-page cheat sheet

Everything that matters for the exam, on **one page**, organized so the student can rebuild each topic from a glance. Making it is itself a great review; reading it the night before is the light final-day task in an exam plan.

## Gather

From the active course: `course.json` topics and exam scope, all notes in `notes/`, the sources for anything not yet in notes, `errors.jsonl` for the student's own recurring mistakes, and any exam guide. Ask which exam it's for if there are several.

## Choose what goes in

Room is the constraint, so prioritize:

1. Definitions of core terms (the shortest precise version)
2. Formulas and equations, with symbols and units
3. Processes as compact sequences (arrows) or tiny diagrams
4. Comparisons as small tables (X vs Y)
5. **"Watch out" lines** from the error log: the student's own repeat mistakes
6. Exam technique reminders from the guide or past-paper profile (command words, units, time per mark)

Leave out side remarks, history, worked examples longer than two lines, and anything the student marked as already mastered (unless it's high-weight).

## Format

- **One page** of A4 or US Letter. As a guide: about 500–900 words of Markdown, in a two-column-friendly structure: one `##` section per major topic, very short bullets, `**bold**` key terms.
- Compression tricks: arrows for processes (`light → e⁻ excited → ETC → H⁺ gradient → ATP`), abbreviations defined once, tables instead of sentences, LaTeX for formulas.
- Small citations in brackets at the end of each section rather than on every line: `[S1 p.3-6, S3 05:10-18:40]`.
- A tiny **"Top 5 traps"** box at the end.

Save as `study/<course>/cheatsheet.md` (or `cheatsheet-<exam-slug>.md`).

**Print version:** when the student wants to print, also make `cheatsheet.html`: a single self-contained page with the same content, CSS two (or three) columns, small but legible type (about 8–9 pt), tight margins, `@page { size: A4; margin: 10mm; }` (or Letter), light and dark screen styles, and black-on-white when printed. Tell them to use the browser's Print → "Save as PDF" and check it fits one page; if it spills over, cut lower-priority lines rather than shrinking the font further.

For cheat sheets built from many sources, hand the draft to the `study:source-checker` agent if available and fix what it finds.

## Quality rules

- **Accuracy over speed.** Compression must not distort. Every line must be true according to the sources; if two sources conflict, include the course's version and flag it. Never invent formulas or values.
- **Cite** each section's sources; mark general-knowledge additions.
- **Active recall.** Suggest the student first try to write the sheet from memory for one topic, then compare, and offer a final quiz.
- **Academic integrity.** A cheat sheet is a study and review aid. Only take it into an exam if the exam explicitly allows a formula or notes sheet, and then follow its rules (size, handwritten, etc.). Say this kindly when you hand it over.
- **Study Mode.** If Study Mode is on, offer to build it together, topic by topic, with the student proposing each line first.
