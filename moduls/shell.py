import os

def runShell():
    while (True):
        currentDir = os.getcwd()
        cmd = input(f'\33[91m{currentDir}:>\33[0m'.format(currentDir))

        if cmd == "restart":
            os.system("python main.py")
            print("Restarting...")
            exit()
        else:
            os.system(cmd)