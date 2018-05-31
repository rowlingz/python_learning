# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def watch_data(train_df):
    # 初探数据
    print(train_df.columns)

    print("ttrain_df infor")
    # 查看数据的统计信息
    print(train_df.info())

    print("train_df describe")
    # 查看数值的统计信息
    print(train_df.describe())


def analysis_each_variable(train_df):
    # 各属性的人数分布
    plt.rcParams['font.sans-serif'] = ['FangSong']
    plt.rcParams['axes.unicode_minus'] = False

    plt.subplot(3, 2, 1)
    train_df['Survived'].value_counts().plot(kind='bar')
    plt.title(u'获救情况分布（1为获救）')
    plt.ylabel(u'人数')

    plt.subplot(3, 2, 2)
    train_df['Pclass'].value_counts().plot(kind='bar')
    plt.title(u'Ticket class 分布')
    plt.ylabel(u'人数')

    plt.subplot(3, 2, 3)
    plt.scatter(train_df.Age, train_df.Survived)
    plt.title(u'年龄分布情况')
    plt.xlabel('Age')

    plt.subplot(3, 2, 4)
    train_df['Embarked'].value_counts().plot(kind='bar')
    plt.title(u'Embarked 分布')
    plt.ylabel(u'人数')

    plt.subplot(3, 1, 3)
    train_df.Age[train_df.Pclass == 1].plot(kind='kde')
    train_df.Age[train_df.Pclass == 2].plot(kind='kde')
    train_df.Age[train_df.Pclass == 3].plot(kind='kde')
    plt.xlabel('Age')
    plt.ylabel(u'人数')
    plt.title(u'各等级下年龄分布')
    plt.legend(('1', '2', '3'), loc='best')

    plt.savefig('variable_distribute.png')
    plt.show()


def kind_show(df, label):
    data = df[label].value_counts()
    print(data)
    data.plot(kind='bar')
    for i in range(len(data)):
        plt.text(i, data[i], str(data[i]), ha='center', va='bottom')
    plt.title(u'%s 分布' % label)
    plt.ylabel(u'人数')


def kind_survived(data, label):
    """查看单一属性的获救情况 kind = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']"""

    df = data.groupby(['Survived', label]).count()['PassengerId'].unstack('Survived')
    # print(df)
    # return df
    df.plot(kind='bar', stacked=True, rot=0)
    # x = np.arange(len(data.index))
    # y = [data[i].values for i in range(len(data.columns))]
    # for i in range(len(y)):
    #     for a, b in zip(x, y[i]):
    #         plt.text(a, b, '%.f' % b, ha='center', va='top')
    plt.ylabel('number of people')
    plt.title('%s 获救情况分布' % label)
    plt.savefig('%s 获救情况.png' % label)
    plt.show()


def subtotal(data, kind):
    """汇总个属性下的获救情况"""
    subtotal = pd.concat([data.groupby(['Survived', kind[i]]).count()['PassengerId'].unstack('Survived')
                          for i in range(len(kind))], keys=kind)
    subtotal.to_csv('subtotal.csv')


def sex_survived(train_df):
    """不同性别的获救情况"""
    df = train_df.groupby(['Survived', 'Sex']).count()['PassengerId'].unstack('Survived')
    print(df)
    df.plot(kind='bar', stacked=True, rot=0)
    x = np.arange(len(df.index))
    y1, y2 = df[0].values, df[1].values
    for a, b, c in zip(x, y1, y2):
        plt.text(a, b - 1, '%.f' % b, ha='center', va='top')
        plt.text(a, b + c, '%.f' % c, ha='center', va='top')
    plt.ylabel('number of people')
    plt.show()


def missing_data_deal(data):
    """处理含缺失值的属性"""
    # Age， 缺失值数目105，采用
    data['Age'] = data['Age'].fillna(data['Age'].median())

    # Cabin 仅有204个有效值；将其设为有/无座位两类
    data.ix[data['Cabin'].notnull(), 'Cabin'] = 'Yes'
    data.ix[data['Cabin'].isnull(), 'Cabin'] = 'No'

    # Embarked 缺失数目 2
    data.ix[data['Embarked'].isnull(), 'Embarked'] = np.random.choice(['S', 'C', 'Q'])

    return data


def set_missing_age(data):
    """采用随机森林 填补 Age的缺失值"""
    age_df = data[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]
    know_age = age_df[age_df['Age'].notnull()].values
    unknow_age = age_df[age_df['Age'].isnull()].values

    y = know_age[:, 0]
    x = know_age[:, 1:]

    rft = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rft.fit(x, y)

    predict_age = rft.predict(unknow_age[:, 1:])

    data.ix[data['Age'].isnull(), 'Age'] = predict_age

    return data


def feature_factorization(data):
    """对类目型的特征因子化, 筛选出数值型属性"""
    kind = ['Pclass', 'Sex', 'Cabin', 'Embarked']
    factor_df = [pd.get_dummies(data[i], prefix=i) for i in kind]
    df = pd.concat([data] + factor_df, axis=1)
    df_drop = df.drop(['Pclass', 'Sex', 'Cabin', 'Embarked', 'Name', 'Ticket'], axis=1)

    return df_drop


def normalized_data(data):
    """大幅度数值型属性 归一化"""
    scale = StandardScaler()
    data['Age_scaled'] = scale.fit_transform(data['Age'].values.reshape(-1, 1))
    data['Fare_scaled'] = scale.fit_transform(data['Fare'].values.reshape(-1, 1))
    result = data.drop(['Age', 'Fare'], axis=1)

    return result


def model_fit(data):
    data_value = data.values
    y = data_value[:, 0]
    x = data_value[:, 1:]

    LR = LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
    LR.fit(x, y)
    return LR


if __name__ == '__main__':
    # train_df = pd.read_csv('train.csv', encoding='utf-8')

    # test_df = pd.read_csv('test.csv')
    # test_df['Fare'] = test_df['Fare'].fillna(test_df['Age'].median())
    # print(test_df.info())

    # watch_data(train_df)
    # kind = ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
    # plt.rcParams['font.sans-serif'] = ['FangSong']
    # plt.rcParams['axes.unicode_minus'] = False
    # for i in range(len(kind)):
    #     kind_survived(train_df, kind[i])
    # train_df[train_df['Age'].isnull()].Cabin = 1

    # # 获取数值型数据，初步预处理
    # data = missing_data_deal(train_df)
    # data_factor = feature_factorization(data)
    # data_factor.to_csv('get_all_num_variable_test.csv', index=False)
    # print(data_factor.head())
    # print(data_factor.info())
    #
    # # 'Age', 'Fare'属性值归一化
    # data = pd.read_csv('get_all_num_variable_test.csv')
    # data_normal = normalized_data(data)
    # data_normal.to_csv('normalized_data_test.csv', index=False)
    # print(data_normal)

    train_data = pd.read_csv('normalized_data.csv', index_col='PassengerId')
    test_data = pd.read_csv('normalized_data_test.csv', index_col='PassengerId')
    # print(test_data)
    model = model_fit(train_data)

    predict = model.predict(test_data)

    result = pd.DataFrame({'PassengerId': test_data.index, 'Survived': predict})

    result.to_csv('predict_data.csv', index=False)
    print('end')

