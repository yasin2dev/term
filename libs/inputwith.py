from libs.printwith import Colors, printlnWithBold
from moduls.config import registeredColor

def inputWithColor(dir: str):
        if registeredColor.capitalize() == "Red":
                color = Colors.RED
        elif registeredColor.capitalize() == "Green":
                color = Colors.GREEN
        elif registeredColor.capitalize() == "Yellow":
                color = Colors.YELLOW
        elif registeredColor.capitalize() == "Cyan":
                color = Colors.CYAN
        elif registeredColor.capitalize() == "Blue":
                color = Colors.BLUE
        else:
                color = Colors.BLUE
        cmd = input(f'{color}{dir}:>{Colors.ENDC} ')
        return cmd