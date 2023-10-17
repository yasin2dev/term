import getpass 
import platform, psutil, json, distro

from libs.printwith import *
from moduls.config import _welcomeText, _pcInfoColor


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
    info={}
    info['platform']=str(distro.linux_distribution()[0])
    info['platform-release']=str(platform.release())
    info['platform-version']=distro.version()
    info['chip-arch']=platform.machine()
    info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+ " GB"
    x = json.dumps(info)
    p = json.loads(x)
    printWithBold(color, Colors.BOLD, "OS: " + p['platform'] + " " + p['platform-version'])
    printWithBold(color, Colors.BOLD, "Release: " + p['platform-release'])
    printWithBold(color, Colors.BOLD, "Platform: " + str(p['chip-arch']))
    if is_64bit():
        printWithBold(color, Colors.BOLD, "Architecture: 64 bit")
    else:
        printWithBold(color, Colors.BOLD, "Architecture: 32 bit")
    printWithBold(color, Colors.BOLD, "RAM: " + p['ram'])
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
    printWithBold(color, Colors.BOLD, "OS: " + p['platform'] + " " + p['platform-release'])
    printWithBold(color, Colors.BOLD, "Version: " + p['platform-version'])
    printWithBold(color, Colors.BOLD, "Platform: " + str(p['chip-arch']))
    if is_64bit():
        printWithBold(color, Colors.BOLD, "Architecture: 64 bit")
    else:
        printWithBold(color, Colors.BOLD, "Architecture: 32 bit")
    printWithBold(color, Colors.BOLD, "RAM: " + p['ram'])
    print("\n")

def getUsername():
    username = getpass.getuser()

    if _welcomeText == "":
        printlnWithEmoji(Colors.BLUE, "Welcome to Term " + username, Emojis.smiling_with_heart_eyes)
    else:
        printlnWithEmoji(Colors.BLUE, _welcomeText, Emojis.smiling_with_heart_eyes)