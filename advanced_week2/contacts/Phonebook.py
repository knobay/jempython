import Contact


class Phonebook(object):
    def __init__(self):
        self.__contactlist = []

    def findContact(self, searchstring):
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
