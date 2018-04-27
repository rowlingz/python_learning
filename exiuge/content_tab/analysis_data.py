# -*- coding:utf-8 -*-

import pymysql
import pandas as pd
import numpy as np
from scipy import stats


def get_data_from_mysql(table):
    """从mySQL中获取数据"""
    coon = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="exiuge",
        port=3306,
        charset="utf8")
    sql_select = "SELECT * FROM " + table
    data = pd.read_sql(sql_select, coon)
    data.to_csv('%s _detail.csv' % table, encoding='utf-8', index=False)
    print(data)
    return data


def filter_data(input_filename, output_filename):
    """筛选掉标签为null， url重复的值"""
    data = pd.read_csv(input_filename, encoding='utf-8', index_col='id')
    notnull_data = data[data['wordsbox'].notnull()]
    print(len(notnull_data))

    unique_data = notnull_data.drop_duplicates()
    unique_data = unique_data[unique_data['num'] <= 10000]

    print(len(unique_data))

    unique_data.to_csv(output_filename, encoding='utf-8')
    print('end')


def label_counts(data):
    labels = []
    labels_dir = {}
    for wordsbox in data['wordsbox']:
        for label in wordsbox.split(';'):
            if label not in labels:
                labels.append(label)
                labels_dir[label] = 1
            else:
                labels_dir[label] += 1

    df = pd.DataFrame({'counts': [j for j in labels_dir.values()], 'labels': [i for i in labels_dir.keys()]})

    return df


input_name = 'fang_1 _detail.csv'
output_name = './analysisdata/fang_filter1.csv'

# filter_data(input_name, output_name)


data = pd.read_csv(output_name, encoding='utf-8', index_col='id')
# print(data['num'].describe())
# new_df = data['num']
# mode = stats.mode(new_df)
# mode_count = stats.mode(new_df)[1]
# print(mode)
# print(mode_count)


# df = label_counts(data)
# df.to_csv('./analysisdata/labels_counts1.csv', encoding='utf-8')

sort_data = data.sort_values(by=['num'], ascending=False)
top10_len = int(0.08 * len(sort_data))
top10_data = sort_data.iloc[:top10_len, :]

top10_count = label_counts(top10_data)
top10_count.to_csv('./analysisdata/top10_count2.csv', encoding='utf-8')
print('end')

