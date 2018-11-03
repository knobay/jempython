import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

x = np.arange(0, 10, 0.5)

y = np.random.randn(20)

fig, ax = plt.subplots()

plt.style.use('seaborn-whitegrid')

plt.plot(x, y)

plt.show()

print(x)
print(y)
