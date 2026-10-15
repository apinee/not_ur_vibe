#!/usr/bin/env python3
"""Cross-platform installer for Not Your Vibe.

Installs configuration, skills, and rule files into a local project or global user config.
Zero third-party dependencies.
"""

import argparse
from pathlib import Path
import shutil
import sys

REPO_ROOT = Path(__file__).resolve().parent


def install_to_project(target_dir: Path):
    print(f"\n🚀 Installing Not Your Vibe into project: {target_dir}")

    # 1. State directory
    state_dir = target_dir / ".vibewise"
    state_dir.mkdir(parents=True, exist_ok=True)

    profile = state_dir / "profile.md"
    if not profile.exists():
        profile.write_text(
            "# Learner Profile\n\n"
            "Learning mode: active\n"
            "Onboarding: incomplete\n\n"
            "Remaining onboarding: Project situation, experience, stack familiarity, goals, and preferences.\n",
            encoding="utf-8",
        )
        print("  ✔ Created .vibewise/profile.md")

    progress = state_dir / "progress.md"
    if not progress.exists():
        progress.write_text(
            "# Learning Progress\n\nNo learning events recorded yet.\n",
            encoding="utf-8",
        )
        print("  ✔ Created .vibewise/progress.md")

    project_map = state_dir / "project-map.md"
    if not project_map.exists():
        project_map.write_text(
            "# Project Map\n\nNot mapped yet. Inspect current project files.\n",
            encoding="utf-8",
        )
        print("  ✔ Created .vibewise/project-map.md")

    # 2. Master AGENTS.md rule
    agents_src = REPO_ROOT / "AGENTS.md"
    agents_dst = target_dir / "AGENTS.md"
    if agents_src.exists() and not agents_dst.exists():
        shutil.copy2(agents_src, agents_dst)
        print("  ✔ Installed AGENTS.md (Antigravity & universal agent directives)")

    # 3. Cursor rules
    cursor_rules_dir = target_dir / ".cursor" / "rules"
    cursor_rules_dir.mkdir(parents=True, exist_ok=True)
    src_cursor_rules = REPO_ROOT / ".cursor" / "rules"
    if src_cursor_rules.exists():
        for rule_file in src_cursor_rules.glob("*.mdc"):
            shutil.copy2(rule_file, cursor_rules_dir / rule_file.name)
        print("  ✔ Installed .cursor/rules/*.mdc (Cursor IDE integration)")

    cursorrules_src = REPO_ROOT / ".cursorrules"
    cursorrules_dst = target_dir / ".cursorrules"
    if cursorrules_src.exists() and not cursorrules_dst.exists():
        shutil.copy2(cursorrules_src, cursorrules_dst)
        print("  ✔ Installed .cursorrules")

    # 4. Antigravity skills
    ag_skills_dst = target_dir / ".agents" / "skills"
    ag_skills_src = REPO_ROOT / "skills"
    if ag_skills_src.exists():
        for skill_dir in ag_skills_src.iterdir():
            if skill_dir.is_dir():
                dest = ag_skills_dst / skill_dir.name
                dest.mkdir(parents=True, exist_ok=True)
                for f in skill_dir.glob("*.*"):
                    shutil.copy2(f, dest / f.name)
        print("  ✔ Installed .agents/skills/ (Antigravity skill catalog)")

    # 5. Gitignore
    gitignore = target_dir / ".gitignore"
    if gitignore.exists():
        content = gitignore.read_text(encoding="utf-8")
        if ".vibewise/" not in content:
            with gitignore.open("a", encoding="utf-8") as f:
                f.write("\n# Not Your Vibe learning state\n.vibewise/\n")
            print("  ✔ Added .vibewise/ to .gitignore")
    else:
        gitignore.write_text("# Not Your Vibe learning state\n.vibewise/\n", encoding="utf-8")
        print("  ✔ Created .gitignore with .vibewise/")

    print("\n✅ Installation complete! Open your project in your AI IDE and start building!\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target",
        default=".",
        help="Target project directory (default: current directory)",
    )
    args = parser.parse_args()
    target_path = Path(args.target).resolve()
    install_to_project(target_path)


if __name__ == "__main__":
    main()
