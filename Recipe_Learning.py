import numpy as np
import pandas as pdb
from pandas import read_csv

import matplotlib.pyplot as plt
import seaborn as sns
from ggplot import *

recipes = read_csv("/home/max/Repos/Recipe_Learning/epi.csv")


recipes = recipes[recipes['calories'] < 10000].dropna()


g1 = ggplot(recipes, aes(x='calories', y='dessert')) + geom_point()
# print(g1)

sns.set(style="darkgrid")
g2 = sns.regplot(x="calories", y="dessert", data=recipes, logistic=True)
g2.figure.set_size_inches(8, 8)

plt.show()