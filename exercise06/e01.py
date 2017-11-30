import math
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
x = 34
lgx = math.log10(x)
y = x*lgx
print("c)\t y = {}".format(y))
x = 0.5
y = (math.sin(x-math.pi)+math.cos(x+math.pi))**2
print("d)\t y = {}".format(y))
x = 10
x1 = x/3.6
y = math.sqrt(math.sqrt(math.sqrt(x1)))
print("e)\t y = {}".format(y))
x=0
y = (math.asin(x)+math.acos(x))
print("f)\t y = {}".format(y))
