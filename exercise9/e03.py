"""Exercise 9, Easy 3"""

def ex03():
    "Do it all in a function for the sake of green squiggles"
    # Initialize lists.
    l1 = []
    l2 = []
    l3 = []

    for i in [0, 1, 2, 3, 4]:
        l1.append(i+1)
        l2.append(-5 + i)
        l3.append(0)

    print("list 1", l1)
    print("list 2", l2)
    print("list 3", l3)

    # a) change the content of object 2 and 4 of l2 to contain their own squares

    l2[2] = l2[2] * l2[2]
    l2[4] = l2[4] * l2[4]

    print("list 2", l2)

    # b) Remove the third object from all lists.

    del l1[2]
    del l2[2]
    del l3[2]

    print("list 1", l1)
    print("list 2", l2)
    print("list 3", l3)

    # c) create one big list by combining l1, l2 and l3

    biglist = []
    while l1:
        biglist.append(l1.pop())
        biglist.append(l2.pop())
        biglist.append(l3.pop())

    print("combined list", biglist)

    # d) calculate the sum of items in the new list

    mysum = 0
    while biglist:
        mysum = mysum + biglist.pop()

    print("sum", mysum)

ex03()
