from pathlib import Path

from loguru import logger

from tools.convert import md_to_ipynb


# todo: add tests for exception
def test_md_to_ipynb(get_ipynb_file: str) -> (None):

    try:

        md_to_ipynb(dir_2_toc="./tests/data", dir_2_ipynb="./tests", testing=True)

        path_to_converted_lecture_to_ipynb = Path("./tests/data/lecture.ipynb")

        # Test len ipynb
        with open(path_to_converted_lecture_to_ipynb, "r") as test_ipynb_file:
            converted_lecture_to_ipynb = test_ipynb_file.read()

        assert len(get_ipynb_file) == len(converted_lecture_to_ipynb)

    except FileNotFoundError:
        logger.error("file not found")
    finally:
        path_to_converted_lecture_to_ipynb.unlink()  # pyright: ignore reportUnboundVariable
