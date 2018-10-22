def findmean(numlist):
    total = 0
    for num in numlist:
        total = total + num
        mean = total/len(numlist)
    return mean

print(findmean([3, 5, 10]))
