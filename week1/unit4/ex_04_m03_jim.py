# E01
#
print("\n--------------------------------------------------------------")
print("\n------------------------     E01     -------------------------\n")
greeting = "Hello World!"
print(greeting)
#
# M02
#
print("\n--------------------------------------------------------------")
print("\n------------------------     M01     -------------------------\n")
v1 = 16
v2 = v1
print(id(v1) == id(v2),str(v1))
v2 = 20
print(id(v1) == id(v2),str(v1))
#
# M03
#
print("\n--------------------------------------------------------------")
print("\n------------------------     M03     -------------------------\n")
name = input("Hiya, enter your name: ")
age = input("Also please enter your age in years: ")
to_hundred = 100 - int(age)
hundred_at = 2017 + to_hundred
if to_hundred < 0:
    print("Wow you turned one hundred {} years ago".format(hundred_at))
else:
    print("You will turn 100 in {}".format(hundred_at))

