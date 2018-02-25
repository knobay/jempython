import Contact

class Phonebook(object):
    def __init__(self):
        self.__contactlist = []

    def findContact(self,searchstring):
        'Retuns a contact object if provided a matching Firstname from the phonebook'
        result = Contact.Contact('Not found', 'Not found', 'Not found')
        for person in self.__contactlist:
            if person.getFirstname() == searchstring:
                result = person
                break
        return result
    	
    def addContact(self, newcontact):
        self.__contactlist.append(newcontact)
        return None

    def deleteContact(self, dumped):
        'Removes a contact if provided their firstname'
        for person in self.__contactlist:
            if person.getFirstname() == dumped:
                self.__contactlist.remove(person)
                break

def test():
    testContact = Contact.Contact('Sienna', 'Miller', '0778282883')
    print('TestName: ', testContact.getFirstname())
    print('TestNumber: ', testContact.getTelno())
    print('adding to phone book')
    testPhonebook = Phonebook()
    testPhonebook.addContact(testContact)
    print('added to phonebook')
    testContact = Contact.Contact('Carmen', 'Elektra', '0778288876')
    print('TestName: ', testContact.getFirstname())
    print('TestNumber: ', testContact.getTelno())
    print('adding to phone book')
    testPhonebook.addContact(testContact)
    print('added to phonebook')

    print('searching for Sienna, number is..')
    foundcontact = testPhonebook.findContact('Sienna')
    print(foundcontact.getTelno())  

    print('searching for Carmen, number is..')
    foundcontact = testPhonebook.findContact('Carmen')
    print(foundcontact.getTelno())

    print('dumping Sienna...')
    testPhonebook.deleteContact('Sienna')
    print('searching for Sienna, number is..')
    foundcontact = testPhonebook.findContact('Sienna')
    print(foundcontact.getTelno())    

if __name__ == "__main__":
    test()
