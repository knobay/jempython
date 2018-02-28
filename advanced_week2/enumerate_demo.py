cupsoftea = [["Mon",1,3,5],["Tues",3,4,2],["Wed",6,4,8]]

# for row in cupsoftea:
#     for item in row:
#         print(str(item).rstrip())

# if "Mon" in cupsoftea[1]:
#     print("found")
# else:
#     print("not found")



position = None

for index, day in enumerate(cupsoftea):
    # print(index,day)

    if day[0] == "Tues":
        print('Found at position', index)
        position = index
        break

    elif position == None:
        pass