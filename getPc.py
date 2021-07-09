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
    printWith(Colors.GREEN, Colors.BOLD, "OS: " + p['platform'] + " " + p['platform-release'])
    printWith(Colors.GREEN, Colors.BOLD, "Version: " + p['platform-version'])
    printWith(Colors.GREEN, Colors.BOLD, "Architecture: " + str(p['architecture']))
    printWith(Colors.GREEN, Colors.BOLD, "RAM: " + p['ram'])
    print("\n")
