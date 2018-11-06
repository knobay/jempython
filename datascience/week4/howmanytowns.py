"""2. How many and what were the towns where people embarked on the Titanic?"""

import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import webbrowser

titanic = sns.load_dataset('titanic')

Total = titanic['embark_town'].nunique()
towns = titanic['embark_town'].unique()
print(Total)
print(towns)
