# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('data1.xlsx', usecols=[i for i in range(1, 13, 3)])


def get_boxplot(data):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure()
    p = data.boxplot(return_type='dict')        # 添加p的返回类型，避免报错
    x = p['fliers'][0].get_xdata()
    y = p['fliers'][0].get_ydata()
    y.sort()

    for i in range(len(x)):
        if i > 0:
            plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8/(y[i] - y[i-1], y[i])))
        else:
            plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

    plt.show()


def get_mean(data):
    data_mean = data.apply(lambda x: np.mean(x))
    data_mean = data_mean.to_frame('data_mean')
    return data_mean


if __name__ == '__main__':
    desc = data.describe()
    print(desc)
    means = get_mean(data)
    plt.plot(range(1, 5), means, 'o-')
    plt.show()