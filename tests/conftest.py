import pytest


@pytest.fixture()
def get_toc_file() -> (str):
    toc_file = """
    - file: book/index.md

    # :ru:

    - part: Test
    chapters:
        - file: book/test/test.md
        title: 🟦 Just test
    """

    return toc_file


@pytest.fixture()
def get_md_file() -> (str):
    md_file = """
    # Test

    Some test text

    $$
    E = mc^2
    $$

    ```python
    print(2+2)
    ```

    """

    return md_file


@pytest.fixture()
def get_ipynb_file() -> (str):
    ipynb_file = """

    """

    return ipynb_file
