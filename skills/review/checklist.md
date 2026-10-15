# Senior Engineering & Codex Code Review Checklist

Use this checklist during `✦ Codex review` gates to ensure high standards of craftsmanship and security.

---

## 1. Security Radar (Critical)

- [ ] **No Hardcoded Secrets**: No passwords, private keys, API secrets, or sensitive tokens in source code.
- [ ] **Input Sanitization**: All external input (HTTP query, body, CLI args, file inputs) validated and sanitized.
- [ ] **Path Traversal Defense**: File operations use `path.basename` or explicit whitelist directory checks.
- [ ] **Injection Defense**: SQL queries use prepared statements; shell executions avoid arbitrary string concatenation.
- [ ] **Safe Deserialization**: No untrusted `eval()`, `pickle.loads()`, or unrestricted YAML/JSON execution.

---

## 2. Robustness & Error Handling

- [ ] **Graceful Failure**: Errors logged or handled cleanly; no crashing on predictable errors (e.g., missing file, network drop).
- [ ] **Resource Cleanup**: Streams, files, database connections, and event listeners properly closed in `finally` blocks or using context managers (`with`, `using`).
- [ ] **Idempotency**: Retrying a failed operation does not duplicate records or corrupt data.
- [ ] **Boundary Testing**: Empty collections, zero values, extreme bounds, and unicode inputs handled properly.

---

## 3. Readability & Maintainability

- [ ] **Naming Clarity**: Variables and functions describe their behavior accurately without cryptic abbreviations.
- [ ] **Single Responsibility**: Each function performs one clear task.
- [ ] **Self-Documenting Code**: Code structure speaks for itself; comments explain *why*, not *what*.
- [ ] **Consistency**: Follows established idioms of the host language (PEP 8 for Python, ESLint/Prettier for JS/TS, Effective Go for Go, etc.).

---

## 4. Performance & Token Efficiency

- [ ] **Algorithmic Efficiency**: No accidental nested iterations ($O(N^2)$) on large datasets.
- [ ] **Memory Footprint**: Large files streamed line-by-line rather than loaded entirely into memory.
- [ ] **Caching**: Expensive repeat operations cached appropriately.
