import platform, psutil, json
from printwith import *


def getPc():
    info={}
    info['platform']=platform.system()
    info['platform-release']=platform.release()
    info['platform-version']=platform.version()
    info['architecture']=platform.architecture()
    info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+ " GB"
    x = json.dumps(info)
    p = json.loads(x)
    printWithBold(Colors.GREEN, Colors.BOLD, "OS: " + p['platform'] + " " + p['platform-release'])
    printWithBold(Colors.GREEN, Colors.BOLD, "Version: " + p['platform-version'])
    printWithBold(Colors.GREEN, Colors.BOLD, "Architecture: " + str(p['architecture']))
    printWithBold(Colors.GREEN, Colors.BOLD, "RAM: " + p['ram'])
    print("\n")
