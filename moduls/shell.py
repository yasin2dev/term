import os
from printwith import *
import moduls.help as help

def runShell():
    while (True):

        cdPrefix = "cd"
        currentDir = os.getcwd()
        cmd = input(f'\33[94m{currentDir}:> \33[0m'.format(currentDir))

        if cmd == "restart":
            os.system("python main.py")
            print("Restarting...")
            exit()
        
        elif cmd.startswith(cdPrefix):
            try:
                ncmd = cmd.split()
                os.chdir(ncmd[1])
            except FileNotFoundError:
                printWithBold(Colors.RED, Colors.BOLD, "Sorry! I can't find your directory!")
        elif cmd == "exit":
            exit()
        
        elif cmd == "ls":
            os.system("dir")
            # In the future, I will create custom 'ls' commands.
        elif cmd == "help":
            help.HelpText()
        else:
            os.system(cmd)