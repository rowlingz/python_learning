# -*- coding:utf-8 -*-

# 对美国个人收入进行逻辑回归分析，主要分析数值型变量，对逻辑回归的流程进行熟悉

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.metrics import confusion_matrix, roc_curve, auc


# 获取数据
def read_data(filename):
    """读取数值型变量， 并将label转换为 数值型"""
    data = pd.read_csv(filename,
                       usecols=['age', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week', 'label'])
    # 将类别型变量 转换为 数值型变量
    data['label'] = pd.Categorical(data['label']).codes
    return data


# 数据可视化
def data_visual(data):
    """数据可视化"""
    data.hist(rwidth=0.9, grid=False, figsize=(8, 8), alpha=0.6, color="grey")
    plt.title("data_hist")
    plt.savefig('data_hist.png')
    plt.show()


def cross_data(data):
    """对hours_per_week, education_num进行交叉表展示"""
    # hours_per_week， label交叉表展示
    factor = pd.cut(data.hours_per_week, 5)
    cross = pd.crosstab(factor, data['label'])
    cross_norm = cross.div(cross.sum(axis=1), axis=0)
    cross_norm.plot(kind='bar', rot=0)
    plt.title("hours_per_week-label交叉表")
    plt.savefig('hours_per_week_cross.png')

    # education_num, label 交叉表展示
    cross_edu = pd.crosstab(pd.qcut(data['education_num'],
                                    [0, 0.25, 0.5, 0.75, 1]), data['label'])
    # 采用mosaic 进行交叉报表图形化
    mosaic(cross_edu.stack())
    plt.title("education_num-label 交叉表")
    plt.savefig('education_num_cross.png')
    plt.show()


# 数据分析
def split_data(data):
    """将数据分成测试集和训练集"""
    train_data, test_data = train_test_split(data, test_size=0.2)
    return train_data, test_data


def train_model(train_data):
    """利用训练集 训练模型"""
    formula = "label ~ age + education_num + capital_gain + capital_loss + hours_per_week"
    model = sm.Logit.from_formula(formula, data=train_data)
    re = model.fit()
    return re


def model_detail(re):
    """模型基本信息"""
    # 模型的变量的机会比
    conf = re.conf_int()
    conf['OR'] = re.params
    conf.columns = ['2.5%', '97.5%', 'OR']

    print("各个变量对事件发生比的影响")
    print(np.exp(conf))

    print("各个变量的边界效应")
    print(re.get_margeff(at="overall").summary())


def model_examine(re):
    """模型的统计性质"""

    # 整体统计分析结果
    print(re.summary2())

    # f_test函数进行假设检验
    print("检验假设education_num 系数等于0")
    print(re.f_test("education_num=0"))

    print("检验education_num的系数等于0，32和hours_per_week的系数等于0.04同时成立")
    print(re.f_test("education_num=0.32, hours_per_week=0.04"))


def make_prediction(re, test_data, alpha=0.5):
    """预测结果"""
    test_data['prob'] = re.predict(test_data.ix[:, :-1])

    print("事件发生概率（预测概率）大于0.6的数据个数：")
    print(test_data.loc[test_data['prob'] > 0.6, :].shape[0])

    print("事件发生概率（预测概率）大于0.5的数据个数：")
    print(test_data.ix[test_data.prob > 0.5, :].shape[0])

    test_data['predict'] = test_data['prob'].apply(lambda x: 1 if x > alpha else 0)
    return test_data


def evaluation_model(test_predict):
    """采用 precision, recall, ROC评价预测结果"""
    y = test_predict['label']
    y_predict = test_predict['predict']

    conf_mat = confusion_matrix(y, y_predict, labels=[0, 1])
    tn, fp, fn, tp = conf_mat.ravel()
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * precision * recall / (precision + recall)

    print(conf_mat)
    print(tn, fp, fn, tp)
    print("查准率： %.3f ; 查全率： %.3f ; f1 %.3f" % (precision, recall, f1))

    # 绘制ROC曲线，
    fpr, tpr, thresholds = roc_curve(y, test_predict['prob'])
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1])
    plt.axis([0.0, 1.0, 0.0, 1.0])
    plt.xlabel("False positive rate")
    plt.ylabel("True positive rate")
    plt.title("ROC lines")
    plt.legend(loc="lower right")
    plt.savefig('ROC曲线.png')
    plt.show()


def logit_regression_process(data):
    """模型基本流程"""
    # 数据集划分
    train_data, test_data = split_data(data)

    # 模型训练
    re = train_model(train_data)

    # 模型基本内容
    model_detail(re)
    model_examine(re)

    # 模型预测
    test_predict = make_prediction(re, test_data, alpha=0.5)

    # 预测值评价
    evaluation_model(test_predict)


if __name__ == "__main__":
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    filename = "./data/adult.data"
    data = read_data(filename)
    data_visual(data)
    cross_data(data)
    logit_regression_process(data)
    print('end')

