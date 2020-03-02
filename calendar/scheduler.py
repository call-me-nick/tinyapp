from datetime import date
from datetime import timedelta
today = date.today()

def printSchedule(x):
    global today
    for i in range(0, x):
        if(today.weekday() < 4):
            print(today.strftime("%Y.%m.%d-%a"))
            print("today:\nyesterday:\nblockers:\n")
        else: print(today.strftime("%Y.%m.%d-%a") + "\n")
        today += timedelta(days = 1)
                
print("Days to display: ")
numDays = int(input())
printSchedule(numDays)