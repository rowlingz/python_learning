# -*- coding: utf-8 -*-

import pandas as pd


filename = './data/air_data.csv'

# 获取原始数据
air_data = pd.read_csv(filename, encoding='utf-8')
explore = air_data.describe(percentiles=[], include='all').T


# 获取缺失值
explore['null'] = len(air_data) - explore['count']

# print(air_data.head())
print(explore['null'])
