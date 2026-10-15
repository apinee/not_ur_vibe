from pathlib import Path
import tempfile
import unittest
import sys

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from doctor import check_python_version, check_state_directory


class TestDoctor(unittest.TestCase):
    def test_python_version_check(self):
        res = check_python_version()
        self.assertIn(res["status"], ("PASS", "FAIL"))

    def test_state_directory_check(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            cwd = Path(temp_dir)
            res = check_state_directory(cwd)
            self.assertEqual(res["status"], "INFO")

            (cwd / ".vibewise").mkdir()
            (cwd / ".vibewise" / "profile.md").write_text("test", encoding="utf-8")
            res_after = check_state_directory(cwd)
            self.assertEqual(res_after["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
