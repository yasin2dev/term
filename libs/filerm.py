import platform, os, subprocess, re
import psutil, socket, getpass

class filerm:
    host = socket.gethostname()
    user = getpass.getuser()
    system = platform.system()
    def getOS(prp: str):
        
        ## DESKTOP ENVIRONMENT
        de = "echo ${XDG_CURRENT_DESKTOP}"
        de_data = subprocess.check_output(de, shell=True).decode().strip()
        ##

        command = "cat /etc/os-release"
        data = subprocess.check_output(command, shell=True).decode().strip()
        if prp == "os-name":
            for line in data.split("\n"):
                if "PRETTY_NAME" in line:
                    return re.sub('.*PRETTY_NAME*.', "", line, 1).replace('"', "")
        elif prp == "kernel":
            command = "uname -r"
            data = subprocess.check_output(command, shell=True).decode().strip()
            return data
        elif prp == "shell":
            shell = "echo ${SHELL}"
            sh_data = subprocess.check_output(shell, shell=True).decode().strip()
            return os.environ["SHELL"]
                
        
        elif prp == "desktop-env":
            if de_data == "GNOME": 
                command = "gnome-shell --version"
                data = subprocess.check_output(command, shell=True).decode().strip()
                for line in data.split("\n"):
                    return re.sub('Shell*.', "", line, 1)
            else:
                return de_data
        
        elif prp == "window-mngr":
            wm = "echo ${XDG_SESSION_TYPE}"
            wm_data = subprocess.check_output(wm, shell=True).decode().strip()
            return wm_data


    def ReadTheme():
        ## DESKTOP ENVIRONMENT
        de = "echo ${XDG_CURRENT_DESKTOP}"
        de_data = subprocess.check_output(de, shell=True).decode().strip()
        ##
        if de_data == "GNOME": 
            command = "gsettings get org.gnome.desktop.interface gtk-theme" 
            theme_data = subprocess.check_output(command, shell=True).decode().strip() 
            return theme_data.replace("'", "")
        elif de_data == "X-Cinnamon":
            command = "gsettings get org.cinnamon.theme name" 
            theme_data = subprocess.check_output(command, shell=True).decode().strip() 
            return theme_data.replace("'", "")
        else:
            pass #TODO

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

    def ReadGPU():
        if platform.system() == "Linux":
            command = "lspci | grep -i 'vga'"
            info = subprocess.check_output(command, shell=True).decode().strip()
            for line in info.split("\n"):
                if "0000:00:02.0 VGA compatible controller" in line:
                    return re.sub(".*0000:00:02.0 VGA compatible controller.*:", "", line, 1).strip(" ")


    def ReadMemory(size: str):
        memory = psutil.virtual_memory()
        if size == "kb":
            return str(round(memory.total / 1024.0)) + " KB"
        elif size == "mb":
            return str(round(memory.total / 1024.0 **2)) + " MB"
        elif size == "gb":
            return str(round(memory.total / 1024.0 **3)) + " GB"
        
    def CurrentRam():
        memory = psutil.virtual_memory()
        return str(round(memory.active / 1024.0 **2)) + " MB"
    
    def ReadDisk():
        disk = psutil.disk_usage("/")
        return str(round(disk.total / 1024.0 **3)) + " GB"


class filermFile:

    def TruncateFile(fileDir: str):
        with open(fileDir, "w+") as f:
            f.truncate(0)
            f.close()

    def CreateFile(fileName: str):
        if os.path.isfile(fileName):
            print("File exist.")
            pass
        else: 
            open(fileName, "w+").close()


class filermWindows:
    def getOs(prp: str):
        if prp == "os-name":
            return platform.win32_ver()[0]
        elif prp == "version":
            return platform.win32_ver()[1]
        
    def ReadMemory(size: str):
        memory = psutil.virtual_memory()
        if size == "kb":
            return str(round(memory.total / 1024.0))
        elif size == "mb":
            return str(round(memory.total / 1024.0 **2))
        elif size == "gb":
            return str(round(memory.total / 1024.0 **3))

    def ReadDisk():
        disk = psutil.disk_usage("/")
        return str(round(disk.total / 1024.0 **3)) + " GB"

    def ReadGPU():
        gpu = subprocess.check_output('wmic path win32_VideoController get name')
        return str(gpu).replace("b'Name", "").replace("\\r", "").replace("\\n", "").replace("'", "").strip()
    
    def ReadCPU():
        if platform.system() == "Windows":
            cpu = subprocess.check_output("wmic cpu get name")
            return str(cpu).replace("b'Name", "").replace("\\r", "").replace("\\n", "").replace("'", "").strip()