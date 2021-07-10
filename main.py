import getpass
from printwith import *
import asyncio
import python_weather
import getPc
import datetime

username = getpass.getuser()
getCity = input("Please enter your city: ")


async def getWeather():
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find(getCity)
    printWith(Colors.RED, Colors.BOLD, f"\n{getCity}: " + str(weather.current.temperature) + "°" + "\n".format(getCity))
    dt = datetime.datetime.now()
    printWith(Colors.CYAN, Colors.BOLD, dt.strftime("%X") + " " + dt.strftime("%d") + "/" + dt.strftime("%m") + "/" + dt.strftime("%Y"))
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getWeather())

printWith(Colors.BLUE, Colors.BOLD, "Welcome to Term " + username + "\n")

getPc.getPc()