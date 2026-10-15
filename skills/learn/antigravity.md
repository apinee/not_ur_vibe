# Antigravity Platform Adaptation

When running in **Google Antigravity (AGY)**:

## 1. Skill Invocations & Commands
- Learning mode can be triggered via slash command `/learn` or natural language prompt.
- Antigravity loads skills from `.agents/skills/` in the workspace or `skills/` in global config.
- When asking multiple choice questions during onboarding or checkpoints, use `AskQuestion` if available, or present formatted markdown choice blocks with clear numerical keys.

## 2. Tool Execution Rules
- Use workspace tools (`run_command`, `write_to_file`, `replace_file_content`, `view_file`, `list_dir`) rather than raw shell commands whenever possible.
- Run commands inside the Standard Sandbox by default; only bypass when network is genuinely required.

## 3. Communication Style
- Keep responses dense and well-formatted with markdown headers and tables.
- Always provide clickable GitHub-style markdown links for files (e.g. `[src/index.js](file:///d:/SRDP/not_ur_vibe/src/index.js)`).
- Preserve the 6 core pillars: Learner Ownership, Real-World Analogies, Problem Diagnosis, Token Optimization, Security Radar, and Codex Review Gate.
