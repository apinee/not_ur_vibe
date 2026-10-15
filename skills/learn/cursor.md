# Cursor Platform Adaptation

When running in **Cursor** (or **Windsurf**):

## 1. Rules & Configuration
- Cursor loads rules from `.cursor/rules/*.mdc` and the workspace `.cursorrules`.
- In Chat (`Cmd+L` / `Ctrl+L`) or Composer (`Cmd+I` / `Ctrl+I`), learning mode is governed by these rules.

## 2. Composer / Agent Behavior
- Cursor Composer frequently attempts to auto-apply code edits across multiple files simultaneously.
- **Under Learning Mode**: The agent must **NOT** generate file diffs or click "Apply" until the user has passed through the `✦ Build checkpoint` and confirmed the `✦ Implementation checkpoint`.
- Keep conversational guidance in chat, showing real-world analogies, security checks, and design trade-offs before invoking Composer edits.
