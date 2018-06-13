# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(target_url, header=0, sep=";")
print(data.head())
print(data.info())


def split_data(data):
    """拆分成训练集和测试集"""
    n_col = len(data.index)
    train_index = [i for i in range(n_col) if i % 3 == 0]
    test_index = [i for i in range(n_col) if i % 3 != 0]
    train_data = data.ix[train_index]
    test_data = data.ix[test_index]
    # train_data, test_data = train_test_split(data, test_size=0.2)
    return train_data, test_data


def get_best_attributes(train_data, test_data):
    """前向逐步 删选特征 并进行特征排序"""
    att_index = range(len(train_data.columns) - 1)        # 属性列
    att_set = set(att_index)

    oss_error = []                              # 测试RSS
    best_att_index = []  # 最佳属性列

    for i in att_index:
        best_att_set = set(best_att_index)
        try_att_set = att_set - best_att_set

        try_att_index = list(try_att_set)

        error_list = []

        for try_att in try_att_index:
            test_index = best_att_index + [try_att]
            train_x = train_data.ix[:, test_index]
            test_x = test_data.ix[:, test_index]
            train_y = train_data.ix[:, -1]
            test_y = test_data.ix[:, -1]

            wine_model = LinearRegression()
            wine_model.fit(train_x, train_y)

            # test_data['prob'] = wine_model.predict(test_x)

            # rms_error = sum((test_y - test_data['prob']) ** 2) / len(test_y)
            rms_error = np.linalg.norm((test_y - wine_model.predict(test_x)), 2) / sqrt(len(test_y))

            error_list.append(rms_error)

        i_best = np.argmin(error_list)
        best_att_index.append(try_att_index[i_best])
        oss_error.append(error_list[i_best])

    # 获取RMSE与属性个数之间的关系
    print(oss_error)
    print(best_att_index)

    x = range(len(oss_error))
    plt.plot(x, oss_error, 'o-')
    plt.xlabel('Number of Attributes')
    plt.ylabel('Error (RMS)')
    plt.show()

    # 最小RMSE时 所选特征集合训练出的预测值与真实值的分布
    index_best = oss_error.index(min(oss_error))
    att_best = best_att_index[: (index_best + 1)]

    cols = data.columns
    best_cols = [cols[i] for i in att_best]

    train_x = train_data.ix[:, best_cols]
    test_x = test_data.ix[:, best_cols]
    train_y = train_data.ix[:, -1]
    test_y = test_data.ix[:, -1]

    wine_model = LinearRegression()
    wine_model.fit(train_x, train_y)

    plt.scatter(wine_model.predict(test_x), test_y, s=100, alpha=0.10)
    plt.xlabel('Predicted Taste Score')
    plt.ylabel('Actual Taste Score')
    plt.show()


if __name__ == "__main__":
    train_data, test_data = split_data(data)

    get_best_attributes(train_data, test_data)

    print('end')
