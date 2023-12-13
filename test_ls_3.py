import yaml
from main import check_command

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(make_folders, clear_folders, make_files, stat):

    res1 = check_command("cd {}; 7z a {}/arx1.7z ".format(data["folder_in"], data["folder_out"]),
                             "Everything is Ok"), ""
    res2 = check_command("ls {}".format(data["folder_out"]), "arx.7z"), ""
    assert res1 and res2, ""


def test_step2(clear_folders, make_files, stat):

    res = []
    res.append(check_command("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    res.append(check_command("cd {}; 7z e arx1.7z -o{} -y".format(data["folder_out"], data["folder_ex"]),
                                 "Everything is Ok"))
    for item in make_files:
        res.append(check_command("ls {}".format(data["folder_ex"]), ""))
    assert all(res)


def test_step3(stat):

    assert check_command("cd {}; 7z t {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                             "Everything is Ok"), ""


def test_step4(make_folders, clear_folders, make_files):

    assert check_command("cd {}; 7z u {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                             "Everything is Ok"), ""


def test_step5(clear_folders, make_files, stat):

    res = []
    res.append(
        check_command("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    for item in make_files:
        res.append(check_command("cd {}; 7z l arx1.7z".format(data["folder_out"]), item))
    assert all(res)





def test_step6(stat):
    assert check_command("7z d {}/arx1.7z".format(data["folder_out"]), "Everything is Ok"), ""


def test_step7(make_files, stat):

    assert check_command("7z t {}/{}".format(data['folder_out'], data['name_of_arch']),
                             "Everything is Ok"), ""