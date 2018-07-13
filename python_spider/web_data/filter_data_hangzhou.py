# -*- coding:utf-8 -*-
import pandas as pd
import re
import numpy as np


def recombin_data(filename1, filename2):
    """将两个文件的数据合并， 去重，索引重排，并进行简单的处理"""
    df1 = pd.read_csv(filename1, header=None)
    df2 = pd.read_csv(filename2, header=None)
    df = pd.concat([df1, df2], ignore_index=True)
    df.columns = ['title', 'title_url', 'icon_tag', 'icon_zt', 'message_list', 'community_name', 'community_address',
                  'tags', 'price_det', 'price_unit']

    data = df.drop_duplicates()
    data_ = data.loc[data['community_name'].notnull()]
    data_set = data_[['message_list', 'community_name', 'community_address', 'tags', 'price_det', 'price_unit']]
    data_set.reindex(range(len(data_set)))
    data_set['message_list'] = data_set['message_list'].apply(lambda x: x.strip('[').strip(']'))
    data_set['tags'] = data_set['tags'].apply(lambda x: x.strip('[').strip(']'))
    return data_set


def split_info(data_set):
    """将复合的信息列分开"""
    # 房型信息分列
    data_set['house_type'] = data_set['message_list'].apply(lambda x: x.split(',')[0])
    data_set['area'] = data_set['message_list'].apply(lambda x: x.split(',')[1])
    data_set['floor'] = data_set['message_list'].apply(lambda x: x.split(',')[2])
    data_set['year'] = data_set['message_list'].apply(lambda x: x.split(',')[3])

    # 地址信息
    data_set['region'] = data_set['community_address'].apply(lambda x: str(x).split('-')[0])
    data_set['sub_region'] = data_set['community_address'].apply(lambda x: str(x).split('-')[1])
    data_set['stree'] = data_set['community_address'].apply(lambda x: str(x).split('-')[2])

    # 对数值类属性转化为数值型变量
    num_col = ['price_det', 'price_unit', 'area', 'year']
    for col in num_col:
        data_set[col] = data_set[col].apply(lambda x: re.findall('\d+', x.strip())[0])

    # 楼层信息
    data_set['floor'] = data_set['floor'].apply(lambda x: x.strip().strip("'"))
    data_set['floor_heigh'] = data_set['floor'].apply(lambda x: x[:2] if len(x) > 4 else None)
    data_set['floor_num'] = data_set['floor'].apply(lambda x: re.findall('\d+', x)[0])

    # 删除分解过的原始项
    data_set_ = data_set.drop(['message_list', 'community_address', 'floor'], axis=1)

    # 更改数值变量为数值类型
    num_cols = ['price_det', 'price_unit', 'area', 'year', 'floor_num']
    data_set[num_cols] = data_set[num_cols].apply(pd.to_numeric, errors='coerce', downcast='float')

    data_set_.to_csv('filter_hangzhou_info.csv', index=False, encoding='utf_8_sig')


if __name__ == '__main__':
    filename1 = 'hangzhou_info_.csv'
    filename2 = 'hangzhou_info_2.csv'
    data_set = recombin_data(filename1, filename2)
    split_info(data_set)
    print('end')
