from libs.filerm import filerm
from libs.printwith import *
from libs.defines import Colors

def fetcherm():
    printlnWithBold(Colors.GREEN, "\nWelcome to Fetcherm")
    
    printWithBold(Colors.YELLOW, f"OS:  {Colors.WHITE}{filerm.getOS('os-name')}")
    printWithBold(Colors.YELLOW, f"Kernel: {Colors.WHITE}{filerm.getOS('kernel')}")
    printWithBold(Colors.YELLOW, f"Shell: {Colors.WHITE}{filerm.getOS('shell')}")
    printWithBold(Colors.YELLOW, f"DE: {Colors.WHITE}{filerm.getOS('desktop-env')}")
    printWithBold(Colors.YELLOW, f"WM: {Colors.WHITE}{filerm.getOS('window-mngr').capitalize()}")
    printWithBold(Colors.YELLOW, f"Theme: {Colors.WHITE}{filerm.ReadTheme()}")

    printWithBold(Colors.YELLOW, f"CPU: {Colors.WHITE}{filerm.ReadCPU()}")
    printWithBold(Colors.YELLOW, f"GPU: {Colors.WHITE}{filerm.ReadGPU()}")
    printWithBold(Colors.YELLOW, f"Memory: {Colors.WHITE}{filerm.CurrentRam() + ' / ' + filerm.ReadMemory('mb')}\n")