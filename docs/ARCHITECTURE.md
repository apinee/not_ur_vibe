# Architecture & Technical Design

**Not Your Vibe** is engineered to be a universal, zero-dependency, multi-agent framework.

```
                      ┌──────────────────────────────────────────────┐
                      │                 USER (Lead)                  │
                      └──────────────────────┬───────────────────────┘
                                             │
                          Architects & Prompts
                                             ▼
                      ┌──────────────────────────────────────────────┐
                      │              AI Pair Programmer              │
                      │  (Antigravity / Claude / Codex / Cursor)     │
                      └───────┬───────────────────────────────▲──────┘
                              │                               │
             1. Checks & Reads│                               │ 6. Writes State
                              ▼                               │
                      ┌─────────────────┐             ┌───────┴──────┐
                      │ Session Hook /  │             │ .vibewise/   │
                      │ Master Rules    ├────────────►│ - profile.md │
                      │ (AGENTS.md)     │             │ - progress.md│
                      └───────┬─────────┘             │ - map.md     │
                              │                       └──────────────┘
                              │
                              │ 2. Build Checkpoint (Asks user's approach)
                              │ 3. Concept & Analogy (Teaches with physical metaphor)
                              │ 4. Security Radar (Audits OWASP risks)
                              │ 5. Codex Code Review Gate (Senior peer review)
                              │
                              ▼
                      ┌─────────────────┐
                      │ Implementation  │
                      │ & Verified Code │
                      └─────────────────┘
```

---

## 1. Zero-Dependency Foundation

The entire framework requires **zero third-party packages**.
- Python automation (`hooks/session_start.py`, `scripts/reset.py`, `scripts/doctor.py`) uses purely Python Standard Library modules (`pathlib`, `hashlib`, `json`, `os`, `re`, `tempfile`).
- Compatible with all platforms: Windows, macOS, Linux.

---

## 2. Cross-Agent Abstraction Layer

| Platform | Discovery Mechanism | Execution Hook / Directives | Commands |
| :--- | :--- | :--- | :--- |
| **Google Antigravity** | `.agents/skills/` | `AGENTS.md`, `GEMINI.md`, native tools | `/learn`, `/reset`, `/review` |
| **Claude Code** | `.claude-plugin/plugin.json` | `hooks/hooks.json` (`SessionStart`) | `/learn`, `/reset` |
| **OpenAI Codex** | `.codex-plugin/plugin.json` | `skills/*/agents/openai.yaml` | `$learn`, `$reset`, `$review` |
| **Cursor / Windsurf** | `.cursor/rules/*.mdc` | `.cursorrules`, `.windsurfrules` | Interactive chat checkpoints |

---

## 3. State Management & Lifecycle

- State is kept in `.vibewise/`:
  - `profile.md`: Current learner preferences, stack familiarity, and concepts mastered.
  - `progress.md`: Chronological log of concepts introduced, demonstrations of understanding, and pending decisions.
  - `project-map.md`: Compact ASCII/text map of components, responsibilities, and data boundaries.
- **Atomic Reset & Backup**: `scripts/reset.py` creates a timestamped snapshot in `.vibewise/backups/reset-YYYYMMDDTHHMMSSZ/` before writing fresh files. Zero data loss.
