#!/usr/bin/env python3
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
                
numDays = 10
today += timedelta(days = numDays-1)
printSchedule(numDays)