PI = 3.14159

def calculate_volume(dims):
    # calculate the area of a circle
    radius = float(dims['radius'])
    height = float(dims['height'])
    area = PI * 2 * radius * height
    return area

#main program

def main():
    "The main program"
    dims = {}

    dims['radius'] = input("what is the radius")
    dims['height'] = input("what is the height")
    print('the area is {0}'.format(calculate_volume(dims)))

if __name__ == "__main__":
    main()