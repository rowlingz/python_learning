#
import pandas as pd
import numpy




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
xlist = []
label = []
for i in range(n_rows):
    xlist.append([])
    label.apend([])
    for j in range(n_cols):
        if j != (n_cols - 1):
            xlist[i].append((data.iloc[i, j] - means[i]) / stds[i])
        else:
            label[i].append((data.iloc[i, j] - means[i]) / stds[i])

beta = [0.0] * (n_cols - 1)







