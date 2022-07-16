from pathlib import Path
from subprocess import call
from typing import Dict
from typing import List
from loguru import logger

# fire guide: https://github.com/google/python-fire/blob/master/docs/guide.md
import fire

import yaml  # type: ignore


def md_to_ipynb(path_2_toc: Path = Path("./qmlcourse"), path_2_ipynb: Path = Path("./notebooks")) -> (None):
    """
    Convert MyST files from toc to ipython notebooks.
    toc: YAML list of the dicts with table of contents for jupyter book.
    """

    # open table of contents
    with open(f"{path_2_toc}/_toc.yml", "r", encoding="utf-8") as toc_file:
        toc: List[Dict[str, Dict]] = yaml.safe_load(toc_file)

    for part in toc[1:]:
        for chapter in part["chapters"]:
            file_path = path_2_toc / Path(chapter["file"])
            logger.info(f"convert {file_path}")

            call(["poetry", "run", "jupytext", file_path.absolute(), "--to", "ipynb"])
            
            Path.mkdir(
                path_2_ipynb / "/".join(chapter["file"].split("/")[1:-1]),
                parents = True,
                exist_ok=True,
            )
            
            try:
                Path.replace(
                    path_2_toc / Path(chapter["file"].split(".")[0] + ".ipynb"),
                    path_2_ipynb / Path("/".join(chapter["file"].split(".")[0].split("/")[1:]) + ".ipynb"),
                )
            except FileNotFoundError:
                logger.error("Problem with", Path(chapter["file"]))

if __name__ == '__main__':
    fire.Fire()