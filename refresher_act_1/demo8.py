cupsoftea = [['Mon', 5, 8, 3], ['Tue', 2, 7], ['Wed', 5, 3, 7, 3]]
print (cupsoftea)

#for row in cupsoftea:
#    print(row)
#    for day in row:
#        print(day, end = ' ')
#    print()

position = None

for index, day in enumerate(cupsoftea):
#    print(index, day)

    if day[0] == 'Tue':
        print(index)
        position = index
        break
    elif position == None:
        print('Not found')



