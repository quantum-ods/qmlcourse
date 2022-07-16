import os
from pathlib import Path
from subprocess import call
from typing import Dict
from typing import List

import yaml  # type: ignore

PREFIX = Path("qmlcourse")


def convert_md2ipynb(toc: List[Dict[str, Dict]]) -> (None):
    """
    Convert MyST files from toc to ipython notebooks.
    toc: YAML list of the dicts with table of contents for jupyter book.
    """
    for part in toc[1:]:
        for chapter in part["chapters"]:
            file_path = PREFIX / Path(chapter["file"])
            print(file_path)
            call(["poetry", "run", "jupytext", file_path.absolute(), "--to", "ipynb"])
            os.makedirs(
                Path("notebooks") / Path("/".join(chapter["file"].split("/")[1:-1])),
                exist_ok=True,
            )
            try:
                os.replace(
                    PREFIX / Path(chapter["file"].split(".")[0] + ".ipynb"),
                    Path("notebooks") / Path("/".join(chapter["file"].split(".")[0].split("/")[1:]) + ".ipynb"),
                )
            except FileNotFoundError:
                print("Problem with", Path(chapter["file"]))


if __name__ == "__main__":

    # Open table of content
    with open(f"{PREFIX}/_toc.yml", "r", encoding="utf-8") as f:
        toc = yaml.safe_load(f)

    # make dir for ipynbs
    os.makedirs("notebooks", exist_ok=True)

    # convert lectures
    convert_md2ipynb(toc)
