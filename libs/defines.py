import getpass, os
import socket

class Colors: 
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    GREEN = '\033[92m'
    CYAN = '\033[36m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    WHITE = '\x1B[1;37m' 

class Paths:
    main_path = os.path.abspath("./main.py")

class User:
    username = getpass.getuser()
    host = socket.gethostname()
    home = os.path.expanduser("~")