from pathlib import Path
from typing import List
from typing import Set


prohibited_packages_listner = set(
    [
        "python",
        "pre-commit",
        "jupyter-book",
        "pyyaml",
        "pylatexenc",
        "pyppeteer",
        "sphinx-jupyterbook-latex",
        "sphinx-sitemap",
        "paramiko",
        "scp",
        "Jinja2",
        "fire",
        "loguru",
        "",
    ],
)
prohibited_packages_dev = set(["python", ""])


def get_packages(prohibited_packages: Set[str]) -> (List[str]):
    """
    Remove prohibited packages and creates text for requirements.txt
    prohibited_packages: set of prohibited packages
    """
    packages = []
    packages_flag = False
    with open("pyproject.toml", "r") as toml_file:
        for line in toml_file:
            line = line.strip()
            if line in ["[tool.poetry.dependencies]", "# [tool.poetry.dev-dependencies]"]:
                packages_flag = True
                continue
            elif line in ["[build-system]"]:
                packages_flag = False
            elif line == "":
                continue
            if packages_flag:
                package, version = line.split(" = ")
                package = package.strip()
                version = version.strip()[1:-1]  # remove brakets \"^version\"
                if package not in prohibited_packages:
                    if version.startswith("^"):
                        if len(version.split(".")) == 3:
                            packages.append(
                                package + "==" + version[1:],  # remove ^
                            )
                        else:
                            packages.append(package + "==" + version[1:])  # remove ^
                    else:
                        packages.append(package + "==" + version)
    return sorted(packages)


if __name__ == "__main__":
    with open(Path("requirements/requirements-listener.txt"), "w") as req_file:
        req_file.writelines("\n".join(get_packages(prohibited_packages=prohibited_packages_listner)))
        req_file.writelines("\n")

    with open(Path("requirements/requirements-dev.txt"), "w") as req_file:
        req_file.writelines("\n".join(get_packages(prohibited_packages=prohibited_packages_dev)))
        req_file.writelines("\n")
