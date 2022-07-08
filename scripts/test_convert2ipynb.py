import os
import pathlib
import unittest
from unittest import TestCase

import yaml
from convert2ipynb import convert_md2ipynb

##
# Test working from scripts folder
# python -m unittest
##
test_toc = """
- file: book/index.md

# :ru:

- part: Test
  chapters:
    - file: book/test/test.md
      title: 🟦 Just test
"""
test_md = """
# Test

Some test text

$$
E = mc^2
$$

```python
print(2+2)
```

"""

test_md_file_path = pathlib.Path("../qmlcourse/book/test/test.md")
test_ipynb_file_path = pathlib.Path("../notebooks/test/test.ipynb")


class TestConvertmd2ipynb(TestCase):
    def setUp(self: TestCase) -> None:
        try:
            os.mkdir(test_md_file_path.parent)
        except OSError:
            print("Test path is exist, that shouldn't be. Testing teardDown don't work.")
        with open(test_md_file_path, "w") as test_md_file:
            test_md_file.writelines(test_md)

    def tearDown(self: TestCase) -> None:
        try:
            os.remove(test_md_file_path)
            os.rmdir(test_md_file_path.parent)
        except OSError:
            print("test don't setup the md file or folder")
        try:
            os.remove(test_ipynb_file_path)
            os.rmdir(test_ipynb_file_path.parent)
        except FileNotFoundError:
            print("test don't get the ipynb file or folder")

    def test_convert_md2ipynb(self: TestCase) -> None:
        cwd = pathlib.Path(os.getcwd())
        os.chdir(cwd.parent)
        print(os.getcwd())
        convert_md2ipynb(toc=yaml.safe_load(test_toc))

        os.chdir("scripts")
        # Test that test ipynb exists
        print(os.path.exists(test_ipynb_file_path))
        # Test len ipynb
        with open(test_ipynb_file_path, "r") as test_ipynb_file:
            test_ipynb_readed = test_ipynb_file.read()
        assert len(test_ipynb_readed) == 685


if __name__ == "__main__":
    unittest.main()
