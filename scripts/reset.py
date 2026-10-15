#!/usr/bin/env python3
"""Safely preview and reset local learning notes with automatic backups.

Ensures zero accidental data loss by creating a full timestamped backup in
`.vibewise/backups/` before replacing active notes with clean templates.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
import sys
import tempfile

# Standard fresh templates
FRESH_TEMPLATES = {
    "profile.md": (
        "# Learner Profile\n\n"
        "Learning mode: active\n"
        "Onboarding: incomplete\n"
        "Onboarding reset: pending\n\n"
        "Remaining onboarding: Project situation, experience, stack familiarity, goals, and preferences.\n"
    ),
    "progress.md": "# Learning Progress\n\nNo learning events recorded yet.\n",
    "project-map.md": "# Project Map\n\nNot mapped yet. Inspect current project files.\n",
}

STATE_DIR_NAMES = (".vibewise", ".vibe-wise", ".not-ur-vibe", ".sensible-vibes")


def find_state_directory(cwd: Path) -> Path:
    """Find the nearest learning directory within project boundaries."""
    # Check current directory and parents
    for directory in (cwd, *cwd.parents):
        for name in STATE_DIR_NAMES:
            candidate = directory / name
            if candidate.is_dir() and not candidate.is_symlink():
                return candidate
        if (directory / ".git").exists():
            break
    return None


def get_snapshot(cwd: Path):
    """Inspect state directory and calculate sha256 fingerprint of current notes."""
    state = find_state_directory(cwd)
    if state is None:
        return None, {}, None

    notes = {}
    for name in FRESH_TEMPLATES:
        path = state / name
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            continue
        if not stat.S_ISREG(mode):
            raise ValueError(f"Refusing to reset non-regular file: {path}")
        notes[name] = path.read_bytes()

    digest = hashlib.sha256(str(state).encode())
    for name in FRESH_TEMPLATES:
        data = notes.get(name)
        digest.update(json.dumps([name, None if data is None else data.hex()]).encode())

    return state, notes, digest.hexdigest()


def reset_notes(cwd: str, confirmation: str = None) -> dict:
    """Preview or execute state reset."""
    cwd_path = Path(cwd).resolve()
    if not cwd_path.is_dir():
        raise ValueError("Target working directory does not exist.")

    state, notes, fingerprint = get_snapshot(cwd_path)
    if not notes:
        return {"status": "no_notes", "cwd": str(cwd_path)}

    if confirmation is not None and confirmation != fingerprint:
        raise ValueError("State files changed since preview. Please preview and confirm again.")

    # Preview mode
    if confirmation is None:
        return {
            "status": "preview",
            "project": str(state.parent),
            "state_dir": str(state),
            "files": list(notes.keys()),
            "backup_destination": str(state / "backups"),
            "confirmation_token": fingerprint,
        }

    # Execute reset with backup
    backup_parent = state / "backups"
    if backup_parent.is_symlink() or (backup_parent.exists() and not backup_parent.is_dir()):
        raise ValueError("Backup path must be a regular directory.")

    backup_parent.mkdir(parents=True, exist_ok=True)
    prefix = datetime.now(timezone.utc).strftime("reset-%Y%m%dT%H%M%SZ-")
    backup_dir = Path(tempfile.mkdtemp(prefix=prefix, dir=backup_parent))

    try:
        # 1. Back up existing notes
        for name, data in notes.items():
            (backup_dir / name).write_bytes(data)

        # 2. Write fresh replacement files in backup staging first
        for name, text in FRESH_TEMPLATES.items():
            (backup_dir / f".new-{name}").write_text(text, encoding="utf-8")

        # 3. Verify fingerprint hasn't drifted during backup write
        if get_snapshot(cwd_path)[2] != fingerprint:
            raise ValueError("Notes modified during backup operation. Reset aborted.")

        # 4. Atomically swap fresh files into place
        for name in FRESH_TEMPLATES:
            os.replace(backup_dir / f".new-{name}", state / name)

    except (OSError, ValueError) as err:
        raise ValueError(f"Reset failed: {err}. Safe backup retained at {backup_dir}") from err

    return {
        "status": "reset",
        "project": str(state.parent),
        "state_dir": str(state),
        "backup_path": str(backup_dir),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", required=True, help="Current project working directory")
    parser.add_argument(
        "--confirm",
        help="Confirmation token from preview. Required to execute reset.",
    )
    args = parser.parse_args()

    try:
        result = reset_notes(args.cwd, args.confirm)
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError) as err:
        print(json.dumps({"status": "error", "message": str(err)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
