# Import all libraries
import math
#
dayInSeconds = 24*60*60
hourInSeconds = 60*60
print("\n--------------------------------------------------------------")
print("------------------------     M05     -------------------------")
x = True
while x:
    kmStr = input("Please enter a distance in Kilometres:- ")
    if kmStr.isdigit():
        kms = int(kmStr)
        break
    elif kmStr.replace(".","").isdigit():
        kms = float(kmStr)
        break
    else:
        print("Sorry, I couldn't find the number in your response, please try again")
miles = kms * 0.621371
print("You entered {} in kilometres: that's {} in miles.\n\n".format(kms, round(miles,4)))
x = True
while x:
    mlStr = input("Now enter a distance in Miles:- ")
    if mlStr.isdigit():
        mls = int(mlStr)
        break
    elif mlStr.replace(".","").isdigit():
        mls = float(mlStr)
        break
    else:
        print("Sorry, I couldn't find the number in your response, please try again")
kms = mls * 1.60934
print("You entered {} in miles: that's {} in kilometres.".format(mls, round(kms,4)))
