# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def get_data(filename):

    data = pd.read_excel(filename)
    print(data.head())

    return data


def split_data(data):
    x = data[['AT', 'V', 'AP', 'RH']]
    y = data['PE']

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

    return x_train, x_test, y_train, y_test


def model_fit(x_train, y_train):
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    return lr


def model_predict(lr, x_test, y_test):

    print(lr.coef_, lr.intercept_)

    y_predict = lr.predict(x_test)

    mse = mean_squared_error(y_test, y_predict)
    print("mse: %.3f" % mse)

    plt.scatter(y_test, y_predict)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
    plt.xlabel('Measured')
    plt.ylabel('Predict')
    plt.show()


def run():
    data = get_data("Folds5x2_pp.xlsx")
    x_train, x_test, y_train, y_test = split_data(data)

    model_lr = model_fit(x_train, y_train)

    model_predict(model_lr, x_test, y_test)
    print('end')


if __name__ == "__main__":
    run()
