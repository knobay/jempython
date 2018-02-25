import Contact as c
import Phonebook as p

class Operator(object):
    def __init__(self):
        self.directory = p.Phonebook()
    
    def takeCall(self):
        choicemade = False
        print(chr(27) + "[2J") # clear screen
        print('(1) Add contact')
        print('(2) Find contact')
        print('Enter choice...\n')

        while choicemade == False:
            choice = input('> ')
            if choice == '1' or choice =='2':
                choicemade = True
            else:
                choicemade = False
        
        if choice == '1':
            contactfname = input('Enter contact first name')
            contactsname = input('Enter contact surname')
            contactnum = input('Enter contact telephone number')
            newcontact = c.Contact(contactfname, contactsname, contactnum)
            self.directory.addContact(newcontact)

        elif choice == '2':
            contactfname = input('Enter contact first name')
            num = self.directory.findContact(contactfname)
            print(num.getTelno())
            input('>') # pause

        self.takeCall()

theoperator = Operator()
theoperator.takeCall()