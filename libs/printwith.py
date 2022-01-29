from libs.emojiSupport import Emojis


class Colors: 
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    GREEN = '\033[92m'
    CYAN = '\033[36m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    YELLOW = '\033[33m'

def printWithBold(color: Colors, b: Colors, text):
    print(color + b + text + Colors.ENDC)

def printWithEmoji(color: Colors, text: str, emj: Emojis):
    print(color + text + emj + Colors.ENDC)

def printWithRegular(color: Colors, text):
    print(color + text + Colors.ENDC)