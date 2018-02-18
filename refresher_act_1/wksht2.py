def printName(name):
    "To print the name passed in as a parameter"
    print('Hello ', name)

def rectArea(length, width):
    "To calculate the area of a rectangle"
    print('The area of a rectangle {} long and {} wide is {}.'.format(length, width, length * width))
    return

def cuboidVol(length, width, height):
    "To calculate the area of a rectangle"
    print('The volume of a cuboid {} long, {} wide and {} high is {}.'.format(length, width, height, length * height * width))
    return

def main():
    "The main programme"
    printName('Jim Strachey')
    length = float(input('Enter the length of the rectangle:- '))
    width = float(input('Enter the width of the rectangle:- '))
    height = float(input('Enter the height of the cuboid:- '))
    rectArea(length, width)
    cuboidVol(length, width, height)

main()
