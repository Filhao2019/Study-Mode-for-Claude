---
name: podcast
description: Write a 5 to 10 minute two-host conversational review podcast script (a host who explains and a curious student who asks questions) from the student's notes or materials, and turn it into audio when a text-to-speech tool is available. Use when the student asks for a podcast, audio review, something to listen to on the bus or at the gym, an audio summary, or a script for text-to-speech.
---

# Review podcast

A short, friendly conversation that reviews one topic for listening on the go. It teaches through dialogue: the student character asks the questions a real student would, gets things slightly wrong, and gets corrected.

## Inputs

- **Topic:** from notes in `study/<course>/notes/` (best) or the sources. If there are no notes yet, build from the sources and say so.
- **Length:** default about 7 minutes. At roughly 150 spoken words a minute, 5 minutes is about 750 words and 10 minutes about 1,500.
- **Hosts:** default **Maya** (host, explains clearly and warmly) and **Leo** (curious student, asks, guesses and summarizes). Use other names if the student wants. Write in the student's language.

## Script structure

1. **Cold open (15 s):** a hook question or surprising fact from the material.
2. **Roadmap (15 s):** what this episode covers, in three points.
3. **Three or four segments**, one per core idea, each with:
   - Leo asks a natural question; Maya explains it simply, then precisely.
   - One concrete example or analogy.
   - Leo restates it in his own words (sometimes with a mistake that Maya corrects kindly; use the error log's real misconceptions when there are any).
4. **Misconception corner (30 s):** the most common mistake on this topic and how to avoid it.
5. **Quick-fire recall (60 s):** Maya asks the listener three or four questions. After each, write `[pause 3 seconds]`, then the answer.
6. **Recap (20 s):** the three things to remember, then a sign-off suggesting a quiz.

## Writing for the ear

- Short sentences. One idea at a time. No tables, bullet lists, citations or symbols read aloud.
- Say formulas and units in words: "six C O two plus six H two O" for 6CO₂ + 6H₂O, "meters per second squared".
- Name things instead of pointing: "the Calvin cycle", never "this one" or "as you can see".
- Keep it natural with light reactions ("Wait, so...", "Exactly."), but no filler and no fake banter.
- Speaker labels on their own lines: `MAYA:` / `LEO:`. Stage directions in square brackets: `[pause 3 seconds]`.

## Output

Save to `study/<course>/podcasts/<topic-slug>.md`:

```markdown
# Podcast: <Topic> (about 7 min)

MAYA: ...
LEO: ...

---
## Show notes (not read aloud)
- Sources used: S1 ¶2-¶9, S3 05:10-18:40
- Fact check: every claim in the script, with its citation
  - "Water is split to release oxygen" [S1 ¶5]
```

The show notes keep the script accurate and traceable without cluttering the audio.

## Turning it into audio

- **If a text-to-speech or audio-generation tool is available in this session**, ask the student before using it (it may cost credits or upload the text). Generate each speaker with a different voice, keep `[pause]` directions as real pauses if the tool supports them (else drop them), and tell the student where the audio file is.
- **If not**, give the script and explain how to convert it:
  - Paste it into any text-to-speech app or reader (most phones have one built in), or a two-voice podcast tool.
  - Free and offline on a computer: `say -f script.txt -o review.aiff` on macOS; Windows Narrator, or PowerShell's built-in speech synthesizer; Piper on Linux, macOS or Windows.
  - For two voices, split the script by speaker, generate each part, and join them in any audio editor.
  - Delete the `MAYA:`/`LEO:` labels first if the tool would read them out.

## Quality rules

- **Accuracy over speed.** Every claim in the script must come from the student's notes or sources and be listed in the show notes with its citation. Simplify, but never so much that it becomes wrong. Mark anything from general knowledge in the show notes.
- **Active recall.** The quick-fire round is required, and always end by offering a quiz or flashcards on the episode's topic.
- **Academic integrity.** A podcast is a review aid; don't script graded presentations or oral exams for the student to read out as their own.
- **Study Mode.** If Study Mode is on, after delivering the script, ask one recall question about it.
