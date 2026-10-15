# Local State Templates

Store learning notes in `.vibewise/` (or `.vibe-wise/`, `.not-ur-vibe/`). These files keep context compact, structured, and token-optimized across restarts.

---

## 1. profile.md

```markdown
# Learner Profile

Learning mode: active
Onboarding: complete

## Project Context
Situation: [New / Existing / Exploratory]
Building: [One-sentence summary of project purpose]
Learning scope: [Entire system / Target feature / Core architecture]

## Experience & Preferences
Programming experience: [Beginner / Intermediate / Advanced]
Stack familiarity: [Details on technologies]
Checkpoint pacing: [Light / Normal / Frequent]
Analogy style: Junior Software Engineer (Real-World Physical Analogies)

## Mastered Concepts
- None recorded yet.

## In-Progress Concepts
- None recorded yet.

## Security & Architecture Checklist
- [x] Security radar active (OWASP Top 10 checks)
- [x] Codex code review gate enabled
- [x] Token-efficient state tracking
```

---

## 2. progress.md

```markdown
# Learning Progress

No learning events recorded yet.

## Pending Decision
None.
```

### Event Logging Format
When a milestone or concept is mastered, append a concise topic entry:
```markdown
## Topic: [e.g., Database Persistence & File Sanitization]
- **Introduced**: Disk vs. Memory persistence.
- **Analogy**: Whiteboard (RAM) vs. Metal Filing Cabinet (Disk).
- **Demonstrated Understanding**: Learner chose local JSON files with path traversal checks.
- **Security Check**: Handled sanitized filenames (`path.basename`) to prevent directory traversal.
- **Codex Review**: Clean error handling, verified edge cases.
```

---

## 3. project-map.md

```markdown
# Project Map

## Purpose
[High-level summary of what this software accomplishes.]

## Architecture & Components
- **Component 1**: Responsibility, file path.
- **Component 2**: Responsibility, file path.

## Data & Trust Boundaries
- **Storage**: [Where and how data is kept].
- **Auth & Access**: [Permissions, public vs. authenticated routes].
- **External Dependencies**: [Third-party APIs, SDKs, or databases].

## Current Flow
```
[User Input] --> [Router / API] --> [Business Logic] --> [Storage]
```

## Security Radar & Quality Considerations
- Input validation boundaries.
- Error reporting without leaking stack traces or secrets.
```
