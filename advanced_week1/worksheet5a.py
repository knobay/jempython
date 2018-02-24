def get_items():
    "gets a number of items into a list from user input"
    items = []
    for i in range(5):
        items.append(input("what is in your pocket?"))
    return items

def main():
    items = get_items()
    print(items)
    print('The item at position 3')
    print(items[3])
    del(items[0])
    print('The item at position 3')
    print(items[3])

if __name__ == "__main__":
    main()
