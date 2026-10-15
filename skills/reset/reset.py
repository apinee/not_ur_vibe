#!/usr/bin/env python3
"""Wrapper around scripts/reset.py for skills/reset directory invocation."""

from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from reset import main

if __name__ == "__main__":
    sys.exit(main())
