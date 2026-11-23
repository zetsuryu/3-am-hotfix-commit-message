"""3 AM Hotfix: the funniest commit message.

Writes a single one-line git commit message to /output/entry.txt.
The line is a tired dev's 3 AM hotfix confession: prod is back up, and
the root cause of the outage was his own "one-line change".
"""

import os

MESSAGE = "fix: prod is back up, root cause: my 'one-line change' at 3 AM"

# Gate: one line, 1-179 characters, not only whitespace.
assert "\n" not in MESSAGE, "commit message must be a single line"
assert "\r" not in MESSAGE, "commit message must be a single line"
assert 1 <= len(MESSAGE) <= 179, f"length {len(MESSAGE)} outside 1-179"
assert MESSAGE.strip(), "commit message must not be only whitespace"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUT_DIR, exist_ok=True)

with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(MESSAGE)
