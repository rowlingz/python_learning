# -*- coding:utf-8 -*-
import pandas as pd

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
                      'key2': ['one',  'one',  'one', 'two',],
                      'val_r': [4, 5, 6, 7]})

df_merge = pd.merge(left, right, on=['key1', 'key2'], how='outer')


if __name__ == '__main__':
    print(left)
    print("++++++++++++++")
    print(right)
    print("++++++++++++++")
    print(df_merge)
