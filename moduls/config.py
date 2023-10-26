import os
import moduls.shell as shell
from libs.defines import *
from libs.printwith import *

import shutil

home = User.home

if os.path.isfile(f"{home}/.term_config"):
    pass
else:
    open(f"{home}/.term_config", "w+").close()

    with open(f"{home}/.term_config", "a") as f:
        f.truncate(0)
        f.close()

def prepareConfig():
    shutil.copy(f"{home}/.term_config", f"{home}/.old_term_config")
    printlnWithBold(Colors.GREEN, f"Old configuration file copied to {home}/.old_term_config")
    with open(f"{home}/.term_config", "a") as f:
        f.truncate(0)
        f.close()

def startConfig():
    _sconfig = input("Are you sure to reconfigure Term? (y | n): ")
    if _sconfig == "y":
        prepareConfig()
    else:
        return
    with open(f"{home}/.term_config", "a") as f:
        #for command input
        cmdColorTo = input("Plese choose color (colors: 'help'): ")
        welcomeColorTo = input("Welcome text: ")
        pcInfoColor = input("PC Info text color: ")
        showPc = input("Show PC Info on startup (1: yes, 0: no): ")
        emoji = input("Choose an emoji (for emojis: help emojis): ")
        welcomeTextColor = input("Welcome Text Color: ")
        f.write(f"INPUT_COLOR: {cmdColorTo}\n")
        f.write(f"WELCOME_TEXT: {welcomeColorTo}\n")
        f.write(f"PC_INFO_COLOR: {pcInfoColor}\n")
        f.write(f"SHOW_PC_INFO: {showPc}\n")
        f.write(f"WELCOME_EMOJI: {emoji}\n")
        f.write(f"WELCOME_TEXT_COLOR: {welcomeTextColor}")
        input("You can do more customization in .term_config soon.\n")
        f.close()
        shell.runShellCommandsExternal("restart", Paths.main_path)

with open(f"{home}/.term_config", "r") as f:
    getColor = f.readline()
    getWelcome = f.readline()
    getPcInfo = f.readline()
    getShowPc = f.readline()
    getEmoji  = f.readline()
    getWelcomeColor = f.readline()
    _welcomeText = getWelcome.replace("\n", "")[14:]
    registeredColor = getColor.replace("\n", "")[13:]
    _pcInfoColor = getPcInfo.replace("\n", "")[15:]
    _showPc = getShowPc.replace("\n", "")[14:]
    _emoji = getEmoji.replace("\n", "")[15:]
    _welcomeTextColor = getWelcomeColor.replace("\n", "")[20:]
    print(_welcomeTextColor)