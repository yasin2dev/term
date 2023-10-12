import getpass 
import platform, psutil, json

from libs.printwith import *
from moduls.config import _welcomeText


def is_64bit():
    return platform.machine().endswith('64')


def getPc():
    info={}
    info['platform']=platform.system()
    info['platform-release']=platform.release()
    info['platform-version']=platform.version()
    info['chip-arch']=platform.machine()
    info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+ " GB"
    x = json.dumps(info)
    p = json.loads(x)
    printWithBold(Colors.GREEN, Colors.BOLD, "OS: " + p['platform'] + " " + p['platform-release'])
    printWithBold(Colors.GREEN, Colors.BOLD, "Version: " + p['platform-version'])
    printWithBold(Colors.GREEN, Colors.BOLD, "Platform: " + str(p['chip-arch']))
    if is_64bit():
        printWithBold(Colors.GREEN, Colors.BOLD, "Architecture: 64 bit")
    else:
        printWithBold(Colors.GREEN, Colors.BOLD, "Architecture: 32 bit")
    printWithBold(Colors.GREEN, Colors.BOLD, "RAM: " + p['ram'])
    print("\n")

def getUsername():
    username = getpass.getuser()

    if _welcomeText == "":
        printlnWithEmoji(Colors.BLUE, "Welcome to Term " + username, Emojis.smiling_with_heart_eyes)
    else:
        printlnWithEmoji(Colors.BLUE, _welcomeText, Emojis.smiling_with_heart_eyes)