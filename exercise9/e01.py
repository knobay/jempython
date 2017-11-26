"""Unit 8 H01, week2"""

def favouritestuff():
    "Prints out Kims favourite ski resorts"
    start = 'n'
    while start != 'y':
        start = input("press y to continue")
    kimsfavourites = ['Chamonix', 'St Anton', 'Oslo Winterpark', 'Kirkwood', 'Bariloche']
    while kimsfavourites:
        print(kimsfavourites.pop())
    return

favouritestuff()
