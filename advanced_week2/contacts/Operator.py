import Contact as c
import Phonebook as p


class Operator(object):
    def __init__(self):
        self.directory = p.Phonebook()

    def printOptions(self):
        print(chr(27) + "[2J")  # clear screen
        print('(1) Add contact')
        print('(2) Find contact')
        print('(Q) Quit')
        print('Enter choice...\n')

    def takeCall(self):

        quitme = False

        while quitme == False:

            choicemade = False

            self.printOptions()

            while choicemade == False:

                choice = input('> ')
                if choice == '1' or choice == '2' or choice == 'q':
                    choicemade = True
                else:
                    choicemade = False
                    self.printOptions()

                if choice == 'q':
                    quitme = True

                elif choice == '1':
                    contactfname = input('Enter contact first name')
                    contactsname = input('Enter contact surname')
                    contactnum = input('Enter contact telephone number')
                    newcontact = c.Contact(contactfname, contactsname, contactnum)
                    self.directory.addContact(newcontact)

                elif choice == '2':
                    contactfname = input('Enter contact first name')
                    num = self.directory.findContact(contactfname)
                    print(num.getTelno())
                    input('...')  # pause

                else:
                    choicemade == False
