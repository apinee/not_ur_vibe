# Security Radar & Vulnerability Defense

Security cannot be bolted on as an afterthought; it must be designed into the architecture from the first line of code.

---

## The OWASP Top 10 Radar in Not Your Vibe

During every `✦ Design checkpoint` and `✦ Codex review`, the AI pair programmer evaluates code against these 6 core vulnerability classes:

### 1. Injections (SQL, Command, Template)
- **Risk**: Attackers pass executable syntax inside user data.
- **Defense**: Strictly enforce parameterized queries / ORM statements. Disallow arbitrary shell execution via string concatenation (`exec("cat " + user_input)`).

### 2. Path Traversal & Arbitrary File Access
- **Risk**: Attackers supply relative traversal sequences (`../../etc/passwd`) in file download or write handlers.
- **Defense**: Strip directory separators using `path.basename` and resolve paths against an explicit whitelist root directory (`Path(base).resolve() in Path(allowed).parents`).

### 3. Broken Authentication & Session Management
- **Risk**: Predictable session IDs, unhashed passwords, lack of rate-limiting on login endpoints.
- **Defense**: Use Argon2 or bcrypt for password hashing; sign tokens with strong secrets; set appropriate expiration and HTTP-only cookie flags.

### 4. Hardcoded Secrets & Information Leakage
- **Risk**: API keys, tokens, and database passwords committed to version control.
- **Defense**: Use environment variables (`process.env` / `os.environ`), `.env.example`, and pre-commit hooks to block secrets.

### 5. Insecure Direct Object References (IDOR)
- **Risk**: A user requests `/api/notes/42` and receives Alice's note even though they are logged in as Bob.
- **Defense**: Always filter by authenticated user ID (`SELECT * FROM notes WHERE id = ? AND user_id = ?`).

### 6. Cross-Site Scripting (XSS) & CSRF
- **Risk**: Injected malicious scripts execute in other users' browsers.
- **Defense**: Context-aware HTML escaping, Content Security Policy (CSP) headers, and anti-CSRF tokens for mutating actions.
