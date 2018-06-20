# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LassoCV
import matplotlib.pyplot as plt
from sklearn import linear_model


target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(target_url, header=0, sep=";")
x_list = np.array(data.iloc[:, :-1])
y_label = np.array(data.iloc[:, -1])

x_scaled = preprocessing.scale(x_list)
y_scaled = preprocessing.scale(y_label)


def lasso_model_cv(x, y):

    # 在红酒口感数据集上，使用交叉验证估计套索模型的样本外错误
    # LassoCV  得到的alpha_  === >获取损失函数中惩罚项lamda
    wine_model = LassoCV(cv=10).fit(x, y)

    # 绘制曲线
    plt.figure()
    plt.plot(wine_model.alphas_, wine_model.mse_path_, ':')
    plt.plot(wine_model.alphas_, wine_model.mse_path_.mean(axis=-1), label='Average MSE Across Folds', linewidth=2)
    plt.axvline(wine_model.alpha_, linestyle='--', label='CV Estimate of Best alpha')
    plt.semilogx()
    plt.legend()
    ax = plt.gca()
    ax.invert_xaxis()
    plt.xlabel('alpha')
    plt.ylabel('Mean Square Error')
    plt.axis('tight')
    plt.show()

    print("alpha value that minimizes CV Error", wine_model.alpha_)
    print("Minimum MSE", min(wine_model.mse_path_.mean(axis=-1)))
    # return wine_model.alphas, min(wine_model.mse_path_.mean(axis=-1))

    # lasso_path 在整个数据集上训练  进行特征选择
    alphas, coefs, _ = linear_model.lasso_path(x, y, return_models=False)
    plt.plot(alphas, coefs.T)

    plt.xlabel('alpha')
    plt.ylabel('Coefficients')
    plt.axis('tight')
    plt.semilogx()
    ax = plt.gca()
    ax.invert_xaxis()
    plt.show()

    nattr, nalpha = coefs.shape

    nz_list = []
    for i in range(1, nalpha):
        coefs_list = list(coefs[:, i])
        nz_coef = [i for i in range(nattr) if coefs_list[i] != 0]
        for q in nz_coef:
            if q not in nz_list:
                nz_list.append(q)

    names = data.columns[:-1]
    name_list = [names[nz_list[i]] for i in range(len(nz_list))]
    print('Attributes Ordered by How Early They Enter the Model', name_list)

    alpha_start = min(wine_model.mse_path_.mean(axis=-1))

    index_alpha_start = [index for index in range(100) if alphas[index] > alpha_start]
    index_start = max(index_alpha_start)

    coef_start = list(coefs[:, index_start])
    print('Best Coefficient Values', coef_start)


