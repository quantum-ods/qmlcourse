import os

import yaml  # type: ignore

from tools.convert import md_to_ipynb


# todo: add tests for exception
def test_md_to_ipynb(get_toc_file: str, get_ipynb_file: str) -> (None):

    # todo: update args
    md_to_ipynb(yaml.safe_load(get_toc_file))

    os.chdir("scripts")

    # Test len ipynb
    with open(get_ipynb_file, "r") as test_ipynb_file:
        test_ipynb_readed = test_ipynb_file.read()
    assert len(test_ipynb_readed) == 685
