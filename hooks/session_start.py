#!/usr/bin/env python3
"""Restore learning context when an AI coding agent starts or resumes a session.

The agent platform sends a JSON event on stdin. If the current project has
active learning notes, we print JSON instructions telling the agent which files
to read. Otherwise, we exit silently.
"""

import json
from pathlib import Path
import re
import sys

# Locate plugin root relative to this script
PLUGIN_ROOT = Path(__file__).resolve().parents[1]

# Recognized state directory names in order of priority
STATE_DIR_NAMES = (".vibewise", ".vibe-wise", ".not-ur-vibe", ".sensible-vibes")


def profile_is_active(path: Path) -> bool:
    """Check if the profile exists and learning mode is not paused.

    Guards against symlinks, non-files, and non-UTF8 corruption.
    """
    if path.is_symlink() or not path.is_file():
        return False
    has_content = False
    try:
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                if line.strip():
                    has_content = True
                if re.fullmatch(r"Learning mode:\s*paused\s*", line, re.IGNORECASE):
                    return False
    except (OSError, UnicodeError):
        return False
    return has_content


def git_root(cwd: Path) -> Path:
    """Find the nearest repository root (.git directory or file)."""
    for directory in (cwd, *cwd.parents):
        if (directory / ".git").exists():
            return directory
    return None


def state_directory(cwd: Path) -> Path:
    """Find the nearest learning state directory within git project boundaries."""
    root = git_root(cwd)
    candidates = (
        [cwd]
        if root is None
        else [cwd, *cwd.parents][: len(cwd.relative_to(root).parts) + 1]
    )

    for directory in candidates:
        for name in STATE_DIR_NAMES:
            state = directory / name
            if state.exists() or state.is_symlink():
                # Stop if found; do not cross beyond to prevent loading a different project's notes
                if state.is_dir() and not state.is_symlink():
                    return state
                return None
    return None


def restore(payload: dict) -> dict:
    """Build the restoration instructions for the agent or return None."""
    if not isinstance(payload, dict) or payload.get("hook_event_name") != "SessionStart":
        return None

    raw_cwd = payload.get("cwd")
    if not isinstance(raw_cwd, str) or not Path(raw_cwd).is_absolute():
        return None

    cwd = Path(raw_cwd).resolve()
    if not cwd.is_dir():
        return None

    state = state_directory(cwd)
    if state is None:
        return None

    if not profile_is_active(state / "profile.md"):
        return None

    skill_path = PLUGIN_ROOT / "skills" / "learn" / "SKILL.md"

    context = (
        "Not Your Vibe learning mode is active for this project.\n"
        "You are pair-programming with the user: they architect the solution, while you explain concepts, "
        "audit security, review code, and implement agreed steps.\n\n"
        f"1. Read the Learn Guide: {skill_path}\n"
        f"2. Inspect learning state in: {state}\n"
        "   - Read profile.md (preferences, experience level, mastered concepts)\n"
        "   - Read project-map.md (architecture, component map, data boundaries)\n"
        "   - Check progress.md for any pending decisions before writing code.\n\n"
        "Core Rules:\n"
        "- Explain every unfamiliar concept using an intuitive real-world analogy (junior engineer level).\n"
        "- If fixing a bug or error: explain root cause + failure analogy + fix.\n"
        "- Continuously check for security vulnerabilities (OWASP top 10).\n"
        "- Execute a Codex peer review gate before completing code changes.\n"
        "- Conserve tokens: keep answers focused and never repeat full summaries needlessly."
    )

    return {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }


def main():
    try:
        payload = json.loads(sys.stdin.read(65536))
        output = restore(payload)
    except (OSError, ValueError, TypeError, RecursionError):
        return  # Hook errors should never block session startup

    if output:
        print(json.dumps(output))


if __name__ == "__main__":
    main()
