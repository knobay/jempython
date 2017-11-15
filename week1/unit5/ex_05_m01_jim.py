# M01
#
print("\n--------------------------------------------------------------")
print("\n------------------------     M01     -------------------------\n")
name = input("Please enter your name: ")
SpaceCount = name.count(" ")
Init = ""
temp = name
for x in range(0, SpaceCount+1):
    Init = Init+temp[0]
    temp = temp[temp.find(" ")+1:len(temp)]
print("{} ({})".format(name,Init))
#
# M02
#

