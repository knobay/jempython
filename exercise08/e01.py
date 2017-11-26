
"""Uniit 8 E01, week2"""

# Gets an input from the user works
# out if even or odd and reports result

# do the work in a function.  Essential for pylint to not get uppity.
def odd_even():
    "Works out if a number is even or odd and then tells the user"
    userinput = input("Enter a number")
    if userinput.isdigit():
        if int(userinput)%2 == 1:
            result = 'odd'
        else:
            result = 'even'
        print(result)
        return
    else:
        print("invalid input")
# call the function
odd_even()
