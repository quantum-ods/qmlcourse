import os
import sys
import time
from subprocess import PIPE, Popen
from git import Repo
import re

import jinja2
import paramiko

if __name__ == "__main__":
    course_root = sys.argv[1]

    # branch_name = os.environ["CURRENT_BRANCH"].replace("/", "_")
    repo = Repo("./")
    branch_name = re.sub("-/",repo.active_branch.name,"_")

    host = os.environ["AWS_HOST"]
    user = os.environ["AWS_USER"]
    ssh_key = os.environ["SSH_KEY"]

    remote_path = "/course"

    print("Create SSH Client...")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        hostname=host,
        port=22,
        username=user,
        key_filename=ssh_key,
    )
    print("Done.")

    print("Get all folders/branches...")
    stdin, stdout, stderr = ssh_client.exec_command(f"ls {remote_path}")
    print(f"Done.")

    existed_branches = []
    for f_ in stdout.readlines():
        if "." in f_[:-1]:
            continue
        else:
            existed_branches.append(f_[:-1])
    print(f"Branches: {existed_branches}")

    if branch_name not in existed_branches:
        print(f"Execute mkdir {remote_path}/{branch_name}")
        ssh_client.exec_command(f"mkdir {remote_path}/{branch_name}")
        existed_branches.append(branch_name)

    print("Update index.html")
    template_loader = jinja2.FileSystemLoader(searchpath=f"{course_root}/tools/")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("index.jinja2")
    rendered = template.render(branches=existed_branches)

    with open(os.path.join(course_root, "index.html"), "w") as f_:
        f_.write(rendered)
    print("Done.")

    ftp_client = ssh_client.open_sftp()
    ftp_client.put(
        os.path.join(course_root, "index.html"), os.path.join(remote_path, "index.html")
    )

    print(
        f"Execute local: tar -zcf {course_root}/build.tar.gz {course_root}/qmlcourseRU/_build/"
    )
    process = Popen(
        [
            "tar",
            "-zcf",
            f"{course_root}/build.tar.gz",
            f"{course_root}/qmlcourseRU/_build/",
        ],
        stdout=PIPE,
        stderr=PIPE,
    )
    res = process.wait()
    print("Done.")

    if res != 0:
        raise ValueError("gzip failed")

    print("Put the build.tar.gz on the AWS machine...")
    ftp_client.put(
        os.path.join(course_root, "build.tar.gz"),
        os.path.join(remote_path, "build.tar.gz"),
    )
    print("Done.")

    print(
        f"execute tar -xzf {remote_path}/build.tar.gz --directory {remote_path}/{branch_name}"
    )
    stdin, stdout, stderr = ssh_client.exec_command(
        f"tar -xzf {remote_path}/build.tar.gz --directory {remote_path}/{branch_name}"
    )
    time.sleep(3)
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")

    print(f"Execute rm -r {remote_path}/{branch_name}/_build")
    stdin, stdout, stderr = ssh_client.exec_command(
        f"rm -r {remote_path}/{branch_name}/_build"
    )
    time.sleep(3)
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")

    print(
        f"Execute mv {remote_path}/{branch_name}/qmlcourseRU/_build {remote_path}/{branch_name}/"
    )
    stdin, stdout, stderr = ssh_client.exec_command(
        f"mv {remote_path}/{branch_name}/qmlcourseRU/_build {remote_path}/{branch_name}/"
    )
    time.sleep(3)
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")

    print(f"Execute rm -r {remote_path}/{branch_name}/qmlcourseRU")
    stdin, stdout, stderr = ssh_client.exec_command(
        f"rm -r {remote_path}/{branch_name}/qmlcourseRU"
    )
    time.sleep(3)
    print(f"stdout: {stdout}")
    print(f"stderr: {stderr}")
