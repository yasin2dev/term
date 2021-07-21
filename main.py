import getpass
from types import TracebackType
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
        f.write(f"WEATHER_CITY: {getCity}".format(getCity))
        f.close()

with open(".term_config", "r") as f:
    if os.stat(".term_config").st_size == 0:
        enterCity()
        setCity = f.read()
        nSetCity = setCity.split("WEATHER_CITY: ")
    else:
        setCity = f.read()
        nSetCity = setCity.split("WEATHER_CITY: ")
    f.close()

async def getWeather():
    try:
        client = python_weather.Client(format=python_weather.IMPERIAL)
        weather = await client.find(nSetCity[1])
        printWithBold(Colors.RED, Colors.BOLD, f"\n{nSetCity[1]}: " + str(weather.current.temperature) + "C°" + "\n".format(setCity))
        dt = datetime.datetime.now()
        printWithBold(Colors.CYAN, Colors.BOLD, dt.strftime("%X") + " " + dt.strftime("%d") + "/" + dt.strftime("%m") + "/" + dt.strftime("%Y"))
        await client.close()
    except:
        printWithBold(Colors.RED, Colors.BOLD, "Sorry, you need to connect to internet for weather forecast.")
        await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getWeather())

printWithBold(Colors.BLUE, Colors.BOLD, "Welcome to Term " + username + "\n")

getPc.getPc()
shell.runShell()