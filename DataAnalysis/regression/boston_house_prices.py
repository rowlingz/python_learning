# -*- coding:utf-8 -*-
from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.metrics import mean_squared_error


# 获取数据
boston = load_boston()
# # .DESCR  describle描述性内容
# print(boston.DESCR)
#
# # .data   数据
# print(boston.data)

# 数据分割
x = boston.data
y = boston.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)


# 标准化处理
std_x, std_y = StandardScaler(), StandardScaler()
x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)


# 要保证x,y 具有相同的维度
y_train = std_y.fit_transform(y_train.reshape(-1, 1))
y_test = std_y.transform(y_test.reshape(-1, 1))


# 模型-线性回归 预测
lr = LinearRegression()
lr.fit(x_train, y_train)
lr_y_predict = lr.predict(x_test)
lr_y_predict = std_y.inverse_transform(lr_y_predict)


# 梯度下降 预测
sgdr = SGDRegressor()
sgdr.fit(x_train, y_train)
sgdr_y_predic = sgdr.predict(x_test)
sgdr_y_predic = std_y.inverse_transform(sgdr_y_predic)


# 岭回归
rd = Ridge(alpha=0.01)
rd.fit(x_train, y_train)
rd_y_predic = rd.predict(x_test)
rd_y_predic = std_y.inverse_transform(rd_y_predic)


# 模型评价
print("lr 均方误差： ", mean_squared_error(std_y.inverse_transform(y_test), lr_y_predict))
print("SGD 均方误差: ", mean_squared_error(std_y.inverse_transform(y_test), sgdr_y_predic))
print("Ridge 均方误差： ", mean_squared_error(std_y.inverse_transform(y_test), rd_y_predic))

# 使用模型自带的评分函数score获得模型在测试集上的准确性结果
print("Accuracy of LR Classifier:", lr.score(x_test, y_test))
print('Accuarcy of SGD Classifier:', sgdr.score(x_test, y_test))
