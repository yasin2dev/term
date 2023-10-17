#Term Version: 0.1.2-beta-2

#Import platform
import platform
import libs.dtime as dt
import libs.printwith as pw
import libs.inputwith as iw
import libs.getPc as getPc

#If OS is Windows bypass import
if platform.system() == 'Windows':
    pass
else:
    import libs.readline as rl


import moduls.shell as shell


if __name__ == "__main__":
    #If platform doesn't Windows run function.
    dt.dateAndTime()
    getPc.getUsername()
    if platform.system() != 'Windows':
        rl.arrowKeys()
        getPc.getLinuxPc()
    else:
        getPc.getPc()
    shell.runShell(__file__)
