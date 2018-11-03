import matplotlib.pyplot as plt
import numpy as np


rng = np.random.RandomState(42)
steps = 1024
runs = 32
numbers = rng.randint(-9, 10, (runs, steps))
sums = numbers.cumsum(axis=1)
plt.figure(figsize=(14, 6))
plt.plot(sums.T)

plt.show()
