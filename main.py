#Term Version: 0.1.3-beta-1

#Import platform
import platform
import libs.dtime as dt
import libs.printwith as pw
import libs.inputwith as iw
import libs.getPc as getPc

from moduls.config import _showPc

#If OS is Windows bypass import
if platform.system() == 'Windows':
    pass
else:
    import libs.readline as rl


import moduls.shell as shell


if __name__ == "__main__":
    #If platform doesn't Windows run function.
    if platform.system() != "Windows":
        rl.arrowKeys()
    dt.dateAndTime()
    getPc.getUsername()
    if _showPc != "0":
        if platform.system() != 'Windows':
            getPc.getLinuxPc()
        else:
            getPc.getPc()
    else:
        pass
    shell.runShell(__file__)
