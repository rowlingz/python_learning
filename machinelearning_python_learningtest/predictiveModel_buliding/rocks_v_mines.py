# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt


def get_data(target_url):
    """获取数据"""
    data = pd.read_csv(target_url, header=None, prefix="V")

    # 将数据的属性和标签分开，并将标签转换为数值型（M-1.0,R-0.0）
    data[data['V60'] == 'R'] = 0
    data[data['V60'] == 'M'] = 1

    return data


def split_data(data):
    """拆分成训练集和测试集"""
    n_col = len(data.index)
    train_index = [i for i in range(n_col) if i % 3 == 0]
    test_index = [i for i in range(n_col) if i % 3 != 0]
    train_data = data.ix[train_index]
    test_data = data.ix[test_index]
    # train_data, test_data = train_test_split(data, test_size=0.2)
    return train_data, test_data


def model_fit(train_data):
    """训练模型"""
    n_col = len(train_data.columns)

    model = LinearRegression()
    model.fit(train_data.iloc[:, :(n_col-1)], train_data['V60'])

    return model


def model_predict(model, test_data):
    """模型预测"""
    n_col = len(test_data.columns)

    test_data['prob'] = model.predict(test_data.iloc[:, :(n_col-1)])

    test_data['predict'] = test_data['prob'].apply(lambda x: 1 if x > 0.5 else 0)

    conf_mat = confusion_matrix(test_data['V60'], test_data['predict'], labels=[0, 1])

    tn, fp, fn, tp = conf_mat.ravel()
    print(tn, fp, fn, tp)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)
    print("查准率： %.3f ; 查全率： %.3f ; f1: %.3f" % (precision, recall, f1))

    fpr, tpr, thresholds = roc_curve(test_data['V60'], test_data['prob'])
    roc_aoc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label="ROC curve (area = %.2f)" % roc_aoc)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.title('ROC curve')
    plt.show()


def run(target_url):
    data = get_data(target_url)
    train_data, test_data = split_data(data)

    model = model_fit(train_data)

    model_predict(model, test_data)


if __name__ == "__main__":
    target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
                  "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
    run(target_url)
    print('end')
