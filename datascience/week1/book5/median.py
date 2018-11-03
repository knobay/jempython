def findmedian(numlist):
    numlist.sort()
    median = numlist[int(len(numlist)/2)]
    return median

print(findmedian([3, 5, 10, 7, 4, 1]))
