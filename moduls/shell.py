import os
from printwith import *
import moduls.help as help
import time

def runShell():
    while (True):

        cdPrefix = "cd"
        currentDir = os.getcwd()
        cmd = input(f'\33[94m{currentDir}:> \33[0m'.format(currentDir))

        if cmd == "restart":
            if os.name == "nt":
                os.system("python main.py")
                exit()
            else:
                os.system("python3 main.py")
        
        elif cmd.startswith(cdPrefix):
            try:
                ncmd = cmd.split()
                os.chdir(ncmd[1])
            except FileNotFoundError:
                printWithBold(Colors.RED, Colors.BOLD, "Sorry! I can't find your directory!")
        elif cmd == "exit":
            exit()
        
        elif cmd == "ls":
            if os.name == "nt":
                os.system("dir")
            else:
                os.system("ls")            
            # In the future, I will create custom 'ls' commands.
        elif cmd == "help":
            help.HelpText()
        elif cmd == "shutdown":
            sure = input("Are you sure? (yes / no): ")
            if sure == 'yes':
                os.system("shutdown /s /t 1")
            elif sure == 'no':
                return
            else:
                printWithRegular(Colors.RED, "Plese enter 'yes' or 'no'"),
                pass
        else:
            os.system(cmd)