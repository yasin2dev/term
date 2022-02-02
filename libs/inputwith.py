from libs.printwith import Colors
from moduls.config import registeredColor

def inputWithColor(dir: str):
        if registeredColor.capitalize() == "Red":
                color = Colors.RED
        elif registeredColor.capitalize() == "Green":
                color = Colors.GREEN
        else:
                color = Colors.BLUE
        cmd = input(f'{color}{dir}:>{Colors.ENDC} ')
        return cmd