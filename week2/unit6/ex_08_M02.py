# Import libraries
import math
#
#
#Define functions
# Entering a number, only positive integers are allowed
def intInput(prompt,errMess):
    x = True
    while x:
        valStr = input(prompt)
        if valStr.isdigit():
            val = int(valStr)
            if val > 30:
                conf = input("Really? ..  Press Y to confirm:- ")
                if conf.upper() != "Y":
                    print(":)")
                else:
                    return val
            elif val >= 0:
                return val
        else:
            print("\t{}\n".format(errMess))
#
# Entering a single letter
def letInput(prompt,errMess):
    x = True
    while x:
        Str = input(prompt)
        if Str.upper() == "P":
            return 5 # Return the offset to the correct price in pricelist[]
        elif Str.upper() == "O":
            return 0 # Return the offset to the correct price in pricelist[]
        else:
            print("\t{}\n".format(errMess))
#
# Prepare price list
#           (     off peak    )  (      peak       )
#            C,  T,  St, Se, A,  C,  T,  St, Se, A
priceList = [5,  7,  7,  7,  8,  7,  9,  9,  9,  10]
#
# Initialise list for count of each visitor type.
#                   C,  T,  St, Se, A
visitorCountList = [0,  0,  0,  0,  0]
#
print("\n--------------------------------------------------------------")
print("------------------------   Ex08-M02   ------------------------")
print("\n\n")
print("Hi, Welcome to the virtual cinema, we're showing python of the world")
print("\nWe have two price ranges based on date and status")
print("-----------------------------------------------------------------------------------------")
print("|\t\t\t|\t     Off Peak\t\t|\t\tPeak\t\t|")
print("|\t\t\t|\t(Monday to Thusday)\t|\t (Friday to Sunday)\t|")
print("|-----------------------|-------------------------------|-------------------------------|")
print("|Child\t\t\t|\t\t£{:.2f}\t\t|\t\t£{:.2f}\t\t|".format(priceList[0],priceList[5]))
print("|(12 years and under)\t|\t\t\t\t|\t\t\t\t|")
print("|-----------------------|-------------------------------|-------------------------------|")
print("|Teen\t\t\t|\t\t£{:.2f}\t\t|\t\t£{:.2f}\t\t|".format(priceList[1],priceList[6]))
print("|(Ages 13 to 17)\t|\t\t\t\t|\t\t\t\t|")
print("|-----------------------|-------------------------------|-------------------------------|")
print("|Student\t\t|\t\t£{:.2f}\t\t|\t\t£{:.2f}\t\t|".format(priceList[2],priceList[7]))
print("|(Student ID)\t\t|\t\t\t\t|\t\t\t\t|")
print("|-----------------------|-------------------------------|-------------------------------|")
print("|Senior\t\t\t|\t\t£{:.2f}\t\t|\t\t£{:.2f}\t\t|".format(priceList[3],priceList[8]))
print("|(Ages 60+)\t\t|\t\t\t\t|\t\t\t\t|")
print("|-----------------------|-------------------------------|-------------------------------|")
print("|Adult\t\t\t|\t\t£{:.2f}\t\t|\t\t£{:.2f}\t\t|".format(priceList[4],priceList[9]))
print("|(Ages 18+)\t\t|\t\t\t\t|\t\t\t\t|")
print("-----------------------------------------------------------------------------------------")
print("")
#
dateChoice = letInput("Please choose Peak or Off Peak\nEnter P for peak and O for off peak:- ","I only accept P or O, please try again")
#
visitorCountList[0] = intInput("How many tickets for children do you want?- ","I only accept whole numbers here, please try again")
visitorCountList[1] = intInput("How many tickets for teenagers do you want?- ","I only accept whole numbers here, please try again")
visitorCountList[2] = intInput("How many tickets for students do you want?- ","I only accept whole numbers here, please try again")
visitorCountList[3] = intInput("How many tickets for seniors do you want?- ","I only accept whole numbers here, please try again")
visitorCountList[4] = intInput("How many tickets for adults do you want?- ","I only accept whole numbers here, please try again")
#
if visitorCountList[2] == 1:
    print("There is a student coming, please show your ID now?")
    x = input("Press enter when done")
elif visitorCountList[2] == 2:
    print("There are {0} students coming, please will both of you show ids now?".format(visitorCountList[2]))
    x = input("Press enter when done")
elif visitorCountList[2] >= 2:
    print("There are {0} students coming, please will all {0} of you show ids now?".format(visitorCountList[2]))
    x = input("Press enter when done")
#
# Price calculations
totalPrice = 0
for x in range(0,5):
    totalPrice=totalPrice+visitorCountList[x]*priceList[x+dateChoice]
#
# Print out explanation and price
if dateChoice == 0:
    print("\n\nYou chose an off peak day")
else:
    print("\n\nYou chose a day in Peak time")
print("and there are {} children, {} teens, {} students, {} seniors and {} adults coming\n".format(visitorCountList[0], visitorCountList[1], visitorCountList[2], visitorCountList[3], visitorCountList[4]))
print("So the total price is £{:.2f}.  Thanks for your custom\n".format(totalPrice))
