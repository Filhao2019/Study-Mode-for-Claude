# 📚 Study Mode for Claude

**Studying with Claude** — a free, open-source skill that turns Claude into a patient, Socratic tutor. Instead of handing you answers, Claude asks guiding questions, gives hints, explains in layers, and checks that ideas actually stick.

It's modelled feature-for-feature on ChatGPT's Study Mode ("Study and learn"), rebuilt as a [Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) so it works in Claude.ai, the Claude apps, Claude Code and the API.

> Learn something — not just finish something.

---

## ✨ Features

| Feature | What Claude does |
|---|---|
| **Toggle on/off** | Say `/study-mode`, "let's study" or "turn on study mode". It stays on for the whole chat until you say "stop studying". |
| **Interactive prompts** | Socratic questions, hints and self-reflection prompts — one question at a time. |
| **Hint ladder** | Stuck? Nudge → specific hint → partial step → worked *similar* example. |
| **Scaffolded responses** | A roadmap for big topics, then one digestible chunk at a time, simple first and deeper later. |
| **Knowledge checks** | Teach-back, apply-it questions, multiple choice, open-ended questions, with specific feedback. |
| **Progress tracking** | Recaps of what's solid, what's shaky, and what to do next. |
| **Homework-safe** | Won't solve your problem or write your essay for you — walks you through it instead. |
| **Your materials** | Works from your notes, slides, PDFs, syllabus or a photo of the problem, and cites pages. |
| **Study plans** | Turns a syllabus or a test date into a day-by-day plan, weakest topics first. |
| **Quizzes & flashcards** | Inline one-at-a-time quizzes, or Claude's quiz/flashcard cards where available. |
| **Adaptive pace** | "Slower", "simpler", "harder", "edge cases" — and it reads your answers to adjust on its own. |
| **Personalization** | Uses Claude's memory and past chats when they're on. |
| **Visuals & voice** | Diagrams when they help; shorter, spoken-friendly turns in voice mode. |

See [`examples/`](examples/) for sample conversations.

---

## 🚀 Install

### Claude.ai / Claude desktop & mobile apps

1. Download **[`study-mode.zip`](dist/study-mode.zip)** from this repo (or the latest [release](../../releases)).
2. In Claude, open **Settings → Capabilities → Skills** and upload the zip.
3. Start a chat and say **"turn on study mode"** or type `/study-mode`.

*(Skills need to be enabled for your account or organization.)*

### Claude Code — as a plugin

```bash
/plugin marketplace add Filhao2019/Study-Mode-for-Claude
/plugin install study-mode@study-mode-for-claude
```

### Claude Code — as a plain skill

```bash
git clone https://github.com/Filhao2019/Study-Mode-for-Claude.git
mkdir -p ~/.claude/skills
cp -r Study-Mode-for-Claude/skills/study-mode ~/.claude/skills/
```

### Claude API / Agent SDK

Upload `skills/study-mode/` as a custom skill, or paste the body of [`SKILL.md`](skills/study-mode/SKILL.md) into your system prompt.

---

## 💬 Try it

- *"Turn on study mode. I'm in first-year biology with an exam on enzymes next week — quiz me one question at a time."*
- *"Let's study. I keep getting stuck factoring quadratics."*
- *"I uploaded my class notes. Make me a study plan for Friday's test."*
- *"I know the answer is B but I don't get why."*
- *"I've got 20 minutes to review the French Revolution. Go."*

Say **"stop studying"** to go back to normal answers.

---

## 🔁 Compared with ChatGPT Study Mode

| ChatGPT Study Mode | Study Mode for Claude |
|---|---|
| "Study and learn" in the Tools menu | `/study-mode` or "turn on study mode" |
| Toggle off in Tools | "stop studying" |
| Socratic prompts, hints, self-reflection | ✅ Same, plus a hint ladder |
| Scaffolded responses | ✅ Roadmaps and layered explanations |
| Knowledge checks with feedback | ✅ Plus progress recaps |
| Works with uploaded files and images | ✅ |
| Memory personalization | ✅ When Claude's memory is on |
| Quizzes shortcut | ✅ Inline quizzes or Claude's quiz cards |
| Parent/admin can make it the default | ❌ Not possible for a skill |
| `chatgpt.com/studymode` direct link | ❌ Use `/study-mode` instead |

---

## ⚠️ Limitations

- Claude can still make mistakes. Double-check anything important, especially for exams.
- It's guidance written in plain language, not a hard filter — a determined user can talk it into giving answers.
- For graded work, follow your school's or instructor's AI-use rules.
- It's a study aid, not a replacement for your teacher or course materials.

---

## 🤝 Contributing

Ideas, fixes and translations are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Fork it, remix it, make it yours.

## 📄 License

[MIT](LICENSE) — free to use, copy, modify and share.

---

<sub>Not affiliated with, endorsed by, or sponsored by Anthropic or OpenAI. "Claude" is a trademark of Anthropic; "ChatGPT" is a trademark of OpenAI.</sub>
