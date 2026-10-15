---
name: reset
description: Safely reset or back up local learning notes (.vibewise/) with confirmation.
disable-model-invocation: true
---

# Not Your Vibe: Reset Mode

Safely preview, back up, and reset learning notes in `.vibewise/`.

## Workflow

1. Run the reset preview script:
   ```sh
   python scripts/reset.py --cwd <PROJECT_ROOT>
   ```
   Or execute directly via the Python runtime.
2. Present the preview to the user:
   - Location of existing notes.
   - Target backup folder.
   - Unique fingerprint token.
3. Require explicit confirmation from the user:
   - "Do you want to reset your local learning profile and start fresh? (Your existing notes will be backed up in `.vibewise/backups/`)."
4. Upon user confirmation, invoke with `--confirm <TOKEN>`:
   ```sh
   python scripts/reset.py --cwd <PROJECT_ROOT> --confirm <TOKEN>
   ```
5. Report the backup location and confirm the fresh profile is ready.
