
"""Uniit 8 E01, week2"""

# Gets an input from the user works
# out if even or odd and reports result

def odd_even():
    "Works out if a number is even or odd and then tells the user"
    userinput = input("Enter a number")
    if int(userinput)%2 == 1:
        result = 'odd'
    else:
        result = 'even'
    print(result)
    return

# Now you can call printme function
odd_even()
