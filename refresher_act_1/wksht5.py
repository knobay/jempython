def printlist(listvar, strt, end):
    for i in range(strt, end):
        print(listvar[i], end = ' ')
    print('\n')

def lists1():
    pocketcontents = ['keys', 'wallet', 'oyster card', 'phone']
    print('\n')
    printlist(pocketcontents,  0, len(pocketcontents))
    print(pocketcontents[2])
    pocketcontents.append('lint')
    print('\n')
    printlist(pocketcontents,  0, len(pocketcontents))
    pocketcontents.remove('keys')
    printlist(pocketcontents,  0, len(pocketcontents))

def lists2():
    intlist = [17, 9, 42, 1, 36, 8]
    printlist(intlist,  2, len(intlist))
    print('\n')

def main():
    lists1()
    lists2()

main()
