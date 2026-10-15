---
name: review
description: Run an adversarial, senior software engineer / Codex code review against recent code changes. Checks security, edge cases, performance, and maintainability.
disable-model-invocation: true
---

# Not Your Vibe: Codex Code Review Gate

Perform a simulated senior staff software engineer / Codex code review before committing or declaring an implementation complete.

## Review Pillars

1. **Security Vulnerabilities (OWASP Top 10)**:
   - Are SQL queries parameterized?
   - Is user input sanitized against XSS, command injection, and path traversal?
   - Are secrets or API keys hardcoded?
   - Are authorization and authentication boundaries enforced?
2. **Correctness & Edge Cases**:
   - What happens with `null`, `undefined`, empty strings, negative numbers, or massive arrays?
   - Are network requests wrapped in try/catch or timeout blocks?
   - Are file descriptors, sockets, or database connections properly closed?
3. **Junior-Friendly Explanations**:
   - For every flaw found, explain the real-world consequence with a physical analogy.
   - Teach the pattern that prevents the issue permanently.
4. **Token & Performance Efficiency**:
   - Any accidental $O(N^2)$ loops or redundant database queries (N+1 queries)?
   - Are data structures chosen appropriately (e.g., Set vs. Array for lookups)?

Refer to [checklist.md](checklist.md) for detailed evaluation criteria.
