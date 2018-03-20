# -*- coding:utf-8 -*-
# 数据聚合和分组运算
import pandas as pd
import numpy as np


df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})


# groupby  分组键： series， 适当长度的数组， 列名
means = df['data1'].groupby(df['key1']).mean()              # series
means1 = df.groupby(['key1', 'key2']).mean()
means2 = df[['data1']].groupby((df['key1'])).mean()         # dataframe


# 对分组进行迭代   产生一组二元元祖
"""
for name, group in df.groupby('key1'):
    print(name)
    print(group)

print("+++++++++++++++++")
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print(k1, k2)
    print(group)

"""


# 利用分组生成字典
"""
pieces = dict(list(df.groupby('key1')))
print(pieces.keys())
print(pieces['b'])

"""


# 通过字典/series进行分组  等价
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['joe', 'steve', 'wes', 'jim', 'jack'])

people.ix[2:3, ['b', 'c']] = np.nan

mapping = {'a': 'red',
           'b': 'red',
           'c': 'blue',
           'd': 'blue',
           'e': 'red',
           'f': 'green'}

by_column = people.groupby(mapping, axis=1)

map_series = pd.Series(mapping)
by_column_series = people.groupby(map_series, axis=1)


# 通过函数进行分组
by_fun = people.groupby(len)


# 数据聚合，除内置函数count,mean, min，。。。可调用自定义函数(agg/aggregate)
def peak_to_peak(arr):
    return arr.max() - arr.min()


by_fun1 = df.groupby('key1').agg([peak_to_peak])


# 面向列的多函数应用  agg

tips = pd.read_csv('./pydata-book-master/ch08/tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

grouped = tips.groupby(['sex', 'smoker'])

grouped_pct = grouped['tip_pct'].agg(['mean', 'std', peak_to_peak])

grouped_pct1 = grouped['tip_pct'].agg([('foo', 'mean'), ('bar', np.std)])


# 分组与转换  transform
k1_means = df.groupby('key1').mean().add_prefix('means_')
new_df = pd.merge(df, k1_means, left_on='key1', right_index=True)

# 等价于
new_df1 = df.groupby('key1').transform(np.mean).add_prefix('means_')


# apply

def top(df, n=5, columns='tip_pct'):
    return df.sort_values(by=columns)[-n:]


# group_key=False   禁止分组建形成层次化索引
tip_apply = tips.groupby('smoker', group_keys=False).apply(top)

result = tips.groupby('smoker')['tip_pct'].apply(lambda x: x.describe())


# 分位数和桶分析  由cut,qcut得到的对象可直接用于groupby
frame = pd.DataFrame({'data1': np.random.randn(100),
                      'data2': np.random.randn(100)})
cat = pd.cut(frame['data1'], 4)


def get_stats(group):
    return {'min': group.min(),
            'max': group.max(),
            'count': group.count(),
            'mean': group.mean()}


grouped = frame['data2'].groupby(cat)
grouped1 = grouped.apply(get_stats).unstack()


if __name__ == '__main__':
    # print(df)
    # print(k1_means)
    # print(new_df)
    print(frame.head())
    print(grouped1)
    # print(result.unstack('smoker'))
