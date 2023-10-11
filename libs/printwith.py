from libs.defines import *

def printlnWithBold(color: Colors, b: Colors, text):
    print(color + b + text + Colors.ENDC + "\n")

def printlnWithEmoji(color: Colors, text: str, emj: Emojis):
    print(color + text + emj + Colors.ENDC + "\n")

def printlnWithRegular(color: Colors, text):
    print(color + text + Colors.ENDC + "\n")

def printWithBold(color: Colors, b: Colors, text):
    print(color + b + text + Colors.ENDC)

def printWithEmoji(color: Colors, text: str, emj: Emojis):
    print(color + text + emj + Colors.ENDC)

def printWithRegular(color: Colors, text):
    print(color + text + Colors.ENDC)