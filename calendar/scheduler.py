#!/usr/bin/env python3
import argparse
from datetime import date
from datetime import timedelta
today = date.today()

def printSchedule(x):
    global today
    for i in range(0, x):
        date = today.strftime("%Y.%m.%d")
        day = today.strftime("%a")
        if(today.weekday() < 5):
            print("## " + date + " - " + day)
            print("today:\nyesterday:\nblockers:\nlong-term:")
        else: print("## " + date + " - " + day)
        today -= timedelta(days = 1)
                
parser = argparse.ArgumentParser()
parser.add_argument("integer", help = "diplay x days", type = int)
arg = parser.parse_args()
today += timedelta(days = arg-1)
printSchedule(numDays)