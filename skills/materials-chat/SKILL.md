---
name: materials-chat
description: Answer the student's questions about course content from their own uploaded or ingested materials first, citing file plus page, slide or timestamp, and clearly flagging anything that comes from general knowledge instead. Use whenever the student asks a content question (what, why, how, explain, does my lecture say, where is) and course materials exist in study/ or in the conversation. Not for producing notes, quizzes, flashcards or plans, which have their own skills.
---

# Chat with your materials

When a student asks about their course, the right answer is **what their course says**, which is what they'll be marked against. Answer from their materials first, show where it comes from, and keep general knowledge clearly separate.

## How to answer

1. **Find the relevant sources.** Look in the active course: search `study/<course>/sources/*.md` (and notes in `notes/`) for the question's key terms and their synonyms, then read the surrounding passages. Also use files the student attached in this conversation.
2. **Answer from the materials**, in your own words, with a citation after each claim: `[S1 p.3]`, `[S2 slide 5]`, `[S3 ¶12]`, `[S4 12:34]`. Quote briefly (one short phrase) when the exact wording matters, such as a definition the student must learn.
3. **Flag general knowledge.** If the materials don't cover something you need for a complete answer, add it in a clearly marked part:
   > **From general knowledge (not in your materials):** ...

   Never mix uncited general knowledge into the cited answer.
4. **Say when the materials don't cover it.** "Your materials don't mention X" is a useful answer. Then offer what you know from general knowledge, marked as above, and suggest checking the textbook or asking the lecturer.
5. **Flag conflicts.** If two sources disagree, or the materials disagree with what's generally accepted, say so plainly, cite both, and recommend going with the course's version for the exam while checking with the instructor.
6. **Keep it short.** Answer the question asked; offer to go deeper.

## Example

> **Q:** Why does the Calvin cycle need NADPH?
>
> In your handout, NADPH supplies the **electrons** that reduce 3-PGA to G3P, while ATP supplies the energy for that step and for regenerating RuBP [S1 ¶7]. Both come from the light-dependent reactions [S1 ¶5].
>
> **From general knowledge (not in your materials):** NADPH is a reduced electron carrier; "reducing" a molecule means adding electrons to it.
>
> Want me to quiz you on the Calvin cycle?

## When there are no materials

If the student has no course or sources yet, answer normally, but say once that answers will be more useful and exam-specific if they share their notes or slides (`/study:ingest`).

## Quality rules

- **Accuracy over speed.** Never invent a citation or attribute something to a source that doesn't say it. If a passage is ambiguous, say so.
- **Every claim from the materials carries a citation**; everything else is labelled general knowledge.
- **Active recall.** After a substantial answer, offer one quick check question or a short quiz on the topic.
- **Academic integrity.** Explain concepts freely, but don't answer the questions of a graded assignment or a live exam for the student. If a question looks like one, say kindly that you'll help them understand the concept so they can answer it themselves.
- **Study Mode.** If Study Mode is on, guide instead of telling: point to the relevant page and ask a question that leads them to the answer, using the hint ladder. Still cite.
