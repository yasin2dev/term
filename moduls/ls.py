import os
from libs.printwith import *


#listing current directory with files and folders.
def ListDir(path):
    items = os.scandir(path)
    for i in items:
        if os.path.isdir(i):
            printWithRegular(Colors.GREEN, "Directory: " + i.name)
        else:
            printWithRegular(Colors.RED, "File: " + i.name)

#listing only directorys in current directory
def onlyDirs(path):
    items = os.scandir(path)
    for i in items:
        if os.path.isdir(i):
            printWithRegular(Colors.GREEN, "Directory: " + i.name)
        else:
            pass

#listing only files in current directory
def onlyFiles(path):
    items = os.scandir(path)
    for i in items:
        if os.path.isfile(i):
            printWithRegular(Colors.RED, "File: " + i.name)
        else:
            pass