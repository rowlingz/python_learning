# -*- coding:utf-8 -*-


import pandas as pd
import numpy as np
from scipy import stats


def fileter_data(data):

    data = data[data['see_time'] <= 2000]

    new_data = data[data['link'].notnull()]
    unique_data = new_data.drop_duplicates()

    return unique_data


# df = pd.read_csv('qijia_detail.csv', encoding='GBK', index_col='id')
# # print(df)
# new_df = fileter_data(df)
# new_df.to_csv('./analysisdata/qijia_filter.csv', encoding='GBK', index=False )
#

new_df = pd.read_csv('./analysisdata/fang_filter.csv', encoding='utf-8')
print(new_df['num'].describe())


# mode = stats.mode(new_df['see_time'])
# mode_count = stats.mode(new_df['see_time'])[1]
# print(mode)
# print(mode_count)