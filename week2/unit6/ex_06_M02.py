# Import all libraries
import math
#
dayInSeconds = 24*60*60
hourInSeconds = 60*60
print("\n--------------------------------------------------------------")
print("------------------------     M02     -------------------------")
secondsStr = input("Please enter a huge number of seconds:- ")
seconds = int(secondsStr)
daysSegment = seconds//dayInSeconds
hoursSegment = (seconds%dayInSeconds)//hourInSeconds
secondsSegment = seconds%60
print("You entered {} seconds: that's {} days, {} hours and {} seconds.".format(seconds,daysSegment,hoursSegment,secondsSegment))

