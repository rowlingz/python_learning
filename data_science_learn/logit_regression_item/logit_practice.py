# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

num_cols = ['age', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']


def translabel(data, label):
    """类别型变量转化为数值型变量"""
    data[label] = pd.Categorical(data[label]).codes
    return data


def visual_data(data):
    """数值型变量 直方图 分布情况 df.hist()"""
    data[['age', 'education_num', 'hours_per_week', 'label']].hist(
        rwidth=0.9, grid=False, figsize=(8, 8), alpha=0.6, color="grey"
    )
    plt.savefig('num_data_visual.png')
    plt.show()


def cross_hours_per_week(data):
    """hours_per_week, label 交叉报表"""
    factor = pd.cut(data.hours_per_week, 5)
    cross = pd.crosstab(factor, data['label'])
    print(cross.dtypes)
    cross_norm = cross.div(cross.sum(axis=1), axis=0)

    # 采用 df.plot进行图表展示
    cross_norm.plot(kind='bar', stacked=True, rot=0)
    plt.show()


def cross_edu_num(data):
    """education_num, label 交叉报表"""
    cross_edu = pd.crosstab(pd.qcut(data['education_num'],
                                    [0, 0.25, 0.5, 0.75, 1]), data['label'])
    print(cross_edu)

    # 采用mosaic 进行交叉报表图形化
    mosaic(cross_edu.stack())
    plt.show()


def logit_regression(data):
    train_data, test_data = train_test_split(data, test_size=0.2)

    re = train_model(train_data)
    model_examine(re)
    # test_data = make_prediction(re, test_data)
    # print(test_data)


def train_model(data):
    # 依据 公式 进行模型训练
    formula = "label ~ age + education_num + capital_gain + capital_loss + hours_per_week"
    model = sm.Logit.from_formula(formula, data=data)
    re = model.fit()

    # model1 = sm.Logit(data['label'], data[['age', 'education_num', 'capital_loss', 'capital_gain', 'hours_per_week']])
    # re = model1.fit()
    return re


def model_examine(re):

    # 整体统计分析结果
    print(re.summary2())

    # f_test函数进行假设检验
    print("检验假设education_num 系数等于0")
    print(re.f_test("education_num=0"))

    print("检验education_num的系数等于0，32和hours_per_week的系数等于0.04同时成立")
    print(re.f_test("education_num=0.32, hours_per_week=0.04"))


def interpret_model(re):
    conf = re.conf_int()
    conf['OR'] = re.params

    conf.columns = ['2.5%', '97.5%', 'OR']

    print("各个变量对事件发生比的影响")
    print(np.exp(conf))

    print("各个变量的边界效应")
    print(re.get_margeff(at="overall").summary())


def make_prediction(re, test_data, alpha=0.5):
    test_data['prob'] = re.predict(test_data.ix[:, :-1])

    print("事件发生概率（预测概率）大于0.6的数据个数：")
    print(test_data.loc[test_data['prob'] > 0.6, :].shape[0])

    print("事件发生概率（预测概率）大于0.5的数据个数：")
    print(test_data.ix[test_data.prob > 0.5, :].shape[0])

    test_data['predict'] = test_data['prob'].apply(lambda x: 1 if x > alpha else 0)
    return test_data


def evaluation(test_predict):
    """计算precision recall, f1"""
    y = test_predict['label']
    y_predict = test_predict['predict']
    from sklearn.metrics import confusion_matrix, roc_curve, auc
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
    plt.show()


if __name__ == "__main__":
    filename = "./data/adult.data"

    origin_data = pd.read_csv(filename,
                              usecols=['age', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week', 'label'])
    orgin_data_num = translabel(origin_data, 'label')
    # data_info = orgin_data_num.info()
    # data_describe = orgin_data_num.describe()
    # # data_info.to_csv('data_info.csv')
    # data_describe.to_csv('data_info.csv')
    # visual_data(orgin_data_num)
    # print('end')

    # print(cross_norm)
    train_data, test_data = train_test_split(orgin_data_num, test_size=0.2)

    re = train_model(train_data)
    test_predict = make_prediction(re, test_data)
    evaluation(test_predict)
    # interpret_model(re)

    print('end')