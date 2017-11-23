import math
#
print("\n--------------------------------------------------------------")
print("------------------------     E03     -------------------------")
x = True
while x:
    Str = input("Please enter a single letter:- ")
    if len(Str) == 1 and Str.isalpha():
        break
    else:
        print("Sorry, it had to be single letter, please try again.\n")
if Str.upper() in "AEIOU":
    print("The letter you entered was {}, it is a vowel".format(Str))
else:
    print("The letter you entered was {}, it is a consonant".format(Str))
