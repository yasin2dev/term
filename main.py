import getpass
from libs.printwith import *
import asyncio
import python_weather
from libs import getPc
import datetime
import moduls.shell as shell
import moduls.config as cfg


username = getpass.getuser()

async def getTimeAndWeather():
    try:
        client = python_weather.Client(format=python_weather.METRIC)
        weather = await client.find(cfg.nSetCity[1])
        printWithBold(Colors.RED, Colors.BOLD, f"\n{cfg.nSetCity[1]}: " + str(weather.current.temperature) + "C°" + "\n".format(cfg.setCity))
        dt = datetime.datetime.now()
        printWithBold(Colors.CYAN, Colors.BOLD, dt.strftime("%X") + " " + dt.strftime("%d") + "/" + dt.strftime("%m") + "/" + dt.strftime("%Y"))
        await client.close()
    except:
        printWithBold(Colors.RED, Colors.BOLD, "Sorry, you need to connect to internet for weather forecast.")
        await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getTimeAndWeather())

printWithBold(Colors.BLUE, Colors.BOLD, "Welcome to Term " + username + "\n")

getPc.getPc()
shell.runShell()