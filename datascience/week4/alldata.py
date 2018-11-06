""" Dump the whole data set on the screen in the browser as an html table """

# import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns
import os
import webbrowser

titanic = sns.load_dataset('titanic')
html = titanic.to_html()

path = os.path.abspath('temp.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(html)
webbrowser.open(url)
