---
name: transcribe
description: Transcribe an uploaded lecture recording (audio or video file such as .mp3, .m4a, .wav, .mp4, .mov) on the student's own computer with a local Whisper model, producing a timestamped transcript saved as a course source, then hand off to notes. Use when the student has a recording of a class, lecture, seminar or study session and wants it as text, notes or study material. Not for documents, slides or YouTube links (use ingest).
---

# Transcribe lecture recordings

Turn a recording the student uploads into a **timestamped transcript** that later notes, quizzes and flashcards can cite as `[S7 12:34]`. Whisper runs locally, so the audio never leaves the student's computer.

**Live recording isn't possible.** Claude can't listen to a class as it happens. The student records with their phone or laptop (voice memo app, camera, or the course's own lecture capture) and uploads the file afterwards.

## Before you start

1. **Permission.** If the student recorded the class themselves, remind them once, briefly, to follow their school's recording rules and the lecturer's wishes. Don't block them.
2. **Find the file** and the active course (`study/courses.json`). Give the transcript the next free source ID (`S<n>`).
3. **Check that Python and an engine are available.** Run the script; exit code 2 means no engine is installed. Ask before installing anything, then suggest:
   - `pip install faster-whisper` (recommended: reads audio and video directly, no ffmpeg needed)
   - or `pip install openai-whisper` (also needs ffmpeg on the PATH)
   The first run downloads the model (tiny ~75 MB, small ~500 MB, large-v3 ~3 GB).

## Run it

```bash
python "${CLAUDE_SKILL_DIR}/scripts/transcribe.py" "<recording>" --id S7 --title "Lecture 5: Photosynthesis" --out-dir "study/<course>/sources" --name "S7-lecture-5"
```

- Use `python3` on macOS and Linux if `python` isn't found.
- `--model`: `small` is the default and a good balance. Use `tiny` or `base` for a quick draft on a slow laptop, and `medium` or `large-v3` when accuracy matters (technical vocabulary, accents, noisy rooms). On a CPU, `small` takes very roughly a third to the full length of the recording.
- `--language pt` (or `en`, `es`, ...) skips language detection and helps with short or noisy clips.
- Long recordings take a while. In Claude Code, run the command in the background and tell the student roughly how long to expect.

Outputs, next to each other: `S7-lecture-5.md` (timestamped paragraphs), `.srt` subtitles and `.json` segments.

## After transcribing

1. **Register the source** in `study/<course>/sources/index.json`: `type` `audio` or `video`, `kind` `transcript`, `original` the recording's path, and `notes` with the model used.
2. **Skim the transcript for problems** and tell the student about them instead of silently fixing: misheard technical terms, names, numbers and formulas, silent or noisy stretches. Fix a term only when the course materials make the correct word unambiguous, and say which ones you changed.
3. **Update the topic list** in `course.json` with what the lecture covered, using timestamp ranges as anchors (`"S7 05:10-18:40"`).
4. **Hand off to notes.** Offer to turn the transcript into rich notes (`/study:notes`). Spoken lectures are full of hints about what's examinable ("this will be on the exam", "make sure you know...", repetition), so tell the notes skill to look for them.

## Quality rules

- **Accuracy over speed.** A transcript is only as good as the audio. Never invent words for inaudible parts; leave them marked as unclear, and flag anything that looks misheard.
- **Cite timestamps.** Facts taken from a recording cite `[S7 mm:ss]` so the student can jump to that moment and listen.
- **Privacy.** Transcription is local. Don't upload the recording anywhere, and don't share transcripts of other people's voices beyond the student's own study.
- **Active recall.** End by offering notes, then a quiz or flashcards on the lecture.
- **Academic integrity.** Transcribing a lecture to study it is fine. Don't use it to complete graded work for the student.
