import datetime

from libs.defines import Colors
import libs.printwith as pw


def dateAndTime():
    dt = datetime.datetime.now()
    pw.printWithBold(Colors.CYAN, dt.strftime("%X") + " "
                     + dt.strftime("%d") + "/" + dt.strftime("%m") + "/" 
                     + dt.strftime("%Y") + " " + "UTC" + datetime.datetime.now(datetime.timezone.utc).astimezone().tzname())