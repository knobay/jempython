PI = 3.14159

def calculate_area(radius):
    # calculate the area of a circle
    radius = float(radius)
    area = PI * 2 * radius
    return area

#main program

def main():
    "The main program"
    radius = input("what is the radius")
    print('the area is {0}'.format(calculate_area(radius)))

if __name__ == "__main__":
    main()