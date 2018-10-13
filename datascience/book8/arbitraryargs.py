def arbitraryargs(*args):
    for member in args:
        print(member)
    pass

arbitraryargs(1, 'gemma', 2.0, 'the somme')

args = [1, 'two', 3.14]
kwargs = {'pinkie': 'pie', 'rainbow': 'dash'}

arbitraryargs(args)
arbitraryargs(kwargs)
