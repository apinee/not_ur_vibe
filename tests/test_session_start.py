import json
from pathlib import Path
import tempfile
import unittest
import sys

# Add hooks directory to path
HOOKS_DIR = Path(__file__).resolve().parents[1] / "hooks"
sys.path.insert(0, str(HOOKS_DIR))

from session_start import (
    profile_is_active,
    git_root,
    state_directory,
    restore,
)


class TestSessionStart(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_profile_is_active_with_valid_file(self):
        profile = self.project_path / "profile.md"
        profile.write_text("# Profile\nLearning mode: active\n", encoding="utf-8")
        self.assertTrue(profile_is_active(profile))

    def test_profile_is_active_when_paused(self):
        profile = self.project_path / "profile.md"
        profile.write_text("# Profile\nLearning mode: paused\n", encoding="utf-8")
        self.assertFalse(profile_is_active(profile))

    def test_profile_is_active_rejects_missing_or_empty(self):
        profile = self.project_path / "nonexistent.md"
        self.assertFalse(profile_is_active(profile))

        empty = self.project_path / "empty.md"
        empty.write_text("   \n\n", encoding="utf-8")
        self.assertFalse(profile_is_active(empty))

    def test_git_root_detection(self):
        git_dir = self.project_path / ".git"
        git_dir.mkdir()
        sub_dir = self.project_path / "src" / "deep"
        sub_dir.mkdir(parents=True)

        self.assertEqual(git_root(sub_dir), self.project_path)
        self.assertEqual(git_root(self.project_path), self.project_path)

    def test_state_directory_discovery(self):
        state = self.project_path / ".vibewise"
        state.mkdir()

        self.assertEqual(state_directory(self.project_path), state)

    def test_restore_payload_flow(self):
        state = self.project_path / ".vibewise"
        state.mkdir()
        profile = state / "profile.md"
        profile.write_text("# Profile\nLearning mode: active\n", encoding="utf-8")

        payload = {
            "hook_event_name": "SessionStart",
            "cwd": str(self.project_path),
        }
        output = restore(payload)
        self.assertIsNotNone(output)
        self.assertEqual(output["hookSpecificOutput"]["hookEventName"], "SessionStart")
        self.assertIn("Not Your Vibe", output["hookSpecificOutput"]["additionalContext"])


if __name__ == "__main__":
    unittest.main()
