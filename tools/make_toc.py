import sys
import yaml
from pathlib import Path


if __name__ == "__main__":
    toc_file = sys.argv[1]
    prefix_path = Path(sys.argv[2])
    prefix_path.mkdir(parents=True, exist_ok=True)

    with open(toc_file, "r") as toc_stream:
        toc = yaml.load(toc_stream)

    for item in toc:
        if "part" in item:
            lec_name = item.get("part")
            part_path = prefix_path.joinpath(f"{lec_name}.yml")

            with part_path.open("w") as part_file:
                yaml.dump(
                    data=[
                        {"file": "book/index"},
                        item,
                    ],
                    stream=part_file,
                    allow_unicode=True,
                )
