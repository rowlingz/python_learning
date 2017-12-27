# RocksVMines 训练简单分类器
import pandas as pd
import numpy
from sklearn import datasets,linear_model
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plot


def confusion_matrix(prediction, actual,threshold):
    if len(prediction) != len(actual):
        return -1
    matrix = {"tp": 0.0, "fn": 0.0, "fp": 0.0, "tn": 0.0}
    for i in range(len(prediction)):
        if prediction[i] > threshold:
            if actual[i] > threshold:
                matrix["tp"] += 1.0
            else:
                matrix["fp"] += 1.0
        else:
            if actual[i] > threshold:
                matrix["fn"] += 1.0
            else:
                matrix["tn"] += 1.0
    return matrix


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = pd.read_csv(target_url, header=None, prefix="V")
# print(data.head())
n_cols = len(data.columns)
n_rows = len(data.index)

# 将数据的属性和标签分开，并将标签转换为数值型（M-1.0,R-0.0）
xlist = numpy.array(data.iloc[:, 0:(n_cols - 1)])
labels = numpy.array(data.iloc[:, (n_cols - 1)])


for i in range(n_rows):
    if labels[i] == "M":
        labels[i] = 1.0
    else:
        labels[i] = 0.0
# print(labels)

# 将数据集分成2部分，1/3为测试集；2/3为训练集
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


# 模型训练
train_model = linear_model.LinearRegression()
train_model.fit(x_train, y_train)


# 获得混淆矩阵confusion matrix
training_predictions = train_model.predict(x_train)
test_predictions = train_model.predict(x_test)
train_confusion_matrix = confusion_matrix(training_predictions, y_train, 0.5)
test_confusion_matrix = confusion_matrix(test_predictions, y_test, 0.5)


print(train_confusion_matrix, test_confusion_matrix)


# 绘制训练集上AOC曲线
fpr, tpr, threshholds = roc_curve(y_train, training_predictions)        # 计算真正率、假正率
roc_auc = auc(fpr, tpr)         # AOC曲线下的面积


plot.plot(fpr, tpr, 'b-', label="ROC fold (area = %.2f)" % roc_auc)
plot.plot([0, 1], [0, 1], 'r--')
plot.xlabel("False Positive Rate")
plot.ylabel("True Positive Rate")
plot.axis([0.0, 1.0, 0.0, 1.0])
plot.title("In sample ROC rocks versus mines")
plot.legend(loc="lower right")
plot.show()


# 绘制测试集上AOC曲线

fpr, tpr, threshholds = roc_curve(y_test, test_predictions)        # 计算真正率、假正率
roc_auc = auc(fpr, tpr)         # AOC曲线下的面积


plot.plot(fpr, tpr, 'b-', label="ROC fold (area = %.2f)" % roc_auc)
plot.plot([0, 1], [0, 1], 'r--')
plot.xlabel("False Positive Rate")
plot.ylabel("True Positive Rate")
plot.axis([0.0, 1.0, 0.0, 1.0])
plot.title("Out-of-sample ROC rocks versus mines")
plot.legend(loc="lower right")
plot.show()
