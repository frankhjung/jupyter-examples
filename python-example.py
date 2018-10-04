#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Worksheet for Juypter notebook Python example.

@author: frank
"""

#
# SUMMARY STATISTICS
#

# import iris dataset
from sklearn import datasets

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#
# USING IRIS DATASET DIRECTLY
#

# load iris data
ds = datasets.load_iris()

# setosa
X = ds.data[0:50,]
XCount = len(X)
XMin = X[:, 0].min()
XMax = X[:, 0].max()
XMean = round(X[:, 0].mean(), 3)
print(XCount, XMin, XMax, XMean)

# versicolor
Y = ds.data[50:100, :4]
YCount = len(Y)
YMin = Y[:, 0].min()
YMax = Y[:, 0].max()
YMean = round(Y[:, 0].mean(), 3)
print(YCount, YMin, YMax, YMean)

# virginica
Z = ds.data[100:150, :4]
ZCount = len(Z)
ZMin = Z[:, 0].min()
ZMax = Z[:, 0].max()
ZMean = round(Z[:, 0].mean(), 3)
print(ZCount, ZMin, ZMax, ZMean)

# pretty print setosa by putting into a dataframe
results = pd.DataFrame(
              [(XCount, XMin, XMax, XMean)],
              columns=('Count','Minimum', 'Maximum', 'Mean')
          )
print(results.head())

#
# USING A PANDAS DATAFRAME
#

# get species names from dataset to use as df index
names = ds['target_names']
list(names)

# convert to dataframe
df = pd.DataFrame(
        data = np.c_[ds['data']],
        columns = ds['feature_names'],
        dtype = 'float64',
        index = names[ds['target']]
     )

df.head(10)
df.columns
df.dtypes
df.info

# select 3 rows from each species
rows = list(range(3)) + list(range(51,53)) + list(range(101,103))
print(list(rows))
df.iloc[list(rows),:]

byspecies = df.groupby(df.index)
byspecies['sepal length (cm)'].describe()
byspecies.get_group('setosa')['sepal length (cm)'].describe()

#
# more information
#
df.info
df.dtypes
df.columns
df.head()


#
# CREATE A SCATTER PLOT
#

X = ds.data[:, :2]    # consider only first 2 columns sepal width and length
y = ds.target         # index to species 
names = ds.target_names #  distinct species
colours = ("red", "green", "blue")

plt.figure(figsize=(5, 4))
plt.clf()               # clear figure

for c, i, n in zip(colours, [0, 1, 2], names):
    plt.scatter(X[y == i, 0], X[y == i, 1], color=c, alpha=0.8, label=n)

plt.title('Sepal by Species')
plt.xlabel('length (cm)')
plt.ylabel('width (cm)')
plt.legend()
# plt.savefig("sepal.png")
plt.show()
