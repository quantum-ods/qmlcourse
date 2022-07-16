import os
from pathlib import Path

import yaml  # type: ignore

from tools.convert import md_to_ipynb

test_toc = """
- file: book/index.md

# :ru:

- part: Test
  chapters:
    - file: book/test/test.md
      title: 🟦 Just test
"""


def test_md_to_ipynb(
    test_md_file_path=Path("./tests/test.md"),
    test_ipynb_file_path=Path("./tests/test.ipynb"),
) -> (None):

    # todo: update args
    md_to_ipynb(yaml.safe_load(test_toc))

    os.chdir("scripts")

    # Test that test ipynb exists
    print(os.path.exists(test_ipynb_file_path))

    # Test len ipynb
    with open(test_ipynb_file_path, "r") as test_ipynb_file:
        test_ipynb_readed = test_ipynb_file.read()
    assert len(test_ipynb_readed) == 685
