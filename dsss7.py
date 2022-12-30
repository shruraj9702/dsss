import math

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
from sklearn import neighbors
from matplotlib.colors import ListedColormap

directory = 'C:/Users/rshru/OneDrive/Desktop/DSSS/7'

classification = pd.read_csv(os.path.join(directory, 'classification.csv'))
reg_1 = pd.read_csv(os.path.join(directory, 'regression_1.csv'))
reg_2 = pd.read_csv(os.path.join(directory, 'regression_2.csv'))
print(classification.head())
print(reg_1.head())
print(reg_2.head())

# TASK1: Classification
cmap_colors = ListedColormap(['#AAAAFF', '#AAFFAA', '#FFAAAA'])
X, y = np.c_[classification['x1'], classification['x2']], classification['label']
weights = ['uniform', 'distance']
kNN = neighbors.KNeighborsClassifier(3, weights=weights[1])
kNN.fit(X, y)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = kNN.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=cmap_colors)
sns.scatterplot(data=classification, x='x1', y='x2', hue='label')
plt.show()


# TASK2: Regression1
def sine_function(val):
    return 2 * (np.sin(val - 0.65))  # Amplitude = 2 and Offset = 0.65


x_min, x_max = reg_1['x1'].min(), reg_1['x1'].max()
x = np.arange(x_min, x_max, 0.02)
line = sine_function(x).reshape(-1, 1)
plt.plot(x, line, '--', color='red', linewidth=3)
plt.scatter(reg_1['x1'], reg_1['x2'])
plt.title('Regression 1')
plt.show()

# TASK3: Regression2
x_min, x_max = reg_2['x1'].min(), reg_2['x1'].max()
x = np.arange(x_min, x_max, 0.02)
reg = LinearRegression()
reg.fit(np.array(reg_2['x1']).reshape((-1, 1)), np.array(reg_2['x2']))
line = reg.predict(x.reshape((-1, 1)))
plt.plot(x, line, '--', color='red', linewidth=3)
plt.scatter(reg_2['x1'], reg_2['x2'])
plt.title('Regression 2')
plt.show()
