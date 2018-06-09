# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


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


def split_data(data):
    train_data, test_data = train_test_split(data)
    return train_data, test_data


def logit_model(data):
    num_feature = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin']
    alg = LogisticRegression(random_state=1)
    scores = cross_val_score(alg, data[num_feature], data['Survived'], cv=3)
    print(scores.mean())


def random_forest(data):
    predictors = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin']

    alg = RandomForestClassifier(random_state=1, n_estimators=50, min_samples_split=4, min_samples_leaf=2)

    scores = cross_val_score(alg, data[predictors], data['Survived'], cv=3)
    print(scores.mean())


if __name__ == "__main__":
    df = pd.read_csv('train.csv')
    data = set_missing_age(df)
    data_not_null = missing_data_deal(data)
    logit_model(data_not_null)
    random_forest(data_not_null)
    print('end')