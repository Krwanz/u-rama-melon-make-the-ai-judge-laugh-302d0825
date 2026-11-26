"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one office-life joke, a single line under 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The joke plays on a universal office truth: the "quick question" that
is never quick. The turn is that after 45 minutes you know everything
about the asker's personal life and still nothing about the work.
The final line tightens the first draft: "opened with" replaces
"said", an em dash replaces "and now" for a punchier beat, and "still
nothing" replaces "absolutely nothing" so the sting lands on the zero
work learned, not on the adverb.
"""

import os
import sys

JOKE = (
    "My boss opened with 'quick question' forty-five minutes ago \u2014 I now "
    "know his dog's diet, his weekend plans, and still nothing about the project."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
