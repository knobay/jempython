""" Using the following example data, please define a random error 
and plot the errorbar, using nice aesthetics (something that looks decent to you).
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

h1 = np.random.normal(size=2048)

h2 = np.random.normal(loc=0.2, scale=.5, size=2048)

h3 = np.random.normal(loc=-0.5, scale=2, size=2048)

plt.hist(h1, bins=100, alpha=0.3)
plt.hist(h2, bins=100, alpha=0.3)
plt.hist(h3, bins=100, alpha=0.3)

plt.show()
