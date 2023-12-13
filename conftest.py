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
                                      data["folder_home"]),
        "")


@pytest.fixture()
def clear_folders():
    return check_command("rm -rf {}/* {}/* {}/* {}/*".format(data["folder_in"], data["folder_out"], data["folder_ex"],
                                            data["folder_ex2"]), "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(5):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if check_command("cd {}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], filename),
                ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not check_command("cd {}; mkdir {}".format(data["folder_in"], subfoldername), ""):
        return None, None
    if not check_command("cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data["folder_in"], subfoldername,
                                                                                      testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture()
def make_ex2():
    check_command("cd {}; 7z a {}/ex2.7z".format(data["folder_in"], data["folder_ex2"]), "Everything is Ok")
    check_command("truncate -s l {}/ex2.7z".format(data["folder_ex2"]), "Everything is Ok")
    yield "ex2"
    check_command("rm -f {}/ex2.7z".format(data["folder_ex2"]), "")




@pytest.fixture()
def stat():
    yield "stat"
    check_command("cat /proc/loadavg >> {}/{}".format(data["folder_home"], "stat.txt"), "")
    check_command("echo {}>> {}/{}".format(datetime.now().strftime("%H:%M:%S.%f"), data["folder_home"], "stat.txt"),
                      "")
    check_command("echo {} >> {}/{}".format(str(data["count_file"]), data["folder_home"], "stat.txt"), "")
    check_command("echo  {} >> {}/{}".format(data["size_file"], data["folder_home"], "stat.txt"), "")