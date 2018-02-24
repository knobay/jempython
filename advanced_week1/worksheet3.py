"""Convert temperatures"""

def convert(fahrenheit):
    "convert fahrenheit"
    centigrade = (fahrenheit - 32) * (5 / 9)
    return centigrade

def convert_to_fahrenheit(centigrade):
    "convert centigrade to fahrenheit "
    fahrenheit = (centigrade * (9 / 5)) + 32
    return fahrenheit

def main():
    "The main program"
    fahrenheit = float(input("Enter value in Fahrenheit"))
    print(convert(fahrenheit))

    centigrade = float(input("Enter value in Centigrade"))
    print(convert_to_fahrenheit(centigrade))

if __name__ == "__main__":
    main()