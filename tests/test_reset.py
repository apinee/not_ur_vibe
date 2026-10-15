from pathlib import Path
import tempfile
import unittest
import sys

# Add scripts directory to path
SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from reset import reset_notes, get_snapshot


class TestReset(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_path = Path(self.temp_dir.name)
        self.state_dir = self.project_path / ".vibewise"
        self.state_dir.mkdir()

        (self.state_dir / "profile.md").write_text("# Old Profile\n", encoding="utf-8")
        (self.state_dir / "progress.md").write_text("# Old Progress\n", encoding="utf-8")
        (self.state_dir / "project-map.md").write_text("# Old Map\n", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_preview_returns_token(self):
        res = reset_notes(str(self.project_path))
        self.assertEqual(res["status"], "preview")
        self.assertIn("confirmation_token", res)
        self.assertTrue(len(res["confirmation_token"]) == 64)

    def test_reset_with_valid_token(self):
        preview = reset_notes(str(self.project_path))
        token = preview["confirmation_token"]

        res = reset_notes(str(self.project_path), confirmation=token)
        self.assertEqual(res["status"], "reset")
        self.assertTrue(Path(res["backup_path"]).exists())

        # Check files were reset to fresh templates
        new_profile = (self.state_dir / "profile.md").read_text(encoding="utf-8")
        self.assertIn("Onboarding: incomplete", new_profile)

    def test_reset_with_invalid_token_fails(self):
        with self.assertRaises(ValueError):
            reset_notes(str(self.project_path), confirmation="invalid_fake_token")


if __name__ == "__main__":
    unittest.main()
