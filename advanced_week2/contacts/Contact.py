
class Contact(object):
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


def test():
    testContact = Contact('Sienna', 'Miller', '0778282883')
    print('Name: ', testContact.getFirstname())
    print('Number: ', testContact.getTelno())

if __name__ == "__main__":
    test()
