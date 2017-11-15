#
# E03
#
name = ""
birth_country = ""
birth_city = ""

print("\n--------------------------------------------------------------")
print("\n------------------------     E03     -------------------------\n")
while len(name) < 2:
    name = input("Please enter your name: ")
    name = name.strip()
    if len(name) < 2:
        print("A name of less than 2 non-space characters is taking the piss.. try again!")
    if name.isnumeric() == True:
        print("A name consisting entirely of numbers is taking the piss.. try again!")
        name = ""

while len(birth_country) < 2:
    birth_country = input("Please enter country you were born in: ")
    birth_country = birth_country.strip()
    if len(birth_country) < 2:
        print("No countries have names less than 2 non-space characters you're taking the piss.. try again!")
    if birth_country.isnumeric() == True:
        print("No countries have names consisting entirely of numbers you're taking the piss.. try again!")
        birth_country = ""

while len(birth_city) < 2:
    birth_city = input("Please enter city where you were born: ")
    birth_city = birth_city.strip()
    if len(birth_city) < 2:
        print("No countries have names less than 2 non-space characters you're taking the piss.. try again!")
    if birth_city.isnumeric() == True:
        print("No countries have names consisting entirely of numbers you're taking the piss.. try again!")
        birth_city = ""

print("\n--------------------------------------------------------------")
print("\nHello {} from {} in {}".format(name,birth_city,birth_country))
print("\nYep... after all that this greeting is all you get")
print("\n--------------------------------------------------------------\n")

