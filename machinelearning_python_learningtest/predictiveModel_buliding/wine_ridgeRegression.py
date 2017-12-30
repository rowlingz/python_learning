# ridge regression for wine

import pandas as pd
import numpy
from sklearn import linear_model
from math import sqrt
import matplotlib.pyplot as plt


target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(target_url, header=0, sep=";")

n_cols = len(data.columns)
n_rows = len(data.index)


# 将数据转换为X-Y
xlist = numpy.array(data.iloc[:, 0:(n_cols - 1)])
index = range(len(xlist[1]))
labels = numpy.array(data.iloc[:, (n_cols - 1)])


# 将样本分成训练集和测试集(2/3--1/3)
xlist_test = []
xlist_train = []
labels_test = []
labels_train = []
for i in range(n_rows):
    if i % 3 == 0:
        xlist_test.append(xlist[i, :])
        labels_test.append(labels[i])
    else:
        xlist_train.append((xlist[i, :]))
        labels_train.append(labels[i])

x_train = numpy.array(xlist_train)
y_train = numpy.array(labels_train)
x_test = numpy.array(xlist_test)
y_test = numpy.array(labels_test)

# ridge regression
alpha_list = [0.1 ** i for i in range(7)]

rms_error = []
for alph in alpha_list:
    model = linear_model.Ridge(alpha= alph)
    model.fit(x_train, y_train)
    error = numpy.linalg.norm(y_test - model.predict(x_test), 2) / sqrt(len(y_test))
    rms_error.append(error)

x = range(len(rms_error))
plt.plot(x, rms_error, 'r-')
plt.xlabel("- log(alph)")
plt.ylabel("Error (RMS)")
plt.show()


index_best = rms_error.index(min(rms_error))
alph = alpha_list[index_best]
best_model = linear_model.Ridge(alpha=alph)
best_model.fit(x_train, y_train)
error = y_test - best_model.predict(x_test)
plt.hist(error)
plt.xlabel("Bin Boundaries")
plt.ylabel("Counts")
plt.show()

plt.scatter(best_model.predict(x_test), y_test, s= 100, alpha=0.10)
plt.xlabel("Predicted Taste score")
plt.ylabel("Actual score")
plt.show()