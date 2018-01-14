from urllib import request
import pandas as pd
import numpy
from math import sqrt
from sklearn import linear_model
from sklearn.linear_model import LassoCV
import matplotlib.pyplot as plot


target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(target_url, header=0, sep=";")

summary = data.describe()
n_cols = len(data.columns)
n_rows = len(data.index)


# get mean and std
means = []
stds = []
for j in range(n_cols):
    means.append(summary.iloc[1, j])
    stds.append(summary.iloc[2, j])

# 归一化
xlist = numpy.array(data.iloc[:, 0:(n_cols - 1)])
label = numpy.array(data.iloc[:, (n_cols - 1)])
for i in range(n_rows):
    for j in range(n_cols - 1):
        xlist[i][j] = (xlist[i][j] - means[j]) / stds[j]
    label[i] = (label[i] - means[-1]) / stds[-1]

alphas, coefs, _ = linear_model.lasso_path(xlist, label, return_model= False)
plot.plot(alphas, coefs.T)

plot.xlabel('alpha')
plot.ylabel('Coefficients')
plot.axis('tight')
plot.semilogx()
ax = plot.gca()
ax.invert_xaxis()
plot.show()