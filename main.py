import getpass
from printwith import *
import asyncio
import python_weather
import getPc
import datetime
import moduls.shell as shell
import os


username = getpass.getuser()

if os.path.isfile(".term_config"):
    pass
else:
    open(".term_config", "w+").close()


def enterCity():
    with open(".term_config", "w+") as f:
        getCity = input("Please enter your city: ")
        f.write(getCity)
        f.close()

with open(".term_config", "r") as f:
    if os.stat(".term_config").st_size == 0:
        enterCity()
        setCity = f.read()
    else:
        setCity = f.read()
    f.close()

async def getWeather():
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find(setCity)
    printWith(Colors.RED, Colors.BOLD, f"\n{setCity}: " + str(weather.current.temperature) + "C°" + "\n".format(setCity))
    dt = datetime.datetime.now()
    printWith(Colors.CYAN, Colors.BOLD, dt.strftime("%X") + " " + dt.strftime("%d") + "/" + dt.strftime("%m") + "/" + dt.strftime("%Y"))
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getWeather())

printWith(Colors.BLUE, Colors.BOLD, "Welcome to Term " + username + "\n")

getPc.getPc()
shell.runShell()