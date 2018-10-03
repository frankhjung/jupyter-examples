#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:42:56 2018

@author: frank
"""

#
# SUMMARY STATISTICS
#
# Using a scikit learn DataSet

# import the datasets package
from sklearn import datasets
from statistics import mean

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load iris data
ds = datasets.load_iris()

# save names for class category
names = ds['target_names']

# convert to dataframe
df = pd.DataFrame(
        data = np.c_[ds['data']],
        columns = ds['feature_names'],
        dtype = 'float64',
        index = ds['target']
     )

# add class as a category
df['class'] = pd.Series(
                names[ds['target']], 
                dtype = 'category'
              )

# calculate some basic statistics
XMean = round(mean(df['sepal length (cm)']), 2)
XCount = len(df['sepal length (cm)'])
XMin = min(df['sepal length (cm)'])
XMax = max(df['sepal length (cm)'])

# display our results
print(XCount, XMin, XMax, XMean)

# pretty print by putting into a dataframe
results = pd.DataFrame(
              [(XCount, XMin, XMax, XMean)],
              columns=('Count','Minimum', 'Maximum', 'Mean')
          )
print(results.head())

#
# more information
#
df.info
df.dtypes
df.columns
df.head()


#
# PLOTTING
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
plt.show()