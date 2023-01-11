import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris = sns.load_dataset('iris')
iris.head()

sns.countplot(x=iris["species"])
plt.show()
