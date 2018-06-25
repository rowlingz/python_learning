# -*- coding:utf-8 -*-
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def tree_mse_different_depth(n_points, depth, n_val):
    """
    权衡二元决策树复杂度以获得最佳性能
    :param n_points: 模拟数据量 int
    :param depth: 最大二元决策树深度 int
    :param n_val: n折交叉  int
    :return: 不同决策树深度下 模型MSE分布
    """
    x_plot = [(float(i) / float(n_points) - 0.5) for i in range(n_points + 1)]

    x = [[s] for s in x_plot]

    np.random.seed(1)
    y = [(s + np.random.normal(scale=0.1)) for s in x_plot]

    n_row = len(x)

    depth_list = range(1, depth + 1)
    x_val_mse = []
    for i_depth in depth_list:
        error = []
        for i_val in range(n_val):
            idx_test = [a for a in range(n_row) if a % n_val == i_val % n_val]
            idx_train = [a for a in range(n_row) if a % n_val != i_val % n_val]

            x_test = [x[i] for i in idx_test]
            x_train = [x[i] for i in idx_train]

            y_test = [y[i] for i in idx_test]
            y_train = [y[i] for i in idx_train]

            tree_model = DecisionTreeRegressor(max_depth=i_depth)
            tree_model.fit(x_train, y_train)

            y_predict = tree_model.predict(x_test)
            error.append(mean_squared_error(y_test, y_predict))
        x_val_mse.append(sum(error) / n_val)

    plt.plot(depth_list, x_val_mse)
    plt.xlabel('depth')
    plt.ylabel('MSE')
    plt.show()
    min_index = x_val_mse.index(min(x_val_mse))
    print('最佳深度: ', depth_list[min_index])
    # return depth_list[min_index]


if __name__ == '__main__':
    n_points = 1000
    depth = 8
    n_val = 10
    tree_mse_different_depth(n_points, depth, n_val)
