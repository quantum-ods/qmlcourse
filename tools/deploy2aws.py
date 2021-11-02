import sys
import os
import paramiko
import scp
import jinja2


if __name__ == "__main__":
    course_root = sys.argv[1]

    branch_name = os.environ["CURRENT_BRANCH"].replace("/", "_")
    host = os.environ["AWS_HOST"]
    user = os.environ["AWS_USER"]
    ssh_key = os.environ["SSH_KEY"]

    remote_path = os.path.join("/course/", branch_name)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(
        hostname=host,
        port=22,
        username=user,
        key_filename=ssh_key,
    )

    stdin, stdout, stderr = ssh_client.exec_command("ls /course")

    existed_branches = []
    for f_ in stdout.readlines():
        if "." in f_[:-1]:
            continue
        else:
            existed_branches.append(f_[:-1])

    if branch_name not in existed_branches:
        ssh_client.exec_command(f"mkdir /course/branch_name")
        existed_branches.append(branch_name)

    template_loader = jinja2.FileSystemLoader(searchpath=f"{course_root}/tools/")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("index.jinja2")
    rendered = template.render(branches=existed_branches)
