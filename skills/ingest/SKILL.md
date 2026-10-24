---
name: ingest
description: Read the student's course materials (PDFs, Word .docx, PowerPoint .pptx, photos or scans of handwritten notes, web pages, YouTube videos, plain text) into the active course, keeping every fact traceable to file plus page, slide or timestamp, and build or update the course topic list. Use when the student uploads, attaches, pastes or points to materials and wants Claude to learn from them, add them to a course, or build a topic list. For lecture audio or video recordings use the transcribe skill instead.
---

# Ingest course materials

Turn whatever the student hands you into **source files with location anchors** and a **topic list**, so every later note, quiz question and flashcard can cite exactly where a fact came from.

## Files

Work in the active course from `study/courses.json` (ask the `course` skill to create one if there is none, or work without saving if the student prefers):

- `study/<course>/sources/S<n>-<slug>.md`: one extracted file per source
- `study/<course>/sources/index.json`: the source registry
- `study/<course>/course.json`: the `topics` list

Anchor and citation formats:

| Source | Anchor written in the source file | How later skills cite it |
|---|---|---|
| PDF | `## [p.3]` | `[S1 p.3]` |
| Slides | `## [slide 5] Title` | `[S2 slide 5]` |
| Word, text, web | `## [§3] Heading`, `[¶12] paragraph` | `[S3 §3]`, `[S3 ¶12]` |
| YouTube, audio, video | `[00:12:34] text` | `[S4 12:34]` |
| Photo or scan of notes | `## [img 1]`, `[line 4]` where useful | `[S5 img 1]` |

The full schemas are in the `course` skill's `reference/layout.md`.

## Steps

1. **Register each source.** Give it the next free ID (`S1`, `S2`, ...; never reuse one) and a short slug. Ask what kind it is only if you can't tell (lecture slides, textbook chapter, own notes, past paper, syllabus).
2. **Extract the text** with the best tool available for the format:
   - **PDF**: read it directly if you can (page by page for long files), or run the extractor below. Pages with no extractable text are scans: read the page image and transcribe it.
   - **Word / PowerPoint**: run the extractor. If a document or slide-deck skill is available, it works too; keep the anchors.
   - **Images of handwritten or scanned notes**: look at the image and transcribe it faithfully, line by line. Write `[illegible]` for words you can't read and `[?]` after a word you're unsure of. **Never fill a gap with a plausible guess.** Afterwards, list the uncertain spots and ask the student to confirm them.
   - **Web pages**: fetch the page with your web tool, keep the main content only (no menus, ads or comments), and anchor it with `§`/`¶`. Record the URL and the date you read it.
   - **YouTube**: run the extractor with the URL to get the captions with timestamps. If there are no captions, ask the student for the audio file and use the `transcribe` skill. Don't download videos the student doesn't have the right to use.
   - **Plain text pasted into chat**: save it as a text source with `¶` anchors.
3. **Write the source file** with this header, then the anchored text:
   ```markdown
   ---
   source_id: S3
   title: Week 5 slides: Photosynthesis
   original: C:/Users/me/Downloads/week5.pptx
   type: pptx
   extracted: 2026-10-23
   ---
   ```
   Keep the student's wording. Fix only obvious extraction noise (broken hyphenation, repeated page headers and footers). Don't summarize at this stage.
4. **Update `sources/index.json`** with `id`, `title`, `file`, `original`, `type`, `kind`, `added`, and `notes` for anything a reader should know (scanned pages, missing images, low-quality captions).
5. **Build or merge the topic list** in `course.json`:
   - Use the source's own structure first (syllabus units, chapter headings, slide titles), then group the remaining content into topics a student would recognize.
   - Two levels are usually enough: topics and subtopics (`parent`).
   - Each topic lists the anchors where it is taught: `"sources": ["S1 p.3-5", "S2 slide 4-9"]`.
   - Merge with the existing list: reuse topic IDs when the new source covers the same idea, and don't create near-duplicates.
   - If a syllabus or exam guide gives exam weights, fill `weight`.
6. **Show the student a short summary**: sources added (with any warnings), and the topic list as an indented outline. Ask them to correct it, since they know their syllabus. Then offer next steps: notes (`/study:notes`), a diagnostic quiz (`/study:quiz`), or an exam plan if an exam date is set.

## Extractor script

```bash
python "${CLAUDE_SKILL_DIR}/scripts/extract.py" "<file-or-youtube-url>" --id S3 --out "study/<course>/sources/S3-<slug>.md"
```

- Use `python3` on macOS and Linux if `python` isn't found.
- Supports `.pdf`, `.docx`, `.pptx`, `.txt`, `.md`, `.html` and YouTube URLs (`--lang en,pt` sets caption language preference).
- Exit code 2 means a package is missing; the message names it. Ask before installing anything: `pip install pypdf python-docx python-pptx youtube-transcript-api` (only the ones needed).
- Notes printed by the script (scanned pages, embedded images, auto-generated captions) go into the source's `notes` in the index and into your summary.

## Quality rules

- **Accuracy over speed.** Extraction must be faithful. Never invent, "clean up" or complete content. If a page, slide or recording is unclear, say exactly what is unclear and ask.
- **Traceability.** Every chunk of text keeps its anchor, so every fact can be traced to file plus page, slide or timestamp.
- **Copyright and privacy.** Materials stay in the student's own folder for their own study. Don't republish them.
- **Academic integrity.** If the material is a live take-home exam or graded assignment the student must do alone, say kindly that you can help them review the underlying topics instead.
- **Study Mode.** If Study Mode is on, keep the summary brief and end with one question (for example, which topic to start with).
