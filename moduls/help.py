from libs.printwith import *


def HelpText():
    printWithRegular(Colors.YELLOW, (f"""
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
    printWithRegular(Colors.YELLOW, "Colors: ")
    printWithRegular(Colors.BLUE, "BLUE")
    printWithRegular(Colors.GREEN, "GREEN")
    printWithRegular(Colors.CYAN, "CYAN")
    printWithRegular(Colors.RED, "RED")
    printWithRegular(Colors.MAGENTA, "MAGENTA")
    printlnWithRegular(Colors.YELLOW, "YELLOW")
                                     