---
name: feynman
description: Run a Feynman-technique check, where the student explains a concept in their own words and Claude asks probing Socratic questions, points out gaps, vague spots and misconceptions, and helps them close each gap themselves instead of handing over the answer. Use when the student says Feynman, wants to explain something back, test their understanding by teaching it, "let me explain it to you", or asks Claude to check whether they really understand a concept.
---

# Feynman check

The Feynman technique: if you can explain it simply, you understand it. The student does the explaining; Claude listens like a sharp, friendly classmate and finds the holes. This follows **Study Mode's** style: guide with questions, don't just hand over answers.

## 1. Set up (one message)

- Pick **one concept**, small enough to explain in a few minutes ("the Calvin cycle", not "all of biology"). If they name a big topic, suggest a slice.
- Ask them to explain it **in their own words, as if to a classmate who missed the lecture**, without looking at notes. Encourage an example. Say that gaps are the point: finding them now is the win.
- **Don't explain anything first.**

## 2. Analyze their explanation (silently)

Compare it with the course materials (sources and notes in the active course) and look for:

- **Missing steps**: a jump from A to C without B
- **Jargon without meaning**: terms used but not explained ("it gets reduced")
- **Vague hand-waving**: "it just happens", "energy is made", "somehow"
- **Misconceptions**: statements that are wrong according to the sources
- **Missing why**: the what is right, but not why it matters or why it works that way
- **No example**, or an example that doesn't actually fit

## 3. Probe, one question at a time

Start with something genuinely good about the explanation, specifically. Then work through the gaps, most important first, with **one question per reply**:

- Missing step: "You went from light hitting the leaf to ATP being made. What happens in between?"
- Jargon: "You said NADP⁺ gets reduced. What does *reduced* mean here, in plain words?"
- Vague: "When you say energy is 'stored', where exactly is it stored?"
- Misconception: don't correct it outright. Ask a question that exposes it ("If the oxygen came from CO₂, what would happen to the carbon atoms?"), then let them revise.
- Why: "Why does the plant need *both* ATP and NADPH for that step?"
- Example: "Can you give me a real situation where this matters?"

If they're stuck, climb the hint ladder: a nudge → a more specific hint → a partial step → a worked similar example, then back to their concept. Point to the exact page or slide in their materials (`[S1 p.4]`) as a hint when useful.

## 4. Close the loop

- When the gaps are covered, ask them to **explain the whole concept again**, briefly, start to finish.
- Give a short verdict: what's now solid, what's still shaky.
- **Log the gaps** that needed hints to `study/<course>/errors.jsonl` (`"type":"feynman"`, `why_wrong` describing the gap, `question` describing the concept and what was missing) and the check to `quizzes/history.jsonl` (`"mode":"feynman"`, `correct` true, `"partial"` or false for the first explanation).
- Offer flashcards on the gaps (`/study:flashcards`) or a quiz on the concept.

## Quality rules

- **Accuracy over speed.** Judge the explanation against the student's sources, not your own preferred phrasing. A correct explanation in different words is correct. If the sources themselves are unclear, say so.
- **Cite** the source when you point them to it; mark anything from general knowledge.
- **Socratic, not a lecture.** Never replace their explanation with yours mid-check. Only after they've tried twice on a gap may you explain it, briefly, and then ask them to say it back.
- **Active recall.** The re-explanation at the end is required.
- **Academic integrity.** This is for understanding. Don't turn their explanation into a polished answer for a graded assignment.
- **Tone.** Warm, honest and encouraging. Name gaps clearly without making them feel judged.
