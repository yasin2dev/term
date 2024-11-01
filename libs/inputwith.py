from libs.printwith import Colors, printlnWithBold
from moduls.config import registeredColor
from libs.defines import User

def inputWithColor(dir: str):
        #Colors fetching from .term_config file.
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
        elif registeredColor.capitalize() == "Magenta":
                color = Colors.MAGENTA
        else:
                color = Colors.BLUE
        # Input template
        cmd = input(f'{Colors.BOLD}{Colors.CYAN}[{User.username}{Colors.RED}@{Colors.BLUE}{User.host}]:~{color}{dir}:>{Colors.ENDC} ')
        return cmd