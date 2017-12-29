# 在wine数据集上实现前向逐步回归--控制过拟合
# 读取数据--抽取列，划分为测试集和训练集--
import pandas as pd
import numpy
from sklearn import linear_model
from math import sqrt
import matplotlib.pyplot as plt


def x_attr_select(x, x_set):
    x_out = []
    for i in range(len(x)):
        x_out.append([])
        for j in x_set:
            x_out[i].append(x[i][j])

    return x_out


target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(target_url, header=0, sep=";")
print(data.head())

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

# 前向回归过程
att_list = []           # 最佳属性列
index = range(n_cols - 1)       # 原始属性列
index_set = set(index)      # 原始属性列的set组合
oss_error = []

for i in index:
    att_set = set(att_list)     # 最佳属性列的set组合
    att_test_set = index_set - att_set      # 剩余属性列的set组合
    att_test = [ii for ii in att_test_set]  # 剩余属性列
    error_list = []
    att_temp = []                            # 测试属性列
    for i_test in att_test:
        att_temp = att_list[:]
        att_temp.append(i_test)
        x_train_temp = x_attr_select(xlist_train, att_temp)
        x_test_temp = x_attr_select(xlist_test, att_temp)
        x_train = numpy.array(x_train_temp)
        y_train = numpy.array(labels_train)
        x_test = numpy.array(x_test_temp)
        y_test = numpy.array(labels_test)

        # 模型测试
        wine_model = linear_model.LinearRegression()
        wine_model.fit(x_train, y_train)

        # 性能度量参数RMSE
        rsm_error = numpy.linalg.norm(y_test - wine_model.predict(x_test), 2) / sqrt(len(y_test))
        error_list.append(rsm_error)
        att_temp = []           # 清空测试属性列

    i_best = numpy.argmin(numpy.array(error_list))       # 得到效果最佳的那列属性
    att_list.append(att_test[i_test])       # 更新最优属性列
    oss_error.append(error_list[i_test])

print("Out of sample error versus attribute set size")
print(oss_error)


# Plot error versus number of attributes
x = range(len(oss_error))
plt.plot(x, oss_error, 'k')
plt.xlabel('Number of Attributes')
plt.ylabel('Error (RMS)')
plt.show()


# Plot histogram of out of sample errors for best number of attributes
index_best = oss_error.index(min(oss_error))        # 返回oss_error最小值所在处的索引
attributes_best = att_list[:(index_best + 1)]       # 截取误差最小时的属性列组合

# Define column-wise subsets of xListTrain and xListTest
x_train_best = x_attr_select(xlist_train, attributes_best)
x_test_best = x_attr_select(xlist_test, attributes_best)
x_train = numpy.array(x_train_best)
y_train = numpy.array(labels_train)
x_test = numpy.array(x_test_best)
y_test = numpy.array(labels_test)
wine_model = linear_model.LinearRegression()
wine_model.fit(x_train, y_train)

error_vector = y_test - wine_model.predict(x_test)
plt.hist(error_vector)
plt.xlabel("Bin Boundaries")
plt.ylabel("Counts")
plt.show()

# scatter plot of actual versus predicted
plt.scatter(wine_model.predict(x_test), y_test, s=100, alpha=0.10)
plt.xlabel('Predicted Taste Score')
plt.ylabel('Actual Taste Score')
plt.show()
