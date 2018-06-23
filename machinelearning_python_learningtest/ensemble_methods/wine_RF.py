# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(target_url, header=0, sep=";")
x_list = np.array(data.iloc[:, :-1])
y_label = np.array(data.iloc[:, -1])

wine_names = data.columns

x_train, x_test, y_train, y_test = train_test_split(x_list, y_label, test_size=0.3, random_state=531)


def random_forest_regressor(x_train, x_test, y_train, y_test):
    """随机森林构建回归模型"""
    # 不同决策树数目的影响
    mse_oss = []
    n_tree = range(50, 500, 10)
    for i_tree in n_tree:
        wine_rf_model = ensemble.RandomForestRegressor(n_estimators=i_tree, max_depth=None, max_features=4,
                                                       oob_score=False, random_state=531)

        wine_rf_model.fit(x_train, y_train)
        predict = wine_rf_model.predict(x_test)
        mse_oss.append(mean_squared_error(y_test, predict))

    print('MSE', mse_oss[-1])

    plt.plot(n_tree, mse_oss)
    plt.xlabel('Number of Trees in Ensemble')
    plt.ylabel('Mean Squared Error')
    plt.show()

    # 获取属性对预测结果得贡献
    feature_importance = wine_rf_model.feature_importances_
    feature_importance = feature_importance / feature_importance.max()
    sort_idx = np.argsort(feature_importance)
    bar_pos = np.arange(sort_idx.shape[0]) + 0.5
    plt.barh(bar_pos, feature_importance[sort_idx])
    plt.yticks(bar_pos, wine_names[sort_idx])
    plt.xlabel('Variable Importanc')
    plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.1)
    plt.show()


def gradient_boosting_regressor(x_train, x_test, y_train, y_test):
    """梯度提升构建回归模型"""
    n_est = 2000
    depth = 7
    learn_rate = 0.01
    sub_sample = 0.5
    wine_gb_model = ensemble.GradientBoostingRegressor(n_estimators=n_est,
                                                       max_depth=depth,
                                                       learning_rate=learn_rate,
                                                       subsample=sub_sample,
                                                       loss='ls')

    wine_gb_model.fit(x_train, y_train)

    mse_error = []
    predict = wine_gb_model.staged_predict(x_test)
    for p in predict:
        mse_error.append(mean_squared_error(y_test, p))

    print('MSE', min(mse_error))
    print(mse_error.index(min(mse_error)))

    plt.figure()
    plt.plot(range(1, n_est + 1), wine_gb_model.train_score_, label='Training Set MSE')
    plt.plot(range(1, n_est + 1), mse_error, label='Test Set Error')
    plt.legend(loc='upper right')
    plt.xlabel('Number of Trees in Ensemble')
    plt.ylabel('Mean Squared Error')
    plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.1)
    plt.show()

    feature_importance = wine_gb_model.feature_importances_
    feature_importance = feature_importance / feature_importance.max()
    sort_idx = np.argsort(feature_importance)
    bar_pos = np.arange(sort_idx.shape[0]) + 0.5
    plt.barh(bar_pos, feature_importance[sort_idx])
    plt.yticks(bar_pos, wine_names[sort_idx])
    plt.xlabel('Variable Importanc')
    plt.show()
