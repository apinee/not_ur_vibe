#!/usr/bin/env python3
"""Diagnostics utility for Not Your Vibe installations.

Checks system prerequisites, agent configurations, and project state health.
"""

import argparse
import json
from pathlib import Path
import sys

STATE_DIR_NAMES = (".vibewise", ".vibe-wise", ".not-ur-vibe", ".sensible-vibes")


def check_python_version():
    major, minor = sys.version_info[:2]
    ok = major >= 3 and minor >= 8
    return {
        "check": "Python Version",
        "status": "PASS" if ok else "FAIL",
        "detail": f"Python {major}.{minor} (Requires Python 3.8+)",
    }


def check_state_directory(cwd: Path):
    found = None
    for directory in (cwd, *cwd.parents):
        for name in STATE_DIR_NAMES:
            candidate = directory / name
            if candidate.is_dir() and not candidate.is_symlink():
                found = candidate
                break
        if found or (directory / ".git").exists():
            break

    if found:
        files = [f.name for f in found.iterdir() if f.is_file()]
        return {
            "check": "Learning State Directory",
            "status": "PASS",
            "detail": f"Active state at {found} with files: {', '.join(files)}",
        }
    return {
        "check": "Learning State Directory",
        "status": "INFO",
        "detail": "No active state folder yet. Run onboarding or invoke /learn.",
    }


def check_agent_configs(root: Path):
    results = []

    # Antigravity skills
    ag_skill = root / "skills" / "learn" / "SKILL.md"
    results.append({
        "check": "Antigravity Skill Definition",
        "status": "PASS" if ag_skill.exists() else "FAIL",
        "detail": str(ag_skill),
    })

    # Claude Code plugin
    claude_cfg = root / ".claude-plugin" / "plugin.json"
    results.append({
        "check": "Claude Code Plugin Config",
        "status": "PASS" if claude_cfg.exists() else "FAIL",
        "detail": str(claude_cfg),
    })

    # Codex plugin
    codex_cfg = root / ".codex-plugin" / "plugin.json"
    results.append({
        "check": "Codex Plugin Config",
        "status": "PASS" if codex_cfg.exists() else "FAIL",
        "detail": str(codex_cfg),
    })

    # Cursor rules
    cursor_rules = root / ".cursor" / "rules" / "learn.mdc"
    results.append({
        "check": "Cursor Rule Config",
        "status": "PASS" if cursor_rules.exists() else "FAIL",
        "detail": str(cursor_rules),
    })

    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", default=".", help="Project working directory to check")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    args = parser.parse_args()

    cwd = Path(args.cwd).resolve()
    repo_root = Path(__file__).resolve().parents[1]

    checks = [
        check_python_version(),
        check_state_directory(cwd),
        *check_agent_configs(repo_root),
    ]

    all_passed = all(c["status"] in ("PASS", "INFO") for c in checks)

    if args.json:
        print(json.dumps({"healthy": all_passed, "checks": checks}, indent=2))
    else:
        print("\n=== Not Your Vibe: Diagnostics Report ===")
        for c in checks:
            badge = f"[{c['status']}]"
            print(f"{badge:<8} {c['check']:<30} : {c['detail']}")
        print("=========================================\n")
        if all_passed:
            print("Everything looks great! Ready for learning-first AI pair programming.\n")
        else:
            print("Some checks failed. Review the details above.\n")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
