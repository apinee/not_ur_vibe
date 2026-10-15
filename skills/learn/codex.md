# Codex Platform Adaptation

When running in **OpenAI Codex**:

## 1. Commands & Invocation
- Slash commands become dollar commands: `/learn` is `$learn`, `/reset` is `$reset`, `/review` is `$review`.
- Session resumes when `$learn` is invoked.

## 2. Environment Variables & Paths
- `${CLAUDE_PLUGIN_ROOT}` is not expanded in Codex. Guides are resolved relative to the skill location (`skills/learn/`).
- Use native file reading and grep tools to inspect `.vibewise/profile.md` and `progress.md`.

## 3. Interactive Prompts
- If `request_user_input` is available, use it for single-question choices.
- Otherwise, format a clear markdown numbered list and end your turn to await the learner's response.
- Do not make assumptions or write code before receiving explicit approval at the `✦ Implementation checkpoint`.
