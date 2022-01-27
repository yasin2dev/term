import os

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