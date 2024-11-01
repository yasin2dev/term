from libs.printwith import *
from libs.emoji import *


# basic help template
def HelpText():
    printWithBold(Colors.YELLOW, (f"""
        Here is the Term Help!

        cd          Change Directory (default)
        ls          List Directory (default)
        lsdir       List Directories only
        lsf         List Files only
        restart     Restart Script (adjust main.py directory to shell.py)
        exit        Exit (default)
        shutdown    Turns off the PC.
        config      Configurate Term.

    """))

    printWithBold(Colors.GREEN, """
        help [topic]
        
        emojis      Print all emojis
        commands    Print all Term commands
    
    """)

    printWithRegular(Colors.YELLOW, "Colors: ")
    printWithRegular(Colors.BLUE, "BLUE")
    printWithRegular(Colors.GREEN, "GREEN")
    printWithRegular(Colors.CYAN, "CYAN")
    printWithRegular(Colors.RED, "RED")
    printWithRegular(Colors.MAGENTA, "MAGENTA")
    printlnWithRegular(Colors.YELLOW, "YELLOW")

#print all emojis from emoji.py
def emojisText():
    for i in emojis:
        print(i + " " + emojis[i])

#for term included commands
def termCommands():
    printWithBold(Colors.BLUE, """
                  Fetcherm [fetcherm]: Detailed PC Information Tool
                  """)