import os
from printwith import *

while (True):

    cdPrefix = "cd"
    currentDir = os.getcwd()
    cmd = input(f'\33[94m{currentDir}:>\33[0m'.format(currentDir))

    if cmd == "restart":
        os.system("python main.py")
        print("Restarting...")
        exit()
        
    elif cmd.startswith(cdPrefix):
        try:
            ncmd = cmd.split()
            os.chdir(ncmd[1])
        except FileNotFoundError:
            printWith(Colors.RED, Colors.BOLD, "Sorry! I can't find your directory!")
    else:
        os.system(cmd)