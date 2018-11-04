"""3. Scatter plot. /
Using the digits dataset from sklearn, plot four /
dimensions at random, in the same manner we did for the iris dataset. /"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()

randomdim = np.random.randint(0, high=64, size=4)

for i in range(10):

    yvals = [digits.data[i][randomdim[0]], digits.data[i][randomdim[1]], digits.data[i][randomdim[2]], digits.data[i][randomdim[3]]]
    plt.scatter(randomdim, yvals)

plt.show()
