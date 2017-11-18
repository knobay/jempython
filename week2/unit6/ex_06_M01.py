import math
#
print("\n--------------------------------------------------------------")
print("------------------------     M01     -------------------------")
Cnum=""
#while type != Cnum.isnumeric():
Cnum = input("Please enter a number in Celcius:- ")
Fnum = ((int(Cnum)*9)/5)+32
print("The number in Celcius was {} and converting it to Fahrenheit its {}".format(Cnum,Fnum))
Fnum = input("Please enter a number in Fahrenheit:- ")
Cnum = (int(Fnum)-32)*(5/9)
print("The number in Fahrenheit was {} and converting it to Celcius its {}".format(Fnum,Cnum))
