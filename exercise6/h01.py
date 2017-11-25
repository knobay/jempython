# Import all libraries
import math
#
x = 0.3
y = 0.1 + 0.2
print("Not rounded:- x = {}, y = {} - are they the same? {}.".format(x, y, x == y))
print("Rounded now:- x = {}, y = {} - are they the same? {}.".format(round(x,10), round(y,10), round(x,10) == round(y,10)))
