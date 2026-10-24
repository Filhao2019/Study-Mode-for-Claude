# Contributing

Thanks for helping make Studying with Claude better! 🎓

## Ways to help

- **Report behavior issues** — open an issue with the prompt you used, what Claude did, and what a good tutor would have done instead.
- **Improve a skill** — each lives in [`skills/<name>/SKILL.md`](skills/); Study Mode is [`skills/study-mode/SKILL.md`](skills/study-mode/SKILL.md). Explain *why* a behavior matters rather than adding rigid ALWAYS/NEVER rules; Claude follows reasoning better than commands.
- **Add examples** — new sample conversations in [`examples/`](examples/) for different subjects and levels.
- **Add an exam guide** — follow the shape in [`skills/exam-guides/SKILL.md`](skills/exam-guides/SKILL.md). Original wording only, no copied textbook or exam content.
- **Translate** the README.

## Guidelines

- Keep each `SKILL.md` focused and under ~500 lines, with frontmatter limited to `name` and `description` so it also loads in Claude Desktop chat and Cowork.
- Run `claude plugin validate . --strict` before opening a PR.
- Don't add behavior that hands out homework answers by default — the point is learning.
- After editing `skills/study-mode/SKILL.md`, rebuild the standalone upload zip:

  ```bash
  ./scripts/build.sh
  ```

- Bump the version in `.claude-plugin/plugin.json` and add a line to [`CHANGELOG.md`](CHANGELOG.md).

## Pull requests

1. Fork the repo and create a branch.
2. Make your change and test it in Claude with a few real study prompts.
3. Open a PR describing what changed and why.
