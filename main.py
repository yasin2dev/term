import getpass
from printwith import *
import asyncio
import python_weather
import getPc
import datetime

username = getpass.getuser()

async def getWeather():
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("Manavgat")
    printWith(Colors.RED, Colors.BOLD, "\nManavgat: " + str(weather.current.temperature) + "°" + "\n")
    dt = datetime.datetime.now()
    printWith(Colors.CYAN, Colors.BOLD, dt.strftime("%X") + " " + dt.strftime("%d") + "/" + dt.strftime("%m") + "/" + dt.strftime("%Y"))
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getWeather())

printWith(Colors.BLUE, Colors.BOLD, "Welcome to Term " + username + "\n")

getPc.getPc()