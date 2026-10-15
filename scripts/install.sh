#!/usr/bin/env bash
# Not Your Vibe: Unix/macOS One-Line Installer
# Usage: curl -fsSL https://raw.githubusercontent.com/nykooi1/vibe-wise/main/scripts/install.sh | bash

set -e

echo ""
echo "=========================================================="
echo "          ✨ Installing Not Your Vibe ✨                 "
echo "  Universal Learning-First AI Pair Programming Framework  "
echo "=========================================================="
echo ""

TARGET_DIR="${1:-.}"
TARGET_PATH=$(cd "$TARGET_DIR" && pwd)

echo "Target project directory: $TARGET_PATH"

mkdir -p "$TARGET_PATH/.vibewise"
mkdir -p "$TARGET_PATH/.cursor/rules"
mkdir -p "$TARGET_PATH/.agents/skills/learn"
mkdir -p "$TARGET_PATH/.agents/skills/reset"
mkdir -p "$TARGET_PATH/.agents/skills/review"

# Create minimal profile.md if not exists
if [ ! -f "$TARGET_PATH/.vibewise/profile.md" ]; then
  cat << 'EOF' > "$TARGET_PATH/.vibewise/profile.md"
# Learner Profile

Learning mode: active
Onboarding: incomplete

Remaining onboarding: Project situation, experience, stack familiarity, goals, and preferences.
EOF
  echo "✔ Created .vibewise/profile.md"
fi

# Create progress.md
if [ ! -f "$TARGET_PATH/.vibewise/progress.md" ]; then
  cat << 'EOF' > "$TARGET_PATH/.vibewise/progress.md"
# Learning Progress

No learning events recorded yet.
EOF
  echo "✔ Created .vibewise/progress.md"
fi

# Add .vibewise/ to .gitignore
if [ -f "$TARGET_PATH/.gitignore" ]; then
  if ! grep -q "\.vibewise/" "$TARGET_PATH/.gitignore"; then
    echo -e "\n# Not Your Vibe learning state\n.vibewise/" >> "$TARGET_PATH/.gitignore"
    echo "✔ Added .vibewise/ to .gitignore"
  fi
else
  echo -e "# Not Your Vibe learning state\n.vibewise/" > "$TARGET_PATH/.gitignore"
  echo "✔ Created .gitignore with .vibewise/"
fi

echo ""
echo "✅ Not Your Vibe installed successfully in $TARGET_PATH!"
echo "Open your project in Antigravity, Claude Code, Codex, or Cursor and start learning!"
echo ""
