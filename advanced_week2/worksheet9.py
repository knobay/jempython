def activity1():
    shoppinglist = {"Beans":3, "Cheese":1, "Hummous":2, "Apples":4}
    print('Activity 1. printing the list')
    print(shoppinglist)

    print('\n\nPrinting using a loop')
    for itemindex, item in enumerate(shoppinglist):
        print(itemindex, ')', item, '\t', shoppinglist[item])

    print('\n\nPrinting total items')
    total = 0
    for item in shoppinglist:
        total += shoppinglist[item]
    print(total)


def activity2():
    doctorlist = {"name":"Peter Capaldi","docnumber":12}
    print('Doctors name is now',doctorlist["name"])
    print("Changing name...")
    doctorlist["name"] = "Jodie Whittaker"
    print('name is now...', doctorlist["name"])
    print('Adding a new key')
    doctorlist["gender"] = "female"
    print('gender is...', doctorlist["gender"])


def main():
    #activity1()
    activity2()

if __name__ == "__main__":
    main()

    
