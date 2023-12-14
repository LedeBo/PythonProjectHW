import random
import string
import subprocess
import pytest
from main import check_command
import yaml
from datetime import datetime

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return check_command("mkdir {} {} {} {} {}".format(data["folder_in"], data["folder_out"], data["folder_ex"], data["folder_ex2"],
                                      data["remote_path"]),
        "")


@pytest.fixture()
def clear_folders():
    return check_command("rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ex"],
                                            data["folder_ex2"]), "")


@pytest.fixture()
def make_ex2():
    check_command("cd {}; 7z a {}/ex2.7z".format(data["folder_in"], data["folder_ex2"]), "Everything is Ok")
    check_command("truncate -s l {}/ex2.7z".format(data["folder_ex2"]), "Everything is Ok")
    yield "ex2"
    check_command("rm -f {}/ex2.7z".format(data["folder_ex2"]), "")


@pytest.fixture()
def stat():
    yield "stat"
    check_command("cat /proc/loadavg >> {}/{}".format(data["remote_path"], 'stat.txt'), "")
    check_command("echo {}>> {}/{}".format(datetime.now().strftime("%H:%M:%S.%f"), data["remote_path"], "stat.txt"),
                      "")
    check_command("echo {} >> {}/{}".format(str(data["count_file"]), data["remote_path"], "stat.txt"), "")
    check_command("echo  {} >> {}/{}".format(data["size_file"], data["remote_path"], "stat.txt"), "")