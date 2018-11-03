import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# %matplotlib inline
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



# 3. Scatter plot. (★★☆)
# Using the digits dataset from sklearn, plot four dimensions at random, in the same manner we did for the iris dataset.


digits = load_digits()
# print(digits['DESCR'])



# print(digits.data.shape)

# plt.gray()
# plt.matshow(digits.images[0])
# plt.matshow(digits.images[1])
plt.matshow(digits.images[3])

plt.show()


#fig3, ax3 = plt.subplots(figsize=(14, 7))
#ax3.scatter(digits[:, 0], digits[:, 1], alpha=0.5, s=256*digits[:, 3], c=digits.target, cmap='viridis', label='Size depicts {0}'.format(digits.feature_names[3]))
#ax3.legend(frameon=True, borderpad=0.9)
# ax3.set_xlabel(digits.feature_names[0])

#print(digits.feature_names[0])
# ax3.set_ylabel(digits.feature_names[1])

# plt.show()