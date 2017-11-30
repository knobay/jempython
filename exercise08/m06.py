# Import libraries
import math
#
# Set up global variables
#
print("\n--------------------------------------------------------------")
print("------------------------     M06     -------------------------")
#
# Get the user's string of numbers
while 1:
    numStr = input("Please enter a string of three numbers (I only accept numbers and spaces to seperate them) :- ")
    x = 0
    charStruct = True
    while x < len(numStr):
        if numStr[x] not in " 0123456789":
            charStruct = False
            break
        x += 1
# next comment
    tempStr = numStr
    if not charStruct: print("1. I only accept three positive integers separated by spaces at the moment.")
    elif numStr.strip().count(" ") != 2: print("2. I only accept three positive integers separated by spaces at the moment.")
#
print("{}".format(numStr))
