import os
from libs.printwith import *

def ListDir(path):
    items = os.scandir(path)
    for i in items:
        if os.path.isdir(i):
            printWithRegular(Colors.GREEN, "Directory: " + i.name)
        else:
            printWithRegular(Colors.RED, "File: " + i.name)

def onlyDirs(path):
    items = os.scandir(path)
    for i in items:
        if os.path.isdir(i):
            printWithRegular(Colors.GREEN, "Directory: " + i.name)
        else:
            pass

def onlyFiles(path):
    items = os.scandir(path)
    for i in items:
        if os.path.isfile(i):
            printWithRegular(Colors.RED, "File: " + i.name)
        else:
            pass