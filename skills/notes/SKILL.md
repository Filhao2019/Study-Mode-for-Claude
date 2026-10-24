---
name: notes
description: Write rich, structured study notes from the student's materials or a lecture transcript, with headings, bold key terms, tables, LaTeX math and chemistry, Mermaid diagrams, code blocks for programming, core exam content separated from side remarks, a likely-exam-questions section, and source citations. Use when the student asks for notes, a summary of a chapter, lecture, slides or transcript, a study guide for one topic, or to organize what they've ingested. For a whole-course one-pager use cheatsheet; to re-explain one idea at a different level use explain-like.
---

# Rich notes

Turn sources into notes a student can learn from and revise with: well organized, precise, honest about what the sources do and don't say, and ending in active recall.

## Inputs

- **What to cover:** a topic from `course.json`, a source (`S3`), a file, a transcript, or text in the chat. If the request is vague ("make notes"), offer the course topic list and ask which topic, or cover the most recent source.
- **Read the sources fully** for the parts you cover. Notes are only as good as your reading. Use the anchored files in `study/<course>/sources/`; if something isn't ingested yet, ingest it first (or read it directly when there's no course).
- **Level and language:** from `course.json` or the conversation. Write in the student's language.

## Structure

Use this skeleton, and drop any section that has nothing true to say:

```markdown
# <Topic>

> <Course> · Sources: S1, S3 · <date> · Check anything important against your materials.

## Overview
Three to five sentences: what this topic is, why it matters, how it connects to the topics around it.

## Core exam content
### 1. <Subtopic>
- **Key term**: precise definition in plain words [S1 p.3]
- How it works, step by step [S1 p.3-4]
(tables, equations, diagrams and code where they help)

## Side remarks
Anecdotes, history, "for interest" material and tangents the lecturer flagged as not examined [S3 12:10].

## Common mistakes
- Mixing up X and Y: X does ..., Y does ... [S1 p.5]

## Likely exam questions
1. <Question in the style of the course's exams> (see §1, [S1 p.3])

## Sources
- S1: Week 5 handout (pages 3–6)
- S3: Lecture 5 recording (05:10–18:40)
```

### Core content vs side remarks

Put material in **Core exam content** when the sources signal it matters: learning objectives, syllabus items, slide titles, definitions, bold or boxed text, "you need to know", "this will be on the exam", repetition across sources, worked examples, past-paper topics. Put it in **Side remarks** when it's an aside: history, anecdotes, "just for interest", previews of later courses, or the lecturer says it isn't examined. When you can't tell, keep it in core content and say so briefly ("not sure if examined").

### Formatting toolkit

- **Bold** each key term the first time it appears, with its definition.
- **Tables** for comparisons (A vs B), classifications, properties, timelines and pros/cons.
- **LaTeX** for math, physics and chemistry: `$...$` inline and `$$...$$` for display. Write chemical equations with plain LaTeX so they render everywhere: `$$6\,\mathrm{CO_2} + 6\,\mathrm{H_2O} \xrightarrow{\text{light}} \mathrm{C_6H_{12}O_6} + 6\,\mathrm{O_2}$$`. Define every symbol and unit.
- **Mermaid** for processes, cycles, hierarchies and cause-and-effect chains. Keep diagrams small (at most about 12 nodes), use `flowchart LR` or `TD`, and quote labels containing punctuation: `A["NADPH + ATP"]`. A Mermaid diagram adds structure; it never replaces the explanation.
- **Code blocks** with a language tag for programming courses. Code must be correct and runnable as shown, with expected output in a comment.
- **Worked examples** for anything procedural, laid out step by step, with each step justified.
- Keep paragraphs short. Notes are for scanning and recall, not prose.

### Likely exam questions

Write 5–8 questions that match how this course examines (use past papers or the exam format in `course.json` if available; otherwise mix recall, explain, apply and compare). Point to the section that answers each one, but **don't write the full answers**: working them out is the revision. Offer to quiz the student on them.

## Saving

Save to `study/<course>/notes/<topic-slug>.md` (if the file exists, ask whether to update it or create `-v2`). Tell the student where it is. Without file access, show the notes in the chat.

For long notes built from three or more sources, or when the student asks for a double-check, hand the draft to the `study:source-checker` agent if it's available, fix what it finds, and mention that it was checked.

## Quality rules

- **Accuracy over speed.** Use only what the sources support. Never invent facts, numbers, dates, formulas, examples or citations. If a source is unclear, incomplete or contradicts another, say so in the notes (`> ⚠️ S1 and S3 disagree on ...`) and ask the student which their course uses.
- **Cite every fact** with its anchor: `[S1 p.3]`, `[S2 slide 5]`, `[S3 ¶12]`, `[S4 12:34]`. Anything you add from general knowledge (a clarifying analogy, a standard definition the sources skip) is marked *(general knowledge, not in your materials)*. Keep such additions few and clearly useful.
- **Active recall.** Always end with an offer: "Want a quick quiz on this (`/study:quiz`) or flashcards (`/study:flashcards`)?"
- **Academic integrity.** Notes are for learning. If the request is really to produce a graded assignment (an essay, lab report, take-home answers), say kindly that you can't write it for them, and offer notes and guidance they can use to write it themselves.
- **Study Mode.** If Study Mode is on, still produce the notes when asked, then continue in its style: check understanding with one question at a time instead of moving on.
