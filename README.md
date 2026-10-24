# 📚 Studying with Claude

**An open-source study toolkit for Claude.** Turn your own course materials into cited notes, adaptive quizzes, spaced-repetition flashcards, exam plans, mock exams and review podcasts, with a Socratic **Study Mode** that helps you work things out instead of handing you answers.

Works in **Claude Code** (terminal, desktop app, IDEs) and in the **Claude desktop app's chat and Cowork**. MIT licensed.

- Every fact is traced to your file + page, slide or timestamp. Anything from general knowledge is labelled.
- Quizzes adapt: harder on what you know, new questions on what you missed, until you get it.
- Every mistake is logged with *why* it happened, and comes back until it's fixed.
- Flashcards use **FSRS** spaced repetition in a single HTML file, and export to Anki.
- Built to help you learn, not to do your graded work.

---

## Contents

- [What's inside](#whats-inside)
- [How it works with Study Mode](#how-it-works-with-study-mode)
- [Install](#install)
- [Quick start](#quick-start)
- [Every command, with examples](#every-command-with-examples)
- [Your course folder](#your-course-folder)
- [Optional Python tools](#optional-python-tools)
- [Limitations](#limitations)
- [Academic integrity](#academic-integrity)
- [Privacy](#privacy)
- [Development](#development)
- [License and credits](#license-and-credits)

## What's inside

| Feature | Command | What you get |
|---|---|---|
| Study Mode | `/study:study-mode` | Socratic tutoring for the whole conversation: questions, hints, knowledge checks |
| Courses | `/study:course` | One folder per subject with topics, exam dates, notes, decks and quiz history |
| Ingest | `/study:ingest` | PDFs, Word, PowerPoint, photos of handwritten notes, web pages and YouTube, turned into cited sources and a topic list |
| Transcribe | `/study:transcribe` | Lecture recordings transcribed on your computer with Whisper, with timestamps |
| Chat with your materials | *(just ask)* | Answers from your own materials first, with citations; general knowledge clearly flagged |
| Rich notes | `/study:notes` | Headings, bold key terms, tables, LaTeX, Mermaid diagrams, code; core vs side content; likely exam questions; sources |
| Quizzes | `/study:quiz` | 5 question types, adaptive rounds, explanations with citations, an HTML quiz for long sets |
| Flashcards | `/study:flashcards` | One fact per card, cloze deletions, an HTML flip-card app with FSRS, Anki CSV export |
| Podcast | `/study:podcast` | A 5–10 minute two-host review script, turned into audio if you have a text-to-speech tool |
| Exam plan | `/study:exam-plan` | A day-by-day schedule mixing new material, spaced review and practice tests, light final day |
| Weak spots | `/study:weak-spots` | An HTML dashboard of accuracy per topic and what to study next |
| Mock exam | `/study:mock-exam` | A timed, full-length practice exam in the real format, graded with a breakdown |
| Past papers | `/study:past-paper` | An old exam's style analyzed, then new original questions in that style |
| Explain like... | `/study:explain-like` | The same idea at ELI5, high school, university or expert level |
| Feynman check | `/study:feynman` | You explain; Claude asks probing questions and finds the gaps |
| Cheat sheet | `/study:cheatsheet` | A whole course on one printable page |
| Error log | `/study:review-mistakes` | Practice only on what you've got wrong before, until it's resolved |
| Exam guides | *(automatic)* | Starter outlines and formats for ENEM, SAT, AP Biology, AP Calculus AB, AP U.S. History, AP Chemistry, IB Diploma and IB Biology |

Two helper agents run behind the scenes in Claude Code and Cowork: **source-checker** (fact-checks notes and answer keys against your sources) and **exam-grader** (marks written mock-exam answers strictly against the mark scheme).

## How it works with Study Mode

This plugin includes **Study Mode for Claude**, a Socratic tutoring skill modeled on ChatGPT's Study Mode, now part of Studying with Claude.

- **Study Mode handles *how* Claude teaches:** one question at a time, hints before answers, explanations in layers, knowledge checks, honest feedback.
- **The other skills handle *what* gets made:** notes, quizzes, flashcards, plans, mock exams, podcast scripts.

Turn Study Mode on (`/study:study-mode`, or just say "let's study") and every other skill follows its style: quizzes give a hint before revealing an answer, notes end with a check question, and the Feynman check is fully Socratic. Where they overlap, Study Mode's rule wins: **guide with questions, don't just hand over answers.** Say "stop studying" to switch back to normal answers.

> Already using the standalone Study Mode skill on claude.ai? After installing this plugin, turn the standalone skill off (**Customize → Skills**) so the two copies don't compete.

## Install



### Claude Code (terminal)

In a Claude Code session:

```text
/plugin marketplace add Filhao2019/studying-with-claude
/plugin install study@studying-with-claude
```

Or from your shell:

```bash
claude plugin marketplace add Filhao2019/studying-with-claude
```

```bash
claude plugin install study@studying-with-claude
```

Then type `/study:` to see the commands. (Inside Claude Code the short form, such as `/quiz`, also works when no other command has that name.)

### Claude desktop app: Code tab

The desktop app's Code tab, the terminal and VS Code share the same plugin settings on your computer.

1. Add the marketplace once, with the shell command above (`claude plugin marketplace add ...`), or with `/plugin marketplace add ...` in a terminal session.
2. In the Code tab, click **+** next to the prompt box → **Add plugins** (or **Plugins → Browse plugins**), find **Studying with Claude**, and choose a scope.

### Claude desktop app: chat and Cowork (and claude.ai)

1. Open **Customize → Plugins** (in the desktop app or at claude.ai).
2. Choose **Add → Add marketplace** and paste `https://github.com/Filhao2019/studying-with-claude`.
3. Install **Studying with Claude** from that marketplace.

Or download this repository as a ZIP and use **Add → Upload plugin**. Plugins you add to your claude.ai account also show up in Claude Code as synced plugins.

### Only want Study Mode on claude.ai?

Download [`dist/study-mode.zip`](https://github.com/Filhao2019/studying-with-claude/raw/main/dist/study-mode.zip) and upload it in **Customize → Skills**. That adds the Socratic tutor on its own, without the rest of the toolkit.

### Upgrading from Study Mode 1.0

The plugin id changed from `study-mode` to `study`. Run `/plugin marketplace update` (or update the marketplace from **Customize → Plugins**) and your install moves to the new plugin.

What runs where:

| | Claude Code (terminal, desktop Code tab, IDEs) | Cowork | Chat |
|---|---|---|---|
| All 18 skills and slash commands | ✓ | ✓ | ✓ (skills load when relevant) |
| Saving course files in `study/` | ✓ | ✓ | Only as downloadable files |
| Python scripts (extract, transcribe, Anki export) | ✓ | ✓ when it can run code | When code execution is available |
| Agents (source-checker, exam-grader) | ✓ | ✓ | Skipped; Claude does the check itself |

## Quick start

```text
/study:course new Biology 101
/study:ingest ~/Downloads/week5-slides.pptx ~/Downloads/chapter8.pdf
/study:notes photosynthesis
/study:quiz photosynthesis
/study:flashcards photosynthesis
/study:exam-plan midterm on 2026-11-14, 2 hours on weekdays
```

See [`examples/photosynthesis/`](examples/photosynthesis/) for a complete worked example with real outputs.

## Every command, with examples

You can type the commands, or just ask in plain words. Claude picks the right skill from what you say ("quiz me on chapter 3" runs the quiz skill).

### `/study:study-mode`: Socratic tutoring

```text
/study:study-mode
Help me with this problem: 3x + 7 = 22
```

Claude asks what you'd undo first instead of answering "x = 5". Say "stop studying" to turn it off.

### `/study:course`: create and switch courses

```text
/study:course new AP Chemistry
/study:course exam Unit 4 test 2026-11-20
/study:course switch bio-101
/study:course list
```

### `/study:ingest`: add your materials

```text
/study:ingest lecture3.pdf
/study:ingest photo-of-my-notes.jpg
/study:ingest https://www.youtube.com/watch?v=VIDEO_ID
/study:ingest https://en.wikipedia.org/wiki/Photosynthesis
```

Each source gets an ID (`S1`, `S2`, ...) and location anchors, so later answers can cite `[S1 p.3]`, `[S2 slide 5]` or `[S4 12:34]`. Claude builds a topic list and asks you to correct it.

### `/study:transcribe`: lecture recordings

```text
/study:transcribe lecture-5.m4a
/study:transcribe seminar.mp4 --language pt
```

Runs Whisper on your own computer and saves a timestamped transcript, then offers to turn it into notes. See [Limitations](#limitations): there's no live recording.

### Chat with your materials

Just ask:

```text
Why does the Calvin cycle need NADPH?
What does my lecture say about limiting factors?
```

Answers come from your sources first, with citations. Anything else is marked *From general knowledge (not in your materials)*.

### `/study:notes`: rich notes

```text
/study:notes photosynthesis
/study:notes S3
```

### `/study:quiz`: adaptive quizzes

```text
/study:quiz photosynthesis
/study:quiz everything for the midterm, 20 questions
```

Short rounds run in the chat. Longer quizzes come as a self-contained HTML file: take it on your phone, then tap **Copy results for Claude** and paste them back so they're logged.

### `/study:flashcards`: cards with spaced repetition

```text
/study:flashcards calvin cycle
/study:flashcards export to Anki
```

You get the deck, a flip-card app (`.html`) that schedules reviews with FSRS, and Anki CSV files (**File → Import** in Anki 2.1.55+).

### `/study:podcast`: listen and review

```text
/study:podcast photosynthesis, 6 minutes
```

### `/study:exam-plan`: day-by-day schedule

```text
/study:exam-plan final on 2026-12-10, 1.5 hours a day, no studying on Sundays
```

### `/study:weak-spots`: what to study next

```text
/study:weak-spots
```

### `/study:mock-exam`: timed practice exam

```text
/study:mock-exam AP Biology, full length
/study:mock-exam midterm, half length
```

### `/study:past-paper`: learn an exam's style

```text
/study:past-paper 2024-final.pdf, then 10 new questions in that style
```

### `/study:explain-like`: change the level

```text
/study:explain-like ELI5 electron transport chain
/study:explain-like university entropy
```

### `/study:feynman`: explain it back

```text
/study:feynman the Calvin cycle
```

### `/study:cheatsheet`: one page for the final review

```text
/study:cheatsheet for the final, printable
```

### `/study:review-mistakes`: clear your error log

```text
/study:review-mistakes
/study:review-mistakes calvin cycle
```

## Your course folder

Everything is saved as plain files in your working folder, so you can read, back up or version them:

```text
study/
├── courses.json              your courses and which one is active
└── bio-101/
    ├── course.json           topics, exams
    ├── sources/              S1-..., S2-... extracted with anchors, plus index.json
    ├── notes/                one file per topic
    ├── decks/                flashcard decks (.json, .html, Anki .csv)
    ├── quizzes/              history.jsonl and HTML quizzes
    ├── mock-exams/           timed exams and results
    ├── errors.jsonl          your error log
    ├── plans/                exam plans
    ├── podcasts/             podcast scripts
    └── cheatsheet.md
```

The formats are documented in [`skills/course/reference/layout.md`](skills/course/reference/layout.md).

## Optional Python tools

Claude can read PDFs and images by itself. These help with other formats (Python 3.9+; install only what you need):

```bash
pip install pypdf python-docx python-pptx youtube-transcript-api
```

```bash
pip install faster-whisper
```

- `pypdf`, `python-docx`, `python-pptx`: text extraction with page and slide anchors.
- `youtube-transcript-api`: YouTube captions with timestamps.
- `faster-whisper`: local lecture transcription (or `openai-whisper` plus ffmpeg). The first run downloads the model (tiny ~75 MB, small ~500 MB).
- The Anki exporter needs nothing extra.

Claude asks before installing anything.

## Limitations

- **No live recording.** Claude can't listen to a class as it happens. Record the lecture with your phone or laptop (where your school allows it), then upload the file and use `/study:transcribe`.
- **Text-to-speech needs a tool.** `/study:podcast` writes the script. It becomes audio only if a text-to-speech tool is connected to Claude, or if you paste the script into a TTS app (Claude suggests free options, including ones built into macOS and Windows).
- **AI can make mistakes. Always verify.** Citations make checking easy, but Claude can still misread a source, mis-transcribe a word or get an answer key wrong. Check anything important against your materials, your textbook or your teacher.
- **Mock exam scores are estimates.** They're percentages on practice questions, not official SAT, AP, IB or ENEM scores.
- **Exam guides are outlines.** Formats change (several AP exams change in May 2027). Check the official pages linked in each guide.
- **Flashcard progress lives in your browser.** Use **Export progress** in the flashcard app to back it up or move it to another device.
- **Chat without file access** can't keep a course folder between conversations; Claude gives you the files to download instead.

## Academic integrity

Studying with Claude is here to help you **learn**: understand the material, practice, find your gaps and walk into the exam prepared.

It won't complete graded assignments, write essays or lab reports you'll hand in as your own, answer take-home exams, or help during a live test. If you ask, Claude will say so kindly and offer something that actually helps you learn the material instead. Please follow your school's rules on AI use, including any requirement to say when you've used it.

## Privacy

- Your materials and course files stay in your own folder. The plugin has no server and collects nothing.
- Transcription runs locally with Whisper; recordings aren't uploaded anywhere.
- Claude reads the files you give it as part of your normal conversation with Claude, under your Claude account's terms.
- The HTML apps work offline. When a page contains math, it loads the KaTeX library from a public CDN (cdnjs) to render it; without internet the raw formula is shown instead.

## Development

```text
studying-with-claude/
├── .claude-plugin/
│   ├── plugin.json           plugin manifest (id "study", display name "Studying with Claude")
│   └── marketplace.json      single-plugin marketplace for this repository
├── skills/                   18 skills, each a slash command (/study:<name>)
│   └── <name>/SKILL.md       plus scripts/, assets/ (HTML templates), reference/, guides/
├── agents/                   source-checker, exam-grader
├── examples/photosynthesis/  sample input and real outputs
├── README.md
└── LICENSE
```

Test a local copy without installing it:

```bash
claude --plugin-dir ./studying-with-claude
```

Validate before publishing:

```bash
claude plugin validate . --strict
```

Contributions are welcome, especially exam guides for more exams (follow the shape in [`skills/exam-guides/SKILL.md`](skills/exam-guides/SKILL.md)), translations, and fixes to the HTML templates. Keep every guide original: no copied textbook or exam content.

## License and credits

[MIT](LICENSE) © 2026 Filhao2019.

- Spaced repetition uses the FSRS-4.5 algorithm and default parameters from the open-source [open-spaced-repetition](https://github.com/open-spaced-repetition) project.
- Transcription uses [faster-whisper](https://github.com/SYSTRAN/faster-whisper) or [OpenAI Whisper](https://github.com/openai/whisper).
- Math in the HTML apps is rendered with [KaTeX](https://katex.org).

Studying with Claude is an independent community project. It isn't affiliated with or endorsed by Anthropic. AP and SAT are trademarks of the College Board; IB is a trademark of the International Baccalaureate Organization; ENEM is administered by INEP. Anki is an independent open-source project. None of them is affiliated with this plugin.
