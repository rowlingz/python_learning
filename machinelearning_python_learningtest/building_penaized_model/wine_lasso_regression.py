import pandas as pd
import numpy
from sklearn.linear_model import LassoCV
import matplotlib.pyplot as plt


target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(target_url, header=0, sep=";")
print(data.head())

summary = data.describe()

print(summary)

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


wine_model = LassoCV(cv=10).fit(xlist, label)

plt.figure()
plt.plot(wine_model.alpha_, wine_model.mse_path_)
plt.plot(wine_model.alpha_, wine_model.mse_path_.mean(axis=1), label='Average MSE Across Folds', linewidth=2)
plt.axvline(wine_model.alpha_, linestyle='--', label='CV Estimate of Best alpha')
plt.semilogx()
plt.legend()
ax = plt.gca()
ax.invert_xaxis()
plt.xlabel('alpha')
plt.ylabel('Mean Square Error')
plt.axis('tight')
plt.show()
