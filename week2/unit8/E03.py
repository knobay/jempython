
"""Uniit 8 E03, week2"""

# Gets an input from the user works
# out if it contains a voul


def voul_or_not():
    "Works out if the user has entered a voul or consonant"
    userinput = input("Enter a letter")

    if userinput == 'a' or userinput == 'e' or userinput == 'i' or userinput == 'o' or userinput == 'u':
        result = 'that was a voul'
    elif len(userinput)>1 or userinput.isdigit():
        result = 'invalid input'
    else:
        result = 'that was a consonant'
    print(result)
    return


# call the funciton
voul_or_not()
