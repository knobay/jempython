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
minutesSegment = (seconds%hourInSeconds)//60
secondsSegment = seconds%60
print("You entered {} seconds: that's {} days, {} hours, {} minutes and {} seconds.".format(seconds, daysSegment, hoursSegment, minutesSegment, secondsSegment))

