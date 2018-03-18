# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})

df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})


df3 = pd.DataFrame({'key1': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})

df4 = pd.DataFrame({'key2': ['a', 'b', 'd'],
                    'data2': range(3)})

# 数据集的合并 merge
# 默认内连接inner  显示交集, on指定连接的列
df = pd.merge(df1, df2, on='key')

# 两个对象名不同时，分别指明要连接的列
df = pd.merge(df3, df4, left_on='key1', right_on='key2')

# how指定连接方式： inner(默认)，outer（并集），left, right
df_outer = pd.merge(df1, df2, how='outer')

df_left = pd.merge(df1, df2, how='left')

df_right = pd.merge(df1, df2, how='right')

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'val_l': [1, 2, 3]})

right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one',  'one',  'one', 'two'],
                      'val_r': [4, 5, 6, 7]})

df_merge = pd.merge(left, right, on=['key1', 'key2'], how='outer')

# suffixes参数指定附加在左右两个dataframe对象的重叠列名上的字符串
df_merge1 = pd.merge(left, right, on='key1', how='outer', suffixes=('_left', '_right'))


# 笛卡尔积
# from itertools import product
#
# for x, y, z in product(['a', 'b', 'c'], [1, 2, 3], ['m', 'n']):
#     print(x, y, z)


# 索引上的合并  以索引为连接键
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})

df2 = pd.DataFrame({'data2': range(2)}, index=['a', 'b'])

# right_index,left_index为True时，表明以此索引为连接键，
df_merge_index = pd.merge(df1, df2, left_on='key', right_index=True, how='outer')

# 轴向连接
# numpy,  contatenation
arr = np.arange(12).reshape((3, 4))
arr_contact = np.concatenate([arr, arr], axis=0)


# pandas, concat
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

# 默认join='outer'
s4 = pd.concat([s1*5, s3])
s5 = pd.concat([s1, s4], axis=1, join_axes=[['a', 'b', 'c', 'e']])
# keys层次化索引
s6 = pd.concat([s1, s4], keys=['aa', 'bb'], join='inner', axis=1)


# 合并重叠数据
# numpy , where
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a)),
              index=['f', 'e', 'd', 'c', 'b', 'a'])

a_b = np.where(pd.isnull(a), b, a)

# series, dataframe , combine_first
a_b1 = a.combine_first(b)       # 等价于np.where(pd.isnull(a), b, a)

df1 = pd.DataFrame({'a': [1, np.nan, 5, np.nan],
                    'b': [np.nan, 2, np.nan, 6],
                    'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5, 4, np.nan, 3, 7],
                    'b': [np.nan, 3, 4, 6, 8]})

df1_df2 = df1.combine_first(df2)  # 用df2填充df1空位


# 删除重复项  drop_duplicates
data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                     'k2': [1, 1, 2, 3, 3, 4, 4]})

data_repet_bool = data.duplicated()
data_repet_drop = data.drop_duplicates(['k1'])



if __name__ == '__main__':
    # print(df1)
    # print("++++++++++++++")
    # print(df2)
    # print("++++++++++++++")
    # print(df_merge_index)
    print(data)
    print("++++++++++++++")
    print(data_repet_bool)
    print(data_repet_drop)