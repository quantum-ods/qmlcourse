"""Fail if any executed code cell in the built MyST site produced an error.

`jupyter-book build --execute` keeps going when a cell raises: the traceback is
rendered on the page and the build exits with 0. This script scans the built
page JSON and exits non-zero if any error output is found.

Usage: python scripts/check_execution_errors.py qmlcourse/_build/site/content
"""

import json
import re
import sys
from pathlib import Path

ANSI = re.compile(r"\x1b\[[0-9;]*m")


def find_errors(node, acc):
    if isinstance(node, dict):
        data = node.get("jupyter_data")
        if isinstance(data, dict) and data.get("output_type") == "error":
            acc.append(f"{data.get('ename')}: {ANSI.sub('', data.get('evalue', ''))[:300]}")
        for value in node.values():
            find_errors(value, acc)
    elif isinstance(node, list):
        for value in node:
            find_errors(value, acc)


def main(content_dir: str) -> int:
    pages = sorted(Path(content_dir).glob("*.json"))
    if not pages:
        print(f"No page JSON found in {content_dir}", file=sys.stderr)
        return 2

    failed = 0
    for page in pages:
        errors = []
        find_errors(json.loads(page.read_text(encoding="utf-8")), errors)
        if errors:
            failed += 1
            print(f"::error file={page.name}::{len(errors)} failing cell(s): {errors[0]}")

    print(f"Checked {len(pages)} pages, {failed} with execution errors.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "qmlcourse/_build/site/content"))
