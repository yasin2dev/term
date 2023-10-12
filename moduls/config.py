import os
import moduls.shell as shell
from libs.defines import *

if os.path.isfile(".term_config"):
    pass
else:
    open(".term_config", "w+").close()


def startConfig():
    with open(".term_config", "a") as f:
        f.truncate(0)
    with open(".term_config", "a") as f:
        #for command input
        colorTo = input("Plese choose color (colors: 'help'): ")
        welcomeTo = input("Welcome text: ")
        f.write(f"INPUT_COLOR: {colorTo}\n")
        f.write(f"WELCOME_TEXT: {welcomeTo}\n")
        f.close()
        shell.runShellCommandsExternal("restart")
    
with open(".term_config", "r") as f:
    getColor = f.readline()
    getWelcome = f.readline()
    _welcomeText = getWelcome.replace("\n", "")[14:]
    registeredColor = getColor.replace("\n", "")[13:]