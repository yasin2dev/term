import os
from webbrowser import get
from libs.printwith import Colors

if os.path.isfile(".term_config"):
    pass
else:
    open(".term_config", "w+").close()


if os.stat(".term_config").st_size == 0:
    with open(".term_config", "w+") as f:
        #for weather
        getCity = input("Please enter your city: ")
        f.write(f"WEATHER_CITY: {getCity}\n")
        f.close()

def startConfig():
    with open(".term_config", "a") as f:
        #for command input
        colorTo = input("Plese choose color (Restart after configuring) (RED, GREEN): ")
        f.write(f"INPUT_COLOR: {colorTo}\n")
        f.close()

    
with open(".term_config", "r") as f:
    setCity = f.readline()
    nSetCity = setCity.replace("\n", "")[14:]

    getColor = f.readline()
    registeredColor = getColor.replace("\n", "")[13:]