import yaml
from ssh_checkers import ssh_checkout
from ssh_checkers import upload_files

with open('config.yaml') as f:
    data = yaml.safe_load(f)

def test_step_d():
    res = []
    upload_files(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'{data.get("local_path")}{data.get("file")}.deb', f'{data.get("remote_path")}{data.get("file")}.deb')
    res.append(ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'echo {data.get("pswd")} | sudo -S dpkg -i {data.get("remote_path")}{data.get("file")}.deb',
    "Настраивается пакет"))
    res.append(ssh_checkout(f'{data.get("host")}', f'{data.get("user")}', f'{data.get("pswd")}', f'echo {data.get("pswd")} | sudo -S dpkg -s {data.get("file")}',
    "Status: install ok installed"))
    print(res)
    return all(res)



def test_step1(make_folders, clear_folders, make_files, stat):

    res1 = ssh_checkout(data["host"], data["user"], data["passwd"],
                        "cd {}; 7z a {}/arx1.7z ".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), ""
    res2 = ssh_checkout(data["host"], data["user"], data["passwd"],
                        "ls {}".format(data["folder_out"]), "arx.7z"), ""
    assert res1 and res2, ""


def test_step3(stat):

    assert ssh_checkout(data["host"], data["user"], data["passwd"],
                        "cd {}; 7z t {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), ""


def test_step4(make_folders, clear_folders):

    assert ssh_checkout(data["host"], data["user"], data["passwd"],
                        "cd {}; 7z u {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), ""




