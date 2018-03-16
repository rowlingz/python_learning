# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np


# index指定索引
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# print(s.head())
# 返回数值和索引对象
val = s.values
index_s = s.index

# 切片索引
s1 = s['b']
s2 = s[['c', 'a', 'b']]

# numpy数组运算(boole过滤、标量乘法、应用数学函数等)
s3 = s[s > 1]
s4 = s * 2
s5 = np.exp(s)

# series 看作是字典
s6 = 'b' in s
s7 = 'f' in s

# 字典<====>series
dict1 = {'kile': 34, 'mary': 28, 'jone': 19, 'sky': 25}
conver_to_series1 = pd.Series(dict1)

states = ['jack', 'mary', 'sky']
conver_to_series2 = pd.Series(dict1, index=states)

# series 对象及其索引的name属性
conver_to_series2.name = 'age'
conver_to_series2.index.name = 'state'

# 可采用赋值的方式修改索引
s.index = ['jack', 'mary', 'sky']

##########################################
# dataframe

# columns指定列名
d = pd.DataFrame([[1, 2, 3], [3, 4, 5]], columns=['a', 'b', 'c'])
# print(d.head())


# 构建dataframe
data = {'state': ['ohio', 'ohio', 'nevada', 'nevada'],
        'year': [2000, 2001, 2002, 2001],
        'pop': [1.7, 2.4, 3.6, 2.9]}
frame = pd.DataFrame(data, columns=['year', 'pop', 'state', 'debt'],
                     index=['one', 'two', 'three', 'four'])

# dataframe 列转换为series
frame_to_series1 = frame['year']
frame_to_series2 = frame.state

# 获取行数据
frame_to_series1 = frame.ix[1]      # 等价于frame_to_series1 = frame.ix['two']

# 采用赋值的方式修改列：
# 1、赋单一值，全部转换
# 2、数组   长度要匹配
# 3、series 匹配索引后赋值
# 4、为不存在的列赋值，会创建新列

frame['debt'] = 5
frame['debt'] = np.arange(4)

val = pd.Series([1.2, 3, 6.7], index=['one', 'two', 'four'])
frame['debt'] = val

# 5、del df[列名]，删除列
del frame['debt']


# reindex 重新索引
obj = pd.Series([5, 9, 3], index=['a', 'b', 'c'])
obj2 = obj.reindex(['a', 'nn', 'c', 'ff'])
obj3 = obj.reindex(['a', 'nn', 'c', 'ff'], method='pad')

data_frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'b'], columns=['mary', 'kity', 'sum'])
frame1 = data_frame.reindex(['a', 'e', 'c', 'f'], fill_value=14)

frame2 = data_frame.reindex(columns=['kity', 'jack'])

frame3 = data_frame.reindex(index=['a', 'e', 'c', 'b'], columns=['kity', 'jack', 'mary'])


# 删除指定轴上的项 drop 得到新列
# 删除行
obj_drop = obj.drop('b')
frame_drop = data_frame.drop('a')

# 删除指定列
frame_drop1 = data_frame.drop('sum', axis=1)


# 函数
def f(x):
    return pd.Series([x.max(), x.min()], index=['max', 'min'])


frame_f = data_frame.apply(f, axis=1)

# 对行/列索引进行排序，得到新的对象，sort_index
frame_sort = data_frame.sort_index()        # 对行索引进行排序
frame_sort1 = data_frame.sort_index(axis=1, ascending=False)     # 对列索引进行排列

# 对数据结构中的值进行排序, sort_values
frame_sort_value = frame3.sort_values(by='kity')

# 求出值所在排名
obj_rank = obj.rank(ascending=False, method='first')
frame_rank = frame_f.rank(ascending=False)

# 索引是否唯一，返回True / False
index_unique = obj.index.is_unique
index_unique1 = frame.index.is_unique

# 仅出现一次的值
value_unique = obj.unique()
value_unique1 = frame1.iloc[:, 1].unique()
value_unique2 = frame1.apply(lambda x: len(x.unique()))

# 值计数 value_counts()
obj_counts = (obj * 2).value_counts()
frame_counts = frame1.iloc[:, 2].value_counts()
frame_counts1 = frame1.apply(lambda x: x.value_counts())

# isin 值是否包含在指定序列中  bool
obj_isin = obj.isin([3, 9])
frame_isin = frame1.isin([5, 7])

# 缺失值
frame_null = frame3.isnull()
obj_null = obj2.isnull()

# 滤掉缺失值 dropna()
obj_filter = obj2[obj2.notnull()]
obj_filter1 = obj2.dropna()

frame_filter = frame3.dropna()          # 删除含NA的行和列
frame_filter1 = frame3.dropna(how='all', axis=1)    # 删除全为NA的行/列
frame_filter2 = frame3.dropna(thresh=2)     # thresh ---int value : require that many non-NA values

# 填充 fillna()
obj_fillna = obj2.fillna(obj2.mean())
frame_fillna = frame3.fillna(method='ffill')
frame_fillna1 = frame3.fillna({'kity': 10, 'jack': 7})

# 层次化索引（多层索引）
multiIndex_data = pd.Series(np.random.randn(10),
                            index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                                   [1, 2, 3, 1, 2, 3, 1, 2, 1, 3]])




if __name__ == "__main__":
    # print(frame)
    # # print(frame_to_series1)
    # print(frame.values)
    # print('four' in frame.index)
    # print(obj2)
    # print("+++++++++++++++++")
    # print(obj_fillna)

    # print(data_frame)
    print(frame3)
    print(frame3.ix[:, 1])
    # print(frame_fillna1)

    # print(multiIndex_data)
    # print(multiIndex_data[:, 2])
    # print(multiIndex_data.unstack())