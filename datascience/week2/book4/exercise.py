"""Numpy exercises on array manipulation.  Start quite easy and get a bit hard at the end."""

# Exercise 1. just import numpy.
import numpy as np

# Exercise 2.  print the version
e2 = (np.version.short_version)
print('result of e2:', e2, '\n')

# Exercise 3.  A null vector of size 10
e3 = np.zeros(10)
print('result of e3:', e3, '\n')

# Exercise 4.  A vector with numbers from 10 to 49
e4 = np.arange(10, 50)
print('result of e4:', e4, '\n') 

# Exercies 5. Create a 3x3 matrix with values ranging from 0 to 8
e5 = np.arange(0, 9).reshape(3, 3)
print('result of e5:', e5, '\n')

# Exercise 6. Create a 3x3x3 array with random values
e6 = np.random.randint(1, 10, size=(3, 3, 3))
print('result of e6:', e6, '\n')


# Exercise 7. Sort the columns of the array
x = np.array([[3, 7],
              [7, 3],
              [1, 2]])
e7 = x.sort(0)
print('result of e7:', e7, '\n')

# Exercise 8. Select the 3rd, 4th and 7th column of the following array
y = np.arange(32).reshape(4, 8)
e8 = y[:, [2, 3, 6]]
print('result of e8:', e8, '\n')

# Exercise 9. Use argsort to sort the following array 
x = np.array([2, 7, 42, 27, 6, 9, 12])
e9 = x.argsort()
print('result of e9:', e9, '\n')

# for i in e9:
#    print(x[i])

# exercise 10. Retrieve all positive values smaller than 7
x = np.arange(-6, 58, 2).reshape(4, 8)
e10 = x[x < 7]
print('result of e10:', e10, '\n')

# exercise 11. In a single operation add 2 to all odd columns and 7 to /
# all even columns
x = np.arange(32).reshape(4, 8)
x[:, :: 2], x[:, 1:: 2] = x[:, :: 2] + 2,  x[:, 1:: 2] + 7
e11 = x
print(e11)
