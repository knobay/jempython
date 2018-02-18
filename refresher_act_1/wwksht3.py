"""Exercise 3"""
import callmod

def messwithtemperature():
    "Converting temperature from centegrade and back"
    far = float(input('\nEnter a temerature in farenheit:='))
    cent = callmod.convftoc(far)
    print('The centegrade value of {} is {}'.format(round(far, 2), round(cent, 2)))
    print('\nConverting back:-')
    far = callmod.convctof(cent)
    print('The farenheit value of {1} is {0}'.format(round(far, 2), round(cent, 2)))

def calcpay():
    "Calculating the gross pay of someone based on hours worked and hourly rate"
    hrs = int(input('\n\nEnter number of hours worked:- '))
    rate = int(input('Enter the hourly rate:- '))
    grosspay = callmod.calcgross(hrs, rate)
    netpay, tax = callmod.calctax(grosspay)
    print('The gross pay for {} hours at an hourly rate of {} is {}'.format(hrs, rate, grosspay))
    print('With tax rate at one third your tax is {} and your takehome pay is {}.' \
        .format(round(tax, 2), round(netpay, 2)))

def main():
    "The main programme"
    #messwithtemperature()
    calcpay()

main()
