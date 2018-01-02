#
import pandas as pd
import numpy
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


# Build cross-validation loop to determine best coefficient values
n_cross = 5
n_steps = 350
step_size = 0.004

# initialize list for storing errors
errors = []
for i in range(n_steps):
    errors.append([])

for i_cross in range(n_cross):
    # Define test and training index sets
    index_train = [a for a in range(n_rows) if a % n_cross != i_cross * n_cross]
    index_test = [a for a in range(n_rows) if a % n_cross == i_cross * n_cross]

    # define test and training x and y
    x_train = [x[i] for i in index_train]
    x_test = [x[i] for i in index_test]
    y_train = [y[i] for i in index_train]
    y_test = [y[i] for i in index_test]


    n_rows_of_train = len(x_train)
    n_rows_of_test = len(x_test)

    beta = [0.0] * (n_cols - 1)
    beta_matrix = []
    beta_matrix.append(list(beta))

    # get residuals
    for i_step in range(n_steps):
        residuals = [0.0] * n_rows_of_train
        for j in range(n_rows_of_train):
            labels_hat = sum(x_train[j][k] * beta[k] for k in range(n_cols - 1))
            residuals[j] = y_train[j] - labels_hat

        # calculate correlation between attribute columns from normalized wine and residual
        corr = [0.0] * (n_cols - 1)
        for j in range(n_cols - 1):
            corr[j] = sum(x_train[k][j] * residuals[k] for k in range(n_rows_of_train)) / n_rows_of_train

        # the largest of correlation
        i_star = 0
        corr_star = corr[0]
        for j in range(1, (n_cols - 1)):
            if abs(corr_star) < abs(corr[j]):
                i_star, corr_star = j, corr[j]

        #  beta列表中对应元素增加
        beta[i_star] += step_size * corr_star / abs(corr_star)
        beta_matrix.append(list(beta))

        # Use beta just calculated to predict and accumulate out of sample error - not being used in the calc of beta
        for j in range(n_rows_of_test):
            labels_hat = sum(x_test[j][k] * beta[k] for k in range(n_cols - 1))
            error = y_test[j] - labels_hat
            errors[i_step].append(error)


cv_curve = []
for err in errors:
    mse = sum(x ** x for x in err) / len(err)
    cv_curve.append(mse)

print(cv_curve)

min_mse = min(cv_curve)
min_index = [i for i in range(len(cv_curve)) if cv_curve[i] == min_mse]
print("Minimum Mean Square Error", min_mse)
print("Index of Minimum Mean Square Error", min_index)


x_axis = range(len(cv_curve))
plt.plot(x_axis, cv_curve)

plt.xlabel("Steps Taken")
plt.ylabel("Mean Square Error")
plt.show()



# # plot range of beta values for each attribute
# for i in range(n_cols - 1):
#     coef_curve = [beta_matrix[k][i] for k in range(n_steps)]
#     x_axis = range(n_steps)
#     plt.plot(x_axis, coef_curve)
#
# plt.xlabel("Steps Taken")
# plt.ylabel("Coefficient Values")
# plt.show()









