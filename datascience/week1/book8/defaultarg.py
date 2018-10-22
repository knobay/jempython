'1. Create a function which has a default argument'


# define function here
def my_func(arg1, arg2='encouraged'):
    return '{0} play is {1} in chess'.format(arg1, arg2)

# test
print(my_func('positional', 'optional'))
print(my_func('positional'))
