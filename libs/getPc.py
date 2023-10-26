import platform, psutil, json, distro
from libs.filerm import filerm
from libs.printwith import *
from libs.emoji import *
from libs.defines import User
from moduls.config import _welcomeText, _pcInfoColor, _emoji, _welcomeTextColor


def is_64bit():
    return platform.machine().endswith('64')

if _pcInfoColor.capitalize() == "Red":
    color = Colors.RED
elif _pcInfoColor.capitalize() == "Green":
   color = Colors.GREEN
elif _pcInfoColor.capitalize() == "Yellow":
        color = Colors.YELLOW
elif _pcInfoColor.capitalize() == "Cyan":
        color = Colors.CYAN
elif _pcInfoColor.capitalize() == "Blue":
        color = Colors.BLUE
elif _pcInfoColor.capitalize() == "Magenta":
        color = Colors.MAGENTA
else:
        color = Colors.BLUE

def getLinuxPc():
    printWithBold(color, "OS: " + filerm.getOS("os-name"))
    printWithBold(color, "Release: " + filerm.getOS("kernel"))
    printWithBold(color, "Platform: " + str(platform.machine()))
    if is_64bit():
        printWithBold(color, "Architecture: 64 bit")
    else:
        printWithBold(color, "Architecture: 32 bit")
    printWithBold(color, "RAM: " + filerm.ReadMemory("gb"))
    print("\n")

def getPc():
    info={}
    info['platform']=platform.system()
    info['platform-release']=platform.release()
    info['platform-version']=platform.version()
    info['chip-arch']=platform.machine()
    info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+ " GB"
    x = json.dumps(info)
    p = json.loads(x)
    printWithBold(color, "OS: " + p['platform'] + " " + p['platform-release'])
    printWithBold(color, "Version: " + p['platform-version'])
    printWithBold(color, "Platform: " + str(p['chip-arch']))
    if is_64bit():
        printWithBold(color, "Architecture: 64 bit")
    else:
        printWithBold(color, "Architecture: 32 bit")
    printWithBold(color, "RAM: " + p['ram'])
    print("\n")


## There is no switch case for Python
if _welcomeTextColor.capitalize() == "Red":
    Wcolor = Colors.RED
elif _welcomeTextColor.capitalize() == "Green":
   Wcolor = Colors.GREEN
elif _welcomeTextColor.capitalize() == "Yellow":
        Wcolor = Colors.YELLOW
elif _welcomeTextColor.capitalize() == "Cyan":
        Wcolor = Colors.CYAN
elif _welcomeTextColor.capitalize() == "Blue":
        Wcolor = Colors.BLUE
elif _welcomeTextColor.capitalize() == "Magenta":
        Wcolor = Colors.MAGENTA
else:
        Wcolor = Colors.BLUE

def getUsername():
    if _welcomeText == "":
        printlnWithBold(Wcolor, "Welcome to Term " + User.username + emojipy(_emoji))
    else:
        printlnWithBold(Wcolor, _welcomeText + " " + emojipy(_emoji))