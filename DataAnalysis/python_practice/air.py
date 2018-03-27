# -*- coding: utf-8 -*-

import pandas as pd


filename = './data/air_data.csv'
air_data = pd.read_csv(filename, encoding='utf-8')


def get_data(air_data):
    """获取数据，初步获得探索结果"""
    # 获取原始数据
    explore = air_data.describe(percentiles=[], include='all').T

    # 获取缺失值
    explore['null'] = len(air_data) - explore['count']

    # 抽取null max min 生成新的对象
    result = explore[['null', 'min', 'max']]
    # result.columns = ['null', 'min', 'max']

    # 将得到的探索结果result写入文件
    result.to_csv('./data/explore.csv', sep=',', header=True)

    print(result)


def data_cleaning(air_data):
    """数据清洗，滤除不合规则的数据"""
    # 舍去票价为空的行
    data = air_data[air_data['SUM_YR_1'].notnull() & air_data['SUM_YR_2'].notnull()]

    # 滤去票价为0， 平均折扣率不为0，总飞行公里数大于0的记录
    index1 = data['SUM_YR_1'] != 0
    index2 = data['SUM_YR_2'] != 0
    index3 = (data['avg_discount'] == 0) & (data['SEG_KM_SUM'] == 0)

    data = data[index1 | index2 | index3]

    data.to_csv('./data/clean_file.csv', sep=',')


if __name__ == '__main__':
    data_cleaning(air_data)