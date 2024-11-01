from libs.defines import *


#print with Colors. bold, regular, with space, line etc.

def printlnWithBold(color: Colors, text):
    print(color + Colors.BOLD + text + Colors.ENDC + "\n")

def printlnWithRegular(color: Colors, text):
    print(color + text + Colors.ENDC + "\n")

def printWithBold(color: Colors, text):
    print(color + Colors.BOLD + text + Colors.ENDC)

def printWithRegular(color: Colors, text):
    print(color + text + Colors.ENDC)