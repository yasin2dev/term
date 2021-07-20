class Colors: 
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    GREEN = '\033[92m'
    CYAN = '\033[36m'
    BOLD = '\033[1m'
    RED = '\033[91m'

def printWithBold(color: Colors, b: Colors, text):
    print(color + b + text + Colors.ENDC)

def printWithRegular(color: Colors, text):
    print(color + text + Colors.ENDC)