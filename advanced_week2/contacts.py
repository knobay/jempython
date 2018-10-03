"""Exercise to make a contacts program allowing the user to add and find \
contacts with names and phone numbers"""


class Contact(object):
    'The contact class'
    def __init__(self, fname, sname, num):
        self.__firstname = fname
        self.__secondname = sname
        self.__telno = num

    def getTelno(self):
        return self.__telno

    def getFirstname(self):
        return self.__firstname

    def getSecondname(self):
        return self.__secondname


class Phonebook(object):
    'The Phonebook class. An updateable and searchable collection of contacts.'
    def __init__(self):
        self.__contactlist = []

    def findContact(self, searchstring):
        'Retuns a contact object if provided a matching Firstname \
        from the phonebook'
        result = Contact('Not found', 'Not found', 'Not found')
        for person in self.__contactlist:
            if person.getFirstname() == searchstring:
                result = person
                break
        return result

    def addContact(self, newcontact):
        self.__contactlist.append(newcontact)
        return None


class Operator(object):
    'The Operator interacts with the user, reading and writing to the \
    phonebook on their behalf'
    def __init__(self):
        self.directory = Phonebook()

    def printOptions(self):
        print(chr(27) + "[2J")  # clear screen
        print('(1) Add contact')
        print('(2) Find contact')
        print('(Q) Quit')
        print('Enter choice...\n')

    def takeCall(self):

        keepalive = True

        while keepalive:

            needinput = True

            while needinput:

                self.printOptions()

                choice = input('> ')
                if choice == '1' or choice == '2' or choice == 'q':
                    needinput = False
                else:
                    needinput = True
                    self.printOptions()

                if choice == 'q':
                    keepalive = False

                elif choice == '1':
                    contactfname = input('Enter contact first name')
                    contactsname = input('Enter contact surname')
                    contactnum = input('Enter contact telephone number')
                    newcontact = Contact(contactfname, contactsname, contactnum)
                    self.directory.addContact(newcontact)

                elif choice == '2':
                    contactfname = input('Enter contact first name')
                    num = self.directory.findContact(contactfname)
                    print(num.getTelno())
                    input('...')  # pause

                else:
                    needinput = True


def main():
    theoperator = Operator()
    theoperator.takeCall()

if __name__ == "__main__":
    main()
