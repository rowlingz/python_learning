#
import pandas as pd
import numpy
import matplotlib.pyplot as plt



def s(z, gamma):
    if gamma > z:
        return 0.0
    else:
        return (z / abs(z)) * (abs(z) - gamma)

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
    label.append([])
    for j in range(n_cols):
        if j != (n_cols - 1):
            xlist[i].append((data.iloc[i, j] - means[j]) / stds[j])
        else:
            label[i].append((data.iloc[i, j] - means[j]) / stds[j])

x = numpy.array(xlist)
y = numpy.array(label)

# select the value for alpha parameter
alpha = 1

# determine the value of lambda
xy = [0.0] * (n_cols - 1)
for i in range(n_rows):
    for j in range(n_cols - 1):
        xy[j] += x[i][j] * y[i]

print(xy)
max_xy = 0.0
for j in range(n_cols):
    val = x[j][0] / n_rows
    if val > max_xy:
        max_xy = val

lam = max_xy / alpha

# initialize the beta
beta = [0.0] * (n_cols - 1)
beta_matrix = []
beta_matrix.append(list(beta))


# begin iteration
steps = 100
lam_mult = 0.93
nzlist = []

for step in range(steps):
    lam = lam * lam_mult

    delta_beta = 100.0
    eps = 0.01
    inter_step = 0
    beta_inner = list(beta)
    while delta_beta > eps:
        inter_step += 1
        if inter_step > 100:
            break

        beta_strat = list(beta_inner)
        for j in range(n_cols - 1):
            xyj = 0.0
            for i in range(n_rows):
                y_pre = sum(x[i][k] * beta_inner[k] for k in range(n_cols - 1))
                residual = y[i] - y_pre

                xyj += x[i][j] * residual

            unc_beta = xyj / n_rows + beta_inner[j]
            beta_inner[j] = s(beta_inner[j], lam * alpha) / (1 + lam * (1 - alpha))

    beta = beta_inner
    beta_matrix.append(list(beta))

    nzbeta = [index for index in range(n_cols - 1) if beta[index] != 0.0]
    for q in nzbeta:
        if q not in nzlist:
            nzlist.append(q)
print(nzlist)

for j in range(n_cols - 1):
    coef_curve = [beta_matrix[k][j] for k in range(len(beta_matrix))]
    plt.plot(range(len(beta_matrix)), coef_curve)

plt.xlabel("Steps Taken")
plt.ylabel("Coefficient Values")
plt.show()




