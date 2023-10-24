import platform, os, subprocess, re
import psutil

class filerm:
    system = platform.system()
    def getOS(prp: str):
        
        ## DESKTOP ENVIRONMENT
        de = "echo ${XDG_CURRENT_DESKTOP}"
        de_data = subprocess.check_output(de, shell=True).decode().strip()
        ##

        ###
        # prp: purpose for os
        ##
    
        ## Get os data terminal command
        command = "cat /etc/os-release"
        ## Read command output and decode.
        data = subprocess.check_output(command, shell=True).decode().strip()
        if prp == "os-name":
            for line in data.split("\n"):
                ## Find full name of os and return it
                if "PRETTY_NAME" in line:
                    return re.sub('.*PRETTY_NAME*.', "", line, 1).replace('"', "")
        elif prp == "kernel":
            command = "uname -r"
            data = subprocess.check_output(command, shell=True).decode().strip()
            return data
        elif prp == "shell":
            ## Get shell data in local variables
            command = "echo ${BASH_VERSION}"
            data = subprocess.check_output(command, shell=True).decode().strip()
            for line in data.split("\n"):
                ## remove release text for version of shell
                if "release" in line:
                    version = re.sub('()-release*.', "", line, 1)
            return os.environ["SHELL"] + " " + version

        ###
        # GNOME is supported for now, will update.
        ###
    
        elif prp == "desktop-env":
            if de_data == "GNOME": 
                command = "gnome-shell --version"
                data = subprocess.check_output(command, shell=True).decode().strip()
                for line in data.split("\n"):
                    return re.sub('Shell*.', "", line, 1)
            else:
                return de_data

        ## Get window manager from local variable    
        elif prp == "window-mngr":
            wm = "echo ${XDG_SESSION_TYPE}"
            wm_data = subprocess.check_output(wm, shell=True).decode().strip()
            return wm_data

        ###
        # if desktop environment is GNOME get theme.
        # will update.
        ###
        if de_data == "GNOME": 
            if prp == "gnome-theme":
                command = "gsettings get org.gnome.desktop.interface gtk-theme" 
                theme_data = subprocess.check_output(command, shell=True).decode().strip() 
                return theme_data.replace("'", "")
        else:
            pass #TODO


    ###
    # get CPU details from local file.
    ##

    def ReadCPU():
        if platform.system() == "Windows":
            return platform.processor()
    
        elif platform.system() == "Darwin":
            os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
            command = "sysctl -n machdep.cpu_brand_string"
            return subprocess.check_output(command).strip()

        elif platform.system() == "Linux":
            command = "cat /proc/cpuinfo"
            info = subprocess.check_output(command, shell=True).decode().strip()
            for line in info.split("\n"):
                if "model name" in line:
                    return re.sub(".*model name.*:", "", line, 1).strip(" ")

    ###
    # get GPU details from local file.
    ##

    def ReadGPU():
        if platform.system() == "Linux":
            command = "lspci | grep -i 'vga'"
            info = subprocess.check_output(command, shell=True).decode().strip()
            for line in info.split("\n"):
                if "0000:00:02.0 VGA compatible controller" in line:
                    return re.sub(".*0000:00:02.0 VGA compatible controller.*:", "", line, 1).strip(" ")


    ###
    # Read memory information with psutil. 
    # round: remove ".00"
    ###
    def ReadMemory(size: str):
        memory = psutil.virtual_memory()
        if size == "kb":
            return str(round(memory.total / 1024.0)) + " KB"
        elif size == "mb":
            return str(round(memory.total / 1024.0 **2)) + " MB"
        elif size == "gb":
            return str(round(memory.total / 1024.0 **3)) + " GB"

    ## read used ram amount.
    def CurrentRam():
        memory = psutil.virtual_memory()
        return str(round(memory.active / 1024.0 **2)) + " MB"

    ###
    # Read total disk size.
    ###
    def ReadDisk():
        disk = psutil.disk_usage("/")
        return str(round(disk.total / 1024.0 **3)) + " GB"
