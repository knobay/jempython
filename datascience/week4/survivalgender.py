"""4. What is the survival rate depending on the gender? /
Use a bar plot to show the difference."""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


titanic = sns.load_dataset('titanic')

males = len(titanic.query("sex=='male'").index)
malesurvivors = len(titanic.query("sex=='male' and survived==True").index)
females = len(titanic.query("sex=='female'").index)
femalesurvivors = len(titanic.query("sex=='female' and survived==True").index)


resultindex = np.array(['Passengers', 'Survivors'])
males = pd.Series([males, malesurvivors], index=resultindex)
females = pd.Series([females, femalesurvivors], index=resultindex)
results = pd.DataFrame([males, females], index=['Men', 'Women'])

plt.plot(results)

plt.show()

