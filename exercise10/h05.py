"""simply multiplies a (c × r) matrix by a number."""

def make_matrix(width, height):
    "Creates a list containing width lists, each of height items, all set to 0"
    matrix = [[0 for x in range(width)] for y in range(height)]
    return matrix


def add_matrices(matrixa, matrixb, size):
    "Adds two matrices of a specified size"
    matrixc = make_matrix(size[0], size[1])
    counter = 0

    while counter < len(matrixa):
        innercount = 0
        while innercount < len(matrixa[counter]):
            matrixc[counter][innercount] = int(matrixa[counter][innercount]) + int(matrixb[counter][innercount])
            innercount += 1
        counter += 1
    return matrixc

def multiply_matrices(matrixa, matrixb, size):
    "Multiplies two matrices of a specified size"
    matrixc = make_matrix(size[0], size[1])
    counter = 0

    while counter < len(matrixa):
        innercount = 0
        while innercount < len(matrixa[counter]):
            summation = 0
            i = 0
            j = 0
            while i < size[0]:
                while j < size[1]:
                    summation += int(matrixa[i][innercount]) * int(matrixb[counter][j])
                    j += 1
                i += 1
            matrixc[counter][innercount]+= summation

            innercount += 1
        counter += 1
    return matrixc

def print_matrix(matrix):
    "Prints out a matrix"
    counter = 0

    while counter < len(matrix):
        innercount = 0
        while innercount < len(matrix[counter]):
            print(matrix[counter][innercount], "\t", end="")
            innercount += 1
        print("\n")
        counter += 1
    return

def populate_matrix(matrix, usr_message):
    "put numbers in a matrix according to input from user"
    print("Put in numbers for ", usr_message)
    counter = 0
    while counter < len(matrix):
        innercount = 0
        while innercount < len(matrix[counter]):
            matrix[counter][innercount] = input("Enter {}, {}: ".format(counter, innercount))
            innercount += 1
        counter += 1
    print("Thanks.  You put in: ")
    print_matrix(matrix)
    return

def ask_size():
    "Asks the user for 2 numbers to size the matrix"
    print("Need dimensions for matrices")
    width = input("Enter width")
    height = input("enter height")
    return (int(width), int(height))

def main():
    "The main program"
    size = ask_size()
    my_matrix1 = make_matrix(size[0], size[1])
    my_matrix2 = make_matrix(size[0], size[1])
    populate_matrix(my_matrix1, 'Matrix 1')
    populate_matrix(my_matrix2, 'Matrix 2')
    my_matrix3 = multiply_matrices(my_matrix1, my_matrix2, size)
    print("result is:")
    print_matrix(my_matrix3)

main()
