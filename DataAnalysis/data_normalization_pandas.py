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


# 数据转换
foods = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef',
                              'Bacon', 'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meet_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

# 利用映射进行数据转换， map修改对象本身
foods['animal'] = foods['food'].map(lambda x: meet_to_animal[x.lower()])


# replace 替换(值， 列表， 字典)，，产生新的对象
f1 = foods.iloc[:, 1].replace(5, np.nan)
f2 = foods.iloc[:, 1].replace([5, 6, 8], np.nan)
f3 = foods.iloc[:, 1].replace({5: np.nan, 12: 0})

# rename 轴索引替换
new_foods = foods.rename(columns=str.upper)
new_foods1 = foods.rename(index={1: 'one', 3: 'three'},
                          columns=str.upper)


# 数据离散化， 划分分组  cut,传入参数（bin边界， bin数量）
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 36, 60, 100]
group_name = ['youth', 'youthAdult', 'middle_Age', 'Senior']
cats = pd.cut(ages, bins, labels=group_name)

# qcut 按样本分位点划分
cats1 = pd.qcut(ages, 4)
# 统计各组数目
values = pd.value_counts(cats1)


# 异常值过滤   布尔型Dataframe 及any方法
data = pd.DataFrame(np.random.randn(1000, 4))

# 找出第3列绝对值大于3的行标索引
col = data[3]
col1 = col[np.abs(col) > 3]

# 找出任意列绝对值超过3的值的所有行标
data1 = data[(np.abs(data) > 3).any(1)]

# 排列和随机采样
df = pd.DataFrame(np.arange(5 * 4).reshape(5, 4))
sampler = np.random.permutation(4)


# take 选取指定行/列
df1 = df.take(sampler, axis=1)


# 计算指标/哑变量 get_dummies   将某一列派生成k列矩阵
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})

df_dummy = pd.get_dummies(df['key'])


df_with_dummy = df[['data1']].join(pd.get_dummies(df['key'], prefix='key'))


df2 = df.take(np.random.permutation(len(df))[: 3])

df3 = pd.get_dummies(cats)

if __name__ == '__main__':
    # print(df1)
    # print("++++++++++++++")
    # print(df2)
    # print("++++++++++++++")
    # print(df_merge_index)
    print(df)
    print("++++++++++++++")
    print(df_dummy)
    # print(df1)
    print("++++++++++++++")
    print(df3)