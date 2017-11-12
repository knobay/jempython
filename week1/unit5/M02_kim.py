# Initialise the data sets
data1 = "Harry Potter 1980"
data2 = "Hermione Granger 1979"
data3 = "Ron Weasley 1980"

import datetime
now = datetime.datetime.now() # the current year in which the program is being executed

pos1=data1.index('1')
print(data1[0:pos1], "age:", now.year-int(data1[pos1:]))

pos2=data2.index('1')
print(data2[0:pos2], "age:", now.year-int(data2[pos2:]))

pos3=data3.index('1')
print(data3[0:pos3], "age:", now.year-int(data3[pos3:]))