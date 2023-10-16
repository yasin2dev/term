import os
import moduls.shell as shell
from libs.defines import *
from libs.printwith import *

if os.path.isfile(".term_config"):
    pass
else:
    open(".term_config", "w+").close()


def startConfig():
    with open(".term_config", "a") as f:
        f.truncate(0)
    with open(".term_config", "a") as f:
        #for command input
        cmdColorTo = input("Plese choose color (colors: 'help'): ")
        welcomeColorTo = input("Welcome text: ")
        pcInfoColor = input("PC Info text color: ")
        f.write(f"INPUT_COLOR: {cmdColorTo}\n")
        f.write(f"WELCOME_TEXT: {welcomeColorTo}\n")
        f.write(f"PC_INFO_COLOR: {pcInfoColor}")
        input("You can do more customization in .term_config soon.\n")
        f.close()
        shell.runShellCommandsExternal("restart", Paths.main_path)

with open(".term_config", "r") as f:
    getColor = f.readline()
    getWelcome = f.readline()
    getPcInfo = f.readline()
    _welcomeText = getWelcome.replace("\n", "")[14:]
    registeredColor = getColor.replace("\n", "")[13:]
    _pcInfoColor = getPcInfo.replace("\n", "")[15:]