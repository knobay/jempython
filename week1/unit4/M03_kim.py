# M03.  Get the user name and their age.  Print a message telling them when they will turn 100.
import datetime
now = datetime.datetime.now() # the current year in which the program is being executed
print("This program will tell you when you will be 100")
userName=input("Enter your name")
userAge=input("Enter your age")
print("{0}, you will turn 100 in the year {1}".format(userName,now.year+100-int(userAge)))
