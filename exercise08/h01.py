"""Uniit 8 H01, week2"""

# Gets an input from the user works
# out if it is an Armstrong number


def armstrong_check():
    "Works out if the user has entered an Armstrong number"
    userinput = input("Enter a 3 digit number")
    evaluation = int(userinput[0])**3 + int(userinput[1])**3 + int(userinput[2])**3

    if len(userinput) > 3:
        result = 'invalid input'
    elif int(userinput) == evaluation:
        result = 'that was an armstrong number'
    else:
        result = 'that was not an armstrong number'
    print(result)
    return


# call the funciton
armstrong_check()
