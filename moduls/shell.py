import os
from libs.printwith import *
import moduls.help as help
import moduls.ls as ls
import libs.inputwith as iw
import moduls.config as cfg

def runShell():
    while (True):

        cdPrefix = "cd"
        currentDir = os.getcwd()
        cmd = iw.inputWithColor(currentDir)

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
                ls.ListDir(str(os.getcwd()))
            else:
                os.system("ls")            
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
        elif cmd == "config":
            cfg.startConfig()
        else:
            os.system(cmd)