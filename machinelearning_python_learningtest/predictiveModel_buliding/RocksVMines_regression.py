# 将二分类问题转换为线性回归问题 rocks-V-mines
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from penalized import lars, normalize


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")


data = pd.read_csv(target_url, header=None, prefix="V")
# print(data.head())
n_cols = len(data.columns)
n_rows = len(data.index)

# 将数据的属性和标签分开，并将标签转换为数值型（M-1.0,R-0.0）

xlist = numpy.array(data.iloc[:, 0:(n_cols - 1)])
labels = numpy.array(data.iloc[:, (n_cols - 1)])

y1 = []
for i in range(n_rows):
    y1.append([])
    if labels[i] == "M":
        y1[i] = [1.0]
    else:
        y1[i] = [0.0]

print(labels)
print(y1)

x = normalize(xlist)
y = normalize(numpy.array(y1))

beta_matrix = lars(x, y)
print(len(beta_matrix))
print(len(beta_matrix[0]))

for j in range(n_cols - 1):
    coef_curve = [beta_matrix[k][j] for k in range(350)]
    x_axis = range(350)
    plt.plot(x_axis, coef_curve)

plt.show()

