"""Exercise 10, E02, Finding the maximum"""


def xfunction(x):
    "work out the equation"
    y = 5-(x-3)**2
    return y

def main():
    "do all that other stuff"
    x = [i for i in range(0, 1001, 1)]
    for i in range(0, 1001, 1):
        x[i] = x[i]/100
    fx = []
    counter = 0
    max = 0
    while counter < len(x):
        calculated=xfunction(x[counter])
        if calculated > max:
            max = calculated
        fx.append(calculated)
        counter = counter+1
    print(max)

main()

