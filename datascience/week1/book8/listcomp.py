'''rewrite the commented out code using list comprehensions'''


def add_five(numbers):
    'gets a list of numbers and adds five to each then returns the result'
    # l = []
    # for num in numbers:
    #     l.append(num + 5)
    # return l

    result = [x+5 for x in numbers]
    return result

print(add_five({1, 2, 3}))
