#Term Version: 0.1.2-beta-1

import getpass
from libs.printwith import *
import asyncio
import python_weather
from libs import getPc
import datetime
import moduls.shell as shell
import moduls.config as c
from libs.emojiSupport import *


username = getpass.getuser()

async def getTimeAndWeather():
    try:
        client = python_weather.Client(format=python_weather.METRIC)
        weather = await client.find(c.nSetCity)
        printlnWithBold(Colors.RED, Colors.BOLD, f"{c.nSetCity}: " + str(weather.current.temperature) + "C°")
        dt = datetime.datetime.now()
        printWithBold(Colors.CYAN, Colors.BOLD, dt.strftime("%X") + " " + dt.strftime("%d") + "/" + dt.strftime("%m") + "/" + dt.strftime("%Y"))
        await client.close()
    except Exception as e:
        print(e)
        printWithBold(Colors.RED, Colors.BOLD, "Sorry, you need to connect to internet for weather forecast.")
        await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(getTimeAndWeather())

printlnWithEmoji(Colors.BLUE, "Welcome to Term " + username, Emojis.SLIGHTLY_SMILING_FACE)

getPc.getPc()
shell.runShell()