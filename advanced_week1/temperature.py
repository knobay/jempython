"""Convert temperatures"""

def convert(fahrenheit):
    "convert fahrenheit"
    centigrade = (fahrenheit - 32) * (5 / 9)
    return centigrade

def main():
    "The main program"
    fahrenheit = float(input("Enter value in Fahrenheit"))
    print(convert(fahrenheit))

if __name__ == "__main__":
    main()