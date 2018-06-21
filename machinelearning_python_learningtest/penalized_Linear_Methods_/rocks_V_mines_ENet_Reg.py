# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import enet_path
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score, roc_curve

# 获取数据
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
              "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = pd.read_csv(target_url, header=None, prefix='V')

# 类别性变量转换为数值型
data.ix[data.ix[:, 'V60'] == 'R', 'V60'] = 0
data.ix[data.ix[:, 'V60'] == 'M', 'V60'] = 1


# 拆分为x, y 并对其标准化
x_list = np.array(data.iloc[:, :-1])
y_label = np.array(data.iloc[:, -1])

x_scaled = preprocessing.scale(x_list)
y_scaled = preprocessing.scale(y_label)

# 交叉验证
n_rows = len(x_list)
n_val = 10
for i_val in range(n_val):
    i_test = [a for a in range(n_rows) if (a % n_val == i_val % n_val)]
    i_train = [a for a in range(n_rows) if (a % n_val != i_val % n_val)]

    x_test = np.array([x_scaled[r] for r in i_test])
    x_train = np.array([x_scaled[r] for r in i_train])

    y_test = np.array([y_scaled[r] for r in i_test])
    y_train = np.array([y_scaled[r] for r in i_train])

    # 利用enet_path 进行训练，获取每组模型的 alpha 及 beta
    alphas, coefs, _ = enet_path(x_train, y_train, l1_ratio=0.8, fit_intercept=False)

    # 利用模型得到的参数，在测试集上采用点乘得到预测值， 从而得到 组合的测试y --y_out;及对应的预测y --pred
    if i_val == 0:
        pred = np.dot(x_test, coefs)
        y_out = y_test
    else:
        y_temp = np.array(y_out)
        y_out = np.concatenate((y_temp, y_test), axis=0)

        pre_temp = np.array(pred)
        pred = np.concatenate((pre_temp, np.dot(x_test, coefs)), axis=0)


# calculate misclassification error
mis_class_rate = []
_, n_pred = pred.shape
for i_pred in range(1, n_pred):
    pred_list = list(pred[:, i_pred])
    err_cnt = 0.0
    for i_row in range(n_rows):
        if (pred_list[i_row] < 0.0) and (y_out[i_row] >= 0.0):
            err_cnt += 1.0
        elif (pred_list[i_row] >= 0.0) and (y_out[i_row] < 0.0):
            err_cnt += 1.0
    mis_class_rate.append(err_cnt / n_rows)

min_error = min(mis_class_rate)
idx_min = mis_class_rate.index(min_error)

plot_alphas = list(alphas[1: len(alphas)])

plt.figure()
plt.plot(plot_alphas, mis_class_rate, label='Misclassification Error Across Folds', linewidth=2)
plt.axvline(plot_alphas[idx_min], linestyle='--', label='CV Estimate of Best alpha')
plt.legend()
plt.semilogx()
ax = plt.gca()
ax.invert_xaxis()
plt.xlabel('alpha')
plt.ylabel('Misclassification Error')
plt.axis('tight')
plt.show()


# calculate AUC
idx_pos = [i for i in range(n_rows) if y_out[i] > 0]
y_out_bin = [0] * n_rows
for i in idx_pos:
    y_out_bin[i] = 1

auc = []
for i_pred in range(1, n_pred):
    pred_list = list(pred[:, i_pred])
    auc_calc = roc_auc_score(y_out_bin, pred_list)
    auc.append(auc_calc)

max_auc = max(auc)
idx_max = auc.index(max_auc)

plt.figure()
plt.plot(plot_alphas, auc, label='AUC Across Folds', linewidth=2)
plt.axvline(plot_alphas[idx_max], linestyle='--', label='CV Estimate of Best alpha')
plt.legend()
plt.semilogx()
ax = plt.gca()
ax.invert_xaxis()
plt.xlabel('alpha')
plt.ylabel('Area Under the ROC Curve')
plt.axis('tight')
plt.show()


# plot best version of ROC curve
fpr, tpr, thresholds = roc_curve(y_out_bin, list(pred[:, idx_max]))
ct_class = [i * 0.01 for i in range(101)]
plt.plot(fpr, tpr, linewidth=2)
plt.plot(ct_class, ct_class, ':')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.show()

print('Best Value of Mis_classification Error = ', mis_class_rate[idx_min])
print("Best alpha for Mis_classification Error = ", plot_alphas[idx_min])

print('Best Vlaue for AUC = ', auc[idx_max])
print('Best alpha for AUC = ', plot_alphas[idx_max])


def coefficient_order(x_scaled, y_scaled):
    # 在整个数据集上训练，获取alphas, coefs
    alphas, coefs, _ = enet_path(x_scaled, y_scaled, l1_ratio=0.8, fit_intercept=False, return_models=False)
    plt.plot(alphas, coefs.T)
    plt.xlabel('alpha')
    plt.ylabel('coefficients')
    plt.axis('tight')
    plt.semilogx()
    ax = plt.gca()
    ax.invert_xaxis()
    plt.show()

    # find coefficient ordering 找到每一列中不为0的行
    n_attr, n_alpha = coefs.shape
    nz_list = []
    for i_alpha in range(1, n_alpha):
        coef_list = list(coefs[:, i_alpha])
        nz_coef = [i for i in range(n_attr) if coef_list[i] != 0]
        for q in nz_coef:
            if q not in nz_list:
                nz_list.append(q)

    names = ['V' + str(i) for i in range(n_rows)]
    name_list = [names[nz_list[i]] for i in range(len(nz_list))]
    print('Attributes Ordered by How Early They Enter the Model')
    print(name_list)

    # find coefficients corresponding to best alpha value（来源于交叉验证）
    alphaStar = 0.020334883589342503
    index_alphaStar = [index for index in range(100) if alphas[index] > alphaStar]
    index_star = max(index_alphaStar)

    coef_star = list(coefs[:, index_star])
    print('Best coefficient values', coef_star)

    print("")

    # The coefficients on normalized attributes give another slightly different ordering
    abs_coef = [abs(a) for a in coef_star]
    coef_sort = sorted(abs_coef, reverse=True)
    idx_coef_size = [abs_coef.index(a) for a in coef_sort if a != 0]
    name_list_2 = [names[idx_coef_size[i]] for i in range(len(idx_coef_size))]

    print("Attributes Ordered by Coef Size at Optimum alpha")
    print(name_list_2)