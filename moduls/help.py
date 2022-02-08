from libs import printwith


def HelpText():
    printwith.printWithRegular(printwith.Colors.YELLOW, ("""
        Here is the Term Help!

        cd          Change Directory (default)
        ls          List Directory (default)
        restart     Restart Script (adjust main.py directory to shell.py)
        exit        Exit (default)
        shutdown    Turns off the PC.

        Colors: BLUE, GREEN, CYAN, RED, YELLOW
    """))
