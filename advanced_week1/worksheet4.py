import mymodules

def get_currency():
    "Ask the user which currency they want"
    currency = int(input("Enter 1 for dollars and 2 for krone"))
    return currency




def main():
    how_much = float(input("How many pounds do you have"))
    currency = get_currency()
    if currency == 1:
        dollars = mymodules.pound_dollar(how_much)
        print('You have ', dollars, 'dollars')
    elif currency == 2:
        krones = mymodules.pound_krone(how_much)
        print('You have ', krones, 'krones')


main()

