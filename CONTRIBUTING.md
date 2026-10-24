# Contributing

Thanks for helping make Studying with Claude better! 🎓

## Ways to help

- **Report behavior issues** — open an issue with the prompt you used, what Claude did, and what a good tutor would have done instead.
- **Improve the skill** — edit [`skills/study-mode/SKILL.md`](skills/study-mode/SKILL.md). Explain *why* a behavior matters rather than adding rigid ALWAYS/NEVER rules; Claude follows reasoning better than commands.
- **Add examples** — new sample conversations in [`examples/`](examples/) for different subjects and levels.
- **Translate** the README.

## Guidelines

- Keep `SKILL.md` focused and under ~500 lines.
- Don't add behavior that hands out homework answers by default — the point is learning.
- After editing `SKILL.md`, rebuild the upload zip:

  ```bash
  ./scripts/build.sh
  ```

- Bump the version in `.claude-plugin/plugin.json` and add a line to [`CHANGELOG.md`](CHANGELOG.md).

## Pull requests

1. Fork the repo and create a branch.
2. Make your change and test it in Claude with a few real study prompts.
3. Open a PR describing what changed and why.
