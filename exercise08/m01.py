import math
#
print("\n--------------------------------------------------------------")
print("------------------------     E03     -------------------------")
x = True
while x:
    Str = input("Please enter a year:- ")
    if len(Str) <= 4 and Str.isdigit():
        break
    else:
        print("Sorry, it had to be year between 0 and 9999, please try again.\n")
year = int(Str)
if (year%4 == 0 or year%100 == 0) and year%400 != 0:
    print("The year you entered was {}, and it is a leap year".format(Str))
else:
    print("The year you entered was {}, and it's not a leap year".format(Str))
