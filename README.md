<p align="center">
  <img src="assets/logo.svg" alt="Not Your Vibe Logo" width="128" height="128" />
</p>

<h1 align="center">Not Your Vibe</h1>

<p align="center">
  <strong>You Architect. AI Mentors, Audits & Writes.</strong><br>
  The universal learning-first AI pair programming framework for <strong>Google Antigravity</strong>, <strong>Claude Code</strong>, <strong>OpenAI Codex</strong>, and <strong>Cursor</strong>.
</p>

<p align="center">
  <a href="https://github.com/nykooi1/vibe-wise/actions"><img src="https://img.shields.io/badge/CI-Passing-success?style=flat-square&logo=githubactions" alt="CI Status" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=flat-square&logo=python&logoColor=white" alt="Python 3.8+" /></a>
  <a href="https://nodejs.org/"><img src="https://img.shields.io/badge/Node-npx_ready-339933.svg?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node Ready" /></a>
  <a href="https://owasp.org/www-project-top-ten/"><img src="https://img.shields.io/badge/Security-OWASP_Radar-red.svg?style=flat-square" alt="Security Radar" /></a>
</p>

---

## What is Not Your Vibe?

In standard "vibe coding", the AI generates hundreds of lines of code while the developer cannot explain how or why it works. When the code breaks, the developer is stranded.

**Not Your Vibe** turns this on its head:
1. **You own the design**: The AI asks for your architectural approach first.
2. **Taught like a junior engineer**: Every unfamiliar computer science concept is grounded in an **intuitive, physical real-world analogy** before code is written.
3. **Root-cause problem fixing**: When bugs occur, the AI explains the *root cause*, gives a *failure analogy*, and shows the *fix*.
4. **Token-efficient communication**: Zero repetitive boilerplate dumps; compact local state files.
5. **Continuous security radar**: Proactive OWASP Top 10 auditing for injections, secrets, auth boundaries, and traversal.
6. **Codex peer review gate**: Every implementation passes through a simulated senior staff / Codex code review before being stamped complete.

---

## Quickstart & Installation

Download and install into any project with **one command**:

### 1. via NPX (Any OS)
```sh
npx not-ur-vibe init
```

### 2. via Curl (macOS / Linux)
```sh
curl -fsSL https://raw.githubusercontent.com/nykooi1/vibe-wise/main/scripts/install.sh | bash
```

### 3. via PowerShell (Windows)
```powershell
irm https://raw.githubusercontent.com/nykooi1/vibe-wise/main/scripts/install.ps1 | iex
```

### 4. via Python (Zero Dependencies)
```sh
python install.py
```

---

## Supported AI Platforms

### Google Antigravity (AGY)
- Built-in skills under `.agents/skills/` and `skills/`.
- In Antigravity chat, run:
  ```text
  /learn
  ```
- Use `/reset` to clear learning state with backups, or `/review` for an on-demand Codex code review.

### Claude Code
- Full `.claude-plugin/` integration with automatic `SessionStart` context restoration.
- Install via Claude plugin command:
  ```text
  /plugin marketplace add nykooi1/vibe-wise
  /plugin install vibe-wise@vibe-wise
  ```
- Run `/vibe-wise:learn` or `/learn`.

### OpenAI Codex
- Plugin manifests and agent definitions under `.codex-plugin/` and `skills/*/agents/openai.yaml`.
- Run:
  ```sh
  codex plugin marketplace add nykooi1/vibe-wise
  codex plugin add vibe-wise@vibe-wise
  ```
- Start Codex and invoke `$learn`.

### Cursor & Windsurf
- Native `.cursor/rules/*.mdc` rules and `.cursorrules` / `.windsurfrules`.
- Simply open your project in Cursor; the learning directives are active immediately!

---

## What It Feels Like (Example Session)

**Scenario**: You are building a private note-taking application.

```text
YOU:
I want notes to be stored on disk so they don't vanish on server restart.

AI:
✦ Build checkpoint: Choosing Storage Architecture

We need durable persistence. How would you like to structure this storage?
Would you prefer plain JSON files on disk, or a lightweight database like SQLite?

✦ Concept & Analogy: RAM vs. Disk
Imagine RAM (memory) is like a whiteboard on your office wall: fast to scribble on,
but wiped clean every night. Disk storage is like a metal filing cabinet: it takes
an extra moment to slide a drawer open, but it stays intact even during a blackout.

YOU:
Let's store each note as a JSON file in a data/ folder using its ID.

AI:
✦ Design checkpoint: Local JSON Files
Approach: Store each note as `data/{id}.json`.
Trade-offs: Zero external database dependencies, but slower searching across thousands of notes.

✦ Security radar: Path Traversal Vulnerability
If an attacker sends an ID like `../../etc/passwd`, they could overwrite sensitive files!
We must sanitize the ID with `path.basename` to prevent traversal attacks.

✦ Implementation checkpoint: Storage Module
Scope: Create `src/storage.js` with sanitized note read/write methods and unit tests.

Options:
1. Implement this step (Authorize writing code)
2. Discuss (Adjust design or explore alternatives)
```

After you confirm:

```text
AI:
✦ Codex review: Storage Module
- Correctness: Pass. Verified synchronous flush guarantees data on disk.
- Security: Pass. `path.basename` eliminates directory traversal.
- Robustness: Handled non-existent directories with recursive creation.
- Grade: Production Ready.

✦ Implementation report: Storage Implemented
- Files created: `src/storage.js`, `tests/test_storage.js`.
- Tests: 3 passed, 0 failed.
- Concept Mastered: Disk durability and path traversal sanitization.
```

---

## State Architecture

Learning progress and project maps are stored in a local `.vibewise/` folder:
- **`profile.md`**: Your experience level, stack familiarity, and concepts mastered.
- **`progress.md`**: A chronological record of topics introduced and demonstrated understanding.
- **`project-map.md`**: A high-level architectural component map.
- **`backups/`**: Safe, timestamped snapshots created automatically before resets.

*(This folder is added to `.gitignore` so your notes remain private to your machine.)*

---

## Testing & Diagnostics

Verify your setup with the built-in doctor:
```sh
python scripts/doctor.py
```

Run unit tests:
```sh
python -m unittest discover tests
```

Export your learning notes to a portfolio summary:
```sh
python scripts/export_notes.py
```

---

## License

Released under the [MIT License](LICENSE). Contributions, new analogies, and agent integrations are welcome!
