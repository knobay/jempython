import math
#
print("\n--------------------------------------------------------------")
print("------------------------     E02     -------------------------")
x = True
while x:
    numStr = input("Please enter a whole number:- ")
    if numStr.isdigit():
        num = int(numStr)
        break
    elif numStr.replace("-","").isdigit():
        num = int(numStr)
        break
    else:
        print("Sorry, it had to be a positive or negative integer, please try again")
if num > 0:
    print("The number you entered was:- {} and it is greater than zero.".format(num))
elif num < 0:
    print("The number you entered was:- {} and it is less than zero.".format(num))
else:
    print("The number you entered was zero")