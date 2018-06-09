# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif
import matplotlib.pyplot as plt
import re


def set_missing_age(data):
    """采用随机森林 填补 Age的缺失值"""
    age_df = data[['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']]
    know_age = age_df[age_df['Age'].notnull()].values
    unknow_age = age_df[age_df['Age'].isnull()].values

    y = know_age[:, 0]
    x = know_age[:, 1:]

    rft = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rft.fit(x, y)

    predict_age = rft.predict(unknow_age[:, 1:])

    data.ix[data['Age'].isnull(), 'Age'] = predict_age

    return data


def missing_data_deal(data):
    """处理含缺失值的属性"""
    # # Age， 缺失值数目105，采用
    # data['Age'] = data['Age'].fillna(data['Age'].median())

    # Cabin 仅有204个有效值；将其设为有/无座位两类
    data.ix[data['Cabin'].notnull(), 'Cabin'] = 1
    data.ix[data['Cabin'].isnull(), 'Cabin'] = 0

    # Embarked 缺失数目 2
    data.ix[data['Embarked'].isnull(), 'Embarked'] = np.random.choice(['S', 'C', 'Q'])

    return data


def name_kind(name):
    title_search = re.search(r'([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ""


def name_feature(data):
    """依据名字 将其分为不同的类别"""
    title_mapping = {'Mr': 1,
                     'Miss': 2,
                     'Mrs': 3,
                     "Master": 4,
                     "Dr": 5,
                     "Rev": 6,
                     "Col": 7,
                     "Major": 7,
                     "Mlle": 8,
                     "Don": 9,
                     "Lady": 10,
                     "Mme": 8,
                     "Sir": 9,
                     "Jonkheer": 10,
                     "Countess": 10,
                     "Ms": 2,
                     "Capt": 7}
    data['name_title'] = data['Name'].apply(name_kind)
    data['name_num'] = data['name_title'].map(title_mapping)

    return data


def feature_factorization(data):
    """对类目型的特征因子化, 筛选出数值型属性"""
    kind = ['Pclass', 'Sex', 'Cabin', 'Embarked']
    factor_df = [pd.get_dummies(data[i], prefix=i) for i in kind]
    df = pd.concat([data] + factor_df, axis=1)
    # df_drop = df.drop(['Pclass', 'Sex', 'Cabin', 'Embarked', 'Name', 'Ticket'], axis=1)

    return df


def normalized_data(data):
    """大幅度数值型属性 归一化"""
    scale = StandardScaler()
    data['Age_scaled'] = scale.fit_transform(data['Age'].values.reshape(-1, 1))
    data['Fare_scaled'] = scale.fit_transform(data['Fare'].values.reshape(-1, 1))
    # result = data.drop(['Age', 'Fare'], axis=1)

    return data


def run(filename):
    """处理数据"""
    data = pd.read_csv(filename)
    data_miss = missing_data_deal(data)
    data_age = set_missing_age(data_miss)
    data_name_num = name_feature(data_age)
    data_factor = feature_factorization(data_name_num)
    data_norm = normalized_data(data_factor)

    return data_norm


def random_forest(x, y):
    """随机森林"""
    predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'name_num', 'Cabin']
    from sklearn.ensemble import RandomForestClassifier

    alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=4, min_samples_leaf=2)

    scores = cross_val_score(alg, x, y, cv=3)
    print(scores.mean())


def logit_model(x, y):
    """逻辑回归"""
    alg = LogisticRegression(random_state=1)
    scores = cross_val_score(alg, x, y, cv=3)
    print(scores.mean())


def feature_corr(x, y):
    """特征 相关性"""
    predictor = ["Pclass", "Sex", "SibSp", "Parch", "name_num", "Cabin", "Age", "Fare"]
    seletor = SelectKBest(f_classif, k=5)
    seletor.fit(x, y)

    scores = -np.log10(seletor.pvalues_)

    plt.bar(range(len(predictor)), scores)
    plt.xticks(range(len(predictor)), predictor, rotation=0)
    plt.show()

    pass


if __name__ == "__main__":
    # filename = "train.csv"
    # df = run(filename)
    # df.to_csv('normal_train_data.csv', index=False)

    data = pd.read_csv('normal_train_data.csv')
    data.ix[data['Sex'] == 'male', 'Sex'] = 1
    data.ix[data['Sex'] == 'female', 'Sex'] = 0

    predictor = ["Pclass", "Sex", "name_num", "Cabin", "Fare"]
    x = data[predictor]
    y = data["Survived"]
    random_forest(x, y)
    logit_model(x, y)

    name_factor = pd.get_dummies(data['name_num'], prefix='name')
    new_data = pd.concat([data, name_factor], axis=1)
    print(new_data.info())
    train_x = new_data.iloc[:, 13:]
    train_y = new_data['Survived']
    random_forest(train_x, train_y)

    logit_model(train_x, train_y)

    # print(data.head())
    # feature_corr(data[["Pclass", "Sex", "SibSp", "Parch", "name_num", "Cabin", "Age", "Fare"]],
    #              data['Survived'])
