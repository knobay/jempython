import numpy as np
import matplotlib as mpl


from sklearn.datasets import load_digits

plt.style.use('seaborn-talk')
mpl.rcParams['figure.figsize'] = (12.5, 6.0)

# Create six plots in the same figure, using a two column and three column 
# configuration. Plot np.sin(x) and np.cos(x) or any custom function in  these plots.

# Please do the same exercise for the MATLAB (plt) interface and for the Pythonic (ax) interface'

fig, axi = plt.subplots(1, 2, figsize=(14, 5))

# 2 columns using the pythonic way

mydata = np.linspace(0, 100, 100)
axi.flat[0].plot(mydata, np.sin(mydata),)
axi.flat[1].plot(mydata, np.sin(mydata),)


# 3 columns using matlab style

plt.figure(figsize=(13, 7))

plt.subplot(231)
plt.plot(mydata, np.exp(mydata))
plt.title('$e^x$')

plt.subplot(132)
plt.plot(mydata, 1/np.exp(mydata))
plt.title('$1/e^x$')

plt.subplot(133)
plt.plot(mydata, np.tan(mydata))
plt.title('$tan(x)$')


plt.show()

# 2. Plot on the same figure. (★★☆)
# Create four plots in the same figure, for any four custom functions
# f(). Your  x  should have at least 10000 samples. The plots 
# # should be correctly labeled and have the appropriate 
# limits for easy viewing.


data2 = np.linspace(1, 100, 10000)

fig2, ax2 = plt.subplots(2, 2, figsize=(5, 5))

ax2.flat[0].plot(data2, np.sin(data2),)
ax2.flat[1].plot(data2, np.sin(data2),)
ax2.flat[2].plot(data2, np.sin(data2),)
ax2.flat[3].plot(data2, np.sin(data2),)

# Exercise three makes no sense at all.
