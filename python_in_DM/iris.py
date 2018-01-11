# 每个样本都有四个特征（或者说变量），即花萼（sepal）和花瓣（petal）的长度和宽度。
from urllib import request
import numpy
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix, classification_report



target_url = "http://aima.cs.berkeley.edu/data/iris.csv"
data = request.urlopen(target_url)
file_name = 'iris.csv'
# with open(file_name, 'w') as file:
#     file.write(data.read().decode())

# 创建数据集
xlist = numpy.genfromtxt(file_name, delimiter=',', usecols=(0, 1, 2, 3))
labels = numpy.genfromtxt(file_name, delimiter=',', usecols=(4), dtype=str)
print(xlist[0])
print(xlist.shape)
print(labels.shape)

# 查看分类样本类型及名字
print(set(labels))


# 可视化两个特征值的--以第一维度和第三维度为例
plt.plot(xlist[labels == 'virginica', 0], xlist[labels == 'virginica', 2], 'ro')
plt.plot(xlist[labels == 'setosa', 0], xlist[labels == 'setosa', 2], 'bo')
plt.plot(xlist[labels == 'versicolor', 0], xlist[labels == 'versicolor', 2], 'go')
plt.xlabel('1th')
plt.ylabel('3th')
plt.show()


# 分特性绘制直方图
x_min = min(xlist[:, 0])
x_max = max(xlist[:, 0])
plt.figure()
plt.subplot(411)
plt.hist(xlist[labels == 'virginica', 0], color='r')
plt.xlim(x_min, x_max)
plt.subplot(412)
plt.hist(xlist[labels == 'setosa', 0], color='b')
plt.xlim(x_min, x_max)
plt.subplot(413)
plt.hist(xlist[labels == 'versicolor', 0], color='g')
plt.xlim(x_min, x_max)
plt.subplot(414)
plt.hist(xlist[:, 0], color='y')
plt.xlim(x_min, x_max)
plt.show()

# 分类器
# 将字符串数组转换为数值型数据
y = numpy.zeros(len(labels))
y[labels == 'setosa'] = 1
y[labels == 'versicolor'] = 2
y[labels == 'virginica'] = 3
classifier = GaussianNB()
x_train, x_test, y_train, y_test = cross_validation.train_test_split(xlist, y, test_size=0.4, random_state=0)
classifier.fit(x_train, y_train)
print(classifier.score(x_test, y_test))
print(confusion_matrix(classifier.predict(x_test), y_test))