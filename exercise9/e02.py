"""Exercise 9 E02 - Shopping List"""

def generatelist():
    "Do everything in one function"
    # a) generate shopping list and count it
    myshopping = [
        "milk", "eggs", "coffee", "red peppers",
        "chicken breast", "apples", "onions",
        "bread", "cucumber",
        ]
    print("list contains", len(myshopping), "items")
    # b) print out the shopping list
    print("Shopping List", myshopping)
    # c) add butter
    myshopping.append("butter")
    print("Shopping List", myshopping)
    # d) add some lemons before onions
    onions = myshopping.index("onions")
    myshopping.insert(onions, "lemons")
    print("Shopping List", myshopping)
    # e) remove coffee
    myshopping.remove("coffee")
    print("Shopping List", myshopping)
    # f) remove chicken with del
    del myshopping[3]
    print("Shopping List", myshopping)
    # g) put tonights dinner in a different list
    dinner = []
    for i in [1, 1, 5]:
        dinner.append(myshopping.pop(i))
    print("Shopping List", myshopping)
    print("Dinner list", dinner)
    # h) check that lemons are in the shopping list
    if "lemons" in myshopping:
        print('lemons is still in the list')
    else:
        print('lemons is no longer on the list')
    return

generatelist()
