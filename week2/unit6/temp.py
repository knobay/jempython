print("power before import of math {}.".format(pow(2,3)))
import math
print("power after import of math - using the math funciton {}.".format(math.pow(2,3)))
print("power after import of math - using old pow {}.".format(pow(2,3)))
#
print("\n--------------------------------------------------------------")
print("------------------------     E01     -------------------------")
x = 5
y = (6*(x**2)+(3*x)+2)
print("a)\t{}".format(y))
a = 3
b = 10
c = -2
y1 = (((b*-1)+math.sqrt(b**2-(4*a*c)))/(2*a))
y2 = (((b*-1)-math.sqrt(b**2-(4*a*c)))/(2*a))
print("b)\t y1 = {}".format(y1))
print("b)\t y2 = {}".format(y2))

