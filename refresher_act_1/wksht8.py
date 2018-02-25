"""Maintian a list of contacts"""

contactlist = [['John', 'Smith', '07899422322'], \
               ['Sally', 'Smith', '07804423422'], \
               ['Joe', 'Bloggs', '07877988753']]
#print(contactlist)

def printContactList(contacts):
    "Print the contents of a list"
    print()
    for index, contact in enumerate(contacts):
#        print(contact)
        for item in contact:
            print(item, end = ' ')
        print()

def adddetails(contacts):
    "Add details to a list"
    fname = input('Enter first name:- ')
    sname = input('enter second name:- ')
    pnum = input('Enter phone number:- ')
    contacts.append([fname, sname, pnum])

def findanddelete(contacts):
    "Remove a row from a list"
    fname = input('Enter the first name of the person you want to remove:- ')
    position = None
    for index, contact in enumerate(contacts):
        if contact[0] == fname:
            position = index
            break
    if position == None:
        print('Not found')
    else:
        del(contacts[index])

def main():
    "The main program"
    printContactList(contactlist)
    adddetails(contactlist)
    printContactList(contactlist)
    findanddelete(contactlist)
    printContactList(contactlist)

main()