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
# 5、del df[列名]，删除列



if __name__ == "__main__":
    print(frame)
    print(frame_to_series1)