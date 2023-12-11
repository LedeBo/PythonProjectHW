import subprocess
from main import check_command
import pytest

folder_in = ' /home/ledebo/folder_in'
folder_out = ' /home/ledebo/folder_out'
folder_ex = ' /home/ledebo/folder_ex'

# def test_step_1():
#     assert check_command(f'cd {folder_in}; 7z a {folder_out}/archieve_1', 'Everything is Ok')
#
# def test_step_2():
#     assert check_command(f'cd {folder_out}; 7z d archieve_1', "Everything is Ok")
#
#
# def test_step_3():
#     assert check_command(f'cd {folder_in}; 7z a {folder_ex}/archieve_2', "Everything is Ok")

def test_step_4():
    assert check_command(f'cd {folder_ex}; 7z rn archieve_2 file_1 f_1 file_2 f_2 file_3 f_3', "Everything is Ok")


if __name__=='__main__':
    pytest.main(['-vv'])