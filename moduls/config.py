import os
import moduls.shell as shell
from libs.defines import *
from libs.printwith import *

import shutil

home = User.home

## kinda difficult but its actually readable.


# check? .term_file exist or not.
if os.path.isfile(f"{home}/.term_config"):
    pass
else:
    # open and insert default configuration into created .term_config file.
    open(f"{home}/.term_config", "w+").close()

    with open(f"{home}/.term_config", "a") as f:
        f.truncate(0)
        with open("default_conf.trm", "r") as w:
            for i in w:
                f.write(i)
            f.close()


# Preparing to configuration; backup old config file into .old_term_config then truncate it
def prepareConfig():
    shutil.copy(f"{home}/.term_config", f"{home}/.old_term_config")
    printlnWithBold(Colors.GREEN, f"Old configuration file copied to {home}/.old_term_config")
    with open(f"{home}/.term_config", "a") as f:
        f.truncate(0)
        f.close()


#start configuration
def startConfig():
    _sconfig = input("Are you sure to reconfigure Term? (y | n): ")
    if _sconfig == "y":
        prepareConfig()
    else:
        return
    #write input values to file
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
        #restart for refreshing.
        shell.runShellCommandsExternal("restart", Paths.main_path)


with open(f"{home}/.term_config", "r") as f:
    #delete whitespace char and another prefixes for file.
    data = tuple(f.readlines())
    for i in range(len(data)):
        if i == 0:
            registeredColor = data[i].replace("\n", "")[13:]
        elif i == 1:
            _welcomeText = data[i].replace("\n", "")[14:]
        elif i == 2:
            _pcInfoColor = data[i].replace("\n", "")[15:]
        elif i == 3:
            _showPc = data[i].replace("\n", "")[14:]
        elif i == 4:
            _emoji = data[i].replace("\n", "")[15:]
        elif i == 5:
            _welcomeTextColor = data[i].replace("\n", "")[20:]