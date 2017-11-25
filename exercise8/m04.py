import math
import datetime
#
# Set up global variables
monList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
seasonList = ["Spring", "Summer", "Autumn", "Winter"]
seasonStartList = ["2017.03.21", "2017.06.21", "2017.09.21", "2017.12.21"]
seasonYDay = [0, 0, 0, 0]
fmt = "%Y.%m.%d"
for x in range (0, 4):
    dt = datetime.datetime.strptime(seasonStartList[x], fmt)
    tt = dt.timetuple()
    seasonYDay[x] = tt.tm_yday
#
print("\n--------------------------------------------------------------")
print("------------------------     M04     -------------------------")
#
# Get the user's date string
while 1:
    dateStr = input("Please enter a day and month in the format 'dd mmm', for example '23 mar' :- ")
    x = 0
    separator = -1
    while x < len(dateStr):
        if dateStr[x] in " /-":
            separator = x
            break
        x += 1
    if separator == -1: print("I couldn't identify the separator, I only accept ' ' or '/' or '-' at the moment.")
    elif separator == 0: print("Did you enter something before the day of the month? I only accept dates in the format 'dd mmm' (like 23 mar) at the moment.")
    elif not dateStr[0:separator].isdigit(): print("You entered {}.  I only accept digits for the day of the month.".format(dateStr[0:separator]))
    elif dateStr[separator+1:len(dateStr)].upper() not in monList: print("You entered '{}'.  I only accept the first three letters of a month right now, for example 'Jul' for July".format(dateStr[separator+1:len(dateStr)]))
    else:
        monthNum = 0
        dayNum = int(dateStr[0:separator])
        while monthNum < 12:
            if dateStr[separator+1:len(dateStr)].upper() == monList[monthNum]: break
            monthNum += 1
        if dayNum > dayList[monthNum]:
            print("You entered {0} of {1}.  This process assumes that {1} only has {2} days".format(dateStr[0:separator], monthList[monthNum], dayList[monthNum]))
        else:
            break
# Got a good date
#
print("You entered {1} {0}.  ".format(dateStr[0:separator], monthList[monthNum]), end = "")
#
chosenDate = "2017."+str(monthNum+1)+"."+dateStr[0:separator]
dt = datetime.datetime.strptime(chosenDate, fmt)
tt = dt.timetuple()
chosenDay = tt.tm_yday
seasonIndex = 0
if chosenDay >= seasonYDay[0] and chosenDay < seasonYDay[1]:
    seasonIndex = 0
elif chosenDay >= seasonYDay[1] and chosenDay < seasonYDay[2]:
    seasonIndex = 1
elif chosenDay >= seasonYDay[2] and chosenDay < seasonYDay[3]:
    seasonIndex = 2
elif chosenDay >= seasonYDay[3] or chosenDay < seasonYDay[0]:
    seasonIndex = 3
else:
    print("Something went wrong with our seasons")

print("It is in {}".format(seasonList[seasonIndex]))
