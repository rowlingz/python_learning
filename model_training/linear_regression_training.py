# 数据第一行涵盖属性名，数值间用“；”分开，最后一列为标签

import pandas as pd
import numpy
from sklearn import linear_model
import matplotlib.pyplot as plt


def get_data(file_name):
    """获取数据，返回x,y(datafames格式)"""
    data = pd.read_csv(file_name, sep=';')
    n_cols = len(data.columns)
    x_lists = data.iloc[:, 0:(n_cols - 1)]
    y_labels = data.iloc[:, (n_cols - 1)]

    return x_lists, y_labels


def divide_test_and_train(list):
    """将数据集分为2部分"""
    n_rows = len(list.index)
    train, test = [], []
    for i in range(n_rows):
        if i % 3 == 0:
            test.append(list.iloc[i, :])
        else:
            train.append(list.iloc[i, :])

    return train, test


def linear_model_main(x_parameters, y_parameters):
    model = linear_model.LinearRegression()
    x_train, x_test = divide_test_and_train(x_parameters)
    y_train, y_test = divide_test_and_train(y_parameters)
    x_taining = numpy.array(x_train)
    x_testing = numpy.array(x_test)
    y_training = numpy.array(y_train)
    y_testing = numpy.array(y_test)

    model.fit(x_taining, y_training)
    predictions = {}
    predictions['intercept'] = model.intercept_
    predictions['coefficient'] = model.coef_
    predictions['predicted_value'] = model.predict(x_testing)

    return predictions


def show_liner_line(x_parameters, y_parameters):
    model = linear_model.LinearRegression()
    x_train = numpy.array(x_parameters)
    y_train = numpy.array(y_parameters)
    model.fit(x_train, y_train)
    plt.scatter(x_train, y_train, 'b')
    plt.plot(x_train, model.predict(x_train), 'c')
    plt.show()





target_url = "C:\Users\zhouning75\Desktop\12.CSV"
x, y = get_data(target_url)
print(linear_model_main(x, y))
show_liner_line(x, y)

