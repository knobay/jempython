import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()


"""plt.set_cmap('Greys')
for i in range(10):
    plt.matshow(digits.images[i])
    plt.show()
"""

randomdim = np.random.randint(0, high=64, size=4)

for i in range(3):
    xvals = [1, 25, 38, 56]
    yvals = [digits.data[i][randomdim[0]], digits.data[i][randomdim[1]], digits.data[i][randomdim[2]], digits.data[i][randomdim[3]]]
    plt.scatter(randomdim, yvals)
plt.show()
