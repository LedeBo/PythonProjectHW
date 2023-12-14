import subprocess

def check_command(command, text):
    result = subprocess.run(command, shell=True, stdout = subprocess.PIPE, encoding='utf-8')

    print(result)

    out = result.stdout

    print(out)

    if result.returncode ==0 and text in out:
        print('TRUE')
        return True
    else:
        print('FALSE')
        return False



if __name__=='__main__':
     check_command('cd /home/ledebo/folder_ex; touch file_1', text='')
