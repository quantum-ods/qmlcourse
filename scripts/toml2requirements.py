prohibited_packages_listner = set(
    [
        "python",
        "pre-commit",
        "jupyter-book",
        "pyyaml",
        "pylatexenc",
        "paramiko",
        "scp",
        "",
    ]
)
prohibited_packages_dev = set(["python", ""])


def get_packages(prohibited_packages):
    """
    Remove prohibited packages and creates text for requirements.txt
    prohibited_packages: set of prohibited packages
    """
    packages = []
    packages_flag = False
    with open("pyproject.toml", "r") as toml_file:
        for line in toml_file:
            line = line.strip()
            if line == "[tool.poetry.dependencies]":
                packages_flag = True
                continue
            elif line == "[build-system]":
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
                                package + ">=" + version[1:]
                            )  # choose major version, needed for security bugfixes
                        else:
                            packages.append(package + "==" + version[1:])
                    else:
                        packages.append(package + "==" + version)
    return sorted(packages)


if __name__ == "__main__":
    with open("requirements.txt", "w") as req_file:
        req_file.writelines("\n".join(get_packages(prohibited_packages=prohibited_packages_listner)))

    # Devs now only with poetry
    # with open("requirements.txt", 'w') as req_file:
    #     req_file.writelines("\n".join(get_packages(prohibited_packages=prohibited_packages_dev)))
