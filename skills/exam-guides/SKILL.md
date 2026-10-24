---
name: exam-guides
description: Starter topic outlines and exam formats for common standardized exams, ENEM (Brazil), the digital SAT, AP Biology, AP Calculus AB, AP U.S. History, AP Chemistry, the IB Diploma and IB Biology, used to seed a course's topic list, exam plan and mock-exam blueprint. Use when the student mentions one of these exams or asks what's on it, how it's structured, or how to prepare for it.
---

# Exam guides

Short, original outlines of what each exam covers and how it's structured, so the other skills can start from a sensible topic list and blueprint. They are **starting points, not course content**: no textbook text, no real exam questions.

## Available guides

| Exam | File |
|---|---|
| ENEM (Exame Nacional do Ensino Médio, Brazil) | [guides/enem.md](guides/enem.md) |
| Digital SAT | [guides/sat.md](guides/sat.md) |
| AP Biology | [guides/ap-biology.md](guides/ap-biology.md) |
| AP Calculus AB | [guides/ap-calculus-ab.md](guides/ap-calculus-ab.md) |
| AP U.S. History | [guides/ap-us-history.md](guides/ap-us-history.md) |
| AP Chemistry | [guides/ap-chemistry.md](guides/ap-chemistry.md) |
| IB Diploma Programme (overview and core) | [guides/ib-diploma.md](guides/ib-diploma.md) |
| IB Biology (SL and HL) | [guides/ib-biology.md](guides/ib-biology.md) |

Read only the guide you need.

## How to use a guide

- **New course for this exam** (`course` skill): seed `course.json` `topics` from the guide's outline (stable topic IDs, `weight` from the published weightings), set the exam `format`, and set `guide` to the file name. Then tell the student to adjust the topics to their own teacher's order and syllabus.
- **Exam plan:** use the weightings to allocate time, and the format to place practice tests.
- **Mock exam:** use the format table as the blueprint (sections, counts, timing, question types).
- **Questions about the exam:** answer from the guide, then point to the official source it names for anything high-stakes (dates, rules, allowed calculators, accommodations).

## Keeping guides honest

- Each guide has a "last checked" date. Exam formats change (several AP exams change in May 2027). **Always tell the student to confirm details on the official page named in the guide** before relying on them, and if something in a guide conflicts with the student's official materials, trust the official materials.
- Don't invent details a guide doesn't contain (cut scores, official scaled-score conversions, exact dates). Say they aren't in the guide and where to find them.
- Content questions are answered from the student's own materials (`materials-chat`), not from the outline.
- **Academic integrity:** guides are for preparation. Never help during a real exam.
- **Study Mode:** if it's on, present the outline briefly and ask which area the student wants to start with.

## Contributing a guide

New guides follow the same shape: official source and last-checked date, format table, topic outline with weights, skills the exam rewards, common traps, and how to use the plugin for it. Original wording only.
