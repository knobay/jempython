mylist = [17, 9, 42, 1, 36, 8]


print('from position 3')
for i in range(3,len(mylist)):
    print(mylist[i])


print('sorted...')
print(sorted(mylist))


print('inserting 11 at position 2')
mylist.insert(2, 11)
print(mylist)

print('removing 36')
mylist.remove(36)
print(mylist)

query = int(input('search for a number'))
if query in mylist:
    print('yep, in there')
else:
    print('nope, not in there')
