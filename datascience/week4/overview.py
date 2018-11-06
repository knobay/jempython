""" Describe general statistics and memory
/values for the data frame, what can you evaluate from it"""

import pandas.tools.plotting as plotting
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')
fig, axes = plt.subplots()
axes.xaxis.set_visible(False)
axes.yaxis.set_visible(False)
axes.set_frame_on(False)
plotting.table(axes, df.describe().round(2), loc='upper right')

plt.show()