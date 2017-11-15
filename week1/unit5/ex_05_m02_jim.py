# M02
#
print("\n--------------------------------------------------------------")
print("\n------------------------     M02     -------------------------\n")
FirstName = "Harry Potter 1980"
SecondName = "Hermione Granger 1979"
ThirdName = "Ron Weasley 1981"
x = 0
temp = FirstName[x].isnumeric()
while temp == False: 
    x = x + 1
    temp = FirstName[x].isnumeric()
NameSegment = FirstName[0:x-1]
AgeSegment = FirstName[x:]
x=0
ActualAge = 2017 - int(AgeSegment)
print("{} was born in {} and is {} years old".format(NameSegment,AgeSegment,ActualAge))
temp = SecondName[x].isnumeric()
while temp == False: 
    x = x + 1
    temp = SecondName[x].isnumeric()
NameSegment = SecondName[0:x-1]
AgeSegment = SecondName[x:]
ActualAge = 2017 - int(AgeSegment)
x=0
print("{} was born in {} and is {} years old".format(NameSegment,AgeSegment,ActualAge))
temp = ThirdName[x].isnumeric()
while temp == False: 
    x = x + 1
    temp = ThirdName[x].isnumeric()
NameSegment = ThirdName[0:x-1]
AgeSegment = ThirdName[x:]
ActualAge = 2017 - int(AgeSegment)
print("{} was born in {} and is {} years old".format(NameSegment,AgeSegment,ActualAge))

