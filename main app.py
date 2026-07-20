
import subprocess
import os

def run_programs():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app1 = os.path.join(current_dir, 'Psiphon3.exe')
    app2 = os.path.join(current_dir, 'Psiphon.exe')

    processes = []
    try:
        process1 = subprocess.Popen([app1])
        processes.append(process1)

        process2 = subprocess.Popen([app2], creationflags=subprocess.CREATE_NO_WINDOW)
        processes.append(process2)
    except:
        pass

if __name__ == '__main__':
    run_programs()
