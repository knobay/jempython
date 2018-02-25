class car(object):
    def __init__(self, name, speed):
        self.carname = name
        self.topspeed = speed


    def printdetails(self):
        print(self.carname, ' can travel at ', self.topspeed)

    
def main():
    mycar = car('polo', '120')
    mycar.printdetails()

main()
