---
name: course
description: Create, switch, list and update study courses (one folder per subject) holding the topic list, exam dates, notes, flashcard decks, quiz history and error log. Use when the student starts studying a new subject, says which class or exam they are working on, asks to switch courses, add or change an exam date, see their courses, or check course status. Other Studying with Claude skills rely on the active course this skill manages.
---

# Course organization

A course is one folder per subject under `study/` in the student's working folder. Every other skill reads the **active course** to know where sources, notes, decks, quiz history and the error log live. Full file formats are in [reference/layout.md](reference/layout.md); read it before creating or editing course files.

## What the student can ask for

| Request | Example | What to do |
|---|---|---|
| New course | `/study:course new Biology 101` | Create the folder and files, make it active |
| Switch | `/study:course switch chem` | Set `active` in `study/courses.json` (match by slug or name, case-insensitive) |
| List | `/study:course list` | Table of courses: name, next exam, days left, topics, decks, last quiz |
| Add exam | `/study:course exam Midterm 2026-11-14` | Append to `exams` in `course.json`; ask for format and topics if unknown |
| Status | `/study:course` or `/study:course status` | Summary of the active course (see below) |
| Rename / archive | `/study:course rename ...` | Change `name` only; never change a slug that files already use |

With no argument, show the status of the active course, or offer to create one if there is none.

## Creating a course

1. Ask only for what you don't know yet, in one short message: course name, level (high school, university year, ...), and any exam with date and format. Everything else can come later.
2. Make a slug from the name (`Biology 101` becomes `bio-101` or `biology-101`; keep it short and readable).
3. Create `study/<slug>/` with `course.json`, `sources/index.json` (`{"sources": []}`), and empty folders `notes/`, `decks/`, `quizzes/`, `plans/`, `podcasts/`, `mock-exams/`. Create `study/courses.json` if it doesn't exist, add the course, and set it as `active`.
4. If the course follows a standard exam (ENEM, SAT, AP, IB), use the `exam-guides` skill to seed `topics` and the exam `format`, and set `guide` to the guide's file name. Tell the student the topics are a starting outline to adjust to their own syllabus.
5. Finish by suggesting the next step: add materials (`ingest`, or `transcribe` for lecture recordings), or build an exam plan if a date is set.

## Status summary

Read `course.json`, `sources/index.json`, `quizzes/history.jsonl`, `errors.jsonl` and the `decks/` folder, then show:

- course name and level
- each exam with date and **days left** (today's date from the environment; never guess it)
- number of sources and topics
- quiz accuracy overall and for the last 7 days, if there is history
- unresolved mistakes in the error log
- flashcard decks
- one suggested next action, with the command to run

Keep it to a short table and two or three lines of text.

## Rules

- **Never delete student data.** Renaming a course changes its `name`, not its folder. To remove a course, tell the student which folder to delete themselves.
- **Don't guess dates.** If the student says "next Friday", turn it into a date, then confirm it with them.
- **One active course at a time.** When a request clearly belongs to another course ("make flashcards for my chem class"), switch to that course and say so in one line.
- **No file access?** On surfaces where you can't read or write files (for example a plain chat), keep the course details in the conversation, use them consistently, and offer the files as downloads at the end. Don't pretend something was saved.
- **Academic integrity.** Courses organize the student's own studying. Help them learn; never complete graded work for them.
