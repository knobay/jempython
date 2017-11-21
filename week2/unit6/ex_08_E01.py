import math
#
print("\n--------------------------------------------------------------")
print("------------------------     E01     -------------------------")
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
        print("Sorry, it had to be an integer, please try again")
if num%2 == 0:
    print("The number you entered was:- {} and it is even.".format(num))
else:
    print("The number you entered was:- {} and it is odd.".format(num))