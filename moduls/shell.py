import os

import libs.dtime as dt
import libs.printwith as pw
import libs.inputwith as iw

import moduls.help as help
import moduls.ls as ls
import moduls.config as cfg

from commands.cmd import *

def runShell(path):
    while (True):

        cdPrefix = "cd"
        currentDir = os.getcwd()
        cmd = iw.inputWithColor(currentDir)

        if cmd == "restart":
            shellRestart(path)

        elif cmd.startswith(cdPrefix):
            changeDirectory(cmd)
        elif cmd == "dt":
            dt.dateAndTime()
        elif cmd == "exit":
            exit(0)

        elif cmd == "ls":
            if os.name == "nt":
                ls.ListDir(str(os.getcwd()))
            else:
                ls.ListDir(str(os.getcwd()))
        elif cmd == "lsdir":
            ls.onlyDirs(str(os.getcwd()))
        elif cmd == "lsf":
            ls.onlyFiles(str(os.getcwd()))
        elif cmd == "help":
            help.HelpText()
        elif cmd == "help emojis":
            help.emojisText()
        elif cmd == "shutdown":
            shutdown()
        elif cmd == "config":
            cfg.startConfig()
        elif cmd == "fetcherm":
            TermCommands.runFetcherm()
        else:
            os.system(cmd)


def shellRestart(path):
    if os.name == "nt":
        os.system("python main.py")
        exit()
    else:
        os.system("python " + path)

def changeDirectory(cmd):
    try:
        ncmd = cmd.split()
        os.chdir(ncmd[1])
    except FileNotFoundError:
        pw.printWithBold(pw.Colors.RED,
                      "Sorry! I can't find your directory!")

def shutdown():
    sure = input("Are you sure? (yes / no): ")
    if sure == 'yes':
        os.system("shutdown /s /t 1")
    elif sure == 'no':
        return
    else:
        pw.printWithRegular(pw.Colors.RED, "Plese enter 'yes' or 'no'"),
        pass


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

