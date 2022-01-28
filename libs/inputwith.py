from turtle import color
from libs.printwith import Colors
from moduls.config import registeredColor

def inputWithColor(dir: str):
        if registeredColor == "RED":
                color = Colors.RED
        elif registeredColor == "GREEN":
                color = Colors.GREEN
        else:
                color = Colors.BLUE
        cmd = input(f'{color}{dir}:>{Colors.ENDC} ')
        return cmd