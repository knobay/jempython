""" 4. Error bars. /
Using the following example data, please define a random error and plot the errorbar,/
using nice aesthetics (something that looks decent to you)."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

x = np.arange(0.1, 20, 0.5)

y = np.exp(-x) + (np.random.randn(40)*0.1)

z = np.exp(-x)

fig, ax = plt.subplots()

plt.style.use('seaborn-whitegrid')

plt.errorbar(x, y, yerr=0.4, color='black',
             ecolor='lightgray', elinewidth=3, capsize=0)

plt.plot(x, z)

plt.show()
