import os

import libs.dtime as dt
import libs.printwith as pw
import libs.inputwith as iw

import moduls.help as help
import moduls.ls as ls
import moduls.config as cfg

from commands.cmd import *

## RUN SHELL

def runShell(path):
    while (True):

        cdPrefix = "cd"
        currentDir = os.getcwd()
        cmd = iw.inputWithColor(currentDir)

        if cmd == "restart":
            shellRestart(path)

        # Combine cls and clear command for clear the command screen
        elif cmd == "clear" and "cls":
            os.system("cls")

        # If command starts with change directory prefix
        elif cmd.startswith(cdPrefix):
            changeDirectory(cmd)
        # Show date and time
        elif cmd == "dt":
            dt.dateAndTime()
        # Exit program
        elif cmd == "exit":
            exit(0)

        # list all files and directories
        elif cmd == "ls":
            if os.name == "nt":
                ls.ListDir(str(os.getcwd()))
            else:
                ls.ListDir(str(os.getcwd()))

        #list just directories
        elif cmd == "lsdir":
            ls.onlyDirs(str(os.getcwd()))
        
        #list just files
        elif cmd == "lsf":
            ls.onlyFiles(str(os.getcwd()))

        #run help command
        elif cmd == "help":
            help.HelpText()
        
        # List emoji list

        elif cmd == "help emojis":
            help.emojisText()

        # List commands via help
        elif cmd == "help commands":
            help.termCommands()
        
        # Shutdown PC (it's asking)
        elif cmd == "shutdown":
            shutdown()
        
        #start configurate term.
        elif cmd == "config":
            cfg.startConfig()
        
        ### Term Included commands

        #List PC specs via fetcherm

        elif cmd == "fetcherm":
            TermCommands.runFetcherm()
        else:
            os.system(cmd)


### Self functions for shell

def shellRestart(path):
    if os.name == "nt":
        os.system("python main.py")
        exit()
    else:
      # check if there is no 'python' package, run with python3
      from shutil import which
      if which("python") is None:
        os.system("python3 main.py")


# Change Directory function
def changeDirectory(cmd):
    try:
        # split input and get path -like array-
        ncmd = cmd.split()
        os.chdir(ncmd[1])
    except FileNotFoundError:
        pw.printWithBold(pw.Colors.RED,
                      "Sorry! I can't find your directory!")


# Shutdown command
def shutdown():
    sure = input("Are you sure? (yes / no): ")
    if sure == 'yes':
        os.system("shutdown /s /t 1")
    elif sure == 'no':
        return
    else:
        pw.printWithRegular(pw.Colors.RED, "Plese enter 'yes' or 'no'"),
        pass


## This function allow you to run shell commands externally in another file.
def runShellCommandsExternal(cmd, path):
    commands = ['restart', 'cd', 'exit', 'ls', 'help', 'shutdown', 'config', 'dt']
    if cmd == 'exit':
        exit()
    elif cmd == 'restart':
        shellRestart(path)
    elif cmd == 'cd':
        print("cd? are you serious mate? PASS!")
        pass
    elif cmd == 'ls':
        ls.ListDir(os.getcwd())
    elif cmd == 'help':
        help.HelpText()
    else:
        pass

