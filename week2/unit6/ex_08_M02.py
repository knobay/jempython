# Import libraries
import math
import locale
locale.setlocale(locale.LC_ALL, '')
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
def letInput(prompt,valChars,errMess):
    x = True
    while x:
        Str = input(prompt)
        if len(Str) == 1 and Str.upper() in valChars:
            return Str.upper() # Return the offset to the correct price in pricelist[]
        else:
            print("\t{}\n".format(errMess))
#
# Prepare price list
#                 (               off peak                  )  (                  peak                  )
#                  Child,   Teen,    Stud,    Senior,  Adult,   Child,   Teen,    Stud,    Senior,  Adult
priceList     = [  5,       7,       7,       7.53,    8,       7,       9,       9,       9.12,    10]
#
# Initialise list for count of each visitor type.
#                   C,  T,  St, Se, A
visitorCountList = [0,  0,  0,  0,  0]
#
print("\n--------------------------------------------------------------")
print("------------------------   Ex08-M02   ------------------------")
print("\n\n")
print("Hi, Welcome to the virtual cinema, we're showing 'Pythons of the World'")
print("Here is our price list")
print("{0:-<28}{0:-<28}{0:-<29}".format("-"))
print("|{0:<27}|{1:^27}|{2:^27}|".format(" ","Off Peak","Peak"))
print("|{0:<27}|{1:^27}|{2:^27}|".format(" ","(Monday to Thursday)","(Friday to Sunday)"))
print("|{0:-<27}|{0:-<27}|{0:-<27}|".format("-"))
print("|{0:<27}|{1:^27}|{2:^27}|".format("Child",locale.currency(priceList[0]),locale.currency(priceList[5])))
print("|{0:<27}|{1:^27}|{2:^27}|".format("(12 years and under)"," "," "))
print("|{0:-<27}|{0:-<27}|{0:-<27}|".format("-"))
print("|{0:<27}|{1:^27}|{2:^27}|".format("Teen",locale.currency(priceList[1]),locale.currency(priceList[6])))
print("|{0:<27}|{1:^27}|{2:^27}|".format("(Ages 13 to 17)"," "," "))
print("|{0:-<27}|{0:-<27}|{0:-<27}|".format("-"))
print("|{0:<27}|{1:^27}|{2:^27}|".format("Student",locale.currency(priceList[2]),locale.currency(priceList[7])))
print("|{0:<27}|{1:^27}|{2:^27}|".format("(Student ID)"," "," "))
print("|{0:-<27}|{0:-<27}|{0:-<27}|".format("-"))
print("|{0:<27}|{1:^27}|{2:^27}|".format("Senior",locale.currency(priceList[3]),locale.currency(priceList[8])))
print("|{0:<27}|{1:^27}|{2:^27}|".format("(Ages 60+)"," "," "))
print("|{0:-<27}|{0:-<27}|{0:-<27}|".format("-"))
print("|{0:<27}|{1:^27}|{2:^27}|".format("Adult",locale.currency(priceList[4]),locale.currency(priceList[9])))
print("|{0:<27}|{1:^27}|{2:^27}|".format("(Ages 18+)"," "," "))
print("{0:-<28}{0:-<28}{0:-<29}\n".format("-"))
#
dateChar = letInput("Please choose Peak or Off Peak\nEnter P for peak and O for off peak:- ","OP","I only accept P or O, please try again")
if dateChar == "O":
    priceOffset = 0
else:
    priceOffset = 5
#
visitorCountList[0] = intInput("How many tickets for children do you want?- ","I only accept whole numbers here, please try again")
visitorCountList[1] = intInput("How many tickets for teenagers do you want?- ","I only accept whole numbers here, please try again")
visitorCountList[2] = intInput("How many tickets for students do you want?- ","I only accept whole numbers here, please try again")
visitorCountList[3] = intInput("How many tickets for seniors do you want?- ","I only accept whole numbers here, please try again")
visitorCountList[4] = intInput("How many tickets for adults do you want?- ","I only accept whole numbers here, please try again")
#
if visitorCountList[2] == 1:
    print("\nThere is a student coming, please show your ID now?")
elif visitorCountList[2] == 2:
    print("\nThere are {0} students coming, please will both of you show ids now?".format(visitorCountList[2]))
elif visitorCountList[2] >= 2:
    print("\nThere are {0} students coming, please will all {0} of you show ids now?".format(visitorCountList[2]))
idCount = 0
if visitorCountList[2] > 0:
    while 1:
        idCount = intInput("How many valid IDs were shown? :-","I only accept Y or N here")
        if idCount > visitorCountList[2]:
            print("How can there be more IDs that there are students?  Try again!")
        elif idCount < visitorCountList[2]:
            notStudents = visitorCountList[2]-idCount
            visitorCountList[2] = visitorCountList[2] - notStudents
            visitorCountList[4] = visitorCountList[4] + notStudents
            print("{} students failed to show valid Ids so I'm charging you as if they were adults.".format(notStudents))
            break
        else:
            break
#
# Price calculations
totalPrice = 0
for x in range(0,5):
    totalPrice=totalPrice+visitorCountList[x]*priceList[x+priceOffset]
#
# Print out explanation and price
if priceOffset == 0:
    print("\n\nYou chose an off peak day")
else:
    print("\n\nYou chose a day in Peak time")
print("and there are {} children, {} teens, {} students, {} seniors and {} adults coming\n".format(visitorCountList[0], visitorCountList[1], visitorCountList[2], visitorCountList[3], visitorCountList[4]))
print("So the total price is {}.  Thanks for your custom\n".format(locale.currency(totalPrice)))
