import sys
import os
import paramiko
import jinja2
from subprocess import Popen, PIPE


if __name__ == "__main__":
    course_root = sys.argv[1]

    branch_name = os.environ["CURRENT_BRANCH"].replace("/", "_")
    host = os.environ["AWS_HOST"]
    user = os.environ["AWS_USER"]
    ssh_key = os.environ["SSH_KEY"]

    remote_path = "/course"

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        hostname=host,
        port=22,
        username=user,
        key_filename=ssh_key,
    )

    stdin, stdout, stderr = ssh_client.exec_command(f"ls {remote_path}")

    existed_branches = []
    for f_ in stdout.readlines():
        if "." in f_[:-1]:
            continue
        else:
            existed_branches.append(f_[:-1])

    if branch_name not in existed_branches:
        ssh_client.exec_command(f"mkdir {remote_path}/branch_name")
        existed_branches.append(branch_name)

    template_loader = jinja2.FileSystemLoader(searchpath=f"{course_root}/tools/")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("index.jinja2")
    rendered = template.render(branches=existed_branches)

    with open(os.path.join(course_root, "index.html"), "w") as f_:
        f_.write(rendered)

    ftp_client = ssh_client.open_sftp()
    ftp_client.put(
        os.path.join(course_root, "index.html"), os.path.join(remote_path, "index.html")
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

    if res != 0:
        raise ValueError("gzip failed")

    ftp_client.put(
        os.path.join(course_root, "build.tar.gz"),
        os.path.join(remote_path, "build.tar.gz"),
    )

    stdin, stdout, stderr = ssh_client.exec_command(
        f"tar -xzf {remote_path}/build.tar.gz --directory {remote_path}/{branch_name}"
    )
    stdin, stdout, stderr = ssh_client.exec_command(
        f"mv {remote_path}/{branch_name}/qmlcourseRU/_build {remote_path}/{branch_name}/"
    )
    stdin, stdout, stderr = ssh_client.exec_command(
        f"rm -r {remote_path}/{branch_name}/qmlcourseRU"
    )
