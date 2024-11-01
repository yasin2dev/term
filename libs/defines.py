import getpass, os
import socket


## Color defines in ASCII codes
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

    TNRM = "\x1B[0m"    # normal 
    TBLK = "\x1B[0;30m" # black 
    TRED = "\x1B[0;31m" # red 
    TBRN = "\x1B[0;33m" # brown 
    TGRN = "\x1B[0;32m" # green 
    TBLU = "\x1B[0;34m" # blue 
    TPUR = "\x1B[0;35m" # purple 
    TCYN = "\x1B[0;36m" # cyan 
    TLGY = "\x1B[0;37m" # light gray 
    TDGY = "\x1B[1;30m" # dark gray 
    TLRD = "\x1B[1;31m" # light red 
    TLGN = "\x1B[1;32m" # light green   
    TYLW = "\x1B[1;33m" # yellow 
    TLBL = "\x1B[1;34m" # light blue 
    TLPR = "\x1B[1;35m" # light purple 
    TLCY = "\x1B[1;36m" # light cyan 
    TWHT = "\x1B[1;37m" # white


# Get main.py file absolute path.
class Paths:
    main_path = os.path.abspath("./main.py")


# User information
class User:
    username = getpass.getuser()
    host = socket.gethostname()
    home = os.path.expanduser("~")