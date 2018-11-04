""" 5. Fill areas.
Using the following example data, please use fill_between to fill regions /
between these lines in different combinations. Fill between y1 and y2, /
between y2 and y3, and between y1 and y3. For each area use a different /
color and use a good alpha (by trial and errors) to make all areas visible."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x  = np.linspace(0, 3, 200)
y1 = x ** 2 + 3
y2 = np.exp(x) + 2
y3 = np.sin(x)


#plt.fill_between(x, y1, y2)
plt.fill_between(x, y1, y2, alpha=0.3)
plt.fill_between(x, y1, y3, alpha=0.3)
plt.fill_between(x, y2, y3, alpha=0.1)

plt.show()